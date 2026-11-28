# R160_S4 — Survey S4: row D, phases 134–156, Papers 46–47, ABCD-CLOSURE-PLAN

Surveyor S4 of five, phase 160 (`R160_000_BLUEPRINT.md`). **Survey only: no new theorem,
no label change, no computation run.** Every statement below cites a file of record. Labels are those of the cited
file; where a surveyor comment is added it is marked *(S4)*. Form convention (rule (d)):
**[prim]** = the primitive form `𝔞_T = A_T|P_T` (bottom `λ^A_T`, and its relaxation `λ^P_T ≤ λ^A_T`);
**[compl]** = the complete form `W_T` on `L²(I_T)` (bottom `λ^W_T`). Always `λ^W_T ≤ λ^P_T ≤ λ^A_T`
(P46 `rem:Kprim`, `main.tex:451–456`). **[frame]** = a statement about Paper 47's intersection-theoretic frame
(`I_∞`, `h⁰`, cones), whose target `I_∞(F,F) ≤ 0` on primitive `F` is the [prim] sign (P47 (1.9)–(1.10),
`main.md:155–165`). **[meth]** = a method constraint (a statement about derivations, not about `ζ`).

Scope read: every `README.md` and every closing decision of phases 134–156 (incl. all nine closing decisions
of phase 155 and the four of phase 153), the phase-136 synthesis and note, Paper 46 `main.tex` §§1–11 and
App. B (all labelled statements), Paper 47 `main.md` §§0–1, 11.1, 11.7, 12.3, 17–23 (statements), 18.13–18.16,
19.17, 19.25, 21.8, 22.17, 27.3, 27.10–27.11, 28 in full, and all files of
`05-meta-and-planning/ABCD-CLOSURE-PLAN/` (PLAN.md skimmed by headings; the rest read).

---

## §1 What was done (one line per phase/paper)

| phase / doc | what it did | files of record |
|---|---|---|
| 134 opening | Paper 47 Part I: `Π` bijection onto primitive class (Lemma 3.1); `Λ(g) = 𝔏(g⋆g^†)`, `𝔏 = −Π²(W_fin+ω_∞)` (Thm 3.6); RH ⟺ a unitary rep. with `Λ(g) = ‖π(g)Ω‖²` (Thm 3.7, RESTATEMENT); swap law for `Σ(T)`; Thm 5.8 finite inertia uninformative; requirement list (R1)–(R5); falsifier suite | `phase-134-row-d-opening/R134_007_CLOSING_DECISION.md` |
| 135 canonical class | Weil class `D^W`; canonical class `K` = Pólya kernel (`Φ_K = ξ`); radical `𝓝_∞`; affine duality `σ_K`; **Hodge-index transfer theorem 12.3** (conditional on an `h⁰`); `Ξ_a` falsifier theorem; `h⁰_Z` candidate | `phase-135-row-d-canonical-class/R135_007_CLOSING_DECISION.md`; P47 Part II |
| 136 map | ~200 mechanisms of phases 0–135 classified into clusters A–E; meta-theorem "sign = polar/Frobenius coupling, phase coherence of unimodular roots"; squares S1–S7; no-gos reopened | `phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md`, `NOTE_OFF_THE_PAGE_CANDIDATES.md`, `MAP_1…5` |
| 137 canonical coupling | phase-65 `RH-PROOF.md` REFUTED (the "fork"); growth of `h⁰_Z(mK)` `≫ (log m)^{3/2}`; D.12 semilocal (acceptance test D.12-α posed); D.13 CC dictionary (`Q = Π`) | `phase-137-…/R137_007_CLOSING_DECISION.md`; `NO-GO-LIST.md:585–650` |
| 138 detecting cones | `D^W = Λ ⊥ P^W` (Thm D.15.1); polar block satisfies Hodge identically; Landau triangle criterion `RH ⟺ W(h_T) ≥ 0 ∀T` (Thm D.17.2); equimodularity separates `ξ` from `Ξ_a`, ceiling `ζ_K` | `phase-138-…/R138_005_CLOSING_DECISION.md`, `README.md` |
| 139 two falsifiers | Epstein class `K_Q`; Hodge index fails for `Ξ_Q`; **T2** (axiom list A1–A9); field-uniform frame (T1 setting); (P139) construction problem | `phase-139-…/R139_005_CLOSING_DECISION.md` |
| 140 Frobenius square | `Frob_𝔫` over every number field (O-9); three Gram forms; tensor square `h⁰_□` has growth `(r²/4)m²` but no bidegree-function satisfies (b′) (D.24.7, D.24.11) | `phase-140-…/R140_005_CLOSING_DECISION.md` |
| 141 Frobenius traces | `ker T = 𝓝_∞`; moment cone `𝔐`; `h⁰_RR⁺` with (a),(c) unconditional; row D reduced to the clause (b′)⁺; O-18 | `phase-141-…/R141_005_CLOSING_DECISION.md` |
| 142 the clause | **frame defect theorem** D.31.12 (no `h⁰` with (a),(b′),(c), given (X19)); `s_1 = 0.99846…`; (C4.1) false; Horns A/B | `phase-142-…/R142_005_CLOSING_DECISION.md` |
| 143 trace cone | `s_* = s_1` certified; (T1′) `B4 ∩ P^W ⊆ 𝓝_∞`; unconditional transfer thm 12.3-B4; `(b′)_{B4} ⟺ RH` | `phase-143-…/R143_005_CLOSING_DECISION.md` |
| 144 fixed index | `(P_m) ⟺ RH` at every fixed `m`; one ray `tF+dK` refutes six weakenings; trace-cone route closed | `phase-144-…/R144_005_CLOSING_DECISION.md`; `ABCD/ROW-D-SYNTHESIS-PHASES-135-144.md` |
| 145 function-field model | the frame on `E/F_2`: frame defect holds where RH is a theorem (`s_C^* = √(7/11)`); bigness clause ⟺ RH (Prop D.42.5); (P145′) | `phase-145-…/R145_005_CLOSING_DECISION.md`; P47 §21 |
| 146 coupled pairing | degree form on `Z⟨Frob_n⟩` zero-blind, indefinite; computed Frobenius diagonal (`P(m)=P(n) ⟹ δ_m=δ_n`); single-prime tower = magnitude only | `phase-146-…/R146_005_CLOSING_DECISION.md` |
| 147 Galois ring | `Z[G]` supplies a `+` on the packet-graded carrier but the `χ=1` slot is exactly `𝓔^∞` (Thm D.55.9′): inert at `ζ` (`phase-147-row-d-galois-ring/single-prime-tower-corpus-check/` holds only `CORPUS_CHECK_R147.md`) | `phase-147-row-d-galois-ring/R147_005_CLOSING_DECISION.md` |
| 148 mixed effectivity | mixed effectivity = tropical condition; vacuous or infinite (D.56.4′); O-148.2 | `phase-148-…/R148_005_CLOSING_DECISION.md` |
| 149 additive pencil | Deligne route over `Z`: extraction D.59 (a Hölder inequality), kill test `c = ½`, `κ(d) = d/φ(d)`, "exponents add/subtract"; (P149) = `k`-tuple conjecture | `phase-149-…/R149_005_CLOSING_DECISION.md`; `ABCD/STATE-AT-PHASE-149.md` |
| 150 method theorems | **T5 PROVED**; T4 → polar/entire classification (classical); T3 conditional on (H-DMV) | `phase-150-…/R150_005_CLOSING_DECISION.md` |
| — decision | **row D closed in the map**; Paper 47 Part IV §§24–28; six-clause reopening criterion §28.4 | P47 `main.md:12611–12654`; `ABCD/ROW-D-CLOSURE-PLAN.md` |
| 151 the bridge | T6: nonnegative families give no a-priori pole; new Lemma 2.4 (ascent `σ_{2k} ≥ 2kσ_2`); axis "summand vs numerator" (O-151.4) | `phase-151-…/R151_005_CLOSING_DECISION.md` |
| 152 new approach, round 0 | FUP/Dolgopyat and Berkovich–Poineau: Prop A.4, Prop B.3; (P152.1)–(P152.3) formulated; "no route, no impossibility" | `phase-152-…/R152_005_CLOSING_DECISION.md` |
| 153 sign-carrying endpoint | **Theorem A** (`Ξ_a` form = cross term of two `ξ` forms); **D.12-α PROVED** at `({∞,2,3}, log 2)`; rounds 3–6: single pair, needle, decay law, symbol-level `Φ_N`, body vs box — all negative or diagnostic | `phase-153-…/R153_005`, `R153_010`, `R153_014`, `R153_017`, `R153_021` |
| 154 law of the body | dual-certificate theory: Thms A (Lévy energy), S, W, **O, D1, E**, Prop P (`β₀ = 2`); **Theorem C** (`½log3`, 437 atoms); tail lemmas F1/T/Hybrid; V′ (log exchange); K; literature reading → Paper 46 | `phase-154-…/R154_012`, `R154_021`, `R154_023`, `R154_030`, `R154_031` |
| 155 flat-kernel criterion | 8 rounds + reverse track: TK/N/N′ class ceilings, B, SC, R, Lemma R, finZ, Theorem D (decay tail), archimedean thresholds, Schur reduction, `W_{log2}[F*]`, E₇ nest, Li dictionary, Kreĭn = RH, Thm J, arena, Thm P, AL retracted → AL′, P6 = equivalence, D-HS killed, margin decays, **(H1) proved at log 2**; PATH-TO-D synthesis | `phase-155-…/README.md` and `R155_003/010/018/029/038/043/046/051/060`; `R155_031` = `ABCD/PATH-TO-D.md` |
| 156 per-window converse | parity–Schur identity, polar capacity `𝔊_T`; converse fails in comb models; `T*_∞ ≤ 0.4608`; residual R1 of frame defect closed (Cor 19.25b) | `phase-156-…/R156_005_CLOSING_DECISION.md` |
| **Paper 47** | Row D: the sign, Parts I–IV (§§0–28): frame, transfer theorems, T1/T2/T5, frame defect, classification, wall §28.2, reopening clauses §28.4; §§28.3a/b add phases 157–158 | `04-papers/47-intersection-frame-defect/archive/main.md` (12 687 lines) |
| **Paper 46** | Dual theory of Weil positivity at finite support (84 pp.): §§2–11 + App. A–C | `04-papers/46-row-d-sign-radial-intersection-form/main.tex` (5 182 lines) |
| ABCD plan files | PLAN.md (history →09-22), PLAN_PRIORITARIO (09-08), FIRST_CAMPAIGN, CORPUS_COVERAGE, CORPUS_CHECK_ROW_D_PLAN (8 inputs vs phases 0–138), ROW-D-COMPLETION-PLAN (139–143), ROW-D-MAP-b (ASCII), ROW-D-SYNTHESIS-135-144, HANDOFF-149, ROW-D-CLOSURE-PLAN-09-19 (Laumon/FUP/Mayer, 57-route catalogue §7), PATH-TO-D-09-22, **ROW-D-REDUCED-STATEMENT-09-23** | `05-meta-and-planning/ABCD-CLOSURE-PLAN/` |

