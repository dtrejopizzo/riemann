#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import cholesky, eigh, eigvalsh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import even_basis, setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8, eval_hom  # noqa: E402
from E72_256_strict_homogeneous_lm8_certificate import BUFFER  # noqa: E402


def even_q_basis_from_even_ground(idx, k, tol=1e-10):
    q = np.eye(len(idx)) - np.outer(k, k)
    u, s, _ = svd(q @ even_basis(idx), full_matrices=False)
    return u[:, s > tol]


def corrected_even_setup_pair(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    eb = even_basis(idx)

    evals_model_even, vec_model_even = eigh(eb.T @ h_model @ eb)
    e0_even = float(evals_model_even[0])
    k = eb @ vec_model_even[:, 0]
    k = k / norm(k)

    evals_actual_even, vec_actual_even = eigh(eb.T @ h_actual @ eb)
    xi = eb @ vec_actual_even[:, 0]
    xi = xi / norm(xi)
    if np.dot(xi, k) < 0:
        xi = -xi

    q = np.eye(len(idx)) - np.outer(k, k)
    bq = even_q_basis_from_even_ground(idx, k)
    c_actual = bq.T @ (q @ (h_actual - e0_even * np.eye(len(idx))) @ q) @ bq
    c_model = bq.T @ (q @ (h_model - e0_even * np.eye(len(idx))) @ q) @ bq
    return idx, L, xi, k, bq, c_actual, c_model, e0_even, evals_model_even


def relative_matrix(mat, c_model):
    chol = cholesky(c_model)
    x = solve(chol, mat)
    rel = solve(chol, x.T).T
    return 0.5 * (rel + rel.T)


def row(lam, n_modes):
    old = setup_pair(lam, n_modes)
    old_min = float(eigvalsh(old[-1])[0])

    idx, L, xi, k, bq, c_actual, c_model, e0_even, evals_even = corrected_even_setup_pair(lam, n_modes)
    min_c = float(eigvalsh(c_model)[0])
    gap_even = float(evals_even[1] - evals_even[0])
    rel_gap_err = abs(min_c - gap_even) / max(gap_even, 1e-30)

    k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
    v0 = eigvalsh(k0)
    v1 = eigvalsh(k1)
    exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)
    r0 = R0_DEG8.copy()
    r1 = R1_DEG8.copy()
    r0[0] += BUFFER
    r1[0] += BUFFER
    env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)

    return {
        "lam": lam,
        "L": L,
        "dim": bq.shape[1],
        "old_min": old_min,
        "min_c": min_c,
        "min_c_l2": min_c / (L * L),
        "gap_even": gap_even,
        "gap_err": rel_gap_err,
        "exact": exact,
        "env": env,
    }


def run():
    print("E72.261 even-sector ground audit")
    print("Compares old setup_pair with corrected even-sector model ground.")
    print("lam L dim oldMinC evenMinC evenMinC/L2 evenGap relGapErr exactBSE ratLM8")
    for lam, n_modes in [(6, 18), (8, 24), (12, 32), (16, 40), (20, 48)]:
        r = row(lam, n_modes)
        print(
            f"{r['lam']:3.0f} {r['L']:.4f} {r['dim']:3d} "
            f"{r['old_min']:.6e} {r['min_c']:.6e} {r['min_c_l2']:.6e} "
            f"{r['gap_even']:.6e} {r['gap_err']:.2e} "
            f"{r['exact']:.6e} {r['env']:.6e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
