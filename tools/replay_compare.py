# SPDX-License-Identifier: MIT
"""Clean replay of a package root (read-only on ROOT) in a temp copy.
Runs run_checks.py (children -I -O -B), requires exit 0 and 'All checks passed.', then compares every
regenerated JSON output with the retained one (numbers: rel 1e-7 / abs 1e-10; volatile timing keys ignored),
requires that no unexpected files appear and that ROOT is unchanged. Usage: replay_compare.py ROOT [--keep DIR]"""
import hashlib, json, math, os, shutil, subprocess, sys, tempfile
from pathlib import Path
root = Path(sys.argv[1]).resolve()
keep = Path(sys.argv[sys.argv.index('--keep') + 1]) if '--keep' in sys.argv else None
VOLATILE = {'runtime_seconds', 'elapsed', 'elapsed_s', 'elapsed_seconds', 'seconds', 'runtime', 'runtime_s', 'wall_time', 'timestamp', 'generated_at', 'date', 'time_s', 'duration_s', 'python', 'python_version', 'platform', 'numpy', 'scipy', 'matplotlib', 'versions', 'environment', 'host', 'cwd', 'script_path'}
def tree(p): return {q.relative_to(p).as_posix(): hashlib.sha256(q.read_bytes()).hexdigest() for q in p.rglob('*') if q.is_file() and not q.relative_to(p).as_posix().startswith('.git/')}
def cmp(a, b, path, diffs, stats):
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b): diffs.append(f'{path}: keys differ {sorted(set(a) ^ set(b))[:5]}')
        for k in set(a) & set(b):
            if k in VOLATILE: stats['volatile'] += 1; continue
            cmp(a[k], b[k], f'{path}.{k}', diffs, stats)
    elif isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b): diffs.append(f'{path}: length {len(a)} vs {len(b)}'); return
        for i, (x, y) in enumerate(zip(a, b)): cmp(x, y, f'{path}[{i}]', diffs, stats)
    elif isinstance(a, bool) or isinstance(b, bool) or not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        stats['exact'] += 1
        if a != b: diffs.append(f'{path}: {str(a)[:60]!r} vs {str(b)[:60]!r}')
    else:
        stats['numeric'] += 1
        if a == b: return
        if isinstance(a, float) and isinstance(b, float) and (math.isnan(a) and math.isnan(b)): return
        if not math.isclose(a, b, rel_tol=1e-7, abs_tol=1e-10): diffs.append(f'{path}: {a!r} vs {b!r}')
        else: stats['last_place'] += 1
before = tree(root)
with tempfile.TemporaryDirectory(prefix='fault-replay-') as td:
    w = Path(td) / 'pkg'; shutil.copytree(root, w, ignore=shutil.ignore_patterns('.git'))
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', MPLBACKEND='Agg', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
    r = subprocess.run([sys.executable, '-I', '-B', str(w / 'run_checks.py')], cwd=w, capture_output=True, text=True, env=env, timeout=3600)
    print(r.stdout.strip())
    if r.returncode or 'All checks passed.' not in r.stdout: sys.exit(f'FAIL run_checks exit {r.returncode}: {r.stderr[-2000:]}')
    after = tree(w)
    extra = sorted(set(after) - set(before))
    if extra: sys.exit(f'FAIL replay wrote unexpected files: {extra}')
    changed = sorted(k for k in before if after.get(k) != before[k])
    diffs, stats, njson = [], dict(exact=0, numeric=0, last_place=0, volatile=0), 0
    for k in changed:
        if k.endswith('.json'):
            njson += 1
            cmp(json.loads((root / k).read_text()), json.loads((w / k).read_text()), k, diffs, stats)
        elif not k.endswith(('.png', '.pdf')):
            diffs.append(f'{k}: non-JSON, non-figure output changed')
    if keep: shutil.copytree(w, keep)
    print(f'changed outputs: {changed}')
    print(f'JSON compared: {njson} changed files; leaves exact={stats["exact"]} numeric={stats["numeric"]} (last-place differences {stats["last_place"]}); volatile keys skipped {stats["volatile"]}')
    if diffs: print('\n'.join(diffs[:40])); sys.exit(f'FAIL {len(diffs)} differences beyond tolerance')
if tree(root) != before: sys.exit('FAIL root changed')
print('PASS clean replay: run_checks.py (all scripts -I -O -B, explicit checks and internal negative controls) passed; regenerated JSON equals retained within rel 1e-7 (figures regenerated, not byte-compared); no unexpected files; root unchanged')
