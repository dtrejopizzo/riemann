# E90.002 - Exact prime-driven Kato current

## 1. Spectral-line derivative

Let `v_t` be a differentiable normalized simple eigenvector of

```text
M_t=H_A^in-tH_P^in-mu_t I,                            (1.1)

M_t v_t=kappa_t v_t.                                 (1.2)
```

Choose the parallel gauge `v_t^T dot v_t=0`.  If `(kappa_(q,t),q_t)` are the
other orthonormal eigenpairs, then

```text
dot v_t
 =sum_q q_t
   [q_t^T dot M_t v_t]/(kappa_t-kappa_(q,t)).         (1.3)
```

Since

```text
dot M_t=-H_P^in-dot mu_t I                           (1.4)
```

and `q_t^Tv_t=0`,

```text
q_t^T dot M_t v_t=-q_t^T H_P^in v_t.                 (1.5)
```

Therefore

```text
dot v_t
 =-sum_q q_t
   [q_t^T H_P^in v_t]/(kappa_t-kappa_(q,t)).          (1.6)
```

Equation (1.6) is exact.  The moving scalar `mu_t` changes the spectral
eigenvalues but does not rotate the eigenline.

## 2. Base-point-subtracted profile current

Define

```text
phi_t(z)=h_zv_t,

J_t(z,z_*)
 =partial_t log[phi_t(z)/phi_t(z_*)].                 (2.1)
```

Where both profiles are nonzero, (1.6) gives

```text
J_t(z,z_*)
 =-sum_q Delta_(t,q)(z,z_*)
   [q_t^T H_P^in v_t]/(kappa_t-kappa_(q,t)),          (2.2)

Delta_(t,q)(z,z_*)
 =[h_zq_t]/[h_zv_t]
  -[h_(z_*)q_t]/[h_(z_*)v_t].                        (2.3)
```

Every factor in (2.2) is invariant under rescaling of the chosen resonant
representative.  The current is therefore intrinsically projective.

## 3. What has disappeared

The exact formula contains neither

```text
dot mu_t,
dot kappa_t,
v_t^Tb_t,
1/kappa_t.                                           (3.1)
```

These quantities remain relevant to `DOM-M`, but not to the arithmetic
identity after dominance.  The surviving operator input is precisely
`H_P^in`.

## 4. Status

```text
proved:
  exact cancellation of the scalar eigenvalue motion from line rotation;
  exact base-point-subtracted Kato current;

open:
  cofinal control of the gap-weighted sum in (2.2).
```

