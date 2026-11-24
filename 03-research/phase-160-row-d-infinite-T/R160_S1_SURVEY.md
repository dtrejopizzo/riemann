# R160_S1 — Survey S1: phases 0–40, papers 01–15, root files

*Surveyor S1, phase 160. Pure survey: nothing new is claimed. Every statement carries a label and a
form tag.*

**Labels.** PROVED = proved in the cited file (not re-proved here unless a check is recorded); CITED = external
theorem, used as stated; HEURISTIC = argued or measured, not proved (all numerics below are **uncertified** unless
explicitly said to be interval-certified — none in this scope is); OPEN; EQUIV = proved equivalent to RH (or to a
named statement); REFUTED = the corpus itself kills it.

**Form tags** (rule (d)). [prim] = statement about `A_T|P_T` (Paper 46 `eq:form`, `P_T`); [compl] = statement about
`W_T` on `L^2(I_T)` (Paper 46 `eq:W`). Almost nothing in phases 0–40 is written in these window forms; the older
objects are height-localized Gram matrices, Paley–Wiener realizations, CCM traces, etc. Those are tagged
[other: …] with the object named, and §0.2 gives the dictionary to the window forms.

**Scope read.** Root: `00-MAP.md` (Parts 1–10 in full; 11–15 skimmed as context), `MASTER-PLAN.md`,
`NO-GO-LIST.md` (in full), `COMPLETE-PROGRAM-SUMMARY.md` (in full), `EXPLANATION.md`, `OPTIONS.md`,
`03-research/THE_BACKWARD_MAP.md`, `03-research/AUDIT_CONSOLIDATED.md`, `03-research/AUDIT_A_CATEGORY_CHANGES.md`.
Phases: every Markdown file in `phase-0-foundations`, `phase-3-uniform-inequality`, `phase-4-handoff` (+ `proofs/`
ledger), `phase-5-structural`, `phase-6-osterwalder-schrader-reflection` … `phase-31-selberg-moments-c-infinity`, `phase-32-ccm`, `phase-33-dbn`, `phase-34-new-directions` …
`phase-40-close-G1` was opened (head + verdict/synthesis); the memos carrying labelled theorems were read in the
theorem sections (list in §1). Papers `04-papers/01`–`15`: abstract + every theorem/proposition environment of
06–15; abstracts of 01–05. Cross-check: the pre-existing audits
`03-research/phase-102-omega7-closure-campaign/RH-MASTER-CONTEXT/fragments/PHASES_000_025_AUDIT.md` and
`PHASES_026_050_AUDIT.md` were read in full; where they disagree with a memo I say so.

---

## §0 Three hazards a memo must know before citing anything in this scope

### 0.1 Numerics printed as "Theorem"
Several numbered "theorems" in papers 10–14 and phases 7–12 are measurements. They are **HEURISTIC (numerical,
uncertified)**, whatever the environment says:
* Paper 12 `thm:saturation` ("`C(d,T_0)=1` exactly once `2d/\log T_0 \gtrsim 0.85`", and its first clause
  "`C(d,T_0)\le1` for all `d,T_0`" — the latter is RH-strength and cannot be a theorem);
  `04-papers/12-band-limited-weil-carleson/main.tex:143`.
* Paper 14 `thm:reggap` (the law `λ_min(G)=\frac{π^2}{6}β_{min}^2`), `04-papers/14-hodge-index-hyperbolicity-reformulations/main.tex:112`
  (a fit from `phase-10-hodge-envelope-degeneration/DEEPRUN-analysis-M10.1-M10.3.md`).
* Paper 13 `t_c/s^2≈−0.02`; Paper 11 Observations `obs:c1`, `obs:c2`; phase 18 "Case A"; phase 10 frame-gap
  stability tables.

### 0.2 Dictionary old objects ↔ Paper 46 window forms (checked against `def:W`, `eq:W`, `eq:form`, `P_T`)
* The old "band `d`" (test functions `g=f⋆\tilde f` supported in `[−2d,2d]`, prime cut `n\le e^{2d}`) is Paper 46's
  window `T=d`: `N_T=\{\log n<2T\}` (`main.tex:119–124`). The old spectral function `f` / `F` (P7, P8, P12) is
  Paper 46's `\widehat F`. The old archimedean density `Ω(r)=\mathrm{Re}\,ψ(\frac14+\frac{ir}2)−\log π` is `m(τ)`;
  the old comb `F(r)=2\sum Λ(n)n^{-1/2}\cos(r\log n)` is `\sum v_n\cos(τ\log n)`, `v_n=2Λ(n)/\sqrt n`. ✔
* Old polar term "`h(i/2)+h(−i/2)`" = `2\mathrm{Re}(A(F)\overline{B(F)})` of `eq:W` (with `\widehat F(i/2)=B(F)`,
  `\widehat F(−i/2)=A(F)`). It equals `2|f(i/2)|^2\ge0` **only for real even `F`**. Paper 12 (`main.tex:118–126`)
  drops it as "nonnegative, hence conservative": this makes `C(d,T_0)\le1` a *sufficient* condition for local
  positivity, and the stated "`\mathrm{RH}\iff C\le1\ \forall d,T_0`" is proved only in the ⟸ direction; the ⟹
  direction fails as written (under RH, `A_Φ−P_F = \sum_ρ|f(γ_ρ)|^2−(\text{polar})` can be negative). **Not a
  statement about `A_T|P_T`**: `A_Φ−P_F` is `\mathfrak a_T` on a height-localized subspace of `L^2(I_T)`, with no
  primitivity constraint.
* Paper 08 / B2-THEOREM's `\mathfrak t(F)=\mathfrak a+\mathfrak q−\mathfrak p` on `PW_d` is `W_T` (`T=d`) [compl],
  evaluated through its zero side. At fixed `T`, `λ^W_T>−∞` in the `L^2` norm is elementary (finite comb, `eq:A`);
  Paper 08 Theorem A's content is the realization in the zero-sampling norm `\mathfrak t_+`, not a bound on `λ^W_T`.
* The old "primitive part `Π^⊥`" (phase 15 M1–M3) = tests killing the two pole classes = Paper 46's `P_T`
  (`A(F)=B(F)=0`); the old "ample cone `2(\int f e^{−u/2})^2`" (phase 15 M2) is the polar term for real even `F`. ✔

### 0.3 Index conventions and paper numbers
* `κ` = negative index of the Weil form. Phase 21 proves `κ=2m`, `m` = number of off-line quadruples (each quartet
  gives two `J`-swap pairs of signature (1,1), `phase-4-handoff/B3-KREIN-STRUCTURE.md` §2 C2). Papers 08/11 and
  phase-16-surf-witness-variety memos write "`κ=\#`off-line zeros", which is off by a factor 2. Moreover every "`κ=2m<∞`" in phases
  26–40 is **conditional** on a Pontryagin realization / Hypothesis D (`PHASES_026_050_AUDIT.md`, critical finding 2).
* Memos in phases 15–40 cite papers as `P7, P8, P21, P35, P39–P44` in the *old* `06-papers/` numbering. P7 = 07,
  P8 = 08, but e.g. "P21 (Lefschetz dichotomy)" is `04-papers/17-sl2-triple-hard-lefschetz-analogy`, "P41–P44" are roughly
  `04-papers/27–30`. Resolve every P-number by title before citing.

---

## §1 What was done (one line each)

### Root files
| file | content |
|---|---|
| `00-MAP.md` | Program map, Parts 1–15: survey → ω-class arc → localized Weil detector → Kreĭn realization → eight-language wall and wrong-sign capstone → log-correlated path → strategy closure → SURF → ω-flow → phases 21–61 → Ω₇/ARP-P → Arc C (rows a–d). |
| `MASTER-PLAN.md` | Repository organization, unconditional ledger, the "only route open" (Li–Keiper Ω₇; row (d); sub-RH targets), guardrails. |
| `NO-GO-LIST.md` | Registry: NG-A1…A8, NG-B1…B8, NG-C1–C3, NG-D1–D4, NG-E1–E7, walls MW-1…MW-6, CIR-1…8, OK-1…12, CAND-1…3, post-28 failures, phase-137 audit of phase-65 `RH-PROOF.md`. |
| `COMPLETE-PROGRAM-SUMMARY.md` | Arc A / Arc B / CCM frame / phases 34–119 verdict logs; walls MW-1…MW-7 ("master quantifier"); unconditional ledger (Part 9). |
| `EXPLANATION.md` | Plain-language account (layers 1–6). |
| `OPTIONS.md` | Decision document : the non-RH-equivalent open targets (Diana L8, Lemma 108, C_B, C5⇒κ<∞, LP-112, GAP-157.A, boundary triples), category changes (condensed, Quillen K, R16). |
| `03-research/THE_BACKWARD_MAP.md` | Requirements d0–d5 of the Hodge-index proof; status after phases 113–118 (d3 impossible inside 𝒟; row (d) = RH). |
| `03-research/AUDIT_CONSOLIDATED.md` | Discreteness hypothesis dominant not universal; non-RH-equivalent open items; CC/Deninger inventory; strongest positive result (quaternionic HR, gapless). |
| `03-research/AUDIT_A_CATEGORY_CHANGES.md` | Inventory of 12 category-change attempts (docs 131, 132, 160–163, 156, phase 65, 67, M6, 107_166, 114_a_*), THEOREM vs STALL; untried categories. |

