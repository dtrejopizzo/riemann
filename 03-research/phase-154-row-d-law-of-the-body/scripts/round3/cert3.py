"""R154 round 3: atomic outside-window certificates with rigorous verification.

  lambda_min(A_T) >= inf_tau f(tau),
  f(tau) = m(tau) - sum_n v_n cos(tau log n) + sum_j 2 a_j cos(u_j tau) + b0 g0h(tau) + b1 g1h(tau)
  m(tau) = Re psi(1/4 + i tau/2) - log pi,  u_j >= 2T,
  g0h = FT of cosh(u/2) 1_{|u|<2T},  g1h = FT of u sinh(u/2) 1_{|u|<2T}.
Verification: (a) tail tau >= taumax analytically; (b) [0,taumax] by adaptive
Lipschitz branch-and-bound with the global constant L computed in lip().
"""
import math, numpy as np
from scipy.special import psi as dg, polygamma
from scipy.optimize import linprog

def vdict(T):
    v = {}
    for n in (2,3,4,5,7,8,9):
        if n < math.exp(2*T) - 1e-9:
            L = {2:math.log(2),3:math.log(3),4:math.log(2),5:math.log(5),7:math.log(7),8:math.log(2),9:math.log(3)}[n]
            v[n] = 2*L/math.sqrt(n)
    return v

def m(tau):
    return np.real(dg(0.25+0.5j*np.asarray(tau,dtype=float))) - math.log(math.pi)

def base(tau, v):
    s = m(tau)
    for n, vn in v.items(): s = s - vn*np.cos(np.asarray(tau)*math.log(n))
    return s

def g0h(tau, T):
    tau = np.asarray(tau,dtype=float); L = 2*T
    return 2*(0.5*math.sinh(T)*np.cos(L*tau) + tau*math.cosh(T)*np.sin(L*tau))/(tau**2+0.25)

def g1h(tau, T):
    tau = np.asarray(tau,dtype=float); L = 2*T; a = 0.5
    def I(s): return (L*np.exp(s*L)/s - (np.exp(s*L)-1)/s**2)
    w = tau
    return 2*np.real(0.5*(I(a+1j*w) - I(-a+1j*w)))

# ---- rigorous constants -------------------------------------------------
def G0(T):  # int_{-2T}^{2T} |u| cosh(u/2) du
    L = 2*T
    return 2*(2*L*math.sinh(L/2) - 4*(math.cosh(L/2)-1))
def G1(T):  # int |u|^2 |sinh(u/2)| du
    L = 2*T
    # 2 int_0^L u^2 sinh(u/2) du = 2[2u^2 cosh(u/2) - 8u sinh(u/2) + 16 cosh(u/2)]_0^L
    F = lambda u: 2*u*u*math.cosh(u/2) - 8*u*math.sinh(u/2) + 16*math.cosh(u/2)
    return 2*(F(L)-F(0))

def lip(T, us, a, b0, b1, v):
    """global bound on |f'(tau)|"""
    Lm = 0.5*polygamma(1,0.25)          # |m'| <= psi'(1/4)/2
    Lp = sum(vn*math.log(n) for n,vn in v.items())
    La = 2*float(np.sum(np.abs(a)*np.asarray(us)))
    return Lm + Lp + La + abs(b0)*G0(T) + abs(b1)*G1(T)

def tailbound(T, us, a, b0, b1, v, taumax):
    """rigorous lower bound of f on [taumax, inf)"""
    mlow = m(np.array([taumax]))[0] - sum(v.values())
    return (mlow - 2*float(np.sum(np.abs(a)))
            - abs(b0)*(2*math.cosh(T)/taumax + math.sinh(T)/taumax**2)
            - abs(b1)*(8*T*math.sinh(T)/taumax))

def fval(tau, T, us, a, b0, b1, v):
    tau = np.asarray(tau,dtype=float)
    out = base(tau, v) + b0*g0h(tau,T) + b1*g1h(tau,T)
    us = np.asarray(us); a = np.asarray(a)
    for i in range(0, len(tau), 20000):
        sl = slice(i, i+20000)
        out[sl] = out[sl] + 2*(np.cos(np.outer(tau[sl], us)) @ a)
    return out

def verify(T, us, a, b0, b1, v, taumax, target, w0=0.02, chunk=400000, maxit=45):
    """Certify f >= target on [0,taumax] by adaptive Lipschitz branch-and-bound.
    Returns (ok, best_midpoint_value, L, n_intervals_left)."""
    L = lip(T, us, a, b0, b1, v)
    n0 = int(math.ceil(taumax/w0)); w = taumax/n0
    cur = np.arange(n0)*w
    best = np.inf
    for it in range(maxit):
        mid = cur + w/2
        vals = np.empty(len(mid))
        for i in range(0, len(mid), chunk):
            sl = slice(i, i+chunk); vals[sl] = fval(mid[sl], T, us, a, b0, b1, v)
        best = min(best, float(vals.min()))
        keep = vals - L*w/2 < target
        nk = int(keep.sum())
        if nk == 0:
            return True, best, L, 0
        if best < target:
            return False, best, L, nk
        cur = np.repeat(cur[keep],2) + np.tile(np.array([0.0, w/2]), nk)
        w = w/2
    return False, best, L, len(cur)
