# E72.249 - Lambda 12 homogeneous exception

## Purpose

E72.248 shows that the homogeneous `P` degree 10 envelope fails only at `lambda=12`. This note tests
whether that finite window can be handled by a higher-degree homogeneous certificate.

## Diagnostic

Script:

```text
E72_249_lambda12_homogeneous_exception_probe.py
```

Output:

```text
E72.249 lambda=12 homogeneous exception probe
Optimizes P_j(u)=u^2R_j(u) specifically for the finite lambda=12 window.
lambda=12 dim=32 exactBSE=8.980903207468e-01
Rdeg Pdeg env slack pass status
   8   10 9.419988968536e-01 -1.098896853565e-03 NO ok
  10   12 9.347834339330e-01 +6.116566066972e-03 YES ok
  12   14 9.180472990080e-01 +2.285270099199e-02 YES ok
  14   16 9.113458345369e-01 +2.955416546314e-02 YES ok
```

## Reading

The finite `lambda=12` exception is recoverable without reintroducing dimensional drift:

```text
P degree 12 passes with slack 6.12e-3.
```

Thus the corrected LM8 route is:

```text
homogeneous degree 10 for lambda>=16,
homogeneous degree 12 or direct interval certificate for lambda=12.
```

## Caveat

These are LP/grid certificates. A final proof-facing version still needs rational coefficients and an
exact interval/SOS certificate for `R_j`.
