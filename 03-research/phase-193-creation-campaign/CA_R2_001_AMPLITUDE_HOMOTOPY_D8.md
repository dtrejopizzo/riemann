# CA_R2_001 — Re-examination of seed D8: the amplitude homotopy W(α) (phase 193, round R2)

Pen and paper; no
numerics. **No negative value of 𝔞_T for ζ is produced or claimed.**
Notation: CA_D_001 (Z_X, Z_T = e^{iΘ}Z_X(½+i·) real, μ_X = δ_0 + μ_− + μ_+, Lemma 2, Thm 1′, Thm 1″), CA_D_002 (Thm 2, 2′).
Audit entry: AUDIT_PHASE193_CERTAINTY, D8 killed at strength **1L** ("non-integer powers need zero information").

## 0. Pre-screen
- CA_D_002 (closure NO-GO): concerns limits of *tests* in the integer cone 𝒲_{T,K}. The homotopy here is a limit in the *weight*
  exponent α → 0 for a fixed test. Different limit; CA_D_002 does not cover it. It does constrain where the defect sits (Thm 2′).
- FE-class genericity: Thm 1″ makes every integer point hold for every FE series of the class (Epstein, DH, ζ_K). Hence any
  interpolation principle fed only by {integer-point positivity} + FE-generic structure proves the same for Epstein at α = 0. With O10
  CITED (complete form) / ARGUED (primitive bottom), this is a CIRC kill only; §3 replaces it by a PROVED abstract obstruction.
- (R)(4): checked separately for the *definition* (§1) and for the *mechanism* (§4).

## 1. Definition — needs no zero information (PROVED; corrects the D8 one-liner)
For F ∈ P_T (real, supp ⊂ [−T,T], F̂(±i/2) = 0) and real α ≥ 0 put
  W_F(α) := ∫_ℝ Θ_X′(τ) |F̂(τ)|² |Z_T(τ)|^{2α} dτ,   |Z_T(τ)| = |ζ(½+iτ)|·exp(−C_X(τ)).
|Z_T|^{2α} is a continuous function of τ, computable from |ζ| on the line; at an ordinate it is 0 (for α > 0), and no location of any
zero is used to define it. Integrability: |Θ′| ≪ log(2+|τ|) + e^{T}, |Z_T|^{2α} ≪_α (1+|τ|)^{α/2}, F̂ Schwartz. Continuity at 0:
for 0 ≤ α ≤ 1, |Z_T|^{2α} ≤ max(1, Z_T²), integrable against |Θ′||F̂|², and |Z_T|^{2α} → 1 off a null set; dominated convergence
gives **W_F(α) → W_F(0) = π𝔞_T(F) (σ_T = 2Θ′) as α → 0⁺**. The complex extension α ↦ W_F(α) is holomorphic on
Re α > −½ (near a simple ordinate |Z_T|^{2α} ≍ |τ−γ|^{2Re α}; Selberg-type multiplicities only shrink this half-plane, harmless for
Re α ≥ 0).
So the *family* is well-defined and zero-free. What D8's one-liner correctly flagged is narrower: the *holomorphic* power Z_X^α (needed
for the support mechanism) requires log Z_X holomorphic on Re s > ½, i.e. zero information. Two different objects; the seed conflated them.
**Corrected D8 status: the family is admissible under (R)(4); the question is whether its integer points control α = 0.**

## 2. Structure: W_F is a Laplace transform of a signed measure (PROVED)
Let ν_F be the push-forward of the signed measure Θ′|F̂|²dτ under ℓ(τ) := log|Z_T(τ)| ∈ [−∞,∞). Then
  W_F(α) = ∫ e^{2αℓ} dν_F(ℓ),    W_F(0) = ν_F(ℝ) = π𝔞_T(F) (up to the fixed constant).
Facts: (a) ν_F is signed (Θ′ changes sign; σ_T(0) < 0 is PROVED in P47). (b) For fixed F the integer points available are finite:
**if F ∈ P_T^{(k)} for every k, then F = 0** (F̂ entire, nonzero ⇒ zero at i/2 of finite order). So a fixed test has PROVED nodes
W_F(k) ≥ 0 only for 1 ≤ k ≤ K(F) < ∞ (Thm 1′), K(F) = Tate order of F.

