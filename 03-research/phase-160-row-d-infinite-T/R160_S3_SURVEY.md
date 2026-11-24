# R160_S3 — Survey S3: phases 91–133 and Papers 31–45 (rows A, B, C on the declared carrier)

Surveyor S3, phase 160. Survey only: no new theorem, no label change, no paper edited.

**Scope read.** `03-research/phase-91-*` … `phase-133-abc-review-panel` (README, closure, ledger or summary of
every phase; the labelled-theorem memos listed in the text), `04-papers/31-*` … `45-*` (abstracts of 31–41; the
labelled theorems of 41, 42; `main.md` of 43, 44, 45, read along the verdict ledgers, the definitions and every
theorem cited below), `NO-GO-LIST.md` §VIII, the phase-136 maps `MAP_3_PHASES_061_110.md` and
`MAP_4_PHASES_111_135_AND_PAPERS.md` (used as an index and then checked against the memos),
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-REDUCED-STATEMENT.md` §§1–4 and Paper 46
(`def:W`, `def:PD`, `eq:W`, `eq:nuw`, `P_T`) for cross-checking definitions.

**Conventions of this survey.**
  NUMERIC-UNCERTIFIED (float computation only) / CERTIFIED (interval arithmetic).
* Forms. `[prim]` = the primitive form `A_T|P_T` (Paper 46 `eq:form` on `P_T`); `[compl]` = the complete Weil
  form `W_T` on `L²(I_T)` (Paper 46 `eq:W`); `[full-a]` = the truncated form `𝔞_T` on all of `L²(I_T)` with no
  polar term (this is what phase 115 calls `A_T` on the full space); `[struct]` = no sign statement.
* The corpus uses three sign conventions for the same object (Paper 45 §1.4, Lemma 1.3). Throughout:
  `I_∂ ≤ 0` on primitive radial classes (rows A–C) ⟺ `𝔞_T ≥ 0` on `P_T` (Paper 46) ⟺ `B_nuc ≤ 0` on `𝒯⁰`
  (Paper 42). See the dictionary D1 in §6.

---

## 0. Summary in ten lines

1. Phases 91–106 are the Li/`Ω₇` and Connes–Consani–Moscovici (CCM) finite-section programme: every target it
   reached is either proved equivalent to RH or killed by a no-go. Nothing in it proves a sign past `T = log 2`.
2. Phases 107–113 rebuild Weil's four rows over `Spec Z` from the back; phase 113 proves "row (d) is RH" (Hodge
   index on `H^⊥` ⟺ RH), and proves there is no lattice inside the Schwartz-data class (O1–O3).
3. Phases 114–122 attack row (d) directly (Douglas gate, Green identity, Sonin/semilocal, scattering, negative
   witness, determinant lines). Every route ends at one of a small number of proved walls (§2).
4. Phases 123–133 build rows A, B, C on one declared carrier (Papers 43, 44, 45). After an audit that withdrew
   the labels (phase 128) and a rebuild (129–132), rows A, B, C are `WEIL-STRENGTH-COMPLETE` on the declared
   carrier (fixed finite chart; the colimit as additional structure; invertible sector), with accepted
   amendments A.6, A.8, B.4, B.7. Panel 3 of phase 133 records that the *name* overstates the specification.
5. What rows A–C prove about the zeros of ζ: **nothing** (all three papers say so).
6. What rows A–C give row D: an exact chain `row-D target ⟹ RH` (Paper 45 Thm 9.6 + Thm 10.4), with the explicit
   formula proved in the repository (Thm 9.4). Together with Weil's criterion (CLASSICAL) the target is EQUIV.
7. What rows A–C deny row D: every naive Hodge-index shape (Paper 43 Thm 14.1; Paper 44 Thm 8bis.4a, 8bis.2;
   `I_A(Frob_n,Frob_n)` undefined; rulings are a quotient, not a subobject; no `h⁰`).
8. Proved signs for ζ inside my scope: `[prim]` for `0 < T ≤ log 2` (Paper 42, CERTIFIED); `[compl]` for
   `T ≤ ½log2` (Yoshida, Bombieri: CITED in 115_03). Nothing beyond.
9. The strongest new results in my scope: Paper 45 Thm 10.4 (primitive tests suffice), Paper 43 Thm 9.8
   (`𝓝 = 0`), Paper 44 Thm 8bis.1e (Weil kernel = Gram form of `Frob ⋆ Δ^rad`), phase 120 Thm 2.1 (all positive
   lifts are one Douglas factorization), 115_17 Prop 3 (unitarity obstruction) and Paper 41 Thm `doob`
   (RH ⟺ one sharp Poincaré inequality).
10. The unfinished items that later phases did not close are listed in §5. None of them is known to avoid all the
    walls.

---

## §1 What was done (by phase / paper, one line each)

Paths relative to `03-research/` unless stated.

### Phases 91–100: the bordered-determinant route to `Ω₇` (Li–Keiper positivity `λ_n ≥ 0`)
| phase | one line | file |
|---|---|---|
| 91 | Line-response equation `C_t v̇_t = Q_t H_P^in v_t`; an inverse-free formula is equivalent to a coboundary; the Euler gauge leaves a derivation defect | `phase-91-kato-coboundary-equivalence/PHASE_91_CLOSURE.md` |
| 92 | Projectivize the full Feshbach cluster, `G_t = N_t/det F_t`; removes dominance/matched-width hypotheses | `phase-92-cluster-adjugate-projectivization/PHASE_92_CLOSURE.md` |
| 93 | PROVED `DIRECT-BORDERED-ANCHOR ⟹ SR-SAFE ⟹ Ω₇ ⟹ RH` (Hurwitz); the anchor has full `Ω₇` strength | `phase-93-direct-bordered-anchor/E93_002_DIRECT_CLOSURE_THEOREM.md`, `PHASE_93_CLOSURE.md` |
| 94 | Inverse-free cofactor form `N = det M − h^T adj(M) b`, rank-two displacement; no termwise Euler identity | `phase-94-global-cofactor-cell-current/PHASE_94_CLOSURE.md` |
| 95 | Moving level absorbed as a branch of `det(H_t − μI) = 0`; Jacobian formula | `phase-95-characteristic-jacobian-current/PHASE_95_CLOSURE.md` |
| 96 | Jacobian expanded as an exact von Mangoldt sum; remaining scalar = the open target | `phase-96-determinantal-prime-response/PHASE_96_CLOSURE.md` |
| 97 | Prime sum collapsed into one trace commutator `Tr(K H_P)` | `phase-97-euler-sensitivity-commutator/PHASE_97_CLOSURE.md` |
| 98 | Exact Fourier-shell split of the commutator (four crossings) | `phase-98-sensitivity-shell-split/PHASE_98_CLOSURE.md` |
| 99 | Adjugate sandwich against the Γ–Euler boundary sources | `phase-99-adjugate-boundary-sandwich/PHASE_99_CLOSURE.md` |
| 100 | The normalized characteristic adjugate is `−Π_t`; it is the chain-rule term, not a new source | `phase-100-characteristic-cofactor-factorization/PHASE_100_CLOSURE.md` |

### Phases 101–106: `Ω₇` campaign, direct A1, CCM/Suzuki global star
| phase | one line | file |
|---|---|---|
| 101 | Reduces the direct route to `LOCAL-COVARIANT-IDENT` on one interval (⟹ `Ω₇`); Stieltjes/heat/beta-mixture/Pearson coordinates; 102 frozen stop-rules | `phase-101-covariant-bordered-current/PHASE_101_LEDGER.md` |
| 102 | `Ω₇` campaign (~300 notes): A0 tail theorem, A1 signed core, Toeplitz/Herglotz/de Branges/Fejér gates; zero-side Li closure | `phase-102-omega7-closure-campaign/README.md`, `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md` |
| 103 | Direct A1 reduced to one Chebyshev–Laguerre inequality; ~40 theta/Jensen/Selberg no-gos; certified strong margin `21 ≤ n ≤ 149`; RH-conditional closure for `n ≥ n_eff` | `phase-103-direct-a1-closure/README.md`, `103_51_*`, `103_58_*` |
| 104 | ~80 positivity mechanisms for A1 closed by stop-gates; Deep limit `Ω_X → 0 ⟺ RH` | `phase-104-unconditional-a1-closure/PHASE_104_CLOSURE.md` |
| 105 | A1/Deep limit visualized; PROVED: an off-line zero forces exponential growth of `λ_n` | `phase-105-a1-geometry-and-deep-limit/README.md`, `105_02_OFF_LINE_ZERO_EXPONENTIAL_THEOREM.md` |
| 106 | ~210 notes testing a positive Hilbert realization `Θ* = 1 − Θ`, `det(s − Θ) = e^{a+bs}ξ`; no-go 106_00; parity theorem 106_11; centered prime–Γ square 106_17; Picone one-atom falsifier 106_19; charged-Tate branch closed by 106.205 (a.c. spectrum); cyclotomic resultants give no diagonal (106.210) | `phase-106-global-modular-star-audit/README.md` |

### Phases 107–113: Weil's four rows reconstructed backwards
| phase | one line | file |
|---|---|---|
| 107 | Reverse-engineer a finite-support Lefschetz divisor with `−D̄_f²·H̄ = 𝒬_W(f)`; finite local packets fail on real elliptic curves (Tamagawa `c_p`); 107_239 corner pairing; 107_240 scalar Picard descent no-go; 107_241 finite-rank no-go; 107_242 Deninger–Morishita no-go | `phase-107-arithmetic-lefschetz-reconstruction/README.md` |
| 108 | Row (a) staged 0–7 over `Z`: Stage 1 bridge, Stage 3 assembly `= −ζ'/ζ`; Stage 2 and 5 negative; symmetrization collapse 108_91; archimedean fibre cannot be a subobject 108_42 | `phase-108-row-a-construction/108_99_PHASE_108_SUMMARY.md` |
| 109 | One-sided pairing `B(f,g) = ΣΛ(n)f(n)g(n)` exists; its radical is prime-power-determined for every kernel on prime powers (109_04 Thm 1.1) | `phase-109-one-sided-pairing/109_99_PHASE_109_SUMMARY.md` |
| 110 | ξ-divisible ∩ compactly supported = {0} (Thm 110.2.4), carried by Γ, not by ζ | `phase-110-principal-xi-divisibility/110_99_PHASE_110_SUMMARY.md` |
| 111 | On Schwartz data every piece of the corner pairing converges; `𝔗` on Schwartz data not constructed | `phase-111-schwartz-admissibility/111_99_PHASE_111_SUMMARY.md` |
| 112 | The effective cone `f ≥ 0 ⟺ u_f` convex; satisfied only formally; no `h⁰` | `phase-112-effective-cone/112_99_PHASE_112_SUMMARY.md` |
| 113 | Frobenius `*`-algebra `(D/rad, ⋆, *, τ)` with zero-free trace, rulings, degree, effective cone, `K = 0`; `rad = χ`-ideal; (E°) ⟺ RH; Hodge index on `H^⊥` ⟺ RH; d3 impossible inside `D`; O1–O3 | `phase-113-the-trace-on-schwartz-data/113_99_PHASE_113_SUMMARY.md`, `113_15_THE_FOUR_ROW_LEDGER.md` |

