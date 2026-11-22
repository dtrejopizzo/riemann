# Inventory of phases 168–184 ( → )

Record survey, with no new mathematics and no numerics. Input for updating Paper 48
(`04-papers/48-row-d-route-map/main.tex`, up to date through phase 167: §sec:spec "Six problems and their status",
§sec:walls W1–W12, §subsec:beurling (thm:BFdisc), §subsec:identification (thm:R, thm:ident), §sec:grid (1022 routes),
paragraph "Phases 166–167" with (G), (N′), (WS*)).
Labels copied from the record (PROVED / CITED / CONDITIONAL / OPEN / NO-GO / E1 / ARGUED / WITHDRAWN). Where an
adversarial review changed a label, the final label is given and the review is cited.
Phase 170 (130 files) is inventoried via the README, R170_808 and the audit R184_002 (+ editorial note R184_091).

Paper 48 problems: P1 (Blaschke–torsion, 5C×5E/8B), P2 (difference channel, 6C), P3 (×p, 5H), P4 (global object in T
with Euler before regularizing, 4F/5F), P5 (m<∞ ⟹ m=0, 8F/4E/7E; includes 4D/8D), P6 (discrete Beurling boundary,
5G/8F/8D/4D/7E/4F).

**Row D: OPEN throughout the period. No grid symbol changes (R184_099 §4).**

---

## Phase 168 — never-used inputs

1. **Goal.** Sweep classes of never-used input (R168_001) and test the best-ranked ones against (★_cell)/(WS*).
2. **PROVED.**
   - R168_101 Prop 2.1: Turán/Λ≥0 inequalities at σ₀=1+η do not bind for β ≤ 1−c (quartet advantage (1+O(δ))^k vs η^{−k}); D-H empty at ½+δ.
   - R168_101 Prop 2.2: local count with positive kernel (σ₀−β)/|s−ρ|²; the quartet is visible only at order O(δ²).
   - R168_102 Thm 1: with a multiplicative twist, Type II is a product and reaches the trivial bound (the additive twist does gain).
   - R168_102 Thm 2/3/4: large sieve in γ = measure bound (blind to γ_q); alignment points the wrong way; uniform (U) in γ is RH-strength.
   - R168_103 Lemma 2: a negative quartet forces a node of G near γ*; (★_loc) sufficient for local (★_cell).
   - R168_201 D2-1…D2-6: L_γ=ζ(s+iγ)ζ(s−iγ) has Weil functional W_ζ on a shifted test; degree-2 positivity ⟸ that of ζ (E1); D2-5 (W4 exact, Fejér–Egerváry); D2-6 DH empty outside dlVP.
   - R168_202 Thm 1.1–1.4, 2.2–2.3, Prop 2.4: O-151.4 and Q27 closed with proof (Hilbert–Pólya = summand side; numerator with Beurling inputs ≤ dlVP; E_(∞,T) identifies ζ; comparison positivity = q_T).
   - R168_203 Thm L1 (L=Ξ′²−ΞΞ″=Ξ²Σ(t−t_ρ)^{−2}, quartet Q(u)), Prop L2, L3, L4 (Laguerre L₁≥0 ≠ LP).
3. **NO-GO.** Deuring–Heilbronn (already NG-B3; re-test: W2/M, slack); Baker/Diophantine ("single-height wall"; generic Beurling falsifier, Thm 5 ARGUED); degree 2 (E1 + W4); local Laguerre (equivalence with small-y (★_cell) FALSE; linear sign ⇒ E1; Riccati=Selberg ⇒ verdict E70_12); small-y: "zero-free empty" draft WITHDRAWN.
4. **OPEN.** O168.101.1 (nonlinear identity-level zero law near σ=½, no candidate); O168.102.1 = (U); **(P_gap)** / O168.103.1 (ζ-specific coupling off-line ↔ on-line neighbors at scale 1/log γ; M_m violates it); small-y (★_cell).
5. **Cells / problems.** 7A, 7D (DH), 3E/3F/4F (Diophantine, GAP-157.A), 4G/1G (degree 2), 8C (O-151.4), 1E/7H (Q27), 2C/7B (Laguerre). P5/P6 (WS*); O167.101.2.
6. **New walls/falsifiers.** *Single-height wall* (R168_102: measure / alignment / uniform=RH); "generically perturbed Beurling" falsifier (ARGUED); M_m violates (P_gap) (PROVED); W4 in exact form D2-5.

## Phase 169 — architecture of the input

