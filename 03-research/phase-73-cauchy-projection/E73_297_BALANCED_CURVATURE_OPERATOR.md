# E73.297 - Balanced curvature operator

Date: 2026-07-16.

## 1. Purpose

E73.194 gives the second-Abel endpoint:

```text
F_L[B]=int_0^L K_L(t)(B^bal)''(t)dt,
```

for the balanced transverse packet

```text
B(y)=qQ_yR_wxi_L.
```

This note writes `(B^bal)''` as one explicit finite matrix operator.  This
removes the remaining ramp bookkeeping from the second-Abel form.

## 2. Balanced packet

Let

```text
eta=R_wxi_L,
B(y)=qQ_yeta.
```

Since

```text
Q_0'=-(2/L)J,       J=11^T,
```

we have

```text
B'(0)=qQ_0'eta=-(2/L)qJeta.
```

Use the neutral ramp from E73.193:

```text
r_*(y)=r_0(y)+c_Lr_1(y),
r_0(y)=y(1-y/L),
r_1(y)=y^2(1-y/L),
B^bal(y)=B(y)-B'(0)r_*(y).
```

Then

```text
(B^bal)''(y)
=qQ_y''eta-B'(0)r_*''(y)
=q[Q_y''+alpha_L(y)J]eta,                      (CURV)
```

where

```text
alpha_L(y)=(2/L)r_*''(y)
          =(2/L)[-2/L+c_L(2-6y/L)].
```

The constant part has the negative sign found in E73.299; the additional
`c_Lr_1` term is required by the exact neutral ramp `F_L[r_*]=0`.

## 3. Explicit matrix entries

For `d_j=2*pi*n_j/L`, the cell entries are

```text
Q_y(j,j)=2(1-y/L)cos(d_jy),
Q_y(j,b)=(sin(d_jy)-sin(d_by))/(pi(n_b-n_j)),  j != b.
```

Therefore

```text
Q_y''(j,j)
= (4d_j/L)sin(d_jy)
   -2(1-y/L)d_j^2cos(d_jy),
```

and, for `j != b`,

```text
Q_y''(j,b)
=(-d_j^2sin(d_jy)+d_b^2sin(d_by))/(pi(n_b-n_j)).
```

The sign of the diagonal `4d_j sin(d_jy)/L` term is positive.

## 4. Curvature form of the endpoint

Combining E73.194 with `(CURV)`, the final scalar is equivalently:

```text
CURV-ABEL:
int_0^L K_L(t) q[Q_t''+alpha_L(t)J]R_wxi_L dt
=O_M(L^(-M)).
```

This is the same theorem as:

```text
FINAL-ETA-ADJ,
CELL-CTM,
Schur-commutator cancellation.
```

It is useful because all boundary terms have been absorbed into the explicit
rank-one curvature correction `alpha_L(t)J`.

## 5. Numerical certification

`E73_297_curvature_operator_probe.py` compares the closed formula against
finite differences of the balanced packet.  Representative output:

```text
 lam     L gamma row y/L relErr absErr
  updated in E73.297 results after the E73.301 ramp correction
```

The finite-difference check is only a sign/normalization audit; `(CURV)` is an
exact algebraic identity.

E73.299 records the constant-sign correction, and E73.301 records the final
neutral-ramp correction including the `c_Lr_1` term.

## 6. What this does not prove

The curvature operator is not norm-small.  The theorem is a signed
orthogonality statement with the exact discrepancy kernel `K_L`:

```text
<K_L, q[Q_t''+alpha_L(t)J]eta>=O_M(L^(-M)).
```

Thus one must not split `Q_t''` and `J` into separate absolute bounds.  The
rank-one correction is part of the cancellation.

## 7. Status

```text
proved: balanced curvature identity (CURV);
reduced: SECOND-ABEL to CURV-ABEL with explicit matrix entries;
verified: signs/factors numerically by finite differences;
open: prove CURV-ABEL uniformly from the signed Gamma-prime/eigenline
      structure.
```
