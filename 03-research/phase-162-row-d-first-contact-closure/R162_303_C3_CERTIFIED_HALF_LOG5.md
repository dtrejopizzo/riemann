# R162_303 — C3: certified positivity of the primitive form at T = ½log5

Status: **CERTIFIED (machine-verified, ball arithmetic)**, pending audit.
Scripts and certificate data: `scripts/c3/`. Paper 47 and all other files are untouched.

Notation is Paper 47's: a_T is the truncated Weil form (eq:form), P_T = {A = B = 0} is the primitive
subspace, λ_A(T) is the bottom of a_T on the unit sphere of P_T, and e_l(t) = √((2l+1)/2T) P_l(t/T).
Also s_T(τ) = m(τ) − Σ_{n∈N_T} v_n cos(τ log n), m(τ) = Re ψ(¼+iτ/2) − log π, v_n = 2Λ(n)/√n.
At T₀ = ½log5 the contact set is N_T = {2,3,4}, with Σv_n = A_T = 2.94186….

## 0. Result

**Theorem C3.** At T₀ = ½ log 5 = 0.804719…,

    λ_A(T₀) ≥ 2.5·10⁻¹² > 0,
    split by parity: λ_even(T₀) ≥ 2.5·10⁻¹² and λ_odd(T₀) ≥ 3.0·10⁻¹⁰.

(Each μ is an Arb ball of radius < 10⁻²⁰⁰ around the decimal shown, so the proved bound is the
decimal minus 10⁻²⁰⁰.)

**Corollary.** λ_A is nonincreasing (lem:monoT), so λ_A(T) ≥ 2.5·10⁻¹² for every T ≤ ½log5.
By R162_103 Prop. 5.1, **first contact is excluded on the whole first chamber 0.8 < T < ½log5.** By the
continuity of λ_A (R162_001), positivity also holds on some interval to the right of ½log5, but its
length is not explicit.

This is the first certified positivity of the primitive form beyond Zhu's T ≤ 0.8. It covers the
primitive form only: the complete form W_T (with the polar term 2AB) is not treated. The numbers are
consistent with the doubly exponential decay −log λ ≍ e^{2T}: the even bottom is about 2.5·10⁻¹².

**Validation.** The same code at T = ½log3 (N_T = {2}, even sector, τ_N = 40) certifies
λ_even ≥ 6.3·10⁻⁴ and fails at 6.5·10⁻⁴. A float Galerkin computation of the same lower form gives
6.39·10⁻⁴. Both are consistent with Paper 47 thm:C (λ_A ≥ λ^P ≥ 8.86·10⁻⁵).

## 1. The lower form (frequency truncation, primes included)

Since a_T(F) = (1/2π)∫ s_T |F̂|² is a Fourier multiplier compressed to I_T, the prime comb goes into
the multiplier, and no operator-norm bound on Π_T is needed. Fix τ_N > 0 and choose s_∞ ≤ m(τ_N) − A_T.
Define

    s_under = s_T on |τ| ≤ τ_N,   s_under = s_∞ on |τ| > τ_N.

m is increasing on [0,∞) (lem:mbounds(i)), so for |τ| > τ_N we have s_T(τ) ≥ m(τ) − A_T ≥ s_∞.
Hence s_under ≤ s_T everywhere. There are no chords and no band loss: on |τ| ≤ τ_N the minorant is
exact.

Write s_under = s_∞ − g, with g = (s_∞ − s_T)·1_{|τ|<τ_N} bounded and indefinite, and put
G = Q_T g(D) Q_T. For every μ,

    a_T(F) − μ‖F‖² ≥ b_μ(F) := (s_∞ − μ)‖F‖² − ⟨GF,F⟩.

Split g = g₊ − g₋ with g_± ≥ 0. Then:
- g₊ ≤ ω₊ := s_∞ − C₀ + A_T, because s_T ≥ C₀ − A_T.
- g₋ ≤ ω₋ := m(τ_N) + A_T − s_∞.
- G_± := Q_T g_±(D) Q_T satisfy 0 ≤ G_± ≤ ω_± S_{c*}, where c* = Tτ_N (thm:P).

For l − i even,

    G_il = (2T/π) √((2i+1)(2l+1)) (−1)^{(l−i)/2} ∫₀^{τ_N} g(τ) j_i(τT) j_l(τT) dτ,

and G_il = 0 for l − i odd. The operator a_T commutes with t ↦ −t. Also P_T ∩ L²_par = ker⟨·,χ_par⟩,
with χ₀ = cosh(t/2) and χ₁ = sinh(t/2). So λ_A = min(λ_even, λ_odd), and each parity is treated
separately.

## 2. Rigorous enclosures

