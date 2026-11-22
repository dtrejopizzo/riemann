# CLASS_001 — Lead 1 (phase 207): class impossibility theorem for the node's sign step

lead 1.
Tool, not closure. No new numerics.

## Summary (≤250 words)

The node's sign step (phase 206) is, for each fixed T, a finite-dimensional statement.

- **Lemma 1 (PROVED).** The node for a datum a is a linear matrix inequality (LMI) in the numbers v^a_n, n < e^{2T}. Its validity set G_T is a closed convex spectrahedron.
- **Corollary: (K2) and (K3) are empty as restrictions.** Every sign step for the node uses the FE "only as symmetry", because the FE is already frozen into 𝔪, 𝔢 and c. Also every step depends on a only through v^a.
- **Corollary: quartets do not falsify the node.** They have the same comb, hence the same node.
- **The only class hypothesis with content is (K1)**, in quantitative form: margin η and Lipschitz constant L uniform in T in the multiplier norm.

**Theorem A (PROVED; the P46 inputs are CITED).** At the node over the full sector, no Ψ ∈ 𝒦_marg proves the node for all T. Reason: the ball of radius η/L around Λ should fit in G_T, and the inscribed radius of G_T in Λ is ≤ μ(T) ≤ 4·10⁹Te^{−15.449T}. The version with N ≈ 4T is CONDITIONAL on μ_N(T) → 0 (NUMERICAL).

**Theorem B (PROVED).** If the premise of Ψ is inherited by every Euler datum over ℕ with a pole and shape FE, Ψ does not prove the node for any T > π/2. The falsifier is a_P with P > e^{2T}, which leaves the window empty; the node is false by lem:archcount, without PRED-aP.

**What falls outside 𝒦:** steps with Lipschitz/margin ratio ≥ e^{15.449T}/(4·10⁹T). These are exactly the identities with an exponentially small positive remainder (certificates, REF-D).

**Objection:** 𝒦 is not empty and does not contain the node trivially. But its complement borders on circularity, and lead 2 has to live there.

---

## 0. Corpus check

I also read the following files:
- P46: thm:noimport, rem:conjunctions, lem:transfer, thm:sos, prop:shape-eulerdel, lem:shape-quartet, prop:shape-inputs, lem:degen, lem:archcount and the margin bound (l. 3576).
- META_200_BARRIER_001 §A1–A5 (Φ200, Φ.14).
- COMPOSE_EF_001 §3 (Theorem C2).
- TOOLS_204U_001 (B_P).
- The routes index README (BARRIER_D1/D2, AUDIT_197_2, residue R1).

I grepped ROUTES-TRIED-INDEX for "class impossibility", "meta-theorem", "continu.* in Λ" and "spectrahedron". Results:
- "meta-theorem" appears in N_018 (operator partitions) and in thm:N/N′ (lattice certificates). Neither is formulated over the phase 206 node.
- **Lipschitz:** BARRIER_D2 Thm 1 already proved |λ_A(a) − λ_A(b)| ≤ Σ|a−b|/√n, and Thm 2, that continuation transfers only the margin.
- **Hamburger:** BARRIER_D1 Thm 4 + AUDIT_9 already say "continuity suffices ⇒ REF-D⁺" for analytic defects of the FE.
- **Transversality:** Φ.14 is the affine version in the direction of a minimizer.
- **Composition:** C2 is the "E + shape FE" case for W and q.

**New reason (written, mandatory).** The previous barriers are stated over λ_A, W or q, each for a concrete family of premises. This memo changes the object and the quantification:

(i) **Object.** It is the phase 206 node over c^⊥ ∩ E_N^ev, which is a finite LMI. On it one can prove that (K2) and (K3) are empty and that quartets do not falsify it. Both are new and correct the setup and the README of 206.

(ii) **Class.** It quantifies over *every* functional Ψ with uniform margin and Lipschitz constant, not over a family of defects. BARRIER_D2 Thm 1 only gives the Lipschitz bound of λ_A.

(iii) **Falsifier.** For the node there is one PROVED without PRED-aP: the empty window of a_P with P > e^{2T} plus lem:archcount. C2 used WP_T and the 0.60 bound.

What is *not* new is marked as "restatement of" in each case.

---

## 1. Definitions

