"""PROVED-check (exact rationals): Z_Q/2 = (zeta_K + L_psi)/2 = sqrt(zeta_K L_psi) cosh(y), y = (1/2)log(L_psi/zeta_K)
 = -sum_{p in Ncal} e_p sum_{k odd} p^{-ks}/k  (Ncal = primes whose prime ideals are non-principal; e_2=1, e_p=2 split).
Hence Lambda_Q = (Lambda_K + Lambda_psi)/2 + Lambda_cosh, Lambda_cosh(n) = log n * [coeff of n^-s in log cosh y].
Verified against the recursion of epstein_coeffs.py for n<=N."""
import math, sympy, sys
from fractions import Fraction as Fr
from sympy import factorint
from math import isqrt
import cert_epstein as C
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
def psi_p(p):
    if p == 2: return -1
    if p == 5: return 1
    if sympy.jacobi_symbol(-20 % p, p) != 1: return None
    return 1 if any(isqrt(p - 5 * y * y) ** 2 == p - 5 * y * y for y in range(isqrt(p // 5) + 1)) else -1
Ncal = [p for p in sympy.primerange(2, N + 1) if psi_p(p) == -1]
y = {}
for p in Ncal:
    e = 1 if p == 2 else 2; k = 1
    while p ** k <= N: y[p ** k] = y.get(p ** k, 0) - Fr(e, k); k += 2
def mul(a, b):
    c = {}
    for m, x in a.items():
        for n, z in b.items():
            if m * n <= N: c[m * n] = c.get(m * n, 0) + x * z
    return c
y2 = mul(y, y); y4 = mul(y2, y2); y6 = mul(y4, y2); y8 = mul(y4, y4)
lc = {}
for d, c in ((y2, Fr(1, 2)), (y4, Fr(-1, 12)), (y6, Fr(1, 45)), (y8, Fr(-17, 2520))):
    for n, x in d.items(): lc[n] = lc.get(n, 0) + c * x
K = C._LK(N)
def chi(D, n):
    if D == -4: return 0 if n % 2 == 0 else (1 if n % 4 == 1 else -1)
    return 0 if n % 5 == 0 else sympy.jacobi_symbol(n, 5)
bad = 0
for n in range(2, N + 1):
    f = factorint(n); lk = lp = 0
    if len(f) == 1:
        p, k = list(f.items())[0]; lk = float(sum(K.get(n, {}).values())) * math.log(p); lp = (chi(-4, p) ** k + chi(5, p) ** k) * math.log(p)
    pred = (lk + lp) / 2 + float(lc.get(n, 0)) * math.log(n)
    act = sum(float(q) * math.log(p) for p, q in C.LQ.get(n, {}).items())
    if abs(pred - act) > 1e-9: bad += 1; print('mismatch', n, pred, act)
print('Lambda_Q = (Lambda_K+Lambda_psi)/2 + Lambda_cosh, n<=%d, mismatches:' % N, bad)
print('Ncal (non-principal prime ideals) primes <= %d:' % N, Ncal)
print('Lambda_cosh(n) != 0, n<=200 (n: value, Omega_Ncal(n)):')
for n, v in sorted(lc.items()):
    if v != 0: print(n, round(float(v) * math.log(n), 4), sum(e for p, e in factorint(n).items() if p in Ncal))
