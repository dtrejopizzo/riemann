# CALIB_R3_001 — Calibrator, phase 203, object III: contact ladder (NUMERICAL)

Everything is **NUMERICAL**.
Data: `CALIB_001_data/P203_ladders.json`. Script: `P203.py`.

## 0. Conventions and precision
- **Partial residue.** W^(N) := arch(g*) + polar − Σ_{n≤N} v_n c_{g*}(log n), with v_n = 2Λ(n)/√n.
  - c_{g*}(u) = ∫g*(t)g*(t+u)dt.
- **ζ data.** True g* of Mori μ = 15, computed in arb at 420 bits as in step1 of F0_TEST.
  - **arch(g*) is the true form:** arch_Ω plus the tail t > 736, which is worth 1.2329e−70 and comes from step1_archtail. That is, the one from W_T(g*), not the Galerkin one.
  - That tail has only about 3 digits. It fixes the absolute error of W^(N) at around 1e−73. The rest has arb radii smaller than 1e−90.
- **DH data.** Certified witness from CERT_DH_001 (T = 9/5, odd sector, N = 260).
  - c_F computed with mpmath at 30 digits and GL with 400 nodes, exact for the polynomial product.
  - The C0 + Lévy base was reconstructed from the certified value −7.05197e−9. It agrees with the certificate pieces to 12 digits: 2.387882175452 against 2.387882175448.
  - Each W^(N) is divided by ‖F‖².

## 1. P203.1 — ζ, μ = 15
**All c_{g*}(log n) are positive for n = 2…14.** Therefore W^(N) is non-increasing in N and W^(N) ≥ W^(14) = W_T(g*) > 0.

| N (contact) | c(log N) | W^(N) | q_N = \|ΔW\|/W^(N−1) |
|---|---|---|---|
| 1 | — | 6.3204e−2 | — |
| 2 | 6.384e−2 | 6.2286e−4 | 0.99015 |
| 3 | 4.901e−4 | 1.0886e−6 | 0.99825 |
| 4 | 1.565e−6 | 3.8516e−9 | 0.99646 |
| 5 | 2.676e−9 | 2.1542e−15 | 0.99999944 |
| 7 | 1.464e−15 | 2.1738e−19 | 0.99989909 |
| 8 | 4.434e−19 | 4.8450e−23 | 0.99977712 |
| 9 | 6.615e−23 | 1.2491e−31 | 1 − O(1e−9) |
| 11 | 8.638e−32 | 2.2142e−43 | 1 − O(1e−12) |
| 13 | 1.556e−43 | **4.97791e−70** | 1 − O(1e−27) |

- **N without contact.** At N = 6, 10, 12 and 14, W^(N) does not change, because Λ(N) = 0 in those cases.
- **Values of c(log n) at those N:** c(log 6) = 2.62e−12, c(log 10) = 4.17e−27, c(log 12) = 3.83e−37, c(log 14) = 6.31e−52.
- **Sign.** **All W^(N) are positive.**
- **Closure.** W^(14) = 4.977908e−70, which reproduces W_T(g*) = 4.978e−70.
- **Pattern.** Each contact consumes almost all of the previous residue: q_N → 1. The remaining residue, W^(N), is of the order of the next term v_{N′}c(log N′), with N′ the next contact. It is an almost exact cancellation ladder.
- **Shape of the ladder.** log₁₀ c(log n) equals −1.19, −3.31, −8.57, −14.83, −31.06 and −42.81 for n = 2, 3, 5, 7, 11, 13.
  - Against (log n)², the slope grows: 2.5, 2.7, 3.3, 3.9, 5.4, 6.5.
  - **The decay is faster than Gaussian in log n.**

## 2. P203.2 — DH and Beurling
**DH, on its own certified witness.** There are 35 contacts, n ≤ 36.
- **Signs of c_F(log n): mixed.** For n = 2…14 they are + − − − + − + − − + + − −.
- **Ladder W^(N)/‖F‖²:** decreases irregularly, for example:

| N | 2 | 4 | 6 | 9 | 11 | 14 | 16 | 19 |
|---|---|---|---|---|---|---|---|---|
| W^(N)/‖F‖² | 2.344 | 1.713 | 1.287 | 1.080 | 0.720 | 0.383 | 0.219 | 0.105 |

- **First sign change:** at N = 21 (−0.195).
- **Afterward it changes sign several times:**
  - +0.0052 (N = 26);
  - −0.0018 (N = 29);
  - −4.2e−6 (N = 31);
  - +9.4e−9 (N = 34);
  - **−7.05e−9 (N = 36, certified value).**
- **Ratios q_N:** do not approach 1 systematically (0.02 to 0.56 up to N = 19; then 2.86, 1.03, 3.96, 1.08, 1.00, 1.75).
- **Differences from ζ:**
  - DH has c_F of mixed signs, intermediate negative residues, and no monotonicity.
  - Only at the end (N ≥ 29) does a cancellation regime of q ≈ 1 appear, in the tail of c_F.

**Beurling** (same g* as ζ, without reoptimizing; position log n + δ, δ = ±1e−5):

| perturbation | ΔW | resulting W_T |
|---|---|---|
| n = 2, δ = +1e−5 | +5.285e−6 | +5.29e−6 |
| n = 2, δ = −1e−5 | −5.286e−6 | **−5.29e−6** |
| n = 3, δ = +1e−5 | +1.003e−7 | +1.00e−7 |
| n = 3, δ = −1e−5 | −1.003e−7 | **−1.00e−7** |

- Moving a single contact by 1e−5 changes W by an amount of order 10⁶⁴ W_T, and with the sign of −δ·c′.
- The ladder of c remains positive, but **the final residue is no longer protected**: at contact 2 the cancellation of q₂ = 0.99015 is lost.
- **Caveat.** Without reoptimizing g*, this measures sensitivity, not the pattern of the Beurling infimum. Reoptimization was not requested as a computation of existing data and was not done.

## 3. P203.3 — μ = 5 and μ = 10
**Not available.**
- **Search.** Checked `*eig*.json`, MORI15_EXTREMAL_001_data, MECH_001 and phase-155/162. Only vectors for μ = 15 exist (p0/p1).
- **What the corpus does have.** For μ = 10 only margins are cited (8.4e−44, MECH_001 l.100), without a vector.
- **What would be needed.** A ladder for μ = 5 or 10 requires recomputing the extremal: it is a new optimization and was not done.
