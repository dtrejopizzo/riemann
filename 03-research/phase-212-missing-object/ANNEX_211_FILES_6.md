# Annex 211 — files ROUND_001_B to ROUND_007_B (complete reading)

Source: `../phase-211-sign-sandbox/`, files `*.md` in alphabetical order from `ROUND_001_B.md` to
`ROUND_007_B.md` inclusive (19 files). Notation of `STATEMENT_001.md`: a_T = Arch − Π on P_T, λ_A(T),
v_n = 2Λ(n)/√n, N_T = {n ≥ 2 : log n < 2T}, A_T = Σ_{N_T} v_n, K the Lévy kernel, C_0 = m(0). The goal is
(★): λ_A(T) ≥ 0 for all T. Labels as in the files. «Next step taken» indicates whether a later file
in the range carried it out.

---------------------------------------------------------------------------------------------------

## Entries by file

### 1. ROUND_001_B.md — exterior form: fused object and sign
- Object: half-line identity W_T(Ef) = 𝒲[Ψ_f], Ψ_f = Φ_f 1_{(−∞,−T)}, Φ_f(x) = e^{x/2}Σ_n f(ne^x),
  Φ̃_f = ζ·Mf; complete form 𝒲 on the line; arbitrary combs w 𝒲^w = 𝒲 + 𝒫_{Λ−w}.
- Thm 1.1 (radical lemma, proof without zeros; inputs (I) coefficients 1, (E) Λ∗1 = log, (F) functional equation): PROVED.
- Cor 1.2 (half-line identity): PROVED.
- Prop 1.3 (defect for an arbitrary comb: W^w_T(Ef) − 𝒲^w[Ψ_f] = 𝒫_{Λ−w}[Ef] − 𝒫_{Λ−w}[Ψ_f]): PROVED.
- Prop 1.4 (no common radical vector of 𝒲 and 𝒲^c, c ≠ 1): PROVED; non-existence of any summation map for cΛ/Beurling: ARGUED.
- Prop 1.5 (the c-exterior value is not gauge invariant): reduction PROVED, last step ARGUED.
- Lemma 1.6 (monotonicity of the comb on cells; cell positivity holds for all w ≤ Λ): PROVED → NO-GO of the «key cancellation» as a source of sign (class: cones with definite-sign comb pairing).
- §1.7 the fused reading does not satisfy clause (5): exterior datum (ζM_N − 1)g̃ (identity PROVED; classification ARGUED).
- Lemma 2.1 (the boundary is a point and is flat; Ψ̌(0⁺) = Σ_{k<N}h(k) = 0 on the kernel): PROVED.
- Prop 2.2 (boundary terms only archimedean): PROVED → residue «layer edges κ_{T+log n}» empty, NO-GO (class: archimedean-only terms).
- Prop 2.3 (φ_0 enters only through the scalar I(g) = σ_g(0)M̃_1(N)): PROVED.
- Prop 2.4 (under (ext-L), near-minimizers concentrate in a finite prolate sector): CONDITIONAL ((ii) also NUMERICAL).
- Unsigned remainder: defect (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]) indefinite; block of classes a ≥ 2 of the lattice reduction: OPEN («no justified attempt without a new identity»).
- Reusable positives: Thm 1.1/Cor 1.2 (exact comb Λ, ζ with Γ_ℝ at conductor 1); Prop 1.3 (every comb w ≥ 0 with Dirichlet series convergent in σ > 1); Lemma 2.1, Prop 2.2, 2.3.
- Next step: write Q₁ of the Γ-limit as a K×K matrix in the weights and decide whether it separates Λ from cΛ (c < 1) and a_P. Taken: yes, ROUND_002_B (result: monotone, NO-GO).

### 2. ROUND_001_C.md — exact Nyquist reduction with η ↓ 0
- Object: samples s_k = s_T(ω_k + α) + c(−1)^k, ω_k = πk/2T; block 𝒩 = {s_k ≤ 0}; Schur complement S on N′ = pr_T 𝒩_η.
- Lemma 1 (shifted and alternating Nyquist identity): PROVED. Lemma 2 (two shifted sectors, gauge c(−1)^k): PROVED.
- Thm 1 ((L2′): λ_A ≥ 0 ⟺ S ⪰ 0, dim N′ ≤ |𝒩|, for all α, c and η ∈ (0, η_0]; |𝒩| ≥ n_−(a_T|L²(I_T))): PROVED.
- Prop 1 (S^low ≤ S ≤ S^{(J)}, S^{(J)} ↓ S): PROVED. Correction: the entries of the exact S are not absolutely convergent series (they contain A_𝒞𝒞^{−1}).
- Prop 2 (n_raw ≤ 2⌊2Tτ*/π⌋ + 1; d_min ≤ (2T/π)|{s_T<0}| ≤ (4T/π)τ*_T): PROVED. Prop 3 (n_raw ≥ 1 for T ≥ ½log2): PROVED.
- O(T) growth of the negative set: not proved; contradicted NUMERICAL (5, 9, 11, 11, 41, 125, ~685); superlinear lower bound OPEN.
- Lemma 3 (an entering contact is a gauge at first order): PROVED.
- Explicit block of dimension 11 at ½log5 + ε: NUMERICAL; equivalence PROVED, truth value OPEN in that form.
- Prop 4 (no criterion on the block samples alone decides the sign): PROVED in L²(I_T), ARGUED in P_T.
- Result: PIVOT (reduction without sign; the arithmetic moves from the dimension to the conditioning of A_𝒞𝒞).
- Countermodel: Prop 4 (abstract sequences equal on the block, ≥ η outside).
- Next step: bound ‖y_*(x)‖ and S − S^low in terms of η; lower bound of A_𝒞𝒞 at ½log5 + ε. Taken: yes, ROUND_002_A.

### 3. ROUND_001_D.md — moment criteria of the representing measure of B
- Object: B(d) = a(F_0, V_dF_0), B = μ̂ under (★); moments/germ of B at 0.
- Prop 1 (for |d| < log2 − 2T_0 the comb part of B vanishes; all existing moments are comb-free): PROVED.
- Prop 2 (no criterion using only the germ or the moments decides the sign; falsifiers cΛ, a_P): PROVED given the CITED falsifiers.
- Result: NO-GO (class: criteria depending only on the germ of B at 0 / moments of μ). Determinacy of the moment problem: not decided, irrelevant.
- Next step: none.

