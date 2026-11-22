# EXP_003 — Structure of Near_M, of A_M(Λ) and of its minimizer

All numbers NUMÉRICO unless marked. Data: data/main_T0*.json, analysis_min_T0*.json, near_triples_T00.3_M800.json, packets_T00.3_M1500.json,
identity_check (scripts/identity_check.py output, reproduced below).

## 1. λ_min(A_M(Λ)): positive, and critically small — M^{−3}
| M | T₀ = 0.3 | 0.15 | 0.05 | floor (0.3) |
|---|---|---|---|---|
| 50 | 3.31e−5 | 2.81e−4 | 3.48e−3* | 1.5e−13 |
| 100 | 4.46e−6 | 3.65e−5 | 6.69e−4* | 5.6e−13 |
| 200 | 5.94e−7 | 4.71e−6 | 1.25e−4 | 2.2e−12 |
| 400 | 7.82e−8 | 6.15e−7 | 1.67e−5 | 9.0e−12 |
| 800 | 1.01e−8 | 8.09e−8 | 2.22e−6 | 3.6e−11 |
| 1200 | 3.05e−9 | 2.43e−8 | 6.73e−7 | 8.1e−11 |
| 1600 | 1.30e−9 | 1.04e−8 | 2.81e−7 | 1.4e−10 |
| 2000 | 6.72e−10 | 5.38e−9 | 6.02e−8* | 2.3e−10 |
| 3000 | 2.01e−10 (≈ floor) | 1.60e−9 | — | 5.1e−10 |
Local exponents −d log λ/d log M: 2.89 → 2.98 (T₀ = 0.3), 2.93 → 2.98 (0.15), 2.9–3.0 (0.05, M = 200…1600). Global fit −2.93, −2.94, −2.87.
b = 2 and b = −1 at T₀ = 0.3 reproduce b = 1 to 3 digits (b → −b is the same profile after normalisation; b = 2: 6.23e−7 vs 5.94e−7 at M = 200).
(*) At T₀ = 0.05 and M ∈ {50, 100, 2000} the Euclidean bottom is a Gram-degenerate direction (‖Σv_mV_{log m}F₀‖² = 10⁻⁷…10⁻²; adjacent
translates at lag 1/m ≪ 2T₀ = 0.1 are nearly identical); those entries are not the arithmetic bottom. Everywhere else the bottom vector has
‖G_v‖² = 0.37…0.93 and is the arithmetic one described in §2. The Gram C_M = [c₀(log m − log k)] has condition number 10⁵ (M = 100) → 10¹²
(M = 3000) at T₀ = 0.3, so the Gram-relative bottom (= an upper bound for λ_A(T₀ + ½log M)) is numerically reliable only for M ≲ 200:
6.5e−5 (M = 50), 9.6e−6 (100), 1.3e−6 (200) at T₀ = 0.3; it is of the same size and decay as the Euclidean λ_min.
**Fact N1 (NUMÉRICO):** λ_min(A_M(Λ)) = M^{−3+o(1)} > 0, uniformly in T₀ ∈ {0.05, 0.15, 0.3} and b. The amplification threshold c*(M) and the
first negative M of every ε-perturbation are governed by this value (EXP_002 §2).

