# CS0_COMMUTE_001 — Phase 200, round 24a: Lemma CS-0 (differential commutant of the window form)

**Summary (≤150 words).** The kernel of 𝒲_T, the complete form W_T = 𝔞_T + 2Re(A·B̄) from P46 (eq:form, eq:W), is of difference type: k(u) = c₀δ(u) − ½K(|u|) + cosh(u/2) − Σ_{n∈N_T}(v_n/2)[δ(u−log n)+δ(u+log n)]. **(a) PROVED:** if D = ∂p∂ + q (with p, q of class C³) commutes with 𝒲_T in the interior of the square, then p and q are (log n)-periodic on the overlaps, for every n ∈ N_T. Moreover q′ = p‴/6 + 4a·p′. **(b) PROVED:** in the Slepian–Morrison class (p a polynomial of degree ≤ 2) this forces p and q to be constant. **(c) PROVED:** no −γ∂² + c with self-adjoint boundary conditions commutes with 𝒲_T. Therefore the "window Courant–Sturm" route is **NO-GO PROVED** in the prolate class, already from **T > ½log 2**: the ½log 3 threshold of the sketch is unnecessary. For general smooth p the result remains **ARGUED/OPEN**. Kronecker is not useful on a bounded interval. Correction to SPEC_011: Slepian does not commute with A_∞.

