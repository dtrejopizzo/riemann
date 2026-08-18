# 107.10 -- Paper C, Part I: universal finite models over the full arithmetic base

## 1. Purpose

This note begins Part III of `107_00`.  Its task is to state the
geometric realization problem in a form compatible with the source
package already built in Papers A and B:
for each finite support bound \(T\), the finite-support divisor and
correspondence data must live on a regular proper arithmetic model over
the whole of \(\mathrm{Spec}\,\mathbb Z\).

The central constraint is the one already fixed in the Phase 107 setup:

\[
 \text{finite support of }D_f
 \neq
 \text{truncation of the arithmetic base.}
 \tag{1.1}
\]

In particular, deleting all places \(p>T\) is not an admissible
construction.  The model may restrict which divisors are present, but it
must remain proper over the complete arithmetic base.

## 2. Why Part III is necessary

Paper A constructs a coherent finite-support intersection theory.
Paper B constructs a decorated Frobenius-like correspondence category
and its arithmetic Lefschetz formula.  Neither achievement by itself
places the divisors inside the domain of Faltings--Hriljac or
Yuan--Zhang.

The obstruction was already isolated in `106.210`:

1. the cyclotomic resultant surface
   \(\mathrm{Spec}\,\mathbb Z[x]\) supplies the correct finite local
   support but no diagonal closure;
2. its natural proper compactification is genus zero and has trivial
   Jacobian degree one;
3. therefore it cannot hold the resonant degree-one class required for
   the final Hodge comparison.

Part III must add exactly what that stop test showed to be missing:

\[
 \text{finite local intersections}
 + \text{Gamma--polar infinity}
 + \text{nontrivial degree one}
 \tag{2.1}
\]

on one global proper object.

## 3. Source input for the global model

Three layers of earlier work constrain the acceptable realization.

### 3.1. Local finite-support geometry

`107_04` and `107_06` fix the finite-place determinant lines, their
exact prime-power support, and the symmetric finite-support intersection
pairing.  Any realization \(\mathcal X_T\) must reproduce those local
intersection lines under pullback to the corresponding finite strata.

### 3.2. Archimedean boundary geometry

`107_05`, `106.159`, and `106.195` fix the Gamma--polar boundary page as
one metrized determinant object.  Therefore the archimedean component of
\(\mathcal X_T\) may not be chosen ad hoc after the finite model is
built: it must realize the same Green metric that already closes the
diagonal in Paper A and the same boundary page that appears in the
Lefschetz formula of `107_09`.

### 3.3. Degree-one global carrier

`107_08` and `107_09` show that the source geometry is not a disjoint
family of prime circles; it is a glued flow object with a common
archimedean phase and a genuine diagonal class.  Meanwhile `106.164` and
the Connes--Consani Jacobian data summarized in Phase 39 identify a
natural universal degree-one carrier: the arithmetic Picard monoid and
its Jacobian quotient.

This suggests that the universal ambient object of Part III should not
be a bare classical surface chosen prime by prime.  It should be a
global arithmetic object whose degree-one sector already remembers the
rooted divisor/Jacobian data, and whose finite classical models are
realizations of finite-support pieces of that object.

## 4. The realization problem

### Definition 4.1: admissible support bound

Let \(T>0\).  Define the admissible prime-power support set

\[
 S_T=\{(p,k): k\log p\le T\}.
 \tag{4.1}
\]

Only these prime-power returns are allowed to appear in the test divisor
or correspondence package at level \(T\).  The ambient arithmetic base
remains all of \(\mathrm{Spec}\,\mathbb Z\).

### Definition 4.2: universal finite model

A universal finite model at level \(T\) consists of:

1. a normal geometrically connected projective surface
   \(Y_T/\mathbb Q\), together with a regular proper model
   \(\mathcal Y_T\to\mathrm{Spec}\,\mathbb Z\), of relative dimension two
   and total Krull dimension three;
2. two transverse polar projections
   \(\pi_{\mathrm v},\pi_{\mathrm h}\) realizing the two rulings;
3. a diagonal-type divisor \(\Delta_T\subset\mathcal Y_T\);
4. realized correspondence cycles
   \(\Gamma_{p,k,T}\) for \((p,k)\in S_T\);
5. a fixed nef and big metrized polarization \(\overline H_T\);
6. an archimedean Green datum whose induced metrized determinant lines
   agree with Paper A.

The dimension is forced by the intended analogue of \(C\times C\).
Calling \(\mathcal Y_T\) an arithmetic surface in the
relative-dimension-one sense would put the terminal Hodge theorem in the
wrong dimension.  The direct Hodge quantity is the polarized triple
intersection \(\overline M_f^{\,2}\cdot\overline H_T\).

The phrase "universal" means universal for the finite-support source
package at level \(T\), not universal over all \(T\) at once.

## 5. Candidate realization architecture

The program of `107_00` listed four directions.  The present paper fixes
how they interact rather than choosing only one.

### Layer A: absolute universal carrier

