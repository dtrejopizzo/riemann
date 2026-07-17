#!/usr/bin/env python3
"""Test whether consecutive-cutoff ground eigenlines have a strong limit."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp, vec_norm


def ground(lam, n_modes, dps=60):
    H, idx, L = build_mp(lam, n_modes, dps)
    vals, vecs = mp.eigsy(H)
    xi = vecs[:, 0]
    gamma = mp.mpf("14.134725141734693790")
    r = mp.matrix([1 / (gamma - 2 * mp.pi * n / L) for n in idx])
    q = abs((r.T * xi)[0]) / vec_norm(r)
    return vals[0], vals[1] - vals[0], xi, q


def embedded_overlap(x_small, x_large):
    if x_large.rows != x_small.rows + 2:
        raise ValueError("expected consecutive symmetric cutoffs")
    embedded = mp.matrix(x_large.rows, 1)
    for j in range(x_small.rows):
        embedded[j + 1] = x_small[j]
    return abs((embedded.T * x_large)[0])


def run():
    mp.mp.dps = 60
    rows = []
    for n_modes in (3, 4, 5, 6, 7, 8):
        rows.append((n_modes, *ground(6, n_modes)))
    print("P76.008 consecutive-cutoff eigenline stability")
    print("N          mu            gap         qgamma    overlap(prev)")
    previous = None
    for n_modes, mu, gap, xi, q in rows:
        overlap = mp.nan if previous is None else embedded_overlap(previous, xi)
        print(
            f"{n_modes:2d} {mp.nstr(mu,9):>13} {mp.nstr(gap,9):>13}"
            f" {mp.nstr(q,9):>13} {mp.nstr(overlap,9):>16}"
        )
        previous = xi


if __name__ == "__main__":
    run()
