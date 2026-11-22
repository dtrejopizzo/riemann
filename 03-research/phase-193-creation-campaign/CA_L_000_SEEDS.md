# CA_L_000 — Front L seeds: exact magic-function constructions (Viazovska, Cohn–Elkies, CKMRV, Radchenko–Viazovska, Cohn–Gonçalves, Delsarte/Turán)

Phase 193. Pen and paper; **no numerics run**.
**No sign contact. No certified negative value for ζ.**

## 0. Corpus check
grep "Cohn–Elkies / Viazovska / magic function / Radchenko" over 03-research, 05-meta: hits R154_013 (Tab. 1(a′),(d): CE dual is
"structurally analogous, different problem"; Fourier-optimisation literature assumes the zeros' location), R157_002 item 50 (Beurling–Selberg /
CE majorants: EXCL by lem:Rrig, cor:nontermwise — termwise-signed), R164_401 (sinc-annihilation = CE device on the theta measure, used to build
FE solutions, no sign), phase-35 doc 101 / index P35-4 (RV interpolation: NO-GO, "refutation weight-independent; needs μ(ℝ)=∞"; modularity of θ
*is* the FE). Index L30 (crystalline measures), L53 (Chirre–Gonçalves–de Laat, absorbed into P46), L54 (Delsarte/Turán on LCA groups, NOT IN
CORPUS), L60 (positive crystalline measures, NOT IN CORPUS). **Nothing in the corpus addresses (i) the attainment/slackness structure that
makes Viazovska's method work, nor (ii) a discrete-primal (site) version of the P46 dual.** Those are the two developments below.

## 1. What makes the sphere-packing method work (three structural inputs)
(V1) **Discrete primal.** The CE LP's primal optimum is a lattice (Dirac comb); complementary slackness forces f to vanish on a *discrete,
known* set (|x|² ∈ 2ℕ for E8), f̂ likewise.
(V2) **Two positive Poisson sides.** Σ_Λ f = vol⁻¹ Σ_Λ* f̂ with *positive* Dirac combs on both sides; the sign conditions (f ≤ 0 off a ball, f̂ ≥ 0)
then give a bound with no estimate.
(V3) **Fourier eigen-decomposition by modular forms.** f = f₊ + f₋ (±1 eigenfunctions), each a Laplace transform ∫ φ(iy)e^{iπ|x|²z}dy of a
(quasi)modular form; the double zeros at √(2n) come from sin²(π|x|²/2), the sign from positivity of explicit modular forms on iℝ₊.
Row D transfer table:
| input | sphere packing | row D window LP (P46 §3–6) |
|---|---|---|
| primal | lattice (discrete) | |F̂_⋆|² dτ (absolutely continuous, full support) |
| Poisson | positive both sides | explicit formula: prime side −v_n (negative), archimedean side indefinite (K-A), zero side = the object |
| vanishing set | known (√(2n)) | prime side: log n (known); spectral side: {γ} (the object) |
| attainment | yes (magic function) | **no** (thm:O, non-attainment) |
| eigen-structure | Fourier ±1, modular | only τ ↦ −τ (FE); Mellin is not Fourier on the comb variable |

## 2. Seeds and pre-screen
Columns: thm:O (exact attainment forbidden); thm:Z (flat-top cert = zero-side smoothing); (D) class (D) / Problem (R): cert admissible only as final
object of a margin-carrying computation; finZ; LC lattice ceilings (AL′ Θ(1/M)); B″ comb-generic; FE FE-class genericity (O8–O12, Epstein O10);
O7 quartets; crit precision λ_A; P35 index P35-4.

| # | seed | thm:O | thm:Z | (D) | finZ | LC | B″ | FE | O7 | crit | P35 | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1 | Exact flat-top magic certificate: w ≡ 1 on [−2T,2T], f_w ≥ λ_A attained, vanishing on prescribed set | **kills** | f_w = Σŵ(τ−γ): reads zero side | — | — | — | — | — | — | — | — | NO-GO (PROVED, CA_L_001 Thm 1.1) |
| L2 | ε-magic family built from Eisenstein/modular Laplace transforms (Viazovska ansatz on u = log x) | ok | zero side | **pre-flag** (TV → ∞, rem:OvsB) | — | — | ? | **kills if construction uses modular data only** | survives (keeps comb) | must be exact to λ_A | weight-indep. | NO-GO for modular-data class (CA_L_001 Thm 1.4) |
| L3 | CE one-sided bound via h ≤ 0 on log n, ĥ ≥ 0 | ok | — | — | — | — | yes | — | — | — | — | DISCARD: gives *upper* bounds on the zero side (Odlyzko direction), CA_L_001 Prop 1.3 |
| L4 | RV interpolation basis on {log n} / on {γ} | — | — | — | finZ | — | — | — | — | — | **NO-GO** | DISCARD (retry of P35-4) |
| L5 | Discrete primal: site LP on prime sites (K-S), PD-extension certificate on X−X | ok (discrete primal) | — | REF-D risk | — | — | ? | ? | ? | ? | — | **SURVIVOR** → CA_L_002 |
| L6 | Bohr/torus certificate: exact optimum on T^X ⊂ Ĝ with slackness on zero locus of P_s | ok | — | REF-D risk | — | — | ? | — | — | Kronecker scale | — | **SURVIVOR** → CA_L_002 §3 |
| L7 | Cohn–Gonçalves sign uncertainty (f, f̂ eventually ≥0, f(0),f̂(0)≤0) on window kernel | — | — | — | — | — | yes | yes | — | — | — | DISCARD: σ_T is not eventually signed in τ in a usable way; the principle bounds a *radius*, not a form; comb-generic |
| L8 | Delsarte/Turán extremal PD functions on [−2T,2T] (L54) | ok | — | **kills**: extremal PD in interval = a certificate whose value is the margin | — | yes | yes | — | — | — | — | DISCARD as sign step; tool only (Krein extension is used in CA_L_002) |
| L9 | CKMRV universal optimality (Gaussian-core energy, interpolation at √(2n)) | — | — | — | — | — | yes | — | — | — | needs discrete radial set | DISCARD: requires (V1)+(V3) on a lattice; row D's discrete sets are log n (non-lattice, density e^u) |
| L10 | Self-dual theta-measure + sinc annihilation (R164_401) as certificate | — | — | — | — | — | — | **kills** (FE only) | — | — | — | DISCARD (retry; R164_401 builds FE solutions, no sign) |

**Survivors:** L5, L6 (one development, CA_L_002). **Least-dead of the rest:** L1/L2 (the literal "magic function for row D"), developed to
record the precise reason of death (CA_L_001), as the brief asked.
