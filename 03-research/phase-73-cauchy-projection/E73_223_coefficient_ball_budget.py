#!/usr/bin/env python3
import math
import sys
from collections import defaultdict

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


RHO_B = {
    (8, "1"): -55.67,
    (8, "1e6"): -45.98,
    (10, "1"): -52.16,
    (10, "1e6"): -43.11,
    (12, "1"): -49.87,
    (12, "1e6"): -41.26,
}


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def coefficient_maps(row, idx, d, L):
    n = len(idx)
    const = defaultdict(lambda: np.zeros(n, dtype=complex))
    linear = defaultdict(lambda: np.zeros(n, dtype=complex))
    for a in range(n):
        for b in range(n):
            coeff_to_eta_b = row[a]
            if a == b:
                omega = d[a]
                const[omega][b] += coeff_to_eta_b
                const[-omega][b] += coeff_to_eta_b
                linear[omega][b] += -coeff_to_eta_b / L
                linear[-omega][b] += -coeff_to_eta_b / L
            else:
                den = math.pi * (idx[b] - idx[a])
                const[d[a]][b] += coeff_to_eta_b / (2j * den)
                const[-d[a]][b] += -coeff_to_eta_b / (2j * den)
                const[d[b]][b] += -coeff_to_eta_b / (2j * den)
                const[-d[b]][b] += coeff_to_eta_b / (2j * den)
    return dict(const), dict(linear)


def bexp(z, L):
    return math.log(max(float(abs(z)), 1e-300)) / math.log(L)


def summarize(maps, eta, rho):
    max_center = 0.0
    max_rad = 0.0
    max_ratio = 0.0
    sum_abs = 0.0
    sum_rad = 0.0
    worst = None
    for omega, vec in maps.items():
        center = vec @ eta
        rad = norm(vec) * rho
        ratio = rad / max(abs(center), 1e-300)
        max_center = max(max_center, abs(center))
        max_rad = max(max_rad, rad)
        max_ratio = max(max_ratio, ratio)
        sum_abs += abs(center)
        sum_rad += rad
        if worst is None or ratio > worst[2]:
            worst = (omega, abs(center), ratio)
    return max_center, max_rad, max_ratio, sum_abs, sum_rad, worst


def run():
    print("E73.223 packet coefficient ball budget")
    print("For c_omega=u_omega eta and l_omega=v_omega eta, radius is ||u|| rho_eta.")
    print(
        " lam     L    N Csec gamma row kind modes maxCoeffB maxRadB "
        "sumCoeffB sumRadB maxRatio worstOmega"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for csec in ["1", "1e6"]:
            rho = float(L ** RHO_B[(lam, csec)])
            for gamma in GAMMAS[:2]:
                q = cauchy_rows(-1j * gamma, d)
                eta = (ident - projector(q)) @ xi
                for row_id in range(2):
                    const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                    for kind, maps in [("c", const_map), ("l", linear_map)]:
                        max_c, max_r, max_ratio, sum_c, sum_r, worst = summarize(maps, eta, rho)
                        print(
                            f"{lam:4d} {L:7.3f} {n_modes:4d} {csec:>4s}"
                            f" {gamma:7.2f} {row_id:3d} {kind:>4s}"
                            f" {len(maps):5d} {bexp(max_c, L):9.2f}"
                            f" {bexp(max_r, L):8.2f} {bexp(sum_c, L):9.2f}"
                            f" {bexp(sum_r, L):8.2f} {max_ratio:8.1e}"
                            f" {worst[0]:9.3f}"
                        )


if __name__ == "__main__":
    run()
