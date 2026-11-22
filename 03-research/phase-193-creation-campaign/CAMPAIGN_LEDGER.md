# Phase 193 — Campaign ledger 
| candidate | object | verdict | YES→NO moves endorsed | open |
|---|---|---|---|---|
| CA_A_001 | Eisenstein norm / Maass–Selberg positivity | EXCLUDED (O11, O12; (R)(1),(5),(8)); Lemma 2, Cor 3 CONFIRMED (2 FIX) | "spectral-variable Eisenstein norm carries the window comb" → NO (PROVED, Cor 3 class) | line doubling NOT a general barrier: Mellin-in-y / Rankin–Selberg in w reach ζ(½+iτ) on the unitary axis |
| CA_A_002 | Lewis–Zagier / Mayer transfer operator | EXCLUDED ((R)(1),(3),(4); no comb ⇒ all O1–O7, O15 survive; O12) | index "Lewis–Zagier route" OPEN → NO-GO (ARGUED): Λ absent, det = zero side, PF only at real s | verify ψ_s formula (CITED-UNVERIFIED) |
| CA_A_003 | Hecke relations on σ_T; Hecke tests; metaplectic | §2 EXCLUDED (B″; O1–O7, O15); §3 REF-D ((S)) + (B′); §4 OPEN | "Hecke multiplicativity is a mechanism on σ_T" → NO (PROVED) | metaplectic off-diagonal packet form: show which positivity is not a norm (O11/O12, (R)(4) risk) |
| CA_B_001 | matching / σ-derivative identity J′(½) | EXCLUDED (O11, O12; (R)(4),(9)); identities CONFIRMED; sign REF-D | (R)(4), (R)(11) → NO | — |
| CA_B_002 | Riesz/Jensen decomposition of −∂_σH | EXCLUDED (zero-free reading (B″); ζ reading (R)(4); (R)(5) local) | "test = ζ's partial sum is used" → NO; (R)(4) → NO | — |
| CA_B_003 | self-matching Δ_a ≡ 0 ⟺ FE (Thm 1) | Thm 1 CONFIRMED PROVED; property EXCLUDED (O8 quartets; O9/O13/O14 when acting on form) | (R)(11) stays NO; new: comb-only ζ-specific properties fail cor:shape(a) | J(σ)-transport: name its O8-destroying datum; pre-verdict (R)(4) risk |
| CA_A_004 | weight-½ Eisenstein P₀⁺ (DIT), Parseval | EXCLUDED (comb-independent: O1–O7, O15; O12; (R)(2),(8),(11)); Prop 1 CONFIRMED; Cor 3 FIX | "metaplectic Parseval carries σ_T-correlation" → NO; line doubling withdrawn as general barrier | Salié/Kuznetsov variant OPEN-RESIDUE (low); RS with minimizer polynomial: show what fails under O2/O8 (Petersson norm holds for every b) |
| CA_B_004 | on-line symbol (Prop 1); J(σ)-transport, Green identity | EXCLUDED (B″); MAJOR FIX: pole at s=1 ⇒ J(1)=∞, convexity chain (3.3) false | "transport uses same ζ on both sides" → NO; "J-convexity across σ=1" → NO (PROVED, pole asymptotics) | — |
| CA_B_005 | matching-defect inversion; Prop 2 openness | Prop 2 CONFIRMED after FIX (radius is ℓ¹ λ_A via prop:wit-sens, NOT λ_A/κ_T); corollary of prop:wit-sens, NOT a new clause; §3 NON-SEQUITUR | "(Inv) defect⇒negative bottom at fixed T" → NO (PROVED). NOT endorsed: "exact identities excluded by openness" | — |
| CA_A_005 | Rankin–Selberg with minimizer test vector | EXCLUDED (comb-blind, test-generic, (B″)); continuation REF-D (S) | "RS/Petersson positivity with minimizer test couples to window form" → NO | — |
| CA_A_006 | MS abscissa transport 1→½ (Y-averaging; Hecke average) | NO-GO CONFIRMED: (ii) PROVED; (i) REF-D (S); Remark 3 identity; retry of MW-2 | "MS positivity carried to ½ by positive Eisenstein operations" → NO | §6 homotopy seed: segment no-crossing = target by concavity; name separating property first |
| CA_B_006 | Lemma B open ball (L_T); inner sets | (i)–(iii) CONFIRMED = P46 prop:wit-sens / l. 8348; (iv) methodological reading NOT endorsed; scale FIX; J-convexity pole FIX repeated | "Euler-tail membership as sign carrier" → NO (because (W_X) controls only I_ζζ) | inner set must be defined without λ_A (endorsed sharpening) |
| CA_B_007 | O7/O8 as point moves in 𝒱_T^meas; convex decomposition; concavity gap Γ | Labels CONFIRMED; decomposition EXCLUDED (REF-D / class (D)); Prop 2 CONFIRMED; Γ OPEN, pre-flag REF-D (high) | "explicit convex inner set as sign carrier" → NO | Γ: name the minimizer property destroyed by O7 (large k) and O2; precision at scale λ_A |

