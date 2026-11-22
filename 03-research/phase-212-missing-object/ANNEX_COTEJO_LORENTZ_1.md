# Annex — Targeted cross-check: Hodge, Lorentz, Alexandrov–Fenchel, log-concavity

Question cross-checked. In each parity sector of J: t ↦ −t, P_T has codimension one; (★) in a sector
is equivalent to a_T having at most one negative direction on the whole space of the sector, with the Tate
vector (cosh(t/2) or sinh(t/2)) as the timelike direction, i.e. to a reversed Cauchy–Schwarz
a_T(F, G)² ≥ a_T(F) a_T(G) for timelike G. The corpus is searched for anyone who tried to prove that signature
by a CLOSURE MECHANISM (induction, log-concavity, closure under products, directional derivative,
limit, deletion/contraction), and not merely stated or counted it. This annex proposes no constructions.

## 1. What was searched

Case-insensitive grep in `03-research/` (all phases), `04-papers/` (43–48),
`00-references/`, `05-meta-and-planning/` (index, SURVEY_MODERN_UNTRIED, crossword) and the master grid,
with the words of the task grouped into a single expression (Hodge index, índice de Hodge, Hodge–Riemann,
Kähler package, hard Lefschetz, Lorentz/Lorentzian, reverse Cauchy, Cauchy–Schwarz invertida, Alexandrov,
Aleksandrov, Fenchel, mixed volume, mixed discriminant, Brunn–Minkowski, log-concav/log-cóncav, matroid,
Chow ring, Adiprasito, Brändén, one positive eigenvalue, exactly one negative, hyperbolic polynomial,
completely log, Gårding). Result: **740 files** with at least one match (most of them for
«Hodge index» in phases 4–50 and for backup copies of the grid). The search was then refined by subfamily
(Lorentzian/completely log: ~25 research files; log-concav: ~25; matroid/Chow ring/Adiprasito:
~25; Alexandrov/mixed volume/mixed discriminant: 10; Gårding/hyperbolic polynomial/Borcea: ~25) and
crossed with the index (README, 02, 03, 04, 05, 05b, 06, AUDIT_PHASE193_CERTAINTY, SURVEY_MODERN_UNTRIED).

**Opened as primary sources (reading of the relevant section or the whole file), 31 files:**
phase 212: README, OBJECT_SPEC, LEDGER, BRIEF_CONSTRUCTOR, REVIEW_003, REVIEW_004, ROUND_004_E (§§Cross-check,
1, 2); phase 211: STATEMENT_001, ROUND_004_A §3; `phase-160/R160_C7_R1.md` §0, §6; `R160_S3_SURVEY.md`
§3.1 (T20) and lead 4; `phase-138/R138_001_ROUND1.md` D.15.2 and closing list; `phase-120/
P3_MATROID_FUSION_NO_GO.md` complete; `P3_G125_T2_AHK_CORRECTION.md` §§4–5, 8;
`phase-114/114_d_244_FOURIER_TANGENT_HODGE_FORM.md` verdict, §§3, 5–7; `phase-41/126-hodge-index-on-
the-square-attainable.md` summary and §1; `phase-195/INV_M_001_REAL_STABILITY_GARDING_MSS_NO_GO.md` §§2–5;
`phase-200/D_CONSTRUCTION_001.md` summary and cross-check table (§5 by heading); `phase-201/
FAMILIES_A_001.md` A1; `FAMILIES_B_001.md` F30; `phase-193/CA_F_000_SEEDS.md` F5; `CA_F_SYNTHESIS.md`;
`phase-186/R186_033_NEW_INSIGHT.md` Idea 2; `phase-135/R135_007_CLOSING_DECISION.md`;
`phase-16/06-hunt-indefinite-object.md` principle; `phase-11/M11.4-5-verdict…` verdict;
`phase-104/104_21_GLOBAL_COMPOUND_POISSON_TP_GATE.md` (log-concavity line); matching lines
in `phase-211/ROUND_005_D.md`, `phase-207/CLASS_001.md`, `phase-206/AUDIT_206_001.md`,
`phase-212/ROUND_004_D.md`, `phase-162/R162_1602`, `phase-200/SPEC_SIGN_OBJECT_008.md`; and the rows of the
index cited below.

