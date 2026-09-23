"""crosscheck_regime.py -- Theorem-Z cross-check, one window per prime regime.
Zero side (Gcut=800) vs prime/Gamma side of (7.2) with Gauss-Legendre order 800
(hostile-audit repair R155_006 SS3).  DIAGNOSTIC."""
import numpy as np, json, time
import reglib as RG

NPRIME = 600_000   # prime-power cutoff; at exp(U) the truncation alone costs 1.6e-4 (see R155_008 SS2.4)

recs = json.load(open("regime_windows.json"))
seen = {}; out = []
for r in recs:
    key = len(r["N_T"])
    if key in seen: continue
    seen[key] = 1
    W = RG.Win(r["T"], r["h"], r["J"])
    d = r["L"]["20.0"]; y = np.array(d["y"]); x = np.array(d["x"])
    tau = np.arange(0.0, r["tau_max"]+1e-9, 0.05)
    ns, lam = RG.vonmangoldt_table(NPRIME)   # NOT exp(U): the psi edge tails are not compactly supported
    t0 = time.time()
    fp = RG.f_prime_side(tau, W, y, x, ns, lam, gl_n=800)
    B, Y, X = RG.zero_side(tau, W, RG.zeros(800.0)); fz = B + y@Y + x@X
    rec = dict(T=r["T"], N_T=r["N_T"], c_fine=d["c_fine"],
               max_diff=float(np.abs(fz-fp).max()), min_f_prime=float(fp.min()),
               min_f_zero=float(fz.min()), npp=int(len(ns)), t=time.time()-t0)
    out.append(rec)
    print("T=%.4f |N|=%d  max|f_zero-f_prime|=%.3e  min f_prime=% .5e  "
          "min f_zero=% .5e  (%.1fs)" % (r["T"], key, rec["max_diff"],
          rec["min_f_prime"], rec["min_f_zero"], rec["t"]), flush=True)
json.dump(out, open("crosscheck_regime.json", "w"), indent=1)
