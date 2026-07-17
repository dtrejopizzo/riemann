# E70.3 — Resolution of the q-resolvent identity

**Date:** 2026-07-07.
**Role:** answer whether the Phase-70 closure identity can be solved as a standalone mathematical
identity.

## Verdict

The proposed q-resolvent identity

```text
Res_{spec(D_N) cap (-infty,0)}
  Tr(G_q (z-D_N)^(-1)) = 0
```

is not an independent forcing identity in its current form. It is exactly `Omega_7` at finite level,
written as a pivotal trace of the negative spectral projection.

This is a useful exact reformulation, but not a proof route unless one supplies an independent
Euler/Gamma/fusion evaluation of the full resolvent trace that does not pass through diagonalizing
`D_N`.

## Exact finite theorem

Let `D` be a finite Hermitian matrix on `H_N=span(e_0,...,e_{N-1})`. Let

```text
Pi_- = 1_{(-infty,0)}(D),
G_q e_n = q^{2(n+y)} e_n,
R_D(z;q) = Tr(G_q (z-D)^(-1)).
```

Then

```text
Res_{spec(D) cap (-infty,0)} R_D(z;q)
  = Tr(G_q Pi_-)
  = q^{2y} sum_{n=0}^{N-1} a_n (q^2)^n,
```

where

```text
a_n = <e_n, Pi_- e_n> = ||Pi_- e_n||^2 >= 0.
```

Therefore the following are equivalent:

```text
(1) Res_- R_D(z;q) = 0 as a polynomial in q^2;
(2) Pi_- = 0;
(3) D >= 0.
```

For `D=D_N=A_N^{-1/2}(A_N-P_lambda)A_N^{-1/2}`, this is exactly:

```text
q-resolvent identity for every N
  <=> D_N >= 0 for every N
  <=> Omega_7.
```

## Proof

The residue identity is the spectral theorem:

```text
(z-D)^(-1) = sum_lambda (z-lambda)^(-1) Pi_lambda.
```

Summing residues over negative eigenvalues gives `Pi_-`. Thus

```text
Res_- R_D(z;q) = Tr(G_q Pi_-).
```

Since `Pi_-` is an orthogonal projection,

```text
a_n = <e_n,Pi_-e_n> = ||Pi_-e_n||^2 >= 0.
```

If `q^{-2y}Tr(G_qPi_-)=sum a_n(q^2)^n` is identically zero, all coefficients vanish. Hence
`Pi_-e_n=0` for every basis vector, so `Pi_-=0`. Conversely, if `Pi_-=0`, the residue vanishes.

This closes the finite q-resolvent identity completely.

## Why this does not close Omega_7

The theorem above proves:

```text
zero negative residue  <=>  no negative spectrum.
```

It does not prove the zero negative residue. For the terminal defect, proving that residue vanishes is
the same statement as proving `A_N-P_lambda>=0`.

Thus the phrase

```text
prove Res_- Tr(G_q(z-D_N)^(-1)) = 0
```

is not weaker than `Omega_7`. It is `Omega_7` in spectral language.

## What would make it non-tautological

The q-resolvent route would become a genuine proof only if one constructed an independent closed form

```text
Tr(G_q (z-D_N)^(-1))
  = explicit Euler/Gamma_q/fusion expression
```

with all of the following properties:

1. it is derived without diagonalizing `D_N`;
2. it does not use zero locations;
3. it does not encode `-zeta'/zeta` as a KMS partition function;
4. it is not obtained by Cholesky/factorization of `P_lambda`;
5. its negative spectral residue can be read as zero by an algebraic/fusion rule.

No such independent evaluation is currently known in Phase 67--70. E67.15's probe even shows that the
negative-projection masses for planted off-line data are irregular, not visibly q-hypergeometric.

## Single-root warning

A fusion identity at a single root of unity would not be enough:

```text
Tr(G_{q0} Pi_-)=0
```

can happen by q-trace cancellation. It does not imply `Pi_-=0` unless the quotient trace is faithful on
the relevant idempotents. The clean finite theorem requires a polynomial identity, or enough distinct
pivotal values to determine the polynomial.

## Consequence for the closure program

The q-resolvent identity is a correct diagnostic and an exact finite equivalence. It should not be the
main remaining theorem.

The real remaining theorem is the gauge-free arithmetic majorization:

```text
Kernel AHM:
K_P >= -K_A on the upper half-plane.
```

Equivalently:

```text
Im(-d/dz log xi(1/2+iz)) >= 0 on C_+,
Lambda <= 0,
Omega_7.
```

So the closure route should be stated as:

```text
prove AHM directly from Euler structure;
use q-resolvent only as a finite spectral certificate after AHM is known,
not as an independent forcer.
```

## Final status

Closed:

```text
q-resolvent zero negative residue <=> finite Omega_7.
```

Still open and RH-equivalent:

```text
prove that the residue is zero for the actual terminal defect.
```

Therefore I cannot honestly "solve" the q-resolvent identity without proving RH. The mathematically
correct resolution is that the identity is exactly the thing to be proved, not a separate mechanism
that proves it.

