# R160_S5 — Survey S5 of 5: phases 157, 158, 159 and `00-references`

*Surveyor S5 (blueprint `R160_000_BLUEPRINT.md`). Scope: `03-research/phase-157-row-d-mechanism-search/` (9 files),
`03-research/phase-158-row-d-mw5-object/` (8 files), `03-research/phase-159-row-d-two-front-construction/` (152 files:
100 memos `G{1,2}_B{1..10}_R{1..5}`, 50 panel reports `G{1,2}_P{1..5}_R{1..5}`, `R159_000`, `R159_099`), and
the top level of `00-references/`. Pure survey: nothing was computed; no paper, README or earlier file was edited.
**No sign is claimed anywhere in this file.**
a restatement of record). Forms: **[prim]** = `𝔞_T` on `P_T` (bottom `λ^A_T`, i.e. `RD_T`); **[compl]** = `W_T` on
`L²(I_T)` (bottom `λ^W_T`). "Self-label" means a memo's own label that no panel audited.*

**How this was read.** Every README, blueprint, closing decision and synthesis in scope was read in full. Read in full:
R157_001, R157_002 (all 692 lines), R157_004, R158_001 (all 444 lines), the §0 and §5 of R158_002, the verdict tables
of R157_003/R157_006/R158_003/R158_004, R158_006 §0, R159_099. In phase 159 the verdict section (§0 or "Verdict, stated
first") of **every** memo was read, and the proofs of the load-bearing unaudited theorems were opened (G2_B8_R5
§1–§4, G2_B5_R5 §2, G2_B6_R5 §2, the Theorem statements of G2_B2_R4, G2_B6_R2, G2_B9_R3, G1_B4_R4, G1_B6_R2). The panel
report G1_P5_R5 was read in full; the other 49 panel reports were read through R159_099's digest of their §0 tables.
Where this survey gives its own assessment of an unaudited item, it is marked **[S5 assessment]** and is itself
unaudited.

---

## §1 What was done (one line per item, with paths)

Paths are relative to `03-research/` unless they start with `04-`, `05-` or `00-`.

### 1.1 Phase 157 — the mechanism search under the proved filters (CLOSED )

| file | one line |
|---|---|
| `phase-157-row-d-mechanism-search/R157_000_BLUEPRINT.md` | Admissibility filter F1–F5 (F4 amended per R157_004: T1 *prescribes* field uniformity, it does not exclude it); round 1 |
| `…/R157_001_DMV_IMPORT.md` | O-150.1: DMV imported from five open secondary sources; phase-150 misquotation found (integer law is `N(x) = ρx + O(x^θ)`, not `O(x e^{−c√log x})`); (H-DMV′) → CITED (secondary source); Lemma 2.1 (continuation to `Re s > θ`) PROVED |
| `…/R157_002_MECHANISM_SEARCH.md` | 61-row table of candidate mechanisms (after audit: EXCL 39, EQUIV 20, SURV 1 = (P152.2), NOT EXCLUDED 1 = MW-5 cluster); observations O1–O4; one-round Lemma P157.S1 |
| `…/R157_003_AUDIT_DMV.md` | PASS with amendments A1–A8; `η ≡ (1−θ)/2`; independent second model (Zhang, Math. Ann. 337 (2007), zbMATH abstract) + Révész Thm 5; T3 stays a Remark |
| `…/R157_004_AUDIT_SEARCH.md` | 31 amendments; O3 PROVED as an upper bound (Lemma D = P46 `lem:degen` PROVED); O4 = RESTATEMENT (Lemmas C, E PROVED); row 37 (Deninger) un-excluded; rows 56–60 added |
| `…/R157_005_BERKOVICH_TEST.md` | Lemma P157.S1 run on (P152.2), the difference kernel on `A^{1,an}_Z`: Lemma 2.1 (group law relative to `M(Z)`), Lemma 3.1–3.3, Theorem 4.1 (decomposition in class 𝔄) |
| `…/R157_006_AUDIT_BERKOVICH.md` | (P152.2) CLOSED as a RESTATEMENT; class 𝔄 → 𝔄⁺ (Lemmas B.1–B.3); NG-E1 PROVED in strong form; D.195 (3.5) ≡ `RD_T` re-audited |
| `…/R157_007_CLOSING_DECISION.md` | Labels of record; "no survivor with an object; MW-5 cluster not excluded, with no object" |

### 1.2 Phase 158 — building an MW-5 object (CLOSED; one post-closing memo)