1. **Goal.** Specify the missing input 𝓘 (R169_000 v2) and audit it (R169_091/102), prove the Eratosthenes induction (R169_101).
2. **PROVED.** R169_091 Prop 3.1 (γ_q is not determined by the window, via R163_901 Thm F); Prop 3.2(a)(b) (structure of Γ_S(F); (c)(d) density (2/π)arctan tanh(T_cδ) PROVED sine-type, ARGUED general); Prop 5.1; **Prop 5.2 (tail of Λ on [X,X²) = Eratosthenes(window))**; Lemma D₀ in the Cramér model (upper bound; "≍" WRONG). R169_101: Lemma 1, Prop 1 (activation identity W_{T′}=W_T⊕…−𝒩), Thm 2 (Schur form, necessary condition (N)), Cor 2′ (the step must be doubly exponential cancellation, W2), Prop 3, 4, 4′ (Mertens), Prop 5 (Eratosthenes ⟺ integers=ℕ; selects ζ). R169_102: the law is already Ψ1 + Thm NB (phase 159).
3. **NO-GO.** Eratosthenes induction: **W2 + single object** (R169_101, coherent with NB); R169_000 §4–5 WRONG as written; reading: 𝓘 at fixed scale = finite window computation (ARGUED) → master quantifier W2/Thm M.
4. **OPEN.** (E_θ), θ<½ ⇒ RH for Beurling systems; Step_{T,Δ} outside certificates; existence of [D] ("Bombieri–Vinogradov at a single frequency selected by the window"); 𝓘 over Γ_S ⟺ RH (OPEN, ARGUED RH-strength); over 𝔈 (ζ_K, Hecke) the law would prove uniform GRH (R169_102).
5. **Cells / problems.** 4F, 5E, 5F (nonlinear integrality in T), 3E; P4, P6.
6. **New.** *Eratosthenes window→tail link* as a datum of ℤ at one scale; "there is no Eratosthenes-determined falsifier in the record" (record + standard).

## Phase 170 — the global inequality over the primes ( → 10-07; R170_000–900)

1. **Goal.** Prove W_T ≥ 0 for all T > ½log5 via constructions on the prime side (prime channels, coherent paths, compensation, archimedean transport, EM/Tate port, virial).
2. **PROVED (tools).** R170_201 operator 𝒟_P with W_T=‖𝒟_PF‖²+R_P, optimal constant budget, R_P non-positive; R170_301 W_T=E_T−C_T (E_T>0); R170_601 minimal non-local cost; **R170_806/808 exact archimedean transport** Arch_T=b−[γ_E+log(2πL)]I−H_L (L=2T); **R170_808 Theorem (A)**: discarding the reserve R_S gives inf W_rel = −∞ for L > L_*≈0.2947 (construction no-go); R170_884–899 exact ledger of the polar port (identities valid for any weight: convolution algebra); R170_888 Hellmann–Feynman + parity wall; R170_890–892 hyperbolic block (1,1) — "KKT signature σΔ" REFUTED; R170_894 §4 independence from the interior datum; R170_900 PC–Tate collision.
3. **NO-GO.** R184_002: the residue (R170-RES) is a signless **equality** [W12] on the contact jet [W5]; as a route to D **NO-GO [W12+W5], E1 closure**; OPEN-empty under RH (emptiness by zero density, correction R184_091). R170_841 VIR–LB: sign of β_Λ FALSE. Three Gates: partial transport accepted, global induction not.
4. **OPEN.** (R170-RES) (empty under RH; needs quantifiers N,M; distinguish (5.3)/(7.2) of R170_899); VIR–LB; covariant cancellation R170_887(5.1); M→∞ limit not justified (R170_899 §7).
5. **Cells / problems.** 4B, 4E, 6B/6C, 4F; P4 (exterior Tate scalar O2302.2), Gate 1.
6. **New.** Theorem (A) of R170_808 (the positive reserve cannot be spent in full); W12+W5 as a diagnostic of the chain; falsifiers (Beurling, κ, M_m) ARGUED without computation (R184_091).

## Phase 171 — discrete Beurling boundary

1. **Goal.** Decide (BF^disc_θ) with a fixed exponent.
2. **PROVED.** **(A) Counterexample P_171**: discrete system, integer multiplicities ≥0, N=cx+O(x^{2/5}) (in fact O(x^{83/208}), 83/208 = 2/5 − 1/1040), with infinitely many zeros at Re s=11/16; deterministic and computable (derandomization via conditional expectations, effectiveness lemma). It is the **λ=3/8 specialization of BFdisc, loss absorbed into 2/5**. Two neutral adversarial audits, no defect found.
3. **NO-GO.** Every route that uses only the class N=cx+O(x^θ), even with integer multiplicities and θ<½ (θ>1/3).
4. **OPEN.** Theorem (B) for θ₀ ≤ 1/3 (O2601.1 sharpened).
5. **Cells / problems.** 5G; P6.
6. **New.** Falsifier **P_171** (integer, fixed exponent 2/5, zeros at 11/16); separation table "uses N" / "uses integrality".

