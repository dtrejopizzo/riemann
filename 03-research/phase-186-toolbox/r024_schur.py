#!/usr/bin/env python3
"""R186_024 — 4x4 Schur of edge modes along T in [1/2 log2, 1/2 log5].

Form (Paper 47, thm:A / lem:K / thm:S(iii), def. eq:form):
  a_T(F) = C_0||F||^2 + int_0^oo (||F||^2 - C_F(u)) K(u) du - sum_{n in N_T} v_n C_F(log n),
  C_0 = psi(1/4) - log pi,  K(u) = 2 e^{-u/2}/(1-e^{-2u}),  v_n = 2 Lambda(n)/sqrt n,
  N_T = {n >= 2 : log n < 2T},  C_F(u) = int F(t) F(t-u) dt,
  P_T = {F in L^2(I_T): int F e^{+-t/2} = 0}.
Everything is computed in x-space (autocorrelations): no oscillatory integrand, the
precision is set by piecewise Gauss quadrature (exact on polynomials) and the
numeric type (float64, or mpmath's mpf if prec > 0).

Decomposition: I_T = union of blocks B (orbits of the log 2 shift):
  T < log2 : J=(-T,T-l), M=(T-l,l-T), J'=(l-T,T)           (3 blocks, dim E = 4)
  T >= log2: (-T,T-2l),(T-2l,l-T),(l-T,T-l),(T-l,2l-T),(2l-T,T)  (5 blocks, dim E = 8)
  V = (+) {h in L^2(B): int_B h e^{+-t/2} = 0},  E = P_T (-) V = span{e^{+-t/2} 1_B} cap P_T.
Galerkin basis: orthonormal Legendre of degree < N on each block (allows jumps).
Control: partition into 3 equal blocks (same algebra, blocks with no arithmetic meaning).

Usage:  python3 r024_schur.py [N=14] [prec=0] [T1,T2,...]
"""
import sys, numpy as np, mpmath as mp
from numpy.polynomial import legendre as L

LOG2 = np.log(2.0)

# ---------- backend ----------
class BE:
    def __init__(self, prec):
        self.mp = prec > 0
        if self.mp: mp.mp.dps = prec
    def num(self, x): return mp.mpf(x) if self.mp else float(x)
    def arr(self, xs): return np.array([self.num(x) for x in xs], dtype=object if self.mp else float)
    def exp(self, a):
        return np.vectorize(mp.exp, otypes=[object])(a) if self.mp else np.exp(a)
    def sqrt(self, x): return mp.sqrt(x) if self.mp else np.sqrt(x)
    def log(self, x): return mp.log(x) if self.mp else np.log(x)
    def zeros(self, *sh):
        return np.full(sh, self.num(0), dtype=object) if self.mp else np.zeros(sh)
    def eye(self, n):
        Z = self.zeros(n, n)
        for i in range(n): Z[i, i] = self.num(1)
        return Z
    def gauss(self, n):
        """Gauss-Legendre nodes/weights on [-1,1] (Newton in mp starting from float64)."""
        x, w = L.leggauss(n)
        if not self.mp: return x, w
        xs, ws = [], []
        for xi in x:
            z = mp.mpf(xi)
            for _ in range(6):
                p, dp = mp.legendre(n, z), mp.diff(lambda t: mp.legendre(n, t), z)
                z -= p / dp
            dp = mp.diff(lambda t: mp.legendre(n, t), z)
            xs.append(z); ws.append(2 / ((1 - z**2) * dp**2))
        return np.array(xs, dtype=object), np.array(ws, dtype=object)
    def eigh(self, A):
        if not self.mp: return np.linalg.eigh(A)
        M = mp.matrix(A.tolist()); E, Q = mp.eigsy(M)
        ev = np.array([E[i] for i in range(M.rows)], dtype=object)
        V = np.array(Q.tolist(), dtype=object)
        o = np.argsort([float(e) for e in ev]); return ev[o], V[:, o]
    def solve(self, A, B):
        if not self.mp: return np.linalg.solve(A, B)
        Ai = np.array(mp.inverse(mp.matrix(A.tolist())).tolist(), dtype=object); return Ai @ B
    def nulls(self, C):
        """orthonormal basis of the kernel of C (rows = constraints), via eigh of C^T C."""
        n = C.shape[1]; ev, V = self.eigh(C.T @ C)
        k = C.shape[0]; return V[:, : n - k]   # the k largest eigenvalues are the nonzero ones
    def f(self, x): return float(x)

# ---------- geometry ----------
def blocks(T, kind='orbit'):
    l = LOG2
    if kind.startswith('equal'):          # 'equal' = 3 equal blocks, 'equalK' = K equal blocks
        k = int(kind[5:]) if len(kind) > 5 else 3
        e = np.linspace(-T, T, k + 1); return [(e[i], e[i + 1]) for i in range(k)]
    if T < l:
        return [(-T, T - l), (T - l, l - T), (l - T, T)]
    assert T < 1.5 * l
    e = [-T, T - 2 * l, l - T, T - l, 2 * l - T, T]
    return [(e[i], e[i + 1]) for i in range(5)]

