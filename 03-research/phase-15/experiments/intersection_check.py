#!/usr/bin/env python3
"""
M1 numerical grounding.
(B) Gamma.Gamma = int_{-2d}^{2d}|S|^2 = pair-correlation 2nd moment >= 0  (Theorem B, P18 identity).
(A) Trace identity = Weil explicit formula:
      sum_rho h(gamma_rho)  ==  [h(i/2)+h(-i/2)] - 2 sum_n Lambda(n)/sqrt(n) g(log n) + (1/2pi) int h(r) W(r) dr,
    W(r) = Re psi(1/4 + i r/2) - log pi,   g(u) = (1/2pi) int h(r) e^{-iur} dr.
We test a Gaussian bump test function h at height T and check LHS == RHS.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

# ---------- (A) explicit-formula / trace identity check ----------
T  = 100.0      # height of the test bump
sg = 1.0        # width in r

def h(r):       # even test function, bumps at +-T
    return mp.e**(-(r-T)**2/(2*sg**2)) + mp.e**(-(r+T)**2/(2*sg**2))

def g(u):       # inverse transform of h: (sigma/sqrt(2pi)) * 2 cos(uT) * exp(-sigma^2 u^2/2)
    return (sg/mp.sqrt(2*mp.pi)) * 2*mp.cos(u*T) * mp.e**(-(sg**2)*(u**2)/2)

def W(r):       # archimedean Weil term
    return mp.re(mp.digamma(mp.mpf('0.25') + 1j*r/2)) - mp.log(mp.pi)

# LHS: sum over zeros (h localized at T -> only zeros near T matter; sum a safe index range)
print("  [A] trace identity (Weil explicit formula) at T=%.0f, sigma=%.1f" % (T, sg))
LHS = mp.mpf(0)
for n in range(20, 50):
    g_im = mp.im(mp.zetazero(n))
    LHS += h(g_im) + h(-g_im)   # sum over BOTH conjugate zeros rho = 1/2 +- i gamma
# RHS pieces
poles = h(1j/2) + h(-1j/2)
# prime sum: 2 sum Lambda(n)/sqrt(n) g(log n), n up to where g(log n) negligible (log n <~ 6/sigma)
Nmax = int(mp.e**(7.0/sg))
def vonmangoldt_terms(X):
    X=int(X); sieve=np.ones(X+1,bool); sieve[:2]=False
    for p in range(2,int(X**0.5)+1):
        if sieve[p]: sieve[p*p::p]=False
    out=[]
    for p in np.nonzero(sieve)[0]:
        lp=mp.log(int(p)); pk=int(p)
        while pk<=X:
            out.append((mp.log(pk), lp/mp.sqrt(pk))); pk*=p
    return out
primesum = mp.mpf(0)
for logn, amp in vonmangoldt_terms(Nmax):
    primesum += amp * g(logn)
primesum *= 2
# archimedean integral (1/2pi) int h(r) W(r) dr  (bumps near +-T; integrate a wide range)
arch = mp.quad(lambda r: h(r)*W(r), [-T-8*sg, -T+8*sg]) + mp.quad(lambda r: h(r)*W(r), [T-8*sg, T+8*sg])
arch = arch/(2*mp.pi)
RHS = poles - primesum + arch
print("     LHS  sum_rho h(gamma)      = %s" % mp.nstr(LHS, 10))
print("     RHS  poles - primes + arch = %s" % mp.nstr(RHS, 10))
print("       poles=%s  primesum=%s  arch=%s" % (mp.nstr(poles,4), mp.nstr(primesum,8), mp.nstr(arch,8)))
print("     |LHS-RHS| = %s   rel = %s" % (mp.nstr(abs(LHS-RHS),4), mp.nstr(abs(LHS-RHS)/abs(LHS),4)))

# ---------- (B) Gamma.Gamma = int |S|^2 >= 0 ----------
print("\n  [B] self-intersection Gamma.Gamma = int_{-2d}^{2d}|S|^2 >= 0 (real zeros #1000-1079)")
gam = np.array([float(mp.im(mp.zetazero(n))) for n in range(1000,1080)])
N=len(gam)
def GG(d):
    diff=gam[:,None]-gam[None,:]
    with np.errstate(divide='ignore',invalid='ignore'):
        K=2*np.sin(2*d*diff)/diff
    np.fill_diagonal(K,4*d)
    pair=np.sum(K)
    xi=np.linspace(-2*d,2*d,200000); S=np.sum(np.exp(1j*np.outer(gam,xi)),axis=0)
    integ=np.real(np.sum(np.abs(S)**2)*(xi[1]-xi[0]))
    return pair, integ
for d in [0.5,1.0,2.0]:
    pair,integ=GG(d)
    print("     d=%.1f : Gamma.Gamma(pairsum)=%.4f  =int|S|^2=%.4f  (>=0: %s, rel.err=%.1e)"
          %(d,pair,integ,pair>=0,abs(pair-integ)/abs(integ)))
