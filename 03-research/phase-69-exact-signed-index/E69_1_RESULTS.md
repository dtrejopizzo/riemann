# E69.1 -- the gauge-invariant object: the Nevanlinna/Hermite-Biehler condition on -xi'/xi

**Date:** 2026-07-07.
**Scripts:** E69_1_nevanlinna.py (buggy, kept), [E69_1b_nevanlinna.py](E69_1b_nevanlinna.py) (correct).

## Result

The gauge-uniform marginality of `ind_-(A_N - P_lambda)` (E68.5) is explained: the finite-gauge index
is a fragile approximation to a gauge-INVARIANT global quantity -- the Krein-Langer index of `-xi'/xi`,
i.e. its Nevanlinna character. In the z-variable `s = 1/2 + i z` (critical line = real axis), with
`F(z) = xi(1/2 + i z)` and `N(z) = -F'/F(z) = -sum_rho 1/(z - z_rho)`:

```
Omega_7  <=>  Im N(z) >= 0  for all Im z > 0   (no gauge z0; gauge-free).
```

Verified faithful:
- true xi (RH holds): `min Im N = +0.024` over a grid in the upper half-plane;
- planted off-line zero at s=20i (z-image 20+0.5i): `min Im N = -4.70` near the zero.

This is the classical Hermite-Biehler / Laguerre-Pólya characterization (`xi in LP <=> RH`).

## Two self-caught setup bugs (audit-the-audit discipline)

1. `N = -i * dlog` instead of `N = -dlog` -- the extra `i` rotated the imaginary part; fixed.
2. The first grid did not cover the off-line zero's z-image (an off-line zero at `s = beta + i*gamma`
   maps to the LOWER half z-plane; its FE partner lands in the upper half at real part `-gamma`).
   Fixed by planting the zero so its upper-half image `z = 20 + 0.5 i` is on the grid.

The classical condition was correct; the initial code was not. Both bugs were caught before drawing
conclusions.

## Honest status

- **Achieved (point 1):** the gauge-invariant object is identified and verified -- the Nevanlinna
  condition on `-xi'/xi`, gauge-free. This removes the gauge-fragility of Phase 67-68 entirely: the
  symbol was a bad finite-gauge shadow of this global invariant.
- **Not a new crack:** this is the classical Hermite-Biehler terminal object (P51 territory), which is
  Weil-hard to force. But it is now in its cleanest, gauge-free form, with the full Phase 67-68
  understanding of why the gauge-dependent objects were fragile.

## Next (point 2)

Attack `Im N(z) >= 0` structurally, using the Hadamard/Euler-Gamma_q form of `-xi'/xi`. The imaginary
part is `Im N(z) = sum_rho Im(z)/|z - z_rho|^2` -- manifestly >= 0 iff all `z_rho` real. The forcer is
to derive `Im N >= 0` from the Euler product + Gamma_q archimedean factor without assuming the zero
locations. This is the terminal Weil-hard inequality, now gauge-free and explicit.
```
achieved : gauge-invariant object = Nevanlinna condition on -xi'/xi (gauge-free, faithful)
open     : force Im N(z) >= 0 by structure (Euler + Gamma_q), the Weil-hard terminal
```