### Phases 114–122: row (d) attacked directly
| phase | one line | file |
|---|---|---|
| 114 | Rows (a)–(c) written in Paper 42; row (d) reduced to the sharp Douglas gate (D.170), exact Green/defect identities, joint residual `𝓡_{N,ε}` (D.262); D.244 Lorentzian inertia `(1,|S|−1)`; method rule "no finite-rank or per-prime local construction" | `phase-114-closing-the-four-rows/PHASE_114_CLOSURE.md` |
| 115 | Mixed class / Green extension; semilocal Sonin route (115_09); Sonin trace identity cannot be exact (115_16 Prop 2); audit of external notes v3–v10 with the unitarity obstruction (115_17 Prop 3), Krein index no-go, hyperbolic polar defect (Props 5–7) | `phase-115-the-mixed-class-and-the-green-extension/115_17_*.md`, `115_16_*.md`, `115_09_*.md` |
| 116 | Logarithmic Schur Angle Conjecture `ρ_N ≤ 1/(20 log N)` extracted (candidate) | `phase-116-the-logarithmic-schur-angle-conjecture/README.md` |
| 117 | Conjecture falsified; Γ–Tate source comparison `c_N < 1` (decays like `(log N)^{−0.6}`) — NUMERIC-UNCERTIFIED, one-sided | `phase-117-the-transfer-comparison-measured/README.md` |
| 118 | `⟨A_T F,F⟩ = Σ_ρ h(γ_ρ)` on primitive `F` ⊂ `L²(I_T)`: "A_T ≥ 0 ∀T" **is** Weil positivity (EQUIV); log 2 certificate replayed; scattering ansätze refuted | `phase-118-the-exact-threshold-inequality/PHASE_118_CLOSURE.md` |
| 119 | Coefficient separator P0/P1/P2_norm distinguishes ζ from Davenport–Heilbronn but not from `Ξ_a = ξ(s+a)ξ(s−a)` | `phase-119-what-a-finite-compression-certifies/RESULTS_119_SEPARATOR.md` |
| 120 | Zero-residual Green identity `−B_nuc,T = ⟨QK_TE_TF,K_TE_TF⟩ − ⟨QE_TF,E_TF⟩`; common-failure Theorem 2.1 and the locality–phase–sign trilemma; global square (C.1) open | `phase-120-global-polarization/PHASE_120_CLOSURE.md`, `P3_COMMON_FAILURE_ARCHITECTURE.md` |
| 121 | Negative-witness rigidity: first-contact normal form, critical defect `D_T^crit`, open arrow F2 (equivalent in force to the global square); `A_T` corpus atlas (13 exhausted families) | `phase-121-negative-witness-rigidity/README.md`, `P121_AT_CORPUS_ATLAS.md` |
| 122 | Integrity audit + minimal specification of a row-D object; local Euler determinant lines, semifinite Bohr carrier; two-gate criterion (R, S); two-prime Green complex (DtN = seam norm / log(q/p)) | `phase-122-row-d-integrity-and-construction/P122_D_SPECIFICATION.md`, `P122_028_*.md` |

### Phases 123–133: rows A, B, C on one carrier
| phase | one line | file |
|---|---|---|
| 123 | 126 notes: acceptance specification (Weil-strength = equality of structural burden), semilocal kernel sheaves, Tate realization, local excess RR, finite-place trace `W_p` (P123.042), archimedean `W_∞` (P123.035), log 2 endpoint replay (P123.036); P123.018 adversarial carrier audit; P123.022 (no `C`-linear category carries `Z/p`); P123.060 (diagonal contact = fixed-point complex) | `phase-123-weil-strength-abc/README.md`, `P123_A_ACCEPTANCE_SPECIFICATION.md` |
| 124 | Direct first-contact route; entire-function coordinate and shielding dichotomy (P124.013); shifted-pair falsifier: both gates fail (P124.014) | `phase-124-direct-first-contact/README.md` |
| 125 | Row A campaign (graph sector, half-density dagger, excision, trace-class domain, torsion theory) | `phase-125-row-a-completion/README.md` |
| 126 | Row B: coprime support of the fixed and ramification contacts; `Prim` not monoidal | `phase-126-row-b-completion/B126_004_LEDGER.md` |
| 127 | Row C: polar packet = ruling form; archimedean term as a determinant; closes the `113_07` sufficiency gap | `phase-127-row-c-completion/C127_005_LEDGER.md` |
| 128 | Adversarial audit: all three labels withdrawn; list of what survives | `phase-128-adversarial-audit/D128_004_WHAT_SURVIVES.md` |
| 129 | Row A rebuild: Thm 9.8 `𝓝 = 0` (import-free), Thm 9.13(a), Thm 14.1; label `CONSTRUCTED` | `phase-129-row-a-rebuild/README.md` |
| 130 | Row A closure: rulings in `N_A^dist`, Mittag–Leffler symbol with universal Tate residue, `𝓐_tr`; label granted (R130.005) | `phase-130-row-a-closure/README.md`, `R130_005_FINAL_AUDIT_AND_LABEL.md` |
| 131 | Row B closure (7 rounds): norm class, Frobenius family, `Sh_Z`, two Gram forms, Thm 8bis.4a, `(Wgr)` withdrawn as false, `(H_L)` OPEN | `phase-131-row-b-closure/README.md`, `R131_019_*.md` |
| 132 | Row C closure: explicit formula proved (Thm 9.4), `c = 0` unique (Cor 9.6a), residues (Thm 9bis.2′) | `phase-132-row-c-closure/README.md`, `R132_007_*.md` |
| 133 | Three-member review panel; labels sustained with qualifications; A.8, B.7 amendments accepted; row-D target boxed identically | `phase-133-abc-review-panel/PANEL_SYNTHESIS.md`, `PANEL_3_LABELS_AND_RH_CHAIN.md` |

### Papers 31–45 (`04-papers/`)
| paper | one line |
|---|---|
| 31 | Curvature criterion: RH ⟺ `∂²_σ log|ξ| > 0` on the line off the ordinates; the arithmetic sector `G_ζ` is the wall (EQUIV) |
| 32 | PROVED: ζ is not Stepanov almost periodic on any closed sub-strip of `(½,1)` (band sense) |
| 33 | Off-line energy `I = Σb_j²`; RH = finiteness ∧ purity; unconditional identities; axiomatized no-go for a class 𝔄 of detectors |
| 34 | Survey of the obstruction map; walls W1–W3; no-gos N1–N8 |
| 35 | de Branges/Lax–Phillips colligation; `L1 ⟹ RH`; Kreĭn–Langer index = number of off-line zeros; PROVED `Γ₂ ≥ 0` (CD(0,∞)) for the prime Dirichlet form after Doob conjugation (`thm:CD0`) |
| 36 | Obstruction ledger; ARP-P chain ⟺ RH terminating at `Ω₇`; A0 proved, A1 open |
| 37 | Sixteen positivity attacks on A1 closed with witnesses; the polar factor is signed |
| 38 | Li sequence as FIR system: RH ⟺ eventual nonnegativity of every sliding sum `Y_L(N)` (EQUIV) |
| 39 | CCM/Suzuki cofinal Weil summability; the global limit ⟺ `∂²_z log(φ̂_L/k̂_L) → 0` |
| 40 | Connes proof skeleton: local geometric data realize `Λ(p^k)/√p^k`; the ordinary Hilbert completion has a.c. spectrum, so it cannot be the missing polarization; six terminal formulations, each containing the full sign |
| 41 | Obstruction catalogue (31 entries); Thm `doob`: RH ⟺ `E_K(r) ≥ ½Var_{μ_K}(r)`; principles P1 radical saturation, P2 measure capacity, P3 counterfactual invariance |
| 42 | Arithmetic Lefschetz programme; `thm:infiniterankcontact`; `thm:rowdtrilemma`; CERTIFIED `[prim]` positivity for `0 < T ≤ log 2` (`thm:certifiedendpoints`, `cor:certifiedinitialinterval`); the log-Schur conditional closure withdrawn (phase 117) |
| 43 | Row A (`main.md`, 5552 lines): carrier, `⋆`, `†`, trace `T`, `𝓝 = 0`, Tate boundary, rulings, λ_RR, Thm 14.1 |
| 44 | Row B (`main.md`, 5892 lines): norm class, Frobenius family, `Sh_Z`, two Gram forms, Thm 8bis.4a, (H_L) |
| 45 | Row C (`main.md`, 2401 lines): explicit formula proved, comparison theorem, `c = 0`, residues, Thm 10.4 |

---

## §2 What FAILED, and exactly why (the list memos must not repeat)

