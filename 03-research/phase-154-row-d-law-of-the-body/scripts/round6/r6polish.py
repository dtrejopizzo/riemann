"""R154 round 6 -- cutting-plane BLOCK POLISH (round 5's F2 stage, with generated rows).

Same programme as r5polish.py: the atom profile a is frozen as a SHAPE and the free
variables are G block scalings lam_g (a_j -> lam_{g(j)} a_j), plus b0, b1, t0, t1 and c.
Round 5 built this on a 2*10^5-row fixed grid; here the rows are generated exactly as in
r6lp.py (scan + refined local minima + slack-based row management), so the polish costs
a few thousand rows and applies at any M.
"""
import argparse, math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, '../round5')
import r5core as C
import r6lp as R


def blockmat(tau, us, a, idx):
    out = np.empty((len(tau), len(idx)))
    for g, ii in enumerate(idx):
        out[:, g] = C.nuhat(tau, us[ii], a[ii])
    return out


def scaled(us, a, lam, idx):
    a2 = a.copy()
    for g, ii in enumerate(idx):
        a2[ii] = a[ii]*lam[g]
    return a2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl')
    ap.add_argument('--G', type=int, default=128)
    ap.add_argument('--h0f', type=float, default=0.02)
    ap.add_argument('--h0h', type=float, default=0.05)
    ap.add_argument('--h_sep', type=float, default=0.005)
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--patience', type=int, default=6)
    ap.add_argument('--slacktol', type=float, default=0.02)
    ap.add_argument('--keepage', type=int, default=5)
    ap.add_argument('--tol', type=float, default=1e-7)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb'))
    T, v = float(r['T']), r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a0 = np.asarray(r['a']); us = np.asarray(r['us'])
    G = min(A.G, len(a0)); idx = np.array_split(np.arange(len(a0)), G)
    tag = A.out or (r.get('tag', 'x') + 'p')
    nv = 5 + G
    cv = np.zeros(nv); cv[0] = -1.0
    bnds = [(None, None)]*(3+G) + [(0, None)]*2
    R4 = np.zeros((4, nv))
    R4[0, 1+G] = 1; R4[0, 3+G] = -1
    R4[1, 1+G] = -1; R4[1, 3+G] = -1
    R4[2, 2+G] = 1; R4[2, 4+G] = -1
    R4[3, 2+G] = -1; R4[3, 4+G] = -1
    pts = {'f': np.arange(1e-7, tau1, A.h0f)}
    for k in range(N+1): pts[f'h{k}'] = tau1 + np.arange(0.0, P, A.h0h)
    base = {w: q.copy() for w, q in pts.items()}
    age = {w: np.zeros(len(q)) for w, q in pts.items()}
    print(f"[{tag}] polish T={T} atoms={len(a0)} G={G} P={P:.3f} tau1={tau1} N={N}", flush=True)
    best = -np.inf; bestit = 0; out = None; t00 = time.time()
    for it in range(A.iters):
        t0 = time.time()
        blocks = [R4]; rhss = [np.zeros(4)]; tally = []
        Bf = blockmat(pts['f'], us, a0, idx)
        M_ = np.zeros((len(pts['f']), nv)); M_[:, 0] = 1.0; M_[:, 1:1+G] = -Bf
        M_[:, 1+G] = -C.g0h(pts['f'], T); M_[:, 2+G] = -C.g1h(pts['f'], T)
        blocks.append(M_); rhss.append(C.base(pts['f'], v)); tally.append(('f', len(pts['f'])))
        for k in range(N+1):
            x_ = pts[f'h{k}']; Bx = blockmat(x_, us, a0, idx)
            M_ = np.zeros((len(x_), nv)); M_[:, 0] = 1.0; M_[:, 1:1+G] = -Bx
            k0, k1 = C.kk(T, x_ + k*P)
            M_[:, 3+G] = k0; M_[:, 4+G] = k1
            blocks.append(M_); rhss.append(R.rhs_k(T, x_, k, P, v, N))
            tally.append((f'h{k}', len(x_)))
        Aub = np.vstack(blocks); bub = np.concatenate(rhss)
        S = 1e4; Aub *= S; bub *= S
        res = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
        if not res.success:
            print(f"[{tag}] LP fail {res.message}", flush=True); return
        x = res.x; c = float(x[0]); lam = x[1:1+G]
        b0 = float(x[1+G]); b1 = float(x[2+G])
        a2 = scaled(us, a0, lam, idx)
        mins, gm, gw, gx = R.separate(T, v, us, a2, b0, b1, P, N, tau1, A.h_sep, 6)
        print(f"[{tag}] it{it} rows={Aub.shape[0]} LPc={c:.10e} truemin={gm:.10e} "
              f"gap={c-gm:.3e} ({gw}@{gx:.4f}) b0={b0:.6f} b1={b1:.6f} "
              f"({time.time()-t0:.0f}s)", flush=True)
        cur = dict(r, a=a2, b0=b0, b1=b1, lp=c, tag=tag, polished_from=A.pkl, G=G,
                   it=it, fine=gm, hmin=gm, lam=[float(z) for z in lam],
                   method='cutting-plane-polish')
        if gm > best:
            best = gm; bestit = it; out = cur
            pickle.dump(out, open(f'lp_{tag}.pkl', 'wb'))
        if it - bestit >= A.patience or c - gm <= A.tol:
            print(f"[{tag}] DONE best truemin={best:.10e} at it{bestit} "
                  f"wall={time.time()-t00:.0f}s", flush=True)
            break
        slack = bub - Aub @ x
        keep = (slack < A.slacktol*S) | (np.abs(np.asarray(res.ineqlin.marginals)) > 0)
        off = 4; newpts = {}; newage = {}
        for w, cnt in tally:
            kk_ = keep[off:off+cnt] | np.isin(pts[w], base[w]) | (age[w] > it - A.keepage)
            off += cnt
            newpts[w] = pts[w][kk_]; newage[w] = age[w][kk_]
        pts = newpts; age = newage
        for w, (xm, vm) in mins.items():
            if not len(xm): continue
            bad = np.where(vm < c - 1e-13)[0]
            if not len(bad): continue
            lo, hi = (0.0, tau1) if w == 'f' else (tau1, tau1+P)
            add = np.clip(xm[bad], lo, hi)
            allp = np.concatenate([pts[w], add])
            alla = np.concatenate([age[w], np.full(len(add), it+1.0)])
            o = np.argsort(allp); allp = allp[o]; alla = alla[o]
            u, iu = np.unique(allp, return_index=True)
            pts[w] = u; age[w] = alla[iu]
    print(f"[{tag}] saved lp_{tag}.pkl  truemin={best:.10e}", flush=True)


if __name__ == '__main__':
    main()