## Phase 172 — P_171 as a probe of D

1. **Goal.** Transport P_171 through the D chain and locate the pieces that fail ([F]) or survive ([V]).
2. **PROVED.** **Dependency classification theorem**: every transport failure falls into {analytic self-duality centered at ½ (FE, Gamma, poles, quartets, explicit formula)} or {exact additive geometry of ℕ (comb, n↦n+1, Poisson–EM, hyperbola, PC–Tate)}; [V] pieces: finite convexity, Schur, abstract Bochner–Kreĭn, Cartwright, Parseval, Landau, abstract Thm M, abstract finZ, Thm R, recentered jets, operator identities.
3. **NO-GO.** Repairs: "FE only" (DH, Epstein, f_χ), "axis only" (recenter at 11/16), "additive lattice = ℕ" (Eratosthenes identification ⇒ eliminates the falsifier). The reading "the only [F] is FE" REFUTED.
4. **OPEN.** **R172-candidate**: liminf_N liminf_M 𝔑_rem(M,N,T;F) ≥ 0 under REG/C1 at first contact (literal residue of R170_900 (1.2)). Minimal-coupling candidate "Euler over ℕ ∧ Poisson/FE over the same lattice": ARGUED. SIGN-REAUDIT §1: R172 does not prove that Euler+FE together suffice.
5. **Cells / problems.** 5G, 4F, 6B; P6, P4; S4/S7/S11 specification.
6. **New.** [V]/[F] dichotomy as a transport filter.

## Phase 173 — construction of the object (0.1)

1. **Goal.** Hermitian form with (Q1)–(Q4) (prespectral positivity + Euler–Poisson coupling + seeing all zeros).
2. **PROVED (maximal theorems).** (a) adelic Schwartz–Bruhat; (b) Jacobi theta with T_{p²} (joint spectral decomposition fiber by fiber); (c) Weil–Connes trichotomy: L²_δ positive but critical zeros only / Meyer–CCM H¹ = Weil (E1) / Connes compressions with forbidden cuts.
3. **NO-GO.** (a), (b), (c) for the families examined; "closing them forever" NO-GO (not a nonexistence theorem).
4. **OPEN.** OT-5′ (object not constructed).
5. **Cells / problems.** 2G, 4H, 5H, 8D; P4; W10.
6. **New.** Trichotomy (c).

## Phase 174 — total exclusion

1. **Goal.** Prove (I) or (II) of the prespectral Euler–Poisson classification.
2. **PROVED.** Construction of H¹_alg and B_Φ in the Tate–Meyer model.
3. **NO-GO.** Three rounds without (I) or (II) PROVED.
4. **OPEN.** **TC-174** (every A_EP-balanced triple (H,π,Ω,Q), minimal in character, with prespectral positivity is Morita-equivalent to the Tate–Meyer module and Q=W(A·,A·)); gaps: Morita universality and A22 synthesis (exhaustiveness = ANALYSIS).
5. **Cells / problems.** 2G, 2H, 4H; P4; W1/W10.
6. **New.** Prespectral filter: P_171 without a compatible additive diagonal; DH without a local Tate tensor product.

## Phase 175 — third coordinate (AKL, Deninger, Borger, CC)

1. **Goal.** Geometric triple (spectral H¹, geometric Q, transfer J, full trace).
2. **PROVED.** OT-3; A1 (group completion of idempotent monoid = 0); A3 (positivity before renormalizing ⇏ finite part); inferred identity over X_E (unpublished by Deninger); H1, H2 (σ_an) for cited carriers.
3. **NO-GO.** A1–A3, B1–B3, C1–C3; OT-1, 2, 4, 5, 5′, 6–12; H3–H5; the six clauses of P47 §28.4. SIGN-REAUDIT §1: not a nonexistence theorem.
4. **OPEN.** Statements A and B pending (conormal complex with archimedean contribution; correspondences in W^*(Spec ℤ)).
5. **Cells / problems.** 2H, 4H, 5H, 8H; W10; P4.
6. **New.** Attribution correction (W^*(Spec ℤ) ≠ Spec Λ; necklace without contact length).

## Phase 176 — Euler–Poisson transversality

