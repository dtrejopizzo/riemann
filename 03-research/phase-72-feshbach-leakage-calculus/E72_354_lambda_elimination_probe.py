#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
from E71_9_relative_arch_background_probe import build  # noqa: E402

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots  # noqa: E402
from E72_349_cfir_row_candidate_probe import (  # noqa: E402
    k_row,
    k_kernel,
    tail_basis_row,
)


def setup_full(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h_actual)
    mu = vals[0]
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2 * np.pi * idx / L
    e = h_actual - mu * np.eye(len(idx))
    return idx, L, d, mu, xi, e


def nodes_from_roots(roots, node_kind):
    if node_kind == "root":
        return [1j * t for t in roots]
    if node_kind == "shift":
        return [0.5 + 1j * t for t in roots]
    raise ValueError(node_kind)


def affine_components(idx, L, d, xi, roots, node_kind):
    nodes = nodes_from_roots(roots, node_kind)
    y_vals = []
    x_vals = []
    for a in nodes:
        k = k_row(a, L, d)
        static = np.zeros(len(d), dtype=complex)
        for w in nodes:
            static -= k_kernel(a, w, L) * k_row(w, L, d)
        static += tail_basis_row(a, nodes, idx, d, L)
        y_vals.append(k @ xi)
        x_vals.append(static @ xi)
    return nodes, np.array(y_vals), np.array(x_vals)


def wedge_defect(x, y):
    if len(x) == 0:
        return np.nan, np.nan, np.nan
    wedge_max = 0.0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            wedge_max = max(wedge_max, abs(x[i] * y[j] - x[j] * y[i]))
    denom = max(norm(x) * norm(y), 1e-300)
    rel = wedge_max / denom
    y_norm = norm(y)
    if y_norm < 1e-14:
        lam_fit = np.nan
        residual = norm(x)
    else:
        lam_fit = -np.vdot(y, x) / np.vdot(y, y)
        residual = norm(x + lam_fit * y)
    rel_residual = residual / max(norm(x), 1e-300)
    return rel, rel_residual, lam_fit


def compatible_control(x, y, lam0=2.0 - 0.75j):
    # Replace x by -lambda*y. This must have zero wedge and zero fitted residual.
    x_good = -lam0 * y
    rel, rel_residual, lam_fit = wedge_defect(x_good, y)
    return rel, rel_residual, lam_fit


def run():
    print("E72.354 affine Lambda-elimination probe")
    print("Tests vec(S Adj(E)) collinear with vec(K Adj(E)) in the rank-one adjugate channel.")
    print(
        " lam   N roots node    ||Kxi||      ||Sxi||      wedgeRel    fitRel      |LambdaFit|"
    )
    controls = []
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, mu, xi, e = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for node_kind in ["root", "shift"]:
            _, y, x = affine_components(idx, L, d, xi, roots, node_kind)
            wedge_rel, fit_rel, lam_fit = wedge_defect(x, y)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(y):5d} {node_kind:>5s} "
                f"{norm(y):11.4e} {norm(x):11.4e} "
                f"{wedge_rel:11.4e} {fit_rel:11.4e} {abs(lam_fit):12.4e}"
            )
            if node_kind == "shift":
                controls.append(compatible_control(x, y))
    print("\ncompatible artificial controls")
    print(" case   wedgeRel    fitRel      |LambdaFit|")
    for i, (wedge_rel, fit_rel, lam_fit) in enumerate(controls[:4], start=1):
        print(f"{i:5d} {wedge_rel:11.4e} {fit_rel:11.4e} {abs(lam_fit):12.4e}")


if __name__ == "__main__":
    run()
