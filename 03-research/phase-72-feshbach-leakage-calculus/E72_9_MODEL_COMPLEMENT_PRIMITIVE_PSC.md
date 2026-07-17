# E72.9 -- Model-complement primitive and the PSC lemma

**Date:** 2026-07-08.
**Role:** integrate the parallel audit/proof attempt and isolate the first non-circular lemma that
would close Phase 72.

## 0. Outcome of the parallel work

Two parallel checks were run:

1. a repository audit searched for prior `prolate/Sonin/Feshbach/Schur/shorting/graph norm`
   attempts;
2. a proof attempt tried to construct the primitive `u_x` without defining it as `C_x^{-1}b_x`.

The audit confirmed:

```text
Phase 72 is new only if it stays one-vector and variational in the actual C_x graph norm.
```

The proof attempt found the strongest non-circular primitive currently available:

```text
u_x^0 := (C_x^0)^{-1}b_x,
```

where `C_x^0` is the **model prolate/Dirichlet complement**, not the actual arithmetic complement
`C_x`.

This does not close the proof by itself, but it removes the tautology `u_x=C_x^{-1}b_x` and creates a
precise perturbative target.

## 1. Setup

On the primitive pole-shorted finite/restricted space, write

```text
H_x     = actual pole-relative CCM/Weil operator,
H_x^0   = prolate/Dirichlet model operator,
R_x     = H_x - H_x^0,
k_x     = k_lambda,
P_x     = |k_x><k_x|,
Q_x     = I-P_x.
```

Set

```text
mu_x^0  = <k_x,H_x^0 k_x>,
a_x     = <k_x,R_x k_x>,
b_x     = Q_x R_x k_x.
```

The actual and model complement operators are

```text
C_x   := Q_x(H_x   - mu_x^0 - a_x)Q_x,
C_x^0 := Q_x(H_x^0 - mu_x^0)Q_x.
```

Then

```text
C_x = C_x^0 + V_x,
V_x = Q_x(R_x-a_x)Q_x.
```

Phase 72 needs:

```text
||C_x^{-1}b_x|| -> 0.
```

## 2. The model primitive

Define

```text
u_x^0 := (C_x^0)^{-1}b_x.                       (MP)
```

This is allowed only if `(C_x^0)^{-1}` is the explicit model/prolate Green operator. It is not the
forbidden actual inverse `C_x^{-1}`.

Since

```text
b_x = C_x^0 u_x^0
    = C_x u_x^0 - V_x u_x^0,
```

we have the exact actual-complement decomposition

```text
b_x = C_x u_x^0 + r_x^0,
r_x^0 := -V_x u_x^0.                             (D)
```

Therefore `u_x^0` closes Phase 72 if:

```text
(M1)  ||u_x^0|| -> 0,
(M2)  ||C_x^{-1}V_xu_x^0|| -> 0.
```

## 3. Theorem 72.9 -- model primitive criterion

Assume the actual complement is invertible on `Q_xH` and that `(M1)` and `(M2)` hold. Then

```text
||C_x^{-1}b_x|| -> 0.
```

Consequently, by E72.3,

```text
theta_x -> k_x.
```

Combined with E71.16/E71.17, the stable CCM divisor converges to the divisor of `Xi`.

### Proof

From (D),

```text
C_x^{-1}b_x
  = u_x^0 - C_x^{-1}V_xu_x^0.
```

Thus

```text
||C_x^{-1}b_x||
 <= ||u_x^0|| + ||C_x^{-1}V_xu_x^0|| -> 0
```

by `(M1)` and `(M2)`. E72.3 gives `theta_x -> k_x`; E71.16/E71.17 give stable-divisor convergence.
`QED`

## 4. Why `(M1)` is still not a proof

As written,

```text
u_x^0 = (C_x^0)^{-1}b_x
```

is allowed only as an intermediate description. A non-circular proof must construct an explicit
representative `w_x` of this model primitive by integration by parts.

