# Map 1 — Walls and Master Documents

Corpus-mapping pass over the master/no-go documents of the repository, for row D
("the sign" / `I_∞(F,F) ≤ 0`) triage. Sources read in full: `NO-GO-LIST.md`,
`OPTIONS.md`, `MASTER-PLAN.md`, `COMPLETE-PROGRAM-SUMMARY.md`, `00-MAP.md` (grepped
for additional no-go labels beyond what the other documents already cite — none
found), `03-research/AUDIT_CONSOLIDATED.md`, `03-research/AUDIT_A_CATEGORY_CHANGES.md`,
`05-meta-and-planning/RH-MASTER-CONTEXT/MASTER_CONTEXT.md`,
`05-meta-and-planning/RH-MASTER-CONTEXT/PHASES_AUDIT.md`,
`05-meta-and-planning/RH-MASTER-CONTEXT/NO_GO_AND_RETRACTIONS.md`.
`fragments/*` were grepped for "never attempted / untried" language (no additional
hits beyond what is already listed here from `NO_GO_AND_RETRACTIONS.md` and
`AUDIT_CONSOLIDATED.md §3`).

No judgment is offered here on whether RH is true; only on the documented status of
each attempt.

---

## Table 1 — English-corpus no-gos (`NO-GO-LIST.md`, `OPTIONS.md`, `MASTER-PLAN.md`,
`COMPLETE-PROGRAM-SUMMARY.md`)

