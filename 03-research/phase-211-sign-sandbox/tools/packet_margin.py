"""Packet margin m(tau) - P^rho_T(tau) on the high range (phase 211).  NUMERICAL tool.

m(tau) = Re psi(1/4 + i tau/2) - log pi  (archimedean symbol; m(0) = C_0 of galerkin_mp.py),
P^rho_T(tau) = sum_{n<N} v_n rho(log n / T) cos(tau log n),  v_n = 2 Lambda(n)/sqrt(n),  N = e^{2T},
rho = normalised autocorrelation of the profile beta on [-1,1].
Grid of spacing <= 1/(20T) on [2 pi N (1+delta), tau_max], then local refinement of the
smallest grid values of m - P (bounded Brent search on a +-1/(10T) neighbourhood).
"""
import numpy as np, math, sys
from scipy.special import psi
from scipy.optimize import minimize_scalar, brentq
from scipy.signal import fftconvolve

def m_sym(t):
    t = np.asarray(t, dtype=float)
    return psi(0.25 + 0.5j * t).real - math.log(math.pi)

def comb(T):
    N = math.exp(2 * T); out = []
    for n in range(2, int(N) + 1):
        if math.log(n) >= 2 * T: break
        k = n; p = None
        for q in range(2, int(math.isqrt(n)) + 1):
            if n % q == 0: p = q; break
        if p is None: p = n
        while k % p == 0: k //= p
        if k == 1: out.append((n, p, 2 * math.log(p) / math.sqrt(n)))
    return out

# ---- profiles on [-1,1]
XS = np.linspace(-1, 1, 40001); DX = XS[1] - XS[0]
def _bump(x, w):
    y = np.zeros_like(x); i = np.abs(x) < w; y[i] = np.exp(-1 / (1 - (x[i] / w) ** 2)); return y
def beta_ind():
    eps = 0.05; core = (np.abs(XS) <= 1 - eps).astype(float)
    k = _bump(XS, eps); k /= k.sum(); return fftconvolve(core, k, mode='same')
PROFILES = {
    'ind': beta_ind,                               # 1_[-0.95,0.95] * mollifier(0.05): C_c^inf, rho ~ triangle
    'cos2': lambda: np.cos(np.pi * XS / 2) ** 2,   # cos^2(pi x/2) on [-1,1]
    'bump': lambda: _bump(XS, 1.0),                # exp(-1/(1-x^2))
}
def rho_fn(name):
    b = PROFILES[name](); a = fftconvolve(b, b[::-1]) * DX; a /= a.max()
    us = (np.arange(a.size) - (b.size - 1)) * DX
    return lambda u: np.interp(np.abs(u), us[b.size - 1:], a[b.size - 1:], right=0.0), b

def Pfun(T, rho):
    C = comb(T); ln = np.array([math.log(n) for n, _, _ in C]); w = np.array([v for _, _, v in C]) * rho(ln / T)
    def P(t):
        t = np.atleast_1d(np.asarray(t, float)); return np.cos(np.outer(t, ln)) @ w
    return P, ln, w, C

def scan(T, name, delta=0.1, tau_max=None, chunk=2_000_000, top=40):
    rho, _ = rho_fn(name); P, ln, w, C = Pfun(T, rho); N = math.exp(2 * T)
    lo = 2 * math.pi * N * (1 + delta); h = 1 / (20 * T)
    S = float(w.sum()); tstar = math.exp(brentq(lambda L: float(m_sym(math.exp(L))) - S, 0, 700))
    hi = tau_max or max(lo + 1, tstar)   # beyond tstar: m - P >= m - S >= 0 (P <= S since weights >= 0)
    best = []  # (value, tau)
    a = lo
    while a < hi:
        t = a + h * np.arange(chunk); t = t[t <= hi]
        if t.size == 0: break
        d = m_sym(t) - P(t)
        idx = np.argpartition(d, min(top, d.size - 1))[:top]
        best += list(zip(d[idx], t[idx])); best = sorted(best)[:top]
        a = t[-1] + h
    ref = []
    for _, t0 in best:
        r = minimize_scalar(lambda s: float(m_sym(s) - P(s)[0]), bounds=(t0 - 0.1 / T, t0 + 0.1 / T), method='bounded', options={'xatol': 1e-10})
        ref.append((r.fun, r.x))
    ref.sort()
    return dict(T=T, profile=name, N=N, lo=lo, hi=hi, min=ref[0][0], argmin=ref[0][1],
                P_at=float(P(ref[0][1])[0]), m_at=float(m_sym(ref[0][1])), Sigma_rho=float(w.sum()), nterms=len(w),
                m_lo=float(m_sym(lo)), tstar=tstar)

if __name__ == '__main__':
    T = float(sys.argv[1]); name = sys.argv[2]; delta = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
    r = scan(T, name, delta)
    print(' '.join(f"{k}={v:.6g}" if isinstance(v, float) else f"{k}={v}" for k, v in r.items()))
