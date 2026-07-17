#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_106_post_main_source_probe import (  # noqa: E402
    int_exp_sin,
    int_r_exp_cos,
    von_mangoldt_upto,
)
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_107_spectral_divergence_probe import even_weighted_band  # noqa: E402
from E72_109_quadratic_flux_probe import centered_flux  # noqa: E402


def sigma_packet(L, d, tau):
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
    return np.concatenate([sigma, dsigma])


def lk_matrix(d, k):
    n = len(d)
    mat = np.zeros((n, 2 * n), dtype=complex)
    for m in range(n):
        for j in range(n):
            if j == m:
                continue
            mat[m, m] += k[j] / (d[m] - d[j])
            mat[m, j] += -k[j] / (d[m] - d[j])
        mat[m, n + m] = k[m]
    return mat


def weighted_even_matrix(idx, mask):
    rows = []
    for nval in idx[idx >= 0]:
        row = np.zeros(len(idx), dtype=complex)
        pos = np.where(idx == nval)[0][0]
        if mask[pos] == 0:
            continue
        row[pos] = 1.0 if nval == 0 else 2.0
        rows.append(row)
    return np.vstack(rows)


def cumulative_center_matrix(m):
    p0 = np.eye(m, dtype=complex)
    p0[-1, :] -= 1.0
    t = np.tril(np.ones((m - 1, m), dtype=complex))
    return t @ p0


def run():
    print("E72.112 operator split probe")
    print(" lam   N roots  max||Y||   max||R||   max prod   maxFlux2  relCheck")
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        roots = finite_roots(xi, d, hmax=6.0)
        if len(roots) == 0:
            continue
        mask = (np.abs(d) <= 8.0).astype(float)
        w = weighted_even_matrix(idx, mask)
        tcent = cumulative_center_matrix(w.shape[0])
        lk = lk_matrix(d, k)
        factor = 2.0 / (L * np.sqrt(np.exp(L)))
        qshort = bq @ solve(c_actual, bq.T)
        rmat_base = tcent @ w @ (mask[:, None] * qshort) @ (mask[:, None] * (factor * lk))

        max_y = 0.0
        max_r = 0.0
        max_prod = 0.0
        max_flux = 0.0
        max_rel = 0.0
        rnorm = svd(rmat_base, compute_uv=False)[0]
        for tau in roots[:6]:
            y = sigma_packet(L, d, tau)
            flux_vec = rmat_base @ y
            flux2 = norm(flux_vec)
            zpm = factor * (lk @ y)
            cpm = bq.T @ (mask * zpm)
            phi_full = mask * (bq @ solve(c_actual, cpm))
            phi_even = even_weighted_band(idx, phi_full, mask)
            _, flux2_direct, _ = centered_flux(phi_even)
            rel = abs(flux2 - flux2_direct) / max(flux2_direct, 1e-30)
            max_y = max(max_y, norm(y))
            max_r = max(max_r, rnorm)
            max_prod = max(max_prod, rnorm * norm(y))
            max_flux = max(max_flux, flux2)
            max_rel = max(max_rel, rel)
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots):5d} "
            f"{max_y:9.3e} {max_r:9.3e} {max_prod:10.3e} "
            f"{max_flux:9.3e} {max_rel:9.1e}"
        )


if __name__ == "__main__":
    run()