### Phases
| phase (path under `03-research/`) | what was done |
|---|---|
| `phase-0-foundations` (`0A1`,`0A2`,`0A3`,`0B`,`phase0-plan`) | `Q` identified as the Hermite–Gauss Gram of the Weil functional; the compression question 0A2 (faithfulness ≠ positivity); de Branges chain + Conrey–Li guard; truncation lemma technical, (LB) = RH. |
| `phase-3-uniform-inequality` (`phase3-plan`, `engine-spec`) | (LB) = uniform limit positivity = RH; Flanks I (Connes trace) and II (de Branges chain) planned; engine specification. |
| `phase-4-handoff` (`B2-THEOREM`, `B3-KREIN-STRUCTURE`, `PAPER-A`, `RH-ENDGAME`, `proofs/00-PROOF-LOG` + 23 day-memos) | 22-day operator programme: EF-identity on a dense core, Lemmas A–D, semibounded realization modulo (H), Kreĭn identity `\mathfrak t=E^*JE`, angular operator, zero-side no-go (= Paper 08); endgame: the only sign route is "`\mathcal T=A^*A`". |
| `phase-5-structural` | CC semilocal residual `Id−K_{CC}` (prolate bridge real only for localized P7), Kreĭn template shared by P8/CC/de Branges (no identification), classification programme M5 (T1 anti-tautology, T2 forced transition), anatomy identity T3, `R_p≈a_pW(\log p)`, T4 Bessel/Carleson + concavity; engine-gate failures in `experiments/`. |
| `phase-6-osterwalder-schrader-reflection` | Osterwalder–Schrader moonshot: S1 recasting correct; S2 per-place prime form `G_p` indefinite (REFUTED mechanism); S2-followup "envelope ≥ comb pointwise" retracted (comb distributional). |
| `phase-7-weil-carleson-sine-kernel` | Band-limited Weil–Carleson constant `C≡1` (saturation, numerical); second order = sine kernel; Connes core "same wall, multiplicatively dressed". |
| `phase-8-heat-flow-monotonicity` | dBN heat flow: Lyapunov identity (Gate B), arithmetic blindness, Rodgers–Tao coupling → upper tail of pair correlation; backward-collision margin (numerical). |
| `phase-9-unconditional-universality` | N6 spearhead no-go (monotone functionals are generic / archimedean / explicit-formula); T9-A (Montgomery `F(α)\ge0` is wrong-signed); T9-cal exchange rate `α_{req}\asymp N(T)^{1/3}` (heuristic). |
| `phase-10-hodge-envelope-degeneration` | Cohomological turn: bare Lorentzian Hodge gap degenerates; regularized gap = sine-kernel Gram of zeros, `\frac{π^2}{6}β_{min}^2` (numerical); prices exactly as T9-cal. |
| `phase-11-hyperbolicity-total-positivity` | Jensen/hyperbolicity/MSS: interlacing present, shift preserver arithmetic-blind, real-rootedness is Hermite-form positivity (capstone holds). |
| `phase-12-meta-obstruction-moment-problem` | Log-correlated fields / multiplicative chaos (native upper bounds); probabilistic–deterministic barrier N7; Littlewood-lemma closure attempt gives density, not absence; supercritical regime = moment problem (heuristic chain). |
| `phase-13-omega-class-multiplicative-chaos` | `d_k(n)=k^{ω(n)}` on squarefree `n`; freezing ↔ large deviations of `ω` (RH-independent). |
| `phase-14-off-diagonal-anchor-asymmetry` | Anchor framework (Landau singularity), N8 density→absence gap, dlVP counterexample to N8's universal form, Stage 1–2 (anchor collapses to edge machinery), Motohashi/`z^{ω}` weight self-referential → ω→zeros line closed. |
| `phase-15-arithmetic-hodge-index` | Anatomy–Kreĭn–Hodge: M1 pairing + trace identity + effectivity, M2 ample cone, M3 (= RH) with 8 attempts, M4 archimedean `\mathfrak{sl}_2`, M5 Lefschetz dichotomy, M6 prismatic, M7 advisor audit, M8 refuted "proof", M9 discovery run, M10 Arakelov equivalence one-directional. |
| `phase-16-surf-witness-variety` | SURF specification sheet; Pillar-1 triage (prismatic rejected, `\mathbb F_1` untestable, GL₂/Eisenstein survives); resonance pairing theorem (definite for every configuration); `H(E_ξ)` as the indefinite object; Herglotz criterion; self-adjoint realization set-up. |
| `phase-17-surf-2-design` | SURF 2.0; Klein-four involution; Route-2 testbed γ-blind; SURF-B: real structure is a symmetry, not a positivity; reduction to the canonical-system inverse problem. |
| `phase-18-negative-directions-portrait` | Portrait of negative directions; explicit-formula coupling: on-line neighbourhood does not protect (numerical toy). |
| `phase-19-omega-rate-freezing` | Forward ω-flow: `k^2` from Selberg–Delange/Erdős–Kac; rate function; B-smooth condensation; random multiplicative maximum (RH-independent). |
| `phase-20-zero-omega-bridge` | ω information barrier `F_q=ζ^qG_q`; error term of `C_k(h,N)` is `O(N^{−1/2+ε})` ⟺ RH. |
| `phase-21-negative-directions-geometry` | Parity `κ\equiv0\pmod2`, `κ=2m`, Lorentz decomposition of the negative space; Pontryagin regime `ξ=ξ_0P_{4m}`; Conjecture EX (`κ∈\{0,∞\}`). |
| `phase-22-pontryagin-finite-defect` | Hypothesis D (finite `m`): modified explicit formula, KV constraint on `b_j`, Thm 22-C.6 (no continuous functional detects the defect), spectral rigidity attempt. |
| `phase-23-two-scale-defect-structure` | Exact Hadamard effect of a quartet on `\log|ζ(\frac12+it)|`; structure function `S_2`; barrier Thm 23-C.1/C.2. |
| `phase-24-lower-bounds-bj` | Lower bounds for `b_j`: none; universal Lorentzian local profile; rigorous-chaos inventory. |
| `phase-25-lower-bounds-bj-audit` | Fifteen-mechanism audit (all fail for a lower bound on `b_j`); dBN ↔ `b_j`; Kreĭn–LP factorization; wall W4-RSRP. |
| `phase-26-krein-connes-bridge` | Bridge conjecture `κ(Q)=\mathrm{neg.ind}(H_C)`; V.2 fails (`x^{b+iγ}\notin L^2(C_{\mathbb Q})`). |
| `phase-27-adelic-rigidity` | V.2 = non-unitary Grössencharacters (Thm 27-B.4); local–global walls A and B. |
| `phase-28-four-fronts` | Four fronts (dBN/Kreĭn, APS-η, K-theory, transverse energy); second variation; σ-curvature of `\log|ξ|`; LP class; sector decomposition of `G(t)`. |
| `phase-29-zeta-spectral-triples` (docs 00–54) | CCM zeta spectral triples: even-simplicity H1, convergence H2, kernel positivity, Jacobi/Weyl–Titchmarsh, potential `C_∞`, Inc. Inv. ⟺ RH (doc 40), deficit formula (42), single-point theorem (43), new-structure proposals (46–54). |
| `phase-30-langlands-bridge-c-infinity` (55–57) | Langlands bridge for `C_∞^{(F)}`; Poincaré duality in 𝓜𝓜 (why Weil/Deligne does not transfer); dBN–`C_∞` bounds. |
| `phase-31-selberg-moments-c-infinity` (58) | Moments of `C_∞(γ_n)`; `M_1=0` ⟺ RH. |
| `phase-32-ccm` (59–69) | Semilocal Jacobi discrepancy, Christoffel scale, CTP "`T_λ=0\ ∀λ` ⟺ RH" (doc 64, later found to rest on the false `W_λ\ge0`), PPP/Wronskian. |
| `phase-33-dbn` (70–89) | dBN × CCM trace; `T_λ` via the explicit formula; Li vs CTP; "arithmetic Castelnuovo–Severi" attempt; `dν\ge0`; Nyman–Beurling variational; KL/entropy; completeness; central object `dν`. |
| `phase-34-new-directions` (90–97) | Dir. A external arithmetic (blocked, `C_A` RH-equiv.); Dir. B Pontryagin/`H_C` (C5, `C_B`, Brodskiĭ–Livšic, Euler subspace, Maslov); Dir. C inverse Jacobi (sum rule); Dir. D second variation / shadow minimizer. |
| `phase-35-five-fronts` (98–103) | Toy quadruple test (absorption theorem, errors found in 93/95); CF rigidity (99, PARTIAL); semilocal Maslov (100: `μ_{\{∞\}}=0`, Conjecture 100.A, obstacle O_SL); Fourier-interpolation frames (101); Bagchi–Voronin audit (102); `W_λ>0` (103, later refuted). |
| `phase-36-ABC-forms` (104–108) | Effective SR_d (104); 2-prime `∂_t–∂_x` coupling (105); amplifier functor ⊠ (106); two-variable Weil form `\mathcal W_2` (107); sieve→index bridge dead (108). |
| `phase-37-physics` (109–113) | Critical anchoring / D-109 (`RH=(m<∞)∧(m∈\{0,∞\})`); inertia-reader axioms L1–L6 and impossibility Thm 4.3 (110); Diana L8 (111); LP-112 ⟹ `m∈\{0,∞\}` (112); LP-112 vs literature (113). |
| `phase-38-final-audit` (114–118) | `W_λ\ge0` REFUTED (114); doc-112 theorem survives with corrections (115); Stepanov theorem survives (116); tensor-index identity survives with corrections (117); trace criterion repaired by moment rigidity (118). |
| `phase-39-G1G2-interface` (119–121) | Backward-derived axioms R-SIG, R-FIN, R-LEF, R-PESO, R-NC, R-TRZ; in-source inventory of CC/CCM; gap grading (G1 technical-ish, G2 conceptual). |
| `phase-40-close-G1` (122–124) | CC Serre duality is Pontryagin duality (no symmetry character; self-dual point has zero spaces); tolerance square PARTIAL (cokernel fixed, rank not); CC Weil positivity is spectral, not a Hodge index. |

### Papers `04-papers/01`–`15`
| paper | content |
|---|---|
| 01 critical-line survey | Survey (analytic / spectral / algebro-geometric); every route reduces to a positivity. |
| 02 ω-class decomposition | `B(N)\le N^ε ⇒` Lindelöf (sufficient, plausibly stronger than LH); computations. |
| 03 sign of inter-class interference | `r` has mean 0 by MVT; sign set by conditioning (peaks +, troughs −). |
| 04 Davenport–Heilbronn null | No power-law growth of DH partial sums up to `N=10^9` at off-line zeros (numerical). |
| 05 ω-hierarchy / chaos | `d_k=k^{ω}`, freezing ↔ large deviations of `ω`, BRW levels (RH-independent). |
| 06 why RH resists | Classifier `D_0`; `thm:gap` (finite-to-full gap in four positivity families); `thm:LI` (no Frobenius periodicity under LI). |
| 07 localized Weil detector | Forced negativity (`thm:forced`), stretched-Gaussian truncation (`thm:trunc`), detector (`thm:detector`), uniform limit ⟺ RH (`prop:dichotomy`). |
| 08 Weil–Kreĭn realization | `thm:A` (semibounded, mod (H)), `thm:B` (`\mathfrak t=E^*JE`, angular `K`), `thm:C` (zero-side no-go). |
| 09 stable fingerprints | Local-arithmetic stability `e^{−α(\log P)^2}`, anatomy identity, extremal reduction. |
| 10 anatomy as local invariant | Euler product ⟺ factorizing anatomy; Satake recovery; Carleson reformulation (`thm:carleson`). |
| 11 Pontryagin index / finite defect | `prop:red` (RFB_X ⇒ `κ<∞`); computations: RFB_X fails for fixed X, saturation approached. |
| 12 band-limited Weil–Carleson | `C(d,T_0)`, saturation (numerical), sine-kernel second order, identification with CC prolate compression, five-language wall. |
| 13 heat-flow Lyapunov | `thm:lyap`, `thm:nogo` (N5), extremal reduction `Λ` = first backward collision. |
| 14 wrong-sign obstruction | Regularized Hodge gap (numerical law), hyperbolicity = Hermite positivity, capstone across eight paradigms. |
| 15 finite-to-full uniformity | `thm:crit`, `thm:overRH` (uniform Hermite convergence is strictly stronger than RH), `thm:hr` (HR stability for towers). |

