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
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2
    xi = xi / norm(xi)
    d = 2 * np.pi * idx / L
    return idx, L, d, xi


def nodes_from_roots(roots, kind):
    if kind == "root":
        return [1j * t for t in roots]
    if kind == "shift":
        return [0.5 + 1j * t for t in roots]
    raise ValueError(kind)


def components(idx, L, d, xi, nodes):
    k_vals = []
    s_win = []
    s_tail = []
    for z in nodes:
        k_vals.append(k_row(z, L, d) @ xi)
    k_vals = np.array(k_vals)
    for z in nodes:
        win = 0.0 + 0.0j
        for b, kb in zip(nodes, k_vals):
            win -= k_kernel(z, b, L) * kb
        tail = tail_basis_row(z, nodes, idx, d, L) @ xi
        s_win.append(win)
        s_tail.append(tail)
    return k_vals, np.array(s_win), np.array(s_tail)


def skew(s, k):
    return np.outer(s, k) - np.outer(k, s)


def run():
    print("E72.362 skew window-tail decomposition probe")
    print("Checks Delta = Delta_win + Delta_tail and reports their relative sizes.")
    print(" lam   N roots node    totalNorm     winNorm      tailNorm     reconErr")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, xi = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for kind in ["root", "shift"]:
            nodes = nodes_from_roots(roots, kind)
            k, sw, st = components(idx, L, d, xi, nodes)
            total = skew(sw + st, k)
            win = skew(sw, k)
            tail = skew(st, k)
            recon = norm(total - win - tail)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {kind:>5s} "
                f"{norm(total):12.5e} {norm(win):12.5e} "
                f"{norm(tail):12.5e} {recon:12.5e}"
            )


if __name__ == "__main__":
    run()
