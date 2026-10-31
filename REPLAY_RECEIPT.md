# Replay receipt

## Lead clean replay of the original bundle (31 October 2026, before revision)

All six original scripts were rerun from a fresh extraction of the original handoff archive with Python 3.12, NumPy 2.3.5, SciPy 1.17.0 and Matplotlib 3.10.8. All passed; outputs equalled the retained ones up to last-place floating-point differences. Two scripts needed sibling-import fixes to run in isolated mode, and assertion-based checks were replaced by explicit checks; both changes are in this package.

## Release replay (31 October 2026, this package before freezing)

Command: `python3 -I -B tools/replay_compare.py <package-root>` in a CPython 3.12.11 environment with the pinned packages (`requirements.txt`), macOS 27 (arm64). The comparer copies the package to a temporary directory and runs `run_checks.py`, which runs each of the ten scripts with `-I -O -B`.

| Script | Result | Time (s) |
|---|---|---|
| verify_kernel_order.py | ok | 5 |
| verify_fault_criterion.py | ok | 31 |
| mechanical_audit_checks.py | ok | 2 |
| reviewer_checks.py | ok | 2 |
| exploratory_transfer_checks.py | ok | 3 |
| verify_multipeak_example.py | ok | 8 |
| constants_and_two_term.py | ok | 2 |
| regime_and_taper_checks.py | ok | 51 |
| history_extension_checks.py | ok | 14 |
| make_extension_figure.py | ok | 4 |

All checks passed, including every internal semantic negative control. The regenerated JSON outputs equal the retained ones in every non-timing field (1,472 numeric and 12 non-numeric leaves compared; zero numeric differences); only recorded run times differ. Figures were regenerated (PNG byte-identical; PDF differs only in embedded metadata). No unexpected files were written and the package root was unchanged.

## Frozen-archive replay

The same comparer is rerun by the publication gate plan from a fresh extraction of the frozen release ZIP; that receipt is kept with the publication records (it cannot be inside the archive it checks). GitHub Actions repeats the replay on Linux for every push ([.github/workflows/replay.yml](.github/workflows/replay.yml)).
