# R186_052 — The Nyquist algebra of D_T: circle 𝕋_{4T}, two spin structures, unified measure μ_T, the two cones, and the test with M₁

Phase 186, round 25. Paper 47, grid and crossword are not touched. Standalone script: `r052_nyquist.py` (`python3 r052_nyquist.py [ABCDE]`, ≈ 6 min; does not import r043/r051). Read: R186_051 §4,
R186_117 (correction: the identity is exact only with the truncated Lévy measure), Paper 47 eq:symbol, eq:form, eq:W, thm:A, def:PD,
def:W, thm:Z, lem:mbounds, lem:gbounds.

## 0. Verdict

1. **The algebra exists and is exact.** The truncated form is the compression to the half-circle I_T = (−T, T) of a Fourier
 multiplier on the circle 𝕋_{4T} = ℝ/4Tℤ whose eigenvalues are the samples of the truncated symbol (Theorem 2.1): 𝔞_T = P_{I_T} s(D_{𝕋_{4T}}) P_{I_T}.
 Equivalently (Theorem 2.2, "two spin structures"): **𝔞_T = ½[s(D_per) + s(D_anti)]** on L²(I_T), with D_per, D_anti the two
 self-adjoint extensions of −i d/dt on I_T with condition F(T) = ±F(−T); each summand is diagonal in its own exponential basis
 with eigenvalues s_T(kπ/T) and s_T((k+½)π/T). On ℓ²(ℤ): 𝔞_T ≅ ½(D_e + HᵀD_oH), H the unitary half-step shift
 (h_m = 2(−1)^m/(π(2m+1))) (Theorem 2.3). Verified: identity to 10⁻¹⁵ (§8 B), entrywise Fourier Galerkin matrix to 3·10⁻⁶ (§8 C).
2. **Unified measure.** The sampled symbol is the cosine transform on the grid πk/2T of a SINGLE signed measure on [0, 2T],
 μ_T = c_T δ₀ + K(u)du − Σ_{n∈𝒩_T} v_n δ_{log n} (δ₀ renormalized against 1 − cos; §1): s_k = c_T + ∫₀^{2T}(1 − cos ω_k u)K(u)du − Σ v_n cos(ω_k log n).
 With σ_T of Paper 47 (full m) there is aliasing ∫c_F K^per (§1, verified to 10⁻¹⁵ with the closed form of R186_117).
3. **The two cones.** 𝒦_T = Nyquist samples of {f ≥ 0 ∈ PW_{2T} ∩ L¹ with a double zero at ±i/2} (Akhiezer; Theorem 3.1); Tate is the
 weight (τ² + ¼)² (Cor. 3.2). 𝒦_T^{(0)*} = samples of the sinc-smoothed positive measures (Theorem 3.3, "window Bochner" = Kreĭn).
 **D_T ⟺ (s_k)_k ∈ 𝒦_T^*** (Theorem 3.4, discrete thm:Z, PROVED as a reformulation) ⟺ ∃ μ ≥ 0, β: (ω_k² + ¼)²... (primitive form: Cor. 3.5).
 The "circulant" cone {w_k ≥ 0 ∀k} (sharp-cutoff-on-the-grid certificate) is strictly smaller and **fails in every window**,
 even with the two Tate parameters and modulo the annihilator (−1)^k (§3.3, NUMERICAL): the difference between "positive on the circle" and
 "positive on the half-circle" is exactly the content of D_T.
4. **Quasi-periodic structure.** The sampled comb p_k = Σ v_n cos(πkθ_n), θ_n = log n/log N, is a sequence of positive type
 (Herglotz) with atomic spectral measure Σ v_n ½(δ_{θ_n} + δ_{−θ_n}) on ℝ/2ℤ; the Lévy part L_k = ∫₀^{2T}(1 − cos πkθ)·2TK(2Tθ)dθ
 is of conditionally negative type (Lévy–Khintchine on ℤ); the sum s_k = c_T + ∫(1 − cos πkθ)d(κ_T + ν_T) has POSITIVE Lévy
 measure κ_T + ν_T and constant c_T = C₀ + ∫_{2T}^∞K − 𝒜_T (§4). The complex comb Σ v_n e^{iπkθ_n} has all its frequencies in
 (0, π): the sine comb is the discrete Hilbert transform of the cosine comb (Hardy, §4.3). None of this carries the sign: Bochner–Herglotz
 on ℤ characterizes positivity on the full circle (circulant cone), not on the half-circle (Kreĭn).
5. **Decisive test with M₁ (NO-GO for the proposed property).** M₁ has the same primes: the Toeplitz positivity of the comb is
 identical for ζ and M₁ (λ_min = −10⁻¹³ in both, §5); the quartet adds to the symbol an indefinite Toeplitz Q(ω_k) (±8.7, ±10.9), as does
 the Lévy part. **The structural property that M₁ breaks is none of those in §4**: it is D_T itself. What the algebra does show
 (NUMERICAL, §5.2): the extremal vector of 𝒫_T at log 2, for ζ (λ = +1.3·10⁻⁷) and for M₁ (−1.4·10⁻³, −1.6·10⁻⁶), has **99.4% of its
 energy in the antiperiodic sector** at the three points k = ±1, ±3, ±5 where s_k < 0 (40% at k = ±3), s(D_per)(h) = +0.43 / +0.99,
 s(D_anti)(h) = −0.43 / −0.99: λ_A is the cancellation of two sectors of opposite sign, with 0.3% of energy in negative even modes.
