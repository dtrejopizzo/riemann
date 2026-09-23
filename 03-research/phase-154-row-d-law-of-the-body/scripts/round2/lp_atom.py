"""R154 round 2: R2 with ATOMIC nu (round 1's class) + the second multiplier h1.
Directly comparable with R154_001 section 6 and with chk6.py of the audit."""
import math, numpy as np
from scipy.special import psi as dg
from scipy.optimize import linprog
from dual2 import base, h0, h1

def run(T, contacts, U, du, cap, two, dtau=0.01, taumax=80.0, ref=20):
    L = 2*T; v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    us = np.arange(L, L+U+1e-12, du); nu_ = len(us)
    def cols(t):
        out = [2*np.cos(np.outer(t, us)), h0(t, T)[:, None]]
        if two: out.append(h1(t, T)[:, None])
        return np.hstack(out)
    tau = np.arange(1e-6, taumax, dtau)
    M = cols(tau); nv = M.shape[1]
    A = np.hstack([np.ones((len(tau), 1)), -M]); c = np.zeros(nv+1); c[0] = -1
    bnds = [(None, None)] + [(-cap, cap)]*nu_ + [(None, None)]*(nv-nu_)
    r = linprog(c, A_ub=A, b_ub=base(tau, contacts, v), bounds=bnds, method='highs')
    x = r.x; lp = x[0]; cc = x[1:1+nu_]; bs = x[1+nu_:]
    coef = np.concatenate([cc, bs]); best = 1e9; arg = 0.
    for k in range(ref):
        tf = np.arange(k*taumax/ref+1e-9, (k+1)*taumax/ref, dtau/50)
        val = base(tf, contacts, v) + cols(tf) @ coef
        if val.min() < best: best = val.min(); arg = tf[val.argmin()]
    print(f"T={T:.5f} {contacts} U={U} du={du} cap={cap} two={two}: LP={lp:.6e} fine={best:.6e}@tau={arg:.3f}"
          f" |c|1={np.abs(cc).sum():.4g} b0={bs[0]:.4g} b1={bs[-1] if two else 0:.4g}", flush=True)

if __name__ == '__main__':
    T3 = 0.5*math.log(3)
    for two in (False, True):
        for U, cap in ((6., 3.), (14., 3.), (25., 3.), (25., 30.)):
            run(T3, [2], U, .05, cap, two)
    for two in (False, True):
        run(math.log(2), [2, 3], 25., .05, 3., two)
