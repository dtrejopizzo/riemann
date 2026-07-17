#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build, primes_upto  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_193_balanced_ramp_probe import functional, r0, r1  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return H.astype(complex), idx.astype(int), d, L, xi.astype(complex)


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def eval_coeffs(const_map, linear_map, eta, y):
    total = 0j
    for om, vec in const_map.items():
        total += (vec @ eta) * np.exp(1j * om * y)
    for om, vec in linear_map.items():
        total += y * (vec @ eta) * np.exp(1j * om * y)
    return total


def deriv0_coeffs(const_map, linear_map, eta):
    total = 0j
    for om, vec in const_map.items():
        total += 1j * om * (vec @ eta)
    for _om, vec in linear_map.items():
        total += vec @ eta
    return total


def run():
    print("E73.237 balanced coefficient second-Abel bridge")
    print("Checks derivative moment, rank-one source, and neutral balanced ramp.")
    print(" lam      L gamma row BpCoeffB BpRankB diffB FstarB FdiffB bal0B balp0B balLB")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        H, idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c_bal = -f0 / f1
        fstar = f0 + c_bal * f1
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                row = Q[row_id]
                const_map, linear_map = coefficient_maps(row, idx, d, L)
                bp_coeff = deriv0_coeffs(const_map, linear_map, eta)
                bp_rank = -(2.0 / L) * np.sum(row) * np.sum(eta)
                # Functional neutrality: F[B - Bp r*] - F[B] = -Bp F[r*].
                fdiff = -bp_coeff * fstar
                bal0 = eval_coeffs(const_map, linear_map, eta, 0.0) - bp_coeff * (
                    r0(0.0, L) + c_bal * r1(0.0, L)
                )
                # Compute derivative of balanced packet symbolically at zero.
                balp0 = bp_coeff - bp_coeff * 1.0
                balL = eval_coeffs(const_map, linear_map, eta, L) - bp_coeff * (
                    r0(L, L) + c_bal * r1(L, L)
                )
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(bp_coeff, L):8.2f} {bexp(bp_rank, L):7.2f}"
                    f" {bexp(bp_coeff-bp_rank, L):7.2f}"
                    f" {bexp(fstar, L):7.2f} {bexp(fdiff, L):7.2f}"
                    f" {bexp(bal0, L):7.2f} {bexp(balp0, L):8.2f}"
                    f" {bexp(balL, L):7.2f}"
                )


if __name__ == "__main__":
    run()
