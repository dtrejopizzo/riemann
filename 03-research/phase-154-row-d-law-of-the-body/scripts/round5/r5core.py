"""R154 round 5 -- core: two-frequency symbol, exact derivatives, second-order (Taylor)
branch-and-bound.

Object (same class as round 4, now with TWO contacts n = 2,3 for 1/2 log 3 < T <= log 2):

    f(tau) = m(tau) - sum_n v_n cos(tau log n) + nuhat(tau) + b0*g0h(tau) + b1*g1h(tau)
    m(tau) = Re psi(1/4 + i tau/2) - log pi           (even, increasing in |tau|)
    nuhat(tau) = sum_j 2 a_j cos(u_j tau),  u_j = j*d, d = 2T/M  (P-periodic, P = 2pi/d)

Lemma F1 (two-frequency graded tail, R154_015 sec.2): periodicity is used ONLY for nuhat,
so the graded lemma survives verbatim with any finite set of frequencies; the prime term is
EXACT on the first N periods and worst-cased only on [tau1+N*P, oo).

VERIFIER (new in round 5).  On a cell [mid-w/2, mid+w/2] the round-4 test was the Lipschitz
one, f >= f(mid) - L*w/2.  Here we split f = m + q + r with
    q = -sum v_n cos + nuhat   (analytic, exact q'),  r = b0 g0h + b1 g1h (analytic, exact r')
and use
    f(x) >= m(mid - w/2) + (q+r)(mid) - |(q+r)'(mid)|*w/2 - M2*w^2/8,        (TAY)
    M2 >= sup|q''+r''| = sum v_n log^2 n + 2 sum |a_j| u_j^2 + |b0| H0 + |b1| H1,
    H0 = int_{-2T}^{2T} u^2 cosh(u/2) du,  H1 = int_{-2T}^{2T} |u|^3 sinh(|u|/2) du.
(TAY) is Taylor with integral remainder plus the monotonicity of m; it is rigorous.  Near a
contact |f'| ~ 0 so the linear term is tiny and the admissible width is ~ sqrt(8*target/M2)
instead of 2*target/L: at target = 1e-7 that is a factor ~ 3e3 fewer evaluations.
"""
import math
import numpy as np
from scipy.special import psi as _dg, polygamma as _pg

# ------------------------------------------------------------------ symbol

def vdict(T):
    v = {}
    for n in (2, 3, 4, 5, 7, 8, 9):
        if n < math.exp(2*T) - 1e-9:
            Ln = {2: math.log(2), 3: math.log(3), 4: math.log(2), 5: math.log(5),
                  7: math.log(7), 8: math.log(2), 9: math.log(3)}[n]
            v[n] = 2*Ln/math.sqrt(n)
    return v


def m(tau):
    return np.real(_dg(0.25 + 0.5j*np.asarray(tau, dtype=float))) - math.log(math.pi)


def _J(k, s, L):
    """int_0^L u^k e^{s u} du, complex s (array), by the stable recursion."""
    e = np.exp(s*L)
    out = (e - 1.0)/s
    for j in range(1, k+1):
        out = (L**j*e - j*out)/s
    return out


def g0h(tau, T):
    """int_{-2T}^{2T} cosh(u/2) cos(u tau) du"""
    tau = np.asarray(tau, dtype=float); L = 2*T
    s = 0.5 + 1j*tau
    return np.real(_J(0, s, L) + _J(0, -0.5 + 1j*tau, L))


def g0hp(tau, T):
    """d/dtau g0h = -int u cosh(u/2) sin(u tau) du"""
    tau = np.asarray(tau, dtype=float); L = 2*T
    return -np.imag(_J(1, 0.5 + 1j*tau, L) + _J(1, -0.5 + 1j*tau, L))


def g1h(tau, T):
    """int_{-2T}^{2T} u sinh(u/2) cos(u tau) du"""
    tau = np.asarray(tau, dtype=float); L = 2*T
    return np.real(_J(1, 0.5 + 1j*tau, L) - _J(1, -0.5 + 1j*tau, L))


def g1hp(tau, T):
    tau = np.asarray(tau, dtype=float); L = 2*T
    return -np.imag(_J(2, 0.5 + 1j*tau, L) - _J(2, -0.5 + 1j*tau, L))


