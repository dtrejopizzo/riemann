# R186.002 — Construction of the semilocal prolate operator W_{λ,S}

No numerical computations were used.
Local sources:
* [CM] Connes–Moscovici, PNAS 119 (2022) e2123174119, 7 pp.
* [CCM] Connes–Consani–Moscovici, arXiv 2310.18423v2 (`mainc2m24fine.tex`; line numbers cited).
* [CC] Connes–Consani, arXiv 2006.13771 (`phase-137/cc_2006.13771_text.txt`).
* Corpus: R183.021 Thm 3.1, R183.031 Thm 1, R185.008 Lemma 1.1(b), Paper 47 thm:Z.

The conjectures of this document are stated as constructive spectral claims about the
window form. They are not classified by equivalences.

## Status

| # | Statement | Label |
|---|---|---|
| 1.1 | W_sa exists, is the unique self-adjoint extension commuting with F and with P_λ, P̂_λ; discrete spectrum | CITED [CM Thm 1.6, p. 3] |
| 1.2 | The negative eigenfunctions lie in Son_λ | CITED [CM Cor 2.2, p. 4] |
| 1.3 | **W_∞(g∗g\*) ≥ Tr(ϑ(g) 1_{(−∞,0)}(W_sa) ϑ(g)\*)** on the CC window (λ = 1) | **PROVED** (from CITED [CC Thm 1] + [CM Cor 2.2]) |
| 1.4 | Conjecture P_∞ (equality modulo finite rank) | OPEN (exact form in §1.4) |
| 2.1 | F_S = (−1)^{N_S} on L²(X_S)^{K_S}; the CCM candidate W_{λ,S} formally commutes with F_S | **PROVED** (on the polynomial kernel) |
| 2.2 | The transport θ_S W_sa θ_S^{−1} is **not** self-adjoint on L²(X_S) | **PROVED** |
| 2.3 | The unitary transport u_S W_sa u_S\* is self-adjoint and commutes with F_S, but has the spectrum of W_sa | PROVED (hence useless) |
| 2.4 | Jacobi matrix of W_{λ,S}: exact formula in terms of the moments of dm_S; closed generating function for S = {∞,2} | **PROVED** |
| 2.5 | Obstruction: dm_{∞,2} is not semiclassical on Γ's lattice, so there is no finite-order coefficient recursion via Pearson's method | PROVED (the obstruction); OPEN whether another closed recursion exists |
| 2.6 | W_{λ,S} commutes with P^S_λ and P̂^S_λ (the semilocal "miracle") | **OPEN — first lemma** |
| 3.1 | Conjecture P_S (spectral form) and its density requirement | OPEN; the requirement is PROVED (R183.031 Thm 1) |

## 1. Archimedean case

### 1.1 Definitions (CITED)

* **[CM p. 1, eq. (1)].** (W_λ ξ)(x) = −∂_x(λ² − x²)∂_x ξ(x) + (2πλ)² x² ξ(x) on L²(ℝ).
 The projections are P_λ = multiplication by 1_{[−λ,λ]} and P̂_λ = F P_λ F^{−1}, with
 F = F_{e_ℝ}.
* **CCM normalization [CCM l. 203–206].** On L²(ℝ)^{ev}, let 𝔰 be the self-adjoint generator of the
 dilations and let ξ = e^{−πx²}. Let N be the grading of the filtration span{p(𝔰)ξ : deg p ≤ n}.
 Then, formally, **W_λ = −𝔰² + 2πλ²(4N+1) − ¼**. Also 𝔰 = −i(H + ½) with H = x∂_x
 [CCM l. 837].
* **[CM Thm 1.6, p. 3].**
 (i) W_min on 𝒮(ℝ) has a self-adjoint extension W_sa that commutes with F.
 (ii) W_sa commutes with P_λ and with P̂_λ.
 (iii) W_sa is the unique self-adjoint extension that commutes with P_λ and P̂_λ.
 (iv) The spectrum is discrete and unbounded on both sides. The negative eigenvalues are
 simple. The positive ones have multiplicity 2, except perhaps for finitely many exceptions.
