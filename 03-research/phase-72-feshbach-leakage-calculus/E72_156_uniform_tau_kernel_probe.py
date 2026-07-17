#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import norm, svd

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_112_operator_split_probe import lk_matrix, sigma_packet  # noqa: E402


def run(tmax=6.0, ngrid=41):
    print("E72.156 uniform tau kernel probe")
    print(" lam   L  grid  maxDist  L*maxDist  medianLdist  tauAtMax")
    taus = np.linspace(0.25, tmax, ngrid)
    for lam, n_modes in [(6, 18), (8, 24), (10, 28), (12, 32), (14, 36), (16, 40), (18, 44)]:
        idx, L, d, xi, k, bq, c_actual, _ = setup_pair(lam, n_modes)
        mask = (np.abs(d) <= 8.0).astype(float)
        op = bq.T @ (mask[:, None] * lk_matrix(d, k))
        _, svals, vh = svd(op, full_matrices=True)
        rank = int(np.sum(svals > 1e-10))
        row_basis = vh[:rank, :]
        vals = []
        for tau in taus:
            y = sigma_packet(L, d, tau)
            vals.append(norm(row_basis @ y) / max(norm(y), 1e-30))
        vals = np.array(vals)
        imax = int(np.argmax(vals))
        print(
            f"{lam:4.0f} {L:5.2f} {len(taus):5d} "
            f"{vals[imax]:8.3e} {L*vals[imax]:10.3e} "
            f"{np.median(L*vals):12.3e} {taus[imax]:8.3f}"
        )


if __name__ == "__main__":
    run()
