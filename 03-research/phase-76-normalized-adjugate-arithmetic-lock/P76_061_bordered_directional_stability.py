#!/usr/bin/env python3
"""Audit bordered evaluation stability for the prolate residual direction."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients


def norm2(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def row_norm(v):
    return mp.sqrt(mp.fsum(abs(v[0, j]) ** 2 for j in range(v.cols)))


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    coeff = coefficients(mp.mpf(6), max_modes, L)
    z0 = mp.mpc(0, 1)
    points = [mp.mpc(0, v) for v in ("0.6", "0.75", "1.5", "2")]
    print("P76.061 bordered directional stability, lambda=6")
    print("N ambientBound actualError amplification actualDirectional")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        columns = idx[1:]
        M = H[1:-1, 1:]
        A = H[1:-1, 1:-1]
        b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        x = A ** -1 * b
        y = mp.matrix([x[j] for j in range(x.rows)] + [mp.mpf(-1)])
        k = mp.matrix([coeff[n] for n in columns])

        def r(z):
            return mp.matrix([[1 / (z - 2 * mp.pi * n / L) for n in columns]])

        alpha = (r(z0) * y)[0] / (r(z0) * k)[0]
        e = y - alpha * k
        f = M * e
        B0 = mp.matrix(M.cols)
        for i in range(M.rows):
            for j in range(M.cols):
                B0[i, j] = M[i, j]
        for j in range(M.cols):
            B0[M.rows, j] = r(z0)[0, j]
        G = B0 ** -1
        top_inverse = G[:, : M.rows]
        ambient = mp.mpf(0)
        actual = mp.mpf(0)
        directional = mp.mpf(0)
        for z in points:
            evalrow = (r(z) - r(z0)) * top_inverse
            denom = abs((r(z) * y)[0])
            ambient = max(ambient, row_norm(evalrow) * norm2(f) / denom)
            value = abs((r(z) * e)[0]) / denom
            actual = max(actual, value)
            directional = max(directional, abs((evalrow * f)[0]) / max(norm2(f), mp.mpf("1e-100")))
        amplification = ambient / max(actual, mp.mpf("1e-100"))
        print(
            f"{n_modes:2d} {mp.nstr(ambient,8):>12} {mp.nstr(actual,8):>11}"
            f" {mp.nstr(amplification,8):>13} {mp.nstr(directional,8):>17}"
        )


if __name__ == "__main__":
    run()
