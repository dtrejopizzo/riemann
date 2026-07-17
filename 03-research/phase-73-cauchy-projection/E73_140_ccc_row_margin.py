#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_137_cell_balance_probe import build_parts  # noqa: E402


def row_norm_data(d, xi, gamma):
    row = 1.0 / (-gamma - d)
    row_norm = float(norm(row))
    e = row / row_norm
    eval_norm = abs(float(np.dot(e, xi)))
    return e, row_norm, eval_norm


def orient_sign(x):
    y = x.copy()
    if y[len(y) // 2] < 0:
        y = -y
    return y


def run():
    print("E73.140 CCC row margin")
    print("evalMargin=q-p is the actual ROW-KER margin.")
    print("cellMargin=-log_L|<e,Hxi>|-p is only the Euler-cell consistency margin.")
    print(" lam     L gamma      pRow  evalExp evalMargin  cellExp cellMargin status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        h, w02, wr, prime, d, L = build_parts(lam, n_modes)
        vals, vecs = eigh(h)
        xi = orient_sign(vecs[:, 0])
        mu = float(vals[0])
        for gamma in GAMMAS[:3]:
            e, row_norm, eval_norm = row_norm_data(d, xi, gamma)
            cell = abs(float(np.dot(e, (w02 - wr - prime) @ xi)))
            eig_cell = abs(mu) * eval_norm
            p = bexp(row_norm, L)
            q = -bexp(eval_norm, L)
            eval_margin = q - p
            cell_exp = -bexp(cell, L)
            cell_margin = cell_exp - p
            rel = abs(cell - eig_cell) / max(abs(eig_cell), 1e-300)
            status = "PASS" if eval_margin >= 17.0 else "FAIL"
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {p:9.3f} {q:8.3f} {eval_margin:10.3f}"
                f" {cell_exp:8.3f} {cell_margin:10.3f}"
                f" {status} relEig={rel:.2e}"
            )


if __name__ == "__main__":
    run()
