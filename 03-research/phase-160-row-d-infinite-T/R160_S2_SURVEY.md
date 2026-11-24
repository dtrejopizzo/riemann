# R160_S2 — Survey S2: phases 40–90 and Papers 16–30

Surveyor S2 of five. Scope: `03-research/phase-40-close-G1` … `phase-90-projective-kato-euler-current`
(including `phase-44-creative-breakthrough`, `phase-44-new-mathematics`, `phase-45-fredholm`,
`phase-60-discriminant`, `phase-64-connes-route`, `phase-65-signature-continuity`, `phase-70-lee-yang-dbn`)
and `04-papers/16-…` through `04-papers/30-…`. All paths are relative to
`/home/trabajo/Documentos/research/riemann/`.

**Method.** Every directory listed; every memo of phases 40–59 read at the executive summary and closing
verdict (these phases are one to nine long Spanish memos each, "Doc 122"–"Doc 199"), with the labelled
theorems of the memos that carry them opened (Docs 131–136, 141–153, 161, 166–173, 198); phase 59 closure
ledger (`phase-59-full-closure/199-total-closure-ledger.md`) read in full; phases 60–70 READMEs, results,
tribunals and key construction memos read; phases 71–90 read through their closure files and cross-checked
against the prior sector map `phase-136-row-d-map/MAP_3_PHASES_061_110.md` (the ≈2 000 incremental files of
phases 72–79 were **sampled, not read exhaustively** — declared here as a coverage limit); Papers 16–30 read
at title, abstract and main-theorem level (Papers 18, 26, 29 opened further).

**Labels.** PROVED / CITED / HEURISTIC / OPEN / EQUIV (= proved equivalent to RH). Every positivity
statement carries its form: **[prim]** = `A_T|P_T` (Paper 46 `eq:form` on `P_T`), **[compl]** = `W_T` on
`L²(I_T)` (Paper 46 `eq:W`). Most objects in this scope pre-date Paper 46; where an object is neither, it is
tagged **[other: …]** with its identification. Key identification used throughout: the CCM Weil matrix
`A_λ` of phases 60–79 acts on functions on an interval of length `L = 2 log λ` with primes `n ≤ λ²` and the
pole term included; in Paper 46 coordinates this is **[compl]** at `T = log λ` (contacts `log n < 2T`). The
Spanish memos use their own tags ([TEOREMA], [DATO], [CONSTRUCCIÓN], [GAP], [DESEO], [PUENTE]); they are
translated below, never upgraded.

**Two warnings for memos before anything else.**
1. **All numerics of phases 60–79 are uncertified.** They are `mpmath` at `dps ≥ 40` (no interval
   arithmetic), on Galerkin truncations. A positive Rayleigh–Ritz minimum on a finite subspace is an
   **upper** bound for the true bottom and certifies nothing about the sign. In particular the measured
   `ε₀(λ) ≈ +2·10⁻²¹ … +5.8·10⁻²¹` for `λ = 7…21` (`phase-61-open-problems/WALL-EULER-LEMMA.md` §0), i.e.
   **[compl]** at `T ≈ 1.95 … 3.04`, is **not** a proved sign for `T > 0.8` and must never be cited as one.
2. The Davenport–Heilbronn (DH) "falsifier" of phases 60–79 is an engine model; NO-GO-LIST `NG-E7` records
   that the DH von Mangoldt data are not reproducible from public definitions and downgraded DH to a
   qualitative control. DH-based separations in this range are HEURISTIC.

---

## §1 What was done (one line per phase / paper)

### Phases 40–59 (Spanish memos,; Docs 122–199)

| phase | content (verdict) | files |
|---|---|---|
| 40 close-G1 | Connes–Consani RR for `Spec Z̄` (2205.01391) read in source: the CC "Serre duality" is Pontryagin duality `Â×A→U(1)`, symmetry bit undefined, `H⁰(D₀)=H¹(D₀)=0` at the self-dual `D₀=−{2}`; square cohomology via tolerance splits into technical (C-cok) and conceptual (C-rank) gaps; CC Weil positivity (2006.13771, 2310.18423) is **spectral**, not intersection positivity | `phase-40-close-G1/122-symmetry-bit-the-character.md`, `123-construction-of-the-cohomology-of-the-square.md`, `124-connes-consani-s-weil-positivity.md` |
| 41 build-G2 | Allermann–Rau intersection on the tropical `C_p×C_p`: Gram on `⟨f₁,f₂,Δ⟩` = `[[0,1,1],[1,0,1],[1,1,0]]`, signature (1,2), primitive negative definite; real (not integer) numbers on flow correspondences; AHK does not apply (finite induction), Babaee–Huh obstructs | `phase-41-build-G2/125-construction-of-the-intersection-form.md`, `126-hodge-index-on-the-square-attainable.md` |
| 42 hodge-dynamics | Forni/EKZ dynamical Hodge theory: right framework, circular (scaling flow is isometric, its trace **is** the explicit formula); Deninger programme judged non-circular *conditional on Kähler–Riemann leaves* | `phase-42-hodge-dynamics/127-dynamical-hodge-theory-as-a-framework.md`, `128-deninger-s-program-is-this-the-missing.md` |
| 43 hodge-foliated | Morishita's space (2508.15971) has profinite 0-dim transversal, real leaves, **no complex structure**; dimension mismatch (curve vs surface); Doc 130 revokes Doc 128: in Deninger's elliptic example the Kähler–Riemann metric uses Hasse `|ξ|²=q` as **input** | `phase-43-hodge-foliated-specZ/129-does-the-foliated-space-of-spec-admit.md`, `130-circularity-to-destruction-test-of-deninger-s.md` |
| 44 creative / new maths | Hodge–Witt "visible inertia" contract; category `𝒜rith` of arithmetic correspondences (orbit theorem `(p,q)` signatures, `q ≤ p`); defect category `𝒫ol_δ` (Theorems A–E: Whitney defect formula, Kreĭn rigidity, dichotomy, parity, tensor flow to `θ=½`); design-by-negation (infinitesimal signature, logistic law `σ^{(k)}=½(1−(1−2σ⁰)^{2^k})`) | `phase-44-creative-breakthrough/131-phase-44-hodge-witt-and-visible-inertia.md`; `phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md`, `132-defect-theory-the-category-ol-of-defective.md`, `133-design-by-negation-the-objects-that-violate.md` |
| 45 fredholm | Weil–Toeplitz algebra (corona symbol, Thm 1.3 robust finiteness ⟺ strict essential positivity; Thm 2.2 fixed-weight normalization has no gap); two-prime theorem for pure objects `F_{p,α}⋆F_{q,α'}`; realizability 133.A: global `σ⁰=0` in both worlds (Thm 2.5), localized `σ_loc` rescue | `phase-45-fredholm/134-weil-toeplitz-algebra-symbol-compact-ideal.md`, `135-two-prime-theorem-positivity-for-pure.md`, `136-problem-133-a-the-realizability-of-under.md` |
| 46 audit & attacks | Audits of local purity (survives with errata), two-prime (correct but trivial direction of Weil), logistic criterion (¬RH branch dies as proof), Weil–Toeplitz (survives, scope caveats); LP-134 formalized (weakest individual statement, still behind the wall); semilocal object with Γ: short-window positivity + low-frequency failure for every finite `S`; Lehmer exponent 2 | `phase-46-audit-and-attacks/137…143-*.md` |
| 47 live fronts | LP-141 refuted in the analytic category (adapted Hadamard function), open in Euler category; semilocal object not spectral-positive (archimedean symbol changes sign); DH off-line zeros; attempted repair of 139.A by exponential dominance; two-prime frames | `phase-47-live-fronts/144…148-*.md` |
| 48 audit & purity | Doc 147 revival refuted (conjugation error); Docs 144/146 audited (DH strong claim refuted); Doc 148 verdict inverted (Thm R.1 frame gap, Prop R.2 Ramanujan spectral); impurity spectrum (Thm 152.2); dlVP-at-½ dies with quantitative certificate (Doc 153) | `phase-48-audit-and-purity/149…153-*.md` |
| 49 cross the wall | Taxonomy of average→individual crossings (positivity is the only mechanism whose input can be the conclusion); individuation-defect theory; `κ=2m` is an index but RH sits in Fredholmicity; tauberian no-go Thm 157.10 + diophantine crack GAP-157.A | `phase-49-cross-the-wall/154…157-*.md` |
| 50 diophantine thread | `ℚ`-linear independence of `{log p}` confined to the value side (Bohr torus); thread dead as a crossing (Thm 158.10) | `phase-50-diophantine-thread/158-diophantine-thread-is-the-linear-independence.md`, `159-destroyer-of-the-diophantine-thread.md` |
| 51 functor | Kronecker crossed product `C(𝕋)⋊ℝ`: genuine transport `𝔉_KMS`, but every canonical inertia metric carries `ζ` through the dual weight (Thm 161.9) | `phase-51-functor-construction/160-*.md`, `161-canonical-inertia-metric-via-noncommutative-poincar.md` |
| 52 homotopy inertia | secondary (e-invariant/Toda) inertia: killed three ways (Doc 163) | `phase-52-homotopy-inertia/162-*.md`, `163-*.md` |
| 53 quantum import | Stone's theorem "inverted": the unitarizing inner product is the Weil form; functional-equation involution is unitary but conjugates, does not evolve | `phase-53-quantum-import/164-import-stone-onda.md`, `165-destructor-of-the-quantum-import-stone-wave.md` |
| 54 index dynamics | metric deformation (Doc 166, largely vacuous per D169); DBN balance law `İ=−2κ−D` (Doc 167, certified D168); `E(T)=Σ_{γ≤T}b²≪T/log T` (Thm 170.5); almost-every-window front closed (Doc 172) | `phase-54-index-dynamics/166…172-*.md` |
| 55 two arrows | Green–Littlewood identity for `I=Σb²` (Thm 173.C), shadow–signal obstruction for holomorphic probes (Thm 173.A); coercivity/backward; energy dichotomy `LP-112 ⟹ I∈{0,∞}`; Hermite take-off | `phase-55-two-arrows/173…177-*.md` |
| 56 two towers | KKL-quantitative lemma; LP-134 polylog repulsion ↔ diffusive dictionary; pivot 176.P1; `0<I<∞ ⟹ ¬LP-112` (Thm 181.1) | `phase-56-two-towers/178…181-*.md` |
| 57 brick A | Dirichlet–Selberg desingularized Green–energy identity (Thm 183.1) | `phase-57-brick-A/183-desingularized-dirichlet-energy-identity-the-selberg.md` |
| 58 full audit | audits D173–D183; boundary flux `F_{1/2}=π Σ b log(γ/2π)+O(log²T)` (Thm 189.2); mollifier floor `c(θ)≥1+log((1−θ)/θ)` for `θ<½` (Thm 191.A); Euler-rigidity conjecture 179.6 | `phase-58-full-audit/184…192-*.md` |
| 59 full closure | RvM-t uniform count (Thm 195.5); DH effective; pipeline barrier (Thm 197.B); **no-go over the axiomatized class 𝔄 + disjunction S1/S2/S3** (Thms 198.2, 198.4); closure ledger | `phase-59-full-closure/193…199-*.md` |

### Phases 60–90 (English, June–

