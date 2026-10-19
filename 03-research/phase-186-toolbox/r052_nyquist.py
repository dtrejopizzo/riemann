#!/usr/bin/env python3
"""R186_052 — The Nyquist algebra of D_T.  SELF-CONTAINED (does not import r043/r051).  python3 r052_nyquist.py  (~2 min)

Conventions (Paper 47 eq:symbol/eq:form; R186_051 Thm 4.1 corrected by R186_117):
  F̂(τ) = ∫F e^{iτt},  c_F(u) = ∫F(t) conj F(t-u) dt,  ω_k = kπ/2T,  N = e^{2T},  θ_n = log n / log N ∈ (0,1).
  s_T(τ)   := C0 + ∫_{2T}^∞K + ∫_0^{2T}(1-cos τu)K(u)du - Σ_{log n<2T} v_n cos(τ log n)   (symbol with truncated Lévy; = σ_T + r_T)
  r_T(ω_k)  = ∫_{2T}^∞ cos(ω_k u)K(u)du = (-1)^k 2Σ_j e^{-(4j+1)T}(2j+½)/((2j+½)²+ω_k²)
  ĝ0(ω_k)   = 2∫_0^{2T}cosh(u/2)cos(ω_k u)du = (-1)^k sinh T/(¼+ω_k²)          w_k := s_k + 2ĝ0(ω_k) (full form W_T)
Parts:
  A  sampled symbol s_k, w_k: signs, minima, pole+tail merger e^T/(¼+ω²); the circulant cone {w_k ≥ 0} (S1) and S1(β)
  B  exact identities: (i) alias of m = ∫c_F K^per; (ii) 𝔞_T = ½[s(D_per)+s(D_anti)]; (iii) aliasing identity Δ_F
  C  Galerkin in the Fourier basis of I_T with both Tate functions: λ_J vs λ_A (r043/r117); matrix = ½(D_e + HᵀD_oH) entrywise
  D  discrete thm:Z: w_k = 4TΣ_ρ sinc(2T(ω_k-γ_ρ)/π) (+½v_N(-1)^k if e^{2T}=N integer), 150 zeros + smooth tail
  E  M₁ (quartet): symbol on the grid, S1, Toeplitz in k of comb / Lévy / quartet, Galerkin of M₁, Δ at the witness
"""
import sys, numpy as np
from numpy.polynomial import legendre as NL
from scipy.special import digamma, sici
from scipy.integrate import quad
from scipy.linalg import toeplitz, eigvalsh

C0 = float(digamma(0.25)) - np.log(np.pi)
GAM1 = 14.134725141734693
HERE = __file__.rsplit('/', 1)[0] if '/' in __file__ else '.'

# ----------------------------------------------------------------- symbol
def contacts(T):
    out = []
    for n in range(2, 100000):
        if np.log(n) >= 2 * T: break
        p = next(q for q in range(2, n + 1) if n % q == 0); r = n
        while r % p == 0: r //= p
        if r == 1: out.append((n, 2 * np.log(p) / np.sqrt(n)))
    return out

def m_arch(tau): return np.real(digamma(0.25 + 0.5j * np.asarray(tau, float))) - np.log(np.pi)
def K(u): return 2 * np.exp(-u / 2) / (1 - np.exp(-2 * u))
def Ktail(T): return np.log(1 / np.tanh(T / 2)) + np.pi - 2 * np.arctan(np.exp(T))
def omega(T, k): return np.asarray(k, float) * np.pi / (2 * T)

def r_grid(T, k):
    k = np.asarray(k); w = omega(T, k); out = np.zeros_like(w)
    for j in range(0, 60):
        a = 2 * j + 0.5; out += np.exp(-(4 * j + 1) * T) * a / (a * a + w * w)
    return 2 * (-1.0) ** k * out

def comb_grid(T, k, cs=None):
    cs = contacts(T) if cs is None else cs; w = omega(T, k); out = np.zeros_like(w)
    for n, v in cs: out += v * np.cos(w * np.log(n))
    return out

