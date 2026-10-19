# INV_B_001 — The pair surface 𝒮 over ℤ: classes, pairing, index statement, proof attempt at ½log3 (phase 194, track B)

Mandate: invent first, audit later. Labels: DEFINITION / PROVED / CONJECTURE / HEURISTIC / OPEN. No numerics run. No negative value for ζ produced.

Notation. Window form: for F even, supported in [−2T,2T], F = g*g̃ with g supported in [−T,T],
  𝔞_T(g) = W(F) = F̂(i/2)+F̂(−i/2)  −  Σ_{n≥2} Λ(n) n^{−1/2} (F(log n)+F(−log n))  +  A_ℝ(F),
A_ℝ(F) = archimedean term (Γ_ℝ log-derivative / Lévy-type principal value at 0). Target (row D on the declared carrier): W(g*g̃) ≥ 0 on the primitive classes (F̂(±i/2)=0 version and its polar-corrected version, as in Paper 47).

## 1. The object (DEFINITION)
𝒮⁺ := (ℝ_{>0} × ℝ_{>0}) with points (x,y), measure dx dy/(xy)^{1/2}·(xy)^{-1/2}·xy = dx dy (half-density normalisation), and the integral sublattice 𝒮(ℤ) := ℕ×ℕ ⊂ 𝒮⁺.
𝒮 := 𝒮⁺ / ℚ_{>0}^× acting diagonally, (x,y) ↦ (qx,qy). The ratio coordinate u = log(y/x) is invariant; the "transverse" coordinate s = ½log(xy) carries the additive/real structure (the integer lattice ℕ×ℕ is NOT invariant under the diagonal action — this is where + enters: the quotient remembers ℕ×ℕ only as the counting measure ν = Σ_{m,n≥1} δ_{(m,n)} pushed down).

Divisor classes (DEFINITION), all as currents on 𝒮⁺ invariant in s up to the counting measure:
- Δ = {y = x} (u=0).
- Γ_a = {y = a x}, a>0 (u = log a); the multiplicative shift graphs. Γ_a∘Γ_b = Γ_{ab} (composition of correspondences). For a = n ∈ ℕ the graph meets the integral lattice in {(m, nm)}.
- Smeared classes: Γ_F := ∫ F(u) Γ_{e^u} du. The test classes are Γ_g for g ∈ C_c^∞(−T,T).
- Fibres: H = {x = const}, V = {y = const}; in the u-coordinate they are the two ends u→±∞, and they pair with Γ_F through the Mellin evaluations F̂(±i/2) (the two ends of the half-density e^{±u/2}).
- Ample class: 𝒜 := H + V (the "hyperplane"), 𝒜² = 2 after normalisation, 𝒜·Γ_F = F̂(i/2)+F̂(−i/2).

## 2. The pairing (DEFINITION + PROVED reproduction)
Intersection of two graphs: Γ_a and Γ_b (as correspondences composed with transpose) meet over the integral lattice exactly at the points (m, n) with n/m = a/b ∈ ℚ; weighting each transversal meeting at a prime-power ratio p^k by its local multiplicity log p · p^{−k/2} (half-density Jacobian times the valuation length at p) gives
  ⟨Γ_a, Γ_b⟩_fin := − Σ_{n≥2} Λ(n) n^{−1/2} [δ(log a − log b − log n) + δ(log a − log b + log n)].
Archimedean meeting (the fibre direction s, real place): ⟨Γ_a,Γ_b⟩_ℝ := A_ℝ(δ_{log a − log b}) — i.e. the self-intersection of the diagonal's normal bundle is the Lévy density of Γ_ℝ (divergent at u=0, renormalised by principal value; the "Δ² = 2−2g = −∞" of infinite genus).
Polar part: ⟨Γ_a, Γ_b⟩_pol := contribution of 𝒜: (a/b)^{1/2}+(b/a)^{1/2}.
Total ⟨D,E⟩ := pol + ℝ + fin, extended bilinearly to smeared classes.

PROVED (by unwinding, bilinearity): ⟨Γ_g, Γ_g⟩ = W(g*g̃) = 𝔞_T(g). Consistent with CA_F_003 Lemma 1: on test classes there is no freedom; the content must be in how the index is proved.

Geometric reading (HEURISTIC but formula-level): the prime term is exactly the set of TRANSVERSAL intersections of Γ_g with the shifted lattice lines through the near-coincidence locus {(m, n): n ≈ k m}: the support of g*g̃ at log n means Γ_g and Γ_{n}Γ_g meet. CA_J_002's frustrated cycles (additive path m→m+1→…→2m closed by the multiplicative edge Γ_2) are the closed loops in 𝒮(ℤ) mixing the s-direction (+1 steps) and the u-direction (Γ_2): they are the 1-cycles whose existence distinguishes 𝒮 from a product of two curves.

