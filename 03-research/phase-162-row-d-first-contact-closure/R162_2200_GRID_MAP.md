# R162_2200 — Grid-paper map of row D (audit)

Read-only. No sign is claimed. Gate 1 remains OPEN. Machine-readable version: `R162_2200_grid.json`.
Sources read: phase 162 README, R162_590, notes R162_001–2190 (header, verdict, falsifiers) and audits
790/791/990/1190/1390/1590/1890/2090/2190; R160_020 §6–7, R160_002, R160_S4.

Killer keys: **F1** λ=0 not used (holds on eigenvectors λ>0) · **F2** orientation / square of (PC) · **F3** passes a
falsifier (which one is indicated: DH, deletion/κ, Λχ₂, Beurling, sΛ) · **F4** linear limit (PC-ren) · **M** Theorem M (margin
≤ exp(−exp((2−ε)T))) · **E1** reformulation of RH.
States: ■ PAINTED (dead) · ◧ PARTIAL (open residue) · □ EMPTY (never attempted).

## 0. Corrections to R162_590

1. **§2 is out of date: five "untried" routes were actually run in 162.** Item 1 (signed bilinear) → R162_502 Part B
   (PARTIAL→NO-GO). Item 2 (D3) → R162_703 (λ_W>0 certified on (0,½log5]; Type II exclusion NO-GO by F3 deletion).
   Item 3 (D5) → R162_504 (NO-GO for the sign). Item 5 (×p) → R162_1001 (NO-GO; Pila–Wilkie/model theory remains).
   Item 6 (Laumon) → R162_1203 (NO-GO). Item 7 (Beurling blindness test) was applied in 1001, 1301, 1302, 1401, 1402.
2. **Structure:** rows 165–190 (R162_502…1902) are appended after §4, outside table §1c.
3. **Missing rows:** 001/190 (continuity), 501 (only cited within row 901), 502 Part B, 503, 504, 1501, 1601, 1701, 1801,
   1802, 1803, 1901, 2001, 2101, 2190. That is, the entire R-C (Type I) line from rounds 15–21 is missing from the map.
4. **Killers corrected by audits, that the table still cites uncorrected:**
   - 1402 "finitely many moments cannot bound (Thm 5)": Thm 5 **WRONG** per 1590 (for j≤−2 the sup is bounded; only j≤2 survives, almost trivial).
   - 1203 "Thm W rationality wall": relabeled **REMARK/HEURISTIC** (1390).
   - 1202 "flatness (Thm A)": the headline only holds on large circles (1390); also Π∘1_I in Thm A(d)/D.
   - 1001 "separates Λχ₂/Beurling": the prime table that fails was **WRONG** (1190). Correction: Λχ₂ fails (3.1) at every p with χ(p)≠1; Beurling only if 𝒩_B⊄ℤ. The separation at the object level survives.
   - 903 "Λχ₂, Beurling pass all": the reading of Λχ₂ is **WRONG** (1190). Λχ₂ violates the "Z has coefficients 1" clause.
   - 1101: Thm 4.1(b) **WRONG**; the "mass 1/d" reading of Thm 2.2 is corrected (1390) and 1202 Prop H corrects where the atom lands.
   - 1602 "universal": the two-restriction count of §3 becomes **HEURISTIC** (1890). K1 and K3 are fine.
   - 703: Prop 4.1 (type = spectrum) only holds as ⟹ (990). 802: the label "RH ⟺ two monotone limits" was **WITHDRAWN** (990).
   - 1004: Thm 3.1 had the quantifier wrong (fixed with Y=X^d); Prop 3.2 becomes REMARK (1190). 801: "not increasing in each a(n)" **WRONG**; the concavity is fine (990).
   - 1802 Prop 4.2 becomes PARTIAL (2090). 1901 §3(iv) (double zero) **WRONG** (2090). 1502 Thm 6 becomes "NO-GO for the argument class" (1890).
   - No audit reversed a NO-GO verdict.