All arithmetic is Arb ball arithmetic (python-flint 0.9.0, vendored in phase-118) at 640 bits.
- **Quadrature.** τ ∈ [0, τ_N] is cut into panels of length h = ½, each with the Arb-rigorous
  Gauss–Legendre rule of N = 46 nodes (`arb.legendre_p_root`, which returns certified nodes and
  weights). The error bound is the Bernstein-ellipse bound |I − I_N| ≤ L·(64/15)·M·ρ^{−2N}/(ρ² − 1)
  (Trefethen 2008, Thm 4.5), with L = h/2 and ρ = 3.2. The ellipse lies in the disk of radius
  L(ρ+1/ρ)/2 = 0.439 < ½, and the poles of ψ(¼ ± iτ/2) sit at |Im τ| ≥ ½, so the integrand is
  analytic there. M bounds the integrand's modulus on the ellipse and is built from three pieces:
  - |j_n(z)| ≤ e^{|Im z|}, from j_n(z) = ½(−i)ⁿ∫_{−1}^{1}P_n(u)e^{izu}du.
  - |cos(τ log n)| ≤ cosh(η log n).
  - An enclosure of |ψ| on a box. It uses ψ(w) = ψ(w+8) − Σ_{k<8} 1/(w+k) together with the Binet
    bound |ψ(u)| ≤ log|u| + π/2 + 1/(2Re u) + 1/(12(Re u)²) for Re u ≥ 8, which follows from
    |1/(eᵗ−1) − 1/t + ½| ≤ t/12. Arb's digamma returns NaN on wide boxes, which is why this bound
    is needed.

  The resulting error, before the prefactor, is 1.5·10⁻⁴³ per entry, uniform in (i,l), and it is
  added as a ball to every entry.
- **Special functions.** j_l(τT) = √(π/2x) J_{l+½}(x) and χ_l = ⟨e_l,χ_par⟩ = √((2l+1)/2T)·2T·i_l(T/2)
  come from Arb's Bessel functions. At 320 bits Arb returns valid but useless balls for l ≳ 300 near
  x ≈ 190, so the run uses 640 bits and asserts that every Bessel ball has radius < 10⁻⁶⁰.
  The quantities m(τ_N), C₀ = m(0) and the node values of ψ come from Arb's digamma at points.
  ‖χ₀‖² = sinh T + T and ‖χ₁‖² = sinh T − T.
- **Trace tails.** Λ_K(c*) ≤ Λ*_K(c*) (cor:P1), a series of rationals in c* with a certified
  geometric tail.

## 3. Schur step (prop:haynsworth adapted to an indefinite G)

Let E be the span of e_l, l < K, of parity par, let Y be its complement in L²_par, and let
b(F,ξ) = b_μ(F) + 2ξ⟨F,χ_par⟩.

(a) **Bound on Y.** b|_Y ≥ q_Y := s_∞ − μ − ω₊Λ_K(c*). This holds because P_Y G P_Y ≤ P_Y G₊ P_Y,
and ‖P^⊥G₊P^⊥‖ ≤ ω₊ tr(P^⊥S_{c*}P^⊥) = ω₊Λ_K(c*), where P^⊥ removes all modes below K.

(b) **Columns.** The columns coupling E to Y are −P_Y G e_i and P_Y χ. Their Gram matrix is an exact
sum over the parity modes K ≤ l < K₂, plus boxes from the modes ≥ K₂:
- For the G columns: ‖P^⊥_{K₂} G_± e‖² ≤ ‖P^⊥G_±P^⊥‖·⟨G_± e,e⟩ ≤ ω_±² Λ_{K₂}(c*). Hence
  ‖P^⊥_{K₂} G e‖ ≤ β := (ω₊+ω₋)√Λ_{K₂}.
- For χ: ‖P_{≥K₂}χ‖² = ‖χ‖² − Σ_{l<K₂} χ_l².

The Schur complement 𝔰 of b|_Y (with b|_Y ≥ q_Y > 0) then satisfies 𝔰 ≥ 𝖱 with

    𝖱_ij  = (s_∞ − μ)δ_ij − G_ij − ⟨P_Y G e_i, P_Y G e_j⟩ / q_Y,
    𝖱_iξ  = χ_i + ⟨P_Y G e_i, P_Y χ⟩ / q_Y,
    𝖱_ξξ  = −‖P_Y χ‖² / q_Y,

and n₋(b) = n₋(𝔰) ≤ n₋(𝖱).

(c) **Inertia.** 𝖱_ξξ ≈ −10⁻¹⁹⁰, so dividing by it is unusable. Two steps avoid it:
- Replace 𝖱_ξξ by −δ′, where δ′ ≥ ‖P_Yχ‖²/q_Y is a certified exact number. This lowers 𝖱, so the
  inequality n₋(𝖱) ≤ n₋(𝖱′) goes the right way.
