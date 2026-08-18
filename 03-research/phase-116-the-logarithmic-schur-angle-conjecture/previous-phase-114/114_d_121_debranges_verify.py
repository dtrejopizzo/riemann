#!/usr/bin/env python3
"""Exact/numerical checks for D.121.

The script verifies only the algebraic bridge and the Gamma symbol.  It
does not assume or test RH.
"""

from __future__ import annotations

import cmath
import math

import mpmath as mp


mp.mp.dps = 60


def close(a: complex, b: complex, tol: float = 1e-38) -> None:
    assert abs(a - b) < tol * max(1.0, abs(a), abs(b)), (a, b)


# 1. The central Mellin coordinate sends the two Fourier jets to s=0,1.
close(0.5 - 1j * (-0.5j), 0.0)
close(0.5 - 1j * (0.5j), 1.0)


# 2. The two-jet Gram eigenvalues are strictly positive.
for T in (mp.mpf("0.01"), mp.mpf("0.7"), mp.mpf("3"), mp.mpf("10")):
    lam_minus = 2 * (mp.sinh(T) - T)
    lam_plus = 2 * (mp.sinh(T) + T)
    assert lam_minus > 0 and lam_plus > 0


# 3. q is exactly the divisor of the two evaluation points.
def q(z: complex) -> complex:
    return z * z + 0.25


close(q(0.5j), 0.0)
close(q(-0.5j), 0.0)


# 4. The full Gamma jump integral equals the digamma difference.
def gamma_integral(tau: mp.mpf) -> mp.mpf:
    f = lambda r: 2 * mp.e ** (-r / 2) / (1 - mp.e ** (-2 * r)) * (
        1 - mp.cos(tau * r)
    )
    return mp.quad(f, [0, 1, mp.inf])


for tau in (mp.mpf("0.1"), mp.mpf("1"), mp.mpf("3.25")):
    lhs = gamma_integral(tau)
    rhs = mp.re(mp.digamma(mp.mpf(1) / 4 + 0.5j * tau)) - mp.digamma(
        mp.mpf(1) / 4
    )
    # Direct infinite-interval quadrature loses digits at the removable
    # singularity r=0; 1e-16 is a stricter check than its observed error.
    close(lhs, rhs, 1e-16)
    assert lhs > 0


# 5. Every real-zero factor shifted down has a Schur reflection factor.
def reflection_factor(z: complex, gamma: float, a: float) -> complex:
    return ((z - (gamma + 1j * a)) / (z - (gamma - 1j * a))) * (
        (z - (-gamma + 1j * a)) / (z - (-gamma - 1j * a))
    )


for z in (0.2 + 0.1j, -1.7 + 0.8j, 3.0 + 2.0j):
    for gamma in (1.0, 4.0, 9.0):
        assert abs(reflection_factor(z, gamma, 0.3)) < 1


# 6. Toy real-entire models demonstrate the exact zero-shift obstruction.
# Real zeros: Phi(z)=(z^2-1)(z^2-4), so Phi(z+ia) has only lower zeros.
def phi_real(z: complex) -> complex:
    return (z * z - 1) * (z * z - 4)


def E_real(z: complex, a: float) -> complex:
    return phi_real(z + 1j * a)


def Estar_real(z: complex, a: float) -> complex:
    return phi_real(z - 1j * a)


for z in (0.1 + 0.2j, 1.3 + 0.7j, -3.0 + 1.1j):
    assert abs(Estar_real(z, 0.4)) < abs(E_real(z, 0.4))


# Off-real zeros: Phi(z)=z^2+d^2.  When 0<a<d, E_a has an upper zero.
d = 0.3
a = 0.1
upper_zero = 1j * (d - a)
close((upper_zero + 1j * a) ** 2 + d**2, 0.0)
assert upper_zero.imag > 0


# 7. Check the infinitesimal de Branges kernel formula on an even toy Xi.
def kernel(E, Estar, z: complex, w: complex) -> complex:
    return (E(z) * E(w).conjugate() - Estar(z) * Estar(w).conjugate()) / (
        2j * math.pi * (w.conjugate() - z)
    )


def phi_prime(z: complex) -> complex:
    return 4 * z**3 - 10 * z


z = 0.4 + 0.3j
w = -0.7 + 0.6j
target = (
    phi_prime(z) * phi_real(w.conjugate())
    - phi_real(z) * phi_prime(w.conjugate())
) / (math.pi * (w.conjugate() - z))
for eps in (1e-3, 3e-4, 1e-4):
    quotient = kernel(
        lambda u: E_real(u, eps),
        lambda u: Estar_real(u, eps),
        z,
        w,
    ) / eps
    assert abs(quotient - target) < 0.02


# 8. A prime-power symbol uses Lambda(p^k)/sqrt(p^k), including k>1.
def prime_symbol(tau: float, p: int, K: int) -> float:
    return sum(
        2 * math.log(p) / (p ** (k / 2)) * (1 - math.cos(k * math.log(p) * tau))
        for k in range(1, K + 1)
    )


tau = 0.73
manual = 0.0
for k in range(1, 5):
    n = 3**k
    von_mangoldt = math.log(3)
    manual += 2 * von_mangoldt / math.sqrt(n) * (
        1 - math.cos(math.log(n) * tau)
    )
close(prime_symbol(tau, 3, 4), manual, 1e-14)


print("D121 de Branges/canonical-system bridge: PASS")
