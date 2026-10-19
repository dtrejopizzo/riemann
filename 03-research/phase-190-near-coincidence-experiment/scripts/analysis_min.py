"""Structure of the minimizer of A_M(Lambda): comparison with m^{-1/2}w(m/M), Dirichlet polynomial at the zero ordinates (observation only),
Gram-relative bottom on the well-conditioned Gram subspace, precise amplification threshold c*(M), and the same for controls."""
import numpy as np, json, sys, mpmath
from profile import Profile
from am import *
T0 = float(sys.argv[1]); Ms = [int(x) for x in sys.argv[2].split(',')]
P = Profile(T0, 1.0)
zeros = np.array([float(mpmath.im(mpmath.zetazero(k))) for k in range(1, 41)])
out = {}
def pencil_bottom(A, C, eps=1e-9):
    lc, Vc = np.linalg.eigh(C); keep = lc > eps*lc[-1]
    W = Vc[:, keep]/np.sqrt(lc[keep])          # C-orthonormal basis of the well-conditioned subspace
    B = W.T @ A @ W; lb, Vb = np.linalg.eigh(B)
    return float(lb[0]), W @ Vb[:, 0], int(keep.sum())
for M in Ms:
    x = np.log(np.arange(1, M+1)); nmax = int(M*np.exp(2*T0)) + 2
    pos, w, ns = lambda_comb(nmax)
    A = AM(P, x, pos, w)
    lam, V = np.linalg.eigh(A.A); v = V[:, 0]
    r = dict(lam_min=float(lam[0]))
    # Dirichlet polynomial of the minimizer at the zero ordinates vs on a generic grid
    tau = np.linspace(0.5, 60, 1200)
    Pv = lambda t: np.abs(np.exp(1j*np.outer(t, x)) @ v)
    r['P_at_zeros'] = Pv(zeros[zeros < 60]).tolist(); r['P_generic_median'] = float(np.median(Pv(tau))); r['P_generic_mean'] = float(np.mean(Pv(tau)))
    r['P_at_zeros_over_median'] = float(np.median(Pv(zeros[zeros < 60]))/np.median(Pv(tau)))
    # compare with m^{-1/2} w(m/M)
    m = np.arange(1, M+1); best = None
    for name, wfun in (('one', lambda t: np.ones_like(t)), ('1-t', lambda t: 1-t), ('(1-t)^2', lambda t: (1-t)**2), ('cos2', lambda t: np.cos(np.pi*t/2)**2), ('(1-t)^3', lambda t: (1-t)**3), ('(1-t)^4', lambda t: (1-t)**4)):
        u = m**-0.5*wfun(m/M); u /= np.linalg.norm(u)
        q = float(u@A.A@u); ov = float(abs(u@v))
        r['smooth_'+name] = dict(rayleigh=q, overlap=ov, Div=float(u@A.Div@u), Near=float(u@A.Near@u), Arch=float(u@A.Arch@u), Gram=float(u@A.Gram@u))
    # signed-ness of minimizer: fraction of v with the sign of m^{-1/2} shape; moebius correlation
    r['v_frac_pos'] = float((v*np.sign(v[0]) > 0).mean())
    mu = np.ones(M); 
    # moebius via sieve
    mob = np.ones(M+1, int); isp = np.ones(M+1, bool)
    for p in range(2, M+1):
        if isp[p]:
            isp[p*p::p] = False; mob[p::p] *= -1; mob[p*p::p*p] = 0
    u = mob[1:]*m**-0.5; u /= np.linalg.norm(u); r['moebius_overlap'] = float(abs(u@v)); r['moebius_rayleigh'] = float(u@A.A@u)
    # Gram-relative bottom on well-conditioned subspace
    for eps in (1e-6, 1e-9, 1e-12):
        lb, vb, dim = pencil_bottom(A.A, A.Gram, eps)
        r[f'pencil_eps{eps:g}'] = dict(bottom=lb, dim=dim, Arch=float(vb@A.Arch@vb)/float(vb@A.Gram@vb), Div=float(vb@A.Div@vb)/float(vb@A.Gram@vb), Near=float(vb@A.Near@vb)/float(vb@A.Gram@vb))
    # precise amplification threshold at n=2 (log bisection) and derivative
    def lmin(c):
        pos2, w2, _ = lambda_comb(nmax, amp2=c); return np.linalg.eigvalsh(AM(P, x, pos2, w2).A)[0]
    lo, hi = 1e-13, 1.0
    for _ in range(40):
        mid = np.sqrt(lo*hi)
        if lmin(mid) < 0: hi = mid
        else: lo = mid
    r['cstar_amp2'] = float(hi)
    # first-order: dA/dc = -(E) with E the n=2 kernel; slope at the minimizer
    pos2, w2, _ = lambda_comb(nmax, amp2=1.0); E = AM(P, x, pos2, w2).A - A.A
    r['dlam_dc_first_order'] = float(v@E@v); r['cstar_first_order'] = float(-lam[0]/(v@E@v)) if v@E@v < 0 else None
    # lower-tail: how many eigenvalues below 1e-6, 1e-4
    r['n_below_1e-6'] = int((lam < 1e-6).sum()); r['n_below_1e-4'] = int((lam < 1e-4).sum()); r['n_below_1e-2'] = int((lam < 1e-2).sum())
    out[M] = r
    print(M, json.dumps({k: (v if not isinstance(v, list) else [round(t, 4) for t in v]) for k, v in r.items()}, default=float)[:1500], flush=True)
    json.dump(out, open(f'../data/analysis_min_T0{T0}.json', 'w'), indent=1, default=float)