| file | one line |
|---|---|
| `phase-158-row-d-mw5-object/R158_000_BLUEPRINT.md` | Option (B′): build an MW-5 object testable by F1–F5 |
| `…/R158_001_SPEC_SHEET.md` | W-1…W-6 (Weil over `F_q` in P46 language); constraints C1–C27; Lemma T; positive list P1–P7, negative list N1–N11; object test OT-1…OT-12; 18 frameworks run through it (none passes) |
| `…/R158_002_ADELE_CLASS_FOLIATION.md` | `X = A_Q/Q^×` as a Deninger-type object: Lemmas A, D, E, U, Construction C, Props B, H; Theorem 158.2-G: every positivity structure on `X` is a restatement, compression, false or void |
| `…/R158_003_AUDIT_SPEC.md` | Sheet accepted with A1–A20; Lemma T CLASSICAL; Connes' adèle-class entry moved from OT-5′ to OT-2 (global trace formula ⟺ RH); OT status table (Rem 3.0); reopening rule Rem 3.3 |
| `…/R158_004_AUDIT_ADELE.md` | Verdict holds with A1–A25; Fact 4.6a.7 false as stated (CCM's form is `B_{ξ′}`, odd multiplier); new `S₃` falsifier; corpus-check failure recorded (Lemma U, Construction C not novel) |
| `…/R158_005_CLOSING_DECISION.md` | "The whole content of MW-5 is OT-5′"; N-a, N-b, N-c; MW-5 stays NOT EXCLUDED, unbuilt |
| `…/R158_006_O0_MEYER_K.md` | **Post-closing, unaudited, not in the README.** Meyer (Duke 2005, math/0311468) read; Theorem J_K (Jordan chains of length `m_ρ` over any `K`), Prop S, Cor F (`S₃` falsifier) self-labelled PROVED |

### 1.3 Phase 159 — two fronts, 30 memos, 5 rounds (NOT ACHIEVED on either front)

Blueprint `phase-159-row-d-two-front-construction/R159_000_BLUEPRINT.md`; synthesis `…/R159_099_SYNTHESIS.md`.
Best G1 score 1/5 (three times, always "negative structural result only"); best G2 score 0/5.

**G1 (the object), by memo** (all files `phase-159-row-d-two-front-construction/G1_B{k}_R{r}.md`):

| memo / angle | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| B1 scaling-site square | Thms A (idempotent collapse), B (homogeneous cone), C (Riesz characterisation of bounded density), E (sum-graph axiom = RH), Prop F *(unaudited)* | Thm H′ (Krasner coefficient absorption), Thm J (standard-part principle), Prop M (Maslov) *(unaudited)* | two-horn theorem; **Thm T(iii)/Cor T.1 refuted** (G1_P3_R3 §1.3) | orbit-closure work | O1–O4 Weil-number law at closed orbits; ergodic DK_α excluded (repair E-P5.19) |
| B2 Deninger laminations | suspension of `A_K/K`, own Cor D1/D2 (`H¹ = 0`) | Hecke/Shimura suspension; Thm E(i) false as stated, repaired | Cor H: prime-local operator carriers empty (Hardy) | Cor M1: codim-one DK_α excluded | Thm R (III₁ law), Cor R1, Thm U (measured universality), Prop NH (natural gluing not Hausdorff) |
| B3 FF / condensed | Thm C slope-½ Serre lemma = restatement | Thm I (Iwasawa = compactness), Prop WA, Lemma S′, Prop C_δ, Prop AP *(unaudited)* | Thm W integer-weight wall, Thm F *(unaudited)* | gap wall G (weaker duplicate of B4 W♯) | flat wall F, Euler wall E (`χ_Co = 0`) |
| B4 Arakelov / Faltings–Hriljac | FH-1…FH-5, Lemma 4.4 *(unaudited)* | Thm A (flow–integrality incompatibility), Example E, Thm C *(unaudited)* | tail wall W | **Thm W♯ (sharp tail wall), Prop Σ** | Thms R/R′ (rationality wall, six exponentials) |
| B5 Borger / Witt / Bost–Connes | Thm A (Witt descent forces a conformal form), Thm B (`Γ_1·Γ_n = Λ(n)`), Thms C, D *(unaudited)* | Thms E, F, G, Props H, K *(unaudited)* | Thm 1 Witt–Kronecker | Thm K covariant `log N`-stability; Cor K5(a) false as stated | Thm E eigen-sector; Thm G (constant repaired) |
| B6 operator algebras | Sz.-Nagy bridge; Cor 8.1(iii) overclaim | **Thm A** (window constants grow linearly on Construction 9), Thm B resolution law, N-e | Cor D1 (needs P3 repair + CITED Selberg density); Thm C(iv)/D(b) unproved for `a < ½` | relative-trace law Δ ("finite split ⟺ RH", EQUIV) | stratification Thm S (Mackey imprimitivity) |
| B7 motivic | numerical motive `𝔐_Z` = restatement | Thm L, Thm B (Baker rank), Thm Q1 *(unaudited)* | contraction wall, Prop BL | Thms A, B (minimal genus `c_* = 2(√2+1)log 2`), Props G, L *(unaudited)* | Thms A″, Γ₀, Γ (genus law), Prop Σ_ζ, Cor M′ *(unaudited)* |
| B8 canonical systems | Nehari norms of Suzuki's kernel | Landau-type growth law Thm G | Thm L local-gauge no-go *(unaudited)* | echo law, Thm K (chains excluded on `(½log3, log 2)`, CITED Romanov) | Lemma A′, Thms J, U (Kreĭn rigidity) *(unaudited)* |
| B9 function-field transport | `q → 1` closure = Bochner cone | Bombieri–Stepanov transport (corrects R157_002 row 29) | `g → ∞` limit, Thm E exhaustion *(unaudited)* | F–V rebalancing on E×E | Thm G theta pull-backs (O-37 closed over `F_q`) |
| B10 probabilistic ladders | Cauchy damping | Gaussian ladder, `ε_G ≤ 1` | Landau cap (Thms 1–3) *(unaudited)* | Thm K Koopman power law, Thm S *(unaudited)* | Thm P phase–power law, Cors Z, E, Thm F′ *(unaudited)* |

**G2 (the mechanism), by memo** (files `…/G2_B{k}_R{r}.md`):

| memo / angle | R1 | R2 | R3 | R4 | R5 |
|---|---|---|---|---|---|
| B1 structure vs randomness | centre identity `C_0 = −2ζ′/ζ(½)` | Thm R, Thm S, Prop F *(unaudited)* | Thm G, Prop Z, Prop E *(unaudited)* | graded converse Thm Q | arithmetic resonators, Prop P (class-level, killed by `cor:void`) |
| B2 bootstrap in `T` | exact annulus renormalisation | sieve flow Ψ, Prop Ψ4 | Thm NB trichotomy, Lemma H *(unaudited)* | **Thm U (upper half, conditional on (BD)), Thm G1, Lemma T** | Lemma L (Lorentzian identity), Thm I (window Bombieri index), Thms U₂, M *(unaudited)* |
| B3 Hermitian squares / convolution identities | **Thms A, B, C** (twist obstruction; `L_2 = ζ(1−2^{−s})/(1+2^{−s})` negative [compl] for `T ≥ 0.38`) | Thm H (Hamburger), Prop G, Thm F *(unaudited; Thm H later adopted by the B9 panel as a citation)* | Thm K (door = RH), Thm S (Selberg split) *(unaudited)* | Landau converse | Lemma A (atom forcing), Thm S (separation), Cors S1, S2 *(unaudited)* |
| B4 SOS / Positivstellensatz | covariant SOS = zero-side SOS; Baker no-go | **Thm R** (fixed/convergent edge profiles fail) | Thm R′ (dilated profiles) *(unaudited)* | Lemmas E1–E3, Thm R′_prim *(unaudited)* | Thm PT, Cor RC, Thm RN *(unaudited)* |
| B5 de Branges window time | canonical system `H ≥ 0` up to `T*(λ)` | Thm L localisation, Thm Φ′ *(unaudited)* | problem `H∞`, Lemma G inverse rigidity *(unaudited)* | Gram converse (EQUIV) | Thm Q♯ (no recovery windows) *(unaudited)* |
| B6 finite/random zero universes | Thm H, Props S, R | **Thm M: `λ^A_T ≤ exp(−e^{(2−ε)T})`** | Prop D, Lemma E re-derived, Prop T′ *(unaudited)* | Thm P (BRS uniqueness), Cor P2 | Lemma S closed, Thm X (Λ extreme point), Prop C, Thm F *(unaudited)* |
| B7 almost periodicity / Kronecker | Bohr–Jessen twist; Thm C = Wintner 1944 | Thms A_ℂ, B_ℂ, H, K *(unaudited)* | Thm L (Laplace in `T`), Thm T (growth `2(Θ−½)`) *(unaudited)* | Thm P one-generator rigidity (Li–Radziwiłł) | Lemma C (Cesàro projection), Thm M (density rigidity) *(unaudited)* |
| B8 Lee–Yang / Pólya–Schur | Thms B, S, Lemma H | Thm R (coupling ray), Cor R′ (`ζ^k`), Prop K (conductor) | Thm L, Remark B, Thm NM | Thm L′, Prop M | Thm D (minimax duality), Lemma Mon, Thm L″ — **all rounds unaudited** |
| B9 jump calculus | contact modulus bound | Thm R (rigidity at `T = ∞`, under RH), Cor R1 | **Thm R′ (unconditional), Thm N, Lemma L** | doubling inequality, graded converse | Thm S (resummation), Thm L, Cor L1 *(unaudited)* |
| B10 mollifiers | Thm M1, Thm N, Prop W-M | Prop L1, Thm H (harmonic rigidity), Thm N±, dichotomy D | Thms M1, M3, Prop M2, Thm B | Lemma Λ, Thms Γ, Q, L(θ), R_s, Prop S | Thm Γ_f, Thm H ("T2 for mollifiers"), Prop J — **all rounds unaudited** |

**Panels** (`…/G{1,2}_P{1..5}_R{1..5}.md`): P1 line-by-line, P2 restatement detector, P3 counterexamples, P4
literature/corpus, P5 falsifiers + inverse check. Their verdicts are digested in `R159_099` §1.1, §1.3, §2.1, §2.3.

### 1.4 `00-references/` (top level; what each source proves that a memo can use)

Read this pass at abstract / main-theorem level (pdftotext of the local copies); nothing below is re-verified.

| file | content usable by a memo | label / caution |
|---|---|---|
| `00-references/2006.13771v1.pdf` (Connes–Consani, *Weil positivity and trace formula, the archimedean place*, 2020) | Thm 6.11: for `g ∈ C_c^∞` supported in `[2^{−1/2}, 2^{1/2}]` with `ĝ(−i/2) = 0`, `W_∞(g∗g*) ≥ Tr(ϑ(g) S ϑ(g)*) − c|ĝ(0)|²`, best constant `13 < c < 17`; hence `W_∞(f) ≥ 0` for positive-definite `f` supported in `[½, 2]` with the moment conditions. Root of positivity: compression of the scaling action to the Sonin space. Archimedean place only | CITED. In P46 terms this is archimedean positivity at `T ≤ ½log 2`. P46 `prop:archneg` (complete archimedean form negative from `T = 0.4608`) and `cor:Tarch` (`0.58 ≤ T*_{∞,P} ≤ 0.60`) cap every archimedean-only positivity; R157_002 row 34 EXCL as a uniformity mechanism |
| `00-references/connes-moscovici-2022-…pdf` (PNAS 119 (2022)) and `draft4.pdf` (the longer arXiv 2112.05500 version) | Unique self-adjoint extension `W_sa` of the prolate operator `W_λ = −∂(λ²−x²)∂ + (2πλ)²x²` on `L²(R)`, commuting with Fourier; discrete spectrum unbounded both ways; eigenvectors of negative eigenvalues lie in the Sonin space; the **semiclassical** count of negative eigenvalues reproduces the **UV (asymptotic) behaviour** of the squares of the zeros (λ = 1, √2); isospectral Dirac family | CITED. The match is asymptotic (Riemann–von Mangoldt density), not the zeros. Self-adjointness gives reality of the spectrum of `W_sa`, which is not ζ's zero set. R157_002 rows 34, 60 |
| `00-references/2310.18423v2.pdf` and `Zeta-zeros-and-prolateproofs-final-2024.pdf` (Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators: semilocal adelic operators*, published 2024) | Semilocal prolate operator; Thm 1 (= Props 4.1–4.2): `F_μ w_S(η_S(f))(s) = ∏_{p∈S∖∞} L_p(½ − is)·(F_μ w_∞ f)(s)` (exact semilocal factorisation); stability of the semilocal Sonin space when `S` grows; relation to Hilbert spaces of entire functions; metaplectic picture | CITED. Finite `S` only. P46 `thm:SC`, `prop:finsupp` (PROVED) exclude deriving the sign from finite `S`, including infinite-support finite-mass `S` (R157_004 A11). G2_B8_R5 (unaudited) shows Euler-factor-local certification fails from `T ≈ 0.59` |
| `00-references/2301.00421v3.pdf` (Suzuki, *On the Hilbert space derived from the Weil distribution*) | Under RH the Hilbert space of the Weil form on `C_c^∞(−a, a)` is isomorphic to a de Branges space; RH-equivalences as series of equalities | CITED; EQUIV (R157_002 rows 38, 39; read in R154_031 §3) |
| `00-references/2307.06748v1.pdf` (Connes–Consani, *On the metaphysics of F₁*) | `Z` as `𝕊[X]` over the sphere spectrum with `1+1 = X+X²`; Riemann–Roch for `Spec Z̄` (integer dimensions, **logarithmic** growth) | CITED. P47 Thm 19.25 / Cor 19.25b kill every `h⁰`/RR-growth reading (R157_002 row 35); growth is logarithmic (MAP_5; P47 X17) |
| `00-references/1001.0448v3.pdf` (Yoshitomi, *Generators of modules in tropical geometry*) | Tropical modules, generators, tropical RR background | CITED; not attached to ζ (same class as the tropical Hodge-index row of R158_001 §4: OT-2 fails) |
| `00-references/arXiv-2511.11199v1/RH.tex` (*The Riemann Hypothesis emerges in dynamical quantum phase transitions*) | Physics: zeros ↔ DQPTs of two quantum systems; five-qubit experiment; quantum-simulation proposal for **numerical verification** | Not usable for a proof: a realisation/numerics; at best a Hilbert–Pólya-type restatement (R157_002 row 32) |
| `00-references/beurling-dmv/` (5 arXiv texts + zbMATH record; primary DMV Math. Ann. 334 (2006) not held) | (H-DMV′): a discrete Beurling system with `N = ρx + O(x^θ)`, `θ < 1`, zeros `β_n → 1` | CITED (secondary source) only (R157_001 §3, R157_003); feeds T3 = P47 Rem 27.16 (METHOD-CONSTRAINT modulo that import) |
| `00-references/PROLATE-REFERENCES.md` | Slepian–Pollak, Landau–Pollak, Landau–Widom (asymptotic only), Bonami–Karoui (non-asymptotic decay), Osipov–Rokhlin–Xiao, Israel | bibliography only, CITED-NOT-VERIFIED; G2_B6_R3 §5 places Theorem M as a Slepian–Landau–Widom "plunge" statement |
| subfolders `papers-nuevos/{A,B,C,D,…}`, `papers-ref-2`, `papers-ref-phase-60` | described in `00-references/README.md`: CC arithmetic/scaling site, RR strategy, ζ-cycles (A); Deninger (B); foliations, Connes 1999 spectral interpretation (C); arithmetic Hodge index for adelic line bundles (D); CCM prolate programme; Connes "letter to Riemann" | not re-read here; R158_001 §4 and R158_002 §1 read the relevant ones (Deninger math/0204110, Leichtnam 1307.3851, Meyer math/0412277, CCM math/0703392, Connes math/9811068) |

---

## §2 What FAILED and exactly why (do not repeat)

Each line: the idea, the theorem or counterexample that kills it, the file. "Walls" = unconditional exclusions.

### 2.1 From phase 157 (R157_002 as amended by R157_004; closing R157_007)

1. **Any mechanism "supplying uniformity in `T`" on the side.** O1 (RESTATEMENT, R157_002 §1.2, audited PASS in R157_004
   §1.3): by `lem:monoT`, `∀T λ^W_T ≥ 0` *is* Weil positivity on `C_c^∞(R)`. A uniformity mechanism is a proof of Weil's
   criterion, no more and no less. The per-window language supplies filters, not an object.
2. **Estimate-type inputs per window** (PNT error terms, zero-free regions, zero density, Levinson–Conrey outputs, sieve
   bounds, bilinear estimates as outputs, dlVP/Rankin amplification): P46 `cor:void`, `thm:finmod` (PROVED) and O3
   (`rem:resweights`; PROVED as an upper bound, vacuous for `T ≤ 1.51`, needs the OPEN non-degeneracy) — R157_002 rows 20,
   21, 30. Globally they must prove `ψ(x) − x ≪ x^{½+ε}` = W4 (P47 Thm 27.10).
3. **Quasi-RH outputs** (zero-free strips, `β < ¼` resonance gaps, `Λ_dBN ≤ t`, `κ < ∞`, density-one): O2 as a
   derivation schema (R157_004 A8) with P45 Thm 10.4.
4. **The 61 table rows** (`R157_002` §2). EXCL rows (with killing statement): D-HS, D-θ (P47 Thm 19.25, Cor 19.25b);
   Pontryagin `κ < ∞` (Paper 11, O2); Paper 36 ARP-P / Li–Keiper / Bombieri–Lagarias / sliding windows (`cor:Li`,
   `lem:Rrig`); sixteen positivity-transfer attacks (Paper 37, `lem:Rrig`, `thm:SC`); CCM/Suzuki cofinal finite operators
   (P41 P1–P3, `thm:O`); nodal criterion P8 (`thm:arena`); prolate concentration floor and CC/CCM archimedean positivity
   (`prop:archneg`, `cor:Tarch`, `thm:index`, `thm:J`); finite compressions / computer-assisted windows (`thm:N`,
   `thm:Np`, `thm:arena`, `thm:finZ`, `thm:margin`); exact finite dual certificate (`thm:O`, `lem:Onat`); rate lemmas
   (`thm:Vp`, `prop:env`); upward induction (`cor:mono`, `lem:monoT`); sub-comb / finite `S` / semilocal (`thm:SC`,
   `prop:finsupp`, infinite-support case PROVED by R157_004 A11); local–global (`thm:SC`/`prop:finsupp`, NG-E1); Deligne
   route (P47 T5 Thm 27.3, T6); Laumon over Z (rationality wall, `thm:finZ`); frame enlargements (P47 Thm 22.17, Lemma
   24.1, Thms 24.10, 25.6–25.7, 26.13, 26.17); Mayer/Lewis–Zagier/FUP (R152 Props A.2, A.4); Berkovich tree potential
   theory (R152 Prop B.3); `×p` rigidity / Kronecker discrepancy (`cor:void` on `C_supp`); o-minimality (arg., scoped);
   Stepanov/Baker (`C_BT`, rationality); Bost–Connes KMS (real axis); GUE/Katz–Sarnak; Selberg-trace analogues;
   Weil–Deligne transported (P47 Thm 21.15, T5/T6, `thm:finZ`); probabilistic models; extremal functions / LP / SDP
   (`lem:Rrig`); SOS with arithmetic squares (P41 P1, `thm:O`); Voronin, Fourier interpolation, sum–product, prismatic,
   functoriality, quantum chaos (closure plan §10.2); Weng / Lagarias–Suzuki; Selberg `μ∗log² ≥ 0`; ζ-cycles/Sonin per `L`.
   EQUIV rows: KEP (`thm:KEP3`(b)), Connes scaling on Pontryagin space, P6 band, first crossing (O4), Weil/Bombieri,
   Hilbert–Pólya, Suzuki screw, de Branges/HB, Laguerre–Pólya full order (P15 `thm:hr`), dBN (P13 N5), Lee–Yang /
   Kurasov–Sarnak, Nyman–Beurling/Báez-Duarte/Burnol, Kreĭn extremal extension, Nicolas/Robin/Mertens/Riesz, horocycle
   equidistribution, Balazard–Saias–Yor, Lax–Phillips/Pavlov–Faddeev (`β = ¼` is RH), Selberg-class axiomatics.
5. **(P152.2), the Berkovich-line difference kernel on `A^{1,an}_Z`** — CLOSED as RESTATEMENT (R157_006; not an
   impossibility): the additive law of `A^{1,an}_Z` is relative to `M(Z)` (R157_005 Lemma 2.1, PROVED), so difference
   kernels see only same-fibre pairs; the only cross-place coupling is the product formula along integer sections, which
   reproduces the Weil local decomposition `W = Σ_v Q_v` with indefinite summands (Lemma 3.2–3.3); every energy in 𝔄⁺
   that reproduces `W` is the explicit formula, D.195 (3.5) ≡ `RD_T`, a finite-prime form, or P46's dual (D) (Theorem
   4.1 in 𝔄⁺ with Lemmas B.1–B.3). Exhaustion of 𝔄⁺ over the literature: CITED/HEURISTIC (Chinburg–Rumely unread).