def nuhat(tau, us, a, chunk=20000):
    tau = np.asarray(tau, dtype=float); out = np.empty(len(tau))
    us = np.asarray(us); a = np.asarray(a)
    for i in range(0, len(tau), chunk):
        sl = slice(i, i+chunk)
        out[sl] = 2*(np.cos(np.outer(tau[sl], us)) @ a)
    return out


def nuhatp(tau, us, a, chunk=20000):
    tau = np.asarray(tau, dtype=float); out = np.empty(len(tau))
    us = np.asarray(us); a = np.asarray(a); au = a*us
    for i in range(0, len(tau), chunk):
        sl = slice(i, i+chunk)
        out[sl] = -2*(np.sin(np.outer(tau[sl], us)) @ au)
    return out


def base(tau, v):
    s = m(tau)
    for n, vn in v.items():
        s = s - vn*np.cos(np.asarray(tau)*math.log(n))
    return s


def fval(tau, T, us, a, b0, b1, v):
    tau = np.asarray(tau, dtype=float)
    return base(tau, v) + b0*g0h(tau, T) + b1*g1h(tau, T) + nuhat(tau, us, a)

# ------------------------------------------------------------------ constants

def G0(T):
    L = 2*T
    return 2*(2*L*math.sinh(L/2) - 4*(math.cosh(L/2) - 1))


def G1(T):
    L = 2*T
    F = lambda u: 2*u*u*math.cosh(u/2) - 8*u*math.sinh(u/2) + 16*math.cosh(u/2)
    return 2*(F(L) - F(0))


def H0(T):
    """int_{-2T}^{2T} u^2 cosh(u/2) du = 2 int_0^{2T} u^2 cosh(u/2) du"""
    L = 2*T
    F = lambda u: 2*u*u*math.sinh(u/2) - 8*u*math.cosh(u/2) + 16*math.sinh(u/2)
    return 2*(F(L) - F(0))


def H1(T):
    """int_{-2T}^{2T} |u|^3 sinh(|u|/2) du = 2 int_0^{2T} u^3 sinh(u/2) du"""
    L = 2*T
    F = lambda u: (2*u**3*math.cosh(u/2) - 12*u*u*math.sinh(u/2)
                   + 48*u*math.cosh(u/2) - 96*math.sinh(u/2))
    return 2*(F(L) - F(0))


def lip(T, us, a, b0, b1, v):
    return (0.5*_pg(1, 0.25)
            + sum(vn*math.log(n) for n, vn in v.items())
            + 2*float(np.sum(np.abs(a)*np.asarray(us)))
            + abs(b0)*G0(T) + abs(b1)*G1(T))


def m2bound(T, us, a, b0, b1, v, with_beta=True):
    """upper bound for sup |q'' + r''| (the non-m part of f'')"""
    s = (sum(vn*math.log(n)**2 for n, vn in v.items())
         + 2*float(np.sum(np.abs(a)*np.asarray(us)**2)))
    if with_beta:
        s += abs(b0)*H0(T) + abs(b1)*H1(T)
    return s


def kk(T, t):
    return (2*math.cosh(T)/t + math.sinh(T)/t**2, 8*T*math.sinh(T)/t)

# ------------------------------------------------------------------ evaluators with (val, slope)

