# Audit of certainty — every discard of phases 190–193

Question: *"we discarded many fronts — are we really sure of everything discarded?"*
Scope: `03-research/phase-193-creation-campaign/` (all CA_*_000 seed tables, CA_* memos, syntheses, adversarial reviews,
CAMPAIGN_LEDGER.md) and the phase 190–192 verdicts in this folder's README. Pen and paper; nothing re-developed.

## 0. Strength scale and the base labels the kills rest on

Strength of a kill (weakest → strongest):
- **NUM** — rests on a NUMÉRICO datum (finite M, finite T, perturbation tests).
- **CIRC** (CIRCULAR-RISK) — the killing clause itself is ARGUED / CONDITIONAL / OPEN in Paper 47 (list below).
- **1L** (ONE-LINE) — a pre-screen sentence, no development, reviewer said only "✓".
- **ARG** (ARGUED) — written reasoning in a memo, no proof.
- **RD** (REF-D) — PROVED that the object *is* the target restated: **this is not a closure**, since a reformulation of D is
  a valid objective, attacked by its constructive tractability. An RD discard means "no progress by itself", never "impossible".
- **CIT** (PROVED-BY-CITATION) — rests on a PROVED Paper 47 lemma / falsifier (O1–O4, O6–O8, O13–O15; lem:shape-ident (B″);
  lem:shape-est (i)–(ii); thm:O; thm:sos; cor:Qp; cor:Tarch; σ_T(0)<0) whose hypotheses were checked to cover the seed.
- **THM** (PROVED-THEOREM) — a written, reviewed proof covering this exact construction.

Status of the clauses that kills invoke (grep-verified in Paper 47 main.tex, def:shape-ops l. 8328, thm:shape l. 8853,
lem:shape-* l. 8370–8527, lem:shape-est l. 8664):

| clause | status in Paper 47 | effect on kills that use it alone |
|---|---|---|
| O1, O2, O3, O4 (c large/small), O6, O7, O8, O13, O14, O15 falsifiers | PROVED | sound (CIT) |
| O4^ε, O5 | CONDITIONAL on κ_T ≠ 0 / c_{F⋆}(log n₀) ≠ 0 | CIRC |
| O10 Epstein | CITED for the complete form, ARGUED for the primitive bottom | CIRC for primitive-bottom kills |
| O11 Beurling | ARGUED (no window form of a Beurling system shown negative) | CIRC |
| O12 ζ_K | falsifier OPEN; (R)(10) is a standard-of-proof clause, not an impossibility | CIRC |
| (B′) "no estimate carries the sign" | lem:shape-est (i),(ii) PROVED, (iii) CONDITIONAL, **(iv) the reading ARGUED** | CIRC unless the seed's loss is shown > proved margin |
| (B″) identity valid for every comb | PROVED (lem:shape-ident) | sound |
| G1 "monoid-only sees nothing" | PROVED as isomorphism; excludes only via (R)(10) (O11 ARGUED, O12 OPEN) | CIRC |
| H0(b) "additive-only ⇒ shared by Epstein x²+5y²" | ARGUED (Γ(s), conductor 20) | CIRC |
| [crit] "precision M^{−3}" | NUMÉRICO (EXP_005, phase 190); the PROVED version is the margin bound 4·10⁹Te^{−15.449T} | NUM unless restated via the proved margin |
| doubly exponential margin exp(−13e^{2T}) | **NOT PROVED** (README correction : conjectural law / NUMÉRICO) | any kill using it is CIRC |

Seed vs idea column: **S** = kill covers the seed as formulated (a property set); a reformulation that adds a load-bearing
ζ-specific ingredient is not excluded (thm:shape(C) says every proof must contain one). **I** = kill covers the whole idea
(structural impossibility of the mechanism itself). **S/I** = mixed.

## 1. Full table of discards (≈105 items), grouped by strength, weakest first

Reviewer column: **C** = adversarial reviewer confirmed; **C+F** = confirmed with a FIX; **C(sc)** = confirmed with a scope restriction;
**—** = no separate review (pre-screen row only, covered by "screens CONFIRMED").

### 1a. NUM and CIRC (weakest)

