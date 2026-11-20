# Round 027-A — Adversarial numerical verification of the damped weight `v_n cos(ω log n)`

Everything in this memo is NUMERICAL except where indicated. Scripts and outputs: temporary folder
`pbp_verify/` (trig.py, sweep.py, leg.py, hi.py; s1.log, s2.log, hi.log).

## 1. Audit of the original implementation (forms.py)

Checked against Paper 47 (eq:symbol, eq:form, lem:K, thm:S(iii), thm:A eq:Aform):
- `K(u) = 2e^{-u/2}/(1−e^{-2u}) = 2e^{3u/2}/(e^{2u}−1)`: correct. `C_0 = ψ(1/4) − log π`: correct.
- Lévy on `[0,2T]` plus tail `c_F(0)∫_{2T}^∞K = log coth(T/2) + π − 2 arctan e^T`: matches thm:S(iii).
- `c_F(u) = ∫F(t)F(t+u)dt` symmetrized; contacts `log n < 2T`; `v_n = 2Λ(n)/√n`: correct.
- `P_T` = kernel of `A, B` with `e^{±t/2}`: correct. Gauss quadrature in `u`: the integrand
  `K(u)(c(0)−c(u))` is a polynomial times an analytic function, without singularity; adequate.
- Damping of taper2: `cos(kπ x/2)`, `x = log n/2T`, is `cos(ω log n)` with `ω = kπ/(4T)`: correct.
I found no error that would manufacture the effect.

## 2. Independent reimplementation

Neumann cosine basis `cos(kπ(t+T)/2T)` (non-polynomial), autocorrelations and Tate moments in
closed form, tanh-sinh quadrature in `u`, Richardson extrapolation (convergence `O(N^{-2})`).

| T | N=40 | 80 | 160 | 320 | Richardson | Paper 47 |
|---|---|---|---|---|---|---|
| ½log3 | 1.0028e-3 | 9.5688e-4 | 9.4769e-4 | 9.4557e-4 | 9.449e-4 | 9.448e-4 |
| log 2 | 1.497e-7 | 1.096e-7 | 1.006e-7 | 9.878e-8 | 9.82e-8 | 9.83e-8 |

Technical warning: with N = 320 and T ≥ 2 the tanh-sinh step h = 0.01 does not resolve the oscillation of
`c_ij(u)` and produces spurious `λ_A ≈ −0.07 … −0.27` (artifact: with h = 0.003, N = 240, `λ_A ≈ −1e−12`,
rounding level). Those rows are discarded.

## 3. Values k = 1.0 and k = 0.6 (trig basis; Legendre of forms.py in parentheses)

Margin `μ(T) = λ_min(a^{w(ω)}_T)`, ω = kπ/(4T):

| T | k=1.0, N=80 / 160 / 240–320 | status | k=0.6 (larger N) | ratio 0.6/1.0 |
|---|---|---|---|---|
| 0.8 | 0.01269 / 0.01269 / 0.01269 | converged | 0.004495 | 0.354 |
| 1.2 | 0.002296 / 0.002292 / 0.002291 | converged | 0.000820 | 0.358 |
| 1.6 | 3.967e-4 / 3.960e-4 | converged | 1.427e-4 | 0.360 |
| 2.0 | 9.96e-5 / 9.86e-5 / 9.84e-5 | converged | 3.557e-5 | 0.361 |
| 2.4 | 4.00e-5 / 2.565e-5 / 2.563e-5 (Leg 60/100/140: 1.55e-4, 4.8e-5, 2.9e-5) | converged trig, Leg not | 9.24e-6 | 0.360 |
| 2.8 | 2.99e-5 / 9.6e-6 / 7.0e-6 (Leg: 1.2e-4, 4.9e-5, 2.2e-5) | NOT converged, decreasing | **−0.00132** | — |
| 3.2 | 2.42e-5 / 6.2e-6 / 3.2e-6 | NOT converged, decreasing | **−0.0137** | — |

- The four values of the finding (T = 0.8…2.0, k = 1.0 and k = 0.6) are reproduced in another basis to 3–4 digits.
- Decay law for k = 1 (T ≤ 2.4, converged): ratios per ΔT = 0.4 of 5.5, 5.8, 4.0, 3.8. Simple exponential
  that slows down: `μ ≈ e^{−3.4T}` at the end, i.e. `≈ N^{−1.7}` with N = e^{2T}. It is not doubly exponential.
