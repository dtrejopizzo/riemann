# Round 13, C — map of combination operations between signed objects and objects that see the weight

Notation of the common brief. a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n. For a real weight
a = (a_n) write a_T^a for the form with v_n = 2a_n/√n, A(ξ) = Σ a_n n^{−1/2}n^{iξ}, A_M the multiplier of
R161_001, g_F = c_F ∗ c_F. Checks: 𝒞 = {2Λ, Λ with a prime power deleted, Beurling-type weight}.

**Selection result.** No candidate with a complete identity and global sign was built.
The operations examined have antecedents or leave an unresolved sign obligation.
Lemma T excludes transfer only under ALL its hypotheses, including nonnegativity of the
additional contribution in the check. It does not prove impossibility from the mere survival of the auxiliary
sign. The parity of the canonical squares of (PC) does not extend to all mixed
squares either; see T5. The following lists are an inventory of selections, not an exhaustive
classification of the possible sources of sign.

Primary-source reading for this memo: RULES_AVOID §§Q–V; ROUND_007_C in full; ROUND_009_G3; REVIEW_009;
ROUND_010_A; ROUND_011_A; ROUND_012_A; ANNEX_SONIN_READING §§4–6; R161_002 §§0–2 and §8 (statement of Thm. 8.1).
ROUND_009_G1, ROUND_009_G2 and ANNEX_LITERATURE_CONCENTRATION: through REVIEW_009 and RULES_AVOID S, T
(indirect reading). Routes index, grid and crossword: through the citations of those memos and annexes, which
reproduce the relevant entries (indirect reading; the whole index was not reread).

## 0. Four-point filter (of the brief as a whole)

1. **Closest antecedent.** ROUND_007_C §3: a_T = αQ_T + R_T, with Q_T the ratio channel (≥ 0) and R_T the remainder,
   which is the «sum» combination of an object S with an object W. R161_002 §2 (OR): the oriented pairing. ROUND_012_A
   Prop. B: the Lyapunov certificate Re⟨H_TF, M_TF⟩. ROUND_009_G3 §4: flow with history and convex functional, both
   without object.
2. **What is new.** It is not an object. It is (i) the table of operations of §2 and (ii) Lemma T of §3, which says when a
   combination operation can, in principle, discriminate the checks.
3. **Why it would avoid the difficulty.** It does not. It localizes the difficulty: the operation is not the place of the sign.
4. **Global link.** No new one. (OR) is an already recorded link, without proved sign.
   It does not follow from Lemma T that every candidate must be odd in A_M or adopt that link.

## 1. The two lists, exactly

«Blind» means here: the sign statement of the object holds, unchanged, for every weight of 𝒞 (and for Λ).
«Sees the weight» means: the value of the object changes under each check and some identity in which it enters fails in a
named term. «Without sign» means: there are F (or weights) with both signs.

### List S (manifest sign, blind)

| # | Object | File, section | Sign | Blindness: what and with what status |
|---|---|---|---|---|
| S1 | Sonin square Son_S | R183_018 Prop 3.1; PROOF_L_SHARP_D_001 Thm 2.1; R186_015 | ≥ 0 (square of a unitary involution) | Holds for cΛ and for deletion: D_001 Thm 4.1, Cor 4.2, PROVED. For Beurling: ARGUED (ANNEX_SONIN_READING §4; F_S is unitary for every odd phase) |
| S2 | Ratio channel ∫\|F̂\|⁴\|A\|² | ROUND_007_C (1.1); R161_034 §§0–1 | ≥ 0 | ≥ 0 for every real weight: PROVED (it is \|·\|²) |
| S3 | Leakage squares of phase 161: L^sc = ‖(I−P_+)C_log g‖²; parallelogram ¼‖(U_N−V_N)f‖²; Toeplitz–Hankel ‖(1−P)SP‖² | R161_020 (0.2); R161_035; R161_045; RULES_AVOID R2 | ≥ 0; L^sc > 0 if F ≠ 0 | ROUND_012_A Lemma A: strict positivity for Λ, 2Λ and deletion, PROVED; Beurling undefined. TH: ≥ 0 for all S, PROVED (trivial) |
| S4 | Canonical PC square, ‖S_NA_M𝓕F‖² | R161_002 Thm. 1.1 | ≥ 0 | Even in A_M: PROVED. Sees A², not A |
| S5 | Lattice discrepancies Δ^R (integral test, Euler–Maclaurin) | ROUND_011_A §1, Lemmas 1–2 | only with monotone φ_t; no uniform sign in F (Lemma 1) | No Λ: PROVED (Lemma 2) |
| S6 | Logarithmic uncertainty (Arch as Beckner, constant C_0) | R160_C8_R1 Thm. 1, Cor. 2.4; ROUND_010_A Lemma C (α) | ≥ 0 on the line | No weights: PROVED. In the window it is not ≥ 0 beyond T ≈ 0.60 (P46 cor:Tarch, CITED) |
| S7 | Hyperbola remainder h(k) = Σ_{dm=k, d≤M, m≤N}Λ(d) ≥ 0 | R161_002 §8; RULES_AVOID K5, K7 | ≥ 0 | ≥ 0 for every weight ≥ 0, hence for 2Λ and deletion: PROVED (trivial) |

