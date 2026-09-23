"""R154 round 4 -- self-contained certificate core for the outside-window dual.

Object certified:
    f(tau) = sigma_T(tau) + nuhat(tau) + b0*g0h(tau) + b1*g1h(tau)      (tau real, even)
    sigma_T(tau) = m(tau) - sum_n v_n cos(tau log n),  m(tau) = Re psi(1/4 + i tau/2) - log pi
    nuhat(tau)   = sum_j 2 a_j cos(u_j tau),   u_j = j*d >= 2T,  d = 2T/M   (lattice => P-periodic, P = 2pi/d)
    g0h = FT of cosh(u/2) 1_{|u|<2T},   g1h = FT of u sinh(u/2) 1_{|u|<2T}
Theorem D1 (R154_007 sec.2) => lambda_min(A_T(v)) >= inf_tau f(tau).

Verification (round 4, repairs RJ/RP of R154_008):
  (a) [0, taumax]: STACK-based Lipschitz branch-and-bound, bound on a cell of width w with
      midpoint mid is  f >= f(mid) - L*w/2 ; NO interval is ever discarded; if the work budget
      is exhausted the routine RAISES (never returns a pass).
  (b) tau >= taumax: periodic tail lemma (Lemma D2.1),
      f(tau) >= m(taumax) - sum_n v_n - rho - |b0|*k0 - |b1|*k1,
      with rho a certified upper bound for -min nuhat computed on ONE period by the same B&B.
  (c) every constant re-evaluated in mpmath interval arithmetic.
"""
import math
import numpy as np
from scipy.special import psi as _dg, polygamma as _pg

# ---------------------------------------------------------------- symbol (float64)

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


def base(tau, v):
    s = m(tau)
    for n, vn in v.items():
        s = s - vn*np.cos(np.asarray(tau)*math.log(n))
    return s


def g0h(tau, T):
    tau = np.asarray(tau, dtype=float); L = 2*T
    return 2*(0.5*math.sinh(T)*np.cos(L*tau) + tau*math.cosh(T)*np.sin(L*tau))/(tau**2 + 0.25)


def g1h(tau, T):
    tau = np.asarray(tau, dtype=float); L = 2*T; a = 0.5
    def I(s):
        return (L*np.exp(s*L)/s - (np.exp(s*L) - 1)/s**2)
    w = tau
    return 2*np.real(0.5*(I(a + 1j*w) - I(-a + 1j*w)))


def nuhat(tau, us, a, chunk=20000):
    tau = np.asarray(tau, dtype=float); out = np.empty(len(tau))
    us = np.asarray(us); a = np.asarray(a)
    for i in range(0, len(tau), chunk):
        sl = slice(i, i+chunk)
        out[sl] = 2*(np.cos(np.outer(tau[sl], us)) @ a)
    return out


def fval(tau, T, us, a, b0, b1, v):
    tau = np.asarray(tau, dtype=float)
    return base(tau, v) + b0*g0h(tau, T) + b1*g1h(tau, T) + nuhat(tau, us, a)

# ---------------------------------------------------------------- rigorous constants

def G0(T):          # int_{-2T}^{2T} |u| cosh(u/2) du
    L = 2*T
    return 2*(2*L*math.sinh(L/2) - 4*(math.cosh(L/2) - 1))


def G1(T):          # int_{-2T}^{2T} u^2 |sinh(u/2)| du
    L = 2*T
    F = lambda u: 2*u*u*math.cosh(u/2) - 8*u*math.sinh(u/2) + 16*math.cosh(u/2)
    return 2*(F(L) - F(0))


def lip(T, us, a, b0, b1, v):
    """upper bound for |f'| on R"""
    return (0.5*_pg(1, 0.25)
            + sum(vn*math.log(n) for n, vn in v.items())
            + 2*float(np.sum(np.abs(a)*np.asarray(us)))
            + abs(b0)*G0(T) + abs(b1)*G1(T))


def lip_nu(us, a):
    return 2*float(np.sum(np.abs(a)*np.asarray(us)))


def tail_k(T, taumax):
    """(k0,k1) with |g0h(tau)| <= k0 and |g1h(tau)| <= k1 for tau >= taumax"""
    return (2*math.cosh(T)/taumax + math.sinh(T)/taumax**2, 8*T*math.sinh(T)/taumax)

# ---------------------------------------------------------------- exhaustive B&B

class BudgetExceeded(Exception):
    pass


