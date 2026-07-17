#!/usr/bin/env python3
"""Falsifiers for the full even boundary characteristic on [0,12]."""

import random

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


def random_symmetric(n, seed=7619):
    rng = random.Random(seed)
    H = mp.matrix(n)
    for i in range(n):
        for j in range(i, n):
            value = mp.mpf(str(rng.gauss(0, 1)))
            H[i, j] = value
            H[j, i] = value
    return H


def metrics(H, idx, L, grid, target):
    db, inner, x = right_transfer_data(H, idx)
    phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)
    even_vals = []
    odd_vals = []
    for t in grid:
        plus = entire_transfer(t, db, inner, x, L)
        minus = entire_transfer(-t, db, inner, x, L)
        even_vals.append((plus + minus) / (2 * phi0))
        odd_vals.append((plus - minus) / (2 * phi0))
    errors = [even_vals[j] - target[j] for j in range(len(grid))]
    target_norm = mp.sqrt(sum(abs(v) ** 2 for v in target))
    rel_l2 = mp.sqrt(sum(abs(e) ** 2 for e in errors)) / target_norm
    rel_sup = max(abs(e) for e in errors) / max(abs(v) for v in target)
    odd_ratio = mp.sqrt(sum(abs(v) ** 2 for v in odd_vals)) / mp.sqrt(
        sum(abs(v) ** 2 for v in even_vals)
    )
    return rel_l2, rel_sup, odd_ratio


def run():
    mp.mp.dps = 70
    n_modes = 9
    zeta, idx, L = build_mp(6, n_modes, 70)
    planted, _, _ = build_mp(
        6,
        n_modes,
        70,
        planted=("14.134725141734693790", "0.30", "5.0"),
    )
    random_h = random_symmetric(len(idx))
    grid = [mp.mpf(j) / 2 for j in range(25)]
    target = [xi_norm(t) for t in grid]

    print("P76.019 boundary characteristic falsifiers")
    print("case              relL2(Xi)      relSup(Xi)      odd/evenL2")
    for tag, H in (("zeta", zeta), ("planted", planted), ("random", random_h)):
        rel_l2, rel_sup, odd_ratio = metrics(H, idx, L, grid, target)
        print(
            f"{tag:12s} {mp.nstr(rel_l2,9):>16}"
            f" {mp.nstr(rel_sup,9):>16} {mp.nstr(odd_ratio,9):>16}"
        )


if __name__ == "__main__":
    run()
