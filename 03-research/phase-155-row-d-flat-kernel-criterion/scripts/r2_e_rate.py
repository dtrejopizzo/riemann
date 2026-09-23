"""Phase 155 round 2, task (e): the ceiling rate at T = (1/2)log 3.

Theorem R (see R155_004 sec.6) gives, for the P-periodisation of any (P)-feasible mu,
   Ceil(M,T;beta) <= int sigma_T dmu + Delta(M,beta) * mu({|tau| > P/2}),  P = pi M / T,
   Delta(M,beta) = m(P/2) - C0 + 2 A_T + 2|beta_0| gh0(0) + 2|beta_1| gh1(0),
so Ceil(M,T;beta) -> lamP.  This script measures the approach in double precision
(DIAGNOSTIC) and fits Ceil(M) = L - c M^{-p}.

Usage: python3 r2_e_rate.py
"""
import json
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import curve_fit
import r2_b_ceiling_twoprime as B

T = 0.5 * np.log(3.0)
MS = [12, 16, 24, 32, 48, 64, 96]

if __name__ == '__main__':
    rows = []
    for M in MS:
        c, b, pc = B.ceiling(T, M, ntau=41, nfft=1 << 15)
        rows.append((M, c, float(b[0]), float(b[1])))
        print("M=%3d  Ceil=%+.6e  beta=(%.5f,%.5f)" % (M, c, b[0], b[1]))
    Mv = np.array([r[0] for r in rows], float); Cv = np.array([r[1] for r in rows])
    f = lambda M, L, c, p: L - c * M ** (-p)
    popt, _ = curve_fit(f, Mv, Cv, p0=[7e-4, 1e-2, 1.5], maxfev=100000)
    print("fit  Ceil(M) = L - c M^-p :  L = %.6e   c = %.4e   p = %.4f" % tuple(popt))
    print("residuals:", np.array_str(Cv - f(Mv, *popt), precision=2))
    json.dump(dict(T=T, rows=rows, fit=dict(L=popt[0], c=popt[1], p=popt[2])),
              open('r2_e_rate.json', 'w'), indent=1)
