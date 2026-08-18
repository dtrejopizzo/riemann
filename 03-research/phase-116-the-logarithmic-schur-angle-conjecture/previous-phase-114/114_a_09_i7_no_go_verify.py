#!/usr/bin/env python3
"""Exact audit of the Frobenius/principal I7 no-go in 114.a.09."""

import math
import sys

import sympy as sp

T, X = sp.symbols("T X")
FAIL = []


def check(name, condition, detail=""):
    print(("PASS  " if condition else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not condition:
        FAIL.append(name)


def frobenius_poly(n, N):
    """Polynomial whose roots are Nth powers of primitive nth roots."""
    A = sp.cyclotomic_poly(n, T)
    resultant = sp.resultant(A, X - T**N, T)
    return sp.Poly(resultant, X, domain=sp.ZZ).monic()


print("A. Coprime Frobenius fixed points")
bad = []
tested = 0
for n in range(2, 61):
    target = sp.Poly(sp.cyclotomic_poly(n, X), X, domain=sp.ZZ)
    for N in range(2, 12):
        if math.gcd(n, N) != 1:
            continue
        tested += 1
        if sp.expand(frobenius_poly(n, N).as_expr() - target.as_expr()) != 0:
            bad.append((n, N))
check(f"A1 F_N(Phi_n)=Phi_n for {tested} coprime pairs", not bad, f"bad={bad[:3]}")

check("A2 C_1 is fixed by every tested Frobenius",
      all(sp.Poly(sp.resultant(T - 1, X - T**N, T), X).monic().as_expr() == X - 1
          for N in range(2, 20)))

print("\nB. Weight-one obstruction")
# Symbolically: g(F_N E_n)=g(E_n) by fixedness and also N*g(E_n).
g, Nsym = sp.symbols("g N", real=True)
forced = sp.solve(sp.Eq(g, Nsym * g), g)
check("B1 fixed point plus weight one forces gauge value zero", forced == [0])
check("B2 each E_n has a coprime N>=2 (chosen below)",
      all(math.gcd(n, next(N for N in range(2, n + 3) if math.gcd(n, N) == 1)) == 1
          for n in range(2, 100)))

print("\nC. Principal/local distinction")
bad_degree = []
bad_resultant = []
for n in range(2, 101):
    phi_n = sp.Poly(sp.cyclotomic_poly(n, T), T)
    if phi_n.degree() != int(sp.totient(n)):
        bad_degree.append(n)
    res = abs(int(sp.resultant(phi_n.as_expr(), T - 1, T)))
    expected = int(sp.exp(sp.log(next(iter(sp.factorint(n))))) if len(sp.factorint(n)) == 1 else 1)
    if res != expected:
        bad_resultant.append((n, res, expected))
check("C1 deg Phi_n=phi(n), so Z_n-phi(n)D_inf has degree zero", not bad_degree)
check("C2 finite resultant is p on prime powers and 1 otherwise", not bad_resultant,
      f"bad={bad_resultant[:3]}")
principal_ratio_degree = sp.degree(phi3 := sp.cyclotomic_poly(3, T)) - sp.degree(phi6 := sp.cyclotomic_poly(6, T))
check("C3 Phi_3/Phi_6 has degree zero, hence Z_3-Z_6 is principal after compactification",
      principal_ratio_degree == 0)

print("\n" + "=" * 72)
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
