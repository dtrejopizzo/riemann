# E71.17 -- Stable Divisor Identification reduced to a ground-state estimate

**Date:** 2026-07-07.
**Role:** convert the source audit from E71.16 into a precise theorem with proof, and isolate the
single analytic estimate that remains unproved.

## Source status

The phrase

```text
the intrinsic stable divisor of (D_N, xi_N) converges to the divisor of Xi
```

is the right Phase 71 slogan, but it is not currently a theorem we can quote from the F1/metaphysics
paper. That paper supplies the global arithmetic-site / Riemann-Weil distribution background. The
finite CCM convergence mechanism is instead the one in Connes `arXiv:2602.04022`, Section 6.

The source-backed chain is:

```text
Theorem 6.1:    Fourier transform of theta_x has only real zeros,
Fact 6.4:       Fourier transform of k_lambda tends locally uniformly to Xi,
Section 6.6:    still missing: theta_x is well approximated by k_lambda.
```

Thus the stable-divisor theorem is equivalent, in this route, to proving the ground-state
approximation

```text
theta_x -> k_lambda
```

in a norm strong enough to control Fourier transforms on compact subsets of the strip.

## Notation

Let

```text
S = {z in C : |Im z| < 1/2}.
```

Let `theta_x` be the normalized even lowest eigenvector of the finite/restricted Weil operator
`QW_x`, when this eigenvalue is simple and isolated. Let

```text
F_x(z) = hat theta_x(z)
```

be its Fourier transform in Connes's centered variable. By Theorem 6.1, every zero of `F_x` is real.

Let `lambda = sqrt(x)` and let `k_lambda=E(h_lambda)` be the prolate model vector in Connes
Section 6.4. Put

```text
G_lambda(z) = hat k_lambda(z).
```

Fact 6.4 states that

```text
G_lambda -> Xi
```

uniformly on compact subsets of `S`.

## Theorem 17.1 -- Stable divisor from ground-state convergence

Assume that, for every compact `K subset S`,

```text
sup_{z in K} |F_x(z)-G_sqrt(x)(z)| -> 0       as x -> infinity.
```

Then

```text
F_x -> Xi
```

locally uniformly on `S`. Consequently the divisor of `F_x` converges, in the Hurwitz sense, to the
divisor of `Xi` inside `S`. Since every `F_x` has only real zeros, every zero of `Xi` in `S` is real.
Equivalently, RH follows.

### Proof

Let `K subset S` be compact. By the assumed ground-state convergence,

```text
||F_x-G_sqrt(x)||_K -> 0.
```

By Connes Fact 6.4,

```text
||G_sqrt(x)-Xi||_K -> 0.
```

The triangle inequality gives

```text
||F_x-Xi||_K <= ||F_x-G_sqrt(x)||_K + ||G_sqrt(x)-Xi||_K -> 0.
```

Thus `F_x -> Xi` locally uniformly on `S`.

Let `rho` be a zero of `Xi` in `S`. If `rho` were non-real, choose a small closed disk
`D(rho,r)` contained in `S` and disjoint from the real axis, with no zeros of `Xi` on its boundary.
Since `Xi` is not identically zero, Hurwitz's theorem implies that, for all sufficiently large `x`,
`F_x` has the same positive number of zeros in `D(rho,r)`, counted with multiplicity. But all zeros
of `F_x` are real, while `D(rho,r)` is disjoint from the real axis. Contradiction.

Therefore all zeros of `Xi` in the centered critical strip are real. In the usual variable
`s=1/2+iz`, this is RH. QED.

## Theorem 17.2 -- Operator-gap criterion for the missing estimate

The previous theorem reduces RH to a function-level estimate. The next step is to reduce that estimate
to a standard perturbative operator statement.

For each `x`, suppose we have two self-adjoint operators on the same Hilbert space:

```text
H_x      = the restricted Weil / CCM operator,
H_x^0    = the prolate model operator,
R_x      = H_x - H_x^0.
```

Assume:

1. `H_x^0` has a simple isolated lowest eigenvalue `mu_x^0` with normalized even eigenvector
   `k_lambda`, `lambda=sqrt(x)`.
2. The spectral gap

```text
g_x = dist(mu_x^0, spec(H_x^0)\{mu_x^0})
```

   is positive.
3. The perturbation is small relative to the gap:

```text
||R_x|| / g_x -> 0.
```

4. The Fourier transform map is locally bounded in the working norm: for every compact `K subset S`
   there is `C_K` such that

