#!/usr/bin/env python3
"""Run every check script with -I -O -B and fail if any of them fails.

Usage (from any directory):
  uv run --python 3.12 --with numpy==2.3.5 --with scipy==1.17.0 \
      --with matplotlib==3.10.8 python3 -I -B /path/to/run_checks.py

Each script uses explicit checks (no assert), so running under -O does not
disable them.  Outputs are written next to the scripts.  The figure script
runs last because it reads the JSON written by two earlier scripts.
"""
from pathlib import Path
import os
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
SCRIPTS = [
    "verify_kernel_order.py",
    "verify_fault_criterion.py",
    "mechanical_audit_checks.py",
    "reviewer_checks.py",
    "exploratory_transfer_checks.py",
    "verify_multipeak_example.py",
    "constants_and_two_term.py",
    "regime_and_taper_checks.py",
    "history_extension_checks.py",
    "make_extension_figure.py",
]


def main():
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1",
               MPLBACKEND="Agg", PYTHONDONTWRITEBYTECODE="1")
    failures = []
    for name in SCRIPTS:
        start = time.time()
        proc = subprocess.run([sys.executable, "-I", "-O", "-B", str(HERE / name)],
                              cwd=str(HERE), env=env, capture_output=True, text=True)
        elapsed = time.time() - start
        status = "ok" if proc.returncode == 0 else f"FAILED (exit {proc.returncode})"
        print(f"{name:34s} {status:18s} {elapsed:7.1f} s", flush=True)
        if proc.returncode != 0:
            failures.append(name)
            sys.stderr.write(proc.stdout[-2000:] + proc.stderr[-2000:] + "\n")
    if failures:
        print("FAILED: " + ", ".join(failures))
        sys.exit(1)
    print("All checks passed.")


if __name__ == "__main__":
    main()
