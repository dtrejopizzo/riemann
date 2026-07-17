#!/usr/bin/env python3
"""Test boundary-characteristic identification in the Euler-safe half-plane."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


def run():
    mp.mp.dps = 70
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 70)
    sigmas = [mp.mpf("0.75"), mp.mpf("1.0"), mp.mpf("1.5")]
    points = [-1j * sigma for sigma in sigmas]
    targets = [xi_norm(t) for t in points]

    print("P76.022 Euler-safe boundary characteristic")
    print("N       maxRelError       odd/evenSafe")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)
        relative_errors = []
        odd_values = []
        even_values = []
        for t, target in zip(points, targets):
            plus = entire_transfer(t, db, inner, x, L)
            minus = entire_transfer(-t, db, inner, x, L)
            even = (plus + minus) / (2 * phi0)
            odd = (plus - minus) / (2 * phi0)
            relative_errors.append(abs(even - target) / abs(target))
            odd_values.append(abs(odd))
            even_values.append(abs(even))
        odd_ratio = mp.sqrt(sum(v * v for v in odd_values)) / mp.sqrt(
            sum(v * v for v in even_values)
        )
        print(
            f"{n_modes:2d} {mp.nstr(max(relative_errors),10):>17}"
            f" {mp.nstr(odd_ratio,10):>18}"
        )


if __name__ == "__main__":
    run()
