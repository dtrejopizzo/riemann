# E73.037 - Hermite kernel bound

## 1. Purpose

E73.036 reduces the remaining endpoint to the positive product budget

```text
PFD:
e^(alpha L) sum_k ||h_A(k)||_Herm
|1-exp(i gamma_k L)| |C_x(i gamma_k)|
<= L^B.
```

This document removes the matrix inverse from the geometric factor `||h_A(k)||_Herm`.

## 2. Setup

Let the off-line Hermite cluster be centered at

```text
a = alpha+i tau, alpha>0,
```

and let the critical node be

```text
k=i gamma.
```

Use the E73.027 variable

```text
w=(s+a)^(-1),       w0=(2a)^(-1),       beta=k-a.
```

The function whose Hermite jets are matched is

```text
f_beta(w)=w/(1+beta w).
```

It has one pole at

```text
w_*=-1/beta.
```

The Hermite coefficient vector `h_A(k)=(h_0,...,h_{m-1})` is encoded by

```text
P_m(w)=sum_{p=0}^{m-1} h_p w^(p+1)
```

whose Taylor expansion at `w0` agrees with `f_beta` through order `m-1`.

Since `w0 != 0`, this is equivalent to writing

```text
P_m(w)=w R_m(w),       R_m(w)=sum_{p=0}^{m-1} h_p w^p,
```

and requiring `R_m` to match

```text
g_beta(w)=1/(1+beta w)
```

through order `m-1` at `w0`.

## 3. Taylor-Cauchy bound

Let

```text
R < |w_*-w0|.
```

Define

```text
M_R := sup_{|w-w0|=R} |g_beta(w)|.
```

Then

```text
g_beta(w) = sum_{r>=0} c_r (w-w0)^r
```

with

```text
|c_r| <= M_R/R^r.
```

The Hermite quotient polynomial is

```text
R_m(w)=sum_{r=0}^{m-1} c_r(w-w0)^r.
```

Expanding `(w-w0)^r` in powers of `w`,

```text
(w-w0)^r = sum_{j=0}^r binom(r,j)(-w0)^(r-j) w^j.
```

The coefficients of `w^p` obey the absolute bound

```text
|h_p|
<= sum_{r=p}^{m-1} binom(r,p)|w0|^(r-p) M_R/R^r.
```

Consequently

```text
||h_A(k)||_Herm
<= M_R H_m(w0,R),
```

where

```text
H_m(w0,R)
:= sum_{p=0}^{m-1} 1/p!
   sum_{r=p}^{m-1} binom(r,p)|w0|^(r-p) R^(-r).
```

This is a completely explicit scalar upper bound.

## 4. A canonical radius

Take

```text
R = theta |w_*-w0|,       0<theta<1.
```

On the circle `|w-w0|=R`,

```text
|1+beta w|
= |beta||w-w_*|
>= |beta|(1-theta)|w_*-w0|.
```

Thus

```text
M_R
<= 1/(|beta|(1-theta)|w_*-w0|).
```

This gives the explicit bound

```text
||h_A(k)||_Herm
<=
[1/( |beta|(1-theta)D )]
H_m(w0,theta D),

D:=|w_*-w0|.
```

## 5. Natural-height simplification

For critical `k=i gamma`,

```text
beta = i gamma - (alpha+i tau) = -alpha+i(gamma-tau).
```

The reflected pole distance is

```text
D
= |-1/beta - 1/(2a)|
= |-(2a+beta)/(2a beta)|
= |a+k|/(2|a||k-a|).
```

Therefore the geometry is bad only when `a+k` is small, i.e. when the reflected critical node is
close to the off-line center.  It is not bad merely because an off-line cluster has multiplicity.

## 6. Consequence for PFD

For any fixed `theta in (0,1)`, `PFD` follows from the scalar inequality

```text
e^(alpha L) sum_k
G_theta,m(a,k)
|1-exp(i gamma_k L)| |C_x(i gamma_k)|
<= L^B,
```

where

```text
G_theta,m(a,k)
:=
[(|w0| + theta D)/( |beta|(1-theta)D )]
H_m(w0,theta D).
```

The remaining arithmetical content is now entirely in the factor

```text
|1-exp(i gamma L)| |C_x(i gamma)|.
```

## 7. Status

```text
proved: explicit Taylor-Cauchy upper bound for the confluent Hermite kernel;
reduced: PFD to a scalar positive sum with no Cauchy matrix inverse;
remaining: prove the product divisor estimate for the finite Cauchy transform.
```
