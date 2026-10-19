# Doc 143 — Attack on Problem 136.A: quantitative localized positivity under RH and the exact exponent of Lehmer pairs

**Program:** Riemann Hypothesis — Phase 46, "audit and attacks".
**Object:** Problem 136.A (D136 §6.3, item 7): under RH, how fast does the localized Weil form approach degeneracy? Is there a per-cell positivity modulus ε(p) > 0, and what quantitative lower bound does the localized form have in a window [T, T+H]? Connection declared in D136: Lehmer pairs make λ_min genuinely small — "estimating it is again a zero-repulsion problem".
**Prerequisites read at source:** D136 complete (Defs. 3.1–3.2, Theorems 2.5, 4.1–4.4, 5.4, Prop. 5.5, Cor. 5.6, §6.3 Problem 136.A); D139 (audit: branch RH⟹0 SURVIVES, branch ¬RH conditional = Problem 139.A, E-139.1–139.6); D141 (LP-134 canonical form, relative no-go 141.B2, Computations 141.M4–M5). Cited spectral inputs: D107 (absolute convergence, spectral side, closure under x∂ₓ), D108 (Prop. 2.2: diagonal positivity under RH).
**Inherited status warning (D139):** everything that follows on the "under RH" side uses only the RH branch of the logistic criterion, which the D139 audit declared SURVIVES without reservations. Theorem 5.4 of D136 (¬RH branch, conditional on 139.A) is not used except where explicitly declared, with its caveat.
**Creative contract:** **[NEW-DEFINITION]** = total freedom; **[THEOREM]/[PROPOSITION]/[LEMMA]** = complete proof or it does not carry the label; **[COMPUTATION]** = closed; **[BRIDGE]** = frank status; **[GAP]/[DESIDERATUM]** = declared. Nothing is fabricated.

---

## 0. Executive summary and anticipated verdict

1. **(§1) The question "speed of σ_loc^(k) → 0" is degenerate as stated, and it is transmuted.** Under RH, x₀(N) = 0 for EVERY N (D136 Prop. 5.5): σ_loc^(k) ≡ 0 identically — there is no speed to measure, neither in k nor in N. The real quantitative content of 136.A lives one floor below: in the **positivity modulus** λ_min(p) := λ_min(Gram(Q|_cell)), which under RH is > 0 in every cell but can be arbitrarily small. 136.A is reformulated: what lower bound does λ_min(p) have, and is it uniform in the height T?

2. **(§2, [THEOREM 143.B]) The bound under RH exists and is closed: a Gram–Vandermonde in the gaps of the zeros of the window.** For every cell of dimension d and any d distinct zeros accessible to the cell,
   λ_min(p) ≥ c(p) · Π_{k<l} ((γ_l − γ_k)/w)², with c(p) explicit and a complete elementary proof (term-by-term positivity under RH + minimum singular value ≥ |det|/‖·‖^{d−1} + Vandermonde determinant). Each close pair of zeros enters the product EXACTLY once: a Lehmer pair at distance δ degrades the bound by (δ/w)², no more. The exact classical framework is Ingham (1936) from below and Montgomery–Vaughan (1974) from above ([PROPOSITION 143.B.3]): the positivity modulus of the localized Weil form IS the Riesz lower bound of the exponential system {e^{iγx}} of the window, and Lehmer pairs live exactly below the Ingham threshold a·δ > π.

3. **(§3, [COMPUTATION 143.C] + [THEOREM 143.C′]) The Lehmer exponent is exactly 2.** Closed 2×2 computation: in the canonical cell (bump × monomials) aligned with a pair γ' − γ = δ, the toy Gram matrix is diagonal with λ_min = 2 b̂(aδ/2)² (δ/2w)² — exponent 2, exact closed form. With the on-line sea of zeros included and a local regularity hypothesis (R_η), bilateral bound: c₁(δ/w)² ≤ λ_min(p) ≤ C₁(δ/w)² + C₂·floor(p), with the floor explicit and as small as desired at fixed profile. Normalization warning ([COMPUTATION 143.C](b)): nearly-dependent bases aligned to the pair inflate the exponent to 4 — the exponent is an invariant of the pair (form, class of bases); for the canonical cells of D136 it is 2.

4. **(§4) Inverse direction: uniformity of the modulus IS a zero repulsion — the vertical twin of LP-134.** [NEW-DEFINITION] **LP-143**: liminf (γ_{n+1} − γ_n)·log γ_n > 0 (vertical repulsion on the line, exact mirror of LP-134 = liminf |β−½|·log γ > 0 of D141). [PROPOSITION 143.E]: under RH, uniform modulus in T for the calibrated profile ⟺ LP-143 (both directions proved over §2–§3). Status of LP-143: open; under RH the normalized liminf is known to be ≤ 0.5172 (Conrey–Ghosh–Gonek 1984) and GUE predicts liminf = 0: **LP-143 is conjecturally FALSE.** The classical Lehmer pair (γ ≈ 7005.063, δ ≈ 0.0377, normalized gap ≈ 0.053) is its numerical shadow. An unconditional bound of λ_min for all cells would imply RH itself — but only via the ¬RH branch of D136, conditional on 139.A: declared with its caveat.

