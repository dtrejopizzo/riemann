# E78.36 - Polarization law for the quadratic-defect drift

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.35 reduced the angular front to the positive quadratic defect

```text
Qdef_N := (1/2) ||a_hat_N - J b_hat_N||^2,               (QP-1)
```

with

```text
a_hat_N := theta'_N/|theta'_N|,
b_hat_N := (1-theta_N)/|1-theta_N|.                      (QP-2)
```

This note expands the shell drift of `Qdef_N` into exact bilinear pieces.

## 2. Exact polarization

Let

```text
m_N := a_hat_N - J b_hat_N.                               (QP-3)
```

Then

```text
Qdef_N = (1/2) ||m_N||^2.                                 (QP-4)
```

For one shell step `N -> N+2`,

```text
Qdef_N+2 - Qdef_N
 = < (m_N+2 + m_N)/2,  m_N+2 - m_N >.                    (QP-5)
```

Since

```text
m_N+2 - m_N
 = (a_hat_N+2 - a_hat_N) - J(b_hat_N+2 - b_hat_N),       (QP-6)
```

we obtain the exact split

```text
QUADRATIC-DRIFT-POLARIZATION:
Qdef_N+2 - Qdef_N
 = NUMDIR_N + DENDIR_N,                                   (QP-7)
```

where

```text
NUMDIR_N
 := < (m_N+2 + m_N)/2,  a_hat_N+2 - a_hat_N >,

DENDIR_N
 := - < (m_N+2 + m_N)/2,  J(b_hat_N+2 - b_hat_N) >.      (QP-8)
```

So the open drift breaks exactly into:

```text
numerator-direction drift  +  denominator-direction drift. (QP-9)
```

## 3. Probe audit

Companion:

```text
E78_36_quadratic_drift_polarization_probe.py
E78_36_quadratic_drift_polarization_results.json
```

The probe reconstructs `(QP-7)` from the certified E78.35 data.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (QP-10)
```

So the polarization identity is exact to roundoff.

### Zeta

On the audited zeta ladder, the denominator-direction term is consistently
secondary.

Representative rows:

```text
sigma=1.0, N=10->12:
  delta Qdef =  0.0201606
  NUMDIR     =  0.0203669
  DENDIR     = -0.0002063

sigma=3.0, N=10->12:
  delta Qdef =  0.00240824
  NUMDIR     =  0.00279293
  DENDIR     = -0.00038469.                               (QP-11)
```

Across the audited zeta steps:

```text
the rotated-denominator term stays visibly smaller than the numerator-direction
term.                                                     (QP-12)
```

### Planted build

The planted build does not support the same hierarchy.

Representative rows:

```text
sigma=1.0, N=10->12:
  delta Qdef = -0.00514941
  NUMDIR     =  0.0197225
  DENDIR     = -0.0248719

sigma=3.0, N=10->12:
  delta Qdef = -0.293201
  NUMDIR     =  0.00693479
  DENDIR     = -0.300136.                                (QP-13)
```

So in the planted build the denominator-direction drift is not secondary; it can
dominate and flip the shell increment.

## 4. Consequence

This yields a smaller open target:

```text
if one proves that DENDIR_N is a controlled correction on the zeta cofinal
path, then the live content of the angular front moves to NUMERATOR-DIRECTION-
DRIFT for a_hat_N.                                        (QP-14)
```

Equivalently,

```text
NUMERATOR-DIRECTION-DOMINANCE
+ controlled DENDIR_N
=> QUADRATIC-DEFECT-DRIFT-SMALLNESS
=> DET-NORM-DRIFT-SMALLNESS
=> EPS-DRIFT-SMALLNESS.                                   (QP-15)
```

That is a genuine reduction because `a_hat_N` belongs to the normalized
`theta'_N` direction alone, while the denominator piece is isolated explicitly.

## 5. Honest reading

This note does not yet prove that `DENDIR_N` is uniformly controlled. What it
does prove is that the shell drift of the quadratic defect is no longer a
single opaque scalar: it is an exact two-term balance, and on the audited zeta
rows the denominator-direction term is already secondary.

That creates the next theorem-grade fork:

```text
either prove denominator-direction control,
or autopsy it and name the exact residual that blocks numerator-direction
dominance.                                                (QP-16)
```

## 6. Status

```text
proved:
  the quadratic-defect drift polarizes exactly into numerator-direction and
  denominator-direction terms;

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  on the audited zeta ladder the denominator-direction term is secondary;

observed:
  on the planted ladder the denominator-direction term can dominate and reverse
  the drift;

reduced:
  QUADRATIC-DEFECT-DRIFT-SMALLNESS to NUMERATOR-DIRECTION-DOMINANCE plus a
  controlled denominator-direction correction;

next:
  test whether the denominator-direction term itself reduces to a smaller shell
  law for the normalized direction of 1-theta_N.
```
