# E73.091 - LOCK/COMP finite certificate

## 1. Purpose

E73.089 reduced `LOCAL-HWIN-5` to `LOCK-UNIF + COMP-UNIF`.
E73.090 shows that the resulting sufficient budget has finite slack.

This note removes the remaining informal words and states the exact finite certificate.

## 2. Rational Cauchy data

Let:

```text
C_x(t)=sum_n xi_n/(t-d_n)=P_x(t)/D_x(t),
D_x(t)=prod_n(t-d_n),
P_x(t)=sum_n xi_n prod_{m != n}(t-d_m).
```

Let `R_x=Div(P_x)` be the finite Cauchy root divisor.

For a critical node `gamma`, set:

```text
t_gamma=-gamma.
```

Then:

```text
|H_0(i gamma)| = |C_x(t_gamma)| = |P_x(t_gamma)|/|D_x(t_gamma)|.
```

## 3. Local split

For a natural-height off-line cluster `A`, the canonical local window is:

```text
Z_loc(A,L)=Z_lock(A,L) union Z_comp(A,L).
```

For `gamma in Z_lock`, choose a finite Cauchy root:

```text
r(gamma) in R_x
```

such that the interval between `t_gamma` and `r(gamma)` contains no pole `d_n`.

For `gamma in Z_comp`, no root assignment is required.

## 4. Explicit lock and companion weights

For locked nodes define:

```text
Delta_x(gamma)=|t_gamma-r(gamma)|,
M_x(gamma)=sup_{t between t_gamma and r(gamma)}
            sum_n |xi_n|/|t-d_n|^2.
```

For companion nodes define the exact rational residual:

```text
Q_x(gamma)=|P_x(t_gamma)|/|D_x(t_gamma)|.
```

The paired local nodal budget is:

```text
N_LC(A,L)
:=
sum_{gamma in Z_lock(A,L)}
  (Delta_x(gamma)M_x(gamma)+Delta_x(-gamma)M_x(-gamma))
+
sum_{gamma in Z_comp(A,L)}
  (Q_x(gamma)+Q_x(-gamma)).
```

All quantities are finite rational/algebraic functions of:

```text
d_n, xi_n, gamma, r(gamma).
```

No zero of `Xi` enters.

## 5. FAR row budget

Let `D_3(A,L)` be the FAR3 evaluation set.  Define:

```text
S_FAR(A,L):=sum_{gamma_k in D_3(A,L)} W_k(A,L),
```

where:

```text
W_k(A,L)=e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

## 6. LOCK-COMP-BUD

The finite certificate is:

```text
LOCK-COMP-BUD(A,L):
4(1+e^(sigma L))/sigma * S_FAR(A,L) * N_LC(A,L)
<= C L^-5.
```

## 7. Theorem

**Theorem 91.1.**  If `LOCK-COMP-BUD(A,L)` holds for a natural-height off-line cluster `A`, then
`LOCAL-HWIN-5(A,L)` holds.

*Proof.*  For `gamma in Z_lock`, Lemma 89.1 gives:

```text
|H_0(i gamma)| <= Delta_x(gamma)M_x(gamma).
```

For `gamma in Z_comp`, the exact rational identity gives:

```text
|H_0(i gamma)| = Q_x(gamma).
```

Thus:

```text
sum_{w in Z_loc(A,L)/+-} (|H_0(w)|+|H_0(-w)|)
<= N_LC(A,L).
```

By Lemma 89.2:

```text
|A_L(z_k,w)|+|B_L(z_k,w)| <= 4(1+e^(sigma L))/sigma.
```

Therefore:

```text
HWIN_k^loc
<= 4(1+e^(sigma L))/sigma * N_LC(A,L).
```

Multiplying by `W_k(A,L)` and summing over `D_3(A,L)` gives:

```text
sum_{gamma_k in D_3(A,L)} W_k(A,L)HWIN_k^loc
<=
4(1+e^(sigma L))/sigma * S_FAR(A,L) * N_LC(A,L).
```

The right side is at most `C L^-5` by `LOCK-COMP-BUD`.  This is `LOCAL-HWIN-5`. `□`

## 8. Why this advances the route

The local part is no longer:

```text
prove H_0 is small on a chosen window.
```

It is the explicit finite inequality:

```text
LOCK-COMP-BUD(A,L).
```

The only remaining analytic work inside this local block is to prove this finite inequality uniformly
from the geometry of the finite divisor `P_x` and the fixed local Cauchy window.  The exact HWIN
matrix no longer appears.

## 9. Updated chain

```text
LOCK-COMP-BUD
=> LOCAL-HWIN-5
=> FACTOR-MAIN-5
```

and, with the already separated mechanisms:

```text
FACTOR-MAIN-5 + TAIL-NODAL-5 + OUTSIDE-WINDOW-POLY
=> BUD-5/9
=> WCS
=> scalar WRL.
```
