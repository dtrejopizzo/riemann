# E72.35 -- Bordered cohomology equation for Mellin divisibility

**Date:** 2026-07-08.
**Role:** turn the corrected cofactor criterion E72.34 into the actual finite equation that must be
solved.

## 0. Corrected target

We need to prove, without evaluating finite roots, that

```text
M_x(s;z)=<v_{x,s},Tcal_x(z)k_x>
```

is divisible by

```text
P_x(z)=-det B_x(z).
```

E72.34 shows that a sufficient root-free certificate is:

```text
M_x(s;z)=a_x(s;z)^TB_x(z)b_x(s;z),
B_x(z)b_x(s;z)=P_x(z)c_x(s;z).                  (BC)
```

The second line supplies the explicit `P_x` factor.

## 1. The adjugate tautology

For any holomorphic `c_x`, the choice

```text
b_x(z)=-adj(B_x(z))c_x(z)
```

gives

```text
B_x(z)b_x(z)=P_x(z)c_x(z).
```

But then

```text
a_x^TB_xb_x=P_x a_x^Tc_x.
```

Matching `M_x` requires

```text
a_x^Tc_x=M_x/P_x,
```

which is exactly the unknown divisibility quotient. Therefore the adjugate construction is
tautological unless `a_x` and `c_x` are fixed independently by the CCM/prolate structure.

## 2. Non-tautological bordered equation

A non-circular proof must specify `a_x,b_x,c_x` from:

```text
D_x, xi_x, k_x, C_x, Tcal_x(z), and the Cauchy test s,
```

before knowing whether `M_x/P_x` is holomorphic.

Equivalently, it must solve:

```text
B_x(z)b_x(s;z)=P_x(z)c_x(s;z),                  (E1)
a_x(s;z)^TB_x(z)b_x(s;z)=<v_{x,s},Tcal_x(z)k_x>.(E2)
```

The second equation says that the scalar WRL Mellin current is a bordered coboundary; the first says
that this coboundary lies in the determinant ideal.

## 3. Reduction to a finite interpolation obstruction

Assume `P_x` has simple zeros `r_j`. Then `(E1)-(E2)` imply

```text
M_x(s;r_j)=0      for all j.                    (I)
```

Conversely, if `(I)` holds, then `M_x/P_x` is holomorphic and one can solve `(E1)-(E2)` by adjugate
methods. Thus the cohomology equation is equivalent to finite interpolation vanishing.

Therefore:

```text
bordered cohomology has content only if it proves (I) structurally.
```

## 4. The structural form needed

Let `c_j` be a right null vector of `B_x(r_j)`. From the definition of `B_x`,

```text
B_x(r_j)[u_j;w_j]=0
```

means:

```text
xi_x^T w_j = 0,
u_j 1_x + (r_jI-D_x)w_j = 0.
```

Thus, up to scale,

```text
w_j = (r_jI-D_x)^(-1)1_x,
```

and the zero condition is exactly

```text
xi_x^T(r_jI-D_x)^(-1)1_x = 0.
```

That is the finite Weyl divisor equation.

The divisibility condition `(I)` is:

```text
<v_{x,s},Tcal_x(r_j)k_x>=0
```

for every Weyl-root resolvent vector.

This means `Tcal_x(r_j)k_x` must lie in the annihilator of the Weyl-Feshbach test vector `v_{x,s}` at
all finite spectral points.

## 5. Required finite identity

The exact structural identity needed is:

```text
Tcal_x(z)k_x
 = U_x(s;z)(r_z) + P_x(z)W_x(s;z),              (TI)
```

where `r_z=(zI-D_x)^(-1)1_x`, and `U_x` is an operator whose image is annihilated by `v_{x,s}` whenever

```text
xi_x^T r_z=0.
```

Equivalently, there must be a finite bilinear concomitant `J_x` such that

```text
<v_{x,s},Tcal_x(z)k_x>
 = J_x(s;z) xi_x^T(zI-D_x)^(-1)1_x
   + P_x(z)E_x(s;z).                            (MSD-sharp)
```

Since

```text
xi_x^T(zI-D_x)^(-1)1_x = P_x(z)/Q_x(z),
```

this becomes:

```text
M_x(s;z)
 = J_x(s;z) P_x(z)/Q_x(z)+P_x(z)E_x(s;z).
```

To avoid poles at the mesh, `J_x/Q_x` must itself be regular after the finite cell construction.

## 6. Status

```text
proved: bordered cohomology is equivalent to finite interpolation vanishing;
proved: the needed vanishing is equivalent to the sharp concomitant identity (MSD-sharp);
open:   construct the concomitant J_x from Tcal_x, C_x, and the CCM eigenvector equation.
```

The next step is to test whether `M_x` is a multiple of the Weyl function

```text
m_x(z)=P_x(z)/Q_x(z)
```

rather than directly of `P_x`. This is the natural finite spectral factor visible from the bordered
pencil.
