#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_224_cubic_sign_decomposition_probe import plus_sum  # noqa: E402


WINDOWS = [(12, 32), (16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]


def even_mode(idx, m):
    v = np.zeros(len(idx))
    if m == 0:
        hit = np.where(idx == 0)[0]
        if len(hit):
            v[hit[0]] = 1.0
    else:
        hp = np.where(idx == m)[0]
        hm = np.where(idx == -m)[0]
        if len(hp) and len(hm):
            v[hp[0]] = 1.0 / np.sqrt(2.0)
            v[hm[0]] = 1.0 / np.sqrt(2.0)
    return v


def subspace_coords(idx, k, bq, modes):
    cols = []
    for m in modes:
        v = even_mode(idx, m)
        v = v - np.dot(k, v) * k
        c = bq.T @ v
        if norm(c) > 1.0e-12:
            cols.append(c)
    if not cols:
        return np.zeros((bq.shape[1], 0))
    q, r = np.linalg.qr(np.column_stack(cols))
    keep = np.abs(np.diag(r)) > 1.0e-10
    return q[:, keep]


def restricted_min(a, q):
    if q.shape[1] == 0:
        return np.nan
    vals = eigvalsh(q.conj().T @ a @ q)
    return float(vals[0])


def run():
    print("E72.232 low-edge subspace Rayleigh probe")
    print("High block A_1; subspaces are Q-projected even Fourier modes.")
    print("lam fullMin min01 ratio01 min01E ratio01E min01EE ratio01EE")
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        a = plus_sum(lam, idx, L, bq, c_model, 0.60, 1)
        full_min = float(eigvalsh(0.5 * (a + a.conj().T))[0])
        edge = int(np.max(np.abs(idx)))
        q01 = subspace_coords(idx, k, bq, [0, 1])
        q01e = subspace_coords(idx, k, bq, [0, 1, edge])
        q01ee = subspace_coords(idx, k, bq, [0, 1, edge - 1, edge])
        m01 = restricted_min(a, q01)
        m01e = restricted_min(a, q01e)
        m01ee = restricted_min(a, q01ee)
        print(
            f"{lam:3.0f} {full_min:+.6e} "
            f"{m01:+.6e} {m01/full_min:.3f} "
            f"{m01e:+.6e} {m01e/full_min:.3f} "
            f"{m01ee:+.6e} {m01ee/full_min:.3f}",
            flush=True,
        )


if __name__ == "__main__":
    run()
