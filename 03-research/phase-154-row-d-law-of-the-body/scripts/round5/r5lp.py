"""R154 round 5 -- graded-tail LP (Lemma F1) for a general T in (1/2 log 3, log 2].

Variables: c, a_j (j = M..J), b0, b1, t0 >= |b0|, t1 >= |b1|.
Rows:  c <= f(tau) on a grid of [0, tau1];  c <= h_k(x) on a grid of one period, k = 0..N.
Cuts: violated points of a 100x finer grid are appended and the LP re-solved.
"""
import argparse, math, pickle, time
import numpy as np
from scipy.optimize import linprog
import r5core as C


def Wrows(T, xs, P, v, N):
    out = []; Sv = sum(v.values())
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = C.kk(T, tk)
        rhs = (C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
               if k < N else C.m(tk) - Sv)
        out.append((tk, k0, k1, rhs))
    return out


def solve(T, us, tau, xs, P, v, N):
    n = len(us); nv = 1 + n + 4
    iA, iB0, iB1, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n
    blocks = []; rhss = []
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -C.g0h(tau, T); R1[:, iB1] = -C.g1h(tau, T)
    blocks.append(R1); rhss.append(C.base(tau, v))
    Cx = -2*np.cos(np.outer(xs, us))
    for tk, k0, k1, rhs in Wrows(T, xs, P, v, N):
        R = np.zeros((len(xs), nv)); R[:, 0] = 1.0
        R[:, iA:iA+n] = Cx; R[:, iT0] = k0; R[:, iT1] = k1
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


def hv_all(T, xf, us, a, P, v, N, b0, b1):
    nu = C.nuhat(xf, us, a)
    out = np.empty((N+1, len(xf)))
    for k, (tk, k0, k1, rhs) in enumerate(Wrows(T, xf, P, v, N)):
        out[k] = nu + rhs - abs(b0)*k0 - abs(b1)*k1
    return out


def run(T, M=24, U=20.0, tau1=30.0, N=2, dlo=0.002, dper=0.003, cuts=10,
        hf=2e-5, hp=2e-5, tag=''):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    tau = np.arange(1e-7, tau1, dlo); xs = tau1 + np.arange(0.0, P, dper)
    tf = np.arange(1e-8, tau1, hf); xf = tau1 + np.arange(0.0, P, hp)
    print(f"[{tag}] T={T:.6f} v={ {n: round(x,6) for n,x in v.items()} } M={M} atoms={len(us)} "
          f"P={P:.3f} tau1={tau1} N={N}", flush=True)
    for it in range(cuts):
        t0 = time.time()
        sol = solve(T, us, tau, xs, P, v, N)
        if sol is None:
            print(f"[{tag}] LP infeasible", flush=True); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        fv = C.fval(tf, T, us, a, b0, b1, v)
        hv = hv_all(T, xf, us, a, P, v, N, b0, b1)
        mf = float(fv.min()); mh = float(hv.min())
        print(f"[{tag}] it{it} rows={sol['nrows']} LPc={sol['c']:.6e} fmin={mf:.6e} "
              f"hmin={mh:.6e} hk={np.array2string(hv.min(axis=1),precision=4)} "
              f"|a|1={np.abs(a).sum():.2f} b0={b0:.6f} b1={b1:.6f} "
              f"({time.time()-t0:.0f}s)", flush=True)
        out = dict(T=T, M=M, U=U, d=d, us=us, a=a, b0=b0, b1=b1, lp=sol['c'], tau1=tau1,
                   N=N, P=P, v=v, fine=mf, hmin=mh, tag=tag, graded2=True, it=it)
        pickle.dump(out, open(f'lp_{tag}_it{it}.pkl', 'wb'))
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
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=float, required=True)
    ap.add_argument('--M', type=int, default=24)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--dlo', type=float, default=0.002)
    ap.add_argument('--dper', type=float, default=0.003)
    ap.add_argument('--cuts', type=int, default=10)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    tag = A.out or f"T{A.T:g}M{A.M}"
    r = run(A.T, M=A.M, U=A.U, tau1=A.tau1, N=A.N, dlo=A.dlo, dper=A.dper,
            cuts=A.cuts, tag=tag)
    if r: pickle.dump(r, open(f'lp_{tag}.pkl', 'wb'))
