# E72.52 -- Hilbert coefficient formula for the compressed scalar channel

**Date:** 2026-07-08.
**Role:** express the Fourier coefficients `c_{x,s,ell}` from E72.51 directly in terms of the finite
vectors `v_{x,s}` and `k_x`.

## 0. Cell formulas

For `m=n`:

```text
q_nn(y)=2(1-y/L)cos(2*pi*n y/L).
```

For `m != n`:

```text
q_mn(y)= [sin(2*pi*m y/L)-sin(2*pi*n y/L)]/[pi(n-m)].
```

Thus the scalar channel:

```text
a(y)=sum_{m,n} conj(v_m) k_n q_mn(y)
```

has coefficients supported at frequencies in the index set.

## 1. Coefficient structure

Ignoring the endpoint linear factor in the diagonal term for the moment, the coefficient at frequency
`ell` receives:

```text
diagonal contribution from m=n=ell,
off-diagonal contribution from all pairs with m=ell or n=ell.
```

Schematically:

```text
c_ell
 = A_diag conj(v_ell)k_ell
   + A_sin [
       conj(v_ell) sum_{n != ell} k_n/(n-ell)
       - k_ell sum_{m != ell} conj(v_m)/(ell-m)
     ].                                          (HC)
```

The bracket is a discrete Hilbert-transform expression.

## 2. Consequence

The compressed Fourier half-power estimate from E72.51 is:

```text
sum_ell |c_ell| = small.
```

Using only generic Hilbert-transform boundedness gives at best:

```text
||c||_2 <= C ||v||_2||k||_2,
||c||_1 <= C sqrt(N)||v||_2||k||_2,
```

which does **not** supply a half-power in `x`.

Therefore the needed smallness cannot follow from generic Fourier/Hilbert estimates. It must use the
specific equation satisfied by `v`:

```text
C_x v = Q_x(sI-D_x)^(-1)1_x,
```

and the prolate ground equation for `k`.

## 3. New coefficient target

### Compressed Hilbert Cancellation

For the specific pair:

```text
v=C_x^(-1)Q_x(sI-D_x)^(-1)1,
k=prolate ground state,
```

the Hilbert coefficient vector `(c_ell)` satisfies:

```text
sum_ell |c_ell|
 = o(x^(-1/2)exp(c(log x)^alpha)).
```

Or, more weakly but closer to the scalar sum:

```text
sum_ell c_ell E_x(ell;z) -> 0
```

where `E_x(ell;z)` are the finite prime exponential-sum errors from E72.51.

## 4. Status

```text
proved: Fourier coefficients of the scalar channel are discrete Hilbert transforms of v and k;
proved: generic Hilbert bounds are insufficient;
open:   exploit the finite Feshbach equation for v to prove compressed Hilbert cancellation.
```

The next step is to insert `C_xv=Qr_s` into the Hilbert coefficient formula.
