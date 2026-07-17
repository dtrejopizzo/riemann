#!/usr/bin/env python3
"""Determine whether the exact prolate CCM residual is a shell source."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients


def run():
    mp.mp.dps = 70
    max_modes = 15
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    coeff = coefficients(mp.mpf(6), max_modes, L)
    print("P76.062 prolate rectangular residual localization, lambda=6")
    print("N ||f|| edge2Energy edge4Energy maxIndex maxEntry/||f||")
    for n_modes in (6, 8, 10, 12, 15):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        columns = idx[1:]
        rows = idx[1:-1]
        M = H[1:-1, 1:]
        k = mp.matrix([coeff[n] for n in columns])
        f = M * k
        energy = [abs(f[j]) ** 2 for j in range(f.rows)]
        total = mp.fsum(energy)
        edge2 = mp.fsum(energy[:2] + energy[-2:]) / total
        edge4 = mp.fsum(energy[:4] + energy[-4:]) / total
        maxpos = max(range(f.rows), key=lambda j: abs(f[j]))
        maxratio = abs(f[maxpos]) / mp.sqrt(total)
        print(
            f"{n_modes:2d} {mp.nstr(mp.sqrt(total),9):>12} {mp.nstr(edge2,8):>11}"
            f" {mp.nstr(edge4,8):>11} {rows[maxpos]:8d} {mp.nstr(maxratio,8):>15}"
        )


if __name__ == "__main__":
    run()
