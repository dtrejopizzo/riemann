# CA_C_002 — MW-3 (infinite-dimensional Hasse–Minkowski): the classical class, and the only well-posed reading

Phase 193, round 6. Seeds C5 + C6 of CA_C_000. Pen and paper.
**No sign contact. No certified negative value for ζ.**
Index row: MW-3 / NG-C1 "∞-dim Hasse–Minkowski: OPEN gap (no theorem either way); Wall A (zero part does not factor), Wall B (no HM
theorem); condensed variant untried". Goal: a theorem either way, in a declared class, and the identification of what is local and what is
global in the window form.

## 1. The classical class: finite-place data never decide definiteness (PROVED)
**Class 𝓗.** Deductions "q is a quadratic form over ℚ (any rank, possibly an orthogonal sum of finite-rank pieces) whose
ℚ_p-isometry class at every finite p has property 𝖯, and which satisfies the global reciprocity Π_v ε_v(q) = 1; hence q is positive
definite".
**Proposition 1 (PROVED).** No such deduction is valid unless 𝖯 already forces the signature, which is a datum at ∞.
*Proof.* q₊ = ⟨1,1,1,1⟩ and q₋ = ⟨−1,−1,−1,−1⟩ over ℚ. Discriminants: 1 and (−1)⁴ = 1. Hasse–Witt invariants at each p:
ε_p(q₊) = Π_{i<j}(1,1)_p = 1, ε_p(q₋) = (−1,−1)_p⁶ = 1. Over ℚ_p a form is classified by rank, discriminant and Hasse invariant
(CITED, Serre, *A Course in Arithmetic*, Ch. IV, Thm 7), so q₊ ≅ q₋ over every ℚ_p. Both satisfy reciprocity ((−1,−1)_∞⁶ = 1). q₊ is
positive definite and q₋ negative definite. For any form r, q₊ ⊥ r and q₋ ⊥ r have the same local classes at every finite p; take r
positive definite of any rank (finite or a Hilbert orthogonal sum) to obtain the infinite-rank version. By lem:transfer (falsifier q₋ ⊥ r),
no deduction in 𝓗 concludes definiteness. ∎
**Reading.** In Hasse–Minkowski, finite places govern *isotropy and representation*. Definiteness is the condition at the single place ∞.
So "local positivity at every place ⇒ global positivity" has no classical content: positivity has no meaning at a finite place
(ℚ_p is not ordered), and the finite-place data that do exist cannot see the sign. The window form has a second obstruction: its
coefficients (v_n = 2Λ(n)/√n, the integrals defining Arch) are not rational, and the log p are ℚ-linearly independent, so there is no
ℚ-structure in which the prime part is defined over ℚ (ARGUED; not needed for Proposition 1).
**Verdict for 𝓗 (and for its condensed/solid transposition, which changes the category in which ℚ_p-data live but not the fact that the
sign is an ∞-datum): NO-GO, PROVED.**

## 2. The window form is local on the prime side (Wall A is a zero-side statement) (PROVED)
On P_T, 𝔞_T = 𝔞_∞ − Σ_{p<X} 𝔮_{p,T} exactly (CA_C_000, common fact); each 𝔮_{p,T} is indefinite on P_T (P46 cor:Qp) and 𝔞_∞ is indefinite
for T ≥ 0.60 (cor:Tarch). So the summands carry no sign, and the question is what couples them. The "places" here are not ℚ_p-forms; they
are real forms indexed by p. The coupling is visible on the integer lattice of P46 §(one profile).

