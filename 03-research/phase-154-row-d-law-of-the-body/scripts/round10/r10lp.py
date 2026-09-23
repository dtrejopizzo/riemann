"""R154 round 10 -- the HYBRID certificate LP.

    nu = nu_lat + c0 * nu_{1/2,0} + c1 * nu_{1/2,1}

nu_lat = sum_j a_j (delta_{u_j} + delta_{-u_j}) on the round-5 lattice u_j = j*d,
d = 2T/M, M = 24, u in [2T, 2T+20]  (414 atoms at T = 0.58); the two columns are the
canonical Levy columns of Identity M (s = 1/2, orders 0 and 1), see r9tail.py.

Tail certification = HYBRID LEMMA (R154_028 sec.3):

  rows on [0, tau1]                : f(tau) >= c, exact, cutting planes (r6lp machinery)
  block rows k = 0..N-1, x in [tau1, tau1+P):
        nuhat_lat(x) + c0*nuhat_{1/2,0}(x+kP) + c1*nuhat_{1/2,1}(x+kP)
        + m(x+kP) - sum_n v_n cos((x+kP) log n) - |b0| k0(x+kP) - |b1| k1(x+kP) >= c
      (everything exact: the row is evaluated AT tau = x+kP, and nuhat_lat is P-periodic)
  block row k = N (covers [tau1+N P, oo)):
        nuhat_lat(x) - |c0| cap_{1/2,0}(x+NP) - |c1| cap_{1/2,1}(x+NP)
        + m(x+NP) - sum_n v_n - |b0| k0(x+NP) - |b1| k1(x+NP) >= c
      cap_{s,p}(tau) = p!/(s^2+tau^2)^((p+1)/2) is DECREASING, so -|c| cap is increasing;
      m increasing, k0,k1 decreasing, -sum v_n cos >= -sum v_n.  Hence the row at x
      certifies every tau = x + kP with k >= N.

Control run: c0 = c1 = 0 fixed  ==>  exactly round 5's Lemma-F1 programme.
"""
import argparse, json, math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog

HERE = __file__.rsplit('/', 1)[0]
sys.path.insert(0, HERE + '/../round5')
sys.path.insert(0, HERE + '/../round9')
import r5core as C
import r9tail as Q
sys.path.insert(0, HERE + '/../round6')
from r6lp import local_minima

SCOLS = [(0.5, 0), (0.5, 1)]          # the canonical Levy columns (Identity M)
NC = len(SCOLS)


def colvals(tau, T):
    """(NC, len(tau)) exact column transforms"""
    return np.array([Q.nuhat_col(tau, T, s, k) for (s, k) in SCOLS])


def colcaps(tau, T):
    return np.array([Q.tailcap(tau, s, k) for (s, k) in SCOLS])


# ---------------------------------------------------------------- objects

def fvals(T, x, v, us, a, b0, b1, c):
    out = C.base(x, v) + C.nuhat(x, us, a) + b0*C.g0h(x, T) + b1*C.g1h(x, T)
    return out + c @ colvals(x, T)


def hvals(T, x, k, P, v, N, us, a, b0, b1, c):
    tk = x + k*P
    k0, k1 = C.kk(T, tk)
    out = C.nuhat(x, us, a) + C.m(tk) - abs(b0)*k0 - abs(b1)*k1
    if k < N:
        out = out - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
        out = out + c @ colvals(tk, T)
    else:
        out = out - sum(v.values())
        out = out - np.abs(c) @ colcaps(tk, T)
    return out


# ---------------------------------------------------------------- LP rows
# variable layout: 0 = c ; 1..n = a ; n+1 = b0 ; n+2 = b1 ; n+3 = t0 ; n+4 = t1 ;
#                  n+5..n+4+NC = column coefficients ; n+5+NC.. = their moduli

def rows_f(T, tau, us, v, nv, n):
    R = np.zeros((len(tau), nv)); R[:, 0] = 1.0
    R[:, 1:1+n] = -2*np.cos(np.outer(tau, us))
    R[:, 1+n] = -C.g0h(tau, T); R[:, 2+n] = -C.g1h(tau, T)
    R[:, 5+n:5+n+NC] = -colvals(tau, T).T
    return R, C.base(tau, v)


