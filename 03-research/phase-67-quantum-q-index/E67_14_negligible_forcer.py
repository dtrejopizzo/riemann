"""
E67.14 -- the forcer precondition: negligibility needs off-diagonal spreading.

Regularization mechanism (the forcer): quotient the root-of-unity form by NEGLIGIBLES
= directions with vanishing quantum dimension under the canonical pivotal
    g = K^2,   g e_n = q^{2(n+y)} e_n    (U_q(su(1,1))).
q-dimension of a direction v = sum_n c_n e_n:
    qdim(v) = | sum_n |c_n|^2 q^{2(n+y)} |.
A direction is negligible iff qdim(v) = 0 (killed by the quotient).

Two facts to establish:
 (1) DIAGONAL forms (E67.10-13): eigenvectors are e_n, qdim(e_n)=|q^{2(n+y)}|=1 -> NOTHING
     is negligible -> the quotient is trivial -> artifacts CANNOT be removed. This is exactly
     why E67.13 could not regularize (contamination + fabrication survive).
 (2) OFF-DIAGONAL forms: eigenvectors spread over levels, qdim can be < 1 or ~0 -> negligible
     directions EXIST. The forcer works iff the ARTIFACT negatives are negligible while the
     GENUINE off-line negatives are non-negligible.

Test: for the EXACT off-diagonal defect J = A_N - P_lambda (harness), for a planted off-line
zero (which has genuine negative directions), compute qdim of the negative eigenvectors and
compare to the diagonal baseline. Do genuine RH negatives carry nonzero qdim (survive the
quotient, cannot hide)?  That is the property the forcer needs.
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

def whitened_defect(z0, N, Xi_deriv=None):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)
    W = H.inv_sqrt(H.herm(A_N))
    D = mp2np(W*H.herm(J)*W); return 0.5*(D+D.conj().T)

def qdim_of_vector(c, y, q):
    n = np.arange(len(c))
    piv = q**(2*(n+y))
    return abs(np.sum((np.abs(c)**2) * piv))

def analyze(name, D, y, q, tol=1e-9):
    w, V = np.linalg.eigh(D)
    negs = [(w[i], V[:,i]) for i in range(len(w)) if w[i] < -tol]
    print(f"  [{name}]  ind_- = {len(negs)}")
    for lam, v in negs:
        qd = qdim_of_vector(v, y, q)
        spread = 1.0/np.sum(np.abs(v)**4)   # participation ratio: 1=localized, N=fully spread
        print(f"     lambda={lam:+.3e}  qdim={qd:.4f}  spread(PR)={spread:.2f}")
    return negs

def main():
    t0, y, N = 100.0, 1.0, 12
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    for ell in (7, 11, 13):
        q = np.exp(1j*np.pi/ell)
        print(f"\n===== q = e^(i pi/{ell}),  y={y},  N={N} =====")
        # (1) diagonal baseline: e_n directions all have |qdim|=1
        qd_en = [qdim_of_vector(np.eye(N)[:,n], y, q) for n in range(N)]
        print(f"  (1) diagonal e_n qdim: min={min(qd_en):.4f} max={max(qd_en):.4f}"
              f"  -> nothing negligible, quotient trivial (why E67.13 failed)")
        # (2) exact off-diagonal defect, zeta (marginal, expect ind_-=0)
        analyze("zeta defect", whitened_defect(z0, N, None), y, q)
        # (2) exact off-diagonal defect, planted off-line zero (genuine negatives)
        rho = mp.mpf("0.8")+mp.mpc(0,1)*mp.mpf(str(t0))
        analyze("offline defect b=0.8", whitened_defect(z0, N, zeta_planted(z0, rho)), y, q)
    print("\nForcer criterion: if off-line negatives have qdim well above 0 (non-negligible) and")
    print("spread (PR>1), the quotient keeps them -> off-line content cannot hide -> quotient-")
    print("positivity would force RH. If they are negligible (qdim~0), the forcer is empty.")

if __name__ == "__main__":
    main()
