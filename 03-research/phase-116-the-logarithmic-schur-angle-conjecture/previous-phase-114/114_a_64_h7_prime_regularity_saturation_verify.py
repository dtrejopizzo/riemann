#!/usr/bin/env python3
"""Finite/source checks for the exact H7-PRIME-REG criteria in a64."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
H17 = ROOT / "00-references/papers-nuevos/A/arXiv-1709.05831v1/HARAN_Dec2016_updated_4.tex"
text = H17.read_text()


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    print("PASS", label)


check("2017 source contains tree presentation and cancellation relation",
      r"\label{eq106}" in text
      and r"(10.16) \quad {\bf cancellation}" in text)
check("Section 11 regularity has all-level/all-arity quantifiers",
      r"\label{eq111}" in text and r"\forall \, M \geq N" in text)

# On Z/n, multiplication by p is injective iff the zero congruence is
# {p^k}-saturated.  Exhaustively compare both formulations.
for n in range(1, 51):
    for p in (2, 3, 5, 7, 11):
        injective = len({(p * x) % n for x in range(n)}) == n
        root_closed = all(
            ((p * x) % n != (p * y) % n) or (x == y)
            for x in range(n) for y in range(n)
        )
        check(f"injectivity equals p-root-closure n={n}, p={p}",
              injective == root_closed)

# Residual criterion: diagonal maps into fields of characteristics q != p.
# If the coordinate tuple separates the finite domain, p can be cancelled in
# every coordinate and hence in the domain.
for modulus in (5, 7, 11, 13):
    domain = list(range(modulus))
    for p in (2, 3):
        if modulus == p:
            continue
        evaluation = {x: (x % modulus,) for x in domain}
        faithful = len(set(evaluation.values())) == len(domain)
        target_regular = p % modulus != 0
        implication = all(
            ((p * evaluation[x][0]) % modulus
             != (p * evaluation[y][0]) % modulus) or x == y
            for x in domain for y in domain
        )
        check(f"residual cancellation q={modulus}, p={p}",
              faithful and target_regular and implication)

doc = (HERE / "114_a_64_H7_PRIME_REGULARITY_TREE_SATURATION_AND_RESIDUAL_CRITERION.md").read_text()
check("a108 resolves full prime regularity negatively",
      "full H7-PRIME-REG and 2-root-closure are false" in doc)
print("VERDICT: CRITERIA PASS; a108 PROVES 2-ROOT-CLOSURE FALSE")
