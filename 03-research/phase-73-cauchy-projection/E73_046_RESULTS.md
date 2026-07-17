# E73.046 results - admissible DNS audit

## 1. Purpose

E73.045 required the dominant set `D` to be chosen without using `|C_x(i gamma)|`; otherwise the
dominant-node split is only a rearrangement of `WCS`.

E73.046 tests the cleanest admissible choice:

```text
D_r(A,L) = top r nodes by
e^(alpha L) G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

This uses only geometry and mesh, not the Cauchy spectral data.

## 2. Result

The admissible geometric-mesh selection fails in important windows.

Representative output:

```text
E73.046 admissible DNS probe
Dominants are selected without C_x: by geometric-mesh weight only.
 lam     L sigma     tau  m   WCS   adm1 adm2 adm3  post3 overlap3  firstAdmGamma firstPostGamma
   8   4.159  0.05   14.13  2 2.39e-07  0.00  0.49  0.87   1.00        2         25.011         32.935
  14   5.278  0.20   14.13  3 1.53e-05  0.23  0.44  0.94   0.94        3         37.586         32.935
  18   5.781  0.20   14.13  3 9.02e-06  0.20  0.28  0.28   1.00        2         37.586         30.425
  24   6.356  0.20   14.13  3 1.59e-05  0.01  0.02  0.02   1.00        2         32.935         37.586
```

Here:

```text
adm3  = WCS fraction captured by top 3 geometric-mesh nodes;
post3 = WCS fraction captured by top 3 nodes chosen after seeing T_k.
```

The gap at `L=6.356` is fatal for geometry-only `DNS`:

```text
adm3 about 0.02, while post3 about 1.00.
```

## 3. Diagnosis

The dominant WCS nodes are not determined by the Hermite-mesh envelope alone.  They are determined
by the product

```text
geometry * mesh * Cauchy defect.
```

Therefore the arithmetic factor `C_x` is load-bearing in selecting the dangerous nodes.

## 4. Consequence

The following route is rejected:

```text
geometry-only DNS => WCS.
```

Any non-tautological dominant-node theorem must choose candidate dominant nodes from an arithmetic
proxy that is independent of the final value being bounded.  Admissible proxies include:

```text
1. finite Cauchy divisor data of P_x;
2. mesh-root combined score using distance to Div(P_x);
3. structural equations satisfied by the CCM pole-even vector xi.
```

The proxy cannot be the final term

```text
T_k = geometry * mesh * |C_x(i gamma_k)|.
```

## 5. Updated endpoint

The remaining finite identity is now sharper:

```text
Arithmetic DNS:
construct a small dominant set D_r(A,L) using finite divisor/eigenvector data before evaluating WCS,
then prove DNS-main and DNS-tail.
```

This keeps the dominant-node split alive, but it rules out a purely geometric selection.
