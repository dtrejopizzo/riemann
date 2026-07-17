#!/usr/bin/env python3
import math
import sys

import mpmath as mp
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_206_hp_matrix_entry_probe import entry_modes  # noqa: E402


mp.mp.dps = 100


def bernoulli_abs(n):
    return abs(mp.bernoulli(n))


def psi_remainder_bound(z, K):
    # Conservative next-term style bound, valid here as a numerical audit in
    # the large right half-plane.  E73.210 records that final proof must cite or
    # derive the corresponding Bernoulli remainder inequality.
    rz = abs(z)
    return bernoulli_abs(2 * K) / (2 * K * rz ** (2 * K))


def trigamma_remainder_bound(z, K):
    rz = abs(z)
    return bernoulli_abs(2 * K) / (rz ** (2 * K + 1))


def digamma_tail_radius_for_entry(m, n, L, R, K):
    const, linear = entry_modes(m, n, L)
    total = mp.mpf("0")
    keys = set(const) | set(linear)
    for om0 in keys:
        om = mp.mpf(str(float(om0)))
        z = mp.mpf(R) + mp.mpf("0.25") - 0.5j * om
        rad_d1 = mp.mpf("0.5") * (
            psi_remainder_bound(mp.mpf(R) + mp.mpf("0.5"), K) + psi_remainder_bound(z, K)
        )
        rad_d2 = mp.mpf("0.25") * trigamma_remainder_bound(z, K)
        total += abs(const.get(om0, 0j)) * rad_d1
        total += abs(linear.get(om0, 0j)) * rad_d2
    return total


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.210 psi asymptotic budget")
    print("Conservative Bernoulli next-term audit for D1/D2 entry radii.")
    print(" lam     L    N  dim    K   maxRadB  targetB  slack")
    targets = {8: -56.26, 10: -51.93, 12: -48.94}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        L = 2.0 * math.log(lam)
        idx = list(range(-n_modes, n_modes + 1))
        target = mp.power(mp.mpf(L), targets[lam])
        for K in [8, 12, 16, 20, 24, 28, 32]:
            max_rad = mp.mpf("0")
            for a, m in enumerate(idx):
                for n in idx[a:]:
                    max_rad = max(max_rad, digamma_tail_radius_for_entry(m, n, L, 80, K))
            print(
                f"{lam:4d} {L:7.3f} {n_modes:4d} {len(idx):4d}"
                f" {K:4d} {bexp(max_rad, L):9.2f}"
                f" {targets[lam]:8.2f} {float(target / max_rad):9.2e}"
            )


if __name__ == "__main__":
    run()
