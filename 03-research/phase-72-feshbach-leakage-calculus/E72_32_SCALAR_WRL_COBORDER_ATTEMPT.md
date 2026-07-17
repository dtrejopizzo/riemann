# E72.32 -- Coborder attempt for scalar WRL resonance annihilation

**Date:** 2026-07-08.
**Role:** attack the minimal remaining target directly:

```text
R_x^{WRL}(s;rho)
 := x^rho L_x(s;x)
    - int_1^x u^rho partial_uL_x(s;u)du
 -> 0.
```

## 0. Algebraic form of the resonance

If `L_x(s;1)=0`, integration by parts gives

```text
R_x^{WRL}(s;rho)
 = rho int_1^x u^{rho-1}L_x(s;u)du.             (M)
```

Therefore scalar resonance annihilation is a Mellin-vanishing statement for the single kernel
`L_x(s;u)`.

## 1. The only possible non-circular mechanism

The only way to prove `(M)->0` without knowing `rho` is to exhibit a coborder:

```text
L_x(s;u) = u partial_u A_x(s;u) + B_x(s;u),       (CB)
```

where:

```text
A_x(s;1)=A_x(s;x)=0,
int_1^x u^{rho-1}B_x(s;u)du -> 0
```

uniformly for `rho` in compact subsets of the off-critical strip.

Then

```text
rho int_1^x u^{rho-1}u partial_uA_x(s;u)du
 = rho [u^rho A_x(s;u)]_1^x
   - rho^2 int_1^x u^{rho-1}A_x(s;u)du,
```

so one still needs the stronger primitive smallness

```text
int_1^x u^{rho-1}A_x(s;u)du -> 0.               (PS)
```

Thus a first coborder is not enough. The correct identity must be a resolvent coborder:

```text
L_x(s;u)
 = (u partial_u-rho)A_{x,rho}(s;u)+B_x(s;u),     (RCB)
```

but this depends on `rho` and is forbidden unless `A_{x,rho}` is obtained by applying a universal
operator-valued resolvent to the character `u^rho`.

This is the first hard obstruction.

## 2. Universal Mellin coborder

To avoid dependence on zeros, define the Mellin generator

```text
E_u := u partial_u.
```

If there exists a universal operator `N_x(s,E_u)` such that

```text
L_x(s;u)=N_x(s,E_u)B_x(s;u),
```

and

```text
N_x(s,rho)->0
```

for every off-critical zero `rho`, then the resonance vanishes.

But this says exactly that the symbol `N_x(s,z)` has the off-critical zeta divisor in its zero set.
By the zero-filter gate E72.16, this is circular unless `N_x` is produced intrinsically by the finite
CCM/prolate algebra and its zero set is forced before seeing `Xi`.

## 3. Direct contradiction with planted controls

Suppose instead that scalar WRL resonance annihilation holds by a universal estimate on `L_x`:

```text
sup_{rho in K} |rho int_1^x u^{rho-1}L_x(s;u)du| -> 0
```

for compact `K subset {Re rho>1/2}`.

Then the same proof applies to planted off-line finite data using the same prolate/model kernel class,
unless the planted perturbation changes `L_x` outside the controlled class.

But Phase 71 shows planted off-line data are detected precisely by convergence failure, not by loss of
finite real-rootedness. Therefore a universal kernel estimate would make the detector blind. This
contradicts the intended falsifier behavior.

Thus the proof cannot be a universal size/smoothness estimate. It must use the exact arithmetic
structure of the true `xi_x`/`C_x` pair.

## 4. The true missing identity

The only admissible remaining identity is:

### Arithmetic scalar coborder

For the true zeta CCM data, and only through the finite Euler/Gamma construction, the scalar kernel
admits

```text
L_x(s;u)= (E_u - Z_x(E_u)) A_x(s;u)+B_x(s;u),
```

where:

```text
Z_x(E_u) -> an intrinsic finite CCM spectral polynomial,
Z_x(rho) -> rho for the true Xi divisor,
boundary terms vanish,
Mellin(B_x)(rho)->0.
```

This would force the resonance to vanish. But the identity is precisely a finite spectral
identification theorem for the CCM divisor. It is equivalent to Schur-free current convergence.

## 5. Verdict of the direct attempt

The scalar WRL annihilation cannot be proved by:

```text
ordinary integration by parts,
universal Mellin smoothing,
PNT-size bounds,
or zero-independent symbol vanishing.
```

Any successful proof must construct a new finite spectral coborder whose symbol carries the CCM
spectral polynomial intrinsically.

In other words, the target is not an estimate on `L_x`; it is an algebraic identity identifying the
finite CCM spectral polynomial inside the Mellin action on the scalar kernel.

## 6. Status

```text
proved: direct coborder/smoothing attempts reduce to a zero-filter or fail planted controls;
open:   construct the arithmetic scalar coborder from finite CCM data.
```

This document does not close RH. It proves that the requested annihilation cannot be obtained by a
generic analytic estimate. The proof must be a finite spectral identity.
