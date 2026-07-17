#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def run():
    hcut = 18
    moments = [0, 1, 2, 3]
    print("E72.93 finite-band phi moment probe")
    print("   lam    N      tau " + " ".join([f"coh{m}" for m in moments]))
    for lam, n_modes in [(8, 24), (12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        mask = (np.abs(d) <= hcut).astype(float)
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            phi = mask * (bq @ solve(ce, c_tau))
            vals = []
            for m in moments:
                weight = d ** (2 * m)
                mu = np.sum(phi * weight)
                abs_ceiling = np.sum(np.abs(phi) * np.abs(weight))
                vals.append(abs(mu) / max(abs_ceiling, 1e-30))
            print(
                f"{lam:6.1f} {n_modes:4d} {tau:8.3f} "
                + " ".join(f"{v:8.2e}" for v in vals)
            )


if __name__ == "__main__":
    run()
