#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E73_287_closed_weight_formula_probe import closed_V, closed_W  # noqa: E402


def bexp(z, L):
    return np.log(max(float(abs(complex(z))), 1e-300)) / np.log(L)


def derivative(func, x, h=1e-5):
    return (
        -func(x + 2 * h)
        + 8 * func(x + h)
        - 8 * func(x - h)
        + func(x - 2 * h)
    ) / (12 * h)


def run():
    print("E73.293 Loewner diagonal probe")
    print("Tests whether U_even is the natural diagonal of -(1/(iL)) Lambda_{Wodd}.")
    print("diagA = U_even; diagB = -(1/(iL)) d/domega(W(omega)-W(-omega)).")
    print(" lam     L relErr bestRel aB bB diagAB diagBB residB")
    for lam in [12, 16, 20, 24, 28]:
        L = 2.0 * np.log(lam)
        nmax = int(2 * lam + 4)
        idx = np.arange(-nmax, nmax + 1)
        idx = idx[idx != 0]
        d = 2.0 * np.pi * idx / L
        W = np.array([closed_W(float(o), L, lam) for o in d], dtype=complex)
        V = np.array([closed_V(float(o), L, lam) for o in d], dtype=complex)
        # Constant gauges do not affect Wodd.  U_even is gauge-dependent only by
        # a constant row; fit and remove a constant after the raw comparison.
        wmap = {float(o): W[k] for k, o in enumerate(d)}
        vmap = {float(o): V[k] for k, o in enumerate(d)}
        diag_a = []
        diag_b = []
        for om in d:
            om = float(om)
            u_even = (wmap[om] - vmap[om] / L) + (wmap[-om] - vmap[-om] / L)
            f = lambda x: closed_W(x, L, lam) - closed_W(-x, L, lam)
            natural = -derivative(f, om) / (1j * L)
            diag_a.append(u_even)
            diag_b.append(natural)
        diag_a = np.array(diag_a)
        diag_b = np.array(diag_b)
        raw_rel = norm(diag_a - diag_b) / max(norm(diag_a), 1e-300)
        A = np.column_stack([diag_b, np.ones_like(diag_b)])
        coeff, *_ = np.linalg.lstsq(A, diag_a, rcond=None)
        pred = A @ coeff
        best_rel = norm(diag_a - pred) / max(norm(diag_a), 1e-300)
        resid = diag_a - pred
        print(
            f"{lam:4d} {L:7.3f} {raw_rel:7.1e} {best_rel:7.1e}"
            f" {bexp(coeff[0],L):5.2f} {bexp(coeff[1],L):5.2f}"
            f" {bexp(norm(diag_a),L):6.2f} {bexp(norm(diag_b),L):6.2f}"
            f" {bexp(norm(resid),L):7.2f}"
        )


if __name__ == "__main__":
    run()