**Not opened as primary sources (seen only via the index row or the grep line):** Paper 47
(`main.tex`, §§11–12, 17, 22–26), Paper 46 (thm:P / cor:P3 and thm:parityschur only via ROUND_004_E),
Paper 43 Thm 14.1, phase 15 (M1–M10), phase 41 doc 125, phases 40, 42, 43, 107 (107_241), 113, 122, 137,
139–142, 155 (R155_054), 159 (G1_B1_R3/R4), 184 (R184_011), the sources in `00-references/` (Tropical
Hodge theory, Cartwright, Hodge index of Yuan–Zhang) and phases 4, 10, 28, 33, 54, 103, 106 where the
word appears in other senses.

## 2. Inventory of antecedents

**A1. Lorentzian criterion (R138_001 D.15.2, PROVED, linear algebra).** For symmetric Q and K with
Q(K) > 0: Q ≤ 0 on K^⊥ ⟺ Q(F, K)² ≥ Q(F)Q(K) for all F ⟺ the same on an absorbing set in K.
It is exactly the reversed Cauchy–Schwarz against the timelike vector. The version «for all
F, G in a convex cone» was refuted (D.15.2(e)). D.15.2b: the effective cone is the wrong cone; the
Khovanskii–Teissier form on that cone is not available; D.17.3 falls into the no-go of the Chebyshev remainder
(114_d_185). Record label: PROVED (criterion) / RESTATEMENT; index: G6 «retry, no sign»,
P47 §17 DEAD. Where it stopped: the criterion contributes no sign; proving it on the detecting cone requires the
sign itself.

**A2. Polar completion of the square and residue (HR-T) (R160_C7_R1, §§0, 5–6).** Builds an algebra
𝒜 = ℝf₁ ⊕ ℝf₂ ⊕ (T) with form B; Thm. 2: Castelnuovo Z² ≤ 2(Z·f₁)(Z·f₂) on Γ_F is literally W_T ≥ 0;
Thm. 3: Metzler structure (off-diagonal > 0, diagonal −∞) and Perron ground state of
A_T on L²(I_T); Thm. 4 states «at most one negative direction on L²(I_T)» as a reformulation (it uses an
external equivalence). **§6.2 is the only explicit examination of the requested mechanism:** (a) the quadratic class
of Brändén–Huh requires entries ≥ 0 and at most one positive eigenvalue; here the diagonal is −∞; removing the
diagonal leads to matrices with zero diagonal that are Lorentzian only in the complete multipartite
case, and the divisibility compressions are not; (b) closure under limits: there is no finite generating
family (arena bound N*(T) ≥ exp(4e^T(1+o(1)))), hence the limit gives nothing beyond the
definition; (c) Alexandrov–Fenchel: a mixed-volume model would have diagonal V(K, K) ≥ 0, impossible
with diagonal −∞; (d) AHK: on a surface the volume polynomial and the Hodge index coincide. §6.3(2):
**raising the degree** (homogeneous polynomial of degree k ≥ 3 whose Hessian is −a_T) — candidates Str(Γ_F^k)
give complex bilinear forms without transpose; the candidates with transpose are −a twisted by Φ_F^{k−2}
and are Lorentzian only if the property already holds for the twisted forms. OPEN; «needs an
independent source of nonnegative coefficients». Label: PARTIAL / REF-D in the index (G8H-R160_C7_R1).

**A3. Lorentzian tangent form over primes (114_d_244, PROVED).** h_S = xx* − diag(|x_p|²) on the
tangent channels of a finite set S of primes; inertia (1, |S|−1, 0) for |S| ≥ 2, by a
rank-one-minus-diagonal determinant lemma. **Closure by cofinal limit in S** (§5): compatibility by
extension by zero, limit form |Σ√log p z_p|² − Σ log p |z_p|², negative on the primitive kernel;
lift to prime powers with coefficient Λ(p^{k+ℓ})/√p^{k+ℓ}. It stopped (§6): rank
obstruction — the degree term has rank one in each S and the archimedean part G_∞ has infinite rank;
moreover it is second order in the velocities while the target form is first order (R160_S3 lead 4,
D.258–259). Index: G4D «PARTIAL, genuine signature theorem, dead-ended».

