"""count.py -- R155_016 step 1: how many comb equalities, how many degrees of freedom,
and is the comb system  w(log n) = 0  (2T < log n <= U)  solvable at all?

For each (T, U, M) we report
  m   = #{prime powers n : 2T < log n <= U}          (equalities)
  n   = J-1 = #free cubic B-splines                  (dof)
  rk  = rank of the m x n collocation matrix
  res = min_x ||base(log n) + A x||_inf              (least squares; 0 => feasible)
  u*  = the largest u such that the equalities can still be met with w != 0 near u
        (diagnosed as the last knot where two prime powers are closer than h)
DIAGNOSTIC.
"""
import numpy as np, json, sys
import comblib as C

Ts = {"log3h": 0.5 * np.log(3), "w058": 0.58, "w062": 0.62, "wlog2": np.log(2)}
rows = []
ns, lam = C.P.prime_table(9.0)
logn_all = np.log(ns)
for name, T in Ts.items():
    for M in (24, 48):
        for U in (3.0, 4.0, 5.0, 6.0, 7.0, 8.0):
            if U <= 2 * T + 4 * (2 * T / M):
                continue
            win = C.WinC(T, U, M=M, Umaxpad=1.0)
            ln, vn = win.comb_nodes(ns, lam)
            A = win.spl(ln).T                       # (m, nX)
            b = -win.base(ln)
            m, nx = A.shape
            if m and nx:
                sol, *_ = np.linalg.lstsq(A, b, rcond=None)
                res = float(np.abs(A @ sol - b).max())
                rk = int(np.linalg.matrix_rank(A, tol=1e-9))
            else:
                res, rk = float("nan"), 0
            # spacing diagnostic: last prime power u with gap to next < h
            gaps = np.diff(ln)
            tight = ln[:-1][gaps < win.h]
            ustar = float(tight[0]) if len(tight) else float("inf")
            rows.append(dict(name=name, T=T, M=M, h=win.h, U=win.U, m=m, dof=nx,
                             rank=rk, resid=res, u_first_tight=ustar,
                             E_at_max=float(vn.sum())))
            print(f"{name:7s} M={M:3d} h={win.h:.4f} U={win.U:5.3f} m={m:4d} dof={nx:4d} "
                  f"rank={rk:4d} resid={res:.3e} u_tight={ustar:.3f}", flush=True)
json.dump(rows, open("count.json", "w"), indent=1)
print("wrote count.json")