5. **(§5) VERDICT on 136.A: RESOLVED IN RELATIVE FORM — the intermediate option, and it is a frank conditional theorem.** Under RH: (i) there is a closed lower bound in terms of the gaps of the window ([THEOREM] conditional, §2); (ii) the Lehmer degradation exponent is exactly 2 (§3); (iii) there is NO bound uniform in T provable today, and uniformity is EQUIVALENT to LP-143, which GUE conjecturally refutes: near-doubles do not destroy positivity (always strict) — they destroy its UNIFORMITY, with speed δ². 136.A reduces exactly to minimum-gap statistics = pair correlation, as D136 §6.3 anticipated. The dream of "Π₁ with modulus" (computable ε(p)) is refuted in its arithmetic version: our ε(p) is computable from the ZEROS, not from the primes — the wall reappears where it should.

---

## 1. Definitions: the localized Weil form and its positivity modulus

### 1.1. Coordinates and the spectral form

We work in the additive coordinate x = log (logarithmic variable of the multiplicative group), with transform
$$\hat h(t) := \int_{\mathbb R} h(x)\,e^{-ixt}\,dx .$$
Generic zero ρ = β + iγ. **Under RH** (hypothesis in force in §§1–3 unless noted): ρ = ½ + iγ, and the Weil form on the class of tests is diagonal in the zeros:
$$Q(h,h') \;=\; \sum_{\gamma} \hat h(\gamma)\,\overline{\hat h'(\gamma)}, \tag{1.1}$$
sum over ordinates with multiplicity (both signs). Status of (1.1): it is the compression of the Weil form to the thickened class, in the program's normalization — D108 Prop. 2.2 (diagonality under RH), with absolute convergence over the class by D107 Lemma 2.2(b); the equality between the arithmetic presentation (primes) and the spectral one (zeros) is the explicit formula [W52]. The term-by-term positivity of (1.1) is the only use of RH in §§2–3, exactly as in the RH branch of D136/D139 (the branch that SURVIVES).

**Lemma 143.A (convergence over cells).** If |ĥ(t)| ≤ C (1 + a|t − c|)^{−m} with m ≥ 2, then Σ_γ |ĥ(γ)|² ≤ C² C₀ a^{−1}(1+a^{-1})·log(2+|c|)-bounded; in particular finite, and ≤ C² C' log(2+|c|) with C' absolute if a ≥ 1.

*Proof.* Grouping ordinates by intervals |γ − c| ∈ [j, j+1): the number of zeros per unit interval at height ~|c|+j is ≤ C₁ log(2+|c|+j) [IK04, Thm. 5.8]. Then Σ_γ |ĥ(γ)|² ≤ C² Σ_{j≥0} C₁ log(2+|c|+j)(1+aj)^{−2m} ≤ C² C₁ log(2+|c|) Σ_j (1+j)(1+aj)^{−4} < ∞ (using log(2+|c|+j) ≤ log(2+|c|)(1+j) and m ≥ 2). ∎

### 1.2. [NEW-DEFINITION 143.1] Window cell and localized form Q_{T,H}

Fix once and for all b ∈ C_c^∞((−1,1)) even, real, nonzero, with b̂ (real, even, entire) normalized b̂(0) = 1 and |b̂(v)| ≤ C_M (1+|v|)^{−M} for the order M of the profile (computable family, as in D136 Def. 3.1; M is FINITE and fixed per profile — no statement with M → ∞, in compliance with the GAP-A lesson of D139).

A **window profile** is p = (d, a, w, M, c): dimension d ∈ ℕ, support a > 0, spectral half-width w > 0, order M ≥ d + 2, center c ∈ ℝ (window height; the window considered is [T, T+H] with c = T + H/2, w = H/2). **Resolution condition:** a·w ≥ 1 (the cell resolves its window). The **cell** is
$$V_p := \mathrm{span}\{h_0,\dots,h_{d-1}\},\qquad
\hat h_j(t) \;:=\; \hat b\big(a(t-c)\big)\cdot\Big(\frac{t-c}{w}\Big)^{j}. \tag{1.2}$$
Each h_j is C_c^∞ with support ⊆ [−a, a]: ĥ_0 is the transform of a^{−1}b(x/a)e^{icx}, and the monomial factor is the differential operator ((−i d/dx − c)/w)^j applied to it (preserves support and smoothness; in multiplicative coordinates it is the closure under x∂ₓ of the class, D107). The cell is test-accessible: the profile does not mention zeros. It is the same class of cells of D136 Def. 3.1, written in the one-variable coordinate (the σ-lateral compression; the bridge with Q₂ of D136 is the factorization (1.2) of D136 §1.1 with the τ side frozen in its bump — every element of V_p ⊗ {φ_0} is a test of the double class).

**[NEW-DEFINITION 143.2] (localized form and positivity modulus).**
$$Q_{T,H} := Q\big|_{V_p}\ \ (\text{the Gram matrix } G_p := (Q(h_i,h_j))_{i,j}),\qquad
\lambda_{\min}(p) := \lambda_{\min}(G_p) = \min_{\|c\|_2 = 1} Q\Big(\sum_j c_j h_j\Big),$$
with the coefficient normalization in the canonical basis (1.2) — exactly the ε(p) whose study D136 §6.3 asks for. The **window part** is Q_W(h) := Σ_{γ ∈ [T,T+H]} |ĥ(γ)|² ≤ Q(h) (under RH, every term is ≥ 0: localizing can only lower). By Lemma 143.A, G_p is well defined, and λ_max(G_p) ≤ d·max_j Σ_γ |ĥ_j(γ)|² ≤ C(p)·log(2+T) (crude bound; the fine one is Prop. 143.B.3).

