# CA_N_002 — (V2) Positive Poisson combs on both sides: three constructions and a unimodular-transfer impossibility theorem (front N, phase 193)

 Pen and paper; the only numbers are closed-form constants (C₀ = ψ(¼) − log π = −γ − π/2 − 3log2 − log π
≈ −5.3721, v₂ + v₃ = 2.24883 = P46 \Aconst), evaluated by hand to 4 digits; no computation of ζ. **No negative value for ζ.**
Conventions of CA_D_001: F̂(τ) = ∫F e^{iτx}dx, ǧ(τ) = ∫g e^{−iτu}du; 𝔞_T(F) = (1/2π)∫σ_T|F̂|² = (1/π)∫Θ′|F̂|², Θ′ = σ_T/2.

## 1. The comb–comb Fourier pair has a forced sign (PROVED)
By thm:Z / Weil, for even test h: Σ_ρ ĥ(γ_ρ) + Σ_n v_n h(log n) = 2∫h cosh(u/2) + (1/2π)∫mĥ. Read as a Fourier pair: the τ-side measure
Z := Σ_ρ δ_{γ_ρ} has u-side transform (polar + archimedean) − ½Σ v_n(δ_{log n} + δ_{−log n}).
**Proposition 1.1 (sign rigidity).** For any weight ω on the τ-side whose inverse transform ω̌ is a finite measure, the atomic part of the
u-side transform of ωZ is −½ ω̌ ∗ Σ v_n(δ_{±log n}) plus the atoms of ω̌ ∗ (polar + arch) (none: those are a.c.). Its weights are
determined by ω, and for ω ≥ 0 a trigonometric polynomial ω = |P_s|², P_s = Σ_{x∈X} s_x e^{iτx}, X ⊂ log ℕ, the pairing ∫ωF̂₀²dZ is
s^T𝔸_M s (prop:AM(ii)).
*Proof.* Uniqueness of the Fourier transform of tempered distributions; prop:AM(ii). ∎
So "making both combs positive by a change of variables" on the τ-side is either a weight ω (the u-comb weights become −½(ω̌∗v), positive
only where ω̌ is signed, and the positive statement is the site matrix: REF-D), or a change of the comb itself (leaves the class).
The positive τ-comb Z is zero-side ((R)(4)).

## 2. Adelic and lattice Poisson: positive on both sides, but shared (PROVED + CITED)
**Construction 2.1 (Tate).** For f ∈ S(𝔸_ℚ), Σ_{a∈ℚ}f(a) = Σ_{a∈ℚ}f̂(a) (CITED Tate 1950): both sides are positive Dirac combs on the
self-dual lattice ℚ ⊂ 𝔸; with f = e^{−πx²}⊗1_{Ẑ} it gives θ(1/x) = x^{1/2}θ(x)·(normalization) and the FE of ζ. (V2) EXISTS for ℚ.
**Proposition 2.2 (the multiplicative image is the explicit formula; PROVED/CITED).** The window form is a form on functions of the
multiplicative variable (u = log x on C_ℚ/Ẑ^× ≅ ℝ_{>0}). The passage from 𝔸 to C_ℚ is the map E(f)(x) = |x|^{½}Σ_{q∈ℚ^×}f(qx), which is
positivity-preserving; its Mellin transform is Z(f, s) (Tate), linear in f. The window symbol needs −ζ′/ζ, i.e. the logarithmic derivative of
Z(f, s) — a non-linear operation in f, after which the u-comb carries −v_n (Prop 1.1). Positivity of both additive combs is therefore lost
exactly at the logarithm.
**Proposition 2.3 (Epstein has it; PROVED).** For Q = x² + 5y² (class number 2, the O10 falsifier of lem:shape-epstein), Poisson summation on
ℤ² ⊂ ℝ² with the Gaussian e^{−πQ} has positive combs ℤ² and its dual ((ℤ²)* ≅ the lattice of 5x² + y² ≅ Q up to scale): (V2) in the
lattice form holds for Epstein. Also every Dedekind ζ_K (Tate over K, O12). Hence (V2)-adelic/lattice is FE-class generic.

## 3. The amplitude-k transfer: (V2) built for k ≥ 1 (CA_D_001, PROVED there)
(1/π)∫Θ′|F̂|²Z_T^{2k}dτ = (2π/k)∫_T^∞u|R^{(k)}|²du ≥ 0: the u-side becomes a positive density u·1_{u≥T}. This IS a "positive on both sides"
representation of a window-type form, at amplitude |Z_X|^k. FE-generic (Thm 1″: Epstein, ζ_K). The question for (V2) at row D is the
amplitude-0 endpoint.