---

## §2 What FAILED, and exactly why (do not repeat)

Grouped by mechanism. Each line: *attempt* — **killer** (label) — file.

### 2.A The intersection-theoretic frame (Paper 47; phases 134–148) — all [frame]

1. *A nonnegative invariant of "norm" type built inside rows A–C, with a duality preserving primitivity* — (R5): the only
   duality rows A–C construct (`†`) preserves the primitive sector, so the requirement list is vacuous (PROVED) —
   `R134_007` §2 item 1; P47 Def 6.8.
2. *Finite inertia of the smeared Frobenius Gram at small `ε`* — Thm 5.8: archimedean diagonal dominates, uninformative,
   for `ζ` and `Ξ_a` alike (PROVED); D.3 retired — `R134_007`.
3. *`h⁰` via the transfer theorem 12.3 (any `h⁰: D^W → R_{≥0}` with (a),(b′),(c))* — **Frame defect theorem** P47
   Thm 19.25 (`main.md:6407`): unsatisfiable for `ξ` for every `χ`, given (X19) (simplicity of `ρ₁` load-bearing);
   holds also on `C_c^∞ ⊕ RK`, `P_c^∞ ⊕ RK` (Cor 19.25b, `main.md:6510`, phase 156); and **on a curve over `F_q` where RH
   is a theorem** (Thm 21.15, `main.md:9038`) — so the defect is of the cone, not of the zeros. Deficit constant
   `s_1 = 0.998460…` (Lemma 19.17 `main.md:6218`, Prop 19.18) — `R142_005`, `R145_005`.
4. *`h⁰_Z` (Frobenius-lattice count)* — satisfies (a),(b′), growth only `(log m)^{3/2}/log log m` vs required `¼m²`,
   fails (c) (PROVED) — `R137_007` §1; P47 Thm 18.28.
5. *Any `h⁰` factoring through the bidegree / through pairings with `r(Div_□)`* — D.24.7, D.24.11 (P47 Thm 19bis.19,
   19bis.22): (b′) fails, explicit witness (PROVED) — `R140_005`.
6. *2-homogeneous trace functionals `Ψ(t_n)`* — D.27.5: (A) fails (b′); (B) (c) ⟹ RH (PROVED) — `R141_005`.
7. *The clause (b′)⁺ (and stable form), `χ > 0`, (C4.1)* — all REFUTED (D.31.9, D.30.7, Thm 19.22) — `R142_005`, P47 §23.3.
8. *Trace-positive cone B4 and all its weakenings* (defect, primitive gate, fixed index `(P_m)`, sparse `{t_{2^k}}`,
   head/tail, bounded density, O-30) — each ⟺ RH or refuted by **one ray `E_t = tF + dK`** with frozen frame
   invariants (P47 Thm 20.37; §D.40 of `R144_001`) (PROVED) — `R144_005`. Final form Restatement 20.30 (`main.md:8308`):
   RH ⟺ `I_∞(E,g_λ) ≥ 0` on `S_0` (EQUIV).
9. *Detection from the polar block / ruling datum* — Thm D.15.3: Hodge identity holds on `Λ = span(K,K_odd)` with slack
   `½μ²`, no detection (PROVED) — `R138_005` §1.2.
10. *Pólya cone as sign source; Khovanskii–Teissier on effective cone; "translation is the operation"* — PNT error term
   (D.17.3, route no-go `phase-114/114_d_185`); `C_Pó ∩ C¹ = {0}`; translation REFUTED (D.16.1) — `phase-138/README.md` "Routes stopped".
11. *Equimodularity `|p−½|` as the sign* — ceiling: every `ζ_K` is equimodular (T1) (PROVED) — `R138_005`; P47 Thm 17.22, Rem 17.24.
12. *Axiom-only derivations (A1–A6 + A2⁺)* — **T2** (P47 Thm 18.16, `main.md:5328`): Epstein `Ξ_Q` satisfies them and
   fails Hodge index; any proof must use A3 **and** one of A7/A8/A9 (Siegel price on A9) [meth] — `R139_005`.
13. *Bigness clause "`D²>0, D·H>0 ⟹ D` effective"* — ⟺ RH (Prop D.42.5 = P47 Prop 21.21) (PROVED, EQUIV) — `R145_005`.
14. *Additive structure on `{Frob_n}` (the `+` of `Z[π]`)* — `Spec Z` terminal, no `Z[π]` (P47 Thm 22.17 `main.md:10089`);
   formal form on `Z⟨Frob_n⟩` = `2ab − W` minus zero sum: zero-blind, indefinite, `Ξ_a`-uniform (Thms 22.3–22.4);
   single-prime tower is magnitude only (D.47.4) — `R146_005`.
15. *Galois group ring as the `+`* — radial collapse `R(Γ_σ) = id` (Lemma 24.1); graded carrier `χ=1` slot `= 𝓔^∞`
   exactly (Thm D.55.9′ = P47 Thm 24.10); defect unchanged (PROVED) — `R147_005`.
16. *Mixed effectivity `Φ(y/x) − φ(x)ψ(y) ≥ 0` on the full square* — tropical `Φ ≥ φ⊛ψ`; for nonnegative factors ⟹ `Φ ≥ 0`;
   signed factors make the (T)×(R) block infinite (D.56.3′/D.56.4′; P47 Thms 25.6–25.7) (PROVED) — `R148_005`.
17. *Pólya realization `r(Frob_n) = τ_{log n}(2K)`* — collapses mod `𝓝_∞` to `NS(P¹×P¹)` (rank 2), deletes the weights (D.23.4–6) — `R140_005`.
18. *D-HS (fibrewise CC `h⁰` on the S-square with Frobenius transport)* — **killed three ways** (Thm 19.25 on `D^W`; radial
   collapse `h⁰ = O(m)`; Lemma 3 (b′)-failure) (PROVED) — `R155_054`, audited `R155_057`. Tensor-square reading already
   refuted in phase 140 (D.24.10).
19. *Phase-65 `RH-PROOF.md` (uniform renormalized `P`-family + Vitali/Montel)* — REFUTED: the "fork" (bound on `G_P^∘`,
   identification only on the trace `M_P`); no-go pattern recorded — `NO-GO-LIST.md:585–650`; `R137_007`.

### 2.B The Deligne / family route (phases 149–151) — [meth]

