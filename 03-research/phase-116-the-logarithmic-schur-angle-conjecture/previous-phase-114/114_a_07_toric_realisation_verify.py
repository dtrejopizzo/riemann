#!/usr/bin/env python3
"""Finite algebraic/numerical audit of the toric realisation in 114.a.07."""

import cmath
import math
import sys

import sympy as sp

FAIL = []


def check(name, condition, detail=""):
    print(("PASS  " if condition else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not condition:
        FAIL.append(name)


print("A. Canonical metric")
z0, z1, lam = 2 - 3j, -1 + 4j, 3 + 2j
k = 5
P = z0**5 + 2 * z0**2 * z1**3 - z1**5
P_scaled = (lam * z0)**5 + 2 * (lam * z0)**2 * (lam * z1)**3 - (lam * z1)**5
norm = abs(P) / max(abs(z0), abs(z1))**k
norm_scaled = abs(P_scaled) / max(abs(lam * z0), abs(lam * z1))**k
check("A1 canonical norm is homogeneous-coordinate invariant", abs(norm - norm_scaled) < 1e-12)

print("\nB. Haar L2 lattice")
coeff = [2, -3, 5, 1, -4, 2]
a = 1.25
N = 32768
l2_quad = 0.0
for ell in range(N):
    z = cmath.exp(2j * math.pi * ell / N)
    value = sum(c * z**j for j, c in enumerate(coeff))
    l2_quad += math.exp(-2 * a) * abs(value) ** 2 / N
l2_exact = math.exp(-2 * a) * sum(c * c for c in coeff)
check("B1 Haar quadrature gives e^(-2a) sum |c_j|^2", abs(l2_quad - l2_exact) < 1e-11,
      f"error={abs(l2_quad-l2_exact):.3e}")

gram_error = 0.0
for i in range(7):
    for j in range(7):
        s = sum(cmath.exp(2j * math.pi * (i - j) * ell / N) for ell in range(N)) / N
        gram_error = max(gram_error, abs(s - (1 if i == j else 0)))
check("B2 monomials 1,z,...,z^6 are Haar-orthonormal", gram_error < 1e-12,
      f"max error={gram_error:.3e}")

print("\nC. Roof, height and polarisation")
k1, a1, k2, a2 = sp.symbols("k1 a1 k2 a2", real=True)
q = lambda kk, aa: 2 * kk * aa
mixed = sp.expand((q(k1 + k2, a1 + a2) - q(k1, a1) - q(k2, a2)) / 2)
check("C1 polarisation of 2ka is ka'+k'a", sp.simplify(mixed - (k1 * a2 + k2 * a1)) == 0)
check("C2 both rulings isotropic and cross once",
      q(1, 0) == 0 and q(0, 1) == 0 and mixed.subs({k1: 1, a1: 0, k2: 0, a2: 1}) == 1)

# Exact integral of the constant roof a on [0,k].
x, kk, aa = sp.symbols("x kk aa", positive=True)
height = 2 * sp.integrate(aa, (x, 0, kk))
check("C3 2! integral_[0,k] a dx = 2ka", sp.simplify(height - 2 * kk * aa) == 0)

DdotDminusK = q(kk, aa) - (kk * 0 + (-2) * aa)
check("C4 K=(-2,0) gives (1/2)D.(D-K)=ka+a",
      sp.simplify(DdotDminusK / 2 - (kk * aa + aa)) == 0)

print("\nD. I7 negative control")
T = sp.symbols("T")
phi3 = sp.cyclotomic_poly(3, T)
phi6 = sp.cyclotomic_poly(6, T)
r3 = abs(int(sp.resultant(phi3, T - 1, T)))
r6 = abs(int(sp.resultant(phi6, T - 1, T)))
check("D1 Phi_3 and Phi_6 have equal degree two", sp.degree(phi3) == sp.degree(phi6) == 2)
check("D2 their Delta resultants remain different (3 versus 1)", (r3, r6) == (3, 1))

print("\n" + "=" * 72)
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")

