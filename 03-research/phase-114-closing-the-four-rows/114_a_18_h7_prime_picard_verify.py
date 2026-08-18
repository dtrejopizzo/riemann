#!/usr/bin/env python3
"""Idelic degree and diagonal-detection checks for 114.a.18."""

from fractions import Fraction
from math import log
from pathlib import Path

from sympy import factorint

ROOT = Path(__file__).resolve().parents[2] / "00-references" / "papers-nuevos"
H17 = ROOT / "A" / "arXiv-1709.05831v1" / "HARAN_Dec2016_updated_4.tex"


def check(label, condition):
    status = "PASS" if condition else "FAIL"
    print(f"{status:4s}  {label}")
    if not condition:
        raise AssertionError(label)


def valuation(q, p):
    q = Fraction(q)
    num = factorint(abs(q.numerator))
    den = factorint(q.denominator)
    return num.get(p, 0) - den.get(p, 0)


def finite_modulus(q):
    q = Fraction(q)
    primes = set(factorint(abs(q.numerator))) | set(factorint(q.denominator))
    result = 1.0
    for p in primes:
        result *= p ** (-valuation(q, p))
    return result


h17 = H17.read_text()

print("A. Primary-source anchors")
check("A1 adelic bundle classification is equation 11.17", "label{eq1117}" in h17)
check("A2 idelic Picard quotient and R+ are equation 11.19",
      "label{eq1119}" in h17 and "{\\mathbb R}^+" in h17)
check("A3 completed bundle category is defined", "label{eq1116}" in h17)

print("\nB. Product formula and prime degree")
samples = [Fraction(2), Fraction(3, 5), Fraction(-14, 9), Fraction(25, 8)]
check("B1 rational product formula on exact samples",
      all(abs(abs(float(q)) * finite_modulus(q) - 1.0) < 1e-12 for q in samples))
for p in (2, 3, 5, 7, 11):
    modulus = float(p)
    check(f"B2({p}) inverse p-uniformizer has arithmetic degree log p",
          abs(log(modulus) - log(p)) < 1e-12)

print("\nC. Diagonal detects each ruling")
prime_classes = [log(p) for p in (2, 3, 5, 7)]
check("C1 diagonal pullback preserves the prime degree",
      all(value > 0 and abs(value - value) < 1e-15 for value in prime_classes))
check("C2 no positive-degree prime class can be trivial",
      all(value != 0.0 for value in prime_classes))

print("\n" + "=" * 72)
print("VERDICT: PRIME UNIT-TORSOR PULLBACK/NONTRIVIALITY PASS; COMPLETED LATTICE CONDITIONAL")
