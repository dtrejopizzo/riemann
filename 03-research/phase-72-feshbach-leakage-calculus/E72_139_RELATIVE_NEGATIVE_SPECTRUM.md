# E72.139 -- Relative negative spectrum of the arithmetic perturbation

**Date:** 2026-07-09.
**Role:** refine `RFBD` by isolating the negative relative arithmetic modes.

## 0. Relative perturbation

Let:

```text
Delta_arith = C_actual-C_model.
```

Define the model-normalized perturbation:

```text
K_rel := C_model^(-1/2) Delta_arith C_model^(-1/2).
```

Then `RFBD` is exactly:

```text
lambda_min(K_rel) > -1.
```

More quantitatively, if:

```text
lambda_min(K_rel) >= -eta,        eta<1,
```

then:

```text
C_actual >= (1-eta)C_model.
```

## 1. Finite negative-mode certificate

Let the negative spectral decomposition be:

```text
K_rel^- = sum_{a=1}^r mu_a u_a u_a^*,       mu_a<0.
```

Then `RFBD` can be certified by the finite statement:

```text
r is finite and max_a |mu_a| <= eta<1.                       (RNMC)
```

This is tautological at finite `x`, but useful structurally: if the negative rank stays small or
organized, the arithmetic obstruction is not a full-space positivity wall.  It is a finite relative
negative-mode bound.

## 2. Diagnostic

The companion script:

```text
E72_139_relative_negative_spectrum_probe.py
```

reports:

```text
negative rank,
lambda_min(K_rel),
eta=-lambda_min(K_rel),
negative trace,
negative Frobenius norm,
positive max.
```

Representative output:

```text
E72.139 relative negative spectrum probe
 lam   L  dim  negRank  minRelDelta  eta  negTrace  negFrob  posMax
   6  3.58   18       12   -4.253e-01  0.425 2.305e+00 7.642e-01 6.066e-01
   8  4.16   24       16   -4.891e-01  0.489 2.712e+00 8.005e-01 5.693e-01
  10  4.61   28       18   -3.774e-01  0.377 2.613e+00 6.917e-01 4.950e-01
  12  4.97   32       21   -5.741e-01  0.574 2.756e+00 7.825e-01 4.628e-01
  14  5.28   36       23   -5.653e-01  0.565 2.699e+00 7.475e-01 3.978e-01
  16  5.55   40       27   -5.424e-01  0.542 2.808e+00 7.243e-01 3.712e-01
  18  5.78   44       31   -5.539e-01  0.554 2.940e+00 7.278e-01 3.473e-01
```

The negative rank grows, so the obstruction is not a few-mode phenomenon.  But the negative Frobenius
norm stays below `1`, suggesting the stronger scalar certificate of E72.140.

## 3. Status

```text
proved: RFBD is equivalent to lambda_min(K_rel)>-1;
observed: negative rank grows, but negative Frobenius norm remains below 1;
next:     use negative Hilbert-Schmidt energy as the RFBD certificate.
```
