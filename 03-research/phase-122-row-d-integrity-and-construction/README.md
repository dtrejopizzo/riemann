# Phase 122 — row (d): integrity audit before construction

## Status

Active.  No proof of row (d), no construction of `D`, and no first-contact
state is assumed at entry.

Phase 121 isolated a plausible terminal implication

\[
 P_T\mathscr A_TF=0\quad\Longrightarrow\quad c^{(1)}(F)=0,
\]

and constructed several faithful coordinates for its conclusion.  It did
not prove the implication.  This phase first checks every load-bearing arrow
needed to make that implication the unique remaining arrow.  Only after that
audit may a new object be promoted as a candidate for row (d).

The working plan is [`PLAN.md`](PLAN.md).  The initial dependency finding is
[`P122_001_FIRST_CONTACT_ATTAINMENT_AUDIT.md`](P122_001_FIRST_CONTACT_ATTAINMENT_AUDIT.md).
Its analytic gap is resolved, conditional on the separately audited strict
base certificate, by the compactly whitened argument in
[`P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md`](P122_002_FIRST_CONTACT_COMPACTNESS_THEOREM.md).

The current integrity results are:

* [`P122_DEPENDENCY_GRAPH.md`](P122_DEPENDENCY_GRAPH.md): exact A/B/C/D DAG;
* [`P122_ROWS_ABC_REFERENCE_AUDIT.md`](P122_ROWS_ABC_REFERENCE_AUDIT.md):
  primary-source and scope audit;
* [`P122_003_CRITICAL_DENSITY_DEPENDENCY_AUDIT.md`](P122_003_CRITICAL_DENSITY_DEPENDENCY_AUDIT.md):
  replaces an unnecessary 2026 dependency by Conrey's classical theorem;
* [`P122_004_RETRACTED_LOG5_CERTIFICATE_AUDIT.md`](P122_004_RETRACTED_LOG5_CERTIFICATE_AUDIT.md):
  prevents reuse of the superseded D.181 claim;
* [`P122_005_PORT_SWAP_INFORMATION_LOSS_THEOREM.md`](P122_005_PORT_SWAP_INFORMATION_LOSS_THEOREM.md):
  proves why scalar row-C data cannot recover the missing oriented defect;
* [`P122_006_NEGATIVE_MINIMIZER_PRINCIPAL_PART_NO_GO.md`](P122_006_NEGATIVE_MINIMIZER_PRINCIPAL_PART_NO_GO.md):
  retires the purely local version of Track II;
* [`P122_007_EXISTING_ARITHMETIC_HODGE_APPLICABILITY_AUDIT.md`](P122_007_EXISTING_ARITHMETIC_HODGE_APPLICABILITY_AUDIT.md):
  proves that existing Arakelov Hodge-index theorems do not type-check on
  the spherical/decorated carrier;
* [`P122_008_PHASE121_LOAD_BEARING_AUDIT.md`](P122_008_PHASE121_LOAD_BEARING_AUDIT.md):
  classifies every terminal phase-121 result and freezes the one open arrow;
* [`P122_009_GLOBAL_RECIPROCITY_DOES_NOT_GIVE_AEIF.md`](P122_009_GLOBAL_RECIPROCITY_DOES_NOT_GIVE_AEIF.md):
  rules out an unweighted product-formula closure of the oriented carrier;
* [`P122_010_SECOND_ORDER_RECIPROCITY_CURVATURE_NO_GO.md`](P122_010_SECOND_ORDER_RECIPROCITY_CURVATURE_NO_GO.md):
  shows that even a mixed second variation of the flat product formula
  cannot create the positive residue square;
* [`P122_011_SINGULAR_COMMUTATOR_DOMAIN_WALL.md`](P122_011_SINGULAR_COMMUTATOR_DOMAIN_WALL.md):
  proves that divisor-singular commutators are admissible only after their
  target residue vanishes, while regularization supplies no vanishing upper
  bound;
