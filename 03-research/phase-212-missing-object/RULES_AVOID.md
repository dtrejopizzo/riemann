# Phase 212 — What is not done

Consolidation of the routes index (now incorporated in full in Part IV of `05-meta-and-planning/ROUTES-MASTER-INDEX.md`; cited «IDX»), the master
grid («GRID»), the crossword («CW»), Papers 47–48 («P47», «P48»), the memory of rejected
selections in the project rules and phase 211 («211/…»). It is a quick-reading guide and does not replace the
sources: before proposing anything one searches them and the full-reading annexes (§H), which
are the complete list; sections A–G are the summary. A closure is cited with its label
(PROVED / ARGUED); an exact reformulation is a valid target, not a closure
(IDX `AUDIT_PHASE193_CERTAINTY.md`).

## A. Hard rules

A1. **Sandbox.** (★) is the sign of an explicit quadratic form. No equivalence with another statement
    is named or used; there is no reduction to zeros; no argument «this is as hard as…».
A2. **Nothing in the index is retried**, neither renamed nor as a variant, without a written reason stating which
    hypothesis, object or method class changes and why that avoids the recorded reason for the failure.
A3. **Four-point filter before building**, verified by an independent review
    (README §4). Without the four points there are no derivations, computations or certificates.
A4. **Does not count as novelty:** another name, another notation, another parameter, another basis, another change of
    variable (Mellin, theta, powers, hyperbolic), another normalization, another dimension, «making it
    global / nonlinear» without an explicit operation, another auxiliary energy without a sign mechanism,
    reproducing an external result, going up one more finite order.
A5. **Mandatory falsifier battery** at every sign step (§E). If the argument survives
    any of them, it is wrong; say where.
A6. **No paper is touched.** No other phase is opened. No authors, dates, model names or
    process roles in the files.
A7. **No «honest closure» is proposed**, nor a chapter of barriers as an ending: barriers are
    tools.

## B. Ten failure patterns (if the candidate falls into one, it stops before deriving)

B1. **Identity valid for every comb.** It carries no sign (P47 lem:shape-ident, thm:shape (B″)).
    Examples: IDX README EI_001–003; Selberg-type identities NODE_001 Prop N.2; divisor gauge
    P47 thm:spec-gauge; strip identities P47 §strip.
B2. **Estimate with slack.** For T ≥ 1 the margin is ≤ 4·10⁹Te^{−15.449T} (and, CONDITIONAL on P47
    thm:ext-half and a cited bound, λ_A ≤ 3.2·10²³N^{33/2}e^{−2πN}, N = e^{2T}; 211/ROUND_009_A Cor 7.1).
    P47 thm:shape(B′)/lem:shape-est proves precision restrictions for deciding the sign in a
    fixed window; the general exclusion of estimates with remainder is labelled ARGUED, not PROVED.
    The exclusions of BARRIER_EST_001 keep their class hypotheses. This includes the limitations
    recorded for absolute-value bounds on ψ(y) − y, large sieve and mean square
    (P47 rem:wit-cheb). It does not apply to fixed blocks already signed with a certificate.
    **Scope:** B2 does not by itself exclude the route of P47 thm:wit-Tc(iv): a uniform lower bound
    λ_A(T_k) ≥ −ε_k, with T_k → ∞ and ε_k → 0, suffices even if ε_k exceeds the expected margin.
    Finding that bound remains OPEN. Also sufficient is an error that vanishes for each fixed test of
    a dense shape kernel, by freezing (ROUND_022_B, Lemma 1); it need not be made uniform
    over all tests for that pointwise argument. Controlling only selected tests
    does not suffice. These are already recorded reductions, not new mechanisms nor sign proofs.
B3. **Exact reformulation presented as progress.** It is a valid target, not a sign result. There are 43
    distinct reformulations recorded (IDX README, phase 204); a 44th is not added without a mechanism.
B4. **Positive model + transfer or comparison.** Excluded with proof, each one in its class:
    positive mixtures and convolutions with a finite positive measure of the hyperbolic model
    (211/HYPERBOLIC §7); matrix order of the scaling flow (§9); fixed prefactors, scalar or
    vector, with or without first derivative (§§10–12.4); exact representation by products of cosh
    (§§11, 13; it does not decide whether multiplying by cosh preserves positivity); comparison K_Φ ≥ εK_{2π}
    for every ε > 0; additive comparators Robin, asinh and 2π, also on primitives; every
    additive comparator D with D = o(1/u) and K_D positive semidefinite is zero; normalized or gauged
    generators, for every c and every a; real diagonal repair of the BPY comparison G1→G2 (any
    real diagonal factor, not only holomorphic); two transports from C_0 (pointwise multiplier,
    imaginary translations) and the quotient A/C_0; positivity imported from a uniform construction
    on the comb (P47 thm:noimport; IDX CPOS_CLASS_001).
    **Not excluded:** non-diagonal or triangular transfers (stopped at selection for lack of
    explicit coefficients, not for impossibility); geometric interpolation with a relative bound
    ∂_sK_{s,U} ≥ −C_U(s)K_{s,U}, C_U integrable, for each finite list U; other models and
    joint compensations; constructions that use the exact multiplicativity of Λ.
B5. **Class closed by finite modification, deletion or rescaling.** cor:void, a_P, cΛ, W-tail:
    sieves, progressions, cones over log ζ, coefficient-by-coefficient integrality, sparse-stable
    properties (P47 prop:spec (2)–(4)).
B6. **Holds for a model with functional equation and without Euler product** (Davenport–Heilbronn,
    Epstein x²+5y², f_t) **or with Euler product and without functional equation** (a_P).
B7. **Monoid only; blind to Beurling** (IDX phase 193 fronts G1, H; INV_K).
B8. **Bounded functional of the weights, local criterion on the symbol, pattern of observables, law on a
    bounded range of windows, determinant or moment of the pencil** (W-lin, W-det, W-fam, W-pat, W-loc,
    W-mom; P47 §barriers).
B9. **The sign remains in a functional of the minimizer** (IDX SPEC_A, BARRIER_W; P48 req:spec R10).
B10. **Wrong direction or only upper bounds** (W4). Concavity on the comb (Danskin) gives
     only upper bounds. Its dual representation Θ_T = max_c λ_A(T;cΛ) is PROVED
     (211/ROUND_002_D Thm 1) and only separates in tangency windows, where Θ_T = λ_A
     (ROUND_002_E Cor 4): status PIVOT, not open ground.

## C. Families already traversed (IDX README «Closed families» and catalogues 03–04)

Reading warning. «0 admissible» in the index means «no seed, as formulated,
passed the proved filters»; it does not mean impossibility. Only C1 is a prohibition. C2–C4 are not relaunched
as they were, but they are legitimate ground with the indicated change. The candidate-by-candidate
classification of phase 193 is in `ANNEX_PHASE_193_LABELS.md`, corrected in 22 points by the reading
of the 128 primary memos (`ANNEX_PHASE_193_PRIMARY.md`, which prevails where they differ).

### C1. Closed with an explicit falsifier or a PROVED class NO-GO

Statistics and numerical phenomenology · inverse spectral / Jacobi / Mercer · Li and Bochner kernels
in ordinates · heat flow, Laguerre–Pólya, Jensen · total positivity of order ≥ 5 (the kernel is not
PF₅; fails at PF₂ in 104_21) · Baker · Fredholm, determinants, Birman–Schwinger, Szegő–Widom ·
pure arithmetic SOS for T ≥ ½log3, positive exterior certificates · sieves, progressions,
short intervals · zero information · averages over characters · Sonin, prolates, semilocal as
a source of sign · coercivity, Schur, inertia, Wiener–Hopf, two Nyquist sectors as a source of
sign · Euler/Möbius algebra, operator partitions, cones · transport in σ, reflection,
conjugation · height flow at σ = 1 · invention set of phase 194 (Lévy/Hamburger,
pair surface, Farey/Möbius, Mp₂, Kronecker–Hurwitz, cones via ∂log, integrality, additive
inputs, pair correlation) · Petersson, Rankin–Selberg in the proved form, Maass–Selberg ·
Bost–Connes, Araki/Petz, NC-SOS · Selberg/Arthur traces · p-derivations, Stepanov, sum-product ·
Markov, maximum principle, virial/Pohozaev, Almgren · OS/checkerboard, GKS, FKG · Viazovska-type
constructions (what is constructible holds for Epstein) · arithmetic of prime sites (parity, residues, singular
series) · real stability / MSS, Bakry–Émery Γ₂, bootstrap, resurgence, band mixing ·
defect/continuation, Morse index, Kreĭn signature, integrality+FE tangent, Farkas {0,1} ·
L♯ programme (exterior form, Grönwall, Möbius sawtooth, passivity, boundary triples) · sign
object of phase 200 (OS on the boundary, Γ-limit, Fejér–Riesz, Cholesky, Q2 ladder, cuts, von Neumann
dimension, Loeb measures, Rankin f×f̄) · nonnegative rank, recurrence {x+y,xy}, imported
positivity · exterior table of phase 202 · chained E∧F composition and uniform continuous
mechanisms (phases 205–207) · phase 211: fixed-scale dominations, families of homogeneous words in (M,Π),
Carleman germ criteria, closures by cosh products, Laplace layer D_{2π}.