## 4. Theorem N2 (no unimodular analytic-signal transfer at amplitude 0; PROVED)
**Definition.** 𝒰_T = set of measurable unimodular W on ℝ such that, for every even F ∈ P_T^∞: (i) WF̂ = e^{−iφ}r_F with r_F real and one
φ ∈ C¹ independent of F with φ′ = σ_T/2; (ii) g_F := the function with ǧ_F = WF̂ is supported in [0, ∞).
For W ∈ 𝒰_T, CA_D_001 Lemma 2 gives 𝔞_T(F) = (1/π)∫φ′|WF̂|² = 2∫_0^∞u|g_F|²du ≥ 0: 𝒰_T is precisely "a change of variables in which the
window form becomes a positive u-side moment" at amplitude one.
**Theorem N2.** If σ_T(0) < 2T − 8, then 𝒰_T = ∅. Since σ_T(0) = C₀ − A_T with C₀ = ψ(¼) − log π ≈ −5.372
and A_T = Σ_{n<e^{2T}}v_n, this holds for every T ≥ ½log 3 (there A_T ≥ 2.2488, 2T ≥ 1.0986: C₀ − A_T ≤ −7.62 < 2T − 8 ⟸ 2T + A_T ≥ 3.35 > 2.628),
and for every T > 1.314.
*Proof.* (a) Since F̂ is real for even F, (i) gives We^{iφ} real, unimodular, continuous ⇒ W = ±e^{−iφ}: W is unique up to sign.
(b) Let H²_− = {ǧ : g ∈ L²[0,∞)}; its elements extend to Im τ < 0. Inner functions of ℂ_− have −d(arg)/dτ ≥ 0 (a positive measure);
e^{−iaτ} (a ≥ 0) and the Blaschke factor b(τ) = (τ + i/2)/(τ − i/2) (zero at −i/2) are inner, with −d arg b/dτ = 1/(τ² + ¼).
(c) For F even, supported in [−T+ε, T−ε], F̂ = e^{iTτ}ȟ_F with ȟ_F ∈ H²_−, ȟ_F entire of exponential type; its inner part is
e^{−iετ}·b·J_F (Cartwright class: Blaschke product over zeros in ℂ_− times the type defect; b because F̂(−i/2) = 0). By (ii), G_F := WF̂ ∈ H²_−.
So W = e^{−iTτ}G_F/ȟ_F; inner–outer factorization and |W| = 1 give equal outer parts up to a constant, hence W = c e^{−iTτ}I_F/(e^{−iετ}bJ_F)
with I_F inner.
(d) Choose F₁, F₂ (F = (¼ − ∂²)H with H even in C_c^∞, e.g. H₂ a dilate of H₁ chosen so that Ĥ₁, Ĥ₂ have no common zero in ℂ_−) with J_{F₁},
J_{F₂} coprime. From I₁/J₁ = I₂/J₂ and coprimality, J₁ | I₁, so Q_ε := I₁/(e^{−iετ}J₁) satisfies W = c e^{−iTτ}Q_ε/b with e^{−iετ}Q_ε inner
for every ε > 0; letting ε → 0 (bounded by 1 in ℂ_−, pointwise limit) Q := Q₀ is inner. Hence
  φ′ = −d(arg W)/dτ = T + μ_Q − 1/(τ² + ¼) ≥ T − 1/(τ² + ¼)   (μ_Q ≥ 0).
(e) At τ = 0: σ_T(0)/2 = φ′(0) ≥ T − 4. Contradiction when σ_T(0) < 2T − 8. Value: m(0) = C₀ (P46 l.170), σ_T(0) = C₀ − A_T. ∎
**Reading.** CA_D_001 obtains one-sidedness by multiplying by Z_X, which is analytic in ℂ_− with the pole cancelled by Tate; at amplitude 0
the only candidate multiplier is e^{−iΘ} = Z_X/Z_T (unique by (a)), and Theorem N2 shows it is never "analytic enough": its phase velocity
would have to exceed T − 1/(τ² + ¼), while the window symbol at the centre is ≤ C₀ − A_T. **The impossibility sits at the centre, where the comb
is coherent** — the same place where CA_D_001 §4 found the Hardy weight doubly-exponentially small.
For T < ½log 3 the theorem says nothing (for T < ½log2 the bound is compatible); not decided there (OPEN, irrelevant to the sign since P46
proves the sign at small T).

## 5. Verdict (V2)
Comb–comb pair: sign forced (Prop 1.1), positive weighting = site matrix (REF-D). Adelic/lattice Poisson: BUILT (exists for ℚ) but shared by
Epstein and ζ_K (Prop 2.3) and lost at the logarithm (Prop 2.2). Amplitude k ≥ 1: BUILT (CA_D_001), FE-generic. Amplitude 0 by unimodular
analytic-signal transfer: IMPOSSIBLE for all T ≥ ½log 3 (Theorem N2, PROVED).
## 6. Self-review
- (a) uses φ ∈ C¹ and r_F real; if r_F were allowed to vanish on intervals, W e^{iφ} is still continuous unimodular real on ℝ, hence constant. ✓
- (c) one-sidedness on [0,∞) is the natural normalization (Lemma 2 needs u ≥ 0 on the support for positivity); a support [c,∞) with c > 0
  only strengthens the bound (φ′ ≥ T + c − …); c < 0 loses positivity of ∫u|g|². ✓
- (d) the existence of F₁, F₂ with coprime J is generic; ARGUED-to-PROVED by choosing H₂(x) = H₁(λx), λ ≠ 1 close to 1, whose zeros are
  dilates; a common zero z would need z and z/λ both zeros of Ĥ₁ for a continuum of λ — impossible for a nonzero entire function. ✓
- Inner-function phase monotonicity in ℂ_−: sign checked on e^{−iaτ} and on b. ✓
- Theorem N2 is a theorem about a class of *proof architectures*, not about the sign of 𝔞_T: it is compatible with 𝔞_T ≥ 0. ✓
- Novelty: CA_D_001 §4 states the amplitude-one obstruction informally ("dividing by Z_T destroys the half-line support"); Theorem N2 is the
  quantitative, class-wide version (uniqueness of W + phase-velocity lower bound). Not a retry.
