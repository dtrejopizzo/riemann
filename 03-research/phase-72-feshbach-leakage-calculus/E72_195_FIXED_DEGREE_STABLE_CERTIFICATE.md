# E72.195 - Fixed-degree stable certificate

## Purpose

E72.194 showed that the mixed sign gate `XNEG` does not need an adaptive degree in the tested stable
range: degree `32` already makes the mixed term non-positive. This note combines the three current
stable gates into one fixed-degree certificate:

```text
NTC-8 + LM8-ASRP + XNEG-32.
```

The point is not numerical convenience. It removes the last adaptive feature from the stable
arithmetic target tested so far. The remaining stable theorem is now a finite list of fixed-degree
cycle inequalities.

## Fixed data

Use the fixed split and weights

```text
I0 = [0, 0.60 L],      I1 = (0.60 L, L],
a0 = 0.70,            a1 = 0.60.
```

Let `K0,K1` be the two block kernels produced by the scalar Weyl-Feshbach residual calculus.

The stable certificate is:

```text
NTC-8:
  Tr((K0/0.90)^16) < 1,
  Tr((K1/0.60)^16) < 1.

LM8-ASRP:
  0.90^2 Tr P0(K0/0.90) + 0.60^2 Tr P1(K1/0.60) < 0.9409,
```

where `P0,P1` are the certified degree-8 scalar majorants from E72.192, and

```text
XNEG-32:
  2 Tr(G0,32 G1,32) <= 0.
```

Here `G0,32,G1,32` are the degree-32 Chebyshev signed residual approximants from the fixed cut.

## Stress result

Script:

```text
E72_195_fixed_degree_certificate_probe.py
```

Output:

```text
E72.195 fixed-degree stable certificate probe
target: NTC-8 + LM8-ASRP + XNEG-32
 lam    L dim   NTC0    NTC1    LM8   XNEG32 pass
  12  4.97  32 1.41e-05 8.46e-03  0.937   -0.047 YES
  16  5.55  40 2.60e-06 6.35e-03  0.817   -0.046 YES
  20  5.99  48 5.36e-07 9.54e-03  0.754   -0.020 YES
  24  6.36  56 3.24e-07 7.08e-02  0.764   -0.022 YES
  28  6.66  64 2.26e-07 2.99e-02  0.663   -0.078 YES
  32  6.93  72 2.35e-08 3.51e-06  0.526   -0.003 YES
  36  7.17  80 5.11e-08 7.05e-02  0.684   -0.007 YES
worst_LM8=0.937 at lambda=12
max_XNEG32=-0.003 at lambda=32
```

## Consequence

On the tested stable range, the scalar WRL residual bound follows from fixed-degree cycle
certificates:

```text
NTC-8       cycle length 16,
LM8-ASRP   cycle length 8,
XNEG-32    mixed cycle length 64.
```

Together with the direct pre-stable `F2B` checks for `lambda=6,8,10`, this gives the current unified
finite certificate:

```text
pre-stable: direct F2B,
stable:     NTC-8 + LM8-ASRP + XNEG-32.
```

The open theorem is now sharply localized:

> Prove the three fixed-degree arithmetic cycle inequalities uniformly for the exact scalar
> Weyl-Feshbach kernels attached to the zeta prime data, without using zeros.

Equivalently, the remaining proof no longer asks for a hidden operator positivity theorem. It asks for
three explicit finite trace inequalities in the von Mangoldt cycle expansion, with fixed lengths
`16`, `8`, and `64`.

## Status

Positive, but not a proof of RH. The stable numerical certificate is fixed-degree and stress-passed;
the missing mathematical step is the uniform arithmetic proof of the three cycle inequalities.
