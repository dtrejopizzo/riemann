#!/usr/bin/env python3
"""R186_026 — piecewise Tate Gram matrix G_k(T) in closed form.

Form (Paper 47 thm:A / lem:K / thm:S(iii)):
  a_T(F,G) = C_0<F,G> + int_0^oo K(u) (<F,G> - C_{FG}(u)) du - sum_{n in N_T} v_n C_{FG}(log n),
  K(u) = 2 e^{-u/2}/(1-e^{-2u}) = 2 sum_{m>=0} e^{-s_m u},  s_m = 2m+1/2,
  C_{FG}(u) = 1/2 [ int F(t)G(t-u) dt + int G(t)F(t-u) dt ],  v_n = 2 Lambda(n)/sqrt n,
  C_0 = psi(1/4) - log pi,  tau(r) := int_r^oo K = log coth(r/4) + pi - 2 arctan e^{r/2}.
Basis: phi_{j,al}(x) = e^{al x} 1_{B_j}(x), al = +-1/2, B_j = (a_j, b_j), j = 1..k.
Entries (all in closed form; see R186_026 §1):
  * same block:   A_jj^{al be} = (C_0 + tau(L)) E(ga;a,b) + D^{al be}(a,b),  ga = al+be,
       D = int_0^L K(u) [E(ga;a,b) - 1/2 (e^{-al u}+e^{-be u}) E(ga;a+u,b)] du   (Lerch series / psi / Li_2)
  * distinct blocks (B_i to the right of B_j):  X_ij^{al be} = - sum_{m>=0} E(al-s_m; a,b) E(be+s_m; c,d)
  * prime n:  P_ij^{al be} = -v_n/2 [ e^{-be l} E(ga; B_i cap (B_j+l)) + e^{-al l} E(ga; B_j cap (B_i+l)) ],  l = log n
  * mass  M_ij^{al be} = delta_ij E(ga;B_j);  Tate vectors t_+-(j,al) = E(al +- 1/2; B_j).
E(g;a,b) = int_a^b e^{g x} dx.  Two independent implementations: closed form (mpmath, dps=30)
and 1-D Gauss quadrature of the analytic integrand (float64).  lam_min(W|E_k) = minimal eigenvalue of the
pencil (Z^T G Z, Z^T M Z), Z = kernel basis of the two global Tate constraints.

Usage:  python3 r026_gram.py [check | scan | struct | limit]
"""
import sys, numpy as np, mpmath as mp
from numpy.polynomial import legendre as NL

mp.mp.dps = 30
HALF = mp.mpf(1) / 2
QUART = mp.mpf(1) / 4
C0 = mp.digamma(QUART) - mp.log(mp.pi)
LOG2 = mp.log(2)

# ---------------------------------------------------------------- utilities
def E(g, a, b):
    """int_a^b e^{g x} dx"""
    g = mp.mpf(g)
    if g == 0:
        return mp.mpf(b) - mp.mpf(a)
    return (mp.exp(g * b) - mp.exp(g * a)) / g

def tau(r):
    """int_r^oo K(u) du  (thm:S iii with 2T -> r)"""
    r = mp.mpf(r)
    return mp.log(mp.coth(r / 4)) + mp.pi - 2 * mp.atan(mp.exp(r / 2))

def S1(z, a):
    """sum_{m>=1} z^m/(m+a),  0 <= z < 1"""
    if z == 0: return mp.mpf(0)
    return z * mp.lerchphi(z, 1, 1 + a)

def S2(z, a):
    """sum_{m>=1} z^m/(m+a)^2,  0 <= z <= 1"""
    if z == 0: return mp.mpf(0)
    if z == 1: return mp.zeta(2, 1 + a)
    return z * mp.lerchphi(z, 2, 1 + a)

def H(a, b):
    """sum_{m>=1} [1/(m+a) - 1/(m+b)] = psi(1+b) - psi(1+a)"""
    return mp.digamma(1 + b) - mp.digamma(1 + a)

def contacts(T):
    out = []
    n = 2
    while mp.log(n) < 2 * T:
        f = mp.mpf(n); p = None
        for q in range(2, n + 1):
            if n % q == 0:
                p = q; break
        m = n; k = 0
        while m % p == 0: m //= p; k += 1
        if m == 1:
            out.append((n, mp.log(f), 2 * mp.log(p) / mp.sqrt(f)))
        n += 1
    return out  # (n, log n = shift, v_n)

