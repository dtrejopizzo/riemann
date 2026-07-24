# E78.4b - Neutral-ground-Cauchy audit

**Run:** 2026-07-18.
**Target:** the build-neutral remnant named in E78.1 section 7,

```text
NEUTRAL-GROUND-CAUCHY:
  for the finite sections, the safe Cauchy row r(z0) does not annihilate the
  lowest-mode subspace, with a lower bound uniform in N and using no
  build-discriminating gap.
```

## 1. Purpose

E77.7ag already showed that on the zeta ladder the anchor factor

```text
r(z0) v0
```

stays macroscopic while the inner almost-zero mode deepens.  After the Phase-78
correction, what matters is whether this remains true **build-neutrally** and
therefore survives as an admissible LP-interface remnant.

This note extends the same audit to the planted build.

## 2. Probe

Companion:

```text
E78_4a_neutral_ground_cauchy_probe.py
E78_4a_neutral_ground_cauchy_results.json
```

The probe uses the same finite-section inner block as E77.7ag:

```text
A = H_inner - mu I,
```

where `mu` is the section spectral point from `right_transfer_data`, and
computes for each section:

```text
1. the smallest inner eigenvalue by absolute value, |lambda0(A)|;
2. the safe Cauchy anchor |r(z0)v0| at z0 = i.
```

The two builds tested are the zeta build and the standard planted falsifier

```text
("14.134725141734693790", "0.30", "5.0").
```

## 3. Zeta

The zeta side reproduces and extends E77.7ag:

```text
N= 6  |lam0| = 7.38e-21   |r(z0)v0| = 0.3976
N=10  |lam0| = 1.84e-30   |r(z0)v0| = 0.3538
N=14  |lam0| = 2.25e-39   |r(z0)v0| = 0.3332
N=16  |lam0| = 1.56e-43   |r(z0)v0| = 0.3266
```

So the zeta anchor remains order one while the inner mode collapses by over
twenty orders of magnitude.

## 4. Planted build

On the planted build the same anchor also stays macroscopic:

```text
N= 6  |lam0| = 8.19e-2    |r(z0)v0| = 0.4402
N= 7  |lam0| = 2.91e-1    |r(z0)v0| = 0.1245
N=10  |lam0| = 1.47e-1    |r(z0)v0| = 0.1714
N=12  |lam0| = 9.62e-3    |r(z0)v0| = 0.1740
N=14  |lam0| = 7.08e-4    |r(z0)v0| = 0.1773
N=16  |lam0| = 4.49e-3    |r(z0)v0| = 0.1796
```

The absolute size fluctuates, but it never approaches the small-defect regime.
Across the tested ladder it stays between about `0.12` and `0.44`.

## 5. Reading

This is the build-neutral counterpart of E77.7ag's conclusion:

```text
the safe Cauchy anchor is not the active obstruction.
```

More precisely:

1. zeta anchor nonvanishing is not a special arithmetic feature;
2. the planted build also shows robust anchor coupling;
3. therefore any LP-interface obstruction cannot honestly be located in
   `r(z0)v0 -> 0`.

This is exactly the kind of remnant Phase 78 asked for: gauge-free, mu-free in
spirit, and not driven by the zeta/plant discriminant.

## 6. What this does and does not prove

This audit does **not** yet prove the full E78.1 remnant theorem.  It still
works sectionwise with the distinguished lowest inner mode `v0`, and does not
by itself provide:

```text
- a theorem-grade uniform lower bound in N;
- a formulation using the whole lowest-mode subspace when multiplicity is not
  assumed away a priori;
- the final assembly with E77.7aj into SAFE-DISK-IDENT.
```

But it does support the exact reduction:

```text
NEUTRAL-GROUND-CAUCHY
=> anchor factor nonvanishing
   + source-side / subspace-side work.
```

and it strongly suggests the live difficulty lies on the source/subspace side,
not on the Cauchy anchor side.

## 7. Consequence

The admissible interface remnant can now be sharpened:

```text
ANCHOR-NEUTRALITY:
  the safe Cauchy row sees the lowest inner mode in both builds; any remaining
  build-neutral interface theorem must therefore work on the source/subspace
  factor rather than on anchor nonvanishing.
```

This is not yet the final theorem, but it is a genuine reduction of the
remaining uncertainty inside `NEUTRAL-GROUND-CAUCHY`.

## 8. Status

```text
observed:
  |r(z0)v0| stays order one on the zeta ladder and also stays macroscopic on
  the planted build through N=16;

clarified:
  anchor nonvanishing is build-neutral and not the active obstruction;

reduced:
  NEUTRAL-GROUND-CAUCHY -> ANCHOR-NEUTRALITY + source/subspace-side work;

live:
  formulate the source/subspace-side remnant build-neutrally and assemble it
  with E77.7aj's separation of safe Cauchy rows.
```
