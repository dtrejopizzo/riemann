# E78.55 - On the inward branch, the cone lock is exactly a size-vs-sine law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.54 reduced the modulus side to the cone condition

```text
r_N + 2 c_N < 0,                                          (DCF-1)
```

where

```text
r_N := |Delta d_N|/|d_N|,
c_N := cos(angle(Delta d_N,d_N)).                         (DCF-2)
```

E78.43 already isolated the sine partner

```text
s_N := DIRINC_N = sin(angle(Delta d_N,d_N)).              (DCF-3)
```

This note shows that on the inward branch `c_N < 0`, the cone lock is exactly a
single size-vs-sine inequality.

## 2. Exact inward-branch formula

Whenever `c_N < 0`, the angle lies on the inward half-circle, so

```text
c_N = -sqrt(1-s_N^2).                                     (DCF-4)
```

Substituting into E78.54 gives the exact equivalent condition

```text
r_N - 2 sqrt(1-s_N^2) < 0,                                (DCF-5)
```

or

```text
SIZE-VS-SINE:
  r_N < 2 sqrt(1-s_N^2).                                  (DCF-6)
```

So, on the inward branch, the denominator modulus lock is fully determined by:

```text
size ratio r_N   +   directional sine defect s_N.        (DCF-7)
```

This is the exact merger of the size front and the direction front.

## 3. Probe audit

Companion data already certified:

```text
E78_54_den_cone_lock_results.json
E78_43_den_directional_increment_results.json
```

Using those rows, the inward-branch reconstruction of `(DCF-5)` holds to
roundoff.

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  r_N = 0.5057780531
  s_N = 0.0019258346
  2 sqrt(1-s_N^2) = 1.9999962912

sigma=3.0, N=12->14:
  r_N = 0.3819535107
  s_N = -0.0120479266
  2 sqrt(1-s_N^2) = 1.9998548422.                        (DCF-8)
```

Across the audited zeta ladder:

```text
min( 2 sqrt(1-s_N^2) - r_N ) = 1.4942182380474347
median                         = 1.6927487779492905
max                            = 1.7381857958014302.     (DCF-9)
```

So the audited zeta branch lies extremely far inside the admissible cone: the
directional defect is tiny, and the size ratio is nowhere near saturating the
bound.

### Planted build

The planted build fails exactly where the inward-branch hypothesis already
breaks:

```text
sigma=1.0, N=10->12:
  c_N = 0.9420192582 > 0,
  r_N = 6.8506848104.                                     (DCF-10)
```

On later planted rows that do re-enter the inward branch, the same exact formula
holds but does not by itself separate them from zeta.

## 4. Consequence

This yields the cleanest unified denominator endpoint so far:

```text
DEN-SIZE-SINE-LOCK:
  prove cofinally that the increment stays on the inward branch
  and that r_N < 2 sqrt(1-s_N^2).                         (DCF-11)
```

Then E78.54 and the whole modulus chain follow immediately.

## 5. Candid reading

This is a genuine structural reduction, but not yet a theorem-grade closure.

Reduction:
it fuses the previously separate denominator fronts into a single exact
criterion involving only the already-named size ratio and directional defect.

Limitation:
on the audited zeta ladder the inequality is so loose that the real burden is
not numerical sharpness here; it is proving the inward-branch/cofinal shell law
at all.

So this note says, plainly:

```text
the denominator front is no longer two fronts.            (DCF-12)
```

## 6. Status

```text
proved:
  on the inward branch c_N<0, the cone lock is exactly equivalent to
  r_N < 2 sqrt(1-s_N^2);

proved:
  this merges the size-ratio front and the directional-defect front into one
  exact denominator criterion;

observed:
  audited zeta rows satisfy the merged criterion with very large margin;

observed:
  the planted build fails first by leaving the inward branch;

reduced:
  DEN-CONE-LOCK to DEN-SIZE-SINE-LOCK on the inward branch;

next:
  isolate a finite shell law forcing the inward branch itself, or identify the
  exact recurrence that keeps c_N negative and close to -1 on zeta.
```
