#!/usr/bin/env python3
import sys
import math
import cmath
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_380_actual_packet_wwr_probe import setup  # noqa: E402


GAMMAS = [
    14.134725141734693790,
    21.022039638771554993,
    25.010857580145688763,
    30.424876125859513210,
    32.935061587739189691,
    37.586178158825671257,
]


def g_cancelled(w, d, xi, L):
    c = sum(xn / (1j * w - dn) for dn, xn in zip(d, xi))
    return (1.0 - cmath.exp(w * L)) * c


def cauchy(a, b):
    return 1.0 / (a + b)


def projection(off_nodes, crit_nodes, crit_vals):
    coo = np.array([[cauchy(a, b) for b in off_nodes] for a in off_nodes], dtype=complex)
    cok = np.array([[cauchy(a, k) for k in crit_nodes] for a in off_nodes], dtype=complex)
    return np.linalg.solve(coo, cok @ np.array(crit_vals, dtype=complex)), np.linalg.cond(coo)


def run():
    print("E72.396 Cauchy projection probe")
    print(" lam     L    nO nK   cond(COO)    max|GK|     max|Proj|   expWeighted")
    for lam, n_modes in [(8, 12), (10, 14), (12, 16), (14, 18)]:
        idx, d, L, xi = setup(lam, n_modes)
        crit_nodes = [1j * g for g in GAMMAS[:4]]
        crit_vals = [g_cancelled(k, d, xi, L) for k in crit_nodes]
        off_nodes = [0.20 + 1j * GAMMAS[0], 0.20 - 1j * GAMMAS[0]]
        proj, cond = projection(off_nodes, crit_nodes, crit_vals)
        weighted = max(abs(cmath.exp(a.real * L) * v) for a, v in zip(off_nodes, proj))
        print(
            f"{lam:4.0f} {L:7.3f} {len(off_nodes):4d} {len(crit_nodes):2d} "
            f"{cond:11.3e} {max(abs(x) for x in crit_vals):10.3e} "
            f"{max(abs(x) for x in proj):10.3e} {weighted:12.3e}"
        )


if __name__ == "__main__":
    run()
