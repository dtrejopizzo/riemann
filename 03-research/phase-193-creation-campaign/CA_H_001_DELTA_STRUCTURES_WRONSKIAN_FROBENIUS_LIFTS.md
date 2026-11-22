# CA_H_001 — Buium δ-structures on ℤ, on the Dirichlet ring and on schemes over ℤ: the arithmetic Wronskian, the δ-logarithm of ζ, and the Frobenius-lift bridge (seeds H1, H3, H8)

Phase 193. Pen and paper; no numerics. no equivalence with any statement about
another object is used.
**No sign contact. No negative value for ζ.**

Question of the memo. A p-derivation is the canonical algebraic object that mixes + and · (it is "the derivative with respect to p").
In the function-field proofs, positivity (Mason–Stothers, Stepanov, Weil on C×C) comes from a derivation or from the graph of
Frobenius. Does Buium's δ_p (on ℤ, on the ring of Dirichlet series, on test vectors, or on a scheme over ℤ) supply a +/·-genuine
input that reads the window form? Answer: no, and the memo proves at which step each reading dies.

## 1. δ_p on ℤ: uniqueness, valuation drop, carry, height growth
**Definition.** A p-derivation on a ring A is a map δ: A → A with δ(1) = 0,
  δ(a+b) = δa + δb + C_p(a,b),  C_p(a,b) := (a^p + b^p − (a+b)^p)/p = −Σ_{0<i<p} p^{−1}binom(p,i)a^ib^{p−i},
  δ(ab) = a^pδb + b^pδa + pδaδb.
Equivalently φ(a) := a^p + pδ(a) is a ring endomorphism lifting Frobenius mod p (Joyal; Buium, *Arithmetic Differential Equations*,
AMS 2005, Ch. 2 — CITED).

**Proposition 1.1 (uniqueness on ℤ; PROVED).** ℤ has exactly one p-derivation for each p, δ_p(n) = (n − n^p)/p.
*Proof.* φ is a ring endomorphism of ℤ, hence the identity; ℤ is p-torsion free, so pδ(n) = n − n^p determines δ. Fermat gives
integrality. ∎

**Lemma 1.2 (valuation drop at p only; PROVED).** Let n = p^e u, p ∤ u.
(i) If e ≥ 1, v_p(δ_p n) = e − 1. (ii) If e = 0, v_p(δ_p n) = v_p(n^{p−1} − 1) − 1 ≥ 0. (iii) For a prime q ≠ p, v_p(δ_q n) ≥ e.
*Proof.* (i) δ_p n = p^{e−1}u − p^{ep−1}u^p and ep − 1 > e − 1. (ii) δ_p n = n(1 − n^{p−1})/p. (iii) δ_q n = n(1 − n^{q−1})/q and q is a
p-unit. ∎
So δ_p imitates d/dt *at the point p only*: it lowers the multiplicity at p by one, and no δ_q lowers it at p.

**Lemma 1.3 (height grows by the factor p; PROVED).** For n ≥ 2, n^p/(2p) ≤ |δ_p n| ≤ n^p/p. Hence log|δ_p n| = p·log n − log p + O(1).
*Proof.* n^p − n ≥ n^p/2 ⇔ n^{p−1} ≥ 2. ∎
Contrast (function field): deg(f′) ≤ deg f − 1. Over ℤ the archimedean absolute value sees the p-derivative as p times larger.

**1.4 Carries (seed H3 folded here; PROVED).** The defect of additivity of δ_p is exactly the carry polynomial C_p of the Witt vector
addition law in the first ghost component (Buium Ch. 2, CITED). The window form is carry-blind in the following precise sense: the
form object is the pair (Γ-factor, comb (Λ(n))_{n<e^{2T}}), and Λ(n) is a function of the exponent vector of n (monoid data, G1) times
log of the norm; no quantity C_p(a,b) for a pair of integers enters the definition (P46 def:W, eq:form). Carries enter only if a
construction introduces sums a + b of indices, which happens in the window form only through the archimedean proximity kn ≈ m (CA_H_002).

