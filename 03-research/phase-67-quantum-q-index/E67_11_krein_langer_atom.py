"""
E67.11 -- the Krein-Langer atom: off-line zero = one negative square.

Structural identity (from the harness): the terminal defect A_N - P_lambda is the
confluent Pick/Loewner jet of  h(z) = h_A + h_P = (log-derivative of Xi) at z0.
A zero of Xi at rho is a simple POLE of -Xi'/Xi with contribution  g_rho(z) = -1/(z-rho).

Krein-Langer atom (built from scratch, not looked up):
  - rho real (on-line):   -1/(z-rho) is anti-/Herglotz -> Pick jet is (semi)definite,
                          ind_- = 0.  No negative square.
  - rho complex (off-line): 1/(z-rho) is a generalized Nevanlinna function with exactly
                          ONE negative square -> ind_- jumps.  Each off-line zero (its
                          conjugate/reflection pair) contributes to kappa = ind_-.

kappa = ind_-(defect jets) = # non-real zeros of Xi = Krein-Langer index. This is the
signed certificate; a Pontryagin module Pi_kappa (su(1,1) at a root of unity) is its
algebraic home. This script verifies the atom and the additivity of kappa, and the
robustness ind_-=0 for zeta at larger N.
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

def pole_taylor(z0, M, rho, sign=-1.0):
    """Taylor coeffs (0..M) of g(z) = sign/(z - rho) around z0.
       g = sign*(z0-rho)^{-1} * sum_p (-1)^p ((z-z0)/(z0-rho))^p."""
    d = z0 - rho
    out = []
    for p in range(M+1):
        out.append(mp.mpf(sign) * ((-1)**p) / d**(p+1))
    return out

def ind_minus_of_jet(coeffs, z0, N, tol=1e-9):
    J = H.herm(H.pick_jet(coeffs, z0, N))
    e = np.linalg.eigvalsh(0.5*(mp2np(J)+mp2np(J).conj().T))
    return int(np.sum(e < -tol)), e

def combine(coeff_lists):
    M = len(coeff_lists[0]) - 1
    return [sum(cl[p] for cl in coeff_lists) for p in range(M+1)]

def main():
    t0, y = 100.0, 1.0
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    N = 8; M = 2*N + 2
    print(f"z0 = {t0} - {y}i,  N={N}\n")

    print("(1) single-zero atom:  ind_- of Pick jet of -1/(z-rho)")
    print("    beta=Re(s) via s=1/2+iz; on-line rho at height t0 means the pole at z=t0.")
    for beta in (0.50, 0.55, 0.65, 0.80, 0.95):
        # zero of Xi at s=beta+i*t0  <=>  z = t0 - i(beta-1/2)  (since s=1/2+iz)
        rho_z = mp.mpc(mp.mpf(str(t0)), -(mp.mpf(str(beta)) - mp.mpf("0.5")))
        c = pole_taylor(z0, M, rho_z, sign=-1.0)
        k, e = ind_minus_of_jet(c, z0, N)
        print(f"   beta={beta:.2f}  off-by={beta-0.5:+.2f}  ind_-={k}  min-eig={e[0]:+.3e}")

    print("\n(2) additivity: K off-line zeros -> kappa grows with K")
    for K in (0, 1, 2, 3):
        lists = []
        # K off-line zeros at beta=0.8, spread in height, each with reflection partner
        for j in range(K):
            g = t0 + 3.0*j
            rho_z  = mp.mpc(mp.mpf(str(g)), -(mp.mpf("0.8") - mp.mpf("0.5")))   # beta=0.8
            rho_z2 = mp.mpc(mp.mpf(str(g)), +(mp.mpf("0.8") - mp.mpf("0.5")))   # reflection beta=0.2
            lists.append(pole_taylor(z0, M, rho_z,  -1.0))
            lists.append(pole_taylor(z0, M, rho_z2, -1.0))
        if not lists:
            lists = [pole_taylor(z0, M, mp.mpc(mp.mpf(str(t0)), 0), -1.0)]  # on-line dummy
        c = combine(lists)
        k, e = ind_minus_of_jet(c, z0, N)
        print(f"   K={K} off-line zeros  ->  ind_- (kappa) = {k}   min-eig={e[0]:+.3e}")

    print("\n(3) robustness: exact zeta defect stays ind_-=0 at larger N")
    for Nz in (8, 12, 16, 20):
        A_N, Plam, J = H.arithmetic_jets(z0, Nz, None)
        W = H.inv_sqrt(H.herm(A_N))
        D = mp2np(W*H.herm(J)*W); D = 0.5*(D+D.conj().T)
        e = np.linalg.eigvalsh(D)
        print(f"   zeta N={Nz:2d}  ind_-={int(np.sum(e<-1e-11))}  lambda_min={e[0]:+.2e}")

if __name__ == "__main__":
    main()
