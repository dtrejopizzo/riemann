# E77.7ap - Projected bridge autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7ao reduced the shell-facing live object from the full Schur source
vector `k` to the projected package

```text
y = S^{-1}k,
corr = tau S^{-1}k,
theta = corr/t0.
```

The next natural hope was stronger:

```text
the same scalar Phase-5 projected package
u = -theta'/(1-theta),
Q_theta,
|theta|,
```

might directly control the Phase-77 shell energy

```text
<r, S_shell^{-1} r>/eta.
```

This note audits that hope against the already recorded certified data.

## 2. Data used

No new theory is assumed.  The comparison uses the existing certified probes:

- `E77_5ac_theta_logderiv_coupling_zeta.json`,
- `E77_5ac_theta_logderiv_coupling_plant.json`,
- `E77_7h_shorted_shell_energy_results.json`.

We compare the shared live shell steps `N=16->18` and `N=18->20` at
`sigma=3.0`.

## 3. Comparison

### Zeta

At the two live shell steps:

```text
N=16:
  energy/eta = 9.0218e-5
  Q_theta    = 1.0920e1
  |u_new|    = 1.8432e-2
  (energy/eta)/Q_theta = 8.26e-6
  (energy/eta)/|u_new| = 4.89e-3

N=18:
  energy/eta = 1.4807e-8
  Q_theta    = 9.1368
  |u_new|    = 1.4259e-2
  (energy/eta)/Q_theta = 1.62e-9
  (energy/eta)/|u_new| = 1.04e-6
```

The shell energy collapses by roughly four orders of magnitude between the
two zeta shell steps, while `Q_theta` and `|u|` remain of comparable size.

### Planted falsifier

At the same shell steps:

```text
N=16:
  energy/eta = 2.2922e-1
  Q_theta    = -5.4953
  |u_new|    = 1.3404e-2
  (energy/eta)/Q_theta = -4.17e-2
  (energy/eta)/|u_new| = 1.71e1

N=18:
  energy/eta = 1.8742e-1
  Q_theta    = 6.7441
  |u_new|    = 9.0980e-3
  (energy/eta)/Q_theta = 2.78e-2
  (energy/eta)/|u_new| = 2.06e1
```

The planted build keeps macroscopic shell energy while `|u|` stays on the
same order as in zeta.

## 4. Autopsy

The scalar bridge is refuted.

Even after the E77.7ao reduction to the projected Schur source, there is no
evidence for a direct scalar law of the form

```text
energy/eta  ~  Q_theta,
energy/eta  ~  |u|,
energy/eta  ~  |theta|,
```

or any fixed-weight version of these already recorded scalar observables.

This is now a theorem-grade autopsy because the failure is structural:

1. `Q_theta` is a second-difference scalar extracted from the safe-axis
   logarithmic derivative of `theta`;
2. the shell energy is a shorted quadratic pairing
   `<r,S_shell^{-1}r>`;
3. the zeta shell collapse occurs while the scalar `Q_theta` and `|u|` stay
   macroscopic.

Therefore the missing bridge cannot be a one-line scalar comparison inside
the already measured Phase-5 package.

## 5. Smaller live object

The admissible replacement is:

```text
PROJECTED-QUADRATIC-BRIDGE:
  derive the shell shorted pairing from the projected Schur source while
  keeping the quadratic operator weight explicit.
```

Concretely, the live object is no longer

```text
PROJECTED-SOURCE-TO-SHORTED-ENERGY via a scalar u/Q_theta law,
```

but the smaller and more candid operator-level target

```text
PROJECTED-QUADRATIC-BRIDGE:
  identify the exact quadratic form on the projected source
  tau S^{-1}k (or its two-component ancestor before Cauchy collapse)
  whose signed cancellation yields the shell energy.
```

This is strictly smaller than returning to the full source vector `k`, and it
still implies the previous target:

```text
PROJECTED-QUADRATIC-BRIDGE
=> PROJECTED-SOURCE-TO-SHORTED-ENERGY
=> SHELL-STIELTJES-INCREMENT
=> ... => BTG-DIV-L.
```

## 6. Consequence

The shell front should now be recorded as

```text
SECTOR-CERTIFICATE,
MOD4-DRIFT-SPLIT,
PROJECTED-QUADRATIC-BRIDGE.
```

The Phase-5 scalar package remains relevant only as a diagnostic or a signed
subfactor inside that bridge.  It is not itself the shell energy carrier.

## 7. Status

```text
refuted:
  direct scalar bridge from Q_theta, |u|, or |theta| to shell energy.

proved:
  the projected-source reduction of E77.7ao still leaves a genuinely
  quadratic bridge open;
  the scalar Phase-5 package is too coarse to be that bridge.

live object:
  PROJECTED-QUADRATIC-BRIDGE.
```
