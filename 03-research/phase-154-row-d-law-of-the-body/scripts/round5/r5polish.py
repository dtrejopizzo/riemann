"""R154 round 5 -- (F2) block polish with row scaling + high-precision active-set re-solve.

Stage 1 (float): with the atom SHAPE a fixed, the only variables are
    x = (c, lam_1..lam_G, b0, b1, t0, t1),      a_j -> lam_{g(j)} a_j,
so the programme can be re-solved on a grid 100-1000x finer.  All rows are multiplied by
S (default 1e4): HiGHS' feasibility tolerance is ABSOLUTE, so scaling by S divides the
effective tolerance on c by S -- this is what lets the LP see values of size 1e-7.

Stage 2 (F2, exact): at the optimum take the rows with non-zero dual multiplier (the active
set).  If they number exactly nv = G+5, solve that square system A_act x = b_act in mpmath
at 50 digits.  The result is the exact vertex, free of HiGHS' tolerance; it is then checked
against every LP row and re-evaluated on the fine grid.
"""
import argparse, math, pickle, time
import numpy as np
from scipy.optimize import linprog
import r5core as C


def blockmat(tau, us, a, G):
    n = len(us); idx = np.array_split(np.arange(n), G)
    out = np.empty((len(tau), G))
    for g, ii in enumerate(idx):
        out[:, g] = C.nuhat(tau, us[ii], a[ii])
    return out


def build_rows(T, us, a, v, tau, xs, P, N, G):
    Sv = sum(v.values()); nv = 5 + G
    rows = []; rhs = []
    nu_t = blockmat(tau, us, a, G)
    R = np.zeros((len(tau), nv)); R[:, 0] = 1.0
    R[:, 1:1+G] = -nu_t; R[:, 1+G] = -C.g0h(tau, T); R[:, 2+G] = -C.g1h(tau, T)
    rows.append(R); rhs.append(C.base(tau, v))
    nu_x = blockmat(xs, us, a, G)
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = C.kk(T, tk)
        b = (C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
             if k < N else C.m(tk) - Sv)
        R = np.zeros((len(xs), nv)); R[:, 0] = 1.0
        R[:, 1:1+G] = -nu_x; R[:, 3+G] = k0; R[:, 4+G] = k1
        rows.append(R); rhs.append(b)
    R4 = np.zeros((4, nv))
    R4[0, 1+G] = 1; R4[0, 3+G] = -1
    R4[1, 1+G] = -1; R4[1, 3+G] = -1
    R4[2, 2+G] = 1; R4[2, 4+G] = -1
    R4[3, 2+G] = -1; R4[3, 4+G] = -1
    rows.append(R4); rhs.append(np.zeros(4))
    return np.vstack(rows), np.concatenate(rhs)


def scaled(us, a, lam, G):
    idx = np.array_split(np.arange(len(us)), G)
    a2 = a.copy()
    for g, ii in enumerate(idx): a2[ii] = a[ii]*lam[g]
    return a2


def vals(T, us, a2, v, b0, b1, tau, xs, P, N):
    fv = (C.base(tau, v) + C.nuhat(tau, us, a2) + b0*C.g0h(tau, T) + b1*C.g1h(tau, T))
    nu_x = C.nuhat(xs, us, a2); hs = []
    for k in range(N+1):
        tk = xs + k*P
        k0, k1 = C.kk(T, tk)
        b = (C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
             if k < N else C.m(tk) - sum(v.values()))
        hs.append(nu_x + b - abs(b0)*k0 - abs(b1)*k1)
    return fv, hs


