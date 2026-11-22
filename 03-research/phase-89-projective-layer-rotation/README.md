# Phase 89 - Projective layer rotation

## 1. Objective

Determine which part of the nested endpoint layer survives after the
projective normalization required by RDI.

## 2. Main observation

The dominant resonant contribution has the form

```text
G_t(z)
 =-[h_(t,z)^eff p_t][p_t^T b_t^eff]/lambda_t
  +remainder.                                         (2.1)
```

The eigenvalue and boundary overlap are independent of `z`.  They disappear
from normalized safe ratios.  Only the lifted Cauchy profile
`h_z tilde p_t=h_(t,z)^eff p_t` can carry a nontrivial layer current.

## 3. Work order

```text
E89.001  projective dominance theorem.
E89.002  cancellation of scalar resonance factors.
E89.003  exact profile-rotation current.
E89.004  endpoint dominance audit and final layer target.
E89.005  exact crosswalk from the layer profile to LP and IDENT.
```

## 4. Phase result

The eigenvalue cascade is normalization data.  After projective
normalization, the surviving endpoint object is exactly the safe Cauchy
profile already present in LP and IDENT.  The next phase expands its
base-point-subtracted Kato current in the prime-shift algebra.

## Outcome

Closed; see [`PHASE_89_CLOSURE.md`](PHASE_89_CLOSURE.md) (“Projective endpoint localization”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `DOM-E`; matched-width existence; Euler identification of the projective Kato current; RDI-ANCHOR and Omega7.

## Contents

- `E89_001_PROJECTIVE_DOMINANCE.md` — E89.001 - Projective dominance of one resonant parity
- `E89_002_SCALAR_FACTOR_CANCELLATION.md` — E89.002 - Cancellation of scalar resonance factors
- `E89_003_PROFILE_ROTATION_CURRENT.md` — E89.003 - Exact profile-rotation current
- `E89_004_DOMINANCE_AUDIT.md` — E89.004 - Endpoint dominance audit
- `E89_005_CROSSWALK_TO_LP_IDENT.md` — E89.005 - Exact crosswalk to LP and IDENT
- `PHASE_89_CLOSURE.md` — Phase 89 closure - Projective endpoint localization

## Relation to other phases

Continues [`phase-88-endpoint-layer-pencil`](../phase-88-endpoint-layer-pencil/); its open target passes to [`phase-90-projective-kato-euler-current`](../phase-90-projective-kato-euler-current/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
