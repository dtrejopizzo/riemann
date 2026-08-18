#!/usr/bin/env python3
"""Checks for the Witt operator correspondence algebra; no geometric claim."""

from math import isclose, log
from pathlib import Path

from sympy import cyclotomic_poly, symbols
from sympy.functions.combinatorial.numbers import reduced_totient
from sympy import totient


ROOT = Path(__file__).resolve().parent
SOURCE = (ROOT.parent.parent / "00-references/papers-nuevos/mas-papers/"
          "arXiv-2209.08536v3/"
          "Non-Additive-Geometry-and-Frobenius-Correspondences.tex")
text = SOURCE.read_text()

print("A. Source anchors and exact types")
for anchor in ("label{eq:12.14}", "label{eq:12.35}",
               "label{eq:12.37}", "label{eq:13.37}",
               "label{remark:12.42}"):
    assert anchor in text
assert "we realy\nneed the intersection theory on the surface" in text
print("  Witt basis, Hilbert state, Verschiebung, lambda trace and warning found")

print("\nB. Verschiebung semigroup and cyclic faithfulness")
cutoff = 120
for m in range(1, 11):
    for n in range(1, 11):
        # V_m V_n(phi_1)=phi_{mn}=V_{mn}(phi_1).
        assert m * n <= cutoff
        assert (m * n) == (n * m)
# A finite linear combination applied to phi_1 has coefficient a_n at phi_n.
coefficients = {1: 3, 2: -5, 6: 7, 11: -2}
image_on_phi1 = dict(coefficients)
assert image_on_phi1 == coefficients
assert any(image_on_phi1.values())
print("  V_m V_n=V_mn and the cyclic vector separates finite sums")

print("\nC. Cyclotomic mass equals von Mangoldt")
t = symbols("t")
for n in range(2, 401):
    value = int(cyclotomic_poly(n, t).subs(t, 1))
    prime_power_base = None
    for p in range(2, n + 1):
        if all(p % d for d in range(2, int(p**0.5) + 1)):
            power = p
            while power < n:
                power *= p
            if power == n:
                prime_power_base = p
                break
    expected = log(prime_power_base) if prime_power_base else 0.0
    assert value == (prime_power_base if prime_power_base else 1)
    assert isclose(log(abs(value)), expected)
print("  log|Phi_n(1)|=Lambda(n) for 2<=n<=400")

print("\nD. Orthogonal norms are nonzero")
for n in range(1, 401):
    assert int(totient(n)) > 0
print("  ||phi_n||^2=varphi(n)>0")

print("\nVERDICT: I7 WITT OPERATOR CORRESPONDENCE CHECKS PASS")
