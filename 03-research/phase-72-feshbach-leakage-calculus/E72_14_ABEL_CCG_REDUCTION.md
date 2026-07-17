# E72.14 -- Abel reduction of centered cumulative Gram cancellation

**Date:** 2026-07-08.
**Role:** reduce the CCG target to a weighted Chebyshev-discrepancy estimate after subtracting the model
main term.

## 0. Starting point

E72.13 expresses the cumulative residual force as

```text
G_x = G_x^{arch-model} - sum_{n<=x} Lambda(n) K_{x,n},
```

where `K_{x,n}` is the centered cumulative kernel for the prime-power cell indexed by `n`.

The target is:

```text
||G_x||_{rho^{-1}}^2 = o(lambda_{x,1}^D).
```

This document applies Abel summation to isolate exactly what arithmetic estimate would prove this.

## 1. Continuous kernel interpolation

Assume the discrete kernels `K_{x,n}` admit a smooth interpolation in the scale variable `u`:

```text
K_x(u)       for 1 <= u <= x,
K_x(n)=K_{x,n}.
```

The interpolation is not unique, but any admissible choice must be built from the explicit finite cell
action on `k_x`, not from zero locations.

Let

```text
Psi(U) := sum_{n<=U} Lambda(n),
E(U)   := Psi(U)-U.
```

Then the prime part is a Stieltjes integral:

```text
sum_{n<=x} Lambda(n)K_{x,n}
 = int_{1^-}^{x} K_x(u)dPsi(u).
```

## 2. Main-term matching

The prolate model `H_x^0` should absorb the PNT main term. The exact condition is:

```text
G_x^{arch-model}
  = int_1^x K_x(u)du + M_x^{err},                (MM)
```

with

```text
||M_x^{err}||_{rho^{-1}}^2 = o(lambda_{x,1}^D).
```

This is the model-main matching condition. It is archimedean/PNT-level, not a zero-location statement.

Under (MM),

```text
G_x
 = - int_{1^-}^{x} K_x(u)dE(u) + M_x^{err}.       (A0)
```

## 3. Abel integration by parts

If `K_x(u)` is of bounded variation in the `rho^{-1}` Hilbert norm, then

```text
int_{1^-}^{x} K_x(u)dE(u)
  = E(x)K_x(x) - int_1^x E(u)partial_u K_x(u)du,
```

assuming `E(1^-)=0`. Thus

```text
G_x
 = -E(x)K_x(x)
   + int_1^x E(u)partial_uK_x(u)du
   + M_x^{err}.                                  (A1)
```

This is exact.

## 4. Sufficient Chebyshev-discrepancy bound

A sufficient condition for CCG is:

```text
|| E(x)K_x(x)
   - int_1^x E(u)partial_uK_x(u)du
||_{rho^{-1}}^2
  = o(lambda_{x,1}^D).                            (CD)
```

Together with (MM), this gives CCG.

The crude absolute sufficient condition is:

```text
|E(x)| ||K_x(x)||_{rho^{-1}}
 + int_1^x |E(u)| ||partial_uK_x(u)||_{rho^{-1}}du
   = o((lambda_{x,1}^D)^{1/2}).                  (CD-abs)
```

But `(CD-abs)` may be too strong. The actual target is the Hilbert-valued cancellation `(CD)`, not the
absolute bound.

## 5. Theorem 72.14 -- Abel reduction

Assume:

```text
(A)  smooth/bounded-variation interpolation K_x(u);
(B)  model-main matching (MM);
(C)  Hilbert-valued Chebyshev discrepancy bound (CD);
(D)  actual/model one-vector replacement from E72.12.
```

Then CCG holds. Consequently CC, DPS, MCC, PSC, reduced leakage, and stable-divisor convergence hold.

### Proof

By (MM), `G_x` equals the discrepancy integral `(A0)` plus `M_x^{err}`. By Abel summation, the discrepancy
integral equals `(A1)`. Assumption (C) makes its `rho^{-1}` norm `o((lambda_{x,1}^D)^{1/2})`; assumption
(B) controls the model-main error. Hence CCG holds. E72.13 and E72.12 then apply. `QED`

## 6. What has been gained

The arithmetic problem is now:

```text
Chebyshev discrepancy E(u)=Psi(u)-u
tested against the derivative of a single family of centered cumulative kernels.
```

This is sharper than asking for RH-like pointwise control of `E(u)`.

The kernel derivative may be sufficiently smoothing that the unconditional PNT error is enough. That is
the first genuine place to test the route.

## 7. Non-circularity gate

The Abel route is admissible only if:

```text
K_x(u) and partial_uK_x(u)
```

are built from the model cell action on `k_x`, and if (MM) is proved from the archimedean/PNT main term.

It is not admissible if:

```text
partial_uK_x
```

is chosen after seeing zeros, or if (CD) is proved using an RH-strength bound

```text
E(u)=O(u^{1/2+epsilon}).
```

The desired proof must use either unconditional PNT bounds or structural smoothing of `partial_uK_x`.

## 8. The next concrete estimate

The new target is:

### ACD -- Abel-Chebyshev discrepancy estimate

For the centered cumulative kernels of E72.13,

```text
|| E(x)K_x(x)
   - int_1^x E(u)partial_uK_x(u)du
||_{rho^{-1}}^2
  = o(lambda_{x,1}^D).
```

This is weaker than pointwise RH if the family `partial_uK_x` is smoothing enough.

## 9. Falsifier

For Davenport-Heilbronn or planted off-line data, replace `Psi` by the corresponding coefficient
summatory function. A failure can occur as:

```text
ACD fails,
MM fails,
or actual/model replacement fails.
```

This separates three mechanisms:

```text
PNT-main matching,
coefficient discrepancy smoothing,
Feshbach graph replacement.
```

## 10. Status

```text
proved:   exact Abel reduction of CCG;
open:     model-main matching and Abel-Chebyshev discrepancy estimate.
```

