# E78.75 - The shell budget is equivalent to a fractional consumption criterion

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.74 expressed the quadratic shell margin exactly as a reserve budget:

```text
Re Delta ell_N - |wrap Im Delta ell_N|^2
 = BASE - TAIL - phase^2.                               (FB-1)
```

This note rewrites that identity in dimensionless form. The result is a cleaner
reduced target: prove that the tail and phase consume less than the full
basepoint reserve.

## 2. Exact fractional identity

Assume the basepoint reserve is positive:

```text
BASE_N(sigma_0) > 0.                                    (FB-2)
```

Divide `(FB-1)` by `BASE_N(sigma_0)` and define

```text
tau_N(sigma) := TAIL_N(sigma_0,sigma) / BASE_N(sigma_0),     (FB-3)
phi_N(sigma) := |wrap Im Delta ell_N(i sigma)|^2 / BASE_N(sigma_0). (FB-4)
```

Then

```text
(Re Delta ell_N - |wrap Im Delta ell_N|^2) / BASE_N
 = 1 - tau_N - phi_N.                                  (FB-5)
```

Therefore the reserve budget from E78.74 is equivalent to

```text
tau_N(sigma) + phi_N(sigma) < 1.                       (FB-6)
```

Equivalently,

```text
slack_N(sigma) := (Re Delta ell_N - |wrap Im Delta ell_N|^2)/BASE_N
                = 1 - (tau_N + phi_N).                 (FB-7)
```

So the live shell target sharpens once more:

```text
FRACTIONAL-BUDGET:
  tau_N + phi_N < 1

<=>
RESERVE-BUDGET
=> LOGQ-QUADRATIC-BARRIER
=> LOGQ-GAIN-SIGN.                                     (FB-8)
```

## 3. Probe audit

Companion:

```text
E78_75_fractional_budget_probe.py
E78_75_fractional_budget_results.json
```

The probe reconstructs the exact identity

```text
slack_N = 1 - (tau_N + phi_N)                          (FB-9)
```

from the certified `E78.74` rows, with

```text
zeta:   max identity error = 0,
plant:  max identity error = 0.                        (FB-10)
```

### Zeta

Across the full audited ladder:

```text
tau_N + phi_N
  min    = 6.249e-9,
  median = 3.007e-3,
  max    = 9.619e-2,                                   (FB-11)

slack_N
  min    = 9.038e-1,
  median = 9.970e-1,
  max    = 1.000.                                      (FB-12)
```

So on every audited zeta row, the total budget consumption stays below `10%`,
leaving more than `90%` of the normalized reserve untouched even at the worst
audited point.

### Planted build

The plant does not preserve a coherent fractional-budget regime:

```text
tau_N + phi_N
  min    = -4.115e-2,
  median = 5.997e-5,
  max    = 1.054e-1,                                   (FB-13)
```

but this no longer has direct shell-sign meaning because the planted build does
not preserve the positive-base hypothesis `(FB-2)`. The discriminant failure is
already upstream, at the basepoint reserve itself.

## 4. Consequence

This makes the remaining burden very concrete:

```text
prove:
  (i) BASE_N(0.55) > 0,
  (ii) tau_N(sigma) + phi_N(sigma) < 1                 (FB-14)
```

cofinally on the admissible ladder. Item `(i)` is exactly E78.73's old-old
radial contraction law; item `(ii)` is now a normalized consumption estimate.

So the shell front has been reduced to a dimensionless inequality rather than a
raw signed scalar.

## 5. Honest reading

This note does not prove a cofinal bound like `tau_N + phi_N <= c < 1`.

What it does prove is that such a bound is exactly what remains once the
basepoint reserve has been identified. In particular, it cleanly separates the
front into:

```text
BASE positivity   +   normalized consumption < 1.      (FB-15)
```

That is strictly sharper than the unfactored reserve inequality of E78.74.

## 6. Status

```text
proved:
  after dividing by the positive basepoint reserve, the shell budget is exactly
  slack = 1 - (tail/base + phase^2/base);

proved:
  FRACTIONAL-BUDGET is equivalent to RESERVE-BUDGET and therefore implies
  LOGQ-GAIN-SIGN;

observed:
  on the audited zeta ladder the total normalized consumption stays below
  9.62e-2, leaving normalized slack above 9.03e-1 throughout;

reduced:
  the live shell target to BASE positivity plus the dimensionless bound
  tail/base + phase^2/base < 1.
```