### C2. Only argued (the proof of the discard is missing; reopened with a written object)

Lewis–Zagier · archimedean liquid input · KMS · Lorentzian Hodge–Riemann · VOA and Soergel in monoid
form (they rest on conditional clauses of P47) · G1 monoid lemma / arithmetic derivative ·
Γ-convergence · Dobrushin/TAP · Cheeger · geometric Brascamp–Lieb · Vinogradov.

### C3. Exact reformulations (valid targets; the mechanism is missing, they are not closed)

Dual, lattice and flat-top certificates (the dual class is the target itself) · integer lattice
matrices and multiplicative sets · function fields, Hodge, Arakelov, arithmetic site ·
Floer, Bridgeland, motivic · supersymmetry, Jordan · Lasserre, Guerra · spectral flow · 𝖯⋆ ·
Arch ≥ Near at prime sites · linear programme at prime sites on the torus · L*_j(θ) · the 43
reformulations of phase 204.

### C4. One line or insufficient examination (do not count as attempted)

Jones index / Temperley–Lieb · t-concavity · strong Rayleigh · Lee–Yang · Iwasawa · seeds
G11, L7, L9 of phase 193 (F6, F7, F13, K7, M7, H3, I8 do have PROVED proofs or reductions in their
memos; C7 and CE6 were developed and remain only argued, with a numerical falsifier) · eigenvectors in rigged space · anti-Siegel
repulsion. Check in the index before using.

Two missing lemmas would close many rows of C2 at once: a PROVED falsifier for
Beurling systems or number fields (O11, O12 of P47 thm:shape), and a PROVED negative primitive background for
the Epstein form x²+5y² (today cited for the full form and argued for the primitive one).

### C5. Open residues of phase 193

Rankin–Selberg in w (A1r: the part w > 1 is closed, the continuation only argued) · metaplectic
package (A3r: rank one PROVED, exclusion argued; its residue is the Kuznetsov variant) ·
Salié/Kuznetsov (A4r) · Fejér means at points off the line · Schur factorization at fixed M · rigged eigenvectors
built with primes · residual of Δ ≡ 0 · polarized object over ℤ with ample class (G-F) ·
total positivity of order ≤ 4 (the four generators and the global sign of the Wronskian of four
densities are PROVED in 211; the global transport is missing) · non-unimodular transfers · D_∃c · SPEC_A with only
identities · the step ½log5 → ½log7.

## D. Do not relaunch from phase 211 (with reopening condition)

Summary. The complete list, deduplicated and with line of origin, is in `ANNEX_211_GLOBAL_REVIEW.md` §A
(54 items) and `ANNEX_211_GRAM_HYPERBOLIC.md` §A (24 items); those of the other files of the phase, in
`ANNEX_211_FILES_*.md`.

D1. Rebuilding the density bridge or another parametrization of the ladder — what is missing is the sign at all
    sizes, not the bridge.
D2. Adding filter dimensions, optimizing thresholds, extending the tower of finite orders. TP2 does not
    imply total positivity of all orders; pairs do not imply triples, nor four-node
    concavities (3×3 counterexample to «V‴ > 0 ⇒ order three», 211/074; cycle (p,p,p²)).
D3. Inferring density or sign from a positive union. L² density alone does not give continuity of the full
    form; repairing the moment with positive generators one by one does not pay for the crossings; varying the
    rate does not repair the density of the union (211/096). Reopened with liminf r(n)²/n = 0, a block
    that repairs the moment **and** control of its crossings.
D4. Recurrence or descent alone. Reopened with a uniform arithmetic bound on the averaged remainder
    R_L ≥ −ε_L, ε_L → 0 (the average per initial entry suffices, not each atom), or with a family of
    jointly positive subspaces approximating in a topology where the form is continuous. The
    bound must distinguish the real multiplier from the shifted one (falsifier W_4 = W − 4‖·‖²).
D5. Schur–Green monotonicities — only with a distinct joint invariant preserved by each operation.
D6. Renamed heat/Poisson/theta identities — only with a concrete joint inequality.
D7. Variants of the cumulative-inverse budget (211/POWER_CUMULATIVE_INVERSE_022) — only if they also pay ARCH_♯ and justify their range in k.
D8. Arch − Div − Near via Poisson/divisors, smooth family s_w, gauged tails, near-coincidence
    patterns — only with a new hypothesis that resolves the identified failure.
D9. Comparing Off with the divisor energy E_y, or A with a fixed fraction of R_res: refuted by an
    explicit falsifier (pairs k, k+1; 211/GRAM_SLICES §17.6); nor is there a uniform upper bound
    in norm; the dilation operator is not paid separately (§17.7) nor via resolvents (§17.8).
    Attention: at y = 0 the inequality Off ≥ −R_res is exactly A_0 ⪰ 0 on integers, that is the
    full target, to be proved without margin; it is not a weaker obligation.
D10. Pointwise smallness of the tail or a fixed number of derivatives as a transfer of all orders;
     uniform Cauchy margin between layers (§8.11).
D11. Nodal localization of a negative witness; positive rates before T; BPY even/odd partition at
     scale ¼; Jensen / operator concavity (the latter with the reopening condition of
     211/GLOBAL «Later duplication control: four proposals without construction»).
D12. Assembling fixed-support PSD certificates (211/POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION);
     finite-support minorants (211/GRAM_SLICES §18.7).
D13. Matrix order by shift K − K_shift with shift 2: refuted
     (211/POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION). Other sizes and normalizations remain open in
     the source; do not relaunch without a new operation.
D14. Completeness of squares / all powers: integrality identifies, it does not sign. The
     fixed-order falsifiers hold with N ∈ {0,1}; the all-powers one needs N(2) = ½;
     exact residue 1 and count x + O(1) do not suffice either (211/SQUARE_COMPLETENESS_OBSTRUCTION §§6, 9–11).
D15. **Local, positive and bounded** metric for the theta realization, with fixed leading coefficient and
     no new connection: excluded (211/HYPERBOLIC §12.7). Not excluded: unbounded or non-local
     metrics, new connections and other realizations; selection without an explicit kernel or Green
     identity was already rejected.
D16. Theta Gram layers and their variants: individual modes, finite prefixes, smooth positive
     cutoffs, prefix plus continuous tail, symmetrization, Jacobi cutoffs, damping n^{−δ},
     primitive U, layers J_u; Hankel; CPD/TP2 («A is not TP2»); HCM; references G0/H0; theta
     branching; BPY rigidity and contractivity in the reciprocal metric; descent B_1 → B_0; factors
     (D_t² + λ); two phases A_0/A_π; fixed collections of branches of G2. The Laplace layer D_{2π} is
     indefinite, which refutes the layer-wise premise; its integrated compensation remains OPEN.
D17. Rounds 1–27: Krylov families and families of words in (M, Π) of bounded degree or homogeneous; windows in
     c; Poisson/ℱ rule; 𝒜𝒫 − c𝒞 with c ≠ 1; Weyl bounds from Arch − θ; process B / Vaughan;
     Λ-free planes E_k and every fixed finite Λ-free subspace; Schur floor class, also on
     enlarged blocks; two- and three-block assemblies; Neumann truncation of the Schur
     coupling; class 𝒦_S (estimates that only see the mass of the comb); class 𝒦_gap (spectral gap);
     Grönwall in T (reformulation); large values with Kovrijkine / Logvinenko–Sereda; λ_max(A_τ)
     without band restriction (false as a condition); sign only from the high block or only from the
     low one; capture of the sign in E_T; Lanczos blindness; exponent ray ℕ^{1+t}; global
     maximization of μ_T(v); local × archimedean Schur product over the coprime ratio. Precision:
     «𝒜𝒫 − c𝒞» is not bounded below on the full class of tails, whereas a
     fixed representative tolerates c ∈ [0, 3.5]; that is why it is not a sign step. Never omit the polar
     term 2AB.
