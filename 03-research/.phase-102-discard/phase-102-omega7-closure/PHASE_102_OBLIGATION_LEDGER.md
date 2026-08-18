# Phase 102 obligation ledger

## Trunk

| Point | Status | Reference |
|---|---|---|
| 1. Exact target | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 2. Paired arithmetic continuation | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 3. Integration by parts with boundary term | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/LIVE_FRONTIER_AND_RESTART_PLAN.md` |
| 4. Finite exceptional range | Closed | `RH-MASTER-CONTEXT-SNAPSHOT/fragments/OMEGA7_POINT4_FINITE_CERTIFICATE.md` |
| 5. Global signed inequality | Open | Reduced to A0 plus A1 |
| 6. Boundary limit | Reduced | `102_BOUNDARY_LIMIT_AND_LIMIT_ORDER.md` |
| 7. All `n` scales | Reduced | `102_SCALE_DECOMPOSITION_AND_TRUNCATION.md` |
| 8. Sign before estimate | Open | A1; see `102_A1_SIGNED_COMPENSATION_CANDIDATES.md` |
| 9. Arithmetic discriminant | Formulated | `102_A1_ZERO_SIDE_DISCRIMINANT.md` |
| 10. Typed off-line sensitivity | Formulated control | `102_A1_ZERO_SIDE_DISCRIMINANT.md` |
| 11. Li assembly | Conditional closed | `102_LI_ASSEMBLY_CONDITIONAL_THEOREM.md` |

## Carril A

| Point | Status | Reference |
|---|---|---|
| 12. Signed unit | Reduced | The only current unit is global; see `102_A1_SIGNED_COMPENSATION_CANDIDATES.md` |
| 13. Global compensation | Open | A1 |
| 14. Signed truncation error | Closed for the far tail | `102_A0_UNIFORM_TAIL_THEOREM.md` |
| 15. Uniformity | Reduced | Tail and boundary handled; core remains A1 |
| 16. Literal Li inequality | Open | A0 plus A1 |

## Carril B

| Point | Status | Reference |
|---|---|---|
| 17. BTG-DIV | Open | `RH-MASTER-CONTEXT-SNAPSHOT/fragments/OMEGA7_CARRIL_B_TRIAGE.md` |
| 18. LP interface | Open | Same |
| 19. GAP-Z | Open | Same |
| 20. RDI-ANCHOR/core | Open | Same |
| 21. RDP-SHELL | Open | Same |
| 22. SAFE-PROLATE-BRIDGE | Open | Same |
| 23. SAFE-LIMIT-POINT | Conditional only | Same |
| 24. SR-SAFE | Open | Same |
| 25. RDI implies Li | Minimal theorem stated | `102_RDI_TO_LI_MINIMAL_BRIDGE.md` |

## Current reduced form

Omega7 is closed if the phase proves:

[
  \lambda_n>0\qquad(1\le n\le7),
]

and

[
  \lambda_n^{prime}\ge-\lambda_n^{arch}\qquad(n\ge8).
]

The first statement is closed. A0 closes the far tail of the second statement.
The remaining live problem is A1, the signed finite core for `n>=8`.

## Current bottleneck

After the phase 102 reductions, every open obligation in the direct route is
concentrated in A1:

[
  -n+\int_1^{e^{T(n)}}(\psi(y)-y)f'_{n,0}(y)\,dy
  \ge
  -{3\over4}\lambda_n^{arch}
  \qquad(n\ge8).
]

The surviving nonlocal mechanisms are a Mellin coboundary or a bordered Euler
current that maps directly to this inequality.
