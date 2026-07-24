# E78.82 - Sigma monotonicity reduces the weighted shell bound to the left endpoint

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.81 identified the next honest sharpening of the radial front:

```text
SIGMA-MONOTONE-WEIGHTED-SAFEDELTA:
  Y_N(sigma) := N * (-SAFEDELTA_N(i sigma)) / A_N
  decreases in sigma on the safe compact.              (LER-1)
```

This note records the exact payoff of proving `(LER-1)`: it collapses the whole
safe compact to its left endpoint.

## 2. Exact transfer

Assume `(LER-1)` on a compact interval

```text
sigma in [sigma_L, sigma_R]                            (LER-2)
```

with `sigma_L > 0`.

Then for every `sigma` in that compact,

```text
Y_N(sigma) <= Y_N(sigma_L).                            (LER-3)
```

Equivalently,

```text
N * (-SAFEDELTA_N(i sigma)) / A_N
 <= N * (-SAFEDELTA_N(i sigma_L)) / A_N.               (LER-4)
```

So the two-variable weighted target from E78.80 reduces to the single-slice
target

```text
LEFT-ENDPOINT-WEIGHTED-SAFEDELTA:
  N * (-SAFEDELTA_N(i sigma_L)) / A_N <= M_*.          (LER-5)
```

Combined with E78.79-E78.78, this yields

```text
SIGMA-MONOTONE-WEIGHTED-SAFEDELTA
 + LEFT-ENDPOINT-WEIGHTED-SAFEDELTA
=> CONSTANT-WEIGHTED-SAFEDELTA
=> WEIGHTED-NORMALIZED-SAFEDELTA
=> NORMALIZED-SAFEDELTA-AVERAGE
=> SAFEU-TAIL-COUPLING.                                (LER-6)
```

This is a genuine reduction because it replaces a compact-in-sigma problem with
a single endpoint slice.

## 3. Current audited benchmark

Companion:

```text
E78_82_left_endpoint_reduction_probe.py
E78_82_left_endpoint_reduction_results.json
```

Using the currently available common audit from E78.81, the left endpoint slice
is

```text
sigma_L = 1.0.                                         (LER-7)
```

On that slice:

```text
Y_N(1.0)
  min    = 9.575e-2,
  median = 1.615e-1,
  max    = 3.203e-1,                                   (LER-8)
```

with the current worst case attained at

```text
N = 8,   Y_8(1.0) = 0.32033520392027215.               (LER-9)
```

So if sigma monotonicity is proved on the safe compact, the entire current
weighted-safe-delta front collapses to the single benchmark inequality

```text
Y_N(1.0) <= 0.321                                      (LER-10)
```

on the audited ladder.

## 4. Consequence

This clarifies the exact next theorem-grade burden. We no longer need to think
of the weighted target as "a function of sigma" first. The logical order is:

```text
1. prove sigma monotonicity,
2. prove the endpoint slice bound.                     (LER-11)
```

Only the second step still carries a genuine numeric burden.

So the radial front is now reduced to:

```text
LEFT-ENDPOINT-WEIGHTED-SAFEDELTA
plus
SIGMA-MONOTONE-WEIGHTED-SAFEDELTA.                     (LER-12)
```

## 5. Honest reading

This note does **not** prove sigma monotonicity, and it does **not** prove the
endpoint bound cofinally.

What it proves is that these are exactly the two remaining ingredients on this
branch, with no further hidden sigma bookkeeping.

That is useful because it prevents the front from drifting back into vague
compact-control language.

## 6. Status

```text
proved:
  sigma monotonicity would reduce the weighted-safe-delta front to the left
  endpoint slice exactly;

observed:
  on the current audited slice sigma=1.0, the worst benchmark is
  Y_8(1.0)=0.32033520392027215 and the whole slice is contained in Y<=0.321;

reduced:
  the radial weighted front to
  SIGMA-MONOTONE-WEIGHTED-SAFEDELTA + LEFT-ENDPOINT-WEIGHTED-SAFEDELTA.
```