| phase | content (verdict) | files |
|---|---|---|
| 60 discriminant | "multiplicativity controls the sign" refuted (smooth non-multiplicative controls match ζ: NG-F1); CCM programme E0–E4: reduction `RH ⟺ ε_loc(λ)=o(λ^{-1/2})`, Perron–Frobenius ground state, CvS real-rootedness, approximation scaffolding; tribunal: no proof, core RH-equivalent | `phase-60-discriminant/RESULTS.md`, `tribunal-VEREDICTO.md`, `REDUCCION-RH-CCM-final.md`, `RH-PROOF-PAPER.md` |
| 61 open problems | CCM chain inventory O1–O11; Doob limit operator (Chebyshev `U_k`, ladder `(k+1)²`) modulo Lemma 2.3.F; exact `I_n(L)=[cos LJ]_{nn}−[cos LJ]_{n−1,n−1}`; 2×2 Tate transfer `T_S` with Pontryagin index `κ₀+|S|`; band-edge claim retracted | `phase-61-open-problems/OPEN-PROBLEMS.md`, `WALL-EULER-LEMMA.md`, `R10_bandedge_closure.md`, `R9_three_new_fronts_RESULTS.md` |
| 62 Cesàro | Cesàro in `λ` is RH-equivalent (secular `λ^{2β−1}`); quaternionic `V₊`-PSD of the Weil matrix, gapless | `phase-62-cesaro-closure/README.md`, `C1-ANALYSIS.md`, `CROSSING-ATTEMPT.md` |
| 63 Lefschetz | scaling generator anticommutes with the phase-62 `J`; `F_q` positive control; "gaplessness = infinite genus" | `phase-63-lefschetz-realization/README.md`, `R1-VERDICT.md`, `R3-VERDICT.md` |
| 64 Connes route | L1 ⟺ RH (Task A); Kreĭn–Langer index; Pick/passivity of shifted scattering; critical Gram/Lax–Phillips reduction; correspondence realization `(Z_f·Z_f)=W(f)` (formal) + Abboud; **binding erratum** (phase 106): finite self-adjoint determinant = Euler factor is false | `phase-64-connes-route/README.md`, `THE-TARGET.md`, `TASK-A-CLOSURE.md`, `M3a-realization.md`, `CURVATURE-computation.md`, `FACE-C-*.md` |
| 65 signature continuity | D0–D12 package (sourced determinants, Feshbach shorting, `τ_κ`); single load-bearing input D8.5; `RH-PROOF.md` **REFUTED as a proof** (phase 137 D.0) | `phase-65-signature-continuity/README.md`, `D*.md`, `RH-PROOF.md`, `CORRECTIONS-CONNES-R2.md` |
| 66 rank-one escape | ¬RH ⟹ unbounded primitive escape; proxy detector; face A = MW-2; candidate proof **retracted**; maximal closure lemmas | `phase-66-rank-one-escape/RESULTS.md`, `CANDIDATE-PROOF-omega7.md`, `MAXIMAL-CLOSURE-omega7.md`, `D3-large-sieve-gap.md` |
| 67 quantum q-index | q-Pick algebra for `Ω₇`; free-product Haar kills interference (E67.4); signed Jantzen index faithful | `phase-67-quantum-q-index/PHASE67-quantum-q-index.md`, `E67_*.md` |
| 68 GLT symbol | object not GLT (measure{κ<0}≈0.4 while ind₋=0); symbol-depth detector only | `phase-68-glt-symbol/README.md`, `E68_*.md` |
| 69 exact signed index | `ind₋(A_N−P_λ)=0 ⟺ RH` gauge-robust numerically; no forcer | `phase-69-exact-signed-index/README.md` |
| 70 Lee–Yang/dBN | heat-flow forcing reduces to Cauchy–Weil positivity; per-prime route excluded; Wiener–Hopf target `A−T_Λ=D*D` | `phase-70-lee-yang-dbn/README.md`, `OMEGA7_CLOSURE_PROGRAM.md`, `E70_3…E70_12*.md` |
| 71 CAND-1 | CCM spectral triples: RH content moved into convergence `sp(H_x)→{γ}`; Hurwitz closure needs local-uniform characteristic convergence | `phase-71-cand1-convergence/README.md` |
| 72 Feshbach leakage | exact conditional `HF+LF ⇒ target`; zero-filter gate E72.16; balanced remainder identity E72.340 | `phase-72-feshbach-leakage-calculus/E72_16_ZERO_FILTER_GATE.md`, `E72_63_*.md`, `E72_340_*.md` |
| 73 Cauchy projection | Cauchy-plane cell residual; needs CPINV, RCE-cell | `phase-73-cauchy-projection/E73_179_CAUCHY_PLANE_CELL_RESIDUAL.md` |
| 74 Hilbert eigenline | reduces to EG_LOCK; planted nodal falsifier (E74.23) | `phase-74-hilbert-eigenline-cancellation/README.md`, `E74_023_PLANTED_NODAL_FALSIFIER.md` |
| 75 numerator divisibility | autopsy: every escape returns to EG_LOCK / CAUCHY-COMP | `phase-75-arithmetic-numerator-divisibility/P75_013_015_THEOREM_ASSEMBLY_OR_AUTOPSY.md` |
| 76 normalized adjugate | `SR-SAFE ⟹ Ω₇` (P76.034); ambient-norm autopsy (up to 1e28 overestimate); radical decomposition | `phase-76-normalized-adjugate-arithmetic-lock/PHASE_76_CLOSURE.md`, `P76_034_SAFE_RATIO_CLOSURE.md` |
| 77 Weyl limit point | LP + IDENT split; detector spiral; attribution gate: detectors ≠ forcers | `phase-77-weyl-limit-point/PHASE_77_CLOSURE.md`, `E77_7AZ_ATTRIBUTION_GATE.md` |
| 78 build-neutral LP | subclauses (c),(e) are μ_L-pinned detectors; quasimode program fails on tested family | `phase-78-build-neutral-lp-and-ident/README.md` |
| 79 shared convergence | GAP-Z: `ZERO(σ)` summability only numerical (p≈1.2); codim-one discriminant `c_N` not a theorem | `phase-79-shared-convergence-and-ident-discriminant/E79_117_POST_AUDIT_LEDGER.md`, `E79_83_*.md`, `E79_89_*.md` |
| 80 RDI | closed C1–C9; minimal open cut A1–D3 to `Ω₇`; arithmetic discriminant located in B1 (RDI-ANCHOR) | `phase-80-relative-determinant-identification/PHASE_80_CLOSURE.md` |
| 81 secular anchor | exact secular coordinates; defining the target shift by inverse transform is circular | `phase-81-secular-arithmetic-anchor/PHASE_81_CLOSURE.md` |
| 82 coupled generator | projective route loops back to LP + radical obligations | `phase-82-coupled-generator-continuum/PHASE_82_CLOSURE.md` |
| 83 Γ–Euler coboundary | exact zero-free chain semigroup→Möbius→von Mangoldt→CCM; `‖M[S_y*,Z]‖ ≥ 2^{−σ}`; `ker X={0}` domain obstruction | `phase-83-gamma-euler-coboundary/PHASE_83_CLOSURE.md` |
| 84 endpoint module | `δ₀` Euler orbit reproduces the coupled source; inverse-free corrector | `phase-84-distributional-endpoint-module/PHASE_84_CLOSURE.md` |
| 85 parity Weyl defect | moving-pole theorem; pointwise control over-strong; residue SIGNED-PW-E/O | `phase-85-parity-weyl-defect/PHASE_85_CLOSURE.md` |
| 86 signed Abel | first-complementary-mode localization; tails FM-E/FM-O open | `phase-86-signed-spectral-abel/PHASE_86_CLOSURE.md` |
| 87 deformation discriminant | sign coherence cannot identify the limit; exact fractional-Euler deformation | `phase-87-euler-deformation-discriminant/PHASE_87_CLOSURE.md` |
| 88 layer pencil | common two-parity scaling singular; nested limits transferred | `phase-88-endpoint-layer-pencil/PHASE_88_CLOSURE.md` |
| 89 layer rotation | projective dominance + exact Kato rotation current; scale separation insufficient | `phase-89-projective-layer-rotation/PHASE_89_CLOSURE.md` |
| 90 Kato–Euler current | scalar motion drops out; line rotation driven only by the prime matrix; residue PROJECTIVE-KATO-EULER | `phase-90-projective-kato-euler-current/PHASE_90_CLOSURE.md` |

### Papers 16–30 (`04-papers/NN-*/main.tex`)

| # | title (short) | main content |
|---|---|---|
| 16 | unconditional finite bottom | semiboundedness `t ≥ −C(log T)^c‖g‖²` of the height-localized form; second moment `V(d,T)` a band-limited square; clean bound ⟺ uniform short-interval prime variance (Goldston–Montgomery) |
| 17 | Lefschetz dichotomy | independence filter; `Ψ(r)=Re ψ(¼+ir/2)−log π` has unique sign change `r₀=6.2898…`; hard-Lefschetz `sl₂` on the continuum (principal series, no Hodge–Riemann form); linear independence forbids a Tate-twist raising operator on the zeros |
| 18 | Kreĭn index of the Weil form | off-axis evaluation localization; `thm:A` positive kernel ⟹ semidefinite; `thm:B` fixed-sign Cauchy kernel definite; `thm:C` β-smooth non-degenerate forms cannot detect the line; `thm:modular` Maass–Selberg–Zagier resonance pairings sign-definite for every configuration |
| 19 | arithmetic defect of off-line zeros | `κ=2m`; modified explicit formula under Hypothesis D; companion `ζ₀` has no Euler product (RSRP wall) |
| 20 | Herglotz criterion | `RH ⟺ Re ξ'/ξ>0` on `σ>½`; unconditional boundary identity `Re ξ'/ξ(½+iτ)=0` |
| 21 | ω-class information barrier | `q^{ω(n)}` shifted correlations; RH ⟺ `O(N^{−1/2+ε})` error (EQUIV) |
| 22 | moment rigidity | `ν=(|ζ|²−|ζ_on|²)dm_∞ ≥ 0`; `RH ⟺ Δ_n` constant (Meixner–Pollaczek, Carleman, Hardy) |
| 23 | CCM Jacobi incidence | limit Jacobi `J_∞`, spectrum = real zeros of `C_∞=w−Ψ`; `RH ⟺` incidence inclusion |
| 24 | trace–measure criterion | dominance `R=|ζ/ζ_on|² ≥ 1`, `dν ≥ 0`, `dν=0 ⟺ RH`; eight equivalences |
| 25 | bridge (Pontryagin index) | conjecture `κ(Q)=ind₋(H_C)`; verification programme V.1–V.4, V.2 central open |
| 26 | Weil–Toeplitz / logistic | corona symbol, trichotomy in axiomatized model; `RH ⟹ lim σ_loc^{(k)}=0` theorem; converse conditional on `hyp:pw`, which `rem:pw-rigidity` (line 1185) shows no fixed bump satisfies |
| 27 | exhaustion of 1-D propagation | no 1-D propagation principle reaches the boundary; Abel kernel strictly positive ⟹ single-scale trace criterion; survivors Form A (2-D) and Form B (index amplification) |
| 28 | two closures and a survivor | Forms A, C close; tensor index `ind₋(Q₁⊗Q₂)=p₁q₂+q₁p₂`; two-variable Weil functional on thickened diagonal, almost-prime arithmetic side; sieve-to-index bridge |
| 29 | master quantifier | Form B closes (`thm:B`: window indices binary, a uniform bound already implies RH at `k=2`); value vs inertia autonomy |
| 30 | two-lemma architecture | `(m<∞) ∧ LP-112 ⟹ RH`; ζ not Stepanov almost periodic (unconditional) |

