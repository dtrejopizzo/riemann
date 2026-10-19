#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — Discriminant.  E2: does MULTIPLICATIVITY control the sign of Weil?
#
# E1 showed that the zero-side is blind to multiplicativity (it only sees zero location).
# The thesis lives on the ARITHMETIC side P (prime block of the explicit formula).
#
# Previous BLOCKER (Phase3-results.md): comparing real L-functions (ζ vs L(χ4)) is
# confounded because they have different Γ factors (a=1/4 vs 3/4) => different A baselines,
# and absolute calibration of the normalization is not settled (C(ζ)~1.98, factor-2).
#
# METHODOLOGICAL CONTRIBUTION (unblocks the discriminant):
#   Fix the archimedean block A (the one for ζ, a=1/4) and vary ONLY the multiplicativity
#   of the coefficients c(n) in the prime block P. The unknown normalization
#   affects ALL the P's equally => it cancels out in the RELATIVE comparison.
#
#   Controls (all with the SAME support {prime powers n<=X} and SAME A):
#     P_zeta    : c(n)=Λ(n)            (multiplicative, derived from Euler)        <- real
#     P_shuffle : exactly the multiset {Λ(n)} reassigned to permuted log n
#                 positions  (preserves the value DISTRIBUTION, breaks the
#                 arithmetic position<->value correlation)                         <- control
#     P_random  : c(n) iid with same mean/var as Λ(n) on the support              <- control
#
# PRE-REGISTRATION (00-PLAN §5):
#   GO   : P_zeta separates from the controls in a STABLE way (X, seed) =>
#          multiplicativity leaves an operator signature. Conjecture + paper.
#   NO-GO: P_zeta falls inside the control cloud => multiplicativity does NOT
#          control the sign on this observable => record NG and close the route.
#
# HONEST: the ABSOLUTE calibration (C<=1) remains open; here we report the
# RELATIVE discriminant (ranking/separation), which is invariant to the normalization.
# ======================================================================================
import numpy as np, mpmath as mp
mp.mp.dps = 20
rng_global = np.random.default_rng(12345)

J, SIGMA, T0, X = 12, 1.0, 46.13, 100000
NCTRL = 200   # number of random/shuffle controls

def hermite(J,u):
    H=np.zeros((J,len(u))); H[0]=np.pi**-0.25*np.exp(-u**2/2)
    if J>1: H[1]=np.sqrt(2.0)*u*H[0]
    for k in range(2,J): H[k]=np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2]
    return H
def primes_upto(X):
    s=np.ones(X+1,bool); s[:2]=False
    for p in range(2,int(X**0.5)+1):
        if s[p]: s[p*p::p]=False
    return np.nonzero(s)[0]
def pp_terms(X):
    out=[]
    for p in primes_upto(X):
        pk=p; lp=np.log(p)
        while pk<=X: out.append((pk,p,lp)); pk*=p
    return out
def wvec(n,J,sigma,T0):
    x=np.log(n); hk=hermite(J,np.array([sigma*x]))[:,0]
    ik=np.array([(-1j)**k for k in range(J)])
    return ik*hk*np.exp(-1j*T0*x)

def build_A(J,sigma,T0):
    u=np.linspace(-10,10,5000); r=T0+sigma*u; h=hermite(J,u); du=u[1]-u[0]
    a=0.25
    Omega=np.array([float(mp.re(mp.digamma(a+1j*rr/2))) for rr in r])-np.log(np.pi)
    A=np.zeros((J,J))
    for i in range(J):
        for j in range(i,J):
            A[i,j]=np.sum(h[i]*h[j]*Omega)*du*sigma; A[j,i]=A[i,j]
    return A

def build_P(coeffs, terms, J, sigma, T0):
    """coeffs[k] is c(n)/sqrt(n) for the k-th term (n,p,lp). P = sum c_k w w*."""
    P=np.zeros((J,J),complex)
    for c,(n,p,lp) in zip(coeffs,terms):
        w=wvec(n,J,sigma,T0)
        P+=c*np.outer(w,np.conj(w))
    return np.real((P+P.conj().T)/2)

