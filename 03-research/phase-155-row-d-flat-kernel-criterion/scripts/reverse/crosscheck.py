"""crosscheck.py NAME L  -- TASK 2: Theorem-Z cross-check (the test set = the primes).
Compares f^known_w (zeros only) with f_w computed from the prime/Gamma side.
DIAGNOSTIC."""
import numpy as np, json, sys, time
import revlib2 as R2

NAME, LKEY = sys.argv[1], sys.argv[2]
DT = 0.05
r = json.load(open(f"win_{NAME}.json"))
T = r["T"]; h = r["h"]; J = r["J"]; sv = np.array(r["svals"])
ujs = 2*T + h*np.arange(2, 2+J)
d = r["L"][LKEY]; y = np.array(d["y"]); x = np.array(d["x"])
tau = np.arange(0.0, r["taumax"]+1e-9, DT)

gam_all = R2.load_zeros()
g1 = gam_all[gam_all <= r["Gcut"]]
Bz, Ay, Ax = R2.zero_side(tau, T, sv, ujs, h, g1); f1 = Bz + y@Ay + x@Ax
Bz, Ay, Ax = R2.zero_side(tau, T, sv, ujs, h, gam_all); f2 = Bz + y@Ay + x@Ax
N = int(np.exp(ujs[-1]+2*h)) + 10
t0 = time.time(); ns, lam = R2.vonmangoldt_table(N)
fp = R2.f_prime_side(tau, T, sv, y, ujs, h, x, ns, lam)
out = {"name": NAME, "L": LKEY, "c": d["c"], "N_primes": N,
       "npp": int(len(ns)), "dtau": DT,
       "max_far_resid_6000_to_Gmax": float(np.abs(f1-f2).max()),
       "max_diff_zeros_vs_primes_Gcut": float(np.abs(f1-fp).max()),
       "max_diff_zeros_vs_primes_Gmax": float(np.abs(f2-fp).max()),
       "min_f_prime": float(fp.min()), "argmin_f_prime": float(tau[np.argmin(fp)]),
       "min_f_known": float(f2.min()), "t": time.time()-t0}
print(json.dumps(out, indent=1))
json.dump(out, open(f"xc_{NAME}_{LKEY}.json", "w"))
