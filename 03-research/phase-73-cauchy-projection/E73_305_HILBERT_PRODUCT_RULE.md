# E73.305 - Hilbert product rule for the closed distribution

Date: 2026-07-16.

## 1. Purpose

E73.304 gives the off-diagonal distribution term

```text
T^off=sum_{j != b} r_j eta_b /(2 i pi(n_b-n_j))
      [delta_{d_j}-delta_{-d_j}-delta_{d_b}+delta_{-d_b}].
```

Pairing with `W` gives the off-diagonal scalar

```text
Off(F)=sum_{j != b} r_j eta_b
       (F_j-F_b)/(2 i pi(n_b-n_j)),
F_j=W^odd(d_j).
```

This note rewrites `Off(F)` as a discrete product rule.

## 2. Mesh Hilbert matrix

Define the skew mesh matrix

```text
A_{jb}=1/(2 i pi(n_b-n_j)),  j != b,
A_{jj}=0.
```

Then `A_{bj}=-A_{jb}`.  A direct index swap gives:

```text
Off(F)
=sum_j F_j [ r_j(A eta)_j + eta_j(A r)_j ].       (HPR)
```

Thus the full scalar endpoint is:

```text
sum_j eta_j r_j U^even_j
+sum_j W^odd_j r_j(A eta)_j
+sum_j W^odd_j eta_j(A r)_j
=O_M(L^(-M)).                                    (HPR-DIV)
```

## 3. Interpretation

`HPR-DIV` is a true product-rule normal form:

```text
off-diagonal distribution
= Hilbert divergence through eta
 + Hilbert divergence through the Cauchy row.
```

But it is not a forcer.  The three displayed terms are individually large.
The small scalar is a signed three-way cancellation.

## 4. Numerical certification

`E73_305_hilbert_product_rule_probe.py` checks the product rule using the
actual symbol `W^odd` and also a random non-cancelling symbol.

Representative output:

```text
 lam      L gamma row directB prodB errB randErrB diagB rAetaB etaArB cancelB
  12    4.970  14.13   0   -21.23  -21.29 -22.77   -23.16   -1.13    -1.11   -3.30   -20.55
  16    5.545  21.02   0   -18.21  -18.21 -21.85   -21.92   -1.42    -1.75   -1.16   -17.45
  20    5.991  21.02   1   -18.97  -19.20 -19.59   -19.47   -2.45    -1.67   -1.55   -17.81
```

The identity is numerically stable on the random symbol (`randErrB`), while
the actual `W` scalar sits far below the sizes of the three product-rule
pieces.  The `cancelB` column measures this cancellation budget.

## 5. Status

```text
proved: off-diagonal distribution obeys exact Hilbert product rule;
verified: product rule numerically against direct off-diagonal pairing;
rejected: any of diag, r(A eta), eta(A r) is individually small enough;
open: prove the signed three-way HPR-DIV cancellation from the eigenline.
```

