"""validation of hp.py: lambda_A at T=1/2 log3, log2 and tapered k=1 at T<=2.4."""
import sys, time, numpy as np
from hp import *
wt = {'v': lambda ns, v, T: v, 'k1': lambda ns, v, T: v*np.cos(np.pi*np.log(ns)/(4*T))}
for T in [0.5*np.log(3), np.log(2), 1.6, 2.4]:
    for (H, p, sig) in [(0.5, 6, 0.3), (0.35, 8, 0.25), (0.25, 10, 0.2)]:
        t0=time.time()
        B = Basis(mesh(T, H, sig, 0.2*np.exp(-2*T)), p)
        Z, A, S = build(T, B, wt)
        print(f"T={T:.4f} E={B.E} p={p} N={B.N} " + " ".join(f"{k}:{np.linalg.eigvalsh(A-S[k])[0]:+.6e}" for k in S), f"{time.time()-t0:.0f}s", flush=True)
