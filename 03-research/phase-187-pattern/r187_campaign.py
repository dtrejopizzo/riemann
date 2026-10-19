#!/usr/bin/env python3
"""R187 — Campaign of 100 non-contiguous windows for lambda_A(T) >= 0 on P_T (row D, data).

Same form as r034_det.py / r040_head_mp.py (phase-186-toolbox; Paper 47 eq:symbol / eq:form / thm:A / prop:negtrace):
  sigma_T(tau) = m(tau) - sum_{n in S(T)} v_n cos(tau log n),  m = Re psi(1/4 + i tau/2) - log pi,  v_n = 2 log p / sqrt n,
  S(T) = {n = p^k : log n < 2T},
  a_T(F) = C_0||F||^2 + int_0^oo (||F||^2 - C_F(u)) K(u) du - sum v_n C_F(log n),   K(u) = 2e^{-u/2}/(1-e^{-2u}),
  P_T = {F in L^2(I_T) : int F e^{+-t/2} = 0},  Neg_T = R_T sigma_-(D) R_T,  Pos_T = a_T + Neg_T.
Orthonormal Legendre Galerkin of degree < M on I_T (variational UPPER bound of lambda_A; the blocks M' < M are
the principal minors, so lambda_A^{(M')} is obtained from a single construction).  Ball arithmetic (python-flint,
arb; the Legendre/Bessel recurrences are rounded to the midpoint at each step, i.e. floating point at prec bits) at prec bits chosen per window (>= 15 digits below the estimate of -log10 lambda_A, checked a
posteriori and increased if it fails).  Eigenvalues: acb_mat.eig (approximate QR at prec bits; absolute error ~ 2^-prec).

Usage:  python3 r187_campaign.py [--stage low|mid|high|all] [--workers N] [--csv path] [--T t1 t2 ...] [--test]
Resumable: T values already present in the CSV are skipped; each row is written as soon as it finishes (file lock).
"""
import sys, os, time, json, math, argparse, fcntl, csv, traceback
import numpy as np
from scipy.special import digamma as sdigamma, spherical_jn
from scipy.optimize import brentq
from flint import arb, acb, arb_mat, acb_mat, arb_poly, ctx

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLBOX = os.path.join(HERE, '..', 'phase-186-toolbox')
CSV_DEFAULT = os.path.join(HERE, 'DATA_100_WINDOWS.csv')
WINDIR = os.path.join(HERE, 'windows')
GAMMA = np.load(os.path.join(TOOLBOX, 'zeros150.npy'))

# ----------------------------------------------------------------------------- grid
L = np.log
BOUNDARIES = {0.5 * L(2): '1/2 log 2', 0.5 * L(3): '1/2 log 3', L(2): 'log 2', 0.5 * L(5): '1/2 log 5',
              0.5 * L(7): '1/2 log 7', 0.5 * L(8): '1/2 log 8', 0.5 * L(9): '1/2 log 9', 0.5 * L(11): '1/2 log 11',
              0.5 * L(13): '1/2 log 13', 0.5 * L(16): '1/2 log 16', 0.5 * L(17): '1/2 log 17', 0.5 * L(19): '1/2 log 19',
              0.5 * L(23): '1/2 log 23', L(5): 'log 5', 0.5 * L(27): '1/2 log 27', 0.5 * L(29): '1/2 log 29',
              0.5 * L(31): '1/2 log 31', 0.5 * L(32): '1/2 log 32', L(7): 'log 7'}

def mesh():
    b = sorted(BOUNDARIES)
    low_b = [t for t in b if t <= 0.5 * L(5) + 1e-12]
    mid_b = [t for t in b if 0.5 * L(5) < t <= 1.3]
    high_b = [t for t in b if 1.3 < t < 1.75]
    low = set(low_b) | {t - 0.01 for t in low_b if t - 0.01 > 0.3} | {t + 0.01 for t in low_b}
    low |= {0.36, 0.39, 0.42, 0.45, 0.48, 0.50, 0.52, 0.58, 0.61, 0.64, 0.67, 0.72, 0.74, 0.76, 0.78}
    low = sorted(t for t in low if t <= 0.5 * L(5) + 1e-12)
    mid = set(mid_b) | {t - 0.01 for t in mid_b} | {t + 0.01 for t in mid_b}
    mid |= {0.8147, 0.83, 0.85, 0.87, 0.89, 0.90, 0.92, 0.94, 0.955, 0.995, 1.015, 1.03, 1.06, 1.075, 1.085, 1.12,
            1.135, 1.15, 1.165, 1.18, 1.22, 1.235, 1.25, 1.265, 1.30}
    mid = sorted(mid)
    high = set(high_b) | {t - 0.01 for t in high_b} | {t + 0.01 for t in high_b}
    high |= {1.32, 1.34, 1.36, 1.45, 1.50, 1.53, 1.60, 1.75}
    high = sorted(high)
    return low, mid, high

