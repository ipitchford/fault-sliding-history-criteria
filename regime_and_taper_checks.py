#!/usr/bin/env python3
"""Regime map, finite-radius taper thresholds and persistence-time bound.

Checks (Sections 5, 7.3, 8 and 9 of the manuscript):
  1. first centre zero of the linear taper (d=0.6, T=L=1) for
     Theta in {0.01,...,10} and eps in {0, 0.02}; refinement study; the
     two-term finite-radius prediction with its rigorous remainder bracket;
  2. the all-time finite-radius taper threshold d_max(Theta) and the
     leading-order formula d_inf - kappa sqrt(Theta);
  3. the abrupt-drop tolerance (28) at realistic source widths eps/T;
  4. an illustrative dimensional example;
  5. the persistence-time bound after shut-in (Proposition 8.2).
Negative controls: an understated persistence bound must be contradicted by an
existing radius; a perturbed leading-order coefficient must miss d_max.
Dimensionless units: alpha = 1, q0 = 1, Theta = Delta/(f c_p q0).
Writes regime_and_taper_checks.json next to this file.
"""
from pathlib import Path
import json
import math
import sys
import time

import numpy as np
from scipy.optimize import brentq, minimize_scalar

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fault_core as fc  # noqa: E402

check = fc.check
C_UPPER = 0.4115           # certified in constants_and_two_term.py
D_INF = 0.5 / math.sqrt(2.0)


def margin(t, hist, theta, eps):
    R = fc.radius(t, hist, theta, eps)
    if R == 0.0:
        return float("nan"), 0.0
    return fc.centre_margin(t, hist, R, eps), R


def first_zero(fun, T=1.0, lo=1e-10, hi=0.95, n=90):
    ts = T + np.geomspace(lo, hi, n)
    prev = None
    for t in ts:
        v = fun(t)
        if v < 0:
            if prev is None:
                return None, ts
            return brentq(fun, prev, t, xtol=1e-13, rtol=4e-15), ts
        prev = t
    return None, ts


