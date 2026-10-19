# CA_B_002 — Review

## Verdict
**EXCLUDED (zero-free reading: survives O1–O7, O15, (B″); ζ reading: (R)(4)); additionally (R)(5) "local on the negative set" (thm:nolocal / W-loc) since (2.1) is pointwise in τ. (2.1) CONFIRMED (PROVED modulo CITED potential theory in an unbounded strip).**

## 1. Claims
| claim | check | label |
|---|---|---|
| q(s) = 2∫Re R_X dμ_s | window form = (1/2π)∫σ_T|F̂|² and Re R_X = ½σ-symbol (CA_B_001 (1.2)); requires μ_s built from the test's own Dirichlet polynomial as in EI_002 Thm 1 ✓ | CONFIRMED |
| ΔH = 2πΣδ_ρ − 2πδ₁ in S | log|Z_{<X}| harmonic (finite zero-free product) ✓ | CONFIRMED |
| signs in (2.1) | G ≤ 0, G=0 on σ=½ ⇒ ∂_σG(½+iτ,·) ≤ 0 (inward); zero terms ≥ 0, pole ≤ 0 ✓; matches Hadamard (β−½)/|s−ρ|² | CONFIRMED |
| Riesz/Green representation on the unbounded strip | needs H = O(log|τ|) growth — true (ζ finite order, CITED); FIX: say so, and that the zero sum converges by exponential decay of ∂_σG_S in |τ−γ| | PROVED modulo CITED |

## 2. Modifications
With the zero-free primitive (CA_B_001 §5) (2.1) is a Poisson identity valid for every comb: O1 a_P, O2 Λ+cδ₂, O3, O4, O5, O6, O7 Beurling, O15 Poisson all survive ⇒ **EXCLUDED** (lem:shape-ident). With the ζ primitive, the extra content is zero terms; O8 quartets (add a quartet ⇒ add nonnegative zero terms, plus FE-partners in the boundary datum) and O9 f_t survive in form — the identity does not see whether zeros are on the line.

## 3. (R): (4) NO, (5) NO (pointwise in τ, any probability measure — exactly the local class), (8) NO, (11) NO. Agree; memo's observation that the test identity is not used is correct and decisive.

## 4. REF-D: the sign step "zero terms + DtN ≥ 0 on supp μ_s" is zero geometry, not D in other coordinates; but restricted to minimizing μ_s it is the window form itself — REF-D in the trivial sense. 5. Retry: MW-7, P33-10, NT_011 (same family: Hadamard/Jensen on log|ζ|). New in form only.
Endorsed move: "Jensen/Riesz uses the test = ζ's partial sum" YES→NO; (R)(4) YES→NO.
