# Phase 80 - Relative determinant identification

## 1. Objective

The phase isolates and attacks the arithmetic identification needed by the
finite real-rooted CCM route to `Omega7`.

The inherited chain is

```text
LP + IDENT + RDP-SHELL + (PROLATE + WEIL-TAIL)
  => SAFE-LIMIT-POINT => SAFE-PROLATE-BRIDGE => SR-SAFE
  => Omega7.
```

The primary object of this phase is the two-scale identification inside
`IDENT`: first finite-section convergence at fixed `L`, then arithmetic
identification as `L->infinity`.  It is written as a relative determinant
theorem, with the finite CCM characteristic and the finite Euler--Gamma product
constructed independently.

## 2. Binding rules

Every claimed closure must contain:

```text
1. an exact statement with all quantifiers;
2. a proof from previously proved statements, or a named hypothesis;
3. an explicit dependency list;
4. a status block separating proved, reduced, refuted and open assertions;
5. a falsification condition whenever the statement is not purely formal.
```

The following mechanisms are excluded:

```text
- zero locations as input;
- positivity as the forcing step;
- absolute summation of prime or spectral shells before cancellation;
- inversion at an unknown limiting eigenvalue;
- identification of an arithmetic limit from a scalar signature alone;
- fitted finite-section constants used as asymptotic theorems.
```

## 3. Exact work order

```text
E80.001  phase contract and dependency cut.
E80.002  independent finite Euler--Gamma product.
E80.003  bilateral relative determinant and equivalence theorem.
E80.004  coherence insufficiency theorem.
E80.005  arithmetic cocycle target for the remaining signed cancellation.
E80.006  GAP-Z minimal-convergence audit.
E80.007  mu-free disk-intersection decision.
E80.008  downstream radical-tail cut audit.
E80.009  minimal LP boundary-trace cut.
```

Later numbering is determined only by mathematical dependencies.

## 4. Initial ledger

```text
closed exactly in this phase:
  independent Euler--Gamma primitive and its outer limit;
  equivalence of projective flatness, derivative identification and normalized
  relative-determinant convergence;
  coherence plus convergence is insufficient to identify the arithmetic limit;
  HPR-DIV is an exact cell coordinate identity, not an established RDI bridge;
  GAP-Z is sufficient but is not the minimal convergence hypothesis;
  the mu-free disk route cannot bypass dimension-one and normalization
  nonvanishing for the original full-solution endpoint;
  the radical-tail front reduces to RDP-SHELL plus directional continuity on
  the actual PROLATE and WEIL residual subspaces;
  the LP front reduces to BTG-DIV plus mu-free completeness; the Feshbach
  envelope is an optional route inside BTG-DIV, not a third final obligation;

first formal closures sought:
  independent Euler--Gamma primitive;
  exact equivalence between relative projective flatness and the two-scale
  logarithmic-derivative identification;
  theorem that spectral coherence alone cannot identify the arithmetic limit;

load-bearing open theorem:
  relative determinant identification for the zeta CCM sections;

separate technical fronts:
  MIN-CONV, through GAP-Z or VITALI-Z;
  BTG-DIV and mu-free LP interface clauses MF-1--MF-6;
  RDP-SHELL;
  DIRECTIONAL-TAIL-CONTINUITY for PROLATE and WEIL-TAIL;
  SAFE-PROLATE-BRIDGE.
```

## Outcome

Closed at reduction grade; see [`PHASE_80_CLOSURE.md`](PHASE_80_CLOSURE.md) (“Corrected minimal cut to Omega7”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: A1--D3 in (3.1).

## Contents

- `E80_001_PHASE_CONTRACT.md` — E80.001 - Phase contract and dependency cut
- `E80_002_INDEPENDENT_EULER_GAMMA_PRODUCT.md` — E80.002 - Independent finite Euler--Gamma product
- `E80_003_BILATERAL_RDI_EQUIVALENCE.md` — E80.003 - Bilateral relative determinant equivalence
- `E80_004_COHERENCE_INSUFFICIENCY.md` — E80.004 - Coherence and summability do not identify the limit
- `E80_005_HPR_AND_THE_ARITHMETIC_COCYCLE.md` — E80.005 - HPR compression and the arithmetic cocycle
- `E80_006_GAP_Z_MINIMAL_CONVERGENCE.md` — E80.006 - Minimal convergence requirements behind GAP-Z
- `E80_007_MU_FREE_DISK_INTERSECTION_DECISION.md` — E80.007 - Decision of the mu-free disk-intersection alternative
- `E80_008_RADICAL_TAIL_CUT_AUDIT.md` — E80.008 - Radical-tail cut audit
- `E80_009_LP_BTG_MINIMALITY.md` — E80.009 - Minimal LP boundary-trace cut
- `PHASE_80_CLOSURE.md` — Phase 80 closure - Corrected minimal cut to Omega7

## Relation to other phases

Continues [`phase-79-shared-convergence-and-ident-discriminant`](../phase-79-shared-convergence-and-ident-discriminant/); its open target passes to [`phase-81-secular-arithmetic-anchor`](../phase-81-secular-arithmetic-anchor/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
