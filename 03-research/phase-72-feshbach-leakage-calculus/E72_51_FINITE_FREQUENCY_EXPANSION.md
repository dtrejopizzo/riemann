# E72.51 -- Finite-frequency expansion of the scalar endpoint channel

**Date:** 2026-07-08.
**Role:** express the remaining WCB estimate as a finite set of weighted prime exponential sums with
explicit scalar coefficients.

## 0. Scalar channel

The scalar channel is:

```text
a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>.
```

The entries of `Q_x(y)` are trigonometric polynomials in `y/L`, with endpoint factor encoded by
overlap. Therefore:

```text
a_{x,s}(y)=sum_{|ell|<=2N_x} c_{x,s,ell} e^{2*pi*i ell y/L}.    (FE)
```

The coefficients are explicit bilinear expressions in `v_{x,s}` and `k_x`.

## 1. Endpoint prime sum in frequencies

The weighted scalar endpoint channel is:

```text
N_x(s;z)=sum_{n<=x} Lambda(n)(n/x)^z n^(-1/2)a_{x,s}(log n).
```

Substituting `(FE)`:

```text
N_x(s;z)
 = sum_{|ell|<=2N_x} c_{x,s,ell} x^(-z)
   sum_{n<=x} Lambda(n)n^{z-1/2+2*pi*i ell/L}.  (PS)
```

The continuous model main term is:

```text
N_x^{cont}(s;z)
 = sum_ell c_{x,s,ell} x^(-z)
   int_1^x u^{z-1/2+2*pi*i ell/L}du.
```

This is precisely the part absorbed by the model endpoint operator of E72.47.

The discrepancy is:

```text
N_x^{err}(s;z)
 = sum_ell c_{x,s,ell} x^(-z)
   int_1^x u^{z-1/2+2*pi*i ell/L}dE(u).          (ERR)
```

## 2. Classical bound

For each fixed `ell/L=O(1)` and `sigma=Re z>1/2`, PNT gives:

```text
int_1^x u^{z-1/2+i tau}dE(u)
 = O_K( x^{sigma+1/2} exp(-c(log x)^alpha) ).
```

After multiplying by `x^(-z)`:

```text
|frequency error|
 <= C_K x^(1/2) exp(-c(log x)^alpha).
```

Therefore:

```text
|N_x^{err}(s;z)|
 <= C_K x^(1/2) exp(-c(log x)^alpha)
    sum_{|ell|<=2N_x}|c_{x,s,ell}|.              (FERR)
```

## 3. Coefficient condition

A sufficient condition for discrepancy smallness is:

```text
sum_{|ell|<=2N_x}|c_{x,s,ell}|
 = o( x^(-1/2) exp(c(log x)^alpha) ).            (COEF)
```

In particular, a true half-power coefficient bound

```text
sum |c_{x,s,ell}| = O(x^(-1/2)L^{-B})
```

for large `B` would close the endpoint discrepancy.

## 4. Meaning

This is the exact scalar form of the missing half-power:

```text
not a prime estimate,
not a zero estimate,
but an l1 Fourier-coefficient estimate for the compressed channel a_{x,s}.
```

The finite Fourier expansion shows why the family is smaller than Phase 70, but it also shows why PNT
alone is insufficient: the half-power must be in the coefficients.

## 5. New target

### Compressed Fourier Half-Power

For fixed compact height and two Cauchy heights:

```text
sum_{|ell|<=2N_x}|c_{x,s,ell}| = o(x^(-1/2) exp(c(log x)^alpha)).
```

This is now a finite-dimensional prolate/Feshbach estimate.

## 6. Status

```text
proved: WCB reduces to finite-frequency prime sums;
proved: classical PNT reduces discrepancy to the l1 coefficient bound (COEF);
open:   prove the compressed Fourier half-power coefficient bound.
```

The next step is to express `c_{x,s,ell}` directly in terms of Fourier coefficients of `v_{x,s}` and
`k_x` and estimate their convolution.
