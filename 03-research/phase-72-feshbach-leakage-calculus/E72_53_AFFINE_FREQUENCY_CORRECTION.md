# E72.53 -- Affine-frequency correction for the scalar endpoint channel

**Date:** 2026-07-08.
**Role:** correct the finite-frequency expansion E72.51/E72.52. The scalar channel is finite-frequency
plus affine-frequency, not a pure trigonometric polynomial.

## 0. The issue

E72.51 wrote schematically:

```text
a_{x,s}(y)=sum_{|ell|<=2N_x} c_{x,s,ell} e^{2*pi*i ell y/L}.
```

This is incomplete because the diagonal CCM cell is:

```text
q_nn(y)=2(1-y/L)cos(2*pi*n y/L).
```

The factor `(1-y/L)` is not a finite Fourier multiplier on `[0,L]`. It must be kept explicitly.

## 1. Exact affine-frequency form

Let:

```text
omega_ell := 2*pi*ell/L.
```

Then the scalar channel has the exact form:

```text
a(y)
 = sum_{ell} A_ell e^{i omega_ell y}
   + (1-y/L) sum_ell B_ell e^{i omega_ell y}.    (AFF)
```

Here:

```text
B_ell
```

comes from the diagonal products `conj(v_ell)k_ell`, while:

```text
A_ell
```

comes from the off-diagonal Hilbert-transform terms.

Thus the frequency support is still finite, but the basis is affine in `y`.

## 2. Prime sums produced by affine terms

For an exponent

```text
alpha = z - 1/2 + i omega_ell,
```

the pure-frequency term contributes:

```text
x^{-z} sum_{n<=x} Lambda(n)n^alpha.
```

The affine endpoint term contributes:

```text
x^{-z} sum_{n<=x} Lambda(n)n^alpha(1-log n/L).
```

Equivalently:

```text
sum Lambda(n)n^alpha(1-log n/L)
 = S_alpha(x) - (1/L) partial_alpha S_alpha(x),
S_alpha(x)=sum_{n<=x} Lambda(n)n^alpha.
```

So E72.51 remains valid after replacing each frequency prime sum by the endpoint differential operator:

```text
E_L := 1 - (1/L)partial_alpha.                   (END)
```

The same correction applies to the Chebyshev-discrepancy integral.

## 3. Corrected discrepancy bound

Classical PNT gives, for `alpha=z-1/2+i tau` and finite `tau=O(1)`,

```text
x^{-z} int_1^x u^alpha dE(u)
 = O_K(x^(1/2) exp(-c(log x)^a)).
```

Applying `E_L` introduces at most one logarithmic factor, because:

```text
partial_alpha u^alpha = (log u)u^alpha.
```

The endpoint operator `(1-(1/L)partial_alpha)` does not change the half-power barrier. It improves
endpoint behavior but not enough to remove the need for compressed half-power coefficients.

Thus the corrected coefficient sufficient condition is:

```text
sum_ell |A_ell| + sum_ell |B_ell|
 = o(x^(-1/2) exp(c(log x)^a)/L^C)               (COEF-aff)
```

for a harmless fixed logarithmic loss `L^C`.

## 4. Corrected Hilbert coefficient target

The off-diagonal coefficients `A_ell` have the discrete Hilbert-transform structure of E72.52.

The diagonal affine coefficients are:

```text
B_ell ~ conj(v_ell)k_ell.
```

Therefore the compressed half-power target splits into:

```text
sum_ell |Hilbert(v,k)_ell|      small,
sum_ell |conj(v_ell)k_ell|      small.
```

The second term is controlled by overlap/localization between `v` and `k`; the first by Hilbert
cancellation plus the Feshbach equation.

## 5. Status

```text
corrected: scalar channel is finite affine-frequency, not pure finite-frequency;
proved: correction only adds exponent derivatives/log factors;
open: prove half-power bounds for both off-diagonal Hilbert coefficients and diagonal affine
      coefficients.
```

This correction preserves the Phase 72 route but prevents a false pure-Fourier simplification.
