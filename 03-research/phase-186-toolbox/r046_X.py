#!/usr/bin/env python3
"""R186_046 — Theorem X per window: new primes on the negative set U_{T0}.  SELF-CONTAINED (does not import r034/r043;
copies their constructions: Paper 47 eq:symbol / eq:form / prop:negtrace / prop:band).

  sigma_T(tau) = m(tau) - sum_{n: log n < 2T} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi,  v_n = 2 log p / sqrt n
  a_T(F) = (1/2pi) int sigma_T |F^|^2  (F in L^2(I_T), I_T = [-T,T]);  P_T = {F : int F e^{+-t/2} = 0}
  S_T(tau) := sigma_{T0}(tau) - sigma_T(tau) = sum_{2T0 <= log n < 2T} v_n cos(tau log n)       (new primes)
  U0 := {sigma_{T0} < 0} (symmetric; |U0| = two-sided measure = 2|U0^+|),  S_{U0} = R_T 1_{U0}(D) R_T  (Slepian)
  E_eta := span{psi_j : lambda_j(S_{U0}) >= 1 - eta};  identity (1/2pi)int_{U0} S_T|F^|^2 = (1/2pi)int_{U0} sigma_{T0}|F^|^2
         + (1/2pi)int_{U0^c} sigma_T |F^|^2 - a_T(F).
Falsifier M_1: sigma^{M1}_T = sigma_T + bhat_T,  bhat_T(tau) = int_{-2T}^{2T} 4 cos(gamma_1 u) cosh(delta u) cos(tau u) du.

All Galerkin in the orthonormal Legendre basis of degree < M on I_T (x-space form as in r034/r043; x-vs-tau control).
Usage: python3 r046_X.py [M=48] [fast]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693
L3, L2, L5, L7 = 0.5 * np.log(3), np.log(2), 0.5 * np.log(5), 0.5 * np.log(7)
NAME = {L3: '½log3', L2: 'log2', L5: '½log5', L7: '½log7'}

# ------------------------------------------------------------------ symbol
def contacts(T):
    out = []
    for n in range(2, 2000):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, np.log(p)))
    return out

def m_arch(tau): return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)

def bhat(T, tau, g=GAM1, d=0.1):
    a = 2 * T; tau = np.asarray(tau, float); out = np.zeros_like(tau)
    for w in (g + tau, g - tau):
        out += 4 * (d * np.sinh(d * a) * np.cos(w * a) + w * np.cosh(d * a) * np.sin(w * a)) / (d * d + w * w)
    return out

def prime_sum(T0, T):
    """S_T(tau) = sum_{2T0 <= log n < 2T} v_n cos(tau log n)."""
    new = [(n, lp) for n, lp in contacts(T) if np.log(n) >= 2 * T0 - 1e-12]
    def S(tau):
        tau = np.atleast_1d(np.asarray(tau, float)); v = np.zeros_like(tau)
        for n, lp in new: v = v + 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
        return v
    return S, [n for n, _ in new]

def sigma_fn(T, quartet=None):
    cs = contacts(T)
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

# ------------------------------------------------------------------ Legendre basis, forms
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=160):
    """(1/2pi) int_R f |F^|^2 restricted to the pieces (lo,hi) of tau>0 and their mirror images (f even): (1/pi) int_{pieces}."""
    xg, wg = NL.leggauss(nq); out = np.zeros((M, M))
    for lo, hi in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        out += np.einsum('klt,t->kl', fhat2(T, M, t), f(t) * w) / np.pi
    return (out + out.T) / 2

def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))

def form_x(T, M, nu=48, npan=16, quartet=None):
    xg, wg = NL.leggauss(M + 2)
    def C(u):
        lo, hi = -T + u, T
        if hi <= lo: return np.zeros((M, M))
        y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        Mx = (legb(T, M, y) * w) @ legb(T, M, y - u).T; return (Mx + Mx.T) / 2
    I = np.eye(M); A = np.zeros((M, M)); ug, uw = NL.leggauss(nu); edges = np.linspace(0, 2 * T, npan + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
            Cu = C(u); A += (I - Cu) * (K(u) * w)
            if quartet: g, d = quartet; A += Cu * (8 * np.cos(g * u) * np.cosh(d * u) * w)
    A += I * (quad(K, 2 * T, np.inf)[0] + C0)
    for n, lp in contacts(T): A -= 2 * lp / np.sqrt(n) * C(np.log(n))
    xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
    return (A + A.T) / 2, (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2)

def form_tau_full(T, M, sig, L=1500.0):
    edges = np.linspace(0, L, int(L / 0.25) + 1)
    A = form_tau(T, M, sig, list(zip(edges[:-1], edges[1:])), nq=12)
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    tl = quad(lambda t: (np.log(t / 2) - np.log(np.pi)) / (2 * T * T * t * t), L, np.inf)[0] / np.pi
    return A + np.outer(c, c) * np.abs(ph) * tl

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def orth(V):
    q, r = np.linalg.qr(V); keep = np.abs(np.diag(r)) > 1e-10 * np.abs(np.diag(r)).max(); return q[:, keep]

def LW_count(T, comps, alpha):
    """Landau-Widom (R186_042 table): #{lambda_n > alpha} = 2c/pi + pi^-2 log c log((1-alpha)/alpha), c = T·half-width, per
    component J_i ∪ -J_i (two copies: c_i = T|J_i|/2 each).  Returns (total Shannon, total LW prediction)."""
    sh = sum(2 * T * (hi - lo) / np.pi for lo, hi in comps)
    lw = 0.0
    for lo, hi in comps:
        c = T * (hi - lo) / 2
        lw += 2 * (2 * c / np.pi + np.log(max(c, 1.0)) * np.log((1 - alpha) / alpha) / np.pi ** 2)
    return sh, lw

# ------------------------------------------------------------------ window (T0, T)
def analyse(T0, T, M, quartet=None, tag='zeta', etas=(0.5, 0.1), verbose=True):
    sig0, sigT = sigma_fn(T0, quartet), sigma_fn(T, quartet)
    S_at, new = prime_sum(T0, T)
    S = (lambda t: S_at(t) - (bhat(T, t, *quartet) - bhat(T0, t, *quartet))) if quartet else S_at
    comps0, compsT = neg_set(sig0), neg_set(sigT)
    U0p = sum(hi - lo for lo, hi in comps0); UTp = sum(hi - lo for lo, hi in compsT)
    A, ta, tb = form_x(T, M, quartet=quartet); Z = null_basis([ta, tb])
    AP = Z.T @ A @ Z; evA, VA = np.linalg.eigh(AP); lamA = evA[0]; hstar = Z @ VA[:, 0]
    # blocks of the identity over U0
    SU0 = form_tau(T, M, lambda t: np.ones_like(t), comps0)
    Msig0 = form_tau(T, M, sig0, comps0); MS = form_tau(T, M, S, comps0); MsigT_U0 = Msig0 - MS
    Leak = A - MsigT_U0                              # (1/2pi) int_{U0^c} sigma_T |F^|^2  (exact identity)
    lam, Psi = np.linalg.eigh(SU0); idx = np.argsort(lam)[::-1]; lam, Psi = lam[idx], Psi[:, idx]
    out = dict(T0=T0, T=T, new=new, comps0=comps0, compsT=compsT, lamA=lamA, lam=lam)
    if verbose:
        print(f"\n=== [{tag}] T0 = {NAME.get(T0, '%.4f' % T0)} -> T = {NAME.get(T, '%.4f' % T)}   M = {M}   new primes n = {new}")
        print(f"  U0^+ = {[(round(a, 3), round(b, 3)) for a, b in comps0]}  |U0^+| = {U0p:.3f}  N_Sh(U0) = 2T|U0^+|/pi = {2 * T * U0p / np.pi:.3f}")
        print(f"  U_T^+ = {[(round(a, 3), round(b, 3)) for a, b in compsT]}  |U_T^+| = {UTp:.3f}  N_Sh(U_T) = {2 * T * UTp / np.pi:.3f}")
        print(f"  lambda_A(T) = {lamA:+.4e}  (sig. {evA[1]:+.3e}, {evA[2]:+.3e});  n_-(a_T|P_T) = {(evA < 0).sum()}")
        print(f"  Slepian S_U0 in window T: lambda_j = {np.round(lam[:12], 4).tolist()}")
        for al in (0.5, 0.1):
            sh, lw = LW_count(T, comps0, al)
            print(f"    #{{lambda_j > {al}}} = {(lam > al).sum()}   Shannon = {sh:.2f}   Landau-Widom (c>=1 clip) = {lw:.2f}")
        # (3) pointwise arithmetic property per component of U0
        print("  S_T on U0 (pointwise, per component): [mean S_T | min S_T | max S_T || mean sigma_T0 | cancels on average? (S_T <= sigma_T0)]")
        for lo, hi in comps0:
            t = np.linspace(lo, hi, 801); s = S(t); s0 = sig0(t)
            print(f"    J=[{lo:7.3f},{hi:7.3f}] c={(lo + hi) / 2:7.3f}: {s.mean():+7.3f} | {s.min():+7.3f} | {s.max():+7.3f} || {s0.mean():+7.3f} | {'yes' if s.mean() <= s0.mean() else 'NO'}   (sigma_T on J: min {sigT(t).min():+.3f}, max {sigT(t).max():+.3f})")
    # (1)/(3) inequality X on E_eta ∩ P_T
    for eta in etas:
        N = int((lam >= 1 - eta).sum())
        if N == 0: print(f"  eta={eta}: E_eta empty"); continue
        PsiN = Psi[:, :N]; cons = np.array([ta @ PsiN, tb @ PsiN]); cN = null_basis(cons) if N > 2 else np.zeros((N, 0))
        Q = orth(PsiN @ cN) if cN.shape[1] else np.zeros((M, 0))
        if Q.shape[1] == 0:
            print(f"  eta={eta}: N_eta = {N} <= 2: E_eta ∩ P_T = 0 (Tate consumes the directions)"); out[f'c_{eta}'] = None; continue
        AE = Q.T @ A @ Q; ev, V = np.linalg.eigh(AE); f = Q @ V[:, 0]
        conc = f @ SU0 @ f; sS = f @ MS @ f; s0 = f @ Msig0 @ f; lk = f @ Leak @ f
        # complement W = P_T ⊖ (E_eta ∩ P_T), coupling, Schur bound
        PW = Z - Q @ (Q.T @ Z); W = orth(PW)
        AW = W.T @ A @ W; cW = np.linalg.eigvalsh(AW)[0]; AEW = Q.T @ A @ W; nrm = np.linalg.norm(AEW, 2)
        cE = ev[0]; schur = (cE + cW) / 2 - np.sqrt(((cE - cW) / 2) ** 2 + nrm ** 2)
        out[f'c_{eta}'] = cE; out[f'cW_{eta}'] = cW
        if verbose:
            print(f"  eta = {eta}: N_eta = {N}, dim E_eta∩P_T = {Q.shape[1]}:  c_eta = lambda_min(a_T|E∩P) = {cE:+.4e}   (vs lambda_A = {lamA:+.4e}, ratio {cE / lamA if lamA != 0 else np.inf:.2e})")
            print(f"      minimizer on E∩P: conc. in U0 = {conc:.4f};  <S_T>_U0 = {sS:+.4f}  <sigma_T0>_U0 = {s0:+.4f}  leak = (1/2pi)int_{{U0^c}} sigma_T|f^|^2 = {lk:+.4f};  X: {sS:+.4f} <= {s0 + lk:+.4f}  [{'holds' if sS <= s0 + lk + 1e-12 else 'VIOLATED'}]")
            print(f"      complement W (dim {W.shape[1]}): c_W = lambda_min(a_T|W) = {cW:+.4e};  ||a_EW|| = {nrm:.4e};  Schur/Weyl bound for lambda_A >= {schur:+.4e}")
    # (2) negative mass of the global minimizer h* per component of U_T: in U0 vs new
    inU0 = lambda lo, hi: any(abs(lo - a) < 0.3 * (b - a) + 1e-9 and abs(hi - b) < 0.3 * (b - a) + 1e-9 or (a <= (lo + hi) / 2 <= b) for a, b in comps0)
    rows = []
    for lo, hi in compsT:
        Nj = form_tau(T, M, lambda t: -sigT(t), [(lo, hi)]); rows.append(((lo, hi), hstar @ Nj @ hstar, inU0(lo, hi)))
    negU0 = sum(m for _, m, i in rows if i); negNew = sum(m for _, m, i in rows if not i)
    Posh = hstar @ (A + form_tau(T, M, lambda t: -sigT(t), compsT)) @ hstar
    if verbose:
        print(f"  h*_T (global minimizer): Neg(h*) = {negU0 + negNew:.4f} = {negU0:.4f} (components of U_T inside U0) + {negNew:.4f} (NEW components, outside U0);  Pos(h*) = {Posh:.4f}")
        print("      per component: " + ", ".join(f"[{lo:.1f},{hi:.1f}]{'*' if not i else ''}:{m:.4f}" for (lo, hi), m, i in rows) + "   (* = new)")
    out['negU0'], out['negNew'] = negU0, negNew
    # (2) iteration: prolates of the NEW components (U_T \ U0) and of the full U_T, ∩ P_T
    for nm, cs in (('U_T\\U0 (new)', [c for c, _, i in rows if not i]), ('full U_T', compsT)):
        if not cs: continue
        Sx = form_tau(T, M, lambda t: np.ones_like(t), cs); lx, Px = np.linalg.eigh(Sx); ix = np.argsort(lx)[::-1]; lx, Px = lx[ix], Px[:, ix]
        N = int((lx >= 0.5).sum())
        if N <= 2: print(f"  prolates of {nm}: N_0.5 = {N} <= 2"); continue
        PsiN = Px[:, :N]; Q = orth(PsiN @ null_basis(np.array([ta @ PsiN, tb @ PsiN])))
        ev = np.linalg.eigvalsh(Q.T @ A @ Q)
        if verbose: print(f"  prolates of {nm}: lambda_j = {np.round(lx[:6], 3).tolist()}  N_0.5 = {N}, dim ∩P_T = {Q.shape[1]}:  lambda_min(a_T|E_0.5∩P_T) = {ev[0]:+.4e}")
        out['c_' + nm] = ev[0]
    return out

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 48
    fast = 'fast' in sys.argv
    print("=== (0) controls")
    T = L3; Ax, _, _ = form_x(T, 16); At = form_tau_full(T, 16, sigma_fn(T))
    print(f"    x-form vs tau-form (½log3, M=16): max|A_x - A_tau| = {np.abs(Ax - At).max():.2e}  (|A| max {np.abs(Ax).max():.2f})")
    S, new = prime_sum(L3, L5); t0 = 9.06
    print(f"    S_T(0) with T0=½log3, T=½log5: {S(0.0)[0]:+.4f} = sum v_n, n={new};  S_T(9.06) = {S(t0)[0]:+.4f};  sigma_T0(9.06) = {sigma_fn(L3)(t0)[0]:+.4f};  sigma_T0(0) = {sigma_fn(L3)(0.0)[0]:+.4f}")
    num = quad(lambda u: 4 * np.cos(GAM1 * u) * np.cosh(0.1 * u) * np.cos(20.3 * u), -2 * 0.7, 2 * 0.7, limit=400)[0]
    print(f"    bhat: quadrature {num:.8f}  closed form {bhat(0.7, np.array([20.3]), GAM1, 0.1)[0]:.8f}")
    # Weyl: phases of the new primes at the centers 2 pi k / log 2 (prop:align) — average of cos over k
    for p in (3, 5, 7):
        ks = np.arange(1, 100001); print(f"    Weyl: mean_k cos(2 pi k log{p}/log2), k<=1e5: {np.cos(2 * np.pi * ks * np.log(p) / np.log(2)).mean():+.5f}")

    pairs = [(L3, L2), (L3, L5), (L3, L7), (L2, L5), (L2, L7), (L5, L7)]
    if fast: pairs = [(L3, L5)]
    res = {}
    for T0, T in pairs: res[(T0, T)] = analyse(T0, T, M, tag='zeta')
    print("\n=== falsifier M_1 (quartet 1/2 ± 0.1 ± i gamma_1): same primes; its Lambda carries the continuous density 4cos(gamma u)cosh(delta u)")
    for T0, T in ([(L3, L2), (L3, L5)] if not fast else [(L3, L5)]):
        res[('M1', T0, T)] = analyse(T0, T, M, quartet=(GAM1, 0.1), tag='M1 d=0.1')
    print("\n=== summary: c_eta (X over U0, with margin) vs lambda_A(T) vs c_W")
    for k, r in res.items():
        print(f"  {str(k)[:40]:40s} lambda_A={r['lamA']:+.3e}  c_0.5={r.get('c_0.5')}  c_W(0.5)={r.get('cW_0.5')}  c_0.1={r.get('c_0.1')}  Neg(h*): U0 {r['negU0']:.3f} / nuevas {r['negNew']:.3f}")
