# R162_2300 — MASTER MAP of row D (8×8 grid, full corpus)

> **Registro cerrado.** Este documento conserva su estructura para consulta y no recibe más registros. Todo lo intentado, incluido el contenido de este documento, está consolidado en `05-meta-and-planning/ROUTES-MASTER-INDEX.md`, que es el único lugar donde se anotan intentos nuevos.

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
  → live residual: P152.1 Dolgopyat for the continued Mayer operator via Lewis–Zagier remains separate. The sign-carrier candidate was attempted in phase-193 CA_A_002_LEWIS_ZAGIER_MAYER.md / CA_A_002_REVIEW.md: historical NO-GO (ARGUED), without W-identification; no universal exclusion of the family.
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
  → actualización de catálogo: O-151.4 ya fue analizada en R168_202 §§1–2; no es un mecanismo nuevo con aquellas hipótesis. Las exclusiones son de las familias allí declaradas, no una prohibición universal por REF-D.
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
26. P152.1 Dolgopyat–Mayer via Lewis–Zagier → 1H: separate residue, preserved by phase-193 CA_A_002 §4. The sign-carrier candidate is already attempted (CA_A_002_LEWIS_ZAGIER_MAYER.md / CA_A_002_REVIEW.md), historical NO-GO (ARGUED), without W-identification; not a universal exclusion.
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


### Fase209 — VIRTUAL_SOURCE_017: ensayo explícito de métrica virtual (2026-10-19)

Por nueva orden del usuario se ensaya una fuente virtual calculable.
Diferencia frente008: se cambia la métrica gaussiana a y^(α−1)τ²dy;
no se afirma reparar el adjunto en el Hilbert original. S=τ conjuga G_n
a dilataciones unitarias y J_virtual a inversión exacta. El mapa unitario
C F=2^(−1/2)y^(−α/2)τ^−1F(log y/2) realiza traslaciones/reflexión.
La suma positiva de energías de saltos, más Lévy gamma, satisface en
el portador par polar libre Q_T=E_pos−(A_T−C0)||F||²,
A_T=Σ_{log n<2T}2Λ(n)/√n y C0<0. Contratermino negativo sin controlar.
La construcción funciona para cualquier perfil positivo, también borrado;
el signo virtual no selecciona los primos completos ni la FE del paper.
Diagnóstico: fuente no funcional para D; retorna a P1_BBSTAR/INV_N,
NO se presenta esa descomposición conocida como nueva ruta o avanceD.
Dominio de perfiles verificado para0<α<1. Sin numéricas ni modificaciónP47.
No NO-GO contra otras virtualizaciones; D sigue OPEN. Memo:
03-research/phase-209-nonlocal-kernel/VIRTUAL_SOURCE_017_METRIC_TEST.md.
Auditoría independiente favorable en AUDIT_017.md; identidades y alcance verificados.


### Fase209 — QRH: lectura focal y mapa condicional de exponentes (2026-10-19)

QRH_SOURCE_RELEVANCE.md y QRH_EXPONENT_MAP.md revisan las fuentes
solicitadas: Kintali47/48; OpenAI5Oct11/12; lectura estructural de
OpenAI30Sept7/8. CorregidaL74; no confundir versiones o formalizaciones.
Quanta reporta revisión humana y Lean para30Sept, no verificados aquí.
PROVED: si hay H^κ réplicas con errorO(DH^-δ) y energía total
O(D^(a+ε)H^b), H=D^h, la extracción da
θ=(1/2)max{a+(b−κ)h,2−2δh}. Sexticκ=δ=1/6,a=b=1,h=1+ϑ
recupera11/12+5ϑ/12. Esa cota no alcanza1/2 ni ampliando sóloelrango.
No se prueba imposibilidad de mejoras ni se interpolan tres fracciones.
OPEN: mejor familia/estimación selectiva y enlace exacto con déficit017.
La estimación crítica de réplicas escrita es un objetivo condicional,
NO un resultado del paper o nuestro. No signoD ni integraciónP47.


### Fase209 — QRH_REPLICA_COHERENCE: estimación selectiva examinada (2026-10-19)

Nuevo cálculo sobre las réplicas p^6 de la fuente QRH, tras consulta
del índice/grid/crucigrama. No se reabre una criba cerrada como pruebaD.
PROVED: Ap6=A1−Bp, Bp=−ν(p)Σ_(p∤m)μ(m)ν(m)W(Np Nm/D).
ParaNp≈Y=√D, conteoideal da |Bp|≪√D y varianza media≪D.
Identidad exacta Esel=|A1−barB|²+VarB. El control sin centrar
Esel≪D^(1+ε), para todoε, equivale a |A1|≪D^(.5+ε), para todoε,
con renombreε. No se probó control nuevo del componente coherente.
Revisión independiente favorable tras precisar estos cuantificadores.
ActualizadoQRH_EXPONENT_MAP: la condición suficiente propuesta era
también necesaria enesta familia; no se cuenta como mejora de cancelación.
No NO-GO general, no equivalenciaexternaD, no integraciónP47; D OPEN.
Memo:03-research/phase-209-nonlocal-kernel/QRH_REPLICA_COHERENCE.md.


### Fase209 — continuación de la media coherente QRH (2026-10-19)

Añadido ataque directo enQRH_REPLICA_COHERENCE.md, con revisión
independiente. Exactamente C_D=ΣμνW w_D, w_D=1−r_D/J∈[0,1].
ParaD>(8v)²,r_D≤2 sobreelsoporte; máscara cercana1 sinoscilaciónnueva.
Bp=−ν(p)A1(D/Np)+O_W(1), conWfijo y resto uniforme: mejorar
la escala corta reduceelerror pero no controlala señal larga.
Al expandir|C_D|², diagonal≪D porconteo; offdiagonal real aún sin
cota superior≪D1+ε. No se obtuvo estimación crítica deC_D, no se
relanzanVaughan/cribasgenéricas ni se declaraNO-GOgeneral.
Este diagnóstico no es un avancepositivoD ni prueba de cancelación.


### Fase209 — QRH7/8 y proyección hiperbólica (2026-10-19)

QRH_HYPERBOLIC_PROJECTION.md, revisión independiente favorable.
Diferencia frenteGreen/modeloshiperbólicosyaindexados: normaproyectada
exacta, frecuenciayposicióninflexión; no nueva fuente ni reapertura.
PROVED enL²par polarfreeb=.5: para0<a<bfijos yγfijo,
||P_bcosh((a+iγ)x)||²/||cosh((a+iγ)x)||²→
[(b−a)²+γ²]/[(b+a)²+γ²]. En a3/8,γ0: razón1/49,
normaresidual²~(2/147)e^(3T/4). La atenuación desaparece aaltas
frecuencias, tambiénparaT fijo. CotaexactaCauchysobremomentos.
Perfilrealcorregido tieneinflexión positivaenT−8log(128/63)+o1
para a3/8b.5, yotra simétrica. Coshmismaesconvexa globalmente.
SeptLemma20.2 certifica49/440640 enexponentecompensado, no margenD.
Franja7/8noidentificafluctuaciónconcosh3x/8 ni daamplitud/signo.
Sincontroldelcontratermino017, sinestimacióncríticanuevaniintegraciónP47.
Es cota geométrica/modelodiagnóstico, no avancepositivo de signoD.


### Fase209 — ensayo aritmético QRH4/5 (2026-10-19)

QRH_FOUR_FIFTHS_ATTEMPT.md, revisión independiente favorable con
alcancecondicionalexplícito. Usuario pideadaptar pruebaSept30, no sólo
modelo hiperbólico. Localmente, mismas identidadesEuler danH−1=O(Q^-87/50)
en caja x≥4/5,z≥33/200,w≥19/20; multiplicadorprincipal−1+O(Q^-4/5).
Noesextensióndetodaprueba. Cota baja publicada3/16 deja déficit3/40.
Alensayargeometría libre conservando majoraciones, aparece pérdida
(5ell−1+d)_+/4 en norma cuadrada completada; trasCS/sumatuplas,
σlow=11/12−ell/4+(5ell−1)_+/8, mínFORMAL13/15 enell1/5.
Así elcertificadoactual no llega4/5 variandosólo longitudes; necesita
almenos1/15 adicionalenexponentebajo (no suficienteparaalta).
No teorema13/15, no barrerauniversal, no cierreD. Candidatoescalar
ell1/5,b1/10,lx7/20,ly9/20,h17/20 pendientevalidaciónglobal.
No se usaX'≥1 comohipótesispublicada ni se confunde CII=s−11/16
con CI=s−2/3. Geometría/hightestsfueraoriginalsiguenOPEN.


### Fase209 — goalQRH4/5 y validación baja/alta (2026-10-19)

Usuariofija nuevoobjetivoexplícito: pruebaRe(s)>4/5; create_goalactive,
no conseguido porresultadosformales/intermedios, no equivaleacierreD.
QRH_LOW_CANDIDATE_VALIDATION: cota11/60paraell1/5,b1/10 bajo
lemmasexternosdeclaradosCITED; soportes,máscaras,perfilesuniformes revisados.
QRH_HIGH_CANDIDATE_AUDIT: mismosupplyslots pasa;certificadodelpiso
no cierra (49/1500 enextremo13/15). Jointformalinf167/192, no teorema
niNO-GOuniversal. Kappa dinámicofuera18.1requiereatención, pero
puedeensayarsekappa3/4coninputbeta*≤7/8; no declararbarrerainevitable.
GOAL_QRH_FOUR_FIFTHS_STATUS.md recogeobjetivo,estadoytrabajopendiente.
Revisiónindependiente de cálculos;ningunanueva regiónlibreprobada.

## Phase 211 (sign sandbox) — round 1
- P211-A near-coincidence mean value along smooth Dirichlet polynomials: PROVED decomposition Q_M = M·𝒜(w)+small; NO-GO for the sign (lattice-to-continuum transfer). Phase-190 residue answered: edge superpolynomially small.
- P211-B exterior form as fused object: half-line identity PROVED without zeros; defect for any comb PROVED; layer-edge residue void (NO-GO PROVED); clause (5) not met (ζ(½+iτ) with Möbius mollifier). NO-GO.
- P211-C exact two-sector reduction (L2′) PROVED, dimension 11 at ½log5±; no sign; coercivity of complement collapses at 2^b≈3^a modes. PIVOT.
- P211-C5 Carleman determinacy: NO-GO (REF-D), moments comb-free.
- Round 2–3: P211-2A coercivity floor (PROVED), floor-only Schur NO-GO (NUMERICAL); P211-2B Q₁ comb-monotone on prolate sector (NO-GO, ARGUED/asymptotic); P211-2DE Candidate I Θ_T = max_c λ_A(T;cΛ) (PROVED), not generic but separates only at tangency (PIVOT); P211-3B gcd Schur multiplier NO-GO (PROVED for the prescriptions; restatement in general); P211-3A parity commutation, Kato–Danskin criterion for c* = 1, Weyl pin, rigidity lemma (PROVED, no sign). State of (★): unchanged.
- **Phase 211, ROUND_005_B:** comb-Krylov family K_j from the archimedean negative cone — NO-GO (NUMERICAL) as capture device and as necessary condition (misses 1.1Λ, Λ+0.1·1₂); PROVED bookkeeping: degree-2 entries are v_m v_n window correlations at log(n/m), log(mn) with mn < e^{2T}; E_k Schur coupling decays ≈ one decade per k, complement coercive only past the near-null cluster (sizes 2…26 for T = log2…1.4).
- Round 5–6: P211-5A/5B comb-Krylov from Neg_T NO-GO at bounded j (scale-invariant subspace); P211-5E sharp band threshold λ_max(Π_T), Thm 3.1 Weyl count PROVED; P211-6A λ_max(Π_T)/A_T ∈ [¼,½] PROVED, arena exponent halves (still doubly exponential); P211-5C object E_T = Nyquist block ⊕ comb responses BUILT (exact reduction PROVED, captures minimiser, sign lemma cubic in v OPEN). State of (★): unchanged.
- Rounds 7–8: P211-7C certified falsifiers (PROVED, re-verified); P211-7D margin law −ln λ_A ≈ 4πe^{2T} (NUMERICAL), λ_W ≤ λ_A ≤ λ_{W,2} (PROVED); P211-7E/8D object E_T: exact Schur reduction reproduces λ_A, finite-degree Neumann needs degree ∝ log(1/λ_A) (NO-GO ARGUED); REVIEW_005 relabels recorded in the index. State of (★): unchanged.
- Phase 211, ROUND_008_C (P211-8C): variation of λ_A in T — virial bracket (Thm 1, Tate multipliers, Danskin over E_T) and exact edge-budget bracket (Prop 3) PROVED pieces; Grönwall in T = restatement (Prop 5), class 𝒦_H; measured −dlogλ_A/dT ≈ 0.83–0.96·8πe^{2T} (T = 0.7–1.2); remaining (EB_C) OPEN.
- Phase 211, ROUND_011_C (P211-11C): packet margin m − P^ρ_T of (1.2) — finite-range reduction PROVED (log τ* ≤ Σ₀ + κ + 2); NUMERICAL inf > 0 over the whole high range for T ≤ 2.5 (3 profiles) and T = 3 (cos², bump), min 0.341 at T = 2 (ind), minimiser at 1.1–1.6·2πN; direct packet W agrees to 2.4e-3; (HR)(a) pointwise form consistent, no packet coupling forced
- Rounds 9–17: P211-9A explicit upper bound λ_A ≤ 3.2·10²³N^{33/2}e^{−2πN} (PROVED given thm:ext-half + BJK); P211-9B exact ℱ-class selection rule (PROVED, C¹ data); P211-10A–16B high block: comb-blind, first chirp archimedean, (HR_g) floor OPEN; P211-17C first-cell coercivity certified (0.0696 T-free; 0.5276 at T=0.8); P211-15B/17A low block: no separate sign step, Λ only via the radical identity; Schur coupling = parity defect (Λ-free) + rung piece (sees Λ only via Λ∗1 = log); P211-16A band-restricted packet margin decreasing (0.888→0.114 for T 1→3); P211-17B: full ranges T = 2.5, 3 confirm 0.257, 0.114; partial T = 3.25/3.5/4 give ≤0.134/≤0.078/≤0.134 — not monotone, no zero crossing, direct W_T positive (NUMERICAL). State of (★): unchanged.
- Rounds 17–24: no negative packet up to T = 4.5 (band margin min 0.063, NUMERICAL); R-cell window in c and on the exponent ray ℕ^{1+t} shrink to {1}/{0} by the generic collapse (NO-GO as sign levers); ℕ positive vs every perturbed integer system in the R-cell form (NUMERICAL), sign tied to the embedding exponent; Selberg identity in operator form (PROVED); contact entry along N is a descent with jump −2v_nF*(T_n)² (PROVED/CONDITIONAL) — positivity cannot be propagated through N. State of (★): unchanged.
- Phase 211, ROUND_027_A (P211-27A): v_T(Λ) is not the global maximiser of the concave bottom μ_T(v): the bottom is simple, with gradient ≠ 0 (T = 0.8, 1.0, 1.2); M_T = 0.047, 0.030 ≫ λ_A. NO-GO (NUMERICAL).


### 2026-11-04 — Casos elementales de potencias

PROVED, con revisión independiente: `03-research/phase-211-sign-sandbox/POWER_CONE_001.md`, signo exterior en cada plano de dos potencias con exponentes >=32 (no envolvente, no PW_N). FALSIFIED: cosh positivo/logconvexidad implica signo de mezclas; H=3+cosh y vector (42,-41) dan -129/(34 log2). No es contraejemplo al dato aritmético. OPEN: P3, todos los órdenes y puente en norma de forma, en `PROPOSAL_POWER_CASES_2026_11_04.md`. Antecedentes Pick conocidos; novedad acotada al lema explícito. `NEAR_CASES_RESULTS_2026_11_04.md`: mejora auxiliar nearfree y contraejemplos a monotonía por contacto/ciclo automáticamente favorable; ningún NO-GO global.


### 2026-11-04 — Goal activo: potencias, ronda 002

`POWER_AUDIT_002.md` confirma normalización y polarización. `POWER_THREE_002.md`: PROVED/revisado caso de tres tasas en [u,3u], u>=2^30; extensión constructiva a n tasas con u>=2^{40n} y obstrucción cuantitativa a densidad (§§7–8 aprobados por revisión independiente). `POWER_BRIDGE_002.md`: puente en norma fraccionaria ponderada a PW_N; revisión independiente favorable §§1–5. La familia fija a=32+k es densa para transportar el signo si TODOS sus órdenes son positivos. Por ello el obstáculo del puente deja de ser el objetivo principal: resta signo a todos los órdenes de una misma familia densa. Umbrales crecientes con n no bastan por concentración. Objetivo siguiente: matrices K_ij=(L(32+i)+L(32+j))/(63+i+j), sin confundir casos finitos con cierre. No se modifica ningún paper.


### 2026-11-04 — Potencias, ronda 003 (revisada)

`POWER_STATE_003.md` resume registro vigente. PROVED/revisado: puente para PW_N y test compacto mediante Möbius finito, familia fija32+k suficiente; seis órdenes de `POWER_FIXED_GRID_003.md` certificados en Fraction con restos y reejecución independiente. `POWER_POLYNOMIAL_003.md`: identidades exactas Jacobi, sin signo uniforme. `POWER_SCHUR_003.md`: F=(z²−z+10)/10 tiene F creciente y F/z decreciente en[1,3], pero detK(1,2,3)=−13/270000; falsifica inducción desde pares/monotonías, no dato aritmético. La concavidad tampoco basta (falsificador por tramos§7). Próximo: caso confluente y auditoría de movimiento de tasas; monotonía sólo hipótesis a probar/refutar. P3 general y todos órdenes siguen OPEN. No hay cierre global ni edición de papers.


### 2026-11-04 — Potencias ronda 004: P3 completo PROVED

`POWER_STATE_004.md` es estado vigente. `POWER_POLE_MOVEMENT_004.md`+`POWER_CONFLUENT_004.md`, revisados en `POWER_AUDIT_004.md`: Q[Σ_{i=1}^3 c_iX^{-a_i}] >= ||Σc_iζ(a_i)e^{-(a_i−1/2)y}||²/20 para TODOS a_i>=32, sin separación/cota superior. Incluye P3 A>=32,h>0 y triples desiguales. Insight probado: cambio de polos repondera densidad por R(|τ|) creciente; covarianza positiva con m da monotonía de todas eigenenergías ARQUIMEDIANAS. Certificado confluente >.1 y pérdidas peine<.003, polar negativo<.042. Próximo: orden4 conservando polar positivo; no se traslada automáticamente movimiento a forma completa. Todos órdenes siguen OPEN; papers intactos.


### 2026-11-04 — Potencias rondas005–006, verificadas

Estado vigente `POWER_STATE_006.md`. PROVED/revisado: confluencia4 a32, W>norm²/5 aunque ARCH admite vector<−norm²/10 (`POWER_CONFLUENT_FOUR_005`). Derivada individual ARCH+POLAR>1/420 para todo numerador grado<4 en confluencia31.5, SOS racional (`POWER_POLAR_MOVEMENT_005`, auditoría005); sólo LOCAL. Test12 explícito: AP<−norm²/100; todos contactos positivos, n2solo repara; W>norm²/50. Borrar SOLO contacto2 conservando potencias4,8,... produce W<−norm²/125 (`POWER_ARITHMETIC_WITNESS_006`, auditoría006, cola restante<norm²/500). Son casos concretos nuevos, no novedad de necesidad aritmética general ni cierre. Todos órdenes y cuádruples arbitrarios siguen OPEN.


### 2026-11-04 — Potencias007: límite exacto del transporte arch+polar

`POWER_HIGH_ORDER_PM_NOGO_007.md`, revisado en `POWER_AUDIT_007.md`: para numerador1 con n=2^17 polos confluentesu=63/2, el Rayleigh AP disminuye al aumentar cualquiera de los polos (u∂_jE<−140/(31n)). Prueba escalar con0<=τm'(τ)<4 y polar exacto; ningún espectro enorme calculado. FALSIFIED sólo la monotonía numeratorfixed AP para todo orden en tasasaltas. NO es falsificador de λmin, ni del signo, ni del movimiento ARCH, ni del teorema local4. Por ello no extender ese mecanismo a todos órdenes; falta tratar cancelación conjunta con peine o una propiedad más débil que preserve signo.


### 2026-11-04 — Potencias007–008: bloque aritmético y patrón contrario

`POWER_STATE_008.md` es estado vigente. PROVED/revisado en `POWER_BLOCK_AUDIT_007`: W>norm²/10000 para TODO bloque Laguerre de dimensión 12 en tasa31.5, todos contactos/cruces (`POWER_ARITHMETIC_BLOCK_007`, verifier Fraction PASS independiente). ARCH+POLAR indefinida allí; contacto 2 repara matriz y cola norma<.0006. PROVED/revisado en `POWER_AUDIT_008`: f=(D²−.25)[y^(n−1)e^-31.5y], n=2^17, polar nulo, ARCH<−3.83norm², TODOS contactos primos <=1024 perjudican. No se afirma signo negativo de W: la cola está abierta. Refuta patrón universal de contactos bajos reparadores, no nuevo NO-GO global sobre peines finitos. Cuádruples arbitrarios, todos los órdenes y signo del Paper 47 OPEN; puente sí PROVED. Papers intactos.


### 2026-11-04 — Potencias009–012: hasta siete polos arbitrarios

`POWER_STATE_012.md` es estado vigente. PROVED/revisado: todos los espacios de4,5,6,7 polos reales>=31.5, incluidas multiplicidades, tienen W>c||f||² con c=2/25,1/100,1/25,1/500 respectivamente (`POWER_FOUR_GLOBAL_009`, `POWER_FIVE_GLOBAL_010`, `POWER_SIX_GLOBAL_011`, `POWER_SEVEN_GLOBAL_012` y auditorías). Verificadores Fraction PASS independientes. Nuevo paso: transporte exacto de margen por filtro, déficit espectral localizado y traza ponderada máxima en confluencia (`POWER_COMMON_TRANSFER_010`). NO se afirma monotonía AP ni del mayor eigenvalor ponderado. Puente a todo dominio sí probado, pero exige todos los órdenes, aún OPEN. `POWER_TATE_CHAIN_009` da segunda diferencia exacta de la suma completa; convexidad abierta, límite E0 ya conocido, familia individual no densa. Papers intactos.


### 2026-11-04 — Potencias013: límite de la cota puntual en orden ocho

`POWER_DEFICIT_LIMIT_013`, `POWER_DEFICIT_AUDIT_013`, verifier Fraction PASS: un vector racional da margen baseAP8<1/25, pero la pérdida uniforme puntual directa obligatoria supera1/20 (evaluaciónτ4, m4<−2/5), para cualquier c>=0. Incluye la mejor cota del producto completo, no sólo máximos separados. FALSIFIED la posibilidad de cerrar8 mediante ese criterio que descarta la ganancia positiva, aunque se optimicen constantes. NO se afirma AP/Wnegativa ni imposibilidad de otro transporte. Pivot autorizado: conservar integral firmada/estructura espectral, no repetir optimización puntual. Global7 sigue PROVED; todos los órdenes OPEN.


### 2026-11-04 — Potencias014: ocho polos arbitrarios y puente confluente

`POWER_STATE_014.md` vigente. PROVED/revisado: W>||f||²/1000 para TODOS los espacios de ocho polos reales>=31.5, multiplicidades permitidas (`POWER_SIGNED_TRANSFER_014`, `POWER_SIGNED_AUDIT_014`, verifier Fraction PASS reproducido). TEL descompone la corrección firmada en energías de nueve polos con numerador cero en0; su ARCH restringida confluente>1/4 permite superar013 sin cota puntual. `POWER_CONFLUENT_BRIDGE_014`, revisado independientemente: todos los bloques de una sola tasa bastan por densidad fuerte H1 ponderada; NO requiere margen uniforme en tamaño. `POWER_PRIME_TRANSFER_014`+auditoría: Wfv−R0Wfu=(1−R0)WG exacta con TODOS contactos/polar; falta probar signo de correcciones en todo orden. No extrapolar ocho/bloque12 a todos. Papers intactos.


### 2026-11-04 — Potencias015: mezcla completa y cola uniformemente positiva

`POWER_STATE_015.md` vigente. PROVED: `POWER_GEOMETRIC_TRANSFER_015` expresa transporte por mezcla positiva absolutamente convergente de W[Q^k f], incluidos polar y TODOS contactos; pesos de Rayleigh incorporan normas. PROVED: `POWER_HIGHPASS_015`, auditado en `POWER_HIGHPASS_AUDIT_015`, para cada u>1,N fijos, W>0 en TODO Q^k V_N para k suficientemente grande, uniformemente en numeradores. ARCH/norma² >=.5logk-C_N; peine completo y polar/norma² tienden a0. Diferencia nueva: se conserva energía firmada completa y se controla su cola mediante matrices Gram, evitando el déficit puntual013 y los patrones falsificados007–008. Queda segmento inicial sin signo ni extremo efectivo; no hay uniformidad en N ni cierre global. Ocho polos arbitrarios sigue PROVED. Papers intactos.


### 2026-11-04 — Potencias016: defecto exacto, interior binomial y límites del descenso

`POWER_STATE_016.md` vigente. `POWER_DESCENT_016`: PROVED Wf=WQf+WLf completo y diferencias finitas eventualmente positivas a orden fijo. Pesos binomiales exactos siguen p=tau²/(u²+tau²); borde cubierto015 pierde masa Y energía, interior conjunto permanece OPEN. `POWER_JOINT_SCALE_016`: PROVED Beta(k+.5,N−.5) para P1, contactos->cos(u sqrt(c)t) si k/N->c; media temporal (N−.5)/u independiente k y varianza explícita. FALSIFIED uniformizar desaparición de contactos en cono lineal y pesos exponenciales fijos en N en cualquier cono; NO falsifica conos de signo. `POWER_DESCENT_AUDIT_016`: momentos nulos impiden densidad fuerte de colas incluso hacia datos primitivos; k creciente sólo admite límite fuerte0 en peso común. W−4norm² conserva estructura+eventual pero inicial negativo (verificador Fraction PASS): NO-GO sólo inferencia estructural. Diferencia nueva respecto015: localizar masa y energía pendientes, no repetir cota de alta frecuencia. Global OPEN; ocho polos sigue PROVED; papers intactos.


### 2026-11-04 — Potencias017: puente escalar por coeficientes positivos

`POWER_SCALAR_BRIDGE_017.md`: prueba escrita, revisión conceptual independiente por mapa y signo; auditoría formal de ronda en curso. PROVED algebraicamente: signo de TODOS los átomos s^k/(s+u)^(N+k), N>=1,k>=0, basta para todos los bloques confluentes. Densidad racional = peso base por R(q)>=0 en[0,1]; R+epsilon admite expansión Bernstein EXACTA de grado elevado con coeficientes positivos. Identidad racional conserva polar al evaluar x=-1/4 y todo peine; epsilon->0 controla cruces sin inferir positividad de una envolvente desde una unión. Diferencia explícita: uso cónico de densidades, no densidad de colas refutada016. Lema clásico de elevación de grado no se presenta como nuevo. Tabla escalar completa OPEN; NO certifica ninguna ventana nueva T>log(5)/2. Construcciones adicionales017 en revisión; papers intactos.


### 2026-11-04 — Potencias017: fila infinita y cono cuadrático con peine completo

`POWER_STATE_017.md` vigente. PROVED/revisado: `POWER_INTERIOR_017` cubre N1, TODOS k>=0,u>=31.5 con W>4norma²/3 (verificador Fraction PASS); WRN ofrece cota efectiva de norma ponderada por cada N para todos k, no signo general. `POWER_QUADRATIC_017`: para cada c>0, P1 tiene W>0 para TODOS k>=cN²,N>=N0(c) explícitamente acotable. Nuevo método: desplazar DENSIDAD racional conjunta, no separar normas temporales; envolvente Ce^-t suma TODO peine y permite perfil gaussiano aritmético completo. Difiere del paquete E0 y evita obstáculo016; no se omite polar. `POWER_SCALAR_BRIDGE_017` revisado íntegramente por dos revisores: TODOS N,k escalares bastan para todas las matrices por identidad cónica Bernstein de densidades y polar racional. Tabla completa OPEN; no nueva ventana T certificada. Extensión numérica del cono en revisión aparte. Papers intactos.


### 2026-11-04 — Potencias017: cono numérico explícito desde dimensión dos

`POWER_QUADRATIC_EXPLICIT_017`: PROVED, prueba completa revisada independientemente por root y verificador Fraction PASS. A u31.5, P1, TODOS N>=2 y k>=10000N² satisfacen W>49norma²/50. Desplazar densidad a Imz15 da autocorrelación<5e^-15|t|; peine completo y polar <norma²/1000 cada uno, ARCH>99norma²/100. Diferencia respectoQUADRATIC017: elimina N0 desconocido/conservador mediante banda más ancha y normalización exacta. No afirma cono para todo numerador ni signo debajo de la parábola. Con la filaN1, resta en el blanco escalar suficiente N>=2,0<=k<10000N². No ventanaT nueva certificada. Revisión adicional APROBADA por mapa y signo (POWER_INTERIOR_AUDIT_017 §9 y POWER_QUADRATIC_EXPLICIT_AUDIT_017); papers intactos.


### 2026-11-04 — Potencias018: primeras dos diferencias y presupuesto del error

`POWER_STATE_018.md` vigente. `POWER_TABLE_DESCENT_018`: PROVED/revisado por root y mapa, verificador Fraction PASS, W>norma²/8 en filas N2,N3 para TODOS k>=0,u>=31.5. Recurrencia completa da primera y segunda diferencias estrictamente positivas de fila1, no completa monotonía. Conserva paridad polar y TODO peine mediante WRN. `POWER_LOW_TABLE_018`: presupuesto exacto D_N(theta)=2+2theta J_N(theta−.5), D_N(0)=2, crecimiento sqrtN en.5 y exponencial para theta>.5; endpoints y regímenes revisados. Sólo cuantifica pérdida conocida de cotas absolutas, no signo nuevo ni NO-GO global. Región suficiente restante N>=4,k<10000N²; no ventanaT nueva certificada. Papers intactos.


### 2026-11-05 — Auditoría018 y falsificador del descenso estructural

`POWER_TABLE_AUDIT_018` guardado y revisado por root. Aprueba filas23 y LOWbudget. Modelo explícito V=2norma²−u|F(iu)|²/100 conserva recurrencias/mezclas, márgenes de todos los espacios de hasta12 polos>=u, filas1/2/3 completas y cono k>=10000N², pero V tiene entrada negativa N40402,k40401. Prueba elemental mediante medida arcoseno menos átomo en1/2 y coeficientes binomiales. Diferencia respectoW4 de016: preserva también las regiones y márgenes positivos conocidos. NO es W ni conserva su dato aritmético ni perfil logarítmico exacto. NO-GO sólo inferencia estructural basada en esas propiedades; signo real OPEN. Próximo paso exige desigualdad aritmética firmada. Papers intactos.


### 2026-11-05 — Potencias019: transición firmada del peine y media de dilataciones

`POWER_STATE_019.md` vigente. `POWER_ARITHMETIC_DIFFERENCES_019` PROVED/revisado: autocorrelación k1 con raíz positiva única para TODO N y frontera O(sqrtN); TODOS los contactos ayudan para1<=N<=211,u>=31.5, peine completo>0. En k0 peine<0 paraTODON; no implica signo W. Verificador Fraction PASS reproducido por root y mapa. `POWER_SIGNED_MEAN_019`: B(x)=log(n!)−xHn+n<=−(1−log2)(x−1) da media firmada negativa de dilataciones; identidadEuler conocida, aplicaciónkernel específica. Inversoadjunto mu(m)mH(mx) exacto; prefijo3 negativo paraN>=2^17, SIN conclusión sobre inversocompleto. `POWER_SIGNED_AUDIT_019` aprueba ambos. CoberturaW no ampliada: filas1/2/3+cono017; global y nuevasventanasT OPEN. Papers intactos.


### 2026-11-05 — Potencias020: inverso completo exterior y déficit del primer contacto

`POWER_STATE_020.md` vigente. `POWER_INVERSE_KERNEL_020`: PROVED H_N/4<=h_N<=7H_N/4 para TODOS N>=2,logx>=(N−1)/30, con cola Möbius COMPLETA dominada mediante coeficientes positivos. N2 inverso positivo paraTODOx>=1. Parte negativa potencial localizada en intervalo explícito; emparejamiento interior OPEN. Diferencia respecto019: no prefijo sino suma completa. `POWER_SIGNED_BALANCE_020`: PROVED ARCH+POLAR+P2<−.66norma² en N211,k1,u31.5; contactos restantes positivos no omitidos y W no decidida. Refuta reparaciónporprimercontacto, no todopeinefinito. Ambos verificadores Fraction PASS root/mapa; POWER_BALANCE_AUDIT_020 aprueba. No nueva coberturaW ni ventanaT; papers intactos.


### 2026-11-05 — Potencias021: balance de un átomo y cola aritmética completa

`POWER_STATE_021.md` vigente. `POWER_CONTACT_BALANCE_021`: PROVED en N211,k1,u31.5, ARCH+POLAR+P2+P3+P4<−.21norma²; y0<sum_(q>300)Pq<5e−13norma². Verificador Fraction PASS root; cola analítica por unimodalidad/derivada logarítmica/recurrencia de integrales, sin enumeración extra. NUMÉRICO45/65dps: parcial hasta300≈−6.0812e−14, errorcuadratura no certificado; NO intervalo deW ni signo deducido de esa cifra. Nueva razón respecto020: magnitud de varios contactos y bound de cola completa en el mismo punto; no campañaN. CoberturaW y ventanasT sin cambios; global OPEN; papers intactos.

Auditoría independiente021 completada: `POWER_CONTACT_BALANCE_AUDIT_021` aprueba FAIL234/TAIL y conserva NUMÉRICO el diagnóstico parcial; sin signo de W deducido.


### 2026-11-05 — Potencias022: inverso Möbius completo negativo en un punto

`POWER_STATE_022.md` vigente. `POWER_INVERSE_INTERIOR_022` + `POWER_INVERSE_INTERIOR_AUDIT_022`: PROVED −2/3<h128(1)<−33/50; verificador Fraction reforzado PASS root/mapa. Segmento m<=64 y COLA COMPLETA<1e−10; diferencia respecto019prefix y020outer: falsificador del inverso completo en región interior. Por continuidad hB adverso cerca1; exterior positivo020 permanece. FALSIFIED sólo h_N>=0 global, NO W ni ERR. Pivot: primitiva exterior y condiciónmásdébil K=J+xh, aún en investigación. CoberturaW y ventanasT sin cambios; papers intactos.


### 2026-11-05 — Potencias023: criterio compensado y peso celular firmado

`POWER_STATE_023.md` vigente. `POWER_CUMULATIVE_INVERSE_022`: PROVED masa sumJ(n)=1, criterioCONDICIONAL K=J+xh>=0⇒ERR<=−2(.75−log2)(1−J1), y representación ERR=−2intK C_B con C_B>0, cota exterior(.75−log2)/2 y daño de borde<=delta²supK^-. No compensaciónW inferida. `POWER_CUMULATIVE_TEST_023`+auditoría: PROVED −1/250<K129(1)<−1/251, suma COMPLETA ycola<1e−10, FractionPASSroot/mapa. FALSIFIED K>=0universal, aunque K128(1)>0; no ERR/Wnegativeclaim. Razón nueva: condición compensada tolera hnegativo y se prueba separadamente del criterio022 ya refutado. CoberturaW/T sin cambios; papers intactos.


### 2026-11-05 — Potencias024–025: media aritmética completa favorable pese al kernel negativo

`POWER_STATE_025.md` vigente. `POWER_CELL_BALANCE_024`: presupuesto celular uniforme tolera K^-; no dominio favorable universal afirmado. `POWER_CELL_TEST_024`: PROVED S129(2)>.33 y primera celdaKC_B>.31, integrales polinómicas exactas y suma Möbius completa. `POWER_INVERSE_LOGCONCAVITY_025`: cocientes coeficientes D_N decrecientes⇒logD cóncava TODOS N. Chequeo racional D129'(2/3)<30D129(2/3)⇒K129>0 paraTODOx>=2⇒todas celdasrestantes positivas. Combinado: ERR129<−.66 COMPLETO, no prefijo. Verificadores Fraction PASS root/mapa, auditorías024/025 aprobadas. Diferencia nueva vs023: integración compensa K129(1)<0 y corte mejorado usa logconcavidad específica, no positividad puntual falsa. ARCH_sharp pendiente; NO nuevo W/T. Papers intactos.


### 2026-11-05 — Potencias026: corte uniforme y kernel conjunto firmado

`POWER_STATE_026.md` vigente. `POWER_UNIFORM_CUTOFF_026`: PROVED dos cortes analíticos t_J y t_R para TODOS N, de orden (N−1)/330 frente al anterior (N−1)/30; suma Möbius COMPLETA K positiva fuera del corte y celdas exteriores favorables. Rango uniforme TODOS2<=N<=129,x>=exp(2/3), por monotonía y extremos, no certificados por fila. Diferencia nueva vs025: Jensen de coeficientes y barreras Riccati eliminan chequeos por dimensión. `POWER_ARCH_CELL_026`: ARCH_sharp129<−.81; beneficio garantizado .66 insuficiente, SIN conclusión W<0. Identidad conjunta W/norma²=intK Omega conserva todas las cancelaciones, pero Omega(3/2)<−.1: FALSIFIED sólo positividad puntual del peso conjunto. Restricciones gamma reales aún disponibles. `POWER_ARCH_CELL_AUDIT_026` aprueba ambos; dos verificadores Fraction PASS root/mapa. CoberturaW/T sin cambios; interior y signo global OPEN; papers intactos.


### 2026-11-05 — Potencias027: contribución conjunta exterior y su magnitud

`POWER_DISCRETE_BALANCE_027`: prueba leída por root y verificador Fraction reproducido PASS; revisión independiente APROBADA en POWER_JOINT_AUDIT_027. Fórmula completa de Omega por pisos y bound Omega(t)>=ell−(4logt+9)/t, ell=1+gamma/2−log(4pi)/2>1/50; por tanto Omega>9/1000 para t>=4096 fuera de singularidades integrables. Con corte gamma026, TODA cola conjunta int_T^infinito K_N Omega es positiva para T>=max(4096,exp(tau_N)), con mayorante explícito. En el único N129: 0<cola4096<10^-36. Diferencia vs026: desigualdad para contribución real de W, no sólo ERR ni identidad; la cota de magnitud impide atribuirle compensación grande. Masas sumK(n)=3/2 y sumK(nx)=x^-32D(logx) registradas como identidades conocidas de inversión, no prueba de signo. Interior y W global OPEN; coberturaW/T sin cambios; papers intactos.


### 2026-11-05 — Potencias027: restricción gamma y dirección de Jensen

`POWER_STATE_027.md` vigente. `POWER_INTERIOR_CONSTRAINT_027`: mezcla de calor REAL ya conocida018, ahora peso positivo específico L_N(a)=E(V_N−a)_+−(EV_N−a)_+ para el resto respecto a gaussiana de igual segundo momento. Identidad completa Wgamma−G_W(EV)=int L_N G_W'' conserva todas las piezas. Masa L=VarV/2 sólo N>=3; N2 tratado sin varianza. ARCH_sharp estrictamente cóncava da cota SUPERIOR, refutando el sentido inferior propuesto. G_W''(a)<0 para TODOS a>=65536 refuta convexidad global del funcional real, NO W ni signo del resto específico. Diferencia explícita: ley inversa gamma fijada y peso de brecha, no mezcla arbitraria ni rebranding heat. `POWER_JOINT_AUDIT_027` aprueba ambos memos027, verificadores PASS root/mapa. Interior, coberturaW/T y signo global sin cierre; papers intactos.


### 2026-11-05 — Potencias028: cuarta fila completa de W positiva

`POWER_STATE_028.md` vigente, N5 aún pendiente. `POWER_ROW_FOUR_028`: PROVED W[f_(4,k)]>norma²/50 para TODOS k>=0, TODOS u>=63/2, con TODO el peine y polar. ARCH exacto y monotonías u/k dan>11/400; WR eta12 da peine<3/500; polar impar<1/1000, par favorable. Diferencia vs018: preservar margen de fórmula ARCH4 y cambiar peso de autocorrelación, no inferencia de recurrencias ni barrido. Tercera diferencia de fila1 estrictamente positiva como corolario, no completa monotonía. `POWER_ROWS_AUDIT_028` aprueba ROW4; verificador Fraction PASS root/mapa. Nueva coberturaW REAL: filas1..4; resto tabla N>=5,k<10000N² a u31.5. No nueva ventanaT certificada ni cierre global; papers intactos.


### 2026-11-05 — Potencias028: quinta fila completa y separación del borde polar

`POWER_STATE_028.md` actualizado. `POWER_ROW_SPLIT_028`: PROVED W[f_(5,k,u)]>norma²/25 para TODOS k>=0,u>=63/2; para k>=1 margen4/5. ARCH50(u0)<−.1 muestra por qué la condición ARCH0 positiva no basta. Nuevo argumento vs018/ROW4: k0 aprovecha polar positivo con extremos opuestos en u∈[u0,2u0], y ARCH positivo para u>=2u0; k>=1 usa covarianza desde1. Peine COMPLETO<.06, polar impar<.002, certificados racionales de extremos y monotonías analíticas. Identidad A_N1=A_N0+uA_N0' y criterio suficiente general registrados, sin extrapolar premisas. `POWER_ROWS_AUDIT_028` aprueba ambas filas, verificadores PASS root/mapa. Nueva coberturaW filas1..5; cuarta diferencia de fila1 positiva. Resto suficiente N>=6,k<10000N² a u31.5; no nueva ventanaT ni cierre global. Papers intactos.


### 2026-11-05 — Potencias029: límite del puente positivo con tasas crecientes

`POWER_SCALE_BRIDGE_LIMIT_029`: PROVED/revisión independiente mapa APROBADA. Toda densidad espectral normalizada del átomo N,k,u tiene altura<sqrtN/(u sqrtpi); el máximo decrece con k por comparación elemental de trigamma con integral midpoint, y el extremo k0 se acota por Cauchy–Schwarz gamma. Por tanto el cono de mezclas positivas con u>=C sqrtN tiene altura uniforme1/(C sqrtpi). En I=[−C/8,C/8] su masa<1/4, mientras un átomo p_(M,0,31.5) tiene masa>3/4 para M grande explícito; distanciaL1>1/2. Diferencia vs016: obstrucción del CONO de densidades con tasa variable, no pesos exponenciales a tasa fija. Impide sustituir automáticamente el puente017 por esa región; NO refuta W ni otros mecanismos. Papers intactos, signo global OPEN. Teoremas positivos de región029 aún en construcción/revisión.


### 2026-11-05 — Potencias029: positividad uniforme con escala cuadrática

`POWER_STATE_029.md` vigente. `POWER_ROW_PATTERN_029`: PROVED W>.7norma² para TODOS N>=2,k>=1,u²>=256N. `POWER_BOUNDARY_WEDGE_029`: PROVED W>.4norma² para TODOS N>=1,k>=0,u²>=4096N. Ambos con peine y polar COMPLETOS. Diferencia vs016/018: CS con pesos opuestos y comparación de coeficientes S_N cancelan el coste Neta/u; queda control por Neta²/u². ARCH por Euler+momentos beta en k>=1; cota de altura espectral y resolvente integrable cubren k0. `POWER_SCALE_AUDIT_029` aprueba tresmemos incluido límite del puente; dosverificadoresPASS root/mapa. No campañaN. NUEVA región real en tasas variables, SIN ampliación de tabla u31.5 ni ventanaT: filas1..5+cono017 siguen cobertura fija. Obstrucción del cono de densidades registrada arriba impide inferir puenteautomático. Papers intactos; global OPEN.


### 2026-11-05 — Potencias030: coste gamma–gaussiano contra la ley real

`POWER_GAMMA_BALANCE_030`: PROVED/AUDITADO, verificador Fraction PASS root/mapa. Para TODOS N>=2 a u31.5, 0<A_sharp(EV)−ARCH_sharp_gamma<=.5[psi(N−.5)−log(N−1.5)]<1/[2(N−1.5)]. Usa K_sharp<=1/t y momento EXACTO int L_N/a²=logEV−ElogV, finito tambiénN2; control constructivo O(1/N) de la pérdida real. Además en el único N2, Wgamma/norma²<.85 y G_W(EV)>.875 ⇒gapCOMPLETO contraL2<−1/40. Refuta comparar Wgamma>=Wgaussiana sin corrección, NO W negativo (filaN2positiva). Diferencia vs027: emparejamiento específico con ley real y presupuesto uniforme, no curvatura genérica ni mezcla arbitraria. `POWER_INTERIOR_AUDIT_030` aprueba; paralelo de bloque interior pendiente. No nueva coberturaW/T, compensación aritmética firmada aún OPEN; papers intactos.


### 2026-11-05 — Potencias030: compensación de un bloque real a tasa fija

`POWER_STATE_030.md` vigente. `POWER_INTERIOR_SCALE_030`: PROVED int_1^(9/4)G_N H>1/100 para TODOS N>=2^20 a u31.5 FIJO, incluyendo contacto2 adverso. Inversión adjunta de Omega cancela singularidades en enteros>1 y da H explícito con sumqLambda(q), conservando W completa. Diferencia vs026/027: bloque INTERIOR integrado real y errorgamma uniforme O(1/N), no otra cola ni signo supuesto del peso. Integralprincipal exacta>1/50, error<1/200. Primitivas H yx²H hasta5/2 negativas refutan sólo criterio de primitivas positivas; el bloque se rescata por comparación real. `POWER_INTERIOR_AUDIT_030` aprueba ambosmemos030; verificadoresPASS root/mapa. Resto desde9/4 aún OPEN; NO Wtotalpositivo ni nuevacobertura/T. Papers intactos.


### 2026-11-05 — Potencias031: prefijo adverso real, recuperación y costo global inicial

`POWER_STATE_031.md` vigente. `POWER_WEIGHTED_BLOCK_031`: PROVED a u31.5, prefijo hasta225/64<−.003 para TODOS N>=2^24; bloque hasta4>.015 para TODOS N>=2^22; recuperación entreextremos>.018 paraN>=2^24. Contactos2/3 íntegros, q4extremo cancela. I_*>=0 universal FALSIFIED, no Wnegativo; errorgammauniforme sin campañaN. `POWER_GAMMA_WEIGHT_031`: PROVED único máximoR antes2/3, q''<0, sobrepaso<=2M2/9 y TV<=1+4M2/9; W/norma²>=int_(T)^infinito I_*(e^t)(−R')dt−M2. Diferencia vs030: variaciónTOTAL real y costo adverso inicialO(1/N), no sólo bloquefinito/identidad. Promedioaritméticofirmadopendiente. `POWER_WEIGHTED_AUDIT_031` aprueba ambos; verificadorbloquesPASS root/mapa. No nueva coberturaW/T ni signo global; papers intactos.


### 2026-11-05 — Potencias032: decisión exacta del candidato211,1

`POWER_STATE_032.md` vigente. `POWER_ARCH_EXACT_032` + `POWER_CONTACT_DECISION_032`: PROVED 3.4e−15<W/norma²<4.5e−15 para ÚNICO N211,k1,u31.5 pendiente021. FórmulaARCH estable de sumandoscontrolados, EM8/corte32 conrestointegral absoluto y ancho<1e−18; todos primepowers<=512 exactos conHornerdivided yfactorq^-32, polarfracciónexacta; colacompleta positiva019 ymayorante<1.1e−15. Diferencia vs021: certificar error sincuadratura ydecidir MISMO candidato, no campañaN/cortes. Parcialnegativo300 se repara porcontactosomitidos, no por atribuirerrquad. `POWER_CONTACT_AUDIT_032` aprueba; certificadoprincipalPASS root/mapa. Nueva cobertura sóloeseátomo, no fila/vecindario/T ni cierre global. Papers intactos.


### 2026-11-05 — Potencias033: resto aritmético relativo y mezcla finita gamma

`POWER_STATE_033.md` vigente. `POWER_PRIME_BALANCE_033`: PROVED kernelreal k1 cumple w(mq)<=m^-2w(q) paraq>=5 enu>=31.5,3<=N<=2u²/9−u/3+1.5. Dcontraeρ2389/3600; identidaddivisores conb(n)corregidopor2,3,4 da paraKimpar0<S_K<=A_tail<=S_K/(1−ρ^(K+1)), yA_tail>=3600L/5989. Errorrelativoalpeine, noalresiduoW; comparaciónconARCHpolarOPEN. `POWER_COEFFICIENT_BALANCE_033`: mezclaErlangFINITA exacta conpesospositivos; −.01<E22<−.006 completo, perfilNOpositivo definido, NOcontraejemploW. Dañoindividual<.22/(N−1). Abel producepesospositivos paraT_m=ΣjE_j; TODOS T_m>=0 sería suficiente sólocolumnak0 yestáOPEN. Diferencias vs027/019: mezclafinita específica ycontracciónprobada paraaritméticareal, noidentidadescomosigno. `POWER_BALANCE_AUDIT_033` apruebaambos; verificadoresPASS root/mapa. Sin nuevacoberturaW/T; papers intactos.


### 2026-11-05 — Potencias034: nuevas filas completas y oscilación del criterioT

`POWER_STATE_034.md` vigente. `POWER_DIVISOR_COMPARISON_034`: PROVED W>norma²/40 para TODOS N>=3,k>=1,u>=31.5,u²>=225N/4; k>=2 margen3/20. k1 conserva peinepositivo019 yARCH−polar>0; higherk pagan peineCOMPLETO conCENTERED029, sin extrapolarsignoaritmético. A u31.5 cubreN<=17,k>=1; combinadoV12fijo007 completafilas1..12 TODOk. Combinado8polos014 completatambiénfilas1..8 TODOk/TODOu>=31.5. No arbitrarycrosses nuevosniTwindow. `POWER_WEIGHTED_COEFFICIENT_034`: PROVED T_m reales cambiansigno infinitasveces, porcoshREALpositivo/paridad/generador ylemadecontinuaciónde coefpositivos demostrado. FALSIFIED criterio033 T_m>=0todos e incluso eventual, NO Wnegativo ni no-go global. No reintentarpositividadporcomponentesTsincompensaciónnueva. `POWER_COMPARISON_AUDIT_034` aprueba ambos, verificadorregiónPASS root/mapa. Tabla fija pendiente k0N>=13 ycolumnasN>=18debajocono salvo211k1; papersintactos, globalOPEN.


### 2026-11-05 — Potencias035: filas1–17 completas y ley del promedio firmado

`POWER_STATE_035.md` vigente. `POWER_BOUNDARY_BALANCE_035`: PROVED W>norma²/40 para TODOS N1..17,k>=0 a u31.5 fijo. Un único terminal17,k0 tiene ARCH>−.868, polar>.911 y peine COMPLETO de módulo<.002; margen>.041. La recurrencia normalizada convexa y la columna k1 real034 completan por descenso los bordes13..16. Diferencia vs018: terminal y columna efectivamente certificados, no recurrencia aislada. `POWER_SIGNED_TRANSFORM_035`: ley positiva exacta P_d del promedio FIRMADO T_m/[m(m+1)/2], cola explícita, ventana m~sqrt(N), límite Gamma2 y costo de cualquier prefijo adverso fijo O(N^-2). No controla magnitudes ni signos en la ventana móvil; oscilación034 permanece. `POWER_BOUNDARY_AUDIT_035` aprueba ambos; verificadores PASS root/mapa. No nuevas combinaciones arbitrarias ni ventana T. Pendiente fijo desdeN18 debajo del cono salvo211,k1; signo global OPEN, papers intactos.


### 2026-11-05 — Potencias036: resto de frontera y localización de energías reales

`POWER_STATE_036.md` vigente. `POWER_RECURRENCE_BOUNDARY_036`: PROVED desde N>=18,k>=0,u31.5, energía COMPLETA del cono017 en frontera diagonal <=O(logL/sqrtL)->0; resto exacto R_L->A inicial. Momento inverso beta-binomial + upper ARCH y bounds017; novedad vs016: TODO cono parabólico creciente y energía real. Pesos de frontera detenida y masa superviviente positivos, sin inferencia de energía detenida. `POWER_MOVING_BALANCE_036`: PROVED energías polar y peine REAL COMPLETO bajo ley035 concentran m/(N−1)->1/32, mientras masa normativa tiene escala sqrtN. Inclinación beta-binomial exacta y cotas exponenciales; fase común(3969/3968)^N. CHEB elemental demostrado, sin truncar aritmética. FALSIFIED descartar colas de componentes separados usando sólo masa035; no localiza ventana del funcional firmado ni estima diferencia prime/polar. `POWER_FRONTIER_AUDIT_036` aprueba ambos; verifier constantes PASS root/mapa. Sin nuevo signo W/cobertura/T; filas1..17 de035 permanecen, globalOPEN, papers intactos. Continuación debe preservar cancelación conjunta y explicitar diferencia frente018/030/031.


### 2026-11-05 — Potencias037: dilatación crítica y agrupación finita firmada

`POWER_STATE_037.md` vigente. `POWER_ENERGY_GROUP_037`: PROVED perfil real D_N(m)=mH_N(mx_N)/H_N(x_N) tiene principal1/m y error explícito M_N(logm+log²m)/m, x_N=exp((N−1)/992). ABS-FAIL para TODOS N>=2^16 por conteo squarefree/Abel discreto, no tabla ni modelo artificial. Agrupación Möbius por Q finito conserva principal U_Q/m y error explícito con momentos divisor; condición WINDOW prueba signo de núcleo AUXILIAR, no W. Q creciente primorial hasta floor(N^(1/8)) da error<.01 para m<=exp(3N^(1/4)), N>=2^80, pero resto agrupado ABSOLUTO>1.48 frente grupo principal<.505. Refutada dominación absoluta para ESA elección, no agrupación firmada ulterior. Diferencia vs018/030/031: cotas uniformes sobre mismo perfil real, no nueva identidad sola; diferencia vs033: banda crítica1/m. `POWER_GROUP_AUDIT_037` aprueba todo, verifier ampliado PASS root/mapa. Error no sumable en infinito; complemento firmado e integración OPEN. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias038: producto firmado por Fourier y ventana ampliada

`POWER_STATE_038.md` vigente. `POWER_SIGNED_MOMENTS_038`: PROVED para N>=16,B_Q<=N/1000, TODOell real, |M_Q f_N(ell)−f_N(ell−A_Q)|<=12000B_Q/N+65sqrtN(V_Q/U_Q+1)e^-N/2000. Conserva multiplicador Möbius EXACTO, normaliza gamma con densidad positiva separada del perfil extendido firmado. Diferencia vs037: eliminaV/U del errorCENTRAL, no mero cálculo de cumulantes ni Jensen firmado. MismaQprimorial037,N>=2^80: (4/5)U/m<K_NQ(m)<(6/5)U/m en A_Q<=logm<=A_Q+sqrtN/100, longitud ampliada de ordenN^.25 a√N. Es núcleo auxiliar, noW ni ventanaT. `POWER_SIGNED_AUDIT_038` aprueba teorema/corolario, verifierconstantesPASS root/mapa, revisiónnormalizador adicionalcasos. Resto aritmético firmado infinito e integralOPEN; errorpolinómico no precisión suficiente por sísolo frenteenergíasexponenciales. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias039: inversos completos positivos desde un corte cercano a la energía

`POWER_STATE_039.md` vigente. `POWER_INFINITE_SHOULDER_039`: PROVED para TODOS N>=4e6,u31.5, h_N(x)>0 yK_N(x)>0 paraTODOx>=exp(T_N), T_N=2(N−1)v/(u²−v²),v=.5+1000/√N; T_N=(N−1)/992+O√N<(N−1)/330. Comparación con026 es del MISMO K; h se prueba también. Inclinación móvil, productoEuler INFINITO σ>1 firmado conservado enFourier, ψ<=2xelemental, normalizadoruniformec/v yperfiltrasladadopositivo. Cocientesfullh/H,K/G∈(.9Uσ,1.1Uσ) enintervalov; cola siguiente por m^-2. Diferencia vs038: noQfinito ni restocoprimoomitido, controla complemento completo enregióndeclarada. `POWER_SHOULDER_AUDIT_039` aprueba; root+dosrevisores, verifierPASS. T_N coordenadanúcleoNOventanaPaper47; interior/balanceWOPEN, sin nueva coberturaW/T, papers intactos.


### 2026-11-05 — Potencias040: patrón central real y corte a distancia constante

`POWER_STATE_040.md` vigente. `POWER_CRITICAL_BALANCE_040`: PROVED para TODOS N>=2^80,δ=N^-2,v=.5+δ,t_v=2(N−1)v/(u²−v²), fullh/H<−1/N yfullK/G>1/N enMISMOcentro. Además fullh,K positivos paraTODOlogx>=(N−1)/992+5. Diferencia vs039: factor elemental reciprocalEuler z−γz² conrest9|z|³ antesdeFourier, erroro1/N efectivo; no momentoscéntricosdivergentes ni seriesformales. NuevaCURV −2q′/t<q″<0 desdepesospolinomiales/Riccati da derivadas y margenreal. Colaδ2000/N..1000/√N enlaza039: distanciaO1 envezO√N, rangodeNexplícito. `POWER_CRITICAL_AUDIT_040` aprueba todo, verifierampliadoPASS root/mapa, curvaturaadversarialcasos. SignosnúcleosNOsignoW; interiorintegrado/ARCHbalanceOPEN. Sin nueva coberturaW/T, papers intactos, globalOPEN.


### 2026-11-05 — Potencias041: beneficio integrado en banda móvil con aritmética completa

`POWER_STATE_041.md` vigente. `POWER_ENERGY_BAND_041`: PROVED para TODOS N>=2^80, T=2(N−1)(.5+N^-2)/(u²−(.5+N^-2)^2), L=√N/100, 2∫_(e^T)^(e^(T+L))h_N B<−C_N/25600, C_N=e^(T/2)(rho/2−rho′)(T)>0. FULLMöbius+Brealsaltos, favoreceW=ARCHsharp−F pero complementoOPEN. Diferencia vs030031/040: bandaenergéticaMOVIL e integraciónfinita del factorδ−D antesabs, conbordes yerrorrelativoa MISMAescalaC controlados; noFubiniglobalcrítico. §7 prueba B=−γx−B1({x})logx+κ+E, −1/x<E<1/(2x), yboundintegrado periódico conQ2norm1/16,bordes/variación/∫|h|/x; auxiliarelementalnoWsign. `POWER_ENERGY_AUDIT_041` aprueba núcleo+append, verifierBANDPASS root/mapa. Sin nueva coberturaW/T; balancecomplemento/globalOPEN, papers intactos.


### 2026-11-05 — Potencias042: cola renormalizada absolutamente pequeña

`POWER_STATE_042.md` vigente. `POWER_RENORMALIZED_TAIL_042`: PROVED global F/2=−γ+(κ−γ/2)J1+R porMASS022 ySAWTOOTH041, con TODOSbordes/saltos. ParaN>=2^80,X=exp((N−1)/992+5), |Rtail|<=N(T+2)e^-3T/2<e^-N/1000; W=ARCHsharp+2γ−(2κ−γ)J1−2Rinside+epsilon, |epsilon|<2e^-N/1000. Diferencia vs041: errorABSOLUTO trascancelaciónGLOBALafín, no escalarelativaC_N ni suma de beneficios incompatibles. REALDECAYfullh/h′ porqT ydivisores, Q2borderXconservado. `POWER_RENORMALIZED_AUDIT_042` aprueba todo, verifierPASS root/mapa. Interiorrenormalizado yWsignOPEN; sin nuevacoberturaW/T, papers intactos.


### 2026-11-05 — Exploración043: interior renormalizado, sin nueva desigualdad

Revisión constructor/auditor de la continuación042: reunir (κ−γ/2)J(1)+R da exactamente ∫h(x)[B(x)+γ floor(x)]dx. Las medias celulares positivas de ese peso no controlan su emparejamiento con h firmado; invertir otra vez por divisores reconstruye H de INTERIOR_SCALE030. No se obtuvo un lower firmado nuevo ni se controla la variación interior mediante Q2. Etiqueta: exploración SIN AVANCE DE SIGNO, no NO-GO global ni teorema nuevo. No se creó un memo de identidades. Evitar repetir esta misma normalización como método nuevo sin una hipótesis o desigualdad adicional. STATE042 conserva el último resultado integrado. Se pasa a revisar mecanismos para la forma completa, con consulta previa del corpus.


### 2026-11-05 — Exploración043: dos pivotes descartados por antecedentes concretos

Sin nuevo resultado matemático. La lectura de BB5 como residuo abierto era histórica: CC_001_CROSS_LAG_LOG6_AND_KAPPA_HESSIAN.md (phase198, §§2,5,7; alcance enlíneas74/83) trata después Hessianκ, separación porlog6 yBochnercuatropuntos. La condición de simplicidad y la auditoría de CC4 se conservan; NO se deduce una prohibición de toda vía de dos primos. Se aclaró la remisión en la entrada BB001 para evitar repetir el intento.

El pivote theta tampoco produjo una desigualdad nueva: 103_34 ya prueba logconcavidad de la suma específica y menores cuadráticos; 103_39–42 delimitan argumentos genéricos de curvatura/hazard; 103_47 contiene las traslaciones aritméticas exactas, la cola relativa decreciente y un criterio cúbico condicional. No se promovieron esos antecedentes como novedad ni se concluyó imposibilidad global. STATE042 conserva el último resultado integrado. Nuevas exploraciones requieren otra hipótesis cuantitativa y un puente explícito a la forma completa.


### 2026-11-05 — Potencias044: chequeo de reflexión y candidato de representación

`POWER_STATE_044.md`: `POWER_REFLECTION_TEST_044` PROVED gapreal W[g_Q]−W[g_L]>3/2, u31.5, normas1; ARCH>2, polar>−.5, peineCOMPLETOgap>0. Refuta SÓLO eliminarsectorantisymétricoporreflexiónq↔1−q enpuente017; no toda subfamilia niW. Reutiliza004/018 explícitamente, sinnuevacobertura. `POWER_REDUCTION_AUDIT_044` aprueba/scriptPASS root/mapa. L55-B revisado: parpositivo explícito+slack/erroraritmético puede darlower; no se construyóparni nueva cota. No se afirma converso/equivalenciageneralniNO-GO deesa herramienta. STATE042 conservaúltimoavancedebalance; globalOPEN, papers intactos.


### 2026-11-05 — Potencias045: reparación compacta y corrección de frontera documental

`POWER_STATE_045.md`: `POWER_PRIMAL_PAIR_045` PROVED, revisión independiente en `POWER_PRIMAL_AUDIT_045`: si un par representante conserva exactamente la cola real del símbolo y sólo cambia una medida espectral PAR compacta, la identidad en TODOS los tests primitivos fuerza que la corrección sea cero. Prueba por F=(D²-1/4)phi, polarización/localización y momentos compactos; paridad esencial. En T=3/5, q_T(0)<-15/2, así ese ansatz no admite slack<=15/2. No es negatividad de W ni NO-GO de L55-B general. El subcaso no compacto con resto temporal exterior medida finita firmada retorna al dual(D) existente; no se generaliza a medidas/distribuciones arbitrarias. Diferencia respecto044: hipótesis concreta de reparación compacta, no mero cambio de orientación ni imposición artificial de masa total finita. `POWER_CONTACT_FLOOR_045` comprueba que el piso CRUDO m(240)-A2345<-1/2 falla al entrar5; ROUND026A ya evita esa limitación, por lo que no es nueva vía ni imposibilidad de otros certificados. Ambos verificadores racionales PASS constructor/root/auditor.

CORRECCIÓN DE ESTADO: Paper47 prueba hasta log5/2, pero el sandbox anterior `ROUND_026_A`, Theorem26A.2, registra PROVED/computer-assisted lambda_A(T)>=2e-26 para TODOS 0<T<=207/200=1.035. Root y auditor leyeron logs archivados de ambas paridades certified:true a mu2e-26; NO se reprodujo ahora la certificación larga. T1.098 sólo tiene builds/matriz localizados, sin certificado final hallado: no se promueve. La frontera local archivada, las cotas CITED y los resultados recientes de potencias son distintos. Ronda045 no añade cobertura W ni ventanaT; signo global OPEN y papers intactos.


### 2026-11-05 — Potencias046: exploración del interior deduplicada, sin nuevo signo

Constructor y revisor volvieron a `POWER_RENORMALIZED_TAIL_042` y al puente suficiente017. No se obtuvo una desigualdad nueva: Turán de los valores completos vuelve a la ruta de momentos/determinantes; recombinar J(1) con el residuo y efectuar la inversión completa reconstruye el peso043 o Hjoint030. Los emparejamientos con primo o Q fijo reproducen037/038. Elegir Q según la escala añade bordes de entrada y un resto firmado que siguen sin estimación. No se promovió un falsificador auxiliar del inverso de divisores de C(n), porque su positividad no era una hipótesis necesaria del intento. No hay NO-GO general ni nuevo artefacto teoremático.

Precisión de la obligación suficiente, ya consecuencia de016/036: para A_Nk=W[f_Nk]/norma² a u fijo, bastaría A_Nk>=-epsilon_N, epsilon_N->0, UNIFORMEMENTE en 0<=k<10000N² para N grande; el cono017 cubre el resto. Para cualquier epsilon, elija M con epsilon_N<=epsilon en N>=M y refine hasta profundidad L>=10000(M-1)²+M. Cada hijo con N'<M cae en el cono por su k' grande, y los demás tienen lower -epsilon. La recurrencia normalizada convexa fuerza A_parent>=-epsilon; epsilon->0 da signo. No requiere certificar excepciones finitas ni margen positivo puntual. Es una condición suficiente conocida, no una estimación aritmética ya obtenida. El resultado042 sólo aborda k0: un lower asintótico ahí no cubre toda la banda. La cota D_N>=2exp(-N/1000) es suficiente para decidir cada k0 puntual, pero no es un requisito necesario del cierre por lower uniforme evanescente.

Estado de cobertura sin cambios respecto045; signo global OPEN, papers intactos. La siguiente construcción necesita una entrada firmada adicional concreta, no otra inversión de los mismos pesos.


### 2026-11-05 — Potencias047: familia primitiva revisada, sin nuevo bound

Se comprobó el candidato H_Nk(s)=(s²-1/4)s^k/(s+u)^(N+k+2), N>=1,k>=0,u=63/2. Dos revisores y root contrastaron TATE_CHAIN009, PRIME_TRANSFER014, CONFLUENT_BRIDGE014 y SCALAR_BRIDGE017 con índice/grid/crucigrama. La adaptación Bernstein con base(s²-1/4)/(s+u)^3, más densidad014 y reparación de los dos momentos por dos racionales fijos, hace suficiente el signo de toda esta tabla para el portador PRIMITIVO. Es una adaptación del puente existente, no una desigualdad aritmética nueva; no se afirma una separación lógica estricta entre los objetivos globales primitivo/completo.

La densidad primitiva es exactamente la suma de las densidades originales (N,k+2), (N+1,k+1), (N+2,k) con coeficientes1,1/2,1/16. La identidad conserva toda W: los tres polares se cancelan por evaluación racional en x=-1/4. Hereda el cono017 para k>=10000(N+2)² y las filas N<=15 a partir de035. La recurrencia conserva pesos normalizados POSITIVOS, pero éstos son cocientes de las normas primitivas, no los coeficientes beta simples originales; su ley es una mezcla positiva de tres leyes beta. El criterio uniforme -o(1) de046 se adapta, sin aportar su hipótesis de signo.

En la otra expansión, con a=u²-1/4=992 y a_Nk=W[f_Nk] original sin normalizar, W[H_Nk]=a_Nk-2a a_(N+1,k)+a² a_(N+2,k). Es la segunda diferencia009 extendida a k variable. La anulación polar no controla el resto ARCH+peine y la mezcla positiva no fuerza un lower evanescente. No se obtuvo un bound nuevo, no se creó otro memo teoremático ni se presentó esta reducción como prueba del signo. La cobertura y la frontera documental permanecen como en045; global OPEN, papers intactos.


### 2026-11-05 — Potencias048: corolario subcuadrático y extremo restringido R12

`POWER_SUBQUADRATIC_COROLLARY_048` PROVED; auditoría independiente `POWER_SUBQUADRATIC_AUDIT_048` y revisión root. A u=63/2, para TODOS N>=exp(10^6) y TODOS k>=2N²/log log N, W[f_Nk]>(2/5)log N·norma². Extracción explícita de STRIP/PRIME/ARCH/POL017 con c_N=2/log log N: C(c_N)<=1+4sqrt(log N), ARCH crece como log N y domina TODO el peine y el polar. No se invoca uniformidad implícita de N0(c), ni límite gaussiano, ni truncamiento aritmético. Es cobertura no acotada adicional explicitada desde bounds existentes, no una nueva desigualdad aritmética. La banda inferior y el resto036 siguen abiertos; no hay nueva ventanaT.

`POWER_R12_ENDPOINT_048` PROVED y auditado en `POWER_R12_AUDIT_048`: para G en V13 confluyente con G(0)=0, E2[G]>norma²/50, donde E2=ARCH+POLAR+contacto2. Extiende una banda del certificado racional007 y verifica por congruencia/LDL12 el extremo v=u de la hipótesisR12 abierta014. Diferencia frente al falsificador universal014: aquí F0 pertenece EXACTAMENTE a V12; aquél no. Verificador PASS constructor/auditor/root. Se sigue un entorno común por continuidad, sin radio efectivo ni transporte para todosv. La cola de los demás primos no está incluida en E2; no se importa automáticamente el bound007 aV13. Para Q=s/(s+u), compresión tridiagonal de q enV12 da minEq>=1/576 y logconvexidad de normas: polar normalizado de Q^jF decae <=(9/62)^j PB12. El corte arquimediano efectivo y los bloques intermedios aún faltan; no se realizó un barrido.

Ambos resultados tienen alcance explícito. Signo global OPEN, papers intactos; frontera documental de ventanas conservada según045.


### 2026-11-05 — Potencias049: R12 uniforme resuelto en la base restringida

`POWER_STATE_049.md`: `POWER_R12_TRANSPORT_049` PROVED y auditado en `POWER_R12_AUDIT_049`. Para TODO F!=0 enV12 confluyente y TODO v>=u=63/2, E2[sF/(s+v)]>norma²/2500. AquíE2=ARCH+POLAR+contacto2. Por T2 de014 transporta coercividadE2 al mover UN polo desdeV12. Diferencia frente al falsificador universal014: se conserva exactamente la base positivaV12; no se declara una ordenación universal. R12, antesOPEN en014/048, queda resuelto en esa clase.

`POWER_CENTERED_CUTOFF_049`: centrar el polinomio del círculo y separar sectores de grados11/10 permite IBP+energía polinómica ponderada con prueba autónoma. Para TODOSj>=14 y TODOSnumeradoresV12, E[tau^-2]<1/405 y ARCH/norma²>859/800. Contacto2<norma² y polar048 decreciente pagan la cola. El corte32 inicial de HIGHPASS_CUTOFF049 queda dominado por14. Se certificó el segmento exhaustivo j1..13 mediante trece congruencias/LDL racionales12dim, error relativo aGram; el segmento fue fijado analíticamente, no por búsqueda de casos favorables. Script PASS constructor/auditor/root. Mezcla geométrica015 preserva norma y polar; |Q|<=1 y dominación de |m||F|² justifican la convergencia para cada v finito.

No se ha transportado la cola de contactos n>=3 desde007, por lo que no se afirmaWcompleto sobrelosnuevosespacios. Tampoco se autoriza iterar sobre bases intermedias distintasdeV12. Signo globalOPEN; no nueva ventanaT; papers intactos. Regiones completas048 y frontera documental045 permanecen.


### 2026-11-05 — Potencias050: W completo en todos los doce polos reales

`POWER_STATE_050.md`: `POWER_FULL_TWELVE_050` PROVED, auditoría independiente `POWER_FULL_TWELVE_AUDIT_050`, verificador completo PASS constructor/auditor/root. Para cualesquiera DOCE polos reales v_i>=63/2, repetidos permitidos, y TODO numerador real propio P, W[P/prod(s+v_i)]>norma²/10000. Incluye todos los cruces, todos los contactos aritméticos y el polar; amplía ocho polos arbitrarios014 y el bloque fijoV12 de007. Por cancelación de factores incluye los espacios de menor dimensión.

Ganancia nueva: W>norma²/250 en TODOS los TRECE polos reales>=u con numerador cero en0. Se reforzó el MISMO segmento exhaustivo j1..13 de049 a E2>norma²/50; la cola analíticaJ14 ya venceese margen. MULTI015 sobreG0=QF0 lleva todaesaórbita a13polosnum0. Trace010 conalpha1/2 da B_T13=109543953194<330975²; conservando n^(-1/4)<=10/13 desde3, la cola aritmética COMPLETA n>=3 tiene norma<2/125. ZERO13 resultante alimenta FULLTEL014, que conserva exactamente norma/polar y transmite sin pérdida la coercividad1/10000 del bloque base. La nueva entrada de signo es aritmética2 junto con ARCH+POLAR y cola infinita, no sólo ARCH.

La consecuenciaMULTI de049 también daE2positivo en todos12polos sin iterarR12; la exploración inicialFULL_TRANSFER_PLAN050(E23) quedó superada y no se ejecutó. No hay barrido de tasas/índices: segmento fijado por corteanalítico y13LDLs racionales12dim. No se afirma signo de13polos generales ni ordenarbitrario, ni nueva ventanaT. GlobalOPEN; papers intactos.


### 2026-11-05 — Potencias051: corte arquimediano lineal para todas las dimensiones

`POWER_DIMENSIONAL_CUTOFF_051` PROVED, versión corregida auditada en `POWER_DIMENSIONAL_AUDIT_051` y revisada por root. Para TODOS n>=1, TODOS F!=0 enV_n y TODOS j>=ceil(7n/6), E_(Q^jF)[tau^-2]<1/405 y ARCH[Q^jF]>(859/800)norma². Diferencia frente015/049: corte explícito LINEAL en dimensión, simultáneo en todos los numeradores, no eventualidad con constante desconocida. Con d=n-1 y r=u²E[tau^-2], (2j-1)r<=1+2sqrt[d(d+2j)r]. Se da J(n,b) explícito para r<b y cualquier margen arquimediano h>=0. Paridad y bordes se justifican por centrado y energía polinómica. Root corrigió el factor del segundo sector a(d-1)(d+2j+1), aún dominado por d(d+2j) con diferencia2j+1; los resultados finales no cambian y la auditoría reconoce la corrección.

No es nuevo signo deW. La extrapolación literal de050 con E2positiva en TODAS las órbitas y TODOS los órdenes ya la refuta PRIME_TRANSFER014: F_Tate de orden2^17 satisface E2[QF]<0. Esto exige cambiar el control aritmético de los segmentos iniciales, no descarta W completo. ZERO13positivo050 sólo deja un pivote deSchur para13polos generales; casos no halló nueva desigualdad del cruce. La reducción Toeplitz/persimétrica y el Schur son antecedentes, no se promueven como nuevo resultado. CoberturaW permanece en050; globalOPEN, papers intactos.


### 2026-11-05 — Potencias052: bloque confluyente13 completo y pivote real cuantificado

`POWER_STATE_052.md`: `POWER_CONFLUENT_THIRTEEN_052` PROVED y aprobado en `POWER_CONFLUENT_THIRTEEN_AUDIT_052`. Para TODO f∈V13 confluyente a u=63/2, W[f]>norma²/4000. Se conserva toda la aritmética: E2>.0003norma² ya positiva pero el majorante de cola desde3 es excesivo; E23>.00028norma² y TODAcola n>=4 tiene norma<.00001. LDL racional, constantes con restos y cotas por bandas; script PASS constructor/auditor/root. ÚNICO bloque siguiente motivado por ZERO13 de050, sin barrido de dimensiones/tasas.

Diferencia frente al Schur abstracto deduplicado051: se controló el acoplamiento REAL y el error de TODOS los cruces. Pivote respecto a h=ell/sqrt13,ell_j=(-1)^j: sigma(E2)∈(.0004054,.0004055), sigma(E23)∈(.0003834,.0003836), sigma(W)∈(.0003,.0005). Se encierran por orden de formas Tc±epsilonI y mínimo sobre el mismo espacio afín, no por errores independientes de una inversa. En el minimizador RACIONAL del centroE2, energías divididas por13: AP∈(.01839,.01841), contacto2∈(-.018,-.01798), contacto3<0. Son energías de una dirección de complemento fijo, NO cocientesRayleighunitarios ni afirmaciones de optimalidad exacta del vector central. Conservar3 mejora el certificado al evitar una pérdida de la cota absoluta;3 NO mejora el pivote real.

La investigación paralela de norma ponderada uniformeQ^jV_n no obtuvo boundnuevo: WRN017monomial no controlaGrammixta ytrace010 no se importa automáticamente aórbita. No se promueve un no-go general. Cobertura050 de12polosarbitrarios se mantiene; trecepolosarbitrarios yorden general siguenOPEN. No nueva ventanaT; papers intactos.


### 2026-11-05 — Potencias053: forma completa en trece polos arbitrarios

`POWER_STATE_053.md`, `POWER_FULL_THIRTEEN_053.md`: PROVED, verificador racional reproducido por constructor, mapa y root, exit0. Para TODO numerador real propio y trece polos reales >=63/2 (repeticiones permitidas), W>norma²/4000. Auxiliar ZERO14: catorce polos con numerador cero en s=0 tienen W>norma²/1000.

Diferencia respecto050/052: se retienen exactamente contactos2,3; momento matricial centrado y monotonía cubren TODOS j>=96, y los95 bloques iniciales se certifican exhaustivamente con error epsilonGram. MULTI14 transporta E23; traza14 acota TODA cola desde4 por<1/1000; FULLTEL13 conserva el margen de052. La optimización intervalar del logaritmo no cambió precisión ni umbrales. No nuevo T, no dimensión arbitraria, no cierre global. No reintentar como si positividad eventual resolviera el segmento inicial para toda dimensión.


### 2026-11-05 — Potencias054: control efectivo de coeficientes en frecuencia inversa

`POWER_INVERSE_COEFFICIENT_054.md`: COEFF/EVAL PROVED, revisados independientemente por root y mapa. Con a=u sqrt(j), R(y)=y^(n−1)P(ia/y), D=integral |R(y)|²(1+y²/j)^−(n+j)dy, se tiene norma²=a^(1−2n)D/(2pi). Para TODO n>=1, j>=n y TODO numerador, (suma|coef R|)²<=9n²9^n D; por tanto el mismo factor controla evaluación compleja y producto R(z)R(-z), con max(1,|z|^(2n−2)). Prueba elemental: peso>=exp(-2) en[-1,1], expansión Legendre, recurrencia de coeficientes y Cauchy.

Diferencia frente015/016: constante efectiva dependiente sólo de n para TODOS j>=n, evitando el menor eigenvalor no cuantificado de una Gram límite; no supone norma temporal ponderada uniforme en n. Las coordenadas por sí solas no son el resultado. Contorno completo, corte efectivo para W y segmento inicial siguen pendientes; no nueva cobertura de signo ni T. No se promueven como nuevas las reformulaciones de energía negativa036 ni la extrapolación de momentos que reproduce016.


**Actualización054 — corte completo aprobado.** `POWER_EFFECTIVE_HIGHPASS_054.md` y `POWER_EFFECTIVE_HIGHPASS_AUDIT_054.md`, PROVED/revisado por root y mapa: con C_n=9n²9^n, D_n=10C_n n!, A_n=6C_n n n! y K(n)=max(10000n²,A_n·3^(4D_n+20)), W[Q^j P/(s+u)^n]>norma² para TODO n>=1, TODO numerador real de grado<n y TODO j>=K(n), u=63/2. Contorno completo<=D_n, momentos beta explícitos incluidas ramas r=0 y r=n, extremo escalarN=1 justificado aparte; autocorrelación<=D_n exp(-15|t|)norma², peine infinito<D_n, ARCH>2D_n+9 y polar<1. No campaña ni evaluación de enteros gigantes. Resuelve el contorno/corte que la entrada054 anterior dejaba pendiente. Diferencia frente015: fórmula efectiva en dimensión variable, sin Gram límite no cuantificada. Segmentos iniciales j<K(n), signo global y nueva ventanaT siguen sin resolver; no eliminar el resto usando recurrencia036.


### 2026-11-05 — Potencias059: escala necesaria para contorno uniforme

`POWER_STRIP_NECESSITY_059.md`, PROVED por prueba analítica root/mapa: para u>0 y0<eta<u fijos, no existe D independiente de n,j que acote integral|rho_(n,j)(x+i eta)| porD integralrho sobre una sucesión n<=j=o(n²), ya conP=1. Var|tau|<=u²[j/(2(n−3/2)(n−1))+1/(2(n−3/2))]→0; elegir t_n en[T,T+2pi/u] con fase media múltiplo2pi hace la correlación→1, incompatible conD exp(-eta t_n) paraTgrande. Excluye estrategiasSTRIPuniforme enconos j>=C n^p,p<2.

Diferencia frente016: toda escala subcuadrática, incluida frecuencia central divergente, con control exacto de varianza. No Wnegativa, no prohibición de signo subcuadrático, no cota necesaria p>=3.017escalarcuadrático y054conD_npermanecenválidos. Constructor investiga producto de amplitudes sin fase causal para p>=2; comparación gaussiana global no justificada. GlobalOPEN; sin nuevoT ni campaña; papers intactos.


### 2026-11-05 — Potencias060: contorno uniforme y signo en cono n³ log³n

`POWER_STATE_060.md`, `POWER_UNIFORM_STRIP_060.md` y `POWER_UNIFORM_STRIP_AUDIT_060.md`: PROVED/APROBADO por constructor, root y mapa. Para TODO n>=1, TODO numerador real P de grado<n y TODO j>=10^12(n ceil(log_2(n+1)))^3, u=63/2, W[Q^jP/(s+u)^n]>norma². STRIP a altura3 tiene constante<2 INDEPENDIENTE de n/P; autocorrelación<=2exp(-3|t|)norma², peine completo<2, ARCH>4, polar<1 en la misma normalización.

Diferencia frente015/054: polinomios ortogonales del peso Student exacto dan FIRST200 para amplitud sin fase; los grados crecen como(n+3r,j−r). Cauchy enL² a altura15 paga sólo colaTaylor desde20nq_n conD_n054, mientras las primeras derivadas cuestan<.01porpaso. No se exponentia un generador de dimensión fija, ni se usa gaussiana global ni norma causal ponderada uniforme refutada016. SINGLE-EVAL controla amplitudes complejas; rho=H H# conserva el producto correcto fuera de la recta. CorteO(n³log³n), también válido el más débil10^12n^6; sin campaña numérica.

Índices iniciales j<J(n) y signo global OPEN. No se infiere descenso desde el cono ni una nueva ventanaT.059 no refuta este rango: sólo exige al menos escala cuadrática paraSTRIPuniforme. Papers intactos.


### 2026-11-05 — Potencias061: decisión completa del caso interior129,0

`POWER_GAMMA_129_DECISION_061.md`, `POWER_GAMMA_129_AUDIT_061.md`, `POWER_STATE_061.md`: PROVED/APROBADO, verificador racional reproducido por constructor/root/mapa, exit0/PASS. ParaG(s)=(s+63/2)^−129, W/norma²∈[13456684165,13456684168]/10^20, enparticularentre1.34e−10y1.35e−10. Caso histórico pendiente025/026/027, no búsqueda de otroN. ARCHestable032,polar racional, TODOScontactoshasta512 ycola completaADVERSA<1e−24 porROOT026q(log512)>16; sin cuadratura ni floatcomo prueba.

ARCHsharp/norma²≈−1.04219397018062543, ERR≈−1.04219397031519227, ambos encerrados racionalmente. El beneficio−ERR supera el déficit sólo1.3456684e−10; la garantía−.66 de025no era suficiente. ConCELL024, restodeceldasn>=3aportaentre.3755y.3822 a−ERR, sin dobleconteo. Se decideWdelmismotest dondeK129(1)<0, no se rehabilitaKpuntual>=0. No se infiere fila, siguienteN, ventanaT ni signo global. Papers intactos.


### 2026-11-05 — Potencias062: déficit afín y residuo completo en el mismo129

`POWER_GAMMA_AFFINE_BALANCE_062.md`, `POWER_GAMMA_AFFINE_AUDIT_062.md`: diagnóstico PROVED/APROBADO, verificadorreproducido constructor/root/mapaexit0PASS. Reusa024J129(1)completo y061ERR/ARCHsharp sinotroN/precisión/corte. AFF=ARCHsharp+2γ−(log(2π)−1−γ)J1∈[−60446492280,−60446492279]/10^12; Rcompleto∈[−30223246208,−30223246207]/10^12; W/norma²=AFF−2R. La parteafínesnegativa y la reparaciónR esesencialenESTEbalance.

RincluyeB1periódico+errorEuler, no B1solo; no usaABS-TAIL042(N>=2^80). ElenclosureRusaERR061conocido, NOesboundindependienteparadescenso;Wmantienecert061sinredondeosindependientescompartidos. No nuevoW/TniNO-GOgeneral. ComparacióndediferenciasNdeJ/K/ARCHsiguesinbound; globalOPEN,papersintactos.


### 2026-11-05 — Potencias064: escala cúbica necesaria para STRIP en todos los numeradores

**PROVED/APROBADO.** `POWER_STATE_064.md`, `POWER_STRIP_CUBIC_NECESSITY_064.md` y `POWER_STRIP_CUBIC_AUDIT_064.md`: prueba analítica revisada por constructor, root y mapa, incluida la mejora al umbral lineal j≥10^6n. Para u=63/2 y0<η<u, TODOS n≥4,j≥10^6n admiten un numerador REAL P de grado<n con ∫|ρ(x+iη)|/∫ρ≥1+η²n³/(1152u²j). En consecuencia se refuta STRIP con D independiente de n,j,P sobre TODOS los tests j≥C n^p para cualquier p<3. Elegir j=max(ceil(Cn^p),ceil(10^6n)) conserva j=o(n³) y hace divergir el lower.

Diferencia frente059: numerador variable, tomado del polinomio ortonormal Student de grado n−1; no P=1 ni extrapolación de un paquete lineal. Recurrencia β exacta con k/8≤β_k≤4k, proyección del generador060 al grado n+2 y resto racional controlado dan ||H′||²/||H||²≥n³/(2304u²j). La paridad construye P real par y ρ=H²; convexidad par de la norma desplazada produce el lower. No necesita transferencia gaussiana ni campaña numérica.

Alcance sólo estrategia de contorno ABSOLUTO: no W negativa ni obstáculo a otros mecanismos de signo.060 sigue válido en n³log³n; potencia3 necesaria para STRIP, factores logarítmicos no decididos. Interior/signo global y nueva ventanaT siguen abiertos; papers intactos.


### 2026-11-05 — Potencias065: exactamente k raíces simples y signo de la cola completa

**PROVED/APROBADO.** `POWER_STATE_065.md`, `POWER_CONTACT_OSCILLATION_065.md` y `POWER_CONTACT_OSCILLATION_AUDIT_065.md`: prueba analítica revisada por root y mapa. Para TODOS u>0,N>=1,k>=1, la autocorrelación de s^k/(s+u)^(N+k) tiene exactamente k ceros positivos simples, signos alternados desde positivo y última raíz en x=ut estrictamente menor que4k(N+k−1). Para u>1/2, TODA la cola de contactos u logq>=4k(N+k−1) tiene contribución de signo(−1)^(k+1): favorable para k impar, adversa para k par; convergencia absoluta y signo estricto de su suma.

Diferencia frente019: conteo exacto para TODO k, no otra evaluación k=1. Momentos nulos hasta2k−1 más grado resuelven N=1; filtros exponenciales unilaterales y Rolle con borde en infinito preservan ceros simples y propagan en N. La cota019 más fina para k=1 no se reemplaza. No se asume positividad total genérica ni se borra ningún primo. No se controla la magnitud frente al prefijo/ARCH/polar: sin nueva fila W, ventanaT ni signo global. Papers intactos.


### 2026-11-05 — Potencias067: el descarte positivo Selberg falla en el caso129 ya certificado

**PROVED/APROBADO.** `POWER_SELBERG_DROP_OBSTRUCTION_067.md`, `POWER_SELBERG_DROP_AUDIT_067.md` y `POWER_STATE_067.md`: revisión independiente mapa y root, sin nuevos cálculos ni otroN. Para el MISMO gamma129,u=63/2 de061, Selberg da S=U−V y W/norma²=ARCH/norma²+polar/norma²−2U+2V. El par2·2 y la mezcla real030/Jensen prueban2V>1/243. Como061 certificó0<W/norma²<1.35·10^(−10), el criterio que descarta2V tiene valor<−1/250. Incluso retener sólo1−theta de2V exige theta<6561/(2·10^11); theta=10^(−7) ya deja ese candidato negativo.

Diferencia explícita frente055/023: no se vuelve a ofrecer la identidad Selberg ni V>=0 como avance.055 dejó abierta la falsedad del criterio fuerte W/norma²>=2V; el certificado completo posterior061 ahora lo refuta en un test ya existente. Es una obstrucción a esa pérdida positiva aislada, no a Selberg completo, métodos compensados ni signo de W. No nueva fila, ventanaT o conclusión global. Nota retrospectiva incorporada a STATE055; papers intactos.


### 2026-11-05 — Potencias073: convexidad global del hazard theta y positividad de TODOS los pares

**PROVED/APROBADO.** `POWER_STATE_073.md`, `POWER_THETA_HAZARD_COMPACT_073.md`, `POWER_THETA_TWO_COPY_073.md` y `POWER_THETA_AUDIT_073.md`. Cerrado el compacto que phase103/103_43 dejaba abierto: un certificado racional de4096paneles prefijados verifica la cuarta derivada de logPhi negativa en[0,1/4], con TODOS los sumandos theta mediante cola explícita. Paridad y el outer10343 dan V'''(t)>0 para TODOt>0, V=−logPhi. Constructor, root y mapa reprodujeron exit0/PASS; no campaña ni edición histórica.

Nueva consecuencia positiva: dos copias independientes del tilt exp(ux)Phi(x) prueban M''(u)<0 y M(u)−uM'(u)>0 para TODOu>0, M(u)=L(u+1/2). La varianza condicional del semidiferencial decrece con el módulo del semipromedio; una covarianza de monotonías opuestas da el signo estricto. Así1<L(a)/L(b)<(a−1/2)/(b−1/2) para a>b>1. El criterio exacto CONE001 prueba positividad de la forma COMPLETA en TODO plano de dos potencias con a,b>1, incluyendo todos los contactos. Para a≠b la matriz es definida positiva; para a=b es semidefinida por redundancia y la función representada no nula tiene energía positiva.

Diferencia explícita: se resuelve el residuo compacto10343 y se demuestra una aplicación de dos copias que no dependía de las cinco comparaciones de tilt polinómico allí pendientes. Supera el antiguo umbral a,b>=32 de CONE001§5 en el caso de PARES; éste queda como antecedente válido, no como frontera actual. No se infiere positividad de tres generadores, todos los órdenes, su envolvente lineal ni una nueva ventanaT. Signo global OPEN; papers intactos.


### 2026-11-05 — Potencias074: la hipótesis fuerte073 no basta para tres generadores

**PROVED/APROBADO.** `POWER_STATE_074.md`, `POWER_TWO_COPY_SCOPE_074.md` y `POWER_TWO_COPY_SCOPE_AUDIT_074.md`; verificador racional exit0/PASS reproducido por constructor, root y auditor. Un potencial par POLINÓMICO V=A[x²/2+x^(2p)/(2p·2^(2p−2))], p=10^6,A=4·10^8, conserva TODAS las hipótesis073, incluso convexidad fuerte. Todos los pares positivos son definidos positivos y M''<0, pero en nodos A,2A,3A el vector(40,−40,3) da c^T Kc<−53111/(10000A). Modos controlados analíticamente y error modo-media<=1/sqrtA por integración por partes; sin cuadratura ni barrido. El jet en0 de V=x^6 se comprobó positivo mediante momentos gamma, sin ofrecerlo como falsificador.

Diferencia frente003: el contraejemplo pertenece exactamente a la clase fuerte probabilística073, no sólo a funciones cóncavas o medidas pares genéricas. Refuta ÚNICAMENTE su promoción automática a orden3; NO Phi real ni W. Los TODOS PARES reales073 permanecen probados, sin nueva cobertura W/T. STATE074 registra como obligación OPEN, no como bound obtenido: con r=uM'/M,t=−u²M''/M, el jet3 exige t<=(1−r)(1+2r); falta magnitud de la covarianza y comparación global. Signo global OPEN; papers intactos.


### 2026-11-05 — Potencias075: densidad positiva del denominador Schur regularizado

**PROVED/APROBADO.** `POWER_THETA_SCHUR_DENSITY_075.md`, `POWER_THETA_SCHUR_DENSITY_AUDIT_075.md` y `POWER_STATE_075.md`. Para la Phi REAL de073, Z(z)=∫Phi(x)e^(zx)dx, u>0,c=M(u),a=M'(0), el denominador D_u=zcZ−uZ' admite la representación positiva explícita H_u(z)=D_u(z)/[z(z²−u²)]=∫Phi_u(x)e^(zx)dx. Aquí h_u=−cPhi'−uxPhi, k_u(x)=∫_x∞h_u(y)dy y Phi_u(x)=u^−1∫_|x|∞sinh(u(y−|x|))k_u(y)dy>0. h_u y k_u tienen cada uno UN cruce negativo/positivo en la semirrecta; la cancelación exacta∫cosh(uy)k_u(y)dy=0 y un cociente creciente prueban el signo antes de tomar valores absolutos. La ecuación Phi_u''−u²Phi_u=k_u, sin delta en0, da la transformada entera y sus valores removibles.

Diferencia frente003/074: se construye una medida positiva para el denominador regularizado que quedaba pendiente, no sólo valores positivos reales del cociente Schur. H_u>0 y(logH_u)''>0 en la recta. Se conserva exactamente F1=−cz/u+c²Z/(uzH_u), con residuo R=uc²/(ua−c)>0 en0. No se identifica F1 con una derivada logarítmica ni se obtiene G=F1−R/z positivo: falta comparar Phi con Phi_u. Sin positividad de tres generadores, todos los órdenes o nueva ventanaT. Sin cómputos ni campañas; papers intactos y signo global OPEN.


### 2026-11-05 — Potencias077: signo real uniforme del resto Schur regularizado

**PROVED/APROBADO.** `POWER_STATE_077.md`, `POWER_THETA_REMAINDER_077.md`, `POWER_THETA_RATIO_COMPACT_077.md`, `POWER_THETA_RATIO_OUTER_077.md` y `POWER_THETA_REMAINDER_AUDIT_077.md`. Para la MISMA Phi real de073/075, TODOu>0, c=M(u),a=M'(0),beta=u²a/(ua−c), la diferencia F_u=J−betaPhi_u tiene exactamente UN cero positivo SIMPLE, con signo negativo/positivo y masa cero. Se obtiene T_u(z)>0 y G_u(z)>0 para TODOSu,z>0, con T=Z−[Z0/H0+z²/c]H y G=c²T/(uzH). Es signo REAL puntual del resto, no positividad de su kernel.

Diferencia frente075/076: se verifican desigualdades locales ESPECÍFICAS C>0 y N=(xq−p)C'−xrC>0, donde p=V',q=V'',r=V''' y C=p³+xp²q−pq−xpr+xq². Así L=(xq−p)/C decrece hacia0; con el borde wPhi->0, un promedio de cola prueba R creciente hacia infinito. El forzante tiene patrón+−+ y dos momentos nulos; interpolación convexa da F(0)<0, la representación anticausal da cola positiva y Rolle con multiplicidades fuerza el único cruce. No se supone que una transformada positiva sea una derivada logarítmica.

Evidencia: exterior x>=1 analítico, numeradores racionales con TODOS los coeficientes positivos en un cuadrante y cola theta completa hasta orden4; root leyó y reprodujo el verificadorFraction, tresPASS. Compacto origen1024/resto8192 paneles FIJOS, jets completos hasta8 y modelosTaylor2 con restos, código auditado línea por línea; constructor1589 terminóexit0/PASS. SHA256 `896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee`. Reproducción independiente root36038 **terminada exit0/FULL PASS**, origen y8192 paneles restantes; hash coincidente con el constructor. Los anterioresFAIL de evaluación intervalar directa fueron dependencia insuficiente; se conservaron mallas/dominios y se justificó el nuevo encierroTaylor, sin cambiar la hipótesis.

El auxiliar074 no refuta estas nuevas condiciones específicas. G>0 no prueba [G(z_i)+G(z_j)]/(z_i+z_j) PSD, ni tres generadores, todos los órdenes, una ventana temporal nueva o signo globalW. Los términos cruzados del kernel del resto siguen OPEN. Papers intactos.


Corolario auxiliar auditado077: N=M/u, B=(a/N−1)/u² cumpleB>0,B′<0,2B+uB′>0; el valor removible G_u(u)=−aB′/[B(2B+uB′)]>0 da el signo deB′. ParaF=uB, |uF′/F|<1 prueba todos sus pares. El complemento deSchur del nodo0 satisface K_M(u,v)−N(u)N(v)/a=[uN(u)vN(v)/a]K_F(u,v), así la matriz anclada{0,u,v} esPD para u,v>0 distintos. Nodo0 corresponde al exponente original1/2, FUERA de los datosW admisiblesa>1; no es positividad de tres generadores admisibles ni del kernelG.


### 2026-11-05 — Potencias078: colas analíticas de dos curvaturas auxiliares

**PROVED/APROBADO en sus rangos declarados.** Apéndice078 de `POWER_STATE_077.md`, auditado en `POWER_THETA_CURVATURE_AUDIT_078.md`. Para x=u², b(x)=B(sqrt x), g(x)=xb(x)=a0u/M(u)−1 y h(x)=1/b(x), se prueba g″<0 para TODOu>=63/2 y h″<0 para TODOu>=128. Series reales completas y cotas elementales poligamma/Dirichlet, sin nuevas matrices, puntosW o mallas. Para g se obtiene el margenDelta>423/10000; para h, el ancla realL8>3/10 da a0>1/25 y luego a0u/M>3 en toda la cola desde128. Identidades de derivadas y constantes racionales verificadas independientemente.

Una condición SUFICIENTE adicional para todos los pares del kernelG_p es la doble concavidad GLOBAL de g,h: las fórmulas exactas de C_P′ y(xC_P)′ son errores de tangentes de h y g. Su descarga global sigueCONDITIONAL: quedan los compactos iniciales de g/h y no se presume preservación al iterar. g″<=0 es el jet ya registrado074, no una condición sin antecedente. La coordenada positiva K del apéndice da b=Z_K/Z_J, pero073 para cada ley por separado no ordena ese cociente.

Diferencia nueva: descarga analítica de las COLAS de estas obligaciones específicas, no una nueva regiónW. Los trece polos de tasas>=31.5 ya están cubiertos053; no se presenta un caso de tres exponentes grandes como avance de cobertura. Sin nuevoT ni signo global; continuación compacta activa, papers intactos.


### Ronda079 — Comparación exacta de secantes para tres generadores (PROVED condicional)

Fuentes phase211: `POWER_THREE_SECANTS_079.md` y `POWER_THREE_SECANTS_AUDIT_079.md`. Bajo BASE073, los bloques de tres nodos del kernel completo son PSD **si y sólo si** g(x)=a sqrt(x)/M(sqrt(x))−1 es cóncava en su intervalo de cuadrados. DET/CONC/GAP comparan exactamente dos cotas de la diferencia de secantes; delta<0 da determinante negativo. No necesita077 ni concavidad de h=1/b, ni concavidad hasta0. La nueva obligación para ai>1 queda reducida a UNA curvatura real en 1/2<u<63/2; la cola g''<0 de078 ya está probada. La región de triples ui>=63/2 ya estaba cubierta por053: ninguna nueva cobertura W o T, ningún resultado de todos los órdenes.003/074 siguen vigentes fuera de la hipótesis nueva. Auditoría root/mapa/insight aprobada; compacto activo.


### Ronda081 — BASE073 no se hereda literalmente por el resto REAL (PROVED, clase acotada)

Fuentes phase211: `POWER_SCHUR_BASE_OBSTRUCTION_081.md`, `POWER_SCHUR_BASE_AUDIT_081.md`. Para el resto exacto G_p de la Phi REAL, G_p'(1024)<0 para todo pivote p>=p0=[25(2g*+24a²·1024²/M(1024)²+2)]². Se prueban mediante cotas reales completas a>1/25, M(1024)<3 y M'(1024)>1/[3(1024+1/2)]. Por positividad global077, tampoco puede conservar concavidad global para esos pivotes. Es un fallo de la clase recursiva que exige BASE073 en cada resto, distinto del falsificador genérico074. NO refuta G_p>0, su kernel, W ni una recursión con hipótesis más amplias; no nueva cobertura ni obstrucción global. Auditoría mapa aprobada; continuación082 separada.


### Ronda082 — Criterio recíproco exacto de tres nodos (PROVED algebraico)

Fuentes phase211: `POWER_RECIPROCAL_SECANTS_082.md`, `POWER_RECIPROCAL_SECANTS_AUDIT_082.md`. Para F>0 con todos los pares del kernel K_F estrictamente PD, todos sus triples son PSD si y sólo si R(x)=sqrt(x)/F(sqrt x) y S(x)=sqrt(x)F(sqrt x) son cóncavas. DET3=Vandermonde²·R[x1,x2,x3]S[x1,x2,x3]/(R1R2R3); RECIPROCAL y pares estrictos excluyen ambos defectos negativos. Permite F decreciente y no exige BASE073, a diferencia de la herencia refutada081. Recupera079 para M real. Aplicación a G_p, pares y ambas curvaturas/preservación siguen OPEN; no nuevo W/T ni orden superior. Auditoría root/insight/mapa aprobada.


### Ronda080 — W completa para TRES potencias arbitrarias ai>1 (PROVED)

Fuentes phase211: `POWER_STATE_080.md`, `POWER_THETA_G_COMPACT_080.md`, `POWER_THETA_G_COMPACT_AUDIT_080.md`, `tools/power_theta_g_compact_080_verify.py`. BASE073+criterio079+cola078+certificado080 dan g''<0 para todo u>=1/2, y por tanto kernel completo PD para tres nodos distintos ui=ai−1/2>1/2. Repetidos se agrupan; positividad de la función representada no nula. ARCH/polar/TODOScontactos conservados por congruenciaCONE001. Certificado continuo4096panelesdyádicos fijos, arb256bits/cap20, Taylorgrado16 con resto Cauchy racional<1e−12; constructor43260 exit0/FULL PASS, hash640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc. Auditoría matemática/código mapa aprobada; reproducción independiente root92790 exit0/FULL PASS4096 y hash coincidente. Novedad: triples pequeños/mixtos fuera de la región053 tasas>=31.5. NO cuatro/todos los órdenes ni nueva ventanaT; signo global OPEN. Historia de encierros de resto fallidos preservada en audit, sin cambio de malla/precisión/margen.


### Ronda083 — Factorización recíproca pfaffiana ALLorders (IDENTIDAD PROVED)

Fuentes phase211: `POWER_RECIPROCAL_PFAFFIANS_083.md`, `POWER_RECIPROCAL_PFAFFIANS_AUDIT_083.md`. Para Kij=(Fi+Fj)/(ui+uj), Ri=ui/Fi,Si=uiFi y (A_R)ij=(Rj−Ri)/(ui+uj), se prueba detK=P_n(A_R)P_n(A_S)/productoRi. P_n es Pf sin borde para n par y Pf con borde FINAL de unos para n impar. Prueba por desplazamiento, actualización rango2, cofactores impares y congruencias; incluye singulares/nodos coincidentes. Álgebra clásica atribuida (Okada/Knuth/Ishikawa–Okada–Tagawa–Zeng; anti-Löwner como antecedente), sin reclamo de prioridad mundial. Nuevo respecto del corpus: especialización exacta de todos los órdenes, no signo. Productos Pfaffianos para la Phi real siguen OPEN; PSD exige todos los subconjuntos principales. NO nueva W/T ni orden4; global OPEN. Auditoría root/mapa aprobada.


### Ronda084 — Turán local suficiente para Pfaffiano4, falsificador y cola real (PROVED acotado)

Fuentes phase211: `POWER_FOUR_TURAN_084.md`, `POWER_FOUR_TURAN_AUDIT_084.md`. PF(A_f)=−det[1,x,f,xf]/producto(ui+uj); f'>0,f''<0 y T_f=2f'f'''−3f''²>0 en TODO un intervalo implican Pf>0 para TODOS sus cuatro nodos por Rolle y Wronskiano. Para R=u/M,S=uM las obligaciones NR,NS son explícitas; se prueban NR>1/4,NS>19/4 en A=u+.5>=128 con aritmética completa. Compacto .5<u<127.5 OPEN; no cuatroglobal. Falsificador recíproco R=1+x−x²/16,S=x/R conserva propiedades escalares073/077/080 pero detK4<0 para todas las cuádruplas distintas en(.5,1): sólo NO-GO de herencia escalar local, no Phi/W negativo. La cola ya estaba cubierta por053; NO nuevaW/T. Auditoría root/mapa aprobada. Apéndice clásico083 Rolle/Hankel también auditado: criterio suficiente abstracto, signos de los cocientes reales OPEN.


### Ronda085 — W completa para CUATRO potencias arbitrarias ai>1 (PROVED)

Fuentes phase211: `POWER_STATE_085.md`, `POWER_FOUR_GENERATORS_085.md`, `POWER_FOUR_GENERATORS_AUDIT_085.md`, `tools/power_four_turan_compact_085_verify.py`. CertificaNR,NS>0 enTODOu∈[.5,127.5] con16384panelesdyádicos fijos/512bits/cap45/Taylor40 y restoCauchy racional<1e−16. Constructor61911 exit0/FULL PASS ambasfunciones, hash4916689a48baf3164b8e99ff8ff7973dbd505367cf9ee46b17b7efc9845abf46; auditoría matemática/código mapa aprobada; reproducción independiente root29132 exit0/FULL PASS16384 y hash coincidente. Exterior084+Rolle084+factorización083+menores080⇒kernel completo PD paraTODOSlos cuatro exponentes distintos ai>1, repetidosPSD/función no nula positiva. ARCH/polar/TODOScontactos conservados. Nueva cobertura exponentespequeños/mixtos, no nuevas tasasgrandes ya053. NOcinco/todoslosórdenes ni ventanaT; objetivo globalOPEN.


### Ronda086 — Curvatura REAL global por tres densidades y TP (PROVED estructural)

Fuentes phase211: `POWER_THETA_DENSITY_CONCAVITY_086.md`, `POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md`. Para R(lambda)=sqrt(lambda)/M(sqrt(lambda)), se prueba R''<0 enTODOlambda>0 SIN usar080: densidades tPhi,(tPhi)'',−Phi' normalizadas por tPhi dan[1,A,B], B'=D/t²>0 y (A'/B')'=tN077/(pD²)>0. Su determinante es negativo; sinh(ut) TP3 y su versión confluente, probadas por serie/Cauchy–Binet, más Andreief absolutamente convergente trasladan ese signo a W(Z'/u,uZ',Z)=f1³R''<0. Se conservan bordes/paridad/factores2; no se supone positividad de cada densidad. Descarga una curvatura real mediante estructura específica077, distinta de meraidentidad; depende073/077 ya probados, no elimina el certificado fijo de077. Recupera triples079/080 y fortalece la curvatura a todaλ>0; NO nuevaW frente080/085, no admisibilidad ai<=1, no jerarquía superior/allorders/T/global. Auditoría mapa aprobada.


### Ronda087 — Siguiente Wronskiano REAL en el origen (PROVED puntual)

Fuentes phase211: `POWER_THETA_DENSITY_ORIGIN_087.md`, `POWER_THETA_DENSITY_ORIGIN_AUDIT_087.md`, `tools/power_theta_density_origin_087_verify.py`. Para densidadesR4 tPhi,(tPhi)'',−Phi',−Phi''' se decide W_lambda(1,A,B,C)(0)<0 mediante UN encierro fijo racional70dig,Q0..10,modos1..8 y colacompleta m>=9, prefactorpi exp5t/2/binomialconvolutionincluido. Constructor/root/mapa exit0NEGATIVE mismos extremos/hashf8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7. Por continuidad el signo deseado pasa en una vecindad existente SIN radio; no Chebyshevglobal. Darbouxexacto Wt=−k³J²(E/J)' ycoefV10=W_R3/840 localizan obligación adicional, NOpreservaciónautomática. RamaS4/globalraising OPEN; ningunaWextra respecto085, no5/allorders/T. Auditoría aprobada.


### Ronda088 — Wronskiano REAL R4 exterior, toda cola theta (PROVED)

Fuentes phase211: `POWER_THETA_DENSITY_OUTER_088.md`, `POWER_THETA_DENSITY_OUTER_AUDIT_088.md`, `tools/power_theta_density_outer_088_verify.py`. Prueba TODOt>=1: Wt(1,A,B,C)<−4000y6/t²,y=pi exp2t. Primer modo exacto con27coefpositivos tras desplazar t1,y21 y margen4096; cola theta COMPLETA hastaV6 mediante cancelaciónlog, Euler/Bell6, E62523502209/6553600000000000000000, caja128y y polinomio55monomios conK30936927338496; error<96t²y6. Constructor/root/mapa Fraction4PASSexit0, hashd2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4. Da signo de determinantes de densidad para cuatro nodos TODOS>=1, no integral completa. Compacto0<t<1OPEN (087sóloentornoorigen no cuantificado); noWextrarespecto085, no5/allorders/T. Auditoría aprobada.


### Ronda090 — Secante recíproca y una curvatura del resto (PROVED real tras089)

Fuentes phase211: `POWER_RECIPROCAL_SECANT_CONCAVITY_090.md`, `POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md`. LemaTf>0⇒secante recíproca estrictamente cóncava, también para anclaINTERIORP conambasorientaciones. InputTRglobal descargado089(constructor/rootFULLPASS): h=1/bstrictconcava; con086/078 todosparesGpstrictPD. REST-SECANTS yTg=a²TR descarganademás S_G(x)=sqrt(x)Gp(sqrt(x)) estrictamente cóncava TODOSp,x>0. Laotra R_Gcurvatura exigeTh>0globalOPEN, equivalenteenconfluenciaanclada al siguientejet: W(x,x²,G,xG)=−a²G⁴Th. ANCHORED-FIVE tiene nodo0auxiliarNOadmisibleW. NoherenciaBASE/TuranGp/allorders/Wnueva/T. Auditoríamapaaprobada.


**Actualización090§9, NO-GO de herencia genérica (PROVED):** w=(5−e^−x)/4 y f0=1,f'=1/w² definen f positiva, creciente, cóncava y T_f=e^−x/w5>0 global. Sin embargo H=x/(f−f0)=1+x/4−x²/12+5x³/192+O(x4) tiene T_H(0)=−1/192 y T_H<0 en una vecindad positiva. Antiderivada y jets exactos auditados root/mapa; sin campaña. Refuta sólo herencia automática T_f⇒T_H, NO T_h de Phi ni W; S_G real sigue PROVED y T_h real OPEN. Consolidado en090, sin registro091 duplicado.

### Ronda089 — Transporte REAL R4 global y T_R>0todoeje (PROVED estructural)

Fuentes phase211:`POWER_STATE_089.md`,`POWER_THETA_DENSITY_COMPACT_089.md`,`POWER_THETA_DENSITY_COMPACT_AUDIT_089.md`,`POWER_THETA_DENSITY_TRANSPORT_089.md`. Constructor40406FULLPASS1024origenλ+8192restot,hash995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa; auditoríamath/literalaprobada,reproducciónindependienteroot87911exit0/FULLPASS1024+8192ymismohash. Boundsthetacomplejos+16modos/colascoefantesderivar+Cauchydeterminante,parámetrosfijos,sinajustes. Empalme088⇒WronskianR4negativoTODOt>0. OrdenECT[1,B,A,C]usaWronskianosprevios086sinpresuponerA'>0; Rolle⇒detdensidadesnegativoTODOSnodos. SinhTP4/Andreiefconfluente⇒W(Z'/u,uZ',Z,u²Z)=−F0⁴T_R<0⇒T_R>0TODOx>0.090aplicableglobal⇒h=1/bstrictconcava yparesdelrestoGpPD via078/086. NoS4global/noherenciaTuranGp/allorders; ningunaWextrarespecto085niT,globalOPEN.


### Ronda091 — Pi/s no monótono para cofactores REALES (NO-GO de criterio, PROVED)

Fuentes phase211:`POWER_PEANO_MONOTONICITY_OBSTRUCTION_091.md`,`POWER_PEANO_MONOTONICITY_AUDIT_091.md`. Para cofactoresellúltimacolde[w,v,w'',*], w=tPhi,v=−Phi', Pi(s)=Σell_i(s−ti)+, W3=w³(B')²J>0real086. Cerca de CUALQUIERt0>0 con ti=t0+(i−1)eps, ell=eps³W3[−1,3,−3,1]+O(eps4). (Pi/s)'=Σactiveell_i ti/s² tiene primerprefijo<0 ysegundo>0; refutaambasmonotoníasglobalesparaTODOSnodos. Peanoexacto det[w,v,w'',K]=∫s zeta[Pi/s−Pi(b)/b] conserva momento/cruceyFubini. Sólo falla esecriteriosuficiente: integral/menoranclado/T_hREALsiguenOPEN, compensaciónposible, ECTR4real089 no refutado. NoWnegativo/nuevaW/T/global. Auditoríaroot/mapaaprobada.


### Ronda092 — Cero REAL de la carta de eliminación Delta (PROVED acotado)

Fuentes phase211:`POWER_SHIFTED_WRONSKIAN_092.md`,`POWER_SHIFTED_WRONSKIAN_AUDIT_092.md`,`tools/power_shifted_wronskian_092_verify.py`. IdentidadDelta=−W(w'',v'',w4)/(w³k²J). Cerca0 Wshift=8Phi0³t6[D0+Ot²], con−56488961026<D0<−56488961025 usandoEXACTAMENTEintervalos087; constructor/root/mapaPASS,sinotratheta. Exterior088jetsVj=2^jy+O1hasta6 paganpolinomiofinito: Wshift/Phi³=4096(2t²−1)y9+O(t²y8)>0eventual. PorcontinuidadDelta tieneceroREAL, carta2×2noinvertibleglobal. Abel: ambasimágenesD3(1/w),D3(t/w) tienenWronskian noidénticocero concero; ningunaODEhomog2mónica concoefcontinuosGLOBALpuedecontenerAMBAS. Sóloexcluyeesaregularizaciónuniversal, nocancelaciónparticularK/otraODE/gauge/carta/orden. NoWnegativo/menorancladodecidido/nuevaW/T/global. Auditoríamapaaprobada.


### Ronda093 — Jet particular REAL seleccionado por bordes (PROVED local)

Fuentes phase211:`POWER_PARTICULAR_ORIGIN_DESIGN_093.md`,`POWER_PARTICULAR_ORIGIN_AUDIT_093.md`,`tools/power_particular_origin_093_verify.py`. Dpart=Pκ+Qc+R,κ=τ0/a−1; NUM=QPhi0I0+PI1I0+(R−P)Phi0I2=Phi0I2Dpart. ÚNICotestmomentosI0..2:128paneles[0,2],Taylor64/cap65/512bits,16modostheta+colascoefcompletas+restotemporal2^-140; parámetrosauditadosantesrun. Constructor37905exit0PASS128/NEGATIVE,hash57c0656deb1767e00a4de674a0f5f6556886eca06edbc93ae1ef8488b032c67e; reproducciónindependienteroot94506exit0/FULLPASS128ymismohash. Dpart<0 (aprox−21658.19847758sololectura)⇒W(w,v,w'',K)<0envecindadexistentedel origen,sinradio. Verifica(nofalsifica)premisalocalparticular; noglobalQF/conoselector/Deltauniversal/nuevaW/T. Auditoríamath/literalmapaaprobada.


### Ronda094 — Distancia exacta y densidad de UNIÓN diagonal en L² (PROVED)

Fuentes phase211:`POWER_HIGHPASS_DIAGONAL_DENSITY_094.md`,`POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md`. CayleyUNITARIOsinpeso llevaQ^rVn aS_n,r=(1+z)^rPdeg<n. dist²(1,S)=1−A,A=[(n+r−1)!]²/[(n−1)!(n+2r−1)!],porGram/Dodgsonconbordesa0/b0. exp(−r²/n)<=A<=exp(−r²/(n+2r−1))upperr>=1; r0A1. UNIÓN_nQ^r(n)Vn esL²densaiff liminf r(n)²/n=0; pruebaMISMOespacioparaaproxpolinomios yexcepcionesfinitascon1+εzM. Todosbloquesr>=n tienen distancia>1/2alvectorbase; finitobloquesconfluentestasaFijano reparanUNIÓN. Diferencia016:normaponderadaallí,distanciaEXACTAL²sinpesoaquí. NOafirmaenvolventelineal/continuidadW/crosses/mezclasninuevaW/T/global. Auditoríasroot/mapaaprobadas.


### Ronda095 — Cola PARTICULAR K con tres derivadas completas (PROVED analítico)

Fuentes phase211:`POWER_PARTICULAR_TAIL_095.md`,`POWER_PARTICULAR_TAIL_AUDIT_095.md`. ParaKreal seleccionadoportail, W(tPhi,−Phi',(tPhi)'',K)<−3071Phi⁴t²y² enTODOt>=64. StripthetaCOMPLETO|Rtheta|<2^-460⇒pboundholomorfo; IBPexactaK/Phi=1/p+resto(6+25|z|)/Y², Cauchycontrola3derivadas(ningúnOrealderivado). ModeloW[t,q,tq²,1/q]=−128q²(6t²+4t−1);7erroresmultilinealespagadosporC=1e6(1+39321600)³<2^98,umbral64analíticosinmuestras. Objeto distinto088densidadoriginal/092cartauniversal; evitainvertirDelta.093sóloorigensinradio,intervalointermedioOPEN; no globalparticular/condeselecciónni nuevaW/T/generadores. Auditoríamapaaprobada.


### Ronda096 — Proyección uniforme con TODAS las tasas, objetivo fijo (PROVED)

Fuentes phase211: `POWER_VARIABLE_RATE_HIGHPASS_096.md`, `POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md`. Para f0(t)=sqrt(2u0)exp(−u0t) FIJO y TODOS u>0,n>=1,r>=1e12n³, ||Proj_(Q_u^rVn(u))f0||²<=200n/sqrt(r)<=1/5000. Por tanto distancia a la UNIÓN con TODAS las tasas >=sqrt(4999/5000). Prueba autónoma Gegenbauer/Rodrigues/Gamma, centrado con ambas paridades y factor4^r/pi, NEAR por evaluaciones imaginarias, FAR por Gram exacta094 y logs explícitos; sin campañas. Diferencia094: allí tasa fija, aquí objetivo fijo y tasa variable; diferencia016: aquí L² sin peso. Cono060 incluido. NO envolvente lineal/cruces/mezclas ni otras familias continuas iniciales; no W negativo ni cierre/imposibilidad global ni nuevaT. Auditorías root/mapa aprobadas.


### Ronda097 — T_h REAL directa, cola u>=512 y jet regular (PROVED acotado)

Fuentes phase211:`POWER_DIRECT_RECIPROCAL_TURAN_097.md`,`POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md`. Identidadexacta T_h=a[auN_S−4C_h]/[16u³(au−M)^4]. BOX084con aritméticaCOMPLETA daN_S>2M²,C_h<4M³; ancla078a>1/25 yMupper/gapmonótono pruebanau>8M TODOu>=512⇒T_h>0allí. Sinmuestras/certnuevo. OrigenregularN=M/u=a+b1x+...+b4x4,b1<0por086; T_h0=12a/b1⁴detHankel3(a..b4),signoNOevaluado. ObjetivoexactomásdébilqueWronskianparticular093/095; uinclinación≠tiempot. Compacto0<u<512OPEN,noT_hglobal/R_GtodoslosP/triplesGp/cinco/allorders/nuevaW/T. Auditoríaroot/mapaaprobada.


### Ronda098 — T_h REAL exacta en el origen (PROVED local)

Fuentes phase211:`POWER_EXACT_H_ORIGIN_DESIGN_098.md`,`POWER_EXACT_H_ORIGIN_AUDIT_098.md`,`tools/power_exact_h_origin_098_verify.py`. ÚNICOtestseismomentosparesI0..I10con128paneles[0,2],Taylor64/cap65/512bits,16modos+EPScoefcompleta,REM1e12adaptado ytailtemporal2^-138paraorden10. Zprec11→log11/Mprec10daNcoefcumulantesa..e; H3=ace−ad²−b²e+2bcd−c³ yTh0=12aH3/b⁴. Constructor19778exit0FULLPASS/H3POSITIVO,hashbebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9; reproducciónindependienteroot57072exit0/FULLPASS128ymismohash. AsíThREAL0>0(aprox3.15513e−5sólolectura)yentornoexistentepositivosinradio. ObjetivoEXACTOmásdébilquedensidadparticular093;0auxiliarnoexponenteW. Compactointermediohasta097u512OPEN,noThglobal/triplesGp/cinco/nuevaW/T. Auditoríamath/literalmapaaprobada.


### Ronda099 — T_h REAL global, triplesGp y cinco nodos AUX anclados (PROVED)

Fuentes phase211:`POWER_STATE_099.md`,`POWER_EXACT_H_GLOBAL_DESIGN_099.md`,`POWER_EXACT_H_GLOBAL_AUDIT_099.md`,`POWER_SCHUR_TRIPLES_APPLICATION_099.md`. Constructor98529FULLPASS2048/hash6712eb8542b4d8b7e0836260fba831cd44ccaffb7f1ea321df0a0a32668d51d7; root8310exit0/FULLPASS2048ymismohash. S=Ntilde/u15=(16/a)NUMλENTERApar; Schwarzlocal/polysPSPC y gaugeexp−4Mc(u−c)antesdatos paganCauchyB2^169/Taylor104/cap109/1024bits,2048paneles[0,512],sinajustesencorrida. Más097⇒Th>0TODOx>0,098incl0.090ancla+082⇒RG/SGstrictconcavas yTODOStriplesKGpPD paraTODOp. DobleSchurcongruenciaREAL(noforzosamentepositivad_i)⇒bloqueK_M{0,p,z1,z2,z3}PD.0auxiliar correspondea_orig1/2NOadmisible: NOcincoWgeneradoresarbitrarios,nuevaW/T/allorders; siguienteTuránrestoOPEN. Auditoríamapaaprobada.


### Ronda100 — Observable REAL de la pareja J/K no creciente (PROVED, clase acotada)

Fuentes phase211:`POWER_PAIR_OBSERVABLE_SCOPE_100.md`,`POWER_PAIR_OBSERVABLE_SCOPE_AUDIT_100.md`. ParaKPAR078/Jpositivos, eta=−K'/J es imparsuave, eta0=0 y0<eta(t)<a/tparaTODOt>0⇒eta∞0, no monótona enningúnsentidoglobal. Balance∫(aPhi−J)=0+uncruce paga−K'>0. IBPbilateralexacta E_(J,u)eta=uZK/ZJ=ub=a/M−1/u, h=u/Eeta. F(u)ya081explícitamenteatribuida, no otroNO-GOdeF/Gp; nuevoobjetoobservabletemporal deLApareja. Sóloinvalida clasequeexigeetacreciente, no otrascomparaciones/datos/parejas/invariantes. NoTh/Wnegativo,nuevacobertura/allorders/T/global;099permanecePROVED. Auditoríamapaaprobada.


### Ronda101 — Curvatura logconvexa del potencial insuficiente (PROVED, auditoría aprobada)

Fuente phase211: `POWER_LOGCONVEX_CURVATURE_OBSTRUCTION_101.md`. Potencial AUX explícito V=A[cosh(t)+10^-4 cosh(10t)], A=10^46: V''>1, V'''/V'' estrictamente creciente por logconvexidad estricta de V'', TODAS derivadas pares positivas y TODAS impares positivas en t>0. Tres nodos U_i=A*i*10^-4 y vector (1,-2,1) dan c^tK_Mc<−3delta^4/(2A): inversa de v' con jet quinto d=−51675000000000/107213535210701<−2/5, resto elemental <=100u^7; concentración IBP exacta <=A^-1/2. Diferencia074: allí potencial polinómico, curvatura no logconvexa en cola y derivadas altas nulas. Sólo refuta esa candidata genérica reforzada de073; NO incorpora todos los inputs077/089/099, que el triple negativo no puede satisfacer conjuntamente. No Phi/W negativo, nueva cobertura, herencia general ni signo global;099 vigente. Consulta DEDUP y chequeo racional PASS; fuente y auditoría independiente `POWER_LOGCONVEX_CURVATURE_AUDIT_101.md` aprobadas; coeficientes y costes reproducidos por Fraction exacta.


### Ronda102 — Cocientes temporales REALES estrictamente decrecientes (PROVED)

Fuentes phase211:`POWER_REAL_PAIR_MONOTONICITY_102.md`,`POWER_REAL_PAIR_MONOTONICITY_AUDIT_102.md`. (K_even/J)'<0TODOt>0 porvalle077+Rolleparconbordes; (Psi_p/D_p)'<0TODOSp,t>0 porECT4impar089⇒Chebyshev4PAR[J,Phi,J'',Phi'']. ParaF=Psi−rD,LpF''=(1+rp)J''+(pbeta−p²)J−rcPhi''−betacPhi tiene<=3raíces; RolleD²yLpganan2,descartanraíz dobleF/estaciónratio. Colaspositivas0<Psi/D<=2tau/c→0fijansigno;normalizaciónexactaGp=c z ZPsi/ZD. Se conservanmultiplicidades/bordes/supertails,sinnuevoscertificados. ObjetoDISTINTOeta100(no contradicción); usa075077089reales,nohipótesisgenéricafalsa101. Sólo parejasactuales/primerpivote: preservaciónECT4/positividadtrasnueva reducción/allordersOPEN,noWextra/T/cincoadmisibles. Auditoríasroot/mapaaprobadas.

**Corolario102§8 aprobado (mismo resultado ampliado):** A=D_p,B=Psi_p yF=zZB/ZA=Gp/c. Cov(rho,t tanhzt)<0⇒q aF>d y h=dA−qB tiene cruce−/+ con balancecosh. Green075 construyeE>0,par/supertail/Neumann, ZE=(dZA−qZB)/(z²−q²). F1=d/z(ZB/ZE−q), residuo r_q=q d²/(q aF−d)>0. U=B−gammaE de masa0 es el NUEVO numerador: cruce/positivadensidadXi todavíaOPEN; no se infiere deB/A. EscalaoriginalGp=cF conserva cE,cF1,cr. Denominador siguientePROVED, pareja completa/monotonía/herenciaallorders no. Auditoríasroot/mapaaprobadas; sin nuevaW/T.

**Complemento099+102 (PROVED, mismo bloque):** con inputADICIONAL099, R_F,S_F paraF=Gp/c sonstrictconcavos yanalíticosen0 (aF>0). DET3con0 ydivididasstrictnegativas,incl[0,q²,q²],danK_F{0,q,z}PD. DobleSchur⇒R_next(z)>0 z!=q; coeficientescuadráticospositivosDET3/ell² y ell'(q)>0pruebanR_next(q)>0. Así el resto REALtransformadoyapositivoTODOSp,q,z>0, no sólo denominador/residuo. Ucross/Xipositive/monotoníanuevapareja/kernelcruces siguenOPEN: positividadtransformada≠densidadpositiva.0auxiliarNOadmisibleW,no nuevaW/T/allorders.


### Ronda103 — Límite REAL de la pareja y signo puntual del origen (PROVED)

Fuentes phase211: `POWER_REAL_PAIR_DOUBLE_LIMIT_103.md`, `POWER_REAL_PAIR_LIMIT_ORIGIN_DESIGN_103.md`, `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md`. Escalas positivas A_p=pD_p y B_p=(ap/M(p))Psi_p convergen a(J,K_even) en normas con peso exponencial fijo y derivadas, por resolvente bilateral y primitiva doble. Para q fijo el Green es continuo; luego E_*(q)/q→H, H''=b0J−K, b0=massK/massJ, Hmass>0. Así U_lim=K−(massK/massH)H. El test puntual único P=720I0²(K0Hmass−KmassH0), polinomio de ocho términos en I0,...,I6, dio NEGATIVO: P=[−3.1683047444094325e−13±2.16e−30], U_lim(0)=[−1.35855717857699839e−6±8.09e−24]. Certificado fijo128 paneles[0,2]/Taylor64/cap65/512bits/16modos, colas theta y temporal completas. Constructor68812 y root91737 exit0/FULLPASS; hash5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080. Auditoría matemática/literal mapa y root aprobadas. También U_original(0)<0 para q pequeño fijo y p suficientemente grande, sin umbrales explícitos. Sólo signo puntual de origen: NO falsificador, cruce global, positividad Xi, nueva W/T ni cierre de órdenes;099+102 siguen vigentes. Papers intactos.


**Extensión analítica103 posterior (PROVED, sin nuevo test):** H/K_even es estrictamente decreciente en TODOt>0. Para F=H−rK, D⁴F=(b0+r)D²J−raD²Phi−aPhi+J es combinación no trivial de EVEN4(102). Doble Rolle par con bordes excluye raíces dobles de F y estaciones del cociente. Cola K>=aI/2,H<=b0tauI⇒H/K→0 fija signo estricto. Promedio de masas⇒U_lim=K−(Kmass/Hmass)H tiene exactamente UN cruce simple−/+ y Xi_lim=G0U_lim>0. El caso LÍMITE completo queda probado; el certificado negativo previo de origen se conserva como comprobación independiente cronológicamente anterior. NO se propaga por límites el cruce global a parámetros FINITOS p,q, ni hay nueva W/T/allorders. Auditorías root/mapa aprobadas.


**Ampliación103 a TODOq>0 (PROVED):** para la pareja REAL(J,K), E_q=Gq(dJ−qK),d=qZK(q)/ZJ(q)>0. Lq(E_q−rK)''=(d+r)J''−raPhi''+a(rq²−q)Phi+(q−rq²)J es EVEN4 no trivial; Rolle D²+Lq excluye estaciones de E_q/K. Continuidad en q para cada t y límite C1 E_q/q→H fijan (E_q/K)'<0 para TODOSq,t>0. Promedio estricto de masas⇒U_q tiene un único cruce simple−/+ y Xi_q>0 para TODOq. Resultado final ya no requiere q pequeño; sigue siendo pareja p→infinito, SIN conclusión global para p FINITO ni nueva W/T/allorders. Auditorías root/mapa aprobadas, sin nuevo cómputo.


**Puente exacto103 a pivotes FINITOS (PROVED):** Con lambda=p²M(p)/(ap−M(p)), se tienen beta D_p+p²Psi_p=lambda K, LpPsi_p=J−lambda K y Psi_p=(lambda/p)E_*(p). Por tanto Psi_p/K decrece estrictamente y D_p/K crece estrictamente para TODOS p,t>0 finitos, mediante103 para todo q, sin suponer estabilidad del cruce bajo límites. Para U=Psi−gammaE, LpLqU es una combinación de[K,J,Phi,J''] con coeficiente de K igual a−lambda alpha≠0, alpha=gammaq−q²>0. La propiedad Chebyshev4 de esta familia MIXTA bastaría, pero sigue OPEN: EVEN4 no la prueba; se conservan los antecedentes093/095. Bajo ese input suficiente, la orientación−/+ usa además Rnext>=0, ya deducida de099+102 mediante Schur para z distinto de q y continuidad en el valor removible z=q. La orientación inversa forzaría Xi<0 y contradicción. No se afirma nuevo cruce global de U finito, positividad Xi, signo W/T ni todos los órdenes; no se ejecutó otro certificado. Auditoría root/mapa aprobada.

**Prefijos mixtos103 (PROVED):** [K,Phi,J] es Chebyshev extendido global de dimensión3: f=AK+BPhi+CJ con tres raíces daría D²f no trivial en EVEN4 con al menos cuatro. Para tau=J/Phi,kappa=K/Phi=tau(K/J), S=kappa'/tau'>0 y W(Phi,J,K)=Phi³(tau')²S' nunca se anula. S'>0 contradiría(K/J)'<0 mediante el promedio de cola de S; así S'<0 y kappa es estrictamente convexa como función de tau. Los primeros tres Wronskianos en orden[K,J,Phi] son positivos. El CUARTO mixto sigue OPEN; sin nuevo certificado ni signo W/T/allorders. Auditoría root/mapa aprobada.


### Ronda104 — Gate mixto de origen positivo y cola analítica (PROVED, alcance local)

Fuentes phase211:`POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md`,`POWER_MIXED_FOUR_ORIGIN_AUDIT_104.md`. Familia[K_even,J,Phi,J'']; matriz regularizada enlambda=t², factoresk! ypuenteW_t=64Phi0⁴t⁶[Dmix+Ot²]. Recuperación087 INTACTA porhash y cajas103 racionales completas, sin cuadratura nueva. Constructor y root exit0/PASS: Dmix>0 (extremos exactos en fuente/log), hash063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105. Log104 persistePhi0,z1,z2,z3 outward antesnoarchivados. Prueba holomorfa independiente con toda cola theta y7errores multilineales daWmixed/Phi⁴>6t²/y² paraTODOt>=64. Por tanto origenpositivo envecindadexistente SINradio ycola positiva; compacto intermedioOPEN. Prefijos1–3globales103vigentes, pero NOCheb4global, falsificador, cruceUfinito/Xipositiva, nuevaW/T/allorders. Auditoríasroot/mapaaprobadas; no más tests. Papers intactos.


### Ronda105 — Kernel Volterra mixto bruto de signo variable (PROVED, clase acotada)

Fuentes phase211:`POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md`,`POWER_MIXED_VOLTERRA_AUDIT_105.md`. Sobre la pareja REAL, tau=J/Phi,kappa=K/Phi,E=−tau'>0,S=kappa'/tau'>0,w=−S'>0,D=tauS−kappa>0. Identidad exacta w'+Bw+RS−TD=1, B=(2−2V''tau)/E,R=(tV'−1)'/E,T=(V'^2−V'')'/E. CT3 yK/J→0 danS=integralcola w yD=integralcola tauw; kernelH(t,s)=R(t)−T(t)tau(s). Jets theta completos y cambio de variable con dominación(1+u)e^-u prueban tauV'/t→1, luego[(tV'−1)'−tau(V'^2−V'')']/(tV')→−2. AsíH<0 cerca de s=t para t grande, peroH→R(t)>0 al s→infinito. Refuta SÓLO positividad punto a punto del kernel BRUTO, distinto del Peano091. No signo de integral, exclusión de gauges/reordenaciones, W4mixto/Ufinito/W ni obstrucción global. Auditorías root/mapa aprobadas, sin cómputos nuevos ni papers modificados.


### Ronda106 — Control holomorfo de integrales mixtas normalizadas (PROVED, sin signo)

Fuentes phase211:`POWER_MIXED_NORMALIZED_INTEGRAL_106.md`,`POWER_MIXED_NORMALIZED_INTEGRAL_AUDIT_106.md`. StripRe z>=−1/16,|Im z|<=1/16: Theta=(2y−3)(1+Rtheta),|Rtheta|<1/4, Y=|pi e2z|>21/8. Variablevreal y r=.5Log(1+v/y) dan representaciones normalizadas EXACTAS de tau=J/Phi ykappa=K/Phi; igualdadreal extendida holomórficamente por dominación, sin cambio de contorno supuesto. FactorTheta/jacobiano acoplado pagaA<=7/(2Y)e^-v(1+v)^2. CotasY|tau|<100(1+|z|),Y²|kappa|<1000(1+|z|); colav>=512<2^-450, modosm>=17<2^-675 parafunciones escaladas, incluidosnumerador/denominador ycolumnaX porlogderiv. Cauchy pagaerrorescoef32^j. BoundWronskianescalado2^120 ydivisibilidadpart6+Schwarz danboundregularizado2^168. Resuelve control de evaluación/errores, NOpositividad. Diseño de ejecución, cuadratura finita/tolerancias/partición/orden siguenPENDIENTES; nocorrida/nuevojet/muestra. Cheb4mixto/Ufinito/W/T/allordersOPEN. Auditorías independientes root/mapa aprobadas; papers intactos.


**Ampliación106§8 (PROVED, herramienta sin ejecución):** Gauss–Legendre64 en diez intervalosv[0,1],[1,2],...,[256,512], discosradio2h,dominiocomplejoRe(y+v)>2 yRe(1+sv/y)>4/5. Mayoranteuniforme2^34 también para parámetrotemporalballsemiancho<=1/64, condominioextendido|z−c|<=3/64 y escalasconstantes. Cauchycoefj yexactitud127/pesospositivos paganerroranalíticototal2^(−83+5j)<=2^-68 paraj<=3. Bolasnodos/pesos,aritmética,colasmodos/v yfactorialesdebenpagarseadicionalmente ANTESWronskiano. Auditorías matemática/literal root/mapa aprobadas; diseño107/ejecución/signos siguen pendientes.


### Ronda107 — Certificado compacto mixto INCONCLUSO (reproducido)

Fuentes phase211:`POWER_MIXED_FOUR_COMPACT_DESIGN_107.md`,`POWER_MIXED_FOUR_COMPACT_AUDIT_107.md`. Diseño/literales auditados ANTESdatos: origenlambda[0,.25],Phi128/cap1025/1024bits/Taylor512,recurrenciasJ/K ymoment103; RESTGauss64*10/512bits/cap4/5; subdivisionleftfirstdepth10/eval8192fijos. Root5594 yreproindependientemapa46719 terminaronexit2/INCONCLUSIVEorigen:11eval,0accepted,depth10lambda[0,1/65536],det[+/−2.94e−3]. RESTNOejecutado. Logsroot/auditpersistidos; hashmain2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054,origin15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553 idénticos/sinmodificaciones. SóloinsuficienciaencierroconESTEpresupuesto: NOfalsificador/obstrucciónmatemática/signonegativo/Cheb4global/Ufinito/W/T/allorders. Nuevarepresentaciónrequiereotro diseñoauditado antescorrida; noajustesparaforzarPASS. Papersintactos.


### Ronda108 — Determinante polinómico correlacionado INCONCLUSO (reproducido)

Fuentes phase211:`POWER_MIXED_FOUR_POLYNOMIAL_DESIGN_108.md`,`POWER_MIXED_FOUR_POLYNOMIAL_AUDIT_108.md`. Cambioalgebraicoauditado ANTESdatos: formar24permscompletasenpolinomios,grado2042real(<=2048),trasladoTaylorallcoef+error2^-200; builders/presupuestos107intactos. Root82660 ymapa28564exit2/INCONCLUSIVE:15eval4accepted,coberturaλ[0,141/8192],depth10en[141/8192,1129/65536],det±2.04e−4;RESTNO. Hash108eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a;107hashesintactos. Logsroot/auditpersistidos. PerfilSÓLOlocalsYAcalculados,noextraprobe:finalcoef0±1.79e−4 yradioadicional≈2.456e−5,asíincertidumbrecentral noseconfundeconvariacióncelda. No decideceroreal/causaúnicadeancho. INCONCLUSO,nofalsificador/obstrucciónmatemática/Cheb4global/Ufinito/W/T/allorders. Otra representación requiere diseño previo, no ajustesparaPASS. Papersintactos.


### Ronda109 — Cauchyclip: origen PASS; certificado total INCONCLUSO por presupuesto

Fuentes phase211:`POWER_MIXED_FOUR_CAUCHY_CLIP_DESIGN_109.md`,`POWER_MIXED_FOUR_CAUCHY_CLIP_AUDIT_109.md`. IntersecciónBASEcoeficientes107conCauchy|phi_k|<=2^(40+k),|J_k|,|K_k|<=2^(42+k),antesrederivar/Q/det108;verdaderoscoeficientespreservados,resto2^-200ymismosparámetros. Root52183terminóexit2/INCONCLUSIVE:origenPASS16/16lambda[0,.25],REST8192eval4113hojasaceptadas. AuditoríalogFractionconfirmacoberturacontiguaREST[1/2,2645/512],longitud2389/512. Siguientecelda[2645/512,1323/256],depth6,NOevaluadaporcap; nofallopordepth/signonegativo. Driverhashc3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba y107/108intactos. NOreproducciónindependiente109niFULLPASS. NoCheb4global/Ufinito/W/T/allorders/obstrucciónmatemática. Logpersistido;papersintactos;auditoríamath/literal/logroot/mapa, sin nuevaevaluaciónporauditor.


### Ronda110 — Cociente theta factorizado: AUDITADO, ejecución root en curso

Fuentes phase211:`POWER_MIXED_FOUR_FACTORED_RATIO_DESIGN_110.md`,`POWER_MIXED_FOUR_FACTORED_RATIO_AUDIT_110.md`. Condición109sinFULLPASSsatisfecha porexit2. IdentidadexactaTheta16=(2y−3)(1+R16),Bm=m4+3m²(m²−1)/(2y−3);ratio=(1+2v/d)(1+Rshift)/(1+R),p16=2y−9/2−6/d−Rt/(1+R). No modosomitidosnifuncióncambiada; mismosorigen109,Gauss107,errores/parámetros/DFS/budgets. Root/mapaaprobarondiseñoyliteralANTESdatos(cachem−1correcto,hashguardscuatroarchivos,nopatch). Primeracorridarootautorizada/encurso, SINresultadofinal,reproducciónniPASSadelantado. No sepromete mejorarencierroocoste. Identidad/controlrepresentación,noW/T/allordersnuevos;papersintactos.


### Ronda111 — Monotonías individuales allp insuficientes para TP2 (PROVED, clase auxiliar)

Fuentes phase211:`POWER_GREEN_PAIR_TP2_SCOPE_111.md`,`POWER_GREEN_PAIR_TP2_AUDIT_111.md`. ParejaabstractaK=1_(|t|<2),J=(1+1_(1<|t|<2))K. Lambda_p=2−1/(2coshp) yGreenVpC1compactoexacto danVp>0,(Vp/K)'<0paraTODOp>0en(0,2). Mismosparams1,2:ratioV2/V1creceen(0,.5],decreceen(1,2),pordesigualdadesanalíticas; menoresnodos(.25,.5)y(1.5,1.75)tienensignosopuestos. InclusoJ/Kstrict↑:añadirdelta t²paradelta>0suficientementepequeñopreservaambosmenoresporcontinuidad;W=Vp' resuelveLpW=2delta t+Dirac1conDirichlet0,Greennegativopruebamonotoníasallp. SuavizarescalóninteriorconKindicadortambiénadmisible; NOseafirmabordescompactossuavesconallp. SóloNO-GOdeimplicacióngenéricamonotoníasindividuales⇒TP2, NOparejaREAL/compatibilidaddiferencial103/MIXED4/W/allorders. Dedup074/101/091/105objetosdistintos. Auditoríasmath/literalroot/mapaaprobadas,sincómputos/campañas,papersintactos.


**Ampliación111§5.3 (PROVED, misma contraclase):** V(x,t),x=p², es además completamente monótona estricta en x para TODO orden y t interior. q_x=−partial_tV satisface(−D²+x)q_x=mu positiva fija(Dirac1, oDirac1+2delta tdt), Dirichlet0,2. Greenpositivo/suaveenxcompactos permite derivar conmedidafinita: A_x partial_x^n q_x=−n partial_x^(n−1)q_x, porinducción signosalternadosestrictos. V=integral_t²q_x heredaCMtodosórdenes. LosMISMOSminoresTP2opuestos persisten: añadirCMparamétrica alasmonotoníasindividualesallp NOimplicaTP2. Sóloauxiliar, noCMdeparejaREALdecidida niW/allordersrefutados. Auditoríasmath/literalroot/mapaaprobadas; sin datos ni campañas.


**Mejora analítica posterior104 (PROVED, sin datos):** conservar las potencias de y en los7errores da61440Ht³/y³+6144H²t³/y⁴+192H³t³/y⁵. Para y>=H suma<2^17Ht³/y³. e²>7 ycomparaciónentera3*7^16=99698791708803>82463372083200=16·2^17H, conH39321600; y/t↑pagaerror<t²/y²paraTODOt>=16. Modelo>7t²/y²⇒Wmixed/Phi⁴>6t²/y² enTODOt>=16, mejorando64. Auditoría root/mapa, sinsampling/certtheta nuevo. NOretoca110 ni declara compacto/global/W antescobertura yrepro.


**Resultado constructor110:** root52878terminóexit2/INCONCLUSIVEporbudget8192,4198hojasRESTaceptadasyorigenPASS16/16. ParserFractionauditorconfirmacoberturacontiguaREST[1/2,845/32],longitud829/32. Siguiente[845/32,3381/128],depth4pendientealcap. Driverhashc629d4ed4b5eeb625a69ee92f6000892b9493c50e825e9ade73bf3a5a9362108. NOFULLPASSdelprogramahasta64. Réplicaindependiente12244sigueMISMOprograma/presupuestosinpararen16; WMglobal112todavíaCONDICIONALhasta coberturaindependiente16+TAIL104. Nofalsificador/obstrucciónmatemática,ningunaactivaciónadelantada.


### POWER — Revisión estratégica y cierre auxiliar WM (sin cierre del signo)

Fuente phase211: `POWER_REASSESSMENT.md`; actualización de110/112. Antecedente explícito: función generadora de R162_803, Theorem H, y D-16; POWER usa su núcleo real de tipo Pick. La diferencia declarada en001 justifica casos finitos y falsificadores, no un mecanismo uniforme nuevo. REF-D no se usa como imposibilidad. Por instrucción del usuario se abandona la continuación automática de la torre: una nueva candidata debe identificar una propiedad que controle todos los tamaños y una diferencia verificable respecto de las obstrucciones previas.

WM PROVED: logs110 constructor/audit idénticos (SHA25690a2ec137e806c8a7f8cce975f7af1cee375d9e48bdaf1c5bc302f7c06428539), origen completo y4198 hojas REST contiguas[1/2,845/32], ambos INCONCLUSIVE por8192evaluaciones, sin FULLPASS hasta64. Cola104 analítica desde16 se solapa y completa Wmixed>0 para todo t>0; prefijos103 dan MIXED4. Quedan activadas las consecuencias auditadas112 (Xi positiva, comparación E/Psi, TP2 real/confluencia y cocientes de la pareja límite). No cinco potencias arbitrarias, conservación indefinida, todos los órdenes ni nueva ventana T. Papers intactos; objetivo global OPEN.


**Auditoría transversal posterior a la revisión de POWER:** phase211 `POWER_CORPUS_OPPORTUNITY_AUDIT.md` y `POWER_GLOBAL_ROUTE_REVIEW.md`. Root y tres revisores contrastaron índices, LEDGER y fuentes primarias selectivas; no se afirma relectura exhaustiva del corpus. No se identificó aún una candidata global nueva justificada entre las familias examinadas. Se distinguen falsificadores de clase, reducciones y obligaciones abiertas; no se usa REF-D como imposibilidad. Se corrigieron etiquetas obsoletas de O-151.4 y06R4, y se incorpora la corrección lógica de TB3-neg desdeR186_092. No nueva torre/certificado ni signo global.


### Completitud en potencias perfectas — alcance algebraico y falsificadores auditados

Fuentes phase211:`SQUARE_COMPLETENESS_OBSTRUCTION.md`,`SQUARE_COMPLETENESS_AUDIT.md` (PROVED,sin nuevaejecución). LocalFp=(1+cpz)/(1−z²),0<=cp<=1, daNmultiplicativa0<=N<=1,N(n²)=1,ell>=0. Endpointc20otros1=ζ/(1+2^-s),antecedenteR163102CorF/R163191,residuo2/3sinFEasumida. ReusaMISMOtestigoprimitivopar007_CThm1conx>1; bordesanalíticosdanC_F(log4)>0,asíWnuevo=Wa3−2log2C4<0. CadamFIJO>=2tambiéninsuficienteconNentero0/1:reemplazo2→2^m,N(n^m)=1;param>=3noátomo2antes8⇒Wm=Wa3<0,residuo1/[2(1−2^-m)]<1.

**TODOSlosórdenessimultáneos, sinintegralidad:** local2=(1−z/2+z²/2)/(1−z),otrosprimosordinarios,N2=1/2,N2k=1k>=2⇒N(n^m)=1TODOn,m>=2. Raícesformalesr±=(1±i√7)/4 demuestranell(2^k)/log2=1−r+^k−r-^k>=0. Pesosv2=√2log2/2<1/2,v4=7log2/4 yMISMO007CdanW<−.00528norm². Residuo7/8,noFEasumida;nofalsificaintegralidad/residuo1/compatibilidadadicional.

**Selección/identificación, NOsigno:** enansatzcp∈[0,1],residuoEXACTO1fuerzacp1inclusoinfinitos(producto≤unfactor). Másgeneralmente,Nmultiplicativa+ALLperfectpowers+N(p)entero>=0+ell>=0fuerzaN≡1:ell(p²)/logp=2−c²⇒c0/1,yc0local(1+z³)/(1−z²)daell(p6)/logp=−1. EstoidentificaLambda,nopruebasusigno. Sóloexclusióndesuficienciadelasclasesdeclaradas,NOimposibilidadglobaldetodousodecuadrados/completitud,NOΛnegativa,nuevacoberturaW/Tnicampaña. Auditoríasroot/mapa completadas;papersintactos.


**Ampliación de residuo normalizado (§11, PROVED, misma clase acotada):** se conserva el factorlocal2simultáneo yseañadenfinitosp>=7conPdelta=1+delta z−delta z²,0<=delta<=2/5. Np=1+delta,Npk=1k>=2; factoresr,sdanellodd>0,elleven>=logp/25. DivergenciaΣ1/ppermiteelegirfinitamenteúltimodeltaracionalconproductoderesiduosEXACTO8/7. AsíF=ζR,RDirichletpolynomialfinito,R1=1:residuo1,sumN=x+O1,Nmultiplicativa0<=N<=Cfinito,ALL-POWERSyell>=0. Compensadoresp>=7invisibles007C⇒MISMOvalorW<−.00528norm². NO N<=1 (Np>1altos),NOintegralidad(N2=.5),NOFE/defectoBohrpequeño. AntecedentesLemaSR163102/resnormalR163802;noideaEulerpresentadacomonueva. No contradicecolapsode§7ni197(controlDelta≠residuo). Auditoríasliteralroot/mapa,sin nuevosdatos ni campañas.


### Gram por traslación theta — identidad y obstrucción de capas PSD

**PROVED, alcance limitado.** Fuentes phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`, `POWER_GRAM_SLICES_AUDIT.md`; auditorías root/casos/mapa, sin certificados nuevos. A(t,s)=integral_0^infinito(t+s+2r)Phi(t+r)Phi(s+r)dr tiene doble transformada [Z′(u)Z(v)+Z(u)Z′(v)]/(u+v), sin factor2. Su desintegración exacta en v da capas Gram para el modelo cuártico. Para Phi REAL no todas pueden ser PSD: la derivada normalizada exige CND de [V′(t)+V′(s)]/(t+s), refutada con tres nodos positivos y V′(R)/R³→infinito. **PSD de A permanece OPEN**; no W negativo, nueva cobertura ni imposibilidad de otro Gram. Dedup dirigido103_47/48,073/074,N_BUILD014/016/018,C9 sin duplicado literal hallado; marco Gram/Pólya clásico, no afirmación de nunca intentado. Compensación conjunta entre capas aún sin cota nueva.


**Addendum Gram — operaciones (PROVED, misma entrada):**074 ya refuta suficiencia de V=g(t²) convexa y con todas sus derivadas no negativas. Mezcla de dos gaussianas distintas falla: (M/u)'=u Var(v)>0 contradice pares001. Convolución conserva el kernel transformado por suma de M; pero mezcla positiva de cuárticas o convolución con un factor cuártico impone cola inferior exp(-Ct⁴), incompatible con Phi real. La corrección hazard DdiagB tiene diagonal (f-tf')/f²<0 por073, no puede descartarse como PSD. Incluso un operador positivo Bop(-Phi')=tPhi existe para la mezcla gaussiana y no basta: la forma A conserva un término de semirrecta no controlado. Sólo suficiencias declaradas refutadas; A real OPEN. NotaGram§7 y auditoría, sin datos nuevos.


### Corrección de cancelación residual L2_BUILD_031 (PROVED)

Fuentes phase211: `CORRECTION_RESIDUE_BALANCE_031.md`, `CORRECTION_RESIDUE_BALANCE_AUDIT_031.md`. La identidad031§3 omite indebidamente módulos p^b<=Q usando B_Q. Contraejemplo exacto M=Q=2,s=(1,1), perfil2T0<log(3/2), interpolante suave S soporte(2/3,5/2),S1=S2=1: W1 tiene filasdelta y la componenteq2 completa es v2/2>0; n>=3 no contribuye. Balance de c2(k) no se transporta a c2(2k). El componente está definido mediante el interpolante explícito030; no se afirma que sea independiente de cualquier interpolación. **TeoremaE de aproximación intacto**, sin W negativo ni cambio del objetivo(S). Aviso añadido a031 preservando texto histórico. Auditoría independiente, sin cómputos/papers.


**Aclaración de reparación031 (misma corrección, PROVED):** en R_Q,Q>=2, exigir anulaciónq2 para TODOS los perfiles e interpolantes deja sólo s0: perfilwidth<log((M+1)/M) daW1delta, soporteimpar hace único el coeficiente deS(j/2), igual a−s_jv2/2. No colapso demostrado en soporte mixto por colisiones diádicas; un ejemplo narrow no decide todos los perfiles. TeoremaE original permanece intacto. Fuente correctiva§5 y auditoría, sin datos nuevos.


**Complemento016§9 — filtro desplazado y límite de las diagonales (PROVED):** en `POWER_DESCENT_AUDIT_016.md`, delta1,u63/2,eta3/4, Qdelta=(s+delta)/(s+u) es un isomorfismo del H_eta fuerte014; su cero externo evita el hiperplano de momento0. Por triangularidad confluente, el SPAN de CUALQUIER cola fr=Qdelta^r/(s+u) es denso. La identidad binomial completa, con d=delta²/u² y producto polar incluido, más015N1, prueba diagonales W[fr] y W4[fr] eventualmente positivas. Sin embargo W4=W−4norm² tiene f0negativo016 y es continua: alguna combinación FINITA de generadores de CADA cola positiva da W4<0. Sólo refuta inferir signo delspan desde densidad+diagonales, aun reparado el momento. NO Wrealnegativa, NOparesPSD ni uniformtodosnumeradores; no nueva familia general cerrada, certificado o ventana. Auditorías root/casos/mapa.


### Ensamblaje PSD de tamaño fijo en la escalera002 — obstrucción limitada (PROVED)

Fuentes phase211: `POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md`, `POWER_FIXED_BLOCK_ASSEMBLY_AUDIT.md`. Un certificado C=sum B_alpha, cada B_alpha PSD soportada en<=k coordenadas originales, exige ones^T C ones<=k trC. Para TODO k fijo, n=k+1 y nodos de la MISMA escalera a_j=32+2N+2j dan L(a_j)=.5logN+O_k1, con psi entero y cola Lambda completa; el bloque normalizado tiene Cij→1. Entonces ones^TC ones→n²>kn=k trC y ningún certificado así existe para algún N finito. Submatrices principales heredan esos certificados: tampoco los bloques iniciales002 que contienen el subbloque los admiten. Caso2 incluye ensamblajes PSD2/Gershgorin escalado. Se excluye sumar certificados2/4/13 o tamaño FIJO para todos los órdenes ENBASEoriginal; NO implica K negativa/PSD arbitraria, NOotrasbases/bloquescrecientes/Schur/partePSDglobaldensa. Dedup186043044/N018019: instrumentos clásicos, clases distintas, sin prioridad absoluta. Auditorías root/casos/mapa, sin cómputos/papers; W global OPEN.


### Desplazamiento simultáneo de exponentes: falla el orden Loewner (PROVED)

Fuentes phase211: `POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION.md`, `POWER_SIMULTANEOUS_SHIFT_AUDIT.md`. La diferencia completa D(f,g)=W(f,g)−W(e^(-2t)f,e^(-2t)g) tiene un plano indefinido. Dos paquetes norma1 separados log2, el primero a distanciaO(epsilon) del borde causal0, dan Dff=O(epsilon^(1−2s)),Dgg=O(epsilon^−2s),s1/8, y Dfg→−3log2/(4sqrt2) por el único contacto2; ARCHsuave/polarO(epsilon). Determinante→−9log²2/32<0. Densidad fuerte014 y continuidad transportan esto a un bloque inicial FINITO [K(32+i,32+j)−K(34+i,34+j)] noPSD. Coeficientes de exponentiales DIRECTAS, sin confundir factoreszeta de rho. AntecedenteN007atom/bump: aquí el borde suprime una diagonal del DEFECTOfullW y paga la reservaARCH antes ausente. Orden contrario ya falla diagonalmente073. Sólo se refuta esta ordenación universalshift2; NO Wnegativa/Knegativa/otros transportes ni todosshifts. Auditorías root/casos/mapa/invariante, sin datos/certificados/papers.


**Addendum IMS al desplazamiento simultáneo (misma entrada, PROVED):** fuenteSHIFT§7 y auditoría. T=e^(-2t),S=sqrt(1−T²),d=1−TtTs−StSs>=0. R=D−W[Sf] conserva ARCH, peine y polar2cosh. Los MISMOS paquetes causales dan Rff=O(epsilon),Rgg=O(epsilon²),Rfg→−3v2/8 y R[f±g]→∓3v2/4; restoIMSindefinido, noWnegativa. Para compactos separados de0, suma_r R[T^r f] tiene coeficiente exacto d/(1−TtTs)∈[0,1], cuyo límite al(0,log2) es1, no0. Convergencia justificada; S no se supone Lipschitz en0. AntecedenteIMS004 explícito; no signo/cancelación global inferidos ni exclusión de otro compensador con prueba propia. Root/mapa literal aprobado, sin nuevos datos/papers.


**Aclaración al objetivo anti-Löwner/Stieltjes (PROVED, no nueva nota):** `POWER_GLOBAL_ROUTE_REVIEW.md`, sección L-DER. L'(a)=Laplace[b(t)dt+ΣLambda(n)logn delta_logn], b=t[(exp2t−1)^−1−exp t]. Tras cualquier tiltA>1 la medida es finita; en(log2,log3) no hay átomos y b<0. No puede existir una medida Laplace POSITIVA que represente L' en NINGUNA raya a>=a0>1. Unicidad autocontenida: tilt, pushx=e^(-t), igualdad de todos los momentos, aproximación polinomial de continuas. AntecedenteformalPaper37cor:bernstein para OTROcociclo;019/020/023 tratan inversoMöbiusgamma, noL'. NO excluye N(x)=M(sqrtx)/sqrtx Stieltjes, NO K/Wnegativas. Es una prevención de ‘Gamma positivo⇒L' positivo como medida’, no cierre del objetivo083. Sin datos/papers.


**Addendum027§8 — inversos gaussianos uniformes refutados (PROVED, misma mezcla real):** `POWER_INTERIOR_CONSTRAINT_027.md` y `POWER_JOINT_AUDIT_027.md`. Para w_a=x^(-1/2)e^(-a log²x), H_a=−w_a'>0, definir FULLh_a=Σmu(m)mH_a(mx),J_a=Σmu(m)w_a(mx),K_a=J_a+xh_a. LeyFIJAV_N inversagamma027 y Tonelli positivo+FubiniABSOLUTO (ΣmH_N(m),Σw_N(m) finitas) dan h_N(1)=E h_VN(1),K_N(1)=E K_VN(1). NEGCOMPLETO022 h128(1)<−33/50 y023 K129(1)<−1/251 fuerzan EXISTENCIAS a_h>0 con h_a_h(1)<0 y a_K>0 conK_a_K(1)<0; parámetros posiblementeDISTINTOS, ninguno calculado. No son prefijos ni Jensen/convexidadW. Refuta ambas premisas gaussianasUNIVERSALES de inverso positivo; NO ERR/Wnegativas, NOheatH_A−Pnegativo, NONStieltjesexcluido. Sin nuevosdatos/certificados/papers; auditoríasroot/mapa/invariante.


### Modelo hiperbólico: Green positivo todos los órdenes; transferencia real abierta

**PROVED para el modelo / OPEN para Phi real.** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. Para phi_a(t)=exp(−a cosh(2t)), a>0, Z_a(u)=K_(u/2)(a), H_a=−D_r²+a²exp(2r) en la semirrecta con borde Dirichlet y R_i=(H_a+u_i²/4)^−1. La identidad positiva M_a(u)/u=(1/2)Tr R_u produce
K_M(u_i,u_j)=(1/2)Tr(H_a R_i R_j)+(u_i u_j/8)Tr(R_i R_j),
una suma de Gram positiva para TODOS los órdenes. Prueba mediante Green/ODE y trazas, sin nuevos datos. Las capas de la desintegración GramSlices NO son todas PSD incluso en este modelo, pues V'(R)/R³→infinito; el Green prueba el kernel completo de M, sin requerir positividad de cada capa. Cotejo dirigido de antecedentes no halló esta aplicación literal; no se afirma prioridad mundial. Auditorías root/casos/invariante, cotejo mapa. La supercola compatible con theta no transfiere la representación: falta una identidad ODE/Green positiva para la Phi REAL; mezclar densidades positivas tampoco preserva automáticamente el kernel logarítmico. NO nueva cobertura W/T ni cierre global real; papers intactos.


**Modelo hiperbólico, §7 — dos transferencias directas excluidas (PROVED, alcance restringido).** `POWER_HYPERBOLIC_MODEL_GRAM.md` conserva el Gram positivo del modelo y prueba que Phi real no es ni una mezcla positiva pura de exp(-a cosh(2t)) (se permite masa infinita, con integral exp(-a)dmu finita), ni phi_a convolucionada con una medida positiva finita no nula (sin suponer soporte compacto). La cola real es 2pi² exp(9t/2)exp(-pi exp(2t)): su tasa obliga el soporte extremo y la representación impondría un prefactor acotado, contradicción. Diferencia frente a la exclusión cuártica de GRAM_SLICES§7: mismo orden doble exponencial, pero prefactor incompatible. Revisión root/casos/invariante. No excluye prefactores temporales, diferenciaciones, combinaciones firmadas ni otros Green; no W negativa, nueva T ni cierre global. Sin datos nuevos ni cambios en papers.


**Modelo hiperbólico, §8 — prefactor afín mediante Robin (PROVED sólo para el modelo).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: para a>0,beta>=0, phi=(beta+a cosh(2t))exp(-a cosh(2t)) tiene transformada beta*y_x(0)-y_x'(0), x=u²/4. Con m=-y'/y y k=y/y(0), m'=integral k² y R_beta=R_D+k tensor k/(m+beta); el borde es f'(0)=beta f(0), con término positivo beta|f(0)|² en la forma. La identidad M/u=(1/2)Tr R_beta y el Gram completo prueban todos los órdenes. Neumann beta=0 corresponde a la derivación de escala; no se afirma preservación por derivaciones generales. El prefactor exp(2t) no es el exp(9t/2) de theta: transferencia real OPEN, sin W/T nueva. Revisión root/casos/invariante, cotejo dirigido mapa, sin prioridad mundial ni nuevos cómputos; papers intactos.


**Modelo hiperbólico, §9 — orden matricial del flujo de escala refutado (PROVED sólo para el modelo).** `POWER_HYPERBOLIC_MODEL_GRAM.md`: aunque cada K_a es PSD, D_a=-a partial_a K_a no lo es en todos los tamaños sobre u>0. La representación P_a(x)=Tr[(H+x/4)^(-1)V_a(H+x/4)^(-1)] tiene coeficientes alternados A_n=(n+1)sum w_j t_j^n, w_j>0. El mayor t_j aislado da A_n A_(n+2)-A_(n+1)^2<0 eventualmente, con error O(n²rho^n). PSD de D_a exigiría los menores opuestos por diferencias finitas desde nodos positivos y los jets pares. No teorema externo Stieltjes ni argumento sobre ceros; sin tamaño evaluado ni campaña. Diferencia SHIFT: escala de densidad auxiliar, no exponentes de tests reales. Revisión root/casos/invariante. NO derivada theta refutada, NO W negativa, NO nueva T; permanece válido el Gram del modelo. No transferir monotonía matricial desde sus diagonales.


**Modelo hiperbólico, §10 — rigidez del prefactor fijo (PROVED, clase restringida).** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. Para Y_nu(b)=integral exp(-b cosh v)q(v)cosh(nu v)dv, q par C² positiva y q,q',q'' de crecimiento a lo sumo exponencial, la fuente de la ecuación en r=log(b/a) es F_nu=integral exp(-b cosh v)[-q''+2b sinh(v)q']cosh(nu v)dv. Si F_nu(b)=E(b)Y_nu(b) con E independiente de nu en sólo dos escalas distintas y un intervalo abierto de nu, unicidad de la transformada y evaluación en v=0 fuerzan q constante. La q real=Phi(v/2)exp(2pi cosh v) crece como exp(9v/4), por lo que esa transferencia escalar directa falla. Diferencia§7: admite prefactor temporal fijo, exige potencial independiente del parámetro. No excluye otros Green, gauges, sistemas ni prefactores dependientes de escala; Robin§8 no pertenece a esta clase. Revisión root/casos/invariante, dedup dirigido mapa; no W negativa, cierre global ni nueva T. Sin cómputos ni cambios en papers.


**Ampliación de la misma clase, modelo§10.1 (PROVED):** admitir Y_rr=A(b)Y_r+[b²+nu²+E(b)]Y, con A,E independientes de nu y el mismo prefactor fijo q, sólo permite q=C o q=C cosh(v/2). Restar dos escalas en la identidad inversa fuerza q=C cosh(v/2)^alpha; la independencia de1,cosh(v),sech²(v/2) fuerza alpha=0 o1. La q theta, de crecimiento exp(9v/4), no pertenece a esta clase. Incluye la imposibilidad de reparar esta familia mediante multiplicación escalar g(r) independiente de nu para obtener z_rr=[nu²+V(r)]z. No excluye otros cambios de variable, transformaciones integrales, prefactores dependientes de escala o sistemas. Diferencia explícita frente§10: ahora se permite primera derivada. Revisión root/casos y dedup mapa; sin signo nuevo ni modificaciones de papers.


**Precisión adicional de§10.1, sólo para q theta:** permitir Y_rr=A Y_r+[w(b)nu²+B]Y tampoco repara esta familia. Invertir la transformada cosh y usar q'/q=9/4+O(exp(-v)), q''/q=81/16+O(exp(-v)) fuerza w=1 por el término dominante (1-w)b²cosh²(v). Así queda excluida también una reparametrización C² de escala con derivada no nula acompañada de multiplicación escalar, ambas independientes de nu, que pretendan dar z_tt=[nu²+V(t)]z. Prueba en la misma§10.1, revisión root/casos y cotejo mapa. No clasificación para q arbitraria ni exclusión de otras familias/sistemas; sin nuevo signo.


**Precisión del puente temporal GramSlices§2.1 (PROVED, sin signo real nuevo):** bajo DOM gaussiana, A es PSD en toda R si y sólo si K_M es PSD para todos los tamaños con nodos en cualquier intervalo abierto positivo fijado. La recíproca usa continuidad de la forma en L²(exp(-Nt²)dt), densidad de exponenciales con exponentes CONTINUOS por unicidad de transformada entera, y aproximación de deltas. No afirma densidad de una escalera discreta bajo cota gaussiana ni suficiencia de un tamaño fijo. La nota existente POWER_GRAM_SLICES_OBSTRUCTION incorpora la prueba; revisión literal root/casos y dedup mapa. El Gram hiperbólico sí firma por ello su A temporal completo; no el real. Es precisión de representación, no atajo ni ampliación T.


**Corrección de alcance temporal, GramSlices§2.2 (PROVED, sin signo nuevo):** A_theta es conjuntamente holomorfo en |Im t|,|Im s|<pi/4 por dominación uniforme de su integral theta. PSD de TODOS los tamaños en cualquier intervalo temporal abierto implica PSD en toda R: diferencias finitas dan matrices mixtas de jets y puntos viejos; Taylor doble y simple conserva también los cruces al ampliar el intervalo, y se itera con radio fijo. Por ello A++ PSD no dejaría una obligación independiente de cruces; queda corregida esa cautela anterior. No se ha probado A++ ni basta orden finito. Fuente existente POWER_GRAM_SLICES_OBSTRUCTION§2.2, revisión root/casos y cotejo mapa; sin prioridad mundial ni nueva T.


**GramSlices§8 — modos theta individuales no PSD ni localmente (PROVED, clase restringida).** Phi_n(t)=n^(-1/2)h(t+log n), y el kernel modal A_n tiene límite diagonal al−infinito (2H/n)(m-log n)<0 para TODOS n>=1. El momento m<0 se prueba por dos recurrencias de integrales gamma y Jensen: m<(1/2)log(5/(4pi))<0. Holomorfía en strips y propagación§2.2 implican que A_n no es PSD de todos los tamaños en ningún intervalo abierto, incluso en la cola donde Phi_n es positiva. Diferencia frente a la traslación modal ya registrada103_47/48: falsificador global y alcance local, no sólo identidad. No refuta A_theta completo, que conserva pares cruzados n,m; no estima comparación relativa ni amplía T. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8, revisión root/casos y cotejo mapa, sin datos nuevos ni cambios en papers.


**GramSlices§8.1 — prefijos theta completos no PSD eventualmente (PROVED, cruces conservados).** Para Phi_M=sum_(n<=M)Phi_n, M^(-1/2)Phi_M(x-log M) converge en L²((1+|x|)dx) a F(x)=-pi exp(5x/2)exp(-pi exp(2x)). Suma Riemann y mayorantes uniformes Ce^(5x/2) a izquierda, Ce^(-x/2) a derecha. Luego integral tPhi_M²/(Mlog M)→-||F||²<0: todos los prefijos suficientemente grandes tienen diagonal negativa en su kernel A cerca de−infinito y, por continuación analítica, noPSD en ningún intervalo abierto. Diferencia§8: se incluyen TODOS los pares n,m<=M. No umbral numérico, no fallo de Atheta infinito ni exclusión de compensar la cola; sólo impide usar prefijos eventualmentePSD. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.1; revisión root/casos y dedup mapa, papers intactos.


**GramSlices§8.2 — primera corrección continua tampoco da aproximantes PSD (PROVED).** Q_M=Phi_M+pi M³exp(5t/2)exp(-pi M²exp(2t)) añade la cola modal integrada. Ahora Q_M→Phi en L²(1+|t|), pero integral tQ_M²=−||h||² logM/(4M)+O(1/M+logM/M^(3/2))<0 eventualmente. Trapecios de la cola aíslan h(t+logM)/(2sqrtM) con resto global controlado; se estiman también todos los cruces conPhi. La diagonal negativa y continuación analítica excluyen PSD local de todos los órdenes. Diferencia§8.1: aproximante corregido con convergencia global, no prefijo bruto. No refuta la positividad del límite ni otras correcciones. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.2; revisión root/casos y cotejo mapa, sin campaña ni cambios en papers.


**GramSlices§8.3 — simetrización corregida refutada para TODO M>=1 (PROVED).** S_M=(Q_M+Q_M reflejado)/2 elimina el momento impar, pero tiene masa>=C>0 y cola −[pi M(3M+1)/4]exp(-5|t|/2). Su transformada Z_M(u) tiende a−infinito al aproximarse u=5/2 desde abajo; valor medio antes del nivel positivo Z_M(0)/2 da Z_M>0,Z_M'<0. LT absolutamente justificada por cota exponencial bilateral produce un test cuadrático negativo ZZ'/u. Continuación analítica excluye PSD en cualquier intervalo. Cambio§8.2: paridad restaurada, falsificador distinto que conserva toda la forma; no se usan ceros. No refuta Phi real ni otras reparaciones. Fuente POWER_GRAM_SLICES_OBSTRUCTION§8.3; revisión root/casos y cotejo mapa, sin datos ni cambios en papers.


**Alcance de GramSlices§§8–8.3:** cualquier reparación que coincida con uno de los aproximantes excluidos en una semirrecta derecha conserva su matriz negativa local: A_psi=A_f allí por r>=0. Incluye reflexiones y suavizados sólo a izquierda, aun sin analiticidad depsi. Mantiene los alcances de índices de cada resultado; no excluye modificar la cola derecha ni firmaPhi. Consecuencia revisada root/casos, añadida a la misma fuente, sin nueva ruta.


**Fortalecimiento de GramSlices§8.1: TODO prefijo bruto, M>=1, fallaPSD.** Z_[Phi_M](u)=(u-1/2)H_M(u), H_M(u)=½pi^(-u/2-1/4)Gamma(u/2+5/4)sum_(n<=M)n^(-u-1/2)>0. Para u positivo cercano a1/2 por debajo, Z<0,Z'>0; LT da test negativo ZZ'/u. Convergencia absoluta sin paridad por |A|<=B(t)B(s), B(t)²=integral_t∞(1+x²)Phi_M². Continuación analítica da fallo local en todo intervalo. Sustituye el alcance eventual del descarte de prefijos brutos y sus reparaciones sólo a izquierda; mantiene intactos la asintótica de masa y el alcance eventual deQ_M. Revisión root/casos, sin datos ni signo real nuevo.


**GramSlices, extensión modal a cortes suaves infinitos (PROVED):** w_n>=0 nozero, sum w_n n²<infinito implica que A de phi_w=sum w_n Phi_n no es PSD en ningún intervalo abierto. Fubini y diferenciación dan Z=(u-1/2)C(u)sum w_n n^(-u-1/2), con factor restante positivo C¹; el test ZZ'/u es negativo inmediatamente a izquierda de1/2. Cotas en substrips y B justifican todo sin momentos adicionales. Incluye exp(-epsilon n²), no heat temporal ni w_n=1. Cambio frente al prefijo: soporte infinito suavizado, todos los cruces conservados. Fuente POWER_GRAM_SLICES_OBSTRUCTION, revisión root/casos y cotejo mapa; sin signo real nuevo ni papers modificados.


**Modelo hiperbólico, §11 — productos temporales de cosh excluidos (PROVED, clase exacta).** Fuente phase211: `POWER_HYPERBOLIC_MODEL_GRAM.md`. No existe Phi(t)=C exp(-a cosh(2t)) prod_j cosh(alpha_j t) con C,a>0, alpha_j>0 y sum alpha_j² finita, producto finito o numerable. La tasa fuerza a=2pi; log Q/t fuerza sum alpha_j=9/2. Infinitos factores anulan el coeficiente principal normalizado, incompatible con2pi². Para finitos, la primera corrección theta exige alpha_min=1 y multiplicidad entera k=pi-3/(2pi), entre2 y3: imposible. Diferencia§7/§10: multiplicación temporal exacta, sin hipótesis de ODE ni de preservación del signo. No excluye potencias reales de cosh, cocientes, sumas, otras aproximaciones ni comparación relativa; tampoco decide preservación abstracta por cosh. Revisión matemática root/casos y dedup dirigido mapa; sin cómputos, signo real nuevo, ampliaciónT ni cambios en papers.


**Núcleo temporal, §8.4 — momento exponencial cancelado y producto de Jacobi (PROVED, clase explícita).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para phi real no nula, continua, con caída exponencial a izquierda y superexponencial a derecha, integral exp(ct)phi=0 con c>0 excluye PSD de A_phi: la identidad LT absoluta daría (Z_phi²)' >=0 hasta Z_phi(c)²=0, contradiciendo unicidad Laplace. Con holomorfía conjunta de A,§2.2 excluye PSD en cualquier intervalo abierto. Aplicación: phi_P=(D²-1/4)[exp(t/2)P(exp(-pi exp(2t)))]/4 para TODO polinomio real no constante P; el momento c=1/2 se anula conservando los bordes. Incluye cortes J>=1 del producto Jacobi, con todos sus coeficientes firmados y cruces. Diferencia frente cortes positivos previos: no exige signo de phi ni de los pesos; usa cancelación exacta de un momento. No pasa al producto infinito/Phi completa, cuyo momento es positivo. Revisión matemática root/casos y cotejo dirigido mapa; identidad clásica citada DLMF20.5.3, no prioridad mundial, sin cómputos ni nuevaW/T.


**Núcleo temporal, §8.5 — Jacobi simetrizado, corolario de pares001 (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para todo J>=1, S_J=(phi_PJ+phi_PJ reflejada)/2 tiene cola POSITIVA D_J exp(-beta|t|), beta=2J+1/2, D_J=(8^J J!pi^J)(beta²-1/4)/8. En nodos beta-epsilon,beta-2epsilon, epsilon K converge a [[2,3/2],[3/2,1]]/(2beta), de determinante negativo. LT absoluta y continuación§2.2 excluyen PSD de A_SJ en cualquier intervalo. Se atribuye el criterio de pares aCONE001, no novedad general; aplicación diferente de§8.4(momento cancelado) y§8.3(cola negativa/diagonal negativa). No afirma S_J positivo en toda la recta ni refutaPhi; otras reparaciones y globalOPEN. Revisión root/casos y dedup dirigido mapa; sin cómputos ni nuevaT.


**Núcleo temporal, §2.3 — alcance de la factorización Hankel traslacional (PROVED; antecedente clásico).** `POWER_GRAM_SLICES_OBSTRUCTION.md`: A no admite integral_0^infinito<h(t+r),h(s+r)>dr, incluso con h medible de valores en un Hilbert e integrales diagonales finitas. La diferencia bajo traslación común sería PSD; su derivada fuerza(t+s)Phi(t)Phi(s) PSD, pero su menor2 es negativo. Antecedente: Blower, https://eprints.lancs.ac.uk/id/eprint/615/1/integrablepaper.pdf, Thm1.2 y§2.5(2.14); no novedad atribuida al mecanismo. Sólo esas variables y esa representación: no refuta PSD deA, otrosGram, otrascoordenadas ni la suma de productos Hankel. Revisión root/fresh_global, sin datos nuevos ni signo/T.


**Núcleo temporal, §8.6 — deformación modal n^(-delta), todo delta distinto de0 (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Para phi_delta=sum n^(-delta)Phi_n, la suma infinita y todos sus cruces se conservan. Z_delta=C(u)(u-1/2)sum n^(-u-1/2-delta), absolutamente para u>max(-5/2,1/2-delta). Delta>0: Z<0,Z'>0 justo a izquierda de1/2. Delta<0: al bajar u a c=1/2-delta desde arriba, Z~D/(u-c),Z'~-D/(u-c)²,D>0, por comparación elemental suma-integral. LT absoluta produce test negativo; holomorfía conjunta y§2.2 excluyen PSD de A_delta en cualquier intervalo. Diferencia frente cortes suaves: cubre amortiguaciones arbitrariamente débiles, antes sólo delta>3; no paridad ni cota gaussiana izquierda supuestas. Delta0 NOcubierto: Z_Phi(1/2)=1/4, mientras Z_delta(1/2)=0 para todo delta>0; distancia L1 con pesoexp(t/2)>=1/4 pese a convergencia compacta. Revisión root/casos y dedup dirigido mapa. No signo negativo dePhi/W, nuevaT, cómputos ni cambios en papers.


**Núcleo temporal, §7.1 — convolución gaussiana, equivalencia global por nodo remoto (PROVED).** Fuente phase211: `POWER_GRAM_SLICES_OBSTRUCTION.md`. Si K(u,R),K(R,R)->0, entonces K+b PSD en todos los bloques finitos equivale a K PSD para b>=0: añadir nodoR y coeficiente menos la suma de los originales elimina el rango uno y recupera cualquier valor negativo al hacerR->infinito. ParaPhi, cotas gaussianas para todoN y convexidad de logZ prueban M(R)/R->0. Convolucionar con gaussiana de varianza sigma² añade exactamente sigma² aK; así basta una prueba independiente para UN sigma fijo. Normalizar la densidad por exp(-sigma²/8) conserva Z(1/2)=1/4 sin cambiarK. Diferencia frente§7: recíproca, no nueva preservación; distinto de multiplicar la densidad por exp(lambda t²). NOsigno suavizado demostrado, NOequivalencia de tamaño fijo/rangoacotado, NOprohibición de usar esta reformulación constructivamente. Revisión root/casos y cotejo mapa; sin nuevos datos ni W/T.

### 2026-11-05 — Criterio logarítmico: falsificador cuártico de una inferencia general

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.1: PROVED, root/theta_joint, dedup mapa. Para phi=exp(-a t^4), a>0, A y todas sus capas son PSD (§4), pero log A no es condicionalmente positivo: el coeficiente t^5s^5 es (51/120)(4a)^5 kappa_5(V)<0 para V de densidad proporcional a exp(-2av²); quinta diferencia en seis nodos da falsificador. Alcance: PSD/capas positivas NO implican infinita divisibilidad del kernel normalizado. No refuta la Phi real. Un único bloque real de cinco nodos no dio falsificador numérico, sin certificado ni extrapolación. La condición logarítmica real sigue OPEN; no nueva positividad W/T. Diferencia frente CND de capas: se estudia logaritmo del integral completo. Papers intactos.

**Actualización CPD, 2026-11-06 (misma entrada).** GRAM§4.1, PROVED global_restart_checked/root; auditoría independiente arithmetic_fresh_candidate PASS y root PASS para ambos mecanismos. Para z=x+iy,x>=0, la identidad F²H=4D+L²+2xbL-Fb usa F=A(z,bar z)>0,b=|Phi(z)|²,L=integral_x^infinito|Phi|² y D=(F/2)min_(a complejo)integral_x^infinito v|Phi'-aPhi|²>=0. En x0, LARGE da L>=c epsilon^-4, la cota global F<=C epsilon^-5 y SMALL b<=C epsilon^-N exp(-a/epsilon): H>0 eventualmente. En x=h=log2/2, Poisson completo hasta3deriv da perfil C1 f=(1+2iu)^(-5/2),u∈[0,1], con min_beta integral|f'-beta f|²>=1/9375; la restricción local del mínimo paga Fb y prueba H>0 eventualmente sin aproximar Ftotal. Cotejo dirigido sin antecedente literal localizado. Pasan sólo esos dos tests diagonales complejos; CPD y signo global OPEN. Sin umbral numérico, asintótica local7/16 del H completo, nueva ruta, cobertura W/T, cómputos ni papers editados.

**Alcance de la extensión conjunta CPD (misma entrada).** GRAM§4.1, PROVED global_restart_checked/root, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Fijados z0,I,peso positivo, para f_eta(u)=Phi(z0+eta+u) y P_eta proyección al span{f0,f_eta}, R_ij=<(I-P_eta)f_i',(I-P_eta)f_j'> no domina c bb* con c>0 uniforme en eta, b_i=f_i(0): R_00<=||f0'-(f_eta-f0)/eta||²=O(|eta|²), pero |b0|²>0 fijo. eta=i tau mantiene las partes reales; resto C2 uniforme, sin exigir independencia. Sólo ese residual/borde y uniformidad: no excluye c(eta), renormalizaciones por separación, otros términos/bordes/proyecciones ni Gram general. S=A^(odot2)odot H PSD no implica H PSD. CPD/global OPEN; sin nueva ruta, W/T, cómputos ni papers.

**Promedio horizontal, alcance CPD (misma entrada).** GRAM§4.1, PROVED root/global_restart_checked/joint_sign_fresh_review, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Para B_y=integral_2^4[logt/(2t)]|Phi(.5logt+iy)|²dt y epsilon=cos2y, epsilon^(9/2)B_y->315(log2)²/(512sqrt2). Diagonal modal por Riemann gaussiana uniforme; cruces COMPLETOS por IBP <=Cepsilon^-4(1+log1/epsilon), término inferior y cross o(epsilon^-9/2). Luego A(iy,-iy)>=c epsilon^-9/2. El segmento[h,h+c0epsilon],h=.5log2,c0 fijo, aporta O(epsilon^-4), proporción O(sqrt epsilon)->0. Equivalente SÓLO de B_y; no de A total ni H, ni bandas arbitrarias. No nueva positividad matricial, CPD, W/T ni ruta; signo global OPEN, sin cómputos/papers.

### 2026-11-05 — Theta completa: fallo de log-supermodularidad temporal

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.2, PROVED root/theta_joint/casos, cotejo mapa. Para A temporal COMPLETO y s en cualquier compacto positivo, H=partial_t partial_s log A=-1/(t+s)²+O(exp(-2t))<0 cuando t crece. Prueba por v=pi exp(2t)(exp(2r)-1), expansión con restos diferenciados hasta orden2 y cola theta completa. Así A no es TP2 global; no puede cerrarse la vía por positividad puntual de H ni por features todas no negativas de H. Diferencia frente§5: integral completo, no capas; TP2 de073/112 pertenece a otros objetos. Alcance restringido: NO refuta PSD de H, CPD de log A ni PSD de A; menores rectangulares negativos no son menores principales. Sin signo W/T nuevo, papers intactos.

### 2026-11-05 — Modelos principales de cola indefinidos en todo intervalo

`POWER_GRAM_SLICES_OBSTRUCTION.md`§4.3, PROVED root/casos/theta_joint, dedup mapa. G0=(t+s)/(exp(2t)+exp(2s)) y H0=sech²(t−s)−1/(t+s)² no son PSD en TODOS los tamaños sobre ningún intervalo positivo, incluidas colas arbitrariamente lejanas. Corolario de continuación analítica§2.2: G0 llega a diagonal negativa t<0; H0 a H0(1/4,1/4)=-3. La expansión theta completa en t=L+x,s=L+y aproxima ambos modelos con error de entradas O(exp(-2L)), incluido control C² para log A, pero no transfiere su indefinición al kernel real. Se descarta usarlos como referencia PSD o mediante un sándwich multiplicativo simétrico. No se refuta A/H reales ni otras compensaciones; sin nueva W/T, papers intactos.

### 2026-11-05 — Cercanía relativa de densidades no conserva positividad

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.7, PROVED root/casos/theta_joint, cotejo mapa. Para cada epsilon>0 se construye psi positiva, par, holomorfa en el mismo strip que Phi, con sup|psi/Phi-1|<epsilon y psi/Phi→1 en ambas colas, cuyo A no es PSD en ningún intervalo. Reparación suave que coincide con Phi_M en cola hereda su bloque negativo; mollificar el ERROR RELATIVO por gaussiana produce analiticidad y conserva ese bloque por continuidad. La razón modal da epsilon_M<=4(M+1)^4 exp[-pi((M+1)²-1)]. Se conservan expansiones relativas exponenciales de todo orden fijo, no momentos exactos ni transseries aritméticas. Diferencia frente8.2/8.3: positividad/paridad/analyticidad y error relativo uniforme simultáneos. No es un contraejemplo a A_Phi; no garantiza ni excluye control en norma de formas o normas analíticas fuertes. Sin nueva W/T, datos numéricos ni cambios en papers.

### 2026-11-05 — Aproximantes analíticos negativos con momentos finitos exactos

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.8, PROVED root/casos, cotejo mapa. La construcción8.7 admite cualquier familia FINITA de pesos pares continuos independientes en(-1,1), integrables contraPhi: corregir momentos con bumps relativos compactos antes de mollificar y resolver el pequeño residual con los mismos bumps mollificados. Positividad/paridad/analyticidad, error relativo arbitrariamente pequeño y colas persisten, así como el bloque negativo fijado. Para pesos cosh(u_i t),t sinh(u_i t), conserva EXACTAMENTE cualquier colección finita de bloques K reales. La conclusión8.8 por sí sola no garantiza las familias infinitas de2/3/4generadores; ver8.9 para hasta4. No conserva estructura aritmética completa ni refutaPhi. Diferencia frente018/8.7: densidad real regular cercana y datos finitos exactos simultáneos. Sin nueva W/T ni papers editados.

### 2026-11-05 — Todos los cuatro generadores pueden coexistir con fallo global en aproximantes

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.9, PROVED preservador/root, revisión casos, dedup mapa. Existe delta_*>0 para el que ||psi/Phi-1||_20<delta_* conserva K_psi PD en TODOS los bloques de<=4 nodos distintos u>1/2. El bound Delta M^(k)=O(delta u^-8(1+logu)^4),k<=3, conserva los numeradores estrictos084/085; T>0 y las colas recuperan crecimiento/concavidad y los signos083 sin asumirBASE073 para psi. Los aproximantes8.8 entran en esa norma sin perder su bloque negativo, analiticidad, paridad, colas y momentos finitos exactos. Diferencia frente8.8: familia CONTINUA completa de orden4, no bloques concretos; controla confluencias y escape mediante criterios escalares. No preserva identidad aritmética theta; la extensión a todoslos13de053 se trata en8.10. NOrefutaPhi ni da nuevaW/T. Sin cómputos ni papers editados.

### 2026-11-05 — Control relativo por Cayley/Newton y estabilidad de trece tasas arbitrarias

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.10, PROVED root/preservador, revisión casos, dedup dirigido mapa. En el espacio de exponenciales por polinomios de dimensión<=13, A=-D es accretivo y Q=(A-a)/(A+a) contractivo. Interpolación Newton/Hermite de F(z)=Delta M(a(1+z)/(1-z)) da un bound de Delta K RELATIVO a la Gram de Cauchy, uniforme en colisiones/escape, sin asumir Delta M globalmente holomorfa. Error relativo de densidad en norma100 controla C12 de F. El margen053 de1/4000 conserva1/8000 para psi suficientemente cercana, todos13polos>=63/2, incluidos polos múltiples. Los aproximantes8.8 pueden conservar esto, TODOS4admisibles y datos finitos exactos, manteniendo fallo global en un bloque de másde13nodos altos. No preserva aritmética theta ni todaslasdimensiones; NOrefutaPhi ni amplíaW/T. Sin datos numéricos/papers.

### 2026-11-06 — Imposibilidad de un margen Cauchy uniforme en dimensión

`POWER_GRAM_SLICES_OBSTRUCTION.md`§8.11, PROVED root/casos/preservador, cotejo mapa. Para M real analítica positiva-variable con M(u)=O(u) en0, ningún K_M-c/(u+v), c>0, es PSD en todos los órdenes sobre ningún intervalo abierto positivo. Continuación analítica por jets hasta un punto pequeño contradice la diagonal M(u)/u-c/(2u). Aplica a Phi REAL y al modelo hiperbólico, sin suponer ni refutar K_M PSD. Impide extender el margen053 o8.10 a todos los órdenes mediante una constante positiva fija, incluso en tasas altas. No excluye no negatividad sin margen, comparaciones relativas distintas ni prueba global. Sin nuevos cálculos ni papers editados.


### Phase211 — covarianza divisorial agrupada (2026-11-06)

PROVED/revisado root-casos, cotejo dirigido mapa: `POWER_GLOBAL_ROUTE_REVIEW.md`, sección «Covarianza divisorial agrupada». Para C_s(n)=sum_(dm=n)mu(d)log(m)(gcd(d,m)^s-1), s>0, C_s(p²)=-(p^s-1)logp<0, mientras C_s(p²q²)=(q^s-1)(p^s-2)logp+(p^s-1)(q^s-2)logq>0 si p^s,q^s>2 (s=1/2: p5,q7). Se conserva toda la cancelación por producto n. Antecedente del factor:209 CONSTRUCTOR005; desintegración distinta:106114. FALSIFIED sólo signo uniforme de coeficientes del resto mixto, NO signo de la forma ni compensación conjunta con ARCH. No nueva W/T ni cambios en papers.


### Phase211 — resto divisorial indefinido en el portador primitivo (2026-11-06)

PROVED/revisado root-casos, dedup mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «El resto divisorial es indefinido». Se fortalece el resultado de coeficientes: R(F)=sum n^(-1/2)C_(1/2)(n)Re c_F(logn) toma ambos signos en tests reales pares C_c^infinito con ambos momentos polares cero, en una misma ventana T=3log4+1/100000. Trenes de bumps espaciados log4, coeficientes (1,-5/2,1) y (1,-3/2,-1/2,-1/2,-1/2,-3/2,1), dan respectivamente R/(kappa||g||²)=7/4 y -1/4, kappa=(sqrt2-1)log2. Todos los contactos quedan tratados por aislamiento exacto; no barrido. FALSIFIED sólo R>=0 o R<=0 universal como pieza aislada; compensación conjunta con ARCH/medias y signo de W siguen OPEN. No nueva W/T ni cambios en papers.


### Phase211 — comparador Robin ajustado, falsificador de dos nodos (2026-11-06)

PROVED/revisado root/casos/preservador, cotejo mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador Robin ajustado». Modelo positivo M_*=wb M_R(bu), w7/2,b2/7,a4pi/7,beta4pi²/49-33/392, coincide con M_Phi hasta u^-2 pero D=M_Phi-M_*=d/u³+O(u^-7/2), d>0. El resto K_D en nodos u,2u tiene det=-5d²/(64u⁸)+O(u^-17/2)<0 para u grande. FALSIFIED sólo esa comparación aditiva PSD; ambos kernels individuales no quedan refutados. Corolario de pares: D=o(1/u) y K_D PSD en una raya fuerzan D=0; no buscar comparador positivo noidéntico cancelando también1/u. Diagnóstico de origen NUMÉRICO no usado en prueba. No nuevaW/T ni cambios en papers.


### Phase211 — comparador asinh, menor negativo certificado (2026-11-06)

PROVED/asistido, root/preservador, auditoría colas-jets casos, dedup mapa. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparador asinh» y `tools/power_asinh_comparison_jet_verify.py`: M_0=.5asinh(u/(4pi)) tiene kernel PSD por integral positiva de resolventes, pero el residual N_D=(M_Phi-M_0)/u tiene menor de jets{5,6}, [[n10,n11],[n11,n12]], con det entre -1.684e-57 y -1.683e-57. Arb256,14momentos hasta26,16modos[0,3], colas totales<2^-645 cubiertas por2^-500; root reprodujo exit0. Sólo un menor prescrito, sin barrido. FALSIFIED comparación aditiva PSD, NO K_Phi ni comparación firmada general; jets no equivalen a sólo dos exponentes. Diagonales positivas no bastaban. No nuevaW/T ni cambios en papers.


### Phase211 — comparación hiperbólica original refutada (2026-11-06)

PROVED/asistido, root/preservador, revisión casos, dedup mapa. `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparación hiperbólica original»; `tools/power_hyperbolic_comparison_jet_verify.py`. Se cierra como FALSIFIED la comparación exacta antes OPEN K_Phi-K_(2pi) PSD. El menor residual de jets{5,6} tiene det entre -3.307e-59 y -3.306e-59, con28 half-moments completos hasta26, Arb256 y colas2^-500 por momento; root reprodujo exit0. No se transfiere el certificado asinh ni se exploran otros bloques. El modelo hiperbólico sigue PSD; K_Phi no queda refutado. Otras escalas, reponderaciones y compensaciones firmadas no decididas. No nuevaW/T ni cambios en papers.


### Phase211 — HCM recíproca no implica el signo del kernel (2026-11-06)

PROVED/root-theta_exacta-casos, dedup mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «HCM, reciprocidad y supercolas». f_epsilon(x)=C(1+x)^(-2)exp[-epsilon(x+x^-1)], epsilon=2^-100, es HCM por producto explícito, recíproca y tiene todos los momentos Mellin. La ley de logX es par/real-analítica con supercolas; su cuarto cumulante>0 por cotas racionales con corte32. Entonces detK(h,2h)=−kappa2·kappa4·h²/6+O(h⁴)<0. FALSIFIED sólo inferencia desde esas hipótesis; no Phi, no BPY general, no propiedad V''' >0 ni etiquetaGGC. El criterio de pares es conocido; nueva clase del falsificador cotejada contra003/074/101 yL93. No nuevaW/T ni cambios en papers.


### Phase211 — HCM de la densidad theta real refutada (2026-11-06)

PROVED/theta_exacta-root-casos, cotejo mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «La densidad theta en S=exp(2t) no es HCM». Para f(x)=Phi(.5logx)/(2xZ0), la paridad da f(1/x)=x²f(x). El producto HCM con a=1 tiene H(w)~(pi⁴/Z0²)w^(9/2)e^-2piw, w=v+1/v. CM exigiría logconvexidad; g=logH+2piw sería convexa, sublineal y tendente a+infinito, imposible. No se derivan restos. FALSIFIED HCM de esta densidad real y sus tilts/escalas positivos; no GGC ni K_Phi ni otros cambios de potencia. Se aplica el mecanismo ya conocido de tasa/prefactor a un objeto distinto de las mezclas§7.1; no reclamar principio nuevo. No nuevaW/T ni cambios en papers.


### Phase211 — los dos comparadores tampoco funcionan en el subespacio primitivo (2026-11-06)

PROVED/casos-root, auditoría matemática preservador y literal casos; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Comparaciones primitivas: transferencia analítica del descarte». Restricciones exactas sum d/(u-.5)=sum d/(u+.5)=0. Para D impar real-analítica global, L=(u²-.25)(v²-.25)K_D convierte esas restricciones en momentos0,1 nulos. Proyección contra dos anclas + continuación de GRAM_SLICES§2.2 propagan positividad condicional desde cualquier intervalo abierto; las filas nulas en±.5 permiten completar los momentos sin energía y fuerzan PSD completa. Los certificados asinh/hiperbólico previos excluyen así también ambas comparaciones PRIMITIVAS uniformes. Diferencia: dominio codim2 antes no decidido por los vectores completos; no nuevo principio de continuación. Test primitivo negativo existencial, sin coeficientes ni ventana; no son automáticamente los jets originales. No negatividad de K_Phi, no equivalencia de mínimos a T fijo, no nuevaW/T ni papers editados.


### Phase211 — clausura de productos cosh a escala hiperbólica fija (2026-11-06)

PROVED/root-casos, auditoría independiente preservador, cotejo dirigido mapa; `POWER_HYPERBOLIC_MODEL_GRAM.md`§11.4. No puede aproximarse Phi localuniformemente por C_n exp(-2pi cosh(2t)) productos finitos de cosh(alpha_nj t), alpha_nj>0, incluso variando cantidad y parámetros. Lema: todo límite positivo normalizado de esos productos es exp(gamma t²)prod cosh(alpha_jt), gamma>=0, sum alpha_j² finita; logQ_n(1) acota la masa cuadrática y Taylor controla uniformemente el residuo. Para el cociente theta, logQ(t)/t→9/2 fuerza gamma0 y contradice§11 exacto. Diferencia: se cierra una clase de aproximaciones antes no cubierta, no se repite mera exclusión de representación exacta. Sólo escala2pi fija, factores unitarios positivos y convergencia uniforme en compactos; no escalas variables, potencias reales, otras topologías ni comparación relativa. Sin cómputos, signo real nuevo, ampliaciónT ni cambios en papers.


### Phase211 — cierre matricial finito sin derivada primera excluido (2026-11-06)

PROVED/root-casos, auditoría independiente preservador; `POWER_HYPERBOLIC_MODEL_GRAM.md`§12. Para vector finito de prefactores fijos Q, pares C² de crecimiento exponencial, con Q1=q_theta, no puede cumplirse Y_rr=(b²+nu²)Y+E(b)Y en dos escalas distintas con E independiente de nu. FORCE y unicidad fuerzan sinh(v)Q'=BQ constante; w=logtanh(v/2) da Q_w=BQ y límite finito de todas las componentes en infinito, incompatible con q_theta~2pi²e^(9v/4). Diferencia§10: dimensión finita arbitraria y potencial matricial, no sólo escalar. Sólo esta clase SIN A(b)Y_r ni prefactores dependientes de b; no exclusión de sistemas generales, infinitos u otros Green. Sin cómputos, nuevaW/T ni cambios en papers.


### Phase211 — cierre matricial finito con primera derivada excluido (2026-11-06)

PROVED/root-casos-preservador, auditoría literal casos y cotejo dirigido mapa; `POWER_HYPERBOLIC_MODEL_GRAM.md`§12.1. No se localizó antecedente literal anterior; E101_070§5 sólo excluía cierre automático de banda finita, no este sistema con matrices arbitrarias. En la familia de prefactores fijos Q que contiene q_theta, tampoco puede cumplirse Y_rr=(b²+nu²)Y+A(b)Y_r+E(b)Y en dos escalas distintas, con matrices independientes de nu y dimensión finita. FORCE y unicidad obligan a Qtilde_x=R(x)Qtilde racional, x=exp(v). Dependencia de filas fuerza un anulador racional escalar de q_theta(logx); conjugación por pi*x^(5/4)*exp(pi/x) lo transporta a g=sum n²(2pi n²x-3)exp[-pi(n²-1)x]. Separar sucesivamente las tasas exponenciales prueba que cada polinomio modal del anulador es nulo; su coeficiente principal exige un polinomio no nulo anulado en infinitas tasas distintas, contradicción. Diferencia§12: ahora permite A(b)Y_r. Sólo prefactores fijos, dimensión finita y coeficiente de nu² identidad; no sistemas generales, prefactores dependientes de b, dimensión infinita ni otras representaciones. Sin cómputos, nueva positividad W/T ni cambios en papers.


### Phase211 — la normalización por Phi no da generador traslacional positivo (2026-11-06)

PROVED/root-casos, cotejo dirigido mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalizar por Phi». Para B=A/(Phi(t)Phi(s)), p=-Phi'/Phi, C=−(partial_t+partial_s)B=t+s−(p(t)+p(s))B. C00=0, pero partial_s C00=1−aB00>0, a=p'(0): si a<=0 es inmediato; si a>0,073 da Phi(r)²/Phi0²<exp(-ar²) y B00<1/a. Menor{0,s} negativo y continuidad dan nodos positivos; continuación analítica excluye PSD en cualquier intervalo abierto. Distinto del hazard§7 y del generador sin gauge§2.3. Sólo falla esta condición suficiente; no B/A/KPhi, otras normalizaciones ni signo global. Sin cómputos, nuevaW/T ni papers editados.


**Ampliación por paridad del generador normalizado (2026-11-06).** En «Normalizar por Phi» de GLOBAL_ROUTE_REVIEW, corolario root/casos con cotejo mapa: ningún g par positivo real-analítico hace PSD local a C_g=−Dcommon[A/(gg)]. Paridad conjunta hace C_g impar; continuación PSD obliga diagonales cero y C_g=0, es decir estacionariedad A/(gg)=F(t-s). La diagonal H(L,L)=1−1/(4L²)+O(e^-2L) de GRAM§4.3 no es constante y excluye esa excepción. Incluye la reparación que anula la fila0 eligiendo g'/g=−sPhi0Phi(s)/A(0,s). Sólo corolario de paridad, continuación y asíntota escalar previas; no nuevos cómputos ni extrapolación matricial. No cubre gauges no pares ni otros mecanismos; sin nuevaW/T ni papers editados.


### Phase211 — generador inclinado C1, diagnóstico inicial (2026-11-06)

**Actualización:** FALSIFIED para todo c finito por el argumento de cúspides modulares registrado abajo. El párrafo siguiente conserva el estado histórico del diagnóstico.

`POWER_GLOBAL_ROUTE_REVIEW.md`, «Generador con inclinación exponencial». Cotejo dirigido mapa sin antecedente literal localizado. g_c=Phi exp(ct) evita paridad; C_c=C0+2cB, B=A/(PhiPhi), y B=integral exp(-2cr)C_c trasladado para c>=1: PSD de C_c sería suficiente. Root/casos: cola negativa exige c>=1. En c1 su principal es el Gram Cauchy1/[pi(e2t+e2s)], sin control relativo de resto. Único jet{0,1} evaluado por preservador a50/80dps, theta16/[0,3]: determinante≈+0.00788625227439, sólo NUMÉRICO sin enclosure. No otros bloques/barrido. Estado histórico inicial: C1PSD todosórdenes OPEN. Estado vigente: **FALSIFIED para todo c finito**, incluido c=1, por «Cúspides modulares» en la misma fuente y la entrada de descarte posterior; no reintentar desde este diagnóstico positivo. No positividad W/T nueva. Diferencia real: normalización no par, fuera del descarte anterior; no suficiencia inferida del diagnóstico.


### Phase211 — cúspides modulares refutan todo C_c con c finito (2026-11-06)

PROVED/root-casos-preservador, cotejo dirigido mapa; `POWER_GLOBAL_ROUTE_REVIEW.md`, «Cúspides modulares». C_cPSD y reflexión exigirían B<=exp(2ch)B trasladado. La congruencia elimina denominadores y produce H_h PSD real, holomorfo en strip²; sus jets exigirían H_h(iy,-iy)>=0. Para h=.5log2, y→pi/4, epsilon=cos2y, Poisson alternado en w→i da |Phi(iy)|<=Cepsilon^-9/2 exp[-pi/(8epsilon)], mientras la cúspide par w→2i da |Phi(h+iy)|>=kappa epsilon^-5/2, uniformemente también en un segmento de longitudepsilon. Integrales horizontales positivas dan A0>=kappa epsilon^-4 y Ah<=Cepsilon^-5. Así H<=C_c epsilon^-14 exp[-pi/(4epsilon)]−kappa epsilon^-9<0 para cada c finito. C1 antes OPEN pasa a FALSIFIED; su jet numérico positivo no implicaba signo global. Serie theta completa, sin cómputos ni argumentos por ceros. Sólo excluye esta familia de generadores y su comparación traslacional, no A/B/KPhi ni otros Gram. No nueva positividad W/T ni papers editados.


### Phase211 — generador con normalización diagonal completa refutado (2026-11-06)

PROVED/root-relative_comparison_audit, auditoría matemática independiente arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup. Fuente `03-research/phase-211-sign-sandbox/POWER_GLOBAL_ROUTE_REVIEW.md`, «Normalización por la diagonal completa». Para d(t)=A(t,t), R=A/sqrt(d(t)d(s)), ningún C_c=2cR-DcommonR es PSD de todos los tamaños en un intervalo real abierto, para ningún c real finito. Cambia el gauge a sqrt(d)exp(ct), no cubierto automáticamente por el descarte Phi exp(ct). Para c>0, reflexión y suma dan R PSD y comparación traslacional; producto de Schur de la diferencia y la suma, seguido de congruencia, da H=exp(4ch)A_h²d(t)d(s)-A²d_h(t)d_h(s) PSD hipotético, holomorfo sin raíces. La identidad d'(z)=-2zPhi(z)² y Poisson prueban d(iy) acotada y d(h+iy)~-(9/16)(h+i*pi/4)(2i)^(3/2)zeta^(-4), zeta=exp(2z)-2i, h=log2/2. Con las cotas completas previas A0>=kappa*epsilon^(-4), Ah<=C*epsilon^(-5), resulta H(iy,-iy)<=C_c*epsilon^(-10)-kappa*epsilon^(-16)<0, contradicción con jets PSD. c<0 falla diagonal; c=0 obligaría R estacionario y H=0, misma contradicción. Antecedentes: descarte modular de gaugePhi, paridad sin tilt y CPD normalizada; diferencia nueva: comparación cuadrada y primitiva de la diagonal. No se refuta A/R/K_Phi ni otros gauges; test real negativo existencial, sin nodos explícitos. Sin numerica, nueva ventana T ni cambios en papers.


**Corolario del descarte de normalización diagonal (2026-11-06).** GLOBAL_ROUTE_REVIEW, corolario final: PROVED root/relative_comparison_audit, auditoría arithmetic_fresh_candidate PASS. También se excluye g_c=sqrt(A(t,t))*exp(ct)/F(t), F(t)=exp(t/2)theta(exp(2t)), para todo c real finito. La comparación traslacional INVERSA y su producto de Schur exigen PSD de J=exp(4ch)A²F(t)²F(s)²d_h(t)d_h(s)-A_h²F_h(t)²F_h(s)²d(t)d(s). Poisson alternante/par y las mismas cotas completas dan J(iy,-iy)<=C_c*epsilon^(-20)*exp(-b/epsilon)-kappa*epsilon^(-10)<0. c<=0 se trata por diagonales reflejadas/paridad. Dividir por F invierte qué comparación falla; es corolario del mecanismo, no nueva clase general de imposibilidad. Sólo ese gauge, no A/K_Phi, otros gauges ni signo global. Cotejo dirigido sin antecedente literal; sin cómputos ni cambios en papers.


### Phase211 — gauge asimétrico de escala theta: menor real negativo (2026-11-06)

PROVED/root-relative_comparison_audit, revisión arithmetic_fresh_candidate PASS, cotejo dirigido diagonal_gauge_dedup. Fuente GLOBAL_ROUTE_REVIEW, «Gauge asimétrico de escala theta». g(t)=exp(2pi sinh(2t)), q=4pi cosh(2t), cambia la clase frente a even-gauge por inclinación constante. El generador congruente C=(q(t)+q(s))A+(t+s)Phi(t)Phi(s) falla en nodos temporales (-L,L) para L grande. Y=pi exp(2L),P=Phi(L): expansión diagonal completa da C--/P²=O(L/Y), C++/P²=4L+O(L/Y), mientras restringir A(-L,L) a0<=r<=Y^-1/2 da Aop>=kappa P²/Y y C-+>=4kappa P². Así det/P4<=O(L²/Y)-16kappa²<0. No precisa cola del integral, cúspides ni cómputos. Antecedentes: GRAM§4.3 y fórmulas de nodos opuestos, no este gauge; no duplicado literal hallado. Sólo esta candidata, no todos gauges asimétricos, A ni W. Los dos nodos no son dos potencias. Sin ampliaciónT ni papers modificados.


**Extensión del gauge asimétrico a todos los parámetros (2026-11-06).** PROVED/root-relative_comparison_audit, auditoría arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup; fuente GLOBAL_ROUTE_REVIEW, extensión final. Ningún g_a(t)=exp(a sinh(2t)), a real finito, hace PSD al generador. Para z=-h+iy,h=log2/2,epsilon=cos2y, el generador congruente satisface C_a(z,barz)=4a cosh(2h)epsilon Ah-2h|Phi(h+iy)|². Si a>0, cotas completas previas dan <=C_a'*epsilon^(-4)-kappa*epsilon^(-5)<0, contra jets PSD; a<=0 falla ya por diagonales reales. Amplía el caso2pi sin barrer parámetros, mediante test complejo DIRECTO del generador. Sólo existencia de un test real finito para a general, no dos nodos explícitos. Aplicación de herramientas previas de cúspides, no método nuevo de positividad ni no-go de todos los gauges. No refuta A/K_Phi; sin cómputos, ampliaciónT ni cambios en papers.


### Phase211 — todos los pares temporales y de capas v son positivos (2026-11-06)

PROVED/root, auditoría arithmetic_fresh_candidate PASS, cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado. Fuente POWER_GRAM_SLICES_OBSTRUCTION§9. De073 V'''(x)>0 y paridad se obtiene xV''-V'=integral_0^x rV'''(r)dr>0, luego G(u)=V(sqrt u) es estrictamente convexa. En SLICE, a=sqrt(m²+v)+delta,b=sqrt(m²+v)-delta tienen a²+b²=t²+s²+2v y dispersión estrictamente mayor que (t²+v,s²+v) si v>0,t!=s. Convexidad da S_v(t,s)²<S_v(t,t)S_v(s,s): todos los bloques de dos nodos reales distintos son SPD para v>0, y también los de A al integrar. v0 es rango uno. Con§5, tres es el tamaño mínimo de un falsificador de una capa v real; NO implica fallo de A en tres. Diferencia: pares TEMPORALES por convexidad en cuadrados, no pares de potencias073 ni TP2 de112. Principio convexo clásico; consecuencia nueva en corpus cotejado, no prioridad mundial. Sin nueva cobertura W/T, cómputos ni papers modificados; global OPEN.


### Phase211 — compensación entre capas probada en triples simétricos (2026-11-06)

PROVED/root, auditoría matemática arithmetic_fresh_candidate, cotejo dirigido diagonal_gauge_dedup. Fuente POWER_GRAM_SLICES_OBSTRUCTION§10. Refinamiento del mismo resultado: A sobre(-R,0,R) es SPD para TODO R>=8. El sector antisimétrico tiene d-b>0 por§9; el simétrico tiene determinante d0(d+b)-2c²>0 por cotas explícitas. Con Y=pi exp(2R),P=Phi(R), B=supPhi=Phi0<450/499<1 (todos los modos), p(x)>=pi exp(2x) en x>=1 da c<=BP(R/Y+2/Y²); integrar hasta r=1/(4Y), usando p(R+r)<3Y, da d>RP²/(4Y). Además d0>81/2^24 por Phi>9/256 en[0,1/16]. Para R>=8, 2c²/d<9B²R/Y<=9R/Y<24/7^8<81/2^24<d0. En LOS MISMOS nodos, para TODO R>=8, las capas pequeñas son negativas sobre w=(1/P,-2/Phi0,1/P): para B_v=S_v/(PhiPhi), eta=(1,-2,1), eta^T B_v eta=-v Q_R+o(v)<0, pues Q_R=2p'(R)-6p(R)/R+4p'(0)>(8-12/R)Y-2-6/R+4p'(0)>0. El intervalo 0<v<v_R depende de R. La integral completa sobre ese vector es positiva, así la contribución posterior compensa estrictamente la pérdida inicial. Diferencia: realización probada de compensación para theta REAL, frente a mera posibilidad abstracta o falsificador de capas§5; R>=8 explicita ambos signos, sin uniformidad de v_R ni ruta nueva. Sin intervalo v uniforme; no triples de potencias080, R intermedios, todos los tamaños, inducción, signo global ni ampliaciónW/T. Sin cómputos ni papers modificados.


### Phase211 — Andréief emparejado: integrando negativo de orden tres (2026-11-06)

PROVED/positive_identity_attempt-root, auditoría arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup. Fuente POWER_GRAM_SLICES_OBSTRUCTION§11. Para f_i(r)=Phi(t_i+r),g_i(r)=(t_i+r)Phi(t_i+r), detA3=(1/6)integral S, S suma de ocho productos det[u_ej(rj)]det[u_(1-ej)(rj)]. En(r,r,r+h), la suma COMPLETA es -4det[g,f,f_h]det[g,f,g_h]. Taylor da principales hC p[x1,x2,x3] y hC(xp)[x1,x2,x3], C>0; p'' y(xp)'' son positivos en la cola theta completa. Así S<0 para h pequeño y, por continuidad conr>0, en una región abierta de r1<r2<r3. Diferencia frente capas crudas: ya se emparejaron todas las elecciones del determinante; fuentes086/089/099–112 usan otros objetos. Sólo se descarta signo puntual de este integrando estándar; NO detA<0, no otros emparejamientos ni compensación integrada. Sin nuevaW/T, cómputos ni papers modificados.


### Phase211 — cierre del criterio recíproco y triples temporales pequeños (2026-11-06)

PROVED con certificado intervalar, constructor positive_identity_attempt/root; auditoría matemática arithmetic_fresh_candidate PASS y cotejo dirigido diagonal_gauge_dedup sin prueba anterior localizada del cierre. Fuente POWER_GRAM_SLICES_OBSTRUCTION§12 y tools/power_temporal_reciprocal_compact_verify.py. Origen u=r² en[0,1/64]: a>0,a''<0 en256paneles; resto r en[1/8,1]: T=N Phi³>0 en8192paneles, Taylor24/cap28, Arb512,16modos más cola completa. Cauchy da resto<1e-30; mínimo certificado T>1.04e-17. Constructor y root FULL PASS, SHA256 498e199ae7bb52f7fedeef02847a1b8642a635b76bb036212259bc2f875e93fa. Junto a cola r>=1 y073, q(u)=r/V'(r) es estrictamente convexa globalmente y a>0. Identidad (HK-J²)/H²=Var(a+ua')+E[u²(2a'²-aa'')] prueba HK>J². Expansión auditada D/d0=R^4(K-J²/H)+O(R6) y pares§9 dan A sobre(-R,0,R) SPD para todo R>0 suficientemente pequeño. Diferencia: se cierra el compacto pendiente de§12; no nuevo criterio. No confundir con M=Z'/Z de086, triplespotencias080 ni triplesRgrande§10. Sin umbral pequeño explícito; R intermedio y todosórdenes OPEN, no ampliaciónW/T ni papers modificados.

Aclaración de alcance (§12.3): el falsificador074 tiene q''<0 en0<u<=1, por lo que no refuta suficiencia de la nueva hipótesis. La familia V=r²/2+r⁴/4+epsilon*r⁶/6,0<epsilon<=1, sí cumple qconvexa pero tiene capas negativas por§5; no se decide su integral A. No se obtuvo extensión a R arbitrario.


### Phase211 — límite global de la nueva convexidad recíproca (2026-11-06)

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§13; construcción arithmetic_fresh_candidate/root, revisión de estabilidad positive_identity_attempt. Se fortalece§8.7: h_M del corte relativo tiende0 en C6 ponderada porque los jets modales tienen bounds polinomiales por exp[-(n²-1)pi e/2]; mollificación conserva la pequeñez. La nueva condición§12 a>0,q''>0 es abierta bajo perturbaciones pares C6 pequeñas: en origen |delta a|<=delta,|delta a'|<=delta/6,|delta a''|<=delta/60; cola N>2r²Y² y error<=1290delta r²Y. También se conserva V'''>0. Elegir M primero y sigma después conserva el bloque negativo de§8.7. Existen así densidades pares positivas analíticas cercanas aPhi con nueva convexidad GLOBAL y HK>J², pero A noPSD en algún tamaño noespecificado. FALSIFIED sólo suficiencia de esas hipótesis genéricas; NOsignonegativoPhi, NOherenciaSchur refutada enTheta, NOcierre global ni nuevaW/T. Sin cómputos ni papers modificados.


### Phase211 — primitiva theta regularizada: menor temporal explícito negativo (2026-11-06)

PROVED/root, auditoría arithmetic_fresh_candidate PASS; cotejo dirigido sin antecedente temporal literal localizado. Fuente POWER_GLOBAL_ROUTE_REVIEW, «La primitiva regularizada tampoco es un núcleo temporal PSD». Para U=2cosh(t/2)-exp(t/2)theta(exp2t)=2g, monotonía modal y exp3>16 dan (4/5)exp(-t/2)<U(t)<exp(-t/2) para t>=0. Entonces A_U(8,8)<18exp(-8), A_U(0,0)<2 y A_U(8,0)>(32/5)exp(-4); menor(0,8)<-(124/25)exp(-8)<0. Diferencia: decide falta dePSD de la fuente auxiliar misma, no sólo indefinitud de la corrección K_g-K_Phi ya registrada. No refuta A_Phi ni excluye compensación adicional; sin nuevaW/T, cómputos ni cambios en papers.


### Phase211 — recíproco temporal: no representación Laplace positiva (2026-11-06)

PROVED/root-arithmetic_fresh_candidate; cotejo dirigido diagonal_gauge_dedup sin antecedente literal localizado. Fuente POWER_GRAM_SLICES_OBSTRUCTION§14. q(u)=sqrtu/V'(sqrtu) no se extiende holomórficamente a todoReu>0, por tanto no es integral exp(-us)dmu(s) conmu>=0. Si Qextendiera, Q(z²)Phi'+zPhi=0 en x>|y|,|y|<pi/4. En w=i(16+2/m)+delta,mimpar, Poisson y |Gauss_m|²=m dan Phi~Cdelta^(-5/2),Phi'/Phi~−5w0/delta. Así Q(z_m²)=0 en puntos distintos acumulados en (log4+i pi/4)², interiorReu>0: unicidadanalítica contradiceq>0. No uniformidad enm ni divisióninteriorporPhi'. Los39primerosórdenesderivados disponibles yorden0 tienen signosalternadosfavorables, pero no pruebanrepresentación. No confundir q conrecíprocoM086 niCMparamétrica111; no refuta convexidad§12 ni signoA_Phi. Sin nuevaW/T ni cambiosenpapers.


### Phase211 — falsificador elemental de triples simétricos bajo G convexa (2026-11-06)

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§15; constructor positive_identity_attempt, revisión root/arithmetic_fresh_candidate PASS, cotejo dirigido sin antecedente temporal literal. phi=exp(-r²/2-epsilon*r⁶/6),epsilon=1/1000 tiene G'>0,G''>0 para u>0 y V'''>0 para r>0. Con w=exp(-u-epsilon*u³/3),Z=intw, a=1+epsilon*u², identidad§12 da Delta=(HK-J²)/H²=-2epsilonEu²+epsilon²(15Eu⁴-9(Eu²)²). Exp(-x)>=1-x prueba I2>=49/25,I4<=24 y Delta<=-89/(25000Z)<0. Por expansión D(R)=2(HK-J²)R⁴+O(R⁶), bloque(-R,0,R) indefinido paraRpequeño, aunque todosparesSPD. q''(0)=-2epsilon: no cumplepropiedadtheta§12. No confundir conKpotencias074/080/101; no refutaPhi ni signoobjetivo. Sin datos numéricos, nuevaW/T ni papers modificados.


### Phase211 — principal aritmético del A completo en escalas enteras fijas (2026-11-06)

**Alcance adicional§16.5, misma entrada (PROVED).** Root/global_restart_checked, auditoría independiente arithmetic_fresh_candidate PASS y root PASS; cotejo dirigido sin antecedente literal localizado. Fijar PRIMERO y∈(0,pi/4) y DESPUÉS k->infinito,l=k+1. Cola theta completa uniforme en r>=0 y Laplace en el extremo dan Akl/(Phi_k conjugado(Phi_l))=(x_k+x_l)/[2pi(epsilon(k+l)+i sigma(k-l))](1+O_y(1/k)); de ahí |C_y(k,k+1)|->1 para C_y normalizado por la diagonal. Como rho(k,k+1)=0, el bloque rho es I2 y eigenmin C_y=1-|corr|->0. No existe c_y>0 con C_y>=c_y rho uniformemente en bloques enteros, aun dependiendo c_y de y; tampoco aproximación uniforme o(1) a rho (sup error>=1 para cada y). Sólo este comparador/normalización; no A negativo ni otros pesos/modelos. Sin régimen conjunto epsilon,k, nueva ruta, W/T, cómputos o papers; signo global OPEN.

Fuentes: [GRAM§16 y banda§4.1](../../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md), [phase209 CONSTRUCTOR_005](../../phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) y [AUDIT_005](../../phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED, fuente POWER_GRAM_SLICES_OBSTRUCTION§16; construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Cotejo dirigido sin antecedente literal localizado para este enlace con A; phase209 CONSTRUCTOR_005/AUDIT_005 son antecedentes del Gram aritmético, y GRAM§4.1 del promedio de banda. Para k,l enteros positivos FIJOS, z_k=.5logk+iy, epsilon=cos2y y L=log(1/epsilon), A(z_k,bar z_l)=[105/(512sqrt2)]rho(k,l)epsilon^(-9/2)L²+O_(k,l)(epsilon^(-9/2)L). Si k=d a²,l=d b² con igual parte libre de cuadrados, rho=gcd(a,b)/sqrt(ab); si no, rho=0. Resonancias exactas por Riemann gaussiana; casi resonancias, incluidas aproximaciones cuadráticas, por separación elemental de residuos y suma gaussiana S_delta<=C_(k,l)delta^-4log(2+1/delta), TODO delta>0. IBP diádica sobre TODO t>=1 da resto no resonante O_(k,l)(epsilon^-4L); términos inferiores pagan por cotas absolutas y Cauchy–Schwarz. La identidad gcd clásica con totientes prueba rho SPD para cada lista fija de enteros DISTINTOS; entonces su bloque COMPLEJO A es SPD eventualmente, con umbral dependiente de la lista. No nuevo Gram clásico ni identificación con norma209; no uniformidad en dimensión/enteros, ventana real, CPD/H, comparación relativa de todos los órdenes ni signo global. Sin cómputos, campañas, nuevaW/T ni papers modificados.


### Phase211 — SOS de todos los órdenes para la parte resonante exacta (2026-11-06)

**Alcance§17.8, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Para T=pi t^(5/4)(-2tD-3), A0=-D, R_s=(A0+s)^(-1) terminal, T^-1F=(1/(2pi))t^-3/2 integral_t^infinito u^-3/4 F(u)du. La forma física q=Re<TA0f,Tf>=(pi²/2)[7 integral t5/2|f'|²−(9/2)integral t1/2|f|²] es negativa para f=t^-3/4u(logt) con bump ancho. Elegir s>0 pequeño y v=T(A0+s)f da Re<T R_s T^-1v,v>=q+s||Tf||²<0. La fórmula integral de Rtilde_s es acotada en H_gamma EXPONENCIAL, norma<=2/gamma+4(s+3/2)/gamma²; densidad§17.7 transfiere la negatividad a un agregado theta finito real. Antecedentes phase199 E§3Rem3.1 y phase188 N_BUILD_007/018 tienen otros núcleos/órdenes/métricas; sin literal localizado. Sólo falla acretividad de todos estos resolventes físicos. El logaritmo contiene MENOS R_s: NO refuta positividad del log conjugado ni todo método de resolventes, balance conjunto con C o signo A. Sin nueva ruta, cómputos, W/T o papers.

**Alcance§17.6, misma entrada (PROVED).** Root/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS, incluido y0 por extensión directa del cálculo de extremo. Fijado y∈[0,pi/4), los pares k,k+1 tienen E_y y R_res diagonales. e_k=√k sum_n I_(kn²), r_k=√k sum_n[J_(kn²)+logk I_(kn²)]; r_k/e_k=logk+O_y(1/k) y Off_y(k,k)/e_k->0 exponencialmente. La correlación da |A_y(k,k+1)|/√e_ke_(k+1)=logk+o1. Coeficientes E-normalizados con cruce negativo producen Off_y[c]=-logk+o1, R_res[c]=logk+o1 y A_y[c]=o1. No existe C_y finito con Off_y>=-C_y E_y ni delta_y>0 con A_y>=delta_y R_res uniformemente. En y0, coeficientes reales(+,-) y A_y[c]>0 por§9; no A negativo ni decisión del bound crítico Off_y>=-R_res. Sin nueva ruta, W/T o papers.

**Atajo escalar§17.7, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Para y0 y F en span FINITO de Theta_k(t)=Phi(.5logkt), C=sum_(m>=2)Lambda(m)/√m T_m², T_m²F(t)=F(m²t), no existe M con |integral(CF)barF dt/(2t)|<=M integral(1+logt)|F|²dt/(2t). El operador C es continuo en H_gamma=L²(e^(gamma t)dt/t),0<gamma<2pi, y el span theta es denso allí por inversión Möbius de h(kt), inversa de L=-2tD-3 y aproximación C1 de polinomios en e^-pi t. Las mesetas1_[1,R] dan numerador>=cR^(1/8)logR y denominador=.5logR+.25log²R. Se extiende primero por densidad para R fijo y después R->infinito. Antecedentes explícitos phase199 PROOF_L_SHARP_C_001§4Prop4.2/E_001§3Rem3.1, BRIDGE002§3, AUDIT_L_SHARP_1§2.4 y019§§3–5; no nuevo principio de no acotación, sólo comprobación en este portador exacto y peso. No A negativo, bound no resonante por R_res ni transferencia/cierre global. Sin cómputos o papers.

**Refinamiento uniforme§17.5, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. D_q>=c_*I_q para todos d,q>=1 y 0<epsilon<=1, c_*=(log2/3)(4pi-3)²e^-6pi/[(4pi+3)²+(4pi-3)²e^-6pi]. Para dq>=2 sirve log(dq)Iq; para d=q=1, N!<=N^N2^-floor(N/2) da gap log2/3 cuando X>=2. Con X=sqrtu, el corchete de DIAG es>=log2/3 en u>=2 (en2<=u<4 la suma está vacía). Core[1,2]<=pi²sqrt2(4pi+3)² y tail[2,3]>=pi²sqrt2(4pi-3)²e^-6pi pagan una fracción uniforme de I1. Así R_res>=c_*E_y, E_y=sum_d sqrt(d)sum_q I_(dq²)|f_(d,q)|². Uniformidad sólo en esa energía divisorial exacta, con I dependientes de epsilon/índices; NO margen euclídeo uniforme, NO A completo ni off-frequency, W/T o cierre global. La eventual positividad del A COMPLETO entero sí se transfiere al real por§18; esta cota resonante sola no la prueba. Sin nueva ruta, cómputos ni papers.

Fuente: [GRAM§17](../../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). Antecedentes: [SIGNED_MEAN_019](../../phase-211-sign-sandbox/POWER_SIGNED_MEAN_019.md), [CONSTRUCTOR_005](../../phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) y [AUDIT_005](../../phase-209-nonlocal-kernel/AUDIT_005.md).

PROVED, construcción root/joint_sign_fresh_review, verificación independiente global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS, incluida SOS y positividad estricta. Cotejo all3/019/209 sin identidad literal localizada. R_res conserva TODOS los pares kn²=lm² del A exacto y su integral t>=1. Cada frecuencia puede ser indefinida: nodos1,4 y lambda4 dan det=-2(log2)²I_4²<0. Pero para cada grupo k=d a² y c_a finito, f_q=sum_(a|q)sqrt(a)c_a, I_q=I_(dq²), J_q=J_(dq²), la identidad exacta es R_res[c]/sqrt(d)=sum_q D_q|f_q|²+sum_q sum_(m|q,m>=2)Lambda(m)I_q|f_q-f_(q/m)|², D_q=J_q+(logd+logq)I_q-sum_(m>=2)Lambda(m)I_(qm)>0. El cambio u=lambda t convierte D_q en integral positiva: sum_(m<=X)Lambda(m)/m<2logX por la identidad factorial y floor(X/m)>=X/(2m). Sumabilidad absoluta gaussiana y f acotado justifican todo; el menor a con c_a!=0 prueba definitud estricta. Así R_res es PD en TODOS los órdenes sobre enteros positivos distintos k para CADA |y|<pi/4, incluido y0. Herramienta factorial clásica, sin inversión Möbius; se acoplan frecuencias distintas, no capas PSD ni Gram sustituto209. NO A completo, NO todos nodos reales, NO control no resonante, nueva W/T o cierre global. Actualización§18: para A COMPLETO, todos los bloques enteros y todos los nodos reales son equivalentes; no se transfiere R_res por separado. Sin campañas, datos numéricos ni papers.


### Phase211 — El A completo entero equivale al A sobre todos los nodos reales (2026-11-06)

Fuente: [GRAM§18](../../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED**, construcción independiente root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Consultados all3 y corpus, sin literal localizado. Definir P_kappa=kappa^(5/4)sum_n n²e^(-pi kappa n²t), T=pi t^(5/4)(-2tD-3), LgP=integral_0^infinito[e^-pi r P(t)-P(t+r)]dr/r y G=.5T LgP-C TP. Frullani y sum_(m|n)Lambda(m)=logn dan TP_kappa=Theta_kappa y G(P_kappa)=.5logkappa Theta_kappa. La forma A completa es integral[logt|F|²+2Re(GbarF)]dt/(2t). Para cada lista finita de escalas positivas se eligen a<pi min(1,kappa_min), gamma<2a; la norma B_a² controla simultáneamente(F,G) en H_gamma exponencial. Los targets tienen jets ponderados tendiendo a0: corte, aproximación C2 en e^-pi t e inversión Möbius absoluta e^-pi kt=k^-5/4 sum_n mu(n)/sqrt(n)P_kn² aproximan por escalas enteras en esa norma. NO se afirma densidad de compactos para todo B_a² ni se usa sólo densidad de F. Continuidad de la forma transfiere PSD de TODOS los bloques enteros a TODOS los nodos reales; la recíproca es restricción. Antecedentes BRIDGE002§3, CONFLUENT_BRIDGE014, SCALAR_BRIDGE017 y GRAM§17.7: herramientas de densidad previas, otras familias o norma sin este grafo completo. No nueva herramienta abstracta ni signo probado: R_res positivo solo no basta; el balance conjunto completo sigue OPEN. Se elimina únicamente la puerta adicional de transferencia del A COMPLETO, la equivalencia con el objetivo lambda_A(T)>=0 para TODOS T se verifica después en§18.9, sin identificar mínimos a T fijo. Sin cómputos, nueva W/T o cambios en papers.


**Alcance§18.5, misma entrada (PROVED).** Root/joint_sign_fresh_review, verificación global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. B=Lg-2sum_(m>=2)Lambda(m)m²D_(m²), p=P1, Bp=0, tiene tasas positivas antes de T sobre P=pf. Pero la cola integral de TU_rT^-1 induce en T Lg T^-1 el núcleo fuera de la diagonal K(t,v)=t^-1/4v^-3/4-t5/4v^-5/4/(v-t), respecto de dv. K>0 para2<v/t<3. TBT^-1=T LgT^-1-2C; elegir t0=2 y F>=0 no nula, soporte compacto en(9/2,11/2), da CF(2)=F(2)=0 y TBT^-1F(2)>0. Refuta únicamente la representación JF=integral[F(t)-F(v)]nu_t(dv)+V(t)F(t), nu_t>=0, incluso con killing local o posterior conjugación por Theta1 positiva. Soportes separados justifican intercambios absolutos sin renormalización diagonal ni pérdida de borde1. Antecedentes106_31, ROUND005D y L2_BUILD008 son otras formas/métricas, sin este T/K; cotejo dirigido sin literal. NO Q/A negativo, NO descarte general de Doob ni del método conjunto; signo completo OPEN. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Alcance§18.6, misma entrada (PROVED).** Root/global_restart_checked, auditoría arithmetic_fresh_candidate PASS y root PASS. Para A_ij(x,y)=integral_x^infinito(x_i+x_j+2s)Phi(x_i+s+iy)barPhi(x_j+s+iy)ds, Delta A_ij=4integral w_ij Phi_i'barPhi_j'-4P_ij(x,y), con borde inferior conservado. En diagonal x_i=0,y0,x>=1,088 da p=-Phi'/Phi>2Y-6>Y, Y=pi e2s. Así I=integral_x^infinito2s p²Phi²>Y(x)[xPhi(x)²+integralPhi²]>Phi(x)² y Delta A_ii>0. Falla superarmonicidad/armonía requerida por el principio mínimo directo desde el borde complejo§16. No se afirma fuente matricial indefinida: su signo conjunto no está probado. El umbral por bloque de§16 tampoco proporciona PSD conjunta en intervalo real abierto para§2.2. NO A/Q negativo ni descarte de toda PDE/transporte; signo global OPEN. Cotejo all3/16/2.2/088 sin literal resuelto; sin nueva ruta, archivos, cómputos, W/T o papers.


**Extensión§18.7, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Cada cola fija k>=K de los P_k aproxima los targets de§18 en B_a² y en el grafo(F,G): tras corte, P_c=x^KQ(x), x=e^-pi t; aproximación C² produce sólo exponenciales con k>=K y error C_K eta e^-pi Kt, y Möbius sólo introduce kn²>=K. Así PSD de TODOS los bloques de cualquier cola equivale al A real global. Para cualquier prefijo fijo c_1..c_J existen completaciones finitas con k>J que aproximan menosP_prefijo y hacen A_0[c]->0, sin suponer PSD. Si PSD, el ínfimo de esas completaciones es0. No puede existir A_0[c]>=delta|ell(c)|² con delta>0 y ell no nulo FINITAMENTE soportado. Tampoco minorantes diagonales no triviales con pesos TODOS NO NEGATIVOS, sobre c_k o los observables divisoriales finitodependientes f_(d,q) de§17; fijar el prefijo conserva un término positivo. Antecedentes DESCENT_AUDIT016§§8–9 (otra cola racional/W4), BRIDGE002§3 y18.3: instrumento previo, no este portador/grafo/conclusión. También excluye una identidad ÚNICA compatible A_0=sum_alpha w_alpha|ell_alpha|² con w_alpha>=0 y todos ell_alpha finitemente soportados, aunque sus tamaños crezcan: cada sumando sería un minorante prohibido. No excluye factorizar por separado cada bloque finito; FIXED_BLOCK_ASSEMBLY trata otra clase/kernel y tamaños uniformemente acotados. Scope y0; no A negativo, no descarte de energías sobre observables globales continuos/SOS no diagonales ni signo global. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Corolario§18.8, misma entrada (PROVED).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS. Para CADA sigma real fijo, ell_sigma(c)=integral_0^infinito e^(sigma u)sum_k c_kPhi(.5logk+u)du no admite A_0[c]>=delta|ell_sigma(c)|² con delta>0 sobre todos los soportes finitos. El momento es continuo H_gamma, por CS con integral_1^infinito t^(sigma-1)e^-gamma t finita;§18 transfiere el supuesto minorante a nodos reales. En x=-R, Axx=2integral_R^infinito sPhi² y ell_sigma(F_x)~Z_sigma e^(sigma R), F_x(t)=Phi(x+.5logt), Z_sigma=integral sobre TODA R de e^(sigma s)Phi(s)>0. La supercola hace el cociente tender a0 para todo sigma real. Antecedentes BRIDGE002/106_31/ROUND005D/106_36 y GRAM8.4 tienen continuidad, otras formas o densidad alterada/momento cancelado; cotejo all3/corpus sin literal. Sólo momentos exponenciales reales individuales: no complejos/test espectral, no momentos firmados generales ni A negativo; global OPEN. Sin nueva ruta, archivos, cómputos, W/T o papers.


**Alcance§18.9, misma entrada (PROVED, no signo).** Root/joint_sign_fresh_review/global_restart_checked; auditoría arithmetic_fresh_candidate PASS y root PASS; reglas del repositorio/all3 y definiciones primarias Paper47 cotejados. El objetivo lambda_A(T)>=0 para TODO T equivale a PSD completo K_(M_Phi), A real y todos los bloques enteros A, incluso cualquier cola fija. Recíproca nueva de alcance: cortar en infinito f(r)=sum d_i e^-u_i r, u_i>.5, con sum d/(u_i±.5)=0; dos bumps físicos fijos corrigen momentos con coeficientes→0 en H_eta014. No se exige f(0)=0: salto causal permitido en H^s,s<.5 y dominio log. Trasladar cada compacto a una ventana conserva Tate/W; hipótesis∀T firma K primitivo. El lema YA probado en GLOBAL Comparaciones primitivas con D=M_Phi impar real-analítica da K completo; suficiencia inversa BRIDGE002. En el grafo, ell_sigma(TP)=pi P(1)+pi(sigma/2-.25)integral t^(sigma/2+.25)P: Tate equivale a P(1)=0 e integralP=0, SIN P'(1)=0. No importar preimagen L2_BUILD008. Cada cola tiene rango2 de momentos: un bump P toca1, otro interior; dos vectores tail FIJOS con matriz invertible corrigen errores→0. Así18.7 conserva cualquier prefijo y A0→0 incluso para completaciones exactamente primitivas; sus no minorantes/SOSlocales sobreviven.18.8σ±.5 vacuo allí, otrosσsin inferir. NO equivalencia de mínimos a T fijo ni nuevo signo; global OPEN. Sin enunciados externos, archivos, cómputos, W/T o papers.


### Phase211 — Signo completo del primer polinomio primitivo en t=exp(2r) (2026-11-06)

Fuente: [GRAM§19](../../phase-211-sign-sandbox/POWER_GRAM_SLICES_OBSTRUCTION.md). **PROVED para el primer vector; ampliación bidimensional posterior en§19.9**, construcción fresh_global/root; auditoría arithmetic_fresh_candidate FULLPASS, root PASS y lectura literal independiente global_restart_checked PASS. Con p=P1=sum_n n²exp(-pi n²t), S_j=sum_n n^-j exp(-pi n²), a=1+(2/pi)S4/S2 y P=p(t)(t-1)(t-a), se tienen EXACTAMENTE P(1)=integral_1^infinitoP=0, por tanto ambos momentos Tate de F=TP nulos. Q(P)=Q_log+Q_B, Q_log>=0 y Q_B>1/1200-1/40000-1/4500-1/30000=199/360000>1/2000. La prueba retiene p exacto; principal(1,1) sólo como referencia con bound, corrección de a exacto, cruces(1,2)/(2,1) y TODO resto de la doble serie theta/prima con colas gaussianas explícitas y partición exhaustiva. No cuadratura/campaña ni truncación sin error. Cotejo all3/corpus101/195/199/209/211 sin familia literal localizada; antecedente E101_061 interpola nodos, las familias gamma/Laguerre previas son en otra variable. Instrumentos elementales, sin prioridad mundial. Esta prueba elemental firma ESTE primer vector primitivo; no hereda otros grados/cruces o recurrencia. La ampliación independiente§19.9 firma el plano E1,E2; grados posteriores, todos los órdenes, nueva ventana W/T y signo global permanecen abiertos. La propiedad de core suficiente se prueba por separado en§19.8 y no aporta esos signos. Papers intactos; sin archivos nuevos.


**Core suficiente§19.8, misma entrada (PROVED como alcance).** Construcciones independientes root/fresh_global, auditoría global_restart_checked PASS; cotejo all3/BRIDGE002§3/CONFLUENT_BRIDGE014/DESCENT_AUDIT016§§8–9/18 sin familia/core literal. En B_a²,a<pi, V=clausura span{pt^j}; H(z)=p e^zt tiene Taylor en norma con ||p e^(z0t)t^j/j!||<=C_(z0)(1+b)²b^-j, b=pi-a-Re z0>0. Diferencias finitas y discos solapados negativos dan p e^-nu t en V para todo nu>0 sin Hahn–Banach. C² en x=e^-t para Q=P_c/(px) aproxima compactos; corte sólo de targets con jets ponderados→0, NO todoB_a². Convergencia B_a² controla grafo(F,G)/Q. Corregir errores(P(1),integralP) mediante p,tp tiene determinante p(1)integral(t-1)p>0 y coeficientes→0. Primitivos son E_j=p(t)(t-1)q_j(t), j>=1, q_j ortogonales mónicos para w=(t-1)p; E1 es el vector firmado, grado2 de R. PSD de TODOS los Gram Gamma_ij=Q(E_i,E_j) equivale al objetivo lambda_A(T)>=0 para TODO T: físico fcompactprimitivo->F(t)=f(.5logt)->P=T^-1F compacto y primitivo, core+repair firmaW y dominio de cada ventana; recíproca TPpoly superdecay se corta∞ y corrige Tate en H_eta014 antes de pasar al límite. Se conserva borde causal/salto0 permitido, sin imponer P'(1)=0. No mínimos a T fijo ni nuevaW/T. El plano E1,E2 tiene signo PROVED por el certificado posterior§19.9; grados/cruces fuera de él y global siguen OPEN. El core no usa resultados numéricos; papers intactos.


**Bloque completo§19.9, misma entrada (PROVED asistido).** Diseño arithmetic_fresh_candidate/root, revisión matemática fresh_global/root, auditoría literal corregida fresh_global/root/global_restart_checked PASS; ejecuciones constructor y reproducción independiente root exit0/FULLPASS con SHA256 e589fb2b9d98d76f021418427a903794f17aa629832f400f2154c21add52f170. Para los dos primeros E1,E2 de§19.8, Gram COMPLETO real simétrico Q11>179/100000, Q22>17/10000, |Q12|<79/50000 y detQ>2733/5000000000: TODA combinación real no nula del plano es positiva. A la vez Q_B(E1+E2)<-1/20000; falla promover el signo separado Q_B(E1) a la familia, NO el signo completo Q. Parámetros exactos mediante momentos de w, encierro theta4modos+cola positiva; referencia de integral2modos pagada con TODAS las colas theta/primas, temporal y resto Cauchy deterministas. Verificador corregido usa192bits,960paneles[1,16],gradoTaylor40 y derivadas R/L algebraicas exactas, assertsorden41; inflación de errores ANTES gates. No cuadratura adaptativa/búsqueda ni corte sin error. Fuentes y proof en GRAM§19.9, tools/power_thermal_primitive_two_verify.py/.log. Sólo este bloque bidimensional: NO herencia siguiente grado, todos los órdenes, margen uniforme, nuevaW/T o signo global; core suficiente§19.8 permanece independiente. Papers intactos.


**Colas de grados§19.10, misma entrada (PROVED como alcance).** Root/joint_sign_fresh_review; auditorías joint_sign_fresh_review/arithmetic_fresh_candidate y root PASS. Para CADA J>=1 fijo, PSD de TODOS los bloques Gamma_(J..N), N>=J, equivale al objetivo lambda_A(T)>=0 para TODO T. Es aplicación del lema de GLOBAL Comparaciones primitivas a un número finito de restricciones: V=prod(u-sigma), d=Vb convierte sum d/(u-sigma)=0 en momentos polinomiales de grados0..m-1; anclas+continuación y filas nulas en sigma reparan mediante Vandermonde y entregan K completo. La cola térmica equivale exactamente a P(1)=0 e integral t^kP=0,0<=k<J, o momentos físicos Sigma_J={.5} union {2k-.5:0<=k<J}; sin P'(1)=0. El core19.8 repara J+1 errores mediante p y t^j(t-1)p: rango por borde p(1)>0 y Hankel positivo de w. Para exponentes físicos se corta PRIMERO en infinito y se reparan todos los momentos con bumps fijos en H_eta014; sólo después T^-1 produce un compacto al que aplicar el core. No se introduce la preimagen con cola de potencia en B_a². Antecedentes014/083/GLOBAL/18.9/19.8, no desigualdad positiva nueva ni no-go general. Ni el plano certificado E1,E2 firma una cola, ni se excluye firmar alguna; todos sus tamaños/cruces siguen OPEN. Sin uniformidad en J, mínimos a T fijo, nuevaW/T, cómputos o cambios en papers.


**Referencia primer modo§19.11, misma entrada (PROVED, aplicación de008).** Root/joint_sign_fresh_review; versión corta auditada por joint_sign_fresh_review/fresh_global/arithmetic_fresh_candidate y root. Para p0=exp(-pi t), la referencia Q0(R)=integral[logt|T(p0R)|²+Re(TLg(p0R)conjT(p0R))]dt/(2t) NO es PSD sobre polinomios reales con R(1)=0 e integral pR=0 EXACTOS. No se afirma que p0R sea primitivo en ambos momentos: las restricciones corresponden a pR. Prueba:008 da Arch[f]<=-4norm²+17normderiv²; tres bumps disjuntos igualmente ensanchados forman un espacio real negativo dimensión3. En sus preimágenes P=T^-1[f(.5logt)], dos restricciones P(1)=0 e integral rhoP=0,rho=p/p0, dejan vector no cero; la primera anula ell_+=piP1 y por sí sola el polar. A_P(P)=Arch+Polar<0. Corep0 en B_a² y reparación mediante p0,tp0, con det=e^-pi integral(t-1)p>0, producen un polinomio admisible yQ0<0 por continuidad. No grado ni coeficientes calculados. Aplicación del falsificador008 al dominio exacto, no nueva necesidad aritmética ni falsificador del Q completo/A/kernel theta truncado. Tampoco refuta toda perturbación o compensación entre modos; certificados19.7/19.9 intactos y global OPEN. Sin cómputos, archivos nuevos, nuevaW/T ni papers.


### Phase211 — Potencial del adjunto causal: signo interior negativo (2026-11-06)

**PROVED, prueba elemental con colas completas.** Fuente: POWER_GRAM_SLICES_OBSTRUCTION.md§19.12. Construcción joint_sign_fresh_review/root; auditoría arithmetic_fresh_candidate FULLPASS y root PASS de gates racionales. Consultados reglas del repositorio/all3/106_31/ROUND005D/18.5/GLOBAL: Picone/Doob y killing logarítmico tienen antecedentes; cambia el potencial del adjunto causal exacto en dt/(2t), no se afirma prioridad mundial ni lectura exhaustiva. Con Theta(t)=Phi(.5logt), J=TBT^-1 y r=.5logt, Bp=0 para todo t>0 y paridad de Phi dan forward Phi=2rPhi, backward Phi=-2rPhi. Su promedio completo anula Phi por esa álgebra física, SIN usar el argumento externo de106_31. Al restringir r>=0 queda g(r)=-integral_0^infinito k(r+s)Phi(s)ds, k(h)=2cosh(h/2)-exp(-h/2)/(1-exp(-2h))-sum Lambda(n)/sqrt(n)delta_logn. Adjunto débil causal J*Theta=2g-4rPhi, incluido borde1; el potencial de la identidad firmada de diferencias es V(f)=integral Phi(r)g(r)|f(exp(2r))|²dr. En log2 por DERECHA, la cola prima empieza n>=3. Aplus=pi p(1)>3/25; Gamma<=Aplus/(3sqrt2). Principal(n,m)=(3,1)<3645/56000; TODO resto, agrupado q=mn, <1024/249000 por cociente<1/250 y exp(25/2)>250000. Así P3<7/100 y g(log2+)<-19/300<-1/20. Gates Taylor racionales y colas detallados en§19.12; sin cuadratura ni truncación sin error. Continuidad derecha da un intervalo con Phi g<0. Tres bumps físicos disjuntos en ese intervalo y dos restricciones Tate dejan una combinación no nula EXACTAMENTE primitiva con V<0; su preimagen P es compacta, P(1)=integralP=0. Falla sólo exigir V>=0, incluso sobre esos perfiles primitivos. No Q/A negativo ni NO-GO universal de caminos/tres puntos; el término de diferencias puede compensarlo. Signo global OPEN; certificados19.7/19.9 intactos. Sin archivos nuevos, campañas, nuevaW/T ni papers.


**Dos fases exactas, GLOBAL (PROVED, alcance restringido).** Root/new_structural_sign; auditoría arithmetic_fresh_candidate PASS. Con perfiles COMPLETOS Psi_(k,theta)=sum_n n^-1/2 h_(kn²)exp(i kn²theta), la media en theta del A_theta ponderado exactamente por logt+.5log(kl) es R_res de GRAM§17. Para D=A0−Api, los nodos{1,2} dan D22=0 yD12>0 por positividad de h y del subagregado impar; detD_{1,2}=−D12²<0. Así fallan AMBOS órdenes PSD entre A0 yApi. No A0/Api negativos, otra mayoración, asintótico uniforme en fase ni signo global. Series y colas completas, sin numerica, archivos nuevos, W/T o papers.


### Phase211 — comparación hiperbólica pequeña: anulación necesaria (2026-11-06)

**PROVED como implicación / comparación OPEN.** GLOBAL, «Comparación hiperbólica pequeña: condición necesaria de anulación». Construcción fresh_global, auditoría new_structural_sign/root. Para H=-D²+(2pi)²exp(2r) Dirichlet, U_f=integral f(t)exp(2it sqrtH)dt, el Gram REAL 2||U_f||HS² reproduce K_h. ContinuidadH_eta, puente014 y traslación transfieren K_Phi>=epsilon K_h a compactos bilaterales reales. Cortes dePhi convergen en H1 con peso exp(eta|t|); la identidad física H_fullPhi=0 deGRAM19.12 fuerza U_Phi=0. Diferencia disponible: identidad física nueva, no principio nuevo de inclusión de radicales. Falta demostrar U_Phi!=0: NO contradicción, NO descarte de epsilon pequeño, NO signo global ni nuevaT. Para complejos se requieren ambas ramas; no aplicar014 directamenteaPhi bilateral. Sin cómputos ni cambios en papers.


### Phase211 — RES-SOS no identifica los canales de 106_38 (2026-11-06)

**PROVED, cotejo de objetos; no nuevo signo.** GLOBAL, «Alcance de RES-SOS frente a los restos de 106_38». Root/new_structural_sign, auditoría arithmetic_fresh_candidate PASS. En X_frac, x=y+log n y v=e2y dan productos h_(n²i²)(v)h_(j²)(v) con n no divide j: TODOS son no resonantes, y llevan un multiplicador de diferencias distinto del peso deGRAM17. X_ctr usa h_(i²)(v)h_(j²)(n²/v), escalas recíprocas. Bajo síntesis BILATERAL f_c=sum c_kPhi(x+.5log k), c=delta1 da g=f_c/Phi=1 y X_frac+X_ctr=0, pero R_res[c]>0; excluye sólo su identificación literal y un minorante positivo por R_res con esa síntesis. NO trasladar al A causal ni descartar comparaciones corregidas. Puente18 transporta A completo, no estos canales. La identidad física19.12 no resuelve la Poincaré antigua ni repone los términos omitidos en106_32. Sin cómputos, nuevaT o cambios en papers.


### Phase211 — cierre infinito simétrico sin deriva: rigidez de norma (2026-11-06)

**PROVED, clase fuerte explícita.** HYPERBOLIC§12.2; root, auditorías new_structural_sign/arithmetic_fresh_candidate PASS. Q C² en norma de un Hilbert, Q(v) en dominio común de B,C simétricos, sinh(v)Q'=BQ y Q''=CQ fuerzan ||Q(v)||²=A+c logcosh(v), A,c>=0. Prueba: w=logtanh(v/2), simetríaB=>K(w,z)=F(w+z), simetríaC=>sinh(s)F''+cosh(s)F'=0. Ninguna observación lineal continua puede ser q_theta~2pi²exp(9v/4). Dos FORCE fuertes -Q''+2b_i sinh(v)Q'=E_iQ con E_i simétricos en dominio común implican ese sistema. Diferencia§12: dimensión infinita y operadores no acotados, añadiendo simetría; no basta anterior argumento matricial finito. No requiere DomB² ni autoadjunción. Para deducir FORCE de una ODE integral se deben justificar dominios/intercambios, no son automáticos. NO exclusión de drift, métricas variables, observaciones no continuas, prefactores dependientes de escala u otros Green. Sin signo real nuevo, cómputos, ventanaT o cambios en papers.


### Phase211 — dimensión infinita con deriva escalar constante (2026-11-06)

**PROVED para la clase fuerte declarada.** HYPERBOLIC§12.3, root; auditorías new_structural_sign/arithmetic_fresh_candidate PASS y literal PASS. Q par C² en norma hasta0, dominio común de B,C simétricos, sinh(v)Q'+alpha cosh(v)Q=BQ y Q''=CQ fuerzan K(v,z)=A/2[cosh((v+z)/2)^(-2alpha)+cosh((v-z)/2)^(-2alpha)], A=||Q0||². SimetríaC da ecuación de ondas; simetríaB fija sus datos. Gram analítico prolonga Q a |ImZ|<pi/2 con norma²=A/2[cosh(ReZ)^(-2alpha)+cos(ImZ)^(-2alpha)]. Alpha>=0: norma real acotada contradice q_theta; alpha<0: norma acotada en ReZ=log2, ImZ->pi/2 contradice cúspide PAR e^Z->2i de theta completa. No usar cúspide alternante i. Diferencia12.2: primera derivada ESCALAR CONSTANTE 2alpha, cualquier signo, dimensión infinita, añadiendo paridad/Neumann0. Dos FORCE fuertes con E_i simétricos y esa deriva implican el sistema; no inferir FORCE desde integrales sin justificar dominios. No excluye deriva variable/operatorial, métricas variables u otros Green. Sin signo global, nuevaT, cómputos o papers editados.


### Phase211 — deriva escalar variable forzada a constante (2026-11-06)

**PROVED, clase fuerte explícita.** HYPERBOLIC§12.4; root, auditorías arithmetic_fresh_candidate y new_structural_sign PASS; literal PASS. Dos FORCE con b1!=b2>0, coeficientes escalares reales a1,a2 y E_i simétricos en dominio común fuerzan a1=a2 para Q C² no nulo, incluso en dimensión infinita. Gauge q=(sinh v)^alpha Q, w=logtanh(v/2), da GramF(w+z); simetríaC impone lado izquierdo sólo de s=w+z igual a beta F(s)/(sinhw sinhz). Variar w-z a s fijo fuerza beta=0; beta=b1b2(a1-a2)/(b2-b1). Con paridad C² hasta0 y observación continua theta, reduce a12.3 y falla. Extiende constante a variable escalar; no deriva operatorial. También excluye gauge multiplicativo escalar real C² no nulo en la misma coordenada y coeficiente espectral1, siempre que FORCE esté justificada. No inferir intercambios de operadores no acotados automáticamente. Sin signo global, nuevaT, cómputos o cambios en papers.


**Control de alcance de HYPER12.4, misma fecha.** Ejemplo algebraico new_structural_sign/root: Q=(1,2coshv), C=diag(0,1), D=diag(-4,-1), B=[[0,-2],[-2,0]] satisface sinhvQ'+coshvDQ=BQ yQ''=CQ con B,C,Dsimétricos y[B,D]!=0. No se extiende automáticamente el descarte escalar a drift operatorial. No contiene theta ni da Green positivo: gauge exp(-rD) produce offdiagonales -4bexp(±3r), perdiendo simetría usual. Otras métricas y sistemas generales no refutados. Sin nuevo signo o ventanaT.


**Reparación por métrica del ejemplo operatorial12.4 (2026-11-06, PROVED).** Root/new_structural_sign PASS. Formal symmetry local de L=-D_r²+2D D_r+b²I+E exige M'=-DM-MD y[E+D²,M]=0, luegoM=e^-rDM0e^-rD. Para el ejemplo2x2 ya registrado, M0V=V*M0 implica -4abexp3r+4dbexp(-3r)-16c=0; b=a0exp r y la independencia de exp4r,exp(-2r),1 fuerzan M0=0. No métrica matricial LOCAL positiva para ESEejemplo en ningún intervalo abierto. No otros sistemas, métricas no locales ni signo theta refutados. FuenteHYPER12.4, párrafo final; sin nuevaT o cómputos.


### Phase211 — tasas móviles: umbral fuerte exacto (2026-11-06)

**PROVED como aproximación, no signo.** CONFLUENT_BRIDGE014§6; root, auditorías new_structural_sign/arithmetic_fresh_candidate PASS. Para eta>1/2, u_N>eta,u_N->infinito y V_N=e^-uNy polynomialsgrado<N, aproximación de todoH_eta A LO LARGO deN iffN/u_N->infinito; densidad de la UNION iff limsupN/u_N=infinito. Distancia exponencialL²_eta=|(u_N-v)/(u_N+v-2eta)|^(2N), caso r0 de096. Paso fuerte nuevo: aproximar f' enL²_eta y antiderivar terminalmente, operador de norma<=1/eta que conserva MISMOgrado/bloque; sin pérdida logarítmica. No envolvente lineal. PSD de esos bloques completos, o lower -epsilon_N||f||² conepsilon_N->0 (criterio036), sería suficiente por continuidad014 ytraslación; hipótesis OPEN. THREE002u>=2^(40N) noentra; preservar margenfijo9 enregimendenso contradicecortesradicalfísico19.12, no contradice semidefinitud. Sin nuevaW/T, cómputos o papers editados.


**Alcance de la doble escala, aplicación de008 (2026-11-06).** BRIDGE014§6 final, root/arithmetic_fresh_candidate. Para u_N=N^(3/4), aproximar enH_1 el test primitivo008 y reparar ambos momentos con dos correctores del MISMO V_N. Se obtiene Polar0, AP[f_N]/||f_N||²<-3 y c_fN(log2)/||f_N||²>1/3 eventualmente, aunqueN/u_N²->0. No vale suprimir uniformemente ese contacto comoO(N/u²), ni declararPSD el principalAP. NoWnegativo ni descarte de un principal que conserve aritmética; aplicación del falsificador previo, no nueva positividad. SinT/cómputos/papers.


### Phase211 — corte primo creciente: error uniforme exp(-N) (2026-11-06)

**PROVED cola / signo retenido OPEN.** BRIDGE014§7, root/arithmetic_fresh_candidate/new_structural_sign PASS. ParaTODOSN>=1,u>=2 y f∈V_N(u), Q=ceil exp(40N/u) da |W−W_(<=Q)|<exp(-N)||f||². Aplicación deTHREE002tailnorm sqrt6·13^Nexp(-ut/2), válida antesdelumbralpositivo yporconfluencia: Lambda<=log, comparaciónintegralexacta dafactor Q^(-(u-1)/2)[2logQ/(u-1)+4/(u-1)²], menorfinal230Nexp(-7N)<exp(-N). SeconservanARCH/polar/contactosq<=Q ytodoscruces; no supresión deátomosbajos. Conu_N=N^.75,corteexp(40N^.25), faltaría loweruniforme -epsilon_N||f||²,epsilon_N->0, paraesebloqueretenido;014§6cerraríaentoncesglobal. NiPSDretendida ni nuevaT demostradas. Cortecreciente no contradice10632fixedcutoff. Sin cómputos/papers.


### Phase211 — corte móvil subcrítico: umbral necesario (2026-11-06)

**PROVED, principal truncado solamente.** CONFLUENT_BRIDGE014§8; fresh_sign_mechanism, auditoría new_structural_sign y root. Para u_N=N^(3/4), cualquier corte log Q_N<=(2-delta)N/u_N, delta>0 fijo, tiene un vector unitario explícito de dos coordenadas Laguerre con W_(<=Q_N)->-infinito. Cota: 2log u+32+4sqrt Q log Q+6/u-(2/u)exp((N-1)/u). Excluye cortes polinómicos para lower evanescente de TODO el bloque; tal lower exigiría liminf u_N log Q_N/N>=2. Diferencia respecto de antecedentes: corte creciente cuantificado;007 aporta bandas exactas,106_32 trata otro objeto (energía transformada con átomos eliminados). Frente al corte suficiente40 de014§7, fija orden exponencial necesario, no constante óptima. No primitividad, no negatividad de W completa, no signo del corte40 ni nuevaT; no extender a toda escala densa sin prueba.


### Phase211 — corte móvil insuficiente aun en primitivas (2026-11-06)

**PROVED para W truncada, no para W completa.** BRIDGE014§9; construcción fresh_sign_mechanism/root, auditoría matemática new_structural_sign PASS. Para u=N^(3/4),N>=2^60 y log Q<=2^(-12)N/u, un vector unitario explícito del MISMO V_N tiene ambos momentosTate0, f(0)=0 y W_(<=Q)[f]<-3. Coeficientes C(z)=(1-z)(z+r)(z+1/r)[sum_(j<M)(-z)^j]^4, M=floor(N/4),r=(u+.5)/(u-.5). Concentración elemental E tau²<=2^18(u/M)²; Arch<-3 y todos los contactos retenidos tienen correlación>=1/2, por lo que empeoran el déficit. Diferencia frente a008: ancho u/M en vez de u/sqrt(N), permite esta escala móvil y corte creciente explícito. No es simple aplicación del polar negativo de§8: aquí se anula exactamente. Descarta también cortes polinómicos en subespacios primitivos; NO transfiere umbral2, no negatividad fullW, no signo del corte40 ni nuevaT. Sin cómputos o cambios en papers.


### Phase211 — comparación hiperbólica pequeña refutada (2026-11-06)

**PROVED asistido, sustituye OPEN de esta comparación específica.** GLOBAL «Cierre de la comparación hiperbólica pequeña»: no existe epsilon>0 con K_Phi>=epsilon K_(2pi). La condición necesaria anterior exigía U_Phi=0, usando el radical físicoGRAM19.12 y el puente de forma. Nuevo input: Picone con r exp(-3r) y Rayleigh con r exp(-5r) sitúan omega_1=2sqrt(lambda_1(H)) en[17,41/2], H=-D²+(2pi)²exp(2r), Dirichlet0. La integral física G(omega)=integral_R Phi(t)cos(omega t)dt es <-10^-8 en TODA esa banda por certificado de bolas, colas completas y Bernstein; luego U_Phi v_1!=0. Constructor arithmetic_fresh_candidate, cotas/auditoría new_structural_sign, root y revisor reproducen FULL PASS/exit0. Script tools/power_hyperbolic_phi_cosine_band_verify.py enphase211, SHA cddcc0bf1c902be2fce90a12969dec3a43209c85a037d5156a916c9a74410ab6. Sólo theta explícita y espectro del MODELO, sin tablas de ceros. No signo negativo del objetivo, no exclusión de otros modelos, no nuevaT ni papers editados.


**Precisión primitiva del mismo cierre (2026-11-06).** GLOBAL aplica su lema anterior de continuación primitiva a D=M_Phi-epsilon M_(2pi). Para CADA epsilon>0 y CADA intervalo abierto no vacío I⊂(1/2,infinito), algún bloque finito de tasas en I con ambos momentosTate0 tiene energía residual negativa. Root/new_structural_sign PASS. Aplicación del lema existente, no nuevo mecanismo ni cómputo; no tamaño, coeficientes o ventana explícitos, no negatividad del núcleo objetivo.


**Familia física del mismo descarte, no nuevo mecanismo.** GLOBAL: g_R=(D²-1/4)(chi_R Phi) es compacto, par y exactamente primitivo; converge en H1 bilateral ponderada a f_*=(D²-1/4)Phi, radical físico. U_f*=-(4H+1/4)U_Phi tiene primer modo no nulo por el certificado ya registrado. Convergencia HS implica W[g_R]-2epsilon||U_gR||HS²<0 para cada epsilon>0 y R suficientemente grande. Root/new_structural_sign PASS; sin R numérico, sin W negativo demostrado, sin nuevos cálculos o papers.


### Phase211 — antecedente bibliográfico directo del kernel temporal (2026-11-06)

GRAM_SLICES§1 incorpora el manuscrito público de Dylan Suvlu (24Sep2026), «Theta correlations and a causal range criterion for the Weil form», §3eq18–23, https://dsuvlu.github.io/weil-form-operators/paper/theta-correlations-causal-range.pdf . Cotejo root/new_structural_sign: j=A/(integral Phi)² y misma respuesta logarítmica. Antecedente de representación, no signo global demostrado; no atribuir novedad a A por ausencia en búsquedas anteriores. No determina prioridad de RES-SOS17 ni del bloque19.9. Borrador, sin afirmación de revisión por pares o auditoría completa; no nueva construcción ni cómputos.


**Compañero causal del mismo antecedente:** GLOBAL registra lectura de SuvluIII§2. La contracción con peso no da L² ordinario; su majorante separado diverge al bajar r a1/2 ya por c_Gamma. No se afirma divergencia del feedback real ni fracaso de toda vía causal. RES-SOS y bloques finitos no aportan aquí una cota de la inversa. Cotejo root/arithmetic_fresh_candidate; no nuevo teorema de signo ni cómputos.


### Phase211 — ramificación BPY examinada, preservación OPEN

GLOBAL registra la candidata T'=W_1^-2 T_1+W_2^-2 T_2 y simetrización recíproca. No es truncación theta. Semilla S delta_(pi/3) tiene Gram explícito; un solo bloque de jets del primer paso fue positivo NUMÉRICAMENTE, sin certificado ni extrapolación. Simetrizar después conserva el límite bajo las hipótesis de convergencia/media fija; simetrizar dentro cambia la dinámica y su convergencia no está probada. El paso conserva una entropía con factor firmado y un borde firmado de integración por partes; no se obtuvo preservación PSD ni contraejemplo. No nueva vía validada ni campaña de grados. Cotejo root/independent_sign_reset; fuente y fórmulas en GLOBAL, sin papers editados.


**Precisión del alcance de la ramificación (2026-11-06).** GLOBAL prueba que S B no factoriza universalmente a través de S: S delta_4=S delta_(1/4), pero las salidas tienen distinta regularidad en t=5. Densidad y salto de derivada exactos; auditoría independiente new_structural_sign PASS. No refuta preservación PSD ni la órbita de media pi/3; las dos entradas tienen medias distintas. Concreción de pérdida de información, no nuevo avance del signo. Extensión auditada independent_sign_reset/root/new_structural_sign: GLOBAL proporciona dos leyes finitas positivas de media pi/3, misma S y salidas S B distintas, mediante una perturbación recíproca antisimétrica de seis átomos y cocientes de saltos de densidad. Tampoco basta añadir la media como dato. No se prueba PSD de esas entradas ni se refuta preservación PSD o la órbita específica; extensión rutinaria del alcance.


**Diagnóstico escalar de ramificación (2026-11-06).** GLOBAL contiene prueba asistida y código inline reproducido de kappa4 del tilt logarítmico de S B delta_c<-1/5000 para todo c>0. Se reduce a k+4ds-2d^4 y a dos cotas de momentos de V=A1+A2. Construcción independent_sign_reset, auditoría algebraica new_structural_sign y reproducción integral root FULL PASS. Este falsificador necesario no funciona; NO se prueba PSD ni preservación. Sin campaña de órdenes ni nueva ventanaT.


**Ramificación: alcance del condicionamiento (2026-11-06).** GLOBAL conserva identidad exacta K=media de congruencias condicionales+C, con C igual al negativo de dos covarianzas normalizadas. Para la entrada real mu=B delta_(pi/3), C(u,u)=−Var(h)u²/2+O(u⁴), Var(h)>0 por continuidad y soporte pleno. Así C noPSD ya en el segundo paso real. Constructor independent_sign_reset, root y auditoría new_structural_sign PASS. Sólo falla pagar ESTA corrección como positiva; no K negativo ni exclusión de compensación conjunta. Sin cómputos ni avance de ventanaT.


**Fuente externa de ventana log11 (CITED/UNVERIFIED, 2026-11-06).** GLOBAL registra rStation45v1 y cotejo de normalización root/new_structural_sign. La afirmación externa cubriría la restricción primitiva deP47 hasta log(11)/2 si se valida; construcción intervalar no reproducida, suplemento ya localizado por API pública; pasan comprobaciones cortas de hashes, matrices pequeñas y Green, sin regeneración400. No nueva frontera local certificada ni cierre global. Papers intactos.


**2026-11-06 — rStation45/log11, actualización parcial auditada.** Sector PAR hasta T=log(11)/2: **PROVED con asistencia computacional, reproducción local de resultado externo**. Cadena completa regenerada (safe/graph/contract/family/checker); checker exit0, complemento393 con Hmin>0 y siete pivotes del núcleo>0. Root y new_structural_sign reprodujeron la eliminación intervalar del núcleo; auditor independiente confirmó seis fuentes idénticas al suplemento, metadatos, enlaces entre archivos y logs. Archivo final SHA25618a3a25b3bacb3e265bee09232bdd09b17ea88074c9619bf6d9be069c4654cb3; último pivote [5.173121145006658e-50 +/-3.29e-66], NO cota de gap espectral. Diferencia con pivotes históricos compatible con distinta congruencia/orden de eliminación; no se requiere identidad bit a bit. **Sector IMPAR todavía pendiente de reproducción; ventana de la forma COMPLETA local permanece1.035; signo global OPEN.** Resultado externo, no novedad propia. Evidencia y procedencia en POWER_GLOBAL_ROUTE_REVIEW.md, sección fuente externa log11, y /tmp/riemann-rstation45-audit/work. No se modifican papers.


**2026-11-06 — log11 COMPLETO: reproducción local auditada.** Sustituye el estado parcial anterior: **PROVED con asistencia computacional, resultado EXTERNO reproducido** para la forma completa W_T en ambas paridades, 0<T<=log(11)/2 (aprox.1.1989476364). Fuente: https://rstation.ai/problems/riemann_hypothesis/papers/45 . Todas las etapas de regeneración terminaron exit0; root y new_structural_sign comprobaron logs, fuentes idénticas al suplemento, metadatos, vínculos de los archivos y reeliminación intervalar de ambos núcleos. Impar: complemento394 con Hmin=[0.0072415100579310717783150120757660513853081885959734786213576 +/-4.96e-62]>0, seis pivotes positivos, último revalidado [2.92609807122468755690e-45 +/-8.74e-66]. SHA final impar7211d28ec770386db511be3942e20ecd4056d2b5cc95501e7fd5a4802ae548ce. Archivo final par y su auditoría constan arriba. La auditoría analítica previa conserva el complemento infinito y coincide con la normalización P47; la restricción primitiva hereda positividad. La frontera local verificada de la forma completa se actualiza de1.035 a log(11)/2. NO se deduce un margen espectral de los pivotes. NO es resultado original nuestro ni prueba para todoT: signo global OPEN. Evidencia persistida en phase-211-sign-sandbox/tools/rstation45_reproduction/ (logs, fuentes, dos resultados finales, auditor pequeño y hashes); las matrices intermedias permanecen en /tmp/riemann-rstation45-audit/work. Papers intactos. No se lanza otra campaña de ventanas: falta una estimación estructural uniforme del bloque Schur completo, no sólo positividad de sus sumandos favorables.


**2026-11-06 — Resta de cortes, auditoría sin signo nuevo.** GLOBAL, «Resta de dos cortes suaves»: w1−w2 elimina el sumando común y da continuo primitivo, pero abarca todo W compacto tras traslación; el principal conserva oneprofile y el resto cruzado carece de cota firmada nueva. Consecuencia de ROUND_001_A/REVIEW_002 y P211-A; revisión root/arithmetic_fresh_candidate/corpus_global_gap. No NO-GO general, nueva ventana ni cambios en papers. Global OPEN.


**2026-11-06 — Candidata PF infinito aditivo + reciprocidad (puente OPEN).** GLOBAL, «Densidad BPY»: q(v)=sum n²(2pi n²v−3)e^(−pi n²v), 2pi q tiene Laplace prod(1+s/(pi n²))^(−2). Convolución de exponenciales dobles y límite uniforme prueban TP aditiva de todos los órdenes; q(1/v)=v^(5/2)q(v). Son propiedades clásicas del dato, no signo nuevo de A. El contramodelo HCM ajustado a esa reciprocidad tiene (log q_e)''(1)=3/4−2epsilon>0 y falla PF2: diferencia de clase comprobada. Falta firmar el kernel integral con q(av)q(bv) y log(abv²); TP aditiva no autoriza esa composición multiplicativa. No se afirma suficiencia, prioridad o cierre. Root/new_structural_sign y auditoría arithmetic_fresh_candidate PASS de identidades y alcance; cotejo selectivo L23/L93/corpus. Sin cómputos ni papers; global OPEN.


**PF aditivo + reciprocidad: alcance adicional, sin signo global.** GLOBAL desarrolla la consecuencia h''<=0 y h(1/x)=beta logx+h(x) ⇒ −(log Phi)''>=2beta=5, ya compatible con la convexidad theta conocida. Una Gamma(2,rate4), PF infinito pero NO recíproca, tiene integral t Phi²<0 por Jensen (media9/16), y su A tiene diagonal negativa. Excluye sólo transferir automáticamente signo desde convoluciones exponenciales; no refuta el paquete conjunto ni sus aproximaciones particulares. Cálculo root/new_structural_sign, sin cómputos. Puente multiplicativo OPEN; papers intactos.


**PF/reciprocidad — aproximantes finitos simetrizados, alcance específico.** GLOBAL: densidad f_N de2Nexponenciales tiene f_N(v)~C_Nv^(2N−1) en0. Su perfil simetrizado tiene cola positiva exp[−(4N+1/2)|t|], por lo que GRAM§8.5 ya implica A noPSD. Además la densidad recíproca ftilde_N tiene cola v^−(2N+3/2) y (log ftilde_N)''>0 eventual: falla PF2. No contraejemplo al paquete completo; f_N→2pi q y perfil normalizado usa factor1/2, no pi. Resultado específico sin cómputos/papers; puente global OPEN.


**2026-11-06 — Rigidez de modificaciones FINITAS de tasas BPY (PROVED en clase).** GLOBAL: mantener exactamente dos tasas pi y modificar finitas otras tasas, todas>pi, da L_f=R racional·L_0. Si además f(1/t)=t^(5/2)f(t), la cola (At+B)e^−pi t y su recíproca fuerzan R=r0+r1/sqrt(s)+r1/(2sqrt(pi)s)+error exponencial; racionalidad implica r1=0,Rconstante=1. Construcción root, auditoría arithmetic_fresh_candidate PASS; sin antecedente literal en cotejo selectivo. No unicidad PF infinito general ni signo de A; modificaciones infinitas/cambio del mínimo fuera de alcance. Sin cómputos/papers; global OPEN.


**2026-11-06 — Renovación aditiva BPY, alcance acotado.** GLOBAL: vf(v)=∫_0^v k(v−u)f(u)du, k=2sumexp(−pi n²x), produce transición descendente; reciprocidad produce ascendente. Su mezcla equiprobable no admite densidad reversible: el cociclo R(L,2L)R(2L,3L)/R(L,3L)~1/sqrt(2L), no1. Construcción global_sign_independent_reset, revisión root; diferencia respecto renovación divisorialE101.089, cotejo dirigido all3/corpus. No se identificó su energía con A: NO signo negativo de A ni cierre del paquete, no exclusión de otros pesos/no reversibilidad. Sin cómputos/papers; global OPEN.


**2026-11-06 — Renovación plegada: identidad exacta y capas indefinidas.** GLOBAL construye xf(x)=∫_1∞f(u)h_u(x)du y A=∫∫f(u)f(w)S_ab^(u,w)dudw, con h_u=k(x−u)+sqrt(u)k(x−1/u) en sus soportes exactos. Fubini absoluto conserva todo el peso logarítmico. Para u>w>1,a=u+delta, Sdiag→S0>0, S1=−C/sqrt(delta)+O1, S12=O(delta^−1/2), luego jetdet=−C²/delta+O(delta^−1/2)<0. Hay capas con menor negativo en cada intervalo real abierto de escalas>1. No signo negativo de A, ni conclusión para nodos enteros, ni exclusión de compensación/agrupamiento. Construcción global_sign_independent_reset/root, doble revisión PASS. Sin cómputos/papers; global OPEN.


**Renovación BPY, una fuente integrada (corolario específico).** GLOBAL: integrar completamente w deja C_ab(u) con g(x)=xf(x). Diagonales positivas para a>=1, pero cerca a=u+delta el jetdet es −u f(u)²(logu)²/(256delta)+O(delta^−1/2)<0. Por tanto tampoco son PSD estas capas individuales; falla en nodos reales próximos>1, no se decide enteros ni A completo. Construcción global_sign_independent_reset, revisión root; aplicación del mecanismo anterior, no nuevo criterio general. Sin cómputos/papers; global OPEN.


**2026-11-06 — Autodescomposición BPY y límite de la órbita de escalas (alcance PROVED; signo OPEN).** POWER_GLOBAL_ROUTE_REVIEW, «Autodescomposición BPY»: L(s)/L(cs)=prod[c+(1−c)lambda/(lambda+s)]² construye el semigrupo de saltos con densidad invariante f y energía positiva auxiliar, rho=−k'. Su estacionariedad reproduce la renovación, sin identificar la energía con A. El semigrupo común NO preserva las dilataciones: si cdX+Y_c fuese bX, la media fija b=1+c(d−1), pero la diferencia de varianzas es −2sigma²c(1−c)(d−1), no nula para d distinto de1. Inversión cambia f dx a x^(1/2)f dx. No descarta otros transportes ni decide A. Objeto distinto de la falsa identificación arquimediana/difusión de phase64/154; herramienta clásica sin prioridad. Construcción root/new_structural_sign y revisión arithmetic_fresh_candidate PASS; cotejo dirigido corpus/all3. Sin web, cómputos numéricos o papers.


**2026-11-06 — RES-SOS: no hay cota SUPERIOR uniforme del resto (corolario, y=0).** GLOBAL, «presupuesto resonante»: para N fijo y k>N², k,...,k+N−1 tienen distintas partes libres de cuadrados; R_res es diagonal. El extremo theta completo de GRAM16.5/17.6 da R^(-1/2) A R^(-1/2)->J_N y Off normalizado->J_N−I_N. Coeficientes r_i^(-1/2) dan Off/R->N−1. Hacer crecer N después de ese límite excluye Off<=C R y |Off|<=C R para todo C finito, y por tanto una norma uniforme de H=−R^(-1/2)Off R^(-1/2). NO excluye H<=I ni decide Off>=−R o A. Mismo mecanismo de bloques cercanos, con presupuesto RES-SOS exacto; no nuevo principio ni signo. Root y auditoría arithmetic_fresh_candidate PASS; cotejo all3/corpus global_arithmetic_restart. Sin web, cómputos numéricos o papers.


**2026-11-06 — Extensión factorial antes de resonancia, restos firmados (identidad PROVED; signo global OPEN).** GLOBAL, «Extensión factorial»: con b_lambda=sum_(n²|lambda)n^-1/2 c_(lambda/n²), Gram completo K, proyección P_m sobre m²|lambda y traslado R_m, Q=sum Lambda||P_mb−R_mb||_K²+b*Db+E. D integra h_lambda h_mu contra log(t sqrt(lambda mu))−loggcd(q_lambda,q_mu)−S(sqrt t); E=−2Re sum Lambda(R_mb)*K(I−P_m)b. El factorial firma TODAS entradasD, pero D noPSD porque H−D>=0 y la referenciaH sinpeine tiene test negativo por GRAM19.11/18.3. E(delta1)<0. Inversión Möbius truncada y colas gaussianas transfieren ambos fallos separados a c finito. No Q/A negativo ni descarte de compensación conjunta. Diferencia con RES-SOS: se conservan cruces de frecuencias distintas; no nueva herramienta factorial/Gram. Constructor global_concrete_reset, root y auditoría new_structural_sign PASS; cotejo dirigido all3. Sin web, cómputos numéricos o papers.


**Corolario de la extensión factorial, 2026-11-06:** c=delta1 da b_(n²)=n^-1/2 y P_m b=R_m b para todos m. Por tanto S_sq=0, mientras E=−2sum Lambda(P_mb)*K(I−P_m)b<0 (ya m2, índices4/1). Ningún C finito permite E>=−C S_sq. Q[delta1]=A(0,0)>0: D paga ese E, sin signo global inferido. Corolario directo de la identidad anterior, no nuevo mecanismo; root y auditoría new_structural_sign PASS. GLOBAL conserva prueba y alcance. Sin web, cómputos o papers.


**Núcleo de S_sq, corolario algebraico (2026-11-06).** En la extensión factorialGLOBAL, para c finito, S_sq=0 iff c está soportado en enteros libres de cuadrados. b_(dq²)=c_d/sqrt q prueba un sentido; inyectividad del GramK por T y unicidad exponencial, recurrencias en cada primo e inversión Möbius prueban el otro. En esa familia Q=D+E; no PSD ni densidad inferidas. Root y auditoría new_structural_sign PASS, cotejo dirigido all3. Sin web, cómputos o papers.


**2026-11-06 — Balance factorial SF: B+M noPSD (test exacto).** GLOBAL: en el núcleo libre de cuadrados, suma de loggcd ponderada por K coincide con B=Gram_S(sqrt t), y D+E=Q=L+M; factorial firma0<=B<=L. La cota suficiente B+M>=0 falla en{1,2},c=(1,−1/100): cotas completas theta dan T11<1e−6,T22<1e−2,T12>1e−4, luego c*Tc<0. L−B>=0 no se elimina de Q y el bloque completo sigue positivo; no signo global. Constructor global_concrete_reset, root y auditoría new_structural_sign PASS; cotejo all3, sin nueva herramienta factorial ni campaña. Sin web, cómputos numéricos o papers.


**2026-11-06 — Densidad SF en grafo y ausencia de margen fijo L−B.** GLOBAL: P_z holomorfaB_a², ||P_z||<=C(1+|z|)^13/4 enRe z>=delta>a/pi. Funcional anulador dividido por(z+1)^4 esacotado; Schwarz con factores finitos yΣSF1/d=infinito fuerzaanulaciónidentica. Hahn–Banach+GRAM18.3/18.7 prueban aproximación de compactos por cualquier colaSF conservando grafo. Con g_R=(D²−1/4)(chi_RPhi), Wg_R->0,normaL²->positiva; trasladar a r>=1 y usar w=logt−S√t>=log2/3 implica que Q>=epsilon(L−B) esfalso∀epsilon>0, tambiénSF. Equivale a excluir B+M+alpha(L−B)PSD∀alpha<1 fijo. No Qneg, nosemidefinitudprobada, nomárgenesvariablesdescartados. Construcción root/global_concrete_reset y auditoría new_structural_sign PASS; cotejo dirigido all3, herramientasclásicas, sinweb/cómputos/papers.


**2026-11-06 — Resto conjunto factorial noPSD; no margen por S_sq.** GLOBAL: aproximarP4 enB_a² porP(cn) con cnSFfinito, y tomar e_n=delta4−cn. Q[e_n]->0, pero J anulaSF y por tanto S_sq[e_n]=S_sq[delta4]=s0>0. Luego(D+E)[e_n]->−s0: restoCONJUNTOnoPSD y ningúnε>0 permiteQ>=εS_sq. S_sq no continua enB_a², aunqueQ sí. Diferencia respecto18.7: observableinfinito deidentidadfactorial, usandodensidadSF. Root y auditoría new_structural_sign PASS. NoQneg ni descarteglobal decompensaciones; sinweb/cómputos/papers.


**2026-11-06 — Resolventes escalares del producto: capas noPSD.** GLOBAL: J_u=integral Phi(r+x)Phi(r+y)[(1+u)^−1−(exp(2r+x+y)+u)^−1]dr, A=integral J_u du conFubiniabsoluto. Paridad da diagonal límite negativa∀0<=u<1; GRAM2.2 excluye PSD deJ_u sobre cualquierintervalorealabierto. DensidadSF aplicada alPAR(P_z,z^-1/2P_z), noPsola, transfiereJ0neg a cSFfinito; continuidadconservamismotest para0<=u<eta. NoAneg ni falloSF∀u<1 afirmado. Objeto distinto deTR_sT^-1 de17.8; falta compensaciónintegrada. Constructor global_signed_balance, root y auditoría new_structural_sign PASS; cotejoall3, sinweb/cómputos/papers.


**Parejas recíprocas de resolventes, candidata OPEN (2026-11-06).** GLOBAL: C_u=J_u+u^-2J1/u, A=integral_0¹C_u du; peso h_u(z)=(z²−1)/[(z+u)(uz+1)] imparbajoinversión. h0=z−1/z,h1=(z−1)/(z+1), integral0¹|h_u(z)|du=|logz|. ParidadPhi da diagonalesC_u(x,x)>0∀xreal,u∈[0,1], eliminando falsificadorindividual. NO PSDallorders ni signoA; faltacotadecruces. Diferencia: emparejarantesdeestimar, no capasindividuales. Root/global_signed_balance y auditoría new_structural_sign PASS deidentidades, cotejoall3; sinweb/cómputos/papers.


**2026-11-06 — Pareja extrema C_0 PSD en TODOS los órdenes reales (PROVED auxiliar).** GLOBAL: C0=integral2sinh(2r+x+y)Phi(r+x)Phi(r+y)dr tiene DOMgaussiano. Transformada=(Z(a+1)Z(b+1)−Z(a−1)Z(b−1))/(a+b). Z(a)=xi(a+.5)/2; S=2pi(s−1)zeta(s)/[(s+1)(s+2)zeta(s+2)],s=a−.5. InversaEulerabsoluta yEuler–Maclaurin construyenS holomorfa, crecimiento polinomial; paridad da|S(it)|1, boundEuler paraRea>=32 y máximoenstrip dan|S|<=1. KernelSchurPSD porHardy/Parseval, congruencia y recíprocaDOM deGRAM2.1 firmanC0 temporal todosnodos. Constructor global_signed_balance, root y auditoría new_structural_sign PASS, cotejodirigidoall3/phase16sinliteral, sinprioridadmundialafirmada. NO C_u interior niAglobal: extremo u0demedidacero. Sinweb,cómputos,papers.


**2026-11-06 — Dos transportes de C_0 descartados en clases precisas (PROVED).** GLOBAL, «Dos transportes desde C_0»: q_u(w)=1/(1+u²+2u cosh w) tiene log estrictamente cóncavo, por lo que q_u(x+y+2r) falla PSD ya en menores2; no es multiplicador Schur positivo. Además NO existe minorante C_u>=integral C_0(x+t,y+t)dmu(t) con mu positiva fija no nula, 0<u<=1: diagonales pares D_u/D_0<=u^(-1)e^(-2|x|)->0, mientras cualquier masa compacta de mu impone cociente positivo en uno de los extremos por monotonía D_0. Incluye imposibilidad de igualdad. Nueva hipótesis de trabajo: C_0 completo ya firmado todos órdenes; distinto del Hankel puntual GRAM2.3. Constructor global_signed_balance, new_structural_sign y root PASS; cotejo dirigido all3. No refuta C_u/A ni transportes con otros perfiles/gauges. Sin web, cómputos o papers; signo global OPEN.


**2026-11-06 — B_1 PSD todos órdenes NO implica B_0 PSD: contramodelo suave (PROVED).** GLOBAL, «El extremo hiperbólico positivo»: B_b tiene peso sinh(b(2r+x+y))/b, B_0 lineal. Perfil phi=3g+(g(·−2)+g(·+2))/2, g normal estándar, Z=exp(a²/2)(3+cosh2a). Inversa geométrica explícita y diferencia de módulos prueban S_1=Z(a−1)/Z(a+1) contractivo; Schur/DOM firma B_1 todos órdenes. Pero K_M, M=Z'/Z, en nodos Laplace(log2/2,log2), vector(42,−41), da1−516/(34log2)<0: B_0 temporal noPSD (no se identifican esos nodos con test temporal2). Antecedente CONE001§4; diferencia gaussianizar y verificar también B_1PSD. Constructor global_concrete_reset, auditoría new_structural_sign y root PASS. Excluye transporte universal bajo paridad/positividad/suavidad/DOMgauss; NO dato theta ni sus hipótesis adicionales/supercolas. Descenso theta OPEN, sin web/cómputos/papers.


**2026-11-07 — Reciprocidad unitaria no hace contractivos los factores BPY (PROVED, clase precisa).** GLOBAL, «PF aditivo e inversión»: R_beta h=x^(−beta)h(1/x), beta=5/2, fija q y es unitario en L²(x^(beta−1)dx). Pero V_lambda=lambda(D+lambda)^(-1) causal NO es contractivo para NINGUNA lambda>0: h_R=h(x/R), v_R=h_R'+lambda h_R, da diferencia de normas R^(alpha−1)[lambda alpha R B−A]>0, alpha=3/2, A,B positivos explícitos. Antecedente VIRTUAL_SOURCE_017§§1–4 cambia métrica; nuevo cálculo sobre factores exponenciales BPY completos en métrica recíproca. new_structural_sign/root y auditoría PASS. Sólo impide esa composición de contracciones; no descarta producto completo/otras compensaciones ni PF+reciprocidad. Cotejo adicional: derivadas del producto devuelven renovación registrada; inversión del kernel aditivo devuelve cambio Möbius ya examinado. Sin nueva cota conjunta ni signo A, sin web/cómputos/papers.


**2026-11-07 — Convolución BPY COMPLETA no acotada en métrica recíproca (PROVED).** GLOBAL, «El producto BPY completo»: H=L²(x^(3/2)dx), T_f causal, f=2pi q. h_epsilon=epsilon^(−5/4)h(x/epsilon), h>=0 compacto(1,2) normalizado, tiene norma1 y ||T_fh_epsilon||>=c epsilon^(−1/4), usando min_[1/2,2]f>0. Cada salida está en H; no existe extensión acotada. Control separado lejos0: h_R=h(x/R) da defecto de contractividad alpha m R^alpha B+O(R^(alpha−1))>0 por Taylor y momento exponencial BPY. Diferencia: evalúa producto completo, no infiere desde sus factores. Root/new_structural_sign PASS; cotejo all3. T_fq!=q (LaplaceL²!=L); normalización por filas cambia operador, kernel k devuelve renovación anterior. Sólo descarta este mecanismo normativo, NO A/PF+reciprocidad. Sin web/cómputos/papers.


**2026-11-07 — Diagnóstico único de C_1, sin falsificador (NUMÉRICO, no certificado).** GLOBAL: bloque de pareja recíproca C_1 en nodos(−1,−1/2,0,1/2,1), fórmula par integrada con tanh(v); primer autovalor normalizado aproximado0.01323704, todos positivos en cálculo double truncado. Fórmula auditada new_structural_sign, cotejo all3: no confundir con antiguo generador gauge C_1. NO certificado ni avance de signo global; sin barrido adicional. Parejas C_u y A siguen OPEN; papers intactos.


**2026-11-07 — Restricción explícita de deriva operatorial (PROVED en clase regular).** HYPERBOLIC§12.5. Q par C4, Q''=CQ, sinh(v)Q'+cosh(v)DQ=BQ, B,C,D simétricos en dominio común y DQ continuo: K=.5[F(v+z)+F(v−z)] fuerza L=<DQv,Qz>=.5[G(v+z)+G(v−z)], G=−coth(t/2)F'(t), G0=−2F''0. Luego Lvv=Lzz; L no se presupone PSD. Con dominios DC/CD y diferenciación en grafoD adicionales sólo se deduce conmutador débil nulo contra spanQ; NO conmutación fuerte. Diferencia§12.4: resuelve kernel operatorial, no reducción escalar. Root/paired_kernel_fresh y auditoría new_structural_sign PASS, cotejoall3. No realización theta, Green ni signoA; escapeoperatorial OPEN. Sin web/cómputos/papers.


**2026-11-07 — Proceso físico SIN PLEGAR tampoco monótono en orden usual (PROVED).** GLOBAL, «Conservar ambas ramas»: para A_markov=−L de106.41, tasa superior Q_x(z), z<log2 próximo, Q'_0/c=−integral_z∞g'K+sum a_nK'(logn)<=g(z)Kz+a2K'(log2)<0. Cada modo theta enlog2 da derivadalog<−19; límiteupper<K(log2)/sqrt2[4/3−19log2]<0. Umbral sin cruces y colas completas justifican derivación/suavización; dos estados ordenados violan condición necesaria de monotonía. Diferencia106.115: recta completa y defecto continuo de tasas, NO salto plegado de reflexión. Root/new_structural_sign PASS, cotejoall3 y10641/42/115. Sólo orden usualR, no otrosconos ni signoA. Sinweb/cómputos/papers.


**2026-11-07 — Semigrupo físico no preserva convexidad PAR (PROVED).** GLOBAL, «El semigrupo físico tampoco conserva las funciones pares convexas». Test suave de bisagra(|x|−R)+, R↑log2, plano cerca0: (A_markov f)''0/(2c) tiene Gamma<K0, cola entera n>=3<K0, contacto2<−38K0/3. Cotas modales p_j''<=y²p_j y series geométricas controlan todos modos/contactos, sin cómputos. Mollificación par positiva deja contactos en región lineal. Testdual psi=rho''/(dmu/dx) delcore, fL²mu, muestra derivada negativa de integralP_tf rho'' inicialmente0: no preservaciónconvexa sin asumir fDomA ni P_tC². Diferencia106115/últimoGLOBAL: reflexión preservaconvexidad, pero tasas completas destruyenestecono;106112Bochner y10364otroobjeto. Root/paired_kernel_fresh, auditoría new_structural_sign PASS, cotejoall3. No signoA ni descarte deotrosconos; papers intactos.


**2026-11-07 — T*T/Hardy ponderado: identidad sin cota nueva (control de duplicación).** GLOBAL: B_j=Lg−2sumΛ(m)m^jD_m², E_j(U)=integral t^(j−1/2)[logt|U|²+ReB_jUbarU]. Para P(1)=0, (B2P)'=B4P' e IBP da Q=(pi²/2)(4E4(P')−6E2(P)−6||P||²_t3/2). Borde−6P1·bar(B2P1) desaparece sin exigirP'1=0. Hardy de normas solas no firmaB_j; no estimación conjunta obtenida. GaugeR=e5x/4P(e^x) devuelve dato físico F=−2pi(R'+R/4). Constructor global_signed_balance/root verificación directa, cotejoall3/GRAM. NO nuevo signo ni NO-GO general; no repetir identidad como cierre. Papers intactos.


**2026-11-07 — Traslaciones imaginarias conjugadas de C_0 no minoran A (PROVED, clase precisa).** GLOBAL, «Traslaciones imaginarias conjugadas»: K_eta=C0(x+i eta,y-i eta), |eta|<pi/4. Theta completa da K_eta(x,x)~pi³/c_eta exp(9x-2pi c_eta exp(2x)), c_eta=cos2eta, uniforme en compactos interiores. Así K_eta/D0>=1/2 uniformemente, mientras A(x,x)/D0<=x/sinh2x->0 y Cu/D0<=u^-1exp(-2x)->0. Ninguna mezcla positiva fija no nula sin gauges puede minorar ni representar A o Cu, 0<u<=1. Diferencia frente a traslaciones reales: argumentos imaginarios conjugados interiores, no cubiertos por aquel descarte. Constructor global_sign_independent_attempt/root, auditor new_structural_sign PASS, cotejo all3 sin antecedente literal; sin prioridad mundial. Sólo esta clase, no negatividad de A ni descarte de gauges/congruencias generales. Sin web/cómputos/papers.


**2026-11-07 — Cociente integrado A/C0 no PSD, incluso con gauges (PROVED).** GLOBAL, «El cociente integrado A/C_0»: diagonales H(x,x)<=x/sinh2x->0, pares; antidiagonal H(x,-x)->1/2. Prueba completa: nu_x proporcional a2sinh2r Phi(x+r)Phi(x-r) concentra en0; lower c exp(7x-2pi exp2x), colas delta..x y x..infinito controladas con theta completa. Menor{−x,x}->−1/4. Para Cu/C0, u>0 fijo, mismo argumento da antidiagonal(1+u)^−2, diagonal0, menor negativo. Factores diagonales no nulos sólo congruencia del cociente: no reparan transporte Schur. Diferencia frente a q_u puntual: aquí kernels ya integrados; no deducible de aquel no-go. Root/global_sign_independent_attempt, auditor new_structural_sign PASS, cotejoall3. Sólo cocientes, NO A/Cu negativos ni descarte de otros transportes; sin web/cómputos/papers.


**2026-11-07 — Proyección ortogonal de divisibilidad: aplicación de densidad (PROVED).** GLOBAL, «Control de la sustitución ortogonal»: en H=L²dt/(2t), clausura span h_(m²k)=H por GRAM17.7 escalado x=exp(-pi m²t); Pi_m=I. Sustituir selección coordenada P_m por Pi_m en factorial pierde divisibilidad. R_mF=m^-1/2F(m²t), norma<=m^-1/2||F||; suma Lambda(m)||F-R_mF||² diverge siF!=0, ya sobre potencias2. No elimina resto firmado ni prueba Q negativo; sólo invalida ese reemplazo. Root/global_sign_independent_attempt, auditor new_structural_sign PASS, cotejoall3. Aplicación del antecedente, no herramienta nueva ni signo; sin web/cómputos/papers.


**2026-11-07 — Realización operatorial theta explícita (PROVED, no signo).** HYPERBOLIC§12.6: H=L²(sech(pi omega/2)domega) directaR³, Q=(cos omega v,cosh(v/4),cosh(5v/4),cosh(9v/4)); C multiplicador(-omega²,lambda_j²). Dcontinuo=1+omega coth(pi omega/2)+(15/2)cosh(pi omega/2)/cosh(2pi omega), Ddiscreto=(-29/4,-23/4,-9/4). BQ=sinhvQ'+coshvDQ define operador simétrico densamente definido sobre spanQ, clausurable; C,D autoadjuntos y dominios de grafo verificados. qtheta=Phi(v/2)exp(2pi coshv) es observación continua exacta: restar trescosh deja residual analítico strip pi/2, O(exp(-|Re v|/4)); densidadcoseno decaeexp(-pi omega/3), cuadrado/rho integrable. Diferencia12.5: se construyen objetos y observación, no sólo condiciones necesarias. Root/global_constructive_rethink, auditor new_structural_sign PASS con corrección tasa residual3/4→1/4. NO métrica compatible, Greenpositivo ni signoA; no prioridad mundial. Sinweb/cómputos/papers.


**Extensión integral de la misma realización12.6 (PROVED, no signo).** Y_nu(b)=integral_0∞exp(-bcoshv)cosh(nu v)Qv dv pertenece a grafosC,D,Bbar por superamortiguación. IBPdoble con bordes nulos da Yrr=(b²+nu²)Y+2DYr+(-C+2bBbar)Y, r=logb. Observaciónexacta <Y_nu(2pi),h>=Z(2nu), normalización completa. Root/new_structural_sign PASS de dominios y signos. No autoadjunción de la suma, métrica ni Greenpositivo/signoA.


**2026-11-07 — Métrica local acotada imposible para realización theta12.6 (PROVED, clase).** HYPER12.7: e2,e1 en grafoBbar,C,D² con Be2=−9e1/4, Be1=−7e0/2−9e2/4. Para M(r)>0 acotada localC², sin diagonalidad, compatibilidad M'=-DM−MD y simetría deE=−C+D²+2bBbar fuerzan Mij=mijexp(−(di+dj)r). Par(e2,e1) da b[−9M11+14M20+9M22]−63M21=0, exponentes25/2,21/2,11/2,8 distintos: m11=m22=0, contradicción. No Be0; límitesdegrafo yformas justificados. Diferencia12.4: realizacióntheta exacta infinita, no modelo2x2. Root/global_constructive_rethink independientes, new_structural_sign PASS. Realización12.6 permanece válida; sólo falla esa reparación local acotada con principal−I. NO métricasnoacotadas/nolocales, otrasconexiones/realizaciones ni signoA decididos. Sinweb/cómputos/papers.


**2026-11-07 — Laplace de parejas recíprocas (identidad PROVED, candidata OPEN).** GLOBAL: D_v=integralPhiPhi[exp(-v/z)-exp(-vz)]dr,z=exp(2r+x+y). Cu=integralexp(-uv)D_vdv yA=integral(1-exp(-v))/v D_vdv, Fubiniabsoluto por |h_u|/|logz|. D_v/v→C0 conmayorante|z−1/z|. PSDdeD_v∀v,tamaños bastaríaA; premisa NOprobada, sinfalsificador. Diferencia: combinarrecíprocosantesfirmar, no fuentesaditivasBPY; Poisson2Dpropuesto no introduce nm, noGram obtenido. Root/global_constructive_rethink, auditor new_structural_sign PASS; cotejoall3/E101070/renovaciónsinliteral. No nueva estimación de signo ni prioridadmundial, sinweb/cómputos/papers.


**2026-11-07 — Capa Laplace D_(2pi) indefinida (PROVED certificado; actualiza candidata anterior).** GLOBAL: bloque−1,0,1 tiene entradasd1,c,e ycentrald0; (d1+e)d0−2c² in[−6e−21 ±8.08e−22]<0. Test racional(1,−1/1300000,1) upper<−2.6e−17. Cuatrointegralesplegadas positivas,32768rectángulosArb192bits porintegral,8modos+omisiónuniforme2^-224,cola s>=4<2^-1000;inflación2^-210. Verificador tools/power_paired_laplace_counterexample_verify.py ylogsroot/audit FULLPASSexit0; SHA256 e6fee17a626174c60ecbd46a4d206deca911a3e156ec25fd4af5b0b695e7a07c. Diseño root/global_constructive_rethink, auditoría previa/literal yreproducción new_structural_sign PASS. Un diagnóstico, sinbarrido. D_vPSD∀v FALSIFIED; identidadLaplace permanece, compensaciónintegradaOPEN. NO Cu/A negativos ni ventanaT/papers modificados.


**Corolario de D_(2pi), misma entrada.** GLOBAL: testcertificadog(v)=c^TD_vc continuoacotado, g(2pi)<0; (-1)^nf^(n)(u)=integralv^nexp(-uv)g(v)dv paraf=c^TC_uc. PesosGamma enu=n/(2pi) concentranen2pi (errorcuadráticov0²(n+2)/n²), porloquederivadasalternadasnegativaseventualmente. RefutaCMmatricialenTODAu>0/cualquiercola; NOen(0,1], niPSDdeCu/monotoníaorden1/signoA. Root/global_constructive_rethink ynew_structural_sign PASS; consecuencia sincómputosnuevos.


**Control puntual posterior, NUMÉRICO no certificado.** GLOBAL: al integrar paraCu conu=1/(2pi), test fijo(1,−1/1300000,1), nodos−1,0,1, forma≈4.0700e−15 positiva en double; no falsificadorintegrado encontrado. Ocho modos/cortes sinenclosure, no PSD ni signonuevo. No barrido ni máscertificados; D_(2pi)negativo sigue sinimplicarCu/Anegativos.


**2026-11-07 — Primitivas de D_v: revisión sin avance de signo.** GLOBAL, «Primitivas de las capas»: G_V=int_0^V D_v, F_R=int_0^R D_v/v; F_R=G_R/R+int_0^R G_v/v² y A=int(-w')G_V, w=(1-exp(-V))/V. Identidades verificadas root/fresh_gap_screen/new_structural_sign; G_V PSD todos V sigue OPEN. Cambio de peso sin operación theta nueva rechazado como ruta nueva. El argumento por radicales aproximados no cierra: nodos normalizados en C0 tienen A/C0->0 y G_V/C0<=V/(2sinh(2x))->0 para cada V, aunque G_V/C0->1 al tomar V->infinito primero. Falta radical fijo en dominio común; no refutación de G_V ni A. Sin cómputos ni papers.


**2026-11-07 — Productos cosh desplazados: clausura entera incompatible con theta (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13. Para Q_n=prod_j(cosh(b_nj t)-c_nj)/(1-c_nj), b_nj>0, -1<c_nj<1, Q_n(1)<=M implica suma d_nj<=M-1, d=(cosh b-1)/(1-c), y b<=B=arcosh(2M-1). En |z|<=R, |Q_n(z)|<=exp[(M-1)R²cosh(BR)]. Todo límite localuniforme real se extiende a función entera. El cociente theta Phi(t)exp[2pi(cosh2t-1)]/Phi(0) diverge en la cúspide t=(log2)/2+i pi/4 ya probada; no es tal límite. Excluye aproximar Phi por C_n exp(-2pi cosh2t) Q_n a escala fija, e infinitos productos definidos por sus parciales. Diferencia frente§11/11.4: c variable evita la multiplicidad entera anterior, pero normalidad excluye la clase ampliada sin clasificar productos límite. Constructor root; filtro y auditoría independiente shifted_cosh_gate PASS, root PASS. No decide conservación de PSD por cada factor; no cubre escalas variables, otros factores, sumas, cocientes o potencias reales. Sin signo A nuevo, ampliaciónT, cómputos numéricos, web ni papers.


**2026-11-07 — Escala positiva variable en productos cosh desplazados: escape cerrado (PROVED).** `03-research/phase-211-sign-sandbox/POWER_HYPERBOLIC_MODEL_GRAM.md`§13.1 amplía§13 a phi_n=C_n exp(-a_n cosh2t)Q_n con a_n>0 variables. Nueva pieza: log[(cosh(b sqrt(s))-c)/(1-c)] es cóncava en s>=0 para b>0,-1<c<1; el numerador de x f''-f' se acota por(1+coshx)(x-sinhx)<0. Con H(s)=cosh(2sqrt(s)), delta=H0+H2-2H1>0, a_n<=[2logphi_n(1)-logphi_n(0)-logphi_n(sqrt2)]/delta. Convergencia positiva en esos tres puntos acota las escalas SIN convergencia de derivadas; normalidad§13 vuelve a aplicar y la cúspide theta excluye aproximación localuniforme real. Diferencia: a_n->infinito evadía el control complejo anterior, ahora se descarta por una cota discreta. Constructor root; filtro y auditoría independiente shifted_cosh_gate PASS, root PASS. Se retira sólo la reserva de escalas positivas variables de la misma base cosh2t; no cambios de frecuencia, otros factores, c fuera(-1,1), sumas/cocientes/potencias reales ni conservación abstracta de PSD. Sin signo global nuevo, ampliaciónT, cómputos, web o papers.


**2026-11-07 — BPY geométrico G2: OPEN, diagnóstico inconcluso.** Fuente: phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «Aproximantes BPY geométricamente simetrizados». G_N=sqrt(Phi_N(t)Phi_N(-t)), con f_N convolución de dos exponenciales por tasa pi n², evita la cola exponencial de la media aritmética previamente descartada. Filtro independiente PASS acotado; fórmula elemental de G2 y supercola revisadas. Dos bloques de jets exploratorios dieron mínimos numéricos positivos, sin certificado; se detuvo enumeración. No Gram allorders ni falsificador, no nueva positividad o T. No repetir diagnóstico sin mecanismo nuevo. NO NO-GO de esta familia; PSD todosN y paso dominado al límite siguen pendientes. Papers intactos.


**Actualización BPY geométrico — límite PROVED, signo OPEN (2026-11-07).** GLOBAL, «Paso al límite de los aproximantes geométricos»: reservar Gamma(2,pi), evaluar E exp(pi Y_N)=[2N/(N+1)]²<=4 y convolucionar da f_N(v)<=4pi²v exp(-pi v). Así G_N(t)<=2pi²exp(-pi cosh2t) uniformemente enN. Con la convergencia previa f_N→2pi q, dominación absoluta prueba A[G_N]→A[Phi] localuniformemente, incluidos todos los cruces de cada bloque fijo. Cierra la obligación de límite de la entrada precedente; no PSD de G2 ni todosN, no comparación matricial desde la cota escalar. Root y filtro/revisión geometric_domination_gate PASS; aplicación de herramientas previas a esta familia, sin prioridad ni nuevaT. Papers intactos.

**2026-11-07 — BPY geométrico: comparación consecutiva con sech REFUTADA para todo c>0.** Fuente phase211 GLOBAL, «Comparación consecutiva BPY con congruencia sech». No existe c>0 con A[G2]>=c D A[G1]D, D(x)=sech(2x), en todos los bloques reales. Diferencia explícita frente al acoplamiento consecutivo: congruencia externa destinada a corregir la caída adicional del perfil. Filtro previo geometric_sech_congruence_gate PASS limitado a falsificación; construcción root y auditoría matemática independiente PASS. Prueba analítica completa: H(z)=z−2+(z+2)e^−z no se anula en Re z>0 por identidad energética elemental, lo que define G2 holomorfa en |Im z|<pi/4. A[G2](iy,−iy) queda uniformemente acotado; A[G1](iy,−iy) tiene cota inferior positiva y D(iy)D(−iy)=sec²(2y) diverge. PSD real implicaría diagonales complejas no negativas por jets y Taylor, contradicción para cada c. Existe por tanto un bloque real finito negativo del RESTO para cada c, sin orden/coefs explícitos ni cómputos. No negatividad de A[G2] ni de A[Phi]; otras congruencias no decididas. Límite geométrico sigue probado, signo global OPEN, sin nuevaT ni cambios en papers.


**2026-11-07 — BPY G1→G2: exclusión de TODA congruencia holomorfa en la franja (PROVED).** Fuente GLOBAL, «Ampliación: ninguna congruencia holomorfa no nula transfiere G1 a G2». Si D es holomorfa en |Im z|<pi/4, real sobre R, y c>0, PSD de A[G2]−c D A[G1]D implica D idénticamente0. No se supone crecimiento, extensión al borde ni ausencia de ceros. Diferencia frente al factor sech: A[G1](x+iy,x−iy) diverge uniformemente para x en compactos positivos al subir y a pi/4, mientras A[G2] permanece acotado. Jets/Taylor fuerzan D→0 uniformemente en esos segmentos; continuidad, reflexión y unicidad concluyen. Construcción root; filtro previo y revisión matemática independiente geometric_sech_congruence_gate PASS. No afirma PSD para D=0 ni negatividad de G2, no cubre factores con franja menor u operaciones no diagonales. Sin cómputos ni nuevaT; papers intactos, signo global OPEN.

**2026-11-07 — Cierre BPY G1→G2 para CUALQUIER factor diagonal real (PROVED).** GLOBAL, «Cierre de la transferencia diagonal: regularidad automática del factor». Para cualquier D:R→R y c>0, PSD de A[G2]−cD A[G1]D implica D≡0, sin hipótesis iniciales de regularidad. L=cD A[G1]D es PSD y dominado por K=A[G2]; el Hilbert de K y un operador 0<=T<=I prolongan L holomórficamente mediante jets/Taylor. Una sección real estrictamente positiva da analiticidad real de D. Ausencia de ceros comunes de las secciones de A[G1] en Re z>0 permite pegar cocientes y extender D allí. La desigualdad compleja y el contraste uniforme de borde anterior fuerzan D=0. Constructor root, filtro y auditoría independiente geometric_sech_congruence_gate PASS. Se cierra buscar otros factores diagonales, incluidos los de franja menor. No afirma que D=0 sea suficiente, ni refuta PSD de G2; transferencias no diagonales fuera de alcance. Sin cómputos, nuevaT o papers; signo global OPEN.


**2026-11-07 — G2: energía derivada de borde y presupuesto de ramas finitas (PROVED, sin signo nuevo).** Fuente phase211 `POWER_GLOBAL_ROUTE_REVIEW.md`, «G2: la energía derivada de borde supera cualquier colección fija de ramas». Para x>0 fijo, E_x(epsilon)=integral_x^infinito 2t|G2'(t+i(pi/4−epsilon))|²dt satisface E_x/log(1/epsilon)->infinito. Las raíces auxiliares H(iu_j)=0 tienen u_j~2pi j; el coeficiente local w_j=|(G2²)'(z_j)|/4~C²d^6/(48u_j) da contribución 4t_jw_j log(1/epsilon)+O_j(1). La suma de t_jw_j diverge: colección finita primero, límite después, colección creciente al final, sin uniformidad en j. Cada colección fija de vecindades aporta fracción->0 de la diagonal completa. B_x=partial_z partial_w A2(x+iy,x−iy)=E_x−|G2(x+iy)|² conserva el borde y tiene el mismo límite normalizado. Resuelve el presupuesto diagonal pendiente del filtro de dos singularidades; NO controla el cruce completo, no descarta ese menor ni prueba/refuta PSD de G2 o Phi. Constructor root; filtro previo y auditoría independiente g2_tail_residue_novelty_gate PASS. Cotejo dirigido Paper48/all3/primarias, sin prioridad mundial. Sin cómputos, nuevaT o cambios en papers; global OPEN.


### Fase 212, ronda 1 — dos NO-GO con clase (sin signo)

- **Fase 212, comparadores real-positivos en la escalera de potencias — NO-GO con clase, PROVED relativo a tres teoremas clásicos citados (representación integral de funciones real-positivas, interpolación de Pick, condición de Blaschke).** `ROUND_001_L.md`, Teorema 3.1 y Cor. 4.1; revisión `REVIEW_001_LC.md`. Clase: núcleos [M0(u)+M0(v)]/(u+v) con M0 real-positiva en Re u > 0 y real en (0,∞), comparados con el núcleo de la escalera en el mismo portador o tras congruencia común, con dominación K_M − εK_{M0} ⪰ 0 en todos los tamaños sobre la escalera 31.5 + n (o cualquier conjunto de nodos con Σ1/u = ∞ o con acumulación interior). Conclusión: M0 no tiene término lineal y su medida de borde está dominada por (1/ε) veces la de M, que bajo esa hipótesis es puramente atómica; quedan excluidos, para el ε correspondiente, todo término lineal, toda parte continua, todo átomo ajeno y toda masa mayor que r_k/ε. Consecuencia nueva: ½asinh(u/4π) queda excluido para todo 0 < ε < 1 sin certificado (ε = 1 ya registrado; ε > 1 trivial). La comparación hiperbólica pequeña a = 2π de 211 es una instancia (misma condición necesaria; su cierre sigue dependiendo del certificado de intervalos). Exclusión no efectiva: no da bloque ni vector. No cubre núcleos PSD generales, congruencias no comunes, compensaciones conjuntas, tamaños acotados, ventana fija ni la

- **Fase 212, sistema ampliado de cuadrados con selección o torsión aritmética en nodos o modos — NO-GO con clase, PROVED (relativo a GRAM §18.2 y a la holomorfía de z ↦ P_z de GLOBAL «Escalas libres de cuadrados»).** `ROUND_001_C.md`, Lema 1, Teorema R, Corolario 2; revisión `REVIEW_001_LC.md` (lema de unicidad de coeficientes modales incluido allí). En una identidad única A_0 = Σ cuadrados + resto no negativo sobre el portador de escalas enteras (y = 0), cada cuadrado es continuo en la norma del grafo y sus coeficientes en k son los valores enteros de una función holomorfa de crecimiento polinómico en un semiplano; por tanto ningún cuadrado no nulo puede anularse sobre un conjunto de nodos o de modos de suma recíproca divergente, ni ser la torsión de un funcional continuo por una función con un conjunto de nivel divergente de complemento divergente (caracteres de módulo q ≥ 2, sumas de Ramanujan no constantes, μ, μ², Λ, indicadoras de clases de residuos, de múltiplos o de gcd fijo). Generaliza con el mismo instrumento GRAM §18.7 (soporte finito) y GLOBAL «Escalas libres de cuadrados» (cola libre de cuadrados, discontinuidad de S_sq); lo nuevo es la clase, no la herramienta. No excluye cuadrados continuos con índice o pesos aritméticos en la dilatación, torsiones sin conjunto de nivel divergente, restos sin signo manifiesto, ni objetos por ventana o sobre 𝔸_M. No aporta signo. La dirección de R9 en la formulación (S) queda abierta con una única restricción de módulo de continuidad (Observación 5).


### Fase 212 — fase 170 leída por archivo (sin signo)

Detalle en `03-research/phase-212-missing-object/RULES_AVOID.md` §I. Cierres de clase PROVED recuperados
de la 170 que no figuraban: factorización universal por 𝒟_N (R170_868); paridad de la clase de borde
(R170_870); congruencia pura de las dilataciones positivas por bloque (R170_860–861); leyes bilaterales
de collar por composición lineal (R170_840 Teor. 6.1); residuo común = cierre (R170_837 Teor. 5.1).
No intentado en la 170: cola como Σ_{k>N} h(k)|ℓ_k(F)|². ([log mcd] sobre F y el canal de dos bases primas sí tienen antecedente en 211 y R166_502; ronda 2 de la fase 212.)


### Fase 212, ronda 2 — selección sin candidata (sin signo)

Cola exterior como suma de cuadrados en finitos momentos Gamma: NO-GO con clase PROVED, genérico en el
peine (`ROUND_002_A.md`, `REVIEW_002_A.md`); no excluye L = ∞ ni la conversión conjunta con E_N y Tate.
[log mcd] sobre F (K2′) y canal de dos bases primas (K5): «sin mecanismo nuevo» por repetición de 211
GLOBAL/GRAM §17.2 y de R166_502 §5.2; ninguno es NO-GO. Piezas PROVED elementales en `REVIEW_002_BC.md`
(Lemas B-1, B-2, C-1, C-2); ninguna es avance de signo. Terreno no examinado: familias que ven la
ventana y no son la modal theta.


### Fase 212, ronda 3 — nueve zonas, ninguna candidata (sin signo)

Detalle en `03-research/phase-212-missing-object/REVIEW_003.md` (R3-a…R3-i) y `RULES_AVOID.md` §J. Cierres
de clase PROVED: multiplicadores y reflexión en sectores de paridad; cuadrado afín emparejado con el
peine; ancla con borde en formas semidefinidas; virial de dilatación pura sobre P_T; bloques exteriores
separados de Poisson–Chebyshev; 𝔸_M = WᵀDW por divisibilidad; métrica de Green de tipo resolvente.
Sin excluir y sin objeto: término de grado ≥ 2 en el peso que sume y se anule en Λ; operadores con
compresión a la ventana; W con soporte en m ≈ kn; formas indefinidas.


### Fase 212 — fase 161 leída por archivo (sin signo)

Detalle en `03-research/phase-212-missing-object/RULES_AVOID.md` §K. Recorrido: compresión a la ventana,
fuga, posición, rango finito, varianza orientada de divisores. R161_018 no es un cierre (R161_075).
Abierto y sobre todo P_T: SP-161/L161.1 con pesos con signo (R161_002 §§4–5). No construida: salida A
de R161_033.


### Fase 212, ronda 4 — cinco zonas, ninguna candidata (sin signo)

Detalle en `03-research/phase-212-missing-object/REVIEW_004.md` (R4-a…R4-f) y `RULES_AVOID.md` §L. Cerrado
con clase: meta L161.1 con pesos con signo; inversos aproximados invariantes por traslación; defecto de
divisores cuadrático exigido para todo peso; pivotes por patrón de casi-divisibilidad; conteo de inercia.
Sin excluir y sin objeto: cierre de {𝔸_M} bajo complemento de Schur con peso transformado; Möbius del
sistema; contabilidad R161_032 (4.2).


### Fase 212, ronda 5 — generativa, ningún objeto (sin signo)

Detalle en `03-research/phase-212-missing-object/REVIEW_005.md` (R5-a…R5-e) y `RULES_AVOID.md` §§M–N. Cerrado
con clase: signatura de Lorentz y log-concavidad en un punto base; polinomio hiperbólico de grado ≥ 3;
cierre bajo producto sobre la signatura; inducción en la ventana por el peso entrante; forma como varianza.
Sin excluir y sin objeto: reparto local por primo no invariante por traslación con fórmula propia.

Fase 212, ronda 6: reparto por primo dependiente de la ventana. NUMÉRICO: `θ_p(t,s)` de dos posiciones alcanza
el techo hasta `T ≈ 0.69` y falla desde `0.70`; genérico en `c`. Regla por bandas de distancia rechazada en
la puerta (repetición del Teorema D de 159 G2_B8_R5; sin mecanismo de signo). Detalle en
`03-research/phase-212-missing-object/REVIEW_006.md` y `RULES_AVOID.md` §O.

Fase 212, cotejo del subespacio casi nulo: repetición de 211 C11 (par casi nulo y tangencia) y cierres
posteriores; no se construye. Detalle en `03-research/phase-212-missing-object/ANNEX_COTEJO_NULLDIR.md`.

Fase 212, ronda 7: cotas de contacto por potencial (NO-GO con clase), predicado de etapa en cono convexo
(equivale a reparto local), canal de producto (repetición de R161_034). Detalle en
`03-research/phase-212-missing-object/REVIEW_007.md` y `RULES_AVOID.md` §Q.

Fase 212, ronda 8: concomitante de borde producto/cocientes, repetición de la fase 161 (R161_035, R161_057–065).
Detalle en `03-research/phase-212-missing-object/ROUND_008_A.md` y `RULES_AVOID.md` §R.

Fase 212, ronda 9: ninguna candidata pasa la puerta; taxonomía de clases y lista de propiedades del objeto en
`03-research/phase-212-missing-object/ROUND_009_G3.md`; revisión en `REVIEW_009.md`.

Fase 212, ronda 10 y lecturas: cuadrado de Sonin ciego a los controles; covarianza aditiva + `Λ∗1 = log` = (PC)
de R161_001; el residuo de pesos con signo en SP-161 ya estaba cerrado (R4-a). Detalle en `03-research/phase-212-missing-object/RULES_AVOID.md` §T.

Fase 212, ronda 11: discrepancia de retículo sobre los restos de (PC), NO-GO de selección. Detalle en
`03-research/phase-212-missing-object/ROUND_011_A.md` y `RULES_AVOID.md` §U.

Fase 212, ronda 12: L161.4 es reformulación de la meta sobre el radical y ciego al peso; no pasa la puerta.
Detalle en `03-research/phase-212-missing-object/ROUND_012_A.md` y `RULES_AVOID.md` §V.

Fase 212, ronda 13: ventana de contactos 2, 3, 4 = repetición de la fase 211; combinación de objeto con signo y
objeto que ve el peso (catorce operaciones), ninguna pasa la puerta. Detalle en
`03-research/phase-212-missing-object/ROUND_013_A.md`, `ROUND_013_B.md`, `ROUND_013_C.md` y `RULES_AVOID.md` §W.

Fase 212, ronda 14: canal de cocientes, positividad multiplicativa sobre primos y transición entre ventanas;
ninguna candidata pasa la puerta. Detalle en `03-research/phase-212-missing-object/ROUND_014_A.md`,
`ROUND_014_B.md`, `ROUND_014_C.md` y `RULES_AVOID.md` §X.

Fase 212, ronda 15: transporte no afín, acoplamiento entre primos, convexidad e índices, todos repetición;
diagnóstico del reparto por primo (lema de rango mínimo; ley de conteo por contactos refutada, NUMÉRICO).
Detalle en `03-research/phase-212-missing-object/ROUND_015_A.md` a `ROUND_015_D.md` y `RULES_AVOID.md` §Y.

Fase 212, ronda 16: curvatura, estados KMS y positividad por reflexión, todos repetición de fases anteriores.
Detalle en `03-research/phase-212-missing-object/ROUND_016_A.md`, `ROUND_016_B.md`, `ROUND_016_C.md` y
`RULES_AVOID.md` §Z.

Fase 212, ronda 17: el muro del reparto por primo (`T ≈ 0.697`) no es un evento de cadena; el corpus no tiene
prueba por mecanismo sobre el umbral arquimediano. Detalle en
`03-research/phase-212-missing-object/ROUND_017_A.md` y `RULES_AVOID.md` §AA.

Fase 212, mapa consolidado de las rondas 1–17: tabla por familia, restricciones sobre el objeto (cláusulas O11–O17 de `OBJECT_SPEC.md` §5) y terreno sin objeto ni cierre, en `03-research/phase-212-missing-object/MAP_ROUNDS.md`. Sin mecanismo de signo; global OPEN.
