#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, inv, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_195_finite_frequency_certificate_probe import cauchy_rows  # noqa: E402
from E73_193_balanced_ramp_probe import functional, r0, r1  # noqa: E402


def projector(q):
    return q.conj().T @ inv(q @ q.conj().T) @ q


def q_cell(idx, d, y, L):
    n = len(idx)
    out = np.zeros((n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            if a == b:
                out[a, b] = 2.0 * (1.0 - y / L) * np.cos(d[a] * y)
            else:
                out[a, b] = (np.sin(d[a] * y) - np.sin(d[b] * y)) / (
                    np.pi * (idx[b] - idx[a])
                )
    return out


def q_cell_second(idx, d, y, L):
    n = len(idx)
    out = np.zeros((n, n), dtype=complex)
    for a in range(n):
        for b in range(n):
            if a == b:
                da = d[a]
                out[a, b] = 4.0 * da * np.sin(da * y) / L - 2.0 * (1.0 - y / L) * da * da * np.cos(da * y)
            else:
                out[a, b] = (-d[a] ** 2 * np.sin(d[a] * y) + d[b] ** 2 * np.sin(d[b] * y)) / (
                    np.pi * (idx[b] - idx[a])
                )
    return out


def setup(lam, n_modes):
    h, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = eigh(h)
    xi = vecs[:, 0].astype(complex)
    if xi[len(xi) // 2].real < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi


def run():
    print("E73.297 balanced curvature operator probe")
    print("Checks (B-B'(0)(r0+c r1))'' = q(Q_y''+alpha_L(y)J)eta.")
    print(" lam     L gamma row y/L relErr absErr")
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c_bal = -f0 / f1
        eye = np.eye(len(d), dtype=complex)
        J = np.ones((len(d), len(d)), dtype=complex)
        ys = [0.07 * L, 0.31 * L, 0.59 * L, 0.91 * L]
        hstep = 1e-5 * L
        for gamma in GAMMAS[:2]:
            q = cauchy_rows(-1j * gamma, d)
            eta = (eye - projector(q)) @ xi
            for row_id in range(2):
                row = q[row_id]
                bp0 = row @ (-(2.0 / L) * J) @ eta
                for y in ys:
                    alpha = (2.0 / L) * (-2.0 / L + c_bal * (2.0 - 6.0 * y / L))

                    def bbal(x):
                        ramp = x * (1.0 - x / L) + c_bal * x * x * (1.0 - x / L)
                        return row @ q_cell(idx, d, x, L) @ eta - bp0 * ramp

                    numeric = (bbal(y + hstep) - 2.0 * bbal(y) + bbal(y - hstep)) / (hstep * hstep)
                    exact = row @ (q_cell_second(idx, d, y, L) + alpha * J) @ eta
                    rel = abs(numeric - exact) / max(abs(exact), 1e-300)
                    print(
                        f"{lam:4d} {L:7.3f} {gamma:7.2f} {row_id:3d}"
                        f" {y/L:5.2f} {rel:7.1e} {abs(numeric-exact):.3e}"
                    )


if __name__ == "__main__":
    run()
