#!/usr/bin/env python3
"""
Spectrum of the full pencil (p, a) on band-d sinc spaces at height T0 = 1000,
for d = 3,...,6, with the basis size scaled with d. Prints lambda_max,
lambda_2, their gap, and the number of eigenvalues above 0.9 and 0.99.
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

def F_vec(r, pp):
    logs = pp[:,0][:,None]; amps = pp[:,1][:,None]
    return 2.0*np.sum(amps*np.cos(logs*r[None,:]), axis=0)

def pencil_spectrum(d, T0, N, grid_pts=7000):
    spacing = np.pi/d
    centers = T0 + spacing*np.arange(-N, N+1)
    span = (N+8)*spacing
    r = np.linspace(T0-span, T0+span, grid_pts); w = r[1]-r[0]
    Xarg = d*(r[None,:]-centers[:,None]); S = np.sinc(Xarg/np.pi)
    Phi = Phi_vec(r); pp = prime_powers(np.exp(2*d)); F = F_vec(r, pp)
    Sw = S*w
    A = Sw @ (Phi[:,None]*S.T); P = Sw @ (F[:,None]*S.T)
    A = (A+A.T)/2; P = (P+P.T)/2
    evA = np.linalg.eigvalsh(A)
    if evA[0] <= 1e-12*evA[-1]:
        # restrict to well-conditioned subspace of A
        keep = evA > 1e-10*evA[-1]
        wv, V = np.linalg.eigh(A); V = V[:, wv>1e-10*wv[-1]]; wvv = wv[wv>1e-10*wv[-1]]
        Ah = V.T@A@V; Ph = V.T@P@V
        L = np.linalg.cholesky((Ah+Ah.T)/2); Li=np.linalg.inv(L)
        M = Li@((Ph+Ph.T)/2)@Li.T
    else:
        L = np.linalg.cholesky(A); Li = np.linalg.inv(L)
        M = Li @ P @ Li.T
    ev = np.linalg.eigvalsh((M+M.T)/2)
    return ev, pp.shape[0]

if __name__ == "__main__":
    print("="*88)
    print(" Full pencil (p,a): top of the spectrum versus band d.")
    print("  gap = lambda_max - lambda_2 ;  n>0.9, n>0.99 = near-critical multiplicity.")
    print("="*88)
    T0 = 1000.0
    print(f"\n   {'d':>4} {'#primes':>8} {'dim':>5} {'lam_max':>9} {'lam_2':>9} {'gap':>8} {'n>0.9':>6} {'n>0.99':>7}  top-5")
    for d in [3.0, 4.0, 5.0, 6.0]:
        N = int(round(3*d)) + 6      # scale basis with band so window ~ const in zeros
        ev, npr = pencil_spectrum(d, T0, N)
        lam = ev[::-1]               # descending
        lmax, l2 = lam[0], lam[1]
        gap = lmax - l2
        n90 = int(np.sum(lam > 0.9)); n99 = int(np.sum(lam > 0.99))
        top5 = " ".join(f"{x:.4f}" for x in lam[:5])
        print(f"   {d:>4.0f} {npr:>8d} {len(ev):>5d} {lmax:>9.5f} {l2:>9.5f} {gap:>8.5f} {n90:>6d} {n99:>7d}  {top5}")
    print("="*88)
