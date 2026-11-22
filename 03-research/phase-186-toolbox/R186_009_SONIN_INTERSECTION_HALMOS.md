# R186.009 — The semilocal Sonin intersection via two projections (Halmos) and formula (84)_S

Model of R186.007/008: L²(ℝ₊,du), P = 1_{(0,λ]}, F_∞ (kernel 2cos 2πux), E = Σ_{k≥0}D_{2^k}, F_S = E F_∞ E⁻¹ = F_∞U, U = e^{iφ(D)}; P̂^S := F_S P F_S^{-1}; Q₁ := 1−P, Q₂ := 1−P̂^S; Π_S := Q₁∧Q₂ (semilocal Sonin projection); A_S := PF_SP.
Notation: CC write P for our Q₁ (support outside [−1,1]).

## Status

| # | Statement | Label |
|---|---|---|
| L0 | F_S is a **self-adjoint unitary involution** (F_S² = 1) and F_S ϑ(ρ) F_S = ϑ(ρ⁻¹). Hence A_S = PF_SP is self-adjoint, compact, real spectrum λ_n ∈ (−1,1)∖{0} | PROVED |
| H | Halmos frame: generic part of (Q₁,Q₂) ≅ generic part of (P,P̂^S); cos²θ_n = λ_n(A_S)²; ran Q₁∩ran Q₂ = son_λ(X_S); ran Q₁∩ker Q₂ = F_S(ker A_S) | PROVED (dim son = ∞: CITED CCM) |
| G | **Gap**: spec(Q₁Q₂Q₁|_{ran Q₁}) ⊂ {0} ∪ {λ_n²} ∪ {1}, sup λ_n² = λ_1² < 1; Π_S = 1_{\{1\}}(Q₁Q₂Q₁) is a Riesz (holomorphic) projection | PROVED (uses R186.007: A_S compact with no eigenvalue ±1) |
| D | Exact decomposition: Π_S = Q₁Q₂Q₁ − Σ_n λ_n² \|ζ_n⟩⟨ζ_n\|, ζ_n := (1−P)F_Sξ_n/√(1−λ_n²), {ξ_n} eigenbasis of A_S; {ζ_n} orthonormal | PROVED |
| (84)_S | Son_S(h) = W_∞(f) − (prime comb of 2)(f) + ∫ f(ρ⁻¹) ε'_S(ρ) d*ρ, ε'_S = ε_∞ + κ_S; for ρ ≥ 1, ε_S(ρ) = Σ_n λ_n(1−λ_n²)^{-1/2}⟨ξ_n\|ϑ(ρ⁻¹)ζ_n⟩ (formal identity, CC (84), with semilocal data) | CONDITIONAL on (TC_S) and on the convergence (CV_S) |
| Δ | ε'_S − ε_∞ = κ_S: the prime comb comes out **exactly** (Thm C′) and κ_S = compression/angle correction, explicit formula §5 | PROVED as a distributional identity, given (TC_S) |
| d | The generic diagonal part d_S(f) := Σλ_n²⟨ζ_n\|ϑ(f)ζ_n⟩ is **not** L^∞_loc near ρ = 1 | PROVED (given TC_S) |
| C | In (84)_S the diagonal part d_S **cancels exactly** (as in CC (89)–(90)); the divergence Σλ_n² = ∞ does not reach ε_S | PROVED (algebraic) |
| B | Boundedness of ε_S (equivalently of κ_S): weights λ_n/√(1−λ_n²) ≍ n^{−1/2} (ARGUED R186.008) — **not** absolutely summable; decided by the decay of c_n(ρ) := ⟨ξ_n\|ϑ(ρ⁻¹)ζ_n⟩ | OPEN (exact criterion §6) |
| (TC_S) | ϑ(g)Q₁Q₂ is Hilbert–Schmidt for g ∈ C_c^∞(ℝ*₊) | OPEN (reduced in §4 to a uniform archimedean bound) |
| NUM | Galerkin estimate from s2.py | NOT CARRIED OUT (R186.008: N ≤ 40 insufficient for the n^{−1/2} tail; working rule: numerical only when strictly necessary) |

