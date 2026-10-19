"""LEMMA_E_EPSTEIN_001: exact coefficients of Z_Q, Q=x^2+5y^2.
r_Q(n) = #{(x,y): x^2+5y^2=n}; a(n)=r_Q(n)/2 (Z_Q/2 = 1+...). Lambda_Q(n) defined by -(Z_Q/2)'/(Z_Q/2)=sum Lambda_Q(n) n^-s,
recursion a(n) log n = sum_{d|n} a(d) Lambda_Q(n/d). Lambda_Q(n) is stored EXACTLY as {p: rational} (sum q_p log p).
Checks r_Q = (1*chi_-20) + (chi_-4 * chi_5) (Dirichlet convolutions)  [Z_Q = zeta L(chi_-20) + L(chi_-4) L(chi_5)]."""
from fractions import Fraction as Fr
from math import isqrt
import json, sys
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
def rQ(n):
    c = 0
    for y in range(-isqrt(n // 5), isqrt(n // 5) + 1):
        r = n - 5 * y * y; x = isqrt(r)
        if x * x == r: c += 1 if x == 0 else 2
    return c
def kron(D, n):  # Kronecker symbol (D/n), D fundamental discriminant
    from sympy import jacobi_symbol
    from sympy.ntheory import factorint
    res = 1
    for p, e in factorint(n).items():
        if p == 2:
            if D % 2 == 0: return 0
            v = 1 if D % 8 in (1, 7) else -1
        else:
            v = jacobi_symbol(D % p, p) if D % p else 0
        res *= v ** e
    return res
def conv(f, g, n): return sum(f(d) * g(n // d) for d in range(1, n + 1) if n % d == 0)
ok = all(rQ(n) == conv(lambda d: 1, lambda m: kron(-20, m), n) + conv(lambda d: kron(-4, d), lambda m: kron(5, m), n)
         for n in range(1, N + 1))
from sympy import factorint
def logvec(n): return {p: Fr(e) for p, e in factorint(n).items()}
def add(u, v, c):
    w = dict(u)
    for p, q in v.items(): w[p] = w.get(p, 0) + c * q
    return {p: q for p, q in w.items() if q != 0}
a = {n: Fr(rQ(n), 2) for n in range(1, N + 1)}
Lam = {}
for n in range(2, N + 1):
    v = {p: a[n] * e for p, e in logvec(n).items()}
    for d in range(2, n):
        if n % d == 0 and a[d] != 0 and Lam.get(n // d): v = add(v, Lam[n // d], -a[d])
    Lam[n] = {p: q for p, q in v.items() if q != 0}
import math
val = {n: sum(float(q) * math.log(p) for p, q in Lam[n].items()) for n in Lam}
if __name__ == '__main__':
    print('identity r_Q = 1*chi_-20 + chi_-4*chi_5 for n<=%d:' % N, ok)
    print('n r_Q(n) Lambda_Q(n) [exact]  ~value   2Lambda(n) (zeta-K proxy: Lambda_zeta+chi Lambda_zeta)')
    for n in range(2, N + 1):
        if Lam[n]:
            print(n, rQ(n), {p: str(q) for p, q in Lam[n].items()}, '%.6f' % val[n])
    neg = [n for n in val if val[n] < -1e-12]
    print('NEGATIVE Lambda_Q(n), n<=%d:' % N, neg)
    json.dump({str(n): {str(p): str(q) for p, q in Lam[n].items()} for n in Lam if Lam[n]},
              open('lambdaQ_exact.json', 'w'), indent=0)
