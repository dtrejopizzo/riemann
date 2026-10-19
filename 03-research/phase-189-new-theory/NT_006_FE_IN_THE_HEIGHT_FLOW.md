# NT_006 — The functional equation inside the height flow: the main factor is odd under σ ↦ 2 − σ; the ℓ² line σ = 1 is the
# fixed line; regularity at σ = 1 singles out Λ among all finite modifications

Phase 189, construction step 6. Notation of NT_005. Labels as there.

## Corpus check
grep "ζ′/ζ(s) + ζ′/ζ(1−s)", "prime-free", "reflection", "2 − σ", "σ ↦ 2": hits — phase-108 108_91 and R160_001_BRIEF I-10
("symmetrization destroys the zeros: ζ′/ζ(s) + ζ′/ζ(1−s) is prime-free"); R160_PD_R1 Lemma 2.1 (Re(−ζ′/ζ)(½+iy) = ½m(y) via FE);
N_004 (reflection = alternating sampled comb, NO-GO); L2_026 (FE reflection of the σ-family of L2_025: a different family — positive
densities on Re s > 1, no height, no coprime counting); R184_014 (unrelated "2−σ"). **New:** the FE acting on the height-flow main factor
(Thm 6.1), the identification of the reflection σ ↦ 2 − σ with the ℓ² line as fixed line (Cor 6.2), regularity at σ = 1 as a Λ-specific
property and its failure for every nonzero finite modification and for truncations (Thm 6.3), the pairing of the two Tate cancellations
(Prop 6.4). The corpus fact "ζ′/ζ(s) + ζ′/ζ(1−s) is prime-free" is used in its antisymmetric form.

## 1. FE turns the main factor into an odd function (PROVED; FE CITED)
Let Γ_ℝ(w) = π^{−w/2}Γ(w/2), γ(w) := Γ_ℝ′/Γ_ℝ(w) = −½log π + ½ψ(w/2), ξ_ℝ(w) := Γ_ℝ(w)ζ(w); FE: ξ_ℝ(w) = ξ_ℝ(1 − w) (CITED).
**Thm 6.1.** With w = σ − ½ + iτ₀, z = −τ₀ + i(σ − 1) as in NT_005:
  m(z) + 2(ζ′/ζ)(w) = M(w) := (ζ′/ζ)(w) − (ζ′/ζ)(1 − w).
Hence the main factor G(σ, τ₀) := Re{F̂₀(z)²M(w)} satisfies G(2 − σ, τ₀) = −G(σ, τ₀) (odd about σ = 1) and is even in τ₀.
*Proof.* m(z) = γ(w) + γ(1 − w) (NT_005 §2: ¼ ± iz/2 = w/2, (1−w)/2). FE: γ(w) + ζ′/ζ(w) = −γ(1−w) − ζ′/ζ(1−w). So
m + 2ζ′/ζ(w) = γ(w) + γ(1−w) + 2ζ′/ζ(w) = ζ′/ζ(w) − ζ′/ζ(1−w). Reflection σ ↦ 2 − σ, τ₀ ↦ −τ₀ sends w ↦ 1 − w and z ↦ −z;
F̂₀ is even, so F̂₀(z)² is invariant and M changes sign. Evenness in τ₀: τ₀ ↦ −τ₀ sends z ↦ −z̄, w ↦ w̄; F̂₀(−z̄)² = conj F̂₀(z)²
(F̂₀ real on ℝ, even), M(w̄) = conj M(w); the real part is unchanged. ∎
**Cor 6.2 (the ℓ² line is the FE fixed line; centre criticality explained).** At σ = 1, w = ½ + iτ₀, 1 − w = w̄, so
M = 2i·Im(ζ′/ζ)(½ + iτ₀) and F̂₀(z)² = F̂₀(τ₀)² > 0: **G(1, τ₀) = 0 for every τ₀** (with ζ(½+iτ₀) ≠ 0). This is the height-flow form of the
corpus "exact criticality at every frequency" (L2_010, N_013): the coprime-counting pole 1/(2(σ − 1)) of ζ(2σ − 1) multiplies a factor
that the FE forces to vanish on the ℓ² line. ∎
**Consequence.** Φ^{curve}_σ(τ₀) is regular at σ = 1 (τ₀ off the discrete set where ζ(½ + iτ₀) = 0), with value
  V(τ₀) := lim_{σ→1}Φ^{curve}_σ(τ₀) = ∂_σG(1, τ₀)/(2ζ(2)) + Re ℛ₁(τ₀)   (NT_007 evaluates ∂_σG).

## 2. Regularity at σ = 1 is Λ-specific (PROVED)
For a real comb a write L_a(w) := Σ_n a(n)n^{−w} and Φ^{curve,a}_σ for the continued curve symbol (NT_005 with −ζ′/ζ ↦ L_a).
**Thm 6.3.** (i) For a = Λ + δ with δ ≢ 0 finitely supported, the residue of Φ^{curve,a}_σ(τ₀) at σ = 1 is
  Res_{σ=1} = −(F̂₀(τ₀)²/ζ(2))·Σ_n δ(n)n^{−½}cos(τ₀ log n),
