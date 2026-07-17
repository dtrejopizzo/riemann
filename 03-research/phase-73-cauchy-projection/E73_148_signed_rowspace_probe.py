#!/usr/bin/env python3
import itertools
import sys
import numpy as np
from numpy.linalg import norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E72_349_cfir_row_candidate_probe import p_active, p_infty  # noqa: E402
from E73_069_exact_far3_row_probe import setup_exact  # noqa: E402
from E73_077_pair_coefficient_budget_probe import coeffs, bexp  # noqa: E402


def pair_row(z, w, idx, d, L, mode):
    row = np.zeros(len(d), dtype=complex)
    for n_pos, n_d in enumerate(d):
        if mode == "active":
            row[n_pos] = p_active(z, n_pos, w, idx, d, L)
        elif mode == "tail":
            row[n_pos] = p_infty(z, n_d, w, L) - p_active(z, n_pos, w, idx, d, L)
        elif mode == "signed":
            row[n_pos] = p_infty(z, n_d, w, L)
        else:
            raise ValueError(mode)
    return row


def coeff_matrix(zs, w, L):
    return np.array([coeffs(z, w, L) for z in zs], dtype=complex)


def forced_rows(mat, rows):
    inv = np.linalg.inv(mat)
    return inv @ np.vstack(rows)


def row_stats(row, xi, L):
    amp = abs(row @ xi)
    row_norm = norm(row)
    rel = amp / max(row_norm, 1e-300)
    return bexp(amp, L), bexp(row_norm, L), bexp(rel, L), amp, row_norm, rel


def best_by_signed_margin(lam, n_modes, gamma, nrows=6, sigma=0.20):
    d, L, xi, _ = setup_exact(lam, n_modes)
    idx = np.rint(d * L / (2.0 * np.pi)).astype(int)
    w = -1j * gamma
    candidates = [sigma + 1j * g for g in GAMMAS[:nrows]]
    best = None
    for z1, z2 in itertools.combinations(candidates, 2):
        mat = coeff_matrix([z1, z2], w, L)
        if abs(np.linalg.det(mat)) < 1e-300:
            continue
        signed_rows = [pair_row(z1, w, idx, d, L, "signed"), pair_row(z2, w, idx, d, L, "signed")]
        frows = forced_rows(mat, signed_rows)
        # The l1 forced divisor is produced by the two scalar rows after
        # applying the inverse.  Use the larger null component as the row
        # certificate score.
        amps = [abs(frows[j] @ xi) for j in range(2)]
        score = -bexp(sum(amps), L)
        rec = (score, z1, z2, frows, L, xi)
        if best is None or rec[0] > best[0]:
            best = rec
    return best


def run():
    print("E73.148 signed rowspace probe")
    print("Builds forced signed rows M^-1[p_infty(z1),p_infty(z2)] and measures null components.")
    print("ampB=log_L |row xi|, normB=log_L ||row||, relB=log_L(|row xi|/||row||).")
    print(" lam     L gamma row    ampB   normB    relB      z1      z2 status")
    for lam, n_modes in [(16, 20), (20, 24), (24, 28), (28, 32), (32, 36)]:
        for gamma in GAMMAS[:3]:
            score, z1, z2, frows, L, xi = best_by_signed_margin(lam, n_modes, gamma)
            for j in range(2):
                amp_b, norm_b, rel_b, *_ = row_stats(frows[j], xi, L)
                print(
                    f"{lam:4d} {L:7.3f} {gamma:7.2f} {j:3d}"
                    f" {amp_b:7.3f} {norm_b:7.3f} {rel_b:7.3f}"
                    f" {z1.imag:7.2f} {z2.imag:7.2f}"
                    f" {'PASS' if -amp_b >= 17.0 else 'FAIL'}"
                )


if __name__ == "__main__":
    run()
