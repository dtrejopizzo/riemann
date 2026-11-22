# Phase 211 — The sign of the window form, in isolation

Target: (★) λ_A(T) ≥ 0 for every T > 0 ([STATEMENT_001.md](STATEMENT_001.md)). The sign of the
Paper 46 window form is treated as a statement about one explicit quadratic form (s_T, a_T, P_T, λ_A)
and nothing else; no equivalence with any other statement is used, named or reasoned from, at any
step. Pure mathematics; computations only to validate single concrete points. No paper is edited
until the sign is proved.

Most working memos (in particular the `POWER_*` series) are written in Spanish; the early rounds,
states and reviews are in English.

## Status (as recorded in the folder's own state files)

- **Global sign (★): OPEN.**
- (★) is PROVED (certified) for T ≤ ½ log 5; CITED for T ≤ ½ log 15 through λ_W ≤ λ_A and the
  complete-form certificate (analytic lemmas of the source not audited) — [STATE_002.md](STATE_002.md) §1.
- Computer-assisted lower certificates: λ_A(1) ≥ 1.0·10⁻²³ and λ_A(1.035) ≥ 2·10⁻²⁶, PROVED
  (computer-assisted) in [ROUND_026_A.md](ROUND_026_A.md); NO-GO on the available machine for T ≥ 1.2.
- Exact reformulations (two-sector reduction, sign budget, band/packet reductions, Weyl counts,
  margin law) are PROVED pieces with no sign; candidates C1–C51 each end in a PROVED piece, a NO-GO
  in a declared class, a NUMERICAL observation or a pivot — see [LEDGER.md](LEDGER.md).
- POWER programme (finite families of matrices built from the completed logarithmic derivative,
  [POWER_CONE_001.md](POWER_CONE_001.md)): PROVED bridges in norm, finite cases (four arbitrary
  powers with exponents > 1, thirteen with exponents ≥ 32), T_h > 0 globally
  ([POWER_STATE_099.md](POWER_STATE_099.md)), and many audited NO-GOs and falsifiers; the uniform
  obligation for all sizes remains OPEN — [POWER_REASSESSMENT.md](POWER_REASSESSMENT.md),
  [POWER_GLOBAL_ROUTE_REVIEW.md](POWER_GLOBAL_ROUTE_REVIEW.md).

Labels used throughout: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL
(NUMÉRICO in the Spanish memos).

## Suggested reading order

1. [STATEMENT_001.md](STATEMENT_001.md) — statement of record: (L2), (S), (B) forms of (★).
2. [DOSSIER_001.md](DOSSIER_001.md) — definitions, tools, barriers, shape of the solution.
3. [OBJECT_SPEC_001.md](OBJECT_SPEC_001.md) and [BRIEF_CONSTRUCTOR.md](BRIEF_CONSTRUCTOR.md) — what
   a sign-carrying object must satisfy; conventions for construction memos.
4. [STATE_001.md](STATE_001.md), [STATE_002.md](STATE_002.md) — state after rounds 1–3 and 5–20(+).
5. [LEDGER.md](LEDGER.md) — one line per candidate object.
6. [POWER_CONE_001.md](POWER_CONE_001.md), [POWER_BRIDGE_002.md](POWER_BRIDGE_002.md), then the
   latest `POWER_STATE_*` and [POWER_REASSESSMENT.md](POWER_REASSESSMENT.md).
7. [POWER_GLOBAL_ROUTE_REVIEW.md](POWER_GLOBAL_ROUTE_REVIEW.md) — review of global routes and
   rejected selections.

## Index of contents

### Starting audit and framing
- [AUDIT_001.md](AUDIT_001.md), [AUDIT_002.md](AUDIT_002.md), [AUDIT_003.md](AUDIT_003.md) — audits of
  phases 0–99, 100–160, 161–210: no proof, near-proof or unrecognised shortcut for (★) beyond ½ log 5.
- [DOSSIER_001.md](DOSSIER_001.md) — Papers 43–48; [SURVEY_001.md](SURVEY_001.md) — Papers 1–42 as a toolbox.
- [LITERATURE_001.md](LITERATURE_001.md) — external literature checked.

### Rounds (English): `ROUND_001_A.md` … `ROUND_027_A.md`
Constructions, one candidate object per memo, each ending in PROVED piece / NO-GO / pivot. Key ones:
[ROUND_002_A.md](ROUND_002_A.md) (exact two-sector reduction), [ROUND_005_C.md](ROUND_005_C.md)
(comb-response family E_T, sign budget), [ROUND_007_C.md](ROUND_007_C.md) (certified falsifiers),
[ROUND_026_A.md](ROUND_026_A.md) (computer-assisted lower certificates).

### Reviews and states
- `REVIEW_001.md` … [REVIEW_010.md](REVIEW_010.md) — independent reviews of the rounds; their
  verdicts govern the labels.
- [STATE_001.md](STATE_001.md), [STATE_002.md](STATE_002.md), [LEDGER.md](LEDGER.md).

