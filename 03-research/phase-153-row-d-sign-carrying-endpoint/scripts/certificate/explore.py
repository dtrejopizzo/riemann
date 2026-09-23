import math, sys, numpy as np, scipy.linalg as sla
import mpmath as mp
from assemble import matrices
mp.mp.dps = 150
T = mp.log(2)
for a in (mp.mpf('0.45'), mp.mpf('0.30'), mp.mpf('0.0001')):
    for m in (4, 6, 8):
        Q, NM, C, Fs, m0a = matrices(T, a, m, 200, mp.mp, False)
        Qf = np.array([[float(x) for x in r] for r in Q])
        Nf = np.array([[float(x) for x in r] for r in NM])
        w, V = sla.eigh(Qf, Nf)
        print(f"a={float(a)} m={m}  lam_min={w[0]: .6e}   v={np.round(V[:,0]/max(abs(V[:,0])),5)}")
    sys.stdout.flush()
