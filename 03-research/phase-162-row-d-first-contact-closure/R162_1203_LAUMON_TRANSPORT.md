# R162_1203 — Laumon ε-factor transport, one dictionary round (route 6 of R162_590 §2)

Status: **NO-GO** (dictionary PROVED; missing step identified; first-contact construction PROVED sign-neutral;
the missing step is the rationality/cohomology wall, proved in the form of Theorem W below; stop).
Corpus prescription honoured: ROW-D-CLOSURE-PLAN §8.2 ("ronda 0 de diccionario ... reubica el muro, no lo
quita"); R157_002 row 23 (desk-excluded, "inherits the rationality wall"); R160_C8_R1 (ε-factors of GL(1) are gauge,
content = Beckner constant C₀ = ψ(¼) − log π; its Thm 1 is `eq:form` and is not reused as a mechanism here).

Setting (README Gate 1): T_* first window with λ_A(T_*)=0, F primitive parity kernel vector (H_{T_*}F=0);
target R_LF=0 ⟺ K_F(a_m)=0 on the Gamma lattice a_m=2m+½. Known: T_* > ½log5 (R162_303), G_+^0(−a_m) =
−εζ′(−2m)K_F(a_m) (R162_402), ‖R_LF‖² = ε∫c_Fκ_L (R162_302).

---

## 1. Laumon's proof skeleton (Weil II via Fourier, Publ. IHÉS 65, 1987), reduced to six steps

L1 Local ε-factors ε(V,F,ψ) and local Fourier transforms F^{(0,∞′)}, F^{(∞,∞′)} (stationary phase at ∞).
L2 Product formula ε(X,F) = q^{C(1−g)rk F}∏_v ε_v(F|_v, ψ_v) (proved via L1 and Fourier).
L3 Fourier–Deligne transform FT_ψ on A¹: exact, involutive up to twist, commutes with duality, sends pure weight w to
   pure weight w+1; generic stalk of FT(F) at t is H¹_c(A¹, F ⊗ L_ψ(tx)) (a one-parameter family of L-functions).
L4 Upper bound (Rankin–Landau on tensor powers): weights of H¹_c ≤ w+1 on the generic stalk.
L5 Determinant/saturation: det(−Frob | H¹_c) = global ε (Grothendieck–Lefschetz + L2), dimension N = −χ_c
   (Grothendieck–Ogg–Shafarevich); |α_i| ≤ q^{(w+1)/2} for all i and |∏α_i| = q^{N(w+1)/2} ⟹ all equal.
L6 Specialisation: weights at the special stalk ≤ generic weights (semicontinuity; constructibility of FT(F)).

## 2. Dictionary to the first-contact setting over ℚ

| Step | ℚ / first-contact analogue | Status over ℚ |
|---|---|---|
| L1 | Tate local zeta integrals; ε_p = 1 (unramified), ε_∞ = Γ-factor ratio; stationary phase at ∞ = Stirling; Gamma lattice a_m = the reflected poles of Γ(s/2) (R162_402 dictionary) | THEOREM (Tate; R162_402) |
| L2 | Tate's global functional equation ξ(s)=ξ(1−s); window form = log-uncertainty of semilocal 𝔉_S (C8 Thm 1); invariant content one constant C₀ (C8 Thm 2) | THEOREM, content a scalar |
| L3 | FT = functional equation; the "Fourier family" = additive twists Σ Λ(n)e(tn) n^{−s}, i.e. Lerch/Hurwitz; decomposed multiplicatively by Gauss sums \|τ(χ)\| = √q into {L(s,χ)} | involution: THEOREM; purity of generic stalk: **FALSE** (§3.1) |
| L4 | Only Re ρ < 1 (Hadamard–dlVP); per window λ_A > 0 on (0,½log5] (R162_303, certified) | PARTIAL, not sharp |
| L5 | regularised det: Hadamard product of ξ; cardinality N(T) ~ (T/2π)log(T/2πe), infinite | **MISSING** (§3.2, Thm W) |
| L6 | "ζ-window ≥ family-window" | **MISSING**; premise false (§3.1) |

So L1, L2, and the involution part of L3 have ℚ-analogues that are theorems. The steps that carry the sign
(L4 sharp, L5, L6) are missing. In Laumon, L5 is elementary *given* the sharp L4 on a finite-dimensional space.
The sharp L4 comes from L3+L6 through a family with finite cohomology.

