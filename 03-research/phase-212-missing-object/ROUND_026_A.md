# ROUND_026_A — Computation of the concave value V*_T against λ_A(T)

Global label: **NUMERICAL** (Galerkin in double-precision floating point, without intervals, not certified).

## 0. What was opened
- Paper 47 `main.tex`: eq:form, eq:W and λ_A (l.115–135), lem:K and eq:m (l.395–410, C_0 = ψ(1/4) − log π, K(u) = 2e^{3u/2}/(e^{2u}−1)),
  thm:S(iii) (tail ∫_{2T}^∞ K), thm:A / eq:Aform (l.444–455), def:PD, def:W/eq:nuw (l.668, 1225), prop:finite (l.3156),
  published numerical values (l.169–170, 2521–2551, 11050–11062).
- R160_M2_R1 §§3–4 (Thm 4.1–4.3: V*_T = max_v V_T(v), v ∈ ℝ^{N_T} with free sign), §7 (PBP_T), H1 (l.378).
- ROUND_025_A §§0–2; master index l.5209, 11995, 12192, 31324–31329 (grep "prime-blind", "V\*_T", "concave value").
- **Antecedent:** no computation of V*_T recorded; H1 explicitly says "no numerics". This memo is that computation.
- Corpus code (phase-162/186 scripts) listed but not reused: a direct Galerkin of eq:Aform was written,
  validated below against the values of the paper.

## 1. Discretization
- a^w_T(F) = C_0‖F‖² + ∫_0^∞ (c_F(0) − c_F(u)) K(u) du − Σ_{2≤n<e^{2T}} w_n c_F(log n) (eq:Aform), F real.
- Orthonormal Legendre basis of degree < N on [−T,T]; c_ij(u) symmetrized by exact Gauss on the overlap;
  integral in u by Gauss–Legendre (240 nodes) on [0,2T] plus the exact tail of thm:S(iii).
- P_T: kernel of (A,B) via SVD (dim = N − 2). λ_A = λ_min with w = v, v_n = 2Λ(n)/√n.
- V*_T = max_{w∈ℝ^{N_T}} λ_min(a^w_T|P_T) as an SDP (cvxpy/SCS, eps 1e-9). The reported value is λ_min recomputed
  with numpy at the returned w, hence a valid lower bound of the discrete V*_T. V*_T⁺ (w ≥ 0) is also computed.
- Scripts and outputs: scratchpad `pbp/forms.py`, `pbp/vstar.py`, `pbp/run1.txt`, `run2.txt`, `run3.txt`.

## 2. Validation against the paper
| control | paper | this computation (N=20/30/40) |
|---|---|---|
| λ_A(½log3) | ≈ 9.448·10⁻⁴ (l.169) | 9.77 / 9.52 / 9.49 ·10⁻⁴ (decreasing towards the value) |
| λ_A(log2) | ≈ 9.83·10⁻⁸ (l.170) | 5.0·10⁻⁷ / 1.056 / 1.042 ·10⁻⁷ |
| λ_min(Arch\|P_T) at 0.58 / 0.60 | > 0 / < 0 (thm:index, T*_ev ∈ [0.58,0.60]) | +0.0273 / −0.0071 |
| λ_A(0.80) | λ_A(½log5=0.8047) ≈ 3.10·10⁻¹² (l.170) | 5.4·10⁻¹² (N=60,100) |
Slow algebraic convergence (symbol with logarithmic singularity); order and sign reproduced.

## 3. Results (free sign, which is the definition of V*_T in R160_M2_R1)
| T | \|N_T\| | N (dim P_T) | λ_A(T) | Arch min | V*_T | mult. at optimum | V*_T⁺ (w≥0) |
|---|---|---|---|---|---|---|---|
| 0.60 | 2 | 30/60 (28/58) | 6.7·10⁻⁵ | −0.0071 | 0.07013 / 0.07007 | 2 | 0.04019 |
| 0.80 | 3 | 30/60/100 | 5.4·10⁻¹² | −0.302 | 0.04598 / 0.04581 / 0.04577 | 3 | 0.02864 |
| 1.00 | 6 | 30/60/100 | < 10⁻¹³ (below resolution) | −0.535 | 0.04022 / 0.03927 / 0.03921 | 4–5 | 0.01747 |
| 1.20 | 10 | 30/60/100 | below resolution | −0.732 | 0.0402 / 0.03325 / 0.03243 | 5 | 0.01306 |
| 1.40 | 15 | 30/60 | below resolution | −0.906 | 0.0438 / 0.03258 | 5–7 | 0.01005 |
| 1.60 | 23 | 30/60 | below resolution | ≈ −1.05 | 0.0469 / 0.03499 | 7 | 0.00857 |
- λ_A for T ≥ 1 comes out ±10⁻¹⁴: it is double-precision noise; the paper bounds λ_A ≤ 4·10⁹ T e^{−15.449T} and places it at
  10⁻¹² already at ½log5. λ_A(T) for T ≥ 1 is not resolved here.