def label_of(T):
    for t, s in BOUNDARIES.items():
        if abs(t - T) < 1e-9: return s
    return ''

# ----------------------------------------------------------------------------- symbol (double precision, for the negative set)
def contacts(T):
    out = []
    for n in range(2, 100000):
        if math.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0)
        r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, p))
    return out

def sigma_np(T, tau, cont):
    s = np.real(sdigamma(0.25 + 0.5j * tau)) - np.log(np.pi)
    for n, p in cont: s -= 2 * np.log(p) / np.sqrt(n) * np.cos(tau * np.log(n))
    return s

def neg_set(T, cont, tau_scan, h=2e-3):
    """components of {sigma_T < 0} on [0, tau_scan]; sigma(0) < 0 always (m(0) = -5.37 - comb(0))."""
    f = lambda t: sigma_np(T, np.array([t]), cont)[0]
    zs = []; chunk = 2_000_000; start = 0.0; prev = None
    while start < tau_scan:
        g = np.arange(start, min(start + chunk * h, tau_scan) + h / 2, h)
        s = sigma_np(T, g, cont)
        if prev is not None and prev[1] * s[0] < 0: zs.append(brentq(f, prev[0], g[0]))
        idx = np.nonzero(s[:-1] * s[1:] < 0)[0]
        for i in idx: zs.append(brentq(f, g[i], g[i + 1]))
        prev = (g[-1], s[-1]); start = g[-1] + h
    pts = [0.0] + zs
    comps = []
    for i in range(len(pts) - 1):
        if f((pts[i] + pts[i + 1]) / 2) < 0: comps.append((pts[i], pts[i + 1]))
    complete = len(zs) % 2 == 1 and prev[1] > 0     # last crossing toward +, and sigma > 0 at the end of the scan
    return comps, complete

# ----------------------------------------------------------------------------- arb tools
def aex(x):
    """exact arb from a float (arb(float) goes through a decimal string of ~21 digits)."""
    m, e = math.frexp(float(x)); return arb((int(m * 2 ** 53), e - 53))

def gauss_arb(n):
    """Gauss-Legendre nodes and weights in arb (Newton from numpy; P_n and P_n' by three-term recurrence)."""
    from numpy.polynomial import legendre as NL
    x0, _ = NL.leggauss(n)
    def PdP(x):
        p0, p1 = arb(1), x
        for k in range(1, n): p0, p1 = p1, arb((((2 * k + 1) * x * p1 - k * p0) / (k + 1)).mid())
        return p1, n * (x * p1 - p0) / (x * x - 1)
    xs, ws = [], []
    for x in x0:
        x = aex(x)
        for _ in range(12):
            p, dp = PdP(x); dx = p / dp; x = arb((x - dx).mid())
            if abs(dx) < arb(2) ** (-ctx.prec + 8): break
        p, dp = PdP(x); xs.append(x); ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws

def leg_rows(M, T, ys, scale=None):
    """flat list (M x n) of phi_k(y_q) [* scale_q]: orthonormal Legendre on I_T."""
    n = len(ys); nrm = [(arb(2 * k + 1) / (2 * T)).sqrt() for k in range(M)]
    cols = []
    for q, y in enumerate(ys):
        u = y / T; p0, p1 = arb(1), u; col = [p0, p1]
        for k in range(1, M - 1):
            p0, p1 = p1, arb((((2 * k + 1) * u * p1 - k * p0) / (k + 1)).mid()); col.append(p1)
        if scale is not None: col = [c * scale[q] for c in col]
        cols.append(col[:M])
    return [cols[q][k] * nrm[k] for k in range(M) for q in range(n)]

