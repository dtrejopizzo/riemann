#!/usr/bin/env python3
"""Apply the core safe logarithmic derivative to arithmetic falsifiers."""

import random

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import right_transfer_data, transfer
from P76_035_safe_log_derivative_probe import transfer_prime, target_log_derivative
from P76_037_core_log_derivative_probe import external_tail


def random_symmetric(size, seed=7645):
    rng = random.Random(seed)
    H = mp.matrix(size)
    for i in range(size):
        for j in range(i, size):
            value = mp.mpf(str(rng.gauss(0, 1)))
            H[i, j] = value
            H[j, i] = value
    return H


def errors(H, idx, L, n_modes):
    db, inner, x = right_transfer_data(H, idx)
    values = []
    for text in ("0.6", "0.75", "1", "1.5", "2"):
        sigma = mp.mpf(text)
        z = 1j * sigma
        t = transfer(z, db, inner, x, L)
        tp = transfer_prime(z, db, inner, x, L)
        core = (
            L * mp.coth(sigma * L / 2)
            + 2 * mp.re(1j * tp / t)
            - external_tail(sigma, L, n_modes)
        )
        target = target_log_derivative(sigma)
        values.append(abs(core - target) / abs(target))
    return values


def run():
    mp.mp.dps = 80
    n_modes = 9
    zeta, idx, L = build_mp(6, n_modes, 80)
    planted, _, _ = build_mp(
        6, n_modes, 80, planted=("14.134725141734693790", "0.30", "5.0")
    )
    random_h = random_symmetric(len(idx))
    print("P76.045 core safe-log falsifiers")
    print("case       maxRel errors(.6,.75,1,1.5,2)")
    for tag, H in (("zeta", zeta), ("planted", planted), ("random", random_h)):
        result = errors(H, idx, L, n_modes)
        print(f"{tag:8s} {mp.nstr(max(result),8):>10} " + ",".join(mp.nstr(e,5) for e in result))


if __name__ == "__main__":
    run()
