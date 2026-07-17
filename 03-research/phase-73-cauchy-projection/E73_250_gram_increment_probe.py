#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def gram_schmidt_increments(rows):
    basis = []
    inc = []
    row_norms = []
    angle_sines = []
    for row in rows:
        row_norm = norm(row)
        res = row.copy()
        for e in basis:
            res = res - (res @ e.conj()) * e
        res_norm = norm(res)
        inc.append(res_norm)
        row_norms.append(row_norm)
        angle_sines.append(res_norm / max(row_norm, 1e-300))
        if res_norm > 0:
            basis.append(res / res_norm)
    return np.array(row_norms), np.array(inc), np.array(angle_sines)


def row_order_by_norm(D):
    return np.argsort([-norm(row) for row in D])


def run():
    print("E73.250 Gram increment probe")
    print("Vol_Q = product of Gram-Schmidt increments.")
    print(
        " lam      L pow order volB prodIncB minRowB maxRowB minSinB "
        "incB-values                     sinB-values"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            _H, _idx, _d, L, _mu, _xi, D, labels, _ranks = quotient_defects(
                lam, n_modes, rat_power
            )
            _u, s, _vh = svd(D, full_matrices=False)
            r = rank_from_svd(s)
            orders = [
                ("native", np.arange(r)),
                ("norm", row_order_by_norm(D[:r])),
            ]
            vol = float(np.prod(s[:r]))
            for name, order in orders:
                rows = D[order, :]
                row_norms, inc, sins = gram_schmidt_increments(rows)
                prod_inc = float(np.prod(inc))
                inc_vals = " ".join(f"{bexp(x, L):6.2f}" for x in inc)
                sin_vals = " ".join(f"{bexp(x, L):6.2f}" for x in sins)
                print(
                    f"{lam:4d} {L:8.3f} {rat_power:3d} {name:<6s}"
                    f" {bexp(vol, L):6.2f} {bexp(prod_inc, L):8.2f}"
                    f" {bexp(np.min(row_norms), L):7.2f}"
                    f" {bexp(np.max(row_norms), L):7.2f}"
                    f" {bexp(np.min(sins), L):7.2f}"
                    f" {inc_vals:<31s} {sin_vals}"
                )


if __name__ == "__main__":
    run()
