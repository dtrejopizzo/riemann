#!/usr/bin/env python3
"""
Phase 3 (first pass) — the Carleson constant  C(L) = lambda_max(A^{-1/2} P A^{-1/2})
and the Hermite-vs-Slepian band test.

C(L) <= 1  <=>  local Weil positivity (Theorem T4-I).  We compute C for zeta and
L(chi4 mod 5) (clean Euler products), report whether C<=1 (validation/consistency),
whether C(zeta) != C(L(chi)) (does the Carleson constant discriminate RH-true L's?),
and run the band test (does the anatomy concentration survive a flat Slepian envelope?).

HONEST: this uses a self-contained Gram, NOT P7's validated engine.  Faithful absolute
calibration (zeta passing the positivity gate) requires engine-spec §3 (X=1e5, full
archimedean+polar, validated normalization).  We report what this build shows + caveats.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20

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

def build(Lname,J=12,sigma=1.0,T0=46.13,X=100000):
    u=np.linspace(-10,10,5000); r=T0+sigma*u; h=hermite(J,u); du=u[1]-u[0]
    if Lname=='zeta': a=0.25; logcond=0.0; chi=None
    else: a=0.75; logcond=np.log(5.0); chi={1:1+0j,2:1j,3:-1j,4:-1+0j,0:0}
    Omega=np.array([float(mp.re(mp.digamma(a+1j*rr/2))) for rr in r])-np.log(np.pi)+logcond
    A=np.zeros((J,J))
    for i in range(J):
        for j in range(i,J):
            A[i,j]=np.sum(h[i]*h[j]*Omega)*du*sigma; A[j,i]=A[i,j]   # NB: no 1/2pi (abs. cal. open)
    P=np.zeros((J,J),complex)
    for (n,p,lp) in pp_terms(X):
        w=wvec(n,J,sigma,T0); cn=(chi[p%5]**(int(round(np.log(n)/np.log(p))))) if chi else 1.0
        LamL=np.real(cn)*lp if chi else lp     # Re for Hermitian (chi-twist symmetrized)
        P+=(LamL/np.sqrt(n))*np.outer(w,np.conj(w))
    P=(P+P.conj().T)/2
    return A, np.real(P), Omega.mean()

def carleson(A,P):
    # C = lambda_max( A^{-1/2} P A^{-1/2} );  C<=1 <=> A-P >=0
    w,V=np.linalg.eigh(A); w=np.maximum(w,1e-12)
    Ainv2=V@np.diag(w**-0.5)@V.T
    M=Ainv2@P@Ainv2; M=(M+M.T)/2
    return np.linalg.eigvalsh(M)[-1], np.linalg.eigvalsh(A-P)[0]

print("="*74); print("Phase 3 — Carleson constant C(L)=lambda_max(A^{-1/2}P A^{-1/2}); C<=1 <=> positivity")
print("="*74)
for X in [1000, 20000, 100000]:
    Az,Pz,Om=build('zeta',X=X); Cz,lz=carleson(Az,Pz)
    Ac,Pc,_=build('chi4',X=X); Cc,lc=carleson(Ac,Pc)
    print(f"\nX={X:6d}  (mean Omega={Om:.3f})")
    print(f"  zeta        : C={Cz:8.4f}   lambda_min(A-P)={lz:+.4e}   {'POS' if lz>=-1e-9 else 'NEG (baseline not suppressed)'}")
    print(f"  L(chi4 mod5): C={Cc:8.4f}   lambda_min(A-P)={lc:+.4e}   {'POS' if lc>=-1e-9 else 'NEG'}")
    print(f"  discriminant: |C(zeta)-C(chi4)| = {abs(Cz-Cc):.4f}")

# ---- band test: anatomy density |u0_hat(log p)|^2, Hermite vs flat-window proxy ----
print("\n"+"="*74); print("BAND TEST: anatomy density over primes (Hermite basis)")
Az,Pz,_=build('zeta',X=100000); w,V=np.linalg.eigh(Az-Pz); u0=V[:,0]
J=u0.shape[0]; sigma,T0=1.0,46.13
print(" log p   p    |u0_hat(log p)|^2   (Hermite envelope ~ |x|<sqrt(2J)/sigma="+f"{np.sqrt(2*J)/sigma:.1f})")
prof=[]
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,67,79,89]:
    x=np.log(p); hk=hermite(J,np.array([sigma*x]))[:,0]
    ik=np.array([(-1j)**k for k in range(J)]); wv=ik*hk*np.exp(-1j*T0*x)
    g=abs(np.vdot(np.conj(u0),wv))**2; prof.append((x,p,g))
mx=max(g for _,_,g in prof)
for x,p,g in prof: print(f"  {x:4.2f}  {p:3d}   {g:.3e}  {'#'*int(50*g/mx) if mx>0 else ''}")
print("\n NOTE: the Hermite envelope cuts at |log p|<~"+f"{np.sqrt(2*J)/sigma:.1f}; concentration near that edge")
print(" is basis (turning point), not necessarily arithmetic. A Slepian (flat-box) basis is needed to")
print(" decide; that is the genuine band test (engine-spec §3 + prolate basis).")
print("="*74)