# ---------------------------------------------------------------- closed form
def cross_cf(al, a, b, be, c, d):
    """-1/2 iint_{(a,b)x(c,d)} K(x-y) e^{al x} e^{be y},  d <= a  (B_i=(a,b) to the right of B_j=(c,d))"""
    al, be = mp.mpf(al), mp.mpf(be)
    X = -E(al - HALF, a, b) * E(be + HALF, c, d)                  # m = 0 (Tate term, rank one)
    a1, a2 = QUART - al / 2, QUART + be / 2
    tot = mp.mpf(0)
    for x, sx in ((a, 1), (b, -1)):
        for y, sy in ((d, 1), (c, -1)):
            D = mp.mpf(x) - mp.mpf(y); z = mp.exp(-2 * D)
            if a1 == a2: Lam = S2(z, a1)
            elif z == 1: Lam = H(a1, a2) / (a2 - a1)
            else: Lam = (S1(z, a1) - S1(z, a2)) / (a2 - a1)
            tot += sx * sy * mp.exp(al * x + be * y - D / 2) * Lam
    return X - tot / 4                                              # m >= 1 (kernel K_1)

def Qf(c, L):
    c = mp.mpf(c)
    return L if c == 0 else (1 - mp.exp(-c * L)) / c

def I1(c, L):
    c = mp.mpf(c)
    return L**2 / 2 if c == 0 else (1 - mp.exp(-c * L) * (1 + c * L)) / c**2

def same_cf(al, be, a, b):
    """A_jj^{al be} = (C_0 + tau(L)) E(ga;a,b) + D^{al be}"""
    al, be = mp.mpf(al), mp.mpf(be); a, b = mp.mpf(a), mp.mpf(b)
    L = b - a; z = mp.exp(-2 * L); ga = al + be
    if ga != 0:                                                     # al = be
        s = HALF
        m0 = (2 * (Qf(s, L) - Qf(s + al, L)) * mp.exp(ga * b) + 2 * (Qf(s - al, L) - Qf(s, L)) * mp.exp(ga * a)) / ga
        pb = H(QUART, QUART + al / 2) - mp.exp(-L / 2) * S1(z, QUART) + mp.exp(-(HALF + al) * L) * S1(z, QUART + al / 2)
        pa = H(QUART - al / 2, QUART) - mp.exp(-(HALF - al) * L) * S1(z, QUART - al / 2) + mp.exp(-L / 2) * S1(z, QUART)
        D = m0 + (mp.exp(ga * b) * pb + mp.exp(ga * a) * pa) / ga
    else:                                                           # be = -al
        m0 = L * (2 * Qf(HALF, L) - Qf(0, L) - Qf(1, L)) + I1(0, L) + I1(1, L)
        sq = (H(QUART, 0) / 2 + H(QUART, HALF) / 2 - mp.exp(-L / 2) * S1(z, QUART)
              + S1(z, 0) / 2 + mp.exp(-L) * S1(z, HALF) / 2)
        si = (mp.zeta(2) / 4 - S2(z, 0) / 4 - L * S1(z, 0) / 2
              + mp.zeta(2, mp.mpf(3) / 2) / 4 - mp.exp(-L) * S2(z, HALF) / 4 - L * mp.exp(-L) * S1(z, HALF) / 2)
        D = m0 + L * sq + si
    return (C0 + tau(L)) * E(ga, a, b) + D

def prime_entry(al, a, b, be, c, d, l, v):
    al, be = mp.mpf(al), mp.mpf(be); ga = al + be
    def ov(lo1, hi1, lo2, hi2):
        lo, hi = max(lo1, lo2), min(hi1, hi2)
        return E(ga, lo, hi) if hi > lo else mp.mpf(0)
    return -v / 2 * (mp.exp(-be * l) * ov(a, b, c + l, d + l) + mp.exp(-al * l) * ov(c, d, a + l, b + l))

# ---------------------------------------------------------------- 1-D quadrature (float64, independent check)
def Kf(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))
def Ef(g, a, b): return (b - a) if g == 0 else (np.exp(g * b) - np.exp(g * a)) / g
GX, GW = NL.leggauss(80)
def gauss(f, lo, hi):
    if hi <= lo: return 0.0
    u = (hi + lo) / 2 + (hi - lo) / 2 * GX
    return float(np.sum(f(u) * GW) * (hi - lo) / 2)

def same_quad(al, be, a, b):
    L = b - a; ga = al + be
    br = lambda u: Ef(ga, a, b) - 0.5 * (np.exp(-al * u) + np.exp(-be * u)) * Ef(ga, a + u, b)
    D = gauss(lambda u: Kf(u) * br(u), 0.0, L)
    C0f = float(C0); tf = float(tau(L))
    return (C0f + tf) * Ef(ga, a, b) + D

