#!/usr/bin/env python3
"""Exact audit of the quarter-dyadic D.79 tail blocks and weights."""
from fractions import Fraction as Q

DEPTH = 160
blocks = []
covered = []
for octave in range(8):
    n0 = DEPTH * 2**octave
    step = n0 // 4
    for part in range(4):
        lo = n0 + part * step
        hi = lo + step
        B = Q(4 * lo + 1, 2)  # 2*lo+1/2
        # The verifier evaluates this finite positive sum in directed Arb.
        # Here we audit its exact index set without constructing a rational
        # with tens of thousands of denominator factors.
        blocks.append((lo, hi, B))
        covered.extend(range(lo, hi))

assert covered == list(range(DEPTH, DEPTH * 2**8))
for left, right in zip(blocks, blocks[1:]):
    assert left[1] == right[0]

# For b>=B the derivative in x of
# B(B^2+x)/(b(b^2+x)) is B(b^2-B^2)/(b(b^2+x)^2)>=0;
# hence its minimum is (B/b)^3.  Check the discrete hypotheses exactly.
for lo, hi, B in blocks:
    for j in range(lo, hi):
        b = Q(4*j + 1, 2)
        assert b >= B

print("PASS 32 exact quarter-dyadic blocks cover [160,40960)")