20. *Deligne extraction over `Z` on the additive pencil* — D.59 is a Hölder inequality `‖·‖_∞ ≤ ‖·‖_{2k}`, `Ξ_a`-uniform;
   kill test: `H(1,c)` proved exactly for `c ≥ ½` where extraction is vacuous, open for `c < ½`; (P149) = Hardy–Littlewood
   `k`-tuples with square-root error (DOWNGRADE) — `R149_005`; P47 §26.
21. *Transport of polar/positivity structure between additive and multiplicative squares* — exponents add on one, subtract on
   the other; only sign-free moment identities transport (D.61.8–9, D.61.10′; P47 Thms 26.15–26.17) — `R149_005`.
22. *Single-fibre extraction from any `L²`-orthogonality moment* — **T5** (P47 Thm 27.3 `main.md:11586`): `𝔅^{1/2k} ≥ L`,
   trivial bound, uniformly in `k`, family size, type (PROVED) — `R150_005`.
23. *"Power saving ⟹ RH" / "smooth-regime" arguments* — polar/entire classification (P47 Thms 27.10–27.11): a partial-sum bound
   for `Λ` or `μ` is *equivalent* to the zero bound; entire-at-zeros sequences carry no zero information (CLASSICAL, PROVED);
   T4's Thm 4.7 (bilinear rank one) WITHDRAWN — `R150_005`.
24. *Any nonnegative family supplying Deligne's a-priori pole* — **T6**: abscissa `≥ 2kβ_max` (restatement of Thm 26.4 +
   Cor 27.10a); the axis is summand vs numerator; dlVP depth `1/log γ` fixed by the archimedean sea — `R151_005`.

### 2.C Non-positivity mechanisms (phase 152)

25. *Branch-sum Dolgopyat for the Gauss map* — Prop A.4: abscissa `Re s = ½` ("MW-2 in dynamical form") (PROVED);
   FUP gap `β > ¼` defeated by density, `β = ¼` is RH (Prop A.2) — `R152_005`.
26. *Tree potential theory on `M(Z)`* — Prop B.3: per-branch, blind to cross-place coupling (PROVED, scoped to trees) — `R152_005`.
   (The line version (P152.2) was closed as a restatement in phase 157, P47 §28.3a; `rem:normline` P46 `main.tex:1274`.)

### 2.D Finite-window and dual methods (phases 153–156; Paper 46)

27. *Single off-line pair detection for `ζ` (P153.5)* — at short support it measures Weil-mass concentration, excludes
   only what Platt–Trudgian already excludes; `γ_0^max` cut-off does not exist (CLOSED negative) — `R153_010`.
28. *The `b`-needle (P153.4)* — an even/odd eigenvalue crossing drifting with `T`; "arithmetic contact" reading WITHDRAWN — `R153_010`.
29. *Slepian/origin-gap prediction for the decay rate* — REFUTED (`c = 75.8` vs `27.6`); no term-by-term bound on `c(T)` — `R153_014`.
30. *Hand proof by uncertainty on the symbol wells; soft (pointwise) minorants* — budget `2Tτ_*/π` vacuous at both endpoints;
   Bochner forces any pointwise minorant `≥ 0` — `R153_017`.
31. *Projection-only arguments (Ingham, Boas–Kac, `cos(π/m)` box)* — Lemma 3.1 (PROVED): box deficit `−1.278` vs truth
   `+1e−7` in the `w_ζ` direction; cannot reach Weil positivity at any `T` — `R153_021`. "Weights at the band edge" = `λ ≈ 0` restated, WITHDRAWN.
32. *Certificate as an identity / closed-form exact dual* — **Theorem O** (P46 `thm:O`, `main.tex:665`): no finite `ν` and no
   finite family of continuous multipliers attains the dual, even with `v = 0` [prim]; complete-form version `lem:Onat`
   (`main.tex:3757`) [compl] (PROVED).
33. *Mass-based / radius-based rate lemmas uniform over the feasible set* — **Theorem V′** (P46 `thm:Vp`, `main.tex:1128`):
   exchange exactly `Θ(log R)` [prim] (PROVED); Remark P3exp: `R(ε,η)` exponential in `1/η` is forced.
34. *Pointwise-envelope closing arguments* — `prop:env` (`main.tex:1170`): `A_T` is the exact sup of the comb, threshold
   `2πe^{A_T}` cannot be lowered, `A_T ∼ 4e^T` (doubly exponential) (PROVED); = Zhu Thm 1.4 barrier.
35. *Clustered atoms; `M_crit` calibration; "incommensurability of log 3 with log 2 lattices"* — clustering 4× worse
   (DIAGNOSTIC, `R154_023`); calibration REFUTED; incommensurability hypothesis REFUTED (F1 works for any finite contact
   set, `R154_016`) — `R154_021`, `R154_030`.
36. *Lattice certificate classes of small order* — **TK** (P46 `prop:TK`, `main.tex:1955`), **Theorem N** (`thm:N`, `:2068`):
   no lattice of step `2T/M`, `M ≤ 8`, certifies at `½log3`; **Theorem N′** (`thm:Np`, `:2136`): none with `M ≤ 24` at
   `T = 0.68` or `log 2` (`Ceil(24,log2) ≤ −6.584323·10⁻⁷`) [prim] (PROVED machine-verified). *Scope:* lattice-supported
   `ν` only; **not** flat-top classes (`R155_012`: applying TK to flat-top weights is a category error).
