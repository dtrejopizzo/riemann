# E70.12 -- Riccati/curvature test for the Mobius connection

**Date:** 2026-07-07.
**Role:** compute the first structural identity after `V_Lambda = Z^{-1}delta Z` and test whether it
can generate the Gamma/polar majorant.

## Setup

From E70.11,

```text
A_Euler := Z^{-1}delta Z
         = sum_{n>=2} Lambda(n)n^{-1/2} S_log n
```

in the critical formal algebra, with Abel regularization understood when needed.

This is a logarithmic derivative, so it satisfies a Riccati identity. Since

```text
Z^{-1}Z = I,
```

we have

```text
delta(Z^{-1}) = -Z^{-1}(delta Z)Z^{-1}.
```

Therefore

```text
delta(A_Euler)
 = delta(Z^{-1}delta Z)
 = -Z^{-1}(delta Z)Z^{-1}(delta Z) + Z^{-1}delta^2 Z
 = -A_Euler^2 + Z^{-1}delta^2 Z.
```

Equivalently,

```text
delta(A_Euler) + A_Euler^2 = Z^{-1}delta^2 Z.
```

## Coefficient form

Since

```text
A_Euler = sum_n Lambda(n)e_n,
```

the two terms are

```text
delta(A_Euler)
 = sum_n Lambda(n)(log n)e_n,
```

and

```text
A_Euler^2
 = sum_n (Lambda * Lambda)(n)e_n.
```

On the other side,

```text
Z^{-1}delta^2 Z
 = mu * (log^2)
```

as a Dirichlet-convolution coefficient. The identity is exactly

```text
Lambda log + Lambda * Lambda = mu * log^2.
```

This is just the second logarithmic derivative of the Euler unit.

## Diagnostic

The Riccati identity is canonical and non-circular, but it is still entirely Euler-side. It does not
produce the Gamma/polar form `A_Gamma` by itself.

Thus the desired dissipativity

```text
2 Re <A_Euler f,f> <= A_Gamma[f]
```

cannot follow from the Euler Riccati identity alone. A separate compatibility identity between the
Euler connection and the Gamma energy is required.

## What would close the proof

The exact missing theorem can now be stated as a curvature-energy comparison:

### Gamma-Euler Connection Bound

For every Cauchy/Hardy test vector `f`,

```text
2 Re <Z^{-1}delta Z f,f>
  <= <G_Gamma f,f>,
```

where `G_Gamma` is the exact Gamma/polar terminal form.

Equivalently,

```text
G_Gamma - (Z^{-1}delta Z + (Z^{-1}delta Z)^*) >= 0.
```

This is AHM/Omega_7 in connection language.

## No-free-lunch result

The Riccati identity proves that the Mobius connection has the correct arithmetic origin, but it does
not provide the sign. It cannot be used as a standalone proof of `Omega_7`, because every term in the
identity is an Euler convolution term:

```text
Lambda log,
Lambda * Lambda,
mu * log^2.
```

No Gamma/polar positivity enters.

Hence:

```text
Mobius connection identity: closes origin of the prime current.
Riccati identity: closes internal Euler curvature.
Missing theorem: Gamma-Euler dissipativity.
```

## Updated route

The only remaining plausible non-circular route is now:

1. keep `A_Euler = Z^{-1}delta Z` as the canonical prime current;
2. identify `G_Gamma` as the positive energy of the same derivation `delta` on the archimedean
   representation;
3. prove that the Euler connection is dissipative with respect to this archimedean energy.

The theorem in step 3 is not a numerical claim and not a factorization by Cholesky. It is the pure
mathematical inequality that would close `Omega_7`.
