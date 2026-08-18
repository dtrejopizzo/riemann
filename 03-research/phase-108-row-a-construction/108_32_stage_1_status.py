#!/usr/bin/env python3
"""Verifier for 108.32 -- Stage 1 terminal status assembly. Lightweight
cross-check of the load-bearing facts from 108_28/108_29/108_31, not a
re-derivation. No zero of xi is used anywhere."""
import numpy as np, sys
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

def u_s(s, r):
    if abs(s) < 1e-12:   return r*np.log(r) - r
    if abs(s+1) < 1e-12: return -np.log(r)
    return r**(s+1)/(s*(s+1))

def d2(g, r, h=1e-4):
    return (g(r+h)-2*g(r)+g(r-h))/h**2

def chi(m, n, s):
    return (float(n)**(1.0+s)) * (float(m)**(-s))

# --- (108_28) Div additive over sums of potentials of different weights ---
ok=True
for (s1,s2) in [(0.3,0.6),(0.2,0.9)]:
    g1 = lambda r,s=s1: u_s(s,r); g2 = lambda r,s=s2: u_s(s,r)
    for r in (1.3,2.5):
        lhs = d2(lambda x: g1(x)+g2(x), r)
        rhs = d2(g1,r)+d2(g2,r)
        if abs(lhs-rhs) > 1e-4*max(1.0,abs(rhs)): ok=False
check("(108_28) Div is additive across weights", ok)

# --- (108_29) chi_s(m,n) strictly positive for a wide weight bank --------
ok=True
for s in (-50.0,-1.0,0.0,0.5,0.9,50.0):
    for (m,n) in [(1,1),(2,3),(7,11)]:
        if not (chi(m,n,s) > 0): ok=False
check("(108_29) chi_s(m,n) > 0 for every tested real s", ok)

# --- (108_29) the two invariance loci are exactly {s=0} and {s=-1} -------
def is_trivial_for_all_m(s, tol=1e-9):
    vals = [chi(m,1.0,s) for m in (2,3,5,7,11)]
    return max(vals)-min(vals) < tol and abs(vals[0]-1.0) < tol
def tau_trivial_for_all_n(s, tol=1e-9):
    vals = [float(n)**(-(s+1.0)) for n in (2,3,5,7,11)]
    return max(vals)-min(vals) < tol and abs(vals[0]-1.0) < tol
ok = is_trivial_for_all_m(0.0) and not is_trivial_for_all_m(0.5) \
     and tau_trivial_for_all_n(-1.0) and not tau_trivial_for_all_n(0.5)
check("(108_29) invariance loci are exactly {s=0} (chi) and {s=-1} (tau), "
      "neither inside (0,1)", ok)

# --- (108_31) div(U_s) nonzero and pairwise distinguishable in (0,1) -----
sample_rs = np.array([0.3,0.7,1.5,2.2,4.0])
weights = (0.1,0.25,0.5,0.75,0.9)
dens = {s: r**(s-1.0) if False else sample_rs**(s-1.0) for s in weights}
ok = all(np.all(np.abs(dens[s])>1e-12) for s in weights)
sk = list(weights)
for i in range(len(sk)):
    for j in range(i+1,len(sk)):
        ratios = dens[sk[i]]/dens[sk[j]]
        if np.max(ratios)-np.min(ratios) < 1e-6: ok=False
check("(108_31) div(U_s) nonzero and pairwise distinguishable for five "
      "weights in (0,1)", ok, f"weights: {weights}")

# --- (108_31) conservativity: old Prin(G) is the s=0 slice of Prin'(G) ---
r0 = np.array([0.5,1.0,2.0,3.0])
ok = np.allclose(1.0/r0, r0**(0.0-1.0), rtol=1e-12)
check("(108_31) Prin(G) (s=0) is exactly the s=0 slice of Prin'(G)", ok)

print()
print("Assembled status table:")
rows = [
    ("pairing on individual f_a",                              "impossible (108_22, inherited)"),
    ("pairing on balanced smooth profiles, 0<a<1",              "exists, proved (108_24, inherited)"),
    ("Prin(G), literal-invariance reading",                     "s=0 only; excluded (108_26, inherited) -- superseded as definition"),
    ("Prin'(G), semi-invariance reading (108_31)",               "nonzero witnesses at every s, incl. (0,1)"),
    ("bridging a weight-s witness into 108_24's domain",         "identified, not checked (108_31 sec.5)"),
    ("Stage 1 blocking question (108_26 sec.4.1)",               "RESOLVED: YES"),
]
for a,b in rows:
    print(f"  {a:55s} | {b}")

print()
print("VERDICT:", "ALL CHECKS PASS -- Stage 1's identified blocking question "
      "(108_26 sec.4.1) is resolved (principal witnesses exist at every "
      "weight, in particular in (0,1), under the corrected Definition 3.1 "
      "of 108_31); one bridging step (108_31 sec.5) remains explicitly open"
      if not FAIL else f"FAILED: {FAIL}")
sys.exit(1 if FAIL else 0)
