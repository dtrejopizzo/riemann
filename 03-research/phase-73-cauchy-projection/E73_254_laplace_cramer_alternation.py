#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import det, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402
from E73_248_symbolic_pivot_rule_probe import best_minor_rule  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def cofactor(M, a, j):
    rows = [r for r in range(M.shape[0]) if r != a]
    cols = [c for c in range(M.shape[1]) if c != j]
    return ((-1) ** (a + j)) * det(M[np.ix_(rows, cols)])


def laplace_terms(DJ, pair, j):
    return np.array([pair[a] * cofactor(DJ, a, j) for a in range(DJ.shape[0])])


def cramer_num(DJ, pair, j):
    A = DJ.copy()
    A[:, j] = pair
    return det(A)


def run():
    print("E73.254 Laplace expansion of Cramer numerators")
    print("N_j=sum_a pair_a Cof_{a,j}; measures alternating cancellation.")
    print(
        " lam      L pow pivIdx              coord numB termMaxB termAbsB altGainB "
        "termExps"
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
            for j in range(r):
                terms = laplace_terms(DJ, pair, j)
                num = cramer_num(DJ, pair, j)
                term_abs = float(np.sum(np.abs(terms)))
                term_max = float(np.max(np.abs(terms)))
                gain = term_abs / max(abs(num), 1e-300)
                term_exps = " ".join(f"{bexp(t, L):6.2f}" for t in terms)
                print(
                    f"{lam:4d} {L:8.3f} {rat_power:3d}"
                    f" {str([int(idx[p]) for p in piv]):>18s}"
                    f" {j:5d}"
                    f" {bexp(num, L):6.2f}"
                    f" {bexp(term_max, L):8.2f}"
                    f" {bexp(term_abs, L):8.2f}"
                    f" {bexp(gain, L):8.2f}"
                    f" {term_exps}"
                )
            print("-")
    print()
    print("ALT-CRAMER target: alternating four-term Laplace sums N_j are O_M(det(D_J)L^-M).")


if __name__ == "__main__":
    run()
