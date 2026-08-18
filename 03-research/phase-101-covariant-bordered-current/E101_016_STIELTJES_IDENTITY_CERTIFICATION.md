# E101.016 - Stieltjes identity certification

## 1. Independent comparison

The raw identity E101.014(4.3) was checked without computing the secular
zeros.
For the exact finite CCM transfer, define

```text
Phi_N(z)=sin(zL/2)T_N(z).                             (1.1)
```

On the safe axis, direct differentiation gives the independent quantity

```text
D_N(sigma)
 ={1/2}d/d sigma log|Phi_N(i sigma)|^2.              (1.2)
```

The cofactor-transfer side is

```text
Q_N(sigma)
 =(L/2)coth(sigma L/2)
  +Re{iT_N'(i sigma)/T_N(i sigma)}.                  (1.3)
```

E101.014 predicts `D_N=Q_N`.

## 2. Multiprecision result

Using the exact Gamma--prime CCM builder with `L=6`, `sigma=1.25`, and
independent automatic differentiation of (1.2), one obtains

```text
N       |D_N-Q_N|             Q_N/sigma
6       4.88e-41              0.126233909282864695
8       4.38e-47              0.103291253687566892
10      3.17e-46              0.089235559903878422
```

The corresponding transfer slopes are

```text
N       Re{iT_N'/T_N}(i sigma)
6       -1.67507114213828587
8       -1.70374946163240812
10      -1.72131907886201871.
```

They cancel the positive hyperbolic lattice slope in (1.3), leaving the
nonnegative Stieltjes mass displayed in the last column.

## 3. Scope

The calculation certifies

```text
the factor of two from bilateralization;
the sign of the transfer slope;
the unmatched boundary-mesh multiplicity;
the hyperbolic normalization.                        (3.1)
```

It does not establish a cofinal bound in `L`; that remains the analytic
content of `RENORMALIZED-SLOPE`.

## 4. Status

```text
certified:
  exact raw Stieltjes mesh-cancellation identity at multiple finite sections;

open:
  uniform outer-length bound.
```
