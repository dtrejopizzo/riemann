# E72.256 - Strict homogeneous LM8 certificate

## Purpose

E72.255 checked `P(u)-target(u)` for the homogeneous majorant

```text
P(u)=u^2R(u).
```

That check is not strict enough near `u=0`: if `R(0)<1`, then `P(u)-u^2` is negative in a punctured
neighborhood of zero but may appear only at tiny scale because of the factor `u^2`.

This note checks the correct inequalities directly:

```text
R(u)>=1                 on [-1,0],
R(u)>=(1-a)^2           on [0,1].
```

## Diagnostic

Script:

```text
E72_256_strict_homogeneous_lm8_certificate.py
```

Output:

```text
E72.256 strict homogeneous LM8 certificate
Checks R inequalities directly with BUFFER=1.5e-03 added to R(0).
K0 strict Rdeg8:
  R(0)=+1.000198611200e+00 R'(0)=-2.612679762300e+00
  min R(u)-1 on [-1,0]        at +0.000000000000: +1.986112000001e-04
  min R(u)-r^2 on [0,1]       at +0.449250478504: +1.496516360979e-03
K1 strict Rdeg8:
  R(0)=+1.000732370790e+00 R'(0)=-1.539636264700e+00
  min R(u)-1 on [-1,0]        at +0.000000000000: +7.323707900000e-04
  min R(u)-r^2 on [0,1]       at +0.305250101916: +1.498058671267e-03
overall PASS
```

## Reading

The strict buffer is:

```text
R(0) -> R(0)+1.5e-3,
P(u) -> P(u)+1.5e-3 u^2.
```

It keeps:

```text
P(0)=P'(0)=0,
```

and therefore does not reintroduce dimensional constant drift.

This is the proof-facing homogeneous LM8 majorant.
