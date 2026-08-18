# E78.81 - The weighted normalized shell derivative decreases across the audited safe sigma slices

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.80 suggested the constant-envelope candidate

```text
Y_N(sigma) := N * (-SAFEDELTA_N(i sigma)) / A_N        (WSM-1)
```

with the observation that the `sigma=3.0` slice sat below the `sigma=1.0` slice
for `N=8,...,18`.

This note extends that audit to every currently available `N` row in the common
source and records the resulting monotonicity pattern.

## 2. Source reconstruction

The companion probe reconstructs `A_N` directly from the `points` table in

```text
E77_5ac_theta_logderiv_coupling_zeta.json,             (WSM-2)
```

using

```text
A_N = N * (safe_u_old - safe_u_new),                   (WSM-3)
```

and pairs that with `SAFEDELTA_N` from

```text
E77_5g_schur_phase_increment_results.json.             (WSM-4)
```

This avoids dependence on the smaller `deltas` serialization and extends the
common audited ladder through `N=20`.

## 3. Probe audit

Companion:

```text
E78_81_weighted_safedelta_sigma_monotonicity_probe.py
E78_81_weighted_safedelta_sigma_monotonicity_results.json
```

The reconstructed rows are:

```text
N= 8:  Y(1.0)=0.320335, Y(3.0)=0.306657
N=10:  Y(1.0)=0.219772, Y(3.0)=0.212573
N=12:  Y(1.0)=0.213459, Y(3.0)=0.209721
N=14:  Y(1.0)=0.151925, Y(3.0)=0.149420
N=16:  Y(1.0)=0.161483, Y(3.0)=0.159936
N=18:  Y(1.0)=0.126929, Y(3.0)=0.125781
N=20:  Y(1.0)=0.095748, Y(3.0)=0.094885.              (WSM-5)
```

So for **every** currently available common row:

```text
Y_N(3.0) < Y_N(1.0).                                   (WSM-6)
```

Moreover the sigma ratio stays close to one:

```text
Y_N(3.0) / Y_N(1.0)
 in [0.9573, 0.9910],                                  (WSM-7)
```

and drifts upward toward `1` as `N` increases.

## 4. Consequence

This strengthens E78.80 in two ways.

First, the constant envelope extends one row further:

```text
Y_N(sigma) <= 0.321
```

now across `N=8,...,20` on the common audited sigma slices.  Second, the
audited sigma dependence has a consistent direction:

```text
the larger safe sigma slice is always smaller.         (WSM-8)
```

So the most economical next target is no longer merely

```text
CONSTANT-WEIGHTED-SAFEDELTA,                           (WSM-9)
```

but the sharpened form

```text
SIGMA-MONOTONE-WEIGHTED-SAFEDELTA:
  Y_N(sigma) decreases in sigma on the safe compact.   (WSM-10)
```

If proved, this would reduce the whole compact to its left endpoint:

```text
Y_N(sigma) <= Y_N(sigma_0^+)                            (WSM-11)
```

and the radial tail law would follow from the single worst safe slice.

## 5. Candid reading

This note does **not** prove sigma monotonicity on the full compact. The common
reconstruction still exposes only the audited slices `sigma=1.0` and `sigma=3.0`.

What it does prove is that the monotone direction survives every currently
available common row and even after extending the audit from `N=18` to `N=20`.

That makes the sigma-monotone version the right next theorem-grade target to
try before introducing any more elaborate sigma profile.

## 6. Status

```text
observed:
  after reconstructing A_N directly from the E77.5ac points table, the weighted
  normalized shell derivative satisfies Y_N(3.0) < Y_N(1.0) for every audited
  N=8,...,20;

observed:
  the constant envelope Y_N <= 0.321 remains valid on the extended common
  ladder;

clarified:
  the next candid sharpening of the radial front is the sigma-monotone target
  SIGMA-MONOTONE-WEIGHTED-SAFEDELTA;

reduced:
  CONSTANT-WEIGHTED-SAFEDELTA to a monotonicity statement in sigma on the safe
  compact.
```