S7 enters the table of H_{M,N} (list W) as a signed piece. Its sign is that of a nonnegative weight, and therefore it is
blind to c = 2.

### List W (sees the weight, without sign)

| # | Object | File, section | Without sign | Sees the weight |
|---|---|---|---|---|
| W1 | Product channel ∫\|F̂\|⁴ Re A² | ROUND_007_C (1.2)–(1.3), (2.1) | PROVED: a single atom gives g_F(2log n) < 0 | Λ∗Λ = μ∗log² − Λ·log breaks under deletion: ARGUED in ROUND_007_C §3 |
| W2 | Support commutator ⟨g,[P,S]w⟩ and boundary concomitant | R161_057–065; R161_042–044; RULES_AVOID R1, K1 | CITED (positive expansion withdrawn) | linear in the current: CITED |
| W3 | Hyperbola H_{M,N} = L_MS_N − K_N and defect δ_a(k) = Σ_{d\|k}a(d) − log k | R161_001 Thm. 3.1, 4.1 | δ_a changes sign according to the check (log 2 at k = 2 with c = 2; −log 2 at k = 4 with deletion of 4) | PROVED (ROUND_010_A claim 10) |
| W4 | Prime part of Sonin: C_p, K_s, κ_S | R183_018 Prop 4.1; ANNEX_SONIN_READING §4 | C_p indefinite, ± spectrum of infinite multiplicity: CITED | the failure under cΛ lives in C_{ε_c}: CITED (D_001 Cor 4.2) |
| W5 | Product port g and defect G_+ + χG_− = ζW_ε | R161_015, R161_017 Thm. 2.1 | linear in F | linear in the weight: CITED |

**Observation (ARGUED, from the table).** All objects of W are linear in the weight, except W1, which is
quadratic and holomorphic (A², not |A|²). All objects of S are either weight-free (S5, S6), or functions
of |A|² or of norms of operators linear in the weight (S1–S4), or functions of a positive weight (S7).

## 2. Combination operations: table

Each row gives the S-object, W-object, antecedent and reason for failure. «Lemma T» refers to §3.

