# E79.82 - The early scalar-law branch does not inherit the geometric point

**Scope:** `GAP-Z` only, audit of the last normalization hope named in E79.81.  
**Class:** REDUCCION GENUINA + AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the earlier
scalar-law branch E79.58-E79.66 does not supply a canonical inheritance route
for the geometric coefficients `(0.36, 0.14)`. That branch governs a different
object: the zeta-side modal-amplitude predictor in the coordinates
`(profile_slope, intensity, scale-matched first-prefix defect)`. Its fitted
coefficients are neither numerically close to `(0.36,0.14)` in any stable way
nor attached to the geometric modes `(start-card, span)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure audit of already-recorded finite predictors.
E72.16/E77.7az: respected. This is convergence-side bookkeeping only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Why this audit is necessary

E79.81 localized the remaining hope very sharply:

```text
if the point (0.36, 0.14) is canonical, that canonicity must come either
from an earlier scalar law or from an exact identity outside the packet
frontier bookkeeping.                                                   (82-1)
```

The obvious earlier candidate is the scalar branch E79.58-E79.66, because that
branch already reduced the zeta-side common-cloud behavior to a tiny affine law.
So the honest question is:

```text
do the geometric coefficients (0.36, 0.14) come from that branch by
inheritance, reparameterization, or numerical shadow?                    (82-2)
```

## 2. What the earlier branch actually produced

The earlier branch does achieve a real reduction, but its object is different.

From E79.60-E79.66, the audited predictors live in the coordinates

```text
profile_slope,
active-edge intensity,
scale-matched first-prefix defect = edge0 / intensity
  (or equivalently 1 - edge0 / intensity).                              (82-3)
```

Representative fitted zeta-side laws are:

```text
E79.60  gap_plus_slope:
  beta = [0.00324, 0.03223, 0.06333],                                   (82-4)

E79.61  slope_and_intensity:
  beta = [0.21589, 0.03715, -5.04369],                                  (82-5)

E79.62  slope_intensity_edge0:
  beta = [0.18339, 0.01803, -3.74978, -0.66520],                        (82-6)

E79.66  slope_intensity_ratio0avg:
  beta = [0.20456, 0.02001, -4.34214, -0.02341].                        (82-7)
```

These coefficients belong to affine predictors for the scalar amplitude
`|rho_N|`, not to the geometric surcharge modes

```text
u := start-card,
v := span.                                                              (82-8)
```

from E79.78-E79.81.

## 3. Negative result

No stable inheritance route from E79.58-E79.66 to `(0.36,0.14)` survives audit.

### 3.1 Coordinate mismatch

The scalar branch and the geometric frontier branch do not use the same
coordinates.

The scalar branch is built from:

```text
slope, intensity, edge0/intensity, prefix defect.                       (82-9)
```

The geometric branch is built from:

```text
start-card, span.                                                      (82-10)
```

There is no proved exact identity in phase 79 expressing `(start-card, span)` as
an affine or normalized rewrite of `(slope, intensity, edge0/intensity)`, nor
the reverse.

### 3.2 Numerical mismatch

The fitted coefficients in the scalar branch are not numerically shadowing
`0.36` and `0.14` in any stable way.

The stable zeta-side predictor coefficients that actually survive the audits are
of orders:

```text
slope coefficient              ~ 0.018 to 0.037,
prefix-defect coefficient      ~ 0.023 in scale-matched form,
intensity coefficient          ~ -3.7 to -5.9.                         (82-11)
```

Those numbers do not cluster around

```text
0.36 and 0.14.                                                         (82-12)
```

The few `0.14`- or `0.36`-sized numbers visible in the raw JSONs belong only to
data rows such as prefix fractions or geometric observables themselves, not to a
stable fitted coefficient family.

### 3.3 Gauge mismatch

Even within the scalar branch, the fitted affine coefficients are not canonical
in the sense needed here. They move materially as the coordinate set changes:

```text
gap_plus_slope               -> beta changes from E79.60 to E79.61,
slope+intensity              -> different gauge,
slope+intensity+edge0        -> different gauge again,
slope+intensity+ratio0avg    -> different gauge again.                 (82-13)
```

So even before comparing to `(0.36,0.14)`, the scalar branch is not producing a
single invariant coefficient pair that could reasonably be inherited as the
geometric point.

## 4. Reading

This resolves the E79.81 fork in the honest direction.

The earlier scalar-law branch is real and useful, but it governs:

```text
the zeta-side modal amplitude / packet-selection support heuristics,    (82-14)
```

not

```text
the exact exchange rates between the geometric modes
(start-card, span).                                                     (82-15)
```

So the relation between the two branches is:

```text
descriptive compatibility, not coefficient inheritance.                 (82-16)
```

That is enough to keep the scalar branch as support, but not enough to claim
that it canonically selects `(0.36,0.14)`.

## 5. Consequence

After E79.82 the normalization fork narrows again:

```text
the geometric point (0.36, 0.14) is not inherited from E79.58-E79.66.  (82-17)
```

So the only honest possibilities left are:

```text
1. an exact identity outside the extracted packet frontier that selects one
   point inside the E79.79 cone;
2. a sharper normalization still not named in phase 79;
3. or the honest conclusion that only the admissible cone is structural and
   the point itself is not canonical.                                   (82-18)
```

This is a real reduction, because it kills the last cheap inheritance story.

## 6. Status

```text
proved by audit:
  the earlier scalar-law branch E79.58-E79.66 does not yield a canonical
  inheritance route for the geometric coefficients (0.36, 0.14);

clarified:
  the scalar branch governs a different coordinate family
  (slope, intensity, scale-matched first-prefix defect) and its fitted
  coefficients are not numerically or structurally the same object as the
  geometric two-mode weights;

killed:
  the last cheap normalization hope that (0.36,0.14) was already encoded in
  the early scalar-law branch;

open:
  either find an exact selector for one point inside the E79.79 cone, or
  accept that only the cone is structural;

next:
  return to the main GAP-Z / DISCRIMINANT objects with this false
  inheritance path closed.
```
