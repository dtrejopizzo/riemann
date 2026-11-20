# REVIEW_002_BC — Critical review of ROUND_002_B and ROUND_002_C

Scope. Full reading of the two memos and of `BRIEF_CONSTRUCTOR.md`, `README.md`, `OBJECT_SPEC.md`,
`LEDGER.md`, `RULES_AVOID.md`, `../phase-211-sign-sandbox/STATEMENT_001.md`. Primary sources opened for
this review: 211 `POWER_GLOBAL_ROUTE_REVIEW.md` ("Factorial extension before resonance" and its
corollaries; "Control of the orthogonal substitution"), 211 `POWER_GRAM_SLICES_OBSTRUCTION.md` §§16.4,
17.2–17.5, 211 `ROUND_003_B.md`, 211 `ROUND_005_A.md` Prop. 3.3, 211 `LEDGER.md` (C9, C33b, C49);
phase 170: R170_201, R170_301, R170_850, R170_851, R170_854 §§3–6, R170_856 §§0, 3–4, R170_868;
R166_502 §5.2; phase 204 `P1_BBSTAR_001.md` §§2.2, 2.6–2.8, 3–4; `ROUND_001_C.md` (Theorem R, instances and
§7); and the phase 116 primary source that memo B did not read
(`phase-116-the-logarithmic-schur-angle-conjecture/working-notes/outputs/row_d_gamma_fourier_tate_v94_audit.tex`,
equations (79)–(84), (132)–(153), (195)–(201), (223l)). The derivations marked PROVED in this
review are written out in full here. No other file was modified.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Summary.

| Memo | Overall verdict | Error in the core | Corrections |
|---|---|---|---|
| ROUND_002_B | ACCEPTED WITH CORRECTIONS | none in the identities; one false corpus claim, one correct but contentless application, one use of R-cont out of scope | §B.3 |
| ROUND_002_C | ACCEPTED WITH CORRECTIONS | none in the two elementary facts; one false sentence about orientation, the three readings are not exhaustive, the OPEN residue is ill-posed in its letter | §C.3 |

In both cases the verdict "repetition, no new mechanism" holds for the candidate as
formulated. Neither is an impossibility, and neither memo phrases it as such
except at the points corrected below.

---

## Part B — ROUND_002_B

### B.1 Check against the primary sources

1. **GLOBAL, "Factorial extension before resonance".** The primary text says: «sum Lambda P_m*KP_m
   has entry K_lambda,mu log gcd(q_lambda,q_mu)», with q_λ the largest integer whose square divides λ,
   P_m the selection of indices divisible by m², and the exact identity
   Q[c] = Σ_{m≥2} Λ(m)‖P_m b − R_m b‖²_K + b*Db + E(b). CITED, checked. The remainders cited by the
   memo (D with positive entries and not semidefinite; E(δ_1) < 0; no finite C with E ≥ −C·S_sq; kernel
   of S_sq = squarefree support; B + M ⪰ 0 false on {1,2}) appear there as cited.
   Precision: the matrix is [log gcd(q_λ,q_μ)] = E′ diag(Λ) E′ᵀ with the incidence E′_{λ,m} = 1_{m²|λ}
   on the modal index, not [log gcd(i,j)] on a free index. It is an instance of (B)
   (ℓ_λ = modal coordinate, arithmetic index q_λ), not the whole scheme (B).
2. **GRAM §17.2.** (RES-SOS) appears as the memo cites it, with f_q = Σ_{a|q}√a c_a, the substitution
   Σ_{m|q}Λ(m) = log q and D_q of §17.3; scope of §17.4 as cited. CITED, checked.
3. **211/ROUND_003_B (C9).** It is the metric δ = log(lcm/gcd) as a Schur multiplier on 𝔸_M;
   its Prop. 1 is a reformulation and the prescribed cases are NO-GO. It is not candidate (B): there the
   kernel multiplies the target matrix, here it weights a Gram in F. The memo cites it with that scope.