5. **Duplicates:** Selberg appears in 501, 901 and 1003 (sieve); Beurling T3 appears in §1a and in §2.7; Hecke appears in §1b, in §3(H) and in 502A.
6. **Omissions from R160_020:** Option 6 is missing (Meyer's mixed S+D class), which was never run and which D2 considers sterile.
   O-D4.2's residue is also missing.

## 1. The grid (summary; cell-by-cell detail is below and in the JSON)

| row \ col | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| 1 identity/functional equation | ■ arcs I-II / phase 120; Li/Keiper, Nyman–Beurling, KEP, κ=0;  | ■ 305; 402; 204 | ■ 1003 | ■ 1301 | ■ 1802; 902 | □  | □  | ■ 1002; 1203; R160_C8 |
| 2 positivity/support | ■ arcs I,VIII; phase 155 prop:archneg; 1603 | ■ 101; 103; 405 | ■ R161_027-029 | ■ 504; 702; 1601 | ■ 802; 1402 | □  | ■ Paper 46 T5 (phases 141-149); phase 150 T3 | ■ Paper 46 (tropical/Künneth) |
| 3 quantitative estimate | ■ arcs I,X; phase 151 dlVP; phase 154 Paper 47 | ■ 001/190; 407 rate | ◧ R160_M7; 502 Part B | ■ 1402 Thm 5; 1502 | ■ 159 G2 | □  | ■ 1004 | ■ phase 152 |
| 4 multiplicativity/Euler product | ■ R161_001-004; 203; phase 153 Thm A | ■ 201/202; 301; 503 | ■ R160_M8; 502 B2; 207 | ■ R152_002; 159 G1 K3 | □  | □  | ■ 1102; arcs III,VIII; 144-149 | ■ 159 G1; 1302 |
| 5 integrality of ℤ | ■ 1902; 801 | ■ 701; 1101 | ◧ 903 | □  | ◧ 1802 O1802.3; 1902 | □  | □  | ◧ 1001; R160_M12 |
| 6 exact values of Λ | ◧ R160_D4 Thm 5.1; D4 Cor 5.2; 406 | ■ 1401; 1502; 403 | ◧ 501; 901 | ■ 702 residue; 1603 | ■ 802 | □  | □  | □  |
| 7 zero side/explicit formula | ■ Paper 47 Thm Z / finZ; phase 155 r5 | ■ 1501 | □  | ◧ 2101; 2190 | ■ 1802 Thm R; 902 | ■ 803 | ■ phase 149 | ■ arcs III-V,X; 158 |
| 8 no arithmetic | ■ arc II; phase 120-121 | ■ 408; P124_004-010; R161_016 | ■ 1202 | ■ 1602; 1701; 1801 | ■ arcs I,IV; 159 G2 | □  | □  | ◧ 159 G1; R160_C1; R160_C3/D2 |
Count: **41 PAINTED, 8 PARTIAL, 15 EMPTY** (64 cells).

## 2. Cells in detail

**1A** (identity/functional equation × quadratic form of a window) — PAINTED
- arcs I-II / phase 120: EQUIV [E1] Kreĭn E*JE, de Branges, canonical systems, global square A*A
- Li/Keiper, Nyman–Beurling, KEP, κ=0: EQUIV [E1] Li kernel at the polar boundary δ=0 (D4 Thm 4.2)
- R162_206: NO-GO [F4] (PC+) algebraic difference zero with (PC−)
- R162_2101: STRUCTURE [M] for s₂=1, T<½log3 the window form IS the full form of ζ

**1B** (identity/functional equation × first-contact kernel vector (linear in F)) — PAINTED
- R162_305: NO-GO [trivial-zero cancellation] exterior Ward: derivative = algebraic zero; δD only via ζ(−2j)=0
- R162_402: NO-GO [F1] reflection dictionary proved; Hardy mechanism dead
- R162_204: NO-GO [F3 (finmod)] regularized jet invariant under every finite modification
- R162_1201: NO-GO [E1,F1,F2,F3] Sonin range: (S_m) ⟺ HF=0, Müntz all-or-nothing
- R161_008-011,017-018,022-023: NO-GO [F4 / open (4.2)] product-Hardy ports collapse to (4.2); tautological linear completions
- *Residue:* (4.2) global Sonin range = the E1 sink of the whole B/C column

**1C** (identity/functional equation × quadratic/higher functionals of F) — PAINTED
- R162_1003: NO-GO [E1,F3] Thm S channels=4(Re D)²; Thm R resums to Σ_ρ (⟺RH); Selberg sieve impossible; holds for DH

**1D** (identity/functional equation × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R162_1301: NO-GO [F3,E1] Robin strings (new Thm 1); isotropy=Gate 1; DH still CM

**1E** (identity/functional equation × flow/family in T) — PAINTED
- R162_1802: EQUIV/PARTIAL [E1] Thm R: RH ⟺ residue window nonempty ∀T; Prop 4.2 relabeled PARTIAL (2090)
- R162_902: NO-GO [E1,F3,DH] Conj 6.1 ⟺ RH; unconditional half already in R160_M4
- *Residue:* nonnegative width of the window moved to integrality (see 5E)

**1F** (identity/functional equation × global transforms in T) — EMPTY
- *Residue:* global transform in T of the FE that does not go through ξ′/ξ (803 lands in Herglotz, see 7F)

**1G** (identity/functional equation × families of L-functions/fields) — EMPTY
- *Residue:* converse/Hamburger theorems as a family sign mechanism (Hamburger used only as a dictionary in 1203)

**1H** (identity/functional equation × geometric/dynamical objects) — PAINTED
- R162_1002: NO-GO [E1,F2] quasicrystal: rigidity presupposes real zeros; one-member class; no local uniqueness
- R162_1203: NO-GO [F1-F4,E1] Laumon ε: L4–L6 missing; Thm W is REMARK (1390); ε-data = scalar C₀
- R160_C8: NO-GO [F3 (Λχ₂,Ξ_a)] ε-phase: Thm 1 literal for falsifiers

**2A** (positivity/support (Λ≥0, supp prime powers) × quadratic form of a window) — PAINTED
- arcs I,VIII: NO-GO [Φ combs,E1] place-by-place/prime-by-prime positivity, finite S
- phase 155 prop:archneg: NO-GO [—] archimedean indefinite from T≈0.58
- R162_1603: NO-GO [F2,F3,E1] positivity lock Thm P; = Gate 1 in coherent class
- phase 156: NO-GO [Φ combs] per-window converse: 2×2 polar-capacity condition fails on combs

**2B** (positivity/support (Λ≥0, supp prime powers) × first-contact kernel vector (linear in F)) — PAINTED
- R162_101: NO-GO [F1] first variation zero
- R162_103: NO-GO [F3 (κ)] a^κ have genuine first contacts
- R162_405: NO-GO [F1] right minimality = monotonicity
- R162_407: NO-GO [F3 (DH)] (LB) ⟺ 𝒱≤0 on N; blind to weight
- R162_703: NO-GO [F3 (deletion)] Type II not excludable; Prop 4.1 only ⟹ (990)

**2C** (positivity/support (Λ≥0, supp prime powers) × quadratic/higher functionals of F) — PAINTED
- R161_027-029: NO-GO [F2] raw prime contacts: indefinite cross terms

**2D** (positivity/support (Λ≥0, supp prime powers) × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R162_504: NO-GO [F3 (DH line v_n≥0)] Perron–Frobenius, parity ladder, Type I/II dichotomy
- R162_702: NO-GO [F3 (κ),M] class 𝒞={a≥0,supp PP} contains κ-models with contact
- R162_1601: UNCERTIFIED [F3 (deletion)] S=2 also for deletion (Type II)
- R162_1803: UNCERTIFIED [F3 (sΛ)] (C2) false with comb; sign ⟨u₂,φ̂⟩ changes across the sΛ family

**2E** (positivity/support (Λ≥0, supp prime powers) × flow/family in T) — PAINTED
- R162_802: NO-GO [F3,M,F4] monotone laws hold for κ/finmod/DH; 'RH ⟺ two limits' WITHDRAWN (990)
- R162_1402: PARTIAL+NO-GO [F3,E1] Q_m monotone, collar law; all transfer to DH/deletion/Beurling

**2F** (positivity/support (Λ≥0, supp prime powers) × global transforms in T) — EMPTY
- *Residue:* full monotonicity/Bernstein property of λ_A(T) or of its transform as a global object

**2G** (positivity/support (Λ≥0, supp prime powers) × families of L-functions/fields) — PAINTED
- Paper 46 T5 (phases 141-149): NO-GO [T5] nonnegative family
- phase 150 T3: CONDITIONAL [Beurling] Beurling gate

**2H** (positivity/support (Λ≥0, supp prime powers) × geometric/dynamical objects) — PAINTED
- Paper 46 (tropical/Künneth): NO-GO [T5, polar/entire] mixed effectivity

**3A** (quantitative estimate × quadratic form of a window) — PAINTED
- arcs I,X: NO-GO [M,Φ] density, PNT, zero-free zones, sieves
- phase 151 dlVP: NO-GO [M] capped by archimedean density
- phase 154 Paper 47: NO-GO [finZ,M] no dual reached nor finite truncation
- phase 155 TK/N/AL′: NO-GO [TK ceiling] lattice loses Θ(1/M)
- R162_303/703: CERTIFIED [M (no mechanism)] λ_A,λ_W>0 on (0,½log5]

**3B** (quantitative estimate × first-contact kernel vector (linear in F)) — PAINTED
- R162_001/190: PROVED [—] continuity of λ_A
- R162_407 rate: PROVED [F3 (DH)] λ_A(T*+δ)≥−2A*Q*/log(1/δ), blind to weight

**3C** (quantitative estimate × quadratic/higher functionals of F) — PARTIAL
- R160_M7: EQUIV [E1] bilinear computation rewrites eq:form
- R162_502 Part B: PARTIAL→NO-GO [—] coupled bilinear square on the contact vector; B3: no admitted input orients it
- *Residue:* uniform-in-T signed bound on the low-frequency block (R160_020 Option 3) outside the contact vector; M7 Prop 5.2(c) suggests global E1

**3D** (quantitative estimate × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R162_1402 Thm 5: WRONG→weak [—] Markov–Kreĭn WRONG as stated (1590); only j≤2 survives
- R162_1502: NO-GO [F2,F3,M] uniform target |x_m|²≤Cλ contradicted by ζ data

**3E** (quantitative estimate × flow/family in T) — PAINTED
- 159 G2: NO-GO [M,I-13,E1] bootstrap in T, SOS, mollifiers, jump calculus

**3F** (quantitative estimate × global transforms in T) — EMPTY
- *Residue:* estimates on a nonlinear global transform (Mellin in T)

**3G** (quantitative estimate × families of L-functions/fields) — PAINTED
- R162_1004: NO-GO [F1,F2,E1,P149] tensor power: polynomial bound in d ⟺ RH; Thm 3.1 quantifier corrected (1190)

**3H** (quantitative estimate × geometric/dynamical objects) — PAINTED
- phase 152: NO-GO [no form] FUP/Dolgopyat, Berkovich–Poineau

**4A** (multiplicativity/Euler product × quadratic form of a window) — PAINTED
- R161_001-004: NO-GO [F2] sum×product square contains the truncated Weil square
- R162_203: EQUIV [E1] ESB = deregularization
- phase 153 Thm A: NO-GO [Ξ_Q,Beurling] separates ζ only from Ξ_a

**4B** (multiplicativity/Euler product × first-contact kernel vector (linear in F)) — PAINTED
- R162_201/202: EQUIV [E1] ESB/multi-prime Sonin leak
- R162_301: NO-GO [F3] Brown–Halmos leak independent of the symbol
- R162_503: NO-GO [DH line empty] transfers to every degree-1 Dirichlet series
- R162_404: NO-GO [F1] Tate jets as λ⟨Γ_PF,φ⟩

**4C** (multiplicativity/Euler product × quadratic/higher functionals of F) — PAINTED
- R160_M8: NO-GO [Φ] + sign is the sign of a square
- R162_502 B2: PROVED rewrite [E1] M_T(Λ)=ZXZ⁻¹−X
- R162_207: NO-GO [F1] Euler curvature/flat source
- R160_020 Option 6: NOT RUN [—] Meyer's mixed S+D class; D2 calls it sterile

**4D** (multiplicativity/Euler product × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R152_002; 159 G1 K3: NO-GO [no form/K3] Hecke unbounded; self-adjoint Hecke on L²(Γ\𝔥) excluded

**4E** (multiplicativity/Euler product × flow/family in T) — EMPTY
- *Residue:* prime-by-prime insertion flow coupled by the Euler product (1801 homotopy in s is blind to weight)

**4F** (multiplicativity/Euler product × global transforms in T) — EMPTY
- *Residue:* a global generating object with the Euler product entering before regularization

**4G** (multiplicativity/Euler product × families of L-functions/fields) — PAINTED
- R162_1102: NO-GO [F1,F2,F3,M] Thm O: sum over χ with no arithmetic
- arcs III,VIII; 144-149: NO-GO [T1/T2, rationality wall] transport from finite fields, Deligne

**4H** (multiplicativity/Euler product × geometric/dynamical objects) — PAINTED
- 159 G1: NO-GO [OT-5′ walls] Bost–Connes, Borger/Witt, scaling site
- R162_1302: NO-GO [F1,F3,E1] Euler = separability; maximal monodromy

**5A** (integrality of ℤ (floors, torsion, periodization) × quadratic form of a window) — PAINTED
- R162_1902: NO-GO [F2,E1] B₂/sawtooth: value linear in c = ∫|F̂|²Re ζ, both signs
- R162_801: NO-GO [F1,F2,M] ledger: D_a≡0 ⟺ a=Λ but per-window weight rewriting

**5B** (integrality of ℤ (floors, torsion, periodization) × first-contact kernel vector (linear in F)) — PAINTED
- R162_701: NO-GO [E1,F1] (B4.1) identity, equality on N
- R162_1101: NO-GO [F2,F3,E1] pole at −2m reads only atom 0; Thm 4.1(b) WRONG (1390)

**5C** (integrality of ℤ (floors, torsion, periodization) × quadratic/higher functionals of F) — PARTIAL
- R162_903: NO-GO [F1,F2,M] unipotent Gram, Moore collapse; Λχ₂ reading corrected (1190)
- *Residue:* a discontinuous functional separating ℤ from Beurling and 1 from χ₂, not a unipotent invariant

**5D** (integrality of ℤ (floors, torsion, periodization) × spectrum (eigenvalues, Perron, nodal)) — EMPTY
- *Residue:* integrality in the spectrum (multiplicities/Smith form of the contact's Gram matrix)

**5E** (integrality of ℤ (floors, torsion, periodization) × flow/family in T) — PARTIAL
- R162_1802 O1802.3: OPEN [—] nonnegative width via integrality
- R162_1902: NO-GO (linear) [F2,E1] only closed the version linear in c
- *Residue:* nonnegative width of the residue window via integrality that is NOT linear in c, followed in T

**5F** (integrality of ℤ (floors, torsion, periodization) × global transforms in T) — EMPTY
- *Residue:* periodization/Poisson in the T variable of a global object

**5G** (integrality of ℤ (floors, torsion, periodization) × families of L-functions/fields) — EMPTY
- *Residue:* integrality across families (conductors, field torsion)

**5H** (integrality of ℤ (floors, torsion, periodization) × geometric/dynamical objects) — PARTIAL
- R162_1001: NO-GO [F1,F2,F3] cocycle Φ_Λ ⟺ a=Λ, separates Λχ₂ and Beurling (𝒩_B⊄ℤ); band-limited tests read only primes
- R160_M12: PARTIAL [—] ×p
- *Residue:* Pila–Wilkie / model theory / ×p measure-rigidity versus W_T never analyzed

**6A** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × quadratic form of a window) — PARTIAL
- R160_D4 Thm 5.1: NO-GO [window shift] identity in tests = translation to T+½log X
- D4 Cor 5.2: NO-GO [F3] finitely many exact values
- R162_406: NO-GO [datum cancels] boundary coefficient cancels at composite thresholds
- *Residue:* O-D4.2: 𝒲 kernel / 𝒞′ cone on decreasing tests of unbounded support

**6B** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × first-contact kernel vector (linear in F)) — PAINTED
- R162_1401: NO-GO [F3,E1] log only touches X at s=1 (Tate); inert on deletion/DH
- R162_1502: NO-GO [F2,F3,M] comb spill, Λ-step inert
- R162_403: NO-GO [F1] H^(P)=0; symbol identities
- R162_401: NO-GO [F4] [X,S_N]=−K_N
- R162_502 A: NO-GO [equivariance] Hecke

**6C** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × quadratic/higher functionals of F) — PARTIAL
- R162_501: PROVED/no sign [—] Selberg–virial identity
- R162_901: PARTIAL [F2,E1,F3,M] Selberg in the ε² sum channel; difference channel uncontrolled; pole ε_c<1
- *Residue:* control the difference channel |Σw_n n^{it}|² without resumming to Σ_ρ (lesson of 1003)

**6D** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R162_702 residue: OPEN→dead [F3,M] only exact values separate Λ in 𝒞
- R162_1603: NO-GO [F3] cancellation at composite thresholds

**6E** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × flow/family in T) — PAINTED
- R162_802: NO-GO [window shift] Λ*1=log = window translation in the flow

**6F** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × global transforms in T) — EMPTY

**6G** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × families of L-functions/fields) — EMPTY

