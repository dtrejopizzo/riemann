# Round 032-A — Is the existence of weights with margin a property of the integers? (NUMERICAL)

Global label: **NUMERICAL**. Nothing that follows is a theorem.

## 1. Object and method
- a^{X,w}_T(F) = C_0‖F‖² + ∫_0^∞(c_F(0)−c_F(u))K(u)du − Σ_j w_j c_F(x_j) on P_T (Paper 46, eq:Aform),
  with the audited Legendre Galerkin (`free_weight_scripts/forms.py`, unchanged; P_T via SVD).
- V*(X,T) = max_w λ_min (free w); V*⁺ = same with w ≥ 0. Baseline: λ_min(Arch|P_T) (w = 0).
- Maximization: λ_min is concave in w; the soft minimum −β⁻¹log Σ e^{−βλ_k} is maximized with L-BFGS(-B)
  and continuation β = 10 … 3·10⁴; the reported value is the EXACT λ_min (in the Galerkin space) at
  the returned w, i.e. a lower bound of the Galerkin maximum. No cvxpy (it was not needed).
- Multiplicity: number of eigenvalues within 1 % of |λ_min| (+10⁻⁶). With the soft minimum the optimum is
  approached, not attained: the multiplicity is indicative (clustering), not exact.
- Script: `free_weight_scripts/lattice_032A.py`; outputs: `free_weight_scripts/out_032A/` (logs and JSON with
  the first 12 points and weights w⁺).

## 2. Validation (integers)
| T | V* (ref / N=60 / N=100) | V*⁺ (ref / N=60 / N=100) |
|---|---|---|
| 0.8 | 0.0458 / 0.04581 / 0.04577 | 0.0286 / 0.02864 / 0.02863 |
| 1.2 | 0.0324 / 0.03313 / 0.03235 | 0.0131 / 0.01305 / 0.01304 |
| 1.6 | — / 0.03495 / 0.02987 | 0.0086 / 0.00855 / 0.00854 |
Reproduces ROUND_026_A. Convergence: V*⁺ stable to 3–4 digits over the whole range; V* (free) NOT converged
for T ≥ 1.6 (15 % variation between N = 60 and 100). Since Galerkin restricts to a subspace, the true
value lies, up to optimizer error, below that of N = 100.

## 3. Comparative table (N = 100; N = 60 in parentheses if it differs > 5 %; * = not converged)
Baseline λ_min(Arch|P_T): −0.302 (0.8), −0.732 (1.2), −1.066 (1.6), −1.364 (2.0).

V* (free w):
| lattice | T=0.8 | 1.2 | 1.6 | 2.0 |
|---|---|---|---|---|
| (1) integers | +0.0458 | +0.0324 | +0.030 (0.035)* | +0.035 (0.040)* |
| (2) odd | −0.262 | −0.333 | −0.365 (−0.354) | −0.367 (−0.342)* |
| (3) coprime to 3 | +0.0321 | −0.054 | −0.135 (−0.124)* | −0.152 (−0.104)* |
| (4) Beurling 2→2.2 | −0.037 | −0.078 | −0.108 (−0.093)* | −0.108 (−0.078)* |
| (5) Beurling 2→2.02 | +0.0512 | +0.0221 | +0.012 (0.019)* | +0.013 (0.033)* |
| (6) log(n+0.3) | +0.0100 | −0.080 | −0.099 (−0.067)* | −0.076 (−0.045)* |
| (7) noise s1 / s2 / s3 | +.029/+.091/+.122 | +.026/+.090/+.081 | +.026/+.088/+.058* | +.026/+.089/+.077* |
| (8) primes only | +0.0286 | −0.068 | −0.120 | −0.150 |
| (9) prime powers | +0.0458 | +0.0263 | +0.0161 | +0.014 (0.015) |

V*⁺ (w ≥ 0), converged to ≤ 1 % except where marked:
| lattice | T=0.8 | 1.2 | 1.6 | 2.0 |
|---|---|---|---|---|
| (1) integers | +0.0286 | +0.0130 | +0.0085 | +0.0066 |
| (2) odd | −0.302 (= baseline) | −0.433 | −0.460 | −0.469 |
| (3) coprime to 3 | +0.00001 (≈0) | −0.406 | −0.481 | −0.485 |
| (4) Beurling 2.2 | −0.095 | −0.209 | −0.223 | −0.263 |
| (5) Beurling 2.02 | +0.0170 | −0.0121 | −0.0164 | −0.046 (−0.020)* |
| (6) log(n+0.3) | −0.149 | −0.177 | −0.187 | −0.189 |
| (7) noise s1 / s2 / s3 | +.007/+.057/+.028 | −.099/+.010/−.026 | −.134/+.0001/−.044 | −.147/−.009/−.054 |
| (8) primes only | +0.0286 | −0.111 | −0.215 | −0.314 |
| (9) prime powers | +0.0286 | +0.0122 | +0.0084 | +0.0064 |

