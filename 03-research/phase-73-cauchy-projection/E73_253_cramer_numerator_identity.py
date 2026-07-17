#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import det, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402
from E73_248_symbolic_pivot_rule_probe import best_minor_rule  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def cramer_numerators(DJ, pair):
    nums = []
    for j in range(DJ.shape[1]):
        A = DJ.copy()
        A[:, j] = pair
        nums.append(det(A))
    return np.array(nums)


def run():
    print("E73.253 Cramer numerator identity")
    print("For J*=max minor: z_j = N_j/det(D_J), N_j=det(D_J with col j replaced by D_Q xi).")
    print(
        " lam      L pow pivIdx              denB numMaxB zMaxB crRel "
        "numAbsCeilB numGainB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            _H, idx, _d, L, _mu, xi, D, _labels, _ranks = quotient_defects(
                lam, n_modes, rat_power
            )
            _u, s, _vh = svd(D, full_matrices=False)
            r = rank_from_svd(s)
            D = D[:r, :]
            piv = best_minor_rule(D, r)
            DJ = D[:, piv]
            pair = D @ xi
            den = det(DJ)
            z = solve(DJ, pair)
            nums = cramer_numerators(DJ, pair)
            cr_rel = norm(nums / den - z) / max(norm(z), 1e-300)

            # Absolute determinant ceiling: replace pair by sum of absolute columnwise
            # multilinear contributions using a crude Hadamard-style proxy.
            # This is not a proof bound, only a scale diagnostic for cancellation.
            col_norms = np.array([norm(DJ[:, j]) for j in range(r)])
            pair_norm = norm(pair)
            num_abs_ceil = []
            for j in range(r):
                factors = [col_norms[k] for k in range(r) if k != j]
                num_abs_ceil.append(pair_norm * float(np.prod(factors)))
            num_abs_ceil = np.array(num_abs_ceil)
            gain = np.max(num_abs_ceil) / max(np.max(np.abs(nums)), 1e-300)
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {str([int(idx[j]) for j in piv]):>18s}"
                f" {bexp(den, L):6.2f}"
                f" {bexp(np.max(np.abs(nums)), L):7.2f}"
                f" {bexp(np.max(np.abs(z)), L):6.2f}"
                f" {cr_rel:7.1e}"
                f" {bexp(np.max(num_abs_ceil), L):11.2f}"
                f" {bexp(gain, L):8.2f}"
            )
    print()
    print("CRAMER-NUM-DIV target: N_j(L,w)=O_M(L^-M)*det(D_J).")


if __name__ == "__main__":
    run()