Use the Connes--Consani arithmetic curve / Picard monoid / Jacobian as
the universal degree-one carrier.  Its role is to remember:

1. the rooted rank-one group data;
2. the common generic orbit;
3. the prime fibres \(C_p\);
4. the common archimedean boundary phenomena.

By itself, this object is not yet a regular proper arithmetic surface in
the classical Arakelov sense.  It is the universal source ambient.

### Layer B: local chart realization

Use cyclotomic/root-cover charts for each \((p,k)\in S_T\) to realize
the finite derived intersections.  These charts are the local model
already justified by `107_04` and by the stop-test audit `106.210`.

### Layer C: finite classical envelope

Construct a regular proper classical arithmetic surface
\(\mathcal X_T\) together with a morphism to the absolute universal
carrier such that:

1. every cycle supported on \(S_T\) pulls back to an candid divisor or
   correspondence cycle on \(\mathcal X_T\);
2. the finite determinant lines agree with the local chart lines;
3. the archimedean Green metric is the pullback of the same
   Gamma--polar boundary page;
4. the degree-one classes remain visible after passage to the classical
   envelope.

This is the direction singled out as crucial in `107_00`: the universal
absolute object may remain stacky or pro-geometric, but each finite
support package must admit a classical proper realization.

## 6. Surface realization conjecture at finite support

### Conjecture 6.1: finite-support realization theorem

For every support bound \(T\), there exists a universal finite model
\(\mathcal X_T\) and realized cycles
\(\Gamma_{p,k,T}\), \(\Delta_T\), \(F_{{\rm v},T}\), \(F_{{\rm h},T}\),
\(Z_{\infty,T}\) such that:

\[
 \boxed{
 \text{source determinant/intersection package at level }T
 \cong
 \text{Arakelov package on }\mathcal X_T.
 }
 \tag{6.1}
\]

More explicitly:

1. finite local intersections on \(\mathcal X_T\) reproduce the exact
   prime-power support of `107_04`;
2. the archimedean Green metric on \(\mathcal X_T(\mathbb C)\)
   reproduces the Gamma--polar metric of `107_05`;
3. the diagonal intersection with the realized \(Z_{f,T}\) reproduces
   the arithmetic Lefschetz identity of `107_09`;
4. the degree-one part of \(\mathrm{Pic}^0(\mathcal X_T)\), or its
   precise adelic substitute, retains the nontrivial resonant classes
   needed for Paper C Part II.

The theorem is stated here as the exact target of III-A.  The present
note does not prove it.

## 7. Structural requirements forced by the stop tests

### Proposition 7.1: genus-zero envelopes are excluded

No genus-zero proper compactification can serve as \(\mathcal X_T\).

Proof.  By `106.210`, genus-zero compactifications such as
\(\mathbb P^1_{\mathbb Z}\) have trivial Jacobian degree one.  They may
host finite resultant data, but they cannot carry the resonant degree-one
class required by the final comparison with the Weil form.  \(\square\)

### Proposition 7.2: the model must keep both polar rulings

The realization must contain two transverse polar families and may not
collapse them to one boundary divisor.

Proof.  The source package distinguishes
\(F_{\mathrm v}\), \(F_{\mathrm h}\), and \(\Delta\) already at the raw
correspondence level in `107_03` and `107_07`.  Collapsing the two
rulings would destroy transpose symmetry and the diagonal formalism that
the fixed-point formula of `107_09` uses.  \(\square\)

### Proposition 7.3: absolutely continuous completions are excluded

An \(L^2\)-type completion that erases point/resonance classes cannot be
the target realization of III-A.

Proof.  The source divisors are built from primitive closed orbits,
their connected cyclic traces, and the diagonal fixed-point package.
Replacing them by an absolutely continuous completion would discard the
pointwise classes whose persistence is one of the stop tests of
`107_00`.  \(\square\)

## 8. Program for construction

The construction of \(\mathcal X_T\) now breaks into four subproblems.

1. Define the absolute universal square carrying the prime fibres, the
   generic orbit, the common archimedean page, and the diagonal.
2. Build finite-support local charts for the set \(S_T\) and prove their
   compatibility with the determinant lines of Paper A.
3. Produce a regular proper classical envelope \(\mathcal X_T\) together
   with comparison morphisms from the universal square and the local
   charts.
4. Verify that the comparison preserves intersections, the
   Gamma--polar metric, and degree-one visibility.

This subproblem list is the operational content of III-A.

## 9. Status

Part III now has a precise target:
the future surface \(\mathcal X_T\) is not allowed to be merely a
compactification of the cyclotomic charts, nor merely the absolute
Picard/Jacobian object by itself.  It must be a finite classical proper
realization of the absolute source geometry, retaining finite local
intersections, the common archimedean boundary, and nontrivial degree
one simultaneously.

The next paper, III-B, will have to construct the map from source
divisors to metrized line bundles on \(\mathcal X_T\) or on the precise
adelic substitute, with exact kernel equal to the explicit Weil radical.
