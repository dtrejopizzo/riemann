"""R154 round 5 -- parallel exhaustive second-order (Taylor) branch-and-bound.

  worker: python3 r5bb.py work <pkl> <which> <lo> <hi> <target> <wmin> <out.json>
  driver: python3 r5bb.py drive <pkl> --target t --nproc 19 --dir bbout_tag
Each segment is covered exhaustively by r5core.bb_taylor: no cap, no discard, budget raises.
"""
import argparse, json, math, os, pickle, subprocess, sys, time
import numpy as np
import r5core as C


def load(pkl):
    r = pickle.load(open(pkl, 'rb'))
    return (r, float(r['T']), r['v'], float(r['tau1']), float(r['P']), int(r['N']),
            np.asarray(r['a']), np.asarray(r['us']), float(r['b0']), float(r['b1']))


def main():
    if sys.argv[1] == 'work':
        _, _, pkl, which, lo, hi, target, wmin, out = sys.argv
        r, T, v, tau1, P, N, a, us, b0, b1 = load(pkl)
        res = C.bb_taylor(which, float(lo), float(hi), T, us, a, b0, b1, v, P, N,
                          float(target), wmin=float(wmin))
        res['L'] = C.lip(T, us, a, b0, b1, v)
        json.dump(res, open(out, 'w'))
        print(f"{which} [{lo},{hi}] lb={res['lb']:.8e} evals={res['evals']} "
              f"nfinal={res['final_intervals']}", flush=True)
        return
    ap = argparse.ArgumentParser()
    ap.add_argument('mode'); ap.add_argument('pkl')
    ap.add_argument('--target', type=float, required=True)
    ap.add_argument('--wmin', type=float, default=1e-9)
    ap.add_argument('--nproc', type=int, default=19)
    ap.add_argument('--nseg', type=int, default=5)
    ap.add_argument('--dir', default='bbout')
    A = ap.parse_args()
    r, T, v, tau1, P, N, a, us, b0, b1 = load(A.pkl)
    os.makedirs(A.dir, exist_ok=True)
    jobs = []
    for which, lo, hi in ([('f', 0.0, tau1)] +
                          [(f'h{k}', tau1, tau1+P) for k in range(N+1)]):
        edges = np.linspace(lo, hi, A.nseg+1)
        for i in range(A.nseg):
            jobs.append((which, edges[i], edges[i+1]))
    print(f"{len(jobs)} segments, target={A.target:.8e}", flush=True)
    procs = []; env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')
    t0 = time.time()
    for j, (which, lo, hi) in enumerate(jobs):
        out = f"{A.dir}/{which}_{j}.json"
        p = subprocess.Popen([sys.executable, __file__, 'work', A.pkl, which,
                              repr(lo), repr(hi), repr(A.target), repr(A.wmin), out], env=env)
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
    print(f"ALL {len(res)} segments complete. certified lower bound = {lb:.10e}")
    print(f"total evals = {sum(x['evals'] for x in res)}  unresolved = "
          f"{sum(x['final_intervals'] for x in res)}  wall = {time.time()-t0:.0f}s")
    json.dump(res, open(f"{A.dir}/_all.json", 'w'), indent=1)


if __name__ == '__main__':
    main()
