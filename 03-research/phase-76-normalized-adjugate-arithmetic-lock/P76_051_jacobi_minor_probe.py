#!/usr/bin/env python3
"""Verify the 2x2 complementary-minor formula for safe shell ratios."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import transfer
from P76_047_mu_freezing_probe import transfer_data_mu


def bordered(Hbig, idxbig, L, z):
    Hn = Hbig[1:-1, 1:-1]
    idxn = idxbig[1:-1]
    g = mp.matrix([Hbig[j + 1, Hbig.cols - 1] for j in range(Hbig.rows - 2)])
    size = Hn.rows + 1
    B = mp.matrix(size)
    for i in range(Hn.rows):
        for j in range(Hn.cols):
            B[i, j] = Hn[i, j]
        B[i, Hn.cols] = g[i]
    for j, n in enumerate(idxn):
        B[Hn.rows, j] = 1 / (z - 2 * mp.pi * n / L)
    B[Hn.rows, Hn.cols] = 1 / (z - 2 * mp.pi * idxbig[-1] / L)
    return B


def minor_det(B):
    inv = B ** -1
    last = B.rows - 1
    plus_shell_row = B.rows - 2
    R = mp.matrix([[inv[0, 0], inv[0, plus_shell_row]], [inv[last, 0], inv[last, plus_shell_row]]])
    return mp.det(R)


def run():
    mp.mp.dps = 100
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z0 = mp.mpc(0, 1)
    print("P76.051 Jacobi 2x2 safe cross-ratio identity")
    print("N sigma relativeError")
    for n_modes in (5, 6, 7, 8):
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        Hn = Hbig[1:-1, 1:-1]
        idxn = idxbig[1:-1]
        Hsmall = Hn[1:-1, 1:-1]
        idxsmall = idxn[1:-1]
        db_new, inner_new, x_new = transfer_data_mu(Hbig, idxbig, mp.mpf(0))
        db_old, inner_old, x_old = transfer_data_mu(Hn, idxn, mp.mpf(0))
        direct0 = transfer(z0, db_new, inner_new, x_new, L) / transfer(z0, db_old, inner_old, x_old, L)
        det0 = minor_det(bordered(Hbig, idxbig, L, z0))
        for sigma in (mp.mpf("0.6"), mp.mpf("1.5"), mp.mpf("2")):
            z = 1j * sigma
            direct = transfer(z, db_new, inner_new, x_new, L) / transfer(z, db_old, inner_old, x_old, L)
            jacobi = det0 / minor_det(bordered(Hbig, idxbig, L, z))
            normalized = direct / direct0
            error = abs(normalized - jacobi) / max(1, abs(normalized), abs(jacobi))
            print(f"{n_modes:2d} {mp.nstr(sigma,3):>5} {mp.nstr(error,8):>14}")


if __name__ == "__main__":
    run()