* **[CM Cor 2.2, p. 4].** If μ < 0 is an eigenvalue, its eigenfunction φ_μ lies in the Sonin space
 Son_λ = {f : P_λ f = 0 = P_λ F f}. CM does not claim that all of the spectrum of W_sa|Son is
 negative: "there could be only finitely many exceptions".
* **[CM Prop 3.2, p. 5] (semiclassical).** The number of eigenvalues −ξ ≤ −E² in the even part is
 approximated by

 σ(E, λ) ≈ (E/2π)(log(E/2π) − 1 + log 4 − 2 log λ) + λ² + o(1).

### 1.2 What is proved and what is observed

* **Proved.** A semiclassical Weyl law. Its leading term (E/2π)log(E/2π) − E/2π is the
 θ(E)/π term of Riemann–von Mangoldt. That term comes from the Γ factor, i.e. it is
 **archimedean**. The constant depends on λ.
* **Observed (numerical only, CM Figs. 1–2).** The eigenvalue-by-eigenvalue resemblance to the
 squares of the zeros.
* **Answer to question 3.** How does an archimedean operator "know" the zeros?
 What has been proved is that it knows the mean density. The global condition (commuting with F)
 fixes the asymptotic phase of the Γ factor, not the fluctuations. No prime enters W_sa.
 Any individual coincidence beyond the mean density would be a new phenomenon and
 is not demonstrated. This agrees with R183.031 §0.

### 1.3 Theorem 1.3 (PROVED from two CITED results)

**Statement.** Let λ = 1. Let g ∈ C_c^∞(ℝ_+^*) with supp g ⊂ [2^{−1/2}, 2^{1/2}] and ĝ(i/2) = ĝ(0) = 0.
Then

 W_∞(g ∗ g*) ≥ Tr(ϑ(g) Π_Son ϑ(g)*) ≥ Tr(ϑ(g) 1_{(−∞,0)}(W_sa) ϑ(g)*) ≥ 0.

**Proof.**
1. The first inequality is [CC Thm 1, eq. (4)], where S is the projection onto Sonin S(1,1).
 The Fourier normalization is the same (F_{e_ℝ}) and λ = 1.
2. For the second: by [CM Thm 1.6(iv)] the negative spectrum is discrete, and by [CM Cor 2.2]
 every negative eigenvector lies in Son_1. Hence Ran 1_{(−∞,0)}(W_sa) ⊂ Son_1, which gives
 1_{(−∞,0)}(W_sa) ≤ Π_Son as operators.
3. Conjugate by ϑ(g) and take the trace. The trace is finite because the intermediate term's
 trace already is [CC]. ∎

**Reading.** On the archimedean window, the **negative** spectral projection of W_sa is already
an admissible positive part of the Weil form. Watch the sign: the goal spoke of "P_+",
but what matches the Weil form is the negative spectrum of W_sa, which is the Sonin
space and the UV regime. The difference Π_Son − 1_{(−∞,0)}(W_sa) = Π_E is the projection onto
E := Son ∩ (eigenspaces ≥ 0). By [CM], E is finite-dimensional, and numerically E = 0.

### 1.4 Conjecture P_∞ (OPEN)

Let λ = 1 and let V_T be the class of g from Theorem 1.3. There exists a finite-rank operator K,
not depending on g, such that for every g ∈ V_T:

 W_∞(g∗g*) = Tr(ϑ(g) [1_{(−∞,0)}(W_sa) + K] ϑ(g)*) + |ĝ(0)|²·c₀.

Remark. [CC Thm 6.11] gives the difference W_∞ − Tr(ϑSϑ*) ≥ −c|ĝ(0)|² with 13 < c < 17,
**as a bound, not an identity**. P_∞ asks that this difference be of finite rank. It is a
spectral claim about an object that exists (W_sa). The "Sonin ↔ negative spectrum" part
is already proved (Thm 1.3). What is open is the identity of the remainder, which by [CC] is
expressed in prolate functions. Since the remainder is finite rank and explicit in prolates, the
first checkable case is dimension 1.

## 2. Semilocal case

