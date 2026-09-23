"""R154 round 6 -- ROW + COLUMN generation for the graded-tail atom LP.

r6lp.py generates rows but keeps all n = |{u_j}| atom columns; with n ~ 10^3 free
variables HiGHS needs minutes per solve.  Here the atoms are generated too:

  * start from a sparse subset S of the atom pool (every `--cstep`-th lattice point);
  * solve the LP on (current rows) x (S);
  * ROW separation: refined local minima of f, h_0..h_N below the LP value  ->  new rows;
  * COLUMN pricing: for every pooled atom u not in S the reduced cost is
        d(u) = sum_i lambda_i * A_i(u),   A_i(u) = -2 cos(u * tau_i),
    with lambda the row duals; a_u is a FREE variable, so |d(u)| > ctol means adding the
    atom strictly improves the LP.  The `--cadd` atoms with the largest |d(u)| are added.
  * stop when no row and no column prices out.

Atoms not in S simply carry a_j = 0, so every iterate is a legitimate member of the same
certificate class.  With `--offlat` the pool is a fine NON-lattice grid of [2T, 2T+U]:
this tests Theorem D1's "atomic, not necessarily lattice" measures on [0, tau1] (the graded
tail lemma then no longer applies, so such runs are DIAGNOSTIC only).
"""
import argparse, math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, '../round5')
import r5core as C
import r6lp as R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=float, required=True)
    ap.add_argument('--M', type=int, default=24)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--h0f', type=float, default=0.03)
    ap.add_argument('--h0h', type=float, default=0.08)
    ap.add_argument('--h_sep', type=float, default=0.005)
    ap.add_argument('--cstep', type=int, default=8)
    ap.add_argument('--cadd', type=int, default=60)
    ap.add_argument('--ctol', type=float, default=1e-9)
    ap.add_argument('--iters', type=int, default=200)
    ap.add_argument('--patience', type=int, default=25)
    ap.add_argument('--slacktol', type=float, default=0.02)
    ap.add_argument('--keepage', type=int, default=6)
    ap.add_argument('--offlat', type=int, default=0, help='pool size for off-lattice atoms')
    ap.add_argument('--maxsec', type=float, default=1e9)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    T = A.T; v = C.vdict(T); d = 2*T/A.M; J = int((2*T+A.U)/d)
    pool = np.arange(A.M, J+1)*d
    P = 2*math.pi/d
    if A.offlat:
        pool = 2*T + (A.U)*(np.arange(A.offlat)+0.5)/A.offlat
    tau1 = A.tau1; N = A.N
    tag = A.out or f"G{T:g}M{A.M}"
    S = np.arange(0, len(pool), A.cstep)
    pts = {'f': np.arange(1e-7, tau1, A.h0f)}
    for k in range(N+1): pts[f'h{k}'] = tau1 + np.arange(0.0, P, A.h0h)
    base = {w: q.copy() for w, q in pts.items()}
    age = {w: np.zeros(len(q)) for w, q in pts.items()}
    print(f"[{tag}] T={T:.6f} M={A.M} U={A.U} pool={len(pool)} start_cols={len(S)} "
          f"P={P:.3f} tau1={tau1} N={N} offlat={A.offlat}", flush=True)
    best = -np.inf; bestit = 0; out = None; t00 = time.time()
    for it in range(A.iters):
        us = pool[S]; n = len(us); nv = 5 + n
        cv = np.zeros(nv); cv[0] = -1.0
        bnds = [(None, None)]*(3+n) + [(0, None)]*2
        R4 = np.zeros((4, nv))
        R4[0, 1+n] = 1; R4[0, 3+n] = -1
        R4[1, 1+n] = -1; R4[1, 3+n] = -1
        R4[2, 2+n] = 1; R4[2, 4+n] = -1
        R4[3, 2+n] = -1; R4[3, 4+n] = -1
        blocks = [R4]; rhss = [np.zeros(4)]; tally = []
        A_, b_ = R.rows_f(T, pts['f'], us, v, nv, n)
        blocks.append(A_); rhss.append(b_); tally.append(('f', len(pts['f'])))
        for k in range(N+1):
            A_, b_ = R.rows_h(T, pts[f'h{k}'], k, P, v, N, us, nv, n)
            blocks.append(A_); rhss.append(b_); tally.append((f'h{k}', len(pts[f'h{k}'])))
        Aub = np.vstack(blocks); bub = np.concatenate(rhss)
        Sc = 1e4; Aub *= Sc; bub *= Sc
        t0 = time.time()
        res = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
        tlp = time.time()-t0
        if not res.success:
            print(f"[{tag}] it{it} LP fail: {res.message}", flush=True)
            if it == 0: return
            break
        x = res.x; c = float(x[0]); a = x[1:1+n]
        b0 = float(x[1+n]); b1 = float(x[2+n])
        lam = np.asarray(res.ineqlin.marginals)
        # ---- column pricing over the whole pool
        allpts = np.concatenate([pts['f']] + [pts[f'h{k}'] for k in range(N+1)])
        lamrow = lam[4:]
        dcol = -2.0*Sc*(np.cos(np.outer(pool, allpts)) @ lamrow)
        dcol[S] = 0.0
        order = np.argsort(-np.abs(dcol))
        newc = order[:A.cadd][np.abs(dcol[order[:A.cadd]]) > A.ctol]
        # ---- row separation
        t1 = time.time()
        mins, gm, gw, gx = R.separate(T, v, us, a, b0, b1, P, N, tau1, A.h_sep, 6)
        tsep = time.time()-t1
        print(f"[{tag}] it{it} rows={Aub.shape[0]} cols={n} LPc={c:.10e} "
              f"truemin={gm:.10e} gap={c-gm:.3e} ({gw}@{gx:.3f}) newcols={len(newc)} "
              f"maxprice={np.abs(dcol).max():.3e} |a|1={np.abs(a).sum():.2f} "
              f"b0={b0:.5f} b1={b1:.5f} lp={tlp:.0f}s sep={tsep:.0f}s", flush=True)
        cur = dict(T=T, M=A.M, U=A.U, d=d, us=us, a=a, b0=b0, b1=b1, lp=c, tau1=tau1,
                   N=N, P=P, v=v, tag=tag, graded2=(A.offlat == 0), it=it, fine=gm,
                   hmin=gm, method='row+column generation', cols=n,
                   rows=int(Aub.shape[0]), wall=time.time()-t00, ub=c)
        if gm > best:
            best = gm; bestit = it; out = cur
            pickle.dump(out, open(f'lp_{tag}.pkl', 'wb'))
        pickle.dump(cur, open(f'lp_{tag}_last.pkl', 'wb'))
        nadd = 0
        slack = bub - Aub @ x
        keep = (slack < A.slacktol*Sc) | (np.abs(lam) > 0)
        off = 4; newpts = {}; newage = {}
        for w, cnt in tally:
            kk_ = keep[off:off+cnt] | np.isin(pts[w], base[w]) | (age[w] > it - A.keepage)
            off += cnt
            newpts[w] = pts[w][kk_]; newage[w] = age[w][kk_]
        pts = newpts; age = newage
        for w, (xm, vm) in mins.items():
            if not len(xm): continue
            bad = np.where(vm < c - 1e-12)[0]
            if not len(bad): continue
            lo, hi = (0.0, tau1) if w == 'f' else (tau1, tau1+P)
            add = np.clip(xm[bad], lo, hi)
            allp = np.concatenate([pts[w], add])
            alla = np.concatenate([age[w], np.full(len(add), it+1.0)])
            o = np.argsort(allp); allp = allp[o]; alla = alla[o]
            u, iu = np.unique(allp, return_index=True)
            pts[w] = u; age[w] = alla[iu]
            nadd += len(add)
        if len(newc):
            S = np.union1d(S, newc)
        if nadd == 0 and len(newc) == 0:
            print(f"[{tag}] CONVERGED it{it}: c={c:.10e} truemin={gm:.10e} "
                  f"cols={n} wall={time.time()-t00:.0f}s", flush=True)
            break
        if it - bestit >= A.patience or time.time()-t00 > A.maxsec:
            print(f"[{tag}] STOP it{it}: best truemin={best:.10e} at it{bestit}; "
                  f"last LP upper bound={c:.10e}; wall={time.time()-t00:.0f}s", flush=True)
            break
    print(f"[{tag}] done best={best:.10e} wall={time.time()-t00:.0f}s", flush=True)


if __name__ == '__main__':
    main()
