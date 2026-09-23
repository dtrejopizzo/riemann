"""run_regime.py -- R155.008: ~100 windows T in [1/2 log 3, 1.20], one fixed
C^2 flat-top class, LP trained on the zeros only, every value re-certified on a
0.005 grid.  Writes regime_table.csv and regime_windows.json.  DIAGNOSTIC."""
import numpy as np, json, time, sys, csv
import reglib as RG, lp2

GCUT   = 800.0     # zeros used; resid_check.py: beyond 800 the change is < 1e-9
TAUCAP = 60.0      # LP domain cap (tau_env exceeds it from the {2,3,4} regime on)
DTAU   = 0.02
DFINE  = 0.005
LS     = [5.0, 20.0]
H, J   = 0.25, 30
ZTAB   = 74920.827498994

def windows():
    ts = list(np.linspace(0.5493061443340548, 1.20, 69))
    for n, t in RG.ENTRIES.items():
        for o in (-0.020, -0.008, -0.002, 0.0005, 0.003, 0.010):
            v = t + o
            if 0.5493061443340548 <= v <= 1.2005: ts.append(v)
    ts = sorted(set(round(t, 9) for t in ts))
    out = [ts[0]]
    for t in ts[1:]:
        if t - out[-1] > 5e-4: out.append(t)
    return out

def main():
    TS = windows(); print("n windows =", len(TS), flush=True)
    gam = RG.zeros(GCUT); print("zeros used:", len(gam), flush=True)
    rows = []; recs = []
    t00 = time.time()
    for iw, T in enumerate(TS):
        W = RG.Win(T, H, J)
        A = RG.A_of_T(T); NT = RG.N_of_T(T)
        tenv = 2*np.pi*np.exp(A); tres = 2*np.pi*np.exp(2*T)
        taumax = min(tenv, TAUCAP)
        tau = np.arange(0.0, taumax+1e-9, DTAU)
        t0 = time.time()
        Bz, Ay, Ax = RG.zero_side(tau, W, gam)
        rec = {"T": T, "N_T": NT, "A_T": A, "tau_env": tenv, "tau_res": tres,
               "index": tenv/tres, "tau_max": taumax, "capped": bool(tenv > TAUCAP),
               "env_below_table": bool(tenv <= ZTAB), "ngrid": len(tau),
               "U": W.U, "h": H, "J": J, "Gcut": GCUT, "L": {}}
        for L in LS:
            c, y, x = lp2.solve(Bz, Ay, Ax, L=L)
            if c is None: rec["L"][str(L)] = {"status": "infeasible"}; continue
            f = Bz + y@Ay + x@Ax
            st = RG.shape_stats(W, y, x)
            tp, finf, slack_c, nband = RG.refine_min(W, gam, tau, f, DFINE, DTAU)
            Bf, Yf, Xf = RG.zero_side(tp, W, gam)
            ff = Bf + y@Yf + x@Xf
            cfine = float(min(f.min(), ff.min()))
            slack_f = RG.bernstein_slack(W.U, finf, DFINE)
            lo = f < c + 1e-5
            idx = np.nonzero(lo & np.r_[True, f[1:] <= f[:-1]] & np.r_[f[:-1] <= f[1:], True])[0]
            d = dict(c_lp=float(c), c_fine=cfine, c_cert=cfine-slack_f,
                     bern_slack=float(slack_f), finf=float(finf),
                     argmin=float(tau[np.argmin(f)]), ncontacts=int(len(idx)),
                     contacts=tau[idx].tolist()[:40], nref=int(len(tp)), nband=nband,
                     y=y.tolist(), x=x.tolist(), **st)
            rec["L"][str(L)] = d
        recs.append(rec)
        d20 = rec["L"]["20.0"]
        rows.append(dict(T=round(T, 9), N_T="|".join(map(str, NT)), nN=len(NT),
                         A_T=A, tau_env=tenv, tau_res=tres, index=tenv/tres,
                         tau_max=taumax, capped=int(rec["capped"]),
                         env_below_table=int(rec["env_below_table"]),
                         c_lp=d20["c_lp"], c_fine=d20["c_fine"],
                         c_cert=d20["c_cert"], bern=d20["bern_slack"],
                         mass=d20["mass"], absmass=d20["absmass"],
                         winf=d20["winf"], rate=d20["rate"], half=d20["half"],
                         centroid=d20["centroid"], last_node=d20["last_node"],
                         sign_changes=d20["sign_changes"],
                         ncontacts=d20["ncontacts"], argmin=d20["argmin"],
                         c_lp_L5=rec["L"]["5.0"]["c_lp"],
                         c_fine_L5=rec["L"]["5.0"]["c_fine"],
                         winf_L5=rec["L"]["5.0"]["winf"],
                         mass_L5=rec["L"]["5.0"]["mass"]))
        print("%3d/%3d T=%.6f |N|=%d env=%9.2f idx=%6.2f c_lp=% .4e c_fine=% .4e "
              "|w|inf=%6.3f mass=%+7.4f rate=%5.2f nc=%3d  %.1fs"
              % (iw+1, len(TS), T, len(NT), tenv, tenv/tres, d20["c_lp"],
                 d20["c_fine"], d20["winf"], d20["mass"], d20["rate"],
                 d20["ncontacts"], time.time()-t0), flush=True)
    json.dump(recs, open("regime_windows.json", "w"))
    with open("../regime_table.csv", "w", newline="") as fh:
        wcsv = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        wcsv.writeheader(); wcsv.writerows(rows)
    print("total %.1f s" % (time.time()-t00), flush=True)

if __name__ == "__main__":
    main()
