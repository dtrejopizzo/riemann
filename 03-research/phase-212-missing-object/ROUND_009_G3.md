# Round 9, item G3 — where the map has no marks

Phase notation: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), v_n = 2Λ(n)/√n, F real, supp F ⊂ [−T,T], F ∈ P_T.
Selection memo. Nothing new is derived. The conclusion (§4) is that **no candidate passes my own
cross-check**; for the two best, the missing operation is given.

Sources read in primary form for this memo: `RULES_AVOID.md` §§A–R; `REVIEW_003.md`–`REVIEW_007.md`;
`ROUND_008_A.md`; IDX `README.md` (targeted searches: BPY renewal l.2270–2357, FAMILIES_B_001 l.571);
IDX `AUDIT_A.md` (A14a-1); `phase-188-closing-D/N_BUILD_007_CONE_ORDER_ON_A_T.md` §§0–3;
`phase-106-global-modular-star-audit/106_115_FOLDED_STOCHASTIC_MONOTONICITY_AND_REFLECTION_GATE.md` §§1–3.
Grep searches in `03-research/` and `05-meta-and-planning/` for: Birkhoff, projective Hilbert metric,
Kreĭn–Rutman, majorization, variation diminishing, variational Donsker/Gibbs, Hamilton–Jacobi, Hopf–Lax,
Prékopa, determinantal, renewal, invariant cone. A search without matches does not prove novelty.

## 1. Taxonomy of method classes traversed (operation producing the sign · why it fails)

| # | Class | Sign operation | Structural reason for failure | Reference |
|---|---|---|---|---|
| 1 | Sum of squares with multiplier/symbol | pointwise split of the symbol into parity sectors | linear in the autocorrelation; blind to the weight | J1 (R3-a), B4 |
| 2 | Local split by contacts | q_∞ + Σ_p q_p, each q_v ⪰ 0 | with free split = goal; with fixed rule it dies at the archimedean threshold | O1–O3, Q1 (R7-a), M2 (G2_B8) |
| 3 | Contact bound by potential / ground state | contact ≤ potential ≥ 0 | remainder ⪯ Arch, indefinite for T ≳ 0.60 | Q1 (R7-a) |
| 4 | Reduction to finite Schur matrix / LDL / canonical factorization | pivots, root of the form | exists with remainder ≥ 0 iff the goal holds | J3, L5, D17 (Schur floor) |
| 5 | Second-order term in the weight | affine square V_0 + V_1(Λ) or summing quadratic defect | ρ ≤ Arch; or the goal with margin; does not pay the first jet | J2 (R3-b), L3 (R4-c) |
| 6 | Signature, inertia, Kreĭn/Pontryagin, Lorentz | count of negative indices | constant for c near 1 | L6 (R4-f), N1 (R5-a), M1 |
| 7 | Hyperbolic polynomial / real stability / Lee–Yang | real roots of an object of degree ≥ 3 | degree two or the goal with margin | N2 (R5-b), M3 |
| 8 | Induction in the window / stage predicates | inheritance of the sign on lengthening T | at the crossing the incoming weight has no influence; uniform step = local split | N4 (R5-d), Q2 (R7-b), BARRIER_W_001 |
| 9 | Naimark dilation / product–ratio channel | parallelogram ¼‖(U−V)f‖² | signed term blind to the weight; the arithmetic one is [P,S], indefinite | Q3 (R7-c), R1, K2–K3 |
| 10 | Leakage / compression to the window / Toeplitz–Hankel | ‖(1−P)SP‖² | no identity with the PC defect; global assembly closed | K1, R2, phase 122 |
| 11 | Variance / partition function / entropy | Var ≥ 0 | the laws of ζ^c are probabilities for all c | N5 (R5-e), I5 |
| 12 | Positive model + transfer or comparison | K ≥ εK_ref, transport from C_0 | additive prefactors and comparators excluded with proof | B4 (211 HYPERBOLIC §§7–13) |
| 13 | Total positivity / variation diminishing / PF_k | minors ≥ 0 | fails at PF₂ (104_21) and PF₅ (A14a-1); 𝖡 is not TP | C1, L5 (R4-e), 106_42 |
| 14 | Stochastic monotonicity / Markov / maximum principle | semigroup preserving a cone of functions | the reflected branch |t−u| reverses the order at each atom | 106_115 §1, C1 (Markov) |
| 15 | Dual cone order in the causal algebra | convolution preserving 𝒦_T^* | the resolvent is order-indefinite; δ_a ∉ ±𝒦_T^* | N_BUILD_007 §§1–3 |
| 16 | Heat flow / Laguerre–Pólya / Bakry–Émery Γ₂ / Grönwall in T | monotonicity under a flow | flow generic in c, or reformulation | C1, D17 |
| 17 | Reflection positivity (OS, chessboard, GKS/FKG) | ⟨θF,F⟩ ≥ 0 | per place or at the boundary excluded; frustration in 𝔸_M | C1, G2 (R-K1), M3 |
| 18 | Virial / dilation / Pohozaev | dilation identity | no remainder bounded below; generic in the comb | J5 (R3-d), I5 |
| 19 | Sieve / truncated Möbius / approximate inverses | sieve test as inverse | does not raise the degree in the weight; R ≤ 0 false | L2, L4 (R4-b, R4-d) |
| 20 | Identity valid for every comb (Poisson, theta, Selberg) | exact equality + positive block | carries no sign | B1, D6, D16 |
| 21 | Estimate with remainder | bound ≥ margin | margin exponentially small in T | B2 |
| 22 | Closure under Euler product | n₋ ≤ κ stable under product | product = sum of forms; unbounded index | N3 (R5-c) |
| 23 | Divisor incidence as a form | E diag(Λ) Eᵀ, rows linear in coefficients | factors through 𝒟_N; loses the first jet | I1–I2, J7, J10 |
| 24 | Additive renewal / BPY self-decomposition | jump semigroup with invariant density | no reversible density; layers with jetdet < 0 | IDX README l.2270–2321 |
| 25 | Integer invariants (nonnegative rank, recurrence {x+y,xy}, Forster) | invariant without generic value | closed in C1 after phase 201 | C1, IDX l.571 |

