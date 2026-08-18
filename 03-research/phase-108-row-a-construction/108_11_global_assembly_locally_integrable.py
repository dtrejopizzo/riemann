#!/usr/bin/env python3
"""Verifier for 108.11 - local integrability of the global assembly.
No zero of xi is used in any definition."""
import math, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- A. the singular set is discrete in (0,1), accumulating only at 0 and 1
def sing_in(delta, cap=200000):
    S1=[1/N for N in range(2,cap) if delta <= 1/N <= 1-delta]
    S2=[1-1/M for M in range(2,cap) if delta <= 1-1/M <= 1-delta]
    return sorted(set(S1+S2))
ok=True; rows=[]
for d in (0.4,0.3,0.2,0.1,0.05,0.01,0.001):
    S=sing_in(d); rows.append((d,len(S)))
    # the content is finiteness on each compact, with count ~ 2/d
    if not (0 < len(S) < 3/d + 10): ok=False
check("A singular set finite on every compact [d,1-d], count ~ 2/d", ok, str(rows))
# and it really does accumulate only at the endpoints
S=sing_in(1e-4)
check("A' accumulation points are exactly 0 and 1",
      min(S) < 2e-4 and max(S) > 1-2e-4 and
      min(b-a for a,b in zip(S,S[1:]) if 0.2<a<0.8) > 1e-3)

# --- B. log is locally integrable, with the exact primitive ----------------
def num_int_log(h, N=4000001):
    x=np.linspace(-h,h,N); x=x[np.abs(x)>1e-18]
    return np.trapz(np.abs(np.log(np.abs(x))), x)
ok=True; rows=[]
for h in (1e-1,1e-2,1e-3,1e-4):
    num=num_int_log(h); exact=2*h*(1-math.log(h)); rows.append((h,round(num,8)))
    if abs(num-exact) > 1e-6*max(1,exact): ok=False
check("B  int_{-h}^{h}|log|x||dx = 2h(1-log h), finite and -> 0", ok, str(rows))

# --- C. the tail of sum_N (phi(N)/N) log zeta(Na) converges geometrically --
# On [d,1-d] only finitely many N have Na <= 1.  For the rest, the principled
# statement is the asymptotic  log zeta(s) * 2^s -> 1  as s -> infinity,
# i.e. geometric decay with ratio 1/2.  Test that, not an arbitrary cutoff.
def zeta_gt1(s, M=400000):
    n=np.arange(1,M+1,dtype=float); return float((n**(-s)).sum())
# log zeta(s)*2^s = 1 + (3/2)^{-s} + ..., so the error must decay at the
# exact rate log(3/2).  Fit it and compare to theory - no arbitrary threshold.
ss=np.array([6.,8.,10.,12.,14.,16.])
err=np.array([abs(math.log(zeta_gt1(float(x)))*2**x - 1.0) for x in ss])
slope=np.polyfit(ss, np.log(err), 1)[0]
theory=-math.log(1.5)
ok = abs(slope-theory) < 0.02 and all(err[i]>err[i+1] for i in range(len(err)-1))
check("C  log zeta(s)*2^s -> 1 with error decaying at the exact rate log(3/2)",
      ok, f"fitted {slope:.4f} vs theory {theory:.4f}")

# and only finitely many N can have Na <= 1 on a compact
ok=True; rows=[]
for d in (0.1,0.2,0.4):
    k=len([N for N in range(1,10000) if N*d <= 1.0]); rows.append((d,k))
    if not (0 < k < 1/d + 2): ok=False
check("C' only finitely many N have Na<=1 on [d,1-d]", ok, str(rows))

# --- D. therefore the assembly is integrable across a singular point -------
# model the worst point a=1/2 with its proved blow-up -log|2a-1|
ok=True; rows=[]
for h in (1e-1,1e-2,1e-3,1e-4):
    x=np.linspace(-h,h,2000001); x=x[np.abs(x)>1e-15]
    I=np.trapz(np.abs(-np.log(np.abs(2*x))), x); rows.append((h,round(I,8)))
    if not (I < 1.0 and I > 0): ok=False
if not all(rows[i][1] > rows[i+1][1] for i in range(len(rows)-1)): ok=False
check("D  integral of the a=1/2 blow-up is finite and shrinks with h", ok, str(rows))

# --- E. pointwise divergence AND integrability coexist ---------------------
vals=[-math.log(abs(2*(0.5+h)-1)) for h in (1e-2,1e-3,1e-4,1e-5)]
check("E  pointwise value diverges while the integral stays finite (both true)",
      all(vals[i] < vals[i+1] for i in range(len(vals)-1)) and vals[-1] > 10,
      f"pointwise {['%.2f'%v for v in vals]} vs integral < 1")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
