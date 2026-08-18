#!/usr/bin/env python3
"""Verifier for 108.38 - Stage 2: the descent and the radical."""
import math, cmath, sys
FAIL=[]
def check(n,ok,x=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {x}");  FAIL.append(n) if not ok else None
def psi(z):
    z=complex(z); r=0.0+0j
    while z.real<15: r-=1.0/z; z=z+1
    z2=1.0/(z*z)
    return r+cmath.log(z)-0.5/z-z2*(1/12.0-z2*(1/120.0-z2*(1/252.0-z2/240.0)))
LP=math.log(math.pi)
def Phi(s):
    s=complex(s)
    return math.pi/cmath.tan(math.pi*s/2)+0.5*(psi(s/2)+psi((1-s)/2))-LP

# A. digamma implementation is correct: psi(1)=-gamma, psi(1/2)=-gamma-2log2,
#    and the recurrence psi(x+1)=psi(x)+1/x
G=0.5772156649015329
ok = abs(psi(1).real+G)<1e-11 and abs(psi(0.5).real+G+2*math.log(2))<1e-11 \
     and all(abs((psi(x+1)-psi(x)-1.0/x).real)<1e-11 for x in (0.3,1.7,4.2))
check("A  digamma: psi(1)=-gamma, psi(1/2)=-gamma-2log2, recurrence holds", ok)

# B. Phi is NOT constant  -> principal invariance fails
vals=[Phi(s).real for s in (0.1,0.25,0.5,0.75,0.9)]
check("B  Phi is not constant on (0,1): principal invariance FAILS",
      max(vals)-min(vals)>1.0, f"values {[round(v,3) for v in vals]}")

# C. Phi is NOT identically zero -> the pairing is not vacuous
check("C  Phi is not identically zero: the pairing is NOT vacuous",
      all(abs(v)>1e-6 for v in vals) and abs(Phi(0.5).real)>1.0,
      f"Phi(1/2) = {Phi(0.5).real:.9f}")

# D. exactly one sign change on the real segment, located by bisection
xs=[i/2000 for i in range(1,2000)]; sg=[Phi(x).real for x in xs]
ch=[(xs[i],xs[i+1]) for i in range(len(xs)-1) if sg[i]*sg[i+1]<0]
lo,hi=0.25,0.32
for _ in range(200):
    m=(lo+hi)/2
    if Phi(lo).real*Phi(m).real<=0: hi=m
    else: lo=m
star=(lo+hi)/2
check("D  exactly one sign change on (0,1), at s* = 0.3016923882",
      len(ch)==1 and abs(star-0.301692388160)<1e-9 and abs(Phi(star).real)<1e-12,
      f"s*={star:.12f}, |Phi(s*)|={abs(Phi(star).real):.1e}, changes={len(ch)}")

# E. the radical characterisation, on explicit combinations
def pair(lams, ss, cg):     # sum_i lam_i c_g(s_i) Phi(s_i)
    return sum(l*cg(s)*Phi(s).real for l,s in zip(lams,ss))
cgs=[lambda s: math.exp(-s), lambda s: 1.0/(1+s*s), lambda s: math.cos(2*s)]
# a mass-zero pair at two NON-zeros of Phi pairs nontrivially for some g
nz=any(abs(pair([1,-1],[0.4,0.7],cg))>1e-9 for cg in cgs)
check("E  a mass-zero pair away from the zeros of Phi is NOT in the radical", nz)
# a combination supported at a zero of Phi contributes nothing
z=all(abs(pair([1,-1],[star,star],cg))<1e-12 for cg in cgs)
check("E' point masses at a zero of Phi contribute zero to the pairing",
      z and abs(Phi(star).real)<1e-12)

print(); print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
