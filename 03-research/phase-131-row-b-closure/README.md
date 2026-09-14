# Phase 131 — row B closure (builder/auditor loop)

Opened 2026-09-12 after row A's closure (phase 130). Closed 2026-09-12 with
R131.019. Builder: Claude Opus 5 (rounds 1–7). Hostile auditor: Claude Opus 5
(five audits). Lead and audit of record: Claude Fable 5.1.

| file | content |
|---|---|
| R131_000 | lead blueprint round 1: the arithmetic object is the unit-averaged (norm) class |
| R131_001 | builder round 1: §3bis of Paper 44 |
| R131_002 | hostile audit round 1 (13 findings; the class forgets factorization) |
| R131_003 | lead audit round 1 |
| R131_004 | builder round 2: `Γ_n^rad` renamed norm class; Thm 3bis.7′ contact locus |
| R131_005 | lead conditional decision (label conditional on the B.4 amendment; rulings on B.7 and the P123.038 §5 arrow) |
| R131_006 | lead blueprint round 3: Frobenius family, integral shadow, Weil interface |
| R131_007 | builder round 3: §3ter, §6bis, §8bis |
| R131_008 | hostile audit round 3: FATAL F1 — the Frobenius Gram form is only the finite half of the Weil kernel |
| R131_009 | lead audit round 3 (L1–L4) |
| R131_010 | builder round 4: two Gram forms (Thm 8bis.1e: Weil kernel = Gram form of `Frob⋆Δ^rad`), diagonal computed, Thm 8bis.8 |
| R131_011 | hostile audit round 4 (M1–M6; label EARNED conditional) |
| R131_012 | lead audit round 4 (LF1–LF4) |
| R131_013 | builder round 5: conventions (C1),(C2); Thm 8bis.4a; partition-of-unity lemma |
| R131_014 | hostile audit round 5 (N1–N5) |
| R131_015 | lead audit round 5 (LF5: the import (Wgr) is false; LF6) |
| R131_016 | builder round 6: Lemma 8bis.6b refutes (Wgr); Thm 8bis.7 made conditional under `(H_L)`; Lemma 8bis.6a |
| R131_017 | hostile audit round 6 (A1–A5, p1–p9; label EARNED conditional on apparatus) |
| R131_018 | builder round 7: apparatus, grep-verified |
| R131_019 | **lead final audit and closure decision** |
| scripts/ | `verify_131_contacts.py` (rounds 1–6 blocks; all pass) |

Outcome:

    ROW B: WEIL-STRENGTH-COMPLETE on Paper 43's declared carrier, as a theorem
    about row A's declared trace; B.4 amended (owner-accepted 2026-09-12);
    B.7 by lead ruling with the auditor's dissent recorded. No sign, no zeros;
    interface with Weil's criterion is a colimit statement; (Wgr) withdrawn as
    false; "positivity on Dirichlet profiles ⟹ RH" OPEN.

Handed to row C (Paper 45): Paper 44 **§9.1** (the prime packet, content
Thm 3bis.7; **[phase 133, PANEL_2 MINOR-4: this line read "Paper 44 Thm 9.1",
which does not exist]**), the withdrawal of the `n−1`
obligation (Paper 45 §11 must be corrected), Paper 43 Thm 10.8b, the two-slice
theorem, Thm 8bis.1e, convention (C1).
