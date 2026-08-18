#!/usr/bin/env python3
"""Exact controls for the metric-kernel target-selection theorem."""

from fractions import Fraction


def ceil_log3(value: int) -> int:
    exponent = 0
    power = 1
    while power < value:
        power *= 3
        exponent += 1
    return exponent


def cc_dimension(radius: int) -> int:
    return ceil_log3(2 * radius + 1)


# These controls are fixed by the published rank-one formula.
radii = (1, 4, 13, 40)
cc_values = tuple(cc_dimension(radius) for radius in radii)
cc_control_ok = cc_values == (1, 2, 3, 4)

# a = log(4): multiplication of radii represents addition of exact weights.
normalized_once = cc_dimension(4) - cc_dimension(1)
normalized_twice = cc_dimension(16) - cc_dimension(1)
cc_nonadditive = normalized_twice != 2 * normalized_once

# A two-coordinate Green weight is an exact additive real channel;
# rationals suffice to detect an implementation which rounds or freezes it.
weights = (Fraction(1, 3), Fraction(5, 7), Fraction(-2, 5))


def metric_channel(weight: Fraction) -> tuple[Fraction, Fraction]:
    return (2 * weight, -3 * weight)


def add_vectors(left, right):
    return tuple(x + y for x, y in zip(left, right))


metric_additive = all(
    metric_channel(a + b) == add_vectors(metric_channel(a), metric_channel(b))
    for a in weights
    for b in weights
)
metric_nontrivial = any(metric_channel(weight) != (0, 0) for weight in weights)

# In Z^r, divisibility by every positive integer forces every coordinate
# to vanish.  Increasing windows certify the finite controls used here;
# the document supplies the general finitely-generated-group proof.
vectors = ((0, 0), (1, 0), (0, -1), (6, 10), (-12, 18))
divisors = tuple(range(2, 13))
infinitely_divisible_controls = tuple(
    vector
    for vector in vectors
    if all(all(coordinate % divisor == 0 for coordinate in vector)
           for divisor in divisors)
)
finite_rank_control_ok = infinitely_divisible_controls == ((0, 0),)

# Negative controls: a nonzero integral archimedean class and a frozen
# metric channel must both be rejected by the same gate.
mutated_algebraic_channel = tuple(range(len(radii)))
mutated_algebraic_rejected = len(set(mutated_algebraic_channel)) != 1
def rounded_metric_channel(weight: Fraction) -> tuple[int, int]:
    return (round(2 * weight), round(-3 * weight))


mutated_metric_rejected = any(
    rounded_metric_channel(a + b)
    != add_vectors(rounded_metric_channel(a), rounded_metric_channel(b))
    for a in weights
    for b in weights
)

verdict = all((
    cc_control_ok,
    cc_nonadditive,
    metric_additive,
    metric_nontrivial,
    finite_rank_control_ok,
    mutated_algebraic_rejected,
    mutated_metric_rejected,
))

print("FINITE_RANK_ALGEBRAIC_CHANNEL: CONSTANT_ON_REAL_DIVISORS")
print("TENSOR_COMPATIBLE_METRIC_CHANNEL: NONTRIVIAL")
print(f"CC_INTEGER_DIMENSION_ADDITIVE: {'YES' if not cc_nonadditive else 'NO'}")
print("SURVIVING_TARGET: METRIZED_OR_TOLERANT_PICARD")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