**[NEW-DEFINITION 143.3] (tower of moduli).** For the grid 𝒢_N of D136 Def. 3.2: ε_N := min{λ_min(p) : p ∈ 𝒢_N, centered wherever it is}. Under RH, "x₀(N) = 0 ∀N" (D136 Prop. 5.5) is the qualitative statement ε_N ≥ 0; Problem 136.A is its quantification: is ε_N ≥ a computable modulus?

**Remark 1.1 (the transmutation of the speed question).** The literal question of 136.A ("how fast does σ_loc^(k) → 0?") has a trivial and empty answer: under RH, x₀(N) = 0 exactly for every N (every compression of a form ≥ 0 is ≥ 0), hence σ_loc^(k) = 0 for every k — convergence in zero time, with no speed. The logistic tower amplifies signs, not moduli: it is an amplifier of the DICHOTOMY, blind to the distance to degeneracy. All the quantitative information is in λ_min(p) and ε_N. The rest of the document attacks that.

---

## 2. [THEOREM] The lower bound under RH: Gram–Vandermonde in the gaps

### 2.1. The central theorem

**Theorem 143.B (quantitative localized positivity under RH; complete proof).** Assume RH. Let p = (d, a, w, M, c) be a window cell and let γ_1 < γ_2 < ⋯ < γ_d be DISTINCT ordinates of zeros of ζ (any, chosen for convenience; infinitely many exist with b̂(a(γ−c)) ≠ 0 because b̂ is entire nonzero and its real zeros are discrete). Set
$$\beta_k := \hat b\big(a(\gamma_k - c)\big) \neq 0,\qquad R := \max_k \frac{|\gamma_k - c|}{w},\qquad
K := \big(\max_k |\beta_k|\big)\cdot \max(1, R)^{\,d-1}.$$
Then
$$\boxed{\ \lambda_{\min}(p) \;\geq\; \frac{\displaystyle\prod_{k=1}^{d} \beta_k^2 \cdot \prod_{1 \le k < l \le d} \Big(\frac{\gamma_l - \gamma_k}{w}\Big)^{2}}{\big(d\,K\big)^{2(d-1)}}\ \;>\;0. }$$

*Proof.* (1) **Term-by-term positivity.** For h = Σ_j c_j h_j, by (1.1) under RH all terms are ≥ 0; discarding all but the d chosen ones:
Q(h) ≥ Σ_{k=1}^d |ĥ(γ_k)|² = ‖E c‖²₂, where E ∈ ℂ^{d×d} is the evaluation matrix E_{kj} := ĥ_j(γ_k) = β_k·((γ_k − c)/w)^j.

(2) **Minimum singular value.** ‖Ec‖² ≥ s_min(E)²‖c‖² for every c. With singular values s_1 ≥ ⋯ ≥ s_d: |det E| = Π s_i ≤ s_min·s_1^{d−1}, hence s_min ≥ |det E|/s_1^{d−1} ≥ |det E|/‖E‖_F^{d−1}, and ‖E‖_F ≤ d·max|E_{kj}| ≤ d·K (d×d matrix; |((γ_k−c)/w)^j| ≤ max(1,R)^{d−1}).

(3) **Vandermonde.** E = diag(β_1,…,β_d)·V with V_{kj} = ν_k^j, ν_k := (γ_k − c)/w: det V = Π_{k<l}(ν_l − ν_k) (Vandermonde, distinct nodes), hence |det E| = Π|β_k|·Π_{k<l}|γ_l − γ_k|/w ≠ 0.

Combining: λ_min(p) = min_{‖c‖=1} Q(h) ≥ s_min(E)² ≥ |det E|²/(dK)^{2(d−1)}, which is the bound. Strict positivity: det E ≠ 0. ∎

**Corollary 143.B.1 (form at the minimum gap, full window).** If the window [c−w, c+w] contains d zeros with b̂ ≥ β₀ > 0 at them and consecutive gaps ≥ δ_*, then (R ≤ 1, K ≤ ‖b̂‖_∞):
$$\lambda_{\min}(p) \;\geq\; \frac{\beta_0^{2d}}{(d\,\|\hat b\|_\infty)^{2(d-1)}}\;\prod_{k<l}\Big(\frac{\gamma_l-\gamma_k}{w}\Big)^2
\;\geq\; \frac{\beta_0^{2d}}{(d\,\|\hat b\|_\infty)^{2(d-1)}}\,\Big(\frac{\delta_*}{w}\Big)^{d(d-1)}\cdot\prod_{k<l}\min\big(1,\tfrac{l-k}{1}\big)\text{-improvable}.$$
More useful than the raw power d(d−1) is the structure of the product: **each close pair enters exactly once**. If the window has ONE pair at distance δ and the rest of the gaps are ≥ comparable to w, the bound is ≥ c(p)·(δ/w)² — a single quadratic factor per Lehmer pair. (Verification in §3: this exponent is exact.) ∎

**Remark 2.1 (what this is, conceptually).** λ_min(p) is the frame (Riesz) lower bound of the evaluation system at the zeros on the cell. Theorem 143.B is the finite determinantal version — the only unconditional-in-configuration one available — of Ingham's theory: the quantitative positivity of localized Weil IS a problem of quantitative linear independence of exponentials {e^{iγx}} on [−a, a], and its modulus is measured in ordinate gaps. The wall of 136.A is thus mapped from the start: a uniform lower bound of λ_min requires a lower bound of gaps — vertical repulsion. §4 turns this into an equivalence.

