#!/usr/bin/env python3
"""Verify the rank-two inverse-displacement boundary formula."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols


def frobenius(M):
    return mp.sqrt(sum(abs(M[i, j]) ** 2 for i in range(M.rows) for j in range(M.cols)))


def run():
    mp.mp.dps = 70
    H, idx, L = build_mp(6, 7, 70)
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    inner_idx = idx[1:-1]
    D = mp.diag([2 * mp.pi * n / L for n in inner_idx])
    s = mp.matrix([symbols(2 * mp.pi * n / L, L, mp.mpf(6))[0] for n in inner_idx])
    one = mp.matrix([1 for _ in inner_idx])
    invA = A ** -1
    u = invA * s
    v = invA * one

    displacement = D * invA - invA * D
    rank_two = (2 / L) * (u * v.T - v * u.T)
    disp_error = frobenius(displacement - rank_two) / frobenius(displacement)

    boundary_col = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
    db = 2 * mp.pi * idx[-1] / L
    sb = symbols(db, L, mp.mpf(6))[0]
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = s - sb * one
    direct_x = invA * boundary_col
    generated_x = (
        -(2 / L) * Rb * (u - sb * v)
        -(4 / (L * L)) * Rb * (u * v.T - v * u.T) * Rb * source
    )
    x_error = mp.sqrt(sum(abs(direct_x[j] - generated_x[j]) ** 2 for j in range(direct_x.rows)))
    x_scale = mp.sqrt(sum(abs(direct_x[j]) ** 2 for j in range(direct_x.rows)))

    print("P76.015 rank-two displacement transfer")
    print("inverse_displacement_relative_error", mp.nstr(disp_error, 10))
    print("boundary_generator_relative_error", mp.nstr(x_error / x_scale, 10))


if __name__ == "__main__":
    run()
