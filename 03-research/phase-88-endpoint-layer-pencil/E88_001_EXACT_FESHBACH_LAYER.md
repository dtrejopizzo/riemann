# E88.001 - Exact Feshbach formula for the layer numerator

## 1. Block data

Let `P` be a spectral cluster projection at the arithmetic endpoint and put
`Q=I-P`.  For fixed `t`, decompose

```text
M_t=[A_t  B_t;
     B_t^* C_t]                                       (1.1)
```

on `ran P+ran Q`.  Decompose the source and the bordered row as

```text
b_t=(b_{P,t},b_{Q,t}),
h_z=(h_{P,z},h_{Q,z}).                                 (1.2)
```

Assume `C_t` is invertible and define

```text
F_t=A_t-B_t C_t^(-1)B_t^*,                            (1.3)

b_t^eff=b_{P,t}-B_t C_t^(-1)b_{Q,t},                  (1.4)

h_{t,z}^eff=h_{P,z}-h_{Q,z}C_t^(-1)B_t^*,             (1.5)

G_{t,z}^reg=1-h_{Q,z}C_t^(-1)b_{Q,t}.                 (1.6)
```

## 2. Exact numerator identity

### Theorem 2.1

For

```text
G_t(z)=1-h_z M_t^(-1)b_t,                             (2.1)
```

one has

```text
G_t(z)
 =G_{t,z}^reg
  -h_{t,z}^eff F_t^(-1)b_t^eff.                       (2.2)
```

### Proof

Solve the `Q` equation first:

```text
x_Q=C_t^(-1)(b_{Q,t}-B_t^*x_P).                       (2.3)
```

Substitution in the `P` equation gives

```text
F_t x_P=b_t^eff.                                      (2.4)
```

Insert (2.3)--(2.4) into `1-h_Px_P-h_Qx_Q`.  The regular terms give
(1.6), and the coefficient of `F_t^{-1}b_t^eff` is (1.5).  This proves
(2.2). `QED`

The formula is an identity before any norm estimate.  The singular behavior
is confined to `F_t^{-1}` on the selected cluster.

## 3. Bilateral layer numerator

For `u=s-1/2`, define

```text
Q_t(s)=G_t(iu)G_t(-iu).                               (3.1)
```

Both factors use the same effective pencil `F_t`; only the safe bordered rows
change.  Hence the layer is intrinsically bilateral and no separate estimate
of the two safe factors is required.

## 4. Status

```text
proved:
  exact Feshbach numerator identity;
  confinement of the singular deformation to the cluster pencil;

open:
  the scaled limit of every effective datum.
```

