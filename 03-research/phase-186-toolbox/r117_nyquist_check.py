#!/usr/bin/env python3
"""Independent check of R186_051 Thm 4.1 (Nyquist sampling identity for the truncated Weil form).
Own discretisation: Legendre basis on [-T,T], exact F^ via spherical Bessel, c_F via Gauss-Legendre.
Conventions = Paper 47 eq:symbol/eq:form/thm:A.
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma, spherical_jn, sici
from scipy.integrate import quad

C0 = float(digamma(0.25)) - np.log(np.pi)
EG = 0.5772156649015329

def K(u):
    u = np.asarray(u, float)
    return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))

def Kr(u):
    """K(u) - 1/u, smooth; series for small u."""
    u = np.asarray(u, float); out = np.empty_like(u)
    sm = u < 1e-3
    # K(u) = 2e^{-u/2}/(1-e^{-2u}); 1/(1-e^{-2u}) = 1/(2u) + 1/2 + u/6 - u^3/90 + ...
    # 2 e^{-u/2} (1/(2u) + 1/2 + u/6) = e^{-u/2}/u + e^{-u/2}(1 + u/3)
    us = u[sm]
    out[sm] = (np.exp(-us / 2) - 1) / np.where(us == 0, 1, us) * (us != 0) + (-0.5) * (us == 0) + np.exp(-us / 2) * (1 + us / 3 - us**3 / 45)
    ub = u[~sm]; out[~sm] = K(ub) - 1 / ub
    return out

def m_arch(tau):
    return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)

def contacts(T):
    X = int(np.exp(2 * T)) + 2
    spf = np.zeros(X + 1, dtype=np.int64)
    for p in range(2, X + 1):
        if spf[p] == 0: spf[p::p][spf[p::p] == 0] = p
    out = []
    for n in range(2, X + 1):
        if np.log(n) >= 2 * T: break
        p = spf[n]; r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, 2 * np.log(p) / np.sqrt(n)))   # (n, v_n)
    return out

# ---------- basis: P_j(t/T), j < M
def legvals(M, x):
    V = np.zeros((M, len(x)))
    for j in range(M):
        c = np.zeros(j + 1); c[j] = 1; V[j] = NL.legval(x, c)
    return V

def Cmat(T, M, u):
    """C(u)_{ij} = int_{-T+u}^{T} P_i(t/T) P_j((t-u)/T) dt, 0<=u<=2T (c_F(u) = h C h)."""
    if u >= 2 * T: return np.zeros((M, M))
    xg, wg = NL.leggauss(M + 2)
    lo, hi = -T + u, T
    t = (hi + lo) / 2 + (hi - lo) / 2 * xg; w = (hi - lo) / 2 * wg
    Vi = legvals(M, t / T); Vj = legvals(M, (t - u) / T)
    return (Vi * w) @ Vj.T

def form_matrices(T, M):
    """A (= a_T Gram), Pcomb (= sum v_n C(log n)), Nrm (= C(0)), Lev (= int_0^{2T}(C(0)-C(u))K du + C(0) int_{2T}^oo K), Pole (= 2 int_0^{2T} e^{u/2} C(u) du)."""
    N0 = Cmat(T, M, 0.0)
    cs = contacts(T)
    Pc = sum(v * Cmat(T, M, np.log(n)) for n, v in cs)
    # u-panels, geometric near 0
    edges = np.concatenate([[0], 2 * T * 2.0 ** (-np.arange(40, 0, -1.0)), [2 * T]])
    edges = np.unique(edges)
    xg, wg = NL.leggauss(24)
    Lev = np.zeros((M, M)); Pole = np.zeros((M, M))
    for lo, hi in zip(edges[:-1], edges[1:]):
        for x, w in zip((hi + lo) / 2 + (hi - lo) / 2 * xg, (hi - lo) / 2 * wg):
            Cu = Cmat(T, M, x)
            Lev += (N0 - Cu) * K(x) * w
            Pole += 2 * np.exp(x / 2) * Cu * w
    tail = quad(K, 2 * T, np.inf)[0]
    Lev += N0 * tail
    sym = lambda X: (X + X.T) / 2
    Pc, N0, Lev, Pole = sym(Pc), sym(N0), sym(Lev), sym(Pole)
    A = C0 * N0 + Lev - Pc
    return A, Pc, N0, Lev, Pole, tail, cs

def tate_rows(T, M):
    xg, wg = NL.leggauss(M + 40); t = T * xg; w = T * wg
    V = legvals(M, xg)
    return np.array([V @ (w * np.exp(t / 2)), V @ (w * np.exp(-t / 2))])

def null_basis(R):
    u, s, vt = np.linalg.svd(R); return vt[R.shape[0]:].T

def fhat(T, M, h, tau):
    """F^(tau) = sum_j h_j 2T i^j j_j(tau T), exact."""
    tau = np.asarray(tau, float)
    J = np.array([spherical_jn(j, tau * T) for j in range(M)])          # (M, len)
    ph = np.array([1j ** j for j in range(M)])
    return 2 * T * (h * ph) @ J

def LT_grid(T, k):
    """L_T(w_k) = int_0^{2T}(1-cos(w u))K(u)du at w_k = k pi/2T, k>=0 array."""
    w = k * np.pi / (2 * T)
    out = np.zeros(len(k))
    # 1/u part: Cin(2T w) = gamma + log(2Tw) - Ci(2Tw)
    x = 2 * T * w
    pos = x > 0
    si, ci = sici(x[pos])
    out[pos] = EG + np.log(x[pos]) - ci
    # regular part: int Kr - int Kr cos(wu)
    IKr = quad(Kr, 0, 2 * T, limit=200)[0]
    cosint = np.zeros(len(k))
    # exact-ish IBP series at w_k: int_0^{2T} Kr cos(wu) du = Kr(2T) sin(2Tw)/w + [Kr'(2T)cos(2Tw) - Kr'(0)]/w^2 - [Kr''(2T) sin]/w^3 - [Kr'''(2T)cos - Kr'''(0)]/w^4 ...
    # at w_k: sin(k pi)=0, cos(k pi)=(-1)^k.  Need Kr', Kr''' at 0 and 2T: finite differences on Kr.
    def d(f, x0, n, hh=1e-2):
        if n == 1: return (f(x0 + hh) - f(x0 - hh)) / (2 * hh) if x0 > 0 else (-3 * f(x0) + 4 * f(x0 + hh) - f(x0 + 2 * hh)) / (2 * hh)
        if n == 3:
            if x0 > 0: return (f(x0 + 2 * hh) - 2 * f(x0 + hh) + 2 * f(x0 - hh) - f(x0 - 2 * hh)) / (2 * hh**3)
            return (-5 * f(x0) + 18 * f(x0 + hh) - 24 * f(x0 + 2 * hh) + 14 * f(x0 + 3 * hh) - 3 * f(x0 + 4 * hh)) / (2 * hh**3)
    k1_0, k1_T = d(Kr, 0.0, 1), d(Kr, 2 * T, 1); k3_0, k3_T = d(Kr, 0.0, 3), d(Kr, 2 * T, 3)
    KQ = 3000
    for i in np.where((k > 0) & (k <= KQ))[0]:
        cosint[i] = quad(Kr, 0, 2 * T, weight='cos', wvar=w[i], limit=2000)[0]
    big = k > KQ
    sg = (-1.0) ** k[big]
    cosint[big] = (sg * k1_T - k1_0) / w[big]**2 - (sg * k3_T - k3_0) / w[big]**4
    # crossover check
    i = np.where(k == KQ)[0]
    if len(i):
        ii = i[0]; approx = ((-1.0) ** KQ * k1_T - k1_0) / w[ii]**2 - ((-1.0) ** KQ * k3_T - k3_0) / w[ii]**4
        print(f"   [LT_grid] crossover k={KQ}: quad {cosint[ii]:.3e} vs IBP {approx:.3e}")
    out[k == 0] = 0.0
    out += IKr - cosint
    out[k == 0] = 0.0
    return out

def run(T, name, M=40, Kmax=200000, seed=7):
    print(f"\n=========== T = {name} = {T:.6f}, M = {M}")
    A, Pc, N0, Lev, Pole, tail, cs = form_matrices(T, M)
    R = tate_rows(T, M); Z = null_basis(R)
    # generalized eigen on P_T: min h A h / h N0 h
    AP, NP = Z.T @ A @ Z, Z.T @ N0 @ Z
    L = np.linalg.cholesky(NP); Li = np.linalg.inv(L)
    lam, V = np.linalg.eigh(Li @ AP @ Li.T)
    hstar = Z @ (Li.T @ V[:, 0]); hstar /= np.sqrt(hstar @ N0 @ hstar)
    print(f" lambda_A (Galerkin, own code) = {lam[0]:+.6e};  |A(h*)|,|B(h*)| = {abs(R @ hstar).max():.1e}; tail int_{{2T}}^oo K = {tail:.6f}")
    rng = np.random.default_rng(seed)
    tests = [('h*', hstar)]
    for j in range(3):
        g = Z @ rng.standard_normal(M - 2); g /= np.sqrt(g @ N0 @ g); tests.append((f'rand{j}', g))
    # grid data
    k = np.arange(0, Kmax + 1); wk = k * np.pi / (2 * T)
    LT = LT_grid(T, k)
    Pg = np.zeros(len(k))
    for n, v in cs: Pg += v * np.cos(wk * np.log(n))
    sT = C0 + tail + LT - Pg                      # memo's s_T
    sig = m_arch(wk) - Pg                         # Paper 47 sigma_T (untruncated)
    # int_{2T}^oo cos(w u) K(u) du at w_k (closed form, K = 2 sum_m e^{-(2m+1/2)u}):
    tail_cos = np.zeros(len(k))
    for mm in range(0, 60):
        a = 2 * mm + 0.5; tail_cos += (-1.0) ** k * 2 * np.exp(-a * 2 * T) * a / (a * a + wk * wk)
    tq = np.array([quad(K, 2 * T, np.inf, weight='cos', wvar=w)[0] for w in wk[1:40]])
    print(f"   check closed-form tail_cos vs QAWF (k<40): {np.max(np.abs(tail_cos[1:40]-tq)):.2e};  check s_T - sigma_T = tail_cos: max|diff| (k<2e5) = {np.max(np.abs(sT - sig - tail_cos)):.2e}")
    # C_0(T, w) = -Re etahat/(4T),  etahat = S_T - M_T
    S = np.zeros(len(k), complex)
    for n, v in cs: S += v * np.exp(1j * wk * np.log(n))
    s = 0.5 + 1j * wk; MT = 2 * (np.exp(s * 2 * T) - 1) / s
    Cz = -np.real(S - MT) / (4 * T)
    def nyq(f2, g, Kc):
        return (f2[0] * g[0] + 2 * np.sum(f2[1:Kc + 1] * g[1:Kc + 1])) / (4 * T)
    for tag, h in tests:
        f2 = np.abs(fhat(T, M, h, wk)) ** 2
        exact = dict(a=h @ Pc @ h, b=h @ N0 @ h, c=-(h @ Pc @ h) + h @ Pole @ h, d=h @ A @ h)
        print(f" --- {tag}: exact: comb (a) = {exact['a']:+.10f}  norm (b) = {exact['b']:.10f}  E_psi (c) = {exact['c']:+.10f}  a_T (d) = {exact['d']:+.10e}")
        print(f"     |F^(w_k)|^2 ~ C/k^2 ? k^2 f2 at k=1e3,1e4,1e5: {(k[1000]**2*f2[1000]):.3e} {(k[10000]**2*f2[10000]):.3e} {(k[100000]**2*f2[100000]):.3e}; F(T)^2,F(-T)^2 = {(h@legvals(M,np.array([1.0]))[:,0])**2:.2e},{(h@legvals(M,np.array([-1.0]))[:,0])**2:.2e}")
        for Kc in (2000, 20000, 200000):
            ra, rb, rc, rd = nyq(f2, Pg, Kc), nyq(f2, np.ones(len(k)), Kc), 4 * T * nyq(f2, Cz, Kc), nyq(f2, sT, Kc)
            rsig = nyq(f2, sig, Kc)
            ral = nyq(f2, tail_cos, Kc)
            print(f"     K={Kc:>6}: err(a) {ra-exact['a']:+.2e}  err(b) {rb-exact['b']:+.2e}  err(c) {rc-exact['c']:+.2e}  err(d, s_T) {rd-exact['d']:+.2e}  |  alias (1/4T)sum f2*int_{{2T}}^oo cos K = {ral:+.4e}")
        # alias closed form: sum_{j>=1} int_{-2T}^{2T} c_F(v) K(4Tj - v) dv
        al = 0.0
        xg, wg = NL.leggauss(60)
        for jj in (1, 2, 3):
            for x, w in zip(T + T * xg, T * wg):
                cF = h @ Cmat(T, M, x) @ h
                al += cF * (K(4 * T * jj - x) + K(4 * T * jj + x)) * w
        # leading Tate term (vanishes on P_T): 2 e^{-2T} A(F)B(F); next: 2 e^{-10T} Phi(5/2)Phi(-5/2)
        xq, wq = NL.leggauss(M + 40); t = T * xq; w = T * wq; Fv = h @ legvals(M, xq)
        t52 = 2 * np.exp(-10 * T) * np.sum(Fv * w * np.exp(2.5 * t)) * np.sum(Fv * w * np.exp(-2.5 * t))
        print(f"     alias closed form sum_j int c_F K(4Tj - v) = {al:+.3e}  (first non-Tate term 2e^{{-10T}}Phi(5/2)Phi(-5/2) = {t52:+.3e}; e^{{-2T}}*2|AB|=0 on P_T)")
        # absolute convergence: sum |f2| |s_T| partial sums
        ab = np.cumsum(2 * f2 * np.abs(sT)) / (4 * T)
        print(f"     sum_k |f2||s_T| partial: K=2e3 {ab[2000]:.6f}  2e4 {ab[20000]:.6f}  2e5 {ab[200000]:.6f};  sum_k>K f2*log k tail est. ~ {np.sum(2*f2[100000:]*np.log(k[100000:]))/(4*T):.2e}")
    return lam[0]

if __name__ == '__main__':
    Ws = [('1/2 log3', 0.5 * np.log(3)), ('log 2', np.log(2)), ('1/2 log5', 0.5 * np.log(5))]
    if len(sys.argv) > 1: Ws = [Ws[int(sys.argv[1])]]
    for nm, T in Ws: run(T, nm)