**State (round 2):** 9 memos, 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. CA_B_005 Prop 2 is not a new structural clause: it is prop:wit-sens (ℓ¹-Lipschitz bottom) read at a certified window; at most a one-line remark. Recurring failure modes: comb-genericity (B″), zero side (R)(4), O8 survival of comb-only properties, and now the pole at s=1 for σ-transports. Note: openness does NOT exclude thin exact properties (a proof of P⇒Q need not cover non-P combs); the operative constraints are lem:transfer (O1–O15) and (B″).


**Round 3b rows**

| candidate | object | verdict | YES→NO moves endorsed | open |
|---|---|---|---|---|
| CA_A_007 | triage: homotopy (withdrawn), boundary triples, cross-place RP | homotopy = retry (N_012/W5); triples = coordinates of thm:parityschur (B″); RP Thm 2 PROVED, comb-generic, EXCLUDED | "RP carries the window sign" → NO (PROVED); index §G triples → covered | §6 index seed: integer invariant = n₋/spectral flow ⇒ first-contact in index language unless a closed loop with Euler×FE flow is named |
| CA_B_008 | concavity gap Γ, two-minimizer angle bound | Thm 1 CONFIRMED (coordinate); Γ EXCLUDED (REF-D tautology, (B″), (R)(5)) | "concavity gap as sign carrier" → NO; "minimizer misalignment" → (R)(5) NO; decomposition family closed | — |

**Erratum (round 3, O-labels).** The campaign brief's list numbered the modifications differently from Paper 46. Paper 46 (l. 8331–8345): O1 finite deletion, O2 amplification Λ+cδ_{n₀}, O3 tail deletion, O4 rescaling, O5 one weight, O6 a_P, O7 quartets, O8 f_t, O9 ζR, O10 Epstein, O11 Beurling, O12 ζ_K, O13 bounded windows, O14 truncation, O15 Poisson. Reviews CA_A_001–004, CA_B_001–005 use the brief's numbering: read their "O7 Beurling"→O11, "O8 quartets"→O7, "O9 f_t"→O8, "O10 ζR"→O9, "O11 Epstein/DH"→O10, "O13 σ-reflection"→structural (not an O), "O14 truncation"→O14. Verdicts unchanged; in particular CA_B_003's exclusion is by O7 (quartets keep the comb exactly, lem:shape-quartet). From round 3 on, Paper 46 labels.

**State (round 3):** 13 memos, 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. Openness (Lemma B / TV-ball) is P46 prop:wit-sens + l. 8348, not a new clause; the "thin properties are excluded by openness" reading is rejected twice. Only live OPEN item: CA_B_007 concavity gap Γ (pre-flag REF-D high).

**State (round 3b):** 15 memos, 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. No OPEN object left with a named separating property; pending seeds: CA_A_007 §6 (index), CA_B_003 residual (inequality using Δ≡0).

| CA_A_008 | integer invariant (spectral flow/Maslov) | COLLAPSE CONFIRMED (REF-D); Lemma 1 PROVED | "integer invariant along path from positive endpoint" → REF-D | — |

