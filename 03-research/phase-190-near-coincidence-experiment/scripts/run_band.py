"""One-variable lag function: X(d) = 1/2 sum_x w_x [c0(x-d)+c0(x+d)], Arch cross term, band ratio |X - archcross|/(2 a0) for Lambda and controls,
d on a fine grid up to dmax (prime powers up to e^{dmax+2T0})."""
import numpy as np, json, sys
from profile import Profile
from am import *
T0 = float(sys.argv[1]); dmax = float(sys.argv[2]) if len(sys.argv) > 2 else 15.0
P = Profile(T0, 1.0, dmax=dmax+1)
nmax = int(np.exp(dmax + 2*T0)) + 2
print('nmax', nmax, flush=True)
d = np.arange(0.0, dmax, 2e-3)
def Xfun(pos, w):
    X = np.zeros_like(d)
    for xa, wa in zip(pos, w):
        lo = np.searchsorted(d, xa-2*T0); hi = np.searchsorted(d, xa+2*T0)
        X[lo:hi] += 0.5*wa*P.c0(xa - d[lo:hi])
        lo = np.searchsorted(d, -xa-2*T0); hi = np.searchsorted(d, -xa+2*T0)
        if hi > lo: X[lo:hi] += 0.5*wa*P.c0(xa + d[lo:hi])
    return X
arch = P.arch(d)
out = {'d': d, 'arch': arch, 'a0': P.a0}
posL, wL, nsL = lambda_comb(nmax); out['Lambda'] = Xfun(posL, wL)
for Pdel in (3, 5):
    pos, w, _ = lambda_comb(nmax, delete_below=Pdel); out[f'a_{Pdel}'] = Xfun(pos, w)
pos, w, _ = lambda_comb(nmax, amp2=0.05); out['amp2_0.05'] = Xfun(pos, w)
pos, w, _ = lambda_comb(nmax, perturb=(2, 1.01)); out['pert2_1.01'] = Xfun(pos, w)
for seed in range(5):
    pos, w, _ = poisson_comb(dmax+2*T0+0.1, 1.0, seed); out[f'poisson_{seed}'] = Xfun(pos, w)
for seed in range(2):
    pos, w, qs = beurling_comb(nmax, 0.02, seed); out[f'beurling_{seed}'] = Xfun(pos, w)
np.savez_compressed(f'../data/band_T0{T0}.npz', **out)
# summary: B(d)=arch - X ; band |B(d)| <= a0 for d>2T0 ; report sup over windows
summ = {}
for k, X in out.items():
    if k in ('d', 'arch', 'a0'): continue
    B = arch - X
    msk = d > 2*T0
    summ[k] = dict(sup_ratio=float(np.abs(B[msk]).max()/P.a0), argmax=float(d[msk][np.abs(B[msk]).argmax()]),
                   sup_by_range={str(int(r)): float(np.abs(B[(d > r-1) & (d <= r) & msk]).max()/P.a0) for r in range(1, int(dmax)+1)},
                   rms_by_range={str(int(r)): float(np.sqrt(np.mean(B[(d > r-1) & (d <= r) & msk]**2))/P.a0) for r in range(1, int(dmax)+1)},
                   n_violations=int((np.abs(B[msk]) > P.a0).sum()))
json.dump(summ, open(f'../data/band_T0{T0}.json', 'w'), indent=1)
for k, v in summ.items(): print(k, 'sup/a0=%.3f at d=%.2f, violations=%d' % (v['sup_ratio'], v['argmax'], v['n_violations']), ' sup by unit range:', [round(v['sup_by_range'][str(r)], 2) for r in range(1, int(dmax)+1)], flush=True)