**6H** (exact values of Λ (Λ*1=log, Selberg, Chebyshev) × geometric/dynamical objects) — EMPTY

**7A** (zero side/explicit formula × quadratic form of a window) — PAINTED
- Paper 47 Thm Z / finZ: EQUIV [E1] certificate = explicit formula
- phase 155 r5: EQUIV [E1] Kreĭn indeterminacy

**7B** (zero side/explicit formula × first-contact kernel vector (linear in F)) — PAINTED
- R162_1501: AUDIT [—] R_LF=0 ⟺ F=0; Lemma D (Descartes) infinitely many sign changes; R-A/B/C targets then dead

**7C** (zero side/explicit formula × quadratic/higher functionals of F) — EMPTY
- *Residue:* a nonlinear functional with zero data (pair correlation as exact, not statistical, input)

**7D** (zero side/explicit formula × spectrum (eigenvalues, Perron, nodal)) — PARTIAL
- R162_2101: PROVED structure [M] quasi-kernel = truncated radical of ζ (Pólya), double-exponential margin
- R162_2190: CONFIRMED float [—] s₂^c=0.9997678
- *Residue:* R-C.b for ζ needs input from the zero side; per-window → collides with M

**7E** (zero side/explicit formula × flow/family in T) — PAINTED
- R162_1802 Thm R: EQUIV [E1] window ∀T
- R162_902: EQUIV [E1] asymptotic

