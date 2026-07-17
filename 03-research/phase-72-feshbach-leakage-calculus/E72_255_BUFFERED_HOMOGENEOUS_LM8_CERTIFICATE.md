# E72.255 - Buffered homogeneous LM8 certificate (superseded)

## Purpose

E72.254 showed small interval overshoots in the unbuffered homogeneous LM8 majorants. This note adds a
homogeneous buffer:

```text
P_j(u) -> P_j(u)+epsilon u^2,
epsilon=5e-6.
```

Equivalently:

```text
R_j(0) -> R_j(0)+epsilon.
```

This preserves:

```text
P_j(0)=P_j'(0)=0.
```

so it does not reintroduce dimensional drift.

## Diagnostic

Script:

```text
E72_255_buffered_homogeneous_lm8_certificate.py
```

Output:

```text
E72.255 buffered homogeneous LM8 interval certificate
Adds BUFFER*u^2 with BUFFER=5.0e-06; equivalently R(0)+=BUFFER.
K0 buffered homogeneous Pdeg10:
  P(0)=+0.000000000000e+00 P'(0)=+0.000000000000e+00
  min P(u)-u^2 on [-1,0]       at -0.000331907831: -4.752446371257e-11
  min P(u)-r^2u^2 on [0,1]     at +0.000000000000: +0.000000000000e+00
K1 buffered homogeneous Pdeg10:
  P(0)=+0.000000000000e+00 P'(0)=+0.000000000000e+00
  min P(u)-u^2 on [-1,0]       at -0.000331051292: -2.782506517383e-11
  min P(u)-r^2u^2 on [0,1]     at +0.000000000000: +0.000000000000e+00
overall PASS
```

The tiny negative values occur at `|u|~3e-4` and are below the numerical tolerance; they are caused by
floating critical-point/root accuracy near the double zero at `u=0`.

## Reading

This certificate is superseded by E72.256. The reason is subtle but important: for a homogeneous
majorant `P(u)=u^2R(u)`, checking `P(u)-u^2` near the double zero at `u=0` can hide a real failure of
`R(u)>=1` in a punctured neighborhood of zero. The correct proof-facing certificate must check the
`R` inequalities directly.

The buffered homogeneous majorants here were useful as a diagnostic:

```text
P_j(u)=u^2R_j(u) + 5e-6 u^2.
```

They remove the dimensional-drift defect, but the strict interval certificate is E72.256 with a larger
buffer. The buffer cost remains negligible relative to the extended homogeneous LM8 slack; for example,
at `lambda=16` the strict envelope remains about:

```text
0.87092 < 0.9409.
```

## Remaining Exactness Step

For a paper proof, replace the floating coefficients by rational coefficients and certify the two
univariate inequalities by exact Sturm/SOS/interval arithmetic.