**Syntheses (CA_A_SYNTHESIS, CA_B_SYNTHESIS):** reviewed in CA_SYNTHESES_REVIEW.md. All proposed moves ENDORSED with scope notes (norm class only for CA_A_001; self-matching excluded by O7 alone, not (B″)). Front B's (P1)–(P6) endorsed as a checklist (+ archimedean-only reading insufficient). Fronts A and B closed; 16 memos, 0 ADMISSIBLE-CANDIDATE.

**Front C (local–global/adelic)**

| candidate | object | verdict | YES→NO moves endorsed | open |
|---|---|---|---|---|
| CA_C_000 | seed list C1–C6 | screens CONFIRMED; C1 discard correct but for termwise reasons (cor:directbound/lem:shape-misc), not REF-D | — | — |
| CA_C_001 | product formula as divisor-class coupling | NO-GO for declared classes CONFIRMED (Thm 1; 2 cells CONDITIONAL); all cells also fall to O7 (comb classes); (Fam_η) OPEN sub-statement, not a candidate | "PF relaxations (local/global/one-sided/tolerance) carry the sign" → NO | (Fam_η) truth + (Span_η); polar-term pre-flag |
| CA_C_002 | MW-3 classical HM; line-vs-Haar | Prop 1 PROVED (class 𝓗 NO-GO); Prop 2 coordinates, positivity = (S) REF-D | MW-3 OPEN → classical class NO-GO; well-posed reading = (S) | condensed with archimedean input: ARGUED only |
| CA_C_003 | (Fam_η) = T*₃(η) settlement | CONFIRMED necessary-only for η>2/3 (NUMÉRICO input); off-route; μ_M(0.7) check NOT strictly necessary — do not run | — | — |
| CA_C_004 | batch 2 (Nyquist, rationality, Kummer, Iwasawa, FE phase, minimizer local law) | all DISCARDS CONFIRMED; area stop endorsed | "p-adic/Iwasawa/special-value couplings carry the sign" → NO | — |

**State (round 7):** 22 memos reviewed (A 8, B 8, C 5 + seeds), 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. Front D (phase/Hardy) not yet started.
| CA_C_005 | μ_M(η) numerics on the span | data ACCEPTED (NUMÉRICO, all positive); "family is critical" NOT established — μ_M is a lower bound (MAJOR FIX); span criticality only | — | none for D |
| CA_C_006 | batch 3 (Pila–Wilkie, free probability, Ax–Schanuel, Helson, Positivstellensatz, zero-side family identity) | all DISCARDS CONFIRMED; FIX: [crit] premise (span, not family); O5 is not rank one | "o-minimal/Pila–Wilkie" never constructed → NO-GO (ARGUED, semialgebraic); "distributional/free-probability methods decide the bottom" → NO | — |

**Front D (phase/Hardy)**

| candidate | object | verdict | YES→NO moves endorsed | open |
|---|---|---|---|---|
| CA_D_000 | seed list D1–D9 | screens CONFIRMED; none wrongly kept/discarded | — | — |
| CA_D_001 | Hardy-amplitude transfer: (1/π)∫Θ′|F̂|²Z_T² = 2∫_T^∞u|R|² ≥ 2Tρ_F on P_T | Thm 1, 1′, Cor 1.1 CONFIRMED PROVED (re-derived); Thm 1″ PROVED (FE class); EXCLUDED as sign step (O10, O12; (R)(10),(11)); first zero-free Euler×FE×pole positivity of the campaign — TOOL | lead "positive coefficients beyond window" → contributes nothing beyond the Euler gap; CA_B_001 §4 "|ζ|²-weighted sign = zero geometry" → scoped (not general) | O7 applicability ARGUED |
| CA_D_002 | closure of the transferred cone | Thm 2, 2′, Cor 2.1 CONFIRMED PROVED; route NO-GO | "row D by approximation from Hardy-amplitude positivity" → NO-GO (PROVED) | classify admissible amplitudes (§3.6) |

