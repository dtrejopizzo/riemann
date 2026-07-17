# E73.183 - WR Taylor-tail bound

Date: 2026-07-14.

## 1. Purpose

E73.182 replaced adaptive quadrature in the archimedean functional by a
closed exponential series.  The remaining analytic bookkeeping is the tail
of

```text
int_0^L [e^(y/2)B(y)-B(0)]/[2sinh y]dy.
```

This note makes the tail bound explicit.

## 2. Taylor remainder

Let

```text
F(y)=e^(y/2)B(y)-B(0).
```

After subtracting the first two local terms,

```text
F(y)=c_1y+c_2y^2+R_3(y),
```

where

```text
c_1=B'(0)+B(0)/2,
c_2=B''(0)/2+B'(0)/2+B(0)/8.
```

If

```text
M_3 >= sup_{0<=y<=L} |F'''(y)|,
```

then Taylor's theorem gives

```text
|R_3(y)| <= M_3 y^3/6.
```

For `a_r=2r+1`,

```text
int_0^infty y^3 e^(-a_ry)dy = 6a_r^-4.
```

Therefore the omitted accelerated tail after `R` terms satisfies

```text
|Tail_R| <= M_3 sum_{r>=R}(2r+1)^-4.              (1)
```

The sum is closed:

```text
sum_{r>=R}(2r+1)^-4 = psi_3(R+1/2)/96.
```

## 3. Finite computable `M_3`

For the finite mode expansion

```text
B(y)=sum_omega c_omega e^(i omega y)
    + y sum_omega l_omega e^(i omega y),
```

one may use the explicit bound

```text
||B^(k)||_infty
<= sum_omega |c_omega||omega|^k
 + sum_omega |l_omega|(k|omega|^(k-1)+L|omega|^k).
```

Thus

```text
M_3
<= e^(L/2)(
     ||B'''||_infty
   + 3/2 ||B''||_infty
   + 3/4 ||B'||_infty
   + 1/8 ||B||_infty).
```

This makes (1) a finite, explicit, machine-checkable inequality.

## 4. Status

```text
proved:   closed WR tail bound after two Taylor accelerants;
verified: actual numerical tail is below the bound in tested rows;
open:     the bound is conservative, so proof-level residual certification
          should either increase Taylor order or exploit cancellations in
          the finite mode coefficients.
```