## 3. The missing piece

### 3.1 The generic stalk is impure over ℚ (THEOREM, CITED)
The ℚ-fibre of the additive family at rational t = a/q is a linear combination of Hurwitz zetas ζ(s, b/q).
Davenport–Heilbronn (1936) showed that ζ(s,α) has infinitely many zeros in Re s > 1 for rational α ∉ {½, 1} and for
transcendental α. Cassels (1961) extended this to algebraic irrational α. So the premise of L6 (a pure generic stalk)
is false over ℚ. The only fibres that *are* expected to be pure are the multiplicative ones (Dirichlet L). The
transport lands on the family {L(s,χ)}, which contains ζ itself as the χ₀-component
(L(s,χ₀) = ζ(s)(1−q^{−s})).

### 3.2 First-contact construction attempt (one window T_*, one kernel vector)
The piece to build is a per-window substitute for L5+L6: an inequality W_{T_*}[Λ] ⪰ (family average) whose
equality case at F forces K_F(a_m) = 0.

**Proposition 1 (per-window transport is linear and sign-neutral; PROVED).** Fix q prime and a coefficient
sequence c. Let W_T[c] be the window Hermitian form built from c exactly as W_T[Λ] is built from Λ (Paper 47
def:W, with c in place of Λ). The map c ↦ W_T[c] is real-linear. For (n,q) = 1,
e(an/q) = φ(q)^{−1} Σ_χ τ(χ̄) χ(an). Hence W_T[Λ e(a·/q)] = Σ_χ φ(q)^{−1}τ(χ̄)χ(a) W_T[Λχ] + W_T[Λ·1_{q|n}e(a·/q)].
The matrix (τ(χ̄)χ(a))_{a,χ} is invertible, since |τ| = √q and the characters are orthogonal. So the additive-twist
family and the character family determine each other linearly, per window.
*Consequence.* At a first-contact vector F, ⟨F, W_{T_*}[Λ]F⟩ = 0 turns into one linear relation among the numbers
⟨F, W_{T_*}[Λχ]F⟩. A sign conclusion requires ⟨F, W_{T_*}[Λχ]F⟩ ≥ 0 for every χ ≠ χ₀, i.e. window-GRH mod q at
T_*. That statement contains the ζ statement (χ₀-component, up to the finite factor 1 − q^{−s}) and is strictly
stronger. The transport is circular. It is linear, so it fails F2 (invariant under A ↦ −A in the square) and F4 (a
linear limit). It holds for any c, so it fails F3. ∎

**Proposition 2 (no window saturation; PROVED).** Laumon's L5 is the equality case of an operator bound
(|α| ≤ bound). The window analogue is the equality ‖P_T𝔉_∞P_TF‖ = ‖F‖ for the archimedean Tate–Fourier involution
𝔉_∞ (additive Fourier on even functions of ℝ), with F supported in the annulus e^{−T} ≤ |x| ≤ e^{T}. Since 𝔉_∞ is
unitary, equality forces 𝔉_∞F to be supported in the same annulus. Then F and its Fourier transform are both
compactly supported, so F = 0 by Paley–Wiener. The semilocal 𝔉_S = 𝔉_∞ ⊗ (⊗_{p∈S}𝔉_p) behaves the same way: each 𝔉_p is
unitary and fixes 1_{ℤ_p}, and the archimedean factor forces vanishing. So the ε-determinant bound is never saturated
by a nonzero window vector. The condition λ_A(T_*) = 0 is the saturation of the *Weil* form, and there the
ε-data enter only through the scalar C₀‖F‖² (C8 Thm 2). A scalar shift carries no information on
K_F(a_m). ∎

