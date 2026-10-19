# R166_301 — The first-contact witness as a Toeplitz kernel element (Makarov–Poltoratski route)

Phase 166, after R166_190 (closure). Labels: PROVED / PROVED-CITED / ARGUED / OPEN.
Citations from memory are marked **[mem]**: Makarov–Poltoratski, *Meromorphic inner functions, Toeplitz kernels and the uncertainty principle* (2005) [MP05]; *Beurling–Malliavin theory for Toeplitz kernels*, Invent. Math. 182 (2010) [MP10]; Poltoratski, *Toeplitz approach to problems of the uncertainty principle*, CBMS 121 (2015) [P15]; Sarason, *Algebraic properties of truncated Toeplitz operators*, Oper. Matrices 1 (2007) [S07]; Câmara–Partington, truncated Toeplitz operators via equivalence after extension, JMAA ≈2016 [CP16]; Hartman–Wintner / Rosenblum: a self-adjoint Toeplitz operator on H² with nonconstant real symbol has no eigenvalues [HW].

Corpus check (grep "Toeplitz", "truncated Toeplitz", "Makarov", "Sarason" in phase-16-surf-witness-variety*, Paper 47). Already present: R164_101 §3(iii) (row D ⟺ the compression of −θ′_{X′} to PW_T is ⪰ 0); R160_PD_R1, R160_M7_R1 (truncated Wiener–Hopf with causal symbols, which is multiplicative and elementary); R161_045 (local Euler Toeplitz–Hankel square, which does not globalize). **No** Makarov–Poltoratski or kernel/argument formulation appears in the corpus. This memo is new as a route. Its outcome is negative, and the wall is named in §5.

## Status table

| # | Statement | Label |
|---|---|---|
| 1.1 | Contact ⟺ nontrivial kernel of the truncated (not ordinary) Toeplitz operator A_T on PW_T ≅ K_Θ, Θ=e^{2iTz}, symbol σ_T/2π plus rank-2 polar term; on the primitive subspace 𝒫_T it is ker A^𝒫_{σ_T} | PROVED |
| 1.2 | T_c = min{T : ker A_T ≠ 0}, given λ_min > 0 for small T | PROVED (from monotonicity + continuity of λ_min, R163_401/Paper 47 lem:contA) |
| 1.3 | log|σ_T| ∈ L¹(dτ/(1+τ²)); outer factor exists; zeros of σ_T are real-analytic and isolated | PROVED |
| 2.1 | The kernel of a truncated Toeplitz operator is **not** a scalar Toeplitz kernel N[U]. It is equivalent after extension to the kernel of a 2×2 matrix Toeplitz operator with symbol [[Θ̄,0],[σ,Θ]] | PROVED-CITED [CP16][mem] (the elementary inclusion is PROVED here) |
| 2.2 | Scalar reduction: N[Θ̄]∩N[σ_T] ⊂ ker A_{σ_T}, sufficient and not necessary. On full H² (T=∞, one-sided) ker T_σ = 0 for real nonconstant σ | PROVED / PROVED-CITED [HW] |
| 2.3 | MP argument criterion for the scalar piece. It does not decide contact | PROVED-CITED statement [MP10][mem]; inapplicability PROVED |
| 3.1 | Toeplitz kernel unchanged under symbol perturbations with Fourier support outside (−2T,2T) | PROVED |
| 3.2 | Lemma L is a **pointwise** identity, so the "prime" and "zero" symbols are the same function: same sign changes, same argument | PROVED (R164_101 L) |
| 3.3 | Sign structure of Re M at real height and for a quartet; per-quartet sign-change deficit O(1) and not additive in the total symbol | PROVED (formula, concentrated-g limit) / ARGUED (non-additivity consequence) |
| 4.1 | Sign-blindness: ker A_σ = ker A_{−σ}; no kernel criterion sees the sign | PROVED |
| 4.2 | Kernel equation over all H = E_c condition (R163_401 §4.6) = (1.1) family through Lemma P: the k=0 jet, not new | PROVED (restatement, E1) |
| 4.3 | Granularity: MP/BM-type criteria are stable under perturbations that move T_c, so they cannot locate T_c or give T₁ > ½log5 | ARGUED |
| 4.4 | New certified T₁ > ½log5 from an "argument budget" Σ_{n<e^{2T}} v_n | **NOT OBTAINED**: the method gives no such bound (4.1 + 4.3) |
| — | (★_cell), row D | OPEN |

