# E72.1 -- The pole-relative Feshbach leakage theorem

**Date:** 2026-07-07.
**Role:** replace the too-strong global residual estimate of E71.17 by a strictly weaker ground-state
leakage estimate.

## 0. Why this phase exists

Phase 71 ended with the estimate

```text
||H_x-H_x^0|| = o(g_x),
```

where `H_x` is the pole-relative CCM/Weil operator, `H_x^0` is the prolate model operator, and `g_x` is
the spectral gap above the prolate ground state.

That estimate is clean but too strong. Phase 65 already taught us that global strong-resolvent control
across the strip is exactly the wall. The ground-state vector does not require global control. It only
requires that the arithmetic perturbation does not push the prolate ground vector into the orthogonal
complement.

This document proves the precise theorem.

## 1. Setup

Let `H` be a Hilbert space. For each `x`, let

```text
H_x^0
```

be a self-adjoint prolate model operator with a simple isolated lowest eigenvalue `mu_x^0` and
normalized eigenvector

```text
k_x = k_lambda,        lambda=sqrt(x).
```

Let

```text
P_x = |k_x><k_x|,      Q_x = I-P_x.
```

Assume the model complement has a gap

```text
Q_x(H_x^0-mu_x^0)Q_x >= g_x Q_x,      g_x>0.
```

Let the pole-relative CCM/Weil operator be

```text
H_x = H_x^0 + R_x,
```

where `R_x` is self-adjoint on the working finite/restricted domain. The pole mode has already been
removed by the Feshbach shorting from Phase 65; all objects below live on the primitive complement.

Write the block decomposition relative to `P_x H plus Q_x H`:

```text
a_x = <k_x,R_x k_x>,
b_x = Q_x R_x k_x,
C_x = Q_x(H_x-mu_x^0-a_x)Q_x.
```

Thus `a_x` is the harmless diagonal energy shift, `b_x` is the leakage vector, and `C_x` is the
compressed complement after the same scalar energy recentering.

## 2. The new estimate

The estimate that should replace global strong-resolvent convergence is:

### Leakage estimate L72

There are constants `c>0` and `x_0` such that for `x>=x_0`,

```text
C_x >= c g_x Q_x,
```

and

```text
||b_x||/g_x -> 0.
```

The first condition says that the complement gap does not collapse after pole-relative shorting. The
second says that the arithmetic perturbation has asymptotically no off-diagonal coupling out of the
prolate ground line.

This is strictly weaker than `||R_x||=o(g_x)`. The block `Q_x R_x Q_x` may be large; it only has to keep
the recentered complement above the ground channel.

## 3. Theorem 72.1 -- Feshbach leakage controls the ground state

Assume L72. Then `H_x` has a unique lowest eigenvector `theta_x` in the spectral island near
`mu_x^0+a_x`, and, after choosing the phase by `<theta_x,k_x> > 0`,

```text
||theta_x-k_x|| <= O(||b_x||/g_x).
```

In particular, if the Fourier transform map is locally bounded on compact substrips of
`|Im z|<1/2`, then

```text
hat theta_x - hat k_x -> 0
```

locally uniformly on the strip. By E71.17 and Connes Fact 6.4, this implies the stable CCM divisor
converges to the divisor of `Xi`, hence RH.

### Proof

Recenter the operator by the model ground energy and diagonal perturbation:

```text
T_x = H_x - mu_x^0 - a_x.
```

In block form,

```text
T_x =
  [ 0      b_x^* ]
  [ b_x    C_x   ].
```

For `u in Q_x H`, consider vectors of the form

```text
psi = alpha k_x + u.
```

The eigenvalue equation `T_x psi = delta psi` becomes

```text
b_x^* u = delta alpha,                 (1)
alpha b_x + C_x u = delta u.           (2)
```

For `|delta| <= (c/2)g_x`, the operator `C_x-delta` is invertible on `Q_x H`, with

```text
||(C_x-delta)^(-1)|| <= 2/(c g_x).
```

Equation (2) gives

```text
u = -alpha (C_x-delta)^(-1)b_x.
```

Substituting into (1), and assuming `alpha != 0`, gives the scalar Feshbach equation

```text
delta = - b_x^*(C_x-delta)^(-1)b_x.    (F)
```

For `|delta| <= (c/2)g_x`, the right side has size at most

```text
2 ||b_x||^2/(c g_x).
```

Since `||b_x||/g_x -> 0`, this lies inside the interval `[-(c/2)g_x,(c/2)g_x]` for large `x`.
Moreover the derivative in `delta` is bounded by

```text
||b_x||^2 ||(C_x-delta)^(-1)||^2
 <= 4 ||b_x||^2/(c^2 g_x^2) = o(1),
```

so (F) has a unique fixed point `delta_x` in that interval.

The corresponding complement component is

```text
u_x = -alpha_x (C_x-delta_x)^(-1)b_x,
```

hence

```text
||u_x|| <= |alpha_x| 2||b_x||/(c g_x).
```

After normalization, `|alpha_x| -> 1`, and therefore

```text
||theta_x-k_x|| <= C ||b_x||/g_x
```

for a constant `C` depending only on `c`.

The complement lower bound also prevents any other eigenvalue from entering this island: all vectors
orthogonal to the two-dimensional graph above have quadratic form bounded below by a positive multiple
of `g_x` for large `x`. Thus the lowest spectral island is simple.

If the Fourier transform map satisfies

```text
sup_{z in K} |hat f(z)| <= C_K ||f||
```

