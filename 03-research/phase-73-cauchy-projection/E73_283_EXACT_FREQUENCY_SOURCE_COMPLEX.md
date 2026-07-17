# E73.283 - Exact frequency source complex

Date: 2026-07-14.

## 1. Purpose

E73.281--E73.282 show that the rational `d`-space source coordinates are not
safe for the scalar APR theorem unless they are made symbolic and exact.  The
least-squares source basis creates scalar contamination much larger than the
APR center.

This note identifies the exact finite source space already present in the
construction: the frequency packet basis of `Q_y`.  Unlike the rational
`d`-basis, this basis is exact by definition of the CCM cells.

## 2. Exact cell frequencies

For

```text
d_n=2pi n/L,
```

the finite CCM cell functions are:

```text
q_nn(y)=2(1-y/L)cos(d_n y),
```

and for `m != n`,

```text
q_mn(y)=(sin(d_m y)-sin(d_n y))/(pi(n-m)).
```

Therefore every matrix cell belongs to the finite frequency source space

```text
F_L
= span{ e^(i d_n y), e^(-i d_n y),
        y e^(i d_n y), y e^(-i d_n y)
        : n in I_L }.
```

The `y e^(±id_n y)` terms occur only from diagonal cells through
`(1-y/L)cos(d_n y)`.

## 3. Exact packet map

For any mesh vector `eta` and Cauchy row `q_a`, define

```text
B_{a,eta}(y)=q_a Q_y eta.
```

Then there is an exact coefficient vector

```text
C_{a}(eta)=(c_omega(eta),l_omega(eta))_{omega in ±d(I_L)}
```

such that

```text
B_{a,eta}(y)
=sum_omega c_omega(eta)e^(iomega y)
 +y sum_omega l_omega(eta)e^(iomega y).          (1)
```

No fitting is involved.  The coefficients are explicit linear functionals of
`eta`.

## 4. Exact scalar functional

The Gamma-prime center is the exact linear functional

```text
F_L[B]
=sum_omega c_omega W_omega
 +sum_omega l_omega V_omega,                     (2)
```

where

```text
W_omega = W_omega^A-W_omega^P,
V_omega = V_omega^A-V_omega^P.
```

E73.268 verifies and records:

```text
F_L[B_{a,R_wxi_L}]
=q_aH_LR_wxi_L.
```

Thus the exact source complex should be written in frequency coordinates:

```text
eta  --C_a-->  F_L  --F_L--> C.
```

The APR theorem is:

```text
F_L C_a(R_wxi_L)=O_M(L^(-M)).                    (APR-FREQ)
```

This is the same theorem as `CELL-CTM`, `COEFF-ETA`, `SECOND-ABEL`, and
`APR-U4`, but now stated in an exact finite source basis.

## 5. Relation to the failed rational source basis

The rational `d`-space basis tried to represent rows such as

```text
rho=q_aH_LR_w
```

as functions of the mesh variable `d`.  That representation is ill-conditioned
and only approximate in the current implementation.  E73.281 shows that this
is fatal because generated rows should pair exactly zero, while coordinate
errors pair much larger than the APR scalar.

The frequency basis avoids this problem:

```text
1. Q_y is exactly frequency-finite;
2. C_a(eta) is obtained by direct coefficient assembly;
3. F_L is the exact Gamma-prime coefficient functional;
4. no quotient or least-squares coordinate map is needed.
```

## 6. What remains

This does not prove Omega7.  It gives the correct exact finite identity:

```text
APR-FREQ:
sum_omega c_omega(R_wxi_L)W_omega
+sum_omega l_omega(R_wxi_L)V_omega
=O_M(L^(-M)).
```

The missing theorem is now a signed frequency divisibility theorem:

```text
FREQ-DIV:
The coefficient vector C_a(R_wxi_L) lies in the rapid kernel of the
Gamma-prime weight row (W,V), uniformly in admissible Cauchy rows.
```

This is not a coordinate artifact; all objects are finite and exact.

## 7. Why this is better than EXACT-SRC in rational coordinates

`EXACT-SRC` asked for a minimal symbolic partial-fraction basis
`S_L^ex`.  E73.283 identifies the canonical choice:

```text
S_L^ex = F_L,
```

the finite exponential-linear frequency space of the CCM cells.

In this basis:

```text
rho_j(w)xi_L
```

is not represented by a fitted row in `d`; it is represented by the exact
packet

```text
B_{j,w}(y)=q_jQ_yR_wxi_L.
```

Therefore the proof should attack the frequency identity directly, not return
to rational source fitting.

## 8. Status

```text
proved: Q_y packets live in the exact finite frequency source space F_L;
proved earlier: frequency center equals q_aH_LR_wxi_L;
rejected: rational least-squares source basis as proof-facing coordinate;
current endpoint: prove FREQ-DIV / APR-FREQ in exact frequency coordinates.
```
