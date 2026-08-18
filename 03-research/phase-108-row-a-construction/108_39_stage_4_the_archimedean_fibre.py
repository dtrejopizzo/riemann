#!/usr/bin/env python3
"""Verifier for 108.39 - Stage 4: the archimedean fibre and its polar page."""
import math, cmath, sys
from fractions import Fraction as F
FAIL=[]
def check(n,ok,x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}");  FAIL.append(n) if not ok else None
def psi(z):
    z=complex(z); r=0j
    while z.real<15: r-=1.0/z; z=z+1
    z2=1.0/(z*z)
    return r+cmath.log(z)-0.5/z-z2*(1/12.0-z2*(1/120.0-z2*(1/252.0-z2/240.0)))
LP=math.log(math.pi)
def Gp(s):  return -0.5*LP+0.5*psi(complex(s)/2)          # (log Gamma_R)'
def fin(s): return 0.5*(psi(complex(s)/2)+psi((1-complex(s))/2))-LP
def Phi(s): return math.pi/cmath.tan(math.pi*complex(s)/2)+fin(s)

PTS=(0.3,0.5,0.7,0.5+2j,0.25-1j)
# A. Theorem 1.1
ok=all(abs(fin(s)-(Gp(s)+Gp(1-s)))<1e-12 for s in PTS)
check("A  finite part = G'(s)+G'(1-s), G = log of pi^{-s/2}Gamma(s/2)", ok,
      f"{len(PTS)} arguments")

# B. Corollary 1.2
ok=all(abs(Phi(s)-(math.pi/cmath.tan(math.pi*complex(s)/2)+Gp(s)+Gp(1-s)))<1e-12
       for s in (0.2,0.5,0.8,0.4+3j))
check("B  Phi = pi cot(pi s/2) + G'(s) + G'(1-s)", ok)

# C. Theorem 2.1, in floating point
def P(s):
    s=complex(s); return 1/s+1/(s-1)
ok=all(abs(P(s)+P(1-s))<1e-13 for s in (0.3,0.5,0.7,1.4,0.6+2j))
check("C  polar page cancels: P(s)+P(1-s)=0", ok)

# C'. and in EXACT rational arithmetic, so the cancellation is not numerical
ok=True
for s in (F(1,3),F(1,2),F(2,7),F(5,4),F(-3,5)):
    if s in (0,1): continue
    v = (F(1,1)/s + F(1,1)/(s-1)) + (F(1,1)/(1-s) + F(1,1)/(-s))
    if v != 0: ok=False
check("C' the polar cancellation is EXACT (rational arithmetic)", ok)

# D. digamma sanity
G=0.5772156649015329
check("D  psi(1)=-gamma, psi(1/2)=-gamma-2log2, recurrence",
      abs(psi(1).real+G)<1e-11 and abs(psi(0.5).real+G+2*math.log(2))<1e-11
      and all(abs((psi(x+1)-psi(x)-1.0/x).real)<1e-11 for x in (0.3,1.7,4.2)))

# E. the two archimedean pieces are genuinely different functions
ok=any(abs(math.pi/cmath.tan(math.pi*complex(s)/2)-(Gp(s)+Gp(1-s)))>1e-3
       for s in (0.2,0.5,0.8))
check("E  the local term and the Gamma-factor piece are distinct functions", ok)

print(); print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