def taper_table():
    h = fc.taper_history(0.6)
    rows = []
    for eps in [0.0, 0.02]:
        for th in [0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
            row = {"Theta": th, "epsilon": eps}
            if eps > 0:
                pmax = max(fc.centre_pressure(t, h, eps) for t in np.linspace(0.05, 2.0, 80))
                if pmax <= th:
                    row.update({"status": "no slip: centre pressure stays below threshold",
                                "max_centre_pressure": pmax})
                    rows.append(row)
                    continue
            f = lambda t: margin(t, h, th, eps)[0]
            root, _ = first_zero(f)
            check(root is not None, "taper root found")
            R = fc.radius(root, h, th, eps)
            fracs = [0.01, 0.05, 0.1, 0.25, 0.5, 0.75, 0.95, 0.999]
            vel = [fc.interior_velocity(x * R, root, h, R, eps) for x in fracs]
            edge = fc.edge_response(root, h, R, eps)
            check(min(vel) > 0 and edge > 0, "noncentral and edge positivity at first zero")
            # two-term prediction with the exact radius, and the rigorous bracket
            def two(t, sign=0.0):
                Rt = fc.radius(t, h, th, eps)
                base = fc.A_STAR * fc.abel_half(t, h, eps) - 2.0 / Rt * float(h.value(t))
                return base + sign * 16 * C_UPPER / (3 * Rt ** 3) * fc.first_moment(t, h, eps)
            t2, _ = first_zero(lambda t: two(t))
            lo_b, _ = first_zero(lambda t: two(t, -1.0))
            hi_b, _ = first_zero(lambda t: two(t, +1.0))
            Bratio = (16 * C_UPPER / (3 * R ** 3) * fc.first_moment(root, h, eps)) / (2.0 / R)
            row.update({"first_zero": root, "R": R, "lambda": R / (2 * math.sqrt(root + eps)),
                        "q": float(h.value(root)),
                        "noncentral_velocities_at_fractions": dict(zip(map(str, fracs), vel)),
                        "edge_response": edge,
                        "two_term_root": t2, "remainder_over_correction": Bratio})
            if lo_b is not None and hi_b is not None and Bratio < 1:
                row["rigorous_bracket"] = [lo_b, hi_b]
                check(lo_b <= root + 1e-9 and root <= hi_b + 1e-9, "root inside bracket")
            if eps > 0:
                p0 = fc.centre_pressure(root, h, eps)
                row["centre_pressure_over_c_p_q0"] = p0
                row["required_f_sigma0_over_Delta_for_no_opening"] = p0 / th
            rows.append(row)
    return rows


def refinement(rows):
    """Recompute the roots with 48 instead of 24 nodes per panel."""
    h = fc.taper_history(0.6)
    fc.set_resolution(48)
    out = []
    for row in rows:
        if "first_zero" not in row:
            continue
        th, eps = row["Theta"], row["epsilon"]
        f = lambda t: margin(t, h, th, eps)[0]
        g = row["first_zero"]
        r2 = brentq(f, g - 1e-6 * (g - 1), g + 1e-6 * (g - 1) + 1e-12, xtol=1e-14)
        out.append({"Theta": th, "epsilon": eps, "root_24": g, "root_48": r2,
                    "difference": abs(r2 - g)})
    fc.set_resolution(24)
    check(max(o["difference"] for o in out) < 1e-9, "quadrature refinement")
    return out


def compare_original(rows):
    """Compare with the independent adaptive-quadrature implementation."""
    orig = json.loads((HERE / "numerics" / "verification_results.json").read_text())
    res = []
    for case in orig["linear_taper_cases"]:
        mine = next(r for r in rows if r["Theta"] == case["theta"]
                    and r["epsilon"] == case["epsilon"])
        res.append({"Theta": case["theta"], "epsilon": case["epsilon"],
                    "adaptive": case["first_zero"], "gauss_legendre": mine["first_zero"],
                    "difference": abs(case["first_zero"] - mine["first_zero"])})
    check(max(r["difference"] for r in res) < 2e-8, "agreement with adaptive implementation")
    return res


def inner_limit_roots():
    d, T, L = 0.6, 1.0, 1.0
    point = (T + math.sqrt(T * T + (L / d) ** 2)) / 2
    eps = 0.02
    f = lambda t: (t + eps) ** -0.5 - (d / L) * 2 * (math.sqrt(t - T + eps) - math.sqrt(eps))
    gauss = brentq(f, 1.0 + 1e-12, 2.0, xtol=1e-14)
    return {"point_source": point, "gaussian_eps_0.02": gauss}


def min_scaled_margin(d, th, eps=0.0):
    h = fc.taper_history(d)

    def f(t):
        R = fc.radius(t, h, th, eps)
        return fc.centre_margin(t, h, R, eps) / fc.K0(R, np.array([t + eps]))[0]
    ts = np.unique(np.r_[1 + np.geomspace(1e-7, 1.0, 40), 2 + np.geomspace(1e-6, 1.0, 15),
                         np.geomspace(3.0, 50.0, 15)])
    v = np.array([f(t) for t in ts])
    i = int(np.argmin(v))
    lo, hi = ts[max(i - 1, 0)], ts[min(i + 1, len(ts) - 1)]
    res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options={"xatol": 1e-10})
    if res.fun < v[i]:
        return float(res.fun), float(res.x)
    return float(v[i]), float(ts[i])


def leading_order(th, T=1.0, L=1.0):
    dinf = 0.5 * math.sqrt(L / (T + L))
    kappa = math.sqrt(L) / math.pi ** 1.5 * (1 - dinf) * math.sqrt(2.0 / (T + L * (1 - dinf / 2)))
    return dinf - kappa * math.sqrt(th), kappa


