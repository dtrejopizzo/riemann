# E72.49 -- Bandlimited PNT endpoint theorem for scalar discrepancy

**Date:** 2026-07-08.
**Role:** test whether finite bandwidth lets classical PNT prove scalar endpoint discrepancy
cancellation. The answer is negative without an additional half-power channel gain.

## 0. Key observation

The Phase 70 Hardy-Euler wall allowed arbitrary Hardy autocorrelations. The scalar endpoint channel here
is much smaller:

```text
a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>.
```

Because `Q_x(y)` is a finite Fourier-overlap matrix with indices `|m|,|n|<=N`, the function
`a_{x,s}(y)` is a trigonometric polynomial in `y/L` with bandwidth `O(N)`, multiplied by the endpoint
overlap/taper.

To identify the divisor in a fixed compact height window `|t|<=T`, the pole mesh spacing is `2*pi/L`,
so one only needs:

```text
N_x = O_T(L).
```

This is a tiny bandwidth compared with the strength of the classical PNT error.

## 1. Bandlimited derivative bound

Let:

```text
F_{x,s,z}(u)=(u/x)^z u^(-1/2)a_{x,s}(log u).
```

Assume:

```text
|a_{x,s}(y)| <= A_x(1-y/L),
|partial_y a_{x,s}(y)| <= A_x * N_x/L,          (BL)
```

uniformly for `0<=y<=L`, two Cauchy heights, and `z` in compact subsets of `Re z>1/2`.

Then:

```text
|partial_u F_{x,s,z}(u)|
 <= C_K A_x x^(-sigma) u^(sigma-3/2)
    (1 + N_x/L + 1/L).                          (D)
```

## 2. PNT input

Use the classical de la Vallee-Poussin/Vinogradov-Korobov form:

```text
E(u)=Psi(u)-u
 = O(u exp(-c (log u)^alpha))
```

for some fixed `alpha>0` sufficient for this argument.

## 3. Conditional theorem

### Theorem 72.49

Fix compact `K subset {Re z>1/2}` and a compact Cauchy-height set avoiding the real pole mesh. Suppose:

1. the scalar channel satisfies `(BL)`;
2. the finite section and channel obey

```text
A_x(1+N_x/L) exp(-c' (log x)^alpha) x^(1/2) -> 0.    (G)
```

Then the scalar endpoint discrepancy cancellation `(SEDC)` from E72.48 holds:

```text
int_1^x E(u) partial_uF_{x,s,z}(u)du -> 0.
```

### Proof

By Abel summation from E72.48:

```text
D_x(s;z)=-int_1^x E(u)partial_uF_{x,s,z}(u)du + endpoint_1.
```

The endpoint at `u=x` vanishes by taper. The `u=1` endpoint is harmless after the usual fixed lower
cutoff; it is absorbed in the model normalization.

Using `(D)` and the PNT error:

```text
|D_x(s;z)|
 <= C_K A_x(1+N_x/L)x^(-sigma)
    int_1^x u exp(-c(log u)^alpha) u^(sigma-3/2)du.
```

The integral is:

```text
O_K( x^(sigma+1/2) exp(-c'(log x)^alpha) ).
```

Therefore:

```text
|D_x(s;z)|
 <= C_K A_x(1+N_x/L)x^(1/2)exp(-c'(log x)^alpha).
```

Assumption `(G)` gives convergence to zero. `QED`

## 4. Why classical PNT is not enough

For fixed compact height `T`, the finite mesh needs only:

```text
N_x ~ T L/(2*pi).
```

Thus:

```text
N_x/L = O_T(1).
```

However, if `A_x` grows only polylogarithmically, condition `(G)` still does **not** follow from the
classical PNT error

```text
exp(-c(log x)^alpha),  alpha<1.
```

The obstruction is the factor:

```text
x^(1/2)=exp((1/2)log x),
```

which dominates `exp(-c(log x)^alpha)` for every `alpha<1`.

Therefore finite bandwidth alone does not escape the Phase 70 wall. It lowers the problem to a
half-power channel gain, but it does not remove that gain.

## 5. Correct remaining estimate

The remaining zero-free estimate is:

### Half-Power Scalar Channel Bound

For fixed compact height and two Cauchy heights,

```text
A_x = o(x^(-1/2) exp(c'(log x)^alpha)/(1+N_x/L)).
```

Equivalently, one needs the compressed scalar channel to supply the missing half-power:

```text
A_x x^(1/2) exp(-c'(log x)^alpha) -> 0.
```

This is exactly the half-power channel requirement already isolated in E72.40, now in the
finite-bandwidth scalar channel.

## 6. Status

```text
proved: bandlimited scalar endpoint channels satisfy SEDC if the compressed channel supplies a
        half-power gain;
corrected: classical PNT plus finite bandwidth alone does not supply that gain;
open:   prove the half-power scalar channel bound from the compressed prolate/CCM geometry.
```

The route has not escaped the half-power barrier yet. It has localized the missing half-power entirely
inside the compressed scalar channel.
