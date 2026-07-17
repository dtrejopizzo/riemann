# No-Go List: Everything That Failed or Hit a Wall

**Author:** David Alejandro Trejo Pizzo · `dtrejopizzo@gmail.com`
**Created:** June 2026
**Updated:** 2026-07-17
**Purpose:** A permanent reference. Before attempting any new attack on RH, consult this list.
If the proposed approach is here, do not try it again. If something new fails, add it.

**Structure:** Each entry has (a) what was attempted, (b) why it failed / the precise
obstacle, (c) where it is documented.

---

## I. APPROACHES THAT FAILED OR WERE REFUTED

### I.A — ω-class program (Arc A)

**[NG-A1] Bound B(N) ≤ N^ε implies Lindelöf via the chain**
- Attempted: prove Lindelöf (and contribute to RH) by bounding the ω-class cross sum B(N) ≤ N^ε.
- Why it fails: the target was STRONGER than Lindelöf. Proving B(N) ≤ N^ε requires Lindelöf as a hypothesis. Circular.
- File: `MASTER-PLAN.md §Part 0`; `01-context` Research Program summaries.

**[NG-A2] Extrapolating the exponent α_B toward 0**
- Attempted: extrapolate that α_B → 0 from 4 data points (N ≤ 1.5×10⁵), implying Lindelöf.
- Why it fails: α_B ≈ 0.42 vs the Bourgain threshold < 0.31. The trend does not cross the threshold. Four data points are insufficient. At the k=2→3 transition the trend reverses.
- File: `MASTER-PLAN.md §3.1`

**[NG-A3] Unconditional cross-covariance as an RH signal**
- Attempted: use the measured anti-correlation between ω-classes as an unconditional statement toward RH.
- Why it fails: the Montgomery–Vaughan theorem (MVT) shows unconditional cross-covariance ≈ 0. The anti-correlation is only measurable conditionally (at peaks). MVT destroys any unconditional claim about cross-interactions.
- File: Research Program summaries.

**[NG-A4] The parity problem (sieve methods) for separating ω-classes**
- Attempted: use the Selberg/Bombieri sieve to distinguish ω-even from ω-odd and obtain a useful bound for RH.
- Why it fails: the parity problem blocks all standard sieves from distinguishing ω(n) mod 2. It is a fundamental obstruction intrinsic to sieve theory, not a technical gap.
- File: Research Program summaries.

**[NG-A5] Li / Jensen / GORZ / Baez-Duarte coefficients as a proof path**
- Attempted: verify λ_n > 0, Jensen/GORZ hyperbolicity, the Baez-Duarte criterion d=0, and treat them as progress toward RH.
- Why it fails: ALL are reformulations of RH, not proof paths. Verifying them numerically for finite N is circular (they are equivalent to RH). Proving them would require proving RH.
- File: Research Program summaries; `MASTER-PLAN.md §Part 4`

**[NG-A6] The r4/r5 phase transition as an RH-relevant result**
- Attempted: claim that the transition N_c ≈ 1.18×10⁵ in ω-class geometry constitutes new insight toward RH.
- Why it fails: the phase-transition headline was refuted by canonical re-verification. Reframed to the weaker, honest result (ζ MORE constructive at peaks, no transition).
- File: memory `project-p5-transition-refuted.md`

**[NG-A7] TDA (Topological Data Analysis) as an RH detector**
- Attempted: use persistent homology (H0, H1) of the zero set to distinguish ζ from L_DH.
- Why it fails: H0 is δ²-insensitive (does not detect the size of the off-line shift); L_DH is not a topological outlier with matched sample size; H1 carries no signal (p ≈ 0.48 — not significant). The instrument cannot detect off-line zeros.
- File: `PLAN-RH-MAXIMAL.md §1`

**[NG-A8] λ_min(ζ) ≈ 0.866 as evidence of Weil positivity**
- Attempted: interpret λ_min(Q) ≈ 0.866 > 0 for ζ as evidence of the Weil positivity condition.
- Why it fails: pure PSD artifact. The zero-side Gram matrix is positive by construction. Only the full form Q (prime side + zero side) carries information. A one-sided form is trivially positive.
- File: `PLAN-RH-MAXIMAL.md §1`

---

### I.B — Lower bounds for b_j (Phases 24–25)

**[NG-B1] 15 classical mechanisms for lower bounds on b_j**
- Attempted: Korobov–Vinogradov, Selberg density, Levinson–Conrey proportions, Deuring–Heilbronn repulsion, Beurling–Nyman criterion, Bohr almost-periodicity, Baker's theorem, Weil–Deligne function fields, Turán powers, Littlewood omega theorems, large sieve, Montgomery pair correlation, de Branges chain condition, Selberg trace formula, Weil positivity.
- Why it fails (universal): arithmetic information from Re(s) > 1 does NOT propagate to the critical strip Re(s) ∈ (1/2, 1). Each mechanism either (a) gives upper bounds on b_j, or (b) applies to the wrong region, or (c) counts off-line zeros in aggregate but does not bound individual shifts, or (d) is circular.
- File: `phase-25/01-audit-classical.md`