## 2. The minimizer: entrywise positive, ≈ m^{−½}, and a Dirichlet polynomial that vanishes at the zero ordinates
Bottom eigenvector v of A_M(Λ), ‖v‖ = 1 (T₀ = 0.3; T₀ = 0.15 identical to the digits shown):
| M | overlap with m^{−½}/‖·‖ | fraction of entries > 0 | mass on m ≤ 10 | participation ratio | |P_v(γ_j)| median / |P_v(τ)| generic median |
|---|---|---|---|---|---|
| 100 | 0.9937 | 1.000 | 0.58 | 16 | 1.0e−3 |
| 200 | 0.9937 | 1.000 | 0.51 | 20 | 2.2e−4 |
| 400 | 0.9933 | 1.000 | 0.46 | 25 | 2.7e−5 |
| 800 | 0.9932 | 1.000 | 0.41 | 31 | 2.3e−6 |
| 1200 | 0.9933 | 1.000 | 0.39 | 34 | 7.1e−7 |
(P_v(τ) = Σ_m v_m m^{iτ}; γ_j = ordinates of the first zeros of ζ below 60, computed with mpmath only to evaluate P_v there; generic median over
τ ∈ [0.5, 60]. Overlap with μ(m)m^{−½}: ≤ 0.004.) The mass on m ≤ 10, 0.37 at M = 2000, equals Σ_{m≤10}m^{−1}/H_M = 2.93/8.18 = 0.36, and the
centre of mass ≈ M/H_M: the minimizer is m^{−½} with a small correction. The pure vector m^{−½} has Rayleigh quotient 0.06 (M = 100) …
0.50 (1200) at T₀ = 0.3 (positive, growing), the smooth cutoffs m^{−½}cos²(πm/2M) give 7·10⁻⁵…3·10⁻⁴: the 0.7 % of the vector that is not
m^{−½} is what brings the quotient from 10⁻¹ to 10⁻⁹. That correction is exactly the one that makes P_v vanish at the zero ordinates:
|P_v(γ_1)|, …, |P_v(γ_5)| ≤ 7·10⁻⁴ already at M = 100 (γ ≤ 33), with the ratio to generic values decreasing like M^{−1.5…−2}.
**Fact N2 (NUMÉRICO, zero-side observation, output not input):** the sign of A_M(Λ) is decided on a positive vector ≈ m^{−½}, and the
minimizer is the Dirichlet polynomial nearest to m^{−½} that annihilates the first zeros with weight F̂₀(γ)². The M^{−3} law of N1 is
consistent with the tail Σ_{γ ≳ cM}F̂₀(γ)²|P_v(γ)|² (F̂₀² ~ τ^{−4}, N(τ) ~ τ log τ): a zero-side mechanism, recorded as such.

## 3. Three-way decomposition at the minimizer (T₀ = 0.3): Div and Near cancel to O(1), the archimedean energy is the balance
| M | Arch(v) | Div(v) | Near(v) | Div + Near | Gram(v) |
|---|---|---|---|---|---|
| 50 | 0.455 | 3.332 | −2.878 | 0.455 | 0.497 |
| 200 | 0.360 | 4.678 | −4.318 | 0.360 | 0.431 |
| 800 | 0.322 | 6.032 | −5.709 | 0.322 | 0.513 |
| 2000 | 0.341 | 6.934 | −6.593 | 0.341 | 0.738 |
| 3000 | 0.368 | 7.334 | −6.966 | 0.368 | 0.927 |
Div(v) grows by ≈ log 2 per doubling of M (Div(v) ≈ log M + 0.4: the Mertens-type sum Σ_n 2Λ(n)n^{−1}H(M/n) of L2_028 §3), Near(v) = −Div(v) + Arch(v) − λ.
T₀ = 0.15: Arch(v) = 0.89 → 0.56, same pattern; T₀ = 0.05: Arch(v) = 1.8 → 1.35. The archimedean energy of the minimizer, Arch(v)/Gram(v) ≈ 0.4–0.7,
is a fixed O(1) quantity; the comb part Div + Near reproduces it to 10⁻⁹.

