# E78.31 - Raw geometric envelope for `Delta safe_u`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.30 reduced the sign-side target to the raw ratio

```text
RAW-DELTA-RATIO_N
 := Delta safe_u_{N+2} / Delta safe_u_N.                  (DG-1)
```

This note records the strongest natural form of that reduction:

```text
DELTA-SAFEU-GEOMETRIC-ENVELOPE:
  0 < Delta safe_u_{N+2} <= eta_* Delta safe_u_N
  for some eta_* < 1.                                     (DG-2)
```

## 2. Exact implication

If `(DG-2)` holds, then multiplying by the harmless weight `(N+2)/N` gives

```text
rho_N
 = ((N+2)/N) * (Delta safe_u_{N+2}/Delta safe_u_N)
 <= ((N+2)/N) eta_*.                                      (DG-3)
```

So any theorem-grade control of `(DG-2)` immediately feeds the weighted target.

In particular, if the bound is available cofinally and `eta_*` stays strictly
below `N/(N+2)` on that branch, then

```text
DELTA-SAFEU-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-TAIL.                                 (DG-4)
```

Even without a sharp closed-form `eta_*`, `(DG-2)` is the most primitive
geometric envelope presently visible.

## 3. Probe audit

Companion:

```text
E78_31_delta_safeu_geometric_probe.py
E78_31_delta_safeu_geometric_results.json
```

### Zeta

On the audited `sigma in {1,3}` ladder:

```text
positive-geometric-envelope count = 12
fails                           = 0
observed eta_*                  = 0.8210067653381925.     (DG-5)
```

The raw ratios are:

```text
sigma=1.0:
  0.64719, 0.68161, 0.73543, 0.74234, 0.78295, 0.81962

sigma=3.0:
  0.65612, 0.68665, 0.73899, 0.74457, 0.78470, 0.82101.  (DG-6)
```

So the audited zeta rows already satisfy a clean positive geometric envelope
for `Delta safe_u` itself.

### Planted build

The planted build fails the raw geometric envelope:

```text
positive-geometric-envelope count = 6
fails                           = 6.                      (DG-7)
```

The failure is immediate at the raw-ratio level, via sign changes:

```text
sigma=1.0:
  ..., 0.03598, -0.58779, 0.45706, -0.40695, -0.68877

sigma=3.0:
  ..., 0.21511, -0.11996, 0.53670, -3.25725, -0.21086.   (DG-8)
```

So the plant is ruled out before the mild weight `(N+2)/N` even enters.

## 4. Consequence

This is now the most elementary current sign-side target:

```text
prove a positive geometric envelope directly for Delta safe_u. (DG-9)
```

That is strictly more primitive than the weighted envelope for `A_N`, and thus
the natural place to search for a theorem-grade shell-update mechanism.

## 5. Candid reading

This note does **not** prove that a uniform `eta_*` exists on the full cofinal
path.  It only shows that the audited zeta rows already sit in such a regime,
with a visible candidate constant around `0.8211`, while the planted build
fails by raw sign changes.

That is a worthwhile reduction because it moves the target to the simplest
sequence in play:

```text
Delta safe_u_N itself.                                    (DG-10)
```

## 6. Status

```text
proved:
  DELTA-SAFEU-GEOMETRIC-ENVELOPE is the primitive geometric form behind the
  weighted safe-u envelope;

observed:
  the audited zeta rows satisfy 0 < Delta safe_u_{N+2} <= 0.82101 Delta safe_u_N;

observed:
  the planted build fails the raw geometric envelope by sign changes and large
  negative ratios;

reduced:
  the sign-side target from SAFE-U-GEOMETRIC-ENVELOPE to
  DELTA-SAFEU-GEOMETRIC-ENVELOPE;

next:
  derive the raw geometric envelope for Delta safe_u from the exact u-sector
  and shell-update formulas.
```
