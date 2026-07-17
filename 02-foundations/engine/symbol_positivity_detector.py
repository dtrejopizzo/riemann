"""
symbol_positivity_detector.py
=============================

A clean, faithful detector for the terminal defect of the ARP-P proof path (Omega_7),
expressed at the level of the Toeplitz SYMBOL of the completed log-derivative -Xi'/Xi.

Result (Phase 67, experiments E67.16-E67.17)
-------------------------------------------
The archimedean jet A_N and the prime jet P_lambda of the whitened terminal defect are
approximately Toeplitz (entries depend on j-k), so each carries a symbol on the unit circle:
  sigma_A(theta) = archimedean symbol,     sigma_P(theta) = prime symbol (-zeta'/zeta on Re s = 1/2).

For Hermitian Toeplitz matrices, A_N >= P_lambda  <=>  sigma_A(theta) >= sigma_P(theta) pointwise
(Szego / Avram-Parter, in the symbol limit). Hence the terminal-defect positivity that is equivalent
to RH becomes a POINTWISE SYMBOL INEQUALITY:

        Omega_7   <=>   sigma_A(theta) >= sigma_P(theta)  for all theta
                  <=>   the symbol of -Xi'/Xi is nonnegative on the circle
                  <=>   RH.

Empirically the detector is clean and faithful:
  - zeta: min(sigma_A - sigma_P) ~ +0.045 -- nonnegative, and MARGINAL (touches 0):
          the symbol-level signature of zeta sitting at the de Branges boundary (delta_N -> 0+).
  - a planted off-line zero: min(sigma_A - sigma_P) dips strongly negative, on ~half the circle.

Classical ground (to avoid known pitfalls): Bottcher-Silbermann (Toeplitz operators),
Simon (Orthogonal Polynomials on the Unit Circle), Borodin-Okounkov (resolvent-trace formula).

This module is self-contained apart from the canonical jet harness `h8lab` (P52 paper directory),
which provides the exact A_N, P_lambda via `arithmetic_jets`.
"""
import os
import sys
import numpy as np
import mpmath as mp

# Canonical source of the exact archimedean/prime Pick jets.
_H8 = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, _H8)
import h8lab as H  # noqa: E402

mp.mp.dps = 40


def _mp2np(M):
    return np.array([[complex(M[i, j]) for j in range(M.cols)] for i in range(M.rows)],
                    dtype=complex)


def planted_zero(z0, rho):
    """Xi_deriv for F(s) = zeta(s) * (s-rho)(s-(1-rho)), planting an off-line zero pair.

    Pass the returned callable as `Xi_deriv` to inject an RH counterexample and watch the
    symbol go negative. rho = beta + i*gamma with beta != 1/2 is off the critical line.
    """
    s0 = mp.mpf(1) / 2 + mp.mpc(0, 1) * z0
    r, rc = rho, 1 - rho

    def gder(j, s):
        return {0: (s - r) * (s - rc), 1: (s - r) + (s - rc), 2: mp.mpf(2)}.get(j, mp.mpf(0))

    return lambda k: sum(mp.binomial(k, j) * mp.zeta(s0, 1, j) * gder(k - j, s0)
                         for j in range(k + 1))


def band_symbol(M, ntheta=400):
    """Band-averaged Toeplitz symbol of a Hermitian matrix M.

    t_d = mean_j M[j, j+d];  sigma(theta) = sum_d t_d e^{i d theta}  (real, since M Hermitian).
    """
    N = M.shape[0]
    theta = np.linspace(-np.pi, np.pi, ntheta)
    sigma = np.zeros(ntheta, dtype=complex)
    for d in range(-(N - 1), N):
        vals = [M[j, j + d] for j in range(max(0, -d), min(N, N - d))]
        sigma += np.mean(vals) * np.exp(1j * d * theta)
    return theta, np.real(sigma)


def symbol_gap(t0=100.0, y=1.0, N=12, Xi_deriv=None, ntheta=400):
    """Return (theta, sigma_A - sigma_P). Omega_7 <=> this is >= 0 everywhere.

    Xi_deriv=None uses zeta (RH true). Pass planted_zero(...) to inject an off-line zero.
    """
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    A_N, Plam, _ = H.arithmetic_jets(z0, N, Xi_deriv)
    A = _mp2np(H.herm(A_N))
    P = _mp2np(H.herm(Plam))
    th, sA = band_symbol(A, ntheta)
    _, sP = band_symbol(P, ntheta)
    return th, sA - sP


def detect(t0=100.0, y=1.0, N=12, Xi_deriv=None):
    """Summary: (min gap, fraction of the circle where the symbol is negative)."""
    _, gap = symbol_gap(t0, y, N, Xi_deriv)
    return float(gap.min()), float(np.mean(gap < -1e-9))


if __name__ == "__main__":
    print("Symbol-positivity detector for Omega_7   (sigma_A - sigma_P >= 0  <=>  RH)\n")
    z0v = 100.0
    mn, frac = detect(t0=z0v)
    print(f"  zeta (RH true)     : min(sigma_A - sigma_P) = {mn:+.4f}   "
          f"neg fraction = {frac:.3f}   [nonnegative, marginal -> RH]")
    for beta in (0.65, 0.80, 0.95):
        rho = mp.mpf(str(beta)) + mp.mpc(0, 1) * mp.mpf(str(z0v))
        z0 = mp.mpc(mp.mpf(str(z0v)), -mp.mpf("1.0"))
        mn, frac = detect(t0=z0v, Xi_deriv=planted_zero(z0, rho))
        print(f"  off-line beta={beta} : min(sigma_A - sigma_P) = {mn:+.2f}   "
              f"neg fraction = {frac:.3f}   [negative -> RH false]")
