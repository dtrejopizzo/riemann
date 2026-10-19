# AUDIT_200_SPEC_003: audit of SPEC_SIGN_OBJECT_003 (phase 200, round 3)

Pure mathematics, no new computation.
OPEN / NO-GO / NUMERICAL. **No sign is proved. L′♯ OPEN. Row D OPEN.**

**Read.** SPEC_SIGN_OBJECT_003 (complete), SPEC_002, AUDIT_200_SPEC_002 (P9′, P10), Q2_LADDER_001 (Lemma R, Theorem Q2.1
"PROVED, given Guo L4.4"), K3_GAMMA_001; phase 199: AUDIT_CONSTRAINTS_001 (row 11, row 17), PROOF_L_SHARP_H_001 (class 𝒦_H,
§5–§6), MORI15_EXTREMAL_001; Paper 47: def:ext, lem:ext-mob, rem:ext-killing, prop:ext-gauge, lem:ext-ellbound,
prob:ext-L, prop:ext-consol (eq:ext-starstar), lem:monoT, lem:contT, subsec:ext-pos. Index: README (phase 200 /
SPEC_003 entry), 04_PHASES l.163 (L2_016), l.401 (G8F-157 lem:monoT: REF-D), l.412 (G3E-159 bootstrap in T: DEAD), l.431
(G8E-159 "flow on orbit is identity"), 06_OPEN_RESIDUES l.37 (W-loc), l.50 (L2_016).

---

## 1. Lemma A.1 (radical of outer summation = gauge)

**(a) Verified, with one typo.** The support of F_{h,s} is [e^{−T_h−s}, e^{T_h−s}]; for s ≥ T + T_h the right endpoint is
≤ e^{−T} = 1/λ. Correct. The constant: 𝓕F_{h,s}(0) = 2∫_0^∞F_h(e^s t)dt = 2e^{−s}∫F_h, and ∫F_h = ∫h(x)e^{−x/2}dx; the factor
"4e^{−s}B(h)" should be 2e^{−s}B(h) (or it depends on the convention for B). Irrelevant, since B(h) = 0.

**(b) Verified.** S(v) = Σ_m G(mv) = 0 for v > 1/λ; for u > 1/λ, Σ_n μ(n)S(nu) = Σ_k G(ku)Σ_{n|k}μ(n) = G(u), with finite
sums because G has compact support. There is no convergence issue.

