#!/usr/bin/env python3
"""R186_051 — Coherence functional C_0(sigma; T, omega) of the prime measure in the window [0, 2T],
anticoherence (Krein indefiniteness) of the fluctuation, sampling identity (Poisson), and M_1 test.
Imports from r043_wh.py only the Legendre discretization (form_x, Cmat_factory, legb, fhat2, contacts, null_basis).

Definitions (Paper 47 eq:Aform; R186_035 Lemma 1):  v_n = 2 log p / sqrt n  (n = p^k < e^{2T})
  eta_T  := sum v_n delta_{log n} - 2 e^{u/2} du   (fluctuation measure on [0, 2T])
  etahat_T(w) = S_T(w) - M_T(w),  S_T = sum v_n n^{iw},  M_T = 2 (e^{(1/2+iw) 2T} - 1)/(1/2 + iw)
  C_0(T, w)  := -Re etahat_T(w) / (4T)   (= 1 for each pair of simple zeros on the line at w = gamma, to O(1/(gamma T)))
  M_1: eta^{M1} = eta^zeta - 8 cos(gamma_1 u) cosh(delta u) du
  a_T = b_0 + E_psi,  E_psi(Phi) = -int_0^{2T} Phi d eta_T   =>   b_0 = A + Q_eta,  Q_eta := Toeplitz of eta_T on L^2(I_T)
Usage: python3 r051_coherence.py   (~2 min, M = 40)
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from numpy.polynomial import legendre as NL
from r043_wh import form_x, Cmat_factory, legb, fhat2, contacts, null_basis, GAM1, C0

WINDOWS = [('1/2 log3', 0.5 * np.log(3)), ('log 2', np.log(2)), ('1/2 log5', 0.5 * np.log(5)), ('1/2 log7', 0.5 * np.log(7))]
DELTAS = [0.01, 0.1]
M = 40

# ---------------------------------------------------------------- (A) zero-order coherence, closed forms
def etahat_zeta(T, w):
    w = np.asarray(w, float); S = np.zeros_like(w, dtype=complex)
    for n, lp in contacts(T): S += 2 * lp / np.sqrt(n) * np.exp(1j * w * np.log(n))
    s = 0.5 + 1j * w; Mt = 2 * (np.exp(s * 2 * T) - 1) / s
    return S - Mt

def quartet_hat(T, w, g, d):
    """int_0^{2T} 8 cos(g u) cosh(d u) e^{i w u} du (closed form)."""
    w = np.asarray(w, float); out = np.zeros_like(w, dtype=complex); a = 2 * T
    for sg in (+1, -1):            # cos(gu) = (e^{igu}+e^{-igu})/2 ; cosh = (e^{du}+e^{-du})/2
        for sd in (+1, -1):
            z = sd * d + 1j * (w + sg * g); out += 2 * (np.exp(z * a) - 1) / z
    return out

def C0_fn(T, w, quartet=None):
    e = etahat_zeta(T, w)
    if quartet: e = e - quartet_hat(T, w, *quartet)
    return -np.real(e) / (4 * T)

def growth(dT): return np.sinh(2 * dT) / (2 * dT)

def part_A():
    print("=== (A) C_0(T, w) = -Re etahat_T(w)/(4T): zeta vs M_1 (closed forms)")
    print("   check: quartet_hat vs quadrature (T=0.7, w=20.3, d=0.1):", end=' ')
    from scipy.integrate import quad
    T0, w0, d0 = 0.7, 20.3, 0.1
    re = quad(lambda u: 8 * np.cos(GAM1 * u) * np.cosh(d0 * u) * np.cos(w0 * u), 0, 2 * T0, limit=400)[0]
    print(f"{re:.10f} vs {quartet_hat(T0, np.array([w0]), GAM1, d0)[0].real:.10f}")
    wg = np.linspace(0, 60, 60001); wr = np.linspace(0, 400, 400001)
    print(f"   {'T':>9} {'obj':>12} {'C0(g1)':>9} {'sup[0,60]':>10} {'arg':>6} {'inf[0,60]':>10} {'arg':>6} {'RMS[0,400]':>10} {'sinh(2dT)/2dT':>14}")
    for name, T in WINDOWS:
        for lab, q in [('zeta', None)] + [(f'M1 d={d}', (GAM1, d)) for d in DELTAS]:
            c = C0_fn(T, wg, q); cr = C0_fn(T, wr, q)
            g = '' if q is None else f"{growth(q[1] * T):.6f}"
            print(f"   {name:>9} {lab:>12} {C0_fn(T, [GAM1], q)[0]:9.4f} {c.max():10.4f} {wg[c.argmax()]:6.2f} {c.min():10.4f} {wg[c.argmin()]:6.2f} {np.sqrt(np.mean(cr**2)):10.4f} {g:>14}")
        sv2 = sum((2 * lp / np.sqrt(n)) ** 2 for n, lp in contacts(T))
        print(f"   {name:>9} sum v_n^2 = {sv2:.4f}  (8T^2 = {8*T*T:.4f}); C0^{{M1}}(g1) - C0^zeta(g1) = {C0_fn(T,[GAM1],(GAM1,0.1))[0]-C0_fn(T,[GAM1])[0]:.5f} vs 2 g(dT) = {2*growth(0.1*T):.5f} (d=0.1)")
    # (i): growth in T at fixed delta
    print("   (i) growth in T of C0^{M1}(T,g1) - C0^zeta(T,g1), delta = 0.1 / 0.01:")
    for T in [1, 5, 10, 20, 40]:
        print(f"      T={T:>3}: {2*growth(0.1*T):12.4e}   {2*growth(0.01*T):12.6f}   (e^{{2dT}}/(2dT) = {np.exp(0.2*T)/(0.2*T):.4e})")

# ---------------------------------------------------------------- (B)(C) Galerkin: a_T, b_0, Q_eta, quartet, h*
def toeplitz_measure(T, M, atoms, dens=None, nu=64, npan=16):
    """Q[mu] = sum_atoms c_j C(u_j) + int_0^{2T} dens(u) C(u) du."""
    C = Cmat_factory(T, M); Q = np.zeros((M, M))
    for u, c in atoms: Q += c * C(u)
    if dens is not None:
        ug, uw = NL.leggauss(nu); edges = np.linspace(0, 2 * T, npan + 1)
        for lo, hi in zip(edges[:-1], edges[1:]):
            for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw): Q += dens(u) * w * C(u)
    return Q

def fhat_of(T, M, h, tau):
    """F^(tau) = int F e^{i tau t} dt, F = sum h_k phi_k (quadrature)."""
    xt, wt = NL.leggauss(M + 60); y = T * xt; w = T * wt; F = h @ legb(T, M, y)
    tau = np.atleast_1d(tau)
    return np.array([np.sum(F * w * np.exp(1j * t * y)) for t in tau]), np.array([np.sum(F * w * y * np.exp(1j * t * y)) for t in tau])

def part_BC():
    print("\n=== (B)(C) Galerkin M=%d: lambda_A, b_0 = A + Q_eta, anticoherence of eta and of the quartet, Lemma P" % M)
    out = {}
    for name, T in WINDOWS:
        A, ta, tb = form_x(T, M); Z = null_basis([ta, tb]); AP = Z.T @ A @ Z
        lam, V = np.linalg.eigh(AP); lamA = lam[0]; h = Z @ V[:, 0]
        Qeta = toeplitz_measure(T, M, [(np.log(n), 2 * lp / np.sqrt(n)) for n, lp in contacts(T)], dens=lambda u: -2 * np.exp(u / 2))
        b0 = A + Qeta
        e_full = np.linalg.eigvalsh(Qeta); e_P = np.linalg.eigvalsh(Z.T @ Qeta @ Z); e_b0 = np.linalg.eigvalsh(Z.T @ b0 @ Z)
        fh, fh1 = fhat_of(T, M, h, [GAM1])
        print(f" [{name}] lambda_A = {lamA:+.4e}  lambda_min(b_0|P_T) = {e_b0[0]:+.4f} (n_- = {(e_b0<0).sum()})  "
              f"Q_eta (=-fluct.): spec L^2(I_T) in [{e_full[0]:+.4f}, {e_full[-1]:+.4f}], n_-={(e_full<0).sum()}; "
              f"en P_T in [{e_P[0]:+.4f}, {e_P[-1]:+.4f}], n_-={(e_P<0).sum()}")
        print(f"      h*: |h^(g1)|^2 = {abs(fh[0])**2:.3e}  |int h* t e^{{i g1 t}}|^2 = {abs(fh1[0])**2:.4e}  "
              f"=> delta_A = sqrt(lambda_A/(4|.|^2)) = {np.sqrt(max(lamA,0)/(4*abs(fh1[0])**2)):.3e}")
        for d in DELTAS:
            Qb = toeplitz_measure(T, M, [], dens=lambda u, d=d: 8 * np.cos(GAM1 * u) * np.cosh(d * u))
            eb = np.linalg.eigvalsh(Z.T @ Qb @ Z); ebf = np.linalg.eigvalsh(Qb)
            AM = A + Qb; lamM = np.linalg.eigvalsh(Z.T @ AM @ Z)[0]
            pred = lamA + 4 * abs(fh[0]) ** 2 - 4 * d * d * abs(fh1[0]) ** 2
            print(f"      M1 d={d}: lambda_A^{{M1}} = {lamM:+.4e} (Lema P: {pred:+.4e}; Rayleigh en h*: {h @ AM @ h:+.4e})  "
                  f"quartet Q_b|P_T: lambda_min = {eb[0]:+.4e}, lambda_max = {eb[-1]:+.4f}, n_-={(eb<0).sum()}; on L^2: n_-={(ebf<0).sum()}, lambda_min={ebf[0]:+.4e}  "
                  f"curvature ratio R(dT) = {(1+0.3*(2*d*T)**2)/(1+(2*d*T)**2/6):.6f}")
        out[name] = (T, A, Z, h, lamA)
    return out

# ---------------------------------------------------------------- (D) sampling identity
def part_D(out):
    print("\n=== (D) sampling identity (Poisson): sum v_n c_F(log n) = (1/4T) sum_k |F^(k pi/2T)|^2 P_T(k pi/2T)")
    for name, (T, A, Z, h, lamA) in out.items():
        cs = contacts(T); C = Cmat_factory(T, M)
        Qv = sum(2 * lp / np.sqrt(n) * C(np.log(n)) for n, lp in cs)
        rng = np.random.default_rng(1); hs = [h] + [Z @ rng.standard_normal(M - 2) for _ in range(2)]
        for j, hh in enumerate(hs):
            hh = hh / np.linalg.norm(hh); lhs = hh @ Qv @ hh
            res = []
            for Kmax in (2000, 20000, 200000):
                k = np.arange(0, Kmax + 1); wk = k * np.pi / (2 * T)
                # |F^|^2 por bloques
                f2 = np.concatenate([np.einsum('k,klt,l->t', hh, fhat2(T, M, wk[i:i + 20000]), hh) for i in range(0, len(wk), 20000)])
                P = np.zeros_like(wk)
                for n, lp in cs: P += 2 * lp / np.sqrt(n) * np.cos(wk * np.log(n))
                s = (1 / (4 * T)) * (f2[0] * P[0] + 2 * np.sum(f2[1:] * P[1:]))
                res.append(s)
            tag = 'h*' if j == 0 else f'random.{j}'
            print(f" [{name}] {tag:>8}: direct {lhs:+.8f}   sampling K=2e3/2e4/2e5: {res[0]:+.8f} {res[1]:+.8f} {res[2]:+.8f}")


# ---------------------------------------------------------------- (E) whole form on the Nyquist grid; (F) comb scaling
def part_EF(out):
    from scipy.integrate import quad
    from r043_wh import K
    print("\n=== (E) a_T(F) = (1/4T) sum_k |F^(w_k)|^2 s_T(w_k), s_T = C0 + int_{2T}^oo K + int_0^{2T}(1-cos)K - P_T  (grid w_k = k pi/2T)")
    for name, (T, A, Z, h, lamA) in out.items():
        cs = contacts(T); tail = quad(K, 2 * T, np.inf)[0]
        Kmax = 20000; k = np.arange(0, Kmax + 1); wk = k * np.pi / (2 * T)
        f2 = np.concatenate([np.einsum('k,klt,l->t', h, fhat2(T, M, wk[i:i + 20000]), h) for i in range(0, len(wk), 20000)])
        P = np.zeros_like(wk)
        for n, lp in cs: P += 2 * lp / np.sqrt(n) * np.cos(wk * np.log(n))
        # int_0^{2T} (1 - cos(w u)) K(u) du on the grid (quadrature with smooth (1-cos)/u); only up to k=K1, beyond that ~ log
        K1 = 400
        lev = np.array([quad(lambda u, w=w: (1 - np.cos(w * u)) * K(u), 0, 2 * T, limit=400)[0] for w in wk[:K1 + 1]])
        s = C0 + tail + lev - P[:K1 + 1]
        # tail k > K1: int_0^{2T}(1-cos wu)K ~ log(w) + c: use numerical asymptotics by extrapolating the last points
        c_as = np.mean(lev[-20:] - np.log(wk[K1 - 19:K1 + 1]))
        s_tail = C0 + tail + np.log(wk[K1 + 1:]) + c_as - P[K1 + 1:]
        sfull = np.concatenate([s, s_tail])
        grid = (f2[0] * sfull[0] + 2 * np.sum(f2[1:] * sfull[1:])) / (4 * T)
        neg = [(round(w, 2), round(v, 3)) for w, v in zip(wk[:K1 + 1], s) if v < 0]
        print(f" [{name}] a_T(h*) direct {lamA:+.4e}  grid (K={Kmax}, asymptotic tail from k={K1}) {grid:+.4e};  ||h||^2 = (1/4T) sum |h^(w_k)|^2 = {(f2[0]+2*f2[1:].sum())/(4*T):.6f}")
        print(f"      s_T < 0 on the grid (k<= {K1}): {len(neg)} points: {neg[:12]}{' ...' if len(neg) > 12 else ''}")
        w_neg = [w for w, v in zip(wk[:K1 + 1], s) if v < 0]
        mass_neg = sum(2 * f2[i] * s[i] for i in range(1, K1 + 1) if s[i] < 0) / (4 * T)
        mass_pos = grid - mass_neg
        print(f"      decomposition of a_T(h*) on the grid: negative {mass_neg:+.5f}  positive {mass_pos:+.5f}")
    print("\n=== (F) comb scaling v_n -> (1+eps) v_n (weight class of def:PD): lambda_A and sup bound of C0")
    for name, (T, A, Z, h, lamA) in out.items():
        if name not in ('log 2', '1/2 log3'): continue
        C = Cmat_factory(T, M); Qv = sum(2 * lp / np.sqrt(n) * C(np.log(n)) for n, lp in contacts(T))
        Ep = h @ Qv @ h
        for eps in (1e-6, 1e-5, 1e-3):
            lam = np.linalg.eigvalsh(Z.T @ (A - eps * Qv) @ Z)[0]
            print(f" [{name}] eps={eps:.0e}: lambda_A(1+eps) = {lam:+.4e} (first order {lamA - eps*Ep:+.4e}; sum v_n c_h*(log n) = {Ep:.5f}); |C0 changes| <= eps*sum v_n/(4T) = {eps*sum(2*lp/np.sqrt(n) for n,lp in contacts(T))/(4*T):.2e}")


# ---------------------------------------------------------------- (G) (E_gamma) from R186_050: S_T(gamma) over the adapted family F_T = (1/4 - d^2)[t sin(gamma t) eta_T]
def contacts_full(T):
    """(n, log p) for n = p^k < e^{2T}, smallest-prime-factor sieve (r043.contacts stops at n < 2000)."""
    X = int(np.exp(2 * T)) + 1; spf = np.zeros(X + 1, dtype=np.int64)
    for p in range(2, X + 1):
        if spf[p] == 0:
            spf[p::p][spf[p::p] == 0] = p
    out = []
    for n in range(2, X + 1):
        if np.log(n) >= 2 * T: break
        p = spf[n]; r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, np.log(p)))
    return out

def adapted_family(T, gam, N=None):
    """F_T on a grid; returns t, F, dt. eta = smoothstep C^4 (degree 9) of width w = min(1, T/2)."""
    N = N or int(max(8001, 3200 * T)) | 1
    t = np.linspace(-T, T, N); dt = t[1] - t[0]; w = min(1.0, T / 2)
    x = np.clip((np.abs(t) - (T - w)) / w, 0, 1); sg = np.sign(t) / w
    S = 70 * x**9 - 315 * x**8 + 540 * x**7 - 420 * x**6 + 126 * x**5
    S1 = 630 * x**8 - 2520 * x**7 + 3780 * x**6 - 2520 * x**5 + 630 * x**4
    S2 = 5040 * x**7 - 17640 * x**6 + 22680 * x**5 - 12600 * x**4 + 2520 * x**3
    eta, eta1, eta2 = 1 - S, -S1 * sg, -S2 * sg * sg
    a, a1, a2 = t * np.sin(gam * t), np.sin(gam * t) + gam * t * np.cos(gam * t), 2 * gam * np.cos(gam * t) - gam * gam * t * np.sin(gam * t)
    g = a * eta; g2 = a2 * eta + 2 * a1 * eta1 + a * eta2
    return t, 0.25 * g - g2, dt

def S_T(T, gam, quartets=()):
    """Returns a dict with S_T(gamma) (zeta), main, arch, a_T/||F||^2, and for each quartet (g, d): -Q/||F||^2 (two ways)."""
    from r043_wh import K
    from scipy.integrate import quad
    t, F, dt = adapted_family(T, gam); nF = np.sum(F * F) * dt
    c = np.correlate(F, F, 'full')[len(F) - 1:] * dt           # c_F(u_j), u_j = j dt, j = 0..N-1  (u in [0, 2T])
    u = np.arange(len(c)) * dt
    cs = contacts_full(T); S = sum(2 * lp / np.sqrt(n) * np.interp(np.log(n), u, c) for n, lp in cs) / nF
    main = 2 * np.trapz(np.exp(u / 2) * c, dx=dt) / nF; main2 = -2 * np.trapz(np.exp(-u / 2) * c, dx=dt) / nF   # iguales si F in P_T
    cosh_test = np.trapz(np.cosh(u / 2) * c, dx=dt) / nF
    lev = np.sum(((c[0] - c[1:]) * K(u[1:]))) * dt + c[0] * quad(K, 2 * T, np.inf)[0]
    aT = (C0 * c[0] + lev) / nF - S
    out = dict(S=S, main=main, main2=main2, cosh=cosh_test, aT=aT, arch=aT + S, nF=nF)
    for g, d in quartets:
        Q1 = 8 * np.trapz(np.cos(g * u) * np.cosh(d * u) * c, dx=dt)
        Pc = np.sum(F * np.cosh(d * t) * np.exp(1j * g * t)) * dt; Ps = np.sum(F * np.sinh(d * t) * np.exp(1j * g * t)) * dt
        Q2 = 4 * abs(Pc) ** 2 - 4 * abs(Ps) ** 2
        out[(g, d)] = (-Q1 / nF, -Q2 / nF)
    return out

def part_G():
    from r043_wh import m_arch
    print("\n=== (G) (E_gamma): S_T(gamma) = sum v_n c_{F_T}(log n)/||F_T||^2 over F_T = (1/4 - d^2)[t sin(gamma t) eta_T]; m(gamma) = Re psi(1/4 + i gamma/2) - log pi")
    print("   check at gamma_1: orthogonality to cosh(u/2), main = -2 int c e^{-u/2}, two ways of computing Q (d = 0.1)")
    for name, T in WINDOWS + [('T=2', 2.0), ('T=3', 3.0), ('T=5', 5.0)]:
        r = S_T(T, GAM1, quartets=[(GAM1, 0.01), (GAM1, 0.1)])
        print(f"   [{name:>8}] int c cosh/||F||^2 = {r['cosh']:+.1e}  main = {r['main']:+.5f} / {r['main2']:+.5f}  S_T(g1) = {r['S']:+.5f}  arch_T = {r['arch']:.5f} (m(g1) = {m_arch(GAM1):.5f})  a_T(F_T)/||F||^2 = {r['aT']:+.5f}"
              f"  -Q/||F||^2: d=0.01 {r[(GAM1,0.01)][0]:+.3e}/{r[(GAM1,0.01)][1]:+.3e}; d=0.1 {r[(GAM1,0.1)][0]:+.3e}/{r[(GAM1,0.1)][1]:+.3e}")
    print("   C(T) := sup_gamma [S_T(gamma) - m(gamma)]_+ over gamma in [2, 40] (step 0.25, + gamma_1); and sup of S_T - m, argmax:")
    gams = np.sort(np.concatenate([np.arange(2, 40.01, 0.25), [GAM1]]))
    for name, T in WINDOWS + [('T=1.5', 1.5), ('T=2', 2.0), ('T=3', 3.0), ('T=4', 4.0), ('T=5', 5.0)]:
        vals = {}
        for g in gams:
            r = S_T(T, g, quartets=[(GAM1, 0.01), (GAM1, 0.1)])
            vals[g] = (r['S'] - m_arch(g), r[(GAM1, 0.01)][1], r[(GAM1, 0.1)][1], r['aT'])
        z = np.array([vals[g][0] for g in gams]); i = z.argmax()
        m1 = np.array([vals[g][0] + vals[g][1] for g in gams]); m2 = np.array([vals[g][0] + vals[g][2] for g in gams])
        amin = min(vals[g][3] for g in gams)
        print(f"   [{name:>8}] zeta: C(T) = {max(z.max(),0):.4f} (sup S-m = {z.max():+.4f} en gamma = {gams[i]:.2f}; min_gamma a_T(F_T)/||F||^2 = {amin:+.2e})   "
              f"M1 d=0.01: C = {max(m1.max(),0):.4f} (en {gams[m1.argmax()]:.2f})   M1 d=0.1: C = {max(m2.max(),0):.4f} (en {gams[m2.argmax()]:.2f});  3e^{{2dT}}/(d^2 T) = {3*np.exp(0.2*T)/(0.01*T):.1f}")
    print("   M1 increment at gamma_1, -Q_delta(F_T)/||F_T||^2, large T (Lemma Q only; no comb):")
    for T in [5, 10, 15, 20, 30]:
        row = []
        for d in (0.01, 0.1):
            t, F, dt = adapted_family(T, GAM1); nF = np.sum(F * F) * dt
            Pc = np.sum(F * np.cosh(d * t) * np.exp(1j * GAM1 * t)) * dt; Ps = np.sum(F * np.sinh(d * t) * np.exp(1j * GAM1 * t)) * dt
            row.append((-(4 * abs(Pc) ** 2 - 4 * abs(Ps) ** 2) / nF, 3 * np.exp(2 * d * T) / (d * d * T)))
        print(f"      T={T:>3}: d=0.01: {row[0][0]:+.4e} (3e^{{2dT}}/(d^2T) = {row[0][1]:.3e});  d=0.1: {row[1][0]:+.4e} ({row[1][1]:.3e})")

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'G': part_G()
    else: part_A(); out = part_BC(); part_D(out); part_EF(out); part_G()
