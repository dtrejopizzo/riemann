# AUDIT  B — L55 (Johns), L57 (Eberwein / "Lemke"), L35 (Franchi Viceré)

Adversarial literature audit. Labels: PROVED / CITED / CONDITIONAL / OPEN / NO-GO / NUMÉRICO.
Sources were downloaded to a scratch directory and read in full where noted. Nothing in Paper 47, the grid or the crossword was edited.

## 0. Bibliographic data and reachability

| item | data | reached? |
|---|---|---|
| L55 | Nic Johns, *Positive solutions of the explicit formula for ζ(s): near-criticality and uniqueness*, v1.4, Oct 2026, Zenodo 23238720; source at github.com/nic410/zeta-positive-solutions (LaTeX, Hermite-interpolation code, Lean 4 with 22 axioms). AI-assisted; the author says no human expert has checked it. Part II (claims Conjectures S and U) is a separate repo and was **not audited** | Zenodo page: yes. GitHub: cloned, §02-setting read in full, abstract and intro read |
| L57a | Logan Eberwein, *The truncated Weil quadratic form: inertia, visibility, structural measurements, and no-go theorems for the Riemann Hypothesis*, Oct 6 2026, Zenodo 10.5281/zenodo.23177438 (supersedes zenodo.23174797); repo github.com/loganeberwein6/Logan-Eberwein-RH-Weil-Window. This is the academia.edu text (academia.edu/178025276) | academia.edu: **403, unreachable**. Same PDF from GitHub: §1–§2 and §7 read in full, §8 in part |
| L57b | "Lemke 2026": Sören Lemke, *From truncated Weil arithmetic to a finite real spectrum*. It is **only** cited as a private communication in arXiv 2609.04908 (*Construction of finite Hilbert–Pólya matrices from Weil's explicit formula*). Content per that citation: subtract the simple least eigenvalue of the arithmetic Weil matrix, normalize its even eigenvector, take an oblique projection, then apply a diagonal frequency matrix. | **No public text found.** The corpus file `00-references/arxiv-math-nt-2026-review/2609.33692v1.txt` is **Freiberg, "Biases in the distribution of primes in short intervals"**, not Lemke, so the L57 entry "Lemke is LISTING-ONLY (2609.33692)" is **misattributed** and must be corrected |
| L35 | Christian Franchi Viceré (A.I. Visions LTD), *A proof of the Riemann Hypothesis…: Weil positivity via semilocal spectral descent*, v1 (file 169_HR_RH_v6.5.pdf), Apr 12 2026, Zenodo 19546495 | PDF downloaded through the Zenodo API and read in full (§2–§3) |

## 1. L55 — Johns, LP slack κ*

**Statements (from 02-setting.tex).**
- Test class: 𝒯 = even, real functions analytic on |Im z| ≤ ½+δ with (1+|z|)²|F| bounded.
- Arch(F) = F(i/2)+F(−i/2)+∫F Ω_∞, where Ω_∞ is the digamma density. **The polar term is part of Arch.**
- Admissible pair: positive measures μ (zero side, even) and ν on [log2/2π, ∞) (prime side) with Arch(F) = ∫F dμ + π⁻¹∫F̂ dν.
- Cone: 𝒞 = {F ≥ 0, F̂ ≥ 0 on [log2/2π, ∞)}. Slack: κ* = inf{Arch(F) : F ∈ 𝒞, ∫F = 1}.
- Thm (duality) [PROVED in paper, standard; the proof route was checked and is sound]: 𝒦 ≠ ∅ ⟺ Arch ≥ 0 on 𝒞 ⟺ the same on Gaussian packets ⟺ κ* ≥ 0. Method: Carathéodory in finite-dimensional sections, a-priori bounds, Helly.
- Prop (floors) [PROVED]: κ* ≥ −1.3231. This is elementary.
- Certified: κ* ≤ 1.4291572·10⁻¹⁰⁶⁰, using Ξ²P_J(t²) with J = 111 prime powers. The certificates vanish at every zero. The proof is computer-assisted; the code was not rerun here (NUMÉRICO for us).
- Unconditional lower bound: κ* ≥ −2.7112·10⁻³, from a certified admissible pair for a slightly larger conductor.
- Theorems B: uniqueness when μ is supported on the ordinates plus 0, or on the ordinates plus summable extra points with ν on the Bondarenko–Radchenko–Seip nodes, or when μ is integer-atomic.

**Correctness.** The parts read are correct and standard: a Delsarte/Odlyzko–Poitou–Serre-type LP. The only nontrivial claims are the numerical certificate and Part II, and neither was re-verified. I found no error in §2.

**Relation to Paper 47.**
- **No overlap in the object.**
  - Johns' κ* is a *linear* program on the whole line with a *fixed* prime gap log 2. It has no window T and no Tate/primitive constraints, and the polar term is inside Arch.
  - Paper 47 def:PD is a *quadratic* (eigenvalue) problem at every window T. The primal is μ = |F̂|²dτ/2π with μ̌ = 0 beyond 2T plus the two polar constraints. The dual consists of signed ν on {|u| ≥ 2T} and β ∈ ℝ².
- **Structural parallels:**
  - (i) Johns' duality theorem ↔ thm:D1 (strong duality, finitely atomic dual sequences). Same Carathéodory/compactness skeleton, different cone.
  - (ii) Johns' certificates Ξ²P_J, which vanish at every zero, ↔ thm:Z (a certificate equals the explicit formula, i.e. a zero-side sum). Johns' certificates are positive on ℝ and not flat-top, so they do not contradict finZ.
  - (iii) The band-limited slice of Johns' cone, with F̂ supported in the gap, is exactly the nonnegative band-limited functions. By Fejér–Riesz/Akhiezer these are the |Ĝ|², i.e. our class at 2T ≤ log 2 **without** the primitive constraints and **with** the polar term. So Johns' statement restricted to the gap is the *complete-form* (non-primitive) version of λ_A(T) ≥ 0 for T ≤ ½log2, which Paper 47 already proves.
- **κ vs κ_⋆: name clash only.** Our κ_⋆ (thm:kappa, sec:combs) is the density threshold for the smooth comb 2κe^{u/2}du to be positive at every window; κ_⋆ ≥ ¼|C₀| > 1. Johns' κ* ≈ 0 is the LP slack. They are not comparable.
- **Usable:**
  - (a) "Certify an admissible *primal* pair for a perturbed conductor to get an unconditional floor" is a primal-side method. Paper 47 has only dual certificates. The analogue would be a lower bound for λ_A via an explicit positive representing pair at a shifted archimedean datum.
  - (b) Hermite interpolation at prime powers as a certificate family. It can be compared with the lattice certificates thm:R / thm:latedge, which pay an O(1/M) edge cost; Johns' family has no window edge because it has no window.
  - Neither touches the sign at T > ½log5.

**Verdict:** parallel and not overlapping, with no error found. Interest: low–medium (tool (a)).

## 2. L57 — Eberwein (and Lemke)

Statements as read in §2 and §7 of the PDF, compared with our walls:

| Eberwein result | statement and method | our counterpart | relation |
|---|---|---|---|
| §2 inertia identity (Thm) | W = P − I, P = ab^T + ba^T (polar, rank 2). With S = [[α, γ−1], [γ−1, β]] built from I⁻¹: ν(W) = π(I) + ν(S) − 1. Method: Haynsworth on a block matrix. Corollary: W ≥ 0 ⟺ π(I) ≤ 1 and Δ_L = α − \|1−γ\| ≥ 0 | phase 156 "converse = 2×2 polar-capacity condition"; phase 155 Schur reduction; Theorem P (n₋ ≤ 5/7/8); R186_044 Thm 2 (exact Schur, ρ_T) | **Duplicate** of our 2×2 polar Schur reduction, in different coordinates (polar block eliminated instead of the V^P head). It is not stronger. Its π(I) ≤ 1 restates W11/prop:archneg (the archimedean part is indefinite) from the other side |
| 7.1 blind zone (Thm) | If W_{Z₀} ≥ μ‖f‖², then adding an off-line quadruple of depth δ costs at most κ(δ,L) = 2sinh(δL)/δ − 2L ≈ δ²L³/3, uniformly in height. Method: Cauchy–Schwarz. PROVED, and the proof is correct | M_m falsifier (κ(M_m) = κ(ζ)+4m); Theorem M (λ_A ≤ exp(−e^{(2−ε)T})) | **Consistent and weaker.** It is a quantitative version of the fact that a window form with margin μ cannot see shallow quadruples. Combined with Theorem M, the blind depth shrinks doubly-exponentially. It does not contradict anything. It adds an explicit δ₀(L) formula we did not record. Usable as a lemma for M_m-type falsifiers (window-uniform depth bound) |
| 7.2 height criterion (Thm + NUMÉRICO) | λ_T ≤ ¼ ⟹ W_{Z₀∪Q} ≥ 0 | R186_046 Thm X (prolate resolution π/T); W-loc | Weaker / orthogonal. The numerics are Galerkin lower bounds and not certified |
| 7.3 Kreĭn indistinguishability (Cor) | W ≥ 0 on window L ⟹ the window data extend to a positive measure, so procedures that read Λ(n ≤ e^L) cannot separate | Paper 47 round 5 (Kreĭn indeterminacy), W3 (class blindness), cor:void, thm:finmod, comb models (156) | **Duplicate** of our Kreĭn/comb-model wall. Ours is stronger: cor:void and finmod hold for every window and for prime-side hypotheses |
| 7.4 no exclusion regions (Prop) | second-order cancellation −δ² | W2/Theorem M; R164_601 (M_m windowed satisfies the tail sign inequality) | Duplicate in spirit (no margin to convert); weaker |
| 7.5 finite jets (Prop) | Hermite multiplier Ξ·R | W-jet (R166_201), W5, W8/finZ | Duplicate; folklore |
| 7.6 CS inflation (Prop) | Conrey–Ghosh–Gonek pairing ratio is unbounded | none (not our arena) | New to the index; irrelevant to row D |
| 7.7 Selberg identity is blind (Prop, CITED DMV) | Beurling DMV | falsifier "Beurling DMV", W3 | Duplicate |
| 7.8 two-sided barrier | DH / Beurling / Epstein / F_q table | W9 (T1/T2), §4 falsifier table | Duplicate, and weaker (no method theorem) |
| 7.9 no tensor square; 7.10 geodesic lengths ≠ log p; 7.11 de Bruijn–Newman | elementary / CITED Rodgers–Tao | W10 (no MW-5 object); W5 | Consistent; 7.9 and 7.10 are new small no-gos for "Deligne tensor power" and "arithmetic-surface trace formula" routes, both already dead in our map (Deligne route, phases 149–150; W10) |
| §8.1 archimedean+pole indefinite (NUMÉRICO); §8.2 positivity is all-or-nothing over prime teams (NUMÉRICO) | eigenvalues | prop:archneg (PROVED, negative from T = 0.4608), W11, Theorem X/W-loc | Ours is PROVED and stronger. 8.2 is numerical evidence for the same phenomenon as W-loc/W-tail (no proper sub-team carries the sign). Consistent |

- **Nothing contradicts our walls.** The only items not already present are 7.1's explicit blind depth and 7.6/7.9/7.10, which lie outside our arena.
- None of Eberwein's no-gos is stated as an impossibility *within a declared method class* acting on the sign of λ_A. They are detection/visibility statements about planted worlds, so none of them closes any route in our sense.
- **Lemke:** the private-communication construction (least-eigenvalue subtraction, oblique projection) is the CCM ε_N-shift mechanism. It produces real spectrum by construction and carries no sign. Same verdict as for L35, Thm 1 below. No text available; the label stays unverified.

## 3. L35 — Franchi Viceré, semilocal spectral descent: the flaw

The chain is Thm 1 (CCM 2025 Thm 1.1: σ_S(N,λ) self-adjoint for the inner product QW_λ^N − ε_N⟨·|·⟩, hence real "spectral zeros") → Thm 2 (QW_λ^N(g∗g♯) = Σ g̃(ρ_k) g̃(1−ρ̄_k) = Σ\|g̃(ρ_k)\|² ≥ 0) → Thm 3 (Fejér truncation g_N → g, giving QW_S(g) ≥ 0) → Thm 4 (S ↑ all places) → Weil.

**Flaw 1 (fatal, Thm 2). The ε_N-shift is dropped.**
- ε_N is *defined* as the least eigenvalue of QW_λ^N. So QW_λ^N − ε_N is PSD by definition, and the reality in Thm 1 is a property of that shifted form only.
- Reality of the zeros of the minimal-eigenvector transform does not give QW_λ^N ≥ 0. Indeed QW_λ^N ≥ ε_N, and the sign of ε_N is exactly the open question.
- The displayed "arithmetic–spectral identity" is a finite-dimensional form written as a sum over the spectral zeros of a different operator. Neither CCM §5 nor Connes 1999 Thm 4 contains it in that form. Connes' semilocal trace formula has a remainder, and that remainder is where the sign lives: our phase 183, E_S = Son + R_{S,T}, with n₋(R_{S,T}) = ∞ for T > ½log2 (R183_018 Thm 5.1, R183_019 Thm 4.1).
- So Thm 2 asserts as an identity precisely the step that the phase-183 Sonin NO-GO shows carries no sign.

**Flaw 2 (fatal, Thm 3/4). "QW_S ≥ 0 for each finite S" is false as stated.**
- Take S = {∞}. Then QW_S is the archimedean+polar form, and Paper 47 prop:archneg (PROVED) exhibits a negative vector from T = 0.4608. So a uniform-in-S positivity of semilocal forms is refuted by a single explicit vector. Eberwein §8.1–8.2 report the same numerically.
- Thm 3 also conflates S (places) with the cutoff λ (all primes ≤ λ² enter QW_λ). The "stabilization for λ > M/ε" is only the finite-support statement for fixed g, and it is true but carries no sign.
- In our terms, Theorem X (R186_046) shows that new primes must cancel σ at resolution π/T. The sign lives in the coupling and the complement, not in any S-local block (W-loc, R186_044 Thm 2). Descent "S finite ⟹ S = all" therefore has nothing to transport.

**Flaw 3 (minor).** The numerics (Mathematica, S = {2,3,5,∞}, 4 test functions, 30 zeros) are reported as verifying "Class A" theorems. A form evaluated with zeros on the line is non-negative by construction, so the check is circular.

**Verdict:** NO-GO. The precise failure point is Thm 2: the PSD of QW − ε_N is substituted for the PSD of QW. The failure falls under the phase-183 Sonin wall, prop:archneg, and W-loc.

## 4. New index rows (for 05_LITERATURE.md)

| ID | Route | Tool family | Where | Outcome | Why |
|---|---|---|---|---|---|
| L55-A | Johns: positive solutions of the EF, LP slack κ* | Delsarte/OPS linear programming, Carathéodory + Helly duality, Hermite interpolation at prime powers, computer-assisted certificates | zenodo 23238720; github nic410/zeta-positive-solutions (§2 read) | PARALLEL, no error found in §2; κ* ≤ 1.43·10⁻¹⁰⁶⁰ and κ* ≥ −2.71·10⁻³ CITED (not rerun) | A linear, window-free problem with the polar term inside Arch. Its gap slice is the complete-form T ≤ ½log2 statement already in Paper 47. Duality parallels thm:D1; zero-vanishing certificates parallel thm:Z; κ* ≠ our κ_⋆ (name clash). Usable: the primal-pair floor method |
| L55-B | Primal admissible-pair floor for λ_A (from L55) | explicit positive representing pair at a shifted archimedean datum | idea only | OPEN (candidate tool) | Paper 47 has only dual certificates; a primal floor is a missing direction. It must be checked against W4 (orientation) before building |
| L57-A | Eberwein inertia identity ν(W) = π(I)+ν(S)−1 | Haynsworth inertia, 2×2 polar fiber | zenodo 23177438 §2 | DUPLICATE (PROVED, correct) | = phase-156 2×2 polar-capacity converse / phase-155 Schur / R186_044 Thm 2 in other coordinates; π(I) ≤ 1 ↔ prop:archneg/W11 |
| L57-B | Eberwein blind zone κ(δ,L) = 2sinh(δL)/δ − 2L | Cauchy–Schwarz on the quadruple contribution | zenodo 23177438 §7.1 | PROVED, consistent; weaker than M_m + Theorem M | A new explicit depth formula. It can serve as a lemma for M_m-type falsifiers; it is not a route to the sign |
| L57-C | Eberwein §7.3–7.5, 7.7–7.8 (Kreĭn indistinguishability, no exclusion, finite jets, Selberg blind, two-sided barrier) | Kreĭn extension, Hermite multipliers, Beurling DMV | §7 | DUPLICATE of W3, cor:void, finmod, W-jet, W5, W8, W9, Beurling-DMV falsifier | Our versions hold at every window and inside method classes, so ours are stronger |
| L57-D | Eberwein §7.6, 7.9, 7.10 (CGG inflation, no Selberg tensor square, geodesic lengths ≠ log p) | elementary | §7 | NO-GO (outside row-D arena) | They kill the tensor-power and arithmetic-surface trace-formula routes, which were already dead under W10 |
| L57-E | Lemke "finite real spectrum" | least-eigenvalue subtraction + oblique projection | private comm., cited in arXiv 2609.04908 | UNVERIFIABLE (no text); structurally the CCM ε_N shift, so no sign | The L57 corpus pointer 2609.33692 is Freiberg (prime biases), so the entry is MISATTRIBUTED and must be corrected |
| L35-A | Franchi Viceré semilocal spectral descent | CCM spectral reality, Connes semilocal trace formula, Fejér truncation, S-exhaustion | zenodo 19546495 (PDF read) | NO-GO / ERROR | Thm 2 replaces PSD(QW − ε_N) (true by definition) with PSD(QW). Its "sum of squares" identity drops the semilocal remainder, which has n₋ = ∞ (phase-183 Sonin NO-GO). "QW_S ≥ 0 ∀S" is refuted at S = {∞} by prop:archneg. The descent has no sign to transport (Theorem X, W-loc) |
