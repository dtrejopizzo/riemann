# E77.7aw - Phase-5 ratio bridge autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7av reduced the live shell-side object to the scale-free quantity

```text
RELATIVE-MISMATCH
  = (r_in sqrt(c) - sgn(b) r_out sqrt(a))
    / (r_in sqrt(a) + sgn(b) r_out sqrt(c)).
```

The natural next hope was that this shell-side ratio might already coincide
with one of the active-block ratios isolated in Phase 5, especially the
weighted parity packages from E77.5t/5u/5v.

This note audits that shortcut directly.

## 2. Compared objects

The shell-side target comes from:

```text
E77_7aq_even_odd_shell_results.json
E77_7aq_even_odd_shell_plant_16_18.json
E77_7h_geometric_shell_residual_results.json
```

The Phase-5 comparison package comes from:

```text
E77_5t_weighted_parity_cell_zeta.json
E77_5t_weighted_parity_cell_plant_n18.json
```

At `sigma=3.0`, we compare `RELATIVE-MISMATCH` against the already named
normalized ratios

```text
lr_odd_abs / inserted_abs,
lr_even_abs / inserted_abs,
outer_pair_abs / inserted_abs,
old_boundary_pair_abs / inserted_abs,
old_shell_pair_abs / inserted_abs,
total_abs / inserted_abs.
```

## 3. Results

### Zeta

For the two live shell steps:

```text
N=16:
  RELATIVE-MISMATCH = 6.4559e-5

  lr_odd/ins        = 0.7802
  lr_even/ins       = 0.7981
  outer/ins         = 3.0838
  old_boundary/ins  = 4.0838
  old_shell/ins     = 1.7981
  total/ins         = 0.7981

N=18:
  RELATIVE-MISMATCH = 3.1402e-4

  lr_odd/ins        = 0.8646
  lr_even/ins       = 0.8792
  outer/ins         = 3.3587
  old_boundary/ins  = 4.3587
  old_shell/ins     = 1.8792
  total/ins         = 0.8792
```

So the shell mismatch lives in a `10^-4` regime while every candidate
Phase-5 ratio stays rigidly order one.

### Planted falsifier

At the shared shell step:

```text
N=16:
  RELATIVE-MISMATCH = -1.8667

  lr_odd/ins        = 0.4394
  lr_even/ins       = 2.4478
  outer/ins         = 0.2416
  old_boundary/ins  = 0.7584
  old_shell/ins     = 1.4478
  total/ins         = 2.4478
```

Again there is no simple equality or stable proportionality law.

## 4. Autopsy

The hoped-for direct bridge is refuted:

```text
RELATIVE-MISMATCH is not any one of the already recorded
Phase-5 weighted-parity ratios.
```

This is a theorem-grade autopsy in the same sense as E77.7ap:

1. the shell-side quantity is tiny in zeta;
2. every candidate active-block ratio remains order one on the same rows;
3. no scalar normalization from the recorded E77.5t package explains the
   shell defect.

So the shell-side target does **not** collapse to an existing scalar from
Phase 5.

## 5. Smaller live object

This does not send us back to a larger object.  It sharpens the bridge.

What remains admissible is:

```text
PHASE5-TO-SHELL-RELATIVE-BRIDGE:
  derive RELATIVE-MISMATCH from the underlying active Schur contributions
  themselves, not from any single pre-collapsed scalar ratio.
```

Equivalently, the missing object is not one of the named ratios

```text
outer/inserted, old_shell/inserted, lr_odd/inserted, ...
```

but a finer signed combination of the active Schur contributions before those
ratios are collapsed.

## 6. Consequence

The candid shell-side frontier is now:

```text
PHASE5-TO-SHELL-RELATIVE-BRIDGE
=> RELATIVE-MISMATCH-LAW
=> WEIGHTED-INNER-OUTER-MISMATCH
=> ... => BTG-DIV-L.
```

This is still a strict reduction, because it rules out a whole family of too
coarse scalar candidates and forces the next step to stay at the exact Schur
contribution level.

## 7. Status

```text
refuted:
  direct identification of RELATIVE-MISMATCH with any recorded E77.5t
  weighted-parity ratio.

proved:
  the shell-side defect is far smaller than those order-one Phase-5 ratios on
  the live zeta rows;
  the bridge must therefore use finer signed contribution data.

live object:
  theorem-grade derivation of RELATIVE-MISMATCH from the exact active Schur
  contribution vector, not from a pre-collapsed scalar package.
```
