"""R154 round 2: R2 decisive test. Direct LP on a dense tau-grid + fine-grid verification
+ explicit O(1/tau) tail bound.  Density certificate (see dual2.py docstring)."""
import math, numpy as np
from scipy.special import psi as dg
from scipy.optimize import linprog
from dual2 import base, h0, h1

def run(T, contacts, U, du, cap, two, dtau=0.01, taumax=120.0, ref=25):
    L = 2*T; v = {n: 2*math.log(n)/math.sqrt(n) for n in contacts}
    edges = np.arange(L, L+U+1e-12, du); nc = len(edges)-1
    def cols(t):
        C = 2*(np.sin(np.outer(t, edges[1:])) - np.sin(np.outer(t, edges[:-1])))/t[:, None]
        out = [C, h0(t, T)[:, None]]
        if two: out.append(h1(t, T)[:, None])
        return np.hstack(out)
    tau = np.arange(1e-6, taumax, dtau)
    M = cols(tau); nv = M.shape[1]
    A = np.hstack([np.ones((len(tau), 1)), -M]); c = np.zeros(nv+1); c[0] = -1
    bnds = [(None, None)] + [(-cap, cap)]*nc + [(None, None)]*(nv-nc)
    r = linprog(c, A_ub=A, b_ub=base(tau, contacts, v), bounds=bnds, method='highs')
    x = r.x; lp = x[0]; cc = x[1:1+nc]; bs = x[1+nc:]
    coef = np.concatenate([cc, bs]); best = 1e9; arg = 0.
    for k in range(ref):
        tf = np.arange(k*taumax/ref+1e-9, (k+1)*taumax/ref, dtau/50)
        val = base(tf, contacts, v) + cols(tf) @ coef
        if val.min() < best: best = val.min(); arg = tf[val.argmin()]
    TV = np.abs(np.diff(cc)).sum() + abs(cc[0]) + abs(cc[-1])
    tail = (np.real(dg(0.25+0.5j*taumax)) - math.log(math.pi) - sum(v.values())
            - 2*TV/taumax - abs(bs[0])*(2*math.cosh(T)/taumax + math.sinh(T)/taumax**2)
            - (abs(bs[-1])*8*T*math.sinh(T)/taumax if two else 0.))
    print(f"T={T:.5f} {contacts} U={U} du={du} cap={cap} two={two}: LP={lp:.6e} "
          f"fine={best:.6e}@tau={arg:.3f} tail>={tail:.4f} TV={TV:.4g} b0={bs[0]:.4g} "
          f"b1={bs[-1] if two else 0:.4g} |c|inf={np.abs(cc).max():.4g}", flush=True)

if __name__ == '__main__':
    T3 = 0.5*math.log(3)
    for two in (False, True):
        run(T3, [2], 14., .05, 5., two)
    for U, du, cap in ((25., .05, 20.), (25., .02, 50.), (40., .02, 100.)):
        run(T3, [2], U, du, cap, True)
    run(math.log(2), [2,3], 25., .05, 20., True)
    run(math.log(2), [2,3], 40., .02, 100., True)
