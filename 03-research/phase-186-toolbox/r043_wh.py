#!/usr/bin/env python3
"""R186_043 — Sign route in the truncated Wiener-Hopf: model M0 (one sub-Shannon interval), M1 (several),
transfer to sigma_T and falsifier M_1 (quartet off the line).  SELF-CONTAINED: does not import r034/r042/r187.

Definitions (Paper 47 eq:symbol, eq:form, lem:roughEF, prop:negtrace):
  sigma_T(tau) = m(tau) - sum_{n: log n < 2T} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi, v_n = 2 log p / sqrt n
  a_T(F) = (1/2pi) int sigma_T |F^|^2 ;  P_T = {int F e^{+-t/2} = 0};  Pos = R sigma_+(D) R, Neg = R sigma_-(D) R.
Two independent constructions of a_T in the orthonormal Legendre basis of I_T:
  (x) x-space: a_T(F) = C0||F||^2 + int_0^{2T} (||F||^2 - C_F(u)) K(u) du + ||F||^2 int_{2T}^oo K - sum v_n C_F(log n),
      K(u) = 2 e^{-u/2}/(1 - e^{-2u}),  C_F(u) = int F(t)F(t-u) dt  (derived again below, numerical control in 'tau');
  (tau) tau-space: (1/pi) int_0^L sigma phi^_k phi^_l + analytic tail (control only, precision ~1e-7).
Usage: python3 r043_wh.py            (all; ~3 min)
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import spherical_jn, digamma
from scipy.optimize import brentq
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693

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

def sigma_fn(T, extra=None):
    cs = contacts(T)
    def s(tau):
        tau = np.atleast_1d(np.asarray(tau, float)); v = m_arch(tau)
        for n, lp in cs: v = v - 2 * lp / np.sqrt(n) * np.cos(tau * np.log(n))
        return v + (extra(tau) if extra else 0.0)
    return s

def neg_set(sig, tmax=250.0, h=2e-3):
    g = np.arange(0, tmax, h); s = sig(g)
    zs = [brentq(lambda t: sig([t])[0], g[i], g[i + 1]) for i in range(len(g) - 1) if s[i] * s[i + 1] < 0]
    pts = [0.0] + zs; assert s[-1] > 0
    return [(pts[i], pts[i + 1]) for i in range(len(pts) - 1) if sig([(pts[i] + pts[i + 1]) / 2])[0] < 0]

# ------------------------------------------------------------------ Legendre basis
def legb(T, M, y):
    u = np.asarray(y) / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def fhat2(T, M, tau):
    """Re phi^_k conj phi^_l (tau) = 2T sqrt((2k+1)(2l+1)) Re(i^{l-k}) j_k j_l"""
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); J = np.array([spherical_jn(k, np.asarray(tau) * T) for k in range(M)])
    ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    return np.einsum('k,l,kl,kt,lt->klt', c, c, ph, J, J)

def form_tau(T, M, f, pieces, nq=120):
    """(1/pi) int f phi^ phi^ over pieces [(lo,hi)] (f callable, support inside)."""
    xg, wg = NL.leggauss(nq); out = np.zeros((M, M))
    for lo, hi in pieces:
        t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
        out += np.einsum('klt,t->kl', fhat2(T, M, t), f(t) * w) / np.pi
    return out

# ------------------------------------------------------------------ x-space form (self-derived)
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
    """A = matrix of a_T (+ optional quartet (gamma, delta): + int_{-2T}^{2T} c_F(u) 4cos(gamma u)cosh(delta u) du)."""
    C = Cmat_factory(T, M); I = np.eye(M); A = np.zeros((M, M)); ug, uw = NL.leggauss(nu)
    edges = np.linspace(0, 2 * T, npan + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, w in zip((hi + lo) / 2 + (hi - lo) / 2 * ug, (hi - lo) / 2 * uw):
            Cu = C(u); A += (I - Cu) * (K(u) * w)
            if quartet: g, d = quartet; A += Cu * (8 * np.cos(g * u) * np.cosh(d * u) * w)   # 2 int_0^{2T}: c_F even
    tail = quad(K, 2 * T, np.inf)[0]
    A += I * (tail + C0)
    for n, lp in contacts(T): A -= 2 * lp / np.sqrt(n) * C(np.log(n))
    xt, wt = NL.leggauss(M + 40); y = T * xt; w = T * wt; F = legb(T, M, y)
    return A, (F * w) @ np.exp(y / 2), (F * w) @ np.exp(-y / 2)

def form_tau_full(T, M, L=1500.0):
    """control: (1/pi) int_0^L sigma phi^ phi^ + tail with m ~ log(tau/2) and j_k j_l ~ cos((k-l)pi/2)/(2 (tau T)^2) (non-oscillatory)."""
    sig = sigma_fn(T); edges = np.linspace(0, L, int(L / 0.25) + 1)
    A = form_tau(T, M, sig, list(zip(edges[:-1], edges[1:])), nq=12)
    c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
    tl = quad(lambda t: (np.log(t / 2) - np.log(np.pi)) / (2 * T * T * t * t), L, np.inf)[0] / np.pi
    return A + np.outer(c, c) * np.abs(ph) * tl      # j_k j_l ~ cos((k-l)pi/2)/(2x^2): the phase factor appears twice

def null_basis(rows):
    _, _, Vt = np.linalg.svd(np.array(rows)); return Vt[len(rows):].T

def pencil(N, P):
    L = np.linalg.cholesky(P); Li = np.linalg.inv(L); B = Li @ N @ Li.T
    return np.sort(np.linalg.eigvalsh((B + B.T) / 2))[::-1]

# ------------------------------------------------------------------ real window
def window(T, M, quartet=None, tag=''):
    sig = sigma_fn(T, None if quartet is None else (lambda tau: bhat(T, tau, *quartet)))
    A, ta, tb = form_x(T, M, quartet=quartet); comps = neg_set(sig)
    Neg = form_tau(T, M, lambda t: -sig(t), comps, nq=160); Pos = A + Neg; Z = null_basis([ta, tb])
    AP, NP, PP = Z.T @ A @ Z, Z.T @ Neg @ Z, Z.T @ Pos @ Z
    ev = np.linalg.eigvalsh(AP); beta = pencil(NP, PP)
    print(f"[{tag}] T={T:.5f} M={M} comps={[(round(a,3),round(b,3)) for a,b in comps]} |U+|={sum(b-a for a,b in comps):.3f}")
    print(f"    lambda_A={ev[0]:+.4e} (sig. {ev[1]:+.3e}) n_-(P_T)={(ev<0).sum()}  1-beta_j={np.round(1-beta[:4],14).tolist()}  #beta>1={(beta>1).sum()}  tr Neg={np.trace(Neg):.4f} vs (2T/2pi)int sigma_-={2*T/np.pi*sum(quad(lambda t:-sig([t])[0],a,b,limit=200)[0] for a,b in comps):.4f}")
    return dict(A=A, Neg=Neg, Pos=Pos, Z=Z, comps=comps, sig=sig, lamA=ev[0], beta=beta)

def bhat(T, tau, g, d):
    """int_{-2T}^{2T} 4 cos(g u) cosh(d u) cos(tau u) du  (closed form; verified by quadrature below)"""
    a = 2 * T; tau = np.asarray(tau, float); out = np.zeros_like(tau)
    for w in (g + tau, g - tau):
        out += 4 * (d * np.sinh(d * a) * np.cos(w * a) + w * np.cosh(d * a) * np.sin(w * a)) / (d * d + w * w)
    return out

# ------------------------------------------------------------------ component analysis (M0/M1 on a given sigma)
def comp_modes(T, M, comps):
    """per component J_i: top eigenpair of S_{J_i ∪ -J_i} in each parity (weighted prolate of index 0, modulated)."""
    modes = []
    for lo, hi in comps:
        S = form_tau(T, M, lambda t: np.ones_like(t), [(lo, hi)], nq=160)
        lam, V = np.linalg.eigh(S); idx = np.argsort(lam)[::-1]
        par = lambda v: np.sum(v[0::2] ** 2)            # even mass (even Legendre)
        got = {}
        for j in idx[:6]:
            p = 'even' if par(V[:, j]) > 0.5 else 'odd'
            if p not in got: got[p] = (lam[j], V[:, j])
        modes.append(((lo, hi), got, lam[idx[:4]]))
    return modes

def span_test(W, tag, modes=None):
    T, M = None, W['A'].shape[0]
    comps, Z, A, Neg, Pos, sig = W['comps'], W['Z'], W['A'], W['Neg'], W['Pos'], W['sig']
    if modes is None: modes = comp_modes(W['T'], M, comps)
    cols, labels, nus, ps = [], [], [], []
    for (lo, hi), got, lam4 in modes:
        for p, (l0, v) in got.items():
            cols.append(v); labels.append(f"[{lo:.1f},{hi:.1f}]{p[0]}")
            nus.append(v @ Neg @ v); ps.append(v @ Pos @ v)
    V = np.array(cols).T; Vp = Z @ (Z.T @ V)                   # projection onto P_T
    q, _ = np.linalg.qr(Vp); r = np.linalg.matrix_rank(Vp); q = q[:, :r]
    b = pencil(q.T @ Neg @ q, q.T @ Pos @ q); lam_sp = np.linalg.eigvalsh(q.T @ A @ q)[0]
    G = V.T @ Pos @ V; Nn = V.T @ Neg @ V; Gr = V.T @ V
    print(f"  [{tag}] per-component modes (unprojected): nu_i=<v,Neg v>={np.round(nus,4).tolist()}")
    print(f"      p_i=<v,Pos v>={np.round(ps,4).tolist()}   local margin p_i-nu_i={np.round(np.array(ps)-np.array(nus),4).tolist()}")
    off = G - np.diag(np.diag(G)); offN = Nn - np.diag(np.diag(Nn))
    print(f"      interference: max|G_ij| (i≠j) = {np.abs(off).max():.4f}, max|N_ij| = {np.abs(offN).max():.4f}, max|<v_i,v_j>| = {np.abs(Gr-np.diag(np.diag(Gr))).max():.4f}")
    print(f"      unprojected pencil (diag nu, G): 1-beta_max = {1-pencil(Nn, G)[0]:+.4e};  on P_T∩span (dim {r}): 1-beta_max|span = {1-b[0]:+.4e}  lambda_min(a|span) = {lam_sp:+.4e}  vs lambda_A = {W['lamA']:+.4e}")
    return dict(labels=labels, nu=nus, p=ps, G=G, N=Nn, V=V)

# ------------------------------------------------------------------ synthetic M0
def model_M0(T, M, s0, w, a, bfun, label):
    """sigma = bfun(tau) outside J=(s0-w,s0+w) (and its mirror), -a inside. All in tau-space (bfun bounded)."""
    L = 400.0; J = (s0 - w, s0 + w)
    edges = sorted(set([0.0, J[0], J[1]] + list(np.linspace(0, L, 801))))
    pcs = [(x, y) for x, y in zip(edges[:-1], edges[1:]) if not (x >= J[0] - 1e-12 and y <= J[1] + 1e-12)]
    Pos = form_tau(T, M, bfun, pcs, nq=24); Neg = form_tau(T, M, lambda t: a * np.ones_like(t), [J], nq=80)
    SJ = form_tau(T, M, lambda t: np.ones_like(t), [J], nq=80)
    lam, V = np.linalg.eigh(SJ); idx = np.argsort(lam)[::-1]; l0, l1 = lam[idx[0]], lam[idx[1]]
    res = {}
    for j in idx[:2]:
        psi = V[:, j]; nu = psi @ Neg @ psi; p = psi @ Pos @ psi
        Pi = np.linalg.solve(Pos, psi); krein = nu * (psi @ Pi)
        var = psi @ Pos @ Pos @ psi - p * p; cP = np.linalg.eigvalsh(Pos)[0]
        res[j] = (nu, p, krein, var, cP)
    beta = pencil(Neg, Pos); c = T * w
    # sinc^2: p_sinc = (T/pi) int_{J^c} b sinc^2(T(tau-s0)) dtau ; nu_sinc = (T/pi) a int_J sinc^2
    sinc2 = lambda t: np.sinc(T * (t - s0) / np.pi) ** 2
    p_sinc = T / np.pi * sum(quad(lambda t: bfun(np.array([t]))[0] * sinc2(t), x, y, limit=100)[0] for x, y in pcs if y <= 60)
    nu_sinc = T / np.pi * a * quad(sinc2, J[0], J[1])[0]
    j0, j1 = idx[0], idx[1]
    print(f"  M0 {label}: c=Tw={c:.3f} N_J=2c/pi={2*c/np.pi:.3f}  lam0={l0:.5f} lam1={l1:.2e} (lam1/lam0={l1/l0:.2e})  1-beta_max EXACT={1-beta[0]:+.5f} #beta>1={(beta>1).sum()}")
    for j, nm in ((j0, 'mode0'), (j1, 'mode1')):
        nu, p, kr, var, cP = res[j]
        print(f"     {nm}: nu={nu:.5f} p=<psi,Pos psi>={p:.5f}  rank-1 Krein beta={kr:.5f} (1-beta={1-kr:+.5f})  necessary p-nu={p-nu:+.5f}  sufficient p-Var/c_P-nu={p-var/cP-nu:+.5f} (Var={var:.3e}, c_P={cP:.4f})")
    print(f"     sinc^2: nu_sinc={nu_sinc:.5f} p_sinc={p_sinc:.5f}  sinc margin={p_sinc-nu_sinc:+.5f};  a|J|T/pi={a*2*w*T/np.pi:.5f}")
    return 1 - beta[0], res[j0]

if __name__ == '__main__':
    fast = len(sys.argv) > 1 and sys.argv[1] == 'fast'
    print("=== (0) controls: closed-form bhat vs quadrature; tail K")
    T0 = 0.7; tau0 = 20.3; d0 = 0.1
    num = quad(lambda u: 4 * np.cos(GAM1 * u) * np.cosh(d0 * u) * np.cos(tau0 * u), -2 * T0, 2 * T0, limit=400)[0]
    print(f"    bhat: cuadratura {num:.10f}  cerrada {bhat(T0, np.array([tau0]), GAM1, d0)[0]:.10f}")
    print(f"    int_{{2T}}^oo K (T=1/2 log3) = {quad(K, np.log(3), np.inf)[0]:.10f}  vs log(coth(T/2)) + pi - 2 atan(e^T) = {np.log(1/np.tanh(np.log(3)/4)) + np.pi - 2*np.arctan(np.sqrt(3)):.10f}")

    print("\n=== (1) x-form vs tau-form (control of the self-derived construction), 1/2 log 3, M=16")
    T = 0.5 * np.log(3); A, ta, tb = form_x(T, 16); At = form_tau_full(T, 16)
    print(f"    max|A_x - A_tau| = {np.abs(A - At).max():.2e}   (|A| max {np.abs(A).max():.2f})")

    print("\n=== (2) real windows (self-derived code), compare with R186_034: 1/2log3: lambda_A=9.486e-4, 1-beta=4.23e-3; 1/2log5: 3.859e-12, 1.72e-11")
    Ws = {}
    for T, nm in ((0.5 * np.log(3), 'l3'), (0.5 * np.log(5), 'l5')):
        for M in ((30, 40) if not fast else (30,)):
            W = window(T, M, tag=nm); W['T'] = T; Ws[(nm, M)] = W

    print("\n=== (3) synthetic M0 lemma: T=0.8, J=(3-w,3+w)")
    T = 0.8; M = 40
    for w, a, lab, bf in ((0.3, 2.0, 'step b=1', lambda t: np.ones_like(t)),
                           (0.3, 2.0, 'slope b=0.5+min(d,20)', lambda t: 0.5 + np.minimum(np.abs(np.abs(t) - 3) - 0.3, 20).clip(0)),
                           (0.3, 2.0, 'pure slope b=min(d,20)', lambda t: np.minimum(np.abs(np.abs(t) - 3) - 0.3, 20).clip(0)),
                           (0.6, 1.0, 'step b=1 (w=0.6)', lambda t: np.ones_like(t)),
                           (0.6, 1.0, 'slope b=0.5+d (w=0.6)', lambda t: 0.5 + np.minimum(np.abs(np.abs(t) - 3) - 0.6, 20).clip(0))):
        model_M0(T, M, 3.0, w, a, bf, lab)
    print("   sweep over a (step b=1, w=0.3): exact sign vs conditions")
    for a in (1.0, 2.0, 3.0, 4.0, 5.0):
        model_M0(T, M, 3.0, 0.3, a, lambda t: np.ones_like(t), f'a={a}')

    print("\n=== (3b) pure slope b=b1·min(d,Dcap): kappa := beta_max/(a w T^2/b1)")
    for Dcap in (5.0, 20.0, 80.0):
        for (Tt, w) in ((0.5, 0.2), (0.8, 0.1), (0.8, 0.3), (1.2, 0.2), (1.6, 0.1)):
            s0 = 8.0; a = 1.0; b1 = 1.0; Mm = 40
            bf = lambda t, w=w, Dcap=Dcap: b1 * np.minimum(np.abs(np.abs(t) - s0) - w, Dcap).clip(0)
            L = 400.0; J = (s0 - w, s0 + w); edges = sorted(set([0.0, J[0], J[1]] + list(np.linspace(0, L, 801))))
            pcs = [(x, y) for x, y in zip(edges[:-1], edges[1:]) if not (x >= J[0] - 1e-12 and y <= J[1] + 1e-12)]
            Pos = form_tau(Tt, Mm, bf, pcs, nq=24); Neg = form_tau(Tt, Mm, lambda t: a * np.ones_like(t), [J], nq=80)
            bmax = pencil(Neg, Pos)[0]
            print(f"   Dcap={Dcap:4.0f} T={Tt} w={w} c=Tw={Tt*w:.2f}: beta_max={bmax:.5f}  kappa={bmax/(a*w*Tt**2/b1):.4f}")
    print("\n=== (4) synthetic M1: two intervals at distance D, step b=1, a=2, w=0.3; interference G_12 vs sinc(TD)")
    for D in (1.0, 2.0, 4.0, 8.0):
        J1, J2 = (3 - 0.3, 3 + 0.3), (3 + D - 0.3, 3 + D + 0.3); L = 400.0
        edges = sorted(set([0.0, *J1, *J2] + list(np.linspace(0, L, 801))))
        inJ = lambda x, y: any(x >= j[0] - 1e-12 and y <= j[1] + 1e-12 for j in (J1, J2))
        pcs = [(x, y) for x, y in zip(edges[:-1], edges[1:]) if not inJ(x, y)]
        Pos = form_tau(T, M, lambda t: np.ones_like(t), pcs, nq=24); Neg = form_tau(T, M, lambda t: 2 * np.ones_like(t), [J1, J2], nq=80)
        vs, ls = [], []
        for J in (J1, J2):
            S = form_tau(T, M, lambda t: np.ones_like(t), [J], nq=80); lam, V = np.linalg.eigh(S); idx = np.argsort(lam)[::-1]
            for p in ('even', 'odd'):
                j = next(j for j in idx[:6] if (np.sum(V[0::2, j] ** 2) > 0.5) == (p == 'even')); vs.append(V[:, j]); ls.append(lam[j])
        V = np.array(vs).T; G = V.T @ Pos @ V; Nn = V.T @ Neg @ V; g = V.T @ V; ls = np.array(ls)
        pred = (1 - ls[:, None] - ls[None, :]) * g; np.fill_diagonal(pred, 1 - ls)   # Pos = 1 - S_1 - S_2 (step)
        ger = min(1 - Nn[i, i] / (G[i, i] - sum(abs(G[i, j]) for j in range(4) if j != i)) for i in range(4))
        print(f"   D={D}: TD={T*D:.2f} sinc(TD)={np.sinc(T*D/np.pi):+.4f}  lam_i={np.round(ls,4).tolist()}  g_ij (same parity)={g[0,2]:+.4f},{g[1,3]:+.4f}  G_ij={G[0,2]:+.4f},{G[1,3]:+.4f} pred (1-lam_i-lam_j)g_ij={pred[0,2]:+.4f},{pred[1,3]:+.4f}  max|G-pred|={np.abs(G-pred).max():.1e}")
        print(f"        1-beta exact={1-pencil(Neg,Pos)[0]:+.5f}  span(4)={1-pencil(Nn,G)[0]:+.5f}  decoupled min_i(1-nu_i/G_ii)={min(1-Nn[i,i]/G[i,i] for i in range(4)):+.5f}  Gershgorin={ger:+.5f}")

    print("\n=== (5) real sigma_T: per-component condition and pencil on the span (1/2 log 3, 1/2 log 5)")
    for key in (('l3', 40 if not fast else 30), ('l5', 40 if not fast else 30)):
        W = Ws[key]; T = W['T']; M = W['A'].shape[0]
        modes = comp_modes(T, M, W['comps'])
        R = span_test(W, key[0], modes)
        # archimedean/prime split of p_i and of nu_i (over U^c and U)
        cs = contacts(T); sig = W['sig']; comps = W['comps']; tl = comps[-1][1]
        Uc = [(comps[i][1], comps[i + 1][0]) for i in range(len(comps) - 1)] + [(tl, 400.0)]
        mpos = form_tau(T, M, lambda t: m_arch(t), Uc, nq=60)
        c = np.sqrt((2 * np.arange(M) + 1) * 2 * T); ph = np.real(1j ** (np.arange(M)[None, :] - np.arange(M)[:, None]))
        mpos += np.outer(c, c) * np.abs(ph) * quad(lambda t: (np.log(t / 2) - np.log(np.pi)) / (2 * T * T * t * t), 400.0, np.inf)[0] / np.pi
        comb = {n: form_tau(T, M, lambda t, n=n: -2 * lp / np.sqrt(n) * np.cos(t * np.log(n)), Uc, nq=60) for n, lp in cs}
        for k, v in enumerate(R['V'].T):
            parts = {n: v @ comb[n] @ v for n in comb}
            print(f"      {R['labels'][k]:>12s}: p_i={R['p'][k]:+.4f} = arch {v@mpos@v:+.4f} + comb {sum(parts.values()):+.4f} {{{', '.join(f'{n}:{x:+.3f}' for n,x in parts.items())}}};  nu_i={R['nu'][k]:.4f}")

    print("\n=== (5b) M0 per-component slope law: beta_pred = kappa (int_J sigma_-/2) T^2 / b1,  b1 = mean of |sigma'| at the two endpoints of J, kappa=0.7")
    def slope_law(W, tag):
        T = W['T']; sig = W['sig']; comps = W['comps']; M = W['A'].shape[0]; modes = comp_modes(T, M, comps)
        for (lo, hi), got, _ in modes:
            mass = quad(lambda t: -sig([t])[0], lo, hi, limit=200)[0]; h = 1e-4
            sl = [abs((sig([x + h])[0] - sig([x - h])[0]) / (2 * h)) for x in ((hi,) if lo == 0.0 else (lo, hi))]
            b1 = np.mean(sl); pred = 0.7 * (mass / 2) * T * T / b1
            ray = {p: (v @ W['Neg'] @ v) / (v @ W['Pos'] @ v) for p, (l0, v) in got.items()}
            print(f"   [{tag}] J=[{lo:.2f},{hi:.2f}] N_J={T*(hi-lo)/np.pi:.2f} mass={mass:.3f} s_max={(-sig(np.linspace(lo,hi,401))).max():.2f} slopes={np.round(sl,3).tolist()}  beta_pred(M0 slope)={pred:.3f}  beta_Rayleigh(mode)={ {p: round(x,3) for p,x in ray.items()} }")
    for key in (('l3', 40 if not fast else 30), ('l5', 40 if not fast else 30)): slope_law(Ws[key], key[0])
    print("\n=== (6) falsifier M_1 (quartet 1/2±delta±i gamma_1), log 2, delta=0.1: lambda_A should be < 0 (R187: -1.522e-3, n_-=2)")
    T = np.log(2)
    for M in ((40, 60) if not fast else (40,)):
        W = window(T, M, quartet=(GAM1, 0.1), tag=f'M1 d=0.1 M={M}'); W['T'] = T
        R = span_test(W, f'M1 M={M}')
    W0 = window(T, 40, tag='zeta log2'); W0['T'] = T; span_test(W0, 'zeta log2'); slope_law(W0, 'zeta log2'); slope_law(W, 'M1 d=0.1')
    Wd = window(T, 40, quartet=(GAM1, 0.001), tag='M1 d=0.001'); Wd['T'] = T; span_test(Wd, 'M1 d=0.001')