6. **"Determinate Kreĭn datum at a first crossing"** (O4's clause): FAILS as stated (R157_004 A6): at `T_c` every KEP
   solution, *if any*, is atomic on `F̂*^{−1}(0) ∩ R`; solvability and uniqueness are unproved.
7. **T1 read as an exclusion** (old F4, rows 12, 37, 45, 48): a misreading, CORRECTED (R157_004 A9; P47 Rem 18.1a). A
   field-uniform argument is admissible and must prove GRH for all `K`.

### 2.2 From phase 158 (R158_001–R158_005)

8. **Deninger/Serre data as axioms.** Lemma T (R158_001 §3.1; PROVED, content CLASSICAL): (D1)–(D3) are satisfiable iff
   RH; (⇒) holds for every realisation (Serre; Deninger math/0204110 Thm 2.1; Leichtnam 1307.3851 §2, Comment 6), (⇐) is
   the spectral witness built from the zeros. A postulated conformal form (D3) is RH-equivalent. **The whole content of
   MW-5 is OT-5′** (R158_005 §1).
9. **Eighteen published frameworks** fail the object test (R158_001 §4, amended A17/A18): first failure OT-1 (9: arithmetic
   site, scaling site, RR strategy, RR `Spec Z̄`, Deninger formalism, Deninger `W_rat` systems, Borger, Haran,
   Deninger–Singhof with OT-12); OT-2 (7: Connes' adèle class space — global trace formula ⟺ RH, CC archimedean, Leichtnam
   `p`-adic, AKL, Kopei, Arakelov, tropical); OT-3 (Deninger elliptic example: metric built from Hasse `|ξ|² = q`); OT-5′
   (Morishita). The only *derived* positivities (Deninger–Singhof, Faltings–Hriljac, tropical) live where ζ cannot
   (compact manifold: `α = 0`, no fixed points, Deninger Cor 3.5 Rem 2–3; no square over `Spec Z`, P47 Thm 22.17; not ζ).
10. **The adèle class space `X = A_Q/Q^×` as the MW-5 object** — CLOSED as RESTATEMENT on `X` (R158_002 Theorem 158.2-G,
    audited R158_004): Connes' Hilbert realisation fails OT-2; Meyer–CCM's nuclear `H¹` passes OT-2 and then OT-5′ *is*
    Weil's criterion. Components: Lemma A (no leafwise `H¹` on `C_Q`, PROVED); Lemma E (every compatible hermitian form
    definite ⟹ RH ∧ simple zeros; classical); E-i (canonical residue polarization `B_1` indefinite, unconditionally, PROVED);
    E-ii (`B_{Φ₀}`, `Φ₀ = (s−½)ξ′`, semidefinite ⟺ RH); Prop H (a definite multiplier has infinite exponential type, PROVED
    and new); Lemma U (Deninger unitarity ⟺ RH ∧ SZ; CLASSICAL, Serre + Connes 1999 Jordan remark); Prop B (CCM Prop 7.2
    over Q = E1 test by test, Castelnuovo form; P47 (18.2) is weaker per test); Construction C (flow-commuting `⋆`
    exists but is defined from the spectrum: OT-3 fails).
11. **Unitarity routes over non-abelian fields.** `S₃`-field falsifier (R158_004 A20; upgraded by R158_006 Cor F,
    unaudited): `ζ_K = ζ L(χ_{−3}) L(ρ)²` has infinitely many zeros of order `≥ 2`, and on Meyer's `H¹_{K,1}` they are
    Jordan chains, so no positive-definite `Θ`-compatible hermitian form exists there **whatever GRH says**. With T1, a
    field-uniform (P-HS) unitarity route proves something false.
12. **"No `J`-linear Frobenius" read as general** (phase 63; MAP_3 row 63 "PROVED-IMPOSSIBLE"): CORRECTION, scoped to
    that `J = σ∘(i⋆_win)` (R158_004 row 4′; R158_005 §1).

### 2.3 From phase 159, G1 (the object) — the unconditional walls (R159_099 §1.2–§1.3)

13. **Tail-factorizable Frobenius** (any carrier whose Frobenius factorises over primes in the tail): at most one critical
    point per summand. Sharp form **Thm W♯** (`G1_B4_R4.md` §0; PROVED, PNT CITED; checked 5/5): holds for uniformly
    Cesàro-bounded tails, uniformly bounded tails, and blocks of bounded size with `‖T_{j,p}‖ ≤ g(p)`, `Σ g(p)^{−2} = ∞`
    — includes the trivial degree bound `‖F_p‖ ≤ Cp`; exactly sharp by Prop Σ. Earlier copies: G1_B3 Thm G, G1_B2 Thm I,
    G1_B7_R3 Thm C.
14. **Algebraic (`Q̄`) structures**: **Thm R/R′** (`G1_B4_R5.md`; PROVED modulo the CITED six-exponentials theorem): no
    zero is a joint Frobenius exponent on a `Q̄`-structure at `≥ 3` primes. (Cor FH is a list, E-P5.22.)
15. **Covariant flows**: `G1_B5_R4.md` Thm K (`log N`-stable spectrum; Cor K5(a) false as a characterisation when
    `κ > #pairs`, G1_P3_R4); `G1_B5_R3.md` Thm 1 (Witt–Kronecker); `G1_B5_R5.md` Thm E (eigen-sector) — zeros enter only
    on the Rosati part `H_u` by installation.
16. **Canonical operator-algebra functionals / crossed products**: `G1_B6_R4.md` law Δ (absolutely continuous flow
    spectrum; "finite split ⟺ RH" is EQUIV), `G1_B6_R5.md` Thm S (Mackey imprimitivity; atoms are installation).
