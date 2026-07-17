#!/usr/bin/env python3
"""Compare boundary and Connes-prolate safe ratios in the same normalization."""

import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm


def entire_vector(z, coeff, idx, L):
    return mp.sin(z * L / 2) * mp.fsum(
        coeff[n] / (z - 2 * mp.pi * n / L) for n in idx
    )


def run():
    mp.mp.dps = 60
    lam = mp.mpf(6)
    max_modes = 12
    Hmax, idxmax, L = build_mp(6, max_modes, 60)
    print("computing prolate coefficients", flush=True)
    coeff = coefficients(lam, max_modes, L)
    sigma0 = mp.mpf("1")
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1.5", "2")]
    target0 = xi_norm(-1j * sigma0) ** 2
    print("P76.058 safe ratios: boundary vs prolate vs Xi^2, lambda=6")
    print("N boundaryErr prolateErr boundaryVsProlate")
    for n_modes in (6, 7, 8, 9, 10, 11, 12):
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)

        def boundary_raw(sigma):
            z = 1j * sigma
            return abs(entire_transfer(z, db, inner, x, L)) ** 2

        def prolate_raw(sigma):
            return abs(entire_vector(1j * sigma, coeff, idx, L)) ** 2

        b0 = boundary_raw(sigma0)
        p0 = prolate_raw(sigma0)
        berr = []
        perr = []
        bp = []
        for sigma in sigmas:
            target = xi_norm(-1j * sigma) ** 2 / target0
            bvalue = boundary_raw(sigma) / b0
            pvalue = prolate_raw(sigma) / p0
            berr.append(abs(bvalue - target) / abs(target))
            perr.append(abs(pvalue - target) / abs(target))
            bp.append(abs(bvalue - pvalue) / max(abs(pvalue), mp.mpf("1e-80")))
        print(
            f"{n_modes:2d} {mp.nstr(max(berr),9):>12} {mp.nstr(max(perr),9):>11}"
            f" {mp.nstr(max(bp),9):>17}"
        )


if __name__ == "__main__":
    run()
