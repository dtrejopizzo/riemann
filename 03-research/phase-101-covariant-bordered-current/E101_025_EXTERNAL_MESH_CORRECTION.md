# E101.025 - External mesh correction

## 1. Exact external derivative

For the right transfer, the raw bilateral characteristic has the residual
mesh zeros listed in E101.014(3.2).  Therefore the exact logarithmic derivative
of the external product is

```text
B_ext^exact(L,N,sigma)
 =2 sigma/(rho_N^2+sigma^2)
  +4 sigma sum_(k>N)1/(rho_k^2+sigma^2),             (1.1)

rho_k=2 pi k/L.                                      (1.2)
```

This replaces P76.037 `(EM-2)`, which omitted `sigma^2` from the denominators.

## 2. Quantified difference from the recorded formula

Let

```text
B_ext^old
 =2 sigma/rho_N^2+4 sigma sum_(k>N)1/rho_k^2.        (2.1)
```

Then

```text
0<=B_ext^old-B_ext^exact.                            (2.2)
```

Uniformly for `0<sigma<=S`,

```text
B_ext^old-B_ext^exact
 <=S^3 L^4/(8 pi^4 N^4)
   +S^3 L^4/(12 pi^4 N^3).                           (2.3)
```

### Proof

For each residual zero,

```text
1/rho^2-1/(rho^2+sigma^2)
 =sigma^2/[rho^2(rho^2+sigma^2)]
 <=sigma^2/rho^4.                                    (2.4)
```

Apply (2.4) to (1.1)--(2.1), use `rho_k=2 pi k/L`, and use

```text
sum_(k>N)k^(-4)<=1/(3N^3).                           (2.5)
```

This proves (2.2)--(2.3). `QED`

The old expression is an upper approximation, not an exact identity.  Its
error need not vanish under `N/L->infinity` alone.

## 3. Raw and core masses

Let

```text
Psi_core=Psi_raw/Z_ext.                              (3.1)
```

The raw and core Stieltjes masses satisfy exactly

```text
M_raw(L,N,sigma)
 =M_core(L,N,sigma)+R_ext(L,N,sigma),                (3.2)

R_ext=B_ext^exact/(2 sigma).                         (3.3)
```

E101.014 gives

```text
M_raw
 ={L/(2 sigma)}coth(sigma L/2)
  +(1/sigma)Re{iT_N'/T_N}(i sigma).                  (3.4)
```

Subtracting (3.3), or using the secular trace directly, gives

```text
M_core
 =sum_(-N+1<=k<=N)1/(d_k^2+sigma^2)
  +(1/sigma)Re{iT_N'/T_N}(i sigma)                   (3.5)

 =sum_j1/(kappa_j^2+sigma^2).                        (3.6)
```

The direct determinant route uses the core family.  Its compactness scalar is
therefore (3.5), not the raw hyperbolic scalar (3.4).

## 4. Consequences for inherited formulas

The definition of `Psi_core`, its finite real-rootedness, and every exact
ratio using the product itself remain valid.  Every later occurrence of
`B_ext` in an exact logarithmic-derivative formula must be interpreted as
`B_ext^exact` from (1.1).

The following scaling statements remain distinct:

```text
raw family:
  R_ext->0 on safe compacta under N/L^2->infinity;

core family:
  the external divisor is removed exactly, so no estimate of R_ext is
  required.                                           (4.1)
```

## 5. Multiprecision certification

For `L=2log 6`, `N=6`, and `sigma=1.25`, direct summation of (1.1) and the
partition formula

```text
B_ext^exact
 =2 sigma{
   [L/(2 sigma)]coth(sigma L/2)
   -sum_(-N+1<=k<=N)1/(d_k^2+sigma^2)
  }                                                  (5.1)
```

agree with residual

```text
4.67e-61.                                            (5.2)
```

At the same parameters,

```text
B_ext^old-B_ext^exact =0.00129920147897,
bound in (2.3)       =0.00159457290423.              (5.3)
```

This independently verifies the denominators, multiplicities, sign and error
bound.

## 6. Status

```text
corrected:
  external mesh logarithmic derivative;
  raw/core Stieltjes-mass distinction;
  interpretation of every inherited B_ext symbol;

preserved:
  exact core product and its real-rootedness;

open:
  cofinal identification of the core secular mass.
```
