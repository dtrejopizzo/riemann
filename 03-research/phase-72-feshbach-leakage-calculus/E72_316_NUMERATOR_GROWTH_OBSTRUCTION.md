# E72.316 -- Why ordinary residue regularity cannot prove NUM-GROW

**Purpose.** Audit the new target `NUM-GROW` from E72.315. This prevents a new circle: proving
ordinary smoothness or bounded variation of the residue vector `xi_m` is not enough to close the
compact contour. The required estimate is exponentially stronger.

## 1. The target

The compact contour route needs, in a fixed shifted strip `0<sigma<=Re z<=sigma_1`,

```text
|(1-e^(zL))C_x(iz)| <= L^B(1+|Im z|)^B.              (SQB)
```

Since

```text
|1-e^(zL)| ~ e^(Re z L)
```

on the right side of the strip, `SQB` is equivalent to

```text
|C_x(iz)| <= L^B e^(-Re z L).                         (EXP-C)
```

Thus the Cauchy transform itself must be exponentially small in every positive shifted half-strip.

## 2. Ordinary residue bounds are insufficient

Let

```text
C_x(iz)=sum_m xi_m/(iz-d_m).
```

Any estimate based only on

```text
||xi||_1 <= L^A,
```

gives at best

```text
|C_x(iz)| <= L^A / dist(iz,mesh),
```

which is polynomial, not `e^(-sigma L)`.

Likewise, an `l^2` estimate gives

```text
|C_x(iz)| <= ||xi||_2 (sum_m |iz-d_m|^-2)^(1/2),
```

again polynomial in fixed strips away from the mesh.

Bounded variation, Sobolev regularity, or finite-difference decay of `xi_m` improves powers of `L`,
but it does not produce the missing factor `e^(-sigma L)`.

Therefore:

```text
ordinary regularity of xi_m cannot prove SQB.
```

## 3. What kind of identity could prove it

To obtain `EXP-C`, the residues must satisfy a one-sided Paley-Wiener cancellation. In finite form,
there must exist a function `G_x` analytic in a rectangle of width at least `sigma` such that

```text
xi_m = residue/sample data of G_x at d_m,
```

and the Cauchy sum is an exact discrete contour transform whose right-half-plane contribution cancels:

```text
C_x(iz)
= e^(-zL) H_x(z) + polynomially small terms,          Re z>0,
```

with

```text
H_x(z)=O(L^B(1+|z|)^B).
```

Equivalently,

```text
(1-e^(zL))C_x(iz)
= -H_x(z) + lower-order terms.
```

This is the missing theorem. Call it:

```text
PW-Cauchy:
C_x(iz) has right-sided exponential type at most -L after the finite Weyl numerator is imposed.
```

## 4. Relation to RH difficulty

For an off-line zero with

```text
z_rho=rho-1/2,        Re z_rho>0,
```

the compact zero contribution contains

```text
(1-e^(z_rho L))C_x(i z_rho).
```

Without `EXP-C`, this term grows exponentially. Hence any proof of compact-root annihilation must
produce either:

```text
1. pointwise EXP-C / PW-Cauchy; or
2. exact packet cancellation over the zero quadruple; or
3. a contour identity whose vertical sides encode the same exponential cancellation.
```

All three are equivalent in strength at this stage. They are not consequences of finite real-root
divisibility alone.

## 5. Consequence for the proof plan

The next theorem cannot be a generic estimate for `xi`. It must use the actual pole-even CCM equation.
The only admissible analytic target is:

```text
PW-Cauchy from the finite eigenvector equation:

C_E xi = mu xi
  =>
(1-e^(zL)) sum_m xi_m/(iz-d_m)
   = O_{sigma,H}(L^B(1+|z|)^B)
```

in fixed shifted strips, with no use of the limiting `Xi` divisor.

This is the compact-route analogue of the original scalar WRL resonance annihilation. It is sharper
and cleaner, but still genuinely new mathematics.

## 6. Status

```text
proved: polynomial/variation bounds for xi cannot imply SQB;
reduced: SQB to the one-sided Paley-Wiener Cauchy identity PW-Cauchy;
open:   derive PW-Cauchy from C_E xi = mu xi.
```

This is the analytic wall now. It is no longer hidden behind finite matrices.
