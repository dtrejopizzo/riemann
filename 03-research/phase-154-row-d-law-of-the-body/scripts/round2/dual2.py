"""R154 round 2, script 2: the TWO-multiplier outside-window certificate (repair R2),
with a *density* (not atoms) so that the tail tau > taumax is rigorously controlled.

  lambda_min(A_T(v)) >= inf_tau [ base(tau) + nuhat(tau) + b0 h0(tau) + b1 h1(tau) ]
  base = Re psi(1/4+i tau/2) - log pi - sum_n v_n cos(tau log n)
  nuhat(tau) = 2 int_{2T}^{2T+U} c(u) cos(u tau) du,  c piecewise constant  (Phi = 0 there)
  h0 = FT of cosh(t/2) 1_{|t|<2T},  h1 = FT of t sinh(t/2) 1_{|t|<2T}   (the two primitivity moments)
Tail: every certificate term is O(1/tau); base is increasing; so the inf over [taumax,inf) is
bounded below explicitly.  Output: LP value, fine-grid verified value, certified tail bound.
"""
import math, sys, numpy as np
from scipy.special import psi as dg
from scipy.optimize import linprog

def base(tau, contacts, v):
    s = np.real(dg(0.25+0.5j*tau)) - math.log(math.pi)
    for n in contacts: s = s - v[n]*np.cos(tau*math.log(n))
    return s

def h0(tau, T):
    L = 2*T
    return 2*(0.5*math.sinh(T)*np.cos(L*tau) + tau*math.cosh(T)*np.sin(L*tau))/(tau**2+0.25)

def h1(tau, T):
    """int_{-2T}^{2T} t sinh(t/2) cos(tau t) dt, exact."""
    L = 2*T; a = 0.5
    # int_0^L t sinh(at) cos(w t) dt  -> closed form via  t e^{at}, t e^{-at}
    def I(s):   # int_0^L t e^{s t} dt with s complex
        return (L*np.exp(s*L)/s - (np.exp(s*L)-1)/s**2)
    w = tau
    val = 0.5*(I(a+1j*w) - I(-a+1j*w))
    return 2*np.real(val)

def run(T, contacts, U=25.0, du=0.05, dtau=0.005, taumax=200.0, cap=50.0, two=True, ref=20):
    L = 2*T
    v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    edges = np.arange(L, L+U+1e-12, du); ncell = len(edges)-1
    tau = np.arange(1e-6, taumax, dtau)
    b = base(tau, contacts, v)
    def cols(t):
        C = 2*(np.sin(np.outer(t, edges[1:])) - np.sin(np.outer(t, edges[:-1])))/t[:, None]
        out = [C, h0(t, T)[:, None]]
        if two: out.append(h1(t, T)[:, None])
        return np.hstack(out)
    nv = cols(tau[:2]).shape[1]
    tf_all = np.arange(1e-9, taumax, dtau/20)
    b_f = base(tf_all, contacts, v)
    def fine_val(coef):
        out = np.empty(len(tf_all))
        for i in range(0, len(tf_all), 20000):
            sl = slice(i, i + 20000)
            out[sl] = b_f[sl] + cols(tf_all[sl]) @ coef
        return out
    act_tau = tau[::8].copy()
    for it in range(15):
        M = cols(act_tau)
        A = np.hstack([np.ones((len(act_tau), 1)), -M])
        c = np.zeros(nv + 1); c[0] = -1
        bnds = [(None, None)] + [(-cap, cap)]*ncell + [(None, None)]*(nv - ncell)
        r = linprog(c, A_ub=A, b_ub=base(act_tau, contacts, v), bounds=bnds, method='highs')
        if not r.success: print("LP failed", r.message); return
        x = r.x; lp = x[0]; cc = x[1:1+ncell]; bs = x[1+ncell:]
        val = fine_val(np.concatenate([cc, bs]))
        best = val.min(); argb = tf_all[val.argmin()]
        viol = np.where(val < lp - 1e-10)[0]
        print(f"    it{it}: LP={lp:.6e} fine={best:.6e} nviol={len(viol)} rows={len(act_tau)}", flush=True)
        if len(viol) == 0: break
        srt = viol[np.argsort(val[viol])][:600]
        act_tau = np.unique(np.concatenate([act_tau, tf_all[srt]]))
    # rigorous tail bound for tau >= taumax
    TV = np.abs(np.diff(cc)).sum() + abs(cc[0]) + abs(cc[-1])
    tail_nu = 2*TV/taumax
    tail_h0 = abs(bs[0])*(2*math.cosh(T)/taumax + math.sinh(T)/taumax**2)
    tail_h1 = abs(bs[-1])*(8*T*math.sinh(T)/taumax) if two else 0.0
    binf = base(np.array([taumax]), contacts, v)[0] - (sum(v.values()) - sum(v[n]*math.cos(taumax*math.log(n)) for n in contacts))
    # base(tau) >= m(taumax) - sum v_n  for tau >= taumax (m increasing)
    mlow = np.real(dg(0.25+0.5j*taumax)) - math.log(math.pi) - sum(v.values())
    tail = mlow - tail_nu - tail_h0 - tail_h1
    print(f"T={T:.6f} {contacts} U={U} du={du} cap={cap} two={two} taumax={taumax}: "
          f"LP={lp:.6e} fine={best:.6e} (tau={argb:.3f}) TAIL>={tail:.4f} "
          f"|c|inf={np.abs(cc).max():.3g} TV={TV:.3g} b0={bs[0]:.4g} b1={bs[-1] if two else 0:.4g}", flush=True)
    return lp, best, tail

if __name__ == '__main__':
    T3 = 0.5*math.log(3); T2 = math.log(2)
    import itertools
    for two in (False, True):
        run(T3, [2], U=14.0, cap=3.0, two=two)
    for U, du, cap in [(25., .05, 10.), (25., .02, 50.), (40., .02, 50.)]:
        run(T3, [2], U=U, du=du, cap=cap, two=True)
    run(T2, [2, 3], U=25., du=.02, cap=50., two=True)
