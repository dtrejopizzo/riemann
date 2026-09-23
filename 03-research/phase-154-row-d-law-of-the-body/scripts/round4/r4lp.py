"""R154 round 4: cutting-plane LP for the lattice outside-window certificate.

Variables: c, a_1..a_n, b0, b1, rho, t0(=|b0|), t1(=|b1|).
Maximise c subject to
   (R1)  c <= sigma_T(tau) + nuhat(tau) + b0 g0h + b1 g1h     for tau in grid of [0,taumax]
   (R2)  nuhat(tau') >= -rho                                   for tau' in grid of one period
   (R3)  c + rho + k0 t0 + k1 t1 <= m(taumax) - sum v          (periodic tail lemma)
   (R4)  t0 >= |b0|, t1 >= |b1|
Rows R1, R2 are refined by cutting planes against fine grids.
"""
import math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog
import r4core as C


def resonance_grid(P, xmax, qmax=12, half=0.012, step=6e-4):
    pts = [np.array([0.0])]
    for q in range(1, qmax+1):
        p = 1
        while True:
            ctr = p*P/q
            if ctr > xmax: break
            pts.append(np.arange(max(0.0, ctr-half), min(xmax, ctr+half), step))
            p += 1
    return np.unique(np.concatenate(pts))


def solve(T, us, tau, tp, taumax, v, rhomax=None, capa=None):
    n = len(us); Sv = sum(v.values())
    nv = 1 + n + 5
    iA, iB0, iB1, iR, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n, 5+n
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -C.g0h(tau, T); R1[:, iB1] = -C.g1h(tau, T)
    R2 = np.zeros((len(tp), nv))
    R2[:, iA:iA+n] = -2*np.cos(np.outer(tp, us)); R2[:, iR] = -1.0
    k0, k1 = C.tail_k(T, taumax)
    R3 = np.zeros((1, nv)); R3[0, 0] = 1; R3[0, iR] = 1; R3[0, iT0] = k0; R3[0, iT1] = k1
    R4 = np.zeros((4, nv))
    R4[0, iB0] = 1; R4[0, iT0] = -1
    R4[1, iB0] = -1; R4[1, iT0] = -1
    R4[2, iB1] = 1; R4[2, iT1] = -1
    R4[3, iB1] = -1; R4[3, iT1] = -1
    Aub = np.vstack([R1, R2, R3, R4])
    bub = np.concatenate([C.base(tau, v), np.zeros(len(tp)),
                          np.array([float(C.m(np.array([taumax]))[0]) - Sv]), np.zeros(4)])
    cvec = np.zeros(nv); cvec[0] = -1.0
    bnds = [(None, None)]*(1+n+2) + [(0, None)]*3
    if rhomax is not None: bnds[iR] = (0, rhomax)
    if capa is not None:
        for i in range(iA, iA+n): bnds[i] = (-capa, capa)
    r = linprog(cvec, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    if not r.success: return None
    x = r.x
    return dict(c=float(x[0]), a=x[iA:iA+n], b0=float(x[iB0]), b1=float(x[iB1]),
                rho=float(x[iR]), nrows=Aub.shape[0])


def run(T, M=16, U=20.0, taumax=100.0, dlo=0.004, dhi=0.01, tsplit=30.0,
        dper=0.02, qmax=12, cuts=8, hf=5e-5, hp=2e-5, rhomax=None, capa=None, tag=''):
    v = C.vdict(T)
    d = 2*T/M; J = int((2*T+U)/d); us = np.arange(M, J+1)*d; P = 2*math.pi/d
    tau = np.unique(np.concatenate([
        np.arange(1e-7, min(tsplit, taumax), dlo),
        np.arange(min(tsplit, taumax), taumax, dhi),
        resonance_grid(P, taumax, qmax)]))
    tp = np.unique(np.concatenate([np.arange(0.0, P, dper), resonance_grid(P, P, qmax)]))
    tfine = np.arange(1e-8, taumax, hf)
    tpf = np.arange(0.0, P, hp)
    print(f"[{tag}] M={M} U={U} taumax={taumax} atoms={len(us)} P={P:.3f} "
          f"rows tau={len(tau)} per={len(tp)}", flush=True)
    sol = None; mn = None
    for it in range(cuts):
        t0 = time.time()
        sol = solve(T, us, tau, tp, taumax, v, rhomax=rhomax, capa=capa)
        if sol is None:
            print(f"[{tag}] LP infeasible", flush=True); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        val = np.empty(len(tfine))
        for i in range(0, len(tfine), 2_000_000):
            sl = slice(i, i+2_000_000); val[sl] = C.fval(tfine[sl], T, us, a, b0, b1, v)
        mn = float(val.min()); arg = float(tfine[val.argmin()])
        nuf = C.nuhat(tpf, us, a)
        rho_true = -float(nuf.min())
        print(f"[{tag}] it{it} rows={sol['nrows']} LPc={sol['c']:.6e} fine={mn:.6e}@{arg:.5f} "
              f"rho_lp={sol['rho']:.4f} rho_true={rho_true:.4f} |a|1={np.abs(a).sum():.3f} "
              f"b0={b0:.6f} b1={b1:.6f} ({time.time()-t0:.0f}s)", flush=True)
        viol = np.where(val < sol['c'] - 1e-11)[0]
        nvp = np.where(nuf < -sol['rho'] - 1e-11)[0]
        if len(viol) == 0 and len(nvp) == 0:
            print(f"[{tag}] converged", flush=True); break
        if len(viol):
            tau = np.unique(np.concatenate([tau, tfine[viol[np.argsort(val[viol])][:6000]]]))
        if len(nvp):
            tp = np.unique(np.concatenate([tp, tpf[nvp[np.argsort(nuf[nvp])][:3000]]]))
    return dict(T=T, M=M, U=U, d=d, us=us, a=sol['a'], b0=sol['b0'], b1=sol['b1'],
                rho_lp=sol['rho'], lp=sol['c'], taumax=taumax, P=P, v=v,
                fine=mn, rho_true=rho_true, tag=tag)


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--M', type=int, default=16)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--taumax', type=float, default=100.0)
    ap.add_argument('--dlo', type=float, default=0.004)
    ap.add_argument('--dhi', type=float, default=0.01)
    ap.add_argument('--cuts', type=int, default=8)
    ap.add_argument('--qmax', type=int, default=12)
    ap.add_argument('--rhomax', type=float, default=None)
    ap.add_argument('--out', type=str, default=None)
    ap.add_argument('--T', type=str, default='log3')
    A = ap.parse_args()
    T = 0.5*math.log(3) if A.T == 'log3' else math.log(2)
    tag = A.out or f"M{A.M}U{A.U:g}t{A.taumax:g}"
    r = run(T, M=A.M, U=A.U, taumax=A.taumax, dlo=A.dlo, dhi=A.dhi, cuts=A.cuts,
            qmax=A.qmax, rhomax=A.rhomax, tag=tag)
    if r: pickle.dump(r, open(f"lp_{tag}.pkl", 'wb'))
