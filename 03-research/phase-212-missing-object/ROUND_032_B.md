# ROUND 032 B — Selection gate: (PBP_T) as a problem of representing measures of the origin on the infinite polydisc

Object: weight-free state of (PBP_T) (ROUND_030_B, 031_A, 031_B). Proposal: lift μ to the torus 𝕋^∞ via the Kronecker
line ι(τ) = (p^{−iτ})_p and read Φ(log n) = 0 (n ≥ 2) as "ν = ι_*μ represents the origin for the polydisc
algebra". Only cross-check, correction and selection; no new derivation.

## 1. Cross-check (sources opened, not by word matching)

**1.1 CA_E_001 (phase 193) §§1–2, Lemma 1 and Theorem 2 (PROVED).** Same operation on the object with the weight:
φ(q) = 𝖡(log q) on G = ℚ_{>0}^× is PD ⟺ target (Lemma 0); the Bochner measure of φ on Ĝ ≅ ∏_p S¹ is ι_*ν,
Radon, concentrated on the Kronecker line (Lemma 1, σ-compactness of ι(ℝ)); every translate of the line is
Haar-null. Concludes: exact reformulation (REF-D, class lem:shape-restate), "valid for every comb", without a sign step.
Eliminates product/Schur factorizations. It did not close because the line is Haar-null: nothing of the torus structure
(independence of places) reaches a measure on the line.

**1.2 CA_C_002 §3, Prop. 2(a)–(d) (PROVED).** Same tool on the form with weight: sᵀ𝔸_M s =
∫ m |P_s∘ι|² dμ_line − ∫(Σ_pδ_p)|P_s|² dθ − (μ_line∘ι^{−1} − Haar)(…). "Local = Haar on 𝕋^S; global coupling = Kronecker
line". Concludes an identity without sign; the Near term is the equidistribution defect of the line.

**1.3 CA_H_002 §3 (Thm. 3.1–3.2, Prop. 3.3–3.4, Cor. 3.5).** Extends 1.2 to the full solenoid: Div = Haar
integral, Div + Near = integral over the line, Near = line − Haar; Kronecker–Weyl as exact limit (§3.4).
Cor. 3.5: the "Kronecker defect" form of the target is REF-D. It did not close: identity linear in Λ, without sign.

**1.4 CA_M_001 Thm. 3.1/Cor. 3.2.** Site arithmetic (p − np′) is "information-free": the conclusion
only uses the PD of the site-free 𝖡; NO-GO for every site-arithmetic route. Relevant to the
"free Beurling" control: there it was already proved that the site side does not distinguish ℕ from a Beurling comb.

**1.5 AUDIT_204_TRACT_F_001 §3 (l.123–125).** Vocabulary only: Bohr lift to H²(𝔻^∞) for the
Báez-Duarte cyclicity question; [H] in its formulation; does not touch the weight-free state or representing measures.

**1.6 NEAR_DOSSIER (212) item 8 and row N_BUILD_022 §4 / L2_BUILD_028 §2(c).** NO-GO PROVED: "on the torus with independent
phases only Div is diagonal; Near and Arch live on the diagonal θ_p = θ log p". It is exactly the point at which
the proposal leaves the arithmetic ("the direction of the line versus m").

**1.7 Montgomery–Vaughan / Hilbert.** ANNEX_211_FILES_7 l.288 and l.464: control of non-resonant pairs by the generalized
Hilbert inequality in the Poisson model; gives a magnitude bound on the off-diagonal term, not a sign.
Index ANNEX_INDEX_04 l.498 "Magnitude bounds RFB/Carleson/sampling" [DEAD]; l.503 "window evaluation finer
than Montgomery–Vaughan" [OPEN] (precisely what would be missing).

**1.8 "Representing measure" in 211.** ROUND_001_D, STATE_001, POWER_REDUCTION_AUDIT_044: another measure (that of B in a
Hamburger/Stieltjes moment problem), NO-GO "blind to the comb". Vocabulary only. "Jensen" in 104/119: Jensen measure
of interior mass, another object. No file formulates Φ(log n) = 0 as "ν represents 0 in A(𝔻^∞)".

**Classification.** Lift + Kronecker line + Haar vs line: same operation already done (1.1–1.3, with weight;
the weight-free version is a special case: setting w = 0 in 𝖡 does not change Lemma 1). Reading "representing measure of the
origin": a new phrase in the corpus, but it is the literal translation of the constraint of the weight-free state (§2).

## 2. Correction of the formulation

(a) **Borel measure.** ι: ℝ → 𝕋^∞ continuous and injective (unique factorization + ℚ-linear independence of the log p);
ι(ℝ) σ-compact ⟹ Borel; ν := ι_*μ is a finite positive Radon measure (CA_E_001 Lemma 1). ∫χ_r dν = ∫ r^{−iτ}dμ = Φ(log r) with the
convention μ̂(x) = ∫e^{−ixτ}dμ. Correct. Normalize ν(𝕋^∞) = Φ(0) = 1.

(b) **Moments.** Φ real and even ⟹ ∫z^a dν = ∫z̄^a dν = 0 for every a ≥ 0, a ≠ 0. That is exactly "ν represents
0 for the polydisc algebra" (equivalently for its closure in C(𝕋^∞)). The mixed moments z^a z̄^b
(a, b of disjoint supports) are Φ(log(n/m)), non-integer quotients: free. Correct.