(Classification by class: ARGUED; each reason is CITED from the indicated entry.)

## 2. Properties that every surviving object must have at once

List extracted from the PROVED NO-GOs; each line cites what forces it.

P1. **Not affine in the weight**, nor affine with paired cross term (R3-b); and not polynomial in such a way that the
    difference with cΛ is only a combination of atoms Σ_{d|n}a(d) − log n without a signed remainder (R3-i).
P2. **The contacts are a source, not a cost, in the negative directions of Arch**: no piece that bounds
    contacts from above works beyond T ≈ 0.60 (R7-a; Paper 47 cor:Tarch, CITED).
P3. **History-dependent step**: a stage predicate with uniform step in a convex cone is a
    local split (R7-b); the incoming weight has no influence at the crossing (R5-d).
P4. **Uses the integer semigroup law** τ_{log k}τ_{log l} = τ_{log kl} coupled to the compression P_T: the
    2×2 (R161_038) and 3×3 (R161_050) countermodels satisfy (PC), radicality, parity and algebraic
    transfer without saturating (ROUND_008_A §3).
P5. **Exact to the precision of the margin**: the width of the window in c is of the order of the margin
    (211 ROUND_021_A Lemma 3.3; §P), and the margin is ≤ 4·10⁹Te^{−15.449T} (B2). No estimate with remainder.
P6. **Not an inertia count nor a local invariant in c**: indices constant near c = 1 (R4-f).
P7. **Not a Gram realization at a base point** (log-concavity, variance, Hessian of a homogeneous
    polynomial): R5-a, R5-e. It may be a property valid on a whole cone with its own certificate
    (which R5-a explicitly leaves unexcluded).
P8. **Not local per place**: the Euler product sums forms (R5-c); Theorem D of phase 159 (G2_B8_R5):
    the optimal split is complementary slackness of obstructing states, circular as a prior rule (J3).