## 3. Interpolation from the integer points: NO-GO (PROVED, abstract)
**Proposition 3.1.** Let 𝔉 be the class of functions w(α) = ∫e^{2αℓ}dν(ℓ), ν a finite signed Borel measure on ℝ with compact
support. For every K ≥ 1 there is w ∈ 𝔉 with w(k) > 0 for all integers k ≥ 1 (in particular 1 ≤ k ≤ K), w entire of exponential
type, increasing on [0,∞), and w(0) < 0.
*Proof.* ν = p δ_0 − q δ_{−L} with L > 0, 0 < p < q < p e^{2L}. Then w(α) = p − q e^{−2αL}: w(0) = p − q < 0, w(1) = p − qe^{−2L} > 0,
w′ > 0. Exponential type 2L; Carlson's theorem is not violated (w is not determined by inequalities at the integers). ∎
**Consequences.** (i) Log-convexity / Hölder: applies to positive measures only; ν_F is signed, and in the model w changes sign, so
log w is undefined on [0, α₀). (ii) Riesz–Thorin / Stein analytic interpolation: interpolate *norms* (moduli of analytic families) on
the interior of a strip whose edges carry bounds; α = 0 is an endpoint *outside* [1, K], and a sign is not a modulus bound. A three-lines
argument would need a bound of Re W on Re α = 0 — that is the target itself (REF-D). (iii) Monotonicity: the model is increasing;
monotone *decrease* W_F(0) ≥ W_F(1) would suffice, but (Prop 3.2) is not available pointwise and is ARGUED false integrally.
(iv) Any principle valid on 𝔉 (or on any subclass containing the two-atom model) cannot deliver W_F(0) ≥ 0. **The interpolation
route is closed for the method class "integer-point positivity + analyticity/convexity in α".** Strength: THM (upgrades the 1L kill).

**Proposition 3.2 (the only sufficient comparison, and where it fails).** W_F(0) − W_F(1) = ∫Θ′|F̂|²(1 − Z_T²)dτ. Pointwise
Θ′(1 − Z_T²) ≥ 0 would give W_F(0) ≥ W_F(1) ≥ 0 on P_T. It is FALSE on the central Nyquist cell I_T (T ≥ 1): there Z_T² ≤ 6.6e^{−√2B_X}
< 1 (CA_D_001 §4, PROVED) while Θ′(0) = σ_T(0)/2 < 0 (PROVED). Integrated form: for tests with spectrum at large |τ₀| (archimedean
part of Θ′ ≈ ½log(|τ₀|/2π) dominating e^{T}), W_F(1) − W_F(0) ≈ c(τ₀)·2πρ_F > 0 by Cor 1.1(i) — ARGUED. So the comparison runs the
wrong way generically.

## 4. Could a non-integer α itself be proved positive by the CA_D_001 mechanism? NO (PROVED for the singular part)
By continuity (§1), positivity of W_F on (0, α₀) for all F ∈ P_T would give row D; so the real question is small non-integer α.
The mechanism of Thm 1′ needs (1) a holomorphic Z_X^α on Re s > ½ — zero information, excluded by (R)(4); and even granting it,
(2) the polar part to be killed by Tate-type conditions. At non-integer α the polar factor is κ^α(s−1)^{−α}·h(s), h holomorphic,
whose leading transform is c_α e^{u/2}(2T − u)_+^{α−1}. One-sided support of F * (that) on u ≤ T requires
  Φ(c) := ∫F(w)e^{−w/2}(c + w)^{α−1}dw = 0  for all c ≥ T.
