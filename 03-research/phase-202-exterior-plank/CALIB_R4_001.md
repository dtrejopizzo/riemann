# CALIB_R4_001 — Calibrator, phase 204n: Lemma WT (prop:WT, P47 l.4358) by sectors (NUMERICAL + one interval result)

Data in `CALIB_001_data/`:
- `WT_scan.json` (+ `.log`) and `WT_epstein_1.59.json`;
- `WT_H1_interval.json`;
- scripts `WT_scan.py` and `WT_H1.py`.

## 0. Convention
- **Form 𝔄.** 𝔄 = archimedean + comb, **without polar or Tate condition**. It is the template of window_bottoms / cert_*, with C0, K and the tail of each function:
  - ζ: Γ_ℝ(s);
  - Epstein: Γ_ℝ(s)Γ_ℝ(s+1), conductor 20, K = 1/sinh(u/2);
  - DH: Γ_ℝ(s+1), conductor 5, K = 2Σe^{−(2k+3/2)u}.
- **Polar direction and W per sector.** χ_ev = cosh(t/2)·1_{I_T} and χ_odd = sinh(t/2)·1_{I_T}, unnormalized, as in P47 subsec:conv. W^ev = 𝔄 + 2ε_ev χχᵀ. This is the prop:WT convention, so nothing had to be adjusted.
- **Quantities per sector.** q = ⟨χ, 𝔄⁻¹χ⟩. λ^W_ev is the minimum eigenvalue of W^ev in the L²-orthonormal Legendre basis.
- **Blocks and precision.** Legendre of degree < M, with **M = 20 and M = 30** (10 and 15 modes per sector). mpmath at 40 digits, exact GL for the products and 80 nodes in u.
- **DH case.** DH has no pole: W = 𝔄 and the WT Lemma is **vacuous**. The DH "q" values carry a fictitious polar projection and are only informative.

## 1. ζ (P1): inertias, q and floors (M = 30; in parentheses, M = 20)
| T | n₋(𝔄_ev) | q_ev + ½ | λ^W_ev | (q_ev+½)/λ^W_ev | floor 𝔄_odd | floor/‖𝔄_odd‖ | ½ − q_odd |
|---|---|---|---|---|---|---|---|
| ½log3 | 1 | −2.162e−8 (−2.208e−8) | 5.64e−8 | −0.38 | 1.51e−2 | 3.3e−3 | **3.37e−4** (3.39e−4) |
| ½log5 | 1 | −5.1e−16 (−8.8e−13) | 1.5e−15 | −0.35 | 1.5e−9 | 3.7e−10 | 6.2e−12 |
| 1 | 1 | −1.3e−20 (−2.3e−15) | 4.0e−20 | −0.32 | 1.1e−13 | 2.9e−14 | 1.4e−16 |
| ½log15 | 1 | −1.5e−23 (−2.3e−17) | 5.8e−23 | −0.25 | 2.9e−18 | 7.7e−19 | 1.4e−21 |
| 1.5 | 1 | −5.1e−25 (−2.6e−19) | 2.3e−24 | −0.22 | 5.1e−20 | 1.3e−20 | 8.0e−22 |
| 2 | 1 | −3.9e−28 | 1.9e−27 | −0.20 | 8.3e−23 | 2.0e−23 | 1.7e−27 |
| 2.5 | 1 | −5.4e−33 | 3.6e−32 | −0.15 | 4.3e−25 | 6.0e−26 | 1.2e−28 |
| 3 | 1 | −2.0e−33 | 1.6e−32 | −0.13 | 7.3e−27 | 5.2e−28 | 4.5e−33 |

**The WT Lemma holds at all T and in both blocks:**
- **Even.** n₋(𝔄_ev) = 1 and q_ev < −½. Hence λ^W_ev > 0 and n₋(W_ev) = 0.
- **Odd.** 𝔄_odd ≻ 0 and q_odd < ½.
- **Signs.** q_ev + ½ < 0 at all T; no sign change.

