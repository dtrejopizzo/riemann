"""Certify the frequencies seen by a nonnegative product of six Fejer kernels."""
from itertools import product

from flint import acb, arb, ctx

ctx.prec = 90
zeros = [z.imag for z in acb.zeta_zeros(1, 220)]
selected = zeros[:6]
assert zeros[-1] > 2 * sum(selected)
excursion = arb(0)
for gamma in selected:
    phase = acb(0, gamma * arb(2).log()).exp()
    coefficient = abs((1 - phase / 4) * (1 - phase / 8))
    excursion += coefficient / abs(acb(2, gamma) * acb(3, gamma))
excursion *= arb(4) / 3

for powers in product(range(-2, 3), repeat=len(selected)):
    if sum(map(abs, powers)) <= 1:
        continue
    frequency = abs(sum(k * gamma for k, gamma in zip(powers, selected)))
    assert frequency > 0
    assert all(not frequency.overlaps(gamma) for gamma in zeros)

assert excursion > arb(7) / 128 - arb(1) / 24
print("PASS: normalized excursion lower bound", excursion)