**7F** (zero side/explicit formula × global transforms in T) — PAINTED
- R162_803: NO-GO [E1,F1,F3] Thm G = Lagarias's Herglotz criterion; first contact invisible

**7G** (zero side/explicit formula × families of L-functions/fields) — PAINTED
- phase 149: NO-GO [rationality wall] Gaussian moments/Deligne extraction

**7H** (zero side/explicit formula × geometric/dynamical objects) — PAINTED
- arcs III-V,X; 158: EQUIV [E1,T1,OT-5′] CCM/Ω₇, unitarizing metric, zeros as spectrum, adele class space

**8A** (no arithmetic (structural, blind to weight) × quadratic form of a window) — PAINTED
- arc II; phase 120-121: EQUIV [E1,trilemma] Pontryagin, APS/η, Maslov; F2 arrow

**8B** (no arithmetic (structural, blind to weight) × first-contact kernel vector (linear in F)) — PAINTED
- R162_408: PROVED [E1] (NE) exact; Conj 7.1 ⟺ no contact
- P124_004-010: NO-GO [F1] virial/Mourre on the collar
- R161_016: NO-GO [F1] Markov pullback

**8C** (no arithmetic (structural, blind to weight) × quadratic/higher functionals of F) — PAINTED
- R162_1202: NO-GO [F2,F3,E1] polynomial collapse to the Sonin range at any degree (Thm C); Thm A only on large circles (1390)