### 4. ROUND_002_A.md — coercivity floor of the complement, Schur inequality with floor, near-coincidences on the mesh
- Object: A_𝒞𝒞 = ½(D_e + HᵀD_oH) compressed to 𝒞; levels W_t; matrices G_t = [h_{l−j}].
- NUMERICAL correction of ROUND_001_C §4: the sample 8.8·10⁻⁵ is k = 18 at the edge of the gauge interval; the modes 2^b ≈ 3^a are not shallow (values of order 1).
- Lemma P (two projections: ‖Px‖² + ‖Qx‖² ≤ (1 + ‖PQ‖)‖x‖²): PROVED.
- Thm F (floor c_floor = ½∫_0^∞(2 − ν_t)dt ≥ c_*, by the angle between even/odd shallow subspaces): PROVED. Cor F1 (Schur test version): PROVED.
- Prop S (finite sufficient inequality (I_c): a_T(x) ≥ c^{−1}‖P_𝒞Ax‖²): PROVED. Prop L (the best member is c = λ_min(A_𝒞𝒞); requires margin S(x) ≥ ⟨b,(C^{−1} − A_𝒞𝒞^{−1})b⟩): PROVED.
- NO-GO (class: floor-only Schur inequalities, A_𝒞𝒞^{−1} replaced by a scalar): mechanism PROVED, failure NUMERICAL (c_need = 2.10 > 1.11 at ½log5+ε; 3.54 vs 1.02 at T = 1).
- Prop M (sample identity: s_k = m + r_T − A_T + c(−1)^k + 2Σv_n sin²(πk log n/4T)); Cor M1, M2 (deep sample ⟹ n′^{q_n} ≈ n^{q_{n′}}): PROVED. Cor M3 (quantitative separation of shallow samples of opposite parity): ARGUED.
- Reusable positives: Lemma P (general); Thm F (every comb, every gauge); Prop M and Cor M1–M2 (every weight v_n ≥ 0).
- Next step: finite-rank + scalar lower bound of A_𝒞𝒞 (R ⊕ c_floor on the space of coupling vectors). Taken: not directly; ROUND_005_C enlarged the block with comb responses and checked that the floor class gets worse.

### 5. ROUND_002_B.md — the O(1) term Q₁ of the exterior form in the prolate sector
- Object: 𝔔^w with arbitrary comb w, W = w∗1; sector span{ψ_4,…,ψ_{4K}}; 𝒩^w = log N·𝐓₀ + Q₁(w) + o(1).
- Lemma 1.1 (exact identity 𝒫_w = Σ(mn)^{−1/2}(W(m)+W(n))⟨u_m,u_n⟩): PROVED.
- Prop 1.2 (𝒫_w = 𝒟_w + 𝒪_w; 𝒟_w = 2∫H₁^w|ϱ|² ≥ 0 monotone; ℬ_n indefinite; 𝔔^w affine in W, without products of weights): PROVED.
- Thm 2.1 (coherent comb matrix on the sector PSD and monotone for all N, K): PROVED.
- Thm 2.2 (limit Σ_n (W(n)/n)𝐆(n), 𝐆(n) Toeplitz PSD): ARGUED (relative prolate phase).
- Prop 2.3 (incoherent part O(N^{−1/2}log N)): ARGUED. §2.4 expansion: ARGUED; 𝐓₀ ⪰ I PROVED in coherent form (correction to the earlier Γ-limit: the leading term is log N·𝐓₀, not ‖b‖²).
- Thm 3.1 (Q₁ non-increasing in w): PROVED for the coherent part, CONDITIONAL for Q₁.
- NO-GO (class: comb dependence of the exterior form in the prolate sector, monotone and linear bounded in the weights): survives cΛ (c < 1), a_P, Beurling, finite modifications.
- Reading: «localize and then sign in the sector» is circular; all the specificity of Λ is in (ext-L).
- Next step: restrict 𝒪_Λ to the gauge quotient of PW_N at bounded Mellin frequency (Legendre block) and decide whether Σ_n log n·ℬ_n has a sign pattern that fails for c·log and W_{a_P}. Taken: no (never carried out in the range).

### 6. ROUND_002_D.md — three candidates by reverse engineering; archimedean floor on the null cone of the comb
- Object: joint range W_T = {(Π(F), Arch(F))}; Θ_T = inf{Arch(F) : F ∈ S_T, Π(F) = 0}; Φ_T(c) = λ_A(T; cΛ); J_T = {c : Φ_T(c) ≥ 0}.
- Thm 1 (W_T convex; Π takes both signs; max_c Φ_T = Θ_T; J_T a closed bounded interval, empty ⟺ Θ_T < 0; (★)_T ⟺ Θ_T ≥ 0 ∧ 1 ∈ J_T; Θ_T invariant under cΛ; empty comb: Θ_T = λ_arch(T)): PROVED.
- Cor 2 (for T ≥ 0.60 and empty comb, Θ_T < 0): PROVED. Cor 3 (λ_A ≥ Θ_T − |1 − c*_T|π_T): PROVED (claim on Π(F*) = 0 corrected in ROUND_002_E).
- Candidate II (Schur coupling of metric δ = log(lcm/gcd) vs ρ): defined, falsifiers ARGUED. Candidate III (signed Lévy measure): recorded as dominated by I.
- Remainder: (I.a) Θ_T ≥ 0 is blind to c (D_∃c); (I.b) is (★). Cor 3(b) loses π_T: estimate with slack.
- Reusable positives: Thm 1 complete (every comb with positive weights and T > ½log2).
- Next step: compute Θ_T at ½log5 + ε and T = 1, test a_P and Λ + η1_2. Taken: yes, ROUND_002_E. Candidate II: ROUND_003_B.

### 7. ROUND_002_E.md — Galerkin test of Θ_T against falsifiers
- Object: Θ_T(w) for weight vectors w at fixed positions; 𝒦_T = {w : Ψ_T(w) ≥ 0}.
- Lemma 1 (Π_w takes both signs for all w ≠ 0): PROVED. Lemma 2 (𝒦_T convex compact; Θ_T(w) ≥ 0 ⟺ ℝw ∩ 𝒦_T ≠ ∅): PROVED.
- Lemma 3 / Cor 4 (Lipschitz persistence Θ_T(w′) ≥ Θ_T(w) − |c*|‖w − w′‖₁; (I.a) can only fail under small modifications where Θ_T(Λ) = 0): PROVED.
- Correction of ROUND_002_D Cor 3: c*_T = 1 ⟺ 0 in the range of Π on the bottom eigenspace (Danskin, CITED): PROVED.
- Remark: Θ_T is not monotone under deletion: ARGUED.
- NUMERICAL: Θ_T < 0 (rigorous up to rounding) for deletions of 2, of 3, swap, shift 3 → 3.2 and modifications of both signs at T = 0.9; at T = log 2 (Θ ≈ 6.5·10⁻⁵ > 0) several survive.
- Result: PIVOT (the candidate only separates at tangency windows, where Θ_T = λ_A: it is not weaker than (★)).
- OPEN lemma: inf{Arch(F) : F ∈ P_T, ‖F‖ = 1, Σ v_n Re c_F(log n) = 0} ≥ 0 at T = 1.
- Next step: confirm tangency at T = 1 and identify the two-dimensional bottom eigenspace where Π changes sign. Taken: yes, ROUND_003_A.