37. *Reverse engineering from the zeros (zero-side LPs; "D for 1000 zeros"; 103-window regime law)* — zero-side LP profile
   negative at all 103 windows (effective order `M ≈ 4.4` inside Thm N's empty class); **thm:finZ** (`main.tex:1488`): no
   finite symmetric zero multiset carries a flat-top certificate; `thm:finDet` (`:1434`): finite `Z` is determinate;
   `cor:infinite` (`:1537`) [compl] (PROVED). Bounded-profile P3 and comb-vanishing LP negative on `ℝ` (DIAGNOSTIC) —
   `R155_010`, `R155_018`.
38. *Termwise positivity in the zeros* — **Lemma R** (`lem:Rrig`, `:1374`): no flat-top `w` has `ŵ ≥ 0` [compl] (PROVED);
   `cor:nontermwise`.
39. *Li–Keiper / Báez-Duarte as flat-top dual certificates (P4)* — `cor:Li` (`:4881`): Li kernel `w_n = −½e^{−|u|/2}L_n'` is
   outside `𝒲_T` for all `n, T` (three reasons), `λ_n` is only the zero-sum half; Li analogue of SC fails (`rem:LiSC`);
   Nyman–Beurling HEURISTIC; **P4 CLOSED** — `R155_038`.
40. *Positivity prime by prime / from a sub-comb* — **Theorem SC** (`thm:SC`, `:2184`): any nonnegative sub-comb of mass
   `A < −C₀ = 5.3721834` is negative on `P_T` for `T > T_0(A)` [prim] (PROVED); each local `Q_p` indefinite (`cor:Qp`, `:3431`).
41. *Classical prime-side hypotheses deciding a window* — **thm:finmod / cor:void** (`:3452`, `:3563`): deletions/amplifications
   of `Λ` keep `a ≥ 0`, `ψ` up to a constant, every zero and the pole (`ζ_a = ζE`), and fail `RD_T`; hence PNT with any
   error, zero-free regions, zero density, sieve bounds decide **no** window `T > ½log2` (upper-bound sieve: `T > 0.74921`)
   [prim][meth] (PROVED) — `R155_053`/`R155_058`.
42. *P6: an arithmetic lower bound on the alignment band* — CLOSED as an equivalence: per window `[∃w: Al_T(w)] ⟺ λ^W_T > 0`
   (`thm:Al`, `:3772`); `∀T ⟺ RH`; the band alone does not decide (`prop:negtrace`) [compl] — `R155_053`, `R155_060`.
43. *Problem A on the archimedean form alone (P1)* — structural negative: `thm:O` holds with `v = 0`; in `(D_∞)` sampling is
   free (Theorem AL of `R155_033`), so the deficit is the continuous edge problem (PROVED) — `R155_038`. *See §5 item 3 for
   the part of this reading later withdrawn.*
44. *(H1) by Birman–Schwinger / CLR* — `M₊` gapless, `tr M₋ = 4.495774·T`, CLR unavailable in `d = 1` (CLOSED negative);
   Jensen on concave `φ` gives only ceilings (Thm J′ REMARK) — `R155_043`; P46 `main.tex:2987–3000`.
45. *Nodal / Sturm criterion for the full even Schur complement (P8)* — `K` completely monotone ⟹ log-convex ⟹ not PF₂,
   Karlin unavailable (`rem:PF2`, `:3076`, kernel only; semigroup `t ≥ 1` OPEN); log-slow gaps (`thm:arena`) ⟹ nodal rule
   loses margin; **P8 CLOSED as a route** — `R155_046`.
46. *Any fixed finite truncation of the archimedean basis* — **arena** (`thm:arena`, `cor:arena`, `:3012–3064`): `N*(T) ≥ 12`
   even modes at `log 2`, `N* ≥ exp(4e^T(1+o(1)))`; no fixed truncation decides `S_even` [prim, prime-free gaps] (PROVED) — `R155_046`.
47. *Prolate two-value relaxation to reach `n₋ = 1`* — Thm P gives `n₋ ≤ 5/7/8`; Remark P4: exact count already 5 at optimal
   `τ₁` at `log 2` (PROVED for two-value only); Problem A via uniform floor does not follow (flat top is the near-`λ₀` concentrator) — `R155_051`.
48. *Kreĭn indeterminacy as a removable obstruction (P5)* — `thm:KEP3` (`:1753`): RH ⟺ KEP(T) indeterminate ∀T;
   indeterminacy is RH, not a lever; `Thm C` does **not** give complete-form indeterminacy (`β ≠ (2,0)`) [compl] — `R155_043`.
49. *Uniform margin / upward induction in `T`* — `thm:margin` (`:3277`): `λ^A_T ≤ 4·10⁹Te^{−15.449T}` for `T ≥ 1` under
   (X19),(X19′),(X-N); `cor:margin2`: no uniform `c > 0`, RH ⟺ `lim λ^A ≥ 0`; `lem:monoT`/`cor:mono`: monotone, no induction
   [prim and compl] (PROVED) — `R155_055`/`R155_059`. Route A: on primitive tests the comb **is** the Chebyshev remainder
   (`rem:Cheb`, `:4143`): prime-side decay proofs are zero-side statements.
50. *Per-window converse `λ^A ≥ 0 ⟹ λ^W ≥ 0` as a structural (comb-class) fact* — `cor:convfail` (`:3996`): fails for
   `Λ·1_{n≥5}` on `[0.4608, 0.58]` and for `θΛ(2)`, `θ ≤ 0.8148`, at `½log3` (PROVED, comb-level) [meth] — `R156_005`.
51. *Lattice sampling of flat-top certificates free to all orders ("the lattice is never the deficit")* — **thm:AL of round 4b
   RETRACTED** (wrong density, hypothesis contradicting `def:W`); replaced by AL′: loss exactly `Θ(1/M)`,
   `E_edge = (4/π)cosh T·d` (`thm:AL`, `:2346`, as now printed) — `R155_049/050`, `R155_051`.
52. *Any numerical value of `inf W_{log2}|P_T`* (e.g. "≈10⁻⁶", "≈10⁻⁷") — WITHDRAWN: Galerkin bottoms unstabilised
   (`rem:galerkin`, `:4244`) — `R155_038`.
53. *Hilbert–Pólya, Laguerre–Pólya/Jensen/Turán/Li, window extension past log 2 as a route, magnitude methods* — standing
   no-gos not reopened (cluster A/B/D of phase 136; `MAP_1`) — `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md` §1, §5.
54. *Laterals discarded at plan level* (Taylor–Wiles = phase 147 in disguise; Kudla; Lee–Yang; Kesten/Ramanujan graphs;
   Maass–Selberg/Eisenstein reaches only `Re s = 1`; Rankin–Selberg→Ramanujan bounds local parameters) —
   `ROW-D-CLOSURE-PLAN.md` §4 "Descartados"; §7 has the compressed 57-route catalogue.

---

## §3 What still STANDS

### 3.1 Proved results of record (label, form, file)

**The sign for ζ (the only sign statements):**

| statement | form | label | source |
|---|---|---|---|
| `λ^A_T ≥ 0` for `T ≤ log 2` (Feshbach capacity margin `8.63·10⁻⁸`, not an L² bound) | [prim] | CITED (Paper 42, interval-certified) | P46 `main.tex:148`; `R153_005` row `λ_min`; `ABCD/ROW-D-REDUCED-STATEMENT` §3 |
| **Theorem C**: `λ^A_{½log3} ≥ λ^P ≥ 8.8577·10⁻⁵` (437 atoms, `β = (2.00256,−0.00965)`) | [prim] | PROVED (machine-verified) | P46 `thm:C` `main.tex:1025` |
| `λ^W_T ≥ 0`, `T ≤ ½log2` | [compl] | CITED (Yoshida 1992, Bombieri 2000) | P46 `main.tex:149–151` |
| `λ^W_T ≥ 8.9·10⁻¹⁸ > 0`, `T ≤ 0.8` | [compl] (hence [prim]) | CITED, not re-verified (Zhu 2026 Thm 1.2) | P46 `main.tex:316–320`, `cor:KEP08` |
| `T > 0.8` | either | **nothing** | `ROW-D-REDUCED-STATEMENT.md:53` |
| Rule: "`T ≤ log 2`" is primitive-form only | — | CORRECTION (R156_004 A14) | same, `:55` |

**Sign-carrying / separating theorems (no sign for ζ beyond the table):**
* **Theorem A (phase 153)** `A_T^{(a)} = E_{−a}A_TE_a + E_aA_TE_{−a}` ⟹ `⟨A_T^{(a)}F,F⟩ = 2[⟨A_Tu,u⟩ − ⟨A_Tw,w⟩]`,
  `u = cosh(at)F`, `w = sinh(at)F` — the falsifier's form is a cross term — [prim] PROVED — `R153_005` §1.
* **D.12-α** at `(S,T) = ({∞,2,3}, log 2)`: `ξ` form `≥ 0` on `P_T`, `Ξ_a` form `< 0` on `P_T^{(a)}`, `a ∈ {0.30,0.45}`
  (400-bit intervals) — [prim] PROVED, conditional on Paper 42 — `R153_005`.
* Theorem 4.1: `A_T^{(a)} = 2A_T + a²D_T + O(a⁴)` in operator norm — PROVED — `R153_014`.

**Dual theory (Paper 46; phase 154–156):**
* `thm:S`/`lem:K` (`:363–407`): `m(τ) = C₀ + ∫(1−cos τu)K`, `K = ½/sinh + ½/cosh` completely monotone; `φ` complete
  Bernstein; pure-jump subordinate BM — PROVED.
* `thm:A` (`:416`): `𝔞_T(F) = C₀‖F‖² + 𝔈(c_F) − Σv_n c_F(log n)`; `λ^P = C₀ − Λ_T` [prim] — PROVED.
* `thm:D1` (`:601`): strong duality `D_T = λ^P`, finitely atomic certificates; complete-form version with `β = (2,0)` (remark
  after proof) — [prim]/[compl] PROVED. `thm:E` (`:975`) exponential columns exhaust. `prop:P` (`:727`): `β₀ = 2` unique
  polar multiplier for `W_T`.
* Tail lemmas `lem:F1`, `lem:T`, `lem:hybrid`, `thm:Dtail` (`:894`, `:933`, `:961`, `:1829`), `cor:comb` (τ_stop polynomial
  in `D(w)` for comb-vanishing `w`) — PROVED; the union of graded + decay techniques OPEN.
* **thm:Z** (`:1234`): certificate = explicit formula on `w(u)cos τu`; `f_w(τ) = Σ_ρ ŵ(τ−γ_ρ)` [compl] — PROVED.
  `thm:Zexh` (`:1297`): `sup_w inf f_w = λ^W` [compl], with `β` correction `= λ^P` [prim]. `cor:RH` (`:1328`) EQUIV.
* KEP: `def:KEP`, `lem:polar`, `thm:KEP1–3`, `cor:KEP08` (unconditional indeterminacy `T ≤ 0.8`, via Zhu) [compl] — PROVED (EQUIV).
* Class results: `prop:TK`, `thm:Bbeta`, `thm:N`, `thm:Np`, `thm:R` + `cor:R3` (ceilings converge to `λ^P`), `cor:CP`
  (no uniform rate; `O(K(log M)^{−δ})` on a sub-family), `thm:P3` (concentration radius) [prim] — PROVED.
* Structure of the archimedean form: `prop:arch`, `prop:nodes`, `lem:strict`, `cor:Tarch` (`0.58 ≤ T*_{∞,P} ≤ 0.60`,
  machine-verified), `prop:archneg` (`T*_∞ ≤ 0.4608`), `prop:NC`, `thm:P`, `thm:J`, **`thm:index`** (`n₋(A_∞|P_T) = 0/1/2`,
  machine-verified), **`cor:H1`** ((H1) holds on `(T*_{∞,P}, log 2]`), `thm:arena`, `cor:arena` [prim, prime-free] — PROVED.
* At `log 2`: `thm:w11` `W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]` (one direction); `thm:nest` `W_{log2} ≻ 0` on
  `E_7 ⊂ P_T` (`λ_min ≥ 6.5687·10⁻⁶`) [prim on finite subspaces; `F* ∈ P_T` so `W = 𝔞` there] — PROVED (machine-verified),
  **not a sign for the form**. `prop:schur`, `prop:bprime` (Schur coupling is purely prime), `prop:shifts` (`Π_T` non-compact,
  `‖Π_T‖ ≤ A_T`), `lem:N`, `prop:G` — PROVED.
* Finite condition per window: `prop:finite`, **`prop:uniform`** (`:3607`): RH ⟺ `∀T: v_T(Λ) ∈ 𝒱_T`, closed convex,
  Γ-data only [prim]; `prop:decide` (sign of `λ^P` decidable when `≠ 0`); `prop:band`, `prop:align` (negative set is a finite
  band; beyond `τ_a = 23.34` negativity only on alignment arcs `|k log3 − l log2| < ¼log6`) — PROVED.
* Per-window relation of the two forms: **`thm:parityschur`** (`:3814`): `In(W_T) = In(A_T|P_T) + In(𝔊_T)`;
  `λ^W > 0 ⟺ [λ^A > 0 ∧ 𝔊_T ≻ 0]`; `prop:polarcap` (`:3954`): `𝔊_T = S^Sch_T + J`, the polar capacity — PROVED.
* Margin: `thm:margin`, `cor:margin1–2` — PROVED under imports; `lem:monoT`, `lem:contT` (continuity of `λ^W`) — PROVED.

**Frame and method theorems (Paper 47):**
* `D^W = Λ ⊥ P^W` (Thm 17.5); Landau triangle criterion `RH ⟺ W(h_T) ≥ 0 ∀T` (Thm 17.14, `main.md:4420`; novelty OPEN);
  `Ξ_a` fails Hodge on effective `τ_uK_a + τ_{−u}K_a` (Thm 17.21) — PROVED [frame].
* **T1** Thm 18.1 (`main.md:4836`), **T2** Thm 18.16 (`:5328`), **T5** Thm 27.3 (`:11586`), classification Thms 27.10–27.11
  (`:11722`, `:11765`) — [meth]. T3 = Remark 27.16 modulo (H-DMV), (H-DMV) discharged at CITED (secondary) in phase 157
  (P47 §28.3 item (41), `main.md:12166`).
* Transfer theorem 12.3 (`:2744`) PROVED-conditional (hypothesis unsatisfiable, Thm 19.25); unconditional transfer theorem
  12.3-B4 (Thm 20.17, `:7876`) whose clause ⟺ RH (Thm 20.23).
* Field-uniform frame (Thm 18.18), base change additive over conjugate packets (Thm 18.20, abelian); `Frob_𝔫` over every
  number field (Thm 19bis.3); `h⁰_□` growth `(r²/4)m²` (Thm 19bis.15); computed Frobenius diagonal (Thm 22.11) — PROVED.
* Additive pencil: D.59 extraction (folklore, PROVED), `κ(d) = d/φ(d)` (Thm 26.11), Lemma 2.4 of R151 (ascent) — PROVED.
* 152: Prop A.4, Prop B.3 — PROVED.

### 3.2 Open leads never closed negatively (in scope)

Analytic / dual side:
1. **Problem A** (P46 `prob:A`, `:1937`): an explicit class-dependent deficit `D(T,d,U) → 0` with `c ≥ λ^P − D`. Only the
   upper-bound side (TK/N/N′/R) is proved; the rate of the ceilings and fixed-`M` lossiness OPEN (`cor:R3`); whether the
   *optimised* lattice class loses `Θ(1/M)` OPEN (`cor:ALdef`(i), `:2434`) [prim].
2. **Problem B** (`prob:B`, `:4375`): a flat-top `w_T` whose `f_{w_T} ≥ 0` on `[0,τ_env]` is proved from the primes below
   `e^{2T}` and the Diophantine structure of `τ log p`. It **is** RH (cor:RH); open (6) of `sec:repro`: can `w_T` depend on
   `T` only through primes outside the window? [compl].
3. Union of the graded (periodic) and decay tail techniques — `rem:Dgrade` (`:1895`): "that is where the remaining
   exponential sits". OPEN.
4. A certificate at a two-prime window `T ∈ (½log3, log 2]` in a class not covered by Thm N′ (lattice `M > 24`, hybrid
   `N ≥ 6`, flat-top): best certified `−3.1964·10⁻³` at `0.58` (DIAGNOSTIC); off-machine package
   `phase-154/scripts/offmachine/` never run (`R154_030` §3) [prim].
5. Open (2): do optimal duals converge to `β = (2,0)`, i.e. `λ^P = λ^W`? Open (5): `λ^W > 0` unconditionally for some
   `T > 0.8`? (`sec:repro`, `:4402–4414`).
6. (H1) at `0.80`; `n_odd(0.80) = 0` — OPEN (needs `τ_N ≈ 60`, off-machine) — `R155_060` §5; `cor:H1`.
7. Per window: `RD_T ⟹ λ^P ≥ 0`; the converse for ζ at `T > 0.8` (`RD_T ⟹ 𝔊_T ⪰ 0`); an **effective window shift**
   `RD_{T'} ⟹ λ^W_T ≥ 0` (comb-level needs `T' ≥ T*_{∞,P}` whenever `T ≥ 0.4608`) — `main.tex:4094–4102` — OPEN.
8. The non-degeneracy hypothesis `c_{F⋆}(log n₀) ≠ 0` and the degenerate case (`lem:degen`, `:3522`: if it occurs,
   `v_T(Λ)` maximises the concave `V_T`) — OPEN.
9. Whether `lim λ^A = −∞` when RH fails (`cor:margin2`) — OPEN. Zhu's Landau–Widom law `−log λ ≍ e^{2T}` — CONJECTURE (cited).
10. Semigroup PF₂ for `t ≥ 1` (`rem:PF2`); Conjecture N-Sturm (`R155_044/045`) — OPEN.
11. (P153.1) certified lower bound on `T*(a)`; (P153.2) finite `(S,T)` separating `ζ` from `Ξ_Q` and from a Beurling system;
   (P153.3) certified `½log5` (Galerkin bottom `≤ 3.2·10⁻¹²`, `R153_021`); (P153.11) clearing inequality; (P153.12) `O(a²)`
   motion of `P_T^{(a)}`; (P153.16) apex offset; (P153.17) prime-free closed law — `R153_005/014/021` — OPEN.

Frame / geometric side (P47 §§23.4, 28.3):
12. **O-148.2 = O-149.5 = Problem 25.13**: a kernel class on the square with a form restricting to `I_∞` on translations,
    pairing the fibre classes `f₁, f₂` finitely and non-trivially, scaling-invariant, with a degree (`main.md:12186–12191`).
13. **(36)** a class on the square carrying the **phase** datum (unimodularity of local roots, falsifier `α_± = p^{±a}`)
    (`:12192–12196`); **(P145′)** the mechanism `(𝔐,𝔈,H⁰,H²)` with (4a)–(4c) as constructions (`:9446–9480`).
14. **Horn B (R2)**: enlarge effectivity so that `C'_{F₀} ≥ G`; only B4 survived and its clause ⟺ RH; the B4 traces at `F_R`
    OPEN (`R155_057`, `R156_005`; `main.md:12206`).
15. (24) clause (iii) on `E` (structural `I_∞(F,F) ≤ ½(deg F)²` on `F ≥ 0`); (25) attribution of Thm 17.14; (26) zero-free
    ample cone; (27)/(27a)/(27b) moment cone `𝔐`; (27c) CC counting function (units problems U1,U2); (31) `s_*^{cone}`; (32)
    sufficiency half of the exponential moment problem; (33) `g ≥ 2` — P47 §23.4 (`main.md:10338–10390`).
16. (37)–(40): realizability of the graded cone; `χ ≠ 1` sectors (O-47.7); non-abelian (O-47.8); sections functor with
    `m²`-growth on `𝒟_L` — `main.md:12153–12165`.
17. (42) coefficient-blind floors of sieve/spectral mechanisms at fixed frequency; bilinear identities
    (Friedlander–Iwaniec, Heath-Brown) **"not to be presumed negative"** (Remark 27.15) — `main.md:12174–12178`; O-150.2.
18. (43) gate cells `⇐` of Thm 27.10 for Beurling and `Ξ_Q`; (44) `H(k,c)` for one `k ≥ 2` (presumed beyond present means).
19. O-151.4: summand-vs-numerator as the true axis of positivity mechanisms — OPEN (`R151_005` §3).
20. (P152.1) Dolgopyat-shape bound for the continued Mayer operator via Lewis–Zagier — formulated, no method (`R152_005` §2);
    desk-classified EXCL/EQUIV in phase 157 (outside scope; `R157_002:161`).
21. D.16-γ in its repaired form (a presentation class `𝒫` of cone conditions on the zero datum) — `R138_004` C2 — OPEN.
22. Citation gap P47 Lemma 19.20(iv) for `21 ≤ T ≲ 2·10⁴`; P47 Cor 6.2 per field (`ξ_K(½) = 0`) repaired in memo, not
    integrated — `ROW-D-REDUCED-STATEMENT` §5.

---

## §4 State of the rows

### Rows A, B, C (as far as the scope informs)
* **Row A** (Paper 43, `04-papers/43-row-a-correspondence-algebra/`): `WEIL-STRENGTH-COMPLETE` on the declared carrier (R130.005;
  A.8 amended, accepted phase 133) — `PATH-TO-D` §1.1. **Caveat of record:** clause A.5 "blindness of the Hochschild
  shadow" is **CONDITIONAL** on the continuity of the crossed-product Hochschild decomposition (Hypothesis 5.9 of LaTeX **[Update : Hypothesis 5.9 is proved (Paper 43 `prop:crossed`); A.5 is PROVED.]**
  Paper 43), not proved anywhere in the corpus; load-bearing clauses for B–D unaffected —
  `phase-137-row-d-canonical-coupling/README.md` "Record note" (lines 108–126). Standing negative: Paper 43 Thm 14.1
  (`I_A` indefinite, infinite index both sides) — P47 `main.md:40–44`.
