# Doc 124 — Is Connes–Consani's Weil positivity the missing Hodge index?

**Program:** Riemann Hypothesis — Phase 40: close G1/G2.
**Prerequisites:** Doc 123 (C-cok/C-rank bifurcation of the square obstruction; tolerance repairs C-cok but NOT C-rank; in dim 2 the C-rank datum is an intersection form = G2); Doc 122 (Request 122.A: a positive polarization on H¹ of the square is missing; CC's duality is Pontryagin duality, it does not give a signature); Doc 119 (R-WEIGHT, R-SIG realizations (i)/(ii)/(iii); the non-circularity test R-NC, clauses NC1–NC4).

**Labeling discipline (absolute rule):** **[DATA]** = read in source this session (PDF in `papers-referencia/`, via the Read tool), with exact citation paper + page/theorem. **[CALCULATION]** = my own derivation, shown. **[GAP]** = what is missing, precisely. **[CONJECTURE]** / **[UNVERIFIED]** = as indicated. NEVER "proved" about anything geometrically new. A false victory is worse than a failure. If the answer to the central question is "cannot be determined in source," that is a valid result — it is declared with the exact datum that would be missing.

---

## 0. Executive summary

This document fixes the geometric template of "which positivity is the right one" (Hodge index / Castelnuovo–Severi over a surface), reads in source the two Connes–Consani papers provided, and applies the R-NC test to decide whether the Weil positivity those papers contain IS the G2 ingredient (intersection positivity, geometric, reusable) or is spectral positivity (the quadratic form of the explicit formula evaluated on test functions, RH-equivalent and hence circular for our purpose).

Source identification of the two papers:
- **2310.18423v2 = Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators — semilocal adelic operators*** (4 May 2024) **[DATA]**. It is a paper about **spectral operators**: cyclic pairs, the prolate operator, the Sonine space as the negative part of the spectrum, Hermitian Jacobi matrices, the semilocal Hardy–Titchmarsh transform, de Branges spaces.
- **2307.06748v1 = Connes–Consani, *On the metaphysics of F₁*** (13 Jul 2023) **[DATA]**. It is a paper about **algebraic foundations / F₁**: rings of 𝕊[μ_{n,+}]-polynomials, the spectrum of the sphere 𝕊 as the absolute base, the RR of Z̄ (genus of Spec Z = 0); it contains a discussion of the counting distribution N(u) on the explicit-formula side and names (in a footnote) the cohomology H¹(**C**) as infinite-dimensional.

**Verdict of the central question (§6): (c) a geometric FRAGMENT of the spectral side, with the global part frankly (a) circular/spectral.** The only positivity with sign content in the corpus read is the Weil positivity of the spectral side (the Weil quadratic form Q_n / the semilocal trace formula), which is RH-equivalent upon globalizing: FAILS NC3. BUT there is an unconditional fragment —the **stability of the semilocal Sonine space under amplification** (CCM Thm 4.6) and **archimedean positivity in a window**— that passes NC1 and overgenerates (NC2 partially); that fragment is the closest thing to "a form defined on a subspace," but **it is not an intersection form on divisor classes of the square**: it is a restriction of the prolate operator (an object on the spectral side of the archimedean place), not of NS(X×X). Consequence for G2: **the ingredient does NOT exist in the corpus read**, not even as a geometric-intersection fragment; it exists in fragment form only on the **spectral side**, and extending it does not give the Hodge index but the global Weil positivity = RH.

---

## 1. Template [DATA + CALCULATION]: which positivity is "the right one"

### 1.1. The classical Hodge index theorem (projective surface)

**[Classical DATA, via Doc 119 §2.3 realization (ii), not re-verified in source this session — it is context].** Let S be a smooth projective surface over an algebraically closed field, NS(S) its Néron–Severi group, ρ = rk NS(S) the Picard number. The intersection form
$$ (\,\cdot\,,\,\cdot\,):\ \mathrm{NS}(S)\otimes\mathbb R \times \mathrm{NS}(S)\otimes\mathbb R \to \mathbb R,\qquad (D,D')\mapsto D\cdot D' $$
is symmetric, non-degenerate (by Poincaré duality in H²), and its **signature is (1, ρ−1)**: it has exactly ONE positive direction. The Hodge index theorem states: on the orthogonal complement (H·)^⊥ of an ample class H (H²>0), the intersection form is **negative definite**. Equivalently, for D with D·H=0 one has D·D ≤ 0, with equality only if D≡0 numerically.

**[CALCULATION] What type of positivity this is, precisely.** It is the positivity of an intersection form on a subspace of divisor classes (codimension 1 on a surface). Its defining features:
1. **It is bilinear over ℝ, symmetric, on ONE space** (NS(S)⊗ℝ), not between a group and its dual.
2. **Its definiteness is restricted to a subspace** ((H)^⊥), determined by an ample class (a polarization H).
3. **It is geometric**: D·D' is computed from the geometry of S (intersection of curves / degrees), **independent of any L-function or zero position**.

That is exactly the profile of **realization (i)/(ii) of R-SIG** (Doc 119 §2.3): "a bilinear/Hermitian form with involution on a space" + "a polarization (operator L) that makes it definite on each piece." Intersection-positivity.

### 1.2. How Weil uses it for RH over function fields

**[Classical DATA, via Doc 119 §2.3 (i), internal citations Wei48; Mattuck–Tate 1958; Grothendieck 1958].** For a curve C/𝔽_q, Weil considers the surface S = C×C. The geometric Frobenius has a graph Γ_F ⊂ C×C, a correspondence. The **Castelnuovo–Severi** inequality is the positivity of the intersection form restricted to the subspace of NS(C×C) generated by correspondences modulo the "trivial" classes (horizontal/vertical fibers):
$$ Z\cdot Z' \ \text{defines a form with signature controlled by the Hodge index over } \mathrm{NS}(C\times C). $$
Applied to Z = Γ_F and its iterates/transposes, positivity forces the **Cauchy–Schwarz inequality** that gives |α| = √q for the Frobenius eigenvalues α in H¹ — which is RH for curves. The logical chain is:
$$ \underbrace{\text{positivity of the intersection form in NS(C×C)}}_{\text{geometric, Hodge index/Castelnuovo}} \ \Longrightarrow\ \underbrace{|\alpha|=\sqrt q}_{\text{purity of weights = RH}}. $$

**[CALCULATION] The decisive point for our program.** What makes this NOT circular —and hence a **proof** rather than a reformulation of RH— is that the starting positivity is a theorem about **ALL correspondences of the surface**, proved by surface geometry (Hodge index), which **ignores what curve C is and where its points are**. This is precisely what the R-NC test formalizes:
- **NC2 (overgeneration):** Castelnuovo holds for every divisor of C×C, not only for Γ_F.
- **NC4 (two-worlds test):** in the ¬RH world, an eigenvalue with |α|≠√q would produce a class with a self-intersection of the forbidden sign, visible in the form without localizing the zero.

**This fixes EXACTLY which positivity is "the right one":** **intersection-positivity** —Q(D,D)≥0 for D in a subspace of divisor classes of a surface, proved by geometry, independent of zero positions—. Any other positivity, in particular the positivity of the quadratic form of the explicit formula evaluated on test functions, is **spectral-positivity** and is RH-equivalent (it is literally Weil's criterion), hence circular for building G2.

### 1.3. The operative dichotomy (what R-NC decides)

**[CALCULATION] I summarize the discriminator.**

| | INTERSECTION-positivity (GOOD) | SPECTRAL-positivity (CIRCULAR) |
|---|---|---|
| object | Q(D,D)≥0, D∈ subspace of NS(X×X) | W(f⋆f̃)≥0, f test function |
| space | divisor/correspondence classes | test functions in the Weil class |
| origin of positivity | geometry of the surface (Hodge index) | = Weil's criterion = RH |
| dependence on zeros | none | total (IT IS the RH condition) |
| R-NC | passes (NC1,NC2,NC4 with content) | FAILS NC3 (it is MW-1 of the catalog) |
| reusable for G2 | yes | no (renaming RH is not proving it) |

The question of the document is: which of the two columns does the Weil positivity that CC actually prove in these papers belong to?

---

## 2. Reading in source — paper 1: CCM, *Zeta zeros and prolate wave operators* (2310.18423v2)

### 2.1. What the paper is and what positivity it handles

**[DATA]** (2310.18423v2, Abstract, p.1, verbatim): *"We integrate in the framework of the semilocal trace formula two recent discoveries on the spectral realization of the zeros of the Riemann zeta function by introducing a semilocal analogue of the prolate wave operator. The latter plays a key role both in the spectral realization of the low lying zeros of zeta —using the positive part of its spectrum— and of their ultraviolet behavior —using the Sonin space which corresponds to the negative part of the spectrum."*

**[DATA]** (ibid., Introduction §1, p.2): *"there exists a property P(n), involving only the Euler factors for primes smaller than n, and whose validity for all n is equivalent to RH. This is derived from Weil's positivity criterion which involves the quadratic form Q_n defined using the Riemann–Weil explicit formulas applied to test functions with support in the compact symmetric interval [1/n, n]. Furthermore, the semilocal trace formula of [7] gives, for each n, a Hilbert space theoretic framework in which the Weil quadratic form Q_n becomes the trace of a simple operator theoretic expression."*

**Structural reading [CALCULATION on DATA].** The positivity named is **explicitly** the **positivity of Weil's criterion** — the quadratic form Q_n of the explicit formula applied to tests supported on [1/n, n]. The paper itself presents it as **RH-equivalent** ("whose validity for all n is equivalent to RH"). This places it, from the outset, in the SPECTRAL/CIRCULAR column of §1.3. The paper does NOT prove the positivity of Q_n (that would be RH): it **realizes** it as the trace of an operator, in order to *study* it with operator-theoretic tools.

### 2.2. (a) What exact positivity, over what space, with what quantifier

**[DATA]** (ibid., §1 p.2–3): the source of Weil positivity (at the archimedean place) is *"the Hilbert space representation of the scaling group"*; the radical of the Weil quadratic form is the **range of the map ℰ** over the Schwartz space S(ℝ)^{ev}_0, ℰ(f)(u) := u^{1/2}∑f(nu) (equation cited on p.2). And the connection with positivity: *"with the Weil functional —which is automatically positive for a selfadjoint operator— ... The conditioning, by the radical of the Weil quadratic form, that worked for the scaling operator in the infrared case will be implemented automatically by the orthogonality of the positive and the negative part of the spectrum of the semilocal prolate operator"* (p.3).

**[CALCULATION] The quadratic form is Weil's; the space is of test functions; the quantifier is "for all f in S(ℝ)^{ev} (or of restricted support)".** There is, in this passage, no form on divisor classes whatsoever. The positivity the paper achieves **unconditionally** is the trivial "tr of a self-adjoint operator ≥ 0" (W(f⋆f̃) = ⟨Tf,f⟩ with T≥0 since it is a square/self-adjoint); the content of RH is that this positivity **coincides** with Q_n, which the paper does not prove (and cannot without RH).

### 2.3. (b) The method

**[DATA]** The method is entirely spectral/operator-theoretic:
1. **Cyclic pairs and the prolate operator** (§2, p.5–6): a cyclic pair (D,ξ), D self-adjoint, ξ a cyclic vector; formal prolate operator ω(D,ξ,λ) := −D² + λ²N, with N the degree operator of orthogonal polynomials (Def. 2.2, p.6). **[DATA]**
2. **Archimedean case = classical prolate operator** (§3): W_λ = −𝕊² + 2πλ²(4N+1) − 1/4 (eq. (5), p.4), with 𝕊 the self-adjoint generator of the dilation group in L²(ℝ)^{ev}. The Jacobi matrix of 𝕊 has entries 𝕊_{n,n+1} = i√((n+1/2)(n+1)) (p.4). **[DATA]**
3. **Sonine space** = negative part of the prolate spectrum (Abstract, and §4.5 Def. 4.4, p.20): S_λ(𝕂,α) := {f∈L²(𝕂) : f(x)=0 & 𝔽_α f(x)=0 ∀|x|<λ}. **[DATA]**
4. **Semilocal Hardy–Titchmarsh transform** (§4): construction of the semilocal cyclic pair (𝕊, ξ_S) over L²(X_S)^{K_S}, with the measure dm_S(s) = |∏_{v∈S} L_v(½−is)|² ds (eq. (6),(48)). **[DATA]**
5. **Stability of the semilocal Sonine space** (§4.7, Thm 4.6, p.23) and connection with de Branges spaces (§4.8). **[DATA]**
6. **Metaplectic representation** (§5): the prolate as an element of the enveloping algebra of sl(2,ℝ) via the metaplectic representation of the double cover of SL(2,ℝ). **[DATA]**

That is: **Sonine + scaling + prolate**, exactly the three ingredients the §4 objective names as fragment candidates. NONE is an intersection form.

### 2.4. (c) Class of test functions

**[DATA]** The starting Weil positivity lives on **restricted-support test functions** [1/n, n] (the Q_n, §1 p.2). The semilocal Sonine space S_λ(X_S, α) is parametrized by λ>0 (Def. 4.5, p.21) and consists of functions in L²(X_S)^{K_S} that vanish together with their Fourier transform on |x|<λ — that is, a **support condition** (ultraviolet). The central stability result is:

**[DATA]** (Thm 4.6, p.23): *"Let S∋∞ be a finite set of places and λ>0. Then the map θ_S is a hilbertian isomorphism of the Sonin spaces θ_S : S_λ(ℝ,e_∞) → S_λ(X_S, α)"*. And the key remark (p.5): *"This result suggests that the obtained invariantly defined Sonin space should, when suitably equipped with a prolate type operator, play the role of the sought for Weil cohomology."*

**[CALCULATION] This is as close as the corpus gets to "an invariant candidate object for a Weil cohomology."** But note: it is a Hilbert space (Sonine) with a prolate operator, **not** a group of divisor classes with an intersection form. The authors' phrasing is **programmatic** ("should ... play the role"), not a theorem that it does.

### 2.5. R-NC applied to the positivity of 2310.18423

**[CALCULATION] I apply the test to the Weil positivity Q_n / trace-formula handled by the paper.**

- **NC1 (externality).** The construction of the cyclic pair, the prolate, and the Sonine space is functorial from adeles/scaling; it does not mention the zeros in its definition. **PASSES.** (Same as Doc 119 §4.3's report for the CC candidate.)
- **NC2 (overgeneration).** The archimedean positivity (that of the self-adjoint operator, ⟨Tf,f⟩≥0) holds for every f∈S(ℝ)^{ev}, not only for the one encoding ζ — it overgenerates trivially, but **trivially**: any form "⟨Tf,f⟩ with T≥0" overgenerates, and that contributes no geometric content. Overgeneration with content (à la Castelnuovo: "holds for every correspondence of a surface by a surface theorem") **is NOT present**, because there is no surface nor correspondences. **PASSES only in the trivial sense; FAILS in the sense with content.**
- **NC3 (non-reduction to catalogued RH-equivalent positivities).** This is where the determination lies. The positivity whose content matters —that Q_n ≥ 0 for every n— is **literally** Weil's criterion = **MW-1** of the catalog (Doc 119 §4.3, NO-GO-LIST). The paper itself says so: "whose validity for all n is equivalent to RH" (§2.1 above, [DATA]). The semilocal version (the trace formula of [7] that turns Q_n into a trace) is its uniformization = **MW-6** (Doc 119 §4.3). **FAILS NC3 outright.**
- **NC4 (two-worlds test).** In the ¬RH world, does the positivity fail for a reason computable from the object without localizing the zero? No: to know whether Q_n<0 one must evaluate the Weil form, whose sign IS the zero position (inaccessible binarity, Doc 119 §4.3, NC4 / Doc 108). **FAILS NC4.**

**[CALCULATION] Conclusion for paper 1.** The positivity of 2310.18423 is **SPECTRAL-positivity**: FAILS NC3 and NC4. It is the circular column of §1.3. **It is not the Hodge index.** It is the operator-theoretic realization of Weil positivity, RH-equivalent.

---

## 3. Reading in source — paper 2: CC, *On the metaphysics of F₁* (2307.06748v1)

### 3.1. What the paper is

**[DATA]** (2307.06748v1, Abstract, p.1, verbatim): *"we investigate the general notion of rings of 𝕊[μ_{n,+}]-polynomials and relate this concept to the known notion of number systems. The Riemann-Roch theorem for the ring ℤ of the integers that we obtained recently uses the understanding of ℤ as a ring of polynomials 𝕊[X] in one variable over the absolute base 𝕊, where 1+1 = X+X². The absolute base 𝕊 ... thus turns out to be a strong candidate for the incarnation of the mysterious F₁."* Dedicated to Yuri Manin.

The paper is about **foundations**: F₁, balanced number systems (X=3, X=−2), the arithmetic site over 𝕊[X], the spectral sphere 𝕊 as the absolute base. **It is NOT a paper about positivity nor about quadratic forms.**

### 3.2. (a) What positivity / what relevant content

The only structure close to "positivity" is the **counting distribution** N(u) of §2 (Adelic and topos theoretic incarnation of C):

**[DATA]** (ibid., §2, eq. (2.4)–(2.5), p.4): N(u) = (d/du)φ(u) + κ(u), φ(u) := ∑_{n<u} n Λ(n), where **κ(u) is exactly the distribution that appears in the Riemann–Weil explicit formula**: ∫₁^∞ κ(u)f(u)d*u = ∫₁^∞ (u²f(u)−f(1))/(u²−1) d*u + cf(1), c = ½(log π + γ). And: *"One shows that the distribution N(u) is positive on (1,∞)"* (p.4), with the formula in terms of zeros (2.5): N(u) = u − d/du(∑_{ρ∈Z} order(ρ) u^{ρ+1}/(ρ+1)) + 1.

**[CALCULATION] What positivity this is.** "N(u) positive on (1,∞)" is a positivity of a **counting distribution on the explicit-formula side** — its kernel κ is the Weil kernel. It is not a quadratic form on a space of classes; it is the positivity of the Hasse–Weil analogue of the counting function N(q), motivated by "N(1) should be −∞" (zero density). It is on the spectral/arithmetic side, and in fact the paper uses it to connect with the trace formula of [5] (Connes 1999) and the adele class space X_Q (eq. (2.6)). **There is no intersection form.**

### 3.3. The decisive datum on H¹(C) and the RR

**[DATA]** (ibid., §2, footnote 3, p.3, verbatim): *"the number of zeros of ζ_Q is infinite, and so is the dimension of the (mysterious) cohomology H¹(**C**)."* And (§1, p.2): the RR of Z̄ *"shows that the genus of Spec Z is zero."*

**[CALCULATION] Consequence for G2/G1.** This paper **confirms from another source** the base datum of Doc 119 §2.4: dim H¹(**C**) = ∞ (the sought cohomology is NOT total finite-dimensional). And the RR that CC have (that of Z̄, genus 0) is a **dimension-1** RR (a "curve" Spec Z, genus 0), **not** a surface RR with an intersection form. The paper contains NO dim-2 ingredient (no square, no NS(X×X), no Hodge index). The phrase "absolute Descartes powers Spec Z × ⋯ × Spec Z" (Manin quote, p.3) is flagged as an **open question**, not as a constructed object.

### 3.4. R-NC applied to paper 2

**[CALCULATION]** There is here no positivity-candidate-for-G2 to test: the positivity of N(u) is that of a distribution of the explicit formula.
- **NC3:** "N(u) positive on (1,∞)" + "N(1)=−∞ reflecting zero density" (p.4, [DATA]) is manifestly on the explicit-formula / zero-density side — interderivable with the spectral side. **FAILS NC3** as a geometric candidate.
- In any case, **paper 2 does not propose this positivity as a purity ingredient**; it uses it as a conceptual bridge NCG↔topos↔tropical. It is not a candidate for G2.

**Conclusion paper 2:** it contributes no intersection-positivity. It contributes (i) confirmation of dim H¹=∞, (ii) that CC's RR is genus 0 / dim 1, (iii) that the square (Spec Z × Spec Z) is an open question, not an object. Consistent with Doc 123 §1.1.

---

## 4. The central question, decided

### 4.1. Statement of the question (reminder)

Is the Weil positivity that CC prove (or contain as a fragment) the Hodge-type **intersection-positivity** on divisor classes of the square (the G2 ingredient), or is it **spectral-positivity** (the explicit-formula form on tests, RH-equivalent, circular)?

### 4.2. Determination

**[CALCULATION, the document's decisive determination].**

The positivity **with sign content** in the corpus read —the only one that could give a signature— is the **spectral-side Weil positivity**:
- In 2310.18423: the Weil quadratic form Q_n / its realization as the trace of the prolate (§2.1–2.2). FAILS NC3 and NC4 (§2.5).
- In 2307.06748: the positivity of the counting distribution N(u) (§3.2). FAILS NC3 (§3.4), and is not even proposed as a purity ingredient.

**Neither is an intersection form on divisor classes.** There is, in neither paper:
- a group of divisor classes of a surface (NS(X×X)) **[DATA: absent in both; the square is an open question, 2307.06748 §1 p.3]**;
- a symmetric bilinear form on ONE space of classes with signature (1, ρ−1) **[DATA: absent]**;
- an ample class / polarization H on such a space **[DATA: absent — confirms Doc 122 §5.3 and Doc 119 §4.3]**.

**Therefore the answer to the central question is: CC's positivity is SPECTRAL-positivity, NOT intersection-positivity.** It is the circular column of §1.3. For our purpose (building G2) it is, in its global form, **circular**: globalizing semilocal Weil positivity is MW-1/MW-6 = RH.

### 4.3. Why it is not intersection-positivity, categorically precise

**[CALCULATION].** There is a structural reason, not an accidental one, anchored in Doc 122:
- Intersection-positivity lives on a **space of classes with a symmetric bilinear form** (NS(S)⊗ℝ with D·D').
- CC's duality structure is **Pontryagin duality group↔dual** (Doc 122 §1.3, [DATA] 2205.01391 Thm 5.3), which **is not a form on a space** and **has no symmetry character** without an external polarization (Request 122.A).
- The positivity of 2310.18423 is **⟨Tf,f⟩≥0 with T≥0 on a Hilbert space of tests/Sonine** — a positive definite form on functions, **not** a signature (1,ρ−1) form on classes. It is the positivity of an operator, not the signature of an intersection.

The two things are categorically distinct: an intersection form **has one positive direction and ρ−1 negative ones** (indefinite signature, this is what gives the Hodge index); CC's spectral positivity is **definite** (the whole spectrum positive, or the positive/negative split of the prolate). The object G2 needs is **indefinite with controlled signature**; what CC have is **definite (semidefinite)**. They do not coincide.

---

## 5. Is there a non-circular geometric fragment in the method? (objective §4)

CC's method is Sonine + scaling + prolate (§2.3). The fragment candidate is the **unconditional semilocal case**: the positivity/stability for restricted support, which is UNCONDITIONAL.

### 5.1. What exactly the unconditional fragment is

**[DATA]** Two unconditional pieces in the corpus:
1. **Archimedean positivity in a window** (via Doc 119 §4.3 / Doc 100, [internal DATA]; the external source is 2006.13771, not re-read this session): W_∞(g⋆g̃)≥0 for tests supported on (½,2). Unconditional.
2. **Stability of the semilocal Sonine space** (2310.18423 Thm 4.6, p.23, [DATA read this session]): the semilocal Sonine space S_λ(X_S,α) is **independent of S** (hilbertian isomorphism θ_S under amplification of the finite set of places). Unconditional. And the programmatic phrase (p.5): *"the obtained invariantly defined Sonin space should ... play the role of the sought for Weil cohomology."*

### 5.2. Is that fragment the restriction of an intersection form to a subspace?

**[CALCULATION, the requested analysis].** The hypothesis to test (objective §4): *if the small-support unconditional semilocal positivity were the restriction of an intersection form to a subspace, extending it to full support would be the global Hodge index = G2, and we would know the ingredient exists in fragment form.*

I analyze. The small-support unconditional positivity:
- Is on a **space of functions** (tests with support in a window / Sonine with a support condition on |x|<λ), **not** on a space of divisor classes. **[DATA: Def. 4.4/4.5, p.20–21.]**
- Is a **definite** positivity (⟨Tf,f⟩≥0, or the positive/negative orthogonality of the prolate), **not** an indefinite form of signature (1, ρ−1). **[CALCULATION §4.3.]**
- Its **extension to full support** is **exactly** the global Weil positivity = Weil's criterion for all n = **RH** (MW-1). **[DATA: 2310.18423 §2.1, "validity for all n equivalent to RH".]**

**[CALCULATION] Fragment verdict.** The unconditional semilocal positivity is **NOT the restriction of an intersection form to a subspace**. It is the restriction of **spectral-side Weil positivity** to small support (where the sum over primes is finite/dominated, which is why it is unconditional — matching the automatic locality of Doc 99/Doc 119 §3.3). Extending it does **not** give the Hodge index: it gives the global Weil positivity = RH. That is: **the fragment exists, but it is a fragment of the SPECTRAL side, not of the geometric-intersection side.** Its extension falls into NC3 (it is MW-6→MW-1), not into a Hodge index.

The deep reason [CALCULATION]: what makes the fragment unconditional is that at small support **the sum over primes does not diverge** (the Mertens tail of Doc 105 does not appear; automatic locality Doc 99). That is an **analytic-arithmetic** fact (how many primes fall in the window), not a **geometric** fact (it is not that an intersection form is definite on a subspace because of an ample class). Unconditionality comes from truncating the explicit formula, not from the geometry of a surface. That is why its extension is RH, not Hodge.

### 5.3. Exact contrast with Castelnuovo (what a genuine geometric fragment would look like)

**[CALCULATION].** A genuine geometric fragment would look like this: a symmetric bilinear form Q on a subspace V ⊂ "NS of the square," with Q **negative definite** on V by a theorem saying "V = (ample class)^⊥ and the surface has the Hodge index." Extending it = removing the restriction to V = Hodge index over all of NS. That would pass NC2 with content (holds for every correspondence) and NC4 (a bad eigenvalue gives a forbidden self-intersection, visible).

CC's fragment **does not have this form**: there is no V of classes, there is no ample class, the positivity is definite (not indefinite with a (H)^⊥), and the extension is RH not Hodge. **The existing fragment is of the wrong type.**

---

## 6. Verdict

### 6.1. The central question

**[CALCULATION] Verdict: (c) a geometric fragment of the spectral side — with the global part frankly (a) circular/spectral.** Breakdown:

- The **global** Weil positivity that CC handle (Q_n for all n; its semilocal uniformization) is **(a) circular/spectral**: FAILS NC3 (it is MW-1) and NC4. It is the circular column of §1.3. **[DATA + CALCULATION §2.5.]**
- There is an **unconditional fragment** (archimedean positivity in a window; stability of the semilocal Sonine space, Thm 4.6): it passes NC1 and overgenerates (NC2 partially, trivially). But **it is not intersection-positivity**: it is spectral-positivity restricted to small support. Its extension is RH, not the Hodge index. **[CALCULATION §5.2.]**
- In no sense is it **(b) geometric/intersection**: there is no intersection form, nor divisor classes of the square, nor ample class/polarization in the corpus read. **[DATA §4.2.]**

Therefore, in the a/b/c/d classification of the objective: **it is NOT (b); the global part is (a); the unconditional fragment is (c) but on the spectral side (not geometric-intersection)**. Component (d) "undeterminable in source" applies only to one thing: whether the invariant semilocal version of the Sonine space, *equipped with a prolate operator not yet built*, "should play the role of the sought for Weil cohomology" (2310.18423 p.5) **will come** to have an intersection form — that is an open program declared by the authors themselves, **undeterminable in the current source** (the paper leaves it "for a forthcoming paper," Abstract).

### 6.2. Consequence for G2: does the ingredient exist, exist in fragment, or not?

**[CALCULATION] The G2 ingredient (the intersection form / Hodge index on the square) does NOT exist in the corpus read — not even as a geometric-intersection fragment.**

- What exists in fragment form is on the **spectral side** (unconditional Weil positivity in a window), whose extension is RH (circular), not Hodge.
- The geometric structure G2 needs —a space of classes with an indefinite symmetric bilinear form of signature (1,ρ−1) and a polarization that makes it definite on (H)^⊥— **is absent**, confirming via a third independent route the findings of Doc 122 (missing positive polarization, Request 122.A) and Doc 123 (missing intersection norm = C-rank = G2). **Three independent derivations, same verdict.**

This **refutes** (frankly, avoiding the false victory that objective §5 warned was of maximum risk) the optimistic hypothesis that "CC's Weil positivity IS ALREADY the missing Hodge index." It is not. It is spectral-positivity, RH-equivalent. That CC realize it operator-theoretically (prolate, Sonine, Jacobi) is valuable mathematics for *studying* the Weil form, but **it does not turn it into a geometric intersection form**, and hence does not provide G2.

### 6.3. What would remain to be read / requested (concrete list)

1. **2006.13771** (*Weil positivity...*) was NOT read in raw source this session (only via Doc 100/120). Confirm verbatim the statement of the archimedean positivity and its support; check whether anywhere CC phrase it as "intersection theory of divisors on the square" with a bilinear form on classes (Doc 120 §4.4 reports the phrase "intersection theory ... in development"). **[Pending; low risk of changing the verdict: the MW catalog already classifies it as MW-6.]**
2. **The "forthcoming paper" on the Weil representation of SL₂(𝔸_S)** announced in 2310.18423 (Abstract; §1 p.3) as "second candidate for the semilocal prolate operator": if that candidate carries an **indefinite form with a signature** (not just the prolate's positive/negative split), it would be the first hint of something Hodge-like. Undeterminable today. **[Request to CC / await publication.]**
3. **Whether the invariant semilocal Sonine (Thm 4.6) admits a natural bilinear form** —not the positive-definite Hilbert product, but an indefinite form coming from duality— that gives a signature. It is the version, in this language, of Request 122.A. **[Internal question to CCM, decidable by an expert in their formalism.]**
4. **The verbatim text of Yoshitomi's Example 6.5** was already read this session (1001.0448v3, p.34): it confirms r(D)=1≠r(D')=0 with isomorphic H⁰. Closes §6.3 point 1 of Doc 123: the reference "[yoshi]" IS Yoshitomi, arXiv:1001.0448, *Generators of modules in tropical geometry*. The rank definition is r(D)=max{r∈ℤ≥−1 : U(D,r)=∅} (p.32, Baker–Norine/Gathmann–Kerber style), a linear-equivalence invariant via ord(f,P) — **not a module invariant**, and Thm 2.7 gives r(D)≤dim(M)−1. **[DATA, already closed.]**

---

## 7. Synthesis and candor

No new geometric statement has been proved here. What has been **read in source** (the two CC PDFs + Yoshitomi) and **calculated**:

- **Template fixed:** the "right" positivity for G2 is intersection-positivity (an indefinite symmetric bilinear form of signature (1,ρ−1) on divisor classes of a surface, negative definite on (H)^⊥ by the Hodge index), which is how Weil proves RH for curves via Castelnuovo–Severi. The "wrong" (circular) positivity is the spectral positivity of the Weil form on tests.
- **Paper 1 (CCM, prolate/Sonine):** SPECTRAL-positivity. The quadratic form is Weil's Q_n, declared RH-equivalent by the authors themselves. FAILS NC3 and NC4. Method: cyclic pairs, prolate, Sonine, Jacobi, semilocal Hardy–Titchmarsh. No intersection object whatsoever.
- **Paper 2 (CC, metaphysics of F₁):** contains no positivity-candidate-for-G2; the positivity of N(u) is on the explicit-formula side. Confirms dim H¹(**C**)=∞ and that CC's RR is genus 0 / dim 1; the square is an open question.
- **Fragment:** there is unconditional small-support positivity (archimedean window; stability of the Sonine space), but it is a fragment of the **spectral side**, not of intersection; its extension is RH (MW-1), not the Hodge index. It is the wrong type of fragment.
- **Verdict (c) with global (a):** CC's positivity is spectral/circular globally, a spectral fragment in its unconditional part, **never geometric/intersection**. **The G2 ingredient does not exist in the corpus read**, not even in intersection-fragment form.

**The point of obstruction IS the result, once again:** what CC have is Weil positivity realized operator-theoretically (positive definite, on functions), not an intersection form (indefinite, on classes, with a signature). The categorical difference between "positive operator on tests" and "signature (1,ρ−1) form on NS" is exactly the difference between the circular column and the good column of §1.3 — and between RH-reformulated and RH-proved. Triple coincidence with Doc 119 (R-NC), Doc 122 (missing polarization), and Doc 123 (missing intersection norm = C-rank): the G2 ingredient still has no candidate in the corpus.

---

## References

**Primary source read this session, via Read over PDFs in `papers-referencia/`):**
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators — semilocal adelic operators*, arXiv:2310.18423v2 (4 May 2024) — Abstract, §1 (Introduction: Q_n, Weil's criterion RH-equivalent, radical = range of ℰ, source of positivity = scaling group rep.), §2 (cyclic pairs, prolate ω=−D²+λ²N, Def. 2.2), §3 (W_λ=−𝕊²+2πλ²(4N+1)−¼, eq. (5); Jacobi matrix of 𝕊), §4 (semilocal: Hardy–Titchmarsh, eq. (36)–(58); local Sonine Def. 4.4 and semilocal Def. 4.5; Prop. 4.5 σ_p; Thm 4.6 Sonine stability; de Branges §4.8), §5 (metaplectic). **[DATA]**
- A. Connes, C. Consani, *On the metaphysics of F₁*, arXiv:2307.06748v1 (13 Jul 2023) — Abstract (RR of ℤ, 𝕊 as F₁, genus of Spec Z=0), §1 (balanced systems X=3, X=−2), §2 (arithmetic site; N(u) eq. (2.4)–(2.5) with Weil kernel κ, "positive on (1,∞)," N(1)=−∞; X_Q eq. (2.6); Thm 2.8; footnote 3 p.3: dim H¹(**C**)=∞), §3 (𝕊[μ_{n,+}], Eilenberg–MacLane HA). **[DATA]**
- S. Yoshitomi, *Generators of modules in tropical geometry*, arXiv:1001.0448v3 (2 Apr 2011) — §1 (T-module M=H⁰(C,O_C(D)); r(D) not a module invariant), §6 (Tropical curves: ord(f,P) Prop. 6.1–6.3; divisors; Prop. 6.4 M is a T-module; r(D)=max{r∈ℤ≥−1:U(D,r)=∅} p.32), Thm 2.7 (r(D)≤dim(M)−1, proof p.33), **Example 6.5 (p.34: C genus 1, C' genus 2, H⁰(C,O(D))≅H⁰(C',O(D')) but r(D)=1≠r(D')=0)**. Identifies "[yoshi]" as 1805.10501. **[DATA]**

**Internal (backward-only):** Doc 119 (R-SIG realizations (i)/(ii)/(iii); R-WEIGHT(a)/(b); R-NC NC1–NC4; NO-GO-LIST MW-1/MW-6; order R-SIG≺R-FIN; §2.4 dim H¹=∞); Doc 122 (CC's duality = Pontryagin, without symmetry character; Request 122.A polarization/self-pairing; §5.3 negative search for a polarization in the corpus); Doc 123 (C-cok/C-rank bifurcation; C-rank = intersection norm = G2; Example 6.5 as the root; tolerance repairs C-cok not C-rank); Doc 121/120/100/105/99/72/108 (via the above).

**Classical (context, via Doc 119 §2.3, not re-verified in source this session):** Hodge index theorem on surfaces, signature (1,ρ−1) of NS(S); Castelnuovo–Severi on NS(C×C); Weil 1948; Mattuck–Tate 1958; Grothendieck 1958.

*End of Doc 124.*
