#!/usr/bin/env python3
"""R186_034 — the determinantal object of the window (self-contained).

Forma (Paper 47 eq:symbol / eq:form / thm:A / lem:K / thm:S(iii)):
  sigma_T(tau) = m(tau) - sum_{n in N_T} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi,
  a_T(F) = (1/2pi) int sigma_T |F^|^2 = C_0||F||^2 + int_0^oo (||F||^2 - C_F(u))K(u)du - sum v_n C_F(log n),
  P_T = {F in L^2(I_T): int F e^{+-t/2} = 0}.
Decomposition prop:negtrace:  a_T = Pos_T - Neg_T,  Pos_T = R_T sigma_+(D) R_T,  Neg_T = R_T sigma_-(D) R_T.

Computed objects (orthonormal Legendre basis of degree < M on I_T, all Galerkin):
  (1) A   = matrix of a_T in x-space (as in r024/r028, nu Gauss nodes in u);
  (2) Neg = (1/2pi) int_{sigma<0} (-sigma) phi^_k phi^_l dtau, with phi^_k = sqrt((2k+1)2T) i^k j_k(tau T)
            (compact support: Gauss quadrature per component of the negative set);
  (3) Pos = A + Neg;
  (4) Birman–Schwinger determinant  D_B(s) = det(1 - s B), B = Pos^{-1/2} Neg Pos^{-1/2} on P_T,
      D_B(1) = det(A|P_T)/det(Pos|P_T);  beta_max = maximal eigenvalue of the pencil (Neg, Pos) on P_T;
  (5) det(1 + Neg_T) (Fredholm, Neg trace-class) vs the leading term of Szegő–Kac–Akhiezer
        log det W_L(a) ~ L·(1/2pi) int log a + int_0^oo x s(x) s(-x) dx,  s(x) = (1/2pi) int log a(xi) e^{-i x xi} dxi,
      with a = 1 + sigma_-, L = 2T (window length);
  (6) self-check of the normalization in (5) with a fixed Gaussian symbol and large L (Nyström/Bornemann).

Usage: python3 r034_det.py [M=40] [nu=400]
"""
import sys, numpy as np, mpmath as mp
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq

LOG2 = np.log(2.0)
C0 = float(mp.digamma(0.25)) - np.log(np.pi)

def contacts(T):
    out = []
    for n in range(2, 400):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0)
        k = 0; r = n
        while r % p == 0: r //= p; k += 1
        if r == 1: out.append((n, np.log(p)))
    return out

def m_arch(tau):
    tau = np.atleast_1d(np.asarray(tau, float))
    return np.real(digamma(0.25 + 0.5j * tau)) - np.log(np.pi)

def sigma_T(T, tau):
    tau = np.atleast_1d(np.asarray(tau, float)); s = m_arch(tau)
    for n, lp in contacts(T):
        s -= 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
    return s

def neg_set(T, tmax=250.0, h=2e-3):
    """components {sigma_T < 0} on [0, tmax] (sigma -> +oo like log, no zeros beyond ~20)."""
    g = np.arange(0, tmax, h); s = sigma_T(T, g)
    zs = [brentq(lambda t: sigma_T(T, [t])[0], g[i], g[i + 1]) for i in range(len(g) - 1) if s[i] * s[i + 1] < 0]
    pts = [0.0] + zs
    comps = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1) if sigma_T(T, [(pts[i] + pts[i + 1]) / 2])[0] < 0]
    assert s[-1] > 0
    return comps, zs

# ---------- form in x-space (as in r024/r028) ----------
def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))
def tail(T): return np.log(1 / np.tanh(T / 2)) + np.pi - 2 * np.arctan(np.exp(T))

def legbasis(T, M, y):
    u = y / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    nrm = np.sqrt((2 * np.arange(M) + 1) / (2 * T))
    return np.array(P[:M]) * nrm[:, None]

