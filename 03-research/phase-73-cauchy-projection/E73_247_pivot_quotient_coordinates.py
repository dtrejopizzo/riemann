#!/usr/bin/env python3
import math
import sys

import numpy as np
from numpy.linalg import cond, norm, solve, svd
from scipy.linalg import qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def pivot_coordinate_audit(lam, n_modes, rat_power):
    _H, idx, _d, L, _mu, xi, D, labels, ranks = quotient_defects(
        lam, n_modes, rat_power
    )
    _u, s, _vh = svd(D, full_matrices=False)
    r = rank_from_svd(s)
    # Column-pivoted QR on D selects physical frequency coordinates.
    _q, _rmat, piv = qr(D, pivoting=True, mode="economic")
    piv = np.array(piv[:r], dtype=int)
    DJ = D[:, piv]
    pair = D @ xi
    zJ = solve(DJ, pair)
    reconstructed = DJ @ zJ
    recon_err = norm(pair - reconstructed)

    rest = np.array([j for j in range(D.shape[1]) if j not in set(piv)], dtype=int)
    T = solve(DJ, D[:, rest]) if len(rest) else np.zeros((r, 0), dtype=complex)
    z_formula = xi[piv] + T @ xi[rest]
    formula_err = norm(zJ - z_formula)
    transfer_norm = norm(T, ord=2) if T.size else 0.0
    return {
        "L": L,
        "idx": idx,
        "labels": labels,
        "ranks": ranks,
        "rank": r,
        "singular": s,
        "piv": piv,
        "piv_idx": [int(x) for x in idx[piv]],
        "cond": cond(DJ),
        "pair": pair,
        "zJ": zJ,
        "xiJ": xi[piv],
        "recon_err": recon_err,
        "formula_err": formula_err,
        "transfer_norm": transfer_norm,
        "rest": rest,
    }


def run():
    print("E73.247 pivot quotient coordinates")
    print("Physical pivot coordinates J give D_Q xi = D_Q[:,J] z_J.")
    print(
        " lam      L pow MDranks qRank pivIdx condB pairMaxB zMaxB "
        "xiJMaxB transB reconErrB formulaErrB"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            out = pivot_coordinate_audit(lam, n_modes, rat_power)
            L = out["L"]
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {str(out['ranks']):>9s} {out['rank']:5d}"
                f" {str(out['piv_idx']):>18s}"
                f" {bexp(out['cond'], L):6.2f}"
                f" {bexp(np.max(np.abs(out['pair'])), L):8.2f}"
                f" {bexp(np.max(np.abs(out['zJ'])), L):6.2f}"
                f" {bexp(np.max(np.abs(out['xiJ'])), L):7.2f}"
                f" {bexp(out['transfer_norm'], L):6.2f}"
                f" {bexp(out['recon_err'], L):10.2f}"
                f" {bexp(out['formula_err'], L):11.2f}"
            )
    print()
    print("Canonical pow=0 pivot coordinates:")
    print(" lam      L pivIdx              zB-values")
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        out = pivot_coordinate_audit(lam, n_modes, 0)
        L = out["L"]
        zvals = " ".join(f"{bexp(z, L):7.2f}" for z in out["zJ"])
        print(f"{lam:4d} {L:8.3f} {str(out['piv_idx']):>18s} {zvals}")


if __name__ == "__main__":
    run()