### 8. ROUND_003_A.md — the near-null pair of a_T in P_T: parity, anchoring, rigidity
- Object: bottom eigenvectors of a_T by parity sector; Π-Gram matrices M_par.
- Prop 1 (P_T = P_T^ev ⊕ P_T^odd orthogonal for L², Arch and Π; λ_A and Φ_T are minima by sector): PROVED.
- Prop 2 (tangency c*_T = 1 ⟺ 0 ∈ convex hull of Π on the sector bottoms; three-case criterion): PROVED (Kato–Danskin CITED).
- Lemma 3 (Weyl anchoring: an orthonormal pair with indefinite Π fixes Θ_T ∈ [λ_A, Λ_2] and |1 − c*_T| ≤ (Λ_2 − λ_A)/min|μ_±|): PROVED.
- Lemma 4 (rigidity: a near-kernel S of a_T bounds λ_A and Θ of every comb modified by ε − λ_max(Π_δ|_S)): PROVED.
- Simplicity of the bottom / λ_ev ≠ λ_odd: OPEN. Conjectures (C1) Π indefinite on the even pair for T > 0.61, (C2) λ_ev,2 decays faster than every exponential, (C3) bottom even and simple: OPEN with NUMERICAL support.
- NUMERICAL: the pair of ROUND_002_E is even+odd with definite Π; the anchoring pair is {e_ev,1, e_ev,2}; the earlier comb generator omitted n = 7 for T > ½log7.
- Remainder: 2×2 inequality Σ v_n R_n(S) ⪯ Arch_S circular (S depends on Λ); saturated to 18 digits.
- Reusable positives: Prop 1, Prop 2, Lemma 3, Lemma 4 (every weight vector).
- Next step: test whether Π is indefinite on the plane of the two bottom eigenvectors of Arch in P_T^ev (Λ-free plane) and write the 2×2 Schur complement. Taken: yes, ROUND_004_A (fails: does not capture the pair).

### 9. ROUND_003_B.md — candidate II decided: Schur coupling of the two metrics of ℕ
- Object: 𝔸_M = 𝕏_M ∘ 𝕂_t + ℝ_M, 𝕂_t = [e^{−tδ}] = [(gcd²/mk)^t] ⪰ 0.
- Prop 1 (existence of the decomposition ⟺ 𝔸_M ⪰ 0): PROVED (reformulation).
- Lemma 2 (entrywise cage |𝔸 − ℝ|_{mk} ≤ βe^{−tδ(m,k)}): PROVED.
- Thm 3 (division prescription 𝕏 = (𝔸 − diag r) ∘ 𝕂_t^{∘(−1)} never PSD for all M; 2×2 minor on {k, k+1}): PROVED.
- Thm 4 (Div/Near prescription leaves ℝ with zero diagonal ≠ 0, never PSD for M ≥ 4): PROVED.
- Prop 5 (𝔸_M ∘ 𝕂_t ⪰ 0 on [t*_M, ∞); (★) ⟺ t*_M = 0 ∀M; t*_M < ∞ for every comb): PROVED.
- Result: NO-GO (class: Schur factorizations by 𝕂_t = [e^{−tδ}] and dual suppression 𝔸_M ∘ 𝕂_t).
- Reopening condition: a multiplier that does not preserve PSD under Schur alone and that is large (not small) on near-coincident pairs.
- Next step: close in the index. Taken: not applicable (recording action).

### 10. ROUND_004_A.md — Λ-free archimedean planes: k × k necessary conditions
- Object: E_k = span of the k bottom eigenvectors of Arch in P_T^ev; R_n(E)_{ij} = symmetrized cross-correlation at log n.
- Prop 1 ((C_k) necessary; for k = 2: (L1), (L2) linear and (Q) quadratic with mixed discriminants ½D(R_m,R_n)): PROVED.
- Lemma A (‖R_n(E)‖ ≤ λ_max(G_E(log n)) ≤ 1; boundary decay (2T − log n)²; Lipschitz; R(0) = I): PROVED.
- Prop B (a finite Λ-free subspace with slack ε_E > 0 tolerates every weight perturbation of ℓ¹ size < ε_E, cΛ with |c−1|‖Π|_E‖ < ε_E and small shifts): PROVED → NO-GO (class: necessary conditions a_T|_E ⪰ 0 on a fixed finite Λ-free E, at fixed T, as a sign step).
- §5 family uniform in T: must have dim ≥ N*(T) and carry Λ-dependent information at precision e^{−15.449T}: ARGUED; not excluded in principle.
- NUMERICAL: (C_k) holds at log2, ½log5, 0.9, 1.0, 1.2 (k = 2,3,4,6); E_2 does not capture the anchored pair beyond T ≈ 0.7; the 2×2 condition lets through cΛ with c > 1 and Λ + 0.1·1_2.
- Reusable positives: Prop 1, Lemma A (every finite E ⊂ P_T^ev).
- Next step: compute BC^{−1}Bᵀ for E_k at T = 1.0, 1.2 and its decay in k. Taken: yes, ROUND_005_B §4 (κ(E_k) decays one decade per unit of k, not like α_{k+1}^{−1}‖B‖²).

### 11. ROUND_005_A.md — Krylov family of the comb from the archimedean negative cone
- Object: K_j = span{Π_P^i e : e ∈ 𝒩_T, i < j}; S_x = Qc_xQ truncated shift.
- Lemma 2.1 (explicit negative cone Σ_T of dim ≥ ⌈2Tt_1/π⌉ − 3): PROVED. Lemma 2.2 (𝒟_T ∩ L^∞ ∩ P_T invariant under Π_P): PROVED; for the spectral cone CONDITIONAL (H_b).
- Prop 3.1 (entries are polynomials of degree ≤ 2j − 1 in v with coefficients K at u − log r, r ∈ ℚ_{>0}): PROVED.
- Lemma 3.2 (shifts in the same direction compose exactly; opposite directions produce leakage slabs): PROVED.
- Prop 3.3 (Π² = Qσ_v²Q − 𝔏*𝔏: [Λ∗Λ indefinite] + [mean value of Dirichlet polynomial ≥ 0] − [leakage ≤ 0]): PROVED.
- Prop 3.4 (degree 3: classes W_3(r) ≥ 0, r = mn/k; near-coincidences work against the inequality): PROVED.
- Prop 3.5 (K_j(cΛ) = K_j(Λ) as sets; cΛ acts only through the frame): PROVED.
- Thm 4.1 (form-level Schur complement for finite K ⊂ 𝒟_T): PROVED. Prop 4.2 (coupling of K_1 only through responses f_α; G = (Π_P²)_ee − Π_ee² ⪰ 0; explicit matrix on K_2; halo/leakage commutator): PROVED (halo constant corrected to ½ in ROUND_006_B). Cor 4.3 (exact reduction at j = 1): PROVED.
- (SL_1), (SL_2), (SL_2^{sc}) ⟺ H_2 + Δ ⪰ 0 (identity PROVED; remainder inequality OPEN without mechanism).
- NO-GO (class: Krylov family of the comb from the archimedean negative cone with bounded j as sign carrier): mechanism PROVED, evidence NUMERICAL; restatement if j grows with the section.
- Result: PIVOT (change generator).
- Reusable positives: Lemma 3.2, Prop 3.3, 3.4, Thm 4.1 (general for any comb with weights ≥ 0).
- Next step: mixed family K̃_j of words in {M, Π_P} or with halo/leakage operators. Taken: yes, ROUND_006_B (closed NO-GO).