def make_eval(which, T, us, a, b0, b1, v, P, N):
    """returns (gfun, mfun, tailfun, M2)

    gfun(x)  -> (q+r)(x), (q+r)'(x)   [everything except m and the |b|k_i tail terms]
    mfun(x)  -> m(x + k P)            [monotone increasing part]
    tailfun(x) -> -|b0| k0(x+kP) - |b1| k1(x+kP)  (monotone increasing in x; None for 'f')
    """
    us = np.asarray(us, float); a = np.asarray(a, float)
    Sv = sum(v.values())
    if which == 'f':
        def gfun(x):
            q = nuhat(x, us, a) + b0*g0h(x, T) + b1*g1h(x, T)
            qp = nuhatp(x, us, a) + b0*g0hp(x, T) + b1*g1hp(x, T)
            for n, vn in v.items():
                ln = math.log(n)
                q = q - vn*np.cos(x*ln); qp = qp + vn*ln*np.sin(x*ln)
            return q, qp
        M2 = m2bound(T, us, a, b0, b1, v, with_beta=True)
        return gfun, (lambda x: m(x)), None, M2
    k = int(which[1:])
    def gfun(x, k=k):
        q = nuhat(x, us, a); qp = nuhatp(x, us, a)
        if k < N:
            tk = x + k*P
            for n, vn in v.items():
                ln = math.log(n)
                q = q - vn*np.cos(tk*ln); qp = qp + vn*ln*np.sin(tk*ln)
        else:
            q = q - Sv
        return q, qp
    M2 = m2bound(T, us, a, 0.0, 0.0, v, with_beta=False)
    def mfun(x, k=k):
        return m(x + k*P)
    def tailfun(x, k=k):
        k0, k1 = kk(T, x + k*P)
        return -abs(b0)*k0 - abs(b1)*k1
    return gfun, mfun, tailfun, M2


def hval(x, which, T, us, a, b0, b1, v, P, N):
    gfun, mfun, tfun, _ = make_eval(which, T, us, a, b0, b1, v, P, N)
    x = np.asarray(x, float)
    q, _ = gfun(x)
    out = q + mfun(x)
    if tfun is not None:
        out = out + tfun(x)
    return out

# ------------------------------------------------------------------ Taylor branch-and-bound

def bb_taylor(which, lo, hi, T, us, a, b0, b1, v, P, N, target,
              w0=0.02, wmin=1e-9, max_evals=4_000_000_000, block=200_000):
    """Exhaustive cover of [lo,hi] proving  <which> >= target.

    Cell [c, c+w] with midpoint mid is RETIRED when
        m(mid-w/2 [+kP]) + tail(mid-w/2 [+kP]) + q(mid) - |q'(mid)|*w/2 - M2*w^2/8 >= target
    (m and the tail terms are increasing, hence bounded below at the left endpoint), and is
    OTHERWISE BISECTED.  Nothing is discarded; exhausting the budget RAISES.
    """
    gfun, mfun, tfun, M2 = make_eval(which, T, us, a, b0, b1, v, P, N)
    n0 = int(math.ceil((hi-lo)/w0)); w = (hi-lo)/n0
    stack = [(lo + np.arange(n0)*w, w)]
    lb = np.inf; best = np.inf; best_arg = None; nfinal = 0; meas = 0.0; nev = 0
    while stack:
        cur, w = stack.pop()
        if len(cur) > block:
            stack.append((cur[block:], w)); cur = cur[:block]
        mid = cur + w/2
        q, qp = gfun(mid)
        mlo = mfun(cur)
        if tfun is not None:
            mlo = mlo + tfun(cur)
        low = mlo + q - np.abs(qp)*(w/2) - M2*w*w/8
        nev += len(mid)
        if nev > max_evals:
            raise RuntimeError(f"budget exceeded ({nev}); NOT certified")
        val = mfun(mid) + q + (tfun(mid) if tfun is not None else 0.0)
        i0 = int(val.argmin())
        if float(val[i0]) < best:
            best = float(val[i0]); best_arg = float(mid[i0])
        keep = low < target
        nk = int(keep.sum())
        if nk == 0:
            continue
        if w/2 < wmin:
            lb = min(lb, float(low[keep].min()))
            nfinal += nk; meas += nk*w
            continue
        c2 = cur[keep]
        stack.append((np.repeat(c2, 2) + np.tile(np.array([0.0, w/2]), nk), w/2))
    return dict(which=which, lo=lo, hi=hi, lb=min(target, lb), best=best, best_arg=best_arg,
                evals=nev, final_intervals=nfinal, surviving_measure=meas, M2=M2,
                target=target, wmin=wmin, w0=w0, complete=True, method='taylor2')


def fine_min(func, lo, hi, h):
    mu = np.inf; arg = 0.0
    n = int((hi-lo)/h) + 1
    for i in range(0, n, 2_000_000):
        t = lo + (np.arange(i, min(i+2_000_000, n)))*h
        val = func(t)
        j = int(val.argmin())
        if float(val[j]) < mu:
            mu = float(val[j]); arg = float(t[j])
    return mu, arg
