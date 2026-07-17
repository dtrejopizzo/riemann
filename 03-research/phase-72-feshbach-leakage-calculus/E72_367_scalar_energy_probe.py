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


def scalar_energy(idx, L, d, xi, nodes, scalar_proxy):
    k = np.array([k_row(z, L, d) @ xi for z in nodes])
    kwin = np.array([[k_kernel(z, w, L) for w in nodes] for z in nodes], dtype=complex)
    t = np.array([tail_basis_row(z, nodes, idx, d, L) @ xi for z in nodes])
    kk = np.vdot(k, k)
    if abs(kk) < 1e-28:
        return [np.nan] * 7
    e_win = np.vdot(k, kwin @ k)
    e_tail = np.vdot(k, t)
    lambda_win = (e_win - e_tail) / kk
    defect = e_win - e_tail - scalar_proxy * kk
    scalar_norm = abs(defect) / np.sqrt(abs(kk))
    return (
        np.sqrt(abs(kk)),
        abs(e_win),
        abs(e_tail),
        abs(lambda_win),
        abs(defect),
        scalar_norm,
        abs(e_tail) / max(abs(e_win), 1e-300),
    )


def run():
    print("E72.367 scalar-consistency energy probe")
    print("Uses mu as scalar proxy; theorem replaces it by Lambda_L=mu+e_pole-2kappa_*.")
    print(
        " lam   N roots node     ||k||       |<k,Kk>|    |<k,t>|     |lambda_win|  |def_mu|    scalarNorm tail/win"
    )
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, mu, xi = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for kind in ["root", "shift"]:
            nodes = nodes_from_roots(roots, kind)
            vals = scalar_energy(idx, L, d, xi, nodes, mu)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {kind:>5s} "
                f"{vals[0]:10.3e} {vals[1]:12.3e} {vals[2]:10.3e} "
                f"{vals[3]:12.3e} {vals[4]:10.3e} {vals[5]:10.3e} {vals[6]:8.2e}"
            )


if __name__ == "__main__":
    run()
