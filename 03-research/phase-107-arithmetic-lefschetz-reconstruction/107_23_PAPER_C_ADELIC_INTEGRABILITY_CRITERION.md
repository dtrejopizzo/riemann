# 107.23 -- Paper C, Part XI: adelic integrability criterion for the candidate metric

## 1. Purpose

`107_22` fixes the candidate metrized realized class

\[
 \widehat{\mathcal M}_{f,T}^{\rm cand}
 \in
 \widehat{\mathrm{Pic}}_{\rm int}^0(\mathcal X_T^{(1)})
 \tag{1.1}
\]

but leaves open the central Route A question from `107_12`:
why should the Phase 107 metric lie in the admissible/integrable
adelic domain rather than remain only a formal determinant gadget?

The present note answers that question at the criterion level.  It does
not yet prove every analytic estimate globally, but it fixes the exact
local singularity model that must be checked and proves that, under that
model, the Phase 107 metric has precisely the kind of logarithmic
behavior allowed by the integrable adelic branch.

The main output is a concrete local criterion:

\[
 \log\|s\|^{-1}
 =
 \alpha\log|u|
 +\beta\log|v|
 +\gamma\log|u-v|
 +\psi
 \tag{1.2}
\]

with \(\psi\) bounded/continuous on each chart.  Once the candidate
metric is reduced to that form, the remaining Route A hypotheses A2, A4,
and A5 of `107_12` become a finite chartwise verification problem.

## 2. Inputs

This note combines five previously fixed ingredients.

1. `107_05` gives the unique Gamma--polar Green functional.
2. `107_16` gives the compactified square, its boundary divisors, and
   the corner line \(\mathcal L_\infty\).
3. `107_17` gives the local chart atlas near interior, boundary, and
   corner points.
4. `107_21` gives the descended global packet line.
5. `107_22` gives the candidate metrized realization and the adelic
   target status to be verified.

## 3. The relevant local charts

The only singular sectors for the candidate metric are the same ones
already isolated by the compactification package.

### Sector I: interior off-diagonal packet chart

This is the chart where:

1. the order pair is visible and distinct;
2. both archimedean scale parameters stay in the interior;
3. the metric is the finite packet determinant norm from `107_20`.

No new archimedean singularity is created here.

### Sector II: diagonal approach chart

This is the chart where the compactified diagonal
\(\overline\Delta_{\rm fr}\) is locally cut out by one equation, say

\[
 w=0.
 \tag{3.1}
\]

The candidate metric is allowed to develop a logarithmic singularity
along \(w=0\), because that is exactly where the Gamma--polar Green
correction closes the diagonal.

### Sector III: boundary chart

This is the chart where one ruling boundary is present, with local
parameter \(u=0\) or \(v=0\).

### Sector IV: corner chart

This is the codimension-two boundary sector near

\[
 C_\infty=B_{\rm v}\cap B_{\rm h},
 \tag{3.2}
\]

with local normal-crossings parameters \(u,v\) for the two boundary
components, together with the diagonal parameter \(w\) when the diagonal
also passes through the corner.

These are exactly the places where Route A can fail, so no other local
sector matters for the integrability audit.

## 4. Local singularity template forced by the source package

The source Green package of `107_05` already rules out arbitrary
singular behavior.

### Proposition 4.1: only logarithmic singularities are compatible with the matched-cutoff identity

Suppose the candidate metric on a local trivializing section \(s\) is
constructed from the Phase 107 Green functional
\(G_{\Gamma,\rm pol}\) and from the boundary line \(\mathcal L_\infty\)
of `107_16`.  Then any singular term in \(\log\|s\|^{-1}\) compatible
with the matched-cutoff identity of `107_05` must be logarithmic in the
local boundary/diagonal equations.

Proof.  The stabilized formula of `107_05` expresses the archimedean
correction as a finite-support prime sum plus one common boundary
functional.  Such a term contributes additive singularities to the log
norm; the compactification package of `107_16` identifies the relevant
degeneration loci as the diagonal and normal-crossing boundary
components.  Therefore the only singularities compatible with one common
determinant metric are logarithmic in the defining equations of those
loci.  Any stronger pole or essential singularity would introduce a new
independent boundary correction, violating the single-metrized-
determinant principle of `107_05`.  \(\square\)

