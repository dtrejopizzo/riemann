# E78.18 - Exact factorization of the relative coupling defect

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.17 reduced the current fixed-`L` residual target to

```text
RELCOUP_N
 = |Q_N| / (|Q_ext,N| + |Q_t0,N| + |Q_theta,N|),          (RF-1)
```

where

```text
Q_N = Q_ext,N - Q_t0,N - Q_theta,N.                       (RF-2)
```

The immediate question is whether `(RF-1)` is genuinely a new three-term
object, or whether it factors through the already-certified two-term quotient
geometry from E78.7-E78.10.

This note shows that it factors **exactly**.

## 2. Exact factorization

Write

```text
Q_logT,N = Q_t0,N + Q_theta,N.                            (RF-3)
```

Then `(RF-2)` is

```text
Q_N = Q_ext,N - Q_logT,N,                                 (RF-4)
```

and therefore

```text
RELCOUP_N
 = |Q_ext,N - Q_logT,N|
   / (|Q_ext,N| + |Q_t0,N| + |Q_theta,N|).                (RF-5)
```

Multiply and divide by `|Q_ext,N| + |Q_logT,N|`:

```text
RELCOUP_N
 = LOGT-CANCEL_N * SCHUR-COMPRESSION_N,                   (RF-6)
```

with

```text
LOGT-CANCEL_N
 := |Q_ext,N - Q_logT,N| / (|Q_ext,N| + |Q_logT,N|),      (RF-7)

SCHUR-COMPRESSION_N
 := (|Q_ext,N| + |Q_logT,N|)
    / (|Q_ext,N| + |Q_t0,N| + |Q_theta,N|).               (RF-8)
```

So `RELCOUP` is not a fresh three-body smallness problem. It is exactly:

```text
old two-term mismatch  x  Schur denominator compression.
```

## 3. Equivalent slack form

By the triangle inequality,

```text
|Q_logT,N| <= |Q_t0,N| + |Q_theta,N|,                     (RF-9)
```

so

```text
0 < SCHUR-COMPRESSION_N <= 1.                             (RF-10)
```

Define the normalized triangle slack

```text
TRIANGLE-SLACK_N
 := (|Q_t0,N| + |Q_theta,N| - |Q_logT,N|)
    / (|Q_ext,N| + |Q_t0,N| + |Q_theta,N|).               (RF-11)
```

Then

```text
SCHUR-COMPRESSION_N = 1 - TRIANGLE-SLACK_N.               (RF-12)
```

Hence the E78.17 residual splits into:

```text
RELCOUP_N
 = LOGT-CANCEL_N * (1 - TRIANGLE-SLACK_N).                (RF-13)
```

The unresolved work is therefore sharply localized:

```text
either show LOGT-CANCEL_N -> 0 on a cofinal envelope,
or show that the Schur slack is uniformly harmless there.
```

## 4. Probe audit

The companion probe

```text
E78_18_relcoup_factor_probe.py
E78_18_relcoup_factor_results.json
```

reconstructs `(RF-6)` from the certified Phase-77 JSONs. The reconstruction
error is at roundoff for both builds.

Representative rows:

### Zeta

```text
sigma=1.0, N=10:
  RELCOUP            = 0.007906
  LOGT-CANCEL        = 0.009306
  SCHUR-COMPRESSION  = 0.849623
  TRIANGLE-SLACK     = 0.150377

sigma=3.0, N=14:
  RELCOUP            = 0.016914
  LOGT-CANCEL        = 0.019068
  SCHUR-COMPRESSION  = 0.887050
  TRIANGLE-SLACK     = 0.112950
```

Across the audited zeta rows:

```text
SCHUR-COMPRESSION stays in the narrow band 0.8206-0.8985,
equivalently TRIANGLE-SLACK stays in 0.1015-0.1794.
```

So on the healthy zeta rows, E78.17 smallness is driven mainly by
`LOGT-CANCEL`, not by a wild denominator effect from the Schur split.

### Planted build

```text
sigma=1.0, N=10:
  RELCOUP            = 0.066085
  LOGT-CANCEL        = 0.477739
  SCHUR-COMPRESSION  = 0.138332
  TRIANGLE-SLACK     = 0.861668

sigma=3.0, N=14:
  RELCOUP            = 0.234857
  LOGT-CANCEL        = 0.250481
  SCHUR-COMPRESSION  = 0.937649
  TRIANGLE-SLACK     = 0.062351
```

The planted build does not show a stable compression regime:

```text
SCHUR-COMPRESSION ranges from 0.1383 up to 1.0000,
equivalently TRIANGLE-SLACK ranges from 0 up to 0.8617.
```

So the plant can look small in `RELCOUP` for two very different reasons:

```text
sometimes because LOGT-CANCEL is smaller,
sometimes because the Schur split itself compresses the denominator heavily.
```

That instability is exactly the opposite of the zeta pattern.

## 5. Consequence for the live target

E78.17 can now be sharpened one more step.

The smallest candid residual target is no longer raw `RELCOUP -> 0`, but

```text
LOGT-CANCEL-COFINAL:
prove a cofinal envelope on which

  LOGT-CANCEL_N -> 0

and the Schur compression factor stays uniformly away from 0.
```

Because of `(RF-6)`, this implies the E78.17 target immediately:

```text
LOGT-CANCEL-COFINAL + lower bound on SCHUR-COMPRESSION
=> RELATIVE-COUPLING-DEFECT.                              (RF-14)
```

For zeta, the certified rows already suggest the second clause is the easy one:
the compression factor looks stable and bounded below by a comfortable constant.
The real content remains the signed two-term cancellation between `Q_ext` and
`Q_logT`.

## 6. Status

```text
proved:
  exact factorization RELCOUP = LOGT-CANCEL * SCHUR-COMPRESSION;

proved:
  equivalently RELCOUP = LOGT-CANCEL * (1 - TRIANGLE-SLACK);

observed:
  on zeta rows, SCHUR-COMPRESSION is stable (0.82-0.90) and therefore
  RELCOUP smallness tracks LOGT-CANCEL smallness;

observed:
  on planted rows, SCHUR-COMPRESSION is unstable and can itself create small
  RELCOUP values transiently;

reduced:
  RELATIVE-COUPLING-DEFECT to LOGT-CANCEL-COFINAL plus a uniform lower bound on
  SCHUR-COMPRESSION;

next:
  attack LOGT-CANCEL directly through the exact quotient identity
  Q_ext - Q_logT = Q_ext - W'/(1+W),
  keeping the Schur compression as a side condition rather than the main front.
```
