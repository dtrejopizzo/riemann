# INV_D_001: the archimedean kernel as the character of the even Weil representation (phase 194, track D)

Pen and paper, no numerics. Checked against P46 lem:K (l.349), eq:m, def:W + eq:nuw (l.1179), thm:Z, thm:shape (l.8853), prob:region (l.8984).
Notation as in P46: K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)) = 2 Σ_{k≥0} e^{−(2k+½)u}; m(τ) = C_0 + ∫_0^∞(1−cos τu)K(u)du;
on 𝒫_T, 𝔞_T(g) = ∫|ĝ|² m dτ/2π − Σ_{n<e^{2T}} v_n F(log n), F = g∗g̃, v_n = 2Λ(n)n^{−½} (the polar term is zero on 𝒫_T).

## Step 1. Candidate objects and the index check

Track brief: an object whose construction has the Γ_ℝ singularity at 0 built in (as a distribution, resolvent or operator) and which also sees Λ on log ℕ exactly.

| # | Candidate | Index hit | Status |
|---|---|---|---|
| D1 | Lévy/Dirichlet form E_μ with μ = K du + comb jumps, killed on I_T: 𝔞_T = E_{μ_T} − κ_T‖g‖², κ_T = Σ_{N_T}v_n − C_0; Green function of the killed process ≥ 0 | G2A-106_17 ("nonneg jump form minus κ_N", F3 one-atom), G2D Beurling–Deny (DEAD), P60-1, CA_I_001 Markov (λ₀<λ_A≤λ₂; O2 preserves Markov) | DISCARDED |
| D2 | Logarithmic Laplacian (Chen–Weth) Dirichlet spectral theory on I_T | R155_001 §2.3, 114_d_174, R162_501 (regularity, virial) and D1 | DISCARDED |
| D3 | Birman–Schwinger / resolvent Neumann series (chains of dilations log n₁+…+log n_k) | R186-D_B (W-det), G2D-106_58…, G8D-R155_043 (CLR) | DISCARDED |
| D4 | Krein resolvent formula for the codimension-2 constraint 𝒫_T (Vakhitov–Kolokolov count) | polar capacity 𝔊_T (P46, phase 156), CA_A boundary triples = 𝔊_T | DISCARDED |
| D5 | Tate–Beckner X + 𝔉X𝔉 = M with Poisson/Müntz and Λ∗1 = log (P^{−1}[log x, P] = −ΣΛ(n)D_n) | R160_C8_R1 (RESTATEMENT), R161_001/002 (sign-blind square), G1C-161 | DISCARDED |
| D6 | Connes distributional trace of the scaling flow (weight 1/\|1−u\|) / ray-slope distribution on ℝ_+² | L05, R158 (restatement) | DISCARDED (but see D8: the identity part coincides) |
| D7 | Heat trace / Mittag-Leffler of ψ (trivial zeros as resonances); heat trace of A_T | R164_502b (W12), thm:Z | DISCARDED |
| D8 | **Character of the even Weil (oscillator) representation ω_+ of Mp(2,ℝ)**: K = 2Θ_+ on the split torus; positivity of characters of unitary representations of the whole group (elliptic + hyperbolic, Weyl integration) | Metaplectic appears in R9-03 (sl₂ Lefschetz triple; needs discrete Cartan spectrum), R186-CCM (prolate), CA_A_003/004 (metaplectic Eisenstein, Parseval squares), CA_A_006 (abscissa transport NO-GO). No entry uses the **character** Θ_ω, Harish-Chandra/Atiyah–Bott traces, or Weyl integration / orbital integrals. | **DEVELOPED** |

New reason for D8 (the routes-tried rule requires it): what changes is the object (a character, i.e. a conjugation-invariant distribution on the whole group Mp(2,ℝ), not the scaling operator, not an sl₂ triple and not an automorphic form) and the class of positivity (positive-definiteness of the trace of ω(f∗∗f) for f on the whole group, coupling elliptic and hyperbolic directions through the Weyl integration formula). R9-03 failed because the Cartan generator has continuous spectrum; here that continuous spectrum is the source of the singularity (Prop. 3), not an obstacle to a Lefschetz decomposition. CA_A_003/004/006 work with global automorphic objects. The local character has not been used anywhere in the corpus.

