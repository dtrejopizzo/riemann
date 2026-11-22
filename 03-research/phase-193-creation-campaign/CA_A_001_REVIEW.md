# CA_A_001 — Review
Checked against P46 prop:boundary, eq:symbol, thm:shape, lem:shape-ident, prob:region; index README, 06_.

## Verdict
**EXCLUDED (O11, O12; (R)(1),(5),(8)) — memo's NO-GO for the norm class CONFIRMED (narrow scope). The "line-doubling" obstruction is NOT endorsed as a general NO-GO for PSL₂(ℤ) (§3).** Two FIXes.

## 1. PROVED claims
| claim | check | label |
|---|---|---|
| Lemma 1 (coefficients of E(·,s) see ζ only via ζ(2s), ζ(2s−1), σ_{2s−1}) | read off the constant term and Fourier coefficients | CONFIRMED (literal statement) |
| Lemma 2 | invariant Hermitian form ⇒ Casimir symmetric ⇒ λ⟨v,v⟩ = λ̄⟨v,v⟩; Im s(1−s) = t(1−2a) = t/2 at a=¼ | CONFIRMED PROVED. FIX 1: irreducibility is not needed (any v with ⟨v,v⟩>0 suffices), and the reducibility set is s ∈ ℤ in this normalization, not s ∈ ½+ℤ |
| Cor 3, Maass–Selberg | −φ′/φ(½+iτ) = 2ξ′/ξ(1−2iτ)+2ξ′/ξ(1+2iτ) = 4Re ξ′/ξ(1+2iτ) ✓ | CONFIRMED. FIX 2: the comb is −4ΣΛ(n)n^{−1}cos(2τ log n) (sign), conditionally convergent at σ=1 (distributional) |

## 2. Modifications O1–O15 applied to the object (MS norm inequality ‖Λ^Y E‖² ≥ 0)
The inequality is a norm, true for every scattering coefficient that comes from a lattice. O11 (Epstein: evaluate at CM points / other lattices) survives; O12 (ζ_K via Bianchi/Hilbert modular Eisenstein) survives; O10 (ζ·R) undefined (no automorphic realization); O1–O7, O15 inapplicable to a statement whose comb is Λ(n)/n at abscissa 1 — the window vector v_n = 2Λ(n)n^{−½} never enters. **EXCLUDED by O11/O12** and by (R)(1).

## 3. Clauses of (R) and the line-doubling claim
(R)(1),(3),(5),(6)–(8),(10),(11): not met (agree with memo). (R)(4): met vacuously.
**Objection to §4 ("obstruction is representation-theoretic") and to its ARGUED extension:** ζ on the line ½ is reached on the unitary axis without Re s = ¼, via Mellin/Hecke integrals of E(iy,½+it) (∫(E−const)y^{w−½}dy/y ∝ ξ(w+it)ξ(w−it)/ξ(1+2it)), or via Zagier's renormalized Rankin–Selberg of |E(·,½+it)|² (products of four ξ's with the free variable w on Re w=½). Lemma 2 forbids invariant positivity at spectral parameter ¼; it says nothing about positivity in the Mellin variable. So the NO-GO holds for the class of Cor. 3 (norms in the spectral variable) and **no further**. The metaplectic escape (→CA_A_003) is one escape; Mellin-in-y/Rankin–Selberg in w is another and must be screened (it is a [zeros]/product-of-ξ object; expect (R)(3) linear-in-ζ-products and O12 survival).

## 4. REF-D
Not D in other coordinates: decides nothing about the window form.

## 5. Retry
Partly: R9-15, G4D-R152_002 (Hecke on L²(Γ\ℍ), DEAD). The MS-norm side is new on record; the result is negative.

## Ledger moves endorsed
"Eisenstein norm (spectral-variable) positivity carries the window comb" YES→NO (PROVED for Cor. 3 class). "Line doubling is a barrier for all PSL₂(ℤ) positivity" — NOT endorsed.
