# Phase 98 - Sensitivity shell split

## 1. Objective

Separate exactly the Fourier-compression contribution in the Euler
sensitivity commutator, without estimating the shell before the safe pairing.

## 2. Main identity

For a Fourier projection `P_N`, its complement `Q_N` and a lifted finite
sensitivity `K_N=P_NK_NP_N`,

```text
[Z,K_N]
 =[P_NZP_N,K_N]
  +Q_NZP_NK_N-K_NP_NZQ_N.                            (2.1)
```

The first term is internal.  The last two are the exact outgoing and incoming
Fourier shell crossings.

## 3. Work order

```text
E98.001  finite-rank physical lift;
E98.002  exact shell commutator split;
E98.003  internal adjugate reduction;
E98.004  bilateral current decomposition;
E98.005  corrected direct boundary target.
```

## Outcome

Closed; see [`PHASE_98_CLOSURE.md`](PHASE_98_CLOSURE.md) (“Compression defect made exact”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `SENSITIVITY-BOUNDARY-SHELL`; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E98_001_FINITE_RANK_PHYSICAL_LIFT.md` — E98.001 - Finite-rank physical lift
- `E98_002_EXACT_SHELL_SPLIT.md` — E98.002 - Exact Euler commutator shell split
- `E98_003_INTERNAL_ADJUGATE_REDUCTION.md` — E98.003 - Internal adjugate reduction
- `E98_004_BILATERAL_CURRENT_DECOMPOSITION.md` — E98.004 - Bilateral current decomposition
- `E98_005_CORRECTED_BOUNDARY_TARGET.md` — E98.005 - Corrected direct boundary target
- `PHASE_98_CLOSURE.md` — Phase 98 closure - Compression defect made exact

## Relation to other phases

Continues [`phase-97-euler-sensitivity-commutator`](../phase-97-euler-sensitivity-commutator/); its open target passes to [`phase-99-adjugate-boundary-sandwich`](../phase-99-adjugate-boundary-sandwich/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
