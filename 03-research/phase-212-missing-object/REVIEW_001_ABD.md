# Review of the selection memos ROUND_001_A, ROUND_001_B and ROUND_001_D

Reference target (★): λ_A(T) ≥ 0 for every T > 0, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md`. Each proof was redone and cross-checked against
P46 (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`: sec:firstcontact, thm:PCfinite, prop:GEgap,
prob:annihilate, prop:annihilate-equiv, rem:returnremarks, prop:opcalc, thm:sos, rem:sosatoms,
prop:nearfree, rem:boxes, thm:oneprofile, prop:AM, lem:shape-scale, thm:geo-split), against 211/LEDGER
(C6, C7, C9, C33b, C49), against `phase-186-toolbox/R186_005` and `R186_092`, against the routes index and against
phase 170 (`phase-170-global-prime-inequality/R170_811`–`R170_862`), which none of the three memos cites.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. The computations of this
review are single-point checks and prove nothing.

Summary of verdicts.

| Memo | Verdict | Most serious defect |
|---|---|---|
| A (K1) | ACCEPT with corrections (major ones in the cross-check and in the scope) | Lemma A(2) is empty in the formal algebra (there A = 0) and the sentence "the orientation enters exclusively through the defects" is false; the cross-check omits phase 170, where the "missing piece" is already recorded |
| B (K2) | ACCEPT with corrections | The reading of Prop. 5 ("there is no formula for the pivot obtained via Λ∗1 = log") is a non sequitur that the memo's own Prop. 6 contradicts; the "it has been proved" of the Result rests on a NUMERICAL datum |
| D (K4) | ACCEPT with corrections | Case (iv) of Theorem B is not a NO-GO, not even a conditional one, in the stated generality: there are true PROVED instances |

None of the three conclusions "no new mechanism" is an impossibility, and none should
be recorded as such. The three memos say so in their result section, but all three contain
sentences that contradict it (pointed out below).

---

## 1. Memo A

### 1.1 Verification of the statements

**Relations against P46.** The definitions agree with P46 (l. 6627–6665): X, 𝓕 = u_∞(D)J,
𝓕* = 𝓕⁻¹ = 𝓕, JV_aJ = V_{−a}, X + 𝓕X𝓕 = 𝓜, S_N, S′_N, L_M, A_M, E_N = S_N𝓕 − JS_N,
H_{M,N} = L_MS_N − S′_N. Relations (b) S𝓕 = JS and (c) [X,S] = −LS are E = 0 and H = 0. Correct.
Relation (a) J𝓜J = 𝓜 is the parity of m. Correct.

**Lemma A(1).** Redone: S𝓜𝓕 = SX𝓕 + S𝓕X = (XS + LS)𝓕 + JSX = XJS + LS𝓕 − XJS + L^♭JS
= (L + L^♭)S𝓕. Correct. Hypothesis (a) is not used in (1). With defects the same computation gives
S_N𝓜𝓕 = JS′_N + S′_N𝓕 + {X,E_N}, which is the proof of thm:PCfinite. PROVED.

**Lemma A(2).** The four checks ((𝓕°)² = 1, (b), (c), (a)) are correct. Moreover the
substitution respects the unlisted relation 𝓕t = t^♭𝓕 (t ∈ 𝒯; u_∞(D) commutes with translations) and
is compatible with the involution * of the realization (X* = X, J* = J, 𝓕* = 𝓕, t* = t^♭). PROVED as an
algebraic statement. Defects:

- **E-A1 (scope; §3, "Reading" of Lemma A, and §2(iii)).** In the universal algebra defined by the
  relations of the lemma, part (1) gives A = 0. Then "A ↦ −A" is 0 ↦ 0 and the bold sentence "the
  formal algebra of the three inputs contains no orientation, in any degree" is a triviality:
  in that algebra every identity A = ΣV_i*V_i + ρ says 0 = ΣV_i*V_i + ρ. Statement (2) adds
  nothing to (1) as long as the relations are exact.
- **E-A2 (the case with defects is neither proved nor stated).** What matters is the version with
  truncations. There (b) and (c) are not relations: they define E_N and H_{M,N}. The mirror tuple
  (X, J, J𝓕J, S°, −L_M) satisfies thm:PCfinite with A_M ↦ −A_M for **any** S° ∈ 𝒯 (including
  S° = S_N), with E° := S°J𝓕J − JS° and H° := −L_MS° − S°′. The "Möbius comb" only intervenes in
  where H° vanishes: with S° = Φ_{≤N}(μ) and M ≥ N, H° has no coefficient at k ≤ N (because
  μ·log = −Λ∗μ) and outside, its coefficients −Σ_{dm=k, d≤M, m≤N}Λ(d)μ(m) have no sign (NUMERICAL, M = 9,
  N = 6: between −1.95 and +2.71). The correct statement is Lemma A′ of §1.3. It is a reformulation of
  the observation of P46 after thm:PCfinite (invariance of the square under A_M ↦ −A_M; code F2); it does not
  go beyond it.
- **E-A3 (false claim; §3, "Reading", and §4 first sentence).** "The orientation enters exclusively
  through the asymmetry of the defects" is false. The mirror image also does not share: Λ ≥ 0 coefficient
  by coefficient (weights −Λ), b ≡ 1 ≥ 0 (versus μ), and the positivity of the Lévy measure K(u) > 0
  of m (STATEMENT §1; the image has −m). None of the three is a defect of (b) or (c): they are
  properties of the realization that the relations (a)–(c) do not express. h_{M,N} ≥ 0 is a consequence
  of the first. The list (α), (β) of §4 is consequently incomplete.