def contacts(T):
    from sympy import factorint
    out = []
    for n in range(2, 200):
        if np.log(n) >= 2 * T: break
        f = factorint(n)
        if len(f) == 1: out.append((n, float(np.log(list(f)[0]))))
    return out

# ---------- basis and form ----------
def legvals(be, u, N):
    """P_k(u), k<N, by recurrence (u array)."""
    P = [np.ones_like(u) if not be.mp else np.full(u.shape, be.num(1), dtype=object), u.copy()]
    for k in range(1, N - 1):
        P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:N])

def basis_on(be, blk, y, N):
    """phi_k(y) = sqrt((2k+1)/(b-a)) P_k(map(y)), k<N, with y inside the block."""
    a, b = blk; u = (2 * y - (a + b)) / (b - a)
    P = legvals(be, u, N)
    nrm = be.arr([np.sqrt((2 * k + 1) / (b - a)) for k in range(N)])
    return P * nrm[:, None]

def build(T, N, be, kind='orbit', nu=24):
    """Gram A of a_T, blocks, Tate (a,b) per block, archimedean part A0 and primes."""
    B = blocks(T, kind); nb = len(B); dim = nb * N
    xg, wg = be.gauss(N + 2); xT, wT = be.gauss(40)
    Bn = [(be.num(a), be.num(b)) for a, b in B]
    idx = [np.arange(i * N, (i + 1) * N) for i in range(nb)]
    # autocorrelation C(u)_{ij} = int phi_i(y) phi_j(y-u) dy, bilinear, then symmetrized
    def C(u):
        M = be.zeros(dim, dim)
        for p, (a1, b1) in enumerate(Bn):
            for q, (a2, b2) in enumerate(Bn):
                lo, hi = max(a1, a2 + u), min(b1, b2 + u)
                if hi <= lo: continue
                y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
                F1 = basis_on(be, (a1, b1), y, N); F2 = basis_on(be, (a2, b2), y - u, N)
                M[np.ix_(idx[p], idx[q])] = (F1 * w) @ F2.T
        return (M + M.T) / 2
    I = be.eye(dim)
    # segments in u: differences of block endpoints
    ends = sorted(set(float(e) for bl in B for e in bl))
    br = sorted(set(round(abs(x - y), 14) for x in ends for y in ends if abs(x - y) > 1e-13))
    br = [be.num(0)] + [be.num(x) for x in br]
    ug, uw = be.gauss(nu)
    A0 = be.zeros(dim, dim)
    for lo, hi in zip(br[:-1], br[1:]):
        us = (hi + lo) / 2 + (hi - lo) / 2 * ug; ws = (hi - lo) / 2 * uw
        for u, w in zip(us, ws):
            K = 2 * be.exp(-u / 2) / (1 - be.exp(-2 * u)) if be.mp else 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))
            A0 = A0 + (I - C(u)) * (K * w)
    Tn = be.num(T)
    if be.mp:
        tail = mp.log(mp.coth(Tn / 2)) + mp.pi - 2 * mp.atan(mp.exp(Tn)); C0 = mp.digamma(mp.mpf(1) / 4) - mp.log(mp.pi)
    else:
        tail = np.log(1 / np.tanh(T / 2)) + np.pi - 2 * np.arctan(np.exp(T)); C0 = float(mp.digamma(0.25)) - np.log(np.pi)
    A0 = A0 + I * (tail + C0)
    Pr = be.zeros(dim, dim); Pn = {}
    for n, lam in contacts(T):
        v = 2 * be.num(lam) / be.sqrt(be.num(n)); Pn[n] = -v * C(be.log(be.num(n))); Pr = Pr + Pn[n]
    # Tate per block
    ta = be.zeros(dim); tb = be.zeros(dim)
    for p, (a1, b1) in enumerate(Bn):
        y = (a1 + b1) / 2 + (b1 - a1) / 2 * xT; w = (b1 - a1) / 2 * wT
        F = basis_on(be, (a1, b1), y, N)
        ta[idx[p]] = (F * w) @ be.exp(y / 2); tb[idx[p]] = (F * w) @ be.exp(-y / 2)
    return dict(A=A0 + Pr, A0=A0, Pr=Pr, Pn=Pn, ta=ta, tb=tb, idx=idx, B=B, dim=dim)