| # | Operation | Antecedent (file, section) | Status | Reason |
|---|---|---|---|---|
| O1 | Sum or positive combination αS + R | ROUND_007_C §3; J2; L3 (BARRIER_D2_001); Sonin identity (T1) | selection NO-GO, repetition | The sign remains in the remainder R = W − αS; S is ≥ 0 under the checks and the failure lives in R (R3-i automatic). Lemma T with Φ(s,w) = αs + w and hypothesis «w ≥ −αs», which is the goal |
| O2 | Oriented pairing ⟨x, W x⟩ with x an S vector | R161_002 §2 (OR) = ⟨A_MG, S_N^*S_NG⟩; SP-161/K7; T3 (signed weights w_N, closed in L1, R4-a) | NO-GO / reformulation | On the line it is equivalent to the sign of the multiplier (R161_002 §2). In the window it is SP-161; the branch w_N ≥ 0 dies (Thm. 8.1) and the signed branch is closed by R4-a |
| O3 | Cauchy–Schwarz / Gram defect | R161_035 (parallelogram); R161_045 and R2 (PS²P − (PSP)² = \|(1−P)SP\|²); phase 122 | repetition | The Gram defect is ≥ 0 for every weight (S3), and therefore blind. The identity joining it to the PC defect does not exist (K1) |
| O4 | Schur complement in a block [[S, W],[W*, S′]] | J3; L5; D17 (Schur floor); W11′ (R184_015 Thm. 2) | NO-GO with class | Positivity of the block ⟺ S′ ⪰ W*S^{−1}W: norm bound of W relative to S (W11′, B2), or root of the form (J3) |
| O5 | Conjugation U*WU with U an S factor (Sonin) | R186_015; ANNEX_SONIN_READING §4; L6 (inertia) | repetition | Unitary conjugation is the Sonin identity itself, which holds for every odd phase. Congruence preserves inertia (Sylvester): class 6 of G3 |
| O6 | Commutator i[H, A] (Mourre, virial) | J5 (class 18 of G3); R161_057–065; ROUND_012_A Prop. B; CS0_COMMUTE_001 | repetition | ⟨F, i[H,A]F⟩ = 2 Im⟨HF, AF⟩ is the Lyapunov format Re⟨HF, MF⟩ with M = −2iA. By Prop. B, without an A with its own formula it is equivalent to ker H = {0}. With A = dilation, the window boundary leaves a remainder without lower bound (J5) |
| O7 | Monotonicity along a flow (dS/dτ = W) | class 16 of G3 (D17, B10 Danskin in c); R161_015 Thm. 3.1; R161_029 (monotonicity FALSE); Q2/R7-b; G3 candidate A | NO-GO with uniform step; with history, no object (§4.1) | The derivative has to have a sign, and W does not. The natural flows (T, c) give the wrong arrow or are generic in c |
| O8 | Legendre / Fenchel–Young duality | Q1 (R7-a, contact ≤ potential); phase 154 (Thm. Z: dual certificate = explicit formula) | NO-GO with class | ⟨x, W⟩ ≤ S(x) + S*(W) bounds contacts from above with a piece ≥ 0: dies before T ≈ 0.60 (cor:Tarch) |
| O9 | Interlacing / min-max (n₋(W) ≤ rank of a defect S) | L6 (R4-f); P46 Thm. P (n₋ ≤ 5/7/8); W-lin | repetition | The indices are constant near c = 1; a count does not see the margin (P6 of G3) |
| O10 | Tensor / Schur product / second quantization | R7-c §§1–2 (Λ∗Λ, degree 2); K2; J2; N3 (R5-c); N5 (R5-e) | repetition | The Schur product S∘W needs W ⪰ 0. The exponential (Schoenberg / Fock) of a form is positive ⟺ the form is conditionally negative: reformulation. Degree 2 in the weight falls into K2/J2 |
| O11 | Relative position of two subspaces (angle operator) | ANNEX_SONIN_READING §4 (Halmos construction); K1; R2 | repetition | Two-subspace theory is what produces Son_S and the leakage squares: sin\|angle\|² = ‖(1−P)SP‖², blind |
| O12 | Kreĭn space: S as fundamental symmetry, W J-self-adjoint | L6; N1 (R5-a); M1 | repetition | Pontryagin count, constant near c = 1 |
| O13 | Contraction in the projective Hilbert metric (Birkhoff) | G3 candidate A | no object | A map T → T′ preserving the cone is missing; the inclusion P_T ⊂ P_T′ goes in the wrong direction (G3 claim 7) |
| O14 | Convex functional with Hessian a_T | G3 candidate B; N5 (R5-e) | no object (§4.2) | The identification of the positive Hessian with the form is missing; its universal auxiliary positivity is not an exclusion (corrected Lemma K) |

Cross-checks: ARGUED, by reading the cited entries; not exhaustive.

## 3. The common reason

**Class 𝔐 (declared).** Certificates of the form a_T^a(F) = Φ(S^a(F), W^a(F)) + (terms vanishing
identically for a = Λ), in which the inequality Φ(s, w) ≥ 0 is deduced from only two things:
- (a) s ≥ 0, which is the sign statement of the object S;
- (b) a set ℛ of relations (identities or inequalities) between s, w and the weight-free data.

**Lemma T (PROVED, with transfer hypotheses made precise).** Let 𝒜 be the set of weights for which
(a), (b), the decomposition and the nonnegativity of the joint contribution of the additional
terms vanishing for a = Λ hold. No individual sign of those terms is required. If 𝒜 contains a
weight a with λ_A(T; a) < 0 for some T, then no certificate of 𝔐 with those (S, W, ℛ) proves a_T^Λ ≥ 0 on P_T
for all T.

*Proof.* For a ∈ 𝒜, (a) and (b) give Φ ≥ 0; the additional contribution is also nonnegative by hypothesis.
The decomposition gives a_T^a ≥ 0 on P_T for all T, contradicting λ_A(T; a) < 0. ∎

