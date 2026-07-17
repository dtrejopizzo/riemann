#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm, qr

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0]
    xi = (xi + xi[::-1]) / 2.0
    xi = xi / norm(xi)
    if xi[len(xi) // 2] < 0:
        xi = -xi
    d = 2.0 * np.pi * idx / L
    return h, vals, d, L, xi


def orthogonal_basis_to(e):
    e = e / norm(e)
    n = len(e)
    m = np.eye(n)
    m[:, 0] = e
    q, _ = qr(m)
    # QR may flip the first vector; only the complement matters.
    return q[:, 1:]


def constrained_min(h, e):
    q = orthogonal_basis_to(e)
    vals, _ = eigh(q.T @ h @ q)
    return vals[0]


def row(lam, n_modes, gamma):
    h, vals, d, L, xi = setup(lam, n_modes)
    k = 1.0 / (-gamma - d)
    e = k / norm(k)
    leak = abs(float(np.dot(xi, e)))
    mu = vals[0]
    gap = vals[1] - vals[0]
    cmin = constrained_min(h, e)
    cg = cmin - mu
    # Davis-Kahan style scale: leak^2 * gap is the natural energy cost.
    predicted_cost = leak * leak * gap
    return L, norm(k), leak, gap, cg, predicted_cost


def run():
    print("E73.135 constrained critical-evaluation gap")
    print("For row e, compares min_{v perp e}<Hv>-mu with leak^2*gap.")
    print(" lam     L gamma      pRow     qNorm     gapB  cGapB predCostB ratio")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32)]:
        for gamma in GAMMAS[:3]:
            L, kn, leak, gap, cg, pc = row(lam, n_modes, gamma)
            ratio = cg / max(pc, 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(kn, L):8.3f} {-bexp(leak, L):9.3f}"
                f" {bexp(gap, L):8.3f} {bexp(abs(cg), L):7.3f}"
                f" {bexp(pc, L):9.3f} {ratio:7.3f}"
            )


if __name__ == "__main__":
    run()
