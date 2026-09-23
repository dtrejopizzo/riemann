"""r5a_01: Birman-Schwinger count for (H1) (round 5a).

A_inf|P_T = (1/2pi) int m |Fhat|^2 on P_T (Paper 47 prop:arch).  m = m+ - m-,
m-(tau) = max(-m(tau),0) supported in |tau| < tau0 = 6.28983599, m- <= -C0 = 5.3721834.
Galerkin in the orthonormal Legendre basis of (-T,T);
  phihat_k(tau) = sqrt((2k+1)/(2T)) * 2T * (-i)^k j_k(tau T)   (spherical Bessel).
Reports: c(T) = C0 + Ktail(2T) (the proved shift constant) and its zero; tr(M-) in closed
form; gamma_T = lambda_min(M+) (Galerkin => UPPER bound on the truth, so the BS bound is
DIAGNOSTIC); the Birman-Schwinger trace tr(M+^{-1} M-); Prop NC's 68.5135*T for comparison.
"""
import sys, os, json, numpy as np
from scipy.special import spherical_jn
from scipy.optimize import brentq
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r3a'))
from arch_core import C0, Kdens, Ktail, gamma_matrix, pole_matrix, restrict

_U, _W = [], []
_edges = [0.0] + list(np.geomspace(1e-8, 80.0, 60))
for lo, hi in zip(_edges[:-1], _edges[1:]):
    xg, wg = np.polynomial.legendre.leggauss(40)
    _U.append(0.5*(hi-lo)*xg+0.5*(hi+lo)); _W.append(0.5*(hi-lo)*wg)
_U = np.concatenate(_U); _W = np.concatenate(_W)*Kdens(_U)

def m(tau):
    tau = np.atleast_1d(np.abs(np.asarray(tau, float)))
    v = C0 + (1.0-np.cos(np.outer(tau, _U))) @ _W
    return v if v.size > 1 else float(v[0])

tau0 = brentq(lambda x: m(x), 1.0, 20.0, xtol=1e-13)
xg, wg = np.polynomial.legendre.leggauss(400)
Im = float(-(m(0.5*tau0*xg+0.5*tau0)*(0.5*tau0*wg)).sum())
def cT(T): return C0 + Ktail(2*T)
Tc = brentq(cT, 0.002, 3.0, xtol=1e-13)
print("tau0 = %.8f   int_0^tau0(-m)dtau = %.6f   c(T)=0 at T = %.6f" % (tau0, Im, Tc), flush=True)

def MpMm(T, N, nq=800):
    Mp = np.zeros((N, N)); Mm = np.zeros((N, N))
    ph = np.array([[(-1.0)**((k-j)//2) if (k-j) % 2 == 0 else 0.0
                    for k in range(N)] for j in range(N)])
    for lo, hi in [(0.0, tau0), (tau0, 40.0), (40.0, 400.0), (400.0, 20000.0)]:
        xg, wg = np.polynomial.legendre.leggauss(nq)
        tau = 0.5*(hi-lo)*xg+0.5*(hi+lo); w = 0.5*(hi-lo)*wg
        mv = m(tau)
        J = np.column_stack([np.sqrt((2*k+1)/(2*T))*2*T*spherical_jn(k, tau*T) for k in range(N)])
        Mp += ph*((J*(w*np.maximum(mv, 0.0)/np.pi)[:, None]).T @ J)
        Mm += ph*((J*(w*np.maximum(-mv, 0.0)/np.pi)[:, None]).T @ J)
    return Mp, Mm

rows = []
for T in [0.5*np.log(3), float(np.log(2))]:
    N = 18
    Mp, Mm = MpMm(T, N)
    G = gamma_matrix(T, N, nu=200); Pl, a, b = pole_matrix(T, N)
    err = float(np.linalg.norm((Mp-Mm)-G)/np.linalg.norm(G))
    gam = float(np.linalg.eigvalsh(Mp)[0])
    bs = float(np.trace(np.linalg.solve(Mp, Mm)))
    r = dict(T=float(T), c_T=float(cT(T)), rel_err_vs_kernel_Galerkin=err, gamma_T=gam,
             trMm_closed=float((2*T/np.pi)*Im), trMm_galerkin=float(np.trace(Mm)),
             bs_trace=bs, crude_trMm_over_gamma=float((2*T/np.pi)*Im/gam),
             prop_NC=float(68.5135*T),
             nneg_L2=int((np.linalg.eigvalsh(G) < 0).sum()),
             nneg_PT=int((np.linalg.eigvalsh(restrict(G, a, b)) < 0).sum()))
    rows.append(r)
    print("T=%.5f c=%+.4f relerr=%.2e gamma_T=%.4f tr(M-)=%.4f BS=%.3f crude=%.2f "
          "PropNC=%.1f n-(L2)=%d n-(P_T)=%d"
          % (T, r['c_T'], err, gam, r['trMm_closed'], bs, r['crude_trMm_over_gamma'],
             r['prop_NC'], r['nneg_L2'], r['nneg_PT']), flush=True)
json.dump(dict(tau0=tau0, Im=Im, Tc=Tc, rows=rows), open(os.path.join(HERE, 'r5a_01.json'), 'w'), indent=1)
