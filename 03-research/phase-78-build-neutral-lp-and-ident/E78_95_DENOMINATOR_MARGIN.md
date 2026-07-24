# E78.95 - `U-RADIAL-GAP` is exactly a denominator margin after paying numerator loss

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.94 polarized the primary modulus-growth object as

```text
U-RADIAL-GAP_N
 = NUMERATOR-RADIAL-GAIN_N
   + DENOMINATOR-RADIAL-DEFICIT_N.                      (DMG-1)
```

That already showed the denominator side is the orderly one. This note sharpens
the comparison to the exact one-sided form that actually matters for positivity.

## 2. Exact margin identity

Define the nonnegative numerator loss

```text
NUMERATOR-LOSS_N
 := max(0, -NUMERATOR-RADIAL-GAIN_N).                   (DMG-2)
```

Then from `(DMG-1)`:

```text
if NUMERATOR-RADIAL-GAIN_N >= 0,
  U-RADIAL-GAP_N >= DENOMINATOR-RADIAL-DEFICIT_N;       (DMG-3)

if NUMERATOR-RADIAL-GAIN_N < 0,
  U-RADIAL-GAP_N
   = DENOMINATOR-RADIAL-DEFICIT_N - NUMERATOR-LOSS_N.   (DMG-4)
```

Combining both cases yields the universal lower bound

```text
DENOMINATOR-MARGIN:
U-RADIAL-GAP_N
 >= DENOMINATOR-RADIAL-DEFICIT_N - NUMERATOR-LOSS_N,    (DMG-5)
```

with equality whenever `NUMERATOR-RADIAL-GAIN_N <= 0`, which is the persistent
regime on the late audited zeta ladder.

So the positivity target reduces to a one-sided comparison:

```text
DENOMINATOR-RADIAL-DEFICIT_N > NUMERATOR-LOSS_N.        (DMG-6)
```

That is the exact smallest current forcing law for `U-RADIAL-GAP_N > 0`.

## 3. Probe audit

Companion:

```text
E78_95_denominator_margin_probe.py
E78_95_denominator_margin_results.json
```

### Exactness

The late-regime equality reconstruction matches the already certified gap to
roundoff on rows where `NUMERATOR-RADIAL-GAIN_N <= 0`:

```text
max exact reconstruction error on applicable rows
< 1e-15.                                                (DMG-7)
```

### Zeta

Across the certified zeta ladder:

```text
NUMERATOR-LOSS_N
  min    = 0,
  median = 0.397415,
  max    = 0.720711,                                    (DMG-8)

DENOMINATOR-MARGIN
  min    = 0.152534,
  median = 0.329774,
  max    = 0.589192.                                    (DMG-9)
```

On each audited sigma slice:

```text
DENOMINATOR-RADIAL-DEFICIT_N   is monotone increasing,
NUMERATOR-LOSS_N               is monotone increasing,
DENOMINATOR-MARGIN             stays strictly positive.  (DMG-10)
```

Representative rows:

```text
sigma=1.0, N=12:
  denominator deficit = 0.678873
  numerator loss      = 0.206549
  margin              = 0.472324

sigma=1.0, N=20:
  denominator deficit = 0.873246
  numerator loss      = 0.720711
  margin              = 0.152534.                       (DMG-11)
```

So on the healthy branch, positivity of the gap is forced by the statement that
the denominator contraction leaves a strictly positive remainder after paying
the late numerator loss; and on the late rows, that remainder is exactly the
gap itself.

### Planted build

The planted build fails this margin law badly:

```text
DENOMINATOR-MARGIN
  min    = -9.711255,
  median = -2.058117,
  max    = 0.425844,                                    (DMG-12)
```

and it is not nonnegative across the ladder.

So the falsifier breaks at the exact one-sided comparison `(DMG-6)`.

## 4. Consequence

This yields the sharpest primary target so far:

```text
DENOMINATOR-DEFICIT-DOMINANCE:
  DENOMINATOR-RADIAL-DEFICIT_N > NUMERATOR-LOSS_N       (DMG-13)
```

Then

```text
DENOMINATOR-DEFICIT-DOMINANCE
=> U-RADIAL-GAP-LOWER-BOUND
=> PREF-CONTROL + U-RADIAL-GAP-LOWER-BOUND
=> LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT.             (DMG-14)
```

This is an admissible reduction with explicit upward implication.

## 5. Honest reading

This note does **not** prove the cofinal dominance law.

What it proves is that the modulus-growth burden has now been reduced to the
cleanest possible one-sided comparison between two one-dimensional shell
scalars, and that the planted falsifier fails precisely there.

That is a substantial sharpening of the live target.

## 6. Status

```text
proved:
  U-RADIAL-GAP_N is bounded below by the denominator radial deficit after
  paying the nonnegative numerator loss, with equality on the late audited
  zeta regime;

proved:
  the exact late-regime reconstruction holds to roundoff on both builds;

observed:
  on the certified zeta ladder the denominator margin stays strictly positive;

observed:
  the planted build fails exactly by loss of denominator-deficit dominance;

clarified:
  the primary live target is now the one-sided comparison
  DENOMINATOR-RADIAL-DEFICIT > NUMERATOR-LOSS;

next:
  import the denominator radial contraction machinery as the main forcing law
  and isolate the smallest theorem-grade upper bound for the numerator loss.
```
