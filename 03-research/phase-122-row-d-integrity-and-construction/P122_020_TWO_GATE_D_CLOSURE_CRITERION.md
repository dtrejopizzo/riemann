# P122 -- a two-gate closure criterion for the missing D object

## Status

`PROVED-IN-REPOSITORY` as a conditional reduction.  The two hypotheses
below are explicit construction targets; neither is asserted to exist.

This note gives the shortest currently justified route from a genuine
relative Gamma--Euler determinant correspondence to row (d).  It separates
the finite Tate boundary from the homogeneous Euler state, so that no
single conservation identity is asked to do both jobs.

## 1. The two required gates

For each `T>log 2`, suppose a source-defined correspondence
`E_(infinity,T)` extends the finite semifinite object
`D^(fin)_(T,sf)` of P122.016.  It must be constructed independently of the
sign of `Delta_T` and have the following equality-state consequences.

### Gate R -- critical Calderon regularity

For every parity first-contact state `F`, its canonical completed incoming
current satisfies

\[
             \mathcal L^{\rm gr}_{T,-}(F)
             \in H^{1/2}(I_T).                    \tag{R}
\]

This must follow from a transmission theorem for a source-defined
horizontal/null family, identifying the relevant semifinite determinant
trace with the physical time boundary.  It may not be imposed directly on
first-contact vectors.  P122.021 proves that no such statement holds for
generic sections after sharp-window truncation.

### Gate S -- horizontal prime-seam matching

If the same state has zero completed incoming current, horizontal/flat
transport in `E_(infinity,T)` identifies at least two distinct active local
Euler channels:

\[
 \mathcal L^{\rm gr}_{T,-}(F)=0
 \quad\Longrightarrow\quad
 (E_{p,T}-E_{q,T})\mathfrak h_F=0                 \tag{S}
\]

for some active primes `p\ne q`.  This implication must be obtained before
scalar supertrace.  Defining horizontal transport by equality of these
channels would simply rename the missing assertion.

The two gates are structurally different.  Gate R is an endpoint domain
theorem and sees the finite-dimensional Tate forcing.  Gate S is an
unsupertraced local-to-global law and sees the homogeneous state through
unequal Frobenius normalizations.

## 2. Closure theorem

### Theorem 2.1 -- R plus S excludes first contact

Assume Gates R and S for every `T>log 2`.  Then no nonzero parity
first-contact state exists.

#### Proof

Let `F` be such a state.  Phase 121 constructs its incoming current and
proves

\[
 \mathcal L^{\rm gr}_{T,-}(F)
 =-\mathcal Z_{T,+}r_\varepsilon.                 \tag{2.1}
\]

Gate R and P122.019, Theorem 2.2, imply

\[
 r_\varepsilon=0,
 \qquad \mathcal L^{\rm gr}_{T,-}(F)=0.           \tag{2.2}
\]

Gate S now gives a vanishing transverse seam for two distinct active
primes.  The phase-121 first-cell separation theorem then implies `F=0`, a
contradiction.  QED.

### Corollary 2.2 -- conditional row (d)

Assume:

1. the strict base positivity on `0<T<=log 2` used by P122.002;
2. the compact first-contact theorem P122.002, including birth thresholds;
3. Gates R and S for every `T>log 2`.

Then

\[
                         \Delta_T\geq0             \tag{2.3}
\]

on the primitive space for every finite `T`, and hence the repository's
row-(d) Weil positivity statement follows by its audited cofinal passage.

#### Proof

If (2.3) failed, P122.002 would produce a first `T_*>log 2` with a nonzero
parity null state.  Theorem 2.1 excludes it.  QED.

This is a conditional theorem, not a proof of row (d), because Gates R and
S remain open.

## 3. Why the criterion is not circular

Each gate has an independent falsifier.

* Gate R fails for a nonzero Tate coefficient by the explicit jump at
  `-T+log 2`; it is therefore a real endpoint theorem, not a weak
  restatement of conservation.
* Gate S is tested on the arithmetic-free first cell.  There the channels
  are `sqrt(1-p^(-1))F` and `sqrt(1-q^(-1))F`; equality is impossible for a
  nonzero state because the two constants differ.
* Neither gate mentions `Delta_T>=0`, a square root of the target form, or
  a spectral projection selected from its nonnegative part.

Nevertheless, merely postulating R and S for null states would be circular
in the constructional sense: together they imply the desired theorem.
They are admissible only if they arise as structural theorems for a
previously defined horizontal/null source family substantially larger than
the first-contact radical.

## 4. Minimal interface for the next construction

The full geometric ambitions in `P122_D_SPECIFICATION.md` remain useful,
but the proof-bearing interface is now only:

```text
finite side:       D^(fin)_(T,sf) and its Hardy determinant domain
infinite side:     quarter-Gamma Calderon module
bridge:            a closed relative trace map to the time boundary
Gate R theorem:    horizontal null sections have H^(1/2) incoming trace
Gate S theorem:    zero trace identifies two active prime fibres
comparison last:   scalar supertrace equals B_nuc
```

The next candidate should first be tested on a two-prime truncation plus the
Gamma boundary.  If it cannot prove R and S there without using the sign of
the scalar form, adding all primes cannot repair the logical defect.

## 5. Remaining obstruction

No object presently in the repository supplies either bridge theorem.
The finite Bohr carrier supplies the left determinant domain but no Gamma
trace.  The phase-121 graph construction supplies the physical incoming
current but no determinant-domain improvement.  The transverse seam is
faithful but no global reciprocity theorem makes it horizontal.

Thus D has not been completed.  What has been completed is the reduction
of its proof obligation to two typed, localizable and adversarially
testable arrows.
