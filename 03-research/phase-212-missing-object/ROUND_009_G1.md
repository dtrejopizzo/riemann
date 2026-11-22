# Round 9, item G1 — object with inverted roles: arithmetic as the source of the sign

Phase notation: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, supp F ⊂ [−T,T], F ∈ P_T.
N_T: negative subspace of Arch on P_T (does not depend on the weight), non-trivial for T above the archimedean
threshold (Paper 46 cor:Tarch; threshold in [0.58, 0.60]).

## 0. Preliminary cross-check (in primary sources and in the index)

What the corpus already has on N_T and on the contacts as a source:

- Paper 46 cor:Tarch and Theorem P (n₋ ≤ 5/7/8): N_T exists and its dimension is bounded at the first
  thresholds; the integer invariants (Pontryagin index) are closed (BARRIER_W_001; index 05b).
- phase-155 R155_029 («the primes are necessary» past ≈0.596), R155_026/032 (Schur reduction), R155_044
  (nodal explanation of the 2/3 cancellation): they describe N_T; they give no sign.
- phase-186 Thm A/B, Cor (L1): exact reduction to the finite matrix S_{T,k}; (L2) OPEN. The Schur rounds of
  phase 211 (ROUND_005_C, 007_B, 015_B, 017_A) end with the sign in the coupling at the precision of the margin
  (excluded by the brief, point iv).
- **phase-188 N_BUILD_001 (A) and N_BUILD_011 (+ review):** this is the direct antecedent of the role
  inversion. On P_T, the mean part of the weight, ρ_1 = 2e^{u/2}du, satisfies ∫₀^{2T} c_F dρ_1 = −𝔭(F) ≤ 0, so that
  the mean density of the contacts **contributes +𝔭(F) ≥ 0**: the symbol passes from m to m^♯ = m + 1/(¼+τ²). It is
  exactly «arithmetic (its main term) is a source of positivity on the negative directions
  of Arch». N_BUILD_011 Theorem 1: ρ_κ ∈ Pos ⟺ κ ≥ κ*, with κ* ≥ |C₀|/4 ≈ 1.343 > 1. The mean density alone
  (κ = 1) does not suffice (index 06, «pointwise symbol positivity (κ=1<κ*)», NO-GO; Paper 46 thm:nolocal, W-loc;
  thm:ceiling for integer densities).
- **phase-188 L2_BUILD_017:** identity Λ = μ∗log in translation operators,
  a_T(F) = 𝔞_∞(F) − 2Re⟨U_μF, U_logF⟩ (N_BUILD_002 §1, N_BUILD_005 §1), and AM-GM-type partition certificates
  with W. The recorded live residue (index 06, line 56, (a)) is an **anti-alignment inequality
  between U_μF and U_logF on 𝒩_T**, quantified against the deficit symbol (κ*−1)/(¼+τ²).
- Walls W-lin, W-det, W-fam, W-pat, W-loc, W-mom (phase 186): every first-order discriminant is a functional of
  h*, not of σ; linear fixed-frame certificates dead; locality dead.
- RULES_AVOID §§O–R, REVIEW_007 R7-a (potential bounds die before 0.60), R7-c (ratio channel ∫ĝ|A|²
  blind to arithmetic), ROUND_008_A (boundary concomitant = support commutator, phase 161).

Conclusion of the cross-check: the role inversion **is already written in the corpus** in its natural form (mean
density → +𝔭; fluctuation Λ−1 as remainder) and its open residue is (a). The following candidates are presented
against that antecedent; none is derived beyond the gate.

## 1. Candidate C1 — mean density as source, fluctuation as payment

1. Antecedent: N_BUILD_001 (A), N_BUILD_011 Theorem 1, L2_BUILD_018 (atomic combs in Pos).
2. New object: none. a_T = (1/2π)∫m^♯|F̂|² − ∫ Re c_F d(Λ-comb − ρ_1).
3. Avoidance: no. Since κ = 1 < κ*, m^♯ has a negative part (m^♯(0) = C₀ + 4 < 0, CITED from the review of
   N_BUILD_011); the fluctuation must contribute positively: it is the original problem.
4. Global connection: that of N_BUILD_011/012 (segment λ_t between ρ_κ and Λ; residue t_∞ > 0, OPEN).
- Falsifiers, reading (ARGUED): with cΛ, c = 2, the mean part is ρ_2; if κ* ≤ 2 the mean alone is positive and
  the breakdown occurs in the fluctuation 2(Λ−1), whose term −2∫Re c_F d(Λ−1) ceases to be dominated (it cannot be
  named without knowing κ*: only κ* ≥ 1.343 is proved). Deleting a power p^k: mean intact, the fluctuation
  gains the atom +v_{p^k}c_F(k log p), indefinite in F. Beurling weight: changes the effective κ and the fluctuation.
- Verdict: **repetition**. Stopped.

## 2. Candidate C2 — polarization of the Möbius–log pair

