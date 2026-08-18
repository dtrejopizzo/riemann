# E79.80 - The current geometric point is not selected by a max-margin principle

**Scope:** `GAP-Z` only, robustness audit inside the E79.79 admissible cone.  
**Class:** AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the point
`(0.36, 0.14)` is not singled out by a simple maximin margin principle on the
audited frontier inequalities. In the scanned cone, the largest minimum margin
lives at an extreme point, not near the current coefficients.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure inequality audit inside the E79.79 cone.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.79 showed that the audited frontier decisions determine an open cone of
admissible geometric coefficients `(a,b)`, not a unique point.

The next natural hope is:

```text
perhaps the chosen point is the most robust one,
e.g. it maximizes the smallest decision margin across the live tradeoff rows.   (80-1)
```

If true, this would give a canonical way to pick one point inside the cone.

## 2. Margin functional

For each tradeoff row, define the signed decision margin at `(a,b)` by

```text
margin_N(a,b)
  :=  Delta_s(a,b) - Delta_m    on rows where the low-cost point should win,
      Delta_m - Delta_s(a,b)    on rows where the high-cost point should win.   (80-2)
```

Inside the admissible cone, all these margins are positive. The maximin
robustness principle would choose `(a,b)` by maximizing

```text
M(a,b) := min_N margin_N(a,b).                                           (80-3)
```

## 3. Probe

Companion files:

```text
E79_80_margin_extremum_autopsy_probe.py
E79_80_margin_extremum_autopsy_results.json
```

The probe scans the same coarse box

```text
a,b in {0.00, 0.01, ..., 0.80},                                          (80-4)
```

restricted to the admissible cone from E79.79, and compares:

```text
- the best maximin point in the scan,
- the current point (0.36, 0.14).                                       (80-5)
```

## 4. Result

On the audited grid, the maximin optimum is not near the current point:

```text
best scanned point   = (0.00, 0.14),
best minimum margin  = 0.378604...,                                     (80-6)
```

whereas the current point has

```text
(a,b) = (0.36, 0.14),
minimum margin = 0.018604....                                           (80-7)
```

So the current coefficients are admissible, but they are far from maximizing a
simple uniform decision buffer.

## 5. Reading

This kills another cheap normalization story.

The current point is **not** selected by:

```text
"pick the most robust point in the admissible cone."                     (80-8)
```

At least on the audited coarse grid, that principle pushes all the way toward
an extreme cone point instead.

So by this stage we know three things:

```text
1. the winner data do not force a unique point (E79.79);
2. the current point is not a one-variable collapse of both sides (E79.78);
3. the current point is not the maximin-robust point of the audited cone. (80-9)
```

## 6. Consequence

The remaining normalization burden is now quite specific.

What can still select `(0.36,0.14)` must be something subtler than:

```text
- decision preservation alone,
- one-scalar reduction,
- crude robustness maximization.                                        (80-10)
```

So the next candid candidates are of a different kind:

```text
- an exact packet identity on the degenerate rows,
- a symmetry/duality condition,
- or a normalization inherited from an earlier finite object in the chain. (80-11)
```

## 7. Status

```text
proved by probe:
  the current coefficients are not selected by a simple maximin margin
  principle on the audited admissible cone;

killed:
  the robustness-extremum normalization story;

clarified:
  if the point (0.36,0.14) is canonical, that canonicity must come from a
  sharper exact structure than mere winner preservation or cone robustness;

open:
  identify that sharper exact structure;

next:
  inspect whether the degenerate rows N=8 and N=14 impose an exact tie or
  symmetry condition that singles out the current coefficients.
```
