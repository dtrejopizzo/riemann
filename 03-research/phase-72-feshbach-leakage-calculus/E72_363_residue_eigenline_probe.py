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


def eigenline_data(idx, L, d, xi, nodes):
    k = np.array([k_row(z, L, d) @ xi for z in nodes])
    kwin = np.array([[k_kernel(z, w, L) for w in nodes] for z in nodes], dtype=complex)
    t = np.array([tail_basis_row(z, nodes, idx, d, L) @ xi for z in nodes])
    v = kwin @ k - t
    if norm(k) < 1e-14:
        lam = np.nan
        resid = norm(v)
        rel = np.nan
    else:
        lam = np.vdot(k, v) / np.vdot(k, k)
        resid_vec = v - lam * k
        resid = norm(resid_vec)
        rel = resid / max(norm(v), 1e-300)
    return norm(k), norm(kwin @ k), norm(t), resid, rel, lam


def run():
    print("E72.363 residue eigenline probe")
    print("Tests P_k^perp(KWin k - tail)=0.")
    print(" lam   N roots node     ||k||      ||Kk||      ||tail||    perpNorm    relPerp   |lambda|")
    for lam, n_modes in [(6, 10), (8, 12), (10, 14), (12, 16)]:
        idx, L, d, xi = setup_full(lam, n_modes)
        roots = finite_roots(xi.real, d, hmax=8.0)[:3]
        for kind in ["root", "shift"]:
            nodes = nodes_from_roots(roots, kind)
            nk, nkw, nt, resid, rel, eig = eigenline_data(idx, L, d, xi, nodes)
            print(
                f"{lam:5.1f} {n_modes:3d} {len(nodes):5d} {kind:>5s} "
                f"{nk:10.3e} {nkw:10.3e} {nt:10.3e} "
                f"{resid:10.3e} {rel:9.3e} {abs(eig):10.3e}"
            )


if __name__ == "__main__":
    run()
