#!/usr/bin/env python3
"""Resolve the signed terms in the rank-two boundary transfer."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_011_loewner_identity_probe import symbols


def audit_boundary(H, idx, L, gamma, side):
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

    boundary_pos = 0 if side < 0 else H.cols - 1
    boundary_n = idx[0] if side < 0 else idx[-1]
    db = 2 * mp.pi * boundary_n / L
    sb = symbols(db, L, mp.mpf(6))[0]
    Rb = (D - db * mp.eye(D.rows)) ** -1
    source = s - sb * one
    r = mp.matrix([[1 / (gamma - 2 * mp.pi * n / L) for n in inner_idx]])

    alpha = (r * Rb * u)[0]
    beta = (r * Rb * v)[0]
    p = (v.T * Rb * source)[0]
    q = (u.T * Rb * source)[0]
    pole = 1 / (gamma - db)
    linear = (2 / L) * (alpha - sb * beta)
    wedge = (4 / (L * L)) * (alpha * p - beta * q)
    total = pole + linear + wedge

    boundary_col = mp.matrix([H[j + 1, boundary_pos] for j in range(H.rows - 2)])
    direct = pole - (r * invA * boundary_col)[0]
    return pole, linear, wedge, total, abs(total - direct)


def run():
    mp.mp.dps = 80
    gamma = mp.mpf("14.134725141734693790")
    print("P76.016 rank-two wedge audit")
    print("N side       |pole|       |linear|        |wedge|        |total|       identityErr")
    for n_modes in (6, 9):
        H, idx, L = build_mp(6, n_modes, 80)
        for side in (-1, 1):
            pole, linear, wedge, total, error = audit_boundary(H, idx, L, gamma, side)
            print(
                f"{n_modes:2d} {side:+2d} {mp.nstr(abs(pole),8):>12}"
                f" {mp.nstr(abs(linear),8):>14} {mp.nstr(abs(wedge),8):>14}"
                f" {mp.nstr(abs(total),8):>14} {mp.nstr(error,5):>17}"
            )


if __name__ == "__main__":
    run()
