# P75.002 - Exact finite numerator package

## Definitions

Let `d=(d_1,...,d_N)` be the finite CCM mesh and let `xi` be a normalized
finite eigenline.  Define

```text
D(z)=prod_n (z-d_n),
P(z)=sum_n xi_n prod_{m != n}(z-d_m),
C(z)=P(z)/D(z).
```

Then away from the mesh,

```text
C(z)=sum_n xi_n/(z-d_n).
```

The identity is algebraic: multiplying the partial fraction expansion by
`D(z)` gives the polynomial numerator exactly.

## Two-row detector

For a real ordinate `gamma`, the Phase 72/74 detector is exactly

```text
Q_gamma xi = (C(gamma), C(-gamma))
```

before optional row normalization.  With normalized rows

```text
r_+(n)=1/(gamma-d_n),  r_-(n)=1/(-gamma-d_n),
```

the measured vector is

```text
(<r_+/||r_+||,xi>, <r_-/||r_-||,xi>)
= (C(gamma)/||r_+||, C(-gamma)/||r_-||).
```

Thus `CRIT-NUM-DIV` is not a new analytic condition; it is the statement that
the finite Weyl numerator is superpolynomially divisible by the critical
evaluation functional.

## Root transport

If `tau_L` is a simple nearby root of `C`, then

```text
C(gamma)=C'(theta)(gamma-tau_L)
```

for some `theta` between `gamma` and `tau_L`.  The theorem-grade equivalence

```text
CRIT-NUM-DIV <=> CCM-ROOT-LOCK
```

therefore requires polynomial lower and upper bounds on `C'(tau_L)` after the
chosen normalization.  For a multiplicity `m`, the required finite condition is
the Hermite block

```text
P(gamma), P'(gamma), ..., P^(m-1)(gamma).
```

## Independent evaluation forms

P75 uses three equivalent finite evaluations:

```text
Cauchy:       C(z)=sum_n xi_n/(z-d_n)
Barycentric: P(z)=sum_n xi_n prod_{m != n}(z-d_m)
Bordered:    P(z)=-det [[diag(z-d), xi], [1^T, 0]]
```

The first is numerically stable away from poles; the second exposes the
polynomial numerator; the third is the determinant form used in P75.003.

