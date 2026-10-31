"""Reproduce the additional numerical checks made during the internal review.

The cap traction uses the real-space fractional Laplacian, independently of
the manuscript's Fourier--Bessel derivation. These finite checks support
normalisation and implementation, not the continuum proof or field validity.
"""
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import i0e

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import verify_fault_criterion as model


def main():
    out = {}
    cap = []
    for r in [1.1, 1.7, 3.0]:
        integral = quad(
            lambda rho: rho * math.sqrt(max(0, 1-rho*rho)) * quad(
                lambda phi: (r*r+rho*rho-2*r*rho*math.cos(phi))**(-1.5),
                0, 2*math.pi, epsabs=2e-10, epsrel=2e-10)[0],
            0, 1, epsabs=2e-9, epsrel=2e-9)[0]
        numerical = -integral/math.pi**2
        exact = 2/math.pi*(math.asin(1/r)-1/math.sqrt(r*r-1))
        cap.append(dict(r=r, real_space=numerical, formula=exact,
                        absolute_error=abs(numerical-exact)))
    out['exterior_cap_traction'] = cap

    # Polynomial Abel pair F(a)=1-a^2, g(r)=1-(3/2)r^2, R=1.
    exterior = []
    for r in [1.1, 2.0, 5.0]:
        def E(a):
            return 2/math.pi*(math.asin(a/r)-a/math.sqrt(r*r-a*a))
        left = quad(lambda a: 2*a*E(a), 0, 1, epsabs=2e-11)[0]-(1-1.5*r*r)
        right = -(1-r*r)+quad(lambda a: -2*a*E(a), 1, r, epsabs=2e-10)[0]
        exterior.append(dict(r=r, direct_gap=left, identity_gap=right,
                             absolute_error=abs(left-right)))
    out['exterior_complementarity_identity'] = exterior

    transfer = []
    alpha = 1.7
    for r, s in [(.3, .1), (1., 1.), (2.7, 10.)]:
        ratio = 2*math.sqrt(s/math.pi)*quad(
            lambda y: math.exp(-s*y*y)*float(i0e(r*r/(8*alpha*y*y))),
            0, np.inf, epsabs=1e-12, epsrel=1e-12)[0]
        phi = 2/math.pi*quad(
            lambda theta: math.exp(-r/math.sqrt(alpha)*math.sqrt(s)*math.sin(theta)),
            0, math.pi/2, epsabs=1e-12)[0]
        transfer.append(dict(r=r, s=s, laplace_ratio=ratio,
                             positive_mixture=phi, absolute_error=abs(ratio-phi)))
    out['limiting_transfer_identity'] = transfer

    out['arcsine_centre_residuals'] = [dict(
        t=t, H=1/math.sqrt(t)-2/math.pi*quad(
            lambda theta: 1/(1+(t-1)*math.sin(theta)**2),
            0, math.pi/2, epsabs=1e-13)[0]) for t in [1.01, 1.7, 10., 100.]]
    t = 1.5193169237762547
    R = model.radius(t, .1, .6, .02)
    out['one_recomputed_taper_case'] = dict(
        t=t, R=R, centre=model.velocity(0, t, R, .6, .02),
        at_0_2_R=model.velocity(.2*R, t, R, .6, .02))
    L = T = 1.
    dc = .5*math.sqrt(L/(T+L))
    out['linear_threshold'] = dict(
        d=dc, H_at_endpoint=1/math.sqrt(T+L)-2*dc/math.sqrt(L),
        H_1percent_above=1/math.sqrt(T+L)-2*dc*1.01/math.sqrt(L))
    (ROOT/'reviewer_checks.json').write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
