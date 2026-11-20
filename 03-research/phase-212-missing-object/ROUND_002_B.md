# Round 2 B — The incidence factorization [log gcd] = E diag(Λ) Eᵀ acting on F (selection memo)

Goal (★): λ_A(T) ≥ 0 for every T, with the definitions of `../phase-211-sign-sandbox/STATEMENT_001.md`.
Candidate: for a family ℓ_i(F), i ≥ 1, linear in F (scalar-valued or valued in a Hilbert space),

    Q_B(F) := Σ_{i,j} log mcd(i,j) ⟨ℓ_i(F), ℓ_j(F)⟩ = Σ_{d≥2} Λ(d) ‖L_d F‖²,   L_d := Σ_{d|i} ℓ_i,      (B)

and the question of whether the comb −Σ v_n Re c_F(log n) of a_T, or a part of it with a manifestly
non-negative remainder, is expressed by (B) with the correct sign. Abbreviations: «GRAM» = 211
`POWER_GRAM_SLICES_OBSTRUCTION.md`; «GLOBAL» = 211 `POWER_GLOBAL_ROUTE_REVIEW.md`.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### (1) Closest antecedent

The antecedent is not only phase 170. The form (B) with F in the indices is already written in phase 211,
on the carrier of integer scales, in two steps.

a. **GRAM §17.2, identity (RES-SOS)** (PROVED there). In each squarefree class d, with coefficients
   c_a of the vector at the nodes k = da², the incidence transform f_q = Σ_{a|q} √a c_a (it is Eᵀ applied
   to the vector) and the identity Σ_{m|q}Λ(m) = log q give

       R_res[c]/√d = Σ_q D_q |f_q|² + Σ_q Σ_{m|q, m≥2} Λ(m) I_q |f_q − f_{q/m}|²,   D_q > 0 (§17.3).

   The weights of the squares are the Λ(m), the orientation comes from the cross term −2Λ(m) I_q Re(f_q conj f_{q/m}) and the
   diagonal is paid by the archimedean logarithm (D_q). It is candidate B restricted to the exact
   coincidences kn² = lm². Scope recorded in §17.4: it does not sign the non-resonant contribution.

b. **GLOBAL, «Factorial extension before resonance: complete identity with signed remainders»**
   (identity PROVED there; global sign OPEN). On the complete form at y = 0, with b_λ = Σ_{n²|λ} n^{−1/2}
   c_{λ/n²}, K the modal Gram, P_m the selection of indices divisible by m² and R_m the dilation,

       Q[c] = Σ_{m≥2} Λ(m) ‖P_m b − R_m b‖²_K + b*Db + E(b).

   The text says literally that Σ_m Λ(m) P_m*KP_m has entry K_{λμ} log mcd(q_λ, q_μ) (q_λ = largest
   integer whose square divides λ): it is the Schur product of a Gram in F with [log gcd] = E diag(Λ) Eᵀ,
   that is (B) with ℓ_λ = (modal coordinate λ of F). Recorded result: D has all entries
   positive and is not positive semidefinite; E(δ_1) < 0; no finite C gives E ≥ −C·(sum of squares); on
   the kernel of the squares (squarefree support) Q = L + M remains without primes and the sufficient
   comparison B + M ⪰ 0 is false (exact test on {1,2}). «Control of the orthogonal substitution in the
   factorial identity» (PROVED there): replacing P_m by the orthogonal projection makes
   Σ_m Λ(m)‖F − R_mF‖² diverge.

c. The selection is also in the memory of rejected selections («Factorial squares and physical
   projections») and in `RULES_AVOID.md` D9 and D18.

Other antecedents consulted.
- Phase 170, R170_863–868 (primaries read): incidence on the coefficient space; ker 𝒟_N = ℝ(Λ,1)
  (866, PROVED); every linear row that annihilates the line factors through 𝒟_N, also after tensoring with the
  physical space (868 §§3–4, PROVED). R170_870: parity wall for the boundary class linear in F.
- Phase 170, R170_201 and R170_301 (read in `ANNEX_170_FILES_1.md`): Σ_n (Λ(n)/√n)‖F − U_nF‖² with unitary
  dilations; remainder with divergent constant, generic in the weights (falsifier a₂ = 100).
- 211/ROUND_003_B (LEDGER C9): the metric δ = log(lcm/gcd), conditionally negative because [log gcd] ⪰ 0,
  as a Schur multiplier on 𝔸_M; NO-GO (reformulation, explicit negative minors). Its cross-check
  cites phase 116 (gcd kernel as Gram of dilation states); I did not check the primary of phase 116.
- 211 GRAM §16.4–16.5: the matrix ρ(k,l) = mcd(a,b)/√(ab) is the main term of A at fixed integer
  scales and is positive definite; it does not dominate uniformly (pairs k, k+1).