**State (round 8):** 29 memos/seed lists reviewed, 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. Best new tool: CA_D_001 (PROVED); the D-defect is located on {|ζ/Z_{<X}| < 1} (central Nyquist cell + ordinates) — a reading, not a reduction.
| CA_C_007 | η-family: Gram-norm numerics, one-scalar reduction s_M, FE falsifier test | Lemmas 1–2, Prop 3 PROVED; family positivity FE-class generic (O10/O12 survive, NUMÉRICO) ⇒ EXCLUDED as sign step; CA_C_005 premise retracted | "η-family positivity is ζ-specific" → NO (NUMÉRICO); stop numerics on η-family | — |
| CA_D_003 | transfer vs s_w family; amplitude-one residual | CONFIRMED (2 FIXes: constant T₀ not 2T₀; bracket O(1)·c², not log M); residual candidates all DEAD/REF-D | "a ζ-specific amplitude-one statement on {Z_T²<1}" → no surviving candidate | — |
| CA_D_SYNTHESIS | front D close | ENDORSED with the CA_D_003 FIXes | — | — |

**State (round 9):** 32 items reviewed across fronts A–D, 0 ADMISSIBLE-CANDIDATE, no negative value for ζ. PROVED tools of the campaign: CA_D_001 (Hardy-amplitude transfer, FE-generic), CA_D_002 (closure NO-GO), CA_C_001 (product-formula table), CA_C_002 (HM class NO-GO; line-vs-Haar), CA_C_007 (one-scalar reduction), CA_A_007 Thm 2 (RP false), CA_B_003 Thm 1 (Δ≡0 ⟺ FE), CA_B_008 Thm 1 (angle bound). Every sign-step candidate failed by (B″), (R)(4), O7, O10/O12 or REF-D.

**Fronts E/F/G (round 10)**

| candidate | object | verdict | YES→NO moves endorsed | open |
|---|---|---|---|---|
| CA_F_000 + SYNTHESIS | 15 topology/geometry seeds | all DISCARDS CONFIRMED; Lemma F5 FIX (Haynsworth statement; Theorem P mis-cited, signature claim ARGUED) | "condensed MW-3" → NO-GO (ARGUED); Floer/RO(G)/A¹/cluster → covered (REF-D / comb-type) | — |
| CA_G_000/001 + SYNTHESIS | 12 algebra/rep-theory/combinatorics seeds; monoid lemma; SUSY; Elias–Williamson ladder | screens CONFIRMED; G0, G1 PROVED; G1 excludes via (R)(10), not thm:shape(A) (O11 ARGUED, O12 OPEN in P46); EW ladder = REF-D/retry | "monoid-built algebra carries the sign" → NO ((R)(10)); "square/dimension/unitarity positivity" → REF-D/class (D); "EW Hodge theory on the window ladder" → REF-D | — |
| CA_F_001 | condensed/liquid MW-3 | CONFIRMED: Lemmas 1–2, Prop 3 (bare local positivity false at every p), Prop 4 (REF-D) PROVED | "condensed MW-3" → NO-GO (PROVED, three declared classes) | — |
| CA_F_002 | exact trace formulas, horocycle/Heegner periods | NO-GO for declared class CONFIRMED; FIX: multiplicity wording; evenness of tests kills Im tr(M^{−1}M′) | "TF⁺ on arithmetic quotients carries the window sign" → NO | — |
| CA_F_003 | polarized object over ℤ | Lemma 1, Prop 2 (unitary invariants = spectral) PROVED; gap G-F = MW-5 OPEN (object unbuilt) | spectral invariants (Floer, capacities, signatures, degrees, heat) → REF-D (PROVED) | read CC 2609.00299 (low) |
| CA_E_000 | 12 quantum/operator-algebra seeds | screens CONFIRMED; E4/E5 deferred to CA_E_001 (pre-flag: cylinder localization vs dense line; compression ≠ Schur multiplier) | — | CA_E_001 |
| CA_E_001 | commutative collapse (separability), Schur-factorization NO-GO | Lemmas 0–1, Thm 1, Cors 1.1–1.2, Thm 2 CONFIRMED PROVED; EXCLUDED as sign steps (B″, REF-D) | "quantum-information positivity distinguishes anything here" → NO (PROVED); "Schur/GCD/Haagerup/product-state factorization" → NO-GO (PROVED) | off-line Fejér means: falsifier search only, not to run |
| CA_E/F/G_SYNTHESIS | front closes | ENDORSED with scope notes (CA_SYNTHESES_REVIEW.md) | — | — |

