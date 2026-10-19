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
Yoshida 1992; priority verdict: never claim "first positivity beyond log 2", Zhu certifies support 1.6 by Galerkin). **Paper 47**
written in LaTeX from this phase: `04-papers/47-row-d-dual-certificates/main.tex` (with the new §7 Theorem Z: the dual certificate is the
explicit formula on `w(u)cos(τu)`, value = flat-top smoothing of the zero measure; RH ⟺ one-sided smoothing for every window).
Off-machine computation package for the two-prime window: `scripts/offmachine/` (E1 M-sweep, E2 hybrid N=6 with IPM + control check,
E3 certify). Successor phase: `phase-155-row-d-flat-kernel-criterion` (Problem A, class-dependent value bounds).
