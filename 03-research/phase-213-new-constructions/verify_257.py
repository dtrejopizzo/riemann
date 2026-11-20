"""Interval certificate for the dyadic weight and the range in round 257."""
from flint import acb, arb, ctx

ctx.prec = 100
length = arb(2).log()
frequency = 2 * arb.pi() / length
zeros = acb.zeta_zeros(1, 20)
weights = arb(0)
trace = arb(0)
for zero in zeros:
    gamma = zero.imag
    argument = gamma * length / 2
    weights += 2 * abs(argument.sin() / argument / (1 - (gamma / frequency)**2))
    trace += 2 / (gamma**2 + arb(1)/4)

height = zeros[-1].imag
remainder = (arb("0.047") - trace) * (1 + 1 / (4 * height**2))
remainder *= 2 * frequency**2 / (length * height * (1 - (frequency/height)**2))
low = weights + remainder
G = arb(3) * 10**12
tail_trace = arb("6.4e-12")
high_coefficient = (1 + arb(2).sqrt()) * frequency**2 / (length * (1 - (frequency/G)**2))
assert low < arb("0.471")
assert high_coefficient < 300
cost = low + 300 * tail_trace * 10**19 / G
cost += 2 * frequency**2 * (arb("0.047") / 1000 + tail_trace)
margin = length * (arb(1)/2 - cost) - arb("1e-12")
assert margin > arb("0.009")
print("verified-zero budget", low)
print("uniform lower margin in units of sqrt(x)", margin)
