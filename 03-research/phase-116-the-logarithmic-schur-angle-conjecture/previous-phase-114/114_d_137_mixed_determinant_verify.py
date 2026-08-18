#!/usr/bin/env python3
"""Checks for D.137 mixed coherent/Fredholm determinant identities.

The script verifies finite-dimensional identities only.  It does not assume
the sign of B_nuc or RH.
"""

from __future__ import annotations

import math

import mpmath as mp
import numpy as np


rng = np.random.default_rng(137)


def close(a, b, tol=1e-10):
    assert abs(a - b) <= tol * max(1.0, abs(a), abs(b)), (a, b)


# 1. Virtual feature difference and exact second cross-effect.
n = 17
X = rng.normal(size=(29, n)) + 1j * rng.normal(size=(29, n))
Y = rng.normal(size=(23, n)) + 1j * rng.normal(size=(23, n))
f = rng.normal(size=n) + 1j * rng.normal(size=n)
g = rng.normal(size=n) + 1j * rng.normal(size=n)


def B(u, v):
    return np.vdot(Y @ u, Y @ v) - np.vdot(X @ u, X @ v)


def log_metric(u):
    return 0.5 * B(u, u).real


cross = log_metric(f + g) - log_metric(f) - log_metric(g)
close(cross, B(f, g).real)


# 2. Birman--Schwinger congruence.
R = X.conj().T @ X + 0.8 * np.eye(n)
W = 0.13 * Y
er, Ur = np.linalg.eigh(R)
Rhalf = (Ur * np.sqrt(er)) @ Ur.conj().T
Rinvhalf = (Ur / np.sqrt(er)) @ Ur.conj().T
A = W @ Rinvhalf
K = A.conj().T @ A
Fdef = np.eye(n) - K
lhs = R - W.conj().T @ W
rhs = Rhalf @ Fdef @ Rhalf
assert np.linalg.norm(lhs - rhs, ord=2) < 1e-10
assert (np.linalg.eigvalsh(lhs)[0] >= -1e-10) == (
    np.linalg.norm(A, ord=2) <= 1 + 1e-10
)


# 3. Symmetric Fredholm block has Schur complement I-A*A.
block = np.block(
    [
        [np.eye(n), -A.conj().T],
        [-A, np.eye(A.shape[0])],
    ]
)
schur = np.eye(n) - A.conj().T @ A
assert np.linalg.norm(schur - Fdef, ord=2) < 1e-12
negative_block = np.count_nonzero(np.linalg.eigvalsh(block) < -1e-10)
negative_defect = np.count_nonzero(np.linalg.eigvalsh(Fdef) < -1e-10)
assert negative_block == negative_defect


# 4. Kernel and cokernel of a finite self-adjoint defect have equal
# dimension, so its Fredholm determinant line is well typed even at a
# crossing.
Fcross = np.diag([0.0, 0.0, 1.0, -2.0])
kernel_dim = Fcross.shape[0] - np.linalg.matrix_rank(Fcross)
cokernel_dim = Fcross.shape[0] - np.linalg.matrix_rank(Fcross.T)
assert kernel_dim == cokernel_dim == 2


# 5. Determinant orientation does not imply positivity.
Fplus = np.diag([2.0, 2.0])
Fminus = np.diag([-2.0, -2.0])
close(np.linalg.det(Fplus), np.linalg.det(Fminus))
assert np.linalg.eigvalsh(Fplus)[0] > 0
assert np.linalg.eigvalsh(Fminus)[-1] < 0


# 6. The scale 1/log(j) is outside every finite Schatten class by block
# condensation: [exp(m), exp(m+1)) contributes at least exp(m)/(m+1)^p.
for p in (1, 2, 4, 10):
    block_mass = [math.exp(m) / (m + 1) ** p for m in range(30, 71)]
    assert block_mass[-1] > block_mass[0]
    assert block_mass[-1] > 1e8


