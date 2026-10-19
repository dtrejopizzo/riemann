#!/usr/bin/env python3
"""R187 — pattern extraction T ↦ λ_A(T) over DATA_100_WINDOWS.csv (row D; CONSTRAINTS_FOR_PATTERN.md §6).

Self-contained: python3 r187_pattern.py [--csv DATA_100_WINDOWS.csv] [--tfit 0.85] [--mm DATA_MM_FALSIFIER.csv]
Only numpy/scipy. Prints markdown tables. Label for everything printed: NUMERICAL (fits) / CONJECTURE (laws).
y := -ln λ_A ;  d := -log10 λ_A (digits).  N := N(T*) from the data (real zeros ≤ T* = 2πe^{2T}),
N_s := (T*/2π) ln(T*/2πe) + 7/8 = e^{2T}(2T-1) + 7/8 (smooth Riemann–von Mangoldt).
"""
import csv, math, os, sys, json, argparse
import numpy as np
from scipy.optimize import curve_fit

HERE = os.path.dirname(os.path.abspath(__file__))
LN10 = math.log(10); G1 = 14.134725141734693; PI2 = 2 * math.pi ** 2

# ----------------------------------------------------------------------------- data
def load(path):
    rows = [r for r in csv.DictReader(open(path))]
    rows.sort(key=lambda r: float(r['T']))
    D = {}
    D['T'] = np.array([float(r['T']) for r in rows]); D['lab'] = [r['T_label'] for r in rows]
    D['lam'] = np.array([float(r['lamA_float']) for r in rows]); D['conv'] = np.array([r['converged'] == 'YES' for r in rows])
    D['nneg'] = np.array([int(r['nneg']) for r in rows]); D['N'] = np.array([int(r['N_Tstar']) for r in rows])
    for k in ('K_1em2', 'K_1em3', 'K_1em4', 'K_e', 'S_size'): D[k] = np.array([int(r[k]) for r in rows])
    for k in ('N_Sh', 'N_Sh_below_Tstar', 'hstar_peak', 'hstar_centroid', 'hstar_even_mass', 'hstar2_even_mass', 'relvar_lastM', 'precision_margin_digits', 'n_comps', 'tau_last'):
        D[k] = np.array([float(r[k]) for r in rows])
    D['parity'] = [r['hstar_parity'] for r in rows]
    D['ladder'] = [np.array([float(x) for x in r['ladder_top10'].split(';')]) for r in rows]
    D['Pos'] = np.array([float(r['Pos_h'].split('+/-')[0].strip('[ ')) for r in rows])
    D['prime'] = np.array([float(r['prime_term_h'].split('+/-')[0].strip('[ ')) for r in rows])
    D['notes'] = [r['notes'] for r in rows]; D['rows'] = rows
    D['y'] = -np.log(D['lam']); D['d'] = -np.log10(D['lam'])
    D['Ns'] = np.exp(2 * D['T']) * (2 * D['T'] - 1) + 7 / 8
    return D

def Ns_of(T): return np.exp(2 * T) * (2 * T - 1) + 7 / 8

