# E78.37 - Denominator-direction term is controlled by a tiny chord defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.36 split the quadratic-defect drift into

```text
Qdef_N+2 - Qdef_N = NUMDIR_N + DENDIR_N,                  (DC-1)
```

with

```text
DENDIR_N
 := - < (m_N+2 + m_N)/2,  J(b_hat_N+2 - b_hat_N) >.      (DC-2)
```

This note isolates the geometric size that controls `DENDIR_N`.

## 2. Exact Cauchy control

Recall

```text
m_N := a_hat_N - J b_hat_N.                               (DC-3)
```

By Cauchy-Schwarz,

```text
|DENDIR_N|
 <= ||(m_N+2 + m_N)/2|| * ||b_hat_N+2 - b_hat_N||.       (DC-4)
```

Since `J` is orthogonal, its presence does not change the norm.

From E78.35,

```text
||m_N|| = sqrt(2 Qdef_N),                                 (DC-5)
```

so

```text
||(m_N+2 + m_N)/2||
 <= (||m_N+2|| + ||m_N||)/2
 = (sqrt(2Qdef_N+2) + sqrt(2Qdef_N))/2
 = (sqrt(Qdef_N+2) + sqrt(Qdef_N))/sqrt(2).              (DC-6)
```

Also, because `b_hat_N` are unit vectors,

```text
DIRDEF_b,N
 := (1/2) ||b_hat_N+2 - b_hat_N||^2
 = 1 - <b_hat_N+2, b_hat_N>.                             (DC-7)
```

Therefore

```text
DEN-DIRECTION-CONTROL:
|DENDIR_N|
 <= (sqrt(Qdef_N+2) + sqrt(Qdef_N)) * sqrt(DIRDEF_b,N).  (DC-8)
```

This is an exact implication, not a heuristic.

## 3. Probe audit

Companion:

```text
E78_37_den_direction_control_probe.py
E78_37_den_direction_control_results.json
```

The probe reconstructs `(DC-8)` from the E78.35/E78.36 data.

### Zeta

On the audited zeta ladder, the denominator-direction chord defect is tiny.

Representative rows:

```text
sigma=1.0:
  N=10->12  DIRDEF_b = 1.94e-06,  |DENDIR| = 2.66e-04
  N=14->16  DIRDEF_b = 2.76e-07,  |DENDIR| = 1.22e-04

sigma=3.0:
  N=10->12  DIRDEF_b = 1.75e-05,  |DENDIR| = 2.76e-04
  N=18->20  DIRDEF_b = 4.33e-06,  |DENDIR| = 2.50e-04.   (DC-9)
```

So the denominator-direction term is small because the normalized denominator
direction barely moves from one shell step to the next.

### Planted build

The planted build fails precisely here at early steps:

```text
sigma=1.0:
  N=10->12  DIRDEF_b = 4.44e-02
  N=12->14  DIRDEF_b = 6.98e-02

sigma=3.0:
  N=10->12  DIRDEF_b = 4.63e-02
  N=12->14  DIRDEF_b = 1.06e-01.                         (DC-10)
```

So the plant does not enjoy the same near-rigidity of the denominator
direction.

### Bound quality

The stored bound utilization is comfortably below `1` on all rows, as it must
be.  More importantly, on zeta the *input* `DIRDEF_b,N` is already tiny.

## 4. Consequence

This reduces the denominator correction to a strictly smaller target:

```text
prove a shell-rigidity law for the normalized denominator direction b_hat_N.
                                                             (DC-11)
```

More precisely,

```text
tiny DIRDEF_b,N
+ controlled Qdef_N
=> small DENDIR_N
=> numerator-direction dominance.                         (DC-12)
```

So the live front after E78.36 becomes

```text
DIRDEF-B-SMALLNESS
+ NUMERATOR-DIRECTION-DOMINANCE
=> QUADRATIC-DEFECT-DRIFT-SMALLNESS.                     (DC-13)
```

This is a genuine reduction because `DIRDEF_b,N` is a nonnegative geometric
scalar on the normalized `1-theta_N` direction alone.

## 5. Honest reading

This note does not yet prove `DIRDEF_b,N` is small cofinally. What it proves is
that the whole denominator-direction correction is controlled by that one
geometric quantity, and that the audited zeta rows already sit in the tiny-chord
regime while the plant does not.

That is exactly the right place for the next theorem-grade attempt.

## 6. Status

```text
proved:
  DENDIR_N is controlled by averaged misalignment size times the shell chord of
  the normalized denominator direction;

proved:
  this yields the exact reduction |DENDIR_N| <= (sqrt(Qdef_N+2)+sqrt(Qdef_N))
  * sqrt(DIRDEF_b,N);

observed:
  on the audited zeta ladder DIRDEF_b,N is tiny;

observed:
  the planted build fails through large early denominator-direction chords;

reduced:
  denominator-direction control to DIRDEF-B-SMALLNESS;

next:
  express DIRDEF_b,N directly in terms of the shell update of normalized
  (1-theta_N) and test whether it inherits a simpler finite law.
```
