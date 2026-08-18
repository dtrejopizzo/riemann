# 107.73 -- Paper C adelic-class intrinsicity audit

## 1. Purpose

`107_57` exact-audits the generatorwise packaging shadow of `107_22`,
but one sharper finite question still remained open:
do the visible chart/root presentations define one intrinsic adelic
class shadow, or are we only repackaging local presentations that could
depend on the chosen trivialization?

This note exact-audits that intrinsicity shadow.

## 2. Exact shadow audited here

The verifier `107_73_paper_c_adelic_class_intrinsicity_audit.py`
exact-audits the following finite shadow of `107_22`.

1. Visible chart/root presentations with the same finite package and the
   same single receiver channel determine one quotient class.
2. The total archimedean receiver weight is intrinsic and does not vary
   with chart changes.
3. Root refinement is invisible at the quotient-class level.
4. Splitting the archimedean receiver into an extra visible channel is
   rejected as a different object rather than silently accepted as the
   same class.

So the candidate realized object is pressure-tested one level beyond
generatorwise additivity: the visible presentations must define one
intrinsic finite class.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper C adelic-class intrinsicity checks passed.
```

So the workspace now contains a reproducible exact audit that the
visible chart/root presentations of `107_22` determine one intrinsic
finite quotient-class shadow with one receiver channel only.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. chart/root presentation choices do not change the visible quotient
   class;
2. the receiver channel remains intrinsically single in the finite
   model;
3. extra receiver splitting is detected as a real mismatch.

It does **not** prove:

1. existence of a genuine adelic Picard class;
2. actual metric descent or integrability on a proved arithmetic
   surface;
3. the final realization theorem of `107_11`.

So the correct reading is:

\[
 \text{finite intrinsic adelic-class shadow exact-audited},
 \qquad
 \text{true adelic Picard class still open}.
 \]
