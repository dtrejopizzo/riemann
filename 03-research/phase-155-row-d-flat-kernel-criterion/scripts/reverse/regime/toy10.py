"""toy10.py -- R155.008 SS7bis: the toy universe of ten zeros, and the
cancellation budget.  Uses the certified L=20 weight of window 1 (T=1/2 log 3)
from regime_windows.json.  DIAGNOSTIC."""
import numpy as np, json, time
import reglib as RG

NPRIME = 600_000   # prime-power cutoff; at exp(U) the truncation alone costs 1.6e-4 (see R155_008 SS2.4)

recs = json.load(open("regime_windows.json"))
r = recs[0]; T = r["T"]; W = RG.Win(T, r["h"], r["J"])
d = r["L"]["20.0"]; y = np.array(d["y"]); x = np.array(d["x"])
tau = np.arange(0.0, r["tau_max"]+1e-9, 0.05)
ns, lam = RG.vonmangoldt_table(NPRIME)   # NOT exp(U): the psi edge tails are not compactly supported
t0 = time.time()
fp = RG.f_prime_side(tau, W, y, x, ns, lam, gl_n=800)
print("prime/Gamma side (GL 800, %d prime powers <= e^%.3f): %.1fs"
      % (len(ns), W.U, time.time()-t0), flush=True)
gall = RG.zeros(1e9)
out = {"T": T, "U": W.U, "n_primepowers": int(len(ns)),
       "min_f_prime": float(fp.min()), "rows": []}
for k in (1, 2, 5, 10, 100, 1000, 10000, 100000):
    g = gall[:k]
    B, Y, X = RG.zero_side(tau, W, g); f = B + y@Y + x@X
    row = dict(nzeros=int(k), gamma_max=float(g[-1]), minf=float(f.min()),
               maxdiff=float(np.abs(f-fp).max()),
               reldiff=float(np.abs(f-fp).max()/max(np.abs(fp).max(), 1e-30)))
    out["rows"].append(row)
    print("N=%7d gamma_N=%11.3f  min f_N=% .6e  max|f_N - f_prime|=%.4e"
          % (k, g[-1], f.min(), row["maxdiff"]), flush=True)
json.dump(out, open("toy10.json", "w"), indent=1)
