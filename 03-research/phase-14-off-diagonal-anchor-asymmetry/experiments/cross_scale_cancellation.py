#!/usr/bin/env python3
"""
The cross-scale cancellation door: how do the primes, octave by octave, build the saturation lambda=1
on the saturating direction g*?

For band d, g* = top generalized eigenvector of (P_F, A_Phi) (the lambda_max ~ 1 direction).
The prime form on g* is p[g*] = a[g*] (since lambda=1).  Naively |p_{<=Y}[g*]| could ~ sqrt(Y) -> e^d,
but it converges to a[g*] ~ log.  We measure the RUNNING RATIO

    R(Y) = p_{<=Y}[g*] / a[g*]    as Y runs over octaves up to e^{2d},

and the per-octave increments Delta R.  FORK:
  increments DECAY  -> cross-scale cancellation is convergent/robust (saturation 'settles');
  increments stay O(1) and alternate -> marginal conspiracy (each octave matters, knife-edge in the limit).

Also reports |p_{<=Y}|/sqrt(Y) to expose the cancellation strength vs the naive Chebyshev amplitude.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 18

def Phi_vec(r):
    out = np.empty_like(r); lp = float(mp.log(mp.pi))
    for i, rr in enumerate(r):
        out[i] = float(mp.re(mp.digamma(mp.mpf('0.25') + 1j*rr/2))) - lp
    return out

def prime_powers(X):
    X = int(X); sieve = np.ones(X+1, bool); sieve[:2] = False
    for p in range(2, int(X**0.5)+1):
        if sieve[p]: sieve[p*p::p] = False
    out = []
    for p in np.nonzero(sieve)[0]:
        lp = np.log(p); pk = p
        while pk <= X:
            out.append((np.log(pk), lp/np.sqrt(pk))); pk *= p
    return np.array(out)

def Fmat(r, pp_subset):
    if pp_subset.shape[0]==0: return np.zeros_like(r)
    logs = pp_subset[:,0][:,None]; amps = pp_subset[:,1][:,None]
    return 2.0*np.sum(amps*np.cos(logs*r[None,:]), axis=0)

def run(d, T0=1000.0, N=None, grid_pts=8000):
    if N is None: N = int(round(3*d))+6
    spacing = np.pi/d; centers = T0 + spacing*np.arange(-N, N+1)
    span = (N+8)*spacing
    r = np.linspace(T0-span, T0+span, grid_pts); w = r[1]-r[0]
    Xarg = d*(r[None,:]-centers[:,None]); S = np.sinc(Xarg/np.pi)
    Phi = Phi_vec(r); Sw = S*w
    A = Sw @ (Phi[:,None]*S.T); A=(A+A.T)/2
    pp = prime_powers(np.exp(2*d))
    Pfull = Sw @ (Fmat(r, pp)[:,None]*S.T); Pfull=(Pfull+Pfull.T)/2
    # generalized top eigenvector
    L = np.linalg.cholesky(A); Li = np.linalg.inv(L)
    M = Li @ Pfull @ Li.T; M=(M+M.T)/2
    ev, U = np.linalg.eigh(M)
    u = U[:,-1]; lam_top = ev[-1]
    g = Li.T @ u                         # original basis
    aval = g @ A @ g
    # octave running ratio
    Ys = np.exp(np.arange(1.0, 2*d+1e-9, 1.0))     # cutoffs e^1, e^2, ..., e^{2d}
    print(f"\n  d={d}  lam_top={lam_top:.5f}  a[g*]={aval:.4e}   (naive tail amp ~ sqrt(e^2d)={np.exp(d):.1f})")
    print(f"   {'Y=e^k':>10} {'#primes<=Y':>11} {'R(Y)=p<=Y/a':>13} {'dR(octave)':>11} {'|p<=Y|/sqrtY':>13}")
    prevR = 0.0
    for k,Y in enumerate(Ys, start=1):
        sub = pp[pp[:,0] <= np.log(Y)+1e-12]
        PY = Sw @ (Fmat(r, sub)[:,None]*S.T); PY=(PY+PY.T)/2
        pY = g @ PY @ g
        R = pY/aval
        print(f"   {k:>10d} {sub.shape[0]:>11d} {R:>13.5f} {R-prevR:>11.5f} {abs(pY)/np.sqrt(Y):>13.5f}")
        prevR = R

if __name__ == "__main__":
    print("="*86)
    print(" CROSS-SCALE CANCELLATION on the saturating direction g*.  R(Y)=p_{<=Y}[g*]/a[g*] -> 1.")
    print("  decaying octave increments dR => robust/convergent ; O(1) alternating => marginal conspiracy.")
    print("="*86)
    for d in [4.0, 5.0, 6.0]:
        run(d)
    print("="*86)
