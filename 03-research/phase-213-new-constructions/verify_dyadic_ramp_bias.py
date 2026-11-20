"""Interval upper bound for the critical-line contribution to the dyadic ramp."""
from flint import acb, arb, ctx

ctx.prec = 80
log_two = arb(2).log()
max_factor = arb(45)/32
total = 2 + arb.const_euler() - (4*arb.pi()).log()
upper = max_factor * total
previous = arb(0)
for zero in acb.zeta_zeros(1, 600):
    t = zero.imag
    assert t > previous and zero.real.contains(arb(1)/2)
    previous = t
    phase = acb(0, t*log_two).exp()
    term = abs((1-phase/4)*(1-phase/8))/abs(acb(2, t)*acb(3, t))
    upper += 2*(term-max_factor/(arb(1)/4+t*t))
assert upper < arb('0.05442')
print("PASS: conditional critical-line budget", upper, "< 0.05442 < 7/128")
