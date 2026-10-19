# CA_B_SYNTHESIS — front B, phase 193

 Pen and paper. **No negative value for ζ; no sign contact in any memo.** No clause of (R) moved.

## 1. Candidates and verdicts (after review)
| memo | candidate | verdict | failing screen |
|---|---|---|---|
| CA_B_001 | matching / total-derivative identity I_ζζ = −J'(½)/2π | EXCLUDED | O10/O11/O12 survive; (R)(4) (sign of J'(½) = zero geometry, ARGUED); (R)(9) if symmetrized; (R)(11) |
| CA_B_002 | variational / Jensen–Riesz in the strip | EXCLUDED at pre-screen | zero-free primitive ⇒ comb-generic (B″); ζ primitive ⇒ zero geometry (R)(4); test identity unused |
| CA_B_003 | self-matching Δ_a ≡ 0 | passes the modification screen as identification; no sign | (R)(11); O7 keeps the comb, so a comb-only property survives it |
| CA_B_004 | matched σ-transport J(σ) | EXCLUDED | (B″) (identity comb-generic with test ζ); J(1) = ∞ breaks (3.3) (PROVED); only I_ζζ covered |
| CA_B_005 | "matching defect ⇒ negative bottom" | inversion FALSE | Prop 2: the bottom is Lipschitz (corollary of prop:wit-sens) |
| CA_B_006 | open-ball lemma; inner sets; (W_σ) | Lemma B = corollary of prop:wit-sens; the (iv) methodological reading WITHDRAWN; (W_σ) excluded | (W_σ) passes (R)(4), fails the inner-set test, covers I_ζζ only |
| CA_B_007 | O7/O8 action; convex decomposition | decomposition EXCLUDED | REF-D (existence), N_012 extended (t' > 1), thm:ceiling, prop:summable, class (D) |
| CA_B_008 | concavity gap Γ, angle bound | EXCLUDED | REF-D tautology, (B″), (R)(5) window observable, (R)(6)/(7) |

## 2. Facts proved (PROVED unless labelled)
1. **On-line symbol (CA_B_004 Prop 1).** For every real comb a, ½m − Re P_{a,X} = ½∂_σ log|γZ_{<X,a}|² at s = ½+iτ. For Λ, the only
   ζ is ∂_σ log|ξ₀| = 0, i.e. the FE. (A rewriting of prop:boundary + rem:fe.)
2. **Δ_a ≡ 0 ⟺ Φ_a(s) = ±Φ_a(1−s)** (CA_B_003 Thm 1). Uniqueness a = Λ is CONDITIONAL on Hamburger's hypotheses; the ε = −1 case is OPEN.
3. **Riesz decomposition** of −∂_σ log|ζ/Z_{<X}| in ½ < σ < 2 (CA_B_002 (2.1)): zeros with β > ½ contribute ≥ 0, the pole ≤ 0.
   Standard potential theory CITED.
4. **Lemma B**: the bottom is concave and Lipschitz in the weights, so positivity holds on a ball of radius λ_A/L_T, or λ_A in TV/ℓ¹. A
   corollary of prop:wit-sens. Correction recorded: P47's κ_T is directional, not a Lipschitz constant.
5. **O7/O8 action** (CA_B_007 Prop 1): in measure-comb space both keep the archimedean part and move the point ν_ζ inside the fixed convex
   set 𝒱_T^{meas}. O7 adds −kβ_z (PROVED); O8 adds atoms off log ℕ (ARGUED).
6. **Convex decomposition** of ν_ζ: its existence restates the target; with ρ_κ it needs t' > 1 on N_012's segment; class (D) otherwise.
7. **Γ angle bound** Γ ≥ min(θg_1,(1−θ)g_2)(1 − |⟨h_1,h_2⟩|). REF-D tautology: B = (𝔞^{ν_ζ} − θA)/(1−θ) exactly.
8. Transport of g (not log g) across ½ < σ < 2 needs no zero information (CA_B_006 §3). It breaks at the pole s = 1 (CA_B_004 §6).

## 3. Endorsed YES→NO moves (none affects the region (R))
- "(R)(4)" and "(R)(11)" → NO for the matching identity (CA_B_001).
- "uses that the test is ζ's own partial sum" → NO for every Jensen/Riesz reading (CA_B_002).
- "transport uses that test and symbol come from the same ζ" → NO (CA_B_004, by Prop 1).
- "J-convexity across σ = 1" → NO.
- "self-matching (Δ ≡ 0) as sign carrier" → NO, on the operative grounds: O7 keeps the comb, plus (B″). The openness argument was withdrawn.
- "Euler-tail class membership as sign carrier" → NO (CA_B_006).
- "explicit convex inner set as sign carrier", "concavity gap", "minimizer misalignment" → NO (CA_B_007/008).

## 4. What an admissible piece would have to be (the output of this front)
Any split 𝔞^{ν_ζ} = Σθ_i𝔞^{ν^{(i)}} is exact and affine. So a proof via pieces is admissible only if **some piece ν^{(i)} that carries Λ's
fluctuation is certified (b(ν^{(i)}) ≥ −c_i, with Σθ_ic_i ≤ the other pieces' margin) by an argument that**:
(P1) is not a lower bound on 𝔞^{ν_ζ} or on 𝔞^{ν_ζ} − (explicit form). Otherwise it is REF-D (CA_B_008 §2).
(P2) is non-linear in Λ at the sign step, not through spectral data of the target form ((R)(3), (R)(5)).
(P3) reads the form or minimizer, not the comb alone. O7 keeps the comb (lem:shape-quartet), so a comb-only property (Hamburger,
     Δ ≡ 0, Euler-tail vanishing) survives it.
(P4) uses no zero data (R)(4). In particular no log-derivative may be transported across (1,3/2] (NT_013/014), and no |g| transport may
     cross the pole at 1 (CA_B_004 §6).
(P5) is not an identity valid for every measure comb (B″). Concavity, angle bounds, Riesz/Poisson, and derivative-of-log identities all are.
(P6) uses the on-line FE matching (Prop 1: the only ζ in the symbol at σ = ½) jointly with Euler at the sign step, as an inequality.
**Obstacles met by each seed:** (a) matching derivative — sign = zero geometry. (b) Jensen/Riesz — comb-generic or zero geometry; test
unused. (c) self-matching — an identity at a point, comb-only (O7). Transport — comb-generic with test ζ, pole at 1. Inner sets /
decomposition / gap — REF-D, since every split writes the target via its own spectral data.
**Status:** OPEN. No candidate input satisfying (P1)–(P6) has been identified on this front. Front B stops here per coordinator.
