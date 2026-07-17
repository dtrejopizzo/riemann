#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_077_pair_coefficient_budget_probe import bexp  # noqa: E402
from E73_148_signed_rowspace_probe import best_by_signed_margin  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402


def spectral_bins(row, e, xi, L):
    vals, vecs = eigh(e)
    coeffs = vecs.conj().T @ row.conj()
    null_j = int(np.argmax(np.abs(vecs.conj().T @ xi)))
    out = {}
    for name, lo, hi in [
        ("null", -1.0, -1.0),
        ("tiny", 0.0, L ** -8),
        ("small", L ** -8, L ** -4),
        ("mid", L ** -4, L ** -1),
        ("bulk", L ** -1, np.inf),
    ]:
        if name == "null":
            mask = np.zeros_like(vals, dtype=bool)
            mask[null_j] = True
        else:
            av = np.abs(vals)
            mask = (av > lo) & (av <= hi)
            mask[null_j] = False
        mass = norm(coeffs[mask])
        out[name] = mass
    return out


def run():
    print("E73.151 forced row spectral profile")
    print("Mass of forced signed rows in spectral bands of E=H-mu I.")
    print("Bands: null, tiny<=L^-8, small L^-8..L^-4, mid L^-4..L^-1, bulk>L^-1.")
    print(" lam     L gamma row    nullB   tinyB  smallB    midB   bulkB status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        d, L, xi, e = setup_exact(lam, n_modes)
        for gamma in GAMMAS[:3]:
            _, _, _, frows, _, _ = best_by_signed_margin(lam, n_modes, gamma)
            for j, row in enumerate(frows):
                bins = spectral_bins(row, e, xi, L)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {bexp(bins['null'], L):8.3f}"
                    f" {bexp(bins['tiny'], L):7.3f}"
                    f" {bexp(bins['small'], L):7.3f}"
                    f" {bexp(bins['mid'], L):7.3f}"
                    f" {bexp(bins['bulk'], L):7.3f}"
                    f" {'PASS' if bins['null'] <= L**-17 else 'FAIL'}"
                )


if __name__ == "__main__":
    run()