The target identity is:

```text
<v,b_x> = <C_x^0 v,w_x> + eps_x(v),              (PSC1)
```

with

```text
||w_x|| -> 0,                                    (PSC2)
sup_{v != 0} |eps_x(v)|/||C_x^0 v|| -> 0.        (PSC3)
```

Then the model dual identity gives

```text
||(C_x^0)^{-1}b_x|| -> 0.
```

The replacement from model graph to actual Feshbach graph is:

```text
||C_x^{-1}V_xw_x|| -> 0,                         (PSC4)
```

plus the same estimate for the small error primitive represented by `eps_x`.

## 5. Lemma PSC -- Pole-relative Prolate-Sonin Coboundary

The exact missing lemma is:

### Lemma PSC

There exists an explicit family `w_x` of primitive complement vectors, built from:

```text
k_x,
P_x,Q_x,
the pole-shorted prolate/Sonin boundary calculus,
and the explicit action of R_x=H_x-H_x^0 on k_x,
```

but not from:

```text
C_x^{-1},
the endpoint Xi resolvent,
zero divisors,
sourced Euler products,
local Christoffel evaluators,
or additive Green assembly,
```

such that `(PSC1)`, `(PSC2)`, `(PSC3)`, and `(PSC4)` hold.

Then Phase 72 closes.

### Proof that PSC closes Phase 72

By `(PSC1)-(PSC3)`,

```text
||(C_x^0)^{-1}b_x|| -> 0.
```

Moreover the primitive `u_x^0` differs from `w_x` by a model-reduced-small error. Applying `(PSC4)` to
`w_x` and the error primitive gives:

```text
||C_x^{-1}V_xu_x^0|| -> 0.
```

Thus `(M1)-(M2)` hold, so Theorem 72.9 gives reduced leakage. `QED`

## 6. What `w_x` would have to look like

In the prolate/Dirichlet scaling, `C_x^0` is a second-order positive model operator on the complement.
Thus `(PSC1)` is a model integration-by-parts identity.

Schematically:

```text
<v,b_x>
  = integral v(theta) Force_x(theta) dtheta
```

must be rewritten as

```text
integral (C_x^0 v)(theta) w_x(theta) dtheta + eps_x(v).
```

The expected mechanism is:

```text
prime force on k_x
  = model total derivative
    + pole boundary term
    + reduced-small high-frequency tail;

pole boundary term is killed by Feshbach shorting;
model total derivative transfers to C_x^0 v;
tail is small in the model graph dual and then in the actual reduced graph on w_x.
```

This is the first concrete mathematical place where the new proof can live.

## 7. Relation to older walls

PSC is new only while it remains **one-vector**.

If PSC is strengthened to all sources in a complement ball, it becomes the old uniform boundedness of
the intrinsic Jacobi/oscillatory term:

```text
uniform-source PSC = Lemma 2.3.F/L1 wall.
```

So the boundary is:

```text
one-vector PSC: potentially new;
uniform-source PSC: old wall.
```

## 8. Kill tests

PSC fails as a new route if:

```text
K1. w_x is defined as C_x^{-1}b_x.
K2. w_x is obtained from the endpoint Xi resolvent.
K3. eps_x is bounded by sum |prime cell|.
K4. C_x^{-1} is expanded over prime/local inverses.
K5. the proof needs uniform boundedness of A_osc on all complement sources.
K6. the proof needs PCN/local Christoffel localization.
K7. model Dirichlet/prolate constant-coefficient identification is asserted after prior refutations.
```

## 9. Status

```text
proved:   model primitive criterion (Theorem 72.9);
proved:   PSC => reduced leakage => theta_x -> k_x => stable divisor convergence;
open:     PSC itself, the one-vector pole-relative Prolate-Sonin coboundary lemma.
```

This is the furthest honest closure currently available. It does not prove RH, but it isolates the first
missing lemma sharply enough to attack or falsify.
