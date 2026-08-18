# Phase 116 — the Logarithmic Schur Angle Conjecture

Snapshot created on 2026-08-14 from the row-(d) work that followed
phase-115 (reciprocal bands and the mean/oscillation Schur audit) and the
immediately preceding phase-114 research tree. This directory was
originally assembled under the working name "phase-115"; by the time it
was filed the number 115 had already been taken by
`phase-115-the-mixed-class-and-the-green-extension`, so it was renumbered
116. Some file contents and one internal script comment still say
"phase-115" — that is a naming artifact, not a dating error; the account
below is the authoritative one.

## What this phase did

Phase 115 left row (d) reduced to an exact constant/mean-zero Schur block
at every arithmetic threshold. This phase:

1. **Audited and rejected** a proposed Cauchy–Schwarz/Gamma-gap argument
   for closing that block (`ANALYTIC_AUDIT.md`). The block reduction is
   exact and useful; the proposed closure conflated a supremum with a
   single evaluation, misidentified the Gamma cross term, and treated a
   zero-mean condition as if it were hard spectral support. None of that
   proves positivity.
2. **Extracted the candid target** left standing after the audit and
   logged it as a candidate theorem, not a proved one
   (`CANDIDATE_LOG_SCHUR_THEOREM.md`): the squared Schur angle
   $\rho_N = b_N^*C_N^\dagger b_N / d_N$ satisfies $\rho_N \le 1/(20\log N)$
   for every $N\ge3$, supported by a seeded finite-dimensional scan
   through $N\le2000$ but not interval-certified.
3. **Carried that candidate into the paper.** It now appears verbatim as
   Conjecture (Logarithmic Schur Angle) in
   `04-papers/42-arithmetic-lefschetz-programme/main.tex`, with row (d)
   completed *conditionally* on it (Corollary, conditional completion of
   row (d)). Paper 42's abstract states this exactly: rows (a)–(c) and the
   certified initial range of row (d) are unconditional; the global Hodge
   inequality and the Riemann Hypothesis remain open unless the conjecture
   is proved.

So this phase did not close row (d). It closed off one wrong route to
closing it, and named the single remaining open estimate precisely enough
that it is now the one conjecture the entire programme in paper 42 is
conditional on.

## Contents

- `ANALYTIC_AUDIT.md`: the rejection of the proposed mean-zero/Gamma-gap
  closure, and the corrected irreducible target (the Schur angle $\rho_N$).
- `CANDIDATE_LOG_SCHUR_THEOREM.md`: the candidate Logarithmic Schur Angle
  theorem, its numerical support, and what an analytic proof would still
  have to establish.
- `current-chat/outputs/`: all TeX deliverables produced while drafting
  this material, including `main42new.tex`, audits v89–v131, and
  `main42new-conditional-row-d.tex` — an evaluation draft in which the
  construction of row (d) is recorded as complete while global positivity
  is explicitly conditional on the Logarithmic Schur Angle Conjecture; it
  does not claim that conjecture as proved.
- `current-chat/work/`: source code and editable textual work products used
  to build or test those deliverables, including
  `mean_zero_schur_scan.py` and its CSV output — the seeded, reproducible
  floating-point scan of the corrected Schur angle cited in
  `ANALYTIC_AUDIT.md` and `CANDIDATE_LOG_SCHUR_THEOREM.md`.
- `previous-phase-114/`: all Markdown, TeX, Python, Perl, JavaScript, JSON,
  shell, Julia, Sage, and notebook sources found in
  `phase-114-closing-the-four-rows`, preserving its relative directory
  structure.
- `paper42-notebook/`: the notebook before this phase's update and an exact
  snapshot of the updated Paper 42 notebook. The live copy is in
  `04-papers/42-arithmetic-lefschetz-programme/paper42-notebook/`.
- `MANIFEST.txt`: generated inventory of every file in this directory.

Binary references and caches from phase 114 were deliberately not copied;
the source texts and code were. The referenced ChatGPT conversation is not
available as a raw export on the filesystem. Its mathematical artifacts
that were present locally are preserved here, but this directory does not
claim to contain a verbatim transcript of every chat turn.

`paper-inputs/` (the five author-supplied source files) and
`CHECKSUMS.sha256`, both mentioned in the original phase-115-era snapshot
notes, were removed from this directory before it was reviewed and are not
reconstructed here; their content is superseded by the merged
`04-papers/42-arithmetic-lefschetz-programme/main.tex`.

## Status

Proved in the current manuscript (paper 42):

1. reciprocal half-integer barriers;
2. a uniform diameter bound for every connected rational-leakage cluster;
3. Gamma–Tate payment of every connected cluster;
4. absence of destructive low-frequency interference inside one band;
5. the exact constant/mean-zero Schur decomposition;
6. the proposed Cauchy–Schwarz/Gamma-gap closure is **rejected by audit**.

Open: the uniform Logarithmic Schur Angle bound, and therefore row (d),
condition G, and the Riemann Hypothesis. Numerical agreement, at any
sample size, does not by itself justify promoting the conjecture to a
theorem.