[CCM] notation.
* X_S = 𝔸_S/Γ, with Γ = {±∏_{p∈S} p^{n_p}}, and K_S = ∏ ℤ_p^*.
* η_S(f) is the class of 1_{R_S}⊗f, and θ_S(f) the class of σ_S⊗f, with σ_p = ε₀ − p^{−1}ε₁.
* In the Mellin variable (𝒰_S = F_μ w_S):
 - η_S multiplies by L_S(½ − is) := ∏_{p∈S∖∞} L_p(½ − is) [l. 249];
 - θ_S multiplies by L_S(½ + is)^{−1} = ∏(1 − p^{−½−is}) [l. 950, 981].
* 𝒱_S : L²(X_S)^{K_S} → L²(ℝ, dm_S) gives the canonical form of the cyclic pair (𝔰, ξ_S), with
 ξ_S = η_S(ξ_∞) [l. 252, 792]. The density is dm_S(s) = |∏_{v∈S} L_v(½ − is)|² ds (up to
 normalization), which is **even** in s.

### 2.1 The CCM candidate and commutation with F_S (PROVED)

**[CCM l. 841–843].** The candidate is

 W_{λ,S} = (H+½)² + λ² N_S = −𝔰² + λ² N_S,

where N_S is the grading of the orthogonal polynomials of dm_S. The operator N_S must have
the affine normalization 2π(4N+1) − ¼ added if S = {∞} is to reproduce W_λ.

**Lemma 2.1 (PROVED).**
(a) F_S 𝔰 = −𝔰 F_S on the kernel 𝒫_S := span{𝔰^j ξ_S}.
(b) F_S ξ_S = ξ_S.
(c) On E_n^S ⊖ E_{n−1}^S one has F_S = (−1)^n, i.e. **F_S = (−1)^{N_S} = γ**, the
 ℤ/2 grading of the even pair.
(d) Consequently, W_{λ,S} commutes with F_S on 𝒫_S, and so does any function of
 (𝔰², N_S).

*Proof.*
1. 𝔰 commutes with η_S, because it acts on the archimedean variable [CCM l. 837]. Also
 F_S η_S = η_S F [CCM l. 251, 768], and on ℝ one has F 𝔰 F^{−1} = −𝔰 because F(H+½)F^{−1} = −(H+½).
 With this, F_S 𝔰 η_S f = η_S F 𝔰 f = −η_S 𝔰 F f = −𝔰 F_S η_S f, which gives (a).
2. (b) follows from F ξ_∞ = ξ_∞.
3. By (a) and (b), F_S 𝔰^j ξ_S = (−1)^j 𝔰^j ξ_S, so F_S preserves each E_n^S.
 - F_S is unitary, so it preserves E_n ⊖ E_{n−1}.
 - The degree-n vector of that complement is 𝔰^n ξ_S modulo E_{n−1}.
 - Since F_S acts by (−1)^n on 𝔰^n ξ_S and leaves E_{n−1} invariant, it acts by (−1)^n on
 the complement.
 This gives (c), and (d) is immediate. ∎

Consequence. In the semilocal case, commutation with Fourier is **automatic** for every
operator built from (𝔰², N_S). It is not the condition that selects the operator. The selective
condition is that of §2.6.

### 2.2 The θ_S transport is not self-adjoint (PROVED)

* By [CCM l. 1000], ⟨θ_S f | η_S g⟩ = ⟨f|g⟩, i.e. η_S\* θ_S = 1. Since θ_S is bijective
 [l. 1025], θ_S^{−1} = η_S\* and θ_S\* = η_S^{−1}.
* Let W^θ := θ_S W_sa θ_S^{−1}. Its adjoint is (W^θ)\* = η_S W_sa η_S^{−1}.
* Hence W^θ is self-adjoint if and only if W_sa commutes with η_S^{−1}θ_S.
* In the Mellin variable, η_S^{−1}θ_S = M_S(𝔰), where M_S(s) := ∏_{p∈S∖∞} |1 − p^{−½−is}|².
* For S = {∞,p} one has M_S(𝔰) = (1+p^{−1}) − p^{−½}(D_p + D_p^{−1}), where D_p is the
 unitary dilation by p.
