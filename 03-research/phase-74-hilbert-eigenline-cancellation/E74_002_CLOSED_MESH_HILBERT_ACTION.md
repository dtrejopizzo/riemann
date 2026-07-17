# E74.2 - Closed finite-mesh Hilbert action on Cauchy rows

Date: 2026-07-16.

## Statement

Let the mesh be `d_n=2 pi n/L` over the finite index set `I`, and let

```text
A_nm = 1/(2 i pi (m-n)), n != m,       A_nn=0.
```

For a Cauchy row

```text
r_beta(n)=1/(i(d_n-2 pi beta/L))
         = L/(2 pi i) * 1/(n-beta),
```

the action of `A` is exactly

```text
(A r_beta)(n)
= -L/(4 pi^2) sum_{m in I, m != n} 1/((m-n)(m-beta)).              (1)
```

Equivalently, by the partial fraction identity

```text
1/((m-n)(m-beta))
= 1/(n-beta) * ( 1/(m-n) - 1/(m-beta) ),
```

one has the multiplicative finite-symbol formula

```text
(A r_beta)(n)=H_beta(n) r_beta(n),                                  (2)
```

where

```text
H_beta(n)= -i/(2 pi) sum_{m in I, m != n}
          [ 1/(m-n) - 1/(m-beta) ].                                 (3)
```

This is the correct replacement for the continuous heuristic
`A r_beta ~= const * r_beta`.

## Consequence

The finite mesh Cauchy row is not an eigenvector.  It is an invariant line only
after allowing multiplication by the nonconstant symbol `H_beta(n)`.

Therefore the Phase 74 lever must be reformulated:

```text
old false lever:
  A r_beta = c_beta r_beta + small.

new exact lever:
  A r_beta = H_beta r_beta,
  H_beta explicit finite harmonic/digamma symbol.
```

The open problem becomes whether the HPR scalar can be rewritten with this
symbol in a form that the pole-even eigenline equation annihilates.

## Status

```text
proved: exact finite formula (1);
proved: exact multiplicative symbol formula (2)-(3);
rejected: constant quasi-eigenvalue collapse as a load-bearing lemma;
open: absorb H_beta into the two-symbol/eigenline equation without smuggling
      zero data or endpoint inverses.
```