---

## §2 What FAILED, and exactly why (the list memos must not repeat)

Grouped by mechanism. Each item: the attempt → the killing theorem/counterexample → file.

### 2.1 Local / per-place / product positivity (relevant to B3, B4, B12, B20)
1. **Per-place reflection positivity (Euler lattice).** The local prime form is `\int|\widehat ψ|^2G_p` with
   `G_p(r)=\frac{2\log p}{p|1−z|^2}(\sqrt p\cos(r\log p)−1)`, `z=e^{ir\log p}/\sqrt p`: `G_p(0)>0`,
   `G_p(π/\log p)<0`. PROVED indefinite (closed form). REFUTED mechanism.
   `phase-6-osterwalder-schrader-reflection/M-OS-2-S2-local-REFUTATION.md` §1; NG-E1.
2. **"OS reconstruction gives Hilbert–Pólya for free."** The two-point function `\sum_ρ e^{iγ_ρu}` is
   oscillatory, not OS-decaying. RETRACTED. `phase-6-osterwalder-schrader-reflection/M-OS-1-S1-setup.md` (header); NG-E5.
3. **"Archimedean envelope ≥ prime comb pointwise."** The comb is a distribution: `Ω_∞−\sum_pG_p=2π\sum_ρδ_{γ_ρ}
   −(\text{pole})`; no pointwise comparison, `\widehat φ\toδ` illegal. RETRACTED.
   `phase-6-osterwalder-schrader-reflection/S2-followup-incoherence.md` (header); NG-E6. (See §5 I9 for the rigorous replacement.)
4. **Hasse–Minkowski factorization `Q=Q_∞\prod_pQ_p`.** Wall A: the zero sum does not factor over primes; Wall B:
   no HM in infinite dimension. `phase-27-adelic-rigidity/02-C-wall-analysis.md`; NG-C1; MW-3.
5. **Additive adelic Maslov index `μ_{\mathbb A}=μ_∞+\sum_pμ_p`.** The index does not add, it *filters* (window
   increments); the additive form presupposes the refuted factorization. `phase-35-five-fronts/100-maslov-semilocal.md`
   §6.1.
6. **"Prime incoherence (ℚ-independence of `\log p`) gives a positivity margin."** Adjoining primes drives the
   band constant *up* to saturation (numerical, Paper 12 `thm:saturation` remark); positivity of `A_Φ−P_F` *is* the
   reality of the zeros. `04-papers/12-band-limited-weil-carleson/main.tex:143–170`; `phase-7-weil-carleson-sine-kernel/P7-OPEN-CORE-carleson-saturation.md`.
7. **Brodskiĭ–Livšic dissipativity.** `Θ(z)=ξ(\frac12+z)/ξ(\frac12−z)` has `|Θ|\equiv1` (unitary, not dissipative).
   **Euler subspace:** the tests with Mellin mass in `\mathrm{Re}\,s>1` form a `Q`-positive subspace `\mathcal E`,
   but density of `\mathcal E` in `\mathcal K` is ⟺ RH (Thm 2.12). **Kreĭn resolvent theorem:** returns the
   starting condition. `phase-34-new-directions/96-direction-b-third-layer-dissipativity-characteristic-function.md` (angles 1, 2, 4).

### 2.2 Zero-side and Pontryagin/index attacks (relevant to all)
8. **Bounding the angular operator from the zero side.** Paper 08 `thm:C`: the depths `b_ρ` enter `\|K\|` only
   through `\mathfrak t` itself; sign-agnostic bounds give `\|K\|^2\gtrsim e^d` (wrong side). PROVED no-go.
   `04-papers/08-krein-space-weil-form/main.tex:126`; `phase-4-handoff/PAPER-A.md` §8.
9. **Magnitude bounds (RFB / Carleson / sampling / density).** They give `|\mathfrak t_-|\le C\mathfrak t_+` with
   `C\ge e^d>1`; lowering `C` below 1 *is* RH. Point-to-point routes (Schur/Gram/Jaffard) pay `P=ρ\ell\to∞`
   (NG-E4); global Cauchy–Schwarz vacuous (NG-E3). `phase-4-handoff/RH-ENDGAME.md` §2; `proofs/00-PROOF-LOG.md`
   ledger (rows "over-sampling FORCED", "❌ global V vacuous").
10. **Eigenvectors `x^{b_j+iγ_j}` of `H_C` / bridge `κ=\mathrm{neg.ind}(H_C)`.** Not in `L^2(C_{\mathbb Q})`
    (`\int x^{2b−1}dx=∞`); Kreĭn–Langer gives only "at most". REFUTED as stated; V.2 ≡ non-unitary characters
    (27-B.4). `phase-26-krein-connes-bridge/01-attack-V2.md` §10; `phase-27-adelic-rigidity/03-verdict.md` §2; NG-C2, NG-C3.
11. **Finite-defect route `κ<∞` via a prime-tail relative form bound.** For fixed `X`, RFB_X fails as `d\to∞`
    (`X^*(d)\approx e^{2d}/10`) and the near-null space grows linearly in `d` (numerical). `04-papers/11-…/main.tex`
    `cor:c1`, `cor:c2`. Structural reason: RFB needs square-root cancellation of `\sum_{n\le N}Λ(n)n^{−1/2}\sim2\sqrt N`
    against `\log` (remark after `prop:red`).
12. **Index/Maslov/spectral flow as an autonomous inertia reader.** Doc 110 Thm 4.3: in the class ℱ of
    test-accessible explicit-formula quadratic functionals, (L2)+(L3)+(L4) are inconsistent: sub-resolution
    windows are positive in both worlds (blind), resolving windows give a binary index whose uniform bound is RH,
    and the finite off×off block is not test-accessible. PROVED for (a),(c); (b) as stated there.
    `phase-37-physics/110-invariants-that-count-modes-one-by-one.md` §4.2. Spectral flow of the Euler filtration: each finite CF step
    has zero flow; the limit needs MW-6 (Prop. 3.4). Parity invariants are vacuous (Prop. 2.6).
13. **Inertia via tensor amplification without finiteness.** Abstract tensor products are sterile (superadditivity
    and growth computed from the same signature data, Prop. 3.9); products of L-functions *unite* zero sets
    (additive `κ`), Rankin–Selberg in GL(1) returns ζ; scaling-site correspondences `Ψ(λ)` are isometries (preserve
    `κ`); multiplicative convolution collapses to Weil positivity. `phase-36-ABC-forms/106-amplifier-functor-systematic-search.md`
    §§3.1–3.4. Doc 110 Obs. 5.3: "Form B is Deligne's trick minus the finiteness".
14. **Sieve→index bridge.** The needed bound is "uniform in windows" where the sieve gives "on average over
    windows" — RH re-encoded; the arithmetic kernel `K(N)=\sum_{d|N}Λ(d)Λ(N/d)φ(d^2/N)` has no sign change yet the
    index is positive under ¬RH. DEAD. `phase-36-ABC-forms/108-sieve-index-bridge-formulation-unconditional-inventory.md` §0, §7.

### 2.3 Finitization and uniformity (relevant to B14, B15, B19)
15. **Finite-dimensional (Frobenius-periodic) model of ζ's positivity.** Under LI of the ordinates there is no
    period `τ` and finite `\{β_j\}` with `\{γ_n\}\subseteq\{β_j+kτ\}`. PROVED (conditional on LI).
    `04-papers/06-positivity-formulations-function-field-analogy/main.tex:257` (`thm:LI`).
16. **Finite-order positivity → full order.** In all four families (Hodge, Hankel, PF, combinatorial Hodge) each
    finite order is unconditional and the full order is RH; thresholds `T_0(k)\to∞`. `06/main.tex:200`
    (`thm:gap`, proof sketch — HEURISTIC in its "no general theorem bridges" clause); `15/main.tex:93` (`thm:crit`,
    PROVED).
17. **Uniform convergence of Jensen polynomials to Hermite.** Strictly stronger than RH; the relaxation is RH itself.
    PROVED. `04-papers/15-…/main.tex:165` (`thm:overRH`). Shift preserver arithmetic-blind (`cos t` control passes
    every test): `phase-11-hyperbolicity-total-positivity/M11.3-verdict-preserver-blind-MSS-pivot.md`. Real-rootedness = Hermite-form PSD:
    `phase-11-hyperbolicity-total-positivity/M11.4-5-…md`; Paper 14 `thm:hermite`.

### 2.4 Dynamics / heat flow / variational (relevant to B11, B16)
18. **dBN flow as a mechanism.** `\dot{\mathcal L}=−2\sum_{j\ne k}(y_j−y_k)^2/|z_j−z_k|^2` holds for *every*
    conjugate-symmetric configuration (arithmetic-blind, N5); forward direction gives only `\mathcal L(0)\ge0`.
    PROVED. `04-papers/13-…/main.tex:150` (`thm:nogo`); `phase-8-heat-flow-monotonicity/GATE-B-verdict-sixth-language.md`.
19. **Arithmetic-aware monotone functional.** Every flow-monotone functional is generic, archimedean (controls the
    count), or explicit-formula (sign = Weil). N6. `phase-9-unconditional-universality/M9.1-N6-spearhead-verdict.md`.
20. **Minimization formulation (energy minimized at `b_j=0`).** Under RH `σ\mapsto\log|ξ(σ+iγ)|` is strictly
    convex at `σ=\frac12`; the Weil form is locally *maximized* at `b=0` (NG-D1, NG-D2). `phase-28-four-fronts/06-curvature-xi.md`
    §5. Controlling `G_ζ(t)` from Euler + FE is ⟺ RH (NG-D3, `phase-28-four-fronts/08-decomposition-sectors.md` Prop. 1).
    Sign conventions of phase 28 need an external re-check (`PHASES_026_050_AUDIT.md`, finding 3).
21. **Second variation of the variational distance / shadow minimizer (Dir. D).** Doc 98: the "transverse"
    variation of Doc 93 was tangential; the true transverse second variation at `f_0^{on}` is *negative*; the EL
    kernel of Docs 95/97 is odd (equations vacuous); absorption theorem: the `δ^2` deficit is absorbable into
    `\overline{\mathcal M}`, so `\tilde δ_λ(δ)=o(δ^2)`. Dir. D degraded. `phase-35-five-fronts/98-b-d-toy-test-an-off-critical.md` §§3–5.
