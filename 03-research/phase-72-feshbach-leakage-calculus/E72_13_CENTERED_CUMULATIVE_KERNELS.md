# E72.13 -- Centered cumulative kernels for the residual force

**Date:** 2026-07-08.
**Role:** express the cumulative cancellation target CC as an exact coherent sum of centered cumulative
cell kernels.

## 0. Starting point

E72.12 reduced the proof target to the weighted cumulative residual force:

```text
G_x(theta)=int_a^theta k_x(t)F_x(t)dt,
F_x=Q_xR_xk_x,
R_x=H_x-H_x^0.
```

This document expands `G_x` exactly without using absolute values, local inverses, or zero-local kernels.

## 1. Centering identity

Let `B` be any self-adjoint cell/operator acting on the model core. Define its scalar expectation on the
model ground vector:

```text
beta_x(B) := <k_x,Bk_x>.
```

Define the centered force:

```text
F_x[B] := Bk_x - beta_x(B)k_x.
```

Then

```text
<k_x,F_x[B]> = 0.
```

The associated centered cumulative kernel is:

```text
K_x[B](theta)
  := int_a^theta k_x(t)(Bk_x)(t)dt
     - beta_x(B) int_a^theta k_x(t)^2dt.         (K)
```

Because of centering,

```text
K_x[B](a)=K_x[B](b)=0.
```

This endpoint cancellation is the cumulative form of the Feshbach scalar recentering.

## 2. Exact expansion of the residual cumulative force

Suppose the actual/model residual decomposes on the finite support as

```text
R_x = sum_{c in C_x^{cells}} omega_c B_{x,c},
```

where the cells include the prime-power pieces and any archimedean/model-difference piece. This is a
finite sum at each `x`, because the prime support is exact in the window.

Then

```text
a_x = <k_x,R_xk_x> = sum_c omega_c beta_x(B_{x,c})
```

and

```text
F_x = Q_xR_xk_x
    = sum_c omega_c F_x[B_{x,c}].
```

Therefore the cumulative residual force is exactly:

```text
G_x(theta)
  = sum_c omega_c K_x[B_{x,c}](theta).            (G)
```

No limiting argument has been used.

## 3. The CC norm

The cumulative cancellation condition of E72.12 becomes:

```text
||G_x||_{rho^{-1}}^2
 := int_a^b |sum_c omega_c K_x[B_{x,c}](theta)|^2
       / rho_x(theta) dtheta
  = o(lambda_{x,1}^D).                            (CC-kernel)
```

where

```text
rho_x(theta)=p_x(theta)k_x(theta)^2.
```

This is the exact one-vector coherent cancellation statement.

## 4. Why this avoids the incoherent ceiling

The forbidden estimate would be:

```text
sum_c |omega_c| ||K_x[B_{x,c}]||_{rho^{-1}} -> 0.
```

That is an absolute ceiling estimate and is expected to fail.

The required estimate is instead:

```text
||sum_c omega_c K_x[B_{x,c}]||_{rho^{-1}} -> 0.
```

The cross terms are the whole point:

```text
||G_x||_{rho^{-1}}^2
 = sum_{c,d} omega_c conj(omega_d)
   int K_x[B_{x,c}](theta) conj(K_x[B_{x,d}](theta))/rho_x(theta)dtheta.
```

Thus Phase 72 has not escaped arithmetic; it has localized it to a precise coherent Gram cancellation of
centered cumulative cell kernels.

## 5. Prime-power form

For the prime-power part, write schematically:

```text
R_x^{prime} = - sum_{p^m <= x} Lambda(p^m) T_{p^m,x},
```

with the exact support cutoff inherited from Phase 60. Then

```text
G_x^{prime}(theta)
 = - sum_{p^m <= x} Lambda(p^m) K_x[T_{p^m,x}](theta).
```

The archimedean/model part is a single additional centered kernel:

```text
G_x^{arch-model}(theta)
 = K_x[B_{x,arch}-B_{x,model}](theta).
```

Hence

```text
G_x = G_x^{arch-model} + G_x^{prime}.
```

This is the exact CC object to compute/prove.

## 6. Kernel Gram matrix

Define the cumulative kernel Gram matrix:

```text
M_x(c,d)
  := int_a^b K_x[B_{x,c}](theta) conj(K_x[B_{x,d}](theta))
       / rho_x(theta) dtheta.
```

Then

```text
||G_x||_{rho^{-1}}^2 = omega_x^* M_x omega_x.
```

The CC target is:

```text
omega_x^* M_x omega_x = o(lambda_{x,1}^D).
```

This is not a positivity problem. `M_x` is positive as a Gram matrix, but the arithmetic vector
`omega_x` has coherent signs/phases through the centered kernels. The smallness must come from the
structure of the vector and kernels, not from termwise positivity.

## 7. Non-circularity gate

The construction of `M_x` uses only:

```text
k_x,
the model coefficient rho_x,
the finite cell action B_{x,c} on k_x,
and scalar centering beta_x(B_{x,c}).
```

It does not use:

```text
C_x^{-1},
endpoint resolvents,
zero locations as sampling centers,
or additive local Green assembly.
```

Therefore the Gram expression is an admissible object.

## 8. What must be proved next

The exact next theorem is:

### CCG -- Centered Cumulative Gram cancellation

For the actual zeta finite cells,

```text
omega_x^* M_x omega_x = o(lambda_{x,1}^D),
```

and the one-vector actual/model replacement term from E72.12 holds:

```text
||C_x^{-1}(C_x-C_x^0)(k_xh_x)|| -> 0.
```

Then CC holds, hence DPS, MCC, PSC, reduced leakage, and stable-divisor convergence.

## 9. Falsifier

For Davenport-Heilbronn or planted off-line data, one expects:

```text
liminf omega_x^*M_xomega_x/lambda_{x,1}^D > 0
```

or failure of the actual/model replacement term.

This is a sharp numerical falsifier because it measures the coherent cumulative residual, not the raw
operator difference.

## 10. Status

```text
proved:   exact centered cumulative kernel expansion of CC;
proved:   CCG + actual/model replacement => CC => DPS => PSC;
open:     prove CCG for zeta finite cells.
```