* [`P122_012_DETERMINANT_SYMBOL_AND_QUILLEN_AUDIT.md`](P122_012_DETERMINANT_SYMBOL_AND_QUILLEN_AUDIT.md):
  isolates the exact algebraic determinant skeleton available in the
  literature and the missing Hermitian/global realization needed here;
* [`P122_013_LOCAL_EULER_DETERMINANT_LINE.md`](P122_013_LOCAL_EULER_DETERMINANT_LINE.md):
  constructs from each degree-one Euler factor an oriented Hermitian line
  with canonical positive rank-one curvature and identifies its still-open
  global metric trivialization;
* [`P122_014_NAIVE_GLOBAL_DETERMINANT_ASSEMBLY_NO_GO.md`](P122_014_NAIVE_GLOBAL_DETERMINANT_ASSEMBLY_NO_GO.md):
  proves that direct tensor/dual assembly has curvature exactly `q_T`, so
  asserting its semipositivity would merely restate row (d);
* [`P122_015_EULER_CONTOU_CARRERE_DETERMINANT_BRIDGE.md`](P122_015_EULER_CONTOU_CARRERE_DETERMINANT_BRIDGE.md):
  proves that orientation, `1-p^(-1)` normalization, von Mangoldt
  connection and rank-one curvature descend from one analytic Hardy loop
  pair, and separates this cocycle from the algebraic tame/CC symbol;
* [`P122_016_SEMIFINITE_BOHR_DETERMINANT_CARRIER.md`](P122_016_SEMIFINITE_BOHR_DETERMINANT_CARRIER.md):
  proves that ordinary restricted determinants fail by continuous
  multiplicity and constructs the canonical semifinite Bohr-flow carrier
  for all active Euler factors;
* [`P122_017_BOHR_CENTRAL_COCYCLE_SPLITTING.md`](P122_017_BOHR_CENTRAL_COCYCLE_SPLITTING.md):
  proves that the native determinant cocycle still splits prime by prime,
  so the missing Gamma coupling must be a relative correspondence rather
  than another cocycle on the same Bohr algebra;
* [`P122_018_GLOBAL_GAMMA_EULER_COCYCLE_PARITY_NO_GO.md`](P122_018_GLOBAL_GAMMA_EULER_COCYCLE_PARITY_NO_GO.md):
  proves that the symmetrically regularized Gamma--Euler cocycle vanishes by
  parity and that every nonzero candidate anomaly is necessarily the
  one-sided incoming history;
* [`P122_019_CRITICAL_SOBOLEV_TATE_JUMP_GATE.md`](P122_019_CRITICAL_SOBOLEV_TATE_JUMP_GATE.md):
  proves that the forced incoming Tate current has nonzero integer-activation
  jumps and therefore cannot lie in the critical determinant class
  `H^(1/2)` unless its Tate coefficient vanishes;
* [`P122_020_TWO_GATE_D_CLOSURE_CRITERION.md`](P122_020_TWO_GATE_D_CLOSURE_CRITERION.md):
  proves that a determinant-domain trace theorem followed by one horizontal
  two-prime seam identity would exclude first contact and conditionally
  close row (d), while recording both bridge theorems as still open;
* [`P122_021_SHARP_WINDOW_CALDERON_TRACE_NO_GO.md`](P122_021_SHARP_WINDOW_CALDERON_TRACE_NO_GO.md):
  proves that sharp-window causal translation destroys endpoint
  `H^(1/2)` regularity, so Gate R must be a genuine horizontal transmission
  law rather than a formal identification of Bohr and physical trace norms;
* [`P122_022_STIRLING_RELATIVE_GAMMA_DETERMINANT.md`](P122_022_STIRLING_RELATIVE_GAMMA_DETERMINANT.md):
  extracts the universal nonrestricted Stirling chirp and proves that the
  residual quarter-Gamma scattering lies in the genuine restricted
  determinant class, constructing the archimedean relative line without
  claiming the still-missing transmission theorem;