22. **KL / Jensen–Shannon / Wasserstein / Herglotz of `dν`.** All vanish iff RH; no independent verification.
    `phase-33-dbn/86-relative-entropy-and-extremality-of-synthesis.md`.
23. **Form A (DBN × Euler coupling, 2-prime approximant).** `\mathcal T(t,x)=0` in the whole interior (heat flow
    preserves reality); on the boundary the per-prime increments change sign (positive for `p\le7`, negative for
    `p\ge11`) and the prime sum diverges like `−\frac{5\sqrt2}{8}\log`. PROVED (closed forms).
    `phase-36-ABC-forms/105-coupling-first-test-of-form.md` §§3, 5.

### 2.5 Hodge / cohomological / geometric (relevant to G1: B1, B2, B5, B6, B7, B17, B18, B19)
24. **Bare Hodge gap of the band-limited form.** Degenerates as the band grows; the regularized gap reprices exactly
    to the pair-correlation exchange rate (capstone holds). `phase-10-hodge-envelope-degeneration/M10.4-verdict-route-priced-capstone-holds.md`
    (numerical basis).
25. **Kähler form from the spectral data.** The only `(1,1)`-form compatible with `(J,Q)` is `Q(J\cdot,\cdot)`, whose
    positivity is RH; the flow `\mathcal T` is unitary, has dense (not integer) spectrum, cannot be the Lefschetz
    grading. PROVED (Prop. `omega`). `phase-15-arithmetic-hodge-index/M3-attempt8-the-kahler-form.md` §1. Bochner positivity gives only the
    lower bound (attempt 2); symmetric powers control Satake, not zeros (attempt 4).
26. **Lefschetz dichotomy.** Continuum `\mathfrak{sl}_2` is principal series (no lowest weight, no HR form); a
    discrete integer grading conflicts with LI. `phase-15-arithmetic-hodge-index/M5-the-lefschetz-dichotomy-closure.md` (Prop. `ps`).
27. **Prismatic / Sen / monodromy grading.** Frobenius eigenvalues are local Satake data (trivial for ζ), the wrong
    side of the explicit formula. `phase-15-arithmetic-hodge-index/M6-the-prismatic-route-assessment.md`; Pillar-1 rejection
    `phase-16-surf-witness-variety/01-pillar1-triage-three-routes.md`.
28. **Arakelov / Faltings–Hriljac / Yuan–Zhang Hodge index.** Exists but controls heights (`\widehat{\mathrm{Pic}}^0`,
    BSD-type), not the zero-carrying `H^1`; "RH ⟺ witness variety" is only ⇐ (and near-tautological).
    `phase-15-arithmetic-hodge-index/M3-attempt6-elliptic-control-heights-vs-zeros.md`; `phase-15-arithmetic-hodge-index/M10-arakelov-equivalence-audit.md`.
29. **Submitted "Frente 1 (Connes–Deninger)" proof.** Six fatal flaws; F1: the scaling action has continuous
    spectrum and infinite invariant measure, does not integrate to `SU(2)`. REFUTED. `phase-15-arithmetic-hodge-index/M8-front1-proof-audit-REFUTED.md`.
30. **Modular-surface resonance / Maass–Selberg / Eisenstein pairing.** Kernel `K_{ρσ}=1/(s_ρ+\overline{s_σ}−1)`,
    `s_ρ=ρ/2`, is negative-definite for *every* configuration in the strip (Hardy kernel of a half-plane). PROVED.
    No resonance pairing can carry `κ`. `phase-16-surf-witness-variety/05-resonance-pairing-definite-THEOREM.md:12–31`; MSZ proposal
    rejected `phase-16-surf-witness-variety/04-MSZ-pairing-hits-CAP.md`; residue sign not `β`-sensitive `phase-16-surf-witness-variety/03-residue-pairing-nontrivial.md`.
31. **Real-structure involution `j(s)=1−\bar s` as a sign handle.** Weak reading holds unconditionally (quartets are
    `j`-symmetric), strong reading = RH. A symmetry, not a positivity. `phase-17-surf-2-design/04-SURF-B-resolvent.md` §1.
32. **CC "Serre duality with tolerance" as a signature.** It is Pontryagin duality `\widehat A\times A\to U(1)`
    between different groups; no symmetric/alternating character exists; at the self-dual divisor `D_0=−\{2\}` both
    spaces are 0. `phase-40-close-G1/122-symmetry-bit-the-character.md` §0. Tolerance repairs the cokernel, not the functorial rank
    (Yoshida Ex. 6.5 root). `123-construction-of-the-cohomology-of-the-square.md` §§1.3, 3. CC Weil positivity is the spectral
    one (RH-equivalent when globalized; fails NC3). `124-connes-consani-s-weil-positivity.md` §6.
33. **Poincaré duality in the category 𝓜𝓜 / direct Deligne transfer to ℚ.** Trivial degree factor, no norm
    tension forcing the line. `phase-30-langlands-bridge-c-infinity/56-poincar-duality-on-construction-non-degeneracy.md`; `55-langlands-bridge-for-automorphic-l-functions.md`.
