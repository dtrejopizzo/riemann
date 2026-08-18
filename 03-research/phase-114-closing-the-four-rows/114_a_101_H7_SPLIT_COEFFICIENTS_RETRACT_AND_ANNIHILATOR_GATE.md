# 114.a.101 — H7: split outer coefficients retract; nonsplit alone is not an obstruction

```
+-------------------------------------------------------------------------+
| CONTEXT     C(a)=c o (a plus e) o d.                                   |
| SPLIT       A left inverse of c and a right inverse of d transmit every |
|             scalar sandwich of a exactly through C.                    |
| MATRIX TEST On an active scalar block, this is the unimodular-row/column|
|             criterion; accessible probe coefficients form I(c)I(d).    |
| WARNING     Nonsplit coefficients can still act injectively.            |
| EXACT NEED  A separated pair which is killed by the two-sided outer     |
|             coefficient context.                                       |
| OPEN        H7-COEFF-ANN (or an independent proof of tameness/purity).   |
+-------------------------------------------------------------------------+
```

## 1. Typed split-coefficient theorem

Work in Haran's bilateral `C F R^t` operation notation, with operation sets
`A_(Y,X)` and their structural zero and identity maps.  (Only this typed
bilateral statement is used here.)  Fix finite sets `X,Y,X_0,Y_0,W,Z` and
operations

\[
 a\in A_{Y,X},\quad e\in A_{Y_0,X_0},\quad
 c\in A_{Z,Y\amalg Y_0},\quad d\in A_{X\amalg X_0,W}.
\]

The corresponding occurrence context is

\[
 C(a)=c\circ(a\oplus e)\circ d\in A_{Z,W}.                 \tag{1.1}
\]

Assume that there are typed operations

\[
 \ell\in A_{Y\amalg Y_0,Z},\qquad
 r\in A_{W,X\amalg X_0}                                   \tag{1.2}
\]

such that

\[
 \ell\circ c=id_{Y\amalg Y_0},\qquad
 d\circ r=id_{X\amalg X_0}.                               \tag{1.3}
\]

### Theorem 1.1 (split coefficients transmit every sandwich)

For every `b in A_(1,Y)` and `q in A_(X,1)` there are
`B in A_(1,Z)` and `Q in A_(W,1)`, independent of `a`, with

\[
 B\circ C(a)\circ Q=b\circ a\circ q                       \tag{1.4}
\]

for every admissible `a`.

### Proof

Extend `b` and `q` by zero on the inactive blocks:

\[
 \bar b=(b,0)\in A_{1,Y\amalg Y_0},\qquad
 \bar q=(q,0)^t\in A_{X\amalg X_0,1}.
\]

Set `B=bar b o ell` and `Q=r o bar q`.  Associativity, (1.3), and the
zero axioms give

\[
\begin{aligned}
 B\circ C(a)\circ Q
 &=\bar b\circ\ell\circ c\circ(a\oplus e)\circ d\circ r\circ\bar q\\
 &=\bar b\circ(a\oplus e)\circ\bar q
 =b\circ a\circ q.
\end{aligned}
\]

No subtraction, normal form, tameness or prime regularity is used.  QED.

### Corollary 1.2

Under H7-TAME-PLANE, no context satisfying (1.3) can identify two distinct
rigid decorations in its active occurrence.  This is Theorem 3.1 of `a99`
with sandwich-retractability now proved rather than assumed for all split
outer labels.

Structural permutations, coordinate insertions/projections and the
finite-set section maps of `a100`, when placed in the required orientation
and restricted to the selected active coordinates, lie in this split
sector.  Consequently a
remaining H7-NORETRACT-ENTANGLE diagram must contain a genuinely nonsplit
outer label after all common refinements and removal of structural maps.

## 2. Exact ordinary-matrix shadow

The residual matrix calculation makes the word *nonsplit* testable.  Take
an active scalar block over a commutative ring `R`, a column
`u=(u_i)` on the left and a row `v=(v_j)` on the right.  Scalar outer probes
produce coefficients

\[
 \left(\sum_i B_i u_i\right)
 \left(\sum_j v_j Q_j\right).
\]

Hence the accessible coefficient ideal is

\[
 I(u)I(v),\qquad I(u)=(u_i),\quad I(v)=(v_j).                \tag{2.1}
\]

### Proposition 2.1 (unimodular criterion)

The active scalar sandwich is retractable in the matrix model if and only
if both `I(u)=R` and `I(v)=R`; equivalently `u` has a left row inverse and
`v` a right column inverse.

### Proof

The two unit-ideal conditions explicitly give probes whose two factors are
one.  Conversely, if `1` belongs to `I(u)I(v)`, then
`I(u)I(v)=R`.  Since `I(u)I(v)` is contained in each factor ideal, both
factor ideals equal `R`.  QED.

This criterion is a residual diagnostic, not a proof that Haran's arithmetic
plane is a matrix generalized ring; `a87` explicitly leaves that assertion
open.

## 3. Nonsplit is necessary but not sufficient

Failure of (1.3) does not itself create a collision.  Over `Z`, the nonsplit
scalar context `a |-> 2a` is still injective.  By contrast, over `Z/4Z` the
same coefficient kills the nonzero difference between `0` and `2`.  Thus a
genuine obstruction needs both:

1. nonsplit outer coefficients; and
2. a nonzero, ambiently separable pair whose difference is annihilated by
   their two-sided context.

In an ordinary matrix residual this means a nonzero matrix `K` with

\[
 cK d=0.                                                    \tag{3.1}
\]

For the generalized-ring presentation the subtraction-free formulation is
the equality

\[
 c\circ(D_0\oplus e)\circ d
 =c\circ(D_1\oplus e)\circ d                               \tag{3.2}
\]

for distinct `D_0,D_1` separated by some ambient scalar sandwich.  This is
compatible with Haran's annihilator-ideal formalism, but (3.2) must be
proved inside the actual arithmetic-plane quotient, not merely in a finite
residual model.

The remaining exact branch of this **nonextractable-parity/context-retraction
route** is therefore

> **H7-COEFF-ANN.** Construct (3.2) for the rigid even moves with genuinely
> nonsplit labels and prove the required fold-zero endpoints survive the
> full macro closure; or prove that no such two-sided annihilation can occur
> in the arithmetic plane.

This strictly sharpens H7-COEFF-NORETRACT from `a100`; it is not a proof that
parity exhausts every possible macro obstruction.  It does not settle
H7-TAME-PLANE, H7-p-CONVEX, H7-p-DIVPATH or H7-PRIME-REG.  Row A remains
open.

## 4. Verification scope

`114_a_101_h7_split_coefficient_retract_verify.py` exhausts small matrices
over `Z/nZ`, checks Theorem 1.1 in its ordinary-matrix realizations, checks
the unit-ideal criterion, and exhibits both the injective nonsplit integer
map and the annihilating `Z/4Z` control.  The general proof is the typed
identity above; the finite computation is regression evidence only.

Primary sources: Haran, [*New foundations for geometry*](https://arxiv.org/abs/1508.04636),
Appendix A.2 (sandwich generation) and Section 9.5 (annihilator ideals);
Haran, [*Geometry over F1*](https://arxiv.org/abs/1709.05831), equations
(3.2)--(3.10) (fiberwise operations and split structural maps).