## 4. Where Near(v) lives: per-atom cancellation, defect at n = 2, 3, 4 only (M = 800, T₀ = 0.3)
Contribution of each atom n to Near(v) and to Div(v) on the minimizer (near_triples_T00.3_M800.json):
| n | 2 | 3 | 4 | 5 | 7 | 8 | 9 | 11 | 13 |
|---|---|---|---|---|---|---|---|---|---|
| Near_n(v) | −0.460 | −0.501 | −0.254 | −0.498 | −0.407 | −0.123 | −0.169 | −0.290 | −0.254 |
| Div_n(v) | +0.629 | +0.621 | +0.281 | +0.501 | +0.407 | +0.124 | +0.170 | +0.290 | +0.254 |
| δ_n := Near_n + Div_n | +0.169 | +0.120 | +0.027 | +0.003 | 0.000 | +0.001 | +0.001 | 0.000 | 0.000 |
Σ_n δ_n = 0.322 = Arch(v) − λ. So **on the minimizer every atom n ≥ 5 cancels its own divisor part to 3 decimals, and the whole comb
balance against the archimedean energy is carried by the near-coincidence defects at n = 2, 3, 4** (the contact set of the certified windows,
Paper 46 thm:log5A). Mechanism (PROVED-elementary, not ζ-specific): for a smooth vector s_m = S(m), Σ_m s_m c₀(log(kn/m)) is a Riemann sum of
∫S(y)c₀(log(kn/y))dy = (kn)^{½}·∫S(kn e^{−u})e^{−u}c₀(u)du, which vanishes exactly for S(y) = y^{−½} by the Tate condition ∫c₀(u)e^{u/2}du = 0
(lem:transl(iii)); the Riemann-sum error is the discretisation defect, large only when the lattice spacing 1/(kn) is not small against the
profile width 2T₀, i.e. for kn ≲ 1/(2T₀) ≈ 2–4. On the exact vector s = m^{−½} this is an identity (scripts/identity_check.py, M = 800):
  s^T(Div + Near)s = 2 Σ_N N^{−½} log N · E_M(N),  E_M(N) := Σ_{m≤M} m^{−½}c₀(log(N/m)),
checked to 12 digits (1.985815103517 both sides), with E_M(2) = 0.778, E_M(3) = 0.636, E_M(4) = 0.287, E_M(5) = 0.0004, |E_M(N)| ≤ 2·10⁻⁶ for
50 ≤ N ≤ 400 (window-edge terms N ≈ M cancel among themselves). This identity uses Λ*1 = log once, linearly (wall W7: it is the pole, not the
sign); the controls a_P, amp2, pert break it by exactly their modification of Σ_{n|N}a(n). It is recorded as an exact structural fact
about Near on the lattice, NOT as a sign source: on s = m^{−½} itself A_M(s)/‖s‖² = 2.58/7.26 > 0 with margin, and the sign is decided by the
0.7 % correction of §2.
Additive shifts h = m − kn: the mass of Near(v) by h is flat (h = ±1: 4.61, ±2: 3.90, ±3: 3.42 for Λ; 0.36…0.63 for the controls' negative
packets): no structure in h beyond the smooth c₀(h/m) weight (as L2_030 §1(c) predicts).

## 5. Near_M as a matrix (T₀ = 0.3; T₀ = 0.15 in parentheses)
* Norms grow linearly in M: ‖Near‖_op = 8, 16, 32, 67, 137, 346, 517 at M = 50…3000 (≈ 0.17M; 0.087M at T₀ = 0.15); ‖Arch‖_op ≈ 0.145M;
  ‖Div‖_op = 3.4 → 7.5 (≈ log M, the Schur bound of prop:nearfree); ‖A_M‖_op = 76 at M = 2000. Near and Arch are O(M) because B's three
  parts are O(1) functions of the lag sampled at density ~M per unit lag; their difference A_M is O(M) too but with λ_min ~ M^{−3}.
* Spectrum: Near is indefinite and full rank: singular values at M = 3000: 517, 483, 312, 235, 76 (j = 10), 20 (j = 20), 4.6 (50), 3.3 (100),
  2.5 (200); 1690 of 3000 above 10⁻³·max, 2673 above 10⁻⁶·max. Eigenvalues from −517 to +312 (T₀ = 0.15: −261 to +223, more symmetric).
  Not low-rank: the leading 20 singular directions carry the lag-bands at log 2, log 3 and the overlap region, the rest is a dense remainder.
