#!/usr/bin/env python3
"""Locate the zeros of the two phase-free boundary transfer components."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp


def component_data(H, idx, side):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    boundary_pos = 0 if side < 0 else H.cols - 1
    db_index = idx[0] if side < 0 else idx[-1]
    b = mp.matrix([H[j + 1, boundary_pos] for j in range(H.rows - 2)])
    x = A ** -1 * b
    return db_index, idx[1:-1], x


def transfer_value(z, db_index, inner_idx, x, L):
    db = 2 * mp.pi * db_index / L
    return 1 / (z - db) - sum(x[j] / (z - 2 * mp.pi * inner_idx[j] / L) for j in range(x.rows))


def transfer_derivative(z, db_index, inner_idx, x, L):
    db = 2 * mp.pi * db_index / L
    return -1 / (z - db) ** 2 + sum(
        x[j] / (z - 2 * mp.pi * inner_idx[j] / L) ** 2 for j in range(x.rows)
    )


def run():
    mp.mp.dps = 80
    gamma = mp.mpf("14.134725141734693790")
    print("P76.017 roots of boundary transfer components")
    print("N side        T(gamma)       |Tprime|       root-gamma")
    for n_modes in (5, 6, 7, 8, 9):
        H, idx, L = build_mp(6, n_modes, 80)
        for side in (-1, 1):
            db, inner, x = component_data(H, idx, side)
            f = lambda z: transfer_value(z, db, inner, x, L)
            fp = lambda z: transfer_derivative(z, db, inner, x, L)
            root = mp.findroot(f, gamma, solver="newton", df=fp, tol=mp.mpf("1e-60"))
            print(
                f"{n_modes:2d} {side:+2d} {mp.nstr(f(gamma),10):>15}"
                f" {mp.nstr(abs(fp(gamma)),9):>14} {mp.nstr(root-gamma,12):>18}"
            )


if __name__ == "__main__":
    run()