## 3. Torus against line: the exact local–global decomposition of Problem (S) (PROVED)
Fix the profile F₀ (2T₀ < log 2, ‖F₀‖ = 1), M, and a finite set S of primes. Write e(m) ∈ ℕ^S for the exponent vector of an S-unit m,
and for s supported on S-units ≤ M put P_s(θ) := Σ_m s_m e^{i⟨e(m), θ⟩}, a trigonometric polynomial on 𝕋^S. Let
ι(τ) := (τ log p)_{p∈S} be the **Kronecker line** (the product formula: one archimedean variable τ drives every place, since
log m = ⟨e(m), (log p)_p⟩), dμ_line := (2π)^{−1}F̂₀(τ)²dτ (a probability measure: ∫F̂₀²/2π = ‖F₀‖² = 1), and dθ the Haar probability
on 𝕋^S. Local symbols: δ_p(θ) := 2 log p Re(x/(1−x)), x = p^{−1/2}e^{iθ} (P46 rem:boxes), so δ_p(θ) = Σ_{j≥1} v_{p^j} cos(jθ).

**Proposition 2 (PROVED).** For real s supported on S-units ≤ M:
(a) s^⊤Arch_M s = ∫_ℝ m(τ)|P_s(ι(τ))|² dμ_line(τ);
(b) s^⊤Div_M s = ∫_{𝕋^S} (Σ_{p∈S} δ_p(θ_p)) |P_s(θ)|² dθ  (Haar: independent places);
(c) s^⊤(Div_M + Near_M)s = ∫_ℝ (Σ_{p∈S} δ_p(τ log p)) |P_s(ι(τ))|² dμ_line(τ), provided all prime powers n with near-coincidences
    |log(kn/m)| < 2T₀ are S-units (otherwise add the non-S-unit atoms on the line side, which have no torus counterpart);
(d) hence s^⊤Near_M s = (μ_line∘ι^{−1} − Haar)(Σ_p δ_p · |P_s|²), the **equidistribution defect of the weighted Kronecker line**
    against Haar measure, tested on the local symbols times |P_s|²; and
    s^⊤𝔸_M s = ∫ m |P_s∘ι|² dμ_line − ∫ (Σ_pδ_p)|P_s|² dθ − (μ_line∘ι^{−1} − Haar)((Σ_pδ_p)|P_s|²).
*Proof.* (a) P46 prop:AM(iii): Arch_M(m,k) = (2π)^{−1}∫ m F̂₀² cos(τ log(m/k)), and P_s(ι(τ)) = Σ s_m m^{iτ}. (b) The Fourier coefficient of
δ_p at ±j is v_{p^j}/2; ∫_{𝕋^S} δ_p(θ_p) e^{i⟨e(m)−e(k), θ⟩}dθ = v_{p^j}/2 if e(m) − e(k) = ±j·e_p (j ≥ 1) and 0 otherwise, i.e. iff m/k or
k/m is p^j; summing gives Σ_{k|m, k<m} v_{m/k}s_ms_k = s^⊤Div_Ms (½(V+V^⊤) with V_{mk} = v_{m/k}). (c) prop:AM(ii): the comb part of
s^⊤𝔸_Ms is ∫ Σ_n v_n cos(τ log n)|P_s(ι τ)|² dμ_line, and Σ_{n S-unit prime power} v_n cos(τ log n) = Σ_p δ_p(τ log p); the identity
Div + Near = this comb part is prop:AM(iii). (d) Subtract (b) from (c). For a trigonometric polynomial Q = Σ_k Q̂(k)e^{i⟨k,θ⟩}, the line
integral is Σ_k Q̂(k) c₀(⟨k, log p⟩) and the Haar integral is Q̂(0); the difference sees exactly the k ≠ 0 with |⟨k, log p⟩| < 2T₀, i.e.
the near-coincidences. ∎

**Reading (the HM dictionary).**
- *Local* = Haar measure on 𝕋^S: the places are independent; (b) is the Kronecker sum of rem:boxes, bounded by Σ_p 2log p/(√p − 1).
- *Global coupling* = the Kronecker line ι: the product formula forces all local angles to be τ log p for one τ. The archimedean term
  lives **only** on the line (a). There is no Haar-side archimedean term.
