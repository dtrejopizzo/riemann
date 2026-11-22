# Coverage index and size control

## Corpus coverage

| Sector | Inventory checked | Reading evidence |
|---|---:|---|
| Paper 36 | 8,806 lines; 54,962 words | [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) and [`fragments/PAPER36_LOGIC_AUDIT.md`](fragments/PAPER36_LOGIC_AUDIT.md) |
| RH2017–RH2019 | 266 task directories | [`RH2017_RH9_AUDIT.md`](RH2017_RH9_AUDIT.md) and [`fragments/RH2017_RH3_AUDIT.md`](fragments/RH2017_RH3_AUDIT.md) |
| RH2020–RH2022 | 211 task directories | [`RH2017_RH9_AUDIT.md`](RH2017_RH9_AUDIT.md) and [`fragments/RH2020_RH6_AUDIT.md`](fragments/RH2020_RH6_AUDIT.md) |
| RH2023–RH2025 | 149 task directories | [`RH2017_RH9_AUDIT.md`](RH2017_RH9_AUDIT.md) and [`fragments/RH2023_RH9_AUDIT.md`](fragments/RH2023_RH9_AUDIT.md) |
| Phases 000–025 | All existing directories in the range | [`fragments/PHASES_000_025_AUDIT.md`](fragments/PHASES_000_025_AUDIT.md) |
| Phases 026–050 | All existing directories in the range, including both 044 branches | [`fragments/PHASES_026_050_AUDIT.md`](fragments/PHASES_026_050_AUDIT.md) |
| Phases 051–075 | All existing directories in the range | [`fragments/PHASES_051_075_AUDIT.md`](fragments/PHASES_051_075_AUDIT.md) |
| Phases 076–089 | All directories; 512 Markdown files checked | [`fragments/PHASES_076_089_AUDIT.md`](fragments/PHASES_076_089_AUDIT.md) |
| Phases 090–101 | All existing directories in the range | [`fragments/PHASES_090_101_AUDIT.md`](fragments/PHASES_090_101_AUDIT.md) |

The nine programs contain 626 `task` directories, continuous from `task1` to the maximum of each program: 89, 94, 83, 83, 60, 68, 43, 27 and 79. The phase tree contains 101 directories. Labels 001 and 002 do not exist and 044 appears in two paths; the coverage keeps these anomalies rather than inventing continuity.

A name check for files containing `CLOSURE`, `cierre` or `final` found no candidate outside the audited ranges. Binaries, images, caches and bulk outputs were not treated as proofs; they were checked when a text relied on them for a material claim.

## Map of the dossier

| Document | Role |
|---|---|
| [`README.md`](README.md) | Entry point, finding and reading order. |
| [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md) | Corpus, labels, H0 and precedence. |
| [`MASTER_CONTEXT.md`](MASTER_CONTEXT.md) | Self-contained context of the whole program. |
| [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) | Spine of Steps 1–15, H0–H8 and the Ω chain. |
| [`RH2017_RH9_AUDIT.md`](RH2017_RH9_AUDIT.md) | Synthesis of the nine programs. |
| [`PHASES_AUDIT.md`](PHASES_AUDIT.md) | Mathematical genealogy of all phases. |
| [`NO_GO_AND_RETRACTIONS.md`](NO_GO_AND_RETRACTIONS.md) | Closed classes, circularities and withdrawals. |
| [`LIVE_FRONTIER_AND_RESTART_PLAN.md`](LIVE_FRONTIER_AND_RESTART_PLAN.md) | Actual front, gates and order of work. |
| [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md) | Independent cross-cutting comparison. |
| [`fragments/COVERAGE_VALIDATION.md`](fragments/COVERAGE_VALIDATION.md) | Mechanical validation of inventory and links. |

The remaining fragments are the block audits listed in the coverage table. A discrepancy is not resolved by file name: the correction that exhibits the mathematical step and its hypotheses prevails.

## Size control

The complete dossier contains twenty Markdown files, fewer than 50,000 words and fewer than 350,000 bytes. The whole dossier can therefore be read in a single sitting.

## Integrity checks

- All existing phase directories belong to an audited range.
- All RH task directories belong to a block audit.
- The targets of local Markdown links were verified.
- Proved, conditional, numerical, refuted, open and RH-strength results were kept separate.
- The labels `QED`, `closure` or `theorem` were not accepted as evidence without auditing hypotheses and quantifiers.
- The bibliographic novelty review remains a separate gate; this index certifies internal coverage, not external priority.