17. **Time-weighted / strip-Hardy carriers for (P-HS)**: `G1_B6_R2.md` **Thm A** (PROVED unconditional, 5/5):
    `sup_{|s|≤T} ‖U_s|H¹_w‖ ≥ (2n_w/πK_w)T − 1`, so OT-5′ (P-HS) is *false* there; Thm B (resolution law): any quotient
    carrier with topology fixed before the spectrum must resolve the zeros at their spacing `≍ 2π/log γ` (N-e:
    super-critical topology); `G1_B6_R3.md` Cor D1 (modulation-invariant carriers, only with P3's repair + CITED Selberg).
18. **Prime-local operator carriers**: `G1_B2_R3.md` Cor H (empty, via Hardy); codimension-one DK_α (`G1_B2_R4.md` Cor
    M1); the natural suspension is not T₁ / not Hausdorff (`G1_B2_R5.md` Prop NH); suspended `H¹ = 0` (G1_B2_R1/R2 Cors
    D1/D2, zero-blind, C16).
19. **Finite-trace and ergodic conformal (DK_α) carriers**: `G1_B3_R5.md` Thm F (flat wall, `dim Ĥ¹ ≤ d` under (FT),
    (IBP), (R), (D)), Thm E (`χ_Co = 0`); `G1_B1_R5.md` O1–O4 (Weil-number law at closed orbits; ergodic carriers carry at
    most one pair; closed orbits μ-null) — under (C), (Def), (Sm)/(Orb), with the one-line repair E-P5.19.
20. **Measured transverse dynamics as carrier of arithmetic**: `G1_B2_R5.md` Thm U (PROVED modulo CITED Connes–Haagerup,
    under amenability): the core flow is that of `R_∞`, the same for a ζ-object, for any Beurling-type system and for
    Bost–Connes at `β = 1` — "carries no arithmetic".
21. **Hodge / twistor / Fargues–Fontaine polarizations**: `G1_B3_R3.md` Thm W (integer-weight wall; elementary; *unaudited*):
    a torus-weight flow has `Θ`-spectrum in `Z`, so the Lefschetz trace is smooth and can never equal `eq:W`, whose prime
    side has atoms at `±log p^k` — OT-2 fails unconditionally; Iwasawa positivity is compactness and cannot act on the
    scaling flow of Q (`G1_B3_R2.md` Thm I); the FF product class is Euler-factorizable (`G1_B3_R3.md` Thm F); Weil–Arakelov
    cohomology is zero-blind (`G1_B3_R2.md` Prop WA, conditional on Flach–Morin conjectures; made unconditional by Cor W2).
    The slope-½ "OT-5′ automatic" of G1_B3_R1 was a redefinition (restatement).
22. **Faltings–Hriljac over Spec Z**: `G1_B4_R1.md` (scheme square has MW group `{0}`; arithmetic surfaces have finite-rank
    positive spaces; `J(Q̄)⊗R` has only trivial arithmetic flows; Lemma 4.4: no abelian variety in characteristic 0 carries
    commuting `φ_p` with `φ_p†φ_p = p` for a density-1 set of primes) and `G1_B4_R2.md` Thm A (a countable set invariant
    under a continuous flow is pointwise fixed ⟹ integral structure and continuous Frobenius flow are incompatible) —
    *both unaudited*.
23. **Borger/Witt square**: `G1_B5_R1.md` Thm C (the unique Λ-Rosati form on `L²(R_+, x^{−2}dx)` is zero-blind: `E^♭` has
    dense range, cokernel 0), Thm D (every other continuous PSD Λ-Rosati form is `∫|Ĝ|²dν`, reads the zeros or is Weil's);
    `G1_B5_R2.md` Props H, K (ghost-cycle form has infinite positive and negative index; no normalisation makes `F_k`
    conformal) — *unaudited*.
24. **Scaling-site square cones**: `G1_B1_R1.md` Thm C (a class satisfies the frame's bounded-density bound iff it is a
    positive Radon measure on `[−∞, +∞]`; so Cor 19.25b's kill extends to the whole homogeneous tropical cone), Thm A
    (characteristic-one `+` is idempotent: the trace term `a` of `deg(m+nπ)` drops out); `G1_B1_R2.md` Thm H′ (Krasner
    hyperring counts are 0 or diagonal), Thm J (infinitesimal enlargements do not escape), Prop M (Maslov: genuine `+`
    and Frobenius endomorphisms never coexist) — *unaudited*. `G1_B1_R3.md` Thm T(iii)/Cor T.1 ("third horn = RH") is
    **refuted** (G1_P3_R3 §1.3: an intermediate salient cone with gate, ample `2K` and all witness classes exists).
25. **Motivic (Rosati trace on `C[Q^×_{>0}]`)**: `G1_B7_R4.md` Thm A (orbit-faithful traces have infinite genus: `c ≥
    λ_max(A′_N) ≥ log N − O(1)`), Thm B (minimal genus `c_* = 2(√2+1)log 2 = 3.3468…`, attained by a Künneth trace that
    carries no zero), Props G, L; `G1_B7_R5.md` Thms A″, Γ₀ (no Radon polarization carries the prime atoms), Γ (genus law
    `d(ε) ≥ log(1/ε) − log(1+log(1/ε)) − C`), Prop Σ_ζ (ζ saturates it) — *unaudited*.
26. **Probabilistic / determinantal carriers**: `G1_B10_R3.md` (horizontal Laplace positivity Landau-capped at `Re s = 1`,
    T3-uniform; vertical Bochner positivity = Weil), `G1_B10_R4.md` Thm K (Koopman power law: point spectrum of any
    measure-preserving flow is closed under `λ ↦ nλ`; with Li–Radziwiłł, no such flow has nontrivial point spectrum inside
    the critical ordinates, even after `λ ↦ κλ + β`), `G1_B10_R5.md` Thm P (phase–power law in standard form), Cor Z
    (zero-carrying ⟹ nilpotent phases, Pauli rule), Cor E (no normal invariant state ⟹ empty point spectrum), Thm F′
    (bounded fields inherit the one-particle spectrum) — *unaudited*. Randomisation is inert (G1_B10_R1); damping ladders are
    restatements (`RH ⟺ ε_G = 0`, G1_B10_R2).
27. **Canonical systems (Suzuki kernel)**: restatements (G1_B8_R1/R2, Herglotz/Lagarias); Frobenius-local concatenated
    chains excluded on `(½log3, log 2)` (`G1_B8_R4.md` Echo Lemma E, Thm K, mod CITED Romanov; the ζ-only link HEURISTIC);
    local-gauge no-go (`G1_B8_R3.md` Thm L: no Frobenius-local contraction rule reproduces `Θ_η` for `Λ` and its one-prime
    substitutions); Kreĭn rigidity, no type-zero stretch (`G1_B8_R5.md`) — last two *unaudited*.
28. **Function-field transport**: all three limits (`q → 1` undilated/dilated, `g → ∞`) and Bombieri–Stepanov give
    restatements over Spec Z (`G1_B9_R1…R5.md`; Thm 5(iv): admissibility of the transported cone ⟺ RH; `𝔗_ζ ≥ 0` is
    Weil's criterion). Correction of record: R157_002 row 29's Bombieri–Stepanov closing is Landau, not rationality
    (`G1_B9_R2.md`, 5/5).

### 2.4 From phase 159, G2 (the mechanism)

29. **Class-level positivity** (any positivity on a set of tests that holds for a class of combs): `cor:void`; re-confirmed
    by `G2_B1_R5.md` Prop P (holds for the deletion/amplification combs and for `ζ·E`), excluded 5/5.
30. **Twist-covariant derivations**: `G2_B3_R1.md` Thms A, B, C (PROVED; Haar average over the twist group = the
    archimedean form; the sign-flipped comb `Λχ_2` with ζ's Γ and pole has `λ^W_T < 0` for every `T ≥ 0.38`, explicit
    witness `F = t`) [compl]. Also `G2_B7_R1.md` (∀T positivity is Haar-null on the Bohr–Jessen twist torus; Thm C is
    Wintner 1944) and `G2_B8_R1.md` Thm S (Satake-torus void for `T ≥ 0.60`, unaudited).
31. **Fixed, convergent, dilated or scaled certificate rules (SOS)**: `G2_B4_R2.md` Thm R (PROVED 5/5; fixed or convergent
    edge profiles fail for arbitrarily large `T`) [compl]; `G2_B4_R3.md` Thm R′ (dilated profiles; under RH depth `≥ c_ΦT`),
    `G2_B4_R4.md` Thm R′_prim [prim], `G2_B4_R5.md` Thm PT and Thm RN (every *resolving* rule fails at all `T ≥ T*`, both
    forms) — *unaudited*. The free per-window choice is `thm:Zexh`/`cor:RH` (EQUIV).
32. **Bootstrap / renormalisation in `T`**: `G2_B2_R3.md` Thm NB (every scheme "state at `T` ⟹ state at `T+δ`" is false on a
    class, or W15 on the singleton orbit `{Λ}`, or `T`-free) — unaudited but consistent with the audited R2 verdict (the flow
    on `{Λ}` is the identity; Prop Ψ4: every exact invariant is a functional of `ζ(½+it)`).
33. **Any "for all `T`" growth target**: the **graded Weil converse**, proved five/six times (G2_B1_R4 Thm Q, G2_B2_R4
    Thm G1 [cleanest, two-sided], G2_B3_R4, G2_B5_R4, G2_B9_R4, G2_B10_R4 Thm Γ): `λ^A_T ≥ −Ce^{κT}` ⟹
    `Θ ≤ ½ + κ/2`; target `κ = 0` ⟺ RH (von Koch–Landau). PROVED; landing EQUIV. `G2_B10_R5.md` Thm Γ_f (unaudited)
    extends it to any zero set (no `κ ≤ 1`, no Landau, no FE, no Euler product).
34. **Proportion-of-zeros inputs** (Levinson–Conrey, Selberg, Bombieri–Hejhal): `G2_B10_R5.md` Thm H (unaudited):
    Davenport–Heilbronn and Epstein `Z_Q` (`h(−D) > 1`) satisfy the mollifier *output* (positive proportion on the line;
    100 % conditionally for `Z_Q`) yet have `κ > 1`, beyond Chebyshev's `κ^W_ζ ≤ 1`. The Euler product has to enter
    after the counting step. Also `G2_B10_R1.md` Thm N (mollifier closure is the same for every comb in `𝒞_E`),
    `G2_B10_R3.md` Thm M1 (mollification at window `T` with length `N` *is* the plain window `T + ½log N`).
35. **Separated arithmetic + archimedean squares** (Vaughan, Heath-Brown, Selberg, `μ∗log`, `Λ²` sieve squares):
    `G2_B3_R5.md` Thm S / Cor S1 (unaudited): separated decomposition exists iff `c_*(T) ≤ λ^{∞,P}(T)`; excluded for
    `T > 0.74921` although Zhu gives positivity on `(0.74921, 0.8]`. Coupled squares = absolutely continuous KEP solutions
    (`thm:KEP1`), whose existence ∀T is RH (`G2_B3_R3.md` Thm K).
36. **Euler-factor-local (stability, Lee–Yang, Pólya–Schur) certification**: `G2_B8_R5.md` Thm D + Thm L″ (unaudited;
    §3 below): excluded for `T ≥ 0.5925` (upper bound machine-verified, **not interval-certified**); earlier versions Thm L
    (`T ≥ 4.70`, R3) and Thm L′ (`T ≥ 1.50`, R4). Remark B (R3): each local prime symbol is positive definite and `m − C_0`
    is conditionally negative definite, so stability preserves the term that enters with the **minus** sign. Coupling ray,
    phase and conductor deformations all leave the positive set (`G2_B8_R2.md` Thm R, Prop K).
37. **Finite/random zero universes, 100 zeros probes**: premise 2 / `thm:finZ`; `G2_B6_R2.md` Thm M makes the per-window
    margin doubly exponential; `G2_B6_R3.md` Prop D (a zero-universe law needs infinite density and reality = RH);
    `G2_B6_R5.md` Cor F1 (on the rigid side, no ∀T-positive law in `Λ + 𝒯` drops finitely many zeros).
38. **Comb perturbation, continuity, deformation, first-crossing in the comb variable**: `G2_B9_R3.md` Thm R′ (PROVED
    unconditional): for real `b ≠ 0` with `Σ|b_n|n^{−½} < ∞`, `Λ + b ∉ 𝒮^W ∪ 𝒮^A`; Thm N: `𝒮^A ∩ (Λ + 𝒯_meas) = {Λ}` if
    RH, `∅` if not. Positivity has empty interior in every summable direction.
39. **Almost periodicity in `T` or in `τ`**: `G2_B7_R2.md` (hull-type inputs blind to the Γ-matching), `G2_B7_R3.md` Thm T
    (growth rate of the certificate value in `T` is exactly `2(Θ − ½)`; bounded ⟺ Bohr a.p. ⟺ RH) — EQUIV.
40. **de Branges / canonical system in window time**: `thm:KEP3`(b) (G2_B5_R1); the germ problem `H∞` ⟺ RH
    (`G2_B5_R3.md`); first-variation formulas for `dλ/dT` do not exist in usable form (archimedean log-singularity; F2/W15
    shape anyway).
41. **Pointwise bounds on `ζ′/ζ` for the upper half of the growth law**: `G2_B9_R5.md` Cor L1 (unaudited): the best known
    pointwise input ties *exactly* with the trivial exponent `κ_W ≤ 1`, even under RH.
42. **Termwise zero-side majorants**: `G2_B2_R5.md` Thm M (unaudited): `𝒩_T < ∞ ⟺ D₂ < ∞`; no termwise zero-side argument
    reaches the upper half without the Carleson hypothesis (BD₂).

### 2.5 Withdrawn or false statements (must not be cited)

G1_B1_R3 Thm T(iii)/Cor T.1; G1_B2_R2 Thm E(i) as stated; G1_B5_R4 Cor K5(a); G1_B6_R1 Cor 8.1(iii) "simple zeros"
(needs cyclicity); G1_B6_R3 Thm C(iv) for `a < ½` (unproved); G2_B9_R3 Remark 3.4 (relabel OPEN); G2_B5_R4 "sharper rate
than P5" (withdrawn in G2_B5_R5 §3); G2_B2_R2 Cor Ψ3′ (downgraded to HEURISTIC); R157_002's "exactly one survivor", O3's
"≍"/"`e^{−14T}`" form, O4's "determinate", Lemma P157.S1 clause (b) as stated; R157_002 row 38's sentence "its proof of ⇐ is
a partial-sum bound (W4)" (UNVERIFIED, struck); R158_001 C21 original wording (contradicts `thm:D1`); R158_002 Lemma D
uniqueness clause, Fact 4.6a.7 as stated, "OT-5′ is the only failure" (struck, A1); R150_001 (DMV-a) misquotation.

### 2.6 The walls, indexed by the phase-160 memo angles (so each memo knows what to answer in its §0)

| memo (R160_000) | walls in my scope that the angle must be shown to avoid |
|---|---|
| B1 Connes (prolate, Sonin, semilocal) | R157_002 rows 18, 34, 60; `prop:archneg`, `cor:Tarch` (archimedean positivity on `P_T` ends in `[0.58, 0.60]`); `thm:SC`, `prop:finsupp`; G2_B8_R5 (local certification fails from ≈0.59, unaudited); R158_002 (Connes' global trace formula ⟺ RH; OT-2) |
| B2 Consani (RR over 𝕊, ζ-cycles) | P47 Thm 19.25, Cor 19.25b (any `h⁰` on `D^W`, `𝒟_c`, `𝒟_p`); R157_002 rows 1, 2, 35; G1_B1_R1 Thm C (bounded-density classes = Radon measures), Thm E (sum-graph axiom = RH); C25 ((P145′)(4a)–(4c) is RH-strength) |
| B3 Jaffe (OS reflection positivity) | NG-E5 (OS reconstruction retracted; R157_002 row 32); Lemma T; G1_B10_R3–R5 (covariance/Bochner = Weil; Koopman power law; phase–power law) |
| B4 Haagerup/Popa (natural cone, entangled state) | G1_B10_R5 Thm P, Cors Z, E, Thm F′ (standard form, natural cone `P^♮`); G1_B2_R5 Thms R, U (III₁ core flow carries no arithmetic); G1_B6_R4/R5 (canonical functionals: installation); Lemma U / `S₃` falsifier (unitarity routes) |
| B5 Scholze (analytic stacks) | G1_B3_R3 Thm W (integer-weight wall), Thm F (FF product Euler-factorizable); G1_B3_R2 Thm I (compactness) |
| B6 Bost (θ-invariants) | R157_002 row 2 (D-θ killed verbatim by Thm 19.25); G1_B4_R1/R2 (integrality vs flow, Thm A) |
| B7 S.-W. Zhang (heights, CM towers) | G1_B4_R1 (heights ≠ zeros; finite-rank positive spaces; Lemma 4.4), G1_B4_R2 Example E (infinite-rank CM conformal family is zero-blind), G1_B4_R5 Thm R/R′ (rationality wall) |
| B17 Lichtenbaum/Morin (Weil-étale) | G1_B3_R2 Prop WA and G1_B3_R3 Cor W2 (Weil–Arakelov cohomology sees ζ only at integers) |
| B18 Morishita/Mazur (arithmetic topology) | C7 (Morishita bridge kills the transverse `p`-adic direction; NG-107); R158_001 §4 Morishita row (OT-5′: no form) |
| B19 Huh (Lorentzian / combinatorial Hodge) | R158_001 §4 tropical row (positive self-intersection is a hypothesis; not attached to ζ); G1_B1_R1 Thm A, G1_B1_R2 Thm H′, Prop M (idempotent / hyperring `+` loses the cross term) |
| B8 Deligne/Katz (tensor power, towers) | P47 T5 (Thm 27.3), T6; R157_002 rows 22, 47; C26; T1 read correctly (field-uniform is admissible, must prove GRH ∀K) |
| B9 Sarnak (Lax–Phillips) | R157_002 rows 25, 58 (`β = ¼` *is* RH, R152 Prop A.2); O2 below RH strength |
| B10 Iwaniec (Maass–Selberg) | R157_002 row 46 (Maass–Selberg reaches only the absolute-convergence region, R152 Prop A.1); G2_B10 (mollifier = window widening; Thm H) |
| B11 Tao (dBN heat flow) | R157_002 row 41 (P13 N5: the flow is arithmetic-blind); graded converse (target EQUIV); Thm M |
| B12 Tao (Schur/Hadamard, multiplicative) | G2_B8_R3 Remark B (Bochner sign is the wrong sign), G2_B8_R5 Thm D (archimedean enters only through `∫K max_p ε`); G2_B3_R3 Cor S1 (quadratic prime side is not PSD) |
| B13 Maynard (large sieve, MV) | `cor:void` (`C_BT`), O3, R157_002 rows 20, 30; G2_B3_R5 (separated squares) |
| B14 Ono (Jensen polynomials) | R157_002 row 40 (P15 `thm:hr`: no uniform gap; finite order quasi-RH by O2) |
| B15 Green (ultralimits at `T = ∞`) | `thm:margin`, Thm M (the limit form is degenerate: `λ → 0`), `cor:margin2`(iii); G2_B9_R2 Thm R / R3 Thm R′ (rigidity at `T = ∞`) |
| B16 Villani (entropy/transport) | P46 `thm:A`/`thm:S` (the form is already a Lévy energy: `C_0‖F‖² + Lev(c_F) − Σ v_n c_F(log n)`); G2_B8_R4 Prop M |
| B20 Connes (semilocal → global) | `thm:SC`, `prop:finsupp`, R157_002 row 18, G2_B8_R5; NG-E1 strong form (P47 Prop 28.4 / P46 `cor:Qp`) |

---

## §3 What still STANDS

### 3.1 Proved results of record in scope (audited)

| result | statement (short) | label | form | file |
|---|---|---|---|---|
| O1 | uniformity in `T` = Weil positivity on `C_c^∞(R)` | RESTATEMENT (PASS) | both | R157_002 §1.2; R157_004 §1.3 |
| O3 = `rem:resweights` | one-weight change of `Λ(n₀)` by `≤ √n₀λ^A_T/(2|c_{F*}(log n₀)|) ≤ 2·10⁹Te^{−14.449T}/|c_{F*}(log n₀)|` flips `RD_T`; vacuous for `T ≤ 1.51`; needs `c_{F*}(log n₀) ≠ 0` | PROVED (upper bound; non-degeneracy OPEN) | [prim]; [compl] with the `W_T`-minimiser | R157_004 §1.1 |
| Lemma D = `lem:degen` | if some minimiser has `c_{F*} ≡ 0` on `log N_T`, then `v_T(Λ)` maximises `v ↦ λ_min(A^{(v)}_T|P_T)` over `R^{N_T}` | PROVED | [prim] | R157_004 §1.1 |
| Lemma C | `T ↦ λ^W_T` continuous on `(0,∞)` (also Bombieri 2000 Thm 5) | PROVED | [compl] | R157_004 §1.2 |
| Lemma E | `λ^W_T ≥ C₀ + log coth(T/2) − 4 sinh T > 0` for `T ≤ 0.005` | PROVED | [compl] | R157_004 §1.2 |
| O4 | RH ⟺ `λ^W_T ≠ 0 ∀T`; if RH fails `{T : λ^W_T = 0}` is a nonempty compact interval | PROVED as equivalence; RESTATEMENT of Bombieri Thms 1, 3, 5 + P45 Thm 10.4 | [compl] | R157_004 §1.2, §5(ii) |
| row 18 infinite-support finite-`S` | `limsup λ ≤ C₀ − A_S < 0` for infinite-support finite-mass sub-combs | PROVED | [prim] | R157_004 A11 |
| (H-DMV′) | DMV/Zhang systems | CITED (secondary source) | — | R157_001 §3; R157_003 |
| T3 | P47 Rem 27.16 | METHOD-CONSTRAINT modulo (H-DMV′); stays a Remark | — | R157_007 §1 |
| NG-E1 strong form | `Q_p(F_φ) = −v_p‖φ‖²`; each local form is negative definite on an infinite-dimensional subspace of `P_T` for `T > ½log p` | PROVED | [prim] | R157_006 (Lemma 3.3); P47 Prop 28.4; P46 `cor:Qp` |
| R157_005 Lemma 2.1, Thm 4.1 (in 𝔄⁺) | Berkovich group law relative to `M(Z)`; every energy in 𝔄⁺ reproducing `W` is a restatement | PROVED within 𝔄⁺ (exhaustion CITED/HEURISTIC) | both | R157_005, R157_006 |
| Lemma T, Cor T′ | (D1)–(D3) satisfiable ⟺ RH; under them `W_T(F) = ‖F(U)|_{H¹}‖²_{HS}` | PROVED, CLASSICAL | [compl]; [prim] by restriction | R158_001 §3.1 |
| C1–C27, OT-1…OT-12 | constraints and object test, each tagged (Rem 3.0) | ANALYSIS (audited) | stated per item | R158_001 §2–§3 |
| R158_002 Lemma A (on `C_Q`), E-i, E-ii, Prop H, Lemma U, Prop B | see §2.2 item 10 | PROVED (U, E: CLASSICAL content; H new) | [compl] (B: E1 test by test) | R158_002 §4–§5; R158_004 |
| CCM trace form = `W_T` under `F(t) = e^{t/2}g(e^t)` | matching | PROVED | [compl] | R158_005 §1 |
| Thm W♯, Prop Σ | sharp tail wall | PROVED (PNT CITED), 5/5 | object-level | G1_B4_R4 |
| Thm R/R′ | rationality wall | PROVED mod CITED six exponentials | object-level | G1_B4_R5 |
| Thm A, Thm B (resolution law) | P-HS false on Construction 9; super-critical topology necessary (N-e) | PROVED unconditional (5/5) | object-level ([compl]/P-HS) | G1_B6_R2 |
| Cor D1 | modulation-invariant carriers have `sup_s‖U_s|H¹‖ = ∞` | PROVED only with P3's repair + CITED Selberg density | object-level | G1_B6_R3 |
| Witt–Kronecker, Thm K, Thm E | covariant flows | PROVED (K5(a) false; Thm G constant `1 − 2^{−β}`) | object-level | G1_B5_R3/R4/R5 |
| Cor H, Cor M1, Thm R, Prop NH, Thm U | DK / III₁ laws | PROVED (Connes–Takesaki, Connes–Haagerup CITED) | object-level | G1_B2_R3/R4/R5 |
| Thm F, Thm E | flat wall, `χ_Co = 0` | PROVED under (FT), (IBP), (R), (D) | object-level | G1_B3_R5 |
| O1–O4 | Weil-number law at closed orbits | PROVED under (C), (Def), (Sm)/(Orb) + E-P5.19 | object-level | G1_B1_R5 |
| Echo Lemma E, Thm K | Frobenius-local chains excluded on `(½log3, log 2)` | PROVED mod CITED Romanov | object-level | G1_B8_R4 |
| Thm G (function field), Thm H | O-37 closed over `F_q`; Thm H = Weil over Spec Z | PROVED (function field) | — | G1_B9_R5 |
| **Thm M, Cor M1–M2** | `λ^W_T ≤ λ^P_T ≤ λ^A_T ≤ exp(−e^{(2−ε)T})` for `T ≥ T₀(ε)`; explicit bound at every `T`; beats `thm:margin` from `T ≈ 6`; not in Zhu 2608.24827 | PROVED unconditional (4 panelists); analysis classical (plunge), application new (G2_B6_R3 §5) | both | G2_B6_R2 |
| graded converse | `λ_T ≥ −Ce^{κT}` ⟹ `Θ ≤ ½ + O(κ)`, sharp | PROVED; target EQUIV | both | G2_B2_R4 Thm G1 (cleanest), G2_B1_R4, G2_B3_R4, G2_B5_R4, G2_B9_R4 |
| Thm U | `κ^A = κ^W = Θ − ½` (normalisation `(2T)^{−1}`) | PROVED **conditional on OPEN (BD)** | both | G2_B2_R4 |
| Thms A, B | twist Haar average = archimedean form; `λ^W_T(χ_2) < 0` for `T ≥ 0.38` | PROVED (one interval evaluation) | [compl] | G2_B3_R1 |
| Thm R | fixed/convergent edge-profile certificates fail for arbitrarily large `T` | PROVED unconditional | [compl] | G2_B4_R2 |
| Thm R′, Thm N, Lemma L | unconditional rigidity in `Λ + ℓ¹_w`; `u_Λ` tempered ⟺ RH | PROVED | both | G2_B9_R3 |
| Thm R | under RH `Λ` is the only ∀T-positive comb in `Λ + ℓ¹_w` | PROVED under RH | both | G2_B9_R2 |
| Thm P, Cor P2 | uniqueness of the explicit formula among combs on `±log N` (BRS dual) | PROVED mod Lemma S (closed in G2_B6_R5, unaudited) | [compl] | G2_B6_R4 |
| Thm P | one-generator rigidity on the fibre over Λ | PROVED (Li–Radziwiłł CITED, primary read) | [compl] | G2_B7_R4 |
| row-29 correction | Bombieri–Stepanov closing is Landau | PROVED/CITED 5/5 | — | G1_B9_R2 |

### 3.2 Preliminary assessment of the UNAUDITED items of R159_099 §2.4 (and of other unaudited memos in scope)

Every entry below is a memo self-label; the right column is **[S5 assessment]**, unaudited, based on reading the
statement and (where marked) the proof.

| item | memo label | [S5 assessment] |
|---|---|---|
| **G2_B8_R5 Thm D** (local certification ⟺ `Φ_T ≥ 0`; `Φ_T = inf [C_0 + ∫K max_p ε_{σ_p} + Σ_p tr(σ_pQ_p)]`) | PROVED [prim] | Proof read (§2 of the memo). Sion's theorem is applied with `X = {θ_p ≥ 0, Σθ_p = 1}` weak-* compact in `(L^∞)^{Π_T}` and `σ` in a convex set of finite-rank density operators with the finest locally convex topology; `f` is affine and continuous in each variable; attainment by weak-* usc of `g`. **Looks correct.** Two checks for the auditor: (a) `D_T = P_T ∩ H¹_0` must be a form core of `𝔞_T|P_T` (true: `H¹_0 ∩ P_T` is dense in the log-Sobolev form domain, but it should be written); (b) the LK-splitting ↔ stability-class reduction uses Schoenberg + Lévy–Khintchine uniqueness with `thm:S`(ii) (no Gaussian part), CITED, fine. A genuine strengthening of `cor:Qp` and `thm:SC` (full budget) to every stability-type distribution of the archimedean budget |
| **G2_B8_R5 Thm L″** (`½log3 ≤ T_loc ≤ 0.5925`) | "PROVED (machine-verified, not interval-certified)" | **Must be recorded as uncertified numerics** (rule (a)). The lower bound is PROVED from Paper 42 (certified). The upper bound rests on a double-precision grid (8000 cells, stated fp allowance `10⁻⁹`, margin `1.66·10⁻³`, stable under refinement) — an interval re-run of the finite list of closed-form autocorrelations would certify it cheaply. Until then: "`T_loc ≤ 0.5925`, uncertified; `T_loc ≤ 1.50` modulo the closed-form 30-digit check of R4 Thm L′ (also not interval arithmetic)". Cor 4.2 ("positivity on `[0.5925, log 2]` is necessarily cross-prime") inherits the uncertified status. Open P159.B8.5 (`T_loc < T*_{∞,P}`?) stands |
| G2_B8_R1 Thm S (Satake-torus void), Lemma H | PROVED | A `cor:void`-type statement for a rotated-phase class that keeps `|α_p| = 1`; rests on `cor:Tarch` (certified). Plausible; signed weights are allowed by `prop:finite`(iii) |
| G2_B8_R2 Thm R (coupling ray), Cor R′ (`ζ^k`), Prop K (conductor) | PROVED | Thm R follows from concavity of `V_T` (`lem:degen`) plus `V_T(0) < 0` for `T ≥ 0.60`: **correct**. Caution on Cor R′: the failing form is the *ζ-normalised* test (one `Γ_R`, comb `kΛ`), not `ζ^k`'s own Weil form (which is `k·W_T`). So it is C11 (`thm:finmod`(iii): the archimedean term must be matched), not a new falsifier of derivations that use `ζ^k`'s own FE |
| G2_B8_R3 Thm L, Remark B, Thm NM; G2_B8_R4 Thm L′, Prop M | PROVED | Remark B is elementary and correct (P46 `thm:S`). Thm L (29-term sum) and L′ (closed forms at 18 points + 8-term sum, 30 digits) are finite numerical checks, **not interval-certified**; superseded by R5 anyway |
| **G2_B10_R5 Thm Γ_f** (any `f` of order 1, zeros in a strip, `N_f ≪ T log T`: `λ^f_T ≥ −Ce^{κT}` ⟹ `|Re ρ − ½| ≤ κ/2`) | PROVED, both forms | Sound in outline: tests `F ± τ_uF` live in the window `T + u/2`, so the hypothesis bounds the shift function `β_F(u) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)cosh((ρ−½)u)` two-sidedly by `C′e^{κu/2}`; absolute convergence of the zero sum and meromorphy of its Laplace transform then kill every term with `|Re ρ − ½| > κ/2` for generic `F`. Note the definition `W^f` is the **zero side**, so for ζ it is `eq:W` only through the explicit formula |
| **G2_B10_R5 Thm H** (DH and Epstein defeat "proportion ⟹ sign") | PROVED from CITED | Logic correct given the inputs, but the inputs are weak-cited: Selberg's DH positive proportion via a **secondary** source (Dousselin 2311.10285), Rezvyakova 2411.18492 **abstract only**, Bombieri–Hejhal conditional. The memo flags this itself (§ "CITED inputs"). Label should be "PROVED modulo CITED (secondary / abstract-level)" |
| G2_B10_R5 Prop J (Levinson–Jensen in `H²` form) | PROVED | Jensen's inequality on `dμ = dt/(2π(¼+t²))`; standard; converse OPEN |
| G2_B10_R1 Thm N; R2 Thm H (harmonic rigidity), Thm N±; R3 Thm M1, Prop M2, Thm M3, Thm B; R4 Thms Γ, Q, L(θ), R_s, Prop S | PROVED | Thm N: `exp(D)`, `D ∈ A_½`, is invertible in `H^∞`, so invariant-subspace closures coincide — correct. Thm H: a linear zero functional `Σ_ρ H(ρ−½)` has, as a function of the position, a kernel that is (the real part of) a holomorphic function, even under the symmetry `ρ ↦ 1 − ρ̄`; an even harmonic function vanishing on the line vanishes identically — correct. Thm M1 (translates by `log n`, `n ≤ N`, of `C_c^∞(I_T)` span `C_c^∞` of an interval of length `2T + log N`): correct (consecutive steps `log((n+1)/n) < 2T`). Thm Q (`B_∞(T₀)` ⟺ RH with two-term mollifiers `1 + n^{½−s}`): the discretisation of the shift variable to `u = log n` needs an explicit argument (sign changes of the dominant almost-periodic part along `log n`); **check this step**. Prop S (`E_A = E_sub ∧ Γ`) is a correct factorisation; EQUIV as a target |
| G2_B2_R5 Lemma L, Thm I, Thm U₂, Thm M | PROVED (U₂ under (BD₂)) | Lemma L is Weil's formula regrouped by quadruples (signature `(2,2)` per off-line quadruple): correct. Thm I is Bombieri 2000's index theorem in window form, **conditional on finitely many off-line zeros**, CITED; the independent proof is plausible. Thm M (`𝒩_T < ∞ ⟺ D₂ < ∞`) is a Carleson-measure equivalence: plausible |
| G2_B3_R5 Lemma A, Thm S, Cor S1, Cor S2 | PROVED | Criterion `c_*(T) ≤ λ^{∞,P}(T)` follows directly from Lemma A (the two blocks exchange one scalar). **Cor S1's threshold is conservative:** since `λ^{∞,P}(T) ≥ 0` is necessary, P46 `cor:Tarch` (certified, `T*_{∞,P} ≤ 0.60`) already excludes separated squares for `T ≥ 0.60` [prim], and `prop:archneg` for `T > 0.4608` [compl]; the memo cites only the `T_0(0) = 0.74921` bound and calls the lower thresholds DIAGNOSTIC. The auditor should restate Cor S1 with the certified thresholds |
| G2_B4_R3 Thm R′, Cor R′2, Prop Q1; R4 Lemmas E1–E3, Thm R′_prim, Cor R′+; R5 Thm PT, Cor RC, Thm RN, Cors E1, E2, D, N | PROVED (RC, N under RH) | Thm PT is claimed with "no input on ζ"; Thm RN is unconditional by a case split (RH branch via RC, ¬RH branch via Weil + `lem:monoT`) but `T*` is non-effective. Plausible; the scale-free branch is `cor:RH` (EQUIV). Open: `C^∞`-flat joins with `a_T/T` unbounded; Q-R(1) (compact families) |
| **G2_B5_R5 Thm Q♯** (Θ attained ⟹ `−λ^A_T ≥ ce^{2(Θ−½)T}` for **every** `T ≥ T₁`) | PROVED, both forms | Proof read (§2). Two-bump test `g(·∓y/2)`, zero-side expansion `V(y) = Σ a_ρ e^{(ρ−½)y}`; the top-modulus part is a nonzero real **mean-zero** Bohr a.p. function (mean zero because no zero on `Re s = Θ` is real: ζ has no real zeros in `(0,1)`), hence negative on a relatively dense set; choosing `y` in that set within bounded distance of `2T` gives every large `T`. The remainder is `o(e^{β*y})` by dominated convergence. **Looks correct.** Non-attained case OPEN |
| G2_B5_R3 Lemma G (inverse rigidity), problem `H∞` ⟺ RH | PROVED | Plausible (Kreĭn inverse problem, segment-by-segment bijection) |
| G2_B6_R5 Lemma S closed, **Thm X** (Λ extreme point of the ∀T-positive fibre), Prop C, Thm F, Cors F1, F2 | PROVED | Thm X's proof read: ∀T positivity of `Λ ± b` ⟹ RH (robust converse (N)), then `D_b` atomic on `Z_on`, then Theorem P ⟹ `b = 0`. **Correct given Thm P**, whose Lemma S is now closed by reading BRS §4.2–4.3 (to be audited against arXiv 2005.02996v3). Cor F2 uses Beurling–Malliavin (CITED) |
| G2_B7_R5 Lemma C, **Thm M** (`|b_n| ≤ 2d⁺(b)√n`), Cors M0, M1, Prop S′ | PROVED unconditional | Lemma C is exact arithmetic: the Cesàro mean of `e^{ijω_m log n}`, `ω_m = 2π/log m`, is 1 iff `log n/log m ∈ Z` — **correct**. Thm M plausible. Prime-side only (the point on which P2 excluded R4). Rigidity, not a mechanism; the positive-density multi-generator case is OPEN |
| G2_B9_R5 Thm S (shifted-contour resummation), Thm L, Cor L1 | S PROVED; L conditional | Thm S is the standard contour shift in P46's normalisation (residue at `s = 1` = polar term). Cor L1 uses the Littlewood three-circle bound (CITED, Titchmarsh §14.2 adapted). Plausible |
| G2_B1_R3 Thm G, Prop Z, Prop E; G2_B2_R3 Thm NB, Lemma H; G2_B3_R3 Thm K, Thm S, Cor S1; G2_B6_R3 Prop D, Lemma E, Prop T′, Cor M4; G2_B7_R3 Thms L, T | PROVED / EQUIV | All are closures or restatements; Thm K is immediate (`∪_T P_T` = all compactly supported primitive tests). G2_B6_R3 flags a **web hit "Certified Weil positivity beyond the unit window" (alphaxiv 2609.\*) not read** — a possible update to premise 1 (`T ≤ 0.8` [compl]); someone must read it before any endpoint is stated |
| G1_B7_R4 Thms A, B, Props G, L; G1_B7_R5 Thms A″, Γ₀, Γ, Prop Σ_ζ, Cor M′ | PROVED | Thm B checked: on `2^Z`, positivity of `cδ_0 − log 2 Σ_{k≠0}2^{−|k|/2}δ_{2^k}` at `θ = 0` needs `c ≥ 2 log 2·(1/√2)/(1 − 1/√2) = 2(√2+1)log 2` — correct; it is the `S = {2}` mass of `thm:SC`'s remark (`2log2/(√2−1) ≈ 3.35`). Genus law plausible; its weakest step is hypothesis (H_M) (completions that are functions away from the identity) |
| G1_B10_R4 Thm K, Thm S; G1_B10_R5 Thm P, Cors Z, E, Thm F′ | PROVED | Thm K checked: if `U_tf = e^{iλt}f`, then `|f|` is invariant and `f^n|f|^{1−n}` is an `L²` eigenfunction for `nλ` — correct on any σ-finite space; the exclusion needs Li–Radziwiłł (non-vanishing on vertical progressions, CITED). Thm P is the standard-form generalisation. Residual: higher bounded-field sectors (`k ≥ 2`) OPEN |
| G1_B1_R1/R2, G1_B3_R2/R3, G1_B4_R1/R2, G1_B5_R1/R2, G1_B7_R2, G1_B8_R3/R5, G1_B9_R3, G1_B10_R3 | PROVED (self) | See §2.3 items 21–28; the elementary ones (B1 Thm A, B3 Thm W, B4 R2 Thm A, B7 R2 Thm B via Baker) check at statement level. G1_B3_R2 Prop WA is **conditional on Flach–Morin conjectures** (CITED) |
| **R158_006** Theorem J_K, Prop S, Cor F (`S₃` falsifier) | PROVED (modulo Duke 2005 lemmas) | Post-closing, not audited, not in the phase README. Plausible; the scope caveat (does not apply to Connes' `L²_δ`, `1 < δ ≤ 3`) is correct. If audited, N-b rests on a PROVED falsifier |

### 3.3 Open leads never closed negatively (in scope)

| lead | status | where |
|---|---|---|
| MW-5 cluster (Deninger foliated cohomology; CC Hodge index on the scaling-site square not routed through `h⁰`; arithmetic surface over `F₁`) | NOT EXCLUDED, unbuilt; content = OT-5′ with N-a, N-b, N-c; RH-strength | R157_004 M6; R158_005 §2 |
| O3 degenerate case (`c_{F*} ≡ 0` on `log N_T` ⟹ `Λ` is the optimal comb for `λ_min` at that window) | OPEN; nothing excludes it, nothing makes it plausible | R157_004 Lemma D |
| O4 at a crossing: solvability and uniqueness of KEP(`T_c`) | OPEN | R157_004 A6 |
| identity-level use of `Λ = μ∗log` (#30/#55) and an entropy-weighted `×p` construction (#27) | regions not excluded by any proved statement; no object, no statement | R157_002 §5 last paragraph |
| energies outside 𝔄⁺ on `A^{1,an}_Z` (a kernel neither a base kernel nor a function of finitely many global points) | no canonical one exists (R157_005 Lemma 2.2 as amended); Chinburg–Rumely unread | R157_006 §2 |
| density of `H¹_alg` in Meyer's `H¹` | OPEN, "possibly RH-adjacent" | R158_004 row 11 |
| R158_002 follow-ups O1 (function-field Jordan block), O2 (Lemma E on `H¹_red`) | OPEN, maintenance | R158_002 §5 |
| upper half of the growth law without (BD)/(BD₂) | OPEN; termwise zero-side arguments cannot reach it (G2_B2_R5 Thm M); pointwise `ζ′/ζ` bounds tie with the trivial exponent (G2_B9_R5 Cor L1) | G2_B2_R4/R5; G2_B9_R5 |
| Q♯ in the non-attained case; the sequential converse there | OPEN | G2_B5_R5 |
| `𝒞 ≠ {0}`? (RH-free pointed cone of rigid perturbations) | OPEN | G2_B6_R5 Prop C |
| multi-generator rigidity in the positive-density case | OPEN | G2_B7_R5 Cor M1 |
| `T_loc < T*_{∞,P}`? (P159.B8.5) | OPEN | G2_B8_R5 §4 |
| Q-R(1) compact families of profiles; `C^∞`-flat joins with `a_T/T` unbounded | OPEN (threshold questions about an EQUIV problem) | G2_B4_R3, R5 |
| non-ergodic DK_α residual | OPEN, no candidate | G1_B1_R5 |
| non-quasi-free fermionic higher sectors (`k ≥ 2`) of bounded-field systems | OPEN, no candidate | G1_B10_R5 |
| completions outside (H_M) in the genus law | OPEN | G1_B7_R5 §6 |
| O-B5.1′: an archimedean correction on Borger's square using the geometry of `W(R)` beyond `log n` | named, not built (Borger's own caveat) | G1_B5_R2 §6 |
| Levinson–Jensen converse (`inf_M R(M) = 1` ⟸ RH?) in the discrete-dilation form | OPEN | G2_B10_R5 Prop J |
| web hit "Certified Weil positivity beyond the unit window" | unread; could move the [compl] endpoint | G2_B6_R3 §0 |

---

## §4 State of rows A, B, C and of row D (as far as my scope informs it)

**Rows A, B, C.** Phases 157–159 do not reopen or re-audit rows A–C. They are used as premises only: R160_000 premise 1
("WEIL-STRENGTH-COMPLETE on the declared carrier; not a proof of RH"), and G1_B4_R1 §2 notes that for ζ the fixed-point
count and the extraction (FH-4, FH-5) "are rows A–C and the reduced statement E1–E5"; what is missing is the group law,
the integral lower bound and a conformal Frobenius (FH-1–FH-3). The one scope item touching row C's material is
R157_005/R157_006's re-audit of phase-114 D.195 (3.5) as ≡ `RD_T` (with two convention fixes: sign `B_P = A_P I − 𝓔_P` is
minus the Weil form; window statement only after compression to `L²(I_T)`). No label of rows A–C changed in scope.

**Row D.** No label; closed in the map with the reopening rule P47 §28.4 (six clauses). Phases 157–159 changed nothing in
the sign table (`ROW-D-REDUCED-STATEMENT.md` §3):

| form | windows proved for ζ | source |
|---|---|---|
| [prim] | `T ≤ log 2` | Paper 42 (certified) |
| [prim] | `T = ½log3`: `λ_min ≥ 8.8577·10⁻⁵` | P46 `thm:C` |
| [compl] | `T ≤ ½log 2` | Yoshida 1992, Bombieri 2000 |
| [compl] (hence [prim]) | `(½log 2, 0.8]` | Zhu 2026 Thm 1.2, CITED, not re-verified |
| either | `T > 0.8` | **nothing** |

What the scope added to the picture of row D:
* **Upper bounds on the margin**: `thm:margin` (`≤ 4·10⁹Te^{−15.449T}`) is superseded for `T ≳ 6` by Thm M,
  `λ^A_T ≤ exp(−e^{(2−ε)T})` (G2_B6_R2, PROVED unconditional). Per-window decidability (`prop:finite`) is, at large `T`, a
  statement about precision `exp(−e^{2T})`.
* **Lower bounds on the negativity if RH fails**: graded converse (`−λ_T ≥ ce^{2(Θ−½)T}` along a sequence; PROVED),
  every-large-`T` version when `Θ` is attained (G2_B5_R5 Thm Q♯, unaudited), two-sided law under (BD) (G2_B2_R4 Thm U).
* **Where the proved positivity lives**: on `(0.5925, log 2]` [prim] it is necessarily cross-prime — no Euler-factor-local
  certificate exists (G2_B8_R5, upper threshold uncertified); separated squares fail from `0.60` [prim] / `0.4608` [compl]
  (G2_B3_R5 with P46's certified thresholds, my restatement).
* **Rigidity**: the ∀T-positive fibre over Λ is `{Λ}` or `∅` in every summable direction (G2_B9_R3 Thm R′, Thm N); Λ is an
  extreme point (G2_B6_R5 Thm X, unaudited).
* **The object side**: the whole content of MW-5 is OT-5′ (R158_005); an OT-5′ object would have to be infinitely entangled
  across primes, non-algebraic and non-covariant (R159_099 §1.2, HEURISTIC but supported by all walls).

---

## §5 Ideas started but not finished, or closed for a reason later removed (possible ingredients)

Each item says what exists, why it stopped, and what would be new. None carries a sign.

1. **Row 37 / MW-5 was closed in R157_002 by a misreading of T1, then reopened** (R157_004 A9). The corrected reading
   (P47 Rem 18.1a) *admits* field-uniform programmes. Deninger-type and Connes–Consani square programmes are therefore
   admissible in principle, held to "GRH for all K". What remains against them is not T1 but Lemma T (a postulated form is
   RH), OT-2 (Connes' global trace formula ⟺ RH), N-b (the `S₃` falsifier kills *unitary* routes over non-abelian fields;
   the semidefinite P-HI/Rosati route tolerates Jordan tails, R158_002 §5 A24).
2. **Derived positivity exists, but in the wrong class**: Deninger–Singhof's Kähler–Riemann polarization (math/0204111) is
   derived from geometry with no ζ input, and fails only because compact manifolds force `α = 0` and no fixed points (C5,
   N11). A laminated/solenoidal carrier with fixed points on which the Álvarez López–Kordyukov Hodge theory still gives a
   polarization is the precise missing piece (R158_001 §4). G1 walls 13–20 constrain it: it must not be tail-factorizable,
   ergodic-conformal, finite-trace-conformal, or have `(W_μ, τ_μ, θ)` carry the arithmetic.
3. **Borger's Witt square gives two things nobody else produced** (G1_B5_R1, unaudited): (i) a *derived* conformal form —
   `F_n^† = V_n` fixes the form uniquely and makes it conformal with factor `n`, so (D3) with `α = 1` is derived, not
   postulated (half of N-a); (ii) the exact von Mangoldt weights as intersection numbers, `Γ_1·Γ_n = Λ(n)`, with a
   non-translation-invariant, `p`-adic-depth pairing the frame lacks. It stopped because the form lives on the wrong space
   (Thm C: dense range of `E^♭`, cokernel 0; Thm D) and the ghost-cycle form is not flow-compatible (R2 Props H, K). R2's
   Thm G additionally excluded it "by T3"; after R157_004 A19 T3 needs a bridge `𝓔_𝒫 ⪰ 0 ⟹ (ZFS_δ)`, so **that** reason is
   weaker than stated — the exclusion stands on Props H, K. Residual O-B5.1′ (archimedean correction via `W(R)`) is unbuilt.
4. **Example E** (G1_B4_R2, unaudited): on `K_∞ = Q(√−p : p prime)` the trace form is positive definite and `√−p` is
   conformal with factor `p` **for every `p`** — an infinite-rank conformal Frobenius family exists. It is zero-blind (Haar
   measure on `{χ(p) = ±i}`; Lefschetz series `ζ(4s−2)/ζ(2s−1)`), failing OT-2/OT-4. It shows conformality at all primes
   is not the obstruction; the coupling to ζ's explicit formula is.
5. **Minimal genus and the genus law** (G1_B7_R4/R5, unaudited): a finite-genus positive trace carrying the prime atoms
   exists (Künneth, `c_* = 3.3468…`) but is local and zero-blind; any completion in (H_M) needs `d(ε) ≥ log(1/ε) − …`, and
   ζ's archimedean term saturates this with constant 1. So the archimedean place is *extremal* for positivity given the
   prime side. An argument that uses this extremality together with a coupling (not a Künneth product) is not on record.
6. **Cross-prime interference** (G2_B8_R5 §5, unaudited): on the test that makes the 2-factor most negative, `c_F(log 3) < 0`,
   so the prime 3 *pays*; the proved [prim] positivity on `(0.5925, log 2]` is carried by sign interference between primes
   inside one autocorrelation, and by Theorem D the archimedean place couples the Euler factors only through the sublinear
   functional `∫K max_p ε_{σ_p}`. A mechanism would be a *joint* constraint on `(c_F(log p))_p` — the zero side of
   `thm:Z` (EQUIV) unless a new identity appears. This is the most precise statement in scope of *where* the positivity is.
7. **O3's degenerate case / `lem:degen`** (R157_004): if at some window every minimiser has `c_{F*} ≡ 0` on `log N_T`, then
   `v_T(Λ)` is a **global maximiser** of the concave function `V_T` on `R^{N_T}`. Together with G2_B6_R5 Thm X (Λ extreme
   in the ∀T-positive fibre) and G2_B9_R3 Thm N (the fibre is `{Λ}` under RH), this suggests a variational
   characterisation of Λ among combs. No one has examined whether `V_T(v_T(Λ)) = max V_T` can hold, or what it would mean.
8. **Single-window reformulations** that move the infinite quantifier elsewhere: G2_B10_R4 Thm Q (RH ⟺ all two-term
   mollified tests at **one** window `T₀` are Weil-nonnegative), Thm L(θ) (100 % is forced by coefficient size `√n`, not by
   length or proportion). Closed as EQUIV because by Thm M1 mollification of length `N` is the window `T₀ + ½log N`; the
   quantifier over `T` becomes a quantifier over `n`. Recorded so that no memo resubmits it as progress.
9. **The Satake/conductor/coupling deformations** (G2_B8_R2): the only input that fixes degree, conductor and phase at once
   is "the L-function is ζ" (Kaczorowski–Perelli), used through the explicit formula. Any new route must name its
   load-bearing use of *all three* scalars; this is a sharper form of T2 + C11.
10. **The coupled square** (G2_B3_R5 Cor S2): a surviving square must have operators `h_j(D)∘D_j` with non-constant
    archimedean multipliers — exactly the absolutely continuous KEP solutions. "No convolution identity supplies the
    coupling, because a convolution identity lives in the group ring of `Q_{>0}` and the coupling lives in `L¹_loc(R)`."
    A structure that lives in both at once (e.g. a Hecke-type algebra acting on `L²(R)` with archimedean multipliers) is the
    shape of a candidate; none is on record.
11. **(P152.2) closed as restatement *within 𝔄⁺***: the exhaustion of the literature is CITED/HEURISTIC (Chinburg–Rumely
    unread). An energy on `A^{1,an}_Z` coupling fibres through something other than the base `M(Z)` and finitely many global
    sections would escape Theorem 4.1; R157_005 Lemma 2.2 (amended) says no canonical one exists.
12. **Super-critical topology (N-e)** (G1_B6_R2 Thm B): a P-HS carrier must resolve the zeros at their own spacing, a
    density fixed by the Γ-factor, so it can be supplied without the zeros but must be built in. This is a positive design
    rule for any G1 memo (B1, B3, B4).
13. **III₁ is forced by the single pole** (G1_B2_R5 Thm R): not an obstruction; the arithmetic must live in the topology of
    the μ-null orbit set and the leafwise Hodge projection (Thm U). This relocates, rather than kills, the Deninger route.
14. **Premise-level item to verify**: the unread web hit in G2_B6_R3 §0 (possible certified [compl] positivity beyond 0.8).

---

## §6 Definitions a memo needs verbatim (file and line)

### 6.1 Paper 46 (`04-papers/46-row-d-dual-certificates/main.tex`)

**Symbol, form, complete form, `P_T`** (l.114–138):
```latex
$\IT=(-T,T)$, and for $F\in L^2(\IT)$ (extended by zero) we write
$\Fh(\tau)=\int F(t)e^{i\tau t}\,dt$ and $\cF(u)=\int F(t)\overline{F(t-u)}\,dt$ ...
\begin{equation}\label{eq:symbol}
m(\tau)=\Rel\psi\!\left(\tfrac14+\tfrac{i\tau}{2}\right)-\log\pi,\qquad
\sT(\tau)=m(\tau)-\sum_{n\in\NT}v_n\cos(\tau\log n),\qquad v_n=\frac{2\Lambda(n)}{\sqrt n},
\end{equation}
where $\NT=\{n\ge2:\ \log n<2T\}$ is the set of \emph{contacts} ...
\begin{equation}\label{eq:form}
\mathfrak a_T(F)=\frac1{2\pi}\int_\R\sT(\tau)\,|\Fh(\tau)|^2\,d\tau ,
\end{equation}
... The two \emph{Tate moments} are $A(F)=\int F(t)e^{t/2}dt$ and
$B(F)=\int F(t)e^{-t/2}dt$, and the \emph{primitive subspace} is
$\PT=\{F\in L^2(\IT):A(F)=B(F)=0\}$. The \emph{complete Weil form} on the window is
\begin{equation}\label{eq:W}
W_T(F)=\mathfrak a_T(F)+2\,\Rel\big(A(F)\overline{B(F)}\big),
\end{equation}
which by the Weil explicit formula equals $\sum_\rho\Phi_F(\rho)\Phi_F(1-\rho)$,
$\Phi_F(s)=\int F(t)e^{(s-\frac12)t}dt$ ...
```
**Bottoms** (l.146–147): "Write `\lamA` for the bottom of `\mathfrak a_T` on the unit sphere of `\PT` and `\lamW` for that
of `W_T` on the unit sphere of `L^2(\IT)`; `\lamW\le\lamA` since the two forms agree on `\PT`."

**Polar functions** (l.341–343): `g_0(u)=\cosh\tfrac u2\,\mathbf 1_{|u|<2T},\qquad g_1(u)=u\sinh\tfrac u2\,\mathbf 1_{|u|<2T}`.

**Lévy density and `C_0`** (`lem:K`, l.363–369):
```latex
$K(u)=\dfrac{2e^{3u/2}}{e^{2u}-1}=\dfrac{1}{2\sinh(u/2)}+\dfrac{1}{2\cosh(u/2)}$ ...
m(\tau)= C_0+\int_0^\infty(1-\cos\tau u)\,K(u)\,du,\quad C_0=\psi(\tfrac14)-\log\pi=-5.3721834\ldots
```
**The form as a Lévy energy** (`thm:A`, `eq:Aform`, l.416–421):
`\mathfrak a_T(F)=C_0\|F\|^2+\Lev(\cF)-\sum_{n\in\NT}v_n\cF(\log n)`, with
`\Lev(\Phi):=\int_0^\infty(\Phi(0)-\Rel\Phi(u))K(u)\,du`.

**`def:PD`** (l.553–560):
```latex
\textbf{(P)} $\ \lamP=\inf\big\{\int_\R\sT\,d\mu:\ \mu$ an even probability measure on $\R$,
$\check\mu(u)=0$ for $|u|\ge2T$, $\int\gh0\,d\mu=\int\gh1\,d\mu=0\big\}$.
\textbf{(D)} $\ D_T=\sup\big\{\inf_{\tau\in\R}\big[\sT(\tau)+\nuh(\tau)+\beta_0\gh0(\tau)+\beta_1\gh1(\tau)\big]:\
\nu$ a finite even signed Borel measure with $\supp\nu\subseteq\{|u|\ge2T\}$, $\beta\in\R^2\big\}$.
A triple $(\nu,\beta_0,\beta_1)$ with $f:=\sT+\nuh+\beta\cdot\widehat g\ge c$ on $\R$ is a
\emph{certificate of value $c$}.
```
**`def:W` and `eq:nuw`** (l.1219–1227):
```latex
$\Wcl$ is the set of even measurable $w:\R\to\R$ with $w\equiv1$ on $[-2T,2T]$ and
$|w(u)|\le Ce^{-(\frac12+\delta)|u|}$ for $|u|\ge2T$, for some $C,\delta>0$. $\Wcl^{\mathrm{reg}}\subset\Wcl$
consists of the $w\in C^\infty(\R)$ with compact support. For $w\in\Wcl$ define the even measure
d\nu_w=\Big[\tfrac12\big(1-w(u)\big)K(|u|)+2w(u)\cosh\tfrac u2\Big]\mathbf 1_{|u|\ge2T}\,du
-\sum_{n\notin\NT}\tfrac{v_n}2\,w(\log n)\,\big(\delta_{\log n}+\delta_{-\log n}\big),
and $f_w:=\sT+\nuh_w+2\gh0$.
```
**`thm:Z`** (l.1234–1250): (i) for every `w ∈ 𝒲_T`, `f_w(τ) = C_0 + ∫_0^∞(1 − w(u)cos τu)K(u)du − Σ_{n≥2} v_n w(log n)
cos(τ log n) + 2∫_R w(u)cosh(u/2)cos(τu)du`, the right side of the explicit formula for `h_τ(u) = w(u)cos(τu)`; (ii) for
`w ∈ 𝒲_T^reg`, `f_w(τ) = Σ_ρ ŵ(τ − γ_ρ)`, absolutely convergent.

**`RD_T`** (l.3363–3367): "For a nonnegative arithmetic function `a` on `n ≥ 2` write `v_n(a) = 2a(n)/√n` and
`λ_min(A_T(a)|P_T)` for the bottom on `P_T` of the form (eq:form) built with these weights ... say that row D holds at `T`
for `a`, written `RD_T(a)`, if `λ_min(A_T(a)|P_T) ≥ 0`; `RD_T := RD_T(Λ)` is `λ^A_T ≥ 0`. (`RD_T` is not the dual value
`D_T` of Definition def:PD.)"

**`prop:finite`(ii)–(iii)** (l.3383–3395): `𝒱_T := {v ∈ R^{N_T} : 𝔞^{(v)}_T ≥ 0 on P_T ∩ form domain}` is closed and
convex, `= ∩_F {v : Σ_n v_n c_F(log n) ≤ C_0 + Lev(c_F)}`; `0 ∉ 𝒱_T` for `T > T_0(0) = 0.74921`, indeed for `T ≥ 0.60`.

**`thm:SC`** (l.2184–2195): nonnegative weights of total mass `A` on any set of contacts give a bottom on `P_T` at most
`C_0 + A + φ((3π/2T)²)`; if `A < −C_0 = 5.3721834…` the form is negative on `P_T` for every `T > T_0(A)`
(`T_0(0) = 0.74921`, `T_0(½) = 1.23295`, `T_0(1) = 2.01848`, `T_0(2) = 4.63567`, `T_0(4) = 13.19461`, `T_0(5) = 29.60905`).

**`cor:void`** (l.3563–3574): "Let `𝒞` be a class of nonnegative arithmetic functions containing `Λ`. If `𝒞` is closed
under deletion of finitely many terms, then for every `T > T_0(0)` some `a ∈ 𝒞` fails `RD_T(a)`; if `𝒞` is closed under
amplification of one term, then for every `T > ½log 2` some `a ∈ 𝒞` fails `RD_T(a)`." Classes named: `𝒞_PNT(ε)`,
`𝒞_zeros = {a ≥ 0 : ζ_a = ζE, E entire and zero-free}`, `𝒞_BT = {a : 0 ≤ a ≤ Λ}`.

**`thm:finZ`** (l.1488–1496): for a finite symmetric multiset `Z ⊂ R∖{0}`, `|Z| ≥ 2`, and even continuous integrable `w`
with `w ≡ 1` on `[−2T, 2T]`, `w → 0`, the function `Σ_{γ∈Z} ŵ(τ − γ)` takes negative values; every truncation of a
flat-top certificate fails.

**`thm:margin`** (l.3277–3285): `λ^W_T ≤ λ^P_T ≤ λ^A_T ≤ 𝓑(T,k)`; consequently `limsup_{T→∞} λ^A_T ≤ 0` (with
`cor:margin1`: `≤ 4·10⁹Te^{−15.449T}` for `T ≥ 1`).

**`prop:uniform`** (l.3607–3616): `RH ⟺ ∀T: RD_T ⟺ ∀T: v_T(Λ) ∈ 𝒱_T`; (a) fixed `T` is a statement about the finite list
`{Λ(n) : n < e^{2T}}` and `m`; (b) no finite initial segment of `Λ` decides `∀T RD_T`.

Other labels to check against (locations): `cor:mono` l.459, `lem:monoT` l.483, `thm:D1` l.601, `thm:O` l.665, `thm:C`
l.1025, `cor:RH` l.1328, `lem:Rrig` l.1374, `thm:KEP3` l.1753, `cor:Tarch` l.2630, `prop:archneg` l.2660, `thm:arena`
l.3012, `lem:cpos` l.3419, `cor:Qp` l.3431, `thm:finmod` l.3452, `rem:resweights` l.3484, `lem:degen` l.3522,
`prop:finsupp` l.3543, `thm:parityschur` l.3814, `cor:convfail` l.3996.

### 6.2 Paper 47 (`04-papers/47-intersection-frame-defect/archive/main.md`)

**T1** (l.4836–4849): "**Theorem 18.1 (T1, field uniformity; `METHOD-CONSTRAINT`).** Let `𝔓` be any list of properties of a
completed zeta function that holds for `ξ` and holds for `ξ_K` for every number field `K`. Then no derivation of the
Hodge-index inequality (18.2) from `𝔓` alone can be sound unless GRH holds for `ζ_K` for every number field `K`. …
(ii) any property invoked at a load-bearing line of a proof of the sign for `ξ` must be named, and must be a property that
`ξ` does **not** share with every `ξ_K` — or else the proof proves GRH for all number fields, and must be held to that
standard."

**Rem 18.1a** (l.4862–4866): "T1 is a statement about admissible derivations, not about functions … uniformity of a
*definition* transfers a *proof*, never the *truth* of a conclusion. It does not say that the sign is false, and it does
not say that GRH is out of reach."

**T2** (l.5328–5345): "**Theorem 18.16 (T2, the Epstein constraint; `METHOD-CONSTRAINT`).** *There is no derivation of the
Hodge-index inequality (18.2) for `ξ` from the axioms A1–A6 together with A2⁺ and the data `𝔇` alone.* … **Consequently,
any proof of the sign must invoke, at some line, one of A7, A8, A9** … > **a proof of the sign must use A3 (equimodularity),
must use at least one of A7 / A8 / A9, and must be uniform in the number field.**"

**§21.7, Rem 21.23** (l.9346–9354): "the cone `𝓔_C` is the cone on the **multiplicative semigroup** `{π^n}` and its
transposes `{π̄^n}`, and **nothing else**. The missing effective classes are exactly the graphs `Γ_{m+nπ}` of the **sums**
… the frame keeps `Frob_m ⋆ Frob_n = Frob_{mn}` … and **has no `+`**."

**§28.4, the reopening rule** (l.12634–12648): "A single object, and nothing less: a construction `𝒪` on the adelic square
satisfying all six of (1) it is a **square**, hence positive after every twist, in the Rankin sense; (2) its **polar
divisor is determined by local data** …; (3) the contribution of the zeros is **holomorphic to the left of that a priori
pole**; (4) it **reads phase**, hence fails for `Ξ_a`; (5) it uses both the additive and the multiplicative structure,
hence fails for `Ξ_Q` and for every Beurling system; (6) it is **uniform in the number field** (T1)."

Frame-defect theorem: Thm 19.25 at l.6407, Cor 19.25b at l.6510, Rem 19.26 at l.6578; §28.3a (phase 157) l.12221; §28.3b
(phase 158) l.12454; Prop 28.4 (NG-E1 proved form) l.12374.

### 6.3 Phase 157–158 definitions

**F1–F5** (`phase-157-row-d-mechanism-search/R157_000_BLUEPRINT.md` l.7–11):
```
F1 uses exact values of `Λ(n)` (or of the zeros), not only class properties — `cor:void`, `thm:finmod`, `cor:convfail`.
F2 is uniform in `T` with no margin (`thm:margin`, `cor:margin2`) and no upward induction (`cor:mono`, W15).
F3 does not rest on a finite truncation (`thm:arena`, `thm:finZ`), a termwise sign (`lem:Rrig`, `thm:SC`), or an identity (`thm:O`).
F4 is not a Beurling-class argument (T3, now METHOD-CONSTRAINT modulo the CITED (secondary source) import (H-DMV′)) and invokes A3 and one of A7/A8/A9 (T2, Epstein). [amended per R157_004: T1 excludes only derivations from properties shared by all ξ_K that stop short of GRH for all K.]
F5 is not an `h⁰` construction in the intersection frame (P47 Thm 19.25, now on the small domain), and not a Deligne extraction (T5, T6).
```
Amended Lemma P157.S1 clause (b′) (`R157_002` l.626–629): "if the positivity of `𝓔` is *inferred* from positivity of the
`𝓔_v`, or of `𝓔_∞ + Σ_{v∈S}𝓔_v` for a finite `S`, it is excluded by `prop:finsupp`/`thm:SC` (PROVED)".

**Lemma T data** (`phase-158-row-d-mw5-object/R158_001_SPEC_SHEET.md` l.209–219):
```
(D1) a complex Hilbert space `H¹` with a strongly continuous group `φ^t` whose generator `Θ` has discrete spectrum,
     and `H⁰ = H² = C` with `Θ = 0`, `Θ = 1`;
(D2) the trace formula: `∫h(t) e^{tΘ}dt|_{H¹}` is trace class for `h ∈ C_c^∞(R)`, and the eigenvalues of `Θ` on
     `H¹`, with algebraic multiplicity, are the non-trivial zeros of `ζ` …;
(D3) the conformal positivity: the given inner product satisfies `⟨φ^tα, φ^tβ⟩ = e^t⟨α,β⟩` …
Then (D1)–(D3) are satisfiable if and only if RH holds [(⇒) for every realisation; (⇐) witness built from the zeros].
```
**Object test** (R158_001 l.300–314; status of each item in Rem 3.0, l.328–342). The decisive item, verbatim (l.307):
"**OT-5′ Prior positivity** | Is the positive form (P-HS or P-HI) defined from geometry of `𝒪` alone, and is its
compatibility with the flow (conformality `e^t`, or Hodge index on the primitive part) **proved** without eigenvalue data?
Would `𝒪` still exist, with the form still defined, if a zero were off the line (NC4 of Doc 119/130)? | a proof valid
'whatever the position of the zeros'". Also OT-2 (l.303): a **proved** Lefschetz formula equal to P46 `eq:W`/`thm:Z(i)` for
all `h ∈ C_c^∞(R)`, with `m(τ)`, `v_n = 2Λ(n)/√n` and the polar pair; OT-4 (l.305): rerun the definition with
`Λ + εδ_{n₀}`, `Λ·1_{n≥N}`, `ζ·E`, a DMV/Zhang system, `Ξ_Q` — each must break a named axiom or a named line of the
positivity proof. Passing OT-1…OT-12 does not reopen row D; §28.4 clauses (2), (3) are separate (Rem 3.3, l.348–355).

**N-a, N-b, N-c** (`R158_005_CLOSING_DECISION.md` l.22–25): "N-a: definiteness for a reason that precedes the
spectrum. The object must deliver the count, never the positivity (P47 §21.7). N-b: for the definite/unitary route only, a
non-cyclic `H¹` (HEURISTIC: a correspondence algebra with `+`). N-c: for the Riemann–Roch route, a two-variable effective
cone strictly larger than `𝓔` that carries information outside the frame's invariants. Its constructive clause is
RH-strength."

### 6.4 Phase-159 comb notation (used by G2 rigidity results)

From `phase-159-row-d-two-front-construction/G2_B9_R3.md` l.72–80 and `G2_B6_R4.md` l.73–79:
`u_a := k_∞ + 2cosh(u/2) − Σ_{n≥2}(a(n)/√n)(δ_{log n} + δ_{−log n})` (the Weil distribution of a real comb `a`; `k_∞` =
inverse Fourier transform of `m`), so that `W^{(a)}_T(F) = ⟨u_a, c_F⟩` for real `F`; `β_b := Σ_n b_n n^{−1/2}(δ_{log n} +
δ_{−log n})`, `D_b := β̂_b`; `𝒮^W` = combs with `u_a` positive definite (`λ^W_T(a) ≥ 0 ∀T`), `𝒮^A` likewise for `RD_T(a)
∀T`; `ℓ¹_w = {b : Σ|b_n|n^{−½} < ∞}`; `𝒯 = {b real : β_b ∈ 𝒮′}`; `𝒯_meas = {b ∈ 𝒯 : D_b locally finite measure,
|D_b|(Γ_ζ) = 0}`; under RH `û_Λ = 2πμ_Λ`, `μ_Λ = Σ_γ m_γ δ_γ`. Growth exponents: G2_B2_R4 uses `κ = limsup (2T)^{−1}
log⁺(−λ_T)` (so `κ = Θ − ½`), G2_B10_R4 uses `T^{−1}` (so `2Θ − 1 ≤ κ^A`); convert before comparing.

---

*End of R160_S5. No sign claimed; no label changed; nothing edited outside this file.*