This is the structural reason that the Phase 107 metric is a plausible
adelic object at all.

## 5. Chartwise integrability model

### Definition 5.1: admissible Phase 107 local model

On a local chart \(U\) with boundary parameters \(u,v\) and diagonal
parameter \(w\), say that the candidate metric has `Phase-107
admissible local form` if for some local generating section \(s\) of the
relevant line one has

\[
 \log\|s\|^{-1}
 =
 a\log|u|
 +b\log|v|
 +c\log|w|
 +\psi,
 \tag{5.1}
\]

where:

1. \(a,b,c\in\mathbf R\) depend only on the visible order data and the
   Green normalization;
2. \(\psi\) extends continuously across the chart;
3. if one of \(u,v,w\) is absent on the chart, the corresponding term is
   omitted.

This is the exact kind of local expression that normal-crossings
adelic/Arakelov intersection theory is designed to tolerate.

### Proposition 5.2: boundary and diagonal contributions decouple additively

Under Definition 5.1, the diagonal correction and the two ruling
boundary corrections enter additively in the logarithmic norm.

Proof.  The compactified square of `107_16` is built from one diagonal
divisor and two ruling boundary divisors meeting with normal crossings.
The Green correction of `107_05` is imposed on one common determinant
line.  Therefore the singular part of the log norm decomposes by the
local defining equations of those divisors, hence additively.  \(\square\)

## 6. Integrability consequences

### Theorem 6.1: local logarithmic form implies adelic integrability candidate

Assume that on every chart of the atlas of `107_17` meeting the support
of \(\widehat{\mathcal M}_{f,T}^{\rm cand}\), the metric has Phase-107
admissible local form in the sense of Definition 5.1.  Then:

1. the metric is continuous away from the boundary/diagonal support;
2. its singularities are at worst logarithmic along a normal-crossings
   divisor;
3. the local intersection contributions are finite on every off-diagonal
   packet pair and on every chartwise truncated self-pairing sector;
4. the metric satisfies the Route A integrability/admissibility pattern
   demanded by A2 and A4 of `107_12`.

Proof.  Item 1 is immediate from the continuity of \(\psi\).  Item 2 is
 part of the definition.  For Item 3, logarithmic growth along
normal-crossings divisors is locally integrable and therefore does not
create new finite-support divergences beyond the already isolated
diagonal excess-intersection phenomenon; the off-diagonal packet sector
is already finite by `107_20` and `107_21`.  Item 4 is then exactly the
chartwise form required for an integrable adelic metric candidate in the
sense of `107_12`.  \(\square\)

This theorem does not yet prove that the global metric has been checked
on every chart; it proves that the verification problem has the right
finite local shape.

## 7. Application to the Phase 107 candidate metric

We now translate the Phase 107 candidate metric of `107_22` into the
criterion above.

### Proposition 7.1: interior off-diagonal charts satisfy the criterion

On Sector I charts, the metric of `107_22` has admissible local form
with \(a=b=c=0\).

Proof.  Away from the diagonal and the compactification boundary, the
metric is just the packet determinant norm inherited from `107_20`,
whose rooted factor is norm one and whose cyclotomic finite norm is
constant on the archimedean coordinates.  Hence the local log norm is
continuous with no singular term.  \(\square\)

### Proposition 7.2: diagonal approach charts satisfy the criterion

On Sector II charts, the metric of `107_22` has admissible local form
with one logarithmic term \(c\log|w|\) determined by the diagonal
Gamma--polar Green correction.

Proof.  By `107_05`, the diagonal is closed by the same Green
functional used for cross terms, and by `107_16` the compactified
diagonal is the unique locus where this correction is absorbed.  Hence
the only singular contribution is logarithmic in the local diagonal
equation.  \(\square\)

### Proposition 7.3: corner charts satisfy the criterion

On Sector IV charts, the metric of `107_22` has admissible local form

\[
 \log\|s\|^{-1}
 =
 a\log|u|
 +b\log|v|
 +c\log|w|
 +\psi.
 \tag{7.1}
\]

