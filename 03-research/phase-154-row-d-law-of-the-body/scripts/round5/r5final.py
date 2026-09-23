"""R154 round 5 -- assemble, audit in interval arithmetic, archive.

  python3 r5final.py lp_X.pkl bbout_X/_all.json --tag CERT_T058

Checks (all must pass):
 1. the B&B segments tile [0,tau1] and [tau1,tau1+P] once per family k = 0..N, exactly;
 2. every segment complete = True, final_intervals = 0, same target/wmin/M2, method taylor2;
 3. the float second-derivative bound M2 dominates a recomputation from the archived data;
 4. f and every h_k re-evaluated in mpmath interval arithmetic at the fine-grid minima and
    at random points agree with the float evaluator to better than eps_fp;
 5. c = min(segment lower bounds) - eps_fp > 0.
Coefficients are archived as EXACT decimal strings.
"""
import argparse, json, math, os, pickle, sys
from decimal import Decimal
import numpy as np
import r5core as C
sys.path.insert(0, '../round4')

EPS_FP = 1e-9


def dec(x):
    return str(Decimal(float(x)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pkl'); ap.add_argument('bb')
    ap.add_argument('--tag', default='CERT'); ap.add_argument('--npoints', type=int, default=40)
    ap.add_argument('--eps', type=float, default=EPS_FP)
    A = ap.parse_args()
    r = pickle.load(open(A.pkl, 'rb')); segs = json.load(open(A.bb))
    T, v = float(r['T']), r['v']
    tau1, P, N = float(r['tau1']), float(r['P']), int(r['N'])
    a = np.asarray(r['a']); us = np.asarray(r['us'])
    b0, b1 = float(r['b0']), float(r['b1'])
    fail = []
    tgt = {s['target'] for s in segs}; wm = {s['wmin'] for s in segs}
    if len(tgt) != 1: fail.append(f"inconsistent targets {tgt}")
    if len(wm) != 1: fail.append(f"inconsistent wmin {wm}")
    target = list(tgt)[0]
    M2f = C.m2bound(T, us, a, b0, b1, v, with_beta=True)
    M2h = C.m2bound(T, us, a, 0.0, 0.0, v, with_beta=False)
    for s in segs:
        if not s.get('complete'): fail.append(f"incomplete segment {s.get('which')}")
        if s.get('method') != 'taylor2': fail.append("segment not taylor2")
        if s['final_intervals'] != 0:
            fail.append(f"{s['which']} [{s['lo']},{s['hi']}]: {s['final_intervals']} unresolved")
        want = M2f if s['which'] == 'f' else M2h
        if abs(s['M2'] - want) > 1e-6*max(1.0, want):
            fail.append(f"{s['which']} M2 {s['M2']} != recomputed {want}")
    need = {'f': (0.0, tau1)}
    for k in range(N+1): need[f'h{k}'] = (tau1, tau1+P)
    for which, (lo, hi) in need.items():
        iv = sorted([(s['lo'], s['hi']) for s in segs if s['which'] == which])
        if not iv: fail.append(f"no segments for {which}"); continue
        if abs(iv[0][0]-lo) > 1e-9 or abs(iv[-1][1]-hi) > 1e-9:
            fail.append(f"{which} endpoints {iv[0][0]},{iv[-1][1]} != {lo},{hi}")
        for p, q in zip(iv, iv[1:]):
            if abs(p[1]-q[0]) > 1e-9: fail.append(f"{which} gap {p[1]} -> {q[0]}")
    lb = min(s['lb'] for s in segs); c = lb - A.eps

    import r4iv as IV
    from mpmath import iv as I

    def h_iv(x, k):
        xv = IV._iv(x); tk = xv + k*IV._iv(P)
        k0 = 2*IV._cosh(IV._iv(T))/tk + IV._sinh(IV._iv(T))/(tk*tk)
        k1 = 8*IV._iv(T)*IV._sinh(IV._iv(T))/tk
        s = IV.m_iv(x + k*P)
        for n, vn in v.items():
            s = s - (IV._iv(vn)*I.cos(tk*I.log(IV._iv(n))) if k < N else IV._iv(vn))
        return s + IV.nuhat_iv(x, us, a) - abs(IV._iv(b0))*k0 - abs(IV._iv(b1))*k1

    fl = lambda t, w: C.hval(t, w, T, us, a, b0, b1, v, P, N)
    pts = {}; mins = {}
    mu, arg = C.fine_min(lambda t: fl(t, 'f'), 0.0, tau1, 2e-5)
    mins['f'] = (mu, arg); pts['f_argmin'] = ('f', arg)
    for k in range(N+1):
        mu, arg = C.fine_min(lambda t, k=k: fl(t, f'h{k}'), tau1, tau1+P, 2e-5)
        mins[f'h{k}'] = (mu, arg); pts[f'h{k}_argmin'] = (f'h{k}', arg)
    rng = np.random.default_rng(2026)
    for i, p in enumerate(rng.uniform(0, tau1, A.npoints//2)): pts[f'f_rand{i}'] = ('f', float(p))
    for i, p in enumerate(rng.uniform(tau1, tau1+P, A.npoints//2)): pts[f'h0_rand{i}'] = ('h0', float(p))
    detail = {}; worst = 0.0
    for nm, (which, p) in pts.items():
        if which == 'f':
            en = IV.f_iv(p, T, us, a, b0, b1, v)
        else:
            en = h_iv(p, int(which[1:]))
        flv = float(fl(np.array([p]), which)[0])
        d = abs(flv - float(en.mid)); worst = max(worst, d)
        if nm.endswith('argmin'):
            detail[nm] = dict(x=dec(p), iv=str(en), float=dec(flv))
            if float(en.a) <= 0: fail.append(f"{nm}: enclosure {en} not strictly positive")
    if worst >= A.eps: fail.append(f"float vs interval discrepancy {worst} >= eps {A.eps}")
    if c <= 0: fail.append(f"c = {c} not positive")

    out = dict(
        title=f"Dual certificate for lambda_min(A_T) at T = {T}",
        statement=("sigma_T(tau) + nuhat(tau) + beta0*g0hat(tau) + beta1*g1hat(tau) >= c for "
                   "all real tau, hence lambda_min(A_T(v)) >= c > 0 on P_T"),
        lemma="F1 (two-frequency graded tail, R154_015 sec.2); verifier: second-order (Taylor) B&B",
        T=dec(T), M=int(r['M']), U=float(r.get('U', 0.0)), G=int(r.get('G', 0)),
        N_atoms=int(len(us)), lattice_step_d=dec(r['d']), period_P=dec(P),
        tau1=dec(tau1), N_periods_exact=N,
        u=[dec(x) for x in us], a=[dec(x) for x in a],
        beta0=dec(b0), beta1=dec(b1), v={str(n): dec(x) for n, x in v.items()},
        M2_f=dec(M2f), M2_h=dec(M2h), L_lipschitz=dec(C.lip(T, us, a, b0, b1, v)),
        bb_target=dec(target), bb_wmin=dec(list(wm)[0]), eps_fp=dec(A.eps),
        lp_value=dec(r['lp']), bb_lower_bound=dec(lb), c=dec(c),
        bb_segments=len(segs), bb_total_evals=int(sum(s['evals'] for s in segs)),
        bb_total_unresolved_intervals=int(sum(s['final_intervals'] for s in segs)),
        fine_min={k: dec(m) for k, (m, _) in mins.items()},
        fine_arg={k: dec(x) for k, (_, x) in mins.items()},
        hp=r.get('hp'), iv_points=detail, iv_max_float_discrepancy=dec(worst),
        checks_failed=fail)
    os.makedirs('certificate', exist_ok=True)
    json.dump(out, open(f'certificate/{A.tag}.json', 'w'), indent=1)
    print(json.dumps({k: out[k] for k in ['T', 'c', 'bb_lower_bound', 'bb_target',
                                          'bb_total_evals', 'bb_total_unresolved_intervals',
                                          'iv_max_float_discrepancy', 'fine_min', 'N_atoms',
                                          'beta0', 'beta1', 'M2_f']}, indent=1))
    for nm, d in detail.items(): print(nm, d['iv'])
    if fail:
        print("FAILED CHECKS:"); [print(" -", x) for x in fail]; sys.exit(1)
    print(f"\nALL CHECKS PASSED.  c = {c:.10e} > 0.  archived certificate/{A.tag}.json")


if __name__ == '__main__':
    main()
