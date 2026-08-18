# 107.26 -- Paper C, Part XIV: control of exceptional corrections in the regularization protocol

## 1. Purpose

`107_25` isolates the denominator of the primitive projection as

\[
 H_T^{(1)}\cdot H_T^{(1)}
 =
 2c_T
 +\varepsilon_{\rm vv}(T)
 +\varepsilon_{\rm hh}(T)
 +2\varepsilon_{\rm vh}(T).
 \tag{1.1}
\]

The present note addresses the next real geometric question:
which parts of the regularization protocol of `107_15` can alter these
corrections, and under what condition do they fail to cancel the corner
contribution \(c_T\)?

The output is not yet a numeric computation of every correction.  It is
a finite control theorem: the correction package is supported only on a
small, explicitly identified family of exceptional centers, and a
corner-preserving regularization criterion is enough to force
nonvanishing of \(H_T^{(1)}\cdot H_T^{(1)}\).

## 2. Inputs

This note uses four already fixed ingredients.

1. `107_15` gives the regularization protocol by blow-ups over special
   strata.
2. `107_16` gives the two ruling divisors and the common corner
   \(C_\infty\).
3. `107_17` gives local corner and boundary charts.
4. `107_25` gives the decomposition of the polarization denominator into
   corner and exceptional parts.

## 3. The only blow-up centers that matter

The regularization protocol of `107_15` is supported over three kinds of
strata:

1. diagonal/boundary intersection strata;
2. self-intersections of distinct graph closures;
3. singular boundary points created by the finite-support incidence
   closure.

For the polarization denominator, most of these are irrelevant.

### Definition 3.1: polarization-active exceptional centers

Call a blow-up center `polarization-active` if it meets at least one of
the ruling strict transforms
\(F_{{\rm v},T}^{(1)}\), \(F_{{\rm h},T}^{(1)}\) and can therefore change
one of the three correction terms
\(\varepsilon_{\rm vv}(T)\), \(\varepsilon_{\rm hh}(T)\),
\(\varepsilon_{\rm vh}(T)\).

### Proposition 3.2: only centers meeting the ruling boundary are polarization-active

Any exceptional center disjoint from \(B_{\rm v}\cup B_{\rm h}\) makes
no contribution to the correction terms of (1.1).

Proof.  The correction terms of `107_25` are defined from intersections
of the strict transforms of the ruling divisors.  A blow-up supported
away from those divisors does not alter their local intersection
configuration.  \(\square\)

### Corollary 3.3: graph self-intersections away from the ruling boundary are invisible to \(h_T\)

The blow-ups resolving self-intersections of distinct graph closures can
affect \(h_T\) only if those self-intersections occur on the ruling
boundary or at the corner receiver.

This trims the regularization audit substantially.

## 4. Local classification near the corner

The local chart model of `107_17` lets us distinguish the exceptional
centers that are capable of destroying the corner contribution from
those that are not.

### Definition 4.1: corner chart

Work in a corner chart with local boundary parameters \(u_1,u_2\), so
that

\[
 B_{\rm v}=\{u_1=0\},
 \qquad
 B_{\rm h}=\{u_2=0\},
 \qquad
 C_\infty=\{u_1=u_2=0,\ \theta_1=\theta_2\}.
 \tag{4.1}
\]

### Definition 4.2: corner-preserving center

A polarization-active exceptional center is called `corner-preserving`
if, in local corner coordinates, it is contained in one ruling boundary
or in an auxiliary singular stratum, but does not contain the whole
mixed corner cycle \(C_\infty\) as a component to be removed.

### Definition 4.3: corner-collapsing center

A polarization-active center is called `corner-collapsing` if the blow-up
protocol forces the mixed corner incidence itself to be absorbed into an
exceptional divisor so that the strict transforms of the two ruling
divisors lose their common visible corner contribution.

This is the actual geometric failure mode behind \(c_T=0\).

## 5. Effect of corner-preserving blow-ups on the denominator

### Proposition 5.1: corner-preserving blow-ups only modify the correction package

If a blow-up center is corner-preserving, then the resulting change in
\(H_T^{(1)}\cdot H_T^{(1)}\) is absorbed entirely into the correction
terms
\(\varepsilon_{\rm vv}(T),\varepsilon_{\rm hh}(T),\varepsilon_{\rm vh}(T)\),
while the explicit corner term \(c_T\) survives.

Proof.  By definition, the mixed corner cycle remains visible in the
strict transforms of the two ruling divisors.  Therefore the ambient
mixed contribution identified in `107_25` is still present after the
blow-up.  The only new contributions come from the exceptional locus,
which are precisely the correction terms.  \(\square\)

### Proposition 5.2: boundary-only blow-ups cannot create a new mixed corner cancellation by themselves

If the center lies entirely in one ruling boundary and is disjoint from
the mixed corner cycle, then it can affect only the corresponding
self-correction \(\varepsilon_{\rm vv}(T)\) or
\(\varepsilon_{\rm hh}(T)\), not the corner term \(c_T\).

