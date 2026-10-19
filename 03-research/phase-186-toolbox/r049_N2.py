#!/usr/bin/env python3
r"""R186_049 — Second term of S2: NEW negativity (outside U_{T0}) seen by the OLD prolates (of U_{T0}).
SELF-CONTAINED: copies the definitions of Paper 47 (eq:symbol / eq:form / prop:band / Tate) like r034/r043/r046; imports no results.

  sigma_T(tau) = m(tau) - sum_{log n < 2T} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi,  v_n = 2 log p / sqrt n
  a_T(F) = (1/2pi) int sigma_T |F^|^2,  F in L^2(I_T), I_T = [-T, T];  P_T = {F : int F e^{+-t/2} = 0};  lambda_A = min a_T|P_T.
  U0 = {sigma_{T0} < 0}, U_T = {sigma_T < 0} (tau > 0, symmetric).  Neg^new := R sigma_T^- 1_{U_T \ U0}(D) R  (outside U0),
  Neg^old := R sigma_T^- 1_{U_T ∩ U0}(D) R;  a_T = a^{(U0)} - Neg^new with a^{(U0)} := Pos_T - Neg^old (σ_T with the new
  negativity suppressed).  V0 := span{psi_i^±} (index-0 prolate per parity of S_{E_i}, E_i = ±J_i, J_i component of U0, on I_T),
  V0^P := P_{P_T} V0, Pi0 = projector.  nu := lambda_max(Pi0 Neg^new Pi0) (max Rayleigh quotient over V0^P).
Falsifier M_1: sigma + bhat_T, bhat_T(tau) = int_{-2T}^{2T} 4 cos(gamma_1 u) cosh(delta u) cos(tau u) du.
Galerkin in the orthonormal Legendre basis of degree < M on I_T.   Usage: python3 r049_N2.py [M=48]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693
L3, L2, L5, L7, L9 = 0.5 * np.log(3), np.log(2), 0.5 * np.log(5), 0.5 * np.log(7), np.log(3)
NAME = {L3: '½log3', L2: 'log2', L5: '½log5', L7: '½log7', L9: '½log9'}
def nm(T): return NAME.get(T, '%.3f' % T)

# ------------------------------------------------------------------ symbol (Paper 47 eq:symbol)
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

def interval_minus(A, B):
    """A \\ B for lists of disjoint, ordered intervals (tau > 0)."""
    out = []
    for lo, hi in A:
        cur = [(lo, hi)]
        for blo, bhi in B:
            nxt = []
            for clo, chi in cur:
                if bhi <= clo or blo >= chi: nxt.append((clo, chi)); continue
                if blo > clo: nxt.append((clo, blo))
                if bhi < chi: nxt.append((bhi, chi))
            cur = nxt
        out += [(a, b) for a, b in cur if b - a > 1e-9]
    return out

def interval_and(A, B):
    out = []
    for lo, hi in A:
        for blo, bhi in B:
            a, b = max(lo, blo), min(hi, bhi)
            if b - a > 1e-9: out.append((a, b))
    return out

# ------------------------------------------------------------------ Legendre basis, forms (eq:form, x-form)
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=160):
    """(1/2pi) int f |F^|^2 over the pieces (lo,hi) of tau > 0 and their mirror images (f even) = (1/pi) int_{pieces}."""
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

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def orth(V):
    q, r = np.linalg.qr(V); keep = np.abs(np.diag(r)) > 1e-8; return q[:, keep]

def top_prolates(T, M, comps):
    """psi_i^± (index 0 per parity) of S_{E_i} in L^2(I_T), Legendre basis (parity = parity of the degree)."""
    out = []
    for lo, hi in comps:
        S = form_tau(T, M, lambda t: np.ones_like(t), [(lo, hi)])
        for par in (0, 1):
            idx = np.arange(par, M, 2); ev, V = np.linalg.eigh(S[np.ix_(idx, idx)])
            psi = np.zeros(M); psi[idx] = V[:, -1]; out.append((psi, ev[-1], ev[-2]))
    return out

def supneg(sig, lo, hi):
    g = np.linspace(lo, hi, 400); return max(0.0, float(-sig(g).min()))

# ------------------------------------------------------------------ window (T0, T)
def analyse(T0, T, M, quartet=None, tag='zeta', verbose=True):
    sig0, sigT = sigma_fn(T0, quartet), sigma_fn(T, quartet)
    comps0, compsT = neg_set(sig0), neg_set(sigT)
    new_pieces = interval_minus(compsT, comps0); old_pieces = interval_and(compsT, comps0)
    # classification of each new piece: does the U_T component containing it overlap U0?
    def kind(p):
        c = next(c for c in compsT if c[0] <= p[0] + 1e-9 and p[1] <= c[1] + 1e-9)
        return 'disjoint' if not interval_and([c], comps0) else 'growth'
    kinds = [kind(p) for p in new_pieces]
    A, ta, tb = form_x(T, M, quartet=quartet); Z = null_basis([ta, tb]); AP = Z.T @ A @ Z
    evA, VA = np.linalg.eigh(AP); lamA = evA[0]; h = Z @ VA[:, 0]
    negT = lambda t: np.maximum(-sigT(t), 0.0)
    Nnew = form_tau(T, M, negT, new_pieces) if new_pieces else np.zeros((M, M))
    Nold = form_tau(T, M, negT, old_pieces) if old_pieces else np.zeros((M, M))
    Npieces = [form_tau(T, M, negT, [p]) for p in new_pieces]
    # old prolates and V0^P
    pro = top_prolates(T, M, comps0)
    V0 = np.array([Z @ (Z.T @ psi) for psi, _, _ in pro]).T          # projected onto P_T (M coords)
    Q = orth(V0)                                                       # orthonormal basis of V0^P in M coords (within P_T)
    QP = Z.T @ Q                                                       # P_T coords
    nu = np.linalg.eigvalsh(Q.T @ Nnew @ Q)[-1] if Q.shape[1] else 0.0
    nu_pieces = [np.linalg.eigvalsh(Q.T @ Np @ Q)[-1] for Np in Npieces]
    # «sup × leak» bound: Neg^new <= sum_p s_p S_p  => nu <= lambda_max(Q^T sum s_p S_p Q)
    Sp = [form_tau(T, M, lambda t: np.ones_like(t), [p]) for p in new_pieces]
    sps = [supneg(sigT, *p) for p in new_pieces]
    nu_ub = np.linalg.eigvalsh(Q.T @ sum(s * S for s, S in zip(sps, Sp)) @ Q)[-1] if new_pieces else 0.0
    leak = [1 - l0 for _, l0, _ in pro]                                # 1 - lambda_0 of each old prolate (total leak outside E_i)
    # leak of each old prolate toward the new pieces (sinc)
    leak_new = [max(float(psi @ S @ psi) for psi, _, _ in pro) for S in Sp]
    # h*: how its negativity is distributed
    neg_h_new = float(h @ Nnew @ h); neg_h_old = float(h @ Nold @ h); neg_h_pieces = [float(h @ Np @ h) for Np in Npieces]
    hV = Q @ (Q.T @ h); mass_hV = float(hV @ hV)
    # two exact terms: a = a^{(U0)} - Neg^new on P_T
    Aold = AP + Z.T @ Nnew @ Z; lam_old = np.linalg.eigvalsh(Aold)[0]
    NnewP = Z.T @ Nnew @ Z; norm_new = np.linalg.eigvalsh(NnewP)[-1]
    beta_new = None
    if lam_old > 0:
        Lc = np.linalg.cholesky(Aold); Li = np.linalg.inv(Lc)
        beta_new = np.linalg.eigvalsh(Li @ NnewP @ Li.T)[-1]
    # Schur with V = V0^P
    nP = AP.shape[0]; Wb = null_basis(QP.T.tolist()) if QP.shape[1] else np.eye(nP)
    H = QP.T @ AP @ QP; cE = np.linalg.eigvalsh(H)[0] if H.size else np.nan
    AWW = Wb.T @ AP @ Wb; cW = np.linalg.eigvalsh(AWW)[0]; B = QP.T @ AP @ Wb; kappa = np.linalg.norm(B, 2) if B.size else 0
    nu_cross = np.linalg.norm(Q.T @ Nnew @ (Z @ Wb), 2) if B.size else 0
    rho = None
    if cE > 0 and cW > 0:
        Cm = B @ np.linalg.solve(AWW, B.T); Lh = np.linalg.cholesky(H); Lhi = np.linalg.inv(Lh)
        rho = np.linalg.eigvalsh(Lhi @ Cm @ Lhi.T)[-1]
    Hold = QP.T @ Aold @ QP; cE_old = np.linalg.eigvalsh(Hold)[0] if Hold.size else np.nan
    r = dict(T0=T0, T=T, tag=tag, lamA=lamA, comps0=comps0, compsT=compsT, new_pieces=new_pieces, kinds=kinds, nu=nu,
             nu_pieces=nu_pieces, nu_ub=nu_ub, leak=leak, leak_new=leak_new, sps=sps, neg_h_new=neg_h_new, neg_h_old=neg_h_old,
             neg_h_pieces=neg_h_pieces, mass_hV=mass_hV, lam_old=lam_old, norm_new=norm_new, beta_new=beta_new, cE=cE, cW=cW,
             kappa=kappa, nu_cross=nu_cross, rho=rho, cE_old=cE_old, dimV=Q.shape[1])
    if verbose:
        print(f"\n=== {tag}: T0 = {nm(T0)} -> T = {nm(T)}  (M = {M})   lambda_A(T) = {lamA:.4e}")
        print(f"  U0+ = {[(round(a,3), round(b,3)) for a, b in comps0]}")
        print(f"  U_T+ (#{len(compsT)}) = {[(round(a,2), round(b,2)) for a, b in compsT[:10]]}{' ...' if len(compsT) > 10 else ''}")
        print(f"  new pieces U_T\\U0: " + '; '.join(f"({a:.2f},{b:.2f}) {k} s={s:.2f}" for (a, b), k, s in zip(new_pieces, kinds, sps)))
        print(f"  old prolates: 1-lambda0 = {np.round(leak, 4).tolist()}   dim V0^P = {Q.shape[1]}")
        print(f"  nu = lambda_max(Pi0 Neg^new Pi0) = {nu:.4e}   sup×leak bound = {nu_ub:.4e}   nu_cross = {nu_cross:.4e}")
        print(f"  nu per piece = {['%.2e' % x for x in nu_pieces]}   max leak of an old prolate into the piece = {['%.2e' % x for x in leak_new]}")
        print(f"  h*: Neg in new = {neg_h_new:.4e} (per piece {['%.2e' % x for x in neg_h_pieces]}), Neg in U0 = {neg_h_old:.4e}, mass in V0^P = {mass_hV:.4f}")
        print(f"  two terms: lambda_min(a^(U0)|P_T) = {lam_old:.4e}; ||Neg^new|P_T|| = {norm_new:.4e}; Weyl = {lam_old - norm_new:+.4e}; "
              f"beta_new = {beta_new if beta_new is None else '%.6f' % beta_new}; 1-beta_new = {None if beta_new is None else '%.3e' % (1 - beta_new)}")
        print(f"  Schur with V0^P: c_E = {cE:.4e} (c_E of a^(U0): {cE_old:.4e}), c_W = {cW:.4e}, kappa = {kappa:.3f}, "
              f"kappa^2/(c_E c_W) = {kappa**2 / (cE * cW) if cE > 0 and cW > 0 else float('nan'):.2e}, 1-rho = {None if rho is None else '%.3e' % (1 - rho)}")
    return r

if __name__ == '__main__':
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 48
    np.set_printoptions(precision=4, suppress=True)
    res = []
    print("### zeta: three requested windows + ½log5 -> ½log7")
    for T0, T in [(L3, L5), (L2, L5), (L5, L7), (L3, L2)]:
        res.append(analyse(T0, T, M))
    print("\n### decay in T with T0 = ½log3 fixed (nu, leak of old prolates)")
    scan = []
    for T in [L2, L5, L7, L9, 1.25, 1.4]:
        r = analyse(L3, T, M, verbose=False); scan.append(r)
        print(f"  T = {nm(T):>6}: nu = {r['nu']:.3e}  sup×leak bound = {r['nu_ub']:.3e}  1-lambda0(old) = {np.round(r['leak'], 4).tolist()}  "
              f"max s_p = {max(r['sps']) if r['sps'] else 0:.2f}  #new pieces = {len(r['new_pieces'])}  "
              f"Neg_h*(new) = {r['neg_h_new']:.2e}  lambda_A = {r['lamA']:.2e}  lambda_min a^(U0) = {r['lam_old']:.2e}")
    print("\n### M_1 (quartet at gamma_1): delta = 0.1 and blind regime")
    for T0, T, d in [(L3, L2, 0.1), (L2, L5, 0.1), (L3, L5, 0.1), (L3, L2, 0.01), (L3, L2, 0.03)]:
        res.append(analyse(T0, T, M, quartet=(GAM1, d), tag=f'M1 delta={d}'))
    print("\n### summary")
    print(f"{'window':<34}{'lambda_A':>11}{'nu':>11}{'nu_ub':>11}{'Neg_h*new':>11}{'lam_old':>11}{'||Nnew||':>11}{'1-beta':>11}{'c_E':>11}{'c_W':>11}{'kappa':>8}")
    for r in res:
        print(f"{r['tag'] + ' ' + nm(r['T0']) + '->' + nm(r['T']):<34}{r['lamA']:>11.2e}{r['nu']:>11.2e}{r['nu_ub']:>11.2e}{r['neg_h_new']:>11.2e}"
              f"{r['lam_old']:>11.2e}{r['norm_new']:>11.2e}{(1 - r['beta_new']) if r['beta_new'] is not None else float('nan'):>11.2e}"
              f"{r['cE']:>11.2e}{r['cW']:>11.2e}{r['kappa']:>8.3f}")
