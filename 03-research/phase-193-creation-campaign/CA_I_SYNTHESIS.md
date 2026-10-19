# CA_I_SYNTHESIS — Front I (analysis and PDE of the extremal problem), phase 193

 Pen and paper; no numerics. **No sign contact. No negative value for ζ. No clause of (R) moved to "satisfied at a sign step".**
Memos: CA_I_000 (10 seeds, full screens, fact I0), CA_I_001 (Markov/Krein–Rutman, rigidity), CA_I_002 (virial, collar, frequency, Γ, CC).

## Verdicts
| seed | verdict | killing clause |
|---|---|---|
| I1 Markov / Beurling–Deny / Krein–Rutman / max principle | developed; NO-GO (001 Thm 2) | O2(c>0) preserves every Markov-class property and drives λ_A → −∞; KR lives below λ₀ < λ_A (Prop 1.1) |
| I2 nodal structure | lemma (≥ 2 sign changes, PROVED); DISCARD | constraint-only, survives all O; upper bound = W-pat |
| I3 rearrangement / polarization | DISCARD (Prop 5) | comb term has no Riesz inequality; 𝒫_T not invariant |
| I4 virial / Pohozaev | developed; retry NO-GO | identities B″ (hold for DH); DH falsifies only the Grönwall bound V3, which is REF-D |
| I5 Almgren frequency | DISCARD | frequency ≥ e^{(2−ε)T} (thm:M(b)); (R)(6), W-fam |
| I6 unique continuation | DISCARD | automatic (Paley–Wiener), sign-free |
| I7 Γ-convergence | DISCARD | absolute o(1) vs super-exponential λ_A; density only |
| I8 concentration–compactness | DISCARD | quadratic ⇒ no strict subadditivity |
| I9 collar boundary layer | developed; REF-D | linear in v_n at entry; edge info bounds Schur margin only from above (Lemma S(iv)) |
| I10 comparison | lemma | λ₀ monotone in comb, λ_A concave not monotone |

## PROVED facts (usable elsewhere)
I-M1. ζ's window form (without polar term) is a positivity-improving Markov form on L²(I_T); λ_A > λ₀ strictly; h* has ≥ 2 sign changes.
I-M2. (NO-GO) Any deduction using only Markov/PF/max-principle/domination/parity/Tate data/class-generic minimizer properties is closed under O2(c>0).
I-M3. (Rigidity) For every nonconstant real FE-symmetric rational E with ξE entire (all quartets O7, entire O9 twists, zero removals), the form of ξE
is non-Markov for T ≥ T_E; uses only ξ(σ) > 0 on ℝ. Entireness is necessary (real-pole twists are Markov and negative).
I-M4. 𝖯⋆ = {(S⁺), residue, entire FE Γ_ℝ, Markov ∀T} is not closed under any declared single modification except O13 (n/a) and O14 (OPEN):
the first such separation set of the campaign. As a route it is REF-D (ζ is its only instance in the declared universe).

## Proposed YES→NO moves
- "maximum principle / Krein–Rutman / comparison for σ_T(D) forces λ_A ≥ 0" → NO (001 Thm 2).
- "virial/Pohozaev identity gives the sign" → NO: identities B″; the sign-bearing form is Grönwall (REF-D), falsified by DH (ARGUED transversality).
- "a qualitative boundary-layer property of h* at ±T forces the sign" → NO: class-generic or W-pat; one-sided in Lemma S.

## What remains (for the record)
The only qualitative property found that separates ζ from O7 is an operator property of the form (Markov ∀T = purity of the a.c. kernel), and it
is a conjunction of Λ ≥ 0 (monoid) with a.c. kernel = Γ-Lévy density (analytic), not a +/· interaction. Open item: O14 Markov status (ARGUED non-Markov).
A sign step would need an inequality that uses 𝖯⋆ non-linearly; no PDE tool in this area supplies it. Area exhausted; front I stops.