def rows_h(T, x, k, P, v, N, us, nv, n):
    R = np.zeros((len(x), nv)); R[:, 0] = 1.0
    R[:, 1:1+n] = -2*np.cos(np.outer(x, us))
    tk = x + k*P
    k0, k1 = C.kk(T, tk)
    R[:, 3+n] = k0; R[:, 4+n] = k1
    if k < N:
        R[:, 5+n:5+n+NC] = -colvals(tk, T).T
        rhs = C.m(tk) - sum(vn*np.cos(tk*math.log(n_)) for n_, vn in v.items())
    else:
        R[:, 5+n+NC:5+n+2*NC] = colcaps(tk, T).T
        rhs = C.m(tk) - sum(v.values())
    return R, rhs


# ---------------------------------------------------------------- separation

def separate(T, v, us, a, b0, b1, c, P, N, tau1, h_sep, nref):
    out = {}
    out['f'] = local_minima(lambda t: fvals(T, t, v, us, a, b0, b1, c), 0.0, tau1, h_sep, nref)
    for k in range(N+1):
        out[f'h{k}'] = local_minima(
            lambda t, k=k: hvals(T, t, k, P, v, N, us, a, b0, b1, c),
            tau1, tau1+P, h_sep, nref)
    gm = np.inf; gw = None; gx = None
    for w, (x, val) in out.items():
        if len(val) and float(val.min()) < gm:
            i = int(val.argmin()); gm = float(val[i]); gw = w; gx = float(x[i])
    return out, gm, gw, gx


# ---------------------------------------------------------------- driver