Optimal weight w⁺ (N = 100, first points; full table of 12 in the JSON). Examples at T = 2.0:
- integers n=2..13: .886 1.008 .501 .896 .041 .747 .244 .302 .083 .498 0 .421
- prime powers (2,3,4,5,7,8,9,11,13,16,17,19): .886 1.010 .499 .913 .830 .144 .400 .559 .427 .129 .395 .197
- primes (2,3,5,…,37): .283 .973 .860 .792 .813 .358 .097 .416 .348 .247 0 0
- Beurling 2.02 (2.02,3,4.08,5,6.06,7,…): .804 .981 .523 .813 .067 .849 .251 .159 0 .869 0 .319
Clustered multiplicity at the optimum: grows with T and with the number of points (T = 0.8: 2–4; T = 2.0: 8–24 for
free w, 6–15 for w ≥ 0); it is the typical behavior of a maximum of λ_min (many eigenvalues
become equal), not a distinctive feature of a lattice.

## 4. Reading
1. **Free weights (V*).** All lattices far exceed the baseline (gaining ≥ 0.25–1.4), but only
   some reach V* > 0. Clearly positive over the whole range: integers, prime powers, the
   Beurling 2.02 perturbation (decreasing margin, not converged) and **the three random lattices**.
   Clearly negative for T ≥ 1.2: odd, coprime to 3, Beurling 2.2, log(n+0.3), primes only.
2. **Integers versus generic lattices with the same gaps, free w:** the margin of the integers is NOT larger.
   Two of three noise seeds give V* ≈ 0.08–0.09, more than double the integers (≈ 0.03); the third
   ≈ 0.026, comparable. The noise V* is almost constant in T (≈ fixed by the first points).
   With free w, positivity seems to depend on having points near log 2, log 3, log 4 with the
   spacing of the lattice, not on the multiplicative structure; log(n+0.3) (first point log 2.3) fails.
3. **Nonnegative weights (V*⁺).** Here the picture changes: at T ≥ 1.6 only integers and prime powers
   have V*⁺ > 0 clearly (≈ 0.0085, 0.0066 at 1.6, 2.0). Noise s2 stays at +0.0001 (≈ 0, within the
   optimizer's resolution) at 1.6 and goes to −0.009 at 2.0; s1, s3 negative from 1.2.
4. **Sign transitions in the range (w ≥ 0):** coprime to 3 (≈0 at 0.8 → −0.41 at 1.2); Beurling 2.02
   (+0.017 → −0.012 between 0.8 and 1.2: a 1 % perturbation of the generator destroys V*⁺ > 0); primes only
   (+0.029 → −0.111); noise s1 and s3 (positive → negative between 0.8 and 1.2); noise s2 between 1.6 and 2.0.
   For free w: coprime to 3, log(n+0.3) and primes only change sign between 0.8 and 1.2.
   At T = 0.8 the test is poorly discriminating (2–3 points): many lattices still pass.
5. **Which points matter.** Primes only fails and prime powers ≈ integers: the composites that are not
   prime powers (6, 10, 12, …) contribute little (w⁺ at n=6, 10, 12 ≈ 0.04, 0.08, 0); the powers
   (4, 8, 9, 16) are necessary. Removing the 2 (odd) or the 3 (coprime) sinks the margin.

## 5. Explicit conclusion
- With **free weights**, (PBP_T) at fixed T **does not distinguish the integers**: random lattices with the
  same gaps have equal or larger margin at every T ∈ [0.8, 2.0] (values at T ≥ 1.6 not converged,
  but the difference, a factor ≈ 2–3, exceeds the variation in N).
- With **nonnegative weights**, in the range T ∈ [1.6, 2.0] the only lattices tested with clearly V*⁺ > 0
  are the integers and their prime powers; the generic ones with the same gaps, the Beurling 2.02
  perturbation and log(n+0.3) give V*⁺ ≤ 0 (noise s2: ≈ 0 at 1.6, negative at 2.0). This is compatible with
  the sign constraint w ≥ 0 being where the arithmetic enters, with two caveats: (a) the margin of
  the integers also decreases (0.0286 → 0.0066) and its behavior at larger T has not been measured;
  (b) three seeds and two Beurling perturbations are a small sample; the contrast is NUMERICAL.
- The sensitivity to Beurling 2.02 (V*⁺ negative from T = 1.2) indicates that, with w ≥ 0, what matters
  is the exact coincidence of positions of the type log(2^k·m) with the spacing of log n, not just the gaps.

## 6. Limitations
- Soft-minimum optimizer: lower bound of the Galerkin maximum; there is no dual certificate.
- Free V* at T ≥ 1.6 without convergence in N; V*⁺ converged except Beurling 2.02 at T = 2.0.
- Multiplicities with 1 % threshold: indicative.
