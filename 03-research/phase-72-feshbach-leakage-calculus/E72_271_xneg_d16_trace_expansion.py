#!/usr/bin/env python3
import sys

import numpy as np
from numpy.linalg import eigvalsh
from numpy.polynomial import Chebyshev, Polynomial

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402
from E72_181_chebyshev_abs_schedule_probe import signed_coeff, eval_cheb_matrix_scaled  # noqa: E402
from E72_262_pole_relative_even_setup_audit import pole_relative_even_setup_pair  # noqa: E402


def power_coeff(a, m_bound, degree=16):
    n_terms = degree // 2
    cheb = signed_coeff(a, m_bound, n_terms)
    # eval_cheb_matrix_scaled applies Chebyshev polynomial to K/m_bound. Thus
    # G(K)=sum_r power[r]*(K/m_bound)^r=sum_r (power[r]/m_bound^r) K^r.
    power_scaled = Chebyshev(cheb).convert(kind=Polynomial).coef
    return np.array([power_scaled[r] / (m_bound**r) for r in range(len(power_scaled))], dtype=float)


def trace_expansion(k0, k1, c0, c1):
    powers0 = [np.eye(k0.shape[0])]
    powers1 = [np.eye(k1.shape[0])]
    for _ in range(1, len(c0)):
        powers0.append(powers0[-1] @ k0)
    for _ in range(1, len(c1)):
        powers1.append(powers1[-1] @ k1)
    total = 0.0
    terms = []
    for r, ar in enumerate(c0):
        if abs(ar) < 1e-14:
            continue
        for s, bs in enumerate(c1):
            if abs(bs) < 1e-14:
                continue
            val = float(np.trace(powers0[r] @ powers1[s]))
            contrib = 2.0 * ar * bs * val
            total += contrib
            terms.append((abs(contrib), r, s, contrib, val, ar, bs))
    terms.sort(reverse=True, key=lambda x: x[0])
    return total, terms


def direct_cross(k0, k1):
    c0 = signed_coeff(0.70, 0.90, 8)
    c1 = signed_coeff(0.60, 0.60, 8)
    g0 = eval_cheb_matrix_scaled(k0, c0, 0.90)
    g1 = eval_cheb_matrix_scaled(k1, c1, 0.60)
    return float(2.0 * np.trace(g0 @ g1))


def run():
    print("E72.271 XNEG-D16 trace expansion")
    print("Expands 2Tr(G0G1)=sum c_rs Tr(K0^r K1^s) in the corrected pole-even geometry.")
    c0 = power_coeff(0.70, 0.90, 16)
    c1 = power_coeff(0.60, 0.60, 16)
    print("G0_power_in_K=" + " ".join(f"{x:+.12e}" for x in c0))
    print("G1_power_in_K=" + " ".join(f"{x:+.12e}" for x in c1))
    idx, L, xi, eb, c_actual, c_model, e_pole, odd_norm, even_leak = pole_relative_even_setup_pair(20, 48)
    k0, k1 = two_blocks(20, idx, L, eb, c_model, 0.60)
    expanded, terms = trace_expansion(k0, k1, c0, c1)
    direct = direct_cross(k0, k1)
    print(f"lambda=20 cut=0.60 direct={direct:+.16e} expanded={expanded:+.16e} absDiff={abs(direct-expanded):.3e}")
    print("top terms: r s coeffContribution traceMoment coeff0 coeff1")
    for _, r, s, contrib, moment, ar, bs in terms[:20]:
        print(f"  {r:2d} {s:2d} {contrib:+.12e} {moment:+.12e} {ar:+.6e} {bs:+.6e}")


if __name__ == "__main__":
    run()
