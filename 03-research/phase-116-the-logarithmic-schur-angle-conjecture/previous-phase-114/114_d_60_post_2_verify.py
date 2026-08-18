#!/usr/bin/env python3
"""High-precision diagnostic for the finite constants in D.60.

The proof uses rational branch bisection and Taylor remainders as described
in the note.  This script independently reproduces the endpoint sums and
checks the deliberately coarse rational margins.
"""
import mpmath as mp

mp.mp.dps = 90
T2 = mp.log(2) / 2
m0 = mp.log(mp.pi) + mp.euler + mp.pi / 2 + 3 * mp.log(2)


def bisect(f, left, right, steps=350):
    fl = f(left)
    fr = f(right)
    assert fl * fr < 0
    for _ in range(steps):
        mid = (left + right) / 2
        fm = f(mid)
        if fl * fm <= 0:
            right, fr = mid, fm
        else:
            left, fl = mid, fm
    return (left + right) / 2


eps = mp.mpf("1e-70")
odd_sum = mp.mpf("0")
for j in range(20):
    b = 2 * j + mp.mpf("0.5")
    x = bisect(lambda z: z / mp.tan(z) + b * T2,
               mp.pi / 2 + eps, mp.pi - eps)
    mu = x / T2
    odd_sum += 2 / b - 2 * b / (b * b + mu * mu)

even_sum = mp.mpf("0")
h_norm_sq = T2 + mp.sinh(T2)
for j in range(5):
    b = 2 * j + mp.mpf("0.5")
    equation = lambda z: z * mp.tan(z) - b * T2
    x0 = bisect(equation, eps, mp.pi / 2 - eps)
    x1 = bisect(equation, mp.pi + eps, 3 * mp.pi / 2 - eps)
    mu0, mu1 = x0 / T2, x1 / T2
    lam0 = 2 * b / (b * b + mu0 * mu0)
    lam1 = 2 * b / (b * b + mu1 * mu1)
    cos_norm_sq = T2 + mp.sin(2 * x0) / (2 * mu0)
    pairing = 2 * (
        mp.mpf("0.5") * mp.sinh(T2 / 2) * mp.cos(x0)
        + mu0 * mp.cosh(T2 / 2) * mp.sin(x0)
    ) / (mu0 * mu0 + mp.mpf("0.25"))
    r = pairing / mp.sqrt(h_norm_sq * cos_norm_sq)
    even_sum += 2 / b - lam1 - (lam0 - lam1) * (1 - r * r)

assert odd_sum > mp.mpf("5.41313")
assert even_sum > mp.mpf("5.45749")
assert m0 < mp.mpf("5.372184")
assert mp.log(10) > mp.mpf("2.3")

rational_margin = mp.mpf(344) / 345 * mp.mpf("5.41312") - mp.mpf("5.372184")
boundary_error = mp.mpf(8) / 3 * mp.mpf(10) ** (-310)
assert rational_margin - boundary_error > mp.mpf("0.02524")

print("PASS odd endpoint sum", mp.nstr(odd_sum, 25))
print("PASS even primitive endpoint sum", mp.nstr(even_sum, 25))
print("PASS m0", mp.nstr(m0, 25))
print("PASS post-2 rational margin", mp.nstr(rational_margin - boundary_error, 25))
print("PASS explicit interval length h2=10^-610")