| id | mechanism attempted | why it failed | status | could it be wrong? | adjacent unexplored square | source |
|---|---|---|---|---|---|---|
| NG-A1 | Bound cross-sum B(N) ≤ N^ε (ω-class program) ⟹ Lindelöf | Target is *stronger* than Lindelöf; proving it needs Lindelöf as hypothesis | PROVED-IMPOSSIBLE (circularity, not an estimate gap) | No — the logical circularity is elementary | none named | `NO-GO-LIST.md:18-21` |
| NG-A2 | Extrapolate exponent α_B → 0 from 4 data points ⟹ Lindelöf | α_B≈0.42 vs Bourgain threshold <0.31; trend reverses at k=2→3; 4 points insufficient | NUMERICAL-ONLY | Yes — a numerical extrapolation failing is not a proof of impossibility, just insufficient evidence so far | more data points / better statistic | `NO-GO-LIST.md:23-26` |
| NG-A3 | Unconditional cross-covariance between ω-classes as RH signal | Montgomery–Vaughan theorem: unconditional cross-covariance ≈ 0; anti-correlation only visible conditionally at peaks | PROVED-IMPOSSIBLE (MVT) | No | none named | `NO-GO-LIST.md:28-31` |
| NG-A4 | Selberg/Bombieri sieve to separate ω(n) mod 2 | Parity problem: intrinsic sieve-theory obstruction | PROVED-IMPOSSIBLE | No — parity problem is a theorem of sieve theory | none named | `NO-GO-LIST.md:33-36` |
| NG-A5 | Li/Jensen/GORZ/Baez-Duarte coefficients as proof path | All reformulations of RH; numerical verification at finite N is circular | EQUIVALENT-TO-RH | No | none | `NO-GO-LIST.md:38-41` |
| NG-A6 | r4/r5 phase transition N_c≈1.18×10⁵ as RH-relevant | Headline refuted by canonical re-verification; reframed as weaker candid result | ABANDONED (refuted numerically) | Partially — the underlying "ζ more constructive at peaks" is retained as a candid weaker claim | none | `NO-GO-LIST.md:43-46` |
| NG-A7 | TDA (persistent homology H0/H1) as RH detector | H0 δ²-insensitive; L_DH not a topological outlier; H1 signal not significant (p≈0.48) | NUMERICAL-ONLY | Yes — instrument insensitivity, not a proof no TDA variant could work | different persistence statistic / larger sample | `NO-GO-LIST.md:48-51` |
| NG-A8 | λ_min(ζ)≈0.866 as evidence of Weil positivity | Pure PSD artifact — zero-side Gram matrix positive by construction; only the full form (prime+zero) carries information | PROVED-IMPOSSIBLE (tautology) | No | none | `NO-GO-LIST.md:53-56` |
| NG-B1 | 15 classical mechanisms (KV, Selberg density, Levinson–Conrey, Deuring–Heilbronn, Beurling–Nyman, Bohr a.p., Baker, Weil–Deligne, Turán, Littlewood, large sieve, Montgomery pair corr., de Branges chain, Selberg trace, Weil positivity) for lower bounds on b_j | Arithmetic info from Re(s)>1 does not propagate to (1/2,1); each gives upper bounds, wrong region, aggregate not individual, or circular | PROVED-IMPOSSIBLE (per-mechanism, see B2–B8 below) | Mixed — each sub-mechanism individually audited; see below | none named as a class | `NO-GO-LIST.md:62-65` |
| NG-B2 | Korobov–Vinogradov zero-free region ⟹ lower bound on b_j | Gives b_j ≤ 1/2−c/(log γ)^{2/3}, an UPPER bound — wrong direction | PROVED-IMPOSSIBLE | No | none | `NO-GO-LIST.md:67-70` |
| NG-B3 | Deuring–Heilbronn repulsion ⟹ zeros off critical line | D-H operates near Re(s)=1 (Siegel zeros); Paley–Wiener barrier shows arithmetic machinery doesn't reach (1/2,1); no known "anti-Siegel" repulsion | PROVED-IMPOSSIBLE (given current tools) | Yes — "no known anti-Siegel repulsion" is an absence-of-tool claim, not an impossibility proof | construct an anti-Siegel repulsion mechanism (never built) | `NO-GO-LIST.md:72-75` |
| NG-B4 | Beurling–Nyman distance d as lower bound on b_j | d>0 under Hyp. D is circular: bounding d>F(b_j) ⟺ bounding b_j | EQUIVALENT-TO-RH / CIRCULAR | No | none | `NO-GO-LIST.md:77-80` |
| NG-B5 | de Bruijn–Newman Λ≥b_j²/2 ⟹ lower bound on b_j | Inequality direction inverted: gives b_j≤√(2Λ), an upper bound; only known bound Λ≤1/4 gives trivial b_j≤√(1/2) | PROVED-IMPOSSIBLE (wrong direction) | No | none | `NO-GO-LIST.md:82-85` |
| NG-B6 | Turán inequalities for ξ₀ (Hyp. D factorization) as constraint on b_j | Circular — the inequalities are a *consequence* of ξ₀∈LP, i.e. of Hyp. D itself; impose no constraint | EQUIVALENT-TO-RH / CIRCULAR | No | none | `NO-GO-LIST.md:87-90` |
| NG-B7 | Baker's theorem (linear forms in logs) to constrain zeros | Baker needs algebraic numbers; γ_j presumed transcendental with no known algebraic structure — wrong category | PROVED-IMPOSSIBLE (category mismatch) | Yes, in principle if γ_j turned out algebraic-adjacent — but no evidence for this | none | `NO-GO-LIST.md:92-95` |
| NG-B8 | Montgomery pair correlation as b_j detector | Pair correlation describes on-line spacings only; off-line zeros invisible to it | PROVED-IMPOSSIBLE (no signal) | No | none | `NO-GO-LIST.md:97-100` |
| NG-C1 | Factor Weil form Q=Q_∞×∏_p Q_p (Hasse–Minkowski) | Wall A: Q_zero doesn't factor over primes (zeros are global, no Frobenius-at-p for ζ/Q); Wall B: no Hasse–Minkowski for ∞-dim Hermitian forms | PROVED-IMPOSSIBLE (two independent obstructions) | Wall A plausible-solid; Wall B is "no known theorem," not disproof — genuinely worth checking against condensed-math or other infinite-dim HM analogues | infinite-dimensional Hasse–Minkowski analogue (none built) | `NO-GO-LIST.md:106-111` |
| NG-C2 | Adelic/Grössencharacter methods (Phase 27) as alternative to Phase 26's V.2 | Theorem 27-B.4: same obstacle in two languages, not an alternative route | PROVED-IMPOSSIBLE (identity of obstacles) | No | none | `NO-GO-LIST.md:113-116` |
| NG-C3 | Explicit eigenvectors f_j(x)=x^{b_j+iγ_j} in L²(C_Q) | Not in L² — norm diverges; eigenvectors are distributions | PROVED-IMPOSSIBLE (elementary computation) | No | rigged Hilbert space / distributional spectral theory (not pursued in this doc) | `NO-GO-LIST.md:120-123` |
| NG-D1 | b_j=0 as global MINIMUM of energy E_arith (Front D, Phase 28) | Theorem 2 (06-curvature-xi.md): under RH, log|ξ| strictly CONVEX at σ=1/2 ⟹ Q locally MAXIMIZED at b_j=0, not minimized | PROVED-IMPOSSIBLE (wrong extremum) | No | t-concavity direction (see D2) | `NO-GO-LIST.md:129-132` |
| NG-D2 | log-concavity of σ↦log|ξ(σ+iγ)| as sufficient condition for RH | Answer is NO under RH: curvature C(γ)=Σ1/(γ-γ_ρ)²>0, i.e. convex not concave | PROVED-IMPOSSIBLE | No | t-concavity (stated as "the right direction," not itself pursued to conclusion) | `NO-GO-LIST.md:134-137` |
| NG-D3 | G_ζ(t)>−G_ana(t) unconditionally (Euler product + functional equation only) | Prop 1 (doc 08): equivalent to RH; Euler product only converges absolutely for Re(s)>1 | EQUIVALENT-TO-RH | No | none | `NO-GO-LIST.md:139-142` |
| NG-D4 | Fourier involution K anticommuting with T₀ ⟹ η(T₀)=0 ⟹ κ=0 (Front B) | Functional-equation involution J *commutes* with T₀ (preserves eigenvalues), not anticommutes; the needed anticommutation condition is open | ABANDONED (open, not proved impossible) | Yes — explicitly labeled open/unresolved, not refuted | resolve Q(f,g)+Q(f̂,ĝ)=0 directly (open) | `NO-GO-LIST.md:144-147` |
| NG-E1 | Reflection positivity per place (OS moonshot, Phase 6) | Computed: local integral form G_p(0)>0, G_p(π/log p)<0 for p=2,3,5,7 — indefinite | PROVED-IMPOSSIBLE (computed refutation) | No | positivity as cross-place (not per-place) phenomenon — acknowledged, not built | `NO-GO-LIST.md:153-156` |
| NG-E2 | Scalar λ_min(Q) as principal non-tautological invariant | Quasi-tautological (=0 under RH by Thm C of P8); real invariant is per-prime anatomy {R_p} | ABANDONED (retired, not refuted) | N/A — retirement of an emphasis, not a claim of impossibility | per-prime anatomy invariant (adopted instead) | `NO-GO-LIST.md:158-161` |
| NG-E3 | Global Cauchy–Schwarz bound for E_g via ‖D_T‖ ~ T log T | Vacuous — loses localization entirely | PROVED-IMPOSSIBLE (bound too coarse) | No, but a sharper localized C-S variant is not excluded | localized/weighted Cauchy-Schwarz (not tried) | `NO-GO-LIST.md:163-166` |
| NG-E4 | Point-to-point routes (Schur/Gram/Jaffard/interpolation) for relative bounded form | All pay price P=ρℓ→∞; oversampling forced | PROVED-IMPOSSIBLE | No | none | `NO-GO-LIST.md:168-171` |
| NG-E5 | Hilbert–Pólya via OS reconstruction "for free" | RETRACTED — two-point function oscillatory not OS-decreasing; OS theorem needs exponential decay | PROVED-IMPOSSIBLE (retraction of earlier claim) | No | none | `NO-GO-LIST.md:173-176` |
| NG-E6 | Reduction "envelope ≥ pointwise comb" ⟹ RH (S2f) | Comb is distributional (Ω_∞−2πΣδ); pointwise comparison ill-defined as φ̂→δ | PROVED-IMPOSSIBLE (ill-posed limit) | No | none | `NO-GO-LIST.md:178-181` |
| NG-E7 | L_DH as reproducible quantitative benchmark | von Mangoldt function of L_DH not reproducible from public definitions; v7 value not recoverable | ABANDONED (downgraded to qualitative control) | N/A | none | `NO-GO-LIST.md:183-186` |
| MW-1 | Weil positivity: W(f⋆f̃)≥0 | EQUIVALENT to RH (Weil 1952) | EQUIVALENT-TO-RH | No — this is Weil's theorem | — | `NO-GO-LIST.md:197-200`; reconfirmed independently twice, Phases 113/118 |
| MW-2 | Arithmetic-propagation wall: Euler product info (Re s>1) doesn't reach (1/2,1); zeros global, no prime "owns" a zero | Blocks all local-to-global arguments | PROVED-IMPOSSIBLE as stated for the mechanisms tried (identified from ≥5 independent directions: Phase 25 W4-RSRP, Phase 27 Wall A, Phase 28 conditional convergence) | Partially — it's an empirical/structural pattern across many mechanisms, not itself a single closed theorem; a genuinely new arithmetic input could in principle cross it (this is exactly what rows a–d of paper 42 and CAND-1 attempt) | any construction supplying non-Euler-product arithmetic data at (1/2,1) | `NO-GO-LIST.md:202-207` |
| MW-3 | Hasse–Minkowski in infinite dimension | No HM theorem for ∞-dim Hermitian forms; local positivity ⇏ global | ABANDONED / genuinely a gap (no theorem either way in this generality) | Yes — absence of a known theorem, not a disproof; condensed math (OPTIONS §1b) proposed as a possible escape, untried | condensed-mathematics HM analogue (untried, OPTIONS.md §1b) | `NO-GO-LIST.md:209-212` |
| MW-4 | Hilbert–Pólya wall (wrong sign): unconditional tools give lower bounds on positivity; RH needs upper bound | Confirmed in 8 independent paradigms (explicit-formula/Kreĭn, per-place, Carleson, pair correlation, Connes prolate, heat flow, cohomological Hodge, hyperbolicity) | PROVED-IMPOSSIBLE for all 8 named paradigms | No, for those 8; a 9th untested paradigm could differ, but pattern is strong | — | `NO-GO-LIST.md:214-219` |
| MW-5 | Connes–Consani arithmetic-site wall: Q=Q_∞+ΣQ_p needs H¹(Spec Z,F), Frobenius φ_p, positive intersection form | Unfinished after decades; sharpened by Phase 113 (O1-O3, impossible inside D) and Phase 118 (analytic route, same wall) | mostly PROVED-IMPOSSIBLE-inside-a-class (D = Schwartz-data, per Phase 113) but genuinely UNBUILT (not proved impossible) as an object in general | Yes for the general existence question (R16, OPTIONS.md §1d) — CC's own scaling-site Riemann–Roch is real-valued not integral, answering R16 negatively only for *that* object; wider literature not scanned | condensed math (dissolve O1), Quillen K-theory of Spec Z, R16 literature scan — all named untried in OPTIONS.md | `NO-GO-LIST.md:221-232`; `OPTIONS.md §1b,1c,1d` |
| MW-6 | Uniform spectral-gap wall: sup_X|λ_min(Q_X)−λ_min(Q_∞)|≤ε(X_0)→0 | Equivalent to RH (Connes/Bombieri/Lagarias positivity) | EQUIVALENT-TO-RH | No | — | `NO-GO-LIST.md:234-238` |
| MW-7 (Hadamard barrier, CCM) | No zero-position-free property of ζ implies dν=0 | Named barrier explaining why the 3 CCM routes (T_λ=0, Jensen δ=0, KL=0, etc.) don't close | PROVED-IMPOSSIBLE as a barrier statement (they're reformulations of RH) | No | — | `COMPLETE-PROGRAM-SUMMARY.md:108-110,139-146` |
| CIR-1 | Selberg density as bound on b_j | Bounds count of off-line zeros in aggregate, not individual b_j | PROVED-IMPOSSIBLE (structural, not per-mechanism numeric) | No | — | `NO-GO-LIST.md:244` |
| CIR-2 | Levinson–Conrey on-line proportions as bound on b_j | 41% on-line says nothing about off-line shift | PROVED-IMPOSSIBLE | No | — | `NO-GO-LIST.md:246` |
| CIR-3 | Beurling–Nyman distance as lower bound on b_j | Circular under Hyp. D | EQUIVALENT-TO-RH | No | — | `NO-GO-LIST.md:248` |
| CIR-4 | Turán inequalities for ξ₀ as constraint | Consequence of Hyp. D, not independent constraint | EQUIVALENT-TO-RH | No | — | `NO-GO-LIST.md:250` |
| CIR-5 | ψ(x)−x=O(x^{1/2+ε₀}) with ε₀<min b_j as lower bound | Equivalent to zero-localization control — circular | EQUIVALENT-TO-RH | No | — | `NO-GO-LIST.md:252` |
| CIR-6 | Li/Jensen/GORZ/Baez-Duarte numeric "verification" as progress | All equivalent to RH; finite verification proves nothing asymptotic | EQUIVALENT-TO-RH | No | — | `NO-GO-LIST.md:254` |
| CIR-7 | Compatibility theorem (KV vs structure-function bounds, Phase 23/24) | Only confirms consistency with any b_j∈(0,1/2); no constraint | PROVED-IMPOSSIBLE (vacuous) | No | — | `NO-GO-LIST.md:256` |
| CIR-8 | F3 chaos incompatibility ("depth=O(log log γ_j)") | Claim was INCORRECT; KV bounds give no upper bound on |log b_j| | ABANDONED (refuted claim) | No — it's a corrected error | — | `NO-GO-LIST.md:258` |
| NG-F1 | Multiplicativity discriminant (Phase 60): thesis "multiplicativity, not zero location, controls the Weil sign" | Refuted numerically both sides: zero side circular (E1); arithmetic side (E2/E2b) shows Carleson constant does NOT separate ζ (1.98) from smooth non-multiplicative controls (flat 2.44, loglin 2.11, logn 2.21) — apparent separation was a smoothness artifact | NUMERICAL-ONLY, but with reproducible code and controls (borderline PROVED-IMPOSSIBLE for the tested class of Carleson-constant discriminants) | Yes in principle — only the *tested* discriminant/instrument family is excluded, not all multiplicativity-based discriminants; a relative-discriminant instrument is explicitly retained as reusable | fixed-A relative discriminant instrument (retained, reusable per doc) | `NO-GO-LIST.md:323-330` |
| NG-F0 | "Phase-60-duality" H1 (minimizer uniqueness) via 3 axes | WITHDRAWN — audit found cited engine did not exist on disk, script did `return None`, tables not reproducible, "H1 CLOSED" proof had false step A>0,B≥0⟹A−B convex | ABANDONED (retracted for non-reproducibility, not disproved on the merits) | Yes — the only valid salvage is the reduction H1⟺‖A^{-1/2}BA^{-1/2}‖<1, itself unresolved | re-attempt H1 with real reproducible code | `NO-GO-LIST.md:332-335` |
| NG-62 | Cesàro-in-λ averaging of `b_bulk(λ)` to relieve boundedness wall | Off-line contributes secular growth λ^{2β−1} (not oscillatory) that no Cesàro average removes; zero-density estimates bound counts/imaginary parts, not real parts | EQUIVALENT-TO-RH (relocates MW-2, doesn't cross it) — confirmed numerically (ζ flat ≈0.13; DH falsifier grows exponent≈0.43) | No | — | `NO-GO-LIST.md:346-360` |
| NG-62b | Quaternionic Hodge–Riemann polarization (Deninger J²=−1) on finite Weil window | Present (A⪰0 on V₊ for ζ, indefinite for DH/random) but GAPLESS: V₊ spectrum decays e^{−cL}→0 exponentially; ζ pinned exactly at marginal μ_max=1 | EQUIVALENT-TO-RH (marginal/gapless detector, not a proof route) | No — three independent reformulations (Cesàro, HR, Euler μ≤1) all confirm the same gaplessness | give the margin a uniform gap = needs MW-5's cohomological realization (unbuilt) | `NO-GO-LIST.md:362-375` |
| NG-63 | J-linear gapped Frobenius realization on ζ window (function-field mimicry) | Real elliptic curves/F_q have both isometry+gap (R3/E98 verified to machine precision); ζ window's scaling operator anti-commutes with J (‖[D_log,J]‖/‖D_log‖=2.000 exact) AND polarization gapless (NG-62b) | PROVED-IMPOSSIBLE for this specific construction (direct F_q-vs-Z contrast, exact computation) | No, for the tested construction; whether *some other* Frobenius-type object could be J-linear and gapped is the open MW-5 question | construct the actual Connes–Consani/Deninger arithmetic-site Frobenius (unbuilt, theory not computation) | `NO-GO-LIST.md:377-391` |
| NG-67 | Prime current as compact-quantum-group (CQG) coefficient, forcing Ω_7 via Haar/Peter-Weyl contractivity | E67.4: strict free-product Haar orthogonality destroys exactly the needed arithmetic interference between prime factors (Woronowicz/free-product no-go) | PROVED-IMPOSSIBLE for this route | No | q-Gamma/Plancherel archimedean sector (retained, reusable, zeta-free) | `NO-GO-LIST.md:393-402` |
| NG-68 | GLT/Toeplitz symbol positivity κ(x,θ)≥0 for terminal defect A_N−P_λ | Position-resolved symbol fails GLT distribution law numerically (measure{κ<0}~0.4 while true index ind_-=0) — gauge-fragile, faithful at some t0 wrong at others | PROVED-IMPOSSIBLE (numerically demonstrated failure of the GLT structure itself) | No — superseded by exact gauge-robust index (Phase 69) | — | `NO-GO-LIST.md:404-413` |
| NG-69 | Prove ind_-(A_N−P_λ)=0 uniformly in gauge, by structure alone | Detector solid and gauge-robust, but no structural proof found; difficulty localizes to one frequency θ~π/2 | ABANDONED (partial — detector survives, forcing mechanism absent) | Yes — explicitly still open, not refuted | resolve the θ~π/2 local obstruction (open) | `NO-GO-LIST.md:415-420` |
| NG-66 | Rank-one escape orthogonality for CAND-1 canonical Gram kernels (P_prim K_P P_prim bounded ⟺ RH) | Orthogonality claim not established; first numerical proxy (E110, crude "drop top eigenvalue" not the true projection) gave noisy wrong-sign exponents, withdrawn as a measurement not a refutation of D1 | ABANDONED / genuinely open (proxy failure only, not a proof) | Yes — explicitly the proxy was wrong, not the underlying claim | build the true P_prim projection numerically (not yet done properly) | `NO-GO-LIST.md:422-430` |
| NG-107 | Deninger–Morishita bridge to attach row (b) shell functionals Γ_{p,k} to algebraic cycles | Residue field at p is F_p-bar with μ_(p) of order prime to p — kills exactly the transverse direction row (b) needs (Thm 4.1) | PROVED-IMPOSSIBLE (for this bridge) | Yes — OPTIONS.md §1a notes a *different*, newer Deninger construction (2508.05329, rational Witt vectors) may not be caught by this specific obstruction; needs checking | check G-4 (rational Witt vectors) against this obstruction — not yet done | `NO-GO-LIST.md:467-472`; `OPTIONS.md §1a` |
| NG-109 | Any pairing to promote Λ(n)=deg_det L_n to genuine intersection number | Proved impossible for EVERY kernel (Thm 1.1) — general obstruction, not a failed search | PROVED-IMPOSSIBLE (universally quantified over kernels) | No — it's a proved universal theorem | — | `NO-GO-LIST.md:474-478` |
| NG-110 | ξ-divisibility (f-hat=ξ·g-hat) on compactly supported test functions for row (d)'s principal subspace | Stirling: ξ has infinite exponential type; compact support ⟹ finite type; forces g-hat=0. Explicitly NOT RH in disguise — obstruction carried entirely by Γ | PROVED-IMPOSSIBLE (elementary growth argument) | No | Schwartz-class (non-compact) extension (attempted next in Phase 111-113) | `NO-GO-LIST.md:480-487` |
| NG-113-O1 | Supply requirement d3 (quadratic growth) inside D=Schwartz-data | D/rad is a plain C-vector space ⟹ effective cone scaling-stable ⟹ h⁰(nD)=h⁰(D), measured exactly at n=2,5,100 — nothing to grow | PROVED-IMPOSSIBLE inside D | Yes — only excludes D as currently defined; condensed mathematics proposed (untried) as a category where Z is genuinely discrete inside a category holding R, "the most direct candidate for dissolving O1" | condensed math against O1 (OPTIONS.md §1b, untried anywhere in corpus) | `NO-GO-LIST.md:489-498`; `OPTIONS.md §1b` |
| NG-113-O2 | (same) via correspondences δ_n | Infinite mutual intersection: |(n/m)^ρ|=(n/m)^{1/2} does not →0; exponent 1/2 *is* the critical line, encoded directly | PROVED-IMPOSSIBLE inside D | No — moving category (condensed math) is not excluded by O1's proof but O2/O3 need independent checking, per OPTIONS §1b's own risk note | check whether condensed math also evades O2/O3 (not done) | `NO-GO-LIST.md:496-497` |
| NG-113-O3 | (same) negative-part spectral gap | sup s(f,f)/‖f‖² = 0 on D-circ∖rad, not attained | PROVED-IMPOSSIBLE inside D | same caveat as O1/O2 | same | `NO-GO-LIST.md:498-500` |
| NG-113-d3 | Repair O1 by finding any section functor h⁰ on D compatible with existing divisor structure | Divisors and sections proved doubly dissociated (mutually independent, explicit two-sided witness, Thm 3.1/3.3); imported CC Riemann–Roch separately insufficient (dim 1, genus 0, Pontryagin duality between different spaces, no signature) | PROVED-IMPOSSIBLE (inside D, and for the specific CC import) | Partial — "no h⁰ inside D" is proved; whether some h⁰ exists in a different ambient category (the actual target of this whole task) is open, not addressed here | THIS IS THE TARGET SQUARE — construct h⁰ satisfying (a) nonneg, (b′) positivity⟹effective mod radical, (c) Riemann–Roch with I_∞(E,E) term, outside D | `NO-GO-LIST.md:504-511` |
| MW-1 (reconfirmed) | Row (d) = RH, twice independently | Phase 113 algebraic: (E°) equivalent to RH both directions, Hodge-index inequality on H^perp holds iff RH (signature (1,7) on-line, (3,5) off, measured). Phase 118 analytic: ⟨A_TF,F⟩=Σh(γ_ρ) verified to 5e-11–2e-9 against real zeros; m_0 forced (ψ(1/4) check to 30 digits) | EQUIVALENT-TO-RH (doubly reconfirmed, independent methods) | No — this is the closest thing to a load-bearing theorem in the corpus for row D | — | `NO-GO-LIST.md:513-529` |
| NG-116 | Complete row (d) conditionally on Logarithmic Schur Angle Conjecture ρ_N≤1/(20 log N) | Falsified against paper 42's own audit table at 4 of 5 tabulated points (N=20,40,80,120); companion claim ρ_N log N<0.047 also fails (reaches 0.0565) | PROVED-IMPOSSIBLE (falsified, not merely unproved) | No — directly contradicted by the paper's own numbers | — | `NO-GO-LIST.md:531-536` |
| NG-117 | Gamma–Tate source model (‖L_N e‖²≤E_{ΓT,N}(e)) to imply exact threshold via constant c_N | c_N<1 at every threshold 3≤N≤37, decaying like (log N)^{-0.6}, decreasing under mesh refinement; c_N is a minimum so Galerkin bounds it from above (one-sided-robust — not a discretization artifact) | PROVED-IMPOSSIBLE for this route, robustly (no amount of sharpening the source estimate can close row (d)) | No — the one-sided-robustness argument is explicit and sound as stated | — | `NO-GO-LIST.md:538-547` |
| NG-118 | Explicit structural formula for scattering operator Y_T=ΦX_T (Douglas' lemma reformulation of row d) | Toeplitz-in-log n and Hankel-in-log n both refuted (R²≤0.16); block-diagonal-over-places excluded elementarily; no Ψ found with I−Φ*Φ=Ψ*Ψ matching any candidate | PROVED-IMPOSSIBLE for the specific structural forms tried (candid negative, not a near-miss) | Yes in principle — only the named structural ansätze (Toeplitz, Hankel, block-diagonal) are excluded; an unnamed structure is not | find a different structural form for Φ (space not enumerated) | `NO-GO-LIST.md:549-556` |

---

## Table 2 — Options document (`OPTIONS.md`): the non-RH-equivalent open sub-targets

These are explicitly **not** shown equivalent to RH, and none is proved impossible —
listed here because row D's "adjacent unexplored squares" partly overlap them.

| id | statement | file | why strictly weaker than RH | status |
|---|---|---|---|---|
| Diana L8 | any unconditional bound m≤C on off-critical-line zero quadruples | `phase-37-physics/111` | bounds without killing the off-line quadruples | OPEN, "INALCANZABLE" with catalogued techniques (every known zero-density mechanism is *binary*: 0 or T^θ, never a finite nonzero count) — **not proved impossible** |
| "Lemma 108" | κ_W(Q_2)≤C·n_W for any absolute C | `phase-36-ABC-forms/108 §8.1` | explicitly not RH-equivalent (allows m>0 up to C/2) | OPEN, tied to conjectural pair-correlation lower-order terms |
| Conjecture C_B | finitely many off-line zeros ⟹ none | `phase-34-new-directions/94 §11` | second half of the RH=(m<∞)∧(...) decomposition | OPEN, no known bridge finitude→nullity |
| C5 ⟹ κ<∞ | tail bound already achievable for large X | `phase-34/91,94` | only the deduction step (Krein–Langer) is missing | OPEN |
| LP-112 | sequential self-approximation of zeta on a fixed compact disc | `phase-37-physics/112,113` | would give m∈{0,∞} | OPEN, "SIN PRECEDENTE" — exhaustive literature check found nothing like it for any L-function; non-equivalence to RH is *asserted, not proved*, and downgraded by a later audit (`phase-38/115`) |
| GAP-157.A | discrepancy/irrationality-measure bound on Kronecker flow τ↦(p^{iτ})_p | `phase-49/157,158,159` | diophantine input strictly weaker than full recurrence | OPEN, 2 of 3 routes killed, core implication undecided |
| Boundary triples for W_λ | classify self-adjoint extensions at endpoints | `phase-60/RH-PROOF-PAPER.md §4.B` | classification question, RH-neutral either way | **OPEN, self-labelled "RH-neutral, doable now," never attempted** |

**Options explicitly named as untried category-change escapes for MW-5 / row (d):**

- **G-4** (`OPTIONS.md §1a`): Deninger's rational Witt vectors (arXiv 2508.05329, Thm 5.1
  `W_rat(O(X))≅Corr(X,A)`) — best row-(a) candidate in the ledger, "BUILT-MODULO-GAP,"
  missing norm and pairing. Risk flagged: may already be closed by NG-107's residue-field
  obstruction, or may survive because it's a different/newer construction — **not checked**.
- **Condensed mathematics vs O1** (`OPTIONS.md §1b`): "does not appear anywhere in the
  corpus's 118 phases." Most direct candidate for dissolving O1 (D as plain C-vector
  space); O2/O3 not guaranteed to be evaded, "would need independent checking."