- Convergence in N of V*_T: ≤ 0.1 % at T ≤ 0.8; 0.2 % at T = 1.0 (60→100); 2.5 % at T = 1.2 (60→100); T = 1.4, 1.6
  only N ≤ 60, **not converged** (the values with N = 30 are clearly overestimated; the slight rise
  1.4→1.6 should not be read as a trend). V*_T⁺ converges to 4 digits at all T.
- Multiplicity: the minimum eigenvalue at the optimum is always degenerate (mult. ≥ 2, growing up to ~|N_T|/3);
  expected: the maximum of λ_min of an affine family is attained on a cluster (Thm 3.2 of R160_M2_R1: 0 ∈ conv κ_T).

## 4. Optimal weight against the true one (N = 100 except T = 1.4, 1.6: N = 60)
| T | v (n=2..7) | w* (n=2..7) | ‖w*−v‖/‖v‖ |
|---|---|---|---|
| 0.80 | .980, 1.269, .693 | .116, −1.000, −1.210 | 1.77 |
| 1.00 | .980, 1.269, .693, 1.440, 0, 1.471 | .277, −.591, −.877, −1.904, −1.024, −2.211 | 2.10 |
| 1.20 | (same; n=8..11: .490, .732, 0, 1.446) | .442, −.176, −.482, −1.265, −.551, −1.575; n=11: −9.2 | 3.75 |
| 1.60 | (same) | .374, −.345, −.647, −1.517, −.731, −1.955, … | 2.66 |
- w* is almost entirely negative (even at n = 6, 10 where v_n = 0), bearing no resemblance to v; it does not approach v as T grows.
  With w ≥ 0, the optimum (T = 1.2: .794, .751, .315, .354, .104, 0, 0, …) rests only on small n and annihilates the rest;
  it is not v either. The true weight is on the boundary of 𝒱_T (λ_A ≈ 0); w* is at its "center".

## 5. Answers
1. **Does V*_T remain non-tiny while λ_A drops?** Yes, in the computed range (NUMERICAL): V*_T ≈ 0.07 → 0.033 between
   T = 0.6 and 1.6, while λ_A drops from 7·10⁻⁵ to below 10⁻¹² already at T = 0.8. The ratio V*_T/λ_A goes from 10³ to > 10¹⁰.
   This is compatible with H1 of R160_M2_R1 (margin of PBP_T not doubly exponential) for T ≤ 1.6; it does not prove it.
2. **Scaling with T:** V*_T decreases slowly; with the converged values (T ≤ 1.2) the drop is ~ −0.035 per unit of T
   and flattening (0.0458, 0.0392, 0.0324); for T ≥ 1.4 the trend is not resolved. V*_T⁺ decreases as
   ≈ 0.08·e^{−1.4T} approx. (0.040, 0.029, 0.017, 0.013, 0.010, 0.0086): simple exponential, not double.
3. **w* → v?** No. w* moves away (relative error 1.8–3.8) and has the sign opposite to v at almost every n.
   The margin of 𝒱_T is given by weights that have nothing arithmetic about them; this reinforces that V*_T is blind to the primes
   (index l.5209) and that its positivity transfers no margin to λ_A(T).

## 6. What was not opened / limits
- There is no certified error bound; the SDP (SCS) issued "inaccurate" warnings in 3 runs; the reported λ_min was
  recomputed at the returned w (honest lower bound of the discrete V*_T); the upper bound was not verified by duality.
- Discrete V*_T ≥ continuous V*_T? No: the Galerkin subspace restricts F, so discrete λ_min ≥ continuous and the
  discrete V*_T **overestimates** the true one; the drop 60→100 at T = 1.2 confirms it. T ≥ 1.4 requires larger N.
- Z^prim_T (mixed relaxation) and Z^A_T were not computed. Neither paper nor index was touched.
