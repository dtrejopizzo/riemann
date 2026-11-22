#!/usr/bin/env python3
"""Ball-arithmetic certificate of lambda_n > 0 for 1 <= n <= 150.

Normalisation: lambda_n = (1/(n-1)!) d^n/ds^n [s^(n-1) log xi(s)] at s = 1, so that
    log( xi(1/(1-z)) / xi(1) ) = sum_{n>=1} (lambda_n / n) z^n,    lambda_1 = 0.0230957...
By xi(s) = xi(1-s) one has xi(1/(1-z)) = xi(w) with w = -z/(1-z), and near w = 0
    xi(w) = (w-1) pi^(-w/2) Gamma(1+w/2) zeta(w),
which has no pole. The script computes the Taylor series of log(xi(w)/xi(0)) in w with
Arb ball arithmetic (python-flint: arb_series.gamma, arb_series.zeta, arb_series.log are
rigorous enclosures), composes it with w = -z/(1-z) by Horner's rule in ball arithmetic,
and checks that the lower endpoint of every ball n*[z^n] is strictly positive.

Requires python-flint (tested with 0.9.0). Runs in a few seconds.
"""

from flint import arb, arb_series as S, ctx

N = 150
ctx.prec = 3000
ctx.cap = N + 1

w = S([0, 1])
xi = (w - 1) * S.exp(-w / 2 * arb.pi().log()) * S.gamma(1 + w / 2) * S.zeta(w)
L = S.log(xi / xi.coeffs()[0]).coeffs()

g = S([0, -1]) * S([1] * (N + 1))  # w = -z/(1-z)
res = S([L[N]])
for k in range(N - 1, -1, -1):
    res = res * g + L[k]
c = res.coeffs()

lam = [n * c[n] for n in range(1, N + 1)]
for n, x in enumerate(lam, 1):
    assert x.lower() > 0, n
    if n <= 3 or n % 25 == 0:
        print(f"lambda_{n} in {x.str(15, radius=True)}")
print(f"certified: lambda_n > 0 for 1 <= n <= {N}; max radius {max(x.rad() for x in lam).str(3)}")
