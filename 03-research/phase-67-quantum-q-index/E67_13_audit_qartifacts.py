"""
E67.13 -- AUDIT: is the nonzero zeta-index of E67.12 an RH signal or a root-of-unity artifact?

Hypothesis. At q=e^{i pi/ell}, [m]_q = sin(m pi/ell)/sin(pi/ell) < 0 for ell<m<2ell, etc.
So the BARE Shapovalov form (NO prime twist, NO zeros) already has negative directions:
pure q-arithmetic artifacts, unrelated to RH. If ind_-(bare) matches ind_-(zeta-twisted)
from E67.12, then the zeta "index" there was artifact, and the root-of-unity form
CONTAMINATES the signed certificate: the RH content is drowned by q-negatives.

This audit computes, for the SAME (ell, y, N) as E67.12:
  (a) ind_- of the bare root-of-unity Shapovalov norms (no prime data at all),
  (b) ind_- of the zeta-twisted norms (E67.12 reproduction),
  (c) ind_- of an off-line-twisted norms,
and reports whether (b) is explained by (a) [=> contamination, artifact] or exceeds it
[=> genuine RH content survives].
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

def whitened_prime_diag(z0, N, Xi_deriv=None):
    A_N, Plam, J = H.arithmetic_jets(z0, N, Xi_deriv)
    W = H.inv_sqrt(H.herm(A_N))
    return np.real(np.diag(mp2np(W*H.herm(Plam)*W)))

def qnum(m,q):
    if abs(q-1)<1e-14: return complex(m)
    return (q**m - q**(-m))/(q - q**(-1))

def ind_minus(tau, y, q, c, n_max):
    r = 1.0+0j; neg = 0
    for n in range(1, n_max+1):
        t = 0.0 if tau is None else c*tau[n-1]
        r = r * qnum(n,q) * qnum(n+2*y-1+t, q)
        if r.real < -1e-9: neg += 1
    return neg

def main():
    t0, y, N = 100.0, 1.0, 16
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    tau_z = whitened_prime_diag(z0, N, None)
    tau_o = whitened_prime_diag(z0, N, zeta_planted(z0, mp.mpf("0.8")+mp.mpc(0,1)*mp.mpf(str(t0))))
    print(f"z0={t0}-{y}i  N={N}  y={y}\n")
    print("  ell  c    bare(no data)   zeta-twist   offline-twist   |  zeta-bare   off-bare")
    print("  ---------------------------------------------------------------------------------")
    for ell in (7, 11, 13, 17):
        q = np.exp(1j*np.pi/ell)
        for c in (0.5, 1.0, 2.0):
            b  = ind_minus(None,  y, q, c, N)
            iz = ind_minus(tau_z, y, q, c, N)
            io = ind_minus(tau_o, y, q, c, N)
            print(f"  {ell:3d} {c:.1f}      {b:3d}           {iz:3d}          {io:3d}"
                  f"        |   {iz-b:+3d}       {io-b:+3d}")
    print("\n  KEY COLUMNS: (zeta-bare) and (off-bare).")
    print("  If zeta-bare ~ 0 : zeta index is pure q-artifact = the bare form -> CONTAMINATION.")
    print("  If off-bare  > 0 consistently : genuine RH content survives above the artifact floor.")
    print("  If off-bare ~ 0 too : the q-form does not carry RH content beyond the artifact.")

if __name__ == "__main__":
    main()
