"""
E67.12 -- twisted root-of-unity Shapovalov form: does the q-regularization stabilize
the signed index and separate on-line from off-line?

Motivation. E67.11 showed the RAW confluent-jet index ind_-(A_N-P_lambda) is a faithful
DETECTOR (0 <=> RH) but an UNSTABLE COUNTER (single off-line pole -> 7 at N=8). The
root-of-unity Shapovalov form is intrinsically finite (finite Jantzen filtration) and is
the candidate to REGULARIZE the count.

Construction (a MODEL of the twist, honestly labeled -- not yet the canonical Euler twist).
Bare discrete-series norms:   r_n = prod_{j<=n} [j]_q [j+2y-1]_q.
Prime weight-twist:           [j+2y-1] -> [j+2y-1 + c*tau_j],
  where tau_j = diagonal of the WHITENED prime jet  diag(A_N^{-1/2} P_lambda A_N^{-1/2})_j,
  a real quantity built from {Lambda(n)} by the harness -- NOT fitted to zero locations.

Tests:
  (I)  q -> 1 sanity: twist reduces to a real weight shift.
  (II) q = e^{i pi/ell}: is ind_-(twisted) STABLE in n, and does it separate
       zeta (RH true) from a planted off-line zero (RH false)?

Honest reading: this probes whether the q-algebra supplies a stable signed separation.
It does NOT claim the canonical (Euler-derived) twist; c and ell are model knobs.
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
    def gder(j,s):
        return {0:(s-r)*(s-rc), 1:(s-r)+(s-rc), 2:mp.mpf(2)}.get(j, mp.mpf(0))
    def Xi_deriv(k):
        return sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*gder(k-j,s0) for j in range(k+1))
    return Xi_deriv

def whitened_prime_diag(z0, N, Xi_deriv=None):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)
    W = H.inv_sqrt(H.herm(A_N))
    WP = mp2np(W*H.herm(Plam)*W)
    return np.real(np.diag(WP))

def qnum(m, q):
    if abs(q-1) < 1e-14: return complex(m)
    return (q**m - q**(-m))/(q - q**(-1))

def twisted_ind_minus(tau, y, q, c):
    n_max = len(tau)
    r = np.ones(n_max+1, dtype=complex)
    negs = []
    for n in range(1, n_max+1):
        fac = qnum(n, q) * qnum(n + 2*y - 1 + c*tau[n-1], q)
        r[n] = r[n-1]*fac
        negs.append(int(np.sum(r[:n+1].real < -1e-9)))
    return negs  # ind_- as function of level

def main():
    t0, y = 100.0, 1.0
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    N = 16
    tau_zeta = whitened_prime_diag(z0, N, None)
    rho = mp.mpf("0.8") + mp.mpc(0,1)*mp.mpf(str(t0))
    tau_off = whitened_prime_diag(z0, N, zeta_planted(z0, rho))
    print(f"z0={t0}-{y}i  N={N}")
    print(f"tau_zeta (whitened prime diag) range: [{tau_zeta.min():.3f}, {tau_zeta.max():.3f}]")
    print(f"tau_off  (beta=0.8 planted)    range: [{tau_off.min():.3f}, {tau_off.max():.3f}]\n")

    print("(II) ind_-(twisted Shapovalov) at q=e^{i pi/ell}, final-level value:")
    print("     comparing zeta-twist vs off-line-twist; stable separation is the goal.\n")
    print("  ell   c      zeta:ind_-(final,[stable?])    offline:ind_-(final,[stable?])   sep")
    for ell in (7, 11, 13, 17):
        q = np.exp(1j*np.pi/ell)
        for c in (0.5, 1.0, 2.0):
            nz = twisted_ind_minus(tau_zeta, y, q, c)
            no = twisted_ind_minus(tau_off,  y, q, c)
            stab_z = "stable" if len(set(nz[-4:]))==1 else "drift"
            stab_o = "stable" if len(set(no[-4:]))==1 else "drift"
            sep = no[-1] - nz[-1]
            print(f"  {ell:3d}  {c:.1f}   zeta={nz[-1]:2d} [{stab_z:6s}]            "
                  f"off={no[-1]:2d} [{stab_o:6s}]           {sep:+d}")
    print("\n  (final = ind_- at top level; [stable]=constant over last 4 levels; sep=off-zeta)")

    print("\n(interpretation guide)")
    print("  want: sep>0 consistently AND zeta ind_- stable & small (ideally 0).")
    print("  if zeta ind_- is nonzero/unstable too, the model twist does not regularize;")
    print("  the separation would then live only in the raw jet, not the q-form.")

if __name__ == "__main__":
    main()