### 12. ROUND_005_B.md — Krylov family of the comb (variant with both parities)
- Object: Neg_T, K_j = span{(PΠP)^i e}, comparison with E_k (both parities).
- Prop 1.1 (⟨e, Π²e′⟩ and ⟨e, ΠPΠe′⟩ as double sums over quotients n/m and products mn < e^{2T}): PROVED. Prop 1.2 (polynomial structure of the generating system): PROVED. Schur identity: standard.
- NO-GO NUMERICAL (not a theorem): K_j does not capture the minimizer with dim O(T) (nor up to 64 of 78 at T = 1.4); complement never coercive (c(K_j) ≈ λ_2); does not detect 1.1Λ nor Λ + 0.1·1_2, which E_4 does.
- NUMERICAL: κ(E_k) decays one decade per unit of k; c(E_k) is O(1) only when k exceeds dim U_low = 2, 4, 6, 9, 16, 26.
- Next step: generate from the sand band K′_j; before that, recompute T ≥ 1.0 in extended precision. Taken: the band, yes (ROUND_005_E); extended precision, no (ROUND_005_E explains why it would not settle anything).

### 13. ROUND_005_C.md — family of comb responses on the negative Nyquist block
- Object: V_T = P_𝒞Π(𝒩_η + 𝒯), E_T = N′ ⊕ V_T, dim ≤ 2|𝒩| + 2; samples C_q, m_q, s_q; budget a_T = σ_T‖F‖² + κ(F) − ℛ(F).
- Prop 2 (responses = Dirichlet polynomials twisted by Λ on the mesh: Πφ_q = φ_qψ_q): PROVED. Prop 2′ (pole-free fluctuation form): PROVED.
- Lemma 1 (Tate gauge g_q = (−1)^q 2sinh T/(¼+ω_q²); (L2′) holds with two gauges): PROVED.
- Prop 3 (budget σ_T + κ − ℛ and its form on the mesh): PROVED (window version of a recorded identity).
- Thm 2 (exact reduction on E_T; the block couples to the complement only via Arch): PROVED (with the Tate responses included).
- Prop 4 (entries of degree ≤ 3 in v), Prop 5 (products and quotients that appear), Lemma 6 (falsifiers; family invariant under ϑΛ for |ϑ − 1| < δ_T): PROVED.
- NO-GO (NUMERICAL, logic PROVED): floor-only Schur certificates over every enlargement of the block (c_need 2.5–8.9 vs λ_min(C) ≈ 1.3); sign mechanisms based on comb identities (Λ∗1 = log, Selberg-type identity Λ_2 = Λlog + Λ∗Λ, local Euler factors, Lévy kernel identity) on E_T (Beurling 3 → 3.2 and a_3 survive, where (SL_T) fails by 0.24 and 0.51).
- Result: PIVOT; (SL′_T) ℛ ≤ κ − |σ_T| on E_T, exact to 5·10⁻¹⁰ / 10⁻¹⁵, fails for every falsifier with the value of λ_A(T; w).
- R4 status: proved dimension of the order of the sand; escape only NUMERICAL (OPEN).
- Reusable positives: Lemma 1, Prop 2, 2′, 3, Thm 2, Props 4–5 (every weight vector and positions).
- Next step: locate the crossing T_× of 𝒦_T(F*_T) and write ℛ ≤ 𝒦 on E_{T_×}. Taken: yes, ROUND_007_B (withdrawn: NO-GO).

### 14. ROUND_005_D.md — window form as a jump Dirichlet form; ground-state representation
- Object: μ_T = K du + Σ v_nδ_{log n}; a_T = (C_0 − A_T)‖F‖² + 𝔈_μ(F); ground state h_T of the complete form in L²(I_T).
- Lemma 1.1 (decomposition and jump/killing kernel form κ): PROVED. Prop 1.2 (i)–(iv) CITED; (v) h_T even, (vi) λ_A > μ_0, λ_A ≤ μ_2, (vii) non-separability: PROVED.
- Thm 2.1 (ground-state representation without residual killing term): PROVED. Cor 2.2 ((★) ⟺ weighted Poincaré inequality Q_h(φ) ≥ |μ_0|‖φ‖²_{h²} on φ ⊥ {e^{±t/2}/h}): PROVED.
- Thm 3.1 (rank-one reduction by sector; (★)_par ⟺ W_par(0) ≤ 0 if n₋ = 1): PROVED (= recorded polar capacity). Cor 3.2 (μ_1 − λ_A = τ_1²/D; interlacing λ_A ≤ μ_1 ≤ λ_{A,2}): PROVED. Cor 3.3 (sufficient condition cos²∠(h_T, χ) ≥ |μ_0|/g_1): PROVED; fails NUMERICAL by 0.2–0.5 %.
- Prop 4.2 (a_Tχ_+ = χ_+ω_+ with explicit ω_+ containing ψ(e^{T−t}) and Σ_{n<e^{T+t}}Λ(n)/n): PROVED, validated to 6·10⁻⁹.
- Thm 6.1 (NO-GO, class 𝒦_gap: lower bounds of the spectral gap with intrinsic loss — isoperimetry, Lyapunov functions, coupling, curvature-dimension, supersolutions): PROVED modulo the NUMERICAL size of the slack (≤ 4·10⁻⁸ at log 2, ≤ 10⁻¹² at ½log5).
- Monotonicity and log-concavity of h_T: OPEN (NUMERICAL: not monotone). Boundary speed: OPEN.
- NUMERICAL: W_ev(0) = −½, W_odd(0) = +½ to 5–6 digits in 17 windows of [0.60, 1.00] (𝔊_T ≈ 0); low null cluster for Tate at the order of its eigenvalues.
- Sign lemma (exact, OPEN): g_1^{ev} ≥ |μ_0^{ev}| + τ_1²/D and μ_0^{odd} ≥ 0.
- Reusable positives: Lemma 1.1, Thm 2.1, Cor 2.2, Thm 3.1, Cor 3.2, Prop 4.2 (every positive comb; 4.2 with exact Λ in ω_+).
- Next step: prove or refute y_T = a_T^{−1}χ_ev with explicit ‖y_T‖ ≤ C(T) (ansatz y = χ_+ν, L_+ν = 1). Taken: no.

