#!/usr/bin/env python3
"""Test whether shell-response moment collapse is arithmetically selective."""

import random

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_051_jacobi_minor_probe import bordered


def random_symmetric(size, seed=7656):
    rng = random.Random(seed)
    H = mp.matrix(size)
    for i in range(size):
        for j in range(i, size):
            value = mp.mpf(str(rng.gauss(0, 1)))
            H[i, j] = value
            H[j, i] = value
    return H


def metrics(Hbig, idxbig, L, z0):
    B0 = bordered(Hbig, idxbig, L, z0)
    G = B0 ** -1
    last = B0.rows - 1
    C = [0, last]
    D = [0, B0.rows - 2]
    R0 = mp.matrix([[G[i, j] for j in D] for i in C])
    a = mp.matrix([G[i, last] for i in C])
    selected = mp.matrix(B0.rows, 2)
    for i in range(B0.rows):
        for j in range(2):
            selected[i, j] = G[i, D[j]]
    w = selected * (R0 ** -1) * a
    wn = mp.sqrt(mp.fsum(abs(w[j]) ** 2 for j in range(w.rows)))
    one = abs(mp.fsum(w[j] for j in range(w.rows))) / wn
    forcing = B0 * w
    fn = mp.sqrt(mp.fsum(abs(forcing[j]) ** 2 for j in range(forcing.rows))) / wn
    rz = bordered(Hbig, idxbig, L, mp.mpc(0, 2))[last, :]
    g = G[:, last]
    theta = abs((rz * w)[0] / (rz * g)[0])
    return one, fn, theta


def run():
    mp.mp.dps = 100
    n_big = 9
    zeta, idx, L = build_mp(6, n_big, 100)
    planted, _, _ = build_mp(
        6, n_big, 100, planted=("14.134725141734693790", "0.30", "5.0")
    )
    random_h = random_symmetric(len(idx))
    print("P76.056 shell moment falsifiers, outer cutoff 9")
    print("case       |1Tw|/||w||    ||Bw||/||w||      |theta(2i)|")
    for tag, H in (("zeta", zeta), ("planted", planted), ("random", random_h)):
        one, forcing, theta = metrics(H, idx, L, mp.mpc(0, 1))
        print(
            f"{tag:8s} {mp.nstr(one,10):>15} {mp.nstr(forcing,10):>17}"
            f" {mp.nstr(theta,10):>17}"
        )


if __name__ == "__main__":
    run()