**State (round 10):** fronts A–G closed; ≈40 items reviewed; 0 ADMISSIBLE-CANDIDATE; no negative value for ζ. New PROVED tools this round: CA_E_001 Thm 1 (separability: Euler-product tests suffice) and Thm 2 (Schur NO-GO); CA_F_003 Prop 2 (unitary invariants are spectral); CA_F_001 Prop 3 (bare local positivity false at every p); CA_G G0/G1. Only OPEN items: gap G-F (MW-5, object unbuilt); CC 2609.00299 direct read (low).
| CA_H_000 | front H seeds (semiring +/·) | discards CONFIRMED; FIXes: H0(b) ARGUED (x²+5y² has Γ(s), conductor 20); H6 = retry of CA_C_002 Prop 2(d); H1/H5 already excluded by own table (O7/O10/O12) — developed only to record death | — | CA_H_001/002 |
| CA_H_001 | Buium δ, arithmetic Wronskian, δ-log of ζ, Frobenius-lift objects | CONFIRMED NO-GOs (PROVED/CITED); FIX Lemma 4.1(ii) mis-attribution to CA_D_001 Thm 1′ | "δ-structures / Mason–Stothers / global Frobenius lifts carry the sign" → NO (declared classes) | — |
| CA_H_002 | Erdős successor invariant (S⁺); Div = Haar, Near = line − Haar | CONFIRMED; (S⁺) excluded at O7 and asymptotic only; Thm 3.1 = CA_C_002 Prop 2(d) extended to Ĝ (cite); (K) REF-D | "+/· interplay carries the sign" → NO for the pairing anatomy (linear in Λ) | — |

**State (round 11):** fronts A–H; ≈45 items; 0 ADMISSIBLE-CANDIDATE; no negative value for ζ. The campaign's operative wall, confirmed on every front: a ζ-specific property of the comb survives O7 (quartets); a property of the form survives O10/O12 (FE class) or is comb-generic (B″); what remains is REF-D.
| CA_H_SYNTHESIS | front H close | ENDORSED (fixes carried) | four moves endorsed with scope | MW-5 non-graph correspondences OPEN |
| CA_I_000 / CA_J_000 | fronts I (PDE of minimizer), J (correlation inequalities) seeds | screens CONFIRMED; J0/J0′ re-derived (kernel negative at log 2, log 4 for 2T₀ ≤ 0.1 — kernel values, not form values); I1 pre-flag: cone property ⇒ REF-D, O2/O4 survive | — | CA_I_001/002, CA_J_001/002 |
| CA_I_001 | Markov structure, Krein–Rutman, Markov-∀T rigidity, 𝖯⋆ | CONFIRMED: Thm 1, Thm 2 (Markov class NO-GO via O2), Thm 3 (ξE entire ⇒ non-Markov at large T; quartets/O9 separated), Cor 6 separation (REF-D as route); FIX: general-E formula ARGUED | "max principle / Krein–Rutman / comparison forces the sign" → NO (PROVED) | O14 Markov status OPEN |
| CA_I_002 | virial, collar, frequency, Γ-conv, conc.-compactness | CONFIRMED retries/NO-GOs; DH transversality ARGUED; Paper 48 citation internal | virial / boundary layer → NO | — |
| CA_J_001 | lattice RP in prime coordinates, chessboard | CONFIRMED: Thm 1, Thm 2 (RP_p ⟺ lattice support of ν), Cor 3/4, Prop 5 | chessboard / Gaussian domination → NO (PROVED) | — |
| CA_J_002 | GKS frustration; FKG on divisor lattice | CONFIRMED: Thm 1.3 frustration, Prop 2.1/Cor 2.2 (Euler tests = FKG-equality class) | GKS/GHS/FK/FKG → NO | — |
| CA_I/J_SYNTHESIS | fronts close | ENDORSED | as above | — |