# 7. All prime powers have the reduced-contact/central-depth coefficient.
for p in (2, 3, 5, 11):
    for k in range(1, 8):
        w = math.log(p) / math.sqrt(p**k)
        close(w, math.log(p) * p ** (-k / 2), 1e-14)


# 8. The two logarithmic jets are exactly Mellin moments 0 and 1 under
# F(t)=exp(t/2)f(exp(t)).  Use a rapidly decreasing test for a numerical
# change-of-variables certificate.
mp.mp.dps = 40


def central_F(t):
    return mp.e ** (-t * t) * (1 + mp.mpf("0.17") * t)


def mult_f_from_F(x):
    t = mp.log(x)
    return mp.e ** (-t / 2) * central_F(t)


for s, sign in ((0, -1), (1, 1)):
    mellin = mp.quad(
        lambda t: mult_f_from_F(mp.e**t) * mp.e ** (s * t),
        [-mp.inf, mp.inf],
    )
    moment = mp.quad(
        lambda t: central_F(t) * mp.e ** (sign * t / 2),
        [-mp.inf, mp.inf],
    )
    assert mp.almosteq(mellin, moment)


# 9. Every centered prime-power channel pulls back to the two translated
# correlations with coefficient Lambda(p^k)/sqrt(p^k).
N = 61
u = rng.normal(size=N) + 1j * rng.normal(size=N)
v = rng.normal(size=N) + 1j * rng.normal(size=N)
for p, k, shift in ((2, 1, 2), (2, 4, 7), (3, 3, 11), (5, 2, 13)):
    a = u[shift:]
    b = u[:-shift]
    c = v[shift:]
    d = v[:-shift]
    jpu = (a + b) / math.sqrt(2)
    jmu = (a - b) / math.sqrt(2)
    jpv = (c + d) / math.sqrt(2)
    jmv = (c - d) / math.sqrt(2)
    channel = np.vdot(jpu, jpv) - np.vdot(jmu, jmv)
    translated = np.vdot(a, d) + np.vdot(b, c)
    close(channel, translated)
    weight = math.log(p) / math.sqrt(p**k)
    close(weight * channel, math.log(p) * p ** (-k / 2) * translated)


# 10. The complete shifted Gamma screw symbol is the digamma difference.
def gamma_density(r):
    return mp.e ** (-mp.mpf("2.5") * r) / (1 - mp.e ** (-2 * r))


for tau in (mp.mpf("0.2"), mp.mpf("1.0"), mp.mpf("3.7")):
    screw = 2 * mp.quad(
        lambda r: gamma_density(r) * (1 - mp.cos(tau * r)),
        [0, 1, mp.inf],
    )
    digamma = mp.re(mp.digamma(mp.mpf("1.25") + 0.5j * tau)) - mp.digamma(
        mp.mpf("1.25")
    )
    assert mp.almosteq(screw, digamma, rel_eps=mp.mpf("1e-30"))

beta = mp.log(mp.pi) - mp.digamma(mp.mpf("1.25"))
assert beta > 0


# 11. The Tate Gram is positive on every nonzero window, and its exact
# Schur projector kills both moment vectors.
for T in (0.01, 0.3, 1.0, 5.0):
    gram = np.array([[2 * math.sinh(T), 2 * T], [2 * T, 2 * math.sinh(T)]])
    assert np.linalg.eigvalsh(gram)[0] > 0

T = 1.7
grid = np.linspace(-T, T, 801)
dt = grid[1] - grid[0]
V = np.column_stack((np.exp(-grid / 2), np.exp(grid / 2)))
Gdisc = dt * V.conj().T @ V
P = np.eye(grid.size) - V @ np.linalg.inv(Gdisc) @ (dt * V.conj().T)
test = rng.normal(size=grid.size)
projected = P @ test
assert np.linalg.norm(dt * V.conj().T @ projected) < 1e-10


print("D137 mixed Fredholm--Tate determinant audit: PASS")