### 1.1 Data and node
- A **datum** is a real sequence a = (a_n)_{n≥1}, with weights v^a_n := 2a_n n^{−½}; Λ is the ζ datum.
- Fix T > 0 and X = e^{2T}. Only the v^a_n with n < X matter (by support, c_F(log n) = 0 if n ≥ X; NODE_001 §1.1).
- **Comb.** comb^a(F) := −Σ_{n<X} v^a_n c_F(log n).
- **Window form of the datum.** 𝔄^a = 𝔪 + comb^a, with 𝔪 the archimedean term of conductor 1 (eq:Aform, with v^a in place of v).
- **Main term.** M = 𝔢 − 2ccᵀ (NODE_001 §1.2). Fluctuation: Φ^a := comb^a − M (Stieltjes; NODE_001 §1.3).
- **Spaces.** V_N := c^⊥ ∩ E_N^ev, with N ≈ 4T (the version from 206), and V_∞ := c^⊥ ∩ L²(I_T)^ev (full even sector, P_T^ev).

**Node for a** (in V ∈ {V_N, V_∞}):
  𝒩_T^V(a):  (𝔪 + 𝔢)(F) + Φ^a(F) ≥ 0  ∀F ∈ V.
Since ⟨F,c⟩ = 0 holds in V, we have (𝔪+𝔢)(F) + Φ^a(F) = 𝔄^a(F). Therefore **𝒩_T^V(a) ⟺ 𝔄^a ⪰ 0 on V** (PROVED, one line).

Node margin: μ^V(T; a) := inf{𝔄^a(F) : F ∈ V, ‖F‖ = 1}. I write μ_N(T) := μ^{V_N}(T; Λ) and μ_∞(T) := μ^{V_∞}(T; Λ).

### 1.2 Sign step
A **sign step** for the node on a range 𝒯 of windows is a family Ψ = (Ψ_T)_{T∈𝒯}. Each Ψ_T(a; F) is real and defined for a in a domain 𝔇 ∋ Λ and F ∈ V. It must satisfy **validity**:

  (Val)  ∀a ∈ 𝔇, ∀T ∈ 𝒯:  [Ψ_T(a; F) ≥ 0 ∀F ∈ V]  ⟹  𝒩_T^V(a).

Also the **premise on ζ** must hold: Ψ_T(Λ; F) ≥ 0 ∀F, ∀T ∈ 𝒯.
- (Val) is the requirement that the proof be *a deduction*: "more identities" means precisely that the implication holds for every a in the domain over which the identities are theorems (lem:transfer, Def O1.2).
- If 𝔇 = {Λ}, any Ψ is valid and the notion is empty. That is why every class with content fixes a large 𝔇, or requires uniformity.

### 1.3 Multiplier norm
For two data a, b over the window, the difference of forms is (𝔄^a − 𝔄^b)(F) = (1/2π)∫ g_{a−b}(τ)|F̂(τ)|²dτ, with g_{a−b}(τ) = −Σ_{n<X}(v^a_n − v^b_n)cos(τ log n). I define
  ‖a − b‖_mult,T := sup_τ |g_{a−b}(τ)|.
Thus |𝔄^a(F) − 𝔄^b(F)| ≤ ‖a − b‖_mult,T ‖F‖² (PROVED). B_P (TOOLS_204U) is the difference a_P − Λ in this norm, uniformly bounded in T for fixed finite P. Two more facts:
- ‖·‖_mult,T ≤ Σ_{n<X}|v^a_n − v^b_n| (BARRIER_D2 Thm 1 in this form).
- The perturbation of a_1 (n = 1, c_F(0) = ‖F‖²) is the constant multiplier. Used in §3.

### 1.4 The class 𝒦
This is the requested definition, after pruning the initial hypotheses (see §2 for why (K2) and (K3) drop out).

**𝒦 = 𝒦_marg ∪ 𝒦_inh**, where:

- **𝒦_marg (quantitative continuity, pruned form of (K1)).** Ψ with domain 𝔇 containing the ball {a : ‖a − Λ‖_mult,T ≤ r} for each T, and such that there exist η > 0 and L < ∞ independent of T with:
  (K1a) margin at ζ: Ψ_T(Λ; F) ≥ η‖F‖² ∀F ∈ V;
  (K1b) Lipschitz: |Ψ_T(a; F) − Ψ_T(b; F)| ≤ L‖a − b‖_mult,T ‖F‖².
  More generally, (K1′) suffices: there is r > 0 independent of T such that {a : ‖a−Λ‖_mult,T < r} ⊂ {a : Ψ_T(a;·) ≥ 0}, with r = η/L in case (K1a–b). I also allow the weighted ℓ¹-norm variant from BARRIER_D2.