* **Row B** (Paper 44): `WEIL-STRENGTH-COMPLETE` on the declared carrier (R131.019; B.7 amended). No sign, no zeros.
  Standing negatives: Thm 8bis.4a (pure Frobenius form `Q_fin` unsigned at every finite chart; colimit OPEN), Thm 8bis.7
  conditional on `(H_L)` — P47 `main.md:45–49`.
* **Row C** (Paper 45): `WEIL-STRENGTH-COMPLETE` (R132.007): explicit formula proved in the repository (Thm 9.4),
  comparison theorem `T_∞(Γ_{F⋆F†}) = 2Φ_F(0)Φ_F(1) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, `c = 0` derived, sufficiency of primitive tests
  (Thm 10.4). No sign — `PATH-TO-D` §1.1.
* Premise of record (blueprint §Premises 1): A–C carry **no inequality**; they are Weil's rows (a)–(c).

### Row D
* **No label, no sign.** Closed in the map; P47 §28.4 (`main.md:12611–12654`). Wall of record = T1 + T2 +
  T5 + polar/entire classification (§28.2, `main.md:12111–12138`): the sign is `ψ(x) − x ≪ x^{½+ε}`.
* **Reduced statement** (`ABCD/ROW-D-REDUCED-STATEMENT.md` §1): E1–E6 are each ⟺ RH; at a fixed window row D is
  a finite decidable condition on `{Λ(n): n < e^{2T}}` and `m` (P46 `prop:uniform`); **the entire difficulty is uniformity
  in `T`**. Obstructions §4 there: margin decays; no classical prime-side theorem decides any window beyond `½log2`; no
  finite zero set certifies; never termwise, never prime by prime; no finite truncation (arena); frame defect; duality
  without attainment; log exchange; Toeplitz ceilings; no upward induction.
* Location of the work (P46 `subsec:where`, DIAGNOSTIC reading; `prop:band`/`prop:align` PROVED at two regimes): above
  `2πe^{A_T}` done; below `2πe^{2T}` individual zeros; the band between, at alignment ordinates of `τ log p`. Past
  `T*_{∞,P} ∈ [0.58,0.60]` the archimedean form is indefinite on `P_T` (exactly one negative direction on `(T*_ev, T*_odd)`),
  so **the primes must create positivity** there (`cor:Tarch`, `thm:index`).
* Addenda §7–§8 of the reduced statement (phases 157–158, outside S4's scope): O3 single-weight flip, continuity of `λ^W`,
  T1 re-read (field-uniform proofs admissible), MW-5 reduced to OT-5′, adèle class space = restatement.
* The decision for the rows: (A) closed in the map, or (B)/(B′) continue only with a mechanism §4 does not exclude —
  must use exact `Λ(n)`, be `T`-uniform with no margin and no truncation (reduced statement §6).

---

## §5 Ideas started but never finished, or closed for a reason later removed (candidate ingredients)

1. **Theorem A as a numerator-sign mechanism.** `R153_005` §2 item 2 identifies Theorem A's `−⟨A_Tw,w⟩` as the
   operator-level form of the "summand vs numerator" axis (O-151.4, `R151_005` §1). Only the *short-support* single-pair
   version (P153.5) was closed (`R153_010` §3: "at short support it measures concentration"); the second-order expansion
   Thm 4.1 and the constrained motion (P153.12) are open. No large-`T` or `T`-uniform use of the cross-term structure was
   ever attempted. *(S4: the one proved identity in scope that carries a sign against a falsifier; it separates `ζ` from
   `Ξ_a`, not from `Ξ_Q` or Beurling — (P153.2) open.)*
2. **The rank-one Schur/Feshbach reduction is now rigorous.** PATH-TO-D P3 (`PATH-TO-D:245–257`) said: if (H1) is proved,
   "the whole low-frequency problem at each window collapses to a single scalar inequality (one pivot, one complement)".
   (H1) was HYPOTHESIS through R155_043 and is now PROVED on `(T*_{∞,P}, log 2]`, indeed on `(T*_ev, T*_odd)` (`cor:H1`,
   `R155_060` §5). P2 (a structural identity for `S_even` at log 2) was never found; the arena theorem shows the complement
   needs `≥ 12` modes, and the nodal rule decides only dominant signs ("arithmetic in the small entries", `R155_046` §2).
   Paper 42 already has positivity at log 2 [prim]; what is missing is a *structural* proof that generalises in `T`.
3. **Problem A after the AL retraction.** Round 4's closure of P1 ("the lattice is never the deficit", `R155_038` §2 item 2)
   was **withdrawn** in `R155_049` (consequence (i)); the correct statement is AL′: the lattice loss is exactly the alias of
   the polar block's jump `2cosh T` at `u = ±2T`, `E_edge = (4/π)cosh T·d`. The structural negative survives only in the
   prime-free `(D_∞)` programme. Whether the optimised lattice class also loses `Θ(1/M)` is OPEN (`cor:ALdef`(i)). The
   edge/polar location of the cost coincides with the location of non-attainment (`thm:O`).
4. **Two-prime windows: the obstruction that was removed.** R154_012 blamed "incommensurability of log 3 with log 2
   lattices"; R154_016 showed F1 works for any finite contact set. What remained was a value/atom-budget problem; Thm N′ then
   emptied lattice classes `M ≤ 24`. Flat-top and hybrid classes are **outside** TK's scope (`R155_012`), and the hybrid
   `N ≥ 6` computation was never run (`R154_030` §3).
5. **T1 re-read.** Until phase 157, T1 was read as "a proof must name a property separating `ξ` from every `ξ_K`"
   (`R138_005` §4, `R139_005` §3). Corrected: a field-uniform proof is **admissible** and proves GRH (P47 Rem 18.1a,
   `main.md:4862–4870`; amendment in `PATH-TO-D:176`). Earlier recommendations that excluded field-uniform routes on this
   ground are void; blueprint memo B8 (tower tensor-power) rests on this.
6. **T3 unblocked.** O-150.1 (read DMV 2006) blocked T3 through phase 156 (`ROW-D-REDUCED-STATEMENT` §5); (H-DMV) is now
   CITED (secondary) (`main.md:12166–12173`). The Beurling falsifier gate (3.2 of `ROW-D-CLOSURE-PLAN`) is usable; (P152.2)'s
   "Beurling blindness" test is the model.
7. **Kreĭn/Nevanlinna frame.** `thm:KEP3` makes certificates ⟷ indeterminacy off `{λ^W = 0}`; "a Nevanlinna-type
   parametrisation of 𝔖(T) in the indeterminate case would describe the set of certificates and is available only once one
   member is known" (`main.tex:1812–1816`). Unconditionally indeterminate for `T ≤ 0.8` (Zhu). The parametrisation was never
   written down. *(S4: it is a restatement per window; its only possible value is structure across `T`.)*
8. **Canonical column `s = ½`.** `prop:M` (`:997`): the outside-window Lévy tail band-limits the symbol and selects the scale
   `s = ½`; Problem B names "the canonical scale `s = ½` ... and weights adapted to the primes outside the window" as natural
   candidates that "the data neither support nor exclude" (`:4383–4385`). Tested only once, as an added column in the hybrid
   LP at `0.58` ("did not improve within solver accuracy", `:1202`) — never as a family.
9. **Concave value function in the weights.** `lem:degen`: `V_T(v)` is concave on `R^{N_T}`, supergradient
   `−c_{F⋆}(log n)`; `prop:finite(ii)`: `𝒱_T` is an intersection of half-spaces indexed by `F`. Never studied as an
   extremal/variational problem over combs (e.g. which faces of `𝒱_T` the true comb touches as `T` grows).
10. **Polar capacity per window.** `prop:polarcap`: `𝔊_T = S^Sch_T + J`; converse = `𝔞_T(h_odd) ≥ 2` and `𝔞_T(h_ev) ≥ −2`
    (`:3989–3992`). Galerkin `θ_* ≈ 0.99991`, `S^Sch ≈ −J` (DIAGNOSTIC, `rem:polarcapdiag`) — near-degenerate; never
    analysed as `T` varies.
11. **Doc 125 toy and O-148.2.** Phase-41 `125-construction-of-the-intersection-form.md`: exact Hodge index `(1,2)` on `⟨f₁,f₂,Δ⟩` for
    compact `C_p × C_p` with `f₁·f₂ = 1` integer; transfer to non-compact `C_Q × C_Q` unavailable (`R148_005` §2, §4). The
    positive half on the toy was never pushed to a semilocal `S`.
12. **Phase datum (36).** `ROW-D-CLOSURE-PLAN` §3.1: for `GL(1)` the phase datum already exists — the local `ε`-factors
    (unimodular, product formula); "what is missing is how it constrains zeros". The Laumon route (Fourier transform as
    transport between the additive and multiplicative squares, Gauss sums) was reclassified to a one-round dictionary
    (§8.2) and **never run** in phases 150–156 (desk-excluded in phase 157, `R157_002:159`, outside scope).
13. **CC counting function as `h⁰` (27c).** Withdrawn as a refutation in phase 140 (D.24.2: `λ_CC = 1/log 3` in CC's units;
    deficit conditional on `deg_CC = deg`), standing OPEN with units problems (U1),(U2) (`main.md:10361–10365`). *(S4: any
    real-valued `h⁰` on `D^W` or `C_c^∞ ⊕ RK` falls under Thm 19.25 / Cor 19.25b; a count on a different carrier would not.)*
14. **Never-analysed non-positivity mechanisms** (`R151_005` §2 item 3; `ROW-D-CLOSURE-PLAN` §10.2): measure rigidity of the
    `×p` semigroup, model-theoretic methods, transcendence/auxiliary functions (Pila–Wilkie), and the S5 Cartwright tropical
    Hodge index at chart level (`PHASE_136` §4 S5; only the Khovanskii–Teissier criterion was stopped, phase 138). Phase 152
    ran only FUP and Berkovich. *(S4: check S5's survey of phase 157 before building.)*
15. **Bilinear cancellation at fixed frequency.** P47 Remark 27.15 / item (42): Friedlander–Iwaniec, Heath-Brown bilinear
    arithmetic cancellation "is not to be presumed negative"; T4's rank-one claim (Thm 4.7) was withdrawn *because* of it
    (`R150_005` §1). Never developed against `W_T`.
16. **Stepwise Kreĭn band (P153.14)**: whether the atom `w_N` at `log N` lies in the Kreĭn-admissible band set by the kernel on
    `[0, log N)` — "new as a computation", its uniform version is RH (`R153_017` §2). Measured at `N = 3,4,5` only as
    Hellmann–Feynman restatements (`R153_021`).
17. **Galerkin-based diagnostics of phase 153 rounds 4–6** (`c(T) ≈ 76`, needle, Kreĭn-band "edge", apex offset `8.5·10⁻⁶`)
    rest on Galerkin bottoms at log 2 that `R155_038` later declared unstabilised (`rem:galerkin`). They are DIAGNOSTIC and
    should not be used as quantitative inputs; the single "curvature datum" (apex offset, `R153_021` §1) was never
    re-examined with certified numbers.

---

## §6 Definitions a memo needs verbatim

### Paper 46 (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`)

