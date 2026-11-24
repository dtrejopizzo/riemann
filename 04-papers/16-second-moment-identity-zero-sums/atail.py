#!/usr/bin/env python3
"""
Largest and smallest generalized eigenvalues of the pencil (p_{>X}, a) on a
band-d sinc space at height T0 = 1000, where p_{>X} keeps only the prime
powers n in (X, e^{2d}] and a is the archimedean multiplier form
(without pole terms). Prints a_tail(X) = max(|lambda_max|, |lambda_min|).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 18

def Phi_vec(r):
    out = np.empty_like(r); lp = float(mp.log(mp.pi))
    for i, rr in enumerate(r):
        out[i] = float(mp.re(mp.digamma(mp.mpf('0.25') + 1j*rr/2))) - lp
    return out

def prime_powers_range(Xlo, Xhi):
    """prime powers n=p^k with Xlo < n <= Xhi -> (log n, Lambda(n)/sqrt n)."""
    Xhi = int(Xhi)
    sieve = np.ones(Xhi+1, bool); sieve[:2] = False
    for p in range(2, int(Xhi**0.5)+1):
        if sieve[p]: sieve[p*p::p] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        lp = np.log(p); pk = p
        while pk <= Xhi:
            if pk > Xlo: out.append((np.log(pk), lp/np.sqrt(pk)))
            pk *= p
    return np.array(out) if out else np.empty((0,2))

def F_vec(r, pp):
    if pp.shape[0]==0: return np.zeros_like(r)
    logs = pp[:,0][:,None]; amps = pp[:,1][:,None]
    return 2.0*np.sum(amps*np.cos(logs*r[None,:]), axis=0)

def a_tail(d, T0, X, N=10, grid_pts=8000):
    spacing = np.pi/d
    centers = T0 + spacing*np.arange(-N, N+1)
    span = (N+8)*spacing
    r = np.linspace(T0-span, T0+span, grid_pts); w = r[1]-r[0]
    Xarg = d*(r[None,:]-centers[:,None]); S = np.sinc(Xarg/np.pi)
    Phi = Phi_vec(r)
    pp = prime_powers_range(X, np.exp(2*d))
    F = F_vec(r, pp)
    Sw = S*w
    A = Sw @ (Phi[:,None]*S.T); P = Sw @ (F[:,None]*S.T)
    A = (A+A.T)/2; P = (P+P.T)/2
    evA = np.linalg.eigvalsh(A)
    if evA[0] <= 0: return None
    L = np.linalg.cholesky(A); Li = np.linalg.inv(L)
    M = Li @ P @ Li.T; M = (M+M.T)/2
    ev = np.linalg.eigvalsh(M)
    return dict(lmax=ev[-1], lmin=ev[0], a_tail=max(abs(ev[-1]),abs(ev[0])),
                nprimes=pp.shape[0])

if __name__ == "__main__":
    print("="*86)
    print(" a_tail(X) = spectral radius of (P_F^{>X}, A_Phi).  X = head cutoff.")
    print(" flag: <1, ~1 (within 5e-3) or >1.")
    print("="*86)
    for d in [4.0, 5.0]:
        Nmax = np.exp(2*d)
        print(f"\n d={d}  (tail primes up to e^(2d)={Nmax:.0f}); high smooth height T0=1000")
        print(f"   {'X (head cut)':>14} {'lambda_max':>12} {'lambda_min':>12} {'a_tail(X)':>11} {'#tail terms':>12}")
        for X in [1, 5, 13, 30, 70, 150, 400, 1000, int(Nmax)//4, int(Nmax)//2]:
            if X >= Nmax: continue
            res = a_tail(d, 1000.0, X)
            if res is None:
                print(f"   {X:>14} A not PD"); continue
            flag = "  <1" if res['a_tail']<1-1e-9 else ("  ~1" if abs(res['a_tail']-1)<5e-3 else "  >1")
            print(f"   {X:>14} {res['lmax']:>12.5f} {res['lmin']:>12.5f} {res['a_tail']:>11.5f} {res['nprimes']:>12d}{flag}")
    print("="*86)
