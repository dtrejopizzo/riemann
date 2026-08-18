# E78.70 - A quadratic phase barrier is a sufficient shell-sign criterion

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.69 reduced the live shell sign to the exact barrier inequality

```text
Re Delta ell_N > -log cos(beta_N),                       (LQQ-1)
beta_N := |wrap Im Delta ell_N|,                         (LQQ-2)
```

on the admissible sector `beta_N < pi/2`.

This note gives a simpler sufficient condition by replacing the exact angular
barrier with a quadratic upper bound.

## 2. Elementary barrier bound

For `0 <= x <= 1`, define

```text
g(x) := x^2 + log cos x.                                 (LQQ-3)
```

Then

```text
g'(x) = 2x - tan x.                                      (LQQ-4)
```

On `[0,1]`, one checks `tan x <= 2x`, so `g'(x) >= 0`. Since `g(0)=0`, we get

```text
-log cos x <= x^2,    0 <= x <= 1.                       (LQQ-5)
```

Therefore, whenever

```text
beta_N <= 1                                              (LQQ-6)
```

we have the implication

```text
Re Delta ell_N > beta_N^2
=> Re Delta ell_N > -log cos(beta_N)
=> LOGQ-BARRIER
=> LOGQ-GAIN-SIGN.                                       (LQQ-7)
```

So the exact shell sign is implied by the simpler sufficient target

```text
LOGQ-QUADRATIC-BARRIER:
  beta_N <= 1
  and
  Re Delta ell_N > |wrap Im Delta ell_N|^2.              (LQQ-8)
```

## 3. Probe audit

Companion:

```text
E78_70_logq_quadratic_barrier_probe.py
E78_70_logq_quadratic_barrier_results.json
```

Across the common certified ladder:

### Zeta

```text
max beta_N = 3.417e-3 << 1,
quadratic margin
  min = 1.010e-1,
  median = 1.190e-1,
  max = 2.202e-1.                                        (LQQ-9)
```

So zeta satisfies the quadratic sufficient barrier with very large margin on
every audited row.

### Planted build

```text
max beta_N = 1.620e-1 < 1,
quadratic margin
  min = -1.017,
  median = -3.137e-1,
  max = 1.247.                                           (LQQ-10)
```

The planted build already fails at the quadratic level because the radial drift
itself turns negative enough to lose even this weaker barrier.

## 4. Consequence

This is a legitimate reduction, with explicit implication:

```text
LOGQ-QUADRATIC-BARRIER
=> LOGQ-BARRIER
=> LOGQ-GAIN-SIGN.                                       (LQQ-11)
```

The live shell target can therefore be sharpened to the more elementary
quadratic barrier law.

## 5. Candid reading

This note does not prove the quadratic barrier. It proves that doing so would be
enough.

It also makes the geometric content very transparent: on the audited zeta rows,
the phase penalty is so tiny that even the crude barrier `beta^2` is utterly
dominated by the positive radial drift.

So the next theorem-grade step can focus on:

```text
positive radial old-old log drift,
with wrapped phase small enough that beta^2 stays below it. (LQQ-12)
```

## 6. Status

```text
proved:
  on beta <= 1, the exact barrier -log cos(beta) is bounded above by beta^2;

proved:
  therefore Re Delta ell_N > |wrap Im Delta ell_N|^2 is a sufficient shell-sign
  criterion;

observed:
  zeta satisfies this quadratic criterion on every audited row with large
  positive margin, while the planted build does not;

reduced:
  LOGQ-BARRIER to the sufficient target LOGQ-QUADRATIC-BARRIER.
```
