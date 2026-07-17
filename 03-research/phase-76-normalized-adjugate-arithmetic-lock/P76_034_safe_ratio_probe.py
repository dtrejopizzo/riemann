#!/usr/bin/env python3
"""Test Euler-safe ratios, which cancel the critical normalization."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    sigma0 = mp.mpf("1.0")
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1.5", "2.0")]
    print("P76.034 safe-ratio audit, lambda=6, sigma0=1")
    print("N       maxRelRatio errors(.6,.75,1.5,2)")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)

        def raw(sigma):
            z = 1j * sigma
            return (
                mp.sinh(sigma * L / 2) ** 2
                * entire_transfer(z, db, inner, x, L) * entire_transfer(-z, db, inner, x, L)
                / mp.sin(z * L / 2) ** 2
            )

        # The expression above simplifies to sinh^2*|T|^2 while reusing the
        # pole-safe entire evaluator.  Its common signs cancel in the ratio.
        base = raw(sigma0)
        target_base = xi_norm(-1j * sigma0) ** 2
        errors = []
        for sigma in sigmas:
            ratio = raw(sigma) / base
            target = xi_norm(-1j * sigma) ** 2 / target_base
            errors.append(abs(ratio - target) / abs(target))
        print(f"{n_modes:2d} {mp.nstr(max(errors),9):>16} " + ",".join(mp.nstr(e,6) for e in errors))


if __name__ == "__main__":
    run()