## Step 2. Development of D8

**Definition.** ω is the Schrödinger model of the oscillator representation on L²(ℝ); ω_+ is its restriction to even functions. A = {a_u} is the split torus, ω(a_u)f(x) = e^{u/2}f(e^u x). K_ell = {k_θ} is the elliptic torus, ω(k_θ) = e^{−iθH} with H = ½(−∂²+x²), so the Fourier transform equals e^{iπ/4}ω(k_{π/2}). R is parity, Rf(x) = f(−x). The intertwiner is ι: L²(ℝ) → L²_even(ℝ), ι g = Φ_g, Φ_g(x) = |x|^{−½} g(log|x|).

**Prop 1 (intertwiner; PROVED).** ‖Φ_g‖² = 2‖g‖² and ω_+(a_u)Φ_g = Φ_{τ_u g}, where τ_u g(t) = g(t+u). Hence ⟨ω_+(a_u)Φ_g, Φ_g⟩ = 2F(u).
*Proof.* Substitute x = e^t. Then e^{u/2}Φ_g(e^u x) = e^{u/2}e^{−u/2}|x|^{−½}g(u+log|x|). ∎

**Prop 2 (the archimedean kernel is the even Weil character on A; PROVED as a distributional-trace computation, CITED for the identification with Harish-Chandra's character).**
For u ≠ 0, the distributional (Atiyah–Bott) trace of ω(a_u) is e^{u/2}∫δ((e^u−1)x)dx = 1/(2|sinh(u/2)|). The trace of Rω(a_u) is e^{u/2}/(e^u+1) = 1/(2cosh(u/2)). Therefore
  Θ_+(a_u) := Tr(½(1+R)ω(a_u)) = ½K(|u|).
So K(|u|) = 2Θ_+(a_u). The singularity K ∼ 1/|u| at u = 0 is the Weyl denominator |e^{u/2} − e^{−u/2}|^{−1} of the character at the identity. Agreement with the Harish-Chandra character on regular elements: Atiyah–Bott 1968; Weil-representation character formulas (Howe; Thomas): CITED.
Analytic continuation: K(iθ) = 2Σ_k e^{−i(2k+½)θ} = 2·Tr_even e^{−iθH}. This is the character on the elliptic torus, and its K-type spectrum {2k+½} consists of the exponents of K, i.e. the distances from ½ to the trivial zeros −2k. (PROVED, termwise.)

**Theorem 3 (exact identity with 𝔞_T on 𝒫_T; PROVED).** For g ∈ 𝒫_T,
  𝔞_T(g) = C_0‖g‖² + lim_{ε↓0} ∫_{|u|>ε} ( ½⟨Φ_g,Φ_g⟩ − ½⟨ω_+(a_u)Φ_g,Φ_g⟩ ) Θ_+(a_u) du − Σ_{n<e^{2T}} Λ(n)n^{−½} ⟨ω_+(a_{log n})Φ_g,Φ_g⟩.
*Proof.* By Prop 1 and Prop 2 the integrand is (F(0) − F(u))·½K(|u|). Integrating over ℝ gives ∫_0^∞(F(0)−F(u))K du, which is the archimedean part ∫|ĝ|²(m−C_0)dτ/2π by eq:m and Plancherel. The last sum is Σ v_nF(log n). ∎
In words: the archimedean part is the matrix coefficient of ω_+ paired with ω_+'s own character over A, renormalised at the identity. The prime part is the same matrix coefficient at the arithmetic points a_{log n}. Thm 4 of INV_C_001 is not contradicted: the identity holds as a principal value plus an F(0)-term, not as a measure on log ℚ. p-adic analogue (CITED, Connes' local trace formula, L05): Tr ω_{p,+}(a) at a = p^k equals p^{−|k|/2}, and log p is the period of the orbit. So the identity part of D8 is Connes' trace formula written in Weil-representation language (D6). It is not new.

**Prop 4 (where the singularity comes from; PROVED).** Take g ∈ C_c(ℝ) as a measure on A ⊂ Mp(2,ℝ). Then ω_+(g) is the Mellin multiplier ĝ(τ) on L²_even ≅ L²(dτ), which has continuous spectrum and is not Hilbert–Schmidt. Formally ‖ω_+(g)‖²_HS = Θ_+(g∗∗g) = ∫F(u)Θ_+(a_u)du, which diverges at u = 0. Theorem 3 says that the archimedean form is the renormalised difference "F(0)·∫Θ_+ − Θ_+(F)" of two divergent quantities. Its sign is indefinite: m(0) = C_0 < 0.

