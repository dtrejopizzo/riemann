# E73.182 - Closed-series archimedean certificate

Date: 2026-07-14.

## 1. Purpose

E73.181 reduced the current endpoint to the explicit-formula residual

```text
A_L[B_{j,w}] - P_L[B_{j,w}] - principal_{j,w}.
```

The weak point of the numerical certificate was the direct quadrature in
`A_L[B]`.  This note replaces it by a closed exponential-series evaluation
for the finite packet

```text
B(y)=q_j Q_L(y)xi_L.
```

## 2. Finite packet expansion

Since

```text
Q_mn(y)
= 2(1-y/L)cos(d_ny),                         m=n,
= [sin(d_my)-sin(d_ny)]/[pi(n-m)],           m!=n,
```

every packet has the exact finite form

```text
B(y)=sum_omega c_omega e^(i omega y)
    + y sum_omega l_omega e^(i omega y).       (1)
```

The frequencies are contained in the pole mesh `{d_n}`.

## 3. Closed primitives

For `lambda in C`,

```text
I(lambda)=int_0^L e^(lambda y)dy
         = [e^(lambda L)-1]/lambda,

J(lambda)=int_0^L y e^(lambda y)dy
         = [e^(lambda L)(lambda L-1)+1]/lambda^2,
```

with the continuous values `I(0)=L`, `J(0)=L^2/2`.

Thus every integral

```text
int_0^L e^(alpha y)B(y)dy
```

is a finite sum of `I(alpha+i omega)` and `J(alpha+i omega)`.

## 4. The `WR` series

The regularized term uses

```text
1/(2sinh y)=sum_{r>=0} e^(-(2r+1)y).
```

Therefore

```text
int_0^L [e^(y/2)B(y)-B(0)]/[2sinh y]dy
= sum_{r>=0}
  { int_0^L e^(-(2r+1/2)y)B(y)dy
    - B(0)int_0^L e^(-(2r+1)y)dy }.             (2)
```

Each summand is closed by §3.  The subtraction by `B(0)` makes the series
convergent at `y=0`.  The tail is controlled from the Taylor expansion

```text
e^(y/2)B(y)-B(0)=c_1y+c_2y^2+O(y^3),

c_1=B'(0)+B(0)/2,
c_2=B''(0)/2+B'(0)/2+B(0)/8.
```

For `a_r=2r+1`,

```text
int_0^infty y e^(-a_ry)dy=a_r^-2,
int_0^infty y^2e^(-a_ry)dy=2a_r^-3.
```

Hence the tail after `R` terms is accelerated by adding

```text
c_1 sum_{r>=R}(2r+1)^-2
+2c_2 sum_{r>=R}(2r+1)^-3,
```

where

```text
sum_{r>=R}(2r+1)^-2 = (1/4)psi_1(R+1/2),
sum_{r>=R}(2r+1)^-3 = -(1/16)psi_2(R+1/2).
```

The remaining tail is `O(sum_{r>=R}(2r+1)^-4)` times an explicit bound on
the third local coefficient of `e^(y/2)B(y)`.

Thus `A_L[B]` can be evaluated without adaptive quadrature.

## 5. Status

```text
proved:   finite mode expansion (1);
proved:   closed primitives for W02 and each WR-series term;
proved:   first two Taylor tail accelerants for the WR series;
verified: closed series matches the CCM matrix and direct quadrature;
open:     write the explicit third-derivative tail bound and then use this
          certificate inside SCRCE-principal-explicit.
```
