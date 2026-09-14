# Phase 122 — execution plan for constructing row (d)

## Objective

Determine whether the arithmetic-Lefschetz programme currently has a sound
chain through rows (a)--(c) to the analytic row-(d) problem and, if it does,
construct a genuinely new source-side object whose theorem proves row (d)
without importing RH or Weil positivity.

The phase is successful only if it produces either:

* a complete proof with every dependency discharged; or
* a smaller, rigorously demonstrated obstruction showing exactly why the
  present A/B/C data cannot determine D.

## Gate 0 — proof-integrity reconstruction

Status: `SUBSTANTIALLY COMPLETE`.  The analytic target and A/B/C scope are
frozen, first-contact attainment is supplied by P122.002, the external
anchors are audited, and the stale `log5` theorem is retracted in P122.004.
The expensive full Tier-2 replay of the surviving `log2` certificate remains
a reproducibility task, not a missing logical arrow.

Build a theorem-level dependency graph, not a narrative summary.

### 0.1 Freeze the analytic target

Verify from definitions, with signs and domains,

\[
 -B_{\rm nuc,T}(F,F)=\langle F,\Delta_TF\rangle,
 \qquad F\in\mathcal P_T,
\]

the equivalence of the cofinal row-(d) statement with Weil positivity, and
the precise core-to-closure passage.

### 0.2 Audit rows (a)--(c)

For every imported engine (Connes--Consani, Haran, Meyer, Clausen--Scholze,
and any enriched/category theorem), record:

* the exact published theorem;
* the category and topology in which it holds;
* the repository object to which it is applied;
* a line-by-line hypothesis map;
* whether the conclusion is literal, analogous, or conjectural.

This gate must be completed before calling rows (a)--(c) “proved”.

### 0.3 Reprove first-contact attainment

The required theorem must handle simultaneously:

1. a common fixed form domain under moving-window transport;
2. lower semiboundedness and compact resolvent of the primitive operator;
3. continuity in `T` at regular values;
4. prime-power birth thresholds, where compressed shifts are not
   operator-norm continuous;
5. uniform compactness of minimizing vectors as Galerkin dimension and
   support vary;
6. transport of the two Tate constraints;
7. parity reduction.

If these points cannot be proved, replace the first-contact programme by a
direct negative-minimizer equation

\[
 \mathscr A_TF=\lambda F+\alpha e^{-t/2}+\beta e^{t/2},
 \qquad \lambda<0,
\]

and redo every phase-121 implication with the `lambda F` term retained.

## Gate 1 — certified map of what phase 121 actually proves

Status: `COMPLETE AS AN INTEGRITY CLASSIFICATION` in P122.008.  The
critical-density input is corrected in P122.003.  The oriented defect and
its faithfulness survive; its equality-state annihilation remains open.

Recheck the proofs, definitions and normalizations of:

* maximal-domain and `H^s`, `s<1/2`, regularity;
* the completed incoming current;
* the critical `H^{-1/2}` residue mass;
* Cartwright density and faithfulness;
* oriented relative `K_2` and its tame symbol;
* Rees--Poisson normal versus localized causal Rees;
* active Euler-ideal overdensity;
* collar, seam and infinitesimal-gap rigidity.

The output is a dependency table marking each result with the status
convention in the phase README.  In particular, formal relative `K_2`
calculations must not silently become a geometric/global reciprocity theorem.

## Gate 2 — minimal specification for `D_candidate`

Status: `SPECIFIED` in `P122_D_SPECIFICATION.md`.  P122.005 adds the
port-swap falsifier: a candidate factoring through scalar row-C data is
inadmissible.

A candidate is admissible only if all the following are defined before any
comparison with `B_nuc`:

1. its carrier, morphisms, topology and domain;
2. the exact local data at every prime power with weights
   `(log p)p^{-j/2}`;
3. the archimedean Gamma component;
4. the cross-place phase and the coherent degree port;
5. both Tate conditions;
6. its orientation before scalar supertrace;
7. restriction in `T` and cofinal stabilization;
8. its behavior for curves, Dedekind zeta, Davenport--Heilbronn and the
   shifted rank-two pair.

It must have a pre-row-(d) falsifier.  A square root, Douglas contraction,
Schur complement, positive metric selected by matching the target, or an
asserted equality-state horizontal lift is rejected.

## Gate 3 — two live construction tracks

### Track I: equality-state source law on active primes

Work with active primes only.  The terminal descent already proved in phase
121 is

\[
 \delta_F(I_p)\subset I_p\quad(p<e^{2T})
 \quad\Longrightarrow\quad F=0.
\]

The new work is to derive a non-symmetric, source-level law from the full
Euler--Gamma equation before row-(c) augmentation.  The first falsifier is
the exact transformed collar formula: if the proposed law cancels the
interior coefficient by assuming away the collar, it is false.

No inactive-prime or cofinal information may be claimed from a finite
compression.

Status: P122.013 constructs the missing local nonflat Hermitian line from
the Hardy polarization defect of every degree-one Euler factor.  The local
curvature is a positive rank-one root observable and is orientation
sensitive.  The track is now reduced to constructing the global
Euler--Gamma--Tate determinant line and proving its first-contact metric
flatness without identifying the two histories by assumption.

P122.016 refines the global type: the physical Euler scattering is not in
the ordinary restricted group, but it has a canonical semifinite
Bohr-crossed-product determinant class.  P122.017 proves that its native
central cocycle splits by prime and has zero primary Euler index.  Hence the
next object cannot be another line/cocycle on the finite Bohr algebra; it
must be a relative archimedean correspondence carrying a genuinely mixed
Gamma--Euler anomaly.

