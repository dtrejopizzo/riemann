# E72.241 - Nonspectral tail bound

## Purpose

E72.238 bounded the positive tail using `D_+`. This note tests whether the split into positive part can
be removed.

For the block decomposition:

```text
A_1=[[B,C],[C^*,D]],
```

the coarse algebraic bound is:

```text
Tr(D^3)+3Tr(DC^*C)
<= ||D||op Tr(D^2) + 3||D||op ||C||_HS^2.        (NTB)
```

This uses no positive spectral projection.

## Diagnostic

Script:

```text
E72_241_nonspectral_tail_bound_probe.py
```

Output:

```text
E72.241 nonspectral tail bound probe
tail <= ||D||op Tr(D^2) + 3||D||op ||C||HS^2, no D_+ split
lam lowMargin tailExact tailPlusBound tailFullBound full/plus low/full status
 12 1.094348e-02 +1.491131e-03 3.860581e-03 7.593378e-03 1.967 1.441 PASS
 16 1.022382e-02 +9.182290e-04 2.947212e-03 6.002100e-03 2.037 1.703 PASS
 20 1.124246e-02 +4.777648e-04 2.147375e-03 4.826362e-03 2.248 2.329 PASS
 24 1.636695e-02 +6.784812e-04 1.959834e-03 4.250174e-03 2.169 3.851 PASS
 28 1.386423e-02 +5.473822e-04 1.679917e-03 3.962054e-03 2.358 3.499 PASS
 32 2.622823e-03 +5.122781e-04 1.473216e-03 3.211498e-03 2.180 0.817 FAIL
 36 1.636806e-02 +1.662408e-04 8.733170e-04 2.139203e-03 2.450 7.651 PASS
```

## Reading

The fully nonspectral tail bound works in the stable windows except the delicate `lambda=32` dip:

```text
lambda=32: lowMargin/tailFullBound = 0.817 < 1.
```

Thus there are two viable proof packages:

```text
Sharp package:
  use D_+ and prove E72.240 uniformly.

Hybrid package:
  use the nonspectral bound for the stable/asymptotic regime,
  treat delicate finite windows by the sharp finite certificate.
```

The hybrid package is likely easier to prove asymptotically, while the sharp package is better for
finite exceptional windows.
