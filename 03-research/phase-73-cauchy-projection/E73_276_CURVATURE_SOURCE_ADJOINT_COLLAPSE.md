# E73.276 - Curvature source adjoint collapse

Date: 2026-07-14.

## 1. Purpose

E73.274--E73.275 leave one possible refinement: instead of projecting mesh
rows, build the APR source in balanced second-Abel curvature coordinates.  This
note records the exact collapse of that idea.

## 2. Coefficient adjoint source

For fixed `q_a`, define

```text
B_a(y)=q_aQ_y eta
     =sum_omega c_omega(eta)e^(iomega y)
      +y sum_omega l_omega(eta)e^(iomega y).
```

Write

```text
c_omega(eta)=u_omega eta,
l_omega(eta)=v_omega eta.
```

Then the coefficient form of the scalar center is

```text
F_L[B_a]
=sum c_omega W_omega+sum l_omega V_omega
=left(sum W_omega u_omega+sum V_omega v_omega right) eta.
```

Thus the adjoint source row is

```text
Src_a=sum W_omega u_omega+sum V_omega v_omega.   (1)
```

## 3. Collapse

By the definition of the finite Gamma-prime matrix,

```text
F_L[q_aQ_y eta]=q_aH_L eta.
```

Since this holds for every `eta`, the source row in (1) is exactly

```text
Src_a=q_aH_L.                                   (2)
```

The balanced second-Abel curvature quotient gives the same row, because the
balanced ramp is neutral:

```text
F_L[r_*]=0.
```

Therefore curvature coordinates are an exact representation of the APR source,
not a new mechanism.

## 4. Correct APR source

The principal residual row is obtained only after Cauchy-plane subtraction:

```text
rho_a=q_aH_LR_w
     =q_aH_L-A_aQ_w,
A=Q_wH_LQ_w^*(Q_wQ_w^*)^(-1).                  (3)
```

Combining (2) and (3), APR-U4 is again:

```text
rho_axi_L=O_M(L^-M).
```

Any coefficient/source-coordinate proof must therefore separate `rho_a` into

```text
rho_a=Y_{a,w}^*E_L+r_{a,w},
```

with a fixed symbolic primitive and a residual class whose pairing is
directly estimated.  Simply changing coordinates from rows to curvature
weights cannot change the scalar theorem.

## 5. Status

```text
proved: curvature coefficient adjoint source equals q_aH_L;
proved: balanced second-Abel source gives the same row;
rejected: source-coordinate curvature rewrite as independent proof source;
open: split the APR row into symbolic coborder plus named residual slots.
```

