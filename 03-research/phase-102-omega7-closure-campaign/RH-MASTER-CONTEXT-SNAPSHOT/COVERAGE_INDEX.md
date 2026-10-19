# Coverage index and size control

## Corpus coverage

| Sector | Inventory cross-checked | Reading evidence |
|---|---:|---|
| Paper 36 | 8,806 lines; 54,962 words | [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) and [`fragments/PAPER36_LOGIC_AUDIT.md`](fragments/PAPER36_LOGIC_AUDIT.md) |
| RH1–RH3 | 266 task directories | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) and [`fragments/RH1_RH3_AUDIT.md`](fragments/RH1_RH3_AUDIT.md) |
| RH4–RH6 | 211 task directories | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) and [`fragments/RH4_RH6_AUDIT.md`](fragments/RH4_RH6_AUDIT.md) |
| RH7–RH9 | 149 task directories | [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) and [`fragments/RH7_RH9_AUDIT.md`](fragments/RH7_RH9_AUDIT.md) |
| Phases 000–025 | All existing directories in the interval | [`fragments/PHASES_000_025_AUDIT.md`](fragments/PHASES_000_025_AUDIT.md) |
| Phases 026–050 | All existing directories in the interval, including the two 044 branches | [`fragments/PHASES_026_050_AUDIT.md`](fragments/PHASES_026_050_AUDIT.md) |
| Phases 051–075 | All existing directories in the interval | [`fragments/PHASES_051_075_AUDIT.md`](fragments/PHASES_051_075_AUDIT.md) |
| Phases 076–089 | All directories; 512 Markdown cross-checked | [`fragments/PHASES_076_089_AUDIT.md`](fragments/PHASES_076_089_AUDIT.md) |
| Phases 090–101 | All existing directories in the interval | [`fragments/PHASES_090_101_AUDIT.md`](fragments/PHASES_090_101_AUDIT.md) |

The nine programs contain 626 `task` directories, continuous from `task1` to each program's maximum: 89, 94, 83, 83, 60, 68, 43, 27 and 79. The phase tree contains 101 directories. Labels 001 and 002 do not exist and 044 appears in two paths; coverage preserves those anomalies instead of inventing continuity.

The nominal check for files with `CLOSURE`, `cierre` or `final` found no candidate outside the audited intervals. Binaries, images, caches and bulk outputs were not treated as proofs; they were cross-checked when a text relied on them for a material claim.

## Dossier map

| Document | Function |
|---|---|
| [`README.md`](README.md) | Entry point, verdict and reading order. |
| [`00_SCOPE_AND_METHOD.md`](00_SCOPE_AND_METHOD.md) | Corpus, labels, H0 and precedence. |
| [`MASTER_CONTEXT.md`](MASTER_CONTEXT.md) | Self-contained context of the full program. |
| [`PAPER36_AUDIT.md`](PAPER36_AUDIT.md) | Step 1–15 column, H0–H8 and chain Ω. |
| [`RH1_RH9_AUDIT.md`](RH1_RH9_AUDIT.md) | Synthesis of the nine programs. |
| [`PHASES_AUDIT.md`](PHASES_AUDIT.md) | Mathematical genealogy of all phases. |
| [`NO_GO_AND_RETRACTIONS.md`](NO_GO_AND_RETRACTIONS.md) | Closed classes, circularities and retractions. |
| [`LIVE_FRONTIER_AND_RESTART_PLAN.md`](LIVE_FRONTIER_AND_RESTART_PLAN.md) | Real frontier, gates and work order. |
| [`fragments/CROSS_PROGRAM_SYNTHESIS.md`](fragments/CROSS_PROGRAM_SYNTHESIS.md) | Independent cross-program comparison. |
| [`fragments/COVERAGE_VALIDATION.md`](fragments/COVERAGE_VALIDATION.md) | Mechanical validation of inventory and links. |

The remaining fragments are the block audits listed in the coverage table. A discrepancy is not resolved by the file name: the correction that exhibits the mathematical step and its hypotheses prevails.

## Size control

The full dossier contains twenty Markdown files, fewer than 50,000 words and fewer than 350,000 bytes. Even using the deliberately conservative bound of one token per byte, the context stays below 350,000 tokens and far from the one-million limit.

The byte bound avoids depending on a specific tokenizer and strongly overestimates the real size. Therefore the full dossier can be loaded as a single context within the requested budget.

## Integrity checks

- All existing phase directories belong to an audited interval.
- All RH task directories belong to a block audit.
- The targets of local Markdown links were verified.
- Proved, conditional, numerical, refuted, open and RH-strength results were separated.
- The labels `QED`, `closure` or `theorem` were not accepted as evidence without auditing hypotheses and quantifiers.
- The bibliographic novelty review remains a separate gate; this index certifies internal coverage, not external priority.
