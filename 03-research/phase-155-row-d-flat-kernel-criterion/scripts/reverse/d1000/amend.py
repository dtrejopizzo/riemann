"""amend.py -- R155_013 / amendments to R155_011 per the hostile audit R155_012.
For each optimal weight:
  (a) TRUE negative-lobe count of what on [0,60] (insight.py:31 capped the list at 24);
  (b) honest TV budget ||nu_w||_TV with the CORRECT even-measure accounting, and log10 tau_env = (A_T+TV)/ln10 + log10(2pi);
  (c) honest Bernstein pad on the dense delta=0.005 grid;
  (d) D(w) = D_K + D_cosh of the decay tail lemma (R155_013), and tau_stop.
DIAGNOSTIC.
"""
import numpy as np, json, sys
import dlib as D, revlib as R1

names = sys.argv[1:]
out = {}
for NAME in names:
    d = json.load(open(f"d_{NAME}.json")); T = d["T"]
    win = D.Win(T, M=d["M"]); y = np.array(d["y"]); x = np.array(d["x"])
    bet = np.array(d.get("beta", [0.0, 0.0])); A_T = win.A_T

    # (a) true lobe count on [0,60]
    tg = np.arange(0.0, 60.0, 0.002)
    wh = D.what(win, y, x, tg)
    sg = np.sign(wh); sw = np.nonzero(sg[:-1]*sg[1:] < 0)[0]
    segs = list(zip(np.r_[0, sw+1], np.r_[sw+1, len(tg)]))
    nneg = sum(1 for a, b in segs if b > a and wh[a:b].mean() < 0)
    npos = len(segs) - nneg

    # (b) honest TV of nu_w  (even measure; a.c. pieces combined before |.|)
    u = win.u; wq = win.wq; wu = win.w_of_u(u, y, x)
    K = 0.5/np.sinh(np.maximum(u, 1e-9)/2) + 0.5/np.cosh(u/2)
    m = u >= 2*T
    dens = 0.5*(1-wu)*K + 2*wu*np.cosh(u/2)          # density on u >= 2T
    E_ac = float(2*np.sum(wq[m]*np.abs(dens[m])))     # both signs of u
    ns, lam = R1.vonmangoldt_table(int(np.exp(win.Umax))+10)
    logn = np.log(ns); sel = (logn > 2*T) & (logn <= win.Umax)
    wn = win.w_of_u(logn[sel], y, x)
    vn = 2*lam[sel]/np.sqrt(ns[sel])
    E_at = float(np.sum(vn*np.abs(wn)))               # = sum v_n |w(log n)|
    TV = E_ac + E_at
    log10_env = (A_T+TV)/np.log(10) + np.log10(2*np.pi)

    # (c) honest Bernstein pad on the dense delta = 0.005 grid
    pad_honest = d["B2"]*0.005**2/8.0

    # (d) D(w) for the decay tail lemma
    du = 2e-5
    ug = np.arange(0.0, win.Umax+2.0, du)
    wg = win.w_of_u(ug, y, x)
    W = wg*np.cosh(ug/2)                               # w cosh, even, C^2
    W2 = (W[2:]-2*W[1:-1]+W[:-2])/du**2
    D_cosh = float(4*np.trapz(np.abs(W2), ug[1:-1]))
    Kg = 0.5/np.sinh(np.maximum(ug, 1e-12)/2) + 0.5/np.cosh(ug/2)
    R = np.where(ug >= 2*T, (1-wg)*Kg, 0.0)
    R2_ = (R[2:]-2*R[1:-1]+R[:-2])/du**2
    mm = ug[1:-1] >= 2*T
    D_K = float(np.trapz(np.abs(R2_[mm]), ug[1:-1][mm]))
    Dw = D_K + D_cosh

    # tau_stop: smallest tau1 with L(tau) > 0 for tau >= tau1, L increasing
    b0, b1 = abs(bet[0]), abs(bet[1])
    def L(t):
        k0 = 2*np.cosh(T)/t + np.sinh(T)/t**2
        k1 = 8*T*np.sinh(T)/t
        return np.log(t/(2*np.pi)) - 1/t - 1/(2*t**2) - A_T - E_at - b0*k0 - b1*k1 - Dw/t**2
    lo, hi = 1.0, 1e80
    for _ in range(400):
        mid = np.sqrt(lo*hi)
        if L(mid) > 0: hi = mid
        else: lo = mid
    tau_stop = hi
    # counterfactual: the same bound with E_at = 0 (vanishing-comb weights)
    E_at0 = 0.0
    def L0(t):
        k0 = 2*np.cosh(T)/t + np.sinh(T)/t**2
        k1 = 8*T*np.sinh(T)/t
        return np.log(t/(2*np.pi)) - 1/t - 1/(2*t**2) - A_T - b0*k0 - b1*k1 - Dw/t**2
    lo, hi = 1.0, 1e80
    for _ in range(400):
        mid = np.sqrt(lo*hi)
        if L0(mid) > 0: hi = mid
        else: lo = mid
    tau_stop0 = hi

    out[NAME] = dict(T=T, A_T=A_T, n_neg_lobes=nneg, n_pos_lobes=npos, n_lobes=len(segs),
                     E_ac=E_ac, E_at=E_at, TV=TV, log10_tau_env=log10_env,
                     B2=d["B2"], pad_honest=pad_honest,
                     cert_honest=float(d["f_fine_min"]-pad_honest),
                     D_K=D_K, D_cosh=D_cosh, D=Dw,
                     tau_stop=float(tau_stop), tau_stop_combfree=float(tau_stop0),
                     winf=d["winf"], int_abs_w=d["int_abs_w"])
    print(NAME, json.dumps(out[NAME]), flush=True)
json.dump(out, open("amend.json", "w"), indent=1)
print("wrote amend.json")