1. **Goal.** first contact ⟹ z ∈ Ran P^mult ∩ Ran P^add ⟹ z=0.
2. **PROVED.** Results 1–4: mod N reduction ill-typed; TU lemma fails at N=4 (Λ*1=log vector fixed by the DFT); nontrivial continuous intersection (Sonine); replacing the DFT by real operators does not cancel the defect.
3. **NO-GO.** Two-projection route.
4. **OPEN.** — (the law must act on K_N^ren F − JK_N^ren before separating orientations).
5. **Cells.** 4E, 6B; P4.
6. **New.** Falsifier: the law cannot come from incompatibility of supports or ranges.

## Phase 177 — Euler–Poisson / Petz

1. **Goal.** Hessian of conditional mutual information = Q_{N,L}.
2. **PROVED.** Thm 2.1 (decomposition by divisor fibers; fibers of cardinality 1 give identically zero loss); Cor 3.1 (mismatch before Gamma: atoms log 2, log 3 absent).
3. **NO-GO (PROVED).** Canonical Petz construction.
4. **OPEN.** —
5. **Cells.** 4C/4E, 6B; P4.
6. **New.** Rule: the law cannot condition on the recombined integer n=dk.

## Phase 178 — fermionic interference

1. **Goal.** Connected CAR cumulant / affine Robertson as the source of the sign.
2. **PROVED.** Thm 1 (connected sign obstruction, already with two modes); Cor 2 (**exact dichotomy: connected correlation preserves orientation without sign; full covariance has sign and loses orientation**); Thm 3 (Robertson does not orient the contact).
3. **NO-GO (PROVED).** Both mechanisms; closes the opening of G1_B10_R5.
4. **OPEN.** Arithmetic restriction excluding the anticorrelation ρ_−.
5. **Cells.** 2C, 4C, 6C; P4. Killer F2.
6. **New.** Orientation/sign dichotomy (two-mode falsifier).

## Phase 179 — chain gate of the common radical

1. **Goal.** Exterior Tate port as the boundary of an arithmetic–Poisson complex.
2. **PROVED.** Thm 1 (chain-gate identity, obstruction d_C L_1 − L_0 d_P); Prop 2 (nilpotency gives no free sign); Thm 3 (order-2 cocycles are coboundaries: affine swap cohomologically trivial); CG1+CG2 ⟹ β_phys=0.
3. **NO-GO.** Naive total complex.
4. **OPEN.** Prespectral construction of L_0, L_1 with CG1–CG2; R_L F=0 / VIR-LB.
5. **Cells.** 4E, 1H, 6B; P4; W12.

## Phase 180 — Kadison equality

1. **Goal.** Kadison equality (multiplicative domain) as a first-contact mechanism.
2. **PROVED.** Thm 1 (Kadison defect as a sum of pairwise squares); multiplicative domain of the random-unitary channel; log-translation realization (automatic equality, vacuous); affine realization (excludes faithful V_p).
3. **NO-GO.** Kadison ⟹ R_L F=0. "First contact forces equality": NOT PROVED.
4. **OPEN.** —
5. **Cells.** 4E, 6B; P4.

## Phase 181 — complex polarization

1. **Goal.** Complex square preserving the oriented commutator.
2. **PROVED.** Exact oriented prime current; Thm 1 (support obstruction: B_c² contains the comb of rational-quotient collisions).
3. **NO-GO.** Closure via complex square; "Λ*1=log cancels quotient fibers" FALSE; Schur/Clifford/CP repairs not new (FALSE).
4. **OPEN.** —
5. **Cells.** 4C, 6B; P4.
6. **New.** Quotient comb as a structural falsifier of every positive square.

## Phase 182 — rectangular tunnel

1. **Goal.** Gram fusion (sign) + affine logarithmic channel (orientation).
2. **PROVED.** Thm 1 (rectangular tunnel lemma: null corner forces R_L F=0; already in R170_862); Thm 2 (factoring a posteriori via H^{1/2} is circular); R182_201 Thm 1/Cor 1.1 (**the remaining coherent channel has infinite rank, Tate removes only two modes**); joint Chebyshev–Gamma column (CITED D.244–247).
3. **NO-GO.** Local fiberwise Euler–Poisson isometry (EPG).
4. **OPEN.** **NGF**: non-local source factor / non-local joint square before the pseudoinverse.
5. **Cells.** 4B, 4E, 6B; P4.

## Phase 183 — Connes–Consani semilocal sufficiency (R183_001–033, 2026-10-10/11)

