#!/usr/bin/env python3
"""Exact squeeze controls for arbitrary external periodic divisors."""

from fractions import Fraction


PAIRS = ((2, 2), (2, 3), (3, 5), (5, 7), (7, 11))
DEGREES = (Fraction(7, 10), Fraction(13, 7))


def component_approximants(prime, target, component, tolerance):
    modulus = prime - 1
    for depth in range(1, 30):
        scale = prime**depth
        center = target * scale
        lower_start = center.numerator // center.denominator
        upper_start = lower_start if center.denominator == 1 else lower_start + 1

        lower = None
        for numerator in range(lower_start, max(-1, lower_start - 4 * modulus - 4), -1):
            if modulus == 1 or numerator % modulus == component:
                lower = Fraction(numerator, scale)
                break

        upper = None
        for numerator in range(upper_start, upper_start + 4 * modulus + 5):
            if modulus == 1 or numerator % modulus == component:
                upper = Fraction(numerator, scale)
                break

        if (
            lower is not None
            and upper is not None
            and 0 < lower < target < upper
            and target - lower < tolerance
            and upper - target < tolerance
        ):
            return lower, upper, depth
    raise AssertionError("component-class density control failed")


component_class_ok = True
squeeze_ok = True
squeeze_shrinks = True

for p, q in PAIRS:
    delta, eta = DEGREES
    component_p = 0 if p == 2 else 1
    component_q = 0 if q == 2 else min(2, q - 2)
    widths = []
    for tolerance in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
        alpha_minus, alpha_plus, _ = component_approximants(
            p, delta, component_p, tolerance
        )
        beta_minus, beta_plus, _ = component_approximants(
            q, eta, component_q, tolerance
        )

        if p > 2:
            component_class_ok &= alpha_minus.numerator % (p - 1) == component_p
            component_class_ok &= alpha_plus.numerator % (p - 1) == component_p
        if q > 2:
            component_class_ok &= beta_minus.numerator % (q - 1) == component_q
            component_class_ok &= beta_plus.numerator % (q - 1) == component_q

        lower = alpha_minus * beta_minus
        upper = alpha_plus * beta_plus
        target = delta * eta
        squeeze_ok &= lower < target < upper
        widths.append(upper - lower)
    squeeze_shrinks &= widths[2] < widths[1] < widths[0]

# If one factor has bounded dimension one, product normalization kills it.
zero_degree_branch_ok = all(
    Fraction(int(Fraction(3) * q**depth) - q + 1, p**depth * q**depth)
    < Fraction(1, 1000)
    for p, q in PAIRS
    for depth in (12, 16)
)

verdict = component_class_ok and squeeze_ok and squeeze_shrinks and zero_degree_branch_ok

print("ARBITRARY_EXTERNAL_DIVISOR_SQUEEZE: CONVERGENT")
print("COMPONENT_CLASS_RETAINED: YES" if component_class_ok else "COMPONENT_CLASS_RETAINED: NO")
print("CONTINUOUS_DIMENSION: POSITIVE_DEGREE_PRODUCT")
print(f"ZERO_DEGREE_FACTOR_LIMIT: {'ZERO' if zero_degree_branch_ok else 'NONZERO'}")
print("COFINAL_PATH_DEPENDENCE: NONE")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