- `ROUND_001_B.md` Lemma 4 and Prop. 6; `REVIEW_001_ABD.md` §2.3 point 2: the piece 2ZDZᵀ (gcd paradigm with
  g(d) = d log d) is positive and generic; missing is the operation that signs −(DG + GD) against Z·Arch·Zᵀ.
- `ROUND_001_C.md` Theorem R, instance 2 (R-cont of `OBJECT_SPEC.md` §3): none of the squares of
  RES-SOS survives in a single exact identity for A_0.
- 211 LEDGER C33b, C49; phase 200 A_MU_FACTORIZATION §1(f) (via IDX README): comb collapsed by Λ∗1 = log,
  form without primes, no sign step.
- Grid, crossword and Paper 48: no own entry for gcd matrices beyond those already cited (the grid and
  the crossword reproduce the two entries of GLOBAL). Search for gcd, mcd, Smith, meet, lcm, incidence
  and Ramanujan in `03-research/`: the remaining hits (phases 159, 162, 193) do not use [log gcd] as
  a Gram on F.

Record correction resulting from the cross-check: the sentence «the matrix [log gcd] = E diag(Λ) Eᵀ acting on
F was not used literally» (`RULES_AVOID.md` I1, note of `LEDGER.md`, IDX README, «not attempted» list)
is true for phase 170 and false for the corpus: it was used in 211 (a, b).

### (2) New object

None that can be written. What (B) requires and what there is:

- ℋ_T and V_T: ℋ_T = ⊕_d (value space, weight Λ(d)), V_T F = (L_d F)_d. The family ℓ_i is missing.
- In a sum of squares the only place for a negative term is a cross term (PROVED, trivial). In (B) the
  cross term of i and j carries the weight log mcd(i,j) ≥ 0, located at the common divisor, whereas in a_T the weight
  Λ(n) is at the quotient (the delay log n of c_F). Moving the weight from the common divisor to the quotient forces
  two-term squares along divisibility edges, ‖(·)_q − (·)_{q/m}‖², with conductance
  Λ(m): it is the form of (a) and (b). ARGUED (I do not prove it is the only arrangement).
- The available ℓ_i split into two classes.
  (i) ℓ_i commutes with translations (ℓ_i = x_i U_{log i}, or any multiplier). Then
      Q_B(F) = (1/2π)∫ σ_B |F̂|², σ_B(τ) = Σ_d Λ(d)|Σ_{d|i} x_i(τ)|² ≥ 0, and F enters only through its
      autocorrelation (PROVED, one line). It is a certificate in the sense of `OBJECT_SPEC.md` O2, of
      arithmetic sum-of-squares type (O8; `RULES_AVOID.md` C1 and C3). With two-term squares it is
      R170_201/301: diagonal debt 2Σ_{n<N}Λ(n)/√n ‖F‖², which the archimedean symbol does not pay.
  (ii) ℓ_i sees the window (does not commute with translations). The only family written in the corpus is the modal one
      of the theta carrier (h_λ, K, P_m, R_m), and it gives exactly (a) and (b).
- ρ_T: in (b) it is b*Db + E(b). It is not manifestly non-negative and its two pieces each have a falsifier
  separately (CITED from GLOBAL). I have no other ρ_T to write.

On the three origins of the sign raised by the task:
- **Archimedean term.** It is D_q of (a) and the factor log(t√(λμ)) of D in (b). It signs the diagonal of the resonant part
  and nothing more.
- **lcm/gcd identity.** −log mcd = log mcm − log i − log j. It is the entry
  log(t√(λμ)) − log mcd(q_λ,q_μ) − S(√t) of D in (b): positive entry by entry, not semidefinite (PROVED
  there); and it is the metric δ of C9 (NO-GO). It does not change the orientation in a usable way.
- **Degree-two relation Λ·log + Λ∗Λ = μ∗log².** Gives [log² gcd] = E diag(μ∗log²) Eᵀ ⪰ 0: again non-negative
  weights at the common divisor, without change of orientation. The form is affine in the comb
  (`OBJECT_SPEC.md` O2) and the relation is the Leibniz rule on Λ∗1 = log (`ROUND_001_A.md` Lemma B).
  The recorded uses (R170_850–851, 856; `RULES_AVOID.md` D17b, term 2V) gave no sign. ARGUED: I
  find no new operation; this is not a NO-GO.

### (3) Why the change would avoid the difficulty of the antecedent

It does not avoid it.

- **R170_868.** The theorem concerns linearity in the weights (a, c), not in F. If ℓ_i and ρ_T do not depend
  on the weights, (B) is linear in diag(Λ) and a_T is affine in the comb. The difference between the two sides of
  (G), as a function of (a, c) with values in the Hermitian forms on the common kernel, is a linear
  row that annihilates ℝ(Λ,1); by 868 §§3–4 (valid for any target space) it factors through 𝒟_N. Hence
  (G) is a linear use of Σ_{d|k}Λ(d) = log k and ρ_T = Arch_T + Σ_k log k · Q_k(F) is a form without primes.
  PROVED as a direct application of 868. Being quadratic in F avoids the parity wall of 870 (which is for
  odd functionals), but does not escape 868: the whole sign obligation passes to a form without primes, which
  is the situation of C33b and of the remainder D + E.