**State (round 12):** fronts A–J closed; ≈55 items; 0 ADMISSIBLE-CANDIDATE; no negative value for ζ. Sharpest new result: CA_I_001 Thm 3/Cor 6 — a property set (𝖯⋆) separating ζ from every declared single modification except O14 (open); a separation, not an inequality (REF-D as route).
| CA_K_000 | front K seeds (frustrated quadratic forms) | screens CONFIRMED; pre-flags on K8 (void in t-picture, wrong comparison in integer picture), K6/K7 ((R)(5), [crit]), K10 (linear in Λ) | — | CA_K_001/002 |
| CA_K_001 | diamagnetism, holonomy, signed Laplacian | CONFIRMED: Thm 1.2 (integer diamagnetic bound → −∞), Prop 1.3 (Arch indefinite), Thm 2.2 (constrained order reversed: λ_A(0.7;0) < 0 < λ_A(0.7;Λ)), Props 3.1–3.4, Thm 4.2/Cor 4.3 | diamagnetic / holonomy / signed Cheeger → NO (PROVED) | — |
| CA_K_002 | Guerra interpolation, disorder, heat flow on Ĝ, site independence | CONFIRMED: Thm 1.2 (deterministic path sign = minimizer statement), Prop 2.1, Thm 3.2 (prime-sited tests suffice), Cor 3.3 (Div is a site artifact; Haar endpoint negative) | Guerra/ASS interpolation → NO (PROVED) | — |
| CA_K_SYNTHESIS | front close | ENDORSED | four moves | — |

**State (round 13):** fronts A–K closed; ≈60 items; 0 ADMISSIBLE-CANDIDATE; no negative value for ζ. Useful coordinates gained: CA_K_002 Thm 3.2/Cor 3.3 (on prime-sited tests the target is Arch ≥ Near); CA_I_001 Thm 3/Cor 6 (separation set 𝖯⋆). Process flag: front J's master-grid entry 52 was written outside the campaign folder; check it against the CA_J reviews.
| CA_L_000 | front L seeds (magic functions) | screens CONFIRMED; V1/V2/V3 transfer table endorsed; L5/L6 REF-D risk flagged | — | CA_L_001/002 |
| CA_L_000–002, CA_L_SYNTHESIS | front L: exact magic-function constructions (Viazovska/CE/RV/CKMRV) | L1 NO-GO (thm:O as slackness, PROVED); L2 NO-GO modular-data class (genus pair, lvl 20; Hamburger caveat lvl 1); L5/L6 prime-site torus LP REF-D (attained dual, slackness on Z_s, exact |X|≤5) — awaiting review | "magic function for row D" → NO; "CE gives lower bound" → NO | check of CA_L_002 Thm 2.3 ⇒ (thm:oneprofile) and Thm 2.2 citations |
| CA_L_001 | literal magic function; CE direction; modular-data class | CONFIRMED (thm:O as slackness; Odlyzko direction; level-20 Epstein NO-GO, level 1 reduced) | magic function / modular-data / CE → NO | — |
| CA_L_002 | prime-site LP, torus certificates | CONFIRMED: attained duals, slackness on Z_s, exact for |X| ≤ 5; Thm 2.3 REF-D | site-LP/torus as sign carrier → REF-D | — |
| CA_L_SYNTHESIS | front close | ENDORSED | three moves | — |
| CA_M_000 | front M seeds (prime-sited problem) | screens CONFIRMED; pre-flag: by K-S the target is PD of 𝖡 on ℝ (site-free) ⇒ integrality of shifts expected invisible | — | CA_M_001 |
| CA_M_001 + SYNTHESIS | prime-sited form: Chen shift identity, parity, integrality, reversal | CONFIRMED: parity/residue NO-GO (trace zero); Thm 3.1/Cor 3.2 site arithmetic information-free; Prop 4.1 reversal = exact FE cancellation (= prop:boundary), FE-generic | three moves ENDORSED | — |