4. **R170_868.** The theorem is stated for an arbitrary target space Y (§0) and in a
   tensor version over the algebraic kernel (§4). Taking Y = Hermitian forms is not an extension: it is
   within the statement. PROVED in the primary source, in finite dimension in (a, c).
5. **R170_201 and R170_301 (primary).** 201: squares per prime channel D_p*D_p = C_p I − (V_p + V_p*),
   without quotients because the channels are separated before the norm; optimal constant cost C_P (Thm. 2,
   proved at frequency zero, with the express caveat that it does not cover factorizations compressed to
   a window); generic in the weights (§6). 301: E_T = Γ_T + 2A_T I − J_T + 2|c⟩⟨c| with
   ⟨E_TF,F⟩ = Γ_T(F) + Σ a_n‖F − S_{log n}F‖² + 2|⟨F,c⟩|², W_T = E_T − C_T, and the equivalence with a
   contraction (11); falsifier a₂ = 100. Neither uses an incidence matrix or [log gcd]. The
   memo's summary is correct for 201; for 301 it omits that there are operators there that do see the
   window (compressed J_T, functionals ⟨F,c⟩, ⟨F,s⟩), which matters for B.2 point 2.
6. **Phase 116 (primary source not read by the memo).** The object is K(m,n) = gcd(m,n)/√(mn) as the Gram of
   dilation states ⟨V_n e_t, V_m e_t⟩ = (mn/g²)^{−t/2} at t ↓ 1 (eqs. (132)–(137)), with
   realization by divisor-incidence columns and Möbius whitening ((195)–(198), (150)–(152)).
   It is coupled to F through the channels J_{a,±}F = (τ_aE_TF ± E_TF)/√2 in L²(ℝ) ((79)–(84)), for which
   ‖J_{a,∓}F‖² = ‖F‖² ∓ Re c_F(a): F enters only through its autocorrelation. Moreover the gcd Gram is
   orthonormalized (η_n = Σ (K_T^{−1/2})_{mn}χ_m, (138)), so it does not enter the form; the
   contractivity (84c) remains unproved there and the canonical inversion does not supply it ((223l)).
   Consequence: phase 116 is a case of the memo's class (i) and **does not change the verdict**.
   Relation with (B): differentiating (mn/g²)^{−t/2} at t = 0 gives log g − ½ log m − ½ log n, i.e.
   [log gcd] minus two low-rank terms; it is the metric δ of C9. PROVED (one line).

### B.2 The three questions of the assignment

**1. Is it literally the same object?** As a scheme, no; as the only written instance that sees the
window and uses the incidence, yes. The verdict sentence "the candidate coincides with RES-SOS and with the
factorial extension" should be read as "the only instance of (B) with [log gcd] written in the corpus is the
modal theta one". The record correction proposed by the memo (RULES_AVOID I1, ledger, index) is
correct and is already incorporated in those files.

**2. Is the dichotomy of the ℓ_i exhaustive?** The partition "commutes with translations / does not commute" is
exhaustive by logic. What is not exhaustive is the description of the second class. The sentence "the
only family written in the corpus is the modal one of the theta carrier" is **false as a corpus
claim**. There are at least three families that see the window and are not the modal one:

- truncated translations: B_nF = 1_Iτ_{log n}F − F (phase 204 `P1_BBSTAR_001` §3, class K3; Prop. 3.1
  closes only the term-by-term use; the residue "K3 not grouped in a fixed basis" remains OPEN there as an
  empty class of candidates); words of truncated translations QV_aQ (211/ROUND_005_A Lemma 3.2,
  Prop. 3.3); compressed J_T and paths B_T^{−1/2}J_TB_T^{−1/2} (R170_301 §§2–5);
- rank-one functionals: ⟨F,c⟩, ⟨F,s⟩ (R170_301 (3)–(4)), A(F), B(F);
- sampling: the Nyquist mesh (P47 thm:nyq, listed in `README.md` §3).