Each item: mechanism → the theorem or counterexample that kills it → file. "EQUIV" means the mechanism's
target was proved equivalent to RH (it is not wrong, but it is RH in another coordinate and adds no arithmetic
input).

### 2.1 Targets proved equivalent to RH (restatements, not routes)
1. **Bordered-determinant anchor.** `DIRECT-BORDERED-ANCHOR`, `LOCAL-COVARIANT-IDENT`, `STIELTJES-IDENT` all have
   full `Ω₇` strength; pointwise log-derivative convergence on one safe interval is already RH-strength by
   Pick–Nevanlinna propagation. EQUIV. `phase-93-*/PHASE_93_CLOSURE.md` §3; `phase-101-*/PHASE_101_LEDGER.md` §2 and
   (3.1) item 98.
2. **Half-plane positivity** `Re(ξ'/ξ)(s) ≥ 0` for `Re s > ½`. EQUIV. `phase-102-*/174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md`.
3. **Direct A1** (Chebyshev–Laguerre inequality). Needs square-root cancellation of `Σ_ρ e^{ρu}/ρ²`; the proposed
   uniform zero-sum bound is ⟺ RH (103_11). `phase-103-*/README.md`, `103_07_*`, `103_11_*`.
4. **Deep limit** `Ω_X → 0` ⟺ `B_Blaschke ≡ 1` ⟺ RH. `phase-104-*/PHASE_104_CLOSURE.md` §2 item 5.
5. **Curvature limit** of the CCM ground transform forces RH (106_07); Paper 39's global gate is the same.
6. **Hodge index on `H^⊥`** in `D/rad` ⟺ RH (113_12 Thm 4.1), and effectivity (E°) ⟺ RH (113_10 Thm 4.2/4.3);
   Ansatz A (surface RR with `K = 0`) ⟹ RH, so it is RH-hard (113_12 Thm 5.1). `phase-113-*/113_12_*`, `113_10_*`.
7. **`A_T ≥ 0` for all `T`** (localized primitive operator) is Weil positivity, EQUIV; no operator reformulation
   (factorization, Schur complement, defect operator, scattering) adds arithmetic input.
   `phase-118-*/PHASE_118_CLOSURE.md`.
8. **Rosati completion** of the external v6 route ⟺ RH (via the unitarity obstruction). `phase-115-*/115_17_*.md` §7, §11.
9. **Paper 31** curvature criterion, **Paper 36** ARP-P, **Paper 38** FIR outputs: EQUIV by the papers' own statements.
10. **Row D's boxed target itself** (Paper 43 §14.1, Paper 44 §8bis.4(vi), §10.4, Paper 45 §14.4): ⟹ RH is PROVED
    (Paper 45 Thm 9.6 (9.10) + Thm 10.4); RH ⟹ target is Weil's criterion (Paper 44 Thm 8bis.4(iii), CLASSICAL).
    So it is EQUIV; rows A–C reduce D to RH and not to anything weaker.

### 2.2 Structural no-go theorems (a whole class of mechanisms dies)
1. **All linear positive lifts are one Douglas factorization** (PROVED, phase 120 Thm 2.1): for bounded `X, Y`,
   `‖XF‖² − ‖YF‖² ≥ 0 ∀F` ⟺ a contraction `Θ` with `Y = ΘX` ⟺ `D*D = X*X − Y*Y`. Schur/Douglas, inner scattering,
   de Branges, KYP storage, Hodge/Rosati polarization, Higgs stability, acyclicity, determinant curvature,
   Fock/CAR descent, modular inclusion, entropy Hessian, persistence in the cofinal limit are one terminal
   morphism. Plus the **locality–phase–sign trilemma** (§5 there): local positivity, exact global phase and
   positive primitive descent — every construction got only two.
   `phase-120-*/P3_COMMON_FAILURE_ARCHITECTURE.md` §§2, 5.
2. **Unitarity obstruction** (PROVED, 115_17 Prop 3): a unitary representation of `R_+^×` on a Hilbert space whose
   trace is `Σ m_ρ f̂(ρ)` forces `Re ρ = ½`. "Unitarity is what buys positivity, and unitarity is what excludes
   off-line zeros." Filter: if the scaling group is made unitary, RH has been assumed.
   `phase-115-*/115_17_*.md` §7 (line 351).
3. **Net-index no-go** (PROVED, 115_17 §8.5): each off-line mirror pair adds a hyperbolic plane,
   `(n₊,n₋) ↦ (n₊+1,n₋+1)`; no Fredholm index, Euler characteristic or net Kreĭn signature can see RH. Only the
   absolute positive (or negative) index can.
4. **Hilbert completions with absolutely continuous spectrum** (PROVED, 106.205; Paper 40): the charged pushout and
   its isometric completion have a.c. normalized-scale spectrum, so every equivariant map from the CCM degree one
   kills the critical eigenclasses. `phase-106-*/README.md` (106.205 block); Paper 40 abstract.
5. **Self-adjoint Euler determinant** (PROVED, 106_00): a perturbation determinant of two self-adjoint operators is
   zero-free off the real axis; a finite critical Euler factor has zeros on `Im z = ½`.
6. **Finite rank is impossible** (PROVED): the convolution map of the Weil functional has infinite algebraic rank,
   also on the two-Tate primitive subspace (Paper 42 `thm:infiniterankcontact`, `cor:primitiveinfiniterank`);
   the polarized Weil form has infinite rank (107_241); additive invariants of the full shadow are constant or
   divergent (Paper 43 Thm 7.1(c), Cor 7.5). So Néron–Severi-type finite-rank shadows, finite-rank compressions
   and finite truncations cannot carry the sign.
7. **No Hodge-index shape on row A's numerical module** (PROVED, Paper 43 Thm 14.1): `I_A(F,F) = ∫|F̂|²(T̂ + c)`
   has infinite negative index for every `c`, infinite positive index iff `c > −m`, and for `c = 0`,
   `m ≥ log π + γ + 3log2 + π/2 ≈ 5.372`, so it is indefinite on both sides; `(D_A^prim)^{⊥I_A} = 0`; no
   `D_A`-module splitting of the Tate boundary (Thm 9.13). **Scope:** fixed finite chart, all of `D_A` (unbounded
   support in the log coordinate). It is not a statement about `𝔞_T` on `L²(I_T)`.
8. **Pure Frobenius form fails** (PROVED, Paper 44 Thm 8bis.4a): at every finite chart there is a primitive radial
   `g` with `Q_fin(g) > 0`, because `ω̂_fin(0) = Σ_{p∈S_f}(log p)2p^{−1/2}/(1−p^{−1/2}) > 0`. Colimit version OPEN
   (Remark 8bis.4b(1)).
9. **Infinite genus** (PROVED, Paper 44 Thm 8bis.2, fixed chart): `I_A(G_ε,G_ε) = −log(1/ε) + C_φ + o(1)` for
   normalized radial approximations of `Δ`; Weil's finite `Δ·Δ = 2 − 2g` has no analogue. `I_A(Frob_n,Frob_n)`
   does not exist (`Frob_n ∉ D_A`, Remark 8bis.1c).
10. **Rulings and classes never live in one space with one form** (PROVED): in `N_A` the rulings are a quotient
    (Paper 43 Thm 9.13(a)); in `N_A^dist` they are a subobject but `I_A` does not extend continuously
    (Remark 9.14c″); the scalar analytic determinant is trivial on the rulings (Thm 10.8).
11. **Symmetrization destroys the zeros** (PROVED, 108_91): `ζ'/ζ(s) + ζ'/ζ(1−s)` is elementary and prime-free; any
    construction that sums a functional over the mirror orbit is blind. Rule: pair across the mirror, never sum
    over it.
12. **Pairings on prime-power coefficients never see the zeros** (PROVED, 109_04 Thm 1.1, for every kernel on the
    prime powers; witness `sin(πx)`).
13. **ξ-divisibility on compact support** is empty (PROVED, 110 Thm 110.2.4), carried by Γ.
14. **No lattice inside the Schwartz class `D`** (PROVED, 113): O1 `D/rad` is a complex vector space, so
    `h⁰(nD) = h⁰(D)`; O2 `𝔰(δ_n,δ_m)` diverges because `|(n/m)^ρ| = (n/m)^{1/2}`; O3 no spectral gap,
    `sup 𝔰(f,f)/‖f‖² = 0` on `D° ∖ rad`, not attained; d3 (RR with quadratic term) impossible inside `D`
    (113_11 Thm 3.1/3.3, divisors and sections doubly dissociated). `NO-GO-LIST.md` [NG-113-*].
15. **Paper 41's three principles** (PROVED as propositions in `04-papers/41-obstruction-catalogue/main.tex`
    §`sec:principles`, lines 1224–1260): P1 radical saturation (no decomposition into nonnegative summands may
    contain a local edge square); P2 measure capacity (no endpoint-preserving positive coupling from the source to
    the polar gradient); P3 counterfactual invariance (every positive datum persists under an off-line orbit;
    "if a proposed argument would remain valid verbatim in a system with an off-line zero, it is already refuted").
16. **Positivity-preserving semigroups / Lévy positivity**: the pole kernel violates the first Beurling–Deny
    criterion (106_13); a positive one-atom jump countermodel has arbitrarily many negative levels, so generic
    Lévy positivity + Hardy/Picone + polar rank one cannot prove the literal-prime inequality (106_19).
17. **Finite-depth heat / moment hierarchies**: for every finite depth there is a real heat model satisfying all
    inequalities through that depth while a nonreal pair fails later (E101.037); a geometric Hausdorff sequence
    obeys every finite-difference sign but has no Stieltjes representation (E101.033); fixed polynomial Pearson
    laws are impossible (E101.070).
18. **Coefficient-level separators are insufficient** (PROVED, 119 §3): `Λ_a(n) = Λ(n)(n^a + n^{−a})` for
    `Ξ_a = ξ(s+a)ξ(s−a)` satisfies P0 (`Λ ≥ 0`), P1 (prime-power support), P2_norm (PSD prime Hankel blocks) and the
    functional equation, and `Ξ_a` has off-line zeros. Any argument using only functional symmetry and an explicit
    formula cannot distinguish ζ from Davenport–Heilbronn (119 §4).
