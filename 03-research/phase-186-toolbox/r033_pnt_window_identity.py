#!/usr/bin/env python3
"""R186_033 - window identity "PNT error + K_1 energy" on the primitive class, and log-convexity test.

Forma (Paper 47 thm:A / eq:Aform / lem:K):
  a_T(F) = C_0||F||^2 + int_0^oo K(u)(C_F(0) - C_F(u)) du - sum_{n in N_T} v_n C_F(log n),
  K(u) = 2e^{-u/2}/(1-e^{-2u}) = 2e^{-u/2} + K_1(u),  K_1 = 2e^{-5u/2}/(1-e^{-2u}) >= 0.
Lemma 1 (R186_033): for F in P_T (A(F)=B(F)=0, i.e. int C_F(u) cosh(u/2) du = 0),
  a_T(F) = (C_0+4) C_F(0) + E_psi(F) + Lev_{K_1}(C_F),
  E_psi(F) = 2 int_1^{e^{2T}} x^{-1/2} C_F(log x) d(x - psi(x))
           = 2 int_0^{2T} C_F(u) e^{u/2} du - sum_{n<e^{2T}} (2 Lambda(n)/sqrt n) C_F(log n).
This script: (1) verifies the identity at the minimizer h*_T (Legendre Galerkin, N modes), (2) splits
a_T(h*) into the three terms, (3) tests convexity of log lambda_A in T, e^{2T}, e^{4T}, A_T.
Usage: python3 r033_pnt_window_identity.py [N=60]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma

C0 = digamma(0.25) - np.log(np.pi)
def K(u):  return 2*np.exp(-u/2)/(1-np.exp(-2*u))
def K1(u): return 2*np.exp(-5*u/2)/(1-np.exp(-2*u))
def tau(r):  return np.log(1/np.tanh(r/4)) + np.pi - 2*np.arctan(np.exp(r/2))      # int_r^oo K
def tau1(r): return tau(r) - 4*np.exp(-r/2)                                        # int_r^oo K_1

def contacts(T):
    out = []
    for n in range(2, 2000):
        if np.log(n) >= 2*T: break
        p = next(q for q in range(2, n+1) if n % q == 0); m = n
        while m % p == 0: m //= p
        if m == 1: out.append((n, np.log(n), 2*np.log(p)/np.sqrt(n)))
    return out

class Win:
    def __init__(self, T, N=60, nu=400):
        self.T, self.N = T, N
        self.xt, self.wt = NL.leggauss(N+24); self.xu, self.wu = NL.leggauss(nu)
        self.nrm = np.sqrt((2*np.arange(N)+1)/(2*T)); I = np.eye(N)
        def Cs(u):
            lo, hi = -T+u, T
            if hi <= lo: return np.zeros((N, N))
            t = (hi+lo)/2 + (hi-lo)/2*self.xt; w = self.wt*(hi-lo)/2
            C = (self.phi(t)*w[:, None]).T @ self.phi(t-u); return (C+C.T)/2
        self.Cs = Cs
        us = T + T*self.xu; wus = self.wu*T
        G = np.zeros((N, N)); G1 = np.zeros((N, N)); E = np.zeros((N, N))
        for u, w in zip(us, wus):
            C = Cs(u); G += w*K(u)*(I-C); G1 += w*K1(u)*(I-C); E += w*np.exp(u/2)*C
        self.Gam = C0*I + G + tau(2*T)*I                       # full archimedean form
        self.Lev1 = G1 + tau1(2*T)*I                           # Lev_{K_1} >= 0
        self.Eexp = 2*E                                        # 2 int_0^{2T} C_F(u) e^{u/2} du
        self.Pi = np.zeros((N, N)); self.cont = contacts(T)
        for n, l, v in self.cont: self.Pi -= v*Cs(l)
        self.A = self.Gam + self.Pi
        t = T*self.xt; w = self.wt*T; P = self.phi(t)
        self.tp = (P*w[:, None]).T @ np.exp(t/2); self.tm = (P*w[:, None]).T @ np.exp(-t/2)
    def phi(self, t): return NL.legvander(t/self.T, self.N-1)*self.nrm

def primitive_bottom(W):
    R = np.vstack([W.tp, W.tm]); _, _, Vt = np.linalg.svd(R); Q = Vt[2:].T       # basis of P_T
    M = Q.T @ W.A @ Q; M = (M+M.T)/2
    ev, V = np.linalg.eigh(M); h = Q @ V[:, 0]
    return ev[0], h

def main(N=60):
    Ts = np.concatenate([np.linspace(0.36, 0.80, 23), [0.5*np.log(3), np.log(2), 0.5*np.log(5)]])
    Ts = np.unique(np.round(Ts, 6)); rows = []
    print("   T      lambda_A      a_T(h*)    (C0+4)|h|^2     E_psi(h*)     Lev_K1(h*)   resid   #cont")
    for T in Ts:
        W = Win(T, N); lam, h = primitive_bottom(W)
        aT = h @ W.A @ h; c = (C0+4)*(h@h); Ep = h@W.Eexp@h + h@W.Pi@h; L1 = h@W.Lev1@h
        res = aT - (c+Ep+L1); rows.append((T, lam, c, Ep, L1))
        print(f"{T:7.4f} {lam:13.4e} {aT:11.4e} {c:13.5f} {Ep:13.5f} {L1:13.5f} {res:9.1e} {len(W.cont):4d}")
    # convexity of log lambda_A in several variables (second differences on the uniform grid)
    R = np.array([r for r in rows if r[1] > 1e-13]); T = R[:, 0]; L = np.log(R[:, 1])
    for name, x in [("T", T), ("e^{2T}", np.exp(2*T)), ("e^{4T}", np.exp(4*T)),
                    ("A_T", np.array([sum(v for _, _, v in contacts(t)) for t in T]))]:
        d1 = np.diff(L)/np.diff(x); d2 = np.diff(d1)
        print(f"log lambda_A vs {name:7s}: slopes {d1.min():9.3f}..{d1.max():9.3f}; "
              f"second differences: {int((d2>0).sum())} >0, {int((d2<0).sum())} <0 out of {len(d2)}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
