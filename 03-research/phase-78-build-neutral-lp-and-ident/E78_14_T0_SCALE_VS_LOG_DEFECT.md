# E78.14 - `t0` drives the transfer scale, but not the signed log defect

**Run:** 2026-07-18.
**Scope:** IDENT, fixed-L finite front.

## 1. Purpose

E78.13 showed that on the audited zeta step the growth of `|T|` is mainly
driven by the growth of `|t0|`, with `|1-theta|` acting as a moderating factor.
This raises a natural hope:

```text
maybe the live IDENT front can now be reduced from the full quotient defect
Delta[T'/T]
to a theorem just about the t0 block.
```

This note shows that this hope is false.  The transfer scale and the signed
log-defect are different layers of the geometry.

## 2. Exact decomposition

From E77.5aa:

```text
T = t0(1-theta),                                            (TS-1)

T'/T = t0'/t0 - theta'/(1-theta).                           (TS-2)
```

Hence the invariant log-transfer quantity splits exactly as

```text
Delta logT = Delta logT_t0 + Delta logT_theta,              (TS-3)
```

and at the second signed-drift level,

```text
Q_logT = Q_t0 + Q_theta.                                    (TS-4)
```

So there are two logically different questions:

```text
1. what drives the magnitude scale |T|?
2. what drives the signed defect Delta[T'/T] or Q_logT?
```

E78.13 only addresses the first.

## 3. Evidence from the certified Phase-77 ledger

The Phase-77 exact decomposition already answers the second question on the
tested zeta ladder.

At `sigma=3.0`:

```text
N=10:   Q_logT =  9.03968,   Q_t0 = -1.55781,   Q_theta = 10.5975
N=14:   Q_logT = 11.1079,    Q_t0 = -1.38793,   Q_theta = 12.4958
N=18:   Q_logT =  7.98492,   Q_t0 = -1.15193,   Q_theta =  9.13685.
```

At `sigma=1.0`:

```text
N=10:   Q_logT = 3.19223,    Q_t0 = -0.559794,  Q_theta = 3.75203
N=14:   Q_logT = 3.81570,    Q_t0 = -0.481859,  Q_theta = 4.29756
N=18:   Q_logT = 2.73296,    Q_t0 = -0.394419,  Q_theta = 3.12738.
```

So on the zeta ladder:

```text
Q_t0 is a small negative background;
Q_theta carries the main signed profile.                     (TS-5)
```

Meanwhile the planted build does not preserve this regime: `Q_t0` can be large,
change sign, or dominate irregularly.

## 4. Verdict

The reduction

```text
T0-DRIVEN-TRANSFER
=> closure of the signed IDENT defect
```

is false.

More precisely:

```text
1. t0 controls the growth scale of |T| on the audited zeta step;
2. but the signed quotient defect lives in T'/T, not in |T|;
3. the certified decomposition (TS-4) shows that the active signed profile is
   carried by Q_theta, not by Q_t0.
```

So the `t0` block is structurally important, but only as part of the exact
product / quotient geometry.  It is not an autonomous forcing mechanism for the
IDENT defect.

## 5. Consequence for the live front

The candid reduction is therefore:

```text
T0-DRIVEN-TRANSFER is a geometric side law,
not the final arithmetic defect law.
```

The live signed front remains coupled:

```text
large t0-driven transfer scale
+ controlled near-anchor 1-theta
+ theta-logderivative coupling
=> Delta[T'/T].                                              (TS-6)
```

In particular, the old Phase-77 target

```text
THETA-LOGDERIV-COUPLING
```

is not superseded by E78.13.  It reappears as the active signed ingredient once
the transfer scale has been factored out.

## 6. Status

```text
proved:
  t0-driven transfer growth and signed log-defect are distinct layers of the
  exact shell geometry;

refuted:
  reduction of the live IDENT defect to the t0 block alone;

clarified:
  t0 explains the size of the denominator, but Q_theta explains the signed
  defect profile;

reduced:
  the live front to the coupled law
    t0 scale + near-anchor control + theta-logderivative coupling;

next:
  re-import the exact Phase-77 theta-logderivative machinery as the signed part
  of the current Phase-78 IDENT front, now with the t0 scale separated cleanly.
```
