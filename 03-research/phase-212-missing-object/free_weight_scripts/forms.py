"""Galerkin matrices of a^w_T on P_T (Paper 47, eq:form / eq:Aform / lem:K).
a^w_T(F) = C0||F||^2 + int_0^inf (c_F(0)-c_F(u)) K(u) du - sum_n w_n c_F(log n),
c_F(u)=int F(t)F(t+u)dt, K(u)=2e^{3u/2}/(e^{2u}-1), C0=psi(1/4)-log pi.
Basis: orthonormal Legendre on [-T,T]; P_T = {A(F)=B(F)=0}, A=int F e^{t/2}, B=int F e^{-t/2}.
"""
import numpy as np
from numpy.polynomial.legendre import leggauss, legvander
from math import log, sqrt
from scipy.special import digamma

C0 = digamma(0.25) - log(np.pi)

def vonmangoldt(n):
    for p in range(2, n + 1):
        if n % p == 0:
            m = n
            while m % p == 0:
                m //= p
            return log(p) if m == 1 else 0.0
    return 0.0

def basis(T, N, t):
    V = legvander(t / T, N - 1)
    return V * np.sqrt((2 * np.arange(N) + 1) / (2 * T))

def corr(T, N, u):
    """symmetrized matrix c_ij(u) (exact Gauss on overlap)."""
    x, wq = leggauss(N + 4)
    a, b = -T, T - u
    t = (b - a) / 2 * x + (a + b) / 2
    w = wq * (b - a) / 2
    P = basis(T, N, t); Q = basis(T, N, t + u)
    C = (P * w[:, None]).T @ Q
    return (C + C.T) / 2

def build(T, N, nu=240):
    I = np.eye(N)
    x, wq = leggauss(nu)
    u = T * (x + 1); wu = wq * T
    K = lambda s: 2 * np.exp(-s / 2) / (1 - np.exp(-2 * s))
    M0 = C0 * I
    for uk, wk in zip(u, wu):
        M0 += wk * K(uk) * (I - corr(T, N, uk))
    # tail int_{2T}^inf K = log coth(T/2)+pi-2 arctan e^T  (thm:S(iii))
    M0 += (np.log(1 / np.tanh(T / 2)) + np.pi - 2 * np.arctan(np.exp(T))) * I
    ns = [n for n in range(2, int(np.ceil(np.exp(2 * T))) + 1) if log(n) < 2 * T]
    Cn = [corr(T, N, log(n)) for n in ns]
    v = np.array([2 * vonmangoldt(n) / sqrt(n) for n in ns])
    xg, wg = leggauss(N + 40)
    t = T * xg; ww = wg * T
    P = basis(T, N, t)
    A = P.T @ (ww * np.exp(t / 2)); B = P.T @ (ww * np.exp(-t / 2))
    Uc, s, Vt = np.linalg.svd(np.vstack([A, B]))
    Z = Vt[2:].T  # orthonormal basis of P_T in coefficient space
    M0 = Z.T @ M0 @ Z
    Cn = [Z.T @ c @ Z for c in Cn]
    sym = lambda X: (X + X.T) / 2
    return sym(M0), [sym(c) for c in Cn], np.array(ns), v

def lam(M0, Cn, w):
    M = M0 - sum(wi * c for wi, c in zip(w, Cn))
    return np.linalg.eigvalsh(M)