**[NG-B2] Korobov–Vinogradov zero-free region for a lower bound on b_j**
- Attempted: use the KV result (no zeros with Re(s) > 1 − c/(log|t|)^{2/3}…) to bound b_j from below.
- Why it fails: this gives b_j ≤ 1/2 − c/(log γ_j)^{2/3} — an UPPER bound. It describes how close zeros get to Re(s) = 1, not how far they move from Re(s) = 1/2. **Completely wrong direction.**
- File: `phase-25/01-audit-classical.md §Mechanism 1`

**[NG-B3] Deuring–Heilbronn repulsion for b_j**
- Attempted: use the repulsion of zeros near Re(s) = 1 to force zeros off the critical line.
- Why it fails: D-H operates near Re(s) = 1 (Siegel zeros). The Paley–Wiener barrier (Phases 22–23) shows the arithmetic machinery does not reach Re(s) ∈ (1/2, 1). No "anti-Siegel" repulsion away from the critical line is known.
- File: `phase-25/01-audit-classical.md §Mechanism 4`

**[NG-B4] Beurling–Nyman criterion for a bound on b_j**
- Attempted: bound the Beurling–Nyman distance d from below in terms of b_j.
- Why it fails: d > 0 under Hypothesis D, so this is circular. Bounding d > F(b_j) from below is equivalent to bounding b_j from below — the exact problem one is trying to solve.
- File: `phase-25/01-audit-classical.md §Mechanism 7`

**[NG-B5] de Bruijn–Newman connection as a lower bound on b_j**
- Attempted: use the inequality Λ ≥ b_j²/2 to get a lower bound on b_j from the constant Λ.
- Why it fails: the direction is **inverted**. The inequality gives b_j ≤ √(2Λ) — an UPPER bound. For a lower bound we would need an upper bound on Λ; the only known bound Λ ≤ 1/4 gives only b_j ≤ √(1/2), trivial.
- File: `phase-25/02-deBruijn-Newman.md`

**[NG-B6] Turán inequalities for ξ₀ as constraints on b_j**
- Attempted: use the factorization ξ = ξ₀ · P_{4m} (under Hypothesis D) and the Turán inequalities for ξ₀ ∈ LP to constrain b_j.
- Why it fails: completely circular. The inequalities T_n^{(ξ₀)} ≥ 0 are SATISFIED for every b_j > 0 under Hypothesis D — they are a consequence of ξ₀ ∈ LP, which is exactly what Hypothesis D asserts. They impose no constraint on b_j.
- File: `phase-25/03-krein-lp.md §Lemma 25-C.5`

**[NG-B7] Baker's theorem (linear forms in logarithms) for b_j**
- Attempted: apply Baker's bounds for linear forms in logarithms to constrain the zeros.
- Why it fails: Baker applies to logarithms of ALGEBRAIC numbers. The zeros of ζ are presumably transcendental and their imaginary parts γ_j have no known algebraic structure. **Wrong category of objects.**
- File: `phase-25/01-audit-classical.md §Mechanism 10`

**[NG-B8] Montgomery pair correlation as a b_j detector**
- Attempted: use distortion of the pair correlation of on-line zeros to bound b_j.
- Why it fails: pair correlation describes spacings between zeros ON the critical line. Off-line zeros do not appear in the pair correlation of on-line zeros. No signal.
- File: `phase-25/01-audit-classical.md §Mechanism 15`

---

### I.C — Local-global principle (Phase 27)

**[NG-C1] Factorization of the Weil form Q = Q_∞ × ∏_p Q_p (Hasse–Minkowski)**
- Attempted: factor Q over primes, use local positivity Q_p ≥ 0 (from Weil–Deligne for curves over F_p) to conclude Q ≥ 0 globally.
- Why it fails: TWO walls.
  - **Wall A:** Q_zero = Σ_ρ ĥ(ρ) does NOT factor over primes. The zeros of ζ are global objects — no prime "owns" a zero. There is no analogue of "Frobenius at a prime" for ζ/Q.
  - **Wall B:** even with a factorization, Hasse–Minkowski does not apply to infinite-dimensional Hermitian forms.
- File: `phase-27/02-C-wall-analysis.md`

**[NG-C2] Phase 27 as an alternative route to Phase 26's V.2**
- Attempted: use adelic methods (Grössencharacter theory) to exclude non-unitary characters from the spectrum of H_C without resolving V.2 directly.
- Why it fails: Theorem 27-B.4 proves that the Phase 26 obstacle (V.2: x^{b_j+iγ_j} ∉ L²(C_Q)) and the Phase 27 obstacle (27-B: |x|^{b_j+iγ_j} ∉ Ĉ_Q^unit) are THE SAME obstacle in two languages. Phase 27 is not an alternative route.
- File: `phase-27/03-verdict.md §2`

### I.C.bis — Phase 26: distributional eigenvectors

