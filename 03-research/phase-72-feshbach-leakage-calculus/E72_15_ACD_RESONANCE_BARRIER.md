# E72.15 -- Resonance barrier for the Abel-Chebyshev estimate

**Date:** 2026-07-08.
**Role:** test whether the Abel-Chebyshev discrepancy estimate from E72.14 is genuinely weaker than
the Hardy-Euler/Abel boundary obstruction of Phase 70.

## 0. The target from E72.14

Let

```text
H_x := L^2([a_x,b_x], rho_x(theta)^(-1)dtheta)
```

and let `K_x(u) in H_x` be the centered cumulative kernel interpolation. E72.14 reduced CCG to

```text
T_x := E(x)K_x(x) - int_1^x E(u)partial_uK_x(u)du,
||T_x||_{H_x}^2 = o(lambda_{x,1}^D),                  (ACD)
```

where

```text
E(u)=Psi(u)-u.
```

This document proves the exact resonance obstruction to `(ACD)`.

## 1. Mellin resonance vectors

For complex `s`, define the Hilbert-valued Abel-Mellin vector

```text
R_x(s) := x^s K_x(x) - int_1^x u^s partial_uK_x(u)du.      (R)
```

Equivalently, by integration by parts,

```text
R_x(s) = K_x(1) + s int_1^x u^{s-1}K_x(u)du
```

whenever the interpolation is absolutely continuous in `H_x`. In the centered cumulative setup
`K_x(1)=0`, so

```text
R_x(s) = s int_1^x u^{s-1}K_x(u)du.                       (R0)
```

Thus `R_x(s)` is not an auxiliary object: it is exactly the response of the cumulative kernel to a
Chebyshev-error component `u^s`.

## 2. Explicit-formula expansion of the ACD vector

Use the standard smoothed explicit formula on `[1,x]`:

```text
E(u) = - sum_rho u^rho/rho + E_triv(u) + E_pole-reg(u),
```

where the sum is understood with a symmetric truncation or a smooth cutoff. Substituting this in `T_x`
gives, after the same Abel integration by parts as E72.14,

```text
T_x
 = - sum_rho R_x(rho)/rho
   + T_x^{triv}
   + T_x^{pole-reg}
   + T_x^{cut}.                                      (EF-ACD)
```

The trivial-zero, pole-regularization, and cutoff terms are controlled by the same archimedean/model
main matching already separated in E72.14. The nontrivial zeros enter only through the vectors
`R_x(rho)`.

This identity is the Abel-Chebyshev analogue of E70.6:

```text
prime-error cancellation = cancellation of zero-resonance vectors.
```

## 3. The resonance barrier theorem

### Theorem 72.15

Assume:

1. `K_x(u)` is absolutely continuous as an `H_x`-valued function and `K_x(1)=0`;
2. the explicit-formula replacement `(EF-ACD)` is valid with

```text
||T_x^{triv}+T_x^{pole-reg}+T_x^{cut}||_{H_x}
  = o((lambda_{x,1}^D)^{1/2});
```

3. there is an off-critical zero `rho_0=beta+i gamma`, `beta>1/2`, and a sequence `x_j -> infinity`
for which its resonance vector is not killed:

```text
dist(
  R_{x_j}(rho_0)/rho_0,
  span{ R_{x_j}(rho)/rho : rho != rho_0, Re rho >= beta } )
    not= o((lambda_{x_j,1}^D)^{1/2}).                  (NR)
```

Then `(ACD)` fails along that sequence.

Equivalently, if `(ACD)` holds in the presence of an off-critical zero, then every maximal real-part
off-line zero must satisfy the structural cancellation

```text
R_x(rho) is absorbed by the other maximal zero-resonance vectors up to
o((lambda_{x,1}^D)^{1/2}).                            (SC)
```

### Proof

By `(EF-ACD)`,

```text
T_x
 = - sum_{Re rho >= beta} R_x(rho)/rho
   - sum_{Re rho < beta} R_x(rho)/rho
   + o((lambda_{x,1}^D)^{1/2})
```

after absorbing the trivial, pole-regular, and cutoff contributions.

For zeros with `Re rho < beta`, the standard explicit-formula truncation gives a strictly smaller
power of `x`; their contribution is lower order relative to the maximal `beta` block. Hence the
maximal block controls whether `T_x` can be small.

Project `T_x` orthogonally onto the complement of

```text
span{ R_x(rho)/rho : rho != rho_0, Re rho >= beta }.
```

All other maximal zero terms vanish under this projection. Assumption `(NR)` says the projected
`rho_0` term is not `o((lambda_{x,1}^D)^{1/2})`. Therefore

```text
||T_x||_{H_x} not= o((lambda_{x,1}^D)^{1/2}),
```

which contradicts `(ACD)`. `QED`

## 4. Consequence

The Abel-Chebyshev target is not automatically easier than Phase 70. It becomes easier only if the
one-vector cumulative kernels have a new structural property:

### Zero-resonance annihilation

For every off-critical zero `rho` with `Re rho>1/2`,

```text
R_x(rho) = o((lambda_{x,1}^D)^{1/2})
```

or the maximal real-part resonance vectors cancel by an intrinsic symmetry that does not use zero
locations.

That is the exact place where new mathematics would have to enter.

## 5. Why unconditional PNT is insufficient

The PNT gives only

```text
E(u)=o(u).
```

Inserted into the crude bound from E72.14, this controls

```text
int_1^x |E(u)| ||partial_uK_x(u)||_{H_x}du,
```

not the signed vector `T_x`. The obstruction above is invisible to such an absolute estimate: an
off-line zero contributes an oscillatory signed term of size `u^beta`, and the Hilbert norm selects the
dual direction resonant with `R_x(beta+i gamma)`.

Therefore no proof of `(ACD)` can be obtained from PNT-scale information plus size/variation bounds on
`K_x`. It must prove zero-resonance annihilation or an equivalent signed cancellation theorem.

## 6. Status

```text
proved: ACD decomposes into explicit zero-resonance vectors R_x(rho);
proved: any non-annihilated off-line resonance violates ACD;
open:   intrinsic zero-resonance annihilation for the actual centered cumulative kernels.
```

This is a real obstruction, not a bookkeeping issue. The next possible proof attempt must target
`R_x(s)` directly, not `E(u)` by absolute estimates.