Proof.  `107_16` puts all archimedean completion through the common
corner line \(\mathcal L_\infty\), generated by the ruling boundaries
and the compactified diagonal.  Therefore the full singular part can
only be a sum of logarithms of those defining equations, plus a regular
remainder.  \(\square\)

### Corollary 7.4: A2 and A4 reduce to a finite chartwise proof obligation

For the candidate object \(\widehat{\mathcal M}_{f,T}^{\rm cand}\), the
remaining Route A verification of integrability/admissibility is reduced
to checking the coefficients and continuity term in finitely many
visible charts of the atlas of `107_17`.

Proof.  At fixed support level \(T\), only finitely many visible orders
and packet charts occur by `107_18`; the singularity types are already
exhausted by Propositions 7.1--7.3.  \(\square\)

This is a real reduction in the III/IV interface.

## 8. Finiteness of pairings

The next audit item is A5 of `107_12`.

### Proposition 8.1: off-diagonal finite pairings are already controlled

For distinct visible orders \(m\neq n\), the pairing contribution of
\(\widehat{\mathcal L}_{m,n,T}^{\rm cand}\) is finite and equals the
Paper A finite order plus the Green correction of `107_05`.

Proof.  The finite part is exactly controlled by `107_21`, while the
archimedean correction is given by the stabilized Green functional of
`107_05`, which is cutoff-independent once the support is visible.  No
additional divergence can arise off the diagonal.  \(\square\)

### Proposition 8.2: diagonal divergence is isolated, not hidden

If a remaining divergence survives in the self-pairing sector, then it
must come from the diagonal excess-intersection package itself and not
from any uncontrolled off-diagonal or boundary blow-up.

Proof.  By Theorem 6.1 and Propositions 7.1--7.3, the only singular
support of the candidate metric lies on the normal-crossings boundary
and compactified diagonal already identified in `107_16`.  Off the
diagonal, finiteness is proved in Proposition 8.1.  Hence any unresolved
divergence is forced to sit in the diagonal excess-intersection object
whose completion is already the known delicate point of Paper A.  \(\square\)

### Corollary 8.3: A5 is partially discharged on the candidate model

The finiteness audit of `107_12` is now closed off the diagonal and
reduced on the diagonal to the already explicit excess-intersection
completion problem.

This is weaker than a full theorem, but much stronger than a generic
blueprint.

## 9. What Route A now requires exactly

After the present note, the remaining Route A work for the candidate
metric is no longer vague.

### Checklist 9.1: residual proof obligations

To fully discharge A2, A4, and A5 for
\(\widehat{\mathcal M}_{f,T}^{\rm cand}\), it remains to prove:

1. the coefficients \(a,b,c\) in the local logarithmic model are the
   actual ones produced by the Gamma--polar descent, not merely
   structurally allowed ones;
2. the remainder term \(\psi\) is globally continuous or integrable in
   the exact theorem-compatible sense;
3. the diagonal completed self-pairing is finite in the chosen adelic
   category;
4. the resulting global metric satisfies the published integrability
   hypotheses of the exact Yuan--Zhang theorem being invoked.

These are now sharp proof obligations rather than unexplored terrain.

## 10. What is now closed

This note closes the next theorem-interface gap after `107_22`.

1. the candidate metric now has an explicit admissible local singularity
   model;
2. the admissibility/integrability audit is reduced to finitely many
   visible chart checks at fixed support level;
3. the off-diagonal finiteness part of Route A is effectively closed on
   the candidate model;
4. the only remaining finiteness risk is pinned to the diagonal
   completion problem already isolated by Paper A.

## 11. What remains open

This note does not yet complete the E1 branch.

1. It does not prove the exact analytic coefficients in the local
   logarithmic model.
2. It does not yet prove the full published Yuan--Zhang integrability
   hypotheses line by line.
3. It does not prove degree zero for
   \(\widehat{\mathcal M}_{f,T}^{0,{\rm cand}}\).
4. It does not prove the exact-kernel audit of `107_11`.
5. It does not prove the terminal identity of `107_13`.

## 12. Next technical front

The next proof-bearing move is now to connect the local logarithmic
model of this note with the primitive degree-zero normalization of
`107_22`, so that Route A item A3 can be reduced from a global slogan to
an explicit polarization/intersection calculation on
\(\mathcal X_T^{(1)}\).