**Convergence in block size (P3):**
- Only **T = ½log3 is converged**: q_ev + ½ = −2.16e−8 to ≈ 2%, and ½ − q_odd = 3.37e−4 to ≈ 0.6%. It is of the order of 2.5e−4 expected, but **not equal**.
- For T ≥ ½log5 all values drop by 10³ to 10⁶ when going from M = 20 to M = 30. They are **Galerkin limits**, not values of the form: at ½log15 the true value is λ^W ≈ 5e−70 and the block gives 6e−23.
- **The "q_ev + ½ ≈ −2e−8 at ½log15" of EDITOR_204 is not reproduced.** −2e−8 is the value at **½log3**. At ½log15 the block only says that |q_ev + ½| ≲ 1e−23.

**What is robust:**
- (q_ev + ½)/λ^W_ev stays in [−0.13, −0.38] at all T and in both blocks. **q_ev + ½ tracks the floor λ^W_ev.**
- Lemma W1: **q_odd(T) is non-decreasing monotone toward ½** across the 8 T and both M.
- The floor of 𝔄_odd is monotone decreasing.

**Rate (request 3 of H3).** Δlog₁₀|q_ev+½|/ΔT gives 30, 21, 8, 10, 6, 9 between consecutive windows (M = 30).
- It is not a constant rate: **it is not e^{−δT} with fixed δ**.
- Beyond ½log5 the rate is set by the block, because it follows Galerkin's λ^W.

## 2. H1⁻ by intervals (request 1 of H3)
- **What is computed.** 𝔪_{T₀}(χ_ev) = 𝔄_ev(χ_ev)/‖χ_ev‖² for ζ, with exact c(u) = sinh(T−u/2) + (T−u/2)cosh(u/2).
- **How.** arb from python-flint at 120 bits, over a more uniform geometric grid and with enclosure per subinterval.
  - The piece [0, 1e−12] is bounded with sup|c′|.
  - At ½log3 the comb (only n = 2) is subtracted exactly.

| T₀ | 𝔪_{T₀}(χ_ev) | |
|---|---|---|
| 0.12 | [−0.047 ± 3.5e−4] | **< 0** |
| 0.5 | [−1.950 ± 2.8e−4] | **< 0** |
| ½log3 | [−2.125 ± 2.2e−4] | **< 0** |

**Status: CERTIFIED by interval arithmetic**, except for review of the [0, ε] bound. That bound is 2e−12, negligible against the radius.
- It is H1⁻ at those three T₀.
- A PROVED label needs validation of the sup|c′| bound and the closed formula for c.

## 3. Falsifiers (P2 / request 2 of H3)
**Epstein x² + 5y²:**
- **M = 20:** WT holds at 1.5, 1.59, 8/5 and 2 (λ^W > 0). Block insufficient.
- **M = 30:**

| T | even | odd | λ^W | which fails |
|---|---|---|---|---|
| 1.5 | n₋ = 1, q_ev = −0.500027 | q_odd = 0.196 | > 0 | nothing |
| **1.59** | n₋ = 1, **q_ev = −0.49989 > −½** | **q_odd = 0.6037 > ½** | ev −6.3e−4, odd −1.5e−2 | **both halves** |
| 8/5 | same as 1.59 | q_odd = 0.604 | | **both** |
| 2 | **n₋(𝔄_ev) = 2** | 𝔄_odd no longer ≻ 0 (n₋ = 1) | | fails by inertia |

**DH (T = 1.5, 9/5, 2):**
- 𝔄_ev and 𝔄_odd are ≻ 0 at M ≤ 30 (floors 6e−17 to 2e−11).
- The certified negative witness (CERT_DH, T = 9/5, odd) lives at degree 260: the M = 30 block does not see it.
- **Without a pole, the only way to fail is n₋(𝔄_odd) ≥ 1.** There is no half q.
- **The witness's ℓ_odd is 0 by construction**, because the sinh moment (P_T) is imposed. Its q_odd is not defined as a witness datum.
- The block's q_odd(9/5) equals 1.0e13: it is an artifact of 𝔄_odd being nearly singular.

## 4. Not done
- Blocks larger than M = 30. For T ≥ ½log5 the ζ values require the Mori degree (832 or more modes).
- The q_ev of Epstein and DH at degree comparable to the certificates.
