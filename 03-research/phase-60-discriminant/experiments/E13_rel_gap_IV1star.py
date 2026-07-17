#!/usr/bin/env python3
# ======================================================================================
# IV.1*  — UNIFORM RELATIVE SPECTRAL GAP   ε_1(λ)/ε_0(λ) >= 1+gamma, gamma>0, uniform in λ.
# Reuses the validated engine (q_func, QW_entry, spec) from E11_relspec_prolate.py.
# Measures ε_0, ε_1, ε_2, gap ratio across λ in {3..12} at high mpmath precision.
# Also tracks N-convergence (finite-section stability of the ratio).
# ======================================================================================
import mpmath as mp
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m, n, L, lam):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx: arith += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return W02-WR-arith

def spec(lam, N):
    L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1)); M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a, b] = v; M[b, a] = v
    E, _ = mp.eigsy(M); return sorted([E[i] for i in range(dim)])

print("="*78)
print(" E13: UNIFORM RELATIVE GAP  ε_1/ε_0  (IV.1* lynchpin)")
print("="*78, flush=True)
print(f"{'λ':>5} {'N':>3} {'ε_0':>14} {'ε_1':>14} {'ε_1/ε_0':>12} {'ε_2/ε_0':>12}", flush=True)
results = {}
for lamstr in ['3.0','4.0','5.0','6.0','7.0','8.0','9.0','10.0','11.0','12.0']:
    lam = mp.mpf(lamstr); N = 16
    e = spec(lam, N); e0 = e[0]; e1 = e[1]; e2 = e[2]
    r1 = e1/e0; r2 = e2/e0
    results[lamstr] = (e0, e1, r1, r2)
    print(f"{lamstr:>5} {N:>3} {mp.nstr(e0,5):>14} {mp.nstr(e1,5):>14} {mp.nstr(r1,8):>12} {mp.nstr(r2,8):>12}", flush=True)

print("\n--- N-convergence of ε_1/ε_0 at fixed λ (finite-section stability) ---", flush=True)
for lamstr in ['7.0','9.0']:
    lam = mp.mpf(lamstr)
    print(f" λ={lamstr}:", flush=True)
    for N in [8, 12, 16, 20, 24]:
        e = spec(lam, N); r1 = e[1]/e[0]
        print(f"   N={N:>2}: ε_1/ε_0 = {mp.nstr(r1,10)}", flush=True)

print("\n--- min over measured λ of (ε_1/ε_0) ---", flush=True)
mn = min(results[k][2] for k in results)
print(f"  min ε_1/ε_0 over λ∈[3,12] = {mp.nstr(mn,10)}  ->  γ_emp = {mp.nstr(mn-1,10)}", flush=True)
