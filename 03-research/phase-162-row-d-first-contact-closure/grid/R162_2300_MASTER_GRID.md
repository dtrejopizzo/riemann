# R162_2300 — MASTER MAP of row D (8×8 grid, full corpus)

Permanent document; updated (part 18 merged). Read-only: no sign is asserted; Gate 1 remains OPEN.
Sources: `R162_2300_MASTER_grid.json` (1022 merged routes: phases 0–161 in parts 1–4, papers 01–47 in part 5, sub-audit of 160–161 (R160_S1–S5 complete, memos R160, R161 1–35 and 030–081, R161_099) in part 6, phase 162 from R162_2200, rounds 22–24 of phase 162 (R162_2201–2402) in part 7, rounds 25–26 (R162_2501–2602, audit 2590) in part 8, rounds 27–28 (R162_2701–2802, audit 2890) in part 9, round 29 (R162_2901, 2902a–c) in part 10, phase 163 (R163_001–003, 101, 102, audit 190) in part 11, round 31 (R163_201–203, audit 290) in part 12, rounds 32–37 of phase 163 (R163_401–1001) in part 13, and rounds 1–2 of phase 164 (R164_101, 102, 201, 401, 402) in part 14, and rounds 3–4 of phase 164 (R164_501, 502, 503, 601, audit 491) in part 15, and phase 165 (R165_101, 102, 201, 202; audit R165_190) in part 16, rounds 6–7 of phase 166 in part 17, and rounds 9–12 of phase 166 and phase 167 (R166_501–802, R167_101–103, audit R167_291) in part 18), the `R162_2300_part1..5.md` summaries, `../R162_2200_GRID_MAP.md` and `../README.md` (late corrections).
Machine-readable version: `R162_2300_MASTER_grid.json`, with refined `status`, `live_residuals`, `editor_note` and `counts` in each cell.

## 0. How to use this map (mandatory rule)

1. **Before building, look up the cell.** Every new idea must declare its cell (row = what arithmetic it uses, column = what object) and cite the id of the nearest route of that cell.
2. **If the cell is ■ or ◩, the idea must name which wall W1–W12 (§3) it evades and why.** If it does not, it is not built.
3. **If the cell is ◧, start from the live residual listed.** Do not open a route parallel to one that already exists.
4. **Every route must pass the §4 falsifier battery** (at minimum DH, deletion, κ/finmod, Beurling DMV, Λχ₂ and the Type I curve) *before* a proof is written.
5. When the round closes, update the JSON and this map (§8).

Legend: **■ PAINTED** (all routes dead, no live residual) · **◩ DEAD WITH RESIDUAL** (dead, but a precise residual survives, usually of RH strength or not yet formulated as a route) · **◧ OPEN** (a live OPEN/PARTIAL route exists that no later phase surpassed) · **□ EMPTY**.
Criterion: an OPEN route from an early phase that a later phase killed **does not count as live**. Cross-checking was done by name and id between parts; doubtful cases are marked "NOT CONFIRMED".
Rows: 1 identity/EF · 2 positivity/support · 3 quantitative estimation · 4 Euler product · 5 ℤ-integrality · 6 exact values of Λ · 7 zero side/explicit formula · 8 arithmetic-free.
Columns: A form of a window · B contact kernel vector (linear in F) · C quadratic/higher functionals · D spectrum · E flow/family in T · F global transforms in T · G families of L-functions/fields · H geometric/dynamical objects.

## 1. The refined grid (symbol + number of routes in the JSON)