**(c) and the label.** (b) is exactly the closing statement of lem:ext-mob ("two admissible representatives of g differ by an
element of 𝒢_T"), with the hypothesis f|_{[1/λ,λ]} replaced by "Φ_G = 0 on (−T,∞)." (a) is Q2's Lemma R specialized. (c)
is prop:ext-gauge. **Nothing in A.1 is new relative to Paper 47; it is a correct reorganization.**
- The part "Φ_φ belongs to the radical of 𝒲" is not proved in A.1: it comes from Guo L4.4 via prop:ext-gauge. The correct
  label is the one Q2 itself uses: **PROVED, given Guo L4.4 (CITED).**
- (c) only identifies summation images of G with compact, C² support. The closure in r-coordinates is 𝒢̄_T by
  definition. What is not by definition — equality with the full radical — is A.3 and remains OPEN, as the spec says.

**Serious finding (not flagged by the spec).** Gauge radicality is the only **arithmetic** step in the entire quotient:
Φ_φ has Mellin transform ζ(s)𝓜φ(s), and it is radical because 𝒲 is built with the exact Λ, whose radical contains functions with
Mellin transform vanishing at the zeros of ζ (Guo L4.4 = explicit formula). For a different comb (a_P, cΛ, DH) the form
𝒲^{(·)} is different and Φ_φ is **not** in its radical. Consequences:
- 𝒬_μ with 𝒲 descended is already a Λ-exact object.
- The claims in C1 ("a_P shares A.1, A.2, and A.5; only v_n changes") and in C2 are false in their A.2 part. A.1 and A.5 are
  arithmetically blind, but "𝒲 descends to the quotient" is not.
- I correct the falsifier table: a_P fails **already at the descent**, not in (ii).

## 2. Zero-coordinates

**Well defined.** On summation images of φ ∈ 𝒢_T, the Mellin transform ζ𝓜φ vanishes at ρ. Correct, and the integral converges:
Φ_φ decays like e^{3x/2} at −∞ because 𝓕φ = O(ξ^{−2}).
- **Continuity is missing.** The spec defines z_ρ on 𝒬^{sum} = L²(λ,∞)/𝒢̄_T, which is a **closure**. One needs
  r ↦ z_ρ(Zr) to be a continuous functional on L²(λ,∞). Written as ∫r(t)k_ρ(t)dt, with k_ρ(t) = Σ_{n<t/λ}(…), one must check
  k_ρ ∈ L²(λ,∞) for 0 < Re ρ < 1. This is not done.
- **Label: PROVED on the algebraic image {Φ_φ}; on 𝒢̄_T, OPEN** (it is part of A.3).

**"Independent of μ" versus a gauge that depends on T: compatible.** 𝒢_T ⊂ 𝒢_{T′} grows as T decreases, but z_ρ
annihilates **all** the 𝒢_T at once. The identity z_ρ = −ĝ(·) only uses D_μ(ρ) = −1, which holds for every μ. There is one
imprecision: for zeros off the line, "ĝ(γ)" should be read as ĝ evaluated at −i(ρ − ½), a complex number. The spec writes it
as if γ were real.

**Injectivity on ℐ_μ: the argument as written is incomplete.**
- ĝ(ρ) = 0 only requires **simple** zeros of ĝ at the distinct points ρ.
- Riemann–von Mangoldt counts with multiplicity. With the elementary multiplicity bound O(log t), the distinct zeros of
  height ≤ t number ≫ t, and that does **not** exceed the Jensen bound O(t) for exponential type T: the argument does not close.
- A superlinear number of distinct ordinates is needed, for example a positive proportion of simple zeros (Levinson,
  Conrey; CITED) or Selberg's result on distinct zeros.
- **Corrected label: PROVED given RvM + (positive proportion of distinct zeros, CITED).** It is true, but the citation is a
  different one.

**Infinite dimension.** Correct. The functionals g ↦ ĝ(ρ_j) are linearly independent on L²(−T,T) and the core is dense,
so the map core → ℂ^J is surjective and z descends to ℐ_μ. The infinitude of zeros (Hadamard) suffices; Hardy's theorem is
not needed. **PROVED.**

The spec's warning P4 is correct: these coordinates are descriptive, not working ones.

## 3. Bridge ι: 𝒬_μ → 𝒬_{μ/2}

**(b) Verified.** If x ∈ [T′,T) and n ≥ 2, then ne^x ≥ 2λ′ = √2λ > λ. So Φ_f(x) = e^{x/2}f(e^x) = g(x) = 0, hence
f = 0 on [λ′,λ) and f is admissible at T′. Ψ^{(T′)} = Ψ^{(T)} because g = 0 on [−T,−T′]. Correct.

**(a) Needs to be made precise.** In **r-coordinates** the map is **not** the inclusion L²(λ,∞) ⊂ L²(λ′,∞). One has
r_f^{(T′)} = 𝓕f|_{(λ′,∞)} ≠ the zero-extension of 𝓕f|_{(λ,∞)}. The map is an inclusion only in the Ψ̌ variable, where
L²(T,∞) ⊂ L²(T′,∞). The spec says "in Ψ̌-coordinates," but A.2 defines 𝒬 in r-coordinates. One must fix a single
presentation: in r, ι is Z_{T′}^{−1}∘Z_T, which is not an inclusion.

**(d) Is lem:monoT.** For g ∈ core_{T′}, 𝒲[Ψ̌_g] = W_T(g) = W_{T′}(g), which is literally the computation in lem:monoT
(zero extension; the new contacts see 𝔉(log n) = 0). That 𝒲 descends along ι is the definition of a quotient by a radical.
- **PROVED, trivial and not new.** The index already has it in two forms: G8F-157 (lem:monoT as the mechanism for uniformity
  in T: REF-D) and G8E-159 ("flow on orbit is identity"). The spec cites neither G8E-159 nor G3E-159 (bootstrap in T: DEAD).

**Direction μ → μ/2.** This is the right one: it transports the inductive hypothesis (level μ/2) toward level μ along the
old directions, and that requires B.1 (ℓ_{T′} ≥ ℓ_T).

**NO-GO as a source of sign: justified (PROVED).** A map that is the identity on 𝒲 produces no inequalities. But the
residue of Q2 was already closed for the same reason in G8E-159. It is a redundant closure, not a finding.

**B.1.** It is a clean statement, with no Λ and no sign. The heuristic K3.1 is plausible: the prolate deficit grows as the
band shrinks, so ℓ_{T′} ≫ ℓ_T. But the proposed route has a real difficulty. The correction φ ∈ 𝒢_{T′} with support on
[1/λ,1/λ′], of width ≍ 1/λ, has its extended transform at scale λ, and its leakage beyond λ is ≍ ‖φ‖². One must show that
this leakage is ≪ ℓ_{T′}(g), at a super-exponentially small scale. **OPEN, and non-trivial.** It is the best lemma in this
round.

## 4. C1, duplication stability

**(iii) is trivial and the spec did not see it.** ℓ = 2dist²(·,𝒢̄_T) and dist is a seminorm. So
ℓ(g_old + g_new) ≤ 2ℓ(g_old) + 2ℓ(g_new) always, i.e. θ′ = ½ with no angle geometry at all. The only non-trivial point is that
the 𝒲-orthogonal decomposition exists in the form domain. That is ARGUED if W is coercive on core_{T′}, which the
inductive hypothesis gives. Hence **C1 ⟺ (i) B.1 + (ii)**.

**(ii) is L′♯ rewritten (REF-D).**
- ℐ_μ^{new} is isomorphic to core_T/core_{T′}: it is of **infinite dimension**, not "a fixed small codimension." It contains
  everything that touches [T′,T].
- The spec itself predicts that Mori's extremal, g*, lies "almost entirely in ℐ^{new}." Then
  inf_{new}ℛ_μ ≈ κ(μ), and (ii) says κ(μ) ≳ θκ(μ/2).
- That is the target inequality, discretized in steps of ½log2. Induction over levels reduces nothing: it transfers all the
  content to (ii).

**Class 𝒦_H / restriction 11.**
- C1 is not a differential inequality at the minimizer; it is its discrete version (continuation in T with a finite step).
- Restriction 11 (SOFT) allows a flow-based proof only if it proves (H), the necessary-and-sufficient closure condition.
- The analogue of (H) here is exactly (ii). C1 falls **at the boundary of 𝒦_H**, alongside G3E-159 (bootstrap in T, DEAD) and
  INV_U §3 ("λ·w(T) non-decreasing is a restatement").
- It is not a literal retry, because it changes the norm: ℓ instead of ‖·‖². But the method class is the same.

**New reasons versus L2_016 and W-loc.**
- Versus L2_016: the reason is **real for the map**, because the Tate moments are taken on the quotient (A(Ψ̌) = 0). It is
  not real for the inductive step: there, L2_016 is not the relevant precedent; G3E-159 and G8E-159 are.
- Versus W-loc: **real**, because C1 does not localize in x. But the analogous risk exists in μ: the new directions are
  concentrated near the edges ±[T′,T], which is precisely the "edge channel" of restriction 19. Any proof of (ii) will have
  to control the edge channel, which is dominant at μ = 15 (51–78%, NUMERICAL).

**Square/count or bound?** As stated, (ii) is a **coercivity bound**: ratio ≥ θκ(μ/2), not a square. The
claim "the output is a square: ℓ = 2dist²" confuses the **denominator** (which is indeed a square) with the **sign** of 𝒲,
which is not. The only new arithmetic input is the v_p, p ∈ [μ/2,μ), which sum to ≍ √μ by Chebyshev.
- Any proof of (ii) using only the aggregate Σ_{p∈[μ/2,μ)}v_p, or primes in a short interval, is TV-robust and falls into
  the exhausted tool (cor:void, "PNT-type error terms," phase-200 README).
- For (ii) to be a square or an exact count one would need to exhibit an identity 𝒲|_{new} = ‖A·‖² + (counting term)
  with A explicit. The spec does not propose one.
- **Verdict C1: DOUBTFUL.** Component (i) = B.1 is VIABLE as a lemma. Component (ii) is REF-D.

## 5. C2, C3, C3′

**C2: NO-GO, and stronger than "partial."**
1. Blindness to a_P is correct: D_μ = ζM_μ − 1 does not contain v_n. But the correct argument is the one in §1: for a_P
   the form 𝒲^{a_P} does not descend to the same quotient, and the comparison n₋ ≤ 𝔦 does not have the same object on both
   sides.
2. The right-hand side is not 0. The 1-points of ζM_μ on Re s > ½ (equivalently, the zeros of the Dirichlet series
   Σ_{N≥μ}c_N N^{−s} in the region of absolute convergence σ > 1) have positive density by height. This is Bohr–Jessen
   theory, and row 82 of the index already has it.
   - 𝔦_μ(H) ≍ H, so "lim sup[𝔦 − 𝔦^{model}]" depends entirely on the choice of model.
   - Jessen–Tornehave requires absolute convergence. For ½ < σ ≤ 1 one only has mean square.
   - The "prediction 𝔦_15 − 𝔦^{model} ≥ 0" has no content.
3. The spec admits that the mollifier enters the symbol, and R-Q2 forbids it.
- **NO-GO (PROVED on points 1–2, modulo Bohr–Jessen CITED).** Record alongside P37-2 and row 82.

**C3 (pieces 𝔇, 𝔅): NO-GO.** The spec acknowledges this, and the problem is worse than stated. For fixed y, Ψ_rug(y) is a
finite sum, but Σ N^{−½} over N rough in [e^{y−T}, e^{y+T}] grows like e^{y/2}/log. Ψ_rug does not have the decay e^{−3y/2}
required by def:ext, so **𝒲[Ψ_rug] is not defined**. The equality of classes [Ψ̌_g] = [Ψ_rug] (Q2.1(4)) only holds in the
regularized sense of Q2. The statement "𝔇 − 𝔅 = 𝒲[Ψ_rug] = W_T(g)" has no literal meaning.

**C3′: DOUBTFUL, leaning NO-GO.**
- The difference of rough representatives between μ/2 and μ, ζ_{≥μ/2}(1 − Π_{p∈[μ/2,μ)}(1 − p^{−s})), inherits the divergence.
- The target inequality, Σ_p v_p·#(…) ≤ (1−θ)·diag, is a **bound on counting primes in [μ/2,μ)**, i.e. the
  exhausted wall.
- Versus a_P: erasing primes **decreases** the left-hand side, so the inequality becomes easier while the
  conclusion fails. Hence C3′ **cannot** imply (ii) without another Λ-exact input, which would have to be the radicality
  of the gauge (§1).
- Consistency with Q2.1(b) at μ = 15 (block −[11|M] − [13|M]) is correct arithmetic and proves nothing.

## 6. Proposed restrictions

- **R-Q3 (radical of summation = gauge).** Valid, **given Guo L4.4**. Not new: lem:ext-mob + prop:ext-gauge; row 17
  of AUDIT_CONSTRAINTS ("gauge fixed before comparing") is its hygiene version. The clause "no other natural norm
  without justifying A.3" is arbitrary: a norm need not come from the radical. Accept it **reformulated**: "every quotient
  structure on the outer datum by summation images is prop:ext-gauge; its induced norm is ℓ." Category: HARD
  (hygiene).
- **R-Q4 (𝒲-isometric bridge).** Valid, but it is lem:monoT on the outside and is already in the index (G8F-157, G8E-159).
  Accept as a **consolidated duplicate** with cross-reference, not as a new restriction. A useful corollary worth
  recording: "every induction in μ has its entire content in ℓ_{T′}/ℓ_T and in the new directions." It is row 11,
  discrete version.
- **R-Q5 (no exact alignments in Ψ_rug).** True (PROVED, one line) but nearly empty. 𝒲 reads autocorrelations at
  scale 2T, not exact alignments, and Ψ_rug is outside the domain of 𝒲. Category MISLABELLED: it is a fact, not an
  exclusion. Record as an observation.
- **New restriction I propose, R-Q6 (PROVED, given Guo L4.4).** The descent of 𝒲 to the quotient by 𝒢̄_T uses the exact Λ.
  No falsifier (a_P, cΛ with c ≠ 1, DH) "shares the quotient while only changing v_n." Falsifier tables in future
  specs must flag the failure at the descent, not at the final step.

## 7. Verdicts, ranking, and what to change

| candidate | verdict | reason |
|---|---|---|
| B.1 (Λ-free lemma) | **VIABLE** (as a lemma, not as a sign candidate) | exact, falsifiable statement, no Λ; real difficulty in the leakage of the width-1/λ correction |
| C1 (i)+(iii) | (iii) **PROVED trivial**, θ′ = ½; (i) = B.1 | §4 |
| C1 (ii) | **DOUBTFUL → REF-D** | L′♯ on an infinite-dimensional subspace containing the extremal; boundary of 𝒦_H; output = bound |
| C3′ | **DOUBTFUL / near NO-GO** | counting primes in [μ/2,μ) (exhausted wall); a_P makes it easier; divergence |
| C3 | **NO-GO** (PROVED) | Ψ_rug outside the domain of 𝒲 |
| C2 | **NO-GO** (PROVED mod Bohr–Jessen) | blind to v_n; 𝔦_μ(H) ≍ H; mollifier in the symbol (R-Q2) |

Own ranking: B.1 > C1(ii), only as a control statement > C3′ > C2 = C3.

**I reject all three candidates as a "sign object."** What needs to change:

1. **Acknowledge the state.** 𝒬_μ with 𝒲 and norm ℓ is prob:ext-L in the form of prop:ext-consol (eq:ext-starstar), letter
   for letter. P9′ + P10 led the spec to re-derive Paper 47's setup. The "sign object" no longer has room to be a space or
   a quotient: both are already given.
2. **What remains for it to be (concretely).** A **factorization operator** A_μ: ℐ_μ → ℋ, with ℋ a Hilbert space, built using
   (ℕ,+,·) at m ≈ kn (the semiring principle), and an exact identity
   𝒲[r] = ‖A_μ r‖²_ℋ − ℰ_μ[r], with ℰ_μ ≥ 0 explicit or of finite rank.
   - With that, coercivity ‖A_μ r‖² ≥ cμ^{−A}dist²(r,𝒢̄_T) becomes a problem **without Λ** (prolates), of the same type as B.1.
   - The anti-tautology requirement is that A_μ not be the abstract square root of 𝒲, but instead be given by a formula
     (integer coefficients, combs, Möbius) **before** knowing that 𝒲 ≥ 0.
   - The falsifier test is applied at the descent (R-Q6): A_μ must stop existing, or ℰ_μ stop being ≥ 0, for a_P and for c = 2.
3. **Procedure.** Launch B.1 now, since it is useful for any induction and for the geometry of the quotient. In parallel,
   specify the class of admissible A_μ (spec round 4) and state in writing its difference from G7E-R160 ("every monotone
   functional is generic/archimedean/explicit-formula") and from the Sonin/Gram factorizations already closed
   (phase 183; GRAM_INERTIA_001).
4. **Label corrections in SPEC_003:**
   - A.1 → "PROVED, given Guo L4.4";
   - constant 4 → 2 in A.1(a);
   - injectivity → "given a positive proportion of distinct zeros (CITED)";
   - z_ρ on 𝒢̄_T → OPEN (continuity);
   - A.5(a) → specify the presentation (r or Ψ̌);
   - A.5(d) → "= lem:monoT";
   - C1/C2 falsifier table → failure at the descent;
   - C1(iii) → trivial with θ′ = ½;
   - C2 → full NO-GO.

**For the index (same session):** C2 NO-GO (Bohr–Jessen, blindness to v_n); C3 NO-GO (domain); C1(ii) REF-D at the boundary
of 𝒦_H / G3E-159; R-Q4 = duplicate of G8E-159; R-Q6 new.

---

## Summary (≤250 words)

SPEC_003 is correct in its elementary parts, but almost nothing is new. **A.1** is lem:ext-mob + prop:ext-gauge, and the
radicality depends on Guo L4.4; label "PROVED given Guo L4.4." Typo: 4→2.
- **Zero-coordinates.** Well defined on the algebraic images. Continuity on 𝒢̄_T is missing. Injectivity, as
  written, does not close with RvM alone: it needs a positive proportion of distinct zeros (CITED). Infinite dimension
  PROVED. "Independent of μ" is compatible with 𝒢_T depending on T.
- **Bridge A.5.** Correct, and it is lem:monoT on the outside. Already in the index (G8F-157, G8E-159). The NO-GO as a
  source of sign is justified but redundant. In r-coordinates it is not an inclusion.
- **Finding.** The descent of 𝒲 to the quotient already uses the exact Λ, so falsifiers fail there, not at (ii).
  New restriction R-Q6.
- **C1.** (iii) is trivial (seminorm, θ′ = ½). (ii) is L′♯ on an infinite-dimensional subspace containing the
  extremal: REF-D, at the boundary of 𝒦_H/G3E-159. Its output is a bound, not a square. DOUBTFUL.
- **B.1.** VIABLE as a Λ-free lemma; launch it.
- **C2.** Full NO-GO: blind to v_n, 𝔦_μ(H) ≍ H by Bohr–Jessen.
- **C3.** NO-GO: Ψ_rug is outside the domain of 𝒲. **C3′** is near NO-GO: it is counting primes in a short interval, and
  a_P makes it easier.
- **Restrictions.** R-Q3 valid, not new. R-Q4 duplicate. R-Q5 nearly empty fact.
- **Proposal.** The quotient is prob:ext-L/eq:ext-starstar. The "sign object" can now only be an explicit factorization
  operator A_μ, built on (ℕ,+,·), with 𝒲 = ‖A_μ·‖² − ℰ_μ and ℰ_μ ≥ 0 explicit. The remaining coercivity is then
  a prolate problem without Λ, like B.1.

L′♯ OPEN. Row D OPEN.
