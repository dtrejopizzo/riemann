"""R154 round 6 -- CUTTING-PLANE (constraint-generation) atom LP for the graded-tail
certificate of Lemma F1 (R154_015 sec.2).  Same programme as round 5's r5lp.py:

    max c   s.t.  c <= f(tau)  on [0,tau1],   c <= h_k(x)  on [tau1,tau1+P), k = 0..N,
    variables (c, a_M..a_J, b0, b1, t0 >= |b0|, t1 >= |b1|).

Round 5 discretised the two intervals ONCE, densely (88 004 rows at M = 24), and the solve
time exploded with the number of atoms (M = 32 did not return in 45 min).  Here the row set
is GENERATED:

  * start from a coarse uniform row set (a few thousand rows);
  * solve;
  * SEPARATION: locate every local minimum of f and of each h_k on a coarse scan grid
    (step h_sep, ~30 points per shortest oscillation 2*pi/u_max) and refine each to ~1e-10
    by iterated 9-point local grids -- this is an exact local-minimum finder, strictly
    sharper than evaluating a uniform 2e-5 grid;
  * append the most violated minima (and their h_sep-neighbours) as new rows;
  * PURGE the rows with zero dual multiplier (they are re-generated if they matter);
  * repeat until  min over all refined local minima  >=  LP value - tol.

At the fixed point the LP value is certified-equal to the true infimum of the current
certificate up to tol, which is exactly the round-5 stopping criterion, at a few thousand
rows instead of ~10^5.
"""
import argparse, math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog

sys.path.insert(0, '../round5')
import r5core as C


# ---------------------------------------------------------------- model pieces

def rhs_k(T, x, k, P, v, N):
    tk = x + k*P
    Sv = sum(v.values())
    if k < N:
        return C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
    return C.m(tk) - Sv


def hvals(T, x, k, P, v, N, us, a, b0, b1):
    k0, k1 = C.kk(T, x + k*P)
    return C.nuhat(x, us, a) + rhs_k(T, x, k, P, v, N) - abs(b0)*k0 - abs(b1)*k1


def fvals(T, x, v, us, a, b0, b1):
    return C.base(x, v) + C.nuhat(x, us, a) + b0*C.g0h(x, T) + b1*C.g1h(x, T)


def rows_f(T, tau, us, v, nv, n):
    R = np.zeros((len(tau), nv)); R[:, 0] = 1.0
    R[:, 1:1+n] = -2*np.cos(np.outer(tau, us))
    R[:, 1+n] = -C.g0h(tau, T); R[:, 2+n] = -C.g1h(tau, T)
    return R, C.base(tau, v)


def rows_h(T, x, k, P, v, N, us, nv, n):
    R = np.zeros((len(x), nv)); R[:, 0] = 1.0
    R[:, 1:1+n] = -2*np.cos(np.outer(x, us))
    k0, k1 = C.kk(T, x + k*P)
    R[:, 3+n] = k0; R[:, 4+n] = k1
    return R, rhs_k(T, x, k, P, v, N)


# ---------------------------------------------------------------- separation

def local_minima(func, lo, hi, h, nref=6, batch=400000):
    """all local minima of func on [lo,hi], scanned at step h and refined to ~h*4^-nref."""
    n = int((hi-lo)/h) + 2
    xs = []; vs = []
    prev = None
    for i in range(0, n, batch):
        j = min(i+batch, n)
        t = lo + np.arange(max(i-1, 0), j+1)*h
        t = t[t <= hi + h]
        val = func(t)
        if len(val) < 3: continue
        m = (val[1:-1] < val[:-2]) & (val[1:-1] <= val[2:])
        idx = np.where(m)[0] + 1
        xs.append(t[idx]); vs.append(val[idx])
    if not xs: return np.array([]), np.array([])
    x = np.concatenate(xs); v = np.concatenate(vs)
    if len(x) == 0: return x, v
    x = np.unique(x)
    w = h
    for _ in range(nref):
        off = np.linspace(-w, w, 9)
        cand = np.clip(x[:, None] + off[None, :], lo, hi)
        val = func(cand.ravel()).reshape(cand.shape)
        j = val.argmin(axis=1)
        x = cand[np.arange(len(x)), j]
        w = w/3.0
    return x, func(x)


