# E77.7z - Fixed-section Schur eta-limit reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7y identified the correct singular candidate:

```text
INTRINSIC-SCHUR-ETA-LIMIT.
```

Before chasing a global theorem, this note reduces the fixed finite-section
`eta -> 0` problem to a single scalar coupling condition inside the `2x2`
Schur block.

## 2. Setup

For a fixed finite section and safe point `z`,

```text
T_eta(z) = t0(z) - tau(z) (Sigma - i eta I)^(-1) kappa,      (Z-1)
Pi_eta(z) = T_eta(z) / T_eta(z0).                             (Z-2)
```

Here `Sigma` is the intrinsic `2x2` Hermitian Schur block from P76.049 /
E77.5f, while `kappa`, `tau(z)`, and `t0(z)` are the coupled source / row /
scalar data.

The finite singular question is:

```text
does Pi_eta(z) admit a limit as eta -> 0 ?
```

## 3. Exact rank split

Because `Sigma` is Hermitian `2x2`, there are only two cases.

### Case A: `det Sigma != 0`

Then `Sigma` is invertible and

```text
(Sigma - i eta I)^(-1) -> Sigma^(-1)
```

entrywise. Therefore

```text
T_eta(z) -> T_0(z) = t0(z) - tau(z) Sigma^(-1) kappa,
```

and `Pi_eta(z) -> T_0(z)/T_0(z0)` provided `T_0(z0) != 0`.

So the nonsingular case is automatic once the anchor is nonzero.

### Case B: `rank Sigma = 1`

Let `u0` be a unit kernel vector of `Sigma` and `P0 = u0 u0^*` the kernel
projector. Let `P1 = I - P0`. On `Ran(P1)`, `Sigma` is invertible. Hence

```text
(Sigma - i eta I)^(-1)
= (-i eta)^(-1) P0 + (Sigma|Ran(P1) - i eta I)^(-1) P1.      (Z-3)
```

Applying `(Z-3)` to `kappa` gives

```text
v_eta
= (-i eta)^(-1) <u0,kappa> u0 + v_reg(eta),                  (Z-4)
```

with `v_reg(eta)` bounded as `eta -> 0`.

Substituting into `(Z-1)`:

```text
T_eta(z)
= (-i eta)^(-1) A(z) + B_eta(z),                             (Z-5)
```

where

```text
A(z) = - <u0,kappa> tau(z) u0,                               (Z-6)
```

and `B_eta(z)` remains bounded as `eta -> 0`.

## 4. The only genuinely singular subcase

Equation `(Z-5)` shows that the fixed-section limit problem has only one
genuinely singular branch.

### Branch B1: `A(z0) != 0`

Then both numerator and denominator of `Pi_eta(z)` share the same simple
`1/eta` blow-up, so the ratio has a finite limit:

```text
Pi_eta(z) -> A(z) / A(z0).                                   (Z-7)
```

This limit depends only on the kernel coupling data `(u0, kappa, tau)`.

### Branch B2: `A(z0) = 0`

Then the pole does not appear in the anchor. The denominator is governed by
the bounded remainder `B_eta(z0)`, so existence of the limit is no longer
automatic. This is the only branch where theorem-grade work remains.

So the fixed-section singular problem reduces exactly to:

```text
KERNEL-ANCHOR-COUPLING:
if rank Sigma = 1, prove A(z0) != 0
or else analyze the bounded remainder branch explicitly.
```

## 5. Consequence for the live object

E77.7y already observed numerically that the shifted intrinsic profile is
stable in both builds. The algebra above explains why that is plausible:

```text
either Sigma is invertible,
or the singular piece is one-dimensional and projective cancellation is
automatic once the anchor couples to that kernel direction.
```

Therefore the live singular theorem is smaller than “control all resonant
directions.”  At fixed section it is enough to prove:

```text
FIXED-SECTION-KERNEL-ANCHOR:
the anchor T_eta(z0) sees the kernel part of Sigma whenever Sigma is singular.
```

Then `(Z-7)` gives the finite-section `eta`-limit automatically.

## 6. Relation to the chain

This reduction yields the admissible implication

```text
FIXED-SECTION-KERNEL-ANCHOR
=> INTRINSIC-SCHUR-ETA-LIMIT at fixed section
=> singular-section clause for PROJECTIVE-MU-TRANSFER.
```

This is a legitimate reduced target under the E77.6 admissibility rule,
because the implication is explicit and finite.

## 7. Status

```text
proved:    fixed-section eta-limit is automatic in the invertible Schur case;
proved:    in the singular rank-one case, the only obstruction is loss of the
           kernel pole in the anchor;
refined:   the live finite singular target is FIXED-SECTION-KERNEL-ANCHOR;
next:      measure / prove the anchor coupling A(z0) = -<u0,kappa> tau(z0)u0
           on the finite sections and transport that statement into the LP
           bridge.
```
