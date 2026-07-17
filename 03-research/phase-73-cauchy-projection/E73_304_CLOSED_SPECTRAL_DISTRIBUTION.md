# E73.304 - Closed spectral distribution

Date: 2026-07-16.

## 1. Purpose

E73.303 rewrites the final frequency endpoint as

```text
<T_eta,W>=O_M(L^(-M)),
```

where

```text
T_eta=sum c_omega delta_omega+i sum l_omega delta'_omega.
```

This note removes the coefficient-map layer and gives `T_eta` directly from
the CCM cell formula.

## 2. Closed formula

Let the mesh frequencies be

```text
d_j=2*pi*n_j/L,
```

let `r_j=q_a(j)` be the Cauchy row, and let `eta=R_wxi_L`.  Then

```text
T_{a,w,L}
=T^diag+T^off,
```

with diagonal part

```text
T^diag
=sum_b r_b eta_b(delta_{d_b}+delta_{-d_b})
 -(i/L)sum_b r_b eta_b(delta'_{d_b}+delta'_{-d_b}),
```

and off-diagonal part

```text
T^off
=sum_{j != b} r_j eta_b /(2 i pi(n_b-n_j))
  [delta_{d_j}-delta_{-d_j}-delta_{d_b}+delta_{-d_b}].
```

This is an exact finite distribution identity.  It uses no pseudoinverse,
least-squares source coordinate, or fitted quotient.

## 3. Pairing with the symbol

Since

```text
<delta'_omega,W>=-W'(omega)=-iV_omega,
```

the diagonal derivative term contributes

```text
-(1/L)sum_b r_b eta_b(V_{d_b}+V_{-d_b}).
```

Together with the diagonal mass term, this gives

```text
sum_b r_b eta_b[(W_{d_b}+W_{-d_b})-(V_{d_b}+V_{-d_b})/L].
```

The off-diagonal part gives

```text
sum_{j != b} r_j eta_b
[(W_{d_j}-W_{-d_j})-(W_{d_b}-W_{-d_b})]
/(2 i pi(n_b-n_j)).
```

Therefore `<T_eta,W>` is exactly the E73.290 kernel:

```text
sum_b eta_b K_b,
```

where

```text
K_b
=r_b U^even_b
 +sum_{j != b} r_j(W^odd_j-W^odd_b)/(2 i pi(n_b-n_j)).
```

Thus:

```text
closed spectral distribution form
<=> K-DIAGOFF
<=> TS-DIV
<=> FINAL-ETA-ADJ.
```

## 4. Numerical certification

`E73_304_closed_spectral_distribution_probe.py` compares the closed
distribution against `coefficient_maps` and then pairs both with `W`.

Representative output:

```text
 lam      L gamma row mapErrB centerErrB centerB closedB
  12    4.970  14.13   0  -430.82    -430.82   -21.27   -21.27
  16    5.545  21.02   0  -403.27    -403.27   -18.21   -18.21
  20    5.991  21.02   1  -385.84    -385.84   -18.81   -18.81
```

Both the map identity and the paired scalar agree at numerical floor.

## 5. Consequence

The current endpoint can be stated without coefficient bookkeeping:

```text
Closed Spectral Distribution Divisibility.
For every admissible row/window and every M,

<T^diag_{a,w,L}+T^off_{a,w,L}, W_L>
=O_M(L^(-M)).
```

The theorem is still open.  The gain is that every term is now an explicit
finite distribution built directly from:

```text
1. the Cauchy row r_j;
2. the projected eigenline eta_b=(R_wxi_L)_b;
3. the mesh differences n_b-n_j;
4. the single closed Gamma-prime symbol W_L.
```

## 6. Status

```text
proved: closed cell formula for T_eta;
proved: closed T pairing equals K-DIAGOFF and the final scalar;
open: prove <T_eta,W_L>=O_M(L^(-M)) from Gamma-prime eigenline structure.
```