def separate(T, v, us, a, b0, b1, P, N, tau1, h_sep, nref):
    """returns dict which -> (argmins, values), global min value, which/where."""
    out = {}
    out['f'] = local_minima(lambda t: fvals(T, t, v, us, a, b0, b1), 0.0, tau1, h_sep, nref)
    for k in range(N+1):
        out[f'h{k}'] = local_minima(
            lambda t, k=k: hvals(T, t, k, P, v, N, us, a, b0, b1), tau1, tau1+P, h_sep, nref)
    gm = np.inf; gw = None; gx = None
    for w, (x, val) in out.items():
        if len(val) and float(val.min()) < gm:
            i = int(val.argmin()); gm = float(val[i]); gw = w; gx = float(x[i])
    return out, gm, gw, gx


# ---------------------------------------------------------------- driver

def run(T, M=24, U=20.0, tau1=30.0, N=2, h0f=0.03, h0h=0.02, h_sep=0.005, nref=6,
        iters=40, nadd=100000, tol=1e-6, purge=True, keepage=5, slacktol=0.02, patience=8, tag='x', lpm='highs',
        verbose=True):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d)
    us = np.arange(M, J+1)*d; P = 2*math.pi/d
    n = len(us); nv = 5 + n
    pts = {'f': np.arange(1e-7, tau1, h0f)}
    for k in range(N+1):
        pts[f'h{k}'] = tau1 + np.arange(0.0, P, h0h)
    base = {w: q.copy() for w, q in pts.items()}   # never purged: keeps the LP bounded
    age = {w: np.zeros(len(q)) for w, q in pts.items()}
    print(f"[{tag}] T={T:.6f} M={M} U={U} atoms={n} d={d:.6f} P={P:.4f} tau1={tau1} N={N} "
          f"v={ {q: round(z,6) for q,z in v.items()} }", flush=True)
    cv = np.zeros(nv); cv[0] = -1.0
    bnds = [(None, None)]*(3+n) + [(0, None)]*2
    R4 = np.zeros((4, nv))
    R4[0, 1+n] = 1; R4[0, 3+n] = -1
    R4[1, 1+n] = -1; R4[1, 3+n] = -1
    R4[2, 2+n] = 1; R4[2, 4+n] = -1
    R4[3, 2+n] = -1; R4[3, 4+n] = -1
    hist = []; out = None; bestmin = -np.inf; bestit = 0
    t00 = time.time()
    for it in range(iters):
        t0 = time.time()
        blocks = [R4]; rhss = [np.zeros(4)]; tally = []
        A_, b_ = rows_f(T, pts['f'], us, v, nv, n)
        blocks.append(A_); rhss.append(b_); tally.append(('f', len(pts['f'])))
        for k in range(N+1):
            A_, b_ = rows_h(T, pts[f'h{k}'], k, P, v, N, us, nv, n)
            blocks.append(A_); rhss.append(b_); tally.append((f'h{k}', len(pts[f'h{k}'])))
        Aub = np.vstack(blocks); bub = np.concatenate(rhss)
        S = 1e4
        Aub *= S; bub *= S          # in place: the LP matrix is the memory bottleneck
        res = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method=lpm)
        tlp = time.time()-t0
        if not res.success:
            print(f"[{tag}] LP fail: {res.message}", flush=True); return None
        x = res.x; c = float(x[0]); a = x[1:1+n]; b0 = float(x[1+n]); b1 = float(x[2+n])
        t1 = time.time()
        mins, gm, gw, gx = separate(T, v, us, a, b0, b1, P, N, tau1, h_sep, nref)
        tsep = time.time()-t1
        gap = c - gm
        print(f"[{tag}] it{it} rows={Aub.shape[0]} LPc={c:.10e} truemin={gm:.10e} "
              f"gap={gap:.3e} ({gw}@{gx:.4f}) |a|1={np.abs(a).sum():.2f} "
              f"b0={b0:.6f} b1={b1:.6f} lp={tlp:.0f}s sep={tsep:.0f}s", flush=True)
        hist.append(dict(it=it, rows=int(Aub.shape[0]), c=c, truemin=gm, gap=gap,
                         lp_s=tlp, sep_s=tsep))
        cur = dict(T=T, M=M, U=U, d=d, us=us, a=a, b0=b0, b1=b1, lp=c, tau1=tau1, N=N,
                   P=P, v=v, tag=tag, graded2=True, it=it, fine=gm, hmin=gm, hist=hist,
                   method='cutting-plane', rows=int(Aub.shape[0]),
                   wall=time.time()-t00)
        if gm > bestmin:
            bestmin = gm; bestit = it; out = cur
            pickle.dump(out, open(f'lp_{tag}.pkl', 'wb'))
        if it - bestit >= patience:
            print(f"[{tag}] STALLED: best truemin={bestmin:.10e} at it{bestit}, "
                  f"wall={time.time()-t00:.0f}s", flush=True)
            break
        if gap <= tol:
            print(f"[{tag}] CONVERGED at it{it}: LPc={c:.10e} truemin={gm:.10e} "
                  f"gap={gap:.2e} wall={time.time()-t00:.0f}s", flush=True)
            break
        # ---- constraint management: keep base rows, active rows, and young rows
        if purge:
            slack = bub - Aub @ x
            keep = (slack < slacktol*S) | (np.abs(np.asarray(res.ineqlin.marginals)) > 0)
            off = 4; newpts = {}; newage = {}
            for w, cnt in tally:
                kk_ = keep[off:off+cnt] | np.isin(pts[w], base[w]) | (age[w] > it - keepage)
                off += cnt
                newpts[w] = pts[w][kk_]; newage[w] = age[w][kk_]
            pts = newpts; age = newage
        # ---- add every violated local minimum
        nadded = 0
        for w, (xm, vm) in mins.items():
            if not len(xm): continue
            bad = np.where(vm < c - 1e-12)[0]
            if not len(bad): continue
            bad = bad[np.argsort(vm[bad])][:nadd]
            lo, hi = (0.0, tau1) if w == 'f' else (tau1, tau1+P)
            add = np.clip(xm[bad], lo, hi)
            allp = np.concatenate([pts[w], add])
            alla = np.concatenate([age[w], np.full(len(add), it+1.0)])
            o = np.argsort(allp); allp = allp[o]; alla = alla[o]
            u, iu = np.unique(allp, return_index=True)
            pts[w] = u; age[w] = alla[iu]
            nadded += len(add)
        print(f"[{tag}]      added {nadded} cuts -> "
              f"{sum(len(q) for q in pts.values())+4} rows", flush=True)
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=float, required=True)
    ap.add_argument('--M', type=int, default=24)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--h_sep', type=float, default=0.005)
    ap.add_argument('--nref', type=int, default=6)
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--nadd', type=int, default=100000)
    ap.add_argument('--keepage', type=int, default=5)
    ap.add_argument('--slacktol', type=float, default=0.02)
    ap.add_argument('--patience', type=int, default=8)
    ap.add_argument('--h0h', type=float, default=0.02)
    ap.add_argument('--tol', type=float, default=1e-6)
    ap.add_argument('--lpm', default='highs')
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    tag = A.out or f"C{A.T:g}M{A.M}"
    run(A.T, M=A.M, U=A.U, tau1=A.tau1, N=A.N, h_sep=A.h_sep, nref=A.nref,
        iters=A.iters, nadd=A.nadd, tol=A.tol, tag=tag, lpm=A.lpm,
        keepage=A.keepage, h0h=A.h0h, slacktol=A.slacktol,
        patience=A.patience)
