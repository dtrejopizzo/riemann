"""Validate the single preselected asinh residual jet minor {5, 6}.

Only half-moments of orders 0, 2, ..., 26 are used.  The finite sixteen-mode
theta integrand is entire and is integrated on the fixed interval [0, 3].
No other residual block is evaluated.  Numerical integration uses outward
complex balls; the omitted mode and temporal tails are added separately.

Tail bounds, uniform over these fourteen moment orders:
* For n >= 17 and 0 <= t <= 3, Phi_n <= 2*pi^2*n^4*exp(9*t/2-3*n^2).
  Using 2 < e < 4, pi < 4, successive terms have ratio < 1/2.
  The integrated tail is < 2^33 * 2 * 17^4 * 2^-867 * 3^27
  < 2^-762, hence in particular < 2^-646.
* For t >= 3, Phi(t) <= 4*pi^2*exp(9*t/2-pi*exp(2*t)).
  Here sum n^4*exp(-x*(n^2-1)) < 2 for x >= 3, by the same ratio test.
  Since t^j <= 26!*exp(t), set x=pi*exp(2*t)>1200.  The inequality
  x^(7/4) <= exp(x/4) gives a tail < (8/3)*26!*pi^(-3/4)*exp(-900)
  < 2^-798, hence in particular < 2^-768.
Thus their sum is < 2^-645 < 2^-500.  Radius 2^-500 is added to EACH
computed half-moment.  The common factor two for full even moments cancels
in N(x)=2 F'(x)/F(x).
"""

from fractions import Fraction
from hashlib import sha256
from math import factorial
from pathlib import Path

from flint import acb, arb, ctx


PRECISION = 256
MODES = 16
PANELS = 12
MOMENT_ORDERS = tuple(range(0, 27, 2))
TOLERANCE_BITS = 230
TAIL_BITS = 500
EVAL_LIMIT = 200000

# Exact elementary bounds used in the tail proof above.
assert 17**4 < 2**17
assert 3**27 < 2**54
assert factorial(26) < 2**100
assert sum((Fraction(3)**k / factorial(k) for k in range(9)), Fraction(0)) > 20
assert 1200**2 < 2**21
assert Fraction(2)**33 * 2 * 17**4 * Fraction(2)**(-867) * 3**27 < Fraction(2)**(-646)
assert 3 * factorial(26) * Fraction(2)**(-900) < Fraction(2)**(-768)
assert Fraction(2)**(-646) + Fraction(2)**(-768) < Fraction(2)**(-TAIL_BITS)

ctx.prec = PRECISION
pi = arb.pi()
assert pi > 3 and pi < 4
assert arb(1).exp() > 2 and arb(1).exp() < 4
tolerance = arb(1) / 2**TOLERANCE_BITS
tail_radius = arb(1) / 2**TAIL_BITS


def theta16(z):
    y = pi * (2 * z).exp()
    total = acb(0)
    for n in range(1, MODES + 1):
        total += n*n * (2*n*n*y - 3) * (-n*n*y).exp()
    return pi * (5*z/2).exp() * total


half_moments = []
for order in MOMENT_ORDERS:
    total = arb(0)
    for panel in range(PANELS):
        left = acb(panel) / 4
        right = acb(panel + 1) / 4
        # This finite-mode integrand is entire; no branch depends on the
        # integration callback's analytic flag.
        value = acb.integral(
            lambda z, analytic: z**order * theta16(z),
            left,
            right,
            rel_tol=tolerance,
            abs_tol=tolerance,
            eval_limit=EVAL_LIMIT,
        )
        assert value.is_finite(), (order, panel, value)
        assert value.imag.contains(0), (order, panel, value)
        total += value.real
    moment = total + arb(0, tail_radius.upper())
    assert moment.is_finite() and moment > 0, (order, moment)
    half_moments.append(moment)
    print("PASS complete half-moment", order, flush=True)

f_coefficients = [moment / factorial(order)
                  for order, moment in zip(MOMENT_ORDERS, half_moments)]
n_real = []
for k in range(13):
    numerator = 2*(k+1)*f_coefficients[k+1]
    numerator -= sum((f_coefficients[j]*n_real[k-j]
                      for j in range(1, k+1)), arb(0))
    n_real.append(numerator / f_coefficients[0])

residual = {}
for n in (10, 11, 12):
    central_binomial = factorial(2*n) // (factorial(n)**2)
    n_model = ((-1)**n * central_binomial
               / (2 * arb(4)**n * (2*n+1) * (4*pi)**(2*n+1)))
    residual[n] = n_real[n] - n_model
    assert residual[n].is_finite()

determinant = residual[10]*residual[12] - residual[11]**2
assert determinant.is_finite()
for n in (10, 11, 12):
    print("ND" + str(n), residual[n], flush=True)
print("determinant jet minor {5,6}", determinant, flush=True)
print("determinant lower", determinant.lower(), flush=True)
print("determinant upper", determinant.upper(), flush=True)
assert determinant.upper() < 0, ("INCONCLUSIVE prescribed minor", determinant)
print("PASS: prescribed asinh residual jet minor {5,6} is NEGATIVE", flush=True)
print("SCRIPT SHA256", sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
