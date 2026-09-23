"""Phase 155 round 2, task (b): the beta-uniform test-kernel ceiling
Ceil(M,T) = sup_beta inf_{tau0} lambda_min(C_M(tau0,beta))  (Paper 47 Prop. 8.4)
in the two-prime windows.  DOUBLE PRECISION -> every number is DIAGNOSTIC.

Run 1:  T = 0.58,  M = 24, 32, 44, 64, 96, 128
Run 2:  T = 0.62, 0.65, 0.68, log 2,  M = 24, 64
Compared with the Galerkin upper bounds on lamA (Paper 47 sec. 6.4) and with the best
recorded certificate value at T = 0.58 (-3.1964e-3).

Usage: python3 r2_b_ceiling_twoprime.py [1a|1b|2a|2b]   (each block < 60 s)
"""
import sys, json, time
import numpy as np
from scipy.linalg import toeplitz
from scipy.optimize import minimize
import tk_common as tk

NTAU = 61          # tau0 nodes on [-2.2P, 0.2P]
NFFT = 1 << 16

GAL = {0.58: 2.16e-4, 0.62: 1.91e-5, 0.65: 2.40e-6, 0.68: 3.24e-7, float(np.log(2)): 1.09e-7}


def ceiling(T, M, ntau=NTAU, nfft=NFFT):
    parts = tk.make_S_parts(T)[:3]
    P = np.pi * M / T
    grid = np.linspace(-2.2 * P, 0.2 * P, ntau)
    MT = []
    for t0 in grid:
        cs = tk.coeff_families(T, M, t0, nfft, parts)
        MT.append([toeplitz(np.conj(c), c) for c in cs])
    def f(b):
        return -min(np.linalg.eigvalsh(Ms[0] + b[0]*Ms[1] + b[1]*Ms[2])[0] for Ms in MT)
    best = None
    for start in ([2.0, 0.0], [2.05, -0.05]):
        r = minimize(f, start, method='Nelder-Mead',
                     options={'xatol': 1e-11, 'fatol': 1e-15, 'maxiter': 6000})
        if best is None or -r.fun > best[0]:
            best = (-r.fun, r.x)
    per_cert = -f([2.0, 0.0])
    return best[0], best[1], per_cert


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else '1'
    L2 = float(np.log(2))
    JOBS = {'1a': [(0.58, M) for M in (24, 32, 44)],
            '1b': [(0.58, M) for M in (64, 96, 128)],
            '2a': [(T, M) for T in (0.62, 0.65) for M in (24, 64)],
            '2b': [(T, M) for T in (0.68, L2) for M in (24, 64)]}
    jobs = JOBS[which]
    out = []
    for T, M in jobs:
        t = time.time(); c, b, pc = ceiling(T, M)
        rec = dict(T=T, M=M, Ceil=c, beta=list(map(float, b)), ceil_beta_2_0=pc,
                   galerkin_UB=GAL.get(T), seconds=time.time() - t)
        out.append(rec)
        print("T=%.4f M=%3d  Ceil=%+.6e  beta=(%.5f,%.5f)   [beta=(2,0): %+.4e]  %.1fs"
              % (T, M, c, b[0], b[1], pc, rec['seconds']))
    json.dump(out, open(f'r2_b_ceiling_twoprime_{which}.json', 'w'), indent=1)
