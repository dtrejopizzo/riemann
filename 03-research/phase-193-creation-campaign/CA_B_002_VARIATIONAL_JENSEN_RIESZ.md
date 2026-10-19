# CA_B_002 — Candidate (b): variational / Jensen–Riesz characterization of the bottom (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed.**

## 0. Corpus / index check
P47 prop:AM (window quotient), rem:fe, prop:shape-twist (O9: pointwise curvature of log|ξ|); NT_011 + review (ζ̃ = ζ·R model:
pointwise statements on log|ξ| are zero geometry); MW-7 (Hadamard barrier), P33-10 (Jensen excess = off-line energy), NG-A5.
Not tried in this form (Riesz decomposition of the symbol's primitive in a strip, averaged against the test measure μ_s).

## 1. The object
For a test s in the window domain let μ_s(dτ) := F̂₀²|P_s(½+iτ)|²dτ / ∫F̂₀²|P_s|² (probability measure). By prop:AM(ii)+EI_002 Thm 1,
the window quotient is q(s) = 2∫Re R_X dμ_s (PROVED) and the bottom is inf_s q(s). With H := log|g_X|, g_X = ζ/Z_{<X} (CA_B_001 (1.1)),
q(s) = −∫∂_σH(½+iτ) μ_s(dτ).                                                                                     (1.1)
Candidate (b): positivity of the bottom as a Jensen/subharmonicity inequality for H, with the test = ζ's own partial sum.

## 2. Riesz decomposition in the strip S = {½ < σ < 2} (PROVED modulo CITED standard potential theory)
ΔH = 2πΣ_{ρ∈S}δ_ρ − 2πδ_1 (log|Z_{<X}| harmonic: Z_{<X} entire zero-free). With G_S the Dirichlet Green function of S (ΔG = δ,
G ≤ 0, G = 0 on ∂S) and Poisson kernels P_½, P_2 of S:
−∂_σH(½+iτ) = 𝒩[H|_{σ=½}](τ) + 𝒩₂[H|_{σ=2}](τ) − 2πΣ_{ρ∈S}∂_σG_S(½+iτ,ρ) + 2π∂_σG_S(½+iτ,1),   (2.1)
with 𝒩, 𝒩₂ the Dirichlet-to-Neumann contributions of the two boundary lines. Since G ≤ 0 inside and = 0 on σ=½, ∂_σG_S(½+iτ,·) ≤ 0:
each zero with β > ½ adds a **nonnegative** term, the pole at 1 a **nonpositive** term. (Consistent with Hadamard: Re(−1/(s−ρ)) =
(β−½)/|s−ρ|² on the line.) The σ = 2 boundary is the absolutely convergent Euler tail (ζ-specific: Euler product).

## 3. Pre-screen
| test | outcome |
|---|---|
| key test a_P / Λ+cδ₂, test m^{−½}w kept | (1.1) holds for every comb with H_a := −log|γZ_{<X,a}| (CA_B_001 §5: on the line the primitive can be taken zero-free). With that primitive ΔH_a = 0 in S: (2.1) has **no** zero/pole terms and is a comb-generic Poisson identity — **survives every O1–O6: excluded by lem:shape-ident**. With the ζ-primitive H = log|ζ/Z_{<X}| the extra content is exactly the FE pairing (the β<½ partners live in the boundary datum H|_{σ=½}) |
| does the sign step use "test = ζ's partial sum"? | **NO.** The test enters only through μ_s ≥ 0; (2.1) is pointwise in τ. Any probability measure works — the matching is not used |
| (R)(4) zero information | **NO** — the only non-generic terms in (2.1) are zeros in S and the pole: zero geometry (NT_011) |
| (R)(8) positive part jointly with negative set | the bottom chooses μ_s concentrated on U_T; (2.1) gives no lower bound on U_T beyond the zero terms |
| (R)(11) | **NO** — the sign step is "zero terms + DtN ≥ 0 on supp μ_s", a zero statement or a restatement |
Verdict: **excluded at pre-screen.** Two clean reasons: (i) with the zero-free primitive it is comb-generic (B″); (ii) with the ζ
primitive the only extra input is zero geometry (R)(4). In neither reading does the identity of the test with ζ's partial sum enter.

## 4. Jensen proper (ARGUED, one line)
Jensen's inequality ∫log|P_s|dμ ≤ log∫|P_s|dμ and Hadamard three-lines bounds on log|ζ| bound H from above; q needs a lower bound on
−∂_σH, i.e. an upper bound on the growth of H into σ > ½, which is (2.1) again. Nothing new.

## 5. Self-review
- (2.1) sign of ∂_σG at the boundary: G ≤ 0, G(½+iτ)=0, so the inward derivative is ≤ 0 ✓; pole sign opposite ✓. The decomposition needs
  H|_{σ=½} ∈ L¹ against the Poisson kernel: log|ζ(½+iτ)| has log-singularities at zeros, integrable ✓ (CITED standard).
- The statement "off-line zeros with β>½ help the symbol pointwise" is correct but useless: their partners 1−ρ̄ sit in the boundary datum.
- YES→NO moves: "uses that the test is ζ's own partial sum" (stated as the mechanism of the seed) → NO for every Jensen/Riesz reading;
  (R)(4) → NO. No region property moves.
