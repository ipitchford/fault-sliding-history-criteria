#!/usr/bin/env python3
"""Constants of the sharpened finite-radius bounds and the two-term expansion.

Checks (Section 7.3 and Appendix D of the manuscript):
  * s_* = sup_x x D(x)            (sharpened uniform tail constant)
  * c   = sup_x x^3 |D(x)-1/(2x)| (two-term remainder constant)
    Both are bounded by a grid with an explicit Lipschitz margin on [0,10]
    and by proved tail inequalities for x >= 10; one value is cross-checked
    with a 50-digit Decimal Taylor series of Dawson's integral.
  * K_R(0,u) = A_* u^{-1/2} - 2/R - rho,  |rho| <= 16 c u / (3 R^3)  (alpha=1)
  * the sharpened bound 0 <= K_inf(r,u)-K_R(r,u) <= 4 s_* arcsin(r/R)/r
  * the constant-rate radius map Theta = 2 int_lambda^inf D(z)/z^2 dz and its
    critically stressed / marginally pressurised asymptotes.
Negative controls: a wrong 1/R coefficient, a wrong remainder constant and the
old constant s_* = 1/2 must each be detected as violating a check.
Writes constants_and_two_term.json next to this file.
"""
from pathlib import Path
import json
import math
import sys
from decimal import Decimal, getcontext

import numpy as np
from scipy.special import dawsn
from scipy.integrate import quad
from scipy.optimize import brentq

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fault_core as fc  # noqa: E402

check = fc.check


def dawson_decimal(x, digits=50):
    """D(x) = sum_k (-1)^k 2^k x^(2k+1)/(2k+1)!!, evaluated in Decimal."""
    getcontext().prec = digits + 20
    x = Decimal(str(x))
    term = x
    total = x
    k = 0
    while True:
        k += 1
        term = term * (-2) * x * x / (2 * k + 1)
        total += term
        if abs(term) < Decimal(10) ** (-(digits + 5)):
            break
    return total


def grid_sup(fun, lipschitz, hi=10.0, n=1_000_001):
    """Upper bound for sup_[0,hi] |fun| from a grid plus a Lipschitz margin."""
    x = np.linspace(0.0, hi, n)
    h = x[1] - x[0]
    vals = np.abs(fun(x))
    pair_max = np.maximum(vals[:-1], vals[1:])
    bound = pair_max + lipschitz(x[1:]) * h / 2.0
    i = int(np.argmax(vals))
    return float(bound.max()), float(vals.max()), float(x[i])


