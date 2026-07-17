#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import weighted_even_matrix  # noqa: E402


def run():
    print("E72.131 shorting mass damping probe")
    print(
        " lam   L    dim  ||C^-1b||/||b||  L*gain  rayEig  rayEig/L  "
        "minEig  maxEig"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        mass_full = mask * (w.T @ np.ones(w.shape[0], dtype=complex))
        b = bq.T @ mass_full
        u = solve(c_actual, b)
        gain = norm(u) / max(norm(b), 1e-30)
        ray = abs(np.vdot(b, b) / np.vdot(b, u))
        evals = eigvalsh(c_actual)
        print(
            f"{lam:4.0f} {L:5.2f} {len(b):6d} "
            f"{gain:16.3e} {L*gain:8.3e} {ray:7.3e} {ray/L:9.3e} "
            f"{evals[0]:7.2e} {evals[-1]:7.2e}"
        )


if __name__ == "__main__":
    run()
