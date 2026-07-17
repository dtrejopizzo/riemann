# E72.223 - Resonant ELR closure

## Purpose

E72.222 gives the simple even-leading raw bound:

```text
Rraw_j
<= (dim_even/2) sum_{n in S_j} (Lambda(n)^2/n)(1-log n/L).
```

Combining this with coercivity gives:

```text
Res_2(S_j)
<= [dim_even/lambda_min(C_x)^2]
   sum_{n in S_j} (Lambda(n)^2/n)(1-log n/L).       (R2-ELR)
```

This note tests the complete bound against the exact resonant pair energy.

## Diagnostic

Script:

```text
E72_223_resonant_elr_closure_probe.py
```

Output:

```text
E72.223 resonant ELR closure probe
bound = dim_even/minC^2 * sum beta2*(1-u)
lam block actual bound ratio dimEven minC
 12     0 7.506459e-01 1.347720e+00 1.80   33 7.526e+00
 12     1 3.723544e-01 7.279197e-01 1.95   33 7.526e+00
 16     0 5.903247e-01 9.974520e-01 1.69   41 1.061e+01
 16     1 3.676131e-01 6.439500e-01 1.75   41 1.061e+01
 20     0 5.066864e-01 7.808971e-01 1.54   49 1.420e+01
 20     1 3.181675e-01 5.099818e-01 1.60   49 1.420e+01
 24     0 4.667205e-01 6.807382e-01 1.46   57 1.775e+01
 24     1 2.615648e-01 4.090763e-01 1.56   57 1.775e+01
 28     0 4.259593e-01 5.994829e-01 1.41   65 2.126e+01
 28     1 2.487475e-01 3.585662e-01 1.44   65 2.126e+01
```

## Reading

The complete ELR bound is effective:

```text
ratio ~= 1.4--2.0,
```

and improves with the stable window size.

It is slightly weaker than the exact raw-profiled coercive bound, but much simpler. It depends only on:

```text
dim_even,
lambda_min(C_x),
sum (Lambda(n)^2/n)(1-log n/L).
```

## Consequence

The resonant degree-2 even sublemma now has a clean proof target:

```text
ELR1: ||B_x^*U_yB_x||_HS^2 <= (dim_even/2)(1-y/L)
      plus controlled finite-section diffraction;

ELR2: lambda_min(C_x) >= c_C L^2;

ELR3: sum_{n in S_j} (Lambda(n)^2/n)(1-log n/L)
      <= explicit elementary bound.
```

Together these prove a usable bound for `Res_2(S_j)`.

## Status

Strong positive. The resonant pair channel has been reduced to elementary Fourier/model/arithmetic
inequalities with measured slack.
