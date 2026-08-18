# 114.a.100 — H7: finite-set reuse alone is retractable; obstruction needs nonsplit coefficients

```
+-------------------------------------------------------------------------+
| SOURCE      Multiplication/contraction are fiberwise over f:X->Y.        |
| SECTION     For every nonempty fiber choose s(y) in f^{-1}(y).           |
| INSERT      Put the tested coordinate at s(y), zeros elsewhere, and use  |
|             unit coefficients.                                           |
| RETRACT     Projection after multiplication, or contraction after        |
|             insertion, recovers the original coordinate.                 |
| CONSEQUENCE Noninjective finite-set maps alone cannot create              |
|             H7-NORETRACT-ENTANGLE.                                       |
| OPEN        Outer operation coefficients c,d with no compatible splitting.|
+-------------------------------------------------------------------------+
```

## 1. Fiberwise formulas

For an ordinary rig model and `f:X->Y`, Haran's formulas are

\[
 (b^Y\lhd a^f)_x=b_{f(x)}a_x,                                      \tag{1.1}
\]

\[
 (v^X\sslash a^f)_y=\sum_{x\in f^{-1}(y)}v_xa_x.                   \tag{1.2}
\]

The abstract generalized-ring operations are indexed by the same fibers;
the operadic zero insertions and coordinate projections satisfy
`projection o insertion=id` (the source explicitly records these split
maps after axiom (3.10)).

Ignore empty fibers, or restrict to the image of `f`.  Choose a section

\[
 s:Y\longrightarrow X,\qquad f\circ s=id_Y.                         \tag{1.3}
\]

## 2. Multiplication and contraction retractions

### Proposition 2.1 (multiplication coordinate retraction)

Put `a_(s(y))=1` in every selected position.  Projection of
`b^Y lhd a^f` to the coordinates `s(Y)` recovers `b^Y`.

### Proof

Equation (1.1) gives

\[
 (b^Y\lhd a^f)_{s(y)}=b_{f(s(y))}a_{s(y)}=b_y.                       \tag{2.1}
\]

QED.

### Proposition 2.2 (contraction coordinate retraction)

Insert `b_y` at coordinate `s(y)`, zero at the other coordinates of the
fiber, and put unit coefficients at the selected positions.  Contraction
recovers `b^Y`.

### Proof

In (1.2) every summand except `x=s(y)` is zero, and the remaining summand is
`b_y*1`.  QED.

The same identities are consequences of the abstract unit, zero-insertion
and fiberwise axioms; no additive cancellation or prime regularity is used.

## 3. Consequence for the parity remainder

Repeated occurrences caused solely by a noninjective set map `f` can be
isolated after choosing a section of its nonempty fibers.  Therefore this
raw reuse cannot by itself satisfy H7-NORETRACT-ENTANGLE from `a99`.

For a full equivalence-ideal edge

\[
 c\circ(a\oplus id_V)\circ d,                                      \tag{3.1}
\]

the possible loss of retraction must come from the outer operation labels
`c,d`: a zero divisor, a nonsplit contraction coefficient, or an overlap in
which no common probes neutralize the other labelled factors.  The finite
set ancestry is not enough.

The remaining exact gate is

> **H7-COEFF-NORETRACT.** Decide whether a sandwich context capable of the
> three parity even moves can have nonsplit outer coefficients `c,d` which
> block every scalar separator, while its endpoints remain 2-divisible and
> its odd closure absent.

If every such coefficient context admits a local splitting after refinement,
H7-CONTEXT-RETRACT follows and the parity branch is eliminated under
H7-TAME-PLANE.  If not, an explicit nonsplit coefficient diagram is required;
the XOR finite-set skeleton alone is not one.

H7-COEFF-NORETRACT, H7-TAME-PLANE, H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_100_h7_finite_set_retract_verify.py` exhausts all surjective finite
maps through six source points, constructs sections, and checks the exact
multiplication/contraction retractions over several finite rings.  It also
tests nonsurjective maps after restricting to their image and enforces the
coefficient-gate scope.

Primary source: Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831),
equations (3.2)--(3.10).
