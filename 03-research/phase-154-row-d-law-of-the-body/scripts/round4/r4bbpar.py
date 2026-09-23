"""R154 round 4: parallel exhaustive Lipschitz branch-and-bound worker.

A domain [lo,hi] is covered by ONE worker with the same stack algorithm as r4core.bb_min
(no discards; budget -> exception).  The driver splits [0,tau1] and each [tau1, tau1+P]
into equal pieces and runs them as independent processes; the certified bound is the min
over pieces, because a cover of each piece is a cover of the union.

  worker:  python3 r4bbpar.py work <pkl> <which> <lo> <hi> <target> <wmin> <out.json>
  driver:  python3 r4bbpar.py drive <pkl> --target t --nproc 16 --wmin 5e-8
"""
import argparse, json, math, os, subprocess, sys, time
import numpy as np
import r4core as C
from r4g2 import kk


def make_fun(pkl, which):
    import pickle
    r = pickle.load(open(pkl, 'rb'))
    T, v = r['T'], r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    b0, b1 = float(r['b0']), float(r['b1'])
    L = C.lip(T, us, a, b0, b1, v)
    if which == 'f':
        fn = lambda t: C.fval(t, T, us, a, b0, b1, v)
    else:
        k = int(which[1:])
        def fn(x, k=k):
            x = np.asarray(x, dtype=float)
            tk = x + k*P
            k0, k1 = kk(T, tk)
            if k < N:
                rhs = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
            else:
                rhs = C.m(tk) - sum(v.values())
            return C.nuhat(x, us, a) + rhs - abs(b0)*k0 - abs(b1)*k1
    return r, fn, L, tau1, P, N


def bb_seg(fn, lo, hi, L, target, w0=0.02, wmin=5e-8, max_evals=4_000_000_000):
    n0 = int(math.ceil((hi-lo)/w0)); w = (hi-lo)/n0
    stack = [(lo + np.arange(n0)*w, w)]
    lb = np.inf; best = np.inf; nfinal = 0; meas = 0.0; nev = 0
    while stack:
        cur, w = stack.pop()
        if len(cur) > 400000:
            stack.append((cur[400000:], w)); cur = cur[:400000]
        mid = cur + w/2
        vals = fn(mid); nev += len(mid)
        if nev > max_evals:
            raise RuntimeError(f"budget exceeded ({nev}); NOT certified")
        best = min(best, float(vals.min()))
        keep = vals - L*w/2 < target
        nk = int(keep.sum())
        if nk == 0:
            continue
        if w/2 < wmin:
            lb = min(lb, float(vals[keep].min()) - L*w/2)
            nfinal += nk; meas += nk*w
            continue
        c2 = cur[keep]
        stack.append((np.repeat(c2, 2) + np.tile(np.array([0.0, w/2]), nk), w/2))
    return dict(lo=lo, hi=hi, lb=min(target, lb), best=best, evals=nev,
                final_intervals=nfinal, surviving_measure=meas, L=L, target=target,
                wmin=wmin, complete=True)


def main():
    if sys.argv[1] == 'work':
        _, _, pkl, which, lo, hi, target, wmin, out = sys.argv
        r, fn, L, tau1, P, N = make_fun(pkl, which)
        res = bb_seg(fn, float(lo), float(hi), L, float(target), wmin=float(wmin))
        res['which'] = which
        json.dump(res, open(out, 'w'))
        print(f"{which} [{lo},{hi}] lb={res['lb']:.8e} evals={res['evals']} "
              f"nfinal={res['final_intervals']}", flush=True)
        return
    ap = argparse.ArgumentParser()
    ap.add_argument('mode'); ap.add_argument('pkl')
    ap.add_argument('--target', type=float, required=True)
    ap.add_argument('--wmin', type=float, default=5e-8)
    ap.add_argument('--nproc', type=int, default=16)
    ap.add_argument('--dir', default='bbout')
    A = ap.parse_args()
    import pickle
    r = pickle.load(open(A.pkl, 'rb'))
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    os.makedirs(A.dir, exist_ok=True)
    jobs = []
    for which, lo, hi, k in ([('f', 0.0, tau1, 3)] +
                             [(f'h{k}', tau1, tau1+P, 6) for k in range(N+1)]):
        edges = np.linspace(lo, hi, k+1)
        for i in range(k):
            jobs.append((which, edges[i], edges[i+1]))
    print(f"{len(jobs)} segments", flush=True)
    procs = []; env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
    for j, (which, lo, hi) in enumerate(jobs):
        out = f"{A.dir}/{which}_{j}.json"
        p = subprocess.Popen([sys.executable, __file__, 'work', A.pkl, which,
                              repr(lo), repr(hi), repr(A.target), repr(A.wmin), out],
                             env=env)
        procs.append((p, out))
        while sum(1 for q, _ in procs if q.poll() is None) >= A.nproc:
            time.sleep(2)
    for p, _ in procs: p.wait()
    res = []
    for p, out in procs:
        if p.returncode != 0 or not os.path.exists(out):
            print(f"FAILED segment {out} rc={p.returncode}"); sys.exit(1)
        res.append(json.load(open(out)))
    lb = min(x['lb'] for x in res)
    print(f"ALL {len(res)} segments complete.  certified lower bound = {lb:.10e}")
    print(f"total evals = {sum(x['evals'] for x in res)}  "
          f"total final intervals = {sum(x['final_intervals'] for x in res)}")
    json.dump(res, open(f"{A.dir}/_all.json", 'w'), indent=1)


if __name__ == '__main__':
    main()
