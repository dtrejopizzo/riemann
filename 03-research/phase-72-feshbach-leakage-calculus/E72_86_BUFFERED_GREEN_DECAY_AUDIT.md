# E72.86 -- Buffered Green decay audit

**Date:** 2026-07-09.
**Role:** test whether physical cofactor tightness follows from an operator-norm Green decay between
separated physical bands.

## 0. Buffered operator

Let:

```text
S_R = physical source band |d_n|<=R,
T_H = physical tail band |d_n|>H,
H>R.
```

The strongest clean mechanism would be:

```text
||T_H C_E^(-1) S_R|| -> 0
```

as `H-R->infty`, uniformly for large `x`. This would imply E72.84's `(PDCT)` for all sources in the
fixed physical band `S_R`, hence for Cauchy sources after source-tail truncation.

## 1. Numerical result

The companion script:

```text
E72_86_buffered_green_decay_probe.py
```

measures the operator norm:

```text
||T_H C_E^(-1) S_R||.
```

Representative output:

```text
lambda=20, N=40:
  R=8,  H=12  norm=4.886e-02
  R=8,  H=24  norm=3.302e-02
  R=8,  H=36  norm=2.338e-02
  R=18, H=24  norm=5.144e-02
  R=18, H=36  norm=3.599e-02

lambda=24, N=48:
  R=8,  H=12  norm=4.811e-02
  R=8,  H=24  norm=4.704e-02
  R=8,  H=36  norm=4.665e-02
  R=18, H=24  norm=4.850e-02
  R=18, H=36  norm=4.809e-02
```

The norm is small, but the tested windows do not show decisive decay with the buffer.

## 2. Consequence

This does **not** falsify physical cofactor tightness `(PDCT)`, because `(PDCT)` only asks about the
specific Cauchy channel:

```text
C_E^(-1)Q_even r_s^even.
```

But it does rule out the currently tested stronger proof route:

```text
uniform operator-norm propagation decay for every source in S_R.
```

The next theorem must use the analytic Cauchy structure of `r_s^even`, not just its support.

## 3. Refined target

The correct target becomes:

```text
Cauchy-channel physical Green decay (CCGD):
For every compact s-window K,

lim_{H->infty} limsup_{x->infty} sup_{s in K}
  ||T_H C_E^(-1)Q_even r_s^even|| / ||C_E^(-1)Q_even r_s^even|| = 0.
```

This is exactly E72.84's `(PDCT)`, now understood as a channel theorem rather than a full operator
theorem.

## 4. Status

```text
rejected: currently tested full operator-norm Green decay as the proof mechanism;
kept:     small buffered norms as supportive structure;
new target: prove Cauchy-channel Green decay (CCGD).
```
