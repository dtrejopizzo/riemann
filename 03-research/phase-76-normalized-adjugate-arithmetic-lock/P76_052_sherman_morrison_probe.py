#!/usr/bin/env python3
"""Verify and scale the scalar Sherman--Morrison shell parameter."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_051_jacobi_minor_probe import bordered, minor_det


def scalar_theta(B0, B, deleted_cols, deleted_rows):
    G = B0 ** -1
    delta_row = mp.matrix([[B[B.rows - 1, j] - B0[B0.rows - 1, j] for j in range(B.cols)]])
    e = mp.matrix(B.rows, 1)
    e[B.rows - 1] = 1
    den = 1 + (delta_row * G * e)[0]
    a = mp.matrix([G[j, B.rows - 1] for j in deleted_cols])
    bg = delta_row * G
    b = mp.matrix([[bg[0, j] for j in deleted_rows]])
    R0 = mp.matrix([[G[i, j] for j in deleted_rows] for i in deleted_cols])
    return (b * (R0 ** -1) * a)[0] / den


def run():
    mp.mp.dps = 100
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z0 = mp.mpc(0, 1)
    print("P76.052 Sherman-Morrison scalar, sigma0=1")
    print("N sigma |theta| scaled=N^2|theta|/L^2 identityError")
    for n_modes in (5, 6, 7, 8):
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        B0 = bordered(Hbig, idxbig, L, z0)
        deleted_cols = [0, B0.cols - 1]
        deleted_rows = [0, B0.rows - 2]
        det0 = minor_det(B0)
        for sigma in (mp.mpf("0.6"), mp.mpf("1.5"), mp.mpf("2")):
            B = bordered(Hbig, idxbig, L, 1j * sigma)
            theta = scalar_theta(B0, B, deleted_cols, deleted_rows)
            direct = det0 / minor_det(B)
            generated = 1 / (1 - theta)
            error = abs(direct - generated) / max(1, abs(direct), abs(generated))
            scaled = n_modes**2 * abs(theta) / L**2
            print(
                f"{n_modes:2d} {mp.nstr(sigma,3):>5} {mp.nstr(abs(theta),9):>11}"
                f" {mp.nstr(scaled,9):>23} {mp.nstr(error,6):>14}"
            )


if __name__ == "__main__":
    run()
