# R166_404 — Survey 2 of 3: phases 111–159 against the three phase-166 requirements

Read-only survey. Index used: master grid `phase-162-row-d-first-contact-closure/grid/R162_2300_MASTER_grid.json` (264 routes whose id names a phase in 111–159, cell given as row+column, e.g. `7A`), `phase-136-row-d-map/MAP_4_PHASES_111_135_AND_PAPERS.md`, `PHASE_136_MAP_SYNTHESIS_AND_PLAN.md`, R160_S1–S5 surveys, PATH-TO-D, ROW-D-REDUCED-STATEMENT. Theorem names were checked against papers 43–47 and the phase files that are cited.

## Criteria (literal, from R166_190 §0 and "Cierre de la phase 166")
- **(i) GLOBAL**: the mechanism reads the node set X / the witness F as a whole (Hadamard product, phase, harmonic measure, Wiener–Hopf / factorization, global extension problem). It fails if it reads finitely many node jets, a finite truncation or a finite mode arena, or if it never touches the witness.
- **(ii) ATOMIC COUPLING**: the mechanism uses Λ(n) beyond the window (n ≥ e^{2T_c}), with Λ ≥ 0 on prime powers, multiplicativity, and all heights, and it does so **non-linearly** and coupled to the zero side. It fails when a falsifier that shares those features kills it (Ξ_a, Ξ_Q, Beurling, DH, Epstein, comb models, function field), because then the atomic structure is not really used. Prime-local, finite-S, window-only and Pólya-type weight-deleting realisations also fail.
- **(iii) NON-REDUCTION**: the mechanism is not equivalent to the explicit formula / a zero-side identity on one test (wall E1). It is also not a window-only statement (killed by f_t, thm:finmod / cor:void) and not a zero-set-only statement (killed by M_m, finZ, Li, Kreĭn on the zero side). Grid killer E1 means the mechanism fails (iii).

`wall` = the wall that killed or caps the mechanism. `residue` = what is left precisely, if anything. Statuses are the grid's.

**Headline. No mechanism in phases 111–159 meets all three.** 17 meet two of three; they are listed first. This agrees with the phase-166 closure ("Ningún mecanismo del corpus cumple (i)–(iii)").

## Table

### Two of three

