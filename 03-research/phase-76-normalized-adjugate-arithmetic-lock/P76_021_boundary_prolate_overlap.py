#!/usr/bin/env python3
"""Compare canonical boundary-null vectors with the prolate model."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients, normalized_overlap


def boundary_vector(H, side):
    vals, _ = mp.eigsy(H)
    mu = vals[0]
    A = H[1:-1, 1:-1] - mu * mp.eye(H.rows - 2)
    boundary_pos = 0 if side < 0 else H.cols - 1
    b = mp.matrix([H[j + 1, boundary_pos] for j in range(H.rows - 2)])
    x = A ** -1 * b
    return [x[j] for j in range(x.rows)] + [mp.mpf(-1)]


def run():
    mp.mp.dps = 60
    lam = mp.mpf(6)
    L = 2 * mp.log(lam)
    max_modes = 9
    coeff = coefficients(lam, max_modes, L)
    Hmax, idxmax, _ = build_mp(6, max_modes, 60)
    print("P76.021 boundary-null/prolate overlap")
    print("N       overlap(left)     overlap(right)")
    for n_modes in (4, 5, 6, 7, 8, 9):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]

        y_left = boundary_vector(H, -1)
        left_indices = idx[1:-1] + [idx[0]]
        k_left = [coeff[n] for n in left_indices]

        y_right = boundary_vector(H, 1)
        right_indices = idx[1:-1] + [idx[-1]]
        k_right = [coeff[n] for n in right_indices]

        print(
            f"{n_modes:2d} {mp.nstr(normalized_overlap(k_left,y_left),10):>19}"
            f" {mp.nstr(normalized_overlap(k_right,y_right),10):>19}"
        )


if __name__ == "__main__":
    run()
