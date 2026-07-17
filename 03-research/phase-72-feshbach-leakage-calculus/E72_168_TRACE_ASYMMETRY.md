# E72.168 -- Trace asymmetry form of BSE

**Date:** 2026-07-09.
**Role:** rewrite the block sign-energy gate as trace asymmetry plus size estimates.

## 0. Scalar identity

For a self-adjoint block `K` and a fixed weight `a`, define:

```text
E_a(K)=(1-a)^2||K^+||_HS^2+||K^-||_HS^2.
```

Let:

```text
H(K)=||K||_HS^2,
S(K)=Tr(K|K|)=||K^+||_HS^2-||K^-||_HS^2.
```

Then:

```text
E_a(K)=c_a H(K)-d_a S(K),
c_a=(1+(1-a)^2)/2,
d_a=(1-(1-a)^2)/2.
```

For the fixed weights:

```text
a_0=0.70: c_0=0.545, d_0=0.455,
a_1=0.60: c_1=0.580, d_1=0.420.
```

Thus the block sign energy is:

```text
BSE=0.545H(K_0)-0.455S(K_0)
   +0.580H(K_1)-0.420S(K_1).
```

This removes the sign decomposition from the statement: it is enough to prove Hilbert-Schmidt size
and signed absolute-trace asymmetry estimates.

## 1. Diagnostic output

The companion script:

```text
E72_168_trace_asymmetry_probe.py
```

reports:

```text
E72.168 trace asymmetry probe
cut=0.60, weights a0=0.70,a1=0.60
 lam    L  block   HS2    pos2    neg2  posFrac  sigAbs    E
   6  3.58    K0  1.895   1.358   0.537    0.717   0.821  0.659
   6  3.58    K1  0.723   0.213   0.511    0.294  -0.298  0.545
   8  4.16    K0  1.461   0.902   0.559    0.617   0.343  0.641
   8  4.16    K1  0.596   0.252   0.344    0.423  -0.091  0.384
  10  4.61    K0  1.381   0.952   0.429    0.689   0.523  0.515
  10  4.61    K1  0.628   0.200   0.429    0.318  -0.229  0.461
  12  4.97    K0  1.282   0.788   0.494    0.615   0.294  0.565
  12  4.97    K1  0.468   0.161   0.307    0.343  -0.147  0.333
  14  5.28    K0  1.179   0.733   0.445    0.622   0.288  0.511
  14  5.28    K1  0.462   0.154   0.307    0.334  -0.153  0.332
  16  5.55    K0  1.042   0.642   0.399    0.617   0.243  0.457
  16  5.55    K1  0.470   0.159   0.311    0.337  -0.153  0.337
  18  5.78    K0  0.939   0.541   0.398    0.576   0.142  0.447
  18  5.78    K1  0.323   0.131   0.192    0.405  -0.061  0.213
  20  5.99    K0  0.922   0.570   0.352    0.618   0.218  0.403
  20  5.99    K1  0.440   0.129   0.311    0.293  -0.182  0.332
  22  6.18    K0  0.847   0.512   0.335    0.604   0.177  0.381
  22  6.18    K1  0.495   0.140   0.355    0.283  -0.215  0.377
  24  6.36    K0  0.850   0.525   0.325    0.617   0.199  0.372
  24  6.36    K1  0.467   0.118   0.349    0.252  -0.232  0.368
```

## 2. Reading

The two blocks play different roles.

```text
K_0: larger HS mass, but positive-asymmetric;
K_1: negative-asymmetric, but smaller HS mass.
```

For `K_0`, the proof should exploit:

```text
S(K_0) >= sigma_0 H(K_0)
```

with observed `sigma_0` around `0.20--0.38` in the stable range. This converts:

```text
E_0 <= (0.545-0.455 sigma_0)H(K_0).
```

For `K_1`, the proof can tolerate negative asymmetry if:

```text
H(K_1) <= h_1
```

is small enough, since:

```text
E_1 <= H(K_1).
```

Thus a clean sufficient asymptotic package is:

```text
H(K_0)<=h_0,
S(K_0)>=sigma_0 H(K_0),
H(K_1)<=h_1,
cross_+<=chi,
(0.545-0.455sigma_0)h_0+h_1+chi < 1.
```

This is the current analytic form of the arithmetic gate.

## 3. Candidate numerical constants

For the tested stable range `lambda>=12`, the observed safe constants are:

```text
H(K_0)<=1.282,
S(K_0)/H(K_0)>=0.151,
H(K_1)<=0.495,
cross_+<=0.034.
```

They give:

```text
(0.545-0.455*0.151)*1.282+0.495+0.034 = 1.106,
```

which is not yet a proof-quality bound. The constants are individually too crude. The sharper target
must keep the actual split:

```text
E_0<=0.565,
E_1<=0.377,
cross_+<=0.034,
```

which gives:

```text
E_0+E_1+cross_+ <= 0.976 < 1.
```

So the next proof target is not merely size/asymmetry separately; it is the direct pair of trace
functional bounds:

```text
0.545H(K_0)-0.455S(K_0)<=0.565,
0.580H(K_1)-0.420S(K_1)<=0.377.
```

Together with `cross_+<=0.034`, these imply `F2B-PSD` in the stable range.
