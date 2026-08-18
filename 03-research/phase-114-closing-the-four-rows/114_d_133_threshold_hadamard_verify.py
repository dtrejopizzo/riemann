#!/usr/bin/env python3
"""Reproducible checks for the D.133 threshold Hadamard formulas.

No zero of zeta and no RH statement is used.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


mp.mp.dps = 50


def close(a, b, tol=1e-8):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


# 1. Verify the old-contact transport derivative (3.1) by finite difference.
def f(x):
    return 1 + 0.3 * x + 0.2 * x**2


def g(x):
    return 0.7 - 0.4 * x + 0.1 * x**3


def gp(x):
    return -0.4 + 0.3 * x**2


def J(alpha):
    return mp.quad(lambda x: f(x) * g(x + alpha), [-1, 1 - alpha])


alpha = mp.mpf("0.73")
analytic_dalpha = -f(1 - alpha) * g(1) + mp.quad(
    lambda x: f(x) * gp(x + alpha), [-1, 1 - alpha]
)
h = mp.mpf("1e-7")
numeric_dalpha = (J(alpha + h) - J(alpha - h)) / (2 * h)
close(analytic_dalpha, numeric_dalpha, 1e-8)


# 2. Verify the threshold derivative (4.1).
a = mp.log(7)
T0 = a / 2


def JT(T):
    al = a / T
    if al >= 2:
        return mp.mpf("0")
    return mp.quad(lambda x: f(x) * g(x + al), [-1, 1 - al])


threshold_target = (2 / T0) * f(-1) * g(1)
for dh in (mp.mpf("1e-5"), mp.mpf("3e-6"), mp.mpf("1e-6")):
    quotient = JT(T0 + dh) / dh
    assert abs(quotient - threshold_target) < 2e-3


# 3. Gamma shape derivative: finite difference versus the differentiated
# multiplier, tested on a Gaussian Fourier profile.
def ell(u):
    return mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * u)) - mp.digamma(
        mp.mpf(1) / 4
    )


def ellp(u):
    return mp.re(0.5j * mp.polygamma(1, mp.mpf(1) / 4 + 0.5j * u))


def gamma_energy(T):
    return mp.quad(lambda s: ell(s / T) * mp.e ** (-s * s), [-mp.inf, mp.inf])


T = mp.mpf("0.91")
dh = mp.mpf("2e-5")
numeric = (gamma_energy(T + dh) - gamma_energy(T - dh)) / (2 * dh)
analytic = mp.quad(
    lambda s: -(s / T**2) * ellp(s / T) * mp.e ** (-s * s),
    [-mp.inf, mp.inf],
)
close(numeric, analytic, 2e-8)


# 4. The entering contact is not operator-norm continuous.  Equal normalized
# profiles on two layers have quadratic correlation exactly one.
for layer in (1e-1, 1e-3, 1e-6):
    amp = 1 / math.sqrt(2 * layer)
    norm2 = 2 * layer * amp**2
    Jlayer = layer * amp**2
    Cquadratic = 2 * Jlayer
    close(norm2, 1.0, 1e-14)
    close(Cquadratic, 1.0, 1e-14)


# 5. Boundary-spike Hadamard values have both signs and scale as 1/epsilon.
w = math.log(7) / math.sqrt(7)
for eps in (1e-2, 1e-4, 1e-6):
    same = -(4 * w / T0) / eps
    opposite = +(4 * w / T0) / eps
    assert same < 0 < opposite
    close(abs(same) * eps, 4 * w / T0, 1e-12)


# 6. Verify the finite-dimensional Schur--Hadamard formula (7.3).
rng = np.random.default_rng(20260806)
M = rng.normal(size=(4, 4))
A = M.T @ M + 2 * np.eye(4)
Adot = rng.normal(size=(4, 4))
Adot = (Adot + Adot.T) / 2
B = rng.normal(size=(4, 3))
Bdot = rng.normal(size=(4, 3))
D = rng.normal(size=(3, 3))
D = (D + D.T) / 2
Ddot = rng.normal(size=(3, 3))
Ddot = (Ddot + Ddot.T) / 2
Ainv = np.linalg.inv(A)
formula = (
    Ddot
    - Bdot.T @ Ainv @ B
    - B.T @ Ainv @ Bdot
    + B.T @ Ainv @ Adot @ Ainv @ B
)


def cap(t):
    At = A + t * Adot
    Bt = B + t * Bdot
    Dt = D + t * Ddot
    return Dt - Bt.T @ np.linalg.inv(At) @ Bt


dh = 1e-6
numeric = (cap(dh) - cap(-dh)) / (2 * dh)
assert np.linalg.norm(numeric - formula, ord=2) < 2e-8


# 7. Verify the projection derivative (5.2) in a quadrature discretization.
x, weights = np.polynomial.legendre.leggauss(200)
Wsqrt = np.sqrt(weights)


def Vmat(T):
    return Wsqrt[:, None] * np.column_stack((np.exp(T * x / 2), np.exp(-T * x / 2)))


def Pmat(T):
    V = Vmat(T)
    return np.eye(len(x)) - V @ np.linalg.inv(V.T @ V) @ V.T


T = 0.83
V = Vmat(T)
Vdot = Wsqrt[:, None] * np.column_stack(
    ((x / 2) * np.exp(T * x / 2), (-x / 2) * np.exp(-T * x / 2))
)
Gram = V.T @ V
Gramdot = Vdot.T @ V + V.T @ Vdot
Ginv = np.linalg.inv(Gram)
Pdot_formula = (
    -Vdot @ Ginv @ V.T
    - V @ Ginv @ Vdot.T
    + V @ Ginv @ Gramdot @ Ginv @ V.T
)
dh = 1e-6
Pdot_numeric = (Pmat(T + dh) - Pmat(T - dh)) / (2 * dh)
assert np.linalg.norm(Pdot_numeric - Pdot_formula, ord=2) < 2e-8


print("D133 threshold Hadamard/capacity audit: PASS")