6. **Contact with the sign: none.** Row D: OPEN. New tools: Theorems 2.1–2.4, 3.1–3.5, Lemma 6.1 (localization of the witness
 on the grid), Lemma 6.2 (aliasing sandwich). Falsifiers in §7.

## 1. The Nyquist identity, exact (PROVED; R186_051 Thm 4.1 with the correction of R186_117)

Paper 47 conventions: F̂(τ) = ∫F e^{iτt}, c_F(u) = ∫F(t)F̄(t−u)dt, ĉ_F = |F̂|², supp c_F ⊂ [−2T, 2T], c_F(±2T) = 0; ω_k := kπ/2T;
N := e^{2T}; 𝒩_T = {n ≥ 2 : log n < 2T}; v_n = 2Λ(n)/√n; 𝒜_T = Σ v_n; K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)) (Paper 47 lem:K).

**Def. 1.1 (unified window measure).** μ_T := c_T δ₀ + K(u)du|_{(0,2T)} − Σ_{n∈𝒩_T} v_n δ_{log n}, with c_T := C₀ + ∫_{2T}^∞K − 𝒜_T,
and renormalized cosine transform ŝ_T(τ) := c_T + ∫₀^{2T}(1 − cos τu)K(u)du + Σ v_n(1 − cos τ log n) = C₀ + ∫_{2T}^∞K + L_T(τ) − P_T(τ) =: s_T(τ),
L_T(τ) := ∫₀^{2T}(1 − cos τu)K(u)du, P_T(τ) := Σ v_n cos(τ log n). (This is the s_T of R186_051(d)/R186_117: σ_T + ∫_{2T}^∞cos(τu)K(u)du.)
*Note.* Σ v_n(1 − cos) − 𝒜_T = −P_T: the comb enters the Lévy measure with sign +, the constant absorbs −𝒜_T. Both writings
("signed measure μ_T" and "positive Lévy measure κ_T + ν_T with constant c_T") are the same sequence s_k (§4.2).

**Theorem 1.2 (Nyquist; PROVED).** For every F ∈ L²(I_T), in [0, ∞] and absolutely convergent in the form domain:
 𝔞_T(F) = (1/4T) Σ_{k∈ℤ} |F̂(ω_k)|² s_T(ω_k), ‖F‖² = (1/4T)Σ_k|F̂(ω_k)|², W_T(F) = (1/4T)Σ_k|F̂(ω_k)|² w_k, w_k := s_T(ω_k) + 2ĝ₀(ω_k).
*Proof.* R186_117 §1 (Poisson over c_F * ν with ν a finite even measure of support [−2T, 2T] with no atoms at ±2T, plus μ_ε and monotone convergence
for K ~ 1/u). W_T = 𝔞_T + 2Re(AB̄) and 2Re AB̄ = 2∫_{−2T}^{2T}Re c_F(u)cosh(u/2)du is the same identity with ν = 2cosh(u/2)1_{|u|<2T}du. ∎
**Aliasing of m (PROVED, R186_117 §0; re-verified §8 B).** (1/4T)Σ_k|F̂(ω_k)|² m(ω_k) = (1/2π)∫m|F̂|² − ∫_{−2T}^{2T}Re c_F(v)K^per(v)dv,
K^per(v) := Σ_{j≥1}K(4Tj − v). Hence the identity with the full m is FALSE; with s_T it is exact. On the grid,
r_T(ω_k) := s_T(ω_k) − σ_T(ω_k) = (−1)^k 2Σ_{j≥0} e^{−(4j+1)T}(2j+½)/((2j+½)² + ω_k²).
**Lemma 1.3 (pole + tail merge; PROVED, elementary).** ĝ₀(ω_k) = (−1)^k sinh T/(¼ + ω_k²) (Paper 47 lem:gbounds on the grid: sin 2Tω_k = 0),
and 2ĝ₀(ω_k) + [j = 0 term of r_T] = (−1)^k e^T/(¼ + ω_k²). Hence
 w_k = m(ω_k) − P_T(ω_k) + (−1)^k [ e^T/(¼ + ω_k²) + 2Σ_{j≥1}e^{−(4j+1)T}(2j+½)/((2j+½)² + ω_k²) ].
Verified to 10⁻¹⁷ (§8 A). The pole and the Lévy tail enter **only** through the alternating (−1)^k·(positive decreasing) component.
**Convergence (CITED R186_117 §3).** s_T(ω_k) = log k + O(1); Plancherel–Pólya gives absolute convergence exactly in the domain of the
form; for F with a jump at ±T the tail is ≍ (F(T)² + F(−T)²)(2T/π)² log K/K. In this memo all numerical tests use F ∈ C¹ with
|F̂|² ~ k⁻⁸ (part B) or the exact Galerkin matrix in x-space (part C), never the truncated sum for a generic F.

## 2. The algebra: circle 𝕋_{4T}, two spin structures, ℓ² model, aliasing identity

**Theorem 2.1 (D_T as a truncated Toeplitz operator on the circle; PROVED).** Let 𝕋_{4T} := ℝ/4Tℤ, and s(D_{𝕋_{4T}}) the Fourier multiplier
on L²(𝕋_{4T}) with eigenvalue s_T(ω_k) at e^{iω_k t} (ω_k = 2πk/4T). For F ∈ L²(I_T) ⊂ L²(𝕋_{4T}) (I_T = half-circle):
𝔞_T(F) = ⟨F, s(D_{𝕋_{4T}})F⟩. That is, 𝔞_T = P_{I_T} s(D_{𝕋_{4T}}) P_{I_T}: **the compression to half the circle of a diagonal operator whose
eigenvalues are the Nyquist samples of the symbol.** *Proof.* The Fourier coefficients of F on 𝕋_{4T} are F̂(ω_k)/√(4T); Theorem 1.2. ∎
*Reading.* On the full circle the operator has spectrum {s_k}, which changes sign (§3.3): D_T is exactly the statement that the
compression to the half-circle (plus the two Tate conditions) is ≥ 0 even though the operator on the circle is not. It is the "in u" version of the
Kreĭn extension problem (R186_051 Lemma 1.5) and the continuous version of "a principal block of an indefinite circulant can be ≥ 0".