### 15. ROUND_005_E.md — Krylov family from the sand band
- Object: Band(t) = eigenvectors of Arch_T with eigenvalue ≤ t, t ∈ {A_T, λ_max(Π_T)}; K′_j(t); cluster U_δ, m_δ.
- Lemma 3.0 (π_± ≤ A_T): PROVED. Thm 3.1 (two-sided Weyl count N_Arch(δ − π_−) ≤ m_δ ≤ N_Arch(δ + π_+) ≤ N_Arch(δ + A_T)): PROVED. Prop 3.2 (lower bounds by pointwise comparison are zero if π_− > δ − α_1): PROVED.
- NUMERICAL: the band at A_T saturates the Galerkin space; the sharp band captures the cluster at j = 1 with coercive complement (c ≈ 0.4–0.62); j = 2 saves no dimension relative to E_k; m_{10⁻³} ≈ 0.15e^{4T}; λ_max(Π_T)/A_T decreasing (Galerkin values, corrected in ROUND_006_A).
- Result: PIVOT. The sharp band is E_{n_P}, dependent on Λ only through a scalar: Prop B of ROUND_004_A applies.
- Asymptotic growth of λ_max(Π_T) relative to A_T: OPEN (settled in ROUND_006_A).
- Next step: bound λ_max(Π_T) ≤ A_T − loss and decide whether λ_max/A_T → 0. Taken: yes, ROUND_006_A (does not tend to 0).

### 16. ROUND_006_A.md — size of the comb form: λ_max(Π_T) versus A_T
- Object: π_±(H) for H = L²(I_T), P_T; V(s) = Σ_{u_n ≤ s} v_n.
- Lemma 1.0 (|Π_T(F)| ≤ Π_T(|F|)): PROVED. Thm 1 (π_±(P_T) = π_±(L²(I_T)), by modulated packets and simultaneous approximation): PROVED. Correction: the values of ROUND_005_E are Galerkin values.
- Thm 2 (π_+ ≤ ½max_s[V(s)+V(2T−s)] ≤ ½(A_T+V(T))): PROVED; Cor 2.1 (limsup π_+/A_T ≤ ½): PROVED with Chebyshev-type bounds CITED.
- (HT_T) head-tail Σ_{n≤a}v_n ≤ Σ_{X/a<n<X}v_n ∀a ≤ √X: OPEN.
- Thm 3 (π_+ ≥ N_T/(sinh T + T), exact arithmetic expression): PROVED; Cor 3.1 (liminf ≥ ¼): PROVED given the prime number theorem CITED. Exact constant in [¼, ½]: OPEN.
- Thm 4 (in P_T the density part of the comb is −∫(u_F′² + ¼u_F²) ≤ 0): PROVED.
- Lemma 5.1 (upper archimedean Weyl count N_Arch(s) ≤ 12.92·T·e^s(s + 6.373)): PROVED. Thm 5 (m_δ ≤ exp(2e^T(1+o(1)))): PROVED.
- Thm 6 (NO-GO, class: Weyl bounds of the cluster from pointwise comparisons a_T ≥ Arch_T − θ; none goes below 2T·exp(e^T(1+o(1)))): PROVED given PNT.
- Failed: Gram/Toeplitz bound on shifted copies (circular).
- Reusable positives: Thm 1–5 (generic in the comb; Thm 4 density only).
- Next step: phase-space count via the joint symbol with uniform tail. Taken: yes, ROUND_006_C.

### 17. ROUND_006_B.md — family of mixed words of (M, Π_P)
- Object: 𝒲_j(𝒢; S) with 𝒢 ⊂ {M, Π_P, [M,Π_P], H_x, L_x}, S ∈ {𝒩_T, Band}.
- Lemma 2.1 (log-Sobolev scale 𝓗 invariant under all words; unconditional for sine seeds, (H_𝓗) for the spectral cone): PROVED / CONDITIONAL.
- Prop 4.1 (word families of v-homogeneous generators from a Λ-free seed are scale invariant as sets; cΛ acts only through the frame; Danskin rejection criterion): PROVED. Refutes the premise of ROUND_005_A.
- Prop 4.2 (the only inhomogeneous family is the Lanczos one; blind to a cluster of spread δ up to O(δ)): PROVED.
- Prop 4.3 (halo and leakage with constant ½; H_x* = L_x; [M_0, S_x] = L_x* − L_x): PROVED; correction to ROUND_005_A Prop 4.2(v).
- Prop 4.4 (3×3 matrix 𝔄_3 on {e, Π_Pe, [M,Π_P]e}; Arch(Πe) − α‖Πe‖² = ⟨Πe, Le⟩ − ⟨LΠe, e⟩ + polar): PROVED.
- (SL̃_3) holds NUMERICAL but never rejects c > 1 nor η > 0 (the bottom grows with c): it cannot be a sign step.
- NO-GO (class: finite families 𝒲_j(𝒢; S) from a Λ-free seed with v-homogeneous generators, at small dimension relative to the capture dimension of the cluster; and Lanczos families with an inhomogeneous generator while the cluster is not resolved): mechanism PROVED, confirmation NUMERICAL. Closes LEDGER C13.
- Reusable positives: Prop 4.1, 4.2, 4.3 (every comb).
- Next step: exact Schur complement on the sharp band, Neumann expansion of the resolvent and degree at which it rejects 1.01Λ and Λ + 0.1·1_2 at T = 0.9. Taken: no (in the range).

### 18. ROUND_006_C.md — count of the cluster via the joint symbol
- Object: s_T = m − M_T, q_T; m_δ, m_δ^{L²}; P(τ) = Σ v_n n^{iτ}; S_T = Σ_p a_p².
- Lemma 1.1 (exact averaging at scale 1/T does not change q_T and fixes the comb: M̃_T = M_T): PROVED.
- Thm A (m_δ ≤ (T/(πη))∫(δ+η−s_T)_+ ≤ (T/(πη))(δ+η−s_min)|{s_T < δ+η}|): PROVED. Cor A.1, A.2 (sand scale exp(4e^T)): PROVED.
- Lemma B.0 (torus model: Σb_m² = E|𝒫|^{2k} ≤ (2k)!(eS_T/k)^k; uses unique factorization): PROVED. Thm B (uniform large values |{τ ≤ Ω : M_T > s}| ≤ (Ω + 3π(X^k+1))e√(2k)(4kS_T/(es²))^k): PROVED (mean value theorem CITED). Obs B.1 (Gaussian tail as Bohr density without rate): PROVED. S_T = 8T²(1+o(1)): PROVED given Mertens.
- Cor C, Cor D (m_δ ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T))): PROVED given PNT and Mertens.
- Limit of the class «Thm A + large values with error controlled by the spacing of {log m : m ≤ X^k}»: ARGUED; does not go below exp(2e^T(1+o(1))).
- Thm B is specific to ℕ (unique factorization and spacing 1/(m+1)), but it is a size statement, not a sign statement.
- Next step: bound the multiplicative energy 𝒩_k(ν) of k-th products of N_T near ratio 1 (θ < 1 gives exp((4 − 2/θ)e^T); a window independent of k gives exp(O(T²))). Taken: no.

