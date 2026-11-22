# CA_I_001 — Markov structure of the window form, Krein–Rutman, and the "Markov for all T" rigidity theorem (seeds I1, I2, I3, I10)

Phase 193. Pen and paper; **no numerics**.
NO-GO / REF-D. **No sign contact. No negative value for ζ.** Checked against P46 eq:form, def:quartetmodel, prop:quartetmodel,
lem:shape-quartet, def:shape-ops.

## 0. Setting
I_T = [−T,T]; F ∈ L²(I_T) real, extended by 0; c_F(u) = ∫F(t)F(t+u)dt; 𝒩_T = {n ≥ 2 : log n < 2T}; v_n = 2Λ(n)n^{−½} (P46 normalization).
**Lévy–Khintchine form of the archimedean symbol (CITED: phase-60 H1_PROOF Lemma A, "Ω CND", P60-1 of the index).** m(τ) = m(0) + 2∫_0^∞(1 − cos τu)ν(u)du
with ν(u) = κ·e^{−u/2}/(1 − e^{−2u}) > 0 for all u > 0 (κ > 0 a normalization constant; ν(u) ~ κ/(2u) at 0, ν(u) ≤ Cκe^{−u/2} at ∞; ν decreasing).
Since (1/2π)∫(1 − cos τu)|F̂|² = ‖F‖² − c_F(u) = ½∫(F(t) − F(t+u))²dt, the window form on L²(I_T) is
  **𝔞_T(F) = m(0)‖F‖² + ∫_0^∞ ν(u)∫_ℝ(F(t) − F(t+u))²dt du − Σ_{n∈𝒩_T} v_n c_F(log n)**,   (0.1)
the polar term vanishing on 𝒫_T = {∫Fe^{±t/2} = 0} (P46). Domain 𝒟_T = {F : arch part finite} (log-Sobolev); compact resolvent (P46).
λ₀(T) := min 𝔞_T on L²(I_T) (unconstrained), λ_A(T) := min 𝔞_T on 𝒫_T, h₀, h* unit minimizers.

## 1. Theorem 1 (Markov structure; PROVED from the CITED Lévy–Khintchine form)
(i) (first Beurling–Deny criterion) F ∈ 𝒟_T ⇒ |F| ∈ 𝒟_T and 𝔞_T(|F|) ≤ 𝔞_T(F). Hence e^{−sA_T} is positivity preserving on L²(I_T).
(ii) It is positivity improving (ν > 0 on (0,∞), I_T connected).
(iii) λ₀(T) is simple, h₀ > 0 a.e.; λ_A(T) > λ₀(T) strictly; λ_A(T) ≤ λ₂(T) (third unconstrained eigenvalue).
*Proof.* (i) (|F(t)| − |F(t+u)|)² ≤ (F(t) − F(t+u))² and c_{|F|}(u) ≥ c_F(u) pointwise; Λ ≥ 0. Positivity of the semigroup is equivalent to (i)
for closed real forms (Ouhabaz, *Analysis of heat equations on domains*, Thm 2.6; CITED). (ii) If E ⊂ I_T is invariant, the arch term of 1_E
is ∫ν(u)|E ∖ (E − u)|du·2 = 0 forces |E|·|I_T∖E| = 0 (ν > 0); irreducible + positive ⇒ improving (Reed–Simon IV, XIII.44; CITED).
(iii) Perron–Frobenius for positivity-improving semigroups (same reference) gives simplicity and h₀ > 0. ⟨h₀, e^{t/2}⟩ > 0, so h₀ ∉ 𝒫_T; if
λ_A = λ₀ the constrained minimizer would be a ground state, i.e. a multiple of h₀: contradiction. λ_A ≤ λ₂: the span of the first three
eigenvectors meets 𝒫_T (codim 2). ∎
This re-derives P60-1 (simplicity) in the window normalization; P60-1 recorded already that it "gives simplicity, not sign".

