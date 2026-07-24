# E78.48 - The radial contraction law is equivalently a normalized squared drop

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.47 reduced the modulus side to the radial contraction law

```text
|d_N+2| / |d_N| < 1,                                      (DSR-1)
```

with

```text
d_N := 1-theta_N.                                         (DSR-2)
```

The natural next question is whether the contraction target becomes materially
smaller when written in squared norm.

## 2. Exact squared-drop identity

From E78.47,

```text
|q_N| = |d_N+2| / |d_N|.                                  (DSR-3)
```

Therefore

```text
(|d_N|^2 - |d_N+2|^2) / |d_N|^2
 = 1 - |q_N|^2
 = (1-|q_N|)(1+|q_N|).                                    (DSR-4)
```

This is exact.

So the normalized squared drop is not a new shell object. It is the old radial
deficit multiplied by the explicit positive factor `1+|q_N|`.

## 3. Consequence

This gives an honest equivalence, not a genuine reduction:

```text
DEN-RADIAL-CONTRACTION
<=> POSITIVE-NORMALIZED-SQUARED-DROP,                     (DSR-5)
```

because `1+|q_N| > 0` always.

So proving positivity of the squared drop is exactly the same burden as proving
the radial contraction from E78.47. The squared-norm version is useful as an
algebraic reformulation, but it does not create a smaller target.

## 4. Probe audit

Companion:

```text
E78_48_den_squared_radial_drop_probe.py
E78_48_den_squared_radial_drop_results.json
```

The probe imports the certified E78.47 rows and verifies `(DSR-4)` directly.

### Exactness

For both builds:

```text
max reconstruction error < 1e-13.                         (DSR-6)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  (|d_N|^2-|d_N+2|^2)/|d_N|^2 = 0.7557427914
  (1-|q_N|)(1+|q_N|)          = 0.7557427914

sigma=3.0, N=12->14:
  normalized squared drop      = 0.6179630935
  reconstructed value          = 0.6179630935.           (DSR-7)
```

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  normalized squared drop      = -59.8388364187
  reconstructed value          = -59.8388364187

sigma=3.0, N=12->14:
  normalized squared drop      = 0.6631319689
  reconstructed value          = 0.6631319689.           (DSR-8)
```

So the squared-drop picture records exactly the same success/failure pattern as
the radial contraction law.

## 5. Honest reading

This note is intentionally half theorem and half autopsy.

Theorem:
the normalized squared drop is an exact shell scalar with clean algebra.

Autopsy:
it is **not** a smaller target than E78.47, because it differs from the radial
deficit only by the harmless positive factor `1+|q_N|`.

That matters because it tells us not to burn more phase budget on squared-norm
renamings of the same modulus law.

## 6. Status

```text
proved:
  the normalized squared denominator drop equals (1-|q_N|)(1+|q_N|) exactly;

proved:
  positivity of the squared drop is equivalent to DEN-RADIAL-CONTRACTION;

observed:
  the zeta/planted audit is exactly the same as for the radial contraction law;

autopsied:
  the squared-norm reformulation does not yield a smaller theorem-grade target;

next:
  seek a true shell recurrence or drift law for |1-theta_N| itself, rather than
  further equivalent norm rewritings.
```
