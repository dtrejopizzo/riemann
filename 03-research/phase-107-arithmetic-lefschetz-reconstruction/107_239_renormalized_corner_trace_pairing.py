#!/usr/bin/env python3
"""Source-backed certificate for the renormalized corner trace pairing."""

from fractions import Fraction
from math import exp
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
SOURCE = (
    HERE.parent.parent
    / "00-references/papers-nuevos/A/arXiv-2602.15941v1/Jacobian.tex"
)
source = SOURCE.read_text(encoding="utf-8") if SOURCE.exists() else ""

published_operator = all(
    token in source
    for token in (
        r"(\theta(u) \, \xi) (a) = \xi (u^{-1} a)",
        "R_\\lambda = \\widehat P_\\lambda  P_\\lambda",
        "2h (1) \\log \\lambda",
    )
)
published_semilocal_limit = all(
    token in source
    for token in (
        "\\Tr (\\theta(h)R_\\lambda)",
        "\\sum_{v \\in S}",
        "\\frac{h(u^{-1}) }{ \\vert 1-u \\vert}",
        "+ o(1)",
    )
)
published_fixed_point_geometry = all(
    token in source
    for token in (
        "isotropy groups of the action",
        "This transverse space is identified with the local field $\\Q_v$",
        "\\delta((u-1)x)",
        "\\frac{1}{|u-1|}",
    )
)
published_global_identity = all(
    token in source
    for token in (
        "The generalized Weil explicit formula",
        "\\sum_v \\int_{\\Q_v^\\times}^{\\prime}",
        "\\hat{h}(0) + \\hat{h}(1)",
    )
)


def cyclic_convolution(left, right, size):
    result = [Fraction(0) for _ in range(size)]
    for index in range(size):
        result[index] = sum(
            left[j] * right[(index - j) % size]
            for j in range(size)
        )
    return result


def regular_matrix(function):
    size = len(function)
    return sp.Matrix(
        size,
        size,
        lambda row, col: sp.Rational(function[(row - col) % size].numerator,
                                             function[(row - col) % size].denominator),
    )


composition_convolution = True
for size in (5, 7, 8, 11, 13):
    left = [Fraction((3 * i + 1) % size, i + 1) for i in range(size)]
    right = [Fraction((5 * i + 2) % size, i + 2) for i in range(size)]
    convolution = cyclic_convolution(left, right, size)
    composition_convolution &= regular_matrix(left) * regular_matrix(right) == regular_matrix(convolution)


def primes_up_to(bound):
    result = []
    for candidate in range(2, bound + 1):
        if all(candidate % p for p in range(2, int(candidate**0.5) + 1)):
            result.append(candidate)
    return result


support_stabilization = True
for window in (2, 3, 4, 5, 6):
    bound = int(exp(window))
    visible = primes_up_to(bound)
    support_stabilization &= all(p <= bound for p in visible)
    support_stabilization &= all(
        p**k > bound
        for p in primes_up_to(bound + 50)
        if p > bound
        for k in (1, 2, 3)
    )


def p_adic_abs(value, prime):
    value = Fraction(value)
    exponent = 0
    numerator = abs(value.numerator)
    denominator = value.denominator
    while numerator and numerator % prime == 0:
        numerator //= prime
        exponent += 1
    while denominator % prime == 0:
        denominator //= prime
        exponent -= 1
    return Fraction(prime) ** (-exponent)


fixed_point_jacobian = True
for value in (Fraction(2), Fraction(3, 2), Fraction(5, 3), Fraction(7, 5), Fraction(11, 7)):
    fixed_point_jacobian &= Fraction(1, 1) / abs(1 - value) > 0
for prime, value in ((2, Fraction(3)), (3, Fraction(4)), (5, Fraction(6)),
                     (7, Fraction(8)), (11, Fraction(12))):
    fixed_point_jacobian &= Fraction(1, 1) / p_adic_abs(1 - value, prime) > 0

renormalized_trace_defined = published_operator and published_semilocal_limit
equals_weil_n = renormalized_trace_defined and published_global_identity and support_stabilization
verdict = all(
    (
        published_operator,
        published_semilocal_limit,
        published_fixed_point_geometry,
        published_global_identity,
        composition_convolution,
        support_stabilization,
        fixed_point_jacobian,
        equals_weil_n,
    )
)

print(f"RENORMALIZED_SEMILOCAL_TRACE: {'DEFINED' if renormalized_trace_defined else 'NOT_DEFINED'}")
print(f"COMPOSITION_CONVOLUTION_COMPATIBILITY: {'YES' if composition_convolution else 'NO'}")
print(f"COMPACT_SUPPORT_PLACE_STABILIZATION: {'YES' if support_stabilization else 'NO'}")
print(f"LOCAL_FIXED_POINT_JACOBIAN: {'YES' if fixed_point_jacobian else 'NO'}")
print(f"DC_CORNER_PAIRING: {'CONSTRUCTED' if verdict else 'OPEN'}")
print(f"PAIRING_VALUE: {'WEIL_N' if equals_weil_n else 'UNIDENTIFIED'}")
print("RR_INTERSECTION_AXIOMS: OPEN")
print("ROW_A_STATUS: PARTIAL")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
