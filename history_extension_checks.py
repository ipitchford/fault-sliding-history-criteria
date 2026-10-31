#!/usr/bin/env python3
"""Near-threshold, stepped and source-profile checks for the revision.

Checks (Sections 4, 5, 9 and Appendices B-D of the manuscript):
  1. a smooth two-dip point-source history tuned to a tangential centre zero
     (Theorem A with an earlier near-contact, contact and recovery);
  2. a stepped Gaussian schedule with downward and upward jumps (Theorem G');
  3. a point-source schedule with an upward jump (Theorem A');
  4. the one-sided asymptotic of a point-source downward jump;
  5. Gaussian scale mixtures (Proposition 3.3) and an annular-source
     counterexample to the instantaneous centre test.
Negative controls: overshooting the tuned dip depth or step size must give a
negative centre margin; the pairwise radial order (old/young ratio monotone in
r) must be detected as false; the annular source must violate the age order.
Dimensionless units alpha = q0 = 1.  Writes history_extension_checks.json.
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
FRACS = [0.01, 0.05, 0.1, 0.3, 0.6, 0.9, 0.99]


# ---------------------------------------------------------------- 1. two dips
def dip_history(kappa, centres=(1.0, 3.0)):
    def value(s):
        s = np.asarray(s, dtype=float)
        out = np.where(s < 0, 0.0, 1.0)
        for c in centres:
            x = s - c
            out = out - kappa * np.where((x >= 0) & (x <= 1), np.sin(np.pi * x) ** 2, 0.0)
        return out
    pieces = [(c, c + 1.0, (lambda s, c=c: -kappa * np.pi * np.sin(2 * np.pi * (s - c))))
              for c in centres]
    return fc.History([(0.0, 1.0)], pieces, value)


def dip_minimum(kappa, theta):
    h = dip_history(kappa)
    f = lambda t: fc.centre_margin(t, h, fc.radius(t, h, theta))
    ts = np.r_[np.linspace(1.05, 2.6, 32), np.linspace(3.05, 4.6, 32), np.linspace(4.7, 6.0, 8)]
    v = np.array([f(t) for t in ts])
    i = int(np.argmin(v))
    res = minimize_scalar(f, bounds=(ts[i - 1], ts[i + 1]), method="bounded",
                          options={"xatol": 1e-11})
    return float(min(res.fun, v[i])), float(res.x if res.fun < v[i] else ts[i]), ts, v


def near_threshold_point_source():
    theta = 0.05
    lo, hi = 0.0, 0.2
    for _ in range(44):
        mid = (lo + hi) / 2
        if dip_minimum(mid, theta)[0] >= 0:
            lo = mid
        else:
            hi = mid
    kappa = lo
    m, tmin, ts, v = dip_minimum(kappa, theta)
    check(-1e-10 < m < 1e-8, "tuned to a tangential centre zero")
    h = dip_history(kappa)
    R = fc.radius(tmin, h, theta)
    vel = [fc.interior_velocity(x * R, tmin, h, R) for x in FRACS]
    edge = fc.edge_response(tmin, h, R)
    check(min(vel) > 0 and edge > 0, "noncentral and edge velocities positive at tangential zero")
    first_dip = float(v[:32].min())
    later = [fc.centre_margin(t, h, fc.radius(t, h, theta)) for t in [4.8, 5.5, 6.0]]
    check(min(later) > 0, "recovery after the tangential zero")
    times = np.linspace(0.05, 6.0, 120)
    radii = np.array([fc.radius(t, h, theta) for t in times])
    check(np.all(np.diff(radii) > 0), "radius increases along the admissible branch")
    series = {"t": times.tolist(),
              "centre": [fc.centre_margin(t, h, R_) for t, R_ in zip(times, radii)],
              "edge": [fc.edge_response(t, h, R_) for t, R_ in zip(times, radii)],
              "q": h.value(times).tolist()}
    # negative control: 1% deeper dips lose full sliding
    m_bad = dip_minimum(1.01 * kappa, theta)[0]
    check(m_bad < 0, "negative control: deeper dip must give a negative centre margin")
    return {"Theta": theta, "kappa_tangential": kappa, "time_of_contact": tmin,
            "centre_margin_at_contact": m, "radius_at_contact": R,
            "noncentral_velocity_at_fractions": dict(zip(map(str, FRACS), vel)),
            "edge_response_at_contact": edge,
            "minimum_centre_margin_first_dip": first_dip,
            "centre_margin_after_recovery_t4.8_5.5_6": later,
            "negative_control_margin_with_1.01_kappa": m_bad,
            "series": series}


# ---------------------------------------------------------- 2. stepped Gaussian
def stepped_history(a):
    return fc.step_history([1.0, 1 - a, 1.0, 1 - a, 1.0], [0.0, 1.0, 2.0, 3.0, 4.0])


def stepped_scan(a, theta, eps, full=False):
    h = stepped_history(a)
    ts = np.unique(np.round(np.r_[np.linspace(0.01, 5.0, 100), [1.0, 2.0, 3.0, 4.0],
                                  1 + np.geomspace(1e-6, 0.9, 15),
                                  3 + np.geomspace(1e-6, 0.9, 15)], 10))
    rows = []
    for t in ts:
        R = fc.radius(t, h, theta, eps)
        if R == 0.0:
            continue
        right = fc.centre_margin(t, h, R, eps, closed=True)
        left = fc.centre_margin(t, h, R, eps, closed=False)
        rows.append((t, R, right, left))
    return h, rows


def stepped_gaussian():
    theta, eps = 0.1, 0.02
    lo, hi = 0.0, 0.2
    for _ in range(40):
        mid = (lo + hi) / 2
        _, rows = stepped_scan(mid, theta, eps)
        if min(r[2] for r in rows) >= 0:
            lo = mid
        else:
            hi = mid
    a_star = lo
    a = 0.9 * a_star
    h, rows = stepped_scan(a, theta, eps)
    check(min(min(r[2], r[3]) for r in rows) > 0, "stepped Gaussian: centre margins positive")
    radii = np.array([r[1] for r in rows])
    check(np.all(np.diff(radii) >= -1e-12), "stepped Gaussian: radius nondecreasing")
    interior_min = np.inf
    edge_min = np.inf
    for t, R, _, _ in rows[::6] + [r for r in rows if r[0] in (1.0, 2.0, 3.0, 4.0)]:
        for closed in (True, False):
            for x in [0.05, 0.3, 0.7, 0.95]:
                interior_min = min(interior_min,
                                   fc.interior_velocity(x * R, t, h, R, eps, closed=closed))
            edge_min = min(edge_min, fc.edge_response(t, h, R, eps, closed=closed))
    check(interior_min > 0 and edge_min > 0, "stepped Gaussian: noncentral and edge positive")
    # single-step tolerance (28) at t=1 versus the second, history-dependent step
    R1 = fc.radius(1.0, h, theta, eps)
    tol1 = fc.K0(R1, np.array([1.0 + eps]))[0] / fc.K0(R1, np.array([eps]))[0]
    _, bad = stepped_scan(1.05 * a_star, theta, eps)
    worst_bad = min(r[2] for r in bad)
    check(worst_bad < 0, "negative control: 5% larger steps must fail")
    tbad = next(r[0] for r in bad if r[2] == worst_bad)
    return {"Theta": theta, "epsilon": eps, "critical_step": a_star, "used_step": a,
            "single_step_tolerance_at_t1": tol1,
            "minimum_centre_margin": min(min(r[2], r[3]) for r in rows),
            "minimum_sampled_noncentral_velocity": interior_min,
            "minimum_sampled_edge_response": edge_min,
            "negative_control_minimum_margin": worst_bad, "negative_control_time": tbad,
            "series": {"t": [r[0] for r in rows], "centre_right": [r[2] for r in rows]}}


# ------------------------------------------------------ 3. point upward jump
def point_upward_jump():
    theta = 0.05
    kappa = 0.05

    def value(s):
        s = np.asarray(s, dtype=float)
        base = np.where(s < 0, 0.0, np.where(s < 1.0, 0.5, 1.0))
        x = s - 2.0
        return base - kappa * np.where((x >= 0) & (x <= 1), np.sin(np.pi * x) ** 2, 0.0)
    h = fc.History([(0.0, 0.5), (1.0, 0.5)],
                   [(2.0, 3.0, lambda s: -kappa * np.pi * np.sin(2 * np.pi * (s - 2.0)))], value)
    times = np.unique(np.round(np.r_[np.linspace(0.05, 4.0, 80), 1 - np.geomspace(1e-6, 0.1, 6),
                                     1 + np.geomspace(1e-6, 0.1, 6)], 10))
    times = times[np.abs(times - 1.0) > 0]
    vals, radii, edges, inter = [], [], [], np.inf
    for t in times:
        R = fc.radius(t, h, theta)
        radii.append(R)
        vals.append(fc.centre_margin(t, h, R))
        edges.append(fc.edge_response(t, h, R))
        for x in [0.1, 0.5, 0.9]:
            inter = min(inter, fc.interior_velocity(x * R, t, h, R))
    check(min(vals) > 0 and min(edges) > 0 and inter > 0, "upward jump: positivity")
    check(np.all(np.diff(radii) > 0), "upward jump: radius increases")
    R1 = fc.radius(1.0, h, theta)
    jump = fc.edge_response(1.0 + 1e-9, h, R1) - fc.edge_response(1.0 - 1e-9, h, R1)
    check(abs(jump - 0.5 * 2.0 / R1 ** 2) < 1e-6, "edge response jumps by a_j * 2/R^2")
    return {"Theta": theta, "dip_depth": kappa, "minimum_centre_margin": min(vals),
            "minimum_edge_response": min(edges), "minimum_sampled_noncentral": inter,
            "edge_jump_at_t1": jump, "predicted_edge_jump": 0.5 * 2.0 / R1 ** 2}


# ------------------------------------------------- 4. downward jump asymptotic
def downward_jump_asymptotic():
    theta, dq = 0.1, 0.3
    h = fc.step_history([1.0, 1.0 - dq], [0.0, 1.0])
    rows = []
    for hh in [1e-4, 1e-6, 1e-8, 1e-10]:
        t = 1.0 + hh
        R = fc.radius(t, h, theta)
        c = fc.centre_margin(t, h, R)
        rows.append({"h": hh, "centre_margin": c,
                     "scaled": c * math.sqrt(hh) / (-dq * fc.A_STAR)})
    check(abs(rows[-1]["scaled"] - 1) < 1e-4, "one-sided asymptotic of a downward jump")
    check(all(r["centre_margin"] < 0 for r in rows), "immediate loss after a downward jump")
    return {"Theta": theta, "drop": dq, "rows": rows}


# ------------------------------------------------------------ 5. source profile
def mixture_kernel(r, R, u, weights, widths):
    return sum(w * fc.Kr(r, R, u + e) for w, e in zip(weights, widths))


def age_order_violation(weights, widths, R=1.0, radii=(0.05, 0.2, 0.5, 0.8, 0.95)):
    ages = np.geomspace(1e-4, 1e2, 400)
    worst = np.inf
    best = None
    den = mixture_kernel(0.0, R, ages, weights, widths)
    for x in radii:
        phi = mixture_kernel(x * R, R, ages, weights, widths) / den
        # largest drop phi(u_o) - max_{u_y<u_o} phi(u_y)
        runmax = np.maximum.accumulate(phi)
        drop = phi - runmax
        j = int(np.argmin(drop))
        rel = float(drop[j] / phi.max())
        if rel < worst:
            worst = rel
            best = (x, ages[int(np.argmax(phi[:j + 1]))], ages[j])
    return worst, best


def source_profiles():
    out = {}
    mixtures = {"two_widths_1e-3_and_3": ([0.5, 0.5], [1e-3, 3.0]),
                "three_widths": ([0.2, 0.3, 0.5], [1e-4, 0.05, 5.0]),
                "point_plus_wide": ([0.5, 0.5], [0.0, 2.0])}
    for name, (w, e) in mixtures.items():
        worst, _ = age_order_violation(w, e)
        check(worst >= -1e-12, f"mixture {name}: centre-relative age order")
        out[name] = {"weights": w, "widths": e, "worst_relative_decrease": worst}
    # annular (difference-of-Gaussians) source: rho = (rho_ew - c rho_en)/(1-c), rho(0)=0
    ring = {}
    for name, (ew, en) in {"ring_0.1_0.01": (0.1, 0.01), "ring_0.02_0.01": (0.02, 0.01)}.items():
        cc = en / ew
        w, e = [1.0 / (1 - cc), -cc / (1 - cc)], [ew, en]
        rr = np.linspace(0, 3 * math.sqrt(ew), 400)
        dens = (np.exp(-rr ** 2 / (4 * ew)) / ew - cc * np.exp(-rr ** 2 / (4 * en)) / en)
        check(np.all(dens >= -1e-12), "annular source density nonnegative")
        worst, (x, uy, uo) = age_order_violation(w, e)
        check(worst < -1e-4, "negative control: annular source violates the age order")
        # explicit single-peaked two-atom counterexample on R = 1 at time t = u_o
        t = uo
        dq = (mixture_kernel(0.0, 1.0, np.array([uo]), w, e)[0]
              / mixture_kernel(0.0, 1.0, np.array([uy]), w, e)[0])
        hist = fc.step_history([1.0, 1.0 - dq], [0.0, t - uy])
        theta = sum(wi * fc.pressure_abel(1.0, t, hist, ei) for wi, ei in zip(w, e))
        aa = np.linspace(0.02, 0.98, 25)
        F = np.array([sum(wi * fc.pressure_abel(a, t, hist, ei) for wi, ei in zip(w, e))
                      for a in aa]) - theta
        check(np.all(F > 0), "trial slip positive inside the disk (F > 0 for a < R)")
        cen = (mixture_kernel(0.0, 1.0, np.array([uo]), w, e)[0]
               - dq * mixture_kernel(0.0, 1.0, np.array([uy]), w, e)[0])
        off = (mixture_kernel(x, 1.0, np.array([uo]), w, e)[0]
               - dq * mixture_kernel(x, 1.0, np.array([uy]), w, e)[0])
        check(abs(cen) < 1e-12 and off < 0, "annular counterexample: centre zero, ring negative")
        ring[name] = {"wide_width": ew, "narrow_width": en, "weight_ratio": cc,
                      "worst_relative_decrease": worst, "radius_fraction": x,
                      "young_age": uy, "old_age": uo, "drop": dq, "time": t,
                      "Theta_making_R_equal_1": theta,
                      "centre_velocity": cen, "offcentre_velocity": off}
    out["annular_sources"] = ring
    out["annular_trajectory"] = annular_trajectory(ring["ring_0.1_0.01"])
    # negative control: the pairwise radial order is false for a single Gaussian/point
    rr = np.linspace(0, 0.999, 151)
    ratio = np.array([fc.Kr(r, 1.0, np.array([0.01]))[0] / fc.Kr(r, 1.0, np.array([0.001]))[0]
                      for r in rr])
    check(not np.all(np.diff(ratio) >= 0), "negative control: pairwise radial order must fail")
    check(ratio.min() == ratio[0], "centre is the minimum of the old/young ratio")
    out["pairwise_radial_order"] = {"centre": ratio[0], "max": ratio.max(),
                                    "argmax_r": rr[int(np.argmax(ratio))], "rim": ratio[-1]}
    return out


def annular_trajectory(case):
    """Follow the annular example in time with the stress parameter fixed.

    Before the drop the history is a single positive step, so every kernel
    contribution is positive; we record where the radius equation has a single
    root, check that sampled velocities are positive there, and check that at
    the drop (right-continuous value) the ring reverses while the centre is
    still positive."""
    ew, en = case["wide_width"], case["narrow_width"]
    cc = en / ew
    w, e = [1.0 / (1 - cc), -cc / (1 - cc)], [ew, en]
    t_end, uy, dq, theta = case["time"], case["young_age"], case["drop"], case["Theta_making_R_equal_1"]
    td = t_end - uy
    hist = fc.step_history([1.0, 1.0 - dq], [0.0, td])

    def press(a, t):
        return sum(wi * fc.pressure_abel(a, t, hist, ei) for wi, ei in zip(w, e))

    def roots(t):
        aa = np.linspace(0.005, 5.0, 400)
        f = np.array([press(a, t) - theta for a in aa])
        idx = np.where(np.diff(np.sign(f)) != 0)[0]
        return [brentq(lambda a: press(a, t) - theta, aa[k], aa[k + 1], xtol=1e-13) for k in idx]

    def vel(r, t, R, closed=True):
        v = mixture_kernel(r, R, np.array([t]), w, e)[0]
        if t > td or (closed and t == td):
            v -= dq * mixture_kernel(r, R, np.array([t - td]), w, e)[0]
        return v
    rows = []
    for t in list(np.linspace(0.005, td, 12)[:-1]):
        rr = roots(t)
        row = {"t": t, "number_of_radius_roots": len(rr)}
        if len(rr) == 1:
            R = rr[0]
            vs = [vel(x * R, t, R) for x in np.linspace(0, 0.99, 60)]
            row.update({"R": R, "min_velocity": min(vs)})
        rows.append(row)
    single = [r for r in rows if r["number_of_radius_roots"] == 1]
    check(len(single) >= 3 and all(r["min_velocity"] > 0 for r in single),
          "annular: positive velocities while the radius root is unique before the drop")
    check(any(r["number_of_radius_roots"] > 1 for r in rows) or rows[0]["number_of_radius_roots"] == 0,
          "annular: early radius equation not single-rooted (recorded)")
    rr = roots(td)
    check(len(rr) == 1, "annular: unique radius at the drop")
    R = rr[0]
    centre = vel(0.0, td, R)
    xs = np.linspace(0, 0.99, 100)
    vs = np.array([vel(x * R, td, R) for x in xs])
    check(centre > 0 and vs.min() < 0, "annular: ring reverses at the drop while the centre is positive")
    return {"samples_before_drop": rows, "drop_time": td, "R_at_drop": R,
            "centre_velocity_at_drop": centre, "min_velocity_at_drop": float(vs.min()),
            "argmin_r_over_R": float(xs[int(np.argmin(vs))])}


def main():
    t0 = time.time()
    out = {"description": "History-class extensions and source profiles; alpha=q0=1"}
    out["near_threshold_two_dip_point_source"] = near_threshold_point_source()
    out["stepped_gaussian"] = stepped_gaussian()
    out["point_source_upward_jump"] = point_upward_jump()
    out["downward_jump_asymptotic"] = downward_jump_asymptotic()
    out["source_profiles"] = source_profiles()
    out["runtime_seconds"] = time.time() - t0
    out["checks"] = "passed"
    (HERE / "history_extension_checks.json").write_text(json.dumps(fc.round_sig(out), indent=2))
    print(json.dumps({"checks": "passed", "runtime_s": round(time.time() - t0, 1)}))


if __name__ == "__main__":
    main()
