# E73.193 - Balanced ramp

Date: 2026-07-14.

## 1. Purpose

E73.192 showed that subtracting the naive ramp

```text
r_0(y)=y(1-y/L)
```

creates a bad split: the ramp and remainder are much larger than the final
signed residual and cancel each other.  This note fixes the normalization.

## 2. Definition

Let

```text
r_0(y)=y(1-y/L),
r_1(y)=y^2(1-y/L).
```

Then

```text
r_0(0)=0,      r_0'(0)=1,      r_0(L)=0,
r_1(0)=0,      r_1'(0)=0,      r_1(L)=0.
```

Let

```text
F_L[f]=A_L[f]-P_L[f],
```

with the same Dirichlet archimedean cell and prime sampling used in
`TRANS-CELL`.  If `F_L[r_1] != 0`, define

```text
c_L=-F_L[r_0]/F_L[r_1],
r_*(y)=r_0(y)+c_L r_1(y).
```

Then

```text
r_*(0)=0,      r_*'(0)=1,      r_*(L)=0,
F_L[r_*]=0.                                          (1)
```

This is an exact finite normalization.  It depends on the model-prime
quadrature at height `L`, but not on zeta zeros or on the smallness of
`Q_wxi_L`.

## 3. Consequence for the transverse packet

Set

```text
B_a^bal(y)=B_a(y)-B_a'(0)r_*(y).
```

Then

```text
B_a^bal(0)=0,
(B_a^bal)'(0)=0,
B_a^bal(L)=0,
```

and by (1)

```text
F_L[B_a]=F_L[B_a^bal].                              (2)
```

Thus the load-bearing matching is equivalent to proving it for a packet with
a double zero at the singular endpoint, without introducing a separate large
ramp term.

## 4. Why this helps

The balanced ramp removes the rank-one endpoint source exactly inside the
same model-prime functional.  This is the finite analogue of subtracting the
continuous main term before estimating the post-main discrepancy, matching the
lesson of E72.58.

The next theorem is therefore:

```text
BAL-DOUBLE-ZERO:
For B_a^bal with B(0)=B'(0)=B(L)=0,
F_L[B_a^bal]=O_R(L^-R).
```

## 5. Status

```text
proved: balanced ramp exists whenever F_L[r_1] != 0;
proved: F_L[B_a]=F_L[B_a^bal];
open: prove BAL-DOUBLE-ZERO analytically.
```