def analyse(d, be):
    A, ta, tb, idx, dim = d['A'], d['ta'], d['tb'], d['idx'], d['dim']
    Cg = np.array([ta, tb])
    Z = be.nulls(Cg)                                   # P_T
    # V: kernel of Tate per block
    cols = []
    for ix in idx:
        n = be.nulls(np.array([ta[ix], tb[ix]])); Bm = be.zeros(dim, n.shape[1]); Bm[ix] = n; cols.append(Bm)
    Zv = np.hstack(cols)
    # E = span{e^{+-t/2} 1_B} cap P_T (coordinates: restrictions of ta, tb to each block)
    Y = []
    for ix in idx:
        for t in (ta, tb):
            y = be.zeros(dim); y[ix] = t[ix]; Y.append(y)
    Y = np.array(Y).T; ce = be.nulls(Cg @ Y); E = Y @ ce
    ev, V = be.eigh(E.T @ E); keep = [i for i in range(len(ev)) if be.f(ev[i]) > 1e-10 * be.f(ev[-1])]
    ev, V = ev[keep], V[:, keep]
    E = E @ V / np.sqrt(ev) if not be.mp else E @ V / np.array([mp.sqrt(e) for e in ev], dtype=object)
    Gvv, Gee, Gve = Zv.T @ A @ Zv, E.T @ A @ E, Zv.T @ A @ E
    out = {}
    evW, VW = be.eigh(Z.T @ A @ Z); out['lamW'] = evW[0]; hstar = Z @ VW[:, 0]
    out['projE'] = sum(be.f(x) ** 2 for x in (E.T @ hstar))          # mass of h* in E
    # archimedean coupling between blocks on V: ||Zv^T (A0 - diag_blocks(A0)) Zv||
    Ad = be.zeros(dim, dim)
    for ix in idx: Ad[np.ix_(ix, ix)] = d['A0'][np.ix_(ix, ix)]
    out['coup'] = max(abs(be.f(x)) for x in be.eigh(Zv.T @ (d['A0'] - Ad) @ Zv)[0])
    out['sec_inf'] = []
    for ix in idx:
        n = be.nulls(np.array([ta[ix], tb[ix]])); out['sec_inf'].append(be.eigh(n.T @ d['A0'][np.ix_(ix, ix)] @ n)[0][0])
    out['c'] = be.eigh(Gvv)[0][0]
    out['c_inf'] = be.eigh(Zv.T @ d['A0'] @ Zv)[0][0]
    out['normP_V'] = max(abs(be.f(x)) for x in be.eigh(Zv.T @ d['Pr'] @ Zv)[0])
    Kmat = be.solve(Gvv, Gve)
    S = Gee - Gve.T @ Kmat
    out['S'] = be.eigh((S + S.T) / 2)[0] if E.shape[1] else be.arr([0, 0])
    out['Gee'] = be.eigh(Gee)[0] if E.shape[1] else be.arr([0])
    out['normK'] = be.sqrt(be.eigh(Kmat.T @ Kmat)[0][-1]) if E.shape[1] else be.num(0)
    out['sector'] = []
    for ix in idx:
        n = be.nulls(np.array([ta[ix], tb[ix]])); out['sector'].append(be.eigh(n.T @ A[np.ix_(ix, ix)] @ n)[0][0])
    out['dimE'] = E.shape[1]
    return out

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    prec = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    Ts = [float(t) for t in sys.argv[3].split(',')] if len(sys.argv) > 3 else \
        [0.36, 0.40, 0.44, 0.48, 0.52, 0.5 * np.log(3), 0.58, 0.62, 0.66, 0.69,
         0.70, 0.72, 0.75, 0.78, 0.5 * np.log(5)]
    be = BE(prec)
    print(f"# N={N} prec={prec}  columnas: T dimE lamW c=minW|V c_inf(V,sin primos) ||P|V|| lamS lam2S minGee ||K|| sectores | control3eq: lamW c lamS")
    for T in Ts:
        d = build(T, N, be); o = analyse(d, be)
        line = (f"{T:.4f} {o['dimE']} {be.f(o['lamW']):+.3e} {be.f(o['c']):.4f} {be.f(o['c_inf']):+.4f} "
                f"{o['normP_V']:.3f} {be.f(o['S'][0]):+.3e} {be.f(o['S'][1]):+.3e} {be.f(o['Gee'][0]):.4f} "
                f"{be.f(o['normK']):.3f} " + "/".join(f"{be.f(s):.3f}" for s in o['sector']) + f" projE={o['projE']:.3f} coup={o['coup']:.3f}")
        if T < LOG2 and not be.mp:
            d2 = build(T, N, be, kind='equal'); o2 = analyse(d2, be)
            line += f" | {be.f(o2['lamW']):+.3e} {be.f(o2['c']):.4f} {be.f(o2['S'][0]):+.3e}"
        print(line, flush=True)

def scan_partitions(N, Ts, ks=(3, 5, 7, 9)):
    """c(T) and lamS(T) for partitions into k equal blocks (dim E = 2k-2)."""
    be = BE(0)
    print(f"# equal partitions, N={N}: T | k: lamW c lamS ||K|| ...")
    for T in Ts:
        line = f"{T:.4f}"
        for k in ks:
            d = build(T, N, be, kind=f'equal{k}'); o = analyse(d, be)
            line += (f" | k={k}: {be.f(o['lamW']):+.2e} c={be.f(o['c']):.4f} c_inf={be.f(o['c_inf']):.3f} "
                     f"|P|={o['normP_V']:.3f} lamS={be.f(o['S'][0]):+.2e} K={be.f(o['normK']):.2f} sec={min(be.f(x) for x in o['sector']):.3f} "
                     f"sec_inf={min(be.f(x) for x in o['sec_inf']):.3f} coup={o['coup']:.3f} projE={o['projE']:.3f}")
        print(line, flush=True)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'scan':
        scan_partitions(int(sys.argv[2]), [float(t) for t in sys.argv[3].split(',')])
    else:
        main()