- **E-A4 (the algebra is underdetermined).** The relations (a)–(c) omit the grading of 𝒯 by
  log ℕ, Φ(α)Φ(β) = Φ(α∗β), [X, V_a] = aV_a and 𝓕t = t^♭𝓕. The symmetry respects them, so the
  conclusion does not change, but "every identity formally deduced from (a), (b), (c)" should be read as
  "every polynomial identity valid in every realization of the relations, without using any
  coefficient inequality or the form of E, H".

**Lemma B.** Redone: [X,H] = −L′_MS_N − L_MS′_N + S″_N and S′_N = L_MS_N − H give
H⁽²⁾ = L_MH − [X,H]. Checked on coefficients with arbitrary weights (NUMERICAL, M = 9, N = 6, error
10⁻¹⁵). PROVED. Consequences (1)–(3) correct. (4) is correct with the definition
P_{j+1} := L_MP_j − [X,P_j], H^{(j)} := P_jS_N − S^{(j)}_N, which gives H^{(j+1)} = P_jH − [X,H^{(j)}]; the
memo does not write that definition: ARGUED as it stands, PROVED with the added line. Defects:

- **E-A5 (truncation).** "Arbitrary weights and truncations" holds for the truncation
  (L′_M + L_M²), which is Φ(Λ_{≤M}∗Λ_{≤M}) and not Φ_{≤M}(Λ∗Λ). With the latter another defect appears with
  support in (M, M²]. Specify.
- **E-A6 (serious overreach; "Concrete next step", first sentence).** "Do not relaunch K1 with another
  relation of the Dirichlet ring (degree three, Vaughan, convolution identities): Lemma B
  derives them from (c) and Lemma A removes their orientation." Every true statement about Λ derives from
  Λ∗1 = log, because that identity defines Λ. "Is a consequence of (c)" excludes nothing and cannot
  be used as a closure criterion. What Lemma B proves is narrower: the truncated defect of
  degree j lies in the ideal generated by H, [X,H], …, and vanishes at k ≤ N when H vanishes. It does not say
  that a degree-two use lacks sign content: it says that it does not introduce a new defect.
  The sentence must be withdrawn from the record.
- **E-A7 (uncited antecedent).** The content of Lemma B and of its consequence (1) is in
  `R170_851` §§0–2 (Selberg collision; the synchronized channel vanishes at k ≤ N and keeps only the
  incomplete hyperbola) and `R170_841`. It is not a new piece.

**Lemma C.** Redone. The atom of ΣV_i*V_i at log(3/2) comes only from L*L with (n,m) = (3,2)
(2n = 3m with n, m prime powers forces n = 3, m = 2), equals (log 2·log 3/√6)Σ(|β_i|² + |γ_i|²), and
the isolation of atoms is that of rem:sosatoms (l. 8469–8474), which applies to the even real part of the
measure. The strict inequality T > ½log3 is the correct one for L = Φ_{<N}(Λ). PROVED (with CITED).
It is rem:sosatoms with coefficients; the memo says so. Scope: degree-one squares with scalar
coefficients; it says nothing about V_i with X, J, 𝓕.

**§2(iv), signature identity.** Wrong by a factor 2 (l. 125). Expanding the right-hand side
gives ½(u(λ) + u(μ)). The correct identity is
u(λ) + u(μ) = (1/ε)(1 + εu(λ))(1 + εu(μ)) − 1/ε − ε u(λ)u(μ). The conclusion (signature (1,1) of the
kernel u⊗1 + 1⊗u for non-constant u) is correct. The PROVED label of the summary ("What was proved",
last item) stands only with the corrected formula.

**§1(5), cΛ and a_P.** δ(k) = (c − 1) log k and, for a_P with P > N, δ(k) = −log k at k ≤ N: correct
(NUMERICAL, c = ½ and c = 2). But the memo does not extract the useful consequence: see R1 in §4.3.

**§5, battery.** The sentence about quartets and f_t is labelled ARGUED by the memo itself; correct.

### 1.2 Cross-check and citation errors

- **E-A8 (major omission in §0 and §1(1)).** Phase 170 worked out exactly the pairings of
  thm:PCfinite: `R170_816` §2 (equation (2): ⟨JH_{M,N}F, g⟩ = 0 by support; (3)–(4): exact exit
  from the identity with h_{M,N} ≥ 0), §3 (two-sided bound with loss √N), §4 (explicit falsification of the
  step "h(k) ≥ 0 ⟹ the pairing is ≥ 0"), §6 (oriented separation of the channel d = 2: two
  unsigned Fourier correlations remain); `R170_819`–`R170_823` (PC at two scales, the divisorial cancellation
  survives the dilation); `R170_837`, `R170_843`, `R170_847`–`R170_856`. The memo does not cite them and
  presents §4 as "missing piece, pinpointed precisely". The routes index has the row
  G4A-R161_001-002 (catalogue 04, l. 759) but no rows for R170_811–R170_840; that gap in the
  index explains the omission and must be repaired (§4.5).
