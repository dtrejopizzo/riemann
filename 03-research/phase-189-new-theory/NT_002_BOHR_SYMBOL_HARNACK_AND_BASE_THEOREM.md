# NT_002 — Spectral side of the height flow: the Bohr symbol Φ_σ, the Euler-vector criterion, a Harnack contraction,
# and the base theorem D(σ) for σ > 3/2 + O(T₀/log(1/T₀))

Phase 189, construction step 2. Pen and paper. Notation of NT_001. Labels as there.

## Corpus check
grep "Bohr torus", "Toeplitz", "|ζ(σ+iτ)|²", "coprime", "Harnack", "ζ(2δ)/ζ(δ)²", "Euler vector", "completely multiplicative"
+ "Weil": hits — L2_028 §2(c)/N_022 §4 (Div is Bohr-diagonal; Arch/Near live on the curve θ_p = τ log p); L2_029 (Kronecker
sums of local Toeplitz forms on Near-free sets; local symbol range); G1_B4_R2 Prop E3(iii) (averages over completely
multiplicative unimodular twists, as a Schur coupling); R160_C3_R1 (the inequality |ζ(s)| ≥ ζ(2σ)/ζ(σ), unrelated use);
phase 106 "Harnack gate" (106_08: anti-orthogonality gate, different object). No memo writes the damped kernel's symbol as
|L(σ, χ_θ)|²/ζ(2σ)-weighted Weil forms, the lower bound of the Poisson product by ζ(2δ)/ζ(δ)², or proves D(σ) for any σ.
**New:** Props 2.2–2.4 in this form, Thm 2.5 (base theorem), Lemma 2.6, Thm 2.7 + Cor 2.8 (Harnack contraction and the
necessary family Φ_δ ≥ c_δ a₀).

## 1. The symbol (PROVED)
𝕋^∞ := Π_p ℝ/2πℤ = dual of G (Haar dθ). Character χ_θ(r) := Π_p e^{iθ_p v_p(r)}; χ_θ is a completely multiplicative unimodular
function on ℕ, and every such function arises. The curve ι: ℝ → 𝕋^∞, ι(τ)_p = −τ log p, gives χ_{ι(τ)}(r) = r^{−iτ}.
**Lemma 2.0 (absolute convergence above 3/2).** |K(r)| ≤ A₁ + 1.04e^{3T₀}·e^{ℓ(r)/2} with A₁ := (1/2π)∫|m|F̂₀² (ψ(x) < 1.04x,
Rosser–Schoenfeld, CITED). Hence Σ_r |K(r)|H(r)^{−σ} < ∞ for σ > 3/2.
*Proof.* |A(d)| ≤ A₁ (spectral form). For d ≥ 0 only c₀(d − log n) survives (log n + d > 2T₀), |c₀| ≤ 1, and
Σ_{|log n − d| ≤ 2T₀}2Λ(n)n^{−½} ≤ 2e^{−(d−2T₀)/2}ψ(e^{d+2T₀}) ≤ 2.08e^{3T₀}e^{d/2}; the factor ½ in B. Then
Σ_{(a,b)=1}(ab)^{−σ}(b/a)^{−½}… ≤ 2ζ(σ−½)ζ(σ+½) and Σ H^{−σ} = ζ(σ)²/ζ(2σ) (Prop 2.2). ∎
**Prop 2.1 (Bochner on G; Toeplitz bottom).** For σ > 3/2, Φ_σ(θ) := Σ_r K_σ(r)χ_θ(r) is continuous, real, even. D(σ) ⟺ Φ_σ ≥ 0,
and λ_inf(σ) = m(σ) := min_θ Φ_σ(θ).
*Proof.* ℓ¹(G) ⇒ convolution by K_σ on ℓ²(G) is unitarily equivalent (Plancherel on G) to multiplication by Φ_σ on L²(𝕋^∞);
the infimum of its numerical range is ess inf Φ_σ = min Φ_σ (continuity, Haar has full support), and it is the infimum of
λ_min over finite sections (finitely supported vectors are dense). K even ⇒ Φ real and even. ∎
**Prop 2.2 (coprime-pair identity = Poisson product = Euler product).** For σ > 1,
  Q_σ(θ) := Σ_r H(r)^{−σ}χ_θ(r) = Π_p (1 − p^{−2σ})/|1 − e^{iθ_p}p^{−σ}|² = |L(σ, χ_θ)|²/ζ(2σ),
