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
    return idx, L, d, mu, xi


def nodes_from_roots(roots, kind):
    if kind == "root":
        return [1j * t for t in roots]
    if kind == "shift":
        return [0.5 + 1j * t for t in roots]
    raise ValueError(kind)


def energies(idx, L, d, xi, nodes, scalar_proxy):
    k = np.array([k_row(z, L, d) @ xi for z in nodes])
    kwin = np.array([[k_kernel(z, w, L) for w in nodes] for z in nodes], dtype=complex)
    t = np.array([tail_basis_row(z, nodes, idx, d, L) @ xi for z in nodes])
    v = kwin @ k - t
    full = norm(scalar_proxy * k - v) ** 2
    kk = np.vdot(k, k)
    if abs(kk) < 1e-28:
        return np.nan, np.nan, np.nan, np.nan
    lambda_win = np.vdot(k, v) / kk
    proj = norm(v - lambda_win * k) ** 2
    scalar = (abs(lambda_win - scalar_proxy) ** 2) * abs(kk)
    return full, proj, scalar, abs(full - proj - scalar)


def run():
    print("E72.368 residual norm master-energy probe")
    print("Uses mu as scalar proxy; theorem replaces it by Lambda_L.")
    print(" lam   N roots node      fullE        projE       scalarE      splitErr")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, mu, xi = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for kind in ["root", "shift"]:
            nodes = nodes_from_roots(roots, kind)
            full, proj, scalar, err = energies(idx, L, d, xi, nodes, mu)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {kind:>5s} "
                f"{full:11.4e} {proj:11.4e} {scalar:11.4e} {err:11.4e}"
            )


if __name__ == "__main__":
    run()