**Theorem 2.2 (two spin structures; PROVED).** Let D_θ (θ ∈ ℝ/2πℤ) be the self-adjoint extensions of −i d/dt on L²(I_T) with domain
{F ∈ H¹(I_T): F(T) = e^{iθ}F(−T)}; spectrum {(k + θ/2π)π/T}. For F ∈ L²(I_T) and 0 < u < 2T:
 ⟨F, cos(uD_θ)F⟩ = Re c_F(u) + Re[e^{iθ} c_F(u − 2T)],
and therefore, with s = s_T (Def. 1.1) in the functional calculus,
 ⟨F, s(D_θ)F⟩ = 𝔞_T(F) − cos θ·Δ_F − sin θ·Δ′_F, Δ_F := ∫₀^{2T}K(2T − v)Re c_F(v)dv + Σ_{n∈𝒩_T} v_n Re c_F(2T − log n),
(Δ′_F the term with Im c_F; = 0 for F real). In particular **𝔞_T = ½[s(D_0) + s(D_π)]** and 𝔞_T = (1/2π)∫₀^{2π} s(D_θ)dθ.
*Proof.* e^{iuD_θ} is the translation t ↦ t − u on I_T with the phase jump e^{iθ} on crossing the boundary: (e^{iuD_θ}F)(t) = F(t − u) if t − u > −T, and
e^{iθ}F(t − u + 2T) otherwise. Hence ⟨F, e^{iuD_θ}F⟩ = c_F(u) + e^{iθ}∫_{−T}^{−T+u}F(t)F̄(t − u + 2T)dt = c_F(u) + e^{iθ}c_F(u − 2T) (a single wrap
since u < 2T). Applied to μ_T: the δ₀ term does not wrap, the Lévy term gives ∫₀^{2T}K(u)[‖F‖² − Re c_F(u) − Re e^{iθ}c_F(u − 2T)]du and
u ↦ 2T − v converts −∫K(u)Re e^{iθ}c_F(u − 2T)du into −Re e^{iθ}∫₀^{2T}K(2T − v)c_F(−v)dv; the comb likewise. The renormalization at u = 0
is that of R186_117 (μ_ε). Averaging over θ ∈ {0, π} or over all θ: the wrapped term cancels. ∎
*Reading.* s(D_0) is diagonal in {e^{ikπt/T}} (coarse grid, even k of the fine one) and s(D_π) in {e^{i(k+½)πt/T}} (odd k): the form is the average
of two diagonal operators in two "mutually biased" orthonormal bases (|⟨e_j, e′_l⟩| = 2/(π|2(l−j)+1|)). This is the operator-level
content of "length × step = π": the Nyquist grid of the symbol is the union of the spectra of the two spin extensions.

**Theorem 2.3 (ℓ² model; PROVED).** In the orthonormal basis e_j = e^{ijπt/T}/√(2T) of L²(I_T), the matrix of 𝔞_T is
 M_{jj′} = ½[ s_T(ω_{2j}) δ_{jj′} + Σ_{l∈ℤ} s_T(ω_{2l+1}) h_{l−j} h_{l−j′} ], h_m := sinc(m + ½) = 2(−1)^m/(π(2m+1)),
that is M = ½(D_e + HᵀD_oH) with D_e = diag s_T(ω_{2j}), D_o = diag s_T(ω_{2l+1}) and H the unitary Toeplitz matrix (h_{l−j}) (Shannon
half-shift in PW_T). The two Tate terms are Σ_j c_j (−1)^j/(½ ∓ ijπ/T) = 0. For the full form, w instead of s.
*Proof.* F̂(ω_{2l+1}) = Σ_j F̂(ω_{2j}) sinc(l + ½ − j) (Shannon in PW_T, step π/T), F̂(ω_{2j}) = √(2T)·c_j, Theorem 1.2. H unitary: Shannon
energy identity for the two shifts of the grid. ∎ Verified: |M_Fourier − ½(D_e + HᵀD_oH)|_max = 3.5·10⁻⁶ (L = 4·10⁵, tail log L/L) and
same λ_min over 𝒫_T to 4 digits (§8 C). Galerkin in this basis converges from above to λ_A: 9.56·10⁻⁴ / 1.09·10⁻⁷ / 4.16·10⁻¹² (J = 40)
vs 9.49·10⁻⁴ / 1.04·10⁻⁷ / 3.84·10⁻¹² (Legendre, r043/r117).
*Algebra.* H = multiplication by e^{iπt/2T} on L²(I_T); H² = e^{iπt/T} commutes with the diagonals, shifting them by 1. The algebra generated
by {diag, H} is M₂(C*(ℤ ⋉ ℓ^∞)) (rational rotation ½); in it 𝔞_T is ½(D_e + H*D_oH), and the product of two such is not of the same form
(truncated Toeplitz operators do not form an algebra, Sarason 2007; see 2.5). "The algebra of D_T" is therefore a **space** of
operators (compressions to PW_T), not a closed subalgebra; what is exact and explicit is the decomposition ½(D_e + H*D_oH).