| # | item | killing clause | strength | S/I | rev |
|---|---|---|---|---|---|
| 1 | P191 SPEC_A (exact induction in T by contacts) | (γ): step inherits λ_A ≈ exp(−13e^{2T}) | **CIRC** — that scale is not proved (README correction); with the proved e^{−15.449T} bound (γ) must be redone. Other kills (B8/(δ) L* = exact restatement → RD; (θ)) remain | S | phase-191 review; correction post-dates it |
| 2 | P191 conclusion "T* cannot be an estimate" | lem:shape-est | **CIRC** ((iv) ARGUED) | I-claimed, S-proved | paper itself labels ARGUED |
| 3 | CA_C_007 η-family as sign step | family positivity is FE-class generic (Epstein positive, Beurling negative) | **NUM** (Lemmas 1–2, Prop 3 PROVED; genericity NUMÉRICO) | S | C |
| 4 | CA_C_003/005 (Fam_η) | necessary-only for η>2/3; criticality retracted | NUM | S | C+F (MAJOR FIX: μ_M lower bound only) |
| 5 | P190 "Near statistics as ζ fingerprint" | [sens]: identical to 5 digits under 1e-5 perturbations | NUM (logic sound: 1e-5 ≫ λ_A ⇒ (R)(5),(6)) | S | — |
| 6 | P190 (Ω₀) as filter | passes amp2, ±1e-2 | NUM | S | — |
| 7 | J4′ geometric Brascamp–Lieb / BCCT | dimension data; Beurling (O11) passes | **CIRC** (O11 ARGUED is the only falsifier named) | S | C |
| 8 | H10 arithmetic derivative | G1 ⇒ (R)(10) | CIRC (O12 OPEN) — but genuinely monoid-only | S | C |
| 9 | G10 sign-reversing involutions | G1, (R)(10); + G0(b) SOS | CIRC on the G1 half; the G0 half is RD | S | C |
| 10 | G12 Hecke algebra of ℕ^× ("Soergel on the monoid") | G1/(R)(10); with ℕ it is comb-only ⇒ O7 | CIRC (monoid form) / CIT (comb form) | S | C |
| 11 | C_004 D4 Iwasawa | ranks/valuations carry no real sign; (R)(10) | 1L category argument + CIRC (R)(10) | I (category) | C |
| 12 | E1 KMS beyond Bost–Connes | real β only; O11; (R)(2); retry 114_d_116 | CIRC on O11; "real β only" ARG | S | C |
| 13 | G5 VOA / moonshine | O10 via lattice-VOA characters | CIRC (O10 primitive bottom ARGUED) | S | C |
| 14 | C_001 product-formula tolerance cells (O4^ε, O5) | lem:shape-est(iii) | **CIRC** (CONDITIONAL κ_T≠0); ledger: "2 cells CONDITIONAL"; all cells also fall to O7 (CIT) | S | C |
| 15 | E8 Golden–Thompson / Gibbs | (B′); commuting before compression (GT = equality) | the "equality" half is THM-level (elementary); (B′) half CIRC | I | C |
| 16 | E9 Kadison–Singer / MSS / Lee–Yang | retry phase 11; (B′); (R)(4) | CIRC on (B′); retry strength inherited | S | C |
| 17 | E2 free probability (C_006) | commuting ⇒ not free (THM); [crit]; O5 | free-part THM; [crit] NUM; O5 replaced by FIX | I (for free independence) | C+F |
| 18 | C_006 E5 Positivstellensatz on η>2/3 | SOS = class (D); [crit] premise retracted | RD (discard stands on SOS only, per reviewer) | S | C+F |
| 19 | J10 Dobrushin / Kotecký–Preiss; K13 TAP/Plefka | perturbative ⇒ cannot reach [crit] | ARG + NUM ([crit]); intuitively solid (constant-factor loss vs proved margin) | I | C |
| 20 | K7 signed Laplacian / Cheeger | Cheeger reaches ½, need 1−O(1/M) | ARG/NUM ([crit]); developed in CA_K_001 §4 (decomposition PROVED, inequality loss) | S | C |
| 21 | I7 Γ-convergence | o(1) absolute vs margin | ARG; leading-term only — sound in spirit (proved margin suffices) | I | C |
| 22 | H4 sum-product (Erdős–Szemerédi/Solymosi) | set statements ignore weights; survive O2/O6/O7/O15 | CIT for survival under PROVED falsifiers (O2, O7, O15 keep supports) ⇒ actually strong | S | C |
| 23 | M5 Hardy–Littlewood singular series | conjectural input; resolution mismatch; (B′) | ARG §1.3; PROVED in decisive class via CA_M_001 Thm 3.1 | S | C |
| 24 | M7 Vinogradov arcs | only θ≈0 arc weighs (ARG §1.4); major arc comb-generic | ARG | S | C |
| 25 | F7 Selberg/horocycle equidistribution | estimates (B′); Selberg L31 | 1L + CIRC (B′) | S | C |
| 26 | C_006 E4 Helson H²(𝔻^∞) | torus/line (CA_C_002 Prop 2) + (B′) | RD + CIRC | S | C |
| 27 | C_006 E3 Ax–Schanuel | O11/O15; [crit] | CIT via O15 (PROVED) | S | C |

