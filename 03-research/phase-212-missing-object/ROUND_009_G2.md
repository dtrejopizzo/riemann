# Round 9, G2: recursion with a history-dependent stage datum

Notation of the common brief: a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n, Π_{T,n}(F) = v_n c_F(log n),
T_n = ½ log n. Task: find a recursion whose step depends on the history through a stage datum with
its own formula. According to REVIEW_007 R7-b, the datum can be neither membership in a cone nor the minimizer.

## 0. Primary-source cross-check (done first)

| Family | Antecedent (file, section) | What was built | Where and why it stopped |
|---|---|---|---|
| Schur / Verblunsky / Szegő (lattice) | `phase-159-.../G2_B9_R1.md` §§1–3 (l. 82–87) | Positivity ∀N ⟺ \|α_N\| < 1, but only if the contacts lie on a lattice hℤ | log 2/log 3 ∉ ℚ: there is no lattice. Lattice sampling is thm:AL (RETRACTED → AL′, deficit Θ(1/M)); the discrete jump calculus is the Kreĭn/KEP reformulation, EQUIVALENT |
| Schur / Verblunsky as hypothesis of a bridge theorem | `phase-201-.../CPOS_CLASS_001.md` §§1–4; `FAMILIES_C_001.md` C5 | «\|α_n\| < 1 ⟹ P ≥ 0» with α_n built from (g, a) | Class theorem: either the bridge is affine in the comb (α: convexity ⟹ C-E′), or it is nonlinear with REF-D verification (β). \|α_n\| < 1 is positivity of the measure (branch 2). Class NO-GO (PROVED in (i), (ii), (γ); trichotomy ARGUED) |
| Causal Cholesky / Kreĭn system in the window | `G2_B4_R1.md` Obs. S2.4 | Gohberg–Kreĭn triangular factorization along L²(−T, −T+s); it is the continuous analogue of Szegő | Exists ∀T ⟺ the recursion does not break ⟺ λ_T > 0. EQUIV (R157_002 rows 38–39). For this unbounded symbol, existence is OPEN even in a single window |
| Canonical / de Branges systems | index 04 l. 410, 457, 467 (G1_B8, G2_B5); 03 ES-16, P0-3, P64 | Suzuki kernel, Nehari norms, de Branges system in window time | REF-D (reformulation of D, not closed). Germ problem H_∞, no usable dλ/dT. P64: false bridge |
| Transfer matrix by primes | `R162_2701` (index 04 l. 817); `ROUND_005_G4.md` §0 | T_p = E_{log p} C_p E_{log p}^{-1}, boost with tanh θ_p = p^{−1/2} | It is J-unitary for every reflection coefficient and detects no falsifier (deletion, Beurling, Λχ₂). NO-GO [W12] |
| Induction in the window / Kreĭn–Bellman–Siegert Riccati | `R162_802` §§4–5; `BARRIER_W_001` §§1–6; `ROUND_005_G4` Lemmas 1–3; README l. 141 (SPEC_A) | Flow in T. The identity Λ∗1 = log acts as a window shift | Linear in the weight. At the crossing the incoming weight has no influence (lem:contA). The only datum of Λ at a crossing is c_{h*}(log n). SPEC_A: the step inherits λ_A ≈ exp(−13e^{2T}) |
| Inverse Jacobi / moments / OPUC | index 01 R5-06, F-06; 03 P33-6, P34-3, P61 | Jacobi T_N reconstructed from the spectral side; e_k ≥ 0 | DEAD: blind to the falsifiers; 2N moments give only N coefficients |
| Sturm / nodal / Courant | README l. 36, 559, 561; 04 l. 264, 395, 672 | Oscillation counts, arena | DEAD (arena ≥ 12 modes, not PF₂; Courant–Sturm class NO-GO) |
| Darboux / commutation / SUSY Riccati | RULES_AVOID J8 (phase 70); FAMILIES_C (Riccati/SUSY, branch β); P1_BBSTAR_001 | A = B*B (+ shift) with the comb as superpotential | BB* NO-GO PROVED in the convolutive class and term by term. «∃B» ⟺ 𝒲 ⪰ 0 |
| Semilocal Sonin chain | index 04 l. 123 (R186_010–015); phases 183–186 | Chain F_S, A_S, Π_S PROVED for all finite S | PARTIAL, no sign: the inertia of the remainder on P_T remains OPEN |
| Recursive transfer | `phase-210-.../RECURSIVE_TRANSFER_001.md` §1 | Exact geometric series of A_{p⁶} in terms of A_1 at scales D/N(p)^j | Another problem (zero density in cubic fields). Contributes no sign to a_T |
| Descent by scales, boundary recurrence | `phase-211/POWER_DESCENT_016` §§2–4, `POWER_RECURRENCE_BOUNDARY_036` §§5–7 | Positive finite differences at fixed order; boundary energy → 0 | Listed in the memory of rejected selections: the remainder keeps the sign obligation |
| Stage predicate with uniform step | `ROUND_007_B` Lemmas 1–2 | — | Equivalent to a local split (§Q2) |
| Szegő–Widom determinants | index 04 l. 39 (W-det), l. 924 (R164_502c) | — | NO-GO: every determinant that decides the sign factors λ_A·R; the symbol is never positive |

