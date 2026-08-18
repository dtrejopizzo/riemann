# E95.001 - Two-parameter algebraic lift

## 1. Full characteristic curve

Let

```text
H_t=H_A-tH_P                                         (1.1)
```

be the finite arithmetic deformation and define

```text
chi(t,mu)=det(H_t-mu I).                              (1.2)
```

The selected finite level is a real branch `mu_t` satisfying

```text
chi(t,mu_t)=0.                                        (1.3)
```

At a simple level,

```text
partial_mu chi(t,mu_t) !=0.                           (1.4)
```

## 2. Bordered polynomial before level selection

Delete the prescribed boundary modes from `H_t-mu I` to obtain

```text
M(t,mu),
b(t).                                                 (2.1)
```

Define the global bordered determinant

```text
P(t,mu,z)
 =det[[M(t,mu),b(t)],
      [h_z,1]].                                       (2.2)
```

This is the numerator `N` of E94.001.  The polynomial two-generator numerator
of E94.003 differs from it by a scalar independent of `z`, so both define the
same projective safe profile.  For fixed finite section, `P` is rational in
`z` with coefficients polynomial in `mu` and polynomial in `t`, because its
bordered matrix is affine in `(t,mu)`.

The physical numerator is the pullback

```text
P_t^phys(z)=P(t,mu_t,z).                              (2.3)
```

## 3. Independence from eigenvectors

Equations (1.2) and (2.2) use only the full Gamma--prime matrix, its boundary
column and the mesh row.  Neither the selected eigenvector nor a Riesz
projection enters the construction.

## 4. Status

```text
proved:
  algebraic two-parameter lift of the full characteristic and bordered
  numerator;

open:
  cofinal identification of their characteristic-curve current.
```
