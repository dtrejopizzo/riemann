# Map 3 — Phases 061–110: every mechanism attempted toward the sign `I_∞(F,F) ≤ 0`

Sector of the Row-D corpus map covering `03-research/phase-61-open-problems` through
`phase-109-one-sided-pairing` (phase-110 does not exist as a directory — the next existing
phase in this range is `phase-135-row-d-canonical-class`, outside this sector). All paths
below are relative to `/home/trabajo/Documentos/research/riemann/03-research/` unless given
in full.

This is a survey of an enormous, extremely disciplined negative-results corpus. Essentially
every phase in 61–109 ends in one of: (a) an exact reduction to a narrower but still-open
statement, (b) a proof that a proposed mechanism is impossible, (c) a proof that a mechanism
is exactly equivalent to RH (circular), or (d) a numerically/diagnostically observed
regularity that is explicitly *not* claimed as a theorem. No mechanism in this entire range
closes `I_∞(F,F) ≤ 0` or its Li–Keiper equivalent `Ω₇`.

---

## 1. Mechanism table

Legend for status: **PROVED-IMPOSSIBLE** (a theorem that the mechanism cannot work),
**EQUIVALENT-TO-RH** (proved circular / exactly as hard as RH), **ABANDONED** (dropped,
not disproved), **NUMERICAL-ONLY** (killed or "supported" only by floating-point evidence),
**PARTIAL-SUCCESS** (a genuine unconditional theorem or exact reduction proved, short of the
target).

### Phases 61–70

| phase | mechanism | why it failed | status | over-generalized? | adjacent square never tried | source |
|---|---|---|---|---|---|---|
| 61 | R10/E85 "band-edge closure": Doob-conjugated Weil operator `G_λ` has a bounded intrinsic Jacobi with quadratic band edge `k(k+2)`, claimed RH-neutral | Self-correction: attempting to *prove* (not just numerically verify) the boundedness Lemma 1 shows the fluctuation term is exactly the zero-sum of the explicit formula; unconditional and even RH-conditional prime bounds both diverge — closing it needs "the oscillatory cancellation of `Σ_ρ ĝ(γ_ρ)` = de Branges/Sonin machinery = the wall" | NUMERICAL-ONLY (initially claimed RH-neutral, retracted) | Yes — R10 itself over-claimed "standard analysis, RH-neutral"; explicitly retracted in-document | The Weyl/homogenization angle (R11) was named as the next attempt | `phase-61-open-problems/R10_bandedge_closure.md:80-92` "El Lema 1, apenas se intenta DEMOSTRAR ... reconecta con el control de ceros = el muro." |
| 62 | Cesàro averaging in λ of the intrinsic Jacobi, to wash out the zero-sum oscillation unconditionally via zero-density | Zero-sum's Cesàro average converges **iff** zeros lie on the line; off-line zeros give secular growth `λ^{2β-1}` that zero-density (which bounds counts/imaginary parts, not real parts) cannot remove | EQUIVALENT-TO-RH (detector only) | No | none (exhausted) | `phase-62-cesaro-closure/README.md:15-20` "averaging relocates the wall but does not cross it" |
| 62 | Quaternionic Hodge–Riemann polarization: is the finite Weil matrix `A` PSD on `V₊` (the `+i`-eigenspace of `J`, `J²=-1`)? | **PARTIAL SUCCESS, then wall.** ζ genuinely IS PSD on V₊ at every tested λ (DH and random-symmetric controls fail) — but the positivity is *gapless*: spectrum cascades `e^{-cL}`→0, with ζ sitting exactly at `μ_max(L_prime,L_arch)=1` (marginal, from below) | PARTIAL-SUCCESS (real, non-circular, non-random positivity result) / wall reached | No | Give V₊-positivity a uniform `e^{-cL}` gap without zero locations — needs the Spec-ℤ cohomological realization (MW-5), untried | `phase-62-cesaro-closure/README.md:35-46` "ζ is positive-semidefinite on V₊ ... But it lands on the master wall ... gapless" |
| 63 | Search for a Hard-Lefschetz `sl₂`-triple `(L,Λ,H)` on ζ's Weil matrix `A` (the operator that forces the gap over `F_q`) | The scaling/Frobenius-candidate operator (spectrum = zeros) **anti-commutes** with `J` (ratio 2.000 exact) — it is complex-antilinear, the wrong type to be Frobenius; `F_q` curves have `[F,J]=0` and a gapped polarization exactly, confirming the contrast | PROVED-IMPOSSIBLE (operator-level obstruction, sharp) | No | squaring (`D²` is J-linear) was tried (R6/E99) and also found gapless in both sectors | `phase-63-lefschetz-realization/README.md` (R1-VERDICT, R3-VERDICT, R6/E99) — "no J-linear Frobenius isometry of a gapped polarization on the ζ window ... this is MW-5" |
| 63 | (deep dive, see §4 below) | | | | | |
| 64 | Connes' route: realize Ξ as structure function of a positive canonical system; L1 boundedness as RH criterion; relative determinant / de Branges / adelic scattering colligation | Binding erratum from phase 106: the finite self-adjoint perturbation-determinant bridge `D_P→Ξ` is **false** in the stated operator class (an ordinary rel. det. of self-adjoint operators is zero-free off ℝ; the Euler factor has zeros off ℝ) | EQUIVALENT-TO-RH (Task A: `L1 ⟺ RH` proved) | Yes — the original finite Tate bridge (`CANONICAL-FOUNDATION.md §3`) is flagged false/over-generalized by phase 106 | The matrix (not scalar) adelic colligation continued to `ω↓0`, never completed | `phase-64-connes-route/README.md:1-9` (erratum), TASK-A-CLOSURE.md, `README.md` "Status" section |
| 64 | (deep dive, see §4 below) | | | | | |
| 65 | Index-graded regularized determinant `D̃` + topology `τ_κ`; positive-pole Feshbach shorting; sourced Witt–Nevanlinna determinants (D0–D12 program) | Program reduces cleanly to one load-bearing input D8.5 (source-level Tate×Binet local-factor convergence); post-Connes-round-2 correction: the real wall is **self-adjointness of the limit operator** (not index of a meromorphic limit) — extending resolvent convergence across the critical strip is valid iff `A_∞^∘` is essentially self-adjoint iff RH | EQUIVALENT-TO-RH (D8.5 ⟹ RH, "candid conditional, not a proof by us") | No — extremely careful, self-corrects an earlier over-claim (RH-PROOF.md capstone superseded) | Building the actual pole-relative self-adjoint completion (Connes' ask #4), never done | `phase-65-signature-continuity/README.md` (D8, D11, D12, CORRECTIONS-CONNES-R2.md) |
| 66 | Rank-one escape dichotomy: is the escape norm `sup_P‖P_prim K_P P_prim‖` bounded for ζ vs. unbounded (`λ^{2β-1}`) for off-line zeros? | The *easy* direction (¬RH ⟹ unbounded) and a faithful proxy detector (ζ bounded / DH unbounded) are confirmed; but the full sharp-dichotomy theorem and face (A)=MW-2, face (B)=MW-5 identification leave the escape theorem itself at RH-strength | PARTIAL-SUCCESS (D1 easy direction + D2 detector + D3 large-sieve-gap identification, all non-circular) | No | Faithful transfer-matrix `K_P` build (identified as "the correct, unattempted build") | `phase-66-rank-one-escape/RESULTS.md` "D1", "D2", "D3", "Phase 66 net" |
| 67 | Quantum q-index / compact-quantum-group prime current, contractive by Haar/Peter–Weyl | Strict free-product Haar orthogonality destroys arithmetic interference (E67.4 NO-GO); Woronowicz character routes insufficient alone; diagonal q-Shapovalov twist loses log-distance coherence (E67.12) | ABANDONED (several named sub-mechanisms proved insufficient); a forcing-theorem draft (E67.15) reached but not closed | No | Root-of-unity q-algebra intrinsic integer index (E67.10) flagged, not fully pursued | `phase-67-quantum-q-index/README.md` (E67_4, E67_11, E67_12, E67_15) |
| 68 | GLT/pseudodifferential symbol `κ(x,θ)` of the terminal defect `A_N - P_λ`; target `κ≥0` everywhere ⟺ Ω₇ | The object fails the GLT distribution law itself (measure{κ<0}~0.4 for ζ while ind₋=0) — rigorous GLT eigenvalue counting unavailable; corrected to a weaker symbol-depth detector (`min κ→0` marginal for ζ) | ABANDONED (as rigorous GLT route); detector survives informally | No | Analytic form of κ via Γ_q/polygamma vs Euler symbol, planned but not completed | `phase-68-glt-symbol/README.md` "Status update (E68.1-E68.2)" |
| 69 | Exact gauge-robust signed index `ind_-(A_N-P_λ)=0 ⟺ RH`, since the phase-68 symbol turned out gauge-fragile | Confirmed robust/uniform numerically (marginal ~1e-16..1e-21 across gauges) but the forcer (prove `ind_-=0` by structure, uniformly in gauge) was not found; localizes to one frequency θ~π/2 | ABANDONED at the forcer step (a genuine, gauge-uniform exact-signed-index result, see §3 below, but not a proof) | No | Gauge-invariant reformulation via Cayley/Möbius invariance (`w_{1-ρ}=1/w_ρ`), named, not built | `phase-69-exact-signed-index/README.md` |
| 70 | Lee–Yang / de Bruijn–Newman heat-flow forcing: monotonicity of the terminal defect under the heat flow `λ`, combined with Rodgers–Tao's `Λ≥0`, to force `Λ=0` (=RH) | Reduces exactly to an arithmetic q-resolvent identity that is "exactly finite Ω₇ unless an independent Euler/Gamma/fusion evaluation of the resolvent trace is supplied" — pushed further (AHM) to exactly Cauchy–Weil positivity, i.e., restated Weil positivity on Cauchy test squares | ABANDONED / EQUIVALENT-TO-RH (reduces to Weil positivity) | No | none — chain of reductions is exhaustive down to the known wall | `phase-70-lee-yang-dbn/README.md`, `OMEGA7_CLOSURE_PROGRAM.md`, `E70_3...md`, `E70_4_AHM_WEIL_REDUCTION.md` |

### Phases 71–79 (collapsed — see full sub-agent survey; these phases form one continuous
reduction chain around a single terminal statement `Ω₇`, with ~2000 numbered incremental
files sampled rather than read exhaustively)

