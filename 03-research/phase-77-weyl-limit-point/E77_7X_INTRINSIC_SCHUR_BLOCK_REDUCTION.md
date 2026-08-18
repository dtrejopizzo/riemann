# E77.7x - Intrinsic Schur block reduction

**Run:** 2026-07-18.

## 1. Purpose

After E77.7w, every attempted resonant package built as an external
subspace of the inner coordinates has been refuted:

```text
spectral mode cuts,
spectral windows,
source-only Krylov blocks,
boundary-pair Krylov blocks.
```

This note records the structural reason the next object must be formulated
directly in the finite Schur/Feshbach coordinates already present in the
ledger.

## 2. The response already factors through a finite Schur block

P76.049 and E77.5f prove that for the right transfer at a fixed finite
section,

```text
T_b(z) = t0(z) - tau(z) Sigma^{-1} kappa,       (X-1)
T_b'(z) = t0'(z) - tau'(z) Sigma^{-1} kappa.    (X-2)
```

Here:

```text
Sigma = C - U^T A0^{-1} U,
kappa = g_shell - U^T A0^{-1} g_core,
tau(z) = r_shell(z) - r_core(z) A0^{-1} U,
t0(z) = 1/(z-d_b) - r_core(z) A0^{-1} g_core.
```

Everything in the finite boundary response is already compressed into the
active shell Schur block and its coupled source/row data.

In particular, the projective quantity relevant for the LP bridge is

```text
Pi_N(z) = T_b(z) / T_b(z_0),                    (X-3)
```

so any singular regularization that works only at the full-coordinate level
but does not descend to `(X-1)` is too coarse.

## 3. Why the external subspace probes stall

The probes E77.7v--w attempted to regularize the inner solve

```text
x_{N,eta} = (A_N(mu_ref)-i eta I)^(-1) b_N
```

by subtracting various external trial subspaces before applying the Cauchy
row and forming the quotient.

But `(X-1)` shows that the boundary response does not depend on `x` through
an arbitrary inner-coordinate geometry.  It depends on `x` only through the
paired Schur combination

```text
tau(z) Sigma^{-1} kappa.
```

So an external trial subspace can easily remove a large part of `x` while
missing the actual unstable Schur coordinate, or vice versa.  That is
exactly the pattern seen in E77.7q--w:

```text
real effect, but not coherent closure.
```

## 4. Consequence

The next admissible singular object must act directly on the intrinsic Schur
data:

```text
Sigma,
kappa,
tau,
t0,
```

before reconstructing `T_b`.

Equivalently, the resonant package should be defined by a low-dimensional
regularization of

```text
v = Sigma^{-1} kappa
```

and of the paired scalar

```text
theta = tau v / t0,                             (X-4)
```

not by a projector in the full inner coordinate space.

## 5. Smaller live object

The next admissible reduction is therefore:

```text
INTRINSIC-SCHUR-FESHBACH-BLOCK:
regularize the singular finite section at the level of the active Schur
block and its coupled source/row package (Sigma, kappa, tau, t0), and prove
projective eta-stability there before lifting back to T_b.
```

This is strictly sharper than the previous wording:

```text
NONSPECTRAL-BOUNDARY-FESHBACH-BLOCK.
```

The new wording rules out further drift into arbitrary external subspaces.

## 6. Status

```text
proved:    the finite boundary response already factors exactly through the
           Schur block (P76.049, E77.5f);
proved:    every full-coordinate regularization is only relevant insofar as
           it changes the Schur package tau Sigma^{-1}kappa;
refined:   the live singular target is INTRINSIC-SCHUR-FESHBACH-BLOCK;
next:      audit singular regularization directly on v=Sigma^{-1}kappa and
           theta=tau v / t0 rather than on external inner-coordinate
           subspaces.
```
