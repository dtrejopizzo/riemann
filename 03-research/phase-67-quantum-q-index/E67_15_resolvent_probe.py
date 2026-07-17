"""
E67.15 -- empirical probe of the pivotal q-resolvent character and the q-index polynomial.

  D_N = A_N^{-1/2}(A_N - P_lambda) A_N^{-1/2}   (exact whitened defect, harness)
  G_q e_n = q^{2(n+y)} e_n                       (canonical pivotal K^2)
  R_N(z;q) = Tr(G_q (z-D_N)^{-1})                (poles at eig(D_N), residue = qTr of eigenproj)
  Q_N(q)   = qTr(Pi_{N,-}) = sum_{lambda_i<0} qdim(v_i)
           = q^{2y} sum_n a_n (q^2)^n,   a_n = <e_n, Pi_{N,-} e_n> >= 0.

Purpose (honest): check the framing numerically and see whether the negative-residue data has
recognizable q-structure (would suggest a closed-form / fusion evaluation) or is generic (no
closed form near). This does NOT prove anything: D_N is diagonalized here (uses zeta), so Q_N=0
for zeta is just the E67.9 detector, not the forcing theorem.
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

def neg_projection_diag(D, tol=1e-9):
    w, V = np.linalg.eigh(D)
    P = np.zeros_like(D)
    for i in range(len(w)):
        if w[i] < -tol:
            v = V[:,i:i+1]
            P += v @ v.conj().T
    return np.real(np.diag(P)), w

def main():
    t0, y, N = 100.0, 1.0, 12
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    print(f"z0={t0}-{y}i  N={N}\n")

    a_zeta, w_zeta = neg_projection_diag(whitened_defect(z0, N, None))
    print("zeta:  a_n = diag(Pi_-) :", np.array2string(a_zeta, precision=2, suppress_small=True))
    print(f"       sum a_n = Tr(Pi_-) = {a_zeta.sum():.3e}   (Q_N(q)=0 for all q  <=>  D_N>=0)")
    print(f"       eigs(D_N) min = {w_zeta[0]:+.2e}\n")

    rho = mp.mpf("0.8")+mp.mpc(0,1)*mp.mpf(str(t0))
    a_off, w_off = neg_projection_diag(whitened_defect(z0, N, zeta_planted(z0, rho)))
    print("offline b=0.8:  a_n = diag(Pi_-) :", np.array2string(a_off, precision=3, suppress_small=True))
    print(f"       sum a_n = Tr(Pi_-) = {a_off.sum():.3f}   (nonzero polynomial => D_N NOT >=0)")
    print(f"       eigs(D_N) neg count = {int((w_off<-1e-9).sum())}\n")

    print("Q_N(q)/q^{2y} = sum_n a_n (q^2)^n  evaluated at roots q=e^{i pi/ell}:")
    print("  ell   |Q_zeta/q^2y|      |Q_off/q^2y|")
    for ell in (5, 7, 11, 13, 17, 23):
        x = np.exp(2j*np.pi/ell)   # q^2 = e^{2 i pi/ell}
        Qz = sum(a_zeta[n]*x**n for n in range(N))
        Qo = sum(a_off[n]*x**n for n in range(N))
        print(f"  {ell:3d}   {abs(Qz):.3e}        {abs(Qo):.3e}")

    print("\nStructure probe of a_n (offline) -- ratios a_{n+1}/a_n (recognizable q-decay?):")
    with np.errstate(divide='ignore', invalid='ignore'):
        ratios = [a_off[n+1]/a_off[n] if a_off[n]>1e-12 else np.nan for n in range(N-1)]
    print("  " + "  ".join(f"{r:.2f}" if not np.isnan(r) else " -- " for r in ratios))
    print("\nHonest note: Q_zeta ~ 0 here is the E67.9 detector (D_N diagonalized, uses zeta),")
    print("NOT the forcing theorem. The open content is an INDEPENDENT closed form for Q_N(q).")

if __name__ == "__main__":
    main()
