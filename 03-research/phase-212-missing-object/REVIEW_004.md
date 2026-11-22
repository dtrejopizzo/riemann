# Review of round 4 (meta SP-161 with signed weights and four non-excluded zones)

Memos reviewed: `ROUND_004_A.md` … `ROUND_004_E.md`. Every proof labelled PROVED was redone except
where indicated. No memo passes the selection gate: there is no candidate ready for construction.
Global sign OPEN. No result of this round carries a sign.

## Verdicts

| Zone | Memo | Verdict | Checked | Correction or reservation |
|---|---|---|---|---|
| A meta L161.1 with signed weights; sieve weights | 004_A | ACCEPTED | (4.2) coefficients of S_N*S_N; Lemma 1 (G(q) = 0 for q ≥ 2 by the coprime pair (q, q−1), inversion over multiples, w = δ_{N=1}); Prop. 2 (c_N(2p) = −2); Lemma 3 (induction λ = μ on [1, N]) | (4.1) uses the conventions of R161_001 §1, cited. The remark on the "Möbius of the system" is ARGUED |
| B quadratic divisor defect that adds | 004_B | ACCEPTED WITH RESERVATION | Lemma 1: minimizing in ℓ the form a_T − ⟨ℓ, η⟩ + ⟨ℓ, Kℓ⟩ gives η ∈ ran K and a_T ≥ ¼⟨η, K⁺η⟩ | The change of variables ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ and the case Q(u) = 0 of Lemma 2(c) were not redone here. The violations with natural kernels are NUMERICAL with values taken from 211 ROUND_017_A; the large-T case is CONDITIONAL |
| C truncated Möbius remainder | 004_C | ACCEPTED WITH RESERVATION | Lemma 3 (multipliers); Lemma 4; Lemma 5: φ = (¼ − ∂²)ψ_ε ∈ P_T, ‖φ‖² ≍ h²ε^{−3}, moments O(hε), and c_N(p^j) = −1 when p^{j−1} ≤ N < p^j, whence the diagonal constant κ_N > 0 | Lemma 2 (closed form of R_0) was not redone. The indefiniteness of R is NUMERICAL (T = 1, T = 1.5) |
| D near-divisibility in (S) | 004_D | ACCEPTED WITH CORRECTIONS | Lemma A; Lemma B (1 ⊲ 2 ⊲ 6 and not 1 ⊲ 6 if 2T_0 < log(7/6)); Lemma C(a)–(c) (analyticity against the term v_2 at d = log 2) | In Lemma C(d), the passage from the continuous kernel to its sampling at logarithms of integers to exclude semiseparable matrices is ARGUED. N_BUILD_022, L2_BUILD_031, CA_K_001/002 and phase 202 were not opened in the primary sources by the memo |
| E indefinite forms and inertia | 004_E | ACCEPTED WITH RESERVATION | Lemmas 2, 3 and 5 (constancy of indices for \|c − 1\| < λ_A(T)/Σ\|v_n\|); citations P46 thm:parityschur, prop:polarcap, subsec:inertia-excl confirmed | Prop. 1(c) is PROVED in finite dimension and ARGUED for unbounded forms. Phases 155 (round 5) and 156, R161_023, 061–063 and R170_854 were not opened in the primary sources by the memo |

## Results recorded (all without sign)

R4-a (PROVED, `ROUND_004_A.md` Lemma 1 and corollary). Class: real weights w_N of finite support in the
cutoff index, test S_N𝓕F, with the requirement of L161.1 that the interior telescope. The only weight is
w = δ_{N=1} and the identity is a_T = a_T. Telescoping the interior requires Σw = 1; cancelling the hyperbola
tail at large primes requires Σw = 0. Closes the signed branch of R161_002 §§4–5. Does not exclude
different tests, F-dependent weights, nor telescoping after compressing to the window.

R4-b (PROVED, `ROUND_004_A.md` Prop. 2, Lemma 3, (4.3)–(4.4)). The Möbius identity of `ROUND_003_6.md` is not
an instance of L161.1. M^λS_N = I + exterior exactly if and only if λ = μ on [1, N]; with Selberg or
Barban–Vehov weights an interior block I^λ without sign appears. The "Selberg square" is the form A_M
on a vector outside P_T. Sieve weights do not raise the degree in the weight. Antecedents: phase 200
(Q1–Q3, MULT_GAUGE R-MOM, GG_001), R162_1003 §4.

R4-c (PROVED, `ROUND_004_B.md` Lemmas 0–1). Format a_T^{(a)}(F) + 𝔇_a(F) ≥ 0 for every weight a, with 𝔇
quadratic, semidefinite in the atoms and zero at Λ: equivalent, for each F, to η(F) ∈ ran K(F) and
a_T(F) ≥ ¼⟨η, K⁺η⟩. It is the target with margin; the second-order term does not pay for the first jet.
Antecedent: phase 197 BARRIER_D2_001 Thm. 1. Does not exclude unbounded K, weight classes that do not contain
a neighbourhood of Λ, nor non-polynomial defects.

R4-d (PROVED, `ROUND_004_C.md` Lemmas 3–5). Class 𝒯_inv of translation-invariant approximate inverses:
a_T + R_b has symbol Re P̂_b · s_M; two manifest writings of a_T + R ≥ 0 and −R ≥ 0 add up to a
certificate of a_T in which the inverse does not appear. For the truncated Möbius with M ≥ N², N ≥ 4, R ≤ 0 is
false on P_T. Antecedent: phase 200 A_MU_FACTORIZATION_001 (d). Does not exclude inverses compressed to the
window (covered in R170_878–883) nor the quotient block of Z_CARRIER (Lemma Z.2, OPEN).

R4-e (PROVED except for the ARGUED point indicated, `ROUND_004_D.md` Lemmas A–C). The support of Div + Near is not a
partial order; for large ratios it fills the threshold semiorder and does not depend on the weight. 𝖡 is not
totally positive, nor Pólya, nor a Laplace transform on (0, ∞). Pivots determined by the
support pattern: class NO-GO. Does not exclude W with values given by its own formula nor the closure of {𝔸_M} under
Schur complement with an explicit transformed weight.

R4-f (PROVED, `ROUND_004_E.md` Lemmas 2, 3, 5, 6). An upper bound on the negative index is a positivity
on a subspace of finite codimension. In every window with λ_A(T) > 0 the inertia indices are
constant for c in a neighbourhood of 1: an inertia count does not distinguish c = 1. The Pontryagin format
is already in P46 thm:parityschur and prop:polarcap. The counts increasing in T come from the archimedean form
without comb.

## What the round leaves unexcluded, and without a written object

1. Closure of the family {𝔸_M} under Schur complement with an explicit transformed weight (R4-e). Must
   first be cross-checked with R3-b and with phase 70 (E70_10–12).
2. The "Möbius of the system" μ_a, coefficients of the inverse of the weight series, non-polynomial in c (R4-b).
3. Telescoping after compressing to the window with the leakage squares of C_T; accounting
   R161_032 (4.2).
4. The quotient block of Z_CARRIER (Lemma Z.2).
5. A count by the argument principle of an explicit function of a spectral parameter other than
   det Γ_T(z) (R4-f).
6. Unchanged with respect to `REVIEW_003.md`: generators other than pure dilation; VIR–LB and
   VIR–DET; exit A of R161_033.