### 19. ROUND_007_B.md — the sign budget disassembled
- Object: a_T = σ_T‖F‖² + κ(F) − ℛ(F) on P_T; ℛ = Π + 𝔢; (SL′_T) on E_T.
- Lemma 1.1 (σ_T = C_0 + 4 + ∫_{2T}^∞K_1, C_0 + 4 = 4 − γ − π/2 − log(8π); decreasing, convex, σ_T < 0 ⟺ T > T_0 = 0.052): PROVED (T_0 a NUMERICAL root). Correction: write −σ_T, not |σ_T|.
- Prop 1.2 (σ_T‖F‖² + κ(F) = 𝔞^♯(F), pole-free form of P46, independent of T, ≥ Arch): PROVED.
- Lemma 1.3 (every real F ∈ P_T changes sign ≥ 2 times; Tate anchoring |F̂(τ)|² ≤ d_T(τ)‖F‖², d_T(0) = T⁵/360 + O(T⁷); counting bounds): PROVED.
- Prop 1.4 (ℛ = Π + 𝔢; 𝒮_q = (1 − (−1)^q e^T)/(¼+ω_q²)): PROVED/CITED. Cor 1.5 (four equivalent forms of the sign lemma, the last Π ≤ Arch on E_T; form in G ∈ H²_0): PROVED.
- Lemma 2.1 (a single form on the nested family P_T): PROVED. Lemma 2.2 (continuity of the pieces on the minimizer): PROVED under simplicity (a hypothesis invisible at any attainable precision).
- Prop 2.4 (accounting theorem: the «carrier role» and the crossing depend on the chosen density ν): PROVED.
- Prop 3.1 (explicit cubic of a response with window cutoffs): PROVED. Cor 3.2 (classes m ≈ nk, mn ≈ k, mnk ≈ 1; thresholds ½log5, ½log7, ½log8, ½log9; weights (2T − log max(m,nk))_+): PROVED.
- NO-GO (i) (class: values of forms on F*_T, in particular locating T_×): accounting PROVED, near-null ladder NUMERICAL; withdraws the next step of ROUND_005_C.
- NO-GO (ii) (class: signing a subpart of ℛ or of a_T on E_T — a degree, a coincidence class, the exact part or the local-factor part — with error not ≤ λ_A): logic PROVED; the three degree parts (+1.4·10⁻³, −2.8·10⁻³, +1.4·10⁻³) cancel to 3·10⁻¹².
- Exact remainder OPEN: Π(F) ≤ Arch(F) for every unit F in E_T.
- Reusable positives: Lemma 1.1, Prop 1.2, Lemma 1.3, Prop 1.4, Cor 1.5, Lemma 2.1, Prop 2.4, Prop 3.1, Cor 3.2.
- Next step: one-sided variation formula of λ_A(T) at an entry threshold T_e ∈ {½log7, ½log8, ½log9}. Taken: no (outside the range).

---------------------------------------------------------------------------------------------------

## A. Deduplicated «do not retry» list (with reopening condition) and cross-check with RULES_AVOID.md

Marks: [ABSENT] not in RULES_AVOID.md; [INACCURATE] present with a different statement; [OK] present.

A1. Exterior form as a source of sign: half-line identity, defect for cΛ/a_P, cell cancellation,
    prolate sector Q₁ (comb-monotone, linear bounded). Reopening: a non-monotone comb term of order 1;
    the only candidate pointed out is 𝒪_w at low Mellin frequency (never carried out). (001_B, 002_B) [OK in C1:
    «L♯ programme (exterior form, …)»; the monotonicity result for Q₁ and the circularity
    «localize and then sign» are not mentioned.]
A2. Residue «layer edges κ_{T+log n}»: empty (a single flat boundary; archimedean-only terms). (001_B) [ABSENT
    as such; C1 says «exterior table of phase 202» without this closure.]
A3. Fused reading of the exterior form as an object satisfying clause (5): it is ζ with a Möbius mollifier.
    (001_B) [ABSENT; RULES_AVOID F lists clause (5) as not excluded without this warning.]
A4. Criteria on the Nyquist block samples alone (Prop 4 of 001_C); dimension count of the block as
    sign carrier. Reopening: none; every criterion must involve A_𝒞𝒞^{−1}. [ABSENT; C1 mentions «two
    Nyquist sectors as source of sign» in general.]
A5. Germ of B at 0 / moments of the representing measure. (001_D) [OK: C1 «Carleman germ criteria».]
A6. Floor-only Schur inequalities (I_c), on the minimal block and on every enlargement by responses.
    Reopening: a finite-rank plus scalar lower bound of A_𝒞𝒞 that follows the alignment of b = P_𝒞Ax with the
    spectrum (proposed in 002_A, not carried out). (002_A, 005_C) [ABSENT.]
A7. Archimedean floor on the null cone of the comb Θ_T as a sign step: blind to c; only separates at tangency
    windows, where Θ_T = λ_A. (002_D, 002_E) [INACCURATE: B10 of RULES_AVOID says «Concavity in the comb
    (Danskin) gives only upper bounds while the dual representation of Θ_T is missing; with it, it is not closed».
    The dual representation exists (002_D Thm 1, PROVED) and 002_E shows that Θ_T(w) ≥ 0 survives every modification
    of ℓ¹ size < Θ_T(Λ)/|c*| where Θ_T(Λ) > 0 (Cor 4): the correct status is PIVOT, «not weaker than (★) where it
    separates».]
A8. Schur coupling of the metrics ρ and δ = log(lcm/gcd) by 𝕂_t = [e^{−tδ}], and suppression 𝔸_M ∘ 𝕂_t.
    Reopening: a kernel that does not preserve PSD under Schur alone and is large on near-coincident pairs. (003_B)
    [ABSENT.]
A9. Necessary conditions a_T|_E ⪰ 0 on a fixed finite Λ-free subspace (planes E_k, sharp band E_{n_P})
    used as a sign step. Reopening: a family with dim E_T → ∞ carrying Λ-dependent information at
    precision λ_A. (004_A Prop B, 005_E) [Partial OK: D17 «Λ-free planes E_k»; missing the general form of Prop B
    (every fixed finite Λ-free E, including the sharp band).]
A10. Krylov families of the comb from the archimedean negative cone (bounded j); word families of
     v-homogeneous generators from a Λ-free seed; Lanczos families of A while the cluster is not
     resolved. Reopening: none within the class; the sign must go to the exact Schur complement on the
     captured band. (005_A, 005_B, 006_B) [OK: D17 «Krylov and word families of (M, Π) at bounded degree or
     homogeneous»; C1 «homogeneous word families of (M,Π)». The Lanczos part (Prop 4.2 of 006_B) is missing.]
A11. Krylov from the sand band with threshold A_T (saturates) or with j = 2 as a dimension saving. (005_E) [ABSENT.]
A12. Sign mechanisms for (SL_T) built with identities valid in every Beurling system or in a_P
     (Λ∗1 = log, Λ_2 = Λlog + Λ∗Λ, generalized identities, bounds on local Euler factors, Lévy
     kernel identity) on E_T. (005_C) [OK in essence: B1 and B7; the family E_T is not named.]
A13. Class 𝒦_gap: lower bounds of the spectral gap of the ground-state-transformed form with
     intrinsic loss (isoperimetry, Lyapunov, coupling, curvature-dimension, supersolutions). Reopening:
     none (the inequality is an equality to 10⁻⁸–10⁻¹⁵). (005_D) [INACCURATE/partial: C1 lists «Markov, maximum
     principle» and «Bakry–Émery Γ₂», not the class 𝒦_gap with the ground-state representation of the complete
     form with the comb.]
