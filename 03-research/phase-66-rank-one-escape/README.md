# Phase 66 — The rank-one escape dichotomy: a positivity-free reformulation and its wall

Unlike the Weil-positivity routes, the Connes–Consani–Moscovici "Zeta Spectral Triples" construction
gives operators that are self-adjoint by construction, so there is no positivity to prove; the phase
studies instead the remaining obstacle, operator convergence/boundedness, as a distinct "rank-one
escape" dichotomy: whether all divergent mass of the canonical Gram kernels $K_P$ escapes only through
the single pole direction. It tries to close this dichotomy end to end, retracts an overreaching
candidate proof, isolates the maximal rigorously closable package, and builds numerical detectors for
the easy direction.

## Results
- Exact statement of the rank-one escape dichotomy: $\sup_P \|P_{\mathrm{prim}} K_P P_{\mathrm{prim}}\| < \infty \iff \mathrm{RH}$
  (an off-line zero is a second escape direction growing like $\lambda^{2\beta-1}$): PROVED as a
  reformulation (positivity is free by von Mangoldt positivity of the canonical Hamiltonians; this
  statement is the sole remaining wall, RH-strength).
- Candidate end-to-end proof of the escape theorem: RETRACTED by internal audit — three specific errors
  found (a claimed Hermite–Biehler structure function that is actually only meromorphic; an incorrect
  de Branges doubling-of-zeros relation; and a refuted claim that leading-trace rank-one bounds the
  Kreĭn–Langer index, refuted by an explicit counterexample). The forbidden circular step (scalar
  determinant convergence implied structural convergence) is identified explicitly.
- Maximal audit-safe closure (superseding the retracted proof): several genuine lemmas are proved —
  Hermite–Biehler passes to the limit under local-uniform structural convergence; positive-pole Schur
  shorting preserves index zero under finite-Gram convergence; rank-one isolation holds on the strict
  subcritical core — but it is proved that leading-trace rank-one is NOT sufficient for operator-norm
  rank-one escape, and the full endpoint statement ($K_P^\circ \to K_\Xi$ at the critical boundary,
  equivalent to the escape bound) remains open and is exactly RH-strength: PROVED (partial closure) +
  explicit identification of the remaining open content.
- D1 (sharp dichotomy, easy direction): the analytic content (¬RH ⟹ unbounded escape via orthogonality
  of the off-line escape direction to the pole direction) is sound; a first crude numerical proxy (E110)
  is withdrawn as not measuring the right object.
- D2 (faithful-proxy escape detector, E111): using a validated proxy (not the full transfer-matrix
  kernel), ζ shows bounded escape mass ($N(P)$ flat, exponent $\approx -0.05$) while the Davenport–Heilbronn
  control shows unbounded growth, with the key structural confirmation that the off-line escape mass is
  essentially unaffected by removing the pole direction (orthogonality confirmed numerically): NUMERICAL,
  a detector/criterion, not a proof.
- D3 (face A, large-sieve gap): identifies "face (A)" of the escape theorem (uniform sup-norm
  boundedness of primitive partial sums of $-\zeta'/\zeta$ on the critical line) as requiring an
  $L^\infty$ bound where the classical Montgomery–Vaughan large sieve gives only an $L^2$ (mean-square)
  bound: PROVED (the gap is precisely identified and mapped to the program's Master Wall MW-2).
- Calibration note: a separate scalar-whitening approximation to the operator (E112/E113) is shown, by
  direct comparison against the exact matrix-whitened operator, to describe the wrong operator entirely
  (its marginal λ_max → 1 behavior is destroyed by the scalar approximation); all conclusions drawn from
  E112/E113 (sub-exponential growth laws, a Toeplitz saturation picture) are RETRACTED as irrelevant to
  this phase's actual object.

## Documents
- `PROBLEM-STATEMENT.md` — the exact rank-one escape statement and why it sidesteps Weil positivity.
- `CANDIDATE-PROOF-omega7.md` — the retracted end-to-end candidate proof, with its three errors documented.
- `MAXIMAL-CLOSURE-omega7.md` — the audit-safe maximal closure and precise isolation of the remaining open content.
- `RESULTS.md` — consolidated log of D1/D2/D3.
- `D3-large-sieve-gap.md` — identification of face (A) with the classical large-sieve sup-vs-mean-square gap.
- `CALIBRATION.md` — retraction of the E112/E113 scalar-operator findings as not transferring to this phase's object.
- `E110_escape_dichotomy.py`, `E111_escape_norm.py`, `E111_RESULTS.md`, `E112_TN_growth.py`, `E112_RESULTS.md`, `E113_TN_closedform.py`, `E113_RESULTS.md` — numerical detector scripts and their results/retractions.

## Relation to other phases
Builds on the canonical Tate–Weil Hamiltonian construction of phase 64 (`CONSTRUCTION-TW-canonical-system.md`)
and the Kreĭn–Langer/Hermite–Biehler audit discipline of phase 65; its unresolved endpoint-convergence
statement remains an open, RH-strength target for any later continuation.