* Let φ ∈ C_c^∞ supported near x₀ ≠ 0, ±λ, ±λp^{±1}. W_sa is local, so commuting with
 D_p + D_p^{−1} forces D_p W_λ D_p^{−1} = W_λ near x₀/p. However
 D_p W_λ D_p^{−1} = −∂(λ²p^{∓2} − x²)∂ + (2πλ)²p^{±2}x² (depending on the direction of the
 dilation), which is different.
* Hence **W^θ is not self-adjoint** on L²(X_S). It is self-adjoint for the inner product
 ⟨θ_S^{−1}·, θ_S^{−1}·⟩, and its spectrum is that of W_sa. ∎

### 2.3 The unitary transport adds nothing (PROVED)

Let u_S := θ_S M_S(𝔰)^{−1/2}, the polar part of θ_S.
* u_S is unitary, because θ_S\*θ_S = M_S(𝔰).
* u_S intertwines F with F_S, because M_S is even and F𝔰 = −𝔰F.
* Hence u_S W_sa u_S\* is self-adjoint, commutes with F_S, and has **exactly the spectrum
 of W_sa**.
* It does not preserve Son_S, because M_S^{−1/2} does not preserve Son_λ. This is the same
 locality issue as §2.2.

**Moral.** Any transport (unitary or by similarity) of W_sa never introduces the primes into the
spectrum. The semilocal object must be **genuinely new**, with a different spectrum. The
CCM candidate is such an object, because N_S ≠ η_S N η_S^{−1} [CCM Rem. care (i)].

### 2.4 Exact Jacobi matrix of the candidate (PROVED)

* dm_S is even, so (𝔰, ξ_S) is an even cyclic pair. In the orthonormal basis of dm_S,
 𝔰 is a Hermitian Jacobi matrix with zero diagonal and coefficients a_n^S.
* [CCM Prop jacobprol, l. 407–413] gives W_{λ,S}|_{𝓗^±} as a Jacobi matrix:

 J^+_{n,n+1} = −a_{2n}a_{2n+1}, J^+_{n,n} = −|a_{2n}|² − |a_{2n−1}|² + 2nλ²,

 and analogously J^−. With the normalization 2π(4N+1) − ¼, [CCM eq. explicitjac1] is recovered
 when S = {∞}:

 a_n = ¼((4n+1)(4n+2)(4n+3)(4n+4))^{1/2}, b_n = −8n² − 2n − ¾ + 2πλ²(8n+1).

* **Everything reduces to the a_n^S.** One has |a_{n}^S|² = D_{n+1}D_{n−1}/D_n², with D_n the
 Hankel determinant of the moments μ_k^S = ∫ s^k dm_S.
* **Generating function for S = {∞,2} (PROVED).** Let q = 2^{−1/2}.
 1. Poisson kernel: |1 − q e^{−iθ}|^{−2} = (1−q²)^{−1} Σ_{k∈ℤ} q^{|k|} e^{ikθ}.
 2. The archimedean part is w_∞(s) ∝ |Γ(¼ + is/2)|².
 3. By Barnes, ∫|Γ(a + it)|² e^{iut} dt = 2π Γ(2a)(2cosh(u/2))^{−2a}. With a = ¼, the
 transform of w_∞ is ∝ (2 cosh u)^{−1/2}.
 4. Hence, with 𝓜_S(u) := ∫ e^{ius} dm_S(s),

 𝓜_{∞,2}(u) = C Σ_{k∈ℤ} 2^{−|k|/2} (2^k e^u + 2^{−k} e^{−u})^{−1/2},
 μ_k^S = (−i d/du)^k 𝓜_S(u)|_{u=0}.

 The series converges uniformly with its derivatives near u = 0, because the term k
 is O(2^{−|k|}).
* **Where log 2 appears.** The "twist by (1 − 2^{−½−is})" appears as **shifts u ↦ u +
 k log 2** of the archimedean generating function, weighted by 2^{−|k|/2}. This is the dilation
 x ↦ 2^k x in the dual variable, which matches 𝓔_p(f)(u) = u^{1/2} Σ f(p^n u) [l. 855].
 This is the exact recursion available: a relation on the moments, not on the coefficients.

