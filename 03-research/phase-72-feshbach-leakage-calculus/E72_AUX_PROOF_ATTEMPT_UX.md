# E72 auxiliary proof attempt -- constructing the non-circular primitive `u_x`

**Date:** 2026-07-08.
**Scope:** Phase 72 only.
**Write constraint:** this file only.

## 0. Status

```text
result: proof conditional on one exact missing lemma.
closed: the abstract construction of the only admissible non-circular corrector.
open:   the arithmetic Prolate-Sonin Coboundary Lemma stated in §6.
```

I do **not** get an unconditional proof of the Phase 72 leakage estimate here. What I can do honestly is
reduce it to a first missing lemma that is sharper than the previous Phase 60/65 walls and does not use
the forbidden moves.

The candidate corrector is not

```text
u_x = C_x^{-1} b_x.
```

The only non-circular primitive that survives the audits is the **model-reduced primitive**

```text
u_x^0 := (C_x^0)^{-1} b_x,
```

where `C_x^0` is the explicit prolate/Dirichlet complement, not the actual arithmetic Feshbach
complement `C_x`. This uses the model Green operator, which is part of the archimedean/prolate
calculus, before solving the arithmetic Feshbach inverse.

The price is precise: one must prove that the arithmetic residual is a small coboundary for the model
complement and that replacing `C_x^0` by `C_x` is harmless on this one primitive.

## 1. Audit constraints used

The repository audit gives the following hard restrictions.

### From the prior Sonin/prolate history

- No PCN/local Christoffel evaluator.
- No claim that a Jacobi/Christoffel kernel localizes at a zeta zero.
- No `1/log gamma` Christoffel scale; the old correction says the relevant scale is `O(1)`.
- No full Weil-Sonine positivity as input.
- No semilocal uniformity in `S` unless constants are actually supplied.

### From the prior Feshbach/Schur history

- Feshbach shorting is valid, but it is a coordinate system, not a convergence proof.
- Do not expand the actual Feshbach inverse as a sum of local inverses.
- Do not use sourced Euler products for finite-rank sources.
- Do not identify the endpoint resolvent from the scalar determinant.
- Do not use row/column `l1` or absolute-value ceilings before cancellation.

### From Phase 60/63

The old shorted-Dirichlet quotient problem, Lemma `2.3.F`, was reduced to a uniform boundedness
statement for the intrinsic Jacobi coefficients. In zero-sum variables, the open part was the uniform
control of the oscillatory term `A_osc`. Therefore any Phase 72 proof that secretly gives full uniform
boundedness of `A_osc` has not escaped the old wall; it has only renamed it.

Phase 72 is valid only if it proves a **one-vector graph-norm coboundary**, not a global coefficient
bound.

## 2. Notation

Work on the primitive, pole-shorted finite/restricted Hilbert space. Let

```text
H_x     = actual pole-relative CCM/Weil operator,
H_x^0   = prolate/Dirichlet model operator,
R_x     = H_x - H_x^0,
k_x     = normalized prolate ground state,
P_x     = |k_x><k_x|,
Q_x     = I - P_x.
```

Let

```text
mu_x^0  = <k_x,H_x^0 k_x>,
a_x     = <k_x,R_x k_x>,
b_x     = Q_x R_x k_x.
```

The actual and model complements are

```text
C_x   := Q_x(H_x   - mu_x^0 - a_x)Q_x,
C_x^0 := Q_x(H_x^0 - mu_x^0)Q_x.
```

Then

```text
C_x = C_x^0 + V_x,
V_x = Q_x(R_x-a_x)Q_x.
```

Phase 72 needs

```text
||C_x^{-1} b_x|| -> 0.
```

Equivalently, it needs

```text
b_x = C_x u_x + r_x,
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0,
```

with `u_x` constructed before applying `C_x^{-1}` to `b_x`.

## 3. The model primitive

Define

```text
u_x^0 := (C_x^0)^{-1} b_x.                       (MP)
```

This is not the forbidden inverse. The inverse is that of the explicit prolate complement. In the
Dirichlet scaling limit, `(C_x^0)^{-1}` is the Green operator of the prolate/Dirichlet box on the
orthogonal complement of the ground line.

Using `C_x = C_x^0 + V_x`,

```text
b_x = C_x^0 u_x^0
    = C_x u_x^0 - V_x u_x^0.
```

