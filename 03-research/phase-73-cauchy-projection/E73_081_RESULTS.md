# E73.081 results - diagonal/off-diagonal audit

## 1. Purpose

E73.081 tests whether the factor budget needs a singular diagonal treatment.

The initial worry was that `A_L(z,w)` and `B_L(z,w)` might become large when the heights of `z` and
`w` are close.

## 2. Output

```text
E73.081 diagonal/off-diagonal factor probe
Splits coefficient-weighted H0 budget for critical zero windows.
 lam     L   zIm   q    diag#   diagB    offB    totalB   delta
  16   5.545  14.13 0.0       1  -18.847  -11.306  -11.306 1.00e+00
  16   5.545  14.13 1.0       0     -inf  -11.306  -11.306 1.80e-01
  20   5.991  14.13 0.0       1  -17.605  -10.783  -10.783 1.00e+00
  20   5.991  14.13 1.0       0     -inf  -10.783  -10.783 1.67e-01
  24   6.356  14.13 0.0       1  -17.184  -10.835  -10.835 1.00e+00
  24   6.356  14.13 1.0       0     -inf  -10.835  -10.835 1.57e-01
```

## 3. Diagnosis

There is no true diagonal singularity on the shifted line:

```text
Re z=sigma>0,
Re w=0.
```

Hence:

```text
|w-z|>=sigma,
|w+z|>=sigma.
```

The apparent large coefficients at equal heights are still finite and bounded by the shifted-line
gap.  The correct analytic target is therefore not a singular diagonal theorem, but a uniform
shifted-strip coefficient bound.

## 4. Consequence

E73.080 was corrected to use:

```text
UNIFORM-FACTOR:
sum_k W_k e^(sigma L)
sum_{w in Z_T/+-} ( |H_0(w)|+|H_0(-w)| )
<= C L^-5.
```

This is cleaner than a diagonal/off-diagonal proof unless `sigma` is later allowed to shrink with
`L`.

## 5. Status

```text
falsified: need for a true singular diagonal split at fixed sigma;
proved: shifted-line gap gives uniform coefficient denominator control;
open: prove the resulting H_0 nodal budget.
```
