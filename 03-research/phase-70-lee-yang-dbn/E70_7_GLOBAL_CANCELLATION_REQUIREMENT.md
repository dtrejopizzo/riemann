# E70.7 — The AHM proof cannot be local per prime

**Date:** 2026-07-07.
**Role:** close the next tempting attack on the Hardy-Euler inequality: proving it by assigning an
independent positive archimedean budget to each prime.

## Target inequality

The Hardy-Euler form is

```text
2 Re sum_{n>=2} Lambda(n)n^{-1/2} C_f(log n) <= A[f].
```

Equivalently,

```text
sum_p 2 Re sum_{k>=1} (log p)p^{-k/2} C_f(k log p) <= A[f].
```

A natural proof attempt is to split the archimedean budget:

```text
A[f] = sum_p A_p[f],
```

and prove for each prime:

```text
2 Re sum_{k>=1} (log p)p^{-k/2} C_f(k log p) <= A_p[f].
```

This would be wonderful: it would convert the global Euler inequality into independent local
positivity statements.

It cannot work in any smooth finite-mass form.

## Frequency-side obstruction

Testing against positive-definite autocorrelations and dualizing by Bochner, a per-prime domination by
a positive density `sigma_p` requires

```text
hat(sigma_p)(xi)
  >= D_p(xi)
  := 2 sum_{k>=1} (log p)p^{-k/2} cos(k xi log p)
```

for every real `xi`.

But `D_p` is periodic/almost-periodic with resonant peaks

```text
D_p(2 pi m/log p) = 2 log p / (sqrt(p)-1),
```

which do not decay as `|xi| -> infinity`.

If `sigma_p` is an `L^1` density, then by Riemann-Lebesgue

```text
hat(sigma_p)(xi) -> 0.
```

Therefore the inequality fails at large resonances.

This is exactly P52's `W5` obstruction in the language of the Hardy-Euler autocorrelation inequality.

## Consequence

The archimedean form cannot be distributed into smooth finite-mass positive pieces that dominate each
prime separately.

Thus AHM cannot be proved by:

- per-prime positive majorants;
- local Bochner densities;
- independent prime-wise Carleson embeddings;
- termwise Cauchy-Schwarz;
- any mechanism that ignores cross-prime phase cancellation.

## What remains possible

Only two kinds of proof remain:

### 1. Global cancellation proof

Keep the full Euler sum

```text
sum_{p,k} (log p)p^{-k/2} C_f(k log p)
```

intact and prove cancellation across all prime powers at once.

This is the real AHM route.

### 2. Singular/atomic archimedean realization

Allow the archimedean budget to contain an atomic or almost-periodic component capable of matching the
nondecaying resonances of each prime.

But if that component reconstructs

```text
product_p (1-p^{-s})^{-1}
```

as a partition function or KMS weight, the proof falls back to Phase 51/MW-5.

So any singular realization must be canonical from the Gamma/polar side and not secretly Euler-zeta.
No such object is currently known.

## Exact remaining theorem

The closure theorem is therefore:

### Global Hardy-Euler Cancellation

For every Hardy autocorrelation `C_f`,

```text
2 Re sum_{p,k>=1} (log p)p^{-k/2} C_f(k log p) <= A[f],
```

and the proof must use global cancellation among the complete set `{k log p}`.

This is precisely the nonlocal arithmetic content of RH.

## Status

The per-prime route is closed negatively. The target is now narrower:

```text
prove AHM by a global Euler cancellation identity,
not by local prime domination.
```

