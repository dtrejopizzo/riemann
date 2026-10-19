# R154.009 — Blueprint, round 4 of phase 154: close the certificate at T = ½log3.

## 0. State (R154_008)
Theorem D1 PROVED (repair RJ: `M ⊆ cl(M_c)`, `int cl C = int C`; name the theorem: Rockafellar Cor. 31.2.1 / Slater conic form).
Lemma D2.1 PROVED (periodic lattice tail). Certified record: `λ_min(A_{½log3}) ≥ −1.6500·10⁻³` (auditor's exhaustive cover, `ρ ≤ 1.70`,
`M = 16`); target `> 0` (upper bound `9.791464·10⁻⁴`). Verifier defects: no `L·w/2` subtraction; silent interval discard at the 400 000 cap;
certificate not archived. Bottleneck diagnosis corrected: `τ_max ≈ one period`, `ρ` from the tail row.

## 1. Single goal
**Produce a fully certified dual certificate at `T = ½log3` with `c > 0`**: explicit `(u_j, a_j)_{j}`, `β₀, β₁`, and a verification that
`f(τ) := σ_T(τ) + ν̂(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ) ≥ c > 0` for all `τ ∈ R`, by (a) exhaustive stack-based Lipschitz branch-and-bound on `[0, τ_max]`
with the `L·w/2` term subtracted and NO cap that discards intervals (if a budget is hit, the run must FAIL, not pass), (b) the periodic
tail lemma for `τ > τ_max`, (c) a final interval-arithmetic (mpmath.iv) evaluation of `f` at every B&B leaf minimum and of all constants
(`L`, `ρ`, tail bound). Archive the certificate (`.json` with exact decimal strings, plus `.pkl`) in `scripts/round4/certificate/`.
Levers (in order): `ρ` set from the tail row; `τ_max` = one lattice period; `M` (16 → 19 → 24); allow a second lattice `u_j' = 2T + j·(2T/M')`
with `M'` coprime to `M` to break the resonances at `τ = pP/q` (its sum is still periodic with period `lcm`; if the period becomes too long,
certify by two-period Lipschitz cover); free `β₀, β₁`. Report a scaling table of the certified `c` against each lever.

## 2. Secondary (only after §1 is done or provably out of reach this round)
(E1) Apply RJ–RP repairs to R154_007 (verifier rewrite, archive, §8 corruption, period residual `3.24·10⁻³`, contact set is a comb).
(E2) Write Theorem D1 + Lemma D2.1 + the certificate as a self-contained statement: "Theorem (structural positivity at `½log3`): there exist
`ν` (explicit, `N` atoms) and `β` such that `σ_T + ν̂ + β·ĝ ≥ c > 0`; hence `A_{½log3} ≥ c` on `P_T`" — the first mesh-free, mechanism-visible
proof of Weil positivity with a prime coupled. Compare with Paper 42's Feshbach certificate: what is visible here that was not there
(the polar term `β₀ = 2`, the outside-window measure, the contact comb).
(E3) `T = log 2` diagnostic only if cheap.

## 3. Rules
Labels; FATAL rule (re-proving a certified endpoint by a new method is the point; no claim beyond `log 2`); every printed constant with its
enclosure; corpus-check lines; deliverable `R154_010_ROUND4.md` (≤ 4000 words) + `scripts/round4/`.