With the identity of L2_BUILD_017, −2Re⟨U_μF,U_logF⟩ = ‖U_μF − U_logF‖² − ‖U_μF‖² − ‖U_logF‖² (PROVED,
polarization), hence
  a_T(F) = [𝔞_∞(F) − ‖U_μF‖² − ‖U_logF‖²] + ‖U_μF − U_logF‖².
The square is built with the contacts using the multiplicative structure (μ∗log = Λ) and the additive one (translations
τ_{log n}); the archimedean part «pays» the two norms.

1. Antecedent: L2_BUILD_017 §2–§4 (partition certificates, AM-GM with W; W = 1 is this identity).
2. New object: only the inverse split of the same polarization. With general W, the family of L2_BUILD_017
   contains it (opposite sign in the cross term = change U_μ → −U_μ).
3. Avoidance: no. ‖U_logF‖² grows with N = e^{2T} (the weights log n/√n are not square-summable: ARGUED), so the
   bracket is very negative and the square must carry the whole sign: it moves the obligation without a mechanism.
4. Global connection: no new one.
- Falsifiers (ARGUED): c = 2 doubles the cross term; the identity then carries ‖U_μF − 2U_logF‖² and the
  payment grows by 3‖U_logF‖²; deleting p^k breaks μ∗log = Λ (the remainder is +v_{p^k}c_F(k log p)); Beurling: the
  convolution μ_B∗log_B still holds, the term that falls is the archimedean one, which no longer fits the mean.
- Verdict: **repetition** (L2_BUILD_017; residue (a) of index 06). Stopped.

## 3. Candidate C3 — anti-alignment restricted to N_T (the best; missing operation)

Sought: for F ∈ P_T, with projection F₋ onto N_T, an inequality
  −2Re⟨U_μF, U_logF⟩ ≥ −controlled Arch₊-part + (positive lower bound in F₋)        (∗)
i.e. that on N_T the cross term of contacts be **positive** and exceed |Arch(F₋)|, with the directions
of P_T ⊖ N_T paid by Arch.

1. Antecedent: index 06, line 56, residue (a) (L2_017 lesson; N_011). No recorded execution.
2. What would be required (not written): an exact identity expressing Re⟨−U_μF₋, U_logF₋⟩ − |Arch(F₋)| as a sum
   of squares using Σ_{d|n}Λ(d) = log n (additive in the translation exponent: τ_{log n} = Π τ_{log p^k}).
3. Why it could avoid R7-a/R7-c: it does not bound contacts from above (positive contribution on N_T) and it is not the ratio
   channel (it is the μ–log cross term, not |A|²).
4. Global connection: (∗) with a constant uniform in T and dim N_T bounded (Theorem P only gives bounds at the first
   thresholds; for T large dim N_T grows, ARGUED) would give a_T ≥ 0 on P_T via a 2×2 block Schur square.
- First non-trivial case: T = 0.5925 (falsifier of §O), N_T of dimension 1, where (∗) reduces to a number.
- Underlying problem: a 2×2 block (N_T, its complement) with the cross coupling at the precision of the margin is
  precisely the reduction excluded by point (iv). Without the sum-of-squares identity of point 2, C3 is
  Schur under another name.
- Verdict: **does not pass** my own check.

## 4. Conclusion

No candidate survives. The role inversion in its natural form exists in the corpus (N_BUILD_001 (A):
the mean density of the contacts contributes +𝔭 ≥ 0 on P_T) and fails because κ = 1 < κ*. **Precise missing
operation** (for C3): an exact identity, valid on all of P_T and for all T, that writes
  −2Re⟨U_μF, U_logF⟩ − ∫Re c_F dρ_1 + (negative part of m^♯ in F)
as a sum of squares in the translations τ_{log p^k}, composed by the law τ_{log m}τ_{log n} = τ_{log mn}, whose
term that loses the sign under c = 2, deletion of p^k and Beurling is nameable. Without that identity the deficit
(κ*−1)/(¼+τ²) remains in the fluctuation.

## 5. List of claims and labels

| Claim | Label |
|---|---|
| On P_T the mean density ρ_1 contributes +𝔭(F) ≥ 0 (N_BUILD_001 (A)) | CITED |
| ρ_κ ∈ Pos ⟺ κ ≥ κ*, κ* ≥ 1.343 > 1 (N_BUILD_011 Theorem 1) | CITED |
| The natural role inversion is a repetition of N_BUILD_001/011 | ARGUED (cross-check) |
| Polarization identity of C2 | PROVED (trivial) |
| C2 contained in the family of L2_BUILD_017 | ARGUED |
| ‖U_logF‖² grows with T and the bracket of C2 becomes very negative | ARGUED |
| Falsifier readings (c = 2, deletion, Beurling) in C1–C2 | ARGUED |
| For c = 2 the breakdown may be in the fluctuation and not in the mean (if κ* ≤ 2) | CONDITIONAL (on κ* ≤ 2, OPEN) |
| C3 without a new identity coincides with the excluded Schur reduction | ARGUED |
| Anti-alignment inequality (∗) on N_T | OPEN |
| Global sign of a_T on P_T | OPEN |