## 1. Set-up

**1.1 (PROVED).** Write PW_T for the functions F̂ of exponential type ≤ T in L² (Fourier support [−T,T]); the form domain is 𝒟_T (R163_401). From R163_401 §1, W_T(F) = (1/2π)∫σ_T|F̂|² + 2Re(A(F)B̄(F)), with σ_T = m − Σ_{n<e^{2T}} v_n cos(τ log n). W_T ≥ 0 and W_T(F)=0 imply W_T(F,·)=0 (Cauchy–Schwarz, §4.6). Equivalently, in the weak sense on 𝒟_T,
  P_{PW_T}(σ_T F̂) + 2π[A(F) b + B(F) a] = 0,
where a, b ∈ PW_T are the Riesz representers of the linear functionals A, B. Under the unitary map F̂ ↦ e^{iTz}F̂, PW_T becomes K_Θ = H² ⊖ ΘH² with Θ = e^{2iTz}. The operator P_{K_Θ} M_σ |K_Θ is Sarason's **truncated** Toeplitz operator A^Θ_σ [S07][mem]. It is not the operator T_U on H² that [MP05, MP10] study. On 𝒫_T = {A=B=0} (codimension ≤ 2) the polar term vanishes. The primitive form 𝔞_T has kernel {F̂ ∈ 𝒫_T : P_{𝒫_T}(σ_T F̂) = 0} = ker A^𝒫_{σ_T}. A rank-2 perturbation changes dim ker by at most 2. A kernel of the full form gives a kernel of the primitive form as soon as A(F)=B(F)=0. In general one uses the bordered 2×2 system, which is finite-dimensional linear algebra and adds nothing analytic.

**1.2 (PROVED).** λ_min(T) := inf W_T on the unit sphere is nonincreasing in T: the spaces are nested, and the Weil functional of a fixed test does not depend on T. It is also continuous (lem:contA). It is > 0 at T ≤ ½log5 (certified, Paper 47). Hence T_c = inf{T : λ_min(T)=0} = min{T : ker ≠ 0 with the form ⪰ 0}. Remark: the predicate "ker A_T ≠ 0" taken alone, without ⪰ 0, also holds at later eigenvalue crossings of negative forms. See 4.1.

**1.3 (PROVED).** m(τ) = Re ψ(¼+iτ/2) − log π ~ log|τ|. So |σ_T| ≤ C_T log(2+|τ|) and log⁺|σ_T| ∈ L¹(Π). σ_T is real-analytic and not identically 0, so its zeros are isolated with finite order, and log|σ_T| ∈ L¹_loc. Near infinity σ_T ≥ ½log|τ| (the comb is bounded by Σ v_n). Hence log|σ_T| ∈ L¹(Π) and the outer function 𝒪_T with |𝒪_T|² = |σ_T| exists. Then σ_T = 𝒪_T 𝒪̄_T · s_T with s_T = sgn σ_T ∈ {±1}, a piecewise-constant unimodular function with finitely many jumps on each compact set. The number of jumps on [−R,R] is O_T(R) (Jensen applied to the entire extension of the comb plus m). The requested reduction U_T = Θ̄ s_T (𝒪̄_T/𝒪_T) has argument
  γ_T(τ) = −2Tτ + π·#{sign changes of σ_T in (0,τ)} + 2·arg 𝒪̄_T(τ),  with arg 𝒪_T = ½ H[log|σ_T|] (Hilbert transform).
This formula is PROVED. Its use is limited by §2.

## 2. What Makarov–Poltoratski can and cannot say here