| phase | mechanism | why it failed | status | over-generalized? | adjacent square never tried | source |
|---|---|---|---|---|---|---|
| 71 | CAND-1 (Connes–Consani–Moscovici zeta spectral triples): push RH content into operator *convergence* `sp(H_x)→{γ}` rather than positivity | 17-step reduction (E71.1–E71.17) to an irreducible "CCM stable divisor identification" / eigenvector-approximation lemma; never closed | PARTIAL-SUCCESS (genuine reduction) | No — deliberately chosen to sit off the positivity wall | The "generic-gap/regularity" Lever B (Tricomi) named but not executed here (moved to phase 74) | `phase-71-cand1-convergence/README.md:104-118` |
| 72 | Feshbach leakage calculus: split explicit-formula/Cauchy–Hilbert pairing into low-frequency (finite cancellation) + high-frequency (Mellin/PNT) estimates | Exact conditional theorem `HF+LF ⇒ target`; neither HF nor LF proved from first principles | PARTIAL-SUCCESS (exact conditional theorem, unconditional implication) | No | A genuinely different high-frequency tool (large sieve / zero density) never tried instead of Mellin oscillation | `phase-72-feshbach-leakage-calculus/E72_63_LOW_HIGH_CAUCHY_HILBERT_CLOSURE.md:162-167` |
| 72 | Balanced remainder / explicit-formula closure identity recasting the classical tail as a finite CCM object, zero-arithmetic-input | Exact identity, but doesn't itself prove polynomial boundedness (`BFW`) | PARTIAL-SUCCESS (exact, unconditional identity) | No | Tauberian/zero-density estimate applied directly to `BFW`, never tried | `phase-72-feshbach-leakage-calculus/E72_340_BALANCED_REMAINDER_CLOSURE_THEOREM.md:140-148` |
| 73 | Cauchy-plane cell residual: pair the CCM eigen-equation against a 2-D "Cauchy plane" to get an exact finite system forcing off-line nodal smallness, contingent on two estimates (`CPINV`, `RCE-cell`) | Both required estimates remain open; a prior tautological ("rowspace") version explicitly rejected | PARTIAL-SUCCESS (exact reduction, one dead end documented) | No | Alternative canonical projection with better-conditioned inverse, untried | `phase-73-cauchy-projection/E73_179_CAUCHY_PLANE_CELL_RESIDUAL.md:150-155` |
| 74 | Hilbert eigenline cancellation (`HPR-DIV`): skew-Hilbert mesh matrix, Cauchy-kernel quasi-eigenvector property, Schur/Tricomi calculus (27-doc arc) | Reduces all the way to `EG_LOCK`/`CCM-ROOT-LOCK`, an irreducible arithmetic divisibility statement; mechanism exhausted (not disproved) | ABANDONED (handed to phase 75) | No — disciplined, explicit non-circularity kill-tests | Higher-order confluent-jet bootstrap tried only to first order, then explicitly refuted | `phase-74-hilbert-eigenline-cancellation/README.md:340-397` |
| 74 | **Planted nodal falsifier (E74.23)** | Zeta: `‖Q_γξ‖`≈1e-15 (roundoff); planted off-line control (`γ0=25,β=0.30`): `‖Q_γξ‖`≈9e-3 to 6e-2, `μ=-5.0` — decisive order-of-magnitude separation | Falsifies the hypothesis that critical nodal cancellation follows from self-adjointness/symmetry alone — it is arithmetic-specific | — | — | `phase-74-hilbert-eigenline-cancellation/E74_023_PLANTED_NODAL_FALSIFIER.md:17-41` |
| 75 | Arithmetic numerator divisibility (`ARITH-LOCK`): bordered-determinant identity for the Weyl numerator, seeking signed Euler/Gamma recombination proving Xi-divisor superpolynomial divisibility | Every escape route collapses back to the same `EG_LOCK`/TPW endpoint or requires the unproved `CAUCHY-COMP` global signed positivity | ABANDONED (theorem-grade autopsy) | No | Independent `ARITH-REM` estimate (not derived from the coupled Feshbach cell), never found | `phase-75-arithmetic-numerator-divisibility/P75_013_015_THEOREM_ASSEMBLY_OR_AUTOPSY.md:37-111` |
| 76 | Normalized adjugate arithmetic lock: scale-free ratio `A_L(z)`, "safe-axis" calculus entirely in `Re s>1`; `SR-SAFE ⇒ Ω₇` | `SR-SAFE` (P76.034) is a clean unconditional-machinery closure theorem ("no eigenvector scale, no value of Ξ(1/2), no fitted constant"), but inserting the actual Gamma-prime/Euler formula and proving log-convergence was never completed | PARTIAL-SUCCESS (cleanest non-circular endpoint in the whole 71–79 arc) | No — self-audits that some sub-steps were "renamings, not reductions" (P76.063/065/066) and stops deliberately | none flagged besides the arithmetic insertion itself | `phase-76-normalized-adjugate-arithmetic-lock/PHASE_76_CLOSURE.md:20-76` |
| 76 | Ambient bordered-inverse norm route (P76.061) | Numerical autopsy: ambient norm overestimates true safe error by up to **1e28** | NUMERICAL-ONLY kill (no impossibility theorem) | — | Is there a provable multiplicative gap, or was 1e28 a test-vector artifact? Untested | `phase-76.../P76_061...md` (per closure) |
| 77 | Weyl limit-point (LP) + IDENT split; ~80-document "detector spiral" (E77.5d–5ah, E77.7aa–ay) building build-discriminating scalars (sign/cone chains, shell-mismatch laws) | The attribution gate E77.7az proves these are **detectors, not forcing mechanisms** — their build-separation power is "surplus zero-location information," ruled inadmissible by the program's own zero-filter gate (E72.16) | ABANDONED (self-flagged over-generalization) | **Yes, explicitly** — "precisely the pattern the phase-size discipline warns against" | Build-neutral compact-resolvent + disk-contraction argument (suggested by phase 78), never executed inside phase 77 | `phase-77-weyl-limit-point/PHASE_77_CLOSURE.md:52-89` |
| 78 | Build-neutral LP interface + IDENT decomposition — correcting phase 77's claim of build-neutrality | Subclauses (c) pencil compatibility and (e) simplicity-at-μ_L are themselves detectors pinned to `μ_L` — "the program LOST two tools and kept the requirement... a DEFICIT" | ABANDONED (subclauses c,e); PARTIAL-SUCCESS elsewhere (subclause a proved build-neutral) | No — itself a correction of phase 77's over-generalization | "mu-free replacement" (scenario S1) proposed, never attempted | `phase-78-build-neutral-lp-and-ident/README.md:51-83` |
| 78 | μ_N→0 quasimode program (naive Λ(n) and three kernel-derived variants) | All variants fail for both builds at every tested L; one weak L=8 signal separates builds but doesn't feed the min-max argument | PROVED-IMPOSSIBLE for the tested family (autopsy); μ_N→0 itself remains OPEN | No | A quasimode built from the operator's own kernel (not pointwise sampling), untried | `phase-78-build-neutral-lp-and-ident/README.md` (E78.137-141) |
| 79 | GAP-Z shared convergence lemma: build-neutral summability of the Poisson-sum-over-spectrum term `ZERO(σ)` | `MESH`,`BND` proved build-neutral; but `ZERO` (the sole build-dependent piece) only numerically observed near a borderline exponent p≈1.2, not proved >1 | NUMERICAL-ONLY (GAP-Z open; two dead-end bounds proved dead) | No | Root-displacement/cloud-level route (E79.2-E79.3), named "the live handle," not completed | `phase-79.../README.md:88-148`, `E79_117_POST_AUDIT_LEDGER.md:38-45,62` |
| 79 | IDENT discriminant `c_N` (codimension-one signature) and single-signedness of `M_N·x`, tested against two independent planted off-line controls | Robust and falsifier-passing on the audited ladder N=8..18, but explicitly **not a theorem** — `c_N` is not monotone/geometric, no convergence law extracted | PARTIAL-SUCCESS / NUMERICAL-ONLY | No — self-corrects earlier over-strong "c_N→0" language | Deriving `GEOM` structurally from the balanced secular package, named, not executed | `phase-79.../E79_83_CODIM_ONE_CLOSURE_SIGNATURE.md`, `E79_89_CLOSURE_BALANCE_TO_GEOM.md:157-175` |

