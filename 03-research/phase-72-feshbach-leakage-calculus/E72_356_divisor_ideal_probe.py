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
    return idx, L, d, xi


def window_nodes(roots, node_kind):
    if node_kind == "root":
        return [1j * t for t in roots]
    if node_kind == "shift":
        return [0.5 + 1j * t for t in roots]
    raise ValueError(node_kind)


def partial_xy(idx, L, d, xi, nodes):
    xs = []
    ys = []
    for z in nodes:
        k = k_row(z, L, d)
        static = np.zeros(len(d), dtype=complex)
        for w in nodes:
            static -= k_kernel(z, w, L) * k_row(w, L, d)
        static += tail_basis_row(z, nodes, idx, d, L)
        ys.append(k @ xi)
        xs.append(static @ xi)
    return np.array(xs), np.array(ys)


def delta_matrix(xs, ys):
    n = len(xs)
    out = np.zeros((n, n), dtype=complex)
    for i in range(n):
        for j in range(n):
            out[i, j] = xs[i] * ys[j] - xs[j] * ys[i]
    return out


def node_poly(z, nodes):
    v = 1.0 + 0.0j
    for a in nodes:
        v *= z - a
    return v


def ideal_control_matrix(nodes):
    n = len(nodes)
    out = np.zeros((n, n), dtype=complex)
    for i, z in enumerate(nodes):
        for j, w in enumerate(nodes):
            a = 1.0 + 0.25j + 0.1 * z
            b = -0.5 + 0.2j + 0.05 * w
            out[i, j] = a * node_poly(z, nodes) + b * node_poly(w, nodes)
    return out


def rel_scale(mat, xs, ys):
    return np.max(np.abs(mat)) / max(norm(xs) * norm(ys), 1e-300)


def run():
    print("E72.356 local divisor-ideal probe")
    print("Simple-node ideal test: Delta in (Z(z),Z(w)) iff Delta(a_i,a_j)=0.")
    print(" lam   N roots node    maxDelta    relDelta    idealCtrlMax")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, xi = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for node_kind in ["root", "shift"]:
            nodes = window_nodes(roots, node_kind)
            xs, ys = partial_xy(idx, L, d, xi, nodes)
            delta = delta_matrix(xs, ys)
            ctrl = ideal_control_matrix(nodes)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {node_kind:>5s} "
                f"{np.max(np.abs(delta)):11.4e} {rel_scale(delta, xs, ys):11.4e} "
                f"{np.max(np.abs(ctrl)):12.4e}"
            )


if __name__ == "__main__":
    run()
