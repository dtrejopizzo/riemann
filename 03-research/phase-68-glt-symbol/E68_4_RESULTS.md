# E68.4 -- the prime-comb hypothesis FAILS; Omega_7 localizes near theta ~ pi/2

**Date:** 2026-07-06.
**Script:** [E68_4_prime_comb.py](E68_4_prime_comb.py).

## Self-correction

Hypothesis (E68.3): sigma_P is a prime comb with single-frequency peaks at theta ~ f(log n). **False.**
The single-frequency symbols all peak near `theta ~ -pi/2 ~ -1.571`, independent of n:

```
n:    2      3      5      7     11     13     17     19
th:  -1.583 -1.563 -1.660 -1.547 -1.726 -1.399 -1.654 -1.442   (scatter +-0.15, NON-monotone)
affine fit slope = 0.0275 ~ 0  -> NOT a comb.
```

The script's auto-verdict "CLEAN comb" was misled: the small fit residual comes from all peaks
CLUSTERING at one point, not from a meaningful affine map. The peak location is fixed by the gauge
(`e^{-i z0 L}`, `z0 = t0 - iy`), not by the frequency `log n`. The frequencies do not resolve in theta.

## Honest structure

`sigma_P` is a **single piled-up peak** near `theta ~ pi/2`, not a comb: all primes contribute at the
same location with heights `~ Lambda(n) n^{-1/2-y}`. So:

- The envelope statement `Omega_7 <=> sigma_A >= sigma_P` still holds (still `conj:envelope`), but
  `sigma_P` is a peak, not a comb.
- **Omega_7 localizes to a neighborhood of `theta ~ pi/2`** -- exactly where E67.19 found the zeta
  symbol touch point (theta* ~ 1.54). The entire terminal difficulty concentrates at one point of the
  circle.

## Net

```
dead   : prime-comb-over-log-frequencies picture
solid  : sigma_P is a gauge-localized peak near theta ~ pi/2; Omega_7 concentrates there
next   : characterize sigma_A and sigma_P in the neighborhood of theta ~ pi/2 (the touch point);
         the terminal positivity is a LOCAL inequality at one frequency, not a global comb bound
```

Localization is progress: it says Omega_7 is decided in a neighborhood of a single symbol point. The
Weil-hard core is unchanged, but the arena is one point of the circle, not the whole of it.
