# R154.003 — Blueprint, round 2 of phase 154.

## 0. Binding corpus facts found after round 1 (record and use)
- Phase 64 `CURVATURE-computation.md`: the prime jump generator `L v(θ) = Σ_j c_j[v(θ+a_j)+v(θ−a_j)−2v(θ)]`, `c_j = Λ(p^k)/p^{k/2}`, is the
  Beurling–Deny/Lévy form of the Weil generator; `Γ₂ ≥ 0` unconditionally (Schur, `Λ ≥ 0`); marginal (no gap at ξ = 0); §5 proposes the
  archimedean factor as the missing curvature; §8 "the one move". **Read §§4–8 and state what round 1's Theorem A adds beyond it.**
- Phase 114 D.98 `114_d_98_TATE_BOUNDARY_MARKOV_GAP_AUDIT.md`: `A_T = L_T − m_T I`, `L_T` a continuous graph Laplacian (prime edges + Gamma
  continuum); positivity ⟺ spectral gap `≥ m_T` on the Tate-orthogonal complement; Doob/killed-process routes reduce to the same gap.
  **The "killed zeta Lévy process on (−T,T)" formulation is therefore a RESTATEMENT of D.98**; do not present it as new.
- Bookkeeping (verify): with `C₀ = ψ(¼) − log π`, `⟨A_T F,F⟩ = E_Γ(F) + E_P(F) + (C₀ − 2Σ_{n<e^{2T}} w_n)‖F‖²`, `E_Γ(F) = ½∫∫|F(t)−F(s)|²K(t−s)`,
  `E_P(F) = Σ w_n ∫|F(t)−F(t−log n)|²` (F = 0 outside). Positivity ⟺ `λ^{P_T}(E_Γ+E_P) ≥ 2Σw_n − C₀` (= 9.87 at `log 2`, = 2·0.4901+5.372 = 6.35 at `½log3`).
- **New structural fact (to be proved):** `Re ψ(¼+iτ/2) − ψ(¼) = Σ_{k≥0} (τ²/4)/((k+¼)((k+¼)²+τ²/4)) = φ(τ²)` with `φ` a complete Bernstein
  function; hence the archimedean Weil process is a **subordinate Brownian motion** (Lévy density `K` is `½/sinh(u/2)`-dominated; check whether `K`
  itself is completely monotone or only the exponent is CBF — the `sech` part is not CM; resolve). Consequence (Song–Vondraček/Chen–Song comparison,
  cite exactly): killed-subordinate eigenvalues are bounded above by `φ` of the Dirichlet Laplacian eigenvalues, `λ_k(Γ^D) ≤ φ((kπ/2T)²)`; this
  gives `φ((3π/2T)²) ≈ 5.5` at `log 2`, so `λ^{P_T}(E_Γ+E_P) ≤ 5.5 + 2Σw_n·(1 − c) …` — make this exact: prove the sharpest *upper* bound on
  `λ_min(A_T)` available from subordination + `‖E_P‖`, and compare with the certified value (`≈ 10⁻⁷`). This is a consistency theorem, and it
  quantifies criticality. (FATAL check: an upper bound below 0 would contradict Paper 42 — if it happens, the bookkeeping is wrong.)

## 1. Repairs from R154_002 (binding)
R1 primitive class: `𝒦_{2T}^{prim} = {Φ ∈ 𝒦_{2T} : ∫Φ(u)cosh(u/2)du = 0 and ∫Φ(u)·u·sinh(u/2)du = 0}`; recompute Λ_T on it and re-verify Theorem A
against the `P_T` value (`9.79e-4` at `½log3`, `1.07e-7` at `log 2`). R2 Theorem B with **two** multipliers `h_T^{(0)}, h_T^{(1)}` (the decisive
62× test): does the best two-multiplier outside-window certificate reach `> 0` at `½log3`? Report LP value and verified-grid value. R3–R7 as listed
in R154_002 (joint top 0.9009, Λ values and signs, Prop 2.1 weights, "trace" wording, Boas–Kac citation, phase-64 RESTATEMENT row).

## 2. The independent characterization (§4(ii) of R154_000) — the round's construction target
(C1) **Euler–Lagrange as a Wiener–Hopf problem on the interval.** `A_T F = λF` on `P_T` ⟺ `(σ_T(τ) − λ)F̂(τ) = Ĥ(τ) + α ĥ₀(τ) + β ĥ₁(τ)` with `H`
supported in `|t| ≥ T` and `h₀,h₁` the Tate multipliers. State and prove exactly (PROVED). This characterizes the minimiser by a factorization
problem with symbol `σ_T − λ` (Krein–Gohberg finite-interval Wiener–Hopf). Say what is known for such symbols (not rational; Lévy exponent minus cosines).
(C2) **The phase shift for the subordinate part.** For the Gamma process alone (symbol `φ(τ²)`), Kwaśnicki's theory (Kwaśnicki 2011 "Spectral
analysis of subordinate Brownian motions on the half-line"; Kwaśnicki 2012 interval; Kulczycki–Kwaśnicki–Małecki–Stós 2010) gives eigenfunctions
`sin(μx + ϑ(μ))` + decaying part on the half-line with an explicit `ϑ(μ)` (a Wiener–Hopf integral of `log(φ(μ²)−φ(s²))/(μ²−s²)`), and interval
eigenvalues `λ_n ≈ φ(μ_n²)`, `μ_n = (nπ/2 − ϑ(μ_n))/T` up to `O(1/n)`. Compute `ϑ` for our `φ` (DIAGNOSTIC + the exact formula), predict
`λ_1, λ_2, λ_3` of the killed Gamma process on `(−T,T)` at `T = ½log3, log 2`, and compare with the spectral assembly of `M_0 − C₀` (DIAGNOSTIC-NUMERIC).
If the two-term formula is accurate to `10⁻³` or better, **the Gamma part has an explicit law**; then the primes enter as a rank-controlled
perturbation of an explicitly known operator — state exactly the resulting expression for `λ_min(A_T)` and its error term. If not accurate, say so.
(C3) **The object, second attempt.** Define `Λ_T` on `𝒦^{prim}_{2T}` (R1) and give at least one proved independent characterization: the
Wiener–Hopf E-L of (C1), or the exact variational identity `Λ_T(v) = inf over certificates` with attainment/non-attainment decided (R154_002 says
the one-multiplier dual is not tight — prove whether the two-multiplier dual is tight, i.e. strong duality with attainment; if the dual is never
attained, prove it — that is an exact obstruction theorem for the whole certificate route and must be recorded as such).

## 3. Rules
Corpus-check lines (this round: also grep "subordinat", "Bernstein", "Wiener-Hopf", "Wiener–Hopf", "phase shift", "Kwaśnicki"); labels
PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN; FATAL rule; no sign for ζ beyond `T ≤ log 2`; scripts in `scripts/round2/`.
Deliverable `R154_004_ROUND2.md` (≤ 5000 words) with sections: Repairs; Structure (subordination, upper bound); The object (C1–C3); Verdict table; Open.
