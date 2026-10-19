# P123.010 — a source effective cone for mixed kernels

## Status

`PROVED-IN-REPOSITORY` for a proper, functorial cone on every semilocal
rapid kernel algebra, stable under addition, nonnegative scaling, dagger
and conjugation by rational correspondence multipliers.

`PROVED-IN-REPOSITORY` that its image defines a cone on the numerical test
quotient without assuming positivity of the intersection pairing.

`OPEN` for properness after numerical quotient/completion, effective
descent in the stronger sense of lifting local positive factorizations,
and compatibility with the still-open completed mixed RR determinant.

## 1. Positivity belongs to the source algebra

Let `K_S^rapid` be the complete dagger algebra of P123.006 and let

```text
j_S:K_S^rapid -> C_0(A_S) rtimes_r Gamma_S            (1.1)
```

be its faithful regular representation in the reduced crossed product.
The acting group is abelian and hence amenable, so reduced and full norms
agree.  Moreover

```text
||j_S(F)||_(C*)<=||F||_0.                             (1.2)
```

Define the algebraic positive cone

```text
Eff_S^alg={sum_(i=1)^r X_i^dagger X_i:
           r finite, X_i in K_S^rapid}                (1.3)
```

and the source effective cone

```text
Eff_S=closure_Frechet(Eff_S^alg).                     (1.4)
```

No trace or intersection value enters this definition.

### Theorem 1.1 — proper functorial cone

`Eff_S` satisfies:

1. `Eff_S+Eff_S subset Eff_S` and `R_+ Eff_S subset Eff_S`;
2. every element is self-adjoint;
3. `Eff_S intersect (-Eff_S)={0}`;
4. `U_q^dagger Eff_S U_q subset Eff_S` for every rational multiplier
   available on the chart;
5. restriction `S -> S'` carries `Eff_S` into `Eff_(S')`.

### Proof

The first two claims hold for finite sums of squares and pass to the
Frechet closure.  By (1.2), Frechet convergence implies convergence in the
faithful `C*` representation.  Thus every element of `Eff_S` has positive
image.  If both `F` and `-F` lie in the cone, `j_S(F)` is both positive and
negative, hence zero; faithfulness gives `F=0`.

For a square,

```text
U_q^dagger (X^dagger X) U_q=(XU_q)^dagger(XU_q),      (1.5)
```

and the multiplier estimates of P123.006 put `XU_q` back in the rapid
ideal.  Continuity proves the assertion on the closure.  Finally,
restriction is a continuous dagger-algebra homomorphism, so it maps every
finite sum of squares to a finite sum of squares and then maps closures
into closures.  QED.

This cone is not claimed to be closed under multiplication: positive
operators do not have positive products unless they commute.

## 2. Descent to numerical equivalence

Let `Q_S` be any trace-class subalgebra on which the numerical radical
`R_A` of P123.007 is defined, and let `q:Q_S -> Q_S/R_A` be the quotient.
Define

```text
Eff_S^num=q(Eff_S intersect Q_S).                     (2.1)
```

It is a cone and is stable under every descended rational conjugation.
This is well-defined because it is the image of a source cone; no choice of
representative is used to test membership.

Properness need not survive a quotient: it is possible that effective
elements differ by an element of the numerical radical.  We therefore do
not assert

```text
Eff_S^num intersect (-Eff_S^num)={0}.                 (2.2)
```

Proving (2.2), or identifying the quotient order with a geometric order,
is part of the remaining A.6/A.7 comparison gate.

## 3. Independence from row D

For `X in K_S^rapid`, source effectivity says only that `X^dagger X` is a
square in the faithful `C*` realization.  It does **not** say

```text
I_A(X,X)>=0                                            (3.1)
```

or its negative.  The renormalized trace need not be a positive `C*` trace,
and no such assertion is used above.  Consequently the cone does not hide
RH or the desired Hodge sign.

The distinction is essential:

```text
C*-effectivity of kernels       [constructed in A]
intersection sign on primitive classes [the future row D].
```

## 4. Relation to classical effectivity

On a finite correspondence graph, the rank-one kernel section `s` produces
the square `s^dagger s`; direct sums produce (1.3).  Thus (1.3) is the
operator-kernel analogue of an effective cycle with nonnegative
multiplicity.  This observation is only a comparison principle.  A theorem
identifying the cone with effective algebraic cycles in the finite-field
control model is deferred to A.9.

## 5. A.7 verdict

A source-defined, nontrivial and proper mixed cone now exists on every
semilocal chart and is functorial for all operations currently used by the
kernel calculus.  It descends as a cone to numerical classes.

A.7 remains `PARTIAL` because two properties required by the final RR
package are not yet proved:

1. properness and closedness in the final separated numerical completion;
2. compatibility of this cone with the determinant of the identity/excess
   object completing A.8.

