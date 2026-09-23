"""insight.py NAME [NAME...] -- INSIGHT (i)-(v) for the optimal weights."""
import numpy as np, json, sys
import dlib as D, revlib as R1

gam = R1.load_zeros()
allout = {}
for NAME in sys.argv[1:]:
    d = json.load(open(f"d_{NAME}.json")); T = d["T"]
    win = D.Win(T, M=d["M"]); y = np.array(d["y"]); x = np.array(d["x"])
    bet = np.array(d.get("beta", [0.0, 0.0])); NZ = d["nzeros"]
    g = gam[:NZ]; Z = D.Zfun(win.u, g)

    def ghat(tt):
        tt = np.asarray(tt, float)
        xs, ws = np.polynomial.legendre.leggauss(600)
        u = T*(xs+1.0); wq = T*ws; C = np.cos(np.outer(u, tt))
        return np.vstack([2*(wq*np.cosh(u/2)) @ C, 2*(wq*u*np.sinh(u/2)) @ C])

    # ---------- (i) the kernel what(t)
    tg = np.arange(0.0, 60.0, 0.002)
    wh = D.what(win, y, x, tg)
    lobes = []
    sgn = np.sign(wh); sw = np.nonzero(sgn[:-1]*sgn[1:] < 0)[0]
    for a, b in zip(np.r_[0, sw], np.r_[sw, len(tg)-1]):
        seg = wh[a:b+1]
        if len(seg) < 3: continue
        i = np.argmin(seg) if seg.mean() < 0 else np.argmax(seg)
        lobes.append({"t": float(tg[a+i]), "val": float(seg[a and i or i]),
                      "sign": int(np.sign(seg.mean())),
                      "mass": float(np.trapz(seg, tg[a:b+1]))})
    # [amended 2026-09-21 per R155_012] the [:24] cap made every run report exactly 12
    # negative lobes (lobes alternate in sign).  No cap: count them all on [0,60].
    lobes = [l for l in lobes if abs(l["val"]) > 1e-12]
    neg = [l for l in lobes if l["sign"] < 0]

    # ---------- (ii)/(iii) contacts
    tau = np.arange(0.0, win.taumax+1e-12, 2e-4)
    f = D.fvals(win, Z, y, x, tau) + bet @ ghat(tau)
    fm = f.min()
    loc = np.nonzero((f[1:-1] <= f[:-2]) & (f[1:-1] <= f[2:]))[0]+1
    con = loc[f[loc] <= fm + 0.05*max(abs(fm), 1e-6) + 1e-5]
    contacts = []
    for i in con[:40]:
        t0 = tau[i]
        j = np.searchsorted(g, t0)
        lo = g[j-1] if j > 0 else -g[0]; hi = g[j] if j < len(g) else np.inf
        terms = np.array([D.what(win, y, x, np.array([t0-gg]))[0]
                          + D.what(win, y, x, np.array([t0+gg]))[0] for gg in g[:60]])
        o = np.argsort(-np.abs(terms))[:5]
        contacts.append({"tau": float(t0), "f": float(f[i]),
                         "gap_lo": float(lo), "gap_hi": float(hi),
                         "frac_in_gap": float((t0-lo)/(hi-lo)) if np.isfinite(hi) else None,
                         "top_terms": [[float(g[k]), float(terms[k])] for k in o],
                         # [amended 2026-09-21 per R155_012] denominator = the first 60 zeros only: this is a
                         # share WITHIN THE HEAD of the sum, not of the whole zero sum.
                         "top5_share_of_first60": float(np.abs(terms[o]).sum()/max(np.abs(terms).sum(), 1e-30))})

    # ---------- (iv) mass of w in u vs log p
    ug = np.linspace(0, win.Umax, 8000); wg = win.w_of_u(ug, y, x)
    tot = np.trapz(np.abs(wg), ug)
    ps = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31]
    near = {}
    for p in ps:
        lp = np.log(p)
        if lp <= 2*T or lp > win.Umax: continue
        m = np.abs(ug-lp) <= 0.5*win.h*2
        near[str(p)] = {"log_p": float(lp), "w_at_logp": float(win.w_of_u(np.array([lp]), y, x)[0]),
                        "local_absmass_frac": float(np.trapz(np.abs(wg[m]), ug[m])/tot)}
    prof = [{"u": float(uu), "w": float(win.w_of_u(np.array([uu]), y, x)[0])}
            for uu in np.arange(2*T, min(win.Umax, 2*T+6.5), 0.05)]

    allout[NAME] = {"T": T, "M": d["M"], "nzeros": NZ, "taumax": win.taumax,
        "fmin_fine": float(fm), "n_contacts": int(len(con)),
        "kernel_lobes": lobes[:24], "n_neg_lobes_on_0_60": len(neg),
        "first_neg_lobe": neg[0] if neg else None,
        "what0": float(D.what(win, y, x, np.array([0.0]))[0]),
        "mean_gap_at_50": float(2*np.pi/np.log(50/(2*np.pi))),
        "mean_gap_at_1400": float(2*np.pi/np.log(1400/(2*np.pi))),
        "contacts": contacts, "near_logp": near, "profile": prof,
        "int_w": d["int_w"], "int_abs_w": d["int_abs_w"], "winf": d["winf"],
        "beta": bet.tolist()}
    print(NAME, "fmin", fm, "ncontacts", len(con), "neg lobes", len(neg),
          "first neg lobe", (neg[0]["t"], neg[0]["val"]) if neg else None, flush=True)
json.dump(allout, open("insight.json", "w"))
print("wrote insight.json")
