# Phase 123 — Weil-strength completion of rows A, B and C

## Objective

Replace the present coefficient-level compatibility of rows A, B and C by
one source-defined correspondence theory in which:

1. A supplies the carrier, correspondence calculus, diagonal, duality,
   intersection/trace target, numerical quotient, effectivity and
   Riemann--Roch infrastructure;
2. B constructs the arithmetic Frobenius family as actual objects of that
   calculus and proves its composition, transpose and local fixed-contact
   theorems there;
3. C proves that the trace/intersection of those objects is the nuclear
   explicit formula.

The intended comparison with Weil is structural, not literal.  The
repository already proves that finite numerical rank is incompatible with
simultaneously retaining all labels, exact multiplicative composition and
the kernel `Lambda(mn)`.  The replacement is therefore allowed to be an
infinite-rank nuclear/topological numerical theory, but it must possess the
same load-bearing operations and comparison theorems.

No Hodge sign belongs to this phase.  Row D begins only after A/B/C have
been constructed without using zeros of zeta or positivity of the Weil
form.

## Required dependency order

```text
A0 source geometry and coefficient category
  -> A1 localized mixed kernels/endocorrespondences
  -> A2 composition, identity and transpose
  -> A3 diagonal trace/intersection and determinant
  -> A4 numerical equivalence, completion and effectivity
  -> A5 mixed Riemann--Roch/equality infrastructure
  -> B1 lift Gamma_n into A
  -> B2 convolution composition and local fixed contact
  -> C1 summable completion
  -> C2 categorical trace = Meyer nuclear supertrace
  -> C3 explicit formula as a theorem in the A-intersection theory
  -> D (separate goal: independent Hodge/sign theorem).
```

An arrow is green only if it is labelled `PROVED-IN-REPOSITORY` or
`IMPORTED` with an exact hypothesis map.  A definition, analogy, scalar
coefficient match or numerical experiment cannot discharge an arrow.

## Row A work programme

### A0 — freeze the category and remove row conflation

Define a Weil-strength A-contract which is independent of the special
labels `n`, `Lambda(n)`, the explicit formula and every sign statement.
Audit the present tuple `A_DN` against that contract.  In particular:

* the reduced contact and the nuclear Dirichlet module remain admissible
  source infrastructure;
* the equations `ell(delta_n)=Lambda(n)` and the selected family `rho_n`
  are outputs of B/C, not axioms certifying A;
* the quotient-defined Green line is not counted as an independently
  constructed Green current.

### A1 — mixed correspondence carrier

Construct a category `Corr_A` over the same arithmetic carrier, beginning
with the mixed endomorphism corner of `N_DN` and promoting it to localized
kernels or an equivalent Morita endofunctor model.  Required data:

* restriction and descent;
* compact/perfect and nuclear admissibility classes;
* a diagonal unit;
* closure under finite sums, completion and composition;
* a faithful localization functor to the existing nuclear global sector.

The preferred geometric formula is

```text
K star L = Rp13_!(Lp12^* K tensor^L Lp23^* L)
```

on the triple product.  It may be used only after the required pullback,
pushforward, projection-formula and Beck--Chevalley statements have been
constructed for the chosen spherical/periodic coefficient category.  If a
Morita endofunctor model is used instead, a localization theorem back to the
carrier is mandatory.

### A2 — transpose and diagonal

Construct an involution `dagger` before specializing to arithmetic labels,
prove `(K star L)^dagger = L^dagger star K^dagger`, and identify the
diagonal kernel as the two-sided unit.  A metric adjoint selected only after
seeing the desired scalar pairing is inadmissible.

### A3 — intersection/shadow

Construct a trace or shadow

```text
Tr_A : Corr_A^tr -> Pic/Perf/nuclear trace target
```

from diagonal pullback or categorical trace.  Prove cyclicity, additivity,
localization, determinant compatibility and finiteness/summability on its
declared domain.  The scalar functional `ell` may be compared with this
trace later; declaring `Tr_A(delta_n)=Lambda(n)` is not a construction.

### A4 — numerical theory and topology

Define numerical equivalence as the radical against all admissible test
correspondences, prove that composition and transpose descend, and specify
the Hausdorff nuclear completion.  Construct the two ruling classes and a
mixed sector in the same quotient.  Finite abelian rank is explicitly not
required; separatedness and continuity are.

Construct an effective cone independently of the Weil-form sign and prove
that it is stable under the operations actually used downstream.

### A5 — mixed RR infrastructure

Extend the intrinsic periodic determinant from the two rulings to the
admissible mixed kernels.  Prove a Riemann--Roch/equality formula in the
trace target, principal invariance, restriction compatibility and
continuity.  This stage does not prove a Hodge index theorem.

### A closure criterion

Row A is complete only when A0--A5 are green and the resulting structure is
non-vacuous on mixed kernels.  In particular, neither the current ruling
form nor the existing global Dirichlet algebra alone closes A.

## Row B work programme

1. Construct a functor from the Witt/cyclotomic source to `Corr_A`.
2. Show that each `Gamma_n` is an admissible mixed kernel, not merely a
   tuple in a product category.
