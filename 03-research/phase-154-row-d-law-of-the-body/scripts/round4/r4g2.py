"""R154 round 4 -- Lemma D2.3 (graded periodic tail, prime term exact for N periods).

nuhat is P-periodic.  Write tau >= tau1 as tau = x + kP with x = tau*(x) in [tau1, tau1+P)
the FIRST preimage >= tau1 and k = 0,1,2,....  Then nuhat(tau) = nuhat(x) and

  f(tau) = m(tau) - v2 cos(tau log 2) + nuhat(x) + b0 g0h(tau) + b1 g1h(tau)
         >= nuhat(x) + W_k(x),
  W_k(x) := m(x+kP) - v2 cos((x+kP) log 2) - |b0| k0(x+kP) - |b1| k1(x+kP),   k < N,
  W_N(x) := m(x+NP) - sum_n v_n - |b0| k0(x+NP) - |b1| k1(x+NP)   (worst case, valid all k>=N,
            because m is increasing and k0,k1 are decreasing).

So   f >= c on [tau1, oo)   <==>   nuhat(x) + W_k(x) >= c for all x in [tau1, tau1+P) and
k = 0..N.  ONE period of phases, N+1 row families -- no taumax, no flat rho, and the prime
term is exact on the first N periods.  For N = 2 and tau1 = 30 the worst-case floor W_2 is
already 2.67 (vs. 2.23 for the flat lemma D2.1 at taumax = 160).
"""
import argparse, math, pickle, time
import numpy as np
from scipy.optimize import linprog
import r4core as C


def kk(T, t):
    return (2*math.cosh(T)/t + math.sinh(T)/t**2, 8*T*math.sinh(T)/t)


def Wrows(T, xs, P, v, N):
    """list of (tau_k array, rhs array) for k = 0..N (k = N is the worst-case family)"""
    out = []
    Sv = sum(v.values())
    l2 = math.log(2)
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = kk(T, tk)
        if k < N:
            rhs = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
        else:
            rhs = C.m(tk) - Sv
        out.append((tk, k0, k1, rhs))
    return out


def solve(T, us, tau, xs, P, v, N):
    n = len(us)
    nv = 1 + n + 4
    iA, iB0, iB1, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n
    blocks = []; rhss = []
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -C.g0h(tau, T); R1[:, iB1] = -C.g1h(tau, T)
    blocks.append(R1); rhss.append(C.base(tau, v))
    Cx = -2*np.cos(np.outer(xs, us))
    for tk, k0, k1, rhs in Wrows(T, xs, P, v, N):
        R = np.zeros((len(xs), nv)); R[:, 0] = 1.0
        R[:, iA:iA+n] = Cx
        R[:, iT0] = k0; R[:, iT1] = k1
        blocks.append(R); rhss.append(rhs)
    R4 = np.zeros((4, nv))
    R4[0, iB0] = 1; R4[0, iT0] = -1
    R4[1, iB0] = -1; R4[1, iT0] = -1
    R4[2, iB1] = 1; R4[2, iT1] = -1
    R4[3, iB1] = -1; R4[3, iT1] = -1
    blocks.append(R4); rhss.append(np.zeros(4))
    Aub = np.vstack(blocks); bub = np.concatenate(rhss)
    cv = np.zeros(nv); cv[0] = -1.0
    bnds = [(None, None)]*(1+n+2) + [(0, None)]*2
    r = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    if not r.success: return None
    x = r.x
    return dict(c=float(x[0]), a=x[iA:iA+n], b0=float(x[iB0]), b1=float(x[iB1]),
                nrows=Aub.shape[0])


def hvals(T, xs, us, a, P, v, N, b0, b1):
    """h_k(x) = nuhat(x) + W_k(x) for k = 0..N, as an (N+1, len(xs)) array"""
    nu = C.nuhat(xs, us, a)
    out = np.empty((N+1, len(xs)))
    for k, (tk, k0, k1, rhs) in enumerate(Wrows(T, xs, P, v, N)):
        out[k] = nu + rhs - abs(b0)*k0 - abs(b1)*k1
    return out


def run(T, M=19, U=20.0, tau1=30.0, N=2, dlo=0.002, dper=0.003, cuts=12,
        hf=2e-5, hp=2e-5, tag=''):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    tau = np.arange(1e-7, tau1, dlo)
    xs = tau1 + np.arange(0.0, P, dper)
    tf = np.arange(1e-8, tau1, hf); xf = tau1 + np.arange(0.0, P, hp)
    print(f"[{tag}] M={M} U={U} tau1={tau1} N={N} atoms={len(us)} P={P:.3f} "
          f"rows {len(tau)}+{(N+1)*len(xs)}", flush=True)
    sol = None
    for it in range(cuts):
        t0 = time.time()
        sol = solve(T, us, tau, xs, P, v, N)
        if sol is None:
            print(f"[{tag}] LP infeasible", flush=True); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        fv = C.fval(tf, T, us, a, b0, b1, v)
        hv = hvals(T, xf, us, a, P, v, N, b0, b1)
        hmin = hv.min(axis=1)
        mf = float(fv.min()); mh = float(hv.min())
        print(f"[{tag}] it{it} rows={sol['nrows']} LPc={sol['c']:.6e} "
              f"fmin={mf:.6e}@{tf[fv.argmin()]:.5f} hmin={mh:.6e} "
              f"hk={np.array2string(hmin, precision=4)} |a|1={np.abs(a).sum():.2f} "
              f"b0={b0:.6f} b1={b1:.6f} ({time.time()-t0:.0f}s)", flush=True)
        pickle.dump(dict(T=T, M=M, U=U, d=d, us=us, a=a, b0=b0, b1=b1, lp=sol['c'],
                         tau1=tau1, N=N, P=P, v=v, fine=mf, hmin=mh, tag=tag,
                         graded2=True, it=it), open(f'lp_{tag}_it{it}.pkl', 'wb'))
        vi = np.where(fv < sol['c'] - 1e-11)[0]
        add = []
        for k in range(N+1):
            j = np.where(hv[k] < sol['c'] - 1e-11)[0]
            if len(j): add.append(xf[j[np.argsort(hv[k][j])][:4000]])
        if len(vi) == 0 and not add:
            print(f"[{tag}] converged", flush=True); break
        if len(vi):
            tau = np.unique(np.concatenate([tau, tf[vi[np.argsort(fv[vi])][:6000]]]))
        if add:
            xs = np.unique(np.concatenate([xs] + add))
    return dict(T=T, M=M, U=U, d=d, us=us, a=sol['a'], b0=sol['b0'], b1=sol['b1'],
                lp=sol['c'], tau1=tau1, N=N, P=P, v=v, fine=mf, hmin=mh, tag=tag,
                graded2=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--M', type=int, default=19)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--dlo', type=float, default=0.002)
    ap.add_argument('--dper', type=float, default=0.003)
    ap.add_argument('--cuts', type=int, default=12)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    T = 0.5*math.log(3)
    tag = A.out or f"g2_M{A.M}t{A.tau1:g}N{A.N}"
    r = run(T, M=A.M, U=A.U, tau1=A.tau1, N=A.N, dlo=A.dlo, dper=A.dper,
            cuts=A.cuts, tag=tag)
    if r:
        pickle.dump(r, open(f'lp_{tag}.pkl', 'wb'))
