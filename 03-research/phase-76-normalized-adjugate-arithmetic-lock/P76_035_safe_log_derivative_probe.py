#!/usr/bin/env python3
"""Probe the normalization-free safe logarithmic derivative."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import right_transfer_data, transfer


def transfer_prime(z, db_idx, inner_idx, x, L):
    db = 2 * mp.pi * db_idx / L
    return -1 / (z - db) ** 2 + sum(
        x[j] / (z - 2 * mp.pi * inner_idx[j] / L) ** 2 for j in range(x.rows)
    )


def target_log_derivative(sigma):
    s = mp.mpf("0.5") + sigma
    return 2 * (
        1 / s
        + 1 / (s - 1)
        - mp.log(mp.pi) / 2
        + mp.digamma(s / 2) / 2
        + mp.diff(mp.zeta, s) / mp.zeta(s)
    )


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1.0", "1.5", "2.0")]
    print("P76.035 safe logarithmic derivative, lambda=6")
    print("N       maxRel errors(.6,.75,1,1.5,2)")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        errors = []
        for sigma in sigmas:
            z = 1j * sigma
            t = transfer(z, db, inner, x, L)
            tp = transfer_prime(z, db, inner, x, L)
            finite = L * mp.coth(sigma * L / 2) + 2 * mp.re(1j * tp / t)
            target = target_log_derivative(sigma)
            errors.append(abs(finite - target) / abs(target))
        print(f"{n_modes:2d} {mp.nstr(max(errors),9):>14} " + ",".join(mp.nstr(e,6) for e in errors))


if __name__ == "__main__":
    run()
