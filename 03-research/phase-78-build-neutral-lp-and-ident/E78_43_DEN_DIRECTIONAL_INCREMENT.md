# E78.43 - The denominator increment area reduces to a directional defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.42 reduced the denominator side to the increment area

```text
det(Delta d_N, d_N),                                      (DDI-1)
```

with

```text
d_N := 1-theta_N,
Delta d_N := d_N+2 - d_N.                                 (DDI-2)
```

This note removes the remaining scale dependence.

## 2. Exact directional normalization

Whenever `Delta d_N != 0` and `d_N != 0`, define

```text
DIRINC_N
 := det(Delta d_N, d_N) / (|Delta d_N| |d_N|).           (DDI-3)
```

Because the determinant of two planar vectors equals the product of their norms
times the sine of the angle between them, we have the exact identity

```text
DIRINC_N = sin(angle(Delta d_N, d_N)).                    (DDI-4)
```

Therefore

```text
det(Delta d_N, d_N)
 = |Delta d_N| |d_N| DIRINC_N.                            (DDI-5)
```

Combining with E78.42 gives

```text
Im((1-theta_N+2)/(1-theta_N))
 = (|Delta d_N| / |d_N|) DIRINC_N.                       (DDI-6)
```

So the denominator shell numerator splits exactly into:

```text
size ratio  *  directional defect.                       (DDI-7)
```

This is the cleanest denominator factorization so far.

## 3. Probe audit

Companion:

```text
E78_43_den_directional_increment_probe.py
E78_43_den_directional_increment_results.json
```

The probe computes the normalized defect `(DDI-3)` from the certified E78.42
rows.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  DIRINC_N =  0.0019258345647960755
  N=12->14  DIRINC_N = -0.003811646612157685
  N=20->22  DIRINC_N = -0.0022928945984962744

sigma=3.0:
  N=10->12  DIRINC_N =  0.006291823565166093
  N=12->14  DIRINC_N = -0.012047926571575048
  N=20->22  DIRINC_N = -0.006966881143171652.            (DDI-8)
```

Across the audited zeta ladder:

```text
median |DIRINC_N| = 0.004058962354682538
max    |DIRINC_N| = 0.012047926571575048.                (DDI-9)
```

So the increment direction is nearly aligned with the denominator vector on the
audited zeta branch.

### Planted build

Representative rows:

```text
sigma=1.0:
  N=10->12  DIRINC_N =  0.33555881320398545
  N=12->14  DIRINC_N =  0.4229232321644782

sigma=3.0:
  N=10->12  DIRINC_N =  0.3434933502338121
  N=12->14  DIRINC_N =  0.4758408805416269.              (DDI-10)
```

Across the audited planted ladder:

```text
median |DIRINC_N| = 0.11949996690414152
max    |DIRINC_N| = 0.4758408805416269.                  (DDI-11)
```

So the plant fails already at the directional level: the increment vector swings
through an order-one angle relative to the denominator vector.

## 4. Consequence

This yields the smallest denominator target so far:

```text
DEN-DIRECTIONAL-INCREMENT-SMALLNESS:
  prove that DIRINC_N stays small cofinally on zeta.      (DDI-12)
```

Then, together with the already audited size ratio `|Delta d_N|/|d_N|`, we get

```text
small directional defect
+ controlled size ratio
=> small Im(q_b,N)
=> denominator rigidity chain.                            (DDI-13)
```

This is a genuine reduction because the live content is now a pure directional
increment law, with the size scale factored off explicitly.

## 5. Honest reading

This note does not yet prove the directional defect is small cofinally. What it
does prove is that the denominator obstruction has been reduced to the angle
between the shell increment `Delta d_N` and the old denominator vector `d_N`.

That is the most local finite denominator object named so far.

## 6. Status

```text
proved:
  the denominator increment area factors exactly as |Delta d_N| |d_N| times a
  directional defect DIRINC_N;

proved:
  Im((1-theta_N+2)/(1-theta_N)) = (|Delta d_N|/|d_N|) DIRINC_N;

observed:
  zeta keeps |DIRINC_N| below about 0.0121 on the audited ladder;

observed:
  the planted build shows order-10^-1 to order-1 directional defects at the
  early failing steps;

reduced:
  the denominator increment-area target to DEN-DIRECTIONAL-INCREMENT-SMALLNESS;

next:
  isolate an exact shell law for the direction of Delta d_N relative to d_N, or
  autopsy that angle into an even smaller normalized update residual.
```