For the first one can say what (B) gives. **Lemma B-1 (PROVED).** Let Q = 1_{I_T}, R = 1 − Q,
U_i the translation by log i and ℓ_i = x_i Q U_i with x_i ∈ ℂ. Then
⟨ℓ_iF, ℓ_jF⟩ = x_i x̄_j [c_F(log i − log j) − ⟨RU_iF, RU_jF⟩] (with the convention for c_F of STATEMENT §1,
up to conjugation), and

    Q_B(F) = (1/2π)∫ σ_B(τ)|F̂(τ)|² dτ − Σ_d Λ(d) ‖R Σ_{d|i} x_i U_i F‖²,
    σ_B(τ) = Σ_d Λ(d) |Σ_{d|i} x_i i^{iτ}|² ≥ 0.

*Proof.* ‖QG‖² = ‖G‖² − ‖RG‖² with G = Σ_{d|i} x_iU_iF, and Plancherel in the first term. ∎
That is: a form of class (i) minus a non-negative leak. The structure is that of 211/ROUND_005_A
Prop. 3.3 (quotients ≥ 0 minus leak ≤ 0). There is no new sign mechanism in this instance, but
it is not excluded either: the remainder ρ_T = a_T − Q_B was not examined in any file.

For scalar functionals (sampling, boundary, rank one), (B) gives Σ_d Λ(d)|Σ_{d|i}ℓ_i(F)|². No
memo in the corpus writes it. See point 4 of B.3 on the actual scope of R-cont in this case.

Correct label of the dichotomy: class (i), PROVED; "class (ii) reduces to the modal theta one",
**withdrawn**; in its place: "the only instance of (ii) with written incidence is the modal one; the
truncated translations give (i) minus a leak (Lemma B-1); per-window scalar functionals, unwritten".

**Lemma B-2 (PROVED, strengthens class (i)).** If the ℓ_i commute with translations, every identity
(G) with ‖V_TF‖² = Q_B(F) has remainder ρ_T(F) = (1/2π)∫(s_T − σ_B)|F̂|², with s_T − σ_B ≤ s_T for all τ.
Hence ρ_T ≤ a_T as forms, and proving ρ_T ≥ 0 on P_T is a statement of the same type as (★) and
stronger. *Proof.* σ_B ≥ 0. ∎ This also holds with values in an auxiliary Hilbert space (for example
ℋ_gcd ⊗ L²(ℝ) of phase 116): the symbol is Σ_{i,j} G_{ij}⟨x_i(τ), x_j(τ)⟩ ≥ 0 for every Gram G.

**3. Is the extension of R170_868 to Hermitian forms proved?** Yes, and it is not an extension (B.1
point 4). But its content here is nil. Written out in full: with ℓ_i and ρ_T independent of the weights and
N′ ≥ all indices involved, the row

    ℓ(a, c) := c·(Arch − ρ_T) − Σ_n a_n κ_n − Σ_d a_d ‖L_d ·‖²,   κ_n := (2/√n) Re c_F(log n),

is linear and vanishes at (Λ, 1) if and only if (G) holds. Factoring through 𝒟_{N′} is equivalent to
κ_d + ‖L_d·‖² = −Σ_{k: d|k} Q_k/√k and Arch − ρ_T = −Σ_k (log k/√k) Q_k, that is

    ρ_T = Arch + Σ_k (log k/√k) Q_k,   Q_k/√k = −Σ_m μ(m) [κ_{km} + ‖L_{km}·‖²].

This is the substitution Λ = μ∗log in ρ_T = a_T − Σ_dΛ(d)‖L_d·‖², valid for every expression linear in
the values of Λ. PROVED and **tautological**: it restricts neither the sign of ρ_T nor the choice of the ℓ_i.
"Prime-free form" means only "without Λ written"; it contains μ and the squares themselves. The memo's
conclusion "it does not follow from 868" overstates: the negative conclusion of 867–868 (every positive
linear extension is a change of metric) refers to extensions 𝓔_N*𝓔_N on the coefficient space,
not to (G). Moreover `OBJECT_SPEC.md` O2 asks exactly for this (form affine in the comb; the nonlinearity
in the action of V_T on F), so being a "linear use of Λ∗1 = log" does not disqualify by itself.
And the hypothesis "ℓ_i independent of the weights" is not forced: ℓ_i built with exact Λ lie
outside 868 (condition 2 of its §0).

