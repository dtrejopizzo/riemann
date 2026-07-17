#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import lstsq, norm, solve

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_79_bordered_minor_probe import finite_roots, setup  # noqa: E402
from E72_91_low_band_cofactor_probe import transport_vector  # noqa: E402


def relative_residual(phi, cols):
    a = np.column_stack(cols).astype(complex)
    coef, *_ = lstsq(a, phi, rcond=None)
    return norm(phi - a @ coef) / max(norm(phi), 1e-30)


def run():
    hcut = 18
    print("E72.95 phi low-rank alignment probe")
    print(" lam   N    tau   span{xi,h,1}   span{h,1}   span{xi,h}")
    for lam, n_modes in [(12, 28), (16, 34), (20, 40), (24, 48)]:
        idx, L, d, xi, k, bq, ce = setup(lam, n_modes)
        h = k - xi
        mask = (np.abs(d) <= hcut).astype(float)
        one = np.ones_like(k)
        for tau in finite_roots(xi, d, hmax=10.0)[:4]:
            z_tau = transport_vector(d, k, L, tau)
            c_tau = bq.T @ (mask * z_tau)
            phi = mask * (bq @ solve(ce, c_tau))
            print(
                f"{lam:4.0f} {n_modes:3d} {tau:6.3f} "
                f"{relative_residual(phi, [mask*xi, mask*h, mask*one]):14.3e} "
                f"{relative_residual(phi, [mask*h, mask*one]):11.3e} "
                f"{relative_residual(phi, [mask*xi, mask*h]):12.3e}"
            )


if __name__ == "__main__":
    run()
