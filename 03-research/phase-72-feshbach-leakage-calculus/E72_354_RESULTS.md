# E72.354 results - affine Lambda-elimination probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_354_lambda_elimination_probe.py
```

The probe tests the finite condition from E72.354:

```text
vec(S_T Adj(E)) and vec(K_T Adj(E)) are linearly dependent.
```

In the simple-rank adjugate channel this is equivalent to collinearity of

```text
S_T xi,  K_T xi.
```

The reported `wedgeRel` is the normalized maximum 2x2 minor

```text
max_{alpha,beta}|(S_alpha xi)(K_beta xi)-(S_beta xi)(K_alpha xi)|
 / (||S xi|| ||K xi||).
```

## Table

```text
lam   N roots node    ||Kxi||      ||Sxi||      wedgeRel    fitRel      |LambdaFit|
 6.0  10     2 root   1.5031e-16  1.8746e-15  9.3014e-02  1.0000e+00          nan
 6.0  10     2 shift  1.2566e+00  3.5010e+00  1.3370e-01  1.3370e-01   2.7611e+00

 8.0  12     3 root   3.0975e-12  1.3728e-11  1.3453e-01  1.3478e-01   4.3914e+00
 8.0  12     3 shift  5.0233e+00  2.3125e+01  1.4345e-01  2.0667e-01   4.5041e+00

10.0  14     3 root   2.9784e-12  1.3406e-11  1.0496e-01  1.1764e-01   4.4700e+00
10.0  14     3 shift  4.9266e+00  2.3773e+01  1.6339e-01  2.4062e-01   4.6837e+00

12.0  16     3 root   1.8317e-14  8.8271e-14  1.1092e-01  1.2162e-01   4.7834e+00
12.0  16     3 shift  4.3486e+00  2.0958e+01  3.8207e-01  4.3249e-01   4.3454e+00
```

Artificial compatible controls replace `S xi` by `-Lambda_0 K xi`.  They pass at roundoff:

```text
case   wedgeRel    fitRel      |LambdaFit|
1      0.0000e+00  4.6245e-17  2.1360e+00
2      6.5913e-17  0.0000e+00  2.1360e+00
3      1.3812e-16  2.4646e-16  2.1360e+00
4      2.1989e-17  1.5492e-16  2.1360e+00
```

## Reading

The detector is calibrated: when scalar compatibility is present by construction, the wedge minors
vanish to roundoff.

The shifted partial residuals are not scalar-compatible:

```text
wedgeRel ~= 0.13 to 0.38.
```

Thus the obstruction found in E72.351 is now expressed as exact finite 2x2 minor failure, not as a
least-squares artifact.

For root windows, `||Kxi||` is near zero because finite Weyl roots satisfy `G_x(a)=0` by construction.
Those rows are therefore not the load-bearing Xi-window test, as clarified in E72.353.

## Consequence

The current partial `S_T` is not the exact Xi-window residual.  If the Phase 72 route is to close, the
missing piece must alter `S_T` before the affine Lambda test.  It cannot be:

```text
1. a fitted scalar Lambda only;
2. an additive rowspace correction A(C_E-mu I);
3. the finite Weyl-root identity G_x(a)=0.
```

The next analytic target is therefore:

```text
derive the exact S_T^{Xi}
and prove LAMBDA-ELIM for S_T^{Xi}, K_T.
```
