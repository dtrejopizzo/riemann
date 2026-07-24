# E77.7am - Anchor/drift to shell autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7al left the shell front split into

```text
SECTOR-CERTIFICATE,
MOD4-DRIFT-SPLIT,
ANCHOR-DRIFT-TO-SHELL.
```

The natural hope was that the shell shorted energy might be a simple scalar
functional of the already measured Phase-5 anchor/drift package

```text
Q_N, Q_theta, |1-theta|.
```

This note audits that possibility directly.

## 2. Probe

Companion:

```text
E77_7am_anchor_drift_to_shell_probe.py
E77_7am_anchor_drift_to_shell_results.json
```

The probe compares, on the two shell steps already certified in
E77.7h shorted-shell anatomy,

```text
energy_over_eta = <r,S^{-1}r>/eta,
cancellation_ratio = ||r|| / max(||g||,||C^*A^{-1}h||),
```

against the Phase-5 scalar package at `sigma=3`:

```text
Q_N,
Q_theta,
|1-theta|.
```

## 3. Result

### Zeta

For the two available shell steps:

```text
16 -> 18:
  energy/eta   = 9.02e-5
  resRatio     = 1.95e-5
  Q3           = 1.417
  Qtheta3      = 10.921
  |1-theta|    = 0.03277

18 -> 20:
  energy/eta   = 1.48e-8
  resRatio     = 2.03e-9
  Q3           = 3.558
  Qtheta3      = 9.137
  |1-theta|    = 0.02419
```

The shell energy and shell residual norm collapse by roughly four orders of
magnitude from one shell to the next, while the anchor/drift scalars remain
order-one or drift only mildly.

### Planted build

For comparison:

```text
16 -> 18:
  energy/eta   = 2.29e-1
  resRatio     = 8.12e-1
  Q3           = 13.545
  Qtheta3      = 5.495
  |1-theta|    = 5.568

18 -> 20:
  energy/eta   = 1.87e-1
  resRatio     = 1.468
  Q3           = 6.138
  Qtheta3      = 6.744
  |1-theta|    = 5.837
```

Again there is no simple proportionality.  The planted shell energy stays
macroscopic while the anchor package drifts on a much milder scale.

## 4. Autopsy

The hoped-for shortcut is refuted:

```text
ANCHOR-DRIFT-TO-SHELL is not a one-line scalar comparison
between <r,S^{-1}r>/eta and any single Phase-5 anchor/drift functional.
```

In particular, none of

```text
Q_N,
Q_theta,
|1-theta|,
```

tracks the shell-energy collapse on its own.

So the missing connector is not a scalar proportionality law.  It must be a
finer finite identity that keeps the shell residual as a vector-level paired
object before the final shorted scalar is formed.

This matches the structural lesson of E77.7h:

```text
the decisive cancellation is in
r = g - C^*A^{-1}h,
not in g or in the Schur anchor package separately.
```

## 5. Smaller live object

The connector must therefore be reformulated as:

```text
VECTOR-LEVEL-ANCHOR-DRIFT-TO-SHELL:
derive an exact finite identity expressing the shell residual vector
r_{R,M}
through the active Schur anchor package and the mod4 drift decomposition,
before taking the shorted pairing <r,S^{-1}r>.
```

This is strictly smaller and more honest than any scalar comparison target.

## 6. Status

```text
refuted:   scalar proportionality from anchor/drift functionals to shell
           shorted energy;
clarified: the missing shell connector remains vector-level, not scalar;
refined:   ANCHOR-DRIFT-TO-SHELL -> VECTOR-LEVEL-ANCHOR-DRIFT-TO-SHELL;
next:      derive that vector identity directly from the common-core
           moving-boundary Schur decomposition of E77.5k and the exact
           log-transfer decomposition of E77.5aa/5y.
```
