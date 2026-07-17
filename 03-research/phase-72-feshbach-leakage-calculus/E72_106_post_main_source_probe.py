#!/usr/bin/env python3
import numpy as np


def von_mangoldt_upto(nmax):
    lam = np.zeros(nmax + 1)
    is_prime = np.ones(nmax + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, nmax + 1):
        if not is_prime[p]:
            continue
        for m in range(p * p, nmax + 1, p):
            is_prime[m] = False
        q = p
        lp = np.log(p)
        while q <= nmax:
            lam[q] = lp
            if q > nmax // p:
                break
            q *= p
    return lam


def int_exp_sin(a, d, L):
    # int_0^L exp(-a r) sin(d r) dr
    if abs(d) < 1e-14:
        return 0.0j
    return (
        (1.0 - np.exp(-(a - 1j * d) * L)) / (a - 1j * d)
        - (1.0 - np.exp(-(a + 1j * d) * L)) / (a + 1j * d)
    ) / (2j)


def int_r_exp_cos(a, d, L):
    # int_0^L r exp(-a r) cos(d r) dr
    def j(b):
        if abs(b) < 1e-14:
            return 0.5 * L * L
        return (1.0 - np.exp(-b * L) * (1.0 + b * L)) / (b * b)

    return 0.5 * (j(a - 1j * d) + j(a + 1j * d))


def loewner_matrix_from_sigma(d, sigma, dsigma):
    n = len(d)
    out = np.empty((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            if i == j:
                out[i, j] = dsigma[i]
            else:
                out[i, j] = (sigma[i] - sigma[j]) / (d[i] - d[j])
    return out


def lo_r_matrix(d, r):
    n = len(d)
    s = np.sin(d * r)
    out = np.empty((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            if i == j:
                out[i, j] = r * np.cos(d[i] * r)
            else:
                out[i, j] = (s[i] - s[j]) / (d[i] - d[j])
    return out


def post_main_source(L, n_modes, tau):
    idx = np.arange(-n_modes, n_modes + 1)
    d = 2 * np.pi * idx / L
    x = np.exp(L)
    nmax = int(np.floor(x))
    lam = von_mangoldt_upto(nmax)
    ns = np.nonzero(lam > 0)[0]
    r = L - np.log(ns)
    weights = lam[ns] * np.exp(-1j * tau * r)

    k_direct = np.zeros((len(d), len(d)), dtype=complex)
    sigma_disc = np.zeros(len(d), dtype=complex)
    dsigma_disc = np.zeros(len(d), dtype=complex)
    for rr, ww in zip(r, weights):
        k_direct += ww * lo_r_matrix(d, rr)
        sigma_disc += ww * np.sin(d * rr)
        dsigma_disc += ww * rr * np.cos(d * rr)

    a = 1.0 + 1j * tau
    sigma_cont = np.array([int_exp_sin(a, dd, L) for dd in d])
    dsigma_cont = np.array([int_r_exp_cos(a, dd, L) for dd in d])
    sigma = sigma_disc - x * sigma_cont
    dsigma = dsigma_disc - x * dsigma_cont

    k_cont = loewner_matrix_from_sigma(d, sigma_cont, dsigma_cont)
    k_direct -= x * k_cont
    k_sigma = loewner_matrix_from_sigma(d, sigma, dsigma)
    return k_direct, k_sigma


def run():
    print("E72.106 post-main source identity probe")
    print("   L modes   tau      relFrob      maxAbs")
    for L, n_modes in [(6.0, 6), (8.0, 8), (10.0, 10), (12.0, 12)]:
        for tau in [0.7, 2.1, 4.0]:
            k_direct, k_sigma = post_main_source(L, n_modes, tau)
            diff = k_direct - k_sigma
            rel = np.linalg.norm(diff) / max(np.linalg.norm(k_direct), 1e-30)
            mx = np.max(np.abs(diff))
            print(f"{L:4.1f} {n_modes:5d} {tau:6.2f}  {rel:10.3e}  {mx:10.3e}")


if __name__ == "__main__":
    run()
