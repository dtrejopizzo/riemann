#!/usr/bin/env python3
"""Rebuild every CCM entry and test bilateral safe-axis scaling."""

import math

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


def run():
    mp.mp.dps = 70
    print("P76.033 direct multiprecision bilateral safe-axis scaling")
    print("lambda N N/L maxRel errors(.6,.75,1,1.5,2)")
    for lam in (4, 6, 8, 10):
        Lf = 2 * math.log(lam)
        n_modes = math.ceil(18 * Lf / (2 * math.pi)) + 4
        H, idx, L = build_mp(lam, n_modes, 70)
        db, inner, x = right_transfer_data(H, idx)
        phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)

        def psi(z):
            return entire_transfer(z, db, inner, x, L) * entire_transfer(-z, db, inner, x, L) / phi0**2

        points = [-1j * mp.mpf(v) for v in ("0.6", "0.75", "1.0", "1.5", "2.0")]
        errors = [abs(psi(z) - xi_norm(z) ** 2) / abs(xi_norm(z) ** 2) for z in points]
        print(
            f"{lam:6d} {n_modes:2d} {mp.nstr(n_modes/L,6):>8} {mp.nstr(max(errors),8):>10} "
            + ",".join(mp.nstr(e,5) for e in errors)
        )


if __name__ == "__main__":
    run()