For c > T > |w|, (c+w)^{α−1} = c^{α−1}Σ_m binom(α−1, m)(w/c)^m, with binom(α−1,m) ≠ 0 for all m when α ∉ ℤ. Vanishing for all c ≥ T
forces every moment ∫F e^{−w/2}w^m dw = 0, hence F e^{−w/2} = 0 (compact support), F = 0.
**Proposition 4.1 (PROVED for the leading singular term; ARGUED for the full h).** For α ∉ ℤ the Tate-admissible class of the
support mechanism is {0}, even if Z_X is assumed zero-free on Re s > ½. At α = k ∈ ℕ the binomial series terminates — this is exactly
why Thm 1′ needs only k Tate conditions. **Integers are isolated points of the mechanism, not samples of a continuum.**
At α → 0 the Thm 1′ identity reads α·W_F(α) = 2π∫u|g_α|²; both sides → 0, and the α-derivative at 0 returns ∫Θ′|F̂|² = W_F(0)
via the transform of log Z_X — REF-D (the linearization of the homotopy at its endpoint is row D).

## 5. Where a ζ-specific input would have to enter
Theorem 1″ holds on the whole FE class, so every integer node is FE-generic. By Prop 3.1 the nodes cannot fix the sign; by CA_D_002
Thm 2′ and Prop 3.2 the deficit is carried by ν_F on {ℓ < 0} = {|Z_T| < 1}, specifically the central cell and the ordinates.
The ζ-specific input must therefore be **a statement about ν_F restricted to {ℓ < 0}**: e.g. a bound ν_F^−({ℓ<0}) ≤ (weighted
positive mass), which is a constraint on how Θ′ < 0 coexists with |ζ/Z_{<X}| < 1. Such a statement is not supplied by any integer node,
and is not FE-generic by thm:shape(C). It is a reformulation of the target localized to {|Z_T|<1} — REF-D, a valid objective (OPEN), not
a closure.

## 6. Verdict
| item | label |
|---|---|
| W_F(α) well-defined, zero-free, continuous at 0, holomorphic on Re α > −½ | PROVED |
| D8 one-liner "(4) ✗" | WRONG for the family; correct only for the holomorphic power Z_X^α |
| fixed F: finitely many PROVED nodes (infinite Tate order ⇒ F = 0) | PROVED |
| interpolation from integer nodes (log-convexity, Riesz–Thorin/Stein, three lines, monotonicity) | NO-GO, PROVED (Prop 3.1), method class declared |
| comparison W(0) ≥ W(1) | pointwise FALSE (PROVED, I_T); integrated ARGUED false at high frequency |
| support mechanism at non-integer α | NO-GO (Prop 4.1 PROVED for leading singularity, ARGUED full) |
| "W_F ≥ 0 on (0,α₀)" / "ν_F on {|Z_T|<1}" | REF-D, OPEN objective |
D8 stays discarded as an *interpolation route*; kill strength upgraded 1L → THM. The family survives as a coordinate (the push-forward
ν_F), which localizes the defect exactly as CA_D_002 did.

## 7. Self-review
1. *Is Prop 3.1 relevant — W_F is not an arbitrary element of 𝔉?* The claim is about a method class: principles using only node
   positivity plus analytic/convex structure in α. Such a principle, valid for W_F, must use a property distinguishing W_F from the
   two-atom model; no such property is given by Thm 1′. Restriction to the subclass realizable as W_F is OPEN, and that is exactly the
   ζ-input of §5. ✓ (scope stated)
2. *Is the model compactly supported in ℓ while ν_F is not (ℓ → −∞ at ordinates, +∞ at large τ)?* Prop 3.1 needs only that the class
   contains the model; non-compact supports only enlarge the class. ✓
3. *Prop 4.1: is the leading-term analysis legitimate when F has Tate order K?* The moment conditions are infinite for every non-integer
   α regardless of K; the correction h(s) contributes further terms of the same (c+w)^{α−1+m} type, which cannot cancel all moments of
   a fixed compactly supported F identically in c; hence ARGUED, not PROVED, for the full term. ✓ (label kept)
4. *Continuity at α = 0 and normalization of W(0):* W(0) = ∫Θ′|F̂|² is the window form up to the constant fixed in CA_D_001 Thm 1. ✓
5. *Any zero information used?* Definition: none. §4 explicitly *grants* zero-freeness to show even that does not help — hypothetical,
   not an input. ✓  *Any use of D ⟺ other statements?* None. *Negative value for ζ?* None certified. ✓