D17b. Pointwise criteria of the POWER series (complete list in `ANNEX_211_FILES_1…5.md` §A):
     positivity of all Abel T_m, Erlang components, Ω ≥ 0, I_* ≥ 0, h_N ≥ 0 and K_N ≥ 0
     universal, Möbius prefixes, absolute Möbius contraction, criterion of positive
     primitives, monotonicities when moving poles, inheritance T_f ⇒ T_H, Peano and Loewner monotonicity of
     contacts, reflection q ↔ 1−q, discarding the Selberg term 2V, repairing only with contact 2,
     affine basis, Turán of the full values, convexity of the Gaussian functional, raw
     Volterra kernel.
D18. The eight selections in the memory of the project rules: factorial squares and physical projections;
     compensation between scales without positivity per atom; compensated primitives of layers; discrete
     summation by parts in theta; change (m,n) → (m+n, m−n) and parity; reserve of non-local
     metrics; transport by shift and congruence; joint cancellation of Pfaffians by
     reciprocity. Each is reopened only with an explicit operation and the four points.

## E. Falsifier battery (P47 thm:shape; P48 tab:cert, tab:models)

Mandatory minimum: finite deletion Λ·1_{n≥N}; amplification Λ + c·1_{n=n₀}; cΛ with c on both sides
of 1; a_P (prime powers p < P deleted: preserves the Euler product, breaks only the functional
equation); Davenport–Heilbronn; Epstein x²+5y²; quartet models ξ_{z,k} (they preserve Λ(n)
exactly and the functional equation); self-dual deformation f_t (preserves Λ(n), n < λ₁, and the functional
equation; breaks Euler and integrality); discrete Beurling systems; b_θ = Λ·½(1+cos(γ log n+ϑ)).
For each one the memo states **which exact line of the argument fails**. Quartets and f_t have the same
node as Λ: a property of the comb alone does not separate them (P47 cor:shape (a)).

## F. What the papers declare not excluded (the ground of this phase)

- Conjunction (E)∧(F)∧(I) with a nonlinear sign step (P47 rem:conjunctions).
- Constructions that use the exact multiplicativity of Λ in the sign step (P47 thm:noimport).
- Exact inequality 𝓕_T ≤ 𝔞^♯ on P_T proved with the vector and the archimedean form together, on
  vectors that see Near_M (P47 rem:bar-arith).
- Arguments with the atomic structure of the arithmetic side and the exact values (P47 rem:bar-pat);
  classes that mix estimates with an exact support axiom on log ℕ (P47 thm:geo-tv).
- Use of the positive part of the symbol on all of ℝ together with the negative set; exact reductions
  that carry the whole margin (P47 rem:bar-loc).
- Signed exterior measures. (The arithmetic squares in (½log2, ½log3) are not ground of
  this phase: 211/DOSSIER_001 §6(e) reduces them to a single eigenvalue.)
- Non-distributional functionals and functionals that couple with ζ itself (P47 thm:geo-parity).
- Two-sided laws λ_A = L(T)(1+o(1)) on unbounded ranges (P47 rem:bar-fam): not excluded, but
  their lower half is the target plus a margin (211/ROUND_007_D Lemma 4.6), and the simple
  exponential law has a NO-GO (211/LEDGER C20). It is not easier ground than the target.
- Pigeonholes without an object: O166.802.1 (nonlinear multiscale inequality, «partial completeness beyond
  X»), O2601.1 (individual Euler property), clause (5) of P47 prop:spec.

## G. Hard restrictions and explicit prohibitions from earlier phases

G1. **Euler composition and functional equation (rule O1).** The two channels must be accredited with
    distinct falsifiers: a_P for the functional equation, quartets for the Euler product. An
    argument that fails only for one of the two is using a single channel.
G2. **Phases 199–200 (IDX README l.508–567):** R-K1 (no boundary reflections nor completely
    monotone kernels in exterior data); R-Q2 (mollifier ladder); R-Π and R-Π4 (the gauge Π_μ is common to
    all falsifiers; jump comb); R-Z1 (the carrier Z is the multiplier on the line);
    C-Guo (every source of sign via radical, gauge, pole or Tate mode must name the property
    absent in Epstein); C-hom (there is no quadratic or four-point identity in the theta
    coefficients; Bochner in θ excluded); R-MOM (the order ≥ 2 constants of moments enter with
    net coefficient zero); Theorem M200.
G3. **Hypotheses to break in order to reopen phase 194:** H_cone (conic premises on log ζ or its logarithmic
    derivative), H_mono (monotone integrality), H_sparse (stability under sparse modification).
G4. **Phase 204:** Lemma F in any variant over representatives (uniform: false by explicit
    falsifier; existential: vacuous); Stein on F; Hardy on λ; the channel q_odd without a lower bound
    independent of ½ − q_odd at ½log15; interlacing or first crossing for (L2) as a method; real
    stability, hyperbolicity or interlacing on Gram symbols.
G5. **Phase 209:** non-local kernel, map U011, dominations LINK012–014, lemma J+C (see
    `ANNEX_INDEX_README.md`).
G6. **Named walls** (statement of each in `ANNEX_INDEX_04.md` §4.1): W1–W12, T1–T5,
    W-identification, W-jet, W-Sonin, W-factor, W-dither, W-coh, W-cont, W-sieve, W-tail, W-lin,
    W-det, W-fam, W-pat, W-loc, W-mom, (N′), thm:X as a necessary condition.
G7. **Falsifiers additional** to those of §E (definition in `ANNEX_INDEX_04.md` §4.2): Ξ_a, ζ_K/S₃,
    function fields, two-atom curve of type I, 3×3 model, Λχ₂, M_m, Λ̃, ζ_θ, substitution of
    roots ℕ ∪ √2ℕ, K(s), f_χ, P_{a,c}, P_171, ζ̃, Poisson combs, M₁, low band.

## H. Full-reading annexes (complete list; they prevail over this summary)

| Annex | Source read line by line | Content |
|---|---|---|
| `ANNEX_INDEX_04.md` | IDX `04_PHASES_100-189.md`, 1058 lines | the 824 rows assigned to 38 families; 227 rows that are not closures (416 with the partial ones); doubtful labels; walls and falsifiers |
| `ANNEX_INDEX_README.md` | IDX `README.md` l.366–2396 | some 565 entries; firm closures and non-closures; positive blocks |
| `ANNEX_PHASE_193_LABELS.md` | phase 193 (ledger, seed tables, audits) | each candidate in one of five classes |
| `ANNEX_211_GLOBAL_REVIEW.md` | 211 `POWER_GLOBAL_ROUTE_REVIEW.md`, 2611 lines | 92 sections; 54 «do not relaunch»; 31 positives; 30 open obligations; 27 inputs that would change the obligation |
| `ANNEX_211_GRAM_HYPERBOLIC.md` | 211 `POWER_GRAM_SLICES_OBSTRUCTION.md`, `POWER_HYPERBOLIC_MODEL_GRAM.md` | formulas of each object; 24 «do not relaunch»; 18 positive groups; 8 open obligations |
| `ANNEX_211_FILES_1…8.md` | the remaining 401 files of phase 211, in eight alphabetical blocks, all read in full | one entry per file; some 210 «do not relaunch» items with reopening condition; positives; open obligations; steps named and never resumed |
| `ANNEX_PHASE_193_PRIMARY.md` | primary memos and reviews of phase 193 | disagreements with `ANNEX_PHASE_193_LABELS.md` |
| `REVIEW_001_LC.md`, `REVIEW_001_ABD.md` | independent review of round 1 | corrected statements and scope |

