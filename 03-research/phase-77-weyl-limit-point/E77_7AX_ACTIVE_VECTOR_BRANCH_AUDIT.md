# E77.7ax - Active-vector branch audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7aw refuted the cheap scalar bridge:

```text
RELATIVE-MISMATCH
```

is not any one of the already collapsed E77.5t weighted-parity ratios.

The next admissible place to look is the full active contribution vector from
E77.5w, before those contributions are collapsed to scalar ratios.

## 2. Data

We compare:

- shell-side defect from `E77_7at_small_mode_alignment_results.json`;
- full active complex vector from `E77_5w_complex_active_vector_zeta.json`;
- planted active complex vector from `E77_5w_complex_active_vector_plant_n18.json`.

For the normalized aligned active vector

```text
(left_outer, left_boundary, left_inner, right_inner, right_boundary, right_outer)
```

we inspect the averaged magnitude scales

```text
outer = (|left_outer| + |right_outer|)/2,
boundary = (|left_boundary| + |right_boundary|)/2,
inner = (|left_inner| + |right_inner|)/2.
```

## 3. Results

### Zeta

At `sigma=3.0`:

```text
N=16:
  RELATIVE-MISMATCH = 6.4559e-5
  outer/inner       = 1.7127
  boundary/inner    = 2.2695
  left_right_gap    = 0.2519
  inserted imbalance ratio = 0.6712

N=18:
  RELATIVE-MISMATCH = 3.1402e-4
  outer/inner       = 1.7856
  boundary/inner    = 2.3182
  left_right_gap    = 0.2180
  inserted imbalance ratio = 0.6827
```

So on the live zeta steps the active vector sits in a stable branch:

```text
boundary > outer > inner,
```

with moderately sized phase gaps and small shell-side mismatch.

### Planted falsifier

At the shared step `N=16`:

```text
RELATIVE-MISMATCH = 1.8667
outer/inner       = 0.1668
boundary/inner    = 0.5238
left_right_gap    = 0.0520
inserted imbalance ratio = 0.2682
```

Here the active vector sits in the opposite amplitude regime:

```text
inner >> boundary > outer,
```

while the shell-side mismatch is order one.

## 4. Autopsy / reduction

This is not yet a theorem that computes `RELATIVE-MISMATCH`.  But it is a
real reduction of the live bridge:

- scalar Phase-5 ratios are too coarse;
- the full active vector already contains a branch structure that sharply
  separates the zeta shell regime from the planted one.

So the honest next target is:

```text
ACTIVE-BRANCH-TO-SHELL-BRIDGE:
  derive the shell-side relative mismatch from the branch geometry of the
  full active Schur contribution vector, not from any scalar ratio collapsed
  out of it.
```

The smallest visible branch invariant is now the amplitude ordering

```text
boundary > outer > inner
```

versus

```text
inner dominant.
```

This is strictly finer than E77.5t/5u/5v, because those blocks only see
selected scalar packages and lose the branch ordering information.

## 5. Consequence

The shell-side frontier becomes:

```text
ACTIVE-BRANCH-TO-SHELL-BRIDGE
=> PHASE5-TO-SHELL-RELATIVE-BRIDGE
=> RELATIVE-MISMATCH-LAW
=> ... => BTG-DIV-L.
```

This does not close the bridge, but it rules out another family of too-coarse
targets and fixes the next admissible object at the active-vector level.

## 6. Status

```text
proved numerically:
  the zeta shell-good regime coincides with a stable active-vector branch
  ordering boundary > outer > inner;
  the planted shell-bad regime has the opposite geometry, with inner
  dominance;
  scalar E77.5t ratios were hiding this information.

reduced:
  PHASE5-TO-SHELL-RELATIVE-BRIDGE
  -> ACTIVE-BRANCH-TO-SHELL-BRIDGE.

live object:
  theorem-grade derivation of RELATIVE-MISMATCH from the branch geometry of
  the full active Schur contribution vector.
```
