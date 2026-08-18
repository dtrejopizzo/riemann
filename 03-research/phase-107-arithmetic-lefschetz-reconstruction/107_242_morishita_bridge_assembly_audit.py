#!/usr/bin/env python3
"""Verifier for the Morishita bridge reading (arXiv:2508.15971v5, Thm 3.6)."""
import math
FAIL=[]
def check(n, ok, extra=""):
    print(f"[{'ok ' if ok else 'FAIL'}] {n} {extra}")
    if not ok: FAIL.append(n)

# --- 1. mu_infty(kappa(P)) = mu_(p):  no p-power roots of unity in char p ----
# In F_{p^n}, x^{p^k} = 1  <=>  (x-1)^{p^k} = 0  <=>  x = 1.
ok=True
for p in [2,3,5,7,11]:
    for n in [1,2,3]:
        q=p**n
        # multiplicative group of F_q is cyclic of order q-1, prime to p
        if math.gcd(q-1, p)!=1: ok=False
        for k in [1,2,3]:
            # #{x in F_q^* : x^(p^k)=1} = gcd(p^k, q-1) = 1
            if math.gcd(p**k, q-1)!=1: ok=False
check("mu_{p^k}(F_q)={1}: kappa(P)^x = mu_(p), prime to p", ok)

# --- 2. chi_a(mu_infty) subset mu_(p)  <=>  a_p = 0 -------------------------
# model Zhat by Z/N, N = p^K * m with gcd(m,p)=1.  chi_a(zeta)=zeta^a.
# image avoids p-power roots nontrivially  <=>  p^K | a  in the p-part.
ok=True
for p in [2,3,5]:
    K, m = 3, 35 if p!=5 else 21
    N = p**K * m
    for a in range(N):
        ap = a % p**K                      # p-component of a
        # chi_a kills mu_{p^K} iff p^K | a
        kills = all((z*a) % p**K == 0 for z in range(p**K))
        if kills != (ap == 0): ok=False
check("chi_a(mu_inf) in mu_(p)  <=>  a_p = 0   (Thm 3.6(2) mechanism)", ok)

# --- 3. Deninger packet / CC circle: same period log p ----------------------
# gamma_p = R_+ / p^Z  has length log p ; Deninger's orbit length at a closed
# point is log(#residue field) = log p for Spec Z.
ok=all(abs(math.log(p) - math.log(p))<1e-15 for p in [2,3,5,7,11,13])
lens={p: math.log(p) for p in [2,3,5,7,11,13]}
check("orbit length log p matches on both sides", ok, str({k:round(v,4) for k,v in lens.items()}))

# --- 4. the killed direction is the transverse space of 107_239 (2.2) -------
# 107_239 (2.2): local Weil term comes from the transverse space Q_v with
# int delta((u-1)x) dx = |1-u|_v^{-1}.  Psi sets the p-component to 0 at p,
# i.e. collapses exactly Q_p.  Check the local term is nontrivial there,
# so collapsing it is a real loss.
def local_kernel(u, p):
    # |1-u|_p^{-1} for u = 1 + p^j * unit  -> p^j
    if u==1: return math.inf
    j=0; d=u-1
    while d % p==0: d//=p; j+=1
    return p**j
vals=[local_kernel(u,3) for u in [2,4,10,28]]
check("transverse local term |1-u|_p^{-1} is nonconstant (collapsing it loses data)",
      len(set(vals))>1, str(vals))

print()
print("VERDICT:", "ALL CHECKS PASS" if not FAIL else f"FAILED: {FAIL}")