**2.1 (PROVED, plus [CP16][mem]).** A^Θ_σ f = 0 with f ∈ K_Θ ⟺ σf ∈ \overline{H²_0} ⊕ ΘH² (the orthogonal complement of K_Θ in L²). This is a condition on a **sum** of two shift-invariant pieces. Writing σf = ḡ + Θk (g ∈ H²_0, k ∈ H²) together with Θf̄ ∈ H²_0 gives a 2-vector Toeplitz kernel with a 2×2 matrix symbol of the form [[Θ̄,0],[σ,Θ]] (equivalence after extension [CP16][mem]). Matrix Toeplitz kernels are not classified by one argument function. The scalar MP theory has no matrix analogue of the argument criterion (to our knowledge [mem]). **This answers task (1)–(2): there is no unimodular U_T with ker A_{σ_T} = N[U_T].** The "argument γ_T" above is the argument of the symbol of the **one-sided** operator T_{σ_T} on H², not of the truncated one.

**2.2 (PROVED / [HW]).** (a) N[Θ̄] ∩ N[σ_T] ⊂ ker A^Θ_{σ_T}. Indeed f ∈ K_Θ = N[Θ̄], and σf ∈ \overline{H²_0} gives P_Θ(σf)=0. This is only the subcase k = 0. (b) N[σ_T] = ker T_{σ_T} on H² is {0}: σ_T is real and nonconstant, so T_σ − 0 is self-adjoint with no eigenvalue [HW][mem]. Direct check: T_σ f = 0 means σf = ḡ with g ∈ H²_0. Then σ|f|² = ḡf ∈ \overline{H¹_0}·… The standard argument shows σf f̄ is real, lies in \overline{H¹_0}, and has mean 0, so it vanishes. Hence the sufficient scalar condition (a) is **never** met, and contact is a purely truncated (two-sided, Θ-dependent) phenomenon. So the criterion "N[U_T] ≠ 0" with U_T = Θ̄·(sign/outer phase) is the wrong object. For a self-adjoint symbol, the phase of U_T only records where σ_T is negative. Positivity of the compression is not a kernel property of any unimodular symbol.

**2.3 (statement PROVED-CITED [MP10][mem]; inapplicability PROVED).** For a meromorphic inner Θ_1 and a unimodular U = Θ̄_1 e^{iγ} with γ real-analytic (or with γ′ bounded below), the [MP10] criterion is as follows. N^p[U] ≠ 0 ⟺ γ = −α + h̃ + c, where α is increasing (α′ ≥ 0, a "Beurling–Malliavin admissible" or almost-Blaschke counting function) and h ∈ L¹(Π) satisfies Poisson-integrability conditions (with exact endpoint statements for p, see [P15, Ch. 3–4][mem]). In density terms, the deficit γ′ + 2T must be absorbable by an increasing α. Applied to s_T this decides only 2.2(b), where the answer is already {0}. The kernel the problem needs is the matrix kernel of 2.1.

**Comparison with T_c > ½log5.** The scalar criterion can neither reproduce nor contradict this. It returns "trivial" for **every** T, including T > T_c(f_t) for the falsifier f_t, where the truncated kernel is not trivial. That is consistent with 2.2(b) and shows the scalar criterion carries no contact information.

## 3. The global coupling

**3.1 (PROVED).** For F̂, Ĝ ∈ PW_T, ⟨φF̂, Ĝ⟩ = (1/2π)∫ φ̌(w) (F̌⋆Ǧ)(w) dw (up to normalisation). F̌⋆Ǧ is supported in [−2T,2T], so A^Θ_φ = A^Θ_ψ whenever (φ−ψ)ˇ vanishes on (−2T,2T) (as a distribution). Truncated Toeplitz kernels are therefore invariant under such changes. This is exactly Sarason's non-uniqueness of the symbol [S07][mem] (symbol defined modulo ΘH² + \overline{ΘH²}). The task's worry is resolved: the kernel is invariant.