- **k = 0.6 crosses zero between T = 2.4 and T = 2.8** (negative and converged in both bases: trig −0.00127/−0.00132,
  Legendre −0.00102/−0.00114). The law `μ ∝ k²` holds up to T = 2.4 (ratio 0.36 = 0.6²) and breaks afterwards.
- k = 1.0 at T ≥ 2.8: positive in every basis tried, but the margin drops as N grows without stabilizing
  (T = 3.2: 2.4e-5 → 6.2e-6 → 3.2e-6). **Positivity cannot be asserted for T ≥ 2.8**: it is compatible with
  a small positive limit and with a limit ≤ 0. Remains OPEN and NUMERICAL not converged.

## 4. Fixed ω

| T | ω=0.2 | ω=0.4 |
|---|---|---|
| 0.8 | 5.29e-4 | 2.08e-3 |
| 1.2 | 2.15e-4 | 8.51e-4 |
| 1.6 | 6.59e-5 | 2.63e-4 |
| 2.4 | 9.58e-6 (conv.) | 3.82e-5 (conv.) |
| 2.8 | 4.9e-6 → 3.6e-6 (not conv.) | **−0.0119** (conv.) |
| 3.2 | 4.2e-6 → 2.1e-6 (not conv.) | **−0.12** |

ω = 0.4 crosses zero between 2.4 and 2.8; it coincides with the threshold `ω·2T > π/2` at which weights with `log n > π/(2ω)`
become negative (n > 51), but k = 0.6 crosses with all weights positive, so the sign of the weight is not
the only cause. ω = 0.2: positive margin that decays and does not converge in N for T ≥ 2.8.
Conclusion: with fixed ω the margin is **not** maintained; the premise "margin ∝ ω² uniformly in T" is false.

## 5. First-order prediction `μ ≈ λ_A + (ω²/2) Q(F_*)`

- T = 0.5 (λ_A = 0.01187, isolated eigenvalue): ω = 0.2 measured 0.013654, predicted 0.013655; ω = 0.4: 0.01893
  versus 0.01900. **Correct** where λ_A is separated.
- T = 0.8: prediction ≈ 2× the measured value (ω=0.2: 1.005e-3 vs 5.29e-4). T ≥ 1.2: prediction 50× to 10⁴×
  above and `Q(F_*)` does not converge in N (T = 1.6: 3.97 → 7.0). Reason: `a^v_T` has a near-null subspace of
  growing dimension (`λ_A` is at rounding level, 1e−13), the minimizer `F_*` is not determined and the
  perturbation is degenerate: the margin is fixed by the `min` of Q over that subspace, not Q at one vector. Formula
  (iii) of the finding, evaluated at a minimizer, is not informative for T ≥ 0.8.

## 6. Controls (k = 1.0; undamped in parentheses)

| T | without n=2 | 2v | Beurling (2 → 2.2) |
|---|---|---|---|
| 0.8 | −0.403 (−0.568) | −0.293 | −0.210 (−0.380) |
| 1.2 | −0.642 (−0.735) | −0.942 | −0.550 (−1.103) |
| 1.6 | −0.775 | −1.67 | −1.09 |
| 2.4 | −0.873 | −1.98 … −2.8 | −1.92 |
| 3.2 | −0.92 | −2.46 | −2.35 |

The three controls give a **negative** damped form of order 1 at every T ≥ 0.8, converged. (At T = 0.5
there is only one contact and the controls are trivial.) Damping does not create positivity by itself: the effect
depends on the exact values of v. This is consistent with the requirement of nonlinearity in Λ.

## 7. Balance

- PROVED (elementary, already in the finding): (i) modulation and (ii) monotonicity of K_T under extension by zero.
- NUMERICAL converged: reproduction of λ_A(½log3), λ_A(log 2) and of the values k = 1, 0.6 up to T = 2.4;
  negative controls; k = 0.6 and ω = 0.4 negative at T = 2.8, 3.2.
- NUMERICAL not converged: k = 1 and ω = 0.2 at T ≥ 2.8 (positive in the bases tried, decreasing with N).
- Consequence for use (ii): a sequence `ω_j → 0` with positive margin requires `ω_j ≳ π/(4T_j)` or more
  (k ≥ 1 with k = 0.6 already failing); what happens at k = 1 for large T is exactly what is unresolved. OPEN.
- What was not opened: extended precision (mpmath) — it was not needed for the reproduced values and would not
  resolve the non-convergence in N, which is a basis issue, not rounding; T = 3.2 with N > 240.