Warnings from the annexes. In catalogue 04, 73 rows record no reason (the field repeats the
name), some 17 routes appear with contradictory statuses in different rows, and several «DEAD» rows
mean «superseded» or «never executed»: a row without a recorded reason is not a prohibition. The
«43 reformulations» of B3 are those of phase 204 and are not compared with the 141 REF-D rows of
catalogue 04 without deduplication.

Known limits of the coverage. (1) The routes index summarizes by phase and not by file: most
memos of the phases before 190 have no row of their own. Verified case: the memos
R170_811–840 of phase 170 (among them R170_816, which falsifies «h ≥ 0 ⟹ pairing ≥ 0», and
R170_819–823) did not appear in the index; phase 170 was later read in full (section I and
`ANNEX_170_FILES_1.md`–`_4.md`), but other large phases before 190 still lack a file-by-file reading. A search without matches in the index does not prove that the
idea was not attempted: one must also search the phase folders. (2) `ROUND_008_A.md` of phase 211
is truncated (it ends at Observation 3.3). (3) The numerical validation values of
`STATEMENT_001.md` §3 are pending re-verification (normalization of F_0).

## I. Phase 170 read file by file (112 memos; `ANNEX_170_FILES_1.md`–`_4.md`)

The whole phase works with a vector in the radical of a supposed first-contact window and with
linear functionals in F; no memo writes an identity (G). What follows has already been traversed and is not
relaunched without the indicated condition. The four points T1–T4 are the ground that round 1 left
unexcluded.

I1. **Divisor incidence as a positive form (T2, T3).** R170_863–868. With free coordinates the
    kernel of ∂ = [B, −I] is the universal graph and the form does not see the weights (865). With a coordinate
    a_d repeated on all multiples, 𝒟_N(a,c) = k^{−1/2}((a∗1)(k) − c log k) has kernel
    exactly ℝ(Λ,1) (866, PROVED). Every linear row annihilating that line factors through 𝒟_N, and every
    positive linear extension is a change of metric that loses the first jet (867–868, PROVED class
    NO-GO, also after tensoring with physical space). The form lives on coefficients,
    not on F. Reopening requires an object that is not a linear row on that space, or the boundary
    coordinate β_T(f) of 868 §5 built from the first-contact equation. The matrix
    [log gcd] = E diag(Λ) Eᵀ was not used on F in phase 170, but it was in 211:
    `POWER_GLOBAL_ROUTE_REVIEW.md`, «Factorial extension before resonance» («Extensión factorial antes de resonancia») (Σ Λ P_m*KP_m with
    entry K_{λμ} log gcd(q_λ,q_μ)) and `POWER_GRAM_SLICES_OBSTRUCTION.md` §17.2. It is the rejected selection
    «factorial squares»; the only instance with written incidence is the theta modal one, and
    the window families distinct from it were not examined (`ROUND_002_B.md`,
    `REVIEW_002_BC.md` Part B).
I2. **Identification Λ∗1 = log used linearly (T3).** R170_101, 401 §4, 704, 814–816, 835 §2.2,
    837 §6, 838 §5, 840 §5, 878–884, 896–897. It annihilates exactly the block k ≤ N; a null monitor does not
    give a sign, on recombination the form becomes again independent of the weight (837 (6.7)), and every
    linear use falls into the factored ideal Q𝒟_N and does not determine the boundary class (869, PROVED). Via
    Cauchy–Schwarz with the probability Λ(d)/log k: |β_Λ|² ≤ (log k)Σ_Λ, but β_Λ is odd and changes
    sign (841 §4.2; β(12) < 0). γ = Λ·log − Λ∗Λ clashes with the Selberg discard (850–851);
    γ + W = 2Λ·log does not survive the Poisson block (856).
I3. **Parity.** The boundary class β_phys = 𝔚_K + Θ_ext is linear and odd in F; minimality, virial and
    tangent cone are quadratic and even. A one-sided sign of β on the radical is equivalent to its
    vanishing (870, PROVED). Varying β while preserving Λ∗1 = log, linear PC, the Tate cocycle and
    diagonal minimality is possible (874, PROVED).
I4. **Common residue (T4).** The tail H_{M,N}, k > N, with h ≥ 0 always appears as an operator or
    pairing −Re⟨H_{M,N}𝓕F, S_L F⟩, without sign and only with a two-sided bound (816, 819–821, 841
    Thm. 6.1, 856). Demanding a common residue between +D_Δ and −‖W^{1/2}𝒢F‖² is exactly the closure
    (837 Thm. 5.1, PROVED): it is not an intermediate piece. The literal conversion into
    Σ_{k>N} h(k)|ℓ_k(F)|² was not attempted in phase 170; in round 2 of 212 it was excluded
    for the isolated tail with finitely many Gamma moments and remainder ≥ 0 (`ROUND_002_A.md`, Lemma;
    `REVIEW_002_A.md`), a format obstruction generic in the weight. The joint conversion with the
    blocks of E_N and of Tate remains without an object and without exclusion.
I5. **Squares per prime channel and averages over the dilation (T1).** Σ(Λ(n)/√n)‖F − U_nF‖² gives
    «squares − constant» with divergent constant and is generic in the weights (201, 301;
    falsifier a₂ = 100). Averaging the dilation only gives smoothing and compactness, without sign or
    uniformity (823–826). The Laplace energy on the Gamma lattice G_δ = 𝓡*𝓡 is positive (843,
    positivity CITED) but does not separate Λ from altered weights, the polar residue comes out with the
    opposite sign (844) and the extraction gives a filtered virial, not the physical one (849). Completing the square
    D*G⁻¹D with arithmetic D is pure congruence (860–861, PROVED). The virial term
    ∫τ m′(τ)|F̂|² of 840 (8.1) remains with sign OPEN on the radical.
I6. **Two-sided laws by linear composition.** 840 Thm. 6.1 (NO-GO PROVED, pointwise in T): no
    two-sided collar law comes out of linear compositions of PC, compressed Chebyshev, reflection,
    collars, weak equation and minimality.
I7. **Other closures.** Multiplicative unitary conjugation preserves the spectrum; a local multiplier
    with phases for every prime is e^{iφ+iθt} (501). Non-local compensation Z − RZR ≥ I + R only adds
    positive cost (601). Exchange of factors (d,m) ↔ (m,d): coincides with the already known support
    concomitant and does not fix the physical operator (871–872, 876–877).
I8. **Open with exact obstacle.** The linear identity 𝔚_K(f) + Θ_ext(f) = 0 (859; explicit
    form 856 (8.7)); the «null anchor with boundary» e_T (862); the arithmetic linear deformation of the
    Schur complement with nonzero first jet (861); VIR–LB and VIR–DET (840 §8), which together have
    the strength of the closure; the two exterior moments of 894; the channel of two prime bases
    (850 §5): cross-checked as a repetition, linear in the weight; residue delimited in
    `REVIEW_002_BC.md` C.3 point 3. Several memos depend on (REG)/C¹, not proved.

Notices. The annexes record inconsistencies between memos (withdrawals 844→846, 851→854→856, 861→862;
corrections of 838 to 837; 870 §§6–7 copied from 871). The ten `verify_*.py` and the six JSON files of the
folder were not analyzed. Several memos use an external equivalence of the target; it was recorded
without developing it and is not used.

## J. Round 3 of phase 212 (`REVIEW_003.md`): closed classes and recovered antecedents

Do not relaunch without the indicated condition. None of these results carries a sign.

J1. Multipliers and reflection J in parity sectors: pointwise splitting of the symbol (R3-a). Antecedents
    of the products mn: R161_032, 034, 035; E70_10 graded option. Reopen: operator outside that
    algebra (compression to the window, M_t, finite rank).
J2. Affine square in the weight with cross term equal to the comb: ρ ≤ Arch, not ⪰ 0 (R3-b), also in (S).
    Reopen: unpaired V, weight-dependent V_0 or V not affine in Λ, with its own formula.
J3. Canonical factorizations (root of the form, LDL in any order, Fejér–Riesz, Wiener–Hopf):
    they exist with remainder ≥ 0 if and only if the target holds (`ROUND_003_2.md` Lemma 2; phase 200
    A_MU_FACTORIZATION_001 §1). Reopen: factor with its own formula whose equality is proved afterwards.
J4. Null anchor with boundary and coordinate β_T inside a semidefinite form: invisible (R3-c).
J5. Pure dilation virial on all of P_T: no identity with remainder bounded below (R3-d).
    Antecedents: R162_501 Thm. 2.2 and Prop. 3.1; 106_124 §1; R165_202 1.4; 211 ROUND_008_C Prop. 5.
