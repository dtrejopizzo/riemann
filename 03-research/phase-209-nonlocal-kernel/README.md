# Phase 209 — A genuine two-variable kernel (O1)

Working memos in this folder are written in Spanish (a few QRH notes are in English).

## Aim

Row D is treated as an independent target. The aim of the phase was to complete the proof of D
through residue O1 of `CELL_001` §8: construct a Hermitian kernel K_T(t,t′), genuinely of two
variables, with explicit domain and regularisation, whose positivity mechanism couples to the
conductor-1 functional equation and to the full arithmetic, and then link it to the window form Q_T
of Paper 47 by an identity or a domination. Non-locality alone does not count as progress; the
operator must be shown not to collapse into ⟨M_f, J⟩ or to be the disguised node.

Mandatory gates, in order: (0) corpus check before building; (1) the exact SOS barrier (P47
thm:sos); (2) the two-variable barrier (P36-4 kernel vs the relaxed set W₂ of the BR tree);
(3) positivity proved without using the sign of Q_T, and specificity under deletion of a prime;
(4) link with Q_T, with every term and sign accounted for.

## Status (as recorded in `GOAL_D_STATUS.md` and `SYNTHESIS.md`)

- **D: OPEN.** The goal is recorded as *blocked* after three consecutive passes without a new
  verifiable link after LINK_016. This does not assert a general impossibility for O1 or D.
- Auxiliary results (audited): SPD kernel −Rα (CONSTRUCTOR_005); functional equation of Π
  (CONSTRUCTOR_006); orthogonal domain and exact PSD cone (CONSTRUCTOR_015, PROVED); dense range of
  the map of LINK_011 (LINK_016).
- First round: PARTIAL / NO CANDIDATE — NO-GO for J+C compact on H_A (CONSTRUCTOR_001, AUDIT_001).
- Positive partial: geometric concavity of θ−1 and anticorrelation of prime factors
  (ANTICORRELATION_003, AUDIT_003); signed Mellin cross term at α = 1/4 (CONSTRUCTOR_004, AUDIT_004).
- Link attempts with Q_T: necessary spectral regularity (LINK_010); Mellin–Gauss map, does not
  coincide with Q_T (LINK_011); domination with the exact normalisation is false, certified
  falsifier at T = 4/5 (LINK_012); no fixed constant c > 0 works (LINK_013); removing positive pieces
  does not help (LINK_014); positivity only on the image gives nothing new (LINK_016).
- Virtual source (VIRTUAL_SOURCE_017): leaves Q_T = E_pos − (A_T − C0)‖F‖² with A_T − C0 > 0
  uncontrolled; not functional for D, not a general NO-GO.
- QRH notes (independent of D): reading of the external Quasi-Riemann Hypothesis preprints; exponent
  map, replica coherence (PROVED identity, no new control of the coherent component), 4/5 attempt
  and candidate audits. Continued in `../phase-210-qrh-four-fifths/`.

No paper was modified.

## Contents

**State and synthesis**
- `GOAL_D_STATUS.md` — continuity log and current status of D.
- `SYNTHESIS.md` — map of results and limits of the phase.
- `GOAL_QRH_FOUR_FIFTHS_STATUS.md` — status of the 4/5 zero-free half-plane goal.
- `CONTROL_001.md`, `REVIEW_TARGETS_002.md`, `SCOPE_P44_009.md`, `DISCOVERY_DIAGNOSTICS.md` — control
  notes, review targets, scope check against Paper 44, diagnostics.

**Constructions** (`CONSTRUCTOR_*`, with matching `AUDIT_*`)
- `CONSTRUCTOR_001.md` … `CONSTRUCTOR_008.md`, `CONSTRUCTOR_015_DOMAIN_AND_CONE.md`.
- `POSITIVE_ASSOCIATION_002.md`, `ANTICORRELATION_003.md` — positive-association and anticorrelation
  results.

**Links with Q_T** (`LINK_*`)
- `LINK_009_CONTINUOUS_FLOW.md`, `LINK_010_SPECTRAL_REGULARITY.md`, `LINK_011_MELLIN_GAUSS_MAP.md`,
  `LINK_012_DOMINATION_FALSIFIER.md`, `LINK_013_NO_FIXED_SCALE.md`, `LINK_014_REMOVING_RANK_ONE.md`,
  `LINK_016_DENSE_RANGE.md`.
- `VIRTUAL_SOURCE_017_METRIC_TEST.md` — virtual metric source test.

**Audits** — `AUDIT_001.md` … `AUDIT_017.md`, one per construction or link memo with the same number.

**QRH notes** — `QRH_SOURCE_RELEVANCE.md`, `QRH_EXPONENT_MAP.md`, `QRH_REPLICA_COHERENCE.md`,
`QRH_FOUR_FIFTHS_ATTEMPT.md`, `QRH_LOW_CANDIDATE_VALIDATION.md`, `QRH_HIGH_CANDIDATE_AUDIT.md`,
`QRH_HYPERBOLIC_PROJECTION.md`, `QRH_PRINCIPAL_TARGET_QUOTIENT.md`, `QRH_QUOTIENT_ABSOLUTE_MEAN.md`.

**Data and scripts**
- `DIAGONAL_005_data/` — `probe.py`, `probe_primes.py` and their JSON outputs (numerical probes for
  CONSTRUCTOR_005).
- `LINK012_data/` — `certify.py` (certified falsifier of LINK_012), `check_laplace.py`, `explore.py`
  and JSON outputs.

## Suggested reading order

1. `SYNTHESIS.md`, then `GOAL_D_STATUS.md`.
2. `CONSTRUCTOR_001.md` / `AUDIT_001.md` (first round, barriers).
3. `ANTICORRELATION_003.md`, `CONSTRUCTOR_004.md`, `CONSTRUCTOR_005.md`.
4. `LINK_011` → `LINK_016` with their audits, then `CONSTRUCTOR_015_DOMAIN_AND_CONE.md`.
5. `VIRTUAL_SOURCE_017_METRIC_TEST.md`.
6. QRH notes, starting with `QRH_SOURCE_RELEVANCE.md` and `QRH_EXPONENT_MAP.md`.

## Running the scripts

Python 3 with `numpy`, `scipy`, `mpmath` and `python-flint` (Arb). Run from inside the data folder,
e.g. `cd LINK012_data && python3 certify.py`. Outputs are the JSON files stored alongside.
