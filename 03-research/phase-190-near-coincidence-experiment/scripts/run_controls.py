import numpy as np, json, sys, time
from profile import Profile
from am import *
T0 = float(sys.argv[1]); b = 1.0
Ms = [int(x) for x in sys.argv[2].split(',')] if len(sys.argv) > 2 else [50, 100, 200, 400, 700, 1000, 1500]
tag = f"T0{T0}"
P = Profile(T0, b)
GAMMA1 = 14.134725141734693
def quartet_kernel(delta, gamma):
    zs = [delta+1j*gamma, delta-1j*gamma, -delta+1j*gamma, -delta-1j*gamma]
    coef = [(z, P.Fhat(-1j*z)**2) for z in zs]
    def Q(d):
        out = np.zeros(np.shape(d), complex)
        for z, c in coef: out += c*np.exp(z*d)
        return out.real
    return Q

def vstats(v, A):
    p = v**2; o = np.argsort(-p)
    return dict(part_ratio=float(1/np.sum(p**2)), top_idx=[int(i+1) for i in o[:6]], top_mass=[float(p[i]) for i in o[:6]],
                Arch=float(v@A.Arch@v), Div=float(v@A.Div@v), Near=float(v@A.Near@v),
                Extra=float(v@A.Extra@v) if hasattr(A, 'Extra') else 0.0, Gram=float(v@A.Gram@v))

def run(A):
    lam, V = np.linalg.eigh(A.A); v = V[:, 0]
    normA = np.abs(lam).max(); floor = 2.2e-16*normA*A.M
    return dict(lam_min=float(lam[0]), floor=float(floor), n_neg=int((lam < -10*floor).sum()), negative=bool(lam[0] < -10*floor),
                lam_low=[float(l) for l in lam[:4]], vec=vstats(v, A))

res = {}
for M in Ms:
    t0 = time.time(); R = {}
    x = np.log(np.arange(1, M+1)); nmax = int(M*np.exp(2*T0)) + 2
    posL, wL, nsL = lambda_comb(nmax)
    R['Lambda'] = run(AM(P, x, posL, wL))
    for Pdel in (3, 5):
        pos, w, ns = lambda_comb(nmax, delete_below=Pdel); R[f'a_{Pdel}'] = run(AM(P, x, pos, w))
    for n0, fac in ((2, 1+1e-5), (2, 1-1e-5), (2, 1+1e-2), (2, 1-1e-2), (3, 1+1e-2), (3, 1-1e-2), (7, 1+1e-2), (7, 1-1e-2)):
        pos, w, ns = lambda_comb(nmax, perturb=(n0, fac)); R[f'pert_{n0}_{fac:+.5f}'] = run(AM(P, x, pos, w))
    # amplification threshold c* by bisection on sign of lam_min
    def lam_of(c):
        pos, w, ns = lambda_comb(nmax, amp2=c); return run(AM(P, x, pos, w))
    lo, hi = 0.0, 1.0
    r = lam_of(hi)
    while not r['negative'] and hi < 64: hi *= 2; r = lam_of(hi)
    if r['negative']:
        for _ in range(18):
            mid = 0.5*(lo+hi); r = lam_of(mid)
            if r['negative']: hi = mid
            else: lo = mid
        R['amp2_cstar'] = hi; R['amp2_at_cstar'] = lam_of(hi)
        R['amp2_at_2cstar'] = lam_of(2*hi)
    else:
        R['amp2_cstar'] = None
    for seed in range(5):
        pos, w, _ = poisson_comb(np.log(M)+2*T0+0.1, 1.0, seed); R[f'poisson_{seed}'] = run(AM(P, x, pos, w)); R[f'poisson_{seed}']['natoms'] = int(len(pos))
    for seed in range(2):
        pos, w, qs = beurling_comb(nmax, 0.02, seed)
        R[f'beurling_int_{seed}'] = run(AM(P, x, pos, w))
        xb = np.log(beurling_integers(qs, M)); R[f'beurling_own_{seed}'] = run(AM(P, xb, pos, w)); R[f'beurling_own_{seed}']['Mown'] = int(len(xb))
    for delta in (0.1, 0.3):
        R[f'M1_delta{delta}'] = run(AM(P, x, posL, wL, extra_kernel=quartet_kernel(delta, GAMMA1)))
    R['secs'] = time.time()-t0
    res[M] = R
    print(M, 'secs %.0f'%R['secs'], {k: ('%.2e' % v['lam_min'], v['negative']) for k, v in R.items() if isinstance(v, dict) and 'lam_min' in v}, 'c*=', R['amp2_cstar'], flush=True)
    json.dump(res, open(f'../data/controls_{tag}.json', 'w'), indent=1, default=float)
