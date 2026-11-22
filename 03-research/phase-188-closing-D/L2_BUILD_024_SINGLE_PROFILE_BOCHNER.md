# L2_BUILD_024 — Sufficiency via multi-copy spans: one explicit profile and one positive-definite function

## Corpus check
Paper 46 §subsec:KEP (Kreĭn extension problem; "the datum is positive definite on the window" ⟺ restriction of the explicit-formula datum
g to (−2T,2T) extends to a positive definite tempered distribution, Schwartz–Bochner), lem:polar, Thm Z; N_BUILD_014 §3 (multi-copy →
packets); L2_BUILD_023 (Lemma L, Theorem T; under referee review, not edited); R162_2601 (translates of a fixed test, polynomial bound).
New: the reduction to translates of ONE fixed explicit profile with positive Fourier transform (Theorem S), and the sharpness check of T.
The KEP is a window-by-window statement about g; Theorem S is a single-function statement in the lag variable, uniform in T.

## 0. Sharpness of Theorem T (023) — identity check only (CITED explicit formula; CONDITIONAL on a Kronecker hypothesis)
For F₀ with 2T₀ < log 2 and zeros written ρ = ½ + iγ_ρ, the explicit formula as an identity gives a₀ = Σ_ρ F̂₀(γ_ρ)conj F̂₀(conj γ_ρ) and
B(d) := 𝔞(F₀, τ_dF₀) = Σ_ρ F̂₀(γ_ρ)conj F̂₀(conj γ_ρ)e^{iγ_ρ d} (both sides finite; polar terms vanish on primitive tests). For real γ_ρ this
reads B(d) = Σ|F̂₀(γ_ρ)|²cos(γ_ρ d), so |B(d)| ≤ B(0) = a₀ and X(d) = −2B(d) + O(e^{−5d/2}): the band |X| ≤ 2a₀ of Theorem T is the
trivial bound of a cosine sum with nonnegative coefficients. It is APPROACHED (sup_d |X(d)| = 2a₀) iff the cosines can be made
simultaneously ≈ ±1 with weights |F̂₀(γ)|² — true if the γ_ρ are ℚ-linearly independent (Kronecker; CONDITIONAL, unproved hypothesis).
So Theorem T is sharp CONDITIONALLY; recorded as identity/heuristic only (not a criterion).

## 1. The function B_{F₀} (PROVED)
For F₀ = (¼−∂²)G₀ (G₀ ∈ H²_0(I_{T₀}), real) define for d ∈ ℝ
  B_{F₀}(d) := 𝔞(F₀, τ_dF₀) = C₀c₀(d) + ∫_0^∞[c₀(d) − ½(c₀(d−u) + c₀(d+u))]K(u)du − ½Σ_{n≥2}v_n[c₀(d − log n) + c₀(d + log n)],
c₀ = c_{F₀} (support [−2T₀, 2T₀]); for each d only finitely many n contribute (|log n ± d| ≤ 2T₀). B is continuous, even, and for every T
the form on any F = Σ_k s_kτ_{a_k}F₀ with all a_k + I_{T₀} ⊂ I_T equals Σ_{k,l}s_ks_lB(a_k − a_l).
*Proof.* Bilinear version of eq:Aform; translation invariance of the convolution symbol; the comb pairs c_F at log n only, and c_F vanishes
beyond 2T. (Lemma L(i): such F ∈ P_T.) ∎

## 2. Theorem S (single-profile reduction)
Let F₀ be the explicit profile: g(t) := e^{bt}1_{[0,a]}(t) (a > 0, b ≠ 0), G₀ := g*g̃*g*g̃ (g̃(t) = g(−t)), shifted to be centred, with
4a < log 2 so 2T₀ = 4a·… < log 2, and F₀ := (¼−∂²)G₀. Then:
(i) G₀ ∈ H²_0(I_{T₀}) (fourfold convolution of bounded compactly supported functions: C², vanishing with first derivative at the ends), so F₀ is
    primitive (PROVED).
(ii) F̂₀(τ) = (τ² + ¼)|ĝ(τ)|⁴ with ĝ(τ) = (e^{(b+iτ)a} − 1)/(b + iτ), whose zeros τ = 2πk/a + ib are non-real (b ≠ 0); hence F̂₀ > 0 on ℝ and
    |ĝ(τ)| ≥ |e^{ba} − 1|/|b + iτ|, so 1/F̂₀² is C^∞ with polynomial growth (PROVED).
