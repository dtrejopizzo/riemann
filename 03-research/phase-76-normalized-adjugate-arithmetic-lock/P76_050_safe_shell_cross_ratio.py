#!/usr/bin/env python3
"""Measure the safe-normalized cross ratio between consecutive shell transfers."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import transfer
from P76_047_mu_freezing_probe import transfer_data_mu


def shell_values(H, idx, L, sigmas):
    db, inner, x = transfer_data_mu(H, idx, mp.mpf(0))
    return [transfer(1j * sigma, db, inner, x, L) for sigma in sigmas]


def run():
    mp.mp.dps = 100
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 100)
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1", "1.5", "2")]
    base_pos = 2
    previous = None
    print("P76.050 safe shell cross ratio, lambda=6, sigma0=1, mu=0")
    print("N->N+1 max|Q_N(sigma)-1| scaled=N^2*defect/L^2")
    for n_modes in range(5, 13):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        current = shell_values(H, idx, L, sigmas)
        if previous is not None:
            ratios = [current[j] / previous[j] for j in range(len(sigmas))]
            base = ratios[base_pos]
            bilateral = [abs(ratio / base) ** 2 for ratio in ratios]
            defect = max(abs(value - 1) for value in bilateral)
            n = n_modes - 1
            print(
                f"{n:2d}->{n_modes:2d} {mp.nstr(defect,10):>18}"
                f" {mp.nstr(n*n*defect/L**2,10):>24}"
            )
        previous = current


if __name__ == "__main__":
    run()
