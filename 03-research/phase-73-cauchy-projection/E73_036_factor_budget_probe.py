#!/usr/bin/env python3
import sys
import cmath
import math
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return d, L, xi


def confluent_matrix(a, m):
    mat = np.zeros((m, m), dtype=complex)
    for q in range(m):
        for p in range(m):
            mat[q, p] = ((-1) ** q) * math.comb(p + q, p) / ((2 * a) ** (p + q + 1))
    return mat


def qjet_coeff(a, k, m):
    return np.array([((-1) ** q) / ((a + k) ** (q + 1)) for q in range(m)], dtype=complex)


def hcoeff_for_k(a, k, m):
    return np.linalg.solve(confluent_matrix(a, m), qjet_coeff(a, k, m))


def hermite_norm(vec):
    return sum(abs(c) / math.factorial(i) for i, c in enumerate(vec))


def raw_cauchy(gamma, d, xi):
    return np.sum(xi / (-gamma - d))


def phase_multiplier(gamma, L):
    return 1.0 - cmath.exp(1j * gamma * L)


def factor_rows(lam, n_modes, sigma, gamma0, m, ncrit):
    d, L, xi = setup_full(lam, n_modes)
    a = sigma + 1j * gamma0
    crit_gammas = GAMMAS[:ncrit]
    crit_nodes = [1j * g for g in crit_gammas]
    hmat = np.column_stack([hcoeff_for_k(a, k, m) for k in crit_nodes])
    raw = np.array([raw_cauchy(g, d, xi) for g in crit_gammas], dtype=complex)
    mesh = np.array([phase_multiplier(g, L) for g in crit_gammas], dtype=complex)
    gdata = np.array([g_cancelled(1j * g, d, xi, L) for g in crit_gammas], dtype=complex)

    out = hmat @ gdata
    projected = math.exp(sigma * L) * hermite_norm(out)

    abs_budget = math.exp(sigma * L) * sum(
        hermite_norm(hmat[:, j]) * abs(mesh[j]) * abs(raw[j]) for j in range(ncrit)
    )
    raw_only_budget = math.exp(sigma * L) * sum(
        hermite_norm(hmat[:, j]) * abs(raw[j]) for j in range(ncrit)
    )
    mesh_only_budget = math.exp(sigma * L) * max(abs(raw[j]) for j in range(ncrit)) * sum(
        hermite_norm(hmat[:, j]) * abs(mesh[j]) for j in range(ncrit)
    )
    herm_ceiling = math.exp(sigma * L) * max(abs(g) for g in gdata) * sum(
        hermite_norm(hmat[:, j]) for j in range(ncrit)
    )
    l1_ratio = projected / max(abs_budget, 1e-300)
    best_k = int(np.argmax([hermite_norm(hmat[:, j]) * abs(mesh[j]) * abs(raw[j]) for j in range(ncrit)]))
    return {
        "lam": lam,
        "L": L,
        "sigma": sigma,
        "gamma0": gamma0,
        "m": m,
        "ncrit": ncrit,
        "projected": projected,
        "abs_budget": abs_budget,
        "raw_only": raw_only_budget,
        "mesh_only": mesh_only_budget,
        "herm_ceiling": herm_ceiling,
        "l1_ratio": l1_ratio,
        "best_gamma": crit_gammas[best_k],
        "best_mesh": abs(mesh[best_k]),
        "best_raw": abs(raw[best_k]),
    }


def run():
    print("E73.036 factor budget probe")
    print("Audits whether CRIT-DIV-FACT survives absolute factor budgets after Hermite projection.")
    print(
        " lam     L sigma  gamma0  m nK    projected    absBudget   ratio"
        "    rawOnly    meshOnly    hermCeil  bestGamma  bestMesh    bestRaw"
    )
    cases = []
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18), (16, 20), (18, 22), (20, 24), (24, 28)]:
        for sigma, gamma0, m in [(0.05, GAMMAS[0], 2), (0.10, GAMMAS[0], 2), (0.20, GAMMAS[0], 3), (0.20, GAMMAS[1], 3)]:
            cases.append((lam, n_modes, sigma, gamma0, m, 6))
    for case in cases:
        row = factor_rows(*case)
        print(
            f"{row['lam']:4d} {row['L']:7.3f} {row['sigma']:5.2f} {row['gamma0']:7.2f}"
            f" {row['m']:2d} {row['ncrit']:2d} {row['projected']:12.3e}"
            f" {row['abs_budget']:12.3e} {row['l1_ratio']:7.2e}"
            f" {row['raw_only']:10.3e} {row['mesh_only']:10.3e}"
            f" {row['herm_ceiling']:10.3e} {row['best_gamma']:10.3f}"
            f" {row['best_mesh']:10.3e} {row['best_raw']:10.3e}"
        )


if __name__ == "__main__":
    run()
