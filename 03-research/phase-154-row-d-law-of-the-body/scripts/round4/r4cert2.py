"""R154 round 4: certify a graded (Lemma D2.3) candidate and archive it.

    python3 r4cert2.py lp_g2m19.pkl [--margin 0.8] [--wmin 5e-8]

Certified statement produced:
    f(tau) = sigma_T(tau) + nuhat(tau) + b0 g0h(tau) + b1 g1h(tau) >= c   for ALL tau in R,
proved by
  (a) exhaustive stack Lipschitz B&B of f on [0, tau1]        (no discards; budget -> raise)
  (b) exhaustive stack Lipschitz B&B of h_k on [tau1, tau1+P], k = 0..N   (Lemma D2.3)
  (c) mpmath.iv re-evaluation of L, G0, G1, k0, k1, m, and of f/h at the minima.
The single Lipschitz constant L = psi'(1/4)/2 + sum v_n log n + 2 sum |a_j| u_j
+ |b0| G0 + |b1| G1 dominates |f'| and every |h_k'| (since |k0'|,|k1'| << G0,G1 for t >= tau1).
"""
import argparse, json, math, pickle, time
from decimal import Decimal
import numpy as np
import r4core as C
from r4g2 import kk, Wrows

EPS_FP = 1e-8


def dec(x):
    return str(Decimal(float(x)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl')
    ap.add_argument('--margin', type=float, default=0.8)
    ap.add_argument('--wmin', type=float, default=5e-8)
    ap.add_argument('--hf', type=float, default=2e-5)
    ap.add_argument('--w0', type=float, default=0.02)
    ap.add_argument('--tag', default=None)
    ap.add_argument('--maxev', type=float, default=3e9)
    ap.add_argument('--noiv', action='store_true')
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb'))
    T, v = r['T'], r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    b0, b1 = float(r['b0']), float(r['b1'])
    keep = np.abs(a) > 1e-12
    print(f"atoms {len(a)} -> {int(keep.sum())}", flush=True)
    us = us[keep]; a = a[keep]
    tag = A.tag or (r.get('tag', 'cert') + '_cert')
    L = C.lip(T, us, a, b0, b1, v)
    print(f"tau1={tau1} P={P:.4f} N={N} L={L:.3f} |a|1={np.abs(a).sum():.3f}", flush=True)

    ff = lambda t: C.fval(t, T, us, a, b0, b1, v)
    mu_f, arg_f = C.fine_min(ff, tau1, A.hf)
    hk = []
    for k in range(N+1):
        def mk(k=k):
            tkx = lambda x: x + k*P
            def h(x):
                tk = tkx(np.asarray(x, dtype=float))
                k0, k1 = kk(T, tk)
                if k < N:
                    rhs = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
                else:
                    rhs = C.m(tk) - sum(v.values())
                return C.nuhat(x, us, a) + rhs - abs(b0)*k0 - abs(b1)*k1
            return h
        hk.append(mk())
    mus = []
    for k in range(N+1):
        g = lambda t, k=k: hk[k](t + tau1)
        mu, arg = C.fine_min(g, P, A.hf)
        mus.append((mu, arg + tau1))
    mu_all = min([mu_f] + [m for m, _ in mus])
    print(f"fine minima: f={mu_f:.8e}@{arg_f:.5f} " +
          " ".join(f"h{k}={m:.8e}@{x:.5f}" for k, (m, x) in enumerate(mus)), flush=True)
    target = A.margin*mu_all if mu_all > 0 else mu_all - 1e-9

    t0 = time.time()
    lb_f, best_f, st_f = C.bb_min(ff, tau1, L, target, w0=A.w0, wmin=A.wmin,
                                  max_evals=int(A.maxev))
    print(f"B&B f on [0,{tau1}]: lb={lb_f:.8e} evals={st_f['evals']} "
          f"nfinal={st_f['final_intervals']} ({time.time()-t0:.0f}s)", flush=True)
    lbs = [lb_f]; stats = [st_f]
    for k in range(N+1):
        g = lambda t, k=k: hk[k](t + tau1)
        t0 = time.time()
        lb, bb, stt = C.bb_min(g, P, L, target, w0=A.w0, wmin=A.wmin,
                               max_evals=int(A.maxev))
        print(f"B&B h{k} on [{tau1},{tau1+P:.3f}]: lb={lb:.8e} evals={stt['evals']} "
              f"nfinal={stt['final_intervals']} ({time.time()-t0:.0f}s)", flush=True)
        lbs.append(lb); stats.append(stt)
    c = min(lbs) - EPS_FP
    print(f"CERTIFIED  inf_R f >= c = {c:.8e}", flush=True)

    out = dict(lemma="D2.3 graded periodic tail", T=dec(T), T_desc="0.5*log(3)",
               M=int(r['M']), U=float(r['U']), N_atoms=int(len(us)), d=dec(r['d']),
               P=dec(P), tau1=dec(tau1), N_periods_exact=N,
               u=[dec(x) for x in us], a=[dec(x) for x in a],
               beta0=dec(b0), beta1=dec(b1),
               v={str(n): dec(x) for n, x in v.items()},
               L=dec(L), bb_target=dec(target), bb_w0=dec(A.w0), bb_wmin=dec(A.wmin),
               eps_fp=dec(EPS_FP), lp_value=dec(r['lp']),
               lower_bounds=[dec(x) for x in lbs], c=dec(c),
               bb_evals=[int(s['evals']) for s in stats],
               bb_final_intervals=[int(s['final_intervals']) for s in stats],
               bb_surviving_measure=[dec(s['surviving_measure']) for s in stats],
               fine_min_f=dec(mu_f), fine_arg_f=dec(arg_f),
               fine_min_h=[dec(m) for m, _ in mus], fine_arg_h=[dec(x) for _, x in mus])

    if not A.noiv:
        import r4iv as IV
        rep = {}
        Liv = IV.lip_iv(T, us, a, b0, b1, v)
        rep['L_iv'] = str(Liv); rep['L_float_ge_iv'] = bool(L >= float(Liv.b))
        pts = {'f_min': arg_f}
        for k, (_, x) in enumerate(mus): pts[f'h{k}_min'] = x
        det = {}
        for nm, p in pts.items():
            fi = IV.f_iv(p, T, us, a, b0, b1, v)
            det[nm] = dict(tau=dec(p), f_iv=str(fi), f_float=dec(float(ff(np.array([p]))[0])))
        rep['points'] = det
        rng = np.random.default_rng(0); worst = 0.0
        for p in rng.uniform(0, tau1 + P, 40):
            fi = IV.f_iv(p, T, us, a, b0, b1, v)
            worst = max(worst, abs(float(ff(np.array([p]))[0]) - float(fi.mid)))
        rep['max_float_vs_iv_discrepancy'] = dec(worst)
        rep['eps_fp_covers_discrepancy'] = bool(worst < EPS_FP)
        # tail floor of the k=N family, in intervals
        tN = tau1 + N*P
        k0iv, k1iv = IV.tail_k_iv(T, tN)
        rep['m_tauN_iv'] = str(IV.m_iv(tN)); rep['k0_N_iv'] = str(k0iv)
        rep['k1_N_iv'] = str(k1iv)
        out['iv_audit'] = rep
        print("IV:", {k: rep[k] for k in ['L_float_ge_iv', 'max_float_vs_iv_discrepancy',
                                          'eps_fp_covers_discrepancy']}, flush=True)

    import os
    os.makedirs('certificate', exist_ok=True)
    json.dump(out, open(f'certificate/{tag}.json', 'w'), indent=1)
    pickle.dump(dict(r, us=us, a=a, cert=out), open(f'certificate/{tag}.pkl', 'wb'))
    print(f"archived certificate/{tag}.json  c = {c:.8e}", flush=True)


if __name__ == '__main__':
    main()
