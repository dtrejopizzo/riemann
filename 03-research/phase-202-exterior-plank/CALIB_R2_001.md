# CALIB_R2_001 — Calibrator, phase 203: P6 per class and interior vs exterior pairing (NUMERICAL)

Everything is **NUMERICAL**.
Data: `CALIB_001_data/P6_classes.json` and `P6_interior.json`. Scripts: `P6_calc.py` and `P6_interior.py`.

## 0. Convention
- **Datum.** The same minimum-leak r* of Mori μ = 15 and the same grid as CALIB_R1. The cutoff is X = 240 and the precision around 1%.
- **Exterior comb X.** Z^X_log r = Σ_d Λ_X(d)·D_d Zr, i.e. the weight (Λ_X∗1)(n) instead of log n.
  - 𝒜 and 2AB are left as those of ζ.
  - So LHS_X − LHS_ζ = −2⟨Zr, (Z^X_log − Z_log)r⟩.
- **Per class.** For each class q = a/b the pairs (ka,kb) and (kb,ka) are summed.
- **Combs.**
  - Exact Λ_Q, from `lambdaQ_exact.json` (Q = x² + 5y²).
  - b_n from DH, with the CERT_DH_001 recursion (double precision).
- **Units.** 10⁻⁷⁰ in the exterior.

## 1. Δ_X(q) per class (exterior)
| | Σ_q Δ_X(q) | Σ_q \|Δ_X(q)\| | classes for 90% |
|---|---|---|---|
| Epstein | **+0.0900** (= 5.152 − 5.062 ✓) | 29.4 | **160** |
| DH | **+1.6547** (= 6.717 − 5.062 ✓) | 88.6 | **82** |

**Dominant classes, with sign:**
- **Epstein:**
  - 1/1: +2.47;
  - 1/6: −1.48; 1/2: −1.46; 1/13: −0.85; 1/11: −0.80; 1/5: −0.71;
  - 1/3: +0.69;
  - 4/9: −0.60; 1/17: −0.60;
  - 5/6: +0.56;
  - 1/14: −0.51;
  - 2/9: +0.51;
  - 1/9: −0.51;
  - 8/9: +0.45; 2/5: +0.45.
- **DH:**
  - 1/1: +11.98;
  - 1/2: −8.95; 1/3: −6.56; 1/5: −4.47;
  - 2/3: +4.07;
  - 3/4: −2.77;
  - 2/5: +2.68;
  - 1/7: −2.36;
  - 3/5: +2.24; 1/4: +2.14; 3/7: +1.51; 2/7: +1.41;
  - 4/5: −1.40; 4/7: −1.14;
  - 1/10: +1.13.

**Reading.**
- No difference concentrates in a few classes. The net sum is 0.3% (Epstein) and 1.9% (DH) of Σ|Δ|. Both differences are cancellations of many O(1) classes.
- **Epstein:**
  - Weights the diagonal: +2.47, because Λ_Q∗1 < log on average.
  - Against it, the integer classes 1/p at primes with Λ_Q(p) = 0 or with flipped sign: 1/2, 1/6, 1/11, 1/13 and 1/17 are negative.
- **DH:**
  - Δ_DH(q) ≈ −(ζ class of ⟨⟩)·2 in the large classes, because the DH weights average ≈ 0.
  - That is, "removing the ζ comb": Δ_DH(1/1) = +11.98 ≈ 2·5.60, and 1/2 ≈ 2·(−4.28).

## 2. Interior pairing with the true g*
- **Formula.** ΔW_X^int = −Σ_{n<15} 2(Λ_X(n) − Λ(n)) n^{−½} c_{g*}(log n).
  - c_{g*} was computed in arb at 420 bits, with the step1_comb pipeline from F0_TEST.
  - The window is 2T = log 15, so only n ≤ 14 enters.
  - The units are those of the window (normalized g*): **without the 10⁻⁷⁰ factor**.

| | interior ΔW (O(1) units) | exterior ΔLHS (×10⁻⁷⁰) | exterior, only d < 15 |
|---|---|---|---|
| Epstein | **+0.06320** | +0.0901 | +0.208 |
| DH | **+0.04560** | +1.654 | +1.062 |

**Per n (interior / exterior·10⁻⁷⁰).**
- The interior contribution is dominated by n = 2, with c(log 2) = 0.0638:
  - In Epstein, Λ_Q(2) = 0 erases the term 2·log2/√2·c(log 2) = 0.0626 from the ζ comb.
  - Hence ΔW_Epstein^int ≈ comb_ζ = 0.0632.
- The remaining n contribute less than 10⁻³, because c(log n) is of order 5e−4 or smaller for n ≥ 3.

**Discrepancy.** It is total: around 10⁶⁸ in scale.
- In the window, changing the comb on the true g* moves W by O(10⁻²). That is equivalent to ≈ 1.3·10⁶⁷ W* for Epstein and ≈ 10⁶⁷ W* for DH.
- In the exterior, the same substitution moves the LHS by only O(10⁻⁷⁰).
- Therefore **they do not coincide, and the difference is neither gauge nor polar.**
  - thm:ext-half carries over to the exterior **only the ζ comb**: it uses Λ∗1 = log and the self-duality of ℤ under Poisson.
  - The "Λ → Λ_X in Z_log" substitution on the exterior side **is not** the exterior image of the interior comb change.
- The substituted exterior only sees the part of the change that lives in r*, which is already O(ℓ*). The interior term Σ(Λ_X − Λ)n^{−½}c(log n) depends on the whole g*, which is O(1). It lies outside the exterior datum and outside 𝒢̄_T, because its image is not an out-of-band tail.
- **Operational consequence.** Comparing combs in exterior coordinates, as was done in CALIB_R1 §4 and here in §1, measures a **different functional** from the falsifier's W_X.
  - With convention B (Z with weights a_X, dual Poisson) the identity might be restored for Epstein, but it was not computed.
  - For DH that Poisson does not exist.

## 3. Not computed
- Convention B, with Z^X of weights a_X and μ_X: it is the only one that could make the interior match the exterior for Epstein.
- That computation requires the Epstein exterior datum; it was not started, per the order not to launch anything further.
