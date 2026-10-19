# R162_190 — Check of R162_001 (continuity of λ_A)

Referee: verification pass. Sources checked: R162_001; Paper 47 main.tex eq:form,
eq:Aform, lem:mbounds, lem:monoT, lem:contT, thm:O, lem:firstcontact, rem:contA.

## Verdict: CORRECT WITH FIXES

The theorem (λ_A continuous on (0,∞)) and the consequence (lem:firstcontact holds without its
continuity hypothesis) are correct. There are two small gaps, both in bookkeeping and both
closed by one line each. Neither affects the conclusion.

## Line-by-line

**Step 1 (dilation, no polar term).** Checked against lem:contT.
- (i) Archimedean: |m(s/r)−m(s)| ≤ M_1|log r|, where M_1 = sup|x m'(x)|. The bound depends only on r, so it is trivially uniform in T'.
- (ii) Comb: the shift is |log n|·|1/r−1| ≤ 4T'|1/r−1| ≤ 8T|1/r−1| =: δ. The sum runs over n < e^{4T'} ≤ e^{8T}, so it is bounded by S_{2T}. The split at |τ| = δ^{-1/2} gives
  S_{2T}(δ^{1/2}‖F‖² + 2‖F‖_Q²/log(2+δ^{-1/2})).
  This is uniform over T' ∈ [T/2,2T] once T is replaced by 2T in δ and S. The note only says "the same η". It should record this replacement. **Cosmetic.**
- Contacts entering or leaving are handled correctly. c_{U_rF}(u) = c_F(u/r) vanishes for |u| ≥ 2rT', so summing over one common range n < e^{8T} is exact for both windows.
- Form-norm bound: from mbounds(ii), log(2+|τ|) ≤ m+C_1. From mbounds(iii), the comb is ≥ −A_{T'}‖F‖² ≥ −A_{2T}‖F‖². Together these give ‖F‖_Q² ≤ a_{T'}(F) + (C_1+A_{2T})‖F‖². Correct.
- The polar step (iii) of lem:contT is not needed and is not used. **OK.**