def carleson(A,P):
    w,V=np.linalg.eigh(A); w=np.maximum(w,1e-12)
    Ainv2=V@np.diag(w**-0.5)@V.T
    M=Ainv2@P@Ainv2; M=(M+M.T)/2
    return np.linalg.eigvalsh(M)[-1], np.linalg.eigvalsh(A-P)[0]

print("building archimedean block A (zeta, a=1/4) ...", flush=True)
A=build_A(J,SIGMA,T0)
terms=pp_terms(X)
sqrtn=np.array([np.sqrt(n) for (n,p,lp) in terms])
Lam=np.array([lp for (n,p,lp) in terms])          # real Λ(n)
base_zeta = Lam/sqrtn                               # c(n)/sqrt(n), multiplicative

print(f"  J={J}, sigma={SIGMA}, T0={T0}, X={X}, #prime-power terms={len(terms)}")

Cz,lz = carleson(A, build_P(base_zeta, terms, J,SIGMA,T0))
print(f"\n[REAL] zeta (multiplicative): C={Cz:.4f}   lambda_min(A-P)={lz:+.4e}")
print( "       (absolute C NOT calibrated, known ~factor-2; we use RELATIVE comparison)")

# --- controls: same A, same support, same |coeff| distribution, no multiplicativity ---
mu, sd = base_zeta.mean(), base_zeta.std()
Cs_shuffle, ls_shuffle = [], []
Cs_random,  ls_random  = [], []
for s in range(NCTRL):
    rng = np.random.default_rng(s)
    # shuffle: SAME values, permuted (log n) positions
    perm = rng.permutation(len(base_zeta))
    Csh,lsh = carleson(A, build_P(base_zeta[perm], terms, J,SIGMA,T0))
    Cs_shuffle.append(Csh); ls_shuffle.append(lsh)
    # random: iid gaussian with same mean/var, clipped to >=0 (Λ>=0)
    cr = np.clip(rng.normal(mu,sd,len(base_zeta)),0,None)
    Crd,lrd = carleson(A, build_P(cr, terms, J,SIGMA,T0))
    Cs_random.append(Crd); ls_random.append(lrd)

Cs_shuffle=np.array(Cs_shuffle); Cs_random=np.array(Cs_random)
def z(val, arr): return (val-arr.mean())/arr.std() if arr.std()>0 else float('nan')

print("\n"+"="*78)
print(" RELATIVE DISCRIMINANT  (C; how much ζ stands out from the control cloud)")
print("="*78)
print(f"  zeta C                         : {Cz:.4f}")
print(f"  shuffle  (n={NCTRL})  C        : media {Cs_shuffle.mean():.4f}  std {Cs_shuffle.std():.4f}  rango[{Cs_shuffle.min():.3f},{Cs_shuffle.max():.3f}]")
print(f"  random   (n={NCTRL})  C        : media {Cs_random.mean():.4f}  std {Cs_random.std():.4f}  rango[{Cs_random.min():.3f},{Cs_random.max():.3f}]")
print(f"\n  z-score zeta vs shuffle : {z(Cz,Cs_shuffle):+.2f} sigma")
print(f"  z-score zeta vs random  : {z(Cz,Cs_random):+.2f} sigma")
pct_sh = (Cs_shuffle < Cz).mean()*100
pct_rd = (Cs_random  < Cz).mean()*100
print(f"  zeta percentile in shuffle: {pct_sh:.0f}%   in random: {pct_rd:.0f}%")

print("\n"+"="*78)
print(" VERDICT (pre-registered)")
print("="*78)
zs = abs(z(Cz,Cs_shuffle)); zr = abs(z(Cz,Cs_random))
if zs>3 and zr>3:
    print(" GO: ζ separates >3σ from BOTH controls => multiplicativity leaves a stable")
    print("     operator signature. Next: stability in X and T0, and identify the block.")
elif zs<1 and zr<1:
    print(" NO-GO: ζ falls INSIDE the control cloud (<1σ) => on this observable")
    print("        multiplicativity does NOT control the sign. Record NG, close the route.")
else:
    print(" PARTIAL: intermediate separation. Requires stability (X, T0, seed) before")
    print("          concluding. Do not report as a result yet.")
