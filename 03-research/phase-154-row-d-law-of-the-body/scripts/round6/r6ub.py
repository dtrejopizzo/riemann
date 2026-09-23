"""R154 round 6 -- UPPER bounds on c*(M) by solving the DUAL of the graded-tail LP.

The primal is  max c  s.t.  c <= f(tau_i) (rows).  Its dual is a MOMENT problem: find
weights y_i >= 0 on the chosen tau-points with

    sum_i y_i = 1                                   (the c column)
    sum_i y_i * 2cos(u_j tau_i)   = 0   for every atom u_j        (a_j free)
    sum_i y_i * g0h(tau_i)        = 0,   sum_i y_i * g1h(tau_i) = 0   (b0, b1 free)
    (t0, t1 >= 0 give the two inequality rows)

and then   c* <= sum_i y_i * base(tau_i)   for the FULL row family, because any dual
feasible point bounds the primal optimum, and restricting the primal rows only raises it.

Why this is the decisive computation: the primal LP has thousands of nearly-active rows and
HiGHS needs minutes; the dual has only n+3 CONSTRAINTS (the basis is n+3 x n+3) and as many
columns as tau-points, which simplex handles far better.  A NEGATIVE dual value is a
certified-up-to-solver-tolerance statement that NO certificate of the class with that atom
budget is positive.
"""
import argparse, math, pickle, sys, time
import numpy as np
from scipy.optimize import linprog
sys.path.insert(0, '../round5')
import r5core as C
import r6lp as R


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--T', type=float, required=True)
    ap.add_argument('--M', type=int, default=24)
    ap.add_argument('--U', type=float, default=20.0)
    ap.add_argument('--tau1', type=float, default=30.0)
    ap.add_argument('--N', type=int, default=2)
    ap.add_argument('--h', type=float, default=0.02)
    ap.add_argument('--out', default=None)
    A = ap.parse_args()
    T = A.T; v = C.vdict(T); d = 2*T/A.M; J = int((2*T+A.U)/d)
    us = np.arange(A.M, J+1)*d; P = 2*math.pi/d; n = len(us)
    tau1 = A.tau1; N = A.N; nv = 5 + n
    pts = {'f': np.arange(1e-7, tau1, A.h)}
    for k in range(N+1): pts[f'h{k}'] = tau1 + np.arange(0.0, P, A.h)
    blocks = [np.zeros((4, nv))]; rhss = [np.zeros(4)]
    blocks[0][0, 1+n] = 1; blocks[0][0, 3+n] = -1
    blocks[0][1, 1+n] = -1; blocks[0][1, 3+n] = -1
    blocks[0][2, 2+n] = 1; blocks[0][2, 4+n] = -1
    blocks[0][3, 2+n] = -1; blocks[0][3, 4+n] = -1
    A_, b_ = R.rows_f(T, pts['f'], us, v, nv, n); blocks.append(A_); rhss.append(b_)
    for k in range(N+1):
        A_, b_ = R.rows_h(T, pts[f'h{k}'], k, P, v, N, us, nv, n)
        blocks.append(A_); rhss.append(b_)
    Aub = np.vstack(blocks); bub = np.concatenate(rhss)
    cv = np.zeros(nv); cv[0] = -1.0
    fr = list(range(3+n)); nn = [3+n, 4+n]
    print(f"[ub] T={T} M={A.M} U={A.U} atoms={n} rows={Aub.shape[0]} h={A.h} P={P:.2f}",
          flush=True)
    t0 = time.time()
    rd = linprog(bub, A_eq=Aub[:, fr].T, b_eq=-cv[fr], A_ub=-Aub[:, nn].T, b_ub=cv[nn],
                 bounds=(0, None), method='highs')
    dt = time.time()-t0
    if not rd.success:
        print(f"[ub] dual failed: {rd.message} ({dt:.0f}s)", flush=True); return
    y = rd.x
    res_eq = Aub[:, fr].T @ y + cv[fr]
    res_ub = (-Aub[:, nn].T @ y) - cv[nn]
    ub = float(bub @ y)
    print(f"[ub] T={T} M={A.M} U={A.U} atoms={n}  UPPER BOUND c*<= {ub:.10e}   "
          f"|res_eq|={np.abs(res_eq).max():.3e} max_res_ub={res_ub.max():.3e} "
          f"nnz_y={int((y>1e-14).sum())} sum_y={y.sum():.12f} ({dt:.0f}s)", flush=True)
    if A.out:
        pickle.dump(dict(T=T, M=A.M, U=A.U, us=us, y=y, ub=ub, h=A.h, tau1=tau1, N=N, P=P,
                         res_eq=float(np.abs(res_eq).max()), secs=dt),
                    open(f'ub_{A.out}.pkl', 'wb'))


if __name__ == '__main__':
    main()
