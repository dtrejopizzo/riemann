# E77.7av - Relative mismatch reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7au identified the smallest explicit shell-side scalar seen so far:

```text
WEIGHTED-INNER-OUTER-MISMATCH
  = r_in sqrt(c) - sgn(b) r_out sqrt(a).
```

That mismatch is candid, but it still carries the overall shell amplitude
scale.  This note records the correct normalization.

## 2. Natural normalization

The companion large-branch amplitude is

```text
BRANCH-AMPLITUDE
  = r_in sqrt(a) + sgn(b) r_out sqrt(c).
```

So the scale-free shell-side defect is

```text
RELATIVE-MISMATCH
  = (r_in sqrt(c) - sgn(b) r_out sqrt(a))
    / (r_in sqrt(a) + sgn(b) r_out sqrt(c)).          (AV-1)
```

In even-basis language this is exactly

```text
ALIGNMENT-DEFECT / BRANCH-AMPLITUDE.
```

Therefore:

```text
RELATIVE-MISMATCH -> 0
```

is the right theorem target for shell-side alignment.  It removes the raw
size of the residual and measures only branch failure.

## 3. Measured values

Using the certified data from:

```text
E77_7aq_even_odd_shell_results.json
E77_7aq_even_odd_shell_plant_16_18.json
E77_7h_geometric_shell_residual_results.json
E77_7at_small_mode_alignment_results.json
```

the normalized defect is:

### Zeta

```text
16 -> 18:
  RELATIVE-MISMATCH = 6.4559210e-5

18 -> 20:
  RELATIVE-MISMATCH = 3.1402185e-4
```

### Planted falsifier

```text
16 -> 18:
  RELATIVE-MISMATCH = 1.8666915
```

So the zeta shell path lives in a genuine small-defect regime, while the
planted build is order-one away from the large branch.

## 4. Consequence

This gives the cleanest shell-facing reduction so far:

```text
RELATIVE-MISMATCH-LAW:
  prove that the weighted inner/outer mismatch is higher order relative to
  the branch amplitude on the zeta shell ladder.
```

Equivalently,

```text
r_out / r_in
  = sgn(b) sqrt(c/a) + higher-order defect,           (AV-2)
```

with the higher-order defect measured by `(AV-1)`.

This is strictly smaller than the absolute mismatch theorem, because the
overall shell amplitude scale is now quotiented out.

## 5. Reduction

The shell front becomes:

```text
RELATIVE-MISMATCH-LAW
=> WEIGHTED-INNER-OUTER-MISMATCH
=> ALIGNMENT-DEFECT
=> SMALL-MODE-ALIGNMENT-LAW
=> SMALL-MODE-SUPPRESSION
=> ... => BTG-DIV-L.
```

## 6. Status

```text
proved numerically:
  the normalized shell-side mismatch is tiny on the live zeta steps and
  order one on the planted falsifier.

reduced:
  WEIGHTED-INNER-OUTER-MISMATCH
  -> RELATIVE-MISMATCH-LAW.

live object:
  theorem-grade proof that the relative mismatch tends to zero, or is
  summably small, on the zeta shell ladder.
```
