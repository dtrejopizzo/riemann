# E78.54 - The Euclidean increment lock is exactly a cone condition

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.52 reduced the modulus side to

```text
-2<Delta d_N,d_N> > |Delta d_N|^2,                        (DCL-1)
```

with

```text
d_N := 1-theta_N,
Delta d_N := d_N+2 - d_N.                                 (DCL-2)
```

This note rewrites that inequality in the pure geometry of

```text
size ratio  +  increment angle.                           (DCL-3)
```

## 2. Exact cone identity

Whenever `Delta d_N != 0` and `d_N != 0`, define

```text
r_N := |Delta d_N| / |d_N|,                               (DCL-4)
c_N := <Delta d_N,d_N> / (|Delta d_N| |d_N|)
     = cos(angle(Delta d_N,d_N)).                         (DCL-5)
```

Then E78.52 becomes

```text
-2 |Delta d_N| |d_N| c_N > |Delta d_N|^2.                (DCL-6)
```

Dividing by the positive factor `|Delta d_N| |d_N|` gives the exact equivalent
form

```text
CONE-LOCK:
  r_N + 2 c_N < 0,                                        (DCL-7)
```

or, solved for angle,

```text
c_N < -r_N/2.                                             (DCL-8)
```

So the denominator modulus front is exactly a cone condition: the increment
direction must be sufficiently inward, with a tolerance determined by its size
ratio.

## 3. Relation to earlier blocks

This connects the modulus side directly to the directional side:

- `r_N = |Delta d_N|/|d_N|` is the denominator size ratio already isolated in
  E78.43-E78.47.
- `c_N = cos(angle(Delta d_N,d_N))` is the cosine partner of the directional
  sine defect from E78.43.

So the live modulus burden can be read as:

```text
size ratio small enough relative to inward angle.         (DCL-9)
```

## 4. Probe audit

Companion:

```text
E78_54_den_cone_lock_probe.py
E78_54_den_cone_lock_results.json
```

The probe reconstructs `(DCL-7)` directly from the certified Phase-77
`one_minus_theta` rows and checks agreement with the Euclidean lock.

### Exactness

For both builds:

```text
max reconstruction error < 1e-12.                         (DCL-10)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  r_N   = 0.5057780531
  c_N   = -0.9999981456
  cone margin = 1.4942182380

sigma=3.0, N=12->14:
  r_N   = 0.3819535107
  c_N   = -0.9999274211
  cone margin = 1.6179013315.                            (DCL-11)
```

Across the audited zeta ladder:

```text
median cone margin = 1.6927487779492902
min    cone margin = 1.4942182380474347
max    cone margin = 1.7381857958014306.                 (DCL-12)
```

So the audited zeta increment lies deep inside the inward cone: the angle is
almost exactly opposite to `d_N`, and comfortably beats the size threshold.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  r_N   = 6.8506848104
  c_N   =  0.9420192582
  cone margin = -8.7347233269

sigma=3.0, N=12->14:
  r_N   = 0.5472009954
  c_N   = -0.8795313845
  cone margin = 1.2118617737.                            (DCL-13)
```

So the plant fails exactly where the increment points outward and is too large;
later rows can re-enter the cone.

## 5. Consequence

This yields the cleanest geometric modulus endpoint so far:

```text
DEN-CONE-LOCK:
  prove cofinally that cos(angle(Delta d_N,d_N))
  < - |Delta d_N| / (2|d_N|).                            (DCL-14)
```

Then

```text
cone lock
=> Euclidean increment lock
=> quadratic radial increment negativity
=> radial contraction of |d_N|.                           (DCL-15)
```

## 6. Honest reading

This note does not prove the cone inequality cofinally. What it does prove is
that the modulus side can now be phrased without quotients or squared norms as a
single angular-threshold law.

That is genuinely useful because it ties the modulus front back to the direction
front already audited in E78.43-E78.45.

## 7. Status

```text
proved:
  the Euclidean increment lock is exactly equivalent to r_N + 2 c_N < 0 with
  r_N = |Delta d_N|/|d_N| and c_N = cos(angle(Delta d_N,d_N));

observed:
  the audited zeta branch lies deep inside the inward cone, with cosine nearly
  -1 and large positive cone margin;

observed:
  the planted build fails exactly where the increment points outward and is too
  large;

reduced:
  DEN-EUCLIDEAN-INCREMENT-LOCK to DEN-CONE-LOCK;

next:
  combine the existing direction-defect control with a theorem-grade size-ratio
  law, or isolate a direct shell law forcing the cosine threshold.
```
