# PROOF_L_SHARP_OO_001: boundary triples, Kreĭn's formula and KVB for the window form

Phase 199. Prover memo, pen and paper. No numerics. Target: L′♯ / λ_A(T) ≥ 0 (Paper 46 eq:target).

**Outcome in one line.** No sign.
- PROVED: there is an exact boundary triple whose Γ₀ is the pair of Tate functionals (A, B). It is the non-densely-defined
  kind (Hassi–de Snoo), with boundary space ℂ². Its Weyl function at 0 is −S^Sch_T, so the KVB/Kreĭn criterion is exactly
  Paper 46 thm:parityschur + prop:polarcap (𝔊_T = D_pol − M(0)).
- PROVED: at the window edge the Weil operator has order log, which is below the trace threshold s = ½. So there is no
  edge Green identity: the form-minimal and form-maximal realisations coincide.
- The full-line cut gives an infinite-rank Dirichlet-to-Neumann Weyl function. On Z-lifts it returns W_T = 𝒲_ext[Ψ]
  (A_001 Thm 1.1).
- NO-GO for the class "boundary triple / Kreĭn / KVB / Vakhitov–Kolokolov": in every version, the hypothesis
  "minimal operator ≥ 0" is λ_A ≥ 0 itself (REF-D).

## 0. Index check and new reason
- **Index entries.** 03_ P60-5, l.251/256 (UNTRIED). 06_ l.212 (OPEN, "must escape W-det, inertia-nogo"). 04_ l.452
  (G1D-R160_S2, deficiency (4,4), DEAD). 04_ l.782 (R162_2702b: boundary triple for the *prolate* W_λ, a second-order
  differential operator with deficiency (2,2); Λ-free, DEAD). README l.207 already records "boundary triples for W_λ
  (= polar capacity 𝔊_T, PROVED)". 04_ R186-D_B (Birman–Schwinger, W-det).
- **Relation to the DEAD entries (AUDIT_L_SHARP_17).** R162_2702b (04_ l.782) and G8D-160 C2 (04_ l.663) built boundary
  triples for the *prolate* W_λ, a second-order differential operator with deficiency (2,2) and prime-free U(2)
  extensions; README l.207 closes the family, and the 06_ 'never attempted' note was stale. Here the object differs: it
  is the Weil operator A_T itself (order log, comb included), with the Tate functionals as Γ₀ and the full-line cut. **The
  outcome does not differ in substance.** The triple is Λ-blind (§3d), its Weyl function is the polar capacity of
  README l.207, and its KVB hypothesis is the target. Hence **NO-GO (retry in substance)**, with the mechanism now explicit.
- **Losslessness input.** This memo uses Guo 4.4 / A_001 Thm 1.1 / the II_001 Gram identity (rigorous), not MM.2
  (CONDITIONAL).
- **Original motivation.** Earlier attempts realised the *prolate* differential operator. Here the object is the Weil operator
  itself. MM_001 MM.2 showed that the full-line loop is lossless, which makes W_T the edge energy of the truncation.
  The question asked is whether that edge energy can be carried by a finite boundary space (edge jet or Tate pair) with
  a Weyl function whose sign is decidable under a nonnegative minimal operator. §§1–3 answer it.

## 1. The Tate boundary triple (PROVED)
**Notation.** H = L²(I_T). A_T is the self-adjoint operator of the closed semibounded form 𝔞_T (eq:form). It has form
domain 𝒟_T and compact resolvent: the Lévy part grows like log|τ|, and the comb is bounded with norm ≤ Σv_n.
Write e₊ = e^{t/2}, e₋ = e^{−t/2}, N = span{e₊, e₋}, E: ℂ² → H, E(c) = c₊e₊ + c₋e₋. Then E*F = (A(F), B(F)) for real F,
and P_T = ker E* = N^⊥.

**Minimal operator.** S := A_T restricted to dom A_T ∩ N^⊥. Its domain is dense in N^⊥ but not in H. Its adjoint is the
linear relation S* = {(F, A_T F + Ec) : F ∈ dom A_T, c ∈ ℂ²}.

**Boundary triple.** 𝒢 = ℂ², with Γ₀(F, A_TF + Ec) := E*F (the Tate pair) and Γ₁(F, A_TF + Ec) := c.

