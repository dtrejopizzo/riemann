#!/usr/bin/env python3
"""High-precision audit of the explicit D.59 endpoint gap.

This reproduces the finite root brackets and spectral lower bounds.  The
proof note explains how the same finite computation is converted into
directed rational interval arithmetic.
"""

import mpmath as mp


mp.mp.dps = 100
T = mp.log(2) / 2
m0 = mp.log(mp.pi) - mp.digamma(mp.mpf(1) / 4)


def bisect_root(fun, left, right, iterations=420):
    """Bisect a continuous sign-changing branch without crossing a pole."""
    fl = fun(left)
    fr = fun(right)
    assert fl * fr < 0
    for _ in range(iterations):
        middle = (left + right) / 2
        fm = fun(middle)
        if fl * fm <= 0:
            right, fr = middle, fm
        else:
            left, fl = middle, fm
    return (left + right) / 2


def odd_root(b):
    eps = mp.mpf("1e-80")
    return bisect_root(
        lambda x: x / mp.tan(x) + b * T,
        mp.pi / 2 + eps,
        mp.pi - eps,
    )


def even_root_0(b):
    eps = mp.mpf("1e-80")
    return bisect_root(
        lambda x: x * mp.tan(x) - b * T,
        eps,
        mp.pi / 2 - eps,
    )


def even_root_1(b):
    eps = mp.mpf("1e-80")
    return bisect_root(
        lambda x: x * mp.tan(x) - b * T,
        mp.pi + eps,
        3 * mp.pi / 2 - eps,
    )


def kernel_eigenvalue(b, x):
    mu = x / T
    return 2 * b / (b * b + mu * mu)


odd_terms = []
for j in range(20):
    b = 2 * j + mp.mpf(1) / 2
    x = odd_root(b)
    lam = kernel_eigenvalue(b, x)
    odd_terms.append(2 / b - lam)

odd_sum = mp.fsum(odd_terms)
odd_gap = odd_sum - m0


def even_compressed_term(j):
    b = 2 * j + mp.mpf(1) / 2
    x0 = even_root_0(b)
    x1 = even_root_1(b)
    mu0 = x0 / T
    lam0 = kernel_eigenvalue(b, x0)
    lam1 = kernel_eigenvalue(b, x1)

    norm_h_sq = T + mp.sinh(T)
    norm_cos_sq = T + mp.sin(2 * mu0 * T) / (2 * mu0)
    inner = (
        2
        * (
            mp.mpf(1) / 2 * mp.sinh(T / 2) * mp.cos(mu0 * T)
            + mu0 * mp.cosh(T / 2) * mp.sin(mu0 * T)
        )
        / (mu0 * mu0 + mp.mpf(1) / 4)
    )
    r_sq = inner * inner / (norm_h_sq * norm_cos_sq)
    assert 0 < r_sq < 1
    compressed_upper = lam1 + (lam0 - lam1) * (1 - r_sq)
    return 2 / b - compressed_upper, r_sq, x0, x1


even_data = [even_compressed_term(j) for j in range(5)]
even_sum = mp.fsum(row[0] for row in even_data)
even_gap = even_sum - m0

# The endpoint p=2 shift is 2T=log 2.  The intersection of the translated
# support intervals has Lebesgue length max(0, 2T-log 2)=0.
overlap_length = max(mp.mpf(0), 2 * T - mp.log(2))

assert mp.mpf("5.41313") < odd_sum
assert mp.mpf("0.040946") < odd_gap
assert mp.mpf("5.45749") < even_sum
assert mp.mpf("0.085306") < even_gap
assert m0 < mp.mpf("5.372184")
assert overlap_length == 0

print(f"PASS T2={mp.nstr(T, 30)}")
print(f"PASS m0={mp.nstr(m0, 30)} < 5.372184")
print(
    "PASS odd first-20 sum="
    f"{mp.nstr(odd_sum, 30)}, gap={mp.nstr(odd_gap, 30)}"
)
print(
    "PASS even first-5 compressed sum="
    f"{mp.nstr(even_sum, 30)}, gap={mp.nstr(even_gap, 30)}"
)
print("PASS p=2 endpoint translated-support overlap has measure zero")