```text
sup_{z in K} |hat f(z)| <= C_K ||f||
```

   for all vectors in the relevant finite/restricted space.

Then the normalized lowest eigenvector `theta_x` of `H_x` can be phased so that

```text
sup_{z in K} |hat theta_x(z)-hat k_lambda(z)| -> 0
```

for every compact `K subset S`.

### Proof

Let `P_x^0` be the rank-one spectral projection of `H_x^0` onto `k_lambda`. Take the circle

```text
Gamma_x = {z : |z-mu_x^0| = g_x/2}.
```

For `z in Gamma_x`,

```text
||(z-H_x^0)^(-1)|| <= 2/g_x.
```

If `||R_x|| < g_x/4`, the resolvent identity and Neumann series give

```text
||(z-H_x)^(-1)|| <= 4/g_x.
```

Thus `Gamma_x` stays in the resolvent set of `H_x`, and the Riesz projection `P_x` inside
`Gamma_x` is well-defined. Since `P_x^0` has rank one and the rank of a Riesz projection is stable
under norm-continuous perturbation while the contour stays in the resolvent set, `P_x` is also rank
one.

The Riesz projections satisfy

```text
P_x-P_x^0
 = (1/2pi i) int_{Gamma_x}
   [(z-H_x)^(-1) - (z-H_x^0)^(-1)] dz
 = (1/2pi i) int_{Gamma_x}
   (z-H_x)^(-1) R_x (z-H_x^0)^(-1) dz.
```

Hence

```text
||P_x-P_x^0||
 <= (1/2pi) (pi g_x) (4/g_x) ||R_x|| (2/g_x)
 <= 4 ||R_x||/g_x.
```

For large `x`, `||P_x-P_x^0||<1`. Choose the normalized eigenvector `theta_x` in the range of `P_x`
with positive inner product with `k_lambda`. Standard rank-one projection geometry gives

```text
||theta_x-k_lambda|| <= 2 ||P_x-P_x^0||
                  <= 8 ||R_x||/g_x -> 0.
```

Applying the compact Fourier bound,

```text
sup_{z in K} |hat theta_x(z)-hat k_lambda(z)|
 <= C_K ||theta_x-k_lambda|| -> 0.
```

This proves the ground-state estimate required by Theorem 17.1. QED.

## Exact remaining estimate

The stable-divisor problem is now no longer vague. It is the following operator estimate:

### Estimate 17.E -- Prolate residual below the gap

Construct the prolate model operator `H_x^0` in the same Hilbert model and normalization as the CCM
restricted Weil operator `H_x`, and prove

```text
||H_x-H_x^0|| = o(g_x).
```

Equivalently, in a weaker residual form sufficient for the ground-state vector,

```text
||(H_x-mu_x^0) k_lambda|| = o(g_x)
```

plus a stability bound excluding another eigenvalue in the same gap.

This is the precise place where arithmetic must enter. It cannot be replaced by:

- persistence clustering alone, because planted/off-line controls can have stable non-zeta clusters;
- raw real-rootedness, because Theorem 6.1 makes real zeros automatic for every admissible input;
- an F1 divisor slogan, unless it supplies the same operator-gap estimate.

## Final reduction diagram

```text
Estimate 17.E
  => theta_x -> k_lambda                         (Theorem 17.2)
  => hat theta_x -> Xi                           (Theorem 17.1 + Fact 6.4)
  => stable CCM divisor -> divisor Xi            (Hurwitz)
  => RH                                          (finite real zeros + Hurwitz)
```

## Status

```text
proved here:       Theorem 17.1 and Theorem 17.2;
proved in source:  Fact 6.4, plus the finite-real-zero mechanism under Theorem 6.1 hypotheses;
open:              Estimate 17.E.
```

This is the cleanest current formulation of "CCM Stable Divisor Identification": it is not an
independent black-box theorem, but the consequence of one explicit prolate-vs-Weil ground-state
estimate.

## What to look for in any newer CCM source

If a later Connes--Consani--Moscovici text already contains the missing result, it should appear in
one of these equivalent forms:

```text
hat theta_x - hat k_sqrt(x) -> 0 on compact substrips;
theta_x - k_sqrt(x) -> 0 in a Fourier-controlling norm;
||QW_x - Prolate_x|| = o(gap_x);
||(QW_x-mu_x^0) k_sqrt(x)|| = o(gap_x) plus isolation.
```

A statement only saying that an intrinsic stable divisor exists is not enough unless it proves one of
these estimates or gives an independent local-uniform convergence theorem for `hat theta_x`.
