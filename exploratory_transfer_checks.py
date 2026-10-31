"""Finite numerical checks of the prospective causal transfer.

The prescribed radius paths need not solve the fault radius equation. This
checks a finite matrix identity and signs, not a continuum theorem or a
physical source history. Decreasing-path cases are probes, not claimed
counterexamples or extensions.
"""
import json
from pathlib import Path

import numpy as np
from scipy.linalg import solve_triangular

import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_fault_criterion import kernel


def main():
    n = 48
    times = np.linspace(1/n, 1, n)
    epsilon = .04
    paths = {
        'fixed': np.ones(n),
        'linear_increase': .3+1.7*times,
        'sqrt_birth': 2*np.sqrt(times),
        'rapid_late_increase': .3+2*times**6,
        'linear_decrease': 2-1.7*times,
        'rapid_late_collapse': np.where(times < .8, 2., .2),
    }
    out = []
    for name, radii in paths.items():
        matrix = np.zeros((n, n))
        for i in range(n):
            for j in range(i+1):
                matrix[i,j] = kernel(0, times[i]-times[j]+epsilon, radii[i])
        for fraction in [.1, .5, .9]:
            r = fraction*radii[-1]
            row = np.array([kernel(r, times[-1]-s+epsilon, radii[-1]) for s in times])
            weights = solve_triangular(matrix.T, row, lower=False)
            out.append({
                'path': name,
                'radius_fraction': fraction,
                'epsilon': epsilon,
                'N': n,
                'minimum_weight': float(weights.min()),
                'negative_weights': int((weights < -1e-12).sum()),
                'min_index': int(weights.argmin()),
                'max_reconstruction_error': float(np.max(np.abs(weights@matrix-row))),
            })
    path = Path(__file__).resolve().parent/'exploratory_transfer_checks.json'
    path.write_text(json.dumps(out, indent=2))
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
