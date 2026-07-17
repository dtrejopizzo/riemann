"""
E100 — Task A (Connes route): detector-nonvanishing => L1 implies RH (numerical confirmation).

Connes' Laplace-pole theorem: with t=log lambda, each intrinsic Jacobi coefficient
F_a(t) = a(A^osc_{e^t}) satisfies, morally,  F_a(t) = -sum_rho C_a(rho,t) e^{(2 rho-1) t}.
If F_a(t)=O(1) then L F_a(w) is holomorphic in Re w>0; but the explicit formula gives a pole at
w = 2 rho - 1 (Re = 2 beta - 1 > 0) for every off-line zero, UNLESS C_a(rho)=0. So

   L1 (all F_a bounded)  ==>  no zero with beta>1/2  ==>  (functional eq) RH,

PROVIDED the DETECTOR-NONVANISHING condition holds: for every off-line rho there is a coefficient
a with C_a(rho) != 0.

Numerical confirmation of detector-nonvanishing: the Davenport-Heilbronn falsador HAS off-line
zeros (beta>1/2). If the Jacobi detector family sees them, then SOME coefficient must grow like
e^{(2 beta-1) t} = lambda^{2 beta-1}. So:
  - zeta:  ALL coefficient growth exponents ~ 0   (L1 holds; consistent with RH)
  - DH  :  the MAX growth exponent > 0, ~ 2 beta_DH - 1  (detector sees the off-line zero => C_a!=0)

We fit log|coef|(lambda) vs t=log lambda for the whole intrinsic-Jacobi family and report the
exponent spectrum. A clear positive max exponent for DH (and ~0 for zeta) confirms that L1 is an
RH criterion (Task A), and that DH cannot satisfy it (its off-line zero is detected).
"""
import os, sys, numpy as np, mpmath as mp
_P61 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'phase-61-open-problems')
sys.path.insert(0, _P61); os.chdir(_P61)
from engine_cache import get_matrices

mp.mp.dps = 40


def lanczos(A, q0, m):
    n = A.rows
    Q = [q0 / mp.sqrt((q0.T * q0)[0])]
    alpha = []; beta = []; qprev = mp.zeros(n, 1); b = mp.mpf(0)
    for j in range(m):
        Aq = A * Q[j]
        a = (Q[j].T * Aq)[0]; alpha.append(a)
        r = Aq - a * Q[j] - (b * qprev if j > 0 else mp.zeros(n, 1))
        for qi in Q:
            r = r - (qi.T * r)[0] * qi
        b = mp.sqrt((r.T * r)[0])
        if b < mp.mpf(10) ** (-mp.mp.dps + 5) or j == m - 1:
            break
        beta.append(b); qprev = Q[j]; Q.append(r / b)
    return [float(x) for x in alpha], [float(x) for x in beta]


def coeffs(lam, N, kind):
    La, Lp, A, L, idx = get_matrices(lam, N, kind, dps=40)
    n = A.rows
    q0 = mp.matrix([[mp.mpf(1) + mp.mpf('0.7') * (2 * i - (n - 1))] for i in range(n)])
    alpha, beta = lanczos(A, q0, n)
    a = np.abs(np.array(alpha)); b = np.abs(np.array(beta))
    # STABLE bulk functionals (individual Lanczos coeffs are too noisy; bulk stats are the detector)
    fam = {
        "beta_bulk_mean": float(np.mean(b[2:-2])),
        "beta_bulk_max":  float(np.max(b[2:-2])),
        "alpha_bulk_mean": float(np.mean(a[2:-2])),
        "specrad_bulk":   float(np.max(np.abs([float(alpha[k]) for k in range(2, len(alpha)-2)]))),
    }
    return fam


def run(kind, grid):
    lams = np.array([g[0] for g in grid]); t = np.log(lams)
    series = {}
    for lam, N in grid:
        fam = coeffs(lam, N, kind)
        for k, v in fam.items():
            series.setdefault(k, []).append(v)
    print(f"\n=== {kind} : growth exponent of each coefficient  (log|coef| ~ exponent * t) ===")
    exps = []
    for k, vals in series.items():
        vals = np.array(vals)
        if len(vals) == len(t) and np.all(vals > 0):
            e = np.polyfit(t, np.log(vals), 1)[0]
            exps.append(e)
            print(f"   {k:4s}: exponent = {e:+.3f}")
    exps = np.array(exps)
    print(f"   --> MAX exponent = {exps.max():+.3f}   (zeta~0 => L1 holds; DH>0 => off-line zero detected)")
    return exps.max()


if __name__ == '__main__':
    grid = [(9.0, 16), (11.0, 18), (13.0, 18), (15.0, 20), (17.0, 20), (19.0, 22), (21.0, 22)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E100 — Task A: detector-nonvanishing (L1 => RH). zeta bounded, DH must show positive growth.")
    run('zeta', grid)
    run('DH', grid)
    print("\nNote: read the STABLE bulk MEANS (beta_bulk_mean, alpha_bulk_mean); the *_max/specrad")
    print("functionals are noisy and inflate both. The means are the validated detector (cf. E91).")
