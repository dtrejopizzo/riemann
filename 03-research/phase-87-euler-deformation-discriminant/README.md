# Phase 87 - Euler deformation discriminant

## 1. Objective

Replace the false implication

```text
spectral single-signedness => arithmetic identification                (1.1)
```

by an exact deformation identity for the relative bordered determinant.

## 2. Deformation

Scale the complete prime current by `t in [0,1]`:

```text
H_t=H_A-t H_P.                                         (2.1)
```

The endpoints are the archimedean build and the full arithmetic build.  The
independent Euler--Gamma product is deformed by the same parameter.

## 3. Load-bearing target

```text
TANGENT-ANOMALY:
the t-integral of the difference between the bordered determinant current and
the independent Euler current is projectively flat in the outer limit.    (3.1)
```

The bordered current is computed through the exact tangent source
`dot b_t-dot M_t x_t`; it is not replaced by a spectral trace of `H_t`.

## 4. Work order

```text
E87.001  correction of the sign-coherence discriminant.
E87.002  exact Euler semigroup deformation.
E87.003  exact bordered tangent anomaly.
E87.004  endpoint boundary-layer split.
E87.005  archimedean-base autopsy and combined anomaly.
```

## Outcome

Closed; see [`PHASE_87_CLOSURE.md`](PHASE_87_CLOSURE.md) (“corrected arithmetic discriminant”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: effective endpoint-layer pencil; signed base-layer cancellation; RDI-ANCHOR and Omega7.

## Contents

- `E87_001_DISCRIMINANT_CORRECTION.md` — E87.001 - Correction of the sign-coherence discriminant
- `E87_002_EULER_SEMIGROUP_DEFORMATION.md` — E87.002 - Exact Euler semigroup deformation
- `E87_003_BORDERED_TANGENT_ANOMALY.md` — E87.003 - Exact bordered tangent anomaly
- `E87_004_ENDPOINT_BOUNDARY_LAYER.md` — E87.004 - Endpoint boundary layer in the arithmetic deformation
- `E87_005_ARCH_BASE_AUTOPSY.md` — E87.005 - Archimedean-base autopsy and combined anomaly
- `PHASE_87_CLOSURE.md` — Phase 87 closure - corrected arithmetic discriminant

## Relation to other phases

Continues [`phase-86-signed-spectral-abel`](../phase-86-signed-spectral-abel/); its open target passes to [`phase-88-endpoint-layer-pencil`](../phase-88-endpoint-layer-pencil/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