**8D** (no arithmetic (structural, blind to weight) × spectrum (eigenvalues, Perron, nodal)) — PAINTED
- R162_1602: NO-GO [universal] resolvent not TP₂; two-restriction count HEURISTIC (1890)
- R162_1701: PARTIAL [E1] R-C.a ⟺ RH given R-C.b
- R162_1801: NO-GO [3×3 counterexample] homotopy/polarization
- R162_1901: NO-GO [3×3 model] model with Type I contact; §3(iv) WRONG (2090)
- R162_2001/2190: FALSIFIER FIRES [two-atom Type I curve] R-C.b false, blind to weight

**8E** (no arithmetic (structural, blind to weight) × flow/family in T) — PAINTED
- arcs I,IV; 159 G2: NO-GO [Φ (DH,Ξ_a)] dBN, Jensen, Lee–Yang, Pólya–Schur

**8F** (no arithmetic (structural, blind to weight) × global transforms in T) — EMPTY

**8G** (no arithmetic (structural, blind to weight) × families of L-functions/fields) — EMPTY
- *Residue:* field-uniform proofs allowed by T1 (phase 157)

**8H** (no arithmetic (structural, blind to weight) × geometric/dynamical objects) — PARTIAL
- 159 G1: NO-GO [OT-5′ walls] motives, Arakelov, operator algebras
- R160_C1: NO-GO [Thm Z] holomorphic lamination: one pole ⇒ ≤1 pair
- R160_C3/D2: NO-GO [Thm H, Thm T] Meyer H¹
- phases 135-140: NO-GO [S-11] real h⁰ / RR
- *Residue:* D1: Torelli-failing lamination with fixed points (Teichmüller lemma unproved); the only carrier class not excluded