**Symbol, contacts, comb mass** (`main.tex:115–124`):
> "`T>0`, `I_T=(-T,T)`, … `F̂(τ)=∫F(t)e^{iτt}dt` and `c_F(u)=∫F(t)\overline{F(t-u)}dt` … `m(τ)=Re ψ(¼+iτ/2)−log π`,
> `σ_T(τ)=m(τ)−Σ_{n∈N_T}v_n cos(τ log n)`, `v_n=2Λ(n)/√n`, where `N_T={n≥2: log n<2T}` is the set of *contacts* and
> `A_T:=Σ_{n∈N_T}v_n` the total mass of the prime comb."

**The primitive form `eq:form`, `P_T`, the complete form `eq:W`** (`main.tex:125–136`):
> "`𝔞_T(F)=(1/2π)∫_R σ_T(τ)|F̂(τ)|²dτ`, defined on the form domain `{F∈L²(I_T): ∫log(2+|τ|)|F̂|²<∞}` … The two *Tate
> moments* are `A(F)=∫F(t)e^{t/2}dt` and `B(F)=∫F(t)e^{−t/2}dt`, and the *primitive subspace* is
> `P_T={F∈L²(I_T):A(F)=B(F)=0}`. The *complete Weil form* on the window is `W_T(F)=𝔞_T(F)+2Re(A(F)\overline{B(F)})`,
> which by the Weil explicit formula equals `Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, `Φ_F(s)=∫F(t)e^{(s−½)t}dt`."

**Bottoms** (`main.tex:146–147`): "Write `λ_min(A_T|P_T)` for the bottom of `𝔞_T` on the unit sphere of `P_T` and `λ^W_T` for
that of `W_T` on the unit sphere of `L²(I_T)`; `λ^W_T ≤ λ_min(A_T|P_T)` since the two forms agree on `P_T`."

**Lévy density** (`lem:K`, `main.tex:363–370`): "`K(u)=2e^{3u/2}/(e^{2u}−1)=1/(2sinh(u/2))+1/(2cosh(u/2))=2Σ_{k≥0}e^{−(2k+½)u}` …
`m(τ)=C_0+∫_0^∞(1−cos τu)K(u)du`, `C_0=ψ(¼)−log π=−5.3721834…`"

**`thm:A`, `𝔈`, `𝒦^prim`, `λ^P`** (`main.tex:417–433`): "`𝔈(Φ):=∫_0^∞(Φ(0)−ReΦ(u))K(u)du` … `𝔞_T(F)=C_0‖F‖²+𝔈(c_F)−Σ_{n∈N_T}v_nc_F(log n)` …
`𝒦^prim_{2T}={Φ∈𝒦_{2T}: ∫Φ(u)cosh(u/2)du=0, ∫Φ(u)u sinh(u/2)du=0}` … `λ^prim_T:=inf_{Φ∈𝒦^prim}[C_0+𝔈(Φ)−Σv_nΦ(log n)]=C_0−Λ_T` … and `λ^prim_T ≤ λ_min(A_T|P_T)`."
Remark `rem:Kprim` (`:451–456`): `𝒦^prim` is slightly larger than the primitive autocorrelations; "also `λ^W_T ≤ λ^prim_T`".

**Multipliers `eq:g`** (`main.tex:341–342`): "`g_0(u)=cosh(u/2)·1_{|u|<2T}`, `g_1(u)=u sinh(u/2)·1_{|u|<2T}`."

**`def:PD`** (`main.tex:553–560`):
> "**(P)** `λ^prim_T=inf{∫σ_T dμ: μ an even probability measure on R, μ̌(u)=0 for |u|≥2T, ∫ĝ_0dμ=∫ĝ_1dμ=0}`.
> **(D)** `D_T=sup{inf_τ[σ_T(τ)+ν̂(τ)+β_0ĝ_0(τ)+β_1ĝ_1(τ)]: ν a finite even signed Borel measure with supp ν⊆{|u|≥2T}, β∈R²}`.
> A triple `(ν,β_0,β_1)` with `f:=σ_T+ν̂+β·ĝ≥c` on `R` is a *certificate of value c*."
Prop `prop:P` (`:727–737`): a certificate with `β=(2,0)` proves `W_T ≥ c` on `L²(I_T)`; `β_0=2` is unique with this property.

**`def:W` and `eq:nuw`** (`main.tex:1219–1227`):
> "`𝒲_T` is the set of even measurable `w:R→R` with `w≡1` on `[−2T,2T]` and `|w(u)|≤Ce^{−(½+δ)|u|}` for `|u|≥2T`, for some
> `C,δ>0`. `𝒲_T^reg⊂𝒲_T` consists of the `w∈C^∞(R)` with compact support. For `w∈𝒲_T` define the even measure
> `dν_w=[½(1−w(u))K(|u|)+2w(u)cosh(u/2)]1_{|u|≥2T}du − Σ_{n∉N_T}(v_n/2)w(log n)(δ_{log n}+δ_{−log n})`, and `f_w:=σ_T+ν̂_w+2ĝ_0`."

**`thm:Z`** (`main.tex:1235–1251`): "(i) `f_w(τ)=C_0+∫_0^∞(1−w(u)cos τu)K(u)du−Σ_{n≥2}v_nw(log n)cos(τ log n)+2∫_R w(u)cosh(u/2)cos(τu)du`,
which is the right-hand side of the Weil explicit formula for the even test function `h_τ(u)=w(u)cos(τu)`. (ii) For
`w∈𝒲_T^reg` … `f_w(τ)=Σ_ρŵ(τ−γ_ρ)`, `ρ=½+iγ_ρ`."

**`def:KEP`** (`main.tex:1659–1674`): "`⟨g,h⟩=C_0h(0)+∫_0^∞(h(0)−h(u))K(u)du−Σ_{n≥2}v_nh(log n)+2∫_R h(u)cosh(u/2)du` … `𝔖(T)={ν a
positive symmetric tempered measure on R: ⟨ν̂−g,h⟩=0 for every even h∈C_c^∞(−2T,2T)}`. `KEP(T)` is *solvable* if `𝔖(T)≠∅`,
*determinate* if `#𝔖(T)=1`, and *indeterminate* if `#𝔖(T)≥2`."

