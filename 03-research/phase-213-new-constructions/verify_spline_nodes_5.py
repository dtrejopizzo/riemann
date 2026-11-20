"""Verify the disjoint sampling disks and exterior-zero error for the spline tests."""
from flint import acb, arb, ctx

ctx.prec = 128
a = arb(5) / 28
height = arb(3) * 10**12
floor = arb(3) / 50
positive = [acb.zeta_zero(j).imag for j in (*range(1, 10), 12, 13, 15)]
nodes = [-v for v in reversed(positive)] + positive
assert all(right - left > 2 for left, right in zip(nodes, nodes[1:]))
assert all(abs(x) < 66 and abs((a*x).sinc()) > floor for x in nodes)
assert (a/2).cosh() / a < 6
ratio = 36 * arb(2)**(arb(7)/5) / (height**(arb(3)/5) * floor**2)
assert ratio < 1
assert arb('0.0465') * height**2 * ratio**28 < arb('7e-63')
print('PASS: 24 disjoint disks, spline samples and relative tail bound')
