# Review of corrections: analysis, spanning and auxiliary estimates

Version reviewed: working tree relative to HEAD `97fb4e78`, 28-11-2026. No manuscripts were modified. This verdict replaces the corresponding local (b) verdicts of the first audit, without certifying other proofs by extension. The new correction of the characters of P53 is reviewed on another front.

## Verdict on the changes

| Current text | Verdict | Verification of application and constants |
|---|---|---|
| P46:277, Hermitian form | (a) | `a bar(b′)+b bar(a′)` is Hermitian sesquilinear and its diagonal is exactly `2 Re(a bar b)`. It does not alter W or its coefficients. |
| P46:1898, ε₉ | (a) | γ₁≥14.1347 is declared, compatible with the certificate already reproduced. The weaker estimate 0.01576 using 14.13 also gives ε<0.016; the denominator 0.484 and the final constant remain. The cut-offs T do not change. |
| P46:2093–2096, M_R | (a) | AM–GM on y,y,2(R²+a−y), all non-negative, gives `y²(R²+a−y)≤4(R²+a)³/27`. For R²<a/2 equality is not attained on y∈[a,R²+a], but the bound does hold. M_R is preserved, and hence the coercive inequality for all R>0. |
| P49:2245–2251, FJ | (a) | The substitution x=gh uses left Haar and `e(g⁻¹x)=d c(x⁻¹g)`. Integrability by F∈L¹, |c|≤1. The Bochner vector of the next step and the formal degree d do not change. The erroneous identification of translations of the previous proof is eliminated. |
| P51:4452,4510–4518, `pm:siegel(c)` | (a) | With g,x in fixed compact sets a common U is chosen with the γxU disjoint. The sets Ω₁⁻¹γΩ₂U escape from each compact set when γ leaves a finite set; the majorant M′ is integrable. Locally uniform convergence is obtained. The bound of the total sum remains global in g. It suffices for continuity and for the subsequent applications; global uniformity of tails is not required. |
| P51:10505–10515, tube | (a) | β has weight 1 and σ weight 2; Q=2ρk+2ρ². The new Q satisfies Q≤(k+2ρ+1)²/2=r²/2. With radius Q²(T²+1)², the quotient of volumes is `(1+1/Q)^Q≤e<3`; T¹⁰ and the factor 3 are preserved. The range of `pbo:local` does not change. |
| P52:1810–1812, floors | (a) | The action preserves the flag and is unitriangular, not pointwise on all its vectors. On V_l it only adds combinations of lower floors. The uses in `pfr:ss-floors` depend on that flag, on the normalisation by G^(l) and on the convolution measures; they do not need vector-by-vector fixing. No Jacobian factor appears: the triangular changes have determinant 1. |
| P52:4361–4367, dual cut | (a) | u invertible and u⁻¹→0 produces exhaustive frequencies and dual neighbourhoods decreasing to 0. With absolute convergence domination applies; the continuity of densities of `pff:fibre(a)` gives the limit of their means. The two dual measures preserve product 1, without residual factor or change of parameters. |
| P53:2252–2253,2640, P and S non-empty | (a) | The decay proof chooses a place of the support. The added hypothesis is necessary for that argument and holds in exchange: S is the set of places of a non-trivial modulus. In the grids the modulus contains the chosen primes of π_M, even for trivial twist. Hence no application of the chain loses its range. |
| P53:4431–4455, slices | (a) | False Hilbert boundedness is replaced by continuity in moments. For coherent states the majorant is C(1+|y|)^(N+M). Superposition gives the bound by ||v||_(N+M); for local continuity in x, M=0 and ||v||_N<∞ suffice. With N=0,M=2p+1 one integrates in real dimension 2p. The vectors used in M1/M2 have the required moments, as do their translates by points of compact sets. The exact constant of the exchange is not changed by this analytic repair. |
| P53:13765–13769, `pgq:slice` | (a) | The product is now r₀⁻¹r, and the change of variable uses left Haar. The norm of the inverse of the minimiser is t₀. s≥16n² and `2·16^(n²)Vτ` are maintained by the ball lemma with s/2. |
| P53:14572–14576, covolume | (a) over the field of the data | `det x·overline(det x)=1` implies total adelic modulus 1: cancellation at split places, valuation 0 at the inert ones. E/E⁺ is unramified at all the finite places of these data (P53:665), so that no ramified case within its scope is omitted. `(2⁻ᶠ|D_E|^(1/2))^n` is preserved. The same proof would hold at a ramified place on replacing "inert" by "non-split". |
| P53:16967, citation of `pm:siegel` | (a) | Reproduces the corrected hypothesis of compactness of g and x. |

## Propagation to volume 58

The modified blocks of the five `main.tex` files were compared by algorithm with the text of 58. **The 30 added/modified blocks appear literally in 58**, including those on the characters of 53 whose mathematical validity is the concern of the other front. The result is saved in `../evidence/propagation_v2_analysis.json`. In addition the diffs of 58 for FJ, tube, flag, cut and coercivity were inspected.

This check certifies textual propagation of the corrections, not automatic reconstruction of all the proofs of 58. In particular, the strong phase formula of 49 was not modified and still requires the distinction explained in REVIEW-PHASE49-V2.

## Consequence for the private verdict

No mathematical failure persists in the repairs of this table, and no loss of constants nor inadvertent restriction of the range used was found. The earlier results that depended on them can use the corrected versions. The verdict on the whole series must still integrate the independent review of the exchange of 53, the other fronts and the difference between proving the sufficient phase lemmas and justifying literally their strong formulation.
