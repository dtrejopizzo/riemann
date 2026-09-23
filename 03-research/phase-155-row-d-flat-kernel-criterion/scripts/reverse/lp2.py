"""lp2.py -- TASK 1 with the C^2 basis of revlib2.  The LP never sees the primes."""
import numpy as np
from scipy.optimize import linprog

def solve(Bz, Ay, Ax, L=50.0, fix_edge=True, wts=None):
    A = np.vstack([Ay, Ax]); nS = A.shape[0]; nY = Ay.shape[0]; nT = A.shape[1]
    n = 2*nS + 1
    A_ub = np.zeros((nT+1, n)); b_ub = np.zeros(nT+1)
    A_ub[:nT, :nS] = -A.T; A_ub[:nT, nS:2*nS] = A.T; A_ub[:nT, -1] = 1.0
    b_ub[:nT] = Bz
    wl = np.ones(2*nS) if wts is None else np.r_[wts, wts]
    A_ub[nT, :2*nS] = wl; b_ub[nT] = L
    Aeq = None; beq = None
    if fix_edge:
        r = np.zeros(n); r[:nY] = 1.0; r[nS:nS+nY] = -1.0
        Aeq = r[None, :]; beq = np.array([1.0])
    c = np.zeros(n); c[-1] = -1.0
    r = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=Aeq, b_eq=beq,
                bounds=[(0, None)]*(2*nS)+[(None, None)], method="highs")
    if not r.success: return None, None, None
    z = r.x[:nS]-r.x[nS:2*nS]
    return r.x[-1], z[:nY], z[nY:]