def cross_quad(al, a, b, be, c, d):
    ga = al + be
    f = lambda u: Kf(u) * np.exp(-be * u) * Ef(ga, np.maximum(a, c + u), np.minimum(b, d + u))
    pts = sorted({a - d, a - c, b - d, b - c})
    return -0.5 * sum(gauss(f, lo, hi) for lo, hi in zip(pts[:-1], pts[1:]))

# ---------------------------------------------------------------- assembly
def blocks_equal(T, k):
    e = [-T + 2 * T * i / k for i in range(k + 1)]
    return [(e[i], e[i + 1]) for i in range(k)]

def blocks_orbit(T):
    l = LOG2
    if T < l: return [(-T, T - l), (T - l, l - T), (l - T, T)]
    e = [-T, T - 2 * l, l - T, T - l, 2 * l - T, T]
    return [(e[i], e[i + 1]) for i in range(5)]

ALS = (HALF, -HALF)

def gram(T, B, with_primes=True, parts=False):
    """G (2k x 2k, index (j,al)), mass M, Tate (t+, t-), and parts A_diag, A_cross, {P_n}."""
    k = len(B); n = 2 * k
    Ad = mp.zeros(n, n); Ax = mp.zeros(n, n); M = mp.zeros(n, n)
    tp = mp.zeros(n, 1); tm = mp.zeros(n, 1)
    idx = lambda j, ia: 2 * j + ia
    for j, (a, b) in enumerate(B):
        for ia, al in enumerate(ALS):
            tp[idx(j, ia)] = E(al + HALF, a, b); tm[idx(j, ia)] = E(al - HALF, a, b)
            for ib, be in enumerate(ALS):
                M[idx(j, ia), idx(j, ib)] = E(al + be, a, b)
                Ad[idx(j, ia), idx(j, ib)] = same_cf(al, be, a, b)
    for i in range(k):
        for j in range(i):                                           # B_i to the right of B_j
            for ia, al in enumerate(ALS):
                for ib, be in enumerate(ALS):
                    x = cross_cf(al, B[i][0], B[i][1], be, B[j][0], B[j][1])
                    Ax[idx(i, ia), idx(j, ib)] = x; Ax[idx(j, ib), idx(i, ia)] = x
    Pn = {}
    if with_primes:
        for nn, l, v in contacts(T):
            P = mp.zeros(n, n)
            for i in range(k):
                for j in range(k):
                    for ia, al in enumerate(ALS):
                        for ib, be in enumerate(ALS):
                            P[idx(i, ia), idx(j, ib)] = prime_entry(al, B[i][0], B[i][1], be, B[j][0], B[j][1], l, v)
            Pn[nn] = P
    G = Ad + Ax
    for P in Pn.values(): G = G + P
    if parts: return G, M, tp, tm, Ad, Ax, Pn
    return G, M, tp, tm

def to_np(A): return np.array(A.tolist(), dtype=float)

def null_basis(rows):
    """orthonormal basis (numpy) of the kernel of the given rows"""
    R = np.array(rows, dtype=float)
    _, s, Vt = np.linalg.svd(R)
    return Vt[R.shape[0]:].T

def lam_min_E(G, M, tp, tm, mpprec=False):
    """eigenvalues of the pencil (Z^T G Z, Z^T M Z) on E_k = ker(t+, t-)"""
    Gn, Mn = to_np(G), to_np(M)
    Z = null_basis([to_np(tp).ravel(), to_np(tm).ravel()])
    A, Bm = Z.T @ Gn @ Z, Z.T @ Mn @ Z
    if not mpprec:
        import scipy.linalg as sl
        return sl.eigh(A, Bm, eigvals_only=True)
    Zm = mp.matrix(Z.tolist())
    Am, Bmm = Zm.T * G * Zm, Zm.T * M * Zm
    Lc = mp.cholesky(Bmm); Li = mp.inverse(Lc)
    S = Li * Am * Li.T
    ev = mp.eigsy((S + S.T) / 2, eigvals_only=True)
    return sorted([ev[i] for i in range(ev.rows)])

