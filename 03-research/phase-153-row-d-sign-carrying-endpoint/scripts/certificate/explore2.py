import math, sys, numpy as np, scipy.linalg as sla
import mpmath as mp
from assemble import matrices
mp.mp.dps = 200
T = mp.log(2)
for a in (mp.mpf('0.45'), mp.mpf('0.30')):
    for m in (10, 12):
        Q, NM, C, Fs, m0a = matrices(T, a, m, 200, mp.mp, False)
        Qf = np.array([[float(x) for x in r] for r in Q]); Nf = np.array([[float(x) for x in r] for r in NM])
        w, V = sla.eigh(Qf, Nf)
        v = V[:,0]/max(abs(V[:,0]))
        print(f"a={float(a)} m={m} lam={w[0]: .6e} condN={np.linalg.cond(Nf):.2e}")
        print("   v=", np.array2string(v, precision=6))
    sys.stdout.flush()
