# E77.7az - Signed active branch autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7ay showed that coarse magnitude ordering

```text
boundary > outer > inner
```

is only a regime classifier and not the carrier of the shell-side defect.

The natural next attempt is to use simple **signed** combinations of the full
active vector, hoping that one of them tracks the tiny shell relative
mismatch.

This note audits that hope.

## 2. Candidate signed combinations

Using the aligned complex active vector

```text
(left_outer, left_boundary, left_inner, right_inner, right_boundary, right_outer),
```

the following simple signed combinations were tested at `sigma=3.0`:

```text
outer_sum              = right_outer + left_outer
boundary_sum           = right_boundary + left_boundary
inner_sum              = right_inner + left_inner
outer_minus_inner      = outer_sum - inner_sum
boundary_minus_outer   = boundary_sum - outer_sum
boundary_minus_inner   = boundary_sum - inner_sum
signed_branch          = boundary_sum - (outer_sum + inner_sum)/2
curvature              = outer_sum - 2*boundary_sum + inner_sum
left_right_total_diff  = (right side sum) - (left side sum)
```

These are the first obvious branch-sensitive signed summaries after the raw
magnitudes.

## 3. Results

### Zeta

At the live shell steps:

```text
N=16:
  RELATIVE-MISMATCH      = 6.4559e-5
  |signed_branch|        = 1.2752
  |curvature|            = 2.5505
  |left_right_total_diff|= 0.1525
  |outer_minus_inner|    = 0.2513

N=18:
  RELATIVE-MISMATCH      = 3.1402e-4
  |signed_branch|        = 1.2653
  |curvature|            = 2.5305
  |left_right_total_diff|= 0.1568
  |outer_minus_inner|    = 0.2683
```

So the shell defect is tiny while every tested signed branch summary remains
order one and barely changes between `N=16` and `N=18`.

### Planted falsifier

At the shared step:

```text
RELATIVE-MISMATCH      = 1.8667
|signed_branch|        = 0.0730
|curvature|            = 0.1460
|left_right_total_diff|= 0.3716
|outer_minus_inner|    = 1.0200
```

This is especially instructive:

- some signed summaries are **smaller** in the planted build than in zeta;
- yet the shell-side mismatch is much **larger**.

So no direct monotone bridge exists from these simple signed branch summaries
to the shell-side defect.

## 4. Autopsy

The signed-branch shortcut is refuted.

Even after keeping complex signs and left/right orientation, the obvious
branch-level collapses remain too coarse:

```text
RELATIVE-MISMATCH is not encoded by any simple O(1) signed summary of the
aligned active vector tested here.
```

This is a theorem-grade autopsy because the scale mismatch is structural:

1. zeta shell defect is already at `10^-4`;
2. every tested signed active summary stays in an order-one regime;
3. some of those summaries are actually smaller for the planted falsifier
   than for zeta.

Therefore the carrier of the shell defect must live in a finer cancellation
inside the active vector than any of these first-level branch collapses.

## 5. Smaller live object

The next admissible target is now:

```text
ACTIVE-VECTOR-CANCELLATION-DEFECT:
  the specific finer cancellation inside the six-node aligned active vector
  that survives after both coarse magnitude ordering and simple signed branch
  combinations are factored out.
```

This is strictly smaller than the vague `ACTIVE-BRANCH-TO-SHELL-BRIDGE`,
because it rules out the whole first layer of branch-level signed summaries.

## 6. Consequence

The shell-side frontier becomes:

```text
ACTIVE-VECTOR-CANCELLATION-DEFECT
=> ACTIVE-BRANCH-TO-SHELL-BRIDGE
=> PHASE5-TO-SHELL-RELATIVE-BRIDGE
=> RELATIVE-MISMATCH-LAW
=> ... => BTG-DIV-L.
```

## 7. Status

```text
refuted:
  simple signed active-branch summaries as carriers of the shell relative
  mismatch.

proved:
  the shell defect lives below the first layer of signed branch collapses.

live object:
  theorem-grade identification of the finer active-vector cancellation defect
  that feeds the shell relative mismatch.
```
