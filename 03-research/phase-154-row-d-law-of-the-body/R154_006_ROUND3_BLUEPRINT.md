# R154.006 — Blueprint, round 3 of phase 154.

## 0. State after R154_005
Theorem A (exact, two-condition primitive class), Theorem W (E-L = finite-interval Wiener–Hopf, non-elliptic symbol), Theorem O (dual
never attained; PROVED; forbids attainment only). Subordination upper bound settled (`2Σw − C₀ = 6.3524 / 7.6210`; UB 1.29 / 2.33 > 0).
Certificate route NOT closed: any dual with value in `(0, λ_min)` proves the sign. Zero duality gap OPEN. Best provable certificate at
`½log3`: `−3.02·10⁻²` (with rigorous tail at `τ_max = 10³`); target `> 0` (λ_min = 9.89·10⁻⁴). Atomic + two-multiplier LP unfinished.

## 1. Tasks
(D1) **Strong duality theorem.** Primal: `λ_min = inf{∫σ_T dμ : μ ≥ 0 prob. measure, μ = |F̂|²dτ/2π, F ∈ P_T}` (equivalently `Φ ∈ 𝒦^prim_{2T}`).
Dual: `sup{c : σ_T(τ) + ν̂(τ) + β₀ĥ₀(τ) + β₁ĥ₁(τ) ≥ c ∀τ, ν finite signed measure on |u| ≥ 2T, β ∈ R²}`. Prove `sup = λ_min` (zero gap)
or exhibit the gap. Route: Fenchel–Rockafellar / Lagrangian duality for the LP over `C_0`-type spaces; the primal constraint set
(autocorrelations of `P_T` functions) is convex; check the closedness/compactness needed (Paley–Wiener: `Φ` continuous, supp ⊂ [−2T,2T],
`Φ(0)=1`); handle the two moment constraints as equalities. State the theorem precisely and prove it (PROVED) — or prove a positive gap (which
would be an obstruction theorem of the strongest kind for this route; check consistency with Theorem O and with the LP data).
(D2) **Construct the certificate at `T = ½log3`.** Class: `ν = Σ_j a_j(δ_{u_j} + δ_{−u_j})`, `u_j ≥ 2T`, plus a continuous part if useful,
plus `β₀, β₁`; objective: maximize `c` with rigorous verification `σ_T + ν̂ + β·ĝ ≥ c` on all of `R` (grid + Lipschitz bound on
`[0, τ_max]`, analytic tail bound for `τ > τ_max` using `σ_T ≥ log τ − const` and `|ν̂| ≤ TV(ν)`). Use the LP with atoms on a fine grid
of positions (`u_j ∈ [2T, 2T + 20]`, step `≤ 0.01`) and free `β`; then re-verify with interval arithmetic (mpmath.iv) at the final point.
**Goal `c > 0`.** If reached: PROVED — the first mesh-free structural proof of Weil positivity with the prime 2 coupled; write the certificate
explicitly (positions, weights, `β`) and its verification. If not reached: report the best `c`, and how `c` scales with the atom range and grid
(does it approach `λ_min` as Theorem D1 predicts? plot-free table).
(D3) **Read the certificate.** Positions and signs of the atoms of near-optimal `ν`: is there structure (atoms near `2T + k·log 2`? near
`log 3, log 4, …` beyond the window? equal spacing?) — a pattern would be the seed of a closed-form "magic measure". DIAGNOSTIC; state only
what the data show.
(D4) **`T = log 2` as diagnostic**: same LP; target `1.09·10⁻⁷` — report the best `c` and the distance; no claim.
(D5) Repairs RA–RI of R154_005 (finite signed measure in Theorem O; `c_F(±2T)=0`; 𝒦^prim affine; "index undefined / symbol non-elliptic";
phase-64 §5 wording "untenable in the prolate scaling"; kernel normalisation `K` vs `ν = K/2` against R129_007; structure.py attribution; the
tail column; novelty credit lines).

## 2. Rules
Corpus-check lines (grep "strong duality", "dualidad fuerte", "Fenchel", "Beurling–Selberg", "Selberg majorant", "extremal function");
labels; FATAL rule; no sign for ζ beyond `T ≤ log 2` (a certificate at `½log3` or `log 2` re-proves certified facts by a new method — that is
the point); scripts in `scripts/round3/`; deliverable `R154_007_ROUND3.md` (≤ 5000 words) with the explicit certificate if found.
