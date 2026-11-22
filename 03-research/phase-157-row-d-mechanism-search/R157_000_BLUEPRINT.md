# R157_000 — Blueprint, phase 157: the mechanism search under the proved filters

Decision: option **(B) continue** (`ROW-D-REDUCED-STATEMENT.md` §6). Ceiling stated in advance:
row D complete = RH; the only remaining content is uniformity in `T` (reduced statement §1).

## Admissibility filter (from the proved record; a candidate failing any item is closed without building)
F1 uses exact values of `Λ(n)` (or of the zeros), not only class properties — `cor:void`, `thm:finmod`, `cor:convfail`.
F2 is uniform in `T` with no margin (`thm:margin`, `cor:margin2`) and no upward induction (`cor:mono`, W15).
F3 does not rest on a finite truncation (`thm:arena`, `thm:finZ`), a termwise sign (`lem:Rrig`, `thm:SC`), or an identity (`thm:O`).
F4 is not a Beurling-class argument (T3, now METHOD-CONSTRAINT modulo the CITED (secondary source) import (H-DMV′)) and invokes A3 and one of A7/A8/A9 (T2, Epstein). **[amended per R157_004: the earlier clause "names a property separating ξ from all ξ_K (P47 T1)" misread T1 — P47 §18.1: the proof must be uniform in the number field; a field-uniform argument is admissible and would prove GRH for all K (Rem 18.1a); T1 excludes only derivations from properties shared by all ξ_K that stop short of GRH for all K.]**
F5 is not an `h⁰` construction in the intersection frame (P47 Thm 19.25, now on the small domain), and not a Deligne extraction (T5, T6).

## Round 1
| file | task |
|---|---|
| `R157_001_DMV_IMPORT.md` | O-150.1: state (H-DMV) exactly from the secondary sources in `00-references/beurling-dmv/`; decide whether it becomes `CITED (secondary)` and T3 (P47 Thm 2.8′) becomes unconditional at that label; check BE1–BE8 against the published construction as described there. |
| `R157_002_MECHANISM_SEARCH.md` | Enumerate every candidate mechanism in the literature and the corpus that could satisfy F1–F5 (corpus grep first); run each through the filter with citations; output the survivors (possibly none) with a one-round test for each. |
Rules: pure mathematics; scripts ≤ 60 s one at a time; audit each memo; no sign claims; state the form (primitive/complete).
