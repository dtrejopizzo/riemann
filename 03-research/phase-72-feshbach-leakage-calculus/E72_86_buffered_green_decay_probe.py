#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_85_high_low_block_probe import even_basis_from_mask, orth  # noqa: E402


def all_even_q_basis(idx, k):
    mask = np.ones(len(idx), dtype=bool)
    q = np.eye(len(idx)) - np.outer(k, k)
    return orth(q @ even_basis_from_mask(idx, mask))


def q_even_basis_for_mask(idx, k, mask, remove=None):
    q = np.eye(len(idx)) - np.outer(k, k)
    raw = q @ even_basis_from_mask(idx, mask)
    if remove is not None and remove.shape[1] > 0:
        raw = raw - remove @ (remove.T @ raw)
    return orth(raw)


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    evals_model, vec_model = eigh(h_model)
    k = vec_model[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)
    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    c = q @ (h_actual - evals_model[0] * np.eye(len(idx))) @ q
    b_all = all_even_q_basis(idx, k)
    c_all = b_all.T @ c @ b_all
    return idx, d, k, b_all, c_all


def run():
    source_cuts = [8, 12, 18]
    tail_cuts = [12, 18, 24, 30, 36]
    print("E72.86 buffered Green decay probe")
    print(" lam   N Rsrc Htail dimS dimT  ||T C^-1 S||")
    for lam, n_modes in [(16, 34), (20, 40), (24, 48)]:
        idx, d, k, b_all, c_all = setup(lam, n_modes)
        for rsrc in source_cuts:
            src_mask = np.abs(d) <= rsrc
            b_src = q_even_basis_for_mask(idx, k, src_mask)
            for htail in tail_cuts:
                if htail <= rsrc:
                    continue
                tail_mask = np.abs(d) > htail
                b_tail = q_even_basis_for_mask(idx, k, tail_mask)
                if b_src.shape[1] == 0 or b_tail.shape[1] == 0:
                    continue
                rhs = b_all.T @ b_src
                sol = solve(c_all, rhs)
                green = b_tail.T @ b_all @ sol
                print(
                    f"{lam:4.0f} {n_modes:3d} {rsrc:4.0f} {htail:5.0f} "
                    f"{b_src.shape[1]:4d} {b_tail.shape[1]:4d} {norm(green, 2):14.3e}"
                )


if __name__ == "__main__":
    run()
