#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import even_basis, setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_193_lm8_asrp_probe import split_energy  # noqa: E402
from E72_252_homogeneous_lm8_extended_stress import R0_DEG8, R1_DEG8, eval_hom  # noqa: E402
from E72_256_strict_homogeneous_lm8_certificate import BUFFER  # noqa: E402


def pole_relative_even_setup_pair(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)

    vals_model, vecs_model = eigh(h_model)
    e_pole = float(vals_model[0])
    pole = vecs_model[:, 0]
    odd_norm = norm((pole - pole[::-1]) / 2.0)
    even_leak = norm((pole + pole[::-1]) / 2.0)

    eb = even_basis(idx)
    he_actual = eb.T @ h_actual @ eb
    vals_actual_even, vec_actual_even = eigh(he_actual)
    xi = eb @ vec_actual_even[:, 0]
    xi = xi / norm(xi)

    c_actual = eb.T @ (h_actual - e_pole * np.eye(len(idx))) @ eb
    c_model = eb.T @ (h_model - e_pole * np.eye(len(idx))) @ eb
    return idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak


def row(lam, n_modes):
    old = setup_pair(lam, n_modes)
    old_min = float(eigvalsh(old[-1])[0])

    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(lam, n_modes)
    vals = eigvalsh(c_model)

    k0, k1 = two_blocks(lam, idx, L, eb, c_model, 0.60)
    v0 = eigvalsh(k0)
    v1 = eigvalsh(k1)
    exact = split_energy(v0, 0.70) + split_energy(v1, 0.60)

    r0 = R0_DEG8.copy()
    r1 = R1_DEG8.copy()
    r0[0] += BUFFER
    r1[0] += BUFFER
    op0 = float(max(abs(v0)))
    op1 = float(max(abs(v1)))
    env = eval_hom(v0, 0.90, r0) + eval_hom(v1, 0.60, r1)

    return {
        "lam": lam,
        "L": L,
        "dim": eb.shape[1],
        "old_min": old_min,
        "min_c": float(vals[0]),
        "min_c_l2": float(vals[0]) / (L * L),
        "cond": float(vals[-1] / vals[0]),
        "odd_norm": odd_norm,
        "even_leak": even_leak,
        "exact": exact,
        "env": env,
        "op0": op0,
        "op1": op1,
    }


def run():
    print("E72.262 pole-relative even setup audit")
    print("Uses global odd pole energy e_pole, but keeps the full physical even sector.")
    print("lam L dim oldMinC poleEvenMinC minC/L2 cond poleOdd poleEvenLeak exactBSE ratLM8 op0 op1")
    for lam, n_modes in [(6, 18), (8, 24), (12, 32), (16, 40), (20, 48), (24, 56), (28, 64)]:
        r = row(lam, n_modes)
        print(
            f"{r['lam']:3.0f} {r['L']:.4f} {r['dim']:3d} "
            f"{r['old_min']:.6e} {r['min_c']:.6e} {r['min_c_l2']:.6e} {r['cond']:.3e} "
            f"{r['odd_norm']:.3e} {r['even_leak']:.3e} "
            f"{r['exact']:.6e} {r['env']:.6e} {r['op0']:.3e} {r['op1']:.3e}",
            flush=True,
        )


if __name__ == "__main__":
    run()