19. **Archimedean-only lower bounds** (115_08 Cor 7): any archimedean lower bound on `−G_∞` costs a slack exactly
    equal to what is missing; the `−D ≥ K` route is false past a small interval (115_10, literature: positivity to
    `u = 1.10246`, `1.15077`).
20. **Exact semilocal Sonin trace identity** (PROVED, 115_16 Prop 2): no entire function has modulus `|E_S|` on the
    critical line, for any `S ∋ ∞`; so hypothesis (H) of 115_09 cannot be an exact identity at fixed `λ`
    ("asymptotic only"). The Sonin excursion (v8) closes at depth one with no prime term (115_17 §8.2), and its
    higher-depth expansion has alternating signs (§8.3).
21. **Two-gate walls** (phases 122, 124): Gate S — "future work on S is admissible only if it introduces an
    independent input … Relations derived solely from `log p`, `p^{−1/2}`, `N` and `Γ` cannot be cited as such an
    input" (P122_028 §6); Gate R — sharp-window translation destroys `H^{1/2}` (P122.021); both gates fail for
    `Ξ_a` (P124.014, qualitative conclusion stands; numeric brackets NUMERIC-UNCERTIFIED per the phase-134 note).
    The naive global determinant assembly has curvature exactly `q_T` (P122.014); the native Bohr determinant
    cocycle splits prime by prime (P122.017); existing Arakelov Hodge-index theorems do not type-check on this
    carrier (P122.007); scalar row-C data cannot recover the oriented defect (P122.005).
22. **Negative-witness package** (phase 121): the closed local package (rank one, Real covariance, dual jets, zero
    scalar supertrace) holds for the universal conormal model `E = z`, `K = c` with arbitrary `c ≠ 0`, so it cannot
    imply F2 (`P121_F2_DIRECT_CLOSURE_AUDIT.md`); ordinary Real covariance does not force opposite parity
    (`P121_TWO_PORT_WRONSKIAN_AND_REAL_AUDIT.md`).
23. **Finite Eulerian/valuative local sources** cannot realize the arithmetic local target once Tamagawa `c_p` is
    retained (107_123–133, real elliptic-curve witness `20a1@2` / `36a4@2`); scalar Picard descent is incompatible
    with the Frobenius pullback law (107_240); Deninger–Morishita kills the `p`-adic transverse direction (107_242).
24. **The archimedean fibre cannot be a subobject** of the corner form (108_42 Thm 4.3: under RH no isometric
    injection); it must enter as a quotient, a complement or with the opposite sign (108_99 §6).
25. **Method-level closures** (phase 104 closure §3): pointwise PNT/Vinogradov–Korobov and absolute values; local
    PSD/PF₂/TP₂/SOS/completely monotone; Selberg–Riccati without a new signed input; Markov/Stein/Palm to second
    order; linear filters, Fejér, block averages; translation-invariant resolvents; positive Euler/Möbius/Landau
    factorizations; Jensen/Cartan/Turán/Blaschke as detectors; zero-density or finite-height verification.
    Phase 101 ledger (3.1) items 76–102 freeze a further list (divisor commutators, `log T`, block-Gram Schur
    complements, carry systems, causal/outer factorization, Hilbert-transform polarization, common dilation).

### 2.3 Measured or refuted specific proposals
1. **Log-Schur angle** `ρ_N ≤ 1/(20 log N)`: refuted by Paper 42's own table at N = 20, 40, 80, 120 (117). Galerkin
   gives lower bounds for a supremum, so the refutation is robust in direction; the entries are float64
   (NUMERIC-UNCERTIFIED).
2. **Γ–Tate source route** (117): `c_N < 1` at every `3 ≤ N ≤ 37`, NUMERIC-UNCERTIFIED but one-sided (Galerkin
   upper bound for a minimum).
3. **Structural scattering ansätze** (118 W3): Toeplitz and Hankel in `log n` (`R² ≤ 0.16`), block-diagonal over
   places, rank-one-plus-diagonal — refuted (partly numeric).
4. **External notes v3–v10** (115_17 §11): v3 no-crossing refuted (Prop 1), v4 threshold induction refuted (Prop 2),
   v10 target `m_e, m_o > 0 ∀T` refuted (numerically at `T ≲ 0.2`, NUMERIC-UNCERTIFIED, 60 zeros); v7 theorem true
   but vacuous; `F_nV_n = nI` false in both normalizations (Prop 8).
5. **D.172 three-block Feshbach template** had a dropped safe-block/tail coupling; the `T = ½log5` certificate was
   demoted (phase 114 closure item 3) and later retracted for reuse (P122.004).
6. **Row B round 3–6 claims withdrawn** (Paper 44 §9bis W13–W23): "the Gram form of the Frobenius family is the Weil
   kernel" — FALSE (refuted by Cor 3ter.10b; the Frobenius family carries only `W_fin`); "Weil positivity implies
   the Hodge index on this class" — retracted; "the sign of the pure Frobenius Gram form is not RH" — withdrawn as a
   non-sequitur; import `(Wgr)` — FALSE (Lemma 8bis.6b: the resonant off-line pair contributes `≍ +e^{δL/2}`, and no
   nonnegative amplitude can peak the transform at `1 − ρ̄_0`).
7. **Row C round claims withdrawn** (Paper 45 §13): the old `§11` `n−1` obligation never existed; `A(s)+A(1−s) ≡ 0`
   demoted (it is the functional equation); the round-2 claim that the sign condition fails for `c ≠ 0` deleted.
8. **Row An audit findings** (phase 128, D128.001–004): Definition 8.1 (germ outside its domain) withdrawn; A.5 not
   addressed then; Thm 5.4 (corner strata) withdrawn; the original proof of Thm 14.1(a),(b) used compactly
   supported `F̂` in `τ`, which is false for `D_A = C_c^∞(C_S)` by Paley–Wiener — withdrawn and re-proved by
   concentration (`[phase 133]` note in Paper 43 §14.1).
9. **Galerkin scans read as positivity**: a positive computed `λ_min` certifies nothing (variational upper bound);
   phases 118–124 scans are diagnostics only (phase-134 scope notes in `PHASE_118_CLOSURE.md` and
   `phase-124-*/README.md`).

---

## §3 What still STANDS

### 3.1 Proved results (label, form, file)

**Sign statements for ζ.**
| # | statement | label | form | file |
|---|---|---|---|---|
| S1 | `A_T > 0` on `P_T` for every `0 < T ≤ log 2` (and at `T = ½log3`, margins 6.5e−4 even / 1.2e−4 odd) | PROVED, CERTIFIED (Arb; replayed P123.036, P118 W4) | [prim] | `04-papers/42-*/main.tex` `thm:certifiedendpoints` (l. 4164), `cor:certifiedinitialinterval` (l. 4355) |
| S2 | `W_T ≥ 0` for `T ≤ ½log2` | CITED (Yoshida 1992; Bombieri 2000) | [compl] | `phase-115-*/115_03_*.md` |
| S3 | nothing for `T > log 2` [prim] or `T > ½log2` [compl] inside my scope (Zhu to 0.8 is later, CITED) | — | — | — |

