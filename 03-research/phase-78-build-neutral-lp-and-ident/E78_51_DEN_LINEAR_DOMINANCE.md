# E78.51 - The quadratic radial increment splits into a dominant linear drift

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.50 reduced the modulus side to the local quadratic shell law

```text
2 Re(w_N) + |w_N|^2 < 0,                                  (DLD-1)
```

with

```text
w_N := Delta d_N / d_N,   d_N := 1-theta_N.               (DLD-2)
```

This note asks whether the burden lies on both terms equally, or whether one of
them is already secondary on the audited zeta ladder.

## 2. Exact linear-plus-quadratic split

Rewrite E78.50 as

```text
QUAD-RADIAL-INCREMENT
<=> -2 Re(w_N) > |w_N|^2.                                 (DLD-3)
```

So the shell contraction mechanism decomposes exactly into

```text
inward linear drift   L_N := -2 Re(w_N),
quadratic penalty     Q_N := |w_N|^2.                     (DLD-4)
```

The live comparison is therefore

```text
LINEAR-DOMINANCE:
  L_N > Q_N.                                               (DLD-5)
```

This is exact and equivalent to E78.50.

## 3. Finer quadratic anatomy

Because

```text
|w_N|^2 = Re(w_N)^2 + Im(w_N)^2,                          (DLD-6)
```

the quadratic penalty itself splits into:

```text
radial self-penalty    Re(w_N)^2,
angular penalty        Im(w_N)^2.                         (DLD-7)
```

So the remaining shell burden after E78.50 is not an opaque quadratic norm: it
is the competition between the inward linear drift and these two penalties.

## 4. Probe audit

Companion:

```text
E78_50_den_quadratic_radial_increment_results.json
```

No new probe is needed: E78.50 already computes `Re(w_N)` and `|w_N|^2`
exactly, and the present note only repackages those certified values.

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  L_N = 1.0115542304
  Q_N = 0.2558114390
  margin = 0.7557427914

sigma=3.0, N=12->14:
  L_N = 0.7638515779
  Q_N = 0.1458884843
  margin = 0.6179630935.                                 (DLD-8)
```

Across the audited zeta ladder:

```text
median L_N          = 0.6144707223305843
median Q_N          = 0.0955366346662237
median Q_N / L_N    = 0.15361986393753707
max    Q_N / L_N    = 0.25288949551879525.               (DLD-9)
```

So on the audited zeta ladder the inward linear drift exceeds the whole
quadratic penalty by a comfortable factor.

Moreover, the angular piece inside `Q_N` is tiny:

```text
median Im(w_N)^2 / |w_N|^2 = 1.653634047323052e-05
max    Im(w_N)^2 / |w_N|^2 = 1.4515253467406683e-04.     (DLD-10)
```

Thus, for zeta, the quadratic penalty is almost entirely radial and already much
smaller than the linear inward drift.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  L_N = -12.9069540470
  Q_N = 46.9318823717
  margin = -59.8388364187

sigma=3.0, N=12->14:
  L_N = 0.9625608982
  Q_N = 0.2994289294
  margin = 0.6631319689.                                 (DLD-11)
```

So the plant fails exactly when the linear part itself points outward; the
quadratic term only amplifies that failure.

## 5. Consequence

This yields the sharpest honest modulus-side endpoint so far:

```text
DEN-LINEAR-INWARD-DRIFT:
  prove cofinally that -2 Re(w_N) dominates |w_N|^2.     (DLD-12)
```

On the audited zeta ladder the real remaining burden is therefore the sign and
size of `Re(w_N)`. The angular part is already negligible at this scale.

This is a genuine reduction in emphasis: the phase/aerial geometry is no longer
the main obstacle on the modulus side.

## 6. Honest reading

This note does not prove the dominance cofinally. What it does prove is that
the local quadratic front from E78.50 is already numerically one-sided:

```text
zeta:
  inward linear drift is the driver;

plant:
  failure occurs when the linear drift itself flips sign. (DLD-13)
```

So the next theorem-grade target should focus on the sign and lower control of
`Re(w_N)`, not on a separate angular penalty mechanism.

## 7. Status

```text
proved:
  the quadratic radial increment law is exactly the linear-dominance inequality
  -2 Re(w_N) > |w_N|^2;

observed:
  on the audited zeta ladder the quadratic penalty is only about 15% of the
  linear inward drift in median, and at most about 25.3%;

observed:
  the angular contribution Im(w_N)^2 is tiny inside |w_N|^2 on zeta;

observed:
  the planted build fails when the linear drift itself turns outward;

reduced:
  DEN-QUADRATIC-RADIAL-INCREMENT to the inward linear drift burden for Re(w_N),
  with quadratic/imaginary corrections already secondary on zeta;

next:
  isolate a finite shell law for Re(w_N), or autopsy it into a still more
  primitive signed update scalar.
```