3. Derive `Gamma_m star Gamma_n ~= Gamma_mn` from A-composition.
4. Construct transpose/Rosati compatibility and the self-dual metric
   normalization.
5. Derive the local Lefschetz complex from diagonal contact, retaining the
   full derived object; justify every later truncation.
6. Prove the determinant mass `Lambda(n)` from the cyclotomic calculation.

## Row C work programme

1. Construct the summable completion of finite linear combinations of the
   B-kernels inside the A-trace domain.
2. Prove convergence and cutoff independence for finite, archimedean and
   polar contributions.
3. Construct a comparison functor to Meyer's Poisson quotient.
4. Prove that `Tr_A` is carried to Meyer's nuclear supertrace.
5. Only then invoke Meyer's character theorem to identify the result with
   the explicit formula and `B_nuc`.

## Adversarial controls

Every proposed A/B/C construction is tested on:

* a smooth projective curve over a finite field, where it must recover the
  ordinary kernel/intersection formalism;
* finite sets of two and three primes, where mixed rank and composition are
  visible;
* a generic commutative nuclear algebra with the same labelled
  multiplication, which must not automatically manufacture arithmetic
  geometry;
* Dedekind and shifted rank-two analogues, to expose accidental use of
  zeta-specific positivity;
* the existing finite-rank obstruction and raw-section growth obstruction.

## Stop rules

* A graph-image product of unrelated decorations is not a kernel category.
* A coefficient equality is not an intersection theorem.
* A Green line defined as `RR/contact` is not independent Green geometry.
* A quotient defined to kill the comparison error is not a geometric
  comparison unless its universal meaning is separately proved.
* No finite-rank Neron--Severi claim may contradict the proved
  `Lambda(mn)` rank obstruction.
* No statement from D, RH, the zeros of zeta or positivity of `B_nuc` may
  enter a definition in A, B or C.

## Deliverables

* `P123_A_ACCEPTANCE_SPECIFICATION.md` — the exact A contract.
* `P123_001_A_BASELINE_AND_MIXED_ENDOMORPHISM_CORNER.md` — first A
  construction and honest boundary.
* `P123_002_COEFFICIENT_TRACE_AND_SEPARATED_MIXED_CORNER.md` —
  source-defined coefficient trace before arithmetic scalarization.
* `P123_003_DAGGER_COMPLETE_RATIONAL_KERNEL_ALGEBRA.md` — the rational
  dilation completion forced by transpose/Rosati.
* `P123_004_SEMILOCAL_CROSSED_PRODUCT_SOURCE_AUDIT.md` — imported
  algebraic localization and exact boundary of the semilocal trace theorem.
* `P123_005_STRICT_LABEL_SHEAF_AND_GENERIC_COMPLETION.md` — strict label
  descent and the completed generic stalk.
* `P123_006_COMPLETE_SEMILOCAL_KERNEL_SHEAF.md` — complete action-groupoid
  kernel sheaf, composition, unit, dagger and fixed-point trace core.
* `P123_007_SOURCE_NUMERICAL_INTERSECTION_QUOTIENT.md` — source intersection,
  closed numerical radical and complete mixed numerical quotient.
* `P123_008_HYPERBOLIC_TATE_REALIZATION.md` — scalar-augmentation no-go,
  two-jet replacement and the first common bridge to the ruling plane.
* `P123_009_LOCAL_EXCESS_LEFSCHETZ_RR.md` — perfect off-identity excess
  complex and local determinant/diagonal-trace equality.
* `P123_010_SOURCE_EFFECTIVE_CONE.md` — source square cone, functoriality
  and honest boundary after numerical quotient.
* `P123_011_FINITE_FIELD_WEIL_CONTROL.md` — exact perfect-kernel control
  model recovering Weil's graph/intersection architecture.
* `P123_012_RENORMALIZED_RELATIVE_DETERMINANT.md` — trace-class cutoff
  determinant, generic-orbit renormalization and identity-label limit.
* `P123_013_INTERNAL_GAUGE_VS_EXTERNAL_SCALING_AUDIT.md` — correction of
  the internal/external group conflation and specification of the true
  idele-class bimodule carrier.
* `P123_014_EXTERNAL_IDELE_CLASS_BIMODULES.md` — lift-independent external
  correspondence bimodules, Fell core and true Tate/ruling realization.
* `P123_015_COMPLETED_EXTERNAL_FELL_CARRIER.md` — lift-cocycle completion,
  nuclear represented trace ray and determinant continuity.
* `P123_016_GRAPH_KERNEL_LOCALIZATION.md` — quotient-stack square and
  equality of graph pull--tensor--push with external bimodule tensor.
* `P123_017_TATE_REFINED_NUMERICAL_QUOTIENT.md` — vector numerical
  equivalence, primitive/ruling exact sequence and separating completion.
* one note per A1--A5 gate, including no-go notes for failed candidates;
* a theorem-level dependency graph and provenance ledger;
* corresponding B and C specifications only after A is closed;
* updates to paper 42 only after the new results survive the phase audit.
