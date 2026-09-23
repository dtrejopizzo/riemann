"""R154 round 3, D2: drive the lattice certificate to a RIGOROUSLY verified c > 0.

Lattice d = 2T/M, atoms u_j = j d, j = M..J (so u_M = 2T exactly).
nuhat(tau) = sum_j 2 a_j cos(u_j tau) is 2pi/d-periodic: its global minimum
is certified on ONE period by grid + Lipschitz, giving the tail bound
   f(tau) >= m(taumax) - sum_n v_n - rho - |b0| k0 - |b1| k1   (tau >= taumax).
Cutting planes on [0,taumax], then Lipschitz branch-and-bound.
"""
import math, pickle, sys, numpy as np
from scipy.optimize import linprog
from cert3 import base, g0h, g1h, vdict, fval, m, verify, lip


def build(T, M, U, taumax, dtau_lo, dtau_hi, dper):
    d = 2*T/M
    J = int((2*T+U)/d)
    us = np.arange(M, J+1)*d
    P = 2*math.pi/d
    tau = np.concatenate([np.arange(1e-7, min(60.0, taumax), dtau_lo),
                          np.arange(min(60.0, taumax), taumax, dtau_hi)])
    tp = np.arange(0.0, P, dper)
    return d, us, P, tau, tp


def lp(T, us, tau, tp, P, taumax, v, capa=None, rhomax=None):
    n = len(us); Sv = sum(v.values())
    nv = 1+n+5
    iA, iB0, iB1, iR, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n, 5+n
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -g0h(tau, T); R1[:, iB1] = -g1h(tau, T)
    R2 = np.zeros((len(tp), nv))
    R2[:, iA:iA+n] = -2*np.cos(np.outer(tp, us)); R2[:, iR] = -1.0
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    R3 = np.zeros((1, nv)); R3[0, 0] = 1; R3[0, iR] = 1; R3[0, iT0] = k0; R3[0, iT1] = k1
    R4 = np.zeros((4, nv))
    R4[0, iB0] = 1; R4[0, iT0] = -1
    R4[1, iB0] = -1; R4[1, iT0] = -1
    R4[2, iB1] = 1; R4[2, iT1] = -1
    R4[3, iB1] = -1; R4[3, iT1] = -1
    Aub = np.vstack([R1, R2, R3, R4])
    bub = np.concatenate([base(tau, v), np.zeros(len(tp)),
                          np.array([m(np.array([taumax]))[0]-Sv]), np.zeros(4)])
    cvec = np.zeros(nv); cvec[0] = -1.0
    bnds = [(None, None)]*(1+n+2) + [(0, None)]*3
    if rhomax is not None: bnds[iR] = (0, rhomax)
    if capa is not None:
        for i in range(iA, iA+n): bnds[i] = (-capa, capa)
    r = linprog(cvec, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    if not r.success: return None
    x = r.x
    return dict(c=x[0], a=x[iA:iA+n], b0=x[iB0], b1=x[iB1], rho=x[iR])


def run(T, M=16, U=40.0, taumax=200.0, dtau_lo=0.005, dtau_hi=0.02, dper=0.02,
        cuts=6, dfine=2e-4, tag=''):
    v = vdict(T)
    d, us, P, tau, tp = build(T, M, U, taumax, dtau_lo, dtau_hi, dper)
    tfine = np.arange(1e-8, taumax, dfine)
    tpf = np.arange(0.0, P, 1e-4)
    sol = None
    for it in range(cuts):
        sol = lp(T, us, tau, tp, P, taumax, v)
        if sol is None: print("LP fail"); return None
        a, b0, b1 = sol['a'], sol['b0'], sol['b1']
        val = fval(tfine, T, us, a, b0, b1, v)
        mn = float(val.min()); arg = tfine[val.argmin()]
        nuf = np.empty(len(tpf))
        for i in range(0, len(tpf), 20000):
            sl = slice(i, i+20000); nuf[sl] = 2*(np.cos(np.outer(tpf[sl], us)) @ a)
        rho_true = -float(nuf.min())
        print(f"  [{tag}] it{it} M={M} nat={len(us)} LPc={sol['c']:.6e} fine={mn:.6e}@{arg:.4f} "
              f"rho_lp={sol['rho']:.4f} rho_true={rho_true:.4f} |a|1={np.abs(a).sum():.3f} "
              f"b0={b0:.4g} b1={b1:.4g}", flush=True)
        viol = np.where(val < sol['c'] - 1e-11)[0]
        nvp = np.where(nuf < -sol['rho'] - 1e-11)[0]
        if len(viol) == 0 and len(nvp) == 0: break
        if len(viol):
            srt = viol[np.argsort(val[viol])][:4000]
            tau = np.unique(np.concatenate([tau, tfine[srt]]))
        if len(nvp):
            srt = nvp[np.argsort(nuf[nvp])][:2000]
            tp = np.unique(np.concatenate([tp, tpf[srt]]))
    out = dict(T=T, M=M, d=d, us=us, a=sol['a'], b0=sol['b0'], b1=sol['b1'],
               rho_lp=sol['rho'], lp=sol['c'], taumax=taumax, P=P, v=v, U=U,
               fine=mn, rho_true=rho_true)
    return out


def certify(r, hper=2e-6, w0=0.005, verbose=True):
    T = r['T']; us = r['us']; a = r['a']; b0 = r['b0']; b1 = r['b1']
    v = r['v']; taumax = r['taumax']; P = r['P']
    Ln = 2*float(np.sum(np.abs(a)*us))
    tg = np.arange(0.0, P, hper)
    nh = np.empty(len(tg))
    for i in range(0, len(tg), 20000):
        sl = slice(i, i+20000); nh[sl] = 2*(np.cos(np.outer(tg[sl], us)) @ a)
    rho = -(float(nh.min()) - Ln*hper/2)          # certified nuhat >= -rho
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    tail = m(np.array([taumax]))[0] - sum(v.values()) - rho - abs(b0)*k0 - abs(b1)*k1
    L = lip(T, us, a, b0, b1, v)
    target = min(tail, r['fine']) - 1e-7
    ok, best, L2, nk = verify(T, us, a, b0, b1, v, taumax, target=target, w0=w0)
    c = min(tail, best if ok else -np.inf)
    if verbose:
        print(f"  CERTIFY rho={rho:.6f} tail={tail:.6e} Lip={L:.1f} bb_ok={ok} "
              f"bb_target={target:.6e} bb_min_grid={best:.6e} nleft={nk} => c >= {c:.6e}", flush=True)
    return dict(rho=rho, tail=tail, L=L, ok=ok, best=best, c=c, target=target)


if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    U = float(sys.argv[2]) if len(sys.argv) > 2 else 40.0
    which = sys.argv[3] if len(sys.argv) > 3 else 'log3'
    T = 0.5*math.log(3) if which == 'log3' else math.log(2)
    r = run(T, M=M, U=U, taumax=200.0, tag=f'{which}-M{M}')
    if r:
        cc = certify(r)
        r.update(cc)
        pickle.dump(r, open(f'cert_{which}_M{M}.pkl', 'wb'))