**State (round 14):** fronts A–M closed; ≈70 items; 0 ADMISSIBLE-CANDIDATE; no negative value for ζ. Fronts K–M converge: the decisive object is 𝖡 PD on ℝ (site-free); its only +/· content is the comb (positions log n, weights Λ(n)n^{−½}); every site, lattice, torus or interpolation reformulation is REF-D. Process flag repeated: fronts J/K wrote master-grid entries 52–53 and a crossword section outside the campaign folder; verify them against these reviews.
| CA_N_000–003 + SYNTHESIS | front N: build Viazovska's V1–V3 or prove impossibility | V1 built on sites (REF-D), impossible exact+attained on window LP; V2 Tate/lattice + amplitude k≥1 built (FE-generic), Thm N2: unimodular analytic-signal transfer impossible ∀T ≥ ½log3 (PROVED); V3 Tate eigen-structure spent in thm:Z, no self-dual multiplicative lattice (PROVED), no moderate-growth automorphic generator of Λ (PROVED); Thm 5: built toolbox holds for Epstein (O10) ⇒ sign-blind | three moves proposed (pending review) | non-unimodular transfers OPEN |

**Round R (re-examination) + front N**

| candidate | object | verdict | moves | open |
|---|---|---|---|---|
| CA_N_000–003 + SYNTHESIS | Viazovska V1–V3 built/impossible | CONFIRMED; FIX: Thm N2 holds for T > ½log3 (not ≥; at ½log3 the comb is {2}, σ(0) ≈ −6.35 > −6.90); Thm 3 scope = declared candidates; grid part19 / crossword l.720 consistent except threshold | three moves ENDORSED | non-unimodular transfers (expected G0) |
| CA_R1_001 | 𝖯⋆ separation vs inequality | CONFIRMED: jump-measure criterion; O14 CLOSED; REF-D by identification PROVED | 𝖯⋆ as route → REF-D (PROVED) | **D_∃c** (OPEN, weaker-or-equal to D, O4-invariant) |
| CA_R2_001 | D8 amplitude homotopy | CONFIRMED: family zero-free; interpolation NO-GO (method class, PROVED); non-integer support mechanism NO-GO | D8 kill 1L → THM | — |
| CA_R2_002 | SPEC_A (γ) with proved margin | CONFIRMED: (γ) CIRC → ARG + PROVED margin; B8 → REF-D | as proposed | — |
| CA_R3_001 | SPEC_A θ-line, L*_j(θ) | identities CONFIRMED; **"ADMISSIBLE" NOT endorsed → REF-D / OPEN objective**: O1–O6/O8/O10–O12/O15 escapes vacuous (singleton class, H1); O7/O9 escaped by identification (purity), not by exact K (shared by quartets); clause (iii) unenforceable; (R)(11) not applicable | — | R4 attempt at n_j = 7 to be reviewed |
| CA_R4_001 | L*_j(θ) at ½log5 → ½log7 | CONFIRMED; OPEN (no proof, no falsifier); Prop R4.2 PROVED: (Ch) ≡ data at every contact ⇒ H1 is a theorem ⇒ CA_R3_001 is REF-D with no extra mechanism; defeating term = exact evaluation of 𝔄_j^{−1} on the four-atom exterior field (not zero-side, not B′) | "(Ch)/θ-line adds a mechanism beyond the data" → NO (PROVED); 𝒞_θ proof at this contact → ARGUED NO-GO | exterior continuation of EL (pre-flag: EI_001 ⇒ REF-D) |

**State (round R):** ≈80 items; 0 ADMISSIBLE-CANDIDATE (CA_R3_001's "ADMISSIBLE" relabelled REF-D); no negative value for ζ. New OPEN residue: D_∃c (CA_R1_001). Note: the ½log5→½log7 step is already covered by cited Liu Thm B; no first *structural* proof beyond ½log5 exists.
