"""R154 script 2: the outside-window dual certificate (Theorem B').

  lambda_min(A_T(v)) >= inf_tau [ sigma_v(tau) + sum_j c_j cos(u_j tau) + beta*h_T(tau) ]
with u_j >= 2T (the autocorrelation vanishes there) and
h_T(tau) = 2(.5 sinh T cos(2T tau) + tau cosh T sin(2T tau))/(tau^2+1/4)
the transform of cosh(t/2) 1_{|t|<2T} (the Paper-42 moment constraint).

LP over (c_j, beta, lambda) on a tau-grid, with the optimum re-evaluated on a 20x finer
grid (the honest value).  This reproduces the table of R154_001 section 6.
DIAGNOSTIC-NUMERIC: the LP value is grid-dependent; the certificate itself is finite and
the bound is PROVED once the 1-D inequality is verified for all tau.
"""
import math, numpy as np
from scipy.special import psi as digamma
from scipy.optimize import linprog


def sym(tau, contacts, v):
    s = np.real(digamma(0.25 + 0.5j*tau)) - math.log(math.pi)
    for n in contacts:
        s = s - v[n]*np.cos(tau*math.log(n))
    return s


def run(T, contacts, du=0.05, umax_extra=14.0, dtau=0.01, taumax=80.0, bnd=3.0):
    L = 2*T
    v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    tau = np.arange(1e-9, taumax, dtau)
    sig = sym(tau, contacts, v)
    us = np.arange(L, L + umax_extra, du)
    h = lambda t: 2*(0.5*math.sinh(T)*np.cos(L*t) + t*math.cosh(T)*np.sin(L*t))/(t**2 + 0.25)
    M = np.hstack([np.cos(np.outer(tau, us)), h(tau)[:, None]])
    Aub = np.hstack([-M, np.ones((len(tau), 1))])
    cobj = np.zeros(M.shape[1] + 1); cobj[-1] = -1.0
    bnds = [(-bnd, bnd)]*len(us) + [(None, None), (None, None)]
    r = linprog(cobj, A_ub=Aub, b_ub=sig, bounds=bnds, method='highs')
    x, lam = r.x[:-1], r.x[-1]
    tf = np.arange(1e-9, taumax, dtau/20.)
    val = sym(tf, contacts, v) + np.cos(np.outer(tf, us)) @ x[:-1] + x[-1]*h(tf)
    print(f"T={T:.5f} n={contacts} ue={umax_extra} bnd={bnd}: LP lam={lam:.5e}  "
          f"fine-grid inf={val.min():.5e} at tau={tf[val.argmin()]:.3f}  "
          f"|c|_1={abs(x[:-1]).sum():.1f} beta={x[-1]:.3f}", flush=True)
    return lam, val.min(), x


if __name__ == '__main__':
    for ue in (6.0, 14.0):
        for bnd in (0.3, 3.0):
            run(0.5*math.log(3), [2], umax_extra=ue, bnd=bnd)
    run(math.log(2), [2, 3], umax_extra=14.0, bnd=3.0)
