# E72.129 -- Mass root-factor audit

**Date:** 2026-07-09.
**Role:** test whether the remaining mass gain is explained by a simple scalar root factor.

## 0. Question

The remaining estimate is:

```text
m_xY_x(tau_j)->0.                                           (MG)
```

Since `tau_j` is a finite CCM root,

```text
M_xi(tau_j)=sum_n xi_n/(tau_j-d_n)=0.
```

The simplest possible closure would be that the mass leakage contains an explicit scalar root factor
such as `M_k(tau_j)`, `M'_k(tau_j)`, `M'_xi(tau_j)`, or the mismatch between actual and model roots.

## 1. Probe

The companion script:

```text
E72_129_mass_root_factor_probe.py
```

reports medians of:

```text
L^2|mass|/|M_k(tau_j)|,
|mass|/|M'_k(tau_j)|,
|mass|/|M'_xi(tau_j)|,
dist(tau_j, Tau_k).
```

This is only a factor audit.  A stable ratio would suggest a scalar root-factor identity; unstable
ratios reject that shortcut.

## 2. Status

```text
observed: L^2|mass|/|M_k| is often O(1), but has large outliers when the scalar factor is small;
rejected: a uniform scalar root-factor proof as the sole explanation of MG;
kept:     MG must be treated as a shorted-matrix effect.
```
