# E69.2 -- decomposition overturns the arch-cushion hope; positivity is prime-side

**Date:** 2026-07-07.
**Script:** E69_2_decompose.py.

## Test

`N = N_arch + N_prime`, `N_arch = -d/dz log([1/2 s(s-1)] pi^{-s/2} Gamma(s/2))`,
`N_prime = -d/dz log zeta(1/2+iz)`. Hypothesis (point 2): the archimedean part is a positive Nevanlinna
cushion (Gamma in Laguerre-Polya) that could force `Im N >= 0`.

## Result (zeta, upper half z-plane)

```
 x    y    Im N_arch   Im N_prime   Im sum
15   0.2   -0.4335     +0.7024     +0.269
25   0.2   -0.6899     +5.7082     +5.018
40   0.5   -0.9250     +1.5624     +0.637
60   1.0   -1.1278     +2.6554     +1.528
```

**Hypothesis overturned.** `Im N_arch < 0` everywhere (-0.43 .. -1.13): the archimedean factor is a
negative DRAG, not a positive cushion. It grows like `-(1/2) log(height)` (from `Re psi(s/2) ~ log|s/2|`).
The positivity is carried entirely by the PRIME part `Im N_prime > 0`, which dominates and keeps the
sum >= 0 for zeta.

## Consequence

- The idea "Gamma_q forces the Nevanlinna sign" is **false**. The archimedean sector (closed, zeta-free,
  E67.1b/c) does not help force `Im N >= 0` -- it subtracts.
- Positivity lives on the Euler/prime side: `Im(-zeta'/zeta) > 0`, which is exactly where the zeros are.
  An off-line zero drives `Im N_prime` negative near its upper-half image and pulls the sum below 0.
- So the forcer must come from the prime/Euler side, not an archimedean cushion. Weil-hard core
  unchanged -- but the "archimedean envelope dominates" intuition (the symbol-era reading, loosely
  `conj:envelope`) does NOT hold in this exact Nevanlinna decomposition: arch does not dominate, it
  drags. (Caveat: the Nevanlinna split `N_arch + N_prime` is a different decomposition from P52's
  symbol `sigma_A` vs `sigma_P`; this rules out the arch-cushion mechanism HERE, not P52's conjecture
  as stated, until the exact correspondence is pinned.)

## Net

```
overturned : arch is a positive cushion (it is a negative drag ~ -1/2 log height)
solid      : positivity is prime-side, Im(-zeta'/zeta) > 0 <=> (locally) RH
ruled out  : Gamma_q / archimedean domination as the forcer
open       : force Im N_prime to overcome the arch drag by Euler structure -- the Weil-hard terminal,
             now known to live purely on the prime side
```