def s_grid(T, k, cs=None): return m_arch(omega(T, k)) + r_grid(T, k) - comb_grid(T, k, cs)
def g0_grid(T, k): return (-1.0) ** np.asarray(k) * np.sinh(T) / (0.25 + omega(T, k) ** 2)
def g1_grid(T, k):
    w2 = 0.25 + omega(T, k) ** 2
    return 2 * (-1.0) ** np.asarray(k) * ((np.sinh(T) + T * np.cosh(T)) / w2 - 0.5 * np.sinh(T) / w2 ** 2)
def w_grid(T, k, cs=None): return s_grid(T, k, cs) + 2 * g0_grid(T, k)

def quartet_grid(T, k, g, d):
    """Q(ω_k) = 8∫_0^{2T}cosh(δu)cos(γu)cos(ω_k u)du (the quartet ½±δ±iγ adds +Q to the symbol)."""
    w = omega(T, k); out = 0
    for b in (g + w, g - w):
        out = out + (d * np.sinh(2 * T * d) * np.cos(2 * T * b) + b * np.cosh(2 * T * d) * np.sin(2 * T * b)) / (d * d + b * b)
    return 4 * out

# ------------------------------------------------------- test functions on I_T
_GL = {}
def _lg(n):
    if n not in _GL: _GL[n] = NL.leggauss(n)
    return _GL[n]
def gl(T, n=4000):
    x, w = _lg(n); return T * x, T * w

def poly_test(T, coef):
    """F(t) = (T²-t²)² Σ coef_i (t/T)^i  (C¹ with F''' piecewise: |F̂|² ~ τ^{-8})."""
    return lambda t: (T * T - t * t) ** 2 * np.polyval(coef[::-1], t / T)

def fhat(F, T, tau, n=6000):
    t, w = gl(T, n); Ft = F(t) * w
    tau = np.atleast_1d(np.asarray(tau, float))
    return np.exp(1j * np.outer(tau, t)) @ Ft

def autocorr(F, T, u, n=4000):
    """c_F(u) = ∫_{-T+u}^{T} F(t)F(t-u)dt (F real), u ≥ 0; even."""
    u = abs(u); x, w = _lg(n); a, b = -T + u, T
    t = (a + b) / 2 + (b - a) / 2 * x; ww = (b - a) / 2 * w
    return float(np.real(np.sum(F(t) * np.conj(F(t - u)) * ww))) if u < 2 * T else 0.0   # Re c_F (complex F allowed)

def form_time(F, T, cs, quartet=None):
    """𝔞_T(F) in the x-space (Paper 47 thm:A) + optional quartet; returns (𝔞_T, ‖F‖², A, B, Lev, comb)."""
    n2 = autocorr(F, T, 0.0)
    lev = quad(lambda u: (n2 - autocorr(F, T, u)) * K(u), 0, 2 * T, limit=200, points=[1e-3, 0.1])[0]
    comb = sum(v * autocorr(F, T, np.log(n)) for n, v in cs)
    val = (C0 + Ktail(T)) * n2 + lev - comb
    if quartet is not None:
        g, d = quartet
        val += 2 * quad(lambda u: autocorr(F, T, u) * 4 * np.cos(g * u) * np.cosh(d * u), 0, 2 * T, limit=200)[0]
    t, w = gl(T); A = float(np.sum(F(t) * np.exp(t / 2) * w)); B = float(np.sum(F(t) * np.exp(-t / 2) * w))
    return val, n2, A, B, lev, comb

def Kper(T, v):
    """K^per(v) = Σ_{j≥1} K(4Tj - v), |v| < 2T  (alias of the Lévy tail)."""
    return sum(K(4 * T * j - v) for j in range(1, 40))