**Scope precision.** The decomposition alone does not transport the vanishing of the additional terms
from Λ to another weight. For example q_w(x)=(2−w)|x|²=|x|²+(1−w)|x|² has a second term vanishing at w=1,
but is negative for w>2 and x≠0. Nor is it required that a positive auxiliary expression lose its sign:
only its identification with the target form may fail. These precisions correct the earlier literal
reading; they do not provide a positive representation of a_T.

With battery E (CITED: λ_A < 0 certified for c > 1 at T = 1 and at ½log5, CERT_FALSIFIERS_001),
some complete transfer hypothesis must fail in each negative check. Only if the decomposition and the other signs
survive is a failure of ℛ forced. In addition the following facts hold.

- (T1) If S is blind (list S), (a) holds on all of 𝒞. PROVED, by the blindness column of §1.
- (T2) A relation of ℛ that is a sign inequality on a nonnegative weight (for example h(k) ≥ 0, or the
  probability laws of ζ^c) holds for 2Λ. PROVED (trivial).
- (T3) A relation that uses only divisors, such as Σ_{d|n}a(d) = log n, holds in Beurling (Lemma A of R9-b, PROVED
  there). A weight-free relation (Tate–Beckner, Poisson on ℤ) holds for 2Λ and deletion (ROUND_010_A Lemma C
  (α), (β), PROVED).
- (T4) Hence ℛ must contain, as an effectively used restriction, the conjunction of Poisson on ℤ with
  Λ∗1 = log, which is the identity (PC) of R161_001 (channel (γ)). This is PROVED within the inventory of relations of
  ROUND_010_A Lemma C; the exhaustiveness of that inventory is ARGUED.
- (T5) **Parity with a precise class.** R161_002 Thm. 1.1 and Cor. 1.2 prove invariance under
  A_M→−A_M of the square ||S_N A_M 𝓕F||² and of its nonnegative sums or integrals with coefficients
  independent of the sign. That information alone does not determine the orientation of A_M. It does not cover
  all squares built using (PC): if L is linear in A_M, then

      ||u_0+L(A_M)F||²
        =||u_0||²+2Re⟨u_0,L(A_M)F⟩+||L(A_M)F||²

  contains an odd term. It does not follow that a complete candidate expression must be odd;
  it may have even and odd components. ROUND_003_2 Lemma 3 remains in force for the affine subclass
  whose cross term reproduces exactly the comb. A Λ-specific identity with a different cross term
  requires its own construction and proof; no candidate is revalidated by this correction.

**Common statement with precise scope.** Lemma T transfers nonnegativity to the check
only if the decomposition, the relations used and the joint sign of the additional terms
survive. It is not enough that the sign of the auxiliary object survive. The identification may fail
only in the check. The list of S/W objects does not prove that every combination stays in the
excluded class nor that it must reduce to (OR).

## 4. The two formats without object of ROUND_009_G3

### 4.1 Flow with history-dependent step (S monotone, W derivative)

Attempt at an explicit pair, with the flow in T:
- 𝔖(T) := λ_min(Son_{S(T)}|P_T), with S(T) = {∞} ∪ {p ≤ e^{2T}};
- derivative: between jumps, 𝔖 is non-increasing by inclusion of domains, for every weight (blind); at T = ½log p,
  the jump of 𝔖 comes from the entry of p (it is the part W4).

The «entropy» format requires a quantity that does not decrease and whose initial value is ≥ 0. Every quantity obtained by
the inclusion P_T ⊂ P_T′ decreases (G3 claim 7, PROVED trivial), and therefore the arrow is the wrong one. To
reverse it one needs the jump of W to have a sign at each T = ½log p, and W4 is indefinite (CITED). The comparison
𝔖 versus λ_A is Lemma H (iv) of R186_029: 1 − ρ* ≤ λ_A/λ_min(Son_S|P_T), which inherits the margin (CITED).
Conclusion: the pair exists but is a repetition (R186_029, W-fam). ARGUED.

With the flow in c (a_T^{cΛ}, c ∈ [0,1]): d/dc = −comb (W, without sign) and a_T^0 = Arch, which is not ≥ 0 on P_T beyond
T ≈ 0.60. It is B10 / class 16. Repetition.

The history dependence required by Q2 would have to enter as a datum with its own formula in the step. No object
of S provides that datum: all are functions of the state at T, without memory. ARGUED.

### 4.2 Convex functional with Hessian a_T (S convex, W Hessian)

