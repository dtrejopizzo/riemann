# L2_BUILD_021 — ζ versus density-matched random combs on the clamped modes; the integer density ceiling

Not a restatement of 009/010: those reduce 𝒯₀ to one deterministic inequality (Ω₀) = Z_T(φ₀) ≥ 0, exactly critical at the centre.
Here: the DISTRIBUTION of the same quantities over random density-matched combs, and where ζ sits.

## Corpus check
phase-159 G2_B1_R5: **Theorem D (density ceiling, PROVED there, primitive form)**: a real comb on log ℕ that is ∀T-positive satisfies
Σ_{n≤x}a_n/n ≤ 2log x + O(1); Corollary D1: a ≥ 0 ⇒ D_a has at most a simple pole at 1 with residue r ≤ 1, Λ saturates; **Theorem R**:
dense structured (Cramér / W-trick) models have λ^A_T ≤ −c·exp((1+o(1))√(2T/log T)) (Soundararajan resonator, CITED there).
R164_402 (self-dual measure equal to the Poisson comb locally). N_BUILD_011 (κ* ≥ 1.343), L2_BUILD_018 (atomic comb in Pos,
real lattice positions). grep "Campbell / Poisson comb variance / random comb on clamped modes / large deviation of the bottom":
none. New: §1–§2 (Poisson statistics), §3 (ceiling × threshold), §4 (consistency check).

## 1. Poisson comb: exact mean and variance on any fixed test vector (PROVED)
Model: Poisson point process on (log 2, ∞) with intensity ρ(u) = e^u/u, atom at u carrying weight w(u) = 2u e^{−u/2} (prime-like:
mean measure w ρ du = 2e^{u/2}du, i.e. κ = 1). For fixed F ∈ P_T, unit norm, the random form 𝔞^ν(F) = 𝔞_∞(F) − Σ_j w(u_j)Re c_F(u_j)
has, by Campbell's formulas (CITED):
  𝔼𝔞^ν(F) = 𝔞_∞(F) − ∫_{log2}^{2T}2e^{u/2}Re c_F du = (1/2π)∫ m^♯|F̂|² + O(1)·‖F‖²_{(0,log 2) part}  [N_BUILD_001 (A),(B)],
  Var 𝔞^ν(F) = ∫_{log2}^{2T} w(u)²(Re c_F(u))²ρ(u)du = 4∫_{log2}^{2T} u (Re c_F(u))² du.
(The (0, log 2) piece of the polar identity contributes |∫_0^{log2}2e^{u/2}c_F| ≤ 4(√2−1)‖F‖²; recorded, not hidden.)

## 2. 𝒯₀ is a coin flip for random combs (PROVED, CLT CITED)
Take F = φ₀ (or its cos² clamped near-minimizer, 008 §2b), low-frequency, c_F(u) = c̃(u/2T) with a fixed shape c̃ (c̃(0) = 1,
c̃(1) = 0). Then Var = 16T²·I, I := ∫_0^1 s c̃(s)² ds ∈ (0, ½) fixed, while the mean is m^♯(0) + O(T^{−2}) + O(1) = O(1)
(m^♯(0) = C₀+4 ≈ −1.37). Lyapunov ratio: ∫w³|c|³ρ / Var^{3/2} = ∫8u²e^{−u/2}|c|³du / (16T²I)^{3/2} = O(T^{−3}) → 0, so the
Poisson CLT applies: (𝔞^ν(φ₀) − mean)/(4T√I) ⇒ N(0,1). Hence
  P(𝔞^ν(φ₀) ≥ 0) → ½  as T → ∞.
**The single test 𝒯₀ does not distinguish ζ from a typical density-matched random comb: fluctuations (≍ T) swamp the O(1)
density deficit.** The same holds for κ > κ* (mean +η_κ, same variance): density alone does not make random combs positive at φ₀.

## 3. Joint positivity on the clamped span (ARGUED)
On the span H of the d lowest clamped modes (d ≍ n_∞(T) ≍ T, 008 §2c ARGUED), the random matrix is M₀ + X, ‖M₀‖ = O(1), X with
entries of size ≍ T and covariances 16T²∫ s c̃_{ik}(s)c̃_{jl}(s)ds (Campbell). If X behaves like a Gaussian matrix ensemble with
non-degenerate covariance, P(M₀ + X ⪰ 0) decays like exp(−θd²) (Dean–Majumdar large deviation for GOE, CITED; transfer to this
non-invariant ensemble ARGUED only). So a "typical" Poisson comb is positive on H with probability ≈ exp(−c'T²): if ζ's comb were
Poisson-typical, its positivity on the clamped span alone would be an exp(−c'T²) event at each window. Rate constant: OPEN.

## 4. The integer density ceiling meets the density threshold (PROVED by combining corpus results)
Theorem D / Cor D1 (phase 159, PROVED there): any nonnegative ∀T-positive comb supported on log ℕ has residue r ≤ 1.
N_BUILD_011 Theorem 1: the density mechanism needs κ ≥ κ* ≥ |C₀|/4 ≈ 1.343.
**Proposition 4.** No nonnegative comb supported on log ℕ can be ∀T-positive by the density mechanism: its density is ≤ 1 < κ*. In
particular, every ∀T-positive comb on log ℕ (Λ included, which saturates r = 1) is positive only through P_T-correlation, and ζ sits
exactly at the integer ceiling. ∎
Consistency check (important): N_BUILD_011's continuous ρ_κ and L2_BUILD_018's lattice comb have κ > 1 and are ∀T-positive. This does
NOT contradict Theorem D: those combs are not supported on log ℕ (Theorem D's proof pairs a_n with the integer test vectors
b_m = m^{−½}, whose autocorrelation lives on log of rationals — an integer-lattice P_T-correlation). So the multiplicative structure
of ℕ, acting through TEST functions (not through the comb's support, cf. 020), is DESTRUCTIVE for density: it caps κ at 1.
(If a referee finds Theorem D inapplicable to real-position combs only through this support hypothesis, the picture is coherent.)

## 5. What this quantifies
(i) At one vector (𝒯₀), ζ is not exceptional among random combs (coin flip). (ii) Jointly on the clamped span, positivity of a random
comb is an exp(−cT²)-rare event (ARGUED). (iii) On log ℕ, density cannot help at all (Prop 4). (iv) Dense structured random models on
log ℕ are deterministically negative, λ ≤ −exp(c√(T/log T)) (Theorem R, CITED). Hence ζ's positivity is an exceptional correlation
event relative to every density-matched model on log ℕ; the arithmetic content to be proved is exactly the deviation of ζ's comb
from these models on the clamped span and beyond, with the integer test-function structure (Theorem D's resonators) working against it.

## 6. Review
- §1: Campbell mean/variance standard; intensity e^u/u integrable away from 0; correct.
- §2: CLT conditions verified (Lyapunov). The near-minimizer vs exact φ₀ distinction does not matter (any fixed low mode works).
  Note φ₀ depends on T but not on the random comb (archimedean ground state) — correct, it is a deterministic test vector.
- §3: only ARGUED; the large-deviation transfer from GOE is not justified. Label kept.
- §4: relies on Theorem D as PROVED in the corpus (phase 159, panel-verified per that record); the support hypothesis distinction is
  my reading — the referee of N_BUILD_011/L2_BUILD_018 should confirm it. If Theorem D held for real-position combs, 018 and N_011
  would contradict it; their proofs are elementary and checked, so the support reading is the consistent one.
- No sign certified; no negative value of 𝔞_T for ζ.