Therefore the exact decomposition is

```text
b_x = C_x u_x^0 + r_x^0,
r_x^0 := -V_x u_x^0.                              (D)
```

So Phase 72 follows from the two estimates

```text
(M1)  ||u_x^0|| = ||(C_x^0)^{-1}b_x|| -> 0,
(M2)  ||C_x^{-1}V_xu_x^0|| -> 0.
```

This is the first clean non-circular reduction. It uses only the model inverse and the actual compressed
complement as a graph norm; it does not solve `C_xu=b_x`.

## 4. Theorem: model primitive closes Phase 72 under (M1)-(M2)

### Theorem 72.U

Assume the actual complement is positive and invertible on `Q_xH` and assume `(M1)` and `(M2)`. Then

```text
||C_x^{-1}b_x|| -> 0.
```

Consequently the reduced Feshbach theorem E72.3 gives

```text
theta_x -> k_x,
```

and the Phase 71 stable-divisor bridge applies.

### Proof

From (D),

```text
C_x^{-1}b_x = u_x^0 + C_x^{-1}r_x^0
            = u_x^0 - C_x^{-1}V_xu_x^0.
```

Taking norms gives

```text
||C_x^{-1}b_x||
  <= ||u_x^0|| + ||C_x^{-1}V_xu_x^0||.
```

The right hand side tends to zero by `(M1)` and `(M2)`. Then E72.3 applies. `QED`

This theorem is elementary but important: it identifies the only place where new arithmetic must enter.

## 5. Why (M1)-(M2) are not enough unless made structural

As written, `(M1)` is the model-reduced leakage estimate

```text
||(C_x^0)^{-1}Q_xR_xk_x|| -> 0.
```

This is weaker than the forbidden actual reduced leakage only if it can be proved from the explicit
prolate/Sonin calculus, not by comparison with `C_x^{-1}` or by endpoint identification.

The safe way to prove `(M1)` is not to estimate coefficients absolutely. It is to prove a variational
identity

```text
<v,b_x> = <C_x^0 v, w_x> + eps_x(v),              (IBP0)
```

where `w_x` is an explicit boundary primitive and

```text
||w_x|| -> 0,
sup_v |eps_x(v)|/||C_x^0 v|| -> 0.
```

Then by the dual identity for `C_x^0`,

```text
||(C_x^0)^{-1}b_x||
  <= ||w_x|| + sup_v |eps_x(v)|/||C_x^0 v||
  -> 0.
```

This supplies `u_x^0 = w_x + o(1)` in a model graph sense, without defining `w_x` by inversion.

The safe way to prove `(M2)` is a one-vector relative graph estimate:

```text
||C_x^{-1}V_x w_x|| -> 0
```

and the same estimate for the model-small error term. This asks only about the explicit primitive
`w_x`, not about all vectors in the complement.

## 6. The first exact missing lemma

The honest load-bearing statement is therefore the following.

### Lemma PSC -- Pole-relative Prolate-Sonin Coboundary Lemma

There exists an explicit family of primitive complement vectors `w_x`, built from

```text
k_x,
P_x,Q_x,
the pole-shortened prolate boundary calculus,
and the explicit action of R_x=H_x-H_x^0 on k_x,
```

but **not** from `C_x^{-1}`, endpoint resolvents, zero divisors, sourced Euler products, or local
Christoffel evaluators, such that for all primitive complement test vectors `v`,

```text
<v,b_x> = <C_x^0 v,w_x> + eps_x(v),               (PSC1)
```

with

```text
||w_x|| -> 0,                                     (PSC2)
sup_{v != 0} |eps_x(v)|/||C_x^0 v|| -> 0,         (PSC3)
```

and the one-vector replacement of the model graph by the actual Feshbach graph holds:

```text
||C_x^{-1}V_xw_x|| -> 0,                          (PSC4)
```

plus the same replacement for the error primitive representing `eps_x`.

Then Phase 72 closes.

### Proof that PSC closes Phase 72

By `(PSC1)-(PSC3)` and the model dual identity,

```text
||(C_x^0)^{-1}b_x|| -> 0.
```

Let

```text
u_x^0 := (C_x^0)^{-1}b_x.
```

