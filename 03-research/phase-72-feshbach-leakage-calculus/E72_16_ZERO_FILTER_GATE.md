# E72.16 -- Zero-filter gate for the resonance vectors

**Date:** 2026-07-08.
**Role:** decide what kind of theorem could prove the resonance annihilation left open by E72.15
without encoding the zeta divisor.

## 0. Input from E72.15

The Abel-Chebyshev discrepancy vector has the zero expansion

```text
T_x = -sum_rho R_x(rho)/rho + lower-order terms,
R_x(s)=x^sK_x(x)-int_1^x u^s partial_uK_x(u)du.
```

Thus the only possible direct proof of ACD is:

```text
R_x(rho) = o((lambda_{x,1}^D)^(1/2))
```

for every off-critical zero `rho`, with cancellations among equal-real-part conjugate blocks allowed.

This document records the non-circularity gate for such a proof.

## 1. Scalar Mellin projections

For a unit vector `eta in H_x`, define

```text
r_{x,eta}(s) := <R_x(s),eta>_{H_x}.
```

Then

```text
r_{x,eta}(s)
 = x^s <K_x(x),eta>
   - int_1^x u^s partial_u<K_x(u),eta>du.
```

If `K_x(1)=0`,

```text
r_{x,eta}(s)=s int_1^x u^{s-1}<K_x(u),eta>du.
```

So every scalar projection is a truncated Mellin transform of an explicitly constructed model-cell
kernel.

## 2. What a proof of annihilation would have to show

There are only three logical possibilities.

### A. Universal model annihilation

For structural reasons independent of zeta,

```text
R_x(s)=o((lambda_{x,1}^D)^(1/2))
```

throughout a region `Re s>1/2`.

This would prove ACD immediately. But it is also the easiest case to falsify: it would kill the same
region for any Euler-like coefficient system using the same prolate cells. Davenport-Heilbronn/planted
controls would then converge too, contradicting the Phase 71 detector behavior.

Therefore universal annihilation is too strong unless the controls fail earlier at model-main matching
or actual/model replacement.

### B. Zeta-specific annihilation through an analytic factor

The scalar projections factor as

```text
r_{x,eta}(s)=Z_x(s)u_{x,eta}(s),
```

and the factor `Z_x` vanishes on the off-critical zeta divisor.

This is admissible only if `Z_x` is built from the finite CCM/prolate data without using zero locations
or `Xi` as an input. Otherwise the proof has simply inserted the desired divisor.

### C. Signed vector cancellation across zeros

The individual `R_x(rho)` need not be small, but the vector sum over zeros of maximal real part cancels:

```text
sum_{Re rho=beta} R_x(rho)/rho = o((lambda_{x,1}^D)^(1/2)).
```

This is the vector form of the Hardy-Euler phase cancellation from E70. It is legitimate only if the
cancellation follows from a symmetry of the finite CCM construction, not from pairing terms after
knowing the zero set.

## 3. Zero-filter theorem

### Theorem 72.16

Let `U` be a connected open set intersecting `{Re s>1/2}`. Assume that for a subsequence `x_j` and a
unit-vector family `eta_j`, the scalar Mellin projections converge locally uniformly:

```text
r_{x_j,eta_j}(s) -> r(s)
```

on `U`, with `r` not identically zero.

If the resonance annihilation

```text
r_{x_j,eta_j}(rho) -> 0
```

holds for every off-critical zero `rho in U`, then every such `rho` is a zero of the limiting analytic
function `r`.

Consequently, any proof of annihilation by scalar Mellin limits must produce a nonzero analytic
zero-filter whose divisor contains the off-critical zeta divisor.

### Proof

The functions `r_{x_j,eta_j}` are analytic in `s` because they are finite-interval Mellin transforms of
absolutely continuous kernels. Local uniform convergence gives an analytic limit `r`.

Fix an off-critical zero `rho in U`. By assumption,

```text
r_{x_j,eta_j}(rho) -> 0.
```

Passing to the limit gives `r(rho)=0`. Since `rho` was arbitrary, the off-critical zeta divisor inside
`U` is contained in the divisor of `r`. If `r` is not identically zero, this is a genuine analytic
zero-filter. `QED`

## 4. Consequence for Phase 72

The desired proof cannot merely say:

```text
the prolate Mellin transform has good decay.
```

Decay gives size bounds and returns to the PNT ceiling. To prove ACD, one needs one of:

```text
1. a zero-filter r(s) forced by finite CCM/prolate algebra;
2. a finite-CCM symmetry forcing vector cancellation among maximal zero resonances;
3. failure of the resonance expansion for controls through model-main matching or replacement.
```

Option 1 is dangerous: if the zero-filter is recognizably `Xi` or a quotient containing `Xi`, the route
is circular. Option 2 is the only plausible non-circular remaining path.

## 5. New target

The next theorem cannot be a scalar estimate on `E(u)`. It must be a finite-dimensional symmetry
statement:

### Maximal-resonance cancellation

For every `beta>1/2`, the finite CCM/prolate construction satisfies

```text
sum_{rho: Re rho=beta} R_x(rho)/rho
  = o((lambda_{x,1}^D)^(1/2)),
```

without using the locations of those zeros as input.

This is exactly the point at which the route either produces genuinely new mathematics or collapses
back to the Phase 70 boundary-loss obstruction.