**`RD_T`, comb-level forms** (`main.tex:3364–3372`): "for a nonnegative arithmetic function `a` … `v_n(a)=2a(n)/√n` … say that
*row D holds at T for a*, written `RD_T(a)`, if `λ_min(A_T(a)|P_T)≥0`; `RD_T:=RD_T(Λ)` is `λ_min(A_T|P_T)≥0`. (`RD_T` is not the
dual value `D_T`.) … `W_T(a)(F):=𝔞^{(v(a))}_T(F)+2Re(A(F)\overline{B(F)})`." Warning (`:3375–3381`): `W_T(a)` is **not** the zero
sum of `ζ_a`; statements about it concern forms and classes, not zeros.

**`def:Al`** (`main.tex:3735–3742`): "`Al_T(w)`: for every `τ∈R`, `−2Re Σ_{n≥2}Λ(n)w(log n)/n^{½+iτ} ≥ −[C_0+∫_0^∞(1−w(u)cos τu)K(u)du]
−2∫_R w(u)cosh(u/2)cos(τu)du` … `Al_T(w)` is exactly `f_w≥0` on `R`."

**Archimedean form and thresholds** (`main.tex:2459–2467`, `:2480–2481`): "`A_∞(F)=2A(F)B(F)+(1/2π)∫m|F̂|²`, … `Π_T(F)=−Σ_{n∈N_T}v_nc_F(log n)`,
so that `W_T=A_∞+Π_T`"; "`T*_∞=sup{T: λ^∞_min(T)>0}` and `T*_{∞,P}=sup{T: λ^{∞,P}_min(T)>0}`." (H1) (`:2949–2950`): "For
`T_2>T*_{∞,P}` write (H1)(T_2) for the statement that `n_−(A_∞|P_T)=1` for every `T∈(T*_{∞,P},T_2]`."

**Parity–Schur objects** (`main.tex:3801–3812`, `:3827–3828`): "`φ_ev=cosh(t/2)1_{I_T}`, `φ_odd=sinh(t/2)1_{I_T}`,
`ℓ_par(F)=⟨F,φ_par⟩`, `ε_ev=+1`, `ε_odd=−1` … `Q^par_T:=P^par_T∩D_T=ker(ℓ_par|D^par_T)` … unique `h_par∈D^par_T` with `ℓ_par(h_par)=1`
and `𝔞_T(h_par,G)=0` for all `G∈Q^par_T`. Put `𝔤_par(T):=W_T(h_par)=𝔞_T(h_par)+2ε_par`"; `𝔊_T:=diag(𝔤_ev,𝔤_odd)` (`:3857`).

**Problem A** (`main.tex:1937–1944`) and **Problem B** (`:4375–4380`) — quoted in §3.2 items 1–2 above.

### Paper 47 (`04-papers/47-intersection-frame-defect/archive/main.md`)

**`D^W`** (Def 11.1, `main.md:1972–1975`): "`D^W` is the set of real functions `g` on `R` such that `g∈C²(R)` and there is `ε>0`
with `g^{(j)}(t)=O(e^{−(1+ε)|t|})` (`j=0,1,2`, `|t|→∞`)." Note (`:2019–2046`): Weil's class `e^{−(½+ε)|t|}` is **not** used, because
the repository's proof of the explicit formula (Paper 45 Thm 9.4) runs on `Re s = c > 1`.

**`I_∞`** (Thm 11.5, `main.md:2136`): "`I_∞(F,G)=Φ_F(0)Φ_G(1)+Φ_F(1)Φ_G(0)−Σ_ρΦ_F(ρ)Φ_G(1−ρ)`", so `I_∞(F,F)=2Φ_F(0)Φ_F(1)−W(F)`;
on primitive `F`, `I_∞ = −W` (P47 (1.9), `:155–161`).

**Canonical class** (Def–Thm 11.7, `main.md:2164–2168`, (11.9)): "`K(t):=Σ_{n≥1}(4π²n⁴e^{9t/2}−6πn²e^{5t/2})e^{−πn²e^{2t}}`" (Pólya's
kernel; **not** P46's Lévy density, same letter), `Φ_K=ξ`, `K>0`, even, `deg K=1`, `M(K)=(½,½)`.

**Transfer theorem** (Thm 12.3, `main.md:2744–2762`): "Suppose there is `h⁰:D^W→R_{≥0}` with **(a)** `h⁰(E)≥0`; **(b′)** if `h⁰(E)>0`
then there is `E'∈D^W` with `E'≥0`, `E'≢0`, and `E−E'∈𝓝_∞`; **(c)** a constant `χ` with `h⁰(E)+h⁰(K−E)≥½I_∞(E,E)−½I_∞(E,K)+χ`.
Then `I_∞(F,F)≤0` for every primitive `F∈C_c^∞(R)`, and hence RH." (Unsatisfiable: Thm 19.25, `:6407`.)

**Axiom list** (Def 18.13, `main.md:5248–5286`): A1 analytic frame; A2 canonical class; A2⁺ polar positivity; **A3** equimodular
polar block `P=1−P`, `|p−½|=θ_P`; A4 nonnegative Dirichlet coefficients; A5 explicit formula; A6 splitting; **A7** zero strip =
polar strip; **A8** Euler product with nonnegative atoms, `c(n)≥0` on prime powers; **A9** `Z(σ)>0` on `R`. Table Thm 18.14
(`:5285–5294`): `Ξ_a` fails A3 only; `Ξ_Q` fails A7, A8, A9; `ξ_K`: A9 OPEN.

**T1** (Thm 18.1, `main.md:4836–4840`): "Let `𝔓` be any list of properties of a completed zeta function that holds for `ξ` and holds
for `ξ_K` for every number field `K`. Then no derivation of the Hodge-index inequality (18.2) from `𝔓` alone can be sound unless
GRH holds for `ζ_K` for every number field `K`." Rem 18.1a (`:4862–4870`): a statement about derivations; a field-uniform proof
is a proof of GRH for all `K`.

**The wall** (§28.2, `main.md:12111–12138`): "The sign is the assertion `ψ(x)−x ≪_ε x^{1/2+ε}`, a partial-sum bound for a
polar-at-zeros sequence" — equivalent to the zero bound; uniform in the number field unless it names a separating property;
uses the Euler product essentially (A7/A8/A9); not by single-fibre extraction from `L²` moments; not from entire-at-zeros sequences.

**Reopening clauses** (§28.4, `main.md:12634–12645`): an object `𝒪` on the adelic square that (1) is a square (Rankin-positive after
every twist); (2) has polar divisor determined by local data; (3) zero contribution holomorphic left of that a-priori pole;
(4) reads phase (fails for `Ξ_a`); (5) uses `+` and `×` (fails for `Ξ_Q` and every Beurling system); (6) is uniform in the number field.

### Falsifiers of record (definitions)
* `Ξ_a(s) = ξ(s+a)ξ(s−a)`, `0<a<½`: polar set `{−a,a,1−a,1+a}`, weights `Λ(n)(n^a+n^{−a})`, off-line zeros — P47 §7.1, `R137_007` §2.
* `Ξ_Q = ½s(s−1)Λ_Q`, `Λ_Q(s) = (√D/2π)^sΓ(s)Z_Q(s)`, principal `Q`, `h(−D) > 1` (Epstein; Davenport–Heilbronn zeros) — P47 §18.2, `R139_005`.
* Beurling systems (Diamond–Montgomery–Vorhauer 2006; Zhang 2007): Euler product, `Λ ≥ 0`, pole, zeros at `1 − c/log t` — T3, P47 §27.4.
* Comb modifications `Λ·1_{n≥N}`, `Λ + c·1_{n=n₀}`, `a_θ = Λ − (1−θ)Λ(2)1_{n=2}` (`thm:finmod`, `cor:convfail`) — same zeros and pole
  as `ζ`, no functional equation.

*S4 end of survey. Nothing here is a new claim; no label moves.*
