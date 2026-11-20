"""Track a band-margin cell continuously in T (phase 211, ROUND_022_B).  NUMERICAL tool.
For each (T, tau0): mu_1/8 scanned on tau0 +- 0.2 (step 0.02), bounded Brent (xatol 2e-5) around the best scan point.
usage: track22.py out.npy nproc tau0:Tlo:Thi[:extra_r1,extra_r2,...] ...   (T grid step 0.05; extra points at T with r = tau0/2pi e^{2T} = given)"""
import sys, math, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')
import align_band as A
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
def w(a):
    T, t0 = a; A._V.clear(); ts = np.arange(t0 - 0.2, t0 + 0.2001, 0.02); mv = [A.margin(T, t, 0.125)[0] for t in ts]; j = int(np.argmin(mv))
    r = minimize_scalar(lambda t: A.margin(T, t, 0.125)[0], bounds=(ts[max(j-1,0)], ts[min(j+1,len(ts)-1)]), method='bounded', options={'xatol': 2e-5})
    m8, res, K = A.margin(T, r.x, 0.125)
    return T, t0, r.x, r.x / (2 * math.pi * math.exp(2 * T)), m8, res, K
if __name__ == '__main__':
    fn, npr = sys.argv[1], int(sys.argv[2]); jobs = []
    for spec in sys.argv[3:]:
        p = spec.split(':'); t0, lo, hi = map(float, p[:3])
        Ts = list(np.round(np.arange(lo, hi + 1e-9, 0.05), 4))
        if len(p) > 3: Ts += [0.5 * math.log(t0 / (2 * math.pi * float(x))) for x in p[3].split(',')]
        jobs += [(T, t0) for T in Ts]
    done = list(np.load(fn, allow_pickle=True)) if os.path.exists(fn) else []
    key = {(round(d[0], 6), round(d[1], 4)) for d in done}; jobs = [j for j in jobs if (round(j[0], 6), round(j[1], 4)) not in key]
    print(len(jobs), 'jobs', flush=True)
    with Pool(npr) as pl:
        for r in pl.imap_unordered(w, jobs):
            done.append(r); np.save(fn, np.array(done, dtype=object), allow_pickle=True); print(*r, flush=True)
