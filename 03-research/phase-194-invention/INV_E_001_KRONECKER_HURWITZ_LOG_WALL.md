# INV_E_001 — Kronecker–Hurwitz residue: Λ-weights, the ∂log wall, and the balance term (track E)

Track E.


## 0. Corpus / index check
- ROUTES-TRIED-INDEX (all files): "Hurwitz" appears only as the Hurwitz zero-counting theorem (ES-17, P36-1, P76). "Kronecker" appears as Diophantine/Kronecker-line (DIOPH, CA_C_002, Q2). Selberg trace appears as L31 (Hejhal analogue) and NG-B1. The **class-number family Σ H(4n−t²)** and the **Eichler–Selberg trace formula** are not indexed, except as the unindexed seed at the end of INV_D_001 (README l.373).
- Grid part5/6/12/18 and crossword: no hit on Hurwitz class numbers or Eichler–Selberg. CA_A_006 (metaplectic Eisenstein, abscissa transport) is NO-GO and is not used here.
- New reason: the object is new. It is the elliptic (class-number) term of the SL₂/Mp₂ trace formula, not the hyperbolic term (Connes L05) and not the Eisenstein term (CA_A_006).

## 1. The family (CITED)
(KH) Σ_{t²≤4n} H(4n−t²) = 2σ(n) − Σ_{dd'=n} min(d,d') =: 2σ(n) − M(n)   (Kronecker, Hurwitz).
(ES_k) For weight k ≥ 2 on SL₂(ℤ): tr T_n|S_k = −½ Σ_t P_k(t,n) H(4n−t²) − ½ Σ_{dd'=n} min(d,d')^{k−1} + δ_{k=2}σ(n). Here P_k(t,n) = (ρ^{k−1}−ρ̄^{k−1})/(ρ−ρ̄) with ρ+ρ̄ = t and ρρ̄ = n (Eichler–Selberg, Zagier's form).
Polynomial weights in t give the whole family of (ES_k). For k = 4, 6, 8, 10, 14 the space S_k = 0, so the class-number sums are exactly the divisor sums σ_{k−1} plus the min^{k−1} terms (CITED).

Dirichlet series (PROVED, termwise):
- Σ σ_{k−1}(n) n^{−s} = ζ(s)ζ(s−k+1).
- Σ M_k(n) n^{−s}, with M_k(n) := Σ_{dd'=n} min(d,d')^{k−1}, equals 2Σ_d d^{k−1−s} ζ_{≥d}(s) − ζ(2s−k+1), where ζ_{≥d}(s) = Σ_{e≥d} e^{−s}.
This is **not** an Euler product. The min-term is the only non-multiplicative piece; it is the d ≈ d' balance.

## 2. How Λ comes out of this family

**Lemma E1 (the only exact Λ-extraction is a log-derivative; PROVED).** Let L denote the operator f ↦ f·log. L is a derivation of Dirichlet convolution. Then
  (σ_{k−1})^{*−1} * L(σ_{k−1}) = Λ·(1 + id^{k−1}),
which is −∂_s log[ζ(s)ζ(s−k+1)]. Here (σ_{k−1})^{*−1} = μ * (μ·id^{k−1}).
*Proof.* L(f*g) = Lf*g + f*Lg, and 1^{*−1} * L1 = μ * log = Λ. ∎
With (KH), for k = 2:
  Λ(n)(1+n) = ½ Σ_{de=n} σ^{*−1}(d) log e · [H_tot(e) + M(e)],   where H_tot(e) := Σ_t H(4e−t²).   (E1)
The left side carries Λ with exact weights. The right side depends on the class numbers **nonlinearly**, because σ^{*−1} is the convolution inverse of a functional of the H-data. This is Identity 5 of INV_C_001 transplanted to the elliptic family.

**Theorem E2 (∂log wall; NO-GO in a declared class).**
Class 𝓒_0 consists of Dirichlet series obtained from the Kronecker–Hurwitz/ES family by the following operations: linear combinations, Dirichlet convolutions and convolution inverses of the data series, and multiplication by elements of ℂ(s). No log-multiplication (∂_s) is allowed. On the same-argument part of the family (the Euler parts ζ(s)^{±1}, with the shifted factor frozen as a coefficient), every element of 𝓒_0 lies in ℂ(s)(ζ(s)).
Then −ζ'/ζ = Σ Λ(n) n^{−s} ∉ ℂ(s)(ζ(s)).
*Proof.* If −ζ'/ζ = R(ζ) with R ∈ ℂ(s)(X), then ζ' − ζ·R(ζ) = 0 is an algebraic differential equation for ζ over ℂ(s). This contradicts Hölder–Hilbert–Ostrowski (ζ is hypertranscendental; CITED). ∎
Status:
- PROVED, given the CITED theorem, for the same-argument class.
- ARGUED for the full class with the shifts ζ(s−a) and the cusp L-series L(f,s) adjoined. This needs difference-differential independence of the shifts. Ostrowski-type results exist, but the exact citation was not checked.
Consequence: Λ is reachable from this family **only** through ∂_s (log-multiplication). It cannot come out linearly with universal coefficients. The route "Λ by hand" (writing Λ = c * σ with c := Λ*σ^{*−1}) is linear but inserts Λ into its own coefficients, so it is tautological.

**Corollary E3 (the shift is visible).** Through (E1), the weight Λ(n)(1+n) mixes the ζ(s) wall with the ζ(s−1) wall. Every Λ obtained from (ES_k) carries a spurious twin Λ(n)n^{k−1}, whose polar set is shifted by k−1. To isolate Λ alone, one must cancel the twin. That again needs the log-derivative of ζ(s−k+1) separately, i.e. the same wall (PROVED from E1).

## 3. Exact identity with 𝔞_T on 𝒫_T (PROVED, bookkeeping)
For g ∈ 𝒫_T with F = g*g̃,
  𝔞_T(g) = Arch_T(g) − Σ_{n<e^{2T}} n^{−½}(1+n)^{−1} F(log n) · ½ Σ_{de=n} σ^{*−1}(d) log e [H_tot(e) + M(e)].
- The d ≈ n/d balance enters **only** through M(e). The class-number part H_tot carries the additive t² ≤ 4e.
- **Free positivity (CITED):** H ≥ 0, hence H_tot ≥ 0 and M ≤ 2σ. Hecke positivity: tr(T_n*T_n) = Σ_f |λ_f(n)|² ≥ 0, which by the Hecke relations is again linear in the ES data. Petersson norms are ≥ 0. None of these survives the convolution with σ^{*−1}, which changes sign (μ*(μ·id)). So the free positivity is lost exactly at the ∂log step.
- **Information content:** Dirichlet inversion is a bijection on comb weights, so every weight vector w admits such a representation. The identity is comb-generic.

## 4. Self-check
- **thm:shape.** (A) The free positivities (H ≥ 0, Hecke traces, Petersson) are comb-free, or they are statements about σ_{k−1}, not about the Λ-comb. Sign-blind. (B″) The identity in §3 holds for every weight vector after Dirichlet inversion, so it is bookkeeping only.
- **Problem (R).**
  - (1) Λ is exact only via ∂log (Theorem E2): FAILS as an operation of the class.
  - (2) Euler product: σ is Euler, M is not (balance). The functional equation is only through the modular form side, not jointly with the comb.
  - (3) Linear in Λ after inversion; quadratic positivity (Petersson) is not transported: FAILS.
  - (4) Not on the zero side: PASSES.
  - (10)/(11) The family exists for every level and nebentypus, and the H-positivity is shared. It does not separate ζ: FAILS.
- **REF-D test.** The only positive statement that would close the gap is "Arch_T − (inverted Hurwitz comb) ≥ 0 on 𝒫_T". This is 𝔞_T ≥ 0 rewritten: **REF-D**.

## 5. Verdict
- PROVED: Lemma E1, identity (E1), the §3 identity, Corollary E3, and Theorem E2 in the same-argument class (from a CITED theorem).
- CITED: (KH), (ES_k), Hölder–Hilbert–Ostrowski.
- ARGUED: Theorem E2 with shifts and cusp forms adjoined.
- REF-D: the sign statement.
- **NO-GO (class 𝓒_0):** linear/convolution/ℂ(s) extraction of Λ from the Kronecker–Hurwitz/Eichler–Selberg family.
- **Surviving residue (OPEN, small):** M(n) = Σ min(d,n/d) is the unique non-Euler, balance-carrying piece. Its Dirichlet series 2Σ_d d^{1−s}ζ_{≥d}(s) − ζ(2s−1) is an incomplete-zeta (Hurwitz-type) object. Whether a (ℕ,+,·) inequality at d ≈ n/d on M can survive σ^{*−1} is unexamined. A priori it inherits the sign-changing μ*(μ·id) and so is likely sign-blind (ARGUED).