**Structural theorems (no sign).**
| # | statement | label | form | file |
|---|---|---|---|---|
| T1 | `𝓝 = 0`: `I_A` nondegenerate on `N_A = D_A` (import-free) | PROVED | [struct] | Paper 43 Thm 9.8 (l. 2939) |
| T2 | symbol `T̂` real, real-analytic, `→ −∞`, `m = sup T̂ < ∞`; Plancherel form `T(H) = ∫Ĥ(T̂+c)dχ` | PROVED | [struct] | Paper 43 Thm 9.7 (l. 2568) |
| T3 | universal Tate residue `1` per place; `vol(Z_p^×) = log p` is the unique local normalization with a universal Tate residue | PROVED | [struct] | Paper 43 Thm 9.7b; Paper 44 Thm 8bis.8 |
| T4 | exact sequence `0 → N_A^prim → N_A → B_T → 0`, `B_T` hyperbolic, `†`-exchanged, no splitting; rulings exist in `N_A^dist` and it splits canonically | PROVED | [struct] | Paper 43 Thms 9.11–9.14c′ |
| T5 | Thm 14.1 (no Hodge-index shape) | PROVED (negative) | fixed chart, all `D_A` | Paper 43 l. 5179 |
| T6 | Frobenius family: `Frob_1 = Δ`, `Frob_n^† = Frob_{n^{−1}}`, `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (idempotent, `≠ Δ`), `M(Frob_n) = (n^{1/2}, n^{−1/2})`, commutative inverse semigroup graded by prime sets; finite contact `Λ(n)n^{−1/2}` exactly | PROVED | [struct] | Paper 44 Thms 3ter.4, 3ter.6, 3ter.7, 3ter.12, 3ter.14 |
| T7 | Weil kernel `W_fin + ω_∞` = Gram form of the unit-averaged family `Frob ⋆ Δ^rad` (colimit); the Frobenius family alone carries only `W_fin` | PROVED | [struct] | Paper 44 Thm 8bis.1e (l. 3598), 8bis.1′ |
| T8 | integral shadow `Sh_Z(Frob_n) = [L_S →n→ L_S]`, Möbius cofiber `[Z → Φ_n(1) → Z]`, `deg_det = log n`; complex realization acyclic | PROVED | [struct] | Paper 44 §6bis, Thm 6bis.4 |
| T9 | explicit formula for real `F ∈ C_c^∞`, finite prime sum `n < e^{2T}`, imports (E1)–(E8), (R1) named | PROVED (classical, re-proved) | [compl] identity | Paper 45 Thm 9.4 (l. 1000) |
| T10 | comparison: `I_∞(Γ_F,Γ_F) = β_T(M,M) − Σ_ρΦ_F(ρ)Φ_F(1−ρ)`; on primitive radial classes `= −q(F) = B_nuc(F,F)`; false at a chart outside the window | PROVED | identity | Paper 45 Thm 9.6 (l. 1144) |
| T11 | `c = 0` is the unique real constant for which the comparison identity holds | PROVED | identity | Paper 45 Cor 9.6a (l. 1185) |
| T12 | `Res_{s=0}A_S = |S_f|+1`, `Res_{s=1}A_S = 0` at a chart; `Res_{0}A = Res_{1}A = 1` for the continued symbol; summation and continuation do not commute at `s = 0` | PROVED | [struct] | Paper 45 Thm 9bis.2′, Cor 9bis.3 |
| T13 | **primitive tests suffice**: `¬RH ⟹` nonzero real compactly supported primitive `F_±` (even, odd) with `Σ_ρΦ_F(ρ)Φ_F(1−ρ) < 0` | PROVED | [prim] detection | Paper 45 Thm 10.4 (l. 1680); from `phase-106-*/106_11_*` Thm 1 |
| T14 | `¬RH ⟹` fixed compactly supported negative Weil tests in both parity sectors | PROVED | [compl] detection | `phase-106-*/106_11_BILATERAL_PARITY_NEGATIVE_TEST_THEOREM.md` Thm 1 |
| T15 | `⟨𝔞_T F,F⟩ = Σ_ρ ĥ(ρ) − 2|⟨F,h_e⟩|² + 2|⟨F,h_o⟩|²`, `h_e = cosh(t/2)`, `h_o = sinh(t/2)` (polar defect hyperbolic, signature (1,1)); inertia count `n₋(A_T|P_T) = n₋(A_T) + #{m_e>0} + #{m_o>0} − 2`; falsifier `n₋(𝔞_T on L²(I_T)) ≥ 2 ⟹ ¬RH` | PROVED | [full-a] ↔ [prim] | `phase-115-*/115_17_*.md` Props 5–7 (l. 524, 550, 603) |
| T16 | `Tr(ϑ(h)𝐒) = ‖T(f)‖²_HS + 𝔇(f,f)` with `𝔇 ≥ 0` (Connes–Consani archimedean Sonin trace split into two nonnegative pieces) | PROVED | archimedean only | `115_17` Prop 4 |
| T17 | RH ⟺ `E_K(r) ≥ ½Var_{μ_K}(r)` for all even compactly supported smooth `r` (full-kernel Doob–variance identity, unconditional) | PROVED (EQUIV) | [compl] in Doob coordinates | Paper 41 `thm:doob` (l. 165) |
| T18 | `Γ₂ ≥ 0` (CD(0,∞)) for the prime Dirichlet generator after Doob conjugation, via Schur products and `Λ ≥ 0`; Davenport–Heilbronn fails it | PROVED | prime part only | Paper 35 `thm:CD0` |
| T19 | Gamma absorption `2K(u) < (1501/2000) r_Γ(u)` | PROVED | archimedean | Paper 41 `thm:absorption` |
| T20 | source-defined Lorentzian inertia `(1,|S|−1,0)` of the signed prime tangent Gram | PROVED | [struct] | `phase-114-*/114_d_244_FOURIER_TANGENT_HODGE_FORM.md` §3 |
| T21 | positive-lift Theorem 2.1; zero-residual Green identity | PROVED | [struct] | `phase-120-*/P3_COMMON_FAILURE_ARCHITECTURE.md`, `PHASE_120_CLOSURE.md` item 9 |
| T22 | unitarity obstruction; net-index no-go | PROVED | — | `115_17` Prop 3, §8.5 |
| T23 | an off-line zero forces exponential growth of `λ_n` (zero side) | PROVED | Li | `phase-105-*/105_02_*.md` |
| T24 | finite strong margin certificate `21 ≤ n ≤ 149`; RH ⟹ A1 for `n ≥ n_eff`, `log n_eff < 8.34·10⁸` | CERTIFIED / PROVED conditional | Li | `phase-103-*/103_51_*`, `103_58_*` |
| T25 | row (d) ⟺ sharp Douglas gate over an exhaustive family of births | PROVED (EQUIV) | [prim] | `phase-114-*/ROW_D_SHARP_DOUGLAS.md` (D.170) |
| T26 | shielding dichotomy: at first contact either Gate R holds or the unconstrained form is already indefinite; Gate R follows from `Σ(T) = B_T − X_T*L_T^{−1}X_T ≥ 0` for `T < T_q` | PROVED (reduction) | [compl]/[prim] | `phase-124-*/P124_013_*.md` |
| T27 | DtN of the canonical two-prime Green complex = `‖(E_q−E_p)h‖²/log(q/p)`; zero flux ⟹ `F = 0` | PROVED | [struct] | `phase-122-*/P122_028_*.md` |
| T28 | 109_04 Thm 1.1; 110 Thm 110.2.4; 108_91 Thm 1.2/2.1; 107_241; 113 O1–O3, 113_11 | PROVED (negative) | — | as cited in §2.2 |

