# Phase 93 - Direct bordered anchor

## 1. Objective

Determine whether fixed-`L` convergence, GAP-Z and the LP interface are
logically required once the complete denominator-free bordered determinant is
available.

## 2. Result

They are not required for the shortest sufficient route.  A direct cofinal
identification of the normalized bordered determinant with `E_L` implies the
safe ratio and hence `Omega7`.

This does not weaken the arithmetic theorem.  The direct identification is
RDI-ANCHOR on a directed family and therefore carries the full force of
`Omega7`.

## 3. Work order

```text
E93.001  direct cofinal bordered target;
E93.002  closure theorem to Omega7;
E93.003  equivalence with SR-SAFE and RDI;
E93.004  optional-infrastructure ledger;
E93.005  final allocation of proof effort.
```

## Outcome

Closed; see [`PHASE_93_CLOSURE.md`](PHASE_93_CLOSURE.md) (“Minimal direct route”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `DIRECT-BORDERED-ANCHOR`; Omega7 and RH.

## Contents

- `E93_001_DIRECT_COFINAL_TARGET.md` — E93.001 - Direct cofinal bordered target
- `E93_002_DIRECT_CLOSURE_THEOREM.md` — E93.002 - Direct closure theorem
- `E93_003_EQUIVALENCE_AUDIT.md` — E93.003 - Equivalence audit
- `E93_004_OPTIONAL_INFRASTRUCTURE_LEDGER.md` — E93.004 - Optional infrastructure ledger
- `E93_005_PROOF_EFFORT_ALLOCATION.md` — E93.005 - Proof-effort allocation
- `PHASE_93_CLOSURE.md` — Phase 93 closure - Minimal direct route

## Relation to other phases

Continues [`phase-92-cluster-adjugate-projectivization`](../phase-92-cluster-adjugate-projectivization/); its open target passes to [`phase-94-global-cofactor-cell-current`](../phase-94-global-cofactor-cell-current/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
