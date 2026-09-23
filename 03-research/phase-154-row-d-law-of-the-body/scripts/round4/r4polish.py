"""R154 round 4: polish a graded candidate on a very fine grid.

The expensive LP has ~350 atom variables, so its grid must be coarse and its narrow dips
survive.  Once the SHAPE of nu is fixed, only four scalars remain,
    c,  lambda (scale of nuhat),  b0,  b1,
so the same programme can be re-solved on a grid 100x finer (millions of rows, 4 columns),
which removes the discretisation error almost entirely.  Cuts are taken from a grid finer
still.  The output is a candidate whose LP value and true infimum agree to ~1e-6.
"""
import argparse, math, pickle, time
import numpy as np
from scipy.optimize import linprog
import r4core as C
from r4g2 import kk


def blockmat(tau, us, a, G):
    """columns: nuhat restricted to each of G contiguous atom blocks"""
    n = len(us); idx = np.array_split(np.arange(n), G)
    out = np.empty((len(tau), G))
    for g, ii in enumerate(idx):
        out[:, g] = C.nuhat(tau, us[ii], a[ii])
    return out


def build_rows(T, us, a, v, tau, xs, P, N, G=1):
    """returns (A, b) for variables [c, lambda, b0, b1] with t0=|b0|, t1=|b1| handled
    by two extra vars t0,t1 -> variables [c, lam, b0, b1, t0, t1]"""
    Sv = sum(v.values())
    rows = []; rhs = []
    nv = 5 + G
    nu_t = blockmat(tau, us, a, G)
    R = np.zeros((len(tau), nv)); R[:, 0] = 1.0
    R[:, 1:1+G] = -nu_t; R[:, 1+G] = -C.g0h(tau, T); R[:, 2+G] = -C.g1h(tau, T)
    rows.append(R); rhs.append(C.base(tau, v))
    nu_x = blockmat(xs, us, a, G)
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = kk(T, tk)
        if k < N:
            b = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
        else:
            b = C.m(tk) - Sv
        R = np.zeros((len(xs), nv)); R[:, 0] = 1.0
        R[:, 1:1+G] = -nu_x; R[:, 3+G] = k0; R[:, 4+G] = k1
        rows.append(R); rhs.append(b)
    R4 = np.zeros((4, nv))
    R4[0, 1+G] = 1; R4[0, 3+G] = -1
    R4[1, 1+G] = -1; R4[1, 3+G] = -1
    R4[2, 2+G] = 1; R4[2, 4+G] = -1
    R4[3, 2+G] = -1; R4[3, 4+G] = -1
    rows.append(R4); rhs.append(np.zeros(4))
    return np.vstack(rows), np.concatenate(rhs)


def scaled(us, a, lam, G):
    idx = np.array_split(np.arange(len(us)), G)
    a2 = a.copy()
    for g, ii in enumerate(idx): a2[ii] = a[ii]*lam[g]
    return a2


def vals(T, us, a2, v, b0, b1, tau, xs, P, N):
    fv = C.base(tau, v) + C.nuhat(tau, us, a2) + b0*C.g0h(tau, T) + b1*C.g1h(tau, T)
    nu_x = C.nuhat(xs, us, a2)
    hs = []
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = kk(T, tk)
        if k < N:
            b = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
        else:
            b = C.m(tk) - sum(v.values())
        hs.append(nu_x + b - abs(b0)*k0 - abs(b1)*k1)
    return fv, hs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl')
    ap.add_argument('--h0', type=float, default=1e-3)
    ap.add_argument('--hf', type=float, default=5e-6)
    ap.add_argument('--rounds', type=int, default=14)
    ap.add_argument('--ncut', type=int, default=120000)
    ap.add_argument('--G', type=int, default=1)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb'))
    T, v = r['T'], r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    tag = A.out or (r.get('tag', 'c') + 'p')
    tau = np.arange(1e-7, tau1, A.h0)
    xs = tau1 + np.arange(0.0, P, A.h0)
    tf = np.arange(1e-8, tau1, A.hf); xf = tau1 + np.arange(0.0, P, A.hf)
    print(f"[{tag}] tau1={tau1} P={P:.4f} N={N} atoms={len(a)} "
          f"fine {len(tf)}+{len(xf)}", flush=True)
    sol = None
    for it in range(A.rounds):
        t0 = time.time()
        G = A.G
        Aub, bub = build_rows(T, us, a, v, tau, xs, P, N, G)
        cv = np.zeros(5+G); cv[0] = -1.0
        bnds = [(None, None)]*(3+G) + [(0, None)]*2
        res = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
        if not res.success:
            print("LP fail", res.message); return
        c = res.x[0]; lam = res.x[1:1+G]; b0 = res.x[1+G]; b1 = res.x[2+G]
        a2 = scaled(us, a, lam, G)
        fv, hs = vals(T, us, a2, v, b0, b1, tf, xf, P, N)
        mf = float(fv.min()); mh = [float(h.min()) for h in hs]
        print(f"[{tag}] it{it} rows={Aub.shape[0]} LPc={c:.8e} lam=[{lam.min():.4f},{lam.max():.4f}] "
              f"b0={b0:.6f} b1={b1:.6f} fmin={mf:.8e} hmin={min(mh):.8e} "
              f"hk={np.array2string(np.array(mh), precision=5)} ({time.time()-t0:.0f}s)",
              flush=True)
        pickle.dump(dict(r, a=a2, b0=float(b0), b1=float(b1), lp=float(c), tag=tag,
                         polished_from=A.pkl, lam=[float(x) for x in lam], it=it),
                    open(f'lp_{tag}_it{it}.pkl', 'wb'))
        vi = np.where(fv < c - 1e-12)[0]
        adds = []
        for k in range(N+1):
            j = np.where(hs[k] < c - 1e-12)[0]
            if len(j):
                adds.append(xf[j[np.argsort(hs[k][j])][:A.ncut]])
        if len(vi) == 0 and not adds:
            print(f"[{tag}] converged", flush=True); break
        if len(vi):
            tau = np.unique(np.concatenate([tau, tf[vi[np.argsort(fv[vi])][:A.ncut]]]))
        if adds:
            xs = np.unique(np.concatenate([xs] + adds))
    out = dict(r, a=a2, b0=float(b0), b1=float(b1), lp=float(c), tag=tag,
               polished_from=A.pkl, lam=[float(x) for x in lam])
    pickle.dump(out, open(f'lp_{tag}.pkl', 'wb'))
    print(f"saved lp_{tag}.pkl", flush=True)


if __name__ == '__main__':
    main()