- **𝒦_inh (inherited premise, the form of (K2) that does have content).** Ψ whose premise "Ψ_T(a;·) ≥ 0" holds for every a in a family 𝔉 ∋ Λ that contains one of these certified falsifiers of the node:
  (α) a_P with P > e^{2T} (Theorem B, PROVED);
  (β) a_P with P = {2} or {2,3} (PRED-aP, NUMERICAL);
  (γ) cΛ with c < 0.9924 at ½log5 (NUMERICAL, NODE_001);
  (δ) the Beurling or DH weights, only if their 𝔪 coincides. It does not coincide for DH (conductor 5), so DH falls outside; see §2.3.
  Without a PROVED certificate that they fail the node, (β)–(δ) give only NUMERICAL.

Hypotheses (K2) and (K3) appear as corollaries (§2), not as clauses.

---

## 2. Three structural facts about the node (all PROVED)

### Lemma 1 (spectrahedron)
For fixed T and V, G_T^V := {x ∈ ℝ^{N_T} : 𝔄^{(x)} ⪰ 0 on V} is convex and closed. Here x = (v_n)_{n<X} and 𝔄^{(x)} = 𝔪 − Σ x_n c_F(log n). Moreover:
- μ^V(T; ·) is concave and 1-Lipschitz in ‖·‖_mult,T;
- its supergradient at Λ is (−c_{F⋆}(log n))_n for every real minimizer F⋆ (if one exists).

*Proof.* x ↦ 𝔄^{(x)}(F) is affine for each F, so G_T^V is an intersection of closed half-spaces and μ is an infimum of affine functions. For the Lipschitz bound I use |𝔄^{(x)}(F) − 𝔄^{(y)}(F)| ≤ ‖x−y‖_mult‖F‖² (§1.3). The supergradient is obtained as in lem:degen, which is exactly this over P_T. ∎

On V_∞ this is lem:degen restricted to the even sector. On V_N it is a compression, and the proof does not change. It is a restatement, not something new.

### Corollary 2 ((K3) is empty)
Every functional of the node depends on a only through (v^a_n)_{n<X}, because the node itself is a function of those numbers. "Weight n^{−½}" is then not a restriction on Ψ: it is a coordinate normalization. If Ψ used a_n/n, the reparametrization x_n = 2a_n/√n rewrites it in v. Hypothesis (K3) **does not narrow the class**. (PROVED, trivial.)

What (K3) was trying to capture is the weight gap from SYNTHESIS §4: the known positivities read primes at weight ≤ n^{−1}. That is not a property of the functional. It is the property that the premise be a theorem for every a with control at weight n^{−1}, and therefore be inherited by data whose comb at weight n^{−½} is arbitrary. It falls into 𝒦_inh or 𝒦_marg, depending on the case (§4).

### Corollary 3 ((K2) is empty and quartets do not falsify the node)
(a) 𝔪, 𝔢 and c depend only on T and on the Γ_ℝ factor with the pole. The conductor-1 FE enters the node only through them, which are fixed. Therefore **any** Ψ for the node uses the FE "only as symmetry": there is no other way for the FE to enter a statement about the LMI.

(b) The quartet models ξ_{z,k} (lem:shape-quartet) preserve the exact comb (Λ(n))_n, and hence v^{ξ_{z,k}}|_{n<X} = v^Λ|_{n<X}. Their node, in the sense of §1.1 (defined by the comb), **is identical** to that of ζ. Their witness of negative W lives in the absolutely continuous part −kβ_z, which the node does not see.

(c) Therefore the branch "(K2) + quartets ⇒ false node" **does not exist**. Quartets falsify deductions about the full form W^{ξ}, which includes −kB_z (EDITOR_O1, C2 obs. 4). They do not falsify deductions about the comb node. The same holds for f_t (lem:shape-ft) on windows with e^{2T} < λ₁, because it preserves Λ(n) for n < λ₁. (PROVED.)

**Reading.** The requirement of prop:shape-inputs / rem:conjunctions, which asks for (E) as a Dirichlet series and not merely as a comb identity, **is already satisfied** by any statement of the node, because the node is formulated over the comb. The question "E ∧ F jointly" then reduces, for the node, to: which data v ∈ ℝ^{N_T} with the *same* 𝔪 fall outside G_T and make the premise true? That is, to 𝒦_inh and 𝒦_marg.

**Consistency warning.** The phase 206 README, property (ii) ("uses that 𝔪 is the conductor-1 Γ_ℝ paired with Λ by the FE; quartets falsify it"), is correct for W but **incorrect for the comb node**. For the node, (ii) reads: 𝔪 is fixed and the FE cannot be "used further". I recommend correcting it (§6).

### Lemma 4 (the node's falsifiers are comb vectors)
A falsifier of the node at T is an x ∈ ℝ^{N_T} \ G_T^V. For a datum a to be one for Ψ, it is additionally required that Ψ_T(a;·) ≥ 0. Since 𝔪 is fixed, data with a different Γ factor or conductor (DH with q = 5, Epstein, ζ_K) **are not node data** for ζ. Their node has a different 𝔪, and they only falsify a Ψ that applies to all Γ factors (thm:noimport (i), with Lemma shape-epstein). (PROVED, by definition.)