**[NG-C3] Explicit eigenvectors f_j(x) = x^{b_j+iγ_j} in L²(C_Q)**
- Attempted: prove H_C has at least κ complex eigenvalues by finding explicit eigenvectors f_j.
- Why it fails: f_j(x) = x^{b_j+iγ_j} is NOT in L²(C_Q). The L² norm is ∫|x^{2b_j}|dx/x = ∫x^{2b_j-1}dx = ∞. The eigenvectors are distributions, not L² vectors. Q(f_j, f_j) is formally divergent.
- File: `phase-26/01-attack-V2.md`

---

### I.D — Phase 28: four fronts

**[NG-D1] Front D as a minimization problem (wrong direction)**
- Attempted: formulate RH as b_j = 0 being the global MINIMUM of some energy E_arith in the transverse direction.
- Why it fails: Theorem 2 of `06-curvature-xi.md` proves that under RH, σ ↦ log|ξ(σ+iγ)| is STRICTLY CONVEX at σ = 1/2. So the Weil form Q is locally MAXIMIZED (not minimized) at b_j = 0. **The minimization formulation was wrong.**
- File: `phase-28/06-curvature-xi.md §5`

**[NG-D2] Question 28.1 — log-concavity in the σ direction**
- Attempted: prove that σ ↦ log|ξ(σ+iγ)| is concave in σ, as a sufficient condition for RH.
- Why it fails: the answer is NO under RH. Theorem 2 of doc 06 establishes that under RH the curvature is C(γ) = Σ_ρ 1/(γ-γ_ρ)² > 0 — strictly positive, i.e. CONVEX, not concave. **The right direction is t-concavity, not σ-concavity.**
- File: `phase-28/06-curvature-xi.md §5 (Proposition 1)`

**[NG-D3] Arithmetic sector G_ζ controllable without RH**
- Attempted: prove G_ζ(t) = d²/dt² log|ζ(1/2+it)| > −G_ana(t) for all t > t_* using only the Euler product and the functional equation, without assuming RH.
- Why it fails: Proposition 1 of doc 08 proves this inequality is EQUIVALENT to RH. The Euler product converges absolutely only for Re(s) > 1; on the critical line convergence is conditional. Two layers: (a) G_ana(t) < 0 for t > t_* (the analytic sector alone does not control G); (b) controlling G_ζ at σ = 1/2 requires information about the distribution of zeros, which IS RH.
- File: `phase-28/08-decomposition-sectors.md §Proposition 1, §6–7`

**[NG-D4] Anticommutation via the Fourier transform for the η-invariant (Front B)**
- Attempted: use F as an involution K anticommuting with T_0 (K T_0 K^{-1} = −T_0), forcing η(T_0) = 0, then κ = 0 via APS.
- Why it fails: the functional-equation symmetry (s ↦ 1−s) PRESERVES eigenvalues of T_0 rather than negating them. The functional-equation involution J satisfies J T_0 J^{-1} = T_0 (symmetry, not antisymmetry). The Fourier anticommutation condition Q(f,g) + Q(f̂,ĝ) = 0 is open and unresolved.
- File: `phase-28/02-front-B.md §4–5`

---

### I.E — General program (Phases 4–9 of the main arc)

**[NG-E1] Reflection positivity per place (OS moonshot, Phase 6)**
- Attempted: factor the Weil form as a product of positive-definite forms per prime, use OS reconstruction to obtain H ≥ 0.
- Why it fails: COMPUTED AND REFUTED. The local integral form ∫|ψ̂|² G_p with G_p(r) = (2 log p)/(p|1−z|²)(√p cos(r log p) − 1) is INDEFINITE: G_p(0) > 0 but G_p(π/log p) < 0. Verified for p = 2, 3, 5, 7. Per-place reflection positivity FAILS. Positivity is a cross-place phenomenon.
- File: `00-MAP.md §Phase 6`

**[NG-E2] Scalar λ_min as the principal non-tautological invariant**
- Attempted: use the scalar minimum eigenvalue λ_min(Q) as the principal discriminator between ζ and L_DH.
- Why it fails: λ_min is quasi-tautological (= 0 under RH by Theorem C of P8). The genuine non-tautological invariant is the per-prime anatomy {R_p}. Retired as the principal invariant.
- File: `00-MAP.md §M5`

**[NG-E3] Global Cauchy–Schwarz bound for the quadratic form E_g**
- Attempted: bound E_g = Σ_γ|F(γ)|² − ρ∫|F|² using ‖D_T‖_{L²} = V(d,T) ~ T log T via C-S.
- Why it fails: the bound is VACUOUS — it loses localization entirely. The global C-S is too coarse and provides no useful control of the quadratic form near off-line zeros.
- File: `00-MAP.md §Phase 4 ladder`

**[NG-E4] Point-to-point routes for RFB (Schur/Gram/Jaffard/interpolation)**
- Attempted: prove the relative bounded form |𝔱₋(g)| ≤ a·𝔱₊(g) + C‖g‖² (a < 1) via point-to-point operator bounds.
- Why it fails: all pay the price P = ρℓ → ∞. Oversampling is FORCED (ℓ ≥ 1/2 forces P → ∞), making all point-to-point routes vacuous.
- File: `00-MAP.md §Phase 4 ladder`