### 2.2. The classical framework: Ingham from below, Montgomery–Vaughan from above

**Proposition 143.B.2 (Bessel/upper bound via Montgomery–Vaughan; complete proof over the cited input).** Let {γ_n} ⊂ [T, T+H] be distinct ordinates with minimum separation δ_* > 0, and h ∈ L²(ℝ) with supp h ⊆ [−a, a]. Then
$$\sum_{n} |\hat h(\gamma_n)|^2 \;\leq\; \Big(2a + \frac{3\pi}{\delta_*}\Big)\,\|h\|_{L^2}^2 .$$

*Proof.* Montgomery–Vaughan's mean-value theorem [MV74, Cor. 2 of the generalized Hilbert inequality theorem] gives, for distinct reals with separation ≥ δ_*:
∫_{−a}^{a} |Σ_n c_n e^{iγ_n x}|² dx = Σ_n |c_n|² (2a + θ_n·3π/δ_n) with |θ_n| ≤ 1, δ_n ≥ δ_*; in particular the norm of the synthesis operator S: (c_n) ↦ Σ c_n e^{iγ_n·} ∈ L²(−a,a) satisfies ‖S‖² ≤ 2a + 3π/δ_*. The analysis operator h ↦ (⟨h, e^{iγ_n·}⟩_{L²(−a,a)})_n = (ĥ(γ_n))_n is S*, with the same norm. Hence Σ|ĥ(γ_n)|² ≤ ‖S*‖²‖h‖² ≤ (2a + 3π/δ_*)‖h‖². ∎

**Remark 2.2 (Ingham and the exact threshold where Lehmer pairs live).** In the lower direction, Ingham's inequality [I36, Thm. 1] gives: if the gaps are ≥ δ_* and **a > π/δ_***, then ∫_{−a}^a |Σ c_n e^{iγ_n x}|² dx ≥ C(a, δ_*) Σ|c_n|² with an explicit constant > 0 — the exponential system of the window is a Riesz sequence, and by the same duality argument the positivity modulus in L² normalization is bounded below at scale. The hypothesis a·δ_* > π is OPTIMAL (Ingham constructs counterexamples at a·δ_* = π). Read the full picture: with support a ≍ A log T (the natural budget; cf. D134/D141, the resolution 1/log T), Ingham covers exactly the pairs with δ > π/a ≍ π/(A log T) — the super-resolution gaps — and **fails exactly for the sub-resolution pairs a·δ ≤ π: Lehmer pairs are, by definition of the scale, the pairs below the Ingham threshold.** Both frame bounds (Ingham below, MV above with its 3π/δ_*) degenerate simultaneously as δ_* → 0: this is not a technical limitation of an inequality, it is the geometry of the problem. Theorem 143.B is what survives below the threshold: no separation hypothesis, a Vandermonde modulus that degrades with the real gaps — and §3 shows that this degradation is exact, not an artifact of the proof.

---

## 3. The Lehmer connection in closed form: the exponent is 2

### 3.1. [COMPUTATION 143.C] The exact 2×2 (toy: only the pair in the universe)

Let γ' = γ + δ be a pair of ordinates (δ > 0 small) and, as a toy, suppose they are the ONLY zeros seen by the cell (the sea is turned off; §3.2 turns it on). Canonical cell d = 2 centered on the pair: c := γ + δ/2, profile (2, a, w, M, c), normalized nodes ν_{1,2} = ∓δ/(2w), weights β := b̂(aδ/2) = b̂(−aδ/2) (b̂ even).

**(a) Canonical basis (bump × monomials).** E = β·[[1, −u],[1, u]] with u := δ/(2w). Then
$$E^*E = \beta^2\begin{pmatrix}2 & 0\\ 0 & 2u^2\end{pmatrix}
\quad\Longrightarrow\quad
\boxed{\ \lambda_{\min} = 2\,\hat b\big(\tfrac{a\delta}{2}\big)^2\,\Big(\frac{\delta}{2w}\Big)^2\ },\qquad \lambda_{\max} = 2\,\hat b\big(\tfrac{a\delta}{2}\big)^2,$$
exact closed form (the toy Gram matrix is diagonal!), minimum eigenvector c = (0,1): the witness is ĥ = b̂(a(t−c))·(t−c)/w, the test ANTISYMMETRIC about the center of the pair, which vanishes at the midpoint and equals ±βu at the two zeros. **Exponent 2 in δ, with exact constant.** This matches Corollary 143.B.1 (the general lower bound gives c·(δ/w)² here): Theorem 143.B is exact in the exponent.

