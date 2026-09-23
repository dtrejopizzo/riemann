"""domain_probe.py -- SS5: the jump is in the DOMAIN.  run_regime.py caps the LP
domain at tau <= 60, which removes the domain jump; here the certified L=20
weight of a few windows is re-evaluated on its FULL interval [0, tau_env].
Only the first three entries are affordable (tau_env = 16.7, 59.5, 119, 502).
DIAGNOSTIC."""
import numpy as np, json, time
import reglib as RG

recs = json.load(open("regime_windows.json"))
want = [1, 2, 3, 4]                       # |N_T| = 1,2,3,4  (tau_env <= 502.4)
out = []
for k in want:
    R = [r for r in recs if len(r["N_T"]) == k]
    if not R: continue
    r = R[0]
    W = RG.Win(r["T"], r["h"], r["J"]); d = r["L"]["20.0"]
    y = np.array(d["y"]); x = np.array(d["x"])
    tenv = r["tau_env"]
    dt = 0.02 if tenv <= 130 else 0.05
    tau = np.arange(0.0, tenv+1e-9, dt)
    g = RG.zeros(tenv + 900.0)
    t0 = time.time()
    B, Y, X = RG.zero_side(tau, W, g); f = B + y@Y + x@X
    m60 = float(f[tau <= 60.0].min())
    rec = dict(T=r["T"], N_T=r["N_T"], tau_env=tenv, dtau=dt, nzeros=int(len(g)),
               c_capped60=d["c_fine"], min_on_0_60=m60,
               min_on_full=float(f.min()), argmin_full=float(tau[np.argmin(f)]),
               t=time.time()-t0)
    out.append(rec)
    print("|N|=%d T=%.5f  tau_env=%8.2f  min f on [0,60]=% .5e  "
          "min f on [0,tau_env]=% .5e at tau=%8.2f  (%.0fs)"
          % (k, r["T"], tenv, m60, rec["min_on_full"], rec["argmin_full"], rec["t"]),
          flush=True)
json.dump(out, open("domain_probe.json", "w"), indent=1)
