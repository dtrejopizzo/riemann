#!/usr/bin/env python3
"""r8d: explicit unconditional upper bound on lambda^A(T) (Theorem 1 of R155_055).

Test function F = (D^2 - 1/4)(D^2 + g1^2) G,  G(t) = phi_k(t/T),  phi_k = k-fold convolution of the
box (k/2)1_{[-1/k,1/k]};  hat phi_k(x) = sinc(x/k)^k.

Parts:
 (A) constants and the counting-function reduction  N(t) <= (t/2pi) log t  (t >= 21) from Rosser 1941;
 (B) the PROVED bound B(T,k) (eq. (3.1) of the memo), min over k, at the requested windows;
 (C) the closed-form Corollary envelope 4e9 * T * exp(-15.449 T) checked against min_k B(T,k) on [1,40];
 (D) DIAGNOSTIC: exact ratio a_T(F)/||F||^2 by quadrature of the symbol (m and the comb only, no zeros),
     compared with the PROVED bound and (cross-check of the explicit formula normalisation only)
     with the zero sum over the first 60 zeros from mpmath.zetazero (NOT an import of record).
Runtime ~ 13 s.
"""
import time, json, math
import numpy as np
from scipy.special import digamma
from numpy.polynomial.legendre import leggauss

t0 = time.time()
G1 = 14.134725141734693790          # import (X19), Paper 46
H0 = 3.0e12                          # Platt-Trudgian height, import (X19)
LOG_PI = math.log(math.pi)
C0 = -5.3721834                      # psi(1/4) - log pi, Paper 47 lem:K
TAU_GAP = 21.0                       # no zero ordinate in (g1, 21], import (X19)

# ---------- (A) constants ----------
def rosser_upper(t):   # Rosser 1941 Thm 19 (t >= 2): N(t) <= (t/2pi)log(t/2pi e) + 7/8 + 0.137 log t + 0.443 loglog t + 1.588
    return t/(2*math.pi)*math.log(t/(2*math.pi*math.e)) + 7/8 + 0.137*math.log(t) + 0.443*math.log(math.log(t)) + 1.588
def trudgian_upper(t): # Trudgian 2014 Thm 1 (t >= e): ... + 0.112 log t + 0.278 loglog t + 2.510
    return t/(2*math.pi)*math.log(t/(2*math.pi*math.e)) + 7/8 + 0.112*math.log(t) + 0.278*math.log(math.log(t)) + 2.510
A = {}
A['g1^4 >= 14.13^4'] = 14.13**4
A['21^9'] = 21.0**9
A['rosser(21)'] = rosser_upper(21.0)
A['trudgian(21)'] = trudgian_upper(21.0)
A['(21/2pi)log21'] = 21/(2*math.pi)*math.log(21)
# slack (t/2pi) log t - rosser_upper(t) must be >= 0 for t >= 21 (bracket 0.137 log t + 0.443 loglog t + 2.463 - 0.4517 t <= 0)
ts = np.linspace(21, 1e6, 200001)
br = 0.137*np.log(ts) + 0.443*np.log(np.log(ts)) + 7/8 + 1.588 - (math.log(2*math.pi)+1)/(2*math.pi)*ts
A['max Rosser bracket on [21,1e6] (= -slack at 21)'] = float(br.max())
A['slack at 21, Rosser'] = 21/(2*math.pi)*math.log(21) - rosser_upper(21.0)
A['slack at 21, Trudgian'] = 21/(2*math.pi)*math.log(21) - trudgian_upper(21.0)
A['(log 2pi +1)/2pi'] = (math.log(2*math.pi)+1)/(2*math.pi)
print("(A) constants:", json.dumps(A, indent=1))

# ---------- (B) the PROVED bound ----------
def S(H, p):        # Sum_{gamma > H} gamma^{-p} <= (p/2pi) H^{1-p} [ log H/(p-1) + 1/(p-1)^2 ],  p >= 2
    return p/(2*math.pi) * H**(1-p) * (math.log(H)/(p-1) + 1/(p-1)**2)
