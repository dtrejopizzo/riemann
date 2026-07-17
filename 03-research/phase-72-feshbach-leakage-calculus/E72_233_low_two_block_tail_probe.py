#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402
from E72_232_low_edge_subspace_probe import subspace_coords  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def pos_cube(mat):
    vals = eigvalsh(0.5 * (mat + mat.conj().T))
    return float(np.sum(vals[vals > 1.0e-12] ** 3))


def neg_cube(mat):
    vals = eigvalsh(0.5 * (mat + mat.conj().T))
    return float(np.sum((-vals[vals < -1.0e-12]) ** 3))


def orth_complement(q, n):
    z = np.eye(n) - q @ q.conj().T
    u, s, _ = np.linalg.svd(z)
    return u[:, s > 1.0e-10]


def run():
    print("E72.233 low-two block/tail probe")
    print("P=Q-projected even Fourier modes {0,1}; R=P^perp.")
    print("lam minA minP negP posR negR ||PR||2 posA negA")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        a = 0.5 * (a + a.conj().T)
        p = subspace_coords(idx, k, bq, [0, 1])
        r = orth_complement(p, a.shape[0])
        app = p.conj().T @ a @ p
        arr = r.conj().T @ a @ r
        apr = p.conj().T @ a @ r
        vals = eigvalsh(a)
        print(
            f"{lam:3.0f} {vals[0]:+.6e} {eigvalsh(app)[0]:+.6e} "
            f"{neg_cube(app):.6e} {pos_cube(arr):.6e} {neg_cube(arr):.6e} "
            f"{norm(apr,2):.3e} {pos_cube(a):.6e} {neg_cube(a):.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
