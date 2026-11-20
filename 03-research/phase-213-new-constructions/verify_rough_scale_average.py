"""Critical-line budget for equally weighted rational dilations of the rough sum."""
from flint import acb, arb, ctx

ctx.prec = 80
ratio = arb(14) / 13
count = 6
majorant = arb(45) / 32
budget = majorant * (2 + arb.const_euler() - (4 * arb.pi()).log())
previous = arb(0)
for zero in acb.zeta_zeros(1, 600):
    gamma = zero.imag
    assert gamma > previous and zero.real.contains(arb(1) / 2)
    previous = gamma
    phase = acb(0, gamma * arb(2).log()).exp()
    step = acb(0, gamma * ratio.log()).exp()
    average = sum(step**j for j in range(count)) / count
    coefficient = (1 - phase / 4) * (1 - phase / 8)
    coefficient /= acb(2, gamma) * acb(3, gamma)
    budget += 2 * (abs(average * coefficient) - majorant / (arb(1)/4 + gamma**2))

margin = arb(7)/128 - arb(1)/24 - budget
assert margin > 0
print("PASS: lower bound for the conditional margin", margin)
