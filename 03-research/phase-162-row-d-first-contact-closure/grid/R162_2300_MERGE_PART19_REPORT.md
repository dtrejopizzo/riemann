# R162_2300 — Merge report for part 19 (phases 168–184)

Master grid editor. No new mathematics; record only. Row D OPEN; no statement label changed.

## Files
- Backups: `R162_2300_MASTER_GRID_pre_p184.md.bak`, `R162_2300_MASTER_grid_pre_p184.json.bak`.
- New: `R162_2300_part19.jsonl` (78 entries, part18 schema: id, name, row, col, status, killer, note, supersedes_or_dup).
- Edited: `R162_2300_MASTER_grid.json` (routes added with `source_part: 19`, `counts` recomputed, `part19_merged`, `part19_tools`, `version`; status, `live_residuals` and `editor_note` of the 8 repainted cells; other fields untouched, including `n`), `R162_2300_MASTER_GRID.md` (§1, count, §2, §3, §4, §5, §6 item 59, §8 entry 19).
- Sources: INVENTORY-PHASES-168-184, R162_2300_REPAINT_PROPOSAL, R184_002 (subroutes of phase 170).

## Part 19 by phase
R168 ×8 · R169 ×4 · R170 ×12 (consolidated per the table in R184_002 §1, plus R170-RES) · R171 ×2 · R172 ×2 · R173–R175 ×6 · R176–R182 ×9 · R183 ×11 · R184 ×18 · SIGN-REAUDIT/SUPPORT-DESCENT ×3 · proposal closures ×3 (R184_C6C, R184_C7F, R184_C7H).
Statuses used (existing vocabulary): DEAD 47 · PROVED-TOOL 14 · OPEN 11 · NO-GO 6. Global totals by status after the merge: DEAD 716 · PROVED-TOOL 149 · PARTIAL 114 · OPEN 105 · NO-GO 15 · PROVED 1.

## Count
- Before: ■ 11 · ◩ 19 · ◧ 34 · □ 0; 1022 routes.
- After: **■ 13 · ◩ 23 · ◧ 28 · □ 0; 1100 routes**.
- Cells changed (proposal, cited proof): 2A, 6C ◩→■; 2G, 4D, 7A, 7B, 7F, 7H ◧→◩. No change by proposal decision: 1E, 2E, 6B, 6G, 8D.

## Editor's decisions
- Old OPEN/PARTIAL routes of the repainted cells keep their status (precedent: 6C and 2A were already ◩ with OPEN/PARTIAL routes); the death is recorded in the new entries and in `editor_note`.
- New OPEN entries were placed in cells that remain ◧ (7D, 5E, 6B, 2H, 5H, 8H, 8D, 5G, 4E, 4C) so as not to contradict the repainted cells; R178_O (anti-ρ_−) goes to 4C, not 2C.
- Several results touch several cells; one entry was recorded in the inventory's main cell and the others are named in `note`.

## Checks (python)
Valid JSON; Σ counts per cell = number of routes per cell; total 1100; the 64 symbols and numbers of §1 match the JSON.

## Not placed
Nothing was left without a cell. The ~150 PROVED statements of the inventory are grouped by file (not one per statement); the 130 files of phase 170 go in 12 consolidated entries.