## 3. Hodge-index theorem for 𝒮 (CONJECTURE HI_𝒮)
Let N_T = span{𝒜, Δ, Γ_g : supp g ⊂ [−T,T]} with ⟨,⟩. Then:
(HI) ⟨,⟩ has exactly one positive direction on the polar part and is ≤ 0 … in the sign convention where the window form is the NEGATIVE of the intersection form on 𝒜^⊥: for every D ∈ N_T with ⟨D,𝒜⟩ = 0, −⟨D,D⟩_int ≥ 0, equivalently 𝔞_T ≥ 0 on primitive classes.
(CS) Castelnuovo–Severi analogue: for every test g, |⟨Γ_g, 𝒜⟩|² ≤ 2·(polar-normalised) ⟨Γ_g,Γ_g⟩^+ ... i.e. |F̂(i/2)+F̂(−i/2)| bounded by 2·||g||_W where ||·||_W is the window norm (Weil's "|N−q−1| ≤ 2g√q" shape, with genus replaced by the archimedean Lévy mass on [−2T,2T]).
(Nef) Nef classes: Γ_g with g ≥ 0 pointwise and ĝ ≥ 0 on ℝ (positive-definite AND positive): these meet every Γ_n non-negatively. CONJECTURE: nef cone ⊂ closure of {D : ⟨D,D⟩ ≥ 0 after polar correction}.

## 4. Proof attempt, smallest nontrivial case T = ½log3 (2T = log 3)
At 2T = log3 the finite part sees only n = 2, 3 (log 3 at the boundary, weight vanishing for g smooth compactly supported inside). So the relevant span is {𝒜, Δ-smeared, Γ_2-meeting, (Γ_3 boundary)}: the prime term reduces to −(log2/√2)·2F(log2) (and the n=3 term only if F(log 3) ≠ 0, which is zero in the open window).
Step 1 (PROVED, standard): on 𝒜^⊥ the form is −[A_ℝ(F) − √2 log2 F(log2)]·(−1). So HI at ½log3 is: A_ℝ(g*g̃) ≥ √2·log2·(g*g̃)(log 2) + polar correction, for g ⊥ 𝒜.
Step 2 (the classical route): over F_q one proves HI by Riemann–Roch on C×C: if D² > 0 and D·𝒜 > 0 then h⁰(kD) ~ k²D²/2 → kD effective → D·𝒜 > 0 contradiction on 𝒜^⊥. We need h⁰ on 𝒮.
DEFINITION (pair count, quadratic growth): h⁰_X(Γ_F) := Σ_{m,n ≤ X} (mn)^{−1/2} F(log(n/m)) = ∫ F̂(t) |Σ_{n≤X} n^{−1/2−it}|² dt/2π.
PROVED: h⁰_X(Γ_{g*g̃}) ≥ 0 for all g (it is |Σ_{m,n} ...|²-type: a Gram form of Dirichlet polynomials; Bochner). PROVED: its leading growth in X is governed by the polar part (F̂(±i/2) times X), the ample term, and it is quadratic in the lattice size (X² points, half-density normalisation brings X¹; "quadratic growth" = counting points of ℕ×ℕ, as required by CA_F_003 (b)).
Step 3 (where it stops — exact point): RR on a surface converts h⁰ ≥ 0 (a positivity of a COUNT) into D² ≥ 0 (a positivity of the LOG-DERIVATIVE structure). On 𝒮 the window form is not the X-coefficient of h⁰_X; it is the coefficient obtained after taking −ζ'/ζ, i.e. after passing from |D_X|² to the logarithmic derivative of the Euler product. Positivity is not preserved by this logarithm. Everything up to here is PROVED; the conversion is missing.

NAMED NEW INPUT (OPEN): **Pair Riemann–Roch with logarithmic transfer (PRR-log).** A statement of the form
  h⁰_X(kD) − h⁰_X(K_𝒮 − kD) = ½ k² ⟨D,D⟩_int · L(X) + k·(linear) + O(1),
for a "canonical class" K_𝒮 (candidate: the Pólya class K of phase 135, the archimedean Lévy current) and a normalisation L(X) → ∞, valid on the smeared graph classes, where h⁰ is the pair count (or a refinement counting sections of the adelic line bundle on ℕ×ℕ restricted to the near-coincidence locus). Equivalently: a multiplicative-to-additive dictionary in which the Euler-product logarithm acts as the intersection product on 𝒮. With PRR-log, the F_q proof runs verbatim (Step 2) and HI at ½log3 follows. Without it, Steps 1–2 only give the Bochner-trivial positivity of the count.
Sub-input (also OPEN): effectivity — "h⁰_X(kD) grows quadratically in k ⇒ D is a limit of nef classes" (a Bogomolov/ampleness lemma on 𝒮).

## 5. What separates ζ from Epstein x²+5y² and from Beurling
- Epstein Z_Q, Q = x²+5y²: the pair object built on represented norms has graphs Γ_n for n ∈ Q(ℤ²), but the composition law fails: Γ_m∘Γ_n ≠ Γ_{mn} with multiplicity one (class number 2, the genus field splits the multiplicities; no Euler product). The "finite intersection" weights are then not Λ_Q(n)n^{−1/2} of a single Euler product, so the pair count Q_X is a Gram form for a non-multiplicative Dirichlet polynomial and PRR-log has no log to take (the logarithm of Z_Q is not a sum over a monoid of primes). Prediction (CONJECTURE): in 𝒮_Q the axiom Γ_mΓ_n = Γ_{mn} fails, so 𝒮_Q is not a surface with a monoid of correspondences, and HI_𝒮 is not even formulated — consistent with its full form being negative.
- Beurling systems: the multiplicative monoid and Γ_n's exist, Γ_mΓ_n=Γ_{mn} holds, but there is no integral lattice ℕ×ℕ with +1 steps: the s-direction (fibres) has no additive structure, the frustrated cycles (additive path m→…→2m closed by Γ_2) do not exist, h⁰_X is not a lattice count, A_ℝ is not tied to the counting measure. So 𝒮_Beurling lacks the fibre class pairing, and PRR-log has no quadratic-growth h⁰. The separating datum is the coexistence: monoid of correspondences (fails for Epstein) + additive lattice in the transverse coordinate (fails for Beurling).

## Compliance
 All reproduction claims are by unwinding definitions; HI_𝒮, CS, Nef, PRR-log are CONJECTURE/OPEN. No numerics; no negative value for ζ.
