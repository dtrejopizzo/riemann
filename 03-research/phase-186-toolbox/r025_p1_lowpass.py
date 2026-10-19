#!/usr/bin/env python3
"""R186_025 (P1) — dos cotas inferiores PROVED para la forma archimediana primitiva en ventana corta y en V_k,
y su comparacion con Galerkin.  Forma: a_inf(F) = C0||F||^2 + int_0^oo (||F||^2 - C_F(u)) K(u) du (Paper 47 thm:A, lem:K).
Ruta A (Levy, ventana sola de semilongitud tau, F perp e^{+-x/2}):
   c_inf(tau) >= C0 + log(2/tau) + pi/2 - tau + kappa0(tau),
   kappa0(tau) >= sup_R w(R) (1 - 16 (R^2+tau^2/4)^3/(27 pi^4 R^2)),  w(R) = log(2R) + gamma - Ci(2R).
Ruta B (paso-bajo, vale en V_k con k bloques de semilongitud tau):
   a_inf|V_k >= int_0^{th*} m_lb(th/tau) delta'(th) dth,  delta(th) = cosh^2(tau) (th^2+tau^2/4)^2/6,
   m_lb(R) = max(C0, log(R/2pi) - 1/R - 1/(2R^2))  (lem:mbounds ii).
Comparacion: Galerkin c_inf(tau) (ventana sola, r024 build) y min a_inf|V_k (r024), y cociente de Rayleigh
generalizado theta_N = sup_{V_k} Q(F)/sum_B a_inf(F_B) (acoplamiento relativo a la diagonal).
Uso: python3 r025_p1_lowpass.py
"""
import sys, os, numpy as np, mpmath as mp
from scipy.special import sici
from scipy.integrate import quad
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r024_schur as R

C0 = float(mp.digamma(0.25)) - np.log(np.pi)
GAM = float(mp.euler)

def w(R):  # int_0^2 (1-cos(Rv))/v dv
    si, ci = sici(2*R); return np.log(2*R) + GAM - ci

def ruta_A(tau):
    a = tau**2/4
    best = max((w(R)*(1 - 16*(R**2+a)**3/(27*np.pi**4*R**2)), R) for R in np.linspace(0.5, 4, 3501))
    kappa0, Rb = best
    lb = C0 + np.log(2/tau) + np.pi/2 - tau + kappa0
    return lb, kappa0, Rb

def ruta_B(tau):
    ch2 = np.cosh(tau)**2; a = tau**2/4
    delta = lambda th: ch2*(th**2+a)**2/6
    dd = lambda th: ch2*2*th*(th**2+a)/3
    ths = np.sqrt(np.sqrt(6/ch2) - a)
    mlb = lambda R: max(C0, np.log(R/(2*np.pi)) - 1/R - 1/(2*R**2)) if R > 0 else C0
    val, err = quad(lambda th: mlb(th/tau)*dd(th), 0, ths, limit=200)
    assert abs(delta(ths)-1) < 1e-12
    return val + C0*delta(0.0)          # termino C0*delta(0), delta(0) = cosh^2(tau) tau^4/96 (despreciable)

def galerkin_single(tau, N):
    be = R.BE(0); d = R.build(tau, N, be, kind='equal1'); o = R.analyse(d, be); return float(o['c_inf'])

def galerkin_Vk(T, k, N):
    be = R.BE(0); d = R.build(T, N, be, kind=f'equal{k}'); o = R.analyse(d, be)
    # theta_N: sup Q / sum_B a_inf(F_B) sobre V_k, Q = -(A0 - diag_bloques A0) sobre V_k
    A0, idx, ta, tb, dim = d['A0'], d['idx'], d['ta'], d['tb'], d['dim']
    cols = []
    for ix in idx:
        n = be.nulls(np.array([ta[ix], tb[ix]])); Bm = be.zeros(dim, n.shape[1]); Bm[ix] = n; cols.append(Bm)
    Zv = np.hstack(cols)
    Ad = be.zeros(dim, dim)
    for ix in idx: Ad[np.ix_(ix, ix)] = A0[np.ix_(ix, ix)]
    D = Zv.T @ Ad @ Zv; Q = -(Zv.T @ (A0 - Ad) @ Zv)
    from scipy.linalg import eigh
    th = eigh(Q, D, eigvals_only=True)
    return float(o['c_inf']), float(th[-1]), float(th[0]), float(np.linalg.eigvalsh(D)[0])

if __name__ == '__main__':
    print("# (P1) ventana sola: tau | log(1/tau) | ruta A (kappa0, R*) | ruta B | Galerkin c_inf (N=14/20) | C_A, C_B, C_gal := log(1/tau) - valor")
    for tau in (0.02, 0.031, 0.05, 0.0619, 0.0894, 0.1):
        lA, k0, Rb = ruta_A(tau); lB = ruta_B(tau); g14 = galerkin_single(tau, 14); g20 = galerkin_single(tau, 20)
        L = np.log(1/tau)
        print(f"{tau:.4f} {L:.3f} | A {lA:.3f} (k0={k0:.3f}, R*={Rb:.2f}) | B {lB:.3f} | gal {g14:.4f}/{g20:.4f} | C_A={L-lA:.3f} C_B={L-lB:.3f} C_gal={L-g20:.3f}")
    print("# (L1 directa) V_k: T k tau | ruta B | Galerkin min a_inf|V_k (N) | theta_N = sup Q/diag | min Q/diag | min diag")
    for T, k in ((0.5*np.log(3), 7), (0.69, 9), (0.5*np.log(5), 9), (0.5*np.log(5), 13)):
        tau = T/k; lB = ruta_B(tau)
        for N in (8, 12, 16):
            c, thmax, thmin, dmin = galerkin_Vk(T, k, N)
            print(f"{T:.4f} {k:2d} {tau:.4f} | B {lB:.3f} | gal {c:.4f} (N={N}) | theta={thmax:.4f} | {thmin:.4f} | diag_min={dmin:.3f}")