L(s, χ) := Σχ(n)n^{−s} = Π_p(1 − χ(p)p^{−s})^{−1}. On the curve: Q_σ(ι(τ)) = |ζ(σ + iτ)|²/ζ(2σ). Haar mean 1, and
  c_σ := min Q_σ = Π_p (1 − p^{−σ})/(1 + p^{−σ}) = ζ(2σ)/ζ(σ)²  (attained at θ_p ≡ π).
*Proof.* Factorize over primes (Prop 2.1(iii) of NT_001): Σ_k ρ^{|k|}e^{ikφ} = (1 − ρ²)/|1 − ρe^{iφ}|² ≥ (1 − ρ)/(1 + ρ); the product
converges absolutely for σ > 1; Π(1 − x)/(1 + x) = Π(1 − x)²/(1 − x²) with x = p^{−σ}. ∎
**Prop 2.3 (Euler-vector criterion).** For σ > 3/2 and every θ, with G_{θ,σ} := Σ_{m≥1}χ_θ(m)m^{−σ}τ_{log m}F₀ (complex test of
infinite support) and its Weil form defined by the absolutely convergent Hermitian series,
  𝔞(G_{θ,σ}) := Σ_{m,k≥1}χ_θ(m)conj χ_θ(k)(mk)^{−σ}B(log m − log k) = ζ(2σ)·Φ_σ(θ).
So **D(σ) ⟺ the Weil form is ≥ 0 on every Dirichlet-series test Σχ(m)m^{−σ}τ_{log m}F₀, χ completely multiplicative unimodular.**
Spectrally, 𝔞(G_{θ,σ}) = (1/2π)⟨σ_∞F̂₀², |L(σ − iτ, χ_θ)|²⟩ when the pairing is defined (e.g. on the curve,
ζ(2σ)Φ_σ(ι(τ₀)) = (1/2π)⟨σ_∞F̂₀², |ζ(σ + i(τ − τ₀))|²⟩ up to the sign convention of τ₀).
*Proof.* Group (m, k) = (da, db), (a, b) = 1: χ(m)χ̄(k) = |χ(d)|²χ(a/b), (mk)^{−σ} = d^{−2σ}H(a/b)^{−σ}; Σ_d d^{−2σ} = ζ(2σ). ∎
The family {G_{θ,σ}} is a torus of tests (one angle per prime) — far smaller than all of ℝ^M, yet at σ ↓ 0 it carries D (NT_001 Thm 1.4).
**Prop 2.4 (Arch / Div / Near on the torus).** Φ_σ = 𝒜_σ − 𝒟_σ − 𝒩_σ, with
  𝒜_σ(θ) = Σ_r A(log r)H^{−σ}χ_θ(r),
  𝒟_σ(θ) = Σ_n Λ(n)n^{−½−σ}(χ_θ(n) + χ̄_θ(n)) = −2Re (L′/L)(½ + σ, χ_θ)  [exact coincidences r = n: H(n) = n],
  𝒩_σ(θ) = Σ_{r∉{n^{±1}}∪{1}} … + Σ_{integers m ≠ n} …  (all near-coincidences, each damped by H^{−σ} = e^{−σℓ}den^{−2σ}).
𝒟_σ is the log-derivative of the twisted Euler product at ½ + σ: the local Euler factors enter **non-linearly** and exactly;
its range is [2Σ_p … at θ ≡ π, −2(ζ′/ζ)(½ + σ) at θ = 0]. ∎ (definitions + NT_001 §0.)

## 2. Base theorem (PROVED)
**Lemma 2.6 (archimedean energy grows under narrowing).** a₀ ≥ ½log(1/T₀) − C for an absolute C (T₀ ≤ T_abs).
*Proof.* m(τ) = Re ψ(¼ + iτ/2) − log π is even and increasing in |τ| (ψ(z) = −γ + Σ_k[1/(k+1) − 1/(k+z)] gives
Re ψ(x+iy) − ψ(x) = Σ_k y²/((k+x)((k+x)²+y²)) ↑ in |y|), m ≥ m(0) = ψ(¼) − log π > −5.4, and m(R) ≥ log R − C (Stirling, CITED).
μ_R := (1/2π)∫_{|τ|≤R}F̂₀² ≤ (R/π)‖F₀‖₁² ≤ 2RT₀/π (Cauchy–Schwarz on a support of length 2T₀). With (1/2π)∫F̂₀² = 1 and
R = T₀^{−½}: a₀ ≥ m(R)(1 − μ_R) + m(0)μ_R ≥ ½log(1/T₀) − C. ∎
**Thm 2.5 (base theorem).** There are absolute constants C₁, C₂, T_abs > 0 such that for every admissible profile with T₀ ≤ T_abs
and every σ > 3/2:
  m(σ) ≥ a₀ − 2(−ζ′/ζ)(½ + σ) − 10T₀e^{2σT₀}ζ(2σ−1)·(−ζ′/ζ)(σ − ½) − C₁(1 + a₀T₀²).