| # | mechanism | phases / files | grid ids | (i) | (ii) | (iii) | wall | residue | why |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Wiener–Hopf factorization 𝒯=A*A / D_Euler / Douglas norm | 136 PHASE_136 S6; 120 C.1 | 1A `136 PHASE_136 S6`; 1A `R160_S3 L3 phase-120 C.1` | Y | Y | N | E1 | none: "target, not route" | A Wiener–Hopf factor of the Euler operator is global and multiplicative in Λ, but its positivity is row D restated (Paper 47 Thm 3.7) |
| 2 | Sharp Douglas gate: contraction over prime-power births | 114 D.170; 120 P3 trilemma | 8A `phase-114/D.170`; 8A `phase-120/P3_COMMON_FAILURE_ARCHITECTURE`; 8A `R160_S3 §2.2#1` | Y | Y | N | E1 + locality–phase–sign trilemma | none | Contraction Y=ΘX is global and indexed by all prime powers; every linear positive lift is one Douglas factor, i.e. E1 |
| 3 | Adèle class space A_Q/Q^× as MW-5 object; Connes spectral realisation | 158 R158_002/005; 160 S5 §2.2#10 | 1H `158 R158_005`; 7H `R160_S5 §2.2#10 R158_002`; 7H `arcs III-V,X; 158` | Y | Y | N | E1 (OT-2 fails; OT-5′ = Weil criterion) | MW-5 not excluded without an object (R157_002) | The spectrum is all zeros and the orbits of length log p carry Λ multiplicatively; positivity is still the Weil criterion |
| 4 | Deninger/Serre axioms D1–D3 (Lemma T); laminated carrier | 158 R158_001 Lemma T, §4 (18 frameworks); 159 G1 | 8H `R160_S5 §2.2#8`; 8H `§2.2#9`; 8H `R160_S5 §5#2` (OPEN); 8H `159 G1` | Y | Y | N | E1 (Lemma T: D1–D3 ⟺ RH); OT-1/2/3/5′ | laminated carrier with fixed points + Álvarez López–Kordyukov polarisation, never built (8H OPEN) | The axioms are global and Frobenius-at-every-p, but they are satisfiable iff RH |
| 5 | Meyer nuclear H¹ / density of H¹_alg | 158 R158_004/006 | 7H `158 R158_006` (PARTIAL); 7H `R160_S5 §3.3 row 11` (OPEN) | Y | Y | N | E1 (sign = off-line part, Thm H) | density of H¹_alg in Meyer H¹ (OPEN, "possibly RH-adjacent") | Density over the whole spectrum is proved (C3); the sign is just the off-line part of the explicit formula |
| 6 | Euler determinant lines / Contou-Carrère / Bohr carrier, global assembly | 122 P122_013-017 | 4H `122 P122_013-017`; 4B `R160_S3 §2.2#21` | Y | Y | N | E1; cocycle splits prime by prime; F3:Ξ_a for the gates | none | The determinant is global and its Euler factors are multiplicative, but the assembled curvature is exactly the window form q_T |
| 7 | de la Vallée Poussin / T6 numerator-sign (3+4cos+cos²) | 151 R151_005 T6; Paper 47 Part IV | 2G `151 R151_005 T6`; 3A `phase 151 dlVP`; 2G `R160_S4 §2.B#24` | N | Y | Y | M (archimedean density cap, depth 1/log γ) | O-151.4 | It uses Λ≥0 at every prime power and every height, non-linearly; it is not E1; it is pointwise in s and never reads X; depth is capped |
| 8 | Summand-vs-numerator axis O-151.4 | 151; 160 S4 §3.2#19 | 8C `151 O-151.4`; 8C `R160_S4 §3.2#19` (OPEN) | N | Y | Y | — (never developed) | **OPEN residue**: the true axis of numerator-sign mechanisms | Same input as row 7, with no window and no E1; nothing in it touches the node set |
| 9 | Landau lemma: no primitive class with all Frobenius traces ≥ 0 | 143 Thm D.34.5 | 4A `143 D.34.5` (PROVED-TOOL) | N | Y | Y | gives only a real-axis singularity / boundary purity (cf. 2A `R160_S2 F38`: ω ≤ ¼) | used as a tool only | It uses non-negativity at all prime powers and all heights, non-linearly (Pringsheim–Landau); it is not a test identity; it is blind to X |
| 10 | Beurling T3 additive-structure theorem (atomicity of log ℕ) | 150 R150_005 T3; Paper 47 Part IV; 157 (H-DMV cited) | 2G `150 T3` (PARTIAL); 2G `phase 150 T3` | N | Y | Y | F3:Beurling ("puerta Beurling") | T3 conditional on H-DMV (now CITED) | It is the only phase-150 statement that sees the integrality of log ℕ (cf. R163_114); it is not E1; it does not read the witness |
| 11 | Deligne extraction on the additive pencil (Gaussian moments, singular series) | 149 R149_005 D.59, D.61; 150 T5 | 6G `149 R149_005 D.59`; 7G `phase 149`; 4G `149 D.61`; 3G `150 R150_005 T5` | N | Y | Y | T5 + rationality wall; (P149) = k-tuple conjecture | missing a-priori ingredient (iii) of D.59 | Moments of Λ correlations beyond the window are non-linear and not E1; extraction is Hölder over fibres (T5), so it never reads X |
| 12 | Rationality wall Thm R / R′ (six exponentials at ≥3 primes) | 159 G1_B4_R5 | 5H `159 G1_B4_R5` (PROVED-TOOL) | N | Y | Y | W8 | residual = OT-5′ | It uses the multiplicative independence of p ≥ 2 (transcendence), not a test identity; it acts per zero, not on X |
| 13 | BRS Theorem P: no pure prime–zero Fourier pair; BRS uniqueness among log ℕ combs | 159 G2_B6_R4 (BRS CITED) | 7B `159 G2_B6_R4` (PROVED-TOOL, F4) | N | Y | Y | F4; β-blind (holds for off-line Dirichlet series) | Lemma S / Thm X unaudited | It characterises the atomic comb (±log ℕ, Γ_ζ) as a crystalline pair, which is not E1; it is blind to β and to X |
| 14 | Identity-level Λ = μ*log; entropy-weighted xp | 157 R157_002 #27/#30/#55 | 6B `R160_S5 §3.3 R157_002` (OPEN) | N | Y | Y | no object | **OPEN**: regions not excluded | A Dirichlet-convolution identity is non-linear and multiplicative and is not a test identity; no witness reading |
| 15 | Non-local Tauberian with LI input (Beurling–Malliavin on p^{iτ}) | 157 GAP-157.A (from phase 49) | 4F `R160_S2 §3.2 GAP-157.A` (OPEN); 3F `F40` (PARTIAL, E1 for the local version) | N | Y | Y | the local version is E1 | **OPEN**: condition C1 of Doc 159, neither known nor excluded | It uses LI over all primes and is non-local in frequency, so it escapes E1; it never touches X |
| 16 | Relative correspondence E_(∞,T) (Bohr ↔ quarter-Γ Calderón) | 122 P122_D_SPECIFICATION | 1H `122 P122_D_SPECIFICATION` (OPEN); 8H `R160_S3 L6/§5#14` | N | Y | Y | must add input independent of log p, p^{-1/2}, N, Γ | **OPEN**: typed contract, never built | The Bohr carrier uses all primes; the contract is not E1 by construction; it is a window-to-Γ transmission, not global in X |
| 17 | Mollifiers (Levinson–Conrey, Jensen, Thm Γ_f, Thm H) | 159 G2_B10 | 3D `159 G2_B10` | Y | N | Y | F3:DH, F3:Epstein (Thm H) | Thm H never audited by the panel | Proportions of zeros on the line are global (Littlewood / argument principle) and not E1; DH and Epstein defeat them, so multiplicativity is not used |

