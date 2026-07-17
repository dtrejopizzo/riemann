# E72.20 -- Poincare-Lelong criterion for CCM divisor-current convergence

**Date:** 2026-07-08.
**Role:** turn the divisor-current convergence needed in E72.19 into a concrete potential convergence
statement for the finite CCM spectral functions.

## 0. Why this criterion matters

E72.19 proves:

```text
finite real-supported divisor currents [D_x] -> [D_Xi]
  => RH.
```

The next question is how to prove `[D_x]->[D_Xi]` without knowing the zeros of `Xi`.

For holomorphic functions the right object is not the zero set directly. It is the subharmonic
potential

```text
log |F|.
```

The divisor is its Laplacian.

## 1. Poincare-Lelong normalization

For a nonzero holomorphic function `F` on the strip `S`,

```text
[D_F] = (1/(2pi)) Delta log|F|
```

as distributions. Equivalently, for `phi in C_c^\infty(S)`,

```text
<[D_F],phi>
 = (1/(2pi)) int_S log|F(z)| Delta phi(z) dA(z).
```

This identity counts zeros with multiplicity and is insensitive to multiplication of `F` by
non-vanishing holomorphic factors whose logarithmic modulus is harmonic.

## 2. Relative gauge

Let `G_x` be the prolate model function from E72.18 and `G` its Cartwright limit. Define

```text
U_x(z) := log|F_x(z)| - log|G_x(z)|,
U(z)   := log|Xi(z)| - log|G(z)|.
```

Then

```text
[D_{F_x}]-[D_{G_x}] = (1/(2pi))Delta U_x,
[D_Xi]-[D_G]        = (1/(2pi))Delta U.
```

If the model divisor currents `[D_{G_x}]` converge to `[D_G]`, then proving `[D_{F_x}]->[D_Xi]` is
equivalent to proving

```text
Delta U_x -> Delta U.
```

A sufficient and natural condition is local `L^1` convergence of potentials:

```text
U_x -> U in L^1_loc(S).                            (PLC)
```

## 3. The criterion

### Theorem 72.20

Assume:

1. `F_x` and `G_x` are holomorphic and not identically zero on `S`;
2. `[D_{G_x}] -> [D_G]` in distributions on `S`;
3. the relative potentials satisfy `(PLC)`:

```text
log|F_x/G_x| -> log|Xi/G|  in L^1_loc(S).
```

Then

```text
[D_{F_x}] -> [D_Xi]
```

in distributions on `S`. Since every finite `F_x` has real zeros, RH follows by E72.19.

### Proof

By Poincare-Lelong,

```text
[D_{F_x}]-[D_{G_x}]
  = (1/(2pi))Delta log|F_x/G_x|.
```

Let `phi in C_c^\infty(S)`. Then

```text
<[D_{F_x}]-[D_{G_x}],phi>
 = (1/(2pi)) int_S log|F_x/G_x| Delta phi dA.
```

The support of `Delta phi` is compact, and `(PLC)` gives `L^1` convergence of the potentials on that
compact set. Therefore

```text
<[D_{F_x}]-[D_{G_x}],phi>
 ->
(1/(2pi)) int_S log|Xi/G| Delta phi dA
 = <[D_Xi]-[D_G],phi>.
```

Using assumption 2 gives `[D_{F_x}]->[D_Xi]`. E72.19 then implies RH. `QED`

## 4. The new analytic target

The exact theorem needed is no longer a zero statement:

### Relative Potential Convergence

In the centered strip,

```text
log|F_x/G_x| -> log|Xi/G|
```

in `L^1_loc`.

This is strictly stronger than pointwise real-axis matching but weaker than tracking individual zeros.
It is the correct Cartwright topology for divisors.

## 5. Non-circularity gate

RPC is admissible if proved from:

```text
finite CCM construction of F_x,
prolate construction of G_x,
Cartwright type bounds,
and an explicit finite-prime/gamma formula for the relative potential.
```

RPC is circular if proved by:

```text
assuming convergence of zero sets,
using RH,
or inserting Xi as an already known divisor correction.
```

## 6. Relation to the leakage route

The leakage route sought:

```text
theta_x -> k_lambda
```

in a Fourier-controlling norm. That implies RPC because Fourier convergence of the spectral functions
gives local uniform convergence away from normalization zeros, hence `L^1_loc` convergence of log
moduli.

But RPC may be weaker. It asks only for convergence of logarithmic potentials, not vector convergence.
This is the first genuinely lower-resolution target after the Feshbach leakage barrier.

## 7. Status

```text
proved: RPC + model divisor convergence => DCC => RH;
open:   prove RPC from finite CCM/prolate data.
```

The next step is to search for a direct formula for the relative potential

```text
log|F_x/G_x|
```

that can be estimated without following eigenvectors.