- *Hasse defect* = (d), Near_M: the deviation of the line from Haar at the resolution 2T₀, which is nonzero exactly at near-coincidences
  m ≈ kn. On tests with no visible near-coincidence (resonators, P46 prop:nearfree) the defect vanishes and positivity holds with a margin:
  **this is the "local–global principle that holds"**, and it is already a theorem.
So the only well-posed infinite-dimensional Hasse–Minkowski statement for this form is: *the archimedean line term dominates the local
Haar term plus the equidistribution defect of the line*, uniformly in M. By prop:AM(i) and thm:oneprofile that statement is the target
(Problem (S)). REF-D.

**Screens for Proposition 2 as a mechanism.** (B″): (a)–(d) hold for every comb supported on prime powers with weights in place of
log p p^{−j/2} (✗ as mechanism; ✓ as coordinates). Index: Bohr torus rows NT_003/005 (curve reduction), G2_B7 (Haar-null twist torus),
F41 (log p independence = REF-D), G2_B3 ("twist Haar average = archimedean form") are the same torus; the new content is the identification
Near_M = line − Haar on the box, which makes MW-3's Wall B precise.

## 4. What a "global coupling condition specific to ℚ" would have to be, in this dictionary (ARGUED)
The defect (d) is controlled by the Diophantine geometry of the vector (log p)_{p∈S} at resolution 2T₀: how often ⟨k, log p⟩ ∈ (−2T₀, 2T₀)
with k ∈ ℤ^S, |k| bounded by the box. That is the distribution of ratios m/(kn) near 1 among S-units, i.e. smooth-number statistics,
which are the same for a_P (prime set ≥ P, O6) on S ⊂ {p ≥ P}, and are a property of positions only (O7 keeps it; O11/O15 move it only
statistically). So a coupling condition phrased through the line/torus geometry alone falls under (B″) + O7 (comb-only). What separates ℚ
is the joint datum: Haar side with the standard local symbols **and** line side with m(τ) at conductor 1, *and* S = all primes. That is
CA_C_001 §3 again: complete places, standard local terms, Γ_ℝ, nothing else. No condition strictly weaker than the form itself was
found that survives O2, O6 and O7 simultaneously.

## 5. Self-review
1. *Is Proposition 1 a strawman?* It closes the classical class (finite-place isometry data + reciprocity), which is what "Hasse–Minkowski"
   names. It does not close "local–global" in a broader sense; §3 is that broader sense, and it lands on (S).
2. *Condensed variant.* Replacing ℚ_p-data by solid ℤ_p-modules changes the category, not the place at which the sign lives. The claim
   "NO-GO for the condensed variant" holds only for variants whose input is finite-place data; a condensed object carrying archimedean
   information (liquid ℝ-vector spaces) is not covered. Label for that sub-claim: ARGUED.
3. *Proposition 2(c) hypothesis.* For a box S not containing every prime involved in near-coincidences, extra line atoms appear. The
   statement as written is exact; the general case adds those atoms to (d). No gap.
4. *Is §3 a retry?* The torus is a retry; the exact formula Near_M = (line − Haar)(Σδ_p|P_s|²) on boxes is not stated in P46 (rem:boxes
   bounds Div on boxes; prop:AM defines Near). It is a coordinate (lem:shape-ident applies), not a mechanism.
5. *Does anything here touch the sign?* No.

## 6. Verdict and proposed index change
- MW-3, classical class 𝓗 (finite-place isometry data + reciprocity, and condensed transpositions with finite-place input): **NO-GO, PROVED**
  (Proposition 1; falsifier q₋ ⊥ r).
- Wall A: the prime side of the window form factors exactly over places; non-factorization is a zero-side statement only (PROVED, §2).
- Wall B / the well-posed reading: line-versus-Haar on multiplicative boxes, Proposition 2 (PROVED); its positivity is Problem (S) (REF-D).
- Proposed index text for MW-3: "classical HM class NO-GO (CA_C_002 Prop 1); well-posed local–global reading = (S) via the Kronecker-line /
  Haar decomposition (CA_C_002 Prop 2); residue: none beyond (S)".
