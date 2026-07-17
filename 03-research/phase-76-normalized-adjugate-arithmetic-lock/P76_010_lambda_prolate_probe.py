#!/usr/bin/env python3
"""Measure the prolate/CCM overlap across support scales at fixed resolution."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm
from P76_009_prolate_overlap_probe import coefficients, normalized_overlap


def run():
    mp.mp.dps = 45
    gamma = mp.mpf("14.134725141734693790")
    print("P76.010 lambda/prolate overlap on a resolved path")
    print("lam  N      L             mu       overlap        qgamma")
    for lam_int, n_modes in ((4, 6), (6, 8), (8, 10)):
        lam = mp.mpf(lam_int)
        L = 2 * mp.log(lam)
        coeff = coefficients(lam, n_modes, L)
        H, idx, _ = build_mp(lam_int, n_modes, 45)
        vals, vecs = mp.eigsy(H)
        c = [coeff[n] for n in idx]
        ground = [vecs[j, 0] for j in range(vecs.rows)]
        overlap = normalized_overlap(c, ground)
        r = mp.matrix([1 / (gamma - 2 * mp.pi * n / L) for n in idx])
        q = abs((r.T * vecs[:, 0])[0]) / vec_norm(r)
        print(
            f"{lam_int:3d} {n_modes:2d} {mp.nstr(L,9):>10} {mp.nstr(vals[0],9):>14}"
            f" {mp.nstr(overlap,10):>13} {mp.nstr(q,9):>13}"
        )


if __name__ == "__main__":
    run()
