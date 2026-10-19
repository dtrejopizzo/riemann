#!/usr/bin/env python3
"""NUMERICAL exploration (float64): Galerkin of a^DH_T on P_T in a Legendre basis P_j(t/T), j<N.
Form as in cert_dh.py. Usage: explore_leg.py sector N T1,T2,..  [comb=DH|zero] """
import sys, numpy as np
from numpy.polynomial import legendre as L
from scipy.special import digamma, eval_legendre
from scipy.linalg import eigh, null_space
K = lambda u: 2*np.exp(-1.5*u)/(-np.expm1(-2*u))
s5 = np.sqrt(5); kap = (np.sqrt(10-2*s5)-2)/(s5-1); CHI = {1:(1,0),2:(0,1),3:(0,-1),4:(-1,0),0:(0,0)}
def bcoef(nmax):
    a = lambda n: CHI[n%5][0]+kap*CHI[n%5][1]; b = {}
    for n in range(2, nmax+1): b[n] = a(n)*np.log(n) - sum(a(d)*b[n//d] for d in range(2, n) if n % d == 0)
    return b
C0 = np.log(5/np.pi) + digamma(0.75)
def legmat(x, N):  # P_j(x) for j<N, rows=x
    P = np.zeros((len(x), N)); P[:, 0] = 1
    if N > 1: P[:, 1] = x
    for j in range(1, N-1): P[:, j+1] = ((2*j+1)*x*P[:, j] - j*P[:, j-1])/(j+1)
    return P
def cmat(u, T, N, xg, wg):  # c_jk(u) = int_{u-T}^{T} P_j(t/T) P_k((t-u)/T) dt, symmetrized
    a, b = u-T, T; t = (b-a)/2*xg + (a+b)/2; w = (b-a)/2*wg
    A = legmat(t/T, N); B = legmat((t-u)/T, N); C = A.T @ (w[:, None]*B)
    return (C + C.T)/2
def form(T, N, comb='DH'):
    nq = N + 20; xg, wg = L.leggauss(nq)
    G = cmat(0.0, T, N, xg, wg)
    ug, uw = L.leggauss(max(400, 3*N)); u = T*(ug+1); uw = T*uw
    Lev = np.zeros((N, N))
    for ui, wi in zip(u, uw): Lev += wi*K(ui)*(G - cmat(ui, T, N, xg, wg))
    tail = sum(2*np.exp(-2*T*(2*k+1.5))/(2*k+1.5) for k in range(200))
    A = (C0+tail)*G + Lev
    nmax = int(np.exp(2*T)); b = bcoef(max(nmax, 2))
    if comb == 'DH':
        for n in range(2, nmax+1):
            if np.log(n) < 2*T: A -= 2*b[n]/np.sqrt(n)*cmat(np.log(n), T, N, xg, wg)
    return G, A
def bottom(T, N, sector, comb='DH'):
    G, A = form(T, N, comb); xg, wg = L.leggauss(N+40); t = T*xg; w = T*wg; P = legmat(xg, N)
    idx = [j for j in range(N) if sector.startswith('full') or j % 2 == 1]
    G = G[np.ix_(idx, idx)]; A = A[np.ix_(idx, idx)]; P = P[:, idx]
    cons = [P.T @ (w*np.sinh(t/2))]
    if sector.startswith('full'): cons.append(P.T @ (w*np.cosh(t/2)))
    if sector.endswith('free'): cons = []
    Z = null_space(np.array(cons)) if cons else np.eye(len(idx))
    e, V = eigh(Z.T @ A @ Z, Z.T @ G @ Z)
    return e[0], dict(zip(idx, Z @ V[:, 0])), e[:4]
if __name__ == '__main__':
    sec, N = sys.argv[1], int(sys.argv[2]); comb = sys.argv[4] if len(sys.argv) > 4 else 'DH'
    for T in [float(x) for x in sys.argv[3].split(',')]:
        e0, v, es = bottom(T, N, sec, comb); print(sec, N, T, comb, 'lowest:', ' '.join('%.6e' % x for x in es), flush=True)

def dump(T, N, sector, path):
    """save the bottom Galerkin vector (Legendre coefficients c_j of G(x)=sum c_j P_j(x), F(t)=G(t/T))"""
    import json
    e0, v, es = bottom(T, N, sector); m = max(abs(x) for x in v.values())
    json.dump({'T': T, 'N': N, 'sector': sector, 'galerkin_float64': e0, 'leg': {int(j): float(c/m) for j, c in v.items()}}, open(path, 'w'))
    print('dumped', path, e0)
