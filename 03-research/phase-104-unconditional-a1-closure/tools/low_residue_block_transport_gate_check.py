#!/usr/bin/env python3
"""Exact checks for 104_109 (rational arithmetic only)."""

from fractions import Fraction as F


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def sub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def inv(z):
    d = z[0] * z[0] + z[1] * z[1]
    return (z[0] / d, -z[1] / d)


def div(z, w):
    return mul(z, inv(w))


def scale(a, z):
    return (a * z[0], a * z[1])


def power(z, n):
    out = (F(1), F(0))
    base = z
    while n:
        if n & 1:
            out = mul(out, base)
        base = mul(base, base)
        n >>= 1
    return out


def norm2(z):
    return z[0] * z[0] + z[1] * z[1]


zero = (F(0), F(0))
one = (F(1), F(0))
w = (F(0), F(4, 5))
winv = inv(w)
rho = inv(sub(one, w))

assert rho == (F(25, 41), F(20, 41))
assert rho[0] > F(1, 2)
assert norm2(w) == F(16, 25)

# The a=4 Cayley image and the two negative-binomial transfer bases.
z4 = sub(scale(F(4), w), (F(3), F(0)))
tau_w = div(w, sub((F(4), F(0)), scale(F(3), w)))
tau_winv = div(winv, sub((F(4), F(0)), scale(F(3), winv)))
assert z4 == (F(-3), F(16, 5))
assert norm2(z4) == F(481, 25) > 1
assert norm2(tau_w) == F(1, 34)
assert norm2(tau_winv) == F(25, 481)
assert tau_winv == inv(z4)


def quartet_li(n):
    """q_n=4-2 Re(w^n+w^{-n})."""
    return F(4) - 2 * (power(w, n)[0] + power(winv, n)[0])


def transformed_B(n):
    """T_4(-q)_n=-4+2 Re(tau(w)^n+tau(w^-1)^n)."""
    return -F(4) + 2 * (power(tau_w, n)[0] + power(tau_winv, n)[0])


# Positive and negative exponential residue classes, and the strong Euler-side
# first-moment bound for the transformed synthetic defect.
for n in range(2, 202):
    if n % 4 == 2:
        assert quartet_li(n) > 2 * F(5, 4) ** n
    if n % 4 == 0:
        assert quartet_li(n) < 0
    assert abs(transformed_B(n)) <= 3 * n

# Every four consecutive degrees contain a positive exponential excursion.
for start in range(2, 202):
    vals = [quartet_li(n) for n in range(start, start + 4)]
    assert any(n % 4 == 2 and quartet_li(n) > 0
               for n in range(start, start + 4))

# Nevertheless there are arbitrarily long far-out blocks with negative linear
# average.  K is increased until the exact rational sum becomes negative.
for M in range(1, 31):
    found = False
    for K in range(0, 4 * M + 20):
        total = sum((quartet_li(n)
                     for n in range(4 * K + 1, 4 * K + 4 * M + 1)), F(0))
        if total < 0:
            found = True
            break
    assert found

print("PASS low-residue block transport gate")
print("rho =", rho, "|w|^2 =", norm2(w), "|z_4|^2 =", norm2(z4))
print("transfer norms^2 =", norm2(tau_w), norm2(tau_winv))
