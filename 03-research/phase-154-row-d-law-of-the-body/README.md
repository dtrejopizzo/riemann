# Phase 154 — Row D: the law of the body → the dual-certificate theory of Weil positivity — rounds 1–4 CLOSED (phase open on P154.1)

Created: Theorem A (λ_min = C₀ − Λ_T, Legendre of the Lévy energy on window-supported PD functions with two primitivity conditions);
archimedean generator = pure-jump subordinate Brownian motion (complete Bernstein φ); Theorem W (Wiener–Hopf E-L); Theorem O (dual never
attained); **Theorem D1 (strong duality: certificates complete)** ⇒ RH ⟺ outside-window atomic certificates for every T; Lemmas D2.1/D2.3
(periodic tail); **Theorem C(½log3): explicit certificate, λ_min(A_{½log3}) ≥ 4.43e-5 > 0, PROOF ACCEPTED** — first proof of Weil positivity with a prime coupled by an explicit
outside-window dual certificate (no Galerkin; larger Galerkin-certified windows exist: Zhu 2608.24827, Groskin 2607.02828); optimal duals restore the polar term (β₀ → 2). Open: certificate at log 2.

Rounds 5–10: tail theory finished (F1 two-frequency, Lemma T exponential columns, Hybrid Lemma), F3 verification (½log3 → 8.8577e-5), Theorem E, Identity M (Lévy tail band-limits the symbol, s = ½), Lemma W/V′ (rate lemma false: Θ(log R) sharp); two-prime step at 0.58 unresolved (best −3.18e-3; value problem, logarithmic returns, solver void at size). See R154_014–R154_030.

Files: R154_000 blueprint (+§4 create-the-object) · R154_001 report r1 · R154_002 audit · R154_003 blueprint r2 · R154_004 report r2 ·
R154_005 audit r2 · R154_006 blueprint r3 · R154_007 report r3 · R154_008 audit r3 · R154_009 blueprint r4 · R154_010 report r4 ·
R154_011 confirmation (PROOF ACCEPTED) · **R154_012 closing decision (labels of record)** · scripts/round{2,3,4}/,
scripts/round4/certificate/CERT_log3_M24.json.

**, after closure (R154_030):** R154_031 literature reading of the five primary texts (Zhu, Groskin, Suzuki ×3, Bombieri 2000,
Yoshida 1992; priority verdict: never claim "first positivity beyond log 2", Zhu certifies support 1.6 by Galerkin). **Paper 46**
written in LaTeX from this phase: `04-papers/46-row-d-dual-certificates/main.tex` (with the new §7 Theorem Z: the dual certificate is the
explicit formula on `w(u)cos(τu)`, value = flat-top smoothing of the zero measure; RH ⟺ one-sided smoothing for every window).
Off-machine computation package for the two-prime window: `scripts/offmachine/` (E1 M-sweep, E2 hybrid N=6 with IPM + control check,
E3 certify). Successor phase: `phase-155-row-d-flat-kernel-criterion` (Problem A, class-dependent value bounds).

## Other files in this folder

- `R154_013_LITERATURE_AND_CORPUS_REVIEW.md` — (P154.2) Literature and corpus review for Theorems A / O / D1 / C(½log3).
- `R154_015_ROUND5.md` — Round 5: the two-frequency staircase above `½log3`.
- `R154_016_AUDIT_R5.md` — Audit of round 5 (phase 154).
- `R154_017_ROUND6.md` — Round 6: cutting planes, column generation, and an **INTERIM** close.
- `R154_018_ROUND7_BLUEPRINT.md` — Blueprint, round 7 of phase 154: PURE MATHEMATICS — the approximation theory of the dual certificate.
- `R154_019_ROUND7.md` — Round 7: the certificate problem is a **spectral-gap one-sided approximation problem**, and its rate is a **zero-counting wall**.
- `R154_020_AUDIT_R7.md` — Audit, round 7 of phase 154.
- `R154_021_ROUND7_CLOSING_DECISION.md` — Closing decision, round 7 (pure mathematics: approximation theory of the certificate).
- `R154_022_CLUSTER_FALSIFIER.md` — Round 8: the clustered-atom falsifier at `T = 0.58`.
- `R154_023_ROUND8_CLOSING_DECISION.md` — Closing decision, round 8 (the clustering falsifier) and state of phase 154.
- `R154_024_ROUND9_BLUEPRINT.md` — Blueprint, round 9: smooth exponential certificates (the tail problem solved by construction) and mass-vs-value.
- `R154_025_ROUND9.md` — Round 9: smooth (Laplace/Laguerre) columns, Lemma T, and the sharpness of the mass–value exchange.
- `R154_026_AUDIT_R9.md` — Audit, round 9 (`R154_025`).
- `R154_027_ROUND10_BLUEPRINT.md` — Blueprint, round 10: the hybrid certificate (lattice + canonical Lévy column) and the repair of Lemma V.
- `R154_028_ROUND10.md` — Round 10: the repair of Lemma V, the Hybrid Lemma, and the tail price of the canonical column.
- `R154_029_AUDIT_R10.md` — Audit, round 10 (`R154_027` orders, `R154_028` deliverable).
