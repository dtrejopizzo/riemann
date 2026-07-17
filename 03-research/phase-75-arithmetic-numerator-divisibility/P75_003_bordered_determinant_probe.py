#!/usr/bin/env python3
"""P75.003: verify diagonal and adjugate bordered identities."""

import numpy as np
from numpy.linalg import det, eigh, norm


def adjugate(a):
    n = a.shape[0]
    out = np.empty_like(a, dtype=complex)
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(a, j, axis=0), i, axis=1)
            out[i, j] = ((-1) ** (i + j)) * det(minor)
    return out


def numerator(z, d, xi):
    return np.prod(z - d) * np.sum(xi / (z - d))


def run_case(tag, perturb=0.0):
    rng = np.random.default_rng(7503)
    n = 7
    idx = np.r_[np.arange(-n, 0), np.arange(1, n + 1)]
    d = 2.0 * np.pi * idx / 6.25

    q, _ = np.linalg.qr(rng.normal(size=(len(d), len(d))))
    eigs = np.linspace(-2.0, 3.0, len(d))
    eigs[0] = -5.0 + perturb
    h = q @ np.diag(eigs) @ q.T
    vals, vecs = eigh(h)
    mu = vals[0]
    xi = vecs[:, 0]
    a = h - mu * np.eye(len(d))
    adj = adjugate(a)
    tr_adj = np.trace(adj)

    print(f"{tag} mu={mu:.6f} tr_adj={tr_adj.real:.6e}")
    for z in [1.3, 4.7, 1.8 + 0.2j]:
        r = 1.0 / (z - d)
        c = np.dot(r, xi)
        lhs = abs(c) ** 2
        rhs = (np.conjugate(r) @ adj @ r) / tr_adj
        p_lhs = abs(numerator(z, d, xi)) ** 2
        p_rhs = abs(np.prod(z - d)) ** 2 * rhs
        p_rel = abs(p_lhs - p_rhs) / max(1.0, abs(p_lhs), abs(p_rhs))
        print(
            f"  z={z!s:12s} c_err={abs(lhs-rhs):.3e}"
            f" p_abs_err={abs(p_lhs-p_rhs):.3e} p_rel_err={p_rel:.3e}"
        )


def run():
    print("P75.003 bordered determinant / adjugate identity")
    run_case("generic")
    run_case("planted-like", perturb=0.37)


if __name__ == "__main__":
    run()
