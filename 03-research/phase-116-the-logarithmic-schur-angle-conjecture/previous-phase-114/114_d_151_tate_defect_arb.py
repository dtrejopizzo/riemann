#!/usr/bin/env python3
"""Directed superfactorial bound for the D.151 Tate defect."""

from flint import arb, ctx


ctx.dps = 1000
N = 170
T = arb(5).log() / 2
k = T / 2

# Bound i_N(k) by its leading term times the exponential majorant.
double_factorial = arb(1)
for j in range(N + 1):
    double_factorial *= 2 * j + 1

i_bound = k**N / double_factorial * (k * k / (2 * (2 * N + 3))).exp()
A_N = (2 * T * (2 * N + 1)).sqrt() * i_bound
ratio = k / (2 * N + 3) * (arb(2 * N + 3) / (2 * N + 1)).sqrt()
tail = A_N * A_N / (1 - ratio * ratio)
gq_norm = 2 * tail
denominator = 2 * (T.sinh() - T) - gq_norm
eta = (gq_norm / denominator).sqrt()

assert denominator > 0
assert ratio < arb("0.0012")
assert eta < arb("1e-424")

print("D151 directed Tate-defect bound: PASS")
print("ratio upper =", ratio)
print("tail upper =", tail)
print("eta upper =", eta)

