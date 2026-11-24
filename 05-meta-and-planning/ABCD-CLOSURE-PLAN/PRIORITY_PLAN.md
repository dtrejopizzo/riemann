# Plan to close A and choose the route toward RH

Planning document, to be executed later with another model. It does not prove A or RH and does not modify the papers.

## 1. Recommended decision

To **close A**, concentrate the next campaign on the link between integral geometry, duality, and the metrized determinant. Suspend the expansion of boundary profiles as an autonomous line: take it up again only if a concrete proof of that link needs an estimate that is still missing.

To **prove RH**, do not impose a prior requirement of closing all of A. The analytic first-contact route allows a shorter attack in terms of dependencies, supported by phases 118–122. Its central arithmetic law remains unproved. Having fewer dependencies does not license the claim that it is mathematically easier.

The first execution will carry out two bounded feasibility studies: one on A, another on the first-contact law. It will choose the subsequent work by the mathematical mechanism obtained, not by the number of lemmas, rounds, or reformulations. If the objective of that execution remains exclusively on A, the direct study is kept as a reference and does not displace its construction.

There is no basis for promising a fast closure. There is a basis for eliminating redundant work and attacking first the obstacles that can invalidate an entire construction.

## 2. Documentary basis and precedence

123 `phase-*` directories and 42 numbered paper directories were checked. This planning used the general indexes, the earlier coverage, searches directed by three independent reviews, and a reading of decisive sources. It does not constitute a full reading nor a new audit of the proofs in every file.

The contract governing A is [P123_A_ACCEPTANCE_SPECIFICATION.md](../../03-research/phase-123-weil-strength-abc/P123_A_ACCEPTANCE_SPECIFICATION.md). The historical label "A closed" in restricted contracts does not satisfy that contract. Its ten clauses are not reduced in this plan.

Working sources the executor should load, without re-reading the whole corpus:

| Topic | Source and use |
|---|---|
| Actual scope of A/B/C | [Reference audit](../../03-research/phase-122-row-d-integrity-and-construction/P122_ROWS_ABC_REFERENCE_AUDIT.md): distinguishes decorated objects, the Meyer character, and geometric intersection. |
| Coefficients and localization | [P123.121](../../03-research/phase-123-weil-strength-abc/P123_121_COMMON_SMOOTH_ZERO_STRATIFIED_SOURCE.md), [122](../../03-research/phase-123-weil-strength-abc/P123_122_DERIVED_COMMON_SOURCE_COMPOSITION.md), [123](../../03-research/phase-123-weil-strength-abc/P123_123_EQUIVARIANT_SEMILOCAL_COMPOSITION.md), [124](../../03-research/phase-123-weil-strength-abc/P123_124_COMMON_SOURCE_LOCALIZED_DERIVED_TENSORS.md), [125](../../03-research/phase-123-weil-strength-abc/P123_125_ZERO_STRATUM_DERIVED_QUOTIENTS.md): reuse their exact domains, do not import a stronger monoidality. |
| Duality and contacts | [A_DUALITY_WORK.md](../../03-research/phase-123-weil-strength-abc/A_DUALITY_WORK.md): read the relevant headers and the later corrections. Contains derived contacts, transport of the unit, strong-dual obstruction, and profiles. |
| Metric | [A_MIXED_METRIC_WORK.md](../../03-research/phase-123-weil-strength-abc/A_MIXED_METRIC_WORK.md): analytic determinants available; the geometric map and the comparison with rulings are missing. |
| Sign law | [Closure 120](../../03-research/phase-120-global-polarization/PHASE_120_CLOSURE.md), [P122.008](../../03-research/phase-122-row-d-integrity-and-construction/P122_008_PHASE121_LOAD_BEARING_AUDIT.md), [P122.028](../../03-research/phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md): signed identity, detectors, and an arrow that is still open. |
| Li alternative | [Restart frontier](../RH-MASTER-CONTEXT/LIVE_FRONTIER_AND_RESTART_PLAN.md), papers [37](../../04-papers/37-limits-of-the-positivity-family/main.tex) and [38](../../04-papers/38-li-fir-stability/main.tex): one-sided target and the limits of the filters. |