**Verdict.** The question "does Σλ²/(1−λ²) ≍ Σ1/n diverge ⇒ ε_S unbounded?" is resolved **negatively in its naive form**: the series Σλ_n² (= ‖A_S‖²_HS = ∞) lives in the diagonal part, which cancels exactly between Tr ϑ(f)Q₁Q₂Q₁ and the generic part (it is CC (90) word for word, because F_S is a self-adjoint involution that inverts ϑ). What remains in ε_S are the **cross** terms with weight λ_n/√(1−λ_n²) ≍ n^{−1/2}, which are also not absolutely summable. Neither does (M) fall nor is it proved: the question reduces exactly to the decay of the cross coefficients c_n(ρ) (boundary mass of ξ_n in [λ/ρ, λ]). Structurally: the prime comb enters **exact and separate**, and all the nonlinear difficulty is κ_S.

## 1. Lemma L0 (PROVED)

In the logarithmic variable, E and E^* are functions of D, hence commute. From F_∞EF_∞ = E^* (R186.007 §1) and F_∞² = 1: F_∞UF_∞ = (F_∞E^*F_∞)(F_∞E⁻¹F_∞) = E(E^*)⁻¹ = U^*. Hence F_S² = F_∞UF_∞U = U^*U = 1; F_S unitary and involutive ⇒ self-adjoint. Also F_∞ϑ(ρ)F_∞ = ϑ(ρ⁻¹) (F_∞DF_∞ = −D) and U commutes with ϑ(ρ) (both functions of D), hence F_Sϑ(ρ)F_S = F_∞Uϑ(ρ)U^*F_∞ = ϑ(ρ⁻¹). ∎
Consequence: P̂^S = F_SPF_S, PP̂^SP = A_S², and the sign alternation of R186.007 is that of real eigenvalues of a self-adjoint operator (not of singular values).

## 2. Halmos frame (H, G: PROVED)

For two projections, the five Halmos summands of (Q₁,Q₂) and of (1−Q₁,1−Q₂) = (P,P̂^S) coincide except for an exchange of the four intersection summands; the generic part is common and, with Q₁ = [[1,0],[0,0]], Q₂ = [[c²,cs],[cs,s²]], one has P = [[0,0],[0,1]], P̂ = [[s²,−cs],[−cs,c²]], so Q₁Q₂Q₁ = c²⊕0 and PP̂P = 0⊕c²: **the same** cos²θ. Since PP̂^SP = A_S² with A_S compact self-adjoint, cos²θ has point spectrum {λ_n²} accumulating only at 0. Intersections:
- ran Q₁∩ran Q₂ = son_λ(X_S) (CCM isosonin, CITED: dim ∞);
- ran P∩ran P̂^S = ker(A_S² − 1) = 0 (R186.007, no eigenvalue ±1);
- ran Q₁∩ker Q₂ = ran(1−P)∩ran P̂^S = F_S(ker A_S) (ξ ∈ ran P with PF_Sξ = 0);
- ker Q₁∩ran Q₂ = symmetric F_S-image, irrelevant for Π_S.
Gap: λ_1² < 1 because the supremum of the spectrum of a compact self-adjoint operator is attained and ±1 is not an eigenvalue. Hence 1 is isolated in spec(Q₁Q₂Q₁) and Π_S = (2πi)⁻¹∮_{|z−1|=r}(z−Q₁Q₂Q₁)⁻¹dz with r < 1−λ_1²; also Π_S = s-lim (Q₁Q₂Q₁)^n with ‖(Q₁Q₂Q₁)^n − Π_S‖ = λ_1^{2n} (von Neumann convergence **in norm**, at a geometric rate: this is the operator version of the gap condition of R183.031, unconditional here). ∎

## 3. Decomposition D (PROVED)

