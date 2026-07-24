# E101.003 - Characteristic Jacobian factorization

## 1. Directional notation

For a positive full direction `Y`, write

```text
delta_Y P=Tr[adj(B_z)beta_z(Y)],
delta_Y chi=Tr[adj(K)Y].                             (1.1)
```

Set

```text
c_Y=Tr(GY)=delta_Y chi/chi_mu.                       (1.2)
```

Since `partial_mu B_z=-J`,

```text
partial_mu P=-Tr[adj(B_z)J].                         (1.3)
```

## 2. Polynomial identity

Define the Jacobian associated with the deformation `H_t=H_A-tY` by

```text
Jac_Y(P,chi)
 =(-delta_Y P)chi_mu
  -(partial_mu P)(-delta_Y chi).                     (2.1)
```

### Theorem 2.1

At every simple characteristic point,

```text
Jac_Y(P,chi)
 =-chi_mu Tr[adj(B_z)beta_z(Hor_K(Y))].              (2.2)
```

Equivalently, without the normalized adjugate,

```text
Jac_Y(P,chi)
 =-Tr{adj(B_z)[chi_mu beta_z(Y)
                +Tr(adj(K)Y)J]}.                    (2.3)
```

### Proof

By linearity and (1.2),

```text
chi_mu Tr[adj(B_z)beta_z(Hor_K(Y))]
 =chi_mu delta_Y P
  +delta_Y chi Tr[adj(B_z)J].                        (2.4)
```

Use (1.3), multiply by `-1`, and compare with (2.1).  This proves
(2.2)--(2.3). `QED`

## 3. Consequence for the logarithmic current

Dividing (2.2) by `P chi_mu` gives

```text
Jac_Y(P,chi)/(P chi_mu)
 =-Tr[adj(B_z)beta_z(Hor_K(Y))]/P.                   (3.1)
```

Thus the nonlinear Jacobian numerator from Phase 95 has one exact horizontal
cofactor factorization.  The factor `chi_mu` cancels before any estimate.

## 4. Status

```text
proved:
  polynomial characteristic-Jacobian factorization;
  normalized one-cofactor form;
  exact cancellation of the characteristic scale.
```