### Phases 80–92 (small, tightly-argued phases; no numbers files, all closures self-contained)

| phase | mechanism | why it failed | status | over-generalized? | adjacent square never tried | source |
|---|---|---|---|---|---|---|
| 80 | Relative-determinant identification (`RDI-ANCHOR`) via bilateral relative-determinant equivalence + independent Euler–Gamma product `E_L` | Coherence + summable spectral convergence alone insufficient to identify the arithmetic limit; reduces to A1–D3 | PARTIAL-SUCCESS (reduction) | No — proved as a negative theorem (C4) | Build-neutral proof of each of A1,C1,C2,D1–D3 independently, before combining | `PHASE_80_CLOSURE.md:28` |
| 80 | μ-free disk-intersection bypass of the dimension-one/normalization step | Full-solution disk uniqueness forces dimension one and nonzero normalization — bypass provably impossible | PROVED-IMPOSSIBLE | No | none (closed) | `PHASE_80_CLOSURE.md:33-34` |
| 81 | Zeros of the bordered secular determinant as an independent arithmetic measure | Defining the target shift by inverse Stieltjes transform reintroduces the target — **circular** | EQUIVALENT-TO-RH (refuted as circular) | Yes — flagged explicitly; re-examinable if a non-circular target-shift definition is found | A genuinely independent (non-transform) definition of the even spectral shift | `PHASE_81_CLOSURE.md:28,72-73` |
| 82 | Leading projective cluster-convergence route to identify limiting profile with `k_L` | Reintroduces exactly the LP + radical-tail obligations of Phase 80 — a loop | ABANDONED (loop) | No | Two-term generator coboundary expansion retaining the source (Path B, tried next) | `PHASE_82_CLOSURE.md:23-24` |
| 83 | Gamma–Euler intertwiner (`TWO-GENERATOR-ARITHMETIC-COBOUNDARY`) — see deep dive §4 | ker of the multiplication-by-`t` operator is {0} on L²(0,L): a **domain obstruction**, not an estimate gap | PROVED-IMPOSSIBLE (Hilbert-space form) | No — explicitly not called "an estimate awaiting improvement" | Distributional repair (pursued next phase, 91) | `PHASE_83_CLOSURE.md:37-40` |
| 84 | Endpoint-source identity from `δ_0` Euler orbit reproducing the exact coupled source | Succeeds as construction; residual scalar leakage does not monotonically shrink under cluster enlargement | PARTIAL-SUCCESS | No | Genuine cofinal-rank existence proof (`COFINAL-PARITY-CLUSTER`) | `PHASE_84_CLOSURE.md:47-49` |
| 85 | Uniform (pointwise) control of moving-pole Weyl-defect bound as sufficient for cross-parity cancellation | Finite exact diagnostics show pointwise scales can remain huge while the true safe scalar is already small — over-strong requirement | ABANDONED (over-strong) | Yes — flagged as replacing the theorem with a stronger claim than needed | Direct signed Abel cancellation without uniform bound (pursued in phase 86) | `PHASE_85_CLOSURE.md:34-36` |
| 86 | First-complementary-mode localization of the signed spectral Abel variation measure | Succeeds in isolating first-mode terms + a strictly lower-variation tail; the tail estimates (FM-E, FM-O) remain open | PARTIAL-SUCCESS | No | d₂ tail estimates independently | `PHASE_86_CLOSURE.md:25-29` |
| 87 | Naive implication "spectral single-signedness ⟹ arithmetic identification" | False implication | PROVED-IMPOSSIBLE | No | none | `PHASE_87_CLOSURE.md` / README |
| 88 | Single common two-parity scaling to resolve the deformation layer | Parity entries live on distinct scales; common scaling gives a singular limit, fails the fixed-pencil hypothesis | PROVED-IMPOSSIBLE (for that hypothesis) | No | Nested even/odd layer limits with independent scales (transferred) | `PHASE_88_CLOSURE.md:17-19` |
| 89 | Scale separation alone implying a matched window exists | Does not by itself prove a matching window; existence is a separate obligation | ABANDONED (demoted to open obligation) | No | Direct existence proof of the matched-width window `DOM-E` | `PHASE_89_CLOSURE.md:44-47` |
| 90 | Static Feshbach eigenline: scalar eigenvalue motion rotating the spectral line | No off-diagonal matrix element between orthogonal eigenvectors — does not rotate the line at all | PROVED-IMPOSSIBLE (as contributing mechanism) | No | none | `PHASE_90_CLOSURE.md:17-19` |
| 91 | Euler-gauge derivation formula applied directly to a nonzero physical resonant vector | ker X={0} for nonzero physical vectors — the phase-83 distributional repair does not transfer to the physical line | PROVED-IMPOSSIBLE (no-bypass theorem) | No | LINE-EULER-COBOUNDARY reduced-leakage term, transferred, open | `PHASE_91_CLOSURE.md:29-33` |
| 92 | Dominant-eigenline/matched-width tracking, required hypothesis for the endpoint limit | Removed entirely by projectivizing the full Feshbach cluster — DOM-E, DOM-M, matched-width were never logically necessary | ABANDONED as unnecessary (genuine simplification, not refutation) | No | CA-1 fixed-L projective convergence, still open, final target of the chain | `PHASE_92_CLOSURE.md:36-41` |

