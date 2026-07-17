# E70.8 — Abel regularization and the boundary-loss obstruction

**Date:** 2026-07-07.
**Role:** test the natural global-cancellation route: prove the Hardy-Euler inequality in a convergent
Euler region and pass to the critical boundary.

## Abel family

Introduce an Abel parameter `epsilon>0` and define the softened prime-shift operator

```text
T_epsilon
  = sum_{n>=2} Lambda(n)n^{-1/2-epsilon}(S_log n + S_log n^*).
```

For Hardy tests with exponential decay this is well-defined. In frequency language, this corresponds
to the regularized Euler symbol

```text
2 Re sum_{n>=2} Lambda(n)n^{-1/2-epsilon+i xi}
```

where convergence becomes honest once the effective real part is to the right of the Euler-product
line.

The desired terminal operator is the boundary value

```text
T_0 = lim_{epsilon downarrow 0} T_epsilon.
```

The target is

```text
A - T_0 >= 0.
```

## What the Abel route would need

The clean proof shape would be:

1. Prove interior positivity:

```text
A_epsilon - T_epsilon >= 0       (epsilon > epsilon_0)
```

in the Euler-convergent region.

2. Prove no boundary loss:

```text
liminf_{epsilon downarrow 0} (A_epsilon - T_epsilon) >= 0.
```

3. Conclude:

```text
A - T_0 >= 0.
```

This would close `Omega_7`.

## Boundary-loss theorem

The second step is exactly the hard part.

Let

```text
H_epsilon := A_epsilon - T_epsilon
```

and suppose `H_epsilon` converges distributionally to `H_0`. Then the only possible obstruction to
passing positivity to the boundary is a negative spectral defect in the limit:

```text
there exist f_epsilon -> f such that
  <H_epsilon f_epsilon,f_epsilon> >= 0
but
  <H_0 f,f> < 0.
```

In the explicit formula this boundary defect is exactly an off-critical zero. More concretely, if a
zero `rho=beta+i gamma`, `beta>1/2`, exists, then the prime error contains a term

```text
x^rho / rho
```

and one can choose Hardy autocorrelations resonant with `gamma` and with growth tuned to `beta-1/2`;
the boundary form becomes negative. Conversely, if no such zero exists, the boundary defect vanishes.

Therefore:

```text
no Abel boundary loss  <=>  no off-line zeros  <=>  RH  <=>  Omega_7.
```

## Why this is still useful

The Abel route converts the problem into a stability theorem:

### Critical Abel Stability

The positive forms `H_epsilon` in the Euler region have no negative spectral loss as
`epsilon downarrow 0`.

This is an exact restatement of the arithmetic direction `Lambda<=0`.

It is sharper than "prove RH" because it identifies the mechanism:

```text
control the boundary spectrum of the Euler-prime shift operator.
```

But it is not a solved theorem.

## Why ordinary compactness does not solve it

Strong or weak convergence of forms does not preserve positivity on a changing domain when the limit is
singular and the test family can concentrate at the critical boundary. The resonant Hardy functions can
move with `epsilon` and detect precisely the off-line zero contribution.

This is the same concentration phenomenon seen earlier as:

- the `S_abs` incoherent ceiling;
- the gauge fragility of the symbol;
- the de Bruijn-Newman direction problem;
- the Laguerre kernels reaching `x ~ exp(4N)`.

## Status

The Abel route is not dead, but its only missing lemma is RH-strength:

```text
Critical Abel Stability
  <=> AHM
  <=> Lambda <= 0
  <=> Omega_7.
```

So the proof cannot be "interior positivity plus continuity"; the continuity at the critical boundary
is exactly where the theorem lives.

