"""fit_regime.py -- SS4 (law inside a regime), SS5 (jump law at prime entries),
SS6 (honest extrapolation regime k -> k+1).  Reads regime_windows.json.
DIAGNOSTIC."""
import numpy as np, json
import reglib as RG

recs = json.load(open("regime_windows.json"))
LK = "20.0"
V = np.linspace(0.0, 8.0, 321)
for r in recs:
    W = RG.Win(r["T"], r["h"], r["J"])
    d = r["L"][LK]
    r["prof"] = RG.profile(W, np.array(d["y"]), np.array(d["x"]), V)
    r["key"] = len(r["N_T"])
keys = sorted({r["key"] for r in recs})
reg = {k: [r for r in recs if r["key"] == k] for k in keys}
out = {"V_grid": [0.0, 8.0, len(V)], "regimes": {}, "jumps": [], "extrap": []}

print("=== SS4  law inside each regime (L=20) ===")
for k in keys:
    R = reg[k]; T = np.array([r["T"] for r in R])
    c = np.array([r["L"][LK]["c_fine"] for r in R])
    P = np.array([r["prof"] for r in R])
    e = {}
    if len(R) >= 3:
        # value: affine and quadratic in T
        for deg, nm in ((1, "aff"), (2, "quad")):
            p = np.polyfit(T, c, deg); e["val_"+nm] = float(np.abs(np.polyval(p, T)-c).max())
            e["coef_"+nm] = np.polyfit(T, c, deg).tolist()
        # profile: affine in T, coefficient-wise in v
        A = np.vstack([np.ones_like(T), T]).T
        co, *_ = np.linalg.lstsq(A, P, rcond=None)
        e["prof_aff_sup"] = float(np.abs(A@co - P).max())
        e["prof_sup_norm"] = float(np.abs(P).max())
        e["prof_coef"] = co.tolist()
    e.update(n=len(R), Tmin=float(T.min()), Tmax=float(T.max()),
             N_T=R[0]["N_T"], c_range=[float(c.min()), float(c.max())],
             mass=[float(r["L"][LK]["mass"]) for r in R],
             winf=[float(r["L"][LK]["winf"]) for r in R],
             rate=[float(r["L"][LK]["rate"]) for r in R],
             ncont=[int(r["L"][LK]["ncontacts"]) for r in R])
    out["regimes"][str(k)] = e
    print("|N|=%d n=%2d T in [%.4f,%.4f] N_T=%s  c in [%.4e,%.4e]  "
          "aff-resid(val)=%.2e  aff-resid(prof)=%.3f (sup|w|=%.3f)  "
          "mass %.3f+-%.3f  |w|inf %.3f+-%.3f  rate %.2f+-%.2f  nc %d-%d"
          % (k, e["n"], e["Tmin"], e["Tmax"], e["N_T"], e["c_range"][0], e["c_range"][1],
             e.get("val_aff", float('nan')), e.get("prof_aff_sup", float('nan')),
             e.get("prof_sup_norm", float('nan')),
             np.mean(e["mass"]), np.std(e["mass"]), np.mean(e["winf"]), np.std(e["winf"]),
             np.mean(e["rate"]), np.std(e["rate"]), min(e["ncont"]), max(e["ncont"])))

print("\n=== SS5  jump law at the prime entries ===")
for n, Te in sorted(RG.ENTRIES.items(), key=lambda kv: kv[1]):
    below = [r for r in recs if r["T"] < Te - 1e-9]
    above = [r for r in recs if r["T"] > Te - 1e-9]
    if not below or not above: continue
    b = max(below, key=lambda r: r["T"]); a = min(above, key=lambda r: r["T"])
    if a["key"] == b["key"]: continue
    vn = 2*np.log(n if n in (2,3,5,7,11) else {4:2,8:2,9:3}[n])/np.sqrt(n)
    jb, ja = b["L"][LK], a["L"][LK]
    rec = dict(n=n, T_entry=Te, T_below=b["T"], T_above=a["T"], dT=a["T"]-b["T"],
               v_n=float(vn), env_ratio=a["tau_env"]/b["tau_env"], pred_ratio=float(np.exp(vn)),
               res_ratio=a["tau_res"]/b["tau_res"], idx_below=b["index"], idx_above=a["index"],
               c_below=jb["c_fine"], c_above=ja["c_fine"],
               prof_jump=float(np.abs(a["prof"]-b["prof"]).max()),
               mass_below=jb["mass"], mass_above=ja["mass"],
               winf_below=jb["winf"], winf_above=ja["winf"],
               rate_below=jb["rate"], rate_above=ja["rate"],
               nc_below=jb["ncontacts"], nc_above=ja["ncontacts"])
    out["jumps"].append(rec)
    print("n=%2d Te=%.6f dT=%.4f  v_n=%.4f  env x%.4f (pred e^{v_n}=%.4f)  "
          "res x%.4f  idx %.2f->%.2f  c %.4e->%.4e (x%.3f)  |dw|sup=%.4f  "
          "mass %.3f->%.3f  nc %d->%d"
          % (n, Te, rec["dT"], vn, rec["env_ratio"], rec["pred_ratio"], rec["res_ratio"],
             rec["idx_below"], rec["idx_above"], rec["c_below"], rec["c_above"],
             rec["c_above"]/rec["c_below"], rec["prof_jump"], rec["mass_below"],
             rec["mass_above"], rec["nc_below"], rec["nc_above"]))

print("\n=== SS6  extrapolation: regimes <= k  ->  first window of regime k+1 ===")
for i in range(len(keys)-1):
    k, k1 = keys[i], keys[i+1]
    train = reg[k]; test = min(reg[k1], key=lambda r: r["T"])
    if len(train) < 3: 
        print("|N|=%d -> %d : training regime has only %d windows, skipped" % (k, k1, len(train)))
        continue
    T = np.array([r["T"] for r in train])
    P = np.array([r["prof"] for r in train]); c = np.array([r["L"][LK]["c_fine"] for r in train])
    A = np.vstack([np.ones_like(T), T]).T
    co, *_ = np.linalg.lstsq(A, P, rcond=None)
    pred = co[0] + co[1]*test["T"]
    perr = float(np.abs(pred - test["prof"]).max())
    pc = np.polyfit(T, c, 1); cpred = float(np.polyval(pc, test["T"]))
    ctrue = test["L"][LK]["c_fine"]
    # naive "last value" predictor
    clast = train[-1]["L"][LK]["c_fine"]
    rec = dict(k=k, k1=k1, T_test=test["T"], ntrain=len(train), prof_err=perr,
               prof_sup=float(np.abs(test["prof"]).max()), c_pred=cpred, c_true=ctrue,
               c_last=clast, rel_err=abs(cpred-ctrue)/abs(ctrue),
               rel_err_last=abs(clast-ctrue)/abs(ctrue),
               sign_kept=bool(np.sign(cpred) == np.sign(ctrue)))
    out["extrap"].append(rec)
    print("|N|=%d (n=%d) -> |N|=%d at T=%.6f : profile sup-err=%.4f (sup|w|=%.3f)  "
          "c_pred=%.4e  c_true=%.4e  rel=%.1f%%   last-value pred=%.4e rel=%.1f%%  "
          "sign kept: %s"
          % (k, len(train), k1, test["T"], perr, rec["prof_sup"], cpred, ctrue,
             100*rec["rel_err"], clast, 100*rec["rel_err_last"], rec["sign_kept"]))

for r in recs: r.pop("prof", None)
json.dump(out, open("fit_regime.json", "w"), default=lambda o: float(o), indent=1)
print("\nwrote fit_regime.json")
