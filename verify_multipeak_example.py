#!/usr/bin/env python3
"""One synthetic smooth, multi-peak history for both source types.

Uses the exact pressure convolution, a fresh scalar radius inversion and
separate centre/edge integrals. Finite samples are implementation checks;
they do not certify continuous-time positivity or replace the theorem.
"""
from pathlib import Path
import json
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_fault_criterion import h, kernel, G, GINF


def check(condition, message="certificate check failed"):
    """Explicit check that still fails under python -O."""
    if not condition:
        raise SystemExit(message)

ROOT = Path(__file__).resolve().parent
THETA = 0.05


def rate(t):
    return 1.0 + 0.1 * np.sin(np.pi * t)


def derivative(t):
    return 0.1 * np.pi * np.cos(np.pi * t)


def abel_impulse(a, u):
    return 2.0 / (a * a) if u == 0 else float(h(a, u))


def pressure_average(a, t, epsilon=0.0):
    if a == 0:
        return quad(lambda u: rate(t-u)/(u+epsilon), 0, t,
                    epsabs=3e-12, epsrel=3e-12)[0]
    return quad(lambda u: rate(t-u) * abel_impulse(a, u+epsilon), 0, t,
                epsabs=3e-11, epsrel=3e-11, limit=150)[0]


def solve_radius(t, epsilon=0.0):
    low, high = 0.01*np.sqrt(t), 64*np.sqrt(t)
    return brentq(lambda a: pressure_average(a, t, epsilon)-THETA,
                  low, high, xtol=2e-11, rtol=2e-12)


def centre(t, radius, epsilon=0.0):
    def integrand(y):
        if epsilon == 0:
            return 4 * (GINF if y == 0 else G(radius/(2*y))) * derivative(t-y*y)
        return 2*y*kernel(0, y*y+epsilon, radius)*derivative(t-y*y)
    return kernel(0, t+epsilon, radius) + quad(integrand, 0, np.sqrt(t),
                                      epsabs=3e-10, epsrel=3e-10)[0]


def edge(t, radius, epsilon=0.0):
    return abel_impulse(radius, t+epsilon) + quad(
        lambda u: abel_impulse(radius, u+epsilon)*derivative(t-u), 0, t,
        epsabs=3e-11, epsrel=3e-11)[0]


def interior(t, radius, fraction, epsilon=0.0):
    r = fraction*radius
    return kernel(r, t+epsilon, radius) + quad(
        lambda u: kernel(r, u+epsilon, radius)*derivative(t-u), 0, t,
        epsabs=2e-9, epsrel=2e-9)[0]


def run_case(epsilon):
    times = np.unique(np.round(np.r_[np.geomspace(0.005, 0.2, 10),
                           np.linspace(0.2, 6, 59),
                           [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]], 12))
    birth = None
    if epsilon > 0:
        birth = brentq(lambda t: pressure_average(0, t, epsilon)-THETA,
                       0, 0.005, xtol=2e-14, rtol=2e-13)
        check(birth < 0.5)  # q is increasing on this whole initial interval.
        times = np.unique(np.r_[times, birth+np.array([0.0001, 0.0005, 0.001])])
    rows = []
    for t in times:
        radius = solve_radius(t, epsilon)
        rows.append({'t': float(t), 'q': float(rate(t)), 'R': radius,
                     'C': centre(t, radius, epsilon), 'edge_F_t': edge(t, radius, epsilon),
                     'radius_equation_residual': pressure_average(radius,t,epsilon)-THETA})
    spatial = []
    for t in [1.5, 3.5, 5.5, 6.0]:
        radius = solve_radius(t, epsilon)
        for fraction in [0.05, 0.2, 0.4, 0.6, 0.8, 0.97]:
            spatial.append({'t': t, 'r_over_R': fraction,
                            'velocity': interior(t, radius, fraction, epsilon)})
    result = {
        'history': 'q(t)=1+0.1*sin(pi*t), 0<=t<=6; causal initial atom 1 at 0',
        'model': 'alpha=1; f*c_p=1; Delta=0.05',
        'epsilon': epsilon,
        'nucleation_time': birth,
        'velocity_normalisation': 'common positive 4*f*c_p/(pi*mu) omitted',
        'qualification': 'Finite numerical samples; no interval certificate of all-time signs.',
        'sampled_times': len(rows),
        'minimum_sampled_centre': min(x['C'] for x in rows),
        'minimum_sampled_edge_F_t': min(x['edge_F_t'] for x in rows),
        'minimum_sampled_radius_increment': min(np.diff([x['R'] for x in rows])),
        'max_radius_equation_residual': max(abs(x['radius_equation_residual']) for x in rows),
        'minimum_sampled_interior_velocity': min(x['velocity'] for x in spatial),
        'final_radius': rows[-1]['R'],
        'rows': rows,
        'interior_samples': spatial,
    }
    check(result['minimum_sampled_centre'] > 0)
    check(result['minimum_sampled_edge_F_t'] > 0)
    check(result['minimum_sampled_radius_increment'] > 0)
    check(result['minimum_sampled_interior_velocity'] > 0)
    check(result['max_radius_equation_residual'] < 1e-9)
    if birth is not None:
        result['centre_pressure_derivative_at_birth'] = (
            1/(birth+epsilon) + quad(lambda u: derivative(birth-u)/(u+epsilon),
                                     0, birth, epsabs=1e-12)[0])
        check(result['centre_pressure_derivative_at_birth'] > 0)
        result['startup_condition'] = (
            'q is increasing on [0,0.5], and the transverse first birth is before 0.005.')
    return result


def main():
    result = run_case(0.0)
    gaussian = run_case(0.02)
    result['gaussian_case'] = gaussian
    (ROOT/'numerics'/'multipeak_example.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({
        'point': {k:v for k,v in result.items() if k not in ('rows','interior_samples','gaussian_case')},
        'gaussian': {k:v for k,v in gaussian.items() if k not in ('rows','interior_samples')},
    }, indent=2))


if __name__ == '__main__':
    main()
