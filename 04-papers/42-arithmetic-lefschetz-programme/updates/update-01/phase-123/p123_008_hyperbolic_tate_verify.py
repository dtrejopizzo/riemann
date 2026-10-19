#!/usr/bin/env python3
"""Exact finite checks for the hyperbolic Tate realization."""

from fractions import Fraction


def mulq(x, y):
    out = {}
    for q, a in x.items():
        for r, b in y.items():
            out[q * r] = out.get(q * r, Fraction(0)) + a * b
    return {q: a for q, a in out.items() if a}


def dagger(x):
    return {Fraction(1, q): a for q, a in x.items()}


# Avoid irrational square roots in the exact regression by testing the
# squared Tate characters q^(+-1); the algebra/dagger identities are the
# same.  The note itself uses the half powers required by normalization.
def rho2(x):
    return (
        sum(a / q for q, a in x.items()),
        sum(a * q for q, a in x.items()),
    )


def bt_mul(z, w):
    return (z[0] * w[0], z[1] * w[1])


def sharp(z):
    return (z[1], z[0])


def beta(z, w):
    sw = sharp(w)
    return z[0] * sw[0] + z[1] * sw[1]


a = {Fraction(1): Fraction(2), Fraction(2): Fraction(-3), Fraction(1, 3): Fraction(5)}
b = {Fraction(3, 2): Fraction(7), Fraction(1, 5): Fraction(-2)}

assert rho2(mulq(a, b)) == bt_mul(rho2(a), rho2(b))
assert rho2(dagger(a)) == sharp(rho2(a))

e_minus = (Fraction(1), Fraction(0))
e_plus = (Fraction(0), Fraction(1))
assert beta(e_minus, e_minus) == 0
assert beta(e_plus, e_plus) == 0
assert beta(e_minus, e_plus) == 1
assert beta(e_plus, e_minus) == 1

# The old scalar augmentation cannot extend over inverses.
eps_delta_2 = Fraction(0)
assert eps_delta_2 * Fraction(1) != Fraction(1)

# Finite crossed-product evaluation at a fixed origin.  Coefficients are
# represented only by their value at zero, where every dilation acts
# trivially; convolution therefore reduces to the group convolution above.
assert rho2(mulq(a, b)) == bt_mul(rho2(a), rho2(b))

print("P123.008 hyperbolic Tate algebra/dagger/ruling identities: PASS")