**3.2 (PROVED).** R164_101 Lemma L, ½σ^g_T = −θ′_{X′} − Re M(½−iτ) + Σ_k Re M(−2k−½−iτ), is an identity of **functions** on ℝ, not merely modulo invisible terms. The smoothed comb σ^g_T differs from σ_T by an invisible symbol by 3.1, since g ≡ 1 below e^{2T} and the comb tail has frequencies log n ≥ 2T. Consequence: the "zero description" and the "prime description" are the **same** truncated Toeplitz operator. Moreover, for the smoothed symbol they are literally the same function: identical sign changes, identical outer factor, identical γ_T. There are no "two argument functions" to compare. The only freedom is the invisible class of 3.1, and the identity across it is Lemma P. That is E1.

**3.3 Sign structure (formula PROVED; consequence ARGUED).** M(z) = z^{−1}∫(−g′)e^{uz}du with supp(−g′) ⊂ [2T, 2T+η]. With w = δ + iy (y = γ−τ):
  Re M(w) = (δ²+y²)^{−1} ∫(−g′)(u) e^{uδ} (δ cos uy + y sin uy) du.
- On-line (δ=0): Re M(iy) = ∫(−g′) sin(uy)/y du. As η→0 this tends to sin(2Ty)/y, which has a positive central lobe of height 2T and sign changes at y ∈ (π/2T)ℤ∖{0}.
- Quartet ρ = ½+δ+iγ (δ>0) together with 1−ρ̄. The sum, as η→0, is
  [e^{2Tδ}(δ cos 2Ty + y sin 2Ty) + e^{−2Tδ}(−δ cos 2Ty + y sin 2Ty)]/(δ²+y²)
  = [2δ sinh(2Tδ) cos 2Ty + 2y cosh(2Tδ) sin 2Ty]/(δ²+y²).
  Its zeros solve tan 2Ty = −(δ/y) tanh(2Tδ). For |y| ≫ δ this is the on-line lattice shifted by O(δ²T/|y|). Near y = 0 there is one lobe of height ≈ 2T cosh(2Tδ) + 2 sinh(2Tδ)/δ (exponentially large in Tδ), compared with 2·2T for two on-line zeros at γ ± δ, whose sign-change sets interlace.
- So a quartet changes the local sign-change count of its **own** bump by O(1). The total symbol −θ′ = Σ_ρ Re M is a conditionally convergent superposition of oscillations with the common frequency 2T. Its sign changes are not the union of the bumps' sign changes; the number per unit length is set by the total amplitude (Jensen), not by the zeros individually. The quartet's O(1) effect is therefore not isolated in γ_T. It is the k = 0 datum (value at t_q), mixed globally exactly as in R166_201's jet hierarchy. ARGUED (the qualitative statement; the formula is exact).

## 4. The question (task 4), decided

**4.1 Sign-blindness (PROVED).** ker A_σ = ker A_{−σ} = ker A_{cσ} for every c ≠ 0. Every Toeplitz-kernel criterion (scalar or matrix, MP or other) is therefore blind to the sign of the compression. Contact = (kernel ≠ 0) ∧ (form ⪰ 0), and the second conjunct is row D itself on [0,T]. A kernel criterion locates T_c only when combined with 1.2. The combination needs triviality of ker(A_{σ_T}+polar) for **all** T in an interval, plus positivity at one point. That is a continuum of eigenvalue non-crossing statements, i.e. λ_min > 0 on the interval: the certificate problem, not a kernel problem.

**4.2 The kernel equation is E1 (PROVED, restatement).** Pair the kernel equation with Ĥ ∈ PW_T and apply Lemma P (R164_101) to h = F̂Ĥ^#. The result is Σ_{δ_ρ>0}[h(t_ρ)+h(t̄_ρ)] + Σ_{δ=0} h(γ) + polar = 0 for all H. This is the family (1.1)_H, i.e. R163_401 §4.6. It is "global in H", but it is the k = 0 jet (R166_201) and the witness-diagonal statement of E1′. It meets requirement (i) only in the trivial sense and fails (ii)–(iii). It adds nothing to R163_401 §4.6.