### 3.2 Open leads never closed negatively (inside my scope)
| # | lead | status | file |
|---|---|---|---|
| L1 | Colimit version of Thm 8bis.4a (does `Q_fin` fail on primitive radial classes in the colimit?) | OPEN; the Plancherel step fails because `ω̂_fin^∞(0) = +∞` | Paper 44 Remark 8bis.4b(1) |
| L2 | `(H_L)`: primitive `g_* ∈ C_c^∞([L/2,L])`, `Q(g_*) < 0`, `R(L) → 0`; then positivity on Dirichlet-polynomial profiles fails; the converse "positivity on Dirichlet profiles ⟹ RH" OPEN | OPEN | Paper 44 Thm 8bis.7 (l. 4359) |
| L3 | Global square (C.1) `P_T E_T*(K_T*QK_T − Q)E_T P_T ≥ 0` for every `T` | OPEN (EQUIV in force) | `phase-120-*/PHASE_120_CLOSURE.md` |
| L4 | F2: one scalar Kreĭn-flux conservation law functorial on the complex radical line of a first-contact state | OPEN (equivalent in force to the global square) | `phase-121-*/README.md` (parabolic lift) |
| L5 | Construct `Z_{N,ε}` with `𝓡_{N,ε} = Z*Z`, no pseudoinverse, no RH | OPEN | `phase-114-*/PHASE_114_CLOSURE.md` "Endpoint" |
| L6 | Relative correspondence `E_(∞,T)` joining the Bohr module to the quarter-Γ Calderón module (P122 §9.1 item 8) | NOT CONSTRUCTED | `P122_D_SPECIFICATION.md` §§7–9 |
| L7 | Semilocal Sonin hypothesis (H) in an asymptotic (not exact) form; CC's `E ≤ 0` beyond `|I| ≤ log 2`; growth of `#{λ_j(K_I) > 1}` | OPEN; "the one question nobody has asked" | `115_09`, `115_15`, `115_16` |
| L8 | Negative-witness rigidity law (reversed quantifiers) meeting the five conditions of 120 §8 | NOT CONSTRUCTED | `P3_COMMON_FAILURE_ARCHITECTURE.md` §8 |
| L9 | a4 (a product with quadratic growth), b4 (a lattice of correspondences with finite mutual intersection), R16 (can a quadratic `χ` exist over `Spec Z`?) | unbuilt, not proved impossible | `113_15_*`, `NO-GO-LIST.md` §VIII net verdict |
| L10 | Non-invertible correspondences (Weil's degree-`q` graphs) | NOT CONSTRUCTED, required by no clause | Paper 43 §11bis item 5(v) |
| L11 | For `c < 0`, is `I_∞^{(c)} ≤ 0` on primitive classes still ⟺ RH? | OPEN (probably yes, not proved) | Paper 45 Cor 9.6a note |
| L12 | `𝓝_∞^W = 0` (colimit radical) | NOT CLAIMED by any row | Paper 43 §13.8, §14.0 |
| L13 | log5 / log6 finite certificates (D.198–D.227; D.222 within 0.09 of budget at `½log6`) | paused, not failed (numeric) | `PHASE_114_CLOSURE.md` "Loose ends" |

---

## §4 State of rows A, B, C, and of row D (as informed by this scope)

### 4.1 The carrier (identical for the three rows)
Paper 43 §14.0a (l. 5010): a **fixed finite chart** `S = {∞} ∪ S_f`, `S_f ≠ ∅`;
`C_S ≅ R^× × ∏_{p∈S_f} Z_p^×`; `D_A = C_c^∞(C_S)` with convolution `⋆` and `F^†(u) = conj F(u^{−1})`; the chart
system `{C_S, π_TS}` and the colimit `D_A^∞` are **additional structure**, not a replacement. Sector: **invertible
only** (§11bis). A.2–A.9 are discharged at a fixed chart; A.1 and O-A5-2 on the chart system and colimit.
`𝓝_∞ = 0` is not claimed.

### 4.2 Row A (Paper 43; granted R130.005; A.6, A.8 amended)
| clause | recorded | panel-3 grade (`PANEL_3_LABELS_AND_RH_CHAIN.md` §1.1) |
|---|---|---|
| A.1 carrier, descent | PROVED on the declared reading (descent = filtered chart system with retraction); PARTIAL under a stack reading | definitional, disclosed |
| A.2 correspondences | PROVED (Thm 8A.12: objects `E_H = λ(H)`, `H ∈ 𝓐_tr`) | honest, thin (Morita localization half not found) |
| A.3 composition, unit, excision | PROVED on `G` | honest |
| A.4 transpose | PROVED (half-density dagger) | honest |
| A.5 trace-class domain, `T_A` | PROVED; O-A5-5 a theorem at the unit shells and a **declared** normalization at the non-unit shells | honest only for the declared trace |
| A.6 numerical equivalence | REFUTED as literally stated (Thm 9.13(a)) + PROVED as amended (exact sequence) | honest; cost: no single space with one form |
| A.7 effectivity | PROVED (cone = nonnegative coefficients; not the operator-positive cone, Thm 10.2(e)) | definitional, disclosed |
| A.8 mixed RR | REFUTED AS STATED (scalar extension, Thm 10.8) + PROVED AS AMENDED (`λ_RR` into `Pic_b(B_T)`; Thm 10.7(e) second slot DEFINITIONAL) | over-graded before amendment; now amended |
| A.9 classical control | PASSED FOR THE FORMALISM on the automorphism sector | weak as a control |
| A.10 independence | PROVED (no zero, RH or positivity used; Thm 10.8b uses Mertens, CLASSICAL, quarantined) | honest |

### 4.3 Row B (Paper 44; granted R131.019; B.4, B.7 amended)
B.1 PROVED (on the reading "no functor into `G` demanded"); B.2 PROVED (strong monoidal `n ↦ Frob_n`, true unit);
B.3 PROVED (`Frob_n ⋆ Frob_n^† = Δ^{(n)} ≠ Δ` — Weil's `Γ_FΓ_F^t = qΔ` with `q` divided out); **B.4 REFUTED AS
STATED** (the derived diagonal contact is the fixed complex, differential `n−1`, P123.060; no `C`-linear category
carries `Z/p`, P123.022) **+ PROVED AS AMENDED** (identity of degrees: finite contact `Λ(n)n^{−1/2}`, and on objects
via `Sh_Z`, Thm 6bis.4); B.5 PROVED twice (shell volume; `Z`-model); B.6 PROVED; **B.7 REFUTED AS STATED + PROVED AS
AMENDED** (test at `p, p²` proved; the two mechanisms, shell volume and deck `μ_n`, have no map between them;
Rem 6.5a′: `Φ_{p^k}(1) = p` for an unrelated reason); B.8 PROVED; B.9 PROVED "with the independence inherited, not
earned". Imports: Weil's criterion and Chebyshev, CLASSICAL, used by no clause. §12 corrections of
record K1 (convolution constant of Thm 8bis.1) and K2 (`Prim_n` structure now proved, Lemma 5.1b).

### 4.4 Row C (Paper 45; granted R132.007)
C.1 PROVED by citation (test class `D_A^rad`); C.2 PROVED (polar packet = `β_T(M,M)`, Thm 8.1); **C.3 PROVED as a
theorem about row A's declared trace — place-additivity is definitional** (§5.1 says so); C.4 PROVED (residues,
Thm 9bis.2′; Mertens quarantined); C.5 PROVED (no two limits interchanged); **C.6 first half = the explicit formula
transported across the definition of `T`** (Thm 9.4 + Def 8.6 + Thm 8.1), second half PROVED (Thm 10.4, "the
principal new mathematical contribution of phases 130–132"); C.7 PROVED, no sign; C.8 PROVED in the strong form
(Thm 9.4, every classical input named); C.9 PROVED.

### 4.5 What rows A–C imply for row D
1. **The chain above the sign is complete** (panel 3 §5, step 8): row-D target ⟹ RH, PROVED, with the explicit
   formula in the repository. Hypotheses that travel with it and may not be dropped: colimit quantifier (C1),
   `c = 0`, primitivity, radiality (Paper 45 §14.4).
2. **The target is EQUIV to RH**, so rows A–C do not weaken the problem. In Paper 46's language (dictionary D1,
   §6): row-D target ⟺ `∀T: λ^A_T ≥ 0` [prim] (E2 of ROW-D-REDUCED-STATEMENT §1).
3. **The object whose sign is at issue is named**: the Gram form of `Frob ⋆ Δ^rad`, i.e. the full kernel
   `W_fin + ω_∞`, not the Frobenius Gram form (Paper 44 Thm 8bis.1e; Paper 45 §14.4 item 3).
4. **Useful structure delivered**: a carrier with composition and dagger; a trace whose symbol is (by definition)
   the prime-power-plus-Γ side; `𝓝 = 0`; a hyperbolic Tate boundary with the polar packet as its form; the
   primitivizer `Π = −∂_t² + ¼`; unimodularity `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (the datum that fails for `Ξ_a`, which
   gives `(n^a + n^{−a})Δ^{(n)}`; Paper 47 Rem 12.4b, outside my scope, builds on it); the integral shadow `Sh_Z`.

### 4.6 What rows A–C do NOT imply for row D (each is a theorem or an explicit disclaimer)
1. No sign anywhere; nothing about the zeros of ζ (Paper 43 banner, Paper 44 §8bis, Paper 45 §0.2).
2. No Hodge-index shape: infinite index on both sides, no orthogonal complement, rulings a quotient
   (Paper 43 Thm 14.1, Thm 9.13; §2.2 items 7, 10).
3. No positive finite-chart approximation: the target is false at every finite chart (Paper 44 (C1), Thm 8bis.4a).
4. No Frobenius self-intersection; `Δ·Δ = −∞` (Paper 44 Thm 8bis.2, Rem 8bis.1c).
5. No section space, no `h⁰`, no nonnegativity, hence no inequality from RR (panel 3 §5 step 7). "Missing for the
   sign, exactly: a functor to something carrying a nonnegative invariant plus a vanishing theorem, turning the
   biextension equality (Paper 43 (10.10)) into an inequality" (`PANEL_SYNTHESIS.md` §3).
6. No non-invertible correspondences (Weil's argument lives there); Weil's three ingredients live in three
   different objects `G`, `Corr_A^tr`, `N_A^dist` (Paper 43 §11bis item 5(iii)).
7. The trace is declared, not derived: `T̂` is verbatim the prime-power-plus-Γ side (Rem 9.7a); the non-unit-shell
   normalization is declared (O-A5-5); so the comparison theorem's arithmetic content is Thm 9.4 (Weil's) and its
   structural content is Thm 8.1 (panel 3 §4(b)). **For G1 this matters:** rows A–C give "a carrier whose Lefschetz
   formula is the explicit formula", but with the form `I_A` indefinite and no positive form defined before the
   spectrum.
8. The Frobenius family alone carries only the finite half `W_fin`; the averaging `Frob ⋆ Δ^rad` that restores the
   full kernel is exactly what forgets the factorization (Paper 44 Thm 8bis.1′, 8bis.1e).

### 4.7 Row D as seen from phases 91–133
* Proved sign: S1 (`[prim]`, `T ≤ log 2`), S2 (`[compl]`, `T ≤ ½log2`, CITED). Nothing beyond inside this scope.
* Reductions, all EQUIV: sharp Douglas gate (D.170), global square (C.1), F2, Gate R ⟸ `Σ(T) ≥ 0`, two-gate
  criterion (P122.020), Hodge index on `H^⊥` (113_12), `A_T ≥ 0 ∀T` (118).
* The minimal specification of a row-D object (P122_D_SPECIFICATION §§1–6): a category `D_T` with rulings, mixed
  classes, oriented local objects before trace, an archimedean object, restriction functors; a duality that does not
  identify the two causal orientations; numerical equivalence against all objects; the comparison
  `(M_f,M_g)_D = B_nuc(f,g)` proved last ("defining the left side by (3.1) is forbidden"); falsifiers: port swap,
  Davenport–Heilbronn, `Ξ_a`, function fields, Dedekind ζ (with GRH consequence stated).
* Paper 42 `thm:rowdtrilemma`: a geometric proof must (1) factor through the ruling plane — impossible
  (`thm:infiniterankcontact`); (2) extend section cohomology to the mixed module with effectivity, RR, continuity
  and an equality theorem; or (3) prove a new Hodge–Rosati theorem intrinsically before comparing with `B_nuc`.

### 4.8 Record inconsistencies found (not edited; reported for the record)
1. `04-papers/43-row-a-correspondence-algebra/README.md` still says "label withdrawn" (phase-128 banner); `main.md` and
   R130.005 grant the label. The README is stale.
2. `04-papers/44-row-b-arithmetic-family/README.md`: its first status block still reads "conditional on the
   acceptance of the B.4 amendment"; the round-3 block records the acceptance, and B.7's amendment
   (accepted, `phase-133-*/AMENDMENTS_A8_B7_RECORD.md`) is not mentioned in the README at all.
3. `phase-114-*/PHASE_114_CLOSURE.md` and `phase-116-*/README.md` say Paper 42's rows (a)–(c) are "complete and
   published / unconditional"; Paper 42's current abstract says "None of the four complete rows is claimed closed".
   Paper 42's rows (a)–(c) are a different construction from rows A–C of Papers 43–45.
4. Paper 43 README describes Paper 43 as "Markdown only"; `main.tex`/`main.pdf` now exist.

---

## §5 Started but unfinished, or closed for a reason later removed — possible ingredients

Each item states the wall it must still pass (from §2). None is known to avoid all walls.

1. **Unimodularity as the discriminating datum** (Paper 44 Thm 3ter.6(ii): `Frob_n ⋆ Frob_n^† = Δ^{(n)}`). It fails
   for `Ξ_a` (local rank two, 119 §3), and phase 119 shows the place-indexed rank-one package separates ζ from DH and
   `Ξ_a` but is shared by curves and Dedekind ζ, so it is necessary input, not sufficient. Must pass P3
   (counterfactual invariance) — it does, since `Ξ_a` violates it; must pass the positive-lift theorem (120 Thm 2.1)
   — unknown. B7, B17, B18.
2. **The integral shadow `Sh_Z`** (Paper 44 §6bis): an integral structure attached to the object, with transitivity
   triangle and Möbius cofiber. It is the only `Z`-structure in rows A–C. 113 requires "any future (a) must carry a
   `Z`-structure on which the row-(c) pairing is finite" and O2 kills the naive `δ_n` lattice. Open question: is there
   a lattice built from `Sh_Z` on which `I_A` is finite? (a4/b4/R16, L9.) B2, B6.
3. **Mertens' global hyperbolic ruling pairing** (Paper 43 Thm 10.8b, CLASSICAL, quarantined): in the colimit the
   scalar form is hyperbolic on the rulings with value `1`, which is Mertens' theorem; the finite-chart
   vector-valuedness of `λ_RR` is its shadow. Excluded from row A by A.10 only; not excluded from row D.
4. **Lorentzian prime tangent form** (D.244, T20): a genuine source-defined signature `(1, |S|−1)` theorem, "worth
   extracting separately"; dead-ended because it is second order in the local log-velocities while the ABC score is
   first order, and finite rank in prime-index space is not finite rank after Fourier realization (D.258–D.259).
   Directly relevant to B19 (Lorentzian polynomials); the rank issue is wall 2.2.6.
5. **Doob–variance / Poincaré form and CD(0,∞)** (Paper 41 `thm:doob`, Paper 35 `thm:CD0`): RH is one sharp
   Poincaré inequality `E_K(r) ≥ ½Var_{μ_K}(r)`; the prime generator already satisfies `Γ₂ ≥ 0` unconditionally, but
   CD(0,∞) is flat and gives no gap; the radical `{K^{(2j)}/K}` is the threshold eigenspace (equality case,
   infinite dimensional). Paper 41's corridor (§`sec:corridor`): signed, nonlocal in the displacement, applied after
   the mean-periodic anti-short, using prime locations before any norm. Relevant to B16 (Villani); must pass P1, P2.
6. **Heat route = Weil positivity on Gaussian-monomial squares** (E101.038: a determining subcone), with exact
   Laguerre derivative hierarchy (E101.037) and complete monotonicity of one explicit difference (E101.036). Finite
   depth is diagnostic only (E101.037). Relevant to B11, B14 (uniformity in degree ↔ uniformity in `T`).
7. **Centered prime–Γ square** (106_17): the actual prime-power-and-Γ multiplier equals a nonnegative full-line
   translation-jump form minus `κ_N = 4λ + o(λ)`, unique minimum at `t = 0`; in the even sector the pole is a
   positive rank-one term. Paper 46's Lévy representation is its later form. Killed as a closure by the one-atom
   Picone falsifier (106_19); usable only with literal prime locations (P3).
8. **Connes–Consani archimedean Sonin trace** (115_15, 115_16, 115_17 Prop 4): the exact nonnegative split T16 bounds
   `E` from below (wrong side for row d); CC's Prop 5.5 is proved only for `|I| ≤ log 2`; the eigenvalue count
   `#{λ_j(K_I) > 1}` as `I` grows is "the one question nobody has asked" (115_15 title). The semilocal identity can
   only be asymptotic (115_16 Prop 2). Relevant to B1, B20.
9. **The falsifier `n₋(𝔞_T) ≥ 2 ⟹ ¬RH`** (T15) needs only the full-space operator, is monotone in `T`, and "has not
   been computed by anyone" (115_17 §9.6). It is a detector (numeric), not a route; the memos should check Paper
   47 `thm:index` / `thm:parityschur` before recomputing it.
10. **Negative-witness programme** (120 §8, phase 121): reverse the quantifiers — assume a mixed primitive `F` with
    `q_T(F) < 0` and derive a forbidden object. Phase 121 built faithful detectors (`D_T^crit`, parabolic `U(1,1)` lift,
    two-semimetric rigidity: a parabolic monodromy preserving both oriented semimetrics is trivial) but not the law.
    The missing law is "conservation of one explicit opposite-metric monodromy trace on a first-contact state".
    Relevant to B15 (compactness + rigidity); must pass 121's universal conormal model `E = z, K = c`.
11. **Closed for a reason later removed.** 110 closed ξ-divisibility on compact support; 111/113 moved to Schwartz
    data, where the class is nonempty and the pairing converges — and then hit O1–O3 instead. 109 closed coefficient
    pairings; its corrected target (continuation-side, non-symmetrized, zero-free definition) was realized by 113's
    `𝔰`, which is exactly the Weil form (Hodge index ⟺ RH). Paper 47 later used the non-compactly-supported Pólya
    kernel `K` (`Φ_K = ξ`), consistent with 110. Lesson: removing the compact-support obstruction relocates the
    difficulty to the absence of a lattice (O1) and of a spectral gap (O3).
12. **Corrected-mass charged Tate boundary** (106.203/106.204 used `log p/p^k` instead of `log p/p^{k/2}`; the
    corrected version was never built). Warning: 106.205's a.c.-spectrum wall applies to any isometric Hilbert
    completion of that pushout regardless of the mass; a corrected version must use "a resonant nuclear,
    reproducing-kernel, or derived cyclic completion in which discrete evaluation jets survive" (106.205).
13. **Non-symmetrizing well-posedness** (108_99 §7): whether Stage 1 of row (a) can be made well-posed without
    symmetrizing is open; 108 §6 gives two entry prohibitions for any row-(d) stage.
14. **Relative correspondence `E_(∞,T)`** (P122 §9.1 item 8, L6), and the "additional transmission condition" of
    P122.021 — never built. Must introduce input independent of `log p, p^{−1/2}, N, Γ` (P122_028 §6).
15. **The certified table beyond 0.8** (L13): `½log5 ≈ 0.805` and `½log6 ≈ 0.896` lie beyond every recorded sign;
    D.222's exact-Green calculation reached within 0.09 of budget at `½log6` (NUMERIC-UNCERTIFIED). Completing it
    would extend `[prim]` by one window; it cannot prove RH (no upward induction in `T`, Paper 46 `cor:mono`).
    Numerics only if judged strictly necessary.
16. **Paper 44 `(H_L)` and the colimit Thm 8bis.4a** (L1, L2): both are genuine open statements about the ζ Weil form
    on moving windows; Lemma 8bis.6b already shows single-frequency nonnegative-amplitude tests cannot witness a
    violation, which constrains any attempt.

---

## §6 Definitions a memo needs (verbatim; file and line)

**D-carrier (Paper 45 §1.2, `04-papers/45-row-c-explicit-formula/main.md` l. 183–215).**
> "The carrier is Paper 43 §14.0a, verbatim: a fixed finite chart `S = {∞} ∪ S_f`, `S_f` finite nonempty, with the
> chart system `{C_S, π_{TS}}` and its colimit as additional structure on that carrier. Concretely:
> `C_S ≅ R^× × ∏_{p∈S_f} Z_p^×, |x|_S = |x_∞|_∞ on C_S,` (1.1) … `D_A := C_c^∞(C_S), F^†(u) = conj(F(u^{−1}))` …
> The declared trace is Paper 43 Definition 8.6 with the constant declared by Definition 8A.7d:
> `T(F) = Σ_{v∈S} W_v(F), c := 0,` (1.2) … The intersection form is Paper 43 Definition 9.2,
> `I_A(F,G) := T(F ⋆ G^†),` (1.3) … The Tate boundary is `M = (λ_−,λ_+)`,
> `λ_∓(F) = ∫_{C_S}F(u)|u|_S^{∓1/2}d^*u`, continuous and surjective onto `B_T = C²` with the hyperbolic form
> `β_T(z,w) = z_−\overline{w_+} + z_+\overline{w_−}` (Theorem 9.1)."

**D-trace (Paper 43 Def 8.6, `04-papers/43-row-a-correspondence-algebra/main.md` l. 1116–1145).**
> "`T(F) := Σ_{v∈S} W_v(F) + c·F(1), F ∈ D_A,` (8.4) where, at a finite place, … `W_p(F) = ∫_{v_p(x)≠0} a(x) τ_p(x)
> d^*x + (log p) ∫_{Z_p^×} (a(u)−a(1)) / |1−u|_p du, a := F∘j_p`, … `d^*x` giving each shell `p^kZ_p^×` the volume
> `log p`, (8.5) … at the real place … `W_∞(F) = (γ+log 4π) b(1) + ∫_0^∞ K(t)[ b(t)+b(−t) − 2b(1)e^{−t/2} ] dt,
> K(t) = e^{−t/2}/(1−e^{−2t})` … (8.5∞) and `c ∈ R` is a declared real constant, the identity-class normalization."
> (Now `c = 0`, derived: Paper 45 Cor 9.6a.)

**D-colimit (Paper 43 Thm 8A.7c, l. 1851–1880).**
> "`R(F) := sup{|log|w|_S| : w ∈ supp F} < ∞` … `T_∞(F) = T_S(F) + Σ_{ℓ∉S_f, log ℓ ≤ R(F)} (log ℓ) Σ_{k≠0} ℓ^{−|k|/2}
> F(δ_S(ℓ^{−k}))`, (8A.21) a finite sum. … on the filtered colimit … `D_A^∞ := colim_S D_A(S)` … `I_∞(F,G) :=
> T_∞(F⋆G^†)` is a well-defined Hermitian form. … (e) Window comparison. If `R(F⋆G^†) < log ℓ_next(S)` … then
> `I_∞(F,G) = I_A^S(F,G)` exactly."
> Convention (C1), Paper 44 l. 3273: "`T` means `T_∞` on `D_A^∞`" whenever all primes are involved; "(8bis.10) is a
> colimit statement. At a fixed finite chart it is *false*."

**D-symbol (Paper 43 Thm 9.7, l. 2568–2600).** At a finite place with `κ_p = 1`:
`Ŵ_p(χ) = (log p)·2Re(ζ_p/(1−ζ_p))`, `ζ_p = p^{−1/2}\overline{η_p(χ)}`; at `∞`, for `ε = 0`,
`Ŵ_∞(0,τ) = log π − Re ψ(1/4+iτ/2)`; `T̂` real-valued, real-analytic, `m := sup T̂ < ∞`, `T̂ → −∞`; and
`T(H) = ∫_{Ĉ_S} Ĥ(χ)(T̂(χ)+c) dχ` (9.13).

**D-radial class (Paper 44 Def 3bis.6, l. 1097–1099; Paper 45 Def 3.1, l. 419–423).**
> "For `h ∈ C_c^∞(R)` put `Γ_h(x) := h(−log|x|_S), x ∈ C_S`" … "`D_A^{rad} := { Γ_h : h ∈ C_c^∞(R) } ⊂ D_A`",
> with `Γ_h ⋆ Γ_g = Γ_{h∗g}`, `Γ_h^† = Γ_{h^∨}`, `λ_∓(Γ_h) = ∫_R h(s)e^{±s/2}ds`.

**D-primitivity (Paper 45 Thm 8.1, l. 780–795).**
> "(i) `M(Γ_F) = (Φ_F(1), Φ_F(0))`, and `β_T(M(Γ_F),M(Γ_F)) = 2Φ_F(0)Φ_F(1)` … (ii) `M(Γ_F) = 0` iff
> `Φ_F(0) = Φ_F(1) = 0`, i.e. iff `F` is primitive", with `Φ_F(s) = ∫F(t)e^{(s−½)t}dt`.
> Primitivizer (Lemma 10.1): "`Π := −∂_t² + ¼` … `Φ_{ΠG}(s) = s(1−s)Φ_G(s)`".

**D-explicit formula (Paper 45 Thm 9.4, l. 1000–1012).**
> "Let `F ∈ C_c^∞(R)` be real with `supp F ⊆ [−T,T]`, `h = F⋆F^†` … `Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = 2Φ_F(0)Φ_F(1) +
> (1/2π)∫_R |F̂(τ)|²[Re ψ(¼+iτ/2) − log π]dτ − Σ_{2≤n<e^{2T}} Λ(n)n^{−1/2}[h(log n) + h(−log n)]`, (9.6)."

**D-comparison (Paper 45 Thm 9.6, l. 1144–1160).**
> "`I_∞(Γ_F,Γ_F) = T_∞(Γ_{F⋆F^†}) = 2Φ_F(0)Φ_F(1) − Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = β_T(M(Γ_F),M(Γ_F)) − Σ_ρ
> Φ_F(ρ)Φ_F(1−ρ)`, (9.9) and consequently, on the primitive radial sector `M(Γ_F) = 0`, `I_∞(Γ_F,Γ_F) =
> −Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = −Q(F) = −q(F) = B_nuc(F,F)`. (9.10)"

**D-sufficiency (Paper 45 Thm 10.4, l. 1680–1683).**
> "If RH is false, there exist nonzero compactly supported **primitive** real tests `F_+` (even) and `F_-` (odd) with
> `Σ_ρΦ_{F_±}(ρ)Φ_{F_±}(1−ρ) < 0`. Consequently `q_T ≥ 0` on `P_T` for every `T` implies RH."

**D-row-D target (boxed identically; Paper 43 l. 5311, Paper 44 l. 3939 and 5680, Paper 45 l. 2292).**
> "ROW D'S TARGET: I_∂ ≤ 0 on every primitive radial class Γ_g, g ∈ C_c^∞(R), on the colimit D_A^∞ with T_∞ and
> c = 0 (Paper 45 Cor 9.6a); this implies RH by Paper 45 Thm 9.6 (9.10) and Thm 10.4. Standing negatives: Paper 43
> Thm 14.1, Paper 44 Thm 8bis.4a; Paper 44 Thm 8bis.7 is conditional under (H_L), OPEN."

**D-(H_L) (Paper 44 l. 4369–4372).**
> "(H_L) there is a primitive `g_* ∈ C_c^∞([L/2,L];C)` — i.e. `ĝ_*(0) = ĝ_*(1) = 0` — with `Q(g_*) < 0` and
> `R(L) := (L e^{−L/4}‖g_*‖_∞‖g_*‖_{C^1} + L e^{−L/2}‖g_*‖_{C^1}²)/|Q(g_*)|`." (8bis.14d)

**D-Paper 47 forms (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`).**
* l. 119–122 (`eq:symbol`): `m(τ) = Re ψ(¼ + iτ/2) − log π`, `S_T(τ) = m(τ) − Σ_{n∈N_T} v_n cos(τ log n)`,
  `v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`.