### POWER programme (Spanish)
- `POWER_STATE_*.md` (57 files, 003–099) — state snapshots after each step; the highest number is
  the latest.
- `POWER_*_AUDIT_*.md`, `POWER_AUDIT_*.md` — audits of the matching memo.
- Memos by topic (file-name prefix): `POWER_THETA_*` (theta densities, ratios, compact
  certificates), `POWER_MIXED_*` (mixed four-generator family), `POWER_CONFLUENT_*`,
  `POWER_FOUR_*`/`POWER_FIVE_*`/`POWER_SIX_*`/`POWER_SEVEN_*`/`POWER_FULL_*` (finite orders),
  `POWER_RECIPROCAL_*`, `POWER_REAL_*`, `POWER_GAMMA_*`, `POWER_SIGNED_*`, `POWER_INVERSE_*`,
  `POWER_CONTACT_*`, `POWER_HIGHPASS_*`, `POWER_INTERIOR_*`, `POWER_ARITHMETIC_*`, and others.
- Obstructions and global reviews: [POWER_GRAM_SLICES_OBSTRUCTION.md](POWER_GRAM_SLICES_OBSTRUCTION.md),
  [POWER_HYPERBOLIC_MODEL_GRAM.md](POWER_HYPERBOLIC_MODEL_GRAM.md),
  [POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md](POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md),
  [POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md](POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md),
  [POWER_DESCENT_016.md](POWER_DESCENT_016.md),
  [POWER_RECIPROCAL_PFAFFIANS_083.md](POWER_RECIPROCAL_PFAFFIANS_083.md),
  [POWER_GLOBAL_ROUTE_REVIEW.md](POWER_GLOBAL_ROUTE_REVIEW.md),
  [POWER_CORPUS_OPPORTUNITY_AUDIT.md](POWER_CORPUS_OPPORTUNITY_AUDIT.md).

### Other memos (Spanish)
- [PROPOSAL_POWER_CASES_2026_11_04.md](PROPOSAL_POWER_CASES_2026_11_04.md),
  [NEAR_CASES_RESULTS_2026_11_04.md](NEAR_CASES_RESULTS_2026_11_04.md) — elementary cases: an
  auxiliary PROVED improvement of nearfree and algebraic counterexamples; no global sign.
- [SQUARE_COMPLETENESS_OBSTRUCTION.md](SQUARE_COMPLETENESS_OBSTRUCTION.md) and its audit.
- [CORRECTION_RESIDUE_BALANCE_031.md](CORRECTION_RESIDUE_BALANCE_031.md) and its audit.

### Tools and data: [tools/](tools/)
- [TOOL_001_GALERKIN_MP.md](TOOL_001_GALERKIN_MP.md) and [tools/README.md](tools/README.md) —
  multiprecision Galerkin engine `tools/galerkin_mp.py` (NUMERICAL only; Galerkin minima are upper bounds).
- `tools/power_*_verify.py` — exact verifiers cited by the POWER memos (most use exact rational
  arithmetic); some have `.sha256` and `.log` files recording a reference run.
- `tools/falsifier_cert.py` — certified falsifier witnesses (ROUND_007_C).
- `tools/prolate_*.py`, `tools/band_*.py`, `tools/schur_coupling_*.py`, `tools/rung_gram_*.py` —
  NUMERICAL scripts of the rounds.
- Subfolders: [tools/cert_window/](tools/cert_window/) (window certificates; very large binary data,
  git-ignored), [tools/cache/](tools/cache/) (matrix caches), [tools/multi_cell/](tools/multi_cell/),
  [tools/first_cell/](tools/first_cell/), [tools/coprime_pair/](tools/coprime_pair/),
  [tools/align21/](tools/align21/), [tools/strip22/](tools/strip22/),
  [tools/tail_direct/](tools/tail_direct/),
  [tools/rstation45_reproduction/](tools/rstation45_reproduction/).

## Running the verification scripts

From the repository root, with Python 3 (some exact verifiers need only the standard library,
others use `python-flint` ball arithmetic; numerical scripts use `mpmath`, `numpy`, `scipy`, `sympy`):

```sh
python3 03-research/phase-211-sign-sandbox/tools/power_five_global_010_verify.py
python3 03-research/phase-211-sign-sandbox/tools/power_exact_h_global_099_verify.py
```

Each POWER memo names its verifier; a passing run exits with status 0 and, where recorded, its
output hash matches the `.sha256` file next to the script. Some scripts write caches under
`/tmp/phase211/`.

## Further series in this folder

- `POWER*` series (122 further memos, `POWER_ARCH_CELL_026.md` … `POWER_WEIGHTED_COEFFICIENT_034.md`).
- `REVIEW*` series (8 further memos, `REVIEW_002.md` … `REVIEW_009.md`).
- `ROUND*` series (41 further memos, `ROUND_003_A.md` … `ROUND_025_B.md`).
