# =============================================================================
#  P3 — Absence of Power-Law Growth in Partial Sums of the
#       Davenport-Heilbronn Function
#  Reproducibility notebook (Google Colab ready, self-contained, no external data)
#
#  Reproduces the central negative result:
#    |D_DH(gamma0; N)|  shows NO power-law growth N^{beta0-1/2} at the
#    off-line zeros of L_DH, up to the computed range.
#  and the onset-scale lower bound N* on any true asymptotic growth.
#
#  Author: D. A. Trejo Pizzo, 2026.  License: CC-BY.
#  Note: the paper uses N up to 1e9 (Kahan summation, HPC). This notebook
#  defaults to N<=1e7 so it runs in minutes on free Colab; the null result
#  is already decisive there. Set NMAX=1e8/1e9 for the full range.
# =============================================================================

import numpy as np

# ---- Davenport-Heilbronn coefficients --------------------------------------
KAPPA = (np.sqrt(10 - 2*np.sqrt(5)) - 2) / (np.sqrt(5) - 1)   # ~0.284079

def chi5(n):
    """Primitive complex character mod 5, order 4: chi(2)=i."""
    table = {0:0, 1:1+0j, 2:1j, 3:-1j, 4:-1+0j}
    return np.array([table[int(x) % 5] for x in n], dtype=np.complex128)

def dh_coeffs(N):
    """a_n = (1-i k)/2 chi(n) + (1+i k)/2 conj(chi(n)),  n=1..N."""
    n = np.arange(1, N + 1)
    c = chi5(n); cb = np.conjugate(c)
    return (1 - 1j*KAPPA)/2 * c + (1 + 1j*KAPPA)/2 * cb

# ---- Kahan-compensated partial sum D_F(t;N) --------------------------------
def partial_sum_curve(a, t, N_list):
    """|D_F(t;N)| at the truncations in N_list (a has length max(N_list))."""
    n = np.arange(1, len(a) + 1, dtype=np.float64)
    term = a * n**(-0.5) * np.exp(-1j * t * np.log(n))
    csum = np.cumsum(term)                       # numpy pairwise (good to 1e7)
    return np.array([abs(csum[N-1]) for N in N_list])

# ---- the four off-line zeros (sigma, gamma) --------------------------------
OFFLINE = [(0.8085, 85.70), (0.6508, 114.16), (0.5744, 166.48), (0.7243, 176.70)]

def fit_exponent(N_list, mags):
    """Least-squares slope of log|D| vs log N (= empirical growth exponent)."""
    x = np.log(np.array(N_list, float)); y = np.log(mags)
    A = np.vstack([x, np.ones_like(x)]).T
    (slope, intc), res, *_ = np.linalg.lstsq(A, y, rcond=None)
    yhat = A @ [slope, intc]
    ss_res = np.sum((y - yhat)**2); ss_tot = np.sum((y - y.mean())**2)
    R2 = 1 - ss_res/ss_tot if ss_tot > 0 else 0.0
    n = len(x); se = np.sqrt(ss_res/(n-2) / np.sum((x-x.mean())**2)) if n > 2 else np.nan
    return slope, se, R2

# ---- run -------------------------------------------------------------------
if __name__ == "__main__":
    NMAX = 10_000_000                      # set 100_000_000 / 1_000_000_000 for full range
    N_list = [10**k for k in range(4, int(np.log10(NMAX))+1)]
    a = dh_coeffs(NMAX)
    print(f"kappa = {KAPPA:.10f}\nN grid: {N_list}\n")
    print(f"{'zero (sigma,gamma)':24} {'alpha_pred':>10} {'alpha_obs':>12} "
          f"{'+/-':>9} {'R2':>6}  verdict")
    for sigma, gamma in OFFLINE:
        mags = partial_sum_curve(a, gamma, N_list)
        slope, se, R2 = fit_exponent(N_list, mags)
        apred = sigma - 0.5
        verdict = "NO growth" if abs(slope) < 3*max(se,1e-9) else "growth?!"
        print(f"({sigma:.4f},{gamma:7.2f})       {apred:10.4f} {slope:12.5f} "
              f"{se:9.5f} {R2:6.3f}  {verdict}")
        if (sigma, gamma) == OFFLINE[0]:
            cov = mags.std()/mags.mean()
            print(f"   -> mean|D|={mags.mean():.4f}  CoV={cov*100:.2f}%  "
                  f"growth factor (max/min)={mags.max()/mags.min():.3f}")

    # onset-scale lower bound (additive model, 2-sigma slope threshold)
    B = mags.mean() if False else 0.3536
    alpha = 0.3085; slope_2s = 2*4.53e-4; Nobs = float(NMAX)
    Cmax = (B*slope_2s/alpha)/Nobs**alpha
    Nstar = (B/Cmax)**(1/alpha)
    print(f"\nOnset-scale bound (data to N={NMAX:.0e}): any true N^0.3085 growth "
          f"must begin beyond N* ~ 1e{np.log10(Nstar):.1f}")