Proof.  Such a center changes one ruling divisor locally without
altering the locus where the two different ruling divisors meet.  Hence
it cannot erase the mixed contribution \(c_T\).  \(\square\)

### Corollary 5.3: the dangerous centers are exactly the ones supported on mixed corner incidence

To prove nonvanishing of \(h_T\), it is enough to control the finitely
many polarization-active centers meeting the mixed corner receiver.

This is the sharp finite bottleneck left by `107_25`.

## 6. Corner-preservation criterion

We can now state the sought sufficient condition.

### Definition 6.1: corner-preserving regularization protocol

Say that the regularization protocol of `107_15` is `corner-preserving
at level \(T\)` if every polarization-active blow-up center is
corner-preserving in the sense of Definition 4.2.

### Theorem 6.2: sufficient condition for survival of the corner contribution

Assume the regularization protocol is corner-preserving at level \(T\).
Then:

1. the mixed corner contribution \(c_T\) remains visible in
   \(F_{{\rm v},T}^{(1)}\cdot F_{{\rm h},T}^{(1)}\);
2. the denominator \(h_T\) keeps the form
   \(2c_T+\text{controlled correction package}\);
3. if the total correction package fails to equal \(-2c_T\), then
   \(h_T\neq0\).

Proof.  Item 1 is Proposition 5.1.  Item 2 is the identity of `107_25`.
Item 3 is Corollary 5.2 of `107_25`.  \(\square\)

This is the first real theorem linking the blow-up protocol to the
primitive degree-zero denominator.

## 7. Why the protocol of `107_15` is naturally expected to be corner-preserving

The stated regularization protocol in `107_15` is designed to resolve
singularities while keeping the boundary and diagonal comparison data
visible, not to erase them.

### Proposition 7.1: the declared purpose of the regularization protocol favors corner preservation

The blow-ups of `107_15` are introduced to resolve:

1. diagonal/boundary intersection strata;
2. graph self-intersections;
3. singular boundary points;

while retaining the source generators and the Gamma--polar boundary
receiver on the final model.

Proof.  This is exactly how `107_15` motivates the regularization step,
and `107_16` identifies \(C_\infty\) as the common receiver required for
all later metric completions.  A protocol meant to preserve those data
is structurally aligned with corner-preserving regularization. \(\square\)

This is not yet a proof of corner preservation, but it shows the program
is internally coherent at this point.

### Consequence 7.2: corner collapse would contradict the current realization strategy

If the chosen regularization actually collapsed the mixed corner, then
the same move would simultaneously damage:

1. the polarization denominator of `107_25`;
2. the boundary receiver \(\mathcal L_\infty\) of `107_16`;
3. the logarithmic singularity model of `107_23`.

So corner collapse is not a benign technicality; it would break several
already fixed parts of the Phase 107 strategy at once.

## 8. Finite exceptional audit for the denominator

The previous sections convert the denominator problem into a finite
audit.

### Checklist 8.1: exceptional audit for \(h_T\)

To prove \(h_T\neq0\), it now suffices to verify:

1. the finite list of polarization-active centers at level \(T\);
2. that each such center is corner-preserving;
3. the resulting signs or sizes of the correction terms in the package
   \(\varepsilon_{\rm vv}(T),\varepsilon_{\rm hh}(T),
   \varepsilon_{\rm vh}(T)\);
4. that their sum does not cancel \(-2c_T\).

### Proposition 8.2: the denominator problem is now a finite local regularization problem

At fixed support level \(T\), the nonvanishing of
\(H_T^{(1)}\cdot H_T^{(1)}\) is reduced to a finite local audit of
exceptional centers and their correction signs.

Proof.  The visible support set \(S_T\) is finite, hence only finitely
many graph closures and singular strata enter the regularization
protocol.  By Corollary 5.3, only the polarization-active centers
meeting the mixed corner matter for \(h_T\).  \(\square\)

This is the exceptional-locus analogue of the chartwise reduction of
`107_23`.

## 9. What is now closed

This note closes the next geometric gap after `107_25`.

1. the correction package in the denominator is localized to a finite
   set of polarization-active exceptional centers;
2. the dangerous blow-up centers are identified as the corner-collapsing
   ones;
3. a corner-preserving regularization criterion now gives a sufficient
   condition for the survival of the corner contribution in the
   denominator;
4. the nonvanishing of \(h_T\) is reduced to a finite local audit of the
   regularization loci.

## 10. What remains open

This note still does not complete Part III-B or E1.

1. It does not yet list the actual polarization-active centers for a
   fully constructed \(\mathcal X_T^{(1)}\).
2. It does not prove corner preservation center by center.
3. It does not compute the correction signs/norms numerically.
4. It does not prove the pairing transport identity or exact-kernel
   identity.
5. It does not prove the terminal identity of `107_13`.

## 11. Next technical front

The next proof-bearing move is now to enumerate the actual mixed
corner-adjacent centers in the chart atlas of `107_17` and prove, one by
one, that the intended blow-ups are corner-preserving.  That would turn
the present sufficient criterion into a genuine proof of nonvanishing
for the polarization denominator.
