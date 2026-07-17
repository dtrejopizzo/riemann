#!/usr/bin/env python3
import itertools
import math
import sys

import numpy as np
from numpy.linalg import cond, det, norm, solve, svd
from scipy.linalg import qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_246_quotient_coordinate_audit import quotient_defects, rank_from_svd  # noqa: E402


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def eval_pivots(D, xi, piv):
    DJ = D[:, piv]
    pair = D @ xi
    z = solve(DJ, pair)
    rest = np.array([j for j in range(D.shape[1]) if j not in set(piv)], dtype=int)
    T = solve(DJ, D[:, rest]) if len(rest) else np.zeros((len(piv), 0), dtype=complex)
    return {
        "cond": cond(DJ),
        "det": abs(det(DJ)),
        "zmax": np.max(np.abs(z)),
        "trans": norm(T, ord=2) if T.size else 0.0,
        "recon": norm(pair - DJ @ z),
    }


def qr_rule(D, r):
    _q, _rmat, piv = qr(D, pivoting=True, mode="economic")
    return np.array(piv[:r], dtype=int)


def norm4_rule(D, r):
    col_norm = np.array([norm(D[:, j]) for j in range(D.shape[1])])
    return np.argsort(-col_norm)[:r]


def sympair_rule(D, idx, r):
    col_norm = np.array([norm(D[:, j]) for j in range(D.shape[1])])
    by_abs = {}
    for j, n in enumerate(idx):
        by_abs.setdefault(abs(int(n)), []).append(j)
    scored = []
    for absn, js in by_abs.items():
        if absn == 0 or len(js) < 2:
            continue
        scored.append((sum(col_norm[j] ** 2 for j in js), absn, js))
    scored.sort(reverse=True)
    piv = []
    for _score, _absn, js in scored:
        js = sorted(js, key=lambda j: -col_norm[j])
        piv.extend(js[:2])
        if len(piv) >= r:
            break
    if len(piv) < r:
        for j in norm4_rule(D, D.shape[1]):
            if j not in piv:
                piv.append(int(j))
            if len(piv) >= r:
                break
    return np.array(piv[:r], dtype=int)


def edge_core_rule(D, idx, r):
    col_norm = np.array([norm(D[:, j]) for j in range(D.shape[1])])
    nonzero = [j for j, n in enumerate(idx) if int(n) != 0]
    edge_abs = max(abs(int(idx[j])) for j in nonzero)
    edge = [j for j, n in enumerate(idx) if abs(int(n)) == edge_abs]
    edge = sorted(edge, key=lambda j: -col_norm[j])[:2]
    rem = [j for j in np.argsort(-col_norm) if j not in edge]
    return np.array((edge + [int(j) for j in rem])[:r], dtype=int)


def best_minor_rule(D, r):
    best = None
    for piv in itertools.combinations(range(D.shape[1]), r):
        DJ = D[:, piv]
        val = abs(det(DJ))
        if best is None or val > best[0]:
            best = (val, np.array(piv, dtype=int))
    return best[1]


def run():
    print("E73.248 symbolic pivot rule probe")
    print("Compare QR pivots with physical rules for PIV-QUOT-DIV.")
    print(
        " lam      L pow rule          pivIdx              condB detB zMaxB transB reconB"
    )
    cases = [(8, 6), (10, 8), (12, 10), (16, 20)]
    rules = [
        ("QR", lambda D, idx, r: qr_rule(D, r)),
        ("NORM4", lambda D, idx, r: norm4_rule(D, r)),
        ("SYMPAIR", lambda D, idx, r: sympair_rule(D, idx, r)),
        ("EDGECORE", lambda D, idx, r: edge_core_rule(D, idx, r)),
        ("MAXMINOR", lambda D, idx, r: best_minor_rule(D, r)),
    ]
    for lam, n_modes in cases:
        for rat_power in [0, 1, 2]:
            _H, idx, _d, L, _mu, xi, D, _labels, _ranks = quotient_defects(
                lam, n_modes, rat_power
            )
            _u, s, _vh = svd(D, full_matrices=False)
            r = rank_from_svd(s)
            for name, fn in rules:
                piv = fn(D, idx, r)
                out = eval_pivots(D, xi, piv)
                piv_idx = [int(idx[j]) for j in piv]
                print(
                    f"{lam:4d} {L:8.3f} {rat_power:3d} {name:<9s}"
                    f" {str(piv_idx):>18s}"
                    f" {bexp(out['cond'], L):6.2f}"
                    f" {bexp(out['det'], L):6.2f}"
                    f" {bexp(out['zmax'], L):6.2f}"
                    f" {bexp(out['trans'], L):6.2f}"
                    f" {bexp(out['recon'], L):7.2f}"
                )
            print("-")


if __name__ == "__main__":
    run()
