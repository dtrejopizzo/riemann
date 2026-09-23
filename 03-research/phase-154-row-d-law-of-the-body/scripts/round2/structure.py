"""R154 round 2, script 1: bookkeeping verification, subordinate-BM structure,
subordination upper bound on lambda_min(A_T).   All values printed are reproducible.
"""
import math, sys, numpy as np, mpmath as mp
sys.path.insert(0, '/home/trabajo/Documentos/research/riemann/03-research/phase-153-row-d-sign-carrying-endpoint/scripts/round6')
import core
from scipy.special import psi as dg

mp.mp.dps = 30
C0 = float(mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi))
print("C0 =", C0)

# ---- 1. nu(u) = sum_{k>=0} exp(-(2k+1/2)u)  =  1/4 sinh + 1/4 cosh  (K/2) -------------
def nu_closed(u): return 0.25/math.sinh(u/2) + 0.25/math.cosh(u/2)
def nu_series(u, N=400): return sum(math.exp(-(2*k+0.5)*u) for k in range(N))
for u in (0.05, 0.3, 1.0, 2.5, 5.0):
    print(f"  nu({u}): closed={nu_closed(u):.18f} series={nu_series(u):.18f} diff={nu_closed(u)-nu_series(u):.3e}")

# ---- 2. phi(x) = Re psi(1/4+i sqrt(x)/2) - psi(1/4) = sum_k (1/a_k) x/(x+4a_k^2) ------
def phi_dg(x): return float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.sqrt(mp.mpf(x))/2)) - mp.digamma(mp.mpf(1)/4))
def phi_ser(x, N=200000):
    a = np.arange(N) + 0.25
    return float(np.sum(x/(a*(x+4*a*a))))
for x in (0.25, 4.0, 46.2, 1000.0):
    print(f"  phi({x}): digamma={phi_dg(x):.15f} series={phi_ser(x):.15f} diff={phi_dg(x)-phi_ser(x):.3e}")

# ---- 3. the bookkeeping identity  <A_T F,F> = E_Gamma + E_P + (C0 - 2 sum w_n)||F||^2 --
for T, contacts in ((0.5*math.log(3), [2]), (math.log(2), [2, 3])):
    B = core.Body(T, 140, contacts, constrained=True)
    w = {n: core.wgt(n) for n in contacts}
    lam, F = B.eig(1.0, {n: -2*w[n] for n in contacts}, 'min')
    sw = sum(w.values())
    print(f"T={T:.6f} contacts={contacts}: lambda_min={lam:.8e}  2*sum w_n={2*sw:.8f}"
          f"  target lambda^{{P_T}}(E_G+E_P) = 2sum w - C0 = {2*sw-C0:.8f}"
          f"  check: {lam - C0 + 2*sw:.8f}")
    # subordination upper bound (analytic):  lambda_min <= C0 - 2 sum w + phi((3pi/2T)^2) + 4 sum w
    mu3 = (3*math.pi/(2*T))**2
    ub = C0 - 2*sw + phi_dg(mu3) + 4*sw
    print(f"   mu_3=(3pi/2T)^2={mu3:.5f}  phi(mu_3)={phi_dg(mu3):.6f}  ||E_P||<=4 sum w={4*sw:.5f}"
          f"   ANALYTIC UPPER BOUND lambda_min <= {ub:.6f}   (certified value {lam:.3e})")
    # sharper: exact E_P on span of first 3 Dirichlet-form eigenfunctions of M0-C0, intersect P_T
    M0 = B.M0 - C0*B.G
    import scipy.linalg as sla
    wv, V = sla.eigh(M0, B.G)
    print(f"   killed-subordinate eigenvalues lambda_n(E_Gamma) (Galerkin): {wv[:5]}")
    print(f"   subordination bound phi((n pi/2T)^2):          "
          f"{[round(phi_dg((n*math.pi/(2*T))**2),6) for n in (1,2,3,4,5)]}")
    EP = B.G*0
    for n in contacts:
        EP = EP + 2*w[n]*(B.G - B.Mn[n])
    V3 = V[:, :3]
    A = V3.T @ (M0 + EP) @ V3; Gm = V3.T @ B.G @ V3
    v3 = sla.eigh(A, Gm)[0]
    print(f"   Rayleigh of E_Gamma+E_P on span(first 3 eigenfns): max={v3[-1]:.6f} -> "
          f"sharper upper bound lambda_min <= {C0 - 2*sw + v3[-1]:.6e}")
