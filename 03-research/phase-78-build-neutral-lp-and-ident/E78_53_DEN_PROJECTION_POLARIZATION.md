# E78.53 - The inward projection is exactly radial drop minus increment cost

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.52 reduced the modulus side to the Euclidean increment lock

```text
-2<Delta d_N,d_N> > |Delta d_N|^2,                       (DPP-1)
```

with

```text
d_N := 1-theta_N,
Delta d_N := d_N+2 - d_N.                                 (DPP-2)
```

The natural next question is what exact scalar geometry is carried by the signed
projection `<Delta d_N,d_N>`.

## 2. Exact polarization identity

From

```text
d_N+2 = d_N + Delta d_N,                                  (DPP-3)
```

we have

```text
|d_N+2|^2
 = |d_N|^2 + 2<Delta d_N,d_N> + |Delta d_N|^2.           (DPP-4)
```

Rearranging gives the exact identity

```text
<Delta d_N,d_N>
 = (|d_N+2|^2 - |d_N|^2)/2 - |Delta d_N|^2/2.            (DPP-5)
```

Equivalently,

```text
-<Delta d_N,d_N>
 = (|d_N|^2 - |d_N+2|^2)/2 + |Delta d_N|^2/2.            (DPP-6)
```

So the inward projection splits canonically into

```text
half radial drop      +  half increment cost.            (DPP-7)
```

This is exact.

## 3. Immediate consequence for the lock

Substituting `(DPP-5)` into E78.52 gives

```text
-2<Delta d_N,d_N> - |Delta d_N|^2
 = |d_N|^2 - |d_N+2|^2.                                  (DPP-8)
```

Therefore

```text
DEN-EUCLIDEAN-INCREMENT-LOCK
<=> |d_N|^2 - |d_N+2|^2 > 0.                             (DPP-9)
```

So the Euclidean lock is exactly the same burden as the squared radial drop
from E78.48, just written through the projection variable.

This is an important autopsy: after E78.52, splitting the projection does **not**
create a smaller theorem-grade target by itself.

## 4. Probe audit

Companion data already checked on this pass using the certified Phase-77
`one_minus_theta` rows.

### Exactness

For both builds:

```text
max reconstruction error < 1e-12.                         (DPP-10)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  <Delta d_N,d_N> = -0.02859934747
  (|d_N+2|^2-|d_N|^2)/2 = -0.02136687292
  |Delta d_N|^2/2       =  0.00723247455

sigma=3.0, N=12->14:
  <Delta d_N,d_N> = -0.00460526019
  radial half-drop      =  0.00372569871
  increment half-cost   =  0.00087956149.                (DPP-11)
```

Across the audited zeta ladder:

```text
median inward projection   = 0.0010776764705804802
median half radial drop    = 0.0009037898249466047
median half increment cost = 0.00017388664563387568.     (DPP-12)
```

So on the audited zeta ladder the inward projection is mainly explained by the
radial drop, with the increment-size term a smaller positive add-on.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  <Delta d_N,d_N> = 288.09395133
  (|d_N+2|^2-|d_N|^2)/2 = 1335.65260743
  |Delta d_N|^2/2       = 1047.55865610

sigma=3.0, N=12->14:
  <Delta d_N,d_N> = -1313.81356207
  radial half-drop      = 905.11860156
  increment half-cost   = 408.69496051.                 (DPP-13)
```

The plant again shows that the same identity can sit on either side of the sign
barrier depending on whether the radial drop itself survives.

## 5. Honest reading

This note is half structural reduction and half autopsy.

Reduction:
it reveals the exact scalar content of the inward projection.

Autopsy:
because `(DPP-8)` collapses right back to the squared radial drop, this split
does not produce a theorem-grade target smaller than the E78.47/E78.48 modulus
law.

So the real value of the note is diagnostic:

```text
if the front is to close through the Euclidean route, the real new burden is not
the polarization identity itself, but a direct shell law forcing the radial
drop term to stay positive.                               (DPP-14)
```

## 6. Status

```text
proved:
  <Delta d_N,d_N> is exactly half the signed radial square change minus half
  the increment square;

proved:
  the Euclidean increment lock is exactly equivalent to the squared radial drop
  positivity from E78.48;

observed:
  on audited zeta rows the inward projection is largely explained by the radial
  drop, with the increment cost secondary;

autopsied:
  the projection split itself does not create a smaller theorem-grade target;

next:
  search for a genuine shell law forcing the radial drop/cofinal contraction,
  or for a new exact recurrence on d_N that is not equivalent to the same
  modulus lock.
```