**Lemma K (PROVED).** Let Φ(F) = ∫ ψ(F̂(ξ)) dμ_a(ξ) or Φ(F) = log Σ_n w_n e^{⟨F, φ_n⟩}, with ψ convex, μ_a ≥ 0 and
w_n ≥ 0 built from a weight a. Then D²Φ(F_0) ⪰ 0 at every base point where the expressions and
their derivatives are defined, for every weight with μ_a ≥ 0 (respectively w ≥ 0). This includes 2Λ only
if the construction preserves those hypotheses there. The lemma does not exclude a specific identity that
identifies this positive Hessian with a_T for Λ and fails for a falsifier.

*Proof.* In the first case, D²Φ(F_0)[H,H] = ∫ D²ψ(F̂_0)[Ĥ,Ĥ] dμ_a ≥ 0. In the second, the Hessian is the
covariance of ⟨H, φ_n⟩ under the law proportional to w_ne^{⟨F_0,φ_n⟩}, which is ≥ 0. ∎

Applications:
- The ratio channel S2, seen as the quartic functional F ↦ ∫|F̂|⁴|A|², is of the first type, with μ = |A|²dξ ≥ 0
  for every weight. Its Hessian at 0 vanishes, and at other points it is ≥ 0 and blind.
- The second type is the variance N5 (R5-e).
- If convexity is certified by a supremum of affine functions indexed by factorizations, each branch is linear in the
  weight: G3 §4B, J2.

The two sources of Lemma K give positive Hessians under their hypotheses, but their identification with a_Λ
has not been built. This is absence of an object at selection, not a universal exclusion.
In particular, that the auxiliary Hessian remains positive under a falsifier does not prevent the
equality with the target form from failing there.

## 5. Candidates

**No candidate passing the gate was obtained.** It is not claimed that O13, O14 and a nonlinear odd
branch of O2 exhaust the open operations. The restriction to those three possibilities depended
on the undue generalization of T5 and on the use of auxiliary blindness as an exclusion.

An explicit block, Hessian or mixed square may be admissible if its complete identity
with a_Λ and its sign on the carrier are proved. It is not required that the auxiliary object lose positivity
at c=2: only the identity may fail. No such construction has been provided here.

Warning (PROVED, trivial). If B(A_M) = f(A_M) with f ≥ 0, then ⟨A_MG, f(A_M)G⟩ = ∫ λ f(λ) dE_G(λ), whose sign
is that of A_M on the support of f. Every Φ of this form is a reformulation (B3). A B that does not commute with A_M falls
into the Lyapunov format of ROUND_012_A Prop. B.

## 6. Claims and labels

| # | Claim | Label |
|---|---|---|
| 1 | Lists S and W with file, section and blindness status | CITED (column by column); the observation of §1 is ARGUED |
| 2 | S2 ≥ 0 and S7 ≥ 0 for every real (respectively nonnegative) weight | PROVED (trivial) |
| 3 | Table O1–O14: antecedents and reasons | ARGUED (cross-check; not exhaustive) |
| 4 | O6: the Mourre/virial format is the Lyapunov format with M = −2iA | PROVED (⟨F,i[H,A]F⟩ = 2 Im⟨HF,AF⟩ for F in the domain) |
| 5 | Lemma T | PROVED in the class 𝔐 |
| 6 | (T2), (T3) | PROVED (T3 from Lemma A of R9-b and Lemma C (α), (β), CITED) |
| 7 | (T4): the effective restriction has to be (PC) | PROVED within the inventory of Lemma C; exhaustiveness ARGUED |
| 8 | (T5): parity of the canonical square and its sums with sign-independent coefficients; no universal extension to mixed squares | PROVED in the cited class; scope corrected |
| 9 | §4.1: the flow in T gives the wrong arrow; the pair with Son_{S(T)} is R186_029 | PROVED (inclusion) / CITED |
| 10 | Lemma K | PROVED |
| 11 | Warning of §5 (commuting f(A_M) ⇒ reformulation) | PROVED (trivial) |
| 12 | Candidate passing the gate: none | selection NO-GO |
| 13 | Global sign of a_T | OPEN |

For independent verification, the following must be rederived: Lemma T and its application to battery E; Lemma K (both cases); the
identity of O6; and claim (T4), i.e. that no relation of ℛ outside (PC) fails simultaneously under the three
checks (this is the weakest piece, because it depends on the ARGUED exhaustiveness of Lemma C of ROUND_010_A).
