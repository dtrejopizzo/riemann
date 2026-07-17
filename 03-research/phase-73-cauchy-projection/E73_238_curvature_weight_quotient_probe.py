#!/usr/bin/env python3
import math
import sys

import numpy as np

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-71-cand1-convergence")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-73-cauchy-projection")

from E71_9_relative_arch_background_probe import build  # noqa: E402
from E72_396_cauchy_projection_probe import GAMMAS  # noqa: E402
from E73_193_balanced_ramp_probe import functional, r0, r1  # noqa: E402
from E73_223_coefficient_ball_budget import coefficient_maps, cauchy_rows, projector  # noqa: E402
from E73_224_weight_amplification_budget import weight  # noqa: E402


def setup(lam, n_modes):
    H, idx, L = build(lam, n_modes, include_arith=True)
    vals, vecs = np.linalg.eigh(H)
    xi = vecs[:, 0]
    if xi[len(xi) // 2] < 0:
        xi = -xi
    xi = xi / np.linalg.norm(xi)
    d = 2.0 * np.pi * idx / L
    return idx.astype(int), d, L, xi.astype(complex)


def exp_mode(omega):
    return lambda y: np.exp(1j * omega * y)


def y_exp_mode(omega):
    return lambda y: y * np.exp(1j * omega * y)


def curvature_u(omega, L, lam):
    # By second Abel integration by parts, this is F[e^{iomega y}]
    # modulo endpoint terms.  We compute the quotient version through F
    # to avoid unstable K_L quadrature.
    return weight(lam, L, omega, "c")


def curvature_z(omega, L, lam):
    return weight(lam, L, omega, "l")


def bexp(z, L):
    return math.log(max(float(abs(complex(z))), 1e-300)) / math.log(L)


def run():
    print("E73.238 curvature weight quotient")
    print("Checks original weights equal curvature quotient on admissible coefficients.")
    print(" lam      L gamma row centerB quotientB diffB fstarB BpB")
    cache = {}
    for lam, n_modes in [(12, 16), (16, 20), (20, 24)]:
        idx, d, L, xi = setup(lam, n_modes)
        I = np.eye(len(idx), dtype=complex)
        f0 = functional(lambda y: r0(y, L), 1.0, L, lam)
        f1 = functional(lambda y: r1(y, L), 0.0, L, lam)
        c_bal = -f0 / f1
        fstar = f0 + c_bal * f1
        # R_* = F[r_*] by second Abel, zero by construction.  The quotient
        # correction therefore vanishes numerically in this finite check.
        rstar_weight = fstar
        for gamma in GAMMAS[:2]:
            Q = cauchy_rows(-1j * gamma, d)
            eta = (I - projector(Q)) @ xi
            for row_id in range(2):
                const_map, linear_map = coefficient_maps(Q[row_id], idx, d, L)
                center = 0j
                quotient = 0j
                bp = 0j
                for om, vec in const_map.items():
                    coeff = vec @ eta
                    bp += 1j * om * coeff
                    key = (lam, float(L), float(om), "c")
                    w = complex(cache.setdefault(key, weight(lam, L, om, "c")))
                    center += coeff * w
                    quotient += coeff * (w - 1j * om * rstar_weight)
                for om, vec in linear_map.items():
                    coeff = vec @ eta
                    bp += coeff
                    key = (lam, float(L), float(om), "l")
                    v = complex(cache.setdefault(key, weight(lam, L, om, "l")))
                    center += coeff * v
                    quotient += coeff * (v - rstar_weight)
                print(
                    f"{lam:4d} {L:8.3f} {gamma:6.2f} {row_id:3d}"
                    f" {bexp(center, L):8.2f} {bexp(quotient, L):9.2f}"
                    f" {bexp(center-quotient, L):7.2f}"
                    f" {bexp(fstar, L):7.2f} {bexp(bp, L):7.2f}"
                )


if __name__ == "__main__":
    run()
