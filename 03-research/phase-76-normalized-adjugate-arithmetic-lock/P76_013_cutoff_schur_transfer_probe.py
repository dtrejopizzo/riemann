#!/usr/bin/env python3
"""Audit the exact two-boundary-mode transfer N-1 -> N."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


GAMMA_TEXT = "14.134725141734693790"


def row(t, indices, L):
    return mp.matrix([[1 / (t - 2 * mp.pi * n / L) for n in indices]])


def row_norm(r):
    return mp.sqrt(sum(abs(r[0, j]) ** 2 for j in range(r.cols)))


def transfer(H, indices, L, t):
    vals, vecs = mp.eigsy(H)
    mu = vals[0]
    xi = vecs[:, 0]
    inner = H[1:-1, 1:-1]
    boundary_cols = mp.matrix(H.rows - 2, 2)
    for i in range(H.rows - 2):
        boundary_cols[i, 0] = H[i + 1, 0]
        boundary_cols[i, 1] = H[i + 1, H.cols - 1]
    rin = row(t, indices[1:-1], L)
    rb = row(t, (indices[0], indices[-1]), L)
    T = rb - rin * (inner - mu * mp.eye(inner.rows)) ** -1 * boundary_cols
    vb = mp.matrix([xi[0], xi[xi.rows - 1]])
    rfull = row(t, indices, L)
    direct = (rfull * xi)[0]
    reduced = (T * vb)[0]
    return mu, vals[1] - vals[0], row_norm(T) / row_norm(rfull), abs(direct) / row_norm(rfull), abs(direct - reduced)


def run():
    mp.mp.dps = 70
    gamma = mp.mpf(GAMMA_TEXT)
    Hmax, idxmax, L = build_mp(6, 9, 70)
    print("P76.013 cutoff Schur transfer")
    print("N          mu          gap      ||Tg||       qgamma     ||Tnear||    identityErr")
    for n_modes in range(3, 10):
        offset = 9 - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        indices = idxmax[offset : len(idxmax) - offset]
        mu, gap, tc, qc, err = transfer(H, indices, L, gamma)
        _, _, tn, _, _ = transfer(H, indices, L, gamma + mp.mpf("0.125"))
        print(
            f"{n_modes:2d} {mp.nstr(mu,7):>12} {mp.nstr(gap,7):>12}"
            f" {mp.nstr(tc,7):>12} {mp.nstr(qc,7):>12}"
            f" {mp.nstr(tn,7):>12} {mp.nstr(err,5):>14}"
        )


if __name__ == "__main__":
    run()