### Phases 93–101

| phase | mechanism | why it failed | status | over-generalized? | adjacent square never tried | source |
|---|---|---|---|---|---|---|
| 93 | Direct identification of normalized bordered determinant with `E_L`, bypassing fixed-L convergence, GAP-Z, LP, RDP-SHELL | Removes infrastructure but `DIRECT-BORDERED-ANCHOR` itself left open — no proof it converges | PARTIAL-SUCCESS (E93.002: `DIRECT-BORDERED-ANCHOR ⟹ Ω₇ ⟹ RH` unconditionally) | No | Non-bordered (purely spectral) route to the same ratio | `E93_002_DIRECT_CLOSURE_THEOREM.md:52-60` |
| 94 | Rank-two cofactor displacement law expressing bordered numerator via `adj(M)` only (inverse-free) | Does not produce a termwise Euler identity; differentiated cofactor pieces remain coupled | PARTIAL-SUCCESS (algebra closed, arithmetic open) | No | Symmetrized/antisymmetrized cofactor split, untried | `PHASE_94_CLOSURE.md:162-183` |
| 95 | Absorb moving finite level as algebraic branch of characteristic determinant, via implicit-function Jacobian | Removes eigenvector/Hellmann–Feynman machinery but leaves the signed Gamma–Euler evaluation of the determinant Jacobian open | PARTIAL-SUCCESS | No | Multi-branch (non-simple eigenvalue) case, untried | `PHASE_95_CLOSURE.md:239-271` |
| 96 | Expand characteristic Jacobian as exact von Mangoldt sum, linear in prime direction | The sum-decision `BASE+ΣΛ(n)...→0` is exactly the still-open target | PARTIAL-SUCCESS | No | Direct comparison to explicit-formula error terms, untried | `PHASE_96_CLOSURE.md:325-351` |
| 97 | Collapse prime sum into one trace-commutator `Tr(K H_P)` via cyclicity of trace | Produces an unspecified "canonical boundary object" rather than closing the sign | PARTIAL-SUCCESS | No | Hilbert–Schmidt norm bound on the commutator, untried | `PHASE_97_CLOSURE.md:388-434` |
| 98 | Exact Fourier-shell/internal commutator split | Isolates exactly four Fourier crossings but doesn't estimate them | PARTIAL-SUCCESS | No | Asymptotic (non-exact) shell estimate, deliberately not tried | `PHASE_98_CLOSURE.md:469-507` |
| 99 | Adjugate sandwich identity for the internal commutator against Γ–Euler boundary sources | Leaves one bilateral scalar unproved | PARTIAL-SUCCESS | No | none flagged | `PHASE_99_CLOSURE.md:541-587` |
| 100 | Identify characteristic-adjugate commutator as signed spectral projection `-Π_t` | Confirms it is *not* a new arithmetic source — recombination needed, not a proof | ABANDONED (clarifying negative result) | No | none | `PHASE_100_CLOSURE.md:615-656` |
| 101 | Two-set/one-interval safe closure theorems (`LOCAL-COVARIANT-IDENT` on one interval ⟹ Ω₇) | Correctly reduces the whole program to one scalar identity, never proves it | PARTIAL-SUCCESS (airtight logic) | No | none — only the identity itself is open | `E101_019_ONE_INTERVAL_CLOSURE.md:20-33` |
| 101 | Scalar Pearson differential equation for the Weil prime distribution | Theorem 2.1: any polynomial Pearson pair forces σ=0, τ=0 (infinitely many distinct prime-power atoms) | PROVED-IMPOSSIBLE | No | Nonlocal (shift-type) Pearson-like law, untried | `E101_070_PEARSON_THETA_CLOSURE_NO_GO.md:47-98` |
| 101 | Theta heat-equation finite recurrence for radical Fourier coefficients | Projects to an infinite dense Fourier convolution — not a finite-band closure | PROVED-IMPOSSIBLE (as finite-band closure) | No | Artificial variable-coefficient recurrence, not excluded but unconstructed | `E101_070...:296-320` |
| 101 | Beta-mixture/Hausdorff moment discriminant for Stieltjes representability | A geometric Hausdorff sequence obeys every finite-difference sign but has NO Stieltjes representation | PROVED-IMPOSSIBLE | No | Mixed/indeterminate moment problem, untried | `PHASE_101_LEDGER.md` (E101.033) |
| 101 | Source-adapted exact exterior Abel identity | Equals `B_y/B_k - 1`, i.e. IS the terminal secant itself — circular | EQUIVALENT-TO-RH | Yes — restates rather than approximates the target | none — dead end acknowledged | `PHASE_101_LEDGER.md` (E101.065) |
| 101 | Full-jet phase-Gram positivity detector | Gram vanishes on the real axis, but requiring it to vanish on the Xi divisor is "simply RH rewritten" | EQUIVALENT-TO-RH | Yes | none | `PHASE_101_LEDGER.md` (E101.077) |
| 101 | Positive star / normal-adjoint construction before divisor extraction | Rank-one parity contraction identically zero at finite level — reduces to `XI-PARITY-CURRENT-NULL ⟺ RH` | EQUIVALENT-TO-RH | Yes | `TRUE-DIVISOR-IDENT`, flagged as only remaining bridge, untried | `PHASE_101_LEDGER.md` (E101.093) |
| 101 | Nonnormal companion-adjoint (eigenvector-overlap) conjugate-graph substitute | Exact false positive found on an explicit all-real symmetric divisor `(w²-1)(w²-4)` | PROVED-IMPOSSIBLE (disproof by explicit counterexample) | Yes — a previously plausible mechanism refuted | Normal-adjoint construction, tried next | `PHASE_101_LEDGER.md` (E101.092) |
| 101 | **E101.035 planted heat falsifier** | Beta-mixture discriminant correctly **rejects** an artificially planted off-line zero (`z=0.4+3i`) — mechanism passes its own falsifier test | (test passed; underlying arithmetic vanishing still OPEN) | No | — | `E101_035_PLANTED_HEAT_FALSIFIER.md:49-122` |
| 101 | **E101.070 Pearson/theta no-go** (task-specified deep dive) | See rows above; declares refuted: fixed scalar polynomial Pearson equations, finite-band closure from the heat equation, constant-coefficient tail recurrences, IBP without full right-bordered collar, fixed-order endpoint differences as discriminant, operator-norm smallness of Γ–Euler commutator | PROVED-IMPOSSIBLE (frozen list, §9) | No | Nonlocal multiplicative Γ–Euler connection of E83.004–007 retained as not-refuted | `E101_070...md:474-480` |

### Phases 102–109