def run(T=0.58, M=24, U=20.0, tau1=30.0, N=2, h0f=0.03, h0h=0.02, h_sep=0.005, nref=6,
        iters=40, nadd=100000, tol=1e-7, keepage=5, slacktol=0.02, patience=8,
        cols=True, tag='H', colcap=50.0):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d)
    us = np.arange(M, J+1)*d; P = 2*math.pi/d
    n = len(us); nv = 5 + n + 2*NC
    pts = {'f': np.arange(1e-7, tau1, h0f)}
    for k in range(N+1):
        pts[f'h{k}'] = tau1 + np.arange(0.0, P, h0h)
    base = {w: q.copy() for w, q in pts.items()}
    age = {w: np.zeros(len(q)) for w, q in pts.items()}
    print(f"[{tag}] T={T} M={M} atoms={n} d={d:.6f} P={P:.5f} tau1={tau1} N={N} "
          f"cols={cols} NC={NC} nv={nv}", flush=True)
    cv = np.zeros(nv); cv[0] = -1.0
    cb = (-colcap, colcap) if cols else (0.0, 0.0)
    bnds = ([(None, None)]*(3+n) + [(0, None)]*2
            + [cb]*NC + [(0, colcap)]*NC)
    # |b_i| <= t_i  and  |c_k| <= d_k
    R4 = np.zeros((4 + 2*NC, nv))
    R4[0, 1+n] = 1; R4[0, 3+n] = -1
    R4[1, 1+n] = -1; R4[1, 3+n] = -1
    R4[2, 2+n] = 1; R4[2, 4+n] = -1
    R4[3, 2+n] = -1; R4[3, 4+n] = -1
    for j in range(NC):
        R4[4+2*j, 5+n+j] = 1; R4[4+2*j, 5+n+NC+j] = -1
        R4[5+2*j, 5+n+j] = -1; R4[5+2*j, 5+n+NC+j] = -1
    nfix = R4.shape[0]
    hist = []; out = None; bestmin = -np.inf; bestit = 0
    t00 = time.time()
    for it in range(iters):
        t0 = time.time()
        blocks = [R4]; rhss = [np.zeros(nfix)]; tally = []
        A_, b_ = rows_f(T, pts['f'], us, v, nv, n)
        blocks.append(A_); rhss.append(b_); tally.append(('f', len(pts['f'])))
        for k in range(N+1):
            A_, b_ = rows_h(T, pts[f'h{k}'], k, P, v, N, us, nv, n)
            blocks.append(A_); rhss.append(b_); tally.append((f'h{k}', len(pts[f'h{k}'])))
        Aub = np.vstack(blocks); bub = np.concatenate(rhss)
        S = 1e4
        Aub *= S; bub *= S
        res = linprog(cv, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
        tlp = time.time()-t0
        if not res.success:
            print(f"[{tag}] LP fail: {res.message}", flush=True); return None
        x = res.x; cval = float(x[0]); a = x[1:1+n]
        b0 = float(x[1+n]); b1 = float(x[2+n])
        cc = np.array(x[5+n:5+n+NC])
        t1 = time.time()
        mins, gm, gw, gx = separate(T, v, us, a, b0, b1, cc, P, N, tau1, h_sep, nref)
        tsep = time.time()-t1
        gap = cval - gm
        print(f"[{tag}] it{it} rows={Aub.shape[0]} LPc={cval:.10e} truemin={gm:.10e} "
              f"gap={gap:.3e} ({gw}@{gx:.4f}) |a|1={np.abs(a).sum():.4f} "
              f"b0={b0:.6f} b1={b1:.6f} c={np.array2string(cc, precision=6)} "
              f"lp={tlp:.0f}s sep={tsep:.0f}s", flush=True)
        hist.append(dict(it=it, rows=int(Aub.shape[0]), c=cval, truemin=gm, gap=gap,
                         l1a=float(np.abs(a).sum()), b0=b0, b1=b1,
                         cols=[float(z) for z in cc], lp_s=tlp, sep_s=tsep))
        cur = dict(T=T, M=M, U=U, d=d, us=us, a=a, b0=b0, b1=b1, cols=cc,
                   scols=SCOLS, lp=cval, tau1=tau1, N=N, P=P, v=v, tag=tag,
                   hybrid=True, it=it, fine=gm, hist=hist,
                   rows=int(Aub.shape[0]), wall=time.time()-t00)
        if gm > bestmin:
            bestmin = gm; bestit = it; out = cur
            pickle.dump(out, open(f'{HERE}/lp_{tag}.pkl', 'wb'))
        if it - bestit >= patience:
            print(f"[{tag}] STALLED best={bestmin:.10e} it{bestit}", flush=True); break
        if gap <= tol:
            print(f"[{tag}] CONVERGED it{it} gap={gap:.2e} "
                  f"wall={time.time()-t00:.0f}s", flush=True); break
        slack = bub - Aub @ x
        keep = (slack < slacktol*S) | (np.abs(np.asarray(res.ineqlin.marginals)) > 0)
        off = nfix; newpts = {}; newage = {}
        for w, cnt in tally:
            kk_ = keep[off:off+cnt] | np.isin(pts[w], base[w]) | (age[w] > it - keepage)
            off += cnt
            newpts[w] = pts[w][kk_]; newage[w] = age[w][kk_]
        pts = newpts; age = newage
        nadded = 0
        for w, (xm, vm) in mins.items():
            if not len(xm): continue
            bad = np.where(vm < cval - 1e-12)[0]
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
        print(f"[{tag}]      +{nadded} cuts -> {sum(len(q) for q in pts.values())+nfix} rows",
              flush=True)
    return out


def report(out, h=2e-4):
    """direct fine-grid minimum of the TRUE f on [0, tau1 + (N+1)P] and the F1 slack."""
    T = out['T']; v = out['v']; us = out['us']; a = out['a']
    b0 = out['b0']; b1 = out['b1']; cc = out['cols']; P = out['P']; N = out['N']
    hi = out['tau1'] + (N+1)*P
    mu = np.inf; arg = 0.0
    nt = int(hi/h)+1
    for i in range(0, nt, 400000):
        t = (np.arange(i, min(i+400000, nt)))*h
        val = fvals(T, t, v, us, a, b0, b1, cc)
        j = int(val.argmin())
        if float(val[j]) < mu: mu = float(val[j]); arg = float(t[j])
    # F1 slack = margin of the worst-case block row k = N over the LP value
    x = out['tau1'] + np.linspace(0, P, 20001)
    hn = hvals(T, x, N, P, v, N, us, a, b0, b1, cc)
    return dict(fine_true_min=mu, fine_arg=arg, hN_min=float(hn.min()),
                F1_slack=float(hn.min()) - out['lp'],
                l1a=float(np.abs(a).sum()), sum2a=float(2*np.abs(a).sum()))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--nocols', action='store_true')
    ap.add_argument('--tag', default='H')
    ap.add_argument('--iters', type=int, default=40)
    ap.add_argument('--both', action='store_true')
    A = ap.parse_args()
    res = {}
    runs = [('H', True), ('CTL', False)] if A.both else [(A.tag, not A.nocols)]
    for tag, cols in runs:
        o = run(cols=cols, tag=tag, iters=A.iters)
        if o is None: continue
        r = report(o)
        r.update(tag=tag, cols=cols, lp=o['lp'], sep_min=o['fine'], b0=o['b0'],
                 b1=o['b1'], c0=float(o['cols'][0]), c1=float(o['cols'][1]),
                 wall=o['wall'], its=o['it']+1, rows=o['rows'])
        print('REPORT', json.dumps(r), flush=True)
        res[tag] = r
        json.dump(res, open(f'{HERE}/r10_results.json', 'w'), indent=1)