**Conclusion of the cross-check (CITED, in primary sources).** The seven classical families of the brief are in the corpus. Each
ended in one of two ways:

- (a) **Exact reparametrization.** The stage parameters (Schur α_k, Cholesky/LDL pivots, Kreĭn causal
  factor, canonical Hamiltonian) are a bijection of the Gram. Their staying in the region is equivalent to
  positivity, and computing them requires inverting the Gram of the previous stage. That is pattern J3 / REF-D.
- (b) **Factors blind to the weight.** The boost of R162_2701 and the Jacobi matrix of RH2021 detect no
  falsifier.

## 1. Search for a recursion outside those entries

Requirements of the brief: (i) indexing by order of entry; (ii) an update that uses the arithmetic of n;
(iii) a named region; (iv) a named breakdown under the three checks.

### 1.1 Two structural restrictions (apply to every candidate)

**Lemma A (the divisor identity is blind to Beurling; CITED + PROVED trivial).** Let (𝒩, Λ_𝒩) be a Beurling
generalized integer system with log as norm. Then Σ_{d|ν} Λ_𝒩(d) = log ν for all ν ∈ 𝒩, by the
definition of Λ_𝒩 as −(ζ_𝒩'/ζ_𝒩). Hence, an update that only uses (ii) in the form
Σ_{d|n} Λ(d) = log n, together with the free monoid structure, runs unchanged on the
Beurling comb. By FAMILIES_A_001 G1 (PROVED, CITED), the free monoid ℕ^× does not distinguish ζ from Beurling. In
consequence, the check (iv)-Beurling can only fail if the step also uses the additive structure of ℕ: which
integer comes after which, or the relation of log n with log(n−1). ∎

**Lemma B (the entry instant is empty; CITED).** If the chain is indexed by the window growing through
T_n, the contact n contributes 0 to all orders at the crossing (Paper 47 lem:contA; 211 ROUND_008_C Prop. 2.3;
ROUND_005_G4 Lemma 1). Between crossings the comb is frozen. Every stage datum updated «at the entry
of n» is therefore updated with an increment that does not depend on v_n at the crossing. Its dependence on v_n can only
appear along [T_n, T_{n+1}), i.e. through transport. By BARRIER_W_001 §6, the derivative on that
stretch is v_n c_{h*_T}(log n), which is read on the minimizer (J3).

Consequence (ARGUED): with window indexing, the «own formula» of the datum cannot be a jump rule
at T_n. It has to be a transport law in T, nonlinear in the weight, that does not go through h*. It is exactly
the residue that R162_802 §5 left without an object. With indexing by n at fixed T (adding Π_{T,n} in order of n),
Lemma 1 of ROUND_007_B forces the datum not to be of cone type.

### 1.2 Candidate 1: Schur chain on the ordered group ℚ_{>0}^×

**Idea.** The log p are linearly independent over ℚ (unique factorization, PROVED). Hence the order
of ℝ restricted to log ℚ_{>0}^× ≅ ℤ^{(∞)} is a total group order, and in it the contacts log n enter in the
order of n. By Helson–Lowdenslager (CITED: prediction on ordered groups), Toeplitz forms on a
group with a total order admit a Schur/Szegő recursion along the order, with one parameter for each
element that enters.

**Four-point filter.**
1. *Antecedent:* G2_B9_R1 §3 (the lattice is necessary for Verblunsky) and AUDIT_PHASE193 row 26 / CA_C_002
   Prop. 2 (Helson H²(𝔻^∞), torus versus line, RD + CIRC). Also CPOS_CLASS_001 (branch β).
2. *New:* replace the lattice hℤ by the total order of ℚ_{>0}^× induced by the line. This avoids the
   objection «log 2/log 3 ∉ ℚ» of G2_B9_R1.
3. *Why it would avoid the difficulty:* it does not. The form a_T is not Toeplitz on ℚ_{>0}^×, because Arch
   has a continuous kernel on ℝ and is not supported on log ℚ^×. Its compression to log ℚ^× is the torus/line
   lifting of CA_C_002 Prop. 2, already classified as RD + CIRC. Moreover, even if it existed, the
   Helson–Lowdenslager parameters are computed by projecting onto the past, i.e. by inverting the Gram (§0 (a)). It is
   REF-D and J3.
4. *Global connection:* it would be «|α_r| < 1 for all r ∈ ℚ^×, r < e^{2T}». This is equivalent to positivity only for
   the discrete form, not for a_T.

**Verdict:** does not pass. It is a repetition of CA_C_002 Prop. 2 plus CPOS branch β.

### 1.3 Candidate 2: multiplicative Schur parameter (the best of the search; no object)

**Desired statement.** Fixed window T. Chain by increasing n, Q_N := Arch − Σ_{n≤N} Π_{T,n} on P_T. The stage
datum is a scalar or finite-rank parameter ρ_N(T), with a rule

  ρ_n = Φ_T(ρ_d : d | n, d < n ; ρ_{n−1} ; log n),

satisfying:
- (iii) Q_N ⪰ 0 for all N ⟸ ρ_n ∈ 𝔇 (fixed region) for all n;
- (ii) Φ uses the divisors (Σ_{d|n}Λ(d) = log n) **and** the additive predecessor n − 1. By Lemma A, without the
  additive predecessor the step cannot fail under Beurling.

**Four-point filter.**
1. *Antecedent:* ROUND_005_G4 §0 (port datum with exact update per crossing, R162_2701); R162_802 §5;
   ROUND_007_B §1 (final reading: the datum has to carry the sign).
2. *New:* only the combined requirement «divisors + additive predecessor» in the step rule. I do not have Φ.
3. *It would avoid the difficulty* of R162_2701, whose factors depend on a single prime and are J-unitary for
   any weight, because it would make the step of n depend on the multiplicative history (the ρ_d) and on the additive
   one (ρ_{n−1}). But I have no formula, so I cannot check that the datum is not the Cholesky pivot
   of the Gram in the ordered basis. If it were, we would be in case (a) of §0.
4. *Global connection:* (iii) for all T. Without Φ there is no identity.

**First non-trivial case (target, not result).** T ∈ (½ log 4, ½ log 5), contacts {2, 3, 4}, where
ROUND_007_B §3 places the first missing square. The entry of 4 = 2·2 is the first in which the rule has
a non-trivial proper divisor: Λ(4) = log 4 − Λ(2) − Λ(1) = log 2, and its additive predecessor is 3. Falsifiers
of the divisor rule in that case (PROVED, arithmetic):
- c = 2: Σ_{d|4} 2Λ(d) = 4 log 2 ≠ log 4. The rule, which receives log 4 and ρ_2, assigns to 4 the weight log 2, while
  the comb has 2 log 2. The step 3 → 4 should leave ρ_4 outside 𝔇.
- Deletion of 4: Σ = log 2 ≠ log 4. Same step.
- Deletion of 2 (with 4 kept): the entry of 2 fails and, through ρ_2, that of 4.
- Beurling: the divisor rule is preserved (Lemma A). Only the term in ρ_{n−1}, i.e. 3 → 4, with
  log 4 − log 3, can break. **That is the line that Φ has to contain.**

That the breakdown under c = 2 leaves the remainder with a negative sign, and does not merely «break the identity», requires knowing
Φ and 𝔇 (discipline R3-i). I do not claim it.

**Verdict:** does not pass the gate: there is no object. The missing operation is recorded (§2).

### 1.4 Candidate discarded without development

A Sturm/Jacobi chain in the Dirichlet basis of the window, with one jump per contact: discarded
by arena ≥ 12 modes (thm:arena), by RFIN_TRACT_001 (n₋(𝔄_N) = 1, REF-D) and by CS0_COMMUTE_001.

## 2. Result

No candidate survives. The classical recursions of the brief are classified as: exact reparametrizations
of the Gram (REF-D/J3), factors blind to the weight, or bridge theorems of the CPOS class. The best direction is
candidate 2.

**The missing operation**, precisely: an explicit rule ρ_n = Φ_T(ρ_d (d|n), ρ_{n−1}, log n) that is not obtained
by inverting or factoring the Gram of the stage. It must satisfy two conditions:
- in the fixed window T ∈ (½ log 4, ½ log 5), Q_4 ⪰ 0 ⟸ ρ_2, ρ_3, ρ_4 ∈ 𝔇;
- the step 3 → 4 must take ρ_4 out of 𝔇 with c = 2, on deleting 4, and under a Beurling weight. In this last case
  the cause must be the additive term log 4 − log 3, because the divisor part is blind to Beurling (Lemma A).

By Lemma B, if the chain is indexed by window instead of by n, Φ has to be a transport law in T,
not a jump at T_n.

## 3. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | The seven families of the brief appear in the corpus with the outcome of the table of §0 | CITED (primary-source reading; not exhaustive) |
| 2 | Dichotomy «Gram reparametrization / blind factor» as a summary of those outcomes | ARGUED |
| 3 | Lemma A: Σ_{d\|ν}Λ_𝒩(d) = log ν in every Beurling system; a rule that only uses divisors and the monoid is blind to Beurling | PROVED (trivial) + CITED (FAMILIES_A G1) |
| 4 | Lemma B: the contact n contributes 0 at the crossing; a jump at T_n does not read v_n | CITED (lem:contA, 211 ROUND_008_C, G4) |
| 5 | With window indexing, the datum must be a nonlinear transport law without h* | ARGUED |
| 6 | Linear independence of the log p and total order of ℚ_{>0}^× | PROVED |
| 7 | Candidate 1 (Helson–Lowdenslager on ℚ_{>0}^×): repetition of CA_C_002 Prop. 2 + CPOS β | NO-GO (repetition), ARGUED |
| 8 | Candidate 2: no object; the missing operation is recorded | OPEN |
| 9 | Mismatches of the divisor rule at n = 4 under c = 2 and under deletion of 4 | PROVED (arithmetic) |
| 10 | That those mismatches produce a negative remainder | OPEN (requires Φ, 𝔇) |
| 11 | Sturm/Jacobi candidate in the Dirichlet basis: discarded by thm:arena, RFIN_TRACT_001, CS0_COMMUTE_001 | CITED |
| 12 | Global sign | OPEN |