**Proposition 1.1 (Krein–Rutman does not reach the constrained problem; PROVED).** (a) The Euler–Lagrange equation reads
(A_T − λ_A)h* = β₀e^{t/2} + β₁e^{−t/2}. For μ < λ₀, R(μ) = (A_T − μ)^{−1} is positivity improving and the polar Gram matrix
𝔊(μ) = [⟨R(μ)φ_i, φ_j⟩] (φ_± = e^{±t/2}) is entrywise > 0 with 𝔊′(μ) ≻ 0. (b) λ_A > λ₀ (Thm 1(iii)), so the EL equation is never in the
positive regime: h* = R(λ_A)(β·φ) with R(λ_A) not positivity preserving. (c) The constrained operator P_TA_TP_T is not Markov: P_T is not
positivity preserving (it maps φ₊ + φ₋ ≥ 0 to 0 and maps positive bumps near the edge to sign-changing functions).
*Proof.* (a) standard: R(μ) = ∫_0^∞e^{μs}e^{−sA}ds. (b) Thm 1(iii). (c) direct. ∎
**Reading.** The Weinstein–Aronszajn count n₋(A|𝒫) = n₋(A) − n₋(𝔊(0)) (A invertible) is the polar-capacity restatement 𝔊_T of P46
(retry, REF-D). Krein–Rutman sign information lives below λ₀ < λ_A and does not transfer.

**Proposition 1.2 (comparison, seed I10; PROVED).** (a) For combs a ≤ a′ pointwise (both ≥ 0), λ₀(T;a′) ≤ λ₀(T;a): the minimum is attained
at a positive h₀ and c_{h₀} ≥ 0. (b) λ_A(T;·) is concave on the cone of combs (an infimum of affine functions of a), with supergradient
−(v-normalized) c_{h*}(log n) at a. (c) λ_A(T;·) is not monotone: c_{h*}(log n) has no fixed sign on 𝒫_T (R165_202 1.2: the form
F ↦ c_F(log n) has both signs with infinite multiplicity on every subspace of finite codimension).
(b) is the concavity of CA_B_008 (retry); recorded only because it makes {a : λ_A(T;a) ≥ 0} convex.

## 2. Theorem 2 (the Markov class proves nothing; NO-GO, PROVED)
Let 𝒦_M be the deduction class (P46 def:shape-class) whose properties are any of: positivity preservation / Beurling–Deny (i), irreducibility,
Perron–Frobenius ground state, nonlocal maximum principle (A − μ ≥ 0 on positive cone for μ < λ₀), domination comparisons, parity
invariance, the Tate constraint data, and every class-generic minimizer property of CA_I_000 I0(a) (simplicity, real-rootedness of ĥ*,
≥ 2 sign changes (§4), node continuity, Hadamard edge principle). Then 𝒦_M is closed under O2 with c > 0 at a prime power n₀ (and under
O4 with c > 1, O6, O11, O12, O15), and for every T with log n₀ < 2T, λ_A(T; Λ + c1_{n=n₀}) → −∞ as c → ∞. Hence no deduction in 𝒦_M
proves λ_A ≥ 0.
*Proof.* Adding c v_{n₀}δ_{log n₀} (c > 0) keeps Λ + c1_{n₀} ≥ 0, so Thm 1 and every listed property persist. Existence of F ∈ 𝒫_T with
c_F(log n₀) > 0: put u = log n₀ < 2T, fix an interval K of length < u with K, K + u ⊂ I_T, disjoint subintervals J₁, J₂, J₃ ⊂ K, g_j ≥ 0 smooth
nonzero on J_j, F_j := g_j + g_j(· − u). For j ≠ k the four overlaps J_j ∩ J_k, J_j ∩ (J_k − u), (J_j + u) ∩ J_k, (J_j + u) ∩ (J_k − u) are empty
(|K| < u), and within one F_j the terms ∫g_jg_j(·+u), ∫g_j(·−u)g_j(·+u), ∫g_j(·−u)g_j vanish for the same reason, so for F = Σα_jF_j,
c_F(u) = Σα_j²‖g_j‖² > 0 unless α = 0. The 3-dimensional span meets 𝒫_T in F ≠ 0.
Then λ_A ≤ 𝔞_T(F)/‖F‖² − c v_{n₀}c_F(log n₀)/‖F‖² → −∞. ∎
**Reading.** Every maximum-principle / Krein–Rutman / comparison argument is a statement about the cone of positive functions, and adding
positive comb mass only strengthens it while destroying the sign. The qualitative theory of the Markov structure is blind to (R)(1).