**A4. Pointwise persistence of Hodge–Riemann under directed systems (P3_G125_T2_AHK_CORRECTION §5,
PROVED).** If q_{S′} restricts to q_S and q_S ≤ 0 on the compatible primitives, the induced form is ≤ 0 on
the algebraic colimit, without taking limits of signature. It is a closure rule under «adding primes», but
it presupposes the signature at each finite S, which was to come from a matroid Chow ring (AHK) on the
prime-collision strata (§4, conditions 1–6). **P3_MATROID_FUSION_NO_GO (PROVED):** there is no
injection ℕ → lattice of flats with Φ(i + j) = Φ(i) ∨ Φ(j), because the join is idempotent
(Φ(2i) = Φ(i)); the faithful additive iteration of Frobenius does not fit in a matroid lattice. Candidate
withdrawn before reaching Hodge–Riemann. Index: G4H-phase-120/P3 DEAD.

**A5. AHK versus the square of the scaling site (phase 41, doc 126).** Analysis of the Kähler package:
AHK requires a finite graded ring, Poincaré duality, an ample class and induction by flips over a
finite lattice; the object is infinite and continuous, which breaks the finite induction; obstruction of
Babaee–Huh type. Verdict (d) «indeterminable», biased toward circular (it uses an external equivalence). Label:
analysis, no theorem; index P41-2 NO-GO, G8H-R160_S2 PARTIAL (toy (1,2) signal not persistent at
infinite rank).

**A6. Real stability, Gårding cones, MSS (phase-195 INV_M_001, PROVED).** On the polarized
multiaffine symbol of the block 𝔸 on {1, 2, 3, 6}: Thm. M1/M2, it is not real stable — on every
coordinate face where the form is positive definite the Rayleigh inequality Δ_ij p ≥ 0 fails, because
stability = reversed Cauchy–Schwarz (signature (1, n−1)) and the target there was definite. §3: a
definite quadratic is not hyperbolic in any direction; the only useful Gårding cone is the PSD cone
(REF-D). §4: MSS gives ∃ and not ∀. **Note:** this attempt applied stable/Lorentzian theory to the
restricted form (definite target), not to the form on the whole space of the sector with the Tate direction.

**A7. Non-AHK Hodge–Riemann/Lorentz (phase-193 CA_F_000_SEEDS F5; CA_F_SYNTHESIS).** Lemma F5
(Haynsworth, PROVED): positivity on the primitives ⟺ k ≤ 2 negatives and a 2×2 Schur condition
(= P46 thm:parityschur). Discarded as «retry» with the argument «Theorem P: n₋ on the whole space > 2
at large T, the signature hypothesis is false». **That argument is mis-cited:** AUDIT_PHASE193 row 35
marks it «Theorem P mis-cited; FIX», and ROUND_004_E Prop. 1 and table §1 show that the growing
counts are of 𝔪_T (without comb), whereas for a_T, if λ_A(T) > 0, n₋(a_T|L²(I_T)) ≤ 2. The
discard of F5 therefore stands only as «reformulation without mechanism».

**A8. Hodge index transfer conditional on h⁰ (R135_007 Thm 12.3; P47 §§11–12; phases
137–142, 155).** Canonical class K, duality σ_K, transfer theorem PROVED conditional on an
h⁰ ≥ 0 with (a), (b′) and the Riemann–Roch inequality (c). h⁰_Z on translations of prime
powers satisfies (a), (b′) and fails (c) (growth (log m)^{3/2} versus ¼m², D.11.3); tensorial h⁰ (140)
reads only bidegrees; frame defect (142 Thm 19.25) excludes the h⁰ with (a), (b′), (c); the falsifier Ξ_a
breaks the transfer. Index: W10 MW-5/OT-5′ NO-GO; G1H-P46 DEAD.