# ----------------------------------------------------------------------------- candidate laws  y = -ln λ_A
# each law: (name, nparams, f(T, N, p), p0, domain(T,N) -> bool)
def L_a0(T, N, p): return PI2 * N / np.log(N)
def L_a1(T, N, p): return p[0] * N / np.log(N)
def L_a2(T, N, p): return p[0] * Ns_of(T) / np.log(Ns_of(T))
def L_b(T, N, p): x = np.exp(2 * T) * (2 * T - 1); return p[0] * x / np.log(x) + p[1]
def L_c(T, N, p): return p[0] * np.exp(2 * T) + p[1] * T + p[2]
def L_d1(T, N, p): return p[0] * N * np.log(N) + p[1]
def L_d2(T, N, p): x = Ns_of(T); return p[0] * x * np.log(x) + p[1]
def L_g(T, N, p): return p[0] * Ns_of(T) + p[1]
def L_g1(T, N, p): return p[0] * N + p[1]
def L_f(T, N, p): return p[0] * np.exp(p[1] * T) + p[2]
def L_h(T, N, p): return p[0] * np.exp(2 * T) * T + p[1]       # e^{2T}·T (zero density × window)
LAWS = [
    ('a0: 2π²N/lnN (Zhu, fixed c)',         0, L_a0, [],              lambda T, N: N >= 2),
    ('a1: c·N/lnN (N from data)',           1, L_a1, [10.0],          lambda T, N: N >= 2),
    ('a2: c·N_s/lnN_s (smooth RvM)',        1, L_a2, [10.0],          lambda T, N: Ns_of(T) > 1.5),
    ('b : c·x/ln x + d, x=e^{2T}(2T−1)',    2, L_b,  [10.0, 0.0],     lambda T, N: np.exp(2 * T) * (2 * T - 1) > 1.5),
    ('c : c₁e^{2T} + c₂T + c₃',             3, L_c,  [10.0, 0.0, 0.0], lambda T, N: np.ones_like(T, bool)),
    ('d1: a·N lnN + d (N from data)',       2, L_d1, [1.0, 0.0],      lambda T, N: N >= 1),
    ('d2: a·N_s lnN_s + d',                 2, L_d2, [1.0, 0.0],      lambda T, N: Ns_of(T) > 1.0),
    ('g : a·N_s + d (linear in count)',     2, L_g,  [6.0, 0.0],      lambda T, N: np.ones_like(T, bool)),
    ('g1: a·N + d (N from data)',           2, L_g1, [6.0, 0.0],      lambda T, N: np.ones_like(T, bool)),
    ('f : a·e^{bT} + d (free rate)',        3, L_f,  [10.0, 2.0, 0.0], lambda T, N: np.ones_like(T, bool)),
    ('h : a·T e^{2T} + d',                  2, L_h,  [5.0, 0.0],      lambda T, N: np.ones_like(T, bool)),
]

def fit_law(law, T, N, y):
    name, npar, f, p0, dom = law
    m = dom(T, N)
    if npar == 0: return np.array([]), m
    try:
        p, _ = curve_fit(lambda TT, *pp: f(TT, N[m], pp), T[m], y[m], p0=p0, maxfev=20000)
    except Exception as e:
        p = np.array(p0) * np.nan
    return np.array(p), m

