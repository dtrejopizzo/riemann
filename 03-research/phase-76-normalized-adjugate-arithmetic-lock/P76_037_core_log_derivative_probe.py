#!/usr/bin/env python3
"""Remove the exact external sine-zero tail from SR-LOG."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import right_transfer_data, transfer
from P76_035_safe_log_derivative_probe import transfer_prime, target_log_derivative


def external_tail(sigma, L, n_modes):
    harmonic2 = mp.fsum(1 / mp.mpf(k) ** 2 for k in range(1, n_modes + 1))
    return (
        sigma * L**2 / (2 * mp.pi**2 * n_modes**2)
        + sigma * L**2 / mp.pi**2 * (mp.zeta(2) - harmonic2)
    )


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1", "1.5", "2")]
    print("P76.037 core safe logarithmic derivative, lambda=6")
    print("N       maxRel signedErrors(.6,.75,1,1.5,2)")
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
            core = (
                L * mp.coth(sigma * L / 2)
                + 2 * mp.re(1j * tp / t)
                - external_tail(sigma, L, n_modes)
            )
            target = target_log_derivative(sigma)
            errors.append((core - target) / target)
        print(f"{n_modes:2d} {mp.nstr(max(abs(e) for e in errors),9):>14} " + ",".join(mp.nstr(e,6) for e in errors))


if __name__ == "__main__":
    run()
