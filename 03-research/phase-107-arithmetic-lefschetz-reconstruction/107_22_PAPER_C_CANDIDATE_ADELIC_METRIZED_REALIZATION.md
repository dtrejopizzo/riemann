# 107.22 -- Paper C, Part X: candidate adelic metrized realization on \(\mathcal X_T^{(1)}\)

## 1. Purpose

`107_21` leaves Part III at the following point:

1. the off-diagonal packet determinant package has been descended to a
   global order-indexed line object on \(\mathcal X_T^{(1)}\);
2. the only admissible archimedean completion has been pinned to the
   boundary line \(\mathcal L_\infty\).

The present note pushes one step further toward `107_11` and `107_12`.
Its task is to package that descended line object into a candidate
adelic metrized realization

\[
 \widehat{\mathcal M}_{f,T}^{\rm cand}
 \in
 \widehat{\mathrm{Pic}}_{\rm int}^0(\mathcal X_T^{(1)})
 \tag{1.1}
\]

for finite-support source divisors \(D_{f,T}\), together with the exact
list of hypotheses that must still be proved in order for this candidate
to lie in the domain of Yuan--Zhang or, after extra regularity input, of
Faltings--Hriljac.

This note does not claim that the target category has already been
reached.  It fixes the candidate object and its proof obligations.

## 2. Inputs

The construction uses six earlier components.

1. `107_05` gives the source Gamma--polar Green metric.
2. `107_06` gives the source arithmetic determinant pairing.
3. `107_11` gives the required realization map and exact-kernel target.
4. `107_12` gives the admissibility/integrability audit.
5. `107_20` gives the local packet determinant line and off-diagonal
   norm comparison.
6. `107_21` gives the global descended packet line and its boundary
   receiver \(\mathcal L_\infty\).

## 3. The finite-support divisor at level \(T\)

Fix \(T>0\).  For any admissible source test \(f\), write

\[
 D_{f,T}
 =
 \sum_{(p,k)\in S_T} a_{p,k}(f)\,\Gamma_{p,k,T}^{(1)}
 +a_\Delta(f)\,\Delta_T^{(1)}
 +a_{\rm v}(f)\,F_{{\rm v},T}^{(1)}
 +a_{\rm h}(f)\,F_{{\rm h},T}^{(1)}
 +a_\infty(f)\,Z_{\infty,T}^{(1)}
 \tag{3.1}
\]

for the realized finite-support divisor on the candidate model of
`107_15`.

The coefficients are exactly those supplied by the source package of
`107_03`, not by a target positivity theorem.

### Requirement 3.1: finite-level exactness

Every compactly supported test must factor through some \(T\), and the
expression (3.1) must use only visible prime-power data from \(S_T\).

This keeps the realization candid to the finite-support architecture of
Phase 107.

## 4. The descended global finite line package

For visible distinct orders \(m\neq n\), `107_21` gives the global line

\[
 \mathcal L_{m,n,T}^{\rm glob}
 \tag{4.1}
\]

on the off-diagonal packet locus of \(\mathcal X_T^{(1)}\).

### Definition 4.1: finite global pairing on generators

Define the finite global pairing between off-diagonal realized packet
generators by

\[
 \langle \Gamma_{m,\bullet,T}^{(1)},\Gamma_{n,\bullet,T}^{(1)}
 \rangle_{\rm fin}^{\rm glob}
 :=
 \mathcal L_{m,n,T}^{\rm glob}.
 \tag{4.2}
\]

For diagonal terms, retain the excess-intersection object inherited from
`107_04` and `107_05`; for the boundary and ruling terms, retain the
source convention that the purely finite stage carries no independent
numerical correction.

### Proposition 4.2: finite global pairing transports the Paper A support law

Off the diagonal, the finite norm of (4.2) is exactly
\(|\mathrm{Res}(\Phi_m,\Phi_n)|\), hence obeys the normalized
prime-power support law of `107_04`.

Proof.  This is Theorem 6.2 of `107_21`, which descends the local
comparison theorem of `107_20`.  \(\square\)

## 5. Candidate archimedean metric on the descended line

The missing step is to attach to the descended global line the same
Gamma--polar Green datum that closed Paper A.

### Definition 5.1: boundary-matched metric candidate

For each off-diagonal global line \(\mathcal L_{m,n,T}^{\rm glob}\),
define its candidate metric \(\|\cdot\|_{m,n,T}^{\rm cand}\) by the two
rules:

1. on the off-corner packet charts, it agrees with the packet norm of
   `107_20`, equivalently with the cyclotomic determinant norm coming
   from `107_04`;
2. in a neighborhood of the compactified diagonal/corner sector, it is
   glued through \(\mathcal L_\infty\) so that its logarithmic
   variation reproduces the Green functional
   \(G_{\Gamma,\rm pol}\) of `107_05`.