**[NG-E5] Hilbert–Pólya via OS reconstruction "for free"**
- Attempted: from OS reflection positivity + the reconstruction theorem, claim H ≥ 0 automatically.
- Why it fails: RETRACTED. The two-point function is oscillatory, NOT OS-decreasing. The OS reconstruction theorem requires exponential decay; oscillatory behavior disqualifies it.
- File: `00-MAP.md §Phase 6 (S1.4 retracted)`

**[NG-E6] Reduction S2f §1 — "envelope ≥ pointwise comb" implies RH**
- Attempted: reduce RH to the pointwise inequality Ω_∞(r) ≥ (Σ_p G_p)_reg(r).
- Why it fails: the reduction is FLAWED. The comb Σ_p G_p is DISTRIBUTIONAL: it equals Ω_∞ − 2π Σ_ρ δ_{γ_ρ}. "Envelope ≥ comb pointwise" cannot be made precise by taking φ̂ → δ (invalid limit).
- File: `00-MAP.md §Phase 6 (S2f-PROGRESS-HONEST)`

**[NG-E7] L_DH as a reproducible quantitative benchmark**
- Attempted: use L_DH (the Davenport–Heilbronn L-function) as a rigorous benchmark with reproducible λ_min ≈ −9×10⁴.
- Why it fails: the von Mangoldt function of L_DH ("log of a sum of L-functions") is not reproducible from public definitions. The v7 value is not recoverable rigorously. L_DH downgraded to a qualitative control only.
- File: `PLAN-RH-MAXIMAL.md §1bis`

---

## II. STRUCTURAL WALLS (OBSTRUCTIONS THAT REAPPEAR ON EVERY FRONT)

These are not "failures" of specific approaches — they are fundamental mathematical obstructions
that appear under every disguise.

### Master Wall (five names for a single obstruction)

**[MW-1] Weil positivity wall**
W(f ★ f̃) ≥ 0 is EQUIVALENT to RH (Weil 1952). Proving positivity requires exactly what it means
to prove RH. It appears on every front.
- Aliases: Wall A (Phase 27), Wall W4-RSRP (Phase 25), arithmetic wall (Phase 28), spectral-uniformity gap (PLAN-RH-MAXIMAL §5).

**[MW-2] Arithmetic-propagation wall (the central one)**
The Euler product ∏_p(1−p^{-s})^{-1} is valid only for Re(s) > 1. Arithmetic information from
Re(s) > 1 does NOT propagate to Re(s) ∈ (1/2, 1). The zeros of ζ are global objects: no Euler
factor ever vanishes, so no prime "owns" a zero. This blocks local-to-global arguments that
would constrain off-line zeros.
- Phase 25: W4-RSRP; Phase 27: Wall A = the Connes–Consani arithmetic site; Phase 28: conditional convergence of G_ζ at σ = 1/2.

**[MW-3] Hasse–Minkowski wall in infinite dimension**
Even if local forms Q_p existed, there is no Hasse–Minkowski theorem for infinite-dimensional
Hermitian forms. Local positivity does not imply global positivity in infinite dimension.
- File: `phase-27/02-C-wall-analysis.md §5`

**[MW-4] Hilbert–Pólya wall (wrong sign)**
Every unconditional tool on ζ gives a LOWER bound on positivity. RH is an UPPER restriction (we
need λ_min(Q) ≥ 0). Positivity tools give lower bounds; RH needs upper bounds. Systematically
the wrong sign. Confirmed in 8 independent paradigms: explicit-formula/Kreĭn, per-place,
Carleson, pair correlation, Connes prolate, heat flow, cohomological Hodge, hyperbolicity.
- File: `00-MAP.md §Phase 9`

**[MW-5] Connes–Consani arithmetic-site wall**
The local-global factorization Q = Q_∞ + Σ_p Q_p requires: (1) a cohomology H¹(Spec ℤ, F); (2)
an arithmetic Frobenius φ_p at each prime; (3) a positive intersection form. This is exactly the
Connes–Consani "arithmetic site" program, unfinished after decades.
- File: `phase-27/02-C-wall-analysis.md §Proposition 27-C.5`

**[MW-6] Uniform spectral-gap wall**
The missing inequality: sup_{X≥X_0} |λ_min(Q_X) − λ_min(Q_∞)| ≤ ε(X_0) → 0. This uniform
spectral control is EQUIVALENT to RH (Connes/Bombieri/Lagarias positivity). It can only come
from a structural reason why positivity must hold.
- File: `PLAN-RH-MAXIMAL.md §5 and §8`

---

## III. IDENTIFIED CIRCULAR ARGUMENTS

**[CIR-1]** Selberg density as a bound on b_j: the density theorem bounds the COUNT of off-line zeros in aggregate, not individual b_j. A single zero with b_j = e^{-10^{100}} is compatible with all density theorems.

**[CIR-2]** Levinson–Conrey proportions as a bound on b_j: on-line proportions (41% on the line, Bui-Conrey-Young 2011) say nothing about the shift of zeros that are off the line.

