"""Interval certificate for removing the lowest critical pair from the theta kernel."""
from flint import arb, acb, ctx

ctx.prec = 96
# Riemann--Siegel zero enclosure from Arb, indexed from one.
gamma = acb.zeta_zero(1).imag
assert gamma > 14 and gamma < 15
grid = 1024
end = 2 * grid
step = arb(1) / grid
pi = arb.pi()
derivatives = [[], []]
for k in range(end + grid // 2):
    v = arb((k + 1) * step, step)  # v+t spans two adjacent grid cells
    e2 = (2*v).exp()
    half = (v/2).exp()
    totals = [arb(0), arb(0)]
    for n in range(1, 5):
        r = pi*n*n*e2
        factor = half*(-r).exp()
        totals[0] += factor*r*((-8*r+30)*r-15)
        totals[1] += factor*r*(((16*r-112)*r+165)*r-arb(75)/2)
    for table, value in zip(derivatives, totals):
        table.append(value + arb(0, '1e-12'))

sines = [(gamma*arb((k+arb(1)/2)*step, step/2)).sin() for k in range(end)]
for i in range(grid // 2):
    # Strict concavity near zero; strict first derivative thereafter.
    table = derivatives[1 if i < grid // 16 else 0]
    bound = gamma*step*sum((sines[k]*table[i+k] for k in range(end)), arb(0))
    assert bound + arb('1e-25') < 0, (i, bound)
print('PASS: 64 curvature cells, 448 slope cells, gamma =', gamma)