A14. Weyl bounds of the cluster by pointwise comparison a_T ≥ Arch_T − θ (θ ≥ π_+ ≥ e^T(1+o(1))); assuming
     λ_max(Π_T)/A_T → 0. (006_A) [ABSENT.]
A15. Gram/Toeplitz bound of Π_T via the shifted copies (circular). (006_A) [ABSENT.]
A16. Gain by smoothing the comb at scale 1/(2T) (exact, zero). (006_C) [ABSENT.]
A17. Count by Thm A + large values with error controlled by the trivial spacing of {log m}: does not go below
     exp(2e^T(1+o(1))) (ARGUED). Reopening: multiplicative energy of k-th products beyond the trivial
     spacing. (006_C) [ABSENT.]
A18. Values of forms on «the minimizer» F*_T; locating the crossing window T_×; «carrier
     role» claims (they depend on the density ν and on the near-null ladder). (007_B §4.3) [ABSENT.]
A19. Signing a subpart of ℛ or of a_T on E_T (a degree, a coincidence class, the exact-coincidence
     part, local factors) with error larger than λ_A. (007_B §3.4) [ABSENT as a class; B2 of RULES_AVOID
     covers estimates with slack in general.]
A20. Anchoring the sign on the 3×3 condition (SL̃_3) or on (SL_2^{sc}) over {e, Π_Pe, [M,Π_P]e}: comb-monotone at the
     bottom, never rejects c > 1. (006_B §4.4) [ABSENT.]

Total: 20 items. Absent 13 (A2, A3, A4, A6, A8, A11, A14, A15, A16, A17, A18, A19, A20); inaccurate 2 (A7, A13);
present 5, of which with omissions A1, A9, A10, A12 and correct A5.

## B. PROVED positive results with exact scope

B1. Radical lemma and the half-line identity W_T(Ef) = 𝒲[Ψ_f] (001_B Thm 1.1, Cor 1.2): f admissible at T;
    only for Λ; proof without zeros with (I), (E), (F), ζ(0) = −½ and residue 1.
B2. Defect for an arbitrary comb and absence of a common radical vector for c ≠ 1 (001_B Prop 1.3, 1.4): w ≥ 0 with
    Dirichlet series convergent in σ > 1; F ∈ L², F = O(e^{3x/2}) at −∞, F = 0 on [T, ∞).
B3. Flat boundary, archimedean-only boundary terms, φ_0 enters through a scalar (001_B Lemma 2.1, Prop 2.2, 2.3):
    kernel data of the exterior form, N ∉ ℤ for the C¹ part.
B4. Shifted Nyquist identity with alternating gauge, reduction (L2′) and its dimension bounds (001_C Lemma 1–3,
    Thm 1, Prop 1–3): every T, α, c, η ∈ (0, η_0]; every comb with weights ≥ 0.
B5. Two-projection lemma and coercivity floor c_floor (002_A Lemma P, Thm F, Cor F1): complement 𝒞 of the block,
    every gauge, every comb.
B6. Sample identity and near-coincidences on the mesh (002_A Prop M, Cor M1–M2): every k, every gauge, every
    weight.
B7. Convex joint range, max_c λ_A(T; cΛ) = Θ_T, J_T an interval, 𝒦_T convex compact, Lipschitz persistence,
    tangency criterion via the bottom eigenspace (002_D Thm 1, Cor 2–3; 002_E Lemmas 1–3, Cor 4, correction):
    T > ½log2; weights at fixed positions.
B8. Schur factorization by 𝕂_t ⟺ 𝔸_M ⪰ 0, entrywise cage, failure of the division and
    Div/Near prescriptions, half-line [t*_M, ∞) (003_B): every M, every t > 0, symmetric matrices with constant positive diagonal.
B9. Parity separation of a_T in P_T, tangency criterion, Weyl anchoring, near-kernel rigidity (003_A
    Prop 1–2, Lemma 3–4): every T; Lemma 4 for every modification vector δ.
B10. Explicit necessary conditions (C_k), bounds on R_n(E) and tolerance Prop B (004_A): E ⊂ P_T^ev (Lemma A) or
     E ⊂ P_T (Prop B) finite Λ-free, T fixed.
B11. Word algebra of truncated shifts; Π² = Qσ_v²Q − 𝔏*𝔏 (Λ∗Λ + mean value ≥ 0 − leakage); degree 3
     with classes W_3(r) ≥ 0; form-level Schur complement (005_A Lemma 3.2, Prop 3.3–3.5, Thm 4.1, Prop 4.2,
     Cor 4.3): L²(I_T), finite K ⊂ 𝒟_T ∩ P_T.
B12. Degree-2 formulas for ⟨e, Π²e′⟩, ⟨e, ΠPΠe′⟩ (005_B Prop 1.1–1.2): e, e′ ∈ L²(I_T).
B13. Comb responses as Dirichlet polynomials twisted by Λ on the mesh; Tate gauge; budget
     σ_T + κ − ℛ; exact reduction on E_T with archimedean-only coupling of the block; formulas for entries of
     degree ≤ 3 (005_C Lemma 1, Prop 2, 2′, 3, 4, 5, Thm 2, Lemma 6): every T, every weight and positions in (0, 2T).
B14. Jump Dirichlet form with the comb, exact ground-state representation, rank-one reduction,
     μ_1 − λ_A = τ_1²/D, interlacing, a_Tχ_+ = χ_+ω_+ (005_D Lemma 1.1, Thm 2.1, Cor 2.2, Thm 3.1, Cor 3.2–3.3,
     Prop 4.2): L²(I_T), every bounded Lipschitz φ (extension CITED); Prop 4.2 with exact Λ.
B15. Two-sided Weyl count m_δ (005_E Lemma 3.0, Thm 3.1, Prop 3.2): P_T and every Galerkin compression.
B16. π_±(P_T) = π_±(L²); ¼ ≤ liminf π_+/A_T ≤ limsup ≤ ½; comb density ≤ 0 in P_T; archimedean count
     N_Arch(s) ≤ 12.92Te^s(s+6.373); m_δ ≤ exp(2e^T(1+o(1))) (006_A Thm 1–5, Lemma 5.1): every T (asymptotic ones given PNT).
B17. Log-Sobolev scale invariant under words; scale invariance of homogeneous families; Lanczos blindness
     to clusters; halo/leakage with constant ½; matrix 𝔄_3 (006_B Lemma 2.1, Prop 4.1–4.4): P_T, seeds in 𝓗.
B18. Useless exact averaging; Landau-type count via the joint symbol; torus moments and uniform large
     values; m_δ ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T)) (006_C Lemma 1.1, Thm A, Lemma B.0, Thm B, Cor C–D):
     Thm A for every comb; Lemma B.0/Thm B use unique factorization and integer spacing (specific to ℕ).