## 3. Theorem 3 (rigidity: "Markov for all T" separates ζ from O7 and O9; PROVED, one CITED input)
Let E be a nonconstant real rational function with E(s) = E(1 − s) such that ξE is entire. The window form of ξE is
𝔞^E_T(F) = 𝔞_T(F) + ∫_ℝ c_F(u)K_E(u)du, K_E(u) := Σ_ρ m_ρ e^{(ρ−½)u} (ρ over zeros and poles of E, m_ρ = ± multiplicity)
(the quartet case E = [((s−½)² − z²)((s−½)² − z̄²)]^k gives K_E = kβ_z, P46 def:quartetmodel; general E: same explicit-formula bookkeeping,
K_E bounded on [−2T,2T] so 𝔞^E_T is a bounded perturbation, closed with compact resolvent). Then:
**there is T_E < ∞ such that for every T ≥ T_E the form 𝔞^E_T violates the Beurling–Deny criterion (its semigroup is not positivity preserving).**
In particular every quartet model ξ_{z,k} (k ≥ 1, any z) and every FE-preserving entire polynomial or zero-removing twist of O9 is non-Markov at
large T, while ζ's form is Markov at every T (Thm 1).

*Lemma 3.1 (exact criterion; PROVED).* For real F, 𝔞^E_T(|F|) − 𝔞^E_T(F) = 2∫_0^{2T}(K_E(u) − ν(u))(c_{|F|} − c_F)(u)du − Σ_{𝒩_T}v_n(c_{|F|} − c_F)(log n).
If K_E > ν on a set of positive measure in (0, 2T), the criterion fails.
*Proof.* The identity is (0.1) term by term (∫_ℝ K_E(c_{|F|} − c_F) = 2∫_0^∞ by evenness). Take a Lebesgue-density point u₀ ∉ log ℕ of
{K_E > ν}, with K_E − ν ≥ η > 0 on (u₀ − 3ε, u₀ + 3ε) ⊂ (0,2T) free of log ℕ (K_E, ν continuous on (0,∞)). Let f₁, f₂ ≥ 0 be bumps of width
ε at x₀ and x₀ + u₀ inside I_T, F = f₁ − f₂. Then c_{|F|} − c_F = 2(f₁ ⋆ f₂)(u) ≥ 0, supported in |u − u₀| < 2ε (u > 0 side), positive there: the
integral is ≥ 2η∫(c_{|F|} − c_F) > 0 and the comb sum vanishes. ∎
*Lemma 3.2 (exponential-polynomial positivity; PROVED with one CITED fact).* K_E(u) > ν(u) on a set of positive measure in (U, ∞) for every U.
*Proof.* After cancellation K_E = Σ_j c_je^{w_ju}, c_j ∈ ℤ∖{0}, distinct w_j, set symmetric under w ↦ −w and w ↦ w̄ (FE and reality);
nonempty since E is nonconstant. Let δ* = max Re w_j ≥ 0 and P(u) := Σ_{Re w_j = δ*} c_je^{i Im(w_j)u}, a real trigonometric polynomial, ≢ 0
(distinct exponentials are independent). K_E(u) = e^{δ*u}P(u) + O(e^{δ′u}), δ′ < δ* (if δ* > 0), or K_E = P (if δ* = 0).
Case 1: P(u₁) > 0 for some u₁. P is almost periodic: there are η > 0, ℓ and a relatively dense set of intervals of length ℓ on which
P ≥ η. There K_E ≥ η/2 for u large, while ν(u) ≤ Cκe^{−u/2} → 0: done.
Case 2: P ≤ 0 everywhere. A nonzero real trigonometric polynomial that is ≤ 0 has negative mean; the mean is the coefficient c₀ of the
frequency 0, i.e. of w = δ* real, so E has a net pole at the real point ½ + δ*. Then ξE entire forces ξ(½ + δ*) = 0. **But ξ(σ) > 0 for every
real σ (CITED: ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s), with ζ(σ) < 0 on (0,1) because (1 − 2^{1−σ})ζ(σ) = Σ(−1)^{n−1}n^{−σ} > 0, and ζ(σ) > 0 for σ > 1, and
FE).** Contradiction; Case 2 is void. ∎
*Proof of Theorem 3.* Lemma 3.2 gives u with K_E > ν on positive measure beyond any U; T_E := ½(that u + 1); Lemma 3.1. ∎

