# CA_H_001, CA_H_002 — Review

## CA_H_001 (δ-structures, Wronskian, Frobenius lifts)
**CONFIRMED: all NO-GOs as labelled. One FIX.**
| claim | check |
|---|---|
| Prop 1.1, Lemmas 1.2–1.3 | δ_p(n) = (n−n^p)/p unique on ℤ ✓; valuations ✓; n^p − n ≥ n^p/2 ⟺ n^{p−1} ≥ 2 ✓ |
| Prop 2.2 | (i) a^pδb − b^pδa = (a^pb − ab^p)/p ✓; (iii) W(a,c) − W(a,b) = (a^{p+1} − ac^p + ab^p)/p = a·C_p(a,b) with c − b = a ✓ |
| Cor 2.3 | product case PROVED; general ARGUED ✓ |
| Props 3.1–3.3 | φ_p f(s) = f(ps) ring endo lifting Frobenius ✓; necklace integrality ✓; Ψ_p(ζ) = −Σ_{q^j, p∤j}(Λ/log)N^{−s}; −dΨ/ds = ζ′/ζ(s) − ζ′/ζ(ps) ✓ (re-derived) |
| Prop 3.5 | Σ2Λ(n)n^{−p/2} = 2|ζ′/ζ(p/2)| ✓ |
| Lemma 4.1(ii) | **FIX:** 𝔸(s^{∗p}) = (1/2π)∫F̂₀²|P_s|^{2p}(m − comb) is the target on a sub-family; it is NOT "the p-th moment family of CA_D_001 Thm 1′" (that theorem has amplitude |Z_X|^{2k} with order-k Tate conditions, a different object), and is not thereby FE-generic. Conclusion "no δ-calculus on tests produces an inequality" stands |
| Prop 5.1 | lift to W₂ ⇒ (1/p)dF̃: F*Ω¹ → Ω¹ non-zero (Deligne–Illusie, CITED) ⇒ p(2g−2) ≤ 2g−2 ✗ for g ≥ 2 ✓ |
| Prop 5.2 | no elliptic curve over ℤ (Tate) ✓ CITED |
| Prop 5.3 | Γ_n = nf₁ + f₂ (Γ·f₂ = n, Γ·f₁ = 1), Γ_n·Δ = n+1, primitive (f₁−f₂)² = −2 ✓ |
| Cor 5.4 | NO-GO for 𝒦_δ (graphs of global Frobenius lifts) ✓; non-graph correspondences (Hecke, scaling) correctly left to MW-5 |
Index: "Buium δ / Mason–Stothers / Frobenius-lift polarized objects → NO-GO (declared classes)". ENDORSED.

## CA_H_002 (Erdős invariant; Kronecker anatomy)
**CONFIRMED. Two FIXes.**
| claim | check |
|---|---|
| Thm 2.2(i) | a on prime powers ⇒ f_a additive ✓; Erdős (CITED) ⇒ f_a = c log ⇒ a = cΛ ✓ |
| Thm 2.2(ii) | O12: inert q gives Λ_K(q) = 0, Λ_K(q²) = 2log q ✓; O10: r_Q(2) = r_Q(3) = 0, r_Q(6) = 4 ⇒ not multiplicative ⇒ log-coefficients not on prime powers ✓ |
| Cor 2.3 | O7 keeps comb ⇒ excluded ✓ |
| Prop 2.4 | (s∗v^a)(N) = 2N^{−½}Σ_{n|N,n≥2}a(n)w(N/(nM)), w ≡ c there ✓ |
| Thm 3.1/3.2 | Haar integrates χ(q) to 1[q=1]; ν₀ to c₀(log q) ✓ |
| Prop 3.3 | Weyl limit ✓ |
| Prop 3.4 | F̂₀ ≍ τ^{−2} ⇒ tail of F̂₀² ≍ U^{−3} ✓; reading ARGUED ✓ |
| Cor 3.5 | REF-D ✓ |
FIX 1 (retry): Thm 3.1 is CA_C_002 Prop 2(d) (PROVED, reviewed) extended from S-unit boxes 𝕋^S to the full solenoid Ĝ without the S-unit hypothesis. Cite it; the extension is a clean improvement, not a new mechanism.
FIX 2 (scope of (S⁺)): (S⁺) is an asymptotic property of the infinite comb (f_a(n+1) − f_a(n) → 0); at any fixed window it is invisible (O3 tail deletion agrees with Λ on N_T). It separates the comb-changing falsifiers only as T → ∞, and is comb-only (O7) — consistent with Cor 2.3.
Verdict: H5 PROVED separating invariant, excluded at O7; H6 coordinates (B″), sign content REF-D. Index entries ENDORSED.
Numerics/norms: none run ✓; Epstein test performed analytically (r_Q) ✓.