on each compact `K subset {|Im z|<1/2}`, then

```text
sup_K |hat theta_x-hat k_x| <= C_K ||theta_x-k_x|| -> 0.
```

E71.17 then gives the stable-divisor convergence and RH. QED.

## 4. What has been gained

E71.17 asked for global residual control. E72.1 shows that this is unnecessary.

The exact object to estimate is now the leakage vector

```text
L_x := Q_x R_x k_x
     = Q_x (H_x-H_x^0) k_lambda.
```

The scalar

```text
ell_x := ||L_x||/g_x
```

is the **pole-relative arithmetic leakage**.

E72.3 sharpens this: raw leakage is only a sufficient condition. The eigenvector is actually controlled
by the reduced leakage

```text
C_x^{-1}L_x,
```

so high-mode leakage is harmless when it is killed by the complement inverse.

The CCM route closes if

```text
ell_x -> 0
```

and the compressed complement gap remains open. The sharper E72.3 route only asks for

```text
||C_x^{-1}L_x|| -> 0.
```

## 5. Why this avoids the old walls

### Not Phase 65 strong-resolvent convergence

We do not need `H_x -> H_x^0` in operator norm or strong resolvent sense. The complement block
`Q_x R_x Q_x` may be large. Only the channel that couples the prolate ground vector to its complement
has to be small.

### Not Weil positivity

No positivity of the limiting Weil form is assumed. The theorem is perturbative around the prolate
ground state. It uses a complement gap and a leakage estimate, not `QW >= 0`.

### Not Sz.-Nagy / Stone / Hilbert-Polya

There is no claim that the zeros are the spectrum of a global self-adjoint operator. Finite real-zero
functions come from the CCM theorem; the limit is obtained by local uniform convergence of Fourier
transforms.

### Not KMS / zeta partition

The leakage vector is computed from the finite pole-relative Weil operator and the prolate model state.
No Gibbs state with partition function `zeta` is introduced.

## 6. What must be invented next

The missing theorem is now:

### Arithmetic leakage theorem

For the actual CCM/Weil operator `H_x`, the actual pole-relative shorting, and Connes's prolate model
state `k_lambda`,

```text
||Q_x (H_x-H_x^0) k_lambda|| = o(g_x),
```

and

```text
Q_x(H_x-mu_x^0-a_x)Q_x >= c g_x Q_x.
```

This theorem is not currently available in classical operator theory or in the Connes literature we
audited. It is the first "off the shelf" theorem that would have to exist. E72.3 sharpens it by replacing
the raw norm above with the reduced norm `||C_x^{-1}Q_x(H_x-H_x^0)k_lambda||`.

## 7. How I would try to prove the arithmetic leakage theorem

The first sufficient approach is to expand the leakage vector against prolate complement modes:

```text
<e_{x,j}, (H_x-H_x^0) k_lambda>,        j>=1.
```

The goal is not to bound the absolute sum of prime cells. That returns to the incoherent ceiling from
Phase 67.

The first tempting formulation would be to make each complement matrix element into a local
Poisson/Christoffel kernel. That is **not allowed**: Phase 32 already refuted the exact PCN and corrected
the Christoffel scale to `O(1)`, not `1/log gamma`. The old locality route is dead.

The corrected E72.1 goal is weaker and more global than operator-norm convergence: prove that the
**projected vector**

```text
Q_x R_x k_lambda
```

has small norm after the pole-relative Feshbach shorting, even though its individual Jacobi/Christoffel
components may oscillate and need not be local. In complement coordinates this means:

```text
sum_{j>=1} |<e_{x,j}, R_x k_lambda>|^2 = o(g_x^2).
```

E72.3 shows that even this is stronger than necessary. The final reduced target is

```text
sum_{j>=1} |<e_{x,j}, R_x k_lambda>|^2/lambda_{x,j}^2 -> 0,
```

where `lambda_{x,j}` are the eigenvalues of the actual compressed complement `C_x`.

The desired identity should therefore look like:

```text
<e_{x,j}, R_x k_lambda>
  = lambda_{x,j} u_{x,j}^{Feshbach/Sonin} + Tail_{x,j},
```

with

```text
sum_j |u_{x,j}^{Feshbach/Sonin}|^2 -> 0
```

because the coboundary part is killed by the complement inverse, and

```text
sum_{j>=1} |Tail_{x,j}|^2/lambda_{x,j}^2 -> 0.
```

This is the genuinely new analytic object:

```text
an arithmetic Feshbach-Sonin projected integration-by-parts formula for the pole-relative Weil operator.
```

It would turn prime interference into an exact null identity at the level of the **leakage vector**,
instead of trying to dominate the prime sum by absolute values or localize Christoffel kernels at zeta
zeros.

## 8. Falsifier

For Davenport-Heilbronn or a planted off-line deformation, the same construction should produce

```text
liminf ell_x > 0
```

or collapse of the complement gap. If `ell_x -> 0` also holds for planted/off-line controls, then the
leakage theorem is too weak or circular.

## 9. Status

```text
proved:   Feshbach leakage theorem;
new:      the correct smaller estimate ell_x -> 0 replaces global residual convergence;
open:     arithmetic Feshbach-Sonin reduced projected leakage cancellation for actual CCM data.
```

This is the best "off the shelf but nonexistent" tool I would build: not another global spectral
realization, but a pole-relative Feshbach calculus that only measures the one coupling capable of
moving the prolate ground state.
