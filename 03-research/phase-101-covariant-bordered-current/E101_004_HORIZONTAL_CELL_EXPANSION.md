# E101.004 - Horizontal prime-cell expansion

## 1. Linear decomposition

Write the finite prime operator as

```text
H_P=sum_(2<=n<=exp L)
     Lambda(n)n^(-1/2)Q_(log n).                    (1.1)
```

For fixed `t`, the projection `Hor_(K_t)` is linear.  Hence

```text
Hor_(K_t)(H_P)
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)Hor_(K_t)(Q_(log n)).            (1.2)
```

Define the level response of one cell by

```text
c_t(y)=Tr[G_tQ_y],                                   (1.3)
```

so that

```text
Hor_(K_t)(Q_y)=Q_y+c_t(y)I.                          (1.4)
```

The complete level velocity is recovered by summation:

```text
dot mu_t
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)c_t(log n).                      (1.5)
```

## 2. Horizontal response kernel

Define

```text
HR_t(z;y)
 =Tr{adj(B_z)[beta_z(Q_y)+c_t(y)J]}/P(t,mu_t,z).
                                                               (2.1)
```

Then E101.002 gives the exact cell expansion

```text
d/dt log P(t,mu_t,z)
 =-sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)HR_t(z;log n).                  (2.2)
```

## 3. Identification with the earlier response

Using

```text
gamma_t(z)=-Tr[adj(B_z)J]/P(t,mu_t,z),               (3.1)
```

equation (2.1) becomes

```text
HR_t(z;y)
 =delta_(Q_y)P/P-gamma_t(z)c_t(y).                  (3.2)
```

This is exactly the constrained response `R_t(z;y)` of E96.003.  Therefore
the horizontal cell expansion is not a new hypothesis; it is the tangent
geometry hidden in the characteristic Jacobian.

## 4. Status

```text
proved:
  exact horizontal von Mangoldt expansion;
  cellwise decomposition of the level velocity;
  equivalence with the Phase 96 response kernel.
```

