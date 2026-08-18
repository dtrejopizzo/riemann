# E78.27 - Quantitative contraction form of `SAFE-U-DECAY`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.26 reduced the sign side of IDENT to

```text
SAFE-U-DECAY:
  A_N > A_{N+2},                                           (SCN-1)
```

for the real sequence

```text
A_N := N Delta safe_u_N.                                   (SCN-2)
```

This note records the corresponding ratio form, which is the natural
quantitative strengthening of `(SCN-1)`.

## 2. Exact ratio form

Whenever `A_N != 0`, define

```text
rho_N := A_{N+2}/A_N.                                      (SCN-3)
```

Then `(SCN-1)` is equivalent to

```text
rho_N < 1                                                  (SCN-4)
```

on the rows where `A_N > 0`.  Therefore a uniform bound

```text
rho_N <= rho_* < 1                                         (SCN-5)
```

would be a theorem-grade quantitative envelope for the sign target.

This gives the sharpened target:

```text
SAFE-U-CONTRACTION:
  prove a cofinal ratio bound rho_N <= rho_* < 1
  for A_N = N Delta safe_u_N.                              (SCN-6)
```

## 3. Probe audit

Companion:

```text
E78_27_safe_u_contraction_probe.py
E78_27_safe_u_contraction_results.json
```

### Zeta

At `sigma=1.0`, the audited ratios are

```text
0.80898, 0.81793, 0.85800, 0.84839, 0.88082.              (SCN-7)
```

At `sigma=3.0`,

```text
0.82015, 0.82398, 0.86216, 0.85094, 0.88279.              (SCN-8)
```

So on the audited zeta ladder:

```text
0.80898 <= rho_N <= 0.88279                               (SCN-9)
```

for `sigma in {1.0,3.0}`.

This is a strong hint that the sign front may admit a uniform contraction law,
not just bare monotonicity.

### Planted build

The planted ratios are unstable and eventually invalid as contraction factors.

At `sigma=1.0`:

```text
0.39451, 0.04317, -0.68575, 0.52236, -0.45782.            (SCN-10)
```

At `sigma=3.0`:

```text
0.90720, 0.25813, -0.13995, 0.61337, -3.66441.            (SCN-11)
```

So the plant fails not only decay but the whole contraction geometry:

```text
the ratio can change sign and leave any stable interval inside (0,1). (SCN-12)
```

## 4. Consequence

The sign front now has two candid nested versions:

```text
SAFE-U-CONTRACTION   => SAFE-U-DECAY
SAFE-U-DECAY         => SAFE-U-WEIGHTED-MONOTONICITY
                      => THETA-SIGN-STABILITY.            (SCN-13)
```

This is a useful refinement because `(SCN-6)` is much closer to an envelope
theorem than raw monotonicity.

## 5. Candid reading

This note does **not** prove a theorem-grade `rho_* < 1` bound.  It only shows
that the audited zeta rows already live in a narrow contraction band, while the
planted build does not support any comparable ratio law.

That is exactly the kind of reduced target we want:

```text
one-dimensional, exact, quantitative, and falsifier-sensitive. (SCN-14)
```

## 6. Status

```text
proved:
  SAFE-U-DECAY is equivalent to the ratio inequality rho_N < 1;

observed:
  on the audited zeta rows, rho_N stays in the narrow band
  0.80898-0.88279 for sigma in {1,3};

observed:
  the planted build has unstable ratios, including sign changes and large
  negative excursions;

reduced:
  the sign side of IDENT from SAFE-U-DECAY to the stronger quantitative target
  SAFE-U-CONTRACTION;

next:
  search for a theorem-grade derivation of rho_N <= rho_* < 1 from the
  u-sector law and the exact shell update formulas for safe_u.
```
