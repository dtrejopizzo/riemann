# EXP_001 — Setup: exact implementation of A_M = Arch − Div − Near for the profile of Theorem S

Nothing below uses, invokes or reasons from any equivalence between row D and any
other statement.

## 0. Index check before building
Read: `ROUTES-TRIED-INDEX/README.md`, `06_OPEN_RESIDUES_DEAD_SUBROUTES.md` R2 and R9, `04_PHASES_100-189.md` Part I (walls W-pat, W-tail,
W-sens = prop:wit-sens, cor:void/thm:finmod, W7, N_018). The object is R9 (problem (S), the near-coincidence part of
[Ξ(log(m/k))]) and the secondary object is R2 ((Ω₀)). Routes NOT retried: Near-free tests (L2_029), Bohr diagonalization (L2_028),
exact matrix identities from 1*Λ = log (N_022), 2×2 sections (L2_023), progression statistics (N_021), residue-balanced subspaces
(L2_031), Near as a separate signed operator (L2_030), Gram of translates (R186_001), resonators (L2_020). What is new here is a
**discovery computation** of the matrices themselves (approved numerics, justified because no structure of Near is known).

## 1. Object (Paper 47, sec:combs; checked against the paper's definitions)
Profile: g(t) = e^{bt}1_{[0,a]}(t), |b| > ½, c_g = g*g̃, G₀ = c_g*c_g, T₀ = 2a, F₀ = (¼ − ∂²)G₀, normalised ‖F₀‖ = 1
(so c₀(0) = 1 as in prop:AM(iii)). F̂₀(τ) = N(τ²+¼)|ĝ(τ)|⁴, ĝ(z) = (e^{(b+iz)a} − 1)/(b+iz), ĉ₀ = F̂₀².
  B(d) = Arch(d) − X(d),  Arch(d) = (1/2π)∫ m(τ)F̂₀(τ)² cos(τd) dτ,  X(d) = ½Σ_n v_n[c₀(log n − d) + c₀(log n + d)],
  m(τ) = Re ψ(¼ + iτ/2) − log π, v_n = 2Λ(n)n^{−½}.
Integer-lattice matrices (prop:AM): A_M = [B(log m − log k)]_{m,k≤M} = Arch_M − Div_M − Near_M, Div = exact pairs m = kn,
Near(m,k) = ½Σ_{n≥2, kn≠m} v_n c₀(log(kn/m)) (0 < |log(kn/m)| < 2T₀). Assumption 2T₀ < log 2 throughout.
For a general comb ν = Σ w_x δ_x the same code uses atoms (x, w) and a lattice of points x_m; "Div" is the set of exact coincidences
x = x_m − x_k (tolerance 10⁻⁹) and "Near" the rest. For the quartet model the Toeplitz kernel
Q(d) = Σ_{z∈{±δ±iγ}} e^{zd} F̂₀(−iz)² (= ∫c₀(v)·4cosh(δ(v+d))cos(γ(v+d))dv, checked numerically at d = 0 to 1.5·10⁻¹⁵) is ADDED to B
(Paper 47 def:wit-model: 𝔞^q = 𝔞 + 𝔮, and 𝔮(F) = ∫c_F(u)4cosh(δu)cos(γu)du).

## 2. Numerics and precision (NUMÉRICO)
* Kernels Arch(d), c₀(d) by the trapezoidal rule on τ ∈ [0, 10⁵], step h = 0.05 (2²¹ points), evaluated on a d-grid of spacing
  2π/(Nh) = 6·10⁻⁵ by one real FFT, then cubic splines. The integrand is even and analytic in |Im τ| < ½ (poles of ψ at
  τ = ∓2i(k+¼)), so the trapezoid error is O(e^{−π/h + d/2}); the tail beyond τ_max is O(τ_max^{−3}log τ_max).