### One of three

| # | mechanism | phases / files | grid ids | (i) | (ii) | (iii) | wall | residue | why |
|---|---|---|---|---|---|---|---|---|---|
| 18 | Kreĭn extension indeterminacy KEP(T) | 155 thm:KEP3 (Paper 46); 157 A6 | 7F `155 thm:KEP3`; 7A `phase 155 r5`; 7E `R160_S5 §2.1#6` (OPEN) | Y | N | N | E1 (RH ⟺ indeterminate ∀T; unconditional to 0.8) | Nevanlinna parametrisation of 𝔖(T) (7F OPEN); KEP(T_c) solvability (7E OPEN) | Global extension problem, but zero-side only |
| 19 | Global square K_T*QK_T − Q ≥ 0 | 120 C.1; 121 F2 | 7A `phase-120 (C.1)`; 1A `arcs I-II / phase 120` | Y | N | N | E1 | (C.1) open, equivalent in force to RH | Global in the witness; window datum Q only |
| 20 | Theorem M: λ^A_T ≤ exp(−e^{(2−ε)T}) | 159 G2_B6_R2 | 3A `159 G2_B6_R2` (PROVED-TOOL, M;W8) | Y | N | Y | M | tool: the margin at the witness → 0 | The witness's bottom eigenvalue is global; the theorem "holds verbatim for every falsifier", so no atomic coupling. It is an obstruction, not E1 |
| 21 | de Branges window time T*(λ) | 159 G2_B5 | 7D `159 G2_B5` | Y | N | N | E1 (= thm:KEP3(b), Suzuki) | Thm Q# unaudited | Global canonical system; restatement |
| 22 | Canonical systems, Nehari norms of the Suzuki kernel, echo law | 159 G1_B8 | 3D `159 G1_B8` | Y | N | N | E1; F4 | Echo Thm K (local exclusion, mod Romanov) | Global Hamiltonian; Herglotz / Lagarias restatement |
| 23 | Isodivisor deformation E(1+εK_F) (Hadamard + Paley–Wiener) | 121 P121_ISODIVISOR | 7D `121 P121_ISODIVISOR_DEFORMATION_NO_GO` | Y | N | N | F1; new zeros O(R) invisible to RvM | none | Hadamard-global on the divisor; zero-side only (an M_m-type object) |
| 24 | Phase-65 RH-PROOF (Vitali/Montel strip crossing) | 137 R137_007 D.0 | 7E `137 R137_007 D.0` | Y | N | N | E1; fork bound / identification | none (refuted, both versions) | Normal-family globality; no prime input |
| 25 | Bordered entire Weil form Σ(T)=B−X*L⁻¹X (shielding) | 124 P124_013 | 7A `124 P124_013` | Y | N | N | E1; F3:Ξ_a | shielding observed for Ξ_a | Global Schur complement; RH-strength |
| 26 | Volterra relative determinant / quasinilpotence | 121 | 8D `121 P121_VOLTERRA_...` | Y | N | N | E1 (global-square force) | none | Global causal determinant |
| 27 | Polar capacity 𝔊_T across T | 156 polarcap | 1E `156 polarcap` (PARTIAL) | Y | N | N | E1 | M4 residual E5 → R162_703 | Across all T, but the 2×2 capacity is a window datum |
| 28 | Dual certificates, Thm D1/O, Theorem Z (flat-top tests) | 154 R154_012; Paper 46 | 7A `154 R154_012 Thm D1/O`; 3A `phase 154 Paper 46` | N | N | N | E1 (Z = explicit formula on flat-top tests); finZ, M | none (strong duality, never attained) | Literally (1.1) on a test |
| 29 | Centered Chebyshev channel dΨ−dx | 114 D.260-262 | 6F `phase-114/D.260-262` (PARTIAL) | N | Y | N | E1 | regularized residual exact, sign open | Ψ at all heights, but linear: the Mellin–Stieltjes of the explicit formula |
| 30 | Gaussian prime correlation S_T(τ) at one frequency | LP-152 (Doc 152) | 6F `R160_S2 §3.2 LP-152` (OPEN, E1) | N | Y | N | E1 | needs an upper bound at one frequency | Pair correlation of Λ is non-linear, but it is an exact identity on one test |
| 31 | Bohr–Jessen twist, one-generator rigidity | 159 G2_B7 | 6E `159 G2_B7` | N | Y | N | Haar-null on twist torus; zero-side input violates premise 3 | none | LI over all primes, but the twist average is the archimedean form |
| 32 | Hermitian squares / separated square / twist obstruction | 159 G2_B3 | 2C `159 G2_B3` | N | N | N | F2; twist Haar average = archimedean form | none | Landau-converse restatement |
| 33 | SOS / Positivstellensatz certificates | 159 G2_B4 | 2C `159 G2_B4` | N | N | N | E1; Thm R; Baker no-go | none | Covariant SOS = zero-side SOS |
| 34 | Lee–Yang / Pólya–Schur local certification (Thms L, L′, L″, D) | 159 G2_B8 | 4A `159 G2_B8` (OPEN); 8A `Thm L″` (OPEN) | N | N | Y | unaudited; numerics uncertified | **OPEN**: audit of T_loc ∈ [½log3, 0.5925] | Euler-factor-local threshold, so window/local; not E1 |
| 35 | Structure vs randomness / resonators, Prop P | 159 G2_B1 | 4A `159 G2_B1` | N | N | N | F3 comb models, deletion; F4 | none | Class-level: holds for finmod combs |
| 36 | Bootstrap in T, sieve flow Ψ, Thm U | 159 G2_B2 | 8E `159 G2_B2`; 8A `Thm U` (OPEN, unaudited) | N | N | N | E1 (flow on the orbit is the identity) | Thm U conditional | Invariants are functionals of ζ(½+it) |
| 37 | Jump calculus, Thm R′; graded Weil converse | 159 G2_B9; SYN 2.2 | 7F `159 G2_B9`; 7E `159 SYN 2.2` | Y | N | N | E1 (κ=0 ⟺ RH, von Koch–Landau) | R′ is a tool | Rigidity at T=∞ is global; restatement |
| 38 | Probabilistic ladders (Cauchy damping, Gaussian heat ladder) | 159 G1_B10 | 8E `159 G1_B10` | N | N | N | E1; OT-4 | none | Weil via a PD semigroup |
| 39 | Sz.-Nagy dilation bridge; numerical motive M_Z; Prop BL | 159 G1_B6_R1, G1_B7 | 7H `G1_B6_R1`, `G1_B7`; 8H `Prop BL` (OPEN) | Y | N | N | E1; tail wall | Prop BL Z[Q/Z] unaudited | Global dilation; restatement |
| 40 | Prime-local operator carriers, DK_α, III₁ law; FF gap/flat/Euler walls; Construction 9′ | 159 G1_B2, G1_B3_R4-5, G1_B6_R2 | 4H `G1_B2_R3-R5`; 8H `G1_B3_R4-R5`, `G1_B6_R2`, `G1_B1_R5` (OPEN) | N | N | Y | Hardy exclusion; OT-5′ false (own Thm A) | non-ergodic DK_α (unaudited) | Obstructions on prime-local carriers; not E1 |
| 41 | Sharp tail wall W# (Arakelov / Faltings–Hriljac) | 159 G1_B4_R4 | 4H `G1_B4_R4` (PROVED-TOOL) | N | N | Y | tail-factorizable Frobenius carries ≤1 zero per summand | tool | Σ‖S_p‖⁻²=∞ threshold; obstruction, not E1 |
| 42 | G1 composite wall: carrier entangled, non-algebraic, non-covariant | 159 SYN 1.2 | 8H `159 SYN 1.2` (PARTIAL) | Y | N | N | Lemma T(≤) fails OT-3/OT-4 | specification of an admissible carrier | Global requirement; no coupling built |
| 43 | Borger/Witt/Bost–Connes, scaling site, Deninger suspension | 159 G1_B1, G1_B2_R1-2, G1_B5 | 4H `G1_B5_R3-R5`, `159 G1`; 8H `G1_B1_R3`, `G1_B2_R1-R2` | N | N | N | OT-5′ walls; T5; suspended H¹=0 | none | Only the polar pair survives |
| 44 | Function-field transport (q→1 Bochner cone, Bombieri–Stepanov) | 159 G1_B9 | 8G `159 G1_B9` | N | N | N | F3:function field; E1 | none | Admissibility ⟺ RH |
| 45 | FUP / Dolgopyat on the Gauss map; Mayer operator via Lewis–Zagier | 152 R152_005 A; P152.1 | 3H `152 R152_005 A`; 1H `152 P152.1` (OPEN) | N | N | N | abscissa ½ = MW-2 dynamical; β=¼ is RH | P152.1 formulated, never built | Dynamical abscissa restatement |
| 46 | Berkovich tree / line difference kernels | 152 B; 157 R157_005-006 | 8H `152 R152_005 B / 157`; 2H `R160_S5 §2.1#5` (PARTIAL) | N | N | N | E1; F3:Beurling | energies outside 𝔄⁺ (Chinburg–Rumely unread) | Per-branch blind; restatement within 𝔄⁺ |
| 47 | Theorem A cross term: D.12-α at ({∞,2,3}, log 2) | 153 R153_005; Paper 46 | 7A `153 R153_005 Thm A`; 4A `phase 153 Thm A`; 4E `R160_S4 §5#1` (OPEN) | N | N | N | F3:Ξ_Q, F3:Beurling; window | (P153.2): ζ vs Ξ_Q/Beurling; T-uniform use never attempted | Sign-carrying, but inside the window and only at two primes |
| 48 | Single-pair detection / b-needle; Slepian / box | 153 R153_010, R153_014-021 | 7A `153 R153_010`; 3A `153 R153_014-021` | N | N | N | measures concentration; Platt–Trudgian; Bochner | none | Zero-side, finite |
| 49 | Explicit certificate Theorem C(½log3); two-prime window 0.58 | 154; R154_030 | 6A `154 Thm C(½log3)`; 3A `154 R154_030` (OPEN numerics) | N | N | N | W8; window | off-machine LP never run | Window-only (killed by f_t) |
| 50 | Lattice certificate classes TK/N/N′, AL→AL′ | 155 | 5A `155 TK/N/N′`, `155 thm:AL→AL′`; 3A `phase 155 TK/N/AL′` | N | N | N | TK ceiling; Θ(1/M) | AL′ loss open | Finite lattice ν, window |
| 51 | Classical prime estimates deciding a window (PNT, ZFR, density, sieve) | 155 thm:finmod / cor:void; 157 | 3A `155 thm:finmod/cor:void`; 3A `R160_S5 §2.1#2-3` | N | N | N | F3:deletion, F3:finmod | none | Window-only: this is the f_t theorem |
| 52 | Sub-comb / prime-by-prime positivity | 155 thm:SC | 2A `155 thm:SC` | N | N | N | each local Q_p indefinite | none | Prime-local |
| 53 | Archimedean negative index one (H1), rank-one Schur; even Schur S_even | 155 cor:H1; P2 | 3D `155 cor:H1` (PROVED-TOOL); 6D `155 P2` (superseded) | N | N | Y | arena ≥12 modes | none | Archimedean structure only; not E1 |
| 54 | Nodal/Sturm arena; prolate Thm P n₋ ≤ 5/7/8 | 155 thm:arena, Thm P | 8D `155 thm:arena/P8`, `155 Thm P`; 8D `R160_S4 §2.D#47` | N | N | N | not PF₂; count stops at 5 | semigroup PF₂ for t≥1 open | Finite mode arena: the node-jet locality excluded by (i) |
| 55 | Uniform margin / upward induction in T | 155 thm:margin; 157 O1 lem:monoT | 3E `155 thm:margin`; 8F `157 O1`; 8E `R160_S5 §2.1#1` | N | N | N | M; E1 (∀T λ≥0 = Weil on C_c^∞) | none | Filters, no object |
| 56 | Li/Keiper, Báez-Duarte as flat-top duals; termwise positivity in zeros | 155 cor:Li, lem:Rrig | 1A `155 cor:Li`; 7C `155 lem:Rrig` | N | N | N | E1; no flat-top w with ŵ≥0 | none | Zero-side only |
| 57 | Reverse engineering from zeros / row D for Z_1000 (finZ) | 155 R155_018; Paper 46 §7 | 7A `155 R155_018 finZ` | N | N | N | W8 (finZ) | none (theorem: row D intrinsically infinite) | Zero-set-only (the M_m side of §0) |
| 58 | Per-window converse λ^A≥0 ⟹ λ^W≥0 (2×2 polar capacity) | 156 R156_005 | 2A `156 R156_005 cor:convfail`; 2A `phase 156` | N | N | N | F3 comb models | none | Window-only |
| 59 | Alignment-band lower bound; Problem B (canonical s=½); Problem A | 155 R155_053, prob:A/B | 6A `155 R155_053 P6`, `155 prob:B`; 3A `155 prob:A` (OPEN) | N | N | N | E1 (per window ⟺ λ^W>0; Problem B is RH) | **Problem A OPEN** (only ceilings proved) | Window statements |
| 60 | MW-5 mechanism search (61 candidates F1–F5); uniformity-in-T | 157 R157_002 | 8H `157 R157_002 61 rows`; 6A `157 O3 lem:degen` (superseded) | N | N | N | E1; T1; T5 | MW-5 not excluded; o-minimal/Pila–Wilkie (5H OPEN, desk-EXCL only) | Classification of candidates, not a mechanism |
| 61 | Unitary routes over non-abelian fields (S₃ falsifier) | 158 R158_004/006 | 1G `158 S₃ falsifier`; 1G `R160_S5 §2.2#11` | N | N | N | F3:ζ_K(S₃) Jordan chains | none | Field-uniform; no atomic Q-input |
| 62 | Canonical class K (Pólya), affine duality σ_K, Hodge-index transfer Thm 12.3 | 135 R135_007; Paper 47 | 1H `135 R135_007`; 8H `135 P47 Cor 12.4a`; 8H `phases 135-140` | N | N | N | E1; F3:Ξ_a; needs h⁰ (a),(b′),(c), unsatisfiable (Thm 19.25) | none | The Pólya realisation deletes the Λ weights |
| 63 | Meta-theorem: sign = polar/Frobenius coupling | 136 §2 | 8H `136 PHASE_136 §2` (PROVED-TOOL) | N | N | N | — (meta) | it states (ii) as a necessity | Prime-only or archimedean-only positivity only; the coupled statement is RH |
| 64 | Cartwright tropical Hodge index at chart level | 136 S5 | 2H `136 PHASE_136 S5` (OPEN) | N | N | ? | never run | **OPEN, unbuilt** | Chart-level, so local; not evaluated |
| 65 | CC Δ→Σ transfer Q=Π; h⁰_Z(mK) Frobenius lattice count | 137 D.13, D.11 | 1H `137 D.13`; 5H `137 R137_007 D.11` | N | N | N | E1; growth (log m)^{3/2} vs ¼m² | D.13-γ open | Window identity; clause (c) fails |
| 66 | Detecting cones (polar block, Pólya cone, Khovanskii–Teissier, zero-datum cone 𝒫) | 138 R138_004/005 D.15–D.17 | 1A `138 R138_005 D.15`; 2A `138 D.16-17`; 7A `138 D.16-γ` (OPEN) | N | N | N | Hodge identity holds identically; PNT error | D.16-γ repaired form, never attempted | No ruling-side detection |
| 67 | Equimodularity \|p−½\| as sign; method theorem T1 | 138; 139–150 T1 | 1G `138 T1 equimodularity`; 1G `R160_S4 §2.A#11` | N | N | N | T1; F3:ζ_K | T1 re-read: field-uniform proofs admissible | Every ζ_K is equimodular |
| 68 | Axiom-only derivations A1–A6+A2⁺; method theorem T2 | 139 R139_005 | 8G `139 R139_005 T2` | N | N | N | T2; F3:Epstein, Ξ_Q | proof must use A3 and one of A7/A8/A9 | Constraint (tool), not a mechanism |
| 69 | Frobenius square / tensor h⁰_□; Pólya realization r(Frob_n)=τ_{log n}(2K) | 140 R140_005, D.23.4-6 | 4H `140 R140_005`; 6H `140 D.23.4-6`; 4H `R160_S4 §2.A#17` | N | N | N | (b′) fails; collapse to NS(P¹×P¹) | none | Deletes the weights |
| 70 | 2-homogeneous trace functionals Ψ(t_n); h⁰_RR⁺ (b′)⁺ | 141 D.27.5, R141_005 | 6A `141 D.27.5`; 7H `141 R141_005` | N | N | N | E1 | none | (c) ⟹ RH |
| 71 | Frame defect theorem (no h⁰ with (a),(b′),(c)) | 142 R142_005 Thm 19.25 | 8H `142 R142_005` (PROVED-TOOL) | N | N | N | s₁=0.99846<1 | tool | Also true in the function-field model |
| 72 | Trace-positive cone B4, fixed index (P_m), sparse cone | 143 R143_005, 144 R144_005 | 7A `143 D.34`, `144 §D.40`; 8H `R160_S4 §2.A#8` | N | N | N | E1 (one ray tF+K kills each weakening) | none | Each weakening ⟺ RH |
| 73 | Function-field model of the frame; bigness clause | 145 R145_005 | 8G `145 R145_005`; 8H `R160_S4 §2.A#13` | N | N | N | F3:function field; E1 | none | Bigness = RH |
| 74 | Degree form on Z⟨Frob_n⟩; Galois ring Z[G] | 146 R146_005; 147 R147_005 | 4B `146`; 5G `147 D.55.9′`; 4H `R160_S4 §2.A#14-15` | N | N | N | F3:Ξ_a; radial collapse | none | Zero-blind, indefinite; the χ=1 slot is 𝓔^∞ |
| 75 | Mixed effectivity Φ(y/x)−φψ (tropical) | 148 R148_005 | 2H `148 R148_005` | N | N | N | max-plus shadow = 𝓔 | O-148.2 = MW-5/OT-5′ (8H OPEN) | Support constant unchanged |
| 76 | T4 polar/entire classification; T5 single-fibre extraction | 150 R150_005 | 3A `150 T4`; 3G `150 T5` (PROVED-TOOL) | N | N | N | partial-sum bound ⟺ zero bound; trivial 𝔅^{1/2k}≥L | tools | Method theorems |
| 77 | Nonnegative families supplying a Deligne a-priori pole (T6 family form) | 151 R151_005 | 2G `151 T6`, `Paper 47 T5 (141-149)` | N | Y | N | abscissa ≥2kβ_max; T5 | O-151.4 (row 8) | Uses Λ≥0 non-linearly, but the outcome is only an abscissa (a pole at the boundary) |
| 78 | Rows A–C labels; norm-type invariant (R5); panel target | 123–134 | 7A `133 PANEL_3`; 8H `128 D128_004`, `134 R134_007` | N | N | N | E1 (target ⟺ RH) | none | Not row-D mechanisms |
| 79 | Phase 121 package: Tate current, collar, F2 conormal jets, Rees half-lift, U(1,1) Kreĭn flux | 121 | 1B/6B/7B/7C/8B/8H/4B `121 P121_*` | N | N | N | F1/F2; universal conormal model E=z, K=c | **L4 Kreĭn-flux law OPEN** (8H) | Local node jets: excluded by (i) by name |
| 80 | Phase 122 gates R/S, Gate R H^{1/2}, Green complex, reciprocity, Γ–Euler cocycle, divisor commutators | 122 P122_* | 3A/4A/4H/5H/1H/7D/7A `122 P122_*` | N | N | N | F3:Ξ_a; E1; constant flux | none | Both gates fail for Ξ_a |
| 81 | Phase 124 direct first contact (window variation, collar, virial, support leakage) | 124 P124_004-014 | 3B/2B/8A `124 P124_*` | N | N | N | F1; F3:Ξ_a | none | Collar-local |
| 82 | Phases 111–120 pre-row-D: Schwartz admissibility, effective cone D_f, D/rad Hodge index, RR ansatz χ(D)=D²/2, Feshbach ½log5, semilocal Sonin, log-Schur angle, Γ–Tate c_N, A_T≥0, separators P0/P1/P2 | 111–120 | 1H `phase-111/111_99`; 2H `phase-112/112_99`; 7H `phase-113/*`; 3A `phase-114/D.172,200`; 2A/8D/8H `phase-115/*`; 3A `phase-116`, `phase-117`; 7A `phase-118`; 6G `phase-119`; 4D `phase-114/D.244` | N (RR ansatz: Y) | N (P0–P2: Λ≥0 but F3:Ξ_a/DH) | N (RR ansatz: open, but grid E1) | E1; F3:Ξ_a; numerics; unitarity obstruction | **RR ansatz χ(D)=D²/2 OPEN** (7H; implies RH, never attacked) | Semilocal or window; the RR ansatz is the only global item and has no prime coupling |