## 3. Universal walls (killers that recur in at least 3 cells)

- **W1: blindness to the support class (F3).** Every step that uses only Λ≥0, support on prime powers, or monotone laws holds equally for deletion Λ1_{n≥5}, κ-models, finmod and DH. Appears in 2A, 2B, 2D, 2E, 3B, 8D and 8E. Precise form: the class 𝒞={a≥0, supp PP} contains κ-models with first contacts (702 Thm 2), and deletion has a Type II contact at T≈0.46–0.60 (703, 1601).
- **W2: E1 sinks.** An honest reducer ends up at a form equivalent to RH: the Sonin range (4.2) (1101, 1201, 1202 Thm C), Herglotz/Li (803), "∀T" (1802 Thm R, 902) or the certificate equal to the explicit formula (Thm Z). Appears in 1A, 1B, 1E, 7A, 7E, 7F, 7H and 8C.
- **W3: jets vanish at λ=0 (F1).** Everything that enters as λ·(…) dies at contact: 101, 207, 402, 403, 404, 405, P124, R161_016. Appears in 1B, 2B, 4B, 4C, 6B and 8B.
- **W4: orientation (F2).** The sum×product square contains the truncated Weil square (R161_002); the sawtooth is the comb of (PC) (701, 801, 1902); the Ward defect changes sign with η (205). Appears in 4A, 5A, 5B, 6B, 3D and 4C.
- **W5: Λ*1=log used linearly is a window shift or cancels.** D4 Thm 5.1; at composite thresholds (406, 1603); inert (1401, 1502); in the flow (802). Appears in 6A, 6B, 6D and 6E.
- **W6: Theorem M and the doubly exponential margin.** No gap, compactness, numerics or bootstrap works (3A, 3E, 5A, 7D). R162_2101 makes it worse: ζ itself is at doubly exponential distance from a Type I contact.
- **W7: linear limit (F4).** 206, 401, R161_017–023. Appears in 1A, 1B and 6B.
- **W8: rationality wall / finZ.** 1203, phase 149 and transport from finite fields. Appears in 1H, 4G and 7G.

