"""run_window.py NAME T  -- TASK 1 for one window, C^2 spline basis.
Writes win_NAME.json.  The LP sees only the zeros.  DIAGNOSTIC."""
import numpy as np, json, sys, time
import revlib2 as R2, lp2

NAME, T = sys.argv[1], float(sys.argv[2])
M = int(sys.argv[3]) if len(sys.argv) > 3 else 8
UTARGET = 14.0
GCUT = 6000.0
DTAU = 0.02
LS = [5.0, 20.0, 100.0, 400.0, 2000.0]

h = 2*T/M
J = min(140, int((UTARGET - 2*T)/h) - 2)
ujs = 2*T + h*np.arange(2, 2+J)
sv = np.array([2.5, 4.0, 8.0, 16.0])
A_T = R2.A_const(T)
taumax = min(2*np.pi*np.exp(A_T), 200.0)
tau = np.arange(0.0, taumax + 1e-9, DTAU)
gam = R2.load_zeros(); gam = gam[gam <= GCUT]

t0 = time.time()
Bz, Ay, Ax = R2.zero_side(tau, T, sv, ujs, h, gam)
tz = time.time()-t0
rec = {"name": NAME, "T": T, "M": M, "h": h, "J": J, "U": float(ujs[-1]+2*h),
       "svals": sv.tolist(), "A_T": A_T, "taumax": taumax, "ngrid": len(tau),
       "Gcut": GCUT, "nzeros": len(gam), "t_zero": tz, "L": {}}
for L in LS:
    c, y, x = lp2.solve(Bz, Ay, Ax, L=L)
    if c is None: rec["L"][str(L)] = {"status": "infeasible"}; continue
    f = Bz + y@Ay + x@Ax
    # shape of the optimal weight
    vgrid = np.linspace(0, ujs[-1]+2*h-2*T, 2000)
    wt = sum(y[i]*R2.psi_edge(vgrid, sv[i]) for i in range(len(sv))) \
       + sum(x[k]*R2.beta_spline((vgrid+2*T-ujs[k])/h) for k in range(J))
    mass = float(np.trapz(wt, vgrid))                  # int_{2T}^inf w
    absmass = float(np.trapz(np.abs(wt), vgrid))
    cen = float(np.trapz(np.abs(wt)*vgrid, vgrid)/max(absmass, 1e-30))
    sgn = np.sign(x); nsw = int(np.sum(sgn[:-1]*sgn[1:] < 0))
    lo = f < c + 1e-5
    idx = np.nonzero(lo & np.r_[True, f[1:] <= f[:-1]] & np.r_[f[:-1] <= f[1:], True])[0]
    rec["L"][str(L)] = {
        "c": float(c), "y": y.tolist(), "x": x.tolist(),
        "l1x": float(np.abs(x).sum()), "tail_mass": mass, "tail_absmass": absmass,
        "tail_centroid": cen, "sign_changes_x": nsw,
        "last_sig_node": float(ujs[np.max(np.nonzero(np.abs(x) > 1e-3)[0])] - 2*T)
                          if np.any(np.abs(x) > 1e-3) else 0.0,
        "fmin": float(f.min()), "argmin": float(tau[np.argmin(f)]),
        "ncontacts": int(len(idx)), "contacts": tau[idx].tolist()[:60],
    }
    print(f"{NAME} L={L:7.0f} c={c: .5e} l1={np.abs(x).sum():8.2f} "
          f"mass={mass:+.4f} |mass|={absmass:.3f} cen={cen:.2f} "
          f"ncont={len(idx)} argmin={tau[np.argmin(f)]:.2f}", flush=True)
json.dump(rec, open(f"win_{NAME}.json", "w"))
print("wrote", f"win_{NAME}.json", "tz=%.1fs" % tz)