Let {ξ_n} be an orthonormal eigenbasis of A_S on ran P (including a basis of ker A_S, λ = 0). F_Sξ_n = λ_nξ_n + (1−P)F_Sξ_n, and ⟨(1−P)F_Sξ_n,(1−P)F_Sξ_m⟩ = δ_{nm} − λ_nλ_m δ_{nm}. So ζ_n := (1−P)F_Sξ_n/√(1−λ_n²) is orthonormal and generates ran Q₁ ⊖ son (= closure of Q₁ ker Q₂ = (1−P)F_S ran P). It is an eigenvector of Q₁Q₂Q₁ with eigenvalue λ_n²: Q₁P̂^SQ₁ζ_n = (1−λ_n²)ζ_n. Hence
 Q₁ = Π_S + Σ_n|ζ_n⟩⟨ζ_n|, Q₁Q₂Q₁ = Π_S + Σ_n λ_n²|ζ_n⟩⟨ζ_n|.
The sum converges strongly; as an operator f(Q₁Q₂Q₁), f(x) = x1_{x<1}, it has norm λ_1² and is **not** trace class nor HS (Σλ_n² = ∞, R186.007 Thm 5). This is CC's (81)/(90) with (P,P̂,prolates) ↦ (Q₁,Q₂,ξ_n). ∎

## 4. The trace step (TC_S)

Son_S(h) := Tr(ϑ(g)Π_Sϑ(g)^*) ∈ [0,∞] always. By §3, ‖ϑ(g)Q₁Q₂‖²_HS = Son_S + d_S(g*g^*), d_S(f) := Σλ_n²⟨ζ_n|ϑ(f)ζ_n⟩ ≥ 0. Hence: (TC_S) ⟺ Son_S < ∞ and d_S < ∞ ⟺ Tr ϑ(f)Q₁Q₂Q₁ < ∞.
Reduction. Q₂ = F_∞(1 − UPU^*)F_∞ and UPU^* = Σ_{n,m}u_nū_m P_{a−nc}T_{(n−m)c} (R186.008 §4), u_1 = −q, u_n = q^{−n}(1−q²) (n ≤ 0). By scale quasi-covariance, ‖ϑ(g)(1−P_a)F_∞(1−P_b)‖_HS = H_g(√(λλ_b)), with H_g(μ)² = Tr ϑ(f)Q₁^{(μ)}Q₂^{(μ)}Q₁^{(μ)} the archimedean case at level μ (finite: CC (43)/(85), CITED). Sufficient for (TC_S): Σ_{n,m}|u_n||u_m|H_g(λ2^{|n|/2}) < ∞, i.e. H_g(μ) = o(μ) as μ → ∞.
Warning (why this remains OPEN): the trivial bound H_g(μ)² ≲ ‖f‖_{L¹}·#{level-μ prolates} ≍ μ² gives H_g ≍ μ, **exactly** at the boundary, compensated by q^{|n|} = λ/μ with no margin. The triangle inequality does not decide; one needs orthogonality between the shifted terms or the δ_μ asymptotics of CC in μ. Label: OPEN, with the bound H_g(μ) = o(μ) as the only pending lemma.

## 5. Formula (84)_S and decomposition Δ (CONDITIONAL on TC_S; algebra PROVED)

