"""
E67.18 -- Szego law for the terminal defect: ind_-/N -> measure{sigma<0}.

Classical Szego / Avram-Parter: for a (Hermitian) Toeplitz sequence T_N with symbol sigma,
   #{negative eigenvalues of T_N} / N  ->  (1/2pi) measure{theta : sigma(theta) < 0}.

The terminal defect A_N - P_lambda is approximately Toeplitz with symbol sigma = sigma_A - sigma_P.
So:
   Omega_7 (ind_-=0 for all N)  <=>  measure{sigma<0} = 0  <=>  sigma >= 0  <=>  RH.

This test verifies the Szego connection: for a planted off-line zero, does
ind_-(A_N - P_lambda)/N approach the symbol measure{sigma<0} (~0.5)? And for zeta, does it stay 0?
Confirming this turns the previously-puzzling linear growth of ind_- (E67.9/E67.11) into a clean
classical law and states the forcer as a symbol-measure identity.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(M):
    return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)], dtype=complex)

def planted(z0, rho):
    s0 = mp.mpf(1)/2 + mp.mpc(0,1)*z0
    r, rc = rho, 1-rho
    def g(j,s): return {0:(s-r)*(s-rc),1:(s-r)+(s-rc),2:mp.mpf(2)}.get(j,mp.mpf(0))
    return lambda k: sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*g(k-j,s0) for j in range(k+1))

def symbol_measure_neg(z0, Nsym, Xi_deriv, ntheta=2000):
    A_N, Plam, _ = H.arithmetic_jets(z0, Nsym, Xi_deriv)
    A = mp2np(H.herm(A_N)); P = mp2np(H.herm(Plam))
    th = np.linspace(-np.pi, np.pi, ntheta)
    def sym(M):
        N=M.shape[0]; s=np.zeros(ntheta,dtype=complex)
        for d in range(-(N-1),N):
            s += np.mean([M[j,j+d] for j in range(max(0,-d),min(N,N-d))])*np.exp(1j*d*th)
        return np.real(s)
    sig = sym(A)-sym(P)
    return np.mean(sig < -1e-9)

def ind_minus_defect(z0, N, Xi_deriv, tol=1e-9):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)
    Jn = mp2np(H.herm(J)); Jn = 0.5*(Jn+Jn.conj().T)
    return int(np.sum(np.linalg.eigvalsh(Jn) < -tol))

def main():
    t0, y = 100.0, 1.0
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    print(f"z0={t0}-{y}i\n")
    print("Szego law:  ind_-(A_N - P_lambda)/N  vs  measure{sigma<0}\n")

    cases = [("zeta", None),
             ("offline b=0.8", planted(z0, mp.mpf("0.8")+mp.mpc(0,1)*mp.mpf(str(t0)))),
             ("offline b=0.95", planted(z0, mp.mpf("0.95")+mp.mpc(0,1)*mp.mpf(str(t0))))]
    for tag, xd in cases:
        meas = symbol_measure_neg(z0, 14, xd)
        print(f"  [{tag}]  symbol measure{{sigma<0}} = {meas:.3f}")
        row = []
        for N in (6, 10, 14, 18, 22):
            k = ind_minus_defect(z0, N, xd)
            row.append(f"N={N}: ind_-={k} ({k/N:.2f})")
        print("     " + "   ".join(row))
        print()
    print("Reading: ind_-/N should approach measure{sigma<0}. zeta -> 0 (RH); off-line -> ~0.5.")
    print("Forcer, symbol form:  measure{sigma_A < sigma_P} = 0  for every gauge  <=>  Omega_7.")

if __name__ == "__main__":
    main()
