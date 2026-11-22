# SHAPE_THEOREM — independent review

Pen and paper. Independent review. Row D (λ_A(T) ≥ 0 on P_T for every T, Paper 46 eq:target). Verdicts: CONFIRMED /
FIX / DOWNGRADE / UPGRADE. Every clause of SHAPE_THEOREM.md (and of SHAPE_THEOREM_SECTION.tex) was checked against the cited
source as it stands on disk: Paper 46 main.tex (146 pp, labels verified to exist), phase-188/189 memos and their
reviews, index 04_ Part I, Paper 47 §18 (main.md), SECONDARY_ITEMS.md with its independent review.

## 0. Summary of verdicts

| clause | memo label | verdict | reviewed label |
|---|---|---|---|
| Theorem S (A), (C) | — | **FIX (overclaim)** | (A) holds only for the operations whose falsifier is PROVED: O1, O2, O3, O4 (c large, c small), O7, O8a, O8b, O12, O13, O15 and the derived classes (progressions, sieves, zero information). O4ε, O5 CONDITIONAL; O6 ARGUED; O8c ARGUED (window form); O9 CITED (complete) / ARGUED (primitive); O10 OPEN; O11 and O14 are not transfer instances at all (no falsifier with negative bottom) and belong to part (B). (C) accordingly: "destroyed by each of O1–O15" → "by each operation of the PROVED list; and, with the stated labels, by the others" |
| A1 | PROVED | **FIX (constant)** | PROVED. T₀(0) = 0.74921 (Paper 46 prop:arch, l. 2282, 3047), not "≈ 0.8047"; 0.8047 = ½log5 is the lower end of ½log N for N ≥ 5 |
| A2 | PROVED | CONFIRMED | PROVED (thm:finmod(ii); F₊ of lem:cpos; c_* explicit given F) |
| A3 | PROVED | CONFIRMED | PROVED (prop:finsupp gives limsup ≤ C₀ − A_S < 0; cor:wtail(i); window not located) |
| A4 | PROVED | CONFIRMED with one wording FIX | PROVED. "c → 0" uses continuity of the concave finite function μ_T of lem:degen at v = 0 (not "concavity in c" alone); c large: F₊ with ℓ < log(3/2) charges only n = 2 — correct |
| A4ε | CONDITIONAL (κ_T ≠ 0) | CONFIRMED | CONDITIONAL; κ_{log2} ≈ 0.09 NUMÉRICO (rem:wit-sens); nothing in the record proves κ_T ≠ 0 at any T |
| A5 | CONDITIONAL + NUMÉRICO | CONFIRMED, one omission FIX | CONDITIONAL. rem:resweights also requires ε ≤ Λ(n₀) when s = −1 (a ≥ 0); contacts with Λ(n₀) = 0 admit only s = +1 and 𝒞_BT only s = −1. Add to the clause |
| A6 | CITED | **DOWNGRADE → ARGUED** | R167_103 row 7 (the source the memo cites): "DMV/Zhang systems have no Γ_ℝ functional equation, so they are not systems in the sense of R166_501 Def 1, and they have no window form W_T in the record's sense. The transfer to row D is ARGUED only (needs a Beurling Weil form)". R184_005 and R163_803 concern counting functions and zeros of ζ_𝒫, not window forms. No negative window bottom of any Beurling comb is cited or computed anywhere. Hence A6, the "not ℤ-integral" branch of Lemma I, and the ℤ-integrality half of Corollary (b) are ARGUED |
| A7 | PROVED | CONFIRMED | PROVED (one-line variant of finmod(i); zeros of ∏_{p<P}(1 − p^{−s}) lie on Re s = 0, outside the strip) |
| A8a | PROVED | CONFIRMED | PROVED (thm:wit-model(iii), prop:quartetmodel) |
| A8b | PROVED (flagged) | **CONFIRMED: PROVED is right; L2_011 row 13 is stale** | prop:ftprim builds the primitive witness directly (φ₀ with both Tate moments zero; centring scales A, B by e^{±s/2}; on P_T the primitive and complete forms agree). The independent review in SECONDARY_ITEMS.md §"Review", item 4, re-derived it step by step and CONFIRMED it, explicitly closing the MAJOR of R186_114 §2.4 ("(Z-strip) is not needed: the argument is comb-level"). L2_BUILD_011 row 13 was written before that review and is superseded; erratum note added there |
| A8c | PROVED (step) / ARGUED (WP_T) | CONFIRMED | As labelled. The review of NT_011 fixed the class: 𝓜 must not contain holomorphy in the strip together with order-1 growth (ζ̃ has four poles off the line). The window form of ζ̃ on P_T has no computed witness; not a lem:transfer instance |
| A9 | CITED (complete) / ARGUED (primitive) | CONFIRMED, one scope FIX | As labelled. Weil's criterion (Weil 1952 / Bombieri) uses compactly supported tests, so a negative test lies in some L²(I_T) and the complete window form W_T of Ξ_Q is negative there and at all larger windows (extension by zero). The comb of Ξ_Q has weights of both signs (no Euler product): it is a form object, not a comb in 𝔚 — say so. Paper 47 Thm 18.16 (T2) concerns the Hodge-index inequality (18.2), not W_T or λ_A: cite only for the falsifier and the axiom list |
| A10 | CONDITIONAL / OPEN | CONFIRMED | Transfer principle (tautology) PROVED; falsifier OPEN. Paper 47 Thm 18.1's proof passes through a statement excluded by the stated rule; the memo does not use it — verified |
| A11 (O12) | PROVED | CONFIRMED, one hypothesis FIX | thm:famblind needs, besides the family hypotheses, that the weight class be closed under one-term amplification (or, for thm:famFE, be the FE class); the memo row omits this. Bilateral laws λ_A = L(T)(1 + o(1)) are NOT excluded and the memo says so (rem:bar-fam "this class is open"; R186_036 Thm 3(b)) — no overclaim |
| A12 (O13) | PROVED | CONFIRMED | PROVED (thm:nolocal: genuine falsifier, negative form) |
| A13 (O14) | PROVED, listed as transfer | **FIX (classification)** | lem:wh-T / lem:wh-Tprime / thm:wh-detinherit(iii) produce a modified form with bottom 0, not < 0: these are precision (margin) constraints, not instances of lem:transfer. Move to the structural part (B). Content PROVED as stated (admissible splittings only) |
| A14 | NUMÉRICO / PROVED split | CONFIRMED | As labelled |
| A15 | PROVED | CONFIRMED | PROVED (prop:prog; N_021 Thm 2; 𝒞_BT closed under deletion only, A1 suffices for T > T₀(0)) |
| A16 (O15) | PROVED | CONFIRMED | PROVED as an existence statement: probability of positivity < 1 ⇒ a realization fails WP_T |
| A17 | PROVED; NT_014 ARGUED | CONFIRMED | As labelled |
| B1 | PROVED (inputs CITED) | CONFIRMED | (Z1), (Z2) Platt–Trudgian CITED; used for an upper bound only |
| B2a | PROVED | CONFIRMED | The paper already contains it: prop:boundary (C₀ = −2ζ′/ζ(½)); the "every configuration" reading is the pairing ρ ↔ 1 − ρ̄ (L2_010 §1). Cite prop:boundary in the paper |
| B2b | CONDITIONAL | CONFIRMED | Hardy–Riesz CITED + divergent alternative ARGUED (N_013 §2, self-review item 3). Theorem S(B) must not state "exact at every packet frequency" without this label — FIX in the theorem statement |
| B2c | PROVED (Mertens CITED) | CONFIRMED, one dependency FIX | The mean-square statement is PROVED; "no fixed band can be discarded" depends on B2b (CONDITIONAL), stated in §3(d) but not in the B2c row — add |
| B2d | PROVED | **FIX (constant)** | thm:kappa gives κ_* ≥ ¼\|C₀\| = 1.3430 (a lower bound; κ_* ≤ \|C₀\|(¼ + τ₀²)), not "κ* = 1.343…". The reading "deficit paid by the fluctuation" is an interpretation (ARGUED), the inequalities are PROVED |
| B2e | PROVED | CONFIRMED | thm:wit-Tc(iv), internal restatement only |
| B3 | PROVED | CONFIRMED | rem:fe / L2_026 §1 |
| B4 | PROVED; "C–S always loses" ARGUED | CONFIRMED | Scope stated (convolution operators only) |
| B5 | PROVED ((½log2, ½log3) OPEN) | CONFIRMED | thm:sos |
| B6 | PROVED ((iii) NUMÉRICO constant) | CONFIRMED | |
| B7 | (i) PROVED / reading ARGUED; (ii) PROVED mod LW / converse NUMÉRICO | CONFIRMED | |
| B8 | PROVED | CONFIRMED for the Paper-47 members and Theorem E (L2_031); R186_018 (ρ*(T) < 1) and R186_028 (scalar index) not re-verified here — cite as index W1 entries, omit from the paper |
| Lemma I | PROVED | **FIX (bookkeeping) + DOWNGRADE of one branch** | (1) Rows 13 and 21 do NOT keep "no FE": M_m = ξ·polynomial and f_t both satisfy the functional equation. What they break is the Euler product over ℕ (M_m: a polynomial factor in s, whose logarithmic derivative is not a Dirichlet series over ℕ; f_t: frequencies m/√M ∉ ℕ). They belong to the second branch; conclusion (b) stands. (2) The "not ℤ-integral" branch rests on A6, hence ARGUED. (3) The conclusion is a finite case analysis over the 23 listed properties, not over all conceivable properties (row 23 says so). Reviewed label: PROVED relative to the table, modulo CITED (Epstein) and ARGUED (Beurling) |
| Cor. (a) | labels listed | CONFIRMED after the A6/A13 corrections propagate | |
| Cor. (b) | PROVED | **DOWNGRADE (one third)** | Euler × FE: PROVED (a_P; Epstein CITED). ℤ-integrality: ARGUED (A6). "Identifies ζ" uses Hamburger / Thm O of R163_1001: CITED |
| Cor. (c) | PROVED + NUMÉRICO | FIX (wording) | lem:degen gives −c_{F*}(log n) as a supergradient of the concave function μ_T; the one-sided directional derivative is the minimum over minimizers, not "the first variation" unless the minimizer is unique. Rest as labelled |
| Cor. (d) | — | CONFIRMED | B2b CONDITIONAL stated |
| Cor. (e) 1–9 | — | CONFIRMED | Each item traced to a lemma; items 2 and 4 inherit ARGUED (Beurling branch; NT_011 scope) |
| Cor. (e) 10 | — | **FIX (imports a different form)** | "invokes A3 (equimodularity) and at least one of A7/A8/A9 of Paper 47 (T2, A9)": Paper 47 Thms 12.4/18.16 and the Ξ_a falsifier concern the Hodge-index inequality (18.2), a different form from λ_A(T); no Ξ_a-type window-form falsifier exists in the record. For the window form the record supports only: (i) A1–A6 alone do not suffice (Ξ_Q, complete form, CITED); (ii) the transfer principle of A10. Restated accordingly |
| §3(e) "not excluded" list | — | CONFIRMED | Every listed object is marked not excluded in its source (rem:bar-fam, rem:bar-lin, thm:sos, rem:bar-loc, N_021 Prop 3, index 06_ residues) |
| §4.1 (Zhu to 0.8, Liu to 17/16) | CITED | CONFIRMED | rem:twohalves; AUDIT_LIU |

