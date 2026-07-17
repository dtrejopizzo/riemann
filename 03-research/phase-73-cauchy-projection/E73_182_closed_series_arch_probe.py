#!/usr/bin/env python3
import math
import sys
from collections import defaultdict

import numpy as np
from numpy.linalg import eigh, lstsq, norm
from scipy.integrate import quad
from scipy.special import polygamma

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import GAMMA, LOG4PI, build  # noqa: E402
from E72_380_actual_packet_wwr_probe import q_matrix_fast  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_model, idx.astype(int), d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def exp_int(lam, L):
    if abs(lam) < 1e-12:
        return L + 0j
    return (np.exp(lam * L) - 1.0) / lam


def y_exp_int(lam, L):
    if abs(lam) < 1e-12:
        return 0.5 * L * L + 0j
    return (np.exp(lam * L) * (lam * L - 1.0) + 1.0) / (lam * lam)


def packet_modes(row, idx, d, xi, L):
    const = defaultdict(complex)
    linear = defaultdict(complex)
    n = len(idx)
    for a in range(n):
        for b in range(n):
            coeff = row[a] * xi[b]
            if a == b:
                omega = d[a]
                const[omega] += coeff
                const[-omega] += coeff
                linear[omega] += -coeff / L
                linear[-omega] += -coeff / L
            else:
                den = math.pi * (idx[b] - idx[a])
                # sin(da y)-sin(db y) over den.
                const[d[a]] += coeff / (2j * den)
                const[-d[a]] += -coeff / (2j * den)
                const[d[b]] += -coeff / (2j * den)
                const[-d[b]] += coeff / (2j * den)
    return dict(const), dict(linear)


def eval_modes(const, linear, y):
    total = 0j
    for om, c in const.items():
        total += c * np.exp(1j * om * y)
    for om, c in linear.items():
        total += c * y * np.exp(1j * om * y)
    return total


def derivative0_modes(const, linear):
    total = 0j
    for om, c in const.items():
        total += 1j * om * c
    for _om, c in linear.items():
        total += c
    return total


def second_derivative0_modes(const, linear):
    total = 0j
    for om, c in const.items():
        total += -(om * om) * c
    for om, c in linear.items():
        total += 2j * om * c
    return total


def integrate_modes(const, linear, alpha, L):
    total = 0j
    for om, c in const.items():
        total += c * exp_int(alpha + 1j * om, L)
    for om, c in linear.items():
        total += c * y_exp_int(alpha + 1j * om, L)
    return total


def odd_square_tail(r_terms):
    # sum_{r=r_terms}^infty 1/(2r+1)^2 = (1/4) psi_1(r_terms+1/2).
    return 0.25 * float(polygamma(1, r_terms + 0.5))


def odd_cube_tail(r_terms):
    # sum_{r=r_terms}^infty 1/(2r+1)^3 = -(1/16) psi_2(r_terms+1/2).
    return -0.0625 * float(polygamma(2, r_terms + 0.5))


def arch_closed_series(row, idx, d, L, xi, r_terms=80, accel=True):
    const, linear = packet_modes(row, idx, d, xi, L)
    b0 = eval_modes(const, linear, 0.0)
    bp0 = derivative0_modes(const, linear)
    bpp0 = second_derivative0_modes(const, linear)
    c1 = bp0 + 0.5 * b0
    c2 = 0.5 * bpp0 + 0.5 * bp0 + 0.125 * b0
    w02 = integrate_modes(const, linear, 0.5, L) + integrate_modes(const, linear, -0.5, L)
    wra = 0j
    for r in range(r_terms):
        # 1/(2sinh y)=sum_{r>=0} exp(-(2r+1)y).
        wra += integrate_modes(const, linear, -(2 * r + 0.5), L)
        wra -= b0 * exp_int(-(2 * r + 1.0), L)
    if accel:
        # Near zero the summand has leading term c1*y*exp(-(2r+1)y).
        # The omitted upper endpoint exponential is negligible at this scale;
        # adding the quadratic term leaves an O(sum (2r+1)^-4) tail.
        wra += c1 * odd_square_tail(r_terms)
        wra += 2.0 * c2 * odd_cube_tail(r_terms)
    wrb = b0 * 0.5 * np.log(np.tanh(L / 2.0))
    wr = 0.5 * (LOG4PI + GAMMA) * b0 + wra + wrb
    return w02 - wr


def arch_quad(row, idx, d, L, xi):
    def b(y):
        return row @ (q_matrix_fast(idx, d, L, y) @ xi)

    b0 = b(0.0)
    h = min(1e-6, L * 1e-7)
    db0 = (b(h) - b0) / h

    def wri(y):
        if y < 1e-8:
            return (db0 + b0 / 2.0) / 2.0
        return (np.exp(y / 2.0) * b(y) - b0) / (2.0 * np.sinh(y))

    w02_re, _ = quad(lambda y: np.real(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    w02_im, _ = quad(lambda y: np.imag(b(y) * (np.exp(y / 2.0) + np.exp(-y / 2.0))), 0, L, limit=250)
    wra_re, _ = quad(lambda y: np.real(wri(y)), 0, L, limit=250)
    wra_im, _ = quad(lambda y: np.imag(wri(y)), 0, L, limit=250)
    wr = 0.5 * (LOG4PI + GAMMA) * b0 + (wra_re + 1j * wra_im) + b0 * 0.5 * np.log(np.tanh(L / 2.0))
    return (w02_re + 1j * w02_im) - wr


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def run():
    print("E73.182 closed-series archimedean probe")
    print("Compares arch matrix, quadrature, and closed exponential-series evaluation.")
    print(" lam     L gamma row modes   matB quadErr seriesErr seriesQuadErr")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28)]:
        h_model, idx, d, L, xi = setup(lam, n_modes)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            for j in range(2):
                const, linear = packet_modes(plane[j], idx, d, xi, L)
                mat = plane[j] @ (h_model @ xi)
                quad_val = arch_quad(plane[j], idx, d, L, xi)
                series_val = arch_closed_series(plane[j], idx, d, L, xi, r_terms=120, accel=True)
                qerr = abs(quad_val - mat) / max(abs(mat), 1e-300)
                serr = abs(series_val - mat) / max(abs(mat), 1e-300)
                sqerr = abs(series_val - quad_val) / max(abs(quad_val), 1e-300)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {len(const)+len(linear):5d} {bexp(mat, L):6.2f}"
                    f" {qerr:7.1e} {serr:9.1e} {sqerr:13.1e}"
                )


if __name__ == "__main__":
    run()
