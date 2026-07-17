# E73.044 results - dominant-node split

## 1. Purpose

E73.044 measures how much of `WCS` is carried by the largest critical-node contributions.

The terms are

```text
T_k := e^(alpha L)G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|.
```

## 2. Representative output

```text
E73.044 dominant-node split probe
 lam     L sigma     tau  m      WCS   top1  top2  top3  topGamma1  mesh1     C1
   8   4.159  0.05   14.13  2 2.395e-07   0.48  0.86  1.00     32.935 1.18e+00 2.71e-09
  14   5.278  0.20   14.13  3 1.529e-05   0.50  0.74  0.94     32.935 1.73e+00 4.06e-09
  16   5.545  0.20   21.02  3 2.858e-05   0.69  1.00  1.00     37.586 1.03e+00 1.31e-08
  18   5.781  0.20   14.13  3 9.016e-06   0.72  0.92  1.00     30.425 5.08e-02 1.19e-07
  24   6.356  0.20   21.02  3 1.726e-05   0.99  1.00  1.00     37.586 1.41e-01 7.07e-08
```

## 3. Diagnosis

In the tested windows:

```text
top3 usually captures all visible WCS mass;
top2 captures at least about 0.71 and often essentially all;
top1 becomes dominant in the harder high-L windows.
```

The leading critical node is not always the nearest zero to the off-line center.  It is the node
where the product

```text
Hermite coupling * mesh defect * Cauchy defect
```

is largest.

## 4. Consequence

The next sufficient theorem is not a global average.  It is:

```text
DNS:
dominant nodes are certified individually,
and the remaining tail is controlled by a coarse separated product or Cauchy-Schwarz bound.
```

This is a finite positive certificate format compatible with `WCS`.
