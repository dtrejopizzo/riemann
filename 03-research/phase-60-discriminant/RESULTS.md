# Phase 60 — Discriminant: RESULTS (frank closure)
**Verdict:** NO-GO. The central thesis (multiplicativity controls the sign of the Weil
residual, measurable via the discriminant of the localized form) is **refuted** by real and
reproducible experiments. All code runs in the venv and reproduces the validated gates. --- ## Thesis tested > The sign of the Weil residual is not controlled by the location of the zeros but by
> **multiplicativity** (Euler product). Isolate it by comparing ζ (Euler) vs. non-multiplicative
> controls in the localized Weil form. ## Experiments (all reproducible, validated P7 engine) ### E1 — `E1_zero_side_blindness.py` (runs, gates PASS)
The validated zero side `M_zeros` is a function of the **multiset of zeros only**.
- Every ON-line configuration (any density/spacing, i.e. any RH-true L-function) stays on the floor: λ_min/tr ∈ [+2.3e-5, +1.1e-1] ≥ 0.
- The only sign-mover is shifting zeros OFF-line (RH-status).
- **Conclusion:** the zero side measures RH-status, it is **blind to multiplicativity**. Separating ζ from L_DH here = separating by off-line zeros = location = **circular** (pre-registered NO-GO §5).
- ⇒ the thesis lives entirely in the **arithmetic side** `M_arith` (P). ### E2 — `E2_multiplicativity_discriminant.py` (runs)
Methodological contribution: fix the archimedean block A (ζ, a=1/4) and vary ONLY the
multiplicativity of the coefficients (unknown normalization cancels in the relative
comparison). C(L) = λ_max(A^{-1/2} P A^{-1/2}).
- ζ (multiplicative): C = 1.98.
- shuffle / random (same support, same value distribution, no positional correlation): C ≈ 0.31 ± 0.05.
- ζ at **+31σ (shuffle), +41σ (random)**. *Apparent* GO. ### E2b — `E2b_kill_confound.py` (runs) — THE DECISIVE CONTROL
Suspicion: shuffle/random break the position(log n)↔value correlation, so the +30σ could
be "coherent (smooth in log n) sum vs incoherent", NOT multiplicativity. Λ(n)=log p is
trivially smooth in log n.
Smooth, **non-multiplicative**, magnitude-matched control: | coefficient | C | multiplicative? |
|---|---|---|
| ζ (real Λ) | 1.98 | yes |
| flat (constant Λ̄) | **2.44** | no |
| loglin (linear fit of Λ) | **2.11** | no |
| logn | **2.21** | no |
| shuffle / random | 0.31 | no | **The smooth, non-multiplicative controls match or EXCEED ζ.** ζ is not even the most
coherent (C(ζ) < C(flat)). --- ## Verdict The separation seen in E2 was **smoothness/coherence in log n**, not multiplicativity. The
"Euler" signature is **spurious**. Combined with E1: > **Both sides of the localized Weil form are blind to multiplicativity.**
> The zero side sees only zero location (RH-status). The arithmetic side, via the localized
> form with a smooth envelope (Hermite/Slepian), sees only the **smooth envelope of the
> coefficients** (first moment/density) and washes out the Euler correlations. Structural reason (new, precise): multiplicativity is a fine arithmetic correlation
(between Λ at p, p², q…) that lives at the scale of individual log p. The smooth envelope of
the localized form integrates it and erases it. This is consistent with T3.4 (the arithmetic
"band" was a basis artifact) — the same finger pointing: **no fine arithmetic structure
survives in the localized form.** This is MW-2 (arithmetic propagation) in new disguise. ## Consequence for RH The multiplicativity-discriminant route **does not lead to a condition for the sign of
Weil** with the available observables. RH remains behind the cross-place wall (MW-3/MW-5),
intact. This phase is **closed**. Recorded as [NG-F1] in NO-GO-LIST. ## What it DOES leave (frank)
1. A relative discriminant instrument (A fixed, vary multiplicativity) that **cancels the normalization** — unblocks the baseline confound of Phase3-results, and is reusable.
2. The hard finding: the localized Weil form is blind to multiplicativity on both sides, with a structural reason. Cleanly closes direction δ of PLAN-RH-FRONTIER.