(Rows 79–82 group several grid entries that share the same verdict. Every grid route id from phases 111–159 is covered by some row.)

## Final list grouped by pair

**(i)+(ii), failing (iii): global and atomic, but E1.** These are the "object" routes. They hold the full Euler product inside a global factorization or spectral realisation, and their positivity is the Weil criterion.
1. Wiener–Hopf 𝒯=A*A / D_Euler (136 S6; 1A)
2. Sharp Douglas gate / prime-power-birth contraction (114 D.170, 120 P3; 8A)
3. Adèle class space as MW-5 object (158 R158_002/005; 1H, 7H)
4. Deninger/Serre axioms D1–D3, Lemma T, laminated carrier (158 R158_001; 8H; open piece = AL-K polarisation)
5. Meyer H¹ / H¹_alg density (158 R158_006; 7H; density OPEN)
6. Euler determinant lines / Contou-Carrère / Bohr assembly (122 P122_013-017; 4H)

**(ii)+(iii), failing (i): atomic and non-E1, but blind to the node set.** These are the "arithmetic" routes. They really use Λ≥0, multiplicativity or integrality at all heights, but they act pointwise, per zero, or on the abscissa, and never on X.
7. dlVP / T6 numerator sign (151; 2G, 3A), capped by M
8. O-151.4 summand-vs-numerator axis (8C, OPEN)
9. Landau lemma D.34.5 (143; 4A, tool)
10. Beurling T3 additive structure (150; 2G, conditional on H-DMV)
11. Deligne extraction on the additive pencil D.59 (149; 6G, 7G), T5 / k-tuple
12. Rationality wall Thm R/R′, six exponentials (159 G1_B4_R5; 5H, W8)
13. BRS Theorem P, no pure prime–zero Fourier pair (159 G2_B6_R4; 7B, β-blind)
14. Identity-level Λ=μ*log (157; 6B, OPEN)
15. Non-local Tauberian with LI input, GAP-157.A (4F, OPEN)
16. Relative correspondence E_(∞,T) (122; 1H, 8H, OPEN, unbuilt)

**(i)+(iii), failing (ii): global and non-E1, but not atomic.**
17. Mollifiers / Levinson–Conrey proportion (159 G2_B10; 3D), defeated by DH and Epstein (Thm H, unaudited)

**Reading.** The 2-of-3 set splits into the two halves that phase 166 says must be joined. The object routes (1–6) have (i)+(ii) and lose (iii) to E1. The arithmetic routes (7–16) have (ii)+(iii) and lose (i). The only (i)+(iii) item (17) loses (ii) to DH. The natural unexplored joins come from pairing an open (ii)+(iii) residue with a global object:
- O-151.4 (row 8), GAP-157.A (row 15), Λ=μ*log (row 14) or E_(∞,T) (row 16),
- with the harmonic-measure phase of G at t_q (R165_201 Thm 2),
- rather than with a factorization, which falls to E1.

The corpus never attempts such a join for phases 111–159. Any relaunch must still name the wall it evades, per §0.
