#!/usr/bin/env python3
"""Measure consecutive finite-section increments of the core safe log trace."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import right_transfer_data, transfer
from P76_035_safe_log_derivative_probe import transfer_prime
from P76_037_core_log_derivative_probe import external_tail


def core_values(H, idx, L, n_modes, sigmas):
    db, inner, x = right_transfer_data(H, idx)
    result = []
    for sigma in sigmas:
        z = 1j * sigma
        t = transfer(z, db, inner, x, L)
        tp = transfer_prime(z, db, inner, x, L)
        result.append(
            L * mp.coth(sigma * L / 2)
            + 2 * mp.re(1j * tp / t)
            - external_tail(sigma, L, n_modes)
        )
    return result


def run():
    mp.mp.dps = 80
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 80)
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1", "1.5", "2")]
    previous = None
    print("P76.046 consecutive core-log increments, lambda=6")
    print("N->N+1 maxAbsDelta scaled=N^2*delta/L^2")
    for n_modes in range(5, 13):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        values = core_values(H, idx, L, n_modes, sigmas)
        if previous is not None:
            delta = max(abs(values[j] - previous[j]) for j in range(len(sigmas)))
            scaled = (n_modes - 1) ** 2 * delta / L**2
            print(f"{n_modes-1:2d}->{n_modes:2d} {mp.nstr(delta,10):>14} {mp.nstr(scaled,10):>22}")
        previous = values


if __name__ == "__main__":
    run()
