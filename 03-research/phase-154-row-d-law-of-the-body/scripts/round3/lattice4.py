"""R154 round 3, D2: COMMENSURATE lattice certificate.

Lattice step d = log(2)/k, atoms u_j = j d with j0 = ceil(2T/d) <= j <= J,
so that BOTH nuhat(tau) = sum_j 2 a_j cos(j d tau) AND the prime term
-v_2 cos(tau log 2) are periodic with the common period P = 2 pi / d = 2 pi k / log 2.
(At T = log 2 the second contact log 3 is incommensurate and is bounded by -v_3.)

Write  f(tau) = m(tau) + Q(tau) + b0 g0h(tau) + b1 g1h(tau),
       Q(tau) = -sum_n v_n cos(tau log n) + nuhat(tau)   [periodic up to the log-3 term]
The LP maximises c subject to
  (i)   f >= c on a grid of [0, taumax];
  (ii)  Q >= -rho on a grid of ONE period (rho an LP variable);
  (iii) c <= m(taumax) - rho - k0|b0| - k1|b1|         (the tail row),
using that m is increasing and |g0h|,|g1h| = O(1/tau).
Everything is then re-verified rigorously by Lipschitz branch-and-bound.
"""
import math, numpy as np
from scipy.optimize import linprog
from cert3 import base, g0h, g1h, vdict, fval, m, verify, lip


def qfun(tau, T, us, a, v, per_only=True):
    """Q(tau) = -sum v_n cos(tau log n) + nuhat(tau); if per_only, only the
    commensurate (n = 2) prime term is included."""
    tau = np.asarray(tau, float)
    out = np.zeros(len(tau))
    for n, vn in v.items():
        if per_only and n != 2: continue
        out -= vn*np.cos(tau*math.log(n))
    for i in range(0, len(tau), 20000):
        sl = slice(i, i+20000)
        out[sl] = out[sl] + 2*(np.cos(np.outer(tau[sl], us)) @ np.asarray(a))
    return out


def solve(T, k=5, U=40.0, taumax=150.0, dtau=0.004, dper=0.002, capa=None,
          verbose=True):
    v = vdict(T); Sv = sum(v.values())
    d = math.log(2)/k
    j0 = int(math.ceil(2*T/d - 1e-12)); J = int((2*T+U)/d)
    js = np.arange(j0, J+1); us = js*d; n = len(js)
    P = 2*math.pi/d
    extra = sum(vn for nn, vn in v.items() if nn != 2)   # incommensurate rest
    tau = np.concatenate([np.arange(1e-7, min(60.0, taumax), dtau),
                          np.arange(min(60.0, taumax), taumax, max(dtau, 0.02))]) \
        if taumax > 60 else np.arange(1e-7, taumax, dtau)
    tp = np.arange(0.0, P, dper)
    nv = 1+n+5
    iA, iB0, iB1, iR, iT0, iT1 = 1, 1+n, 2+n, 3+n, 4+n, 5+n
    rows = []; rhs = []
    R1 = np.zeros((len(tau), nv)); R1[:, 0] = 1.0
    R1[:, iA:iA+n] = -2*np.cos(np.outer(tau, us))
    R1[:, iB0] = -g0h(tau, T); R1[:, iB1] = -g1h(tau, T)
    rows.append(R1); rhs.append(base(tau, v))
    # (ii)  -Q - rho <= 0  with Q built from the n=2 term only
    R2 = np.zeros((len(tp), nv))
    R2[:, iA:iA+n] = -2*np.cos(np.outer(tp, us)); R2[:, iR] = -1.0
    rows.append(R2); rhs.append(-v[2]*np.cos(tp*math.log(2)))
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    R3 = np.zeros((1, nv)); R3[0, 0] = 1; R3[0, iR] = 1; R3[0, iT0] = k0; R3[0, iT1] = k1
    rows.append(R3); rhs.append(np.array([m(np.array([taumax]))[0] - extra]))
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
    out = dict(T=T, k=k, d=d, us=us, a=x[iA:iA+n], b0=x[iB0], b1=x[iB1],
               rho=x[iR], lp=x[0], taumax=taumax, P=P, v=v, U=U, extra=extra)
    if verbose:
        print(f"T={T:.5f} k={k} d={d:.5f} P={P:.3f} nat={n} tmax={taumax}: "
              f"LP c={x[0]:.6e} rho={x[iR]:.4f} b0={x[iB0]:.4g} b1={x[iB1]:.4g} "
              f"|a|1={np.abs(x[iA:iA+n]).sum():.4f}", flush=True)
    return out


def certify(r, h=2e-6, w0=0.01, verbose=True):
    """Rigorous certified lower bound for inf_tau f."""
    T = r['T']; us = r['us']; a = r['a']; b0 = r['b0']; b1 = r['b1']
    v = r['v']; taumax = r['taumax']; P = r['P']; extra = r['extra']
    # (1) min of Q over one period, Lipschitz-certified
    LQ = 2*float(np.sum(np.abs(a)*us)) + v[2]*math.log(2)
    tg = np.arange(0.0, P, h)
    q = qfun(tg, T, us, a, v)
    rho = -(float(q.min()) - LQ*h/2)
    k0 = 2*math.cosh(T)/taumax + math.sinh(T)/taumax**2
    k1 = 8*T*math.sinh(T)/taumax
    tail = m(np.array([taumax]))[0] - extra - rho - abs(b0)*k0 - abs(b1)*k1
    # (2) branch and bound on [0, taumax]
    target = min(tail, r['lp']) - 1e-9
    ok, best, L, nk = verify(T, us, a, b0, b1, v, taumax, target=target, w0=w0)
    c = min(tail, best if ok else best)
    if verbose:
        print(f"   CERTIFY rho={rho:.5f} tail={tail:.6e} bb_ok={ok} bb_min={best:.6e} "
              f"L={L:.1f} nleft={nk} -> c >= {c:.6e}", flush=True)
    return dict(rho=rho, tail=tail, bb_ok=ok, bb_best=best, L=L, nleft=nk, c=c)


if __name__ == '__main__':
    T3 = 0.5*math.log(3)
    for k in (3, 4, 5, 6, 8):
        for tm in (100.0, 200.0):
            solve(T3, k=k, U=40.0, taumax=tm)
