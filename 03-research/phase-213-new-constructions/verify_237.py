"""Certified bounds for the residues used in ROUND_237_A.md (python-flint)."""

from flint import arb, ctx

ctx.prec = 96
cells = 1024
mid_height = arb(2827) / 200
real_zero = arb(0)
real_first = arb(0)
imag_first = arb(0)

for j in range(cells):
    y = 1 + arb(2 * j + 1) / (2 * cells)
    base = (2 * arb.pi() * y).cos() / y.sqrt()
    phase = mid_height * y.log()
    real_zero += base
    real_first += base * phase.cos()
    imag_first += base * phase.sin()

# Integral of the distance to the cell midpoint, summed over [1,2].
# |d/dy of the integrand| <= |-.5+it| + 2*pi, bounded by 7 or 22.
err_zero = arb(7) / (4 * cells)
# On the entire certified ordinate bracket |delta t| <= 1/200,
# and |dH/dt| <= log(2) < 1.
err_first = arb(22) / (4 * cells) + arb(1) / 200
real_zero /= cells
real_first /= cells
imag_first /= cells

assert abs(real_zero) + err_zero < arb(1) / 100
assert real_first + err_first < -arb(16) / 100
assert imag_first - err_first > arb(20) / 100
assert (arb(16) / 100) ** 2 + (arb(20) / 100) ** 2 > (arb(25) / 100) ** 2
print("PASS |H(1/2)| < 1/100 and |H(1/2+i gamma)| > 1/4 for 14.13 <= gamma <= 14.14")