- Apply the exact congruence diag(H,1), where H is a binary64 Householder matrix sending mid(𝖱_{X,ξ})
  to a multiple of e₀. H is invertible because ‖HᵀH − I‖_∞ < 1 is checked in balls.

In the new coordinates (t, ξ | y), the 2×2 block B on (t, ξ) has det B < 0 (certified), so its
inertia is (1,1). By Haynsworth, inertia(𝖱′) = (1,1) + inertia(S), where S = 𝖱′_yy − 𝖱′_{y,B}B⁻¹𝖱′_{B,y}.
Interval Cholesky shows that every pivot of S is > 0, so n₋(𝖱) ≤ 1.

(d) **Conclusion.** n₋(b) ≤ 1. lem:border then gives n₋(b_μ|_{ker⟨·,χ_par⟩}) = 0, that is,
a_T ≥ μ on P_T ∩ L²_par.

## 4. Certificate data (T₀ = ½log5, τ_N = 240, K = 280, K₂ = 330, 640 bits)

| quantity | even | odd |
|---|---|---|
| dim E | 140 | 140 |
| s_∞ (from m(τ_N) = 3.64276…) | 0.700787608327… | same |
| ω₊, ω₋ | 9.0150, 5.8839 | same |
| Λ*_K(c*), Λ*_{K₂}(c*), c* = 193.13 | 4.4·10⁻²⁰, 3.9·10⁻⁷⁰ | same |
| q_Y | 0.70079 | 0.70079 |
| β | 2.9·10⁻³⁴ | 2.9·10⁻³⁴ |
| max entry radius of 𝖱 | 4.4·10⁻⁴¹ | 4.4·10⁻⁴¹ |
| Cholesky of S succeeds at μ | 0, 5e-13, …, **2.5e-12** | 0, 1e-11, …, **3e-10** |
| Cholesky fails (no claim) at μ | 3e-12 | 4e-10 |
| diagnostic λ_min(mid S, μ=0), mpmath 50 digits | 2.5308·10⁻¹² | 3.6204·10⁻¹⁰ |

The Cholesky threshold agrees with the diagnostic eigenvalue in both parities. Two runs are recorded,
`cert_*_run1.json` (7 values of μ) and `c3_log5_*.json` (3 values of μ), and they give identical
results. Each run takes about 6 min per parity. The float prototype gives Galerkin bottoms of the same
lower form of 2.25·10⁻¹² (τ_N = 200) and 2.57·10⁻¹² (τ_N = 250) in the even sector; these are
diagnostic only. For the odd sector at τ_N = 160 the lower form is already negative (−2·10⁻⁹): τ_N must
exceed about 200, which is roughly the envelope scale 2πe^{A_T} ≈ 119 with margin.

No certified *upper* bound on λ_A(T₀) is given. The diagnostic values say that the certified lower
bound is within a small factor of the true bottom, which is of order 10⁻¹².

## 5. What the proof uses (audit checklist)

- From Paper 47: lem:mbounds(i) (m increasing, m(0) = C₀), thm:P (trace identity and Ky Fan tail),
  cor:P1, lem:border, lem:monoT, and the parity splitting of P_T.
- Adapted in §3: prop:haynsworth for an indefinite G (the proof is given in §3).
- External: Trefethen's Gauss-quadrature bound; DLMF 10.54.2 and ∫_{−1}^{1}P_l(u)e^{xu}du = 2i_l(x);
  Binet's formula; the Arb enclosures of digamma, Bessel J/I and the Legendre roots and weights.
- **Deviation from the brief:** the arithmetic is Arb (python-flint), not mpmath.iv. It is equally
  rigorous and it was needed for speed (≈7.3M Bessel evaluations per parity).
- **Non-rigorous inputs:** only the floating-point Householder matrix and the midpoint data. Both
  enter through an exact congruence whose invertibility is checked.

## 6. Files (`scripts/c3/`)

- `c3_cert.py` is the certificate. Usage: `python3 c3_cert.py log5 <par> <mu list> 240 640 280 330 46`.
- `c3_log5_par{0,1}_tauN240_K280_N46.json` and `cert_log5_par{0,1}_run1.json` are the outputs;
  `run2_*.log` are the logs.
- `c3_log3test_par0_tauN40_K50_N30.json` is the ½log3 validation run.
- `c3_diag_eig.py` is the diagnostic eigenvalue check. Its `S_mid` inputs are not archived.
- `c3_float_prototype.py` is the float prototype (diagnostic).
