#!/usr/bin/env python3
import math
import sys
from collections import defaultdict

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def closed_distribution_maps(row, idx, d, L):
    n = len(idx)
    mass = defaultdict(lambda: np.zeros(n, dtype=complex))
    deriv = defaultdict(lambda: np.zeros(n, dtype=complex))
    for b in range(n):
        rb = row[b]
        mass[d[b]][b] += rb
        mass[-d[b]][b] += rb
        # T contains i*l delta'.  Since l_{+-d_b,b}=-r_b/L,
        # derivative coefficient is -i*r_b/L.
        deriv[d[b]][b] += -1j * rb / L
        deriv[-d[b]][b] += -1j * rb / L

    for j in range(n):
        rj = row[j]
        for b in range(n):
            if j == b:
                continue
            den = 2j * math.pi * (idx[b] - idx[j])
            coeff = rj / den
            mass[d[j]][b] += coeff
            mass[-d[j]][b] += -coeff
            mass[d[b]][b] += -coeff
            mass[-d[b]][b] += coeff
    return dict(mass), dict(deriv)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.304 closed spectral distribution")
    print("Checks closed cell formula for T against coefficient_maps and W pairing.")
    print(" lam      L gamma row mapErrB centerErrB centerB closedB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                row = Q[row_id]
                c_map, l_map = coefficient_maps(row, idx, d, L)
                mass, deriv = closed_distribution_maps(row, idx, d, L)
                all_omega = sorted(set(c_map) | set(l_map) | set(mass) | set(deriv))
                map_err = 0.0
                map_den = 0.0
                center = 0j
                closed = 0j
                for om in all_omega:
                    c_vec = c_map.get(om, np.zeros(len(idx), dtype=complex))
                    l_vec = l_map.get(om, np.zeros(len(idx), dtype=complex))
                    m_vec = mass.get(om, np.zeros(len(idx), dtype=complex))
                    # T derivative coefficient should be i*l.
                    d_vec = deriv.get(om, np.zeros(len(idx), dtype=complex))
                    map_err += np.linalg.norm(m_vec - c_vec) ** 2
                    map_err += np.linalg.norm(d_vec - 1j * l_vec) ** 2
                    map_den += np.linalg.norm(c_vec) ** 2 + np.linalg.norm(l_vec) ** 2

                    w = complex(cache.setdefault((lam, float(L), float(om), "c"), weight(lam, L, om, "c")))
                    v = complex(cache.setdefault((lam, float(L), float(om), "l"), weight(lam, L, om, "l")))
                    center += (c_vec @ eta) * w + (l_vec @ eta) * v
                    # <delta',W>=-W'= -i V, so deriv delta' contributes deriv*(-iV).
                    closed += (m_vec @ eta) * w + (d_vec @ eta) * (-1j * v)
                rel = math.sqrt(map_err / max(map_den, 1e-300))
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(rel, L):8.2f} {bexp(center-closed, L):10.2f}"
                    f" {bexp(center, L):8.2f} {bexp(closed, L):8.2f}"
                )


if __name__ == "__main__":
    run()
