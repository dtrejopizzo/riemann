# 114.a.126 — H7: fresh evaluation is natural for open restrictions

```
+------------------------------------------------------------------------+
| SOURCE      Haran's O(D) is a sheaf/right act and restricts on opens.   |
| COMMON      Choose one fresh p avoiding all denominators in a finite    |
|             open-restriction diagram.                                  |
| NATURAL     Evaluation of a restricted rational operation equals the   |
|             restriction of its evaluation.                             |
| IMAGE       Global evaluated images include canonically into local ones.|
| CLOSED      The open-restriction part of H7-FRESH-RESTR.                |
| OPEN        Restriction to a closed Cartier quotient and its fiber count.|
+------------------------------------------------------------------------+
```

## 1. A finite open diagram and one fresh target

Fix a completed divisor presentation `D` on `Y^reg` and a finite diagram of
open inclusions `V subset U` occurring at finitely many pro-levels.  Haran's
equations (8.8)--(8.9) give restriction homomorphisms of the structure
generalized rings, and (11.7) makes `O(D)` a sheaf of operation sets with a
right action.  Thus there are source restriction maps

\[
 r_{UV}:\mathcal O(D,U)\longrightarrow\mathcal O(D,V).                 \tag{1.1}
\]

Only finitely many rational coefficients and denominators occur in the
chosen diagram and in the selected powers.  Choose the least prime `p`
satisfying the `a118` fresh conditions for their union, and use one product
bio target

\[
 T=\prod_{e\in E}\mathbb F_p^{(e)}.                                   \tag{1.2}
\]

Every denominator in the entire diagram is a unit in `T`.

## 2. Naturality

Let `epsilon_U` evaluate a rational operation section on `U` in (1.2).
Restriction changes only the open on which the same localized expression is
read.  A generalized-ring homomorphism commutes with composition,
contraction, involution and localization at elements sent to units.  Hence

\[
 \varepsilon_V(r_{UV}s)=\varepsilon_U(s)                              \tag{2.1}
\]

for every scalar section `s` on `U`, after identifying both values with
their common element of `T`.

### Theorem 2.1 (fresh open naturality)

Common fresh evaluation defines a natural transformation from every finite
open-restriction diagram of bounded scalar sections to the constant diagram
with value `T`.  In particular,

\[
 \mathrm{im}\,\varepsilon_U
 \subseteq\mathrm{im}\,\varepsilon_V\subseteq T                  \tag{2.2}
\]

whenever `V subset U`.

### Proof

Equation (2.1) proves naturality.  Every value of a section on `U` is also
the value of its restriction on `V`, which proves (2.2).  Composition of
open restrictions gives the same localized expression, so all higher
commuting triangles follow.  QED.

The same argument is compatible with source multiplication: for sections
`s,t` whose product is defined,

\[
 \varepsilon_V(r(st))
 =\varepsilon_V(r(s)r(t))
 =\varepsilon_U(s)\varepsilon_U(t).                                   \tag{2.3}
\]

No transition between targets attached to different output diagrams is used.

## 3. Exact remaining restriction gate

This closes the open-sheaf naturality part of H7-FRESH-RESTR.  It does not
construct a restriction functor from completed right acts to a closed
generalized Cartier quotient `Z`, nor a source sequence comparing
`O(D-Z)`, `O(D)` and `O(D|_Z)`.  The remaining typed statement is therefore

> **H7-FRESH-CARTIER.** Construct the closed-Cartier source restriction
> diagram on `Y^reg`, prove common fresh evaluation is natural for it, and
> prove the finite fiber/cardinality relation needed by the sheaf/Deligne
> comparison.

The all-ray numerical RR theorem `a120` does not depend on this stronger
comparison.  H7-FRESH-CARTIER, H7-RULING-PF, the Cartier/Deligne realization,
row A and RH remain open.

**Later resolution (`a127`).**  The common-target form of
H7-FRESH-CARTIER is impossible: the inverse generic chart makes the Cartier
prime invertible, while the closed quotient sends it to zero.  The corrected
comparison gate is the two-target determinant/norm-line statement
H7-TWO-TARGET-DELIGNE.

## 4. Verification scope

`114_a_126_h7_fresh_open_restriction_verify.py` checks localization and
reduction on exhaustive rational samples, image inclusion, multiplication,
composition of restrictions and the source anchors.  The categorical proof
of (2.1) is functoriality of localization, not a numerical extrapolation.
