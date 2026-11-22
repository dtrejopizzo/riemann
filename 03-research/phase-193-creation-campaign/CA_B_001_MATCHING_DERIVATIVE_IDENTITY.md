# CA_B_001 — Candidate (a): the matching / total-derivative identity (phase 193)

 Pen and paper; no numerics.
**No negative value of the window form for ζ is produced or claimed.**

## 0. Corpus / index check
- P46 prop:boundary (m = −2Re ζ'/ζ(½+iτ)), rem:fe (D_σ = 2Re ξ'/ξ(σ+iτ), D_{1−σ} = −D_σ, D_{1/2} = 0; symmetrizations of D_σ vanish), (R)(9).
- EI_002 Thm 1 (PROVED): Q_M(w) = (1/π)∫F̂₀²|ζ_w(½+iτ;M)|² Re R_{X'}(½+iτ)dτ; EI_002 review: the family test is NOT ≈ cζ at bounded height (polar term M^{½−iτ}W(½−iτ) of size M^{½}).
- EI_003 Thm 1: R_X(½+iτ) = Θ_X' + iZ_T'/Z_T, Z_{<X}(s) = exp Σ_{n<X}Λ(n)n^{−s}/log n.
- Index: NT_011 (pointwise curvature of log|ξ| = zero geometry), MW-7, P33-10 (Jensen δ = off-line energy). Not tried before in this exact form (σ-derivative of a test-weighted mean square with the test = the symbol's own primitive); closest: rem:fe.

## 1. The identity (PROVED, elementary)
Let γ(s) = π^{−s/2}Γ(s/2), ξ₀ = γζ (so |ξ₀(σ+iτ)| = |ξ₀(1−σ+iτ)|, FE + reality), g_X := ζ/Z_{<X}.
(1.1) For every real τ off the zero ordinates: Re R_X(½+iτ) = −½ ∂_σ log|g_X(σ+iτ)|²|_{σ=½}.
(1.2) Equivalently, since ∂_σ log|ξ₀|(½+iτ) = 0 (FE): Re R_X(½+iτ) = +½∂_σ log|γ(s)Z_{<X}(s)|²|_{σ=½} = ½m(τ) − Re P_X(½+iτ).
Proof. R_X = −(log g_X)' (EI_003); Re of a holomorphic log-derivative is ∂_σ log|·|. (1.2): log|g_X| = log|ξ₀| − log|γZ_{<X}|. ∎
**Matching identity.** If the test were exactly ζ (it is not; §3), then |ζ|²Re R_X = −½|Z_{<X}|²∂_σ|g_X|², and with the frozen weight
ω(τ) := F̂₀(τ)²|Z_{<X}(½+iτ)|², J(σ) := ∫ω(τ)|g_X(σ+iτ)|²dτ:  (1/π)∫F̂₀²|ζ|²Re R_X dτ = −(1/2π) J'(½).   (1.3)  PROVED (J finite near σ=½: ζ polynomial growth, CITED; F̂₀ rapidly decaying).

## 2. Pre-screen (before any development)
| test | outcome |
|---|---|
| a_P / Λ+cδ₂ with test kept m^{−½}w | (1.3) needs test = exp(Σ a(n)n^{−s}/log n) AND the on-line identity (1.2) for that series. For a ≠ Λ the test (coefficients 1) is not exp of the comb, so (1.3) has no analogue: **the matching is destroyed — passes the key test**. But (1.2) with γZ_{<X,a} in place of γZ_{<X} holds for EVERY comb (it is the definition of the symbol): the symbol side of (1.3) is comb-generic (lem:shape-ident); only the identification ζ ↔ test is ζ-specific. |
| (R)(1),(6),(7) | only through the frozen weight; the sign step (§4) does not see the weights at scale λ_A/κ_T |
| (R)(2) Euler × FE | YES as identification: Euler (test = exp of comb), FE (∂_σ log|ξ₀| = 0) |
| (R)(3) non-linear | YES (|g_X|² is exp of the comb) |
| (R)(4) zero information | **NO** — §4: the sign of J'(½) is decided by the zeros in ½ < β < 1 and the pole |
| (R)(9) symmetrization of D_σ | **NO if one symmetrizes**: replacing ω|g_X|² by the σ-symmetric ω|ξ₀|² gives K(σ)=K(1−σ), K'(½)=0 identically (rem:fe) |
| (R)(11) specific at the sign step | **NO** — the sign step is "J decreasing at ½", which is a zero statement |
| thm:shape (B″) | the identity (1.1)–(1.2) itself is comb-generic; (1.3) is not, but carries no sign |
Pre-screen verdict: **fails (R)(4), (R)(11); and the exact form is not on the family** (§3). Not developed further as a route; the
useful product is the observation of §5.

## 3. The family is not the matched test (PROVED, from EI_002 Thm 2)
ζ_w(½+iτ;M) = ζ(½+iτ) + M^{½−iτ}W(½−iτ) + ρ_M. Inserting into Q_M gives (1.3) times c² plus I_pp + 2I_ζp + I_ρ (EI_002 (3.1)); the
three extra pieces are not derivatives of anything matched to the symbol, and at bounded height I_pp dominates (EI_002 review §1).
So on the actual minimizing family the matching identity is at best one of four pieces, not the window form.

## 4. Why the sign step is zero geometry (ARGUED, standard)
J'(½) = ∫ω|g_X|²·2Re(g_X'/g_X)(½+iτ)dτ, and by Hadamard 2Re ζ'/ζ(½+iτ) = −m(τ) + 2Σ_ρ Re 1/(½+iτ−ρ) + (pole) ; the ρ-sum is
pointwise 0 for on-line ρ and the pair {ρ,1−ρ̄} sums to 0 on the line. The sign of J'(½) given the symbol is therefore the
weighted Re P_X-correction plus m — i.e. the original window form — and no information is gained; any attempt to sign J'(½) through
log-convexity of J (Hardy/three-lines, CITED) gives only J'(½) ≥ (J(½)−J(½−h))/h, a comparison with σ < ½ where the FE returns the
same form with |χ|² weights: circular. NO-GO (ARGUED) for (a) as a sign mechanism.

## 5. What survives (PROVED; for the record)
The "second occurrence" of ζ in the symbol is, on the line, exactly the FE vanishing ∂_σ log|ξ₀| = 0: Re R_X = ½∂_σ log|γZ_{<X}|²
(1.2), a zero-free, entire, comb-generic primitive. Hence **on the critical line the symbol carries no ζ beyond Γ and the finite comb**;
a coupling "same ζ on both sides" must be made **off the line** (σ ≠ ½) or through the FE as a global identity (CA_B_003).

## 6. Self-review
- (1.1)–(1.3): one-line, correct; zeros of ζ on the line make |g_X|² vanish, integrand extends continuously (EI_002 Thm 1 remark). ✓
- "Passes the key test" is only identification (W-identification, thm:shape(C)): the a_P-modified object is undefined, not shown false. ✓ recorded honestly.
- Columns moved YES→NO: "(R)(4) no zero information" and "(R)(11) specific at sign step". No property of the region changes.
