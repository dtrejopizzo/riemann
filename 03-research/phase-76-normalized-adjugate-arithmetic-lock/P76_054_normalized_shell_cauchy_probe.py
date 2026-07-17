#!/usr/bin/env python3
"""Verify theta=r(z)w/r(z)g for the canonical bordered responses."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_051_jacobi_minor_probe import bordered
from P76_052_sherman_morrison_probe import scalar_theta


def run():
    mp.mp.dps = 100
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z0 = mp.mpc(0, 1)
    print("P76.054 normalized shell Cauchy identity")
    print("N sigma relIdentity r0w r0g-1 scaledRatio")
    for n_modes in (5, 6, 7, 8):
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        B0 = bordered(Hbig, idxbig, L, z0)
        G = B0 ** -1
        last = B0.rows - 1
        C = [0, last]
        D = [0, B0.rows - 2]
        R0 = mp.matrix([[G[i, j] for j in D] for i in C])
        a = mp.matrix([G[i, last] for i in C])
        selected = mp.matrix(B0.rows, 2)
        for i in range(B0.rows):
            for j in range(2):
                selected[i, j] = G[i, D[j]]
        w = selected * (R0 ** -1) * a
        g = G[:, last]
        r0w = (B0[last, :] * w)[0]
        r0g = (B0[last, :] * g)[0]
        for sigma in (mp.mpf("0.6"), mp.mpf("1.5"), mp.mpf("2")):
            B = bordered(Hbig, idxbig, L, 1j * sigma)
            rz = B[last, :]
            ratio = (rz * w)[0] / (rz * g)[0]
            theta = scalar_theta(B0, B, C, D)
            error = abs(ratio - theta) / max(1, abs(ratio), abs(theta))
            scaled = n_modes**2 * abs(ratio) / L**2
            print(
                f"{n_modes:2d} {mp.nstr(sigma,3):>5} {mp.nstr(error,5):>11}"
                f" {mp.nstr(abs(r0w),3):>8} {mp.nstr(abs(r0g-1),3):>8}"
                f" {mp.nstr(scaled,8):>12}"
            )


if __name__ == "__main__":
    run()
