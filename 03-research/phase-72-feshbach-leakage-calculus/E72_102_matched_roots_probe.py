#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, solve, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402
from E72_101_model_vs_actual_d2_probe import even_q_basis  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)

    _, va = eigh(h_actual)
    xi = va[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)

    em, vm = eigh(h_model)
    k = vm[:, 0]
    k = (k + k[::-1]) / 2
    k = k / norm(k)
    if np.dot(xi, k) < 0:
        xi = -xi

    d = 2 * np.pi * idx / L
    q = np.eye(len(idx)) - np.outer(k, k)
    bq = even_q_basis(idx, k)
    ca = bq.T @ (q @ (h_actual - em[0] * np.eye(len(idx))) @ q) @ bq
    cm = bq.T @ (q @ (h_model - em[0] * np.eye(len(idx))) @ q) @ bq
    return idx, L, d, xi, k, bq, ca, cm


def d2_values(d, k, L, bq, ce, root_vec, roots, s, hcut):
    mask = (np.abs(d) <= hcut).astype(float)
    a = bq.T @ (s / (s * s - d * d))
    vals = []
    for tau in roots:
        c_tau = bq.T @ (mask * transport_vector(d, k, L, tau))
        vals.append(np.vdot(a, solve(ce, c_tau)))
    return np.array(vals, dtype=complex)


def run():
    s = 10 + 0.2j
    hcut = 18
    hmax = 10
    print("E72.102 matched-roots D2 probe")
    print(" lam   N  rootsA rootsM  max actual@A  max model@A  max model@M")
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ca, cm = setup(lam, n_modes)
        roots_a = finite_roots(xi, d, hmax=hmax)
        roots_m = finite_roots(k, d, hmax=hmax)
        vaa = d2_values(d, k, L, bq, ca, xi, roots_a, s, hcut)
        vma = d2_values(d, k, L, bq, cm, k, roots_a, s, hcut)
        vmm = d2_values(d, k, L, bq, cm, k, roots_m, s, hcut)
        max_vaa = np.max(np.abs(vaa)) if len(vaa) else np.nan
        max_vma = np.max(np.abs(vma)) if len(vma) else np.nan
        max_vmm = np.max(np.abs(vmm)) if len(vmm) else np.nan
        print(
            f"{lam:4.0f} {n_modes:3d} {len(roots_a):7d} {len(roots_m):6d} "
            f"{max_vaa:13.3e} {max_vma:12.3e} {max_vmm:12.3e}"
        )


if __name__ == "__main__":
    run()
