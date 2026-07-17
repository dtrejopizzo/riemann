#!/usr/bin/env python3
"""Test whether omitted Fourier columns cancel the prolate rectangular residual."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients


def norm2(v):
    return mp.sqrt(mp.fsum(abs(v[j]) ** 2 for j in range(v.rows)))


def run():
    mp.mp.dps = 70
    max_modes = 18
    H, idx, L = build_mp(6, max_modes, 70)
    coeff = coefficients(mp.mpf(6), max_modes, L)
    pos = {n: j for j, n in enumerate(idx)}
    print("P76.064 Fourier-tail cancellation, lambda=6")
    print("N finiteNorm fullJNorm ratio fullMaxIndex")
    for n_modes in (8, 10, 12, 15):
        rows = list(range(-n_modes + 1, n_modes))
        finite_cols = list(range(-n_modes + 1, n_modes + 1))
        full_cols = list(range(-max_modes, max_modes + 1))

        def product(columns):
            out = mp.matrix(len(rows), 1)
            for i, rn in enumerate(rows):
                out[i] = mp.fsum(H[pos[rn], pos[cn]] * coeff[cn] for cn in columns)
            return out

        finite = product(finite_cols)
        full = product(full_cols)
        max_row = rows[max(range(len(rows)), key=lambda j: abs(full[j]))]
        print(
            f"{n_modes:2d} {mp.nstr(norm2(finite),10):>12} {mp.nstr(norm2(full),10):>12}"
            f" {mp.nstr(norm2(full)/norm2(finite),9):>10} {max_row:12d}"
        )

    n_modes = 8
    rows = list(range(-n_modes + 1, n_modes))
    print("cumulative J for fixed rows N=8")
    print("J residualNorm")
    for cutoff in range(8, max_modes + 1):
        columns = list(range(-cutoff, cutoff + 1))
        residual = mp.matrix(len(rows), 1)
        for i, rn in enumerate(rows):
            residual[i] = mp.fsum(H[pos[rn], pos[cn]] * coeff[cn] for cn in columns)
        print(f"{cutoff:2d} {mp.nstr(norm2(residual),12):>16}")


if __name__ == "__main__":
    run()
