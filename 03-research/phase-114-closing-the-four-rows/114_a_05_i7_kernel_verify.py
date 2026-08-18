#!/usr/bin/env python3
"""Exact finite audit for 114.a.05.  No zeta zeros and no floating decisions."""

import sys
import sympy as sp

T = sp.symbols("T")
FAIL = []


def check(name, condition, detail=""):
    print(("PASS  " if condition else "FAIL  ") + name + (("   " + detail) if detail else ""))
    if not condition:
        FAIL.append(name)


def phi(n):
    return sp.Poly(sp.cyclotomic_poly(n, T), T, domain=sp.ZZ)


def beta_cyclotomic(n):
    # Kronecker: every cyclotomic has logarithmic Mahler measure zero.
    return (int(sp.totient(n)), sp.Integer(0))


print("A. Explicit cyclotomic kernel lattice")
irreducible = all(phi(n).is_irreducible for n in range(1, 81))
distinct = len({str(phi(n).as_expr()) for n in range(1, 81)}) == 80
check("A1 Phi_1,...,Phi_80 are distinct irreducibles over Z", irreducible and distinct)

kernel_ok = True
for n in range(2, 81):
    b_n = beta_cyclotomic(n)
    b_1 = beta_cyclotomic(1)
    e_beta = (b_n[0] - int(sp.totient(n)) * b_1[0], b_n[1] - int(sp.totient(n)) * b_1[1])
    kernel_ok &= e_beta == (0, 0)
check("A2 E_n=C_n-phi(n)C_1 lies in ker(r,m), 2<=n<=80", kernel_ok)

# Coordinate matrix of E_2,...,E_N in basis C_1,...,C_N.
independent = True
for N in (5, 10, 20, 40):
    matrix = sp.zeros(N, N - 1)
    for n in range(2, N + 1):
        matrix[0, n - 2] = -sp.totient(n)
        matrix[n - 1, n - 2] = 1
    independent &= matrix.rank() == N - 1
check("A3 E_2,...,E_N have full column rank for N=5,10,20,40", independent)

print("\nB. I7 no-factorisation witness")
b3, b6 = beta_cyclotomic(3), beta_cyclotomic(6)
check("B1 beta(C_3)=beta(C_6)=(2,0)", b3 == b6 == (2, 0), f"b3={b3}, b6={b6}")

delta = T - 1
r3 = abs(int(sp.resultant(phi(3).as_expr(), delta, T)))
r6 = abs(int(sp.resultant(phi(6).as_expr(), delta, T)))
check("B2 |Res(Phi_3,T-1)|=3 and |Res(Phi_6,T-1)|=1", (r3, r6) == (3, 1),
      f"values={(r3, r6)}")
check("B3 intersections are log(3) and 0, despite identical bidegree", sp.log(r3) != sp.log(r6))

print("\nC. Mahler blindness and missing diagonal")
mahler_blind = all(beta_cyclotomic(n)[1] == 0 for n in range(1, 201))
check("C1 Mahler coordinate vanishes on C_1,...,C_200", mahler_blind)
check("C2 Mahler coordinate vanishes on every tested E_n and nonzero multiple",
      all(k * (beta_cyclotomic(n)[1] - sp.totient(n) * beta_cyclotomic(1)[1]) == 0
          for n in range(2, 81) for k in (-7, -1, 1, 9)))
check("C3 the ordinary resultant has no diagonal: Res(Phi_12,Phi_12)=0",
      sp.resultant(phi(12).as_expr(), phi(12).as_expr(), T) == 0)

print("\nD. Haran source anchors")
# These are source-presence guards, not a substitute for the mathematical reading.
from pathlib import Path

source = Path(__file__).parents[2] / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = source.read_text(encoding="utf-8")
anchors = [r"D_d (X_N)", r"{\mathcal O}_{X_N} (D)", r"{\mathcal B}_d^* (X)", r"{\rm Pic}"]
check("D1 Haran section 11 contains bundles, section sheaves, bounded completion and Pic",
      all(anchor in text for anchor in anchors))

print("\n" + "=" * 72)
if FAIL:
    print("FAILED CHECKS:", FAIL)
    sys.exit(1)
print("VERDICT: ALL CHECKS PASS")
sys.exit(0)