**Theorem 2.4 (aliasing identity; PROVED).** For F ∈ L²(I_T) real, with c_k the Fourier coefficients of F in I_T and c′_k those of
e^{iπt/2T}F: 𝔞_T(F) = Σ_k s_T(kπ/T)|c_k|² + Δ_F = Σ_k s_T((k+½)π/T)|c′_k|² − Δ_F, Δ_F as in 2.2. Hence Δ_F = ½[s(D_π) − s(D_0)](F).
Δ_F is the pairing of c_F with the **reflection u ↦ 2T − u** of the positive part K du + Σ v_n δ_{log n} of μ_T: it weights each contact
by c_F(2T − log n), i.e. by its closeness to the edge of the window (the newest contact, log n ≈ 2T, weighs ≈ ‖F‖²; n = 2 weighs
c_F(2T − log 2) ≈ 0 for large T). For M₁ one must add the wrapped part of the quartet: Δ^{M₁}_F = Δ_F − 8∫₀^{2T}Re c_F(v)cos(γ₁(2T−v))cosh(δ(2T−v))dv.
Verified to 10⁻¹⁵ (§8 B) and on the witness of M₁ (§8 E).

**2.5 Identification (CITED).** By Paley–Wiener, PW_T = K_Θ with Θ = e^{2iTz}, the model space of the half-plane; the form (1/2π)∫s_T|F̂|² is the
quadratic form of the truncated Toeplitz operator A_{s_T} = P_{K_Θ} s_T P_{K_Θ} (Sarason, *Algebraic properties of truncated Toeplitz
operators*, 2007). The symbol of a TTO is unique modulo ΘH² + conj(ΘH²), which in u is "Fourier support in |u| ≥ 2T": **the family of
certificates {f_w : w ∈ 𝒲} of Paper 47 def:W is exactly Sarason's symbol class for the operator A_T**, and thm:Z says that class
contains Σ_ρ ŵ(τ − γ_ρ). On the grid, the symbol class collapses to the sequence (s_k) modulo the annihilator (2.6). On whether a TTO ≥ 0
has a symbol ≥ 0: the answer is Kreĭn's extension theorem (yes, as a measure: Theorem 3.3), not a new algebraic property.

**2.6 The annihilator (PROVED).** Σ_k (−1)^k |F̂(ω_k)|² = 4T Re c_F(2T) = 0 for every F ∈ L²(I_T). Hence (s_k) is determined by the form only
modulo c·(−1)^k: the alternating sequence is the transform of ½(δ_{2T} + δ_{−2T}) (boundary atoms = the ambiguity of the sharp cutoff).
Consequence: in every criterion "s_k ≥ 0" one must quotient by (−1)^k (§3.3); in the discrete thm:Z the numerical discrepancy is exactly
c(−1)^k (§3.4). For large T the alternating component dominates s_k (T = 5: s_0 = −593, s_1 = +425, …; w_k = ±0.256 after the merge of 1.3):
it is the mass of the comb near the edge (θ_n → 1 ⟹ cos πkθ_n ≈ (−1)^k) against the pole, and carries no information.

## 3. The two cones