---

## 3. Theorem A: the continuity branch (𝒦_marg)

### Theorem A
(a) **(PROVED, given lem:degen and the margin bound from P46 l. 3576, whose inputs are CITED.)** Let V = V_∞ and let Ψ ∈ 𝒦_marg with radius r = η/L > 0 independent of T. If Ψ is valid (Val) for all T ≥ T₀, then
  r ≤ μ_∞(T)  ∀T ≥ T₀.
This is impossible given the bound μ_∞(T) ≤ 4·10⁹ T e^{−15.449T}, examined below. More precisely, Ψ ceases to be valid as soon as T satisfies 4·10⁹Te^{−15.449T} < r.

(b) **(CONDITIONAL.)** For V = V_N (N ≈ 4T), the same conclusion holds under hypothesis (H_N): liminf_T μ_N(T) = 0. NUMERICAL evidence: margin 0.00185 with 2 modes and 10⁻⁶–10⁻⁷ with 3 modes at ½log5 (NODE_001, AUDIT_206).

(c) **(PROVED, dichotomy.)** If inf_{T≥T₀} μ^V(T) = μ_* > 0, the node itself, Ψ_T(a;F) := 𝔄^a(F), belongs to 𝒦_marg with η = μ_* and L = 1. In that case 𝒦_marg contains a valid step. Consequently: **𝒦_marg contains no valid step ⟺ inf_T μ^V(T) = 0.** This is the sought non-vacuity condition: the class does not trivially contain the node exactly when the node's margin is not bounded below.

*Proof of (a).* By (K1′), every a with ‖a − Λ‖_mult,T < r satisfies the premise. By (Val), it then satisfies 𝒩_T(a). Take a^{(s)} := Λ + s·δ₁ with s := r′/2 and r′ < r, i.e., add s to a_1. By §1.3, 𝔄^{a^{(s)}} = 𝔄^Λ − r′‖·‖², and ‖a^{(s)} − Λ‖_mult = r′ < r. Therefore 𝔄^Λ − r′ ⪰ 0 on V, i.e. μ^V(T) ≥ r′. Letting r′ → r gives μ^V(T) ≥ r.

The upper bound for μ_∞: in the even sector, V_∞ = P_T^ev ⊂ P_T. But the infimum over the even sector can be *larger* than λ_A, whose minimizer might be odd. **Caution:** P46 l. 3576 bounds λ_A = min(μ_ev, μ_odd). That is why the PROVED statement is for the **two-sector node** (V = P_T ∩ 𝒟_T, which is lem:degen as is), with μ = λ_A ≤ 4·10⁹Te^{−15.449T} for T ≥ 1. For the even sector alone, (a) is CONDITIONAL on the witness of the P46 bound being even. I record this as (H_ev). The P46 construction (l. 3576–3591) uses a test I did not verify sector by sector: OPEN-check, mechanical. ∎

*Proof of (c).* 𝔄^a − 𝔄^Λ is a multiplier of norm ‖a − Λ‖_mult. ∎

**Note on the choice of perturbation.** Using a_1 (constant multiplier) is legitimate in the multiplier topology, but one might object that a_1 ≠ 0 is not an "arithmetic datum". The robust variant: any perturbation with g ≤ −r′ on the support of F̂⋆ works. For example, a = Λ + s·1_{n=2}, with g = −2s·2^{−½}cos(τ log 2), works when F̂⋆ is concentrated where cos(τ log 2) > 0. In general, by lem:degen, any direction u with ⟨u, w_T⟩ > μ and ‖u‖_mult < r suffices. That is the Φ.14 transversality, whose applications to concrete families remain CONDITIONAL. With a_1 the theorem is PROVED. With Euler data (a_1 = 0) it remains CONDITIONAL on Φ.14-transversality.

### Corollary A1 (quantitative)
Every valid step with uniform margin η and Lipschitz constant L ceases to be valid from
  T_* ≈ (1/15.449)·log(4·10⁹·T_*·L/η),
of order 1.5 + 0.065·log(L/η). For a step of this kind to cover all T, its ratio L(T)/η(T) must grow at least like e^{15.449T}/(4·10⁹T). (PROVED in the two-sector version.)

This is exactly BARRIER_D2 Thm 2 ("continuation transfers only λ_A(a₀) − d_v") viewed from the functional rather than the path. It is new as a statement about arbitrary Ψ, but adds no information not already in lem:degen plus the margin bound. I state this explicitly.