**Free positivity (CITED).** For f ∈ C_c^∞(Mp(2,ℝ)) with ω_+(f) Hilbert–Schmidt, Θ_+(f∗∗f) = ‖ω_+(f)‖²_HS ≥ 0. By Weyl integration this equals ∫_A |D|Θ_+ O^{hyp}_{f∗∗f} + ∫_{K_ell} |D|Θ_+ O^{ell}_{f∗∗f}. The hyperbolic integral alone is of the shape of Theorem 3. The elliptic integral is the compensator, and Harish-Chandra's limit formula at the singular element e (f(e) as a jump of orbital integrals) is the intrinsic replacement for the FP at u = 0.

**The precise gap.**
- (G1, OPEN) Find a lift g ↦ f_g ∈ C_c^∞(Mp(2,ℝ)) with O^{hyp}_{f_g∗∗f_g}|_A = F such that the elliptic compensator E(f_g) := Θ_+(f_g∗∗f_g) − (hyperbolic part) satisfies, on 𝒫_T, "renormalised hyperbolic part − comb ≥ −(something controlled by E)". With no comb, the identity Θ_+ ≥ 0 is archimedean-only. By thm:shape(A) (closure under deleting or scaling the comb, O1–O4) it cannot carry the sign.
- (G2, NO-GO for one realisation) The arithmetic coupling. The global oscillator representation of Mp(2,𝔸) (theta of weight ½) leads to metaplectic Eisenstein series, and abscissa transport 1 → ½ for those is NO-GO PROVED (CA_A_006; CA_A_004 rank-one obstruction). The elliptic terms of the Mp₂/SL₂ trace formula carry Hurwitz class numbers. The Kronecker–Hurwitz relation Σ_{t²≤4n} H(4n−t²) = 2σ(n) − Σ_{d|n} min(d, n/d) (CITED, classical) has the additive t² against the multiplicative n, and its min(d, n/d) term is a balance term at d ≈ n/d. It is the only (ℕ,+,·) hook found here: **OPEN seed, unindexed, not developed**. Its weights are σ and min, not Λ. Getting Λ would need a log-derivative, which is the Identity-5 wall of INV_C_001.

## Step 3. Self-check

- **REF-D test.** The free positivity ‖ω_+(f)‖²_HS ≥ 0 is not 𝔞_T ≥ 0. It is comb-free and therefore sign-blind for row D (thm:shape(A)). The only positive statement that would close G1, "renormalised character defect − comb ≥ 0 on 𝒫_T", is 𝔞_T ≥ 0 restated through Theorem 3. **REF-D.**
- **Problem (R).**
  - (1) Λ is used exactly, but only linearly and at the points a_{log n}. Fails as stated.
  - (2) The Fourier transform is the Weyl element of Mp₂, so the functional equation at conductor 1 is built into ω. The Euler product enters only through the local p-adic characters. "Jointly" holds only in the global realisation, which is CA_A_006 NO-GO.
  - (3) The HS norm is quadratic in f but linear in Λ. Fails.
  - (4) Not on the zero side. Passes.
  - (7)/(8) Theorem 3 is exact at the centre (the F(0)-term). Passes as bookkeeping.
  - (10)/(11) The character positivity is the same for every Γ-factor of the same type (shared with ξ_K at real places). It does not separate ζ, so the sign step would have to come from G2. Fails.
  - (B″) Theorem 3 holds for every weight vector in place of Λ(n)n^{−½}. It is comb-generic, so it is bookkeeping only.
- **Verdict.**
  - PROVED: Props 1, 2 and 4, Theorem 3 (new language: K = 2Θ_+, with the Weyl denominator as the singularity; the identity content is Connes' local trace formula).
  - CITED: character positivity and Weyl integration.
  - REF-D: the sign statement.
  - OPEN: G1.
  - NO-GO (global metaplectic realisation): via CA_A_006.
  - Live residue: the Kronecker–Hurwitz elliptic seed (OPEN, unindexed).
  - No contact with the sign.