(c) **Finite window.** Φ = μ̂ is the autocorrelation of F ∈ P_T, with support in [−2T, 2T]. For n ≥ e^{2T},
Φ(log n) = 0 is automatic. The effective constraint is the monomials with n < e^{2T}, finitely many. Therefore, for
finite T, ν does **not** represent the origin by imposition: it does so by the compact support of Φ, which is a property of the
Paley–Wiener class and not of ℕ. Moreover, in one variable (one prime p) only the moments k < 2T/log p are imposed: the
image measure on S¹ is not forced to be Lebesgue at a finite window. "Uniqueness in one variable = optimality of one generator"
holds only in the limit of all moments, not in the window. That statement of the proposal must be corrected.

(d) **Densities of the window on 𝕋^∞.** ν is singular with respect to Haar (concentrated on a Haar-null translate of the
line). The class "μ = |F̂|²dτ/2π with F ∈ P_T" has no intrinsic description on 𝕋^∞: it is the image of a
Paley–Wiener space of the line; the exponential type 2T and the double zeros at ±i/2 are conditions on ℝ, not on the torus.

(e) **The functional.** m(τ) = Re ψ(¼ + iτ/2) − log π grows like log|τ| and is not almost periodic: it is not the restriction to the line
of any continuous function (nor reasonable bounded Borel function) on 𝕋^∞ on which ∫m dν would depend as a functional of ν on the
torus. ∫m dν only makes sense as ∫m dμ on ℝ. The target does not live on the polydisc.

## 3. Available tools and minimal statement

- Theory of representing/Jensen measures of the polydisc (Rudin, *Function theory in polydiscs*): describes the
  convex set of measures on 𝕋^n annihilating analytic moments; its lower bounds are for functionals of the type
  ∫ log|f| dν ≥ log|f(0)| (Jensen), with f analytic on the polydisc. m∘ι^{−1} is not log|f| of any f analytic on
  𝔻^∞ (it would be log|f(p^{−iτ})| on the line: a Dirichlet series); one would have to exhibit f = Σ a_n n^{−s} with
  log|f(½·?+iτ)| ≤ m(τ) on the line and f(0) = a_1 controlled. That is rewriting m as a subharmonic function of a
  Dirichlet series: an object not constructed and not motivated by the proposal.
- Carlson: lim (1/2X)∫_{−X}^{X} |Σa_n n^{−it}|² dt = Σ|a_n|² = line → Haar in the limit: it is CA_H_002 §3.4.
- Montgomery–Vaughan: ∫_{−X}^{X}|Σa_n n^{−it}|² = Σ|a_n|²(2X + O(n/δ_n)): magnitude bound on the defect line − Haar
  = Near; it is 1.7, without sign, and at finite-window scale the error O(n/δ_n) dominates.
- Local embedding of H²(𝔻^∞) (Dirichlet series on intervals): gives ∫_I |f(it)|² ≲ ‖f‖²_{H²}; again magnitude.

**Minimal statement that would have to be proved.** For every μ = |F̂|²dτ/2π, F ∈ P_T, with Φ(log n) = 0 (n < e^{2T}):
∫ m dμ ≥ 0. Expressed on the torus it does not simplify: one needs a bound that uses at once ι (the frequencies log p) and m,
i.e. an estimate of the defect line − Haar with sign against m. It is (PBP_T) identically.

## 4. Four-point filter

1. **Closest antecedent:** CA_E_001 Lemma 1 + CA_H_002 Thm. 3.1/Cor. 3.5 (lift to Ĝ, Kronecker line,
   line − Haar), with the NO-GO of NEAR_DOSSIER item 8 (Arch and Near live on the diagonal θ_p = θ log p).
2. **What is new:** only the label "representing measure of the origin" for the constraint Φ(log n) = 0, and the observation
   that in dimension ≥ 2 the convex set is large. No new inequality.
3. **Does it avoid the antecedent's difficulty?** No. The difficulty of 1.1–1.3 is that the line is Haar-null and that m is not
   a function on the torus; the proposal keeps both (§2(d)–(e)) and moreover the representing condition is, at a finite
   window, a consequence of the support of Φ (§2(c)).
4. **Inequality that would connect with the global sign:** none named. The polydisc tools either bound functionals
   of Jensen type (which m is not) or give magnitudes (Carlson, Montgomery–Vaughan) that already appear as DEAD/OPEN without sign.

**Controls.** Free Beurling system {q_j}: same group ⊕ℤ, same polydisc, same convex set of representing
measures, same m; only ι_q(τ) = (q_j^{−iτ}) changes. Odd integers: a polydisc with one fewer variable, same scheme.
At which named step does the exact direction (log p)_p enter? In none of the polydisc statements: it enters only in
∫m dμ evaluated on ℝ, which is the original problem. CA_M_001 already proved that the site side is "information-free".

## 5. Verdict

**DOES NOT PASS (repetition; moreover without mechanism).** The lift to 𝕋^∞ via the Kronecker line and the line − Haar reading
are done (CA_E_001, CA_C_002, CA_H_002; the weight-free version is a special case). The rereading as a representing measure
of the origin is another language: at a finite window it is a consequence of the support of Φ, the functional m is not definable on the torus,
and no polydisc tool uses the direction (log p)_p. Correction recorded: at window T one-variable uniqueness
does not apply (only the moments k < 2T/log p are imposed).
Reopening only with an explicit analytic f on 𝔻^∞ (Dirichlet series) such that log|f∘ι| ≤ m on the line with f(0)
controlled, or with a signed bound of the defect line − Haar against m; the proposal provides neither.
