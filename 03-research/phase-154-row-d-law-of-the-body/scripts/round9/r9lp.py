"""R154 round 9 -- the SINGLE smooth-column LP (task A3 of R154_024).

    max c  s.t.   c <= f(tau) for all tau in [0, tau1]            (rows, cutting planes)
                  c <= L(tau1)                                    (ONE row: Lemma T)
    f = m - sum v_n cos(tau log n) + nuhat + b0 g0h + b1 g1h
    nuhat = sum_k c_k * nuhat_{s_k,p_k}  +  sum_j a_j (delta_{u_j}+delta_{-u_j})^
    L(tau1) = log(tau1/2)-log pi-1/(12.5 tau1^2) - Sv
              - sum_k |c_k| cap_k(tau1) - 2 sum_j |a_j| - |b0| k0(tau1) - |b1| k1(tau1)

By Lemma T (R154_025 sec.2) the second row implies f >= c on [tau1,oo): no period, no
lattice, no flat floor.  Everything here is weak duality, so any certified min > 0 is a
proof; a min < 0 certifies nothing.
"""
import argparse, json, math, sys, time
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, '../round5')
import r5core as C
import r9tail as R9


def build(T, S, PK, us_at, tau1):
    """returns evaluator pieces"""
    v = C.vdict(T); Sv = sum(v.values())
    nc, na = len(S), len(us_at)
    # variable order: c | c_k (nc) | a_j (na) | b0 b1 | p_k (nc) | q_j (na) | t0 t1
    nv = 1 + nc + na + 2 + nc + na + 2
    idx = dict(c=0, col=slice(1, 1+nc), at=slice(1+nc, 1+nc+na), b=slice(1+nc+na, 3+nc+na),
               p=slice(3+nc+na, 3+2*nc+na), q=slice(3+2*nc+na, 3+2*nc+2*na),
               t=slice(3+2*nc+2*na, 5+2*nc+2*na))
    return v, Sv, nc, na, nv, idx


def colmat(tau, T, S, PK):
    return np.column_stack([R9.nuhat_col(tau, T, s, k) for s, k in zip(S, PK)])


def fvals(tau, T, v, S, PK, x, us_at, idx):
    tau = np.asarray(tau, float)
    out = C.base(tau, v)
    if len(S):
        out = out + colmat(tau, T, S, PK) @ x[idx['col']]
    if len(us_at):
        out = out + 2*(np.cos(np.outer(tau, us_at)) @ x[idx['at']])
    b0, b1 = x[idx['b']]
    return out + b0*C.g0h(tau, T) + b1*C.g1h(tau, T)


def rows_f(tau, T, v, S, PK, us_at, nv, idx):
    tau = np.asarray(tau, float)
    A = np.zeros((len(tau), nv)); A[:, 0] = 1.0
    if len(S): A[:, idx['col']] = -colmat(tau, T, S, PK)
    if len(us_at): A[:, idx['at']] = -2*np.cos(np.outer(tau, us_at))
    A[:, idx['b']] = -np.column_stack([C.g0h(tau, T), C.g1h(tau, T)])
    return A, C.base(tau, v)


