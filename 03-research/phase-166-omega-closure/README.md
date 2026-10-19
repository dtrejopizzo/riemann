# Phase 166 — Closing ω(E): the quartet's sign at first contact

Goal: complete the proof of D. After phases 164–165 the gap is a single variable: ω(E), the position of
the witness's nodes within their cells at first contact, which decides the quartet's sign via
4Re G(t_q)² = 4|G(t_q)|² cos 2(Φ_Z ± πω(E) + Ψ_out) (R165_201 Cor 2.2). Wall dichotomy (R166_190 §0): any
argument using only the zero set is killed by M_m; any argument using only the prime window is killed by f_t;
the only thing ζ has that they don't is the exact duality "this zero set ↔ atomic prime side Λ on log ℕ." Each
round attacks ω(E) with a mechanism coupling the two and names the wall it evades.

Rounds: see R166_190_AUDIT.md.

## File index
- `R166_101_NODE_WEIGHT_SINGULARITY.md` — round 6: 1/δ² singularity of the nodal weights. DEAD (E1); tool Thm 2.1 (|G(t)/(t−x₀)| ≤ e^{Tδ}‖G′‖_∞).
- `R166_102_EXCHANGE_FLOW.md` — round 6: exchange flow Z_s. DEAD (W2/M in s); exact form and Lipschitz PROVED, lower bound ARGUED.
- `R166_103_FREE_MECHANISM.md` — round 6: free mechanism (α) Selberg, (β) determined tail, (γ) θ−1 moments. All three DEAD; tools: split 𝒯^det + ζ_{≥X} (B1–B2), falsifier P_{a,c}.
- `R166_201_SINE_COSINE_FLOW.md` — round 7: sine–cosine at the node, flow in T, atomic sampling. DEAD (E1); tools: jet hierarchy Thm 1.3, Cor 1.4, Prop 2.2.
- `R166_202_PARITY_COUPLING.md` — round 7: parity coupling (OS-2, 6C). DEAD (empty/E1); Thm 3 parity identity; residual O202.1 (T_e = T_o) OPEN.
- `R166_400_SURVEY_2_OF_3_MERGED.md` — round 9: merged survey (≈230 mechanisms, phases 0–166) of those meeting 2 of the 3 requirements; {i,iii} empty.
- `R166_401_SURVEY_2_OF_3_A.md`, `R166_402_SURVEY_2_OF_3_B.md`, `R166_403_SURVEY_2_OF_3_C_phases_001_110.md`, `R166_404_SURVEY_2_OF_3_D_phases_111_159.md` — round 9: partial surveys (160–163 + grid; 164–166; 0–110; 111–159).
- `R166_405_FAMILIES_P_Q_PATTERN.md` — round 9: families P {i,ii} (15) and Q {ii,iii} (30), how each member satisfies them, common pattern and P↔Q crossings.
- `R166_501_I_AND_III_IMPLIES_II.md` — round 9: **Thm A (PROVED): (iii) alone ⇒ (ii)**; transport of Thm R to η = Z − Q_X, obstruction B(5); requirements (G)+(N); O166.501.1 OPEN.
- `R166_502_P7_Q25_PRECHECK.md` — round 9: P7+Q25 precheck, REPEATED (E70_11/12); lemma on V*V's non-integer comb.
- `R166_601_ROUGH_ZETA_JOIN.md` — round 10: P1/P5+Q1 crossing (rough zeta, Legendre). Closed negatively (E1 / identification).
- `R166_701_THETA_ZERO_RIGIDITY.md` — round 11: rigidity at θ = 0. T3/T4 PROVED (coboundaries); C1/C2 OPEN; NO-GO as a route to D (fails (N)).
- `R166_702_POSITION_TUNED_BEURLING.md` — round 11: position-tuned systems. DEAD (DMV barrier θ ≥ β); tool Lemma PT.
- `R166_801_SECOND_MOMENT_7C.md` — round 12: cell 7C, second moment over translations. DEAD (E1/f_t); grid item 46 DONE.
- `R166_802_LAMBDA_INEQUALITY_CIRCULARITY.md` — round 12: circularity of every inequality over Λ (PROVED for single tests and power-size families; ARGUED in general, O166.802.1); sharpens (N) to (N′).
- `R166_190_AUDIT.md` — reference audit (§0 wall dichotomy, rounds 6–7 and 9–12, closures); authoritative labels.

## Rounds 6–7 (summary)
Round 6: three new mechanisms (nodal singularity, flow in s, free mechanism α/β/γ), three closures with proof; the quartet enters singularly (1/δ) only in the sine channel and at second order in the weights. Round 7: sine–cosine and parities, closed (E1 / empty). Structural theorem: jet hierarchy — the quartet's term in S^{(k)}(x₀) is 2k!|Q|²r^{1−k}cos(2E+(k−1)ψ); Re G(t_q)² is the jet k = −1, below every nodal datum; ω(E) is a global phase of G at t_q.

## Rounds 9–12 (summary)
Round 9: survey of the whole corpus against (i)–(iii): none satisfies all three; families P and Q disjoint; R166_501's Thm A proves (iii) alone implies (ii), so "{i,iii} empty" is a theorem. Round 10: the three P↔Q crossings settled (repeated, tautological/E1, excluded by Thm A). Round 11: the Beurling frontier below 1/3 (θ = 0, position) undecided, but NO-GO as a route to D: the count N is blind to the zeros. Round 12: cell 7C closed; the only inequality over Λ that would work is von Koch's O-bound localized at frequency γ_q (= localized RH). Final requirements: **(G) + (N′)**.

## Status
**Phase 166 closed (rounds 6–7 and 9–12); (★_cell) OPEN; row D OPEN.** Requirements for any future route (after round 12): **(G)** a non-constant invariant S of the witness, global in X; **(N′)** control of Λ beyond the window with zero-localization strength. No class, window, zero, or Λ-inequality route satisfies them without being RH. Continues in phase 167 (the (WS*) bound).
Editor (R164_301 §13): grid part 17 (1009 routes, ■10 ◩20 ◧34), R163_401 v11 (§4.11(h)), Paper 48 ("Phase 166" paragraph, Theorem jet hierarchy; 29 pages).
Editor (R164_301 §15): grid part 18 (1022 routes, ■11 ◩19 ◧34; 7C painted), R163_401 v12 (§4.11(i)), Paper 48 ("Phases 166–167" paragraph; 31 pages).
