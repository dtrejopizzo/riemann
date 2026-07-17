# E73.301 - Neutral ramp curvature correction

Date: 2026-07-16.

## 1. Purpose

E73.299 corrected the sign for the simple ramp `r_0(y)=y(1-y/L)`.  But the
load-bearing balanced ramp was fixed earlier in E73.193:

```text
r_*(y)=r_0(y)+c_Lr_1(y),
r_1(y)=y^2(1-y/L),
F_L[r_*]=0.
```

This note gives the final curvature operator for the actual neutral ramp.

## 2. Derivation

Let

```text
B(y)=qQ_yeta,
B^bal(y)=B(y)-B'(0)r_*(y).
```

As before,

```text
Q_0'=-(2/L)J,
B'(0)=qQ_0'eta=-(2/L)qJeta.
```

For the neutral ramp,

```text
r_*''(y)=r_0''(y)+c_Lr_1''(y)
        =-2/L+c_L(2-6y/L).
```

Therefore

```text
(B^bal)''(y)
=B''(y)-B'(0)r_*''(y)
=qQ_y''eta+(2/L)r_*''(y)qJeta
=q[Q_y''+alpha_L(y)J]eta,
```

where

```text
alpha_L(y)=(2/L)[-2/L+c_L(2-6y/L)].
```

This is the final corrected curvature operator.

## 3. Endpoint

The proof-facing second-Abel endpoint is:

```text
CURV-ABEL-neutral:
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

It is equivalent to the finite identity package:

```text
FINAL-ETA-ADJ
<=> CELL-CTM
<=> Schur-commutator cancellation.
```

## 4. Why this matters

The constant correction `-(4/L^2)J` is only the `c_L=0` special case.  It is
not the exact neutral ramp used to preserve the scalar center:

```text
F_L[B^bal]=F_L[B].
```

Thus future analytic work must use `alpha_L(t)J`, not the constant correction.

## 5. Status

```text
proved: exact neutral-ramp curvature formula;
supersedes: E73.299 as the load-bearing curvature endpoint;
kept: E73.299 as the sign audit for the simple-ramp component;
open: prove CURV-ABEL-neutral uniformly from Gamma-prime/eigenline structure.
```

