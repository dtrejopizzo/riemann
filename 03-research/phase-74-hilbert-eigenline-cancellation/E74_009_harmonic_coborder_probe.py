#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-74-hilbert-eigenline-cancellation")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import cauchy_rows, projector  # noqa: E402
from E74_002_closed_mesh_action_probe import harmonic_symbol, hilbert_mesh  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(H)
    mu = vals[0]
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, float(mu), xi


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def row_fit(target, images):
    if not images:
        return np.zeros_like(target)
    M = np.vstack(images).T
    coeff, *_ = np.linalg.lstsq(M, target.T, rcond=None)
    return coeff @ np.vstack(images)


def primitive_rows(Q, idx, d, gamma, degree, rat_power, include_harmonic):
    rows = []
    A = hilbert_mesh(idx)
    for row_id in range(2):
        base = Q[row_id].copy()
        beta = gamma * CURRENT_L / (2.0 * math.pi)
        if row_id == 1:
            beta = -beta
        Hsym = harmonic_symbol(idx, beta)
        seeds = [base]
        if include_harmonic:
            seeds.extend([base * Hsym, base @ A])
        for seed in seeds:
            for k in range(degree + 1):
                rows.append((d**k) * seed)
        if rat_power > 0:
            betas = [abs(gamma), 2.0 * math.pi / CURRENT_L, 1.0]
            for b in betas:
                den = d * d + b * b
                for m in range(1, rat_power + 1):
                    for seed in seeds:
                        for k in range(degree + 1):
                            rows.append((d**k) * seed / (den**m))
    return rows


def audit_module(rho, E, xi, L, rows):
    images = [row @ E for row in rows]
    approx = row_fit(rho, images)
    res = rho - approx
    return approx, res, norm(res) / max(norm(rho), 1e-300), bexp(res @ xi, L)


def run():
    print("E74.9 harmonic left-coborder probe")
    print("Target rho=qH(I-P). Fit rho by Y(H-mu I) with fixed non-tautological modules.")
    print("harm adds q*H_beta and q*A, where A q^* = H_beta q^* is the new E74 structure.")
    print(
        " lam      L gamma row module dim centerB resPairB resRel projRel"
    )
    configs = [
        ("poly", 2, 0, False),
        ("rat", 2, 1, False),
        ("harm", 2, 0, True),
        ("harmRat", 2, 1, True),
        ("harmHi", 3, 1, True),
    ]
    global CURRENT_L
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20), (20, 24)]:
        H, idx, d, L, mu, xi = setup(lam, n_modes)
        CURRENT_L = L
        I = np.eye(len(idx), dtype=complex)
        E = H - mu * I
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            R = I - projector(Q)
            for row_id in range(2):
                rho = Q[row_id] @ H @ R
                center = rho @ xi
                rho_norm = norm(rho)
                for name, deg, rat_power, include_harmonic in configs:
                    rows = primitive_rows(Q, idx, d, gamma, deg, rat_power, include_harmonic)
                    approx, res, res_rel, res_pair_b = audit_module(rho, E, xi, L, rows)
                    proj_rel = norm(approx) / max(rho_norm, 1e-300)
                    print(
                        f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                        f" {name:7s} {len(rows):4d}"
                        f" {bexp(center, L):8.2f}"
                        f" {res_pair_b:8.2f}"
                        f" {res_rel:7.1e}"
                        f" {proj_rel:7.1e}"
                    )


if __name__ == "__main__":
    run()
