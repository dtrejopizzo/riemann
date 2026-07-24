# E77.7ao - Projected source reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7an identified the shell residual with the exact Schur active source

```text
r  <=>  k = g_a - A_ac A_cc^{-1} g_c.
```

That was an honest reduction, but it may still be too strong.  The exact
Phase-5 identities never use `k` directly: they first solve

```text
y = S^{-1} k,
```

and only then form the projected Cauchy scalar

```text
corr = tau y = tau S^{-1} k,
theta = corr / t0.
```

This note audits whether the live shell-facing object is really the full
vector `k`, or only the resolved/projection package

```text
y = S^{-1}k,
tau S^{-1}k.
```

## 2. Exact structural observation

The probe formulas show the same pattern on both sides:

- Phase 5 log-transfer chain:

```text
k = g_a - A_ac A_cc^{-1} g_c,
y = S^{-1}k,
corr = tau y,
theta = corr/t0.
```

- Phase 77 shell-energy chain:

```text
r = h_s - K_os^* x_old,
energy = <r, S_shell^{-1} r>.
```

So once E77.7an identifies `r <=> k`, the active source still enters every
exact scalar observable only after resolvent action or Cauchy projection.  No
already-proved exact identity uses the bare norm of `k` as its terminal
object.

## 3. Probe

Companion:

```text
E77_7ao_projected_schur_source_probe.py
```

The audit compares, at the live `sigma=3` shell steps,

```text
||k_N||,
||y_N|| = ||S_N^{-1}k_N||,
|tau_N y_N| = |tau_N S_N^{-1}k_N|,
```

against the already certified shell collapse package

```text
energy_over_eta,
cancellation_ratio.
```

## 4. Results

### Zeta

For the two shell steps already used in E77.7h:

```text
16 -> 18:
  k_rel_change      = 4.32e-1
  y_rel_change      = 3.62e-1
  |tau y| rel_change = 9.91e-1
  energy/eta        = 9.02e-5
  residual ratio    = 1.95e-5

18 -> 20:
  k_rel_change      = 8.23e-1
  y_rel_change      = 7.85e-1
  |tau y| rel_change = 9.46e-1
  energy/eta        = 1.48e-8
  residual ratio    = 2.03e-9
```

The key point is qualitative:

```text
the shell collapse tracks the projected object |tau S^{-1}k|,
not the raw source norm ||k||.
```

The raw Schur source and even the resolved vector `S^{-1}k` still move on an
order-one scale; the near-annihilation shows up only after the Cauchy
projection.

### Planted falsifier

At the shared shell step:

```text
16 -> 18:
  k_rel_change      = 5.22e-1
  y_rel_change      = 6.75e-1
  |tau y| rel_change = 7.84e-1
  energy/eta        = 2.29e-1
  residual ratio    = 8.12e-1
```

So the same projected package stays macroscopic precisely where the planted
shell energy stays macroscopic.

## 5. Autopsy

This refines E77.7an in an important way.

The full vector connector

```text
SCHUR-SOURCE-TO-SHORTED-ENERGY:
  control the exact Schur source vector k.
```

is admissible, but stronger than what the exact formulas currently expose.

The smaller shell-facing object is:

```text
PROJECTED-SCHUR-SOURCE:
  control the resolved/projection package
  y = S^{-1}k,
  corr = tau S^{-1}k,
  and in particular the shell-facing collapse of corr.
```

Equivalently, the live connector can be reformulated as

```text
PROJECTED-SOURCE-TO-SHORTED-ENERGY:
  derive the shell shorted energy from the exact projected Schur source
  tau S^{-1}k, not from the bare source norm ||k||.
```

This is a strict reduction of target size:

- it keeps the exact finite Schur algebra already certified in E77.5aa/5ac;
- it matches the observed zeta collapse site;
- it remains neutral to the falsifier at the structural level, because the
  plant build also passes through the same projection package and simply fails
  to cancel there.

## 6. Consequence for the live chain

The shell front should now be recorded as

```text
SECTOR-CERTIFICATE,
MOD4-DRIFT-SPLIT,
PROJECTED-SOURCE-TO-SHORTED-ENERGY.
```

The operative exact object is no longer "the whole vector `k`", but the
projected/resolved connector seen by both the log-transfer and shell-energy
formulas:

```text
u = -theta'/(1-theta),
theta = (tau S^{-1}k)/t0,
energy = <k, S^{-1}k> on the shell side.
```

What remains open is the theorem-grade bridge between the Phase-5 signed
projection law (`u`, `Q_theta`, mod4 drift) and the shell shorted pairing.

## 7. Status

```text
proved:
  the exact formulas use k only after resolvent action/projection;
  on the zeta shell steps, the dramatic collapse is visible in |tau S^{-1}k|
  and not in ||k|| alone;
  the planted build keeps the same projected package macroscopic where the
  shell energy stays macroscopic.

refined:
  SCHUR-SOURCE-TO-SHORTED-ENERGY
  -> PROJECTED-SOURCE-TO-SHORTED-ENERGY.

live object:
  derive the shell shorted-energy collapse from the exact projected Schur
  source tau S^{-1}k together with the signed Phase-5 sector/drift laws.
```