## 4. Falsifier table (which model kills which property)

| model | what it shares with ζ | what it kills | files |
|---|---|---|---|
| DH / Epstein | functional equation, ε, archimedean side; no Euler product | every FE identity, flow laws, (LB)/virial, CM Kreĭn, degree-1 transport | 102, 407, 503, 1003, 1203, 1301, 802 |
| deletion Λ1_{n≥5} | Λ≥0, support PP, λ_W≤0.4608<T* | Type II exclusion by minimality, monotonicity, nodal S=2, Douglas/log inert | 703, 802, 902, 1401, 1601, 1803 |
| κ-models / finmod a^κ | support, positivity, most values | first quarter, Perron–Tate angle, regularized jet, flow | 103, 204, 702, 802 |
| sΛ amplification | every identity except the scale | sign of ⟨u₂,φ̂⟩, (C2), homotopy in s | 1801 Thm D, 1803 |
| two-atom Type I curve s₂δ_{log2}+s₃δ_{log3} | positive cone, monotone laws | R-C.b blind to weight (FALSE); any spectral exclusion of Type I without zero data | 1901 §4, 2001, 2190 (s₂^c=0.9997678) |
| 3×3 matrix models | Perron, monotone laws | homotopy (1801 Thm B), Type I contact compatible with every law (1901 Thm 2) | 1801, 1901 |
| Λχ₂ | Euler product, Λ*1 = L-series | sums over characters, ε-phase, BCH (after correction); not killed by the Φ_Λ cocycle | 1102, C8, 903, 1001 |
| Beurling DMV | Λ≥0, Euler, exact Λ_B*1=log, zeros off the line | every use of Λ*1=log without ℤ: 903, 1302, 1401, 1402, T3; only killed by the torsion cocycle (𝒩_B⊄ℤ) and by integrality | 1001, 1302, 150 |

