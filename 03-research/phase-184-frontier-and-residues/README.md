# Phase 184 — Frontier and live residues

Goal: work toward a closure of D, deciding each
round from the corpus (grid R162_2300 §3 walls, §4 falsifiers, §7 S1–S12,
NO-GO-LIST). Rule: every closure goes through audit
before being recorded.

## Round 1 (R184_001–004)

| file | front | cell / residue |
|---|---|---|
| R184_001 | discrete Beurling frontier θ ≤ 1/3 | 5G, O2601.1 sharpened (BF_θ^disc) |
| R184_002 | fresh audit of phase 170 | residual: Wronskian sign over the first contact |
| R184_003 | identity λ₁(ker ℓ)=λ₂(prim); estimate (M) | phase 183, tools |
| R184_004 | C_B dichotomy (m<∞ ⟹ m=0) with inertia | 8F/4E/7E, gap (b) of R162_2501 |

State: in progress. D OPEN.

## Round 1 results

* R184_001: frontier θ ≤ 1/3 OPEN. New: Prop 2.1 (O(1) placement at the prime level preserves the target's zeros), Prop 2.2 (N's remainder ⟺ polynomial growth), ceiling ½ with a smooth target. Rigidity with θ₀>0 would be stronger than RH. Residues O184.001a/b/c.
* R184_002: phase 170 = exact signless identities about the contact jet (W12+W5); as a route to D, E1. Residue (R170-RES) is an equality.
* R184_003: the constant is NOT an eigenvector (NO-GO); the coincidence λ₁(ker ℓ)=λ₂(prim) is explained by parity (Thm A.1, Cor A.2, PROVED). (M) reduced to (M_w), OPEN.
* R184_004: C_B by inertia NO-GO (PROVED): M_m has the same A_∞ and B_p as ζ, differing in rank ≤ 6m.
* R184_091: review (in progress).

## Round 2 (R184_005–008)

| file | front | cell / residue |
|---|---|---|
| R184_005 | C1 rigidity at θ = 0 | 5G, C1/C2 (R166_701) |
| R184_006 | one-quartet detection law | (P153.5), 7A/7D |
| R184_007 | needle theorem b = log 3 | (P153.4), 3A/W2 |
| R184_008 | factor route and discrepancy below 1/3 | O184.001a/b, 5G |

## Round 2 results

* R184_005: C1 OPEN in the O(1) reading; false literally in O(log x) but with counterexamples that are modifications of ζ (new zeros only at Re s = 0). L1–L3 PROVED. Frontier θ=0 remains in E1.
* R184_006: one-quartet detection law, Thm 1 PROVED under Max–Iso: T*(a,γ) = max{1+1/a, (1/2a) log(C_ψ L(γ))}. Empty for T ≤ 0.805. Quantifies ¬RH ⟹ ¬positivity; blind to the class (M_m).
* R184_007: needle b=log 3 already closed in R153_010; reconfirmed: even/odd roof, positive set (log3 − 3.9e-7, log3 + 2.03e-5). Theorem W (convexity in weights) PROVED, blind. Previous verification failure by the editor.
* R184_008: factor route NO-GO PROVED for every θ<1 (Lemma AC + Theorem F, Landau). O184.001a the only live construction; L* remains ARGUED.

## Round 3 (R184_009–010, R184_092)

| file | front |
|---|---|
| R184_092 | review of 005–008 |
| R184_009 | sweep of local 2026 literature: never-used inputs, tested against the walls |
| R184_010 | Theorem L* via large sieve / Franel (O184.001a) |

## Round 4 (R184_014–015)

* R184_014: erratum PROVED (chaos of every order has the same power X^{1−2a}; level k contributes x^{(1−θ)/(2k)}); L*_comp CONDITIONAL on (ZF_R) (R zero-free in Re u > σ₁ < ½); counterexample in the relaxed class without integrality (R = L(u,χ), error x^{max(2/5,(1+θ)/3)}): every proof must use that b_{p,1} is an integer.
* R184_015: no candidate; Theorem 2 / Cor 3 (PROVED): every Sonin-remainder norm bound is either blind to M_m (source) or E1 (form); sharper form of W11.
* Synthesis: R184_099 (rounds 1–3) + this section. D OPEN.

## Round 5 (global survey)

* INVENTORY-PHASES-168-184 (05-meta): ≈150 PROVED, ≈60 NO-GO, 24 OPEN groups, 12 corrections.
* R162_2300_REPAINT_PROPOSAL + merged part 19: 1100 routes, ■13 ◩23 ◧28; 8 cells change (2A, 6C → ■; 2G, 4D, 7A, 7B, 7F, 7H → ◩); walls W11′, W-Sonin, W-factor, W-dither; new falsifiers.
* CROSSWORD-TO-D (05-meta): E1 cluster (19), 14 intermediate nodes, 18 meta-theorems; minimal crossword {A1,(Dom_θ),(P_gap)}.
* R184_016: A1 is E1 (PROVED given (Dom_θ)). Only blank square: O166.802.1.
* Paper 48 updated to phase 184 (main_pre_p184.tex; 33 pp., compiles).

## Other files in this folder

- `R184_011_MULTIGENERATOR_AND_LP152.md` — Residues (6F) of the grid: multigenerator rigidity (G2_B7_R5) and LP-152.
- `R184_012_POLARCAP_AND_MINOR_RESIDUES.md` — `prop:polarcap` in T and minor residues of master grid item 59.
- `R184_013_FULL_SYSTEM_DITHER.md` — The full system with dither: the composites are the exponential, and the exponential sees all frequencies.
- `R184_093_REVIEW_009_010_012.md` — Review of R184_010 (priority), R184_009 and R184_012.
- `R184_094_REVIEW_016.md` — Review of R184_016 (A1 selector check).
