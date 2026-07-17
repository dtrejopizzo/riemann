#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_349_cfir_row_candidate_probe import k_row, k_kernel, tail_basis_row  # noqa: E402


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    mu = vals[0]
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2 * np.pi * idx / L
    e = h_actual - mu * np.eye(len(idx))
    return h_actual, idx, L, d, mu, xi, e


def nodes_from_roots(roots, kind):
    if kind == "root":
        return [1j * t for t in roots]
    if kind == "shift":
        return [0.5 + 1j * t for t in roots]
    raise ValueError(kind)


def rows(idx, L, d, mu, h_actual, nodes):
    full_rows = []
    reduced_rows = []
    operator_rows = []
    for z in nodes:
        k = k_row(z, L, d)
        full = k @ h_actual
        interp = np.zeros(len(d), dtype=complex)
        for w in nodes:
            interp += k_kernel(z, w, L) * k_row(w, L, d)
        tail = tail_basis_row(z, nodes, idx, d, L)
        reduced = mu * k - interp + tail
        # full residual after subtracting interpolation/tail pieces with the same proxy scalar.
        full_cfir = full - interp + tail
        full_rows.append(full_cfir)
        reduced_rows.append(reduced)
        operator_rows.append(full - mu * k)
    return full_rows, reduced_rows, operator_rows


def run():
    print("E72.371 full-row ladder probe")
    print("Uses h_actual as coupled operator and mu as scalar proxy.")
    print(" lam   N roots node     fullDef     redDef      couplingErr  opRowAmp")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        h_actual, idx, L, d, mu, xi, e = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for kind in ["root", "shift"]:
            nodes = nodes_from_roots(roots, kind)
            full_rows, reduced_rows, operator_rows = rows(idx, L, d, mu, h_actual, nodes)
            full_def = norm(np.array([r @ xi for r in full_rows]))
            red_def = norm(np.array([r @ xi for r in reduced_rows]))
            coupling = norm(np.array([(f - r) @ xi for f, r in zip(full_rows, reduced_rows)]))
            op_amp = norm(np.array([r @ xi for r in operator_rows]))
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {kind:>5s} "
                f"{full_def:11.4e} {red_def:11.4e} {coupling:12.4e} {op_amp:10.3e}"
            )


if __name__ == "__main__":
    run()
