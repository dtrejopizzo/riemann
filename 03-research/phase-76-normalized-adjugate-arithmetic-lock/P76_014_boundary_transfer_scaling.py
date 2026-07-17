#!/usr/bin/env python3
"""Measure boundary-Schur selectivity on a jointly resolved (L,N) path."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_013_cutoff_schur_transfer_probe import transfer


def run():
    mp.mp.dps = 70
    gamma = mp.mpf("14.134725141734693790")
    print("P76.014 boundary-transfer scaling")
    print("lambda N      L          gap        ||Tg||       qgamma      ||Tnear||")
    for lam, n_modes in ((4, 6), (6, 9), (8, 10)):
        H, idx, L = build_mp(lam, n_modes, 70)
        _, gap, tc, qc, _ = transfer(H, idx, L, gamma)
        _, _, tn, _, _ = transfer(H, idx, L, gamma + mp.mpf("0.125"))
        print(
            f"{lam:6d} {n_modes:2d} {mp.nstr(L,8):>9} {mp.nstr(gap,7):>12}"
            f" {mp.nstr(tc,7):>12} {mp.nstr(qc,7):>12} {mp.nstr(tn,7):>13}"
        )


if __name__ == "__main__":
    run()