34. **K-theory front.** `[P_−]=κ` is tautological; KK homotopy `H_C\sim\mathrm{Id}` open. *Check against
    definitions:* the memo's "`K_0(C^*(C_{\mathbb Q}))\cong\mathbb Z`" is doubtful: `C^*(C_{\mathbb Q})\cong
    C_0(\widehat C_{\mathbb Q})`, `\widehat C_{\mathbb Q}\cong\mathbb R\times(\text{countable discrete})`, whose `K_0`
    is `\bigoplus K_0(C_0(\mathbb R))=0`. `phase-28-four-fronts/03-front-C.md` §§2, 9.
35. **η-invariant by Fourier anticommutation.** The FE involution preserves eigenvalues (`JT_0J^{-1}=T_0`), not
    negates. NG-D4, `phase-28-four-fronts/02-front-B.md` §4–5 (the anticommutation identity itself remains open, §3b).

### 2.6 ω-class, chaos, pair correlation, lower bounds (relevant to B11, B13, B14)
36. **ω-class route to Lindelöf/RH.** Target stronger than LH (circular), parity problem, MVT kills unconditional
    cross-covariance, α_B not crossing Bourgain. NG-A1–A4; `04-papers/02`, `03`.
37. **ω sees the zeros.** Explicit formula is ω-blind (`Λ(n)z^{ω(n)}=zΛ(n)`); the `z^{ω}` Motohashi weight is
    ζ-isobaric (self-referential); zeros enter only an error term ⟺ RH. `phase-14-off-diagonal-anchor-asymmetry/STRATEGIC-where-omega-touches-the-zeros.md`,
    `M14.3-VERDICT-…`, `phase-20-zero-omega-bridge/02-proof-error-correlation.md`.
38. **Littlewood lemma to absence.** Gives density (weighted count of `β−σ_0`), not absence.
    `phase-12-meta-obstruction-moment-problem/M12.11-N7-closure-attempt-littlewood.md`.
39. **Pair correlation / GUE as input.** `F(α)\ge0` gives lower bounds on clustering (wrong sign); the needed
    upper bound for `α>1` is the prime-variance frontier. `phase-9-unconditional-universality/T9A-verdict-wrong-sign.md`. Extremal, not
    average: one tight pair decides `Λ` (`phase-8-heat-flow-monotonicity/UPPER-TAIL-verdict.md`). NG-B8.
40. **Lower bounds for `b_j`.** Fifteen mechanisms (KV, Selberg density, Levinson–Conrey, Deuring–Heilbronn, BN,
    Bohr, Baker, Weil–Deligne, Turán, Littlewood Ω, large sieve, Montgomery, de Branges, Selberg trace, Weil
    positivity) all fail. `phase-25-lower-bounds-bj-audit/01-audit-classical.md`; NG-B1–B7; CIR-1–5.
41. **Siegel-type repulsion for quadruples; Turán power sums; zero-density to finiteness.** Anti-Siegel (two
    quadruples are seen *worse* than one); Turán circular via Landau–Ingham; every known count is binary
    (0 or `T^θ`). `phase-37-physics/111-target-l8-is-an-unconditional-bound.md` §§2.6, 3, 4.
42. **Bagchi strong recurrence / pointwise replication from B² almost periods.** Strong recurrence ⟺ RH; under
    H(m) the Rouché-good shifts have upper density 0 (Prop. 2.6) — the distributional direction is proved *against*.
    `phase-35-five-fronts/102-audit-of-the-bagchi-criterion-strong-recurrence.md`; `phase-37-physics/112-…md` §2.4.

### 2.7 CCM trace thread (phases 29–33; relevant to B1, B20)
43. **`W_λ\ge0` (Abel kernel positivity).** False: `\int W_λ\,dm_∞=0`; Abel summation sign flip, missing boundary
    term, coefficient `n` should be `2n+\frac12`. REFUTED, propagated into docs 64, 70–90, 103 and old P39–P43.
    `phase-38-final-audit/114-adversarial-audit-of-doc-103-positivity.md`. Consequence to check in any reuse: doc 85's "completeness in
    `L^2(W_λdm_∞)`" presupposes a positive weight.
44. **Inc. Inv. / `C_∞(γ_n)=0` / deficit measure `μ_{off}`.** Every formulation is equivalent to zero location
    (MW-7, Hadamard barrier); `C_∞` is built from conditionally convergent / Abel-renormalized series (cf. NG-E6).
    `phase-29-zeta-spectral-triples/40-…`, `42-…` §7, `43-…` Thm 4.2 (EQUIV; HEURISTIC as to the representation, see doc 44 §1).
45. **CF rigidity route (CCM zeta spectral triples).** Passes the circularity filter at finite level (real spectra of
    `H_x` unconditional), but the only link to ζ is `\lim_λ μ_λ\ge0` = semilocal Weil positivity (MW-1/MW-6) and the
    prime tail diverges `\sim λ/\log λ` (Lemma 5.1). PARTIAL. `phase-35-five-fronts/99-convergence-and-carath-odory-fej-r-rigidity.md` verdict.

---

## §3 What still STANDS

### 3a Proved results (label, form, file)

| # | statement | label | form | file |
|---|---|---|---|---|
| 1 | RH ⟺ `W_T\ge0\ ∀T` ⟺ `\mathfrak a_T\ge0` on `P_T\ ∀T`. | CITED (Weil 1952; Bombieri 2000; Paper 45 Thm 10.4) | [compl],[prim] | `04-papers/47-…/main.tex:134–147` |
| 2 | Forced negativity: an off-line zero at displacement `δ` within `O(σ)` of `T_0` gives `λ_{min}(Q)\le λ_{min}(Q_0)−c`, `c\sim δ^2A(γ)`. | PROVED (constants matched numerically) | [other: height-localized Hermite–Gauss Gram of the complete form] | `04-papers/07-…/main.tex:244` |
| 3 | Truncation floor `η(X)\le Ae^{−α(\log X)^2}`, `α\approx σ^2/8`, PNT only; local-arithmetic stability of `Q(L)`, `λ_{min}`. | PROVED | [other: localized Gram] | `07/main.tex:305`; `09/main.tex:147` |
| 4 | Detector theorem (fixed off-line zero detected unconditionally beyond `X_{min}`). | PROVED | [other: localized] | `07/main.tex:347` |
| 5 | Uniform transfer `\sup_{X\ge X_0}|λ_{min}(Q_X)−λ_{min}(Q_∞)|\to0` ⟺ RH. | EQUIV | [other: localized → compl] | `07/main.tex:402–433` |
| 6 | `\mathfrak t=E^*JE`, `(Jc)_ρ=c_{1−\barρ}`, `J=J^*`, `J^2=I`; negative directions of `J` = off-line swap pairs; exact split `\mathfrak t=\|P_+EF\|^2−\|P_−EF\|^2`. | PROVED (unconditional) | [compl] via zero side, `T=d>\frac12` | `phase-4-handoff/B3-KREIN-STRUCTURE.md` §§1–3; `08/main.tex:116` |
| 7 | `\|K\|\le1` ⟺ RH. | EQUIV | [compl] | `08/main.tex:116` |
| 8 | Zero-side no-go (Theorem C). | PROVED | [compl] | `08/main.tex:126` |
| 9 | Semibounded self-adjoint realization in the `\mathfrak t_+` norm, `\inf\mathrm{spec}\ge1−4C`. | PROVED modulo (H) (CONDITIONAL) | [compl], `\mathfrak t_+`-norm | `08/main.tex:109`; `B2-THEOREM.md` §5 |
| 10 | Lemmas A–D: IBP `E_g=−\int g'S`; quadrature error `O(ρ\|F\|^2)`; vertical `\|F(\cdot+ib)\|^2\le e^{2d|b|}\|F\|^2`; off-line sum `\widetilde{\mathfrak t}_-\le C_dρ\|F\|_2^2` (Plancherel–Pólya). | PROVED | [other: `PW_d`] | `B2-THEOREM.md` §§1–4 |
| 11 | Parity `κ\equiv0\pmod2`, `κ=2m`, `\mathcal N\cong\bigoplus_j\mathbb R^{1,1}_j`. | PROVED (given the Pontryagin realization; see §0.3) | [compl], full test space | `phase-21-negative-directions-geometry/01-parity-and-geometry.md:42–150` |
| 12 | Under Hyp. D: `ξ=ξ_0P_{4m}`, `ψ=ψ_0−D_m`, `S_2\gg e^{2b_jT}/T`. | PROVED, CONDITIONAL (Hyp. D) | [other: prime counting] | `phase-21-negative-directions-geometry/02-…` Thm 21-D.1; `phase-22-pontryagin-finite-defect/01-…` Thm 22-A; `phase-23-two-scale-defect-structure/02-…` |
| 13 | Local prime form `G_p` indefinite (closed form above). | PROVED | [other: per-prime piece of `W`] | `phase-6-osterwalder-schrader-reflection/M-OS-2-S2-local-REFUTATION.md` §1 |
| 14 | Lyapunov identity for the dBN Coulomb dynamics; N5 arithmetic blindness. | PROVED (finite configurations) | [other: dBN] | `13/main.tex:105,150` |
| 15 | Off-line height bound `|\mathrm{Im}|\le\sqrt{2Λ}` (`Λ\ge b_j^2/2`). | PROVED for the isolated-pair model; for ζ stated under Hyp. D only | [other: dBN] | `13/main.tex:128`; `phase-25-lower-bounds-bj-audit/02-deBruijn-Newman.md` |
| 16 | Real-rootedness ⟺ Hermite form PSD; shift preserver arithmetic-blind. | CITED / PROVED | [other: Jensen] | `14/main.tex:178,189` |
| 17 | Anatomy identity `λ_{min}=R_∞−\sum_pR_p`; Hellmann–Feynman gradient; concavity + coordinatewise monotonicity in `Λ_n\ge0` (positivity over a box ⟸ positivity at the corner, `ζ^2`-point for `[0,2]`). | PROVED | [other: localized] | `09/main.tex:113,129,182`; `10/main.tex:289` |
| 18 | Carleson/Bessel reformulation of local positivity; finite Carleson constant unconditional. | EQUIV / PROVED | [other: localized] | `10/main.tex:256,269` |
| 19 | Euler product ⟺ factorizing anatomy; Satake recovery; RS multiplicativity. | PROVED (RH-independent, sign-irrelevant) | [other] | `10/main.tex:132–423` |
| 20 | No Frobenius periodicity of `\{γ_n\}` under LI. | PROVED, CONDITIONAL (LI) | [other] | `06/main.tex:257` |
| 21 | Finite-to-full criterion; uniform Hermite convergence strictly stronger than RH; **HR stability**: a convergent HR tower has uniform HR iff the limit form is strictly definite. | PROVED (finite-dim common model) | [other: towers] | `15/main.tex:93,165,203` |
| 22 | Modular-surface resonance pairing definite for every configuration. | PROVED | [other: SL₂(ℤ)\ℍ] | `phase-16-surf-witness-variety/05-…:12–31` |
| 23 | `\mathrm{Re}\,ξ'/ξ=0` on `σ=\frac12` (FE); RH ⟺ `ξ'/ξ` Herglotz on `σ>\frac12`; `m(z)=\frac1i\frac{ξ'}{ξ}(\frac12+iz)` has poles at `γ_ρ`, residues `+1`. | PROVED / EQUIV | [other] | `phase-16-surf-witness-variety/08-…`, `09-…` |
| 24 | Real-structure involution is a symmetry, not a positivity. | PROVED (elementary) | [other] | `phase-17-surf-2-design/04-…` §1 |
| 25 | Sector decomposition `G_{poly}`, `G_Γ` of `G(t)`; control of `G_ζ` ⟺ RH. | PROVED / EQUIV (sign audit pending) | [other] | `phase-28-four-fronts/08-…` |
| 26 | `dν=dm_{full}−dm_{full,on}\ge0` pointwise (Hadamard product). | PROVED | [other: CCM measures] | `phase-33-dbn/83-…` §1 |
| 27 | Repaired trace criterion: RH ⟺ `\int κ_n\,dν=0\ ∀n\ge0`, `κ_n=(a_n^∞)^2(|\mathcal P_{n+1}|^2−|\mathcal P_n|^2)` (Hamburger/Carleman rigidity). The literal λ-form is OPEN (block coincidences under ¬RH). | EQUIV (PROVED) / OPEN | [other: CCM] | `phase-38-final-audit/118-…:14` and §5.6 |
| 28 | Amplification skeleton: `κ(ψ^{⊠k})\ge kκ(ψ)` and `\le f(k)=o(k)` ⇒ `κ(ψ)=0`; `\mathrm{neg.ind}(Q_1⊗Q_2)=p_1q_2+q_1p_2`. | PROVED (audited 117) | [other: abstract] | `phase-36-ABC-forms/106-…:160`; `phase-38-final-audit/117-…` |
| 29 | `\mathcal W_2` (two-variable Weil form, kernel `g(x_1x_2)φ(x_1/x_2)`) is well-defined; arithmetic side autonomous (`Λ\starΛ`); toy signature (8,8). | PROVED | [other: two-variable] | `phase-36-ABC-forms/107-…` §§2–5 |
| 30 | Sub-resolution blindness: fixed support, height `\to∞` ⇒ the form is positive definite on those tests (`AA\sim c(\log T)^2` dominates). Windowed index binary. | PROVED (per doc) | [other: two-variable `Q_2`; one-variable analogue by eq:A] | `phase-36-ABC-forms/108-…` Thm 3.3, Prop. 2.5 |
| 31 | RH ⟺ `\mathrm{sf}\{A_λ\}=0` (Euler filtration, primes enter at `λ=\sqrt p`); finite a-priori rank ⇒ inertia autonomous (Newton). | EQUIV / PROVED (abstract) | [other: semilocal CCM] | `phase-37-physics/110-…` Thm 3.2, Prop. 4.5 |
| 32 | LP-112 ⇒ `m∈\{0,∞\}`; under H(m) Rouché-good shifts have upper density 0. | PROVED (survives audit with corrections) | [other] | `phase-37-physics/112-…` Thm 2.3, Prop. 2.6; `phase-38-final-audit/115-…` |
| 33 | ζ is not Stepanov almost periodic in any sub-band of the strip (band/vector version). | PROVED (survives audit) | [other] | `phase-37-physics/113-…` §5.2; `phase-38-final-audit/116-…` |
| 34 | In the class ℰ (entire, order 1, FE, real) there are members with exactly `m` quadruples for every finite `m`: any "`m\ge1⇒m=∞`" theorem must use the Euler product. | PROVED | [other] | `phase-37-physics/111-…` Prop. 2.2 |
| 35 | Exhaustion `κ(Q)=\lim_nκ(Q|_{\mathcal D_n})`; `μ_{\{∞\}}=0` (Weil positivity at autocorrelation support `(1/2,2)`). | PROVED / CITED (Yoshida 1992; Connes–Consani 2021) | [compl], `T\le\frac12\log2` | `phase-35-five-fronts/100-…` §§3–4 |
| 36 | Closed form `B_{λ_0}(r)=\frac{(\cosh r)^{-1/2}}8(5−78\,\mathrm{sech}^2r+105\,\mathrm{sech}^4r)`; per-prime sign change `p\ge11`; `−\frac{5\sqrt2}8\log` divergence. | PROVED | [other: CCM trace, minimal window] | `phase-36-ABC-forms/105-…` §5 |
| 37 | Absorption theorem (toy quadruple). | PROVED (toy model) | [other: variational] | `phase-35-five-fronts/98-…` §§4–5 |
| 38 | `k(u)>0\ ∀u>0` (Weil kernel); `k_λ\ge0` for `λ\ge λ_0`; even-simplicity H1 for `λ\ge λ_0(N)`. | PROVED per memo (not independently audited) | [other: CCM] | `phase-29-zeta-spectral-triples/04-…:43,103`; `phase-29-zeta-spectral-triples/01-…:45` |
| 39 | CC Serre duality = Pontryagin duality; self-dual `D_0=−\{2\}`, `χ(D_0)=0`, spaces 0. | CITED (arXiv:2205.01391) + PROVED computation | [other] | `phase-40-close-G1/122-…` |
| 40 | Phase 15 M1: explicit formula as a Lefschetz trace; effectivity `Γ\cdotΓ=\int_{-2d}^{2d}|S|^2\ge0`; M2 ample part `2(\int fe^{−u/2})^2\ge0`; Prop. C: RH ⟺ pairing ⪰ 0 on the primitive part. | PROVED / EQUIV | [prim] (primitive part = `P_T`; ample = polar term) | `phase-15-arithmetic-hodge-index/SYNTHESIS-M1-to-M3-and-the-precise-gap.md` Part A |

