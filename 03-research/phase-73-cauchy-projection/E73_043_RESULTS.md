# E73.043 results - WCS factorization audit

## 1. Purpose

E73.043 tests whether `WCS` can be proved by fully separated product bounds such as

```text
max_k |C_x(i gamma_k)| * sum_k W_k,
max_k W_k * sum_k |C_x(i gamma_k)|,
or Cauchy-Schwarz.
```

Here

```text
W_k=e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

## 2. Representative output

```text
E73.043 WCS factorization probe
 lam     L sigma     tau  m      WCS    maxDsumW  r1    maxWsumD  r2        CS  rCS  conc  corr
   8   4.159  0.05   14.13  2 2.395e-07   5.522e-07   2.3   4.227e-07   1.8 3.653e-07   1.5  0.48  0.83
  14   5.278  0.20   21.02  3 1.295e-05   1.510e-04  11.7   8.088e-05   6.2 8.270e-05   6.4  0.51  0.11
  18   5.781  0.20   21.02  3 7.160e-06   5.665e-04  79.1   3.565e-04  49.8 4.063e-04  56.7  0.64  0.40
  24   6.356  0.20   21.02  3 1.726e-05   4.240e-04  24.6   1.626e-04   9.4 2.290e-04  13.3  0.99  0.45
```

## 3. Diagnosis

Separated product bounds are not uniformly sharp.  The loss can reach factors around `80` in the
tested windows.

However, the product itself is highly concentrated:

```text
conc = max_k W_k|C_x(i gamma_k)| / sum_k W_k|C_x(i gamma_k)|
```

can be as high as `0.99`.

Therefore the correct proof shape is not a global separated product estimate.  It is a
dominant-node certificate plus a tail bound.

## 4. Status

```text
tested: global product decoupling is too lossy;
observed: WCS mass is concentrated on very few critical nodes;
feeds: E73.044 dominant-node split.
```
