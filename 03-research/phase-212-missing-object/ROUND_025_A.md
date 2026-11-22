# ROUND_025_A — Cross-check of antecedents: "existence + rigidity" scheme (WF)/(R)/(E) against Paper 46 and phases 153–160, 197

Labels: PROVED / CITED / CONDITIONAL / OPEN / NO-GO. Review of novelty and logic; nothing new is derived.

## 0. What was opened
- Paper 46 (`04-papers/46-row-d-dual-certificates/main.tex`): def:PD (l.668), def:W and thm:Z (l.1224–1300),
  prop:finite (l.3156–3180), rem:regimes, lem:cpos, thm:finmod (l.3228–3258), rem:resweights (l.3260–3292),
  lem:degen (l.3294–3313), prop:finsupp (l.3316–3334), cor:void (l.3336–3362), rem:twohalves (l.3364–3378).
- `phase-155-.../R155_053_ROUND8B_P6_ALIGNMENT.md` §1 (Prop 1.1, 1.3); README row R155_053.
- `phase-197-barrier-theorem/BARRIER_Y_001_...md` (complete; 102 lines).
- `phase-159-.../G2_B9_R3.md` §3 (Theorems N, R′, Cor R1′, Rem 3.1–3.4), §4.
- `phase-160-row-d-infinite-T/R160_M2_R1.md` §0, §2 (T1, T8), §4 (Thm 4.1–4.3), §6 (Prop 6.1), §7.
- Master index: l.5205–5211, 4733, 4778, 12192.
- Not opened in full: phases 153–154 beyond the grep (only Lagrange multipliers of the Tate constraint and β₀=2, which are
  something else); thm:TK/prop:TK, Theorem X, prop:nearfree, rem:bar-arith, prop:spec of the paper (grep
  unrelated to a free weight on the comb). G2_B6_R5 (Prop C) not opened.

## 1. Fixed or free weight in the paper?
- The certificate LP (def:PD, l.668; thm:Z, l.1240) has the comb **fixed** at v: "Fix T and the weights v"
  (l.665). The "weight" w of def:W/thm:Z is a flat-top weight on the **test side** (w≡1 on [−2T,2T]), not a weight of the
  comb; Theorem Z/TK do not vary the comb.
- The **free** comb appears in §"A fixed window is a finite condition": prop:finite(ii) (l.3159–3163) defines
  𝒱_T = {v ∈ ℝ^{N_T}: 𝔞^{(v)}_T ≥ 0 on P_T}, closed and convex, as an intersection of half-spaces — it is exactly
  the K_T of the proposal. lem:degen (l.3294–3302) introduces concave μ_T(v) and the case "minimizer with c_F(log n)=0
  ∀n ∈ N_T" ⟹ v_T(Λ) maximizes μ_T. R155_053 Prop 1.1/1.3: the arithmetic content is the uniformity in T of v_T ∈ 𝒟_T.

## 2. (WF) — weight-free statement
**It is there, under another name.** R160_M2_R1:
- D5 (l.110–113): "prime-blind" test if c_F(log n)=0 ∀n ∈ N_T; Z^A_T (pure) and Z^prim_T (relaxed, mixed states /
  positive-definite autocorrelations) = infimum of the archimedean energy over prime-blind tests.
- Thm 4.1 (l.240–256, PROVED): strong duality max_v V^prim_T(v) = Z^prim_T, with 𝒪^prim_T = ∂g_T(0): "the best possible
  comb at window T is the Lagrange multiplier of a problem in which the primes enter only through their positions"
  (l.259–260). It is the phrase "v as Lagrange multiplier" of the proposal.
- Thm 4.3(a) (l.272, PROVED): 𝒱_T ≠ ∅ ⟺ V*_T ≥ 0; 𝒱^prim_T ≠ ∅ ⟺ Z^prim_T ≥ 0. This is (WF) (mixed version = prim).
  Thm 4.2 sandwich Z^prim_T ≤ V*_T ≤ Z^A_T: for pure states there is only an inequality; the proposal must use the
  relaxed version to have exact Farkas (the corpus does it this way; the pure version is not an exact dual).
- §7.1 (l.398–402): (PBP_T) "prime-blind positivity" recorded as OPEN for T > log 2 (pure) and T > 0.8 (relaxed).
- Index l.5209 / l.12192: "Concave value function V_T / variational characterization of Λ" → **DEAD [F3: Λχ₂]**:
  𝒱_T, V*_T, Z^A_T, Z^prim_T are blind to the primes (Rem 4.6, l.304–305: Λχ₂ shares 𝒱_T with ζ and fails).
