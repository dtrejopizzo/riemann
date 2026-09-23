"""R154 round 3, D2: atomic outside-window LP with an explicit L1 cap (so the
tail bound is rigorous at a moderate taumax), by cutting planes on tau."""
import math, numpy as np, sys
from scipy.optimize import linprog
from cert3 import base, g0h, g1h, vdict, fval, tailbound, verify, lip

def solve(T, U=25.0, du=0.05, A=3.0, taumax=400.0, dtau=0.01, dfine=0.0005,
          rounds=12, verbose=True, us=None):
    v = vdict(T); L2T = 2*T
    if us is None: us = np.arange(L2T, L2T+U+1e-12, du)
    nA = len(us)
    def cols(t):
        return np.hstack([2*np.cos(np.outer(t,us)), -2*np.cos(np.outer(t,us)),
                          g0h(t,T)[:,None], g1h(t,T)[:,None]])
    nv = 2*nA+2
    act = np.arange(1e-6, taumax, dtau)
    tf = np.arange(1e-7, taumax, dfine)
    bf = base(tf, v)
    cvec = np.zeros(1+nv); cvec[0] = -1.0
    bnds = [(None,None)] + [(0,A)]*(2*nA) + [(None,None)]*2
    # L1 row: sum(p+q) <= A
    l1 = np.zeros(1+nv); l1[1:1+2*nA] = 1.0
    for it in range(rounds):
        M = cols(act)
        Aub = np.hstack([np.ones((len(act),1)), -M])
        Aub = np.vstack([Aub, l1]); bub = np.concatenate([base(act,v), [A]])
        r = linprog(cvec, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
        if not r.success: print("LP fail", r.message); return None
        x = r.x; lp = x[0]; a = x[1:1+nA]-x[1+nA:1+2*nA]; b0,b1 = x[1+2*nA], x[2+2*nA]
        # fine evaluation
        val = np.empty(len(tf))
        for i in range(0,len(tf),400000):
            sl=slice(i,i+400000); val[sl] = bf[sl] + fval(tf[sl],T,us,a,b0,b1,v) - bf[sl] + bf[sl]
        val = fval(tf,T,us,a,b0,b1,v)
        mn = val.min(); arg = tf[val.argmin()]
        viol = np.where(val < lp - 1e-12)[0]
        if verbose: print(f"  it{it} LP={lp:.6e} fine={mn:.6e}@{arg:.4f} nviol={len(viol)} rows={len(act)} |a|1={np.abs(a).sum():.3f} b0={b0:.4g} b1={b1:.4g}",flush=True)
        if len(viol)==0: break
        srt = viol[np.argsort(val[viol])][:1500]
        act = np.unique(np.concatenate([act, tf[srt]]))
    tb = tailbound(T,us,a,b0,b1,v,taumax)
    return dict(lp=lp, fine=mn, a=a, us=us, b0=b0, b1=b1, tail=tb, v=v, T=T, taumax=taumax)

if __name__ == '__main__':
    T3 = 0.5*math.log(3)
    for A in (2.0, 3.0, 4.0):
        for U in (14.0, 25.0):
            print(f"== T=1/2log3 A={A} U={U}")
            r = solve(T3, U=U, du=0.05, A=A, taumax=400.0, dtau=0.02, dfine=0.001, rounds=8)
            if r: print(f"   RESULT lp={r['lp']:.6e} fine={r['fine']:.6e} tail={r['tail']:.4f} |a|1={np.abs(r['a']).sum():.4f}",flush=True)
