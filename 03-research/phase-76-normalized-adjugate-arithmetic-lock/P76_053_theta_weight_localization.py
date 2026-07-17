#!/usr/bin/env python3
"""Locate the directional weight responsible for the small shell scalar."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_051_jacobi_minor_probe import bordered


def run():
    mp.mp.dps = 100
    max_modes = 9
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    z0 = mp.mpc(0, 1)
    z = mp.mpc(0, 2)
    print("P76.053 theta directional-weight localization, z0=i,z=2i")
    print("N |sum| sumAbs lowAbs highAbs boundaryAbs cancellation")
    for n_modes in (5, 6, 7, 8):
        off_big = max_modes - (n_modes + 1)
        Hbig = Hmax[off_big : Hmax.rows - off_big, off_big : Hmax.cols - off_big]
        idxbig = idxmax[off_big : len(idxmax) - off_big]
        B0 = bordered(Hbig, idxbig, L, z0)
        B = bordered(Hbig, idxbig, L, z)
        G = B0 ** -1
        last = B0.rows - 1
        deleted_cols = [0, last]
        deleted_rows = [0, B0.rows - 2]
        R0 = mp.matrix([[G[i, j] for j in deleted_rows] for i in deleted_cols])
        a = mp.matrix([G[i, last] for i in deleted_cols])
        selector = mp.matrix(B0.rows, 2)
        for i in range(B0.rows):
            selector[i, 0] = G[i, deleted_rows[0]]
            selector[i, 1] = G[i, deleted_rows[1]]
        w = selector * (R0 ** -1) * a
        delta = [B[last, j] - B0[last, j] for j in range(B0.cols)]
        terms = [delta[j] * w[j] for j in range(len(delta))]
        total = abs(mp.fsum(terms))
        total_abs = mp.fsum(abs(term) for term in terms)
        # Columns 0..2N correspond to modes -N..N; the last is +(N+1).
        mode_indices = idxbig[1:-1]
        low = mp.fsum(abs(terms[j]) for j, k in enumerate(mode_indices) if abs(k) <= n_modes // 2)
        high = mp.fsum(abs(terms[j]) for j, k in enumerate(mode_indices) if abs(k) > n_modes // 2)
        boundary = abs(terms[-1])
        cancellation = total_abs / max(total, mp.mpf("1e-100"))
        print(
            f"{n_modes:2d} {mp.nstr(total,7):>9} {mp.nstr(total_abs,7):>9}"
            f" {mp.nstr(low,7):>9} {mp.nstr(high,7):>9} {mp.nstr(boundary,7):>11}"
            f" {mp.nstr(cancellation,7):>12}"
        )


if __name__ == "__main__":
    run()
