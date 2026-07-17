#!/usr/bin/env python3
"""Extrapolate the fixed-L boundary safe ratio using its 1/N shell tail."""

import numpy as np
import mpmath as mp

from P76_002_mp_entry_audit import build_mp
from P76_009_prolate_overlap_probe import coefficients
from P76_018_boundary_characteristic_probe import entire_transfer, right_transfer_data, xi_norm
from P76_058_prolate_safe_ratio import entire_vector


def run():
    mp.mp.dps = 60
    max_modes = 15
    Hmax, idxmax, L = build_mp(6, max_modes, 60)
    coeff = coefficients(mp.mpf(6), max_modes, L)
    sigma0 = mp.mpf("1")
    sigmas = [mp.mpf(v) for v in ("0.6", "0.75", "1.5", "2")]
    ns = list(range(10, 16))
    samples = {sigma: [] for sigma in sigmas}
    for n_modes in ns:
        offset = max_modes - n_modes
        H = Hmax[offset : Hmax.rows - offset, offset : Hmax.cols - offset]
        idx = idxmax[offset : len(idxmax) - offset]
        db, inner, x = right_transfer_data(H, idx)
        base = abs(entire_transfer(1j * sigma0, db, inner, x, L)) ** 2
        for sigma in sigmas:
            value = abs(entire_transfer(1j * sigma, db, inner, x, L)) ** 2 / base
            samples[sigma].append(float(value))

    design = np.array([[1.0, 1.0 / n, 1.0 / (n * n)] for n in ns])
    print("P76.059 boundary safe-ratio 1/N extrapolation, lambda=6")
    print("sigma extrap-vs-prolate extrap-vs-Xi fittedA fittedB")
    pbase = abs(entire_vector(1j * sigma0, coeff, list(range(-max_modes, max_modes + 1)), L)) ** 2
    xbase = xi_norm(-1j * sigma0) ** 2
    for sigma in sigmas:
        fit, *_ = np.linalg.lstsq(design, np.array(samples[sigma]), rcond=None)
        intercept, aa, bb = fit
        pvalue = float(
            abs(entire_vector(1j * sigma, coeff, list(range(-max_modes, max_modes + 1)), L)) ** 2
            / pbase
        )
        xvalue = float(xi_norm(-1j * sigma) ** 2 / xbase)
        print(
            f"{float(sigma):4.2f} {abs(intercept-pvalue)/abs(pvalue):17.7e}"
            f" {abs(intercept-xvalue)/abs(xvalue):13.7e} {aa:9.3e} {bb:9.3e}"
        )


if __name__ == "__main__":
    run()
