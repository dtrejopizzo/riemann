# P123.013 — internal gauge arrows versus external scaling

## Status

`PROVED-IN-REPOSITORY` distinction and no-go.

This note corrects an over-identification in P123.004--P123.010.  Those
constructions remain valid as algebraic/topological statements, but their
internal rational multipliers are not the external scaling
correspondences occurring in the semilocal trace.

## 1. The two groups

For a finite set of places `S`, the structure algebra is

```text
K_S=S(A_S) rtimes Gamma_S,
Gamma_S=Z_S^times.                                    (1.1)
```

Here `Gamma_S` is the group by which the additive space is quotiented.  Its
elements are arrows of the presentation groupoid

```text
Gamma_S acting on A_S.                                (1.2)
```

The scaling dynamics in the semilocal trace is instead

```text
C_(Q,S)=Gamma_S backslash A_S^times.                  (1.3)
```

It acts externally on the quotient `X_S=Gamma_S backslash A_S`.

## 2. Exact no-go

On

```text
H_S=L^2(Gamma_S backslash A_S)
```

the external scaling representation is

```text
(theta(u)xi)(a)=xi(u^-1 a).                           (2.1)
```

### Proposition 2.1

For every `gamma in Gamma_S`,

```text
theta(gamma)=identity.                                (2.2)
```

### Proof

A vector on the quotient satisfies `xi(gamma a)=xi(a)`.  Therefore

```text
(theta(gamma)xi)(a)=xi(gamma^-1 a)=xi(a).
```

QED.

### Corollary 2.2

There is no faithful realization which simultaneously:

1. interprets the internal multiplier `U_gamma` as the physical external
   scaling correspondence on `H_S`; and
2. distinguishes different `gamma in Gamma_S`.

Indeed (2.2) sends all of them to the identity.

## 3. Consequences for the preceding constructions

The exact status is:

* P123.005 remains a valid strict sheaf of rational **gauge-label**
  algebras;
* P123.006 remains a valid complete structure-kernel sheaf with composition,
  dagger and internal multipliers;
* P123.008 remains a valid hyperbolic representation of that label algebra,
  but it is a representation before quotient descent and cannot be called
  the external Tate realization of the physical scaling action;
* P123.009 remains valid place by place when its label is read as a local
  isotropy/scaling element `u in Q_v^times`, not as an internal global
  gauge arrow;
* P123.010 remains a valid source cone on the structure kernels;
* P123.007 and P123.012 concern the external test algebra and semilocal
  representation, and are unaffected after removing the claimed lift from
  internal rational multipliers.

No numerical identity proved in those notes is changed.  What changes is
the typing of the arrows.

## 4. Correct two-level carrier

The carrier required by A must contain both levels:

```text
internal structure:  Gamma_S acting on A_S
external dynamics:   C_(Q,S) acting on (Gamma_S backslash A_S).
```

Equivalently one needs the semidirect/bivariant groupoid

```text
(Gamma_S acting on A_S) semidirect C_(Q,S),           (4.1)
```

where an idele lift acts by multiplication on `A_S` and commutes with the
rational gauge action.  A different lift changes the external action by an
inner gauge arrow, so the induced bimodule depends only on the idele class.

This supplies the correct role of the internal multipliers: they implement
independence of the lift; they are not themselves the external
correspondence.

## 5. Required next construction

For `u in C_(Q,S)`, construct the `K_S`--`K_S` correspondence bimodule
`E_u` induced by the automorphism

```text
alpha_u(f)(x)=f(u^-1 x).                              (5.1)
```

and prove

```text
E_u tensor_(K_S) E_v ~=E_(uv),
E_u^dagger ~=E_(u^-1),
E_1 ~=K_S.                                            (5.2)
```

Then complete compactly supported smooth superpositions

```text
E_h=integral_(C_(Q,S)) h(u)E_u d^*u.                 (5.3)
```

The trace of `E_h` is the source operator `theta(h)` of P123.012.  This is
the missing common carrier connecting the structure sheaf to the external
trace-class algebra.

## 6. Ledger correction

Before P123.013 the live plan treated

```text
U_q in Mult(K_S)  =  external arithmetic correspondence.
```

That equality is retracted.  The correct relation is

```text
U_gamma: change of idele lift / internal gauge  [structure]
E_[u]:    external idele-class bimodule         [correspondence].
```

This correction prevents row B from collapsing all of its labels to the
identity on the semilocal quotient.  It also gives a concrete construction
target rather than another abstract comparison functor.

