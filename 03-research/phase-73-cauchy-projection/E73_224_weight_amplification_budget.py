#!/usr/bin/env python3
import sys

import mpmath as mp
import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
import E73_201_mp_finite_assembly_probe as mpff  # noqa: E402
from E73_223_coefficient_ball_budget import RHO_B, coefficient_maps, cauchy_rows, projector  # noqa: E402


mp.mp.dps = 80


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def weight(lam, L, omega, kind):
    if kind == "c":
        const = {omega: 1.0 + 0j}
        linear = {}
    else:
        const = {}
        linear = {omega: 1.0 + 0j}
    return mpff.mp_arch_closed_digamma(const, linear, L, 80) - mpff.mp_prime_modes(
        const, linear, L, lam
    )


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def run():
    print("E73.224 weight amplification budget")
    print("Uses W,V centers to measure sum |W|rad(c)+sum |V|rad(l).")
    print(" lam     L    N Csec gamma row maxWB maxVB sumWradCB sumVradLB totalB centerB ratio")
    cache = {}
    for lam, n_modes in [(8, 6), (10, 8), (12, 10)]:
        idx, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(idx), dtype=complex)
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (ident - projector(q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(q[row_id], idx, d, L)
                weights_c = {}
                weights_l = {}
                for omega in const_map:
                    key = (lam, float(L), float(omega), "c")
                    weights_c[omega] = cache.setdefault(key, weight(lam, L, omega, "c"))
                for omega in linear_map:
                    key = (lam, float(L), float(omega), "l")
                    weights_l[omega] = cache.setdefault(key, weight(lam, L, omega, "l"))
                center = sum((vec @ eta) * complex(weights_c[om]) for om, vec in const_map.items())
                center += sum((vec @ eta) * complex(weights_l[om]) for om, vec in linear_map.items())
                max_w = max(abs(complex(v)) for v in weights_c.values())
                max_v = max(abs(complex(v)) for v in weights_l.values())
                for csec in ["1", "1e6"]:
                    rho = float(L ** RHO_B[(lam, csec)])
                    sum_wrc = 0.0
                    sum_vrl = 0.0
                    for om, vec in const_map.items():
                        sum_wrc += abs(complex(weights_c[om])) * norm(vec) * rho
                    for om, vec in linear_map.items():
                        sum_vrl += abs(complex(weights_l[om])) * norm(vec) * rho
                    total = sum_wrc + sum_vrl
                    ratio = total / max(abs(center), 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {n_modes:4d} {csec:>4s}"
                        f" {gamma:7.2f} {row_id:3d}"
                        f" {bexp(max_w, L):6.2f} {bexp(max_v, L):6.2f}"
                        f" {bexp(sum_wrc, L):9.2f} {bexp(sum_vrl, L):9.2f}"
                        f" {bexp(total, L):7.2f} {bexp(center, L):7.2f}"
                        f" {ratio:8.1e}"
                    )


if __name__ == "__main__":
    run()