* [`P122_023_STIRLING_FROBENIUS_CANONICAL_RELATION_NO_GO.md`](P122_023_STIRLING_FROBENIUS_CANONICAL_RELATION_NO_GO.md):
  identifies the canonical scale relation `phi_St'(tau)=log n` at
  `|tau|=2 pi n`, but proves that the exact Stirling/Gamma multiplier
  commutes with all Euler translations and couples them only after the
  already-known sharp-window boundary defect is introduced;
* [`P122_024_AFFINE_INTEGER_GAMMA_EULER_CARRIER.md`](P122_024_AFFINE_INTEGER_GAMMA_EULER_CARRIER.md):
  constructs a single affine integer carrier for the Gamma oscillator,
  Euler Hamiltonian and Frobenius isometries, and derives the exact
  `log p` connection anomaly from Gauss residue-class determinant descent;
* [`P122_025_FINITE_AFFINE_COMPRESSION_AND_ANOMALY_WALL.md`](P122_025_FINITE_AFFINE_COMPRESSION_AND_ANOMALY_WALL.md):
  proves that the affine relation survives the natural finite cutoff with
  no boundary curvature and that the Gauss `log p` term is a genuinely
  cofinal regularized-dimension anomaly, not a finite first-contact seam
  law;
* [`P122_026_RESIDUE_BRAIDING_SIGN_CANCELLATION.md`](P122_026_RESIDUE_BRAIDING_SIGN_CANCELLATION.md):
  proves that the quadratic-reciprocity-looking tensor flip in two-prime
  residue descent is exactly cancelled by the two arithmetic mixed-radix
  relabellings, leaving no canonical cross-prime determinant sign;
* [`P122_027_FINITE_SUCCESSOR_PATH_GAMMA_EULER_BRIDGE.md`](P122_027_FINITE_SUCCESSOR_PATH_GAMMA_EULER_BRIDGE.md):
  realizes `log p` as the positive finite successor-path energy from the
  Gamma vacuum to its Frobenius image and constructs the exact
  prime-power weights, while proving that its nonzero cross-prime Gram
  requires a still-missing graded causal transgression before row C;
* [`P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md`](P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md):
  carries out the decisive two-prime calculation: the canonical finite
  Gamma path has DtN form `||(E_q-E_p)h||^2/log(q/p)`, but harmonicity only
  gives constant flux, not zero flux, so Gate S remains the independent
  sign-bearing theorem;
* [`P122_029_LIONS_MAGENES_TRANSMISSION_AUDIT.md`](P122_029_LIONS_MAGENES_TRANSMISSION_AUDIT.md):
  identifies Gate R with the classical `H^(1/2)_00` transmission space,
  proves its exact weighted interval norm, and shows that existing
  `mu`-transmission theory requires rather than derives the missing trace
  matching for sharply truncated translations;
* [`P122_030_PROVENANCE_AND_NOVELTY_LEDGER.md`](P122_030_PROVENANCE_AND_NOVELTY_LEDGER.md):
  separates imported classical machinery, repository specializations,
  programme-level reductions and genuinely open arrows so that
  `PROVED-IN-REPOSITORY` is never mistaken for a priority claim;
* [`P122_D_SPECIFICATION.md`](P122_D_SPECIFICATION.md): the minimum typed
  contract a genuine new D must satisfy.

## Non-negotiable status convention

Every statement is labelled as one of:

1. `PROVED-IN-REPOSITORY`: a complete proof with all hypotheses and domains;
2. `IMPORTED`: an exact external theorem with a checkable citation and a
   verified hypothesis map;
3. `COMPUTATIONAL-CERTIFICATE`: finite and reproducible, with its range;
4. `CONDITIONAL`: a consequence of a separately named open statement;
5. `CANDIDATE`: a precise statement not yet proved;
6. `RETRACTED/REFUTED`.

No chain to row (d) may pass through an unlabeled arrow.

## Meaning of “construct D”

`D` will not mean a formal square root of the Weil form.  Phase 120 proves
that such a linear Hilbert factorization exists exactly when row (d) is
already true.  A successful `D` must instead be a source-defined arithmetic
object, constructed before the sign comparison, whose independently proved
structural theorem implies the row-(d) inequality.

Until that theorem is proved, the notation `D_candidate` is mandatory.
