#!/usr/bin/env python3
import sys
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS, g_cancelled  # noqa: E402


def d_o(s, off_nodes):
    out = 1.0 + 0j
    for b in off_nodes:
        out *= s + b
    return out


def d_o_prime_at_minus(b, off_nodes):
    out = 1.0 + 0j
    for c in off_nodes:
        if c != b:
            out *= -b + c
    return out


def ell(a, s, off_nodes):
    out = 1.0 + 0j
    for c in off_nodes:
        if c != a:
            out *= (s - c) / (a - c)
    return out


def q_k(a, crit_nodes, crit_vals):
    return sum(g / (a + k) for k, g in zip(crit_nodes, crit_vals))


def rational_projection(off_nodes, crit_nodes, crit_vals):
    rows = []
    for b in off_nodes:
        total = 0j
        for a in off_nodes:
            total += q_k(a, crit_nodes, crit_vals) * d_o(a, off_nodes) * ell(a, -b, off_nodes)
        rows.append(total / d_o_prime_at_minus(b, off_nodes))
    return np.array(rows, dtype=complex)


def matrix_projection(off_nodes, crit_nodes, crit_vals):
    coo = np.array([[1.0 / (a + b) for b in off_nodes] for a in off_nodes], dtype=complex)
    cok = np.array([[1.0 / (a + k) for k in crit_nodes] for a in off_nodes], dtype=complex)
    return np.linalg.solve(coo, cok @ np.array(crit_vals, dtype=complex))


def run():
    print("E73.002 rational Cauchy projection probe")
    print(" lam     L    nO nK    |mat|       |rat|       absErr     relErr")
    off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0], 0.20 + 1j * GAMMAS[1]]
    crit_nodes = [1j * g for g in GAMMAS[:5]]
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        crit_vals = [g_cancelled(k, d, xi, L) for k in crit_nodes]
        mat = matrix_projection(off_nodes, crit_nodes, crit_vals)
        rat = rational_projection(off_nodes, crit_nodes, crit_vals)
        err = np.linalg.norm(mat - rat)
        den = max(np.linalg.norm(mat), 1e-30)
        print(
            f"{lam:4.0f} {L:7.3f} {len(off_nodes):4d} {len(crit_nodes):2d} "
            f"{np.linalg.norm(mat):10.3e} {np.linalg.norm(rat):10.3e} "
            f"{err:10.3e} {err/den:10.3e}"
        )


if __name__ == "__main__":
    run()
