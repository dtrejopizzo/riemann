# E74.3 - Harmonic-symbol normal form

Date: 2026-07-16.

## Input from E74.2

For each Cauchy row `r_beta`,

```text
A r_beta = H_beta r_beta,
H_beta(n)= -i/(2 pi) sum_{m != n}[1/(m-n)-1/(m-beta)].
```

## Exact normal form

The Hilbert product rule is

```text
HPR =
<r, M_U eta> + <r, M_W A eta> + <eta, M_W A r>.
```

Using the bilinear convention of the finite scalar and the pointwise identity
`A r = H_beta r`, the last term becomes

```text
<eta, M_W A r> = <r, M_W H_beta eta>.
```

Hence

```text
HPR =
<r, M_U eta> + <r, M_W (A+M_{H_beta}) eta>.              (HS-NF)
```

This is the correct replacement for the rejected one-sided symbol collapse.

## Meaning

The remaining cancellation is no longer hidden in a Loewner matrix.  It is the
directional smallness of

```text
M_U eta + M_W (A+M_{H_beta}) eta
```

against the Cauchy row `r_beta`.

Thus the new theorem target is:

```text
Harmonic-Symbol Eigenline Cancellation.
For eta=R_w xi_L and every admissible beta,

<r_beta, M_U eta + M_W (A+M_{H_beta}) eta> = O_M(L^(-M)).
```

This keeps the mesh Hilbert transform explicit and avoids the false constant
eigenvalue heuristic.

## Status

```text
proved: exact HS-NF identity;
verified: HS-NF equals HPR to roundoff;
open: derive smallness from the pole-even eigenline equation.
```