J6. Sign of an exterior block separated from the Poisson–Chebyshev identity, with any test that does not
    use the weight, envelope in the parameters or passage to the limit: homogeneous in c (R3-e).
J7. 𝔸_M = WᵀDW with W supported on divisibility: does not exist for large M (R3-f). Arch_M is
    indefinite (CA_K_001 Prop. 1.3(a), CITED).
J8. Riccati/Darboux with the comb as superpotential: phase 70, E70_10–12; R166_502 §5; CA_G_001 §2.
J9. Non-local metric in resolvent-type Green identities: determined by M; its positivity is that
    of the ladder (R3-g). Refines the entry «reserve of non-local metrics».
J10. Divisor incidence on the Nyquist mesh: 211 ROUND_005_C Prop. 2 and §5.3 (holds for Beurling
     systems and a_P). Pointwise values and jets are not admissible components of V_T (R3-h).

Refined method rule (R3-i): an isolated formal breaking does not prove the sign. What is required is a complete
identity, proved, with a right-hand side nonnegative for Λ. In a falsifier that identity may fail
without the auxiliary object losing positivity; it is not required that the remainder necessarily change sign.
See the audit of O4/O17 and of Lemma T at the end of Part V of the index.

## K. Phase 161 read file by file (83 memos and README; `ANNEX_161_FILES_1.md`–`_3.md`)

From R161_004 on, the phase works on a vector in the radical of a supposed first contact; no memo
writes (G) on all of P_T except the SP-161 goal of K7. Several memos use an external equivalence of the
target; it was recorded without developing it and is not used.

K1. **Compression to the window, leakage, position, finite rank.** Traversed thoroughly. Leakage squares
    ‖(I−P_+)C_log g‖² (020), X_T = ½‖(I+εC)g‖² (021), compressed coherent leakage (034 (5.2)), Poisson
    exterior leakage (040): correct, with no identity connecting them to the finite defect of PC. The
    test Π_TP_TZ*g collapses into the mixed pairing of (PC-ren) (023). Mixed Green with X = M_t: residual
    pieces without sign (042); the Tate term of Xf is 0 by parity (043); the primitive is a
    modulation tautology (044). Rank-one local Toeplitz–Hankel does not globalize (045). Green and power
    rewritings end in the commutator [P,S] (057, 059, 062–065). Finite rank: only the
    first collar (013, 016); reduction to λ_max(M) < 1 without a bound (073–074). Reopening requires an identity that
    connects a leakage square with the PC defect, not another leakage square.
K2. **Oriented divisor variance (030).** PROVED identity with a degree-two term in Λ that
    adds, ½ΣΣΛ(d)Λ(e)‖m_d − m_e‖². It vanishes by coherence of the translations for any weight, not by
    Σ_{d|n}Λ(d) = log n: generic. The realization fails: the path vectors do not depend on d (031);
    the physical one is the coherent sum in k with uncontrolled cross Gram (033); its diagonalization is quotient
    channel plus product channel (034; collision with phase 106).
K3. **Exit A of 033 (Parseval/Naimark dilation with labels k).** Stated, never built;
    035 declares it unnecessary and 052–053 build another dilation without labels, whose tangent gives the
    mean U+V and not the difference (056). It requires compensating the cross Gram of 034. Without a proof of
    impossibility.
K4. **Indefinite forms.** Symplectic Ω withdrawn (zero diagonal, every vector neutral; 061→062); Hermitian B
    used only on the diagonal (063); indefinite Tate cross matrix, rejected as Gram
    (023 §4; 032). No memo studies a non-radical neutral vector.
K5. **Hyperbola remainder.** h(k) = Σ_{dm=k, d≤M, m≤N}Λ(d) ≥ 0 (001 Thm. 2.1); no weighting
    w_N ≥ 0 cancels it (002 Thm. 8.1). The truncated Möbius c_N(k) does not appear in the phase.
K6. **Q ≥ 0 on the whole primitive space** for the Q of 071: excluded (081 (2.1): fails on eigenvectors
    with λ ≥ 0). It could hold only on the radical. Countermodels: 038 (2×2) to automatic saturation; 050
    (3×3) to transfer between blocks.
K7. **Open.** SP-161 / L161.1 (002 §§4–5): a_T = Σ w_N Re⟨RF, S_N𝓕F⟩ + leakage squares of
    C_T = (1−P_T)𝓕P_T, on all of P_T; only the branch w_N ≥ 0 died; the version with signed weights or
    discrete derivatives was not written. Joint accounting 032 (4.2), not derived. Coherent saturation
    (035, 037, 039), which requires a physical boundary Green identity absent from the corpus.

Notices. The exclusion of R161_018 («every linear limit of the PC graph is tautological») is declared not
established by R161_075; it is not used as a closure. The synthesis R161_099 does not cover 046–081 and keeps that
exclusion. R161_010 Thm. 3.1 was retracted by 011. R161_082–098 do not exist. The four scripts were not
analyzed.

## L. Round 4 of phase 212 (`REVIEW_004.md`): closed classes and recovered antecedents

L1. Goal L161.1 (R161_002 §§4–5) with real weights in the cutoff index, signed or not: only the
    trivial solution (R4-a). K7 of the previous section is closed in that class.
L2. Sieve weights (Selberg, Barban–Vehov, GPY, Λ_R) as test or inverse: phase 200 Q1–Q3, MULT_GAUGE,
    GG_001; R162_1003 §4. They do not raise the degree in the weight (R4-b).
L3. Quadratic divisor defect that adds, required for every weight: target with margin (R4-c); phase 197
    BARRIER_D2_001.
L4. Translation-invariant approximate inverses, truncated Möbius included: splitting of the symbol; R ≤ 0
    false (R4-d); phase 200 A_MU_FACTORIZATION_001 (d).
L5. Pivots determined by the near-divisibility pattern; totally positive, Pólya, Green kernels
    or functions of the gcd for 𝔸_M (R4-e).
L6. Inertia count, Kreĭn or Pontryagin signature: P47 thm:parityschur, prop:polarcap,
    subsec:inertia-excl; phase 197 BARRIER_W_001. It does not distinguish c = 1 (R4-f).

## M. Cross-check of signature and closure mechanisms (`ANNEX_COTEJO_LORENTZ_1.md`, `_2.md`)

Cross-check by grep over the whole corpus with 31 and 36 files opened as primary sources; it is not exhaustive.

M1. The reading «at most one negative direction per parity sector» is already in `R160_C7_R1` §§5–6:
    the Lorentzian quadratic class, the closure by limits, Alexandrov–Fenchel and the combinatorial version
    reduce on the quadratic form to the original statement (Prop. 6.2). §6.3(2) leaves OPEN an object of
    degree ≥ 3 with Hessian −a_T, for lack of an independent source of nonnegative coefficients.
M2. Closure mechanisms already attempted: phase 120 (combinatorial induction on a lattice of collisions
    of prime powers; additive iteration does not inject into an idempotent join, Φ(2i) = Φ(i));
    `114_d_244` (tangent form with inertia (1, |S|−1); rank obstruction; not identified with a_T);
    phase 197 `BARRIER_W_001` (induction in the window; its five properties hold for cΛ, a_P and
    Beurling); phase 65 (Schur shorting on kernels of a canonical system; refuted in R137_005);
    `G2_B8` (sum of local forms; fails for T > 0.5925).
M3. On 𝔸_M or 𝖡: real stability, Gårding, MSS (`INV_M_001`, false); GKS/FKG (`CA_J_002`, frustration);
    total positivity (fails at order 2); Perron–Frobenius (`H1_PROOF`, only simplicity and parity).
M4. The logarithmic-derivative wall (`INV_F_001` F2) reaches conic premises on the series or its
    logarithmic derivative; it does not formally reach signature properties of a_T nor integrality.
    That only the infinitely divisible classes and the Pick class cross is ARGUED outside the
    classified list (P47 prop:spec (6)).
