# E77.7ac - Bordered singularity reduction of kernel blindness

**Run:** 2026-07-18.

## 1. Purpose

E77.7ab reduced the finite singular target to

```text
KERNEL-DOUBLE-COUPLING:
for every nonzero kernel vector v0 of the shifted inner block A,

  v0^T g != 0,
  r(z0)v0 != 0.
```

This note shows that either failure is exactly a bordered singularity of the
square anchor matrix.  So the blindness question is equivalent to an
invertibility question for one finite bordered system.

## 2. The shifted bordered matrix

At the fixed anchor `z0`, define the square bordered matrix

```text
M(z0) =
[ A      g ]
[ r(z0)  c0 ],                                      (AC-1)
```

where

```text
A = H_inner - mu I,
g = right boundary coupling column,
r(z0) = safe Cauchy row on the inner nodes,
c0 = 1/(z0-d_b).
```

This is the shifted analogue of the finite bordered matrices from P76.051 /
P76.054, with the interior block now centered at the moving finite spectral
point `mu`.

## 3. Anchor blindness gives a right kernel

Assume `v0 != 0` satisfies

```text
Av0 = 0,
r(z0)v0 = 0.                                         (AC-2)
```

Then

```text
M(z0) [v0; 0]
= [Av0; r(z0)v0]
= 0.                                                 (AC-3)
```

So any anchor-blind inner kernel vector makes the bordered matrix singular.

## 4. Source blindness gives a left kernel

Assume `v0 != 0` satisfies

```text
Av0 = 0,
v0^T g = 0.                                          (AC-4)
```

Since `A` is symmetric/Hermitian in the finite CCM sections,

```text
[v0^T, 0] M(z0)
= [v0^T A, v0^T g]
= 0.                                                 (AC-5)
```

So any source-blind inner kernel vector also makes the same bordered matrix
singular.

Therefore:

```text
if M(z0) is invertible,
then every nonzero kernel vector of A is seen both by g and by r(z0).      (AC-6)
```

This yields the exact implication

```text
BORDERED-ANCHOR-INVERTIBILITY
=> KERNEL-DOUBLE-COUPLING
=> FIXED-SECTION-KERNEL-ANCHOR-THEOREM.             (AC-7)
```

## 5. Why this is the right reduction

The new target is stronger than needed but much more canonical.

It no longer mentions:

```text
Sigma,
kappa,
tau,
u0.
```

Instead it asks for one finite statement about the same square bordered
object that already underlies P76.051--P76.054:

```text
the anchor-bordered system remains invertible even when the interior block A
develops a kernel.
```

That is precisely the geometry suggested by E77.7aa: the singularity of the
inner block is resolved projectively by the border.

## 6. What is still open

This note does **not** prove `M(z0)` invertible.  It only identifies the
exact obstruction:

```text
M(z0) singular
<=> some nonzero inner kernel vector is blind to the source or the anchor.
```

The next theorem target can therefore be stated cleanly as:

```text
FIXED-SECTION-BORDERED-ANCHOR-INVERTIBILITY:
the shifted bordered matrix M(z0) is invertible on every finite section.
```

Then `(AC-7)` closes the singular fixed-section clause.

## 7. Status

```text
proved:    anchor blindness produces a right kernel of the bordered matrix;
proved:    source blindness produces a left kernel of the same bordered
           matrix;
refined:   the live singular target is bordered-anchor invertibility;
next:      compare M(z0) with the finite bordered matrices of P76.051--P76.054
           and decide whether invertibility is already encoded there or needs
           an independent argument/autopsy.
```
