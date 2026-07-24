# E77.7ab - Kernel coupling reduction of the Schur anchor

**Run:** 2026-07-18.

## 1. Purpose

E77.7aa left the finite singular target at

```text
FIXED-SECTION-KERNEL-ANCHOR-THEOREM:
if Sigma is singular, then A(z0) = -<u0,kappa> tau(z0)u0 != 0.
```

This note rewrites that scalar entirely in terms of an actual kernel vector
of the shifted inner block.  The result is an exact reduction from the Schur
statement to a two-functional non-blindness statement.

## 2. Schur kernel lifts to an inner kernel vector

Write the shifted inner block in shell/core form:

```text
A =
[ C   U^T ]
[ U   A0  ].
```

Assume `A0` is invertible and `Sigma = C - U^T A0^{-1} U` is singular.
Let `u0 != 0` satisfy

```text
Sigma u0 = 0.                                            (AB-1)
```

Define the lifted vector

```text
v0 =
[ u0 ]
[ -A0^{-1} U u0 ].                                       (AB-2)
```

Then `v0` is a nonzero kernel vector of the full inner block `A`.

Indeed, the lower block gives

```text
U u0 + A0(-A0^{-1}Uu0) = 0,
```

while the upper block gives

```text
C u0 + U^T(-A0^{-1}Uu0)
= (C - U^T A0^{-1}U)u0
= Sigma u0
= 0.
```

So:

```text
Sigma singular  =>  Av0 = 0.                             (AB-3)
```

## 3. The Schur coupling factors are lifted row/source pairings

Split the boundary source and Cauchy row compatibly:

```text
g = [g_shell; g_core],
r(z) = [r_shell(z), r_core(z)].
```

Using

```text
kappa = g_shell - U^T A0^{-1} g_core,
tau(z) = r_shell(z) - r_core(z) A0^{-1} U,
```

we obtain the exact identities

```text
u0^T kappa
= u0^T g_shell - u0^T U^T A0^{-1} g_core
= [u0^T, -u0^T U^T A0^{-1}] g
= v0^T g,                                                (AB-4)
```

and

```text
tau(z)u0
= r_shell(z)u0 - r_core(z) A0^{-1} Uu0
= r(z) v0.                                               (AB-5)
```

Therefore the singular Schur anchor scalar is exactly

```text
A(z)
= -(u0^T kappa)(tau(z)u0)
= -(v0^T g)(r(z)v0).                                     (AB-6)
```

So the Schur theorem target is equivalent to saying:

```text
the lifted kernel vector v0 is seen both by the source g and by the anchor
Cauchy row r(z0).
```

## 4. Exact reduced target

Equation `(AB-6)` gives the admissible implication

```text
KERNEL-DOUBLE-COUPLING:
every lifted kernel vector v0 of the singular shell Schur block satisfies

  v0^T g != 0
  and
  r(z0)v0 != 0

=> FIXED-SECTION-KERNEL-ANCHOR-THEOREM.
```

This is strictly smaller than the old target because it removes the Schur
intermediates `kappa` and `tau` and speaks directly about the kernel vector
of the full shifted inner block.

## 5. Reading

The reduction is structurally important for two reasons.

First, it aligns the singular finite-section question with the Phase 76 / 77
bordered Weyl viewpoint: `g` is the canonical source and `r(z0)` is exactly
the normalizing safe row.

Second, it isolates the only way the theorem could fail:

```text
there would have to exist a nonzero inner kernel vector that is blind to the
source or blind to the anchor row.
```

That is a far more concrete obstruction than “Schur eta instability.”

## 6. Consequence for the chain

The singular LP-interface chain can now be sharpened once more:

```text
KERNEL-DOUBLE-COUPLING
=> FIXED-SECTION-KERNEL-ANCHOR-THEOREM
=> INTRINSIC-SCHUR-ETA-LIMIT at fixed section
=> singular-section clause for PROJECTIVE-MU-TRANSFER.
```

This implication is exact and admissible under the E77.6 reduced-target rule.

## 7. Status

```text
proved:    singular Schur directions lift exactly to kernel vectors of the
           full shifted inner block;
proved:    the scalar A(z) factors as -(v0^T g)(r(z)v0);
refined:   the live singular theorem target is KERNEL-DOUBLE-COUPLING;
next:      prove or autopsy the impossibility of a kernel vector blind to g
           or to the anchor row r(z0).
```