Equivalently, the candidate metrized line is

\[
 \widehat{\mathcal L}_{m,n,T}^{\rm cand}
 :=
 \bigl(\mathcal L_{m,n,T}^{\rm glob},\|\cdot\|_{m,n,T}^{\rm cand}\bigr).
 \tag{5.1}
\]

### Principle 5.2: no second archimedean metric

The metric on \(\widehat{\mathcal L}_{m,n,T}^{\rm cand}\) is not allowed
to use any archimedean correction other than the one forced by
`107_05`.  In particular, one may not add a second ad hoc Green term to
repair the diagonal or degree-zero conditions later.

This preserves the single-metrized-determinant principle of Paper A.

## 6. Integrability target

The natural target suggested by `107_12` is the integrable adelic Picard
category.

### Definition 6.1: candidate integrable adelic class

Say that \(\widehat{\mathcal L}_{m,n,T}^{\rm cand}\) is
`admissible-candidate` if the following hold:

1. the metric extends continuously on each chart of the regularized
   model away from a controlled logarithmic singularity along the
   compactified diagonal and corner;
2. those logarithmic singularities are exactly the ones prescribed by
   \(G_{\Gamma,\rm pol}\);
3. the local metrics are compatible on overlaps and define a globally
   integrable adelic metric in the sense required by Yuan--Zhang.

This is a definition of target status, not yet a proved theorem.

### Proposition 6.2: the Yuan--Zhang route is the first admissible target

At the current state of Part III, the most natural theorem-compatible
target is
\(\widehat{\mathrm{Pic}}^0_{\rm int}(\mathcal X_T^{(1)})\), not
yet the smooth classical Arakelov category.

Proof.  `107_21` leaves the metric completed through the compactified
corner line \(\mathcal L_\infty\), where logarithmic boundary behavior
is intrinsic.  `107_12` allows precisely an integrable adelic route for
such data, whereas the smooth classical route requires stronger
regularity not yet established.  \(\square\)

This does not exclude a later classical upgrade; it fixes the immediate
target candidly.

## 7. Candidate degree-zero metrized bundle attached to a test

### Definition 7.1: generatorwise metrized realization

For each generator of `107_03`, assign the following candidate
metrized line contribution on \(\mathcal X_T^{(1)}\):

1. \(\Gamma_{p,k,T}^{(1)}\) contributes the packet-descended line with
   metric inherited from \(\widehat{\mathcal L}_{p^k,\bullet,T}^{\rm cand}\);
2. \(\Delta_T^{(1)}\) contributes the diagonal excess-intersection line
   completed by the same Gamma--polar metric of `107_05`;
3. \(F_{{\rm v},T}^{(1)}\) and \(F_{{\rm h},T}^{(1)}\) contribute the two
   ruling corrections needed to keep degree bookkeeping visible;
4. \(Z_{\infty,T}^{(1)}\) contributes the boundary metric receiver
   singled out by \(\mathcal L_\infty\).

### Definition 7.2: candidate finite-support realization

Define

\[
 \widehat{\mathcal M}_{f,T}^{\rm cand}
 :=
 \bigotimes_{(p,k)\in S_T}
 \widehat{\mathcal M}_{p,k,T}^{\otimes a_{p,k}(f)}
 \otimes
 \widehat{\mathcal M}_{\Delta,T}^{\otimes a_\Delta(f)}
 \otimes
 \widehat{\mathcal M}_{{\rm v},T}^{\otimes a_{\rm v}(f)}
 \otimes
 \widehat{\mathcal M}_{{\rm h},T}^{\otimes a_{\rm h}(f)}
 \otimes
 \widehat{\mathcal M}_{\infty,T}^{\otimes a_\infty(f)}.
 \tag{7.1}
\]

This is the first explicit candidate for the object that `107_11`
denotes \(\overline M_f\).

### Proposition 7.3: additivity is built in at the candidate level

For finite-support source divisors \(D_{1,T},D_{2,T}\),

\[
 \widehat{\mathcal M}_{D_{1,T}+D_{2,T}}^{\rm cand}
 \cong
 \widehat{\mathcal M}_{D_{1,T}}^{\rm cand}
 \otimes
 \widehat{\mathcal M}_{D_{2,T}}^{\rm cand}.
 \tag{7.2}
\]

Proof.  Definition 7.2 is multiplicative in the generator coefficients.
\(\square\)

So the first compatibility of `107_11` is already encoded formally.

## 8. Pairing transport target

The candidate realization is meaningful only if its height pairing is
forced to match the source arithmetic pairing of Paper A.

### Requirement 8.1: candidate pairing identity

For all finite-support tests \(f,g\), the intended theorem target is

