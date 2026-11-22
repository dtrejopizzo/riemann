# LEDGER L5 — meta layer (routes index, grid, crossword, surveys, maps) — phase 200

Analyst L5. Sources: ROUTES-TRIED-INDEX (full README, 01–06, 05/05b, SURVEY_MODERN_UNTRIED, AUDIT_*),
survey (SYNTHESIS, BRIEF), grid R162_2300 (via `04_` Part II, 824 rows), crossword, THE_BACKWARD_MAP,
AUDIT_L_SHARP_16 §6 (restrictions 1–28). Labels: PROVED / ARGUED / OPEN /
NUMERICAL. Counts: "≈" = keyword assignment from the index (Part II uncurated) plus a reading of the curated sections;
these are orders of magnitude, not exact censuses.

Index totals (table rows): 01: 51 · 02: 38 · 03: ≈190 · 04: ≈200 curated + 824 grid · 05/05b: 110 ·
06: ≈40 sub-routes · phases 190–199 (README only): ≈200 (including ~105 discards from the certainty audit).
Total ≈1,650. Part II results: 393 DEAD, 191 REF-D, 189 PARTIAL, 15 explicit NO-GO.

## 1. Taxonomy: ten method classes

The grid separates routes into ≈60 families, but under the mechanism that kills them they reduce to ten classes. BARRIER_001's
catalog 𝒜 (A1–A9) is almost the same list seen from the premise side.

| # | Class | Examples (where) | Mechanism that kills it | Label | ≈routes |
|---|---|---|---|---|---|
| C1 | **Linear in Λ / comb-generic** (identities and affine functionals of the comb: Euler/Möbius, Hecke on σ_T, Vaughan/Ramanujan, Poisson-ℤ, exact traces, bootstrap, Stokes) | N_018, EI_001–003, INV_H/E/G, front A, INV_O, INV_S, INV_V_002 | thm:shape(A), lem:shape-ident: the route survives O1–O15 (a_P, cΛ, Beurling, Epstein x²+5y², DH) | PROVED (form); Beurling falsifier ARGUED, ζ_K OPEN | ≈330 |
| C2 | **Cone on log ζ / ∂log** (Dirichlet positivity, Lévy–Khintchine, PF/TP, Laguerre–Pólya, Pick, Markov/jumps ≥ 0) | INV_F (F2), INV_A, 𝖯⋆, 104_21, R155_046, M2 | the convex cones do not survive ∂log; the ones that do are stable under adding positive mass, so they let O2 and (1+c)Λ through | PROVED (F2, 𝖯⋆); PF₅ CITED, PF₄ OPEN | ≈120 |
| C3 | **Certificate / dual / LP / SOS** (flat-top, network, Lasserre, Viazovska, LP on the torus, CP/separability) | Paper 46 §3–6, thm:Z/O/R, fronts E/L/N, G0 | the dual is D (thm:Z); the certificate is bounded by λ_P; magic functions are impossible (thm:O) | PROVED | ≈140 |
| C4 | **Zero side** (density, zero-free regions, Li/Keiper, Montgomery–Dyson, Nyquist central cell) | cor:void C_zeros, thm:finZ, NT_011/014, front D | no finite set of zeros carries a certificate; zero information is empty for the window | PROVED | ≈160 |
| C5 | **Place by place / semilocal** (Sonin, CCM, prolates, reflection by place, local FE, local Tate) | phase 183, R186, INV_L L1, L81, NG-E1 | the local FE is O6-stable; semilocal stabilization has no sign source; Borel data stay separated by places | PROVED (L1, S1); L81 ARGUED | ≈90 |
| C6 | **Estimate with remainder** (sieves, BV, VK, moments, Baker, sum-product, uniform Schur estimates) | W-sieve, phase 167/168, BARRIER_EST_001, SPEC_A, MECH_001 | slack ≤ λ_A ≤ 4·10⁹T e^{−15.449T}; every premise robust in TV dies with an atom near 0 | PROVED (class 𝓔, margin bound); "no estimate" reading ARGUED | ≈110 |
| C7 | **Exact identity + Cauchy–Schwarz / Bochner / Schur** (coercivity, Wiener–Hopf, Kreĭn, de Branges, Hessian in c) | W-lin, W-det, W-fam, N_018, CC_001, BB_001 | C–S only gives upper bounds (wrong direction); the identity holds for every comb | PROVED (N_018, CC4) | ≈130 |
| C8 | **Decomposition in a basis that cancels** (prolates, Galerkin, harmonics, Möbius cells, parity sectors, nodes, kinks) | AUDIT_L_SHARP 1–16, HH/kinks, sawtooth, Z_001 | 33–70 digit cancellation: no piece carries its own sign (restrictions 14, 18, 20, 24, 25, 28) | NO-GO by class (kink, diagonal) PROVED; "non-local cell content" ARGUED | ≈90 |
| C9 | **Flow / homotopy / induction** (de Bruijn–Newman, heat, flow in T, Morse index, Maslov, Grönwall in c, continuation over combs) | N5, R164_502, BARRIER_W/D2, SPEC_A, D8, PROOF_H | n₋ is monotone and crossings have a single sign; index constancy is exactly what has to be proved; interpolation from integers is NO-GO | PROVED (W1–W3, D2 Thm 1, D8); SPEC_A with identities only OPEN | ≈100 |
| C10 | **Global object never built** (surface Spec ℤ⊗Spec ℤ, Hodge index, h⁰, Arakelov, F₁, scaling site, condensates, G-F, MW-5) | phases 135/145/149, RH2025, backward map d1, front F, INV_B/C, phase 196 | no death by theorem. The object is missing. INV_C Thm 4 rules out measures on log ℚ and MW-3 only falls into three classes | OPEN (missing construction, not impossibility) | ≈180 |

