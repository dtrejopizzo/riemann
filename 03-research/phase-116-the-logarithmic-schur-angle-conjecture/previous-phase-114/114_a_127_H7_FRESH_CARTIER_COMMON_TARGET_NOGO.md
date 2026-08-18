# 114.a.127 — H7: the fresh generic target cannot also be a Cartier residue target

```
+------------------------------------------------------------------------+
| GENERIC     Evaluating a section containing 1/ell makes ell a unit.    |
| CLOSED      Factoring through the Cartier quotient by (ell) kills ell. |
| CONFLICT    A nonzero unital target cannot make ell both a unit and 0. |
| RETRACT     H7-FRESH-CARTIER cannot use one common algebra target.      |
| SURVIVES    Open restriction naturality and the direct all-ray RR count.|
| REPLACE     Compare generic moments and residue contact by norm lines,  |
|             not by a common evaluation square.                         |
+------------------------------------------------------------------------+
```

## 1. The incompatible universal properties

Let `A` be a unital (ordinary or generalized) ring, let `ell` be a central
scalar, and assume that a divisor chart contains the inverse-lattice scalar
`1/ell`.  A unital evaluation of that chart in a nonzero target `T` must
satisfy

\[
 f(\ell)f(1/\ell)=1,                                                   \tag{1.1}
\]

so `f(ell)` is a unit.  On the other hand, a map from the principal closed
Cartier quotient

\[
 A/E((\ell))\longrightarrow T                                        \tag{1.2}
\]

exists exactly when the image of `ell` is zero.  This is the quotient
universal property used in `a67`.

### Lemma 1.1 (unit-zero obstruction)

There is no nonzero unital target `T` and compatible pair of maps from both
`A[1/ell]` and `A/E((ell))` whose restrictions to `A` agree.

### Proof

Compatibility makes the common image of `ell` a unit by (1.1) and zero by
(1.2).  Then `1=f(ell)f(1/ell)=0`, contradicting nonzeroness of `T`.  QED.

The argument is characteristic-free.  In particular it is not repaired by
choosing a fresh finite characteristic different from `ell`: that choice
makes `ell` invertible and therefore makes factorization through the
`ell`-residue quotient impossible.

## 2. Consequence for H7-FRESH-CARTIER

Take the prime ruling `V_ell=D_Y(ell)` and the inverse completed lattice used
to present `O(V_ell)`.  Common fresh evaluation, as in `a118`--`a120` and
`a126`, chooses a finite target in which every displayed denominator,
including `ell`, is a unit.  A closed-restriction evaluation on `V_ell`
would have to factor through the quotient killing `ell`.  Lemma 1.1 rules
out a commuting unital algebra square

\[
\begin{array}{ccc}
 A &\longrightarrow&A[1/\ell]\\
 \downarrow&&\downarrow\\
 A/E((\ell))&\longrightarrow&T
\end{array}                                                           \tag{2.1}
\]

with `T` nonzero.

### Theorem 2.1 (common-target Cartier no-go)

The remaining H7-FRESH-CARTIER demand in `a126`, if it means reevaluating
the inverse generic chart and its same-prime closed Cartier quotient in one
nonzero unital target, is impossible.  Hence that formulation is retracted;
there is no missing choice of a sufficiently large fresh prime that can
make it commute.

This theorem does **not** say that Haran's source closed quotient is absent.
The quotient exists by `a67`, and its ordinary diagonal layer is the genuine
residue object `F_ell`.  It says only that the generic moment evaluation and
the residue evaluation cannot be two faces of one unital evaluation apex.

## 3. The typed replacement

The two evaluations have different jobs:

1. the generic fresh target, with `ell` invertible, measures the calibrated
   section image of `a120`;
2. the residue target, with `ell=0`, measures the diagonal contact mass
   `log #F_ell=log ell` of `a67` and `a114`.

They must remain separate.  The remaining comparison gate is therefore:

> **H7-TWO-TARGET-DELIGNE.** Construct a determinant/norm-line or
> biextension comparison between the generic calibrated image and the
> Cartier residue/contact object, without a unital map between their
> evaluation targets.  Prove that its numerical class is the splitting
> `E_C tensor E_G ~= E_RR` of `a124` and that it descends to repaired
> Cartier classes.

Thus H7-FRESH-CARTIER is closed **negatively as a common-target strategy**.
The direct all-ray numerical RR theorem `a120`, open naturality `a126`, the
residue contact calculation, and the numerical Green biextension `a124`
survive.  H7-TWO-TARGET-DELIGNE and H7-RULING-PF remain open, so row A and RH
remain open.

In particular, row A and RH remain open.

## 4. Verification scope

`114_a_127_h7_fresh_cartier_nogo_verify.py` exhausts finite residue targets,
checks the localization/quotient truth table, and guards the source and
scope statements.  The general theorem is the displayed universal-property
contradiction, not a finite extrapolation.