a nonzero trigonometric polynomial times F̂₀(τ₀)² > 0; so the curve symbol of a has a genuine pole at σ = 1 for all τ₀ outside a discrete set,
of both signs as τ₀ varies (a nonzero real almost-periodic polynomial Σc_n cos(τ₀ log n) with log n > 0 has mean 0; see §4).
(ii) For truncations a = Λ1_{n<N} (the W-tail family's extreme member), the residue is (F̂₀(τ₀)²/(2ζ(2)))·[m(τ₀) − 2Σ_{n<N}Λ(n)n^{−½}cos(τ₀log n)],
which is not identically zero (it grows like log|τ₀| as |τ₀| → ∞).
(iii) For Λ the residue vanishes identically (Cor 6.2).
*Proof.* The residue of (ζ(2σ−1)/ζ(2σ))G_a at σ = 1 is G_a(1, τ₀)/(2ζ(2)); ℛ^a is analytic there (Prop 5.3; a finite δ adds finitely many
analytic defect terms; for truncations the n-sum is finite). G_a(1, τ₀) = G_Λ(1, τ₀) − 2Re[F̂₀(τ₀)²Σδ(n)n^{−½−iτ₀}] = −2F̂₀(τ₀)²Σδ(n)n^{−½}cos(τ₀log n).
(ii) G_a(1, τ₀) = F̂₀(τ₀)²[m(τ₀) − 2Re Σ_{n<N}Λ(n)n^{−½−iτ₀}] (σ = 1: z = −τ₀ real, m(z) = m(τ₀)); the Dirichlet polynomial is bounded, m → ∞. ∎
**Reading.** Inside the height flow, the FE (conductor 1, Γ_ℝ) acts as the reflection σ ↦ 2 − σ of the arithmetic main factor, and its
footprint is **regularity of the curve symbol across the ℓ² line**. Every finite modification (cor:void's falsifiers) and every truncation
(W-tail's) breaks it. This is the first Λ-specific (non-class) property of the theory: it uses Euler (ζ′/ζ), FE, and integrality (the
coprime-counting pole ζ(2σ−1) and the discreteness remainder) in one exact identity, non-linearly (product ζ(2σ−1)·ζ′/ζ).
Beurling systems indexed by their own integers are not even in the frame (the tests are indexed by ℕ).

## 3. The two Tate cancellations are FE images (PROVED)
**Prop 6.4.** The cancellations at σ = 3/2 (pole of ζ′/ζ(w) at w = 1, τ₀ = 0, killed by F̂₀(i/2)² = 0) and at σ = ½ (pole of ζ′/ζ(1 − w) at
w = 0, τ₀ = 0, killed by F̂₀(−i/2)² = 0) are exchanged by σ ↦ 2 − σ. ∎ (z ↦ −z, w ↦ 1 − w.)
So the lines σ = 3/2 (Chebyshev/absolute) and σ = ½ (Kakutani/ℓ²) of NT_003 are mirror images under the FE of the flow, about σ = 1.

## 4. Review
- Thm 6.1: the continuation of m to complex z is the even function ½[ψ(¼ + iz/2) + ψ(¼ − iz/2)] − log π; at real z it equals Re ψ(¼ + iz/2) −
  log π ✓. FE log-derivative form ✓ (standard).
- Cor 6.2: requires ζ(½ + iτ₀) ≠ 0 at the point; at zeros M has a pole (stated). No statement about where zeros are is made or needed.
- Thm 6.3(i) "of both signs": for δ supported at a single n₀, cos(τ₀ log n₀) changes sign — PROVED; for general δ, a real nonzero
  trigonometric polynomial Σ c_n cos(τ₀ log n) with frequencies log n > 0 has mean zero (almost periodic, no constant term), hence takes both
  signs — PROVED. ✓
- Is Thm 6.3 a positivity statement? No. It is a structural, Λ-specific characterization of the FE inside the flow. It becomes sign-relevant
  only through NT_007 (the value V at σ = 1).
- Danger of zero-side reasoning: none used; zeros appear only as possible poles of ζ′/ζ.
- **No sign contact.**

## Erratum note (after NT_005_007_REVIEW)
(4) The Epstein/DH caveat (stated in NT_007 §4) points the wrong way: their archimedean factors/conductors differ from ζ's, so with the fixed m
of ℚ the line identity m + 2Re L′/L(½+iτ) ≡ 0 fails and their curve symbols also have a pole at σ = 1. Regularity on the line forces ζ's FE
(Hamburger-type rigidity, CONDITIONAL on finite-order continuation). The regularity property is therefore MORE Λ-specific than stated.
**Cor 6.5 (added; PROVED).** For truncations a = Λ1_{n<N}, the residue at σ = 1, τ₀ = 0 is (F̂₀(0)²/(2ζ(2)))[m(0) − 2Σ_{n<N}Λ(n)n^{−½}] < 0
(m(0) = ψ(¼) − log π ≈ −5.37 < 0, and the Dirichlet sum is ≥ 0). Hence, by continuity in τ₀ and the curve reduction (σ < 3/2 needs the
analytic continuation; for D_a(σ) with a finite comb K^{(a)}_σ ∈ ℓ¹ for σ > 1 and Φ^{(a)}_σ is continuous, so the curve values are the
symbol): Φ^{(a)}_σ(ι(0)) → −∞ as σ ↓ 1, i.e. **every truncation fails D(σ) for σ close to 1, for every profile.**