* Sign pattern: 56.5 % of the nonzero Near entries are positive (52 % at T₀ = 0.15, 62 % at 0.05); Σ entries = −2786 vs Σ|entries| = 4.5·10⁵
  at M = 2000: Near is nearly balanced in sign. Off-diagonal entries of A_M itself: 64 % positive at lags < 2T₀ (overlap region), 45–57 % at
  larger lags — A_M is not a Z-matrix, so the positivity of the minimizer (§2) is not a Perron–Frobenius effect.
* Mass by atom (Σ|Near entries| from atom n, M = 2000): n = 2: 1.6·10⁵, 3: 1.4·10⁵, 5: 9.3·10⁴, 7: 6.8·10⁴, 4: 5.6·10⁴, 11: 4.2·10⁴ … ∝ Λ(n)n^{−3/2}M²
  up to the lattice geometry; the first three primes carry 45 % of the mass.
* Alignment: the five leading eigenvectors of Near have squared overlap ≤ 2.7·10⁻⁴ with the negative eigenspace of Arch (which has only
  10–11 negative eigenvalues at M = 2000–3000, bottom −1.8…−2.7; 6–7 at T₀ = 0.15, bottom −0.06…−0.09), and ≤ 5 % with the span of Div's 20
  leading eigenvectors (decreasing with M from 93 % at M = 50). Near's large directions are orthogonal to the archimedean negativity: the
  sign is not decided where Arch is negative, nor where Near is large, but on the vector of §2 where Arch ≈ +0.3 and Near ≈ −Div.

## 6. Packet family (T₀ = 0.3, M = 1500): Λ against controls on fixed-shape tests
Gaussian packets u_m ∝ exp(−(log m − log m₀)²/2w²), Rayleigh quotient 𝔞(G_u)/‖G_u‖², minimum over m₀ (data/packets_T00.3_M1500.json):
| w | Λ | pert₂(+10⁻⁵) | pert₂(−10⁻⁵) | pert₂(+10⁻²) | a₃ | Poisson 0 | M₁(0.1) |
|---|---|---|---|---|---|---|---|
| 0.2 | 7.1e−3 (m₀ = 992) | 7.1e−3 | 7.1e−3 | 7.2e−3 | −4.3e−2 | −0.31 | 7.7e−3 |
| 0.4 | 1.5e−5 (270) | 2.1e−5 | 9.8e−6 | 5.5e−3 | −0.51 | +0.36 | 1.7e−5 |
| 0.7 | 5.3e−3 (99) | 5.3e−3 | 5.3e−3 | 3.8e−3 | −0.29 | +0.46 | 6.7e−3 |
| 1.0 | 1.5e−2 (1) | 1.5e−2 | 1.5e−2 | 1.1e−2 | +0.30 | −0.82 | 1.7e−2 |
The fixed-shape packets separate the structural controls (a₃, Poisson negative) but not the ε-perturbations nor M₁ at this M; Λ's packet
margin is smallest (1.5·10⁻⁵) at w = 0.4, m₀ = 270 — a near-critical packet at the top of the window, exactly where the controls' negative
eigenvectors live (EXP_002 §3). Consistent with [crit] (exact criticality of packet families, N_013, L2_010).

## 7. Summary of what Near is, in this experiment
Near_M = ½[Ξ_{F₀}(log(m/k))]_{m≠k} − Div_M: a Toeplitz-in-log sampling of the bounded one-variable fluctuation Ξ (sup|B|/a₀ = 0.94 at
T₀ = 0.3, EXP_002 §5) minus the atoms. Its matrix statistics (O(M) norm, full rank, balanced signs, mass ∝ Λ(n)n^{−3/2}, orthogonality to the
archimedean negativity) are shared to 5 digits by the 10⁻⁵ perturbations, which are indefinite. The only Λ-specific behaviour visible in
Near is on the minimizer (§3–§4): per-atom Tate cancellation for n ≥ 5 (analytic, comb-independent) plus a defect at n = 2, 3, 4 that
balances the archimedean energy to 10⁻⁹ — and the exactness of that balance is the target itself, explained numerically by the
zero-side observation N2.