---

## §2 What FAILED and exactly why (the do-not-repeat list)

Each entry: mechanism → the theorem or counterexample that kills it → file.

### 2.1 Geometric carriers (G1-type): cohomology of the square, Hodge index, foliations

| # | mechanism | killer | file |
|---|---|---|---|
| F1 | Get a signature from CC's duality on `Spec Z̄` | CC duality is Pontryagin `Â×A→U(1)` between non-isomorphic objects; "symmetric/alternating" is undefined without a self-duality iso `H¹(D)≅Ĥ¹(D)`, which CC do not have; at `D₀=−{2}` both `H⁰,H¹` vanish (eq. (1.5) of 2205.01391) | `phase-40-close-G1/122-symmetry-bit-the-character.md` §5 (HEURISTIC/CITED reading of source) |
| F2 | Tolerance repairs the square's `H¹` | Tolerance repairs cokernels of a single presented map (C-cok) but not rank non-invariance under module isomorphism (C-rank, Yoshitomi Ex. 6.5); the integer rank *is* an intersection form, i.e. G2 | `phase-40-close-G1/123-construction-of-the-cohomology-of-the-square.md` §6 (HEURISTIC: "[CONSTRUCCIÓN]") |
| F3 | CC Weil positivity as the missing Hodge index | Positivity in 2006.13771/2310.18423 is spectral (on tests), RH-equivalent when globalized; not intersection positivity on classes | `phase-40-close-G1/124-connes-consani-s-weil-positivity.md` §0 |
| F4 | Toy Hodge index on `C_p×C_p` propagates to the full square | Correspondences with `μ ∉ p^ℤ` are dense ⟹ infinite rank; signature not continuous under the limit; Babaee–Huh (Duke 2017) exhibits tropical surfaces with the wrong signature; intersection numbers on flow correspondences are real, not integer (G-125.A) | `phase-41-build-G2/125-construction-of-the-intersection-form.md` §5.5–§7 |
| F5 | Adiprasito–Huh–Katz Kähler package for the scaling-site square | AHK is a finite induction on a finite matroid; the square is infinite-dimensional with a continuous flow; no matroidal credential ⟹ default side is Babaee–Huh | `phase-41-build-G2/126-hodge-index-on-the-square-attainable.md` §6 |
| F6 | Forni/Kontsevich–Zorich curvature positivity | Teichmüller flow is hyperbolic with an external Masur–Veech measure; the scaling flow is an isometric translation whose trace **is** the prime side of the explicit formula ⟹ circular | `phase-42-hodge-dynamics/127-dynamical-hodge-theory-as-a-framework.md` §4–§6 |
| F7 | Deninger foliated Hodge–Riemann (math/0204111) on Morishita's space | Morishita's `𝔛_K` has a profinite 0-dim transversal and real leaves, no complex structure; even Deninger's realized elliptic example has leaves of `dim_ℂ 1` while the square needs `dim_ℂ 2`; **and** the Kähler–Riemann metric `g=e^t Re(ξη̄)` of math/0204194 is defined using Hasse `|ξ|²=q` (the RH analogue) as input | `phase-43-hodge-foliated-specZ/129-does-the-foliated-space-of-spec-admit.md` §8; `130-circularity-to-destruction-test-of-deninger-s.md` §0, §6 (Doc 128's non-circular verdict REVOKED) |
| F8 | "Hard-Lefschetz `sl₂`" built from the Frobenius flow | Any raising operator that is a function of the flow restates Weil positivity (independence filter); on the zeros, linear independence of ordinates forbids a Tate-twist raising operator; on the continuum the only `sl₂` is principal series without a Hodge–Riemann form | Paper 17 (`04-papers/17-lefschetz-dichotomy/main.tex`, abstract; "Lefschetz dichotomy") |
| F9 | J-linear gapped Frobenius on the ζ window (function-field mimicry) | The scaling generator anticommutes with the phase-63 `J` (`J e_n = sgn(n)e_{−n}`), ratio 2.000; `D²` sector also gapless. **Scope (R158_004 note):** proved only for that `J`, which factors as the functional-equation involution times a Hilbert-transform factor; it does **not** exclude other quaternionic structures | `phase-63-lefschetz-realization/README.md`, `R1-VERDICT.md`; MAP_3 row 63 scope note |
| F10 | Correspondence realization `Z_f=∫f̂(t)[F_t]dt−c_f[Δ]` + Abboud's inequality closes RH | The self-intersection identity `(Z_f·Z_f)=W(f)` is only formal (trace formula); the arithmetic intersection pairing on `Spec Z̄²` with Hodge-index sign does not exist (MW-5); the degree condition `(Z_f·H)=0 ⟺ μ_max=1` rests on numerics (E96/E101), not a proof | `phase-64-connes-route/M3a-realization.md` §§1–4 (Lemma 1 formal; §4 OPEN) |

### 2.2 Operator/spectral carriers (Hilbert–Pólya, crossed products, determinants, canonical systems)

| # | mechanism | killer | file |
|---|---|---|---|
| F11 | Canonical inertia metric from the KK fundamental class of the Kronecker crossed product `C(𝕋)⋊_φℝ` | Orientation requires the dual weight; its modular partition function is `ζ` (Bost–Connes); every canonical non-flat inertia metric carries `ζ` **necessarily** | `phase-51-functor-construction/161-canonical-inertia-metric-via-noncommutative-poincar.md` §5.2 **[Thm 161.9, PROVED in its setting]** |
| F12 | Secondary (homotopy) inertia: e-invariant / Toda bracket | The filling of the Witt-trivial primary is a Lagrangian that is a datum of `Q` (reintroduces the form); the ℚ/ℤ receptor annihilates the integer `m`; carrier = primes ⟹ partition `ζ` | `phase-52-homotopy-inertia/163-destructor-of-secondary-homotopic-inertia.md` (three kills) |
| F13 | Stone's theorem: a structural unitary evolution with spectrum `{γ}` | Stone "inverted": the inner product making the scaling flow unitary is the Weil form `Q`; the only RH-free unitary (functional equation `J`) lives in `ℤ/2` and conjugates `γ ↦ γ̄`; deficiency indices = boundary conditions = phase of `ζ`; absorption ≠ emission | `phase-53-quantum-import/164-import-stone-onda.md` Props 164.4, 164.6, 164.8; `165-destructor-of-the-quantum-import-stone-wave.md` |
| F14 | Positive-kernel / RKHS carrier of `κ` (Bergman, Hardy, Fock, heat, Bochner-positive convolutions, de Branges with HB structure function) | A positive kernel gives `κ=0` for every configuration, hence cannot be identified with `Q` except under RH | Paper 18 `thm:A` (line 328) |
| F15 | Maass–Selberg / Lax–Phillips resonance pairings on `SL₂(ℤ)\ℍ` as detector | Gram `K_{ρσ}=(s_ρ+s̄_σ−1)^{−1}` is negative definite for **every** configuration in `0<β<1`: sign-definite regardless of RH | Paper 18 `thm:modular` (line 279), `thm:B` (line 347) |
| F16 | Any Hermitian form depending smoothly and non-degenerately on `β` detects `β=½` | Signature is locally constant off degeneracies; detection forces degeneration at `½` | Paper 18 `thm:C` (line 367) |
| F17 | Finite self-adjoint perturbation determinant `D_P = ` critical Euler factor, `D_P → Ξ` | **False in the stated class**: a relative determinant of self-adjoint operators is holomorphic and zero-free off `ℝ`, while `1−p^{−½−iz}` vanishes at `2πk/log p + i/2`; valid only as a scattering/virtual determinant | `phase-64-connes-route/README.md` lines 1–9 (erratum from `phase-106-…/106_00_SELFADJOINT_EULER_DETERMINANT_NO_GO.md`) |
| F18 | Scalar determinant convergence transports positivity/index | A scalar determinant is signature-blind; `D_P→Ξ` does not give `E_P→Ξ` locally uniformly; the join "positive AND Ξ-realizing" is RH by definition | `phase-64-connes-route/THE-TARGET.md` §3; `FACE-C-rigidity-attack.md`; `phase-66-rank-one-escape/CANDIDATE-PROOF-omega7.md` (RETRACTED header) |
| F19 | Phase-65 capstone `RH-PROOF.md` (Vitali resolvent bridge, D8.5d) | REFUTED as a proof of RH; correct only as a reduction to the `P`-uniformity of a renormalized family. Extending resolvent convergence across the strip ⟺ essential self-adjointness of `A_∞°` ⟺ RH | `phase-137-row-d-canonical-coupling/R137_007_CLOSING_DECISION.md` §1 (D.0); `phase-65-signature-continuity/CORRECTIONS-CONNES-R2.md` |
| F20 | Candidate `Ω₇` proof via `E_∞` HB and `κ≤1` | `E_∞=π^{−(¼+iz/2)}Γ(¼+iz/2)` is not entire HB (Γ-poles in the upper half-plane); `Ξ=½E_ξE_ξ^#` doubles real zeros; counterexample `K_P=a_P|e₀⟩⟨e₀|+b_PQ_V`, `b_P=o(a_P)`, `b_P→∞` kills "leading-trace rank one ⟹ bounded primitive escape" | `phase-66-rank-one-escape/CANDIDATE-PROOF-omega7.md` (retraction) and `MAXIMAL-CLOSURE-omega7.md` §3 |
| F21 | Finite-`S` scalar Euler/Tate colligation continued to `ω=0` | Scalar Euler product diverges at the critical value (E109); local scalar factors unimodular but not individually inner — passivity is collective; finite-`S` scalar Robin condition has poles/zeros in `ℂ₊` | `phase-64-connes-route/README.md` (E105, E109); `phase-60-discriminant/RH-PROOF-PAPER.md` Step 11.2-bis |
| F22 | `p`-adic prolate/Sonin operator carrying zeros | `p`-adic concentration on balls has rank one; `p`-adic Sonin space is one-dimensional (CM Prop. 4.5); no finite place carries a zero-bearing spectrum | `phase-60-discriminant/RH-PROOF-PAPER.md` 11.3-quater; `phase-61-open-problems/OPEN-PROBLEMS.md` O8 |
| F23 | Compact-quantum-group prime current, contractive by Haar/Peter–Weyl | strict free-product Haar orthogonality destroys the arithmetic interference; group-like generators collapse to Bost–Connes; diagonal q-Shapovalov loses log-distance coherence | `phase-67-quantum-q-index/E67_4_INTERFERENCE_NO_GO.md`, `E67_12_RESULTS.md`, `PHASE67-quantum-q-index.md` §0 |
| F24 | GLT/Toeplitz symbol positivity `κ(x,θ)≥0` | object fails the GLT distribution law (measure{κ<0}≈0.4 while ind₋=0); gauge-fragile | `phase-68-glt-symbol/README.md`, `E68_5_RESULTS.md` |
| F25 | Cesàro averaging in `λ` of the CCM Jacobi | off-line zeros give secular `λ^{2β−1}`; zero density bounds counts and ordinates, not abscissae ⟹ EQUIV | `phase-62-cesaro-closure/C1-ANALYSIS.md` |
| F26 | Boundedness L1 `sup_λ‖A^osc_λ‖<∞` as a sub-RH lemma | L1 ⟺ RH (Laplace-pole theorem; Paley–Wiener nonvanishing Lemma 1 unconditional) | `phase-64-connes-route/TASK-A-CLOSURE.md` (EQUIV, PROVED with two flagged standard inputs) |
| F27 | "Band-edge closure" R10 as RH-neutral | proving Lemma 1 reconnects to the zero sum of the explicit formula | `phase-61-open-problems/R10_bandedge_closure.md` (retracted in-document) |
| F28 | `k(k+2)` ladder of the Doob-transformed Weil matrix as an arithmetic discriminant | DH reproduces it better than ζ: generic period-2 Dirichlet geometry | `phase-62-cesaro-closure/README.md` "C0 result" |
| F29 | Build-discriminating scalars (sign/cone chains, shell laws) of phase 77 as forcers | Attribution gate: they carry surplus zero-location information, inadmissible by the zero-filter gate E72.16 — detectors, not forcing mechanisms | `phase-77-weyl-limit-point/PHASE_77_CLOSURE.md`, `E77_7AZ_ATTRIBUTION_GATE.md`, `phase-72-…/E72_16_ZERO_FILTER_GATE.md` |
| F30 | Hilbert-space one-vector Γ–Euler intertwiner | `ker X={0}` in `L²(0,L)` (domain obstruction, not an estimate); gauged commutator `‖M[S_y*,Z]‖≥2^{−σ}` for shifts in `(log2,log3)` | `phase-83-gamma-euler-coboundary/PHASE_83_CLOSURE.md` §§1–2 |
| F31 | Secular determinant zeros as independent arithmetic measure | defining the target shift by inverse Stieltjes transform reintroduces the target | `phase-81-secular-arithmetic-anchor/PHASE_81_CLOSURE.md` §2 item 5 |
| F32 | μ-free disk-intersection bypass; sign coherence ⟹ arithmetic identification; common two-parity scaling; static Feshbach eigenline rotation | respectively: full-solution disk uniqueness forces dimension one; false implication; singular limit; scalar motion has no off-diagonal element | `phase-80-…/PHASE_80_CLOSURE.md` C7; `phase-87-…/PHASE_87_CLOSURE.md` §1; `phase-88-…/PHASE_88_CLOSURE.md` §2; `phase-90-…/PHASE_90_CLOSURE.md` §1 |
| F33 | Ambient bordered-inverse norm estimates | overestimate the safe error by up to `1e28` (numerical autopsy, uncertified; no impossibility theorem) | `phase-76-…/P76_061_BORDERED_NORM_AUTOPSY.md` |

