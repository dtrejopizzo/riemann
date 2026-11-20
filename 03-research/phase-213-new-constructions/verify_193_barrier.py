"""Rayleigh lower bound for the compressed prime operator at radius 3.3."""
from math import isqrt

from flint import arb, ctx

ctx.prec = 160
width = arb(33) / 5
lower = arb(0)
for p in range(2, 701):
    if any(p % d == 0 for d in range(2, isqrt(p) + 1)):
        continue
    q = p
    while q <= 700:
        overlap = 1 - arb(q).log() / width
        assert overlap > 0
        lower += 2 * arb(p).log() * overlap / arb(q).sqrt()
        q *= p

upper = (arb(3 * 10**12) / (8 * arb.pi())).log()
assert lower > 26
assert upper < 26
print("Rayleigh lower bound from q <= 700:", lower)
print("Upper bound for log(R/(2*pi)):", upper)
