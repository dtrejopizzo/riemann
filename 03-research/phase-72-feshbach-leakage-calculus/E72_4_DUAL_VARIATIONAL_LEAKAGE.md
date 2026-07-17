# E72.4 -- Dual variational form of reduced leakage

**Date:** 2026-07-08.
**Role:** convert the reduced leakage target of E72.3 into an exact dual variational estimate, suitable
for a Sonin/Feshbach integration-by-parts proof.

## 0. Why this document exists

E72.3 changed the missing estimate from raw leakage

```text
||Q_x R_x k_x|| / g_x -> 0
```

to reduced leakage

```text
||C_x^{-1} Q_x R_x k_x|| -> 0.
```

This document rewrites that condition without diagonalizing `C_x` and without localizing Christoffel
kernels. It shows that the exact object to prove is a first-variation estimate against the **strong
complement norm**

```text
v |-> ||C_x v||.
```

That is the right analytic slot for the new Sonin identity.

## 1. Abstract dual identity

Let `C` be a positive self-adjoint invertible operator on `QH`, and let `b in QH`. Then

```text
||C^{-1}b||
  = sup_{v in Dom(C), Cv != 0} |<v,b>| / ||C v||.          (D)
```

### Proof

Set `w=Cv`. Since `C` is invertible on `QH`, `w` ranges over the range of `C`, dense in `QH` in the
finite/restricted CCM models and in the graph closure in the limiting model. Then

```text
<v,b> = <C^{-1}w,b> = <w,C^{-1}b>.
```

Therefore

```text
sup_{Cv != 0} |<v,b>|/||Cv||
 = sup_{w != 0} |<w,C^{-1}b>|/||w||
 = ||C^{-1}b||.
```

`QED`

## 2. Application to Phase 72

With

```text
b_x = Q_x(H_x-H_x^0)k_x,
C_x = Q_x(H_x-mu_x^0-a_x)Q_x,
```

the reduced leakage condition is exactly

```text
sup_{v in Q_xH, C_x v != 0}
   |<v,(H_x-H_x^0)k_x>| / ||C_x v||
      -> 0.                                      (RL-dual)
```

This is a strict improvement over the raw estimate, which would require the same numerator to be small
against `||v||`.

The denominator `||C_x v||` allows high complement oscillation. Therefore the proof may integrate by
parts and move derivatives/finite-difference weight onto `v`; the resulting strong norm is precisely
what absorbs high modes.

## 3. The correct Sonin/Feshbach integration-by-parts target

The desired arithmetic identity should not be written as a pointwise formula for the coefficients

```text
<e_{x,j},(H_x-H_x^0)k_x>.
```

It should be written as a variational identity:

```text
<v,(H_x-H_x^0)k_x>
   = B_x(C_x v) + E_x(v),                         (IBP)
```

where

```text
||B_x||_{(Q_xH)^*} -> 0,
sup_{v != 0} |E_x(v)|/||C_x v|| -> 0.
```

Then (RL-dual) follows immediately.

Equivalently, by Riesz representation, (IBP) is the same as the coboundary form of E72.3:

```text
Q_x(H_x-H_x^0)k_x = C_x u_x + r_x,
```

with

```text
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0.
```

## 4. Why this avoids the old failures

The old Phase 32 Sonin/Jacobi route asked for a local formula of the kind

```text
L_n[f] approx f(gamma_n).
```

That failed because the Christoffel kernel is not localized at zeta-zero scale.

The new identity asks for something different:

```text
<v, residual ground force> is small after measuring v in the C_x-graph norm.
```

No zeta zero is singled out. No individual Jacobi kernel is interpreted as a Poisson kernel. The
cancellation is global in the complement and only measured after the Feshbach inverse has selected the
part capable of moving the ground vector.

This also avoids the Phase 65 Green-additivity trap. We do not claim

```text
(A+B-z)^(-1) = (A-z)^(-1)+(B-z)^(-1).
```

The operator `C_x` is the actual compressed complement after pole-relative shorting. All cross terms are
inside `C_x`; the estimate is made only after that non-additive inverse has been accepted.

## 5. A practical proof template

A proof of Phase 72 should now have the following shape.

### Step 1 -- identify the actual complement norm

Work with

```text
||v||_{F,x} := ||C_x v||.
```

This is the Feshbach graph norm, not the ambient Hilbert norm and not the prolate model norm.

### Step 2 -- compute the first variation

For primitive complement tests `v`,

```text
F_x(v) := <v,(H_x-H_x^0)k_x>.
```

This is the exact residual force on the prolate ground line.

### Step 3 -- prove a projected integration-by-parts formula

Show

```text
F_x(v) = B_x(C_xv) + E_x(v),
```

where `B_x` is represented by a vector `u_x` with `||u_x||->0`, and `E_x` is small in the dual
`C_x`-graph norm.

### Step 4 -- conclude by E72.3

By the dual identity,

```text
||C_x^{-1}Q_x(H_x-H_x^0)k_x|| -> 0.
```

Then Theorem 72.3 gives

```text
theta_x -> k_x.
```

Combined with E71.16/E71.17, this gives stable-divisor convergence to `Xi`.

## 6. The exact mathematical statement to prove next

The new load-bearing statement is:

### Arithmetic Feshbach--Sonin Variational Lemma

For the actual CCM pole-relative operator `H_x`, the prolate model `H_x^0`, and Connes's vector
`k_x=k_lambda`, the functional

```text
F_x(v)=<v,(H_x-H_x^0)k_x>
```

on the primitive complement satisfies

```text
||F_x||_{(Dom C_x, ||C_x .||)^*} -> 0.
```

Equivalently,

```text
||C_x^{-1}Q_x(H_x-H_x^0)k_x|| -> 0.
```

This is now the precise missing pure-mathematical identity.

## 7. Falsifier

The falsifier is equally precise. For Davenport--Heilbronn or planted off-line data, compute the same
functional in the same graph norm. The control should fail:

```text
liminf ||F_x||_{(Dom C_x, ||C_x .||)^*} > 0,
```

or the complement lower bound for `C_x` should fail.

If the dual norm tends to zero for a planted off-line control, then Phase 72 is too weak and does not
detect RH.

## 8. Status

```text
proved:   reduced leakage = exact dual graph-norm first variation;
new:      the proof target is a variational Feshbach-Sonin identity, not coefficient localization;
open:     prove the arithmetic Feshbach-Sonin Variational Lemma for CCM data.
```

