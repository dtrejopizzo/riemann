#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_106_post_main_source_probe import post_main_source  # noqa: E402
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402


def even_weighted_nonnegative(idx, vec):
    vals = []
    for n in idx[idx >= 0]:
        j = np.where(idx == n)[0][0]
        if n == 0:
            vals.append(vec[j])
        else:
            vals.append(2.0 * vec[j])
    return np.array(vals, dtype=complex)


def even_weighted_band(idx, vec, mask):
    vals = []
    for n in idx[idx >= 0]:
        j = np.where(idx == n)[0][0]
        if mask[j] == 0:
            continue
        if n == 0:
            vals.append(vec[j])
        else:
            vals.append(2.0 * vec[j])
    return np.array(vals, dtype=complex)


def flux_metrics(phi):
    mass = np.sum(phi)
    phi0 = phi.copy()
    phi0[-1] -= mass
    flux = np.cumsum(phi0[:-1])
    return mass, np.sum(np.abs(flux)), norm(phi), norm(phi0)


def run():
    print("E72.107 spectral-divergence probe for post-main cofactor")
    print(" lam   N roots  max|D2pm|    max|mass|   max h||flux||1   max ||phi||")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        h = 2 * np.pi / L
        mask = (np.abs(d) <= 8.0).astype(float)
        max_d2 = 0.0
        max_mass = 0.0
        max_flux = 0.0
        max_phi = 0.0
        for tau in roots[:6]:
            kpm, _ = post_main_source(L, n_modes, tau)
            zpm = (2.0 / (L * np.sqrt(np.exp(L)))) * (kpm @ k)
            cpm = bq.T @ (mask * zpm)
            y = solve(c_actual, cpm)
            phi_full = bq @ y
            phi_band = mask * phi_full
            phi_even = even_weighted_band(idx, phi_band, mask)
            mass, flux_l1, phi_norm, _ = flux_metrics(phi_even)
            a = bq.T @ (10.0 / (10.0 * 10.0 - d * d))
            d2pm = np.vdot(a, y)
            max_d2 = max(max_d2, abs(d2pm))
            max_mass = max(max_mass, abs(mass))
            max_flux = max(max_flux, h * flux_l1)
            max_phi = max(max_phi, phi_norm)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_d2:10.3e} {max_mass:11.3e} {max_flux:15.3e} {max_phi:12.3e}"
        )


if __name__ == "__main__":
    run()