Outside these ten classes there remain ≈200 routes of statistics and numerical phenomenology (RH2017–RH2020, RH2022–RH2024), refuted or
merely NUMERICAL, with no sign mechanism to classify.

Reading of the table: nine of the ten classes have a **class theorem** (PROVED) or an explicit falsifier. The
only one not dead by theorem is C10, and it is not dead because no object was ever written down to prove anything against.
BARRIER_001 Thm 3 (T ≥ 0.60) says every method with premises from catalog 𝒜 falls into one of three exits:
comb-generic, certificate ≤ λ_P, or REF-D. The statement is PROVED except for A2 ∧ loose FE, which is ARGUED. This does not reach
C10, because a new object is not a premise of 𝒜.

## 2. Negative space: operations that appear in no route

Criterion: the area does not appear in the index (not even under another name) or appears only as a one-line discard. For
each one, the restrictions from AUDIT_L_SHARP_16 §6's list 1–28 that exclude it a priori are given: 2 (no identity +
C–S), 4 (no multiplier + remainder), 5 (using a_n ≡ 1, residue 1, Γ_ℝ, aliasing n ≈ λ/u simultaneously, and failing for
cΛ/a_P/Beurling), 6 (quadratic leakage scale μ^{−A}dist²), 25 (respecting the 33–70 digit cancellation), and
27 (exact resolvent). An "X" means the exclusion depends on how it is formulated; "open" means no
restriction touches it from the outset.

