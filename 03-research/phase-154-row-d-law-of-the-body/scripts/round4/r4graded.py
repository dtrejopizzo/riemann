"""R154 round 4, Lemma D2.2 (GRADED periodic tail) and its LP.

Lemma D2.1 (round 3) bounded  f >= m(taumax) - sum v - rho - |b|k(taumax)  on [taumax,oo)
with rho = -min nuhat, and needed explicit rows on the whole of [tau1, taumax].
Since nuhat is P-periodic and m is increasing, that is wasteful: writing tau = x + kP with
x in [0,P) and k >= 0, the binding member of each residue class is the SMALLEST tau >= tau1,
    tau*(x) = x + P*max(0, ceil((tau1-x)/P)).
Hence, for every tau >= tau1,
    f(tau) >= nuhat(x) + W(x),
    W(x) := m(tau*(x)) - sum_n v_n - |b0| k0(tau*(x)) - |b1| k1(tau*(x)),
    k0(t) = 2 cosh(T)/t + sinh(T)/t^2,  k1(t) = 8 T sinh(T)/t.
So  f >= c  on [tau1, oo)  <==>  nuhat(x) + W(x) >= c  for all x in [0,P):
ONE period of rows replaces the whole of [tau1, oo).  No rho, no taumax.
"""
import argparse, math, pickle, time
import numpy as np
from scipy.optimize import linprog
import r4core as C


def tau_star(x, tau1, P):
    x = np.asarray(x, dtype=float)
    k = np.maximum(np.ceil((tau1 - x)/P), 0.0)
    return x + k*P


def solve(T, us, tau, xs, tau1, P, v):
    n = len(us); Sv = sum(v.values())
    nv = 1 + n + 4
    iA, iB0, iB1, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -C.g0h(tau, T); R1[:, iB1] = -C.g1h(tau, T)
    b1v = C.base(tau, v)
    ts = tau_star(xs, tau1, P)
    k0 = 2*math.cosh(T)/ts + math.sinh(T)/ts**2
    k1 = 8*T*math.sinh(T)/ts
    R2 = np.zeros((len(xs), nv)); R2[:, 0] = 1.0
    R2[:, iA:iA+n] = -2*np.cos(np.outer(xs, us))
    R2[:, iT0] = k0; R2[:, iT1] = k1
    b2v = C.m(ts) - Sv
    R4 = np.zeros((4, nv))
    R4[0, iB0] = 1; R4[0, iT0] = -1
    R4[1, iB0] = -1; R4[1, iT0] = -1
    R4[2, iB1] = 1; R4[2, iT1] = -1
    R4[3, iB1] = -1; R4[3, iT1] = -1
    Aub = np.vstack([R1, R2, R4])
    bub = np.concatenate([b1v, b2v, np.zeros(4)])
    cv = np.zeros(nv); cv[0] = -1.0
    bnds = [(None, None)]*(1+n+2) + [(0, None)]*2
    r = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    if not r.success: return None
    x = r.x
    return dict(c=float(x[0]), a=x[iA:iA+n], b0=float(x[iB0]), b1=float(x[iB1]),
                nrows=Aub.shape[0])


def Wfun(x, T, tau1, P, b0, b1, v):
    ts = tau_star(x, tau1, P)
    k0 = 2*math.cosh(T)/ts + math.sinh(T)/ts**2
    k1 = 8*T*math.sinh(T)/ts
    return C.m(ts) - sum(v.values()) - abs(b0)*k0 - abs(b1)*k1


def hfun(x, T, us, a, tau1, P, b0, b1, v):
    return C.nuhat(x, us, a) + Wfun(x, T, tau1, P, b0, b1, v)


def run(T, M=19, U=20.0, tau1=30.0, dlo=0.002, dper=0.002, cuts=12,
        hf=2e-5, hp=2e-5, tag=''):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    tau = np.arange(1e-7, tau1, dlo)
    xs = np.arange(0.0, P, dper)
    tf = np.arange(1e-8, tau1, hf); xf = np.arange(0.0, P, hp)
    print(f"[{tag}] M={M} U={U} tau1={tau1} atoms={len(us)} P={P:.3f} "
          f"rows {len(tau)}+{len(xs)}", flush=True)
    sol = None
    for it in range(cuts):
        t0 = time.time()
        sol = solve(T, us, tau, xs, tau1, P, v)
        if sol is None:
            print(f"[{tag}] LP infeasible", flush=True); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        fv = C.fval(tf, T, us, a, b0, b1, v)
        hv = hfun(xf, T, us, a, tau1, P, b0, b1, v)
        mf = float(fv.min()); mh = float(hv.min())
        print(f"[{tag}] it{it} rows={sol['nrows']} LPc={sol['c']:.6e} "
              f"fmin={mf:.6e}@{tf[fv.argmin()]:.5f} hmin={mh:.6e}@{xf[hv.argmin()]:.5f} "
              f"|a|1={np.abs(a).sum():.2f} b0={b0:.6f} b1={b1:.6f} ({time.time()-t0:.0f}s)",
              flush=True)
        vi = np.where(fv < sol['c'] - 1e-11)[0]
        hi = np.where(hv < sol['c'] - 1e-11)[0]
        if len(vi) == 0 and len(hi) == 0:
            print(f"[{tag}] converged", flush=True); break
        if len(vi):
            tau = np.unique(np.concatenate([tau, tf[vi[np.argsort(fv[vi])][:6000]]]))
        if len(hi):
            xs = np.unique(np.concatenate([xs, xf[hi[np.argsort(hv[hi])][:6000]]]))
    return dict(T=T, M=M, U=U, d=d, us=us, a=sol['a'], b0=sol['b0'], b1=sol['b1'],
                lp=sol['c'], tau1=tau1, P=P, v=v, fine=mf, hmin=mh, tag=tag,
                graded=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--M', type=int, default=19)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--dlo', type=float, default=0.002)
    ap.add_argument('--dper', type=float, default=0.002)
    ap.add_argument('--cuts', type=int, default=12)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    T = 0.5*math.log(3)
    tag = A.out or f"g_M{A.M}t{A.tau1:g}"
    r = run(T, M=A.M, U=A.U, tau1=A.tau1, dlo=A.dlo, dper=A.dper, cuts=A.cuts, tag=tag)
    if r:
        pickle.dump(r, open(f'lp_{tag}.pkl', 'wb'))
