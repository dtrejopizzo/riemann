# R166_402 — Survey (B): mechanisms of phases 164–166 against the three requirements

Surveyor: read-only pass. Sources: R164_190, R165_190, R166_190 (reference audits, the binding labels), the
round files cited per row, and master grid R162_2300 §5 (phase 164–166 entries). No new mathematics; labels are the
audited ones.

## Criteria (literal, from R166_190 "Cierre de la phase 166")
- **(i) GLOBAL in X:** the mechanism uses the whole node set X of the witness F (G², the phase / harmonic measure ω(E), the
  full form W_T on F), not finitely many node jets. Re G(t_q)² is the k = −1 jet (R166_201 Thm 1.3), so any jet-local
  device fails (i).
- **(ii) ATOMIC beyond the window, coupled to X:** Λ(n) for n ≥ e^{2T_c} (Λ ≥ 0, multiplicative, the tail 𝒯_X or
  ζ_{≥X}) enters with structure/sign **and** is coupled to the node set / zero side. Notation: ✓ = both; ◐ = the atomic
  side beyond the window enters with sign/structure but is **not** coupled to X (no witness in the statement); ✗ = no
  atomic data beyond the window.
- **(iii) NOT reducible:** not (1.1) on a single test (E1), not window-only (killed by f_t), not zero-set-only (killed by
  M_m). Applied literally: a mechanism killed by another falsifier (ζ_B, P_{a,c}, ζ_θ) still passes (iii) literally; the
  wall column records what killed it.

Score = #✓ + ½·#◐. Sorted by score, then phase.

## Table