M5. Not found (does not prove novelty): object of degree ≥ 3 with Hessian a_T built with the comb and the
    window; closure under product of Euler factors applied to the signature with the archimedean factor
    fixed, and its check at c = 2; Lee–Yang measures or Newman/Lieb–Sokal closure built
    from the form; stability preservers on s_T; induction lengthening the window for the
    signature per sector; deletion and contraction on the divisibility lattice of [1, e^{2T}).
    Citation correction: the discard F5 of phase 193 uses «n₋ > 2 on the whole space», miscited
    (`ROUND_004_E.md` Prop. 1).

## N. Round 5 of phase 212 (`REVIEW_005.md`): signature and closure mechanisms

N1. Lorentz signature or log-concavity at a base point: it is (G) or the statement (R5-a).
N2. Hyperbolic polynomial of degree ≥ 3 with Hessian −a_T: degree two, or the target with margin (R5-b).
N3. Closure under product of Euler factors on the signature: impossible without balance; with balance no
    operation remains (R5-c).
N4. Induction in the window using that «the incoming weight is determined by the previous ones»: the premise
    holds for every weight; at the crossing the incoming weight has no influence (R5-d).
N5. The form as a variance of a valuation model: it is (G); the laws of ζ^c are probabilities for
    every c (R5-e).


## O. Round 6 of phase 212 (`ROUND_006_WINDOW_SPLIT_NUMERIC.md`, `REVIEW_006.md`): window-dependent splitting per prime

- O1. Rule «each prime yields the kernel at the distance of its own contact» + free potentials `W_p(t)`:
  rejected at the gate. The kernel part is the complementary slackness of Theorem D of
  `phase-159-row-d-two-front-construction/G2_B8_R5.md` (the interior maximum is attained at the indicator of the prime
  with largest `ε_σ(u)`; the values of §4 already show it). As a prior rule it is circular (J3): the bands are
  defined by the obstructing states. With free `W_p(t)` it is class M of round 6, `τ = −1.60·10⁻⁴` at
  `T = 0.5925` (NUMERICAL, one resolution).
- O2. The literal statement «the kernel at its own distance contributes nothing» is false: adding kernel in a
  band around `log p` strictly raises the bottom of the local form (`REVIEW_006.md`; PROVED for
  `T > log p − δ` if the infimum is attained, ARGUED otherwise).
- O3. Signed parts without a rule: empty splitting (existence = the target), `G2_B8_R4.md` §1.
- O4. NUMERICAL, without textual antecedent: two-position `θ_p(t,s)` reaches the ceiling up to `T ≈ 0.69` and
  fails from `0.70`; it is generic in `c`; the dual is a pair of states of equal pointwise density.
- Reopening: closed formula for `θ_p(t,s)` and `W_p(t)` not taken from an optimizer, not affine in the exact
  weights or in relations between contacts of distinct primes, with the breaking for `cΛ` named and a
  three-prime statement; or an identity writing the negative part of `θ_p` as a square compensated by a
  named term of another prime with manifestly nonnegative remainder. First falsifier: `T = 0.5925`.

## P. Cross-check of the near-null subspace (`ANNEX_COTEJO_NULLDIR.md`)

- P1. Taking as the object the near-null directions of `a_T` on `P_T` and seeking an exact identity on
  that subspace: repetition of candidate C11 of phase 211 («near-null pair and tangency»), with C8, C12,
  C16, C19, C21, C35, C43, C51. Antecedents: 211 `ROUND_003_A.md` (parity, tangency, rigidity; PROVED, without
  sign), `ROUND_002_D.md`, `ROUND_002_E.md`, `ROUND_004_A.md` Prop. B (finite `Λ`-free planes, NO-GO),
  `ROUND_021_A.md` Lemma 3.3 (width of the window in `c` = margin); phase 192 (three exact identities on
  the minimizer, excluded); Paper 47 lem:contA, cor:Tarch, lem:degen, thm:X.
- Reopening: a subspace `S_T` written without solving the problem and of growing dimension, with the
  identity on all of `P_T` and every `T` and the line that breaks for `cΛ`. Not executed: the conjectures
  (C1)–(C3) of `ROUND_003_A.md` as theorems (structural; they do not give the sign).

## Q. Round 7 of phase 212 (`REVIEW_007.md`)

- Q1. Bounding each contact by a potential `≥ 0` (local gauge, ground-state representation with
  position-dependent `φ_p`, chains of any length, with any kernel splitting): NO-GO with class,
  PROVED relative to Paper 47 cor:Tarch; dies before `T = 0.60` (R7-a).
- Q2. Stage predicate «form + correction in a convex cone» with uniform step: equivalent to a local splitting
  by contacts, PROVED (R7-b). Reopening: history-dependent step with data given by its own formula.
- Q3. Dilation with composition of contacts (exit A of R161_033): repetition of R161_034; the quotient
  channel is `∫ĝ|A|²` and does not see the arithmetic, the product channel is `∫ĝ Re A²` and has no sign (R7-c).

## R. Round 8 of phase 212 (`ROUND_008_A.md`)

- R1. Boundary concomitant converting the product channel into the quotient channel (demand of R161_034 §0):
  already executed and closed in phase 161. R161_035 (parallelogram square `¼‖(U_N − V_N)f‖²`, saturation
  missing), R161_037–039 (2×2 countermodel), R161_057–065 (the boundary term is the support commutator
  `⟨g,[P,S]w⟩`, without sign; positive expansion withdrawn), R161_050 (3×3 countermodel). Repetition.
- R2. Flagged residue: using the semigroup law `τ_{log k}τ_{log l} = τ_{log kl}` inside the commutator. Summed
  with weights `Λ∗Λ` the Leibniz rule gives `[P,S²]`; the associated square, `PS²P − (PSP)² = |(1−P)SP|²`, is the
  Toeplitz–Hankel identity of R161_045, whose global assembly is already closed there (phase 122). Reading
  ARGUED; R161_045 was not reread in full.

## S. Round 9 of phase 212 (`REVIEW_009.md`)

- S1. Mean density of contacts as a source of positivity and fluctuation as cost: repetition of 188
  N_BUILD_001 / N_BUILD_011 (`κ* > 1`). Polarization of `Λ = μ∗log`: repetition of L2_BUILD_017.
- S2. Schur, Verblunsky, Jacobi, Sturm, Darboux recursions, canonical systems, transfer by primes:
  all with antecedent; they end in J3 or are blind to the weight. A step using only divisors does not fail under
  Beurling (R9-b, Lemma A): every recursion must couple the additive structure.
- S3. List P1–P12 of properties of the object and taxonomy of classes: `ROUND_009_G3.md`. Without mark and without object:
  contraction in a projective metric with history-dependent step; convex functional with Hessian `a_T`.

## T. Reading of the Sonin family, round 10 and concentration literature

- T1. (`ANNEX_SONIN_READING.md`) The identity «form = Sonin square + remainders» (R183_018 Prop 3.1,
  PROOF_L_SHARP_D_001 Thm 2.1, R186_015) uses a unitary transform for any phase, also with `cΛ`,
  deletion and Beurling; its square is blind and the sign remains in the remainders (smooth part and prime Toeplitz, without
  sign). `W_{S(T)} = W_T` is already in R183_030 §1.1. No statement about the remainders outside closed classes.
- T2. (`ROUND_010_A.md`) Additive covariance enters through three channels: Tate–Beckner (without weights, blind), Poisson
  over ℤ of the unweighted comb (detects only Beurling), and its coupling with `Λ∗1 = log`, which is the identity
  (PC) of R161_001 Thm 3.1. The first two PROVED; exhaustiveness ARGUED. Ladder factorization, domination by
  the prolate operator and mixed Bochner: repetition (R161_002, K2, J8; W-lin, W11′, B2; CPOS_CLASS_001).
- T3. The residue that `ROUND_010_A.md` leaves as OPEN (signed weights `w_N` in SP-161, K7) is already closed in
  L1: with real weights in the cutoff index, signed or not, the only solution is the trivial one (R4-a of
  `REVIEW_004.md`; `N = 1` gives `S_1 = I` and (PC) reduces to `X + 𝓕X𝓕 = M`). No residue of round 10 remains.
- T4. (`ANNEX_LITERATURE_CONCENTRATION.md`) Literature on Fourier interpolation, crystalline measures,
  magic functions, prolates, de Branges, Dirichlet `H²`: already in the index or without sign dependent on the
  exact values of the weight. Five mechanisms without substantive mark, none passes the gate: Gauss-type
  transfer at critical density; Serre derivative criterion with integrality; reflection of operators of order
  > 2 (residue of CS0_COMMUTE_001); Borodin–Okounkov on a finite interval; Olsen's local theory. Citations not
  verified in the primary sources.