The ingredients of the proof of CC Thm 4.7 are exactly: (i) F a self-adjoint involution, (ii) Fϑ(ρ)F = ϑ(ρ⁻¹), (iii) support: ⟨ζ_n|ϑ(ρ⁻¹)ξ_n⟩ = 0 for ρ ≥ 1 (ξ_n supported at u ≤ λ, ϑ(ρ⁻¹) contracts it, ζ_n supported at u > λ), (iv) spectral decomposition §3, (v) a local trace formula for Tr ϑ(f)Q₁Q₂Q₁. (i)–(iv) hold for F_S by L0, §3. Step by step:
- (87)_S: ⟨F_Sξ_n|ϑ(ρ⁻¹)F_Sξ_n⟩ = ⟨ξ_n|ϑ(ρ)ξ_n⟩ (by (ii)); expanding F_Sξ_n = λ_nξ_n + √(1−λ_n²)ζ_n gives the relation between ⟨ξ|ϑξ⟩, ⟨ζ|ϑζ⟩ and the cross terms with τ_n = λ_n/√(1−λ_n²) — identical to CC (77)/(87).
- (88)–(89)_S: δ_S(ρ) = Σλ_n²⟨ζ_n|ϑ(ρ⁻¹)ζ_n⟩ + ε_S(ρ), ε_S(ρ) = Σ_n λ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑ(ρ⁻¹)ζ_n⟩, ρ ≥ 1 (the cross terms ⟨ζ|ϑ(ρ⁻¹)ξ⟩ vanish by (iii)); symmetry ρ ↦ ρ⁻¹ by (ii).
- (90)_S: Tr ϑ(f)Q₁Q₂Q₁ = Son_S(f) + d_S(f) (§3, §4). **The diagonal part d_S cancels** and one is left with Son_S = [linear term] + ∫fε_S.
(v) is replaced by: Tr ϑ(f)Q₁Q₂^SQ₁ = Tr ϑ(f)Q₁Q₂^∞Q₁ − Tr ϑ(f)Q₁XQ₁, X := P̂^S − P̂_∞, and
 Q₁XQ₁ = X − PX − XP + PXP, Tr ϑ(f)X = Σ_k log2·2^{−k/2}(f(2^k)+f(2^{−k})) (Thm C′, exact).
Result (Δ): with δ_∞ from CC (85),
 Son_S(f) = W_∞(f) − comb₂(f) + ∫f(ρ⁻¹)[ε_∞(ρ) + κ_S(ρ)]d*ρ,
 κ_S := dens[Tr ϑ(f)(PX + XP − PXP)] − (d_S − d_∞) + (d_S − d_∞) − (diagonal of (PXP) absorbed) ≡ ε_S − ε_∞ + comb₂-density,
