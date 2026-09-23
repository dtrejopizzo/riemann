"""Independent check of the certified value.  Evaluates q_a(F) for the SAME explicit F
as the Fourier-multiplier integral straight from Prop. 12.6's symbol
  Sigma(tau) = sum_pm Re psi(1/4 pm a/2 + i tau/2) - 2 log pi - sum_n 2 c_n n^{-1/2} cos(tau log n),
  q_a(F) = (1/2pi) int_R Sigma(tau) |Fhat(tau)|^2 dtau .
No resolvent/energy decomposition: a completely independent route to the same number.
DIAGNOSTIC-NUMERIC (double precision)."""
import math, numpy as np, mpmath as mp
from scipy.special import psi as digamma
from numpy.polynomial.legendre import leggauss
from xiform import build_Fi
from polyalg import padd, pscal
from cert import GVEC
mp.mp.dps = 60
TSW = 30.0

def fhat_big(coef, Tv, tau):
    out = np.zeros(tau.shape, dtype=complex); P = list(coef); it = 0
    while any(abs(c) > 0 for c in P):
        pT = np.polyval(P[::-1], Tv); pmT = np.polyval(P[::-1], -Tv)
        out = out + (pmT*np.exp(1j*tau*Tv) - pT*np.exp(-1j*tau*Tv))/(1j*tau)**(it+1)
        P = [P[k]*k for k in range(1, len(P))] or [0.0]; it += 1
    return out

def run(astr):
    T = mp.log(2); a = mp.mpf(astr); g = [mp.mpf(x) for x in GVEC[astr]]; m = len(g)-1
    Fs = build_Fi(T, a, m, mp.mp); F = [mp.mpf(0)]
    for i in range(m+1):
        if g[i] != 0: F = padd(F, pscal(Fs[i], g[i], mp.mp), mp.mp)
    f = [float(x) for x in F]; Tf = float(T); af = float(a)
    xq, wq = leggauss(800); ts = Tf*xq; ws = Tf*wq; Fv = np.polyval(f[::-1], ts)
    N2 = float(np.sum(ws*Fv**2))
    def fh(tau):
        o = np.zeros(tau.shape, dtype=complex); big = tau > TSW
        if big.any(): o[big] = fhat_big(f, Tf, tau[big])
        sm = ~big
        if sm.any(): o[sm] = (np.exp(-1j*np.outer(tau[sm], ts))*(ws*Fv)).sum(axis=1)
        return o
    def sigma(tau):
        s = np.zeros_like(tau)
        for sg in (1, -1): s += np.real(digamma(0.25+sg*af/2+0.5j*tau))
        s -= 2*math.log(math.pi)
        for n, l in ((2, math.log(2)), (3, math.log(3))):
            s -= 2*l*(n**af+n**(-af))/math.sqrt(n)*np.cos(tau*math.log(n))
        return s
    edges = np.concatenate([np.linspace(0, TSW, 601)[:-1],
                            np.arange(TSW, 4000.0, 0.5), np.exp(np.linspace(math.log(4000), math.log(1e9), 30001))])
    x2, w2 = leggauss(24); tot = 0.0; par = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        tau = 0.5*(hi-lo)*x2+0.5*(hi+lo); wg = 0.5*(hi-lo)*w2
        A2 = np.abs(fh(tau))**2
        tot += float(np.sum(wg*sigma(tau)*A2)); par += float(np.sum(wg*A2))
    print(f"a={astr}:  Parseval check  (1/2pi)int|Fhat|^2 = {2*par/(2*math.pi):.10f}  vs ||F||^2 = {N2:.10f}")
    print(f"a={astr}:  independent multiplier route  q_a(F)/||F||^2 = {2*tot/(2*math.pi)/N2: .8f}")

if __name__ == '__main__':
    for s in ('0.45', '0.30'): run(s)