---

## 4. Theorem B: the inheritance branch (𝒦_inh) with a PROVED falsifier

### Theorem B (PROVED)
Let 𝔉_E be the set of data a ≥ 0 such that Σ a_n n^{−s}/log n is the logarithm of an Euler product over ℕ with non-negative integer completely multiplicative Dirichlet coefficients, with a simple pole at s = 1, and a(p^k) = log p on its support. Let Ψ be a step whose premise holds on all of 𝔉_E. This includes the premise that the FE enters only through 𝔪, c and parity, which is automatic by Corollary 3. Then Ψ is not valid for the node, neither on V_N nor on V_∞, for any T > π/2.

*Proof.* Given T > π/2, choose a prime P > e^{2T}. By prop:shape-eulerdel (PROVED), a_P ∈ 𝔉_E, and v^{a_P}_n = 0 for all n < e^{2T}, because the smallest element of its support is P. Then comb^{a_P} = 0 and, on V, 𝔄^{a_P} = 𝔪.

lem:archcount, in its fully proved variant with t₁ = 3 (m(3) ≤ 0), says: for πN < 2T·3, 𝔪 ≤ −B(9 − (πN/2T)²)‖F‖² on span{sin(πk(x+T)/2T)}_{k≤N}, with B > 0. Take N = 3. The condition is T > π/2. The even subspace span{e₁, e₃} has dimension 2 and 𝔪 is negative definite there. Its intersection with c^⊥ has dimension ≥ 1 and is contained in V_N (because N ≈ 4T ≥ 3 when T > π/2) and in V_∞. There is then F ≠ 0 in V with 𝔄^{a_P}(F) = 𝔪(F) < 0. The node fails for a_P and the premise holds, so (Val) is false (lem:transfer). ∎

*Remarks.*
1. With the numerical constant t₀ = 6.2898 (NUMERICAL), the range lowers to T > 3π/(2t₀) ≈ 0.749. Below ½log5 ≈ 0.805 the node is PROVED (AUDIT_206), and between 0.749 and 0.805 there is overlap. It does not matter.
2. This is C2 transported to the node, with a shorter proof: it needs no WP_T, no 0.60 bound and no PRED-aP. For the "fixed P and T → ∞" version (B_P bounded), the falsifier remains NUMERICAL (n₋(𝔄^{a_{2}}_ev) = 2, …, 10; TOOLS_204U). An argument that a_P falsifies the node for *all* large T with fixed P **does not** follow from the zero-counting considered here. a_P has "zeros" at Re s = 0, β = 0. In the Weil-form model, the pair ρ = it, 1 − ρ = 1 − it contributes Φ_F(it)Φ_F(1−it), where Φ_F(s) = ∫F(x)e^{(s−½)x}dx. For F real, Φ_F(1−it) = F̃(½ − it) and Φ_F(it) = F̃(−½ + it): these are values at *distinct* points, not conjugates. The term is the bilinear form ⟨F, e^{(−½+it)·}⟩⟨F, e^{(½−it)·}⟩ plus its conjugate (from ρ̄): a hyperbolic form of rank ≤ 4 and signature (2,2) when the four functionals are independent. Each zero of a_P at Re s = 0 then contributes ≥ 1 negative direction *in the full form* (PROVED as algebra, Lemma 5 below). Going from there to n₋(𝔄^{a_P}|_{V_N}) ≥ 1 requires those directions to survive compression to E_N^ev and orthogonality with c, and not be offset by the zero part of ζ. That is ARGUED (the zeros of 1 − p^{−s} are at t = 2πj/log p, and for p = 2 the first ones, t ≈ 9.06, exceed the band ω_N ≈ 2π of E_N). **Honest remark:** with N ≈ 4T the band of E_N is |τ| ≲ 2π, and the zeros of 1 − 2^{−s} with |t| ≤ 2π are only t = 0 (double, with its pair). The numerical negativity of PRED-aP then comes from B_P (bands τ ≈ (2k+1)π/log 2 ≈ 4.53, inside the band), not from the zeros at Re s = 0. The "via zeros at Re s = 0" explanation of H1PLUS is, at most, an asymptotic reading. Hence it does not serve as a proof: the fixed-P branch remains NUMERICAL.

### Lemma 5 (zeros with β = 0 in the full form; PROVED, algebra)
Let q(F) = Re[2Φ_F(ρ)Φ_F(1−ρ)] for ρ = it, t ≠ 0, with F real. With u = Φ_F(it) and w = Φ_F(1−it), q = 2Re(uw). If the functionals F ↦ (Re u, Im u, Re w, Im w) are linearly independent, q has signature (2,2). *Proof:* 2Re(uw) = 2(u₁w₁ − u₂w₂) is a sum of two 2×2 hyperbolic forms. ∎