def build_form(T, M, n_u, n_pan, cont):
    """A = A0 + Pr (M x M), A0, Pr, ta, tb (M x 1) in arb; Legendre Galerkin of degree < M on I_T."""
    T = aex(T); C0 = arb(0.25).digamma() - arb.pi().log()
    xg, wg = gauss_arb(M + 2); n = M + 2
    mirror = list(range(n))[::-1]                        # symmetric nodes: x_{n-1-q} = -x_q
    sgn = [arb((-1) ** k) for k in range(M)]
    K = lambda u: 2 * (-u / 2).exp() / (1 - (-2 * u).exp())
    tail = (1 / (T / 2).tanh()).log() + arb.pi() - 2 * T.exp().atan()
    I = arb_mat(M, M); 
    for i in range(M): I[i, i] = 1
    def Cmat(u):
        half = T - u / 2
        if half <= 0: return arb_mat(M, M)
        ys = [u / 2 + half * x for x in xg]
        flat = leg_rows(M, T, ys)                        # phi_k(y_q)
        F1 = arb_mat(M, n, [flat[k * n + q] * (wg[q] * half) for k in range(M) for q in range(n)])
        F2 = arb_mat(M, n, [flat[l * n + mirror[q]] * sgn[l] for l in range(M) for q in range(n)])   # phi_l(y_q - u)
        Mx = F1 * F2.transpose(); return (Mx + Mx.transpose()) / 2
    ug, uw = gauss_arb(n_u); A0 = arb_mat(M, M)
    edges = [2 * T * k / n_pan for k in range(n_pan + 1)]
    for lo, hi in zip(edges[:-1], edges[1:]):
        for x, w in zip(ug, uw):
            u = (hi + lo) / 2 + (hi - lo) / 2 * x; ws = (hi - lo) / 2 * w
            A0 += (I - Cmat(u)) * (K(u) * ws)
    A0 += I * (tail + C0)
    Pr = arb_mat(M, M)
    for nn, p in cont: Pr -= Cmat(arb(nn).log()) * (2 * arb(p).log() / arb(nn).sqrt())
    nt = M + 80; xt, wt = gauss_arb(nt); ys = [T * x for x in xt]
    flat = leg_rows(M, T, ys)
    ta = arb_mat(M, 1, [sum(flat[k * nt + q] * wt[q] * T * (ys[q] / 2).exp() for q in range(nt)) for k in range(M)])
    tb = arb_mat(M, 1, [sum(flat[k * nt + q] * wt[q] * T * (-ys[q] / 2).exp() for q in range(nt)) for k in range(M)])
    return A0 + Pr, A0, Pr, ta, tb

def sub(A, m):
    rows = A.tolist(); return arb_mat(m, m, [rows[i][j] for i in range(m) for j in range(m)])

def null_basis(ta, tb, m):
    """Z (m x (m-2)) orthonormal with Z^T ta = Z^T tb = 0 (two Householder reflections)."""
    I = arb_mat(m, m)
    for i in range(m): I[i, i] = 1
    Q = I; Tm = arb_mat(m, 2, [ta[i, 0] if j == 0 else tb[i, 0] for i in range(m) for j in range(2)])
    for j in range(2):
        v = [Tm[i, j] if i >= j else arb(0) for i in range(m)]
        nv = sum(x * x for x in v).sqrt()
        v[j] = v[j] + (nv if v[j] >= 0 else -nv)
        nv2 = sum(x * x for x in v)
        V = arb_mat(m, 1, v); H = I - (V * V.transpose()) * (2 / nv2)
        Tm = H * Tm; Q = Q * H
    rows = Q.tolist(); return arb_mat(m, m - 2, [rows[i][j] for i in range(m) for j in range(2, m)])

def eig_sym(X, vectors=False):
    """real eigenvalues (sorted) of symmetric X (approximate QR at prec bits); eigenvectors optional."""
    try:
        res = acb_mat(X).eig(right=vectors, algorithm='approx')
    except Exception:
        res = acb_mat(X).eig(right=vectors, nonstop=True)
    if vectors:
        E, R = res; order = sorted(range(len(E)), key=lambda i: float(E[i].real))
        return [E[i].real for i in order], R, order
    return sorted([e.real for e in res], key=float)

def eig_pencil(AP, PP):
    """omega_j = 1 - beta_j: eigenvalues of Pos^{-1} a_T on P_T (real, in (0, 1]); sorted increasing."""
    X = PP.solve(AP)
    try: E = acb_mat(X).eig(algorithm='approx')
    except Exception: E = acb_mat(X).eig(nonstop=True)
    return sorted([e.real for e in E], key=float)

