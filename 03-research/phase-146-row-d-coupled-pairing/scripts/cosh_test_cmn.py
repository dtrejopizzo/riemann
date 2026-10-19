#!/usr/bin/env python3
"""R146 / D.45.2 -- the cosh test (Lemma D.31.4) on the would-be sum classes c_{m,n},
plus the D.44.1 rank-2 would-be norm form and the D.45.1 indefiniteness witness.

Objects (all defined in R146_001_ROUND1.md):
  L(m,n)   = min(m,n)*Lambda(max/min)   if max/min is a prime power, else 0   (un-normalized
             off-diagonal Gram entry of Paper 44 Thm 8bis.1 = "deg(Frob_m - Frob_n)")
  G(m,n)   = (m + n - L(m,n))/2         (the would-be trace pairing)
  c_{m,n}  = E_m + E_n - F_2 + 2 G(m,n) F_1     (the would-be class of Gamma_{Frob_m+Frob_n})
  deg c    = 2(m+n) + 1 - L(m,n),   Phi_c(rho_1) = m^{rho_1} + n^{rho_1}
             (F_1, F_2 have Phi = 0 at every zero: R140 D.23.7 / Paper 46 Thm 11.8)
Test:  margin(m,n) = max_theta [ |Re(e^{i theta} Phi_c(rho_1))| - (1/2) s(gamma_1,theta) deg c ].
       margin > 0  ==>  c_{m,n} is NOT >= 0 in D^W (cannot be effective).
Usage: python3 cosh_test_cmn.py [--fast]
"""
import sys, math, cmath

FAST = "--fast" in sys.argv
GAMMA1 = 14.134725141734693790457251983562470270784257115699243175685567460149963429809256764949010
SPRIME = 3.0

def s_of_theta(gamma, theta, n=200001, U=40.0):
    """s(gamma,theta) = sup_u |cos(gamma u + theta)| / cosh(u/2)."""
    best = 0.0
    for i in range(n):
        u = -U + 2*U*i/(n-1)
        v = abs(math.cos(gamma*u + theta))/math.cosh(u/2)
        if v > best: best = v
    return best

def Lambda(x):
    """von Mangoldt at a positive rational x: log p if x = p^k (k>=1), else 0."""
    if x <= 1: return 0.0
    if abs(x - round(x)) > 1e-12: return 0.0
    m = int(round(x))
    p = 2
    while p*p <= m:
        if m % p == 0:
            while m % p == 0: m //= p
            return math.log(p) if m == 1 else 0.0
        p += 1
    return math.log(m)

def L(m, n):
    if m == n: return 0.0                      # diagonal counterterm delta = 0 (model g=1 convention)
    lo, hi = min(m, n), max(m, n)
    return lo * Lambda(hi/lo)

def G(m, n): return 0.5*(m + n - L(m, n))

NTH = 721 if FAST else 36001
THETAS = [2*math.pi*j/NTH for j in range(NTH)]
SCACHE = {}
def s_theta(th):
    key = round(th, 9)
    if key not in SCACHE:
        SCACHE[key] = s_of_theta(GAMMA1, th, n=(20001 if FAST else 200001))
    return SCACHE[key]

def margin(m, n):
    rho = complex(0.5, GAMMA1)
    Phi = cmath.exp(rho*math.log(m)) + cmath.exp(rho*math.log(n))
    deg = 2*(m+n) + 1 - L(m, n)
    best, bt = -1e300, 0.0
    for th in THETAS:
        val = abs((cmath.exp(1j*th)*Phi).real) - 0.5*s_theta(th)*deg
        if val > best: best, bt = val, th
    return best, bt, abs(Phi), deg

print("=== [1] D.45.2  cosh test on c_{m,n}  (margin > 0 would refute effectivity) ===")
print(f"{'(m,n)':>10} {'|Phi(rho1)|':>12} {'deg c':>10} {'2G':>10} {'margin':>14} {'theta*':>8}")
pairs = [(1,1),(1,2),(2,3),(1,3),(1,5),(1,7),(2,4),(3,9),(1,101),(6,10),(2,2),(5,5)]
if not FAST: pairs += [(1,1024),(1000,1001)]
for (m,n) in pairs:
    mg, th, aP, dg = margin(m,n)
    print(f"{str((m,n)):>10} {aP:12.6f} {dg:10.3f} {2*G(m,n):10.3f} {mg:14.6f} {th:8.4f}")

print()
print("=== [2] D.44.1  the rank-2 would-be norm form  Q(m,n) = m^2 + a_l m n + l n^2 ===")
print("      a_l = l + 1 - Lambda(l)   (the arithmetic 'trace'); Hasse test a_l^2 <= 4l")
print(f"{'l':>6} {'Lambda(l)':>10} {'a_l':>12} {'a_l^2':>14} {'4l':>10} {'Hasse?':>8} {'g >= a/(2sqrt l)':>18}")
for l in [2,3,4,5,7,8,9,11,13,16,17,19,23,29,31,101,1009]:
    lam = Lambda(l)
    a = l + 1 - lam
    ok = "PASS" if a*a <= 4*l else "FAIL"
    print(f"{l:>6} {lam:10.5f} {a:12.5f} {a*a:14.4f} {4*l:10d} {ok:>8} {a/(2*math.sqrt(l)):18.4f}")

print()
print("=== [3] D.45.1  indefiniteness witness for the would-be degree form Q on M ===")
print("      Q(x) = (sum a_n)(sum a_n n) - (1/2) x^T L x,  delta = 0")
def Q(coeffs):
    ns = list(coeffs.keys())
    A = sum(coeffs.values())
    B = sum(a*n for n, a in coeffs.items())
    xLx = sum(coeffs[m]*coeffs[n]*L(m, n) for m in ns for n in ns)
    return A*B - 0.5*xLx
for w in [{6:5,10:-4}, {6:1,10:-1}, {6:5,10:-4,1:0}, {1:1,2:-1}, {1:1,2:1}, {15:7,22:-5}]:
    print(f"   x = {w}   Q = {Q(w):.6f}")
print()
print("   scan over pairs (m,n), m<n<=60, coefficients |a|,|b| <= 12, for min Q:")
best = (1e300, None)
for m in range(1,61):
    for n in range(m+1,61):
        for a in range(-12,13):
            for b in range(-12,13):
                if a == 0 and b == 0: continue
                v = Q({m:a, n:b})
                if v < best[0]: best = (v, (m,n,a,b))
print(f"   min Q = {best[0]:.6f} at (m,n,a,b) = {best[1]}")