def hp_resolve(Aub, bub, res, nv, dps=50):
    """(F2) exact vertex from the active set, in mpmath."""
    from mpmath import mp, matrix, lu_solve
    mp.dps = dps
    mu = np.asarray(res.ineqlin.marginals)
    act = np.where(np.abs(mu) > 1e-14)[0]
    # variables sitting at a bound are active constraints too (t0, t1 >= 0)
    bnd = []
    for nm, val in (('lower', 0.0),):
        mm = getattr(res, nm, None)
        if mm is not None:
            for i, g in enumerate(np.asarray(mm.marginals)):
                if abs(g) > 1e-14: bnd.append((i, val))
    info = dict(n_active=int(len(act)), n_bound_active=int(len(bnd)), nv=int(nv))
    if len(act) + len(bnd) != nv:
        info['status'] = (f'active set {len(act)}+{len(bnd)} != nv {nv} (degenerate); skipped')
        return None, info
    A = matrix(nv, nv); b = matrix(nv, 1)
    for i, r in enumerate(act):
        for j in range(nv):
            A[i, j] = mp.mpf(float(Aub[r, j]))
        b[i] = mp.mpf(float(bub[r]))
    for i, (col, val) in enumerate(bnd):
        r = len(act) + i
        for j in range(nv):
            A[r, j] = mp.mpf(1) if j == col else mp.mpf(0)
        b[r] = mp.mpf(val)
    try:
        x = lu_solve(A, b)
    except Exception as e:
        info['status'] = f'singular active system: {e}'
        return None, info
    xf = np.array([float(x[i]) for i in range(nv)])
    resid = Aub @ xf - bub
    info['status'] = 'ok'
    info['max_violation'] = float(resid.max())
    info['c_float_lp'] = float(res.x[0])
    info['c_exact'] = float(x[0])
    info['delta_c'] = float(x[0]) - float(res.x[0])
    info['c_exact_str'] = mp.nstr(x[0], 25)
    return xf, info


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl')
    ap.add_argument('--h0', type=float, default=1e-3)
    ap.add_argument('--hf', type=float, default=5e-6)
    ap.add_argument('--rounds', type=int, default=3)
    ap.add_argument('--ncut', type=int, default=120000)
    ap.add_argument('--G', type=int, default=128)
    ap.add_argument('--scale', type=float, default=1e4)
    ap.add_argument('--hp', action='store_true', help='(F2) exact active-set re-solve')
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb'))
    T, v = float(r['T']), r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    tag = A.out or (r.get('tag', 'c') + 'p')
    tau = np.arange(1e-7, tau1, A.h0); xs = tau1 + np.arange(0.0, P, A.h0)
    tf = np.arange(1e-8, tau1, A.hf); xf = tau1 + np.arange(0.0, P, A.hf)
    G = A.G
    print(f"[{tag}] T={T:.6f} tau1={tau1} P={P:.4f} N={N} atoms={len(a)} G={G} "
          f"scale={A.scale:g} fine {len(tf)}+{len(xf)}", flush=True)
    for it in range(A.rounds):
        t0 = time.time()
        Aub, bub = build_rows(T, us, a, v, tau, xs, P, N, G)
        S = A.scale
        cv = np.zeros(5+G); cv[0] = -1.0
        bnds = [(None, None)]*(3+G) + [(0, None)]*2
        res = linprog(cv, A_ub=Aub*S, b_ub=bub*S, bounds=bnds, method='highs')
        if not res.success:
            print("LP fail", res.message); return
        x = res.x.copy(); hpinfo = None
        if A.hp:
            xh, hpinfo = hp_resolve(Aub*S, bub*S, res, 5+G)
            print(f"[{tag}] (F2) {hpinfo}", flush=True)
            if xh is not None and hpinfo['max_violation'] <= 1e-9:
                x = xh
        c = x[0]; lam = x[1:1+G]; b0 = x[1+G]; b1 = x[2+G]
        a2 = scaled(us, a, lam, G)
        fv, hs = vals(T, us, a2, v, b0, b1, tf, xf, P, N)
        mf = float(fv.min()); mh = [float(h.min()) for h in hs]
        print(f"[{tag}] it{it} rows={Aub.shape[0]} LPc={c:.10e} b0={b0:.6f} b1={b1:.6f} "
              f"fmin={mf:.8e} hmin={min(mh):.8e} hk={np.array2string(np.array(mh),precision=5)} "
              f"({time.time()-t0:.0f}s)", flush=True)
        out = dict(r, a=a2, b0=float(b0), b1=float(b1), lp=float(c), tag=tag,
                   polished_from=A.pkl, lam=[float(t) for t in lam], it=it, G=G,
                   hp=hpinfo, fine=mf, hmin=min(mh))
        pickle.dump(out, open(f'lp_{tag}_it{it}.pkl', 'wb'))
        vi = np.where(fv < c - 1e-13)[0]; adds = []
        for k in range(N+1):
            j = np.where(hs[k] < c - 1e-13)[0]
            if len(j): adds.append(xf[j[np.argsort(hs[k][j])][:A.ncut]])
        if len(vi) == 0 and not adds:
            print(f"[{tag}] converged", flush=True); break
        if len(vi):
            tau = np.unique(np.concatenate([tau, tf[vi[np.argsort(fv[vi])][:A.ncut]]]))
        if adds:
            xs = np.unique(np.concatenate([xs] + adds))
    pickle.dump(out, open(f'lp_{tag}.pkl', 'wb'))
    print(f"saved lp_{tag}.pkl", flush=True)


if __name__ == '__main__':
    main()