The sign is not "2β − 1 < 0". The contribution of an off-line zero in the Weil form is indefinite, not negative definite. This confirms that care was needed here.

### Theorem B′ (closure; ARGUED)
Let 𝔉 ∋ Λ be a family of data and Ψ a premise with these properties:
- it holds on 𝔉;
- it is closed in the topology of pointwise convergence of the v_n (e.g., an infimum of continuous functions of finitely many v_n).

Then the premise holds on the closure of 𝔉. In particular, if Λ is a limit of data a^{(j)} with true premise and false node, the premise cannot be strictly stronger than the node in a neighborhood. Candidate sequences are cΛ with c ↑ 1 or a_{P_j} with P_j → ∞. But a_P erases primes *smaller* than P, so in a fixed window a_P → 0 as P grows, and a_P = Λ only when P = 2. There is then no sequence of a_P converging to Λ on the window, except the constant a_2 = Λ. cΛ → Λ does converge, but its node is false only for c < c_*(T), which is NUMERICAL (0.9924 at ½log5). The closure argument reduces to Theorem A. **There is no independent closure branch.** (ARGUED, and negative for the question "a* in the closure".)

---

## 5. Check: the class contains all the dead mechanisms

| Mechanism (index) | 𝒦 branch | Why | Label |
|---|---|---|---|
| Linear in Λ (Theorem X, thm:noimport (iii), linear Hamburger) | 𝒦_marg ∪ Φ.14 | Ψ affine in v: uniform L. If the margin is uniform, Theorem A. If not, thm:noimport (iii): margin ≤ C·λ_A. Both cases are restatements. | PROVED (two sectors) |
| SOS / flat-top explicit formula (thm:sos) | empty | The decomposition does not exist for T ≥ ½log3. Stronger than 𝒦: no Ψ exists. | PROVED (P46) |
| Size bounds \|Φ\| ≤ 𝔪 + 𝔢 | 𝒦_marg | Every size bound "‖Φ^a‖ ≤ κ(𝔪+𝔢)" with κ < 1 is an open condition: (K1′) with r ≥ (1−κ)·inf\|𝔪+𝔢\|. Also false pointwise (SKELETON_002). | PROVED / NUMERICAL |
| Analytic defect of the FE (BARRIER_D1 Thm 4) | 𝒦_marg | AUDIT_9: "continuity suffices". The (one-sided) residue R1 already closed: continuous ⇒ 𝒦_marg; discontinuous ⇒ cone/certificate (outside, §6). | PROVED (Thm 4) + Theorem A |
| Selberg / Dirichlet series identities (NODE_001 Prop N.2, TB-3) | 𝒦_inh | Hold for every Dirichlet series ⇒ hold on a_P (P > e^{2T}) ⇒ Theorem B. | PROVED |
| Gram \|P_X\|² ≥ 0 (NODE_001 Prop N.3) | 𝒦_inh (via N.2) or J1 | Reduced to Selberg or to J1 (closed by H_sparse). | PROVED given N.3 |
| Turán / PF_k / convexity (L22, L23, L75, A14a) | 𝒦_inh | These are properties of log ζ(σ) or of coefficients that hold for every Euler product with coefficients ≥ 0 (in particular ζ_{a_P}): convexity of log ζ_a(σ) for σ > 1 by Cauchy–Schwarz, log-concavity of moments of a positive measure. ⇒ Theorem B. Whether *every* concrete index entry has an inheritable premise was not checked one by one. | ARGUED |
| Loewner / Pick | — | Falls on the zeros side (thm:Z). It is a restatement (REF-D), not a sign step. This theorem does **not** kill it. It is outside 𝒦, see §6. | — |
| C2 (E + shape FE) | 𝒦_inh | Theorem B is C2 at the node. | PROVED |
| B_P, PRED-aP | 𝒦_inh (β) | NUMERICAL falsifier for fixed P. | NUMERICAL |
| Continuation in T / comb homotopy (BARRIER_D2) | 𝒦_marg | D2's Thm 2 is Corollary A1 in path form. | PROVED |
| Szegő/Widom, PF/Markov | 𝒦_marg | Asymptotics with uniform or norm error: (K1′). | ARGUED |

**Non-vacuity.** The node itself, Ψ = 𝔄^a|_V, is in 𝒦_marg only if inf_T μ > 0, and is in 𝒦_inh only if its premise holds on a falsifier, which is contradictory. By Theorem A(c) and the margin bound, in the two-sector version the node **does not** belong to 𝒦. The class does not contain it trivially. (PROVED in two sectors; CONDITIONAL (H_N) for V_N.)