P9. **Sees the arithmetic side with exact values and the atomic structure**, not only the mass of the comb
    (𝒦_S, W-pat; P47 rem:bar-pat) and does not factor through a fixed Λ-free object (phase 170, «factor-through»:
    every linear row annihilating ℝ(Λ,1) factors through 𝒟_N, I1).
P10. **Two channels credited by distinct falsifiers**: a_P breaks the functional equation, quartets
     the Euler product (G1); and the remainder (not the identity) ceases to be ≥ 0 at c = 2, under deletion and
     under Beurling (R3-i).
P11. **Dimension growing with T** (Thm finZ; §P; D12 fixed support excluded).
P12. **A cone preserved by the operation cannot be 𝒦_T^* under convolution by signed measures
     with atoms in (0,2T)** (N_BUILD_007 §§1–2): if the mechanism is order-based, the operation is not a
     convolution in the causal algebra.

(P1–P12: ARGUED as a list; each item CITED from its source.)

## 3. Sign operations outside the taxonomy: cross-check

| Operation | Closest antecedent | What exactly is excluded | Does it survive? |
|---|---|---|---|
| Variance with a genuinely nonlinear law | N5 (R5-e); 104_54, 104_71 (Gibbs/entropy); IDX FAMILIES_B (DPP, RMT) | every variance identity under the laws of ζ^c (generic in c); DPP «not virgin» | No: a law built from the weight inherits genericity in c unless it uses P4, and I have no object |
| Fixed point / monotone flow with known limit | R7-b, R5-d, D17 (Grönwall in T), N_BUILD_007, 106_115 | uniform step; convolution in the causal algebra; folded Markov semigroup | **Yes as a gap (candidate A, no object)**: contraction in the projective Hilbert metric (Birkhoff) with non-uniform step; «Hilbert projective metric» without match in the corpus (the 46 matches of «Hilbert metric» are inner-product metrics, 114_d_102–139) |
| Order: lattice, majorization, TP, variation diminishing | C1 (TP order ≥ 5, PF₂), L5, 106_42, 106_115, N_BUILD_007, M3 (FKG) | TP/Pólya kernels; pattern pivots; stochastic monotonicity; convolution preserving 𝒦_T^* | No: the majorization «comb ≺ Arch in the order of 𝒦_T^*» is exactly window positivity (N_BUILD_007, header): reformulation |
| Convexity in another parameter (form = second derivative) | R5-a, R5-b, M1 (R160_C7_R1 §6.3(2)), B10 (Danskin in c) | log-concavity at a base point; hyperbolic polynomial; concavity in the comb | **Yes as a gap (candidate B, no object)**: functional convex on a whole cone with its own certificate (R5-a leaves it explicit) |
| Reflection positivity t ↦ −t with crossing contacts | C1 (OS/chessboard, OS at the boundary, OS per place NG-E1), J1 (J in parity sectors), G2 R-K1, 106_115 (reflected branch |t−u|) | reflection at the boundary, per place, in parity sectors; R-K1 forbids boundary reflections | No: with reflection at 0, ⟨θF,F⟩ is ⟨JF,F⟩, and the multiplier algebra + J is R3-a; the contacts crossing the plane are the term ε⟨X²F,F⟩ of opposite sign in the two sectors |
| Counting (form = cardinality or measure) | C1 (nonnegative rank, recurrence {x+y,xy}); I5 (Laplace energy on the Gamma lattice, generic); K5 (hyperbola remainder ≥ 0, no weighting cancels it) | integer invariants of phase 201; h(k) ≥ 0 | No: a cardinality is ≥ 0 for every weight supported on ℕ; it does not break at c = 2 (P10) without a subtracted term, and then it is not counting |
| Categorical / trace | C3 (Floer, motivic, Bridgeland, arithmetic site) | reformulations | No: I cannot write the object (rule of the brief) |

(Cross-checks: ARGUED, by reading the cited entries; not exhaustive.)