B19. σ_T in closed form; σ_T‖·‖² + κ = 𝔞^♯ independent of T; Tate anchoring and nodes; ℛ = Π + 𝔢; four forms
     of the sign lemma; a single form on the nested family; accounting by density ν; explicit response cubic
     and entry thresholds (007_B Lemma 1.1, Prop 1.2, Lemma 1.3, Prop 1.4, Cor 1.5, Lemma 2.1, Prop 2.4,
     Prop 3.1, Cor 3.2): P_T, every T.

## C. Open obligations (precise statement and what was attempted)

C1. (L2′) at ½log5 + ε: S = A_{N′N′} − A_{N′𝒞}A_{𝒞𝒞}^{−1}A_{𝒞N′} ⪰ 0 on the block of dimension 11 with gauge 1.21–1.24.
    Attempted: scalar floor (002_A, fails), enlargement by responses (005_C, the floor class fails).
C2. Growth of the negative set of the mesh: superlinear lower bound of min_{α,c}#{s^{α,c}_k ≤ 0} and of
    n_−(a_T|L²(I_T)). Attempted: only upper bounds (001_C Prop 2) and numerics.
C3. Block a ≥ 2 of the lattice reduction of the exterior form: an inequality on 𝔊 that is neither a size bound
    nor a rewriting of 𝒲[g] (001_B §2.5). Nothing attempted beyond the remark.
C4. Q₁: O(1) term of the exterior form; incoherent part 𝒪_Λ at low Mellin frequency (002_B). Not attempted.
C5. Θ_T ≥ 0 at T = 1: inf{Arch(F) : F ∈ P_T, ‖F‖ = 1, Π(F) = 0} ≥ 0 (002_E). Attempted: Galerkin; reduced to
    tangency (003_A).
C6. Simplicity of the bottom of a_T in P_T and λ^a_ev(T) < λ^a_odd(T); (C1)–(C3) of 003_A. Attempted: there is no
    Perron–Frobenius in P_T.
C7. Remainder of (SL_2^{sc}): Δ_{22} ≥ ((1/2π)∫s_Tσ_v|ê|² + Δ_{12})²/((1/2π)∫s_T|ê|²) − (1/2π)∫s_Tσ_v²|ê|² (005_A §5.3).
    Attempted: products/quotients decomposition; no mechanism.
C8. (SL′_T) / Π(F) ≤ Arch(F) for all F ∈ E_T (005_C §5.2, 007_B §3.4): cubic inequality in (v_n) with 2|𝒩|+2
    unknowns (24 at ½log5 + ε, 84 at T = 1). Attempted: comb identities (NO-GO), subparts (NO-GO).
C9. Sign lemma of 005_D: g_1^{ev}(T) ≥ |μ_0^{ev}| + τ_1²/D(λ_A^{ev}) and μ_0^{odd} ≥ 0. Attempted: spectral gap
    tools (NO-GO 𝒦_gap).
C10. Uniform range of the Tate function: y_T = a_T^{−1}χ_ev ∈ L²(I_T) with explicit ‖y_T‖ ≤ C(T) (005_D). Not
     attempted.
C11. Monotonicity, log-concavity and boundary speed of h_T (005_D §4.3). Not attempted (numerics: not monotone).
C12. (HT_T) Σ_{n≤a}v_n ≤ Σ_{X/a<n<X}v_n for all 1 ≤ a ≤ √X and all T; exact constant of π_+/A_T in [¼, ½] (006_A).
     Not attempted.
C13. Phase-space count with uniform tail in R for M_T, or multiplicative energy 𝒩_k(ν) ≤ C^kΣb_m² for
     ν ≥ X^{−θk}, θ < 1 (006_C §7). Attempted: moments with mean value (cap exp(2e^T)).
C14. Exact Schur complement on the sharp band S_T = D_b − Π_bb − Π_bc(Arch_c − Π_cc)^{−1}Π_cb ⪰ 0 and Neumann
     degree at which it rejects 1.01Λ (006_B). Not attempted.
C15. One-sided variation formula dλ_A/dT⁺ at entry thresholds T_e (007_B §4.5). Not attempted.
C16. Family uniform in T with dim E_T ≥ N*(T) carrying the sign in its Schur complement at precision λ_A
     (004_A §5). Not excluded; not constructed.

## D. Objects, next steps or ideas named and never taken up (within the range)

D1. Block a ≥ 2 / signed correlation of Möbius means with Gram entries (001_B §2.5).
D2. 𝒪_Λ restricted to the gauge quotient of PW_N at bounded Mellin frequency; matrix in the Legendre basis (002_B).
D3. Finite-rank + scalar lower bound of A_𝒞𝒞 on the space of coupling vectors and modes W_{t_1}
    (002_A).
D4. Candidate III, signed Lévy measure / subordination between two infinitely divisible laws (002_D;
    recorded as dominated, not constructed).
D5. First test of candidate II with 𝔸_M ∘ [e^{tδ}] for M ≤ 12 and symbolic cases {1, p, q} (002_D): settled
    negatively in general by 003_B, without the symbolic cases.
D6. 2×2 inequality on the fixed plane of Arch with a «non-circular» Schur complement (003_A): carried out as a test in
    004_A, capture fails; the explicit 2×2 Schur complement was not written.
D7. Anchor with seed E_k (k ≥ 6) under a mixed generator (005_A, final alternative): not taken.
D8. Recompute T ≥ 1.0 in extended precision with high-precision Arch (005_B, 005_E): not taken.
D9. Range of the Tate function y_T = a_T^{−1}χ_ev, ansatz y = χ_+ν, L_+ν = 1 (005_D).
D10. Window crossing law and two-form inequality on N′ (005_C): withdrawn by 007_B.
D11. Phase-space count with a numerical Landau–Widom test in a high-frequency basis (006_A §7): replaced
     by Thm A of 006_C without the numerical test.
D12. Multiplicative energy 𝒩_k(ν) of products of N_T (006_C §7).
D13. Exact Schur complement on the sharp band, Neumann expansion, rejection degree (006_B).
D14. Variation formula of λ_A at entry thresholds (007_B).
D15. Index insertion: entries requested for 003_B, 005_D (𝒦_gap, Prop 4.2, values W_par(0) = ∓½), 007_B
     (P211-7B): recording actions, outside the scope of this reading.

## E. Coverage

Files in the range (order of `ls *.md | sort`): ROUND_001_B, ROUND_001_C, ROUND_001_D, ROUND_002_A, ROUND_002_B,
ROUND_002_D, ROUND_002_E, ROUND_003_A, ROUND_003_B, ROUND_004_A, ROUND_005_A, ROUND_005_B, ROUND_005_C, ROUND_005_D,
ROUND_005_E, ROUND_006_A, ROUND_006_B, ROUND_006_C, ROUND_007_B — 19 files, ≈ 470 KB. Read completely: 19 of 19.
There are no files ROUND_002_C, ROUND_004_B…, ROUND_006_D nor ROUND_007_A in the listing of the range. In addition,
`RULES_AVOID.md`, `OBJECT_SPEC.md` and `STATEMENT_001.md` were read for the cross-check. No file or stretch of the range was left
unread. The numerical scripts cited by the files (scratchpad) were not read.
