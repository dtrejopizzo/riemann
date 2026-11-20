"""lambda_min of a^w_T on P_T, hp basis, refinement levels. usage: run_hp.py T levels(comma)"""
import sys, time, numpy as np
from hp import *
LEV = {1: (0.5, 6, 0.3, 0.3), 2: (0.35, 8, 0.25, 0.1), 3: (0.25, 10, 0.2, 0.03), 4: (0.2, 12, 0.18, 0.01), 5: (0.15, 14, 0.15, 0.003), 6: (0.12, 16, 0.15, 0.001), 7: (0.1, 18, 0.15, 0.0003)}
wt = {'v': lambda ns, v, T: v}
for k in (0.9, 1.0, 1.1):
    wt[f'k{k}'] = (lambda k: lambda ns, v, T: v*np.cos(k*np.pi*np.log(ns)/(4*T)))(k)
T = float(sys.argv[1])
for L in [int(s) for s in sys.argv[2].split(',')]:
    H, p, sig, c = LEV[L]; t0 = time.time()
    B = Basis(mesh(T, H, sig, c*np.exp(-2*T)), p)
    Z, A, S = build(T, B, wt)
    out = {}
    for k in S:
        ev, V = np.linalg.eigh(A - S[k]); x = V[:, 0]
        out[k] = (ev[0], x @ A @ x, x @ S[k] @ x, ev[1])
        np.savez(f'hp_out/vec_T{T}_L{L}_{k}.npz', x=B.x, p=p, c=Z @ x, lam=ev[:6], arch=x@A@x, arith=x@S[k]@x)
    print(f"T={T} L={L} E={B.E} p={p} N={B.N} hmin={B.h.min():.2e} " + " ".join(f"{k}:{out[k][0]:+.4e}" for k in out),
          f"| k1.0 arch={out['k1.0'][1]:.6f} sum={out['k1.0'][2]:.6f} lam2={out['k1.0'][3]:+.3e}", f"{time.time()-t0:.0f}s", flush=True)
