#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigh, norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402


def setup(lam, n_modes):
    h_actual, idx, L = build(lam, n_modes, include_arith=True)
    h_model, _, _ = build(lam, n_modes, include_arith=False)
    prime = h_model - h_actual
    vals, vecs = eigh(h_actual)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / norm(xi)
    d = 2.0 * np.pi * idx / L
    return h_actual, h_model, prime, vals[0], d, L, xi


def cauchy_rows(w, d):
    return np.vstack([1.0 / (w + 1j * d), 1.0 / (-w + 1j * d)])


def plane_projector(plane):
    u, s, _ = svd(plane.T, full_matrices=False)
    rank = int(np.sum(s > 1e-12 * s[0]))
    u = u[:, :rank]
    return u @ u.conj().T


def bexp(z, L):
    return np.log(max(float(abs(z)), 1e-300)) / np.log(L)


def participation(v):
    n2 = norm(v)
    if n2 == 0:
        return 0.0, 0.0
    top = float(np.max(np.abs(v)) / n2)
    eff = float((np.sum(np.abs(v)) ** 2) / (n2 * n2))
    return top, eff


def angle(u, v):
    nu = norm(u)
    nv = norm(v)
    if nu == 0 or nv == 0:
        return 0.0
    return float(abs(np.vdot(u, v)) / (nu * nv))


def run():
    print("E73.187 transverse vector structure")
    print("Tests whether xi_perp is small, concentrated, or a genuine large transverse vector.")
    print(
        " lam     L gamma  parN perpN top eff"
        "  modelB primeB signedB gain angle parValB"
    )
    for lam, n_modes in [(12, 16), (16, 20), (20, 24), (24, 28), (32, 36)]:
        _h, h_model, prime, _mu, d, L, xi = setup(lam, n_modes)
        ident = np.eye(len(d), dtype=complex)
        for gamma in GAMMAS[:2]:
            plane = cauchy_rows(-1j * gamma, d)
            proj = plane_projector(plane)
            xi_par = proj @ xi
            xi_perp = (ident - proj) @ xi
            top, eff = participation(xi_perp)

            t_model = plane @ (h_model @ xi_perp)
            t_prime = plane @ (prime @ xi_perp)
            t_signed = t_model - t_prime
            gain = norm(t_signed) / max(norm(t_model), norm(t_prime), 1e-300)
            par_val = norm(plane @ xi)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {norm(xi_par):5.2e} {norm(xi_perp):5.2e}"
                f" {top:4.2f} {eff:5.1f}"
                f" {bexp(norm(t_model), L):7.2f}"
                f" {bexp(norm(t_prime), L):7.2f}"
                f" {bexp(norm(t_signed), L):8.2f}"
                f" {bexp(gain, L):5.2f} {angle(t_model, t_prime):5.3f}"
                f" {bexp(par_val, L):7.2f}"
            )


if __name__ == "__main__":
    run()
