#!/usr/bin/env python3
"""R186_048 — Birth of negative components and migration of the minimizer.  SELF-CONTAINED (copies the constructions
of r043/r046: Paper 47 eq:symbol / eq:form / prop:band; imports nothing from the repository).

  sigma_T(tau) = m(tau) - sum_{n: log n < 2T} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi,  v_n = 2 log p/sqrt n
  (boundary convention: at T = T_n := ½ log n exactly, n is NOT a contact; sigma_{T_n^-} := sigma without n, sigma_{T_n^+} := with n)
  a_T(F) = (1/2pi) int sigma_T |F^|^2 = C0||F||^2 + int_0^{2T}(||F||^2 - c_F(u))K(u)du + ||F||^2 int_{2T}^oo K - sum v_n c_F(log n)
  P_T = {int F e^{+-t/2} = 0};  lambda_A(T) = min a_T|P_T;  h*_T unit minimizer (Legendre-Galerkin, M modes).
Parts: (A) birth geometry from sigma alone; (B) migration of h* across T_n and slope kink (Lemma 2
of R186_036); (C) new-prime term v_n c_{h*}(log n) vs lambda_A and per-component M0 threshold; (D) falsifier M_1.
Usage: python3 r048_birth.py [fast]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq, minimize_scalar
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693
FAST = len(sys.argv) > 1 and sys.argv[1] == 'fast'

# ------------------------------------------------------------------ symbol
def contacts(T, strict=True):
    out = []
    for n in range(2, 2000):
        if (np.log(n) >= 2 * T - 1e-12) if strict else (np.log(n) > 2 * T + 1e-12): break
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, np.log(p)))
    return out

def vn(n):
    p = next(q for q in range(2, n + 1) if n % q == 0); return 2 * np.log(p) / np.sqrt(n)

def m_arch(tau): return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)

def bhat(T, tau, g=GAM1, d=0.1):
    a = 2 * T; tau = np.asarray(tau, float); out = np.zeros_like(tau)
    for w in (g + tau, g - tau):
        out += 4 * (d * np.sinh(d * a) * np.cos(w * a) + w * np.cosh(d * a) * np.sin(w * a)) / (d * d + w * w)
    return out

def sigma_fn(T, strict=True, quartet=None):
    cs = contacts(T, strict)
    def s(tau):
        tau = np.atleast_1d(np.asarray(tau, float)); v = m_arch(tau)
        for n, lp in cs: v = v - 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
        return v + (bhat(T, tau, *quartet) if quartet else 0.0)
    return s

def neg_set(sig, tmax=250.0, h=2e-3):
    g = np.arange(0, tmax, h); s = sig(g)
    zs = [brentq(lambda t: sig([t])[0], g[i], g[i + 1]) for i in range(len(g) - 1) if s[i] * s[i + 1] < 0]
    pts = [0.0] + zs; assert s[-1] > 0
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1) if sig([(pts[i] + pts[i + 1]) / 2])[0] < 0]

def mass(sig, lo, hi): return quad(lambda t: -sig([t])[0], lo, hi, limit=200)[0]

def overlaps(J, comps):
    return [K for K in comps if min(J[1], K[1]) - max(J[0], K[0]) > 0]

# ------------------------------------------------------------------ Legendre Galerkin (x-space form)
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=160):
    """(1/2pi) int f |F^|^2 over pieces of tau>0 and their mirror images (f even) = (1/pi) int_{pieces}."""
    xg, wg = NL.leggauss(nq); out = np.zeros((M, M))
    for lo, hi in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        out += np.einsum('klt,t->kl', fhat2(T, M, t), f(t) * w) / np.pi
    return (out + out.T) / 2

def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))

def Cmat_factory(T, M):
    xg, wg = NL.leggauss(M + 2)
    def C(u):
        lo, hi = -T + u, T
        if hi <= lo: return np.zeros((M, M))
        y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        Mx = (legb(T, M, y) * w) @ legb(T, M, y - u).T; return (Mx + Mx.T) / 2
    return C

def form_x(T, M, strict=True, quartet=None, nu=48, npan=16):
    C = Cmat_factory(T, M); I = np.eye(M); A = np.zeros((M, M)); ug, uw = NL.leggauss(nu); edges = np.linspace(0, 2 * T, npan + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
            Cu = C(u); A += (I - Cu) * (K(u) * w)
            if quartet: g, d = quartet; A += Cu * (8 * np.cos(g * u) * np.cosh(d * u) * w)
    A += I * (quad(K, 2 * T, np.inf)[0] + C0)
    for n, lp in contacts(T, strict): A -= 2 * lp / np.sqrt(n) * C(np.log(n))
    xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
    return (A + A.T) / 2, (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2), C

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def window(T, M, strict=True, quartet=None):
    A, ta, tb, C = form_x(T, M, strict, quartet); Z = null_basis([ta, tb])
    ev, V = np.linalg.eigh(Z.T @ A @ Z); h = Z @ V[:, 0]
    sig = sigma_fn(T, strict, quartet); comps = neg_set(sig)
    return dict(T=T, M=M, A=A, C=C, lamA=ev[0], ev=ev, h=h, sig=sig, comps=comps)

def h_edge(W):
    """boundary values h*(T), h*(-T) (Legendre evaluated at ±T) and peak of |h^*|^2."""
    T, M, h = W['T'], W['M'], W['h']
    hp, hm = float(h @ legb(T, M, np.array([T]))[:, 0]), float(h @ legb(T, M, np.array([-T]))[:, 0])
    tg = np.linspace(0, 60, 6001); F2 = np.einsum('klt,k,l->t', fhat2(T, M, tg), h, h)
    return hp, hm, tg[np.argmax(F2)], F2

def neg_by_comp(W, comps=None, sig=None, h=None):
    comps = W['comps'] if comps is None else comps; sig = W['sig'] if sig is None else sig; h = W['h'] if h is None else h
    return [float(h @ form_tau(W['T'], W['M'], lambda t: -sig(t), [J]) @ h) for J in comps]

# ================================================================== (A) birth geometry (sigma only)
def part_A(ns=(2, 3, 4, 5, 7, 8, 9)):
    print("=== (A) birth of negative components: sigma_{T_n^+} = sigma_{T_n^-} - v_n cos(tau log n); T_n = ½ log n")
    print("    exact criterion: new J = connected component of {sigma_{T_n^-} < v_n cos(tau log n)} disjoint from U_{T_n^-}")
    print("    necessary: min_J sigma_{T_n^-} < v_n  and  cos(tau log n) > sigma_{T_n^-}(tau)/v_n on J")
    law = []
    for n in ns:
        T = 0.5 * np.log(n); v = vn(n); ln = np.log(n)
        s0, s1 = sigma_fn(T, strict=True), sigma_fn(T, strict=False)
        U0, U1 = neg_set(s0), neg_set(s1)
        new = [J for J in U1 if not overlaps(J, U0)]
        print(f"\n  n={n} T_n={T:.4f} v_n={v:.4f} log n={ln:.4f} (cosine period 2pi/log n = {2*np.pi/ln:.3f})")
        print(f"    U^-_{{T_n}} = {[(round(a,3),round(b,3)) for a,b in U0]}  (#={len(U0)})")
        print(f"    U^+_{{T_n}} = {[(round(a,3),round(b,3)) for a,b in U1]}  (#={len(U1)})")
        # candidates: positive local minima of sigma^- with value < v_n (up to tau=250)
        g = np.arange(0.0, 250.0, 1e-3); sv = s0(g)
        idx = [i for i in range(1, len(g) - 1) if sv[i] < sv[i - 1] and sv[i] <= sv[i + 1] and sv[i] > 0 and sv[i] < v]
        cands = []
        for i in idx:
            t = g[i]; c = np.cos(t * ln)
            # does it become a birth? the minimum falls within some new component
            born = [J for J in new if J[0] <= t <= J[1]]
            # alignment: max value of v cos - sigma^- in a neighborhood of half-period width
            tt = np.linspace(t - np.pi / ln / 2, t + np.pi / ln / 2, 401); gap = (v * np.cos(tt * ln) - s0(tt)).max()
            cands.append((t, sv[i], c, gap, bool(born)))
        print(f"    candidates (local minima 0 < sigma^- < v_n): tau | sigma^-(tau) | cos(tau log n) | local max(v cos - sigma^-) | born")
        for t, s, c, gp, b in cands[:25]:
            print(f"      {t:8.3f} | {s:7.3f} | {c:+.3f} | {gp:+.3f} | {'YES' if b else 'no'}")
        rows = []
        for J in new:
            tt = np.linspace(J[0], J[1], 801); ms = mass(s1, *J); c = (J[0] + J[1]) / 2
            i0 = np.argmin(s0(tt)); rows.append((J, ms, T * (J[1] - J[0]) / np.pi, tt[i0], s0(tt)[i0], np.cos(c * ln)))
        print(f"    NEW components ({len(new)}): J | mass int sigma^- | Shannon T_n|J|/pi | argmin sigma^- on J | min sigma^- | cos(center·log n)")
        for J, ms, sh, am, mn, c in rows:
            print(f"      [{J[0]:8.3f},{J[1]:8.3f}] | {ms:7.4f} | {sh:6.3f} | {am:8.3f} | {mn:+.3f} | {c:+.3f}")
        # law: does the candidate of lowest frequency / lowest sigma^- / highest alignment become a birth?
        if cands and new:
            bornc = [c for c in cands if c[4]]; notc = [c for c in cands if not c[4]]
            lowest = min(cands, key=lambda c: c[0])[4]; deepest = min(cands, key=lambda c: c[1])[4]; aligned = max(cands, key=lambda c: c[3])[4]
            law.append((n, lowest, deepest, aligned, len(bornc), len(notc)))
            print(f"    law: does the lowest-frequency candidate get born? {lowest}; the lowest sigma^-? {deepest}; the highest (v cos - sigma^-)? {aligned};  {len(bornc)} of {len(cands)} candidates are born")
            if bornc: print(f"    max mass among new ones: {max(r[1] for r in rows):.4f};  the candidate with the highest gap has gap {max(c[3] for c in cands):+.3f}")
        # negative and positive mass of the new term: int_J v cos vs mass in the component: how much of the new one is 'from the cosine'?
        for J in new:
            cosm = quad(lambda t: v * np.cos(t * ln), J[0], J[1])[0]; s0m = quad(lambda t: s0([t])[0], J[0], J[1])[0]
            print(f"      decomposition on [{J[0]:.2f},{J[1]:.2f}]: mass = int v cos ({cosm:+.4f}) - int sigma^- ({s0m:+.4f}) = {cosm - s0m:+.4f}")
    print("\n  law summary (n, lowestFreq, lowestSigma, highestGap, #born, #notBorn):", law)

# ================================================================== (B) migration and kink
def part_B(ns=(3, 4, 5, 7)):
    print("\n=== (B) migration of h* across T_n (NUMERICAL) and slope kink (Lemma 2 of R186_036)")
    out = {}
    for n in ns:
        T = 0.5 * np.log(n); M = 40 if T < 0.75 else (48 if not FAST else 40)
        nxt = {2: 3, 3: 4, 4: 5, 5: 7, 7: 8}[n]; Tn = 0.5 * np.log(nxt)
        Wm = window(T, M, strict=True)          # T_n^-: without n
        Wp = window(T, M, strict=False)         # T_n^+ (same I_T, symbol with n): a_T identical (c_F(log n) = 0)
        print(f"\n  n={n}: T_n={T:.4f}, M={M}.  lambda_A(T_n^-)={Wm['lamA']:+.4e}  lambda_A(T_n^+)={Wp['lamA']:+.4e}  (should match: c_F(log n)=0 on I_{{T_n}})")
        print(f"    max|A^- - A^+| = {np.abs(Wm['A'] - Wp['A']).max():.2e}  |<h^-,h^+>| = {abs(Wm['h'] @ Wp['h']):.6f}")
        U0, U1 = Wm['comps'], Wp['comps']; new = [J for J in U1 if not overlaps(J, U0)]
        nb = neg_by_comp(Wp, U1); tot = sum(nb); nn = sum(m for J, m in zip(U1, nb) if J in new)
        hp, hm, pk, _ = h_edge(Wm)
        print(f"    h*_{{T_n}} seen with sigma^+ (bookkeeping, same vector): Neg = {tot:.4f}, in new ones {nn:.4f} ({100*nn/tot:.1f} %), peak |h^|^2 at tau={pk:.2f}; h*(T)={hp:+.4f} h*(-T)={hm:+.4f}")
        print(f"    new ones at T_n^+: {[(round(a,2),round(b,2)) for a,b in new]}")
        # along (T_n, T_next]
        epss = sorted(set([0.004, 0.012, 0.03, 0.06, 0.5 * (Tn - T), Tn - T]))
        rows = []
        for e in epss:
            Te = T + e; W = window(Te, M, strict=True); comps = W['comps']; newc = [J for J in comps if not overlaps(J, U0)]
            nb = neg_by_comp(W); tot = sum(nb); nn = sum(m for J, m in zip(comps, nb) if J in newc)
            cn = float(W['h'] @ W['C'](np.log(n)) @ W['h']); hp, hm, pk, _ = h_edge(W)
            # mass of h* in the two boundary strips of width 2e (bound |c_F(log n)| <= ||F||_{strips}^2)
            xt, wt = NL.leggauss(200); y = -Te + e * (xt + 1); w = e * wt; F = legb(Te, M, y)
            edge = float(2 * ((F.T @ W['h']) ** 2 @ w))
            rows.append((e, W['lamA'], tot, nn, pk, cn, edge, hp * hm))
            print(f"    T_n+{e:.4f}: lambda_A={W['lamA']:+.4e}  Neg(h*)={tot:.4f} new={nn:.4f} ({100*nn/max(tot,1e-300):.1f} %)  peak={pk:.2f}  v_n c_h*(log n)={vn(n)*cn:+.3e} (strip bound v_n||h||_edge^2={vn(n)*edge:.3e})  h*(T)h*(-T)={hp*hm:+.4f}")
        out[n] = (Wm, Wp, rows)
        # kink: one-sided slopes of lambda_A at T_n vs -2 v_n h*(T_n)h*(-T_n)
        d = 0.004
        lm = window(T - d, M, strict=True)['lamA']; lp = window(T + d, M, strict=True)['lamA']; l0 = Wm['lamA']
        hp, hm, _, _ = h_edge(Wm)
        print(f"    kink: left slope={(l0-lm)/d:+.4e} right slope={(lp-l0)/d:+.4e} jump={(lp-l0)/d-(l0-lm)/d:+.4e}  Lemma 2: -2 v_n h*(T)h*(-T) = {-2*vn(n)*hp*hm:+.4e}  (h*(T)={hp:+.4f}, h*(-T)={hm:+.4f})")
    return out

# ================================================================== (C) per-component M0 threshold and new-prime signal
def part_C(B):
    print("\n=== (C) local M0-slope threshold per component: beta_pred = 0.7·(mass/2)·T²/b1  (R186_043 M0-slope lemma, kappa=0.7)")
    print("    T_c(J) := T with beta_pred = 1 = sqrt(2 b1/(0.7·mass)) ; compare with T_next (next birth)")
    for n, (Wm, Wp, rows) in B.items():
        T = Wp['T']; sig = Wp['sig']; nxt = {3: 4, 4: 5, 5: 7, 7: 8}[n]; Tn = 0.5 * np.log(nxt)
        U0 = Wm['comps']
        print(f"\n  n={n} enters at T_n={T:.4f}; next T_{nxt}={Tn:.4f}. Components of sigma_{{T_n^+}} (fixed on (T_n, T_next)):")
        for J in Wp['comps']:
            if J[1] > 60: continue
            ms = mass(sig, *J); h = 1e-4
            sl = [abs((sig([x + h])[0] - sig([x - h])[0]) / (2 * h)) for x in ((J[1],) if J[0] == 0.0 else (J[0], J[1]))]
            b1 = np.mean(sl); Tc = np.sqrt(2 * b1 / (0.7 * ms)) if ms > 0 else np.inf
            tag = 'NEW' if not overlaps(J, U0) else 'old'
            print(f"    [{J[0]:7.3f},{J[1]:7.3f}] {tag}: mass={ms:.4f} N_J(T_n)={T*(J[1]-J[0])/np.pi:.3f} b1={b1:.3f}  beta_pred(T_n)={0.7*ms/2*T*T/b1:.3f}  T_c={Tc:.3f}  {'CROSSES before T_next' if Tc < Tn else 'does not cross'}")

# ================================================================== (D) falsifier M_1
def part_D():
    print("\n=== (D) falsifier M_1 (quartet ½±delta±i gamma_1): births and sign between boundaries")
    for d in (0.1, 0.01):
        q = (GAM1, d); n = 4; T = np.log(2)
        s0, s1 = sigma_fn(T, True, q), sigma_fn(T, False, q); U0, U1 = neg_set(s0), neg_set(s1)
        new = [J for J in U1 if not overlaps(J, U0)]
        print(f"  delta={d}: n=4 at log 2: U^- #={len(U0)} {[(round(a,2),round(b,2)) for a,b in U0]}")
        print(f"             U^+ #={len(U1)}, new={[(round(a,2),round(b,2)) for a,b in new]}, masses={[round(mass(s1,*J),4) for J in new]}")
    print("  lambda_A(M_1, delta=0.1) along T (M=40): does it change sign at a boundary T_n or between them?")
    Ts = [0.5 * np.log(3), 0.56, 0.58, 0.60, 0.62, 0.64, 0.66, 0.68, np.log(2), np.log(2) + 0.01, 0.72, 0.76, 0.5 * np.log(5)]
    for T in Ts:
        W = window(T, 40, strict=True, quartet=(GAM1, 0.1)); ev = W['ev']
        print(f"    T={T:.4f}: lambda_A={ev[0]:+.4e} (sig {ev[1]:+.3e}) n_-={(ev<0).sum()}  contacts={[n for n,_ in contacts(T)]}")


# ================================================================== (E) fission vs ex nihilo; cost of the new prime D(eps); genealogy of the 70%
def classify(U0, U1):
    """for each J of U1: 'exnihilo' (J ∩ U0 = ∅), 'fission' (the K of U0 overlapping J also overlaps another J'), 'deformed'."""
    out = []
    for J in U1:
        Ks = overlaps(J, U0)
        if not Ks: out.append((J, 'exnihilo')); continue
        sib = [J2 for J2 in U1 if J2 != J and any(overlaps(J2, [K]) for K in Ks)]
        out.append((J, 'fission' if sib else 'deformed'))
    return out

def part_E():
    print("\n=== (E) birth type (fission / ex nihilo), cost of the new prime D(eps) and genealogy of the 70% of R186_046")
    for n in (2, 3, 4, 5, 7):
        T = 0.5 * np.log(n); U0, U1 = neg_set(sigma_fn(T, True)), neg_set(sigma_fn(T, False))
        cl = classify(U0, U1)
        print(f"  n={n}: " + "; ".join(f"[{J[0]:.2f},{J[1]:.2f}]:{k}" for J, k in cl if J[1] < 70))
    print("  genealogy of [4.24,6.46] (½log5): U_{½log3} ⊃ (6.945,10.531) [ex nihilo at n=2, adjacent to the zero of m at 6.29] → fission by 3 into (4.816,7.272)+(9.666,11.966) → deformed by 4 into (4.237,6.458)")
    # h* at ½log5 by component type relative to U_{½log3} (reproduces the 70% of R186_046)
    W = window(0.5 * np.log(5), 48 if not FAST else 40); U3 = neg_set(sigma_fn(0.5 * np.log(3)))
    nb = neg_by_comp(W); tot = sum(nb)
    print(f"  h*_{{½log5}}: Neg={tot:.4f}; per component: " + ", ".join(f"[{J[0]:.1f},{J[1]:.1f}]:{m:.4f}" for J, m in zip(W['comps'], nb) if J[1] < 70))
    print(f"    in [4.24,6.46]: {nb[1]:.4f} = {100*nb[1]/tot:.1f} % (R186_046: 70 %); in ex nihilo components (16.5+): {sum(m for J,m in zip(W['comps'],nb) if J[0]>12):.4f}")
    print("  D(eps) := lambda_A^{without n}(T_n+eps) - lambda_A(T_n+eps)  (exact cost of the new prime; first order = v_n c_{h*}(log n)); local exponent p: D ~ eps^p")
    for n, M in ((3, 40), (4, 40)):
        T = 0.5 * np.log(n); prev = None
        for e in (0.002, 0.004, 0.008, 0.016, 0.032, 0.064):
            Te = T + e
            Wn = window(Te, M, strict=True); A0, ta, tb, C = form_x(Te, M, strict=True)
            A0 = A0 + vn(n) * C(np.log(n))                       # remove the n term: 'without n' form
            Z = null_basis([ta, tb]); l0 = np.linalg.eigvalsh(Z.T @ A0 @ Z)[0]
            D = l0 - Wn['lamA']; first = vn(n) * float(Wn['h'] @ C(np.log(n)) @ Wn['h'])
            p = np.log(D / prev[1]) / np.log(e / prev[0]) if prev and D > 0 and prev[1] > 0 else float('nan')
            print(f"    n={n} eps={e:.3f}: lambda_A={Wn['lamA']:+.3e}  sin n={l0:+.3e}  D={D:+.3e}  1er orden v_n c_h*(log n)={first:+.3e}  D/lambda_A(T_n)={D/window(T,M)['lamA'] if e==0.002 else float('nan'):.3f}  p={p:.2f}")
            prev = (e, D)

if __name__ == '__main__':
    if 'E' in sys.argv: part_E(); sys.exit()
    part_A()
    B = part_B((3, 4, 5) if FAST else (3, 4, 5, 7))
    part_C(B)
    part_D()
    part_E()
