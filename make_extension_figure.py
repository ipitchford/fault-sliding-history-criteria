#!/usr/bin/env python3
"""Second manuscript figure, drawn from the JSON written by
regime_and_taper_checks.py and history_extension_checks.py.

It recomputes nothing except closed-form reference curves, and checks that the
plotted data are the checked data (both JSON files must report "passed").
Writes numerics/extension_results.png and .pdf.
"""
from pathlib import Path
import json
import math
import os
import sys

os.environ.setdefault("MPLCONFIGDIR", "/tmp/geology-mpl")
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fault_core as fc  # noqa: E402

check = fc.check


def main():
    reg = json.loads((HERE / "regime_and_taper_checks.json").read_text())
    his = json.loads((HERE / "history_extension_checks.json").read_text())
    check(reg.get("checks") == "passed" and his.get("checks") == "passed",
          "figure data come from passing checks")
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "figure.facecolor": "#fffdf8", "axes.facecolor": "#fffdf8",
                         "savefig.facecolor": "#fffdf8", "axes.titleweight": "bold"})
    plum, ochre, moss, slate = "#78375d", "#b17721", "#55715a", "#536471"
    fig, axs = plt.subplots(2, 2, figsize=(11.5, 8.3), layout="constrained")

    rows = reg["finite_radius_taper_thresholds"]
    th = np.array([r["Theta"] for r in rows])
    dm = np.array([r["d_max"] for r in rows])
    ax = axs[0, 0]
    ax.semilogx(th, dm, "o-", color=plum, lw=2, label="Finite radius (exact test)")
    tt = np.geomspace(th.min(), 1.0, 100)
    kappa = rows[0]["kappa"]
    d_inf = 0.5 / math.sqrt(2)
    ax.semilogx(tt, d_inf - kappa * np.sqrt(tt), "--", color=ochre,
                label="Leading order  d∞ − κ√Θ")
    ax.axhline(d_inf, color=slate, lw=1, ls=":", label="Inner limit  d∞ = 1/(2√2)")
    ax.set(xlabel="Stress-injection parameter Θ", ylabel="Largest admissible taper depth d",
           title="A  Linear taper over L = T: admissible depth", ylim=(0, 0.4))
    ax.legend(frameon=False, fontsize=8)

    s = his["near_threshold_two_dip_point_source"]["series"]
    ax = axs[0, 1]
    t = np.array(s["t"])
    c = np.array(s["centre"])
    ax.plot(t, c / c.max(), color=plum, lw=2, label="Centre margin C(t) / max C")
    ax.plot(t, np.array(s["q"]), color=slate, lw=1.4, ls="--", label="Rate q(t)")
    ax.axhline(0, color="#817c74", lw=0.8)
    tc = his["near_threshold_two_dip_point_source"]["time_of_contact"]
    ax.axvline(tc, color=ochre, lw=0.8, ls=":")
    ax.set(xlabel="Time t", ylabel="Dimensionless value",
           title="B  Two dips: tangential centre zero, then recovery")
    ax.legend(frameon=False, fontsize=8, loc="lower left")

    s = his["stepped_gaussian"]["series"]
    ax = axs[1, 0]
    ax.plot(s["t"], s["centre_right"], ".", ms=3, color=moss,
            label="Right-continuous centre margin (normalised)")
    ax.axhline(0, color="#817c74", lw=0.8)
    for x in [1, 2, 3, 4]:
        ax.axvline(x, color="#cfc8bd", lw=0.6)
    ax.set(xlabel="Time t (rate steps at t = 1, 2, 3, 4)", ylabel="H(t)",
           title="C  Stepped Gaussian schedule (ε = 0.02, Θ = 0.1)")
    ax.legend(frameon=False, fontsize=8)

    ax = axs[1, 1]
    drops = [r for r in reg["abrupt_drop_tolerance"] if "tolerated_relative_drop" in r]
    for theta, col in [(0.1, plum), (1.0, ochre), (10.0, moss)]:
        rr = [r for r in drops if r["Theta"] == theta]
        if rr:
            ax.loglog([r["eps_over_T"] for r in rr], [r["tolerated_relative_drop"] for r in rr],
                      "o-", color=col, label=f"Θ = {theta:g}")
    ee = np.geomspace(1e-8, 0.02, 50)
    ax.loglog(ee, np.sqrt(ee / (1 + ee)), ":", color=slate, label="Upper bound √(ε/(T+ε))")
    ax.set(xlabel="Source width ε / T", ylabel="Tolerated abrupt drop Δq / q₀",
           title="D  Abrupt-drop tolerance versus source width")
    ax.legend(frameon=False, fontsize=8)

    fig.suptitle("Finite-radius thresholds and extended history classes\n"
                 "Dimensionless: α = q₀ = 1, time in units of the first stage T",
                 fontsize=13, weight="bold")
    out = HERE / "numerics"
    fig.savefig(out / "extension_results.png", dpi=190)
    fig.savefig(out / "extension_results.pdf")
    plt.close(fig)
    print(json.dumps({"checks": "passed", "figure": str(out / "extension_results.png")}))


if __name__ == "__main__":
    main()
