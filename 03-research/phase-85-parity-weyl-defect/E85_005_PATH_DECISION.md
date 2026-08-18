# E85.005 - Path decision from moving poles to signed complement sums

## 1. Diagnostic quantities

For a parity-balanced cluster containing the nearest `r` eigenlines in each
sector, define

```text
Q_E=m_1^E/(z_O)^2,
Q_O=m_1^O/(z_E)^2,                                    (1.1)
```

where `z_O` is the smallest complementary odd eigenvalue and `z_E` the
smallest complementary even eigenvalue.  By E85.004, these are necessary
moving-pole scales for uniform pointwise collapse of the two Weyl defects.

## 2. Exact finite comparison

On the multiprecision `L=2 log 6` CCM sections, the values are

```text
outer modes   r    Q_E          Q_O          |ell_i(C^(-1)e)|
6             1    1.69e5       3.45e12      1.31e-1
6             2    3.96e1       1.14e8       1.10e-3
6             3    1.67e-1      2.11e4       2.40e-5
6             4    1.89e-2      3.00e2       5.74e-6

8             1    2.41e9       6.37e16      6.07e1
8             2    6.11e7       2.99e13      2.34
8             3    2.98e4       8.22e9       5.27e-2
8             4    5.56          1.11e6       6.93e-4.               (2.1)
```

The exact coboundary identity is satisfied to the working multiprecision
floor in every row.

## 3. Decision

The scalar safe response can already be small while the individual
moving-pole scale, especially in the odd-cluster-to-even-complement channel,
is enormous.  Therefore a proof through uniform estimates of
`Delta_P(lambda_q)` would discard the cancellation that the finite identity
actually uses.

```text
MP-1  uniform moving-pole collapse: archived as structurally over-strong;
MP-2  signed complement cancellation: retained.                     (3.1)
```

The table does not prove the limiting scalar theorem.  It decides which of
the two sufficient mechanisms is compatible with the exact finite anatomy.

## 4. Surviving target

For each parity, order the complementary eigenvalues increasingly and retain
the signed weights

```text
b_q^E(z)=L_z(q)S_q,
b_q^O(z)=L_z(q)A_q.                                   (4.1)
```

The live expressions are

```text
PW-E=alpha sum_q b_q^E(z)Delta_P^E(lambda_q),
PW-O=beta  sum_q b_q^O(z)Delta_P^O(lambda_q).          (4.2)
```

Since `-Delta_P(lambda)` is positive and decreasing above the cluster, Abel
summation can preserve cancellation through cumulative sums of the `b_q`.
This is the next admissible reduction.

## 5. Status

```text
decided:
  pointwise moving-pole bounds are not the observed mechanism;
  the signed complementary sums are indispensable;

open:
  an Abel bound for the cumulative safe spectral weights that is uniform on
  safe compact sets and stable under one derivative.
```