The same argument gives `u_x^0 = w_x + e_x` with `||e_x|| -> 0` and with `e_x` model-reduced-small.
By `(PSC4)` and its error version,

```text
||C_x^{-1}V_xu_x^0|| <= ||C_x^{-1}V_xw_x|| + ||C_x^{-1}V_xe_x|| -> 0.
```

Thus `(M1)-(M2)` hold, and Theorem 72.U yields

```text
||C_x^{-1}b_x|| -> 0.
```

`QED`

## 7. What would `w_x` have to look like?

In the prolate/Dirichlet scaling, `C_x^0` is a second-order positive operator on the complement. The
identity `(PSC1)` is therefore an integration-by-parts statement. Schematically, if `theta` is the
prolate coordinate and `L_x^0` is the Dirichlet limit of `C_x^0`, then

```text
<v,b_x>
  = integral v(theta) * Force_x(theta) dtheta
```

must be rewritten as

```text
integral (L_x^0 v)(theta) * w_x(theta) dtheta + boundary/error.
```

The primitive `w_x` should be a pole-shortened solution of the **model** homological equation

```text
L_x^0 w_x = Force_x
```

with the boundary/pole component removed by the Sonin condition. This is allowed because `L_x^0` is the
explicit prolate/Dirichlet operator. It is not allowed to replace `L_x^0` by the unknown actual
`C_x`.

The expected mechanism is:

```text
prime force on k_x = total prolate derivative + pole boundary term + high-frequency tail,
pole boundary term is killed by the existing shorting,
total derivative transfers to C_x^0 v,
tail is small in the C_x^0 graph dual.
```

This is a genuine new mathematical identity. It is not present in the old Sonin documents.

## 8. Why the old prolate attempts do not prove PSC

The old prolate/Sonin route compared full quadratic forms and tried to get the `(k+1)^2` ladder or
uniform Jacobi boundedness. That was too global. PSC is one-vector and graph-dual:

```text
old target: control the whole shorted Dirichlet quotient / all Jacobi coefficients.
new target: control <v,R_xk_x> modulo C_x^0 integration by parts.
```

However, PSC would still be false if its proof required any of the following:

- a bound on `sup_lambda ||A_osc_lambda||`;
- localization of a Jacobi kernel at `gamma_n`;
- an additive Green expansion;
- absolute summation of prime cells;
- endpoint identification with `G_Xi`.

If PSC collapses to one of those, it is not a new route.

## 9. Relation to Lemma 2.3.F

PSC is strictly targeted below Lemma `2.3.F` only if it remains a one-vector estimate.

If one strengthens PSC from the single source `b_x=Q_xR_xk_x` to a uniform statement for every source in
a full complement ball, then it implies the old uniform boundedness of the intrinsic Jacobi/oscillatory
part. That is exactly Lemma `2.3.F`/L1 and inherits the old wall.

So the boundary is:

```text
one-vector PSC: potentially new.
uniform-source PSC: old wall.
```

The next proof attempt must keep this distinction visible.

## 10. Kill tests for PSC

PSC fails as a new proof if:

```text
K1. w_x is defined as C_x^{-1}b_x.
K2. w_x is obtained from the endpoint Xi resolvent.
K3. eps_x is bounded by sum |prime cell|.
K4. C_x^{-1} is expanded over prime/local inverses.
K5. the proof needs uniform boundedness of A_osc on all complement sources.
K6. the proof needs PCN/local Christoffel localization.
```

PSC survives the old audits only if all six are avoided.

## 11. Final verdict

The proof is **not closed**. The abstract Feshbach part is closed, and the correct non-circular
primitive is isolated:

```text
u_x^0 = (C_x^0)^{-1}Q_x(H_x-H_x^0)k_x,
```

or, better, its explicit integration-by-parts representative `w_x`.

The exact missing lemma is PSC:

```text
<v,Q_x(H_x-H_x^0)k_x>
  = <C_x^0v,w_x> + eps_x(v),
||w_x|| -> 0,
||eps_x||_{(C_x^0)^*} -> 0,
||C_x^{-1}(C_x-C_x^0)w_x|| -> 0.
```

This is the first lemma to attack. It is narrower than the previous Feshbach/Green endpoint wall and
narrower than the old prolate uniform-boundedness wall, but it is still genuine new arithmetic. I cannot
honestly replace it by an unconditional proof from the material currently in the repository.