**A9. Arakelov / arithmetic Hodge index (phases 15, 40, 122; R9-05, R9-09; L26, L80, L83).** Import
of Faltings–Hriljac/Yuan–Zhang: controls heights, does not type-check on the carrier; P40-3 CIRCULAR (spectral
versus intersection positivity). Not opened as primary sources here.

**A10. Mixed volume (phase-200 D_CONSTRUCTION_001 §5).** Kazarnovskiĭ/BKK + Minkowski
V(P, Q)² ≥ V(P, P)V(Q, Q): gives an integer quadratic form with Hodge signature, but it does not see the
coefficients, it is generic for Beurling and Epstein, and its isometric embedding is equivalent to (W⁰)
(REF-D, PROVED). R160_C7_R1 §6.2(c) adds: volume diagonal ≥ 0, incompatible with the diagonal −∞.

**A11. Mixed discriminant (211 ROUND_004_A Prop. 1, PROVED).** The necessary conditions (C_k) in
2×2 contain Σ v_m v_n ½D(R_m, R_n), the mixed discriminant of overlap matrices; it couples pairs of
prime powers with no arithmetic relation. Necessary condition, not a mechanism; class NO-GO
(Prop. B: finite subspaces independent of Λ do not carry the sign).

**A12. Log-concavity/log-convexity.** (i) R186_033 Idea 2: convexity of log λ_A(T) in a
canonical variable — NO-GO NUMERICAL (falsified in T, e^{2T}, e^{4T}). (ii) 211 ROUND_005_D: log-concavity of the
ground-state profile OPEN, «not expected», NUMERICAL. (iii) 212 ROUND_004_D: Pólya functions
PF₂ excluded because 𝖡 is not ≥ 0. (iv) R162_1602: a sum of ≥ 2 deltas fails PF₂. (v) 104_21: compound
Poisson sequence neither log-concave nor PF₂ for 1 < Q < 3. (vi) Turán/Jensen/Laguerre–Pólya/log-concavity
of Taylor coefficients (index L22, L23, L75, A14a; NG-D1/D2; G1F-103): properties of the Fourier
side or of every Euler series with coefficients ≥ 0, class 𝒦_inh, Thm. B of 207 CLASS_001 (falsifier
a_P). (vii) FAMILIES_A A1: «applying log-concavity to (Λ(n)/√n) or to (c_N) would be a cone condition
on a sequence» — discarded by adjacency, without construction.

**A13. Indefiniteness as a principle (phase 16, memo 06; phase 11).** Principle: the carrier must have
intrinsic Lorentz/Pontryagin signature; a naive Klein–Gordon modification of the
modular resonances remains definite. Phase 11: the hyperbolicity/total positivity route «is a positivity».
No object.

**A14. Inertia and Pontryagin format (ROUND_004_E; P46 thm:parityschur, prop:polarcap,
subsec:inertia-excl; phase 197 BARRIER_W).** Index counting; constancy in c near 1. Already covered
by the task.

## 3. Classification

| Antecedent | Class |
|---|---|
| A1 Lorentzian criterion D.15.2 | (a) reformulation |
| A2 R160_C7_R1 (Thm. 4; §6) | (a) reformulation; §6.2–6.3 is a negative examination of the mechanism (no construction) |
| A3 tangent form 114_d_244 | (c) degenerate: signature (1, n−1) over primes with closure by cofinal limit in S, but the mechanism is a rank-one-minus-diagonal lemma, not induction or log-concavity, and the form is not a_T |
| A4 persistence + fusion matroid (phase 120) | attempt at (c) on objects of the problem (collision strata of prime powers), with closure by colimit in S; died before Hodge–Riemann |
| A5 AHK/square (phase 41) | (b) transfer |
| A6 stability/Gårding/MSS (195) | (c) applied to the wrong target (definite form); NO-GO on that formulation |
| A7 F5 non-AHK (193) | (a) reformulation (discarded with an erroneous citation) |
| A8 h⁰ transfer (135–142, P47) | (b) transfer |
| A9 Arakelov | (b) transfer |
| A10 mixed volume (200) | (b) transfer from convex bodies/BKK, REF-D |
| A11 mixed discriminant (211) | (a) necessary condition |
| A12 log-concavity (186, 211, 212, 162, 104, Turán…) | tests of log-concavity of scalar quantities (λ_A in T, profiles, sequences); none is a closure mechanism for the signature of the form |
| A13 indefiniteness principle | (a) |
| A14 inertia | (a) counting |

