"""R154 round 8 -- SINGLE falsifier of the clustering remedy (R154_020 sec.5, R154_021).

Two LP solves in ONE process, cutting planes only, no B&B:
  CLUSTERED : 175 atoms on [2T, 2T+~2.0], spacing h' = 2T/M, M = 102
  CONTROL   : 175 atoms on [2T, 2T+~20.2], spacing h  = 2T/10 (u_max ~ 21.3, R154_020 sec.5(iii))
Reported per run: LP value, fine-grid (1e-3) true minimum over [0,tau1] and the three
tail blocks [tau1,tau1+P), beta0, beta1, ||a||_1, Lemma-F1 slack |b0|k0+|b1|k1 at tau1, wall.
"""
import sys, os, math, time, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'round6'))
sys.path.insert(0, os.path.join(HERE, '..', 'round5'))
os.chdir(os.path.join(HERE))
import r5core as C
import r6lp as L

T = 0.58
TAU1 = 59.544
N = 2

def finemin(T, us, a, b0, b1, v, P, tau1, N, h=1e-3):
    """true minimum on a 1e-3 grid of f on [0,tau1] and h_k on [tau1,tau1+P), k=0..N."""
    out = {}
    mu, arg = C.fine_min(lambda t: L.fvals(T, t, v, us, a, b0, b1), 1e-7, tau1, h)
    out['f'] = (mu, arg)
    for k in range(N+1):
        mu, arg = C.fine_min(
            lambda t, k=k: L.hvals(T, t, k, P, v, N, us, a, b0, b1), tau1, tau1+P, h)
        out[f'h{k}'] = (mu, arg)
    gm = min(x[0] for x in out.values())
    gw = [w for w, x in out.items() if x[0] == gm][0]
    return gm, gw, out[gw][1], out

def one(tag, M, natoms, h0f, h0h, h_sep, iters):
    d = 2*T/M
    J = M + natoms - 1
    U = J*d - 2*T + 1e-9
    t0 = time.time()
    res = L.run(T, M=M, U=U, tau1=TAU1, N=N, h0f=h0f, h0h=h0h, h_sep=h_sep, nref=5,
                iters=iters, tol=1e-6, patience=iters, tag=tag)
    wall = time.time()-t0
    if res is None:
        print(f"[{tag}] FAILED"); return None
    us, a, b0, b1, P = res['us'], res['a'], res['b0'], res['b1'], res['P']
    v = res['v']
    print(f"[{tag}] atoms={len(us)} umin={us[0]:.6f} umax={us[-1]:.6f} d={d:.8f} P={P:.3f}", flush=True)
    t1 = time.time()
    gm, gw, gx, detail = finemin(T, us, a, b0, b1, v, P, TAU1, N)
    k0, k1 = C.kk(T, TAU1)
    slack = abs(b0)*k0 + abs(b1)*k1
    rec = dict(tag=tag, M=M, d=d, natoms=len(us), umax=float(us[-1]), P=P,
               lp=res['lp'], truemin_sep=res['fine'], truemin_fine=gm, argmin=gx, where=gw,
               b0=b0, b1=b1, a1=float(np.abs(a).sum()), f1_slack=slack,
               wall_lp=wall, wall_fine=time.time()-t1, iters=res['it']+1,
               detail={w: [float(x[0]), float(x[1])] for w, x in detail.items()})
    print(f"[{tag}] RESULT LP={res['lp']:.6e} truemin(1e-3)={gm:.6e} @{gx:.4f}({gw}) "
          f"b0={b0:.6f} b1={b1:.6f} |a|1={rec['a1']:.4f} F1slack={slack:.6e} "
          f"lp_wall={wall:.0f}s fine_wall={rec['wall_fine']:.0f}s", flush=True)
    return rec

if __name__ == '__main__':
    R = []
    R.append(one('R8CLU', 102, 175, 0.06, 552.5/700, 0.06, 8))
    R.append(one('R8CTL',  10, 175, 0.06,  54.2/700, 0.010, 8))
    json.dump(R, open('r8_results.json', 'w'), indent=1)
    print(json.dumps([{k: r[k] for k in ('tag','umax','P','lp','truemin_fine','b0','b1','a1','f1_slack','wall_lp','iters')} for r in R if r], indent=1))