- **E-A9 (improper identification; §4, last sentence).** "Converting them into diagonals is exactly what
  conditions (ii)–(iii) of prob:annihilate ask for … and prop:annihilate-equiv identifies it with
  (★)." prob:annihilate asks for 𝒪_LF = 0 for first-contact vectors, with minimality of the
  window (i) as an ingredient; it mentions neither h_{M,N} ≥ 0 nor a diagonalization. The identity of §4
  is of another kind: it holds on all of P_T and does not use first contact. That both imply (★) does not make them
  the same question. What P46 does record about diagonalization is in rem:returnremarks
  (l. 6940–6943): the variance indexed by divisor paths is not the norm of the coherent sum
  in k, which contains cross Gram terms between distinct k; additive phases diagonalize in k
  but do not factor through de = k, and multiplicative characters factor but change the operator.
  That is the pertinent citation and the memo does not give it.
- Citations checked and correct: P1_BBSTAR_001 §2.8 and Theorem P1.A; README index Prop N.2; R162_2301
  Lemma S; thm:sos and its extension; observation after thm:PCfinite. N_BUILD_018/019/022
  and ROUND_023_A were not checked.

### 1.3 Corrected statements

- **Lemma A′ (PROVED).** (1) In every algebra with the exact relations of Lemma A, 𝓜 = L + L^♭.
  (2) For any M, N and every S° ∈ 𝒯, the tuple (X, J, J𝓕J, S°, −L_M) satisfies the identity
  of thm:PCfinite with A_M replaced by −A_M and defects E° = S°J𝓕J − JS°, H° = −L_MS° − S°′.
  Consequence: a polynomial identity deduced from thm:PCfinite that treats E_N and H_{M,N} as
  symbols does not determine the sign of A_M. Scope: algebraic identities that use no
  property of E_N, H_{M,N}, Λ, b ≡ 1 or K beyond the relations. It is not a NO-GO for any
  class of constructions: every construction using Λ ≥ 0, K > 0, the support of H or the rank of E_∞
  falls outside.
- **Lemma B (PROVED, not new: R170_851).** As in the memo, with the truncation specified and the
  degree-j recursion written.
- **Lemma C (PROVED with CITED).** As in the memo.
- **Observation D.** ARGUED; kept as such.

### 1.4 Does it close the design question?

It closes one thing: the degree-two relation does not contribute a defect independent of the degree-one one and, in
the class of multipliers, does not complete a square (thm:sos, P1_BBSTAR §2.8, Lemma C). It does not close
K1 as a conjunction separator + Poisson + archimedean factor with a nonlinear step; the memo says so in
"Result" and contradicts it in "Concrete next step" (E-A6). The concrete gap is the common
residue, treated in §4.

### 1.5 What may be recorded

Routes index and grid, admissible wording:

> "Degree-two relation of the Dirichlet ring as a nonlinear step together with thm:PCfinite: no
> new mechanism. PROVED: the truncated degree-two defect is L_MH − [X,H] (already in R170_851); the
> identity of thm:PCfinite admits a mirror tuple with A_M ↦ −A_M, so that no
> polynomial consequence treating E_N, H_{M,N} as symbols fixes the sign (reformulation of F2);
> degree-one squares in (L, L*) with atoms in log ℕ are constant for T > ½log3 (rem:sosatoms).
> Not a NO-GO of the conjunction (E)∧(F)∧(I). Antecedents: R170_816, R170_819–823, R170_851,
> P46 rem:returnremarks."

It may not be recorded: "no formal consequence of the three relations is oriented" without the
scope clause (row K1 of the phase LEDGER says it this way and must be corrected); "the orientation
lives only in the defects"; "do not relaunch with degree three, Vaughan or convolution identities";
any wording presenting Lemmas A, B, C as an obstruction to an object that uses Λ ≥ 0 or K > 0.

---

## 2. Memo B

### 2.1 Verification of the statements

