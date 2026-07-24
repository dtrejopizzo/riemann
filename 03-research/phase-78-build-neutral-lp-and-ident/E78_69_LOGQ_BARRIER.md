# E78.69 - `LOGQ-GAIN-SIGN` is exactly a radial-vs-angular barrier inequality

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.68 reduced the live shell sign to the exact scalar gain

```text
LOGQ-GAIN_N = 1 - exp(-a_N) cos(b_N),                   (LQB-1)
```

where

```text
a_N := Re Delta ell_N,
b_N := Im Delta ell_N                                  (LQB-2)
```

on the old-old logarithmic shell chain.

This note removes the last ambiguity about what positivity means by rewriting
the sign condition as a sharp barrier inequality.

## 2. Exact barrier form

Let

```text
beta_N := |wrap(b_N)| in [0, pi),                        (LQB-3)
```

where `wrap` denotes reduction modulo `2 pi` into `[-pi,pi]`.

On the admissible sector

```text
beta_N < pi/2,                                           (LQB-4)
```

we have `cos(beta_N)>0`, so

```text
LOGQ-GAIN_N > 0
<=> exp(-a_N) cos(beta_N) < 1
<=> a_N > -log cos(beta_N).                              (LQB-5)
```

Define the exact angular barrier

```text
ANG-BARRIER_N := -log cos(beta_N),                       (LQB-6)
```

and the exact margin

```text
BAR-MARGIN_N := a_N - ANG-BARRIER_N.                     (LQB-7)
```

Then, on `(LQB-4)`,

```text
LOGQ-GAIN_N > 0
<=> BAR-MARGIN_N > 0.                                    (LQB-8)
```

So the old-old shell sign is exactly a competition between:

```text
radial contraction  a_N = Re Delta ell_N,
angular penalty     -log cos(|wrap Im Delta ell_N|).     (LQB-9)
```

## 3. Probe audit

Companion:

```text
E78_69_logq_barrier_probe.py
E78_69_logq_barrier_results.json
```

The scalar reconstruction from `(LQB-1)` through `(LQB-8)` is exact to
roundoff:

```text
zeta:   max reconstruction error = 0,
plant:  max reconstruction error = 0.                    (LQB-10)
```

### Zeta

Across the audited zeta ladder:

```text
ANG-BARRIER_N:
  min = 1.160e-9,   median = 5.127e-7,   max = 5.837e-6

BAR-MARGIN_N:
  min = 1.010e-1,   median = 1.153e-1,   max = 2.202e-1

LOGQ-GAIN_N:
  min = 9.604e-2,   median = 1.089e-1,   max = 1.977e-1. (LQB-11)
```

So zeta lives in a very clean barrier regime:

```text
the angular barrier is tiny,
the radial drift stays uniformly positive and vastly larger,
hence the exact gain stays positive.                     (LQB-12)
```

### Planted build

Across the audited planted ladder:

```text
ANG-BARRIER_N:
  min = 7.390e-7,   median = 6.435e-5,   max = 1.322e-2

BAR-MARGIN_N:
  min = -1.030,     median = -3.695e-1,  max = 1.247

LOGQ-GAIN_N:
  min = -1.766,     median = -4.425e-1,  max = 7.127e-1. (LQB-13)
```

The planted build therefore fails the zeta regime for the sharpest possible
reason: not because the angle becomes huge, but because the radial drift itself
crosses below the exact angular barrier.

## 4. Consequence

This is a genuine sharpening of the live target:

```text
LOGQ-GAIN-SIGN
<=>
LOGQ-BARRIER:
  prove Re Delta ell_N > -log cos(|wrap Im Delta ell_N|) on the zeta cofinal
  path.                                                   (LQB-14)
```

That is still one coupled scalar inequality, but now it is fully explicit and
exact.

## 5. Honest reading

This note does not prove the barrier inequality. It proves that the barrier
inequality is the exact content of the sign question.

In particular, the angular part is already negligible on the audited zeta rows,
so the remaining mathematical burden is to derive:

```text
positive radial drift with an angular penalty small enough to stay below it.
                                                            (LQB-15)
```

The next admissible theorem-grade step is therefore to derive this barrier
regime directly from the invariant `LOGT-CELL` update, not from post hoc
numerics.

## 6. Status

```text
proved:
  on the admissible sector |wrap Im Delta ell_N| < pi/2, positivity of the
  old-old shell gain is exactly equivalent to the barrier inequality
  Re Delta ell_N > -log cos(|wrap Im Delta ell_N|);

observed:
  zeta satisfies this inequality on every audited row with large positive
  margin;

observed:
  the planted build loses the inequality because the radial drift crosses below
  the exact angular barrier;

reduced:
  LOGQ-GAIN-SIGN to the exact scalar target LOGQ-BARRIER.
```
