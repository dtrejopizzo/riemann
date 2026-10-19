# CA_B_007 — What O7/O8 do to WP_T; the convex-decomposition inner set (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed; no sign contact.**

## 1. What the quartet and self-dual modifications do (checked against P47's own statements)
**Labels.** In P47 the quartets are **O7** (lem:shape-quartet, def:quartetmodel, prop:quartetmodel). **O8** is the self-dual deformation
f_t = ζ + tg (lem:shape-ft). "O8 quartets" in the round-3 brief is O7. I record both.
Measure-comb setting (P47 uses it in thm:atomic): a comb is a real measure ν on (0,2T). Its window form is
𝔞^ν_T(F) = C_0 + Lev(c_F) − ⟨ν, c_F⟩, and 𝒱_T^{meas} := {ν : inf_F 𝔞^ν_T(F) ≥ 0}. ζ corresponds to ν_ζ := Σ_n v_n δ_{log n}.
**Proposition 1 (PROVED, from P47).**
(a) O7: by prop:quartetmodel(ii), 𝔞^{z,k}_T(F) = C_0 + Lev(c_F) − Σ v_n c_F(log n) + k∫c_Fβ_z. The archimedean part is unchanged
    (same m, no polar term on P_T), and the arithmetic side becomes ν_ζ − kβ_z with β_z absolutely continuous (lem:shape-quartet).
    So **O7 does not move the set 𝒱_T^{meas}; it moves the point** ν_ζ ↦ ν_ζ − kβ_z, off the atomic coordinates.
(b) O8: f_t keeps Riemann's FE with the archimedean factor and pole of ζ, and keeps Λ(n) for n < λ_1 (lem:shape-ft). Its arithmetic side
    is a comb with atoms at non-integer frequencies beyond λ_1. **Again the set is fixed and the point moves**, now along atoms off log ℕ.
(c) Hence, in measure-comb space, the modifications that keep the archimedean factor (O1–O8) all act as **point moves inside one fixed
    convex set**. They differ only in where the point goes: deletions and scalings on log ℕ (O1–O6), continuous parts (O7), atoms off
    log ℕ (O8). "O7 keeps the comb exactly" (thm:shape (a)) means it keeps the atomic part on log ℕ.
**Correction to CA_B_006 §6.** The "pairs (form, v)" are unnecessary. With combs as measures, Lemma B holds verbatim in total-variation
norm: |⟨ν − ν', c_F⟩| ≤ ‖ν − ν'‖_{TV} since |c_F| ≤ 1. Positivity therefore holds on the TV-ball of radius λ_A(T) around ν_ζ (PROVED). That
ball contains non-atomic measures, so "atomic on log ℕ" is again a point property (Lemma B(iv)). For large k, ν_ζ − kβ_z leaves the ball.
Consistent with thm:wit-model(ii),(iii).