**Is the class circular?** 𝒦_inh is not: it is a list of data with a certificate. Neither is 𝒦_marg: it is a condition on Ψ, verifiable without knowing the node. What is nearly circular is the **complement** (§6).

---

## 6. What falls outside 𝒦: the forced shape of the sign step

Combining Theorems A and B, a step Ψ valid for all T must satisfy the two following conditions. The conclusion is PROVED in the two-sector version with the a_1 perturbation, and CONDITIONAL otherwise.

**(O1) Exponential fineness.** The ratio L_T/η_T between the sensitivity of Ψ in multiplier norm and its margin at Λ must be ≥ 1/μ(T) ≥ e^{15.449T}/(4·10⁹T). In other words: the set {Ψ_T ≥ 0} must touch ∂G_T at distance ≤ μ(T) from Λ. There are three ways to achieve this:
- (O1-i) Ψ is an **identity with remainder**: Ψ_T(a;F) = 𝔄^a(F) − R_T(a;F) with R_T ≥ 0 and R_T(Λ;·) ≤ μ(T) as forms.
- (O1-ii) Ψ is **discontinuous** at Λ in the multiplier topology: it jumps when a coefficient is moved.
- (O1-iii) Ψ is continuous but with a modulus that degrades exponentially with T: determinant-type amplification, conditioning, or a product of ~T factors.

**(O2) Not inheritable by the empty window.** The premise must fail for a_P with P > e^{2T}, i.e., for the null comb with the same 𝔪, c, pole and Euler product. Therefore the premise **must read values of Λ(n) with n < e^{2T}** in a way that the null comb violates. No property of "being the log-derivative of an Euler product with a pole" suffices.

**On "tail invariant with FE".** For fixed T, the node is a statement about the window n < e^{2T}. The tail of primes p > e^{2T} **does not enter** the node. Therefore "sensitive to the tail" is not a property a *valid* Ψ_T can have for that T: two data with the same window have the same node. What is called "tail" is really **uniformity in T**: a formula Ψ that, applied at T, uses the window of T. The distinction "Euler over all primes" versus "over almost all" is, window by window, the distinction between the vector v^Λ and the vector v^{a_P}, which differ in the coordinates p^k < e^{2T} with p < P. It is a **finite, local** difference, not a tail one. (PROVED, by the support remark.) That is why the formulation "tail invariant + FE" **does not apply to the node**.

For the full W it would apply, because W sees the entire product through the zeros, and that is why quartets falsify it but not the node.

**Known instances (explored without being built).**
- *Residue at s = 1 and Mertens* (Σ_{p≤x} log p/p = log x + O(1)): linear in Λ and shared by a_P up to O(1) per erased prime ⇒ 𝒦_marg ∪ 𝒦_inh. Dead.
- *C₀ = ψ(¼) − log π* and the constant ζ′/ζ(0) = log 2π: these are 𝔪 data or linear functionals of Λ via continuation. C₀ is the same throughout the node (fixed). (ζ′/ζ)(0) = log 2π links Λ with Γ_ℝ via the FE, but is linear in Λ (with regularization), so it is Theorem X / thm:noimport (iii). Dead as a sign step. I know of **no** nonlinear window invariant mixing Λ(n), n < e^{2T}, with Γ_ℝ outside the explicit formula (thm:Z, which is (O1-i) with R = sum over zeros, i.e. REF-D). (ARGUED.)

**Is the complement circular?**
- (O1-i) with R_T = sum over zeros is REF-D by lem:shape-restate. Any other R_T ≥ 0 with ‖R_T‖ ≤ μ(T) requires estimating R_T to precision e^{−15.4T}, which is the node's own precision. This is **nearly circular**: not impossible, but all the difficulty stays inside R_T.
- (O1-ii) is the "discontinuous ⇒ cone/certificate" residue from AUDIT_197_2 (R1 closed). By thm:sos/thm:Z, certificates are the flat-top explicit formula. Also nearly circular.
- (O1-iii) is the only exit not yet examined as such: a Ψ whose sensitivity grows like e^{cT} with c ≥ 15.449 *by construction*, not from being close to ∂G_T. Examples of shape (not content): determinants of size ~T (Hankel/Toeplitz of the v_n), *evaluated* truncated Euler products, not log-derivatives (∏_{p<e^{2T}}(1 − p^{−s})^{−1} at window points: its sensitivity to a_p is multiplicative), and moments of order ~T. The determinant of the node's own matrix has sensitivity 1/μ and is circular (it is the node). An unrelated one, of sensitivity ~e^{15.4T} by size, **is not** in the index as a class. **This is the shape lead 2 must have:** positivity of an object of size ~T whose natural conditioning (not inherited from the node) is ≥ e^{15.449T}, that reads the Λ(n) of the window, and that fails for the null comb with the same Γ_ℝ.

