# Phase 185 — Filling in the crossword

Goal: starting from CROSSWORD-TO-D (05-meta), advance square by
square with real gains, documenting every step worth entering into Paper 46.
Starting square: **O166.802.1** (circularity of R166_802 only PROVED for a test and
power families; ARGUED for multiscale non-linear B). Two sides: barrier (extend
the circularity: new theorems) and positive (a B outside the proved classes).

## Round 1

| file | result |
|---|---|
| R184_094 | audit of R184_016: A1 local E1 (sandwich); "single square" only on route A |
| R185_001 | finite-dimensional circularity PROVED (Lemmas 2–4, Thm 5 M1/M2, Thm 6); residues ρ1 (non-power infinite families), ρ2 (non-convex with zero integrality), ρ3 (uniformity of K*) |
| R185_002 | integrality probe NO-GO; Thm C (convexity/solidity ⟹ blind to W-sieve) and Thm F (closure under deletion ⟹ does not exclude) PROVED; Conj G: what remains must be non-convex, non-counting, sensitive to deletion, zero-free |
| Paper 46 | DRAFT_SECTION_INERTIA_BARRIERS + CHECK_TABLE (in progress) |

## Round 2

| file | front |
|---|---|
| R185_091 | audit of R185_001/002 (publication standard) |
| R185_003 | ρ1: infinite families (M1 immediate; M2 Hahn–Banach, mixture ≥ 0; residual (TC)) |
| R185_004 | U3: every sentence of 𝔐_Λ is closed under deletion or identifies ζ (trichotomy with the boundary θ ≤ 1/3) |

Status: D OPEN. The gains are barrier theorems; none gives a sign.

## Round 2 results

* R185_091: audit of 001/002. FATAL: Thm D (002) false → ARGUED. MAJOR: Thm 5(b) closure; Cor 7 "excludes W"; Prop A; "Thm F ⇒ E1". Ready for Paper 46: Lemmas 2–4, Thm 5(a), Thm 6, Thm C(i)(ii), core of Thm F.
* R185_003: (ρ1) CLOSED on the bounded-type cone (M1 any 𝔉; M2 with 𝓡 compact or product topology). Residues (ρ1′) 𝓡 non-compact, (ρ1″) unbounded type = the terrain of (TC).
* R185_004: U3 PROVED relative to 𝔐_Λ. Obs 4: on 𝒟, a ζ-type EF with conductor 1 identifies ζ alone (Thm R). Trichotomy (i) deletion ⟹ E1, (ii) completeness ⟹ identification, (iii) counting: (iii-a) CONDITIONAL (splice window), (iii-c) OPEN = boundary θ≤⅓ (positive ⟹ stronger than RH).
* Paper 46: DRAFT_SECTION_INERTIA_BARRIERS.tex (4 pp., compiles) + CHECK_TABLE.md. Entering: thm:inertia-split, -B2, -nogo (generalized to bounded kernel), -finite, -quartet, -rank. Flagged: detection law. Held back: metric ξ, conditionals, semilocal objects, A1. Conflict: "Q ⟺ RH" of R184_015 vs cor:margin2(iii) → only under Max–Iso.

## Round 3

| file | front |
|---|---|
| R185_092 | audit of 003/004 |
| R185_005 | assembled relative barrier theorem (U1+U2+U3), proof tree, CONDITIONAL/OPEN leaves, what falls outside 𝔐 |

## Round 3 results

* R185_092: audit of 003/004. FATAL: U3(i) depended on "Thm F ⇒ E1" (ARGUED). MAJOR: scope W₂ in Thm 2; Prop 3 Radon only (ba(𝔉) = ρ1′, narrowed by Tychonoff); Def 5(C) X_P ≤ window; (iii-a) no known falsifier → rewrite via circularity; (iii-b) family ℙ∖S with p_k ≥ 2^{2^k}.
* R185_005: Theorem BR (relative barrier) assembled and corrected (Revision 2): PROVED relative to 𝔐 except ρ1′, ρ2 (M2) and exhaustiveness (ARGUED). Outside 𝔐: unbounded type, zeros+Euler, non-RH (Λ,Γ), operator.

## Round 4 (outside 𝔐)

| file | result |
|---|---|
| R185_006 | analytic proof at ½log3: NO-GO (gap_∞ ≈ 0.083 < 0.490); reduction PROVED to a finite check of dim ≤ 47 (NUMERICAL 7.7e-4); the positivity is a 10⁻³ cancellation with alignment h(x)↔h(x+log2); the LP certificate remains the tool |
| R185_007 | (ρ1″) closed: unbounded type circular (Thm 1∞/2∞); the non-E1 content is partial bounds Θ ≤ ½+δ′ (quasi-RH, OPEN, out of scope); (TC) type Q, δ′→0 term |
| R185_008 | W11 literally false for finite T; W11-∞/W11-fin; **Lemma 1.1(b) PROVED** (finite index ⟹ finitely many off-line zeros; sup N = 2m) → R183_031 Thm 1 without RH; correction: archimedean indefinite from 0.4608 (full) / 0.58 (primitive) |
| R185_093 | audit of 006–008 (in progress; priority Lemma 1.1(b)) |
</content>

## Other files in this folder

- `R185_005B_BR_WITHOUT_EQUIVALENCE.md` — Relative barrier theorem BR, rewritten with no equivalence.
