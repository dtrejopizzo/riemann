#!/usr/bin/env python3
"""Probe the full boundary characteristic along genuinely cofinal cutoffs."""

import math

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import (
    entire_transfer,
    right_transfer_data,
    xi_norm,
)


def normalized_phi(z, H, idx, L):
    db, inner, x = right_transfer_data(H, idx)
    phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)
    return entire_transfer(z, db, inner, x, L) / phi0


def run():
    mp.mp.dps = 60
    points = [
        mp.mpf("2.0"),
        mp.mpf("8.0"),
        -mp.mpc(0, "0.75"),
        -mp.mpc(0, "1.0"),
        mp.mpc("4.0", "0.4"),
    ]
    print("P76.025 full cofinal boundary characteristic")
    print("lambda N N/L max|Phi| maxRelSafe oddDefect(s=1.5)")
    for lam in (4, 6, 8, 10):
        L_float = 2 * math.log(lam)
        # Cover |Re z|<=18 with at least four extra modes.  This also makes
        # N/L increase slowly along the sampled path.
        n_modes = math.ceil(18 * L_float / (2 * math.pi)) + 4
        H, idx, L = build_mp(lam, n_modes, 60)
        values = [normalized_phi(z, H, idx, L) for z in points]
        safe_points = [-mp.mpc(0, sigma) for sigma in ("0.75", "1.0", "1.5")]
        safe_errors = []
        for z in safe_points:
            target = xi_norm(z)
            safe_errors.append(abs(normalized_phi(z, H, idx, L) - target) / abs(target))
        z = -mp.mpc(0, "1.0")
        odd_defect = abs(normalized_phi(z, H, idx, L) - normalized_phi(-z, H, idx, L))
        print(
            f"{lam:6d} {n_modes:2d} {mp.nstr(n_modes/L,6):>8}"
            f" {mp.nstr(max(abs(v) for v in values),8):>12}"
            f" {mp.nstr(max(safe_errors),8):>12} {mp.nstr(odd_defect,8):>18}"
        )


if __name__ == "__main__":
    run()