Compatibility note with the semiring principle: the evaluated Euler product, with m ≈ kn interaction, is precisely a multiplicative amplification of type (O1-iii). I do not assert this; I only record it as a coherent filter.

---

## 7. Corollaries, abstract falsifiers, program gain

### 7.1 One-shot kills
Theorem A + Theorem B kill, each in a single clause, the following routes:
- **By A (𝒦_marg):** linear in Λ, size bounds, analytic defects of the FE, continuation/homotopy, asymptotics with uniform error (Szegő/Widom), first-order discriminants in h*.
- **By B (𝒦_inh):** Selberg identities, Gram squares via N.3, Turán/PF/convexity (ARGUED), C2, every "structural Euler + pole property".

### 7.2 Abstract falsifiers
- **(FA-1)** For 𝒦_marg: Λ + s·δ₁, the constant multiplier. PROVED. Arithmetic variants (Λ + s·δ₂, cΛ) are CONDITIONAL (Φ.14).
- **(FA-2)** For 𝒦_inh: a_P with P > e^{2T} (empty window). PROVED for T > π/2.
- Quartets and f_t are **not** falsifiers of the node (Corollary 3).

### 7.3 What the program gains if everything ends up PROVED
1. **Reclassification.** Index rows marked "NO-GO by falsifier" for W or λ_A, whose mechanism is uniformly continuous or inheritable by Euler + pole, get relabeled for the node as instances of Theorem A or B. No new falsifier is needed per route.
2. **Correction of skeleton 206.** Property (ii) of the 206 README ("quartets falsify it") is false for the comb node. The FE is not an extra input of the node's sign step, because it is already fixed in 𝔪. The "E ∧ F jointly" of rem:conjunctions translates, at the node, into (O2): reading window values so that the null comb fails.
3. **Specification for lead 2:** (O1-iii) ∧ (O2). A single line that filters candidates before building.

### 7.4 What remains OPEN or CONDITIONAL
- (H_ev): that the P46 margin bound has an even witness. A mechanical check.
- (H_N): μ_N(T) → 0 with N ≈ 4T. NUMERICAL evidence in favor.
- Φ.14-transversality for arithmetic perturbations (a_1 = 0).
- PROVED falsifier with fixed P (B_P) for large T: NUMERICAL.
- Turán/PF row by row: ARGUED.

---

## 8. Index entry

- **CLASS_001 (phase 207, lead 1):** class impossibility theorem for the node's sign step 𝒩_T. New reason: the object is the node (a finite LMI in v_n, n < e^{2T}), not λ_A/W; it quantifies over every Ψ.
  - **Lemma 1 (PROVED):** G_T is a spectrahedron; μ is concave and 1-Lipschitz in multiplier norm.
  - **Cor 2–3 (PROVED):** (K3) and (K2) ("weight n^{−½}", "FE only as symmetry") are empty for the node. Quartets and f_t **do not** falsify the node (same comb). Corrects property (ii) of README 206.
  - **Theorem A (PROVED in two sectors with the a_1 perturbation, P46 inputs CITED; CONDITIONAL (H_ev), (H_N) for the even sector and for N ≈ 4T):** no Ψ with uniform margin η and Lipschitz constant L is valid for T with 4·10⁹Te^{−15.449T} < η/L. Dichotomy: 𝒦_marg has a valid step ⟺ inf_T μ > 0.
  - **Theorem B (PROVED):** every premise inherited by Euler products with a pole fails on a_P with P > e^{2T} (null comb; lem:archcount with t₁ = 3), for all T > π/2. It is C2 at the node, without PRED-aP.
  - **Lemma 5 (PROVED):** a zero with β = 0 contributes signature (2,2), not a sign. PRED-aP with fixed P remains NUMERICAL (its negativity comes from the bands of B_P, not from those zeros).
  - **B′ (closure): ARGUED, no branch of its own.**
  - **Forced shape:** (O1) exponential fineness e^{15.449T} (identity with remainder ⇒ REF-D, or discontinuous ⇒ certificate, or size-~T amplification, the only exit not yet examined) ∧ (O2) premise false for the null comb with the same Γ_ℝ. "Tail invariant + FE" does not apply to the node (the tail is not in the window).
  - Do not retry uniformly continuous mechanisms nor premises inheritable by Euler + pole for the node.
  - No sign. Row D OPEN.
  (`03-research/phase-207-class-impossibility-and-empty-cell/CLASS_001.md`)
