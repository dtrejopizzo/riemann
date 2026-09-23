"""revlib2.py -- phase 155 REVERSE-ENGINEERING, basis 2 (C^2 flat-top weights).

w = 1 on [-2T,2T];  for u > 2T (even extension):
      w(u) = sum_i y_i psi_{s_i}(u-2T) + sum_j x_j beta((u-u_j)/h),
      psi_s(v) = (1 + s v + s^2 v^2/2) e^{-sv}      (psi(0)=1, psi'=psi''=0),
      beta = cardinal cubic B-spline (C^2, support 2h, integral h), u_j = 2T + j h.
With sum_i y_i = 1 the weight is C^2 across the window edge, so what(t) = O(t^-4)
and the zero sum sum_gamma what(tau-gamma) converges fast enough to truncate.
Conventions as in revlib.py.  ALL NUMBERS DIAGNOSTIC.
"""
import numpy as np
from scipy.special import digamma
from revlib import (LOG_PI, C0, load_zeros, m_of_tau, what_box, vonmangoldt_table,
                    Ktail_box, cosh_box, A_const, NIK)

# ---------------------------------------------------------------- shapes
def beta_spline(z):
    a = np.abs(z); out = np.zeros_like(a)
    m1 = a <= 1; m2 = (a > 1) & (a < 2)
    out[m1] = 2/3 - a[m1]**2 + a[m1]**3/2
    out[m2] = (2 - a[m2])**3 / 6
    return out

def psi_edge(v, s):
    return (1 + s*v + 0.5*s*s*v*v) * np.exp(-s*v)

# ---------------------------------------------------------------- transforms
def sinc4(a):
    out = np.ones_like(a); m = np.abs(a) > 1e-8
    out[m] = (np.sin(a[m])/a[m])**4
    return out

def Phi(z, s):            # int_0^inf psi_s(v) e^{-zv} dv  with z complex
    return 1.0/z + s/z**2 + s*s/z**3

def what_psi(t, T, s):
    t = np.asarray(t, float)
    return 2*np.real(np.exp(2j*T*t) * Phi(s - 1j*t, s))

def what_bspline(t, T, uj, h):
    t = np.asarray(t, float)
    return 2*h*np.cos(uj*t)*sinc4(t*h/2)

# ---------------------------------------------------------------- zero side
def zero_side(tau, T, svals, ujs, h, gam, chunk=96):
    """Bz[i] = sum_{|g|<=Gmax} what_box(tau_i-g);
       Ay[i_s,i], Ax[i_j,i] likewise for the psi and B-spline components."""
    tau = np.asarray(tau, float); nT = len(tau)
    Bz = np.zeros(nT); Ay = np.zeros((len(svals), nT)); Ax = np.zeros((len(ujs), nT))
    for a in range(0, len(gam), chunk):
        g = gam[a:a+chunk]
        for d in (tau[None, :] - g[:, None], tau[None, :] + g[:, None]):
            c2 = np.cos(2*T*d); s2 = np.sin(2*T*d)
            with np.errstate(divide='ignore', invalid='ignore'):
                bb = 2.0*s2/d
            bb[np.abs(d) < 1e-12] = 4.0*T
            Bz += bb.sum(0)
            P = 2*h*sinc4(d*h/2)
            th = h*d; ct2 = 2*np.cos(th)
            Cm = c2                                    # cos(2T d)      (j=0)
            Cc = c2*np.cos(th) - s2*np.sin(th)         # cos((2T+h) d)  (j=1)
            for j in range(0, JOFF + len(ujs)):
                if j == 0: cur = Cm
                elif j == 1: cur = Cc
                else:
                    cur = ct2*Cc - Cm; Cm, Cc = Cc, cur
                k = j - JOFF
                if 0 <= k < len(ujs):
                    Ax[k] += (cur*P).sum(0)
            for k, s in enumerate(svals):
                Ay[k] += (2*np.real(np.exp(2j*T*d)*Phi(s - 1j*d, s))).sum(0)
    return Bz, Ay, Ax

JOFF = 2   # first B-spline node index (support starts at 2T)

# ---------------------------------------------------------------- prime side
def Ktail_psi(tau, T, s):
    tau = np.asarray(tau, float); out = np.zeros_like(tau); ph = np.exp(2j*T*tau)
    for i in range(NIK):
        a = 2*i + 0.5
        out += 2*np.exp(-a*2*T)*np.real(ph*Phi(s + a - 1j*tau, s))
    return out

def cosh_psi(tau, T, s):
    tau = np.asarray(tau, float); ph = np.exp(2j*T*tau)
    return 2*np.real(ph*(np.exp(T)*Phi(s - 0.5 - 1j*tau, s)
                         + np.exp(-T)*Phi(s + 0.5 - 1j*tau, s)))

_GL = {}
def gl(n):
    if n not in _GL: _GL[n] = np.polynomial.legendre.leggauss(n)
    return _GL[n]

def Ktail_bspline(tau, T, uj, h, n=200):
    xs, ws = gl(n); a, b = uj - 2*h, uj + 2*h
    u = 0.5*(b-a)*xs + 0.5*(a+b); wq = 0.5*(b-a)*ws
    K = 0.5/np.sinh(u/2) + 0.5/np.cosh(u/2)
    return (wq*beta_spline((u-uj)/h)*K) @ np.cos(np.outer(u, tau))

def cosh_bspline(tau, T, uj, h, n=200):
    xs, ws = gl(n); a, b = uj - 2*h, uj + 2*h
    u = 0.5*(b-a)*xs + 0.5*(a+b); wq = 0.5*(b-a)*ws
    return 2*(wq*beta_spline((u-uj)/h)*2*np.cosh(u/2)) @ np.cos(np.outer(u, tau))

def w_of_logn(logn, T, svals, y, ujs, h, x):
    v = logn - 2*T
    out = np.where(v <= 0, 1.0, 0.0)
    m = v > 0
    acc = np.zeros(m.sum())
    for i, s in enumerate(svals): acc += y[i]*psi_edge(v[m], s)
    for k, uj in enumerate(ujs): acc += x[k]*beta_spline((logn[m]-uj)/h)
    out[m] = acc
    return out

def f_prime_side(tau, T, svals, y, ujs, h, x, ns, lam):
    tau = np.asarray(tau, float); logn = np.log(ns)
    Kt = Ktail_box(tau, T) \
         - sum(y[i]*Ktail_psi(tau, T, svals[i]) for i in range(len(svals))) \
         - sum(x[k]*Ktail_bspline(tau, T, ujs[k], h) for k in range(len(ujs)))
    ch = cosh_box(tau, T) \
         + sum(y[i]*cosh_psi(tau, T, svals[i]) for i in range(len(svals))) \
         + sum(x[k]*cosh_bspline(tau, T, ujs[k], h) for k in range(len(ujs)))
    wn = w_of_logn(logn, T, svals, y, ujs, h, x)
    coef = 2*lam/np.sqrt(ns)*wn
    nz = np.abs(coef) > 0
    pr = -(coef[nz] @ np.cos(np.outer(logn[nz], tau)))
    return m_of_tau(tau) + Kt + pr + ch
