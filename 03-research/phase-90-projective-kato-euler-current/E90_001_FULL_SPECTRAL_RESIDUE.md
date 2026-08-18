# E90.001 - Full spectral residue

## 1. Exact decomposition

Let `M_t` be a real symmetric invertible finite matrix with orthonormal
eigenpairs

```text
M_t v_(j,t)=kappa_(j,t)v_(j,t).                       (1.1)
```

For a fixed bordered row `h_z` and source `b_t`, put

```text
G_t(z)=1-h_z M_t^(-1)b_t.                             (1.2)
```

Then

```text
G_t(z)
 =1-sum_j
   [(h_z v_(j,t))(v_(j,t)^T b_t)]/kappa_(j,t).        (1.3)
```

This follows immediately from the spectral resolution of `M_t^(-1)`.

## 2. One-line dominance

Select a simple line `v_t` with eigenvalue `kappa_t` and write

```text
a_t(z)=(h_zv_t)(v_t^Tb_t),                           (2.1)

R_t(z)
 =1-sum_(j not equal r)
   [(h_zv_(j,t))(v_(j,t)^Tb_t)]/kappa_(j,t).          (2.2)
```

Thus

```text
G_t(z)=-a_t(z)/kappa_t+R_t(z).                        (2.3)
```

### Theorem 2.1

On a safe domain `V`, suppose

```text
inf_(z in V)|a_t(z)|>0,

sup_(z in V)|kappa_t R_t(z)/a_t(z)|->0.              (2.4)
```

Then, for every safe base point `z_*`,

```text
G_t(z)/G_t(z_*)
 -[h_zv_t]/[h_(z_*)v_t] ->0                          (2.5)
```

locally uniformly on `V`.  The same conclusion holds after one safe-variable
derivative.

### Proof

Factor (2.3) exactly as in E89.001.  The eigenvalue and the source overlap
cancel from the normalized ratio.  Uniform convergence followed by Cauchy's
formula gives the derivative assertion. `QED`

## 3. Full-space dominance target

The sufficient estimate is

```text
DOM-M:
sup_(z in K)|kappa_t R_t(z)/a_t(z)|->0               (3.1)
```

on every safe compact set, uniformly across a matched endpoint layer.  It is
the full-space counterpart of `DOM-E`; neither estimate is proved here.

## 4. Status

```text
proved:
  exact full spectral residue;
  full-space projective dominance theorem;

open:
  DOM-M and its matched-layer uniformity.
```