The old indexes guide searches; a later specific correction prevails over their labels. Do not repeat the existing certificates or contact computations unless their entries, their category, or the hypothesis intended for use change.

## 3. Does A exist in the literature?

**No construction satisfying A.1–A.10 jointly was found.** This is the outcome of this directed search, not a nonexistence theorem. Important components were found, along with a concrete import opportunity:

| Primary source | What it offers | What is missing for our A |
|---|---|---|
| Connes–Consani, [On the Jacobian of Spec Z, 2602.15941](https://arxiv.org/html/2602.15941) | A monoid of rank-one arithmetic divisors with a seminorm, an adelic interpretation, and associated sheaves; at infinity, a unit-ball condition on sections. | A stable category of mixed correspondences over the square and its RR. It is the first candidate for preserving the integral/metric datum that the purely complex model loses. |
| Connes–Consani, [Absolute Geometry, 2606.06604](https://arxiv.org/html/2606.06604) | The absolute sheaf, description of stalks, perfectoid points, and relation to Tate curves and Fargues–Fontaine. | An identification of points or symmetries does not import composition of kernels, global duality, or intersection. |
| Connes–Consani, [Riemann–Roch for the ring Z, 2306.00456](https://arxiv.org/abs/2306.00456) and [Scaling Site, 1603.03191](https://arxiv.org/abs/1603.03191) | RR in their respective settings: divisors on the arithmetic curve and periodic orbits. | Mixed RR over the square. Do not substitute a one-dimensional result for the required result. |
| Connes–Consani, [Riemann–Roch strategy, 1805.10501](https://arxiv.org/html/1805.10501) | Adelic complex lifting, tropical descent, and a strategy for the existence of sections. The introduction identifies the difficulty of the cohomology of the square. | It is a route for investigating A.7/A.8, not the full theorem being sought. |
| Cisinski–Tabuada, [1111.0257](https://arxiv.org/html/1111.0257), theorems 1.7 and 1.11 | Noncommutative Lefschetz and HRR; explicit smoothness/properness hypotheses depending on the result. | Proving that the relevant arithmetic domain satisfies the hypotheses; also constructing the metric comparison. Fréchet nuclearity does not imply dg properness. |
| Marcolli–Tabuada, [1105.2950](https://arxiv.org/abs/1105.2950) | Intersections via Hochschild and numerical equivalence in noncommutative motives. | Realization of our source, topology of the completed quotient, and preservation of the mixed sector. It does not automatically import the infinite-rank theory. |
| Deninger, [2508.05329](https://arxiv.org/abs/2508.05329), §5 | Rational Witt vectors as finite relative correspondences under precise algebraic hypotheses. | A functor toward the square of A and a derived diagonal contact. It helps B; it does not define A via Lambda values. |
| Meyer, [math/0412277v3](https://arxiv.org/abs/math/0412277v3) | Nuclear realization and a character formula. | Identifying that character with the geometric shadow of A. It is imported in C. |
| Connes–Consani–Moscovici, [Zeta Spectral Triples, 2511.22755](https://arxiv.org/html/2511.22755#S8) | Spectral approximants; §8 states as pending the simplicity/parity of the minimum and the eigenvector approximation that would allow convergence. | It does not provide the positivity or limiting identification that would close RH. |

The local sources `2510.08033` and `2512.01811` from `00-references/papers-nuevos/arithmetic-intersection-theory` were also reviewed: their results on ordinary arithmetic surfaces require a geometry whose identification with our square is not constructed. The bridge [Morishita, 2508.15971](https://arxiv.org/abs/2508.15971), theorem 3.6 of local version v5, gives compatible maps of flows/orbits, not an equivalence of cohomologies with polarization.

**Proposed priority import:** divisor and section geometry from 2602.15941 + the common source P123.121–125 + relative computation of kernels. The realization that unites them is a new, explicit problem; it is not claimed to exist merely by combining these references.

## 4. First campaign on A: two decisive feasibility tests

### A-V1. Geometric realization and duality in the same category

**Inputs:** common source P123.121–125; divisor sheaves of the Jacobian; classical duality and the boundary triangle from `A_DUALITY_WORK.md`.

**Candidate:** geometrically localized correspondences, with relative support/perfection conditions that allow composition, and a realization in bimodules of the common source. The diagonal must remain the full unit. Keep the domain of correspondences and the traceable ideal separate.

Concrete work:

1. Define the realization functor on divisor sheaves and general finite correspondences, before choosing B's arithmetic family. Specify which category preserves the metric restrictions when passing to a stable context. A stable envelope by itself does not prove that preservation.
2. Require in a single domain the diagonal, both rulings, and nonzero mixed contacts, together with their cones and compositions. The analytic contacts already built serve to detect information loss; they are not automatically the arithmetic contacts of B.
3. Seek duality via relative adjoints and the dualizing object. Compute its square, including the possible Serre twist. If a dualizing square root is proposed, construct it or explain its descent; do not choose it tacitly.
4. Apply the candidate to the source triangle `I -> B -> B/I`. Compute the images of its arrows, the bidual, and the evaluation. This test must overcome the already-documented boundary loss of the strong Hom quotient.
5. Prove composition reversal, fixed unit, and semilocal compatibility. Switch to condensed/bornological categories only if it is shown how they resolve this test; the name of the formalism is not a proof.

**Output that justifies continuing:** a real functor and duality on a domain containing the above objects, with a precise list of the extensions still needed. **Discard output:** a counterexample to biduality, loss of the contact, or an unavoidable twist incompatible with A.4. A local result is not labeled as global A.4.

### A-V2. Extension of the intrinsic determinant, before enlarging completions

**Inputs:** same A-V1 candidate; rulings and their intrinsic norm; contact determinants and their equation-change laws; `A_MIXED_METRIC_WORK.md`.

Concrete work:

1. Build from the sections of the source the determinant datum intended for extension. Distinguish absolute perfect complexes, relative determinants with a perfect cone, and nuclear determinants. Do not take the ordinary determinant of an infinite complex.
2. Compare objects and trivializations in the ruling–ruling, ruling–mixed, and mixed–mixed sectors. The first sector must recover the norm `exp(-d1*d2)`, with the correct convention between the norm and its square.
3. Compute the changes under substitution of a local equation by a unit, addition of divisors, and semilocal change. Use the resultants and unit norms already obtained for contacts; compute the discrepancy cocycle that still separates the two realizations.
4. Prove that this cocycle admits the canonical trivialization required by the geometry and that it preserves the metric. An equality of curvatures at zero, or adjusting a constant so that numbers match, does not give that trivialization.
5. Declare an effective class from sections/cycles of the source. Do not take as effective every object of a stable category, since their shifts change the sign in K0. Nor identify it with sums of squares of operators.

**Output that justifies continuing:** a natural comparison of metrized lines in a genuinely mixed sector, with the principal invariance and an explicit mechanism for extending it. **Discard output:** the realization erases the integral datum of the sections, the metric does not descend, or the comparison requires assuming the desired Weil form/sign.

Both tests are architecture filters, not a promise that the candidate will pass. If one fails, the next task is its concrete mathematical obstruction or a candidate that changes it; not more boundary profiles unrelated to it.

## 5. Full program for A once a viable candidate is chosen

| Package | Construction work | Closure criterion and clauses |
|---|---|---|
| A-I: source and geometry | Extend the realization to all declared charts; localize on the square; descent and triple coherence. Reuse the existing relative derived tensors. | A single carrier and stable geometric domain: A.1, A.2. |
| A-II: operations | Extend composition and duality from A-V1; prove stability under the chosen completion, continuity, and the full unit. | Composition, biduality, and reversal formulas valid in the same domain: A.3, A.4. |
| A-III: shadow | Build the cyclic diagonal shadow before scalarizing, distinguish excess contacts, and prove localization. Compare it with the determinant on its allowed domain. | A.5 with explicit target and limits. The unit does not need a finite scalar trace. |
| A-IV: numerical | Define the radical against ALL traceable tests. Prove ideal-ness, dagger-stability, closure, Hausdorff quotient, and continuity of operations. | A.6 with a ruling plane and a nonzero mixed sector of rank compatible with the full kernel; injectivity of a local sector is not enough. |
| A-V: effectivity and RR | Extend A-V2: principal invariance, biextension, restriction, convergence, and RR equality; prove the effectivity descent actually used. | A.7, A.8. If the subsequent Hodge route uses growth of sections, also prove the necessary existence inequality; a determinant degree does not substitute for it. |
| A-VI: comparison and closure | Classical control via a typed functor: finite curves, non-invertible finite graphs, diagonal, transposition, intersection, and effect. Review independence from B/C/D. | A.9, A.10, and a joint audit of A.1–A.10. |

The classical control is used from A-V1 onward to rule out errors; A-VI checks its compatibility with the final construction. The packages are not six known theorems waiting to be transcribed: A-I, A-II, and A-V contain genuine research problems.

**Closure of A:** all clauses satisfied within the same theory, with no conditional arrows. If only one sector is closed, report which one and which global clause remains pending.

## 6. B/C/D if the Weil-type proof is continued

**B — moving from labels to geometric contacts.** Realize the Witt correspondences via the functor compatible with A. Derive the diagonal contact that produces the cyclotomic complex, instead of attaching it as decoration. Prove the result for the general family; the comparison between a prime, its square, and a product of primes detects whether an incorrect linear contact was obtained. Do not repeat small proofs that already exist without a change of construction. Unit/excess is handled separately. The mass `log|Phi_n(1)|` is deduced at the end.

**C — a single comparison theorem.** Build a realization of A's shadow inside Meyer's Poisson complex that preserves the action, duality, and Tate terms. Prove that the finite contact, the Gamma term, and the identity excess together give the explicit formula, first on a common kernel and then on the domain sufficient for Weil. A coincidence of coefficient lists does not substitute for that functor. Declare the order of limits; do not impose uniformity over all windows if controlling each compact support suffices.

**D — choose one of two proofs.** Either the Hodge index via the geometry/effectivity and RR already built, or the arithmetic first-contact law of the next section. Do not require solving both. In either case the primitive sign must be proved, without building it into the definition of the metric or the cone. Semidefiniteness suffices if it covers the criterion used; do not add an unnecessary global equality classification.

A direct proof of RH does not retroactively fill in the functors of A/B/C nor an entire geometric version of D.

## 7. A more direct route: sign via first contact

This is the priority alternative for an RH attempt with less prior construction. It reuses [P122.002](../../03-research/phase-122-row-d-integrity-and-construction/P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md), the existing initial certificate, and the corrections from [P122.008](../../03-research/phase-122-row-d-integrity-and-construction/P122_008_PHASE121_LOAD_BEARING_AUDIT.md).

The analytic goal is to prove `q_T(F)=-B_nuc,T(F,F)>=0` for every window and every primitive test in its domain. A failure past the certified window provides, under the hypotheses of the first-contact theorem, a nontrivial null state. It remains to exclude it arithmetically.

The computation available is

```
E_eff(F) = ||(E_q,T - E_p,T) h_F||^2 / log(q/p).
```

The harmonic equation only forces constant flow. It does not force zero energy. The new task is to obtain from the arithmetic source, for the first-contact state, the critical transmission and the gluing that annihilate the defect. The exact specification of the two conditions is in [P122_D_SPECIFICATION.md, §8](../../03-research/phase-122-row-d-integrity-and-construction/P122_D_SPECIFICATION.md) and its boundary condition in [P122.029](../../03-research/phase-122-row-d-integrity-and-construction/P122_029_LIONS_MAGENES_TRANSMISSION_AUDIT.md).

Order of attack:

1. Work on the full source with the additive successor, multiplicative isometries, and Gamma already built; write a candidate global relation with all its boundary terms.
2. Derive a Green/reciprocity identity for that relation. Identify the step that selects real arithmetic data and the two orientations before they are lost in the trace.
3. Prove the required critical transmission condition and the vanishing of the flow. They must be consequences, not conditions added to the definition of the state.
4. Apply the rigidity already available, with ALL its hypotheses, to exclude the first contact. Pass by exhaustion to the Weil domain.

**First deliverable:** a global identity with a controlled new term, or a refutation of the candidate relation. Not another equivalent zero-flow detector.

The factorization `q=||X F||^2-||Y F||^2` and a contraction that would imply the sign are legitimate coordinates of the problem. Their equivalence with RH does not rule them out; it requires proving the contraction from new arithmetic properties. The corpus's no-go results are used only with their exact class of hypotheses.

## 8. Other routes and the criterion for changing priority

| Route | Remaining useful objective | When to activate it |
|---|---|---|
| First contact | A global law that rules out a nontrivial null state at the first loss of sign. | First direct alternative, since the detector, regularity, and reduction are already available. |
| Connes–CCM spectral | Necessary simplicity/parity and an estimate identifying the real-spectrum approximants with Xi in a sufficient holomorphic topology. | Only if a new gap/residue control and normalization appear that survive the limit. Numerical closeness or finite self-adjointness is not enough. |
| Li–Laguerre | A signed one-sided bound for all indices, with a paired prime–pole continuation. | If a compensating arithmetic identity or a uniform sign-preserving estimate appears. |
| Full Weil | Strong A, realization B, comparison C, and sign D. | Priority for closing A as a theory, or if the new geometry produces the sign mechanism missing from the direct routes. |

Alternative exact target of Li, in the conventions of the restart frontier:

```
f_(n,eps)(y) = y^(-1-eps) L_(n-1)^(1)(log y),
lambda_n^prime
 = lim_(eps down to 0) integral_1^infinity (psi(y)-y+1) f'_(n,eps)(y) dy,
lambda_n^prime >= -lambda_n^arch  for n>=8.
```

The range 1–7 has a separate certificate on that frontier. The paired limit, the dependence on n, and the tails are obligations of the theorem; no manipulation of separated divergent sums is admissible. The paper 38 filters do not prove this bound.

In the spectral variant, first fix a nonzero normalizer and the complex domain of convergence. Uniform local holomorphic convergence to a function that is not identically zero would allow using Hurwitz to exclude zeros off the line in that domain. Justifying precisely that convergence, and its coverage of the possible zeros, is the problem; it is not assumed.

## 9. Economical execution and deliverables

Use automatic tools for source extraction, hypothesis checking, and a first construction per package. An independent review should concentrate on the new decisive arrow, not re-read every inherited lemma. Another model is an option for the author if available in their round; it is not required for this plan.

First round, at most two independent mathematical jobs:

1. **Job A:** solve A-V1 and formulate the concrete cocycle/obligation of A-V2 on that same candidate. If duality fails, deliver its obstruction before building further completions.
2. **Direct job:** propose and analyze a single global first-contact law using the data from phases 120–122. If the assignment is exclusively to close A, replace it with A-V2 starting from an explicit common-source interface.

A main line is then chosen. Do not simultaneously launch separate Hodge, KYP, de Branges, Fock, entropy, and positivity projects if they end in the same contraction without a new mechanism.

Each deliverable must contain only:

- a new statement with quantifiers and domain;
- a proof, or the precise step that remains open;
- imported references with their hypotheses verified;
- the clause of A or the arrow toward RH that changed;
- the next concrete task, if there is progress that justifies it.

A refuted attempt rules out that attempt. A difficult theorem that is still open is not declared impossible or closed. Notation is not changed to simulate progress.

**Do not create new phases, expand memories, or edit papers during this first campaign.** Keep only the mathematical deliverable needed to evaluate the route. Do not regenerate certificates already accepted as routine.

## 10. Hand-off task statement

> Execute the plan PRIORITY_PLAN.md, starting with A-V1. The goal of this execution is to produce a realization functor and a contravariant duality in the same category that contains the unit, rulings, and a mixed contact, or to isolate its concrete obstruction. Use P123.121–125 and the corrections from A_DUALITY_WORK; do not repeat local constructions already on record. Investigate importing the Connes–Consani divisor sheaves from 2602.15941 while preserving their integral and metric data. Test early the triangle I→B→B/I and the bidual twist. Do not confuse a covariant involution with a dagger, a category of contacts with the global unit, or nuclearity with properness. If that architecture works, move to A-V2 before enlarging the completions. Do not edit any paper. Report the new arrow proved, the hypotheses that remain open, and the exact scope. Do not declare A closed until A.1–A.10 are satisfied.

To prioritize RH instead of A, replace the first task of the task statement with section 7. That change keeps A's results as resources but does not require completing an entire geometric theory before attacking the sign.