### 2.5 The obstruction to a closed recursion (PROVED / OPEN)

* For S = {∞}, w_∞ is Meixner–Pollaczek. It satisfies a Pearson equation on the
 lattice s ↦ s + 2i: w(s+2i)/w(s) is rational in s. The closed-form a_n follow from this.
* For S = {∞,2}, the ratio w_S(s+2i)/w_S(s) contains the factor
 [(1−q2^{−is})(1−q2^{is})] / [(1−q2^{−is}2^{2})(1−q2^{is}2^{−2})].
 This factor has infinitely many poles in s, so **it is not rational (PROVED)**.
* The weight is "mixed", with a Γ-type lattice in s and a 2^{is} lattice. It is semiclassical
 in neither one alone.
* Conclusion: there are no finite-order Laguerre–Freud equations via the Pearson route. Whether
 another closed recursion exists remains OPEN.

With this, CCM's request ("deferred to a forthcoming paper", l. 259) is reduced to an
explicit problem: the Hankel determinants of 𝓜_{∞,2}.

### 2.6 The first lemma (OPEN)

**Target lemma L1 (OPEN).** There exists an affine normalization c_S(N_S) giving
W_{λ,S} = −𝔰² + λ² c_S(N_S) with these three properties:
(i) it is essentially self-adjoint on the polynomial kernel 𝒫_S;
(ii) it commutes with P^S_λ = 1_{|x|_S ≤ λ} and with P̂^S_λ = F_S P^S_λ F_S^{−1};
(iii) its negative spectral subspace coincides with Son_λ(X_S, α), up to a finite-dimensional
discrepancy.

Status of each part.
* (i) reduces to the Carleman determinacy of dm_S. It is PROVED: dm_S ≤ C·dm_∞ and the density
 decays exponentially in |s|. Hence μ_{2k}^S ≤ C(2k)!/c^{2k}, and the Carleman condition
 Σ (μ_{2k}^S)^{−1/(2k)} = ∞ holds. Essential self-adjointness of −𝔰² + λ²N_S also needs a
 Nelson-type argument. Left OPEN.
* (ii) is the real content. For S = {∞} it is the Bell Labs miracle, and it depends on the
 coefficients of the differential equation vanishing at x = ±λ. For finite S there is no
 differential operator: P^S_λ is not a multiplier in s.
* **Falsifier (F1).** For S = {∞,2}, compute ⟨[W_{λ,S}, P^S_λ] e_0, e_1⟩ in the orthonormal
 basis of dm_S. It suffices to use the moments μ_0..μ_4 of §2.4 and the integrals
 ⟨P^S_λ e_i, e_j⟩, which are explicit through θ_S/η_S. If it does not vanish for any affine
 c_S, the CCM candidate is refuted and one must move to CCM's second option:
 metaplectic in SL_2(𝔸_S) [l. 270].

## 3. The spectral requirement and Conjecture P_S

* **Why the diagonal suffices (R183.021 Thm 3.1).** Every trace-type positive part enters
 only through its diagonal density in s. In canonical form,
 Tr(ϑ(g) P ϑ(g)\*) = ∫ |ĝ(s)|² P(s,s) ds, because ϑ(g) = ĝ(𝔰) is a multiplier.
* **Requirement (R183.031 Thm 1, unconditional by R185.008 Lemma 1.1(b)).** Let
 E_{S(T)} = P_T + R_T with n₋(R_T) bounded. Then the density ρ_T = P_T(s,s) tends to 0 in
 Landau measure on every compact set away from the ordinates of the zeros.

**Conjecture P_S (OPEN, constructive).** Let S(T) ⊇ {p < e^{2T}} and λ = λ(T) (the λ ↔ T
calibration is part of the conjecture; in [CC], λ = 1 corresponds to T = ½log 2). For the
operator W_{λ,S(T)} of L1 the following hold:
(a) For g in the primitive class of window T,
 W_{S(T)}(g∗g\*) ≥ Tr(ϑ(g) 1_{(−∞,0)}(W_{λ,S(T)}) ϑ(g)\*) − (rank-≤ N₀ term).