### 1b. ONE-LINE and ARGUED

| # | item | killing clause | strength | S/I | rev |
|---|---|---|---|---|---|
| 28 | **D8 amplitude-exponent homotopy W(α)=∫Θ′\|F̂\|²\|Z_X\|^{2α}** | non-integer α needs zero-free Z_X^α ((R)(4)); integers don't control α=0 (no Carlson rigidity) | **1L/ARG** — the (R)(4) half concerns a holomorphic construction; W(α) itself is defined pointwise for every real α ≥ 0 without zeros | **S** | C (1 line) |
| 29 | CA_A_002 Lewis–Zagier / Mayer | Λ absent; det = zero side; PF only at real s | **ARG** (NO-GO ARGUED; ψ_s formula CITED-UNVERIFIED) | S | C |
| 30 | C_004 D2 rationality ζ(2k)/π^{2k} | O7 with rational quartet parameters | ARG (reviewer: witness on an open parameter set "plausible"); (R)(5) CIT | S | C+F |
| 31 | C_004 D3 Kummer / p-adic | ℚ_p unordered (CA_C_002 Prop 1 THM); O7 ARG | THM (category) + ARG | I (as inequality at p) | C |
| 32 | C1 weighted Hasse–Minkowski split | per-place bounds; each 𝔮_p ≤ c_p𝔞_∞ on the negative cone contradicts cor:Qp | ARG (reviewer: the construction's REF-D reason wrong; right kill ARGUED) | S | C+F |
| 33 | C5 condensed HM with archimedean (liquid) input | — | **ARG** ("not covered — keep ARGUED", C_000 review; F_001 PROVED only three declared classes) | S | C(sc) |
| 34 | F3 condensed MW-3 (generic) | O6 closes every condensed HM hypothesis | ARG (upgraded to THM only for 3 declared classes in CA_F_001) | S | C(sc) |
| 35 | F5 Hodge–Riemann / Lorentzian (non-AHK) | retry; signature hypothesis fails | ARG (Theorem P mis-cited; FIX) | S | C+F |
| 36 | CA_A_007 §4 t-concavity of log\|ξ\| (NG-D2) | (R)(4)/prop:shape-twist, O9 | ARG, not developed | S | C ("ACCEPTED") |
| 37 | CA_A_007 §4 rigged eigenvectors x^{b+iγ} | zero side unless rigging from primes | ARG — escape explicitly named (prime-built rigging) | S | C |
| 38 | CA_A_001 extension "any PSL₂(ℤ) Eisenstein positivity" | — | **WITHDRAWN**; NO-GO only for the norm class (THM) | S | C(sc) |
| 39 | CA_A_004 Cor 3 (metaplectic Parseval = arithmetic squares) | thm:sos class | ARG ("not checked that thm:sos literally covers squares of ζ/L-values") | S | C+F |
| 40 | CA_I_002 DH transversality | — | ARG | S | C |
| 41 | CA_I_001 general-E Markov formula | — | ARG (FIX) | S | C+F |
| 42 | CA_F_003 trichotomy for invariants outside 𝒢_u | — | ARG | S | C |
| 43 | E3 Jones index / TL Gram | no object; O6; integer collapse | 1L ("no map known or constructible") — absence of object, not impossibility | S | C |
| 44 | E10 Araki / Petz | wrong monotonicity direction (lem:monoT) | CIT for direction; 1L otherwise | S | C |
| 45 | E6 CCR / Robertson | retry 114_d_92/142/195, R178; global square | inherits retries (R178 NO-GO) | S | C |
| 46 | E11 operator systems / Arveson | KEP indeterminacy (RD) | RD, 1L | S | C |
| 47 | E12 NC-SOS / de Finetti | (R)(3); commutative collapse (THM CA_E_001) | CIT | I | C |
| 48 | F6 Weyl/heat invariants | spectral + (B″) | 1L | S | C |
| 49 | F9 DAG / ∞-traces | ES-20; T1 | 1L (object unbuilt; = G-F OPEN) | S | C |
| 50 | F13 perfectoid tilting | ℚ_p unordered; function fields L25 | 1L | S | C |
| 51 | F14 homogeneous dynamics (exact) | Bochner class; σ_T(0)<0; (B″) | 1L + CIT | S | C |
| 52 | F15 nef/ample, Nakai–Moishezon on arithmetic square | class (D) | 1L, RD | S | C |
| 53 | F8 calibrations | dual certificate, class (D) | 1L, RD | S | C |
| 54 | F11 cluster positivity (front F) / G7 cluster TP | comb-type (O2/O6); PF₅ fails CITED, **PF₄ OPEN** | CIT for O2/O6; the TP order-≤4 residue is OPEN | S | C |
| 55 | G4 categorification / graded dimension | G0(c) | 1L, RD | S | C |
| 56 | G8 Jordan / symmetric cones | self-duality = thm:D1 | 1L, RD | S | C |
| 57 | G9 Connes–Kreimer Birkhoff | = Wiener–Hopf (W-det) | 1L retry | S | C |
| 58 | G11 quantum groups / Shapovalov | retry NG-67 | 1L retry | S | C |
| 59 | G6 Lorentzian polynomials | retry R138 D.15.2 | retry (PROVED criterion, no sign) | S | C |
| 60 | G2 Clifford / Weitzenböck | both summands indefinite (cor:Tarch, cor:Qp) | CIT for natural split only; other splits not covered | S | C |
| 61 | H2 Stepanov over ℤ | retry G1_B9 Lemma 3 | CIT (char-0 Lemma 3 PROVED) | S | C |
| 62 | H3 carries / Witt vectors | form is carry-blind | ARG (folded into CA_H_001 §1.4) | S | C |
| 63 | H7 integrality gap / Liouville | density ceiling only (thm:ceiling) | CIT (necessary direction) | S | C |
| 64 | H9 CRT divisibility (SPEC_B line 3) | W7 linear; RD for η≤η₀ | RD/retry | S | C |
| 65 | I6 unique continuation | automatic (Paley–Wiener) | THM-level elementary | I | C |
| 66 | I8 concentration–compactness | quadratic ⇒ no strict subadditivity | ARG (short) | I | C |
| 67 | I3 symmetrization | Tate constraint not rearrangement invariant (Prop 5.1) | THM in CA_I_001 §5 | S | C |
| 68 | I5 Almgren frequency | frequency unbounded (Prop 2.2) | THM | S | C |
| 69 | J3 Ginibre/GHS/Lebowitz; J7 Gaussian domination; J9 FK; K9 Lieb flux | presuppose ferromagnetic/RP ⇒ die with J1/J6 | CIT (Thm 1.3 frustration, CA_J_001 Thm 1–2 PROVED) | I (for these inequalities) | C |
| 70 | J5 Prékopa–Leindler | PF route; PF₅ fails | CIT (PF₅), PF₄ OPEN | S | C |
| 71 | J8 strong Rayleigh | zero location (Lee–Yang family) | 1L (R)(4) | S | C |
| 72 | J4 Brascamp–Lieb variance | input Hess V ⪰ 0 = target | RD | S | C |
| 73 | K2 Talagrand/Parisi | no disorder | 1L, sound | I | C |
| 74 | K11 Doob transform | retry Paper 41 | retry | S | C |
| 75 | K12 frustration-free decomposition | bare local positivity false at every p (CA_F_001 Prop 3) | CIT | S | C |
| 76 | L3 Cohn–Elkies | gives upper (Odlyzko) direction | THM (CA_L_001 Prop 1.3) | S | C |
| 77 | L4 RV interpolation | retry P35-4; finZ | CIT | S | C |
| 78 | L7 Cohn–Gonçalves sign uncertainty | bounds a radius, not a form; comb-generic | 1L | S | C |
| 79 | L9 CKMRV | needs lattice discrete set | 1L | S | C |
| 80 | L10 self-dual theta + sinc | FE only (R164_401) | retry | S | C |
| 81 | M4 sieve weights | W-sieve, NG-A4 parity | CIT (R167_102) | S | C |
| 82 | D3 Landau / Bohr–Jessen | retry R164_102 (ζ·E falsifier) | CIT | S | C |
| 83 | D4 Kramers–Kronig | (R)(4) or (B″) | CIT/1L | S | C |
| 84 | D5 Riemann–Siegel FM | R163_603 (f_χ) | CIT | S | C |
| 85 | D6 scattering causality | ⟺ zero-free half-plane (R)(4) | THM-level | I | C |
| 86 | D7 de Branges / Kreĭn | Θ′ not pointwise >0; positive extension = certificate | CIT (σ_T(0)<0; thm:Z) | S | C |
| 87 | C_004 D5 FE unitarity | prop:shape-phase, (B″) | CIT | S | C |
| 88 | C2 Lévy–Khintchine per place | (B″), O7/O11/O15, (R)(7) | CIT | S | C |

### 1c. REF-D (PROVED to be the target restated — not a closure)

| # | item | what it restates | rev |
|---|---|---|---|
| 89 | C4 Tate residues / adèle class space | Connes' formulation | C |
| 90 | C6, H6, CA_C_002 Prop 2, CA_H_002 Thm 3.1 | (S): Near = Kronecker line − Haar | C |
| 91 | C_004 D1 Nyquist mesh | (N) | C |
| 92 | C_004 D6 / I9 minimizer local law, Lemma S | Theorem X / C*_A | C |
| 93 | E4 CP / Choi; CA_E_001 Thm 1 | separability: D ⟺ positivity on Euler product vectors | C |
| 94 | F1 Floer, F12 capacities, F4 A¹/RO(G), CA_F_003 Prop 2 | spectral data / signature of 𝔞_T | C |
| 95 | F2 Bridgeland | support property on ker Z = P_T | C |
| 96 | G1 SUSY (Witten/Riccati), G0 Gram | factorization ⟺ positivity | C |
| 97 | G3 / CA_G_001 §3 Elias–Williamson ladder | primitive complement carries the target; Schur tower | C |
| 98 | K3 cavity, K4 Grothendieck/SDP, K5 Lasserre, L8 Delsarte | Schur reductions / dual certificate | C |
| 99 | K1/K10 Guerra, heat flow on Ĝ (CA_K_002 Thm 1.2) | deterministic path sign = minimizer statement | C |
| 100 | L5/L6 prime-site LP, torus certificate (CA_L_002) | attained dual, slackness on Z_s, exact for \|X\|≤5, comb-generic | C |
| 101 | CA_A_008 integer invariant / spectral flow; CA_A_007 §1 homotopy | no-crossing = positivity | C |
| 102 | CA_B_007 convex decomposition; CA_B_008 concavity gap Γ | affine split writes target via own spectral data | C |
| 103 | CA_A_003 §3, CA_A_005, CA_A_006(i) (S) continuation | (S) | C |
| 104 | **CA_I_001 Cor 6 property set 𝖯⋆** | discarded as "separation, not an inequality — REF-D as route" | C |
| 105 | P191 SPEC_B T*₂ correlated, T*₃(η); P192 EI_001/EI_002 sign content | (N), (S), C*_A | phase-192 review |

### 1d. PROVED (THM / CIT covering the exact construction) — the solid core

CA_A_001 (norm class, Cor 3), CA_A_003 §2 (Hecke multiplicativity comb-generic), CA_A_005 (RS minimizer, comb-blind),
CA_A_006(ii) (abscissa transport), CA_A_007 Thm 2 (RP fails for every atomic comb), CA_B_001 (zero side), CA_B_002, CA_B_003
(Δ≡0 ⟺ FE; excluded by O7 alone), CA_B_004 (J(1)=∞, pole), CA_B_005 (inversion false), CA_B_006 (Euler-tail membership),
CA_C_001 Thm 1 (exact/one-sided PF; all cells fall to O7), CA_C_002 Prop 1 (classical HM class), CA_C_006 E1 Pila–Wilkie
(semialgebraic ⇒ vacuous — elementary, labelled ARGUED by the index but essentially immediate), CA_D_001 (tool; excluded by
(R)(10),(11) — note O12 leg is CIRC, O10 leg cited), CA_D_002 (closure NO-GO, PROVED), CA_D_003, CA_E_001 Thm 2 (Schur
factorization NO-GO), CA_F_001 (three classes), CA_F_002 (TF⁺), CA_H_001 (𝒦_δ, declared class only), CA_H_002 (S⁺) (O7,
comb-only), CA_I_001 Thm 2 (Markov via O2), CA_J_001 (lattice RP ⟺ lattice support), CA_J_002 (frustration Thm 1.3; FKG
equality class), CA_K_001 (diamagnetism, order reversal), CA_K_002 Thm 3.2/Cor 3.3, CA_L_001 (thm:O; level-20 Epstein,
level 1 reduced — **level-20 NO-GO uses O10 on the complete form: CITED**), CA_M_001 (site arithmetic information-free;
reversal = FE cancellation), P192 EI_001–003 (identities valid for every comb ⇒ (B″), PROVED; EI_003 Thm 2 correctly
withdrawn as a NO-GO).

## 2. Systematic findings

1. **REF-D is the single largest discard category (≈30 items) and it is not a closure.** Every RD verdict
   is PROVED as an equivalence, but reformulations of D are valid objectives in their own right. The campaign used "REF-D" as a
   stop. The correct label is "restatement — rank by constructive tractability". None of these was ranked by tractability.
2. **Kills resting on CIRC clauses** (O11 ARGUED, O12 OPEN, O10 primitive ARGUED, (B′)(iv) ARGUED, κ_T≠0 CONDITIONAL, H0(b)
   ARGUED, G1 via (R)(10)) account for ≈15 items. In most of them a PROVED falsifier (O2, O7, O15) or (B″) also applies, so the
   kill survives the downgrade. **The exceptions — killed by a CIRC clause alone — are J4′ (O11 only), H10/G10/G12-monoid (G1
   only), D4 Iwasawa ((R)(10)), G5 VOA (O10 primitive only), SPEC_A ((γ) used the unproved doubly-exponential scale).**
3. **The [crit] screen rests on NUMÉRICO M^{−3}.** The proved substitute (margin ≤ 4·10⁹Te^{−15.449T}, lem:shape-est(i)) supports
   every [crit] kill against perturbative/constant-loss methods, but only through the ARGUED reading (iv). The kills are very likely
   right; their label is ARG, not PROVED.
4. **Almost all O-kills are seed-level (S).** thm:shape(C) guarantees a proof must contain a property destroyed by all
   modifications; a seed killed because it survives O7 is killed *as formulated*, and the idea escapes if a load-bearing ζ-specific
   ingredient is added. Idea-level (I) kills are few and solid: commutative collapse/Schur NO-GO (E), RP false for every atomic comb,
   frustration (no ferromagnetic gauge), Markov class via O2, magic function via thm:O, free independence of commuting elements,
   Pila–Wilkie vacuity, Golden–Thompson equality, closure of the Hardy cone.
5. **Adversarial reviewers confirmed every discard**, but several confirmations are one-line "✓" on one-line kills (F6–F15, G4–G11,
   E3, E10–E12, J8, K11–K12, L7–L10). Confirmation of a one-line kill is itself one-line.
6. **Labels that drifted upward**: index README phrase "NO-GO" for Lewis–Zagier (ARGUED), condensed MW-3 generic (ARGUED; PROVED only
   for three classes), Pila–Wilkie (ARGUED in index although near-immediate), SPEC_A (rests on the retracted scale). Recommend
   re-labelling in the README (not done here: audit only).

## 3. Discards that deserve re-examination, ranked by plausibility of an escape

1. **CA_I_001 Cor 6 — the property set 𝖯⋆ = {(S⁺), pole residue, entire with FE and Γ_ℝ, Markov ∀T}.** The only object of the
   campaign not closed under any declared single modification (O14 OPEN). Discarded as "a separation, not an inequality ⇒ REF-D as
   route" — that step is ARGUED, and thm:shape(C) says exactly that a proof must use such a property. Escape: a deduction whose
   load-bearing line is 𝖯⋆ (first: settle O14's Markov status, then ask what Markov-∀T forces on λ_A). Highest priority.
2. **CA_L_002 prime-site LP / torus certificate (L5/L6).** Attained dual, slackness set = minimizer, exact for |X| ≤ 5 — the exact
   analogue of Viazovska's structure. Killed as RD + comb-generic (true for the LP as formulated). Escape: an LP whose constraint set
   contains a ζ-specific datum (FE/pole via the archimedean column) with |X| → ∞ controlled by the elliptope rank. RD ≠ impossible.
3. **D8 amplitude-exponent homotopy W(α).** One-line ARG kill; W(α) is defined for real α without zero-freeness, and W(k) ≥ 0 at
   integers is PROVED (CA_D_001). The real question — a convexity/interpolation in α between integer data and α = 0 — was never
   examined. Seed-level kill.
4. **CA_K_002 site independence (Arch ≥ Near on prime-sited tests) and (S)/(N) restatements.** RD, but they are the most concrete
   reformulations produced (finite matrices, explicit Chen-type shifts). They should be ranked by tractability, not
   closed.
5. **CA_A_001 residue: Mellin-in-y / Rankin–Selberg in w reaching ζ(½+iτ) on the unitary axis** and **CA_A_003 §4 metaplectic
   off-diagonal packet form** — both left OPEN in the ledger, never developed; CA_A_004 Salié/Kuznetsov OPEN-RESIDUE.
6. **P191 SPEC_A.** Its main kill (γ) used the unproved doubly exponential scale; the remaining kills are RD (L* exact) and (θ).
   Re-run the (γ) check with the proved margin; the RD part then becomes a tractability question.
7. **C5/F3 condensed HM with archimedean (liquid) input** — explicitly ARGUED and uncovered by CA_F_001's three classes.
8. **G7/J5 total positivity of order ≤ 4** (PF₄ OPEN) and **CA_A_007 §4 rigged-space eigenvectors built from primes** — the
   memo itself names the escape.
9. **J4′, H10, G10/G12 (monoid form), G5, D4** — killed only by CIRC clauses; escape requires naming a property separating ζ from
   Beurling/ξ_K, which these seeds as formulated cannot do; low plausibility, but the kill is not a proof.
10. **CA_A_002 Lewis–Zagier** — ARGUED; low plausibility (Λ absent), verify ψ_s formula before relying on the NO-GO label.

## 4. Overall statement of certainty

- **Certain (PROVED, idea-level):** about 15 structural NO-GOs (commutative collapse and Schur NO-GO, RP failure, frustration,
  Markov class, thm:O magic functions, Hardy-cone closure, Hecke multiplicativity, J(1)=∞, inversion false, classical HM class,
  site arithmetic information-free, identities valid for every comb). These close mechanisms, not just seeds.
- **Certain as formulated (PROVED / CITED, seed-level):** about 35 kills through PROVED falsifiers O1–O3, O6–O8, O15 or (B″). They do
  not exclude a reformulation that adds a load-bearing ζ-specific property.
- **Not closures:** about 30 REF-D verdicts. They are PROVED restatements and remain objectives in their own right.
- **Weak (one-line, ARGUED, CIRC, NUM):** about 25 kills. Most would survive a downgrade because a PROVED falsifier also applies, but
  ≈8 rest on a CIRC clause alone or on the unproved margin scale.
- **Honest summary:** the campaign's statement "0 admissible candidates" is reliable in the narrow sense that no seed *as formulated*
  passes the PROVED filters. The stronger reading "these areas are closed" is not established: roughly one third of the discards are
  REF-D (not closures), one quarter are one-line or argued, and the single best object found (𝖯⋆) was set aside by an ARGUED step.
  No discard was found to be wrong; several are under-proved or over-labelled.
