#!/usr/bin/env python3
import sys
import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_071_packet_mellin_formula_verifier import h0  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402


def coeff_matrix(zs, w, L):
    rows = []
    for z in zs:
        a, b = coeffs(z, w, L)
        rows.append([a, b])
    return np.array(rows, dtype=complex)


def run():
    print("E73.142 local divisor condition probe")
    print("Tests whether two FAR rows invert the divisor coefficients A H0(w)+B H0(-w).")
    print(" condB=log_L cond(A/B matrix), ampB=log_L ||inv||, hsumB=log_L(|H0(w)|+|H0(-w)|).")
    print(" lam     L gamma        hsumB    condB     ampB   reconRel")
    sigma = 0.20
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, _ = setup_exact(lam, n_modes)
        # Use two nearby non-identical z rows.  They share the critical target w
        # but probe the divisor coefficients at two imaginary heights.
        for j, gamma in enumerate(GAMMAS[:3]):
            w = -1j * gamma
            eta1 = GAMMAS[j]
            eta2 = GAMMAS[(j + 1) % 3]
            zs = [sigma + 1j * eta1, sigma + 1j * eta2]
            mat = coeff_matrix(zs, w, L)
            rhs = np.array([sum(mat[r, c] * [h0(w, d, xi), h0(-w, d, xi)][c] for c in range(2)) for r in range(2)])
            sol = np.linalg.solve(mat, rhs)
            target = np.array([h0(w, d, xi), h0(-w, d, xi)])
            cond = np.linalg.cond(mat)
            amp = np.linalg.norm(np.linalg.inv(mat), ord=2)
            hsum = abs(target[0]) + abs(target[1])
            recon = np.linalg.norm(sol - target) / max(np.linalg.norm(target), 1e-300)
            print(
                f"{lam:4d} {L:7.3f} {gamma:7.2f}"
                f" {bexp(hsum, L):10.3f} {bexp(cond, L):8.3f}"
                f" {bexp(amp, L):8.3f} {recon:10.2e}"
            )


if __name__ == "__main__":
    run()