(b) Necessary consequence, by the requirement: the diagonal density 1_{(−∞,0)}(W_{λ,S(T)})(s,s)
 concentrates near the ordinates of the zeros as T → ∞.

* For S = {∞}, (a) is exactly Theorem 1.3, with T = ½log 2 and N₀ = 0. **The conjecture is
 true in its first case.**
* CM's data are compatible with (b) at the level of mean density (Weyl's law), and nothing more.
 A single fixed S cannot give (b) as T → ∞, because the requirement demands growing S(T).

**Identified risk (heuristic, OPEN).**
* For finite S, the factor M_S^{−1} is bounded above and below, with bounds
 (1 ± p^{−1/2})^{∓2}.
* Máté–Nevai–Totik-type theorems (cited from memory, must be verified) say that the
 diagonal of the Christoffel–Darboux kernels for the weight tends to the equilibrium density,
 **independent of the bounded factor**.
* If this transfers to the spectral projections of −𝔰² + λ²N_S, then for fixed S the
 density (b) does not see the primes at leading order. The localization would have to come from
 the regime where ∏_{p<e^{2T}}(1+p^{−1/2})² → ∞, i.e. from the joint dependence S(T), λ(T). That
 is the correct scale of the problem.

## 4. Program

1. **L1(ii) for S = {∞,2}**: the falsifier F1 (finite and exact). This is the first task.
2. If L1 falls: the metaplectic version (CCM l. 270), with the analogous lemma.
3. If L1 holds: prove P_S(a) for S = {∞,2} on the window T ≤ log 2. This is the extension of
 Theorem 1.3, using the isometry θ_S : Son → Son_S [CCM Thm isosonin], which is Hilbertian but
 not unitary. The control of the non-unitarity is M_S(𝔰), which is explicit.
4. P_∞ (finite-rank identity) in parallel, from [CC §6] (prolates).

No new sign is claimed.

## Audit notes

1. **Thm 1.3.** Check that the S of [CC] (Sonin S(1,1), Fourier F_{e_ℝ}) is the Son_1 of
 [CM]. Both use F_{e_ℝ} and the cutoff [−1,1] on L²(ℝ)^{ev}. Also check that
 Tr(ϑ 1_{<0} ϑ\*) is finite: it is dominated by the trace of the intermediate term, which is finite.
2. **Lemma 2.1.** Depends on F_S η_S = η_S F (CITED) and on 𝔰 commuting with η_S [CCM l. 837].
 Check the sign of F(H+½)F^{−1} = −(H+½) on L²(ℝ)^{ev}.
3. **§2.2.** The locality argument needs x₀ away from the singular points; it is a standard
 local argument. That M_S(𝔰) is a combination of D_p^{±1} is only exact for
 S = {∞,p}. For |S| > 2, products of dilations appear, and the argument is the same.
4. **§2.4.** The Barnes constant and the normalization of dm_S do not affect the a_n (the
 normalization cancels in D_{n+1}D_{n−1}/D_n²). The series converges as O(2^{−|k|}).
5. **L1(i).** Only the determinacy of dm_S is claimed. Essential self-adjointness of the
 composite operator remains OPEN.
6. **§3, risk.** It is heuristic: Totik's theorems are cited from memory and apply to
 compact support or Freud weights. Not used as a NO-GO.
7. The conjectures are spectral and constructive.

## Note (R186_091)

* Thm 1.3: directions verified; one-line corollary of [CC] Thm 1 + [CM] Cor 2.2, not new; add commutation with parity; [CM] does not prove dim E < ∞.
* Lemma 2.1: statement correct, proof of (c) invalid (fix with parity of the orthogonal polynomials of an even measure; ξ_S cyclic). §2.4 recomputed: correct. §3: Totik heuristic, do not use. Real content: L1(ii)/F1 OPEN.

## Note (R186_020)

* §2.4 (moment generating function, Hankel/Jacobi) re-derives CCM arXiv:2403.01247 Prop 3.2/4.1, Thm 5.6/6.5; cite it.
</content>