### 2.3 Prime-side / semilocal / truncation mechanisms (G2-type)

| # | mechanism | killer | file |
|---|---|---|---|
| F34 | Semilocal interpolation: finite `S` of primes + polar block + Γ-weight satisfies Weil positivity (H⁺) | **Thm B (Doc 142 §5):** for every finite `S`, **including `S=∅`**, an explicit low-frequency family `f_T` with `f̂_T(1)=0` gives `lim Q_S(f_T)/‖f_T‖²_w = Ω(0) − Σ_{p∈S} 2log p/(√p−1) < 0` (`≈ −11.72` for `S={2,3}`); each added prime worsens it. The custody of the pole is transmitted to the real axis only by the **complete** prime sum | `phase-46-audit-and-attacks/142-attack-on-gap-135-b-the-semilocal.md` §5–§8 (PROVED) [other: semilocal `Q_S`, P48 normalization] |
| F35 | Spectral-positive realization of the semilocal object | `∫|F̂|²Ω` is a positive spectral measure iff `Ω ≥ 0` a.e. (Bochner); `Ω(0)=ψ(¼)−log π<0` ⟹ no | `phase-47-live-fronts/145-deciding-gap-142-b-the-spectrality.md` Thms 2.2, 2.4, 3.4 (proof (A) only, per D151); `phase-48-…/151-adversarial-audit-of-docs-145-and-148.md` A.a–A.d, Prop R.2 (vacuity for every `a≥0`) |
| F36 | Per-prime (local) positivity / reflection positivity / per-prime squares | every finite set of primes is "semi-globally pure" (`ω≡0`): impurity and the pole's custody are irreducibly collective; per-prime/local-positive route ruled out for AHM | `phase-48-…/152-attack-purity-rigidity-the-two-purities-semi.md` Prop 152.7; `phase-70-…/E70_7_GLOBAL_CANCELLATION_REQUIREMENT.md` |
| F37 | "Multiplicativity (Euler product) controls the Weil sign" measured by the localized form | zero side blind to multiplicativity (E1); arithmetic side: smooth non-multiplicative controls (flat 2.44, loglin 2.11, logn 2.21) match or beat ζ (1.98): separation was smoothness (NUMERICAL, reproducible, uncertified) | `phase-60-discriminant/RESULTS.md` (NG-F1) |
| F38 | Positivity of `Λ` (Mertens `3+4cos θ+cos2θ≥0`) pushed to the centre | `Λ≥0 ⟹ |S_T(τ)| ≤ S_T(0)`, i.e. `ω ≤ ¼` with equality only at the pole: positivity certifies exactly the boundary purity (dlVP) and nothing towards `½` | `phase-48-…/152-attack-purity-rigidity-the-two-purities-semi.md` Props 152.4–152.5, §3 (F1–F3) |
| F39 | de la Vallée Poussin repulsion transposed to `½` | a quadruple at distance `δ` perturbs `σ>1` by `≤C₀δ²/(1+(t−γ)²)` (second order, FE kills first order); a sub-resolution swarm needs `≳log²γ` zeros per unit window, forbidden by Riemann–von Mangoldt; the dlVP inequality centred at `½` reads `0≥0` | `phase-48-…/153-attack-on-conjecture-144-d-gap-144.md` Lemma 153.2, Prop 153.3, Cor 153.4, §2.5 |
| F40 | Tauberian crossing (Wiener–Ikehara, Ingham–Karamata, Pitt, Carleman, moments) | every tauberian condition local in frequency that suffices for RH is RH-equivalent; Littlewood's oscillation refutes slow oscillation | `phase-49-cross-the-wall/157-tauberian-probe-does-tauberian-theory-cross.md` Thm 157.10, §5.4 |
| F41 | `ℚ`-linear independence of `{log p}` / completeness of `{p^{iτ}}` as a transversality certificate | it certifies transversality on the Bohr-torus (value) coordinate only; the only phase→inertia bridge is the explicit formula, an identity; completeness measured in the Weil-form space becomes RH-equivalent | `phase-50-diophantine-thread/158-diophantine-thread-is-the-linear-independence.md` Thm 158.10; `159-destroyer-of-the-diophantine-thread.md` |
| F42 | Fixed-support (polynomial) test families detect individual off-line zeros | universal blindness: a test of support `e^{±L}` separates a quadruple at distance `δ` from its projection by `O((δL)²)` per unit mass; the second-order signature has **zero total integral**; no countable family of polynomial-support functionals separates LP-134 worlds from their negation | `phase-46-…/141-attack-on-lp-134-resolution-repulsion-formalization.md` Lemma 141.B, Cor 141.B2, Calcs 141.M4–M5 |
| F43 | Almost-every-window / window-statistics improvement of `E(T)` | the second moment of the von Mangoldt bias over windows is a universal prime identity `⅔+o(1)` (Montgomery–Vaughan, Fejér test) in every world; arithmetic progressions give exact blindness by Poisson; ceiling `E≪T/log T` in every world | `phase-54-index-dynamics/172-almost-every-window-detection-direct-improvement.md` Thms 172.2, 172.4, Props 172.6–172.9 |
| F44 | Holomorphic self-contained probes `Σ_ρ Φ(ρ)` weighting `b²` | shadow–signal theorem: the quadratic weight is `w_Φ=−2φ_r''`; if `w_Φ≥0` it is integrable (weight 1 or `1/γ` unreachable); mass–height law | `phase-55-two-arrows/173-structural-representation-of-sum-rules.md` Thm 173.A |
| F45 | Detectors in class 𝔄 (flow laws, density exponents, vertical moduli moments, short mollifiers `θ<½`, deterministic-kernel linear functionals of the Riesz measure) | no `Φ∈𝔄` detects A (`E=o(T/log T)`) nor Dic (`I∈{0,∞}`); every detector pays S1 (microscopic phase correlations = GAP-141.G1), S2 (long mollifiers `θ≥½`), or S3 (exact positivity = Weil) | `phase-59-full-closure/198-gap-190-a-axiomatized-the-trichotomy.md` Thms 198.2, 198.4 (one audit round less: `199-total-closure-ledger.md` §5) |
| F46 | Heat-flow (dBN) forcing via a monotone defect + Rodgers–Tao `Λ≥0` | reduces to finite `Ω₇` / Cauchy–Weil positivity unless an independent Euler–Γ evaluation of the resolvent trace is supplied; Abel-regularized Euler positivity reduces to critical boundary stability (`Λ≤0`); **Form A** of Papers 27–29: the only joint heat-time/arithmetic trace with unconditional edges vanishes identically in the interior (forward dBN preserves reality) | `phase-70-…/E70_3_*.md`, `E70_4_AHM_WEIL_REDUCTION.md`, `E70_8_ABEL_BOUNDARY_LOSS.md`; Paper 29 `thm:A` |
| F47 | Tensor-power / index amplification (Deligne-type) at the level of densities or windows | global density `σ⁰=0` in **both** worlds under finite defect (tensor bookkeeping dilutes the defect) — Doc 133's bridge 2.13(b) false; tensor defect density flows to the absorbing Witt-trivial ideal `θ=½`; **Form B closes**: window indices of the two-variable functional are binary, so any uniform bound implies RH already at `k=2` | `phase-45-fredholm/136-problem-133-a-the-realizability-of-under.md` Thm 2.5, Cor 2.6; `phase-44-new-mathematics/132-defect-theory-the-category-ol-of-defective.md` Thm E; Paper 29 `thm:B` |
| F48 | ¬RH branch of the localized logistic criterion | Paley–Wiener uniformity `hyp:pw` is false for every fixed bump (Lemma 139.1 = Paper 26 `rem:pw-rigidity`); resonant pairs uncontrolled; the Doc 147 repair dies by a conjugation error (`ĝ(σ₀)ĝ(σ₀')‾ = ĝ(σ₀)²`, sign oscillates with `a₀`) | `phase-46-…/139-adversarial-audit-of-the-logistic-equivalence-rh.md`; `phase-48-…/149-adversarial-audit-of-the-139-a-revival.md` |
| F49 | LP-141 / LP-134 (resolution repulsion) without arithmetic | adapted Hadamard function: for **every** fixed unbounded calendar there is an order-1 entire function with FE, reality, ζ-like counting, `m=∞` and zero fat quadruples | `phase-47-…/144-attack-on-lp-141-the-minimal-finiteness.md` Prop 144.2 (verified `phase-48-…/150-adversarial-audit-of-docs-144-and-146.md`) |
| F50 | "D–H zeros are band-separated (liminf δ>0)" | refuted: joint universality + Rouché force `liminf δ_ρ = 0` for DH; only "infinitely many fat zeros" (β>1, [DH36]) survives | `phase-48-…/150-adversarial-audit-of-docs-144-and-146.md` Prop 150.2 (PROVED; third-party audit pending per ledger §5.1) |
| F51 | LP-112 (sequential self-approximation) as an independent input (Paper 30 architecture) | `0<I<∞ ⟹ ¬LP-112` (Thm 181.1); LP-112 is another name for the dichotomy | `phase-56-two-towers/181-gap-175-a-the-minimal-instance.md`; Paper 30 superseded on this point |
| F52 | Uniform lower bound of the localized positivity modulus in height | under RH the modulus is uniform in `T` ⟺ LP-143 (vertical repulsion `liminf(γ_{n+1}−γ_n)log γ_n>0`), conjecturally false (GUE; CGG84 `≤0.5172`) | `phase-46-…/143-attack-on-problem-136-a-quantitative-localized.md` Prop 143.E |
| F53 | Positivity-based size control of the rank-one escape | positivity collapses the Carleson condition to one primitive-diagonal sup, which equals the centre-of-strip second moment (pair correlation): positivity is orthogonal to size; spectral-shift monotonicity is first order while positivity is zeroth order | `phase-64-connes-route/FACE-C-positivity-vs-size.md`, `FACE-C-spectral-shift-monotonicity.md` |
| F54 | Naive Dirichlet-shift square factorization `A−T_Λ = D*D` | manufactures Euler ratio-comb terms `log(n/m)`; a viable factor must cancel the Euler square by a grading/quotient | `phase-70-…/E70_10_DIRICHLET_SQUARE_OBSTRUCTION.md` |