**Green identity.** For F̂ = (F, A_TF + Ec) and Ĝ = (G, A_TG + Ed):
⟨A_TF + Ec, G⟩ − ⟨F, A_TG + Ed⟩ = ⟨c, E*G⟩ − ⟨E*F, d⟩ = ⟨Γ₁F̂, Γ₀Ĝ⟩ − ⟨Γ₀F̂, Γ₁Ĝ⟩,
using A_T = A_T*. The map (Γ₀, Γ₁) is onto ℂ⁴: choose F with E*F prescribed (N ⊂ 𝒟_T) and c freely. So this is a
boundary triple for S* in the sense of relations (CITED framework: Hassi–de Snoo–Szafraniec; Derkach–Malamud).

**Extensions.**
- ker Γ₁ = A_T.
- ker Γ₀ is the relation (compression of A_T to P_T) ⊕ ({0} × N). Its bottom is λ_A.
- For Θ = Θ*, the extension A_T + EΘE* is a self-adjoint extension of S. Indeed E*F = 0 on dom S, so it agrees with A_T there.
- The complete form W_T = 𝔞_T + 2Re(AB̄) is this extension with Θ = D_pol, the polar matrix [[0,1],[1,0]] in (A, B)
  coordinates.

So the Tate functionals *are* Γ₀ (as conjectured). The selected extension "Γ₀ = 0" is the primitive problem.

**Weyl function.** Take z ∉ σ(A_T). The defect elements are F_z = (A_T − z)^{-1}Ec. Use the swapped triple
(Γ₀′ = c, Γ₁′ = −E*F), so that A₀′ = A_T. Then its Weyl function is
  Q_T(z) = E*(A_T − z)^{-1}E   (2×2, Kreĭn Q-function)
and, for the triple above, M(z) = −Q_T(z)^{-1}.

**Kreĭn's formula.** On N^⊥ the compression satisfies
(A_T|_{P_T} − z)^{-1} = P[R_z − R_zE Q_T(z)^{-1} E*R_z]P, with R_z = (A_T − z)^{-1}.

**Identification at z = 0 (PROVED).** Assume 0 ∉ σ(A_T), work in parity sectors, and write χ for the sector Tate vector.
Put h = A_T^{-1}χ / Q(0).
- Then 𝔞_T(h, G) = ⟨χ, G⟩/Q(0) = 0 for every G ∈ P_T, and ℓ(h) = 1, so h is the h_par of thm:parityschur(a).
- Also 𝔞_T(h) = 1/Q(0).
- Hence S^Sch_T = Q_T(0)^{-1} = −M(0), and 𝔊_T = S^Sch_T + D_pol = D_pol − M(0).

## 2. KVB / index reading (CITED + PROVED reduction)
**Finite-rank KVB.** If the Γ₀-extension is nonnegative and invertible (λ_A > 0), then A_T + EΘE* ≥ 0 if and only if
Θ − M(0) ⪰ 0 (Kreĭn–Birman–Vishik for finite deficiency; Derkach–Malamud, CITED). With Θ = D_pol this is precisely
thm:parityschur(c) "λ_W > 0 ⟺ λ_A > 0 and 𝔊_T ≻ 0". **Not new.** It is the boundary-triple name for Paper 46's polar
capacity, consistent with README l.207.

**Reverse direction (Vakhitov–Kolokolov / Maddocks constrained index, CITED: Maddocks 1985; Pelinovsky 2011).**
If 0 ∉ σ(A_T) and Q_T(0) is nondegenerate, then
  n₋(𝔞_T | P_T) = n₋(A_T) − n₋(Q_T(0)).
So λ_A > 0 ⟺ n₋(A_T) = n₋(Q_T(0)) (≤ 2). This reduces the target to a 2×2 sign condition **plus** the exact count
n₋(A_T) of the unconstrained window operator, and n₋(A_T) ≤ 2 is itself a codimension-two positivity statement for
𝔞_T. Both sides are global spectral data of A_T, which contains the comb. The arithmetic enters Q_T(0) only through
A_T^{-1}: a resolvent of the full operator Lévy + C₀ − comb, evaluated on e^{±t/2}. No new input, and the reduction is
not an improvement: REF-D.

