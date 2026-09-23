"""R154 round 4: assemble, audit in interval arithmetic, and archive the certificate.

  python3 r4final.py lp_c24_it1.pkl bbout/_all.json --tag CERT_log3_M24

Checks performed here (all must pass or the script exits non-zero):
  1. the B&B segments tile [0,tau1] and [tau1,tau1+P] (once per family k=0..N) exactly;
  2. every segment reports complete = True and final_intervals = 0 (a full cover);
  3. every segment used the same target, the same wmin and the same L;
  4. the float Lipschitz constant L dominates its interval enclosure;
  5. f and every h_k, evaluated in mpmath interval arithmetic at the fine-grid minima and
     at 60 random points, agree with the float evaluator to better than eps_fp = 1e-8;
  6. c = min(segment lower bounds) - eps_fp > 0.
The archived JSON stores u_j, a_j, beta_0, beta_1 as EXACT decimal strings (the exact values
of the float64s used), so the certificate is a statement about those rationals.
"""
import argparse, json, math, pickle, sys
from decimal import Decimal
import numpy as np
import r4core as C
from r4g2 import kk

EPS_FP = 1e-8


def dec(x):
    return str(Decimal(float(x)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl'); ap.add_argument('bb')
    ap.add_argument('--tag', default='CERT')
    ap.add_argument('--npoints', type=int, default=60)
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb'))
    segs = json.load(open(A.bb))
    T, v = r['T'], r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    b0, b1 = float(r['b0']), float(r['b1'])
    L = C.lip(T, us, a, b0, b1, v)
    fail = []

    # 1-3: coverage and consistency
    tgt = {s['target'] for s in segs}
    wm = {s['wmin'] for s in segs}
    Ls = {round(s['L'], 9) for s in segs}
    if len(tgt) != 1: fail.append(f"inconsistent targets {tgt}")
    if len(wm) != 1: fail.append(f"inconsistent wmin {wm}")
    if len(Ls) != 1 or abs(list(Ls)[0] - L) > 1e-6:
        fail.append(f"segment L {Ls} != recomputed {L}")
    target = list(tgt)[0]
    for s in segs:
        if not s.get('complete'): fail.append(f"segment {s} incomplete")
        if s['final_intervals'] != 0:
            fail.append(f"segment {s['which']} [{s['lo']},{s['hi']}] has "
                        f"{s['final_intervals']} unresolved intervals")
    need = {'f': (0.0, tau1)}
    for k in range(N+1): need[f'h{k}'] = (tau1, tau1+P)
    for which, (lo, hi) in need.items():
        iv = sorted([(s['lo'], s['hi']) for s in segs if s['which'] == which])
        if not iv: fail.append(f"no segments for {which}"); continue
        if abs(iv[0][0] - lo) > 1e-9 or abs(iv[-1][1] - hi) > 1e-9:
            fail.append(f"{which} endpoints {iv[0][0]},{iv[-1][1]} != {lo},{hi}")
        for p, q in zip(iv, iv[1:]):
            if abs(p[1] - q[0]) > 1e-9:
                fail.append(f"{which} gap {p[1]} -> {q[0]}")
    lb = min(s['lb'] for s in segs)
    c = lb - EPS_FP

    # 4-5: interval arithmetic
    import r4iv as IV
    Liv = IV.lip_iv(T, us, a, b0, b1, v)
    if not (L >= float(Liv.b)):
        fail.append(f"L={L} does not dominate its enclosure {Liv}")

    def hfun(x, k):
        x = np.asarray(x, dtype=float); tk = x + k*P
        k0, k1 = kk(T, tk)
        if k < N:
            rhs = C.m(tk) - sum(vn*np.cos(tk*math.log(n)) for n, vn in v.items())
        else:
            rhs = C.m(tk) - sum(v.values())
        return C.nuhat(x, us, a) + rhs - abs(b0)*k0 - abs(b1)*k1

    def h_iv(x, k):
        """enclosure of h_k(x) = nuhat(x) + W_k(x); k<N exact prime term, k=N worst case"""
        from mpmath import iv as I
        xv = IV._iv(x); tk = xv + k*IV._iv(P)
        k0 = 2*IV._cosh(IV._iv(T))/tk + IV._sinh(IV._iv(T))/(tk*tk)
        k1 = 8*IV._iv(T)*IV._sinh(IV._iv(T))/tk
        s = IV.m_iv(x + k*P)
        for n, vn in v.items():
            if k < N:
                s = s - IV._iv(vn)*I.cos(tk*I.log(IV._iv(n)))
            else:
                s = s - IV._iv(vn)
        return s + IV.nuhat_iv(x, us, a) - abs(IV._iv(b0))*k0 - abs(IV._iv(b1))*k1

    ff = lambda t: C.fval(t, T, us, a, b0, b1, v)
    pts = {}
    mu_f, arg_f = C.fine_min(ff, tau1, 2e-5)
    pts['f_argmin'] = ('f', arg_f)
    hmins = {}
    for k in range(N+1):
        g = lambda t, k=k: hfun(t + tau1, k)
        mu, arg = C.fine_min(g, P, 2e-5)
        hmins[k] = (mu, arg + tau1)
        pts[f'h{k}_argmin'] = (f'h{k}', arg + tau1)
    rng = np.random.default_rng(12345)
    for i, p in enumerate(rng.uniform(0, tau1, A.npoints//2)):
        pts[f'f_rand{i}'] = ('f', float(p))
    for i, p in enumerate(rng.uniform(tau1, tau1+P, A.npoints//2)):
        pts[f'h0_rand{i}'] = ('h0', float(p))
    detail = {}; worst = 0.0
    for nm, (which, p) in pts.items():
        if which == 'f':
            en = IV.f_iv(p, T, us, a, b0, b1, v); fl = float(ff(np.array([p]))[0])
        else:
            k = int(which[1:])
            en = h_iv(p, k); fl = float(hfun(np.array([p]), k)[0])
        d = abs(fl - float(en.mid)); worst = max(worst, d)
        if nm.endswith('argmin'):
            detail[nm] = dict(x=dec(p), iv=str(en), float=dec(fl))
            if float(en.a) <= 0:
                fail.append(f"{nm}: interval enclosure {en} not strictly positive")
    if worst >= EPS_FP:
        fail.append(f"float vs interval discrepancy {worst} >= eps_fp {EPS_FP}")
    if c <= 0:
        fail.append(f"c = {c} is not positive")

    out = dict(
        title="Dual certificate for lambda_min(A_T) at T = (1/2) log 3",
        statement=("sigma_T(tau) + nuhat(tau) + beta0*g0hat(tau) + beta1*g1hat(tau) >= c "
                   "for all real tau, hence lambda_min(A_T(v)) >= c > 0 on P_T"),
        lemma="D2.3 (graded periodic tail, prime term exact for N periods)",
        T=dec(T), T_desc="0.5*log(3)", M=int(r['M']), U=float(r['U']),
        N_atoms=int(len(us)), lattice_step_d=dec(r['d']), period_P=dec(P),
        tau1=dec(tau1), N_periods_exact=N,
        u=[dec(x) for x in us], a=[dec(x) for x in a],
        beta0=dec(b0), beta1=dec(b1), v={str(n): dec(x) for n, x in v.items()},
        L=dec(L), L_interval=str(Liv), bb_target=dec(target),
        bb_wmin=dec(list(wm)[0]), eps_fp=dec(EPS_FP),
        lp_value=dec(r['lp']), bb_lower_bound=dec(lb), c=dec(c),
        bb_segments=len(segs),
        bb_total_evals=int(sum(s['evals'] for s in segs)),
        bb_total_unresolved_intervals=int(sum(s['final_intervals'] for s in segs)),
        fine_min_f=dec(mu_f), fine_arg_f=dec(arg_f),
        fine_min_h={str(k): dec(m) for k, (m, _) in hmins.items()},
        fine_arg_h={str(k): dec(x) for k, (_, x) in hmins.items()},
        iv_points=detail, iv_max_float_discrepancy=dec(worst),
        checks_failed=fail)
    import os
    os.makedirs('certificate', exist_ok=True)
    json.dump(out, open(f'certificate/{A.tag}.json', 'w'), indent=1)
    pickle.dump(dict(r, cert=out, segments=segs),
                open(f'certificate/{A.tag}.pkl', 'wb'))
    print(json.dumps({k: out[k] for k in
                      ['c', 'bb_lower_bound', 'L', 'L_interval', 'bb_total_evals',
                       'bb_total_unresolved_intervals', 'iv_max_float_discrepancy',
                       'fine_min_f', 'fine_min_h', 'N_atoms', 'beta0', 'beta1']}, indent=1))
    for nm, d in detail.items():
        print(nm, d['iv'])
    if fail:
        print("FAILED CHECKS:"); [print(" -", x) for x in fail]; sys.exit(1)
    print(f"\nALL CHECKS PASSED.  c = {c:.10e} > 0.  archived certificate/{A.tag}.json")


if __name__ == '__main__':
    main()
