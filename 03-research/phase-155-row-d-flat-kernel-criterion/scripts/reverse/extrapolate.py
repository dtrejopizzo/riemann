"""extrapolate.py L  -- TASK 4: fit the optimal tail profile w_T(2T+v) on the
training windows T <= 0.68, extrapolate to T = log2 and 0.80, and evaluate the
predicted weight's f^known minimum.  DIAGNOSTIC."""
import numpy as np, json, sys
import revlib2 as R2, lp2

LKEY = sys.argv[1] if len(sys.argv) > 1 else "100.0"
TRAIN = ["log3h", "058", "062", "065"]
TEST = ["log2", "080"]
VG = np.linspace(0.0, 10.0, 501)          # v = u - 2T, common profile grid

def profile(name, LKEY):
    r = json.load(open(f"win_{name}.json")); T = r["T"]; h = r["h"]; J = r["J"]
    sv = np.array(r["svals"]); ujs = 2*T + h*np.arange(2, 2+J)
    d = r["L"][LKEY]; y = np.array(d["y"]); x = np.array(d["x"])
    w = sum(y[i]*R2.psi_edge(VG, sv[i]) for i in range(len(sv))) \
      + sum(x[k]*R2.beta_spline((VG+2*T-ujs[k])/h) for k in range(J))
    return T, w, r

Ts, Ws = [], []
for n in TRAIN:
    T, w, _ = profile(n, LKEY); Ts.append(T); Ws.append(w)
Ts = np.array(Ts); Ws = np.array(Ws)
# least-squares affine law  w(v;T) = a(v) + b(v) T   fitted on the training set
A = np.vstack([np.ones_like(Ts), Ts]).T
coef, *_ = np.linalg.lstsq(A, Ws, rcond=None)
resid = Ws - A @ coef
print("affine-in-T fit residual (sup over v, per training window):",
      np.abs(resid).max(1))

gam = R2.load_zeros(); gam = gam[gam <= 6000]
out = {"L": LKEY, "train": TRAIN, "fit_resid": np.abs(resid).max(1).tolist(), "test": {}}
for n in TEST:
    Tt, wtrue, r = profile(n, LKEY)
    wpred = coef[0] + coef[1]*Tt
    # project the predicted profile onto this window's own basis (least squares)
    T = r["T"]; h = r["h"]; J = r["J"]; sv = np.array(r["svals"])
    ujs = 2*T + h*np.arange(2, 2+J)
    B = np.vstack([[R2.psi_edge(VG, s) for s in sv],
                   [R2.beta_spline((VG+2*T-uj)/h) for uj in ujs]]).T
    # enforce sum y = 1 (C^2 at the edge) by substitution y_0 = 1 - sum_{i>0} y_i
    z, *_ = np.linalg.lstsq(B, wpred, rcond=None)
    z = np.asarray(z); z[:len(sv)] /= max(z[:len(sv)].sum(), 1e-12)   # renormalise edge
    y, x = z[:len(sv)], z[len(sv):]
    tau = np.arange(0.0, r["taumax"]+1e-9, 0.02)
    Bz, Ay, Ax = R2.zero_side(tau, T, sv, ujs, h, gam)
    f = Bz + y@Ay + x@Ax
    cpred = float(f.min())
    out["test"][n] = {"T": Tt, "c_predicted_weight": cpred,
                      "c_LP_optimum": r["L"][LKEY]["c"],
                      "proj_err": float(np.abs(B@z - wpred).max()),
                      "argmin": float(tau[np.argmin(f)])}
    print(f"{n}: predicted-w min f^known = {cpred: .5e}   LP optimum = "
          f"{r['L'][LKEY]['c']: .5e}   (proj err {np.abs(B@z-wpred).max():.2e})")
json.dump(out, open(f"extrap_{LKEY}.json", "w"))