## 0. Index and corpus check
- grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/` with "commut", "Slepian", "prolat", "Sturm", "Tracy": R9-03 appears (CCM prolate/sl₂ as Lefschetz triple, negative), Mori B1 (prolate test vector) and Guo B3 (prolate leak). **No entry deals with a differential commutant of W_T** or with commutation with the comb. "Courant" gives 0 results (SPEC_011:36). This is not a retry.
- Definitions checked against P46: eq:symbol (lines 110–114, v_n = 2Λ(n)/√n, N_T = {n ≥ 2 : log n < 2T}), eq:form, eq:W (121–123) and lem:K (364–366: K(u) = u⁻¹ + O(1)).

## 1. The exact kernel of 𝒲_T
For F ∈ L²(I_T) one has |F̂|² = (c_F)^ and m(τ) = C₀ + ∫₀^∞(1−cos τu)K(u)du. Therefore 𝔞_T(F) = ∫∫ F(s)F̄(t) k₀(s−t) ds dt with
k₀(u) = c₀δ(u) − ½·Pf K(|u|) − Σ_{n∈N_T}(v_n/2)[δ(u−log n) + δ(u+log n)].
Here Pf is the Hadamard finite part that regularizes the 1/|u| at the origin, and c₀ absorbs C₀ and the regularization. The polar term 2Re(A B̄) = ∫∫F(s)F̄(t)·2cosh((s−t)/2) is, likewise, of difference type. Thus 𝒲_T = 𝒦_T, the compression to I_T of convolution with
**k(u) = c₀δ(u) + g(u) − Σ_{n∈N_T}(v_n/2)[δ_{log n} + δ_{−log n}](u)**, with g(u) = −½K(|u|) + 2cosh(u/2).
g is even and real-analytic for u ≠ 0, with g(u) = −1/(2|u|) + G(|u|), where G is analytic at 0 (because 1/(2sinh(u/2)) − 1/u is odd and analytic). Set a := G′(0).

On the lines: the line s − t = log n meets the open square (−T,T)² if and only if log n < 2T, i.e. if and only if n ∈ N_T. **The first line (n = 2) enters at T > ½log 2.**

## 2. Statement
**Lemma CS-0.** Let T > ½log 2 and D = ∂p∂ + q, with p, q real of class C³ on (−T,T). We say D commutes with 𝒲_T if ⟨DG, 𝒲_T F⟩ = ⟨G, 𝒲_T DF⟩ for all F, G ∈ C_c^∞(I_T). This is a necessary condition for any operator version (with any boundary condition), because compact supports avoid the boundary terms. Then:
(a) for every n ∈ N_T, with ℓ = log n: p(t+ℓ) = p(t) and q(t+ℓ) = q(t) for t ∈ (−T, T−ℓ);
(b) q′ = p‴/6 + 4a·p′ on (−T,T);
(c) if p is a polynomial of degree ≤ 2 (the prolate normal form: Slepian uses p = 1 − x², and Morrison/Grünbaum give this form for commutants of difference kernels), then p and q are constant;
(d) no self-adjoint realization on L²(I_T) of −γ∂² + c (γ ≠ 0), with separated or periodic boundary conditions, commutes with 𝒲_T.
**Conclusion: in the prolate class there is no differential operator of order ≤ 2 that commutes with 𝒲_T, except for multiples of the identity. NO-GO PROVED for T > ½log 2.**

## 3. Proof
**Kernel identity.** For F, G ∈ C_c^∞ one has ⟨G,[D,𝒦]F⟩ = ⟨(D_s − D_t)k(s−t), G⊗F̄⟩ in 𝒟′((−T,T)²), because D is formally symmetric. For h(s−t), with s = t + u:
(D_s − D_t)h = (p(s)−p(t))h″(u) + (p′(s)+p′(t))h′(u) + (q(s)−q(t))h(u).   (★)
Commutation is equivalent to (★), summed over the pieces of k, being 0 in 𝒟′ of the square.

**(a) Lines.** Fix n ∈ N_T and ℓ = log n. In a tubular neighborhood of the line L_ℓ = {s − t = ℓ} that touches neither the diagonal nor the other lines (they are parallel and distinct), the remaining pieces of k are C^∞ functions, and (★) applied to them gives a continuous function. The piece on L_ℓ is −(v_n/2)δ(u−ℓ), with v_n > 0. Set u′ = u − ℓ and use coordinates (t, u′), in which the decomposition f(t)δ″ + g(t)δ′ + h(t)δ is unique. With f(t,u′)δ″(u′) = f(t,0)δ″ − 2∂_{u′}f(t,0)δ′ + ∂²_{u′}f(t,0)δ, the coefficients of (★) on L_ℓ are:
- δ″: p(t+ℓ) − p(t);
- δ′: −2p′(t+ℓ) + p′(t+ℓ) + p′(t) = p′(t) − p′(t+ℓ);
- δ: p″(t+ℓ) − p″(t+ℓ) + q(t+ℓ) − q(t) = q(t+ℓ) − q(t).
A distribution of order ≥ 0 supported on L_ℓ cannot cancel against a continuous function. Therefore all three coefficients vanish for t ∈ (−T, T−ℓ). ∎(a)

**(b) Diagonal.** For u ≠ 0, equation (★) with h = g holds pointwise away from the lines, and by continuity holds for all u ≠ 0. Expand as u → 0⁺ with g = −1/(2u) + G(u). This computation was checked symbolically (sympy) in the session:
- u⁻²: −p′/2 + p′/2 = 0;
- u⁻¹: −p″/2 + p″/2 = 0;
- u⁰: p‴/12 − q′/2 + 2a·p′.
For u → 0⁻ the same coefficient comes out with opposite sign. The singular δ(u) pieces of the diagonal commute: this is the case ℓ = 0 of (a), where all three coefficients are identically 0. Thus q′ = p‴/6 + 4a p′. ∎(b)
*Remark.* The Lévy singularity alone does not force p′ = 0. The singular orders cancel for every p. This is why the "Slepian on the diagonal" argument of the sketch does not work as is.

**(c)** Let p = αt² + βt + γ and n = 2 ∈ N_T (T > ½log 2). By (a), on the nonempty interval (−T, T − log 2) we have 0 = p(t+ℓ) − p(t) = 2αℓt + αℓ² + βℓ. Hence α = 0 and β = 0, so p ≡ γ. By (b), q′ = 0 and q ≡ c. ∎(c)
**Only one** period is needed. The ½log 3 threshold of the sketch (two ℚ-independent periods + Kronecker) is unnecessary in the polynomial class. Outside that class it does not work either: on a bounded interval, the relations p(t + log 2) = p(t) and p(t + log 3) = p(t) only link overlaps of length 2T − log n. For T slightly larger than ½log 3 there are non-constant p of class C^∞ satisfying them: one is chosen freely on the central stretch and copied onto the overlaps. Kronecker needs the whole line.

**(d)** With p ≡ γ ≠ 0, (★) vanishes identically in the interior: ∂² commutes with every convolution on ℝ. The obstruction is at the boundary. A self-adjoint realization L of −γ∂² + c with separated conditions has simple spectrum, and its eigenbasis {φ_j} is trigonometric. If 𝒦 commutes with L, then 𝒦 = Σ w_j φ_j⊗φ_j.
- *Dirichlet.* φ_jφ_j is written in terms of cos(jπ(s−t)/2T) and cos(jπ(s+t+2T)/2T). The kernel is then A(s−t) − A(s+t+2T), with A of period 4T. Since k depends only on s − t, A(v) is constant for v ∈ (0, 4T), i.e. A is constant over a period. Then k is constant on (−2T, 2T), which contradicts the presence of δ_{log 2} and of 1/|u|.
- *Neumann and Robin.* The argument is identical, with + instead of − (and, in Robin, with an analytic correction in s + t, which must also vanish).
- *Periodic (period 2T).* The kernel is A(s−t) with A of period 2T, so k(u) = k(u + 2T) for u ∈ (−2T, 0). As u → 0⁻, the left side diverges like 1/(2|u|), while k near 2T⁻ is bounded (if 2T ∉ {log n}; if 2T = log n, a δ is used instead of 1/|u|). Contradiction.
General coupled conditions (θ-periodic, non-simple) reduce to the twisted periodic case with the same translation argument. I cover these only as ARGUED. ∎(d)

**Labels.** (a), (b), (c) and (d) for separated and periodic conditions: **PROVED**. General coupled conditions: ARGUED.

## 4. What remains open
- **Non-polynomial smooth p: OPEN, with negative ARGUED.** The orders u¹, u², … of (★) on the diagonal give a tower of ODEs in p, in the style of the bispectrality of Morrison (1962) and Grünbaum (1983). The expectation is that the tower forces p to be polynomial of degree ≤ 2, and then (c) closes the case. The tower was not written out. Label: ARGUED.
- **Order > 2.** The lines argument (a) generalizes to (log n)-periodic coefficients on the overlaps, but reduction (c) does not. Label: ARGUED.
- **Correction to SPEC_011 §B.** The "Slepian miracle" refers to the concentration operator Q_c, whose kernel is sinc. It does not refer to A_∞, whose kernel is the finite part of 1/|u|. Theorem P uses the prolate functions as **comparison**, not as commutant. It is not proved that a differential commutant exists for A_∞ alone. With p = T² − t² (prolate), the u⁰-order coefficient only fixes q′ = p‴/6 + 4a p′ = −8a·t, and the higher orders remain to be checked: OPEN.

## 5. Consequence and falsifiers
- The "window Courant–Sturm" class (A5 of SPEC_011), in its prolate differential-commutant version, is **NO-GO PROVED** for every T > ½log 2. The replacement C5 (Gantmacher–Kreĭn) was already dead (A6).
- The argument uses only that the kernel of 𝒲_T is of difference type and contains at least one atom δ_{±ℓ} with 0 < ℓ < 2T. Hence it holds equally for cΛ, a_P (with P^c ≠ ∅), Beurling and Epstein. It is a **class** NO-GO, comb-generic. It says nothing about the sign, and that is as it should be: it cannot separate the positive objects from the non-positive ones.

## 6. Index entry (ROUTES-TRIED-INDEX, phase 200)
| CS-0 | Window Courant–Sturm via differential operator ∂p∂+q that commutes with W_T | OPALG | phase-200/CS0_COMMUTE_001 | **NO-GO PROVED** (prolate class: p polynomial of degree ≤ 2, T > ½log 2). Reason: the atom δ_{log 2} forces p to be (log 2)-periodic, hence p const, hence the boundary does not commute. General smooth p and order > 2: ARGUED. Comb-generic, no sign. |
