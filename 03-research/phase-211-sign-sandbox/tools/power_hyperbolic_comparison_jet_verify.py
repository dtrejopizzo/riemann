"""Certify only jet minor {5,6} of K_Phi minus K_hyperbolic(2*pi).

Fixed design: 256 bits, fourteen even half-moments through order26,
sixteen theta modes, twelve quarter-length panels on [0,3], and absolute
and relative integration tolerances 2^-230.  Each half-moment receives
radius 2^-500 for omitted tails.  No other residual block is evaluated.

The theta-mode tail is < 2^-646, by the exact estimates also used in
power_asinh_comparison_jet_verify.py.  The common temporal majorant
4*pi^2*exp(9*t/2-pi*exp(2*t)), valid for t>=3, bounds BOTH densities.
Using t^j<=26!*exp(t), x=pi*exp(2*t)>1200 and x^(7/4)<=exp(x/4),
its integrated tail is < (8/3)*26!*pi^(-3/4)*exp(-900)<2^-768.
Thus adding radius 2^-500 encloses every complete half-moment.
Both finite theta and hyperbolic integrands are entire.
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
    y = pi * (2*z).exp()
    total = acb(0)
    for n in range(1, MODES + 1):
        total += n*n * (2*n*n*y - 3) * (-n*n*y).exp()
    return pi * (5*z/2).exp() * total


def hyperbolic(z):
    return (-2*pi*(2*z).cosh()).exp()


def complete_half_moments(density, label):
    moments = []
    for order in MOMENT_ORDERS:
        total = arb(0)
        for panel in range(PANELS):
            value = acb.integral(
                lambda z, analytic: z**order * density(z),
                acb(panel)/4,
                acb(panel+1)/4,
                rel_tol=tolerance,
                abs_tol=tolerance,
                eval_limit=EVAL_LIMIT,
            )
            assert value.is_finite(), (label, order, panel, value)
            assert value.imag.contains(0), (label, order, panel, value)
            total += value.real
        moment = total + arb(0, tail_radius.upper())
        assert moment.is_finite() and moment > 0, (label, order, moment)
        moments.append(moment)
        print("PASS complete half-moment", label, order, flush=True)
    return moments


def n_coefficients(moments):
    # The factor two for complete even moments cancels from 2 F'/F.
    f = [moment/factorial(order)
         for order, moment in zip(MOMENT_ORDERS, moments)]
    n = []
    for k in range(13):
        numerator = 2*(k+1)*f[k+1]
        numerator -= sum((f[j]*n[k-j] for j in range(1, k+1)), arb(0))
        n.append(numerator/f[0])
    return n


n_real = n_coefficients(complete_half_moments(theta16, "Phi"))
n_hyperbolic = n_coefficients(complete_half_moments(hyperbolic, "hyperbolic"))
residual = {n: n_real[n]-n_hyperbolic[n] for n in (10, 11, 12)}
determinant = residual[10]*residual[12] - residual[11]**2
assert determinant.is_finite()
for n in (10, 11, 12):
    print("ND" + str(n), residual[n], flush=True)
print("determinant jet minor {5,6}", determinant, flush=True)
print("determinant lower", determinant.lower(), flush=True)
print("determinant upper", determinant.upper(), flush=True)
assert determinant.upper() < 0, ("INCONCLUSIVE prescribed minor", determinant)
print("PASS: prescribed hyperbolic residual jet minor {5,6} is NEGATIVE", flush=True)
print("SCRIPT SHA256", sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
