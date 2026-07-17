#!/usr/bin/env python3
import sys
import numpy as np
from numpy.linalg import eigvalsh, norm

sys.path.append("/Users/dt/riemann/riemann-program/03-research/phase-72-feshbach-leakage-calculus")
from E72_101_model_vs_actual_d2_probe import setup_pair  # noqa: E402
from E72_165_fixed_cut_stress_probe import two_blocks  # noqa: E402


WINDOWS = [
    (12, 32),
    (14, 36),
    (16, 40),
    (18, 44),
    (20, 48),
    (22, 52),
    (24, 56),
    (26, 60),
    (28, 64),
]


def abs_cheb_coeff(n_terms):
    # q_N(u) = 2/pi + (4/pi) sum_{k=1}^N (-1)^(k+1) T_{2k}(u)/(4k^2-1).
    coeff = np.zeros(2 * n_terms + 1)
    coeff[0] = 2.0 / np.pi
    for k in range(1, n_terms + 1):
        coeff[2 * k] = (4.0 / np.pi) * ((-1.0) ** (k + 1)) / (4 * k * k - 1)
    return coeff


def signed_coeff(a, m_bound, n_terms):
    q = abs_cheb_coeff(n_terms)
    coeff = -(a * m_bound / 2.0) * q
    if len(coeff) < 2:
        coeff = np.pad(coeff, (0, 2 - len(coeff)))
    coeff[1] += (1.0 - a / 2.0) * m_bound
    return coeff


def eval_cheb_matrix_scaled(mat, coeff, m_bound):
    x = mat / m_bound
    t0 = np.eye(mat.shape[0])
    out = coeff[0] * t0
    if len(coeff) == 1:
        return out
    t1 = x
    out = out + coeff[1] * t1
    for k in range(2, len(coeff)):
        t2 = 2.0 * x @ t1 - t0
        out = out + coeff[k] * t2
        t0, t1 = t1, t2
    return 0.5 * (out + out.T)


def theoretical_error_sum(n_terms):
    # For degree D=2N, | |u|-q_N(u) | <= 2/(pi(2N+1)).
    delta = 2.0 / (np.pi * (2 * n_terms + 1))
    return 0.495 * delta


def collect():
    rows = []
    for lam, n_modes in WINDOWS:
        idx, L, d, xi, k, bq, c_actual, c_model = setup_pair(lam, n_modes)
        k0, k1 = two_blocks(lam, idx, L, bq, c_model, 0.60)
        op0 = float(np.max(np.abs(eigvalsh(k0))))
        op1 = float(np.max(np.abs(eigvalsh(k1))))
        rows.append((lam, L, k0, k1, op0, op1))
        print(f"prepared lambda={lam:.0f} dim={k0.shape[0]} op0={op0:.3f} op1={op1:.3f}", flush=True)
    return rows


def run():
    print("E72.181 explicit Chebyshev |t| schedule probe")
    print("degree D=2N; theoretical eps_sum <= 0.495*2/(pi(2N+1))")
    rows = collect()
    print("   D   epsSum  maxBound worstLam  per-window")
    for degree in [28, 40, 56, 80, 112, 160]:
        n_terms = degree // 2
        c0 = signed_coeff(0.70, 0.90, n_terms)
        c1 = signed_coeff(0.60, 0.60, n_terms)
        eps_sum = theoretical_error_sum(n_terms)
        worst = (0.0, None)
        parts = []
        for lam, L, k0, k1, op0, op1 in rows:
            if op0 > 0.90 or op1 > 0.60:
                bound = np.inf
            else:
                rpoly = eval_cheb_matrix_scaled(k0, c0, 0.90) + eval_cheb_matrix_scaled(k1, c1, 0.60)
                bound = norm(rpoly, "fro") + np.sqrt(k0.shape[0]) * eps_sum
            if bound > worst[0]:
                worst = (bound, lam)
            parts.append(f"{int(lam)}:{bound:.3f}")
        print(
            f"{degree:4d} {eps_sum:8.3e} {worst[0]:8.3f} {int(worst[1]):8d} "
            + " ".join(parts),
            flush=True,
        )


if __name__ == "__main__":
    run()