**The crux asked.** "Is the minimal operator nonnegative?" The minimal operator S ≥ 0 means 𝔞_T ≥ 0 on dom A_T ∩ P_T,
which is λ_A ≥ 0: **the target itself.** Using A_T as the minimal object instead does not help: A_T is not ≥ 0
(m(0) = b_∞ < 0, prop:archneg, and the comb), so the KVB band between the Kreĭn–von Neumann and Friedrichs extensions
does not exist.

## 3. The edge: no finite boundary space (PROVED / ARGUED)
**(a) PROVED (form level).** C_c^∞(I_T) is dense in 𝒟_T.
- C_c^∞(I) is dense in H^s(I) for s < ½ (Lions–Magenes / Triebel: H^s_0 = H^s, CITED).
- H^s(I) is dense in 𝒟_T, because (1+|τ|)^{2s} dominates log(2+|τ|).

Hence the closures of 𝔞_T from C_c^∞(I) and from 𝒟_T coincide. There is no edge boundary condition at the form level,
and the jet at ±T carries no boundary form. FF.2's jet relation [1 + (−1)^k c_μ μ^{−1/2}]g^{(k)}(T) is a regularity
match of the lift, not a Green term.

**(b) ARGUED (operator level).** Functions with jumps at ±T (e.g. 1_I, e^{±t/2}) lie in dom A_T, since
log|τ|·τ^{−1} ∈ L². So the order-log operator has no edge deficiency. This contrasts with R186_052, where the operators
D_per, D_anti are first order with deficiency (1,1); that is why their s(·) splitting is an extension statement while
𝔞_T is not.

**(c) PROVED (formal at II_001's level).** The full-line cut: 𝒲 on L²(I) ⊕ L²(ext).
- Radical lifts Φ = g ⊕ Ψ have 𝒲_{ext,I}g + 𝒲_ext Ψ = 0 on the exterior (Guo 4.4).
- Hence, wherever 𝒲_ext is invertible, the cut Weyl (DtN) function is Λ = 𝒲_{I,ext}𝒲_ext^{-1}𝒲_{ext,I}.
- The Schur complement 𝒲_I − Λ vanishes on lifts (Guo 4.4; II_001 Gram identity).
- So W_T(g) = ⟨g, Λg⟩ = 𝒲_ext[Ψ], which is A_001 Thm 1.1.

The boundary space is all of L²(ext) because the coupling is nonlocal (Lévy ν and translations log n < 2T). II_001's
rank-one Gram on span{g, Ψ̌} is this identity, not a finite boundary space. Λ ≥ 0 on lifts is (L_ext) of A_001
Thm 3.1, so this direction is REF-D. 𝒲_ext is indefinite (MM.3b), so KVB has no nonnegative minimal operator here either.

**(d) Where the arithmetic sits.**
- Tate triple: inside Q_T(0) = E*A_T^{-1}E (the comb Σv_n τ_{log n} inside the resolvent).
- Cut triple: inside Λ (comb plus Möbius tail c_N via FF.1, and the pole).
- The structure of §1 holds verbatim for any comb: a_P, cΛ, Beurling. It is Λ-blind (falsifier test passed by every
  class), so it carries no sign.

## 4. Verdict
- **PROVED:** the Tate boundary triple of §1 (Green identity, Kreĭn formula, M(0) = −S^Sch_T, 𝔊_T = D_pol − M(0)); the
  form-level absence of edge boundary conditions (§3a); the cut DtN identity (§3c, formal at II_001's level).
- **CITED:** KVB/Derkach–Malamud; the Maddocks/Vakhitov–Kolokolov index.
- **ARGUED:** §3b.
- **NO-GO (retry in substance of R162_2702b / G8D-160 C2)** (class 𝒦𝒱ℬ: boundary-triple / Kreĭn-formula / KVB / constrained-index proofs of λ_A ≥ 0 over the Tate or
  edge boundary): the minimal-operator positivity hypothesis is λ_A ≥ 0 (Tate triple) or 𝒲_ext ≥ 0 on lifts (cut
  triple), i.e. REF-D. The 2×2 condition is already Paper 46's polar capacity. The index version needs n₋(A_T), which is
  no easier.
- The residue "produce the boundary energy directly" (MM_001) is **not** served by finite boundary data: the window edge
  of an order-log operator has no trace.

**Do not retry:** boundary triples for W_T/W_λ with Tate or edge-jet boundary maps, Kreĭn Q-function at 0, KVB band,
constrained index. L′♯ OPEN. **Row D OPEN.**