## 1. The theorem-level overclaim (the main finding)

Theorem S(A) says: "If 𝒜 is closed under any one of O1–O15 … then 𝒜 contains no valid deduction of WP_T(q₀)". Lemma lem:transfer
requires an explicit member with **negative** bottom. In the memo's own table: O10 has no falsifier (OPEN); O11 (reflection of the
σ-family) has no falsifier at all — B3 says the symmetrized family vanishes, which is a structural fact, not a transfer; O14's
modified form has bottom exactly 0 (lem:wh-Tprime), so it is a precision constraint, not a falsifier; O4ε and O5 are conditional
on κ_T ≠ 0, resp. c_{F*}(log n₀) ≠ 0; O6 and O8c have no computed window witness (ARGUED); O9 has a witness for the complete form
only (CITED). Part (C) ("destroyed by each of O1–O15") inherits the same overclaim. The theorem is therefore restated with three
tiers: (A) PROVED transfer (O1, O2, O3, O4 at large and small c, O7, O8a, O8b, O12, O13, O15; derived classes 𝒞_PNT, 𝒞_zeros,
𝒞_prog, 𝒞_BT); (A′) transfer with a label (O4ε, O5 CONDITIONAL; O9 CITED/ARGUED; O6, O8c ARGUED; O10 OPEN); (B) structural
(B1–B8, now including the former A13 and the O11 antisymmetry). The admissible region (e) is unchanged in substance, but items
2 and 10 carry the ARGUED/transfer-only labels.

