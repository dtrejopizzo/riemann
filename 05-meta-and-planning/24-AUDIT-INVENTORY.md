# Repository Audit & Reorganization Inventory

**Date:** 2026-06-26
**Scope:** Full audit of `/Users/dt/riemann` for ordering, currency, and English-only language,
plus the actions taken.

## What was found

- **Two empirical/theoretical layers** under-documented by the top-level files: Research Programs
  1–9 (`01-context/RH1…RH9`, 627 trajectories) and Program 10 (`03-research/`, **61 phases**).
- **Stale high-level docs.** `00-README.md` described a folder layout that no longer existed;
  `MASTER-PLAN.md` stopped ~P13/phase-4; `PROGRAMA-COMPLETO-*` stopped ~P30/phase-20; the
  whitepapers predated the RH1–9 + 61-phase framing.
- **Duplication.** Root `MASTER-PLAN.md` vs `riemann-program/MASTER-PLAN.md`; root
  `PROGRAMA-COMPLETO-MAPA.md` vs `riemann-program/PROGRAMA-COMPLETO-RESUMEN.md`.
- **Language.** A scan of 528 docs (excluding the RH dumps and reference PDFs) found **309 Spanish
  files**, ~10 of them front-door/navigation docs and ~300 dense internal phase notes; **26 phase
  folders** had Spanish names.

## Actions taken

| Action | Result |
|---|---|
| Renamed Spanish phase folders → English (`git mv`) | 28 folders renamed; ~15 referencing docs path-fixed; verified clean |
| Moved `meta-docs/` → `05-meta-and-planning/`; `WHITEPAPER.md` → `whitepaper/` | New layout |
| Reconciled duplicates | Single canonical `MASTER-PLAN.md` (in-folder, rewritten current); root duplicates deleted |
| Translated + updated front-door docs | `README.md`, `EXPLANATION.md`, `00-README.md`, `NO-GO-LIST.md`, `COMPLETE-PROGRAM-SUMMARY.md` (from the Spanish RESUMEN), folder READMEs — all English & current through Phase 61 |
| Extended `00-MAP.md` | Appended English continuation through Phase 61 |
| Per-phase translation | Per user decision: **summary/setup/verdict docs only** translated; granular working notes left in original Spanish as the raw record |
| Reproducibility notebook | Replaced with an honest "checks that pass" notebook |

## Deliberately left in Spanish

The ~300 granular internal phase notes inside `03-research/phase-*/` (e.g. step-by-step
derivations, audit logs). These are the raw research record; per the agreed scope, only each
phase's top-level summary/setup/verdict documents were translated. A future pass can translate the
remainder if needed.
