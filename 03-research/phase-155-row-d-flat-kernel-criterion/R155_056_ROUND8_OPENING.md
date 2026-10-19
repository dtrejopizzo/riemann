# R155_056 — Opening, round 8

Decision: advance PATH-TO-D (`R155_031`), close P6 and P7, prove and complete.
This opening states the ceiling in advance, to avoid overclaiming: **row D complete = RH** (Paper 47 §9.1
reduction chain; every link an equivalence). What this round can prove are (i) the exact negative index of the
archimedean form (P3 sharpened by the multi-band relaxation left open in `rem:P4`), (ii) the exact arithmetic
content per window (P6, expected outcome: an equivalence, not a proof), (iii) the D-HS kill (P7, hygiene),
(iv) an unconditional decay bound for the margin `λ^P(T)` (new item P9), which decides whether any
uniform-margin argument can exist.

Memos (parallel, files of record):
| round | file | task |
|---|---|---|
| 8a | `R155_052_ROUND8A_INDEX_MULTIBAND.md` | exact `n₋(A_∞|P_T)`: multi-band Ky Fan ceiling + certified negative Gram floor |
| 8b | `R155_053_ROUND8B_P6_ALIGNMENT.md` | P6: theorem `X_T`, per-window finiteness, conditional reduction, the negative on unconditional prime-side inputs |
| 8c | `R155_054_ROUND8C_P7_DHS_KILL.md` | P7: D-HS against the frame-defect theorem 19.25 / 21.15; T1, T2, T5 |
| 8d | `R155_055_ROUND8D_MARGIN_DECAY.md` | P9: unconditional explicit upper bound `λ^P(T) → 0`; consequence for uniform-margin arguments |

Rules unchanged: pure mathematics; scripts ≤ 60 s; corpus grep before novelty; audit per memo;
integration into Paper 47 only after audit and check against the paper's own definitions
(`feedback-check-against-paper-definitions`). No sign for ζ beyond `T ≤ log 2`; no statements about zeros.
