"""Track fixed arithmetic cells across T: polished min of mu_1/8 within tau0 +- 0.1 for T on a grid."""
import sys; sys.path.insert(0, '..')
import align_band as A, numpy as np, math
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
def w(a):
    T, t0 = a; ts = np.arange(t0-0.1, t0+0.1001, 0.02); mv = [A.margin(T, t, 0.125)[0] for t in ts]; j = int(np.argmin(mv))
    r = minimize_scalar(lambda t: A.margin(T, t, 0.125)[0], bounds=(ts[max(j-1,0)], ts[min(j+1,len(ts)-1)]), method='bounded', options={'xatol': 2e-5})
    return T, t0, r.x, r.x/(2*math.pi*math.exp(2*T)), r.fun
jobs = [(T, 7713.88) for T in (3.0, 3.25, 3.375, 3.5)] + [(T, 30774.98) for T in (3.75, 3.875, 4.0, 4.1, 4.2)] + [(T, 14303.97) for T in (3.25, 3.5, 3.6, 3.75)]
with Pool(6) as p:
    for r in p.imap_unordered(w, jobs): print(*r, flush=True)
