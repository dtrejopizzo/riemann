# E91.001 - Exact line-response equation

## 1. Reduced operator

Let

```text
M_t v_t=kappa_t v_t,
v_t^Tv_t=1,                                           (1.1)
```

with `kappa_t` simple.  Set

```text
P_t=v_tv_t^T,
Q_t=I-P_t,
C_t=Q_t(M_t-kappa_t I)Q_t.                            (1.2)
```

Then `C_t` is invertible on `ran Q_t`.

## 2. Differentiated eigen-equation

Choose `v_t^T dot v_t=0`.  Differentiating (1.1) gives

```text
(M_t-kappa_t I)dot v_t
 =-(dot M_t-dot kappa_t I)v_t.                        (2.1)
```

Projection by `Q_t` removes the scalar term.  Since

```text
dot M_t=-H_P^in-dot mu_t I,                           (2.2)
```

one obtains the exact equation

```text
C_t dot v_t=Q_t H_P^in v_t.                           (2.3)
```

Consequently,

```text
dot v_t=C_t^(-1)Q_t H_P^in v_t.                      (2.4)
```

Equation (2.4) is equivalent to the reduced-resolvent formula of E90.003.

## 3. Projective observable

For any safe base point `z_*`,

```text
J_t(z,z_*)
 =[h_z dot v_t]/[h_zv_t]
  -[h_(z_*) dot v_t]/[h_(z_*)v_t].                   (3.1)
```

Thus the entire projective current is the safe reduced response to the single
source

```text
f_t=Q_t H_P^in v_t.                                  (3.2)
```

## 4. Status

```text
proved:
  exact reduced line-response equation;
  exact identification of its source;

open:
  inverse-free construction or direct safe control of its solution.
```