def run(T=0.58, K=40, smin=0.05, smax=50.0, orders=(0,), J=20, atwid=0.5, tau1=120.0,
        step=0.02, hsep=0.005, iters=6, tol=1e-7, tag='A', cap=1e4):
    t00 = time.time()
    S, PK = [], []
    for k in orders:
        for s in np.exp(np.linspace(math.log(smin), math.log(smax), K)):
            S.append(float(s)); PK.append(k)
    us_at = (2*T + np.linspace(0.0, atwid, J)) if J else np.array([])
    v, Sv, nc, na, nv, idx = build(T, S, PK, us_at, tau1)
    caps = np.array([float(R9.tailcap(tau1, s, k)) for s, k in zip(S, PK)])
    k0, k1 = C.kk(T, tau1)
    Lf = float(R9.L_floor(tau1, T, Sv))

    tau = np.arange(0.0, tau1 + 1e-12, step)
    A, b = rows_f(tau, T, v, S, PK, us_at, nv, idx)
    # tail row: c + sum p_k cap_k + 2 sum q_j + t0 k0 + t1 k1 <= Lf
    tr = np.zeros(nv); tr[0] = 1.0
    if nc: tr[idx['p']] = caps
    if na: tr[idx['q']] = 2.0
    tr[idx['t']] = [k0, k1]
    # |x| <= aux rows
    aux = []
    for sl, sla in ((idx['col'], idx['p']), (idx['at'], idx['q']), (idx['b'], idx['t'])):
        n = len(np.arange(nv)[sl])
        for i in range(n):
            for sg in (+1, -1):
                r = np.zeros(nv); r[np.arange(nv)[sl][i]] = sg
                r[np.arange(nv)[sla][i]] = -1.0
                aux.append(r)
    aux = np.array(aux) if aux else np.zeros((0, nv))
    baux = np.zeros(len(aux))

    cobj = np.zeros(nv); cobj[0] = -1.0
    bnd = [(None, None)]*(1+nc+na+2) + [(0, cap)]*(nc+na) + [(0, cap)]*2
    hist = []
    for it in range(iters):
        Aub = np.vstack([A, tr[None, :], aux]); bub = np.concatenate([b, [Lf], baux])
        res = linprog(cobj, A_ub=Aub, b_ub=bub, bounds=bnd, method='highs')
        if not res.success:
            print('LP FAIL', res.message); return None
        x = res.x; cval = x[0]
        f = lambda t: fvals(t, T, v, S, PK, x, us_at, idx)
        xs, vs = r6_local_minima(f, 0.0, tau1, hsep)
        tmin = float(vs.min()) if len(vs) else np.inf
        hist.append(dict(it=it, rows=int(Aub.shape[0]), lp=float(cval), truemin=tmin,
                         t=round(time.time()-t00, 1)))
        print(f"  it{it}: rows={Aub.shape[0]:6d} LP={cval:+.8e} truemin(0,tau1)={tmin:+.8e} "
              f"({time.time()-t00:.1f}s)")
        if tmin >= cval - tol: break
        bad = xs[vs < cval - tol/10]
        if not len(bad): break
        newt = np.unique(np.concatenate([bad, bad+hsep, bad-hsep]))
        newt = newt[(newt >= 0) & (newt <= tau1)]
        An, bn = rows_f(newt, T, v, S, PK, us_at, nv, idx)
        A = np.vstack([A, An]); b = np.concatenate([b, bn])
    # tail diagnostics
    pk = x[idx['p']] if nc else np.array([]); qj = x[idx['q']] if na else np.array([])
    t01 = x[idx['t']]
    tailcost = float(pk @ caps) + 2*float(qj.sum()) + float(t01[0]*k0 + t01[1]*k1)
    tailrow = Lf - tailcost
    fine = np.arange(0.0, tau1, 1e-3)
    truemin_fine = float(fvals(fine, T, v, S, PK, x, us_at, idx).min())
    out = dict(tag=tag, T=T, K=K, orders=list(orders), J=J, tau1=tau1, nvar=nv,
               LP=float(x[0]), truemin_sep=hist[-1]['truemin'], truemin_grid1e3=truemin_fine,
               Lfloor=Lf, tailcost=tailcost, tail_rhs=tailrow,
               tail_binding=bool(tailrow - x[0] < 1e-6*max(1, abs(x[0]))),
               tail_slack=float(tailrow - x[0]),
               col_cost=float(pk @ caps), atom_cost=2*float(qj.sum()),
               beta_cost=float(t01[0]*k0 + t01[1]*k1),
               b0=float(x[idx['b']][0]), b1=float(x[idx['b']][1]),
               nu_mass_hat0=float(fvals(np.array([0.0]), T, v, S, PK, x, us_at, idx)[0]
                                  - C.base(np.array([0.0]), v)[0]
                                  - x[idx['b']][0]*C.g0h(np.array([0.0]), T)[0]
                                  - x[idx['b']][1]*C.g1h(np.array([0.0]), T)[0]),
               l1_cols=float(np.abs(x[idx['col']]).sum()) if nc else 0.0,
               l1_atoms=float(np.abs(x[idx['at']]).sum()) if na else 0.0,
               hist=hist, secs=round(time.time()-t00, 1))
    return out, x, (S, PK, us_at, idx, v)


def r6_local_minima(func, lo, hi, h, nref=6):
    n = int((hi-lo)/h) + 2
    t = lo + np.arange(n)*h; t = t[t <= hi]
    val = func(t)
    m = (val[1:-1] < val[:-2]) & (val[1:-1] <= val[2:])
    x = t[np.where(m)[0]+1]
    x = np.concatenate([x, [t[0], t[-1]]])
    w = h
    for _ in range(nref):
        off = np.linspace(-w, w, 9)
        cand = np.clip(x[:, None] + off[None, :], lo, hi)
        vv = func(cand.ravel()).reshape(cand.shape)
        x = cand[np.arange(len(x)), vv.argmin(axis=1)]
        w /= 3.0
    return x, func(x)


if __name__ == '__main__':
    runs = []
    cfgs = [dict(tag='A_cols+atoms', orders=(0,), J=20, tau1=120.0),
            dict(tag='B_cols_only', orders=(0,), J=0, tau1=120.0),
            dict(tag='C_laguerre012', orders=(0, 1, 2), J=0, tau1=120.0)]
    for cf in cfgs:
        print('=== ', cf['tag'])
        r = run(**cf)
        if r: runs.append(r[0])
    json.dump(runs, open('r9_results.json', 'w'), indent=1)
    print(json.dumps(runs, indent=1))
