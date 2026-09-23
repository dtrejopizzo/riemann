"""primeside.py -- prime/Gamma side of Theorem Z (7.2) for the d1000 weights.
Full prime-power sum up to e^Umax (w vanishes beyond, up to the psi tail ~1e-17),
Gauss-Legendre order NGL=800 on every B-spline support.  No truncation at e^U.
"""
import numpy as np, dlib as D
import revlib as R1, revlib2 as R2
NGL = 800

def prime_table(Umax):
    N = int(np.exp(Umax)) + 10
    return R1.vonmangoldt_table(N)

def f_prime(win, y, x, tau, ns, lam):
    T, h, ujs, sv = win.T, win.h, win.ujs, win.sv
    tau = np.asarray(tau, float)
    Kt = R2.Ktail_box(tau, T) - sum(y[i]*R2.Ktail_psi(tau, T, sv[i]) for i in range(len(sv)))
    ch = R2.cosh_box(tau, T) + sum(y[i]*R2.cosh_psi(tau, T, sv[i]) for i in range(len(sv)))
    for k, uj in enumerate(ujs):
        if abs(x[k]) < 1e-14: continue
        Kt -= x[k]*R2.Ktail_bspline(tau, T, uj, h, n=NGL)
        ch += x[k]*R2.cosh_bspline(tau, T, uj, h, n=NGL)
    logn = np.log(ns)
    wn = win.w_of_u(logn, y, x)*(logn <= win.Umax)
    coef = 2*lam/np.sqrt(ns)*wn
    nz = np.abs(coef) > 0
    pr = np.zeros_like(tau); ln = logn[nz]; cf = coef[nz]
    for a in range(0, len(ln), 20000):
        b = min(a+20000, len(ln))
        pr -= cf[a:b] @ np.cos(np.outer(ln[a:b], tau))
    return R1.m_of_tau(tau) + Kt + pr + ch

# ---------------------------------------------------------------- fast unified version
def Ktail_beyond(tau, Umax):
    """int_{Umax}^inf K(u) cos(tau u) du,  K = 2 sum_i e^{-(2i+1/2)u}."""
    tau = np.asarray(tau, float); out = np.zeros_like(tau); ph = np.exp(1j*Umax*tau)
    for i in range(R2.NIK):
        a = 2*i + 0.5
        out += 2*np.exp(-a*Umax)*np.real(ph/(a - 1j*tau))
    return out

def f_prime_fast(win, y, x, tau, ns, lam, tblk=20000, ublk=2000):
    """Same as f_prime but the K- and cosh-integrals over the shoulder use ONE
    knot-aligned Gauss-Legendre panel set (win.u, win.wq), not one per B-spline."""
    T = win.T; tau = np.asarray(tau, float)
    u = win.u; wq = win.wq; wu = win.w_of_u(u, y, x)
    K = 0.5/np.sinh(np.maximum(u, 1e-12)/2) + 0.5/np.cosh(u/2)
    inw = u >= 2*T
    g = np.where(inw, wq*(1.0-wu)*K, 0.0) + 4.0*wq*wu*np.cosh(u/2)
    out = np.zeros(len(tau))
    for a in range(0, len(u), ublk):
        b = min(a+ublk, len(u)); uu = u[a:b]
        for c in range(0, len(tau), tblk):
            d = min(c+tblk, len(tau))
            out[c:d] += g[a:b] @ np.cos(np.outer(uu, tau[c:d]))
    out += Ktail_beyond(tau, win.Umax)
    logn = np.log(ns); wn = win.w_of_u(logn, y, x)*(logn <= win.Umax)
    coef = 2*lam/np.sqrt(ns)*wn
    nz = np.abs(coef) > 1e-15; ln = logn[nz]; cf = coef[nz]
    for a in range(0, len(ln), 20000):
        b = min(a+20000, len(ln))
        out -= cf[a:b] @ np.cos(np.outer(ln[a:b], tau))
    return R1.m_of_tau(tau) + out
