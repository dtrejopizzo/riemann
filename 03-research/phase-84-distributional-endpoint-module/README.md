# Phase 84 - Distributional endpoint module

## 1. Objective

Replace the impossible nonzero `L^2` ground vector of Phase 83 by the canonical
endpoint distribution `delta_0`, and determine whether its finite Fourier
images recover the exact coupled source

```text
f_N=alpha_b s_N+beta_b 1                              (1.1)
```

before any complement inverse is applied.

## 2. Load-bearing target

```text
ENDPOINT-SOURCE-IDENTITY:
the full Gamma--Euler distribution generated from delta_0, after the exact
boundary operation and finite Fourier projection, equals the source (1.1)
with every renormalization and shell term displayed.                  (2.1)
```

If (2.1) holds, the remaining estimate is the safe scalar response to its
explicit boundary defect.  If it fails, the Gamma--Euler coboundary branch is
closed without returning to an abstract unspecified model vector.

## 3. Restrictions

```text
- distributions are used only through explicit actions and Fourier pairings;
- no ambient distribution norm is substituted for the safe topology;
- the source coefficients alpha_b and beta_b remain coupled;
- the finite Fourier shell is retained;
- no inverse of the CCM complement is used to define the endpoint current.
```

## 4. Work order

```text
E84.001  exact endpoint Euler orbit and Fourier symbols.
E84.002  distributional representation of the full Weil symbols.
E84.003  rank-two source coboundary.
E84.004  spectral-cluster moment selection.
E84.005  parity split and cofinal-rank obstruction.
```

## Outcome

Closed at exact-construction grade; see [`PHASE_84_CLOSURE.md`](PHASE_84_CLOSURE.md) (“endpoint source and inverse-free corrector”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: cofinal cluster-rank selection; safe reduced response; outer arithmetic identification; `Omega7`.

## Contents

- `E84_001_ENDPOINT_EULER_ORBIT.md` — E84.001 - Endpoint Euler orbit and Fourier symbols
- `E84_002_FULL_WEIL_DISTRIBUTION.md` — E84.002 - Full Weil sine distribution
- `E84_003_RANK_TWO_SOURCE_COBBOUNDARY.md` — E84.003 - Rank-two source coboundary
- `E84_004_CLUSTER_MOMENT_SELECTION.md` — E84.004 - Cluster moment selection
- `E84_005_PARITY_MOMENT_SPLIT.md` — E84.005 - Parity split of the moment problem
- `PHASE_84_CLOSURE.md` — Phase 84 closure - endpoint source and inverse-free corrector

## Relation to other phases

Continues [`phase-83-gamma-euler-coboundary`](../phase-83-gamma-euler-coboundary/); its open target passes to [`phase-85-parity-weyl-defect`](../phase-85-parity-weyl-defect/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