| row \ col | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 identity/EF | ◩ 22 | ◩ 19 | ◩ 13 | ◩ 11 | ◧ 11 | ■ 11 | ◩ 8 | ◧ 28 |
| 2 positivity/support | ■ 39 | ■ 12 | ◩ 10 | ■ 12 | ◧ 10 | ◩ 5 | ◩ 10 | ◧ 24 |
| 3 estimation | ◧ 46 | ■ 4 | ◩ 8 | ◧ 22 | ◧ 17 | ◧ 14 | ■ 6 | ■ 5 |
| 4 Euler | ◧ 27 | ◩ 22 | ◧ 24 | ◩ 20 | ◧ 26 | ◧ 18 | ■ 13 | ◧ 29 |
| 5 ℤ-integrality | ◩ 6 | ■ 4 | ◩ 2 | ◩ 4 | ◧ 4 | ◩ 8 | ◧ 29 | ◧ 26 |
| 6 Λ values | ◧ 21 | ◧ 17 | ■ 15 | ■ 4 | ◧ 5 | ◧ 11 | ◧ 3 | ◧ 8 |
| 7 zero side | ◩ 55 | ◩ 13 | ■ 7 | ◧ 25 | ◧ 17 | ◩ 29 | ■ 1 | ◩ 19 |
| 8 arithmetic-free | ◧ 23 | ◩ 15 | ◧ 7 | ◧ 37 | ◩ 22 | ◩ 7 | ◩ 9 | ◧ 101 |
**Count (after part 19, phases 168–184):** ■ 13 · ◩ 23 · ◧ 28 · □ 0; 1100 routes. Part 19 (78 entries from phases 168–184, source INVENTORY-PHASES-168-184; phase 170 in 12 consolidated entries per R184_002) applies the R162_2300_REPAINT_PROPOSAL proposal in 8 cells: **2A, 6C ◩ → ■**; **2G, 4D, 7A, 7B, 7F, 7H ◧ → ◩**. Unchanged (no citable proof, proposal §3): 1E, 2E, 6B, 6G, 8D. No cell moves up. Row D OPEN; no statement label changed.
**Count (after part 18, phase 166 rounds 9–12 and phase 167):** ■ 11 · ◩ 19 · ◧ 34 · □ 0; 1022 routes. Part 18 (13 entries) changes one symbol: **7C ◩ → ■** (R166_801, second moment over translations, DEAD [E1/f_t]; the "non-linear functional with pair correlation as exact input" residual, §6 item 46, is now DONE negatively). 7B gets the Thm A tool from R166_501 ((iii) ⇒ (ii)) and the meta-residual O166.501.1; 6C gets R166_502 (P7+Q25, REPEATED); 4F gets R166_601 (rough zeta, DEAD [E1]); 5G gets R166_701 (θ = 0, NO-GO as a route to D; residuals C1/C2) with tools T3/T4 and R166_702 (position/replacement, DEAD; Lemma PT); 3A gets R166_802 (inequality over Λ, DEAD circular) + tools R166_802T, R167_101 ((WS*), tool; residuals O166.802.1 and (WS*)), R167_102 (sieves, DEAD [W-sieve]) and R167_291 (Lemma K downgraded); 3G gets Theorem S (R167_103); 7D gets O167.101.1–2.
**Count (after part 17, phase 166):** ■ 10 · ◩ 20 · ◧ 34 · □ 0; 1009 routes. Part 17 (12 entries) changes no symbol: 7A gets R166_101 (DEAD [E1]; tool Thm 2.1) and R166_201 (DEAD [E1]; jet-hierarchy tool Thm 1.3, Cor 1.4, Prop 2.2); 7E gets R166_102 (flow in s, DEAD [W2/M]) and R166_201E; 7F and 1F get the duplicates R166_102F/102I [W2/M]; 6C gets R166_103 (α) and R166_202 (OS-2 **CLOSED** negatively; the OS-2 residual is replaced by O202.1, T_e = T_o with no sign; 6C remains ◩); 4F gets R166_103 (β) DEAD and the tool R166_103T (split 𝒯^det + ζ_{≥X}); 2F gets R166_103 (γ) DEAD with the falsifier P_{a,c}; 2A gets R166_201S (atomic sampling, ψ-blind).
**Count (after part 16, phase 165):** ■ 10 · ◩ 20 · ◧ 34 · □ 0; 997 routes. Part 16 (8 entries) changes no symbol: 7A gets Det+ (R165_101, PROVED-TOOL), Det− (R165_102, DEAD: false for large δ*Λ*, contact = min_ρ T_det), "interlacing ⇒ quartet off the cone" (R165_201, DEAD by Thm 3(a)) and "contact ⇒ EC" (R165_202A, DEAD); its D.16-γ residual is now DONE negatively and is replaced by ω(E) at contact = Rem 4.8a; 7D gets Det+ and Thm 1/Cor 2(c) as tools and residuals O102.1, O102.2, O701.1–3; 7E gets R165_202 (node flow, PARTIAL/E1); 2A gets Prop 4/Cor 2 of R165_102.
**Count (after part 15, rounds 3–4 of phase 164):** ■ 10 · ◩ 20 · ◧ 34 · □ 0; 989 routes. Part 15 (9 entries) changes no symbol: 7A gets R164_501 (sinc on the zero side, DEAD [E1, no room]; tools Thm SA, Cor SA.1); 7F gets the Prop 4 tool (R164_501P) and R164_601 (dlVP over G², DEAD [W2/M + Thm 3.1]; O164.501.1 CLOSED; residual O164.601.1 = (★_cell) weighted by K); 4A/4E/8D get R164_502 (moments, det/heat trace, Szegő–Widom, DEAD; tools L4, L5, L6); 5G gets R164_503 (Goal B ≥ RH + quadratic GRH, prime-ceiling rounding at x^{1/2} ARGUED; O164.503a–d); 2A gets Props 1.1/1.3 (R164_601T); 4F the R164_491 audit (fixes applied).
**Count (after part 14, rounds 1–2 of phase 164):** ■ 10 · ◩ 20 · ◧ 34 · □ 0; 980 routes. Part 14 (5 routes) changes no symbol: 4F gets R164_101 ((KZ), DEAD [E1]), R164_102 (positive tail, DEAD [Thm A]), R164_402 (superseded) and the tool R164_401 (**Thm R**: O164.101 ⟺ ¬RH, witness class = {ζ}, wall W-identification); 4F remains ◧ because of its previous residuals (GAP-157.A, O2802.1, generating object). 5G gets R164_201 (Theorem L PROVED after audit R164_291): O163.803a / L2a **CLOSED NEGATIVELY** in 𝒦_θ, replaced by **O164.201a** (off-lattice, ARGUED); 5G remains ◧. New wall **W-identification** (§3).
**Count (after parts 12–13, rounds 31–37 of phase 163):** ■ 10 · ◩ 20 · ◧ 34 · □ 0; 975 routes. Part 12 (5 routes: R163_201a–c, 202, 203; audit 290) records the Euler gate (modes K_F(1+2πik/log p)) as a circular NO-GO (4B, 5G). Part 13 (17 routes: R163_401, 402, 501, 502, 601, 602, 603, 701, 702, 801, 802, 803, 901, 1001a–c, 1001O; audits 490, 590/591, 790, 891/892, 991 in the notes) raises **7B** from ◩ to ◧ (R163_401, closure candidate with the gap (★_cell) ⟺ RH at the witness; tail form (TC) in R164_000) and changes no other symbol. **5E and 5F:** the R163_1001 routes (deformation; theta periodicity; windowed Hamburger) end up DEAD [E1 + W3′], but R163_1001 §7 says it does not touch the live residuals O1802.3/O2802.1 (5E) or O2302.1/2 (5F); by rule §8.3, 5E remains ◧ and 5F remains ◩. 1G: residual sharpened to "degree-one GRH, uniform in χ" (Thm O.2). 5G: Theorem C (R163_803) closes O163.101a for θ∈(1/3,½); BF_θ^disc remains at θ≤1/3. New wall **W3′** (§3); new falsifiers **f_χ** and **f_t** (§4).
**Count (after parts 10–11, round 29 and phase 163):** ■ 10 · ◩ 21 · ◧ 33 · □ 0; 953 routes. Part 10 (4 routes: R162_2901, 2902a–c) closes O2801.1 in 4F (Thm A/B NO-GO; residual = integrality of dN), does P2 in 6D (◧→■, Λ-blind structural identity) and lem:degen in 6A (PARTIAL, missing log 2). Part 11 (13 routes from phase 163: R163_001, 003a, 002a/b, 101a–d, 102a–d and the cited tool 191a; audits R163_190 and R163_191) opens 5G (■→◧) with the **Beurling frontier**: ζ_θ (Broucke's own system, §6.1; CITED, not new) answers YES to BF_θ in the extended class ∀θ∈(0,1), so the class branch is false; only **BF_θ^disc** survives (discrete systems, θ<θ₀≈1/3), which is the sharpened form of O2601.1. **Audit R163_191:** nothing WRONG; the K(y) bound from random rounding is a SKETCH (the construction remains PARTIAL, C_{1/3} conjectural); Révész 2207.00665 Obs. 7 (via Hilberdink 2010): in discrete systems θ<½ forces zeros with β>θ (an integrality-over-zeros result, compatible with RH); Thm T requires ρ>0; root substitution sup|R|≈2.00. 7F gets the canonical exchange + D_test (tool) and property 2 ⟺ RH (E1); 5F the support lemma and the falsifier K.
**Count (after part 9, rounds 27–28):** ■ 10 · ◩ 21 · ◧ 33 · □ 0; 936 routes. Part 9 (6 routes: R162_2701, 2702a–c, 2801, 2802; audit 2890) closes residual O8 of 4E (Tate 2×2, W12), doc 107 of 4C (closed by 108) and NG-D4 and B_CCM of 1D (◧→◩; Λ-free invariants). **Audit R162_2890:** the (2,2) deficiency of the 2702 boundary triple is WRONG ((4,4), limit circle at ±∞): the tool remains "to be redone" and is 1D's residual; 2701's phrase "the phase-61 index was an artefact" is replaced by "not certified; index 0 after normalizing". 4F gets O2801.1 and O2802.1 (the second one also in 5E, row 5). **8D returns to ◧** by the §8 rule: it has 4 unsurpassed PARTIAL/OPEN routes (phase-37/110, 35/99, 63 F9, R160_010), which part 8 had not accounted for. All residuals converge to O2601.1, with the sub-forms O2801.1 and O2802.1.
**Count (after part 8, rounds 25–26):** ■ 10 · ◩ 21 · ◧ 33 · □ 0; 930 routes. Part 8 (10 routes: R162_2501, 2501a/b, 2502, 2502a, 2601a–c, 2602a/b) lowers 8F and 8D from ◧ to ◩ (common residual O2601.1); 4D remains ◧ only because of the exclusion conjecture (= C_B → O2601.1); the R161_068–070 residual is folded into R162_1603 (d). **Convergence:** 8F, 8D and O2501.1 reduce to ONE lemma, O2601.1.
**Audit R162_2590 (round 25):** nothing WRONG; both NO-GOs stand. 2501 Prop 1 (upper bound) repaired, 2β* law holds; M_m correct (2m conjugate pairs); Thm 3 changes O(mT) to small T; Prop 3 E restricted to quartet type; 2502 Thm K only "(4.1) at least as strong as Gate 1".
**After part 7:** ■ 10 · ◩ 19 · ◧ 35; 920 routes. Before part 7: ■ 10 · ◩ 15 · ◧ 39. Part 7 (10 routes: R162_2201a–c, 2202a–b, 2301, 2302, 2401a–b, 2402) lowers 8B, 5C, 6C and 5F from ◧ to ◩; 5H remains ◧ (only the o-minimality/Pila–Wilkie residual dies). Before part 6 it was ■ 15 / ◩ 19 / ◧ 29 / □ 1; R162_2200 gave 41 ■ / 8 ◧ / 15 □. Part 6 (309 entries, 308 new) reopens 1D, 2E and 6E (■→◧), lowers 1C and 2C to ◩, raises 3F, 4C, 4F, 6G, 6H and 7D (◩→◧), and fills 5F (□→◧).
**Round 22 audit corrections R162_2290:** both NO-GOs stand. 2201: Thm N3 is FALSE as a theorem about "all the consequences" and is downgraded to a *proposition* about the three routes it lists (F6); Thm N1(a) carries a factor of 2 and N1(b) is only ⟹. 2202: Thm NI correct (only n<e^{T_c} enter); Thm ND needs the ι-invariance hypothesis of Thm R (F12); the example in Prop T is false (partial sums of Z with real zeros, F11).
**Reading warning:** "◧" means *something remains unclosed*, not that there is a promising route. Most of the ◧ in columns A/E/H are unbuilt objects or pending audits, and many will fall into E1. The ranking in §7 is what decides.
Late corrections incorporated (README and part 6): the certificate at ½log5 **is already done** (R162_303/391 primitive and R162_703/791 complete, λ_A, λ_W>0 on (0,½log5], with Arb and complete audit reruns). **It is independent of the old D.172 certificate (114),** which S3 records and which was downgraded/retracted. Other corrections from part 6: the killer of R161_016 is F2, not F1. R161_075 says that the general exclusion by linear limit of R161_018 is "unproved as written". The factorization no-go of R161_069 was corrected by R161_070, so it is not a no-go. R161_030–081 were missing from R162_2200: the Γ–Euler detector 068–074 (partly open), weak renormalization 075–079 and the sign test 081. the R-C separation (1701) does not isolate arithmetic (2101); the two-atom Type I curve (2001, verified by 2190, s₂^c=0.9997678) kills R-C.b blind to weight.

## 2. Cells in detail

Format: status, number of routes by status, killers of DEAD routes (count), dead ids (no duplicates), duplicates, tools and **live residual**. The full text of each route is in the JSON.
**1A** ◩ (identity/EF × form of a window) — 22 routes: DEAD 18 · OPEN 2 · PARTIAL 2
  killers: E1×11, OTHER×7, F3:Xi_a×1, F4×1
  dead: phase-0/0A3; phase-16-surf-witness-variety/07-09; phase-33/82,85; phase-35/99; phase-46/137; 136 PHASE_136 S6; 138 R138_005 D.15; 155 cor:Li; P08 main.tex; P46 §3-5 D.1-D.3; (+6)
  duplicates: phase-5/B3.2; phase-29-zeta-spectral-triples/50
  → live residual: λ_W>0 beyond ½log5 (P47 Open 5): certificate, not mechanism; clashes with M
  → live residual: Conjecture C_B (34/91) → lives in 8F
  note: B3-KREIN and 34/91 absorbed by E1

**1B** ◩ (identity/EF × contact kernel vector (linear in F)) — 19 routes: DEAD 11 · OPEN 1 · PARTIAL 2 · PROVED-TOOL 5
  killers: OTHER×4, F2×2, F1×2, E1×2
  dead: 121 P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT; R162_305; R162_402; R162_204; R162_1201; R161_008-011,017-018,022-023; R160_S2 F20 phase-66; R160_S3 §2.2#13 phase-110; R160_X_C1; R161_008-010
  duplicates: R161_011
  tools: 121 P121_GRAPH_RENORMALIZED_INCOMING_CURRENT; 121 P121_TATE_PORT_OPPOSITE_PARITY_RIGIDITY; R161_005-007; R161_017
  → live residual: R161_011 (4.2) global Sonin range (R161_011; R162_1201): E1 sink of columns B/C
  note: P121 current/collar = tools
  part19: R183_022 DEAD [E1]; R183_029 PROVED-TOOL

**1C** ◩ (identity/EF × quadratic/higher functionals) — 13 routes: DEAD 12 · PARTIAL 1
  killers: OTHER×7, E1×5, preserver arithmetic-b×1, F3×1
  dead: phase-11-hyperbolicity-total-positivity/M11.2-5; phase-28-four-fronts/04-06; phase-28-four-fronts/07-08; phase-101/E101_061,070; 122 P122_005; 161 R161_002; R162_1003; R160_S1 §2.4#20 phase-28-four-fronts; R160_S5 §2.4#30 G2_B3_R1; R161_022-023; (+2)
  → live residual: R161_020-021: scalar terminal objective X_T=½‖(I+εC_log)g‖², not realized from finite (PC-ren)
  note: formerly ■

**1D** ◩ (identity/EF × spectrum) — 11 routes: DEAD 10 · PROVED-TOOL 1
  killers: E1×4, OTHER×3, F3×1, W3×1
  dead: phase-61/O8; P20 main.tex; P31 main.tex; R162_1301; R160_S1 §2.5#35 phase-28-four-fronts/02 NG-D4; R160_S2 F13 phase-53/164; R160_S2 §3.2 phase-60 §4.B; R162_2702b; R162_2702c
  duplicates: R160_C2_R1
  tools: phase-64/C,D
  → live residual: redo the boundary triple of W_λ with (4,4) deficiency (2890; RH-neutral tool, not a mechanism)
  → live residual: O2702.1: comparison with Burnol (RH-neutral)
  note: part9: NG-D4 DEAD (2702c, index count); boundary triples/B_CCM NO-GO for O2601.1 (2702b, Λ-free invariants, W3) but the (2,2) deficiency calculation is WRONG (2890: (4,4), limit circle at ±∞); formerly ◧

**1E** ◧ (identity/EF × flow/family in T) — 11 routes: DEAD 7 · OPEN 1 · PARTIAL 3
  killers: E1×7, F3×1, DH×1
  dead: phase-25-lower-bounds-bj-audit/02-03; phase-30-langlands-bridge-c-infinity/57; R162_1802; R162_902; R160_S2 F19 phase-65 RH-PROOF; R160_S3 §2.1#9 Papers 31/36/38; R160_S5 §2.4#40 G2_B5
  → live residual: Conj. A.15 (phase-28-four-fronts/01): Λ=max b_j²/2, monotonicity of the Kreĭn index under dBN, 0 later citations
  → live residual: D-109 critical anchor (37/109): falsifiable partition, no mechanism
  note: polarcap 156 → 703 (closed)

**1F** ■ (identity/EF × global transforms in T) — 11 routes: DEAD 10 · PROVED-TOOL 1
  killers: E1×6, F3:positive kernels wi×1, F3:positive even kerne×1, OTHER×1
  dead: phase-33/75,78; phase-33/81,84; phase-35/102; phase-103/103_15,29,39,42; phase-103/103_30; P47 KEP; R160_S3 §2.1#2 phase-102/174; R161_066-067; R161_080; R166_102I
  tools: R161_019/024-025
  note: 2200 gave it □; it has 6 DEAD [E1/F3] routes; part17: R166_102I DEAD [W2/M]

**1G** ◩ (identity/EF × L-function/field families) — 8 routes: DEAD 6 · PROVED-TOOL 2
  killers: T1×2, OTHER×1, definite×1, E1×1
  dead: phase-16-surf-witness-variety/01-05; phase-30-langlands-bridge-c-infinity/55; 138 T1 equimodularity; 158 S₃ falsifier; R160_S4 §2.A#11 phase-138; R160_S5 §2.2#11 R158_004/006
  tools: P46 §18.1 T1; R163_1001O
  → live residual: converses/Hamburger as a sign mechanism in a family: sharpened by Thm O.2 (R163_1001) — would need to be degree-one GRH, uniform in χ (W9/T1)
  note: 2200 gave it □; part13: Thm O + f_χ (R163_1001O) tool, wall W3′

**1H** ◧ (identity/EF × geometric/dynamical objects) — 28 routes: DEAD 19 · OPEN 3 · PARTIAL 4 · PROVED-TOOL 2
  killers: OTHER×8, E1×7, F2×2, symmetry not positivit×1
  dead: phase-17-surf-2-design/SURF-A,B; phase-108/108_17,38,50-55,91; phase-110/110_99; 122 P122_018; 158 R158_005; 159 G1_B3_R1; P46 §11-12 D.6-D.8; 03-research/THE_BACKWARD_MAP §5-7; R162_1002; R162_1203; (+7)
  tools: phase-111/111_99; P43 main.tex
  → live residual: P122_D_SPECIFICATION: relative correspondence E_(∞,T) Bohr↔quarter-Γ Calderón (L6), never built
  → live residual: P25 V.2: Pontryagin completion with characters x^{b+iγ} (bridge κ(Q)=ind₋ H_C)
  → live residual: P152.1 Dolgopyat for Mayer via Lewis–Zagier (only desk EXCL in 157)
  part19: R168_202Q DEAD [W-identification]; R183_031 DEAD [W-Sonin]

**2A** ■ (positivity/support × form of a window) — 39 routes: DEAD 29 · PARTIAL 3 · PROVED-TOOL 7
  killers: OTHER×14, E1×4, F3:comb models×2, Φ combs×2
  dead: phase-33/83,86,89; phase-35/103 +38/114; phase-46/142+47/145; P43 Thm 14.1; 138 D.16-17; 155 thm:SC; 156 R156_005 cor:convfail; arcs I,VIII; phase 155 prop:archneg; R162_1603; (+10)
  duplicates: R160_S2 F35 phase-47/145; R160_S3 §2.2#19 115_08/10
  tools: phase-4/B2-THEOREM; phase-45/134; P18 main.tex; P47 thm:C, thm:log5W; R160_S1 §3a#35 phase-35/100; R164_601T
  → live residual: semilocal global CC (phase-5/B2) — not run; coincides with PATH-TO-D (ii) in 8D
  → live residual: 115_13-16 semilocal Sonin trace-phase derivative: favorable sign, no exact identity exists
  note: P35 L1 = ε₀≥0 (E1); part15: Props 1.1/1.3 of R164_601 tool; part16: Prop 4/Cor 2 of R165_102 tool; part17: R166_201S atomic sampling DEAD [Cor 1.4, ψ-blind]
  part19 (repainted ◩→■, proposal): R183_008 DEAD [W12]; R183_016 DEAD [W12]; R183_019 DEAD [W-Sonin;W12]; R183_027 DEAD [F3:low band;E1]; R183_030 DEAD [E1]; R184_003 DEAD [W12]; R184_015 DEAD [W11′;F3:M_m;E1]. Residual: none

**2B** ■ (positivity/support × contact kernel vector (linear in F)) — 12 routes: DEAD 10 · PARTIAL 1 · PROVED-TOOL 1
  killers: OTHER×3, F1×2, F3 (κ)×1, F3 (DH)×1
  dead: phase-109/109_99; 124 P124_009-010; R162_101; R162_103; R162_405; R162_407; R162_703; R160_S2 F53 phase-64 FACE-C; R160_S3 §2.2#18 phase-119; R161_071-072
  tools: R161_014-015
  note: 60 CCM: last link ε₀≥0 ⟺ RH

**2C** ◩ (positivity/support × quadratic/higher functionals) — 10 routes: DEAD 7 · PARTIAL 2 · PROVED-TOOL 1
  killers: OTHER×4, F2×2, E1×2, Baker no-go×1
  dead: 159 G2_B3; 159 G2_B4; P41 main.tex; R161_027-029; R160_S2 F39 phase-48/153; R160_M10_R1
  tools: phase-65/D6
  → live residual: P41 thm:doob: non-local corridor with sign, never executed (E1: RH ⟺ a sharp Poincaré)
  note: formerly ■; R161_026-028 F3 (Λ≥0 is not enough)
  part19: R168_203 DEAD [E1;E70_12]

**2D** ■ (positivity/support × spectrum) — 12 routes: DEAD 12
  killers: OTHER×5, E1×1, F3 (DH v_n≥0 line)×1, F3 (κ)×1
  dead: phase-29-zeta-spectral-triples/51; phase-62/E94-E96; phase-102/118; phase-106/106_58,59,61,62,67,70; P22 main.tex; R162_504; R162_702; R162_1601; R162_1803; R160_S2 F14-F16 Paper 18; (+2)

**2E** ◧ (positivity/support × flow/family in T) — 10 routes: DEAD 5 · OPEN 2 · PARTIAL 2 · PROVED-TOOL 1
  killers: E1×2, F3×2, OTHER×1, F3:DH×1
  dead: phase-64/FACE-C; phase-65/RH-PROOF; R162_802; R162_1402; R161_029
  → live residual: prop:polarcap: polar capacity 𝔊_T as a function of T (S^Sch≈−J), never analyzed in T; follow-up D3 of M4 never run
  → live residual: P47: effective window shift RD_{T′} ⟹ λ^W_T≥0 (at comb level requires T′≥T*_{∞,P})
  note: formerly ■
  part19: R184_012 PROVED-TOOL

**2F** ◩ (positivity/support × global transforms in T) — 5 routes: DEAD 5
  killers: OTHER×3, E1×2, integral W_lambda dm=0×1, Falsifier P_{a×1
  dead: phase-102/115,116; phase-102/117; P24 main.tex; 03-research/AUDIT_CONSOLIDATED §4; R166_103G
  → live residual: full monotonicity / Bernstein of λ_A(T) or of its transform as a global object (2200)
  note: 2200 gave it □; 4 DEAD routes; part17: R166_103 (γ) DEAD [falsifier P_{a,c}]

**2G** ◩ (positivity/support × L-function/field families) — 10 routes: DEAD 6 · NO-GO 2 · OPEN 1 · PARTIAL 1
  killers: OTHER×3, T5×2, summand vs numerator×1, Beurling×1
  dead: phase-15-arithmetic-hodge-index/M3-attempt6; 151 R151_005 T6; Paper 46 T5 (phases 141-149); phase 150 T3; R160_S4 §2.B#22 P46 T5; R160_S4 §2.B#24 phase-151 T6
  → live residual: P46 §28.4: six-clause object over the adelic square — no candidate built
  → live residual: T3 Beurling (150): conditional on H-DMV, already CITED (157)
  part19 (repainted ◧→◩, proposal): R173_FINAL NO-GO [W10;E1]; R174_FINAL NO-GO [W10]. Residual: six-clause object of P46 §28.4 with no live candidate (W10)

**2H** ◧ (positivity/support × geometric/dynamical objects) — 24 routes: DEAD 18 · OPEN 4 · PARTIAL 1 · PROVED-TOOL 1
  killers: OTHER×9, E1×7, F3:function-field×1, one ray refutes every×1
  dead: phase-14-off-diagonal-anchor-asymmetry/ANCHOR,STAGE1-2; phase-15-arithmetic-hodge-index/M3 + attempts 1-8; phase-33/80; phase-40/124; phase-42/127; phase-101/E101_083; phase-112/112_99; 122 P122_007; 148 R148_005; 160 C5/C6/C7; (+8)
  tools: phase-15-arithmetic-hodge-index/M1-M2
  → live residual: phase-15-arithmetic-hodge-index/M10: Arakelov witness variety 𝒳 (not built)
  → live residual: PHASE_136 S5: tropical Hodge index of Cartwright at the chart level (never run)
  → live residual: S1 I1: interlaced (not product) OS model of the whole W_T, never attempted
  → live residual: Chinburg–Rumely: energies outside 𝔄⁺ (Berkovich kernels), not read
  part19: R174_TC OPEN

**3A** ◧ (estimation × form of a window) — 46 routes: DEAD 29 · OPEN 7 · PARTIAL 3 · PROVED-TOOL 7
  killers: OTHER×11, E1×6, M×4, F3:finmod×3
  dead: phase-3/phase3-plan; phase-14-off-diagonal-anchor-asymmetry/N8; phase-25-lower-bounds-bj-audit/01; phase-36/104; phase-116/README; phase-117/README; 122 P122_019-021; 153 R153_014-021; 155 thm:finmod/cor:void; arcs I,X; (+17)
  duplicates: R160_S3 §5#15 D.198-227; R166_802T
  tools: phase-0/0B; 150 T4; 159 G2_B6_R2; P16 main.tex; R160_S5 §2.4#37 G2_B6_R2 Thm M; R166_802T
  → live residual: P47 Problem A: class-dependent lower bound (only ceilings proved)
  → live residual: R154_030: two-prime window at 0.58, off-machine package (numerical; not a route)
  → live residual: S1 (141.G1/199): per-window arithmetic beyond Montgomery–Vaughan — ceiling 172.9, ancestor of M
  → live residual: S5 §5#14: unread web hit "Certified Weil positivity beyond the unit window"
  → **:** residual S5 §5#14 READ (AUDIT_LIU.md): Liu (alphaXiv, under review at Math. Comp., not peer-reviewed, certificate not yet publicly reproducible) gives W_T ≥ 2^−151 at T ≤ 1 and ≥ 2^−49162 at T ≤ 17/16 (half-width = T); by monotonicity and λ^W ≤ λ^prim ≤ λ_A, λ_A > 0 on (0,17/16] — CITED, integrated into Paper 47 (rem:liu). Constants with double-exponential collapse: a window record, not a method. 3A's symbol unchanged.
  → live residual: I6 (36/108): negative-block dimension bound under resolution
  → live residual: O166.802.1: extension of circularity to arbitrary non-linear B (tied to O166.501.1)
  → live residual: (WS*) (R167_101): single-scale polylogarithmic one-sided bound on Re Σ_{n≤Y}Λ(n)n^{−½+iγ_q}w(log n); unreachable by sieves (Thm B′), uniform ⟺ zero-free (Thm C), at one scale = explicit formula (Thm E)
  note: 114/D.172 (old ½log5) DOWNGRADED; the 162 certificates at ½log5 (303/391 primitive, 703/791 complete; Arb, complete audit reruns) are independent of D.172; part18: R166_802 inequality over Λ DEAD [circular]; R167_102 sieves DEAD [W-sieve]; R167_291 Lemma K downgraded; tools R166_802T, R167_101
  part19: R184_007 DEAD [W4;W11]; R184_009 DEAD [W-sieve;(N′)]

**3B** ■ (estimation × contact kernel vector (linear in F)) — 4 routes: DEAD 2 · PROVED-TOOL 2
  killers: OTHER×2, two refuted routes×1, F1×1
  dead: phase-61/OPEN-PROBLEMS O5,O11; 124 P124_004-008
  tools: R162_001/190; R162_407 rate
  note: continuity of λ_A and the 407 rate = tools

**3C** ◩ (estimation × quadratic/higher functionals) — 8 routes: DEAD 5 · PARTIAL 3
  killers: E1×3, OTHER×2, F3:M_m (no line of the×1, W3′/F3:f_χ (Riemann–Si×1
  dead: phase-58/188+59/191,193,197; R160_S1 §2.2#14 phase-36/108; R160_S1 §2.6#36-39; R160_M7_R1; R163_603
  → live residual: Option 3 of R160_020: T-uniform-sign bound of the low-frequency block outside the contact vector (M7 Prop 5.2(c) suggests E1)
  note: C_D (34/93) unsupported

**3D** ◧ (estimation × spectrum) — 22 routes: DEAD 13 · OPEN 2 · PARTIAL 3 · PROVED-TOOL 4
  killers: OTHER×9, E1×1, F4×1, F3:DH×1
  dead: phase-9-unconditional-universality/T9A; phase-23-two-scale-defect-structure/24; phase-31-selberg-moments-c-infinity/58; phase-37/111; phase-86/PHASE_86_CLOSURE; phase-101/E101_024,027; 159 G1_B8; 159 G2_B10; P11 main.tex; P28/P29 FormB; (+3)
  tools: phase-9-unconditional-universality/T9cal; phase-32/65-68; phase-47/146; 155 cor:H1 / (H1)
  → live residual: GAP-196.A: near-doubles of Λ_f from DH under mean spacing (never attacked)
  → live residual: 22/03 GMC rigidity (conditional)
  note: LP-134 dies at scale 1/log T

**3E** ◧ (estimation × flow/family in T) — 17 routes: DEAD 10 · OPEN 2 · PARTIAL 1 · PROVED-TOOL 4
  killers: OTHER×6, M×3, finite heat-order wall×1, same exponent as densi×1
  dead: phase-12-meta-obstruction-moment-problem/M12.1-9; phase-55/175+56/181; phase-101/E101_033,037; phase-106/106_98-120; 155 thm:margin; P28 main.tex FormC; 159 G2; R160_S2 F43 phase-54/172; R160_S4 §2.D#49 P47 thm:margin
  tools: phase-54/170; P32 main.tex; R160_S2 §3.1 phase-54/167,170
  → live residual: GAP-157.A: Kronecker-flow discrepancy (2 of 3 routes dead; central implication undecided)
  note: Tower 1: A ⟹ Lindelöf; Dic undetectable (198.2)
  part19: R168_102 DEAD [single-height wall;F3:generic Beurling]; R169_091 PROVED-TOOL

**3F** ◧ (estimation × global transforms in T) — 14 routes: DEAD 10 · OPEN 1 · PARTIAL 2 · PROVED-TOOL 1
  killers: OTHER×10
  dead: phase-58/189+59/194; phase-102/167,170,171; phase-102/221,223,232,241,250,257; phase-102/270,281,290,300,310,328; phase-102/294,311,314; phase-103/103_05; phase-103/103_24,25,26; phase-104/104_101-116; phase-104/104_27,95; phase-105/105_04,05
  tools: phase-102/102_A0_UNIFORM_TAIL_THEOREM
  → live residual: GAP-157.A non-local Tauberian with LI input (F40; Beurling–Malliavin over p^{iτ})
  → live residual: rem:Dgrade: union of graded and tail techniques
  note: A1 = RH strength; formerly ◩

**3G** ■ (estimation × L-function/field families) — 6 routes: DEAD 3 · PROVED-TOOL 3
  killers: E1×2, T5×1, F1×1, F2×1
  dead: P46 §26; R162_1004; R160_S4 §2.B#23 P46 27.10-11
  tools: 150 R150_005 T5; P46 §27; R167_103
  note: ; part18: Theorem S (R167_103) tool; DMV/Zhang sieve-proof falsifier

**3H** ■ (estimation × geometric/dynamical objects) — 5 routes: DEAD 5
  killers: OTHER×3, no mechanism×1, all three converge on×1, signed cone maximally×1
  dead: 152 R152_005 A; P01 main.tex; P46 §17; phase 152; R160_S4 §2.C#25-26 phase-152

**4A** ◧ (Euler × form of a window) — 27 routes: DEAD 19 · OPEN 3 · PARTIAL 2 · PROVED-TOOL 3
  killers: OTHER×9, F2×3, E1×2, unsigned at every char×1
  dead: phase-6-osterwalder-schrader-reflection/M-OS-2; phase-6-osterwalder-schrader-reflection/S2-followup; phase-7-weil-carleson-sine-kernel/P7-OPEN-CORE; 122 P122_028; P44 Thm 8bis.4a; 159 G2_B1; 03-research/AUDIT_CONSOLIDATED §4; R161_001-004; R162_203; phase 153 Thm A; (+8)
  duplicates: phase-47/148; R161_001-002
  tools: 143 D.34.5; P09 main.tex; R160_S4 §3.1 Theorem C / D.12-alpha / Theorem A
  → live residual: GAP-135.A / doc 148: incommensurate frames (Seip, Olevskii–Ulanovskii), never taken up again
  → live residual: 159 G2_B8 Thms L,L′,L″,D: local Euler threshold ½log3≤T_loc≤0.5925, unaudited
  → live residual: Paper 44 (H_L): negative primitive in Dirichlet profiles
  note: ; part15: R164_502 moments/Selberg DEAD [W3, L1/L6]

**4B** ◩ (Euler × contact kernel vector (linear in F)) — 22 routes: DEAD 14 · NO-GO 2 · PARTIAL 3 · PROVED-TOOL 3
  killers: OTHER×7, E1×3, F3:Xi_a×2, no sign×1
  dead: phase-36/108; phase-91/E91_004; phase-94..100/closures; phase-102/119; 121 P121_CAUSAL_REES_HALF_LIFT; 146 R146_005; R162_201/202; R162_301; R162_503; R162_404; (+3)
  tools: phase-93/E93_002; R163_201a
  → live residual: distributional carrier (83–84, ker X=span δ₀) not excluded by the domain obstruction
  → live residual: minimal cut A1–D3 (phase 80) — the anchor is ⟺ RDI (93, E1)
  part19: R170_201 PROVED-TOOL; R182 DEAD [W12;circular]

**4C** ◧ (Euler × quadratic/higher functionals) — 24 routes: DEAD 14 · OPEN 5 · PARTIAL 3 · PROVED-TOOL 2
  killers: OTHER×4, F2×3, E1×2, r averages to 0×1
  dead: phase-36/107; 160 M7/M8/M9; P03 main.tex; R160_M8; R162_207; R160_020 Option 6; R160_S1 §5 I7 phase-36/107; R160_S2 F54 phase-70/E70_10; R160_M8_R1; R161_033-034; (+2)
  tools: phase-57/183; R162_502 B2
  → live residual: L5 (114): Z_{N,ε} with R=Z*Z, no pseudo-inverse, never built
  → live residual: G2_B3_R5 Cor S2: Hecke-type algebra on L²(ℝ) with archimedean multipliers (coupled square), no candidate
  → live residual: R160_020 Option 6 (Meyer S+D): never run; D2 declares it sterile
  → live residual: R161_030-032: source of the open oriented-variance gate
  note: part9: doc 107 / W_2 CLOSED by doc 108 (R162_2702a, W2+E1; not MW-7)
  part19: R177 DEAD [F3:fibers of cardinality 1]; R178_O OPEN; R181 DEAD [F3:quotient comb]

**4D** ◩ (Euler × spectrum) — 20 routes: DEAD 15 · OPEN 1 · PARTIAL 1 · PROVED-TOOL 3
  killers: OTHER×11, E1×3, LI of log p gives no m×1, no form/K3×1
  dead: phase-35/100; phase-81/PHASE_81_CLOSURE; phase-83/E83_008; phase-85/PHASE_85_CLOSURE; phase-89/PHASE_89_CLOSURE; phase-106/106_00; P12 main.tex; R152_002; 159 G1 K3; R160_S1 §2.1#5 phase-35/100; R160_S2 F17-F18 phase-64/106; (+3)
  tools: phase-114/D.244; P10 main.tex; R162_2502a
  → live residual: Exclusion conjecture (21/01-02): all on the line or infinitely many off it — it is C_B, converges to O2601.1
  note: part8: Γ–Euler detector R161_068-070 NO-GO (R162_2502 Thm D/K, Prop A); residual folded into R162_1603 (d)
  part19 (repainted ◧→◩, proposal): R184_004D DEAD [F3:M_m;W3]; SUPPORT-DESCENT DEAD [E1;F3:scalar model q_T]. Residual: O2601.1: individual property of the Euler product, used non-linearly (no candidate; R184_099 §4)

**4E** ◧ (Euler × flow/family in T) — 26 routes: DEAD 15 · NO-GO 1 · OPEN 3 · PARTIAL 3 · PROVED-TOOL 4
  killers: OTHER×8, F2×1, log divergence×1, E1×1
  dead: phase-36/105; phase-70; phase-82/PHASE_82_CLOSURE; phase-87/PHASE_87_CLOSURE; phase-88/PHASE_88_CLOSURE; phase-101/E101_089,092,096; R160_S1 §2.4#23 phase-36/105; R160_S2 §3.2 phase-61 O8; R160_S5 §2.3#15 G1_B5_R3-R5; R160_M3_R1; (+1)
  tools: phase-13-omega-class-multiplicative-chaos/RESULT; phase-19-omega-rate-freezing
  → live residual: P30: L8 + LP-112
  → live residual: R153_005 Thm A cross term as a T-uniform sign mechanism (P153.2), never attempted
  → live residual: 90 PROJECTIVE-KATO-EULER
  note: part9: O8 Tate 2×2 CLOSED (R162_2701 NO-GO: Thm TC, Thm P, Thm I; W12); phase-61 index not certified, 0 after normalizing (2890); part15: R164_502 det/heat-trace DEAD [W12, E1]
  part19: R170_808 PROVED-TOOL; R170_841 DEAD [W5;F2]; R170_885 DEAD [W12]; R170_887 DEAD [W12;W5;E1]; R170_888 PROVED-TOOL; R176 DEAD [F3:DFT N=4]; SUPPORT-DESCENT-4 OPEN

**4F** ◧ (Euler × global transforms in T) — 18 routes: DEAD 9 · NO-GO 4 · OPEN 1 · PROVED-TOOL 4
  killers: E1×2, OTHER×1, W6×1, F:deletion×1
  dead: phase-103/103_16,17,19,20,21; R160_S2 F41 phase-50/158; R162_2801; R164_101; R164_102; R166_103B; R166_601
  duplicates: R164_402
  tools: R164_401; R164_491; R166_103T
  → live residual: GAP-157.A: condition C1 of Doc 159 (non-local Tauberian), neither known nor excluded
  → live residual: global generating object with Euler before regularizing (2200)
  → live residual: O2802.1 (sub-form of O2601.1, row 5): non-formal property, uniform in k≍log x, of the whole b≡1 book (Piltz up to k≍log x = ψ bound, E1 expected)
  note: part10: O2801.1 CLOSED negatively (R162_2901 Thm A/B NO-GO; residual = integrality/atomicity of dN, O2601.1); part14: R164_101 (KZ) DEAD [E1], R164_102 positive tail DEAD [Thm A], R164_402 superseded; R164_401 Thm R closes O164.101 by identification (O164.101 ⟺ ¬RH); other residuals untouched, the cell stays ◧; part15: audit R164_491 accepted (Thm R PROVED after F3/F1); part17: R166_103 (β) DEAD [Thm A/Cor R.1/Landau]; split 𝒯^det + ζ_{≥X} tool (B1–B2); part18: R166_601 rough zeta + Legendre DEAD [E1, tautology]
  part19: R169_101 NO-GO [W2;single object;NB]; R170_000 DEAD [E1]; R170-RES NO-GO [W12;W5;E1]; R184_002 PROVED-TOOL

**4G** ■ (Euler × L-function/field families) — 13 routes: DEAD 10 · PROVED-TOOL 3
  killers: OTHER×5, W8×2, T1/T2×2, F3:function-field×1
  dead: phase-14-off-diagonal-anchor-asymmetry/M14.1-3; phase-33/74; phase-48/153; 149 D.61; P46 §24; R162_1102; arcs III,VIII; 144-149; R160_S1 §2.5#33 phase-30-langlands-bridge-c-infinity/56; R160_S4 §2.B#20-21 phase-149
  tools: phase-5/M5,T1-T2; P05 main.tex; P46 §18.2 T2
  note: T2 tool
  part19: R168_201 DEAD [E1;W4]

**4H** ◧ (Euler × geometric/dynamical objects) — 29 routes: DEAD 20 · NO-GO 1 · OPEN 2 · PARTIAL 4 · PROVED-TOOL 2
  killers: OTHER×16, E1×3, F3:cross-root falsifie×1, T1×1
  dead: phase-67; phase-83/E83_003; phase-106/106_207-210; phase-107/107_00; phase-107/107_147-241; phase-120/P3 no-gos; 122 P122_009-010; 122 P122_013-017; 140 R140_005; 159 G1_B5_R3-R5; (+10)
  tools: 159 G1_B2_R3-R5; 159 G1_B4_R4
  → live residual: phase-27-adelic-rigidity: local-global adelic rigidity, walls A and B open (objects, not signs)
  → live residual: 36/106+38/117 amplifying functor ⊠ with corrections
  → live residual: Paper 44 Thm 8bis.4a: colimit L1 version of the pure Frobenius form
  → live residual: I11 (34/96): absorbing-channel torsion / symplectic curvature
  part19: R175_FINAL NO-GO [W10]

**5A** ◩ (ℤ-integrality × form of a window) — 6 routes: DEAD 4 · PARTIAL 1 · PROVED-TOOL 1
  killers: F2×2, OTHER×1, Θ(1/M) edge×1, E1×1
  dead: 155 thm:AL→AL′; R162_1902; R162_801; R163_901
  tools: 155 TK/N/N′
  → live residual: Problem A (P47) — same residual as 3A
  note: ; part13: R163_901 (f_t, Thm F) DEAD [F3:f_t]

**5B** ■ (ℤ-integrality × contact kernel vector (linear in F)) — 4 routes: DEAD 3 · PROVED-TOOL 1
  killers: E1×2, OTHER×1, F1×1, F2×1
  dead: phase-75+76; R162_701; R162_1101
  tools: R161_003

**5C** ◩ (ℤ-integrality × quadratic/higher functionals) — 2 routes: DEAD 1 · PARTIAL 1
  killers: F1×1, F2×1, OTHER×1
  dead: R162_2201b
  → live residual: O2201.1: asymmetric nodal weight = Z′/Z with a sign (zero side)
  note: part7: R162_2201b DEAD (FE + nodal symmetry erase the atoms); formerly ◧

**5D** ◩ (ℤ-integrality × spectrum) — 4 routes: DEAD 3 · PROVED-TOOL 1
  killers: OTHER×3, GAP-179.B no tool×1, 2m maps to 0×1
  dead: phase-50/158-159; 121 P121_CYCLOTOMIC_RESOLVENT_AND_LATTICE_AUDIT; 03-research/AUDIT_A §1 doc163
  tools: R163_201b
  → live residual: integrality in the spectrum: multiplicities / Smith form of the contact Gram (2200)
  note: 2200 gave it □; 3 DEAD routes

**5E** ◧ (ℤ-integrality × flow/family in T) — 4 routes: DEAD 1 · OPEN 1 · PARTIAL 2
  killers: E1 (a jump at t=0 ⟹ 0∈×1, Thm A.3)×1, decoupled invariants (×1
  dead: R163_1001a
  → live residual: O1802.3: width ≥0 of the residual window via NON-linear integrality in c, tracked in T (1902 closed only the linear case)
  → live residual: O2802.1 (sub-form of O2601.1; route in 4F): non-formal property, uniform in k≍log x, of the whole b≡1 book (Piltz up to k≍log x = ψ bound, E1 expected)
  note: part9: O2802.1 folds into row 5 (b≡1 integrality); part13: R163_1001a (deformation) DEAD [E1 + decoupled invariants]; the residuals O1802.3/O2802.1 are untouched by R163_1001 (§7), the cell stays ◧
  part19: R169_101E OPEN

**5F** ◩ (ℤ-integrality × global transforms in T) — 8 routes: DEAD 6 · PARTIAL 1 · PROVED-TOOL 1
  killers: F1×1, E1×1, OTHER×1, S7 Euler only via W7/z×1
  dead: R162_2302; R162_2601a; R163_002b; R163_1001b; R163_1001c
  tools: R163_002a
  → live residual: O2302.2: c_f≠0 from integrality (left outer Tate moment on the radical)
  → live residual: O2302.1: finite-N remainder (Li type, E1 expected)
  note: part7: R162_2302 Thm N (limit ≡0 via ζ(1−ρ)=0), Thm V; formerly ◧; part8: atomicity does not exclude E (2601a, falsifier Λ̃); part11: support lemma (R163_002a) tool, falsifier K (002b); part13: R163_1001b/c (theta periodicity, windowed Hamburger) DEAD [W3′ + E1]; residuals O2302.1/2 untouched
  part19: R169_102 DEAD [E1;T1]

**5G** ◧ (ℤ-integrality × L-function/field families) — 29 routes: DEAD 11 · NO-GO 3 · OPEN 2 · PARTIAL 1 · PROVED-TOOL 12
  killers: OTHER×3, χ=1 slot = 𝓔^∞×1, F3:zeta_theta×1, (N): N blind to zeros×1
  dead: phase-107/107_108-133; phase-107/107_134-139; 147 R147_005 D.55.9′; R163_101a; R166_701; R166_702
  tools: R162_2601c; R163_101b; R163_102a; R163_102b; R163_102c; R163_191a
  → live residual: BF_θ^disc, θ≤1/3 (sharpened by Theorem C of R163_803: for θ∈(1/3,½) discrete systems with zeros off the line exist): does every discrete Beurling system with N=ρx+O(x^θ), θ≤1/3, satisfy RH? (ℤ: θ=0). Line L2 of R164_000
  → live residual: O164.201a: discrete Beurling system off the Witt lattice with error O(x^{θ′}), θ′≤1/3, and a zero with β>½ (ARGUED that it must lie off the lattice, via L*)
  → live residual: O163.101b: discrete construction with Θ<1/3 and zeros off the line, or an integrality obstruction at θ<1/3
  → live residual: O163.101c: Révész Rem. 7 / Hilberdink 2010 (discrete θ<½ ⟹ zeros with β>θ, R163_191a) and Hilberdink 2005's exponent pairing: do they sharpen toward the line?
  → live residual: O102.1–3: non-lattice system with ρ=1; (BF_0) with σ_τ>½; Thm T modulo multiplicative cancellation
  → live residual: O164.503a–d (R164_503): quadratic-mean bound §3.3; Huxley exponent; non-rescaled θ<1/3 system; "returns to" clause §4.2
  → live residual: C1/C2 (R166_701): C1 every θ=0 system is ζ up to a finite Euler modification (OPEN); C2 there exists a θ=0 with a zero off the line (OPEN); T6: if C1, C2 ⟺ ¬RH
  note: part11 (phase 163): Beurling frontier; ζ_θ refutes the (extended) class branch; Lemma R, Thm R, Lemma S, Thm T/Cor F tools; analytic and perturbative NO-GO; formerly ■; part12: Euler gate (R163_202) NO-GO; part13: Theorem C (R163_803, audit 891 VALID WITH FIXES) closes O163.101a on (1/3,½); part14: R164_201 Theorem L PROVED (audit R164_291): L2a/O163.803a CLOSED NEGATIVELY in 𝒦_θ; Thm R (R164_401) tool: support integrality forced by positivity+gap+FE; part15: R164_503 Goal B ≥ RH + quadratic GRH (rejected as a route), prime-ceiling rounding at x^{1/2} ARGUED, Goal A OPEN; part18: R166_702 position/replacement DEAD [DMV wall θ≥β, Lemma PT]; R166_701 θ=0 NO-GO as a route to D [(N)], tools T3/T4; R166_601 NO-GO
  part19: R171_FINAL PROVED-TOOL; R171_CLS DEAD [F3:P_171]; R172_FINAL PROVED-TOOL; R184_001 PROVED-TOOL; R184_005 DEAD [F3:ℕ∪√2ℕ]; R184_008 DEAD [W-factor]; R184_010 DEAD [W-dither]; R184_013 DEAD [W-dither]; R184_014 OPEN

**5H** ◧ (ℤ-integrality × geometric/dynamical objects) — 26 routes: DEAD 15 · OPEN 7 · PARTIAL 3 · PROVED-TOOL 1
  killers: OTHER×13, W8×2, braiding sign cancels×1, T5×1
  dead: phase-15-arithmetic-hodge-index/M6; phase-114/114_a_*; 122 P122_024-027; 137 R137_007 D.11; 155 R155_054 P7; P46 §6,§13 D.4/D.9; P46 §19; P46 §22; 03-research/AUDIT_A §1 phase15; R160_S3 §2.2#23 phase-107; (+5)
  tools: 159 G1_B4_R5
  → live residual: torsion cocycle Φ_Λ (R162_1001) with non-band-limited tests
  → live residual: THE_BACKWARD_MAP a4/R16 (quadratic χ over Spec ℤ)
  → live residual: Quillen K_n(ℤ)/regulators, RO(G), A¹-motivic (AUDIT_A §3), untouched
  → live residual: P42 arithmetic Lefschetz programme: open global sign argument
  → live residual: Paper 44 §6bis: lattice from the integral shadow Sh_Z with finite I_A
  → live residual: Paper 43 §11bis: non-invertible correspondences (degree-q graphs)
  note: part7: o-minimality/Pila–Wilkie DEAD (R162_2402: W10+W8)
  part19: R173_OT5 OPEN

**6A** ◧ (Λ values × form of a window) — 21 routes: DEAD 12 · NO-GO 1 · OPEN 2 · PARTIAL 4 · PROVED-TOOL 2
  killers: E1×6, OTHER×3, F3:rigidity Thm R'×1, Lemma D / Thm U: Λ iso×1
  dead: phase-20-zero-omega-bridge/01-02; 141 D.27.5; 155 R155_053 P6; 155 prob:B; 157 O3 lem:degen; R160_S3 §2.2#12 phase-109; R160_S4 §2.D#36 P47 TK/N/N'; R160_S4 §2.D#42 P47 thm:Al; R160_D4_R2; R160_D4_R2 Cor 5.2; (+1)
  tools: 154 Thm C(½log3); R160_S4 §3.1 P47 prop:uniform
  → live residual: lem:degen log 2 case (R162_2902b): two-sided enclosure of the minimizer of the full form
  → live residual: O-D4.2: kernel of 𝒲 / cone 𝒞′ on decreasing tests of unbounded support
  note: part10: 2902b lem:degen PARTIAL (D1–D3), 2902c P153.17 NO-GO
  part19: SIGN-REAUDIT DEAD [F3:t₀=π/log2;W4]

**6B** ◧ (Λ values × contact kernel vector (linear in F)) — 17 routes: DEAD 11 · OPEN 4 · PROVED-TOOL 2
  killers: F3×3, F2×2, E1×1, M×1
  dead: R162_1401; R162_1502; R162_403; R162_401; R162_502 A
  duplicates: R162_2202b
  tools: 121 P121_RESOLVED_TATE_COLLAR_INTEGRAL; R162_2202a
  → live residual: P47 prob:annihilate = Gate 1 of phase 162 (annihilation of Γ moments at first contact)
  → live residual: O2202.1: [prim] version of Thm NI
  note: part7: Thm NI tool; Euler/Möbius self-similarity DEAD (2202b)
  part19: R170_892 DEAD [W12;moving σΔ countermodel]; R170_894 DEAD [W12;W5]; R170_900 DEAD [W12]; R172_CAND OPEN; R179 DEAD [W12]; R180 DEAD [W12]; R182_NGF OPEN

**6C** ■ (Λ values × quadratic/higher functionals) — 15 routes: DEAD 9 · OPEN 2 · PARTIAL 2 · PROVED-TOOL 2
  killers: OTHER×3, P} fails T>0.60×1, F3:Lambda chi_2×1, phase-104/106 ANOVA×1
  dead: R160_S5 §2.4#35 G2_B3_R5; R161_004 L161.2; R162_2301; R166_103A; R166_202; R166_502
  duplicates: R160_M2_R1
  tools: R162_501
  → live residual: O202.1: T_e = T_o for ζ (R166_202; no sign)
  note: part7: R162_2301 (Lemma S, Thm Q) + 2401 closes O2202.2; formerly ◧; part17: OS-2 CLOSED negatively (R166_202, empty/E1); R166_103 (α) DEAD [f_t/M_m]; part18: R166_502 P7+Q25 REPEATED [E70_11/12]
  part19 (repainted ◩→■, proposal): R170_899 PROVED-TOOL; R178 DEAD [F2;F3:two modes]; R184_C6C DEAD [W12]. Residual: none

**6D** ■ (Λ values × spectrum) — 4 routes: DEAD 3 · PROVED 1
  killers: F3×2, M×1
  dead: 155 P2 even Schur; R162_702 residual; R162_1603
  note: part10: P2 DONE (R162_2902a, exact structural identity, Λ-blind; tool)

**6E** ◧ (Λ values × flow/family in T) — 5 routes: DEAD 2 · OPEN 1 · PARTIAL 1 · PROVED-TOOL 1
  killers: OTHER×1, zero-side input violat×1, window shift×1
  dead: 159 G2_B7; R162_802
  tools: R160_S5 §2.4#38 G2_B9_R3
  → live residual: G2_B6_R5 Prop C: RH-free pointed cone under rigid perturbations C≠{0}
  → live residual: P153.14 staggered Kreĭn band admissibility of atom w_N (only N=3,4,5 measured; uniform = RH)
  note: formerly ■

**6F** ◧ (Λ values × global transforms in T) — 11 routes: DEAD 4 · NO-GO 1 · OPEN 4 · PARTIAL 2
  killers: OTHER×2, zeros enter only via M×1, E1×1, F3:DH×1
  dead: phase-102/313; P21 main.tex; R160_M1_R1; R160_M5_R1
  → live residual: P47 Problem B: arithmetic certificate w_T from external primes (no construction)
  → live residual: 114 D.260-262: centered Chebyshev channel dΨ−dx, exact residual, sign open
  note: A1 = E1
  part19: R184_011 NO-GO [E1;F3:Type I]

**6G** ◧ (Λ values × L-function/field families) — 3 routes: DEAD 1 · OPEN 1 · PARTIAL 1
  killers: T5×1, OTHER×1, c) proved only where v×1
  dead: 149 R149_005 D.59
  → live residual: O-D4.3: transposition of identity (C′) to ζ_K, routine, never done
  → live residual: separator 119 (P0/P1/P2) insufficient
  note: formerly ◩

**6H** ◧ (Λ values × geometric/dynamical objects) — 8 routes: DEAD 3 · OPEN 2 · PARTIAL 2 · PROVED-TOOL 1
  killers: E1×2, OTHER×1, NS rank 2×1
  dead: 140 D.23.4-6; 160 C4; R160_C4_R1
  tools: P44 main.tex
  → live residual: Paper 43 Thm 10.8b: Mertens global hyperbolic-ruled pairing (excluded from row A by A.10, not from row D)
  → live residual: 106.203-205: loaded Tate boundary with corrected mass log p/p^{k/2} (non-isometric resonant completion)
  → live residual: O-B5.1′ Borger W(R) not built
  note: formerly ◩

**7A** ◩ (zero side × form of a window) — 55 routes: DEAD 37 · OPEN 2 · PARTIAL 7 · PROVED-TOOL 9
  killers: E1×18, OTHER×8, W8×3, Platt–Trudgian×1
  dead: phase-4/PAPER-A Thm C; phase-18-negative-directions-portrait/01-02; phase-22-pontryagin-finite-defect; phase-32/59-64; phase-34/90; phase-61/O10; phase-118/PHASE_118_CLOSURE; 133 PANEL_3; 143 R143_005 D.34; 144 R144_005 §D.40; (+24)
  duplicates: R160_M6_R1
  tools: phase-0/0A1; phase-106/106_11; 121 P121_BOMBIERI_SUZUKI_XIA_AUDIT; 153 R153_005 Thm A; 154 R154_012 Thm D1/O; P07 main.tex
  → live residual: ω(E) at contact = Rem 4.8a (node position within its cell; R165_201 Cor 2.2)
  note: 122 two gates fail for Ξ_a; part15: R164_501 sinc on the zero side DEAD [E1, no room]; Thm SA, Cor SA.1 tools; part16: D.16-γ DONE negatively (R165_201 Thm 3(a), R165_202); Det− DEAD (R165_102); Det+ tool (R165_101); "interlacing ⇒ quartet off the cone" and "contact ⇒ EC" DEAD; part17: R166_101 DEAD [E1, Thm 2.1]; R166_201 DEAD [E1, jet hierarchy: Re G(t_q)² = jet k=−1]; ω(E) restated as the global phase of G at t_q
  part19 (repainted ◧→◩, proposal): R168_101 DEAD [W2/M]; R184_006 PROVED-TOOL [E1]; R184_006H DEAD [E1]. Residual: ω(E) at contact = Rem 4.8a = (★_cell) at the witness (forces RH; jet k=−1, W-jet)

**7B** ◩ (zero side × contact kernel vector (linear in F)) — 13 routes: DEAD 7 · PARTIAL 3 · PROVED-TOOL 3
  killers: OTHER×4, zero-filter gate E72.1×1, Cauchy-jet no-go E74.2×1, —×1
  dead: phase-72; phase-73; R162_1501; R160_S2 F29 phase-72/77; R160_S3 §2.1#1 phase-93/101
  duplicates: phase-74
  tools: 159 G2_B6_R4; R163_402; R166_501
  → live residual: R163_401: (★_cell) at the first-contact witness (⟺ RH at the witness, Rem 4.8a); tail form (TC) in R164_000
  → live residual: 159 G2_B6_R4 BRS uniqueness mod Lemma S (unaudited), Thm X extreme point unaudited
  → live residual: O166.501.1 (meta): is every non-confinement separator H whose proof does not use Z^off non-linear in Λ beyond the window?
  note: 121 F2 = global square; part13: R163_401 PARTIAL (closure candidate), R163_402 tool; formerly ◩; part18: Thm A of R166_501 (iii) ⇒ (ii); requirements (G)+(N′)
  part19 (repainted ◧→◩, proposal): R184_015F DEAD [W11′;E1]. Residual: (★_cell)/(TC) at the witness (E1 by definition) | O166.501.1 (meta)

**7C** ■ (zero side × quadratic/higher functionals) — 7 routes: DEAD 6 · PROVED-TOOL 1
  killers: OTHER×4, S1/S2/S3 disjunction×1, F3:DH×1, Epstein×1
  dead: phase-103/103_27,28; phase-106/106_26,29; 155 lem:Rrig; R160_S2 F44-F45 phase-55/59; R160_S5 §2.4#34 G2_B10_R5 Thm H; R166_801
  tools: 121 P121_CRITICAL_NEGATIVE_HALF_RESIDUE_GATE
  note: 2200 gave it □; P121 D_T^crit = global square; part18: R166_801 second moment over translations DEAD [E1/f_t]; residual "pair correlation as exact input" (§6 item 46) DONE negatively; fourth-moment nodal identity tool

**7D** ◧ (zero side × spectrum) — 25 routes: DEAD 13 · OPEN 3 · PARTIAL 3 · PROVED-TOOL 6
  killers: OTHER×7, E1×4, F1×1, E1 (terminates at Li-K×1
  dead: phase-7-weil-carleson-sine-kernel/P7b; phase-12-meta-obstruction-moment-problem/M12.10-11; phase-35/98; phase-35/101; phase-69; 121 P121_ISODIVISOR_DEFORMATION_NO_GO; 122 P122_011; 159 G2_B5; P36 main.tex; R160_S1 §2.7#44 phase-29-zeta-spectral-triples; (+2)
  tools: phase-48/152; R162_2101; R160_S3 §3.1 T15 115_17; R163_502; R165_101D; R165_102T
  → live residual: Diana L8/C_B/EX: m≤C quadruples; m<∞ ⟹ m=0 (see 8F)
  → live residual: phase-69: gauge-invariant Cayley signed index (named, not built)
  → live residual: R-C.b for ζ needs input from the zero side (2101)
  → live residual: O2401.1: individual sizes of V(F_M), H(F_M)
  → live residual: O102.1 (explicit Gevrey γ₁(ψ); does H=3·10¹² suffice?); O102.2 (Det− with δ*Λ*≤y₀; needs O701.2 and Cor 2(c)); O701.1 (remove (Dom)), O701.2 (sub-Landau lower frame), O701.3 (medium regime) (R165_102)
  → live residual: O167.101.1 (Dom_θ): other quartets near γ_q carry ≤ θ|Q_K|; O167.101.2: small-y regime, on-line count finer than S=O(log t) (R167_101)
  note: part7: Thm M's margin does not come from hidden contacts (2401b); part16: Det+ (R165_101) and Thm 1 (R165_102) tools; bracket 0.8047 < T_c ≤ min_ρ τ(ρ) PROVED (clustering caveat); part18: (Dom_θ) of R167_101 = (Dom) of R165_102
  part19: R168_101DH DEAD [W2/M]; R168_103 OPEN

**7E** ◧ (zero side × flow/family in T) — 17 routes: DEAD 10 · OPEN 2 · PARTIAL 2 · PROVED-TOOL 3
  killers: E1×6, OTHER×3, W2/M in the variable s:×1, cannot cross×1
  dead: phase-8-heat-flow-monotonicity/RT-coupled; phase-33/70-72,79; phase-102/178,182,258; 137 R137_007 D.0; R162_1802 Thm R; R162_902; R160_S1 §2.4#19 phase-9-unconditional-universality N6; R160_S2 F25-F26 phase-62/64; R166_102; R166_201E
  tools: 159 SYN 2.2; R160_S5 §2.4#33 G2 graded converse; R162_2501a
  → live residual: 77–80: (c) pencil compatibility, (d) ℓ² class, (e) simplicity, (f) assembly, FIXED-L-WEYL, SAFE-GAMMA-IDENT
  → live residual: P19 Hyp D: m<∞ ⟹ m=0 (C_B) → O2601.1 (8F)
  → live residual: O2501.2: e<1 ⟹ Θ<1 without finiteness
  → live residual: R165_202: node monotonicity and parity simplicity OPEN
  note: part8: 2β* exponent law (2501a) tool; part16: R165_202 node flow PARTIAL/E1; part17: R166_102 flow in s DEAD [W2/M]; R166_201E sine Lyapunov DEAD [E1]

**7F** ◩ (zero side × global transforms in T) — 29 routes: DEAD 16 · OPEN 2 · PARTIAL 3 · PROVED-TOOL 8
  killers: E1×12, OTHER×2, F1×1, F3×1
  dead: phase-29-zeta-spectral-triples/00-28; phase-29-zeta-spectral-triples/42-48; phase-29-zeta-spectral-triples/53-54; phase-62/C1; phase-102/174,175; P47 thm:Z; 155 thm:KEP3; 159 G2_B9; P38 main.tex; R162_803; (+4)
  duplicates: R163_003a
  tools: phase-29-zeta-spectral-triples/26; phase-55/173+176; phase-64/TASK-A; phase-105/105_02,03; R162_2601b; R163_001
  → live residual: KEP: Nevanlinna parametrization of 𝔖(T) through T (never written)
  → live residual: P33: finiteness A and purity D of the Cesàro −π/8
  → live residual: O164.601.1: lower bound of Σ_{q′}Re[G(t_{q′})²K(t_{q′})] for K Poisson/trig localized at γ_q (= (★_cell) weighted by K; R164_601)
  note: 803 = Herglotz (E1); part11: canonical exchange + D_test tool (R163_001); property 2 ⟺ RH (R163_003a, E1); part13: R163_801 Thm 3/Cor 3.1 tool (the tail 𝒯_X carries residues off the line); part15: Prop 4 tool (R164_501); O164.501.1 CLOSED (R164_601 Prop 2.1, dlVP over G²); route DEAD [W2/M + Thm 3.1]; part17: R166_102F DEAD [W2/M]
  part19 (repainted ◧→◩, proposal): R184_C7F DEAD [E1;Thm Z]. Residual: O164.601.1 = (★_cell) weighted by K (forces RH at the witness) | O2601.1 via the C_B cluster

**7G** ■ (zero side × L-function/field families) — 1 route: DEAD 1
  killers: rationality wall×1
  dead: phase 149

**7H** ◩ (zero side × geometric/dynamical objects) — 19 routes: DEAD 14 · OPEN 2 · PARTIAL 2 · PROVED-TOOL 1
  killers: E1×11, OTHER×4, T1×1, OT-5′×1
  dead: phase-4/RH-ENDGAME; phase-15-arithmetic-hodge-index/M8; phase-113/113_12,15; 141 R141_005; 159 G1_B6_R1; 159 G1_B7; P14 main.tex §cohom; arcs III-V,X; 158; R160_S1 §2.2#10 phase-26-krein-connes-bridge/27; R160_S2 F6 phase-42/127; (+3)
  tools: P45 main.tex
  → live residual: 113_12 Ansatz A: χ(D)=D²/2 (implies RH, passes the tests, never attacked)
  part19 (repainted ◧→◩, proposal): R184_C7H DEAD [W10;E1]. Residual: Ansatz A χ(D)=D²/2 (carrier implying RH; W10)

**8A** ◧ (arithmetic-free × form of a window) — 23 routes: DEAD 16 · OPEN 4 · PROVED-TOOL 3
  killers: OTHER×10, E1×7, W8×2, F3:Xi_a×1
  dead: phase-14-off-diagonal-anchor-asymmetry/AUDIT-P7; phase-68; phase-101/E101_068,078,081,082; phase-114/D.170; phase-114/D.191-262; phase-118/W3; phase-120/P3_COMMON_FAILURE_ARCHITECTURE; 121 P121_AT_CORPUS_ATLAS; 124 P124_014; 160 M1/M2/M5/M6/M10; (+6)
  tools: phase-58/190+59/198; P47 thm:finmod; R160_S3 §2.2#15 Paper 41
  → live residual: pending audit: 159 G2_B8_R5 Thm L″, G2_B2_R4 Thm U, R5 (Lemma S, Cor M1, Prop J)
  → live residual: GAP-198.1: non-factorizable inter-currency combinations outside 𝔄

**8B** ◩ (arithmetic-free × contact kernel vector (linear in F)) — 15 routes: DEAD 10 · OPEN 1 · PARTIAL 2 · PROVED-TOOL 2
  killers: OTHER×5, E1×5, F2×3, K=c×1
  dead: 121 P121_F2_DIRECT_CLOSURE_AUDIT; 160 R160_X_C1; 161 R161_037-039; P124_004-010; R161_016; R160_S3 §3.1 T25 D.170; R161_046-051; R162_2201a; R162_2201c; R162_2401a
  tools: R162_408; R163_501
  → live residual: O2201.1: asymmetric nodal weight = Z′/Z with a sign at the nodes (zero side)
  → live residual: M11 slot (never written): opposite-parity metric monodromy trace
  note: part7: Blaschke–torsion DEAD (R162_2201a/c, 2401a); formerly ◧

**8C** ◧ (arithmetic-free × quadratic/higher functionals) — 7 routes: DEAD 4 · OPEN 3
  killers: E1×2, F3:shift operator arit×1, F2×1, F3×1
  dead: P14 main.tex §hyperb; R162_1202; R160_S1 §2.4#21 phase-35/98
  → live residual: O-151.4: summand-versus-numerator axis as a mechanism (never developed)
  → live residual: Lemma 108: bound κ_W(Q_2)≤C n_W (not ⟺ RH), never attacked
  part19: R168_202 DEAD [W-identification;E1]

**8D** ◧ (arithmetic-free × spectrum) — 37 routes: DEAD 25 · OPEN 2 · PARTIAL 3 · PROVED-TOOL 7
  killers: OTHER×10, E1×5, F1×2, F2×1
  dead: phase-34/92; phase-49/154-157; phase-106/106_13,15; phase-115/115_15; 121 P121_VOLTERRA_RELATIVE_DETERMINANT_RIGIDITY; 155 thm:arena/P8; PATH-TO-D (ii); 160 C2; 161 R161_081; R162_1602; (+14)
  duplicates: R162_2602a
  tools: 155 Thm P; P47 thm:index/P/J/arena; R160_S2 §3.1 phase-60; R160_S4 §3.1 P47 thm:parityschur; R162_2602b
  → live residual: phase-37/110 (PARTIAL; entry R160_S1 §2.2#12 lists it as DEAD — unreconciled duplicate)
  → live residual: phase-35/99 (R160_S1 §2.7#45, PARTIAL)
  → live residual: phase-63 (R160_S2 F9, PARTIAL)
  → live residual: R160_010 D1/D3/D5 (OPEN)
  note: part9: rule §8 — 4 unsurpassed PARTIAL/OPEN routes ⟹ ◧ (part8 had lowered it to ◩ by mistake); O2601.1 (= O2602.1) and O2602.2 remain attached via 8F; part15: R164_502 Szegő–Widom DEAD [W4/W6]; L4, L5, L6 tools
  part19: R183_001 PROVED-TOOL; R183_023 PROVED-TOOL; R183_033 OPEN

**8E** ◩ (arithmetic-free × flow/family in T) — 22 routes: DEAD 17 · PARTIAL 2 · PROVED-TOOL 3
  killers: OTHER×10, E1×5, divergent constant C3(×1, reads verified zeros×1
  dead: phase-8-heat-flow-monotonicity/GATE-B (N5); phase-9-unconditional-universality/M9.1 N6; phase-45/136+46/139+47/147+48/149; 159 G1_B10; 159 G2_B2; P13 main.tex; P15 main.tex; P27 main.tex; P28 main.tex FormA; arcs I,IV; 159 G2; (+6)
  duplicates: phase-33/88
  tools: phase-54/167-168; phase-92/PHASE_92_CLOSURE; R160_S1 §3a#21 Paper 15 thm:hr
  → live residual: 92 CA-1 fixed-L convergence; Ω₇ (66) fails at the critical endpoint
  note: P39 gap with no cut ⟺ objective

**8F** ◩ (arithmetic-free × global transforms in T) — 7 routes: DEAD 5 · PROVED-TOOL 2
  killers: OTHER×2, E1×1, sub-resolution stratum×1, W2 (Theorem M is an up×1
  dead: phase-37/112-113 +38/115-116; 157 O1 lem:monoT; P26 main.tex; R162_2501
  tools: P29 main.tex; R162_2501b
  → live residual: O2601.1: individual property of the Euler product of ζ that uses the exact values of Λ non-linearly and bounds the off-line count (fails for deletion, M_m, Λ̃) → sharpened in part11 to BF_θ^disc (5G)
  note: part8: route (a) of C_B DEAD (R162_2501: 2β* law, model M_m, Thm 3); O2501.1 false as stated (2601a, Λ̃); formerly ◧
  part19: R184_004 DEAD [F3:M_m;W3]

**8G** ◩ (arithmetic-free × L-function/field families) — 9 routes: DEAD 7 · PARTIAL 1 · PROVED-TOOL 1
  killers: F3:function-field×3, T2×2, F3:Epstein×2, E1×2
  dead: 139 R139_005 T2; 145 R145_005; 159 G1_B9; R160_S2 F47 phase-44/45, Paper 29; R160_S4 §2.A#12 P46 T2; R160_S5 §2.3#28 G1_B9; R160_M9_R1
  tools: R160_S1 §3a#28 phase-36/106
  → live residual: field-uniform proofs (T1)
  → live residual: 36/106 tensorial amplification: missing finiteness sub-lemma R-FIN

**8H** ◧ (arithmetic-free × geometric/dynamical objects) — 101 routes: DEAD 61 · OPEN 17 · PARTIAL 15 · PROVED-TOOL 8
  killers: OTHER×43, E1×23, F3:Xi_a×3, LI×2
  dead: phase-8-heat-flow-monotonicity/PLAN (Epstein); phase-10-hodge-envelope-degeneration/M10.1-4; phase-15-arithmetic-hodge-index/M4-M5; phase-16-surf-witness-variety/06; phase-29-zeta-spectral-triples/49,52; phase-30-langlands-bridge-c-infinity/56; phase-40/122; phase-40/123; phase-41/126; phase-44/131-hw; (+50)
  duplicates: phase-43/129-130
  tools: 136 PHASE_136 §2; 142 R142_005 Thm 19.25; 159 G1_B3_R4-R5; 159 G1_B6_R2; P06 main.tex; P34 main.tex
  → live residual: 160 D1: Torelli-failing lamination with fixed points (the only carrier class not excluded by Thm Z/Thm H)
  → live residual: 28/02 APS η-invariant; 28/03 class [H_C] in KK
  → live residual: 108 Stage 7 scale compatibility
  → live residual: boundary triples for W_λ / uniqueness of B_CCM (AUDIT_CONSOLIDATED §2)
  → live residual: 121 Kreĭn flow conservation law (L4/M11)
  → live residual: 42/128 Deninger with Kähler–Riemann foliation
  → live residual: 159 unaudited: non-ergodic DK_α, Prop BL ℤ[ℚ/ℤ]
  → live residual: Request 122.A: natural self-duality of H¹(D) at 2D=K
  → live residual: I14 (40/123): Čech complex of D_0, never executed
  → live residual: R158_001 laminated carrier with fixed points + ALK polarization
  part19: R175_AB OPEN

## 3. Universal walls

| W | precise statement | cells it paints | first → last appearance |
|---|---|---|---|
| **W1 E1** | An honest reducer ends in a form equivalent to RH: Kreĭn/de Branges/Herglotz, Li/Keiper, Nyman–Beurling, (4.2) Sonin, Thm Z (certificate = explicit formula), "∀T" of a per-window law, ε₀≥0, Ω₇/RDI, Hodge ⟺ RH | 1A 1B 1E 1F 2B 2E 2F 3F 7A 7E 7F 7H 8A and ≈40% of all routes | phase-0/0A3 (de Branges) → R162_1802 Thm R, 803 Thm G (phase 162) |
| **W2 master quantifier / Theorem M** | Average ⇏ per-window uniform (P26–P29). Per-window ceiling T/log T (Thm 172.9, phases 54–59). **Theorem M:** λ^A_T ≤ exp(−e^{(2−ε)T}), so no margin, compactness or bootstrap works. ζ is at double-exponential distance from a Type I contact (2101) | 3A 3E 5A 7D 2D, and partly 3C/8F | 172.9 (phase 54) → P26–P29 → 155 thm:margin → 159 G2_B6_R2 → R162_2101 |
| **W3 class blindness (F3)** | What uses only Λ≥0, support on prime powers, EF or monotone laws holds equally for deletion, κ/finmod, DH, Epstein and the Type I curve (702 Thm 2; 703; 1601) | 2A 2B 2D 2E 3B 8D 8E 1D 4A | phase-8-heat-flow-monotonicity (Epstein), 14 (function field) → R162_2001/2190 |
| **W3′ integer-frequency blindness** (R163_1001 §5, Thm O) | In every class defined by Fr⊂ℕ + EF with Γ(s/2) + finite order + reality (any conductor) there are members with zeros off the line and a 2-periodic modular theta (f_χ); at conductor 1 the class is {cζ} (Hamburger). Global integrality is blind to the sign or amounts to an identification | 5E 5F 1G 4G (and 5A via f_t) | R163_113/114 (identification form), R162_2601c/2801 (form ζ=ζ), R163_901 (window form) → R163_1001 (deformation, periodicity, windowed Hamburger) |
| **W4 wrong sign / orientation (F2)** | Unconditional positivities give lower bounds and RH is upper (T9-A). The sum×product square contains the truncated Weil square (R161_002). The sawtooth is the comb of (PC). The Ward changes sign with η | 4A 5A 5B 6B 3D 4C 2C 8B | phases 9–12 (T9-A) → R161_001-004, R161_016 (Markov pullback; killer corrected to F2), R162_1902 |
| **W5 jets at λ=0 (F1)** | Everything entering as λ·(…) or as a first variation vanishes at contact | 1B 2B 4B 4C 6B 8B | P124_004-010 → R162_101/403/404/405 (R161_016 is **no longer** here: it is F2) |
| **W6 linear limit (F4)** | Tautological linear completions; [X,S_N]=−K_N; (PC+) and (PC−) have zero algebraic difference | 1A 1B 6B | R161_017-023 (**caveat:** R161_075 says the general exclusion of R161_018 is "unproved as written"; only 206 and 401 count as proved) → R162_206/401 |
| **W7 Λ*1=log linear** | Used linearly, it is a window translation T→T+½log X or cancels at composite thresholds (D4 Thm 5.1) | 6A 6B 6D 6E | phase-20-zero-omega-bridge (ω barrier) → R160_D4 → R162_406/1603/802 |
| **W8 rationality / finZ** | No finite set of zeros carries a flat-top certificate (finZ). Transport from finite fields hits the rationality wall (six exponentials, 159 G1_B4_R5) | 1H 4G 7G 5H 2G | 33/74 → phase 149 → 155 finZ → R162_1203 |
| **W9 method theorems T1/T2/T5** | T1: the proof must be field-uniform or name a separating property (ζ_K, S₃). T2: A1–A6 is not enough (Epstein), Euler is needed. T5: extracting a single fibre from L² moments is trivial | 1G 2G 3G 4G 8G | P46 §18 (phases 139–150) → 158 (S₃) |
| **W10 missing MW-5 object / OT-5′** | Every geometric or cohomological carrier postulates positivity or is ⟺ RH (Lemma T). Thm Z: one pole ⟹ at most one pair. Thm H: blind to off-line blocks. Tail wall W#. Thm 19.25: there is no h⁰ with (a),(b′),(c), not even over F_q | 2H 4H 5H 7H 8H | phases 41–44 (Deninger/Forni) → 142 Thm 19.25 → 158–160 |
| **W11 phase-136 meta-theorem** | Unconditional positivity is only prime-side or only archimedean; any statement coupling both sides is RH. The archimedean side is indefinite from T≈0.58 (prop:archneg) | 2A 4A 6H 8H | phases 5–6 (indefinite G_p) → 136 §2 → 155 prop:archneg |
| **W12 exact identity without sign / Γ dominates** | Chains of exact identities (secular, Kato, cofactor, Jacobian) preserve all the information but carry no sign. The locality–phase–sign trilemma (120). Γ dominates (110, 114, 118) | 4B 4D 4E 8A 1H | phases 81–101 → 120 → R162_1003 |
| **W-identification** (R164_190 §Round-2 synthesis; Hamburger, Thm O, Thm R) | Every global property that separates ζ from all falsifiers identifies ζ: the class it defines reduces to {ζ} (or {cζ}) and the zero question returns unchanged (= RH). Table: Fr⊂ℕ + EF, conductor 1 → {cζ} (Hamburger; R163_113, R163_1001 Thm O); Fr⊂ℕ + EF, q>1 → contains f_χ with zeros off the line (R163_1001); measure ≥0 off ℕ + gap (1,X) + EF + poles of ζ → {ζ} (R164_401 Thm R); Euler + ℕ + conductor 1 → {ζ}, with q>1 degree-one GRH (R163_1001 Thm O.2); on-line abundance, Riemann–Siegel, families/Parseval → do not separate (R163_602 F2, R163_603, phase 150); positive tail without EF → blind to zeros (Thm A, ζ_θ; R164_102, R164_101); integrality without EF (BF_θ^disc) → content only at θ≤1/3, the Witt lattice does not go below 1/3 (R163_803, R164_201) | 4F 5G 1G 5E 5F 7B (every class route) | Hamburger 1921 → R163_1001 Thm O → R164_401 Thm R, synthesis R164_190 |
| **W-jet** (R166_201 Thm 1.3; R166_190 "Close of phase 166") | Jet hierarchy: at the node x₀ adjacent to the quartet, the quartet's term in S^{(k)}(x₀) is 2k!\|Q(t_q)\|²r^{1−k}cos(2E+(k−1)ψ); the nodal weights are k = 1 (blind to ψ), the kernel equation is k = 0 (window and zero data), and **Re G(t_q)², the (★_cell) quantity, is the jet k = −1**: it is not a polynomial function of any nodal datum; only the global phase of G at t_q (harmonic measure of the node set, R165_201 Thm 2) reads it | 7A 7E 2A | R163_401 §4.4 (heuristic) → R166_101 Thm 2.1 → R166_201 Thm 1.3 |
| **Wall dichotomy** (R166_190 §0) | Zero side alone → M_m (R163_801 Thm 5); prime side (window) alone → f_t (R163_901 Thm F); class property → identification (R164_190); node identities → E1; spectral invariants → window data; margins at the witness → 0 (Theorem M). The only datum proper to ζ: the exact duality Z_ζ ↔ atomic Λ on log ℕ at every height (R163_114). Every round must couple both sides and name the wall it evades | all of row 7 and 6C/4F/2F | R166_190 §0 |
| **W-sieve** (R167_102 Thm B/B′, R167_291; R167_103 Theorem S) | Sieve blindness: b_θ = Λ·½(1+cos(γ log n + arg W + θ)) satisfies 0 ≤ b_θ ≤ Λ, lives on prime powers and obeys every upper bound that Λ obeys (Brun–Titchmarsh, Selberg, large sieve), and its twisted sum reaches X^{1/2} (two-sided PROVED; one-sided Re form, B′, with minorant cos² and Vinogradov–Korobov at height 2γ). **Positivity + support + upper bounds + large sieve never go below ½ in one-sided form.** Everything that goes below ½ uses an identity (Λ = μ*log, Selberg), and after Perron that is a zero-density statement (Thm D, ARGUED). Theorem S: the same tools hold in discrete Beurling, where DMV/Zhang have false RH | 3A 3G 2A | R166_802 Thm 4 → R167_102 Thm B → R167_291 (B′) |
| **(N′) localized RH** (R166_802; R166_190 round 12) | Sharpening of (N): a mechanism excluding the witness must control the sum of Λ beyond the window **at the frequency γ_q with the exact strength of the zero's absence** (localized von Koch O-bound; Landau / MV 15.3: exponent Θ − ½ at every fixed frequency). A lower bound on Λ is given by the zero and confirms the witness; excluding it requires the O-bound of the same size. No true inequality about Λ for ζ escapes this (PROVED for single tests and power families; ARGUED in general, O166.802.1) | 3A 7B 7C 4F | R164_601 Thm 3.1 → R166_501 Thm A → R166_802 |
| **W11′ source/form disjunction** (R184_015 Thm 2, Cor 3; part 19) | For every decomposition W_T = Pos_S + Δ_T with Pos_S ≥ 0 local and every P = "‖Δ_T‖ ≤ e^{o(T)}": if Δ_T is defined from the source (Γ, δε_p), P is invariant under X↦M_m (blind); if defined as W^X − Pos_S, its lower half is ⟺ RH (E1). No third option except the explicit formula (identity with no sign). Reinforces W11 | 2A 1H 7B 8F 4D and every Sonin/CC route | R183_018 → R184_015 |
| **W-Sonin (gap requirement)** (R183_031, R183_033; part 19) | Every positive-part multiplier with ∀T-bounded inertia remainder has a limiting density supported on the zeros (under RH): the Sonin/CC route carried to every T converges to the explicit formula; entire Sonin has n₋=∞ for T>½log2 (R183_018 Thm 5.1, R183_019 Thm 4.1) | 2A 1B 1H | R183_018/019 → R183_031 → R183_033 §5 |
| **W-factor** (R184_008 Lemma AC + Theorem F; part 19) | An Euler factor with multiplicities ≥0 has no zeros to the right of its abscissa; if P = B⊔Q is exact with θ<1, Q has abscissa ≤θ and contributes no zeros in Re s>θ. Multiplying ℕ by a factor never produces zeros outside, ∀θ<1 | 5G | R184_008 |
| **W-dither** (R184_010 Theorem D + R184_013 (1−θ)/2 ceiling; part 19) | In the linear model there is a rounding with sup\|T₁\| ≪ x^{(1−2a)/4}: linear L* is false. In the full system the composites do not diffuse and the exponential method does not go below (1−θ)/2 (ARGUED). Every "rounding + Perron" route for θ<1/3 stops there | 5G | R184_010 → R184_013 Cor 3.2 (audit R184_093) |

Weight order: **E1 ≫ W-identification ≈ W2 (M/quantifier) > W3 (F3) ≈ W3′ > W10 > W9 > W8 > W4/W5**.

## 4. Falsifiers and countermodels × properties refuted

| model | shares with ζ | refutes | files |
|---|---|---|---|
| **DH** (Davenport–Heilbronn) | EF, ε, archimedean side; no Euler | EF identities, flow laws, (LB)/virial, Kreĭn CM, degree-1 transport, mollifiers, repulsion (thick zeros) | P04, 47/146, 64 C,D, 102, 407, 503, 1003, 1301, 802, 159 G2_B10 |
| **Epstein** | EF, geometry | "geometry is enough," axioms A1–A6 (T2) | phase-8-heat-flow-monotonicity, P46 §18.2, 139 T2 |
| **Ξ_a** (deformed ξ) | Weil's form except the cross term | Hodge transfer, modelless h⁰, two gates R+S, ε-phase | 121–146, 122 P122_020, 124 P124_013/014, R160_C8 |
| **Ξ_Q, ζ_K, S₃** | Euler over other fields | equimodularity, Ξ_a-only separations (Thm A 153), non-abelian unitary routes | 138 T1, 153 Thm A, 158 |
| **function field (F_q)** | Frobenius, true RH | Landau anchor, Weil transport, frame (the frame defect holds there too), q→1 | 14, 33/74, 63, 145, P46 §21, 159 G1_B9 |
| **Hadamard** (generic products) | every dynamical law | LP-134 repulsion, dynamical finiteness | 179, 46/141 |
| **deletion Λ1_{n≥5}** | Λ≥0, PP support; λ_W≤0.4608<T* | Type II exclusion, monotonicity, S=2 nodal, Douglas/log | 703, 802, 902, 1401, 1601, 1803, 155 finmod |
| **κ-models / finmod a^κ** | support, positivity, almost every value | first quarter, Perron–Tate angle, regularized jet, flow; "one fixed window decides" | 103, 204, 702, 802, P47 thm:finmod |
| **sΛ amplification** | everything except scale | sign of ⟨u₂,φ̂⟩, (C2), homotopy in s | 1801 Thm D, 1803 |
| **two-atom Type I curve** s₂δ_{log2}+s₃δ_{log3}, s₂^c=0.9997678 | positive cone, monotone laws | R-C.b blind to weight; every spectral exclusion of Type I without zero data | 1901 §4, 2001, 2190, 2101 |
| **3×3 models** | Perron, monotone laws | homotopy/polarization (1801 Thm B); Type I compatible with every law (1901 Thm 2); coherent saturation (2×2, R161_037) | 1801, 1901, R161_037-039 |
| **Λχ₂** | Euler, Λ*1 = L-series | character sums, ε-phase, BCH, Problem B family. **Does not** pass the cocycle Φ_Λ nor "Z with coefficients 1" | 1102, C8, 903 (corrected in 1190), 1001, 160 M1 |
| **Beurling DMV** | Λ≥0, Euler, Λ_B*1=log exact, zeros off the line | every use of Λ*1=log without ℤ (903, 1302, 1401, 1402, T3, Berkovich kernels). Only separated by Φ_Λ (𝒩_B⊄ℤ) and integrality | 1001, 1302, 150, 152, 157 |
| **comb models** | coherent class | windowed converse (156), (C2) from T≈0.38 | 156, 1502, 1803 |
| **M_m** (ξ × rational factors of m off-line quartets; R162_2501b) | EF, zero-side identity, closed semi-bounded form, lem:contA, first contact, witness, nodes, finZ, Theorem M; κ(M_m)=κ(ζ)+4m | route (a) of C_B, every class argument (Thm 3); sup N<∞ (N→2m). Missing only the purely atomic arithmetic side | 2501, 2590, 2602 |
| **windowed M_m** (M_m windowed; R164_601) | EF, zero-side identity, positive tail of Λ above the window | **satisfies the tail sign inequality** (Prop 4 / Prop 2.1): the tail's sign does not exclude quartets without an independent lower bound (Thm 3.1) | R164_501 §8, R164_601 |
| **Λ̃** (positive atomic weights Λ̃(n)=1−Σ2Re n^{ρ_j−1} at {±log n}; R162_2601 Thm Λ̃) | atomicity, positivity, Chebyshev; reproduces the non-tempered part E of D under H(m) | O2501.1 as it stood ("atomic comb ⟹ E=0"); G(s) is not a log-derivative. Only separated by the individual Euler-product property (O2601.1) | 2601 |
| **ζ_θ(s)=ζ((s−θ)/(1−θ))** (Broucke system 2409.10051 §6.1, CITED; R163_101 Prop 1) | extended Beurling class (dΠ≥0, dN=exp_*(dΠ)), extended Euler, N=(1−θ)x+O(x^θ) ∀θ∈(0,1), analyticity in Re s>θ, growth/PL, Jensen, Broucke densities; zeros at Re s=(1+θ)/2 | the class branch of BF_θ ("integer error <√x ⟹ RH, uniform over the class"); every analytic obstruction (NO-GO §5 of R163_101). Only separated by integrality of the prime multiplicities (BF_θ^disc) | R163_101, 190 |
| **root substitution** p↦p^{1/m} (e.g. P=(primes∖{2})∪{√2}; R163_102 Lemma S) | discrete Beurling, N=ρx+O(1) (√2: sup R≈2.00 up to 10⁶, R163_191), zeros of ζ at σ>0 | "N=ρx+O(1) ⟹ lattice" (rigidity only for ⌊x⌋+c, Thm R); τ and q cancel exactly (O102.3) | R163_102 |
| **finite prime deletion** T (ζ·∏_T(1−p^{-s})) | discrete Beurling, N=ρx+O(1), sup R ≤ 2^{#T−1}, same zeros as ζ at σ>0 | bounded-error rigidity; by Cor F every ℕ-comparable system is RH-equivalent (not a countermodel) | R163_102 |
| **K(s)=1−c/(s+1)**, Z₀=ζ/K (R163_002 §2) | exact integers b≡1 and Euler of ζ, positive Beurling quotient | "exact integer + Euler + positive quotient ⟹ trivial factor" (no EF, not an exchange) | R163_002, 190 |
| **f_χ** = αL(s,χ)+ᾱL(s,χ̄), χ an even cubic character mod 7, α²=ε̄_χ (even DH combination; R163_1001 Lem 1.1) | integer frequencies (Fr⊂ℕ), real 7-periodic coefficients, ζ's Γ(s/2) form, exact EF Λ_χ(s)=Λ_χ(1−s) (conductor 7), order-1 entire, 2-periodic weight-½ modular theta; zeros off the line PROVED-CITED (Kaczorowski–Kulas 2007; Saias–Weingartner 2009; page caveat, phase-48 doc 150) | every argument by global integrality / periodicity / modularity / Hamburger that does not use q=1 (W3′, Thm B.3); on-line abundance as a separator (DH type, Bombieri–Hejhal, R163_602 F2); Riemann–Siegel/AFE (EF only, R163_603 L2.1). Only separated by q=1 (identification) and the Euler product | R163_1001, R164_000 P3 |
| **f_t = ζ+t·g** (g a quasicrystal of frequencies m/√M; R163_901 Thm F) | ζ's EF, pole, real coefficients, integer zero multiplicities, ζ's prime side at log n<2T₀ (∀N₀), the witness and T_c of ζ if T_c<½log N₀; zeros off the line | every argument from window data + multiplicity integrality + any property shared with f_t (L-A of R163_1001); forces use of primes beyond the window (P1 of R164_000). Only separated by Fr⊂ℕ and the Euler product (f_t has neither) | R163_901, 991, 1001 |
| **P_{a,c}** = ζ(s)·[1 + c·cosh((s−½)log a)] (R166_103 G1) | θ−1 > 0, exact EF with Γ(s/2), order 1, pole at 1 | moments of θ−1 / Markov–Krein: W_T is not affine in the coefficients, only ξ(ρ)=0 is a linear moment; infinitely many zeros off the line in the strip | R166_103 (γ), G2 |
| **b_θ** = Λ·½(1+cos(γ log n + arg W + θ)) (R167_102 Thm B; B′ after R167_291) | 0 ≤ b_θ ≤ Λ, support on prime powers, every sieve upper bound that Λ obeys (Brun–Titchmarsh, Selberg, large sieve) | every proof of (WS*) by positivity + support + upper bounds: the one-sided twisted sum reaches X^{1/2}. Does not obey bounds coming from identities (Vaughan) nor two-sided Bombieri–Vinogradov | R167_102, R167_291 |
| **DMV / Zhang as a sieve falsifier** (R167_103 Cor S′) | discrete Beurling with N = Ax + O(x^θ), θ ≥ ½, Euler, Λ_B ≥ 0; all the sieves of Theorem S (Selberg, Brun–Titchmarsh, Vaughan, MV/large sieve; large-sieve constant via log gaps) | every proof of (WS) uniform in X with η < ½ made with those tools (Beurling RH false). Sieve classes do exclude f_t and see only the atomic part of M_m: **for sieve proofs the correct falsifier is DMV/Zhang, not f_t/M_m**. ℤ's additive structure (congruences, Bombieri–Vinogradov) is identification | R167_103, R167_291 |
| **positive theta kernels with zeros off the line** | kernel positivity | "theta positivity is enough" | 103_15-30 |
| **ℕ ∪ √2·ℕ** (θ=0 root-substitution systems; R184_005 N1/N2; part 19) | discrete Beurling, N = ρx+O(1) (θ=0), zeros of ζ at σ>0 | the set-theoretic form of C1 ("{n_k} ⊂ finite modification of (1/c)ℕ"); the O(1)-window Diophantine route (N2) | R163_102 Lemma S, R184_005 |
| **relaxed class R = L(u,χ)** (R184_014 Prop B.3, Cor B.3′; part 19) | polynomial growth of ζ_𝒫; ε_p bounded at every Witt level, no integrality | every proof of L*_comp that uses only size bounds on ε_p: requires ε_p ≡ −p^a (mod 1) | R184_014 |
| **low band** (zero gap (−γ₁,γ₁); R183_027; part 19) | — | (L-Son) with η uniform in T; C_T ∀T with no null density in the gap (CONDITIONAL(RH), sufficient because (L-Son) ⟹ RH) | R183_027, R183_028 §2 |
| **P_171** (R171_FINAL; part 19) | discrete Beurling with integer multiplicities ≥0, N = cx+O(x^{83/208}) (fixed exponent 2/5), deterministic and computable; infinitely many zeros at Re s = 11/16 | every discrete rigidity with θ₀ > 2/5 and every route using only the class N = cx+O(x^θ), θ>1/3; specialization λ=3/8 of BFdisc (R163_803) | R171_FINAL, R172_FINAL |

## 5. Inventory of proved tools (PROVED-TOOL, reusable)

- **Erratum (part 19; R184_014 A1–A6, R184_093):** R164_201 §1 (l.~33–38) and R184_001 item 1, §1.1, §1.3 row 1: chaos of order k ≥ 2 and Witt levels k ≥ 2 are **not** O(x^{θ+ε}) for every a>0 (same power X^{1−2a} at every order; level k contributes x^{(1−θ)/(2k)} if θ<1/(2k+1)). Theorem L and the exponent (1−θ)/2 of the random method do not change. **Phases 168–184 (part 19):** P_171 (R171_FINAL); classification [V]/[F] (R172_FINAL); Prop 5.2/Prop 5 Eratosthenes (R169_091/101); archimedean transport and Theorem (A) (R170_806/808); polar-port ledger (R170_884–899); connected/covariance dichotomy (R178); quotient comb (R181); infinite rank of the coherent channel (R182_201); E_S = Son + R_{S,T}, relative 0 bound, law (Λ) (R183_018/023/029); Lemma AC + Theorem F (R184_008); Theorem D (R184_010); Thm 4/Cor 5 (R184_004); T*(a,γ) (R184_006); Theorem W (R184_007); Lemmas 1–2 (R184_012); Theorem 2/Cor 3 (R184_015).
- **Phases 166 (rounds 9–12) and 167 (part 18):** **Thm A** (R166_501): (iii) alone ⇒ (ii) (requirement (i) unused; "{i,iii} empty" is a theorem), B(1)–B(5) transport of Thm R to η = Z − Q_X without (Q), exact obstruction B(5); non-integer comb lemma of V*V (R166_502); **T3/T4** (R166_701): adding a prime q preserves θ = 0 ⟺ R bounded coboundary for x ↦ x/q, ℕ + a real q never gives θ = 0 (check Hilberdink 2012); **Lemma PT** (R166_702): Parseval for Besicovitch means (discreteness obstruction); second-moment identity over translations and **fourth-moment nodal identity** (R166_801 (2.3), (4.1)); **Thm 0, Thm 3, Thm 4** (R166_802): general discarded term, frequency-localized Landau, zero-free sieves give Θ ≤ 1; **Thm A, Lemma Q, Thm C, Prop W** (R167_101): exact identity 4Re 𝒮_full = (L/π)I − Q_K − R_K − O_K + polar, Q_K = −4c_Θ\|G(t_q)\|²\|k(−iδ)\|, η < δ, the sum covers [1,Y]; **Thm B/B′** (R167_102, b_θ); **Theorem S / Cor S′** (R167_103).
- **Phase 166 (part 17):** **Thm 2.1** (R166_101): \|G(t)/(t−x₀)\| ≤ e^{T\|δ\|}‖G′‖_∞ (Phragmén–Lindelöf + Bernstein; no pole singularity at the nodes; the quartet weighs in d_x as two zeros on the line); **rough-tail split** (R166_103 B1–B2): 𝒯_X = 𝒯^det (window, holomorphic in Im x > −½) + 𝒯^new = −ζ′_{≥X}/ζ_{≥X}, with ζ_{≥X} the zeta of X-rough integers, carrying all residues off the line and separating f_t, f_χ, M_m; **falsifier P_{a,c}** (R166_103 G1); **jet hierarchy** (R166_201 Thm 1.1, Thm 1.3, Cor 1.4, Prop 2.2); **parity identity** (R166_202 Thm 3): W_T(F^ev)+W_T(F^odd) = 4W_{T/2}(Φ).
- **Phase 165 (part 16):** **Det+** (R165_101): ¬RH at ρ* ⟹ λ^W_T<0 for T ≥ τ(ρ*), τ ≤ T_L(γ*)+½log(π/2)+o(1) (dividing ξ by its quartet, truncating the Riemann–Pólya kernel); bracket **0.8047 < T_c ≤ min_ρ τ(ρ)** PROVED with a clustering caveat. **Thm 1 / Cor 2(c)** (R165_102): sub-Landau detection T_det for a dominant zero; contact is decided by min_ρ T_det. **Thm 2 / Cor 2.2** (R165_201): exact phase identity, 4Re G(t_q)² = 4|G(t_q)|² cos 2(Φ_Z ± πω(E) + Ψ_out); sign variable ω(E). **R165_202:** no jumps in T, real-rooted at every simple T, quadrature and Cauchy at every T, separation by loaded zeros (E1).
- **Phase 164 (part 15, rounds 3–4):** **Thm SA** (R164_501): every ≥0 test on ℝ annihilated by the kernel equation is ĤĤ^# with H∈E_c (finite-dimensional cone; critical node density T_c/π, no surplus type); Cor SA.1 (polynomial ladder; direct route F5 of R164_491). **Prop 4** (R164_501): Ψ_y=G²·y/(z²+y²)≥0, Σ_ρΨ_y(t_ρ)=𝔄_y−G(iy)²𝒯(iy), 𝒯(iy)=Σ_{log n≥2T}Λ(n)n^{−½−y}>0 (signed tail of Λ at real height; an identity, not an inequality). **L1, L4, L5, L6** (R164_502): A_T depends only on σ̌ on (−2T,2T) — every spectral invariant is window data; heat-trace criterion (given L3 ARGUED); Stieltjes = Krylov positivity; Widom identity. **Props 1.1/1.3** (R164_601): exact tail-sign condition for G²K; **Thm 3.1** discarded-term principle. Thm R PROVED after F3/F1 of the R164_491 audit (novelty: not found in this form, possibly folklore).
- **Phase 164 (part 14):** **Thm R** (R164_401, audited): sinc annihilation of self-dual measures with gap and sign — m̂=m, m=comb on (−X,X) with X>1, m≥0 off ℤ ⟹ supp m⊂ℤ (Lem 2), and then m=comb (Lem 3); hence N=N_ζ on [1,X), N≥0 off ℕ, EF of ζ with its poles, finite order ⟹ f=ζ (Hamburger with positivity + gap instead of integer support; novelty to be verified). **Theorem L** (R164_201, audit R164_291): in 𝒦_θ, θ<1/3, every bounded-deviation rounding of Witt counts has quadratic mean error ≫ x^{θ+δ(θ)}, δ=θ(1−3θ)/(5−3θ). Also: Thm L Landau–Pringsheim of the tail, Thm H, Thm A (R164_102); Lemma H, Thm KZ, Prop D, Prop θ (R164_101); Props P/S/F/B (R164_402, superseded).
- **Beurling frontier and exchange (part 11, phase 163):** canonical exchange E=∏E_{δ,γ} with log E(½)=2Σlog(1+δ²/γ²), Frullani current q_E and faithful defect D_test (R163_001, 7F; continuous in the distributional topology, 190); support lemma for positive factorization (R163_002a, 5F); Lemma R (R163_101b): ζ·R positive rational with θ-regularity ⟹ θ≥½+β; Thm R (R163_102a) ⌊x⌋+c lattice rigidity ⟹ ℕ; Lemma S (102b) ζ·A, Σ|a|<∞ ⟹ N=A(1)x+O(1); Thm T + Cor F (102c, with ρ>0) zero transfer at σ>max(σ_τ,θ,0); Révész 2207.00665 Obs. 7 via Hilberdink 2010 (191a, cited): discrete with θ<½ ⟹ zeros with β>θ, finite perturbations ⟹ RH_B ⟺ RH.
- **Round 29 (part 10):** structural identity of S_even at log 2 (2902a, ‖Π_log2‖=0.9009276); lem:degen D1–D3 (2902b); spec S={0,±½}, ½-Lipschitz concave V, Danskin (2902c); R162_2901 Props 1–2 and Thm B (ζS₁^K P₀/P positive Beurling with RH).

- **Tate 2×2, quantitative Hamburger, multiplicative book (part 9, rounds 27–28):** Thm TC (2701) H_S=½exp(2Θσ₁), Θ=Σ artanh p^{-1/2}; Thm P (2701) H≻0 for every boost chain (RH-neutral); Lemmas 1–3 (2801): −ζ₀′/ζ₀ = Dirichlet + canonical rational, ζ₀=ζ/R off S, Hamburger with rational defect returns cζR for every m; Thm PB (2802) Piltz with integer k sees no zeros, H(m) ⟹ LH; Thm L (2802) terminating identity ψ–D_k (formal, blind to m). *Downgraded to "to be redone" (2890):* boundary triple of W_λ (2702b), (4,4) deficiency, not (2,2); only Prop 2.5 (Λ-free invariants) remains certified.

- **C_B and counting (part 8, rounds 25–26):** exponent law (2501a) under H(m) lim (1/T)log(−λ_A)=2β*, unconditional floor −4e^T (repaired by 2590); model M_m (2501b); Thm K (2502a) faithful comparison without division ⟺ Gate 1, ‖K_T‖≥c/λ(T) (reusable test for any "faithful detector + comparison"); Thm T (2601b) m=0 ⟺ D tempered, exponential type of D mod S′ = β*; Hamburger rigidity (2601c): atomic log-derivative + conductor-1 EF + finite order ⟹ F=cζ (cited from memory); Sonin count N(T)=n₋(A_T|P_T) (2602b), non-decreasing, first jump = first contact, lim N = 2κ_off.
- **Witness nodes (part 7, rounds 22–24):** Thm NI (2202) w_x=L(x)/F̂′(x), only n<e^{T_c} (Christoffel); Thm ND (2202, with ι-invariance) no descent; Thm N1 (2201) atomic object 𝒜(s;G)=Σ q_x(−ζ′/ζ)(s+ix) (factor of 2 in (a), (b) only ⟹); Lemma S (2301) Selberg identity ⟺ a=Λ (recursive); Thm Q (2301) exact nodal quadrature at type ≤2T_c (Akhiezer); Thm HV (2401) H = witness-mean sum channel, c_F=(F₊*F₊) on [T,2T]; Lemma U (2401) witness+μ^< determine the hidden comb; Thm N (2302) weak limit ≡0 mod Tate via ζ(1−ρ)=0; Thm V (2302) radicality ⟺ Gate 1. Proposition N3 (2201, downgraded by 2290).
- **Window/certificates:** Thm C(½log3) 8.86e-5; λ_A, λ_W>0 on (0,½log5] (R162_303/703, P47 thm:log5W); strong duality D1/O (154, never reached); continuity of λ_A (R162_001, P47 lem:contA); 407 rate λ_A(T*+δ)≥−2A*Q*/log(1/δ); Theorem M (159 G2_B6_R2); TK/N/N′ (M≤24); (H1)/cor:H1 archimedean negative index one; Thm P n₋≤5/7/8; thm:index/arena (exact n₋ for T≤0.90); thm:finmod.
- **Structure of ζ at contact:** R162_2101 (near-kernel = truncated Pólya radical); R162_408 (NE) exact; R162_501 Selberg–virial identity; R162_502 B2 M_T(Λ)=ZXZ⁻¹−X; P121: incoming Tate current, opposite-parity port rigidity, closed Tate collar, residue square D_T^crit.
- **Method theorems and proved walls:** P46 T1/T2/T5, T3 (conditional on H-DMV, already cited), T4 polar/entire; 136 meta-theorem; Thm 19.25 (frame defect) and its model over F_q (P46 §21); D.34.5 (no primitive class with all Frobenius traces ≥0); 159 walls: tail W#, rationality wall R/R′, Cor H/Cor M1, Thm A 9′, SYN 2.2 graded Weil converse; P29 master quantifier; 198.2 (non-collapsibility, class 𝔄).
- **General analytic results:** 0B truncation lemma; A0 Laguerre uniform tail (102); 105_02 Li exponential mode; 106_11 compact negative tests under ¬RH; 55/173 Green–Littlewood energy (Cesàro = πI−π/8); 64 TASK-A (Paley–Wiener non-vanishing); 54/170 E(T)≪T/log T; 54/167 dBN balance law; P32 Stepanov; P16 prime variance in short intervals; 9T-cal Montgomery→extremal rate; 32/65 PPP recurrence; 47/146 thick DH zeros.
- **Dictionaries/structure:** 0A1 (Q = Weil–Guinand Gram); P07 localized Weil detector; P09/P10 anatomy (factorizes ⟺ Euler); P05/13/19 ω hierarchy; P43/P44/P45 carriers of rows A/B/C; P06 D0 classifier; P18 Kreĭn index anatomy; 111 Schwartz admissibility; 114 D.244 (1,|S|−1) inertia; 57/183 Dirichlet–Selberg identity; 29/26 Carleman failure; 159 G2_B6_R4 BRS uniqueness (mod Lemma S, unaudited).

## 6. Never attempted / abandoned without closure

Deduplicated list of routes marked open that no later phase attacked. Format: origin → cell. **DONE** = already closed; *unaudited* = text exists without audit verification.

1. Conjecture A.15, monotonicity of the Kreĭn index under dBN (phase-28-four-fronts/01) → 1E
2. APS η-invariant (28/02) and class [H_C] in KK (28/03) → 8H
3. Exclusion conjecture "all on the line or infinitely many off it" (21/01-02) → 4D
4. Doc 107, Weil in two variables (36/107) → 4C (probably absorbed by 108/MW-7, NOT CONFIRMED)
5. Walls A/B of adelic rigidity (27) → 4H; Arakelov witness 𝒳 (15/M10) → 2H
6. GAP-135.A / doc 148, incommensurate frames → 4A
7. GAP-196.A, DH near-doubles of Λ_f → 3D
8. GAP-197.1: (TW_y) for some y>½ → 3C/3E
9. GAP-189.1: ζ-correlated weights on the boundary → 3F
10. GAP-198.1: inter-currency combinations outside 𝔄 → 8A
11. GAP-179.B / 192.A: effective separation of the discriminant of ξ → 5D
12. O8 (61): explicit 2×2 H_S (Sonin + de Branges) → 1D (the p-adic Sonin range 1 weakens it)
13. 77–80: pencil compatibility, ℓ² class, simplicity, assembly, FIXED-L-WEYL, SAFE-GAMMA-IDENT, cut A1–D3 → 7E/4B
14. Deninger with Kähler–Riemann foliation (42/128) → 8H
15. Connes–Consani Sonin count #{λ_j(K_I)>1} (115_15) → 8D
16. Ansatz A χ(D)=D²/2 (113_12) → 7H
17. Stage 7 of 108, scale compatibility → 8H
18. Distributional carrier ker X=span δ₀ (83–84) → 4B
19. Deep limit Ω_X→0 and subexponential Li bound from the primes (105) → 3F (forces RH)
20. Extension of the certificate to ½log5 (118 W4, 114) → 3A: **DONE** (R162_303/703)
21. PATH-TO-D (ii): A_T as the compression of an explicit self-adjoint operator → 8D
22. S5 of 136: tropical Hodge index of Cartwright → 2H
23. P122_D_SPECIFICATION: correspondence E_(∞,T) → 1H
24. Kreĭn flow conservation law (P121, L4/M11) → 8H (memo R160_X_C1: Blaschke witness **DONE**, NO-GO in R162_2201/2401; M11 slot still unwritten)
25. D.16-γ: cone cut by the zero data (138) → 7A — **DONE** (negative, R165_201/202)
26. P152.1 Dolgopyat–Mayer via Lewis–Zagier → 1H
27. KEP: Nevanlinna parametrization of 𝔖(T) → 7F
28. P2: structural identity for S_even at log 2 → 6D: **DONE** (R162_2902a)
29. O3/lem:degen, degenerate case of V_T → 6A: **DONE** except log 2 (R162_2902b PARTIAL)
30. O-151.4, summand-versus-numerator axis → 8C
31. Round-2 D1 (160), Torelli-failing lamination → 8H
32. 159 *unaudited*: G2_B8_R5 Thm L″, G2_B2_R4 Thm U, G1_B1_R5 non-ergodic DK_α, Prop BL ℤ[ℚ/ℤ], R5 (Lemma S, Cor M1, Prop J) → 8A/8H/4A
33. Chinburg–Rumely; the web hit "Certified Weil positivity beyond the unit window" (unread) → 3A/7A
34. Off-machine two-prime package at 0.58 (numerical; not a route) → 3A
35. Option 6 of R160_020, Meyer's mixed class S+D → 4C; O-B5.1′ Borger W(R) → 6H
36. Boundary triples for W_λ / uniqueness of B_CCM (AUDIT_CONSOLIDATED §2, "RH-neutral") → 8H
37. Quillen K_n(ℤ)/regulators, RO(G) Klein-4, A¹-motivic (AUDIT_A §3) → 5H
38. P25 V.2: Pontryagin completion with characters x^{b+iγ} → 1H
39. P30 LP-112 + L8 and P19/P33 Conjecture C_B (m<∞ ⟹ m=0) → 8F/4E/7E
40. GAP-157.A, Kronecker flow discrepancy → 3E
41. P47 Problem B, arithmetic certificate → 6F (touched in 159/R160_S4, no construction)
42. P47 Open 5: λ_W>0 beyond ½log5 → 1A/3A (the stretch up to ½log5 is **DONE**; beyond it, open): existence PROVED by continuity (Paper 47 cor:beyond5: 𝔊_T ≻ 0 and λ_W > 0 on (½log5, ½log5+ε]); a window certified with a value: open (log 44)
43. P46 §28.4, six-clause object → 2G
44. THE_BACKWARD_MAP a4/R16, quadratic χ over Spec ℤ → 5H
45. Pila–Wilkie / o-minimality versus W_T → 5H: **DONE** (NO-GO, R162_2402: W10+W8)
46. R162_2200 "idea-residuals" nobody formulated as a route: 5F Poisson in T (**DONE**, NO-GO R162_2302), 4F generating object with Euler before regularizing, 2F Bernstein of λ_A(T), 5D Smith form of the contact Gram, 1G converses/Hamburger, 7C exact pair correlation (**DONE**, negative, R166_801: Theorem 7C, E1/f_t)
47. *(part 6)* canonical Tate 2×2 transfer system, O8 (61), κ₀+|S|→0 index collapse → 4E (absorbs item 12)
48. loaded Tate boundary with corrected mass (106.203–205) → 6H
49. lattice from Sh_Z (P44 §6bis); non-invertible correspondences (P43 §11bis); Mertens ruled pairing (P43 Thm 10.8b); Request 122.A → 5H/8H/6H/8H
50. interlaced OS model of W_T (S1 I1) → 2H
51. NG-D4, Fourier anticommutation Q(f,g)+Q(f̂,ĝ)=0 (I15) → 1D
52. Lemma 108 κ_W(Q_2)≤C n_W → 8C; colimit of P44 Thm 8bis.4a → 4H; (H_L) of P44 → 4A
53. slots D1 (→ 8H, already in item 31) and M11 (→ 8B)
54. Option 6 Meyer S+D (item 35) → 4C; O-D4.2 → 6A; O-D4.3, transposition of (C′) to ζ_K → 6G
55. GAP-157.A (item 40): also in its non-local Tauberian form with LI input → 3F/4F
56. Chinburg–Rumely energies outside 𝔄⁺ (item 33) → 2H
57. Hecke-type G2_B3_R5 Cor S2 coupled square → 4C
58. web hit "Certified Weil positivity beyond the unit window" unread (item 33) → 3A
59. other OPEN items of part 6 with no later attack: I6 (negative block under resolution, 3A), I11 (absorbing channel, 4H), I14 (Čech of D_0, 8H), Cayley index of 69 (7D), prop:polarcap in T (2E), R153_005 Thm A uniform in T (4E), G2_B6_R5 Prop C (6E), G2_B7_R5 multigenerator rigidity (6F), LP-152 Gaussian prime correlation (6F), R157_004 O4 Kreĭn data at the first crossing (7E), R161_073-074 residual upper certificate (3D)
  **Part 19 update:** prop:polarcap (2E) **DONE** (closed earlier by R160_M4_R1 and R162_703; Lemmas 1–2 of R184_012); LP-152 (6F) **DONE** (R160_M5_R1 Cor 2.4, DEAD [F3: DH, Epstein, Ξ_a]); G2_B7_R5 (6F) → (Q*), **NO-GO as a route** (R184_011); I11 (4H), I14 (8H) and the Cayley index of 69 (7D): **no statement**, not routes (R184_012); R161_073–074 (3D): **E1** (certificate, not mechanism; R184_012). (P153.4) closed by R153_010 (R184_007). Still unattacked: I6 (3A), R153_005 Thm A uniform in T (4E), G2_B6_R5 Prop C (6E), R157_004 O4 (7E).
- *(part 7)* New residuals from rounds 22–24, unattacked: O2201.1 asymmetric nodal weight (zero side) → 8B/5C; OS-2 witness parity → 6C; O2302.2 c_f≠0 from integrality → 5F; O2302.1 finite-N remainder → 5F; O2202.1 [prim] version of NI → 6B; O2401.1 sizes of V(F_M), H(F_M) → 7D.
- *(part 8)* Rounds 25–26: item 3 (exclusion conjecture, 4D) = C_B → O2601.1; items 15 and 21 (8D) **DONE** (NO-GO, R162_2602); item 39 (C_B, 8F) route (a) **DONE** (NO-GO, R162_2501), residual O2601.1; Γ–Euler detector R161_068–070 (4D) **DONE** (NO-GO, R162_2502, folded into 1603 (d)). New residuals: **O2601.1** (converging lemma, 8F/8D/4D/7E), O2602.2 (δ=2?, 8D), O2501.2 (e<1 ⟹ Θ<1 without finiteness, 7E).
- *(part 9)* Rounds 27–28: items 12 and 47 (O8 Tate 2×2, 4E) **DONE** (NO-GO, R162_2701); item 4 (doc 107, 4C) **DONE** (closed by 108, R162_2702a); item 51 (NG-D4, 1D) **DONE** (DEAD, 2702c); item 36 (boundary triples / B_CCM) **DONE** as NO-GO for O2601.1 (W3), but the calculation must be redone with (4,4) deficiency (2890). New residuals: O2801.1 (4F), O2802.1 (4F/row 5), O2702.1 (Burnol, RH-neutral, 1D).
- *(parts 10–11)* Round 29 and phase 163: items 28 (P2) and 29 (lem:degen, except log 2) **DONE**; O2801.1 (4F) **DONE** negatively (R162_2901). **O2601.1 is now sharpened to the discrete Beurling frontier BF_θ^disc** (5G): does every discrete Beurling system (integer prime multiplicities) with N=ρx+O(x^θ), θ<θ₀≈1/3, satisfy RH? In the extended class the answer is NO for every θ (ζ_θ); the analytic NO-GO (R163_101 §5) forces use of the prime multiplicities' integrality; the perturbative NO-GO (R163_102 §4) says a θ=0 countermodel must differ from Π_ζ on a set of abscissa >½. New residuals: O163.101a (C_{1/3}; the K(y) bound is a sketch, R163_191), O163.101b (Θ<1/3), O163.101c (Révész Obs. 7 / Hilberdink 2010: discrete θ<½ ⟹ zeros with β>θ; does it sharpen toward the line?), O102.1–3 (5G).
- *(parts 12–13)* Rounds 31–37 of phase 163: O163.101a (C_{1/3}) **DONE** on θ∈(1/3,½) (Theorem C, R163_803, audit 891 VALID WITH FIXES; novelty R163_892 pending Diamond–Zhang ch. 17). New residuals: **O163.803a** (negatively correlated rounding, low van-der-Corput-type discrepancy over the Witt collar, to push the error below x^{1/3}; L2a of R164_000) → 5G; **BF_θ^disc with θ≤1/3** (sharpened; L2 of R164_000) → 5G; (★_cell) at the witness in tail form (TC) (R163_401, R163_801 Cor 3.1, R164_000) → 7B/4F/7F.
- *(part 18)* Phase 166 rounds 9–12 and phase 167: item 46 (7C) **DONE** negatively (R166_801). New residuals: **C1/C2** (R166_701; rigidity at θ = 0: C1 every θ = 0 system is ζ up to a finite Euler modification, C2 there exists a θ = 0 with a zero off the line; both OPEN, if C1 then C2 ⟺ ¬RH) → 5G; **O167.101.1** (Dom_θ) and **O167.101.2** (small-y regime: an on-line count finer than S = O(log t), not a bound on Λ) → 7D; **O166.802.1** (circularity for arbitrary non-linear B) → 3A; **O166.501.1** (meta: must a separating H with no Z^off be non-linear in Λ beyond the window?) → 7B. Exact stopping point of R167_102 (OPEN, no literature): large-values bound for Type II products of length X at a single height → 3A.
- *(part 17)* Phase 166: residual OS-2 (6C) **DONE** negatively (R166_202) and replaced by **O202.1** (T_e = T_o for ζ, no sign) → 6C. **ω(E)** (7A) is restated as the **global phase** of G at t_q (harmonic measure of the node set; R165_201 Thm 2), not a local nodal datum (R166_201 Thm 1.3: Re G(t_q)² = jet k=−1). Five new mechanisms DEAD with proof (R166_101, 102, 103 α/β/γ, 201, 202).
- *(part 16)* Phase 165: item 25 (D.16-γ) **DONE** negatively (R165_201 Thm 3(a), R165_202). New residuals: **ω(E) at contact = Rem 4.8a** → 7A; **O102.1** (explicit Gevrey γ₁(ψ); does H=3·10¹² suffice?), **O102.2** (Det− with δ*Λ*≤y₀; needs O701.2 and Cor 2(c)), **O701.1** (remove (Dom)), **O701.2** (sub-Landau lower frame), **O701.3** (medium regime) → 7D; node monotonicity and parity simplicity (R165_202) → 7E. (★_cell) remains OPEN.
- *(part 15)* Phase 164 rounds 3–4: O164.501.1 **DONE** (R164_601 Prop 2.1: the test exists, dlVP over G²; gives no new inequality, Thm 3.1–3.3). New residuals: **O164.601.1** (lower bound of Σ_{q′}Re[G(t_{q′})²K(t_{q′})] for K Poisson/trig localized at γ_q = (★_cell) weighted by K) → 7F; **O164.503a–d** (quadratic mean §3.3; Huxley exponent; non-rescaled θ<1/3 system; "returns to" clause) → 5G. (★_cell)/(TC) remain OPEN.
- *(part 14)* Phase 164 rounds 1–2: O163.803a (L2a) **DONE** negatively in 𝒦_θ (Theorem L, R164_201/291); O164.101 = O164.102.1 **DONE** negatively by identification (Thm R, R164_401: O164.101 ⟺ ¬RH). New residual: **O164.201a** — discrete Beurling system off the Witt lattice, error O(x^{θ′}), θ′≤1/3, with a zero of β>½ (that it must lie off the lattice is ARGUED, via L*) → 5G. (TC)/(★_cell) remain OPEN (7B/7F).
- Closed since being listed: "density of H¹_alg" (R160_S5 §3.3) is **DONE** by R160_C3 Thm B. Items 1, 2, 3, 5, 6 and 7 of R162_590 §2 are **DONE** in 162 (502B, 703, 504, 1001, 1203; Beurling test).

**Total: 59 entries (+1 block of part-7 residuals); items 45 and part of item 46's 5F DONE in part 7, ≈90 open atomic items (2 DONE within the list and 2 more already closed). The old D.172 certificate at ½log5 is downgraded; the DONE of item 20 refers to the 162 certificates, independent of D.172.**

## 7. Reverse-engineering specification of a closing argument, and ranking

A closing argument MUST satisfy all of the following (S1–S8 are from R162_2200 §5; S9–S12 come from earlier walls):
- **S1** use λ=0 non-perturbatively, with no jet λ·⟨…⟩ (W5).
- **S2** be non-linear and non-polynomial in the test c (or in F): the polynomial case collapses to Sonin (1202 Thm C) and linear integrality is Poisson (1902).
- **S3** not be orientation-invariant, i.e. not contain the square of (PC) or of the truncated Weil form (W4).
- **S4** separate ζ from *the whole* §4 table at once, in particular from Beurling DMV and from Λχ₂. That requires using ℤ-integrality and the exact values together.
- **S5** not be a per-window statement with a gap (M, 2101) nor the "∀T" of a per-window law (E1). It must be an object in T that is not a restatement.
- **S6** not be Hecke-equivariant nor window-translation-equivariant (W7, I-13).
- **S7** bring in the Euler product before regularizing and after resumming the EF (204, 305, 1003).
- **S8** not be a weight-blind spectral criterion (Type I curve).
- **S9** be field-uniform or name the property separating ζ from ζ_K/S₃ (T1). It must use A7–A9 (Euler) and not only A1–A6 (T2).
- **S10** not need an h⁰ with (a),(b′),(c) (Thm 19.25) nor an MW-5 object that postulates positivity (W10).
- **S11** couple primes and the archimedean place in a way that is not already the RH statement (meta 136). So it must be *weaker than ⟺* at some intermediate step, like C_B or LP-112.
- **S12** not depend on a finite set of zeros (finZ) nor on a numerical margin (M).

**Ranking of cells and residuals** (updated after rounds 25–26, part 8):

*NO-GO in part 8:* 8F route (a) of C_B (R162_2501: 2β* law, M_m), 4D Γ–Euler detector (R162_2502: Thm D/K, Prop A), 8D PATH-TO-D (ii) + CC Sonin count (R162_2602). **Convergence:** the surviving residuals (8F, 8D, O2501.1, 4D's exclusion, 7E's C_B) reduce to ONE lemma, **O2601.1: an individual property of the Euler product of ζ that uses the exact values of Λ non-linearly and bounds the off-line count; it must fail for deletion, M_m and Λ̃** (by 2501's Thm 3 and Hamburger rigidity, no class argument works).

*Current ranking (part 18) — phases 166 (rounds 9–12) and 167 CLOSED:* the survey of ≈230 mechanisms (R166_400–405) gives two families that never touch, P = {i,ii} (15, fall by E1) and Q = {ii,iii} (30); {i,iii} empty, and by **Thm A of R166_501** that is a theorem: (iii) alone ⇒ (ii). The three P↔Q crossings are settled (P7+Q25 repeated; P1/P5+Q1 tautological; "Q + global phase" excluded by Thm A). The Beurling frontier below 1/3 remains open on both sides but fails (N) as a route to D (N blind to zeros). 7C closed. **Final requirements: (G)** a non-constant invariant S of the witness, global in X (degree 0 allowed); **(N′)** control of Λ beyond the window with the strength of zero localization (= localized RH; R166_802). **Exact remaining target (WS\*)** (R167_101): Re Σ_{n≤Y}Λ(n)n^{−½+iγ_q}w(log n) < (1−θ)c_Θ\|G(t_q)\|²\|k(−iδ_q)\| − E_K/4, with w = (e^{−iγ_q·}g)*ǩ, the sum over all of [1, Y], given (Dom_θ) (O167.101.1); it is a single-scale polylogarithmic bound, of RH quality. Status (R167_190 after audit R167_291): **unreachable by the sieve class** (Thm B′, b_θ; DMV/Zhang), **its scale-uniform form ⟺ a zero-free statement** (Thm C / Landau), **at a single scale it is an evaluation of the explicit formula** (Thm E). It is not "uniformly false" (Lemma K downgraded). (★_cell) and row D OPEN.

*Ranking of part 17 — phase 166 CLOSED (rounds 6–7):* five new mechanisms (nodal singularity, flow in s, free mechanism α/β/γ, sine–cosine, parities) closed with proof; OS-2 closed negatively. Final obstruction (R166_190): every proof of (★_cell) must **(i)** be global over the node set X (not local in jets), **(ii)** couple X with the atomic prime side beyond the window, and **(iii)** not reduce to (1.1) on a test. No mechanism in the corpus satisfies (i)–(iii); every future route must declare how it satisfies (i)–(iii) and name the wall it evades (§0, §3 wall dichotomy, W-jet) before relaunching. (★_cell) and row D OPEN.

*Ranking of part 16 — phase 165 CLOSED:* the geometric branch (critical interlacing ⇒ quartet off the cone) is **refuted with proof** (R165_201 Thm 3(a)); "contact ⇒ EC" DEAD (R165_202); Det− DEAD as a route (R165_102). **Bracket of T_c PROVED:** 0.8047 < T_c ≤ min_ρ τ(ρ), τ(ρ) ≤ T_L(γ_ρ)+0.226 (clustering caveat). The quartet's sign at contact is carried by ω(E) (= Rem 4.8a). (★_cell) and row D OPEN.

*Ranking of part 15 — phase 164 CLOSED (rounds 1–4):* every route opened by R164_000 is closed with proof (L1a E1; L1b Thm A + Thm R; L2 Theorem L, and below 1/3 off the lattice OPEN with a positive direction ≥ RH + quadratic GRH; determinant/moments = window data; sinc on the zero side E1 with no room; dlVP over G² W2/M). **Identification theorem** (R164_190 §Round 2) + Thm R: no class property separates ζ without identifying it. **Every route returns to (★_cell)**, i.e. RH at the witness, with R163_401's geometry as the form of the proof. Rule §0: none of these cells is relaunched without an idea naming the wall it evades.

*Ranking of part 14:* **every class route is closed by identification** (W-identification, §3): the lower separator 1 (Euler product above the window, L1) died — (KZ) is E1 (R164_101), the positive tail is blind to zeros without EF (R164_102 Thm A) and with EF the witness class is {ζ} (R164_401 Thm R). The only content that is not identification is **BF_θ^disc with θ≤1/3 off the lattice** (O164.201a, 5G; L2a closed negatively in 𝒦_θ by Theorem L). (★_cell) must be proved for ζ individually from the comb / the explicit formula at every height; equivalently (TC).

*Ranking of parts 12–13:* separators **REMOVED**: (i) on-line abundance (Levinson/Conrey, positive proportion or 100%): Bombieri–Hejhal (Duke 1995; R163_602 F2, PROVED-CITED) gives, for DH-type combinations, 100% of zeros on the line conditionally and still infinitely many off it; (ii) Riemann–Siegel/AFE structure: EF-only data, shared by f_χ (R163_603 L2.1). Frequency integrality is either identification or blind to the sign (W3′, Thm O). **Two** remain: 1. **the Euler product above the window** (tail 𝒯_X of −ζ′/ζ with X=e^{2T_c}, used non-linearly; tail theorem (TC), line L1 of R164_000: Gonek–Hughes–Keating hybrid cutoff; cells 4F/7F/7B); 2. **BF_θ^disc with θ≤1/3** (5G; line L2 of R164_000: L2a construction via O163.803a or L2b positive direction).

*Ranking of parts 10–11:* 0. **O2601.1 in its sharpened form BF_θ^disc** (5G, discrete Beurling frontier): discrete systems with N=ρx+O(x^θ), θ<θ₀≈1/3 ⟹ RH? It satisfies S4 only if it uses the integrality of prime multiplicities (ζ_θ kills everything else); it satisfies S11 because it is a class statement not equivalent to RH (ℤ has θ=0 with margin), but its ℕ-comparable part is RH-equivalent (Cor F), so the novelty must lie in the non-comparable systems. Heuristic threshold θ₀=1/3 (C_{1/3}: random rounding; datum: quadratic Dedekind systems have θ=1/3). Literature: Broucke 2409.10051 (Thm 1.2, §6.1, Thm 6.3), Broucke–Debruyne–Vindas 2004.11501, Révész 2207.00665 Obs. 7 (via Hilberdink 2010: the only integrality-over-zeros result, pushes zeros to the right of θ, not onto the line), DMV (secondary) and Zhang 2007 (secondary; error x^{½}exp(c(log x)^{2/3})). O2801.1 CLOSED (2901); 6D P2 DONE, 6A lem:degen PARTIAL (2902).

*Ranking of part 9:* 0. **O2601.1**, with two sub-forms: **O2801.1** (dN₀≥0 for ζ₀=ζ/R with real zeros, 4F) and **O2802.1** (non-formal property, uniform in k≍log x, of the whole b≡1 book, 4F/row 5). All residuals converge here. NO-GO in part 9: 4E Tate 2×2 (2701), 1D NG-D4 + boundary triples (2702b/c), 4C doc 107 (2702a), two angles on O2601.1 (2801, 2802). Still unattacked: 5E/5F (non-linear integrality); 6D/6A (P2, lem:degen) in progress (R162_2902); O2801.1 in progress (R162_2901).

*Ranking of part 8:* 0. **O2601.1** (converging lemma; not ⟺ RH, S11). Unattacked items: 4. 5E/5F integrality; 5. 4E Tate 2×2; 6. 6D/6A; 7. 1D NG-D4 + 4C doc 107. Items 1 (8F), 2 (4D) and 3 (8D) below are now NO-GO.

*Earlier ranking (part 7):*

*Already NO-GO:* old #1 5C×8B Blaschke–torsion (R162_2201/2202; residual O2201.1 = zero side), old #2 6C Selberg difference channel (R162_2301 + 2401: hidden contacts do not force a sign; only OS-2 parity remains), old #3 5H o-minimality/Pila–Wilkie (R162_2402: W10+W8), old #5 5F weak renormalization limit (R162_2302: limit ≡0; only c_f≠0 remains). The common lesson: nodal quadrature (Thm Q) is exactly W≥0 at type ≤2T_c, so everything read at the nodes is E1 or zero side.

1. **8F/4E/7E, dichotomy m<∞ ⟹ m=0** (LP-112, L8, C_B). It is one of the few intermediate statements *not* equivalent to RH (S11) and uses Euler three times (S7). Risk: no precedent; P33 notes that finiteness A has Lindelöf strength.
2. **4D, Γ–Euler detector −ζ′/ζ(2m+1) (R161_068-070).** Faithful arithmetic detector off the axis (S7, partial S4); missing the primitive Weil comparison. Risk: a detector might not force the sign (lesson of 66–80).
3. **8D, PATH-TO-D (ii) + CC's Sonin count (115_15)**. Analytic (S10) and computable. Risk: E1 by compression (A_T=Σ_ρ in 118).
4. **5E/5F, non-linear integrality tracked in T** (O1802.3 + O2302.2: c_f≠0 from integrality). The only part-7 residual that calls for ℤ-arithmetic and not the zero side. Risk: c_f is an outer Tate moment (zero-side, W6).
5. **4E, canonical Tate 2×2 transfer system / κ₀+|S|→0 collapse** (§6 item 47) and **R153_005 Thm A uniform in T** (§6 item 59): never attempted, S7.
6. **6D/6A, P2 (identity for S_even) and lem:degen**: cheap, never attempted; tools, not closure (fail S5).
7. **1D, NG-D4 Fourier anticommutation Q(f,g)+Q(f̂,ĝ)=0** (§6 item 51) and **4C doc 107 W_2** (§6 item 4): never attacked.

Discarded by the specification: 7D (M, S5), 3C (E1 by M7), 1E A.15 (dBN flow blind to arithmetic, W3/N5), 2G §28.4 (W10), 8H D1 (costly and barely falsifiable; only if 1–5 fail), 6C OS-2 (parity = the sign), 8B/5C O2201.1 (zero side, W6), 3A Problem A (certificates, S12).

## 8. Maintenance

1. **Add a route:** add an object to `cells[i].routes` of the JSON with `{id: "R16x_NNN", name, row, col, status: DEAD|PARTIAL|OPEN|PROVED-TOOL, killer: "E1;F3:DH;M;W…", note, supersedes_or_dup: "<earlier id>" or "", source_part: 7 (=phase ≥163; parts 8–9 are rounds 25–28; part 6 is the 160–161 sub-audit)}`. Use the W1–W12, F1–F4 and F3:<falsifier> keys from §3–§4 in `killer`.
2. **If the route kills a live residual:** remove the `live_residuals` line from the cell, and also put `supersedes_or_dup` on the new route and mark the old OPEN route as DEAD (do not delete it).
3. **Recompute the status:** □ if there are no routes; ◧ if some unsurpassed OPEN/PARTIAL route remains; ◩ if all are dead but `live_residuals` is non-empty; ■ otherwise. Update `counts`, then the §1 table, the cell's §2 section, the count, and §6 (mark DONE).
4. **New wall:** if a killer appears in ≥3 cells, promote it to W13… with its statement and its first and last appearance. If a new falsifier appears, add a row to §4.
5. **Every 3 rounds:** audit the map against the cited files (editor's rule, feedback-check-against-paper-definitions). No audit has reversed a NO-GO so far; if one does, the cell returns to ◧.
6. Regenerate the grid and sections with the `scripts/` script (or by hand) and date the header.
7. ** (editor, phase 164 L3):** merged parts 12 (R163_201–203) and 13 (17 routes from rounds 32–37 of phase 163) with the script pattern (`scripts/r162_2300_refine_grid.py`, part12/part13 block; backups `*_pre_p164*`). Count ■ 10 · ◩ 20 · ◧ 34 · □ 0, 975 routes. Added W3′ (§3), the f_χ and f_t rows (§4), residuals O163.803a and BF_θ^disc θ≤1/3 (§6) and the two-separator ranking (§7). 5E/5F: R163_1001 routes DEAD, cell symbols unchanged (previous residuals untouched). No statement label changed.
8. ** (editor, phase 164 round 2, R164_301 §6):** merged part 14 (5 routes: R164_101, 102, 201, 401, 402) with the script pattern (part14 block; backups `*_pre_p164b*`). Count ■ 10 · ◩ 20 · ◧ 34 · □ 0, 980 routes; no symbol changes (4F and 5G keep live residuals). Added W-identification (§3), Thm R and Theorem L (§5), O164.201a (§6) and the "every class route closed by identification" ranking (§7). No statement label changed.
9. ** (editor, phase 164 rounds 3–4, R164_301 §9):** merged part 15 (9 entries: R164_501, 501P, 502, 502b, 502c, 503, 601, 601T, 491) with the script pattern (part15 block; backups `*_pre_p164c*`). Count ■ 10 · ◩ 20 · ◧ 34 · □ 0, 989 routes; no symbol changes. Added Thm SA, Prop 4, L1/L4–L6, Props 1.1/1.3, Thm 3.1 (§5), O164.601.1 and O164.503a–d (§6), falsifier "windowed M_m" (§4), closure of phase 164 (§7). No statement label changed.
10. ** (editor, phase 165, R164_301 §11):** merged part 16 (8 entries: R165_101, 101D, 102, 102T, 102P, 201, 202, 202A) with the script pattern (part16 block; backups `*_pre_p165*`). Count ■ 10 · ◩ 20 · ◧ 34 · □ 0, 997 routes; no symbol changes. Added Det+, Thm 1/Cor 2(c), Thm 2/Cor 2.2, flow tools (§5); item 25 DONE, ω(E), O102.1–2, O701.1–3 (§6); closure of phase 165 (§7). No statement label changed.
11. ** (editor, phase 166, R164_301 §13):** merged part 17 (12 entries: R166_101, 102, 102F, 102I, 103A, 103B, 103T, 103G, 201, 201E, 201S, 202) with the script pattern (part17 block; backups `*_pre_p166*`). Count ■ 10 · ◩ 20 · ◧ 34 · □ 0, 1009 routes; no symbol changes. §3: W-jet and wall dichotomy; §4: P_{a,c}; §5, §6 (O202.1; ω(E) as a global phase), §7 (phase 166 closed; requirements (i)–(iii)).
12. ** (editor, phases 166–167, R164_301 §15):** merged part 18 (13 entries: R166_501, 502, 601, 701, 701T, 702, 801, 802, 802T, R167_101, 102, 103, 291) with the script pattern (part18 block; backups `*_pre_p167*`). Count **■ 11 · ◩ 19 · ◧ 34 · □ 0, 1022 routes**; one symbol changes: 7C ◩ → ■ (pair-correlation residual DONE by R166_801, rule §8.3). §3: W-sieve and (N′); §4: b_θ and DMV/Zhang as a sieve falsifier; §5; §6 (item 46 DONE; C1/C2, O167.101.1–2, O166.802.1, O166.501.1); §7 (phases 166–167 closed; (G)+(N′); (WS*)). No statement label changed.
13. ** (editor, phase 183, R183_017–020):** Connes–Consani route "Sonin trace + rank-one correction". Exact identity E_S = Son + R_{S,T} PROVED (R183_018 §3; closes the "no exact identity exists" gap of row 2A). NO-GO PROVED (two independent proofs, R183_018 Thm 5.1 and R183_019 Thm 4.1; audit review R183_020): for T>½log 2 with a prime in the window, n₋(R_{S,T})=∞ on primitives and in ker ∫h; CC's "single negative direction" structure (Lemma 6.9/Thm 6.11) dies exactly at log 2 for a structural reason (the prime term = non-compact truncated Wiener–Hopf). Obligation 3 ≡ positivity with a gap in ker ℓ (R183_019 Cor. 3.2), not an extra condition. Only (L-Son) with η<1 survives (R183_018 §6), OPEN. No symbol changes; D OPEN.
14. ** (editor, phase 183 round 2, R183_021–028):** four approaches to the Connes–Consani extension plus a decision round. PROVED: relative-0 bound of the prime term against Son (finite index for every fraction η>0, R183_023); ε is not of positive type and CC's index lives in the ξ metric (R183_026); two-boundary model reproduces the exact prime term with factor log p (R183_025). NO-GO/downgrades: the rank-one archimedean mechanism dies only at |I|≈1.61 (n₋≈4T−2, numerical, R183_026); (L-Son) with uniform η false (cond. RH, R183_027); frequency multiplier NO-GO or stronger than D_T (R183_022, Thm 3.3 downgraded to CONDITIONAL(RH)). Open and decisive: (E′) r_p∈L² (prime-free) ⟹ L1; structural requirement: every ∀T-valid positive part must have null density in the zero gap (−γ₁,γ₁), i.e. the route converges to the explicit formula. Synthesis R183_028. No symbol changes; D OPEN.
15. ** (editor, phase 183 round 3, R183_029–033):** scaling law (Λ) PROVED and exact semilocal identity Son_S − Son_∞ = prime term + ∫c_h ε'_p + ∫|φ|² r_p without hypotheses (R183_029); prime-free microlocal (M) ⟹ semilocal remainder Hilbert–Schmidt, (M) OPEN; full form S(T) with a gap up to ½log5 (Paper 47) and numerical n₋=0 up to 0.80 with a superexponential gap (R183_030); "one aligned direction ∀T" does not exist; "zero directions ∀T" ⟺ D; gap requirement under RH PROVED but trivial with P_T=0 (R183_031, downgraded by R183_032). Observed identity λ₁(ker ℓ)=λ₂(prim) to 8 digits, OPEN. Synthesis R183_033. No symbol changes; D OPEN.
16. ** (editor, phase 184 rounds 1–2, R184_001–008, audit 091):** live residuals attacked. 5G: θ≤1/3 frontier OPEN (Prop 2.1/2.2 PROVED; factor route NO-GO PROVED ∀θ<1, Lemma AC + Thm F; C1 OPEN at O(1), false at O(log x) only by modifications of ζ). Phase 170: residual = equality with no sign (W12+W5), route E1. 8F/4E/7E: C_B by inertia NO-GO PROVED for class 𝒜 (M_m has the same blocks, rank ≤6m; a valid 𝒜 ⟹ κ(ζ)=∞). (P153.5): explicit detection law T*(a,γ) PROVED under Max–Iso, empty on certified windows. (P153.4): already closed by R153_010; Theorem W weight convexity. Phase 183: constant is not an eigenvector; coincidence λ₁(ker ℓ)=λ₂ by parity (Thm A.1). No symbol changes; D OPEN.
17. ** (editor, phase 184 round 3, R184_009–013, audits 092–093; synthesis R184_099):** local 2026 literature with no surviving inputs; L* FALSE in the linear model (martingale dither, Theorem D PROVED) but the full system returns to (1−θ)/2 (ARGUED, R184_013): the 1/3 frontier stands; erratum R164_201 §1 (order-2 chaos not negligible). Item 59 pruned: polarcap, LP-152 already closed; G2_B7_R5 → (Q*)/NO-GO; I11/I14/Cayley have no statement. No symbol changes; D OPEN.
18. ** (editor, phase 184 round 4, R184_014–015):** erratum PROVED for order-k chaos (same power X^{1−2a} at every order); L*_comp CONDITIONAL on (ZF_R), with a countermodel in the relaxed class (R = L(u,χ)): the integrality of b_{p,1} is indispensable. Source/form disjunction PROVED (R184_015 Thm 2): every P = "‖Δ_T‖ ≤ e^{o(T)}" is either blind to M_m or E1; no third option except the explicit formula. New wall **W11′**. No symbol changes; D OPEN.
19. ** (editor, merge of phases 168–184, part 19):** merged part 19 (`R162_2300_part19.jsonl`, 78 entries: R168 ×8, R169 ×4, R170 ×12 consolidated per R184_002, R171 ×2, R172 ×2, R173–R175 ×6, R176–R182 ×9, R183 ×11, R184 ×18, SIGN-REAUDIT/SUPPORT-DESCENT ×3, and 3 closures from proposal R184_C6C/C7F/C7H), source INVENTORY-PHASES-168-184; backups `*_pre_p184*`. Count before ■ 11 · ◩ 19 · ◧ 34 · □ 0, 1022 routes; after **■ 13 · ◩ 23 · ◧ 28 · □ 0, 1100 routes**. Applied R162_2300_REPAINT_PROPOSAL to the 8 cells with cited proof: 2A, 6C ◩→■; 2G, 4D, 7A, 7B, 7F, 7H ◧→◩ (§2, "part19" notes). 1E, 2E, 6B, 6G, 8D unchanged (the proposal declines). §3: W11′, W-Sonin, W-factor, W-dither; §4: ℕ∪√2ℕ, R=L(u,χ), low band, P_171; §5: erratum R164_201 §1 and 168–184 tools; §6 item 59 updated. The old OPEN/PARTIAL routes of the repainted cells keep their status (as with 6C/2A before the merge); their death is recorded in the new entries and in `editor_note`. Report: R162_2300_MERGE_PART19_REPORT.md. Row D OPEN; no statement label changed.
20. ** (editor, R184_016):** A1 (R169's decorrelator) is E1 (Thm 1–2, Prop 3, given (Dom_θ)); (Dom_θ) and (P_gap) are zero-side. The minimal crossword (CROSSWORD-TO-D addendum) is left with a single blank square: **O166.802.1**. No symbol changes; D OPEN.
21. ** (editor, phase 185 rounds 1–3, R185_001–005, audits 091–092, R184_094):** "crossword" campaign on O166.802.1. PROVED (verified): finite-dimensional circularity (R185_001 Lemmas 2–4, Thm 5(a), Thm 6); circularity for infinite families in the bounded-type cone (R185_003 Thm 1; Thm 2 on W₂); Thm C convexity/solidity ⟹ blind to W-sieve and Thm F's kernel closed under deletion (R185_002); Obs 4: in 𝒟 the ζ-type EF identifies ζ alone (R185_004). Downgrades: Thm D (002) false→ARGUED; "Thm F ⇒ E1" ARGUED; U3(i) CONDITIONAL; A1 E1 only as a sandwich (R184_094). Relative barrier theorem BR assembled (R185_005): no scheme in 𝔐 excludes every witness with something strictly weaker than RH; open leaves ρ1′, ρ2, (iii-a), (iii-c)=θ≤⅓ frontier, exhaustiveness of 𝔐 ARGUED. Outside 𝔐: unbounded-type tests ((TC)/(★_cell)), zero inputs with Euler, joint (Λ,Γ) non-RH statements, operator objects (W10). Paper 47: DRAFT_SECTION_INERTIA_BARRIERS + CHECK_TABLE (not integrated). No symbol changes; D OPEN.
22. ** (editor, phase 185 round 4, R185_006–008, audit 093):** outside 𝔐. **Lemma 1.1(b) PROVED** (finite negative index ∀T ⟹ finitely many zeros off the line; sup N = 2m CITED): R183_031 Thm 1 (gap requirement) holds without RH; R184_004 Prop 2(iv) PROVED. W11 corrected: literally false for finite T (thm:C, thm:log5A, CC 6.11); W11-∞ PROVED-CITED; W11-fin with a caveat (λ_{T₀}>0 proved only up to ½log5); archimedean indefinite from 0.4608 (full) / 0.58 (primitive). Analytic proof at ½log3: NO-GO (gap_∞ = 0.084 < 0.490); symbol identity PROVED; reduction to a finite check with a tail to fix. (ρ1″) closed: unbounded type is circular; residual = partial bounds Θ ≤ ½+δ′ (quasi-RH, OPEN). No symbol changes; D OPEN.
23. ** (editor, phase 186 rounds 1–6, R186_000–009, audits 091–094):** toolbox for row D. TB-3 closed negatively (PROVED). TB-1 reduced to a ~4-mode Schur problem (edge lemma, monotonicity, pair sectors PROVED). TB-2: CCM candidates (−𝔰²+λ²N_S) and metaplectic NO-GO by exact computation; built: F_S = E F_∞ E⁻¹ unitary and involutive (PROVED), A_S = PF_SP compact non-HS with new spectrum (PROVED), Thm C exact dispersion phase φ′ = −Σ v_{2^k}cos(kt log2), Thm C′ exact linear trace (PROVED; linear part of (Δ)), Π_S Riesz projection with an unconditional operator gap (PROVED). Decisive OPEN items: TC_S, CV_S, bound on ε_S. No symbol changes; D OPEN.
24. ** (editor, phase 186 rounds 7–9, R186_010–014, audits 095–098):** semilocal Sonin chain closed for S={∞,2}: TC_S PROVED (010); operator gap PROVED, cos²θ_n=λ_n² (095); CV_S NO-GO in L^∞ (ε_S diverges logarithmically at 2^j, PROVED; 011); L2_S PROVED for d_S with β_j = 2^{j/2}(1−2^{−j})λ²/(2log2) (012); (84)_S PROVED, relative Δ ∀λ, absolute given CC 4.7 at λ=½ (014). Result: E_S = Son_S − ∫c_hε_S with Son_S ≥ 0 trace type, comb absorbed, Hilbert–Schmidt remainder ∀T. Phase 183's (M) replaced by proved (E′_loc). Reconciliation: atom in the comb, ε_S is the remainder (no double counting). OPEN: inertia of the remainder in 𝒫_T over T; S(T) increasing. No new sign; D OPEN.
25. ** (editor, phase 186 rounds 10–13, R186_015–024, audits 099–104):** semilocal chain for every finite S PROVED (015); non-perturbative S(T) limit (‖κ_{S(T)}‖ ~ e^{3T}/T², ARGUED). Consistency test C1 resolved: dictionary D0–D3 PROVED (017/099), term 2log(1/λ)‖h‖²; CONSISTENT chain; no absorption. Contact at λ=1 (018/101): no sign; **invariant ρ*(T) = sup C/Son_S** (0 at ½log2 → 0.944 at ½log3, positivity ⟺ ρ*<1); archimedean s₀ (021); Sonin density zero NO-GO (022). Single-mode alignment model FALSIFIED (023; AL-k = rewriting of W≥0 in A_∞'s eigenbasis, NO-GO as a route, 103). **Uniform 4×4 Schur NO-GO** (c = min 𝔞_T|𝒱 drops to 0.013 at T=0.69); **stable with k ≍ T equal blocks** (dim E = 2k−2): c ≥ 1.24 (k=13) on [½log2, ½log5], λ_S/λ_W ∈ [1.00,1.09]; h* lives 99% on piecewise Tate exponentials (024, NUMERICAL). PROVED: Tate sector = archimedean background of window τ=T/k; Tate cancels 2e^{−u/2} of K, residual K₁ ≤ 1/u. (L1) by operator norms NO-GO (audit 104: ‖𝒦₁‖ → π in the continuum, ‖P|𝒱_k‖ ≤ 𝒜_T/2 false for T>log2); k ≍ T stability is an approximation artefact (E_k = piecewise linear), (L2) inherits thm:margin whole. Survives and grows (R186_025, audit 105 no fatal flaws): **Thm A PROVED** c_∞(τ) ≥ log(1/τ) − C_A (C_A ≤ 1.29, τ ≤ 0.1); **Thm B PROVED** 𝔞_∞(F) ≥ (log(k/T) − C_B)‖F‖² on 𝒱_k (C_B → 1.64; Lemma 2.1 low-pass leak with two Tates per block); **Cor. (L1) PROVED** c(T,k) ≥ log(k/T) − C_B − 1.674, positive with k ≥ 25 at ½log5; ‖K₁‖ = π as a bilinear kernel, π/2 in the quadratic form (C1, Paper 47 editor) PROVED (the norm route NO-GO). **Rigorous windowed reduction: λ_A(T) > 0 ⟺ S_{T,k(T)} ≻ 0 in dim 2k−2** (48 at ½log5); (L2) OPEN, inherits thm:margin; closed form of G_EE in progress (R186_026). R186_013 closed with no progress (n₋ = ∞ of the semilocal remainder at λ=½, ARGUED). λ_min(W|𝒫_T) > 0 on the whole mesh up to ½log5 (Galerkin); beyond 0.85, a double-precision floor. No symbol changes; no contact with the sign; D OPEN.
26. ** (editor, phase 186 round 14, R186_026–028, audit 106, Paper 47 DRAFT section 3, cross-check R186_027, paper for Connes in 08-sent):** closed form of the piecewise Tate Gram matrix G_k(T) PROVED (026; Cauchy integrated at ξ = e^{2x}, primes = overlaps, prime rank linear in k); (L2_k) = W ≥ 0 rewritten (NO-GO as a route); jump kernel 𝒢_T (restatement PROVED). Index of the full form n₋(𝔞_T|L²(I_T)) = 1 on [0.12, ½log5] PROVED mod CITED (028 Thm 1.4) and an exact sector formula ∀T (Thm 1.2); the −1 eigenvalue of the Haynsworth block = rank-one pole −2ℓ_ev² of eq:W (Thm 2.1); scalar criterion = D rewritten (NO-GO as a route). NUMERICAL byproducts: A_∞ = Γ+pole dies at T ≈ 0.37 (odd)/0.41 (even), before prop:archneg's 0.4608; n₋(Γ|𝒫) 1 → 2 at T ≈ 0.8026. arXiv cross-check (027): Thm A/B PARTIAL (qualitative in Yoshida/CC 3.6; new Tate rate), blocks/K₁/π NEW, reduction ANALOGOUS to Zhu (doubly exponential k, no gain). Paper 47 DRAFT_SECTION_COERCIVITY_REDUCTION (8 pp., PROVED, C1 π/2) pending decision. Short paper for Connes written and reviewed (08-sent). No symbol changes; no contact with the sign; D OPEN.
27. ** (editor, phase 186 round 15, R186_029–031, audit 107):** synthesis 029: the margin-inheritance "Lemma H" downgraded to ARGUED by 107 (countermodel W_e = 𝔞_e + 2ℓ_ev², λ_W/λ_A ≈ 6e-5; only the inertia passes exactly); correction: W_T ≥ c on all of L²(I_T) ALREADY certified (thm:log5W, cor:KEP08). T₁ front (031): NO-GO as a route; PROVED Lemma N, optimal Lemma ½, Cor. D (λ_A ≥ λ_A^∞ − 0.490), **domination ΔSon − ΔC = −v₂c_h(log2) identically** (the semilocal decomposition does not improve the direct bound); edge bound (B_T) FALSE. Structural certificate front β₀ = 2 (030): **structural NO-GO Thm 4** (excluded class: zero presentations, and measure ν_w ≥ 0 with β = (2,0) — Thm 3 by certifiable NUMERICAL weak duality, sup inf f ≤ −0.138 at ½log3; the "Euler → zeros" reduction is ARGUED/incorrect, audit 108: the real prime-side NO-GO is lem:mbounds(iii)); exact accounting at τ=0 PROVED; obstacle: the certificate needs negative mass outside the window (‖ν‖_TV/ν(ℝ) ≈ 52 in thm:C). New wall **W-lin**: fixed-basis linear certificates, congruence/Schur/inertia reductions and norm bounds in the semilocal chain decide no new window (R155 Lemma R + R185 circularity + R186 rounds 14–15). Residuals: R30.1, R30.2. No symbol changes; no contact with the sign; D OPEN.
28. ** (editor, phase 186 round 16, R186_032–035, audits 108–109):** synthesis 032: none of the three classes outside W-lin ((★_cell)/(TC), ν with ≤k atoms, archimedean Bochner) has a positive statement attackable with the new tools; **specification Ω of the missing tool** (S1 non-linear in F; S2 Λ beyond the window at the node frequencies with strength (N′); S3 structural verification; S4 non-identity/one-sided/class; S5 node↔Λ coupling; S6 admission against M_m, f_t). New insight (033): windowed PNT identity PROVED but = Paper 47 rem:Cheb (audit 109); "O(1) margin in the negative archimedean cone" FALSE (S-lemma: inf decays ≈ λ_A^{0.7}); log-convexity of λ_A NO-GO; Lemma 2 (e^{−s_T} positive kernel, Feynman–Kac) PROVED standard. Window determinant (034): det(1−A_S²) diverges; Γ^{−1/2}Π_TΓ^{−1/2} ∉ S_p; σ_T outside Szegő/Widom/Basor–Widom; **built D_B(s;T) = det(1 − s·Pos^{−1/2}Neg·Pos^{−1/2}) entire (Thm 2.1 PROVED), λ_A > 0 ⟺ β_max < 1; Thm 3.1 (general inheritance): any determinant whose sign decides λ_A factors as λ_A·R, a leading term with multiplicative error O(1) never decides → NO-GO as a route**. Findings: rank cancellation ≈ the Shannon number of the negative set (2.4/7.0); bound n₋(𝔞_T|𝒫_T) ≤ 4/10 (improves prop:NC). New wall **W-det** (determinants and Szegő asymptotics do not decide the sign). Audit 108 on 030/031: W-lin confirmed, with the excluded class sharpened (ν ≥ 0 with β = (2,0)). No symbol changes; no contact with the sign; D OPEN.
29. ** (editor, phase 186 round 17, R186_035–036):** cone of (★₃₃) NO-GO verified (c_𝒞/λ_A ≈ 10³ constant; lemmas 3.1/3.2/4.1 PROVED). "Family in T" route closed: **Theorem 3 (R186_036), bounded rank: CONDITIONAL [audit R186_114: f_t's primitive witness is ARGUED (Cor F), only the L²(I_T) witness is PROVED]: no functional of the family {λ_A(T′)} decides D (bounded rank: falsifier f_t; unbounded rank: equivalent to L = lim λ_A ≥ 0; M_m shares every qualitative property)**; transport between windows trivial (λ_A(T) ≥ λ_A(T′), with no edge terms or new primes); dual certificates inherited downward (Lemma 1′). New wall **W-fam** [sharpened by audit 110: excludes functionals of {λ_A(T′)} of bounded rank and the limit L alone; does NOT exclude **two-sided asymptotic laws** λ_A(T) = L(T)(1+o(1)) with L > 0, which are stronger than D, are not refuted by f_t and are not shared by M_m: a new box, distinct from S2 = O166.802.1]. Balance of the "toolbox" campaign (rounds 1–17): built and proved — the semilocal chain ∀S, Thm A/B, finite reduction, sector index, closed Gram, D_B, Theorem 3; closed by impossibility in-class: literal Sonin, alignment, stable Schur, Gram/index/scalar criterion, norm bounds, structural certificates, determinants, log-convexity, PNT-cone, family in T. **The only blank box remains O166.802.1 ≡ Ω's S2 (Λ beyond the window at the node frequencies, non-linear in F), with open leaves of the BR barrier theorem (ρ1′, ρ2, (iii-a), (iii-c) = θ ≤ ⅓ frontier).** No symbol changes; no contact with the sign; D OPEN.
30. ** (editor, phase 186 round 18, R186_038–040, audits 111–112):** construction of S2 (038): three NO-GO seeds (fold/Grönwall empty = true-if-D; fourth moment already closed; future-prime alignment dominated by the pole); Lemma 0 = R165_202; S2's trilemma is not exhaustive (it omits degree-0-in-F functionals: nodes of ĥ*; unexplored). Two-sided law (039/040): = Zhu's Conj. 12.1; **the leading Landau–Widom term does NOT fix the sign (it predicts β_max > 1); prolate tail ARGUED; the head block = functions vanishing at zeros ≤ T* = 2πe^{2T} (vanishing confirmed to 1e-25) = explicit formula / Zhu's low-zero sampling; total inheritance via lem:roughEF; the value 𝔞(u_j) comes 85–91% from zeros in (T*, 10T*), not from the low ones.** New NUMERICAL: λ_A(0.9) ≈ 5.8e-17, λ_A(1.0) ≤ 4.2e-23 (mp, positive Galerkin upper bounds). BL box OPEN with no tool. Balance: every reduction interior to the window (Sonin, Schur, Gram, determinant, beam) is the explicit formula under another name; the only unexplored direction: degree-0-in-F functionals (minimizer nodes) with Λ beyond the window. No symbol changes; no contact with the sign; D OPEN.
31. ** (editor, phase 187 "pattern", campaign of 46 non-contiguous windows (T ≤ 1.075, Galerkin-certified balls, mp): λ_A > 0, n₋ = 0 throughout; new values beyond ½log5 (0.9 → 4.7e-17; ½log7 → 1.0e-21; ½log8 → 8e-26; 1.075 → ~1e-29). **Descriptive CONJECTURAL law: −ln λ_A ≈ 13.0e^{2T} − 24.6T − 18.7**, predicts out-of-sample to ¼ digit; smooth across prime entries; K = N(T*) ± 1 in 40/40; Zhu's 2π²N/ln N pre-asymptotic here. **Falsifier M₁ executed: shares λ_A (0.2–3%), K, parity, peak and staircase, and with δ = 0.1/0.3 is negative (n₋ = 2) keeping K and parity ⇒ every pattern of window observables is a class property (W-pat; the M₁ half is NUMERICAL with a PROVED falsifier in 𝒫_T, R162_2501; the f_t half is CONDITIONAL, audit R186_114).** Phase 186 rounds 18–19: two-sided law = Zhu's Conj. 12.1; the real object is not on a plateau ("sub-Shannon sea"); the sign = the extreme eigenvalue of a truncated Wiener–Hopf operator W_T(σ₊ − σ₋/β) at the crossing of inertia with an oscillating symbol (OPEN, no literature); nodal measure = lem:roughEF rewritten (nodes = zeros below T*, as expected). No symbol changes; no contact with the sign; D OPEN.
32. ** (editor, phase 186 round 20: truncated Wiener–Hopf route, R186_043, audit R186_114):** corpus cross-check: new formulation (R186_042), anticipated by thm:W, prop:negtrace(v), R186_004, R186_039 §2.3; no literature. **Lemma M0 PROVED (minimal model, a single sub-Shannon negative interval): sign = Kreĭn formula β_max = ν⟨Pos⁻¹ψ,ψ⟩; local condition at ∂U: negative mass·T² < (2/κ)·slope of σ₊.** Lemma M1 PROVED (step): interference O(1/(T·dist)), the real object is coupled (T·dist ≈ 1.6–2). **Transfer to σ_T: the local per-component condition FAILS on ζ (rescued by Tate + coupling) → NO-GO as a local criterion; the necessary rank condition #comp (beam over the span of modes ∩ 𝒫_T) gives the correct sign on ζ with its own margin (2.6e-6 at ½log5) and FAILS for M₁ (−1.16e-3): the first quantity ≠ λ_A that tells ζ apart from the falsifier.** OPEN for an ∀T theorem: Kreĭn with a linear minorant for unions + non-Gershgorin interference bound + comb phase alignment in the low components. Falsifier audit (R186_114): M_m PROVED and correct (δ → 0 limit = ζ with a triple zero at γ₁); f_t primitive witness ARGUED → entries 29 and 31 sharpened; **R185_005 §2.1 (BR) invokes the forbidden equivalence: must rewrite.** No symbol changes; no contact with the sign; D OPEN.
33. ** (editor, R185_005B):** BR barrier theorem rewritten without the forbidden equivalence (03-research/phase-185-crossword/R185_005B_BR_WITHOUT_EQUIVALENCE.md). The equivalence was a logical step only in Conclusion §2.1 (via I1), §2.4.3, N-I(ii) and node N-U2: WITHDRAWN. BR in D-only form: (0) PROVED (with R186_037 Thm C/E; leaf ρ1′ → ρ1‴), (a) PROVED, (b) PROVED restated (exclusion (★_π) for ζ with no arithmetic hypothesis), (c) PROVED by scope; Conclusion "nothing strictly weaker than D" PROVED relative to 𝔐 modulo ρ1‴, ρ2, N-EX (ARGUED). No conclusion dropped to OPEN. I11 with f_t: CONDITIONAL. Changes to the BR wall (§3) and to log entry 21: "weaker than RH" → "weaker than D"; U2 "E1 sandwich" → "OPEN (selector)"; remove "E1" from U3(i); crossword §4.2 and item 7 and DRAFT_SECTION_INERTIA_BARRIERS: replace the statement with §2.1 of the new file before integrating. No symbol changes; D OPEN.
34. ** (editor, phase 186 round 20 closed, R186_044, audit 115):** truncated Wiener–Hopf route: Lemma M0 PROVED (minimal model), Lemma M1 corrected (cross leak), Thm 2 exact Schur PROVED (λ_A > 0 ⟺ prolate block ≻ 0 ∧ coercive complement ∧ ρ_T < 1; inherited). **New facts: with Tate the per-component diagonal is positive on every window and all of λ_A's decline is done by the coupling G, with no sign structure; comb phase alignment is tautological (FALSIFIED); the M₁ quartet is rank (2,2) with Kreĭn threshold δ_c = √(λ_A/4|ĥ*′(γ₁)|²) (Lemma P, 1–2%); in the blind regime the ζ/M₁ difference is a functional of h*, not of σ.** Conclusion: every first-order discriminating quantity is a functional of the minimizer; the sign is neither local, nor finite-rank, nor phase-based. New wall **W-loc** (local/finite-rank criteria on the symbol). (L-W) coercivity of the prolate complement remains a likely lemma with no consequence for the sign. No symbol changes; no contact with the sign; D OPEN.
35. ** (editor, phase 186 round 21, R186_045):** round-20 synthesis. Flow in β/T NO-GO (coefficient dominated by h*(T)²/λ_A, Hellmann–Feynman PROVED); T → ∞ premise false (σ_T does not converge); **Theorem X PROVED mod LW: positivity ∀T forces new primes to cancel σ_{T₀} on U_{T₀} with exact sign and magnitude at resolution π/T** (= R183_031 + (N′)), X from (m, Λ) OPEN = Ω's S2; **beam moments: Lemma T PROVED (every universal order-k criterion on moments has margin ≤ k(1 − β_max)), Lemma T′ (every continuous functional of 𝔞_T|𝒫_T)**: new wall **W-mom** (no finite number of traces decides the sign with its own margin). Round 21: (L-W) coercivity of the prolate complement; windowed Theorem X reserved with constants. No symbol changes; no contact with the sign; D OPEN.
36. ** (editor, phase 186 round 21 closed, R186_046–047):** windowed Theorem X PROVED mod LW (averaged only; empty for T ≤ ½log7 with η = 0.1); **converse NO-GO with a number**: fails on the NEW negative set (from ½log3 to ½log5, 70% of Neg(h*) lives in the component created by the newly entered primes) and in the plunge; the arithmetic form of X is lem:roughEF + (N′) (not a new statement about Λ); the new primes do NOT cancel σ_{T₀} component by component; M₁ satisfies windowed X while being negative. Ω's S2 restated with two terms: (N′) per packet + "no creation of negativity outside U₀ as seen by U₀'s prolates" (no analogue in the corpus). **Lemma (L-W) PROVED with a quadrature-certified version** (Lemma 3: Cavalieri over sublevels with deflated time-bandwidth — new tool): λ_A(T) > 0 ⟺ C_T ∧ ρ_T < 1 in dim 2·#comp; fit for Paper 47. New localization: each window's sign is carried by the negative component newly created by the latest prime (dynamics in T, not local). No symbol changes; no contact with the sign; D OPEN.
37. ** (editor, phase 186 round 22 closed, R186_048, audit 116):** correction to entry 36: "the sign is carried by the newly created component" WITHDRAWN (QR artefact in 046 §3 and a single-case reading; R186_048: h* never moves to components ex nihilo, the 70% component is a product of FISSION of U_{½log3}). Lemma 3.1 PROVED (at T_n the form changes for no F: c_F(log n) = 0); ex nihilo births with Shannon number < ½ and O(1) mass (PROVED from σ); no arithmetic birth law (Weyl). Perturbative continuation lemma NO-GO (inherits λ_A(T_n), regime from 25% → 4% of the interval). All of the sign's dynamics lives BETWEEN births (M₁ changes sign at T ≈ 0.573). (L-W) PROVED modulo floating quadrature (Lemma 3 deflated Cavalieri, new tool, fit for Paper 47 with V′). No symbol changes; no contact with the sign; D OPEN.
38. ** (editor, phase 186 round 23 closed, R186_049):** S2's second term ("no creation of negativity outside U_{T₀} as seen by the old prolates") ELIMINATED as an independent object: ν(T₀,T) is O(1), dominated by fission glued to U₀, blind to the sign (identical for M₁ across the sign change); the old/new partition is an exact restatement (Prop. 2.1 PROVED) with the whole sign in β_new ≤ 1 = D. **Toolbox campaign balance (rounds 1–23): seven proved walls (W-lin, W-det, W-fam, W-pat, W-loc, W-mom, perturbative continuation) and the unifying fact: every first-order quantity distinguishing ζ from a negative is a functional of h*, not of σ. Single box: Ω's S2 = O166.802.1, now with no candidate object in the corpus.** No symbol changes; no contact with the sign; D OPEN.
39. ** (editor, Paper 47):** sections 16 (inertia and barriers), 17 (semilocal Sonin at the first prime) and 18 (archimedean coercivity and finite reduction) INTEGRATED into main.tex (88 → 104 pp., zero errors, N1/N3/N4/C1–C9 conflicts resolved against the paper's own definitions, precedents cited, zero forbidden vocabulary; backup main_pre_integration). Draft of the Wiener–Hopf section (10 pp.) and Part IV of the check table ready for decision; memo fixes: C-W1 (R186_034 sandwich mixes extremals), C-W2 (R186_042 Thm 2.3: cot²φ, not tan²φ). Round 24 (witness theory, R186_050): absorption PROVED (D ⟺ T_c = ∞), node lemma, freezing lemma (NO-GO of the asymptotic witness mechanism), M₁ satisfies every known necessary condition ⇒ is consistent; object with content **(E_γ): limsup_T 𝔖_T(γ) ≤ m(γ)** (twisted Chebyshev sum without the polar term; D ⇒ (E_γ) PROVED), under evaluation as the arithmetic form of S2 (R186_051). No symbol changes; no contact with the sign; D OPEN.
40. ** (editor, phase 186 round 24 closed, R186_051):** construction of the coherence functional: NO-GO as a discriminant (Prop. 2.2: no pointwise functional of σ separates witness from non-witness with margin > (2δT)²/3; Prop. 4.5: no BOUNDED functional of σ implies D — 1e-5 sensitivity in v_n flips λ_A). **New tool PROVED: Nyquist identity (Thm 4.1): the window form only sees the symbol on the mesh kπ/2T.** Prop. 3.3: (E_γ) requires the full 1 → ½ exponent improvement of ψ's error in twisted form, with no intermediate form (= absence of quartets, zero side). Precise statement of the missing mathematics (Ω's S2): **a signed pointwise bound on the twisted Chebyshev sum Σ_{log n ≤ 2T} v_n cos(ω log n) − polar, at the ~N_Sh Nyquist points correlated with 𝒫_T's admissible samples, with exponent-½ strength**; the large sieve (sign-free L²) and Vinogradov–Korobov (exponent 1 − o(1)) do not give it. New wall **W-coh**. Comb truncation bug in r043 for T > 3.8 (fixed in r051). No symbol changes; no contact with the sign; D OPEN.
41. ** (editor, phase 186 rounds 25–26, R186_052–053, audits 117–118):** "algebra of D_T": exact Nyquist identity with s_T (truncated Lévy; alias with σ_T, R186_117); 𝔞_T = ½[s(D_per) + s(D_anti)] (two self-adjoint extensions, diagonal on the two mesh halves), ≅ ½(D_e + HᵀD_oH) with H the unitary half-shift, over codim 2 (PROVED, = R186_117 by parity); Akhiezer/Blaschke cones (Tate = double zeros) PROVED; discrete thm:Z CONDITIONAL (modulo the (−1)^k annihilator); circulant cone fails on every window. **Two-sector Schur reduction PROVED (R186_053 Thm 2.1–2.2, Cor. 2.3): free complement coercivity with explicit c_η; sufficient certificate S_η^low without inversion; certifies ½log3, log2, ½log5 with d = 7/29/59; NO-GO ∀T (d_η ≳ λ_A^{−1/p}, W-det in this basis).** Pointwise criterion in the dual variable: NO-GO PROVED (the sectors are convolutions, not multipliers). Retraction: "99% in the antiperiodic sector" was a basis artefact (audit 118). Finding to be audited: Fourier–Nyquist Galerkin gives upper bounds below the Legendre references (up to 20% at ½log5). No symbol changes; no contact with the sign; D OPEN.
42. ** (editor, audit R186_119):** numerical references for λ_A corrected: log2 = 9.83e-8, ½log3 = 9.448e-4, ½log5 = 3.10e-12 (upper bounds extrapolated with Legendre and Fourier on balls; the old values were Legendre M = 40 without convergence, up to 20% too high). Paper 47's certificates intact. No verdict changes; no contact with the sign; D OPEN.
43. ** (editor, record cleanup, RECORDS-CLEANUP):** corrections C-W1 and C-W2 APPLIED with a dated note (no silent rewrite) in R186_034 (Thm 2.1(iv), Thm 2.2, §0 item 3, §6: the sandwich was mixing extremals; correct λ_A/Pos(u₁) ≤ 1 − β_max ≤ λ_A/Pos(h*) ≤ λ_A/c_P), in R186_042 (Thm 2.3: β_j = (s₋/s₊)cot²φ_j, not tan²; sign of ½[(1−β)Q + (1+β)J]; Cor 2.4 was the correct form) and in the phase-186 README; checked against Paper 47's final main.tex `thm:wh-pencil`(iii) (eq:wh-sandwich) and `thm:wh-angles`/`cor:wh-nogap`: they agree. Log entries 32 and 39 of this record, and every citation of R186_034 Thm 2.2 or R186_042 Thm 2.3, are read with these corrections. No number changes (u₁ ≈ h*). Also: ROW-D-REDUCED-STATEMENT §1/§6 and CROSSWORD-TO-D §0–§1 (and §2–§5 line by line) rewritten in D-only form (label E1 → REF-D, D's internal restatement; no external equivalence), with an editor's note; historical plan memos (PLAN, INVENTORY-168-184, ROW-D-CLOSURE-PLAN, HANDOFF-149) with a note at the start. No grid symbol changes; no contact with the sign; D OPEN.

44. ** (audit, secondary items of Paper 47 §19, SECONDARY_ITEMS.md):** (1) annihilation of Γ moments at first contact: **PROVED to be equivalent to window positivity** (prop:annihilate-equiv: target ⟺ no first-contact vector ⟺ O_L F = 0 with O_L injective on the radical); the problem stays OPEN as the prescribed route to (L2), not as a weaker statement. (2) class-dependent value bounds: sharpened thm:R (constant K_β independent of M) and **cor:Rrate PROVED**: lattice ceilings exceed λ_P by at most O(1/log M), explicit, with the primal minimizer's tail coming only from the shape domain; the dual-side deficit D(T,d,U) remains OPEN (precise statement: one-sided approximation in L¹(|F̂*|²) by lattice polynomials with no low modes; polynomial rate ⟸ regularity of the minimizer beyond the shape domain). (3) polar capacity beyond ½log5: **existence PROVED** (cor:beyond5, continuity lem:contT through contact 5 + thm:log5W + thm:parityschur(c)); a certified window OPEN. (4) two-sided asymptotic law with sign: precise OPEN (the lower half is missing; by thm:wit-Tc(iv), λ_A ≥ −ε(T) already equals target; no lower bound better than the trivial one beyond ½log5); no new NO-GO. (5) **(H_f) PROVED** (prop:ftprim: direct primitive witness of f_t with primitive φ₀; thm:famFE unconditional; closes the MAJOR of R186_114 §2.2 without (Z-strip)); **(H_G) PROVED** (lem:sl-HG: pointwise kernel bound of G₀ with log(1/z) growth and L²-summable log₂⁺ ridges; thm:sl-L2 and cor:sl-split unconditional; closes gap (a) of R186_097). (7) optimal multipliers: **thm:mult PROVED**: λ_P = max_β V_T(β) with V_T concave coercive; converges to (2,0) ⟺ unique maximizer; λ_P = λ_W ⟺ 0 ∈ conv of the moments of W_T's minimizers; fails if λ_W < λ_A and the parity backgrounds differ; at ½log3, λ_W < λ_A (NUMERICAL, Galerkin upper bound). Paper 47: 133 pp, 0 errors, 0 undefined refs; backup main_pre_secondary.tex. No grid symbol changes; no contact with the sign; D OPEN. **Independent audit review (same day): all six items CONFIRMED (prop:annihilate-equiv, thm:R+cor:Rrate, cor:beyond5, prop:ftprim, lem:sl-HG, thm:mult); no label change; three local fixes (explicit |t| threshold in prop:ftprim, clarification of "first-contact vector," overflow box in eq:sl-HG1); 0 errors, 0 undefined refs, 0 overflow boxes; "Audit review" section in SECONDARY_ITEMS.md; DEFINITIVE_CHANGES aligned (sl-L2/famFE PROVED).**

45. ** (editor, phase 188 "closing D," tracks (L2) L2_BUILD_001–019 and (N) N_BUILD_001–015, audits N_011 and L2_018; synthesis `03-research/phase-188-closing-D/SYNTHESIS_188.md`):** pen and paper. **New positive structure PROVED:** Pos (window-shaped combs ≥ 0 ∀T) is convex and NOT empty: ρ_κ = 2κe^{u/2}du ∈ Pos ⟺ κ ≥ κ* = sup(−m)(¼+τ²) ≥ |C₀|/4 ≈ 1.343 (N_011 Thm 1, audit CONFIRMED; Cor 2 continuous Beurling systems, 4κ fix); ATOMIC comb in Pos ∀T (L2_018 Thm B, audit CONFIRMED); Λ's leading term is κ = 1 < κ* — the arithmetic fluctuation must supply the explicit deficit (κ*−1)/(¼+τ²). Segment λ_t = (1−t)ρ_κ + tΛ: t*(T) monotone, target ⟺ t_∞ = 1, (Ω_{t₀}) strictly weaker (N_012). Two-copy identity with the PNT term cancelled by Tate; Thm A (unbounded Ξ ⇒ t_∞ = 0); unconditional Thm L (limsup Ξ ≥ 0 ≥ liminf, Landau CITED) (N_014–015). Exact criticality of packet limits at every frequency γ (N_013; center = L2_010). (E_γ) exact with no ±4 slack; Dirichlet resolvent form (N_001–002). Map of Λ's entries (L2_011; new falsifier a_P). **New walls:** W-tail (N_003), Euler structure (N_005), monotone-cone resolvent (N_007), relative order (N_008 ⊂ W-lin), scalar transfer (L2_003), Euler cone (L2_013), Möbius–log certificate (L2_017), Frobenius duplication (L2_016), perturbative Φ (N_010), constant packets (N_013). New objects: algebra 𝔄_T (overlaps R162_903), Poisson–Euler map Φ (characterization = Hamburger, CONDITIONAL), Euler–Poisson cube. Frontier: (N)/(N_loc) by correlation in P_T with the exact vector; (Ω_{t₀}) over non-convergent spectral-measure families; (Ω_Φ) global; (Ω₀), Q3. No grid symbol changes; no contact with the sign for ζ; D OPEN.

46. ** (editor, phase 188 update 2: N_BUILD_016–020, L2_BUILD_020–024, audits 021/023; SYNTHESIS_188.md §1′ and §5):** pen and paper. PROVED: three-vector Gram identity with ℤ-additive center (N_016) — the center equals +4T‖F‖² (wrong sign, N_017); meta-theorem: computing translation multipliers = linear identities in 𝔄_T + Bochner/Cauchy–Schwarz (N_018); SOS with a free p.d. part = dual class (D), purely arithmetic SOS empty ∀T ≥ ½log3 (N_019, by hand); exterior certificates at Poisson-dual positions = thm:Z's prime part, far exterior support ⇒ negative value via W-tail (N_020); Lemma L + Theorem T (two-sided band |X(d)| ≤ 2a₀, necessary at every scale; audit CONFIRMED, novelty downgraded) and Theorem P (Poisson combs fail with prob. ≥ 1 − exp(−cT log T)) (L2_023); Theorem S: target ⟺ an explicit function B_{F₀} is positive-definite (L2_024; (⇐) modulo ARGUED Lemma I); Prop 4 (no comb ≥ 0 on log ℕ with residue r > 1 lies in Pos; CONDITIONAL on Q′; the "correlation-only" reading downgraded to HEURISTIC, audit 021). **New section "Primal and dual sides reduced to D in every known form"** (SYNTHESIS §5): packets, translations, the t_∞ segment, operator splits, interior SOS, every known exterior choice and the orders in 𝔄_T all reduce to D. No grid symbol changes; no contact with the sign for ζ; D OPEN.

47. ** (editor + independent audit, phase 188 → Paper 47; INTEGRATION_188.md, SYNTHESIS_188.md Update 3):** pen and paper. **N_020 Thm 2 → OPEN** (the dilated W-tail tests have window-moment pairings T ≈ 4 sinh T·‖G‖², not o(1); only the weak-duality reduction remains PROVED, rem:farext). **L2_021 Prop 4 → PROVED without Q′**, restated as thm:ceiling: a ≥ 0 positive ∀T ⇒ liminf S(x)/log x ≤ 1 (lower logarithmic density), directly from Theorem D (re-proved in the paper, lem:reson) by monotonicity of S; density/residue forms via partial summation and Hardy–Littlewood–Karamata (CITED). **Paper 47 (146 pp):** §sec:combs (pole-free form, smooth and atomic positive combs, integer density ceiling, resonator positivity, two-sided band, Poisson combs, thm:oneprofile, Arch−Div−Near matrices), §subsec:bar-arith (fifth barrier class), open problem (S) near-coincidence matrix. Audit review: everything CONFIRMED; one wording fix ("lower logarithmic density" in abstract/intro); 0 errors, 0 undefined refs, 0 overflow boxes. No grid symbol changes; no contact with the sign; D OPEN.

48. ** (independent audit, phase 189 NT_011–014 + NT_SYNTHESIS; NT_011_014_REVIEW.md):** pen and paper. NT_011 Prop 11.1 and NO-GO Thm 11.2 CONFIRMED (FE ✓, R > 0 on the line ✓, moments O(δ) ✓, Δℓ″ = 3/(2δ²) ✓) with class 𝓜 restated: ζ̃ has 4 poles off the line, so 𝓜 excludes holomorphy + order 1 (Hadamard = zero geometry). NT_012 Thm 12.1 CONFIRMED (width √(T₀log(1/T₀)), Titchmarsh 9.6(B)); Prop 12.2 → ARGUED. NT_013 Thm 13.2 (σ > 3/2, exact threshold) and Prop 13.3 CONFIRMED; Prop 13.5 (absolute NO-GO) → ARGUED. NT_014 direct PROVED; converse ARGUED with an extra σ-analyticity hypothesis; "⟺" → implication + ARGUED converse; NO-GO (b) → ARGUED. Synthesis §4 → HEURISTIC (the "Euler on the line" exception does not apply to (b)). **Target-E route (transport in σ via the odd-FE factor) EXCLUDED**: ζ′/ζ(w) converges only for σ > 3/2; crossing (1, 3/2] is (b); antisymmetry L2_026 §1, empty transport L2_026 §3, non-conjugation L2_027, cor:void. Remaining door: an inequality at σ = 1 that uses multiplicativity (false for ζ̃ and DH) and is not a zero-free-region argument; OPEN. No grid symbol changes; no contact with the sign; D OPEN.

49. ** (editor, audit L70 → Paper 47; AUDIT_LIU.md):** Liu, "Certified Weil Positivity Beyond the Unit Window" integrated as CITED: full form Q = W_T (half-width L = T, comb log n < 2T) ≥ 2^−151 for T ≤ 1 and ≥ 2^−49162 for T ≤ 17/16; λ_A(T) > 0 on (0,17/16] by monotonicity and λ^W ≤ λ^prim ≤ λ_A. The paper's own PROVED results at ½log5 (2.5·10^−12, 10^−18) remain intact; cor:beyond5 is still the unconditional internal statement. Paper 47: 146 pp, 0 errors, 0 undefined refs, 0 overflow boxes; backup main_pre_liu.tex. Residual 3A S5 §5#14 closed (read). No grid symbol changes; D OPEN.

50. ** (independent audit + editor, phase 190 SHAPE_THEOREM → Paper 47 §"The shape of a proof"; SHAPE_THEOREM_REVIEW.md):** pen and paper. Clause-by-clause review against the sources: **Theorem S overclaimed** (closed under "any of O1–O15"): O10 has no falsifier (OPEN), O11 and O14 are not instances of lem:transfer (background 0, not < 0; moved to the structural part), O4ε/O5 CONDITIONAL, O6 Beurling **CITED → ARGUED** (R167_103 row 7: no Beurling window form exists in the record), O8c ARGUED as a window falsifier, O9 Epstein CITED (complete)/ARGUED (primitive). Corrected constants: T₀(0) = 0.74921 (not 0.8047); κ_* ≥ ¼|C₀| = 1.343 (lower bound). Lemma I: rows 13/21 (M_m, f_t) keep the FE and break the Euler product over ℕ (corrected accounting; conclusion intact, modulo CITED Epstein and ARGUED Beurling). Cor. (e)10 no longer needs A3/A7–A9 of Paper 46 (Hodge-index form, not λ_A). **f_t decided: primitive witness PROVED** (prop:ftprim, confirmed by independent review); L2_BUILD_011 row 13 obsolete (erratum added). Paper 47: new §"The shape of a proof" (thm:shape in three levels; prop:shape-eulerdel and prop:shape-twist proved in the paper; prop:shape-crit(c) comb quadratic mean = 4T²; prop:shape-inputs) and **Problem (R) prob:region** (admissible region, ten properties) in §Open problems; bibitems Paper46, Titchmarsh1986; backup main_pre_shape.tex; **155 pp, 0 errors, 0 undefined refs, 0 overflow boxes.** No grid symbol changes; no contact with the sign; D OPEN.

51. ** (editor + own audit review, phases 191–192 → Paper 47 §"The shape of a proof"):** pen and paper. New subsection "Estimates and exact identities" (subsec:shape-est) and two clauses of the shape theorem. **(B′) no estimate:** lem:shape-est (i) pinch PROVED: if Λ satisfies (E_T,R_T) then μ_T − R_T ≤ λ_A ≤ μ_T + R_T, and for T ≥ 1 a decision by estimation has 0 ≤ μ_T − R_T ≤ 4·10⁹Te^{−15.449T}; (ii) PROVED: every exact reduction via lem:wh-schurabs (finite-dimensional E, λ_S < c_X) inherits the margin, λ_A ≤ λ_S ≤ (1+‖K‖)²λ_A (Lemma S of SPEC_A in finite form; the infinite-collar version remains ARGUED); (iii) CONDITIONAL (κ_T ≠ 0): slack > 𝔄_Tλ_A/|κ_T| ⇒ falsifier (1+δ)Λ; (iv) the reading "no estimate with remainder closes the step" ARGUED. The doubly exponential scale exp(−e^{(2−ε)T}) **only conditional on Zhu's conjectural law** (what is proved is e^{−15.449T}; not used). rem:shape-est: (E_γ) exact threshold PROVED, no-slack CONDITIONAL; pointwise form on the Nyquist mesh FALSE (σ_T(0) = C₀ − 𝔄_T < 0); T*₃ collapse by Λ∗1 = log PROVED. **(B″) no comb-generic identity:** lem:shape-ident PROVED (adding an identity valid for every weight vector does not break closure under O1–O6); prop:shape-ext (EI_001 Thm 1, E = p − q − r), prop:shape-family (collapse; spectral form EI_002 Thm 1; Mellin EI_002 Thm 2; second-order vanishing from both Tate conditions with cutoff y ≥ 1, EI_002 Thm 3), prop:shape-phase (EI_003 Thm 1, σ_T = 2Θ_T′, R_X = Θ′ + iZ_T′/Z_T), all PROVED, with no sign. rem:shape-ident: EI_003 Thm 2 ("symbol rigidity") recorded as a **tautology, not a barrier**; Fact N2 remains NUMERICAL (the M^{½}𝒲 polar term dominates at bounded height); self-duality on ℤ² mentioned, not used. cor:shape (e),(f); Problem (R) clause (11) (ζ-specific sign step by construction). Backup main_pre_shape2.tex; **159 pp, 0 errors, 0 undefined refs, 0 overflow boxes.** No grid symbol changes; no contact with the sign; D OPEN.

52. ** (phase 193 front J; CA_J_000–002, CA_J_SYNTHESIS):** correlation inequalities / stat mech (0 corpus hits previously). NO-GO PROVED: lattice RP per prime ⟺ ν on (π/log p)ℤ (chessboard dead; two primes ⇒ 𝖡 constant); 𝔸_M frustrated (+/· cycle) ⇒ GKS/GHS/FK dead; Euler tests = FKG-equality class ⇒ FKG blind. BL/PL: REF-D/retry. No contact with the sign.

53. ** (phase 193 front K; CA_K_000–002, CA_K_SYNTHESIS):** theory of frustrated quadratic forms (0 prior hits for Guerra/Parisi/diamagnetic/Harary; Doob = Paper 41, retry). NO-GO PROVED: diamagnetic in both images (integer image: bound |couplings| → −∞ at rate M; t image: Λ is the diamagnetic extreme, λ₀(T;a) ≥ λ₀(T;Λ) ∀|a|≤Λ, but on 𝒫_T the order reverses: λ_A(0.7;0) < 0 < λ_A(0.7;Λ)); Arch_M indefinite (C₀<0); ℤ/2 holonomy of the frustration = sgn 𝖡 (insufficient); Guerra-type interpolation: concavity ⇒ sign = a statement about the minimizer (REF-D), archimedean and Haar extremes indefinite; Cheeger with sign ≤ ½ vs. the required 1−O(1/M). New tool: **site independence** (D ⟺ positivity on prime tests; there Div ≡ 0 and D ⟺ Arch ≥ Near). No contact with the sign.

### Scope note — phase 208

Consolidated audit: `03-research/phase-208-node-scope-audit/README.md`.
No construction, no new route, no cell/status change: this does not call for
altering the JSON counts. Distinguish finite/complete node, even sector/full
row and pointwise/continuous ZCERT. The arithmetic identification of Λ is not
the sign step. Row D OPEN.

### Addendum, phase 209: subclass O1 control

See `03-research/phase-209-nonlocal-kernel/CONSTRUCTOR_001.md`, §§4–5:
NO-GO for compact J in H_A and explicit large domains; the no-go is NOT extended
to PW_T or Euler+FE. CONTROL_001 removes decorative non-locality by compression.
Recorded in the index without repainting cells, altering historical routes or
JSON counts: O1 remains OPEN, with no sign source or new link to the node.

### Phase209, second round — partial cross sign

ANTICORRELATION_003 / CONSTRUCTOR_004 (audits003/004): new record of a strict
auxiliary sign in punctured theta covariance; ordinary coprime Mellin at
α1/4 by cancellation G₀=0, including powers of two fixed primes. Not
identified with Q_T, nor is the global diagonal/tail proved. O1 remains OPEN;
no historical cell changes, nor are JSON counts/statuses altered.

### Phase209 — audited auxiliary completion and active goal D

CONSTRUCTOR005/AUDIT005 prove canonical SPD of −Rα, 0<α<1/2, on arithmetic
c_00; kernel inherited by finite deletions, so its sign is not identified
with Q_T. New identity recorded in the index; cell links do not change
status and historical JSON counts are intact. Explicit goal D
active (GOAL_D_STATUS.md); proof of link006 still OPEN.

### Fase209 — estructura funcional auditada (2026-10-19)

006/007: FE exactadeΠ y semigrupocontractivoV_n del auxiliar−Rα,
con defectos calculados y límites deespecificidad explícitos. No nueva
identidadQ ni cierre. Registroeníndice; sinrepintar celdas/conteosJSON.
GoalcompletoD active, continuacióndominio/inversión/enlace.

### Fase209 — control de inversión y límites (2026-10-19)

008/audit008 registran defecto explícito de inversión-adjunto y falla de
un argumento de límitefuerte primorial en el módulo nuevo. No cierre de
invariancia/clausurabilidad niQ. Sólo índice ampliado, sin cambio de celdas
ni conteosJSON; objetivoD íntegro active.

### Fase209 — prueba del enlace de flujo (2026-10-19)

009/audit009 excluyen interpolaciónC0 exacta de n^betaV_n, y compresión
unitariafijaV_n; sóloclase del módulo007, noO1global. El mapaQ aún ausente.
NotaP44alcance separada con contraejemplo a continuidad arbitraria.
Índice actualizado, sinrepintar celdas/conteosJSON; D íntegro active.


### Fase209 — LINK010: regularidad de una compresión de D_n (2026-10-19)

LINK_010_SPECTRAL_REGULARITY calcula, para cada observable finito centrado
no nulo A, incrementos con liminf ||D_mA−D_nA||²/log(m/n)^s>0,
s=2alpha, mediante n=1+kL,m=n+L fuera del soporte primo de A.
Toda realización D_n=P U(log n)J con mapas fijos acotados y U unitario C0
requiere momento espectral s INFINITO para JA: no Dom(|B|^(s/2)).
En alpha1/4, momento1/2 y potencia de dominio1/4. PROVED, revisión
independiente favorable en AUDIT_010. Sólo excluye compresiones con esa
regularidad; la compresión general permanece OPEN, igual que el enlace Q_T.
No se reabre la compresión normalizada009 ni se modifica el estado de D.


### Fase209 — LINK011: primer mapa continuo calculado y cotejado (2026-10-19)

LINK_011_MELLIN_GAUSS_MAP construye UF=Σ a_d(F)(X_d−1/d), con
 a_d=2∫ e^(x/2)F(x)W_d(e^(2x))dx en alpha1/4.
Convergencia enH por a_d=O_T(||F||/d), Sdd=O(d^-s); operador compacto,
featureC∞ y kernel efectivo suave. FEcoef paraFpar recupera exactamente
C(F)=∫Fcosh(x/2). No sumar el vector polar separado: diverge; cancelar
coeficientes primero. La igualdad Q_T=||UF||² en el portador continuo es
FALSA para ESTE mapa: tests polarcorregidos de alta frecuencia tienen
Q_T~logλ y||UF||→0. La dominación Q_T≥||UF||² sigue OPEN, igual que otros
mapas no suavizantes. No NO-GO generalO1, ni prueba deD. Revisión favorable en AUDIT_011.
Precisión006: no se exigen correspondenciasG/Π/v pieza a pieza; basta
identidad o dominación TOTAL sobre un core denso para norma de forma.


### Fase209 — LINK012: dominación011 refutada por test certificado (2026-10-19)

LINK_012_DOMINATION_FALSIFIER conserva exactamente el mapaU de011 y
prueba la desigualdad que había quedadoOPEN, sin reintentar la igualdad.
Test explícitoT=4/5, ω=5π/8, r=3(ω²+1/4)/(9ω²+1/4),
F=(cos3ωx+r cosωx)/sqrt(T(1+r²)), par, H0¹ y polar libre EXACTO.
CertificaciónArb128 y colasanalíticas: Q(F)<.002351, mientras el rango uno
positivo de005 da ||UF||²≥κ|Σa_dv_d|²>.26134304. Resto<−.25899.
Laplaceexacta de autocorrelación y expansiónK=2Σexp(−(2j+.5)u)
proporcionan comprobaciónindependiente sincuadraturagamma/peine:
Qupper<.001647953. Datos/códigoenLINK012_data. AproximaciónH1polarcorregida
extiende el falsificador a coreC_c∞. AUDIT_012 favorable, ambos scripts reproducidos.
Sólo escala EXACTA deU011: ninguna exclusión de reescalares pequeñas,
otros mapas/O1 niD. Esta dominación concreta ya no es un residuoOPEN.
No integraciónP47 ni cambio de celdas/conteos. ObjetivoD íntegro active.


### Fase209 — LINK013: toda escala fija deU011 falla para ventanas grandes (2026-10-19)

Diferencia nueva escrita respecto012: no cambiaU ni reintenta escala1;
calcula la respuesta del mismo mapa sobre la familia EXPLÍCITA de P47
lem:testfam aT→∞, y prueba la clase antesabierta de constantes arbitrarias.
El perfilM(F)=∫Fh cumple h(−∞)=−κ,h(+∞)=0, por sumaRiemann y Mellin
positiva de m=y^−1/2−τ. Para G_T=ω_k(x/T),k=ceil21T/e,F_T=P(D)G_T,
masaG_T/Tescapa compactos, derivadasL1 son o(T), y
M(F_T)/T→γ1²κ/8. AsíE_T≥κM²≥c0T². La prueba deP47thm:margin/cor:margin1
(CITED, inputsZ1/Z2 y fórmulaexplícita sólo para este falsificador) da
|Q_T(F_T)|/||F_T||²≤4e9Texp(−15.449T) paraESTAFAMILIA, no porinferir
un test de un ínfimo. NormF²O(T^1.5) => |Q|/E=O(√Texp(−15.449T))→0.
No existec>0 fijo conQ_T≥cE_Ten todasventanas. Cualquierc(T) eventual
requiere c(T)≤C√Texp(−15.449T); su existencia no se demuestra.
Pruebaanalítica sin nuevo cálculo numérico; AUDIT_013 favorable, inputCITED explícito.
No exclusión de otrosmapas, ni signoD nuevo. No integraciónP47/celdas/conteos.


### Fase209 — LINK014: quitar piezas positivas tampoco reparaU011 (2026-10-19)

Diferencia escrita:013 descartó una forma MAYOR porκvv*; no implicaba
falla de subformas. Aquíse prueba directamente cada pieza conMISMOa_d011.
ParaΠ, el perfil K_y(x)=2e^.5xΣWd(e2x)(qd(y)−1/d) es positivo,L1 y
∫K_y=C(y)=κΣvd(1/d−qd)>0. LocalCLTporFourier paraG_T ycotassupderivadas
=>B_FT(y)/√T→−γ1²g0 C(y)/4. Fatouen[1,2] daEΠ(F_T)≳T.
ParaG_s, G(d,2)=(1−1/√2)d^−.5 1_even; perfilh2boundedconlímites
−κ(1−1/√2)/2 y0. Riemannpares+masaescape danL2(F_T)≍T; Cauchycovarianza
=>E_G(F_T)≳T². κvv*ya daba≳T² en013. ConQ(F_T)CITEDdelpaper decreciendo
exponencialmente, TODA combinaciónfija nonegativanonula AκG+Bκvv*+CΠ
con MISMOa_d011 tiene |Q|/E→0. No constantepositivauniforme de dominación.
No inferencias de mayor a menor; nueva prueba para ambas subformas.
Sin numerics nuevos. AUDIT_014 y addendum favorables para toda la clase.
No se excluyen otros mapas, cancelacionesfirmadas ni factoresTdependientes.
ObjetivoD íntegro active/OPEN; no integraciónP47/celdas/conteos.


### Fase209 — CONSTRUCTOR015: dominio separado y cono PSD exacto (2026-10-19)

Diferencia nueva frente008: pequeños tilts positivos sobre muchos primosaltos,
no el primorial cuya normaGaussian divergía. ParaH=Σp^-s→∞,t=H^-2/3,
Z_u=∏(1+tp^-u), A=∏(1+tXp)/Z_s−Z_1/Z_s es Haarcentrado y satisface
Es|A−1|²→0, ||TA||≤C(Z_r−1)/Z_s→0,r=(s+1)/2>s, porΠdd de011.
Esto produce(√κ1,0)∈H. AccionesDnacotadas007 generan purosXd y dan
H=L²(P_s)⊕V,V=closureTA0. Tdensamente definido NOclausurable, con
sucesiónexplícita f2−(D2A_j−A_j/2)→0arith, imagen→q2−1/2≠0.
Las3formasκG,κvv*,Π son energías de3proyeccionesortogonales genuinas.
El conoPSD en su spanREAL sobreTODOA0 es exactamentea,b,c≥0.
Con014cierratambiéncombinacionesfirmadasPSDglobales deese span con
MISMOmapa011. No clasifica formas positivas sóloensuimagen niotrosmapas.
Psproducto devaluaciones, NOleyzetasobreN. NoV=todoGaussian niFEinvariancia.
Sin numerics nuevos ni inputnuevo de ceros. AUDIT_015 favorable a los tres teoremas.
No signoQ/D; objetivo íntegroactive, sin integraciónP47/celdas/conteos.


### Fase209 — LINK016: imagen par polar libre densa (2026-10-19)

Nueva diferencia frente015: ya no se suponePSDglobal; se calcula el
anulador de U_T011 sobre TODOS los tests pares polar libres. Enα1/4,
para cadaT>0, closureU_T(P_Tev)=H, tambiénparaelcoreC_c∞polarcorregido.
Prueba: ηd=<fd,h>=O(d^-1/4), c=Σηd/d converge; el perfilanalítico b_h
anuladorsatisface b_even=λcosh. Combμatómicaentera, a_n=Σd|nηd−c,a0=0;
μ'=μ−λδ0/2 es antiFourier porinyectividadGaussianenS'par (lemaentero
incluido). Fourierdecombenteraesperiódica=>μ'periodic=>constantcoeff;
Thetaμ'(1)=0 obliga0; divisorinductionηd0=>h0. No nuevo input de ceros.
Así cualquierformaHermítica Hcontinua PSDenU_T(core) esPSDglobal.
Con015+014cierratambiéncombinacionesfirmadascontinuas del span3piezas
positivas sóloenesa imagen, conMISMOmapa011. No finiteblockE_N, no formas
Hdiscontinuas, no otrosmapas/coefTdependientes ni signoQ. Auditoría favorable
independiente enAUDIT_016.md. D íntegroactive/OPEN.