* l. 125–127 (`eq:form`): `𝔞_T(F) = (1/2π)∫_R S_T(τ)|F̂(τ)|² dτ`, `F̂(τ) = ∫F(t)e^{iτt}dt`, `F ∈ L²(I_T)`,
  `I_T = (−T,T)`.
* l. 131–133: `A(F) = ∫F(t)e^{t/2}dt`, `B(F) = ∫F(t)e^{−t/2}dt`, "`P_T = {F ∈ L²(I_T) : A(F) = B(F) = 0}`".
* l. 134–136 (`eq:W`): "`W_T(F) = 𝔞_T(F) + 2 Re(A(F)\overline{B(F)})`".
* l. 553–559 (`def:PD`): (P) `λ_P = inf{∫S_T dμ : μ` even probability, `μ̌(u) = 0` for `|u| ≥ 2T`,
  `∫ĝ_0 dμ = ∫ĝ_1 dμ = 0}`; (D) certificates `(ν, β_0, β_1)` with `supp ν ⊆ {|u| ≥ 2T}` and
  `S_T + ν̂ + β·ĝ ≥ c`.
* l. 1219–1227 (`def:W`, `eq:nuw`): `𝒲` = even measurable `w` with `w ≡ 1` on `[−2T,2T]` and
  `|w(u)| ≤ Ce^{−(½+δ)|u|}` outside; `dν_w = [½(1−w)K(|u|) + 2w cosh(u/2)]1_{|u|≥2T}du −
  Σ_{n∉N_T}(v_n/2)w(log n)(δ_{log n} + δ_{−log n})`.