**Theorem 3.1 (the primal cone; PROVED with Akhiezer CITED).** 𝒦_T := {(|F̂(ω_k)|²)_k : F ∈ 𝒫_T} = {(f(ω_k))_k : f entire of exponential
type ≤ 2T, f ≥ 0 on ℝ, f ∈ L¹(ℝ), f with a zero of order ≥ 2 at z = ±i/2}.
*Proof.* (⊂) f = |F̂|² is of type 2T, L¹, ≥ 0 and f(z) = F̂(z)·conj F̂(z̄); F̂(±i/2) = 0 (A(F) = F̂(−i/2), B(F) = F̂(i/2)) gives zeros of order ≥ 2 at ±i/2.
(⊃) Akhiezer (1948; Boas, *Entire functions*, 7.5.1; CITED): f ≥ 0 of type 2T with ∫log⁺f/(1+τ²) < ∞ (automatic in L¹) is f = |G|² with G
entire of type T; G ∈ L² ⟹ G = F̂, F ∈ L²(I_T) (Paley–Wiener). The zeros of f are those of G together with the conjugates; the Blaschke factor
(z + i/2)/(z − i/2) (unimodular on ℝ, type 0) moves a zero from −i/2 to i/2 without changing |G| on ℝ, so from a double zero of f at i/2 (and at
−i/2) one obtains G with G(i/2) = G(−i/2) = 0. ∎
**Cor. 3.2 (Tate = weight; PROVED).** 𝒦_T = {((ω_k² + ¼)² b_k)_k : b = samples of f₀ ≥ 0 ∈ PW_{2T} with (1 + τ²)²f₀ ∈ L¹} (G = (z² + ¼)G₀; in t:
F = (¼ − ∂²)F₀, F₀ ∈ H²₀(I_T), which is the parametrization of R186_051 Def. 1.6 / Paper 47). Hence D_T ⟺ ((ω_k² + ¼)² s_k)_k ∈ 𝒦_T^{(0)*},
𝒦_T^{(0)} := samples of {f ≥ 0 ∈ PW_{2T} ∩ L¹} (Tate-free cone, with the corresponding weight).
**Theorem 3.3 (window Bochner; PROVED modulo Riesz extension, CITED).** For σ = (σ_k) of logarithmic growth (paired
with the f's of the form domain): σ ∈ 𝒦_T^{(0)*} ⟺ ∃ a positive measure μ on ℝ (with ∫log(2+|τ|)dμ(τ)/(1+τ²)-type growth) such that
σ_k = (B_T μ)(ω_k) ∀k, (B_T μ)(τ) := ∫ (2T/π) sinc(2T(τ − τ′)/π) dμ(τ′) (band-limited projection / Dirichlet smoothing).
*Proof.* (⇐) Σ_k f(ω_k)(B_Tμ)(ω_k) = ∫f dμ ≥ 0 by Shannon in PW_{2T}. (⇒) the functional f ↦ Σσ_k f(ω_k) is positive on the cone {f ≥ 0}
of PW_{2T} ∩ L¹ (with weight), which contains a strictly positive element (sinc² + sinc²(· − ½)); M. Riesz extension to a positive
functional over C₀ with weight = positive measure μ; Shannon back gives σ_k = (B_Tμ)(ω_k). In u: B_T cuts μ̂ to (−2T, 2T): this is Kreĭn (1940). ∎
**Theorem 3.4 (discrete thm:Z; PROVED as a reformulation).** D_T ⟺ (s_k)_k ∈ 𝒦_T^* ⟺ ∃ μ ≥ 0, β ∈ ℝ²: s_k + β₀ĝ₀(ω_k) + β₁ĝ₁(ω_k) = (B_Tμ)(ω_k) ∀k
(modulo closure of the cone, as in Paper 47 prop:weak/prop:P). If (ν, β) is a certificate of Paper 47 def:PD with f = s_T + ν̂ + β·ĝ ≥ 0, then
μ = f dτ works: (B_T f)(ω_k) = s_k + β·ĝ(ω_k) because B_T ν̂ = 0 (supp ν ⊂ {|u| ≥ 2T}, no atoms at ±2T) and B_T σ_T = s_T (Def. 1.1). And for every
w ∈ 𝒲: w_k = (B_T f_w)(ω_k) = Σ_ρ (B_Tŵ)(ω_k − γ_ρ) = **4T Σ_ρ sinc(2T(ω_k − γ_ρ)/π)** (CONDITIONAL in the explicit formula for the sharp
cutoff 1_{[−2T,2T]}cos(τu) with symmetric summation, classical; if e^{2T} = n ∈ ℕ is a prime power, add ½v_n(−1)^k for the ½ convention at the
jump, an annihilator term). NUMERICAL (§8 D): with 150 zeros + smooth tail, w_k − 4TΣsinc = c_T(−1)^k with c_T = 0.0075, 0.0052, 0.0128,
0.0217 (T = 0.6, log 2, 1, 1.7) **constant in k to 4 digits**: the discrepancy is entirely the fluctuation of the zeros not included
(Σ_{γ>Γ} sin(2Tγ)/γ-type), which lives in the annihilator. The identity modulo (−1)^k is confirmed to ≤ 10⁻⁴.
*Reading.* The samples w_k are **intrinsic** (the same for every certificate f_w) and are the zero measure smoothed by the Dirichlet
kernel of the window and sampled at its own Nyquist rate. D_T says that sequence is also the B_T-smoothing of SOME
positive measure (without assuming anything about the γ_ρ); nothing in this memo uses the reality of the zeros.
**Cor. 3.5 (primitive form).** D_T ⟺ ∃ μ ≥ 0: (ω_k² + ¼)² s_T(ω_k) = (B_Tμ)(ω_k) ∀k.

**3.3 The circulant cone fails (NUMERICAL, §8 A).** Sufficient condition S1: w_k ≥ 0 ∀k ⟹ W_T ≥ 0 ⟹ D_T. And S1(β): ∃β: s_k + β·ĝ(ω_k) ≥ 0 ∀k.
Results (k ≤ 4000): w_k < 0 at k = {1, 3} (½log3; w_1 = −0.631, w_3 = −0.643), {1, 3, 5, 8, 20} (log 2), {1, 3, 5, 9, 14, 23} (½log5),
14 points (½log7), 25 (T = 1), 166 (1.5), 426 (2), 1017 (3), 1545 (5). max_β min_k[s_k + β·ĝ] = −0.247, −0.571, −1.417, −1.903, −1.319,
−3.589, −6.90, −9.67, −11.17. Modulo the annihilator (quotient by (−1)^k: ½(min_even + min_odd)) it remains < 0 in every case (½log3: min_even w = 0.245
at k = 6, min_odd = −0.643). **No grid certificate without a measure works**: positivity requires a μ whose B_T-smoothing is negative at
k = 1, 3, 5, … (negative sinc lobes between resolved zeros for large T; for small T, the archimedean well m < 0 for |τ| ≲ 6.3,
which contains ≈ 4T grid points of both parities). What fails is not a property of the symbol but the compression (Theorem 2.1).

## 4. Multiplicative and quasi-periodic structure (PROVED, elementary; no sign)

**4.1 Irrational nodes.** s_T(ω_k) = m(ω_k) + r_T(ω_k) − Re Σ_{n<N} v_n n^{−iπk/log N}: the comb on the grid is the "DFT with nodes
θ_n = log n/log N ∈ (0, 1)": p_k = Σ v_n cos(πkθ_n). The shift U: k ↦ k + 1 multiplies the term n by e^{iπθ_n} = n^{iπ/log N}
(half a turn over the length of the polynomial: phase 0 at n = 1, π at n = N); in the comb sampled on the coarse grid (even k) it is
Σ v_n cos(2πkθ_n) and on the fine odd one Re Σ v_n n^{iπ/log N} e^{2πikθ_n}: the rotation n ↦ n^{iπ/log N} is the "twist" of the antiperiodic structure.
**4.2 Types.** (i) p_k = ∫cos(πkθ)dν_T, ν_T = Σ v_n δ_{θ_n} ≥ 0 on (0, 1): p is of **positive type** on ℤ (Herglotz) with atomic spectral
measure ½(ν_T + ν̃_T) on ℝ/2ℤ; Toeplitz_n[p_{k−l}] ≥ 0 exactly (λ_min = −10⁻¹³ numerical, n = 80). (ii) L_k := L_T(ω_k) =
∫₀^{1}(1 − cos πkθ)dκ_T(θ), κ_T := 2TK(2Tθ)dθ ~ dθ/θ at 0 (Lévy measure on the circle, ∫θ²dκ_T < ∞, infinite mass): L is
**of conditionally negative type** (Lévy–Khintchine on ℤ): Σx_k x̄_l L_{k−l} ≥ 0 if Σx_k = 0; hence Toeplitz_n[−L_{k−l}] is ≥ 0 on the
hyperplane Σx = 0 and has ≤ 1 negative eigenvalue (numerical n = 80: 79 positive, λ_max = +63, one negative; Schoenberg).
(iii) s_k = c_T + ∫(1 − cos πkθ) d(κ_T + ν_T)(θ): **Lévy–Khintchine exponent on ℤ of the POSITIVE measure κ_T + ν_T, plus the constant
c_T = C₀ + ∫_{2T}^∞K − 𝒜_T < 0**. Hence D_T ⟺ for every a ∈ 𝒦_T: Σ_k a_k ψ_T(k) ≥ −c_T Σ_k a_k, ψ_T(k) := ∫(1 − cos πkθ)d(κ_T + ν_T) ≥ 0,
i.e. 4T∫(c_F(0) − Re c_F(2Tθ))d(κ_T + ν_T)(θ) ≥ 4T(𝒜_T − C₀ − ∫_{2T}^∞K)‖F‖²: the "Lévy energy" of the test against primes + archimedean
must exceed a fixed multiple of its mass. This is Paper 47 thm:A/eq:Aform on the circle: **it adds no information**, but it shows that the writing
"measure of m minus measure of primes" is incorrect as far as signs go: in Lévy form both measures are positive and the negative
sign lies entirely in the constant c_T (the mass 𝒜_T of the comb, PNT in the window: 𝒜_T ≈ 2(e^T − 1) against 2∫cosh = 4 sinh T of the pole).
**4.3 Hardy.** S_T(ω) := Σ v_n n^{iω} is the transform of a measure supported on (0, 2T) ⊂ (0, ∞): on the grid, (S_T(ω_k))_k has its entire
spectrum (on the dual circle) in (0, π), it is an "analytic" sequence, and the sine comb Σ v_n sin(ω_k log n) is the discrete Hilbert
transform of the cosine comb. The same holds for the Lévy part. This is the discrete version of "μ_T^+ lives on (0, 2T)" and does not enter D_T,
which only sees the even part (Re c_F).
**4.4 Almost periodicity.** p_k is Bohr-almost-periodic with frequencies {πθ_n}; s_k = (log k + O(1)) + almost periodic. Bochner–Herglotz on ℤ
characterizes the circulant cone {Toeplitz ≥ 0} = {spectral measure ≥ 0 on the full circle}, which is exactly the positivity on 𝕋_{4T}
of §2.1 (false, §3.3). Positivity against 𝒦_T (half-circle) is not a Bochner-type statement but a Kreĭn-type one (Theorem 3.3). There is no
theorem on almost periodic functions that could replace Kreĭn; the almost periodicity of p_k with irrational frequencies {θ_n} only says that
Toeplitz[p] is a sum of rank-2 projectors (one per contact), which we already knew (R186_035 cone, Paper 47 eq:Kprim).

## 5. Decisive test with M₁ (NUMERICAL + PROVED where indicated)

M₁ = ξ·(quartet ½ ± δ ± iγ₁), γ₁ = 14.1347; the form gains ∫_{−2T}^{2T}c_F·4cos(γ₁u)cosh(δu)du (R186_114 §1.1, Lemma Q), the symbol gains
Q(τ) = 8∫₀^{2T}cosh(δu)cos(γ₁u)cos(τu)du (closed form in the script). On the grid (log 2): Q(ω_k) = 0.38, −0.39, 0.43, −0.50, 0.65, −1.07, **5.14** (k = 6, ω = 13.6 ≈ γ₁).
**5.1 (NO-GO).** The Toeplitz positivity of the comb (4.2 i) is identical for ζ and M₁ (same primes); Toeplitz[Q] is indefinite (λ = ±10.9 at
log 2, ±8.7 at ½log3), as is Toeplitz[−L] (4.2 ii): the quartet breaks no positive-/negative-type property of the sampled
sequence; #{s_k < 0} does not change (6 → 6 at log 2, 3 → 3 at ½log3). **The property that M₁ breaks is the positivity of the compression
(Theorem 2.1), i.e. D_T; there is no structural property of (s_k) on ℤ that detects it**, by the same argument as R186_051 Prop. 2.2:
Q is O((2δT)²) in uniform norm relative to the triple zero on the line M₁(0), which is positive.
**5.2 Where the sign lives in the algebra (NUMERICAL, §8 E; Fourier Galerkin J = 24, log 2).**

| model | λ_J | s(D_per)(h) | s(D_anti)(h) | energy at odd k with s_k<0 (±1, ±3, ±5) | at even k with s_k<0 | dominant mode |
|---|---|---|---|---|---|---|
| ζ | +1.31·10⁻⁷ | +0.4292 | −0.4292 | 0.994 | 0.003 | k = ±3 (0.40 each), s_3 = −0.413 |
| M₁ δ = 0.01 | −1.64·10⁻⁶ | +0.9946 | −0.9946 | 0.994 | 0.003 | k = ±3 (0.40), s_3^{M₁} = −0.912 |
| M₁ δ = 0.1 | −1.39·10⁻³ | +0.9021 | −0.9049 | 0.802 | 0.195 | k = ±5 (0.36), s_5^{M₁} = −1.764 |

(λ_A^{M₁} reproduces R186_044/051: −1.66·10⁻⁶ at δ = 0.01.) The extremal vector is almost purely **antiperiodic**: h ≈ a combination of
cos(3πt/2T), cos(5πt/2T), cos(πt/2T) (all vanishing at ±T: this explains h*(±T) ≈ 0 of R186_117), with s(D_anti)(h) = −0.43 balanced to 10⁻⁷ by
s(D_per)(h) = +0.43 (the same h viewed in the periodic basis, where it falls on modes with s_{2j} > 0). λ_A is the average of two numbers of
opposite sign and modulus ~0.4–1 that cancel to 10⁻⁷; M₁ lowers s_3 from −0.41 to −0.91 and shifts the balance by 10⁻⁶. What separates ζ from M₁
is not the structure of s_k (both have the same sign pattern) but the exact value of the coupling HᵀD_oH between sectors.
**5.3 Falsifier for reading 5.2.** If in some window T > ½log5 the extremal vector of ζ had < 50% of its energy in the antiperiodic
sector, the reading "the sign is the even/odd balance" would be false; at T = 1, 1.5 the archimedean well has negative points of both
parities (§3.3) and the reading must be re-examined (not done here: OPEN).

## 6. Two new lemmas with no sign (PROVED)

**Lemma 6.1 (localization of the witness on the grid).** If F ∈ 𝒫_T and 𝔞_T(F) < 0, then for every η > 0, with N_η := {k : s_k < η} and
A_η := max_k (−s_k)₊: (1/4T)Σ_{k∈N_η}|F̂(ω_k)|² > η‖F‖²/(η + A_η). *Proof.* Theorem 1.2: Σ_{k∉N_η}s_k|F̂(ω_k)|² ≥ η(4T‖F‖² − Σ_{N_η}|F̂|²) and
Σ_{N_η}s_k|F̂|² ≥ −A_ηΣ_{N_η}|F̂|². ∎ With η = 0.3 at log 2: N_η = {0, ±1, ±3, ±5, ±8, ±20} (11 points), A = 5.6, fraction > 5%. Even/odd
version (Theorem 2.4): a real witness satisfies ‖P_{N_e}F‖²(A_e + s₊^e) > s₊^e‖F‖² + Δ_F and ‖P_{N_o}F′‖²(A_o + s₊^o) > s₊^o‖F‖² − Δ_F
(F′ = e^{iπt/2T}F; N_e, N_o the negative points of each parity; s₊ the minimum positive value outside them). In M₁'s witness: Δ_F = −0.99 < 0,
so the second is the active one: ‖P_{N_o}F′‖² > 0.99/(A_o + s₊^o) — consistent with the measured 99%.
**Lemma 6.2 (aliasing sandwich).** D_T ⟺ −s(D_0) ≤ Δ ≤ s(D_π) as forms on 𝒫_T (Δ the quadratic form F ↦ Δ_F). In particular, if
σ_e := min_k s_T(kπ/T), σ_o := min_k s_T((k+½)π/T): 𝔞_T(F) ≥ max(σ_e‖F‖² + Δ_F, σ_o‖F‖² − Δ_F) and a witness needs Δ_F ∈ (σ_o‖F‖², −σ_e‖F‖²).
(Trivial from 2.4; useful only if Δ_F can be bounded independently — not achieved: |Δ_F^{comb}| ≤ 𝒜_T‖F‖² is useless, and Δ_F^{Lévy} has
the singular weight K(2T − v) at the edge where c_F → 0.)

## 7. Honesty, falsifiers, what was NOT obtained

- Nothing in §2–§4 changes a cell: these are exact reformulations (Shannon/Poisson + spin extensions + Akhiezer + Kreĭn). What is new
 as a statement: Theorems 2.1–2.4 (two spin structures, ℓ² model ½(D_e + HᵀD_oH), aliasing identity Δ_F), 3.1–3.3 (primal cone
 via Akhiezer with Tate = double zeros / weight (τ² + ¼)²; dual cone = sinc-smoothing of positive measures), Lemma 1.3 (pole + tail merge),
 2.6 (annihilator), discrete thm:Z with its verification modulo (−1)^k. Prior grep: "spin|antiperiodic|half-shift|medio paso|Akhiezer|
 truncated Toeplitz|Sarason" do not appear in phase-186 nor in Paper 47 (Akhiezer appears in Paper 47 only as Kreĭn–Akhiezer of the moment problem).
- **Falsifiers.** (F1) If for some F ∈ L²(I_T) with |F̂|² ~ k⁻⁸ the sum (1/4T)Σ s_k|F̂(ω_k)|² differed from 𝔞_T(F) by more than the tail,
 Theorem 1.2 would be false: 6 tests to 10⁻¹⁵ (§8 B). (F2) If |M_Fourier − ½(D_e + HᵀD_oH)| did not decay as log L/L, 2.3 would be false: 3.5·10⁻⁶
 at L = 4·10⁵. (F3) If w_k − 4TΣsinc were not c(−1)^k to tail precision, 3.4 would be false: it holds to 4 digits in 4 windows. (F4) If S1(β)
 gave ≥ 0 at some T where D_T is unknown, there would be a trivial certificate: does not occur (−0.25 … −11). (F5) 5.3.
- **What was not obtained:** no lower bound on λ_A; no property of (s_k) separating ζ from M₁; no independent control of Δ_F.
 The "Toeplitz positivity of the comb" is exact and empty for D_T (it lives in the circulant cone). The reformulation of D_T as
 cosine moments of μ_T in 𝒦_T^* is exactly Kreĭn/thm:Z; its only added value is that the family of certificates reduces to ONE
 positive measure μ with a sampling condition (Theorem 3.4), and that the samples are intrinsic.
- **Contact with the sign: none.** Row D: OPEN.

## 8. Self-checks (NUMERICAL; `r052_nyquist.py`)

A. s_k, w_k in 9 windows (k ≤ 4000): pole + tail merge (Lemma 1.3) to ≤ 7·10⁻¹⁵; sign patterns and S1(β) by LP on a 241² grid of β ∈ [−30, 30]².
B. 6 tests F = (T² − t²)²·(random polynomial) at T = ½log3, log 2, 1.5 (K = 1500, |F̂|² ~ k⁻⁸, F̂ via Gauss–Legendre, 8000 nodes): Nyquist(s_T)
 vs 𝔞_T in x-space: error ≤ 2.5·10⁻¹²; ‖F‖² ≤ 5·10⁻¹³; aliasing of m (grid vs ∫c_F K^per with K^per(v) + K^per(−v)) identical to 4 digits
 (4.49·10⁻⁴ … 3.06·10⁻¹); s(D_per) ≠ s(D_anti) (e.g. −14.57 vs +2.89, T = 1.5) with ½(sum) = 𝔞_T and even + Δ = odd − Δ = 𝔞_T to 10⁻¹⁵.
 (A first attempt with 6000 nodes and K = 2·10⁴ gave errors of 10⁻²: quadrature aliasing for k > 6000, corrected; noted here for the record.)
C. Fourier matrix M_{jj′} = 𝔞_T(e_j, e_j′) exact in x-space (composite GL, 3000 nodes; |Im M| ≤ 3·10⁻¹⁵), exact Tate: λ_J(J = 12/24/40)
 = 1.116/0.979/0.956·10⁻³ (½log3), 1.76/1.31/1.09·10⁻⁷ (log 2), 9.3/4.45/4.16·10⁻¹² (½log5), decreasing toward λ_A of r043/r117;
 |M − ½(D_e + HᵀD_oH)|_max = 3.5·10⁻⁶ (L = 4·10⁵) and λ_J identical to 4 digits with the Nyquist matrix.
D. Discrete thm:Z: 150 zeros (zeros150.npy) + tail ∫_Γ^∞(log(t/2π)/π)sin(2Tt)[1/(t−ω)+1/(t+ω)]dt (QAWF): diff = c(−1)^k with c constant to 4 digits
 (0.0075, 0.0052, 0.0128, 0.0217); at log 2 the contact n = 4 at the edge requires +½v_4(−1)^k (½ convention): without it, diff = 0.688(−1)^k.
E. M₁: Q on the grid; Toeplitz₈₀ of p (λ_min −10⁻¹³), −L (79 eigenvalues > 0, 1 < 0), Q (±10.9/±8.7); Fourier Galerkin of M₁ (log 2): −1.39·10⁻³ (δ = 0.1),
 −1.64·10⁻⁶ (δ = 0.01), same with the Nyquist matrix; even + Δ^{M₁} = λ_J to 10⁻¹⁰ after including the wrapped part of the quartet (without it: +0.54, error
 detected and corrected); even/odd energies of table 5.2 (H with L = 3000).

## 9. Labels

| statement | label |
|---|---|
| Theorem 1.2 (Nyquist with μ_T / s_T), aliasing of m, Lemma 1.3 | PROVED (R186_117 + elementary) |
| Theorem 2.1 (compression of 𝕋_{4T}), 2.2 (two spin structures), 2.3 (ℓ² model), 2.4 (aliasing Δ_F), 2.6 (annihilator) | PROVED; verified to 10⁻¹⁵ / 3·10⁻⁶ |
| 2.5 (Sarason's TTO; certificates of Paper 47 = symbol class) | CITED (identification) |
| Theorem 3.1, Cor. 3.2 (primal cone; Tate = double zeros / weight (τ²+¼)²) | PROVED (Akhiezer CITED) |
| Theorem 3.3 (window Bochner), 3.4 (discrete thm:Z), Cor. 3.5 | PROVED as a reformulation (Riesz/Kreĭn CITED); zero formula CONDITIONAL (symmetric summation), NUMERICAL modulo (−1)^k |
| §3.3 circulant cone fails in every window, even with β and modulo (−1)^k | NUMERICAL |
| §4 positive type / conditionally negative type / Hardy / Lévy–Khintchine on ℤ | PROVED, no sign |
| §5.1 Toeplitz positivity of the comb is not the property broken by M₁ | NO-GO (PROVED: same primes) |
| §5.2 the extremal lives in the antiperiodic sector (k = ±1, ±3, ±5) | NUMERICAL (log 2); OPEN for T > ½log5 |
| Lemmas 6.1, 6.2 | PROVED, no sign |
| Row D | OPEN; contact with the sign: none |
