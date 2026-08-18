# E77.7ay - Active branch order autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7ax showed that the full active Schur contribution vector contains a
branch geometry that separates the zeta shell-good regime from the planted
shell-bad one:

```text
zeta:    boundary > outer > inner,
plant:   inner dominant.
```

The natural question is whether that branch ordering already *is* the missing
bridge to the shell-side relative mismatch.

This note answers: not yet.

## 2. Data

Using the same active-vector and shell-side artifacts as E77.7ax, the live
zeta rows at `sigma=3.0` give:

### Zeta `N=16`

```text
RELATIVE-MISMATCH               = 6.4559e-5
outer_minus_inner_over_sum      = 0.2627
boundary_minus_outer_over_sum   = 0.1398
boundary_minus_inner_over_sum   = 0.3883
outer/inner                     = 1.7127
boundary/inner                  = 2.2695
geom_mean_gap                   = 0.5009
```

### Zeta `N=18`

```text
RELATIVE-MISMATCH               = 3.1402e-4
outer_minus_inner_over_sum      = 0.2820
boundary_minus_outer_over_sum   = 0.1298
boundary_minus_inner_over_sum   = 0.3973
outer/inner                     = 1.7856
boundary/inner                  = 2.3182
geom_mean_gap                   = 0.5012
```

So the branch-order scalars remain stable at order one while the shell-side
defect moves in the `10^-4` regime.

### Planted `N=16`

```text
RELATIVE-MISMATCH               = 1.8667
outer_minus_inner_over_sum      = -0.7140
boundary_minus_outer_over_sum   = 0.5169
boundary_minus_inner_over_sum   = -0.3125
outer/inner                     = 0.1668
boundary/inner                  = 0.5238
geom_mean_gap                   = 0.2437
```

These order-one branch indicators do separate the planted regime from zeta,
but they do not model the tiny zeta shell defect itself.

## 3. Autopsy

The coarse branch-order bridge is refuted:

```text
RELATIVE-MISMATCH is not controlled by branch ordering alone.
```

The reason is structural:

1. branch-order invariants remain order one on the live zeta rows;
2. the shell-side defect is already of size `10^-4`;
3. therefore the shell defect must depend on a finer signed feature of the
   active vector than the mere ordering of outer/boundary/inner magnitudes.

So `boundary > outer > inner` is a real regime classifier, but not yet the
missing shell theorem.

## 4. Smaller live object

This sharpens E77.7ax.

The next admissible target is not:

```text
ACTIVE-BRANCH-TO-SHELL-BRIDGE via magnitude ordering alone,
```

but the finer object

```text
SIGNED-ACTIVE-BRANCH-DEFECT:
  the specific signed/complex combination inside the active contribution
  vector that survives after the coarse branch geometry is factored out.
```

In other words: branch ordering is the container, not the carrier.

## 5. Consequence

The shell-side frontier becomes:

```text
SIGNED-ACTIVE-BRANCH-DEFECT
=> ACTIVE-BRANCH-TO-SHELL-BRIDGE
=> PHASE5-TO-SHELL-RELATIVE-BRIDGE
=> RELATIVE-MISMATCH-LAW
=> ... => BTG-DIV-L.
```

This is a strict reduction because it rules out another family of too-coarse
active-vector summaries without discarding the useful branch localization.

## 6. Status

```text
refuted:
  branch-order magnitudes alone as the shell-side bridge.

proved:
  the active-vector branch geometry is a regime separator but not the
  shell-defect carrier.

live object:
  theorem-grade identification of the signed active-branch defect that
  remains after the coarse magnitude ordering is factored out.
```