## U. Round 11 of phase 212 (`ROUND_011_A.md`): open residues of phase 161

- U1. Sign of a lattice discrepancy (integral test, Hermite–Hadamard, Euler–Maclaurin) applied to the
  remainders of (PC): selection NO-GO. `Δ^R ℓ_T(F)` is linear in `F`; a sign for every `F` on a linear
  functional annihilates it (PROVED). `Δ^R` uses only the integer lattice with weights `n^{−1/2}`, without `Λ`: its sign survives
  `cΛ` and deletion (PROVED). Replacing `log n` by `Σ 1/m` collapses to the Stieltjes scalar class (R161_004).
- U2. Status of the four residues: quadratic L161.3 closed by R161_029 (false monotonicity), oriented OPEN;
  L161.5–6 tautological (R161_023, R163_153); port minimum closed by R161_038 / R161_050; L161.4 OPEN without
  no-go (a non-circular normalization `V` is missing). All four live on the radical of a supposed first
  contact, not on all of `P_T`. CITED by the memo; partial reading of several memos.

## V. Round 12 of phase 212 (`ROUND_012_A.md`): residue L161.4

- V1. L161.4 (R161_020) does not pass the gate: on the radical it is equivalent to the goal. The vanishing of the leakage
  `(I−P_+)C_log g` forces `F = 0` for any weight (Lemma A of the memo; not re-derived here), so that the
  clause «the first contact annihilates the left-hand side» is `ker H_{T*} = {0}`. The version on all of `P_T`
  exists only with `M_T = H_T^{−1}Ł`, circular (J3). `E_N^ren` does not contain `Λ`: the two squares are blind to
  `cΛ` and to deletion; what breaks is the equality, not a signed remainder. Patterns B3/B9.
- Reopening: `M_T` or `V` with its own formula from `E_N^ren`, the Euler current and the Tate
  coefficients, without `H^{−1}`, breaking at `c = 2` at a named step that uses `Σ_{d|n}Λ(d) = log n`.

## W. Round 13 of phase 212 (`ROUND_013_A/B/C.md`): small window and combination operations

- W1. «Structural proof in the window of contacts 2, 3, 4» is a repetition of 211 `ROUND_003_A` (codimension-one
  tangency at `c*`, without missing square) and `ROUND_021_A` (Prop. 3.2 at `R = 5`: the form is
  `Q_0 − c𝒦_R` with both pieces `Λ`-free; controls of §2.3). The set of `c` with positivity is a
  closed interval containing `[1 − λ_0/‖𝒦‖, 1 + λ_0/‖𝒦‖]` (PROVED; the form is affine in `c`). Hence
  no proof is obliged to use `c = 1` exactly, only with precision of the order of the margin, and an
  identity that merely breaks at `c ≠ 1` is not a reason for the sign.
- W2. Combining a blind square and an object that sees the weight by Cauchy–Schwarz, Gram or Schur complement:
  the concrete formats examined repeat R170_861 (0.3) and R170_841 §4.2. The projection-residue identity
  and the Schur equivalence are valid, but they do not exclude a Gram with its own formula whose
  identification with a_Λ is proved independently. The former universal veto is corrected: the
  auxiliary positivity may survive a control and only the identification with the form may fail.
  Building the block assuming the sought sign remains circular.
- W3. A square `‖u_0 + u_Λ‖²` is quadratic in the weight and the form is affine: an identity valid for every
  `c` forces the vanishing of the quadratic term (PROVED). An identity valid only for the true weight
  is not excluded by this; it requires a quadratic identity in `Λ` in the quotient channel, where the
  coefficient at coprime `a/b` is `Λ(a)Λ(b)/√(ab)` and the diagonal `Σ Λ²/n` diverges, and where `Λ∗1 = log` does not
  act (it governs products `L S_N`, not quotients `L^*L`) (PROVED). Clash already recorded in I2/I5.
- W4. Map of fourteen combination operations (`ROUND_013_C.md` §2): eleven with antecedent and closure; the
  Mourre/virial commutator is the Lyapunov format of `ROUND_012_A` Prop. B. Lemma T (PROVED in the
  declared and refined class): a certificate transfers positivity to a control only if the identity,
  the sign hypotheses and the control of all additional terms survive. Lemma K (PROVED): the two declared sources
  of convexity give Hessian `≥ 0` when their measures or weights are positive. This does not exclude
  identifying them with the form via a Λ-specific identity that fails in the control. That (PC) is the only relation that
  fails in the three controls at once is ARGUED (it depends on the completeness of `ROUND_010_A` Lemma C).
- Without a written object and without class closure: Birkhoff contraction between windows; convex functional with
  a source of convexity distinct from those examined or a specific arithmetic identification not yet built;
  odd and nonlinear pairing in `A_M`; positive
  non-Gram block with its own source of positivity; quadratic identity in `Λ` in the quotient channel.

## X. Round 14 of phase 212 (`ROUND_014_A/B/C.md`): quotient channel, non-Gram block, transition between windows

- X1. Quadratic identity in the weight in the quotient channel: no candidate passes the gate. Polarization
  (PROVED): `‖Lw‖² = 2⟨Lw,LB⟩ − ‖LB‖² + ‖L(w−B)‖²` for every weight, so that «linear in the weight plus nonnegative
  remainder» always exists and the remainder is blind. If `u_0` may contain `Λ` as a fixed function, the
  identity `a_T = ‖u_0 + u_Λ‖²` exists if and only if `a_T ≥ 0` (J3). Transport from the product channel to the
  quotient channel by finite sums of weight-free translations and `J`: excluded by unique factorization
  (PROVED for finite families and shifts `±2 log r`; ARGUED with `𝓕`, windows or infinite families);
  class distinct from R1. `TT^*` duality: kernel diagonal in `n`, without product channel (PROVED). Cross-check of
  R161_034/035 and of phase 106 indirect (via annexes).
- X2. Multiplicative positivity over primes (Schoenberg, Schur product, Pick, total positivity):
  repetition of `ROUND_013_C` O10, INV_F_001 (row C5, Theorem F2), M3. In a semigroup the parameter plays the role of
  `c`; the Schur product passes to integer Hadamard powers. Class 𝔖 (Schur product of exponential
  factors per prime, each `⪰ 0`, times a weight-free archimedean factor): remains `⪰ 0` with `2Λ`,
  with deletion and with Beurling (PROVED at finite points). M4 is PROVED only for 𝔖.
- X3. Transition `Φ: P_{T′} → P_T` with `a_{T′} = κ a_T∘Φ + R`: without an object. The remainder satisfies `R ≤ a_{T′}` and
  `κ s² ≤ λ(T′)/λ(T)` if `‖ΦF‖ ≥ s‖F‖` (PROVED); this restricts the step (exact identity or loss equal
  to the ratio of margins) but is not a class closure: what is missing is a manifestly nonnegative `R`.
  The base window does not distinguish the controls; the step that must break at `c = 2` is the certificate of `R`.
  `Φ` based on `P_T S_N^*`: falls into the commutator `[P_T, S_N]` of R161_057–065 (ARGUED).
- Without a written object and without class closure after the round: non-affine lag transport (reindexing that
  depends on the factorization; cross-check first with the rejection «(m,n) to (m+n,m−n)»); Hadamard positivity
  coupling distinct primes using `m ≈ kn`; non-exponential factors in the weight; maps between windows nonlinear
  in `F`; convex functional with a source of convexity distinct from positive measure/weights;
  odd and nonlinear pairing in `A_M`.

## Y. Round 15 of phase 212 (`ROUND_015_A/B/C/D.md`)

- Y1. Non-affine lag transport: repetition. The reindexing `m − kn = h` is 188 `L2_BUILD_030` §1(c); the
  Farey variant, INV_C_001; Ramanujan sums, INV_H_001; large sieve, SPEC_SIGN_OBJECT_008 V3; Selberg
  weights, L2. Class `Σ_n x_n Q_n` with `Λ`-free `Q_n ≥ 0` and `x_n ≥ 0` affine in `Λ`: nonnegativity
  only uses `x_n ≥ 0`, which holds in the three controls (PROVED, with Lemma T of round 13).
