# R129.006 — auditor report, round 3

Target: Paper 43 after R129.005.

## Headline
**Theorem 9.8 (`𝓝 = 0`) is CORRECT** — verified step by step: ramified places exact via
P123.105 §3 (4)–(5) with probability Haar (no double `log p`); unramified shell sum
`(log p)·2Re(ζ/(1−ζ))` recomputed for both signs of `k`; archimedean symbol `−log|τ|+O(1)`
in **both** parities (singularity at `x=+1` where `sgn^ε=1`; odd kernel differs from even by
the regular `1/(2cosh(t/2))`), confirmed against P123.035 (4.1): `log π − Re ψ(1/4+iτ/2)
= −log|τ| + log 2π + O(τ^{−2})`; `T̂` real-analytic in `τ`, `→ −∞` on every component of the
dual `Ĉ_S` (correctly `C_S ≅ R^× × ∏Z_q^×`, since `−1 ∉ Γ_S`), so its zeros are discrete and
`𝓝 = {F : F̂·(T̂+c)=0 a.e.} = 0`.  Unknown constant `c` harmless.  A.10-clean.
(T1)–(T6) and the P123.017 transfer all verified.  Round 2's impossibility claim correctly
withdrawn (§13.7).

## Findings
- **F1 (MEDIUM).** Archimedean factor 2: P123.035 (3.1) gives `W_∞ = ½∫F τ_∞ d^*x`
  (`K(t)=¼[1/sinh(t/2)+1/cosh(t/2)]`, numerically checked), so (8.6) and (9.10) are off by 2
  at `∞`; harmless for `𝓝=0`, false as displayed.  Fix: `d^*x_∞ := dx/(2|x|)`.
- **F2 (MEDIUM).** Thm 8A.5's proof still asserts `c_T=c_S` while its statement carries
  `(c_T−c_S)F(1)`.
- **F3 (MEDIUM–HIGH).** (O-A5-1) is NOT reduced to an inequality: P123.105 is proved for
  locally constant tests on units only, §4 disclaims non-unit shells; P123.107 §5 disclaims
  multiplicativity.  Split into (1) the unit-block inequality and (2) a construction.
- **F4 (LOW).** (8A.14) display false as written; `W_∞` needs the `E_R` seminorms, whose
  submultiplicativity is unproved.
- **F5 (HIGH, conceptual).** A.6 reading.  Spec text: "its Hausdorff quotient `N_A` **contains
  the ruling plane**".  Stronger negative theorem than 9.13: no `D_A`-module splitting exists
  at all, since `λ_∓(a)=â(∓1/2)` is off the unitary axis.  A weak non-canonical hyperbolic plane
  exists (isotropic vectors, `T̂+c` changes sign) but is not *the* ruling plane.  Verdict:
  A.6 PROVED in P123.017 §4's exact-sequence sense; REFUTED in the spec's literal sense.
  **Governance decision, to be made in the spec file, not in the paper.**
- **F6 (HIGH, downstream).** `I_A(F,F) = ∫|F̂|²(T̂+c)` is indefinite with **infinite positive
  index**, and `(D_A^prim)^⊥ = 0`: no Hodge-index shape.  Must be transmitted to rows B/C/D.
- F7 slogan `𝓝={F: F̂=0 on supp T̂}` wrong (needs `T̂+c`).  F8 swapped exponents in Thm 9.12.
  F9 `T̂` real-valued never stated.  F10 G4 misreported (paragraph retained but now correct).
- **F12 (MEDIUM, transparency).** `T̂` is verbatim the prime+Gamma side of the explicit formula;
  A.10 not violated (`Λ` derived, no zero used), and `𝓝=0` is not a renaming — but §9.3.2/§11
  must say so, per the spec's §4 closure rule.
- **F13 (MEDIUM, cheap, valuable).** Define `T := Σ_v W_v + c·F(1)` directly (P123.042 (3.2),
  P123.035 (3.1), both proved); then `𝓝=0` is import-free and IMPORT `C` becomes a comparison.
- **F14 (MEDIUM).** A.8: account accurate; (O-A8-1) and (O-A8-2) merge into ONE theorem.
  `A_MIXED_METRIC_WORK` already constructs the analytic *target* biextension `L_tan`; the
  missing piece is the geometric *source* functor.  Closing theorems: (A.8-I) monoidal
  `Φ_det: Corr_A^tr → (periodic Deligne ruling category, λ_per)` carrying `⋆↦⊗`, `†↦`duality,
  `Tr_A ↦ λ_per`, `M ↦` rulings; (A.8-II) metric comparison with `L_tan`; (A.8-III) = O-A5-1.
  No route in the corpus; every candidate note disclaims exactly this arrow.
- F15 Thm 10.3a correct but near-vacuous (pointwise cone).  F16 G1–G11: 8 clean, 2 partial,
  1 misreported.  F17 nothing else newly false.

## Clause table
A.1 PARTIAL · A.2 PARTIAL · A.3 PROVED on G · A.4 PROVED on G · A.5 PARTIAL ·
**A.6 PARTIAL (proved in P123.017 §4's sense, refuted in the spec's literal sense)** ·
A.7 PARTIAL · **A.8 OPEN — binding** · A.9 PASSED for the formalism · A.10 PROVED.

## Verdict
`ROW A: CONSTRUCTED` is correct.  Between Paper 43 and WEIL-STRENGTH-COMPLETE stand exactly:
(1) A.8 = (A.8-I)+(A.8-II): new mathematics, no route in the corpus;
(2) A.6 = a spec decision (amend "contains" to the exact-sequence reading, in the spec file);
(3) A.5 = (O-A5-1) construction beyond the unit block;  (4) A.1, A.2, A.7 depend on the above.