| phase | mechanism | why it failed | status | over-generalized? | adjacent square never tried | source |
|---|---|---|---|---|---|---|
| 102 | Direct A1 signed-core inequality (Laguerre coefficient sign) via ~300 reformulations (Toeplitz, Fejér, Schoenberg, Herglotz, de Branges, Pick–Stieltjes, Loewner–Schur...) | Every route reduces to the same open compact-A1 target; the phase proves many reformulations are literally equivalent, not distinct attempts | ABANDONED / reopened EQUIVALENT-TO-RH | No | A non-symmetrized continuation-side bilinear pairing (only isolated in 108/109) | `102_A1_SIGNED_COMPENSATION_MECHANISMS.md` |
| 102 | Zero-side Li criterion (critical-line ⇒ λ_n≥0 geometrically) | Proves only Li⇔RH equivalence; the arithmetic (A1) side remains open | PARTIAL-SUCCESS (zero side fully closed) | No | none | `139_ZERO_SIDE_LI_CRITERION_CLOSURE.md:117-129` |
| 102 | Global half-plane positivity `Re(ξ'/ξ)(s)≥0` for Re s>1/2 (Toeplitz/Herglotz disk form) | Proved exactly EQUIVALENT-TO-RH; constructing the positive measure non-circularly is the open problem | EQUIVALENT-TO-RH | No | Constructing ν_ξ from Euler–Gamma data directly, unsolved | `174_LOG_DERIVATIVE_HALF_PLANE_POSITIVITY_GATE.md:104-197` |
| 102 | Fejér/log-density closure (conditional: positive increment measure + log-density coefficient a>1/2) | Conditional only; Tauberian gap (Abel≠Fejér) blocks transfer | PARTIAL-SUCCESS (conditional) | No | Anti-concentration/Carleson-window construction, reduced not solved | `259_FEJER_LOG_DENSITY_CLOSURE_THEOREM.md:274-281` |
| 102 | Selberg convolution, Turán–Riccati, Jensen/heat-flow (Newman), Hermite–Biehler, Poisson–Carathéodory support, bordered Euler current | Each a distinct no-go: signed Laguerre-kernel obstruction, Schur-complement rigidity, or an independent HB/support construction not derivable from arithmetic | PROVED-IMPOSSIBLE (each, as stated) | No | Selberg with a genuinely new signed input for real weights Λ, flagged untried | `PHASE_102_EXECUTION_PLAN.md` |
| 103 | Direct A1 via oriented Laguerre-lobe transport, reduced to `∫E(u)K_n(u)du ≤ q(n)` | Unconditional proof requires square-root cancellation for `Σe^{ρu}/ρ²` (RH-strength); RH-conditional proof given but with an uncertified finite gap 150≤n<n_eff | EQUIVALENT-TO-RH (the missing step is itself RH-strength) | No, precisely characterized | Certifying the finite gap rigorously, recommended not done | `103_07_CLOSURE_LEDGER_AND_FINAL_DEDUCTION.md:123-138` |
| 103 | ~40 exploratory theta/Jensen/Selberg/Vaughan–Heath-Brown/von-Mangoldt-quantile mechanisms | Each an exact no-go with explicit sign-witness (log-concavity stops at PF2, cubic Jensen fails, Selberg square self-cancels, etc.) | PROVED-IMPOSSIBLE (individually) | Some flagged possibly over-narrow (e.g. 103_47: only *translation mixtures* shown to fail) | Correlated multi-order theta tail with new discriminant sign input | `103_07...README.md` |
| 104 | ~80 "cociclo"/positivity mechanisms (Jordan cocycle, Möbius–divisor Gram, Selberg–Riccati, Stein–Mecke, Fejér–Carathéodory, size-biased martingale, Fermi/entropy, Bernstein pressure, Hadamard–Jensen semigroup) | Each closed by an explicit stop-gate/witness — several individually equivalent to RH (e.g. holomorphy on complete disks ⇔ RH) | ABANDONED / several EQUIVALENT-TO-RH | No — carefully audited | A genuine density-nulling theorem for prime–pole overshoots, never closed | `PHASE_104_CLOSURE.md:90-107` |
| 105 | Off-line-zero ⇒ exponential growth of |λ_n| (contrapositive route) | Only the zero-side implication (¬RH⇒unbounded) proved; the needed prime-side subexponential bound is open | PARTIAL-SUCCESS (one-directional) | No | Literal Λ(p^k) non-resonance inequality, isolated but not attacked | `105_02_OFF_LINE_ZERO_EXPONENTIAL_THEOREM.md` |
| 105 | Bregman/nodal-flux resonance gate on zero-free Euler approximants | Adaptive linear correlation can still resonate at exp{R/2-η(R)}; positive atomic countermodel realizes the loss | PROVED-IMPOSSIBLE (positivity+PNT+renewal+quadratic-variation route) | No | Non-resonance inequality with literal Λ(p^k) values | `README.md` (105_05) |
| 106 | Global modular star / operator-valued Γ-boundary program — see deep dive §4 | 106.205 negatively closes the charged-Tate-boundary branch (106.203/106.204); phase-120 annotation flags 106.203/106.204 as using the *wrong* Gram mass `log(p)/p^k` instead of the physical `log(p)/p^{k/2}` needed for row (d) | ABANDONED (this branch) / PARTIAL-SUCCESS (program-wide, see §4) | **Yes** — explicitly flagged over-generalized/miscalibrated for row (d) | Correct `log(p)/p^{k/2}` Gram-mass version, flagged by phase-120, not built | `106_205` (README lines 2413-2429); phase-120 warnings in 106_203, 106_204 |
| 107 | Arithmetic-Lefschetz reconstruction: build a Weil-radical-free divisor whose arithmetic self-intersection reproduces `Q_W(f)`, invoke Faltings-Hriljac/Yuan-Zhang | No finite Eulerian/valuative local packet realizes the true local arithmetic target once the Tamagawa number is retained — proved by explicit real elliptic-curve counterexamples | PROVED-IMPOSSIBLE (for the "row-c" legacy source grammar) | No — real-curve-verified | A genuinely new Galois-sensitive channel (mod-32 minimal-model residue), opened but only partially built | `107_133_CURRENT_ROW_C_CLOSURE_GATE.md:78-80` |
| 108 | Row-(a) global rational-function/divisor theory over ℤ, staged 0–7 | Stage 2 fails negatively; Stage 5 fails by two independent routes; the constant term `Σ_p C_p` resists three independent regularizations by a proved structural bulk/boundary-accumulation obstruction | ABANDONED (0 of 4 rows closed) | No — two initially-claimed positives (G2, G4) retracted as circular/contentless (§ below) | Stage 6 (row d, primitive inequality) opened with two proved entry prohibitions, not attempted | `108_99_PHASE_108_SUMMARY.md:1-141` |
| 109 | One-sided bilinear pairing `B(f,g)=ΣΛ(n)f(n)g(n)` from shell functionals k≥1 only, testing whether excluding the identity shell gives a zero-determined radical | Radical is prime-power-determined, not zero-determined, for every kernel on prime powers; explicit witness `F=sin(πx)` is zero-free at every zero of ξ | PROVED-IMPOSSIBLE (hypothesis cleanly refuted, non-numerically) | No | Continuation-side, non-symmetrized, zero-free-by-definition pairing, identified as corrected target, not built | `109_99_PHASE_109_SUMMARY.md:1-49,109-142` |

---

## 2. "Promising but not pursued" / "future work" / "untried" — quoted lines

The corpus almost never literally uses these phrases; it uses "OPEN," "live target," "next candidate,"
or names an explicit unbuilt object. Genuine hits and functional equivalents:

- `phase-101-covariant-bordered-current/E101_071_EXPLICIT_QUARTET_LOEWNER_RESPONSE.md:418-420` — "Consequently, separately estimating the quartet and boundary terms would fight a forced cancellation. **Future work** must begin from the already recombined right side of (7.3)."
- `phase-107-arithmetic-lefschetz-reconstruction/107_235_DIRECT_DIVISOR_SHEAF_TO_PERIODIC_H0_NO_GO.md:95-97` — "that paper explicitly leaves the descent of Frobenius eigenspaces to `C_p` and their relation with the periodic geometry for **future work**. It therefore supplies the scalar/analytic bridge for structure functions, not the divisor-module comparison required here."
- `phase-108-row-a-construction/108_51_STAGE_5_WHAT_WOULD_CLOSE_IT_AND_THE_DESIGN_PRETEST.md:188-190` — "Conditions I–III of §2 ... proving any of them is **future work**, not attempted here."
- `phase-108-row-a-construction/108_04_WELL_POSEDNESS_VERDICT.md:127-130` — "there is now a named, explicit, zero-free-constructed candidate `Prin(𝒢)` for **future work** to test against, once `I_∂` is extended."
- `phase-108-row-a-construction/108_23_THE_SMEARED_PAIRING_CONVERGENCE_AND_THE_ZERO_SOURCE_DICHOTOMY.md:192-196` — "It is recorded as open, for **future work**, and is not needed for anything claimed in this Phase."
- `phase-108-row-a-construction/108_00_PHASE_108_PLAN.md:120-128` — "the one **untried** lemma (row c, cheap, parallel): 108.30 — Component-triviality ... Named as the escape in 107_144 §5; **never attempted**."
- `phase-73-cauchy-projection/E73_179...` / `phase-77.../PHASE_77_CLOSURE.md:52-89` — E77.8 (falsifier sweep), E77.9 (non-circularity audit), E77.10 (assembly) planned in phase 77 but only partially executed later (phase 79, E79.116/117).
- `phase-78-build-neutral-lp-and-ident/README.md:51-67` — scenario S1: "A2(f) can be re-derived from the mu-free remnant (a) + NEUTRAL-GROUND-CAUCHY... **NOT DONE**."
- `phase-79-shared-convergence-and-ident-discriminant/E79_89_CLOSURE_BALANCE_TO_GEOM.md:154-155` — "the immediate next move is not another geometry proxy search, but a direct attack on how the balanced secular package shapes the K_N cloud" — untried at phase close.
- `phase-102.../104_13` (per phase-104 survey) — "no descarta todo posible teorema acoplado especial para los pesos reales" (does not rule out every possible coupled theorem for the real weights) — a genuinely open door, not pursued further.
- `phase-61-open-problems/R10_bandedge_closure.md` — "Ver R11 (ángulo Weyl/homogeneización) para el intento siguiente" — R11 is a named next attempt for the band-edge route.

---

## 3. Every PARTIAL SUCCESS — exact scope and what blocked extension

1. **Phase 62 — quaternionic Hodge–Riemann polarization (E92–E94).** ζ's finite-window Weil
   matrix `A` is genuinely **positive-semidefinite on `V₊`** (the `+i`-eigenspace of the
   quaternionic structure `J`, `J²=-1`), at every tested finite window λ, while the
   Davenport–Heilbronn falsifier and a symmetry-matched random control both fail (are
   indefinite). This is real, non-circular, non-random positivity — "the clearest intrinsic
   appearance of Weil/Hodge–Riemann positivity in the program." **Blocked by:** the positivity
   is *gapless* — the spectral margin cascades `e^{-cL}`→0 with ζ sitting exactly at
   `μ_max(L_prime,L_arch)=1` from below (marginal). Giving `V₊`-positivity a uniform gap
   without using zero locations requires the Spec-ℤ cohomological realization (MW-5), which
   is exactly the object phase 63 shows does not exist as a Hard-Lefschetz operator.
   `phase-62-cesaro-closure/README.md:35-46`.

2. **Phase 66 — rank-one escape dichotomy (D1/D2/D3).** The easy direction (¬RH ⟹ escape norm
   `sup_P‖P_prim K_P P_prim‖` unbounded, growth `λ^{2β-1}`) is proved, and a faithful proxy
   detector confirms ζ bounded / DH unbounded with the off-line escape direction numerically
   confirmed **orthogonal to the pole direction H** (μ_max essentially unchanged by removing
   the pole, 5.356→5.357). **Blocked by:** the full sharp dichotomy and its faithful
   transfer-matrix `K_P` were never built; the escape theorem itself remains RH-strength on
   all three faces (A,C→MW-2, B→MW-5). `phase-66-rank-one-escape/RESULTS.md`.

3. **Phase 76 — `SR-SAFE ⇒ Ω₇` (P76.034).** Exact unconditional theorem: if a specific
   finite-section limit converges locally uniformly in the region `Re σ>1/2` of absolute Euler
   convergence (no critical-line evaluation, no eigenvector-scale ambiguity), normal families +
   Hurwitz force all zeros onto the line. **Blocked by:** the arithmetic content (inserting the
   actual Gamma-prime/Euler formula and proving the limit) was never supplied. `PHASE_76_CLOSURE.md:20-76`.

4. **Phase 93 — E93.002 direct closure theorem.** Proves
   `DIRECT-BORDERED-ANCHOR ⟹ Ω₇ ⟹ RH` unconditionally, using only `E_L→(2ξ)²`, finite
   real-rootedness, safe-axis domination, and Hurwitz, genuinely removing several prior
   hypotheses. **Blocked by:** `DIRECT-BORDERED-ANCHOR` itself (projective convergence of the
   bordered determinant to the Euler–Gamma product) is unproved. `E93_002_DIRECT_CLOSURE_THEOREM.md:52-60`.

5. **Phase 101 — E101.010/013/019 (two-set/one-interval safe closure).** Proves that
   identification of the bordered characteristic with `[Ξ(1/2+σ)/Ξ(1/2+σ₀)]²` on **any single
   nonempty open interval** already yields full normality + Hurwitz ⟹ Ω₇, with no separate
   compactness/mass-bound hypothesis. **Blocked by:** `LOCAL-COVARIANT-IDENT` (the pointwise
   identification on even one interval) is never proved. `E101_019_ONE_INTERVAL_CLOSURE.md:19-33`.

6. **Phase 102 — zero-side Li criterion / σ>1 half-plane positivity.** `Re(ξ'/ξ)(s)≥0` proved
   *unconditionally* for `Re s>1` (`177_UNCONDITIONAL_SIGMA_GT_1_POSITIVITY.md`), and the
   Li⇔RH equivalence fully closed on the zero side. **Blocked by:** exactly at the strip
   `1/2<Re s≤1`, where an off-line zero would force a sign-changing pole defect.

7. **Phase 103 — RH-conditional Laguerre-coefficient closure.** Proves `C_n(T_n)≥0` for all
   n≥150 *assuming* RH, with an explicit (if astronomically large) effective bound. **Blocked
   by:** unconditionally needs square-root cancellation of `Σ_ρ e^{ρu}/ρ²` (Open problem
   103-X); even the RH-conditional proof leaves the finite range 150≤n<n_eff uncertified.

8. **Phase 105 — zero-side exponential growth theorem.** `¬RH ⇒ limsup|λ_n|^{1/n}>1` proved
   unconditionally. **Blocked by:** the needed converse direction (a prime-side subexponential
   bound) is not attacked.

9. **Phase 108 — Stage 1/3/4 sub-results.** Character classification forced trivial (no
   log-periodic escape); Stage-1 bridge identity finite with the divergent constant
   contributing zero at finite regularization depth; Tate-correspondence assembly proved equal
   to `-ζ'/ζ(s)` exactly; regularized-determinant/Gamma-factor identity derived from first
   principles. **Blocked by:** the residual constant `Σ_p C_p` is a genuine bulk/boundary-
   accumulating divergence resistant to three independent repair mechanisms (Stage 1); no route
   supplies an actual intersection number (Stage 5).

10. **Phase 109 — Step 1 (bilinear pairing existence).** A genuine pairing
    `B(f,g)=ΣΛ(n)f(n)g(n)` proved to exist non-circularly, matching phase 108's known value at a
    specialization. **Blocked by:** Step 2 shows the radical is prime-power-determined, not
    zero-determined, for every kernel on prime powers — closing the route rather than stalling it.

---