## 5. Reverse-engineered specification of a closing argument

A closing argument MUST satisfy all of the following:
1. **Use λ=0 non-perturbatively** (F1): must not enter as a jet λ·⟨…⟩ nor as a first variation.
2. **Be nonlinear in the test c (or in F) and non-polynomial**. Every polynomial functional collapses to the Sonin range (1202 Thm C) and every linear use of integrality is Poisson (1902). Something discontinuous or transcendental in F is needed.
3. **Not be orientation-invariant** (F2): it cannot be the square of (PC)/(PC-ren) nor contain the truncated Weil square.
4. **Separate ζ from all the falsifiers at once**, in particular from Beurling DMV and from Λχ₂. It must therefore use the integrality of ℤ and the exact values (Λ*1=log) together, not just the support. The only objects in the corpus that do this are the torsion cocycle Φ_Λ (1001), the Selberg identity on the boundary channel (901), and the ledger D_a (801, at the level of weights).
5. **Not be a per-window statement with a gap.** ζ is at doubly exponential distance from a Type I contact (2101) and M bounds every margin. It also cannot be an "∀T" of a per-window law (1802 Thm R, 902, 803 are E1). It must be an object in T that is not a reformulation.
6. **Not be Hecke-equivariant nor translation-equivariant** (D4 Thm 5.1, I-13): it cannot be an identity in ℤ[ℚ_{>0}].
7. **Bring in the Euler product after resummation of the FE and before regularizing**, breaking the trivial-zero/continuum cancellation (204, 305, 1003).
8. **Not be a weight-blind spectral criterion**: there exists a Type I curve in the positive cone (2001).

Unpainted cells that can satisfy 1–8: **5C** (discontinuous, non-unipotent functional; satisfies 2, 4 and 6), **5E** (nonlinear integrality followed in T; satisfies 2, 4 and 5), **5H** (non-band-limited ×p torsion plus o-minimal counting; satisfies 4 and 6), **6C** (boundary Selberg; satisfies 4 and 7, but is at per-window risk), and **4F/5F/6F** (nonlinear global object in T; satisfies 5; nobody has tried it). Candidates the specification rules out or that collide with it: **7D** (per-window, collides with 5 and M), **3C** (M7 suggests E1), **6A** (O-D4.2 is a domain question, contributes no mechanism), and **8H** (D1 is costly and poorly falsifiable).

## 6. Unpainted directions, ranked

1. **5C×5E: a discontinuous integrality functional followed in T.** One must build Ψ_T(F) from the cocycle Φ_Λ, reading torsion atoms r/d with r≠0 (not only atom 0, which is what killed 1101), not a unipotent invariant (residue of 903). Then its evolution across the residue window must be studied (O1802.3, nonlinear version). First falsifiable lemma: Ψ vanishes identically for Beurling with 𝒩_B⊂ℕ iff a=Λ, and fails on a declared line for Λχ₂ and deletion. This is the only direction that satisfies 2, 4, 5 and 6 at once.
2. **6C: the difference channel of the boundary Selberg identity (901).** It is the only exact nonlinear object that separates the four falsifier classes. What remains is to control |Σw_n n^{it}|² without resumming to Σ_ρ (otherwise it falls into 1003 Thm R). Risk: it is per-window (point 5).
3. **5H: ×p with Pila–Wilkie / model theory / measure rigidity versus W_T.** Never analyzed; the cocycle already separates Λχ₂ and Beurling. One must move from band-limited tests to non-trigonometric window measures.
4. **4F/5F/6F: a nonlinear global generating object in T.** The linear version (803) is Herglotz (E1). A product or determinant in T where Euler and integrality enter before regularization has not been attempted. First check: that it does not reduce to ξ′/ξ.
5. **8H (D1): the Torelli-failing lamination with fixed points.** It is the only carrier class not excluded by Thm Z/Thm H. It is the costliest and least falsifiable direction; worthwhile only if 1–4 fail.

Rule of use: before building, locate the idea in a cell. If the cell is ■, the idea must declare which of properties 1–8 breaks that cell's killer; if it does not declare it, it is not built.
