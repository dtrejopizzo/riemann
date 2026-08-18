# E101.054 - Difficulty flow and novelty gate

## 1. Purpose

The current route contains many exact identities and several equivalent
coordinates for the same limiting assertion.  Exactness alone does not show
that the remaining difficulty has decreased.  This document audits where the
difficulty moves and imposes a stopping rule on further reformulation.

Let `Z` denote the arithmetic build and let `P` denote a controlled build
with one prescribed off-line quartet.  The control is used only as a
falsifier.  No location from `P` may enter an argument for `Z`.

## 2. Model-separation lemma

Let `I_1,...,I_r` be statements defined on a class of builds containing both
`Z` and `P`.

### Lemma 2.1

Assume

```text
I_j(P) is true for every j,
Omega7(P) is false.                                  (2.1)
```

Then the implication

```text
I_1(B) and ... and I_r(B) => Omega7(B)               (2.2)
```

cannot be valid on that class.

### Proof

Apply (2.2) to `B=P`.  Its hypotheses hold and its conclusion does not.  This
is a contradiction. `QED`

The lemma is elementary, but it is the exact logical form of conservation of
difficulty.  Every valid route to `Omega7(Z)` must contain at least one input
`D(Z)` for which

```text
D(P) is false.                                       (2.3)
```

Such an input is called a discriminating input.  If all preceding inputs pass
the control, the force has not yet appeared.

## 3. Three classes of statements

The present route contains three logically different classes.

### 3.1 Universal finite algebra

This class includes

```text
bordered determinant identities;
horizontal characteristic projection;
dual Green-row equations;
cofactor and maximal-minor formulas;
rectangular displacement identities;
periodic Cauchy summation;
external-column rational transfer.                  (3.1)
```

These statements hold for arbitrary matrices satisfying the stated finite
hypotheses.  They necessarily pass `P`.  They can expose the scalar where the
difficulty lives, but cannot supply the discriminating input.

### 3.2 Build-neutral convergence infrastructure

This class includes

```text
LP contraction when formulated for the common operator class;
fixed-L Fourier convergence;
PROLATE-BV-MOMENT;
geometric far-column decay;
summable mesh and prime tails in absolute convergence;
cofinal diagonal selection.                          (3.2)
```

The intended statement must hold for `P` as well as `Z`.  By Lemma 2.1 it
cannot carry the force of `Omega7`.  A proof may be necessary for assembly,
but closing it does not shrink the discriminant.

### 3.3 Arithmetic discrimination

This class must fail for `P`.  In the current notation it appears as

```text
LOCAL-COVARIANT-IDENT;
STIELTJES-IDENT;
INTEGER-COFACTOR-IDENT;
HEAT-COFACTOR-IDENT;
DIRECTIONAL-IDENT;
MATCHED-CURRENT-IDENT.                               (3.3)
```

The listed statements are not six independent obligations.  They are
coordinates for one obligation.  Several are already proved equivalent, and
each one by itself implies `Omega7` after the established compactness or
uniqueness step.

## 4. The reformulation cycle

The dependency chain inside Phase 101 is

```text
signed covariant boundary cancellation
 -> positive Stieltjes-transform identification
 -> countable safe values
 -> compact moment sequence
 -> beta-mixture representation
 -> arithmetic heat defect
 -> Gaussian-Weil determining family
 -> directional paired residual
 -> matched invariant current.                      (4.1)
```

Every arrow in (4.1) has produced a useful exact representation or a sharper
falsifier.  None has yet produced a new premise satisfying (2.3).  Therefore
(4.1) is a coordinate atlas, not a descending sequence of weaker open
theorems.

This gives a precise answer to the circularity concern:

```text
the route is not formally circular in its proved algebra;
the research motion has become circular at the discriminant level.       (4.2)
```

Proving another equivalence among the nodes in (4.1) cannot change that
verdict.

## 5. No-go patterns currently visible

### 5.1 Positivity return

Complete monotonicity of the heat defect, positivity on the complete
Gaussian-Weil family, and nonnegativity of all Li coefficients are equivalent
forms of the same sign problem.  A proof that assumes any one of them to prove
another has returned to the original wall.

Finite-order heat inequalities do not repair this.  E101.037 constructs
models passing every prescribed finite order and failing later.

### 5.2 Absolute shell ceiling

Bounding a coherent shell by the sum of the magnitudes of its cells loses the
required cancellation.  The phase-79 edge audit already rules out that
method.  FAR-MOMENT and COLLAR-RATIONAL are admissible only as a signed,
recombined transfer.

### 5.3 Target insertion

Identifying a finite limit with `Xi` by analytic continuation from the target
itself would assume the desired divisor.  Arithmetic identification is
admissible on `Re(s)>1`, where the Euler series converges absolutely.  Any
passage from there to the critical boundary must be produced by the finite
construction, not imported from the known continuation of `Xi`.

