# E101.002 - Bordered horizontal lift

## 1. Border restriction

Let

```text
B_z(t,mu)=[[M(t,mu),b(t)],
           [h_z,1]],
P(t,mu,z)=det B_z(t,mu).                              (1.1)
```

Denote by `beta_z(Y)` the linear bordered direction induced by a full matrix
direction `Y`.  The safe row and the bordered scalar are fixed under this
variation.  A scalar full direction induces

```text
beta_z(I)=J=[[I_inner,0],[0,0]].                     (1.2)
```

The dependence on `mu` is therefore

```text
partial_mu B_z=-J.                                   (1.3)
```

## 2. Physical deformation

Let

```text
H_t=H_A-tH_P,
chi(t,mu_t)=0.                                       (2.1)
```

At a simple level, E100.003 gives

```text
dot mu_t=Tr(G_tH_P).                                 (2.2)
```

Differentiate the bordered matrix along the characteristic curve:

```text
d/dt B_z(t,mu_t)
 =-beta_z(H_P)-dot mu_t J
 =-beta_z(Hor_(K_t)(H_P)).                           (2.3)
```

The last equality follows from the linearity of `beta_z`, (1.2) and
E101.001(2.1).

## 3. Cofactor current

Where `P(t,mu_t,z)` is nonzero, the singular-safe determinant derivative gives

```text
d/dt log P(t,mu_t,z)
 =-Tr[adj(B_z)beta_z(Hor_(K_t)(H_P))]/P(t,mu_t,z).   (3.1)
```

Equation (3.1) is the complete derivative.  It already contains both the
fixed-level prime response and the motion of the selected level.

## 4. Status

```text
proved:
  exact horizontal lift to the bordered matrix;
  one-cofactor formula for the physical current.
```

