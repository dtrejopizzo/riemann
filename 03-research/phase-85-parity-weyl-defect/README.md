# Phase 85 - Parity Weyl defect

## 1. Objective

Resolve the safe reduced response left by Phase 84 without replacing it by an
ambient inverse estimate.

The exact target is

```text
COFINAL-PARITY-CLUSTER:
choose a cofinal parity-balanced spectral cluster for which the two safe
parity responses of C^(-1)QD Mg vanish locally uniformly, together with one
safe derivative.                                      (1.1)
```

## 2. Strategy

The rank-two displacement equation determines every matrix element of `D`
between eigenvectors of opposite parity.  This converts the reduced response
into two normalized finite Weyl defects.  No eigenvector matrix element of
`D` remains unknown.

## 3. Work order

```text
E85.001  exact spectral-ratio formula.
E85.002  normalized Weyl-defect form.
E85.003  separation of the two defects on the safe axis.
E85.004  cofinal cluster criteria and obstruction audit.
```

## Outcome

Closed; see [`PHASE_85_CLOSURE.md`](PHASE_85_CLOSURE.md) (“two parity Weyl defects”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: signed Abel cancellation in each parity sector; cofinal cluster schedule compatible with that cancellation; the outer arithmetic anchor and Omega7.

## Contents

- `E85_001_SPECTRAL_RATIO_FORMULA.md` — E85.001 - Exact spectral-ratio formula
- `E85_002_NORMALIZED_WEYL_DEFECT.md` — E85.002 - Normalized Weyl-defect form
- `E85_003_SAFE_AXIS_SEPARATION.md` — E85.003 - Separation of parity responses on the safe axis
- `E85_004_MOVING_POLE_CRITERION.md` — E85.004 - Moving-pole criterion and quadratic separation
- `E85_005_PATH_DECISION.md` — E85.005 - Path decision from moving poles to signed complement sums
- `PHASE_85_CLOSURE.md` — Phase 85 closure - two parity Weyl defects

## Relation to other phases

Continues [`phase-84-distributional-endpoint-module`](../phase-84-distributional-endpoint-module/); its open target passes to [`phase-86-signed-spectral-abel`](../phase-86-signed-spectral-abel/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
