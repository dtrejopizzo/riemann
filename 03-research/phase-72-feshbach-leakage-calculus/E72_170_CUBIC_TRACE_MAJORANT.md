# E72.170 -- Cubic trace majorant audit

**Date:** 2026-07-09.
**Role:** test the first polynomial way to remove the spectral sign decomposition.

## 0. Cubic majorant

For:

```text
E_a(K)=(1-a)^2||K^+||_HS^2+||K^-||_HS^2,
```

and a spectral bound:

```text
||K||<=M,
```

the scalar inequality:

```text
lambda<0: lambda^2 <= lambda^2(1-(1-r^2)lambda/M),
lambda>0: r^2 lambda^2 <= lambda^2(1-(1-r^2)lambda/M),
r=1-a,
```

gives:

```text
E_a(K) <= Tr K^2 - (1-r^2)Tr K^3/M.
```

This is attractive because the right side is a finite trace expression.

## 1. Diagnostic result

The companion script:

```text
E72_170_cubic_trace_majorant_probe.py
```

shows that the cubic bound is too loose:

```text
lambda=12: exact BSE=0.898, cubic sum=1.594
lambda=16: exact BSE=0.794, cubic sum=1.440
lambda=20: exact BSE=0.735, cubic sum=1.340
lambda=24: exact BSE=0.740, cubic sum=1.359
```

## 2. Status

```text
proved: cubic trace majorant is valid;
failed: cubic trace majorant is too loose to prove F2B-PSD.
```

The failure is informative: the polynomial must approximate the sign-split quadratic more sharply
near the positive spectrum. This motivates the degree-10 fixed polynomial certificate of E72.171.