- BARRIER_Y_001 is Farkas for another class (majorization cone {0,1}); it is not (WF).

## 3. (R) — rigidity
**It is there.** G2_B9_R3 Theorem R′ (l.204–219, PROVED, unconditional): for b ∈ 𝒯_meas∖{0} (includes b ∈ ℓ¹_w, Σ|b_n|n^{−1/2}<∞),
Λ+b is not ∀T-positive (primitive and complete); the ∀T-positive set in Λ+𝒯_meas is {Λ} or ∅ (Thm N(iii), l.181).
The proof uses D_b(τ)=Σ b_n n^{−1/2}·2cos(τ log n) and sup D_b > 0 by almost-periodic mean (l.218–219): the same
mechanism "Dirichlet polynomial without constant term ≤ 0 ⟹ zero" as in the sketch. Rem 3.3 (l.243–249): empty interior
in every summable direction. Index l.5210, l.4778.
Difference: the proposal states (R) for **every** real w; the corpus only for w − v ∈ 𝒯_meas. The proposal's sketch
does not cover more either: for non-summable d, D(τ) is not defined as an almost-periodic function, and radical vectors with
small a^v do not control Σ d_n c_X(log n) when d grows. **That gap is exactly step (iii) of the corpus.**

## 4. (E) — gluing existence ⟹ sign
**It is there.** R160_M2_R1 Prop 6.1 (l.359–367, PROVED as an implication): if (i) Z^prim_T ≥ 0 ∀T [= K_T ≠ ∅ ∀T], (ii) a
selection of multipliers v*_T converges coordinatewise to a comb a*, (iii) a* − Λ ∈ 𝒯, then
∀T positivity of a*, and a* = Λ if a* − Λ ∈ 𝒯_meas. T1 (l.16): 𝒱_T compact; T8 (l.24, Prop 2.4): the restriction
π^{T′}_T maps 𝒱_{T′} into 𝒱_T — the "inverse limit" of the proposal.
Only technical piece that the proposal improves: (ii). The corpus asks for a convergent selection and declares the uniform
bound OPEN (§7.6, l.412). The proposal uses the inverse limit of nonempty compacts (π^{T′}_T(K_{T′}) nested), which gives a
∀T-positive w **without** a uniform bound. It is correct and removes (ii), but it is a standard compactness detail.

## 5. Why it did not close at the source
- R160_M2_R1 §6 (l.369–376): "(iii) is where the whole of the arithmetic sits: Λ ∉ 𝒯 (mass ≍ √X) … the proposition
  relocates the sign into (iii) without weakening it"; "shape, not a mechanism". §7.7 (l.414–415): the exact location of the wall.
- G2_B9_R3 Rem 3.2 (l.238–241): R′ "fixes the candidate but does not decide its membership": the existence of a ∀T-positive element
  is the whole content [H].
- Falsifier Λχ₂ (Rem 4.6): K_T is blind to the primes; (WF) is identical for Λ and Λχ₂. It does not refute (E) logically
  (the w produced need not be Λχ₂), but it confirms that (WF) does not use the exact values of Λ, and that all the
  arithmetic weight passes to the rigidity (R) for arbitrary w, which is (iii) unweakened.
- cor:void / thm:finmod / prop:finsupp of the paper: partial rigidity per window (finite combs fail for large T);
  consistent with (R), they do not extend it.

## 6. Additional logical observations
1. (WF) with mixed states requires closure of the cone (κ_T(ρ), Arch(ρ)); the corpus resolves it with 0 ∈ int dom g_T
   (Thm 4.1 step 2). With pure states there is only a sandwich.
2. Boundedness of K_T: corpus T1 (V_T ≤ C_T − c_T|v|), PROVED; not a problem per window.
3. The comb w obtained by inverse limit is arbitrary (possibly not tempered); without global (R) the scheme does not close.

## 7. Verdict
**REPETITION** (with a minor technical adjustment). (WF) = R160_M2_R1 Thm 4.1/4.3 + (PBP_T); (R) = G2_B9_R3 Thm R′/N on
Λ+𝒯_meas; (E) = R160_M2_R1 Prop 6.1, already qualified at the source as "shape, not mechanism", with the arithmetic in (iii),
and the index entry l.5209 marks it DEAD [F3: Λχ₂]. The only unrecorded thing is replacing (ii) by the inverse limit
of compacts, which does not touch (iii). Reopening requires a proof of (R) for **non**-tempered weights (outside 𝒯),
which is precisely the open step §7.7 of R160_M2_R1; without that mechanism the proposal does not pass the filter.