## 4. Special deep dives

### Phase 63 — Lefschetz realization ("the missing Lefschetz operator")

Phase 63's own framing: phase 62 showed the finite-window Weil matrix `A` carries **the right
positive structure** (PSD on `V₊`) but only *gaplessly/marginally* — `max μ(Lprime,Larch)=1`
exactly, "the master wall." Phase 63's diagnosis:

> "we **have** the polarization data `(A, J)`; what we **lack** is what turns a polarization
> into a *Hodge index theorem with a gap*. In every case where RH-type positivity is a
> theorem — curves over `F_q` (Weil), Kähler manifolds (Hodge) — the gap is forced by a
> **Lefschetz operator `L`** generating an `sl₂` action with **Hard Lefschetz**. Over `F_q`
> that operator is the Frobenius/hyperplane class; over Spec ℤ there is no such operator (no
> Weil cohomology). **That absence is MW-5.**" (`phase-63-lefschetz-realization/README.md`)

R1 (E97): the candidate scaling operator (spectrum = zeros) **anti-commutes** with `J`
(exact, ratio 2.000) — it is complex-antilinear, "the wrong type to be Frobenius." R3: three
real curves over `F_q` have `[F,J]=0` exactly, PD-gapped polarization, `|eig|=√q` — confirming
the contrast is real, not an artifact. Verdict:

> "no J-linear Frobenius isometry of a gapped polarization on the ζ window — that object would
> be the Frobenius of the Connes–Consani arithmetic site / Deninger cohomology, which is not a
> realized object: this is **MW-5**, now stated and demonstrated by direct contrast."

R6 (E99), the "squaring lever": since the antilinear operator `D` has `D²` J-linear (spectrum
`γ²`, `RH⟺D²⪰0`), squaring moves zeros into the J-linear sector — but that sector is *also*
gapless (relgap ~1e-12), sector-independent. Deepest statement of the wall:

> "A spectral gap needs finitely many eigenvalues. A curve over `F_q` has finite genus `g`...
> ζ has infinitely many, accumulating zeros ... so its polarization margin → 0 as λ grows —
> **gaplessness is the analytic shadow of Spec ℤ having "infinite genus".** The crossing needs
> ... an candidly infinite-dimensional *regularized* positivity (Deninger regularized
> determinants), not a finite gap — a theory problem beyond numerics."

**Missing object:** a Weil-cohomology-style **Lefschetz/Frobenius operator over Spec ℤ**
(equivalently, a Deninger regularized-determinant infinite-dimensional positivity) that would
force the spectral gap the way the hyperplane class does over `F_q`. No such object is known
to exist; the phase stops here by design ("no crossing within reach of numerics").

### Phase 64 — Connes' route (trace formula / colligation)

Binding erratum (from phase 106) placed at the top of the phase README:

> "The finite 'self-adjoint perturbation determinant = critical Euler factor' bridge in
> `CANONICAL-FOUNDATION.md` §3 is false in the stated operator class. A relative perturbation
> determinant of two self-adjoint operators is holomorphic and nonzero off the real axis,
> whereas `(1-p^{-1/2-iz})` has zeros at `2πk/log p + i/2`. ... Consequently every statement
> below depending on the finite Tate perturbation-determinant identification is conditional on
> a replacement global, non-factorized cohomological construction." (`phase-64-connes-route/README.md:1-9`)

The phase's target (as re-stated after this correction): realize Ξ as the structure function of
a **positive canonical system** ⟺ the negative Kreĭn–Langer index `κ` is *continuous* through
the rank-one pole renormalization of the positive von Mangoldt system. Task A closure proves
`L1 ⟺ RH` unconditionally (Paley–Wiener nonvanishing lemma proved unconditionally). The
Connes-round-3 sharpening replaces the marginal boundary index `μ_max=1` with an exact integer
Kreĭn–Langer negative-square count `ind₋(K_{S_κ})`, verified `=0` for ζ and `=2k` for k planted
off-line zeros — "an exact integer count, robust." Final status:

> "L1 **is** an RH criterion (A); finite-window positivity = edge-contractivity (B); canonical
> Hamiltonian marginal at the boundary (C); DH violates with the predicted `λ^{2β−1}` drift ...
> No 1st-order J-linear zero operator (D). **The crossing is now precisely: construct the
> Euler-product/adelic unitary colligation whose Schur function `S_λ` is contractive by
> Hilbert-space geometry** — a theory construction (Connes–Consani / adelic scattering) that
> numerics can scaffold and falsify-test ... but not carry out." (`README.md`, "Status" section)

**Missing object:** a genuine **Euler-product/adelic *matrix* (not scalar) unitary
colligation** whose Schur function stays contractive under continuation to the critical
value ω=0 — the E109 test shows the scalar finite-prime criterion diverges exactly at ω=0,
confirming "the matrix colligation + renormalization is essential (the open Gram step)."

### Phase 83 — Gamma–Euler coboundary

Objective: construct the `TWO-GENERATOR-ARITHMETIC-COBOUNDARY` via the
`GAMMA-EULER-INTERTWINER` — transport the scale derivation in the Euler semigroup
representation to the actual CCM complement on the single vector needed by the coupled source.
Builds an exact, zero-free chain (truncated shift semigroup → Euler unit/Möbius inverse →
von Mangoldt connection → prime CCM matrix → Gamma–Euler boundary commutator), then proves the
key negative result:

> "The gauged commutator is not small in operator norm. For a fixed shift in the interval
> `(log 2, log 3)`, E83.007 proves `norm(M[S_y^*,Z]) ≥ 2^{-σ}`. ... The obstruction is an
> exact uncancelled `k=2` endpoint wedge." (`PHASE_83_CLOSURE.md:19-26`)

The abstract intertwiner criterion requires a nonzero vector annihilated by multiplication-by-`t`:

> "`ker X = {0}` in `L²(0,L)`. Therefore the Hilbert-space form of the proposed one-vector
> construction is trivial. This is not an estimate still awaiting improvement; it is a domain
> obstruction." (`PHASE_83_CLOSURE.md:37-40`)

**Missing object:** a genuine ground vector for the scale derivation — repaired only
distributionally (`ker X = span{δ_0}` in the distributional extension, giving an exact
left-endpoint mass), i.e. the needed object is fundamentally a **distribution, not a
Hilbert-space vector**; the arithmetic anchor and Ω₇ remain open even after this repair
(`PHASE_83_CLOSURE.md:46-52,74-75`).

### Phase 106 — Global modular-star audit

Objective (README opening): test the only spectral construction left by the Phase 101 trace
no-go — construct a positive Hilbert realization with generator `Θ` satisfying
`Θ*=1-Θ`, `det_∞(s-Θ)=e^{a+bs}ξ(s)`, from Euler–Gamma source data, without zero labels.

This is the largest phase in the corpus (documents 106.00–106.210+), an unbroken chain of
successive constructions each closed by an explicit no-go or handed forward. Key milestones
directly relevant to the task's named files:

- **106.196–198 (operator-valued Gamma boundary pushout):** upgrades a scalar archimedean
  boundary compliance to a complete operator-valued Gamma compliance, closing "the full Gamma
  boundary row, its minimum right inverse, and the finite operator-valued pushout without zero
  input." Ends: "Still required: pull back (17) through the derived CCM localization ...; prove
  that its alternating form equals the CCM residue alternating form; prove that the resulting
  Hilbert completion retains the separated CCM quotient. **The last two clauses are now the
  sole global Hodge-index comparison.**" (`106_198_OPERATOR_VALUED_GAMMA_BOUNDARY_PUSHOUT.md`)

