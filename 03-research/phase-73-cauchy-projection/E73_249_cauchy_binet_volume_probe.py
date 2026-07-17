#!/usr/bin/env python3
import itertools
import math
import sys

import numpy as np
from numpy.linalg import det, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def binom(n, k):
    return math.comb(int(n), int(k))


def minors(D, r):
    vals = []
    pivs = []
    for piv in itertools.combinations(range(D.shape[1]), r):
        val = abs(det(D[:, piv]))
        vals.append(val)
        pivs.append(piv)
    return np.array(vals), pivs


def run():
    print("E73.249 Cauchy-Binet quotient volume")
    print("vol^2=det(D_Q D_Q*)=sum_J |det D_Q[:,J]|^2.")
    print(
        " lam      L pow n r volB maxB rmsB combB gapMaxVolB svProdB cbRel"
    )
    for lam, n_modes in [(8, 6), (10, 8), (12, 10), (16, 20)]:
        for rat_power in [0, 1, 2]:
            _H, _idx, _d, L, _mu, _xi, D, _labels, _ranks = quotient_defects(
                lam, n_modes, rat_power
            )
            _u, s, _vh = svd(D, full_matrices=False)
            r = rank_from_svd(s)
            D = D[:r, :]
            vals, _pivs = minors(D, r)
            max_minor = float(np.max(vals))
            sumsq = float(np.sum(vals * vals))
            vol = math.sqrt(max(0.0, float(np.real(det(D @ D.conj().T)))))
            svprod = float(np.prod(s[:r]))
            rms = math.sqrt(sumsq / len(vals))
            comb_loss = math.sqrt(len(vals))
            cb_rel = abs(sumsq - vol * vol) / max(sumsq, vol * vol, 1e-300)
            gap = vol / max(max_minor, 1e-300)
            print(
                f"{lam:4d} {L:8.3f} {rat_power:3d}"
                f" {D.shape[1]:3d} {r:2d}"
                f" {bexp(vol, L):6.2f}"
                f" {bexp(max_minor, L):6.2f}"
                f" {bexp(rms, L):6.2f}"
                f" {bexp(comb_loss, L):6.2f}"
                f" {bexp(gap, L):10.2f}"
                f" {bexp(svprod, L):8.2f}"
                f" {cb_rel:8.1e}"
            )
    print()
    print("The deterministic inequality is max_J |minor_J| >= vol/sqrt(C(n,r)).")


if __name__ == "__main__":
    run()
