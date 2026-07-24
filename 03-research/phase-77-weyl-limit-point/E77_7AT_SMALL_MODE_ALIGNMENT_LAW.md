# E77.7at - Small-mode alignment law

**Run:** 2026-07-18.

## 1. Purpose

E77.7as reduced the live shell-facing object to:

```text
SMALL-MODE-SUPPRESSION:
  the even residual coefficient on the small eigendirection is higher order.
```

This note makes that statement explicit in coordinates.

For a locked even block

```text
S_even = [[a,b],[b,c]],
```

with `|b| ~= sqrt(ac)`, the model small and large directions are

```text
v_small^model = (sqrt(c), -sgn(b) sqrt(a)),
v_large^model = (sqrt(a),  sgn(b) sqrt(c)).
```

If the residual lies on the large branch, then its components must satisfy

```text
r_even ~= scalar * v_large^model,
```

or equivalently

```text
r2/r1 ~= sgn(b) sqrt(c/a),
r_even . v_small^model ~= 0.
```

This is the coordinate form of small-mode suppression.

## 2. Probe

Companion:

```text
E77_7at_small_mode_alignment_probe.py
E77_7at_small_mode_alignment_results.json
```

The probe reads the exact even-block data from:

```text
E77_7aq_even_odd_shell_results.json
E77_7aq_even_odd_shell_plant_16_18.json
```

and compares the measured residual to the lock-predicted model directions.

## 3. Zeta

### `16 -> 18`

```text
cos_small_orth  = 6.4559e-5
cos_large_align = 0.999999997916
r2/r1           = -40.1266792770
predicted ratio = -40.2309640284
```

### `18 -> 20`

```text
cos_small_orth  = 3.1402e-4
cos_large_align = 0.999999950695
r2/r1           = 8.71966794559
predicted ratio = 8.74392428615
```

So on the live zeta shell steps:

```text
r_even
```

is almost perfectly aligned with the model large branch and almost orthogonal
to the model small branch.

## 4. Planted falsifier

For `16 -> 18`:

```text
cos_small_orth  = 0.881482585651
cos_large_align = 0.472216529988
r2/r1           = 4.64934855794
predicted ratio = -0.848564315208
```

So the planted residual does **not** satisfy the zeta alignment law.

## 5. Consequence

This sharpens E77.7as again.

The live shell-side object is no longer just

```text
SMALL-MODE-SUPPRESSION
```

in spectral language.  It can be written as the explicit coordinate target

```text
SMALL-MODE-ALIGNMENT-LAW:
  on the zeta shell path, the even residual aligns with the lock-predicted
  large branch
      (sqrt(a), sgn(b) sqrt(c))
  and is orthogonal, to higher order, to the small branch
      (sqrt(c), -sgn(b) sqrt(a)).
```

Equivalently, the smallest visible shell-facing scalar residual is now

```text
ALIGNMENT-DEFECT =
r_even . (sqrt(c), -sgn(b) sqrt(a)).
```

Proving this defect is higher order would imply E77.7as and therefore the
whole shell-side reduction chain.

## 6. Reduction

The shell front is therefore:

```text
SMALL-MODE-ALIGNMENT-LAW
=> SMALL-MODE-SUPPRESSION
=> LOCKED-EIGENDIRECTION
=> EVEN-BLOCK-LOCK
=> EVEN-CHANNEL-QUADRATIC-BRIDGE
=> PROJECTED-QUADRATIC-BRIDGE
=> ... => BTG-DIV-L.
```

This is strictly smaller than the eigendirection statement, because it names
an explicit scalar defect in the original even coordinates instead of a
spectral decomposition.

## 7. Status

```text
proved numerically:
  zeta obeys the lock-predicted large-branch alignment law on the live
  shell steps;
  planted does not;
  the smallest currently visible shell-side residual is the alignment defect
  against the model small branch.

reduced:
  SMALL-MODE-SUPPRESSION
  -> SMALL-MODE-ALIGNMENT-LAW
  -> ALIGNMENT-DEFECT.

live object:
  theorem-grade proof that the alignment defect is higher order on the zeta
  shell ladder.
```