### B.3 Verdict per claim and exact corrections

| # | Claim of the memo | Verdict | Correction |
|---|---|---|---|
| 1 | Class (i): Q_B is a multiplier with symbol ≥ 0, F enters through c_F (PROVED) | ACCEPTED | add Lemma B-2 |
| 2 | Σ_mΛ(m)P_m*KP_m = K ∘ [log gcd(q_λ,q_μ)] in GLOBAL (CITED) | ACCEPTED | specify: incidence m² \| λ on the modal index |
| 3 | Application of R170_868 with target in Hermitian forms (PROVED) | ACCEPTED WITH CORRECTIONS | correct and tautological (B.2 point 3); withdraw "it does not follow from 868" and "the whole sign obligation passes to a prime-free form" as an obstacle; add that it does not cover ℓ_i depending on Λ |
| 4 | R-cont excludes L_d = Σ_{d\|i}ℓ_i when i indexes nodes or modes | ACCEPTED WITH CORRECTIONS | only on the integer-scale carrier of A_0: Theorem R does not transport to (S) or to per-window objects (`ROUND_001_C.md` §7(ii); `OBJECT_SPEC.md` §3). For Nyquist sampling or boundary functionals there is no exclusion. Withdraw "and that is why the remainder E has no sign": the lack of sign of E is proved directly in GLOBAL |
| 5 | "The only family written in the corpus [that sees the window] is the modal one" | REJECTED | replace by the list of B.2 point 2 and Lemma B-1 |
| 6 | "The candidate coincides with RES-SOS and with the factorial extension" | ACCEPTED WITH CORRECTIONS | "the only instance with written incidence is that one" |
| 7 | Three origins of the sign (archimedean, lcm/gcd, degree two): ARGUED, not NO-GO | ACCEPTED | the relation with phase 116 in B.1 point 6 confirms the second |
| 8 | The pairs k, k+1 share no L_d, d ≥ 2 | ACCEPTED (PROVED, trivial) | — |
| 9 | Breaking line: none in Q_B; the substitution Σ_{d\|k}Λ(d) = log k breaks the identity, not a sign step | ACCEPTED | — |
| 10 | Summary of R170_201/301 | ACCEPTED WITH CORRECTIONS | 301 contains operators compressed to the window (B.1 point 5) |
| 11 | Phase 116 unchecked | resolved here | B.1 point 6: class (i), orthonormalized Gram; changes nothing |
| 12 | Result: "no new mechanism; not a class NO-GO" | ACCEPTED | — |

### B.4 What remains not excluded

- ℓ_i that see the window and are not the modal theta one: truncated translations grouped by incidence
  (Lemma B-1: their remainder ρ_T was not examined), per-window scalar functionals (Nyquist sampling,
  boundary), and any family on 𝔸_M.
- ℓ_i depending on the exact values of Λ (outside the linearity hypothesis).
- A joint compensation of b*Db + E(b) with the factorial squares, or of Off with R_res.

None of these has a written object or a sign mechanism today; they are listed as terrain, not
as candidates.

---

## Part C — ROUND_002_C

### C.1 The two proofs

**Coefficient matrix.** Σ_p y_p² − 2Σ_{p<q}y_py_q = 2Σ_p y_p² − (Σ_p y_p)². The matrix is 2I − J
(J of ones), with eigenvalues 2 (multiplicity r − 1) and 2 − r; congruence by diag(ℓ_p) preserves
inertia. For r = 2 it is (y_p − y_q)²; for r ≥ 3 there is a negative direction (at y = (1,…,1) it equals
r(2 − r)). PROVED, correct. Scope, as the memo says: only the matrix that results from assigning to each
prime a diagonal ℓ_p² and to each pair the cross term −2ℓ_pℓ_q; the law (0.2) distributes those values over
distinct nodes (p^k and p^aq^b), and that identification of nodes is a choice of reading, not a
consequence of the law.