1. **Goal.** Formalize CC's Conjecture 4.1 (1910.14368) and the Sonin route (2006.13771) and decide whether it gives D.
2. **PROVED.** R183_001 Thm 1 (rough gap m∈M_S, m>1 ⟹ log m ≥ 2T) and **formalized sufficiency ∀q ⟺ row D**; Thm 183.R (return sufficiency); R183_014 Thm 1–2 (restored trace limit, scope of the cancellation); R183_015 (trace class in the module sector); R183_016 (operator order undefined for every smooth test); R183_006–010 (gcd fibers, positive Gram, tangent pairing log p/(p+1) = D.244 coordinate x_p); R183_008 (infinite-rank white-light residue); **R183_018/019 identity E_S = Son + R_{S,T}** and **NO-GO whole Sonin: n₋(R_{S,T})=∞ for T>½log2** (two proofs, R183_020); **R183_023 relative bound 0, index N(η,T) ≲ 4T e^{2A/η}**; spectrum of B₂ = {0, ±log2/√2}; ε is not of positive type; CC index lives in the ξ metric; R183_025 Thm 2 two-edge model; **R183_029 scaling law (Λ)** and identity Son_S − Son_∞ = prime term + ∫c_hε′_p + ∫|φ|²r_p; R183_030 gap of the full form up to ½log5 (given P46 thm:log5A); **R183_031 Thm 1 gap requirement** (under RH: every positive part with bounded inertia remainder ∀T has limit density on the zeros).
3. **NO-GO.** Raw Gram (R183_008); operator order (R183_016); whole Sonin η=0; frequency multiplier (R183_022, Thm 3.3 → CONDITIONAL(RH)); prolate route (R183_031, structural); (L-Son) uniform η FALSE (CONDITIONAL(RH)); no aligned direction exists ∀T (R183_030 §7). WITHDRAWN: R183_004 (Poisson–Möbius factorization), R183_011 (3.2), R183_002 Cor 1.1 (later restored under trace class by R183_014), general exclusions of R183_013.
4. **OPEN.** **(M)** microlocal (⟹ R′_S Hilbert–Schmidt); (E′_loc); **N_T** (semilocal remainder inertia); λ₁(ker ℓ)=λ₂(prim) (resolved in R184_003); RET, BRO, NGF-type; sign (4.5) of the relative determinant.
5. **Cells / problems.** 8D (CC's Sonin count N(T), already in P5), 4D, 2E, 1B (global Sonin); P5.
6. **New.** "**Archimedean window**" wall: the CC mechanism only works for T ≤ 0.80 (uncertified numerics: #{λ(K_{I_T})>1} ≈ 4T−2); gap requirement (the positive part must know the zeros ⇒ reformulation of D).

## Phase 184 — boundary and live residues (R184_001–015, 091–093, 099; )

1. **Goal.** Attack every live residue of the grid, with adversarial review.
2. **PROVED.**
   - R184_001 Prop 2.1 (O(1) collocation at the prime level preserves the zeros of the target: ζ_P=ζ₀ exp G̃), Prop 2.2 (N_P=cx+O(x^θ) ⟺ polynomial growth, PROVED-standard after R184_091); rigidity with θ₀>0 ⟹ RH.
   - R184_003 Thm A.1 (reflection symmetry), Cor A.2 (μ₁=min(λ₁⁻,μ₁⁺); criterion λ₁(ker ℓ)=λ₂(prim) via parity); Lemma B.1. "T₂ = odd crossing" downgraded to CONDITIONAL (R184_091).
   - R184_004 Lemma 1 (quartet = signature (2,2), ∀T>0), Prop 2 (N monotone, N ≤ 2m), Lemma 3 (Haynsworth), **Thm 4 (M_m chain = ζ chain + rank ≤ 6m)**, **Cor 5 (inertia NO-GO for C_B; valid 𝒜 ⟹ κ(ζ)=∞)**, literal class.
   - R184_005 L1 (trimmed), L2 (O(1) ⟹ #Q ≤ #T), L3, N2, Prop 4.1 (C1 at O(log x) and O(x^ε) FALSE, ζ-modification counterexample).
   - R184_006 Thm 1/1′/Cor 2 (**single-quartet detection law**: T*(a,γ)=max{1+1/a,(1/2a)log(C_ψL(γ))} under Max–Iso; PROVED conditional on rewriting the absorption, R184_092); empty for T ≤ ½log5.
   - R184_007 Lemma 1.1, **Theorem W** (convexity in weights), Cor W′; interior of ζ PROVED via Lipschitz.
   - R184_008 **Lemma AC** (generalized Euler with multiplicities ≥0, no zeros at Re s > θ_Q) and **Theorem F** (multiplicative rigidity, Landau; "Lemma" per R184_092); division variant §2.3; Prop M (linear model).
   - R184_010 **Theorem D** (error diffusion with dither: sup|T₁| ≪ x^{(1−2a)/4}(log x)^{1/2}); Cor 1; Cor 2 only in narrow form (R184_093).
   - R184_011 Prop 3.1 (Q_mg true if RH false), Thm 3.2 (Q_mg ⟺ (Q*) under RH), Thm 3.3 (analogue of (Q*) false in Type I), Cor 3.4.
   - R184_012 Lemma 1 (Loewner monotonicity of 𝔊^{AB}_T), Lemma 2 (left continuity of 𝔤̃_par; justification corrected R184_093).
   - R184_013 log R linear in ε; dither ⇒ N=cx+O(x^{(1−θ)/2+ε}); loss of cancellation on ((1−θ)/3,(1−θ)/2); exponential method does not go below (1−θ)/2.
   - R184_014 **Errata A1–A6** (order-k chaos: Var ≍ X^{1−2a}(log log X)^{k−1}/((k−1)! log X); Witt level k contributes x^{(1−θ)/(2k)} if θ<1/(2k+1)); Prop B.3 / Cor B.3′ (counterexample in the relaxed class R=L(u,χ): every proof of L*_comp must use ε_p ≡ −p^a mod 1); Thm B.4 (under (ZF_R)).
   - R184_015 Prop 1 (P_src(ζ) ⟹ RH), **Theorem 2 (source/form disjunction)**, **Cor 3 (stronger form of W11)**.
3. **NO-GO.** R184_002 phase 170 [W12+W5, E1]; R184_003 "constant = eigenvector" and "exact rank-one correction"; R184_004 C_B via inertia; R184_005 N2 (Diophantine route); R184_007 log 3 needle as a lever (blind to W4/W11); **R184_008 factor route ∀θ<1**; **R184_010 linear L* FALSE**; R184_011 multigenerator as a route; R184_013 dither does not diffuse composites (O184.010a NEGATIVE); R184_009 no entry from the 2026 literature survives; R184_015 candidate "norm of the Sonin remainder".
4. **OPEN.** Q (θ<1/3, discrete, zero β>½) = O184.001a/c; **L*_comp (O184.093a)**, CONDITIONAL on (ZF_R) (R184_014); **C1(O(1))**, C1′, O(x^ε) with ε<½; O166.701.1 (Hilberdink 2012 not in the corpus); **(M_w)**; even v₁ without nodes; **(Q*)**; optimality of T*; division variant P=B∖Q; Bessel/large sieve up to Y^{1/2−ε} (sharp exponent of Thm D); O184.015a/b; C_B.
5. **Cells / problems.** 5G (P6: 001, 005, 008, 010, 013, 014); 8F/4E/7E (P5: 004); 7A/7D (006); 3A/W2 (007); 6F (011); 2E, 3D (012); 4F/8D (003, 015).
6. **New.** Lemma AC / Theorem F; Theorem D (dither); order-2 chaos errata; necessary integrality (Cor B.3′); source/form disjunction (W11′); single-quartet detection (quantifies E1).

## Meta files

- **SIGN-REAUDIT.** PROVED: B(s)=Σβ(n)n^{−s} ≥ ¼ζ(s)Σ_p(log p)²p^s/(p^s−1)² > 0 for s ≥ 2, with β(n)=2Σ_{d|n}Λ(d)log d − log²n (B=ζ(g−f²), Cauchy–Schwarz); (2) positivity over the Laplace cone; (3) lim 2^s Re B(s+iπ/log2) = −(log2)² < 0. PROVED: no Grönwall q′₁ ≥ −Cq₁ for dilation transport on ½log2<T<½log3. NO-GO: (1)/(2) as a sign of D; propagation over the whole domain; bispectrum, fourth moment, independence of rational translations (universal). Scope of exclusions: R158_003 A10, R170_841 §6.1, R172, R175 are not nonexistence theorems.
- **SUPPORT-DESCENT-TEST.** PROVED: no-descent theorem (𝔞_{T′}(G,G)=𝔞_{T_*}(EG,EG) ≥ 0 ∀T′<T_*); global equivalence (descent ⟺ D); dark state (3); collar coupling lemma. NO-GO: support descent as a weaker lemma. OPEN (gate reformulation): (4) K_F(2m+½)=0 ∀m ≥ 1, i.e. holomorphy of ζ(s)W⁰_ε(s) at the positive odd integers (residue ζ(2m+1)K_F(2m+½)). Cells 4D/4E; P4/P5.

---

## Consolidated table

### A. Reusable PROVED tools

| tool | file | use |
|---|---|---|
| P_171: N=cx+O(x^{83/208}), zeros at 11/16, integer and computable | R171_FINAL | class falsifier, 2/5 specialization of BFdisc |
| [V]/[F] dependency classification | R172_FINAL | transport filter |
| Prop 5.2 / Prop 5: tail = Eratosthenes(window); Eratosthenes ⟺ ℕ | R169_091, R169_101 | identification at one scale |
| Activation identity and Schur form of the step T→T+Δ | R169_101 | induction in T |
| Exact archimedean transport; reserve Theorem (A) | R170_806/808 | construction in the window |
| Exact ledger of the polar port (valid for any weight) | R170_884–899, R184_002 | — |
| Connected/covariance dichotomy; support obstruction (quotient comb); Petz fibers | R178, R181, R177 | mechanism test |
| Infinite rank of the coherent channel | R182_201 | — |
| E_S = Son + R_{S,T}; relative bound 0, finite index with η>0; law (Λ); gap requirement | R183_018/023/029/031 | semilocal route |
| No-descent theorem; collar coupling lemma | SUPPORT-DESCENT | first contact |
| β(n) Laplace inequality (s ≥ 2) | SIGN-REAUDIT | absolute region only |
| Prop 2.1/2.2 (collocation, Perron) | R184_001 | Beurling boundary |
| Lemma AC, Theorem F | R184_008 | multiplicative rigidity ∀θ<1 |
| Theorem D (dither) | R184_010 | roundings |
| Errata A1–A6, Cor B.3′ | R184_014 | chaos/level accounting |
| Thm 4 / Cor 5 (M_m chain) | R184_004 | inertia blindness |
| Single-quartet detection T*(a,γ) | R184_006 | quantified E1 direction |
| Theorem W (convexity in weights) | R184_007 | certificates |
| L1–L3 (θ=0) | R184_005 | Beurling rigidity |
| Lemma 1–2 (Loewner, continuity) | R184_012 | prop:polarcap in T |
| Theorem 2 / Cor 3 (source/form) | R184_015 | discard criterion |

### B. New walls (or new forms)

| wall | short statement | file |
|---|---|---|
| Single height | Diophantine input = measure (blind) / alignment (wrong direction) / uniform (= RH) | R168_102 |
| Master quantifier W2 over Eratosthenes | at fixed scale 𝓘 is a finite computation; the infinite is ∀T (ARGUED) | R169_000 v2 |
| W12+W5 on the contact jet | the PC–Tate–EM chain is a signless equality | R184_002 |
| Self-duality / additive geometry dichotomy | every [F] falls into one of the two | R172 |
| Orientation vs sign | connected orients without sign, covariance signs without orienting | R178 (+R180, R181) |
| CC archimedean window (T ≲ 0.80) and gap requirement | the positive part must know the zeros | R183_026/028/031/033 |
| **W11′ source/form disjunction** | every norm bound on the Sonin remainder is blind to M_m (source) or E1 (form) | R184_015 Cor 3 |
| Necessary integrality below 1/3 | without ε_p ≡ −p^a mod 1 there is a counterexample (R=L(u,χ)) | R184_014 B3′ |
| Dead factor route ∀θ<1 | Lemma AC + Theorem F (Landau) | R184_008 |
| (W-sieve, (N′): already in Paper 48 via phases 166–167; reappear as killers in R168_102, R184_009) | — | — |

### C. New falsifiers

| falsifier | kills | file |
|---|---|---|
| P_171 (2/5, 11/16) | class routes N=cx+O(x^θ), θ>1/3, even integer ones | R171 |
| Generically perturbed Beurling (ARGUED) | Diophantine/equidistribution inputs | R168_102 Thm 5 |
| M_m against (P_gap) | small-y regime | R168_103 |
| Moving counterexample σΔ in ℝ² | "KKT signature σΔ" | R170_892 |
| Relaxation W_rel → −∞ | spending the whole reserve | R170_808 |
| Two fermionic modes | CAR cumulant | R178 |
| DFT at N=4 | two projections | R176 |
| Fibers of cardinality 1 (2, 3) | Petz | R177 |
| Bump pairs at distance log 2 / Toeplitz symbol | whole Sonin | R183_018/019 |
| Low band (−γ₁,γ₁) (CONDITIONAL RH) | (L-Son) uniform η | R183_027 |
| ζ modifications with zeros at Re s=0 | C1 at O(log x) | R184_005 |
| R = L(u,χ) in the relaxed class | L*_comp without integrality | R184_014 |
| Dither (Theorem D) | linear L* | R184_010 |
| Type I curve | (Q*) uniform over the field | R184_011 |
| Scalar model q_T=(T_*−T)|x|² | support descent | SUPPORT-DESCENT |
| t₀=π/log2 | β(n) positivity under modulation | SIGN-REAUDIT |

### D. Live residues after phase 184

| id | statement | last file |
|---|---|---|
| Q = O184.001a/c (P6, θ₀ ≤ 1/3) | discrete, θ<1/3, a zero with β>½? | R184_013 / R184_014 |
| L*_comp = O184.093a | lower bound for every rounding; CONDITIONAL on (ZF_R) | R184_014 |
| C1(O(1)), C1′; O(x^ε), ε<½; O166.701.1 | θ=0 rigidity | R184_005 |
| Division variant P=B∖Q | — | R184_008 |
| Bessel/large sieve up to Y^{1/2−ε} | sharp exponent of Thm D | R184_010 |
| (M_w) / (M) | compact semilocal remainder (signless) | R184_003 |
| (Q*) | no B≠0 real Dirichlet with Re B ≤ Re ξ′/ξ exists (under RH) | R184_011 |
| O184.015a/b | structure of Son_S; non-norm properties | R184_015 |
| C_B (P5) | m<∞ ⟹ m=0 | R184_004 |
| optimality of T*(a,γ) | — | R184_006 |
| N_T, (E′_loc), RET, BRO | CC semilocal route | R183_033 / R183_028 |
| R172-candidate | liminf 𝔑_rem ≥ 0 | R172_FINAL |
| (R170-RES), VIR–LB, cancellation R170_887(5.1) | OPEN-empty under RH | R184_002 / R184_091 |
| NGF | non-local joint square | R182_201 |
| L_0, L_1 with CG1–CG2 | chain gate | R179 |
| anti-ρ_− restriction | — | R178 |
| TC-174; OT-5′; statements A/B of R175 | global object | R174 / R173 / R175 |
| (E_θ); Step_{T,Δ}; [D] | Eratosthenes | R169_101 / R169_091 |
| (P_gap) / O168.103.1; O168.101.1; O168.102.1 (U) | small-y, zero law, uniform | R168_103 / 101 / 102 |
| (4)/(5) of SUPPORT-DESCENT | absence of an interior dark state | SUPPORT-DESCENT-TEST |
| (★_cell), row D | — | R184_099 |

### E. Corrections to the record (for Paper 48 and the grid)

1. **prop:polarcap (2E)**: already closed by R160_M4_R1 (L1, A, B) and R162_703; grid §6 item 59 obsolete (R184_012, verified R184_093). Add Lemmas 1–2 of R184_012.
2. **LP-152**: closed by R160_M5_R1 (Cor 2.4), DEAD [F3: DH, Epstein, Ξ_a]; G2_B7_R5 → (L-184.011), NO-GO as a route (R184_011).
3. **(P153.4)** log 3 needle: closed by R153_010; relaunched by editorial error (R184_007).
4. **Errata R164_201 §1 (l.~33–38) and R184_001 item 1, §1.1, §1.3 row 1**: order-≥2 chaos and Witt levels k≥2 are not O(x^{θ+ε}) for every a>0; level k contributes x^{(1−θ)/(2k)} if θ<1/(2k+1). The (1−θ)/2 exponent of the random method and Theorem L **do not change** (R184_093 §1.6, R184_014 A1–A6).
5. I11, I14, Cayley-69: "no statement"; R161_073–074: E1 (certificate, not mechanism).
6. R184_010 Cor 3 / row 7: O184.001a is **reduced to O184.010a** (complete system), not "not reopened because (1+θ)/4>θ" (R184_093).
7. R184_002: emptiness under RH by zero density, not by strict λ_T>0 (R184_091).
8. R184_006 "applies to M_m" → ARGUED; R184_005 L1 trim the sentence about Re s=0 (R184_092).
9. R169_101 §6 "every θ<½ open" obsolete after BFdisc (R171 §1).
10. R183: R183_004 and R183_011(3.2) WITHDRAWN; Cor 1.1 of R183_002 restored under trace class (R183_014); Bochner reading of ε withdrawn; "single theorem ⟺ RH" of R183_031 downgraded to "⟹ finite index".
11. R168_203: Thm 1 of phase 28 ("positive pair ⇒ convex") incomplete as it stands.
12. Paper 48 thm:BFdisc: add the deterministic specialization with fixed exponent 2/5 (R171), and the P6 text "(θ₀ ≤ 1/3) OPEN" with Lemma AC/Theorem F, Theorem D and the errata.

### F. Count (items labeled in this inventory, by phase)

PROVED ≈ 150 statements (168: 15; 169: 14; 170: 10 blocks; 171: 1; 172: 1 + 15 [V] rows; 173: 3; 174: 1; 175: 5; 176: 4; 177: 2; 178: 3; 179: 4; 180: 4; 181: 2; 182: 4; 183: ~25; 184: ~45; meta: 7).
NO-GO ≈ 60 (including the 17 OT/H/clauses of R175 counted as one).
Live OPEN: 24 rows of table D (≈ 40 individual statements).