**Prop. 1.** Correct. It is missing the declaration of β > 0 as step j = 0 of (a) (the memo uses it: "β = π(∅; n_1) >
0"). PROVED, reformulation.

**Prop. 2.** Correct (density of ℤ log p + ℤ log q, continuity of 𝖡, thm:oneprofile). Does not require
2T_0 < log 2. PROVED, reformulation.

**Prop. 3.** Correct as a statement: it is the Kolmogorov uniqueness of the realization of a positive
semidefinite kernel. Defects:

- **E-B1 (hidden hypothesis).** The existence of r presupposes that 𝖡 is positive definite, i.e.
  (★). Without it the proposition is empty; in spaces with an indefinite form uniqueness fails in
  general. It must be stated as "if it exists".
- **E-B2 (reading exceeding what is proved; "Reading" of §2 and "What failed", first item).** "The identity
  (G) has, if it exists, a single solution up to isometry" holds only for the complete realization with
  zero remainder on the carrier of a profile; the split between ‖V_TF‖² and ρ_T is not unique. And
  uniqueness up to isometry holds for every positive semidefinite kernel: it does not distinguish one explicit
  presentation from another nor say anything about which one exists. "K2 is not a reduction of (G), it is (G) with an
  added shape condition" is correct as a classification (reformulation, B3), not as an obstacle.

**Lemma 4.** Redone and checked (NUMERICAL, divisor-closed set of 9 elements, error
10⁻¹⁵): 𝕍_a = 2U⁻¹[D,U]; U Div_a U^⊤ = DG + GD − 2UDU^⊤; formulas for G and for Z Div Z^⊤. The units
for cΛ (d_c) and a_P (indicator of P-rough numbers) are correct. PROVED. Agrees with (𝕍_M)_{mk} = v_{m/k}
of prop:AM(iii).

**Prop. 5.** Correct (standard linear algebra; C_f is triangular in the order of every divisor-closed
chain). PROVED. Main defect of the memo:

- **E-B3 (non sequitur; "Reading" of §3, bold sentence, and "What failed", second item).** From "the
  pivots are invariant under unipotent triangular congruences" the memo concludes "there is no
  formula for the pivot obtained via Λ∗1 = log in this class". It does not follow. The pivots are invariants
  of the matrix; every LDL^⊤ factorization **is** a unipotent triangular congruence exhibiting them.
  Invariance does not prevent a congruence from making them visible: that is how they are computed. The
  memo's own Prop. 6 is the counterexample: [log gcd(m,k)] = E diag(Λ) E^⊤ is the identity
  Σ_{d|n}Λ(d) = log n used as a congruence by E⁻¹, a unipotent element of the incidence algebra, and
  gives the pivots Λ(n). What §3 proves is only this: the congruence by Z does not diagonalize 𝔸_𝒩;
  it transforms Div into DG + GD − 2ZDZ^⊤ and leaves Arch and Near untreated. Whether another unipotent congruence
  (from the incidence algebra or not) takes 𝔸_𝒩 to a manifestly positive form is the open
  question, not a closed one.
- **E-B4 (label; "Result", last sentence; "What was proved", Prop. 6 and (4.1)).** "It has been proved that
  the three sources of explicitness … do not produce it." For the incidence pattern, what is PROVED is the
  necessary condition (4.1); its failure is NUMERICAL. This review checked it in the minimal case
  𝒩 = {1,2,3} with the profile a = 0.15, b = 1 (NUMERICAL, c_0(0) = 1): β·𝖡(log(3/2)) = 0.1435 versus
  𝖡(log 3)·𝖡(log 2) = 0.3888; it also fails at (4,3), (5,2), (5,3), (5,4). The exclusion of the incidence
  pattern remains a NUMERICAL NO-GO on one profile, not PROVED. A computation-free proof that
  (4.1) fails would require a lower bound on β − |𝖡(log k)| that is not available without estimates.
  For the substitution by Z, what is proved is what E-B3 says. For the product over primes (Prop. 8)
  the claim is correct in the model without Near, which the memo acknowledges does not describe 𝔸.

**Prop. 6.** Correct. Note: on an 𝒩 containing 1 the matrix [log gcd] is singular
(pivot Λ(1) = 0 and Λ(n) = 0 outside prime powers); "pivots Λ(n) ≥ 0" should be read with the
factorization E diag(Λ) E^⊤, not with quotients of minors.

**Prop. 7.** Redone: π(S;n) ≤ 𝔞(e_{log n} − e_{log k}) = 2[β − 𝖡(log n − log k)]; for
d < log 2 − 2T_0 there is no comb; 1 − cos x ≤ x²/2 gives κ_0d². Checked at three points (NUMERICAL:
d = 0.01, 0.03, 0.08; 2(β − 𝖡(d)) = 0.041, 0.311, 1.544 versus κ_0d² = 0.046, 0.411, 2.925).
PROVED. Defect:

- **E-B5 (reading).** "The pivot recursion has no uniform margin at any late step" is a
  normalization effect. The bound κ_0d² is the squared distance between two neighbouring translates and
  holds equally for the archimedean form alone. The quantity with content is the ratio
  π(S;n)/(2[β − 𝖡(log n − log k)]) ∈ [0,1] (or the pivot relative to the archimedean pivot), about
  which Prop. 7 says nothing. "Identical for every comb" describes the bound, not the pivot. The memo says
  it is not a NO-GO; the reopening condition ("a numerator vanishing to the required order") does
  treat it as a hard restriction and must be downgraded to an observation.

**Prop. 8.** Correct. Agrees with rem:boxes (Kronecker sum of single-prime Toeplitz
matrices). PROVED.

**Cross-check with 211.** C49 and C9 are cited in accordance with the LEDGER (C49: PROVED NO-GO of the Schur product
local × archimedean; C9: weighted diagonal dominance reduces to Σ_{n|m}Λ(n) = log m). C6 and C7
appear as NOT STARTED, as the memo says. The proposal "close 211/C6 with the same reference" is not
warranted: C6 remains "without mechanism in the multiplicative order", not closed.

**Inherited NUMERICAL datum.** The memo uses from STATEMENT_001 §3 the values β = 0.01492 and
|𝖡(d)| ≤ 0.0122 on 0 < d ≤ 13. This review reproduces β = 0.014923 only **without** normalizing F_0 (with
‖F_0‖ = 1, as the text of STATEMENT §2 says, β = 0.8973), and obtains 𝖡(log 6) = 0.01373 on the same
scale (0.8253 normalized), larger than 0.0122 and smaller than β (NUMERICAL, two meshes). The memo's
argument for (4.1) does not depend on it (it only needs a value smaller than β), but the bound 0.0122 of
STATEMENT_001 must be rechecked and its normalization clarified.

### 2.2 Corrected statements

- Props. 1, 2, 4 (Lemma), 5, 7, 8: PROVED as they stand, with the precisions above.
- Prop. 3: PROVED, conditional on 𝖡 being positive definite.
- (4.1): necessary condition PROVED; failure NUMERICAL (case {1,2,3} and four other pairs).
- Reading of §3, corrected: "The congruence by Z = C_z, which realizes Λ∗1 = log on Div, does not
  diagonalize 𝔸_𝒩 nor change its pivots; no explicit unipotent congruence that does so is known.
  OPEN."

### 2.3 Does it close the design question?

No. It establishes that K2 is a reformulation (Props. 1–3) and that three concrete attempts at
explicitness do not work (one of them only NUMERICAL). Gaps the memo does not examine:

1. Unipotent congruences outside the incidence pattern, or triangular with respect to an order that
   is not divisibility. The memo's reopening condition excludes them verbally ("that is not
   a triangular congruence in the divisibility order") relying on E-B3; it must be inverted:
   they are precisely the unexamined terrain.
2. The piece 2ZDZ^⊤ = [2(mk)^{−1/2}Σ_{d|gcd(m,k)} d log d] that Lemma 4 extracts from −Div is positive
   semidefinite and is written as a sum of squares (gcd paradigm with g(d) = d log d). The memo does not
   point it out. It is generic in the comb (UDU^⊤ ⪰ 0 for every unit u), so by itself it is not a sign
   step (B1); but Z𝔸Z^⊤ = Z(Arch − Near)Z^⊤ + 2ZDZ^⊤ − (DG + GD) is an exact identity where
   u ≡ 1 enters in G and in ZDZ^⊤, and the memo does not analyse the term −(DG + GD) against Z·Arch·Z^⊤. It is not
   proposed as a candidate: the operation that signs that remainder is missing and it does not pass the four-point
   filter (the antecedent is C33b and A_MU_FACTORIZATION §1(f), and no new mechanism is identified).
3. Relative pivots (E-B5).

None of the three is a candidate ready for construction. The conclusion "no new mechanism" is
correct; "the question should not be relaunched" (end of §0) exceeds what is proved.

### 2.4 What may be recorded

> "K2, Schur pivots by multiplicative nesting of indices: no new mechanism; reformulation
> (positive pivots along an exhausting chain ⟺ target up to a zero pivot). Tools
> PROVED: comb = 2U⁻¹[D,U] in the incidence algebra (valid for every comb; u ≡ 1 ⟺ Λ);
> bound π(S;n) ≤ 2[β − 𝖡(log n/k)] ≤ κ_0 log²(n/k), independent of the comb; Schur complement of
> a Kronecker sum. A triangular factor with incidence pattern would require
> β𝖡(log m/k) = 𝖡(log m)𝖡(log k) on coprime pairs, which fails (NUMERICAL). Not a class NO-GO;
> congruences outside the incidence pattern not examined."

It may not be recorded: "pivots invariant under the unipotent incidence group" as a reason for
closure; "the same realization (Prop. 3)" as an obstruction; the closure of 211/C6; "it has been proved that
the three sources of explicitness do not produce it".

---

## 3. Memo D

### 3.1 Verification of the statements

**Lemma 1 and Corollary 1.** Redone: support, conditions A = B = 0, c_F = 2c_φ + ε c_φ(· − u)
+ ε c_φ(· + u), separation |log n − log n_0| > 1/N > 2η. Correct. PROVED.

**Lemma A.** (i) κ_n = Σ_{d|n, d≥2}(x_d − Λ(d)) and Möbius inversion: correct. (ii) and (iii):
correct. PROVED. Actual scope: (ii) is the tautology "a polynomial vanishing at a point lies in
the maximal ideal of the point", with the **complete** set of atoms 2 ≤ n < N. It is not a statement
about inequalities or about positivity certificates. The "Reading" ("a nonlinearity in Λ that
decides the sign must lie in the coupling of Λ with F") does not follow from the lemma: it is ARGUED and
coincides with clause O2 of OBJECT_SPEC.

**Transfer principle.** Correct in the declared class. PROVED.

**Theorem B.** (i), (ii), (iii): correct; (ii) does not use the sign of λ_A (recession direction of an
unbounded closed convex set and Corollary 1). PROVED. (iv): the two inequalities are correct consequences
of (MS) (the second, by Cauchy–Schwarz in q_± ≤ 2a_T). PROVED as implications. Defects:

- **E-D1 (wrong label; "Status of case (iv)/(c)", "Conclusion of §3", §7 (P2), §8).** Case
  (iv) is labelled "CONDITIONAL NO-GO" and "not a reasonable target". In the generality of
  Theorem B (any closed convex K) it is false that it is a NO-GO: let T ≤ ½log5, where
  λ_A(T) > 0 (PROVED, P46 thm:log5A and monotonicity), E = ∅ and K the closed ball of radius r around Λ.
  Then Π is bounded, Π ≠ {Λ}, and for r·Σ_{n<N}2n^{−1/2} ≤ λ_A(T) one has
  a_T^λ(F) ≥ (λ_A(T) − r Σ 2n^{−1/2})‖F‖² ≥ 0: (MS) is true. Case (iv) is "target with
  margin", whose truth depends on the size of the polytope relative to the margin; the correct label is
  OPEN in general, true for small polytopes where there is strict margin, and CONDITIONAL
  (false under the hypothesis W[δ](F_⋆) ≠ 0 and s|W[δ](F_⋆)| > λ_A(T)) only for polytopes of fixed size
  such as those of K_0. The trichotomy stated in the summary ("either it is false, or it is identification, or it requires
  margin") is correct; what is incorrect is calling the third arm a NO-GO.
- **E-D2 ("strictly stronger").** The memo defines the sense (there exists F with h_Π(F) > 0), and in
  that sense it is correct. It is not proved that (★) at T does not imply (MS): by E-D1, with strict
  margin it implies it for small polytopes. Replace by "implies (★) at T and adds the inequality
  s|W[δ](F)| ≤ a_T(F)".
- **E-D3 (overreach; opening summary (b) and §0(3)).** "Closes that direction as a source of sign" and
  "no E turns it into a mechanism". Arm (iii) (Π = {Λ}) is not closed: it is the case in which
  the class restricts nothing, and by Corollary C(b) it is reached with a very partial E (it suffices, for
  N ≤ X², to have an n ∈ E with p^j ∥ n for each prime power p^j ∈ [X,N)). What §3 proves is
  that a deduction with Π ≠ {Λ} is either false or pays margin. That is a classification, not a closure.

**Corollary C.** (a) Redone: the recession cone is D(E) ∩ K_0 and a δ ≥ 0 with Σ_{d|n}δ(d) = 0
vanishes at the divisors of n. Correct. (b) Redone: for n < N ≤ X² the prime powers ≥ X that
divide n are of a single prime; the system decouples into partial sums per tower; unique
solution ⟺ 𝒯_p ⊂ J_p(E). Correct. (c) Correct, including the segment |s| ≤ log p and the exhibited
inequality. PROVED. Note: the inequality of (c) can be refuted or confirmed in a concrete window
(for example p = 2, a = 2, X ∈ (2√2, 4), N ≤ X²), which would decide arm (iv) for K_0 in that
window; this was not done.

**Observations 1 and 2.** Redone: N_λ(q_1q_2) = λ(q_1)λ(q_2)/(log q_1 log q_2) for distinct primes
and λ supported on prime powers; the hyperbola is not convex but it is unbounded and the argument
with Lemma 1 at n_0 = q_1 holds. Correct. PROVED.

**Proposition D.** Redone and checked (NUMERICAL: X = 7, N = 49, every n ∈ [7,49)). (E2), the
triangularity of 𝖳 (n/k ∈ [X,N) because k ≤ n/X) and (I2) are correct. PROVED. "What (I2) does not give":
(1) and (2) correct; (3) is the tautology that (I2) rewrites the same weight vector.

**Cross-check with R186_005 / R186_092.** The citations are faithful: Lemma S0 (generalized Selberg identity
with own system), Lemma S1 (triangularity), TB3-neg, the residue "completeness beyond X that is
not total identification: OPEN", and correction M5.1 of R186_092 to item (ii). Corollary C(a)
and Observation 1 give a direct proof of what corrected TB3-neg(ii) asserts in the class
of completeness atoms; it is consistent with R186_092.

**Cross-check with P46.** thm:geo-split(i) says what the memo attributes to it (the sign in the class is the
sign at Λ plus an unsigned rigidity), but with its own hypotheses (functional Δ, unit
minimizer F_⋆); the sentence "by thm:geo-split its sign content is the sign at Λ" is a correct
analogy, not an application: Theorem B(i) already says it by itself and the citation can be removed.
lem:shape-scale: "proved for c large and small, conditional for O₄^ε"; the memo does not cite it falsely.
cor:margin1 is used only in the conditional arm.

- **E-D4 (class narrower than the title).** The title speaks of "Λ beyond the window", but
  the class of §3 only admits weights in [2,N) and atoms in E ⊂ [X,N). Premises involving
  Λ(d) with d ≥ N (such as the coefficients h_{M,N}(k) with M > N of thm:PCfinite) are not in the class.
  The extension is immediate (variables in [2,N′), projection of Π onto [2,N), which is still
  convex) and Theorem B applies to the projection; this should be stated.
- **E-D5 (cross-check).** It does not cite phase 170 either (`R170_819`–`R170_823`, PC at two scales), which is the
  direct antecedent of the "design X → X²" with the Poisson–Chebyshev identity.

### 3.2 Corrected statements

- **Theorem B (PROVED).** (i)–(iii) as in the memo. (iv): "If Π is bounded and Π ≠ {Λ}, (MS) is equivalent
  to positivity at the extreme points, implies (★) at T and the inequalities
  s|W[δ](F)| ≤ a_T(F), s|W[δ](F,G)| ≤ 2(a_T(F)a_T(G))^{1/2}. Conversely, if λ_A(T) > 0 and
  sup_{λ∈Π}Σ_n 2n^{−1/2}|λ(n) − Λ(n)| ≤ λ_A(T), (MS) holds." Status of arm (iv): OPEN; true in
  the instances of the converse; CONDITIONAL-false for K_0 under the hypothesis on the minimizer.
- **Conclusion of §3.** "Classification PROVED. NO-GO PROVED only in the unbounded arm
  (Theorem B(ii), Corollary C(a), Observation 1). The identification arm is the target without
  added restriction. The polytope arm is a target with margin, not a NO-GO."
- Lemma A, Corollary C, Proposition D: PROVED as they stand.

### 3.3 Does it close the design question?

It closes the cell "partial completeness beyond X" in a precise sense: in the class of
linear atoms with convex K, a completeness premise that does not identify Λ is either false (PROVED)
or asks for margin. That answers R7 better than the previous state ("OPEN; no candidate"). It does not close:
the identification arm (which is where any object satisfying O4 lives); the polytope arm;
non-convex classes; premises that are not properties of the comb. Statement (P1) of §7 is O2 ∧ O4 of
OBJECT_SPEC and is not a result. I do not see an object that satisfies OBJECT_SPEC §1 and escapes the lemmas
of the memo, because those lemmas exclude no object of the identification arm.

### 3.4 What may be recorded

> "O166.802.1, partial completeness beyond X (linear atoms Σ_{d|n}λ(d) = log n on E ⊂ [X,N),
> convex restriction K): classified. Π(E,K) unbounded ⟹ the class contains a comb with negative
> form (NO-GO PROVED, without using the sign at Λ); for K_0 this happens if and only if some prime
> power in [X,N) divides no element of E. Π = {Λ} ⟹ the statement is the target at T
> (for N ≤ X² and K_0: if and only if each p^j ∈ [X,N) exactly divides some n ∈ E). Π bounded
> ≠ {Λ} ⟹ target with margin s|W[δ](F)| ≤ a_T(F): OPEN, true for small polytopes where
> λ_A(T) > 0. The two-scale degree-two identity is linear in the new contacts for
> N ≤ X² (PROVED). Live residue: total identification with nonlinearity in the weight–vector coupling
> (O2 ∧ O4)."

It may not be recorded: "NO-GO (class) … CONDITIONAL in (iv)"; "closes the direction as a source of
sign"; "not a reasonable target"; "no E turns it into a mechanism".

---

## 4. The common residue of memos A and D

Stated in A §4 and taken up in D §8(3) and in row K1 of the phase LEDGER: an identity

    a_T(F) = ‖V_TF‖² + Σ_{k>N} h_{M,N}(k) |ℓ_k(F)|² + (polar terms as squares),
    h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0,   M ≥ N,

that converts into diagonals the pairings of H_{M,N} and E_N of thm:PCfinite.

### 4.1 Is it well stated?

The formula for h_{M,N} and its support in k > N agree with thm:PCfinite (l. 6673–6678); the rank two
of E_∞ on the Schwartz kernel is correct (for F(t) = e^{t/2}f(e^t), SF − JS𝓕F
= ½e^{−t/2}f̂(0) − ½e^{t/2}f(0)). But as a target it is **underdetermined**:

- With ℓ_k ≡ 0 it is the identity (G) of OBJECT_SPEC §1. Without specifying where the ℓ_k come from it is not a
  statement different from (G) with a prescribed form for part of ρ_T. For it to be a residue and not
  a wish the ℓ_k must be fixed; the only thing thm:PCfinite offers is
  ⟨Y, V_{−log k}𝓕F⟩ with Y = (S_N⁻¹)*F, which is not a squared modulus.
- S_N⁻¹ is formal: the symbol Σ_{n≤N}n^{−1/2−iτ} is not uniformly bounded from below and
  P46 rem:Sren warns that S_N has no limit; the "solved" identity of A §1(4) is not defined
  as an identity of forms on P_T ∩ 𝒟_T. The memo marks it "formal" and does not resolve it.
- thm:PCfinite is an identity on the line; it does not contain the compression to the window. On the
  line, A_M has no sign (its symbol is negative on a nonempty set). The whole sign of a_T
  depends on F being supported in I_T, whereas 𝓕F and Y are not. The residue does not say how
  the support enters.

### 4.2 Is it recorded in the corpus?

Yes, in essence, and the memos do not cite it.

- `R170_816` §2: exact exit from the identity on window vectors, with ⟨JH_{M,N}F, g⟩ = 0 by
  support and C = Re⟨H_{M,N}𝓕F, g⟩ as the only hyperbola term; §3: only a two-sided bound, loss
  ≥ (log 2/2√2)√N with M = N²; §4: **explicit falsification** of "h(k) ≥ 0 ⟹ pairing ≥ 0" (two
  functions u, τ_au of small support); §6: oriented separation of the channel d = 2, leaving two
  unsigned Fourier correlations; §5 and §7: the missing correlation "would be exactly the new arithmetic
  law".
- `R170_819`–`R170_823`, `R170_837`, `R170_843`, `R170_847`–`R170_856`: two-scale variants,
  curvature, exterior Wronskian, Möbius extraction, Selberg collision.
- P46 rem:returnremarks: cross Gram terms between distinct k; additive phases versus
  multiplicative characters.
- P46 eq:Qbalance, eq:Qrecombine, eq:Qspectral: there already exists an exact identity with non-negative
  arithmetic coefficients paired with squared moduli of exterior functionals,
  c_{N,L}(F) = Σ_{m≤L} d_{m,N}|(𝒪_LF)_m|², d_{m,N} = Σ_{n≤N}Λ(n)n^{−(a_m+1/2)} > 0; and P46 proves that
  it is blind to the sign (holds for every eigenvector, with λ of either sign) and that Q_{N,L} admits no
  representation as a sum of squares on all of P_T.
- Routes index: row G4A-R161_001-002 (catalogue 04, l. 759). **There are no rows for R170_811–R170_840**
  (catalogue 04 jumps from R170_808 to R170_841). The phase 212 annexes inherit the gap
  (`ANNEX_INDEX_04.md` only mentions the row of phase 160/161).

The residue is therefore not a newly identified piece: it is the open obligation of R170_816 §5
transferred from "first-contact vectors" to "all of P_T", plus the requirement of diagonal form.

### 4.3 Does anything proved obstruct it?

There is no PROVED obstruction. The lemmas of A do not touch it (Lemma A′ leaves out every construction that
uses h ≥ 0; Lemmas B and C do not speak of it). Theorem B of D places it in the
identification arm (it uses all atoms k ≤ N), where there is no restriction. There are, however, four restrictions
that any version must satisfy; the first two are proved here.

- **R1 (PROVED, with CITED lem:shape-scale, proved part).** There is no family of identities
  a_T^a(F) = ‖V^aF‖² + Σ_{k≥2} h^a(k) q_k^a(F), valid for every weight a ≥ 0 in a cone containing
  {cΛ : c ≥ 1}, with q_k^a ≥ 0 and h^a(k) = Σ_{dm=k, d≤M, m≤N}a(d) − log k·1_{k≤N}.
  *Proof.* For a = cΛ, c > 1, M ≥ N: h^a(k) = (c − 1) log k ≥ 0 at k ≤ N and h^a(k) = c·h(k)
  ≥ 0 at k > N (NUMERICAL control, c = 2). The identity would give a_T^{cΛ} ≥ 0 on P_T, false for large c
  and T > ½log2 (lem:shape-scale; also Lemma 1 of memo D). ∎
  Consequence: the residue cannot be obtained from the version of thm:PCfinite with generic weights
  treating interior and exterior coefficients alike and specializing to Λ at the end. The
  terms at k ≤ N cannot enter as squares with the same pattern; the line that breaks for
  cΛ (clause O4) has to be that one, and it must also break for c < 1, where the interior defect
  is negative and restriction R1 says nothing.
- **R2 (PROVED; already in R170_816 (2)).** For F, G ∈ L²(I_T) and M ≥ N ≥ e^{2T}, ⟨G, H_{M,N}F⟩ = 0. The
  functionals ℓ_k(F) cannot be functionals of the compression of H to the window; they depend on F
  through non-local vectors (𝓕F, (S_N⁻¹)*F, exterior tails). The natural link is the exterior
  moments of P46 §collars, and there lies the warning of eq:Qspectral.
- **R3 (CITED, R170_816 §4 and rem:returnremarks).** Positivity of the coefficients does not sign a
  pairing between two distinct vectors, and the sum in k is coherent (cross terms between distinct
  k). A diagonalization requires an operation that identifies the two vectors
  JS⁻¹JF and S⁻¹JSF (formal) or that cancels the cross terms; none is written.
- **R4.** The identity must be sensitive to the support of F in I_T (§4.1, third point).

### 4.4 Four-point filter applied to the residue

(1) Closest antecedent: `R170_816` §§2–7; P46 thm:PCfinite, rem:returnremarks, eq:Qbalance.
(2) New object: none written; ℓ_k and V_T undefined. (3) Difference from the antecedent: global
form on P_T instead of the first-contact radical, which avoids needing minimality of
the window but does not avoid the recorded difficulty (pairing between two vectors, cross terms in k,
loss √N in absolute value). (4) Connecting identity: thm:PCfinite, which is bilinear and unsigned.
Conclusion: **it does not pass the filter**; it is not a candidate ready for construction. It is an
open cell with specification R1–R4, not a mechanism. Reopening it requires writing the operation of R3.

### 4.5 What to record

> "PC-diagonal residue: identity a_T = ‖V_TF‖² + Σ_{k>N}h_{M,N}(k)|ℓ_k(F)|² + polar terms. OPEN, no
> object. Antecedents: R170_816 (exact exit, falsification of h ≥ 0 ⟹ pairing ≥ 0, channel d = 2),
> R170_819–823, P46 rem:returnremarks and eq:Qspectral. Restrictions: it cannot be a specialization of
> an identity generic in the weight with interior and exterior coefficients treated alike
> (falsifier cΛ, c large; PROVED); the ℓ_k are exterior functionals (H vanishes compressed to the
> window; PROVED); an operation diagonalizing the cross terms in k is needed (not written). Do not reopen
> without that operation."

In addition: add to catalogue 04 of the index the missing rows for R170_811–R170_840, and correct
row K1 of the phase LEDGER ("the orientation lives only in the defects" → "in properties of the
realization that the relations do not express: Λ ≥ 0, b ≡ 1, K > 0 and the defects").

---

## 5. List of mandatory corrections before recording

| Ref. | Place | Correction |
|---|---|---|
| E-A1, E-A2 | A §3 Lemma A, reading; §2(iii) | Replace by Lemma A′; declare the scope |
| E-A3 | A §3 reading; §4 | Withdraw "exclusively"; add Λ ≥ 0, b ≡ 1, K > 0 |
| E-A5 | A Lemma B | Specify the truncation; write the degree-j recursion |
| E-A6 | A "Concrete next step" | Withdraw the prohibition of degree three / Vaughan / convolution |
| E-A7, E-A8 | A §0, §1(1), §4 | Cite R170_816, R170_819–823, R170_851; rem:returnremarks |
| E-A9 | A §4 | Withdraw the identification with prob:annihilate |
| — | A §2(iv) | Correct the factor 2 in the signature identity |
| E-B1, E-B2 | B Prop. 3 and reading | Make conditional on 𝖡 positive definite; downgrade the reading |
| E-B3 | B §3 reading; "What failed" | Replace by the corrected reading of §2.2 |
| E-B4 | B "Result"; "What was proved" | (4.1): NUMERICAL failure; withdraw "it has been proved" |
| E-B5 | B Prop. 7 reading; reopening | Downgrade to observation; invert the reopening condition |
| — | B "Next step" | Do not close 211/C6 |
| E-D1, E-D2 | D §3, §7 (P2), §8 | Arm (iv): OPEN / target with margin; add the converse |
| E-D3 | D summary, §0(3) | Withdraw "closes the direction" and "no E" |
| E-D4, E-D5 | D §3, §0 | Declare the extension to weights beyond N; cite R170_819–823 |
| — | STATEMENT_001 §3 (outside the memos) | Clarify the normalization of β and recheck the bound 0.0122 (NUMERICAL from this review: 𝖡(log 6) = 0.01373 on the same scale) |
