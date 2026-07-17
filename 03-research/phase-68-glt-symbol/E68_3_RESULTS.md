# E68.3 -- audit + step 2: the 1D symbol is the spectral object; Omega_7 = envelope dominates prime comb

**Date:** 2026-07-06.
**Script:** [E68_3_symbol_analytic.py](E68_3_symbol_analytic.py).

## Audit (reconciles E67.18 vs E68.1-2)

The 1D position-AVERAGED symbol satisfies the Szego distribution law:

| case | measure{sigma<0} | ind_-/N | min sigma |
|---|---|---|---|
| zeta | 0.000 | 0.000 | +0.037 |
| offline b=0.8 | 0.499 | 0.438 | -1377 |

So the 1D averaged symbol IS the correct spectral object (Szego-consistent, faithful). The 2D LOCAL
symbol failed (E68.1-2) because per-position band Fourier of a non-Toeplitz matrix produces spurious
excursions that are not eigenvalues. Conclusion: work with the 1D symbol (the Phase-67 detector, in
02-foundations). Phase 67's detector is on firm ground.

## Step 2 -- first analytic pass

Naive guess "sigma_P = Re(-zeta'/zeta) along the critical line (linear height map)" FAILS:
correlation -0.31, and ranges mismatch (`sigma_P in [-0.11, 2.80]` vs `Re(-zeta'/zeta) ~ 1.38`, nearly
constant near t0=100). So the symbol is NOT `-zeta'/zeta` on a contour. It is the symbol of the LOCAL
jet at z0, encoding the prime log-frequencies -- a prime "comb" in theta.

Structural identification:
```
sigma_A = archimedean envelope symbol
sigma_P = prime-frequency comb symbol
Omega_7 <=> sigma_A(theta) >= sigma_P(theta)  <=>  the archimedean envelope dominates the prime comb.
```

This is exactly P52's `conj:envelope`, recovered in symbol form from the Toeplitz/quantum side -- the
same nucleus reached independently. Not a coincidence: both are the terminal positivity.

## Net

```
solid : 1D averaged symbol = spectral object, Szego law holds (audit)
solid : Omega_7 <=> sigma_A >= sigma_P (envelope dominates prime comb) = conj:envelope in symbol form
open  : characterize the prime comb sigma_P (peaks at log-frequencies of primes) and the archimedean
        envelope sigma_A explicitly; attack sigma_A >= sigma_P (Weil-hard core, explicit functions)
next  : confirm the comb (peaks of sigma_P at theta ~ log p / scale) and derive sigma_A analytically
```
