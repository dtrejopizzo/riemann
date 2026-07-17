# E73.160 Results - Scalar dual cancellation audit

Date: 2026-07-12.

Script:

```text
E73_160_scalar_dual_cancellation_probe.py
```

Purpose:

Compare the absolute termwise ceiling

```text
sum_k |Pi(b,k)(exp(i gamma_k L)-1)F_x(gamma_k)|
```

against the signed scalar dual value.

## Output

```text
 lam     L b      l1B signedB cancelB maxTermB phaseVar
  16   5.545 0  -12.852  -12.865   -0.013  -12.923    1.215
  16   5.545 1  -15.296  -15.308   -0.012  -15.361    0.756
  16   5.545 2  -10.812  -10.826   -0.014  -10.890    0.934
  20   5.991 0  -12.864  -13.058   -0.195  -13.025    2.970
  20   5.991 1  -15.233  -15.441   -0.207  -15.408    3.402
  20   5.991 2  -10.879  -11.060   -0.181  -11.028    2.352
  24   6.356 0  -14.538  -14.578   -0.040  -14.575    1.759
  24   6.356 1  -16.800  -16.836   -0.036  -16.833    1.228
  24   6.356 2  -12.652  -12.695   -0.043  -12.691    1.529
  28   6.664 0  -13.919  -13.919   -0.000  -13.919    1.048
  28   6.664 1  -16.121  -16.121   -0.000  -16.121    1.368
  28   6.664 2  -12.083  -12.083   -0.000  -12.083    1.076
  32   6.931 0  -17.847  -17.879   -0.032  -17.889    1.152
  32   6.931 1  -21.339  -22.093   -0.754  -21.664    1.321
  32   6.931 2  -17.000  -17.187   -0.187  -17.239    1.598
```

## Reading

There is little critical-node cancellation in the current diagnostic:

```text
cancelB ~= 0 to -0.2
```

except for one stronger row at `lambda=32,b=1`.

The signed scalar is essentially the termwise ceiling.  Therefore a proof
can plausibly proceed by:

```text
critical-line polynomial Cauchy values
+ weighted confluent Cauchy projection geometry.
```

This supports the E73.024 route and deprioritizes a search for hidden
multi-critical phase cancellation.
