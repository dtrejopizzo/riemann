# Phase 91 - Kato--coboundary equivalence

## 1. Objective

Determine whether the prime-driven projective current of Phase 90 can be
integrated directly by the Euler gauge, or whether doing so is exactly the
inverse-free coboundary problem already isolated in the continuum route.

## 2. Result

The derivative of the resonant line solves a reduced equation

```text
C_t dot v_t=Q_t H_P^in v_t.                           (2.1)
```

An inverse-free formula for `dot v_t` is equivalent to an explicit
coboundary decomposition of the right side.  The Euler gauge supplies a
candidate only with an additional derivation defect, which vanishes on the
endpoint distribution but not on a nonzero physical spectral vector.

## 3. Work order

```text
E91.001  exact line-response equation;
E91.002  equivalence with an inverse-free coboundary;
E91.003  Euler gauge derivation defect;
E91.004  no-bypass theorem and minimal remaining target.
```

## Outcome

Closed; see [`PHASE_91_CLOSURE.md`](PHASE_91_CLOSURE.md) (“Coboundary localization of the line current”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: LINE-EULER-COBOUNDARY reduced leakage; `PROJECTIVE-KATO-EULER`; RDI-ANCHOR and Omega7.

## Contents

- `E91_001_LINE_RESPONSE_EQUATION.md` — E91.001 - Exact line-response equation
- `E91_002_INVERSE_FREE_EQUIVALENCE.md` — E91.002 - Inverse-free coboundary equivalence
- `E91_003_EULER_DERIVATION_DEFECT.md` — E91.003 - Euler gauge derivation defect
- `E91_004_NO_BYPASS_THEOREM.md` — E91.004 - No-bypass theorem for the Kato current
- `PHASE_91_CLOSURE.md` — Phase 91 closure - Coboundary localization of the line current

## Relation to other phases

Continues [`phase-90-projective-kato-euler-current`](../phase-90-projective-kato-euler-current/); its open target passes to [`phase-92-cluster-adjugate-projectivization`](../phase-92-cluster-adjugate-projectivization/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
