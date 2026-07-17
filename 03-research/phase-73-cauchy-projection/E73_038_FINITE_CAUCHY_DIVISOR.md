# E73.038 - Finite Cauchy divisor identity

## 1. Purpose

E73.035 introduced `FINROOT` as the observation that

```text
C_x(i gamma)
```

is small when the critical height is close to a zero of the finite Cauchy transform.  This document
turns that observation into an exact rational divisor identity.

## 2. Finite Cauchy transform

Let the finite CCM pole-even vector have real poles `d_n` and real weights `xi_n`.  Define, on the
real height line,

```text
C_x(t) := sum_{n=1}^N xi_n/(t-d_n).
```

Equivalently, in the notation of E73.035,

```text
C_x(i gamma) = -C_x(-gamma)
```

up to the harmless sign convention used for `d_n`.

Let

```text
D_x(t) := prod_{n=1}^N (t-d_n).
```

Then

```text
C_x(t)=P_x(t)/D_x(t),
```

where

```text
P_x(t) := sum_{n=1}^N xi_n prod_{m != n}(t-d_m).
```

Thus the finite Cauchy roots are exactly the zeros of `P_x`.

## 3. Divisor factorization

Assume `P_x` has degree `r` with roots `rho_1,...,rho_r`, counted with multiplicity, and leading
coefficient `c_x`.  Then

```text
C_x(t)=c_x prod_{j=1}^r (t-rho_j) / prod_{n=1}^N (t-d_n).        (1)
```

This is an exact identity of rational functions.

## 4. Proof

The common denominator identity follows by multiplying the finite sum by `D_x(t)`.
The numerator is the polynomial `P_x(t)`.  Factoring `P_x` over `C` gives

```text
P_x(t)=c_x prod_j(t-rho_j).
```

Substitution gives (1).

No analytic continuation, no infinite limit, and no zero of `Xi` is used.

## 5. FINROOT bound

For any real critical height `gamma`,

```text
|C_x(gamma)|
= |c_x| prod_j |gamma-rho_j| / prod_n |gamma-d_n|.
```

If `gamma` lies near a simple finite Cauchy root `rho_j` and remains separated from the poles, then

```text
|C_x(gamma)|
<= Sep_x(gamma)^(-1) |gamma-rho_j|,
```

where the explicit local constant is

```text
Sep_x(gamma)^(-1)
:=
|c_x|
prod_{\ell != j} |gamma-rho_l|
/ prod_n |gamma-d_n|.
```

This is the exact finite version of `FINROOT`.

## 6. Product divisor endpoint

Combining E73.037 with (1), the sufficient positive gate becomes:

```text
e^(alpha L) sum_{gamma_k in K_L}
G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|c_x| prod_j |gamma_k-rho_j| / prod_n |gamma_k-d_n|
<= L^B.
```

This is now a completely explicit finite product inequality involving:

```text
1. the off-line Hermite geometry;
2. the critical mesh phase;
3. the divisor of the finite Cauchy numerator;
4. the finite pole divisor.
```

## 7. What remains

The remaining theorem is no longer a matrix statement.  It is the alignment estimate:

```text
For every off-line natural-height cluster A, the critical heights that couple strongly to A are
covered by enough small factors from either

|1-exp(i gamma L)|

or

dist(gamma, Div(P_x)).
```

This is the exact finite scalar form of the remaining obstruction.
