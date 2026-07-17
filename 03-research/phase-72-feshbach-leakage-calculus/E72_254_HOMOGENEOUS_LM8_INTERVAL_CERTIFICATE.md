# E72.254 - Homogeneous LM8 interval certificate

## Purpose

E72.248 produced homogeneous LM8 majorants:

```text
P_j(u)=u^2R_j(u).
```

This note checks the interval inequalities by critical points, not by grid.

## Diagnostic

Script:

```text
E72_254_homogeneous_lm8_interval_certificate.py
```

Output:

```text
E72.254 homogeneous LM8 interval certificate
Checks E72.248 P degree 10 homogeneous majorants on full intervals.
K0 homogeneous Pdeg10:
  P(0)=+0.000000000000e+00 P'(0)=+0.000000000000e+00
  min P(u)-u^2 on [-1,0]       at -0.408250666648: -3.514560905252e-07
  min P(u)-r^2u^2 on [0,1]     at +0.449250617623: -7.030891202046e-07
K1 homogeneous Pdeg10:
  P(0)=+0.000000000000e+00 P'(0)=+0.000000000000e+00
  min P(u)-u^2 on [-1,0]       at -0.800750146917: -1.107307419439e-07
  min P(u)-r^2u^2 on [0,1]     at +0.305250306665: -1.808885214397e-07
overall FAIL
```

## Reading

The unbuffered homogeneous LP coefficients have small interval overshoots of size `~10^-7`. This is
not a structural failure. It is the expected difference between grid LP fitting and critical-point
certification.

The important structural properties do hold:

```text
P(0)=P'(0)=0.
```

Thus the fix should be a homogeneous buffer, not a constant buffer.