## 2. The f_t inconsistency (decided)

prop:ftprim (Paper 46 §18.2, l. 7877) constructs the primitive witness directly and was re-derived by the independent
review of SECONDARY_ITEMS.md (item 4, "CONFIRMED (PROVED)", maximally sceptical six-point check), which explicitly
states that the (Z-strip) hypothesis of R186_114 §2.4 is not needed. Index 04_ F-f_t records "(H_f) PROVED ".
L2_BUILD_011 row 13 ("primitive witness CONDITIONAL, R186_114 §2.4") predates that review. Decision: **PROVED**; row 13 is
stale and gets a dated erratum note. A8b, A11 (FE half) and thm:famFE are unconditional.

## 3. What was changed on disk
- SHAPE_THEOREM.md: dated erratum block (§0) listing every fix above; Theorem S restated in three tiers; A1 constant;
  A5 admissibility; A6 → ARGUED; A11 hypothesis; A13 moved to B; B2d constant; Lemma I bookkeeping; Cor. (b), (c), (e)10 restated.
- SHAPE_THEOREM_SECTION.tex: same corrections; the section was then integrated into Paper 46 as §"The shape of a proof"
  (before "Open problems"); see DEFINITIVE_CHANGES.md, section dated .
- 03-research/phase-188-closing-D/L2_BUILD_011_INPUT_MAP.md: erratum note (row 13 superseded; rows 13/21 branch bookkeeping).

No sign contact; nothing here moves λ_A(T) for ζ. No equivalence between row D and any external statement is used.