# ----------------------------------------------------------------------------- Neg_T (tau-space, spherical Bessel)
def sph_jn(M, x):
    """j_0..j_{M-1}(x) in arb: forward recurrence if x > M + 10, descending Miller otherwise."""
    if x == 0: return [arb(1)] + [arb(0)] * (M - 1)
    if x > M + 10:
        j0 = x.sin() / x; j1 = (x.sin() / x - x.cos()) / x; out = [j0, j1]
        for k in range(1, M - 1): j0, j1 = j1, arb(((2 * k + 1) / x * j1 - j0).mid()); out.append(j1)
        return out[:M]
    Kx = M + 40 + int(float(x)); jp1, j = arb(0), arb(2) ** (-ctx.prec)
    vals = [arb(0)] * (Kx + 1); vals[Kx] = j
    for k in range(Kx, 0, -1):
        jm1 = arb(((2 * k + 1) / x * j - jp1).mid()); jp1, j = j, jm1; vals[k - 1] = j
    scale = (x.sin() / x) / vals[0]
    return [v * scale for v in vals[:M]]

def sigma_arb(T, tau, cont):
    s = acb(arb(1) / 4, tau / 2).digamma().real - arb.pi().log()
    T = aex(T)
    for n, p in cont: s -= 2 * arb(p).log() / arb(n).sqrt() * (tau * arb(n).log()).cos()
    return s

