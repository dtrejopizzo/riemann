"""R154 round 3, D2 (fast variant): lattice certificate with a resonance-enriched
initial tau grid.  The dips of f are at rational multiples of the period
P = 2pi/d (where the lattice phases align), so those windows are put in the grid
from the start instead of being discovered by cutting planes.
"""
import math, pickle, sys, numpy as np
from scipy.optimize import linprog
from cert3 import base, g0h, g1h, vdict, fval, m, verify, lip
from close3 import lp, certify


def resonance_grid(P, taumax, qmax=12, half=0.012, step=6e-4):
    pts = [np.array([0.0])]
    for q in range(1, qmax+1):
        for p in range(1, q*int(taumax/P)+q+1):
            c = p*P/q
            if c > taumax: break
            pts.append(np.arange(max(0, c-half), min(taumax, c+half), step))
    return np.unique(np.concatenate(pts))


def run(T, M=16, U=20.0, taumax=200.0, dtau_lo=0.008, dtau_hi=0.008, dper=0.02,
        cuts=8, dfine=5e-5, tag='', qmax=12):
    v = vdict(T)
    d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    tau = np.concatenate([np.arange(1e-7, min(60.0, taumax), dtau_lo),
                          np.arange(min(60.0, taumax), taumax, dtau_hi),
                          resonance_grid(P, taumax, qmax)])
    tau = np.unique(tau)
    tp = np.unique(np.concatenate([np.arange(0.0, P, dper),
                                   resonance_grid(P, P, qmax)]))
    tfine = np.arange(1e-8, taumax, dfine)
    tpf = np.arange(0.0, P, 2e-5)
    print(f"  [{tag}] rows tau={len(tau)} per={len(tp)} atoms={len(us)} P={P:.3f}", flush=True)
    sol = None
    for it in range(cuts):
        sol = lp(T, us, tau, tp, P, taumax, v)
        if sol is None: print("LP fail"); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        val = np.empty(len(tfine))
        for i in range(0, len(tfine), 2000000):
            sl = slice(i, i+2000000); val[sl] = fval(tfine[sl], T, us, a, b0, b1, v)
        mn = float(val.min()); arg = tfine[val.argmin()]
        nuf = np.empty(len(tpf))
        for i in range(0, len(tpf), 20000):
            sl = slice(i, i+20000); nuf[sl] = 2*(np.cos(np.outer(tpf[sl], us)) @ a)
        rho_true = -float(nuf.min())
        print(f"  [{tag}] it{it} LPc={sol['c']:.6e} fine={mn:.6e}@{arg:.5f} "
              f"rho_lp={sol['rho']:.4f} rho_true={rho_true:.4f} |a|1={np.abs(a).sum():.3f} "
              f"b0={b0:.6f} b1={b1:.6f}", flush=True)
        viol = np.where(val < sol['c'] - 1e-11)[0]
        nvp = np.where(nuf < -sol['rho'] - 1e-11)[0]
        if len(viol) == 0 and len(nvp) == 0:
            print("  converged", flush=True); break
        if len(viol):
            srt = viol[np.argsort(val[viol])][:6000]
            tau = np.unique(np.concatenate([tau, tfine[srt]]))
        if len(nvp):
            srt = nvp[np.argsort(nuf[nvp])][:3000]
            tp = np.unique(np.concatenate([tp, tpf[srt]]))
    return dict(T=T, M=M, d=d, us=us, a=sol['a'], b0=sol['b0'], b1=sol['b1'],
                rho_lp=sol['rho'], lp=sol['c'], taumax=taumax, P=P, v=v, U=U,
                fine=mn, rho_true=rho_true)


if __name__ == '__main__':
    M = int(sys.argv[1]); U = float(sys.argv[2])
    which = sys.argv[3] if len(sys.argv) > 3 else 'log3'
    T = 0.5*math.log(3) if which == 'log3' else math.log(2)
    tmax = float(sys.argv[4]) if len(sys.argv) > 4 else 200.0
    r = run(T, M=M, U=U, taumax=tmax, tag=f'{which}-M{M}U{U:g}t{tmax:g}')
    if r:
        pickle.dump(r, open(f'c4_{which}_M{M}_t{int(tmax)}.pkl', 'wb'))
        cc = certify(r, w0=0.005)
        r.update(cc); pickle.dump(r, open(f'c4_{which}_M{M}_t{int(tmax)}.pkl', 'wb'))