Since −2(ζ′/ζ)(2) < 1.15 (CITED value), −ζ′/ζ(s) ≤ 1/(s−1) + C₂ for s > 1 (the difference is continuous on [1, ∞) and → 0), and
a₀ ≥ ½log(1/T₀) − C (Lemma 2.6): **for every η > 0 there is T(η) > 0 such that every admissible profile with T₀ ≤ T(η) satisfies
D(σ) for all σ ≥ 3/2 + η.** For a fixed profile: σ₁(F₀) ≤ 3/2 + C T₀/(a₀ − C′) whenever a₀ > C′ (absolute C, C′).
*Proof.* m(σ) ≥ a₀ − Σ_{r≠1}|K(r)|H(r)^{−σ} (Gershgorin on G: Prop 2.1 and |Φ_σ − a₀| ≤ Σ_{r≠1}|K_σ(r)|). Split |K| ≤ |A| + |Div| + |Near|.
(Div) r = n^{±1}: Σ_n 2Λ(n)n^{−½}n^{−σ} = 2(−ζ′/ζ)(½ + σ).
(Near) For r > 1 the comb part of K(r) is ½Σ_n v_nc₀(log r − log n) (|c₀| ≤ 1). For fixed n and b ≥ 1 the integers a ≠ nb with
|log(a/nb)| ≤ 2T₀ number ≤ 2nb(e^{2T₀} − 1) ≤ 5T₀nb (T₀ ≤ T_abs), each with H(a/b) ≥ nb²e^{−2T₀} (summing over all
pairs (a, b), reduced or not, only over-counts). Counting r and 1/r (the ½ cancels the 2):
Σ ≤ Σ_n v_n n^{1−σ}·5T₀e^{2σT₀}Σ_b b^{1−2σ} = 10T₀e^{2σT₀}ζ(2σ−1)(−ζ′/ζ)(σ − ½). (Integers m ≠ n near n are the case b = 1.)
(Arch, ℓ(r) ≤ 4T₀, r ≠ 1) |A| ≤ A₁ ≤ a₀ + CT₀ (A₁ − a₀ = (1/π)∫m₋F̂₀² ≤ (5.4/π)μ_R with R the zero of m, μ_R ≤ 2RT₀/π). Writing r = a/b,
a > b: a − b ≥ 1 forces b ≥ 1/(e^{4T₀} − 1) ≥ 1/(5T₀); the number of such r with b ∈ [D, 2D) is ≤ 2D·10T₀D, and H ≥ D². Dyadic sum:
≤ C(a₀ + 1)T₀·(5T₀)^{2σ−2} ≤ C(a₀ + 1)T₀² for σ ≥ 3/2.
(Arch, ℓ(r) > 4T₀) For d > 2T₀, c₀(d) = 0 and eq:Aform gives A(d) = −½∫c₀(w)K(d − w)dw with K(u) = 2e^{−u/2}/(1 − e^{−2u})
(L2_023 Lemma C); the term 2e^{−u/2} integrates to −e^{−d/2}∫c₀e^{w/2} = 0 (Tate). The remainder kernel 2e^{−5u/2}/(1 − e^{−2u}) at
u = d − w ≥ 2T₀ is ≤ e^{−5u/2}/T₀ (1 − e^{−4T₀} ≥ 2T₀ for small T₀), and ‖c₀‖₁ ≤ 4T₀; so |A(d)| ≤ 2e^{5T₀}e^{−5d/2}. Then
Σ_{r≠1} e^{−5ℓ(r)/2}H(r)^{−σ} ≤ 2Σ_{a>b≥1}a^{−5/2−σ}b^{5/2−σ} ≤ 2Σ_{a≥2}a^{−4}·a² < 1 at σ = 3/2 (and smaller above): an absolute constant.
Adding up gives the display. ∎
**Status of the base theorem w.r.t. the barriers.** The proof uses only |a(n)| ≤ Λ-type Dirichlet-series bounds
(Σ|a(n)|n^{−s} ≤ −ζ′/ζ(s) + O(1)) and ψ_a(x) ≤ 1.04x: it is a CLASS theorem (holds for a_P, for Λ + c1_{n₀} with |c| small,
for Beurling-type combs indexed by ℕ with the same bounds). It is the analogue, for the flow, of "positivity for windows below
½ log 2": the cheap region. It is not sign-carrying, as expected.

