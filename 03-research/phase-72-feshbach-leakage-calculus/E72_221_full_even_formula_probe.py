#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair, even_basis  # noqa: E402
from E72_197_signed_green_word_probe import u_matrix  # noqa: E402


def full_even(idx, L, y):
    eb = even_basis(idx)
    eproj = eb @ eb.T
    u = u_matrix(idx, L, y)
    return float(np.real(np.trace(eproj @ u.conj().T @ eproj @ u @ eproj)))


def run():
    print("E72.221 full-even U_y formula probe")
    print("compares ||E U_y E||_HS^2 to qdim*(1-u)")
    print("lam qdim u fullEven qdim(1-u) diff rel")
    for lam, n_modes in [(12, 32), (16, 40), (20, 48), (24, 56)]:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        qdim = bq.shape[1] + 1  # even dimension before removing k
        for u in [0.1, 0.25, 0.5, 0.75, 0.9]:
            val = full_even(idx, L, u * L)
            model = qdim * (1.0 - u)
            diff = val - model
            rel = diff / max(abs(val), 1e-30)
            print(
                f"{lam:3.0f} {qdim:4d} {u:.2f} {val:.9e} {model:.9e} "
                f"{diff:+.3e} {rel:+.3e}",
                flush=True,
            )


if __name__ == "__main__":
    run()
