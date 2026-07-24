# E78.50 - Radial contraction is exactly a quadratic increment negativity law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.47 reduced the modulus side to the radial contraction law

```text
|d_N+2| < |d_N|,                                          (DQI-1)
```

with

```text
d_N := 1-theta_N.                                         (DQI-2)
```

E78.44 had already introduced the centered shell increment

```text
w_N := Delta d_N / d_N
     = (d_N+2/d_N) - 1.                                   (DQI-3)
```

This note combines them and shows that radial contraction is exactly the sign of
a single quadratic shell residual in `w_N`.

## 2. Exact quadratic identity

Since

```text
d_N+2 = d_N (1+w_N),                                      (DQI-4)
```

we have

```text
|d_N+2| / |d_N| = |1+w_N|.                                (DQI-5)
```

Therefore

```text
DEN-RADIAL-CONTRACTION
<=> |1+w_N| < 1.                                          (DQI-6)
```

Squaring and expanding gives

```text
|1+w_N|^2 - 1
 = (1+w_N)(1+conj(w_N)) - 1
 = 2 Re(w_N) + |w_N|^2.                                  (DQI-7)
```

Hence the contraction law is exactly

```text
QUAD-RADIAL-INCREMENT:
  2 Re(w_N) + |w_N|^2 < 0.                                (DQI-8)
```

Equivalently,

```text
-2 Re(w_N) > |w_N|^2.                                     (DQI-9)
```

So the entire denominator modulus front reduces to a one-step dominance law:
the inward linear drift `-2 Re(w_N)` must dominate the quadratic shell size
`|w_N|^2`.

## 3. Why this is a real reduction

E78.47 phrased the front as a ratio law on `|d_N|`. This note moves the burden
entirely onto the **increment variable** `w_N`.

That is a genuine reduction because the live content is now local at one shell
step and split into:

```text
inward linear part   -2 Re(w_N),
quadratic penalty     |w_N|^2.                            (DQI-10)
```

This is more primitive than the ratio target and directly compatible with the
centered-quotient front already isolated in E78.44-E78.46.

## 4. Probe audit

Companion:

```text
E78_50_den_quadratic_radial_increment_probe.py
E78_50_den_quadratic_radial_increment_results.json
```

The probe imports the certified E78.44 rows and verifies `(DQI-7)` directly.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (DQI-11)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  w_N = -0.5057771152 + 0.0009740449 i
  2 Re(w_N)+|w_N|^2 = -0.7557427914

sigma=3.0, N=12->14:
  w_N = -0.3819257889 - 0.0046017479 i
  2 Re(w_N)+|w_N|^2 = -0.6179630935.                     (DQI-12)
```

Across the audited zeta ladder:

```text
median negative margin  = 0.5189340876643607
min    negative margin  = 0.45496200514317114
max    negative margin  = 0.7557427913616168.            (DQI-13)
```

So the audited zeta branch has a robust inward linear drift that comfortably
beats the quadratic penalty.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  w_N =  6.4534770235 + 2.2988076646 i
  2 Re(w_N)+|w_N|^2 = 59.8388364187

sigma=3.0, N=12->14:
  w_N = -0.4812804491 + 0.2603806035 i
  2 Re(w_N)+|w_N|^2 = -0.6631319689.                     (DQI-14)
```

So the plant fails exactly where the outward linear drift overwhelms everything
else, even though later rows may re-enter the contracting regime.

## 5. Consequence

This yields the sharpest modulus-side endpoint so far:

```text
DEN-QUADRATIC-RADIAL-INCREMENT:
  prove cofinally that -2 Re(w_N) > |w_N|^2.             (DQI-15)
```

Then E78.44-E78.47 recover:

```text
quadratic increment negativity
=> radial contraction of |d_N|
=> modulus subunit law
=> denominator direction chain.                           (DQI-16)
```

## 6. Honest reading

This note still does not prove the inequality cofinally. What it does prove is
that the modulus burden is not an opaque ratio law anymore; it is a single local
quadratic comparison in the centered shell increment.

That is the first genuinely more local denominator modulus target after E78.47.

## 7. Status

```text
proved:
  |d_N+2|<|d_N| is exactly equivalent to 2 Re(w_N)+|w_N|^2<0;

proved:
  the radial contraction law is equivalently the dominance inequality
  -2 Re(w_N) > |w_N|^2;

observed:
  zeta shows a strong audited negative quadratic margin on every tested row;

observed:
  the planted build fails exactly through large positive quadratic residual at
  the early breaking steps;

reduced:
  DEN-RADIAL-CONTRACTION to DEN-QUADRATIC-RADIAL-INCREMENT;

next:
  split the quadratic increment residual into the already-controlled angular
  piece and a remaining radial-linear clause, or autopsy that residual into an
  even smaller signed shell drift.
```
