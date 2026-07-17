#!/usr/bin/env python3
"""Compare the bilateral boundary characteristic with normalized Xi squared."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_018_boundary_characteristic_probe import (
    entire_transfer,
    right_transfer_data,
    xi_norm,
)


def run():
    mp.mp.dps = 60
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 60)
    real_grid = [mp.mpf(j) / 2 for j in range(25)]
    safe_grid = [-1j * mp.mpf(v) for v in ("0.75", "1.0", "1.5")]
    print("P76.030 bilateral boundary characteristic, lambda=6")
    print("N       realRelL2     realRelSup     safeMaxRel")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        phi0 = entire_transfer(mp.mpf(0), db, inner, x, L)

        def psi(z):
            return entire_transfer(z, db, inner, x, L) * entire_transfer(-z, db, inner, x, L) / phi0**2

        targets = [xi_norm(t) ** 2 for t in real_grid]
        values = [psi(t) for t in real_grid]
        errors = [values[j] - targets[j] for j in range(len(values))]
        rel_l2 = mp.sqrt(sum(abs(e) ** 2 for e in errors)) / mp.sqrt(sum(abs(v) ** 2 for v in targets))
        rel_sup = max(abs(e) for e in errors) / max(abs(v) for v in targets)
        safe_errors = [abs(psi(z) - xi_norm(z) ** 2) / abs(xi_norm(z) ** 2) for z in safe_grid]
        print(
            f"{n_modes:2d} {mp.nstr(rel_l2,9):>16} {mp.nstr(rel_sup,9):>16}"
            f" {mp.nstr(max(safe_errors),9):>16}"
        )


if __name__ == "__main__":
    run()