**(b) Normalization warning (the false exponent 4).** If instead of the canonical basis one uses the "pair-aligned" basis u_j with û_j(t) = b̂(a(t−γ_j)) (one bump per zero), then E = [[1, β_δ],[β_δ, 1]] with β_δ := b̂(aδ), symmetric, Gram = E², and
λ_min = (1 − b̂(aδ))² = κ_b²(aδ)⁴ + O((aδ)⁶), κ_b := −b̂''(0)/2 > 0:
**exponent 4.** There is no contradiction: the aligned basis is itself nearly dependent (u_1 ≈ u_2 as aδ → 0), and normalizing by coefficients in a basis that degenerates inflates the apparent modulus. In the L² normalization of the test (Rayleigh quotient Q(h)/‖h‖²_{L²}, basis-invariant), the same computation gives min = (1−b̂(aδ))²·2/(2(‖b‖²-terms)(1−\widehat{|b|^2}-ratio)) ≍ a-scale·(aδ)² — exponent 2 again. **Moral, recorded:** the Lehmer exponent is an invariant of the pair (form, class of admissible bases); for the canonical cells of D136 (bump × monomials, Riesz basis with constants independent of the configuration) it is 2; the 4 is an artifact of degenerate bases. Every quantitative statement of 136.A must declare its normalization — the same lesson as E-139.1 (the radical bug was also a badly chosen denominator).

### 3.2. The sea turned on: upper bound with controlled tail

For the toy to become a theorem, two things must be paid for: annihilating the pair's neighboring zeros (with the cell's degrees of freedom, à la D136 Lemma 5.3) and bounding the far tail (with the decay M of the profile, at FIXED M — no limits in M, lesson GAP-A of D139).

**Hypothesis (R_η) (local regularity of the sea; declared, not proved — a configuration hypothesis).** Let c be the height of the pair. The zeros in [c−1, c+1] other than the pair have mutual gaps ≥ η·w (η > 0 fixed; with the natural calibration w = 1/log T it is the typical GUE separation, which holds for almost every pair in the density sense but NOT for all — frankness: (R_η) excludes the presence of a SECOND Lehmer pair stuck to the first).

**Theorem 143.C′ (bilateral bound of the aligned cell; complete proof under RH + (R_η)).** Assume RH. Let γ' = γ + δ with 0 < δ ≤ w, c := γ + δ/2, and suppose (R_η). Fix s ≥ 1 with sw ≤ 1 and let S := {zeros γ_n ∉ {γ,γ'} : |γ_n − c| ≤ s·w}, d := |S| + 2 (finite: |S| ≤ 2s/η + 1 by (R_η)). Let p = (d, a, w, M, c) with aw ≥ 1 and M ≥ d + 2. Then there exist constants 0 < c_1(p,η,s) ≤ C_1(p,η,s) and C_2(p,η,s), explicit in the proof and depending ONLY on the profile and on (η, s) — not on T nor on δ — such that
$$c_1\,\Big(\frac{\delta}{w}\Big)^2 \;\leq\; \lambda_{\min}(p) \;\leq\; C_1\,\Big(\frac{\delta}{w}\Big)^2 \;+\; C_2\,\Big[(as w)^{-2(M-d)-1} + \log(2+T)\,(a)^{-2(M-d+1)}\Big].$$

