"""Galerkin of a^w_T on P_T with discontinuous piecewise Legendre (degree p-1 per element)
on a mesh graded geometrically toward t = +-T.
Kernel part: sum over element pairs (e,f) of int (delta - C_ef(u)) K(u) du, each u-integral split at the
breakpoints of the pair and done by Gauss-Legendre in u (the integrand is analytic on each piece:
near u=0 the factor (I - C_ee(u)) vanishes linearly and cancels the 1/u of K).
Diagonal: int_0^{h_e} (I - C_ee) K + I*G(h_e), G(s) = int_s^inf K = log coth(s/4) + pi - 2 arctan e^{s/2}.
Arithmetic part: C(log n) exact by Gauss in t on each overlap.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from math import log, sqrt, pi
from scipy.special import digamma
from forms import vonmangoldt

C0 = digamma(0.25) - log(np.pi)
Kf = lambda s: 2 * np.exp(-s / 2) / (-np.expm1(-2 * s))
Gf = lambda s: np.log(1 / np.tanh(s / 4)) + pi - 2 * np.arctan(np.exp(s / 2))

def mesh(T, H, sigma, hmin, extra=()):
    """uniform interior of size <=H, geometric layers of ratio sigma toward +-T down to hmin."""
    lay = [0.0]; h = hmin
    while lay[-1] + h < H:
        lay.append(lay[-1] + h); h /= sigma
    L = lay[-1]  # layer thickness
    m = max(1, int(np.ceil((2 * T - 2 * L) / H)))
    inner = np.linspace(-T + L, T - L, m + 1)
    left = -T + np.array(lay); right = T - np.array(lay)[::-1]
    x = np.unique(np.concatenate([left, inner, right, np.array(extra)]))
    x = x[np.diff(np.concatenate([[-np.inf], x])) > 1e-14]
    return x

class Basis:
    def __init__(self, x, p):
        self.x = x; self.p = p; self.E = len(x) - 1; self.N = self.E * p
        self.h = np.diff(x)
    def ev(self, e, t):
        """values (len t, p) of the p orthonormal Legendre functions of element e."""
        a, b = self.x[e], self.x[e + 1]
        s = (2 * t - a - b) / (b - a)
        return legvander(s, self.p - 1) * np.sqrt((2 * np.arange(self.p) + 1) / (b - a))

def shiftblock(B, e, f, u, q):
    """C_ef(u)_{ij} = int phi_i^e(t) phi_j^f(t+u) dt (exact for q >= p)."""
    a = max(B.x[e], B.x[f] - u); b = min(B.x[e + 1], B.x[f + 1] - u)
    if b <= a: return None
    xg, wg = leggauss(q)
    t = (b - a) / 2 * xg + (a + b) / 2; w = wg * (b - a) / 2
    return (B.ev(e, t) * w[:, None]).T @ B.ev(f, t + u)

def build_arch(B, T, qu=None):
    p = B.p; N = B.N; E = B.E
    qu = qu or (2 * p + 16)
    xu, wu = leggauss(qu)
    M = np.zeros((N, N))
    sl = lambda e: slice(e * p, (e + 1) * p)
    for e in range(E):
        for f in range(e, E):
            ae, be, af, bf = B.x[e], B.x[e + 1], B.x[f], B.x[f + 1]
            br = sorted(set([max(0.0, af - be), af - ae, bf - be, bf - ae]))
            br = [b for b in br if b >= max(0.0, af - be) - 1e-15]
            blk = np.zeros((p, p)); diag = np.zeros((p, p))
            for lo, hi in zip(br[:-1], br[1:]):
                if hi - lo < 1e-15: continue
                us = (hi - lo) / 2 * xu + (hi + lo) / 2; ws = wu * (hi - lo) / 2
                for uk, wk in zip(us, ws):
                    C = shiftblock(B, e, f, uk, p + 1)
                    if C is None: continue
                    if e == f:
                        blk += wk * Kf(uk) * (np.eye(p) - (C + C.T) / 2)
                    else:
                        blk -= wk * Kf(uk) * C
            if e == f:
                M[sl(e), sl(e)] += blk + Gf(B.h[e]) * np.eye(p) + C0 * np.eye(p)
            else:
                # c_F(u) symmetric part: F_e(t)F_f(t+u) contributes to (e,f) and (f,e) with 1/2 each
                M[sl(e), sl(f)] += blk / 2; M[sl(f), sl(e)] += blk.T / 2
    return M

def corr_full(B, u):
    p = B.p; N = B.N
    C = np.zeros((N, N))
    for e in range(B.E):
        lo = np.searchsorted(B.x, B.x[e] + u, 'right') - 1
        hi = np.searchsorted(B.x, B.x[e + 1] + u, 'left')
        for f in range(max(lo, 0), min(hi, B.E)):
            c = shiftblock(B, e, f, u, p + 1)
            if c is not None:
                C[e*p:(e+1)*p, f*p:(f+1)*p] += c
    return (C + C.T) / 2

def constraints(B):
    xg, wg = leggauss(B.p + 30)
    rows = np.zeros((2, B.N))
    for e in range(B.E):
        a, b = B.x[e], B.x[e + 1]
        t = (b - a) / 2 * xg + (a + b) / 2; w = wg * (b - a) / 2
        P = B.ev(e, t)
        rows[0, e*B.p:(e+1)*B.p] = P.T @ (w * np.exp(t / 2))
        rows[1, e*B.p:(e+1)*B.p] = P.T @ (w * np.exp(-t / 2))
    _, _, Vt = np.linalg.svd(rows)
    return Vt[2:].T

def build(T, B, weights):
    """weights: dict name -> function(ns, v, T) -> w. Returns Z, Arch (on P_T), dict of reduced forms."""
    Z = constraints(B)
    A = build_arch(B, T)
    ns = [n for n in range(2, int(np.ceil(np.exp(2 * T))) + 1) if log(n) < 2 * T and vonmangoldt(n) > 0]
    ns = np.array(ns); v = np.array([2 * vonmangoldt(n) / sqrt(n) for n in ns])
    W = {k: f(ns, v, T) for k, f in weights.items()}
    S = {k: np.zeros_like(A) for k in W}
    for i, n in enumerate(ns):
        C = corr_full(B, log(n))
        for k in W: S[k] += W[k][i] * C
    sym = lambda X: (X + X.T) / 2
    Ar = sym(Z.T @ A @ Z)
    return Z, Ar, {k: sym(Z.T @ S[k] @ Z) for k in S}

def _evb(B, e, t):
    a, b = B.x[e], B.x[e + 1]
    s = (2 * t - a - b) / (b - a)
    return legvander(s, B.p - 1) * np.sqrt((2 * np.arange(B.p) + 1) / (b - a))

def build_arch_fast(B, T, qu=None):
    """same as build_arch, vectorized over the u-nodes of each pair."""
    p = B.p; N = B.N; E = B.E
    qu = qu or (2 * p + 16)
    xu, wu = leggauss(qu); xt, wt = leggauss(p + 1)
    M = np.zeros((N, N)); I = np.eye(p)
    for e in range(E):
        for f in range(e, E):
            ae, be, af, bf = B.x[e], B.x[e + 1], B.x[f], B.x[f + 1]
            u0 = max(0.0, af - be)
            br = sorted(set([u0, af - ae, bf - be, bf - ae]))
            br = [b for b in br if b >= u0]
            us = []; ws = []
            for lo, hi in zip(br[:-1], br[1:]):
                if hi - lo < 1e-15: continue
                us.append((hi - lo) / 2 * xu + (hi + lo) / 2); ws.append(wu * (hi - lo) / 2)
            us = np.concatenate(us); ws = np.concatenate(ws) * Kf(np.concatenate(us) if False else us)
            a = np.maximum(ae, af - us); b = np.minimum(be, bf - us)
            ok = b > a; us, ws, a, b = us[ok], ws[ok], a[ok], b[ok]
            t = (b - a)[:, None] / 2 * xt[None, :] + ((a + b) / 2)[:, None]
            wq = (ws * (b - a) / 2)[:, None] * wt[None, :]
            Pe = _evb(B, e, t); Pf = _evb(B, f, t + us[:, None])
            C = np.einsum('uq,uqi,uqj->ij', wq, Pe, Pf)
            if e == f:
                M[e*p:(e+1)*p, e*p:(e+1)*p] += ws.sum() * I - (C + C.T) / 2 + (Gf(B.h[e]) + C0) * I
            else:
                M[e*p:(e+1)*p, f*p:(f+1)*p] -= C / 2; M[f*p:(f+1)*p, e*p:(e+1)*p] -= C.T / 2
    return M
build_arch_slow = build_arch
build_arch = build_arch_fast
