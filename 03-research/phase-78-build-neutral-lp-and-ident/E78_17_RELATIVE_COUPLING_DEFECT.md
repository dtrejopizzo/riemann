# E78.17 - Relative coupling defect for the current IDENT endpoint

**Run:** 2026-07-18.
**Scope:** IDENT, fixed-L finite front.

## 1. Purpose

E78.16 identified the exact remaining residual in the current tranche:

```text
Q_N = Q_ext,N - Q_t0,N - Q_theta,N.                         (RC-1)
```

The next useful question is whether this residual is naturally small only in an
absolute sense, or whether it is better read relative to the coupled scale

```text
|Q_ext| + |Q_t0| + |Q_theta|.                              (RC-2)
```

This note audits that relative defect on the certified zeta and planted rows.

## 2. Relative defect

Define

```text
RELCOUP_N(sigma)
 = |Q_N(sigma)| / (|Q_ext,N(sigma)| + |Q_t0,N(sigma)| + |Q_theta,N(sigma)|).
                                                             (RC-3)
```

This is a scale-free version of `(RC-1)`.  It does not discard the exact signed
identity; it simply measures how large the unresolved coupling defect is
compared with the total size of the three exact components.

## 3. Audit on certified rows

Using the certified artifacts

```text
E77_5y_q_functional_identity_results.json
E77_5aa_schur_logt_functional_{zeta,plant}.json
```

one gets the following values.

### Zeta

At `sigma=1.0`:

```text
N= 8   RELCOUP = 0.0450
N=10   RELCOUP = 0.00791
N=14   RELCOUP = 0.0302
N=16   RELCOUP = 0.0487
N=18   RELCOUP = 0.151.
```

At `sigma=3.0`:

```text
N= 8   RELCOUP = 0.0856
N=10   RELCOUP = 0.0167
N=14   RELCOUP = 0.0169
N=16   RELCOUP = 0.0609
N=18   RELCOUP = 0.163.
```

### Planted build

At `sigma=1.0`:

```text
N= 8   RELCOUP = 0.947
N=10   RELCOUP = 0.0661
N=14   RELCOUP = 0.293
N=16   RELCOUP = 0.623
N=18   RELCOUP = 0.0959.
```

At `sigma=3.0`:

```text
N= 8   RELCOUP = 0.269
N=10   RELCOUP = 0.137
N=14   RELCOUP = 0.235
N=16   RELCOUP = 0.685
N=18   RELCOUP = 0.313.
```

## 4. Reading

This is not yet a theorem, but it gives a sharper operational picture.

For the zeta rows that looked healthiest in the earlier audits (`N=10,14`):

```text
RELCOUP is already at the 0.8%--3% level at sigma=1 and
about 1.7% at sigma=3.
```

The planted build does not reproduce a comparably coherent low-defect regime.
Its best rows can transiently look smaller, but the profile is not stable:

```text
it jumps from 0.066 to 0.623 at sigma=1,
and from 0.137 to 0.685 at sigma=3.
```

So the candid current reading is:

```text
zeta has a low relative coupling-defect window on the live rows;
plant does not sustain such a window across the same geometry.
```

## 5. Consequence

The current exact endpoint from E78.16 can now be sharpened to the following
smallest candid residual target:

```text
RELATIVE-COUPLING-DEFECT:
prove a cofinal envelope forcing

  RELCOUP_N(sigma) -> 0

on the zeta path, using only the exact shell/cell algebra for
Q_ext, Q_t0, and Q_theta.
```

This is strictly smaller than proving an absolute bound on `Q_N` from scratch,
because it uses the exact scale of the three resolved components.

## 6. Status

```text
observed:
  on the healthy zeta rows, the relative coupling defect is already at the
  percent-level to few-percent level;

observed:
  the planted build does not sustain a comparably coherent low-defect regime;

reduced:
  the current residual target from absolute Q_N to RELATIVE-COUPLING-DEFECT;

next:
  derive RELCOUP directly from the admissible shell/cell identities and isolate
  the exact term responsible for the zeta low-defect window.
```
