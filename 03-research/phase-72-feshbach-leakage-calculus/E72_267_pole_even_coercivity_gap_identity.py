#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, eigvalsh

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import even_basis  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


WINDOWS = [(6, 18), (8, 24), (12, 32), (16, 40), (20, 48), (24, 56)]


def row(lam, n_modes):
    h_model, idx, L = build(lam, n_modes, include_arith=False)
    evals_full = eigvalsh(h_model)
    e_pole = float(evals_full[0])
    eb = even_basis(idx)
    evals_even = eigvalsh(eb.T @ h_model @ eb)
    gap = float(evals_even[0] - e_pole)

    idx2, L2, xi, eb2, c_actual, c_model, e_pole2, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    min_c = float(eigvalsh(c_model)[0])
    max_c = float(eigvalsh(c_model)[-1])
    return {
        "lam": lam,
        "L": L,
        "dim_even": eb.shape[1],
        "e_pole": e_pole,
        "lambda_even0": float(evals_even[0]),
        "gap": gap,
        "min_c": min_c,
        "relerr": abs(min_c - gap) / max(abs(gap), 1e-30),
        "gap_l2": gap / (L * L),
        "cond": max_c / min_c,
        "odd_norm": odd_norm,
        "even_leak": even_leak,
    }


def run():
    print("E72.267 pole-even coercivity gap identity")
    print("Checks min eig(C_model)=lambda_0(H_model|even)-lambda_0(H_model).")
    print("lam L dim e_pole even0 gap minC relErr gap/L2 cond oddNorm evenLeak")
    for lam, n_modes in WINDOWS:
        r = row(lam, n_modes)
        print(
            f"{r['lam']:3.0f} {r['L']:.6f} {r['dim_even']:3d} "
            f"{r['e_pole']:+.9e} {r['lambda_even0']:+.9e} "
            f"{r['gap']:.9e} {r['min_c']:.9e} {r['relerr']:.2e} "
            f"{r['gap_l2']:.9e} {r['cond']:.3e} "
            f"{r['odd_norm']:.3e} {r['even_leak']:.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