### 3b Open leads never closed negatively (in scope)
| lead | statement | status | file |
|---|---|---|---|
| (H) | uniform local sparsity of deep off-line zeros in every Nyquist cell | OPEN, ≪ RH, not known unconditionally | `phase-4-handoff/PAPER-A.md:281` |
| Diana L8 | any unconditional bound `m\le C` | OPEN ("unreachable with catalogued techniques", not proved impossible) | `phase-37-physics/111-…` |
| Lemma 108 | `κ_W(Q_2)\le C\,n_W` | OPEN, explicitly not RH-equivalent | `phase-36-ABC-forms/108-…` §8.1 |
| C_B / EX / D-109 | `m<∞⇒m=0` | OPEN | `phase-34-new-directions/94-…` §11; `phase-21-negative-directions-geometry/02-…`; `phase-37-physics/109-…` §4 |
| C5 ⇒ `κ<∞` | tail bound achievable; Kreĭn–Langer deduction missing | OPEN | `phase-34-new-directions/91-…`, `94-…` Part 1 |
| LP-112 | a sequence `τ_k\to∞` with `ζ(s+iτ_k)\toζ(s)` on a fixed compact disc | OPEN ("sin precedente"; non-RH-equivalence asserted, not proved) | `phase-37-physics/112-…`, `113-…`; `phase-38-final-audit/115-…` |
| 0A2 Part II | self-adjoint bounded-below realization + form-completeness without RH | OPEN (not RH) | `phase-0-foundations/0A2-connes-compression.md` §2 |
| NG-D4 | `Q(f,g)+Q(\hat f,\hat g)=0` (Fourier anticommutation) | OPEN, never attacked | `phase-28-four-fronts/02-front-B.md` |
| Doc 96 angles 1, 3 | twisted (absorbing-channel) characteristic function; symplectic/Maslov curvature | not obturated in principle | `phase-34-new-directions/96-…` summary |
| Doc 99 E1+E2 | even-simplicity of `QW_λ` + internal limit | OPEN sub-route | `phase-35-five-fronts/99-…` verdict |
| Doc 107 Lemma 5.2 | analytic realization of the tensor square | OPEN | `phase-36-ABC-forms/107-…` |
| Doc 121/123 cross B | Čech complex of the square as Γ-𝕊-modules with tolerance (technical) + functorial rank on the square (conceptual) | OPEN | `phase-39-…/121-…`; `phase-40-…/123-…` §6 |
| Doc 122 request | a natural self-pairing `H^1(D_0)\cong\widehat{H^1(D_0)}` | OPEN | `phase-40-…/122-…` §5 |
| additive energy | sharp high-order additive energy of `\{\log p\}` (moment frontier) | OPEN (not RH) | `00-MAP.md` Part 6; `phase-12-meta-obstruction-moment-problem/M12.9-…` |
| Conj. 100.A | see §5 I2 — superseded | resolved later | `phase-35-five-fronts/100-…:316` |

---

## §4 State of rows A, B, C, D as seen from this scope

Rows (a)–(d) are named only from phase 107 on; phases 0–40 contain their pre-images.

* **Row A (the space).** Pre-image: the SURF witness variety (`phase-16-surf-witness-variety/00-SURF-SPEC-SHEET.md`: four pillars,
  independence filter "zeros must be output, not input") and G1 (cohomology of the square;
  `phase-39-…/119-…`, `121-…`). State in scope: **no space**. CC's scaling-site Riemann–Roch has real-valued
  `χ(D)=\deg D` (`phase-15-arithmetic-hodge-index/M9-discovery-run-1-assessment.md`, Discovery 1; `THE_BACKWARD_MAP.md` §4: curve-like
  `Θ(\deg D)`, the quadratic growth of a surface is missing); tolerance gives a cokernel but not a rank on the square
  (`123` §3). Premise 1 (rows A–C WEIL-STRENGTH-COMPLETE on the declared carrier) is outside this scope; nothing here
  contradicts it.
* **Row B (correspondences).** Pre-image: phase 15 M1 "Frobenius-graph class Γ" — a functional, not a cycle; doc 106
  §3.3: CC correspondences `Ψ(λ)` form a multiplicative monoid of isometries (they preserve `κ`, they cannot
  amplify). State in scope: identities only.
* **Row C (pairing = explicit formula as Lefschetz trace).** Pre-image: phase 15 M1 Theorem A (trace identity,
  verified to `10^{-12}`, numerical check), M2 ample cone; doc 121 grades R-LEF-POLO and R-LEF-PRIMOS as TECHNICAL
  (the identity exists, the carrier does not), R-LEF-REG as TECHNICAL with a divergent `2h(1)\log λ` term pending.
* **Row D (the sign).** In scope: Phase 15 Prop. C — RH ⟺ positivity on the primitive part — EQUIV [prim]; all eight
  attempts on M3 fail (§2.5 items 24–28); doc 121: "G2: nobody has a signature anywhere"; doc 124: the only
  sign-carrying positivity in the CC corpus is spectral Weil positivity (RH-equivalent when globalized). **Signs
  actually proved in scope:** only the archimedean window, `μ_{\{∞\}}=0`, i.e. [compl] for `T\le\frac12\log2`
  (CITED, Yoshida 1992 / CC 2021; `100-…` §4). Conjecture 100.A ([prim] at `T=\frac12\log3`) was open then; it is
  now covered by Paper 42 ([prim], `T\le\log2`) and by Zhu ([compl], `T\le0.8`) per the premises of record (§5 I2).
  **Nothing in scope bears on `T>0.8`.** The obstruction named for the passage to all windows is O_SL: the
  non-uniformity in the window index of the operator control of the Weil–Sonine discrepancy, with the `\sqrt n`
  versus `\log n` barrier reappearing window by window (`100-…` §5; `91-…` Prop. 4.5). This is consistent with, and
  an early form of, the phase-159 walls and Theorem M.

---

## §5 Ideas started but never finished, or closed for a reason later removed

Each is a potential ingredient, tagged with the memo(s) it concerns. None is a proof step as it stands.

* **I1 — OS positivity, archimedean half now available [B3, B4].** Phase 6 closed OS because (i) the per-prime form is
  indefinite and (ii) the two-point function is oscillatory. Paper 46 later proved (CITED, `thm:S`, `eq:A`,
  `main.tex:160–167`) that `m(τ)=C_0+\int_0^∞(1−\cos τu)K(u)du` with `K` completely monotone: the archimedean part is
  a Lévy energy of a subordinated Brownian motion — an OS-decaying, reflection-positive structure. What remains
  closed is only the product-over-primes version (item 1 of §2). A non-product (entangled) Euclidean model whose OS
  form is the whole `W_T` was never attempted. (B3 must still meet phase-159 walls on product/covariant carriers.)
* **I2 — The filtration picture and Conjecture 100.A [B1, B20].** Doc 100 reformulated the adelic Maslov index as
  window increments `μ(n)=0` (`C_D^{SL}`), proved the exhaustion lemma and the base case, and posed 100.A: for
  `g\in C_c^∞(\mathbb R_+^*)`, `\mathrm{supp}\,g\subset(3^{-1/2},3^{1/2})`, `\hat g(0)=\hat g(1)=0`,
  `W_∞(g*g^*)\ge\frac{\log2}{\sqrt2}[(g\star\tilde g)(2)+(g\star\tilde g)(1/2)]` (`100-…:316–318`). In window terms this
  is [prim] at `T=\frac12\log3` (only contact `n=2`). The reason it was open is **removed**: Paper 42 proves [prim]
  for `T\le\log2`, Zhu [compl] for `T\le0.8` (premise 1). Reusable residue: Programme 100.B (Sonine compression in
  `L^2(X_{\{∞,2\}})` with weight `|L_2L_∞|^2`, compact discrepancy, Toeplitz defect, `100-…:328–336`) is a test of
  whether the CC *mechanism* reproduces a sign that is now known — a calibration, not a new sign.
  (Memo must check the dictionary `g\leftrightarrow F`, `F(t)=e^{t/2}g(e^t)`, against `P_T` before citing.)
* **I3 — Spectral flow of the Euler filtration [B1, B20, B15].** `RH ⟺ \mathrm{sf}\{A_λ\}=0` with primes entering one
  at a time and each crossing an individual event at a finite `λ_0` (`110` Thm 3.2). Unfinished: nothing locates the
  crossing without the zero; CF steps give zero flow; the limit is MW-6.
* **I4 — Finiteness axiom L6 / R-FIN [B2, B5, B6, B17].** `110` Prop. 4.5–Cor. 4.6 and `119` R-FIN: inertia is
  autonomous exactly when it factors through an a-priori finite-dimensional object with arithmetic traces (Newton).
  Tension a memo must resolve: Paper 46 `thm:finZ` (CITED; no finite zero set carries a flat-top certificate;
  row D is intrinsically infinite). R-FIN asks for finiteness of the *impure* part only, which `thm:finZ` does not
  exclude.