**4.3 Granularity (ARGUED).** Shifting the symbol by a constant moves the contact: λ_min(σ_T + c) = λ_min(σ_T) + c on the primitive space. So for every T with λ_min(T) attained there is a c(T) with ker A_{σ_T + c(T)} ≠ 0. The BM/MP criteria are formulated modulo h̃ with h ∈ L¹(Π) and modulo increasing α. They are stable under perturbations of log|U| and arg U by such h̃. A constant shift c of σ changes log|σ| by an amount in L¹(Π) where |σ| ≫ |c| (and the sign set only on a compact set). Hence any criterion invariant under the [MP10] equivalence returns the same answer for σ_T and σ_T + c on a range of c, while the actual kernel varies with c. **Consequence: MP-type density/argument criteria cannot locate T_c, and cannot certify λ_T > 0 on any interval.** In particular they give no T₁ > ½log5. The "argument budget" Σ_{n<e^{2T}} v_n controls the **number of sign changes** of the comb (Jensen/Bernstein). It does not control eigenvalue crossings, which depend on exact values. This matches the a priori remark in the brief: any triviality argument from σ_T alone applies to f_t verbatim and must fail at T_c(f_t).

**4.4 T₁ (NOT OBTAINED).** No new certified range. The honest negative result is 4.1 + 4.3.

## 5. Wall named

**W-TK (truncation + sign-blindness).** (a) Contact is a kernel of a *truncated* Toeplitz operator. That is a 2×2 matrix Wiener–Hopf kernel (2.1). The scalar Makarov–Poltoratski criterion sees only the one-sided operator, whose kernel is always {0} (2.2b). (b) Kernel criteria are sign-blind (4.1) and coarse (4.3). (c) By Lemma L pointwise and Lemma P, the zero-side and prime-side symbols are one operator, and its kernel equation is (1.1) over all H (4.2) = **E1**. Evaded walls: none. This route lands on E1 (R164_101 Thm E1) with the secondary wall "kernel ≠ positivity".

## Ledger

| Item | Status | Depends on |
|---|---|---|
| 1.1 truncated-Toeplitz set-up, primitive kernel | PROVED | R163_401 §1, §4.6; [S07][mem] for the name |
| 1.2 T_c = first kernel under ⪰ 0 | PROVED | lem:contA, nesting |
| 1.3 outer factorisation of σ_T, γ_T formula | PROVED | m ~ log, real-analyticity |
| 2.1 matrix equivalence after extension | elementary part PROVED; equivalence PROVED-CITED [CP16][mem] | — |
| 2.2 scalar kernel = 0 | PROVED (direct) / [HW][mem] | — |
| 2.3 MP criterion statement | PROVED-CITED [MP10],[P15][mem] | exact endpoint hypotheses to be checked against the source |
| 3.1 invisibility of symbols with Fourier support outside (−2T,2T) | PROVED | Paley–Wiener |
| 3.2 same operator, same function | PROVED | R164_101 Lemma L, 3.1 |
| 3.3 quartet bump formula | PROVED (η→0 limit); non-additivity ARGUED | — |
| 4.1 sign-blindness | PROVED | — |
| 4.2 kernel equation = (1.1)_H = E1 | PROVED (restatement) | Lemma P |
| 4.3 granularity, no T₁ | ARGUED | [MP10] invariance [mem] |
| (★_cell), row D | OPEN | — |

## Grid cells (for the editor)

- **8D** (DEAD routes): "Makarov–Poltoratski / Toeplitz-kernel first contact (R166_301)". Killer W-TK = E1 + sign-blindness + truncation. Residue: none.
- **1D** (restatements of D): "Contact ⟺ ker A^Θ_{σ_T} ≠ 0 under ⪰ 0 (truncated Toeplitz, matrix symbol [[Θ̄,0],[σ,Θ]])". Equivalent to D on [0,T] only together with positivity; not a new reduction.
- **2A** (tools, PROVED): scalar kernel triviality 2.2(b); kernel invariance 3.1; exact quartet bump formula 3.3; sign-blindness 4.1.

## Residue

O166.301 (OPEN, low priority): a matrix (2×2) Makarov–Poltoratski theory for kernels of truncated Toeplitz operators with real symbols. Even if it existed, 4.1 shows it would be sign-blind. It could at most locate crossings given positivity elsewhere, which is the certificate problem. Not recommended as a lead.
