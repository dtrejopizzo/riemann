"""Off-machine driver for the HYBRID certificate LP at large N (R154_028 §4.5, R154_029 L-b).

Wraps round10/r10lp.run with:
  * --N (default 6): worst-case block pushed to tau1 + N P  (~810 at T = 0.58, M = 24);
  * interior-point HiGHS ('highs-ipm') instead of dual simplex, rows UNscaled  -> the two
    solver settings R154_029 §3 asked for;
  * solver status / residual printout for every solve;
  * feasibility check of the round-5 control point (lp_Q058.pkl) against each row set: the LP
    value of a maximisation can never lie below a feasible point; if it does the run is VOID.
Usage: python3 hybrid_N.py --N 6 --iters 60 --tag H6 [--nocols] [--M 24] [--T 0.58]
"""
import argparse, json, math, os, pickle, sys, time
import numpy as np
import scipy.optimize as so

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round10'))
import r10lp as R                                   # noqa: E402

_orig_linprog = so.linprog

def _linprog_ipm(*a, **k):
    k['method'] = 'highs-ipm'
    k.setdefault('options', {})
    k['options'].update(dict(presolve=True, disp=False, primal_feasibility_tolerance=1e-10,
                             dual_feasibility_tolerance=1e-10, ipm_optimality_tolerance=1e-12))
    t0 = time.time()
    res = _orig_linprog(*a, **k)
    print(f"    [solver] status={res.status} success={res.success} fun={res.fun!r} "
          f"nit={getattr(res,'nit',None)} wall={time.time()-t0:.1f}s msg={res.message!r}", flush=True)
    if not res.success:
        print("    [solver] WARNING: unsuccessful solve -- iterate is DIAGNOSTIC only", flush=True)
    return res

so.linprog = _linprog_ipm
R.linprog = _linprog_ipm                            # r10lp imported the name directly


def control_check(T, M, U, tau1, N):
    """Evaluate the round-5 control certificate through the round-10 rows (c0 = c1 = 0)."""
    pkl = os.path.join(HERE, '..', 'round5', 'lp_Q058.pkl')
    if not os.path.exists(pkl):
        print("[control] round5/lp_Q058.pkl not found; skipping control check"); return None
    o = pickle.load(open(pkl, 'rb'))
    a, b0, b1 = np.asarray(o['a']), float(o['b0']), float(o['b1'])
    v = R.C.vdict(T); d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    if len(us) != len(a):
        print(f"[control] atom count mismatch {len(us)} vs {len(a)}; skipping"); return None
    c0 = np.zeros(R.NC)
    x = np.arange(1e-7, tau1, 2e-4)
    fmin = float(R.fvals(T, x, v, us, a, b0, b1, c0).min())
    xs = tau1 + np.arange(0.0, P, 2e-4)
    hmin = min(float(R.hvals(T, xs, k, P, v, N, us, a, b0, b1, c0).min()) for k in range(N+1))
    val = min(fmin, hmin)
    print(f"[control] round-5 certificate through N={N} rows: min f = {fmin:.9e}, min h_k = {hmin:.9e}, "
          f"value = {val:.9e}  (any LP value below this is VOID)", flush=True)
    return val


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=float, default=0.58)
    ap.add_argument('--M', type=int, default=24)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=6)
    ap.add_argument('--iters', type=int, default=60)
    ap.add_argument('--nocols', action='store_true')
    ap.add_argument('--tag', default='H6')
    A = ap.parse_args()
    ctl = control_check(A.T, A.M, A.U, A.tau1, A.N)
    o = R.run(T=A.T, M=A.M, U=A.U, tau1=A.tau1, N=A.N, iters=A.iters, cols=not A.nocols, tag=A.tag)
    if o is None:
        print("run returned None"); sys.exit(1)
    r = R.report(o)
    r.update(tag=A.tag, N=A.N, cols=not A.nocols, lp=o['lp'], sep_min=o['fine'], b0=o['b0'], b1=o['b1'],
             c0=float(o['cols'][0]), c1=float(o['cols'][1]), wall=o['wall'], its=o['it']+1,
             rows=o['rows'], control_value=ctl,
             VOID=(ctl is not None and o['lp'] < ctl - 1e-9))
    print('REPORT', json.dumps(r), flush=True)
    json.dump(r, open(os.path.join(HERE, f'result_{A.tag}.json'), 'w'), indent=1)