# ----------------------------------------------------------------- part A
def part_A():
    print("=== A. sampled symbol s_k (primitive) and w_k = s_k + 2ĝ0(ω_k) (full) on the grid ω_k = kπ/2T")
    print("    exact identity: 2ĝ0(ω_k) + r_T(ω_k)|_{j=0} = (-1)^k e^T/(¼+ω_k²)  (pole + first term of the Lévy tail)")
    for T in [0.5 * np.log(3), np.log(2), 0.5 * np.log(5), 0.5 * np.log(7), 1.0, 1.5, 2.0, 3.0, 5.0]:
        cs = contacts(T); k = np.arange(0, 4001); s = s_grid(T, k, cs); w = w_grid(T, k, cs)
        chk = 2 * g0_grid(T, k[:5]) + 2 * (-1.0) ** k[:5] * np.exp(-T) * 0.5 / (0.25 + omega(T, k[:5]) ** 2) - (-1.0) ** k[:5] * np.exp(T) / (0.25 + omega(T, k[:5]) ** 2)
        ns, nw = np.where(s < 0)[0], np.where(w < 0)[0]
        print(f" T={T:.4f} N=e^{{2T}}={np.exp(2*T):.2f} |𝒩_T|={len(cs)} 𝒜_T={sum(v for _,v in cs):.3f}  step π/2T={np.pi/2/T:.3f}  "
              f"pole+tail merger: max|err|={abs(chk).max():.1e}")
        print(f"   s_k<0 at k={ns.tolist()[:12]}{'…' if len(ns)>12 else ''} (#={len(ns)}, min={s.min():+.3f} at k={s.argmin()});  "
              f"w_k<0 at k={nw.tolist()[:12]}{'…' if len(nw)>12 else ''} (#={len(nw)}, min={w.min():+.3f} at k={w.argmin()})")
        print(f"   s_0..s_6 = {np.round(s[:7],3).tolist()}   w_0..w_6 = {np.round(w[:7],3).tolist()}")
        # S1(β): ∃β with s_k + β0 ĝ0 + β1 ĝ1 ≥ 0 ∀k?  2-dim LP: maximize t s.t. s_k + β·ĝ(ω_k) ≥ t.  (fine grid in β)
        g0, g1 = g0_grid(T, k), g1_grid(T, k); best = -np.inf
        for b0 in np.linspace(-30, 30, 241):
            vals = s + b0 * g0; m1 = (vals[:, None] + np.outer(g1, np.linspace(-30, 30, 241))).min(axis=0); best = max(best, m1.max())
        print(f"   S1(β): max_β min_k [s_k + β0ĝ0 + β1ĝ1] = {best:+.3f}  (≥0 ⟹ D_T trivial; <0: no grid certificate without ν)")

# ----------------------------------------------------------------- part B
def part_B():
    print("\n=== B. exact identities (tests with F = (T²-t²)² × random polynomial, non-primitive)")
    rng = np.random.default_rng(1)
    for T in [0.5 * np.log(3), np.log(2), 1.5]:
        cs = contacts(T)
        for trial in range(2):
            F = poly_test(T, rng.normal(size=4)); a, n2, A, B, lev, comb = form_time(F, T, cs)
            Kmax = 1500; k = np.arange(-Kmax, Kmax + 1); fk = np.abs(fhat(F, T, omega(T, k), n=8000)) ** 2
            s = s_grid(T, k, cs); m = m_arch(omega(T, k)); r = r_grid(T, k)
            nyq = (fk * s).sum() / (4 * T); nrm = fk.sum() / (4 * T)
            # (i) alias of m: (1/4T)Σ|F̂|² r_T(ω_k) = ∫_{-2T}^{2T} c_F(v) K^per(v) dv
            alias_grid = (fk * r).sum() / (4 * T)
            alias_int = quad(lambda v: autocorr(F, T, v) * (Kper(T, v) + Kper(T, -v)), 0, 2 * T, limit=200)[0]
            # (ii) two spin structures: periodic (coarse grid kπ/T) and antiperiodic ((k+½)π/T)
            even = (fk[k % 2 == 0] * s[k % 2 == 0]).sum() / (2 * T); odd = (fk[k % 2 != 0] * s[k % 2 != 0]).sum() / (2 * T)
            # (iii) Δ_F = ∫_0^{2T}K(2T-v)c_F(v)dv + Σ v_n c_F(2T - log n)   ⟹ 𝔞 = even + Δ = odd - Δ (unchanged formula)
            Delta = quad(lambda v: K(2 * T - v) * autocorr(F, T, v), 0, 2 * T, limit=200, points=[2 * T - 1e-3])[0] \
                + sum(v * autocorr(F, T, 2 * T - np.log(n)) for n, v in cs)
            print(f" T={T:.4f} #{trial}: 𝔞_T={a:+.6f}  Nyquist(s_T)={nyq:+.6f} (err {abs(a-nyq):.1e}; ‖F‖² err {abs(n2-nrm):.1e})"
                  f"  alias of m: grid {alias_grid:+.3e} vs ∫c_F K^per {alias_int:+.3e}")
            print(f"      s(D_per)={even:+.6f}  s(D_anti)={odd:+.6f}  ½(sum)={(even+odd)/2:+.6f}  Δ_F={Delta:+.6f}  "
                  f"even+Δ={even+Delta:+.6f}  odd-Δ={odd-Delta:+.6f}  (both = 𝔞_T; truncation K=1.5e3 on |F̂|²~k^-8)")

