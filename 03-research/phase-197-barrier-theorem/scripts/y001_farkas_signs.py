#!/usr/bin/env python3
"""BARRIER_Y_001 (NUMÉRICO, Galerkin, not certified): signs of c_{F*}(log q) on the top layer
Q = {prime powers sqrt N <= q < N}, N = e^{2T}, and the deleted-comb bottoms lambda_A(T; Lambda_Q).
Form: P47 eq:Aform, Legendre Galerkin in x-space (copied from phase-186 r046_X.form_x, extended to signed combs).
Usage: python3 y001_farkas_signs.py [M list]"""
import sys, itertools, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma
from scipy.integrate import quad
C0 = float(digamma(0.25)) - np.log(np.pi)

def pp(nmax):
    out = []
    for n in range(2, nmax + 1):
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, p))
    return out

def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))

class Win:
    def __init__(s, T, M, nu=48, npan=24):
        s.T, s.M = T, M; s.xg, s.wg = NL.leggauss(M + 4)
        I = np.eye(M); A = np.zeros((M, M)); ug, uw = NL.leggauss(nu); edges = np.linspace(0, 2 * T, npan + 1)
        for lo, hi in zip(edges[:-1], edges[1:]):
            for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
                A += (I - s.C(u)) * (K(u) * w)
        A += I * (quad(K, 2 * T, np.inf)[0] + C0)
        s.A0 = (A + A.T) / 2
        xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
        ta, tb = (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2)
        _, _, Vt = np.linalg.svd(np.array([ta, tb])); s.Z = Vt[2:].T
        s.N = np.exp(2 * T); s.cont = [(n, p) for n, p in pp(int(s.N) + 1) if np.log(n) < 2 * T]
        s.Cn = {n: s.C(np.log(n)) for n, _ in s.cont}
    def C(s, u):
        T, M = s.T, s.M; lo, hi = -T + u, T
        if hi <= lo: return np.zeros((M, M))
        y = (hi + lo) / 2 + (hi - lo) / 2 * s.xg; w = (hi - lo) / 2 * s.wg
        Mx = (legb(T, M, y) * w) @ legb(T, M, y - u).T; return (Mx + Mx.T) / 2
    def bottom(s, a):   # a: dict n -> a(n) (comb values); v_n = 2 a(n)/sqrt n
        A = s.A0.copy()
        for n, _ in s.cont: A -= 2 * a.get(n, 0.0) / np.sqrt(n) * s.Cn[n]
        ev, V = np.linalg.eigh(s.Z.T @ A @ s.Z); return ev, s.Z @ V[:, 0]

def run(T, Ms):
    for M in Ms:
        W = Win(T, M); Lam = {n: np.log(p) for n, p in W.cont}
        ev, h = W.bottom(Lam)
        # parity of h*: coefficients of odd Legendre vs even
        pe, po = np.sum(h[0::2] ** 2), np.sum(h[1::2] ** 2)
        top = [(n, p) for n, p in W.cont if n >= np.sqrt(W.N)]
        print(f"T={T:.6f} N={W.N:.3f} M={M}: lamA~{ev[0]:+.3e} gap {ev[1]:+.3e}; parity even/odd mass {pe:.3f}/{po:.3f}; contacts {[n for n,_ in W.cont]}; top layer {[n for n,_ in top]}")
        for n, p in top:
            c = h @ W.Cn[n] @ h; k = round(np.log(n) / np.log(p)); g = 2 * c * np.log(n) / np.sqrt(n)
            print(f"   q={n:3d}: c(log q)={c:+.5e}  g(q)=2c log q/sqrt q={g:+.5e}  deletion bound lamA+g={ev[0]+g:+.3e}")
        # deleted combs Lambda_Q (single-level deletions) + two-level paths for small p
        for r in range(1, len(top) + 1):
            for Q in itertools.combinations([n for n, _ in top], r):
                a = dict(Lam); [a.__setitem__(q, 0.0) for q in Q]
                print(f"   lambda_A(T;Lambda minus {Q}) = {W.bottom(a)[0][0]:+.4e}")
        bypr = {}
        for n, p in top: bypr.setdefault(p, []).append(n)
        for p, qs in bypr.items():
            for i, j in itertools.combinations(sorted(qs), 2):   # path: b drops at q_i, returns at q_j
                a = dict(Lam); a[i] = 0.0; a[j] = 2 * Lam[j]
                print(f"   two-level path p={p}: -e_{i}+e_{j}: lambda_A = {W.bottom(a)[0][0]:+.4e};  g({j})-g({i}) = "
                      f"{2*(h@W.Cn[j]@h)*np.log(j)/np.sqrt(j) - 2*(h@W.Cn[i]@h)*np.log(i)/np.sqrt(i):+.4e}")

if __name__ == '__main__':
    Ms = [int(x) for x in (sys.argv[1] if len(sys.argv) > 1 else '40,56').split(',')]
    for T in (0.5 * np.log(3), 0.5 * np.log(5) + 0.01, 0.9, 1.0, np.log(3) - 1e-6, 0.5 * np.log(11) - 0.01):
        run(T, Ms)