### 5.4 Infrastructure promoted to discrimination

Neither GAP-Z, PROLATE-ENDPOINT, nor a uniform projective bound may use a
property that fails for `P`.  If it does, the statement has silently changed
from build-neutral infrastructure into the force-RH step.

## 6. Audit of the active Phase 101 fronts

```text
front                         passes P   role
--------------------------------------------------------------
PROLATE-BV-MOMENT             yes        infrastructure
fixed-L Fourier diagonal      yes        infrastructure
FAR-MOMENT                    expected   infrastructure
COLLAR-RATIONAL               expected   infrastructure
LP normality bounds           required   infrastructure
dual/cofactor transfer        yes        universal algebra
MATCHED-CURRENT-IDENT         no         discriminant
Gamma-prime endpoint match    no         discriminant
complete heat monotonicity    no         equivalent sign form.            (6.1)
```

The first six rows may be completed later for final assembly.  They must not
remain the main research front while the last two rows have no forcing
mechanism.

## 7. Novelty gate

A proposed new step counts as progress on the discriminant only if it passes
all five tests.

```text
N1  It is stated before taking the cofinal limit.
N2  Its hypotheses use finite CCM data and Euler--Gamma data only in
    absolute convergence.
N3  The controlled off-line build violates its conclusion.
N4  The proof does not invoke positivity, a zero location, an unknown Riesz
    projection, or a sum of absolute cell magnitudes.
N5  It implies MATCHED-CURRENT-IDENT through a one-way estimate or uniqueness
    theorem, not through a restatement of MATCHED-CURRENT-IDENT.           (7.1)
```

Failure of `N3` classifies the step as infrastructure.  Failure of `N5`
classifies it as another coordinate.  Failure of `N2` or `N4` classifies it
as inadmissible.

## 8. New attack coordinate: two-transport holonomy

The finite construction has two exact transports:

```text
spectral transport: enlarge the Fourier section N;
arithmetic transport: turn on the von Mangoldt operator along t.          (8.1)
```

E101.003--E101.005 give the infinitesimal arithmetic transport as one
horizontal bordered cofactor.  E101.046 and E101.051 give the spectral-shell
transport as a dual rational current.

The next proposed object is not another limiting transform.  It is the
finite closed-loop mismatch between these two transports:

```text
HOL_(N,t)(z)
=Delta_N[horizontal arithmetic current]
 -partial_t[spectral shell logarithm].               (8.2)
```

For a single scalar determinant whose two transports are computed from the
same finite matrix, the complete mixed difference is zero.  The useful object
is therefore the difference between

```text
the spectral connection supplied by the bordered determinant,
the independent Euler--Gamma connection supplied by the explicit formula.
                                                               (8.3)
```

Its curvature is exactly the failure of their finite compatibility.  A
viable theorem would have the form

```text
ARITHMETIC-HOLONOMY:
  the signed sum of HOL over one cofinal rectangle is a four-boundary term;
  three boundaries vanish by build-neutral estimates;
  the fourth is MATCHED-CURRENT-IDENT.               (8.4)
```

This direction is worth testing because it can sum the prime cells before
taking absolute values and can keep the shell current coupled.  It also has a
mandatory falsifier: the independent Euler connection is unchanged by an
inserted off-line quartet, whereas the spectral connection is changed, so the
closed-loop mismatch must retain a nonzero boundary defect for `P`.

Equation (8.4) is not yet a theorem.  Before it is promoted, the next document
must derive `HOL` entirely from the existing finite matrices and verify `N1`
through `N5`.  If the resulting curvature is merely the old IDENT defect with
no new finite cancellation, the direction is rejected immediately.

## 9. Work decision

```text
freeze as main front:
  further sharpening of PROLATE-ENDPOINT;
  further GAP-Z profile fitting;
  new equivalent Stieltjes, moment, heat or Weil coordinates;

retain for later assembly:
  E101.046--E101.053;

promote as main front:
  finite arithmetic holonomy and its planted falsifier;
  only if it passes the novelty gate.                (9.1)
```

This is a priority change, not a claim that the infrastructure is false.

## 10. Status

```text
proved:
  model-separation lemma;
  logical classification of universal, build-neutral and discriminating
  statements;
  the existing equivalences form a coordinate atlas;

found:
  current effort was rotating at the discriminant level;
  PROLATE-BV-MOMENT cannot be the force-RH step;

adopted:
  five-part novelty gate;
  stop rule on further coordinate reformulation;

open:
  derive or reject ARITHMETIC-HOLONOMY at finite level;
  prove a discriminating input that passes N1--N5;
  Omega7.
```