## 2. Convex-decomposition inner set — pre-screen (all items PROVED unless labelled)
Proposal: write ν_ζ = Σ_i θ_iν^{(i)} with θ_i > 0, Σθ_i = 1, and each ν^{(i)} ∈ 𝒱_T^{meas} certified by a form-reading argument.
| screen | outcome |
|---|---|
| existence | 𝒱 is convex (prop:finite(ii)). A decomposition exists ⟺ ν_ζ ∈ 𝒱 (take θ = 1). As an existence statement it is the target: REF-D |
| N_012 (segment λ_t = (1−t)ρ_κ + tΛ) | a two-point decomposition with ν^{(1)} = ρ_κ forces ν^{(2)} = (ν_ζ − θρ_κ)/(1−θ) = λ_{t'} with t' = 1/(1−θ) > 1. So it needs the segment **beyond** Λ to lie in 𝒱: t*(T) > 1 along the extended line. That is stronger than N_012's t*(T) = 1, which is the target. It holds iff Λ is interior along that line, with t' − 1 ≲ λ_A/(L_T‖ν_ζ − ρ_κ‖) |
| thm:ceiling (density of log ℕ ≤ 1 < κ*) | if every ν^{(i)} is a nonnegative atomic comb on log ℕ in 𝒱 for all T, then each has density r_i ≤ 1, and Σθ_ir_i = 1 (PNT for ν_ζ) forces r_i = 1 for all i. Every piece then sits at the ceiling, exactly as hard as ν_ζ. Any slack must come from mass off log ℕ (continuous ρ_κ, density κ > κ* > 1). That mass must be cancelled by pieces with negative or non-atomic parts, and those pieces lie on the far side of ν_ζ (row above) |
| prop:summable | pieces with Σv < ∞ have λ_A < 0 for large T, so they are excluded as uniform-in-T pieces. Uniformity in T must come from non-summable pieces (ceiling row) |
| class (D) / lem:shape-lin | the deduction is b(ν_ζ) ≥ Σθ_i b(ν^{(i)}) ≥ 0 (concavity of b, then the certified pieces). The identity ν_ζ = Σθ_iν^{(i)} is linear in ν, so Λ is used linearly unless some piece's certificate is non-linear in Λ. **cor:shape(a)**: a linear use is a measure identity plus Bochner, i.e. class (D). The piece containing Λ's fluctuation must be certified non-linearly, which moves the whole problem into that piece: REF-D |
Verdict: **EXCLUDED.** The convex decomposition is the target (existence), or the target with margin along a line (N_012 extended), or class
(D) (certified pieces). thm:ceiling shows the pieces cannot gain anything on log ℕ. **YES→NO:** "explicit convex inner set as sign carrier" → NO.

## 3. What is left over: the concavity gap (new object, definition + one PROVED fact)
Because b is concave, b(Σθ_iν^{(i)}) − Σθ_ib(ν^{(i)}) =: Γ(θ, ν^{(·)}) ≥ 0. This is the one place where a convex decomposition is
**non-linear**. Proposition 2 (PROVED): for two pieces with simple bottoms and minimizers h_1, h_2, Γ = 0 iff some unit F minimizes both
𝔞^{ν^{(1)}} and 𝔞^{ν^{(2)}}. In general Γ ≥ θ_1θ_2·(bounded-below quadratic in the misalignment of minimizers) — the lower bound is ARGUED (second-order
perturbation, spectral gap needed). Proof of "iff": the infimum of the sum is attained (compact resolvent, prop:quartetmodel(iii)-type);
equality in inf(A+B) ≥ inf A + inf B holds iff a common minimizer exists. ∎
Reading. Take ν^{(1)} = ρ_κ (b ≥ η_κ, minimizer spread over all frequencies) and ν^{(2)} = λ_{t'} with t' > 1 (minimizer concentrated on
the near-coincidence packets of the window). Then b(ν_ζ) ≥ θη_κ + (1−θ)b(λ_{t'}) + Γ. The sign could come from Γ, the **misalignment
between the archimedean minimizer and the near-coincidence minimizer**. This acts on the correlation with the window minimizer (seed),
and Λ enters non-linearly (through the minimizer of λ_{t'}). Not pre-screened yet against (R)(4)–(8) and the O-list. In particular O7
moves ν^{(2)} by −kβ_z/(1−θ), which may realign the minimizers; that is the first test.

## 4. Self-review
- Prop 1: the archimedean factor is kept by O7 (prop:quartetmodel(ii): "archimedean term m, no polar term") ✓ and by O8 (lem:shape-ft) ✓.
  Treating the O8 arithmetic side as a measure on (0,2T) uses the explicit formula for f_t, whose atoms P47 describes as "frequencies m/√M".
  Their exact weights are not reproduced here: ARGUED for O8, PROVED for O7.
- §2 ceiling row: thm:ceiling is a statement for combs positive at every T. A T-dependent decomposition escapes it at a fixed T. Then
  uniformity in T is again the issue (prop:summable row). ✓ stated.
- §2 is a sequence of reductions to recorded objects (REF-D, N_012, D). No new exclusion theorem is claimed beyond "the decomposition
  is linear".
- §3: the "iff" is standard. The quantitative lower bound is ARGUED, and Γ ≤ b(ν_ζ) − Σθb(ν^{(i)}) is an identity, not an estimate. Γ could
  be REF-D in disguise (Γ = b(ν_ζ) − known terms). It escapes only if Γ is bounded below **without computing b(ν_ζ)**, e.g. from
  misalignment of two explicitly computable minimizers. Flagged as the decisive question.
