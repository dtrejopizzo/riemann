#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_106_post_main_source_probe import (  # noqa: E402
    int_exp_sin,
    int_r_exp_cos,
    von_mangoldt_upto,
)
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def packet_parts(L, d, tau):
    x = np.exp(L)
    nmax = int(np.floor(x))
    lam = von_mangoldt_upto(nmax)
    ns = np.nonzero(lam > 0)[0]
    r = L - np.log(ns)
    weights = lam[ns] * np.exp(-1j * tau * r)
    sigma_disc = np.zeros(len(d), dtype=complex)
    dsigma_disc = np.zeros(len(d), dtype=complex)
    for rr, ww in zip(r, weights):
        sigma_disc += ww * np.sin(d * rr)
        dsigma_disc += ww * rr * np.cos(d * rr)
    a = 1.0 + 1j * tau
    sigma_cont = np.array([int_exp_sin(a, dd, L) for dd in d])
    dsigma_cont = np.array([int_r_exp_cos(a, dd, L) for dd in d])
    sigma = sigma_disc - x * sigma_cont
    dsigma = dsigma_disc - x * dsigma_cont
    return sigma, dsigma, sigma_disc, dsigma_disc, x * sigma_cont, x * dsigma_cont


def run():
    print("E72.124 packet component probe")
    print(
        " lam   L roots  ||Y||/(sqrtxL)  sigma%  dsigma%  "
        "disc/cont sigma  disc/cont dsigma"
    )
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        sqrtx = np.sqrt(np.exp(L))
        max_y_scaled = 0.0
        max_sigma_frac = 0.0
        max_dsigma_frac = 0.0
        max_sc_ratio = 0.0
        max_dc_ratio = 0.0
        for tau in roots[:6]:
            sigma, dsigma, sd, dsd, sc, dsc = packet_parts(L, d, tau)
            y_norm = np.sqrt(norm(sigma) ** 2 + norm(dsigma) ** 2)
            if y_norm == 0:
                continue
            max_y_scaled = max(max_y_scaled, y_norm / (sqrtx * L))
            max_sigma_frac = max(max_sigma_frac, norm(sigma) / y_norm)
            max_dsigma_frac = max(max_dsigma_frac, norm(dsigma) / y_norm)
            max_sc_ratio = max(max_sc_ratio, norm(sd) / max(norm(sc), 1e-30))
            max_dc_ratio = max(max_dc_ratio, norm(dsd) / max(norm(dsc), 1e-30))
        print(
            f"{lam:4.0f} {L:5.2f} {len(roots):5d} "
            f"{max_y_scaled:15.3e} {max_sigma_frac:7.3f} {max_dsigma_frac:8.3f} "
            f"{max_sc_ratio:15.3e} {max_dc_ratio:17.3e}"
        )


if __name__ == "__main__":
    run()
