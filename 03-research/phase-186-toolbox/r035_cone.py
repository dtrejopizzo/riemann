#!/usr/bin/env python3
"""R186_035 - the negative archimedean cone of the PNT-window identity (R186_033 Lemma 1) and the inequality (*_33).

Identity (R186_033, F in P_T, Phi = autocorrelation):
  a_T(F) = b0(F) + E_psi(F),   b0(F) := (C0+4)Phi(0) + Lev_{K1}(Phi),   E_psi = E_exp + E_prime,
  E_exp = 2 int_0^{2T} Phi(u) e^{u/2} du,  E_prime = -sum_{n<e^{2T}} v_n Phi(log n).
Cone C_T = {F in P_T : b0(F) < 0}.  This script computes (all NUMERICAL, Legendre Galerkin N modes):
  (1) inertia of b0|P_T, lambda_min(b0|P_T) = -sup_C b/|F|^2, direction e_-, E_psi(e_-), a_T(e_-);
      fraction of e_- and of h* in the piecewise Tate modes E_k (k equal blocks, R186_024);
  (2) mu(s) = lambda_min(s b0 + E_psi | P_T), s >= 1 (S-lemma: a_T >= 0 on C_T <=> there is s>=1 with mu(s)>=0);
  (3) piecewise identity E_psi = -2 int_0^{2T} R(u) phi'(u) du, R(u) = e^u - psi(e^u), phi = Phi e^{-u/2}:
      R_min, R_max, positive variation TV+(phi) at e_- and h*, and the bound E_psi >= 2 R_min Phi(0) - 2(R_max-R_min) TV+.
Usage: python3 r035_cone.py [N=60]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma

C0 = digamma(0.25) - np.log(np.pi)
def K(u):  return 2*np.exp(-u/2)/(1-np.exp(-2*u))
def K1(u): return 2*np.exp(-5*u/2)/(1-np.exp(-2*u))
def tau(r):  return np.log(1/np.tanh(r/4)) + np.pi - 2*np.arctan(np.exp(r/2))
def tau1(r): return tau(r) - 4*np.exp(-r/2)

def contacts(T):
    out = []
    for n in range(2, 5000):
        if np.log(n) >= 2*T: break
        p = next(q for q in range(2, n+1) if n % q == 0); m = n
        while m % p == 0: m //= p
        if m == 1: out.append((n, np.log(n), 2*np.log(p)/np.sqrt(n)))
    return out

def psi_cheb(x):
    return sum(np.log(p) for n, _, _ in contacts(0.5*np.log(x+1e-12)+1e-9) for p in [n] if n <= x) if False else \
        sum(2*np.log(p)/v*0 + np.log(p) for (n, l, v) in contacts(10) if n <= x for p in [min(q for q in range(2, n+1) if n % q == 0)])

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
        G1 = np.zeros((N, N)); E = np.zeros((N, N))
        for u, w in zip(us, wus):
            C = Cs(u); G1 += w*K1(u)*(I-C); E += w*np.exp(u/2)*C
        self.Lev1 = G1 + tau1(2*T)*I
        self.b0 = (C0+4)*I + self.Lev1
        self.Eexp = 2*E
        self.Pi = np.zeros((N, N)); self.cont = contacts(T)
        for n, l, v in self.cont: self.Pi -= v*Cs(l)
        self.Epsi = self.Eexp + self.Pi
        self.A = self.b0 + self.Epsi
        t = T*self.xt; w = self.wt*T; P = self.phi(t)
        self.tp = (P*w[:, None]).T @ np.exp(t/2); self.tm = (P*w[:, None]).T @ np.exp(-t/2)
        R = np.vstack([self.tp, self.tm]); _, _, Vt = np.linalg.svd(R); self.Q = Vt[2:].T   # basis of P_T
    def phi(self, t): return NL.legvander(t/self.T, self.N-1)*self.nrm
    def red(self, M): M = self.Q.T @ M @ self.Q; return (M+M.T)/2
    def autocorr(self, h, us):
        return np.array([h @ self.Cs(u) @ h for u in us])
    def tate_modes(self, k):
        """E_k = span{e^{+-x/2} 1_B} cap P_T, projected L2 onto the Galerkin space (orthonormalized)."""
        T = self.T; edges = np.linspace(-T, T, k+1); cols = []
        for a, b in zip(edges[:-1], edges[1:]):
            t = (a+b)/2 + (b-a)/2*self.xt; w = self.wt*(b-a)/2; P = self.phi(t)
            for sgn in (+1, -1): cols.append((P*w[:, None]).T @ np.exp(sgn*t/2))
        Y = np.array(cols).T                      # N x 2k
        Rm = np.vstack([self.tp, self.tm]) @ Y    # 2 x 2k
        _, _, Vt = np.linalg.svd(Rm); Z = Y @ Vt[2:].T
        Qz, _ = np.linalg.qr(Z); return Qz

def R_cheb(u, cont):
    x = np.exp(u); return x - sum(np.log(min(q for q in range(2, n+1) if n % q == 0)) for n, l, v in cont if n <= x)

def analyse(T, N=60, verbose=True):
    W = Win(T, N); Q = W.Q
    b0 = W.red(W.b0); Ep = W.red(W.Epsi); A = W.red(W.A)
    ev, V = np.linalg.eigh(b0); nneg = int((ev < 0).sum()); em = Q @ V[:, 0]
    evA, VA = np.linalg.eigh(A); lamA = evA[0]; h = Q @ VA[:, 0]
    def forms(f): return dict(b0=f@W.b0@f, Eexp=f@W.Eexp@f, Epr=f@W.Pi@f, Epsi=f@W.Epsi@f, a=f@W.A@f)
    fe, fh = forms(em), forms(h)
    # mu(s)
    ss = np.concatenate([np.linspace(0.5, 1, 11), np.linspace(1, 6, 101)])
    mu = np.array([np.linalg.eigvalsh(s*b0 + Ep)[0] for s in ss])
    i = np.argmax(mu[ss >= 1]); sbest = ss[ss >= 1][i]; mubest = mu[ss >= 1][i]
    # interval of s with mu>0
    pos = ss[(ss >= 1) & (mu > 0)]
    # piecewise identity
    us = np.linspace(0, 2*T, 4001); cont = W.cont
    Rv = np.array([R_cheb(u, cont) for u in us]); Rmin, Rmax = Rv.min(), Rv.max()
    out = {}
    for name, f, fr in (("e-", em, fe), ("h*", h, fh)):
        Phi = W.autocorr(f, us); ph = Phi*np.exp(-us/2); d = np.diff(ph)
        TVp = d[d > 0].sum(); Eparts = -2*np.sum(Rv[:-1]*d)
        out[name] = dict(TVp=TVp, Eparts=Eparts, Phimin=Phi.min()/Phi[0], bound=2*Rmin*Phi[0]-2*(Rmax-Rmin)*TVp)
    # piecewise Tate modes
    fracs = {}
    for k in (5, 9):
        Qz = W.tate_modes(k)
        fracs[k] = (np.linalg.norm(Qz.T @ em)**2, np.linalg.norm(Qz.T @ h)**2)
    if verbose:
        print(f"\n=== T = {T:.4f}  (e^2T = {np.exp(2*T):.3f}, contacts {[n for n,_,_ in cont]})")
        print(f" inertia b0|P_T: n_- = {nneg}, lambda_min(b0) = {ev[0]:+.4f} (= -sup_C b/|F|^2), lambda_2 = {ev[1]:+.4f}; lambda_A = {lamA:.3e}")
        print(f" e_-: b0 {fe['b0']:+.4f}  E_exp {fe['Eexp']:+.4f}  E_prime {fe['Epr']:+.4f}  E_psi {fe['Epsi']:+.4f}  a_T(e_-) {fe['a']:+.4f}")
        print(f" h*:  b0 {fh['b0']:+.4f}  E_exp {fh['Eexp']:+.4f}  E_prime {fh['Epr']:+.4f}  E_psi {fh['Epsi']:+.4f}  a_T(h*) {fh['a']:+.3e}  <e_-,h*>^2 = {(em@h)**2:.4f}")
        print(f" mu(s)=lambda_min(s b0+E_psi): mu(1)={mu[ss==1][0]:.3e}, max_{{s>=1}} mu = {mubest:+.4f} en s = {sbest:.2f}; "
              f"mu>0 for s in [{pos.min() if len(pos) else float('nan'):.2f}, {pos.max() if len(pos) else float('nan'):.2f}]; mu(0.9)={mu[np.isclose(ss,0.9)][0]:+.4f}")
        print(f" R(u)=e^u-psi(e^u) on [0,2T]: R_min = {Rmin:.4f}, R_max = {Rmax:.4f}")
        for name in ("e-", "h*"):
            o = out[name]
            print(f"  {name}: TV+(Phi e^-u/2)/Phi(0) = {o['TVp']:.4f}, piecewise E_psi = {o['Eparts']:+.4f}, min Phi/Phi(0) = {o['Phimin']:+.4f}, Lemma 3 bound = {o['bound']:+.4f}")
        print(f" fraction in piecewise Tate modes (k=5, k=9): e_- {fracs[5][0]:.3f}, {fracs[9][0]:.3f};  h* {fracs[5][1]:.3f}, {fracs[9][1]:.3f}")
    return dict(T=T, nneg=nneg, lam_b0=ev[0], lamA=lamA, mubest=mubest, sbest=sbest, Rmin=Rmin, Rmax=Rmax, out=out)

def main(N=60):
    for T in [0.60, 0.62, 0.65, np.log(2), 0.75, 0.5*np.log(5), 0.9, 1.0, 1.2]:
        analyse(T, N)
    print("\n# sweep of the inertia of b0|P_T")
    for T in np.linspace(0.5, 1.6, 12):
        W = Win(T, 40); ev = np.linalg.eigvalsh(W.red(W.b0))
        print(f"  T={T:.3f}: n_-={int((ev<0).sum())}, lambda_min={ev[0]:+.4f}, lambda_2={ev[1]:+.4f}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