**Theorem W (the missing step is the rationality wall; PROVED).** Laumon's L5 inference ("each term ≤ c and
their sum = Nc ⟹ each term = c") needs two things: a spectral multiset of *finite, known* cardinality N, and a
per-element sharp bound. Over ℚ, per window, neither is available. Proof:
(i) Cardinality. The only ℚ-substitute for N = −χ_c is the regularised zero count. By thm:finZ / cor:infinite
(Paper 47 §7), no finite zero multiset carries a flat-top certificate at any window. So a finite-N saturation
identity equivalent to the window certificate does not exist.
(ii) Sharp bound. With the functional-equation symmetry ρ ↔ 1−ρ̄, the per-element bound "β ≤ ½" alone is already RH.
L5 therefore adds nothing beyond L4-sharp. In Laumon, L4-sharp comes from L3 + L6 on a family with finite
cohomology (constructibility of FT(F)). Over ℚ the family's generic fibre is impure (§3.1), and the pure
multiplicative family returns the question in stronger form (Prop 1).
(iii) The ε-data cannot replace (i)–(ii). By L2 over ℚ their invariant content is the single scalar C₀ (C8 Thm 2), and
Prop 2 shows this scalar never meets K_F(a_m).
What the Laumon architecture needs, a finite cohomology with det = ε and constructible specialisation, is exactly the
rationality/cohomology wall (ROW-D-CLOSURE-PLAN 3.4, P46 §28.4 clause "no ring of correspondences on Spec ℤ").
Stop, as prescribed. ∎

Net value of the dictionary (this is the relocation §8.2 predicted): the Gamma lattice a_m is the ℚ-image of the
local monodromy at ∞ (L1). The Gauss-sum isometry is the only ℚ-transport between the additive and multiplicative
squares, and at a first-contact vector it moves the sign to window-GRH mod q.

## 4. Falsifier and gate lines

- **DH.** Davenport–Heilbronn shares the complete ε-datum of its FE class (Γ-factor, conductor 5, root number). Steps
  L1–L3 over ℚ see only this datum, so every conclusion of §2 holds verbatim for DH, which has first contacts
  (R162_407). This is a pass as a falsifier, and a kill as a mechanism. At conductor 1, Hamburger's theorem makes the
  FE class {cζ}. That identifies the object and gives no sign (a restatement).
- **Deletion/κ.** Finite modifications a ≠ Λ: ε_p = 1 at unramified p regardless of the local factor, so the ε-data
  are blind to any finite deletion. This is consistent with R162_204 (the critical jet is invariant under finite
  modification). κ_L in ‖R_LF‖² = ε∫c_Fκ_L never meets an ε-factor beyond the global sign ε.
- **Beurling.** A Beurling system has no additive structure, so there is no additive Fourier, no Gauss sums and no
  L3. The route cannot be run there. Beurling does not distinguish anything, because §2 never uses Λ*1 = log.
- **F1.** Prop 1 does not use λ = 0 or minimality non-perturbatively. It would "prove" Q ≥ 0 on positive
  eigenvectors too, so any closing version fails F1.
- **F2.** Linear in the coefficients, so it cannot orient the (PC) square. Fails.
- **F3.** Valid for every coefficient sequence c (Prop 1) and for DH (above). Fails.
- **F4.** The transport is a finite linear change of basis. Fails.

## 5. D1 (Torelli-failing lamination) status
D1 remains **never built**. R160_C1_R1 §(OS-1) derived the requirement: a Hodge-preserving leafwise flow that is
infinitesimally Torelli-trivial but Teichmüller-nontrivial along the leaves. That means ℋ^{1,0}·ℋ^{1,0} is not dense in
the integrable holomorphic quadratic differentials, together with one pole, (Sc_1) and σ_p(V|ℋ^{1,0}) infinite. The
implication "density ⟹ ∂̄-exact ⟹ isotopy conjugacy" rests on a lamination Teichmüller lemma that is itself
unproved (HEURISTIC in C1). On the three explicit carriers (CM solenoid, horospherical frame flow, dense linear torus
foliations), ℋ^{1,0} = dz·L²(Sat) heuristically, and every flow written down there was holomorphic up to isotopy.
The route is still the only carrier class not excluded by Thm Z / Thm H. It is highest-cost and lowest-falsifiability
(R162_590 §2 item 4). This round did not touch it. The Laumon result suggests no link: Torelli failure is a
cohomological-finiteness question, and it would need the same finite H¹ that Theorem W shows is absent per window.

## 6. Verdict
Laumon transport over ℚ: L1, L2 and the L3 involution are theorems (Tate, Stirling, R162_402). L4-sharp, L5 and L6 are
missing. The first-contact attempt produces a PROVED linear Gauss-sum isometry (Prop 1) that makes the question
circular (window-GRH mod q), and a PROVED no-saturation lemma (Prop 2). Theorem W identifies the missing step with the
rationality/cohomology wall. **NO-GO; route 6 of R162_590 closed.** Do not rerun without a finite-cohomology object
per window.