### 2.4 Do-not-repeat map for the phase-160 memos (from this scope only)

| memo | walls in S2 scope it must answer in its §0 |
|---|---|
| B1 Connes (prolate/Sonin, semilocal trace) | F17, F21, F22, F25–F28, F34; phase-60 tribunal C.1 (frame deficit `g₀=Ξ_T` is RH-hard; horizon lemma: zeros sample `PW_Ω` sub-critically, density ratio `1−1/(2log λ)`) |
| B2 Consani (RR over 𝕊 / ζ-cycles) | F1, F2, F3 |
| B3 Jaffe (OS reflection) | F13, F14, F35 (`Ω(0)<0`: the Γ-term is not a positive measure) |
| B4 Haagerup/Popa (natural cone, Tomita–Takesaki) | **F11 (Thm 161.9)** — the dual-weight modular structure of the Kronecker crossed product carries `ζ`; F13, F14 |
| B5 Scholze, B6 Bost | F2, F4, F5, F10 |
| B7 S.-W. Zhang | F10 (Abboud's inequality is available only once the pairing with `(Z_f·Z_f)=W(f)` exists) |
| B17 Lichtenbaum/Morin | F1, F10; Doc 128 cites Flach–Morin only via abstract |
| B18 Morishita/Mazur | **F7** (Morishita's space: 0-dim transversal, no complex structure; Hasse-as-input in Deninger's example), F6 |
| B19 Huh | **F4, F5** (Babaee–Huh; AHK finite induction), Doc 125 toy (1,2) |
| B8 Deligne/Katz | **F47** (dilution, absorbing ideal, Form B binarity), F51 |
| B9 Sarnak, B10 Iwaniec | **F15 (Paper 18 `thm:modular`)**, F14, F16 |
| B11 Tao (dBN + Euler) | **F46**, Doc 167 balance law, Doc 177 take-off; Doc 198 coin (i) |
| B12 Tao (Schur/Hadamard products) | F47, F54, Doc 132 Thm E; phase-64 Γ₂ theorem is generic for every nonnegative weight (see §3.1) |
| B13 Maynard (large sieve, MV) | F43 (MV pinned moment), phase-66 D3 (large sieve = mean square = pole channel), Paper 16 (clean bound = uniform short-interval variance), Paper 29 `thm:B` |
| B14 Ono (Jensen) | no specific wall in this scope beyond F44/F45 (Jensen/Laguerre routes are in phases 102–103, outside S2) |
| B15 Green (ultralimits at `T=∞`) | **F47 (Doc 136 Thm 2.5: `σ⁰=0` for every ultrafilter)**, Doc 134 Thm 5.5 (every calendar misses invisible configurations), F42 |
| B16 Villani (convexity/transport) | Doc 166/169: the metric-deformation functional is convex with Hessian `≥0` by construction; the Weil form is always a critical point and RH is only its membership in the cone (vacuous as a mechanism) |
| B20 Connes (finite `S → all primes`) | **F34, F35, F36, F21**, phase-61 `κ(T_S)=κ₀+|S|` (one negative square per prime) |

---

## §3 What still STANDS

### 3.1 Proved results (label, form, file)

Positivity / sign statements (the only ones that bear directly on row D):

| result | label | form | file |
|---|---|---|---|
| Semilocal short-window positivity: for every finite `S` (and `ζ` itself), `2T ≤ 1/150 ⟹ Q_S(f) ≥ (3/10)‖f‖²_w`; mechanism entirely archimedean (at such windows no prime is in contact; Doc 142 Obs 3.2) | PROVED | [other: semilocal `Q_S` with pole + Γ, P48 normalization]; for `ζ` it is weaker than the classical `[compl] T≤½log2` and Paper 42 `[prim] T≤log2` | `phase-46-…/142-attack-on-gap-135-b-the-semilocal.md` §3 (Thm A = 3.1); restated as surviving in `phase-47-…/145-…` §5 |
| High-frequency cone: positivity of `Q_S` in every window on the cone with dead pole and high frequency | PROVED | [other: `Q_S`] | Doc 142 Prop 7.2 |
| Two-prime pure objects `X_{p,q}=F_{p,α}⋆F_{q,α'}`: Axiom H ⟺ `|α|=√p, |α'|=√q`; exact gap `Q_X=2log(pq)‖f‖²_w` in windows `≤ log min(p,q)`; kernel threshold at `2T=log(pq)` | PROVED (audit D138: correct, content = trivial direction of Weil on a divisor placed on the line) | [other: pure constructive objects, not ζ] | `phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md` Thms A, B, 5.2, 5.4; `phase-46-…/138-adversarial-audit-of-the-two-prime-theorem.md` |
| Two-prime frame gap `μ(T) ≥ min(log q/(2N),(2−√3)log p) > 0` for `log q < 2T ≤ log q + θ`, `θ = dist(log q,(log p)ℤ)` | PROVED | [other: pure two-prime form] | `phase-48-…/151-adversarial-audit-of-docs-145-and-148.md` Thm R.1 |
| Local purity: `H ⟺ |α|=√p ⟺ |c_m| ≤ 2p^{m/2}` for one-prime Euler objects | PROVED (with errata) | [other: one-prime objects] | `phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md` Thm 6.7; `phase-46-…/137-adversarial-audit-of-the-local-purity-theorem.md` |
| Finite bottom (semiboundedness) of the height-localized Weil form, unconditional, `t ≥ −C(log T)^c‖g‖²` | PROVED (numerical appendix for the identity) | [other: height-localized `Q` of Paper 07] | Paper 16 |
| Perron–Frobenius: `A_λ` is `M_θ − V` with positivity-preserving semigroup; at each finite `λ` the bottom eigenvalue is simple, isolated, with even eigenvector | PROVED at finite `λ` (uniformity OPEN) | [compl] at `T=log λ` (sign **not** decided) | `phase-60-discriminant/REDUCCION-RH-CCM-final.md` §2 (Thm 2.1); tribunal "H1 SÓLIDO (estructura)" |
| Real-rootedness of `ξ̂_λ` for convolution-type forms with simple isolated even ground state | CITED (Connes–van Suijlekom arXiv:2511.23257); RH-neutral (holds for DH) | [compl]-type | same file §3 |

Structural theorems (no sign; usable as tools or as walls):

| result | label | file |
|---|---|---|
| Robust finiteness of the defect: `δ(G+K)<∞ ∀K` compact ⟺ strict essential positivity (bounded `G`) | PROVED (audit D140) | `phase-45-fredholm/134-weil-toeplitz-algebra-symbol-compact-ideal.md` Thm 1.3; `phase-46-…/140-adversarial-audit-the-weil-toeplitz-algebra.md` (a) |
| Fixed-weight normalization: `inf spec_ess ≤ 0` unconditionally (no gap to offer) | PROVED | Doc 134 Thm 2.2 |
| Corona of the window field: `‖σ(A)‖=limsup‖A_n‖`, `spec_𝒞 σ(A)` = limit points of window spectra | PROVED | Doc 134 Lemmas 3.2–3.3 |
| Defect arithmetic (Whitney formula `δ(X⊗Y)=d₁δ₂+d₂δ₁−2δ₁δ₂`), Kreĭn rigidity B1–B4, dichotomy for replicable negatives, parity (`δ` even under functional symmetry, **hypothesis `z²∉ℝ` load-bearing**), tensor flow `1−2θ(X⊗Y)=(1−2θ_X)(1−2θ_Y)` | PROVED (audit D140 (d),(e) scope caveats) | `phase-44-new-mathematics/132-defect-theory-the-category-ol-of-defective.md` Thms A–E |
| Logistic law `σ^{(k)}=½(1−(1−2σ⁰)^{2^k})` (exact algebra) | PROVED | `phase-44-…/133-design-by-negation-the-objects-that-violate.md` Thm 2.10; D139 |
| Global density collapse: under finite defect `σ⁰=0` for every ultrafilter | PROVED | `phase-45-…/136-problem-133-a-the-realizability-of-under.md` Thm 2.5 |
| `RH ⟹ lim σ_loc^{(k)} = 0` | PROVED | Doc 136 Prop 5.5; D139 |
| LP-134 formal hierarchy `RH ⇒ m<∞ ⇒ LP-134 ⇒ LP-141` (strict); Lemma 141.M1 (density technology dies at `δ≍1/log T`); universal blindness Lemma 141.B; relative no-go Cor 141.B2 | PROVED | `phase-46-…/141-attack-on-lp-134-resolution-repulsion-formalization.md` |
| Adapted Hadamard countermodel to LP-141 for every calendar | PROVED | Doc 144 Prop 144.2; D150 |
| Impurity spectrum: with `S_T(τ)=Σ_n Λ(n)n^{−½}e^{−(log n)²/4T²}cos(τ log n)`, `ω(τ)=limsup T^{−2}log(2+|S_T(τ)|) = max(0, max_j(δ_j²−(γ_j−τ)²))` for `τ≥1`; forced negative bias `S_T(γ_J) = −2√π m_J T e^{δ_max²T²}(1+o(1))`; `ω(0)=¼` (the pole); `RH ⟺ ω≡0` on `[1,∞)` (EQUIV) | PROVED (explicit formula with Gaussian test; D171 (c) verified term by term) | `phase-48-…/152-attack-purity-rigidity-the-two-purities-semi.md` Def 152.1, Thm 152.2 |
| Self-scale excess: each quadruple evaluated at its own scale `L_j=1/δ_j` with centred Fejér test has one-signed excess `≥ L_j/3 ≫ log γ_j` | PROVED | Doc 153 Prop 153.6 |
| Kaczorowski–Perelli degree < 2 classification ⟹ continuation + Euler + FE give unitary local data | CITED (modulo GAP-153.E) | Doc 153 §3 |
| Individuation-defect theory (collapse ⟺ transversality `𝒮∩H_osc={0}` forced by external input) | PROVED (abstract Hilbert) | `phase-49-…/155-individuation-defect-a-theory.md` Thms 3.2, 3.4, 4.8 |
| `κ=2m` is spectral flow = Maslov = Toeplitz winding **under Fredholmicity**; Fredholmicity ⟺ `m<∞` | PROVED in the model | `phase-49-…/156-index-maslov-probe-is-2m-an-index.md` Thm 156.5, Prop 156.6 |
| Tauberian no-go for frequency-local conditions | PROVED | Doc 157 Thm 157.10 |
| Structural circularity of the Kronecker crossed-product route | PROVED (setting of the memo) | Doc 161 Thm 161.9 |
| DBN balance law `İ = −2κ − D`, `D≥0`, universal rate `−2` per unstable mode | PROVED (certified D168; Cor 2.4 constant corrected to `κ(0)/4`, Cor 2.5 exception clause false) | `phase-54-…/167-dynamics-of-the-index-quantization-maslov-walls.md` Thm 2.3; `168-adversarial-audit-of-doc-167-dynamics.md` |
| `E(T)=Σ_{γ_j≤T}b_j² ≪ T/log T`; `Σ b_j²/(γ_j(log log γ_j)^{1+ε}) < ∞` (first unconditional second-order bound) | PROVED (certified D171) | `phase-54-…/170-second-order-visibility-is-certifiable-by-unconditional.md` Thm 170.5, Cor 170.6 |
| `∫_{T₀}^{2T₀}Σ(τ)²dτ ≪ T₀` (power spectrum of the energy measure), not a density consequence | PROVED | Doc 172 Thm 172.4 |
| Green–Littlewood identity `I(T) = π^{−1}∬ log|ζ| + ⅛ − (2π)^{−1}∫(σ−½)² Im ζ'/ζ(σ+iT)dσ`; Cesàro limit `πI−π/8`; `RH ⟺ −π/8` exact; A ⟹ Lindelöf | PROVED (certified D185) | `phase-55-…/173-structural-representation-of-sum-rules.md` Thm 173.C; `176-attack-on-problem-a-via-green-littlewood.md` Thms 176.4, 176.7 |
| Energy dichotomy `LP-112 ⟹ I∈{0,∞}`; `0<I<∞ ⟹ ¬LP-112` | PROVED (certified D184) | `phase-55-…/175-energy-dichotomy-lp-112-i-0.md` Thm 175.2; `phase-56-…/181-…` Thm 181.1 |
| Hermite self-similar take-off `β²_max = c(n)|t−t_col|`; static pincer `178.C ∧ LP-134∞ ⟹ m<∞` | PROVED (certified D186, D187) | `phase-55-…/177-gap-174-b-decided-the-hermite-takeoff.md`; `phase-56-…/178-…` Cor 178.11 |
| Boundary flux `F_{1/2}=π Σ b log(γ/2π) + O(log²T)` | PROVED (certified D194) | `phase-58-…/189-chink-r2-to-full-calculation-the-boundary.md` Thm 189.2 |
| Universal mollifier floor `c(θ) ≥ 1+log((1−θ)/θ)−o(1)`, `θ<½`, divisor-bounded class | PROVED (novelty reserve GAP-191.L1) | `phase-58-…/191-chink-r1-to-decision-farmer-s-floor.md` Thm 191.A |
| RvM-t uniform count for `H_t`, `t∈[0,1]`; pipeline barrier; no-go on 𝔄; Lehmer inverted (near-double without crossing ⟹ genuine off pair) | PROVED with **one audit round less** (ledger §5.2) | `phase-59-…/195-…` Thm 195.5; `197-…` Thm 197.B; `198-…` Thms 198.2/198.4; `196-…` Lemma 196.2 |
| CCM scaffolding: E0 identity `A_λ(f,f)=Σ_ρ f̂(γ_ρ)f̂(γ̄_ρ)‾`; N0 `|Ξ_T−Ξ| ≤ Cλ^{5/2+δ}e^{−πλ²}`; N1–N3; reduction `RH ⟺ ε_loc(λ)=o(λ^{−1/2})` (modulo E1 = CvS); Hurwitz E3 | PROVED/CITED (tribunal "SÓLIDO", with corrections C.1–C.4) | `phase-60-discriminant/tribunal-VEREDICTO.md`, `REDUCCION-RH-CCM-final.md` §§1, 4, 5 |
| Horizon lemma (corrected): `N(T*) = 2λ²log λ − λ² + O(log λ)` vs Nyquist DOF `4λ²log λ` — zeros sample `PW_Ω` sub-critically, deficit `≈2λ²` | PROVED | tribunal B.2 |
| Exact propagator identity `I_n(L)=[cos LJ]_{nn}−[cos LJ]_{n−1,n−1}` (archimedean Meixner–Pollaczek Jacobi `J`); fine oscillation law with gudermannian frequency `2arcsin(tanh L)` | PROVED | `phase-61-open-problems/OPEN-PROBLEMS.md` O6, O6-bis (Thm 9.5) |
| Parity no-go: a scaling-compatible first-order operator has odd symbol ⟹ anticommutes with that `J`; `J`-linear ⟹ even ⟹ sees only `γ²` | PROVED (for the phase-63/64 `J`) | `phase-64-connes-route/README.md` Task D; `RESULTS.md` |
| `L1 ⟺ RH` (Laplace-pole theorem, Paley–Wiener nonvanishing lemma unconditional) | EQUIV (two standard inputs flagged) | `phase-64-…/TASK-A-CLOSURE.md` |
| `Γ₂(e^{iξθ},e^{−iηθ}) = B(ξ,η)² e^{i(ξ−η)θ}` for the prime jump generator, hence `CD(0,∞)` | PROVED — **but generic**: it holds for every nonnegative weight sequence (any translation-invariant jump generator), so it carries no ζ-specific content (class-level, cf. P46 `cor:void`); DH fails only because its weights are signed | `phase-64-…/CURVATURE-computation.md` Thm 1 |
| Stage-1 finite model: Haynsworth `ν₋(G)=ν₋(Short_a G)` (positive-pole shorting preserves index); subtraction creates a spurious negative square (`G_R` counterexample); a negative pole line forces `ν₋≥1`; index-0 closed in `τ_κ` | PROVED | `phase-65-…/STAGE1-finite-dimensional-model.md`; `D6-POSITIVE-POLE-CLOSEDNESS.md` |
| Maximal closure lemmas: HB closed under local-uniform structural convergence; positive pole shorting preserves index 0; leading-trace rank one ⇏ primitive boundedness; rank-one isolation on subcritical cores `a_φ>½` | PROVED | `phase-66-…/MAXIMAL-CLOSURE-omega7.md` §§1–4 |
| Exact zero-free chain truncated shift semigroup → Möbius → von Mangoldt connection → prime CCM matrix → Γ–Euler commutator; `ker X=span{δ₀}` distributionally | PROVED | `phase-83-…/PHASE_83_CLOSURE.md` |
| `SR-SAFE ⟹ Ω₇` (normal families + Hurwitz, all normalizations in `Re s>1`); `DIRECT-BORDERED-ANCHOR ⟹ Ω₇` (phase 93, outside S2) | PROVED (conditional theorem) | `phase-76-…/P76_034_SAFE_RATIO_CLOSURE.md` |
| Phase 80 C1–C9; phase 81 items 1–7; phase 84 source chain; phase 85 moving-pole bounds `m₁/z² ≤ −Δ_P(z) ≤ m₁/[z(z−η)]`; phase 86 first-mode theorem; phase 87 fractional-Euler deformation `E_{L,t}=E_{L,0}exp(tJ_L)`; phase 89 Kato rotation current; phase 90 prime-driven Kato current `∂_t log[φ_t(z)/φ_t(z_*)] = Σ_n Λ(n)n^{−½}K_t(z,z_*;log n)` | PROVED (exact identities / reductions) | the respective `PHASE_8x_CLOSURE.md`, `PHASE_90_CLOSURE.md` |
| Papers: 17 (`Ψ` unique sign change `r₀=6.2898…`); 18 `thm:A/B/C/modular/F`; 19 (`κ=2m`, companion without Euler product); 20 (boundary identity); 22, 24 (`dν≥0`, `R≥1`); 23 (Theorems B, C); 27 (Abel kernel strictly positive ⟹ single scale suffices); 28 (tensor index identity); 30 (ζ not Stepanov a.p.) | PROVED (as stated in each paper); the RH criteria therein are EQUIV | `04-papers/NN-*/main.tex` |

### 3.2 Open leads never closed negatively

| lead | status | where |
|---|---|---|
| **G1 in this scope's language:** an arithmetic intersection pairing on `Spec Z̄²` with `[F_t]`, `[Δ]` as classes, `(Z_f·Z_f)=W(f)`, and Hodge index `(D·D)≤0` on `(D·H)=0` | OPEN (= MW-5 = OT-5′) | `phase-64-…/M3a-realization.md` §4 |
| Pedido 122.A: a natural self-duality `j_D: H¹(D) ≅ Hom(H¹(D),U(1)_{1/4})` in `ΓT_*` at self-dual `2D=K`, compatible with `σ`, positive | OPEN (never asked/answered) | `phase-40-…/122-symmetry-bit-the-character.md` §5.2 |
| G-125.B: tropical Hodge index on the full square avoiding Babaee–Huh (matroidal/Lefschetz credential external to `ζ`) | OPEN | Docs 125–126 |
| ENUNCIADO-MÍNIMO-130: construct the Kähler–Riemann polarization of a Spec-ℤ foliated space without the localization of zeros | OPEN (believed hard) | Doc 130 §5 |
| LP-152(`τ₀`): subexponentiality in `T²` of the Gaussian prime correlation at **one** frequency | OPEN; strictly weaker than RH as an instance | Doc 152 Def 152.8, §4 |
| GAP-157.A / GAP-162.D: non-local spectral tauberian condition with `ℚ`-linear independence of `{log p}` as input (Beurling–Malliavin/Kreĭn on `{p^{iτ}}`); condition C1 of Doc 159 (discrepancy ⟹ no zero, without the explicit formula) | OPEN; direct thread killed (Doc 158/159) but C1 neither known nor excluded | Doc 157 §5.4; Doc 159 §6 |
| Conjectures 141.E / 144.D / Rigidity 153.M′ / CONJ 179.6 (Euler continuation rigidity ⟹ fat off-line zeros) | OPEN, calibrated (GRH_cat ⟹ 141.E ⟹ 153.M′ ⟹ 144.D ⟹ LP-141_cat) | Docs 141, 144, 153, 179, 192 |
| 139.A: ¬RH branch of the localized logistic criterion | OPEN | D139, D149 |
| GAP-151.A: frame gap in the whole intermediate region for two primes (quasi-invariance by `θ`) | OPEN | Doc 151 §5.2 |
| GAP-196.A: near-doubles of `Λ_f` for DH below mean spacing with line avoidance | OPEN (called "the most decidable") | `phase-59-…/196-gap-192-b-do-the-off-zeros.md` |
| S1 = GAP-141.G1: per-window arithmetic evaluation finer than Montgomery–Vaughan | OPEN (master residue of phases 46–59) | ledger `199-…` §4 |
| Boundary triples for `W_λ` (deficiency `(4,4)`, classify Fourier-invariant self-adjoint `B`; is `B_CCM` unique?) — "RH-neutral, doable now" | OPEN, **never attempted** | `phase-60-discriminant/RH-PROOF-PAPER.md` §4.B item 1 |
| O8: explicit 2×2 Tate canonical system `J Ẏ = z H_S Y`; wall recast as collapse of the Pontryagin index `κ₀+|S| → 0` | OPEN (partially built) | `phase-61-…/OPEN-PROBLEMS.md` O8 |
| O9: individual eigenvalue–zero correspondence for the Sonin spectrum (beyond counting) | OPEN | same, O9 |
| Faithful transfer-matrix `K_P` and true `P_prim` projection | OPEN, unbuilt | `phase-66-…/RESULTS.md` |
| Gauge-invariant (Cayley `w_{1−ρ}=1/w_ρ`) reformulation of the signed index | OPEN, named not built | `phase-69-…/README.md` plan 1 |
| Matrix (not scalar) adelic Tate colligation continued to `ω↓0` | OPEN (RH-strength) | `phase-64-…/README.md` |
| Pole-relative self-adjoint completion (Connes' ask #4) | OPEN | `phase-65-…/README.md` |
| Theory of index jumps on `∂𝕄` (degenerate metrics), dual of the dBN boundary `Λ=0` | OPEN, named | Doc 166 §6 |
| Phase 80 minimal cut A1–D3 (B1 = RDI-ANCHOR carries the arithmetic); phase 85 SIGNED-PW-E/O; phase 86 FM-E/FM-O; phase 90 PROJECTIVE-KATO-EULER | OPEN (each RH-strength as a whole) | phase 80–90 closures |

---

## §4 State of rows A, B, C and of row D (as informed by this scope)

**Rows A, B, C.** The row vocabulary (Paper 42, phases 107–119) post-dates this scope; rows A–C are
WEIL-STRENGTH-COMPLETE on the declared carrier by the premises of record (phases 130–132, outside S2).
What this scope contributes, with the dictionary G1 ≈ carrier/cohomology (rows A–B), "Lefschetz = explicit
formula" ≈ row C, G2 ≈ row D:

* **Row C analogue is formal and unobstructed.** The trace of the scaling flow is the prime side of the
  explicit formula (Connes 1999, CITED in Docs 125, 127); the correspondence self-intersection identity
  `(Z_f·Z_f)=W(f)` holds formally (`phase-64-…/M3a-realization.md` Lemma 1, HEURISTIC/formal). Nothing in S2
  contradicts row C.
* **Rows A–B analogue:** in the tropical/CC setting the carrier splits into a technical half (C-cok,
  closable) and a conceptual half (C-rank: an integer, isomorphism-invariant rank on the square) which Doc
  123 argues *is* an intersection form, i.e. G2 (HEURISTIC, `123-…` §6.2). A finite toy (tropical
  `C_p×C_p`) has the Hodge-index signature (1,2) (Doc 125 §5, computation), but intersection numbers on
  the flow correspondences are real, not integer (G-125.A), and the signature need not persist to infinite
  rank (Babaee–Huh). **Consequence consistent with premise 1:** completing a carrier (A–C) does not by
  itself give the signature; S2 found no mechanism by which it could.

**Row D.** Every phase in 44–90 is a row-D attack. State of record from this scope:

1. **No sign for ζ is proved anywhere in phases 40–90 or Papers 16–30** beyond short-window semilocal
   positivity (Doc 142 Thm A, `2T≤1/150`, weaker than classical) and the structural (unsigned) facts of
   §3.1. The measured positivity of the CCM form (`ε₀(λ)>0` numerically, **[compl]** at `T=log λ ∈ [1.95,3.04]`;
   phase-61 `WALL-EULER-LEMMA.md`) and of `V₊`/`Â_λ`/Pick matrices (phases 61–64) are **uncertified numerics
   on Galerkin truncations** and carry no proof value; the proved record remains that of `ROW-D-REDUCED-STATEMENT`
   §3 (nothing for `T > 0.8`).
2. **The margin decays.** Phases 60–63 observed numerically that the positivity is gapless/marginal
   (`ε₀ = O(1/log λ)` proved by Rayleigh with `Ξ_T` — tribunal / REDUCCION §6 Prop 6.1; measured `≈10⁻²¹`;
   `V₊` cascade `e^{−cL}`; "gaplessness = infinite genus", phase 63 R6). This is the precursor of the later
   proved margin theorems (P46 `thm:margin`; Theorem M of phase 159). Any G2 argument must work with zero
   margin.
3. **Where the sign lives, as located by S2.** (a) Collective, not local: finite `S` fails at large windows
   (F34), each finite set of primes is semi-globally pure (Prop 152.7), the pole's custody reaches the real
   axis only through the full prime sum (Doc 142 §6). (b) Phase, not magnitude: `κ` is a phase invariant
   (phase-61 O10; phase-60 marginality 12.2 — HEURISTIC because its DH comparison is an engine model).
   (c) Inertia, not value: the value of a quadratic functional is computable from the primes, its inertia is
   not (Paper 29 value/inertia; Doc 156: RH enters in Fredholmicity). (d) Quantifier inversion: every
   unconditional object is averaged/generic/interior, RH is individual/uniform/boundary (Paper 29
   `prin:master`); Doc 198's disjunction S1/S2/S3 makes this a theorem over class 𝔄.
4. **Relation to Paper 46 objects.** CCM `A_λ` = **[compl]** `W_T` at `T=log λ`; the "primitive" objects of
   phases 64–66 (`P_prim` removing the pole line `H`) are rank-one-pole primitive analogues, **not** `P_T`
   (which removes two Tate moments `A(F),B(F)`); do not transfer statements between them without checking
   Paper 46 `eq:W` and `P_T` (lines 131–136). `Ω(ξ)` of Doc 142 = `m(τ)` of Paper 46 `eq:symbol`
   (`C₀=Ω(0)=ψ(¼)−log π`), consistent with P46 §9.

---

## §5 Started-but-unfinished ideas, and closures whose reason later phases removed

**(a) Closure reasons later removed or narrowed.**
1. **"No J-linear Frobenius" (phase 63, NG-63)** was read as general; R158_004 narrowed it to the specific
   `J e_n = sgn(n)e_{−n}` (functional-equation involution × Hilbert transform). A different quaternionic
   structure with a J-linear Frobenius is **not excluded** (`phase-136-row-d-map/MAP_3_PHASES_061_110.md`
   row 63, scope note).
2. **Finite Tate determinant bridge (phase 64 `CANONICAL-FOUNDATION.md` §3)** is false as an ordinary
   self-adjoint determinant but Tate's local factor **remains valid as a scattering/virtual determinant**
   (erratum, phase 106). A route that uses it in that category is not closed by the erratum.
3. **Doc 148's "arithmetic is an epiphenomenon"** for two-prime frames was inverted by Doc 151 Thm R.1: the
   frame constant is governed by `θ = min_m|log(q/p^m)|`, an arithmetic quantity; GAP-135.A reopened.
4. **GAP-142.A / GAP-151.C** (archimedean negativity with the pole killed, window `< log 2`) were open in
   phases 46–48; they are now answered for `P_T` by Paper 46 §9 (`thm:index`, `prop:archneg`:
   `T*_∞ ≤ 0.4608 < 0.58 ≤ T*_{∞,P} ≤ 0.60`). Doc 142's short-window Thm A was the precursor of the later
   semilocal positivity at `log 2` (phase 153, outside S2).
5. **Doc 128's "non-circular" Deninger verdict** was revoked by Doc 130 (Hasse as input). What survives is
   the conditional implication "Kähler–Riemann ⟹ positivity" (math/0204111, geometric, over-generating) —
   the antecedent is ENUNCIADO-MÍNIMO-130.
6. **NG-66 proxy** (E110) was withdrawn as a *measurement*, not a refutation; the faithful `P_prim K_P P_prim`
   build was never done.
7. **NG-F0 (phase-60-duality)** was withdrawn for non-reproducibility, not on the merits; its only salvage is
   `H1 ⟺ ‖A^{−1/2}BA^{−1/2}‖<1` (`phase-60-discriminant/00-PLAN.md` §0; NO-GO-LIST NG-F0).
8. **Paper 30's LP-112** was replaced by the dichotomy Dic (`I∈{0,∞}`) after Thm 181.1; the finiteness half
   `m<∞` (L8, "countable avatar of cohomological finite-dimensionality") remains OPEN and is not refuted.

**(b) Unfinished ingredients a memo could use (each with its known cost).**
1. **Gaussian prime correlation `S_T(τ)` (Doc 152).** An exact explicit-formula identity (152.E) with the
   exact `Λ(n)`, no truncation, uniform family in `T`, whose growth rate reads the off-line zeros with a
   **forced sign** at the right height (Thm 152.2(b)). Not reused by later phases (grep over phases
   130–159 finds no citation). Cost: `RH ⟺ ω≡0` is EQUIV; the proof side needs an upper bound on
   `|S_T(τ)|` at one frequency (LP-152), which the positivity of `Λ` cannot give (Prop 152.4). Relevant to G2
   and to the Gaussian-moment Deligne route (memory: phase 149).
2. **Self-scale evaluation (Doc 153 Prop 153.6).** Tests adapted to each quadruple's own scale escape the
   fixed-family no-go 141.B2 and give a one-signed dominant zero-side excess; the missing piece is the prime
   side at super-logarithmic adapted support (Rigidity 153.M′, precision `L e^{−L/2}`).
3. **Boundary triples for the prolate `W_λ`** (phase 60 §4.B): RH-neutral classification of self-adjoint
   extensions at `q=±λ`; decisive test "can the boundary condition be stated without the zeros?" Never
   attempted. Relevant to B1.
4. **2×2 Tate transfer matrices** `T_p=(1−1/p)^{−1/2}[[1,−p^{−½+iz}],[−p^{−½−iz},1]]`, J-unitary on `ℝ`,
   generalized-J-inner with Pontryagin index `κ₀+|S|` (numerically observed, uncertified); wall recast as
   index collapse (phase 61 O8). Relevant to B9/B20.
5. **Critical Gram / Lax–Phillips reduction:** `RH ⟺` positive angle between the Tate subspaces
   `𝒟₋, 𝒟₊=ℱ𝒟₋` (EQUIV; DH fails for lack of `ℱ=⊗'_vℱ_v`) (`phase-64-…/CONSTRUCTION-critical-gram.md`
   §3). Relevant to B9.
6. **Defect category `𝒫ol_δ` as a test of non-circularity:** a construction is non-circular iff it defines a
   functor into the *total* category (also where `δ>0`), not only its `δ=0` fibre (Doc 132 §8). A usable
   §0 criterion for G1 memos.
7. **Correspondence category `𝒜rith`** (all arithmetic functions as objects, so every theorem is external to
   `ζ` by construction; Doc 131) with the orbit theorem and the almost-prime degree formula
   `Σ_N g(N)Σ_{d|N}a(d)a(N/d)φ(d²/N)` (Thm 3.3; Paper 28's autonomous arithmetic side). Warning: P46
   `cor:void` — class-level positivity over such a class decides nothing; the object must single out `Λ`.
8. **Two-variable Weil functional on the thickened diagonal** `h(x₁,x₂)=g(x₁x₂)φ(x₁/x₂)` with (8,8)
   signature on the spectral side and autonomous almost-prime arithmetic side (Paper 28). Form B closed
   (Paper 29 `thm:B`): useful only with a *non-uniform* mechanism.
9. **Phase-83/84 distributional ground vector `δ₀`** and the endpoint Euler orbit: the needed object is a
   distribution, not a Hilbert vector (`PHASE_83_CLOSURE.md` §3). A G1 carrier built on distributions (rigged
   space) is not excluded by F30.
10. **Stepanov theorem (Paper 30/32):** every seminorm seeing compact windows is destroyed by the growth of
    `ζ`; every seminorm under which `ζ` is almost periodic is blind to compact windows. A constraint on any
    "ergodic/almost-periodic" G2 mechanism.

---

## §6 Definitions a memo needs verbatim

**Paper 46** (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`):

* lines 119–124 (`eq:symbol`):
  ```
  m(\tau)=\Rel\psi\!\left(\tfrac14+\tfrac{i\tau}{2}\right)-\log\pi,\qquad
  \sT(\tau)=m(\tau)-\sum_{n\in\NT}v_n\cos(\tau\log n),\qquad v_n=\frac{2\Lambda(n)}{\sqrt n},
  where $\NT=\{n\ge2:\ \log n<2T\}$ is the set of \emph{contacts} and
  $\Aconst:=\sum_{n\in\NT}v_n$ the total mass of the prime comb.
  ```
* lines 125–131 (`eq:form`):
  ```
  \mathfrak a_T(F)=\frac1{2\pi}\int_\R\sT(\tau)\,|\Fh(\tau)|^2\,d\tau ,
  defined on the form domain $\{F\in L^2(\IT):\int\log(2+|\tau|)|\Fh|^2<\infty\}$; it is the
  quadratic form of the operator $A_T$ of \cite{Paper42}, namely the archimedean multiplier
  $G_\Gamma-m_0$ minus $\sum_{n\in\NT}w_n(S_{\log n}+S_{-\log n})$, $w_n=\Lambda(n)/\sqrt n$,
  compressed to $\IT$.
  ```
* lines 131–136 (`P_T`, `eq:W`):
  ```
  The two \emph{Tate moments} are $A(F)=\int F(t)e^{t/2}dt$ and
  $B(F)=\int F(t)e^{-t/2}dt$, and the \emph{primitive subspace} is
  $\PT=\{F\in L^2(\IT):A(F)=B(F)=0\}$. The \emph{complete Weil form} on the window is
  W_T(F)=\mathfrak a_T(F)+2\,\Rel\big(A(F)\overline{B(F)}\big),
  ```
  with (lines 137–138) `W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`, `Φ_F(s)=∫F(t)e^{(s−½)t}dt`; `I_T=(−T,T)`,
  `F̂(τ)=∫F(t)e^{iτt}dt`, `𝒞_F(u)=∫F(t)F(t−u)‾dt` (lines 114–117).
* lines 146–147: "Write `λ_min(A_T|P_T)` for the bottom of `𝔞_T` on the unit sphere of `P_T` and `λ^W_T`
  for that of `W_T` on the unit sphere of `L²(I_T)`; `λ^W_T ≤ λ_min(A_T|P_T)` since the two forms agree on
  `P_T`." (macros `\lamA`, `\lamW`, lines 39–40.)
* lines 553–559 (`def:PD`):
  ```
  \textbf{(P)} $\ \lamP=\inf\big\{\int_\R\sT\,d\mu:\ \mu$ an even probability measure on $\R$,
  $\check\mu(u)=0$ for $|u|\ge2T$, $\int\gh0\,d\mu=\int\gh1\,d\mu=0\big\}$.
  \textbf{(D)} $\ D_T=\sup\big\{\inf_{\tau\in\R}\big[\sT(\tau)+\nuh(\tau)+\beta_0\gh0(\tau)+\beta_1\gh1(\tau)\big]:\
  \nu$ a finite even signed Borel measure with $\supp\nu\subseteq\{|u|\ge2T\}$, $\beta\in\R^2\big\}$.
  A triple $(\nu,\beta_0,\beta_1)$ with $f:=\sT+\nuh+\beta\cdot\widehat g\ge c$ on $\R$ is a
  \emph{certificate of value $c$}.
  ```
* lines 1219–1227 (`def:W`, `eq:nuw`):
  ```
  $\Wcl$ is the set of even measurable $w:\R\to\R$ with $w\equiv1$ on $[-2T,2T]$ and
  $|w(u)|\le Ce^{-(\frac12+\delta)|u|}$ for $|u|\ge2T$, for some $C,\delta>0$. $\Wcl^{\mathrm{reg}}\subset\Wcl$
  consists of the $w\in C^\infty(\R)$ with compact support. For $w\in\Wcl$ define the even measure
  d\nu_w=\Big[\tfrac12\big(1-w(u)\big)K(|u|)+2w(u)\cosh\tfrac u2\Big]\mathbf 1_{|u|\ge2T}\,du
  -\sum_{n\notin\NT}\tfrac{v_n}2\,w(\log n)\,\big(\delta_{\log n}+\delta_{-\log n}\big),
  and $f_w:=\sT+\nuh_w+2\gh0$.
  ```
  with `K(u)=½/sinh(u/2)+½/cosh(u/2)` and `C₀=ψ(¼)−log π` (lines 161–162; numerical value
  `C₀=−5.3721834…` line 369).

**Paper 47** (`04-papers/47-intersection-frame-defect/archive/main.md`, lines 158–159): "`I_∞(Γ_F,Γ_F) = 2Φ_F(0)Φ_F(1) −
Σ_ρΦ_F(ρ)Φ_F(1−ρ)` (9.9), and on the primitive radial sector `I_∞(Γ_F,Γ_F) = −Σ_ρΦ_F(ρ)Φ_F(1−ρ)` (9.10)."

**From this scope** (quoted from the memos; memos must re-normalize to Paper 46 before use):

* **Gaussian prime correlation and impurity weight** (`phase-48-audit-and-purity/152-attack-purity-rigidity-the-two-purities-semi.md`,
  lines 182–188, Def 152.1):
  `S_T(τ) := Σ_{n≥2} Λ(n)/√n · e^{−(log n)²/4T²} cos(τ log n)`;
  `ω(τ) := limsup_{T→∞} log(2+|S_T(τ)|)/T² ∈ [0,∞]`; `Σ_imp := {τ≥0 : ω(τ)>0}`.
  The explicit formula used (line 218, [IK04 Thm 5.12] normalization):
  `(2/(√π T)) S_T(τ) = −Σ_ρ h_{T,τ}(t_ρ) + 4e^{T²(¼−τ²)}cos(τT²) + A_T(τ)`,
  `h_{T,τ}(t)=e^{−T²(t−τ)²}+e^{−T²(t+τ)²}`, `t_ρ=(ρ−½)/i` (152.E).
* **CCM form** (`phase-60-discriminant/REDUCCION-RH-CCM-final.md`, line 13, Def 1.1): on band-limited
  `E_λ` supported in `[−L/2,L/2]`, `L=2log λ`, `Ω=log λ`,
  `A_λ(f,f) = ∫ Ω̃(t)|f̂(t)|²dt − ∫ D_λ(t)|f̂(t)|²dt`, `Ω̃(t)=−log π+Re ψ_Γ(¼+it/2)`,
  `D_λ(t)=Σ_{n≤λ²}Λ(n)n^{−½}cos(t log n)`; identity `A_λ(f,f)=Σ_ρ f̂(γ_ρ)f̂(γ̄_ρ)‾` (Thm 1.3, pole and
  archimedean terms included — tribunal: "el término de polo 𝒫 es load-bearing"). Reduction (line 41,
  Thm 5.1): `HR ⟺ ε_loc(λ) = o(λ^{−1/2})`. In Paper 46 terms: **[compl]**, `T=log λ`.
* **`Ω₇`** (`phase-67-quantum-q-index/PHASE67-quantum-q-index.md`, lines 65–73):
  `δ_N = λ_min(A_N^{−1/2}(A_N−P_λ)A_N^{−1/2}) = 1−λ_max(A_N^{−1/2}P_λA_N^{−1/2})`;
  `Ω₇: δ_N ≥ 0 ∀N ⟺ A_N ⪰ P_λ ∀N`, with `A_N` the archimedean Pick jet and `P_λ` the prime Pick jet at gauge
  `z₀=t₀−iy` (`phase-66-rank-one-escape/CANDIDATE-PROOF-omega7.md` line 30); `Ω₇ ⟺ RH` (EQUIV, Paper 36).
* **Semilocal archimedean weight** (`phase-46-audit-and-attacks/142-attack-on-gap-135-b-the-semilocal.md`, lines 21–22):
  `Ω(ξ)=Re ψ(¼+iξ/2)−log π`, `Ω(0)=ψ(¼)−log π=−γ−π/2−3log2−log π ≈ −5.3722 < 0` (= `C₀` of Paper 46);
  Thm B deficit (line 30): `lim_T Q_S(f_T)/‖f_T‖²_w = Ω(0) − Σ_{p∈S} 2log p/(√p−1)`.
* **Defect** (`phase-44-new-mathematics/132-defect-theory-the-category-ol-of-defective.md`, line 60): for `(H,Q,P)` with Weil
  operator `C`, `δ(X) := neg.ind(Q_C|_P) ∈ ℕ∪{∞}`; reduced defect `δ̂ = δ/2` under functional symmetry (line 61).
* **LP-134** (`phase-46-audit-and-attacks/141-attack-on-lp-134-resolution-repulsion-formalization.md`, Def 141.1 at line 107; canonical
  form in §0): `liminf_{ρ off} |β_ρ−½|·log γ_ρ > 0` (`:= +∞` if finitely many off-line zeros).
* **Class 𝔄 and the disjunction** (`phase-59-full-closure/198-gap-190-a-axiomatized-the-trichotomy.md`, §1, Def 198.1;
  coordinates line 9): `I=Σb²`, `E(T)=Σ_{γ≤T}b²`, `μ₂(T)=(log T/T)E(T)`; **A** ⟺ `E(T)=o(T/log T)`;
  **Dic** ⟺ `I∈{0,∞}`; `RH ⟺ A ∧ Dic`; five coins (i) ζ-free flow laws, (ii) exponential densities, (iii)
  vertical moduli moments, (iv) short mollifiers `θ<½`, (v) deterministic-kernel linear functionals of the
  Riesz measure of `log|ζ|`; (A2) accessibility by a proved unconditional envelope.

*End of S2 survey.*