## 2. The arithmetic Wronskian and the Mason–Stothers template
Function-field template (CITED, Mason 1984 / Stothers 1981; Snyder's proof): for coprime a + b = c in k[t], W := ab′ − a′b = ac′ − a′c ≠ 0,
deg W ≤ deg a + deg b − 1, and W is divisible by ∏_P P^{e_P − 1} over the prime factors of abc; hence Σ(e_P − 1)deg P ≤ deg a + deg b − 1.

**Definition 2.1.** For integers a, b put W_p(a,b) := a^pδ_pb − b^pδ_pa.
**Proposition 2.2 (PROVED).** (i) W_p(a,b) = ab(a^{p−1} − b^{p−1})/p.
(ii) If p^e ‖ a with e ≥ 1 and p ∤ b, then v_p(W_p(a,b)) = e − 1 (the derivative-like divisibility).
(iii) **Mason identity fails exactly by the carry:** for c = a + b, W_p(a,c) − W_p(a,b) = a·C_p(a,b).
(iv) For coprime 1 ≤ b < a, log|W_p(a,b)| ≥ log(ab) + (p−2)log a − log p.
*Proof.* (i) Substitute δ_p x = (x − x^p)/p. (ii) v_p(ab) = e, a^{p−1} − b^{p−1} is a p-unit. (iii) By (i),
W_p(a,c) − W_p(a,b) = a[(c−b)a^{p−1} − c^p + b^p]/p = a(a^p + b^p − c^p)/p. (iv) x^n − y^n ≥ x^n − (x−1)^n ≥ x^{n−1} for integers x > y ≥ 1. ∎
**Corollary 2.3 (no degree drop; PROVED for this construction, ARGUED for the class).** Let S ⊇ {p : p | abc}. Any integer W_S built as a
product or ℤ-combination of the W_p, p ∈ S, that is divisible by p^{e_p−1} for every p ∈ S has "cost" log|W_S| ≥ Σ_{p∈S}((p−1)log a − log p)
in the product case, while the "gain" is Σ_p(e_p − 1)log p ≤ log(abc). By Lemma 1.2(iii) the divisibility at p can only come from δ_p, so
every p | abc must be paid for separately, each at height ≈ p·log a (Lemma 1.3). The function-field inequality deg W ≤ deg a + deg b − 1
has no analogue: the archimedean place charges each p-derivative its full Frobenius degree. *Label:* product case PROVED; "every
polynomial expression in a, b and the δ_p a, δ_p b has height ≳ Σ_p p log a unless it vanishes" ARGUED (cancellations not excluded by
a proof).
**Reading for row D.** Mason–Stothers concerns individual triples a + b = c, not the comb. Its natural target would be the near-identities
kn = m + h of Near (CA_H_002). Corollary 2.3 says the derivative template cannot even reproduce the classical inequality over ℤ, because
the cost is archimedean. This is the H1 analogue of G1_B9 Lemma 3 (characteristic 0 kills Stepanov's amplification).

## 3. δ-structure on the Dirichlet ring: δ_p ζ and the δ-logarithm of ζ
Let D_ℤ be the ring of formal Dirichlet series Σ_{n≥1} a_n n^{−s}, a_n ∈ ℤ (Dirichlet convolution), i.e. the completed monoid algebra
ℤ[[ℕ^×]].
**Proposition 3.1 (PROVED).** φ_p(f)(s) := f(ps), i.e. a_n n^{−s} ↦ a_n (n^p)^{−s}, is a ring endomorphism of D_ℤ lifting Frobenius mod p;
hence δ_p f := (f(ps) − f(s)^p)/p is a p-derivation on D_ℤ. The φ_p commute (φ_pφ_q = φ_{pq}): D_ℤ is a Λ-ring.
*Proof.* φ_p is induced by the monoid endomorphism n ↦ n^p, so it is a ring map. In D_{𝔽_p}, (Σa_nn^{−s})^p = Σa_n^p(n^{−s})^p (multinomial
coefficients vanish mod p), a_n^p ≡ a_n and (n^{−s})^p = (n^p)^{−s}. ∎
**Proposition 3.2 (δ_p ζ; PROVED).** δ_p ζ = Σ_n p^{−1}(1[n is a p-th power] − d_p(n)) n^{−s}, with integral coefficients, where d_p(n) is the
number of ordered factorizations n = n₁⋯n_p.
*Proof.* ζ(ps) = Σ1[n = m^p]n^{−s}, ζ^p = Σd_p(n)n^{−s}. Integrality: the cyclic group ℤ/p permutes ordered p-factorizations; orbits have
size p or 1, and the fixed points are the constant tuples, which exist iff n is a p-th power (then exactly one). ∎
**Proposition 3.3 (δ-logarithm of an Euler product; PROVED).** For f ∈ 1 + (higher terms), put Ψ_p(f) := p^{−1}log(φ_p f / f^p) ∈ D_ℚ (Buium's
δ-character of G_m, applied in D). Then Ψ_p(fg) = Ψ_p f + Ψ_p g, and
  Ψ_p(ζ) = −Σ_{N = q^j, p ∤ j} (Λ(N)/log N) N^{−s},   −(d/ds)Ψ_p(ζ) = −Σ_{N = q^j, p∤j} Λ(N)N^{−s} = ζ′/ζ(s) − ζ′/ζ(ps).
So the δ-logarithmic derivative of ζ has the comb Λ^{(p)} := Λ·1[N is not a p-th power] (for p = 2: the prime powers with odd exponent).
*Proof.* log ζ = Σ_N (Λ(N)/log N)N^{−s}. For N = q^j, φ_p sends q^{−js}/j to q^{−pjs}/j = p·q^{−(pj)s}/(pj), so p^{−1}φ_p log ζ =
Σ_{N=q^{j'}, p|j'}(Λ(N)/log N)N^{−s}. Subtract log ζ. For the second form, Σ_{N p-th power}Λ(N)N^{−s} = Σ_nΛ(n)n^{−ps} = −ζ′/ζ(ps). ∎
**Corollary 3.4 (Ψ_p is monoid-functorial; PROVED).** Ψ_p acts on each local Euler factor by the same rule (delete the exponents divisible by
p), so Ψ_p of any Euler product over any free monoid with a norm is computed identically. In particular Ψ_p(ζ_K) and Ψ_p(ζ_B) (Beurling)
are the corresponding exponent deletions. The δ-structure of D_ℤ is induced by the monoid endomorphisms n ↦ n^p of ℕ^×: **the "+" in
Buium's δ is the addition of coefficients, never the addition of the index monoid ℕ.** Hence every construction on D_ℤ is G1-type
(survives O11/O12 in its formal content) unless it adds ℤ-Poisson data, which is additive-only (H0(b)).
**Proposition 3.5 (the δ-split of the window form; PROVED).** For F ∈ P_T,
  𝔞^Λ_T(F) = 𝔞^{Λ^{(p)}}_T(F) − Σ_{n: n^p < e^{2T}} 2Λ(n)n^{−p/2} Re c_F(p log n),
and for p ≥ 3 the subtracted term is bounded in absolute value by 2|ζ′/ζ(p/2)|·‖F‖² (absolutely convergent, abscissa p/2 > 1); for p = 2 it is
the comb of ζ(2s) at abscissa 1 on dilated autocorrelations (CA_A_006 Remark 3).
*Proof.* v_{n^p} = 2Λ(n^p)n^{−p/2} = 2Λ(n)n^{−p/2}; |c_F| ≤ ‖F‖². ∎
**Where it dies.** (a) The split is a convex/affine decomposition of the comb: CA_B_007/008 (REF-D unless a piece is certified
independently). (b) The piece Λ^{(p)} is the comb of ζ(s)ζ(ps)^{−1/p}, which has branch points (at s = 1/p and at the zeros of ζ(ps)); it has no
functional equation of conductor 1, so prop:shape-inputs(i) applies to any deduction from it. (c) For p ≥ 3 the moved piece is a bounded
functional of the weights, (R)(5), and is O(1) while λ_A(T) ≤ 4·10⁹Te^{−15.449T}: a termwise transfer (lem:shape-misc). (d) Every piece is
comb-only, so O7 survives.

## 4. δ-structure on test vectors (Adams operations) — the derivation acting on the form
On real finitely supported s on ℕ put ψ_p s (supported on p-th powers, (ψ_p s)_{m^p} = s_m) and s^{*p} (p-fold Dirichlet convolution); for
integer s, δ_p s := (ψ_p s − s^{*p})/p is integral (Prop 3.1 on the polynomial P_s). Let 𝔸_𝖡(s) := Σ s_ms_k𝖡(log m − log k).
**Lemma 4.1 (PROVED; valid for every even continuous 𝖡).** (i) 𝔸_𝖡(ψ_p s) = 𝔸_{𝖡(p·)}(s), and 𝖡 is PD iff 𝖡(p·) is PD.
(ii) P_{s^{*p}} = P_s^p, so 𝔸(s^{*p}) = (1/2π)∫F̂₀²|P_s|^{2p}[m − κ]dτ (the p-th moment family of CA_D_001 Thm 1′).
(iii) 𝔸(δ_p s) = p^{−2}[𝔸(ψ_p s) − 2𝔸(ψ_p s, s^{*p}) + 𝔸(s^{*p})].
*Proof.* (i) log(m^p/k^p) = p log(m/k); dilation preserves positive definiteness. (ii) prop:AM(ii). (iii) bilinearity. ∎
**Where it dies.** (i) is self-similarity of the target (the problem at scale p is the problem), true for every comb: (B″). (ii) is FE-generic
(CA_D_001 Thm 1″). (iii) has no sign: the cross term is ∫P_s(pτ)·conj P_s(τ)^p·(m − κ)dν₀, indefinite. Integrality of δ_p s gives |entries| ≥ 1,
which is no information for a form that is not yet known to be positive. **No δ-calculus on tests produces an inequality.**

## 5. The bridge to gap G-F (coordinator): a polarized object built from global Frobenius lifts
Over 𝔽_q the Weil form lives on C×C and the correspondence is the graph of Frobenius. A ℤ-analogue built from the semiring would be a
scheme X/ℤ with lifts φ_p of Frobenius at every p (a δ-structure for every p; with commutation, a Λ-structure in Borger's sense,
CITED: J. Borger, *The basic geometry of Witt vectors I*, Adv. Math. 2011), and the graphs Γ_{φ_p} ⊂ X ×X as correspondences.
**Proposition 5.1 (no Frobenius lift on curves of genus ≥ 2; degree argument PROVED, non-vanishing CITED).** Let X be a smooth proper curve of
genus g ≥ 2 over W₂(k), k perfect of characteristic p. Then X admits no lift of the absolute Frobenius.
*Proof.* A lift F̃ satisfies F̃*(dx) = d(x^p + py) = p(x^{p−1}dx + dy), so dF̃ is divisible by p and (1/p)dF̃: F*Ω¹_{X₁} → Ω¹_{X₁} is a morphism of
line bundles on the special fibre. It is non-zero: it induces the inverse Cartier isomorphism on the cohomology sheaves of the de Rham
complex (Deligne–Illusie, Invent. Math. 89 (1987), CITED). A non-zero map L → L′ of line bundles on a curve forces deg L ≤ deg L′, i.e.
p(2g−2) ≤ 2g−2, false for g ≥ 2. ∎
**Proposition 5.2 (genus 1; CITED).** There is no elliptic curve over ℤ (Tate; no elliptic curve over ℚ has good reduction everywhere). Over
ℤ[1/N], a Frobenius lift mod p² on an elliptic curve exists only at ordinary primes (Serre–Tate canonical lift); for a CM curve the lifting
endomorphisms exist only at primes split in the CM field. So no elliptic curve carries Frobenius lifts at all p.
**Proposition 5.3 (the semiring geometrized is content-free; PROVED).** G_m = Spec ℤ[x^{±1}] = Spec ℤ[(ℤ,+)] with ψ_n: x ↦ x^n (multiplication by n
on the character group (ℤ,+)) is a Λ-scheme; it is (ℤ,+,·) acting on itself. On the compactification P¹ × P¹ with fibre classes f₁, f₂
(f₁·f₂ = 1, f_i² = 0), the graph of x ↦ x^n has class Γ_n = n f₁ + f₂, the diagonal Δ = f₁ + f₂, and
  Γ_n·Δ = n + 1 = #{0, ∞} + #μ_{n−1} exactly;  Γ_n = ((n+1)/2)H + ((n−1)/2)(f₁ − f₂), H = f₁ + f₂, (f₁ − f₂)² = −2.
The primitive part has negative square, as Hodge index demands, and the trace formula has no middle term (H¹(P¹) = 0): the
"fluctuation" of this object is identically zero, and its counting function n − 1 contains no prime.
*Proof.* Γ_n·f₂ = n (preimages of a point), Γ_n·f₁ = 1; fixed points of x ↦ x^n on P¹ are 0, ∞ and the (n−1)-th roots of unity, all
transversal for n ≥ 2 away from char | n−1 (over ℂ). ∎
**Corollary 5.4 (NO-GO for the declared class; PROVED from 5.1–5.3).** Class 𝒦_δ: polarized objects X/ℤ (smooth proper, of relative
dimension 1, or products of such) whose correspondences are graphs of global Frobenius lifts at every p. Every member with H¹ ≠ 0 is
excluded by Props 5.1–5.2, and the members that exist (toric, genus 0) have zero primitive trace content. So **𝒦_δ supplies no object
for gap G-F (a) + (c)**. Buium's way around Prop 5.1 is to replace X by its arithmetic jet spaces J^n_p(X) and to use δ-characters
ψ: E(ℤ_p) → ℤ_p (CITED, Buium Ch. 7). These are p-adic and per prime: the values lie in an unordered ring, so positivity cannot be
formulated in them (CA_F_001 condensed/ℚ_p verdict), and assembling them over all p is exactly what Lemma 1.3 charges at ∞.
Scope: 𝒦_δ requires lifts of Frobenius as morphisms. Correspondences that are not graphs (Hecke correspondences, the scaling
action of the adèle class space) are outside 𝒦_δ; they are MW-5/OT-5′ and are not reopened here.

## 6. Screens
| clause | §2 Wronskian | §3 δ-log split | §4 δ on tests | §5 𝒦_δ |
|---|---|---|---|---|
| Idx | new (G1_B9 Rem. 3.1 was HEURISTIC; now Cor 2.3) | new | new | partly MW-5, R175; new Props 5.1–5.3 |
| +/· genuine (H0) | yes, but triple-level (no comb) | no: Cor 3.4, monoid-functorial | no: (B″) | yes; content-free |
| (R)(3) | — | split = certificate-type | identity + C–S if anything | Hodge index = Gram (G0) |
| (R)(5) | — | ✗ bounded at p ≥ 3 | — | — |
| (R)(10) | — | ✗ G1 | — | — |
| (P3) | ✗ no form | ✗ comb-only | reads form ✓ but (B″) | — |
| O7 | — | survives | survives | — |
| O11/O12 | — | survive (Cor 3.4) | survive | — |
| FE-gen | — | survives (D_ℤ functorial) | survives | — |
| REF-D | — | CA_B_007/008 | self-similarity only | — |
| [crit] | — | ✗ O(1) moves | ✗ | — |
**Verdict.** H1/H3 DISCARDED after development: NO-GO (PROVED) for the Wronskian template in the product class, the δ-log split,
and the δ-calculus on tests. H8: NO-GO (PROVED from Raynaud-type degree argument + CITED inputs) for the class 𝒦_δ of polarized objects
built from global Frobenius lifts.

## 7. Self-review
1. *Is Prop 3.3 just a renaming of prime-power deletion?* Yes, and that is the point: Buium's δ-log on an Euler product is exponent
   deletion at every place, so its +/· content disappears on Euler products. The +/· mixture of δ_p lives in coefficient carries
   (Prop 3.2, d_p(n) mod p), which are congruences on integer coefficients; the window form is ℝ-linear in the comb and has no use for
   them unless an integrality gap is invoked (that is H7, a retry).
2. *Cor 2.3 is only for products.* Correct; labelled ARGUED for general expressions. Even a successful Mason analogue would bound
   individual triples, which is (B′) as an input to the comb, and abc-type bounds are far coarser than M^{−3}.
3. *Prop 5.1 cites the non-vanishing.* Yes (Deligne–Illusie). The degree inequality is proved here. The conclusion (no lift for g ≥ 2) is
   classical (Raynaud; also Buium's book, Ch. 7 introduction) and stated as such.
4. *Prop 5.3 on ℂ vs over ℤ.* The intersection numbers are those of P¹×P¹ over any field; the arithmetic (Arakelov) intersection of Γ_n
   with Δ adds archimedean Green terms log|x^n − x| integrated, plus heights of roots of unity (zero). Not computed; it cannot create an
   H¹. The claim "content-free" refers to the geometric primitive part, PROVED.
5. *Did I use any zero information or any equivalence?* No.
6. *Did I miss a δ-object that reads the form?* The form reads only (Γ-factor, comb); §3 handles the comb, §4 the tests, and the
   Γ-factor carries no δ-structure (Γ_ℝ is archimedean). Remaining: jet-space δ-characters, p-adic (§5). Area of H1 exhausted.