**Step 2.** A(U_rF) = r^{-1/2}∫F(t/r)e^{t/2}dt = r^{1/2}∫F(s)e^{rs/2}ds. Subtracting r^{1/2}A(F) = 0 is legitimate. By Cauchy–Schwarz on I_{T'} ⊂ I_{2T}, ε(r) → 0 uniformly in T'. The same holds for B. **OK.**

**Step 3 (correction space).**
- Zero-extension invariance holds. For φ supported in I_{T/4}, c_φ vanishes on |u| ≥ T/2. So by eq:Aform, a_S(φ) is the same for every S ≥ T/4. The bilinear values follow by polarization, since φ_i ± φ_j and φ_i ± iφ_j are also supported in I_{T/4}.
- The φ_i are smooth, so they lie in every form domain.
- M is invertible: e^{±t/2} are independent on I_{T/4}, so (A,B) maps C_c^∞(I_{T/4}) onto C².
- A(u−G) = B(u−G) = 0, and u−G ∈ D_{rT'}.
- ‖G‖ ≤ ‖M^{-1}‖(‖φ_1‖+‖φ_2‖)·2ε and a(G) ≤ C_3ε², where C_3 depends on the fixed Gram matrix a(φ_i,φ_j).
**OK.**

**Step 4 (cross term): minor gap, fix needed.**
- The positivity claim is correct. eq:Aform gives a_S ≥ (C_0−A_S)‖·‖², because Lev ≥ 0 and |c_F(log n)| ≤ ‖F‖². Since A_S ≤ A_{2T}, we get b := a_S + M_0‖·‖² ≥ 0 whatever the sign of M_0.
- The gap: Cauchy–Schwarz for b bounds |b(u,G)|, not |a(u,G)|. In fact a(u,G) = b(u,G) − M_0⟨u,G⟩, so the displayed inequality is missing a term.
- **Fix:** |a(u,G)| ≤ b(u)^{1/2} b(G)^{1/2} + |M_0|‖u‖‖G‖. The extra term is ≤ |M_0|C_2ε → 0. Add it to ω(r). Severity: **minor**; the conclusion is unchanged.

**Step 5 (Rayleigh quotient): minor gap, fix needed.**
- Nonvanishing of v: ‖v‖ ≥ 1 − C_2ε > 0 for r near 1. This should be stated.
- The gap: when a(v) < 0, the step from a(v)/‖v‖² to a(v) needs a two-sided bound on a(v). We have
  a(v)/‖v‖² − a(v) = a(v)(1−‖v‖²)/‖v‖²,
  so we need |a(v)| bounded, not only a(v) ≤ V+ω. The lower bound is available from Step 4: a(v) ≥ −M_0‖v‖² ≥ −|M_0|(1+C_2ε)².
- **Fix:** with |a(v)| ≤ max(V+ω, |M_0|(1+C_2ε)²), the correction is ≤ const·ε(r)/(1−C_2ε)², uniformly in F. Severity: **minor**.

**Step 6.**
- Bounds: the lower bound C_0−A_{2T} comes from Step 4. The upper bound is λ_A(T') ≤ λ_A(T/2) for T' ≥ T/2, by monotonicity (lem:monoT). λ_A(T) is finite, since P_T∩D_T has codimension 2 in D_T.
- (a) Uses T' = T. Near-minimizers with a ≤ λ_A(T)+δ ≤ V exist. **OK.**
- (b) Uses T' = rT ∈ [T/2,2T] with factor 1/r, which is admissible since (1/r)T' = T. It needs Step 5 to be uniform in T', which it is (see Step 1). **OK.**
- Letting δ → 0 gives continuity at T. Since T is arbitrary, λ_A is continuous on (0,∞). **OK.**

**Consequence.**
- If RH fails, Paper 45 Thm 11.3 gives T_0 with λ_A(T_0) < 0. By lem:monoT, {T: λ_A(T) ≥ 0} is an initial interval.
- Set T_* = sup{T: λ_A(T) ≥ 0}. Then T_* ≥ log 2 (Paper 42).
- λ_A(T_*) = 0: continuity from the left gives ≥ 0, and continuity from the right gives ≤ 0.
- T_* < T_0 strictly, because λ_A(T_0) < 0 and λ_A is continuous.
- This T_* coincides with the inf{T: λ_A < 0} used in lem:firstcontact.
- Attainment: the sublevel sets are compact on the closed subspace P_{T_*} (thm:O proof; Bombieri Thm 3), so H_{T_*} has compact resolvent and 0 is an eigenvalue.
- Parity: J preserves P_T (it swaps A and B) and commutes with H_T. So the finite-dimensional kernel contains a vector of definite parity.
- The hypothesis of lem:firstcontact is therefore discharged, and rem:contA can be updated.
- The "Minimality" caveat (λ_A may vanish on an interval ending at T_*) is correct and harmless.
**OK.**

## Issues

| # | Location | Severity | Issue | Fix |
|---|----------|----------|-------|-----|
| 1 | Step 4 | minor | Cauchy–Schwarz is applied to b = a+M_0‖·‖², but the bound is written for a; the term −M_0⟨u,G⟩ is dropped | add \|M_0\|C_2ε to ω(r) |
| 2 | Step 5 | minor | only the upper bound of a(v) is invoked; the Rayleigh step needs \|a(v)\| bounded, and ‖v‖>0 is not stated | use a(v) ≥ −M_0‖v‖² (Step 4); ‖v‖ ≥ 1−C_2ε |
| 3 | Step 1 | cosmetic | uniformity in T' is asserted rather than shown | write δ = 8T\|1/r−1\| and S_{2T} = Σ_{n<e^{8T}} v_n explicitly |

No issue with: η/ε uniformity, contacts entering or leaving, nonnegativity of a_S+M_0‖·‖², zero-extension
invariance of a_S(φ_i,φ_j), λ_A(T_*)=0, attainment, parity.