def eps_k(k, Y):    # (1/2pi) int_{|x|>Y} |hat phi_k|^2 <= (1/pi) k^{2k} Y^{1-2k}/(2k-1)
    le = 2*k*math.log(k/Y) + math.log(Y/(2*k-1)/math.pi)
    return math.exp(le) if le < 700 else math.inf
def B(T, k):
    p = 2*k - 8
    Y = T*G1/math.sqrt(2)
    e = eps_k(k, Y)
    if e >= 0.5: return math.inf
    # log-space: (k/T)^{2k} S(H,p) = (k/(T H))^{2k} H^9   [fixed per TEX_HOSTILE_REVIEW_R4 R4-1: was H^8] (p/2pi)[log H/(p-1)+1/(p-1)^2]
    def lterm(H):
        return 2*k*math.log(k/(T*H)) + 9*math.log(H) + math.log(p/(2*math.pi)*(math.log(H)/(p-1)+1/(p-1)**2))
    l1 = lterm(TAU_GAP); l2 = lterm(H0) + T
    lnum = math.log(2*1.0012*T**2) + l1 + math.log1p(math.exp(l2-l1))
    lden = math.log((14.13**4 * T/64) * (0.5 - e))
    return math.exp(lnum-lden) if lnum-lden < 700 else math.inf
def best(T, kmax=None):
    if kmax is None: kmax = int(12*T)+30
    vals = [(B(T,k), k) for k in range(5, kmax)]
    return min(vals)
Ts = [0.5*math.log(3), math.log(2), 0.80, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 10.0]
print("\n(B) PROVED bound  min_k B(T,k):")
rows = []
for T in Ts:
    b, k = best(T)
    kstar = 21*T/math.e
    rows.append((T, k, b))
    print(f"  T={T:7.4f}  k_opt={k:3d}  (21T/e={kstar:6.2f})  bound={b:.3e}")
# crossings
def cross(level):
    lo, hi = 0.6, 6.0
    for _ in range(60):
        mid = (lo+hi)/2
        if best(mid)[0] > level: lo = mid
        else: hi = mid
    return hi
for lev in [1.0, 8.8577e-5, 1e-7]:
    print(f"  bound = {lev:.3e} at T = {cross(lev):.3f}")

# ---------- (C) Corollary envelope ----------
worst = -math.inf
for T in np.linspace(1.0, 40.0, 391):
    b, k = best(float(T))
    env = 4e9 * T * math.exp(-15.449*T)
    worst = max(worst, b/env)
# Corollary 1 ingredients with k = ceil(21T/e): sup of eps_k over T>=1, and (2k-8)/(2k-9)[log21+1/(2k-9)]/(2pi) <= 0.5797
sup_eps = max(eps_k(math.ceil(21*T/math.e), T*G1/math.sqrt(2)) for T in np.linspace(1.0, 40.0, 39001))
# exact interval endpoints T_k = (k-1)e/21 (k >= 9) plus T = 1 (k = 8); eps decreases in T at fixed k
ends = [(8, 1.0)] + [(k, (k-1)*math.e/21) for k in range(9, 400)]
eps_end = max(eps_k(k, T*G1/math.sqrt(2)) for k, T in ends)
print(f"\n(C) sup_(T>=1) eps_k(Y) with k=ceil(21T/e): grid {sup_eps:.5f}, at interval endpoints {eps_end:.5f} (k=9, T=8e/21; memo uses <= 0.0157);  "
      f"const check: 2*1.0012*0.5797*21^9*e^0.259/(14.13^4/64*0.484) = {2*1.0012*0.5797*21.0**9*math.exp(0.259)/(14.13**4/64*0.484):.3e}  (0.5-0.01566 = {0.5-0.01566:.5f} >= 0.484)")
print(f"(C) max over T in [1,40] of  min_k B(T,k) / (4e9 T e^(-15.449 T))  = {worst:.4f}  (must be <= 1)")

# ---------- (D) DIAGNOSTIC exact ratio ----------
def m_sym(tau):
    return digamma(0.25 + 0.5j*tau).real - LOG_PI
