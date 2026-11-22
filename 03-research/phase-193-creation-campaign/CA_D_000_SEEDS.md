# CA_D_000 — Phase 193 round 6+: seed generation, PHASE / HARDY-FUNCTION area

Pen and paper; no numerics.
**No negative value of the window form for ζ is produced or claimed in this round.**

Read before seeding: CA_A_SYNTHESIS, CA_B_SYNTHESIS ((P1)–(P6)), CAMPAIGN_LEDGER (O-labels per P46 l. 8331–8345), P46 §20
(thm:shape, lem:shape-ident, prop:shape-phase, prob:region (1)–(11)), ROUTES-TRIED-INDEX README + 06_, EI_003 (+ review).
There are no CA_C_* files in the folder at the time of writing, so there is nothing to avoid duplicating.

## Common frame (EI_003 Thm 1 = P46 prop:shape-phase, PROVED)
X = e^{2T}; Z_X = ζ/Z_{<X} = 1 + Σ_{n≥X} z_X(n)n^{−s}; Θ = Θ_X; Z_T = e^{iΘ}Z_X(½+iτ) real; 𝔞_T(F) = (1/π)∫Θ′|F̂|²dτ on P_T.
Convention used in all CA_D memos: F̂(τ) = ∫F(x)e^{iτx}dx; for a tempered g on ℝ_u, G(τ) = ∫g(u)e^{−iτu}du, so ∫|G|²dτ = 2π∫|g|²du.

## Seeds and pre-screen

Legend: ✓ passes, ✗ fails, — not applicable. "Index" = grep of ROUTES-TRIED-INDEX + 03-research.

| # | seed (one line) | index / retry? | (R) clauses | (P1)–(P6) | O-modifications, (B′), (B″), REF-D | verdict |
|---|---|---|---|---|---|---|
| D1 | **Spectral first moment (Mandel / Wigner–Smith time delay).** For h = e^{iΘ}F̂: 𝔞_T(F) = −2∫u\|ȟ(u)\|²du. D says the phase-modulated test has nonpositive mean frequency. | no hit for Mandel / time delay / analytic signal; not a retry | (3) ✗: linear in Θ, hence in Λ; (11) ✗ | (P2) ✗, (P5) ✗ | identity holds for every comb (B″) and every finite measure (survives O11, O15) | **DISCARD as a route.** Kept as the coordinate in which D2 and D9 are written. |
| D2 | **Hardy-amplitude transfer.** Replace the unit amplitude by \|Z_X\| = \|Z_T\|. G = F̂·Z_X has phase −Θ (mod π), and its spectrum is {window part in [−T,T]} ∪ [T,∞): the Euler gap 1<n<X plus the Tate condition, which kills the pole. | no hit. Nearest: CA_B_001 (J′(½) with frozen weight F̂₀²\|Z_{<X}\|²; sign there ARGUED to be zero geometry). D2 uses a different weight and proves a sign. Not a retry. | (2) ✓ (Euler gap × FE phase × pole); (3) ✓ (\|Z_X\|² = exp of comb); (4) ✓ (no zeros); (11) ✗ for D (§ verdict) | (P4) ✓, (P6) ✓ as an inequality; (P1) ✓ (a different form, not a bound on 𝔞^{ν_ζ}); (P5) ✗ within the FE class | holds for every real Dirichlet series with FE, Γ-factor and at most a simple pole at 1, including DH/Epstein (O10) and ζ_K (O12). So it cannot be the sign step (thm:shape(C)). Not a bound on prime sums (no B′). | **SURVIVES AS A TOOL** (new PROVED inequality, not a sign step). Developed in CA_D_001. |
| D3 | **Landau / max-modulus phase inequality** for Z_X, which has nonnegative coefficients supported on n ≥ X: \|Z_X(σ+iτ)\| ≤ Z_X(σ), argument bounds, Bohr–Jessen (lead (a)). | R164_102 Thm A, Cor A.1 (W-Landau): every such property lives on σ>1 and holds for ζ·E, which has the window of ζ, a positive tail and off-line zeros anywhere. Bohr–Jessen: G6E-159 DEAD. | (4) ✗ once transported; | (P4) ✗ (crossing the pole at 1) | ζ·E falsifier (PROVED) | **DISCARD (retry of DEAD R164_102).** Side remark (CA_D_001 §4): D2 does not use z_X ≥ 0; only the gap matters. |
| D4 | **Kramers–Kronig / Dirichlet-to-Neumann** between log\|Z_X\| and arg Z_X on the line. | EI_003 §4; CA_B_002 (Riesz); CA_B_004 Prop 1 (Cauchy–Riemann for γZ_{<X}) | for Z_X: (4) ✗ (holomorphy of log Z_X in Re s>½). For γZ_{<X}: an identity, (3) ✗ | (P4) ✗ / (P5) ✗ | B″ | **DISCARD.** |
| D5 | **Riemann–Siegel chirp + comb as frequency modulation** (lead (b)): θ′ = ½m is the carrier; the comb is an FM perturbation with Jacobi–Anger sidebands. | R163_603 DEAD (RS/AFE is FE-only data, shared by f_χ) | (3) ✗ (mean frequency is linear in the phase, by D1) | (P2) ✗ | f_χ (O-type F3) | **DISCARD.** |
| D6 | **Scattering causality (Wigner bound)** for S_X = e^{2iΘ} = Z_X(1−s)/Z_X(s): time delay ≥ −radius for causal S. | phase 161 product-Hardy / typed scattering (PARTIAL, REF-D); phase 118 W3 DEAD | causality of S_X ⟺ no poles of S_X in the physical sheet ⟺ no zeros of Z_X in Re s>½: (4) ✗ | (P4) ✗ | — | **DISCARD.** |
| D7 | **de Branges / Kreĭn phase function** with phase Θ. | ES-16 CIRCULAR/FALSIFIED; P46 Kreĭn indeterminacy (phase 155 r5) | a phase function of a Hermite–Biehler E needs Θ′>0 pointwise, which fails (σ_T(0)=C₀−A<0, thm:nolocal). A positive extension of Θ′ is a certificate (thm:Z). | (P1) ✗ | class (D) | **DISCARD.** |
| D8 | **Amplitude-exponent homotopy** α ↦ W(α) = ∫Θ′\|F̂\|²\|Z_X\|^{2α}. W(0) is D; W(k) ≥ 0 for k ∈ ℕ_{≥1} (by D2 with k-th order Tate). | no hit | at non-integer α, Z_X^α is single-valued in Re s>½ only without zeros there: (4) ✗. Integers do not control α=0: no Carlson-type rigidity, since W is a signed integral. | (P4) ✗ off ℕ | — | **DISCARD as a route.** The integer statement is included in CA_D_001 (Thm 1′). |
| D9 | **Closure of the transferred cone.** If the spectral densities \|F̂_j Z_X\|², F_j ∈ P_T, were L¹((1+\|Θ′\|)dτ)-dense among the \|F̂\|², F ∈ P_T, D would follow from D2. | no hit; it is a question about D2 | it would be a valid deduction (it uses D2 jointly with an approximation); whether it is (11)-specific depends on the approximation | — | — | **SURVIVES PRE-SCREEN as a question.** Developed in CA_D_002. Answer: NO-GO, PROVED. |

## Ranking of survivors
1. D2 (CA_D_001): new PROVED inequality, zero-free, uses Euler × FE × pole jointly. Not ζ-specific (FE class). Tool only.
2. D9 (CA_D_002): decides whether D2 can reach D by density. A NO-GO would localize the sign.

No seed gives sign contact. Results of the developed memos are summarized at the end of CA_D_002.
