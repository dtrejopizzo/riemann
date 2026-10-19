# R162_2300 — Master grid repaint proposal

Assignment: surveyor + audit editor. Read-only of the grid, the JSON and the cited files; this file is the only piece of writing. No web, no numerics. **No sign is asserted; row D OPEN; no statement label changes.** It is a *proposal*: the editor merges it (grid §8) or rejects it.

Sources: grid §1–§8 (log entries 13–18), `R162_2300_MASTER_grid.json` (OPEN/PARTIAL routes per cell, extracted with python), NO-GO-LIST.md, R183_028, R183_033, R184_001–015, R184_091–093, R184_099. **Side finding:** phases 168–182 **are not merged into the grid** (the log jumps from entry 12, phase 167, to 13, phase 183). Here I use only their explicit verdicts: R168_001 (residual survey), R168_103, R168_202, R171_FINAL, R173–R175_FINAL, R182_201. Their full merge remains pending.

Criterion applied (hardened §8.3 rule): an OPEN/PARTIAL route counts as live only if (a) no later file killed it, (b) it is not E1 (statement ⟺ RH, or a per-window "∀T" law), (c) it is not blind to the class (M_m, DH, deletion, DMV, Type I) and (d) it has a statement. If something survives that does not satisfy (b)–(d), the cell is ◩ with that residual named. An object with no candidate or a pending audit is **not** a route.

## 1. Proposed grid

| row \ col | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 identity/EF | ◩ | ◩ | ◩ | ◩ | ◧ | ■ | ◩ | ◧ |
| 2 positivity/support | **■** ← ◩ | ■ | ◩ | ■ | ◧ | ◩ | **◩** ← ◧ | ◧ |
| 3 estimation | ◧ | ■ | ◩ | ◧ | ◧ | ◧ | ■ | ■ |
| 4 Euler | ◧ | ◩ | ◧ | **◩** ← ◧ | ◧ | ◧ | ■ | ◧ |
| 5 ℤ-integrality | ◩ | ■ | ◩ | ◩ | ◧ | ◩ | ◧ | ◧ |
| 6 Λ values | ◧ | ◧ | **■** ← ◩ | ■ | ◧ | ◧ | ◧ | ◧ |
| 7 zero side | **◩** ← ◧ | **◩** ← ◧ | ■ | ◧ | ◧ | **◩** ← ◧ | ■ | **◩** ← ◧ |
| 8 arithmetic-free | ◧ | ◩ | ◧ | ◧ | ◩ | ◩ | ◩ | ◧ |

## 2. Proposed count

**■ 13 · ◩ 23 · ◧ 28 · □ 0** (before ■ 11 · ◩ 19 · ◧ 34). 8 cells change:
- ◩ → ■: **2A, 6C**.
- ◧ → ◩: **2G, 4D, 7A, 7B, 7F, 7H**.
- No cell moves up. Borderline cells I do **not** change for lack of a citable proof: 1E, 2E, 6B, 6G, 8D (see §3).

## 3. Cell-by-cell justification

Abbreviations: "killer" is the file that kills the route and the wall or falsifier it uses. Cells ■ with no live OPEN/PARTIAL routes in the JSON (1F, 2B, 2D, 3B, 3G, 3H, 4G, 5B, 6D, 7C, 7G) are kept without comment. The only PARTIAL of 2B (phase-60 CCM) already carries E1.