# ----------------------------------------------------------------- part C
def fourier_matrix(T, J, cs, quartet=None, nq=3000):
    """M_{jj'} = 𝔞_T(e_j, e_j'), e_j = e^{ijπt/T}/√2T, |j| ≤ J, in the x-space (exact up to composite GL quadrature)."""
    js = np.arange(-J, J + 1); Om = js * np.pi / T; D = Om[:, None] - Om[None, :]  # ω_{2j} - ω_{2j'}
    def c(u):   # c_{jj'}(u), u ≥ 0:  (1/2T) e^{iω_{2j'}u} ∫_{-T+u}^{T} e^{iΔt} dt
        with np.errstate(divide='ignore', invalid='ignore'):
            I = np.where(abs(D) < 1e-12, 2 * T - u, (np.exp(1j * D * T) - np.exp(1j * D * (-T + u))) / (1j * D))
        return np.exp(1j * Om[None, :] * u) * I / (2 * T)
    def cs_even(u):  # ½(c(u) + c(-u)),  c(-u) = conj(c(u))ᵀ
        cu = c(u); return 0.5 * (cu + cu.conj().T)
    M = (C0 + Ktail(T)) * np.eye(2 * J + 1) + 0j
    x, w = _lg(64); edges = np.linspace(0, 2 * T, nq // 64 + 1)
    for lo, hi in zip(edges[:-1], edges[1:]):
        for u, ww in zip((hi + lo) / 2 + (hi - lo) / 2 * x, (hi - lo) / 2 * w):
            Ce = cs_even(u); M += (np.eye(2 * J + 1) - Ce) * (K(u) * ww)
            if quartet is not None:
                g, d = quartet; M += Ce * (8 * np.cos(g * u) * np.cosh(d * u) * ww)
    for n, v in cs: M -= v * cs_even(np.log(n))
    a = (-1.0) ** js * 2 * np.sinh(T / 2) / (np.sqrt(2 * T) * (0.5 + 1j * js * np.pi / T))   # A(e_j)
    b = (-1.0) ** js * 2 * np.sinh(T / 2) / (np.sqrt(2 * T) * (0.5 - 1j * js * np.pi / T))   # B(e_j)
    return M, a, b

def nyquist_matrix(T, J, cs, L=400000, quartet=None):
    """½(D_e + HᵀD_oH) truncated: D_e = diag s(ω_{2j}), (HᵀD_oH)_{jj'} = Σ_{|l|≤L} s(ω_{2l+1}) h_{l-j} h_{l-j'}, h_m = 2(-1)^m/(π(2m+1))."""
    js = np.arange(-J, J + 1); se = s_grid(T, 2 * js, cs)
    if quartet is not None: se = se + quartet_grid(T, 2 * js, *quartet)
    M = 0.5 * np.diag(se); l = np.arange(-L, L + 1)
    so = s_grid(T, 2 * l + 1, cs)
    if quartet is not None: so = so + quartet_grid(T, 2 * l + 1, *quartet)
    for ch in range(0, len(l), 50000):
        ll = l[ch:ch + 50000]; mm = ll[:, None] - js[None, :]
        H = 2 * (-1.0) ** mm / (np.pi * (2 * mm + 1)); M += 0.5 * H.T @ (so[ch:ch + 50000, None] * H)
    return M

def primitive_min(M, a, b):
    """λ_min of M over {c: Σc_j a_j = Σ c_j b_j = 0} (orthonormal basis of the complement)."""
    Q = np.linalg.qr(np.stack([a.conj(), b.conj()], axis=1), mode='complete')[0][:, 2:]
    Mp = Q.conj().T @ M @ Q; Mp = 0.5 * (Mp + Mp.conj().T)
    ev, V = np.linalg.eigh(Mp); return ev, Q @ V[:, 0]

def part_C():
    print("\n=== C. Galerkin in the Fourier basis of I_T (e_j = e^{ijπt/T}/√2T, |j|≤J) with both Tate functions: λ_J ≥ λ_A; matrix vs ½(D_e+HᵀD_oH)")
    ref = {0.5 * np.log(3): 9.486e-4, np.log(2): 1.042e-7, 0.5 * np.log(5): 3.84e-12}
    out = {}
    for T, lam in ref.items():
        cs = contacts(T)
        for J in (12, 24, 40):
            M, a, b = fourier_matrix(T, J, cs); Mr = M.real
            ev, c = primitive_min(Mr, a, b)
            msg = f" T={T:.4f} J={J}: λ_J={ev[0]:+.4e} (λ_A ref {lam:+.3e}; λ_2={ev[1]:+.3e}; n_-={int((ev<0).sum())}; max|Im M|={abs(M.imag).max():.1e})"
            if J == 24:
                N = nyquist_matrix(T, J, cs); err = abs(Mr - N).max()
                evN, _ = primitive_min(N, a, b)
                msg += f"\n      |M_Fourier − ½(D_e+HᵀD_oH)|_max = {err:.2e} (L=4e5; tail ~log L/L)  λ_J(Nyquist)={evN[0]:+.4e}"
            print(msg)
        out[T] = (c, a, b)
    return out

# ----------------------------------------------------------------- part D
def part_D():
    print("\n=== D. discrete thm:Z: w_k vs 4TΣ_ρ sinc(2T(ω_k-γ_ρ)/π) (150 exact zeros + smooth tail N'(t)=log(t/2π)/2π; NUMERICAL)")
    zs = np.load(HERE + '/zeros150.npy'); G = zs[-1]
    for T in [0.6, np.log(2), 1.0, 1.7]:
        cs = contacts(T); N = np.exp(2 * T); edge = 0.0
        nN = int(round(N))
        if abs(N - nN) < 1e-9:   # boundary contact: ½ convention of the explicit formula
            p = next(q for q in range(2, nN + 1) if nN % q == 0); r = nN
            while r % p == 0: r //= p
            if r == 1: edge = 0.5 * 2 * np.log(p) / np.sqrt(nN)
        ks = np.array([0, 1, 2, 3, 5, 8, 13, 21]); w = w_grid(T, ks, cs); rows = []
        for k, wk in zip(ks, w):
            om = omega(T, k); x = 2 * T * (om - zs) / np.pi; y = 2 * T * (om + zs) / np.pi
            main = 4 * T * (np.sinc(x).sum() + np.sinc(y).sum())
            # tail: ∫_G^∞ (log(t/2π)/2π)[4T sinc(2T(ω-t)/π) + 4T sinc(2T(ω+t)/π)]dt = (-1)^k ∫_G^∞ (log(t/2π)/π) sin(2Tt)[1/(t-ω)+1/(t+ω)]...
            # 4T sinc(2T(ω-t)/π) = 2 sin(2T(t-ω))/(t-ω); on the grid sin(2T(t-ω_k)) = (-1)^k sin(2Tt)
            f = lambda t: (np.log(t / (2 * np.pi)) / np.pi) * (1 / (t - om) + 1 / (t + om))
            tail = (-1) ** k * quad(f, G, np.inf, weight='sin', wvar=2 * T, limit=400)[0]
            rows.append((k, wk, main + tail + edge * (-1) ** k, main, tail))
        print(f" T={T:.4f} (N={N:.3f}{', boundary contact n=%d, ½v_N(-1)^k added (½ convention at the jump)' % nN if edge else ''})")
        for k, wk, tot, main, tail in rows:
            print(f"   k={k:2d}: w_k={wk:+.4f}  4TΣsinc(150 zeros)+tail={tot:+.4f} (zeros {main:+.4f}, tail {tail:+.4f})  diff={wk-tot:+.4f}")

# ----------------------------------------------------------------- part E
def part_E(witness):
    print("\n=== E. M₁ = ζ × quartet (γ₁, δ): symbol on the grid, Toeplitz in k, Fourier Galerkin, Δ at the witness")
    for T in [np.log(2), 0.5 * np.log(3)]:
        cs = contacts(T); k = np.arange(0, 4001)
        for d in (0.01, 0.1):
            q = quartet_grid(T, k, GAM1, d); s = s_grid(T, k, cs); sM = s + q
            print(f" T={T:.4f} δ={d}: Q(ω_k) at k≤6: {np.round(q[:7],4).tolist()};  max|Q|={abs(q).max():.3f} at k={abs(q).argmax()} "
                  f"(ω={omega(T, abs(q).argmax()):.2f}; γ₁=14.13);  #{{s_k<0}}={int((s<0).sum())} → #{{s_k^{{M₁}}<0}}={int((sM<0).sum())}")
        # Toeplitz in k (n=80): comb p_k (exact positive type), Lévy ℓ_k := ∫_0^{2T}cos(ω_k u)K_reg, quartet q_k
        n = 80; kk = np.arange(0, n); p = comb_grid(T, kk, cs); q = quartet_grid(T, kk, GAM1, 0.1)
        lev = np.array([quad(lambda u: (1 - np.cos(omega(T, kq) * u)) * K(u), 0, 2 * T, limit=200)[0] for kq in kk])
        e_p, e_l, e_q = (eigvalsh(toeplitz(x)) for x in (p, -lev, q))
        print(f"   Toeplitz_{n}[x_{{k-l}}]: comb λ_min={e_p[0]:+.3e} (≥0 exact: measure Σv_nδ_{{θ_n}} ≥ 0), "
              f"−L_T (conditionally negative type) λ_max={e_l[-1]:+.3e}, #λ>0={int((e_l>1e-9).sum())} (n−1 expected: ≤1 negative, Schoenberg), quartet λ_min={e_q[0]:+.3e} λ_max={e_q[-1]:+.3e}")
    # Fourier Galerkin for M₁ at log 2
    T = np.log(2); cs = contacts(T)
    for d in (0.1, 0.01):
        M, a, b = fourier_matrix(T, 24, cs, quartet=(GAM1, d)); ev, c = primitive_min(M.real, a, b)
        N = nyquist_matrix(T, 24, cs, quartet=(GAM1, d)); evN, _ = primitive_min(N, a, b)
        # Δ at the minimizer: Δ_F = ∫_0^{2T}K(2T-v)c_F(v)dv + Σ v_n c_F(2T-log n); form = even + Δ
        js = np.arange(-24, 25); F = lambda t: (np.exp(1j * np.outer(t, js) * np.pi / T) @ c) / np.sqrt(2 * T)
        Fr = lambda t: F(np.atleast_1d(t)) if np.ndim(t) else F(np.array([t]))[0]
        Delta = quad(lambda v: K(2 * T - v) * autocorr(Fr, T, v), 0, 2 * T, limit=200, points=[2 * T - 1e-3])[0] \
            + sum(v * autocorr(Fr, T, 2 * T - np.log(n)) for n, v in cs) \
            - 8 * quad(lambda v: autocorr(Fr, T, v) * np.cos(GAM1 * (2 * T - v)) * np.cosh(d * (2 * T - v)), 0, 2 * T, limit=300)[0]   # quartet wrap
        se = s_grid(T, 2 * js, cs) + quartet_grid(T, 2 * js, GAM1, d); even = float(np.sum(se * abs(c) ** 2))
        n2 = float(np.sum(abs(c) ** 2))
        print(f" M₁(log 2, δ={d}) Fourier-Galerkin J=24: λ_J={ev[0]:+.4e} (Nyquist matrix {evN[0]:+.4e}); minimizer: ‖c‖²={n2:.4f}, "
              f"s(D_per)={even:+.4e}, Δ_F={Delta:+.4e}, even+Δ={even+Delta:+.4e} (=λ_J·‖c‖² if exact)")
        neg = se < 0; print(f"     minimizer energy on even modes with s^{{M₁}}_{{2j}}<0 (j={js[neg].tolist()}): {float(np.sum(abs(c[neg])**2))/n2:.3f};"
              f" min_j s^{{M₁}}(ω_{{2j}})={se.min():+.3f}")

if __name__ == '__main__':
    parts = sys.argv[1] if len(sys.argv) > 1 else 'ABCDE'
    if 'A' in parts: part_A()
    if 'B' in parts: part_B()
    wit = part_C() if 'C' in parts else None
    if 'D' in parts: part_D()
    if 'E' in parts: part_E(wit)
