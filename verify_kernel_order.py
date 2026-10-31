"""Independent numerical checks for the proved Dawson--Abel kernel order.

Run: python geology_research/verify_kernel_order.py
These checks illustrate, but do not replace, the analytic proof.
"""

from __future__ import annotations

import json
import math
from decimal import Decimal, getcontext, localcontext
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import dawsn


def check(condition, message="certificate check failed"):
    """Explicit check that still fails under python -O."""
    if not condition:
        raise SystemExit(message)


def kernel(r: float, u: float, R: float = 1.0, alpha: float = 1.0) -> float:
    """Remove the Abel endpoint singularity before adaptive quadrature."""
    length = math.sqrt(R * R - r * r)

    def integrand(y: float) -> float:
        x = math.sqrt((r * r + y * y) / (4 * alpha * u))
        return dawsn(x) / x if x else 1.0

    return quad(integrand, 0, length, epsabs=2e-13, epsrel=2e-13)[0] / u


def kernel_decimal(r: str, u: str, digits: int = 70) -> Decimal:
    """Independent high-precision beta-moment series; standard library only.

    For R=alpha=1, let I_n=int_0^1[r^2+(1-r^2)z^2]^n dz.
    Integration by parts gives I_n=(1+2n*r^2*I_(n-1))/(2n+1).
    Let b_n=(-lambda)^n E[(1-T^2)^n]/n!, so b_n/b_(n-1)
    equals -2lambda/(2n+1). Summing b_n*I_n computes M_r(lambda).
    Extra decimal precision covers alternating cancellation of size exp(lambda).
    """
    lam_float = 1 / (4 * float(u))
    with localcontext() as ctx:
        ctx.prec = digits + int(lam_float / math.log(10)) + 50
        rr, uu = Decimal(r), Decimal(u)
        lam = 1 / (4 * uu)
        moment, coefficient, total = Decimal(1), Decimal(1), Decimal(1)
        threshold = Decimal(10) ** (-digits - 25)
        for n in range(1, 10000):
            moment = (1 + 2*n*rr*rr*moment) / (2*n+1)
            coefficient *= -2 * lam / (2*n+1)
            term = coefficient * moment
            total += term
            if n > 2*lam_float + 10 and abs(term) < threshold:
                break
        else:
            raise RuntimeError("Moment series did not converge within 10000 terms")
        result = (1-rr*rr).sqrt() * total / uu
        ctx.prec = digits
        return +result


def edge_ratio(old: float, young: float) -> float:
    xo, xy = 1 / math.sqrt(4 * old), 1 / math.sqrt(4 * young)
    return (young / old) * (dawsn(xo) / xo) / (dawsn(xy) / xy)


def main() -> None:
    getcontext().prec = 80
    records: dict[str, object] = {}
    # Concrete refutation of stronger radial monotonicity.
    example = []
    for rs in ["0", "0.1", "0.2", "0.3", "0.5", "0.8", "0.99"]:
        r = float(rs)
        low = kernel(r, 0.01) / kernel(r, 0.001)
        high = kernel_decimal(rs, "0.01") / kernel_decimal(rs, "0.001")
        check(abs(low - float(high)) < 2e-12)
        example.append({"r": r, "scipy_ratio": low, "decimal_70_digit_series_ratio": str(high)})
    check(example[3]["scipy_ratio"] > example[4]["scipy_ratio"])
    records["radial_nonmonotonicity_example"] = example

    # A modest logarithmic grid covering six orders of magnitude in age.
    # Strictness of finite differences can be lost below machine precision;
    # the check allows a small round-off tolerance.
    radii = [0.01, 0.1, 0.3, 0.5, 0.8, 0.95, 0.999]
    ages = np.logspace(-5, 2, 100)
    centre = np.array([kernel(0, float(u)) for u in ages])
    minimum_increment = math.inf
    for r in radii:
        normalised = np.array([kernel(r, float(u)) for u in ages]) / centre
        increments = np.diff(normalised)
        minimum_increment = min(minimum_increment, float(increments.min()))
        check(increments.min() > -2e-12)
        check(normalised.max() < math.sqrt(1 - r * r))
    records["centre_order_grid"] = {
        "radii": radii,
        "age_count": len(ages),
        "age_min": float(ages[0]),
        "age_max": float(ages[-1]),
        "smallest_increment": minimum_increment,
        "violations": 0,
    }

    # Edge-normalised formula: direct numerical limit versus scalar Dawson limit.
    edge_results = []
    for old, young in [(10.0, 1.0), (1.0, 0.1), (0.1, 0.01), (0.01, 0.001)]:
        scalar = edge_ratio(old, young)
        sampled = kernel(1 - 1e-8, old) / kernel(1 - 1e-8, young)
        centre_ratio = kernel(0, old) / kernel(0, young)
        check(abs(sampled - scalar) < 3e-8)
        check(scalar > centre_ratio)
        edge_results.append({"old": old, "young": young, "scalar_limit": scalar,
                             "sample_at_1_minus_1e-8": sampled,
                             "centre_ratio": centre_ratio})
    records["edge_limit"] = edge_results

    # Three independent moments: beta-product formula against direct double integral.
    moment_results = []
    for r in [0.0, 0.5, 0.8]:
        for n in [1, 2, 3]:
            qmoment = 4**n * math.factorial(n)**2 / math.factorial(2*n + 1)
            formula = qmoment * sum(math.comb(n, k) * r**(2*(n-k))
                                    * (1-r*r)**k / (2*k+1) for k in range(n+1))
            integral = quad(lambda z: quad(lambda t: ((r*r+(1-r*r)*z*z)*(1-t*t))**n,
                                          0, 1)[0], 0, 1)[0]
            check(abs(formula - integral) < 1e-13)
            moment_results.append({"r": r, "n": n, "formula": formula, "integral": integral})
    records["moments"] = moment_results

    # Point-source centre and non-centre small-age constants.
    small_age = 1e-8
    centre_ratio = kernel(0, small_age) * math.sqrt(small_age) / (math.pi**1.5 / 2)
    r = 0.5
    noncentre_ratio = kernel(r, small_age) / (2 * math.acos(r) / r)
    check(abs(centre_ratio - 1) < 1e-4)
    check(abs(noncentre_ratio - 1) < 1e-6)
    records["small_age_constants"] = {"u": small_age, "centre_ratio_to_leading_term": centre_ratio,
                                       "r": r, "noncentre_ratio_to_limit": noncentre_ratio}

    output = Path(__file__).with_name("kernel_order_checks.json")
    output.write_text(json.dumps(records, indent=2) + "\n")
    print(json.dumps({"status": "passed", "output": str(output),
                      "monotonicity_smallest_increment": minimum_increment,
                      "counterexample_ratio_r03": example[3]["scipy_ratio"],
                      "counterexample_ratio_r05": example[4]["scipy_ratio"]}, indent=2))


if __name__ == "__main__":
    main()