- **Quillen K-theory of Spec Z** (`OPTIONS.md §1c`): "Untried." No corpus connection
  between K_*(Z)/higher regulators and the inertia invariant m.
- **R16** (`OPTIONS.md §1d`): does a quadratic Riemann–Roch exist over Spec Z *at all*?
  CC's own scaling-site Riemann–Roch answers this negatively only for that object
  (χ(D)=deg(D) real-valued, not even integral); "no scan of the wider arithmetic-geometry
  literature ... has been done from inside this corpus."

---

## Table 3 — Spanish-corpus no-gos (`NO_GO_AND_RETRACTIONS.md`) and `AUDIT_A_CATEGORY_CHANGES.md`

The Spanish master registry (`05-meta-and-planning/RH-MASTER-CONTEXT/NO_GO_AND_RETRACTIONS.md`)
uses a different labeling convention (route families rather than numbered IDs) and a
four-way verdict taxonomy: REFUTACIÓN (refutation/counterexample), INSUFICIENCIA
(insufficient — a genuine off-line zero survives it), CIRCULARIDAD (already contains
RH-strength hypothesis), DUPLICACIÓN (relabels the same residual), CONDICIONALIDAD
(valid only if an unbuilt object existed). Mapped onto this task's status column:
REFUTACIÓN→PROVED-IMPOSSIBLE, INSUFICIENCIA→ABANDONED (numerics/heuristics show it
doesn't reach far enough, no proof of impossibility), CIRCULARIDAD/DUPLICACIÓN→
EQUIVALENT-TO-RH, CONDICIONALIDAD→ABANDONED (unbuilt object required).

| id (assigned) | mechanism attempted | why it failed | status | could it be wrong? | source |
|---|---|---|---|---|---|
| ES-1 | Multiplicativity / ω-classes as zero criterion | Liouville and random multiplicative controls break the inference | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:26` |
| ES-2 | Coherence/tails/GEV classifiers as proof chain | Parameters depend on generator/selection/scale; finite classifier can't quantify over unknown zeros | PROVED-IMPOSSIBLE (as a proof chain) | No | `NO_GO_AND_RETRACTIONS.md:27` |
| ES-3 | Peak matrices as spectral inversion | Respond mainly to coefficients/conductor/support/ablations, not to zero injection | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:28` |
| ES-4 | Gram matrix built only from zeros as horizontality detector | PSD by construction — tautological; may have discarded the very coordinate needed | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:29` |
| ES-5 | TDA / point-cloud geometry | A finite distance / truncated cloud doesn't exclude a future zero or control the full divisor | ABANDONED (insufficient, not disproved) | Yes — insufficiency of *this* instrument, not proof no geometric instrument works | `NO_GO_AND_RETRACTIONS.md:30` |
| ES-6 | Finite positivity of Li, Mercer, or Weil forms | A finite stretch doesn't control all indices/tests; full quantification is RH-strength | EQUIVALENT-TO-RH (in the limit) | No | `NO_GO_AND_RETRACTIONS.md:31` |
| ES-7 | Weil form vs truncated residual | Residual between two cutoffs does not inherit positivity of the complete form | PROVED-IMPOSSIBLE (confusion, corrected) | No | `NO_GO_AND_RETRACTIONS.md:32` |
| ES-8 | Pointwise bounds on \|ψ(x)−x\| in absolute value | Loses phase against Laguerre kernel; measured order deficit; doesn't rule out every signed inequality | ABANDONED (insufficient in the tried route) | Yes — only the absolute-value route is closed, a signed route "remains admissible" per the doc's own closing note (though itself RH-strength to close) | `NO_GO_AND_RETRACTIONS.md:33,153` |
| ES-9 | Term-by-term positivity of Λ(n) | Whitening amplifies individual norms and destroys the interprime interference carrying the sign | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:34` |
| ES-10 | Positive prime truncation | Finite sections can be negative while the full observed form is positive — no "positive part minus small tail" | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:35` |
| ES-11 | Zero-free regions / zero density for all n | Admit at least one off-line zero, which alone can force negative Li coefficients at large n | ABANDONED (insufficient for all n) | No | `NO_GO_AND_RETRACTIONS.md:36` |
| ES-12 | Almost-periodic recurrence of all phases | Cost of matching the full vector exceeds available detection gain — not a universal no-go for every scalar function | ABANDONED | Yes — explicitly "not universal no-go for every scalar function" | `NO_GO_AND_RETRACTIONS.md:37` |
| ES-13 | Fejér–Riesz | Circular — requires nonnegativity of the boundary symbol, which is the sought positivity | EQUIVALENT-TO-RH / CIRCULAR | No | `NO_GO_AND_RETRACTIONS.md:38` |
| ES-14 | Kreĭn abstract positive extensions | Existence of *some* positive extension doesn't identify the arithmetic kernel as that extension | ABANDONED (insufficient) | Yes | `NO_GO_AND_RETRACTIONS.md:39` |
| ES-15 | Heat flow / de Bruijn–Newman without arithmetic input | Characterizes the real regime but doesn't determine the terminal parameter; further cascade bounds open | ABANDONED (insufficient without input) | Yes | `NO_GO_AND_RETRACTIONS.md:40` |
| ES-16 | de Branges / Hermite–Biehler | Circular or incompatible in the tried conditions; useful conditions imply real-rootedness | EQUIVALENT-TO-RH / CIRCULAR | No, for the versions tried | `NO_GO_AND_RETRACTIONS.md:41` |
| ES-17 | Real-zero approximants converging to Ξ | If they converge locally to Ξ, Hurwitz transmits reality — building that convergence IS the work | EQUIVALENT-TO-RH | No | `NO_GO_AND_RETRACTIONS.md:42` |
| ES-18 | Finite Pontryagin index | Depends on finiteness of the defect; doesn't exclude infinitely many off-line orbits | ABANDONED (conditional/insufficient) | Yes | `NO_GO_AND_RETRACTIONS.md:43` |
| ES-19 | GLT symbol, index, passivity | In the full limit these return to global positivity or an equivalent Herglotz condition | EQUIVALENT-TO-RH (duplication) | No | `NO_GO_AND_RETRACTIONS.md:44` |
| ES-20 | Hodge, Lefschetz, absolute surface | A real geometry could be decisive, but corpus builds no object/diagonal/cohomology/Frobenius/polarization | ABANDONED (conditional, unbuilt) | Yes — this is precisely the "adjacent unexplored" direction | `NO_GO_AND_RETRACTIONS.md:45` |
| ES-21 | Castelnuovo/Minkowski transplant | Condition X3 for positive norm applied to a negative-norm class | PROVED-IMPOSSIBLE (as written) | No, as written | `NO_GO_AND_RETRACTIONS.md:46` |
| ES-22 | Prolate, gap, quasimode | A gap doesn't identify the ground state or exclude negative index without an extra bound that reduces to Weil | ABANDONED (insufficient) | Yes | `NO_GO_AND_RETRACTIONS.md:47` |
| ES-23 | Pseudoinverse on singular curve | Must use polynomial adjugates/cofactors; dividing at the singular point loses the object | PROVED-IMPOSSIBLE (as attempted) | No | `NO_GO_AND_RETRACTIONS.md:48` |
| ES-24 | Cell-by-cell matching | Cancellation is coupled; separating summands destroys the signed identity | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:49` |
| ES-25 | Single-level holomorphic moments to recover divisor | Distinct signed representations share the same finite moments; missing transversal support and linear multiplicity | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:50` |
| ES-26 | Trace products to recover conjugation | Create all pairs and quadratic weight in multiplicities; later restriction doesn't reconstruct conjugate graph | PROVED-IMPOSSIBLE | No | `NO_GO_AND_RETRACTIONS.md:51` |
| ES-27 | Real-divisor convergence sensitive to support | Preserving real support up to Ξ already excludes off-line zeros — not neutral topological infrastructure | EQUIVALENT-TO-RH | No | `NO_GO_AND_RETRACTIONS.md:52` |

**Retirals/corrections** (`NO_GO_AND_RETRACTIONS.md:117-137`, table "Afirmación anterior /
Estado vinculante"): multiplicativity suppresses dangerous resonance (RETIRED); inter-class
covariances predominantly negative (RETIRED); ω=2 singular cause (RETIRED); off-line zero
automatically produces growth law in truncation (RETIRED as lemma); zero-only Gram detects
horizontality by negativity (REFUTED, tautological PSD); H0 has universal linear/quadratic
law (RETIRED); `det Y≡1` closes Hermite–Biehler convergence (RETIRED, non sequitur); Phase 65
QED label (SUPERSEDED — D8.5 left open by later corrections); H2 covers bounded heights by
compactness+positive diagonal (REFUTED — doesn't prove PSD); H6 gives quantitative negative
witness per cluster (DOWNGRADED — pending tail domination, inconsistent |κ| factor); Ω_4 uses
single global whitening (CORRECTED — different domains); Ω_5 proves boundary positivity for N
(CORRECTED — only proves continuity); **Ω_7 equivalent to |λ_n^prime|<λ_n^arch for all n**
(REFUTED — exact target is λ_n^prime≥−λ_n^arch; the absolute-value bound is only a sufficient
strategy when the archimedean part is positive, and already fails as an equivalence at n=1:
λ_1^arch≈−0.554, λ_1^prime=γ≈0.577, λ_1≈0.023>0); prime integration by parts sign error
(REFUTED — correct form is −n+∫(ψ−y)f′ dy, prior formula flipped sign, omitted lower boundary
term); envelope asymptotic can omit linear term (REFUTED — contains (γ−1)/2·n, not
O(√n log n)); Σ_ρ(1−1/ρ)^n can be isolated (REFUTED — diverges even under RH); adjugate
characteristic term vanishes (REFUTED — it's the chain rule, must be recombined); raw mass,
antisymmetrized border and core mass interchangeable (REFUTED — differ by explicit exterior
factor and phase defect); single holomorphic level recovers divisor (REFUTED — signed
representations and loss of linear multiplicity).

**`AUDIT_A_CATEGORY_CHANGES.md`** — category-change escapes tried against O1/O2/O3
(`03-research/AUDIT_A_CATEGORY_CHANGES.md §1`, table rows 1–12, condensed):

| doc | category proposed | verdict |
|---|---|---|
| 131 (Hodge-Witt) | Real Witt group W(R)≅Z as codomain for inertia defect | STALL — foundational only, no construction of the actual pre-RH polarization attempted |
| 132 (𝒫ol_δ) | Category of Hermitian spaces with marked primitive subspace, defect δ=neg.ind | THEOREM: δ is provably not a character (Prop A.4) — the one route that could see δ (Thm C) reduces to LP-112 in disguise |
| 160 (functor construction) | Crossed product 𝒜=C(T)⋊_φR of Kronecker flow, transport functors phase→inertia | THEOREM (Prop 160.10): the polarization metric, not the transport, carries ζ — flat/dynamics-only metric is RH-free but signature-0 (blind) |
| 161 (KK canonical metric) | KK-theoretic fundamental class [Δ], noncommutative Poincaré duality | THEOREM (Teorema 161.9, cleanest full no-go): canonical orientation is a Tomita–Takesaki modular weight whose partition function is literally ζ(β) (Bost–Connes) |
| 162 (homotopy inertia) | L-theory cofiber spectrum, Adams e-invariant e_ζ∈Q/Z (metric-free) | THEOREM (162.7c): metric genuinely evaded, but the carrier spectrum's fundamental class still re-encodes ζ, one node deeper |
| 163 (destructor) | Adversarial re-check of 162 | THREE THEOREMS: (i) "metric-free" filler silently reimports Q via the Lagrangian; (ii) **genuine non-ζ counterexample**: 2m even integer maps to 0 in Q/Z identically, by pure group theory, before ζ ever enters; (iii) any primes-built carrier has spectrum {log k}, partition ζ |
| 156 (Maslov/index) | Spectral flow / Maslov index / Toeplitz winding on H_J | THEOREM, two-layered: Toeplitz operator fails to be Fredholm at all once m=∞ (existence itself is RH-adjacent); granted Fredholmicity, winding number = zero count |
| 65 (Krein–Langer/de Branges) | Index-graded determinant category, κ as functor | STALL by the phase's own D12 audit — reduces to one named input D8.5; **later docs in the same phase claim closure, uncorroborated by the rest of the corpus and explicitly flagged as disputed, not verified** |
| 67 (quantum q-index) | CQG / Woronowicz comultiplication | STALL — every positive construction gives only an incoherent ceiling; the one faithful reader (ind_-) is exactly Ω_7 |
| M6 (prismatic) | Bhatt–Scholze prismatic Frobenius | THEOREM — computes local Satake data (anatomy side), not global zeros (spectral side); wrong-object failure, not ζ-reentry |
| 107_166 (topos) | Derived global sections in presheaf topos on Frobenius rulings | THEOREM — unbounded cohomological amplitude (dimension no-go), fails before ζ ever enters |
| 114_a_36/38 (Haran F1/Witt) | Witt-vector Verschiebung correspondences on Haran's arithmetic square | MIXED — 114_a_36 faithfully recovers Λ(n) exactly (real positive result, "closed operatorially, open geometrically"); 114_a_38 shows naive scalar transport collapses (diagonal fold) |

**Never-attempted category changes** (`AUDIT_A_CATEGORY_CHANGES.md §3`, exact quotes):

> "Condensed mathematics / pyknotic objects (Clausen–Scholze) as a replacement for the
> topological-vector-space category D ... not attempted anywhere found."

> "Quillen algebraic K-theory of Spec Z directly (K_n(Z)) ... No attempt in the corpus
> connects K_*(Z) (or higher regulators / Beilinson's conjectures) to the inertia
> invariant m."

> "Non-archimedean / Berkovich analytic geometry over the 'generic fibre at infinity' ...
> No Berkovich space over Spec Z or over the completed adeles is built anywhere in the
> corpus."

> "a triple spectral object whose Chern character gives κ without its zeta spectral
> function being ζ ... this is arguably the sharpest named-but-unattempted target in the
> whole corpus."

> "Cluster categories / cluster algebras, Floer-theoretic invariants beyond the bare
> Maslov index ..., and motivic homotopy theory (A¹-homotopy) ... none appear in the
> corpus."

> "Genuine (Bredon/equivariant) RO(G)-graded stable homotopy for the Klein-four symmetry
> ... Might or might not evade O1–O3 ... but it has not been tried."

---

## Taxonomy: no-gos grouped by mechanism type

**1. Analytic positivity from the explicit formula / Weil quadratic form (direct):**
MW-1, NG-A8, NG-B1–B8 (as a family targeting b_j), CIR-1–8, NG-E3, NG-E4, ES-6, ES-7,
ES-9, ES-10, ES-13 (Fejér–Riesz), ES-25, ES-26, NG-118 (scattering-operator structural
forms). These mostly resolve to MW-1/MW-4 (right form, wrong-direction tools) or are
tautological/circular.

**2. Operator / spectral realizations (Hilbert–Pólya style):** NG-C3, NG-D4, NG-E1,
NG-E2, NG-E5, NG-E6, MW-4, ES-14, ES-15 (heat/dBN), ES-17 (real-zero approximants),
ES-18 (Pontryagin index), NG-65 (Krein–Langer determinant category / D8.5), NG-66
(rank-one escape). Common failure: constructing a self-adjoint object with the right
spectrum already presupposes or re-imports the zero data (Bost–Connes partition = ζ).

**3. Cohomological / geometric realizations of Spec Z (arithmetic-Lefschetz, MW-5):**
NG-C1, MW-2, MW-3, MW-5, NG-107, NG-109, NG-110, NG-113-O1/O2/O3, NG-113-d3, NG-116,
NG-117, NG-63, doc-131/132/160/161/162/163/156/M6/107_166/114_a_36/38 (all of
`AUDIT_A_CATEGORY_CHANGES.md`'s table), ES-20 (Hodge/Lefschetz), ES-27. This is the
largest and most systematically audited cluster, and is the direct locus of row D /
paper 46's problem. Repeated finding: any candidate object that is provably RH-free
(topological, continuous, C-linear) is blind to the sign; the step that imposes
discreteness/orientation/Fredholmicity is exactly where ζ (or an equivalent RH-strength
statement) re-enters — with genuine counterexamples where the failure is pure
representation theory/dimension-counting instead (163's parity argument, 107_166,
114_a_38, M6).

**4. Averaging / Cesàro / statistical mechanisms:** NG-A2, NG-A3, NG-62, ES-2, ES-8,
ES-11, ES-12, ES-19 (GLT duplication), ES-22 (prolate/gap). Common pattern: "small on
average" or "convergent subsequence" does not imply "no individual atom / off-line
zero" — averaging relocates but never crosses MW-2.

**5. Hodge–Riemann / quaternionic constructions:** NG-62b, NG-63 (both = the sharpest,
gapless intrinsic positivity found in the corpus).

**6. Finite compressions / numerics:** NG-A6, NG-A7, NG-F0, NG-F1, NG-68 (GLT numerics),
Phase 119 (open, gated on unrun DH test). These are killed (or left open) by
reproducibility/numerical failure rather than by theorem.

**7. Category-theoretic constructions (operator-algebraic/homotopy/index-theoretic
escapes from D):** the entire `AUDIT_A_CATEGORY_CHANGES.md` inventory (item 3 above);
distinct from cluster 3 in that these attack the *reading mechanism* (what invariant to
extract) rather than building the arithmetic surface itself.

**8. Quantum-group / q-deformation:** NG-67, NG-68, NG-69 (Phase 67–69's specific
sub-attempts within the CAND-1 arc).

**9. Sieve-theoretic / classical analytic-number-theory tools applied directly to b_j
or ω-classes:** NG-A4, NG-B2–B8 individually (Korobov–Vinogradov, Deuring–Heilbronn,
Baker, Montgomery pair correlation, etc.) — each a specific, named classical mechanism
shown wrong-directional or category-mismatched.

---

## No-gos judged possibly wrong or over-generalized

Ranked by how directly the corpus's own text flags the doubt (not by the mapping
agent's own mathematical judgment — these are the doubts *already recorded in the
documents*):

1. **MW-2 (arithmetic-propagation wall)** — stated as "identified from 5 independent
   directions" but is a *pattern* across mechanisms, not a single closed theorem; the
   entire arithmetic-Lefschetz programme (Phases 107–119) is itself an attempt to find
   an arithmetic input that crosses exactly this wall, and OPTIONS.md's live items
   (G-4, condensed math, K-theory) are explicitly proposed as possible crossings.
2. **NG-113-O1 (D is a plain C-vector space, no growth)** — `OPTIONS.md §1b` names
   condensed mathematics as "the most direct candidate for dissolving O1 specifically,"
   untried; explicitly flagged that O2/O3 are not guaranteed to survive a category
   change and "would need independent checking."
3. **MW-3 (Hasse–Minkowski in infinite dimension)** — recorded as "no theorem," i.e.
   absence of a positive tool, not a disproof; genuinely open whether an infinite-dim
   analogue (e.g. via condensed math) exists.
4. **MW-5 / R16 (no quadratic Riemann–Roch over Spec Z)** — `OPTIONS.md §1d` explicitly:
   "It does not settle R16 in general — no scan of the wider arithmetic-geometry
   literature ... has been done from inside this corpus," despite being treated
   elsewhere as if closed by the Connes–Consani counterexample.
5. **NG-107 (Deninger–Morishita bridge kills row (b))** — `OPTIONS.md §1a` flags this
   may not apply to the different, newer G-4 construction (rational Witt vectors,
   2508.05329); "needs checking ... it may already be closed ... or it may survive."
6. **Phase 65's D8.5/H1 closure claim** — `AUDIT_A_CATEGORY_CHANGES.md §4` calls this
   "the single most important item for a follow-up audit": later phase-65 documents
   claim an unconditional closure that the rest of the corpus (through Phase 118)
   silently ignores — an internal inconsistency neither resolved nor endorsed.
7. **LP-112's non-equivalence to RH** — `AUDIT_CONSOLIDATED.md §2` and `OPTIONS.md §0`:
   "Its non-equivalence to RH is *asserted, not proved* — downgraded by a later audit
   (`phase-38/115`)."
8. **NG-B3 (Deuring–Heilbronn: "no known anti-Siegel repulsion")** — phrased as absence
   of a known mechanism, not a proof one cannot exist.
9. **ES-8 (signed vs. absolute-value pointwise bound on ψ(x)−x)** — the doc's own
   closing note: "this class returns to being admissible, although by H0 its closure
   will still have RH-strength" — i.e. explicitly not closed, only the absolute-value
   variant is.
10. **NG-118 (no explicit scattering-operator structure)** — only three named ansätze
    (Toeplitz, Hankel, block-diagonal) were tested; the space of possible structural
    forms for Φ is not enumerated, so "no structure found" is candidly a search failure
    over a finite list, not an exhaustive impossibility proof.
11. **NG-A7 (TDA)** and **NG-66 (rank-one escape numerical proxy)** — both explicitly
    diagnosed as *instrument* failures (wrong statistic / wrong projection), not proofs
    that no such detector construction could work.

---

## Squares explicitly named as "untried" / "never attempted" (exact quotes)

- `OPTIONS.md:34` — Boundary triples for W_λ: **"OPEN, self-labelled 'RH-neutral,
  doable now', never attempted"**.
- `OPTIONS.md:73-74` — Condensed mathematics against O1: **"it does not appear anywhere
  in the corpus's 118 phases."**
- `OPTIONS.md:84-89` — Quillen K-theory of Spec Z: **"Nothing in the corpus connects
  `K_n(Z)` or higher regulators to the inertia invariant `m`. Untried."**
- `OPTIONS.md:101-106` — R16 literature scan: **"no scan of the wider arithmetic-geometry
  literature (arithmetic surfaces, Arakelov theory over number fields, other F1
  candidates) has been done from inside this corpus. This is a literature question,
  cheap to attack."**
- `AUDIT_CONSOLIDATED.md:141-145` — Condensed mathematics: **"The most direct candidate
  for dissolving O1 specifically ... and it does not appear anywhere in the corpus's
  118 phases."**
- `AUDIT_CONSOLIDATED.md:146-150` — Quillen K-theory: **"Nothing in the corpus connects
  `K_*(Z)` or higher regulators to the inertia invariant `m`."**
- `AUDIT_A_CATEGORY_CHANGES.md:124-129` (§3) — Condensed mathematics / pyknotic objects:
  **"not attempted anywhere found."**
- `AUDIT_A_CATEGORY_CHANGES.md:118-123` (§3) — Quillen K-theory of Spec Z: **"No attempt
  in the corpus connects `K_*(ℤ)` ... to the inertia invariant `m`."**
- `AUDIT_A_CATEGORY_CHANGES.md:130-132` (§3) — Berkovich geometry: **"No Berkovich space
  over `Spec ℤ` or over the completed adeles is built anywhere in the corpus."**
- `AUDIT_A_CATEGORY_CHANGES.md:133-138` (§3) — the triple spectral object with
  Chern character giving κ without its zeta spectral function being ζ: **"arguably the
  sharpest named-but-unattempted target in the whole corpus."**
- `AUDIT_A_CATEGORY_CHANGES.md:139-142` (§3) — RO(G)-graded equivariant stable homotopy,
  Floer refinements, cluster categories, motivic A¹-homotopy: **"none appear in the
  corpus."**
- `AUDIT_A_CATEGORY_CHANGES.md:111-117` (§3, RO(G) item) — **"Doc 162 uses the group
  action only to kill `d_2` ...; it never builds the equivariant spectrum itself ...
  it has not been tried."**

---

## Counts per status (this map's 3 tables combined; ≈95 individually labeled items)

- **PROVED-IMPOSSIBLE:** 47
- **EQUIVALENT-TO-RH:** 21
- **ABANDONED** (given up / stalled, no impossibility proof): 22
- **NUMERICAL-ONLY:** 4
- Plus 3 **THEOREM**-graded genuine non-ζ counterexamples inside the PROVED-IMPOSSIBLE
  count (163's parity argument, 107_166, 114_a_38, M6) that fail for reasons unrelated
  to the sign/positivity question at all.

(These counts follow the per-row status column above; several items have compound or
partial status and are counted under their primary/first-listed verdict.)