P122.018 shows that a symmetric mixed scalar cocycle vanishes by parity.
P122.019 then identifies a sharper endpoint mechanism: a genuine Calderon
trace into the determinant class `H^(1/2)` would annihilate the forced Tate
current because that current has explicit activation jumps.  P122.020
proves the remaining two-gate criterion: after this endpoint gate, one
horizontal identity between two distinct active prime fibres annihilates the
homogeneous state by first-cell separation.  Constructing and proving those
two bridge theorems, for general source sections rather than by postulate on
the radical, is now the live Track-I objective.

P122.022 constructs the Gamma side as a genuine determinant class relative
to its universal Stirling chirp.  P122.023 tests the resulting microlocal
scale map and proves that it cannot itself be the bridge: globally it
commutes with every Euler return, while finite-window compression recovers
only the known incoming boundary history.  The live bridge must therefore
contain an arithmetic transmission morphism beyond the Stirling canonical
shear.

P122.024 constructs such a source algebra at the integer level: the
additive Gamma successor and multiplicative Frobenius isometries generate an
affine semigroup on one Hilbert space, while Gauss determinant descent
produces `log p`.  P122.025--P122.026 remove two false closures (the Gauss
anomaly is cofinal, and the apparent residue-braiding sign cancels).
P122.027 supplies a genuinely finite bridge: the positive successor path
from `1` to `p` has energy `log p` and nonzero cross-prime overlaps.  The
two-prime calculation is completed in P122.028.  Its exact DtN form is the
transverse seam square divided by `log(q/p)`, but harmonicity permits every
endpoint pair and gives only constant flux.  Zero flux is precisely Gate S,
not a consequence of the carrier.  Therefore Track I is no longer allowed
to add another carrier.  It must either prove the causal transmission Gate
R from an external boundary theorem or introduce a genuinely independent
arithmetic/geometric input proving the zero-flux law; positivity of an
ungraded Gram is not an admissible substitute because it changes row C.

P122.029 completes the external transmission check.  Gate R is membership
in the Lions--Magenes space `H^(1/2)_00` at each activation seam; the exact
weighted norm shows that this is equivalent to zero Tate trace.  The
Boutet de Monvel/Hormander--Grubb calculi propagate regularity once the
transmission condition is imposed, but do not derive it for a truncated
translation.  Therefore no existing generic boundary theorem closes R.

### Track II: direct negative minimizer and nonlinear pole law

Avoid first contact.  Start with an attained negative eigenvector (if Gate 0
proves attainment at fixed `T`) and retain its spectral parameter `lambda`.
Compute, rather than postulate, the sourced connection and the principal
parts of its curvature.  Test whether the sign `lambda<0`, together with
complex-line covariance and the exact Tate forcing, imposes a pole-order or
residue restriction on a positive-density subset of critical zeros.

The route dies if the `lambda`-dependent identity is a scalar multiple of
the eigen-equation, if its double-pole term is inserted by choosing a frozen
connection, or if the required vanishing is equivalent to row (d).

Status: the purely local principal-part version is `RETIRED` by P122.006.
The negative minimizer exists, but `lambda K_F` is entire and disappears
from all polar orders.  A future version must exhibit a genuinely global
identity in which the sign `lambda<0` survives.

### Track III audit: divisor-singular equality variations

Status: `RETIRED` by P122.011.  Multiplication by `E'/E` detects exactly the
critical Cauchy residue, but the unregularized vector lies in the equality
form domain only when that residue already vanishes.  Regularized double
commutators yield a nonnegative divergent Gram energy and no upper bound.
Any successor must therefore construct an independent oriented
curvature/anomaly equality before comparison with the target form.

## Gate 4 — adversarial comparison and proof closure

Every surviving lemma is tested against:

* finite-dimensional causal/Real countermodels;
* a generic symmetric explicit-formula model;
* Davenport--Heilbronn;
* `xi(s+a)xi(s-a)`;
* function fields, where the true Hodge theorem is known;
* Dedekind zeta functions, recording explicitly if the result would prove
  their GRH as well.

Then verify the entire chain in reverse, from row (d) back to each new
hypothesis, to detect hidden equivalences and assumed signs.

## Deliverables

1. `P122_DEPENDENCY_GRAPH.md` — theorem-level DAG with exact statuses.
2. `P122_ROWS_ABC_REFERENCE_AUDIT.md` — external-theorem hypothesis map.
3. `P122_FIRST_CONTACT_THEOREM.md` or a formal retraction of that reduction.
4. `P122_D_SPECIFICATION.md` — typed definition and falsifiers.
5. construction notes and countermodels for Tracks I and II.
6. a self-contained proof manuscript only after all arrows are green.

## Stop rules

* No numerical experiment upgrades an asymptotic or universal statement.
* No identity is called a sign theorem.
* No equivalent reformulation is reported as progress toward proving RH.
* A failed candidate is added to the no-go ledger with the exact failure.
* Paper 42 is not changed to claim row (d) until the independent audit of
  the complete chain succeeds.
* **Carrier stop rule after P122.028:** no new carrier is constructed when
  its defining data are functorially generated by
  `{log p, p^(-1/2), N, Gamma}`.  Such a proposal must first name and prove
  a theorem using an independent input not recoverable from those data, and
  must show on the two-prime finite complex how that input forces critical
  trace matching or zero DtN flux.  Otherwise it is downstream of row C and
  is rejected before construction.
