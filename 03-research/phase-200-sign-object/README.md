# Phase 200 — The sign object

re-analyze the ENTIRE program (RH1–RH9, phases 0–199, indices, maps, Paper 47) to extract the
positive insights about the sign, and with that map invent the "sign object": a new mathematical piece, that does not use
any of the already exhausted tools (Chebyshev, Fourier, Euler–Poisson, Kreĭn–von Neumann, Schur, Möbius on lines,
passivity, …), and that is the missing plank for Lemma L′♯ / row D.

Working rules: row D independent; no D⟺RH equivalence; honest labels; routes index before
building; every proposal must be falsifiable against Mori's certified extremal (μ=15) and against the certified
falsifiers.

## Stage 1 — Insight ledgers (one verification per segment)
- L1: RH1–RH9 (01-context) + phases 0–99
- L2: phases 100–162
- L3: phases 163–193
- L4: phases 194–199 + Paper 47
- L5: indices/maps (routes index, now ROUTES-MASTER-INDEX.md; grid, crossword, surveys, NO-GO-LIST, MASTER-PLAN)

## Stage 2 — Specification of the sign object + candidates
## Stage 3 — Construction + audit

## Log

## Status (afternoon)
- Stage 1 DONE: LEDGER_L1…L5 (12,167 words). Convergence: second-order object, non-factorized,
  half-space/reflection positivity, reads the exact comb on log ℕ without going through h*, output = square or count,
  post-cancellation coordinates c_N (N ≥ μ), coercivity transverse to the truncated Pólya radical, orientation-sensitive.
  L5: ~1,650 routes in 10 classes; C10 (global object) never constructed; 6 areas of the negative space not excluded.
  Tension T2 of the index (Mori label) corrected in README l.445.
- Stage 2 DONE: SPEC_SIGN_OBJECT_001.md — properties P1–P8, elementary fact PROVED c_N = −μ(N) on [μ,2μ),
  candidates K1 OS-Γ (OS reflection at x=T, CM kernel of poles Γ_ℝ) > K3 Γ-limit (Hermite/ultraproduct, sector ψ_{4j})
  > K2 DS-×ℕ (defect on the solenoid, cocycle μ(n)). Naive lemma K1.1 already refuted by the synthesizer itself.
