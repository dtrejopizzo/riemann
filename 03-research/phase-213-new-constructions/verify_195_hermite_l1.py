"""Enclose the full theta-weighted L1 error for explicit Hermite prefixes."""
from flint import acb, arb, ctx

ctx.prec = 160
prefixes = (8, 16, 32)
cells = 2048
gamma = [acb.zeta_zero(j).imag for j in range(1, max(prefixes) + 1)]
weights = {}
quarter = arb(1) / 4
for n in prefixes:
    nodes = [quarter] + [-g * g for g in gamma[:n]]
    weights[n] = []
    for j, node in enumerate(nodes):
        coefficient = arb(1)
        for k, other in enumerate(nodes):
            if k != j:
                coefficient *= (9 * quarter - other) / (node - other)
        weights[n].append(coefficient)

# Rational candidate selected by a finite sampled L1 fit; the proof below
# uses only these integers, independently of the optimizer.
weights["fit16"] = [arb(k) / 10**7 for k in (
    10290845, -883521, 2283505, -3379734, 6001705, -7138414, 9609623,
    -20617556, 22237618, -34585409, 39240784, -21541846, 16243476,
    -15617639, 8379129, -666811, 144181)]
width = arb(2) / cells
delta = arb(0, width / 2)
numerator = dict.fromkeys(weights, arb(0))
denominator = arb(0)
pi = arb.pi()
for i in range(cells):
    mid = (i + quarter * 2) * width
    x = mid + delta
    scale = pi * (2 * x).exp()
    density = arb(0)
    for k in range(1, 9):
        a = k * k * scale
        density += (2 * a * a - 3 * a) * (-a).exp()
    density = (x / 2).exp() * density + arb(0, '1e-48')
    denominator += width * density * (x / 2).cosh()
    # Cubic expansion retains cancellation between the cosine coefficients.
    for n, coeff in weights.items():
        central = sum(c * (g * mid).cos() for c, g in zip(coeff[1:], gamma))
        linear = sum(-c * g * (g * mid).sin() for c, g in zip(coeff[1:], gamma))
        quadratic = sum(-c * g**2 * (g * mid).cos() / 2 for c, g in zip(coeff[1:], gamma))
        cubic = sum(c * g**3 * (g * mid).sin() / 6 for c, g in zip(coeff[1:], gamma))
        rem = sum(abs(c) * (g * width / 2)**4 / 24 for c, g in zip(coeff[1:], gamma))
        trig = central + delta * (linear + delta * (quadratic + delta * cubic)) + arb(0, rem)
        residual = (3 * x / 2).cosh() - coeff[0] * (x / 2).cosh() - trig
        numerator[n] += width * density * abs(residual)

# Evenness cancels the factor 2 in the ratio. Normalization is K(1)=1.
for n, coeff in weights.items():
    tail = arb('1e-33') * (1 + sum(map(abs, coeff)))
    value = (numerator[n] + arb(0, tail)) / (denominator + arb(0, '1e-33'))
    print(n, value.lower().str(12), value.upper().str(12))