\[
 -\,\widehat{\deg}
 \bigl(
 \widehat{\mathcal M}_{f,T}^{\rm cand}
 \cdot
 \widehat{\mathcal M}_{g,T}^{\rm cand}
 \bigr)
 =
 \widehat{\deg}\,
 \overline{\langle D_{f,T},D_{g,T}\rangle}_{\rm src}.
 \tag{8.1}
\]

The right side is already known in the source determinant package
(`107_06`), so (8.1) is a concrete comparison theorem target rather than
a slogan.

### Proposition 8.2: the off-diagonal finite part already matches

In (8.1), the off-diagonal finite contribution from distinct visible
orders already agrees with Paper A.

Proof.  This is Proposition 4.2 above.  The missing work is entirely in
the completed metrized target interpretation, not in the visible
prime-power resultant support.  \(\square\)

## 9. Degree-zero normalization target

The next obstruction identified by `107_11` is degree zero.

### Definition 9.1: polarization-corrected primitive candidate

Let \(H_T^{(1)}\) denote the fixed polarization candidate on
\(\mathcal X_T^{(1)}\) coming from the two-ruling compactified square.
Define the primitive correction coefficient

\[
 c_T(f)
 :=
 \frac{\deg(\mathcal M_{f,T}^{\rm raw}\cdot H_T^{(1)})}
      {\deg(H_T^{(1)}\cdot H_T^{(1)})}
 \tag{9.1}
\]

whenever the denominator is nonzero and the intersection numbers exist
in the candidate category.  Then set

\[
 \widehat{\mathcal M}_{f,T}^{0,{\rm cand}}
 :=
 \widehat{\mathcal M}_{f,T}^{\rm cand}
 \otimes
 \mathcal O_{\mathcal X_T^{(1)}}(-c_T(f)\,H_T^{(1)}).
 \tag{9.2}
\]

This is the candidate primitive projection demanded by Part III-B.

### Caution 9.2: degree zero is not yet proved

Formula (9.2) is a normalization protocol, not yet a theorem that the
required degree and intersection numbers exist in the admissible target
category.

That proof obligation remains part of the next front.

## 10. Exact-kernel audit at the candidate level

### Requirement 10.1: radical classes must map to candidate torsion/zero

For every visible radical jet \(r_j\) lying in the finite-support test
class at level \(T\), the candidate realized class
\(\widehat{\mathcal M}_{r_j,T}^{0,{\rm cand}}\) must be torsion or zero
after realification.

### Requirement 10.2: no extra collapse

If \(f\notin\mathfrak R_W\), then the candidate class
\(\widehat{\mathcal M}_{f,T}^{0,{\rm cand}}\) must remain nontrivial in
the realified target.

These are the exact-kernel conditions of `107_11` rewritten as a test on
the concrete candidate object introduced here.

## 11. Route-A and Route-B implications

### Proposition 11.1: this note narrows the Route A task

After `107_22`, the remaining Route A burden of `107_12` is no longer to
guess what the target object should be.  It is to prove that
\(\widehat{\mathcal M}_{f,T}^{0,{\rm cand}}\) actually belongs to the
integrable adelic Picard category and satisfies degree zero, finite
pairings, and equality-case control.

Proof.  The candidate object, its metric source, and its generatorwise
construction are now fixed.  The missing items are precisely the
hypotheses A2--A6 of `107_12`.  \(\square\)

### Consequence 11.2: Route B remains strictly unnecessary for now

As long as the integrable adelic candidate of this note remains viable,
there is no need yet to open a new absolute Hodge theorem route.

This is strategically important: it keeps the program on the already
audited E1 branch until a genuine failure occurs.

## 12. What is now closed

This note closes the next interface gap between Part III-A and III-B.

1. the descended global packet determinant package now has a candidate
   adelic metrized completion;
2. the immediate target category is fixed candidly as the integrable
   adelic branch suggested by `107_12`;
3. the first generatorwise formula for the candidate realized class
   \(\widehat{\mathcal M}_{f,T}^{\rm cand}\) is now explicit;
4. the degree-zero normalization protocol and the exact-kernel audit are
   now attached to a concrete candidate object.

## 13. What remains open

This note still does not complete Paper C or Part IV.

1. It does not prove the metric is integrable/admissible in the precise
   Yuan--Zhang sense.
2. It does not prove the primitive correction coefficient \(c_T(f)\) is
   well defined in the target category.
3. It does not prove the pairing identity (8.1) in the completed
   metrized target.
4. It does not prove the exact-kernel identity
   \(\ker(f\mapsto\overline M_f)=\mathfrak R_W\).

## 14. Next technical front

The next proof-bearing move is now sharply isolated: verify the
integrability/admissibility hypotheses of `107_12` for the candidate
metric of Definition 5.1, and then prove that the candidate pairing
identity (8.1) reproduces the Paper A source arithmetic degree on the
completed target side.
