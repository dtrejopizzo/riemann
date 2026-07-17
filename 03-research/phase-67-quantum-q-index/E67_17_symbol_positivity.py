"""
E67.17 -- symbol-positivity form of Omega_7 (Toeplitz route).

A_N, P_lambda are approximately Toeplitz (E67.16). For Hermitian Toeplitz matrices the
generalized domination  A_N >= P_lambda  <=>  sigma_A(theta) >= sigma_P(theta) pointwise
(Szego / Avram-Parter, in the symbol limit). Omega_7 <=> sigma_A - sigma_P >= 0 on the circle
<=> the symbol of -Xi'/Xi is nonnegative <=> RH.

We extract band-averaged symbols
   t_d = mean_j M[j, j+d],   sigma(theta) = sum_d t_d e^{i d theta}
for A_N and P_lambda, and check whether  sigma_A - sigma_P >= 0  for zeta (RH true) and dips
negative for a planted off-line zero (RH false). This is the honest symbol-level detector; the
forcing statement becomes 'the pivotal-weighted symbol integral has no negative part'.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(Mx):
    return np.array([[complex(Mx[i,j]) for j in range(Mx.cols)] for i in range(Mx.rows)], dtype=complex)

def zeta_planted(z0_val, rho):
    s0 = mp.mpf(1)/2 + mp.mpc(0,1)*z0_val
    r, rc = rho, 1-rho
    def gder(j,s): return {0:(s-r)*(s-rc),1:(s-r)+(s-rc),2:mp.mpf(2)}.get(j,mp.mpf(0))
    return lambda k: sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*gder(k-j,s0) for j in range(k+1))

def band_symbol(M, ntheta=400):
    """Band-averaged Toeplitz symbol of Hermitian M."""
    N = M.shape[0]
    td = {}
    for d in range(-(N-1), N):
        vals = [M[j, j+d] for j in range(max(0,-d), min(N, N-d))]
        td[d] = np.mean(vals)
    th = np.linspace(-np.pi, np.pi, ntheta)
    sig = np.zeros(ntheta, dtype=complex)
    for d, t in td.items():
        sig += t*np.exp(1j*d*th)
    return th, np.real(sig)  # Hermitian => real symbol

def analyze(z0, N, Xi_deriv, tag):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)
    A = mp2np(H.herm(A_N)); P = mp2np(H.herm(Plam))
    th, sA = band_symbol(A); _, sP = band_symbol(P)
    diff = sA - sP
    negfrac = np.mean(diff < -1e-9)
    print(f"  [{tag}]  min(sigma_A - sigma_P) = {diff.min():+.4f}   "
          f"frac(theta: sigma_A<sigma_P) = {negfrac:.3f}")
    return th, sA, sP, diff

def main():
    t0, y, N = 100.0, 1.0, 12
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    print(f"z0={t0}-{y}i  N={N}\n")
    print("Symbol-positivity detector  Omega_7 <=> sigma_A - sigma_P >= 0 on the circle:\n")
    analyze(z0, N, None, "zeta (RH true)")
    for beta in (0.65, 0.80, 0.95):
        rho = mp.mpf(str(beta)) + mp.mpc(0,1)*mp.mpf(str(t0))
        analyze(z0, N, zeta_planted(z0, rho), f"offline beta={beta}")
    print("\nReading:")
    print("  zeta: min(sigma_A-sigma_P) should be >= ~0 (symbol nonnegative = RH true).")
    print("  offline: should dip clearly negative (symbol goes negative = RH false).")
    print("  If clean, Omega_7 = symbol nonnegativity of -Xi'/Xi, a Toeplitz/Szego statement,")
    print("  and the pivotal q-trace forcing becomes a symbol integral (Borodin-Okounkov surface).")

if __name__ == "__main__":
    main()
