"""W1 task 1: fit lam_min_norm(refine) to test convergence-to-0 vs a
positive or negative limit L, plus Aitken/Richardson extrapolation.

Reads W1_convergence.json (produced by W1_convergence_run.py).

Command:
    python3 W1_convergence_fit.py

Models fit by nonlinear least squares (scipy.optimize.curve_fit) on the
raw (refine, lam) pairs, refine in {4,...,128}:
    (a) lam = C * r^-p            (L fixed = 0)
    (b)/(c) lam = L + C * r^-p    (L free)
Since the data are deterministic Galerkin values (no random measurement
noise), curve_fit's covariance is only a local-curvature diagnostic, not a
true confidence interval. To get an HONEST uncertainty on L we instead
report the spread of L across refits on nested trailing subsets of the
refine grid (using only the k largest refine values, k=4..10) -- this
measures how much the extrapolated limit moves as more of the asymptotic
regime is included, which is the real source of doubt here.

Independent check: Aitken/Shanks extrapolation
    L_hat(n) = x_n - (x_{n+1}-x_n)^2 / (x_{n+2} - 2 x_{n+1} + x_n)
applied to consecutive triples along the two exact geometric (ratio-2)
sub-chains present in the refine grid: {4,8,16,32,64,128} and
{12,24,48,96}. This needs no assumed exponent p: for x_n - L = C q^{-np}
with fixed ratio q=2 between successive refine values, the ratio
(x_{n+1}-L)/(x_n-L) is constant regardless of p, which is exactly what
Aitken's formula exploits.
"""
import json
import numpy as np
from scipy.optimize import curve_fit

with open('W1_convergence.json') as f:
    DATA = json.load(f)


def model(r, L, C, p):
    return L + C * np.power(r, -p)


def fit_L_free(refs, lams, L_bounds):
    p0 = [0.0, lams[0] * refs[0], 1.0]
    try:
        popt, pcov = curve_fit(model, refs, lams, p0=p0, bounds=(
            [L_bounds[0], -np.inf, 0.01], [L_bounds[1], np.inf, 10.0]),
            maxfev=20000)
        resid = lams - model(refs, *popt)
        sse = float(np.sum(resid**2))
        return popt, pcov, sse
    except Exception as e:
        return None, None, None


def fit_pure_power(refs, lams):
    def m(r, C, p):
        return C * np.power(r, -p)
    p0 = [lams[0] * refs[0], 1.0]
    popt, pcov = curve_fit(m, refs, lams, p0=p0,
                            bounds=([0, 0.01], [np.inf, 10.0]), maxfev=20000)
    resid = lams - m(refs, *popt)
    return popt, pcov, float(np.sum(resid**2))


def aitken_chain(refs_all, lams_all, chain):
    idx = {r: i for i, r in enumerate(refs_all)}
    out = []
    for i in range(len(chain) - 2):
        r0, r1, r2 = chain[i], chain[i + 1], chain[i + 2]
        if r0 not in idx or r1 not in idx or r2 not in idx:
            continue
        x0, x1, x2 = lams_all[idx[r0]], lams_all[idx[r1]], lams_all[idx[r2]]
        denom = x2 - 2 * x1 + x0
        if abs(denom) < 1e-300:
            out.append((r0, r1, r2, float('nan')))
            continue
        Lhat = x0 - (x1 - x0)**2 / denom
        out.append((r0, r1, r2, Lhat))
    return out


CHAIN_A = [4, 8, 16, 32, 64, 128]
CHAIN_B = [12, 24, 48, 96]

print("=" * 100)
for key, rows in DATA.items():
    refs = np.array([row['refine'] for row in rows], dtype=float)
    lams = np.array([row['lam_min_norm'] for row in rows], dtype=float)
    order = np.argsort(refs)
    refs, lams = refs[order], lams[order]

    print(f"\nstep ({key})   refine -> lam_min_norm")
    for r, l in zip(refs, lams):
        print(f"   refine={int(r):4d}  lam={l:.8e}")

    # (a) pure power law, L=0
    Ca, pa, ssea = fit_pure_power(refs, lams)
    print(f"  (a) lam=C r^-p (L=0):        C={Ca[0]:.4e} p={Ca[1]:.4f}  SSE={ssea:.3e}")

    # log-log linear fit (direct OLS on log r, log lam), all points and last 5
    for label, sl in (("all pts", slice(None)), ("last 5", slice(-5, None))):
        A = np.vstack([np.log(refs[sl]), np.ones(refs[sl].size)]).T
        coef, res, *_ = np.linalg.lstsq(A, np.log(lams[sl]), rcond=None)
        p_ll = -coef[0]
        print(f"      log-log OLS ({label}): p={p_ll:.4f}  "
              f"C=exp({coef[1]:.4f})={np.exp(coef[1]):.4e}")

    # (b)/(c) free L, unconstrained sign
    popt, pcov, sse = fit_L_free(refs, lams, (-np.inf, np.inf))
    if popt is not None:
        L, C, p = popt
        Lerr_local = float(np.sqrt(pcov[0, 0])) if np.isfinite(pcov[0, 0]) else float('nan')
        print(f"  (b/c) lam=L+C r^-p (free L): L={L:+.4e} (local-curvature err {Lerr_local:.2e})  "
              f"C={C:.4e} p={p:.4f}  SSE={sse:.3e}")
    else:
        print("  (b/c) fit failed to converge")

    # honest uncertainty: refit on nested trailing windows (k largest refine values)
    print("  L stability across trailing windows (k largest refine points used):")
    Ls = []
    for k in range(4, len(refs) + 1):
        rr, ll = refs[-k:], lams[-k:]
        popt_k, pcov_k, sse_k = fit_L_free(rr, ll, (-np.inf, np.inf))
        if popt_k is None:
            continue
        Ls.append(popt_k[0])
        print(f"      k={k:2d} (refine {int(rr[0])}..{int(rr[-1])}): "
              f"L={popt_k[0]:+.4e}  p={popt_k[2]:.3f}  SSE={sse_k:.2e}")
    if Ls:
        Ls = np.array(Ls)
        print(f"    -> spread across windows: min={Ls.min():+.4e} max={Ls.max():+.4e} "
              f"median={np.median(Ls):+.4e}  (this spread IS the honest uncertainty)")

    # constrained fits: force L>0 and force L<=0, compare SSE to unconstrained
    poptP, _, sseP = fit_L_free(refs, lams, (0.0, np.inf))
    poptN, _, sseN = fit_L_free(refs, lams, (-np.inf, 0.0))
    print(f"  constrained L>=0 fit: L={poptP[0]:+.4e} p={poptP[2]:.3f} SSE={sseP:.3e}")
    print(f"  constrained L<=0 fit: L={poptN[0]:+.4e} p={poptN[2]:.3f} SSE={sseN:.3e}")
    print(f"  SSE ratio (L<=0 forced)/(free) = {sseN/max(sse,1e-300):.3f}   "
          f"(near 1 means data does NOT distinguish sign of L)")

    # Aitken/Shanks, two independent ratio-2 chains
    print("  Aitken/Shanks extrapolation (needs no assumed p, exact for geometric refine ratio 2):")
    for name, chain in (("chain A (4,8,16,32,64,128)", CHAIN_A),
                         ("chain B (12,24,48,96)", CHAIN_B)):
        trip = aitken_chain(refs, lams, chain)
        for r0, r1, r2, Lhat in trip:
            print(f"      {name}: ({int(r0)},{int(r1)},{int(r2)}) -> L_hat={Lhat:+.4e}")
print("=" * 100)