## 4. Candidates

**None survives my own cross-check.** There is no written object for any of them. I give the two best with the
missing operation, in the gate format, so that an independent check can decide whether they deserve a round.

### A. Projective contraction with history-dependent step (Birkhoff–Hopf)

1. *Antecedent:* `ROUND_007_B.md` Lemma 1 / R7-b (uniform step = local split); `N_BUILD_007` §2
   (convolution preserving 𝒦_T^*: only multiples of δ₀ known; general case undecided); 106_115 §1.
2. *Object that would be needed:* a **nonlinear** map Φ_{T→T′} between cones of forms (or of dual
   measures) of the windows T < T′, preserving the cone, with finite projective diameter of the image, and
   whose fixed point or limit is the form of Λ. Positivity would come from the Birkhoff–Hopf theorem
   (CITED as a classical tool), not from a split.
3. *Why it would avoid the antecedent:* R7-b requires the step to hold for every Q; a projective contraction
   only requires preserving the cone on the image of the previous step (history dependence, P3). It is not
   a convolution (P12).
4. *Global connection:* if Φ preserves {a_T ⪰ 0 on P_T} and the iteration from a certified window
   (T ≤ ½log15, cited) reaches every T, one obtains a_T ⪰ 0 for all T.
- **Missing operation:** I know no natural window-to-window map that preserves
  positivity and uses P4. The only known transition (lengthening the window) is the inclusion P_T ⊂ P_{T′}, which
  goes in the wrong direction (the sign at T′ implies that at T). Without that map, the candidate is an
  empty scheme. First statement to attempt: «there exists an explicit Φ with Φ(a_T^{Λ}) = a_{T′}^{Λ}
  on P_{T′} taking forms ⪰ 0 to forms ⪰ 0». Falsifier: cΛ with c = 2 must violate cone preservation
  (not just the identity), and a_P must break it in a different line than the quartets.

### B. Functional convex on a whole cone with its own certificate, whose Hessian is a_T

1. *Antecedent:* R5-a (leaves unexcluded «a property valid on an entire cone with its own certificate»);
   R5-b; M1 / R160_C7_R1 §6.3(2); N5.
2. *Object that would be needed:* Φ: P_T → ℝ, defined with the semigroup law and the compression P_T, convex on
   all of P_T for a reason other than Gram at a point (e.g. a supremum of affine functions indexed by
   factorizations k·l, or composition of a convex increasing function with convex functions), with
   D²Φ(0) = a_T.
3. *Why it would avoid the antecedent:* R5-a and R5-b look at a base point or a polynomial; a global
   certificate of convexity is not a Gram realization at a point.
4. *Global connection:* D²Φ(0)[F,F] = a_T(F) ≥ 0 on P_T, for each T.
- **Missing operation:** a supremum of affine functions indexed by factorizations is linear in the weight on each
  branch (falls into P1/J2); a convex-increasing composition needs a convex inner piece that already carries the
  sign. I have no third source of convexity. First statement: «Φ(F) = sup_{k,l} ℓ_{k,l}(F) + q(F) with
  q ⪰ 0 Λ-free and D²Φ(0) = a_T» — I suspect it is the J2 format and I do not propose it.

## 5. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | Taxonomy of 25 classes and their reasons | ARGUED (each reason CITED) |
| 2 | Mandatory properties P1–P12 | ARGUED (each item CITED) |
| 3 | Majorization in the order of 𝒦_T^* = window positivity | CITED (N_BUILD_007, header) |
| 4 | Reflection at 0 with crossing contacts falls into R3-a | ARGUED |
| 5 | A pure count does not break at c = 2 | ARGUED |
| 6 | «Hilbert projective metric» / Birkhoff without substantive match in the corpus | NUMERICAL (grep; does not prove novelty) |
| 7 | The inclusion P_T ⊂ P_{T′} transfers the sign only from T′ to T | PROVED (trivial) |
| 8 | Candidates A and B: no object; they do not pass the gate | OPEN |
| 9 | Global sign | OPEN |