**Remark 3.3 (entireness is load-bearing; PROVED).** E = ((s−½)² − δ²)^{−k}, 0 < δ < ½, gives K_E = −2k cosh(δu) ≤ 0 < ν: the form of ξE
(not entire) is Markov for every T, keeps the comb Λ, Γ_ℝ, the FE and reality, and λ_A(T;ξE) → −∞ as k → ∞ (for real F, ∫_ℝc_F(u)e^{δu}du = L(−δ)L(δ) with L(x) := ∫F(t)e^{xt}dt, so
∫c_F cosh(δu)du = L(δ)L(−δ) = L(δ)² > 0 for even F ∈ 𝒫_T with L(δ) ≠ 0, which exist since δ ≠ ½). So "Markov ∀T" alone is not a sign
property; it becomes rigid only jointly with entireness.

**Remark 3.4 (on-line additions too).** Lemma 3.2 does not distinguish on-line from off-line added zeros: adding a pair ½ ± iγ (which keeps
every form ≥ itself) also breaks Markov at large T (P = 2cos γu). So "Markov ∀T" is not a positivity mechanism; it is a **rigidity of the
a.c. part of the kernel**: ζ's window kernel has no absolutely continuous component beyond the Γ-Lévy density. This is the "purity of the
arithmetic side" that CA_H_002 Cor 2.3 named as the only property O7 destroys, now stated as an operator property of the form.

## 4. Lemma 4 (sign-change lower bound, seed I2; PROVED, class-generic)
h* (indeed every nonzero F ∈ 𝒫_T) has at least two sign changes in I_T.
*Proof.* span{e^{t/2}, e^{−t/2}} is a Chebyshev system on ℝ (a nonzero combination has at most one zero). F ≥ 0 contradicts ∫Fe^{t/2} = 0. If F
changes sign exactly once, at s, then F(t)sinh((t − s)/2) has constant sign and is ≢ 0, but sinh((t−s)/2) ∈ span, so its integral against F is 0. ∎
An upper bound (nonlocal Courant theorem for the codimension-2 problem) is OPEN; it would be a property of every Markov form (Thm 2 class) and
a finite pattern observable of h* (W-pat). Not pursued.

## 5. Proposition 5 (rearrangement and polarization are inadmissible, seed I3; PROVED)
(a) The arch term of (0.1) decreases under symmetric-decreasing rearrangement of |F| (ν symmetric decreasing; Almgren–Lieb 1989, CITED).
(b) No inequality holds for the comb term: F = bumps at x₀ and x₀ + log n has c_F(log n) > 0 while its rearrangement (one bump of width < log n)
has c_{F*}(log n) = 0, and the reverse configurations give the opposite sign.
(c) 𝒫_T contains no nonnegative function, so F ↦ |F|* leaves 𝒫_T; two-point polarization about any c ∈ I_T does not preserve ∫Fe^{t/2} (the weight is
not reflection-symmetric about c) and preserves ∫F(e^{t/2}+e^{−t/2}) only for c = 0, where it fails for the odd weight.
Hence rearrangement acts only on the archimedean half and leaves the admissible space: additive-only, comb-blind (H0(b)); DISCARD.