**D1 — dictionary between rows A–C and Paper 46 (surveyor's check; elementary; to be re-verified by P5).**
For real `F ∈ C_c^∞(I_T)`, `c = 0`, colimit: the displayed formula in the proof of Paper 45 Thm 9.6
(`T_∞(Γ_h) = Σ_{n≥2}Λ(n)n^{−1/2}[h(log n)+h(−log n)] + (1/2π)∫|F̂|²[log π − Re ψ(¼+iτ/2)]dτ`, `h = F⋆F^†`) and
Paper 46 `eq:form`/`eq:A` (`h(u) = C_F(u)`, `Σ_n v_n C_F(log n)`) give
**`I_∞(Γ_F,Γ_F) = −𝔞_T(F)` for every real `F` (primitive or not)**, and, since `A(F) = Φ_F(1)`, `B(F) = Φ_F(0)`,
`β_T(M,M) = 2A(F)B(F)`, (9.9) reads `I_∞ = 2AB − W_T(F) = −𝔞_T(F)`. Hence row-D target ⟺ `𝔞_T ≥ 0` on real
`P_T ∩ C_c^∞(I_T)` for all `T`. Complex `F`: `𝔞_T(F) = 𝔞_T(Re F) + 𝔞_T(Im F)` (real even symbol; the argument of
Paper 44 (8bis.8c)), and `A, B` are real-linear with real kernels, so the complex and real statements agree; the
passage from `C_c^∞` to the form domain of `P_T` needs density in the form norm (standard; not checked here).
Fourier conventions differ (`e^{−iτt}` in Paper 45, `e^{iτt}` in Paper 46); harmless because every symbol is even
(Paper 45 Remark 1.2). On the principal component, row A's symbol in the colimit is `T̂ = −S_∞` (untruncated).

**D-positive lift (phase 120, `P3_COMMON_FAILURE_ARCHITECTURE.md` l. 32–47).**
> "For bounded source maps `X:H->K_X` and `Y:H->K_Y`, the following are equivalent: 1. `||XF||^2-||YF||^2>=0` for
> every `F in H`; 2. there is a contraction `Theta:closure(Ran X)->K_Y` satisfying `Y=Theta X`; 3. there is a Hilbert
> space `K_D` and an operator `D:H->K_D` satisfying `D^*D=X^*X-Y^*Y`."

**D-unitarity filter (115_17 l. 351–365).**
> "Let `𝒦` be a Hilbert space carrying a unitary representation `t ↦ U_t` of `R_+^×`, and suppose `λ(f)` is trace
> class on `𝒦` with `Tr_𝒦 λ(f) = Σ_ρ m_ρ f̂(ρ)` (Meyer's trace). Then every `ρ` has `Re ρ = ½`." … "Working filter.
> Does the construction make the scaling group unitary? If yes, RH has already been assumed."

**D-Doob (Paper 41 `thm:doob`, `main.tex` l. 165–192).**
> "`𝒬_W(Kr,Kr) = E_K(r) − ½Var_{μ_K}(r)`, … `E_K(r) = ∫_0^∞∫_R K(x)K(x−u)|r(x)−r(x−u)|² dx dν_ζ(u)`,
> `dν_ζ(u) = Σ_{n≥2} (Λ(n)/√n) δ_{log n}(du) + e^{−u/2}/(1−e^{−2u}) du`, `dμ_K = hK dx/c_K`. The identity is
> unconditional. Consequently the Riemann Hypothesis is equivalent to the single sharp Poincaré inequality
> `E_K(r) ≥ ½Var_{μ_K}(r)` for all even compactly supported smooth `r`." (`K` Riemann's kernel, `K̂ = Ξ`,
> `h = cosh(x/2)`, `c_K = ½`.)

**D-Paper 42 primitive target (`04-papers/42-*/main.tex` l. 3320–3330).**
`B_nuc(f,g) = I_Δ^nuc(f ⋆ g^∨)` on `𝒯 = C_c^∞(R_+^×)`; `𝒯⁰ = {f ∈ 𝒯 : f̂(0) = f̂(1) = 0}`; row (d) there is
`B_nuc(f,f) ≤ 0` on `𝒯⁰` (sign convention (S1) of Paper 45 §1.4: `q = −B_nuc`).

---

*End of S3 survey. Numeric statements quoted from the corpus are marked NUMERIC-UNCERTIFIED unless the corpus
records an interval certificate (S1, T24). No statement here is new mathematics except the dictionary D1, which is
an elementary comparison of two displayed formulas and is flagged for the panel to re-check.*