**[CIR-3]** Beurling–Nyman distance d as a lower bound on b_j: under Hypothesis D, d > 0, but bounding d > F(b_j) is equivalent to bounding b_j — the problem one is trying to solve.

**[CIR-4]** Turán inequalities for ξ₀: they are a CONSEQUENCE of Hypothesis D, not additional constraints on b_j.

**[CIR-5]** Bounds ψ(x) − x = O(x^{1/2+ε_0}): ε_0 < min b_j would be a lower bound for b_j, but that bound on ψ is equivalent to zero-localization control — circular.

**[CIR-6]** Li / Jensen / GORZ / Baez-Duarte coefficients as "verification" of progress: all equivalent to RH. Verifying them numerically for finite N verifies nothing about RH asymptotically.

**[CIR-7]** Compatibility theorem (Phase 23/24): verifying that the KV and structure-function bounds are compatible does not constrain b_j — it only confirms the bounds are consistent with any b_j ∈ (0, 1/2).

**[CIR-8]** F3 (chaos incompatibility): the claim "depth = O(log log γ_j)" was INCORRECT. The KV bounds only bound b_j from above, giving no upper bound on |log b_j|. The incompatibility cannot be established in either direction.

---

## IV. CORRECT RESULTS (FOR REFERENCE)

These are correctly proved results — do not retry them unnecessarily, but cite them as a base.

