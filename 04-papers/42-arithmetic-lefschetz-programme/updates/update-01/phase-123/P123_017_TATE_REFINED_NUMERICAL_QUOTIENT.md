# P123.017 — Tate-refined numerical equivalence

> **Audit override (P123.018):** The original status claims below are
> superseded where identified by the [adversarial audit](P123_018_ADVERSARIAL_CARRIER_AUDIT.md).
> Global completed-carrier/descent acceptance is reopened.

## Status

`PROVED-IN-REPOSITORY` for the source-defined vector-valued numerical
pairing, its closed dagger ideal, its nondegenerate quotient, and the exact
Tate-boundary/primitive sequence.

`PROVED-IN-REPOSITORY` for a complete nuclear distributional realization
on which the pairing against the dense test sector remains separating and
the original test algebra acts continuously.

`OPEN` for multiplication of two arbitrary distributional boundary points
and for properness of the effective cone after this completion.

## 1. The two source Tate moments

On

```text
D=C_c^infinity(R_+^times)
```

define

```text
M_0(f)=integral f(x)d^times x,
M_1(f)=integral f(x)x d^times x.                      (1.1)
```

They are continuous multiplicative characters:

```text
M_j(f star g)=M_j(f)M_j(g).                           (1.2)
```

For the half-density dagger of P123.007,

```text
M_0(f^dagger)=conjugate(M_1(f)),
M_1(f^dagger)=conjugate(M_0(f)).                      (1.3)
```

Thus `M=(M_0,M_1):D->B_T=C^2` is exactly the external Tate/Rosati boundary
map.  It is surjective: the two distributions `1` and `x` are linearly
independent, so two sufficiently small bump functions around two distinct
positive points have linearly independent moment vectors.

Indeed, for the centrally normalized external translation

```text
(tau_u f)(x)=|u|^(-1/2)f(u^-1 x),
```

direct substitution gives

```text
M(tau_u f)=(|u|^(-1/2)M_0(f),|u|^(1/2)M_1(f)),       (1.4)
```

which is precisely `rho_T^ext` of P123.014.

Let

```text
D^0=ker M_0 intersect ker M_1.                        (1.5)
```

This is the source primitive test space, defined without a zero or a sign.

## 2. Why the trace and ruling coordinates must not be added

Let

```text
I_partial(f,g)=T(f star g^dagger)                     (2.1)
```

be the source pairing of P123.007, and let

```text
I_Tate(f,g)=M_0(f)conjugate(M_1(g))
            +M_1(f)conjugate(M_0(g)).                 (2.2)
```

The scalar sum `I_partial+I_Tate` could have a larger radical through
cancellation between unrelated components.  Numerical equivalence must
retain both tests separately.  Define the vector-valued pairing

```text
I_vec(f,g)=(I_partial(f,g),I_Tate(f,g)) in C^2.        (2.3)
```

and its radical

```text
R_W={f:I_vec(f,g)=0 for every g in D}.                (2.4)
```

### Proposition 2.1

```text
R_W=R_partial intersect D^0,                          (2.5)
```

where `R_partial` is the radical of P123.007.

### Proof

If `f in R_W`, the first component gives `f in R_partial`.  Since `M` is
surjective and the hyperbolic form on `B_T` is nondegenerate, vanishing of
the second component against every `g` gives `M(f)=0`.  The converse is
immediate.  QED.

## 3. Closed dagger ideal and quotient

### Theorem 3.1

`R_W` is a closed two-sided convolution ideal stable under dagger.

### Proof

`R_partial` has these properties by P123.007.  Equations (1.2)--(1.3) show
that `D^0` is a closed dagger ideal.  Their intersection has the same
properties.  QED.

Define

```text
N_W^c=D/R_W.                                          (3.1)
```

Convolution and dagger descend continuously.  The vector pairing descends
and is nondegenerate by definition and Proposition 2.1.

## 4. One numerical object with a Tate boundary

The moment map descends to a surjection

```text
Mbar:N_W^c ->B_T.                                     (4.1)
```

Its kernel is the primitive mixed numerical sector

```text
N_W^prim=D^0/R_W.                                     (4.2)
```

Hence there is a canonical exact sequence

```text
0 ->N_W^prim ->N_W^c ->B_T ->0.                      (4.3)
```

The quotient `B_T`, with pairing (2.2), is the hyperbolic ruling plane and
dagger exchanges its basis directions.  Thus the rulings and primitive
mixed classes belong to one numerical object as boundary quotient and
kernel.  No noncanonical splitting and no formal direct sum is used.

External idele classes act compatibly on (4.3): on `B_T` they act by the
two characters `|u|^(-1/2),|u|^(1/2)` of P123.014, while on the kernel they
act by translated test correspondences.

## 5. A separating complete nuclear realization

Let `D'_b` be the strong distribution dual of the nuclear test LF space
`D`.  It is complete and nuclear.  Define

```text
J:N_W^c ->D'_b direct-sum B_T,
J([f])=(g |->I_partial(f,g), M(f)).                   (5.1)
```

Proposition 2.1 says that `J` is injective.  Put

```text
N_W^dist=closure(J(N_W^c)) in D'_b direct-sum B_T.    (5.2)
```

It is a closed subspace of a complete nuclear space, hence is complete and
nuclear.  Every element is a pair `(ell,m)`.  Its pairing against a test
class is

```text
I_vec((ell,m),g)=(ell(g), beta_T(m,M(g))).             (5.3)
```

If (5.3) vanishes for every `g`, then `ell=0`; surjectivity of `M` and
nondegeneracy of `beta_T` give `m=0`.  Therefore the completed realization
remains numerically separated against the dense test sector.  This removes
the unspecified “boundary radical” left in P123.007.

## 6. Operations on the completion

For `a in D`, convolution acts on (5.1) by

```text
(a dot ell_f)(g)=ell_f(a^dagger star g),
M(a star f)=M(a)M(f).                                 (6.1)
```

These formulas define a continuous `D`-module action on `N_W^dist` and
extend dagger by duality.  On the dense quotient `N_W^c`, this is exactly
the descended correspondence composition.

No product of two arbitrary elements of `D'_b` is defined in general.
Accordingly (5.2) is a complete **numerical module**, not falsely a
distribution algebra.  Composition of actual completed kernels continues
to live in the Fell carrier `L_S` of P123.015; its numerical realization
acts on (5.2).  This division is the same one used classically between a
correspondence category and its numerical representation.

## 7. Effectivity boundary

The source cone of P123.010 maps into `N_W^c`, and its closure maps into
`N_W^dist`.  It is functorial under the action (6.1).  However, proving that
the image cone remains proper requires excluding

```text
q(Eff) intersect -q(Eff) != {0}                       (7.1)
```

after numerical identification.  Neither vector-valued separation nor
source `C*`-positivity alone proves this, because the trace component is
not a positive `C*` trace.  A.7 therefore remains partial here.

## 8. A.6 conclusion

The numerical theory now has:

1. a source-defined closed numerical ideal;
2. continuous descended composition and dagger on test classes;
3. a nondegenerate vector-valued intersection target;
4. the primitive mixed sector and ruling plane in one exact sequence;
5. a complete nuclear, boundary-separated distributional realization;
6. continuous action by the completed geometric correspondence carrier.

This closes A.6 in the appropriate correspondence-module sense.  It does
not manufacture multiplication of arbitrary distributions, which is not a
requirement of numerical cycle theory.