* Convergence check (scripts/profile.py, `check`): (h, τ_max) = (0.05, 10⁵) vs (0.025, 2·10⁵):
  max|ΔArch| = 9.9·10⁻¹⁰ (T₀ = 0.05), 4.2·10⁻¹¹ (0.15), 5.7·10⁻¹² (0.3); max|Δc₀| ≤ 7.3·10⁻¹¹. a₀ = 𝔞(F₀) = B(0):
  2.6891447 (T₀ = 0.05), 1.5905063 (0.15), 0.8972643 (0.3) for b = 1; b = 2, −1 change a₀ in the 4th digit only.
  min c₀ = −0.648 (c₀ changes sign inside (−2T₀, 2T₀); Near entries have both signs).
* Matrix build: enumeration of all (atom, k, m) with |x − (x_m − x_k)| < 2T₀ (≈ 1.8·10⁶ off-diagonal Near entries at M = 2000,
  T₀ = 0.3); eigenvalues by LAPACK `eigh`. Round-off floor quoted as 2.2·10⁻¹⁶·‖A_M‖·M (conservative).
* Verification at M = 300, T₀ = 0.3 (scripts/test1.py): (i) Arch − Div − Near equals the matrix [Arch(d) − X(d)] built independently
  from the gridded X: max difference 8.9·10⁻¹⁶; (ii) prop:AM(ii), s^T A_M s = (1/2π)∫F̂₀²|P_s|²[m − Σ_{n<Me^{2T₀}}v_n cos(τ log n)]dτ, for a
  random s: 292.8338967328909 (integral) vs 292.8338967328759 (matrix), relative 5·10⁻¹⁴; (iii) Div symmetric, Near diagonal = 0.
* Runtime: all runs together ≈ 2.5 CPU-hours (largest single eigenproblem M = 3000, 80 s).

## 3. Ranges computed
| run | T₀ | b | M | file |
|---|---|---|---|---|
| Λ, full characterisation | 0.3 | 1 | 50…3000 | data/main_T00.3_b1.0.json |
| Λ | 0.15 | 1 | 50…3000 | data/main_T00.15_b1.0.json |
| Λ | 0.05 | 1 | 50…2000 | data/main_T00.05_b1.0.json |
| Λ, b-robustness | 0.3 | 2, −1 | 100…800 | data/main_T00.3_b2.0.json, main_T00.3_b-1.0.json |
| controls (24 combs) | 0.3 | 1 | 50…1500 | data/controls_T00.3.json |
| controls | 0.15 | 1 | 100…800 | data/controls_T00.15.json |
| lag function B(d), 12 combs, d ≤ 15 (primes to 6·10⁶) | 0.3, 0.15, 0.05 | 1 | — | data/band_T0*.npz/json |
| minimizer analysis, c*(M) | 0.3, 0.15 | 1 | 100…1200 | data/analysis_min_T0*.json |
| Near mass by (m,k,n), by h = m − kn | 0.3 | 1 | 800 | data/near_triples_T00.3_M800.json |
| packet family (m₀, w) | 0.3 | 1 | 1500 | data/packets_T00.3_M1500.json |
| (Ω₀) clamped ground mode, T ∈ [0.40, 1.10] | — | — | — | data/omega0.json |

Limit: M = 3000 is the largest M at which λ_min(A_M(Λ)) is still resolvable above the round-off floor at T₀ = 0.3 (2.0·10⁻¹⁰ vs floor
5·10⁻¹⁰: at M = 3000 the sign is NOT resolved; at M ≤ 2000 it is, by a factor ≥ 3; at M ≤ 1200 by a factor ≥ 38). Larger M is
feasible in time (M = 4000 ≈ 3 min) but useless in double precision. The feasible-M limit is therefore set by precision, not time.

## 4. Sign contact: none
At every (T₀, b, M) computed, λ_min(A_M(Λ)) > 0, with λ_min/floor ≥ 3 for M ≤ 2000 (all T₀) and ≥ 10² for M ≤ 800. No certified
negative eigenvalue; no STOP condition triggered. (The smallest values are reported in EXP_003 §1 with their floors.)