| # | mechanism | file / thm | (i) | (ii) | (iii) | wall | residue | why (one line) |
|---|---|---|---|---|---|---|---|---|
| 1 | Prop 4: Λ-tail at real height | R164_501 Prop 4 | ✓ | ✓ | ✗ | E1 + drop-term (Thm 3.1) | (★_cell) | Σ_ρ G²y/(z²+y²) = 𝔄_y − G(iy)²𝒯(iy), 𝒯(iy) = Σ_{log n ≥ 2T} Λ(n)n^{−½−y} > 0: the whole G² (i) and the atomic tail with sign (ii), but it is **(1.1) on the single test Ψ_y**; it is an identity, and the tail weighs e^{−(log n₀−2T)y}, visible only at y = O(1), where the quartet weighs y/γ_q² |
| 2 | dlVP on G² (Ψ = G²[w₀P₀ + w₁(P_a+P_{−a})]) | R164_601 Prop 2.1, Thm 3.2–3.3 | ✓ | ✓ | ✗ | W2/M + Thm 3.1 | O164.601.1 = (★_cell) weighted by K | the test exists (tail sign from G² monotonicity in |y|), but it is one test of (1.1); dropping the signed tail gives inequalities true for any zero set; what is left is ½ − δ_q ≤ c/log γ_q (Fejér cap + archimedean ≍ log γ_q) |
| 3 | drop-term principle | R164_601 Thm 3.1 | ✓ | ✓ | ✗ | E1 (meta) | (★_cell) | proves that every inequality obtained by dropping the signed tail from a (1.1) test holds for the true zeros whatever they are; it excludes a quartet only together with an independent lower bound, which is (★_cell) |
| 4 | exact tail-sign condition for G²K | R164_601 Props 1.1–1.3 | ✓ | ✓ | ✗ | E1 | — (refutes R166_190's uncertainty observation) | tail has sign ⟺ g*Ǩ keeps its sign on [2T,∞), g = (G²)^∨: global and atomic, but it characterises the admissible single tests of (1.1) |
| 5 | rough-zeta split 𝒯^det + ζ_{≥X} | R166_103 B1–B2 (grid §5) | ✗ | ◐ | ✓ | W-Landau (no FE: Thm A) / W-identification (with FE: Cor R.1) / unilateral = Landau = E1 | the "box": an exact relation between ζ_{≥X} on ½<Re s<1 and the witness that reads cos, Re G(t_q)² | 𝒯_X = 𝒯^det (window, holomorphic in Im x > −½) − ζ′_{≥X}/ζ_{≥X}; every off-line residue lives in ζ_{≥X}; separates f_t, f_χ, M_m (iii ✓). But X here is the cutoff e^{2T}, **not the node set**: no witness enters, so (i) ✗ and the coupling half of (ii) is missing |
| 6 | Thm R: sinc annihilation (positivity + gap ⟹ ζ) | R164_401 Lem 2–3, Thm R, Cor R.1–R.3 | ✗ | ◐ | ✓ | W-identification | none (O164.101 ⟺ ¬RH, Cor R.2) | N ≥ 0 off ℕ beyond a gap (1,X) + FE + poles ⟹ f = ζ. The atomic/positive side beyond the window carries everything, and f_t is excluded (Cor R.3, negative coefficients). But the output is **identification**, not a sign: no node set, no zeros, so (i) ✗ and nothing is coupled to X |
| 7 | Theorem L: Witt-lattice error bound (integrality) | R164_201 Thm L (audit R164_291) | ✗ | ◐ | ✓ | integrality blind to zeros (Lemma D); threshold 1/3 inside 𝒦_θ | O164.201a: below 1/3 off the lattice (Goal A OPEN) | integrality of multiplicities beyond the window is an atomic property (ii-half), and it is a class statement, neither window nor zero-only (iii). It never sees zeros or nodes (Lemma D "blind to zeros"), so (i) ✗ and (ii) is not coupled |
| 8 | Lemma D (integrality defect inequality) | R164_201 Lemma D | ✗ | ◐ | ✓ | blind to zeros | as #7 | same mechanism as #7 in inequality form |
| 9 | off-lattice Beurling below 1/3 | R164_503 pts 1–7 | ✗ | ◐ | ✓ | Goal B ≥ RH (+ quadratic GRH); rounding stops at x^{1/2} | O164.503a/b | an O(x^θ) error gives holomorphy only, nothing on zeros; the positive direction is stronger than RH |
| 10 | positive tail / Bernstein (Landau–Pringsheim for the tail; ζ_B) | R164_102 Thm L, Cor L.1, Thm A, Cor A.1 | ✗ | ◐ | ✓ | W-Landau (positivity sees only poles) | O164.102.1, closed by Thm R | a positive tail beyond the window with the window of ζ still allows a zero at an arbitrary β+iγ (Thm A); the witness of ζ does not transfer; no X |
| 11 | Prop I / Hamburger (support in log ℕ) | R164_102 Prop I | ✗ | ◐ | ✓ | W-identification | — | integer support ⟹ ζ_B = ζ; identification, no sign |
| 12 | θ−1 moments | R166_103 (γ), G1 | ✗ | ✗ | ✓ | P_{a,c} falsifier (θ−1 > 0, exact FE, zeros off the line) | — | θ−1 is a full Dirichlet-series positivity, not atomic Λ; only ξ(ρ)=0 is a moment; W_T is not affine in the coefficients |
| 13 | Prop D: deletion | R164_101 Prop D | ✗ | ✗ | ✓ | — (a falsifier-type fact) | "the sign lives in window × Z_X" | D has exactly the zeros and the Z_X of ζ and is negative at T ≤ 0.4608: kills every statement that reads only the zero side, so it is a guide for (iii), not a mechanism |
| 14 | Thm H: finite-modification rigidity | R164_102 Thm H | ✗ | ✗ | ✓ | W-identification | any member with an off-line zero moves infinitely many zeros | Q = ζ_B/ζ with finitely many zeros/poles ⟹ Q ≡ 1 (FE + Phragmén–Lindelöf); no Λ, no nodes |
| 15 | hybrid Euler–Hadamard cut (KZ) | R164_101 Lemma H, Thm KZ, Thm E1, Cor E1′, Prop EB | ✓ | ✗ | ✗ | E1 | O164.101 (→ Thm R) | W_T(F,H) = −(1/π)∫F̂Ĥ^#θ′_{X′} is the full form (global). The kernel M has Fourier support at u ≥ 2T, invisible to type-2T products, so the atomic tail drops out (ii ✗); term by term it is (1.1) and is valid for f_t, f_χ, M_m |
| 16 | Thm SA: positive annihilator = kernel | R164_501 Thm SA, Cor SA.1 | ✓ | ✗ | ✗ | E1 | Rem 4.8a | every test ≥ 0 annihilated by the kernel equation is ĤĤ^#, H ∈ E_c (a cone tied to the critical node density T_c/π, so it is global); no type to spare, no Λ |
| 17 | phase identity (harmonic measure ω(E)) | R165_201 Thm 2, Cor 2.2, Thm 3 | ✓ | ✗ | ✗ | zero-set-only (Thm 3(a): sin/cos interlace at critical density with G(x₀−iδ)² < 0) | ω(E) at the contact = Rem 4.8a | 4Re G(t_q)² = 4|G(t_q)|² cos 2(Φ_Z ± πω(E) + Ψ_out): the only exact global reader of the sign (i ✓), but pure zero/node geometry, valid for M_m |
| 18 | node flow / Cauchy identity S | R165_202 | ✓ | ✗ | ✗ | E1 (M_m) | node monotonicity, parity simplicity OPEN | no jumps in T; real-rooted at every simple T; quadrature w_x ≥ 0; S = 0 at nodes, S′ = d_x ≥ 0; all node-global, all valid for M_m |
| 19 | parity coupling | R166_202 Prop 1, Thm 2, Thm 3 | ✓ | ✗ | ✗ | vacuous or E1 | O202.1 (T_e = T_o, no sign) | W_T(F^ev) + W_T(F^odd) = 4W_{T/2}(Φ) is an identity of (1.1); the cross identity is empty term by term |
| 20 | Toeplitz kernel (Makarov–Poltoratski) | R166_301 | ✓ | ✗ | ✗ | W-TK: sign-blind (σ vs −σ, 4.1) + window symbol | O166.301 (matrix MP), low | a truncated Toeplitz kernel on K_Θ is global, but kernels cannot see positivity and the symbol is window data |
| 21 | determinant / Szegő / spectral moments | R164_502 L0–L8 | ◐ | ✗ | ✗ | window-only (L1: A_T depends only on σ̌ on (−2T,2T); f_t) | — | invariants of the compressed operator are global in the operator, not in X; Widom L6: frequencies outside the window cancel exactly |
| 22 | bilinear / Selberg (N < e^{2T}) | R164_502 L7–L8 | ✗ | ✗ | ✗ | window-only (f_t); extra content = identification | — | the separation is in T, never in k |
| 23 | Det+: Riemann–Pólya truncation | R165_101 | ✗ | ✗ | ✗ | zero-set-only (valid for f_t, M_m, f_χ) | bracket 0.8047 < T_c ≤ min_ρ τ(ρ) | h = Ξ·R/Q^k with its own test, not the witness's nodes; the tail is archimedean (Φ ~ exp(−πe^{2|u|})), with no Λ beyond the window |
| 24 | Det−: amplification test | R165_102 Thm 1, Cor 2, Prop 4 | ✗ | ✗ | ✗ | zero-set-only (false for M_m with large δ) | the contact is set by min_ρ T_det | a local test at one zero; frame constants O(ΛT) against the quartet gain e^{2δT}/δ |
| 25 | separation by charged zeros (Rolle), clustering | R165_202 | ◐ | ✗ | ✗ | E1 (M_m) | (SEP_J) replaces (EC) | gap-by-gap local statement; counting does not localise (S(t) = O(log γ)) |
| 26 | node-weight singularity 1/δ² | R166_101 Thm 2.1 | ✗ | ✗ | ✗ | E1 | weights see δ only to second order (curvature) | (t−x₀) cancels the Cauchy pole; the quartet weighs in d_x like two on-line zeros; the atomic separator is never used |
| 27 | exchange flow in s | R166_102 | ✗ | ✗ | ✗ | W2/M in the variable s; M_m passes | margin ½ log log log(1/s) > 0 | ∂_s 2Re F̂² has indefinite sign, decided by ω(E); atomicity at s = δ* never enters a window bound |
| 28 | free mechanism (α): convolutions / Loewner / 1/δ sine term | R166_103 (α) | ✗ | ✗ | ✗ | f_t (convolutions of type ≤ 2T), M_m (Loewner) | — | the singular 1/δ term is −Im G(t_q)²/δ, the sine, not the cosine of (★_cell) |
| 29 | sine–cosine jets (jet hierarchy) | R166_201 Thm 1.1, 1.3, Cor 1.4, Thm 2.1, Prop 2.2 | ✗ | ✗ | ✗ | E1 on both sides | the k = 0 jet W(F,H_{x₀}) = kernel equation = window ∧ zero data | this is the theorem that **establishes** (i): node jets k ≥ 0 are blind to ψ; atomic sampling Σ v_n k_F(x₀, log n) oscillates (ARGUED) |

## Grouped by pairs

**{i, ii} (global + atomic tail coupled to X; fail (iii) because each is (1.1) on one test, and the drop-term principle applies):**
- #1 Prop 4 (R164_501): the only identity in the corpus where Λ ≥ 0 at all heights enters the witness with a sign
- #2 dlVP on G² (R164_601 Prop 2.1)
- #3 drop-term principle (R164_601 Thm 3.1) (the meta form of the failure)
- #4 exact tail-sign condition for G²K (R164_601 Props 1.1–1.3)

**{ii, iii}:** none literally. Relaxed (◐ = atomic beyond the window with structure, but **not coupled to X**):
- #5 rough-zeta split (R166_103 B1): passes (iii) because it separates f_t, f_χ and M_m; fails (i) because X is the cutoff, not the node set; positivity of 𝒯^new is blind (Thm A), identifies (Cor R.1) or is unilateral (E1)
- #6 Thm R (R164_401): passes (iii) (excludes f_t, Cor R.3); fails (i) because its output is identification, with no witness or zeros
- #7–8 Theorem L / Lemma D (R164_201): passes (iii); fails (i) and the coupling, being blind to zeros by design
- #9 off-lattice Beurling (R164_503), #10 positive tail (R164_102), #11 Hamburger (Prop I): the same pattern

**{i, iii}:** none. Every mechanism that is global in X (#15–20) is a zero/node identity or window data, so it is E1 or zero-set-only.

**All three:** none (agrees with R166_190 "Ningún mecanismo del corpus cumple (i)–(iii)").

## Reading
The corpus splits into two disjoint families. Family P (#1–4) is global in X and uses the signed atomic tail, but it lives
inside (1.1) on a single test, where Thm 3.1 neutralises the tail. Family Q (#5–11) uses atomic data beyond the window in
a way that no falsifier shares, but it never contains the node set, and its positive content ends in identification
(W-identification) or in blindness to zeros (W-Landau, Lemma D). The missing object is exactly the "box" of R166_103: a
relation from family Q (ζ_{≥X} on ½ < Re s < 1) that reads the cosine Re G(t_q)² of family P's witness, without
collapsing to a single test of (1.1).