def build_x(T, M, nu):
    xg, wg = NL.leggauss(M + 2)
    def C(u):
        lo, hi = -T + u, T
        if hi <= lo: return np.zeros((M, M))
        y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        F1 = legbasis(T, M, y); F2 = legbasis(T, M, y - u)
        Mx = (F1 * w) @ F2.T; return (Mx + Mx.T) / 2
    I = np.eye(M)
    # u in (0,2T): subdivide into 8 segments with nu/8 nodes each (regular integrand: (I-C(u))K(u) = O(1))
    A0 = np.zeros((M, M)); edges = np.linspace(0, 2 * T, 9); ug, uw = NL.leggauss(max(nu // 8, 8))
    for lo, hi in zip(edges[:-1], edges[1:]):
        us = (hi + lo) / 2 + (hi - lo) / 2 * ug; ws = (hi - lo) / 2 * uw
        for u, w in zip(us, ws): A0 += (I - C(u)) * (K(u) * w)
    A0 += I * (tail(T) + C0)
    Pr = np.zeros((M, M))
    for n, lp in contacts(T): Pr -= 2 * lp / np.sqrt(n) * C(np.log(n))
    # Tate
    xt, wt = NL.leggauss(60); y = T * xt; w = T * wt; F = legbasis(T, M, y)
    ta = (F * w) @ np.exp(y / 2); tb = (F * w) @ np.exp(-y / 2)
    return A0 + Pr, A0, ta, tb

def fhat(T, M, tau):
    """phi^_k(tau) phi^_l(tau) real: c_k c_l i^{k-l} j_k j_l (k+l even); returns matrix (M,M,len(tau))."""
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T)
    J = np.array([spherical_jn(k, tau * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[:, None] - np.arange(M)[None, :]))   # 0 if k+l odd (killed by the integral over R)
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def build_neg(T, M, comps, nq=200):
    xg, wg = NL.leggauss(nq); N = np.zeros((M, M))
    for lo, hi in comps:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        sm = -sigma_T(T, t)
        N += np.einsum('klt,t->kl', fhat(T, M, t), sm * w) / np.pi    # (1/2pi) int_R = (1/pi) int_0^oo (even)
    return N

def null_basis(rows):
    U, S, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def szego_terms(T, comps, nq=400, X=60.0, nx=6000):
    """a = 1 + sigma_-: log G = (1/2pi) int log a;  E = int_0^oo x s(x)s(-x)dx, s(x) = (1/2pi) int log a e^{-ix xi}."""
    xg, wg = NL.leggauss(nq); ts, ws = [], []
    for lo, hi in comps:
        ts.append((hi + lo) / 2 + (hi - lo) / 2 * xg); ws.append((hi - lo) / 2 * wg)
    ts = np.concatenate(ts); ws = np.concatenate(ws); la = np.log(1 - sigma_T(T, ts))
    logG = (la * ws).sum() / np.pi                       # even: (1/2pi) int_R = (1/pi) int_0^oo
    x = np.linspace(0, X, nx); dx = x[1] - x[0]
    s = (np.cos(np.outer(x, ts)) @ (la * ws)) / np.pi    # s real and even
    E = np.trapz(x * s * s, dx=dx)
    return logG, E

def fredholm_det_gauss(kernel, L, n=200):
    """det(I + K) on L^2(0,L), kernel k(x-y), Gauss–Legendre Nyström (Bornemann)."""
    xg, wg = NL.leggauss(n); x = L / 2 * (1 + xg); w = L / 2 * wg
    Kmat = kernel(x[:, None] - x[None, :]) * np.sqrt(w[:, None] * w[None, :])
    return np.linalg.slogdet(np.eye(n) + Kmat)

def check_szego_normalisation():
    """symbol a(xi) = 1 + alpha e^{-xi^2/2}: k(x) = (1/2pi) int (a-1) e^{-ix xi} = alpha e^{-x^2/2}/sqrt(2pi)."""
    alpha = 0.7
    xi = np.linspace(-40, 40, 40001); la = np.log(1 + alpha * np.exp(-xi ** 2 / 2)); dxi = xi[1] - xi[0]
    logG = np.trapz(la, dx=dxi) / (2 * np.pi)
    x = np.linspace(0, 30, 6001); s = (np.cos(np.outer(x, xi)) @ la) * dxi / (2 * np.pi)
    E = np.trapz(x * s * s, dx=x[1] - x[0])
    print("# Szegő check (fixed Gaussian symbol): log G = %.6f, E = %.6f" % (logG, E))
    for L in (5.0, 10.0, 20.0, 40.0):
        sg, ld = fredholm_det_gauss(lambda d: alpha * np.exp(-d ** 2 / 2) / np.sqrt(2 * np.pi), L, n=300)
        print("   L=%5.1f  log det = %.6f   L·logG + E = %.6f   remainder = %.2e" % (L, ld, L * logG + E, ld - L * logG - E))

def run(T, M, nu):
    name = {0.5 * np.log(3): '1/2 log 3', 0.5 * np.log(5): '1/2 log 5'}.get(T, '%.4f' % T)
    A, A0, ta, tb = build_x(T, M, nu)
    comps, zs = neg_set(T)
    N = build_neg(T, M, comps); Pos = A + N
    Z = null_basis([ta, tb])
    AP, NP, PP = Z.T @ A @ Z, Z.T @ N @ Z, Z.T @ Pos @ Z
    evA = np.linalg.eigvalsh(AP); lamA = evA[0]
    evPos = np.linalg.eigvalsh(PP); evPosL2 = np.linalg.eigvalsh(Pos)
    # pencil (Neg, Pos) on P_T
    Lc = np.linalg.cholesky(PP); Li = np.linalg.inv(Lc); B = Li @ NP @ Li.T; beta = np.linalg.eigvalsh(B)
    sA, ldA = np.linalg.slogdet(AP); sP, ldP = np.linalg.slogdet(PP)
    DB = sA * sP * np.exp(ldA - ldP)
    # minimizer and Pos(h*)
    w, V = np.linalg.eigh(AP); h = V[:, 0]; Posh = h @ PP @ h; Negh = h @ NP @ h
    # det(1+Neg) on L^2(I_T) and Szegő
    evN = np.linalg.eigvalsh(N); ld1N = np.log1p(evN).sum()
    logG, E = szego_terms(T, comps)
    print(f"\n=== T = {name} = {T:.5f}   M = {M}  contacts = {[n for n,_ in contacts(T)]}")
    print(f"zeros of sigma_T: {np.round(zs, 4).tolist()}")
    print(f"negative set: {[(round(a,3), round(b,3)) for a,b in comps]}   measure = {sum(b-a for a,b in comps):.4f}   Shannon (2T/2pi)·measure·2 = {2*T*2*sum(b-a for a,b in comps)/(2*np.pi):.3f}")
    print(f"lambda_A = {lamA:+.4e}   (siguientes: {evA[1]:+.3e}, {evA[2]:+.3e});  n_-(a_T|P_T) = {(evA<0).sum()},  n_-(a_T|L2) = {(np.linalg.eigvalsh(A)<0).sum()}")
    print(f"Pos_T: min autovalor en L2 = {evPosL2[0]:.3e}, en P_T = {evPos[0]:.3e}; max = {evPos[-1]:.3f}  (Pos > 0 en L2: {evPosL2[0] > 0})")
    print(f"Neg_T: eigenvalues > 1e-3: {np.round(evN[evN>1e-3][::-1], 5).tolist()};  tr Neg = {np.trace(N):.5f}  vs (2T/2pi) int sigma_- = {2*T*2*sum(((lambda t,w: ( -sigma_T(T,t)*w).sum())((hi+lo)/2+(hi-lo)/2*NL.leggauss(200)[0], (hi-lo)/2*NL.leggauss(200)[1])) for lo,hi in comps)/(2*np.pi):.5f}")
    print(f"Birman–Schwinger en P_T: beta_max = {beta[-1]:.12f}   1 - beta_max = {1-beta[-1]:.4e}   lambda_A/Pos(h*) = {lamA/Posh:.4e}   Pos(h*) = {Posh:.4f}  Neg(h*) = {Negh:.4f}")
    print(f"   next betas: {np.round(beta[-4:-1][::-1], 6).tolist()}   #beta>1 = {(beta>1).sum()}")
    print(f"D_B(1) = det(A|P)/det(Pos|P) = {DB:+.6e}   sign = {int(np.sign(DB))}   log|D_B| = {ldA-ldP:+.6f}   log(1-beta_max) = {np.log(1-beta[-1]):+.6f}   remainder (bulk) = {ldA-ldP-np.log(1-beta[-1]):+.6f}")
    print(f"det(1+Neg_T) (L2(I_T), Fredholm): log = {ld1N:+.6f};  Szegő: 2T·logG = {2*T*logG:+.6f}, E = {E:+.6f}, sum = {2*T*logG+E:+.6f}, rel. error in det = {np.expm1(2*T*logG+E-ld1N):+.3e}")
    g = np.linalg.eigvalsh(A0 - C0 * np.eye(M)); j = np.arange(1, M + 1)
    print(f"Theorem 1.2 check: eigenvalues of A0 - C0 (archimedean) / log(1+j) at j=5,10,20,{M}: " + ", ".join(f"{g[i-1]/np.log(1+i):.3f}" for i in (5, 10, 20, M)))
    return dict(lamA=lamA, DB=DB, beta=beta[-1], ld1N=ld1N, szego=2*T*logG+E)

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 40
    nu = int(sys.argv[2]) if len(sys.argv) > 2 else 400
    check_szego_normalisation()
    for T in (0.5 * np.log(3), 0.5 * np.log(5)):
        for Mi in (M // 2, M):
            if Mi == M or len(sys.argv) > 3: run(T, Mi, nu)
