# R166_401 — Survey A: mechanisms of phases 160–163 against requirements (i)–(iii)

*Read-only survey. No numerics, no commits. No label of record moves.*
*Calibration: R166_190 §0 (wall dichotomy) and "Cierre de la phase 166" (R166_201 Thm 1.3, jet hierarchy).*

**Criteria (applied literally, as specified in R166_190).**
- **(i) GLOBAL in X**: the mechanism uses the whole node set or the whole witness globally (Hadamard/Cartwright product, phase, Poisson/harmonic measure, Cauchy transform of G², Toeplitz/Wiener–Hopf structure). Jets or divided differences at nodes (k = 0, 1 in R166_201 Thm 1.3) do **not** count. Global in the *zero* set only (e.g. canonical exchange E) does **not** count.
- **(ii) ATOMIC PRIME SIDE BEYOND THE WINDOW**: Λ(n) for n ≥ e^{2T_c} (in practice: all n, since f_t matches ζ's prime side on any finite range log n < 2T₀, R163_901 Thm F) enters atomically / positively / multiplicatively. "The explicit formula" in the abstract, Λ*1 = log used linearly (W7), or prime data with n < e^{2T} do **not** count.
- **(iii) NOT E1 / NOT f_t / NOT M_m**: the statement is not (1.1) on a single test (nor an E1 restatement), and the record does not kill it by f_t (window-only) or M_m (zero-set-only). A kill by a *different* falsifier (Λ̃, Z_K, f_χ, ζ_θ, K(s), DH, orientation F2, identification) does **not** remove (iii); it is recorded in the wall column.

Sources read: R166_190 (§0, cierre); R162_2300 MASTER GRID §3–§7; R162_590 (dead-end map, phases 0–162); R160_010 (round-1 verdicts C1–C8, M1–M12), R160_X_C1 via R163_501/R162_2201; phase-161 file list + R162_590 §1b; phase-162 README log + memo headers; phase-163 README (R163_001–162) and memo headers of R163_001–003, 101, 102, 113–118, 401, 402, 501, 502, 601–603, 701, 702, 801–803, 901, 1001.

## 1. Table (sorted: 2-of-3, then 1-of-3, then 0-of-3)

| # | mechanism | files | (i) | (ii) | (iii) | wall / killer | best residue | one-line why |
|---|---|---|---|---|---|---|---|---|
| **2-of-3** |||||||||
| 1 | **Interpolation identity with tail** Σ_ρ G(t_ρ)²/(t_ρ−x) = C_T(x) − iG(x)²𝒯_T(x) | R163_801 Thm 3, Cor 3.1 | Y | Y | N | M_m (R163_801 Thm 5: Thm 3 holds verbatim for M_m); on X the tail vanishes (Cor 3.1) ⟹ node system = E1 | the tail 𝒯_T carries every off-line residue; rough-zeta split 𝒯_X = 𝒯^det + 𝒯^new (R166_103 β) | Cauchy transform of the whole G² (global) against Σ_{log n≥2T}Λ(n)n^{−½+ix} (atomic, beyond window); but evaluated on X it is the kernel equation and M_m satisfies it |
| 2 | **Minimal atomic node object** 𝒜(s;G) = Σ_x q_x(−ζ′/ζ)(s+ix) | R162_2201 Thm N1, Lemma N0 | Y | Y | N | Lemma N0: node tests are Paley–Wiener ⟹ band-limited pairing reads only n < X = e^{2T_c} (window ⟹ f_t); (b) only "⟹"; W4/W5 | O2201.1 asymmetric node weight → zero side (W6) | sums over all nodes against the full Dirichlet series −ζ′/ζ, but every pairing it supports is band-limited |
| 3 | **Atomic support ⟹ automatic Dirichlet ⟹ RH** (supp q_E ⊂ log ℕ; no-gap lemma on (0, log 2); first-gap cones, two-channel margin) | R163_114, 115, 116, 117, 123, 124, 125, 126 | N | Y | Y | W-identification: the hypothesis (support in log ℕ at all heights) is unprovable without RH; R163_114 = "atomicity of exchange ⟺ RH" (R166_190 §0) | "único dato propio de ζ": exact duality Z_ζ ↔ Λ atomic on log ℕ at all heights | uses atomicity of the whole prime side; a class statement, not (1.1), not shared by f_t/M_m; never touches X |
| 4 | **Hamburger collapse / rigidity** (Euler fibres, rational defect ζ₀=ζ/R, conductor-1 class {cζ}) | R163_113; R162_2601c, 2801; R163_1001 Thm O (deformation + theta-periodicity routes) | N | Y | Y | W-identification; W3′ (f_χ at conductor > 1, R163_1001 §5) | none on record beyond identification | integer frequencies + FE at all heights pins ζ; identification returns the zero question unchanged |
| 5 | **Beurling frontier BF_θ^disc** (integer prime multiplicities, N = ρx + O(x^θ); lattice rigidity Thm R; Witt rounding C_{1/3}) | R163_003, 101, 102, 103–105, 110, 803; R162_2901 | N | Y | Y | ζ_θ (extended class), Theorem C (θ ∈ (1/3,½)), Cor F (ℕ-comparable part RH-equivalent), Theorem L (R164) | O164.201a: off-lattice discrete system, θ′ ≤ 1/3 | multiplicative, atomic, all scales; class statement about Beurling systems, not about X |
| 6 | **Positive-factorisation support lemma** ν_N = ν₀*κ ⟹ both on log ℕ | R163_002 | N | Y | Y | countermodel K(s)=1−c/(s+1) (no FE); E(σ)<1 so E is not a Laplace factor | — | support rigidity of positive multiplicative measures; the arithmetic never supplies the positivity hypothesis |
| 7 | **Classical zero-free region / sub-Landau P_loc** (de la Vallée Poussin, 3+4cos+cos² Euler positivity) | R163_701 (with R163_602 §2.1) | N | Y | Y | W2 / Theorem M (width 1/log γ, dominance needed; only near-RH, asymmetric log log loss) | O701.1–3 (remove (Dom); sub-Landau lower frame; middle regime) | uses Λ ≥ 0 at all n via the Euler product; not window, not zero-side; quantitatively too weak |
| 8 | **Zero-density input** Σ_{γ≤R} δ² ≪ R/log R (Selberg) | R163_115 §1, R163_502 Δ, R163_401 §4.2 | N | Y | Y | W2 (aggregate, not individual; NG-B1/CIR-2) | used only as a bound on where a quartet can sit | mollified Dirichlet polynomials of all lengths; density, not sign |
| 9 | **Gamma–Selberg tail / rational collision ledger** B_F″(0) = E_X + εC_X − εI_X, collar opened from n > e^{2T} | R163_135, 139, 140, 141 | N | Y | Y | R163_141: E_X is trace class, no uniform gap (W2 type); C_X sign open | collar of rational collisions e^{2T} < n < e^{4T} | second Selberg jet W = Λ·log + Λ*Λ beyond the window, positive tail; no gap, never sees X |
| 10 | **Cross-energy torsion lift + Gamma tail** (k > e^{4T}: −εĥ_A(k) = Σ K_m(F)²/[ζ(2m+1)k^{2m+1}] > 0) | R163_127, 128, 129, 130, 131, 132 | N | Y | Y | F2 (Jensen gives the same sign after A ↦ −A, R163_129); two-ledger falsifier a_κ (R163_132) | (G_K) of RH strength | Euler inversion beyond the window with strict positive tail; orientation-blind |
| 11 | **Same-weight Euler lift / tilt / Euler–Poisson rectangle** | R163_142, 143, 144, 145 | N | Y | Y | Z_K = ζ(1−2^{−s})^{−K} (R163_147: genuine Euler, primitive first contact) — W3 | Gamma–Euler cross term 2(χ′/χ)L(1−s) | μ_a inverse of the full Euler product; class-blind |
| 12 | **Moving-graph boundary waves / hyperbola cross channel / dyadic resolvent / microscopic cutoff tomography** | R163_148–162 | N | Y | Y | Z_K (main term identical, R163_157); no sign in the radical (R163_159); unitary tangent = mean orientation (R163_162) | dyadic subprincipal signature (R163_160–161) | Λ *_M Λ on the cut hyperbola, all n as N → ∞; recovers every a(n); sign-free |
| 13 | **Tate 2×2 canonical system** H_S = ½exp(2Θσ₁), Θ = Σ artanh p^{−½} | R162_2701 | N | Y | Y | Thm P: H ≻ 0 for every boost chain (RH-neutral, W3) | — | product over all primes, multiplicative and positive; positivity holds for any chain |
| 14 | **Piltz / multiplicative ledger** (d_k exact integers, k ≍ log x) | R162_2802 | N | Y | Y | Thm PB: Piltz sums see only the pole; zeros killed by 1/Γ(−z) (W3) | O2802.1 | integer multiplicative coefficients at all n; zero-blind |
| 15 | **Generalised integer measure dN₀ ≥ 0** (ζ₀ = ζ/R) | R162_2901 | N | Y | Y | Thm A: dΠ₀ ≥ 0 fails for every m ≥ 1 in the strict class; Thm B (Beurling positive with RH) | BF_θ^disc (row 5) | positivity of a Beurling integer measure at all scales; class statement |
| **1-of-3** |||||||||
| 16 | **Light-cone lemma / phase law** θ′_δ = πP_δ (Cartwright–Levinson product) | R163_402 §1, R163_401 §3 (Lemmas 3.1–3.4) | Y | N | N | M_m (same witness/nodes); resolution law PROVED only in lattice model, (★_cell) fails there (Cor 4.10a) | ω(E) = global phase / harmonic measure of X (R165_201, Rem 4.8a) | Hadamard product of the whole real-rooted witness; zero side only |
| 17 | **Lattice-model resolution law** sinh(2δT) − 2δT = δL | R163_402 §2, R163_401 Lemma 4.10 | Y | N | N | model only; M_m; (I0) refuted a fortiori | — | phase of a lattice product (global), no arithmetic |
| 18 | **Blaschke witness** (Thm B invariance, Thm R, FC; real-rooted, parity-definite) | R160_X_C1, R163_501 | Y | N | N | M_m has the same witness structure (R163_801 Thm 5) | witness existence PROVED (input, not mechanism) | global structure of ker W; no primes |
| 19 | **Node quadrature / closure of the node span** (Thm Q Akhiezer; Q0/Q1 annihilator) | R162_2301 Thm Q, R163_502 Q0–Q2, R163_401 §4.5 | Y | N | N | window (exact only in type ≤ 2T_c) + E1; M_m | (Q) in D-norm OPEN (RH-neutral) | uses all nodes as quadrature, but only window data |
| 20 | **Poisson majorant / bound on N_−; balance N_− = P_+** | R163_401 Lemma 3.2, §4.1, §4.3 | Y | N | N | balance is (1.1) itself (E1); M_m | — | harmonic majorant of log\|G\| is global; content is (1.1) |
| 21 | **Kreĭn determinacy of the node measure** (Thm G, w_x = d_x/\|F̂′\|²) | R160_X_C1 Thm G; R162_2201 §3 (P47 thm:KEP3) | Y | N | N | E1 (RH ⟺ Kreĭn indeterminacy, phase 155 r5) | — | global moment problem on X; restatement |
| 22 | **Selberg-invariant regions** ∩_T 𝒫_T | R163_802 | N | Y | N | E1 (Fact 1 = Weil criterion); Thm U: Λ isolated in ∩𝒫_T, no N_b condition separates | — | Selberg map multiplicative, all a(n) as T → ∞; region = Weil |
| 23 | **Selberg difference channel** (Lemma S: Selberg identity ⟺ a = Λ, recursive) | R162_2301, R162_501, R162_901 | N | Y | N | hidden contacts n ∈ [e^{T_c}, e^{2T_c}) are window (f_t); E1, F2 | O202.1 (T_e = T_o, no sign) | multiplicative identity Λ·L + Λ*Λ = μ*L²; evaluated only in the window |
| 24 | **Torsion cocycle Φ_Λ / ×p rigidity** (ℒ_pΦ − Φ = log p(δ₀ − Leb) ∀p ⟺ a = Λ) | R162_1001, R160_M12 | N | Y | N | pairs to the prime term only (band-limited ⟹ window ⟹ f_t); F1, F2 | separates Λχ₂/Beurling (new) | atomic, multiplicative cocycle over all p; reaches W_T only through the window |
| 25 | **Torsion atoms (non-band-limited tests)** / torsion entropy | R162_1101, R163_106, 107 | N | Y | N | Thm 2.2: pole at −2m reads only atom 0; Riesz → Sonin (E1); R163_107 exact collapse h_F(0)−∫h_F = 2‖F‖² (λ-independent) | — | non-band-limited pairing with Φ_Λ; collapses to a contact-blind identity |
| 26 | **Euler-value detector −ζ′/ζ(2m+1)** (Γ–Euler observability) | R161_066–072, R162_2502 | N | Y | N | Thm K: faithful comparison without division ⟺ Gate 1 (window, E1); Thm D: detects only Gamma moments | — | full Euler values (all n), but comparison is the window gate |
| 27 | **Euler gate modes** K_F(1+2πik/log p) | R163_201–203, 290 | N | Y | N | CIRCULAR: (U) holds for every F ≠ 0; the contact equation sees no mode | — | local Euler pole lattice at every p; tautological |
| 28 | **Single Euler-channel scalar (R-B)** | R162_1603 | N | Y | N | Thm P positivity lock; = Gate 1 on coherent class (E1); composite-threshold cancellation | — | all convergent Euler scalars are positive; reduces to the window gate |
| 29 | **Floor ledger** (D_a ≡ 0 ⟺ a = Λ) | R162_801 | N | Y | N | per window a weight rewrite (f_t); floor + Stirling = (PC) sawtooth (F2), M | — | exact integer identity at all n, used per window |
| 30 | **Fourier quasicrystal / crystalline rigidity** | R162_1002 | N | Y | N | E1 (presupposes real zeros; one-member class) | — | supp log ℕ globally; the rigidity theorem assumes the conclusion |
| 31 | **Atomic comb vs exponential density** ("atomic comb ⟹ E = 0") | R162_2601 | N | Y | N | false as posed: falsifier Λ̃ (positive atomic weights 1 − Σ2Re n^{ρ_j−1}) | O2601.1 (individual Euler-product property) | atomic positive weights at all n, but Λ̃ reproduces E |
| 32 | **Splicing / zero-free Euler completion / normal family** | R163_119–122 | N | Y | N | R163_122: {Z_X} normal ⟺ RH (E1); R163_119 finite jets splice into a counterexample (f_t-type) | — | completes prime prefixes by positive continuous primes; equivalence |
| 33 | **Local prime capacity / single-prime period / atomic infinite-exchange model** | R163_108–112 | N | N | Y | finite prime set (not beyond-window multiplicative); verification height; Hamburger collapse R163_113 | — | rational local factors at finitely many primes; class statement, not (1.1) |
| 34 | **Twisted prime sums at the Landau window** Σ_{n<γ}Λ(n)n^{−½−iγ} | R163_602 | N | Y | N | finite-range ⟹ f_t (any N₀); Bombieri–Hejhal falsifier; P_loc family ⟺ D (E1) | O602.1 → R163_701 | atomic sums beyond e^{2T_c} but finite and window-local |
| 35 | **Witness–mollifier coupling** (Z·M, Levinson–Conrey) | R163_603 | N | Y | N | L2.1: RS/AFE is FE-only, shared by f_χ; (A-loc) ARGUED, f_t | (A-loc) OPEN | μ(n) up to the mollifier length; local, aggregate |
| 36 | **(★_cell)/(I1-T) from the arithmetic** | R163_401 §4.8–4.9, Rem 4.8a | N | Y | N | W2 (fails at named step); Rem 4.8a: (★_cell) ⟺ RH at the witness (E1) | (★_cell) itself | Euler input on δ, cell-local |
| **0-of-3** |||||||||
| 37 | Canonical exchange of quartets E = ∏E_{δ,γ}, Frullani current q_E, defect D_test | R163_001, 003, 118 | N | N | N | E1 (R163_003: q_E = off-line part of the explicit formula) | tool (faithful defect) | global in zeros, not in X; reorganises the EF |
| 38 | Node-pair Gram system W(H_a,H_b) = 0 (Loewner matrix of Ω) | R163_801 Thm 1, Prop 2, Prop 4 | N | N | N | E1 (= kernel equation on {H_x}); M_m (Thm 5) | — | divided differences = jets; primes only n < e^{2T} |
| 39 | Local atomic count with budget V_T | R163_801 Prop 5.1 | N | N | N | no sign; window atoms (f_t) | — | atomicity only inside the window |
| 40 | Node identity w_x = L(x)/F̂′(x); no descent (Thm ND) | R162_2202 | N | N | N | Christoffel, n < e^{T_c}; F1 | O2202.1 | nodal jets (k = 1) |
| 41 | Hidden contacts (H = sum channel of the half-witness) | R162_2401 | N | N | N | window [e^{T_c}, e^{2T_c}); no forced sign | OS-2 → O202.1 | window contacts |
| 42 | P_loc cell decomposition, margin inheritance, verified height | R163_601, 702, R163_401 §4.7 | N | N | N | E1 (family ⟺ D); Theorem M; Thm B (K_H: verification reduces to the tail) | — | window-local cells; finite verification = finZ |
| 43 | Integer zero configurations / f_t family | R163_901 | N | N | N | is the f_t killer (Thm F) | — | window data + integrality of multiplicities |
| 44 | C_B (m < ∞ ⟹ m = 0), exponent law 2β* | R162_2501 | N | N | N | M_m | O2601.1 | zero-side counting |
| 45 | Window-Hamburger | R163_1001 (third route) | N | N | N | f_t (W3′, "5A vía f_t") | — | Hamburger restricted to a window |
| 46 | Sum × product square, Müntz–Chebyshev anomaly, polar renormalisation | R161_001–004 | N | N | N | F2 (contains the truncated Weil square) | L161.3 Poisson port | Λ*1 = log in the window |
| 47 | First-contact Poisson port / exterior port kernel / two exterior histories | R161_005, 006, 040 | N | N | N | F4; (4.2) Sonin range | — | archimedean/Tate ports |
| 48 | Product-Hardy ports / typed and exact scattering defect / three-block scattering | R161_008–011, 017, 020, 049–051 | N | N | N | F4 tautology [ζ,D_Γ]=0; unitary countermodel | "required arithmetic input" (R161_050) | linear completions |
| 49 | Gamma-lattice exterior field / Sonin range / pole-lattice rigidity / residue energy (Hankel) | R161_014, 019, 025, 026, 028; R162_1201, 1202 | N | N | N | E1, F1–F3 (holds for all models); polynomial collapse to Sonin (Thm C) | — | archimedean only |
| 50 | Markov pullback / moving discrepancy / method of images | R161_016, 027–029 | N | N | N | F2 | reverse-Markov typing | window prime contacts, indefinite |
| 51 | Mixed Green / Wronskian / Tate defect / double commutator / Poisson–Tate Lagrangian / power identities | R161_042–044, 057–065 | N | N | N | F4, E1, horizontal NO-GO | — | linear Tate identities |
| 52 | Toeplitz–Hankel local square | R161_045 | N | N | N | does not globalise the gate (R161_045 title) | — | local square, not global Toeplitz structure |
| 53 | Unimodular Poisson colligation / two causal orientations / unitary phase | R161_052–056, R163_162 | N | N | N | wrong tangent (mean orientation) | — | phase of a unitary, not of the witness |
| 54 | Local Weil limit / weak renormalisation / continuum mod Tate | R161_075–079, R162_2302 | N | N | N | Thm N: weak limit ≡ 0 (ζ(1−ρ)=0) | O2302.2 c_f ≠ 0 | — |
| 55 | Minimality / virial / right minimality / local lower bound | R162_101, 405, 407, 501 | N | N | N | F1 (zero first variation), DH has first contacts | comb virial with Euler before regularisation | weight-blind |
| 56 | ESB / multiprime Sonin leakage / Ward defect / exterior Ward / coefficient law | R162_201–205, 302, 304, 305 | N | N | N | E1, F2, F3, trivial-zero cancellation | — | — |
| 57 | Log-weighted channel / smooth comb / Chebyshev threshold / Möbius-conjugation square / nonlinear Möbius BCH | R162_401, 403, 406, 502, 701, 903 | N | N | N | W7, F4 ([X,S_N] = −K_N), F1 | — | Λ*1 = log linear, windowed M_T(Λ) |
| 58 | Perron–Tate angle / D3 converse / Type I–II split and searches | R162_702, 703, 1701, 1801, 1901, 2001, 2101 | N | N | N | F3 (κ-models, deletion), two-atom Type I curve | R-C.a + R-C.b | spectral, weight-blind |
| 59 | T-evolution / Laplace in T (Thm G Herglotz) / Q-functions / Kreĭn Jordan / Douglas-log | R162_802, 803, 1301, 1401, 1402 | N | N | N | E1 (Lagarias Herglotz), F3, M | — | ∀T restatements |
| 60 | q-difference RH problem / Laumon transport / character family / tensor power / o-minimality | R162_1302, 1203, 1102, 1004, 2402 | N | N | N | F3 + E1; rationality wall W8; Thm O; idempotent; W10+W8 | — | Euler curve data shared by Λχ₂/Beurling (1302: (ii) arguable, killed E1) |
| 61 | Phase-160 round-1/2 carriers: lamination (Thm Z), prolate triples, Meyer H¹ (Thm H) + non-homogeneous positivity, Witt/W(R), ε-phase, variational, polar capacity, Gaussian correlation, bilinear, two-variable Schur, Doob CD, ring datum Λ*1 = log via dilations | R160_C1–C8, M1–M10, D2, D4 | N | N | N | Thm Z, Thm H/Thm T, E1, Φ (identities hold for Λχ₂/Ξ_a/DH/combs), D4 Thm 5.1 (window shift) | D1 Torelli-failing lamination (never written) | none uses a ζ-specific datum (R160_010 lesson) |

## 2. The 2-of-3 mechanisms, grouped by pair

**{i, ii}** (global in X **and** atomic primes beyond the window; fail (iii)):
1. Interpolation identity with tail (R163_801 Thm 3 / Cor 3.1). Killed by M_m (Thm 5), and on X it reduces to the node system (E1).
2. Minimal atomic node object 𝒜(s;G) = Σ q_x(−ζ′/ζ)(s+ix) (R162_2201 Thm N1). Killed because node tests are Paley–Wiener: every pairing reads only the window (Lemma N0 ⟹ f_t).

**{i, iii}**: **empty.** In 160–163 every mechanism that is global in X (light cone, Blaschke witness, Poisson majorant, quadrature, Kreĭn node measure, lattice resolution law) is zero-side only and so is killed by M_m.

**{ii, iii}** (atomic arithmetic, class-level, not E1/f_t/M_m; all fail (i), never touching X):
3. Atomic support ⟹ Dirichlet ⟹ RH, with the no-gap lemma and first-gap cones (R163_114–117, 123–126). Wall: identification (the hypothesis is the "único dato propio").
4. Hamburger collapse / rigidity (R163_113, R162_2601c/2801, R163_1001 Thm O). Walls: W-identification and W3′ (f_χ).
5. Beurling frontier BF_θ^disc (R163_101–105, 110, 803; R162_2901). Walls: ζ_θ, Theorem C, Cor F, Theorem L. Residue O164.201a.
6. Positive-factorisation support lemma (R163_002). Killed by the K(s) countermodel.
7. Classical zero-free region, sub-Landau (R163_701). Walls: W2 / Theorem M.
8. Selberg zero density Σδ² ≪ R/log R (R163_115, R163_502 Δ). Wall: aggregate, W2.
9. Gamma–Selberg tail / rational collision ledger (R163_135, 139–141). Wall: trace class, no gap.
10. Cross-energy torsion lift with positive Gamma tail beyond e^{4T} (R163_127–132). Walls: F2 orientation, a_κ.
11. Same-weight Euler lift / tilt / rectangle (R163_142–145). Wall: Z_K (W3).
12. Moving-graph waves / hyperbola cross channel / dyadic resolvent (R163_148–162). Walls: Z_K, no sign.
13. Tate 2×2 canonical system (R162_2701). Wall: RH-neutral (Thm P).
14. Piltz multiplicative ledger (R162_2802). Wall: zero-blind (Thm PB).
15. Generalised integer measure dN₀ ≥ 0 (R162_2901). Wall: Thm A.

**Reading.** The record splits cleanly along the R166_190 dichotomy. Global-in-X devices are zero-side only (M_m), and atomic-arithmetic devices are class statements that never touch X (identification, W3/W3′, W2). The only bridges are the two {i,ii} items. Both pair the whole witness with the full −ζ′/ζ, and both are killed in the same way: once they are evaluated on X or paired with Paley–Wiener node tests, the beyond-window tail drops out exactly (R163_801 Cor 3.1; R162_2201 Lemma N0). So the open target is a statement built on the tail G²𝒯 **off** X (e.g. at t_q or Im x > ½) that M_m does not satisfy. This is where R166_103 β (rough-zeta split) and R164_501 Prop 4 (positive tail 𝒯(iy)) already point.
