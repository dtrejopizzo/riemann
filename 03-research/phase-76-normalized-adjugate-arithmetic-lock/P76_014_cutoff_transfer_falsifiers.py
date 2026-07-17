#!/usr/bin/env python3
"""Falsify generic explanations of the cutoff-boundary transfer lock."""

import random

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_013_cutoff_schur_transfer_probe import transfer


GAMMA_TEXT = "14.134725141734693790"


def random_symmetric(n, seed=7614):
    rng = random.Random(seed)
    H = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            value = mp.mpf(str(rng.gauss(0, 1)))
            H[i, j] = value
            H[j, i] = value
    return H


def report(tag, H, idx, L, gamma):
    mu, gap, tc, qc, err = transfer(H, idx, L, gamma)
    _, _, tn, qn, _ = transfer(H, idx, L, gamma + mp.mpf("0.125"))
    print(
        f"{tag:14s} {mp.nstr(mu,8):>12} {mp.nstr(gap,8):>12}"
        f" {mp.nstr(tc,8):>12} {mp.nstr(qc,8):>12}"
        f" {mp.nstr(tn,8):>12} {mp.nstr(qn,8):>12} {mp.nstr(err,4):>10}"
    )


def run():
    mp.mp.dps = 70
    gamma = mp.mpf(GAMMA_TEXT)
    n_modes = 9
    zeta, idx, L = build_mp(6, n_modes, 70)
    planted, _, _ = build_mp(
        6,
        n_modes,
        70,
        planted=(GAMMA_TEXT, "0.30", "5.0"),
    )
    random_h = random_symmetric(len(idx))

    print("P76.014 cutoff-transfer falsifiers")
    print("case                    mu          gap       ||Tg||       qgamma    ||Tnear||        qnear   idErr")
    report("zeta", zeta, idx, L, gamma)
    report("planted", planted, idx, L, gamma)
    report("random", random_h, idx, L, gamma)


if __name__ == "__main__":
    run()