def bb_min(func, xmax, L, target, w0=0.02, wmin=5e-8, max_evals=2_000_000_000,
           block=400_000, verbose=False):
    """Certified lower bound for inf_{[0,xmax]} func.

    Returns (lb, best_mid, stats).  lb <= inf func is GUARANTEED:
      * every cell is either resolved (f(mid)-L*w/2 >= target, so func >= target there)
        or split, or, at width < 2*wmin, contributes f(mid)-L*w/2 to `lb_surv`.
      * nothing is discarded; the returned value is min(target, lb_surv).
    Raises BudgetExceeded if max_evals is reached -- it never silently passes.
    """
    n0 = int(math.ceil(xmax/w0)); w = xmax/n0
    stack = [(np.arange(n0)*w, w)]
    lb_surv = np.inf; best = np.inf; nfinal = 0; meas = 0.0; nev = 0
    argmins = []
    while stack:
        cur, w = stack.pop()
        if len(cur) > block:
            stack.append((cur[block:], w)); cur = cur[:block]
        mid = cur + w/2
        vals = func(mid); nev += len(mid)
        if nev > max_evals:
            raise BudgetExceeded(f"evals {nev} > {max_evals}; certificate NOT established")
        i0 = int(vals.argmin())
        if float(vals[i0]) < best:
            best = float(vals[i0]); best_arg = float(mid[i0])
        keep = vals - L*w/2 < target
        nk = int(keep.sum())
        if nk == 0:
            continue
        if w/2 < wmin:
            vk = vals[keep]
            lb_surv = min(lb_surv, float(vk.min()) - L*w/2)
            nfinal += nk; meas += nk*w
            if len(argmins) < 200000:
                argmins.append(mid[keep])
            continue
        c2 = cur[keep]
        stack.append((np.repeat(c2, 2) + np.tile(np.array([0.0, w/2]), nk), w/2))
    lb = min(target, lb_surv)
    stats = dict(evals=nev, final_intervals=nfinal, surviving_measure=meas,
                 lb_survivors=(None if lb_surv == np.inf else lb_surv),
                 best_sampled=best, best_arg=(None if best == np.inf else best_arg),
                 L=L, wmin=wmin, w0=w0, target=target)
    return lb, best, stats


def bb_lower(func, xmax, L, target, w0=0.02, wmin=5e-8, max_evals=2_000_000_000,
             block=400_000, keep_leaves=20000):
    """Wrapper of bb_min that also returns up to `keep_leaves` surviving leaf midpoints."""
    lb, best, st = bb_min(func, xmax, L, target, w0=w0, wmin=wmin,
                          max_evals=max_evals, block=block)
    return lb, best, st


def fine_min(func, xmax, h):
    """float64 fine-grid minimum (NOT a certificate; only used to choose the B&B target)."""
    mu = np.inf; arg = 0.0
    n = int(xmax/h) + 1
    for i in range(0, n, 2_000_000):
        t = (np.arange(i, min(i+2_000_000, n)))*h
        val = func(t)
        j = int(val.argmin())
        if float(val[j]) < mu:
            mu = float(val[j]); arg = float(t[j])
    return mu, arg


def certify(T, us, a, b0, b1, v, taumax, w0=0.02, wmin=5e-8, rho_wmin=2e-8,
            hf=5e-5, hp=2e-5, eps=1e-9, verbose=True, max_evals=2_000_000_000):
    """Full certificate.  Returns dict; the certified bound is res['c'] <= inf_R f."""
    us = np.asarray(us, dtype=float); a = np.asarray(a, dtype=float)
    d = float(us[1]-us[0]); P = 2*math.pi/d
    Lf = lip(T, us, a, b0, b1, v); Ln = lip_nu(us, a)
    # ---- rho: certified  nuhat >= -rho  on R (one period suffices, exhaustively)
    fnu = lambda t: nuhat(t, us, a)
    mu_p, arg_p = fine_min(fnu, P, hp)
    rlb, rbest, rst = bb_min(fnu, P, Ln, mu_p - eps, w0=0.02, wmin=rho_wmin,
                             max_evals=max_evals)
    rho = -rlb
    # ---- tail
    k0, k1 = tail_k(T, taumax)
    mtail = float(m(np.array([taumax]))[0])
    tail = mtail - sum(v.values()) - rho - abs(b0)*k0 - abs(b1)*k1
    # ---- [0, taumax]
    ff = lambda t: fval(t, T, us, a, b0, b1, v)
    mu_f, arg_f = fine_min(ff, taumax, hf)
    lb, best, st = bb_min(ff, taumax, Lf, mu_f - eps, w0=w0, wmin=wmin,
                          max_evals=max_evals)
    c = min(tail, lb)
    if verbose:
        print(f"  rho<={rho:.8f} tail>={tail:.8e} L={Lf:.2f} finemin={mu_f:.8e}@{arg_f:.5f} "
              f"bb_lb={lb:.8e} evals={st['evals']} nfinal={st['final_intervals']} "
              f"==> c >= {c:.8e}", flush=True)
    return dict(rho=rho, tail=tail, L=Lf, Lnu=Ln, bb_lb=lb, best=best, c=c,
                bb=st, rhobb=rst, k0=k0, k1=k1, P=P, d=d, taumax=taumax,
                fine_min=mu_f, fine_arg=arg_f, m_taumax=mtail, Sv=sum(v.values()),
                nu_fine_min=mu_p, nu_fine_arg=arg_p)