- Stage 3 IN PROGRESS: K1_OSG_001.md, K3_GAMMA_001.md, AUDIT_200_SPEC_001.md.
- Stage 3 round 1 DONE: K1 NO-GO (PROVED; restriction R-K1: the gap protects products, sign in quotients N′/N), K3 NO-GO
  (comb-generic Γ-limit; K3.1=(P0c) PROVED asymptotic, Mori's f* saturates the escape bound), K2 NO-GO (μ not a cocycle).
  AUDIT_200_SPEC_001: rewrite P3 (free positivity nonlinear in the comb, false at the identity for DH and cΛ c<1).
  Index updated. Next: SPEC v2 with P3 rewritten and P7 removed; candidates on quotient structure.
- Round 2 DONE (SPEC_002, AUDIT_200_SPEC_002, Q2_LADDER_001): T.1/T.3/rule c_{pN}/Q2.1/Lemma R PROVED; Q1, Q2 NO-GO
  (tautological: every mollified exterior ≡ −g mod radical at any level), Q3 DOUBTFUL. Restrictions R-Q2 (coordinates
  inside the radical) and properties P9′ (object in L²/𝔑) + P10 (anti-tautology). No sign. L′♯ OPEN.
- Round 3 DONE (SPEC_003, AUDIT_200_SPEC_003, C1_DUPLICATION_001): 𝒬_μ = escape quotient of Paper 47 (A.1 PROVED);
  bridge ι PROVED = lem:monoT exterior, NO-GO as sign; R-Q6 (the descent to the quotient already uses exact Λ); C1/C2/C3/C3′
  NO-GO; B.1 OPEN ← B.1♭. Final operative definition: A_μ explicit from (ℕ,+,·) with 𝒲 = ‖A_μ·‖² − ℰ_μ, ℰ_μ ≥ 0,
  nonexistent for a_P and c=2. Round 4: build A_μ.
- Round 4 DONE: A_μ (a)–(e) NO-GO; (f) NO-GO (Theorem D = chain rule; n^ε = moving σ); B.1♭/uniform B.1 FALSE
  (harmonic stacking, β_μ ≤ C/log μ). Round 5 DONE: Π_μ = projector onto 𝒦_T PROVED (‖Π r‖² = ℓ/2), archimedean
  and blind to the comb (R-Π); architecture A_μ = B∘Π_μ CLOSED (= eq:ext-starstar on 𝒦_T); jumps of f♯ PROVED, rank-one
  jump comb c_J = +0.01158 (R-Π4). Exact Λ lives in: inclusion 𝒢̄_T ⊂ rad 𝒲 (Guo L4.4) and the intertwiner Z.
  Round 6: Z as carrier — form inequality on 𝒦₁ whose arithmetic comes from Z quantitatively.
- Round 6 DONE: Z_CARRIER NO-GO (R-Z1: Euler enters only through dead (α), Guo L4.4 (β), dead (γ)). Round 7 DONE:
  META_200_BARRIER (Theorem M200, class 𝒦_200); GUO_QUANT: (β) NO-GO, P1 NO (W*/J²Σ1/(ρ(1−ρ)) = 1.022, coincidence),
  Epstein x²+5y² (h=2) as reference falsifier — restriction C-Guo; P2 NO at escape scale; P3 PROVED on 𝒮,
  Mori ∉ 𝒮. Pending: Lemma E (certified Epstein + Λ−Λ_Q comb at the extremal), F₀. Only lever: quadratic Euler
  product in the complement of the radical.
- Round 7 close: Lemma E PROVED (Epstein x²+5y², T ≥ 1.59; witness 11; P47 lem:shape-epstein PROVED, backup
  main_pre_epstein.tex). Round 8 DONE: COSH_DEFECT — exact identity Λ_cosh, 𝔇 = −𝒬_g[b] − R₄ without definite sign;
  Theorem S (affine in θ); C-int; restriction C-θ. Round 9 IN PROGRESS: SPEC_004 — nonlinear object in θ (inertia/Fredholm
  index as a count) or Theorem M200′.
- Round 9 DONE (SPEC_004): N1–N5 NO-GO; Prop 2.1 ζ isolated in degree 1 (Kaczorowski–Perelli); Lemma I.1; M200′.
  Round 10 DONE: Q2 degree-2 family Z_τ (Beurling with FE; positive set ⊂ 13 Heegner h=1 CONDITIONAL; C-τ:
  discontinuous positivity in τ); Lemma I.3 NO-GO (affine bundle in c; A_⊥⊥(1) gap O(1) in block; smallness of Mori = carrier).
  Convergence of three barriers (TV, C-θ, C-τ): positivity is DISCONTINUOUS in the comb; the object must read the
  exact integrality discontinuously. Next: I.4 (real carrier) and positivity at Heegner points.
- Round 11 DONE (SPEC_005 + AUDIT_200_Q2): discontinuous invariant 𝔖 = h(D)−1 (classifier, not a motor); Lemma H ⇒ C-hom
  (0-homogeneous form in theta: no quadratic identity/4 points); test a_P (loses the lattice origin); Q2 = reformulation
  DH I + BG (corrected citations). Round 12 IN PROGRESS: R11_1_CUTS — relations of the multiplicative collapse as cuts in the
  LP/SDP dual of P47 (block test: does the dual value go up?).
- Round 12 DONE: R11.1 NO-GO PROVED (C-data: the multiplicative relations are equalities between data, not between
  SDP variables; dual value invariant). Pending: R11.2, Lemma 12.1 (h=2,3 unified).
- Round 13 DONE: R11.2 NO-GO PROVED (C-pol: the (A,B) moments are null in P_T; polar channel closed); Lemma 12.1 PROVED
  (Λ_def = log n·log E_χ[e^{y_χ}], cumulants of the class group dual; h=3: order 2 does not dominate). Round 14: full
  cumulant form in the principal class (Lemma 13.1).
- Round 14 DONE: Lemma 13.1 PROVED — the class defect is a pure finite comb in P_T, indefinite; no Jensen/convexity
  under L. means. "Cumulants" direction closed. Next: Lemma 14.1 (relative pencil) / non-principal class.
- Round 15 DONE (SPEC_006): table of 25+28 restrictions; Theorem Φ200 (5 branches); Φ.12 additivity PROVED → P47
  rem:shape-additive (backup main_pre_phi12.tex); Φ.14 PROVED with hypothesis. Round 16 DONE: Ξ1 NO-GO PROVED (C-MvN),
  Ξ2 NO-GO (Φ.13 PROVED), Ξ3 NO-GO ARGUED (C-𝔖). Virgin space checked: empty except for gaps without an object.
- Round 17 DONE: DH_TRANSFER (channel (i) of Φ200 PROVED as a restriction of premises in 𝔗₁; DH NOT certified in the
  corpus → CERT_DH in progress); SPEC_007 immersion channel ⊂ 𝒦_200 (C-emb; Lemma B.2: comb of an indefinite prime;
  positivity = collective balance). Φ200 PROVED in all channels (exhaustiveness/composition ARGUED).
- Round 18 DONE: AUDIT_SPEC007 (F8 withdrawn; Cor B.3 = cor:Tarch, inverted reading); SPEC_008: free variables V1–V6
  NO-GO (V3 large sieve = R162_1102; V1 log-convexity falsified; V2 loses C-pol); Prop 18.4: exogenous free variable.
  Pending: CERT_DH (certification of the Davenport–Heilbronn falsifier).
- Round 19 DONE (SPEC_009): exogenous objects X1–X5 NO-GO (Rankin/Φ.12 REF-D; Hecke-Petersson = Γ/conductor; shifted
  Selberg = CA_F_002). Conclusion: the exogenous variable must live outside L-functions with FE over ℚ.
- Round 20 DONE (SPEC_010 + HORN_A): C10/arithmetic Hodge — phase 135 is not reopened (Thm 19.25 holds in P_T); Prop 20.1
  arithmetic Serre duality = Poisson without comb (C-RR); Horn A = (W⁰) reformulated, NO-GO PROVED; Hodge-transfer line
  closed. Pending: CERT_DH.
- Round 21 DONE (HORN_B_BIGSHARP): Horn B and (Big♯) NO-GO PROVED; Hodge-transfer line closed. Alive under the name:
  SPEC-𝔇 (S1–S6) = existential specification of the object for phase 201; (Eff_𝓔′). Pending: CERT_DH.
- Round 22 DONE (D_CONSTRUCTION + AUDIT_DCONS): direct construction of 𝔇 — 𝔇₀/𝔇₁/𝔇₂, Möbius as duality, mixed
  area: all NO-GO; δ ≡ 0 PROVED without Schanuel; Lemma 𝔇-Sch NO-GO; Thm 3′: χ of analytic-rank type in the test is
  generically constant. No object satisfies S1 ∧ S3. Pending: CERT_DH.
- Round 23 DONE (SPEC_011): oscillation counts NO-GO by class (Lemma N2 Paley–Wiener: gap ⟺ cut unrelated to the comb;
  negativity at low frequency without a gap). Pending: CERT_DH.
- Round 17C DONE: CERT_DH PROVED (F_DH negative in P_T ∀T ≥ 9/5, arb 7000 bits; reproduces Ziad) → witness 12;
  P47 rem:FDH proved (188 pp, backup main_pre_certdh.tex). Round 24 IN PROGRESS: CS-0, MAP_200.
- Round 24 DONE: CS-0 PROVED (prolate class); MAP_200 (64 tools, 36+28 restrictions, 12 falsifiers,
  spec v12, 13 not constructed, 3 questions). Round 24c IN PROGRESS: AUDIT_CERTDH (P201.1), P201_2_IDEALS.
- Round 24c: P201.2 NO (δ measures splitting, not h). Round 25 DONE (MOMENTS): symbol channel fully closed —
  ∫|ĝ|²(|D_μ|²−1)σ = 0 (R-MOM). Pending: AUDIT_CERTDH.
- Round 24c DONE: AUDIT_CERTDH PROVED (re-run bit by bit; ζ control always positive); P47 rem:FDH corrected
  (Spira 1994 in the bibliography, monoT applies to DH, «for every T ≥ 9/5»), 188 pp, 0 errors. Round 26 IN PROGRESS: multiplicative
  gauge (R-MOM as a class theorem); Π.5 (|f♯(0)|² ≤ Cℓ, tool without Λ).
- Round 26 DONE: MULT_GAUGE (M.2 PROVED; R-MOM class theorem; additive+multiplicative gauges = REF-D);
  PI5_TATE (Π.5 PROVED by N with e^{4πN}, uniform NO-GO; ℓ* of MORI15 is an upper bound). Phase 200: 26 rounds.
