#!/usr/bin/env python3
"""Finite exact regression model for P123.007.

This checks the formal identities used to prove that the radical of a
star-real convolution trace is a dagger ideal.  It is a regression
certificate, not evidence for the infinite-dimensional trace theorem.
"""

from fractions import Fraction


N = 8


def conv(a, b):
    return [sum(a[j] * b[(i - j) % N] for j in range(N)) for i in range(N)]


def dagger(a):
    # Coefficients are rational in this exact model, so conjugation is idle.
    return [a[(-i) % N] for i in range(N)]


# A star-real trace functional on Q[Z/N].  Choosing Fourier mode zero gives
# a nontrivial radical: T(a)=sum a_i and I(a,b)=T(a)T(b).
def trace(a):
    return sum(a)


def pairing(a, b):
    return trace(conv(a, dagger(b)))


e = [[Fraction(int(i == j)) for i in range(N)] for j in range(N)]
a = [Fraction(i * i - 3 * i + 1, 7) for i in range(N)]
f = [Fraction(1), Fraction(-1)] + [Fraction(0)] * (N - 2)
g = [Fraction((-1) ** i * (i + 2), 5) for i in range(N)]

assert dagger(dagger(a)) == a
assert dagger(conv(a, g)) == conv(dagger(g), dagger(a))
assert trace(dagger(a)) == trace(a)
assert pairing(a, g) == pairing(g, a)

# f belongs to the numerical radical because its augmentation is zero.
assert trace(f) == 0
assert all(pairing(f, basis) == 0 for basis in e)
assert all(pairing(conv(a, f), basis) == 0 for basis in e)
assert all(pairing(dagger(f), basis) == 0 for basis in e)

# The quotient is nonzero: the unit class has nonzero pairing.
assert pairing(e[0], e[0]) == 1

print("P123.007 finite radical/ideal/dagger identities: PASS")