* **I5 — HR stability at the degenerate limit [B14, B15, B19].** Paper 15 `thm:hr`: uniform positivity of a tower ⟺
  strictly definite limit. By Theorem M (premise 2, `λ^A_T\le\exp(−e^{(2−ε)T})`) the relevant limit gap is 0, so any
  tower/compactness argument must certify sign **without** a uniform gap. The criterion (`thm:crit` case 2, "bounded
  threshold") is the exact format such an argument would have to beat.
* **I6 — Sub-resolution blindness [B13, B15].** `108` Thm 3.3 (and, for one variable, the Lévy energy `\log(2+|τ|)`
  in `eq:A`): at a fixed window the high-frequency part is positive in both worlds; negativity lives in a
  low-frequency block. Unfinished: a quantitative statement "`W_T` can fail only on a block of dimension `\le n(T)`"
  with explicit `n(T)` from arithmetic data was not written in scope.
* **I7 — The two-variable Weil form `\mathcal W_2` [B12, B8].** `107`: the prime×prime block is a transform of
  `Λ\starΛ` entering with **plus** sign, arithmetic side autonomous; the thickened diagonal kernel produces the
  Minkowski sum `(\rho_1+\rho_2)/2`. Only the sieve bridge (`108`) was killed; `\mathcal W_2` as a positivity object
  (Schur/Hadamard-type, multiplicative) was never finished (Lemma 5.2 open).
* **I8 — Amplification with finiteness [B8].** `106` Thm 1.4 is valid; it failed only for lack of (a) a non-circular
  superadditive `⊠` and (b) a sublinear bound. Doc 110 Obs. 5.3 names the missing piece (R-FIN). Any
  tensor-power/field-tower memo must supply (b) from outside the Weil form (C3 in `106:177–185`).
* **I9 — The phase-6-osterwalder-schrader-reflection pointwise reduction, repaired [B11, B16, B20].** NG-E6 killed "envelope ≥ comb pointwise"
  because the comb is distributional. Paper 46 `thm:Z` (CITED, `main.tex:1219–1252`) is the rigorous smoothed version:
  with `w\in\mathcal W_T`, `f_w=σ_T+\widehat{ν_w}+2\widehat g_0` equals `\sum_ρ\widehat w(τ−γ_ρ)` and `W_T\ge\inf f_w`;
  RH ⟺ one-sided smoothing for all `T`. The objection of phase 6 is removed; the sign content is unchanged (it is
  the zero measure again).
* **I10 — What a scattering/Maass–Selberg memo must change [B9, B10].** `phase-16-surf-witness-variety/05` proves every resonance
  pairing on `SL_2(\mathbb Z)\backslash\mathbb H` is definite, because Petersson is Riemannian (half-plane Hardy kernel);
  `phase-16-surf-witness-variety/06` states the principle: an RH-carrying form needs an intrinsically indefinite (Lorentzian/Kreĭn)
  geometry; the indefinite term is the off-axis evaluation `4\mathrm{Re}[\hat f(t−ib)^2]`, unbounded on `L^2`. Unitarity
  of a wave group alone reproduces the definite pairing.
* **I11 — Euler subspace and dissipative twists [B4, B18].** `96` Thm 2.12: the Euler subspace is `Q`-positive; its
  density is ⟺ RH. Angles 1 (absorbing channel twisting `Θ`) and 3 (symplectic curvature) were left "not obturated".
* **I12 — Rigidity by determinate moment problems [B14, B16].** `118` repaired a criterion using Carleman
  determinacy of `dm_∞` + `dν\ge0`: the only positive `ν` with `\int|\mathcal P_n|^2dν` constant is `c\,m_∞`. A
  genuine rigidity mechanism; it converts a positive measure plus equalities into vanishing. It needs *equalities*
  (a zero-side input), which is where it re-meets RH.
* **I13 — Replication mechanism (LP-112) [B15].** Under `m<∞`, one pointwise self-approximation on a fixed disc
  multiplies off-line zeros (Bohr–Rouché, constants frozen); ℚ-independence of `\{\log p\}` makes almost periods
  non-discrete (`112` Lemma 3.3). Ultralimit/compactness memos: the needed shift set has density 0 (Prop. 2.6), so
  it cannot come from a positive-density argument.
* **I14 — Self-dual divisor and the square [B2].** `D_0=−\{2\}` with `K−D_0=D_0`, `χ(D_0)=0` — the analogue of a theta
  characteristic — exists and is explicit (`121` cross A); the self-pairing does not (`122`). Technical core (a) of
  `123` §6 (Čech complex of `C_p\times C_p` with tolerance) was never executed.
* **I15 — Fourier anticommutation [B1].** The identity `Q(f,g)+Q(\hat f,\hat g)=0` (NG-D4) was stated and left open;
  it is the one place in scope where Fourier self-duality (Sonin/prolate territory) is posed as a sign mechanism.
* **I16 — Weight monotonicity [B12].** `λ_{min}` is concave and non-increasing in each prime weight (`10/main.tex:289`);
  Paper 46 notes any nonnegative weights may be used in (P)/(D) (`main.tex:550`). Comparison principles between
  weight vectors are therefore free; none gives the sign for `v_n=2Λ(n)/\sqrt n` by itself (the heavier corner is
  harder).
* **I17 — Mechanism-correct upper-bound chain [B11, B13].** Phase 12: `S(t)` log-correlated, derandomized as a prime
  sum, large sieve, additive energy of `\log p` (HEURISTIC; `M12.9` §2 states it is not a rigorous reduction). Never
  converted into a window statement.
* **I18 — Faithfulness Part II [B15].** 0A2 (II-a)/(II-b): pollution-free Galerkin convergence of the bottom without
  RH. Directly relevant to any Galerkin certificate at `T>0.8`; never proved in scope (v9 was a falsifier that did not
  fire, HEURISTIC).
* **I19 — CCM infrastructure for `λ\to∞` [B1].** `phase-29-zeta-spectral-triples/01` Thm 1 (even-simplicity for large `λ`), `04` Thms 0–1
  (kernel positivity), `99` Lemma 6.1 (CF stability), with the named gaps 6.2/6.5 and Lemma 5.1 (prime tail
  `\sim λ/\log λ`). Anything built on docs 63–103 must first be re-checked against the `W_λ` refutation (`114`).

---

## §6 Definitions a memo needs, verbatim (file:line)

**D1. Symbol, contacts, truncated form, Tate moments, primitive subspace, complete form, bottoms** —
`04-papers/46-row-d-sign-radial-intersection-form/main.tex:115–147`:
> Throughout, $T>0$, $\IT=(-T,T)$, and for $F\in L^2(\IT)$ (extended by zero) we write
> $\Fh(\tau)=\int F(t)e^{i\tau t}\,dt$ and $\cF(u)=\int F(t)\overline{F(t-u)}\,dt$ for the autocorrelation […]
> $m(\tau)=\Rel\psi\!\left(\tfrac14+\tfrac{i\tau}{2}\right)-\log\pi,\qquad
> \sT(\tau)=m(\tau)-\sum_{n\in\NT}v_n\cos(\tau\log n),\qquad v_n=\frac{2\Lambda(n)}{\sqrt n}$,
> where $\NT=\{n\ge2:\ \log n<2T\}$ is the set of \emph{contacts} […] The truncated Weil form is
> $\mathfrak a_T(F)=\frac1{2\pi}\int_\R\sT(\tau)\,|\Fh(\tau)|^2\,d\tau$ […] it is the quadratic form of the operator
> $A_T$ of \cite{Paper42} […] The two \emph{Tate moments} are $A(F)=\int F(t)e^{t/2}dt$ and $B(F)=\int F(t)e^{-t/2}dt$,
> and the \emph{primitive subspace} is $\PT=\{F\in L^2(\IT):A(F)=B(F)=0\}$. The \emph{complete Weil form} on the
> window is $W_T(F)=\mathfrak a_T(F)+2\,\Rel\big(A(F)\overline{B(F)}\big)$ (eq:W) […]
> Write $\lamA$ for the bottom of $\mathfrak a_T$ on the unit sphere of $\PT$ and $\lamW$ for that of $W_T$ on the
> unit sphere of $L^2(\IT)$; $\lamW\le\lamA$ since the two forms agree on $\PT$.

(`\lamA=\lambda_{\min}(A_T|\mathcal P_T)`, `\lamW=\lambda^{\mathrm W}_T`, macros at `main.tex:20–21`.)

**D2. Lévy form** — `main.tex:165–167` (eq:A):
> $\mathfrak a_T(F)=C_0\|F\|^2+\int_0^\infty\big(\|F\|^2-\cF(u)\big)K(u)\,du-\sum_{n\in\NT}v_n\cF(\log n)$,
> with $C_0=\psi(\frac14)-\log\pi$ and $K(u)=\frac12/\sinh(u/2)+\frac12/\cosh(u/2)$ (`main.tex:160–162`).

**D3. Primal and dual** — `main.tex:553–559` (def:PD):
> \textbf{(P)} $\lamP=\inf\big\{\int_\R\sT\,d\mu:\ \mu$ an even probability measure on $\R$, $\check\mu(u)=0$ for
> $|u|\ge2T$, $\int\gh0\,d\mu=\int\gh1\,d\mu=0\big\}$.
> \textbf{(D)} $D_T=\sup\big\{\inf_{\tau\in\R}\big[\sT(\tau)+\nuh(\tau)+\beta_0\gh0(\tau)+\beta_1\gh1(\tau)\big]:\ \nu$ a
> finite even signed Borel measure with $\supp\nu\subseteq\{|u|\ge2T\}$, $\beta\in\R^2\big\}$. A triple
> $(\nu,\beta_0,\beta_1)$ with $f:=\sT+\nuh+\beta\cdot\widehat g\ge c$ on $\R$ is a \emph{certificate of value $c$}.

**D4. Flat-top weights and `ν_w`** — `main.tex:1219–1226` (def:W, eq:nuw):
> $\Wcl$ is the set of even measurable $w:\R\to\R$ with $w\equiv1$ on $[-2T,2T]$ and $|w(u)|\le Ce^{-(\frac12+\delta)|u|}$
> for $|u|\ge2T$, for some $C,\delta>0$. […] For $w\in\Wcl$ define the even measure
> $d\nu_w=\Big[\tfrac12\big(1-w(u)\big)K(|u|)+2w(u)\cosh\tfrac u2\Big]\mathbf 1_{|u|\ge2T}\,du
> -\sum_{n\notin\NT}\tfrac{v_n}2\,w(\log n)\,\big(\delta_{\log n}+\delta_{-\log n}\big)$, and $f_w:=\sT+\nuh_w+2\gh0$.

**D5. On/off decomposition of the Weil form on `PW_d`** — `03-research/phase-4-handoff/B2-THEOREM.md:31–34`:
> Writing $b_\rho=\beta_\rho-\tfrac12$,
> $\mathfrak t(F)=\underbrace{\sum_{\beta_\rho=1/2}|F(\gamma_\rho)|^2}_{\mathfrak t_+(F)\ \ge0}\ +\ \underbrace{\sum_{\text{off-line quartets}}4\,\mathrm{Re}\big[F(t_\rho-ib_\rho)^2\big]}_{\mathfrak t_-(F)\ \text{indefinite}}$.

**D6. Kreĭn fundamental symmetry** — `03-research/phase-4-handoff/B3-KREIN-STRUCTURE.md:22–31`:
> The correct object is the **linear involution** induced by the partner map $\sigma$:
> $(Jc)_\rho:=c_{\sigma(\rho)},\qquad \sigma(\rho)=1-\bar\rho$. Then $J^2=I$, $J=J^*$ […]
> $\langle EF,\,JEF\rangle=\sum_\rho F(t_\rho+ib_\rho)\,\overline{F(t_\rho-ib_\rho)}=\mathfrak t(F)$.

**D7. Hypothesis (H)** — `03-research/phase-4-handoff/PAPER-A.md:281–286`:
> **Definition 4.2 — Hypothesis (H) (uniform local sparsity of deep off-line zeros).** There exist $\delta>0$,
> $\eta>0$, $T_0$ such that for all $T\ge T_0$ and every interval $I$ of length $1/d$ centred at height $T$,
> $\#\{\rho:\ |b_\rho|<\delta,\ t_\rho\in I\}\ \ge\ \eta\,\rho(T)\,|I|$.

**D8. Uniform transfer (the "single missing inequality" of Paper 07)** — `04-papers/07-localized-weil-form-hermite-gauss/main.tex:411–413`:
> $\sup_{X\ge X_0}\bigl|\lmin(Q_X)-\lmin(Q_\infty)\bigr|\ \le\ \varepsilon(X_0)\xrightarrow[X_0\to\infty]{}0$.

**D9. Band-limited Weil–Carleson constant** — `04-papers/12-band-limited-weil-carleson/main.tex:124`
(read with §0.2: polar term dropped):
> $\Cband(d,T_0)\;:=\;\lambda_{\max}\!\big(\Pf,\Aphi\big),\qquad \mathrm{RH}\iff \Cband(d,T_0)\le 1\ \ \forall d,T_0.$

**D10. Prime-tail relative form bound** — `04-papers/11-offline-zeros-pontryagin-index/main.tex:94–100`:
> If for some $X$ the tail satisfies the relative form bound
> $\bigl|\fp_{>X}[g]\bigr|\le a\,\fa[g]+C\|g\|^2,\qquad a<1,$ (RFB$_X$) then $\ft$ has finitely many negative
> squares, $\kappa<\infty$.

**D11. Parity** — `03-research/phase-21-negative-directions-geometry/01-parity-and-geometry.md:42–46`:
> **Theorem 21-A.1 (Parity of κ).** Let $\zeta$ be the Riemann zeta function, or any real primitive
> Dirichlet L-function $L(s,\chi)$ with $\chi$ real. Then: $\kappa(Q) \equiv 0 \pmod{2}$.

**D12. Inertia reader and the class ℱ** — `03-research/phase-37-physics/110-invariants-that-count-modes-one-by-one.md:420–443, 455–466`:
> **(L1) Quantization.** I takes values in ℤ […] **(L2) Autonomy of the value.** I is computable from the
> unconditional arithmetic data — primes, pole, gamma factor — WITHOUT the positions of the zeros […] **(L3) Inertia
> detection.** I = 0 ⟺ m = 0 […] **(L4) Stability under computation.** […] WITHOUT an RH-equivalent uniformity […]
> **(L5) Localization.** I satisfies an index theorem […] **(L6) A priori finiteness.** I factors through an object
> of finite dimension, bounded by arithmetic data (NOT by zero positions), with arithmetically
> computable traces on that object.
> **Definition 4.2 (class ℱ …).** ℱ consists of the invariants of the form I = neg.ind(Q|_{V′}), where: (i) Q is a
> Hermitian form […] with an explicit-formula-type identity […] (ii) V′ ⊆ 𝒱 is **test-accessible**:
> specified without zero positions (by supports, frequency windows, norms).

**D13. Forced axioms for a cohomology over the square** — `03-research/phase-39-G1G2-interface/119-forced-axioms-backward-derivation.md:22–27`:
> **R-SIG**: $H$ carries a weight grading with an associated integer signature […] **R-FIN**: the
> *impure* weight part of $H^1$ has finite dimension bounded a priori by site data, and that dimension bounds
> $\kappa(Q)=2m$ […] **R-LEF**: a flow $F$ on $H$ whose distributional trace reproduces term by term the
> explicit formula […] **R-PESO**: the weight invariant of each class is computable from $H$, not from the
> position of the zero; "weights $=1/2$" must FOLLOW from a geometric positivity […] **R-NC**: a
> non-circularity test in four clauses (NC1–NC4) […] **R-TRZ**: the traces are evaluable against a class of tests
> with strict margin $\varepsilon$ within the Weil class.

**D14. Abstract amplification** — `03-research/phase-36-ABC-forms/106-amplifier-functor-systematic-search.md:160–163`:
> **Theorem 1.4 (Abstract amplification).** Let $(\mathcal{C}, \boxtimes, \kappa, \mathcal{F})$ be an amplification
> datum satisfying (a) and (b). Then for every $\psi \in \mathcal{C}$ such that
> $\psi^{\boxtimes k} \in \mathcal{F}$ for all $k \geq 1$: $\kappa(\psi) = 0$.
> [(a) $\kappa(\psi^{\boxtimes k})\ge k\kappa(\psi)$; (b) $\kappa(\psi^{\boxtimes k})\le f(k)$, $f(k)/k\to0$; `106:17–21`.]

**D15. HR tower and HR stability** — `04-papers/15-eventual-versus-uniform-positivity/main.tex:191–215`:
> A \emph{Hodge--Riemann tower} is a sequence $(V_m,L_m,Q_m)$ […] with the Hodge--Riemann property
> $(-1)^jQ_m|_{P_m^j}>0$. Set the \emph{HR gap} $\delta_m=\inf_{j}\inf_{\|v\|=1,\,v\in P_m^j}(-1)^jQ_m(v,v)$ […]
> \textbf{Theorem (HR stability).} […] If $\delta_\infty>0$ […] the tower has \emph{uniform Hodge--Riemann} […]
> If $\delta_\infty=0$ […] uniform HR fails: $\inf_m\delta_m=0$.

**D16. Resonance pairing** — `03-research/phase-16-surf-witness-variety/05-resonance-pairing-definite-THEOREM.md:12–19`:
> Let the modular-surface resonances be $s_\rho=\rho/2$ […] The resonance kernel
> $K_{\rho\sigma}=\frac{1}{s_\rho+\overline{s_\sigma}-1}$ […] is **negative-definite** for every such configuration —
> on-line or off-line.

**D17. Repaired CCM trace criterion** — `03-research/phase-38-final-audit/118-repair-of-the-trace-criterion-moment-rigidity.md:14`:
> $\text{RH}\iff \int_{\mathbb{R}}\kappa_n(s)\,d\nu(s)=0\ \ \text{for all } n\geq 0$
> [with $\kappa_n=(a_n^\infty)^2(|\mathcal{P}_{n+1}|^2-|\mathcal{P}_n|^2)$, $d\nu=dm_{\rm full}-dm_{\rm full,on}\geq0$; `118:15`].

**D18. Conjecture 100.A** (now superseded, §5 I2) — `03-research/phase-35-five-fronts/100-maslov-semilocal.md:316–318`:
> For every $g \in C_c^\infty(\mathbb{R}^*_+)$ with $\mathrm{supp}(g) \subset (3^{-1/2}, 3^{1/2})$ and
> $\hat g(0) = \hat g(1) = 0$ (Mellin at the poles), one has
> $W_\infty(g * g^*) \;\geq\; \frac{\log 2}{\sqrt{2}} \Big[ (g \star \tilde g)(2) + (g \star \tilde g)(1/2) \Big]$.

---

## Appendix — memo cross-index (must-read files in this scope, by angle)

| memo | read first |
|---|---|
| B1 Connes (prolate, Sonin, λ→∞) | `phase-5-structural/B2-semilocal-residual.md`; `phase-7-weil-carleson-sine-kernel/connes/P7c-…`; Paper 12 §prolate; `phase-35-five-fronts/99-…`, `100-…`; `phase-40-close-G1/124-…`; §5 I2, I3, I15, I19 |
| B2 Consani (RR over 𝕊) | `phase-39-…/120-…`, `121-…`; `phase-40-…/122-…`, `123-…`; `phase-15-arithmetic-hodge-index/M9-…` (χ = deg D ∈ ℝ); §5 I4, I14 |
| B3 Jaffe (OS) | `phase-6-osterwalder-schrader-reflection/*` (all four); §5 I1 |
| B4 Haagerup/Popa | `phase-34-…/96-…`; §5 I1, I11 (Tomita–Takesaki orientation no-go is doc 161, phase 51, outside S1) |
| B5 Scholze | `phase-15-arithmetic-hodge-index/M6-…`; `phase-16-surf-witness-variety/01-…` (prismatic rejected at Pillar 1); `AUDIT_A_CATEGORY_CHANGES.md` §3 (condensed untried) |
| B6 Bost / B7 Zhang | `phase-15-arithmetic-hodge-index/M3-attempt5-…`, `M3-attempt6-…`, `M10-…` (Hodge index controls heights) |
| B8 Deligne/Katz | `phase-36-…/106-…` (Thm 1.4, Prop 3.9, §3.2.4), `107-…`, `117` audit; `phase-30-langlands-bridge-c-infinity/55-…`, `56-…`; `110` Obs 5.3; §5 I7, I8 |
| B9 Sarnak / B10 Iwaniec | `phase-16-surf-witness-variety/02-…`–`06-…`; §5 I10 |
| B11 Tao (dBN) | Paper 13; `phase-8-heat-flow-monotonicity/*`; `phase-9-unconditional-universality/M9.1-…`; `phase-25-lower-bounds-bj-audit/02-…`; §5 I9, I17 |
| B12 Tao (Schur/Hadamard) | `106-…` §3.1 (tensor index), `107-…`; Paper 10 `thm:concave`; §5 I7, I16 |
| B13 Maynard | `108-…`; `phase-9-unconditional-universality/T9A-…`; Paper 11 remark after `prop:red`; `phase-4-handoff/proofs/Day19–22`; §5 I6 |
| B14 Ono | `phase-11-hyperbolicity-total-positivity/*`; Papers 06, 14, 15; §5 I5, I12 |
| B15 Green | Paper 15 `thm:hr`; Paper 11; `phase-18-negative-directions-portrait/02-…`; `108` Thm 3.3; `112-…`; §5 I5, I6, I13, I18 |
| B16 Villani | `phase-28-four-fronts/05-…`, `06-…`; `phase-34-…/93-…`, `95-…`, `97-…`; `phase-35-…/98-…`; `phase-33-dbn/86-…` |
| B17 Lichtenbaum/Morin, B18 Morishita, B19 Huh | `119-…` (axioms), `121-…`; Paper 06 `thm:gap`, Paper 15 table (AHK scale-free vs ζ); `phase-11-hyperbolicity-total-positivity/*` (MSS) |
| B20 Connes (semilocal→global) | `100-…` (O_SL), `99-…`, `105-…`, `phase-34-…/91-…` Prop 4.5 (√n vs log n); §5 I2, I3, I9 |