## 4. Answer

**Is there an attempt of class (c) in the corpus?** Only two partial ones, and neither on a_T with the Tate
direction in a parity sector.

- **Phase 120 (A4).** Closure operation: union of sets of primes (directed colimit in S, with the
  pointwise persistence lemma PROVED) and, within each S, the AHK induction by flips/deletion–
  contraction on a lattice of flats that was meant to encode the collisions C_{p^i}∘C_{p^j} → C_{p^{i+j}}.
  It was stopped by a type incompatibility PROVED: the faithful additive iteration does not inject into an
  idempotent join (Φ(2i) = Φ(i)). The lattice used was the collision lattice, not the divisibility lattice
  of the window; the AHK induction was never executed.
- **114_d_244 (A3).** Closure operation: adding primes (extension by zero, cofinal limit), with
  lifting to all powers. The signature (1, |S|−1) comes from a determinant lemma, not from
  induction. It was stopped by a rank obstruction: the degree term has rank one, the
  archimedean part has infinite rank, and the form is second order versus the first-order target
  form; it was never identified with a_T.
- **Negative examinations without construction:** R160_C7_R1 §6.2 discards the Brändén–Huh quadratic class
  (diagonal −∞), closure under limits (no finite generating family), Alexandrov–Fenchel (volume
  diagonal ≥ 0) and AHK on a surface (coincides with the statement); §6.3(2) leaves OPEN the raising of
  degree (polynomial of degree ≥ 3 with Hessian −a_T) for lack of an independent source of nonnegative
  coefficients. Phase 195 refutes real stability on the definite form, not on the whole form of the
  sector. The other mentions are reformulations (a) or transfers (b).

No opened file carries out an induction of the type «signature on the window T ⇒ signature at T′ > T»,
nor a directional derivative/polarization on a_T, nor deletion/contraction on the divisor lattice of
[1, e^{2T}).

## 5. What was not found (without claiming novelty)

In the opened files and in the grep matches the following was not found:

1. An attempt to prove «at most one negative direction per parity sector for a_T on L²(I_T),
   with cosh(t/2) or sinh(t/2) as the timelike direction» by induction in T (lengthening the window) or by
   any closure rule. The statement appears only as a reformulation (A2 Thm. 4, A7, A14) or as a
   count.
2. A polynomial of degree ≥ 3 in the test, built from the objects of the problem, whose Hessian is a_T
   (or −a_T) and to which the Brändén–Huh characterization by derivatives is applied; only the negative examination
   of R160_C7_R1 §6.3(2) on Str(Γ_F^k).
3. Chow rings, lattices of flats or deletion–contraction on the divisibility lattice
   {n < e^{2T}} or on the comb; the only matroid lattice treated (phase 120) was the collision lattice of
   correspondences.
4. Real stability or Gårding cones applied to the form of the whole sector (Lorentz signature), instead
   of the restricted form or the block 𝔸_M (A6).
5. Log-concavity of a sequence or generating polynomial tied to the signature (for example, of
   coefficients of a characteristic polynomial of compressions of a_T); the log-concavities examined
   are of scalar quantities or of Fourier-side coefficients.
6. Alexandrov–Fenchel/mixed discriminants with nonpositive diagonal or with «virtual bodies»; only the
   discard by diagonal of R160_C7_R1 §6.2(c) and the necessary condition of 211 ROUND_004_A.

A search without matches does not prove that nothing was attempted: Paper 47,
phases 15, 40–43, 107, 113, 122, 137–142, 155, 159, 184 and the sources in `00-references/` remain unopened as primary sources. Moreover, a
signature mechanism on the whole space of the sector remains subject to what is PROVED in ROUND_004_E Lemma 2
(every bound on the negative index is a positivity in finite codimension) and to the falsifier test
of `RULES_AVOID.md` §E: this annex does not examine whether any closure rule distinguishes Λ from cΛ or from a_P.