| Code | Result | Reference |
|------|--------|-----------|
| [OK-1] | Forced negativity: an off-line zero at distance δ forces λ_min(Q) ≤ −c(δ, σ, J). | `PLAN-RH-MAXIMAL.md §1bis` |
| [OK-2] | Unconditional truncation control: η(X) ≈ A·exp(−α log²X), α ≈ σ²/8. | `PLAN-RH-MAXIMAL.md` |
| [OK-3] | Unconditional detector lemma (OK-1 + OK-2). | P7 |
| [OK-4] | DH null result: no power-law growth up to N=10⁹; onset bound N* ≳ 10¹⁴. | P3 |
| [OK-5] | LP/Turán reformulation of MW-2 (Theorem 25-C.6): an algebraic question about the coefficients c_n of ξ(1/2+it). | `phase-25/03-krein-lp.md` |
| [OK-6] | Kreĭn–de Bruijn–Newman connection: under Hypothesis D, Λ ≥ b_j²/2. | `phase-25/02-deBruijn-Newman.md` |
| [OK-7] | Second-variation formula: δ²_b Q(f,f) = −8Σ_j c_j²[Re(ĥ''(ρ_j)ĥ̄(ρ_j)) + |ĥ'(ρ_j)|²]. | `phase-28/05-second-variation.md` |
| [OK-8] | Curvature criterion: RH ↔ C(γ) = Σ_ρ 1/(γ−γ_ρ)² > 0. | `phase-28/06-curvature-xi.md` |
| [OK-9] | Sector decomposition: G_poly(t) = 2(1/4−t²)/(t²+1/4)², G_Γ(t) = −(1/4)Re ψ^{(1)}(1/4+it/2). | `phase-28/08-decomposition-sectors.md` |
| [OK-10] | The four fronts of Phase 28 (A, B, C, D) are the same problem: ξ(1/2+it) ∈ LP. | `phase-28/07-lp-class-rh.md` |
| [OK-11] | No-go on the zero side (Theorem C, P8): the zero side cannot decide the sign. | P8 |
| [OK-12] | Lefschetz dichotomy: the ample class cannot be supplied by Spec ℤ. | P21 |

---

## V. THE SINGLE MASTER OBSTRUCTION

In every phase, the same obstacle appears in a new disguise:

- **Phase 25:** Can arithmetic information from Re(s) > 1 propagate to Re(s) ∈ (1/2, 1)?
- **Phase 27:** Can Q = Q_∞ + Σ_p Q_p be factored, and does local positivity imply global?
- **Phase 28:** Can G_ζ(t) be controlled without assuming RH?
- **Phases 4–9:** Is the operator T = A*A for A independent of the zeros?
- **PLAN-RH-MAXIMAL:** Is sup_X |λ_min(Q_X) − λ_min(Q_∞)| → 0?

These are the same question. The wall has been named precisely from 7 independent directions.

---

## VII. ACTIVE CANDIDATES (not refuted, not on the failure list)

These are ideas that the recent literature (2020–2026) identifies as genuinely open and
non-circular, per deep research from June 2026.

**[CAND-1] Zeta Spectral Triples — Connes, Consani, Moscovici (2025–2026)**
- What it proposes: build self-adjoint operators H_x via finite Euler products (primes p ≤ x) using Carathéodory–Fejér rigidity to guarantee self-adjointness by construction (without needing to prove Weil positivity). The spectra of H_x reproduce the zeros of ζ with extraordinary precision (error ≈ 10⁻⁵⁵ for the first zero using only 6 primes).
- Open question: do H_x → H_∞ converge in an appropriate operator sense, with sp(H_∞) = {γ_ρ}?
- Key difference from prior approaches: the operators are self-adjoint BY CONSTRUCTION (no quadratic-form positivity to prove). The obstacle is operator convergence, not positivity.
- References: arXiv:2511.22755 (November 2025); arXiv:2602.04022 (February 2026, Connes's "Letter to Riemann").
- Status: open, not refuted, extraordinary numerical evidence. **Candidate explored from Phase 29 onward (the CCM thread).**

**[CAND-2] Weng Non-Abelian Zeta Functions (function field) — Shi Zhan (2025)**
- What it proposes: the non-abelian zeta functions of curves over finite fields (associated with moduli spaces of vector bundles) satisfy RH. Proved for genus 2 as rank n → ∞ (arXiv:2511.06729).
- Difference: not the standard function-field analogy — a new family of zeta functions with their own RH, recently proved.
- Relevance to classical ζ: a testing tool for the program. The jump to ℤ requires moduli-space geometry over ℤ (no known analogue of the Weil conjectures).
- Status: proved for finite fields; ℤ open.

**[CAND-3] Lee–Yang spin models with ζ as a partition function**
- What it proposes: if there existed a ferromagnetic spin system with interactions that (a) satisfy the Lee–Yang theorem conditions and (b) have ζ(s) as a partition function, then the zeros of ζ would lie on the critical line.
- Status: the appropriate model is unknown; Knauf's version (1999) does not satisfy the Lee–Yang conditions. Open, but no active candidate.

---

## VIII. NEW FAILURES (post-Phase-28)

**[NG-F1] Multiplicativity discriminant in the localized Weil form (Phase 60)**
- Attempted: isolate the arithmetic invariant controlling the Weil sign by comparing ζ (Euler) vs non-multiplicative controls in the localized form — using L_DH as an explicit violator. Thesis: "multiplicativity (the Euler product), not zero location, controls the sign."
- Why it fails (two sides, refuted numerically, reproducible code in `phase-60-discriminant/`):
  - **Zero side (E1):** `M_zeros` is a function of the zero multiset only. Every on-line configuration sits at the floor ≥ 0 independent of the L-function. Separating ζ from L_DH here = separating by off-line zeros = location = circular. Blind to multiplicativity.
  - **Arithmetic side (E2/E2b):** the Carleson constant C = λ_max(A^{-1/2}PA^{-1/2}) does NOT distinguish ζ (C = 1.98) from SMOOTH non-multiplicative controls (flat C = 2.44, loglin 2.11, logn 2.21). The apparent +30σ separation vs shuffle/random was an artifact of smoothness/coherence in log n, not multiplicativity. ζ is not even the most coherent.
- Structural reason: multiplicativity is fine arithmetic correlation (the scale of individual log p); the smooth envelope of the localized form integrates it out and erases it. A new variant of MW-2.
- What it does leave: a relative-discriminant instrument (fixed A, varying multiplicativity) that cancels the normalization — reusable.
- File: `phase-60-discriminant/RESULTS.md`, `00-PLAN.md`, `experiments/E1,E2,E2b`.

**[NG-F0] Phase-60-duality (wave–particle duality) — withdrawn for non-reproducible results**
- Attempted: prove H1 (uniqueness of the minimizer) / H_x→H_∞ via three axes (Krein-Connes, finite-infinite, zero partition).
- Why it is withdrawn: an audit found the cited engine did not exist on disk; the H1 verification script did `return None` and called undefined functions; the numerical tables ("|T|∈[1.33,5.52]", "gates PASS") came from no reproducible computation; the "H1 CLOSED" proofs had the error A>0,B≥0⟹A−B convex (false). The only valid result: the reduction H1 ⇔ ‖A^{-1/2}BA^{-1/2}‖<1 (correct algebra). The Krein↔Connes axis confirms they are not identifiable (K_Krein zero-dependent, K_CC zero-independent).
- Lesson: pre-registration + runnable code + a control that fails when it should (adopted in NG-F1).

> **Note on Phases 29–61 (the CCM / structural thread).** The long arc from the spectral-triple
> setup (Phase 29) through the Hodge/Spec-ℤ construction attempts (Phases 39–44), the
> Weil–Toeplitz algebra (Phase 45), and the closure audits (Phases 46–59) did **not** breach the
> Master Wall. Each construction that reached for a global positive intersection form over Spec ℤ
> landed back on **MW-5** (the Connes–Consani arithmetic site is the missing object), and each
> "average → individual" crossing attempt (Phases 49–57) landed on **MW-2 / the master
> quantifier**. The closure ledgers (Phase 59) and the open-problems inventory
> (`phase-61-open-problems/`) record the residual open inputs; none is below RH in difficulty.

> **Phase 62 — Cesàro-in-λ averaging does not relieve the boundedness wall (NG-62).**
> The last open non-RH item, Lemma 2.3.F, reduces (R10) to the boundedness `sup_λ max|A_ij| < ∞`
> of the intrinsic Jacobi of `G_λ`, whose pointwise-in-λ proof touches the wall. Phase 62 tested
> the OPEN-PROBLEMS-O11 escape — **average over λ** — hoping the arithmetic fluctuation washes out
> unconditionally. **It does not.** A zero `ρ = β+iγ` contributes `λ^{2β−1}·λ^{2iγ}` to the
> band width: on the critical line this is pure oscillation that Cesàro-averages to 0, but
> **off the line it is secular growth `λ^{2β−1}`** that no average removes, and zero-density
> estimates bound counts and imaginary parts but **not real parts**. Hence Cesàro convergence of
> `b_bulk(λ)` is **RH-equivalent**, not RH-neutral — it relocates the wall, not crosses it.
> Numerically confirmed (`03-research/phase-62-cesaro-closure/`, E90/E91): ζ's `b_bulk` is
> flat/bounded (≈0.13, slope ≈0) while the DH falsador — which has off-line zeros — grows as a
> positive power (log–log exponent ≈0.43), exactly the predicted off-line signature. **Outcome:**
> `b_bulk` boundedness is a *detector* (bounded ⟺ zeros on line), not a proof step. This lands on
> **MW-2** (the average→individual / master quantifier wall). The live lever remains the
> geometric-positivity / Hodge route (**MW-5**), not λ-averaging.

> **Phase 62 — quaternionic Hodge–Riemann positivity is present but gapless (NG-62b).**
> Pursuing the MW-5 lever, the finite-window Weil matrix of ζ was shown to carry an intrinsic
> **quaternionic Hodge–Riemann polarization** (Deninger object `J²=−1`): `A` is positive
> semidefinite on V₊ (J's +i eigenspace) for ζ, while the DH falsador and a symmetry-matched
> random control are both **indefinite** (`03-research/phase-62-cesaro-closure/`, E92→E94). The
> clearest intrinsic Weil positivity the program has found, and not trivially algebraic. **But it
> is gapless:** the V₊ spectrum is an exponential cascade `e^{−cL}` to zero (rate ≈1.40 log10/step,
> λ-independent; intrinsic, no cancellation). The crossing attempt (E95/E96) reformulated it as
> `max μ(Lprime,Larch) ≤ 1`, with ζ pinned **exactly at μ_max=1** (marginal) and DH at 6–13. All
> three Phase-62 reformulations (Cesàro `b_bulk`, Hodge–Riemann `A|V₊⪰0`, Euler `max μ≤1`) are
> **faithful but gapless marginal detectors** — the master wall (`ε₀(λ)≥0`) seen from three sides.
> Giving the margin a uniform gap = proving RH; it needs the Spec-ℤ cohomological realization
> (**MW-5**), which numerics cannot manufacture. The quaternionic HR object is the *right* object;
> the wall is unmoved. Phase 62 closed.

> **Phase 63 — MW-5 made precise: no J-linear gapped Frobenius on the ζ window (NG-63).**
> Attacking the MW-5 realization frontier head-on (`03-research/phase-63-lefschetz-realization/`),
> the function-field→RH mechanism was isolated to two ingredients: a **J-linear Frobenius** (a Hodge
> morphism) that is an **isometry of a positive-definite, gapped polarization**; positivity then
> forces eigenvalues onto `|z|=√q`. R3 (E98) verified real elliptic curves over F_q have both
> exactly (`[F,J]=0`; polarization PD with gap; `|eig|=√q` to machine precision). R1 (E97 + the
> clean engine-framework check) showed the ζ window has **neither**: the scaling operator whose
> spectrum is the zeros **anti-commutes** with the quaternionic `J` (exact, `‖[D_log,J]‖/‖D_log‖
> =2.000`; symbol odd in n) → it is complex-**antilinear**, the wrong type for a Frobenius; and the
> polarization is **gapless** `e^{−cL}` (NG-62b). These are two faces of one absence — there is no
> J-linear Frobenius isometry of a gapped polarization on the window. Such an object is the
> Frobenius of the Connes–Consani arithmetic site / Deninger cohomology (**MW-5**), which is not a
> realized object; manufacturing it is a theory problem, not computational. **This is the sharpest,
> most concrete statement of the master wall the program has produced** (direct F_q-vs-ℤ contrast).
> No proof of RH. Phase 63 closed; the realization frontier does not cross within reach of numerics.

> **[NG-67] Free-product Haar orthogonality kills the quantum q-index route (Phase 67).**
> - Attempted: construct a prime current as a genuine compact-quantum-group (CQG) coefficient
>   (quantum algebra / q-deformation, distinct from Bost–Connes KMS and Berry–Keating CCR), then
>   show it contractive by Haar/Peter–Weyl relations to force `Ω_7`.
> - Why it fails: E67.4 shows strict free-product Haar orthogonality destroys exactly the
>   arithmetic interference the route needs between prime factors — a Woronowicz/free-product
>   no-go. The group-like Euler ansatz was separately marked Bost–Connes/NO-GO (E67.2). What
>   survives (reusable, zeta-free): the q-Gamma/Plancherel archimedean sector (E67.1b/c).
> - File: `03-research/phase-67-quantum-q-index/E67_4_INTERFERENCE_NO_GO.md`,
>   `PHASE67-quantum-q-index.md`.

> **[NG-68] GLT/Toeplitz symbol positivity is gauge-fragile (Phase 68).**
> - Attempted: express the terminal defect `A_N - P_λ` as a Generalized Locally Toeplitz
>   sequence with a 2-variable symbol `κ(x,θ)`, and prove `κ≥0` everywhere (⟺ `Ω_7` ⟺ RH) by
>   structure from the archimedean Γ_q carrier and Euler/von Mangoldt data.
> - Why it fails: the position-resolved symbol is not a clean GLT sequence — the GLT
>   distribution law fails numerically (`measure{κ<0}~0.4` for ζ while the true index `ind_-=0`).
>   Symbol positivity is not a faithful detector; it is false-negative/false-positive depending
>   on gauge (confirmed E68.5–E68.6: faithful at some t0, wrong at others, because the operator
>   is not actually Toeplitz). Superseded by the exact gauge-robust index of Phase 69.
> - File: `03-research/phase-68-glt-symbol/README.md`, `02-foundations/engine/symbol_positivity_detector.py`.

> **[NG-69] The exact signed index is gauge-robust but the forcing mechanism is still absent (Phase 69).**
> - Attempted: prove `ind_-(A_N-P_λ)=0` for all N, uniformly in the gauge, by structure alone.
> - Why it fails (partial): the *detector* is now solid — `ind_-=0 ⟺ RH`, verified gauge-uniform
>   and precision-robust — but no structural proof of it was found; the terminal difficulty
>   localizes to one frequency (θ~π/2), a genuine local picture, still open.
> - File: `03-research/phase-69-exact-signed-index/README.md`.

> **[NG-66] Rank-one escape orthogonality not yet nailed; naive numeric proxy fails (Phase 66).**
> - Attempted: prove the sharp escape dichotomy for CAND-1's canonical Gram kernels — uniform
>   boundedness of `P_prim K_P P_prim` (⟹ RH) — by showing the off-line escape direction is
>   orthogonal to the pole direction H.
> - Why it fails (so far): the orthogonality claim is not yet rigorously established (genuine new
>   content, not nailed). A first numerical proxy (E110, single-height local Gram, "drop the top
>   eigenvalue" instead of the true rank-one projection `P_prim`) gave noisy, wrong-sign exponents
>   and was withdrawn as a measurement — not a refutation of D1 itself, but of the crude proxy.
> - File: `03-research/phase-66-rank-one-escape/RESULTS.md`, `PROBLEM-STATEMENT.md`.

> **Note on Phases 64–76 (the CAND-1 / ARP-P arc).** Phases 64–69 each closed a specific
> sub-mechanism for forcing `Ω_7` (Connes' relative-determinant target reclassified but unbuilt in
> 64–65; rank-one escape orthogonality open in 66; the quantum q-index closed by NG-67; the GLT
> symbol closed by NG-68; the exact signed index left gauge-robust but unforced by NG-69) without
> crossing MW-1. Phase 70 then supplied a genuine positive result — connecting `Ω_7` to the
> classical Lee–Yang/de Bruijn–Newman forcing mechanism (`RH ⟺ Λ=0`) — and Phases 71–76 built on
> it: a chain of *finite* reductions (CAND-1 stable-divisor convergence, Feshbach leakage
> calculus, the Cauchy projection gate, Hilbert eigenline cancellation, arithmetic numerator
> divisibility, and the normalized-adjugate arithmetic lock) that is real, positive progress, not
> a further no-go — see the closing note below.

> **Phases 70–76 are progress, not further no-gos.** Unlike the entries above and everything in
> Sections I–II, Phases 70 through 76 did not end in a wall. They constructed, step by step, a
> concrete finite architecture (Lee–Yang/dBN forcing → CAND-1 operator convergence → Feshbach
> leakage → Cauchy projection → Hilbert eigenline cancellation → arithmetic numerator
> divisibility → the normalized-adjugate lock) that feeds directly into the fifteen-step
> arithmetic Pick positivity (ARP-P) chain of paper **36**
> (`04-papers/36-obstruction-ledger/`), proved equivalent to RH with fourteen of fifteen steps
> closed. The remaining open input is the classical **Li–Keiper criterion**
> ($\lambda_n\ge0$ for all $n$, equivalently $\Omega_7$) — the same difficulty the whole program
> has circled since Phase 0, now reached by an independent construction and named precisely. This
> is the transition this list should not obscure: the program moved from "only walls" to "a
> complete reduction with a single, precisely named open input." That input is still, honestly,
> exactly as hard as RH.

---

## VI. PROTOCOL FOR NEW IDEAS

Before attacking any new direction:

1. **Check this list.** Is the proposed approach here, or a variant of something here?
2. **Identify which wall (MW-1 to MW-6) the idea depends on.** Any idea depending on MW-2 (arithmetic propagation) is suspect.
3. **Search the literature.** Has anyone else tried this? If so, what happened?
4. **Add new failures here** immediately when they occur.

---

*Last updated: 2026-07-17. Compiled from Phases 3–76 of the program.*