## 6. The characterization (Corollary 6; PROVED from Thm 3 + CA_H_002 Thm 2.2; REF-D as a route)
Let 𝖯⋆ := {(S⁺) of CA_H_002; comb density Σ_{n≤x}a(n) ~ x (pole residue); ξ̃ entire of order 1 with FE and Γ_ℝ at conductor 1; window form
Markov for every T}. Within the single-step orbit of ζ's form under O1–O12, O15, 𝖯⋆ holds only for ζ:
(S⁺) excludes O1, O2, O3, O5, O6, O8, O10, O11, O12, O15 (CA_H_002 Thm 2.2); the residue excludes O4 (c ≠ 1); Theorem 3 excludes O7 and every
entire O9; entireness excludes the non-entire O9 (Remark 3.3). O13 is not a modification of the form object; **O14 (symbol truncation): OPEN**
(ARGUED non-Markov: min(σ_T, η) is bounded, so the Lévy singularity ν ~ 1/u is removed and the off-diagonal kernel of the truncated form is the
Fourier transform of a bounded symbol, generally of both signs; not proved).
**Status.** 𝖯⋆ is the first property set of the campaign not closed under any declared single modification (except the OPEN O14). It is a
**separation**, not an inequality: the statement "𝖯⋆ ⇒ λ_A ≥ 0" has, inside the declared universe, ζ as its only instance, so as a route it is the
target (REF-D). PRINCIPIO RECTOR: (S⁺) is +/·-genuine (Erdős), but Markov ∀T is a conjunction of a monoid-only half (Λ ≥ 0) and an
additive/analytic half (a.c. kernel = ν), so 𝖯⋆ uses + and · side by side, not in interaction, at the place where a sign step would sit.

## 7. Pre-screen of the survivor after development
| item | Idx | (R) | P1–P6 | O | B′/B″ | FE-gen | G0/G1 | H-anat | REF-D | [crit] | PR |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Thm 1, Prop 1.1–1.2 | P60-1, CA_B_008 | (3) linear cone | P2 ✗ | all positive-comb O survive | — | — | G1 (Λ≥0) | monoid half | — | — | no |
| Thm 2 | new NO-GO | — | — | O2 kills 𝒦_M | — | — | — | — | — | — | — |
| Thm 3 | new | (10)(11) separation only | P3 ✓ P5 ✓ | separates O7, O9 | not B″ | ? | — | a.c. kernel rigidity | — | — | no (purity) |
| Cor 6 | new | (1)(10)(11) met as separation | P2 ✗ (no inequality) | all but O13/O14 | — | — | — | — | **yes** | — | side by side |

## 8. Self-review
1. *Is (0.1) P46's form?* The Lévy representation of m is CITED from phase 60 (with its κ); only the sign of ν and its decay to 0 are used, so κ and
   the exact constant m(0) are irrelevant. The polar term is absent on 𝒫_T but present on L²(I_T); Thm 1 is about the form on L²(I_T) without the
   polar term. If P46's form on L²(I_T) includes the rank-2 polar term, it adds −|∫Fe^{t/2}|·|∫Fe^{−t/2}|-type terms with positive kernel
   e^{(t+s)/2}...: its off-diagonal kernel is a positive rank-2 kernel and would break Beurling–Deny. Hence Thm 1 is stated for the form **without**
   the polar term, which agrees with 𝔞_T on 𝒫_T (and Prop 1.1 treats the constraint separately). MAJOR caveat recorded, not an error.
2. *Thm 3 uses ξ(σ) > 0 on ℝ.* This is zero information of the most classical kind (no real zeros); it is used only to exclude net real poles of E,
   i.e. inside the separation of falsifiers, never at a sign step. (R)(4) is not engaged at a sign step because there is none.
3. *Is Thm 3 trivial?* It is elementary, but it is the first statement that turns "purity" into an operator property checkable on the form,
   and it shows exactly why O7 survives every comb property yet fails a form property. It does not touch ζ's sign.
4. *Thm 2 vs (R)(1).* Thm 2 is the precise reason qualitative PDE theory of positive-comb Markov forms cannot decide: all its tools are
   monotone in positive comb mass, and positive comb mass kills the sign.
5. *Numerics.* None run. No value of λ_A computed.
**Verdict.** I1: Markov/Krein–Rutman route NO-GO (Thm 2); by-product: rigidity Thm 3 and characterization Cor 6 (separation, REF-D as route).
I2, I3, I10: lemmas, DISCARD as routes.
