# E77.7u - Spectral Feshbach equivalence

**Run:** 2026-07-18.

## 1. Purpose

E77.7t reduced the singular-section front to

```text
MATRIX-FESHBACH-RESONANT-BLOCK.
```

Before launching another numerical search, one structural point should be
fixed: if the resonant block is chosen as a **spectral** subspace of
`A_N(mu_ref)`, then the corresponding Feshbach block is not a genuinely new
object.  It is exactly the mode-subtraction family already audited in
E77.7q--s.

This note records that equivalence and sharpens the next admissible target.

## 2. Spectral-block identity

Let

```text
A = A_N(mu_ref),
R_eta = (A - i eta I)^(-1),
```

and let `P` be the orthogonal projector onto any spectral subspace of `A`
(for example, one mode, the lowest three modes, or any eta-window of
eigenmodes).  Put `Q = I - P`.

Since `P` is spectral,

```text
PA = AP,
QA = AQ,
P Q = 0.
```

Therefore the resolvent is block diagonal with respect to `P + Q`:

```text
R_eta = P R_eta P + Q R_eta Q.                  (U-1)
```

No off-diagonal Feshbach coupling survives, because the Schur complement
between `P` and `Q` is trivial:

```text
P(A-i eta I)Q = 0 = Q(A-i eta I)P.
```

Applied to the boundary source `b_N`,

```text
R_eta b_N
 = P R_eta b_N + Q R_eta b_N.                  (U-2)
```

In an eigenbasis of `A`, `(U-2)` is exactly the sum over the selected
eigenmodes plus the complementary remainder.

So every spectral Feshbach block equals a mode-subtraction rule.

## 3. Consequence for the recent autopsies

This means:

```text
one-mode subtraction            [E77.7q]
fixed 3-mode block             [E77.7r]
eta-adaptive spectral window   [E77.7s]
```

already cover the entire class of **spectral** Feshbach blocks.

The failures observed there are not accidents of implementation.  They show
that no reduction based only on a spectral projector `P_res(A)` can solve the
zeta singular-section problem.

In particular:

```text
MATRIX-FESHBACH-RESONANT-BLOCK on a spectral subspace
```

is not a smaller live object.  It is a renamed member of a class already
refuted numerically.

## 4. What must be genuinely new

A genuinely new matrix block must therefore be **non-spectral**.  It has to
mix the near-null directions using the boundary data before the projection is
fixed.

The natural candidates are subspaces generated from the coupled finite Schur
objects already present in the ledger:

```text
boundary source b_N,
safe Cauchy row r_z or r_{z0},
shell Schur vectors kappa, tau,
or a low-dimensional Krylov/Feshbach space built from these.
```

Only then can the resonant block retain the internal coupling that scalar or
spectral selections destroy.

## 5. Smaller live object

The next admissible target is therefore:

```text
NONSPECTRAL-BOUNDARY-FESHBACH-BLOCK:
construct a low-dimensional resonant block from the boundary-coupled Schur /
Feshbach data, not from an eigenvalue cutoff or spectral projector alone,
and prove projective eta-stability of the complementary block.
```

This is strictly smaller and sharper than the old wording
`MATRIX-FESHBACH-RESONANT-BLOCK`.

## 6. Status

```text
proved:    every spectral Feshbach block reduces exactly to a mode-
           subtraction rule;
proved:    spectral-block Feshbach does not create any new off-diagonal
           coupling in the resolvent;
refuted:   spectral versions of MATRIX-FESHBACH-RESONANT-BLOCK as a new
           front, because they are already covered by E77.7q--s;
open:      NONSPECTRAL-BOUNDARY-FESHBACH-BLOCK;
next:      build the resonant package from finite Schur boundary data rather
           than from spectral projectors.
```