def margin_B(T):
    """𝓑(T,k) from Paper 47 eq:Bmargin minimized over k ≥ 5 (lem:zerosum for Σ_p; H_PT = 3e12)."""
    best = np.inf; kb = None
    for k in range(5, 400):
        p = 2 * k - 8; Y = T * G1 / math.sqrt(2)
        leps = 2 * k * math.log(k) + (1 - 2 * k) * math.log(Y) - math.log(math.pi * (2 * k - 1))
        if leps >= math.log(0.5): continue
        eps = math.exp(leps)
        Sig = lambda H: p / (2 * math.pi) * H ** (1 - p) * (math.log(H) / (p - 1) + 1 / (p - 1) ** 2)
        lg = math.log(2 * 1.0012 * T * T) + 2 * k * math.log(k / T) + math.log(Sig(21) + math.exp(T) * Sig(3e12)) \
             - math.log(14.13 ** 4 * T / 64 * (0.5 - eps))
        if lg < best: best, kb = lg, k
    return best, kb          # log 𝓑

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--csv', default=os.path.join(HERE, 'DATA_100_WINDOWS.csv'))
    ap.add_argument('--tfit', type=float, default=0.85); ap.add_argument('--tmin', type=float, default=0.55)
    ap.add_argument('--mm', default=os.path.join(HERE, 'DATA_MM_FALSIFIER.csv')); a = ap.parse_args()
    D = load(a.csv); T, y, d, N, lam = D['T'], D['y'], D['d'], D['N'], D['lam']
    n = len(T); print(f"## Data: {n} windows, T ∈ [{T[0]:.4f}, {T[-1]:.4f}]; converged {D['conv'].sum()}; nneg>0: {(D['nneg']>0).sum()}; λ_A ≤ 0: {(lam<=0).sum()}; min precision margin {D['precision_margin_digits'].min():.1f}")
    bad = [(T[i], D['nneg'][i], lam[i], D['notes'][i]) for i in range(n) if D['nneg'][i] > 0 or lam[i] <= 0]
    print("CONTACT/ALERT:", bad if bad else "no row with nneg>0 or λ_A ≤ 0")
    nc = [f"{T[i]:.4f}" for i in range(n) if not D['conv'][i]]; print("Not converged (upper bound):", nc or 'none')

    # ---------------------------------------------------------------- 1. local slope (editor's observation)
    print("\n## 1. Local slope  s(T) = d(−log10 λ_A)/dT ÷ e^{2T}  (centered differences over consecutive windows)")
    print("| mean T | s = d'/e^{2T} | d'(T) digits/u.T | N(T*) |"); print("|---|---|---|---|")
    Tm = 0.5 * (T[1:] + T[:-1]); dp = np.diff(d) / np.diff(T); s = dp / np.exp(2 * Tm)
    for i in range(len(Tm)):
        if T[i + 1] - T[i] > 0.015 or True: print(f"| {Tm[i]:.4f} | {s[i]:.2f} | {dp[i]:.1f} | {N[i]} |")
    sel = Tm > 0.6; print(f"s(T) at T>0.6: mean {s[sel].mean():.2f}, sd {s[sel].std():.2f}, range [{s[sel].min():.2f}, {s[sel].max():.2f}]")

    # ---------------------------------------------------------------- 2. fit of laws at T ≤ T_fit, prediction T > T_fit
    fitm = (T >= a.tmin) & (T <= a.tfit); test = T > a.tfit
    print(f"\n## 2. Laws for y = −ln λ_A. Fit on {a.tmin} ≤ T ≤ {a.tfit} ({fitm.sum()} windows); prediction on T > {a.tfit} ({test.sum()} windows)")
    print("| law | #par | parameters | fit rms (digits) | out-of-sample error in −log10 λ_A: mean±sd, max (digits) | relative error in y: first → last | trend |")
    print("|---|---|---|---|---|---|---|")
    results = {}
    for law in LAWS:
        name, npar, f, p0, dom = law
        p, m = fit_law(law, T[fitm], N[fitm], y[fitm])
        mt = dom(T[test], N[test]); Tt, Nt, yt, dt = T[test][mt], N[test][mt], y[test][mt], d[test][mt]
        if len(Tt) == 0: continue
        yp_fit = f(T[fitm][m], N[fitm][m], p); rms = np.sqrt(np.mean((yp_fit - y[fitm][m]) ** 2)) / LN10
        yp = f(Tt, Nt, p); err = (yp - yt) / LN10; rel = (yp - yt) / yt
        trend = 'decreases' if abs(rel[-1]) < abs(rel[0]) else 'does NOT decrease'
        results[name] = dict(p=p, err=err, rel=rel, f=f, Tt=Tt)
        pstr = ', '.join(f"{v:.4g}" for v in p) if npar else '—'
        print(f"| {name} | {npar} | {pstr} | {rms:.2f} | {err.mean():+.2f}±{err.std():.2f}, max {np.abs(err).max():.2f} | {rel[0]:+.3f} → {rel[-1]:+.3f} | {trend} |")
    print("\nPer-window prediction (predicted − observed digits), windows T > T_fit:")
    keys = [k for k in results]; print("| T | d obs | " + " | ".join(k.split(':')[0] for k in keys) + " |"); print("|---|---|" + "---|" * len(keys))
    Tt_all = T[test]
    for j, tt in enumerate(Tt_all):
        cells = []
        for k in keys:
            r = results[k]; idx = np.where(np.isclose(r['Tt'], tt))[0]
            cells.append(f"{r['err'][idx[0]]:+.2f}" if len(idx) else '—')
        print(f"| {tt:.4f} | {d[test][j]:.2f} | " + " | ".join(cells) + " |")

    # law (c) and (g) over the whole range, and full fit for extrapolation
    print("\n### Fit over the whole range T ≥ %.2f (for extrapolation)" % a.tmin)
    full = T >= a.tmin; FULL = {}
    for law in LAWS:
        name, npar, f, p0, dom = law
        if npar == 0: continue
        p, m = fit_law(law, T[full], N[full], y[full]); yp = f(T[full][m], N[full][m], p)
        res = (yp - y[full][m]) / LN10; FULL[name] = (p, res)
        print(f"- {name}: p = {np.array2string(p, precision=4)}; rms {np.sqrt(np.mean(res**2)):.3f} dig; max residual {np.abs(res).max():.2f} dig; residual on the last 3: {np.array2string(res[-3:], precision=2)}")

    # ---------------------------------------------------------------- 3. folds at boundaries
    print("\n## 3. Folds at the ½log n boundaries (triples T_b − 0.01, T_b, T_b + 0.01). Δ := slope jump of y = −ln λ_A")
    print("Prediction (CONSTRAINTS 1.11–1.12, R186_036 Lemma 2, even sector): Δ(dλ_A/dT) = −2 v_n h*(T_b)²  ⇒  Δ(dy/dT) = +2 v_n h*(T_b)²/λ_A")
    EDGE = []
    print("| boundary | n, v_n | y(T−), y(T_b), y(T+) | left slope | right slope | measured Δ | noise ~ y''·h | h*(T_b)² | predicted Δ | N_Sh jump |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for i in range(n):
        lab = D['lab'][i]
        if not lab: continue
        im = np.where(np.isclose(T, T[i] - 0.01, atol=2e-4))[0]; ip = np.where(np.isclose(T, T[i] + 0.01, atol=2e-4))[0]
        if not len(im) or not len(ip): print(f"| {lab} | (triple not yet complete) | | | | | | | | |"); continue
        im, ip = im[0], ip[0]
        sl = (y[i] - y[im]) / (T[i] - T[im]); sr = (y[ip] - y[i]) / (T[ip] - T[i]); dlt = sr - sl
        nn = int(round(math.exp(2 * T[i]))); pp = next(q for q in range(2, nn + 1) if nn % q == 0); vn = 2 * math.log(pp) / math.sqrt(nn)
        # h*(T_b) from Legendre coefficients (orthonormal basis on I_T, P_k(1) = 1)
        fn = os.path.join(HERE, 'windows', f"T_{T[i]:.6f}.json"); hT2 = float('nan')
        if os.path.exists(fn):
            c = np.array(json.load(open(fn))['hstar_coeffs']); k = np.arange(len(c))
            hT = np.sum(c * np.sqrt((2 * k + 1) / (2 * T[i]))); hT2 = hT ** 2 / np.sum(c ** 2)
            from numpy.polynomial import legendre as NL
            prof = [NL.legval(x, c * np.sqrt((2 * k + 1) / (2 * T[i]))) ** 2 for x in (1.0, 0.99, 0.95, 0.9, 0.5, 0.0)]
            EDGE.append((lab, prof, lam[i]))
        # noise: local second derivative of y (law c over the whole range) × step
        pc = FULL['c : c₁e^{2T} + c₂T + c₃'][0]; ypp = 4 * pc[0] * math.exp(2 * T[i]); noise = ypp * 0.01
        pred = 2 * vn * hT2 / lam[i]
        print(f"| {lab} | {nn}, {vn:.3f} | {y[im]:.3f}, {y[i]:.3f}, {y[ip]:.3f} | {sl:.1f} | {sr:.1f} | {dlt:+.1f} | ±{noise:.1f} | {hT2:.3e} | {pred:.2e} | {D['N_Sh'][im]:.2f} → {D['N_Sh'][ip]:.2f} |")

    print("\nProfile |h*(t)|² (Legendre, final M) at t/T = 1, 0.99, 0.95, 0.9, 0.5, 0 and ratio |h*(T)|²/λ_A:")
    for lab, prof, lm in EDGE: print(f"- {lab}: " + ", ".join(f"{v:.2e}" for v in prof) + f"; |h*(T)|²/λ_A = {prof[0]/lm:.2f}")

    # ---------------------------------------------------------------- 4. observables
    print("\n## 4. Observables")
    print("### 4.1 K_δ − N(T*) per threshold (all windows with N(T*) ≥ 1)")
    sel = N >= 1
    print("| threshold | mean(K−N) | sd | min | max | #{K−N ∈ {−1,0,1}} / #windows | corr(K, N_Sh) | corr(K, N) |"); print("|---|---|---|---|---|---|---|---|")
    for k in ('K_1em2', 'K_1em3', 'K_1em4', 'K_e'):
        diff = D[k][sel] - N[sel]
        print(f"| {k} | {diff.mean():+.2f} | {diff.std():.2f} | {diff.min()} | {diff.max()} | {np.sum(np.abs(diff)<=1)}/{sel.sum()} | {np.corrcoef(D[k][sel], D['N_Sh'][sel])[0,1]:.3f} | {np.corrcoef(D[k][sel], N[sel])[0,1]:.3f} |")
    # fit K = α N + β and K vs N_s
    for k in ('K_1em3', 'K_e'):
        A = np.vstack([N[sel], np.ones(sel.sum())]).T; co = np.linalg.lstsq(A, D[k][sel], rcond=None)[0]
        A2 = np.vstack([D['Ns'][sel], np.ones(sel.sum())]).T; co2 = np.linalg.lstsq(A2, D[k][sel], rcond=None)[0]
        print(f"- {k} = {co[0]:.3f}·N(T*) + {co[1]:+.3f};  {k} = {co2[0]:.3f}·N_s + {co2[1]:+.3f}")
    print("\n### 4.2 Ladder ℓ_j = −ln(1−β_j): identity y = ℓ₁ − ln Pos(h*), steps ℓ_j − ℓ_{j+1}")
    print("| T | N(T*) | K_e | ℓ₁ | y − ℓ₁ (= −ln Pos) | ℓ₁/N(T*) | ℓ₁/N_s | steps 1..5 | mean step over j ≤ K_e |"); print("|---|---|---|---|---|---|---|---|---|")
    for i in range(n):
        if T[i] < 0.5: continue
        l = D['ladder'][i]; st = l[:-1] - l[1:]; ke = max(1, min(D['K_e'][i], 9))
        print(f"| {T[i]:.4f} | {N[i]} | {D['K_e'][i]} | {l[0]:.2f} | {y[i]-l[0]:.3f} | {l[0]/max(N[i],1):.2f} | {l[0]/D['Ns'][i]:.2f} | {', '.join(f'{v:.1f}' for v in st[:5])} | {st[:ke].mean():.2f} |")
    # ladder law: ℓ₁ vs N_s and vs y
    sel2 = T >= a.tmin; l1 = np.array([D['ladder'][i][0] for i in range(n)])
    co = np.polyfit(D['Ns'][sel2], l1[sel2], 1); print(f"- ℓ₁ ≈ {co[0]:.3f}·N_s + {co[1]:+.3f} (T ≥ {a.tmin}); rms residual {np.std(l1[sel2]-np.polyval(co, D['Ns'][sel2])):.2f}")
    st1 = np.array([D['ladder'][i][0] - D['ladder'][i][1] for i in range(n)]); st2 = np.array([D['ladder'][i][1] - D['ladder'][i][2] for i in range(n)])
    print("- first step ℓ₁−ℓ₂ by T: " + ", ".join(f"{T[i]:.2f}:{st1[i]:.1f}" for i in range(n) if T[i] >= 0.6 and i % 2 == 0))
    print("- second step ℓ₂−ℓ₃ by T: " + ", ".join(f"{T[i]:.2f}:{st2[i]:.1f}" for i in range(n) if T[i] >= 0.6 and i % 2 == 0))
    print("\n### 4.3 Parity, peak and centroid of the minimizer")
    print(f"- h* parity: {set(D['parity'])}; min even mass {D['hstar_even_mass'].min():.6f}; even mass of the 2nd eigenvector: min {D['hstar2_even_mass'].min():.4f}, max {D['hstar2_even_mass'].max():.4f}")
    pk = D['hstar_peak']; sel3 = T >= 0.5
    for nm, g in (('a + b/T', lambda t, a_, b_: a_ + b_ / t), ('a + b/T²', lambda t, a_, b_: a_ + b_ / t ** 2), ('a + b·e^{−2T}', lambda t, a_, b_: a_ + b_ * np.exp(-2 * t)), ('a + b·ln T', lambda t, a_, b_: a_ + b_ * np.log(t))):
        p, _ = curve_fit(g, T[sel3], pk[sel3], p0=[6, 1]); r = pk[sel3] - g(T[sel3], *p)
        print(f"- peak ≈ {nm}: a={p[0]:.3f}, b={p[1]:.3f}, rms {np.sqrt(np.mean(r**2)):.3f} (T ≥ 0.5; T→∞ limit = {p[0]:.2f}; γ₁/2 = {G1/2:.3f})")
    print("- peak·T: " + ", ".join(f"{T[i]:.2f}:{pk[i]*T[i]:.2f}" for i in range(0, n, 3)))
    print("- peak/T*: " + ", ".join(f"{T[i]:.2f}:{pk[i]/(2*math.pi*math.exp(2*T[i])):.3f}" for i in range(0, n, 3)))
    print("\n### 4.4 N_Sh vs λ_A (insensitivity)")
    print("| T | S(T) | N_Sh | N_Sh/N(T*) | y | residual of law c (dig) |"); print("|---|---|---|---|---|---|")
    pc = FULL['c : c₁e^{2T} + c₂T + c₃'][0]
    for i in range(n):
        if T[i] < 0.5: continue
        resid = (L_c(T[i], N[i], pc) - y[i]) / LN10
        print(f"| {T[i]:.4f} | {D['S_size'][i]} | {D['N_Sh'][i]:.2f} | {D['N_Sh'][i]/max(N[i],1):.2f} | {y[i]:.2f} | {resid:+.2f} |")
    jumps = []
    for i in range(1, n):
        if D['S_size'][i] > D['S_size'][i - 1] and T[i] - T[i - 1] < 0.03:
            jumps.append((T[i], D['N_Sh'][i] / D['N_Sh'][i - 1], (y[i] - y[i - 1]) / (T[i] - T[i - 1]) / (np.exp(2 * T[i]) * LN10)))
    print("- at each prime entry: (T, N_Sh(T+)/N_Sh(T−), local slope s = d'/e^{2T} across the boundary): " + "; ".join(f"({t:.3f}, ×{r:.2f}, s={sl:.1f})" for t, r, sl in jumps))
    print(f"- corr(log N_Sh, residual of law c) over T ≥ 0.55: {np.corrcoef(np.log(D['N_Sh'][sel2]), (L_c(T[sel2], N[sel2], pc) - y[sel2]))[0,1]:+.3f}")

    # ---------------------------------------------------------------- 5. admissibility and extrapolation
    print("\n## 5. Admissibility (CONSTRAINTS §1) and extrapolation")
    print("| T | d obs | log10 𝓑(T,k*) | k* | λ_A ≤ 𝓑 | closed bound 1.5 (T ≥ 1): log10 | λ ≤ closed |"); print("|---|---|---|---|---|---|---|")
    for i in range(n):
        if i % 4 and T[i] < 1.0: continue
        lgB, kb = margin_B(T[i]); lgB10 = lgB / LN10
        cl = (math.log(4e9 * T[i]) - 15.449 * T[i]) / LN10 if T[i] >= 1 else float('nan')
        print(f"| {T[i]:.4f} | {d[i]:.2f} | {lgB10:+.2f} | {kb} | {'YES' if -d[i] <= lgB10 else 'NO'} | {cl:+.2f} | {'YES' if T[i] < 1 or -d[i] <= cl else 'NO'} |")
    print("- monotonicity/continuity of the data: y increasing in T in %d of %d consecutive pairs" % (np.sum(np.diff(y) > 0), n - 1))
    print("\n### Extrapolation (full fit T ≥ %.2f; N(T*) by smooth RvM N_s)" % a.tmin)
    Tx = np.array([1.2, 1.5, 2.0, 3.0]); Nx = Ns_of(Tx)
    print("| T | N_s(T*) | " + " | ".join(k.split(':')[0] for k in FULL if k[0] in 'abcdgfh') + " | log10 𝓑 | closed 1.5 | Thm M: e^{2T}/ln10 (ε=0) |"); print("|---|---|" + "---|" * (len(FULL) + 3))
    for j, tx in enumerate(Tx):
        cells = []
        for k, (p, res) in FULL.items():
            f = next(l[2] for l in LAWS if l[0] == k)
            try: v = f(np.array([tx]), np.array([Nx[j]]), p)[0] / LN10
            except Exception: v = float('nan')
            cells.append(f"{v:.0f}")
        lgB = margin_B(tx)[0] / LN10; cl = (math.log(4e9 * tx) - 15.449 * tx) / LN10
        print(f"| {tx} | {Nx[j]:.1f} | " + " | ".join(cells) + f" | {lgB:+.1f} | {cl:+.1f} | {math.exp(2*tx)/LN10:.1f} |")
    print("(cells = predicted −log10 λ_A, digits; admissible if ≥ −log10 𝓑 and ≥ −closed; Thm M only asymptotic: requires −log10 λ_A ≥ e^{(2−ε)T}/ln10 for T ≥ T₀(ε) not explicit)")

    # ---------------------------------------------------------------- 6. M_m
    if os.path.exists(a.mm):
        print("\n## 6. M_1 falsifier (quartet ½ ± δ ± iγ₁; same code, r187_mm.py)")
        M = load(a.mm); rows = M['rows']
        print("| modelo | T | λ_A^{M} | −ln λ^M | −ln λ^ζ (misma T) | conv | n₋ | K₂/K₃/K₄/K_e (M) | K₂/K₃/K₄/K_e (ζ) | N(T*) | paridad | pico (ζ) | ℓ₁..ℓ₃ (M) | ℓ₁..ℓ₃ (ζ) | N_Sh (M / ζ) |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for i, r in enumerate(rows):
            Tm_ = float(r['T']); iz = np.where(np.isclose(T, Tm_, atol=1e-6))[0]
            if len(iz):
                iz = iz[0]; z = f"{y[iz]:.2f}"; Kz = f"{D['K_1em2'][iz]}/{D['K_1em3'][iz]}/{D['K_1em4'][iz]}/{D['K_e'][iz]}"; lz = ', '.join(f"{v:.1f}" for v in D['ladder'][iz][:3]); pz = f"{D['hstar_peak'][iz]:.2f}"; nz = f"{D['N_Sh'][iz]:.2f}"
            else: z = Kz = lz = pz = nz = '—'
            lm = M['lam'][i]; ym = -math.log(lm) if lm > 0 else float('nan')
            print(f"| {r['model']} | {Tm_:.4f} | {lm:.3e} | {ym:.2f} | {z} | {r['converged']} | {r['nneg']} | {r['K_1em2']}/{r['K_1em3']}/{r['K_1em4']}/{r['K_e']} | {Kz} | {r['N_Tstar']} (+2 from the quartet) | {r['hstar_parity']} | {r['hstar_peak']} ({pz}) | {', '.join(f'{v:.1f}' for v in M['ladder'][i][:3])} | {lz} | {float(r['N_Sh']):.2f} / {nz} |")
    else: print("\n## 6. (no DATA_MM_FALSIFIER.csv)")

if __name__ == '__main__': main()
