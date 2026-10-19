#!/usr/bin/env python3
"""R186_047 — (L-W) Lemma: coercivity of the complement of component prolates.
SELF-CONTAINED (the constructions of r044_coupling.py are copied and re-verified; nothing is imported from the corpus).

Objects (Paper 47 eq:symbol, eq:form; R186_034 Thm 2.1; R186_044 §2):
  sigma_T = m - sum_{log n<2T} v_n cos(tau log n);  a_T(F) = (1/2pi) int sigma_T |F^|^2  in L^2(I_T), I_T=(-T,T);
  P_T = {int F e^{±t/2} = 0};  Pos = R sigma_+(D) R, Neg = R sigma_-(D) R, a_T = Pos - Neg;  U = {sigma_T<0} = ∪ J_i.
  S_i := R 1_{J_i ∪ -J_i}(D) R;  psi_i^± := top eigenvector of S_i per parity;  V := span{psi_i^±};
  W := P_T ∩ V^⊥  ( = (P_P V)^⊥ ∩ P_T, Lemma 1 of R186_047 ).
Bounds (R186_047):
  Lemma 2 (Neg on W):  Neg|_W ≤ lambda_max(M),  M_ii = s_i·lam1_i,  M_ik = sqrt(s_i s_k)·||S_i^{1/2}S_k^{1/2}||,
          s_i = max_{J_i} sigma_-, lam1_i = second eigenvalue of S_i per parity (max of the two parities),
          ||S_i^{1/2}S_k^{1/2}|| = sqrt(lambda_max(S_i S_k)) ≤ HS(1_{E_k} R 1_{E_i}).
  Lemma 3 (Pos on W):  Pos|_W ≥ ∫_0^∞ (1 - mu_bar(s))^+ ds,  mu_bar(s) ≥ sup_W mu_F({sigma ≤ s}) via the same Gram norm
          over the pieces of {sigma ≤ s} (deflation of S_{J_i} on the pieces containing J_i).
  c_W^expl := Pos_lb - Neg_ub.   Exact values (NUMERICAL) for comparison: lambda_min(A_WW), lambda_min(Pos_WW), ||Neg_WW||.
Usage: python3 r047_LW.py [fast]   (approx. 2-4 min with M=44)
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
np.set_printoptions(linewidth=200, precision=4, suppress=True)

# ------------------------------------------------------------------ symbol (copied from r044, re-verified)
def contacts(T):
    out = []
    for n in range(2, 5000):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, np.log(p)))
    return out

def m_arch(tau): return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)

def sigma_fn(T):
    cs = contacts(T)
    def s(tau):
        tau = np.atleast_1d(np.asarray(tau, float)); v = m_arch(tau)
        for n, lp in cs: v = v - 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
        return v
    return s

def sublevel(sig, level, tmax=300.0, h=2e-3):
    """{tau in [0,tmax): sigma(tau) <= level} as a list of intervals; None if sigma(tmax) <= level (unbounded on the grid)."""
    g = np.arange(0, tmax, h); s = sig(g) - level
    if s[-1] <= 0: return None
    zs = [brentq(lambda t: sig([t])[0] - level, g[i], g[i + 1]) for i in range(len(g) - 1) if s[i] * s[i + 1] < 0]
    pts = [0.0] + zs + [tmax]
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1) if sig([(pts[i] + pts[i + 1]) / 2])[0] - level < 0]

# ------------------------------------------------------------------ Legendre Galerkin (copied from r044)
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=120):
    """(1/2pi) ∫_{E ∪ -E} f |F^|^2 with E = ∪ pieces ⊂ [0,∞) (f even)."""
    xg, wg = NL.leggauss(nq); out = np.zeros((M, M))
    for lo, hi in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        out += np.einsum('klt,t->kl', fhat2(T, M, t), f(t) * w) / np.pi
    return out

def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))

def Cmat_factory(T, M):
    xg, wg = NL.leggauss(M + 1)
    def C(u):
        lo, hi = -T + u, T
        if hi <= lo: return np.zeros((M, M))
        y = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        Mx = (legb(T, M, y) * w) @ legb(T, M, y - u).T; return (Mx + Mx.T) / 2
    return C

def form_x(T, M, nu=64, npan=16):
    C = Cmat_factory(T, M); I = np.eye(M); A = np.zeros((M, M)); ug, uw = NL.leggauss(nu)
    edges = np.linspace(0, 2 * T, npan + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
            A += (I - C(u)) * (K(u) * w)
    A += I * (quad(K, 2 * T, np.inf)[0] + C0)
    for n, lp in contacts(T): A -= 2 * lp / np.sqrt(n) * C(np.log(n))
    xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
    return A, (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2)

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def sym_eigh(A): return np.linalg.eigh((A + A.T) / 2)

# ------------------------------------------------------------------ (L-W) tools
def parity_top(S, M, k=2):
    """per parity (Legendre: even indices = even functions): the k largest eigenvalues and eigenvectors."""
    out = {}
    for p, idx in (('even', np.arange(0, M, 2)), ('odd', np.arange(1, M, 2))):
        lam, V = sym_eigh(S[np.ix_(idx, idx)]); o = np.argsort(lam)[::-1][:k]
        vecs = []
        for j in o:
            v = np.zeros(M); v[idx] = V[:, j]; vecs.append(v)
        out[p] = (lam[o], vecs)
    return out

def hs_cross(T, E1, E2, nq=48):
    """HS norm of 1_{E2 ∪ -E2}(D) R_T 1_{E1 ∪ -E1}(D): kernel sin(T(t-t'))/(pi (t-t')) over E1^± × E2^±."""
    xg, wg = NL.leggauss(nq); tot = 0.0
    for lo1, hi1 in E1:
        t1 = (hi1 + lo1) / 2 + (hi1 - lo1) / 2 * xg; w1 = (hi1 - lo1) / 2 * wg
        for lo2, hi2 in E2:
            t2 = (hi2 + lo2) / 2 + (hi2 - lo2) / 2 * xg; w2 = (hi2 - lo2) / 2 * wg
            for sg1 in (1, -1):
                for sg2 in (1, -1):
                    d = sg1 * t1[:, None] - sg2 * t2[None, :]
                    kern = np.where(np.abs(d) < 1e-12, T / np.pi, np.sin(T * d) / (np.pi * d))
                    tot += np.einsum('i,ij,j->', w1, kern ** 2, w2)
    return np.sqrt(tot)

def traces(T, pieces, nq=200):
    """tr S_E = T|E|/pi and tr(S_E J) = (1/pi) ∫_{E+} sin(2 tau T)/tau dtau (E = ∪ pieces ∪ -pieces); returns (tr_even, tr_odd)."""
    xg, wg = NL.leggauss(nq); tr = 0.0; trJ = 0.0
    for lo, hi in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        tr += 2 * T * (hi - lo) / np.pi; trJ += np.sum(w * np.where(t < 1e-12, 2 * T, np.sin(2 * t * T) / np.maximum(t, 1e-300))) / np.pi
    return (tr + trJ) / 2, (tr - trJ) / 2

def gram_norm(diag, cross):
    """||Σ A_j|| ≤ lambda_max(M), M_jj = ||A_j||, M_jk = ||A_j^{1/2}A_k^{1/2}|| (Gram lemma for operators ≥ 0)."""
    n = len(diag); Mx = np.array(cross, float).copy()
    for j in range(n): Mx[j, j] = diag[j]
    return sym_eigh(Mx)[0][-1] if n else 0.0

def window(T, M, tag):
    sig = sigma_fn(T); A, ta, tb = form_x(T, M); comps = sublevel(sig, 0.0)
    Neg = form_tau(T, M, lambda t: -sig(t), comps, nq=160); Pos = A + Neg; Z = null_basis([ta, tb])
    AP = Z.T @ A @ Z; ev, EV = sym_eigh(AP)
    print(f"[{tag}] T={T:.5f} M={M} #comp={len(comps)} comps={[(round(a,2),round(b,2)) for a,b in comps]}")
    print(f"    lambda_A={ev[0]:+.4e}  lambda_min(Pos|P_T)=c_P={sym_eigh(Z.T@Pos@Z)[0][0]:+.4f}  ||Neg||={sym_eigh(Neg)[0][-1]:.4f}  tr Neg={np.trace(Neg):.4f}")
    return dict(T=T, M=M, A=A, Neg=Neg, Pos=Pos, Z=Z, comps=comps, sig=sig, lamA=ev[0], AP=AP, ta=ta, tb=tb)

def LW(Wd, tag, nlev=36, wtd=False):
    """wtd=False: V = span{psi_i^±} (R186_044). wtd=True: V' = span{psi_i^±, phi_i^±}, phi_i = top of Neg_i per parity (weighted prolate)."""
    T, M, Z, sig, comps = Wd['T'], Wd['M'], Wd['Z'], Wd['sig'], Wd['comps']
    nyq = 0.8 * M / T
    res = [c for c in comps if (c[0] + c[1]) / 2 <= nyq]; far = [c for c in comps if (c[0] + c[1]) / 2 > nyq]
    # --- component prolates (S_i), deflation, data
    Sm, psi, lam0, lam1, smax, Nsh, Nm, phi, nu1, lam1c, lam0s, nu1c = [], [], [], [], [], [], [], [], [], [], [], []
    for lo, hi in res:
        S = form_tau(T, M, lambda t: np.ones_like(t), [(lo, hi)], nq=160); pt = parity_top(S, M)
        Sm.append(S); psi += [pt['even'][1][0], pt['odd'][1][0]]
        trp, tri = traces(T, [(lo, hi)]); lam1c.append(max(trp - pt['even'][0][0], tri - pt['odd'][0][0])); lam0s.append(pt['even'][0][0] + pt['odd'][0][0])
        lam0.append(max(pt['even'][0][0], pt['odd'][0][0])); lam1.append(max(pt['even'][0][1], pt['odd'][0][1]))
        g = np.linspace(lo, hi, 400); smax.append(float(np.max(-sig(g)))); Nsh.append(T * (hi - lo) / np.pi)
        Nn = form_tau(T, M, lambda t: -sig(t), [(lo, hi)], nq=160); pn = parity_top(Nn, M)
        Nm.append(Nn); phi += [pn['even'][1][0], pn['odd'][1][0]]; nu1.append(max(pn['even'][0][1], pn['odd'][0][1]))
        xg3, wg3 = NL.leggauss(200); t3 = (hi + lo) / 2 + (hi - lo) / 2 * xg3; w3 = (hi - lo) / 2 * wg3; sm = -sig(t3)
        trN = 2 * T * np.sum(w3 * sm) / np.pi; trNJ = np.sum(w3 * sm * np.sin(2 * t3 * T) / t3) / np.pi
        nu1c.append(max((trN + trNJ) / 2 - pn['even'][0][0], (trN - trNJ) / 2 - pn['odd'][0][0]))
    n = len(res); Vb = np.array(psi + (phi if wtd else [])).T             # M × 2n (or 4n)
    # Lemma 1: W = P_T ∩ V^⊥  (coordinates in P_T: Z^T V generates (P_P V) in coordinates of P_T)
    Vz = Z.T @ Vb; q, _ = np.linalg.qr(Vz); r = np.linalg.matrix_rank(Vz, tol=1e-12); q = q[:, :r]
    Wc = null_basis(q.T)                                                  # orthonormal basis of W in P_T coords
    Wfull = Z @ Wc                                                        # columns = functions of W in Legendre
    chk = np.max(np.abs(Vb.T @ Wfull)) if n else 0.0
    print(f"  [{tag}] resolved components {n} (center ≤ {nyq:.1f}), far {len(far)}; dim V^P={r}; dim W={Wc.shape[1]};  max|<psi_i, w>| over W = {chk:.1e} (Lemma 1)")
    print(f"      N_i = {np.round(Nsh,3).tolist()}")
    print(f"      lam0_i = {np.round(lam0,4).tolist()}")
    print(f"      lam1_i = {np.round(lam1,4).tolist()}   s_i^max = {np.round(smax,3).tolist()}   nu1_i(Neg_i) = {np.round(nu1,4).tolist()}")
    # --- exact values on W (NUMERICAL)
    AWW = Wfull.T @ Wd['A'] @ Wfull; PWW = Wfull.T @ Wd['Pos'] @ Wfull; NWW = Wfull.T @ Wd['Neg'] @ Wfull
    lamA_W = sym_eigh(AWW)[0][0]; lamP_W = sym_eigh(PWW)[0][0]; nN_W = sym_eigh(NWW)[0][-1]
    # exact Neg per deflated component: ||Σ s_i S̃_i|_W||  and  Σ_i s_i ||S̃_i|_W||
    St = []
    for i, S in enumerate(Sm):
        Sd = S.copy()
        for v in (psi[2 * i], psi[2 * i + 1]):
            Sd -= (v @ S @ v) * np.outer(v, v)
        St.append(Sd)
    exact_sum = sym_eigh(sum(s * Wfull.T @ Sd @ Wfull for s, Sd in zip(smax, St)))[0][-1] if n else 0.0
    neg_tb = sym_eigh(sum(s * Sd for s, Sd in zip(smax, St)))[0][-1] if n else 0.0          # ||Σ s_i S̃_i|| in L^2(I_T)
    SU_t = sum(St) if n else np.zeros((M, M)); muU_W = sym_eigh(Wfull.T @ SU_t @ Wfull)[0][-1]; muU_tb = sym_eigh(SU_t)[0][-1]
    print(f"      NUMERICAL on W: lambda_min(A_WW)={lamA_W:+.4f}  lambda_min(Pos_WW)={lamP_W:+.4f}  ||Neg_WW||={nN_W:.4f}  ||Σ s_i S̃_i|_W||={exact_sum:.4f}  sup_W mu_F(U)={muU_W:.4f}")
    print(f"      time-band data (without Tate): ||Σ s_i S̃_i||={neg_tb:.4f}  ||S̃_U||=sup_{{V^⊥}} mu_F(U)={muU_tb:.4f}")
    # --- Lemma 2: explicit bound of Neg on W
    cross = np.zeros((n, n)); crossHS = np.zeros((n, n))
    for i in range(n):
        for k in range(i + 1, n):
            lm = np.max(np.real(np.linalg.eigvals(Sm[i] @ Sm[k]))); cross[i, k] = cross[k, i] = np.sqrt(max(lm, 0)) * np.sqrt(smax[i] * smax[k])
            h = hs_cross(T, [res[i]], [res[k]]); crossHS[i, k] = crossHS[k, i] = h * np.sqrt(smax[i] * smax[k])
    diag = [s * l for s, l in zip(smax, lam1)]
    neg_cert = sum(s * l for s, l in zip(smax, lam1c))                 # certificate: lam1 ≤ tr_sector - lam0 ≤ tr_sector - lam0^Gal
    print(f"      certificate (per-sector traces): lam1_i ≤ {np.round(lam1c,4).tolist()}  ->  Neg_ub^cert = Σ s_i(tr_sec - lam0^Gal) = {neg_cert:.4f}")
    far_term = sum(float(np.max(-sig(np.linspace(lo, hi, 200)))) * 2 * T * (hi - lo) / np.pi for lo, hi in far)   # ≤ s_i tr S_i
    if far: print(f"      far: {[(round(lo,1),round(hi,1), round(float(np.max(-sig(np.linspace(lo,hi,200)))),3), round(2*T*(hi-lo)/np.pi,3)) for lo,hi in far]} (J_i, s_i, tr S_i)")
    neg_sum = min(sum(diag), neg_tb) + far_term; neg_gram = gram_norm(diag, cross) + far_term; neg_gramHS = gram_norm(diag, crossHS) + far_term
    if wtd:
        neg_w = sum(nu1) + far_term; print(f"      Lemma 2' (V' with weighted prolates): Σ nu1_i = {sum(nu1):.4f} (+ far {far_term:.4f}); certificate Σ(tr_sec Neg_i - nu0^Gal) = {sum(nu1c):.4f}"); neg_sum = min(neg_sum, neg_w)
        neg_cert = min(neg_cert, sum(nu1c))
    print(f"      Lemma 2: Σ s_i lam1_i = {sum(diag):.4f}; cross leaks: exact Gram -> {neg_gram - far_term:.4f}, Gram-HS -> {neg_gramHS - far_term:.4f}; far (s_i tr S_i) = {far_term:.4f}")
    print(f"              Neg_ub = min(sum, Gram) = {min(neg_sum, neg_gram):.4f}   (exact ||Neg_WW|| = {nN_W:.4f}; bound/exact ratio = {min(neg_sum,neg_gram)/nN_W:.2f})")
    # --- Lemma 3: explicit bound of Pos on W by layers
    def mu_bar(level):
        L = sublevel(sig, level)
        if L is None: return 1.0
        resp = [(lo, hi) for lo, hi in L if hi <= nyq]; unres = [(lo, hi) for lo, hi in L if hi > nyq]
        if any(T * 2 * (hi - lo) / np.pi >= 1.0 for lo, hi in unres): return 1.0   # unresolved piece with tr ≥ 1: trivial bound
        pieces = []
        if resp:
            Sp = form_tau(T, M, lambda t: np.ones_like(t), resp, nq=160)            # S_{L_s ∩ resolved} as ONE operator
            for i, (a, b) in enumerate(res):
                if any(a >= lo - 1e-9 and b <= hi + 1e-9 for lo, hi in resp):
                    for v in (psi[2 * i], psi[2 * i + 1]):
                        Sp -= (v @ Sm[i] @ v) * np.outer(v, v)                     # exact deflation of S_{E_i} ⊂ S_{L_s}
            pieces.append((resp, min(1.0, sym_eigh(Sp)[0][-1])))
        for lo, hi in unres: pieces.append(([(lo, hi)], min(1.0, 2 * T * (hi - lo) / np.pi)))
        m = len(pieces); cr = np.zeros((m, m))
        for j in range(m):
            for k in range(j + 1, m):
                cr[j, k] = cr[k, j] = hs_cross(T, pieces[j][0], pieces[k][0])
        return min(1.0, gram_norm([p[1] for p in pieces], cr))
    # --- HS certificate with explicit V (Legendre polynomials): ||(1-Π)S_L(1-Π)||^2 ≤ tr(S_L^2) - 2 tr(Π S_L^2) + tr(Π S_L Π S_L)
    xq, wq = NL.leggauss(400); xs = T * xq; ws = T * wq
    Ebasis = np.linalg.qr(Vb)[0][:, :Vb.shape[1]]                      # ON basis of V in Legendre coordinates (= explicit functions)
    Ex = Ebasis.T @ legb(T, M, xs)                                        # e_j(x) at the nodes
    def mu_bar_hs(level):
        L = sublevel(sig, level)
        if L is None: return 1.0
        xg2, wg2 = NL.leggauss(160); taus, wts = [], []
        for lo, hi in L:
            taus.append((hi + lo) / 2 + (hi - lo) / 2 * xg2); wts.append((hi - lo) / 2 * wg2)
        taus = np.concatenate(taus); wts = np.concatenate(wts)
        E = np.exp(1j * np.outer(taus, xs))                               # e^{i tau x}
        ehat = (Ex * ws) @ E.T                                            # ê_j(tau), dim V × ntau
        Hm = np.real((np.conj(ehat) * wts) @ ehat.T) / np.pi                # <e_j, S_L e_k> = (1/pi) ∫_{L+} Re conj(ê_j) ê_k
        SLe = np.real(((ehat * wts) @ np.conj(E))) / np.pi                # (S_L e_j)(x) = (1/pi) ∫_{L+} Re[ê_j e^{-i tau x}]
        Gm = (SLe * ws) @ SLe.T                                           # <S_L e_j, S_L e_k>
        hs2 = hs_cross(T, L, L, nq=64) ** 2
        val = hs2 - 2 * np.trace(Gm) + np.sum(Hm ** 2)
        return min(1.0, float(np.sqrt(max(float(np.real(val)), 0.0))))
    def mu_bar_cert(level):
        L = sublevel(sig, level)
        if L is None: return 1.0
        tr = 2 * T * sum(hi - lo for lo, hi in L) / np.pi
        defl = sum(lam0s[i] for i, (a, b) in enumerate(res) if any(a >= lo - 1e-9 and b <= hi + 1e-9 for lo, hi in L))
        return min(1.0, tr - defl)
    # levels: integrate (1 - mu_bar)^+ ds until it vanishes
    levels = np.linspace(0.0, 1.5, nlev + 1); vals = []
    for s in levels:
        mb = mu_bar(s); vals.append(max(0.0, 1 - mb))
        if mb >= 1.0 and s > 0: break
    vals = np.array(vals); ls = levels[:len(vals)]
    pos_lb = float(np.sum(np.diff(ls) * vals[1:])) if len(vals) > 1 else 0.0   # right Riemann sum: sup_F mu_F(L_s) is nondecreasing in s
    lv2 = np.linspace(0.0, 1.5, 4 * nlev + 1); v2 = []
    for s_ in lv2:
        mb = mu_bar_cert(s_); v2.append(max(0.0, 1 - mb))
        if mb >= 1.0 and s_ > 0: break
    v2 = np.array(v2); pos_cert = float(np.sum(np.diff(lv2[:len(v2)]) * v2[1:])) if len(v2) > 1 else 0.0
    print(f"      certificate (traces): 1 - mu_bar^cert(0) = {v2[0]:.3f}, Pos_lb^tr = {pos_cert:.4f}")
    lv3 = np.linspace(0.0, 1.5, 2 * nlev + 1); v3 = []
    for s_ in lv3:
        mb = mu_bar_hs(s_); v3.append(max(0.0, 1 - mb))
        if mb >= 1.0 and s_ > 0: break
    v3 = np.array(v3); pos_hs = float(np.sum(np.diff(lv3[:len(v3)]) * v3[1:])) if len(v3) > 1 else 0.0
    print(f"      certificate (HS, explicit V): 1 - mu_bar^HS(s) = {np.round(v3,3).tolist()}")
    print(f"              Pos_lb^HS = {pos_hs:.4f};  c_W^cert = Pos_lb^HS - Neg_ub^cert = {pos_hs - neg_cert - far_term:+.4f}")
    pos_cert = max(pos_cert, pos_hs)
    print(f"      Lemma 3: 1 - mu_bar(s) at s = 0, {ls[1]:.3f}, ...: {np.round(vals,3).tolist()}")
    print(f"              Pos_lb = ∫(1-mu_bar)^+ ds = {pos_lb:.4f}   (exact lambda_min(Pos_WW) = {lamP_W:.4f})")
    cW = pos_lb - min(neg_sum, neg_gram)
    print(f"      ==> c_W^expl = Pos_lb - Neg_ub = {cW:+.4f}   vs  lambda_min(A_WW) = {lamA_W:+.4f}  (CONDITIONAL: lamP_W - Neg_ub = {lamP_W - min(neg_sum, neg_gram):+.4f})")
    return dict(cW=cW, pos_lb=pos_lb, neg_ub=min(neg_sum, neg_gram), lamA_W=lamA_W, lamP_W=lamP_W, nN_W=nN_W, n=n, r=r, pos_cert=pos_cert, neg_cert=neg_cert + far_term, cW_cert=pos_cert - neg_cert - far_term)