**Homogeneity.** The natural objection is that Λ∗Λ is quadratic in the weight, so that the expression
a·log − a∗a evaluated at a = cΛ gives cΛ·log − c²Λ∗Λ ≠ c·γ_Λ. The primary source settles which of the two objects
is γ: R170_850 (3.1) gives B_Λ(s) = −ζ²(1/ζ)″, and for a general weight with series A(s) the arithmetic
Wronskian is β_a = 1∗(a·log) − a∗log (series −ζA′ + ζ′A), linear in a with the integer comb fixed. Then
μ∗β_a = a·log − (μ∗a)∗log = a·log − a∗(μ∗log), which is R170_854 (4.7) (checked in the primary source: «μ∗β_a =
Da − (μ∗a)∗D1»). With a = Λ, a∗(μ∗log) = Λ∗Λ. With a = cΛ, γ_{cΛ} = c(Λ·log − Λ∗Λ) = c·γ_Λ. **PROVED,
correct**, with this precision that the memo must write: one of the two factors of "Λ∗Λ" is
μ∗log of the fixed integer comb; the quadratic object a·log − a∗a is not the one produced by the extraction.
For a_P: (a_P∗Λ)(p^aq^b) = (1_{p≥P} + 1_{q≥P})ℓ_pℓ_q; the memo's values are correct.

Correction of the conclusion. "Does not distinguish c = 1" is too much. For cΛ the law of values (0.2) is
multiplied by c, so the identity γ_a = −Σ_{d|n}μ(d)log²d is false for c ≠ 1: the channel
distinguishes c = 1 exactly as the linear separator Σ_{d|n}a(d) = log n does, and no more. What
homogeneity proves is that the channel **does not contribute a degree-two break**: it is not the
non-homogeneous relation Λ·log + Λ∗Λ = μ∗log² of `OBJECT_SPEC.md` O10 (which is false for cΛ in a
quadratic sense), but its linear half. "Violates O4" should be read as "adds to O4 nothing the linear
separator does not give"; "violates O10", correct.

### C.2 Antecedents