def contacts(T):
    out = []
    N = int(math.exp(2*T)) + 2
    for n in range(2, N):
        if math.log(n) >= 2*T: continue
        # Lambda(n)
        p, q = None, n
        for d in range(2, int(n**0.5)+1):
            if n % d == 0:
                p = d; break
        if p is None: p = n
        while q % p == 0: q //= p
        if q == 1: out.append((n, 2*math.log(p)/math.sqrt(n)))
    return out
def Fhat2(tau, T, k):
    x = T*tau/k
    s = np.where(np.abs(x) < 1e-12, 1.0, np.sin(x)/np.where(np.abs(x)<1e-12, 1.0, x))
    return (tau**2+0.25)**2 * (tau**2-G1**2)**2 * T**2 * s**(2*k)
def ratio_quad(T, k, tau_max=4000.0, h=0.25, ng=24):
    xg, wg = leggauss(ng)
    edges = np.arange(0.0, tau_max+h/2, h)
    a, b = edges[:-1], edges[1:]
    tau = (0.5*(b-a)[:,None]*xg[None,:] + 0.5*(a+b)[:,None]).ravel()
    w = (0.5*(b-a)[:,None]*wg[None,:]).ravel()
    con = contacts(T)
    comb = np.zeros_like(tau)
    for n, v in con: comb += v*np.cos(tau*math.log(n))
    sig = m_sym(tau) - comb
    f2 = Fhat2(tau, T, k)
    AT = sum(v for _, v in con)
    aF = 2*np.sum(w*sig*f2)/(2*math.pi)
    nF = 2*np.sum(w*f2)/(2*math.pi)
    # tails beyond tau_max: |Fhat|^2 <= 1.0012 tau^8 T^2 (k/(T tau))^{2k};  |sigma| <= log tau + A_T
    p = 2*k-8
    tail_n = 2*1.0012*T**2*(k/T)**(2*k) * tau_max**(1-p)/(p-1) /(2*math.pi)
    tail_a = tail_n*(math.log(tau_max)+1+AT)
    return aF, nF, tail_a, tail_n, AT
print("\n(D) DIAGNOSTIC: exact ratio of the test function (symbol quadrature; no zeros) vs PROVED bound")
diag = []
for T in [0.5*math.log(3), math.log(2), 0.8, 1.0, 1.5, 2.0]:
    b, k = best(T)
    aF, nF, ta, tn, AT = ratio_quad(T, k)
    r = aF/nF
    diag.append((T, k, r, b))
    print(f"  T={T:6.4f} k={k:2d}  a_T(F)/||F||^2 = {r:.6e}   (tail err <= {ta/nF:.1e})  PROVED bound {b:.3e}  A_T={AT:.4f}")
# cross-check of the explicit-formula normalisation with mpmath zeros (DIAGNOSTIC ONLY)
try:
    import mpmath as mp
    mp.mp.dps = 20
    zs = [float(mp.zetazero(n).imag) for n in range(1, 61)]
    print("\n    zero-sum cross-check (first 60 zeros, mpmath.zetazero; DIAGNOSTIC, not an import):")
    for T in [1.0, 1.5, 2.0]:
        b, k = best(T)
        aF, nF, ta, tn, AT = ratio_quad(T, k)
        zsum = 2*sum(float(Fhat2(np.array([g]), T, k)[0]) for g in zs)
        p = 2*k-8
        ztail = 2*1.0012*T**2*(k/T)**(2*k)*S(zs[-1], p)
        print(f"    T={T}: symbol integral a_T(F) = {aF:.6e};  Sum_rho |F^(gamma)|^2 (60 zeros) = {zsum:.6e}  (+ tail <= {ztail:.1e});  rel diff {(aF-zsum)/aF:.2e}")
except Exception as ex:
    print("   mpmath cross-check skipped:", ex)
print(f"\nruntime {time.time()-t0:.1f} s")
json.dump({'A':A,'B':rows,'C_worst_ratio':worst,'D':diag}, open(__file__.replace('.py','.json'),'w'), indent=1)