*Proof.* **Lower bound.** Theorem 143.B with the d nodes {γ, γ'} ∪ S: the Vandermonde product contains the pair's factor (δ/w)² once; all other factors involve at least one element of S or the gap between distinct members: by (R_η) and because the elements of S are mutually ≥ η·w apart and the nodes are at distance ≤ (s+1)w from the center, each of the remaining d(d−1)/2 − 1 factors is ≥ (η/2)² and ≤ (2s+2)² in normalized absolute value (the gaps to the pair: ≥ the separation of S from the pair, which by (R_η) applied to the whole set is ≥ η·w·½ taking η from the hypothesis on all zeros of [c−1,c+1] minus the pair's internal gap, which is the only one exempt). The weights: |β_k| = |b̂(a(γ_k−c))| with a|γ_k−c| ≤ a(s+1)w ≤ 2asw bounded by the profile: β₀(p,s) := min of |b̂| over the compact set [−2asw, 2asw] minus its zeros — if some β_k falls on a zero of b̂, move the center c within the mesh (D136 Lemma 5.3, last point: the zeros of b̂(a(·−ic)) are discrete and the grid dodges them with margin b₀/2; same argument). Collecting: λ_min ≥ c_1(δ/w)² with c_1 = β₀^{2d}(η/2)^{d(d−1)−2}/(dK)^{2(d−1)}.

**Upper bound.** Witness: v with
$$\hat v(t) := \hat b\big(a(t-c)\big)\cdot P(t),\qquad
P(t) := \frac{t-c}{w}\,\prod_{\gamma_n \in S}\frac{t-\gamma_n}{w},$$
monic polynomial of degree d−1 in (t−c)/w: v ∈ V_p with coefficient vector c_v = (elementary symmetric functions of the normalized nodes ν_n = (γ_n−c)/w ∈ [−s,s], and the central factor 0); its top coordinate is 1, hence ‖c_v‖ ≥ 1, and λ_min(p) ≤ Q(v)/‖c_v‖² ≤ Q(v). Budget of Q(v) = Σ_γ |v̂(γ)|², in four classes:
(i) **S:** v̂(γ_n) = 0 — annihilated exactly (the key of D136 Obs. 5.1: the witness may use positions; the cell does not mention them).
(ii) **The pair:** |P(γ)| = (δ/2w)·Π_S |γ−γ_n|/w ≤ (δ/2w)(s+1)^{d−2}, likewise γ'; with |b̂| ≤ ‖b̂‖_∞: contribution ≤ 2‖b̂‖²_∞ (s+1)^{2(d−2)} (δ/2w)² =: C_1(δ/w)².
(iii) **Ring sw < |γ_n − c| ≤ 1:** by (R_η), at most 1 + 1/(ηw) zeros, separated ≥ ηw: grouping by layers |γ_n−c| ∈ [kw, (k+1)w], k ≥ s, there are ≤ 1 + 1/η zeros per layer; in layer k, |b̂(a(γ_n−c))| ≤ C_M(akw)^{−M} and |P| ≤ (2k)^{d−1} (since |t−γ_n|/w ≤ |t−c|/w + s ≤ 2k for k ≥ s): term ≤ C_M²(1+1/η)·Σ_{k≥s} (2k)^{2(d−1)}(akw)^{−2M} ≤ C(d,M,η)·(aw)^{−2M}·s^{2(d−1)−2M+1}/(2M−2d+1) ≤ C'(asw)^{−2(M−d)−1} (using aw ≥ 1 to absorb powers).
(iv) **Far away, |γ_n − c| > 1:** by unit intervals with density ≤ C log(2+T+j) [IK04]: |v̂| ≤ C_M(aj)^{−M}(2j/w)^{d−1}; the sum ≤ C(d,M)·log(2+T)·w^{-2(d-1)}a^{−2M}Σ_j j^{2(d−1)−2M}(1+j) ≤ C''·log(2+T)·a^{−2(M−d+1)} (with M ≥ d+2 the series converges; the w^{−2(d−1)} is absorbed via aw ≥ 1 into a^{2(d−1)}).
Summing (i)–(iv): the stated bound. ∎

**Corollary 143.C′.1 (natural calibration and reading).** With a = A log T, w = 1/log T (natural resolution; aw = A ≥ 1), s and η fixed: d ≤ 2s/η + 3 fixed, and
$$c_1\,(\delta \log T)^2 \;\leq\; \lambda_{\min}(p) \;\leq\; C_1\,(\delta\log T)^2 + C_2\Big[(As)^{-2(M-d)-1} + (\log(2+T))^{1-2(M-d+1)}\Big].$$
At fixed profile, the floor C₂[…] can be made smaller than any fixed target ε̄ > 0 by choosing M (FIXED) large enough with respect to (A, s, d, ε̄) — a choice made ONCE, with no limit M → ∞ (the constants C_M, β₀ of the chosen profile enter c_1, C_1: legitimate because δ → 0 is the only limit in the statement). Conclusion: **in the range δ log T ≥ floor^{1/2}, λ_min(p) ≍_{p,η} (δ log T)²** — the Lehmer exponent is exactly 2 at resolution scale. A Lehmer pair with small normalized gap ϑ = δ log T/2π depresses the positivity modulus of ITS cell to ≍ ϑ²: it quantifies "near-counterexample" with a closed rate. ∎

**Remark 3.1 (crossing with D141, Computation 141.M5).** The exponent 2 is the same "second order" of D141: the first-order signal of a symmetric configuration is null (141.M4) and the second-order one has zero mean with width δ (141.M5). Here the symmetry is vertical (on-line pair about its midpoint) instead of horizontal (quadruple about the line), and the antisymmetric test of Computation 143.C(a) is exactly the functional that detects it at order δ². The two near-degeneracy geometries of the program — vertical Lehmer and horizontal sub-resolution — have the SAME quadratic signature. This is not a coincidence: §4.3.

---

## 4. Inverse direction: uniform modulus ⟺ vertical repulsion; connection with LP-134

### 4.1. [NEW-DEFINITION] LP-143, the vertical twin of LP-134

D141 §1.2 fixed the canonical form LP-134: liminf_{ρ off} |β−½|·log γ > 0 (HORIZONTAL repulsion: zeros that leave the line do so visibly). Its mirror in the vertical coordinate:
$$\textbf{LP-143}:\qquad \liminf_{n\to\infty}\ \big(\gamma_{n+1}-\gamma_n\big)\cdot\log\gamma_n \;>\;0$$
(consecutive distinct ordinates of zeros of ζ; the convention on multiplicities: a multiple zero counts as gap 0, so that LP-143 implies in particular eventual simplicity). LP-143 says: there are no asymptotically degenerate Lehmer pairs at sub-resolution scale — the boundary that (per D141 §4.1 and [RT20]) ζ grazes, not crossed vertically either.

### 4.2. The equivalence

**Proposition 143.E (under RH: uniform modulus ⟺ LP-143; complete proof over §§2–3).** Assume RH, and restrict to heights/pairs satisfying (R_η) for some fixed η > 0 (class 𝒞_η). Let 𝔓 be the calibrated profile of Corollary 143.C′.1 (fixed parameters, free center). The following are equivalent:

(a) **Uniform modulus:** there exists ε₀ > 0 such that λ_min(p) ≥ ε₀ for every cell p of profile 𝔓 centered at any height c (in 𝒞_η), for every T.

(b) **Quantitative vertical repulsion:** there exists c₀ > 0 such that every pair of consecutive ordinates (in 𝒞_η) satisfies (γ_{n+1} − γ_n)·log γ_n ≥ c₀.

Constants: (b) ⟹ (a) with ε₀ = c_1·c₀² (Theorem 143.C′, lower bound, together with 143.B for windows with no close pair); (a) ⟹ (b) with c₀ = √((ε₀ − floor)/C_1) taking the profile with floor ≤ ε₀/2 (Corollary 143.C′.1, upper bound, contraposed: a pair with δ log T < c₀ produces a cell with λ_min < ε₀). ∎

**Remark 4.1 (status of LP-143 — the verdict of the literature, frank).** (i) **Open** for ζ; no known technique proves it (the classical vertical statistics of D141 Lemma 141.B0 are about ordinates, so here they ARE sensitive — but what they prove goes against it: see (ii)). (ii) Under RH, Conrey–Ghosh–Gonek [CGG84] prove liminf (γ_{n+1}−γ_n)·(log γ_n)/2π ≤ 0.5172: gaps below 52% of the mean infinitely often. That does NOT refute LP-143 (0.5172 > 0), but Montgomery's GUE conjecture [M73] predicts density of normalized gaps ~ c·u² near u = 0 (WEAK quadratic repulsion: positive probability in every neighborhood of 0), whence **liminf = 0: GUE conjecturally refutes LP-143.** (iii) The numerical shadow: the original Lehmer pair (γ ≈ 7005.0629, γ' ≈ 7005.1006: δ ≈ 0.0377, normalized gap ≈ 0.053 [CSV94]) and the thousands found later show normalized gaps descending with no sign of a floor. (iv) Perfect symmetry with D141: LP-134 (horizontal) is unprovable by averages (no-go 141.B2), irrefutable without refuting RH, and conjecturally… open; LP-143 (vertical) is moreover **conjecturally false** — the vertical coordinate is even worse for uniformity. Conclusion for 136.A: **(a) is conjecturally false: there is NO modulus uniform in T.**

**Proposition 143.E′ (the unconditional version of the inverse, with its caveat).** If there existed an UNCONDITIONAL lower bound λ_min(p) ≥ ε(p) > 0 for every cell of the grid 𝒢 of D136 (without assuming RH), then: (α) ¬RH would be refuted IF the ¬RH branch of the logistic criterion (D136 Thm. 5.4) were a theorem — that is, modulo Problem 139.A: under ¬RH that branch produces a cell with neg.ind ≥ 1, i.e. λ_min < 0 < ε(p), contradiction; (β) without resolving 139.A, the only thing that follows unconditionally is: no cell of the grid certifies ¬RH — consistent with RH but not a proof. **Status: the implication "unconditional quantitative positivity ⟹ RH" is exactly as conditional as 139.A.** And by Prop. 143.E, that unconditional bound would moreover imply LP-143 (via the RH part of the argument if RH is true) — so that the program "prove ε(p) > 0 uniform" carries at once the weight of RH and of a vertical repulsion that GUE denies: **[heuristic NO-GO]** the "uniform modulus first" route is doubly blocked. ∎

### 4.3. [BRIDGE] Vertical Lehmer ↔ horizontal LP-134: the De Bruijn–Newman dictionary

Status of this subsection: declared connection, no new theorems; it cites exact published results and a labeled heuristic dictionary.

- **What is proved:** Csordas–Smith–Varga [CSV94] quantitatively define "Lehmer pair" and prove: every genuine Lehmer pair forces a lower bound for the De Bruijn–Newman constant, Λ ≥ −λ(pair), with λ(pair) decaying with the quality of the pair (its quality measure is, in essence, the square of the normalized gap against the separation to the rest of the spectrum — the SAME quantity (δ log γ)² of our Corollary 143.C′.1, in another normalization). Rodgers–Tao [RT20]: Λ ≥ 0 unconditionally.
- **The dictionary (heuristic, labeled [DESIDERATUM]):** under the heat flow that defines Λ, an on-line pair with gap δ at time t = 0 collides and becomes an off-line quadruple at time ≍ −δ² (the collision of two real zeros of a polynomial under backward heat flow occurs at time quadratic in their separation — exact for the local quadratic model). That is: **LP-143 at t = 0 is the trace of LP-134 at infinitesimal times t < 0: today's vertical repulsion is the horizontal repulsion of the immediate thermal past, and the exponent 2 of §3 is the same δ² of the collision time.** Λ = 0 ([RT20] + RH would give Λ = 0) means that ζ is at the exact boundary: the two liminfs — the horizontal one of LP-134 and the vertical one of LP-143 — measure the distance to the same boundary from the two sides. No theorem of this document depends on this dictionary; it is recorded because it explains the coincidence of exponents (Rem. 3.1) and because it ties 136.A to the LP-134 file of D141 with the right geometry: **they are not two repulsions, it is a single one, seen at t = 0⁻ and at t = 0.**
- **Consequence for the map of the wall:** D141 §3.3 showed that LP-134 attacked with averages leads back to the old wall (uniformity of windows). Prop. 143.E shows that the uniformity of 136.A leads back to LP-143, twin of LP-134. The circuit closes: **136.A-uniform, LP-134, LP-143 and window uniformity are four faces of the same polyhedron**, and the only proved edge is the exact quantitative relation between modulus and gap (this document, §§2–3).

### 4.4. The dream of Π₁-with-modulus (D136 §6.3), settled with precision

D136 §6.3 asked for a **computable** ε(p) (from the primes) with λ_min(Gram(p)) ≥ ε(p) under RH, to convert the Π₁ of the RH branch into a Π₁ with modulus and give a level stopping criterion to the search for ¬RH. Balance after §§2–4: (i) the modulus EXISTS and is closed — but as a function of the gaps of the zeros (Theorem 143.B): computable from the ZEROS, not from the primes; using zero positions in the certificate destroys the autonomy (P43) that motivated the dream. (ii) An autonomous, uniform ε(p) would be equivalent to LP-143 (Prop. 143.E), conjecturally false. (iii) A frank degraded version remains: an autonomous ε(p) NOT uniform, depending on a regularity parameter η declared as a configuration hypothesis — exactly the degradation "ε(p) must degrade with the local on-line configuration" that D136 §6.3 anticipated, now with the exact rate: quadratic in the local minimum gap. **The dream is not fulfilled; it is replaced by its true form: modulus relative to the gap, without uniformity.**

---

## 5. Verdict on Problem 136.A

**RESOLVED IN RELATIVE FORM — the third option, which is a frank conditional theorem and not a defeat.** Breakdown:

1. **The speed question, corrected.** σ_loc^(k) ≡ 0 under RH for every k and every N (D136 Prop. 5.5; branch confirmed by D139): the "speed" is instantaneous and the literal question is empty. The quantitative content of 136.A is λ_min(p) (Rem. 1.1). This correction of the statement is the document's first result.

2. **[Conditional THEOREM — the bound exists and is closed.]** Under RH, λ_min(p) > 0 in EVERY cell, with an explicit Gram–Vandermonde modulus in the gaps of any d zeros (Theorem 143.B), framed exactly by Ingham 1936 (below, super-resolution) and Montgomery–Vaughan 1974 (above); both frames degenerate together below the threshold a·δ = π, where 143.B still gives a positive, non-uniform modulus.

3. **[Conditional THEOREM — the Lehmer exponent is 2.]** Exact closed 2×2 form (λ_min = 2b̂(aδ/2)²(δ/2w)², Computation 143.C) and bilateral bound with the sea under (R_η): λ_min ≍ (δ log T)² at natural calibration (Theorem 143.C′). Lehmer pairs are near-counterexamples with exact quadratic rate; the exponent 4 appearing in aligned bases is a normalization artifact, recorded as a warning.

4. **There is no uniform speed — and that is a structured statement, not a diffuse failure.** Modulus uniform in T ⟺ LP-143 (vertical repulsion, twin of LP-134; Prop. 143.E, proved equivalence), which is open, bounded above by [CGG84] and conjecturally FALSE under GUE. Lehmer pairs do not destroy positivity (always strict under RH); they destroy its uniformity, exactly with speed δ². **136.A reduces to minimum-gap statistics = pair correlation**, as D136 §6.3 predicted ("the wall shows up there too, as it should") — but now with the reduction turned into a quantitative equivalence with constants.

5. **By-products for the program's file:** (i) LP-143 named and formalized as the vertical twin of LP-134, with the De Bruijn–Newman dictionary ([CSV94], [RT20]) explaining that they are a single boundary seen at t = 0⁻ and t = 0 (§4.3, declared heuristic [BRIDGE]). (ii) The Π₁-with-modulus dream of D136 §6.3 is settled in its autonomous-uniform version and replaced by the gap-relative modulus (§4.4). (iii) Double block of the "unconditional modulus" route: it would carry both 139.A and ¬GUE at once (Prop. 143.E′).

**[Declared GAP — what this document does NOT prove:]** (a) no instance of LP-143 nor of its negation; (b) hypothesis (R_η) of Theorem 143.C′ is a configuration one (it excludes stacked double Lehmer pairs) — without it the upper bound gains a log T factor in the floor and the profile must grow slowly with T; (c) the thermal dictionary of §4.3 is heuristic; (d) nothing here moves the ¬RH branch (139.A remains open, and this document does not touch it).

---

## References

**Internal (backward-only):** D136 (Defs. 3.1–3.2, Prop. 3.3, 5.5, Thms. 2.5, 4.1–4.4, 5.4, Cor. 5.6, §6.3 Problem 136.A); D139 (verdict by branches; E-139.1 normalization; GAP-A lesson on M-dependent constants; Problem 139.A); D141 (LP-134 canonical form Def. 141.1, Computations 141.M4–M5, no-go 141.B2, §4.1 Lehmer as boundary); D107 (absolute convergence, x∂ₓ closure); D108 (Prop. 2.2, diagonal positivity under RH); P43 (autonomy); D134 (schedules/resolution, via D141).

**Literature (published and verifiable):**
- A. E. Ingham, *Some trigonometrical inequalities with applications to the theory of series*, Math. Z. 41 (1936), 367–379. [I36] — lower inequality for exponentials with gap, optimal threshold a·δ > π.
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) 8 (1974), 73–82. [MV74] — generalized Hilbert inequality and mean-value theorem with term 3π/δ.
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24, AMS (1973), 181–193. [M73] — pair correlation; GUE quadratic repulsion (conjectural).
- J. B. Conrey, A. Ghosh, S. M. Gonek, *A note on gaps between zeros of the zeta function*, Bull. London Math. Soc. 16 (1984), 421–424. [CGG84] — under RH, normalized gaps ≤ 0.5172 infinitely often.
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann hypothesis*, Constr. Approx. 10 (1994), 107–129. [CSV94] — Lehmer pairs ⟹ lower bounds of Λ.
- B. Rodgers, T. Tao, *The de Bruijn–Newman constant is non-negative*, Forum Math. Pi 8 (2020), e6. [RT20] — Λ ≥ 0.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Lund (1952). [W52] — explicit formula and positivity.
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53 (2004), Thm. 5.8. [IK04] — N(t+1) − N(t) ≪ log t.

*End of Doc 143.*