Checked in the primary sources and consistent with the citation: R170_850 §§0, 4, 5 (law (0.2), form (4.2), «this
completion is not asserted here»); R170_851 §§0, 2 (γ = Λ·log − Λ∗Λ; with W it returns to R162_501
Prop. 3.1(a)); R170_854 (3.4) («every exact quadratic representation of the current preserves an
indefinite metric») and §6.3 (squaring the sector: quotients with the positive metric, or indefinite
supertrace); R170_856 §4 ((4.3)–(4.5): the W completing γ cancels against the −W of the Poisson branch);
R166_502 §5.2 (V*V versus V²; the non-integer part of V*V is Σ_{p≠q}V_p*V_q; «cancellation must come
from a signed second sector»); `P1_BBSTAR_001` Theorem P1.A, Lemma 2.7, §2.8; 211/ROUND_005_A Prop. 3.3;
R186_005 Lemma S0; README index (rows R11_2_ORIGIN, P1_BBSTAR, P211-5A) and Paper 48 (row "Selberg
difference channel"). All CITED.

Precision on "literal antecedent". R166_502 §5.2 treats V*V with causal V (one-directional
translations). The candidate additionally asks for diagonals "that a_T contains" and admits translations in both
directions. It is the closest antecedent and covers the causal reading; by itself it does not cover the reading of
C.3 point 2.

### C.3 The three readings, the orientation and the OPEN residue

**1. A false sentence.** In (3): "The correct orientation of the cross term is obtained only in the
convolution square (linear in c_F), not in the Hermitian one". One-line counterexample: with
D(τ) = Σ_p w_p sin(τℓ_p), |D|² = ½Σ_{p,q}w_pw_q[cos τ(ℓ_p − ℓ_q) − cos τ(ℓ_p + ℓ_q)], a Hermitian square
whose cross term at ℓ_p + ℓ_q is −w_pw_q, negative for all pairs at once. PROVED. What is true is: in a
scalar-valued Hermitian square the negative cross term at sums comes with quotients of
positive coefficient and with mass. The memo's own Hermitian reading already admits pairing
one direction with the opposite; (3) contradicts it.

**2. The three readings are not exhaustive.** Missing is the reading of **separated vector-valued
channels**, which eliminates the quotients. **Lemma C-1 (PROVED).** Let ℓ_1,…,ℓ_r > 0, w_p > 0, r ≥ 2,
G = I − (2/r)J (symmetric, eigenvalues 1 and −1). In 𝒦 = ℝ^r ⊕ ℝ^r set e_p = (δ_p, 0),
f_p = (Gδ_p, (I − G²)^{1/2}δ_p); both families are orthonormal and ⟨e_p, f_q⟩ = G_{pq}. With
a_p = w_p√r/2 and the multiplier x_p(τ) = a_p(e^{iτℓ_p}e_p + e^{−iτℓ_p}f_p), X_p : L²(ℝ) → L²(ℝ; 𝒦_ℂ),

    ⟨x_p(τ), x_q(τ)⟩ = −w_pw_q cos τ(ℓ_p + ℓ_q)   (p ≠ q),
    ‖x_p(τ)‖² = (r/2) w_p² [1 + (1 − 2/r) cos 2τℓ_p],

and therefore, for every F,

    ‖Σ_p X_pF‖² = (r/2)Σ_p w_p² [‖F‖² + (1 − 2/r) Re c_F(2ℓ_p)] − 2Σ_{p<q} w_pw_q Re c_F(ℓ_p + ℓ_q).

*Proof.* ⟨e_p,e_q⟩ = ⟨f_p,f_q⟩ = δ_{pq} kills the terms at ℓ_p − ℓ_q; the terms at ℓ_p + ℓ_q
give 2a_pa_qG_{pq} cos τ(ℓ_p + ℓ_q) with G_{pq} = −2/r; the diagonal uses G_{pp} = 1 − 2/r. ∎
Thus there is an explicit square, without any atom at log(p/q), with the cross term −2w_pw_q of fixed sign for
all pairs. Its price is mass (r/2)Σw_p², which grows with the number of primes (compare with the
direction 2 − r of the coefficient matrix: it is the same fact seen from the diagonal). It holds for
arbitrary weights and frequencies: it is generic, survives the whole battery of `RULES_AVOID.md` §E, and
hence is not a sign step. It belongs to the class of sums of squares of almost
periodic polynomials (R170_201 §3 separates channels in the same way; `P1_BBSTAR_001` class K1), and by Lemma B-2 of
Part B its use in (G) leaves a remainder with symbol smaller than s_T. The memo's claim "the whole
class is closed for T ≥ ½log3 by P1.A" is exact only when the archimedean compensation is a
constant (statement of P1.A); in general what there is is Lemma B-2, which is not a NO-GO.

**3. The OPEN residue is ill-posed in its letter.** Condition (a), "X_q*X_p is, for all
pairs p ≠ q, the shift by log p + log q with a coefficient of fixed sign", is contradictory
as an operator identity. **Lemma C-2 (PROVED).** If X_q*X_p = κ S_a and X_p*X_q = κ′ S_a with
a = ℓ_p + ℓ_q ∈ (0, 2T) and S_a the translation (on L²(ℝ)) or its compression to L²(I_T), then κ = κ′ = 0.
*Proof.* X_p*X_q = (X_q*X_p)* = κ̄ S_{−a}, hence κ′S_a = κ̄S_{−a}. For F ≠ 0 supported in
(T − δ, T) with δ < min(a, 2T − a) one has S_{−a}F = 0 and S_aF ≠ 0 in the window (on the line, S_a and
S_{−a} are linearly independent); hence κ′ = 0, and by symmetry κ = 0. ∎
The meaningful condition is the symmetrized one, Re⟨X_qF, X_pF⟩ = κ_{pq} Re c_F(ℓ_p + ℓ_q). And by Lemma C-1
the symmetrized one, together with (b), **does have a solution** in the class commuting with translations. All the
weight of the residue is then in (c), and in that class (c) asks that the archimedean form pay on
P_T a growing mass, which is the obstruction of R170_201 Thm. 2 and of `P1_BBSTAR_001` Prop. 3.1 (CITED;
not proved here for every τ-dependent compensation).

Correctly delimited residue: operators X_p **that do not commute with translations** (they see the
window), with Re⟨X_qF, X_pF⟩ = κ_{pq} Re c_F(ℓ_p + ℓ_q) for all pairs, without atoms at quotients, and
with Σ_p‖X_pF‖² equal to a part of the archimedean form plus translation terms that a_T contains,
uniformly in T; moreover, by C.1, the non-homogeneity in the weight has to enter by another route,
because γ is linear. OPEN, no object.

### C.4 Verdict per claim and exact corrections

| # | Claim of the memo | Verdict | Correction |
|---|---|---|---|
| 1 | Matrix 2·diag − rank one; square only with two primes; eigenvalue 2 − r (PROVED) | ACCEPTED | add that the reading identifies nodes p^k and p^aq^b by choice; add Lemma C-1 as counterpart (with diagonal r/2 times larger there is a square) |
| 2 | γ_{cΛ} = c·γ_Λ (PROVED from R170_854 (4.7)) | ACCEPTED | write β_a = 1∗(a·log) − a∗log and that one factor is fixed μ∗log |
| 3 | "Does not distinguish c = 1 (violates O4 and O10)" | ACCEPTED WITH CORRECTIONS | distinguishes c = 1 only linearly, like the separator; contributes no degree-two break |
| 4 | Antecedents (1)a–g | ACCEPTED (CITED, checked) | R166_502 §5.2 is the closest; "literal" only for the causal reading |
| 5 | Coefficient reading: linear use in the autocorrelation | ACCEPTED | — |
| 6 | Convolutive Hermitian reading: "translations in the same direction produce the quotients"; class closed by P1.A | ACCEPTED WITH CORRECTIONS | true with scalar values; false with separated channels (Lemma C-1); P1.A only with constant compensation |
| 7 | Compressed reading = ROUND_005_A Prop. 3.3; "there is no fourth piece" | ACCEPTED WITH CORRECTIONS | true for Π² with Π = Qσ_vQ; not a statement about every truncated family |
| 8 | "The three possible readings" | REJECTED as exhaustiveness | they are three examined readings; add the separated-channel one; those that see the window remain unexamined |
| 9 | (3): the correct orientation only in the convolution square | REJECTED | C.3 point 1 |
| 10 | (3): "NO-GO in those classes, CITED" for R170_854 (3.4), §6.3 | ACCEPTED | the classes are: exact quadratic representations of the graded current; square of the sector with positive metric or supertrace |
| 11 | (4): a_T has no shifts at log(pq); the μ∗log² of the bridge cancels (R170_856 §4) | ACCEPTED | — |
| 12 | OPEN residue (a)–(c) | ACCEPTED WITH CORRECTIONS | literal (a) is impossible (Lemma C-2); symmetrized and with (b) it is solvable (Lemma C-1); the real residue is C.3 point 3 |
| 13 | "Do not relaunch … nor another reading of Λ·log ± Λ∗Λ" | REJECTED in that breadth | "do not relaunch the coefficient, scalar Hermitian, separated-channel and Π² readings without the operators of C.3 point 3"; a rejected selection is not a class exclusion |
| 14 | Result: "no new mechanism; not an impossibility" | ACCEPTED | — |

### C.5 What remains not excluded

- The residue of C.3 point 3 (operators that see the window).
- A second signed sector cancelling the quotients before taking the norm (E70_10, R166_502),
  never built.
- A use of the non-homogeneous degree-two relation Λ·log + Λ∗Λ = μ∗log² that does not go through γ (which is its
  linear half); there is no object.

---

## Annotation texts (without overstating)

**LEDGER.md, two new rows.**

| K2′ | [log gcd] = E diag(Λ) Eᵀ as a Gram on F: Q_B = Σ_dΛ(d)‖L_dF‖² | 2 | NO NEW MECHANISM, ACCEPTED WITH CORRECTIONS (ROUND_002_B; REVIEW_002_BC). Not an impossibility. The only instance with written incidence is the modal theta one (211 GLOBAL "Factorial extension"; GRAM §17.2). PROVED: if the ℓ_i commute with translations, the remainder has symbol ≤ s_T (includes phase 116, gcd/√(mn) with ambient channels); with truncated translations, Q_B = form of that class − leak. Withdrawn: "the only family that sees the window is the modal one"; the application of R170_868 is correct and tautological; R-cont only applies on the carrier of A_0 | not excluded: per-window ℓ_i (grouped truncated, sampling, boundary), ℓ_i depending on Λ, joint compensation of D + E; none with a written object |
| K5 | Two-prime-base channel −2 log p log q of γ = Λ·log − Λ∗Λ (R170_850 §5) | 2 | NO NEW MECHANISM, ACCEPTED WITH CORRECTIONS (ROUND_002_C; REVIEW_002_BC). Not an impossibility. PROVED: coefficient matrix 2I − J, negative direction from three primes on; γ_{cΛ} = cγ_Λ (one factor is fixed μ∗log: the channel is the linear half of the degree-two relation); there is a separated-channel square without quotients with cross term −2w_pw_q, generic and with mass (r/2)Σw_p². Withdrawn: "the orientation only comes out in the convolution square"; "three readings" as an exhaustive list; the condition X_q*X_p = shift is contradictory in its letter | residue: X_p that see the window with Re⟨X_qF,X_pF⟩ = κ_{pq}Re c_F(log p + log q), without quotients and with the diagonal paid by the archimedean form; OPEN, no object |

**Routes index (README, phase 212 entry).**

- P212-2B. [log gcd] = E diag(Λ) Eᵀ as a Gram on F: selection rejected as repetition (211 GLOBAL
  "Factorial extension before resonance"; GRAM §17.2; phase 116, kernel gcd/√(mn) with channels that
  commute with translations). No new mechanism; not a NO-GO. PROVED (elementary): in the class that
  commutes with translations the remainder has symbol ≤ s_T; with truncated translations the form is that
  class minus a leak ≥ 0. Not examined: per-window ℓ_i other than the modal one, ℓ_i depending on Λ.
- P212-2C. Two-prime-base channel of R170_850 §5: selection rejected as repetition (R166_502 §5.2;
  R170_851, 854, 856; P1_BBSTAR; 211/ROUND_005_A). No new mechanism; not a NO-GO. PROVED
  (elementary): γ is linear in the weight with the comb fixed; the coefficient matrix is 2I − J; a
  separated-channel square realizes the cross term without quotients at the cost of growing mass and is generic.
  Reopening: operators that see the window, with the symmetrized condition of `REVIEW_002_BC.md` C.3.

**Grid (same section as the phase 212 note).**

Round 2 of phase 212: [log gcd] on F (K2′) and two-prime-base channel (K5), both "no new
mechanism" as repetition of 211 GLOBAL/GRAM §17.2 and of R166_502 §5.2; neither is a NO-GO. Elementary PROVED
pieces in `REVIEW_002_BC.md` (Lemmas B-1, B-2, C-1, C-2); none is sign progress. Unexamined
terrain: families that see the window and are not the modal theta one.

**RULES_AVOID.md.** I1, replace the last sentence by: "It is the rejected selection 'factorial
squares'; the only instance with written incidence is the modal theta one, and the per-window families
other than it were not examined (`ROUND_002_B.md`, `REVIEW_002_BC.md` Part B)". I8, replace
"the two-prime-base channel −2 log p log q (850 §5, not built)" by: "the two-prime-base
channel (850 §5): cross-checked as repetition, linear in the weight; residue delimited in
`REVIEW_002_BC.md` C.3 point 3".
