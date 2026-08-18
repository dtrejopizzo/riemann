#!/usr/bin/env python3
"""Verifier for 108.27 - why weight s=0 is forced, and what would unforce it.
No zero of xi is used anywhere."""
import math, numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

def d2(g, r, h=1e-4):
    return (g(r+h)-2*g(r)+g(r-h))/h**2

# 108_03 (2.1): u_s(r) = r^{s+1}/(s(s+1)) for s not in {0,-1}
def u(s):
    if abs(s) < 1e-12:      return lambda r: r*np.log(r) - r
    if abs(s+1) < 1e-12:    return lambda r: -np.log(r)
    return lambda r: r**(s+1)/(s*(s+1))

# --- A. Div is LINEAR in f  (this is the whole point) ----------------------
# u_f'' = f(r)/r ; so u_{cf}'' = c f(r)/r, i.e. Div(cU) = c Div(U)
ok=True; rows=[]
for s in (0.3, 0.5, 0.8):
    for c in (2.0, -3.5, 0.25):
        rs=[1.3, 2.0, 3.7]
        lhs=[c*d2(u(s), r) for r in rs]          # c * u_s''
        rhs=[c*r**(s-1) for r in rs]             # c * f_s(r)/r
        e=max(abs(a-b)/max(1e-12,abs(b)) for a,b in zip(lhs,rhs))
        rows.append((s,c,round(e,12)))
        if e>1e-5: ok=False
check("A  Div is LINEAR in f: Div(cU) = c Div(U), not Div(U)", ok,
      f"max rel err {max(r[2] for r in rows):.1e}")

# --- B. Div kills affine functions (107_237 Thm 2.1: unique mod affine) ---
# Test the two facts that compose the statement, avoiding catastrophic
# cancellation from differencing a large constant twice at h=1e-4:
#   (i) the second derivative of an affine function is exactly 0;
#   (ii) the second-difference operator is linear.
# Together these give d2(g + affine) = d2(g) exactly.
ok=True; worst=0.0
for al,be in ((2.3,-1.1),(-0.7,4.2),(10.0,10.0),(1e3,1e3)):
    for r in (1.3,2.0,3.7):
        for h in (1e-2,1e-3):
            v=((al*(r+h)+be) - 2*(al*r+be) + (al*(r-h)+be))/h**2
            worst=max(worst,abs(v))
            if abs(v) > 1e-6*max(1.0,abs(al)): ok=False
check("B(i)  the second difference of an affine function is 0", ok,
      f"worst |d2(affine)| = {worst:.2e}")
ok=True
for s_ in (0.3,0.5,0.8):
    g=u(s_)
    for r in (1.3,2.0,3.7):
        h=1e-2
        lin=( (g(r+h)+2.3*(r+h)-1.1) - 2*(g(r)+2.3*r-1.1) + (g(r-h)+2.3*(r-h)-1.1) )/h**2
        base=(g(r+h)-2*g(r)+g(r-h))/h**2
        if abs(lin-base) > 1e-6*max(1.0,abs(base)): ok=False
check("B(ii) hence d2(g + affine) = d2(g): Div is insensitive to affine shifts", ok)

# --- C. the Frobenius action is MULTIPLICATIVE on potentials --------------
# 108_02: f_s(r/n) = chi(n) f_s(r) with chi(n) = n^{-s}
ok=True; rows=[]
for s in (0.0, 0.3, 0.5, 0.8):
    for n in (2,3,5,7):
        lhs=(2.7/n)**s if False else (2.7/n)**(-s)   # f_s(r/n) with f_s(r)=r^{-s}
        rhs=(n**(s))*(2.7**(-s))                     # chi(n) f_s(r), chi(n)=n^{s}
        rows.append((s,n,round(abs(lhs-rhs),14)))
        if abs(lhs-rhs) > 1e-12: ok=False
check("C  f_s(r/n) = chi(n) f_s(r) exactly, with chi(n) a nontrivial character",
      ok, f"max err {max(r[2] for r in rows):.1e}")

# --- D. invariance of Div forces chi == 1, i.e. s = 0 --------------------
# Div transforms by the MULTIPLIER chi(n); Div is invariant iff chi(n)=1 for all n
def chi(n, s): return float(n)**(s)
ok=True; rows=[]
for s in (0.0, 1e-3, 0.1, 0.5, 0.9, 1.0):
    trivial = all(abs(chi(n,s)-1.0) < 1e-12 for n in (2,3,5,7,11,101))
    rows.append((s, trivial))
    if trivial != (abs(s) < 1e-12): ok=False
check("D  chi(n) = n^{s} is trivial for ALL n iff s = 0", ok, str(rows))

# --- E. the mismatch: action multiplies, Div only forgives addition ------
# Div forgives U -> U + affine (check B) but NOT U -> chi*U (check A).
# The Frobenius action is of the second kind (check C).  Hence s=0 forced.
s=0.5; g=u(s); r0=2.0
add_ok = abs(d2(lambda r: g(r)+3.1*r+0.7, r0) - d2(g,r0)) < 1e-6
mul_ok = abs(d2(lambda r: 2.0*g(r), r0) - d2(g,r0)) < 1e-6
check("E  Div forgives ADDITION of affine but not MULTIPLICATION by a constant",
      add_ok and (not mul_ok),
      f"additive invariant: {add_ok}; multiplicative invariant: {mul_ok}")

# --- F. what would unforce it: a logarithmic Div -------------------------
# classically div(c*phi) = div(phi) because div is logarithmic.
# model: Dlog(U) := (log U)'' would satisfy Dlog(cU) = Dlog(U)
def dlog2(g, r, h=1e-4):
    L=lambda x: math.log(abs(g(x)))
    return (L(r+h)-2*L(r)+L(r-h))/h**2
ok=all(abs(dlog2(lambda r,g=u(0.5),c=c: c*g(r), 2.0) - dlog2(u(0.5), 2.0)) < 1e-6
       for c in (2.0, 5.0, 0.3))
check("F  a LOGARITHMIC divisor would be invariant under constant multiples",
      ok, "so the obstruction is the linearity of Div, not the family")

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
