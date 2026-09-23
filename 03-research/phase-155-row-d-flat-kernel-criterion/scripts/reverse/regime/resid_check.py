"""resid_check.py -- how many zeros are needed?  Optimise at Gcut=800, then
re-evaluate the SAME weight with more zeros.  Fixes the Gcut of the 100-window
run.  DIAGNOSTIC."""
import numpy as np, time, json, sys
import reglib as RG, lp2
T = 0.62
W = RG.Win(T)
tau = np.arange(0.0, 60.0+1e-9, 0.02)
B, Y, X = RG.zero_side(tau, W, RG.zeros(800.0))
c, y, x = lp2.solve(B, Y, X, L=20.0)
print("LP at Gcut=800: c=%.6e  l1(x)=%.2f" % (c, abs(x).sum()), flush=True)
out = {"T": T, "c_G800": float(c)}
base = None
for G in (400., 800., 2000., 6000., 20000.):
    t0 = time.time(); g = RG.zeros(G)
    Bz, Ay, Ax = RG.zero_side(tau, W, g); f = Bz + y@Ay + x@Ax
    if base is None: base = f.copy()
    print("G=%8.0f n=%6d  min f=% .8e  max|f-f(400)|=%.3e  t=%.1fs"
          % (G, len(g), f.min(), np.abs(f-base).max(), time.time()-t0), flush=True)
    out["G%d" % G] = {"n": int(len(g)), "minf": float(f.min()),
                      "maxdev_from_G400": float(np.abs(f-base).max())}
json.dump(out, open("resid_check.json", "w"), indent=1)
