#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_106_post_main_source_probe import post_main_source  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_107_spectral_divergence_probe import even_weighted_band  # noqa: E402


def centered_flux(phi):
    mass = np.sum(phi)
    centered = phi.copy()
    centered[-1] -= mass
    flux = np.cumsum(centered[:-1])
    return mass, norm(flux), len(flux)


def run():
    print("E72.109 quadratic centered flux probe")
    print(" lam   N roots  max|D2pm|  max|mass|   max Flux2   max hsqrtMFlux2")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        h = 2 * np.pi / L
        mask = (np.abs(d) <= 8.0).astype(float)
        max_d2 = 0.0
        max_mass = 0.0
        max_flux2 = 0.0
        max_scaled = 0.0
        for tau in roots[:6]:
            kpm, _ = post_main_source(L, n_modes, tau)
            zpm = (2.0 / (L * np.sqrt(np.exp(L)))) * (kpm @ k)
            cpm = bq.T @ (mask * zpm)
            y = solve(c_actual, cpm)
            phi_full = mask * (bq @ y)
            phi_even = even_weighted_band(idx, phi_full, mask)
            mass, flux2, m = centered_flux(phi_even)
            a = bq.T @ (10.0 / (10.0 * 10.0 - d * d))
            d2pm = np.vdot(a, y)
            max_d2 = max(max_d2, abs(d2pm))
            max_mass = max(max_mass, abs(mass))
            max_flux2 = max(max_flux2, flux2)
            max_scaled = max(max_scaled, h * np.sqrt(max(m, 1)) * flux2)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_d2:10.3e} {max_mass:10.3e} {max_flux2:11.3e} {max_scaled:16.3e}"
        )


if __name__ == "__main__":
    run()