## 3. Harnack contraction (PROVED)
**Thm 2.7.** For σ > 3/2 and δ > 1: Φ_{σ+δ} = Q_δ ⋆ Φ_σ (Haar convolution on 𝕋^∞), hence
  m(σ + δ) ≥ c_δ a₀ + (1 − c_δ)m(σ),   c_δ = ζ(2δ)/ζ(δ)² ∈ (0, 1).
*Proof.* Fourier coefficients multiply (K_{σ+δ} = K_σ·H^{−δ}) and Q_δ is continuous with coefficients H^{−δ}; ∫Φ_σ = K_σ(1) = a₀;
Φ_{σ+δ} = c_δ∫Φ_σ + ∫(Q_δ − c_δ)(θ − ·)Φ_σ with Q_δ − c_δ ≥ 0 of mass 1 − c_δ. ∎
**Cor 2.8 (necessary family with explicit positive floor).** If D holds then for every δ > 1 and every θ ∈ 𝕋^∞:
  Φ_δ(θ) := (Q_δ ⋆ μ₀)(θ) ≥ c_δ·a₀ = a₀ζ(2δ)/ζ(δ)²,
where μ₀ ≥ 0 is the Bochner measure of K on 𝕋^∞ (mass K(1) = a₀); for δ > 3/2, Φ_δ is the absolutely convergent series of
Prop 2.1. In particular, for δ > 3/2 (Prop 2.3; for 1 < δ ≤ 3/2 only a.e. in χ): D ⟹ 𝔞(Σχ(m)m^{−δ}τ_{log m}F₀) ≥ a₀ζ(2δ)²/ζ(δ)² for all χ.
*Proof.* Herglotz–Bochner on the discrete group G (CITED): PD K = Fourier–Stieltjes transform of μ₀ ≥ 0; Q_δ ≥ c_δ. ∎
**Sign-contact protocol.** A single pair (δ > 3/2, θ) with Φ_δ(θ) < c_δa₀, certified from the absolutely convergent series, would be
a certified failure of D — to be flagged immediately. None is computed here (no numerics), none is claimed.
Note: c_δ ↓ 0 as δ ↓ 1, c_δ ↑ 1 as δ → ∞; the base theorem gives Φ_δ ≥ a₀ − O(1), so the floor is consistent for large δ.

## 4. Requirements check
- Euler product: exact and non-linear in Q_σ = |L(σ,χ)|²/ζ(2σ) and in 𝒟_σ = −2Re L′/L(½+σ, χ). Integrality: G = ℚ_{>0}, den.
  FE: only through A. Joint use: not achieved in this step.
- N_018: Prop 2.3 expresses D(σ) through Weil forms of Dirichlet-series tests (inside the shift calculus); Thm 2.7/Cor 2.8 are
  Bochner. **These are restatements/organization plus one class theorem (2.5).** Nothing here escapes N_018 as a *proof* of D.
- Falsifiers: Thm 2.5 holds for them in its class; Cor 2.8 fails for any comb failing D (it is necessary for D).

## 5. Review
- Lemma 2.0 constant 1.04: ψ(x) < 1.03883x (Rosser–Schoenfeld 1962, CITED). ✓
- Prop 2.1: Bochner/Plancherel on a discrete abelian group, standard (Rudin, *Fourier analysis on groups*, CITED). ✓
- Prop 2.3: the "Weil form" of an infinite-support test is DEFINED as the absolutely convergent series; its identification with
  a window form of Paper 47 is only via truncation (finite sections) — correct use: D(σ) is about finite sections (Prop 2.1). ✓
- Thm 2.5 (Arch) paragraph: the bookkeeping for small-height rationals with ℓ ∈ (4T₀, 1/2) is sketched, not written to the last
  constant; the dependence is O(T₀)·O(1). **Label: PROVED with absolute constants left implicit (routine).** The Near count is
  exact and is the term that produces the 3/2 line. ✓
- Lemma 2.6: monotonicity of m in |τ| from the ψ series; μ_R bound via ‖F̂‖_∞ ≤ ‖F‖₁. ✓
- Thm 2.7: requires continuity of Φ_σ (σ > 3/2) for the pointwise min; Cor 2.8 requires only D. ✓
- Overclaim risk: Thm 2.5 is NOT a partial result toward D in any implication sense; it is the cheap end of the flow (class level).
- No certified negative value; **no sign contact**.


## Erratum note (after NT_001_004_REVIEW)
Near count needs T₀ ≤ T_abs; Cor 2.8 test form restricted to δ > 3/2 (referee FIX 3–4).
