#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import even_basis  # noqa: E402


def odd_basis(idx):
    used = set()
    cols = []
    n = len(idx)
    pos = {int(v): i for i, v in enumerate(idx)}
    for val in idx:
        val = int(val)
        if val in used:
            continue
        if val == 0:
            used.add(val)
            continue
        j = pos[val]
        k = pos[-val]
        col = np.zeros(n)
        if val > 0:
            col[j] = 1.0 / np.sqrt(2.0)
            col[k] = -1.0 / np.sqrt(2.0)
        else:
            col[k] = 1.0 / np.sqrt(2.0)
            col[j] = -1.0 / np.sqrt(2.0)
        cols.append(col)
        used.add(val)
        used.add(-val)
    return np.column_stack(cols)


def model_upper(lam, n_modes):
    h_model, idx, L = build(lam, n_modes, include_arith=False)
    eb = even_basis(idx)
    ob = odd_basis(idx)
    he = eb.T @ h_model @ eb
    ho = ob.T @ h_model @ ob
    ev_e = eigvalsh(he)
    ev_o = eigvalsh(ho)
    e_pole = float(ev_o[0])
    op_c = float(ev_e[-1] - e_pole)
    min_c = float(ev_e[0] - e_pole)
    return L, eb.shape[1], ob.shape[1], e_pole, ev_e[0], ev_e[-1], min_c, op_c


def run():
    print("E72.286 model upper identity probe")
    print("For C_model=H_model|even-lambda_0(H_model|odd)I:")
    print("lambda_min(C_model)=lambda_0^even-lambda_0^odd, ||C_model||=lambda_max^even-lambda_0^odd.")
    print("lam L dimE dimO odd0 even0 evenMax minC/L2 opC/L2")
    for lam, n_modes in [(16, 40), (20, 48), (24, 56), (28, 64), (32, 72)]:
        L, dim_e, dim_o, odd0, even0, even_max, min_c, op_c = model_upper(lam, n_modes)
        L2 = L * L
        print(
            f"{lam:3.0f} {L:.6f} {dim_e:4d} {dim_o:4d} "
            f"{odd0:.6e} {even0:.6e} {even_max:.6e} "
            f"{min_c / L2:.6e} {op_c / L2:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
