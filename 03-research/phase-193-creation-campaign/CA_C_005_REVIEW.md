# CA_C_005 — Review

## Verdict
**NUMÉRICO data ACCEPTED as data (all μ_M > 0; no negative value). The conclusion "T*₃(η) is critical" is NOT established — logical direction error (MAJOR FIX). Process note: this run was flagged in my CA_C_003 review as not strictly necessary for row D; recorded, no further numerics on this sub-statement.**

## 1. The direction error
μ_M(η) is the minimum over the span S_η ⊋ {s_w : w ∈ 𝒲_η}. Minimum over a larger set is ≤ the family infimum: μ_M is a **lower** bound for inf_{𝒲_η} Q_M/‖s_w‖². A small lower bound says nothing about whether the family infimum is small. The memo's sentence "if it is critical, so is the family" is false; the correct implication is the converse ("if μ_M is of order 1, the family has a margin"). The data (μ_M ≍ M^{−2…−3}) therefore leave the margin-or-critical dichotomy of CA_C_003 **undecided** for the smooth family. Self-review (1) concedes this as ARGUED; the Conclusion section must be downgraded accordingly: "the span S_η is critical (NUMÉRICO); the smooth family: not decided".
What the data do show (NUMÉRICO): A_M restricted to the *span* — vectors c·m^{−½} on [1, ηM], free on (ηM, M] — has bottom ≍ M^{−3}, within a factor 5–210 of λ_min. Since the collapse of CA_C_001 Obs 1 uses only constancy on [0, η], the span forms are also prime-free (log 2 only) for 2T₀ < log 2, e^{2T₀}/η < 3 — checked: T₀ = 0.3, η = 0.7 gives e^{0.6}/0.7 ≈ 2.6 ✓; T₀ = 0.15 ✓. So "criticality visible on prime-free vectors" holds for the span (NUMÉRICO), not for the smooth family.

## 2. Other checks
- Floating point: double-precision eigh has absolute error ~10⁻¹⁶‖A_M‖; λ_min ~ 3·10⁻⁹ is resolvable; the memo's caution is conservative. Not certified ✓.
- One profile only ✓ stated.
## 3. Bearing on row D
None either way: (Fam_η)/span positivity is a necessary sub-statement (CA_C_003 review). The open sub-question (is span-criticality a zero-side phenomenon via EI_002 Thm 1?) is (R)(4)/C_zeros by construction — not a route; endorse not developing it.