(iii) (target ⟹ PD, PROVED) If λ_A(T) ≥ 0 for all T, then B_{F₀} is a positive definite function on ℝ: for any finite a_1..a_K, s ∈ ℝ^K, take T so
    large that all translates fit; Σs_ks_lB(a_k − a_l) = 𝔞_T(F) ≥ 0.
(iv) (PD ⟹ target, PROVED modulo Lemma I below) If B_{F₀} is positive definite, then by Bochner B_{F₀}(d) = ∫e^{iτd}dμ(τ) with μ a finite positive
    measure (|B| ≤ B(0)), and μ = (1/2π)σ_∞F̂₀²dτ in the sense of Lemma I, where σ_∞ := m − Σ_{n≥2}v_n cos(τ log n) (a distribution on
    Paley–Wiener test functions). For G ∈ P_T smooth, 𝔞_T(G) = (1/2π)⟨σ_∞, |Ĝ|²⟩ = ∫ |Ĝ|²/F̂₀² dμ ≥ 0, and smooth G are form-dense in P_T ∩ D_T.
Hence: **λ_A(T) ≥ 0 for all T ⟺ the single explicit function B_{F₀} is positive definite on ℝ.**
Lemma I (ARGUED): for |Ĝ|² with G smooth and compactly supported, ⟨σ_∞, |Ĝ|²⟩ = ∫(|Ĝ|²/F̂₀²)(2π dμ). Sketch: both sides are limits of the
same pairing on the dense class {F̂₀²·φ̂ : φ ∈ C_c^∞}; on that class it is ⟨B, φ⟩, finite; continuity of the left side in the relevant
topology (rapidly decreasing |Ĝ|² with compact lag support) and dominated convergence on the right (μ finite, |Ĝ|²/F̂₀² rapidly decreasing
since F̂₀^{−2} grows polynomially) give equality. Not written in full; label ARGUED.

## 3. What the reformulation says
B_{F₀}(d) = A(d) − ½X(d) with A(d) the explicit archimedean part (C₀c₀ + Lévy part; for |d| > 4T₀ it is O(e^{−5|d|/2}) by Lemma C of 023) and
X(d) the prime part. For |d| > 4T₀, B(d) = −½Ξ(d) + O(e^{−5d/2}): a smoothed Chebyshev fluctuation at scale e^{|d|}, main term removed by the
Tate conditions. **D is equivalent to: the function d ↦ a₀δ-part ⊕ (−½Ξ(d)) — i.e. B_{F₀} — is positive definite on ℝ**, for ONE explicit
profile F₀ (any profile with F̂₀ > 0 on ℝ works). Theorem T is its 2×2 case; multi-copy matrices are its finite sections.
Escape analysis: not a norm bound (PD is an infinite family of quadratic conditions), not W-loc (all lags), not W-fam (one window-free
function, not window observables); it is a reformulation (like KEP), so barriers are not violated but nothing is gained in sign either.
Finmod (cor:void): deletion/amplification change B(d) at d = log n₀ — PD fails for them at large amplification (consistent).

## 4. Review
- §0 uses the explicit formula only as an identity; the sharpness claim is CONDITIONAL on Kronecker independence of ordinates (unproved). OK.
- §2(i): fourfold convolution of bounded functions supported on [0,a] is C² with G₀, G₀′ vanishing at the ends — correct (k-fold convolution of
  bounded compactly supported functions is C^{k−2} and vanishes to order k−1 at the endpoints of its support). Support length 4a; condition
  2T₀ = 4a < log 2 needed only for the central-window remark, not for Theorem S.
- (ii) correct: zeros of e^{(b+iτ)a} = 1 are τ = 2πk/a + ib.
- (iii) PROVED. (iv) depends on Lemma I (ARGUED); with Lemma I it is a clean equivalence. Relation to KEP: KEP is per window and about
  the datum g; Theorem S fixes one profile and removes T. Novelty: moderate (Bochner reformulations of Weil positivity are classical in spirit);
  the single-explicit-profile compression with F̂₀ > 0 is not in the corpus.
- No sign certified; no negative value of 𝔞_T for ζ.
