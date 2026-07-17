#!/usr/bin/env python3
"""
M5 / D2 — clean check of Proposition D2 (the gradient formula) as LINEAR ALGEBRA,
on a complex-Hermitian localized arithmetic Weil Gram.  This isolates the analytic
claim  d lambda_min / d Lambda(n) = -(1/sqrt n) |<w_n|u0>|^2  from the (separate,
engine-dependent) question of whether the absolute lambda_min is the validated margin.

Reports: (i) Hellmann-Feynman gradient vs finite difference (should match to ~1e-6
if lambda_min is simple); (ii) the eigenvalue gap (simplicity check); (iii) the
gradient PROFILE over primes (the non-tautological structure).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 25

def hermite(J, u):
    H = np.zeros((J, len(u)))
    H[0] = np.pi**-0.25*np.exp(-u**2/2)
    if J>1: H[1] = np.sqrt(2.0)*u*H[0]
    for k in range(2,J): H[k] = np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2]
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
        while pk<=X: out.append((pk,lp)); pk*=p
    return out

def wvec(n, J, sigma, T0):
    x=np.log(n); hk=hermite(J,np.array([sigma*x]))[:,0]
    ik=np.array([(-1j)**k for k in range(J)])
    return ik*hk*np.exp(-1j*T0*x)          # phi_k(log n), complex

def build_Q(J=10, sigma=1.0, T0=46.13, X=20000, a=0.25, logcond=0.0, chi=None):
    u=np.linspace(-9,9,3000); r=T0+sigma*u; h=hermite(J,u); du=u[1]-u[0]
    Omega=np.array([float(mp.re(mp.digamma(a+1j*rr/2))) for rr in r])-np.log(np.pi)+logcond
    A=np.zeros((J,J))
    for i in range(J):
        for j in range(i,J):
            A[i,j]=np.sum(h[i]*h[j]*Omega)*du*sigma/(2*np.pi); A[j,i]=A[i,j]
    P=np.zeros((J,J),complex); coeffs={}
    for (n,lp) in pp_terms(X):
        w=wvec(n,J,sigma,T0)
        cn=chi[n%5] if chi else 1.0
        LamL=cn*lp; coeffs[n]=LamL
        P+=(LamL/np.sqrt(n))*np.outer(w,np.conj(w))
    Q=A.astype(complex)-P
    Q=(Q+Q.conj().T)/2
    return Q, coeffs

J,sigma,T0,X=10,1.0,46.13,20000
print("="*74); print("M5 / D2 — Proposition D2 gradient check (complex-Hermitian Q)"); print("="*74)
Q,coeffs=build_Q(J,sigma,T0,X)            # zeta
w,V=np.linalg.eigh(Q); l0=w[0]; u0=V[:,0]
gap=w[1]-w[0]
print(f"J={J} sigma={sigma} T0={T0} X={X}")
print(f"lambda_min = {l0:+.6e}   gap(lambda_1-lambda_0) = {gap:.4e}   (simple if gap>>0)")
print("\n Prop D2:  d lambda_min/d Lambda(n) = -(1/sqrt n)|<w_n|u0>|^2")
print("   n    HF_analytic        finite_diff        rel_err")
eps=1e-6
for n in [2,3,4,5,7,8,9,11,13]:
    w_n=wvec(n,J,sigma,T0)
    hf=-(1.0/np.sqrt(n))*abs(np.vdot(w_n,u0))**2          # <w_n|u0> = sum conj(w_n)_k u0_k
    dQ=-(eps/np.sqrt(n))*np.outer(w_n,np.conj(w_n))       # d/dLambda(n) of Q=A-P, times eps
    dQ=(dQ+dQ.conj().T)/2
    lp=np.linalg.eigvalsh(Q+dQ)[0]
    fd=(lp-l0)/eps
    print(f"  {n:3d}   {hf:+.6e}   {fd:+.6e}   {abs(hf-fd)/(abs(hf)+1e-30):.2e}")
print("\n gradient PROFILE |dI/dLambda(n)| = (1/sqrt n)|<w_n|u0>|^2 over primes:")
prof=[]
for p in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]:
    w_p=wvec(p,J,sigma,T0); g=(1/np.sqrt(p))*abs(np.vdot(w_p,u0))**2; prof.append((p,g))
mx=max(g for _,g in prof)
for p,g in prof: print(f"   p={p:3d}  {g:.3e}  {'#'*int(60*g/mx) if mx>0 else ''}")
nsig=sum(1 for _,g in prof if g>0.01*mx)
print(f"\n => {nsig}/{len(prof)} primes carry >1% of the max gradient: the invariant's")
print(f"    sensitivity is SPREAD across many Euler factors (structural non-tautology).")
print("="*74)