| cell | before | proposal | OPEN/PARTIAL routes from the JSON and who kills them | surviving residual or route |
|---|---|---|---|---|
| 1A | ◩ | ◩ | B3-KREIN, 34/91 (E1); P47 thm:parityschur (M, W2); 120 C.1 global square (E1) | λ_W>0 beyond ½log5 (certificate, clashes with M); C_B → O2601.1 |
| 1B | ◩ | ◩ | R161_011–019 (E1), R161_018 (F4) | (4.2) global Sonin range, E1. R183_018/019 reinforce: entire Sonin NO-GO for T>½log2 |
| 1C | ◩ | ◩ | R161_020–021 PARTIAL | scalar X_T not realized (not formulated) |
| 1D | ◩ | ◩ | — | boundary triple (4,4), O2702.1 Burnol (RH-neutral; R184_009 confirms it: tool, not input) |
| 1E | ◧ | ◧ | polarcap PARTIAL **dead**: R184_012 (already closed by R160_M4_R1 L1/A/B and R162_703; E1 for any ∀T statement). Bagchi/LP-112 (E1) | **alive:** Conj. A.15 (monotonicity of the Kreĭn index under dBN, phase-28-four-fronts/01; never attacked, no proven killer; §7 discards it for W3 without proof). D-109 without mechanism. *Candidate for ◩ if an audit writes up A.15's W3 blindness.* |
| 1G | ◩ | ◩ | — | degree-one GRH uniform in χ (Thm O.2) |
| 1H | ◧ | ◧ | P122_D_SPECIFICATION / Q27 E_(∞,T) **dead**: R168_202 Thm 2.2–2.3 (with (E1)+(E3) the class is {ζ}, W-identification; its comparison positivity is q_T, a restatement); 115_16 semilocal Sonin trace identity **done and NO-GO**: R183_018 §3 (exact identity) + Thm 5.1, R183_019 Thm 4.1 (n₋=∞); R135_007, D.13, phase-64 (E1) | **alive:** P152.1 Dolgopyat–Mayer via Lewis–Zagier; P25 V.2 Pontryagin completion (bridge κ(Q)=ind₋H_C) |
| 2A | ◩ | **■** | phase-5/B2 semilocal CC and 115_13–16 (semilocal Sonin trace-phase derivative): **dead** by R183_018 Thm 5.1 + R183_019 Thm 4.1 (entire Sonin n₋=∞ for T>½log2), R183_027 ((L-Son) with uniform η is false: refuted unconditionally, because (L-Son)⟹RH and RH⟹¬(L-Son)), R183_033 §4 ("zero directions ∀T" ⟺ D, E1; one direction aligned ∀T does not exist, R183_030 §7) and R184_015 Cor 3 (W11′: every decomposition Pos_S+Δ with ‖Δ‖≤e^{o(T)} is either blind to M_m or E1). P35 L1 (E1). The missing exact identity already exists (R183_018 §3, R183_029) and has no sign (W12) | none with a sign. (M)/(M_w) (R184_003 Lemma B.1) gives only a compact remainder, no sign: it passes to §5 as a tool. λ₁(ker ℓ)=λ₂(prim): explained by parity (R184_003 Thm A.1) |
| 2C | ◩ | ◩ | thm:doob (E1); R161_026–028 (F3) | sharp Poincaré (E1) |
| 2E | ◧ | ◧ | prop:polarcap OPEN and R160_M4_R1 **dead**: R184_012 (Lemmas 1–2; E1 ∀T); Pick/Schur (E1) | **alive (weak):** P47 effective window shift RD_{T′} ⟹ λ^W_T≥0 (no killer; at comb level requires T′≥T*; suspected W7). *Candidate for ◩.* |
| 2F | ◩ | ◩ | — | Bernstein monotonicity of λ_A(T) (not formulated) |
| 2G | ◧ | **◩** | T3 Beurling (PARTIAL, F3:Beurling, conditional on H-DMV, CITED in 157); P46 §28.4: every candidate built is **NO-GO** against the six clauses (R174_FINAL l.80; R175_FINAL §4: "the six clauses stay NO-GO for the triple"; R173_FINAL NO-GO) | six-clause object with no live candidate (W10) |
| 2H | ◧ | ◧ | Berkovich P152.2 (E1) | **alive:** Arakelov 𝒳 (15/M10), Cartwright's tropical Hodge index (136 S5), interlaced OS model (S1 I1), Chinburg–Rumely energies outside 𝔄⁺. All of them are objects under W10 |
| 3A | ◧ | ◧ | 114/D.172 and D.198–227 (M); R154_030 (numerical: not a route); F48 (hyp:pw false); unread web hit (not verifiable without web; R184_009 finds no input in the local literature); (WS*): sieves dead (R167_102 Thm B′, W-sieve), uniform form ⟺ zero-free (R167_101 Thm C), one scale = explicit formula (Thm E) | **alive:** exact stopping point of R167_102: large-values bound for Type II products of length X at a single height (R168_001 row 10: "the only sub-RH form of (WS*)"); P47 Problem A; I6 (36/108); O166.802.1 (meta) |
| 3C | ◩ | ◩ | 34/93 (ND3), M7 (E1), 502 B | Option 3 of R160_020 (E1 by M7) |
| 3D | ◧ | ◧ | R161_073–074 **dead**: R184_012 (numerical certificate, E1; not a mechanism); LP-134 (F3 Hadamard); Tower 2 (E1) | **alive:** GAP-196.A (DH near-doubles under mean spacing); 22/03 GMC rigidity (conditional) |
| 3E | ◧ | ◧ | G2_B9/B2_R5 (needs BD) | **alive:** GAP-157.A, Kronecker flow discrepancy in non-local form (R168_001 row 2: "the non-local form remains OPEN"); Tower 1 (A ⟹ Lindelöf) |
| 3F | ◧ | ◧ | 103_13 (threshold withdrawn); F40 (E1) | **alive:** GAP-157.A non-local Tauberian with LI input; rem:Dgrade |
| 4A | ◧ | ◧ | phase-5 anatomy (F3) | **alive:** GAP-135.A / doc 148 incommensurate frames; G2_B8 Thms L, L′, L″, D (unaudited); P44 (H_L) |
| 4B | ◩ | ◩ | RDI (E1), 84 (rank), R161_012–013 | distributional carrier ker X=span δ₀; cut A1–D3 |
| 4C | ◧ | ◧ | P02 (Lindelöf, not RH); R161_035–038 (2×2 countermodel); G2_B8_R5 joint restriction (E1) | **alive:** L5 Z_{N,ε}; Hecke-type algebra G2_B3_R5 Cor S2; Meyer S+D (R160_020 Opt 6); R161_030–032 oriented variance gate |
| 4D | ◧ | **◩** | exclusion conjecture (21/01–02) = C_B: route (a) NO-GO (R162_2501 Thm 3, every class argument fails by M_m), Γ–Euler detector NO-GO (R162_2502), inertia NO-GO (R184_004 Cor 5, PROVED, not conditional on RH; audit R184_091 upholds it); D.244 tangent Gram (1,\|S\|−1) is prime-to-prime inertia, covered by R184_004 Cor 5 (prime-to-prime Schur chain) | O2601.1: individual property of the Euler product, used non-linearly (no candidate: R184_099 §4) |
| 4E | ◧ | ◧ | P30 L8 (C_B → R184_004); 37/110 and 80–90 (E1); O8 Tate 2×2 closed | **alive:** R153_005 Thm A, cross-term as a uniform-in-T sign mechanism (P153.2, never attacked; R184_006 and R184_007 close P153.5 and P153.4, not P153.2); LP-112 sequential rigidity; phase-90 PROJECTIVE-KATO-EULER |
| 4F | ◧ | ◧ | everything from parts 10–18 (KZ E1, positive tail Thm A, Thm R, rough zeta E1) | **alive:** GAP-157.A condition C1 of Doc 159. Global generating object and O2802.1 not formulated / E1 expected |
| 4H | ◧ | ◧ | I11 **no statement** (R184_012); motivic Rosati (infinite genus); finite colligation (passivity) | **alive:** walls A/B of phase-27-adelic-rigidity; amplifying functor ⊠ (36/106+38/117); colimit L1 of P44 Thm 8bis.4a |
| 5A | ◩ | ◩ | P47 thm:N… (class M≤2) | Problem A |
| 5C | ◩ | ◩ | R162_903 | O2201.1 (zero side) |
| 5D | ◩ | ◩ | — | Smith form of the contact Gram (not formulated) |
| 5E | ◧ | ◧ | R162_1902 (linear only; F2, E1) | **alive:** O1802.3, width ≥0 from **non-linear** integrality in c, tracked in T. O2802.1 (E1 expected) |
| 5F | ◩ | ◩ | R161_075–079 | O2302.1/2 |
| 5G | ◧ | ◧ *(Beurling only)* | ℕ⊔Q factor route **NO-GO ∀θ<1** (R184_008 Lemma AC + Theorem F); linear L* **false** (R184_010 Theorem D, dither); the exponential method does not go below (1−θ)/2 (R184_013 Cor 3.2), so R163_101d is superseded below 1/3; C1 in O(log x) false except for modifications of ζ (R184_005 Prop 4.1); set-theoretic form refuted by ℕ∪√2ℕ (R184_005 N1); θ=0 boundary ∈ E1 (R184_005) | **alive as Beurling theory, not as a route to D** (R166_701: fails (N), blind to zeros): L*_comp (O184.093a; CONDITIONAL on (ZF_R) by R184_014 Thm B.4, OPEN unconditionally, requires ε_p ≡ −p^a mod 1, Cor B.3′); C1 in O(1) (R184_005); question Q / O164.201a, discrete θ<1/3 with a zero β>½ (R184_001 item 11; off-lattice construction O184.001a, the only one alive); division variant P=B∖Q (R184_008 item 4) |
| 5H | ◧ | ◧ | o-minimality (R162_2402) | **alive:** cocycle Φ_Λ with non-band-limited tests (R162_1001); a4/R16 quadratic χ over Spec ℤ; Quillen K_n(ℤ)/RO(G)/A¹; P42's Lefschetz programme; lattice from Sh_Z (P44 §6bis); non-invertible correspondences (P43 §11bis) |
| 6A | ◧ | ◧ | D4 Thm 5.1 / Cor 5.2 (W7, F3), R162_406; Problems A/B (E1) | **alive:** lem:degen at log 2 (R162_2902b); O-D4.2 kernel of 𝒲 on decreasing tests of unbounded support |
| 6B | ◧ | ◧ | prob:annihilate = Gate 1 (registered E1 killer); self-similarity (2202b) | **alive (weak):** identity level Λ=μ*log with entropic ×p (R157_002); the threat is W-sieve Thm D (R167_102), ARGUED only. O2202.1 is a tool with no sign. *Candidate for ◩ if Thm D is proved.* |
| 6C | ◩ | **■** | R162_901 (F2, E1, F3, M); bilinear FI/HB (superseded by R162_502 B); lem:degen / variational characterization (done by R162_2902b except at log 2, which lives in 6A); OS-2 closed (R166_202); R166_502 repeated | none. **O202.1** (T_e=T_o with no sign) closes as a statement with no route (R166_202 Thm 3, parity identity; R168_001 row 13) |
| 6E | ◧ | ◧ | P153.14 (E1) | **alive:** G2_B6_R5 Prop C, RH-free pointed cone under rigid perturbations (untouched; R184_011 treats G2_B7, not B6) |
| 6F | ◧ | ◧ | LP-152 **dead** (R160_M5_R1 Cor 2.4, F3: DH, Epstein, Ξ_a; R184_011); G2_B7_R5 multigenerator **NO-GO as a route** (R184_011 Prop 3.1/Thm 3.2/3.3: → (Q*) under RH, false in the Type I curve); 104 and D.260–262 (E1); P47 Problem B: 6A's twin entry already carries E1 | **alive (weak):** P47 prop:M, weight family of the canonical column s=½ outside the window. (Q*) is noted as a rigidity residual, with no effect on D |
| 6G | ◧ | ◧ | separator 119 (F3: DH) | **alive (weak):** O-D4.3, transposition of (C′) to ζ_K (routine; likely W7+T1, no proof) |
| 6H | ◧ | ◧ | P40 (E1); Borger/Witt Λ-Rosati ("wrong space"; R175 NO-GO for Witt carriers) | **alive:** hyperbolic ruled pairing of Mertens (P43 Thm 10.8b); loaded Tate boundary 106.203–205 |
| 7A | ◧ | **◩** | D.16-γ done (R165_201/202); Hyp (H) "uniform local scarcity of deep zeros off the line" and Doc 153 (quartet tests): both feed the ¬RH ⟹ detection direction, which is E1 and already quantified (R184_006 Thm 1/1′; R184_092: Max–Iso is coherent only under ¬RH); 0A2, 143, 120 C.1, P124_013 (E1); P122_020 (F3: Ξ_a); R163_701 (W2/M) | ω(E) at contact = Rem 4.8a = (★_cell) at the witness (forces RH; jet k=−1, W-jet) |
| 7B | ◧ | **◩** | R163_401 PARTIAL: its gap is (★_cell) ⟺ RH at the witness, i.e. E1 by definition (R168_001 row 19: (★_cell)/(TC)/(WS*), with the routes of 163–167 all DEAD); CCM CAND-1 (E1); P121 F2 (E1, F2); G2_B6_R4 BRS is a tool audit | (★_cell)/(TC) at the witness; O166.501.1 (meta, R168_001 row 8). R184_015 Thm 2: the only source↔form bridge is the explicit formula (W11′) |
| 7D | ◧ | ◧ | Diana C_B → R184_004; Cayley from 69 **no statement** (R184_012); Carleman (E1); P23 (only one inclusion); R162_2190 (numerical) | **alive:** O167.101.2, small-y regime: a finer on-line count than S(t)=O(log t) (class c, sub-RH; R168_103 sharpens it, OPEN); O167.101.1/O701.1 (Dom_θ); O701.2–3; O102.1–2; O2401.1 |
| 7E | ◧ | ◧ | P19 Hyp D (C_B → R184_004); R165_202 (E1) | **alive:** 77–80 (pencil compatibility, class ℓ², simplicity, assembly); R157_004 O4 Kreĭn data at the first crossing; O2501.2 (e<1 ⟹ Θ<1 without finiteness) |
| 7F | ◧ | **◩** | KEP: the twin entry P47 KEP carries E1 (parametrizing 𝔖(T) ∀T = Thm Z, certificate = explicit formula); P33 (E1 at the value −π/8; the A finiteness belongs to the C_B → R184_004/R162_2501 cluster); 38/118 (Carleman, E1); Li Ω₇ (E1) | O164.601.1 = (★_cell) weighted by K (R168_001 row 18: forces RH at the witness); O2601.1 via the C_B cluster |
| 7H | ◧ | **◩** | Ansatz A χ(D)=D²/2 (E1 killer in the JSON); density of H¹_alg in Meyer H¹ **done** (R160_C3 Thm B; R168_001 row 5: "nothing open with content"); R158_006 and C3/D2 (E1) | Ansatz A (carrier implying RH; W10) |
| 8A | ◧ | ◧ | unaudited Thms of 159 (audits, not routes) | **alive:** GAP-198.1, non-factorizable inter-currency combinations outside 𝔄; 0A2 Part II, uncontaminated Galerkin |
| 8B | ◩ | ◩ | M11/M12, P121 (F3) | O2201.1; M11 slot unwritten |
| 8C | ◧ | ◧ | O-151.4 (two entries) **dead**: R168_202 Thm 1.1–1.4 (summand side = restatement; numerator side with valid inputs in Beurling bounded in dlVP; with integrality+EF, class {ζ}) | **alive:** Lemma 108, κ_W(Q_2)≤C n_W (not ⟺ RH, never attacked) |
| 8D | ◧ | ◧ | 37/110 (duplicate: 4E's entry carries E1;MW-6); 35/99 (MW-1/MW-6, W10); phase-63 J-linear Frobenius (function-field mimicry, W8/Thm 19.25) | **alive (to reconcile):** R160_010 D5 (D1 lives in 8H; D3, the windowed converse, died in phase 156). *Candidate for ◩ after reconciling duplicates (NOT CONFIRMED).* |
| 8E | ◩ | ◩ | Ω₇ (critical endpoint), P39 | CA-1 |
| 8F | ◩ | ◩ | — | O2601.1 (R184_004 closes the inertia; no candidate) |
| 8G | ◩ | ◩ | 36/106 (R-FIN) | field uniformity (T1); R-FIN |
| 8H | ◧ | ◧ | E_(∞,T) (R168_202); I14 and Request 122.A **no statement** (R184_012); R160_C1 (Thm Z); C3/D2 (Thm H); 135–140 h⁰ | **alive:** Torelli-failing lamination with fixed points (160 D1 / R158_001, ALK polarization), APS η and [H_C] in KK; Stage 7 of 108; Deninger with Kähler–Riemann foliation; P43 §11bis; non-ergodic DK_α and Prop BL (unaudited); boundary triples of W_λ (RH-neutral, tool) |

## 4. Surviving ◧ routes (raw material for the "crossword")

All of them have a statement and none is marked E1 or is blind to the class according to the record. Those marked † are weak (objects or lemmas with no candidate, or with an ARGUED threat).

1. **1E** Conj. A.15 (Kreĭn index monotone under dBN) †W3; D-109.
2. **1H** P152.1 Dolgopyat–Mayer via Lewis–Zagier; P25 V.2 Pontryagin completion.
3. **2E** RD_{T′} ⟹ λ^W_T≥0 †W7.
4. **2H** Arakelov 𝒳; Cartwright's tropical Hodge; interlaced OS; Chinburg–Rumely †W10.
5. **3A** large values of Type II at a single height (sub-RH form of (WS*)); Problem A; I6.
6. **3D** GAP-196.A; GMC 22/03.
7. **3E/3F/4F** GAP-157.A (Kronecker / non-local Tauberian with LI input / C1 of Doc 159). It is **one route in three cells**. rem:Dgrade (3F).
8. **4A** GAP-135.A (incommensurate frames); G2_B8 L/L′/L″/D †unaudited; (H_L).
9. **4C** L5 Z_{N,ε}; Hecke-type G2_B3_R5 Cor S2; Meyer S+D; R161_030–032.
10. **4E** R153_005 Thm A uniform in T (P153.2); LP-112; PROJECTIVE-KATO-EULER.
11. **4H** walls A/B (27); functor ⊠; colimit of P44 8bis.4a.
12. **5E** O1802.3 (non-linear integrality in c, tracked in T).
13. **5G** L*_comp; C1(O(1)); Q / O164.201a / O184.001a; division variant P=B∖Q. They are open **as Beurling theory**; as a route to D they are dead by (N) (R166_701).
14. **5H** non-band-limited Φ_Λ; a4/R16; Quillen/RO(G)/A¹; P42; Sh_Z; P43 §11bis.
15. **6A** lem:degen at log 2; O-D4.2.
16. **6B** identity level Λ=μ*log (entropic ×p) †W-sieve Thm D (ARGUED).
17. **6E** G2_B6_R5 Prop C.
18. **6F** P47 prop:M (column s=½) †.
19. **6G** O-D4.3 ((C′) at ζ_K) †W7/T1.
20. **6H** Mertens 10.8b; loaded Tate 106.203–205.
21. **7D** O167.101.2 (small-y regime, sub-RH); Dom_θ/O701.x; O102.x; O2401.1.
22. **7E** pencil 77–80; R157_004 O4; O2501.2.
23. **8A** GAP-198.1; 0A2 Part II.
24. **8C** Lemma 108.
25. **8D** R160_010 D5 †to reconcile.
26. **8H** Torelli-failing lamination with fixed points + ALK; APS/KK; Stage 7; Deninger–Kähler; DK_α/BL †unaudited.

The only ones of **class c** (sub-RH, with a statement and outside every named wall) are: Type II at a single height (3A), O167.101.2 (7D), non-local GAP-157.A (3E/3F/4F), L*_comp and C1 (5G, Beurling only), Lemma 108 (8C) and O1802.3 (5E). None is a candidate that passes S4 and S11 at once (R184_099 §4).

Convergent ◩ residuals, which are not routes: **O2601.1** (4D, 7F, 8F; C_B cluster), **(★_cell)/(TC)/ω(E)/O164.601.1** (7A, 7B, 7F), object §28.4 (2G), Ansatz A (7H).

## 5. Walls to be added in §3

| W | statement | cells | source |
|---|---|---|---|
| **W11′ source/form disjunction** | For every decomposition W_T = Pos_S + Δ_T in P_T with Pos_S ≥ 0 local and every P = "‖Δ_T‖ ≤ e^{o(T)}": if Δ_T is defined from the source (Γ, δε_p), P is invariant under X↦M_m (blind); if it is defined as W^X − Pos_S, its lower half Q is ⟺ RH (E1). There is no third option except the explicit formula (identity with no sign) | 2A 1H 7B 8F 4D, and every Sonin/CC route | R184_015 Thm 2, Cor 3 (PROVED); reinforces W11 |
| **W-Sonin (gap requirement)** | Every positive-part multiplier with bounded inertia remainder ∀T has a limiting density supported on the zeros (under RH), so the Sonin/CC route carried to every T converges to the explicit formula; entire Sonin has n₋=∞ for T>½log2 | 2A 1B 1H | R183_018 Thm 5.1, R183_019 Thm 4.1, R183_031 Thm 1, R183_028 §3.3, R183_033 §5 |
| **W-factor (Lemma AC + Theorem F)** | An Euler factor with multiplicities ≥0 has no zeros to the right of its abscissa; if P = B⊔Q is exact with θ<1, Q has abscissa ≤θ and contributes no zeros in Re s>θ. Multiplying ℕ by a factor never produces zeros outside, ∀θ<1 | 5G | R184_008 §1–2 (PROVED) |
| **W-dither (Theorem D) / (1−θ)/2 ceiling** | In the linear model there exists a rounding with sup\|T₁\| ≪ x^{(1−2a)/4}: linear L* is false. In the full system the composites do not diffuse and the exponential method does not go below (1−θ)/2. Every "rounding + Perron" route for θ<1/3 stops there | 5G | R184_010 Theorem D, Cor 1–3; R184_013 Cor 3.2; audit R184_093 |
| **Erratum (not a wall; goes to §5/§8)** | R164_201 §1 and R184_001 §1/§1.3 row 1: chaos of order k≥2 and Witt levels k≥2 are **not** negligible (same power X^{1−2a} at every order). Theorem L and the exponent (1−θ)/2 do not change | 5G | R184_014 A1–A6 (PROVED), R184_093 |
| **(note) blind inertia** | The inertia of W_T, its monotonicity and the prime-to-prime Schur chain are blind to the class: M_m satisfies all of it (rank ≤6m); a valid 𝒜 would imply κ(ζ)=∞. It is an instance of W3/W-identification; it may be registered inside W3 | 4D 7D 7E 8F | R184_004 Cor 5 (PROVED, not conditional) |

## 6. Falsifiers to be added in §4

| model | shares with ζ | refutes | file |
|---|---|---|---|
| **ℕ ∪ √2·ℕ** (and θ=0 root-substitution systems: ζ(1+2^{−s/2}), N=⌊x⌋+⌊x/√2⌋) | discrete Beurling, N = ρx+O(1) (θ=0), zeros of ζ at σ>0 | the set-theoretic version of C1 ("{n_k} ⊂ finite modification of (1/c)ℕ"); the O(1)-window Diophantine route (N2) | R184_005 N1/N2; R163_102 Lemma S |
| **relaxed class R = L(u,χ)** (\|ε_p\|=1 ≥ ‖p^a‖, ε bounded at every Witt level, no integrality) | polynomial growth of ζ_𝒫; error N_𝒫−cx ≪ x^{max(2/5,(1+θ)/3)+ε} < x^{(1−θ)/2} for θ<1/5 | every proof of L*_comp that uses only size bounds of ε_p: requires ε_p ≡ −p^a (mod 1) | R184_014 Prop B.3, Cor B.3′ |
| **low band (zero gap (−γ₁,γ₁))** | — | (L-Son) with η uniform in T; C_T ∀T with no null density in the gap (CONDITIONAL(RH), which suffices by the §3 argument, 2A) | R183_027, R183_028 §2 |
| **θ=2/5 countermodel of R171** (discrete, N=cx+O(x^{83/208}), zeros at Re s=11/16) | prime and integral integrality, deterministic | every discrete rigidity with θ₀>2/5; confirms BFdisc (R163_803) | R171_FINAL (not merged) |

## 7. Corrections to §6 (item 59) and other grid texts

- Remove from "never attempted": prop:polarcap (R160_M4_R1, R162_703, R184_012), LP-152 (R160_M5_R1), G2_B7_R5 (→ (Q*), NO-GO as a route, R184_011), R161_073–074 (E1, R184_012). I11, I14, Cayley-69 and I14/Request 122.A move to "no statement," they are not routes.
- Item 23 / 1H (P122_D_SPECIFICATION) and item 30 / 8C (O-151.4): **DONE**, negatively (R168_202).
- Item 33/58 (web hit): cannot be closed without web access. Left out of 3A's live-route count.
- O202.1 (6C): DONE as a statement with no route.
- Phase 170 residual: OPEN-empty under RH; NO-GO route [W12+W5], E1 closure (R184_002, R184_091).
- (P153.4) closed since R153_010 and (P153.5) quantified (R184_006/007): they are not residuals of 4E.
- Editor's pending task: merge phases 168–182 into the JSON (part 19) before applying this proposal, and recount.