# ---------------------------------------------------------------- modes
def check():
    print("# 1. closed form vs 1-D quadrature (individual entries)")
    for (al, be, a, b) in ((0.5, 0.5, -0.3, 0.1), (0.5, -0.5, -0.3, 0.1), (-0.5, -0.5, 0.2, 0.8), (-0.5, 0.5, -0.8, -0.1)):
        cf = same_cf(al, be, a, b); q = same_quad(al, be, a, b)
        print(f"  same  al={al:+.1f} be={be:+.1f} ({a},{b}):  cf={mp.nstr(cf, 15)}  quad={q:.15g}  dif={float(cf) - q:.1e}")
    for (al, a, b, be, c, d) in ((0.5, 0.1, 0.5, 0.5, -0.4, 0.1), (0.5, 0.1, 0.5, -0.5, -0.4, 0.1), (-0.5, 0.1, 0.5, 0.5, -0.4, 0.1),
                                 (-0.5, 0.1, 0.5, -0.5, -0.4, 0.1), (0.5, 0.3, 0.7, -0.5, -0.6, -0.2), (-0.5, 0.3, 0.7, 0.5, -0.6, -0.2)):
        cf = cross_cf(al, a, b, be, c, d); q = cross_quad(al, a, b, be, c, d)
        print(f"  cross al={al:+.1f} be={be:+.1f} ({a},{b})x({c},{d}): cf={mp.nstr(cf, 15)}  quad={q:.15g}  dif={float(cf) - q:.1e}")
    print("# 2. exact lam_min(W|E_k) vs r024_schur.py Galerkin (min G_EE)")
    sys.path.insert(0, __file__.rsplit('/', 1)[0])
    import r024_schur as r
    be = r.BE(0)
    for T, kind in ((mp.log(3) / 2, 'orbit'), (mp.log(5) / 2, 'orbit'), (mp.log(3) / 2, 'equal5'), (mp.log(5) / 2, 'equal5'), (mp.log(5) / 2, 'equal9')):
        B = blocks_orbit(T) if kind == 'orbit' else blocks_equal(T, int(kind[5:]))
        G, M, tp, tm = gram(T, B); ev = lam_min_E(G, M, tp, tm)
        d = r.build(float(T), 14, be, kind=kind); o = r.analyse(d, be)
        print(f"  T={float(T):.4f} {kind:7s} dimE={len(ev)}  exact: {ev[0]:+.6e} {ev[1]:+.4e}   r024(N=14) minGee={o['Gee'][0]:+.6e}  lamA(Galerkin)={o['lamW']:+.3e}")

def scan():
    print("# lam_min(W|E_k) (exact upper bound of lam_A; k equal blocks); last column: all <0 ?")
    for T in (mp.log(3) / 2, 0.62, mp.log(2), 0.75, mp.log(5) / 2):
        T = mp.mpf(T); row = f"T={float(T):.4f}:"
        for k in (3, 5, 9, 13, 20, 30, 45):
            G, M, tp, tm = gram(T, blocks_equal(T, k)); ev = lam_min_E(G, M, tp, tm)
            row += f"  k={k}:{ev[0]:+.3e}"
        print(row, flush=True)