def build_neg(T, M, comps, cont, prec_neg):
    """(1/pi) sum_comp int (-sigma) phi^_k phi^_l dtau,  phi^_k = c_k i^k j_k(tau T); Gauss nodes per component."""
    old = ctx.prec; ctx.prec = prec_neg
    Ta = aex(T); N = arb_mat(M, M)
    ck = [((2 * k + 1) * 2 * Ta).sqrt() for k in range(M)]
    ph = [arb(1 if (k // 2) % 2 == 0 else -1) for k in range(M)]      # i^k = (-1)^{k/2} (k even), i (-1)^{(k-1)/2} (k odd)
    cache = {}
    for lo, hi in comps:
        w = hi - lo; nq = min(120, 16 + int(6 * w * T))
        if nq not in cache: cache[nq] = gauss_arb(nq)
        xg, wg = cache[nq]
        for x, ww in zip(xg, wg):
            t = (aex(hi) + aex(lo)) / 2 + (aex(hi) - aex(lo)) / 2 * x; ws = (aex(hi) - aex(lo)) / 2 * ww
            sm = -sigma_arb(T, t, cont) * ws / arb.pi()
            J = sph_jn(M, t * Ta)
            v_e = arb_mat(M, 1, [ck[k] * J[k] * ph[k] if k % 2 == 0 else arb(0) for k in range(M)])
            v_o = arb_mat(M, 1, [ck[k] * J[k] * ph[k] if k % 2 == 1 else arb(0) for k in range(M)])
            N += (v_e * v_e.transpose() + v_o * v_o.transpose()) * sm
    ctx.prec = old
    return N

# ----------------------------------------------------------------------------- double-precision post-processing
def legvals_np(T, M, t):
    u = t / T; P = [np.ones_like(u), u.copy()]
    for k in range(1, M - 1): P.append(((2 * k + 1) * u * P[k] - k * P[k - 1]) / (k + 1))
    return np.array(P[:M]) * np.sqrt((2 * np.arange(M) + 1) / (2 * T))[:, None]

def uhat2_np(T, c, tau):
    M = len(c); ck = np.sqrt((2 * np.arange(M) + 1) * 2 * T)
    J = np.array([spherical_jn(k, tau * T) for k in range(M)])
    return np.abs(((c * ck)[:, None] * (1j ** np.arange(M))[:, None] * J).sum(0)) ** 2

def hstar_stats(T, c, tau_c):
    c = np.asarray(c, float); c = c / np.linalg.norm(c); M = len(c)
    even = float(np.sum(c[0::2] ** 2))
    tg = np.linspace(0, tau_c, int(tau_c / 0.01) + 1); u2 = uhat2_np(T, c, tg)
    peak = float(tg[np.argmax(u2)]); cen = float((tg * u2).sum() / u2.sum())
    from numpy.polynomial import legendre as NL
    x, w = NL.leggauss(M + 40); t = (T / 2) * x; ww = (T / 2) * w
    h = c @ legvals_np(T, M, t); inner = float((h ** 2 * ww).sum())
    return even, peak, cen, inner

# ----------------------------------------------------------------------------- estimates and parameters
def digits_est(T):
    """-log10 lambda_A estimated (fit to 1/2log3, 1/2log5, 0.9, 1.0 and rate ~ N(T*))."""
    if T <= 1.0: return 22.6 * math.exp(3.3 * (T - 1.0))
    return (52.0 + 75.0 * (math.exp(2 * (T - 1.0)) - 1.0)) / math.log(10)

M_CAP = 420; M_SLOPE = 1.8; M_OFFSET = 50

def params(T, M_override=None, extra_digits=0):
    Tstar = 2 * math.pi * math.exp(2 * T)
    D = digits_est(T) * 1.15 + 25 + extra_digits
    prec = max(128, int(D * 3.33) + 16)
    n_pan = 16; a = 16 * math.pi / T; rho = a + math.sqrt(a * a + 1)
    M = M_override or min(M_CAP, max(60, int(M_SLOPE * Tstar * T) + M_OFFSET))
    n_u = max(12, int(D * math.log(10) / (2 * math.log(rho))) + 6, M // 6 + 16)   # degree of the C(u) polynomial per panel ~ M/8
    return dict(Tstar=Tstar, D=D, prec=prec, n_pan=n_pan, n_u=n_u, M=M)

# ----------------------------------------------------------------------------- a single window
def run_window(T, stage, M_override=None, extra_digits=0, M_step=20, verbose=True):
    t0 = time.time(); cont = contacts(T); P = params(T, M_override, extra_digits)
    M, prec, n_u, n_pan, Tstar = P['M'], P['prec'], P['n_u'], P['n_pan'], P['Tstar']
    ctx.prec = prec; dps = int(prec * math.log10(2))
    notes = []
    # negative set (double precision)
    A_sum = sum(2 * math.log(p) / math.sqrt(n) for n, p in cont); tau_bound = 1.1 * 2 * math.pi * math.exp(A_sum) + 10
    tau_scan = min(tau_bound, 2e5); comps, complete = neg_set(T, cont, tau_scan)
    tau_last = comps[-1][1]; meas = sum(b - a for a, b in comps)
    meas_below = sum(min(b, Tstar) - a for a, b in comps if a < Tstar)
    tau_neg = min(tau_scan, 3e4); comps_neg = [c for c in comps if c[0] < tau_neg]
    NZ = int(np.sum(GAMMA <= Tstar))
    if Tstar > GAMMA[-1]: notes.append('N(T*) requires more zeros')
    if verbose: print(f"[T={T:.5f}] M={M} prec={prec} (dps {dps}) n_u={n_u}x{n_pan} comps={len(comps)} tau_last={tau_last:.1f} complete={complete}", flush=True)
    # form + convergence in M (principal blocks); an automatic extension of M if it does not converge and is cheap
    while True:
        tb0 = time.time(); A, A0, Pr, ta, tb = build_form(T, M, n_u, n_pan, cont); t_build = time.time() - tb0
        if verbose: print(f"[T={T:.5f}] forma construida en {t_build:.0f}s (M = {M})", flush=True)
        Ms = sorted(set([m for m in range(M, 39, -M_step)][:6] + [M]))
        lam_hist = []
        for m in Ms:
            Z = null_basis(ta, tb, m); AP = Z.transpose() * sub(A, m) * Z
            ev = eig_sym(AP); lam_hist.append((m, ev[0], ev[1], sum(1 for e in ev if e < 0)))
            if verbose: print(f"[T={T:.5f}]   M'={m}: lambda_A = {ev[0].str(6)}  lambda_2 = {ev[1].str(4)}  n_- = {lam_hist[-1][3]}", flush=True)
        m_fin, lam, lam2, nneg = lam_hist[-1]
        lam_f = float(lam)
        if len(lam_hist) >= 2:
            lam_prev = float(lam_hist[-2][1]); relvar = abs(lam_f / lam_prev - 1) if lam_prev != 0 else float('nan')
        else: lam_prev, relvar = float('nan'), float('nan')
        converged = relvar < 1e-2
        if converged or M_override or M >= M_CAP or t_build > 500: break      # extend only if the build was cheap
        notes.append(f'M extendido {M} -> {M + 60} (relvar {relvar:.2e})'); M += 60; n_u = max(n_u, M // 6 + 16)
        if verbose: print(f"[T={T:.5f}] no convergido (relvar {relvar:.2e}); extiendo M a {M}", flush=True)
    margin = dps - (-math.log10(abs(lam_f))) if lam_f != 0 else float('nan')
    if margin < 15:
        notes.append(f'precision margin {margin:.1f} < 15: redone with +{int(20-margin)+10} digits')
        if verbose: print(f"[T={T:.5f}] margen {margin:.1f} insuficiente, rehago con mas precision", flush=True)
        return run_window(T, stage, M_override, extra_digits + int(20 - margin) + 10, M_step, verbose)
    nneg_flag = ''
    if nneg > 0:
        nneg_flag = 'POSSIBLE CONTACT WITH THE SIGN' if abs(lam_f) > 10 ** (-(dps - 10)) else 'n_- > 0 within noise'
        notes.append(nneg_flag)
    # final objects at M
    Z = null_basis(ta, tb, M); ZT = Z.transpose()
    AP = ZT * A * Z; A0P = ZT * A0 * Z; PrP = ZT * Pr * Z
    ev, R, order = eig_sym(AP, vectors=True)
    y1 = acb_mat(R.ncols(), 1, [R[i, order[0]] for i in range(R.nrows())]); y1 = arb_mat(y1.nrows(), 1, [y1[i, 0].real for i in range(y1.nrows())])
    y2 = arb_mat(R.nrows(), 1, [R[i, order[1]].real for i in range(R.nrows())])
    nrm = (y1.transpose() * y1)[0, 0].sqrt(); y1 = y1 / nrm
    nrm2 = (y2.transpose() * y2)[0, 0].sqrt(); y2 = y2 / nrm2
    arch_h = (y1.transpose() * A0P * y1)[0, 0]; prime_h = (y1.transpose() * PrP * y1)[0, 0]
    lam_inf = eig_sym(A0P)[0]
    # pencil
    tn0 = time.time(); prec_neg = min(prec, 256)
    N = build_neg(T, M, comps_neg, cont, prec_neg); t_neg = time.time() - tn0
    NP = ZT * N * Z; PP = AP + NP
    om = eig_pencil(AP, PP)                      # 1 - beta_j increasing
    beta = [1 - o for o in om]
    Pos_h = (y1.transpose() * PP * y1)[0, 0]; Neg_h = (y1.transpose() * NP * y1)[0, 0]
    K2 = sum(1 for o in om if o < 1e-2); K3 = sum(1 for o in om if o < 1e-3); K4 = sum(1 for o in om if o < 1e-4)
    Ke = sum(1 for o in om if float(o) < math.exp(-1)); nb1 = sum(1 for b in beta if b > 1)
    top = om[:10]
    ladder = [-math.log(float(o)) if float(o) > 0 else float('nan') for o in top]
    # h*
    c1 = Z * y1; c1f = np.array([float(c1[i, 0]) for i in range(M)]); c2 = Z * y2; c2f = np.array([float(c2[i, 0]) for i in range(M)])
    tau_c = min(tau_last, 4 * Tstar)
    even1, peak1, cen1, inner1 = hstar_stats(T, c1f, tau_c); even2 = float(np.sum((c2f / np.linalg.norm(c2f))[0::2] ** 2))
    parity = 'par' if even1 > 0.999 else ('impar' if even1 < 0.001 else 'mixta')
    t_tot = time.time() - t0
    row = dict(T=f"{T:.10f}", T_label=label_of(T), stage=stage, S_size=len(cont), S_max_n=cont[-1][0] if cont else 0,
               prec_bits=prec, dps=dps, n_u_total=n_u * n_pan, M=M, M_list=';'.join(str(m) for m, *_ in lam_hist),
               lamA_list=';'.join(l.str(6) for _, l, _, _ in lam_hist), lamA=lam.str(10), lamA_float=f"{lam_f:.6e}",
               lamA_prev=f"{lam_prev:.6e}", relvar_lastM=f"{relvar:.3e}", converged='YES' if converged else 'NOT CONVERGED',
               log10_lamA=f"{math.log10(abs(lam_f)):.4f}" if lam_f != 0 else 'nan', lam2=lam2.str(6), nneg=nneg, nneg_flag=nneg_flag,
               precision_margin_digits=f"{margin:.1f}",
               beta_top10=';'.join(b.str(12) for b in beta[:10]), one_minus_beta_top10=';'.join(o.str(6) for o in top),
               ladder_top10=';'.join(f"{v:.4f}" for v in ladder), K_1em2=K2, K_1em3=K3, K_1em4=K4, K_e=Ke, n_beta_gt_1=nb1,
               hstar_even_mass=f"{even1:.6f}", hstar_parity=parity, hstar2_even_mass=f"{even2:.6f}", hstar_peak=f"{peak1:.3f}",
               hstar_centroid=f"{cen1:.3f}", centroid_cut=f"{tau_c:.2f}", hstar_mass_inner_T2=f"{inner1:.6f}",
               Pos_h=Pos_h.str(8), Neg_h=Neg_h.str(8), arch_term_h=arch_h.str(8), prime_term_h=prime_h.str(8), lamA_inf=lam_inf.str(8),
               Tstar=f"{Tstar:.4f}", N_Tstar=NZ, tau_scan=f"{tau_scan:.1f}", tau_last=f"{tau_last:.3f}", scan_complete='YES' if complete else 'NO',
               n_comps=len(comps), n_comps_Neg=len(comps_neg), tau_Neg_cut=f"{tau_neg:.1f}", neg_measure=f"{meas:.6f}",
               N_Sh=f"{2 * T * meas / math.pi:.4f}", N_Sh_below_Tstar=f"{2 * T * meas_below / math.pi:.4f}",
               time_build_s=f"{t_build:.1f}", time_neg_s=f"{t_neg:.1f}", time_total_s=f"{t_tot:.1f}", notes=' | '.join(notes))
    side = dict(T=T, M=M, prec=prec, lam_hist=[(m, l.str(12), l2.str(8), nn) for m, l, l2, nn in lam_hist],
                hstar_coeffs=c1f.tolist(), hstar2_coeffs=c2f.tolist(), comps=comps, one_minus_beta=[o.str(10) for o in om[:40]],
                eig_AP_low=[e.str(8) for e in ev[:20]])
    with open(os.path.join(WINDIR, f"T_{T:.6f}.json"), 'w') as f: json.dump(side, f)
    if verbose: print(f"[T={T:.5f}] DONE: lambda_A={lam.str(6)} conv={row['converged']} n_-={nneg} K3={K3} N(T*)={NZ} N_Sh={row['N_Sh']} t={t_tot:.0f}s", flush=True)
    return row

FIELDS = None
def append_row(csv_path, row):
    global FIELDS
    with open(csv_path, 'a+', newline='') as f:
        fcntl.flock(f, fcntl.LOCK_EX); f.seek(0); empty = f.read(1) == ''; f.seek(0, 2)
        w = csv.DictWriter(f, fieldnames=list(row.keys()))
        if empty: w.writeheader()
        w.writerow(row); f.flush(); fcntl.flock(f, fcntl.LOCK_UN)

def done_Ts(csv_path):
    if not os.path.exists(csv_path): return set()
    with open(csv_path) as f: return {round(float(r['T']), 6) for r in csv.DictReader(f)}

def worker(args):
    T, stage, csv_path, M_override = args
    try:
        row = run_window(T, stage, M_override); append_row(csv_path, row); return (T, 'ok')
    except Exception as e:
        traceback.print_exc(); return (T, 'ERROR ' + repr(e))

if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--stage', default='all'); ap.add_argument('--workers', type=int, default=8)
    ap.add_argument('--csv', default=CSV_DEFAULT); ap.add_argument('--T', type=float, nargs='*'); ap.add_argument('--M', type=int)
    ap.add_argument('--test', action='store_true'); a = ap.parse_args()
    os.makedirs(WINDIR, exist_ok=True)
    if a.test:
        r = run_window(0.5 * L(5), 'test', M_override=a.M or 40); print(json.dumps(r, indent=1)); sys.exit()
    low, mid, high = mesh()
    jobs = []
    if a.T: jobs = [(T, 'manual', a.csv, a.M) for T in a.T]
    else:
        for st, lst in (('low', low), ('mid', mid), ('high', high)):
            if a.stage in ('all', st): jobs += [(T, st, a.csv, a.M) for T in lst]
    done = done_Ts(a.csv); jobs = [j for j in jobs if round(j[0], 6) not in done]
    print(f"{len(jobs)} pending windows; workers = {a.workers}", flush=True)
    if a.workers <= 1:
        for j in jobs: print(worker(j), flush=True)
    else:
        import multiprocessing as mp
        with mp.Pool(a.workers, maxtasksperchild=1) as pool:
            for res in pool.imap_unordered(worker, jobs): print(res, flush=True)