def taper_thresholds():
    rows = []
    for th in [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        lo, hi = 0.0, D_INF
        check(min_scaled_margin(D_INF, th)[0] < 0, "d_inf is inadmissible at finite radius")
        for _ in range(32):
            mid = (lo + hi) / 2
            if min_scaled_margin(mid, th)[0] >= 0:
                lo = mid
            else:
                hi = mid
        m, tm = min_scaled_margin(lo, th)
        lead, kappa = leading_order(th)
        rows.append({"Theta": th, "d_max": lo, "binding_time": tm,
                     "leading_order": lead, "kappa": kappa,
                     "difference": lo - lead})
        check(lo < D_INF, "strict finite-radius reduction of the taper threshold")
    small = [r for r in rows if r["Theta"] <= 0.1]
    check(all(abs(r["difference"]) < 0.05 * r["Theta"] for r in small),
          "leading-order taper threshold accurate to O(Theta)")
    # negative control: a coefficient 20% too small misses d_max by more than the O(Theta) error
    bad = [abs(r["d_max"] - (D_INF - 0.8 * r["kappa"] * math.sqrt(r["Theta"])))
           for r in small if r["Theta"] >= 0.01]
    check(all(b > 0.05 * r["Theta"] for b, r in zip(bad, [r for r in small if r["Theta"] >= 0.01])),
          "negative control: perturbed leading-order coefficient must be detected")
    return rows


def constant_rate_radius(th, eps, T=1.0):
    h = fc.step_history([1.0], [0.0])
    return fc.radius(T, h, th, eps)


def drop_tolerances():
    rows = []
    for th in [0.1, 1.0, 10.0]:
        for e in [0.02, 1e-4, 1e-6, 1e-8]:
            h = fc.step_history([1.0], [0.0])
            if fc.centre_pressure(1.0, h, e) <= th:
                rows.append({"Theta": th, "eps_over_T": e, "status": "not nucleated by T"})
                continue
            R = fc.radius(1.0, h, th, e)
            ratio = fc.K0(R, np.array([1.0 + e]))[0] / fc.K0(R, np.array([e]))[0]
            rows.append({"Theta": th, "eps_over_T": e, "R_over_sqrt_alpha_T": R,
                         "tolerated_relative_drop": ratio,
                         "sqrt_eps_over_T": math.sqrt(e / (1 + e))})
            check(0 < ratio < math.sqrt(e / (1 + e)) * 1.0000001, "drop tolerance below sqrt(eps/T)")
    return rows


def dimensional_example(dmax_rows):
    alpha, a_w, T_h = 0.1, 0.1, 6.0          # m^2/s, m, hours (illustrative)
    T = T_h * 3600.0
    eps_s = a_w ** 2 / (4 * alpha)             # 2 sqrt(alpha eps) = a_w
    e = eps_s / T
    ell = math.sqrt(4 * alpha * T)
    rows = []
    for th in [0.1, 1.0, 10.0]:
        h = fc.step_history([1.0], [0.0])
        R = fc.radius(1.0, h, th, e)
        ratio = fc.K0(R, np.array([1.0 + e]))[0] / fc.K0(R, np.array([e]))[0]
        out = {"Theta": th, "R_at_T_m": R * math.sqrt(alpha * T),
               "tolerated_abrupt_drop_percent": 100 * ratio,
               "persistence_bound_after_constant_stage_h": T_h * (1 + 1 / th)}
        dm = next((r["d_max"] for r in dmax_rows if r["Theta"] == th), None)
        out["taper_threshold_L_equals_T"] = dm
        for d in [0.6, 1.0]:
            hd = fc.taper_history(d)
            f = lambda t: margin(t, hd, th, e)[0]
            root, _ = first_zero(f)
            out[f"first_loss_time_h_taper_{d:g}"] = None if root is None else root * T_h
        rows.append(out)
    return {"alpha_m2_per_s": alpha, "wellbore_radius_m": a_w, "stage_hours": T_h,
            "epsilon_s": eps_s, "epsilon_over_T": e, "diffusion_length_m": ell,
            "inner_limit_taper_threshold": D_INF,
            "inner_limit_first_loss_h_d0.6": T_h * (1 + math.sqrt(1 + 1 / 0.36)) / 2,
            "inner_limit_first_loss_h_d1": T_h * (1 + math.sqrt(2.0)) / 2,
            "rows": rows, "status": "illustrative parameters, not a calibrated site"}


def persistence():
    """Smooth C1 taper to zero: q=1 on [0,1], q=cos^2(pi(s-1)/2) on [1,2], 0 after."""
    def value(s):
        s = np.asarray(s, dtype=float)
        mid = np.cos(np.pi * (s - 1.0) / 2.0) ** 2
        return np.where(s < 0, 0.0, np.where(s < 1.0, 1.0, np.where(s < 2.0, mid, 0.0)))
    h = fc.History([(0.0, 1.0)], [(1.0, 2.0, lambda s: -np.pi / 2 * np.sin(np.pi * (s - 1.0)))],
                   value)
    V, ts = 1.5, 2.0
    out = []
    for eps in [0.0, 0.02]:
        th = 0.1
        bound = ts + V / th - eps
        lower = V / th - eps
        # centre pressure after shut-in vs. the bound c_p V/(t-t_s+eps)
        tt = np.linspace(2.05, 30.0, 60)
        p = np.array([fc.history_integral(lambda u: 1.0 / u, t, _pressure_view(h), eps,
                                          sqrt_sub=False, scale=1.0) for t in tt])
        check(np.all(p <= V / (tt - ts + eps) + 1e-10), "centre pressure bound after shut-in")
        check(np.all(p >= V / (tt + eps) - 1e-10), "centre pressure lower bound")
        last = brentq(lambda t: fc.history_integral(lambda u: 1.0 / u, t, _pressure_view(h), eps,
                                                    sqrt_sub=False, scale=1.0) - th,
                      2.05, 40.0, xtol=1e-12)
        check(lower <= last <= bound, "last radius time inside the proved window")
        # the radius exists just before `last` and not after it
        check(fc.radius(last * 0.999, h, th, eps) > 0, "radius exists before last time")
        f = lambda t: margin(t, h, th, eps)[0]
        first, _ = first_zero(f, T=1.0, lo=1e-6, hi=0.99)
        check(first is not None and first < bound, "first loss before the persistence bound")
        # negative control: an understated bound t_s + 0.5 V/Theta is contradicted
        wrong = ts + 0.5 * V / th - eps
        check(fc.radius(wrong + 1.0, h, th, eps) > 0,
              "negative control: understated persistence bound must be contradicted")
        out.append({"epsilon": eps, "Theta": th, "V": V, "shut_in": ts,
                    "first_negative_centre_margin_time": first,
                    "last_time_radius_exists": last, "proved_window": [lower, bound]})
    return out


def _pressure_view(h):
    """History object whose atoms/pieces describe q itself (not dq):
    p(0,t)/c_p = int_0^t q(s)/(t-s+eps) ds is then history_integral(1/u)."""
    pieces = [(0.0, 1.0, lambda s: 1.0 + 0.0 * s),
              (1.0, 2.0, lambda s: np.cos(np.pi * (s - 1.0) / 2.0) ** 2)]
    return fc.History([], pieces, h.value)


def main():
    t0 = time.time()
    out = {"description": "Regimes, finite-radius taper thresholds, persistence bound; alpha=q0=1"}
    rows = taper_table()
    out["taper_first_zero_table"] = rows
    out["inner_limit_roots"] = inner_limit_roots()
    out["refinement"] = refinement(rows)
    out["comparison_with_adaptive_implementation"] = compare_original(rows)
    dmax = taper_thresholds()
    out["finite_radius_taper_thresholds"] = dmax
    out["abrupt_drop_tolerance"] = drop_tolerances()
    out["dimensional_example"] = dimensional_example(dmax)
    out["persistence_bound"] = persistence()
    out["runtime_seconds"] = time.time() - t0
    out["checks"] = "passed"
    (HERE / "regime_and_taper_checks.json").write_text(json.dumps(fc.round_sig(out), indent=2))
    print(json.dumps({"checks": "passed", "runtime_s": round(time.time() - t0, 1)}))


if __name__ == "__main__":
    main()