1. **Nonlinear calculus of variations beyond Euler–Lagrange.** No route uses Morse/mountain-pass theory on the
   Rayleigh functional, Γ-limits with defect, minimizers in spaces with an obstacle, or variational inequalities.
   Γ-convergence and concentration–compactness have a one-line discard on front I. Quasi-minimizers with
   boundary structure (free-boundary regularity theory of the 2ε collar) were never posed. *Why it was not
   tried:* every route reads h* only through its linear EL equation. *Restrictions:* 27 (exact resolvent) does not
   exclude it. 6 bounds it: it would need a quadratic stability estimate (Fuglede type or "sharp quantitative
   stability") and that is exactly a μ^{−A}dist² bound. **Open, and the one that best matches (★★) in form.**
2. **Representation theory beyond Mp₂, Heisenberg, Hecke, and ax+b.** Missing: Mackey induction for the pair
   (ℚ^×_{>0} ⋉ ℝ), multiplicities of restricted representations, positivity of characters of non-commutative adelic
   groups (GL₂(𝔸) only via Hecke), positive spherical functions, geometric quantization and
   Kirillov positivity. *Restrictions:* 2 and 5 threaten it, because every character is a linear identity on the space of ideals
   (C1 risk). **Open only if the object is a multiplicity (a non-negative integer) and not a character.**
3. **Combinatorics and probability beyond Lee–Yang, Knauf, FKG, and multiplicative chaos.** Never appearing:
   couplings between the Λ process and a reference one, Talagrand transport inequalities on the divisor
   lattice (Talagrand appears only as "no disorder"), martingales in the filtration by primes p < X, large-deviation
   theory for the spectral measure of the window, or positivity via bijective counting of pairs (m, k, n)
   with m ≈ kn. *Restrictions:* 4 excludes martingales with remainder. No restriction excludes the bijective
   count, but front M (PROVED: site arithmetic carries no information) bounds it. **Open in the
   bijective variant over comb positions (S⁺), not over sites.**
4. **Logic and model theory beyond proof mining and o-minimality.** Missing: compactness and ultraproducts (the
   limit μ → ∞ as a form in an ultraproduct of windows), nonstandard analysis of the infinitesimal collar, and model
   theory of valued fields (only a Berkovich discard exists). *Restrictions:* none excludes it a priori. But the
   transfer is a logical equivalence and produces no sign: it would be REF-D unless the ultraproduct carries a
   "free" positivity (e.g., a global object in the limit, which would connect to C10). **Open as a
   source of C10 objects.**
5. **Discrete geometry and lattices beyond Möbius lines.** Missing: infinite-dimensional geometry of numbers over
   the lattice log ℕ ⊂ ℝ^{(primes)} (Minkowski and successive minima), Newton polytopes of the Euler product,
   Voronoi tessellations of the comb, and matroids of the ratio pairs m/n. Bhargava and Lorentzian polynomials are
   discarded in one line. *Restrictions:* 24 (the Möbius lattice structure is mandatory; single-line models
   are invalid) **requires it**, and 25 demands that any lattice form respect the cancellation.
   **Open and aligned with 24.**
6. **Dynamical systems beyond T-flows.** Missing: symbolic dynamics and topological entropy of the dilation shift
   n·, thermodynamic formalism with pressure (Ruelle appears only as a "not of the object" piece), measure rigidity for
   the ×2,×3 action (Furstenberg/Rudolph), and homogeneous dynamics on the solenoid. This last one matters because
   Near equals the Kronecker line minus Haar on the solenoid (PROVED, front H). *Restrictions:* 5 requires reading
   a_n ≡ 1; ×2,×3 rigidity is multiplicative and G1 threatens it. But the Kronecker line is + and ·. **Open: it is the
   only dynamics that sees exactly the Near object.**
7. **Categories and topoi beyond the scaling site.** Missing: categorification of 𝔞_T as the dimension of a Hom
   (positivity of dimensions), categorical traces with even Euler sign, K-theory and cyclicity of the window form.
   *Restrictions:* 13 (the pole couples only through rank-one residues) is compatible. The risk is C10: the object does not
   exist. **Open, and one of the few that produce non-negative integers (C10 + dimension positivity).**
8. **Information and entropy beyond Bakry–Émery and KL.** Missing: Rényi or Wehrl entropy of the Husimi
   function in the window (Lieb–Wehrl relation), entropic uncertainty principles (Beckner–Białynicki-Birula applied to
   the window/comb pair), and channel capacity and Shannon duality for aliasing. Tate–Beckner appears only as an indexed D5.
   *Restrictions:* 6 and 16 (Sonin/PW transfer gap). Entropic uncertainties are dilation-invariant,
   so they are comb-generic unless the weight depends on log n. **Mostly excluded (C1); open
   only with arithmetic weights.**
9. **Tropical geometry and semirings beyond the scaling site.** Missing: the semiring (ℕ,+,·) as a universal
   algebra object (semiring varieties, prime ideals of ℕ[x], Lorscheid blueprint geometry with positivity),
   tropicalization of the Euler product at weight ½, and max-plus algebra of the collar. Tropical and Berkovich appear as
   DEAD in L10, L29, and phase 152. *Restrictions:* 5 requires it (a_n ≡ 1). Choi confirms the tropical wall at the
   curve level. **Excluded in the classical tropical form; open in the blueprint form, which was not tried.**
10. **Nonlinear PDE and geometric measure theory.** Missing: arithmetic Monge–Ampère and isoperimetric
    inequalities, geometric flows with monotonicity (Perelman appears with score 2 and no construction), and
    viscosity comparison principles. *Restrictions:* 11 (no flow argument without the virial bound is admitted) excludes the
    flows. Monge–Ampère is not excluded. **Partially open.**
11. **Genuine additive-multiplicative number theory** (Erdős–Szemerédi only as an estimate). Missing is Erdős's
    1946 theorem (S⁺) used as a structure rather than as a separator. It appears only in front H as a separating invariant.
    *Restrictions:* 5 and the guiding principle require it. **Open: it is the only recorded fact that distinguishes ζ from
    O1–O15 except O7 without being linear.**

Pattern: the open areas (1, 4, 5, 6, 7, 11) share a trait. Either they produce a **non-negative integer or dimension**, or
they produce an **exact quadratic stability estimate**. No route in the corpus produced either of these two things
on the window form.

## 3. Contradictions and tensions

**T1. The margin scale: retracted on the 15th and reinstated on the 16th.** The README's "Correction" retracts the
doubly exponential scale exp(−13e^{2T}): "not used in any proof." Only PROVED λ_A ≤ 4·10⁹Te^{−15.449T} remains.
That retraction is why SPEC_A was reopened. On October 16, "Certified frontier" and PATTERN_001 reinstall
exp(−4πe^{2T}) (Mori) as a "plausible quantitative ceiling," and restriction 6 requires leakage μ^{−A}dist² with μ = e^{2T}. The
same README thus holds two margin scales at once. Reopening SPEC_A depends on which one holds. If Mori's
is confirmed, SPEC_A dies again via (γ) in its estimate-based variant, and only the identity-based variant stays alive.

**T2. Mori's frontier appears verified and unverified at the same time.** In "Certified frontier," ½log15
appears as "CITED, computationally verified" (AUDIT_ZENODO_FRONTIER), while SYNTHESIS §2 and the
"Survey" section say "UNVERIFIED, do not cite." PROOF_L_SHARP_H Prop H.1 already uses μ ≤ 15 as a PROVED base ("Mori
CITED"), and AUDIT_L_SHARP_16 treats it as a certified extremal. Phase 200's mandate requires falsifying against "Mori's
certified extremal." The foundation of the entire L′♯ stretch depends on a label the corpus assigns two different ways.

**T3. The guiding principle versus what the corpus actually PROVED about it.** It was set as vital that the sign come from the
+ / · interaction at m ≈ kn. Front M corrects this with PROVED results: the "+" in p − np′ is cosmetic, site
arithmetic carries no information, and symbol densities cancel exactly. Front J proves the +/·
cycle is **frustrated** (Thm 1.3), and front K that the only ζ-specific fact (anti-diamagnetism) is an
obstruction. Then, restriction 28 says that "the Möbius gap 2 ≤ N < μ is shared by a_P (it is not Λ-specific)."
At the same time, AUDIT_L_SHARP_16 §6 places the residue in the "non-local Möbius cell content," i.e., in
m/n = α/β interactions, again at m ≈ kn. The near-coincidences are the live residue (R9, (S)), and at the same time all
additive-multiplicative mechanisms tried on them turned out cosmetic or obstructive.

Minor tensions recorded:
- The index labeled 89 rows "DEAD [REF-D]" despite its own rule. They were relabeled, but 393 DEAD from Part II
  are still keyword-assigned.
- MW-3 appears as "NO-GO" in the SURVEY table, when it only holds for three classes.
- Lewis–Zagier appears as NO-GO, but is ARGUED.
- Phase 193's front C marked an M^{−3} criticality as fact, which was later retracted as a normalization
  artifact (CA_C_005). Phase 190 had used it.
- The backward map says the **object** is missing (d1, product structure). BARRIER_001 Thm 3 has a universal
  statement about methods, but does not cover new objects. If its scope is misread, it gets taken for a total barrier.

## 4. What the meta layer says the sign object has to be

The list of missing pieces repeats under different names in the backward map (d1: product structure with quadratic h⁰
and a ℤ-structure with finite pairing), MW-5 and the G-F gap (object polarized over ℤ with an ample class and a
trace property), clause (5) of phase 194's specification, P1–P4 of the SYNTHESIS, Problem (R)(11), and
restrictions 1–28. Their intersection says this. The sign object **is not a statement about Λ but a new structure
whose positivity is intrinsic and integral.** It has to be a dimension, a multiplicity, or an intersection form
on a global "square"-type object of Spec ℤ, with quadratic growth. It has to live at **weight ½** (the cell
"weight ½ + global FE + built-in positivity" is empty in the literature) and couple the exact comb values
(a_n ≡ 1, residue 1, Γ_ℝ of conductor 1) with the global functional equation without going through ζ(½+iτ) or place by place. Its
arithmetic content has to be in the **positions and weights of the comb over log ℕ** (successor property (S⁺),
m/n = α/β near-coincidences with their non-local Möbius structure), not in site arithmetic. It must see
Kronecker parity (even levels p^{2j}). Its output has to be an **exact equality or an invariant**, not an
estimate: all slack is spent at scale e^{−cT} or smaller. In the language of (★★), it must deliver quadratic
stability 𝒲_ext ≥ κμ^{−A}dist²(r, 𝒢̄) with the gauge fixed modulo 𝒢̄ and respecting the 33–70 digit cancellation, so
that **the inequality comes out as a corollary of something being a square or a count, and not from a bound**. By the
taxonomy, the only place on the map where this is not forbidden by theorem is C10, the global object, intersected with
open areas 1 (quantitative variational stability), 5 (geometry of numbers on log ℕ), 6 (dynamics of the
Kronecker line in the solenoid), and 11 ((S⁺) as structure). Row D: OPEN.
