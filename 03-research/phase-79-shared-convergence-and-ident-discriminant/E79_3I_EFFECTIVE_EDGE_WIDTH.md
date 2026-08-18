# E79.3i - The effective edge width gives a constant gain, not an exponent gain

**Scope:** `GAP-Z` only, refinement of the edge-budget mechanism.  
**Class:** AUTOPSIA UTIL + REDUCCION FRANCA.  
**What we know after this document that we did not know before:** the raw shell
count `m_theta(N)` overstates the active edge width on the zeta side, but only
by a moderate constant factor. So there is real gain inside the edge, yet not
the kind of gain that by itself changes the borderline exponent.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side anatomy only.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3h left the live object in the form

```text
COMMON-GAP-Z
  = [extended-ladder-stable linear edge width]
    x [extended-ladder-stable local N^-2 shell profile]
    + [tiny interior correction].                                        (T-1)
```

The natural objection to that budget is that the raw shell count `m_theta(N)`
may be too crude: perhaps most deep shells contribute very little, so the
*effective* edge width is much smaller.

That is exactly what this probe tests.

## 2. Probe

Companion files:

```text
E79_3I_EFFECTIVE_EDGE_WIDTH_PROBE.py
E79_3I_effective_edge_width_results.json
```

For the first `m_theta(N)` shells in the active edge, with weights given by the
absolute `N^2`-scaled shell amplitudes, define:

```text
raw width       = m_theta,
effective width = (sum weights) / (max weight).                         (T-2)
```

So:

```text
effective/raw < 1
```

measures how much narrower the edge really is once shell amplitudes are taken
into account.

## 3. Result: zeta gets a real but only constant-factor gain

At `sigma = 1`, for the `theta = 0.9` edge, zeta gives:

```text
N    m90/N         effective/raw      effective/N
8    0.8750000000  0.807292046        0.706380540
10   0.8000000000  0.717811720        0.574249376
12   0.7500000000  0.779547134        0.584660351
14   0.7142857143  0.784916001        0.560654287
16   0.6875000000  0.798840088        0.549202560
18   0.7222222222  0.725987262        0.524324134
20   0.6500000000  0.734688618        0.477547602
22   0.7272727273  0.748213381        0.544155186
24   0.6250000000  0.781278483        0.488299052
```

The summary statistics are:

```text
mean(effective/raw) = 0.7643...
range               = 0.7178 ... 0.8073.                               (T-3)
```

For the tighter `theta = 0.99` edge, the discount is stronger:

```text
effective99/raw99 is typically 0.56 ... 0.69,
mean about 0.64.                                                        (T-4)
```

So there is a real gain:

```text
the effective edge is substantially narrower than the raw shell count.   (T-5)
```

But the crucial point is just as important:

```text
effective/N stays order 1 throughout the audited ladder.                 (T-6)
```

So the gain is a constant-factor discount, not a collapse of the linear-width
law.

## 4. Reading

This is the candid autopsy:

```text
the shell amplitudes do taper enough to shrink the active width,
but not enough to turn width ~ N into anything visibly sublinear.         (T-7)
```

Therefore the effective-width refinement does **not** by itself beat the
borderline `N^-1` budget. It improves the constant, not the exponent.

That is still useful: one more plausible location of the missing summability
gain has now been tested and localized.

## 5. Plant remains geometrically incoherent

The planted build does not exhibit the same controlled regime; its ratios are
either erratic or pinned trivially when `m_theta` collapses to a single shell.

So this effective-width refinement reinforces the same structural split as the
previous cloud audits: zeta has a coherent edge economy, plant does not.

## 6. Consequence

The live object sharpens one more time:

```text
COMMON-GAP-Z
  = [constant-factor-reduced but still linear effective edge width]
    x [local N^-2 shell profile]
    + [tiny interior correction].                                        (T-8)
```

This is not a closure, but it is a real reduction. It tells us where the extra
gain is **not** hiding:

```text
not in a dramatic collapse from raw width to effective width.            (T-9)
```

So the candid remaining places to search are now even narrower:

```text
1. deeper decay of shell coefficients as a function of edge depth r,
2. cancellations across neighboring shells beyond absolute-width accounting,
3. a more delicate coupling between edge profile and interior correction. (T-10)
```

## 7. Status

```text
proved by probe:
  on the zeta side, the effective edge width is consistently smaller than the
  raw shell count by a moderate constant factor;

observed:
  that discount is not enough to change the width law from linear to
  sublinear on the audited ladder;

reduced:
  the gain mechanism cannot be attributed merely to replacing raw width by
  effective width;

open:
  find a genuinely stronger source of gain than this constant-factor width
  discount;

next:
  measure shell-decay as a function of normalized depth r/m_theta, to test
  whether the deep part of the active edge has an intrinsic profile that could
  yield a sharper-than-constant discount.
```