i.e. ε'_S := ε_S + (density of the comb) = ε_∞ + κ_S, with κ_S the density of Tr ϑ(f)(PX+XP−PXP) minus the variation of the generic diagonal. Since the prime term of E_S at p = 2 coincides with comb₂ (R186.008 C, C′):
 **E_S(h) = Son_S(h) − ∫c_h(x)(ε_∞ + κ_S)(e^{|x|})dx** (semilocal version of CC (83); R′_S = −∫c_h ε'_S),
with no residual prime term: the comb is absorbed exactly into Son_S. ∎ (CONDITIONAL on TC_S and on κ_S being a locally order-0 distribution, see §6.)

## 6. Boundedness: what is proved and what remains

**Prop. d (PROVED, given TC_S).** d_S ∉ L^∞_loc near ρ = 1. Proof: g_k ≥ 0 an approximate identity in L¹(d*ρ), ‖g_k‖₁ = 1, ϑ(g_k) → 1 strongly. Fatou: liminf d_S(g_k*g_k^*) = liminf Σλ_n²‖ϑ(g_k)ζ_n‖² ≥ Σλ_n² = ∞. If d_S ∈ L^∞ near 1, |d_S(f_k)| ≤ ‖d_S‖_∞‖f_k‖₁ ≤ ‖d_S‖_∞. Contradiction. ∎ (Archimedean: Σλ(n)² < ∞, no phenomenon.)
**Prop. C (PROVED).** d_S does not appear in ε_S (cancellation §5 (90)_S). Hence Prop. d does **not** imply that ε_S is unbounded: the divergence feared by the target lies in the part that cancels.
**Exact criterion for (M).** c_n(ρ) := ⟨ξ_n|ϑ(ρ⁻¹)ζ_n⟩ satisfies c_n(1) = 0, |c_n| ≤ 1, and |c_n(ρ)| ≤ ‖1_{[λ/ρ,λ]}ξ_n‖ (only the boundary mass of ξ_n contributes: ϑ(ρ⁻¹)ξ_n is supported at u ≤ λ/ρ… after inversion, the overlap with supp ζ_n ⊂ (λ,∞) comes from the boundary shell). Sufficient for ε_S ∈ L^∞_loc:
 (CV_S) Σ_n |λ_n| ‖1_{[λ/ρ,λ]}ξ_n‖ < ∞ locally uniformly in ρ,
and sufficient for ε_S ∈ L²_loc the quadratic version with cancellation. With |λ_n| ≍ n^{−1/2} (ARGUED), (CV_S) requires boundary mass ‖1_{[λ/ρ,λ]}ξ_n‖ = O(n^{−1/2−δ}). In the archimedean case the boundary mass of high-index prolate functions is O(1) (they concentrate near the boundary), and convergence is provided by λ(n); if the same behavior occurs for A_S, ε_S is **not** absolutely convergent and its boundedness would depend on sign cancellation — the alternation λ_{2j−1} > 0 > λ_{2j} (R186.007) is precisely the candidate mechanism. OPEN.

## 7. Consequence for the toolbox

1. The prime comb lives **exactly** in the linear part (Thm C′) and is absorbed into Son_S with no remainder: (M) is reformulated without the comb as "κ_S ∈ L^∞ (or HS on L²(I_T))".
2. The non-HS character of A_S does **not** contaminate ε_S through the diagonal (exact cancellation); it potentially contaminates through the cross terms with weight n^{−1/2}.
3. Bifurcation: (a) if the boundary mass decays (CV_S), ε_S is bounded, R′_S is compact as in R183.018, and (M) reduces to a bound on κ_S on L²(I_T): the explicit pending lemma = (CV_S) + H_g(μ) = o(μ). (b) If the boundary mass is O(1) with no alternating cancellation, ε_S is unbounded at ρ = 1 and the positive part of the semilocal Sonin over-subtracts; then one must return to the gap requirement of R183.031 with a different positive part — which, by §2, can be taken as (Q₁Q₂Q₁)^N with error λ_1^{2N} in norm (not in trace).

## Audit notes

- L0 is the new point and verifiable in two lines: F_∞UF_∞ = U^* only uses that E, E^* commute (functions of D in the logarithmic variable). If rejected, A_S is not self-adjoint, eigenvalues are replaced by singular values, and (87)_S loses its symmetry; the rest of §3 survives with singular values.
- The target wrote the weight λ²/(1−λ²); the correct weight in ε of CC (84) is λ/√(1−λ²) (the λ²/(1−λ²) is that of f(Q₁Q₂Q₁) in the non-normalized basis (1−P)F_Sξ_n). The "logarithmic divergence Σ1/n" corresponds to Σλ_n² = ‖A_S‖²_HS, which is in the canceled diagonal.
- §5 is CONDITIONAL: TC_S (§4) is not proved; the trivial bound sits exactly at the boundary (H_g ≍ μ against q^{|n|} = λ/μ). Son_S < ∞ is not claimed.
- The expression for κ_S in §5 is a definition by difference; its content is "density of Tr ϑ(f)(PX+XP−PXP) minus diagonal variation." It has not been proved to be a function.
- Nothing numerical: the relevant tail is n ≫ 40.

## For Paper 46

Add as a remark (not a main theorem): "F_S = EF_∞E⁻¹ is a self-adjoint unitary involution that reverses scale; consequently the derivation of CC Thm 4.7 carries over word for word to the semilocal case and gives E_S = Son_S − ∫c_h ε'_S with the prime term absorbed exactly; the finiteness of Son_S and the boundedness of ε'_S remain open (TC_S), (CV_S)". Labels: L0, H, G, D PROVED; (84)_S CONDITIONAL; boundedness OPEN. Do not use any equivalence with RH.

## Note (R186_095)

* Operator gap G PROVED: cos²θ_n = λ_n²; sup = λ₁² < 1; ‖(Q₁Q₂Q₁)^n − Π_S‖ = λ₁^{2n} exact. L0, H, G, D tool-ready.
* M1: the reduction TC_S ⟸ H_g(μ)=o(μ) is ARGUED (TC_S is proved PROVED by R186_010 via another route). M2: Δ is DEFINITION + CONDITIONAL (κ_S by difference; traces of ϑ(f)PX etc. not proved). M3: withdraw "operator version of the R183_031 gap" (different gaps). Prop C → CONDITIONAL. Weight λ/√(1−λ²) correct.
