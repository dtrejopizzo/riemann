#!/usr/bin/env python3
"""Compare boundary and prolate vectors through the rectangular CCM equation."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients


def norm2(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def run():
    mp.mp.dps = 70
    max_modes = 15
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    coeff = coefficients(mp.mpf(6), max_modes, L)
    z0 = mp.mpc(0, 1)
    points = [mp.mpc(0, v) for v in ("0.6", "0.75", "1.5", "2")]
    print("P76.060 prolate rectangular residual, lambda=6, mu=0")
    print("N ||Mk||/||k|| ||Me||/||e|| maxSafeError")
    for n_modes in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        inner = idx[1:-1]
        columns = idx[1:]
        M = H[1:-1, 1:]
        A = H[1:-1, 1:-1]
        b = mp.matrix([H[j + 1, H.cols - 1] for j in range(H.rows - 2)])
        x = A ** -1 * b
        y = mp.matrix([x[j] for j in range(x.rows)] + [mp.mpf(-1)])
        k = mp.matrix([coeff[n] for n in columns])

        def row(z):
            return mp.matrix([[1 / (z - 2 * mp.pi * n / L) for n in columns]])

        alpha = (row(z0) * y)[0] / (row(z0) * k)[0]
        error = y - alpha * k
        rk = M * k
        re = M * error
        safe = max(abs((row(z) * error)[0]) / abs((row(z) * y)[0]) for z in points)
        print(
            f"{n_modes:2d} {mp.nstr(norm2(rk)/norm2(k),9):>13}"
            f" {mp.nstr(norm2(re)/norm2(error),9):>13} {mp.nstr(safe,9):>13}"
        )


if __name__ == "__main__":
    run()
