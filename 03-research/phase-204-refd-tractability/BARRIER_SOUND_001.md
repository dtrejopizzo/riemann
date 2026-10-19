# BARRIER_SOUND_001 — Soundness audit of the barriers (phase 204b)

This memo does not
prove or close anything. It inventories the holes in the barrier theorems and says what method would pass through each.

Sources read: META_200_BARRIER_001 (§1.3–1.4 and Addendum A1–A6), SPEC_SIGN_OBJECT_006 (§B, table A, I1–I10, composition
rule l.141–142), DH_TRANSFER_001 (summary, 𝔗₁, S1–S4), CPOS_CLASS_001 (§2 (β), §3 h1–h6, §4), FAMILIES_A_001 (G1),
FAMILIES_C_001 (§1: L-loc, C-pos, S-0, S-1), AUDIT_200_DCONS_001 (Thm 3′), SPEC_SIGN_OBJECT_007 (C-emb, "honest
answer to B"), AUDIT_200_Q2_001 (C-τ, L1, Prop 4.1), AUDIT_CONSTRAINTS_001 (the 28 restrictions, HARD/SOFT/MISLABELLED),
phase-197 BARRIER_001 (Lemma 2, sub-case A2∧loose-FE), BARRIER_EST_001 + REVIEW_BARRIER_EST_001, AUDIT_203_001,
phase-202 README (closure), Paper 47 thm:shape, thm:noimport, lem:spec-collapse (lem:transfer cited in both).
I did not reread Z_CARRIER_001 or Q2_DEGREE2_001 in full: I use the labels META_200 and AUDIT_200_Q2 give them. I take
Theorem X with the statement recorded in the index and in memory (phase 186: "new primes must cancel σ on U at
resolution π/T; every first-order discriminant is a functional of h*"). I did not re-verify its proof.

## Summary (≤250 words)

I found no gross error of the type "a PROVED tool was discarded by a false theorem." The barriers with a PROVED core
(lem:transfer with certified falsifiers, Lemma R/Guo, R-Q6, lem:spec-collapse, C-emb (a)–(c), G1, L-loc,
Danskin, thm:shape(B)'s margin) exclude exactly what they claim to exclude. I did find three points where the corpus
**read more than what is proved**, and a method could pass through those points:

1. **thm:noimport (iv) / C-pos (β)** (ARGUED). It says that a nonlinear gate whose verification for ζ uses Euler is "at
   least as strong" as the goal. That is logically true, but it does not imply that it is harder. Weil for curves has
   exactly this form. Phase 201 was closed as a **strategy**, not by impossibility.
2. **Φ200's branch-composition rule + the conjunction of premises in 197** (ARGUED). No theorem says that a proof whose
   premises each fail at a **different** falsifier falls into a single branch. This is precisely the form cor:shape(b)
   requires.
3. **Thm 3′ and the non-analytic class** (ARGUED, and no theorem outside the analytic case). Sign or |·|-type invariants
   that see the test (nodal counts of c_g(log n), inertias with absolute value) are covered in first order only by
   Theorem X. (The DH falsifier, which in the draft was the third hole, is **certified**: CERT_DH_001 +
   AUDIT_200_CERTDH_001, PROVED at T = 9/5.)

Signs of falsity: none numerical. There are historical signs of overclaiming: thm:AL retracted, multiplier C
Thm 6.1 retracted, Cor 3.7 overclaimed, false informational reading of the DH lemma. Answer: a gross error is
implausible. What is plausible is an overreading of (β) and of the composition as a NO-GO. Already-proved tools that
would help: Φ.12 (additivity), Danskin/(2.1), lem:transfer, Lemma R.

## 1. Inventory of non-PROVED pieces

Columns: (a) what it claims and why it stands as it does; (b) the hole, i.e. the method that would pass if the piece
were false and that no PROVED restriction excludes; (c) signs of falsity; (d) cost of proving or refuting it.

| # | Piece (label) | (a) Claims / why not PROVED | (b) Method that would pass if false | (c) Sign of falsity | (d) Cost |
|---|---|---|---|---|---|
| P1 | **thm:noimport (iv) = C-pos (β)** (ARGUED) | A nonlinear gate H in a, verified for ζ with an input outside 𝔗₁, "is at least as strong as the goal." What is ARGUED is the classification: the memo admits (l.127) that it is not excluded that a stronger statement be **more tractable**. | A positivity theorem with hypothesis H(O_{g,ζ}) verified **by structure** (Euler, conductor 1, integrality), not by estimation. This is the Weil/Castelnuovo pattern: the Hodge index is stronger than the Riemann inequality for a divisor and easier to prove. Concretely, a Hankel/Gram form G(g) nonlinear in Λ (e.g. built from log ζ or from Λ∗Λ) whose PSD property is proved by exact factorization. | None. The piece is not "false": it is misread when used as a NO-GO. CPOS labels it correctly. Phase 201's corollary rests on it as "closed as strategy." | Cannot be proved as a class theorem: "more tractable" is not a mathematical predicate. It can only be refuted by exhibiting an H. |
| P2 | **Branch-composition rule (Φ200)** and "the conjunction of heterogeneous premises still finds a falsifier" (197's BARRIER_001, "ARGUED as a set") (ARGUED) | Each input I1–I10 is sent to a branch, and the composition falls into "the worst one" (order 2≻5≻4≻3≻1). There is no proof that nonlinear operations between outputs of different branches stay within one branch. | A proof with premises P_E (false for Beurling and a_P: uses the full ℕ), P_F (false for DH: Euler) and P_W (false for Epstein: degree 1, conductor 1), combined nonlinearly (Schur, min, product). No certified falsifier satisfies all three, so lem:transfer does not apply to the conjunction. This is exactly the form cor:shape(b) **requires**. | None against the rule. But the rule was never proved, and it is exactly where the only type of proof thm:shape leaves alive sits. | Proving it: medium-high (calculation of proofs over 𝒦_NL). Refuting it: exhibit a concrete composition of two branches whose result reads Λ in a free variable g (F7). |
| P3 | **DH falsifier at T = 9/5** (rem:FDH). DH_TRANSFER §1.4 gave it as CITED/ARGUED, but **CERT_DH_001 certifies it, PROVED** (intervals, −7.05·10⁻⁹ in the odd sector, −0.75 at T = 2; redone bit by bit in AUDIT_200_CERTDH_001) | The degree-1 part of thm:noimport (i) and C-pos (i) uses 𝔞^{DH}_T < 0 for T ≥ 9/5 (lem:monoT). | **None for T ≥ 9/5.** h6 remains: on [½log15, 9/5) there is no certified 𝔗₁ falsifier, and on [½log15, 1.59) none for 𝔗₂ either. There the class theorems are vacuous and any uniform construction passes. But it only helps for bounded windows, not for the ∀T goal. | None: certified. | Closed. Lowering the threshold T_DH < 9/5 would be NUMERICAL, of low value. |
| P4 | **Thm 3′** (AUDIT_200_DCONS; ARGUED) | A rank-type χ with **analytic** dependence on the test is constant on a dense open subset of P_T. Missing detail: the minors do not vanish identically, uniformly in n. | χ that depend on the test non-analytically but are not a sign of 𝔞: (i) counts of sign changes (nodal) of c_g(log n) over n < N; (ii) Lipschitz-type |·| or max functionals (inertia of blocks with absolute value); (iii) Fredholm indices of pairs of g-dependent projectors. | There is a datum that makes it relevant. CALIB_R3: c_{g*}(log n) > 0 for all n = 2..14 at Mori's extremal (NUMERICAL). A sign pattern is a non-analytic invariant that **does** see the test. But it is a functional of the minimizer, so Theorem X covers it in first order. | Proving 3′: low (Zariski genericity on analytic entries; standard). The real hole is not 3′ but its scope: the non-analytic class is covered by no theorem. |
| P5 | **Theorem X** (recorded as PROVED in phase 186; hypothesis: **first-order** discriminants) | Every first-order discriminant between combs is a functional of h* (the minimizer), and new primes must cancel σ on U at resolution π/T. | **Second-order** or non-local discriminants in the minimizer: the Hessian of λ_A in a (AUDIT_203: "second variation" recorded, Danskin only gives first order), or functionals of the space of near-minimizers (κ̂ from BARRIER_EST). | None. | Extending X to second order: medium. The concavity of λ_A in a (PROVED) gives the sign of the second variation, so the second order is probably also a functional of minimizer data. Small hole. |
| P6 | **Φ.11 / 𝒦_NL as a list** (PROVED piece by piece, ARGUED as a list) and **exhaustiveness of I1–I10** (A6 (a)) | The list of nonlinear operations and inputs is an inventory, not a closure. | Any input F1–F10 outside the list: Ξ1 (ax+b von Neumann dimension, OPEN), rows 16–17 (Lorscheid, arithmetic Monge–Ampère), no object. | Not applicable: it is declared incompleteness, not an error. | Cannot be proved (inventories are not closed). |
| P7 | **Φ.13 Łoś / Ξ2** (ARGUED; Łoś CITED) | A non-standard internal normalization ν of an ultraproduct in μ falls into branches 1 or 2. An internal non-standard ν is left uncovered. | A non-standard limit μ → ∞ with internal renormalization adapted to the escape (Loeb), where ∗𝒲 ≥ 0 is proved in the model and not transferred pointwise. | None. | Lemma Ξ2.1: medium. If it comes out negative, Φ.13 rises to PROVED. |
| P8 | **(α) of C-pos / thm:noimport (iii) / O_4^ε** (CONDITIONAL on κ_T ≠ 0) | An affine gate has margin ≤ C·λ_A, or the family (1+δ)Λ violates it. Requires κ_T ≠ 0. | Affine gates in a with large margin in T with κ_T = 0: weighted dual certificates stable along the line cΛ. | Against falsity: AUDIT_203 gives slope ≈ −0.063 at c = 1 and (1+ε)Λ negative for ε ≳ 1e−68 at ½log15 (NUMERICAL-certifiable). κ_T = 0 would be a coincidence. | Low at fixed T (certify). Uniform in T: medium. |
| P9 | **BARRIER_EST: the whole class 𝓔^ℕ only qualitative** (Prop 6 PROVED qualitative; quantitative κ̂ OPEN; "classical estimates are in 𝓔" ARGUED) | For premises using Λ only at integers (not measures), the TV slack bound has no size. | An estimate with remainder whose proof is not uniform over a TV ball: uses the integrality of the frequencies log n (not perturbable). | None. thm:shape(B)'s margin ≤ 4·10⁹ T e^{−15.449T} is PROVED for **every** valid deduction. Any estimate going through here needs the same double-exponential precision. Small hole in practice. | Quantitative κ̂: high, per the audit. |
| P10 | **197's trichotomy, sub-case A2∧loose-FE** (ARGUED) and A8 (CONDITIONAL), A9 (CITED) | A class with premises A2 and a "loose" FE without Euler contains Ξ_Q or a Beurling system with Γ(s/2)^c. | Proofs using an approximate (not exact) FE plus Beurling density. DH (certified, P3) satisfies exact FE, so it alone does not cover the loose FE case. | None. | Medium: build the Beurling system with Γ(s/2)^c satisfying an approximate FE. |
| P11 | **M.i / R-Z1** (previously ARGUED; DH_TRANSFER: PROVED as a premise restriction in 𝔗₁; reassigning **nonlinear S4** to C-data/I10 is ARGUED) | Arithmetic readings across the line (moments with an Euler factor, mollifiers with μ, exact-order lower bounds) are not channel (i). | Levinson/Conrey methods (mollifiers with μ, proportion of zeros on the line) or Keating–Snaith moments with an arithmetic constant used as a **lower bound** in the form. | None. But locating zeros is S3 (REF-D), and lower moments without locating zeros have no known bridge to 𝔞_T. | Medium. |
| P12 | **C-τ** (CONDITIONAL; step 4.2 "zero off ⇒ negative form in P_T" ARGUED; L1 ARGUED on the arc \|τ\|=1) | In the Epstein family Z_τ, S_∞ has empty interior. | Methods uniform over the continuous degree-2 family Z_τ (using τ as a parameter) outside the Heegner τ_D. The certified falsifier remains x²+5y², so only what is continuous in τ and does not hold at τ = i√5 is freed. | There are citation errors: the Bateman–Grosswald threshold is 7.0556, not 7.0236, and DH II/Cassels treat Hurwitz, not Epstein. These are citation errors, not mathematical ones. | Medium. |
| P13 | **C-emb branch (d): correlations** (outside the restriction; "honest answer to B") | Outside the explicit formula, density, finite data and correlations, there is no second-order collective property of {log p} in the window. (d) is not closed by C-emb. | Hardy–Littlewood-type prime correlations (Λ∗Λ̃ at shifts, Montgomery–Vaughan with singular main terms) as a **signed second-order** input. | None. But Λ∗Λ is a "second-order relation" (C-data) within the window, by lem:spec-collapse (finite). Only the exterior version remains, which is (★★)/phase 202 (dead by criterion (a)). | Medium. |
| P14 | **L-loc** (PROVED) | Covers only **local** second variations. | Non-local potentials V_F(x) = ∫K(x,y)F… with K that sees log n. These are covered by C-pos (β) and (P1), not L-loc. | — | Not its own hole: it reduces to P1. |
| P15 | **Restriction 11 (virial, H.5 PROVED mod Lemma 4.1; NO-GO class ARGUED)** and 7 (cross-class cancellation, ARGUED), 4 (multipliers: NO-GO **only ARGUED** after retracting C Thm 6.1), 14, 15, 18, 21 (SOFT) | Reductions, not impossibilities (AUDIT_CONSTRAINTS). | 11: a flow/Grönwall argument in T from the certified boundary ½log15 proving (H) ρ_N ≤ ρ_L + A/c (necessary and sufficient condition). 7: class-diagonal bounds on Π-projected data. 4: multipliers on the exterior carrier. | 4 and 7 have a history of retraction and unproved forcing (AUD_7). | Each: medium. |
| P16 | **Φ.3 (channel I3) ARGUED, Φ.9 except τ, C-𝔖 NO-GO ARGUED, Φ.12′ ARGUED** | Individual channel lemmas. | A class weight h(D) that is not discontinuous (e.g. a Siegel average over D with smooth weight); a reading of I3 that is not DH-transportable. | None. | Low-medium. |
| P17 | **C-θ** (PROVED, only affine/Euler-segment families) | No sign information in affine families of the parameter θ. | Non-affine families in θ with an extremum at ζ (e.g. ζ^θ with θ ∉ {0,1}, degree deformations). Must be distinguished from Φ.12′ (ARGUED) and Φ.14. | None. | Low. |

Pieces that **are no longer holes**: Φ.12 (PROVED, checked against P47), R-Z1 (PROVED as a premise restriction in 𝔗₁),
G1 (PROVED: the free monoid does not distinguish ζ from Beurling; it closes only what reads **only** (ℕ^×,·)), R-Q6,
Lemma R (given Guo L4.4 CITED), C-emb (a)–(c), lem:spec-collapse, Danskin on the truncated class (PROVED; on P_T it is
inequality (2.1), PROVED). The interaction (ℕ,+)×(ℕ^×,·) is **not** closed by G1. Within the window, lem:spec-collapse
reduces it to a finite datum, but that does not close it: every proof uses finite data in each window (cor:shape(b)).

## 2. Overall reading

The barriers have two layers.

- **Hard layer (PROVED):** "if your deduction is valid for a certified falsifier, it does not prove the goal"
  (lem:transfer). This layer is unassailable, and its scope is exactly the set of **certified** falsifiers: a_P,
  cΛ at a fixed scale, Beurling (NUMERICAL), Epstein x²+5y² (T ≥ 1.59) and DH (T ≥ 9/5, CERT_DH_001).
- **Soft layer (ARGUED):** "every deduction that is not valid for a falsifier is REF-D or a datum." This is where P1,
  P2, P6, P7 and P10 live. This layer **is not an impossibility**. By the methodological rule that a route is closed
  only by a proof of impossibility within a declared class or by an explicit falsifier. The soft layer does neither.

The risk of a bookkeeping error is that the index records as NO-GO something closed only by the soft layer. Phase
201's closures ("closed as strategy") and SPEC_006 §C's (β) rows ("REF-D in disguise") are of this type. An honest
record would say "reduced to a verification of H for ζ with non-uniform input (OPEN)," not NO-GO.

## 3. The three biggest holes

Order: (size of the method space freed) × (plausibility that the piece is false or overread).

### Hole 1 — P1: "stronger" ≠ "harder" (thm:noimport (iv), C-pos (β))

- **Size:** maximum. It frees every imported positivity whose hypothesis H is not linear in the comb and is verified
  for ζ by exact structure. This is the form of every known positivity proof in analogous contexts (Weil for curves
  over 𝔽_q: Hodge index over C×C; Deligne: positivity of weighted Rankin–Selberg). In all of them, the verified
  hypothesis is stronger than the sought inequality.
- **Plausibility of overreading:** high. What is ARGUED is not a false claim, but it is used as a closure.
- **Concrete method that would pass:** an operator G_T(Λ) on the declared carrier, quadratic in Λ (not affine, so it
  dodges (α)), built with Λ∗Λ **and** the Euler product (so it dodges (i) for DH and Beurling). One of two things is
  required of it: (a) G_T(Λ) ⪰ 0 by exact factorization, G = BB* built from multiplicativity; or (b) an identity
  𝔞_T(g) = ⟨g, G_T g⟩ + (term ≥ 0 by Bochner). The identity must be exact, not an estimate, by thm:shape(B′).
- **Why it is not in the index as such:** the index records concrete objects with (β) and kills them one by one
  because "the verification is REF-D" (GL/Kreĭn, Riccati, no bound states). An H **quadratic in Λ with exact
  factorization** does not appear as a class. The closest things are SPEC_009 X1 (Rankin f×f̄, closed by Φ.12:
  "subtracting is REF-D") and Selberg forms (Q1, branch 2). Before launching, one must search ROUTES-TRIED-INDEX for
  "Gram," "Hankel," "Λ∗Λ," "BB*" and "factorization." My reading is that everything recorded is linear in Λ once the
  test is fixed, or subtracts 𝔞^ζ.
- **First lemma testing it (Lemma P1.1):** does there exist a sesquilinear form G_T(g; Λ⊗Λ) **bilinear in Λ** such that
  𝔞_T(g) − ⟨g, G_T g⟩ is comb-generic (branch 1, cancellable) and G_T ⪰ 0 is an identity of 𝔗₁ + Euler? I know of one
  obstruction: Φ.12 says that additivity in L makes 𝔞 **linear** in the logarithm of the L-function. A G quadratic in Λ
  must come from a product L·L̄ (Rankin) evaluated on the diagonal. It must be decided whether Φ.12 (PROVED) plus
  SPEC_009 Prop 19.2 already kill **every** bilinear form in Λ, or only those going through Rankin. If they kill all
  of them, P1 closes at the bilinear level and rises to PROVED in degree 2. Cost: a pencil memo.

### Hole 2 — P2: branch composition and conjunction of premises

- **Size:** large. It is literally the only format thm:shape(C) and cor:shape(b) leave alive: Euler, FE at conductor 1,
  and integrality **together**.
- **Plausibility that the rule is false:** medium. The branches are **information** classes (what the object reads),
  and a nonlinear operation between a branch-4 output (blind to ζ, positive) and a branch-3 one (functional of h*) can
  read more than each alone. The order 2≻5≻4≻3≻1 has no proof.
- **Concrete method that would pass:** an exact Schur complement (not via norms, via R-K1) where the archimedean block
  blind to ζ (branch 4, with PROVED sign: prop:archneg gives the **negative** sign from T = 0.4608, so the correct
  block must be chosen) couples with the window block through the Guo/Lemma R identity (Euler) and the gap c_N = 0
  (integrality). No certified falsifier satisfies all three premises: a_P breaks the gap, DH breaks Euler, Epstein
  breaks the degree. lem:transfer does not apply to the conjunction.
- **Why it is not in the index:** it is **partially** there. Phase 202 (exterior (★★), dead by criterion (a) in round
  2) and R-K1/Schur ("the coupling needs a sign-sensitive bound"). What would be new is attacking the **rule**, not
  the object: proving or refuting "composition falls into the worst branch." That is not recorded. New reason versus
  the index: phase 202 died from lack of a PROVED intermediate statement, not from a theorem that the conjunction is
  in one branch.
- **First lemma (P2.1):** for two objects O₁ (branch 4) and O₂ (branch 3), is any semialgebraic F(O₁,O₂) in the worst
  branch? Candidate counterexample: F = O₁ − O₂ with O₂ = 𝔞 at the minimizer (Danskin, branch 3) and O₁ archimedean.
  The difference reads exactly λ_A, i.e. branch 2. If **every** composition of two branches falls into branch 2 or the
  worst one, the rule is PROVED at composition degree 2. Cost: medium, pencil-level.

### Hole 3 — P4: the non-analytic class (Thm 3′ covers only the analytic case; Theorem X only first order)

(Initial candidate dismissed: the degree-1 DH falsifier. CERT_DH_001 and AUDIT_200_CERTDH_001 certify it, PROVED at
T = 9/5, so it is not a hole. What remains of it is h6, which only frees bounded windows.)

- **Size:** medium. It frees integer or Lipschitz invariants of the test that are not analytic in g: counts of sign
  changes (nodal) of c_g(log n) for n < N, block inertias with |·|, Fredholm indices of pairs of g-dependent
  projectors, and max/min functionals over finite families of tests.
- **Plausibility:** medium-low that something signed passes through. Thm 3′ is almost certainly true within its
  scope. The hole is one of scope, not of falsity. But there is a datum: CALIB_R3 (NUMERICAL) gives c_{g*}(log n) > 0
  for all n = 2..14 at Mori's extremal, and by Danskin ∂λ_A/∂a(n) < 0 for all n < 15. The minimizer has a **rigid sign
  pattern** on the integers. It is a non-analytic invariant that sees the test and is specific to Λ (in a_P the list
  of contacts changes).
- **Concrete method that would pass:** a Sturm/Courant-type lemma: "if 𝔞_T(g) < 0 for some g ∈ P_T, the minimizer has
  at least k sign changes in {c_g(log n)}_{n<N}," together with a **structural** proof (Euler + gap) that ζ's
  minimizer cannot have those changes. This dodges Thm 3′ (not analytic rank) and dodges Theorem X in its first-order
  form: the nodal count is not a linear discriminant, it is a topological invariant of the minimizer.
- **Why it is not in the index:** memory records "nodal explanation of the 2/3 cancellation" (phase 155, round 5) and
  "one-mode alignment FALSIFIED" (183–186), and Theorem X covers "functionals of h*." Before launching, one must
  search the index for "nodal," "Sturm," "Courant," "sign changes" and "sign pattern." If a nodal count is already
  recorded as a functional of h* with a PROVED NO-GO, the hole closes. New reason versus the index: the sign-pattern
  datum ∀n < 15 is from CALIB_R3 (phase 202/203), later than phase 155.
- **First lemma (P4.1):** for P_T at fixed T, is the condition "c_{g*}(log n) > 0 ∀n < N" **open** in the comb (stable
  at a_P, Beurling)? If it is, it is comb-generic (branch 1) and the hole closes. If it fails at a_P at n = P (the
  deleted prime), it is a legitimate non-uniform invariant and enters via (h1). Cost: low-medium (pencil plus a check
  at the a_P extremal that already exists in the pipelines).

## 4. Honest answer

**Did we make a gross mistake?** I find no evidence of one. Every PROVED exclusion I reviewed excludes what it says it
does. The recorded errors were overclaims and were corrected (thm:AL, C Thm 6.1, Cor 3.7, the false informational
reading of the DH lemma, C-τ citations). No concrete tool was discarded by a theorem that turned out false.

**Where might we be wrong?** In the **reading** of the ARGUED pieces as impossibilities:
- all of phase 201 and SPEC_006's (β) rows were closed by P1, which is a reduction, not an impossibility;
- the "joint premises" format was closed by P2, which has no proof;
- the test's non-analytic invariants (P4) are covered only in first order (Theorem X), not as a class.
(The DH falsifier is indeed certified, CERT_DH_001; that part of the barrier is solid.)

By the rule that a route is closed only by a proof of impossibility or an explicit falsifier, these three
families should appear in the index as **reduced/OPEN**, not as NO-GO.

**What already-proved tool would help if a hole is real?**
- Hole 1: **Φ.12** (transfer additivity, PROVED) gives the language for bilinear forms in Λ via products of
  L-functions; **lem:spec-collapse** ensures the verification is finite in each window; the **Guo identity / Lemma R**
  gives the radical where a BB* factorization would have to live.
- Hole 2: **Danskin / (2.1)** (PROVED) gives the "functional of h*" block with explicit gradient −2n^{−½}c_{g*}(log n);
  **prop:archneg** fixes the sign of the archimedean block; **R-Q6** says exactly where exact Λ is used.
- Hole 3: **Danskin** (sign of the gradient = sign of c_{g*}(log n)), **lem:degen** (exact affinity at the minimizer)
  and Mori's certified extremal as a test bench.

None of these tools gives a sign by itself. What these holes say is where it is **not** demonstrated that none can
exist. L′♯ OPEN. Row D OPEN.

## Labels in this memo

Inventory: a reading of the corpus (not a result). Holes 1–3: OPEN (proposed reclassification, not proved).
Lemmas P1.1, P2.1: OPEN. P4.1: OPEN. P3 closed (CERT_DH_001 PROVED). No NO-GO is added.
Suggested index action for the editor: note P1/P2/P4 as "closures by the ARGUED layer" in ROUTES-TRIED-INDEX (this
memo does not write to the index, by mandate).
