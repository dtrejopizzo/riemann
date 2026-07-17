"""
E67.9 -- signed-index detector for the terminal defect.

Register shift (Phase 67): from POSITIVE certificates (Haar/CP/q-dim, all blind to
phase cancellation -> S_abs) to a SIGNED certificate = the negative index

    ind_-(A_N - P_lambda) = # negative eigenvalues of the whitened defect
    D_N = I - A_N^{-1/2} P_lambda A_N^{-1/2}.

Omega_7  <=>  ind_-(D_N) = 0 for all N   (delta_N = lambda_min(D_N) >= 0).

This test validates the register BEFORE any q-deformation:
  (A) baseline zeta: ind_- should be 0 (delta_N marginal, -> 0+).
  (B) planted off-line zero pair rho=beta+i*gamma, 1-rho: ind_- should jump > 0.

If ind_- faithfully tracks off-line zeros, the signed index is the right object to
realize as a Jantzen index at a root of unity. If not, we learn what the twist lacks.
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

def whitened_defect_eigs(z0, N, Xi_deriv=None):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)   # J = A_N - Plam (Hermitian)
    W = H.inv_sqrt(H.herm(A_N))
    D = W * H.herm(J) * W                               # whitened defect
    Dnp = mp2np(D)
    Dnp = 0.5*(Dnp + Dnp.conj().T)
    return np.linalg.eigvalsh(Dnp)

def zeta_planted(z0_val, N, rho):
    """Xi_deriv for F(s) = zeta(s) * g(s), g = (s-rho)(s-(1-rho)) planting an off-line
       zero pair. Leibniz with g,g',g'' (g'''=0)."""
    s0 = mp.mpf(1)/2 + mp.mpc(0,1)*z0_val
    r  = rho
    rc = 1 - rho
    def gder(j, s):
        if j == 0: return (s-r)*(s-rc)
        if j == 1: return (s-r) + (s-rc)
        if j == 2: return mp.mpf(2)
        return mp.mpf(0)
    def Xi_deriv(k):
        # (zeta*g)^{(k)}(s0) = sum_j C(k,j) zeta^{(j)}(s0) g^{(k-j)}(s0)
        tot = mp.mpc(0)
        for j in range(k+1):
            tot += mp.binomial(k,j) * mp.zeta(s0, 1, j) * gder(k-j, s0)
        return tot
    return Xi_deriv

def report(z0, N, tag, Xi_deriv=None):
    e = whitened_defect_eigs(z0, N, Xi_deriv)
    negs = int(np.sum(e < -1e-12))
    print(f"  [{tag:22s}] N={N:2d}  lambda_min={e[0]:+.3e}  ind_-={negs}  (eigs: "
          + ", ".join(f"{v:+.2e}" for v in e[:min(4,len(e))]) + (" ...)" if len(e)>4 else ")"))
    return negs, e[0]

def main():
    t0, y = 100.0, 1.0
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    print(f"z0 = {t0} - {y}i\n")
    print("(A) baseline zeta -- expect ind_-=0, delta_N -> 0+ (marginal):")
    for N in (4, 6, 8, 10, 12):
        report(z0, N, "zeta", None)
    print()
    print("(B) planted off-line zero pair rho=beta+i*gamma near t0 -- expect ind_- > 0:")
    for beta in (0.65, 0.80, 0.95):
        gamma = t0
        rho = mp.mpf(str(beta)) + mp.mpc(0,1)*mp.mpf(str(gamma))
        print(f"  -- rho = {beta} + {gamma}i  (off the line by {beta-0.5:.2f}) --")
        for N in (4, 6, 8, 10):
            report(z0, N, f"planted b={beta}", zeta_planted(z0, N, rho))
    print()
    print("(C) control: planted ON-line zero (beta=0.5) -- should stay ind_-=0:")
    rho = mp.mpf("0.5") + mp.mpc(0,1)*mp.mpf(str(t0))
    for N in (4, 6, 8, 10):
        report(z0, N, "planted b=0.5", zeta_planted(z0, N, rho))

if __name__ == "__main__":
    main()
