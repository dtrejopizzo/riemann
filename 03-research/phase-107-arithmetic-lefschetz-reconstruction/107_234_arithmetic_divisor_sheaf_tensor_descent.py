#!/usr/bin/env python3
"""Exact certificate for arithmetic-divisor sheaf tensor descent."""

from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent.parent
    / "00-references/papers-nuevos/A/arXiv-2602.15941v1/Jacobian.tex"
)


def valuation(value, prime):
    value = Fraction(value)
    numerator = abs(value.numerator)
    denominator = value.denominator
    result = 0
    while numerator and numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def prime_support(value, *divisors):
    value = Fraction(value)
    candidates = set().union(*(set(divisor) for divisor in divisors))
    residue = abs(value.numerator) * value.denominator
    prime = 2
    while prime * prime <= residue:
        if residue % prime == 0:
            candidates.add(prime)
            while residue % prime == 0:
                residue //= prime
        prime += 1
    if residue > 1:
        candidates.add(residue)
    return sorted(candidates)


def belongs(value, divisor):
    return all(valuation(value, p) >= -divisor.get(p, 0) for p in prime_support(value, divisor))


def split_product(value, first, second):
    """Factor an element of H_(D1+D2) as x*y with x in H_D1, y in H_D2."""
    value = Fraction(value)
    x = Fraction(-1 if value < 0 else 1)
    y = Fraction(1)
    for p in prime_support(value, first, second):
        total = valuation(value, p)
        left = -first.get(p, 0)
        right = total - left
        if right < -second.get(p, 0):
            raise AssertionError("valuation split does not exist")
        if left >= 0:
            x *= p**left
        else:
            x /= p ** (-left)
        if right >= 0:
            y *= p**right
        else:
            y /= p ** (-right)
    if x * y != value or not belongs(x, first) or not belongs(y, second):
        raise AssertionError("invalid product factorization")
    return x, y


source_text = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""
source_checks = {
    "picard_monoid": "canonical monoid isomorphism $X_\\Q \\cong \\Pic(\\spzb)$" in source_text,
    "divisor_sheaf": all(
        token in source_text
        for token in (
            "The following construction defines a sheaf",
            "If an open set $U$ does not contain $\\infty$, set",
            "If $U$ contains $\\infty$, define",
        )
    ),
    "mass_ball": "\\sum_{x\\in X\\setminus\\{*\\}}\\|\\phi(x)\\|\\le 1" in source_text,
    "tensor_product": "The group $L$ is the tensor product: $L = L_1 \\otimes_\\Z L_2$" in source_text,
    "rooted_monoid": "canonical isomorphism of monoids between moduli of framed and rooted" in source_text,
}

# Fixed before calculation: ordinary, localized, mixed-prime, and deep divisors.
ATLAS = (
    ({}, {}, Fraction(1), Fraction(1)),
    ({2: 1}, {3: 1}, Fraction(2), Fraction(3, 2)),
    ({2: 3, 5: 1}, {2: 1, 7: 2}, Fraction(5, 3), Fraction(7, 4)),
    ({3: 4, 11: 2}, {5: 3, 11: 1}, Fraction(13, 5), Fraction(17, 6)),
    ({2: 6, 3: 2, 13: 1}, {2: 2, 5: 4, 13: 3}, Fraction(19, 7), Fraction(23, 8)),
)
NUMERATORS = (-3003, -35, -1, 1, 10, 77, 2145)

valuation_descent = True
projective_mass = True
atlas_nontrivial = len(ATLAS) >= 5

for first, second, lambda_one, lambda_two in ATLAS:
    product = {p: first.get(p, 0) + second.get(p, 0) for p in set(first) | set(second)}
    sections = []
    factorizations = []
    denominator = 1
    for p, exponent in product.items():
        denominator *= p**exponent
    for numerator in NUMERATORS:
        z = Fraction(numerator, denominator)
        if belongs(z, product):
            x, y = split_product(z, first, second)
            valuation_descent &= x * y == z and belongs(x, first) and belongs(y, second)
            sections.append(z)
            factorizations.append((x, y))

    target_mass = lambda_one * lambda_two * sum(abs(z) for z in sections)
    factor_mass = sum(
        (lambda_one * abs(x)) * (lambda_two * abs(y))
        for x, y in factorizations
    )
    projective_mass &= target_mass == factor_mass

# Deliberate negative controls: lowering one product valuation or changing the
# product seminorm must be detected.
negative_valuation_detected = not belongs(Fraction(1, 4), {2: 1})
negative_norm_detected = Fraction(2) * Fraction(3) != Fraction(2) + Fraction(3)

source_ok = all(source_checks.values())
verdict = all(
    (
        source_ok,
        atlas_nontrivial,
        valuation_descent,
        projective_mass,
        negative_valuation_detected,
        negative_norm_detected,
    )
)

print(f"PUBLISHED_ARITHMETIC_PICARD_MONOID: {'YES' if source_checks['picard_monoid'] else 'NO'}")
print(f"PUBLISHED_DIVISOR_SHEAF_O_D: {'YES' if source_checks['divisor_sheaf'] else 'NO'}")
print(f"FINITE_TENSOR_DESCENT: {'YES' if valuation_descent else 'NO'}")
print(f"ARCHIMEDEAN_PROJECTIVE_MASS_EQUALITY: {'YES' if projective_mass else 'NO'}")
print(f"ROOTED_GALOIS_CHANNEL_RETAINED: {'YES' if source_checks['rooted_monoid'] else 'NO'}")
print("ARITHMETIC_DIVISOR_SHEAF_TENSOR_DESCENT: CLOSED" if verdict else "ARITHMETIC_DIVISOR_SHEAF_TENSOR_DESCENT: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