if __name__ == '__main__':
    fast = len(sys.argv) > 1 and sys.argv[1] == 'fast'
    out = {}
    for T, nm, M in ((0.5 * np.log(3), '½log3', 44), (np.log(2), 'log2', 44), (0.5 * np.log(5), '½log5', 36 if fast else 112)):
        if fast: M = min(M, 36)
        Wd = window(T, M, nm); out[nm] = LW(Wd, nm)
        print(f"  --- variant V' = V + weighted prolates of Neg_i (dim ≤ 4·#comp)")
        out[nm + " V'"] = LW(Wd, nm + " V'", wtd=True)
    print("\n=== summary (L-W)")
    print(f"{'T':>9s} {'dimV':>5s} {'Pos_lb':>8s} {'Neg_ub':>8s} {'c_W^expl':>9s} | {'Pos^cert':>8s} {'Neg^cert':>8s} {'c_W^cert':>9s} | {'lam_min(Pos_W)':>14s} {'||Neg_W||':>9s} {'lam_min(A_WW)':>13s}")
    for nm, o in out.items():
        print(f"{nm:>9s} {o['r']:5d} {o['pos_lb']:8.4f} {o['neg_ub']:8.4f} {o['cW']:+9.4f} | {o['pos_cert']:8.4f} {o['neg_cert']:8.4f} {o['cW_cert']:+9.4f} | {o['lamP_W']:14.4f} {o['nN_W']:9.4f} {o['lamA_W']:+13.4f}")
