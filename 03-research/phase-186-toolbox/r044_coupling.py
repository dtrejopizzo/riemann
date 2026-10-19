#!/usr/bin/env python3
"""R186_044 — Coupling theory: the rank-#comp condition (C_T), its Schur complement,
D − G (local diagonal vs sinc coupling), ζ vs M_1 at log 2, and structure for T ≤ ½ log 7.
SELF-CONTAINED: does not import r043/r034/r187 (the constructions of r043 are copied and re-verified).

Objects (Paper 47 eq:symbol, eq:form, prop:negtrace, def:PD):
  sigma_T(tau) = m(tau) - sum_{log n < 2T} v_n cos(tau log n);  a_T(F) = (1/2pi) int sigma_T |F^|^2;
  P_T = {int F e^{±t/2} = 0};  Pos = R sigma_+(D) R, Neg = R sigma_-(D) R;  U = {sigma_T < 0} = ∪ J_i.
  psi_i^± := top eigenvector of S_{J_i} = R 1_{±J_i}(D) R in each parity (weighted prolate of index 0);
  V_T := span{psi_i^±};  V_T^P := P_{P_T} V_T;  H_T := matrix of a_T on an orthonormal basis of V_T^P.
  C_T :  H_T ≻ 0.
Usage: python3 r044_coupling.py [fast]
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693
np.set_printoptions(linewidth=200, precision=4, suppress=True)

# ------------------------------------------------------------------ symbol
def contacts(T):
    out = []
    for n in range(2, 5000):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, np.log(p)))
    return out

def m_arch(tau): return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)

def sigma_fn(T, extra=None):
    cs = contacts(T)
    def s(tau):
        tau = np.atleast_1d(np.asarray(tau, float)); v = m_arch(tau)
        for n, lp in cs: v = v - 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
        return v + (extra(tau) if extra else 0.0)
    return s

def neg_set(sig, tmax=300.0, h=2e-3):
    g = np.arange(0, tmax, h); s = sig(g)
    zs = [brentq(lambda t: sig([t])[0], g[i], g[i + 1]) for i in range(len(g) - 1) if s[i] * s[i + 1] < 0]
    pts = [0.0] + zs; assert s[-1] > 0
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1) if sig([(pts[i] + pts[i + 1]) / 2])[0] < 0]

# ------------------------------------------------------------------ orthonormal Legendre basis of I_T
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=120):
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

def form_x(T, M, nu=64, npan=16, quartet=None):
    """A = matrix of a_T; also returns Q = quartet matrix (0 if none) and the two Tate functionals."""
    C = Cmat_factory(T, M); I = np.eye(M); A = np.zeros((M, M)); Q = np.zeros((M, M)); ug, uw = NL.leggauss(nu)
    edges = np.linspace(0, 2 * T, npan + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
            Cu = C(u); A += (I - Cu) * (K(u) * w)
            if quartet: g, d = quartet; Q += Cu * (8 * np.cos(g * u) * np.cosh(d * u) * w)
    tail = quad(K, 2 * T, np.inf)[0]
    A += I * (tail + C0)
    for n, lp in contacts(T): A -= 2 * lp / np.sqrt(n) * C(np.log(n))
    xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
    return A + Q, Q, (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2)

def bhat(T, tau, g, d):
    a = 2 * T; tau = np.asarray(tau, float); out = np.zeros_like(tau)
    for w in (g + tau, g - tau):
        out += 4 * (d * np.sinh(d * a) * np.cos(w * a) + w * np.cosh(d * a) * np.sin(w * a)) / (d * d + w * w)
    return out

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def pencil(N, P):
    L = np.linalg.cholesky(P); Li = np.linalg.inv(L); B = Li @ N @ Li.T
    return np.sort(np.linalg.eigvalsh((B + B.T) / 2))[::-1]

# ------------------------------------------------------------------ window
def window(T, M, quartet=None, tag=''):
    sig = sigma_fn(T, None if quartet is None else (lambda tau: bhat(T, tau, *quartet)))
    A, Q, ta, tb = form_x(T, M, quartet=quartet); comps = neg_set(sig)
    Neg = form_tau(T, M, lambda t: -sig(t), comps, nq=160); Pos = A + Neg; Z = null_basis([ta, tb])
    AP = Z.T @ A @ Z; ev, EV = np.linalg.eigh(AP)
    print(f"[{tag}] T={T:.5f} M={M} #comp={len(comps)} comps={[(round(a,2),round(b,2)) for a,b in comps]}")
    print(f"    lambda_A={ev[0]:+.4e}  n_-(P_T)={(ev<0).sum()}  1-beta_max={1-pencil(Z.T@Neg@Z, Z.T@Pos@Z)[0]:+.4e}  tr Neg={np.trace(Neg):.4f}")
    return dict(T=T, M=M, A=A, Q=Q, Neg=Neg, Pos=Pos, Z=Z, comps=comps, sig=sig, lamA=ev[0], hstar=Z @ EV[:, 0], AP=AP)

def comp_modes(T, M, comps):
    """per resolved component (center <= 0.8 M/T, Legendre Nyquist): top eigenvector of S_{J_i} in each parity."""
    modes = []
    for lo, hi in comps:
        if (lo + hi) / 2 > 0.8 * M / T: continue
        S = form_tau(T, M, lambda t: np.ones_like(t), [(lo, hi)], nq=160)
        lam, V = np.linalg.eigh(S); idx = np.argsort(lam)[::-1]; got = {}
        for j in idx[:6]:
            p = 'even' if np.sum(V[0::2, j] ** 2) > 0.5 else 'odd'
            if p not in got: got[p] = (lam[j], V[:, j])
        for p in ('even', 'odd'):
            if p in got: modes.append(((lo, hi), p, got[p][0], got[p][1]))
    return modes

def centroid(T, M, v, taus=None):
    taus = np.linspace(0, 120, 2401) if taus is None else taus
    F2 = np.einsum('k,klt,l->t', v, fhat2(T, M, taus), v); F2 = np.maximum(F2, 0)
    return np.trapz(taus * F2, taus) / np.trapz(F2, taus)

# ------------------------------------------------------------------ (1) C_T and Schur
def schur_analysis(W, modes, tag):
    A, Z, T, M = W['A'], W['Z'], W['T'], W['M']
    V = np.array([m[3] for m in modes]).T; labels = [f"[{m[0][0]:.1f},{m[0][1]:.1f}]{m[1][0]}" for m in modes]
    Vz = Z.T @ V                                   # coordinates in P_T of the projections
    q, _ = np.linalg.qr(Vz); r = np.linalg.matrix_rank(Vz, tol=1e-8); q = q[:, :r]
    AP = W['AP']; n = AP.shape[0]
    # orthogonal complement of V^P within P_T
    H = q.T @ AP @ q; lamH = np.linalg.eigvalsh(H)[0]
    hz = Z.T @ W['hstar']; massV = np.sum((q.T @ hz) ** 2); cen_h = centroid(T, M, W['hstar'])
    if r >= n:
        print(f"  [{tag}] dim V^P={r} = dim P_T={n}: no complement (M insufficient to separate); lambda_min(H_T)={lamH:+.4e}")
        return dict(q=q, H=H, labels=labels, V=V, lamH=lamH, lamS=lamH, lamWW=np.nan, massV=massV, r=r, rho=np.nan)
    Wc = null_basis(q.T)
    A_WW = Wc.T @ AP @ Wc; A_VW = q.T @ AP @ Wc
    lamWW = np.linalg.eigvalsh(A_WW)[0]
    S = H - A_VW @ np.linalg.solve(A_WW, A_VW.T); lamS = np.linalg.eigvalsh(S)[0]
    corr = lamH - lamS
    ew, EW = np.linalg.eigh(A_WW); wmin = Z @ (Wc @ EW[:, 0]); cen_w = centroid(T, M, wmin)
    sv = np.linalg.svd(A_VW, compute_uv=False)[0]
    Cm = A_VW @ np.linalg.solve(A_WW, A_VW.T)                 # Schur correction (⪰ 0 if A_WW ≻ 0)
    rho = pencil(Cm, H)[0] if lamH > 0 else np.nan            # max C(u)/H(u) over V^P
    es, ES = np.linalg.eigh(S); us = ES[:, 0]
    resid = hz - q @ (q.T @ hz); nres = np.linalg.norm(resid)
    cen_res = centroid(T, M, Z @ resid) if nres > 1e-12 else np.nan
    a_res = (resid @ AP @ resid) / nres**2 if nres > 1e-12 else np.nan
    print(f"      rho_T = max_V C(u)/H_T(u) = {rho:.10f}  (1-rho={1-rho:+.3e});  at u*=argmin S_V: H_T(u*)={us@H@us:+.4e}  C(u*)={us@Cm@us:+.4e}  ||C||={np.linalg.eigvalsh(Cm)[-1]:.4f}")
    print(f"      residual h*-P_V h*: norm^2={nres**2:.2e}  spectral centroid={cen_res:.2f}  a_T(res)/||res||^2={a_res:+.4e}  (A_WW ≥ {lamWW:.3f})")
    print(f"  [{tag}] dim V^P={r} (of {len(modes)} modes; dim P_T={n})  lambda_min(H_T)={lamH:+.4e}  C_T {'PASSES' if lamH>0 else 'FAILS'}")
    print(f"      lambda_min(Schur S_V)={lamS:+.4e}  vs lambda_A={W['lamA']:+.4e}  (S_V ≥ lambda_A: {lamS>=W['lamA']-1e-12})  correction lamH-lamS={corr:+.4e}  (relative {corr/abs(lamH):.3f})")
    print(f"      complement: lambda_min(A_WW)={lamWW:+.4e}  ||A_VW||={sv:.4e}  bound ||A_VW||^2/lam_min(A_WW)={sv**2/lamWW:+.4e}  spectral centroid of the minimizer of A_WW={cen_w:.2f}")
    print(f"      head h*: mass in V^P={massV:.4f} (outside {1-massV:.4f}); spectral centroid of h*={cen_h:.2f}; a_T(P_V h*)/||P_V h*||^2={(q.T@hz)@H@(q.T@hz)/max(massV,1e-300):+.4e}")
    return dict(q=q, H=H, labels=labels, V=V, lamH=lamH, lamS=lamS, lamWW=lamWW, massV=massV, r=r, rho=rho)

# ------------------------------------------------------------------ (2) D − G
def DG_analysis(W, modes, tag, Aform=None, show=True):
    """H unprojected in the mode basis (nearly orthonormal): H_ij = <psi_i, A psi_j>; D=diag, G=-offdiag.
       Also returns the version projected onto P_T (with the two Tate relations)."""
    A = W['A'] if Aform is None else Aform; Z = W['Z']; T = W['T']; M = W['M']
    V = np.array([m[3] for m in modes]).T; labels = [f"[{m[0][0]:.1f},{m[0][1]:.1f}]{m[1][0]}" for m in modes]
    Hu = V.T @ A @ V; Gr = V.T @ V
    D = np.diag(np.diag(Hu)); G = -(Hu - D)
    # same parity only: modes of different parity are orthogonal and A commutes with reflection
    ev_u = np.sort(np.linalg.eigvals(np.linalg.solve(Gr, Hu)).real)
    Vz = Z.T @ V; q, _ = np.linalg.qr(Vz); r = np.linalg.matrix_rank(Vz, tol=1e-8); q = q[:, :r]
    Hp = q.T @ (Z.T @ A @ Z) @ q; lamHp = np.linalg.eigvalsh(Hp)[0]
    # Tate: how much H changes due to the projection (norm of the part of V outside P_T)
    tate_loss = [1 - np.sum(Vz[:, j] ** 2) for j in range(V.shape[1])]
    if show:
        print(f"  [{tag}] modes: {labels}")
        print(f"      D_ii (local, without Tate) = {np.round(np.diag(Hu),4).tolist()}")
        print(f"      mass of each mode outside P_T (Tate) = {np.round(tate_loss,4).tolist()}")
        print(f"      G (coupling, −offdiag; rows/cols = modes):")
        for i in range(len(labels)):
            print(f"        {labels[i]:>13s} " + ' '.join(f"{G[i,j]:+.4f}" if i != j else "   .   " for j in range(len(labels))))
        print(f"      lambda_min(H without Tate, gen.)={ev_u[0]:+.4e}  (#neg={np.sum(ev_u<0)})   lambda_min(H_T with Tate)={lamHp:+.4e}")
    return dict(Hu=Hu, D=D, G=G, Gr=Gr, labels=labels, V=V, Hp=Hp, lamHp=lamHp, q=q, ev_u=ev_u)

def sign_structure(G, labels, D, tag):
    """Does a signature s exist with s_i s_j G_ij ≥ 0 (G entrywise nonnegative after signs ⇒ H = D − G is a Z-matrix)?
       If so: H ≻ 0 ⟺ H is an M-matrix ⟺ ∃ x > 0 with Hx > 0. Checked via a sign graph (cycle consistency)."""
    n = len(labels); s = np.zeros(n, int); ok = True; thr = 1e-6
    for comp_start in range(n):
        if s[comp_start] != 0: continue
        s[comp_start] = 1; stack = [comp_start]
        while stack:
            i = stack.pop()
            for j in range(n):
                if i == j or abs(G[i, j]) < thr: continue
                want = s[i] * (1 if G[i, j] > 0 else -1)
                if s[j] == 0: s[j] = want; stack.append(j)
                elif s[j] != want: ok = False
    H = D - G; Hs = (s[:, None] * s[None, :]) * H if ok else H
    # M-matrix test: x = H^{-1} 1 > 0 ?
    msg = ''
    if ok:
        try:
            x = np.linalg.solve(Hs, np.ones(n)); msg = f"  M-matrix test: H^-1·1 > 0 ? {bool(np.all(x>0))} (min={x.min():+.3e})"
        except np.linalg.LinAlgError: msg = ' singular'
    print(f"  [{tag}] consistent signature (G ≃ entrywise ≥ 0 after signs): {ok}{msg}; signs={s.tolist()}")
    return ok, s

# ------------------------------------------------------------------ (3) sinc structure and phases
def sinc_structure(W, modes, R, tag):
    T, M, sig = W['T'], W['M'], W['sig']
    V = R['V']; Gr = R['Gr']; G = R['G']; labels = R['labels']
    cen = [ (m[0][0] + m[0][1]) / 2 for m in modes ]
    print(f"  [{tag}] g_ij=<psi_i,psi_j> vs sinc(T(s_i−s_j)) (same parity) and G_ij/g_ij:")
    rows = []
    for i in range(len(modes)):
        for j in range(i + 1, len(modes)):
            if modes[i][1] != modes[j][1]: continue
            d = cen[j] - cen[i]; sc = np.sinc(T * d / np.pi); ratio = G[i, j] / Gr[i, j] if abs(Gr[i, j]) > 1e-4 else np.nan
            rows.append((labels[i], labels[j], T * d, Gr[i, j], sc, G[i, j], ratio))
    for r in rows: print(f"      {r[0]:>13s} {r[1]:>13s}  T·dist={r[2]:5.2f}  g_ij={r[3]:+.4f}  sinc={r[4]:+.4f}  G_ij={r[5]:+.4f}  G/g={r[6]:+.3f}")
    # comb phases at the component centers: cos(s_i log n)
    cs = contacts(T)
    print(f"      comb phases at the centers s_i (cos(s_i log n), n ∈ N_T) and sigma_-(s_i), slopes at ∂J:")
    for (lo, hi), p, lam, v in modes:
        if p != 'even': continue
        s0 = (lo + hi) / 2; ph = {n: float(np.cos(s0 * np.log(n))) for n, lp in cs}
        h = 1e-4; sl = [float((sig([x + h])[0] - sig([x - h])[0]) / (2 * h)) for x in ((hi,) if lo == 0.0 else (lo, hi))]
        print(f"        s_i={s0:6.2f} N_J={T*(hi-lo)/np.pi:.2f} sigma(s_i)={sig([s0])[0]:+.3f} m={m_arch(s0):+.3f} phases={{{', '.join(f'{n}:{x:+.2f}' for n,x in ph.items())}}} sigma'(∂J)={np.round(sl,2).tolist()}")

# ------------------------------------------------------------------ main
if __name__ == '__main__':
    fast = len(sys.argv) > 1 and sys.argv[1] == 'fast'
    M = 30 if fast else 40
    print("=== (0) control: closed-form bhat vs quadrature")
    T0, tau0, d0 = 0.7, 20.3, 0.1
    num = quad(lambda u: 4 * np.cos(GAM1 * u) * np.cosh(d0 * u) * np.cos(tau0 * u), -2 * T0, 2 * T0, limit=400)[0]
    print(f"    quadrature {num:.10f}  closed form {bhat(T0, np.array([tau0]), GAM1, d0)[0]:.10f}")

    print("\n=== (1) C_T, Schur and head at ½log3, log2, ½log5 (ζ) and M_1 (log 2, δ=0.1 and 0.001)")
    Ws, Rs = {}, {}
    for T, nm, qt in ((0.5 * np.log(3), 'l3', None), (np.log(2), 'l2', None), (0.5 * np.log(5), 'l5', None),
                      (np.log(2), 'M1 d=0.1', (GAM1, 0.1)), (np.log(2), 'M1 d=0.001', (GAM1, 0.001))):
        W = window(T, M, quartet=qt, tag=nm); modes = comp_modes(T, M, W['comps'])
        Ws[nm] = (W, modes); Rs[nm] = schur_analysis(W, modes, nm)

    print("\n=== (2) D − G: ζ vs M_1 at log 2, entry by entry")
    Wz, mz = Ws['l2']; Wm, mm = Ws['M1 d=0.1']
    Rz = DG_analysis(Wz, mz, 'zeta log2'); Rm = DG_analysis(Wm, mm, 'M1 d=0.1')
    print("  --- separation: form of M_1 on the MODES OF ζ (change of form without change of basis)")
    Rzm = DG_analysis(Wz, mz, 'A(M1) on zeta modes', Aform=Wm['A'])
    Qv = mz and (np.array([m[3] for m in mz]).T)
    Qmat = Qv.T @ Wm['Q'] @ Qv
    print("  --- quartet Q restricted to the modes of ζ: Q_ij = <psi_i, Q psi_j> (D part = diag, G part = −offdiag)")
    for i in range(len(Rz['labels'])):
        print(f"        {Rz['labels'][i]:>13s} " + ' '.join(f"{Qmat[i,j]:+.4f}" for j in range(len(Rz['labels']))))
    dQ = np.diag(Qmat); offQ = Qmat - np.diag(dQ)
    print(f"      ||diag Q||_inf={np.abs(dQ).max():.4f}  ||offdiag Q||_2={np.linalg.norm(offQ,2):.4f}  lambda_min(Q|V)={np.linalg.eigvalsh(Qmat)[0]:+.4f}  lambda_min(diag Q)={dQ.min():+.4f}")
    # how much of the change in lambda_min(H_T) comes from D and from G: exchange tests
    Hz, Hm = Rz['Hp'], Rzm['Hp']           # same basis q (zeta modes), ζ and M_1 forms
    print(f"      lambda_min(H_T): zeta={Rz['lamHp']:+.4e}; M1 form on zeta modes={Rzm['lamHp']:+.4e}; M1 on M1 modes={Rm['lamHp']:+.4e}")
    Dz, Dm = np.diag(np.diag(Hz)), np.diag(np.diag(Hm))
    print(f"      exchange (basis q of ζ modes, with Tate): D(ζ)−G(M1): {np.linalg.eigvalsh(Dz + (Hm - Dm))[0]:+.4e}   D(M1)−G(ζ): {np.linalg.eigvalsh(Dm + (Hz - Dz))[0]:+.4e}")
    print(f"      diag H_T zeta ={np.round(np.diag(Hz),4).tolist()}")
    print(f"      diag H_T M1   ={np.round(np.diag(Hm),4).tolist()}")
    print(f"      ||offdiag zeta||_2={np.linalg.norm(Hz-Dz,2):.4f}  ||offdiag M1||_2={np.linalg.norm(Hm-Dm,2):.4f}  ||offdiag(M1−zeta)||_2={np.linalg.norm((Hm-Dm)-(Hz-Dz),2):.4f}")
    # negative eigenmode of H_T(M1): mode composition
    ev, EV = np.linalg.eigh(Hm); u = EV[:, 0]
    print(f"      minimum vector of H_T(M1 on zeta modes): lambda={ev[0]:+.4e}, weight^2 per mode={np.round(u**2,3).tolist()}")
    evz, EVz = np.linalg.eigh(Hz); uz = EVz[:, 0]
    print(f"      minimum vector of H_T(ζ): lambda={evz[0]:+.4e}, weight^2 per mode={np.round(uz**2,3).tolist()}")
    print(f"      form of M1 on the minimizer of H_T(ζ): {uz@Hm@uz:+.4e};  form of ζ on the minimizer of H_T(M1): {u@Hz@u:+.4e}")
    print("  --- Lemma Q: quartet = 4|Phi_c|^2 - 4|Phi_s|^2, Phi_c=int F cosh(dt) e^{i g t}, Phi_s=int F sinh(dt) e^{i g t} (exact rank (2,2))")
    T2 = np.log(2); Mq = Wz['M']; xt, wt = NL.leggauss(Mq + 40); y = T2 * xt; w = T2 * wt; Fb = legb(T2, Mq, y)
    for dd in (0.1, 0.001):
        cc = (Fb * w) @ (np.cosh(dd * y) * np.cos(GAM1 * y)); cs_ = (Fb * w) @ (np.cosh(dd * y) * np.sin(GAM1 * y))
        sc = (Fb * w) @ (np.sinh(dd * y) * np.cos(GAM1 * y)); ss = (Fb * w) @ (np.sinh(dd * y) * np.sin(GAM1 * y))
        Qrec = 4 * (np.outer(cc, cc) + np.outer(cs_, cs_)) - 4 * (np.outer(sc, sc) + np.outer(ss, ss))
        Qmat_full = Wm['Q'] if dd == 0.1 else Ws['M1 d=0.001'][0]['Q']
        print(f"      delta={dd}: max|Q_Galerkin - Q_rank(2,2)| = {np.abs(Qmat_full - Qrec).max():.2e}  (|Q| max {np.abs(Qmat_full).max():.3f});  |Phi_s|^2 scale: ||sc||^2+||ss||^2={sc@sc+ss@ss:.3e}, ||cc||^2+||cs||^2={cc@cc+cs_@cs_:.3e}")
        # rank-2 Krein over V^P (basis q of zeta modes, with Tate): min_{u ⊥ c} H_T(zeta)(u) - 4|<s,u>|^2 < 0 ?
        q = Rz['q']; Zq = Wz['Z'] @ q
        cv = np.array([Zq.T @ cc, Zq.T @ cs_]); sv_ = np.array([Zq.T @ sc, Zq.T @ ss])
        Hq = Rz['Hp']; Hplus = Hq + 4 * cv.T @ cv                      # H_T(zeta) + positive part
        Kmat = 4 * sv_ @ np.linalg.solve(Hplus, sv_.T)                  # Krein: eigenvalues of the pencil (4 s s^T, H+)
        kev = np.linalg.eigvalsh(Kmat)
        print(f"      delta={dd}: rank-2 Krein on V^P: eigenvalues of 4 S^T H_+^{{-1}} S = {np.round(kev,6).tolist()}  -> H_T(M1)|V ≻ 0 ⟺ max < 1: {kev.max()<1}  (direct λ_min={np.linalg.eigvalsh(Hplus - 4*sv_.T@sv_)[0]:+.3e})")
        # who does the work: the positive part 4|Phi_c|^2 (restriction) or H_T(zeta)?  Without the positive part:
        kev0 = np.linalg.eigvalsh(4 * sv_ @ np.linalg.solve(Hq, sv_.T))
        print(f"               without the positive part (pencil (4 s s^T, H_T(zeta))): max = {kev0.max():.4f};  with it: {kev.max():.4f}")
    print("  --- sign structure (Z-matrix / M-matrix) of H (without Tate, eigenmodes)")
    sign_structure(Rz['G'], Rz['labels'], Rz['D'], 'zeta log2'); sign_structure(Rm['G'], Rm['labels'], Rm['D'], 'M1 d=0.1')
    sign_structure(Rzm['G'], Rzm['labels'], Rzm['D'], 'A(M1) zeta modes')
    print("  --- sinc and phases, log 2 (ζ and M1)")
    sinc_structure(Wz, mz, Rz, 'zeta log2'); sinc_structure(Wm, mm, Rm, 'M1 d=0.1')
    # where is the mass of Q? bhat symbol at the centers
    print(f"      bhat(s_i) (quartet symbol at the centers): {[(round((m[0][0]+m[0][1])/2,1), round(float(bhat(np.log(2), np.array([(m[0][0]+m[0][1])/2]), GAM1, 0.1)[0]),3)) for m in mz if m[1]=='even']}")

    summary = []
    print("\n=== (3) structure in T: C_T, Schur, sinc and phases up to ½log7")
    Tlist = [(0.5 * np.log(3), 'l3', M), (np.log(2), 'l2', M), (0.5 * np.log(5), 'l5', M), (0.9, 'T=0.9', 50 if not fast else 36), (0.5 * np.log(7), 'l7', 56 if not fast else 40)]
    for T, nm, MM in Tlist:
        if nm in Ws: W, modes = Ws[nm]
        else:
            W = window(T, MM, tag=nm); modes = comp_modes(T, MM, W['comps']); Ws[nm] = (W, modes)
            Rs[nm] = schur_analysis(W, modes, nm)
        R = DG_analysis(W, modes, nm, show=(nm in ('l5', 'l7')))
        sign_structure(R['G'], R['labels'], R['D'], nm)
        if nm in ('l5', 'l7'): sinc_structure(W, modes, R, nm)
        # law: lambda_min(H_T) vs lambda_A vs Schur
        summary.append((nm, T, W['lamA'], Rs[nm]['lamS'], Rs[nm]['lamH'], Rs[nm]['lamWW'], Rs[nm]['massV'], Rs[nm]['r'], Rs[nm]['rho'], len(W['comps'])))
        print(f"  [{nm}] SUMMARY: lambda_A={W['lamA']:+.3e}  lambda_min(S_V)={Rs[nm]['lamS']:+.3e}  lambda_min(H_T)={Rs[nm]['lamH']:+.3e}  lam_min(A_WW)={Rs[nm]['lamWW']:+.3e}  h* mass in V={Rs[nm]['massV']:.3f}  dim V^P={Rs[nm]['r']}")

    print("\n=== FINAL TABLE (ζ): T | #comp | dim V^P | lambda_A (double; noise < 1e-13) | lambda_min(S_V) | lambda_min(H_T) | 1-rho_T | lam_min(A_WW) | h* mass in V")
    for nm, T, lA, lS, lH, lW, mV, r, rho, nc in summary:
        print(f"    {nm:>6s} T={T:.4f} #comp={nc:2d} dimV={r:2d}  lamA={lA:+.3e}  lamS={lS:+.3e}  lamH={lH:+.3e}  1-rho={1-rho:+.3e}  lamWW={lW:.3f}  h*inV={mV:.4f}")

    print("\n=== (4) critical delta of the M_1 falsifier via rank-2 Krein (Lemma Q): C_T (on V^P) vs lambda_A (on P_T)")
    print("    Q_delta = 4|Phi_c|^2 - 4|Phi_s|^2; |Phi_s|^2 = delta^2 |int F t e^{i g t}|^2 (1+O(delta^2)): delta_c := delta at which max spec(4 S^T H_+^{-1} S) = 1")
    for nm in ('l3', 'l2', 'l5'):
        W, modes = Ws[nm]; T = W['T']; Mq = W['M']; Z = W['Z']; AP = W['AP']
        xt, wt = NL.leggauss(Mq + 40); y = T * xt; w = T * wt; Fb = legb(T, Mq, y)
        dd = 1e-3
        cc = (Fb * w) @ (np.cosh(dd * y) * np.cos(GAM1 * y)); cs_ = (Fb * w) @ (np.cosh(dd * y) * np.sin(GAM1 * y))
        sc = (Fb * w) @ (np.sinh(dd * y) * np.cos(GAM1 * y)); ss = (Fb * w) @ (np.sinh(dd * y) * np.sin(GAM1 * y))
        q = Rs[nm]['q']; Zq = Z @ q
        for lab, B, Hb in (('V^P (C_T)', Zq, Rs[nm]['H']), ('P_T (lambda_A)', Z, AP)):
            cv = np.array([B.T @ cc, B.T @ cs_]); sv_ = np.array([B.T @ sc, B.T @ ss])
            Hplus = Hb + 4 * cv.T @ cv
            kmax = np.linalg.eigvalsh(4 * sv_ @ np.linalg.solve(Hplus, sv_.T)).max()
            print(f"    [{nm}] {lab:>16s}: max Krein at delta=1e-3 = {kmax:.4e}  -> delta_c ≈ {dd/np.sqrt(kmax):.4e}")

    print("\n=== (5) blind regime delta_A < delta < delta_V: which direction and which block carry the sign? (V := P_P V, index 0; W := complement in P_T)")
    def quartet_functionals(T, Mq, dd):
        xt, wt = NL.leggauss(Mq + 40); y = T * xt; w = T * wt; Fb = legb(T, Mq, y)
        cc = (Fb * w) @ (np.cosh(dd * y) * np.cos(GAM1 * y)); cs_ = (Fb * w) @ (np.cosh(dd * y) * np.sin(GAM1 * y))
        sc = (Fb * w) @ (np.sinh(dd * y) * np.cos(GAM1 * y)); ss = (Fb * w) @ (np.sinh(dd * y) * np.sin(GAM1 * y))
        return cc, cs_, sc, ss
    for nm, dlist in (('l2', (0.01, 0.03)), ('l5', (1e-4, 1e-3))):
        W0, modes0 = Ws[nm]; T = W0['T']; Mq = W0['M']; Z0 = W0['Z']; q0 = Rs[nm]['q']; AP0 = W0['AP']; n = AP0.shape[0]
        Wc0 = null_basis(q0.T)
        h0 = Z0.T @ W0['hstar']; hV0, hW0 = q0 @ (q0.T @ h0), Wc0 @ (Wc0.T @ h0)
        print(f"  [{nm}] ζ: lambda_A={W0['lamA']:+.4e}; h* = h_V + h_⊥ with ||h_⊥||^2={hW0@hW0:.2e};  a(h_V)={hV0@AP0@hV0:+.4e}  2a(h_V,h_⊥)={2*hV0@AP0@hW0:+.4e}  a(h_⊥)={hW0@AP0@hW0:+.4e}")
        for dd in dlist:
            cc, cs_, sc, ss = quartet_functionals(T, Mq, dd)
            Wd = window(T, Mq, quartet=(GAM1, dd), tag=f'{nm} M1 d={dd}')
            # same basis (ζ modes; U changes little) to compare blocks
            Zd = Wd['Z']; APd = Zd.T @ Wd['A'] @ Zd            # Tate is the same (does not depend on the quartet): Zd == Z0 up to sign
            hd = Zd.T @ Wd['hstar']; hVd, hWd = q0 @ (q0.T @ hd), Wc0 @ (Wc0.T @ hd)
            ovl = abs(hd @ h0)
            # Lemma Q functionals on h_V and h_⊥ (of h* for ζ and for M1)
            def fun(hv, hw):
                Phc = [ (Z0 @ hv) @ cc + 1j * (Z0 @ hv) @ cs_, (Z0 @ hw) @ cc + 1j * (Z0 @ hw) @ cs_ ]
                Phs = [ (Z0 @ hv) @ sc + 1j * (Z0 @ hv) @ ss, (Z0 @ hw) @ sc + 1j * (Z0 @ hw) @ ss ]
                return Phc, Phs
            Phc0, Phs0 = fun(hV0, hW0); Phcd, Phsd = fun(hVd, hWd)
            pred = W0['lamA'] + 4 * abs(Phc0[0] + Phc0[1])**2 - 4 * abs(Phs0[0] + Phs0[1])**2
            print(f"    delta={dd}: lambda_A(M1)={Wd['lamA']:+.4e}  1st-order prediction lambda_A + 4|Phi_c(h*)|^2 - 4|Phi_s(h*)|^2 = {pred:+.4e}   |<h*(M1),h*(ζ)>|={ovl:.6f}")
            print(f"        on h*(ζ):  Phi_c(h_V)={Phc0[0]:+.3e}  Phi_c(h_⊥)={Phc0[1]:+.3e}  (sum={Phc0[0]+Phc0[1]:+.2e});  Phi_s(h_V)={Phs0[0]:+.3e}  Phi_s(h_⊥)={Phs0[1]:+.3e}  (sum={Phs0[0]+Phs0[1]:+.2e})")
            print(f"        on h*(M1): Phi_c(h_V)={Phcd[0]:+.3e}  Phi_c(h_⊥)={Phcd[1]:+.3e};  Phi_s(h_V)={Phsd[0]:+.3e}  Phi_s(h_⊥)={Phsd[1]:+.3e}")
            print(f"        energy of h*(M1): ||h_⊥||^2={hWd@hWd:.2e}  a_M1(h_V)={hVd@APd@hVd:+.4e}  2a_M1(h_V,h_⊥)={2*hVd@APd@hWd:+.4e}  a_M1(h_⊥)={hWd@APd@hWd:+.4e}  (mass of h*(M1) in V={1-hWd@hWd:.5f})")
            # blocks: change in H (VV), A_VW, A_WW and in the Schur correction at u* of ζ
            H0 = q0.T @ AP0 @ q0; Hd = q0.T @ APd @ q0
            VW0 = q0.T @ AP0 @ Wc0; VWd = q0.T @ APd @ Wc0; WW0 = Wc0.T @ AP0 @ Wc0; WWd = Wc0.T @ APd @ Wc0
            C0_ = VW0 @ np.linalg.solve(WW0, VW0.T); Cd = VWd @ np.linalg.solve(WWd, VWd.T)
            S0 = H0 - C0_; Sd = Hd - Cd; es0, ES0 = np.linalg.eigh(S0); us = ES0[:, 0]
            print(f"        blocks: lambda_min(H_T): {np.linalg.eigvalsh(H0)[0]:+.3e} -> {np.linalg.eigvalsh(Hd)[0]:+.3e};  ||ΔA_VW||={np.linalg.norm(VWd-VW0,2):.3e};  lam_min(A_WW): {np.linalg.eigvalsh(WW0)[0]:.3f} -> {np.linalg.eigvalsh(WWd)[0]:.3f};  lambda_min(S_V): {es0[0]:+.3e} -> {np.linalg.eigvalsh(Sd)[0]:+.3e} (= lambda_A(M1)? {abs(np.linalg.eigvalsh(Sd)[0]-Wd['lamA'])<1e-9})")
            print(f"        at u*=argmin S_V(ζ): ΔH(u*)={us@(Hd-H0)@us:+.3e}  −ΔC(u*)={-us@(Cd-C0_)@us:+.3e}  sum ΔS(u*)={us@(Sd-S0)@us:+.3e}  (λ_A(M1)−λ_A(ζ)={Wd['lamA']-W0['lamA']:+.3e})")
        # 1st-order delta_A: lambda_A = 4 delta^2 |int h* t e^{i g t}|^2  (Phi_s ≈ delta * int h* t e^{i g t})
        cc, cs_, sc, ss = quartet_functionals(T, Mq, 1e-3)
        b2 = abs((Z0 @ h0) @ sc + 1j * (Z0 @ h0) @ ss)**2 / 1e-6
        print(f"  [{nm}] 1st order: |int h* t e^{{i g1 t}}|^2 = {b2:.4e}, |h*^(g1)|^2 = {abs((Z0@h0)@cc + 1j*(Z0@h0)@cs_)**2:.3e}  -> delta_A ≈ sqrt(lambda_A/(4 b^2)) = {np.sqrt(W0['lamA']/(4*b2)):.3e}")