def main():
    out = {"description": "Constants and two-term finite-radius expansion; alpha = 1"}

    # --- s_* = sup x D(x)
    s_fun = lambda x: x * dawsn(x)
    # |d/dx (xD)| = |D + x(1-2xD)| <= 1 + x  since 0 <= D <= min(x, 1/x) <= 1
    s_bound, s_grid, s_arg = grid_sup(s_fun, lambda x: 1.0 + x)
    # proved tail: x D(x) <= 1/2 + 1/(4x^2) + 2.1214/x^4 + 0.7072 x^2 e^{-x^2/2}
    tail_s = 0.5 + 1 / (4 * 100.0) + 2.1214 / 1e4 + 0.7072 * 100 * math.exp(-50.0)
    S_STAR_UPPER = 0.6424
    check(s_bound <= S_STAR_UPPER and tail_s < S_STAR_UPPER, "s_* bound")
    dec = float(dawson_decimal(s_arg)) * s_arg
    check(abs(dec - s_grid) < 1e-13, "Decimal Dawson cross-check (s_*)")

    # --- c = sup x^3 |D - 1/(2x)|
    c_fun = lambda x: x ** 3 * dawsn(x) - x ** 2 / 2.0
    # |E'| <= 3x^2 D + x^3 |1-2xD| + x <= 3x^2 + x^3 + x
    c_bound, c_grid, c_arg = grid_sup(c_fun, lambda x: 3 * x ** 2 + x ** 3 + x)
    tail_c = 0.25 + 2.1214 / 100.0 + 0.7072 * 1e4 * math.exp(-50.0)
    C_UPPER = 0.4115
    check(c_bound <= C_UPPER and tail_c < C_UPPER, "c bound")
    dec = float(dawson_decimal(c_arg)) * c_arg ** 3 - c_arg ** 2 / 2
    check(abs(dec - c_grid) < 1e-12, "Decimal Dawson cross-check (c)")
    # the tail inequalities themselves on a sample beyond 10
    xt = np.linspace(10.0, 60.0, 5001)
    lower = 1 / (2 * xt) + 1 / (4 * xt ** 3) - np.exp(-xt ** 2) * (1 / xt + 1 / xt ** 3)
    upper = 1 / (2 * xt) + 1 / (4 * xt ** 3) + 2.1214 / xt ** 5 + 0.7072 * xt * np.exp(-xt ** 2 / 2)
    check(np.all(dawsn(xt) >= lower - 1e-16) and np.all(dawsn(xt) <= upper + 1e-16),
          "tail inequalities for Dawson's integral")
    # explicit floating-point allowance for every grid evaluation of D:
    # compare SciPy's dawsn with an 80-digit Taylor series on 2001 points
    xs = np.linspace(0.0, 10.0, 2001)
    disc = max(abs(float(dawson_decimal(float(x), digits=80)) - float(dawsn(x))) for x in xs)
    EVAL_ALLOW = 1e-13
    check(disc < EVAL_ALLOW / 10, "observed Dawson evaluation error well inside the allowance")
    check(s_bound + 10.0 * EVAL_ALLOW <= S_STAR_UPPER, "s_* bound with evaluation allowance")
    check(c_bound + 1000.0 * EVAL_ALLOW <= C_UPPER, "c bound with evaluation allowance")
    out["evaluation_error"] = {"max_observed_abs_error_of_D_on_2001_points": disc,
                               "allowance_per_evaluation": EVAL_ALLOW,
                               "s_bound_with_allowance": s_bound + 10.0 * EVAL_ALLOW,
                               "c_bound_with_allowance": c_bound + 1000.0 * EVAL_ALLOW}
    out["constants"] = {"s_star_grid_max": s_grid, "s_star_argmax": s_arg,
                        "s_star_certified_upper": S_STAR_UPPER,
                        "c_grid_max": c_grid, "c_argmax": c_arg,
                        "c_certified_upper": C_UPPER,
                        "remainder_coefficient_16c_over_3": 16 * C_UPPER / 3,
                        "tail_bound_s_for_x_ge_10": tail_s,
                        "tail_bound_c_for_x_ge_10": tail_c}

    # --- two-term centre expansion and its remainder bound
    rows = []
    worst = 0.0
    worst_ctrl_coef = 0.0
    worst_ctrl_const = 0.0
    for R in [0.5, 1.0, 3.0, 10.0, 30.0]:
        u = np.geomspace(1e-6, 1e3, 400) * R * R
        k = fc.K0(R, u)
        two = fc.A_STAR / np.sqrt(u) - 2.0 / R
        bound = 16 * C_UPPER * u / (3 * R ** 3)
        ratio = np.abs(k - two) / bound
        worst = max(worst, float(ratio.max()))
        # negative control 1: wrong coefficient 1/R instead of 2/R
        bad = fc.A_STAR / np.sqrt(u) - 1.0 / R
        worst_ctrl_coef = max(worst_ctrl_coef, float((np.abs(k - bad) / bound).max()))
        # negative control 2: remainder constant 16/3 * 0.2 (too small)
        worst_ctrl_const = max(worst_ctrl_const,
                               float((np.abs(k - two) / (16 * 0.2 * u / (3 * R ** 3))).max()))
        # sharpened tail bound: 0 <= K_inf - K_R <= 4 s_* / R
        tail = fc.A_STAR / np.sqrt(u) - k
        check(np.all(tail >= -1e-13) and np.all(tail <= 4 * S_STAR_UPPER / R + 1e-13),
              "sharpened centre tail bound")
        sharp = float(tail.max() * R / 4)
        rows.append({"R": R, "max_abs_error_over_bound": float(ratio.max()),
                     "max_tail_times_R_over_4": sharp})
    check(worst <= 1.0, "two-term remainder bound")
    check(worst_ctrl_coef > 1.0, "negative control: wrong 1/R coefficient must fail")
    check(worst_ctrl_const > 1.0, "negative control: too-small remainder constant must fail")
    out["two_term_expansion"] = {"rows": rows, "max_error_over_bound": worst,
                                 "negative_control_wrong_coefficient_max_ratio": worst_ctrl_coef,
                                 "negative_control_small_constant_max_ratio": worst_ctrl_const}

    # --- sharpened off-centre bound K_inf(r,u) - K_R(r,u) <= 4 s_* arcsin(r/R)/r
    from scipy.special import i0e
    off = []
    worst_off = 0.0
    worst_old = 0.0
    for R in [1.0, 4.0]:
        for frac in [0.1, 0.5, 0.9]:
            r = frac * R
            u = np.geomspace(1e-4, 1e2, 120) * R * R
            kinf = fc.A_STAR / np.sqrt(u) * i0e(r * r / (8 * u))
            diff = kinf - fc.Kr(r, R, u)
            b = 4 * S_STAR_UPPER * math.asin(r / R) / r
            check(np.all(diff >= -1e-11), "off-centre tail nonnegative")
            worst_off = max(worst_off, float(diff.max() / b))
            # negative control 3: the asymptotic constant 1/2 is NOT a uniform bound
            worst_old = max(worst_old, float(diff.max() / (4 * 0.5 * math.asin(r / R) / r)))
            off.append({"R": R, "r_over_R": frac, "max_diff_over_bound": float(diff.max() / b)})
    check(worst_off <= 1.0, "sharpened off-centre bound")
    check(worst_old > 1.0, "negative control: s_* = 1/2 must be violated")
    out["sharpened_off_centre_bound"] = {"rows": off, "max_ratio": worst_off,
                                         "negative_control_half_constant_max_ratio": worst_old}

    # --- constant-rate radius map and asymptotes
    def theta_of(lam):
        if lam >= 1.0:
            return 2 * quad(lambda z: dawsn(z) / z ** 2, lam, np.inf, limit=400,
                            epsabs=1e-14, epsrel=1e-13)[0]
        # split off the 1/z singularity: D(z)/z^2 = 1/z + (D(z)/z - 1)/z
        tail = quad(lambda z: dawsn(z) / z ** 2, 1.0, np.inf, limit=400,
                    epsabs=1e-14, epsrel=1e-13)[0]
        near = quad(lambda z: (dawsn(z) / z - 1.0) / z, lam, 1.0, limit=400,
                    epsabs=1e-15, epsrel=1e-13)[0]
        return 2 * (math.log(1.0 / lam) + near + tail)
    lam_rows = []
    for th in [0.001, 0.01, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0]:
        lam = brentq(lambda l: theta_of(l) - th, 1e-12, 1e3, xtol=1e-15, rtol=1e-14)
        crit = 1 / math.sqrt(2 * th)
        marg = 0.5 * math.exp((2 - np.euler_gamma - th) / 2)
        lam_rows.append({"Theta": th, "lambda": lam,
                         "critically_stressed_asymptote": crit,
                         "marginally_pressurised_asymptote": marg})
    check(abs(lam_rows[0]["lambda"] / lam_rows[0]["critically_stressed_asymptote"] - 1) < 1e-3,
          "critically stressed asymptote")
    check(abs(lam_rows[-1]["lambda"] / lam_rows[-1]["marginally_pressurised_asymptote"] - 1) < 1e-6,
          "marginally pressurised asymptote")
    # the constant in the marginal asymptote: 2 - gamma - 2 log 2
    # check via the exponential-integral form Theta = A[E1(lambda^2 s^2)](1)
    from scipy.special import exp1
    lam = 1e-4
    # s = sin(phi) removes the endpoint singularity of the Abel weight
    lhs = quad(lambda p: exp1(lam * lam * math.sin(p) ** 2) * math.sin(p), 0, math.pi / 2,
               limit=400, epsabs=1e-13)[0]
    check(abs(lhs - theta_of(lam)) < 1e-9, "E1 and Dawson forms of the radius map agree")
    check(abs(lhs - (2 - np.euler_gamma - 2 * math.log(2 * lam))) < 1e-6,
          "marginal-asymptote constant")
    out["constant_rate_radius_map"] = lam_rows
    out["checks"] = "passed"
    (HERE / "constants_and_two_term.json").write_text(json.dumps(fc.round_sig(out), indent=2))
    print(json.dumps(fc.round_sig(out["constants"]), indent=2))


if __name__ == "__main__":
    main()
