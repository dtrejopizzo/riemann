"""R154 round 3, D2: LATTICE certificate.

Atoms are placed on the lattice u_j = j*d, d = 2T/M, j = M..J  (all u_j >= 2T),
so nuhat(tau) = sum_j 2 a_j cos(j d tau) is PERIODIC with period P = 2pi/d.
Hence its global minimum -rho is certified on ONE period, and the tail
tau >= taumax is bounded by

  f(tau) >= m(taumax) - sum_n v_n - rho - |b0|(2cosh T/tau + sinh T/tau^2)|_{taumax}
                                        - |b1| 8T sinh T / taumax          (*)

which replaces the lossy |nuhat| <= TV bound of round 2.  The LP maximises c
subject to (i) f >= c on a grid of [0,taumax], (ii) nuhat >= -rho on a grid of
one period, (iii) the linear tail row (*) >= c, with rho, |b0|, |b1| as LP
variables.  Grid -> rigorous by the Lipschitz branch-and-bound of cert3.verify.
"""
import math, numpy as np
from scipy.optimize import linprog
from cert3 import base, g0h, g1h, vdict, fval, m, G0, G1, verify, lip


def solve(T, M=4, J=None, U=30.0, taumax=120.0, dtau=0.004, dper=0.002,
          capa=None, verbose=True):
    v = vdict(T); Sv = sum(v.values())
    d = 2*T/M
    if J is None: J = int(round((2*T+U)/d))
    js = np.arange(M, J+1); us = js*d; n = len(js)
    P = 2*math.pi/d
    tau = np.concatenate([np.arange(1e-7, min(60.0,taumax), dtau),
                          np.arange(min(60.0,taumax), taumax, max(dtau,0.02))]) if taumax>60 else np.arange(1e-7, taumax, dtau)
    tp = np.arange(0.0, P, dper)
    nv = 1+n+5
    iA, iB0, iB1, iR, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n, 5+n
    rows = []; rhs = []
    Nt = len(tau)
    R1 = np.zeros((Nt, nv))
    R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -g0h(tau, T); R1[:, iB1] = -g1h(tau, T)
    rows.append(R1); rhs.append(base(tau, v))
    R2 = np.zeros((len(tp), nv))
    R2[:, iA:iA+n] = -2*np.cos(np.outer(tp, us)); R2[:, iR] = -1.0
    rows.append(R2); rhs.append(np.zeros(len(tp)))
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    R3 = np.zeros((1, nv)); R3[0, 0] = 1; R3[0, iR] = 1; R3[0, iT0] = k0; R3[0, iT1] = k1
    rows.append(R3); rhs.append(np.array([m(np.array([taumax]))[0]-Sv]))
    R4 = np.zeros((4, nv))
    R4[0, iB0] = 1; R4[0, iT0] = -1
    R4[1, iB0] = -1; R4[1, iT0] = -1
    R4[2, iB1] = 1; R4[2, iT1] = -1
    R4[3, iB1] = -1; R4[3, iT1] = -1
    rows.append(R4); rhs.append(np.zeros(4))
    Aub = np.vstack(rows); bub = np.concatenate(rhs)
    cvec = np.zeros(nv); cvec[0] = -1.0
    bnds = [(None, None)]*(1+n+2) + [(0, None)]*3
    if capa is not None:
        for i in range(iA, iA+n): bnds[i] = (-capa, capa)
    r = linprog(cvec, A_ub=Aub, b_ub=bub, bounds=bnds, method='highs')
    if not r.success:
        print("LP fail:", r.message); return None
    x = r.x
    out = dict(T=T, M=M, d=d, us=us, a=x[iA:iA+n], b0=x[iB0], b1=x[iB1],
               rho=x[iR], lp=x[0], taumax=taumax, P=P, v=v, U=U)
    if verbose:
        print(f"T={T:.5f} M={M} J={J} d={d:.4f} P={P:.3f} nat={n} tmax={taumax}: "
              f"LP c={x[0]:.6e} rho={x[iR]:.4f} b0={x[iB0]:.4g} b1={x[iB1]:.4g} "
              f"|a|1={np.abs(x[iA:iA+n]).sum():.4f}", flush=True)
    return out


def certify(r, h=1e-5, w0=0.01):
    """Rigorous certified value: min over one period of nuhat (Lipschitz),
    then the tail row, then Lipschitz branch-and-bound on [0,taumax]."""
    T = r['T']; us = r['us']; a = r['a']; b0 = r['b0']; b1 = r['b1']
    v = r['v']; taumax = r['taumax']; P = r['P']
    Ln = 2*float(np.sum(np.abs(a)*us))
    tg = np.arange(0.0, P, h)
    nh = np.empty(len(tg))
    for i in range(0, len(tg), 20000):
        sl = slice(i, i+20000); nh[sl] = 2*(np.cos(np.outer(tg[sl], us)) @ a)
    rho = -(float(nh.min()) - Ln*h/2)
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    tail = m(np.array([taumax]))[0] - sum(v.values()) - rho - abs(b0)*k0 - abs(b1)*k1
    target = min(tail, r['lp']) - 1e-9
    ok, best, L, nk = verify(T, us, a, b0, b1, v, taumax, target=target, w0=w0)
    return dict(rho=rho, tail=tail, bb_ok=ok, bb_best=best, L=L, nleft=nk,
                c=min(tail, best))


if __name__ == '__main__':
    T3 = 0.5*math.log(3)
    for M in (2, 4, 6, 8):
        for U in (20.0, 40.0):
            for tm in (60.0, 120.0):
                solve(T3, M=M, U=U, taumax=tm)