- **106.199 (global Hilbert completion / Gamma-compliance kernel):** separates "nuclear jet
  faithfulness" from "Hilbert closure faithfulness" — the finite pushouts have a canonical
  Hilbert direct limit, but the product of translated jets does not by itself define a vector
  in that limit. Produces the first viable nonlocal orbit kernel (positive, faithful, real-
  translation invariant). "The remaining theorem is now the Hilbert-closure identity for the
  complete relative prime–Gamma–polar differential." Also: "a complex-linear symplectic
  pullback from the positive pushout would already imply the complete Rosati sign."
  (`106_199_GLOBAL_HILBERT_COMPLETION_AND_GAMMA_COMPLIANCE_KERNEL.md`)

- **106.203 (complete-return charged Tate boundary):** makes the finite-level algebra of the
  charged return explicit (amplitudes `α_{p,k}`, Gram operator `C_X I`). Bears a **phase-120
  physical-weight warning**, quoted in full because it is decisive for row D:
  > "This source pushout is not the row-(c) attachment required for row (d). It uses
  > `p^{-k/2}` as a boundary *amplitude*, so its quadratic Gram mass is `log(p)/p^k`. In the
  > central Weil form `log(p)/p^{k/2}` is already the quadratic coefficient ... All internal
  > statements below are statements about the phase-106 source object, not a comparison with
  > `B_nuc`." A further covariance correction notes the raw sum in 106.203 identifies
  > different charged generators without an intertwiner; superseded by 106.204.

- **106.204 (covariant charge-mixing boundary):** supplies the missing charge transport via a
  unitary `S_ℓ` making the boundary equivariant under all charges, with numerically verified
  errors 5.1e-16–3.5e-15. Also carries the **same phase-120 warning** ("fails the physical
  {2,3} calibration as an attachment for row (d)"). Its remaining statement (descent
  faithfulness, boxed eq. 28) is called "the remaining force-bearing theorem."

- **106.205 (immediately following, closes the branch negatively):**
  > "performs the required range test and closes this particular Hilbert branch negatively.
  > ... More decisively, the Cauchy module, all charge shifts, the Gamma graph, the covariant
  > mixing, and their isometric cofinal Hilbert completion have purely absolutely continuous
  > normalized-scale spectrum. The CCM cyclic degree one contains nonzero eigenclasses at the
  > known critical zeros. Any equivariant map to the pushout therefore kills those classes, so
  > the charged Hilbert-closure identity 106.200(24) is **false** for this concrete target.
  > ... the next candidate must use a resonant nuclear, reproducing-kernel, or derived cyclic
  > completion in which discrete evaluation jets survive before Hilbert reduction."
  (`README.md:2413-2429`)

- The audit continues to at least 106.210 (cyclotomic-resultant / arithmetic-intersection
  attempt) and ends without a global diagonal:
  > "the standalone classical surface cannot supply the global diagonal; the construction
  > stops rather than borrowing the cardinality diagonal from a different pairing."
  (`README.md`, tail)

**Overall conclusion / what phase 106 says is missing:** across its entire ~210-document arc,
every locally-constructed positive object (Gamma boundary pushout, charge-mixing boundary,
cyclotomic intersection form) is real and non-circular, but **none of them supplies a genuine
global bilinear self-intersection / Hodge-index pairing** on the arithmetic side — exactly the
missing ingredient the task's framing calls unimodularity `Frob_n ⋆ Frob_n^† = Δ^{(n)}`. The
phase-120 annotations retroactively flag the entire 106.203/106.204 branch as calibrated to
the *wrong* physical mass (`log p/p^k` instead of `log p/p^{k/2}`) for row (d), meaning even
its positive partial results are **not directly usable** for the sign problem as currently
scoped — a genuine "possibly wrong/over-generalized" flag on a large fraction of phase 106.
**Partial-success scope:** the operator-valued and charge-covariant boundary constructions
(106.196–106.204) are real, rigorous, positive, faithful Hilbert-space objects — this is a
nontrivial partial success in constructing pieces of a global positive Hilbert realization.
**What blocked it:** (i) 106.205 proves the specific completion attempted has the wrong
spectral type (absolutely continuous, killing the discrete CCM eigenclasses at real zeros);
(ii) even where the local algebra is right, the row-(d) physical calibration was wrong.

---

## 5. Mechanisms killed only by numerics or only by circularity — "might be re-examined as pure mathematics"

- **Phase 61, R10 Lemma 1 (band-edge boundedness)** — self-retracted: the boundedness claim
  was first offered as "RH-neutral, standard analysis," then shown (on attempting a proof, not
  just numerics) to require the same oscillatory zero-sum cancellation as the wall. Not a
  clean numerical kill, but a documented over-claim later walked back — worth flagging as a
  place where the *numerical* verification (bounded up to λ=21) still stands even though the
  claimed unconditional route failed.
- **Phase 76, ambient bordered-inverse norm route (P76.061)** — killed purely by a numerical
  autopsy showing the ambient norm overestimates the true safe error by up to **1e28**; no
  impossibility theorem. *Candidate for re-examination: is there a provable multiplicative
  gap, or was 1e28 an artifact of the specific test vectors?*
- **Phase 77/78, μ_N→0 quasimode attempts** — killed by numerical evidence across specific
  vector families; no impossibility theorem. *A genuinely different quasimode ansatz was never
  tried.*
- **Phase 79, `c_N`/single-signedness IDENT discriminant** — a numerically robust,
  falsifier-passing regime (audited against two independent planted controls, ladder N=8–18)
  rather than a theorem. *Explicit self-correction that "c_N→0" language over-claimed;
  candidate for re-examination as pure mathematics via the named next step (derive `GEOM`
  structurally).*
- **Phase 81, zeros of the bordered secular determinant** — refuted specifically because
  "defining the target shift by inverse transform is circular," not by a hard impossibility
  proof. *Might be re-examined if a genuinely independent (non-transform) definition of the
  even spectral shift is found.*
- **Phase 101, E101.065 (source-adapted exterior identity)** — killed only by circularity
  (shown algebraically identical to the terminal secant). *The corpus treats this as
  informative rather than re-examinable, since it *proves* the identity of two previously
  distinct-looking statements.*
- **Phase 101, E101.077 / E101.093 / E101.096** — three separate mechanisms (full-jet phase
  Gram, normal-adjoint/positive-star construction, Guinand–Weil dictionary bypass), each killed
  *only* by being shown exactly equivalent to RH, not by an independent obstruction. *Flag: each
  remains re-examinable if a genuinely non-circular route to the same Gram-vanishing/divisor
  statement is ever found — none is proposed in the corpus.*
- **Phase 103, the entire direct-A1 route (103_04, 103_06, 103_08)** — the mechanism is
  numerically true with an enormous margin (factor ~n log n) up to n~1200, but the corpus is
  explicit: "Every no-go recorded in phase 102 concerned methods of *estimating* J_n, never the
  truth of (1)." This is the single strongest "numerics say yes, proof absent" case in the
  entire sector — a genuine candidate for renewed pure-mathematical attack.
- **Phase 108, the G2/G4 "circular results"** — self-flagged by the phase itself as a blind
  spot of its own verification discipline: "no numerical check could have caught either,
  because both statements are arithmetically true; the defect is that they are contentless."
  *Explicitly flagged by the authors as worth re-examining, since the same discipline might be
  missing a genuine mechanism elsewhere.*
- **Phase 106, the entire 106.203/106.204 branch** — not killed by numerics (it verified to
  1e-15 precision) nor by an internal contradiction, but by (i) 106.205's proof that the
  completion has the wrong spectral type, and (ii) the phase-120 retroactive finding that the
  Gram mass used was simply the wrong physical normalization for row (d). *A corrected-mass
  version of 106.203/106.204 (using `log p/p^{k/2}`) was never built — a clear, well-specified
  re-examination candidate.*

---

## Counts, partial successes, and top unexplored squares

See the final assistant message for the summary counts and the ranked list of ten unexplored
adjacent squares, as requested by the task.