def struct():
    T = mp.log(5) / 2; k = 9; B = blocks_equal(T, k)
    G, M, tp, tm, Ad, Ax, Pn = gram(T, B, parts=True)
    Gn, Adn, Axn = to_np(G), to_np(Ad), to_np(Ax)
    print(f"# structure at T=1/2 log5, k={k} (basis dim {2*k})")
    print("  signs: max archimedean cross entry =", Axn.max(), " (all <=0 ?)", (Axn <= 0).all())
    off = Adn[0, 1]; print(f"  entry (+,-) same block B_1: {off:+.4f};  diag (+,+): {Adn[0,0]:+.4f}  (-,-): {Adn[1,1]:+.4f}")
    for nn, P in Pn.items():
        Pn_ = to_np(P); print(f"  prime n={nn}: max entry {Pn_.max():+.3e}, rank {np.linalg.matrix_rank(Pn_, tol=1e-12)}, blocks reached {sum(1 for (a,b) in B if a + float(mp.log(nn)) < float(T))}, norm {np.abs(np.linalg.eigvalsh(Pn_)).max():.3f}")
    s = np.linalg.svd(Axn, compute_uv=False); print("  singular values of A_cross:", np.array2string(s[:8], precision=3), "...")
    s = np.linalg.svd(Gn, compute_uv=False); print("  singular values of G:", np.array2string(s[:6], precision=3), "... min", f"{s[-1]:.2e}")
    ev = np.linalg.eigvalsh(to_np(M)); print("  cond(M)=", f"{ev[-1]/ev[0]:.1e}")
    evG = np.linalg.eigvalsh(np.linalg.solve(to_np(M), Gn) if False else Gn); print("  inertia of G (full basis, no Tate): n_- =", (evG < 0).sum(), " n_+ =", (evG > 0).sum())
    # form on e^{x/2} 1_{I_T} (c = 1 on all blocks, al=+): = a_T(e^{x/2} 1_I)
    c = np.zeros(2 * k); c[0::2] = 1; print(f"  a_T(e^{{x/2}} 1_I) = {c @ Gn @ c:+.4f}  (negative: W indefinite on the full basis)")
    # jump basis: F = sum_j [d_j chi_{x_j} + d'_j psi_{x_j}],  chi = cosh((y-x_j)/2) 1_{y>x_j}, psi = 2 sinh(...)
    J = np.zeros((2 * k, 2 * k)); xs = [float(a) for a, _ in B]
    for i in range(k):
        for j in range(i + 1):
            J[2 * i, 2 * j] = 0.5 * np.exp(-xs[j] / 2); J[2 * i + 1, 2 * j] = 0.5 * np.exp(xs[j] / 2)
            J[2 * i, 2 * j + 1] = np.exp(-xs[j] / 2); J[2 * i + 1, 2 * j + 1] = -np.exp(xs[j] / 2)
    Gj = J.T @ Gn @ J
    dom = np.diag(Gj) - (np.abs(Gj).sum(1) - np.abs(np.diag(Gj)))
    print("  jump basis: diag:", np.array2string(np.diag(Gj)[:6], precision=3), " min(diag - sum|off|) =", f"{dom.min():+.3f}", " (dominant ?)", (dom > 0).all())
    # local Tate basis (support 2 blocks): kernel of the two Tate constraints restricted to B_j u B_{j+1}
    cols = []
    tpn, tmn = to_np(tp).ravel(), to_np(tm).ravel()
    for j in range(k - 1):
        ix = [2 * j, 2 * j + 1, 2 * j + 2, 2 * j + 3]
        Zl = null_basis([tpn[ix], tmn[ix]])
        for q in range(Zl.shape[1]):
            v = np.zeros(2 * k); v[ix] = Zl[:, q]; cols.append(v)
    Bl = np.array(cols).T; Mn = to_np(M)
    # normalize in mass
    Bl = Bl / np.sqrt(np.einsum('ij,ij->j', Bl, Mn @ Bl))
    Gl = Bl.T @ Gn @ Bl; Ml = Bl.T @ Mn @ Bl
    dom = np.diag(Gl) - (np.abs(Gl).sum(1) - np.abs(np.diag(Gl)))
    import scipy.linalg as sl
    print("  local Tate basis (2 blocks): lam_min pencil =", f"{sl.eigh(Gl, Ml, eigvals_only=True)[0]:+.3e}", " min(diag - sum|off|) =", f"{dom.min():+.3f}", " (dominant ?)", (dom > 0).all(),
          " diag min", f"{np.diag(Gl).min():+.3f}")
    Gl0 = Bl.T @ (Adn + Axn) @ Bl; dom0 = np.diag(Gl0) - (np.abs(Gl0).sum(1) - np.abs(np.diag(Gl0)))
    print("  same, archimedean only: min(diag - sum|off|) =", f"{dom0.min():+.3f}", " lam_min =", f"{sl.eigh(Gl0, Ml, eigvals_only=True)[0]:+.3e}")

def limit():
    """jump kernel  Gcal(x,x') = a_T(psi_x, psi_x'),  psi_x = 2 sinh((y-x)/2) 1_{(x,T)}  (via blocks (x,x'),(x',T))"""
    T = mp.log(5) / 2
    def Gpsi(x, xp):
        x, xp = mp.mpf(x), mp.mpf(xp)
        if x > xp: x, xp = xp, x
        B = [(x, xp), (xp, T)] if x < xp else [(x, T)]
        G, M, tp, tm = gram(T, B)
        # psi_x = e^{-x/2} e^{y/2} - e^{x/2} e^{-y/2} on all blocks to the right of x
        def coef(x0):
            c = mp.zeros(2 * len(B), 1)
            for j, (a, b) in enumerate(B):
                if a >= x0 - mp.mpf('1e-25'):
                    c[2 * j] = mp.exp(-x0 / 2); c[2 * j + 1] = -mp.exp(x0 / 2)
            return c
        return (coef(x).T * G * coef(xp))[0]
    print("# jump kernel at T=1/2 log5: Gcal(x,x') = a_T(psi_x, psi_x')")
    xs = [-0.8, -0.4, 0.0, 0.4]
    for x in xs:
        print("  x=%+.1f:" % x, "  ".join(f"{float(Gpsi(x, xp)):+.5f}" for xp in xs))
    print("  continuity on the diagonal: G(0,0)=%.6f  G(0,1e-3)=%.6f  G(0,1e-6)=%.6f" % (float(Gpsi(0, 0)), float(Gpsi(0, 1e-3)), float(Gpsi(0, 1e-6))))

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
    {'check': check, 'scan': scan, 'struct': struct, 'limit': limit}[mode]()