- **R-cont.** If i indexes nodes or modes, L_d = Σ_{d|i} ℓ_i is the twist by the indicator of the multiples
  of d, excluded by Theorem R as a square of a single identity (the P_m of (b) is that, and that is why the
  remainder E has no sign). If i indexes unitary dilations one falls into class (i). The variant admitted
  by R-cont with non-unitary dilations on the half-line is R_m; with the orthogonal projection instead of
  P_m the sum diverges (GLOBAL, «Control of the orthogonal substitution»).
- **Near-coincidences.** (B) groups by exact divisibility. The pairs k, k+1 have gcd 1 and share
  no L_d with d ≥ 2, while their columns in the form are nearly parallel (GRAM §16.5, §17.6; `ROUND_001_B.md`
  §4). The content of `OBJECT_SPEC.md` O6 remains entirely in ρ_T.

### (4) Identity that would connect with global positivity

Only the one already recorded: Q = Σ_m Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b) (GLOBAL), or A_0 = R_res + Off with R_res
in the form (RES-SOS). Global positivity is equivalent to jointly signing D + E (respectively
Off ≥ −R_res, which at y = 0 is the complete target without margin, `RULES_AVOID.md` D9). I have no additional
identity.

### (5) Line that breaks for cΛ and for a_P

In (B) alone, none: Q_B ≥ 0 for every non-negative weight. What ceases to be true for cΛ and for a_P is the
substitution Σ_{d|k}Λ(d) = log k (it gives c·log k, or the logarithm of the part of k without primes less than P), that
is the identification of the diagonal of the squares with the archimedean logarithm. That line breaks the
identity, but it is not a sign step: in (a) the signed part has a uniform margin (GRAM §17.5), so
that its positivity cannot break for c close to 1 (ARGUED; not derived here). The sign step would be
in ρ_T, and there there is no line to point to because there is no argument. By `OBJECT_SPEC.md` §4, the candidate is not
ready.

### Cross-check verdict

**Repetition; no new mechanism.** The candidate coincides with RES-SOS (GRAM §17.2) and with the factorial
extension of GLOBAL, already rejected as a selection. The memo ends here; there is no construction.

## Result

**No new mechanism.** It is not a class NO-GO: a joint compensation of D + E with the
squares is not excluded, nor a family ℓ_i that sees the window different from the modal one.

## What was proved

- (PROVED, one line) If the ℓ_i commute with translations, Q_B is a multiplier with symbol
  Σ_d Λ(d)|Σ_{d|i}x_i(τ)|² ≥ 0 and F enters only through c_F: class of certificates.
- (PROVED, application of R170_868 with target space the Hermitian forms) Every identity
  a_T = Σ_d Λ(d)‖L_dF‖² + ρ_T with ℓ_i and ρ_T independent of the weights is a linear use of Λ∗1 = log, and its
  remainder is a form without primes.
- (CITED, checked in the primary) Σ_m Λ(m)P_m*KP_m = K ∘ [log mcd(q_λ,q_μ)] in GLOBAL: the incidence
  matrix did act on F in phase 211.

None of this is sign progress.

## What failed and why

- The weight Λ(d) of the incidence is at the common divisor and that of the comb at the quotient; the only
  written bridge is the squares on divisibility edges, already constructed.
- None of the three sources of orientation (archimedean logarithm, lcm/gcd, degree two) gives an operation
  that is not already in D, in C9 or in the discard of the Selberg term.
- The remainder contains all the near-coincidences and has no manifest sign; its pieces D and E have
  falsifiers separately.
- I cannot write ρ_T nor the breaking line of a sign step.

## Concrete next step

None within B. For the record (this memo does not edit other files):
1. Correct in `RULES_AVOID.md` I1, in the note of `LEDGER.md` and in the «not attempted» list of the index: [log gcd]
   on F was used in 211 (GRAM §17.2; GLOBAL, «Factorial extension»); only in phase 170 does it not appear.
2. Proposed ledger line: «K2′, [log gcd] = E diag(Λ) Eᵀ as Gram on F: repetition of RES-SOS and of
   the factorial extension; no new mechanism; not an impossibility».
3. Reopening condition: an explicit operation that jointly signs b*Db + E(b) with the factorial
   squares (or Off with R_res) without separating the pieces, or a family ℓ_i that sees the window, is not an
   arithmetic selection of nodes and whose remainder can be written as a sum of squares or a positive measure.
   I know of neither.