- Y2. Coupled splitting of two primes and block hierarchy: repetition of 159 G2_B8_R5 Obs. 4.3; the level
  of a block is the form itself (J3). The obstructing pair is not a marginals problem (ARGUED).
  Smith factorization over prime powers: blocks per prime plus a rank-one term, `Λ`-free
  (PROVED).
- Y3. Convexity with another base point: within R5-a/M1. Second variation of `log ζ^c` along any
  path: affine in `c`, both pieces convex (PROVED according to the memo). Index of a pair of projections, spectral
  shift function, Cayley/sign: equal to `n_−(a_T) − n_−(Arch)` (circular; BARRIER_W_001 W1/W2).
  `det(1 − cK_T)` and its cycle expansion: R186_034 and R186_045 §3.2 (W-det). Prékopa marginalization:
  `−D² log Z = E[Schur complement of D²V] + G`, `G ⪰ 0` blind (PROVED modulo Brascamp–Lieb CITED).
- Y4. Threshold of the two-position per-prime splitting: `T_DIR ∈ (0.697, 0.699)` (NUMERICAL); contact 4 is not
  the cause (it fails also without it). Lemma R (PROVED): if `a = q_2 + q_3 ≻ 0`, the minimal rank of a
  transfer `X` with `q_2 + X ⪰ 0`, `q_3 − X ⪰ 0` is `ν_−(q_2) + ν_−(q_3)`. The vector of the missing square
  is `ℓ ∝ a·w` with `w` the bottom of `a w = μ q_3 w` (construction PROVED; coincidence with the optimum
  NUMERICAL). No closed form. The law «missing squares = contacts in the window» is false in this class
  (NUMERICAL: rank 0, 1, 2, ≤ 4 between 0.697 and 0.80 with fixed contacts 2, 3, 4).
- Without a written object and without closure: sieve weights defined by an extremal problem on the
  exact values of `Λ`; potential `V(x,F)` non-quadratic in `x`, convex only for the true weight; the invariant
  `n_miss(T) = min ν_−(q_2) + ν_−(q_3)` as a function of `T`.

## Z. Round 16 of phase 212 (`ROUND_016_A/B/C.md`): curvature, states, reflection positivity

- Z1. Curvature (Bakry–Émery, Ollivier, Erbar–Maas): repetition of phase 64 `CURVATURE-computation.md`, 195
  `INV_N_001` (Theorem 3.3) and `R160_M10_R1` (T3, T4). With signed rates: for symmetric `L` with
  `∫Γ = ⟨−Lf,f⟩` and `∫Γ_2 = ‖Lf‖²`, the integrated condition CD(κ,N) is equivalent to the spectrum of `−L` not touching
  `(0, κN/(N−1))`; it is a gap, compatible with eigenvalues `≤ 0`, and gives no sign (PROVED).
- Z2. KMS states on Hecke algebras / `𝒯(ℕ⋊ℕ^×)`: repetition of 193 `CA_E_000` §E1 and 114_d_116. The
  smoothing of the dynamics evaluates `F̂` at the frequencies `log n`; the form uses `c_F` at the lags `log n`
  (dual variable) (PROVED according to the memo). The control `c = 2` is realized with the ring `ℤ×ℤ` (weight `2Λ`,
  exact mixed relations), but there the archimedean part is also doubled: no ring realizes
  «double weight with simple Arch». Deleting a prime power breaks integrality (PROVED). Beurling:
  ARGUED.
- Z3. Reflection positivity, correlation inequalities, Gaussian domination: repetition of 193
  `CA_A_007` §3 (Lemma 1, Theorem 2), 200 `K1_OSG_001`, front J of phase 193 (`CA_J_000`–`002`), M3.
- Without a written object: elements built with the additive shift instead of the dynamics; pointwise
  form `Γ̃ ≥ 0` that does not come from nonnegative rates with `∫Γ̃ = a_T +` blind term.

## AA. Round 17 of phase 212 (`ROUND_017_A.md`): the wall of the per-prime splitting

- AA1. Correction of a premise: Theorem A of phase 153 (`R153_001` §1.2) is a conjugation identity
  for the form of the falsifier `Ξ_a`, not a decomposition of `a_T`; the positivity at `log 2` comes from
  an interval-arithmetic certificate. The corpus contains no proof by mechanism of the
  positivity above the archimedean threshold; nothing proves `T_DIR ≥ log 2`.
- AA2. `T_DIR ∈ (0.696, 0.698)` at two resolutions, without approaching `log 2` on refinement, and the same without the term
  `n = 4` (NUMERICAL). The double chain `t, t+log 2, t+2 log 2` already fits at `0.694` and the splitting still reaches the
  ceiling: the chain hypothesis is discarded. At `T_DIR` the diagonal pair `Y_2 = Y_3 = ½e⊗e` ceases to be
  optimal in the dual and the non-diagonal pair is born at second order (PROVED in Galerkin, ARGUED in the continuum).
- AA3. Allowing the atom of a contact to be split between the two pieces according to position, with nonnegative
  fractions, recovers the ceiling at `T = 0.70, 0.72, 0.75` (NUMERICAL; undecided at `0.80`). It works
  by dissolving the prime labels; the two-sided version is trivially exact (`q_2 = q_3 = a/2`), pattern
  J3/O3. What makes DIR fail is requiring that each atom be whole in one piece.
- AA4. For every splitting, the step that fails in the controls is the existence of the splitting, which fails only
  because the form ceases to be `⪰ 0`: automatic case R3-i, not a named step. Reopening: own and
  explicit formula for the one-sided weight of the atom that breaks at `c = 2`.

## AB. Round 18 of phase 212 (`ROUND_018_A.md`): local mechanism for the per-prime splitting

Local goal, with point (4) of the filter relaxed for this case: a proof by mechanism at one `T` above the
archimedean threshold. It was not obtained; there is no closed formula for `θ_p`, `W_p` nor a proof of `q_p ⪰ 0`.

- AB1. Ground-state identity (PROVED): for real `φ` nonzero a.e.,
  `Q(F) = ∫(Qφ/φ)F² + ¼∬M φ(t)φ(s)(F/φ(t) − F/φ(s))²` on all of `L²(I)`. A contact is a positive jump
  rate; its square carries the sign of `φ(t)φ(t−log n)`. A `φ` that changes sign across the contact
  makes it negative: the hypothesis of a «ground state with sign change» had the sign backwards.
- AB2. `a_T(1) ≤ ∫W < 0` for `T ∈ [0.2, 0.75]` with elementary bounds (PROVED according to the memo; at `T = 0.65`,
  `a_T(1) ≤ −2.17`). Corollary: no representation «sum of squares plus potential `≥ 0`» valid on all of
  `L²(I)` exists in that range, with `φ` of any sign and independently of the weight. Every local proof
  must use the restrictions of `P_T`. It covers the gap of sign-changing `φ` left by
  `ROUND_007_A` §2.
- AB3. NUMERICAL (coarse Nyström model): positive ground state with the restrictions of `P_T` as
  rank-two Lagrange terms: margin `−0.28` at `T = 0.5` and `−0.80` at `T = 0.62`. The bottom of `a_T`
  on `P_T` for `T = 0.62–0.68` is even, with pattern `+ − +` and nodes near `±0.2`, of the same sign in the two
  extreme zones of the contact of 3.
- Not attempted: Poincaré/Wirtinger-type inequality on `P_T` for the kernel `K` with explicit constant
  obtained by hand (Paper 47 has it only by certificate).

## AC. Round 19 of phase 212 (`ROUND_019_A.md`): scale reading of the margin

- AC1. «The positive remainder is the lattice tail beyond `N = e^{2T}`»: REFUTED. The exponent of the margin
  is `(e^{−π e^{2T}})²`, the Gaussian tail of the `n = 1` term of theta squared (PROVED, read from
  R160_M4_R1), not a lattice term at `k = N`; the prime tail beyond `N` enters with negative
  sign (ARGUED). `ρ_T` cannot be a lattice tail with nonnegative weights.
- AC2. Under the controls the near-null vector `X_T` ceases to be so because `M` leaves the radical: `≈ +1.70` with
  `2Λ`, `≈ −9.56` deleting 2, `≈ +7.70` deleting 3 (NUMERICAL). The breaking is fixed by the small contacts, not
  by the tail.
