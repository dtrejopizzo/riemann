#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def budget(vals):
    pos = vals[vals > 1.0e-12]
    neg = vals[vals < -1.0e-12]
    p3 = float(np.sum(pos**3))
    n3 = float(np.sum((-neg) ** 3))
    lead_neg = float((-neg[0]) ** 3) if len(neg) else 0.0
    lead_pos = float(pos[-1] ** 3) if len(pos) else 0.0
    return p3, n3, lead_neg, lead_pos, len(pos), len(neg)


def run():
    print("E72.229 cubic eigen-budget probe")
    print("A=sum plus cells; Tr(A^3)=posCube-negCube")
    print("lam block posCube negCube margin leadNegFrac leadPosFrac posCt negCt")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        for block in [0, 1]:
            a = plus_sum(lam, idx, L, bq, c_model, 0.60, block)
            vals = eigvalsh(0.5 * (a + a.conj().T))
            p3, n3, lead_neg, lead_pos, pc, nc = budget(vals)
            margin = n3 - p3
            lead_neg_frac = lead_neg / max(n3, 1.0e-300)
            lead_pos_frac = lead_pos / max(p3, 1.0e-300)
            print(
                f"{lam:3.0f} {block:5d} "
                f"{p3:.6e} {n3:.6e} {margin:+.6e} "
                f"{lead_neg_frac:.3f} {lead_pos_frac:.3f} {pc:5d} {nc:5d}",
                flush=True,
            )


if __name__ == "__main__":
    run()
