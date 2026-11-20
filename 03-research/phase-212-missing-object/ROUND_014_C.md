# Round 14, memo C: transition between windows that is not the inclusion

Notation of the common brief. a_T(F) = Arch_T(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n,
λ(T) = inf{a_T(F)/‖F‖² : F ∈ P_T, F ≠ 0}. Checks: 𝒞 = {2Λ, deletion of a prime power, Beurling}.

Idea submitted to the gate: a linear map Φ = Φ_{T→T′}: P_{T′} → P_T, different from restriction, with

  (E) a_{T′}(F) = κ·a_T(ΦF) + R(F),   R ≥ 0 manifest, κ > 0,

or the inequality version a_{T′} ≥ κ a_T∘Φ, so that positivity climbs from window to window starting from the proved
region (T < ½log 2, where there are no contacts and a_T = Arch_T ≥ 0 up to T ≈ 0.60, Paper 47 cor:Tarch).

## 1. Four-point filter

**(1) Closest antecedents, read in primary sources.**
- `phase-186-toolbox/R186_029_SYNTHESIS_ROUND14.md`, Lemma H and list (α)–(δ) of what escapes: congruence,
  Schur, finite rank and relative quotient inherit the margin; only (β) «exact decomposition with zero
  remainder» escapes, which uniformly in T collapses into thm:Z of Paper 47. Also W11′ (R184_015): every decomposition
  W_T = Pos + Δ_T has positivity itself as its lower half.
- `phase-160-row-d-infinite-T/R160_D4_R2.md`, Thm 3.4 and Thm 5.1: the Chebyshev completion
  comb(S_X F) = ℒ_X(F) − ℛ_X(F) and the closure «positivity through any convolution identity on
  tests = λ^W_{T+½log X} ≥ 0 per window, W^{Li} ≥ 0 in the limit». It covers exactly: maps acting
  on the tests by Dirichlet dilations/convolutions without boundary compression; S_X takes P_T to functions
  supported in the shifted window T + ½log X. That is, it covers the direction P_T → P_{T′} (upwards in
  support), which transports positivity in the wrong direction.
- `phase-161-row-d-sum-product-square/R161_002*.md` §3: the only exit from Thm 5.1 is the compressed version
  E_{N,T} = P_T(S_N𝓕 − J S_N)Π_T and the leakages C_T, C_T^{(N)}. Their residues: RULES_AVOID R1 (the boundary term is
  the support commutator ⟨g,[P,S]w⟩, without sign; R161_057–065), U2 and V1 (L161.3–L161.6 closed or circular).
- `phase-211-sign-sandbox/ROUND_021_A*.md` Lemma 3.3 (window sandwich): J_R ⊇ [1 − λ_0/‖𝒦‖, 1 + λ_0/‖𝒦‖] and
  J_R → {1} as λ_0 → 0.
- `ROUND_013_C.md` §4.1 (flow in T with history-dependent step; wrong arrow; repetition of Lemma H(iv))
  and RULES_AVOID Q2 (stage predicate with uniform step = local split).
- Index: `04_PHASES_100-189.md` rows W7 («linear Λ∗1 = log = window shift»), G6A-R160_D4_R2
  (DEAD, window shift), G6E-R162_802 (Λ∗1 = log = window translation in the flow), G2E-R160_S4 §3.2#7
  («effective shift RD_{T′} implies λ^W_T ≥ 0», OPEN-RESIDUE: the arrow is that of restriction).

**(2) New object.** A transition Φ_{T′→T} downwards in support, not a restriction, with remainder R of (E). In the
corpus transitions appear in the direction of the inclusion (P_T ⊂ P_{T′}, S_X: P_T → P_{T+½log X}); the
downward direction with signed remainder has no memo of its own. This is the only marked item.

**(3) Why it would avoid the difficulty.** The inclusion gives λ(T′) ≤ λ(T): wrong arrow. A downward Φ
formally reverses the arrow: if a_T ≥ 0 and R ≥ 0 then a_{T′} ≥ 0.

**(4) Connection with global positivity.** Chaining T_0 < T_1 < … with T_k → ∞ and T_0 < ½log 2: a_{T_k} ≥ 0 for
all k, hence for all T by monotonicity. It is exactly global positivity.

**Gate result.** Point (3) is only formal: §2 proves that the remainder R inherits in full the sign obligation of
the large window, with margin ≤ λ(T′). It is the between-windows face of W11′ and of Lemma H; there is no new
mechanism for the sign. **Does not pass.** Nothing is built. A class NO-GO (§2) and the exact status (§4) are recorded.

## 2. The transition does not lower the sign obligation

**Proposition M (PROVED, linear algebra).** Let Φ: P_{T′} → P_T be any linear map, κ > 0, and R := a_{T′} − κ a_T∘Φ.
Assume a_T ≥ 0 (inductive hypothesis). Then:
(i) R ≤ a_{T′} as forms on P_{T′}; in particular inf_{‖F‖=1} R(F) ≤ λ(T′).
(ii) R ≥ 0 on P_{T′} implies a_{T′} ≥ 0; if F*_{T′} is a unit minimizer, R(F*) ≤ λ(T′) and
κ a_T(ΦF*) ≤ λ(T′).
(iii) If R ≥ 0 and ‖ΦF‖ ≥ s‖F‖ on P_{T′}, then λ(T′) ≥ κ s² λ(T); since λ(T′) ≤ exp(−e^{(2−ε)T′}) (Paper 47
thm:margin, CITED), κ s² ≤ λ(T′)/λ(T): either Φ is almost non-injective exactly in the direction of the minimizer,
or R is a form whose bottom is ≤ λ(T′).
*Proof.* (i) κ a_T(ΦF) ≥ 0. (ii) a_{T′} = R + κ a_T∘Φ ≥ R, and a_{T′}(F*) = λ(T′) with both summands ≥ 0.
(iii) a_{T′}(F) ≥ κ λ(T)‖ΦF‖² ≥ κ s² λ(T)‖F‖². ∎

Reading. «R ≥ 0» is a sign statement in the window T′ stronger than the target (R ≤ a_{T′}) with a bottom of
size at most λ(T′). There are two ways to certify it: (a) by another transition (infinite regress, same
obligation) or (b) as a manifest sum of squares with zero remainder in the window T′, which is type (β) of
R186_029 = dual certificate of Paper 47 def:PD in that window; uniformly in T, thm:Z. The transition only splits the
form into two pieces, one of them positive by hypothesis: it is W11′ with Pos := κ a_T∘Φ. Repetition. History
dependence (Φ built with all previous primes, à la Λ∗1 = log) does not change (i)–(iii): they hold for
any Φ.

**Lemma C (PROVED, combining Lemma T of ROUND_013_C and Lemma 3.3 of 211 ROUND_021_A).** The base case T_0 < ½log 2 is
blind to the checks cΛ and deletion (there are no contacts: a_{T_0} = Arch_{T_0}, independent of the weight). For the
check c = 2 there exists T with a_T^{2Λ} not ≥ 0 on P_T (ROUND_021_A Lemma 3.3: J_R ⊂ [1 − δ_−, 1 + δ_+] with δ_+ ≤ λ_0/K_0
→ 0, NUMERICAL in the measured cells; CITED). Hence, in every chain T_0 < … < T_k reaching that T, some remainder
R_j must cease to be ≥ 0 under c = 2. Since R_j is affine in c, its positivity must use c = 1 with precision of
order λ(T_{j+1})/‖𝒦‖. An R_j certified by blind squares and relations valid at c = 2 would prove the
false statement: that is the step that must break, and it has to break inside R, not in Φ. ∎

## 3. The four proposed families of Φ

- **Müntz / compressed S_N^***, ΦF = P_T Σ_{n≤N} n^{−1/2}F(· + log n). Its pullback form is
  ⟨F, S_N P_T A_T P_T S_N^* F⟩; compared with A_{T′} the difference contains the Chebyshev completion (Thm 3.4 of
  R160_D4_R2, adjoint version) plus the support commutator [P_T, S_N]. Without compression, Thm 5.1 identifies the
  positivity with that of the shifted window (covered). With compression, the new term is the boundary
  commutator of R161_057–065 (RULES_AVOID R1), without sign. Φ-as-transition is not a distinct residue: it is the
  compressed pairing of R161_002 §3 read with a_T instead of a square. ARGUED (the full expansion was not
  rederived). Moreover Φ annihilates every F supported in [−T′, −T − log N) (the translations move to the
  left), so on that subspace (codimension ≤ 2 inside P_{T′}) (E) requires R = a_{T′}: there the
  transition contributes nothing (PROVED, trivial).
- **Folding** F ↦ F ± F(· − log p) with truncation: finite sum of translations, same class; Proposition M applies.
- **Scaling** t ↦ 2t, F ↦ √2 F(2·): does not preserve P (∫F(2t)e^{±t/2}dt = ½∫F(s)e^{±s/4}ds, different constraints),
  K(u) is not homogeneous, and the contacts log n go to ½log n, which are not logarithms of integers unless n is a square; the
  remainder contains the comb at non-arithmetic positions with mismatched weights n^{−1/2}. Proposition M applies
  equally. ARGUED as to the form of the remainder; PROVED as to P.
- **Hecke average** over d | N: finite sum of translations by log d; same class.

First requested instance ({2,3} → {2,3,4} → {2,3,4,5}): Proposition M fixes that every remainder R has bottom
≤ λ(T′) ≈ 5·10⁻⁵ (order of the margins measured in 211 for R = 4, CITED) and, by Lemma C, must distinguish c = 1
from c = 1 + O(λ_0/K_0). No explicit Φ is written because no choice changes that obligation.

## 4. Verdict and status

- Gate: **does not pass**. The downward transition is W11′/Lemma H (β) between windows: R ≤ a_{T′} and R ≥ 0 is the target at
  T′ with equal or smaller margin (Proposition M, PROVED, for every linear Φ and every κ). Declared class NO-GO: «inductive
  step T → T′ of the form (E) with arbitrary linear Φ and R certified by another step of the same type or by
  blind squares»: it does not lower the obligation (PROVED) and, with blind squares, would prove the check c = 2 (Lemma C,
  PROVED relative to the failure of c = 2, CITED/NUMERICAL).
- Question (1): Thm 5.1 covers the uncompressed upward Φ; the downward ones compressed by S_N^* fall into
  R161_002 §3 / R161_057–065 (ARGUED). Question (2): the step that must break under c = 2 is the certificate of R,
  not Φ. Question (3): the multiplicative loss is not the problem; with R ≥ 0 one gets λ(T′) ≥ κ s² λ(T), and the
  margin forces κ s² ≤ λ(T′)/λ(T).
- What remains (OPEN, no object): transitions nonlinear in F (type (γ) of R186_029: Φ depending on the
  minimizer of a_T), where Proposition M (i) still holds if a_T(Φ(F)) ≥ 0, and hence they do not escape either
  unless R has zero remainder. There is no defensible next explicit operation from this idea.

## 5. For independent verification

Rederive: Proposition M (three lines); Lemma C (requires only affinity in c and the existence of T with
a_T^{2Λ} indefinite, taken from 211 ROUND_021_A §2–3); the non-preservation of P under t ↦ 2t; the kernel of
P_T S_N^* on [−T′, −T − log N). Verify in primary sources that the reading of R161_057–065 as closure of the boundary
term corresponds to [P_T, S_N] and not to another compression.
