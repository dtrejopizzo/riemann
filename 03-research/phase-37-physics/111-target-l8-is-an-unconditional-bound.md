# Doc 111 — Target L8: is an unconditional bound on the number of off-critical quadruples reachable?

**Phase 37 — Physics mode ·**
**Prerequisites:** Doc 108 (Prop. 2.3/2.5; "two worlds" Theorem 3.4; Conjecture 108-N and Theorem 4.3; §5; §8.1–8.2: κ_W ≤ C·n_W ⟹ m ≤ C/2); P43 (Principle 3.1; ledger L8; §6); Doc 98 (toy case m = 1: κ = 2, Prop. 6.1; Cor. 2.4); Doc 107 (Prop. 6.1); Doc 100 (semilocal positivity, MW-7); P35 (κ = 2m); P41; P42 (§6).
**Absolute rule:** no proof is fabricated; every step is a complete proof, a closed-form computation, or a declared GAP. No numerics or simulations. Backward-only citations; what is unverified is marked [NOT VERIFIED].

---

## 0. Executive summary

**The target.** Let m be the number of off-critical zero quadruples of ζ (Doc 98, Hypothesis T1:
each RH violation contributes a quadruple {½±δ±iγ₀}; m = 0 ⟺ RH; under ¬RH, m ∈ {1, 2, …}
∪ {∞}). Item L8 of the P43 ledger records: an unconditional bound κ_W ≤ C·n_W on
per-window indices would give m ≤ C/2 (Doc 108, Obs. 8.1) — a theorem **strictly weaker
than RH** ("at most C/2 exceptions") that would be historic even without resolving RH. This
document measures whether ANY finiteness bound on m is reachable, or whether "m finite" is
already behind the same wall as "m = 0".

**Findings, in order:**

1. **(§2) The unconditional inventory contains no theorem forbidding nonzero finite m, and
   cannot contain one without arithmetic.** It is proved (Prop. 2.2) that in the program's
   "physical" class (entire of order 1, functional equation, real symmetry — the class ℰ of
   the variational arc) there exist elements with exactly m quadruples for every finite
   m: any theorem "m ≥ 1 ⟹ m = ∞" must use the Euler product. No such theorem exists in
   the literature (§2.5). The region currently excluded in (δ, γ₀) is
   {γ₀ ≤ 3·10¹²} (Platt–Trudgian) ∪ {δ > ½ − c/((log γ₀)^{2/3}(log log γ₀)^{1/3})}
   (Korobov–Vinogradov); the proved partial positivities add nothing (§2.4).

2. **(§2.6) The full inventory is binary.** Every known theorem about off-critical zero
   counts produces either **0** (free regions) or **T^θ, θ > 0** (density): there is no
   statement producing a "finite nonzero count uniform in height". The binarity of the
   per-window index (Doc 108, Prop. 2.5) is a special case of a binarity of the whole
   inventory.

3. **(§3) The Siegel mechanism has NO analogue for quadruples of ζ.** Landau–Page–Siegel
   repulsion works because near s = 1 the positivity budget is **the simple pole — a global
   O(1) budget** — and two zeros cannot both consume it. For ζ itself: (a) the "Siegel
   zone" in the s-aspect (β near 1) **is already unconditionally zero-free** — the classical
   free region IS the pole→zero repulsion, via 3+4cos θ+cos 2θ ≥ 0; (b) in the interior of
   the strip the local positivity budget at height γ₀ is the archimedean sea ≍ log γ₀: **it
   grows**, there is no scarcity, no repulsion; (c) the cross term of two quadruples in the
   explicit formula, of size X^{δ₁+δ₂} < X, falls **below** the Montgomery–Vaughan error bar
   just like the diagonal terms X^{2δᵢ} < X, and its detection requires simultaneous
   resolution at two unknown frequencies: the pair looks **worse** than the single
   quadruple alone (anti-Siegel, §3.4).

4. **(§4) Turán gives no finiteness.** Power sums give lower bounds on the oscillation of
   ψ(x)−x forced by the quadruples (degrading exponentially in the number of terms); the
   contradiction would require an upper bound |ψ(x)−x| = o(x^{½+δ}), and by the classical
   reciprocal theorem (Landau/Ingham) that bound IS the quasi-RH one wanted to conclude:
   exact circularity. What remains is only finiteness in compact boxes,
   m(δ₀, Γ) ≤ N(½+δ₀, Γ) < ∞, already trivially given by density theorems; the entire
   non-triviality of L8 is uniformity in Γ (§4.3).

5. **(§5) The central count — exceptional windows vs. unconditional moments:**
   (a) statistics with an unconditional limit theorem (S(T), Selberg's CLT) are **blind**
   to the abscissa: a quadruple is indistinguishable, for S(t), from an on-line double zero
   at the same height (Lemma 5.1); Gaussian concentration does not bound m at all. (b) The
   statistic that does see it (second-order deficit) contributes per quadruple a signal
   ≍ X^{2δ} against an unconditional error bar O(X·log²X) in the Montgomery–Vaughan mean
   value: invisible for every δ < ½ and every m, **even m = ∞ of zero density**
   (Prop. 5.3). (c) Large values tolerate R ≪ T^{θ(δ)} exceptional windows with θ(δ) > 0
   strict for every δ < ½ — that IS the density theorem read backward; no finite moment
   brings the tolerance down to O(1); the uniform k → ∞ limit is the master quantifier
   again (§5.4). (d) The pigeonhole "m ≥ M ⟹ M windows with simultaneous deficit" does not
   break the circularity: the accumulated deficit M/log T stays below the error bar of
   every accessible mean value (§5.5).

6. **(§6) Synthesis — the budget/cost dichotomy.** A theorem m ≤ C requires a functional
   B with (P1) unconditional bound and (P2) uniform minimum cost c > 0 per quadruple. The
   whole inventory splits into two exclusive classes: bounded ones with vanishing cost
   (T_λ: cost 2δ²K_λ(γ₀) → 0, Doc 98 Cor. 2.4) and uniform-cost ones with RH-equivalent
   boundedness (κ_W: cost 2, uniform bound = RH, Doc 108 Prop. 2.5). The two historical
   precedents of "at most k exceptions" have exactly (P1)+(P2): Siegel (budget = order of
   the pole = 1) and Weil in function fields (budget = dim H¹ = 2g, finiteness BEFORE
   purity). L8 is the counting avatar of cohomological finite-dimensionality; the analysis
   has no O(1) budget with uniform cost available, and fabricating one from averages is the
   inversion of the quantifier.

**VERDICT: TARGET UNREACHABLE with the cataloged forms of argument** (§7), with the
precision that L8 does NOT collapse to RH: "m finite" remains logically strictly weaker
than RH (we neither prove nor does there exist "m ≥ 1 ⟹ m = ∞"), so the target remains
alive as an objective for a new mechanism — and §6 states exactly what form that
mechanism must take: a bounded global budget with minimum cost per quadruple.

---

## 1. The target: definitions and logical status

### 1.1. The parameter m

**Definition 1.1.** By the functional equation ξ(s) = ξ(1−s) and the reality of ξ on the
critical line (Schwarz reflection), every zero ρ = β+iγ with β ≠ ½ generates the quadruple
{ρ, ρ̄, 1−ρ, 1−ρ̄} = {½±δ±iγ₀} with δ = β−½ ∈ (0,½), γ₀ = |γ| > 0 (Doc 98, §1.1; the case
γ = 0 is excluded: ζ has no real zeros in (0,1), a classical fact). We define
$$m := \#\{\text{off-critical quadruples of } \zeta\} \in \{0, 1, 2, \dots\} \cup \{\infty\},$$
counted with multiplicity. Then m = 0 ⟺ RH.

**Definition 1.2 (target L8).** An unconditional statement of the form **m ≤ C** for
some absolute constant C < ∞. By P43 (ledger, L8) and Doc 108 (§8.2, Obs. 8.1), the
identified route is κ_W ≤ C·n_W (a linear-in-density bound on the per-window index of the
double form Q₂), which implies 2m·n_W(1+o(1)) ≤ C·n_W and hence m ≤ C/2.

### 1.2. What m ≤ C would be worth

Three remarks on the value of the statement, to calibrate the frankness of the measurement:

(a) **It would be stronger than every known density theorem in its region:** the N(σ,T)
give o(T) off zeros up to height T; an absolute bound independent of T does not exist for
any σ < 1 (§2.6).

(b) **It would give "RH except for finitely many bounded exceptions":** ψ(x) = x + O(x^{½+δ_max+ε}) with
at most C/2 explicit oscillating terms; Weil positivity on a subspace of codimension ≤ 2C
(P35: κ = 2m ≤ C); a Pontryagin space with a priori finite-dimensional negative part — the
starting situation of function-field theory before Castelnuovo positivity (§6.3).

(c) **It would not imply RH** (for C ≥ 2 it does not force m = 0): it passes the "disguised
RH" test (discriminator I2a, Doc 99) in its statement. The document's question is whether
it passes it in its **provability**: whether every proof route re-encodes the
RH-equivalent uniformity.

### 1.3. The three possible outcomes (point (v))

(A) There is a conceivable path to m ≤ C with current technique — one would need to state
the exact lemma and its input. (B) "m finite" is equivalent or near-equivalent to RH — in
particular if "m ≥ 1 ⟹ m = ∞" exists or is proved, the target collapses: finite = 0 and
every finiteness bound IS RH. (C) The target lies behind the master quantifier (P43,
Principle 3.1), with exact localization. §§2–5 carry out the measurement; §6 decides.

---

## 2. (i) Exhaustive inventory: what is known about the structure of ¬RH

### 2.1. The quadruple symmetry and its only free structural consequence

The symmetry (Def. 1.1) is the only unconditional theorem of the form "if an off-critical
zero exists, then…" whose content is about the **configuration**: the zero brings three
others with it. Consequence: m is well defined and κ = 2m (P35; Doc 98, Prop. 6.1: two
hyperbolic planes per quadruple). No other unconditional configurational rigidity is
known: nothing forces two quadruples to share a height, an abscissa, or any arithmetic
relation.

### 2.2. Can the "physical" part (symmetry + growth) forbid nonzero finite m?

No. We prove this in the program's own class.

**Proposition 2.2 (realizability of every finite m in class ℰ).** Let ℰ be the class of
entire functions F of order ≤ 1, with F(s) = F(1−s) and F(½+is) real for real s (the class
of the variational arc, Docs 93–98). For every m ∈ {0, 1, 2, …} there exists F ∈ ℰ with
exactly m quadruples of zeros off the line Re s = ½ and all remaining zeros on it, in
infinite number.

*Proof.* Let F₀(s) := cosh(a(s−½)) with a > 0: entire of order 1, F₀(1−s) =
cosh(−a(s−½)) = F₀(s), and F₀(½+is) = cos(as) ∈ ℝ for s ∈ ℝ, with zeros exactly at
s = ½ + iπ(k+½)/a, k ∈ ℤ — all on the critical line, simple, infinite in number. For each
j = 1, …, m choose δⱼ ∈ (0,½), γⱼ > 0, and set
$$P_j(s) := \bigl((s-\tfrac12)^2-(\delta_j+i\gamma_j)^2\bigr)\,\bigl((s-\tfrac12)^2-(\delta_j-i\gamma_j)^2\bigr),$$
a monic degree-4 polynomial in (s−½), even in (s−½) — hence Pⱼ(1−s) = Pⱼ(s) — with real
coefficients in (s−½)² (the product of the two conjugate factors), hence
Pⱼ(½+is) = (−s²−(δⱼ+iγⱼ)²)(−s²−(δⱼ−iγⱼ)²) = |s²+(δⱼ+iγⱼ)²|² ≥ 0 real for real s. Its
zeros are exactly the quadruple {½±δⱼ±iγⱼ}. Then F := P₁⋯P_m·F₀ ∈ ℰ (product of an entire
function of order 1 by a polynomial: order 1; the symmetries multiply) has exactly
m off quadruples and the infinitely many on-line zeros of F₀. ∎

**Corollary 2.3 (finiteness is not obstructed by physics).** Any theorem
"m ≥ 1 ⟹ m = ∞" for ζ must use the arithmetic structure (Dirichlet series with
coefficients 1, Euler product), not just the functional equation, reality, and growth
order: in the class defined by the latter alone, m = 1 is realizable (Prop. 2.2 with
m = 1). The same holds for any bound m ≤ C: as a theorem on ℰ it is false for every
C (take m = C+1 quadruples); as a theorem on ζ it requires arithmetic input.

**Observation 2.4 (the next step, declared open).** With a Dirichlet series and
functional equation but **without** an Euler product, examples with infinitely many
off-critical zeros are known (Davenport–Heilbronn, 1936: a combination of L-functions
with a Riemann-type functional equation and zeros for Re s > 1; exposition in
Titchmarsh [T86], §10.25). No example is known in that intermediate class with
**exactly one** off quadruple, nor a proof that none exists: GAP declared (not
load-bearing: Corollary 2.3 already fixes that the necessary input is arithmetic; this
gap would only measure how much arithmetic).

### 2.3. Density theorems: what they say and what they do not

Verified inventory (standard statements; [T86] Ch. IX, [IK04] Ch. 10):

- **Bohr–Landau (1914).** For σ > ½ fixed, N(σ,T) = O(T): the proportion of zeros with
  β > ½+ε is 0 (against N(T) ∼ (T/2π)log T). First "zero density" theorem for
  exceptions; compatible with m = 1 and with m = ∞.
- **Carlson (1920).** N(σ,T) ≪ T^{4σ(1−σ)+ε}.
- **Ingham (1940).** N(σ,T) ≪ T^{3(1−σ)/(2−σ)} log⁵T; under Lindelöf, N(σ,T) ≪ T^{2(1−σ)+ε}
  (density). Also [In40]: the density exponent controls prime gaps.
- **Huxley (1972).** N(σ,T) ≪ T^{12(1−σ)/5+ε}; the range σ ≥ ¾ improved since then
  (Bourgain and others; exact constants not load-bearing here).
- **Halász–Turán (1969).** Near σ = 1: N(σ,T) ≪ T^{c(1−σ)^{3/2}} (log T)^{O(1)} —
  Turán's power-sum method (relevant in §4).
- **Linnik (log-free, 1944; modern form [IK04] Thm. 10.4 and Ch. 18).** Log-free density
  N(σ,T) ≪ T^{c(1−σ)}: the base for quantitative Deuring–Heilbronn.
- **Vinogradov–Korobov (1958).** Free region: no zeros with
  β ≥ 1 − c/((log|γ|)^{2/3}(log log|γ|)^{1/3}), |γ| ≥ 3. **Zero** count in that region.
- **Selberg (1942) / Levinson (1974) / Conrey (1989).** Positive proportion of zeros ON
  the line: ≥ 1/3, ≥ 2/5; improvements beyond 5/12 [value and attribution NOT VERIFIED;
  not load-bearing]. They bound the proportion that CANNOT be exceptional; nothing about
  the absolute count of exceptions.

**What there is not:** no theorem on the list (nor any known one) forbids nonzero finite
m, nor forces accumulation ("if there is one off zero, there is another nearby"), nor
produces a count bound independent of T for any σ < 1. Not even via ζ′: Speiser's theorem
(1934; refined by Levinson–Montgomery 1974: N⁻(T) = N₁⁻(T) + O(log T)) **transports** the
finiteness question to ζ′ with the same status; it does not reduce it.

### 2.4. Proved partial positivities: does an extreme quadruple get excluded by anything?

The objective's question: does a quadruple with extreme (δ, γ₀) contradict any **proved**
positivity? The proved positivities and their reach:

(a) **Small-support/semilocal Weil positivity (Connes–Consani; Doc 100).** For tests with
small multiplicative support (only finitely many primes — or none — on the arithmetic
side), the positivity of the Weil functional is proved unconditionally in the semilocal
framework (Doc 100; Connes–Consani 2021–22 [bibliographic details NOT VERIFIED; the cited
content is that of Doc 100]). Can a quadruple violate it? No: by MW-7
(P43 §3.2; Doc 100), for the quadruple's negative term to overcome the positive
archimedean sea, ĥ must resolve the frequency γ₀ and the abscissa δ: support a ≳ log γ₀
(Doc 108, Theorem 3.3: sub-resolution blindness). The supports where positivity is proved
are O(1); the γ₀ with log γ₀ = O(1) are numerically excluded (item (c)). **The proved
regimes never intersect the visibility regime: no choice of (δ, γ₀) produces a
contradiction.**

(b) **Partial Li positivity.** λ_n ≥ 0 ∀n ⟺ RH (Li 1997; Bombieri–Lagarias 1999: it is Weil
positivity in the test family (1−(1−1/s)ⁿ)). A quadruple with zero ρ
(Re ρ > ½) makes |1−1/ρ| > 1 and hence λ_n → −∞ exponentially along a subsequence,
with first negative index n* ≍ (γ₀²/δ)·log(γ₀²/δ) (the quadruple's term grows like
r^n, r−1 ≍ δ/γ₀², against the main term ∼ (n/2)log n; an order-of-magnitude computation,
the constants are not load-bearing). Positivity λ_n ≥ 0 has been computationally verified
up to a certain finite range [exact range NOT VERIFIED; literature: computations by
Maślanka and others]; this excludes the compact region {γ₀²/δ ≲ n*/log} — strictly weaker
than the direct verification of RH in height, which excludes γ₀ ≤ 3·10¹² for EVERY δ.
**Partial Li adds no region.**

(c) **Published numerical verification (height bound).** Platt–Trudgian, *The Riemann
hypothesis is true up to 3·10¹²*, Bull. London Math. Soc. 53 (2021), 792–797: every zero
with 0 < γ ≤ 3·10¹² has β = ½. Excludes γ₀ ≤ 3·10¹².

(d) **Classical free regions.** de la Vallée Poussin: β < 1 − c/log|γ|;
Korobov–Vinogradov (§2.3): excludes δ > ½ − c/((log γ₀)^{2/3}(log log γ₀)^{1/3}).

**Region excluded today, exactly:**
$$\mathcal{R}_{\mathrm{exc}} = \{\gamma_0 \le 3\cdot10^{12}\} \;\cup\;
\Bigl\{\delta > \tfrac12 - \frac{c}{(\log\gamma_0)^{2/3}(\log\log\gamma_0)^{1/3}}\Bigr\}.$$
It is a thin strip hugging the edge δ = ½ plus a finite-height box. The entire
rectangle {δ ∈ (0, ½−ε), γ₀ > 3·10¹²} is allowed by everything proved, **with any
multiplicity m, including m = 1 and m = ∞**. The L8 bound (m ≤ C) would be orthogonal to
𝓡_exc: it does not exclude a region, it bounds the **cardinal** — a type of statement the
inventory contains no example of (§2.6).

### 2.5. Does the theorem "m ≥ 1 ⟹ m = ∞" exist?

Search performed (classical literature + current review): **it does not exist**, such a
theorem is not in the refereed literature. What circulates in that form are unaccepted
preprints that use it as a step toward "disproofs" of RH (not citable; the relevant,
verifiable fact is the absence of the theorem from the standard references [T86], [IK04]
and from surveys of the area). The converse ("there exists a configuration with finite m
realizable by a function in the Selberg class") also does not exist: both directions are
open, and Corollary 2.3 shows that any proof of the first needs the Euler product
essentially. Frank status: **"m ≥ 1 ⟹ m = ∞" is not a theorem, is not refutable with what
is known, and there is no known attack**. For the logic of the outcomes (§1.3): outcome
(B) cannot be certified today in either of its two forms (neither the finite = 0
collapse, nor the m-finite ⟺ RH equivalence).

### 2.6. Conclusion of the inventory: global binarity

**Observation 2.6 (the inventory is binary).** Going through the full list
(§2.3, §2.4), every known unconditional statement bounding off-critical zeros falls into
exactly one of two forms:

| form | examples | count it produces |
|---|---|---|
| free region | VP, VK, height verification | **0** in the region |
| density / large values | Bohr–Landau, Carlson…Huxley, log-free | **≪ T^θ, θ > 0** |

There is no theorem of the third form — "finite nonzero count uniform in T" — in any
region of parameter space. This is the same binarity that Doc 108 (Prop. 2.5) found in
the test-accessible index (0 under RH, ≍ m log T under ¬RH), now verified at the level of
the ENTIRE classical inventory. §5.4 will explain the structural reason (the shape of
moment budgets) and §6 will raise it to a dichotomy.

---

## 3. (ii) The Siegel analogue: anatomy, transport, and failure

### 3.1. Anatomy of the Siegel mechanism

The only analytic precedent for "at most ONE exception" is the exceptional-zero theory
(Landau 1918; Page 1935; Siegel 1935; Deuring 1933 / Heilbronn 1934; Linnik 1944). It is
worth taking it apart into its load-bearing pieces:

(S1) **Real localization.** The exceptional zero β₁ of L(s,χ) (χ real primitive mod q) is
REAL and pinned near s = 1: β₁ > 1 − c/log q. The entire machinery lives on the real
segment [1−c/log q, 1], within the perturbative reach of the region of absolute
convergence.

(S2) **Termwise positivity of an auxiliary product.** For two distinct real primitive
characters χ₁ mod q₁, χ₂ mod q₂:
$$F(s) := \zeta(s)\,L(s,\chi_1)\,L(s,\chi_2)\,L(s,\chi_1\chi_2)$$
has **nonnegative** Dirichlet coefficients (it is, for quadratic χᵢ, the Dedekind zeta
function of a biquadratic field, or in general: log F has coefficients ≥ 0 because
(1+χ₁(p^k))(1+χ₂(p^k)) ≥ 0).

(S3) **Budget = simple pole.** F has a SIMPLE pole at s = 1 (contributed only by ζ).
Landau's lemma on series with positive coefficients gives: if β₁ and β₂ are real zeros of
L(s,χ₁), L(s,χ₂) respectively, then F(σ) would have, as real σ → 1⁺, a sign structure
impossible unless min(β₁,β₂) < 1 − c/log(q₁q₂). **Two zeros cannot both consume a pole of
order 1**: the repulsion is the scarcity of a global budget of size exactly 1.

(S4) **Amplification (Deuring–Heilbronn / Linnik).** The exceptional zero, if it exists,
repels all the other zeros of the family mod q, with a constant that explodes as
β₁ → 1. Input: log-free density (Linnik) + (S2)–(S3).

### 3.2. Transport to ζ, first attempt: the Siegel zone of ζ is already closed

What would a "Siegel zero of ζ" look like in the s-aspect? A zero β+iγ with β → 1. The
(S2)–(S3) piece for ζ itself exists and is **classical**: the inequality
3+4cos θ+cos 2θ ≥ 0 applied to combinations of −Re(ζ′/ζ)(σ) −Re(ζ′/ζ)(σ+iγ) is exactly
"the pole of ζ³ϕ⁴ψ repels the zero": its output is de la Vallée Poussin's free region, and
with Vinogradov sums, Korobov–Vinogradov's. That is: **the analogue of the Siegel
mechanism for ζ itself has already been executed, and its full product is the classical
free region** — the strip of §2.4(d). The mechanism does not produce counts: it produces
the region where the pole's budget suffices, and that region has depth O(1/log γ)
(improved to (log γ)^{−2/3}…), never fixed depth ε > 0. The reason: termwise control of
−ζ′/ζ(σ+it) — the source of all positivity (S2) — dies at the abscissa of absolute
convergence σ = 1; its reach into the interior of the strip is the pole's perturbative
reach O(1/log). **The surviving quadruples (δ < ½ − c/(log γ₀)^{2/3}…) live, by
definition of the excluded region, exactly where the Siegel mechanism has no leverage at
all.**

### 3.3. Transport, second attempt: do two quadruples repel via the explicit formula?

We take ¬RH with two quadruples {δ₁,γ₁}, {δ₂,γ₂} (inheriting the toy-model framework, Doc
98 T1 extended to m = 2) and look for the analogue of (S2)–(S3): a test function whose
PROVED PARTIAL positivity is violated with both present but not with one.

**(a) In the linear Weil functional (one variable).** The zero term is
Σ_ρ ĥ(ρ); the two quadruples contribute Σ_{j=1,2} Σ_{quad_j} ĥ(ρ). There is no cross
term: the functional is LINEAR in the zeros — the product structure of (S2) (four
L-functions multiplied ⟹ the two zeros enter the SAME positive object) has no analogue,
because there is only one ζ: the "product" ζ·ζ is ζ², which adds no information (its
zeros are the same ones with double multiplicity; in (S2) the new information is brought
by χ₁χ₂, a THIRD character — for ζ alone there is no third object). For two quadruples to
interact, a **quadratic** functional in the zeros is needed: exactly the form Q₂ of Doc
107/108.

**(b) In the quadratic form Q₂.** The mixed pairs (ρ ∈ quad₁, ρ′ ∈ quad₂) exist and
contribute. Their spectral structure: the involution (ρ₁,ρ₂) ↦ (1−ρ̄₁,1−ρ̄₂) acts freely
on those pairs (none is a fixed point: both slots are off), so they form **hyperbolic
planes** — signature (k,k), NET contribution zero to definiteness and ADDITIVE
contribution to the negative index. Count computation (same apparatus as Doc 107 Theorem
5.5, Doc 108 Prop. 2.3): with m = 2, the off×off block has (4·2)²/2 = 32 planes; the
16² = 64 pairs include the 2·(16·... ) cross pairs, all in free orbits. **The index grows
with m (κ(Q₂^rel) = 8m²); it never decreases.** There is no term in the quadratic form
where the presence of the second quadruple HINDERS the first: the structure is a
perturbed direct sum, not a competition for a budget. Competition would require both
quadruples to draw against the same BOUNDED positive term; but the local positive term
(the on×on sea of the window, ≍ n_W² with n_W ≍ log T) **grows** with height: unlimited
budget, zero scarcity, zero repulsion. Exact contrast with (S3): there the budget was the
order of the pole, = 1, fixed.

**(c) The cross term on the prime side.** With the explicit formula over a smoothed
Dirichlet polynomial P_w(t) = Σ_n Λ(n)w(n/X)n^{−½−it} (standard expansion:
P_w(t) = Σ_ρ X^{ρ−½}·ŵ-localization at |t−γ(ρ)| ≲ 1, plus pole and lower-order terms;
[IK04] Thm. 5.12 + Mellin), the contribution of the quadruples to ∫|P_w|²dt is
$$\underbrace{m_1\,X^{2\delta_1} + m_2\,X^{2\delta_2}}_{\text{diagonal}}
\;+\; \underbrace{O\bigl(X^{\delta_1+\delta_2}\bigr)\cdot \mathbf{1}_{|\gamma_1-\gamma_2|\lesssim 1}}_{\text{cross}},$$
the cross term only if the heights overlap at the test's resolution. Sizes: δ₁+δ₂ <
½+½ = 1 ALWAYS (the zeros are in the strip), so **the cross term, like the diagonal ones
(2δᵢ < 1), falls strictly below the unconditional error bar O(X log²X) of the
Montgomery–Vaughan mean value theorem** (full computation in §5.3). Crossing does not
change accessibility: it lives at the same invisible scale. And in the localized
quadratic detector, seeing the cross term requires ĥ to SIMULTANEOUSLY resolve the two
unknown frequencies γ₁, γ₂ and the two abscissas δ₁, δ₂: the resolution cost is the
maximum of the costs, the signal is the product of two small factors. **Detecting the
pair is harder than detecting a single quadruple**, not easier.

### 3.4. Verdict of the Siegel front: anti-repulsion

**Proposition 3.1 (no Siegel analogue; proved summary).**
(a) Piece (S2) (an auxiliary product with positive coefficients containing both zeros)
has no analogue for two quadruples of ζ: it requires a third object (χ₁χ₂) that does not
exist in a one-element family. (b) Piece (S3) (an O(1) budget) has no analogue in the
interior of the strip: the local positivity budget at height γ is ≍ log γ and grows.
(c) The only valid transport of the mechanism (termwise positivity + pole) is the
classical free region, already cashed in (§3.2). (d) In the program's quadratic
functionals, two quadruples add up (κ = 4, extra hyperbolic planes), and their prime-side
cross term is of size X^{δ₁+δ₂} < X, below the error bar of the unconditional mean
values. **There exists no theorem, with the cataloged technology, of the form "m ≥ 2 is
harder than m = 1": the detectable directions point the other way (the pair is detected
worse than the lone quadruple).**

*Proof.* (a)–(d) = §3.1–§3.3. ∎

Physical reading: Siegel repulsion is a phenomenon of the **edge of absolute
convergence** (scarcity of positivity next to the pole). The quadruples of ζ live deep in
the interior of the strip, where the available positivity is oceanic and nothing is
scarce: without scarcity there is no repulsion. The boundary between the two
phenomenologies is the classical free region.

---

## 4. (iii) Turán power sums: measurement

### 4.1. What the machinery gives

Turán's second main theorem (standard form; P. Turán, *On a New Method of
Analysis and its Applications*, Wiley 1984; also Halász–Turán 1969 for use in density):
for z₁,…,z_n ∈ ℂ with |z₁| ≥ … ≥ |z_n| and coefficients b_j,
$$\max_{\nu = M+1,\dots,M+n} \Bigl|\sum_j b_j z_j^\nu\Bigr| \;\ge\;
\Bigl(\frac{n}{8e(M+n)}\Bigr)^{n}\,\Bigl|\sum_{j} b_j\Bigr|\,|z_n|^{M+n}\!,$$
(variants with min-conditions on subsets; the load-bearing feature is the **exponential
degradation in n**, the number of consecutive terms). Application to the problem: under
¬RH with m quadruples of parameters (δⱼ, γⱼ), δ_min := min δⱼ, the explicit formula gives
ψ(x) − x = −Σ_off x^{ρ}/ρ + O(x^{½}log²x), and the power sums over the 4m off terms
(z_j = e^{(½+δ_j±iγ_j)u} in the variable u = log x) force, in every progression
u ∈ [U, U(1+1/m-scale)], the existence of x with
$$|\psi(x) - x| \;\gg_{m,\,\delta_{\min},\,\gamma_{\max}}\; x^{\frac12+\delta_{\min}-\varepsilon}.$$
This is a **detection** theorem: m quadruples guarantee localizable oscillation at every
scale, with constants explicit in (m, δ_min, γ_max) that degrade exponentially in m
(n = 4m terms in Turán's theorem; if the off zeros must also be separated from
neighboring on-line ones, n grows to ≍ log γ_max and the constant to a polynomial loss in
γ_max — the same phenomenon that makes the density theorems produced by this method
polynomial, §2.3 Halász–Turán). Note the direction of the degradation: **more quadruples
⟹ worse guaranteed bound** (they can conspire to cancel for longer). Turán's method is
structurally anti-repulsive: it quantifies how much they can hide, not how much they get
in each other's way.

### 4.2. The circularity of the upper bound (where finiteness dies)

To turn detection into a contradiction — and from there into "m ≤ f(δ_min, γ_max)" —
an unconditional upper bound is needed that the guaranteed oscillation would violate:
$$|\psi(x) - x| \;\le\; B(x) \quad\text{with}\quad B(x) = o\bigl(x^{\frac12+\delta_{\min}}\bigr)
\ \text{in the range of x where Turán guarantees the minimum.}$$
Inventory of unconditional upper bounds: the best is
ψ(x) − x ≪ x·exp(−c(log x)^{3/5−ε}) (Vinogradov–Korobov; [IK04] Cor. 8.30) — of size
x^{1−o(1)}, **enormously above** x^{½+δ} for every δ < ½. And it is not bad luck: by the
classical reciprocal theorem (Landau; in the form used by Ingham [In40] and
expounded in [T86] §Ch. III: ψ(x) − x ≪ x^θ implies ζ has no zeros with β > θ, via
the Mellin representation of ζ′/ζ), **any** upper bound ψ(x)−x = O(x^{½+δ_min−ε})
implies there are no zeros with β > ½+δ_min−ε: that is, the upper bound Turán's argument
needs as input IS the quasi-RH conclusion one intended to obtain.
**Exact circularity, no slack:** the method can produce neither "m ≤ f(δ_min, γ_max)"
nor any finiteness, because its upper half is identical to the theorem sought.

### 4.3. What does remain: finiteness in compact boxes (and why it is not the target)

**Observation 4.1.** In any compact box {δ ≥ δ₀, γ₀ ≤ Γ}, finiteness is trivial and
unconditional: m(δ₀, Γ) ≤ N(½+δ₀, Γ) ≪ Γ^{12(½−δ₀)/5+ε} (Huxley) — finite, explicit,
polynomial in Γ. This does not use Turán (although Halász–Turán improves the exponent
near δ₀ → ½). Target L8 is exactly the limit Γ → ∞ with a bound independent of Γ: **the
entire non-triviality of L8 is uniformity in height**, the same old quantifier (P41:
controlled interior / boundary = the statement). The "finiteness in compact regions of
parameter space" the objective asked about already exists and is cheap; it is not a
stepping stone toward L8 because the dependence on Γ is increasing and polynomial, and no
known amplification flattens it (Doc 108, Prop. 7.3: the boundary is k-invariant).

---

## 5. (iv) The central count: exceptional windows vs. unconditional moments

This section carries out the requested count: how many deficit-bearing windows does the
unconditional average asymptotic tolerate? The answer first requires deciding WHICH
per-window statistic sees a quadruple.

### 5.1. Statistics with an unconditional limit theorem are blind

**Lemma 5.1 (blindness of S(t) and Selberg's CLT).** Consider two zero configurations:
(I) a quadruple {½±δ±iγ₀} (plus on-line zeros Z); (II) two on-line double zeros at
½±iγ₀ (plus the same Z). Then the counting functions N(t) of (I) and (II) are
identical, and S(t) = π⁻¹arg ζ(½+it) differs between the two configurations only at
|t−γ₀| ≲ δ, by an amount O(1).

*Proof.* N(t) counts zeros in the rectangle 0 < β < 1, 0 < γ ≤ t (argument
principle over the contour): the abscissa β does not enter the count; (I) and (II) have
the same γ's with the same total multiplicities (the quadruple contributes 2 at height γ₀
and 2 at −γ₀; the two double zeros likewise). S(t) = N(t) − (smooth term) + O(1) and the
fine variation of arg ζ between the two configurations comes from the factor
(s−ρ)(s−(1−ρ̄)) vs (s−½−iγ₀)², whose arguments on the line differ by O(1) and
coincide away from |t−γ₀| ≲ δ (the factors agree to first order far from the zero). ∎

**Consequence 5.2.** Selberg's unconditional CLT (moments of S(t):
∫₀^T S(t)^{2k}dt = c_k T(log log T)^k(1+o(1)), Selberg 1946; exposition [T86] and Tsang)
**does not restrict m at all**: the two configurations of Lemma 5.1 have identical S
statistics except on m windows of size O(1) with O(1) perturbation, and configuration
(II) is RH-compatible. A Gaussian concentration with variance log log T tolerates, by
Chebyshev, up to ≍ T/(log log T)^k windows with deviation O(1) — astronomically more than
any m; but the strong point precedes the tolerance: **the statistic does not distinguish
the worlds even at zero tolerance**, because the abscissa never enters S. The answer to
the question ("does such a concentration limit how many windows can have deficit ≍ 1?")
is: it limits windows with S-deficit, and the off-criticity deficit **is not an S-deficit**.
Likewise log|ζ(½+it)|: the difference between (I) and (II) is a bounded factor away from
γ₀ and a smoothed logarithmic singularity (log δ instead of −∞) in an O(1) window:
perturbation O(polylog) against moments ≍ T(log log T)^k — invisible and of ambiguous
sign.

**The consolidated "what sees what" catalog:** the abscissa δ is seen only by **second-order**
functionals (pair correlation / near-prime deficit ΔK, Doc 108 Def. 3.6; the
κ_W indices). Every first-order statistic with an unconditional limit theorem (N, S,
log|ζ| on average) is blind by construction: the abscissa information lies in the
position of zeros relative to the involution s ↦ 1−s̄, and first order only reads heights.

### 5.2. The per-window deficit count, done carefully

We inherit from Doc 108 (Prop. 2.3, Theorem 3.4) the exact structure of the visible
deficit:

- Windows of the sum variable at height T, width Δ: under ¬RH with m quadruples
  (heights ≤ γ_max fixed), **every** high window has index κ_W ≍ 2m·n_W (off×on
  contamination), with n_W ≍ (2Δ/π)log T. The realizable deficit of the normalized test
  family functional: signal ≍ m·n_W against archimedean mass ≍ n_W²: **relative
  deficit ≍ m/log T per window, in ALL windows** (not just in m of them — this is the
  point the objective's naive pigeonhole underestimates in its favor: the signal is
  everywhere).
- In the one-variable reading (Weil functional per window of height t, width Δ): the
  quadruple's spectral terms live only in |t−γⱼ| ≲ Δ: m exceptional windows
  with local deficit ≍ 1 zero-unit (relative 1/n_W ≍ 1/log T of the window total).

In both readings the deficit accumulated in the average over M windows up to height T₀ is
**relative ≍ m/log T₀** (in the first reading because every window carries it; in the
second because m windows of deficit 1/log T₀ dilute over M windows: m/(M log T₀),
even smaller). The quantitative question: what relative precision do the unconditional
mean values averaging that functional have?

### 5.3. Montgomery–Vaughan: the error bar absorbs every δ < ½, and the exact reason why

**Proposition 5.3 (mean invisibility, quantified).** Let
P_w(t) = Σ_n Λ(n)w(n/X)n^{−½−it} with w smooth and compactly supported. Then:

(a) [MV74] ∫₀^{T₀}|P_w(t)|²dt = (T₀ + O(X))·Σ_n Λ(n)²w(n/X)²/n = (T₀ + O(X))·(½+o(1))(log X)²·c_w.

(b) By the explicit formula ([IK04] Thm. 5.12, via Mellin with ŵ of rapid decay),
each zero ρ = β+iγ contributes to P_w(t) a term of amplitude ≍ X^{β−½} localized at
|t−γ| ≲ 1; the total contribution of m quadruples (heights ≤ T₀) to ∫₀^{T₀}|P_w|²dt is
$$\Delta_{\mathrm{off}} \;\asymp\; \sum_{j\le m} X^{2\delta_j}
\;+\; O\Bigl(\sum_{|\gamma_i-\gamma_j|\lesssim 1} X^{\delta_i+\delta_j}\Bigr).$$

(c) Since δⱼ < ½ and δᵢ+δⱼ < 1, we have Δ_off = o(X·(number of terms)) and hence
Δ_off stays within the O(X log²X) error term of (a) for every m ≤ X^{1−2δ_max−ε} —
in particular **for every fixed m, for m = m(T₀) → ∞ of zero density, and even for m
polynomial in X of exponent < 1−2δ_max**. The Montgomery–Vaughan mean value is
logically compatible with all of those worlds simultaneously.

*Proof.* (a) is the Montgomery–Vaughan mean value theorem [MV74] applied to
a_n = Λ(n)w(n/X)n^{−½}, with Σ|a_n|² ≍ (log X)²·c_w by partial summation with PNT. (b) is
the standard expansion: P_w(t) = (1/2πi)∫(−ζ′/ζ)(½+it+u)X^u ŵ(u)du shifting the
contour: residues at the zeros (term X^{ρ−½−it}ŵ(ρ−½−it), with |ŵ| of rapid decay ⟹
localization at |t−γ| ≲ 1) and at the pole. The integral of the square of the j-th
zero's term over its localization window is ≍ X^{2δ_j}; cross products between zeros at
distance > 1 decay rapidly (decay of ŵ), nearby ones give the indicated term. (c)
arithmetic of exponents: X^{2δ} ≤ X^{1−2ε′} if δ ≤ ½−ε′; compare with
O(X log²X). ∎

**Reading.** The barrier has a strikingly clean shape: **the entire critical strip
(δ < ½) is built to fit inside the diagonal error term O(X) of the large sieve.** The
O(X) error of MV74 is essentially optimal (it is the cost of near-diagonals
n = n′ ± small); improving the bar to o(X^{2δ}) for every δ > 0 — what is needed for
the average to SEE a quadruple — means improving O(X) to O(X^ε), i.e. suppressing the
off-diagonal range entirely, which is the "in every window" asymptotic again (Conjecture
108-N in mean-value form). The Doc 108 wall reappears in the most elementary possible
exponent count.

### 5.4. Large values and high moments: the tolerance never drops below T^θ

Second half of the requested count: instead of the average, count directly the windows
where |P_w| is large (those a quadruple of abscissa δ produces with |P_w| ≍ V = X^δ).
The inventory of unconditional large-value bounds (MV large values, Huxley,
Jutila; [IK04] Ch. 9–10):
$$R(V) \;\ll\; \frac{G\,X}{V^2}\,(\log)^{O(1)} \;+\; \frac{G^3\,T_0\,X}{V^6}\,(\log)^{O(1)},
\qquad G := \textstyle\sum|a_n|^2 \asymp (\log X)^2,$$
and Halász–Montgomery refinements of the same character. With V = X^δ:
R ≪ X^{1−2δ+ε} + T₀X^{1−6δ+ε}: **polynomial in (X, T₀), never O(1)**. This is not an
improvable defect: large-value bounds with 2k-th moments give
R ≪ T₀^{c_k}·X^{k(1−2δ)+ε}-type; to kill the polynomial dependence one would need
k ≍ log T₀ with constants uniform in k — and control of ALL moments with
uniform constants is equivalent to control of the supremum: the master quantifier's
mean → uniform inversion (P43, Principle 3.1), in its moment presentation. In fact the
duality is exact in both directions: **zero-density theorems ARE large-value bounds**
(that is how Ingham, Huxley, Montgomery are proved), so "how many exceptional windows do
second moments tolerate" already has a name in the literature: N(σ,T) ≪ T^{θ(σ)} — the
right-hand column of the §2.6 table. The objective's question is answered in closed
form:

**Quantitative answer (iv).** The unconditional variances and moments (MV74, moments
of S(T), Selberg's CLT, 2k-th moments of Dirichlet polynomials) tolerate
$$R_{\mathrm{tolerated}}(\delta, T) \;\asymp\; T^{\theta_k(\delta)} \quad\text{with } \theta_k(\delta) > 0
\ \ \forall k < \infty,\ \forall \delta < \tfrac12,$$
exceptional windows; the m quadruples produce ≍ m (linear reading) or "all with deficit
m/log T" (quadratic reading). Since m ≪ T^θ for every fixed m and even for
m = ∞ of zero density (the only real restriction: m(T) ≤ N(½+δ, T) ≪ T^θ — which is the
density theorem itself!), **the average tolerates infinite m of zero density: there is
the wall again**, now with its exact quantitative form: the gap between the T^θ
tolerance and the O(1) goal does not narrow for any finite-order moment, and closing it
with uniform k → ∞ is the quantifier.

### 5.5. The pigeonhole and the bootstrapping circularity, resolved against

The hopeful argument was: "for m ≤ C one only needs uniformity on the windows
containing the γⱼ — finite if m is finite; and if m ≥ M, there are M disjoint windows
with simultaneous deficit that might violate an average bound". Three provable failures:

1. **Localization is illusory in the quadratic reading:** under ¬RH the deficit
   κ_W ≍ m·n_W is in ALL high windows (Doc 108, Prop. 2.3: off×on
   contamination), so "only the windows of the γⱼ" describes the linear reading — and in
   the linear reading the per-window deficit is first order in a blind statistic
   (Lemma 5.1) or second order in a statistic with no mean-value theorem at that precision.
2. **The accumulated deficit M/log T violates no accessible mean:** by Prop. 5.3,
   the accessible mean has a relative error bar O(X/T₀) ≥ O(1) in the resolution
   regime (X ≥ T₀) and absorbs X^{2δ} in the sub-resolution regime: in no regime
   does the bar drop to o(M/log T) for fixed M. There is no inequality the pigeonhole can
   activate.
3. **The circularity is not broken but re-encoded:** the pigeonhole converts
   "m ≥ M" into "M simultaneous individual measure-zero events"; but M measure-zero
   events remain a measure-zero event, and P43's Principle 3.1 applies without
   modification: genericity does not detect null-measure events, whether one or M. The
   only way M events could be detectable where one is not would be a supra-additive
   (repulsive) interaction term — exactly what §3 proved does not exist
   (the interaction is additive in κ and below the error bar in primes).

---

## 6. (v) Synthesis: the budget/cost dichotomy and the decision between outcomes

### 6.1. Outcome (B): ruled out as certifiable, with its useful half recorded

There is no theorem "m ≥ 1 ⟹ m = ∞" (§2.5), nor can one be produced without essential
arithmetic input (Cor. 2.3); nor is there a proof of "m finite ⟺ RH". Hence target L8
**does not collapse**: it remains logically strictly weaker than RH. This is the
document's good half: L8 stays alive as a statement. The bad half is methodological and
is decided by §6.2.

### 6.2. The budget/cost dichotomy

**Definition 6.1.** A **finiteness certificate** is a functional B, computable from the
arithmetic side (test-accessible in the sense of Doc 108, Def. 1.2), with:
(P1) **budget**: an unconditional theorem B ≤ C_B < ∞;
(P2) **minimum cost**: an unconditional theorem "each quadruple contributes ≥ c > 0 to B",
with c uniform in (δ, γ₀) over the non-excluded region.
Then m ≤ C_B/c. Every route to L8 is a finiteness certificate (the route κ_W ≤ C·n_W is
the case B = sup_W κ_W/n_W, c = 2).

**Proposition 6.2 (the inventory splits; no candidate satisfies (P1)+(P2)).**
Over the functionals cataloged by the program and the literature:

(a) *Functionals with (P1) without (P2):* T_λ = ∫W_λ dν satisfies (P1) in the relevant
form (it is finite and its value is computable/boundable in fixed worlds), but its cost
per quadruple is 2δ²K_λ(γ₀) (Doc 98, Cor. 2.4; Doc 86 §6), which **tends to 0** as
δ → 0 or γ₀ → ∞ (K_λ decays with the measure dm_∞ ≍ e^{−πγ₀/2}): arbitrarily cheap
quadruples, no bound on m. The same happens to every fixed trace/measure functional (the
eight equivalents of Doc 89): positivity d ν ≥ 0 gives a budget, but the cost vanishes in
the tails of parameter space.

(b) *Functionals with (P2) without (P1):* κ_W/n_W has uniform cost c = 2 per quadruple
(Doc 108, Prop. 2.3 — the cost does NOT decay with γ₀ nor with δ: that is why it is the
L8 candidate), but its uniform boundedness over windows is **RH-equivalent already in its
o(n_W) version** (Doc 108, Prop. 2.5 and Theorem 4.3) and its constant-C·n_W version
requires the same second-order precision o(C/log T) uniform (Doc 108, §8.1): (P1) is
exactly the statement behind the wall. The same holds for every index/supremum over
windows or frequencies.

(c) *There is no third class:* a functional with uniform cost must detect a quadruple at
arbitrary height γ₀ with response ≥ c; by sub-resolution blindness (Doc 108, Theorem
3.3) detection requires tests of resolution a ≳ log γ₀, so B is (at least) a supremum
over the frequency/height of window functionals; and its unconditional boundedness is a
uniform-over-windows bound of a functional whose mean-value version is a theorem and
whose uniform version separates the two worlds at second order — Doc 108's Theorem 3.4
(two worlds) applies mutatis mutandis: (P1) for a B of class (P2) implies evaluating Π
with relative precision O(c/log T) uniform in T. This is not asserted as a general
theorem about "every conceivable functional" (no such classification exists); it is
asserted, with proof, about the program's test-accessible class, which is where all
known candidates live. GAP declared: the dichotomy is exhaustive over the inventory, not
over the space of all mathematically possible functionals.

*Proof.* (a): Doc 98 Cor. 2.4 plus the decay of K_λ (Doc 95, Lemma 2.2:
dm_∞ ≍ |s|^{−1/2}e^{−π|s|/2}ds). (b): the cited references from Doc 108. (c): chain of
sub-resolution blindness + two worlds, as indicated. ∎

### 6.3. The two precedents for "at most k exceptions" confirm the dichotomy

- **Siegel:** B = order of the pole of F(s) at s = 1 (= 1); cost: each exceptional zero
  consumes ≥ c of the pole by termwise positivity (S2)–(S3). **(P1) trivial (the
  budget is a visible integer!), (P2) proved near s = 1.** Result: at most
  1 exception. The mechanism lives where it lives because only there does (P2) hold.
- **Weil (function fields):** B = dim H¹(C̄, ℚ_ℓ) = 2g; cost: each zero is a
  Frobenius eigenvalue in H¹, cost 1. **(P1) is the finite-dimensionality of the
  cohomology — a theorem prior to and independent of purity**; "RH" (purity) comes
  afterward, by Castelnuovo positivity. Note the logical order: in the only world
  where the RH analogue was proved, the L8 analogue ("at most 2g zeros total, in
  particular finitely many exceptions possible") was **free and prior**, handed over by
  the finite-dimensional structure.

**Observation 6.3 (L8 is the counting avatar of finite-dimensionality).** Target L8 asks
for exactly what cohomology gives for free: an a priori bounded finite-dimensional
receptacle where the exceptions must live. The analysis has the right receptacle —
𝒦_off ⊂ (𝒦, Q), of dimension 4m (P35, Doc 96/98) — but its dimension is a function of
the unknown m: the receptacle **measures** the exceptions, it does not bound them;
turning "dim = 4m" into "dim ≤ D" requires the budget (P1) that Prop. 6.2(b) places
behind the wall. This refines P43 §6 (the missing mechanism must read inertia, not
value): the first dividend of a genuine cohomological invariant over Spec ℤ would not be
RH but L8 — and conversely, **an analytic proof of L8 would amount to fabricating finite
dimension out of averages**: the master quantifier inversion in its barest form.

### 6.4. Decision

- **(A) — ruled out, with the lemma's localization known.** The only lemma of the right
  shape is that of Doc 108 §8.1 (κ_W ≤ C·n_W uniform), or, equivalently by Prop. 6.2(c),
  any pair (P1)+(P2): its input is evaluating the near-prime deficit to second order,
  with relative error O(C/log T), uniform in frequency — the scale of the
  lower-order pair-correlation terms, conjectural even under RH
  (Doc 108, §5.3 and §6.2). There is no path with current technique.
- **(B) — ruled out as certifiable** (§6.1): neither collapse nor equivalence is
  demonstrable; L8 remains strictly weaker than RH. (Recording this is itself a result
  of the document: the target is not RH in disguise.)
- **(C) — is what occurs.** With exact and triple localization: (i) the interaction
  between quadruples is additive/sub-error, not repulsive — there is no Siegel-type
  leverage (§3); (ii) the upper bound Turán needs is the theorem sought — circularity
  (§4); (iii) all unconditional averages tolerate m = ∞ of zero density, with tolerance
  T^θ that no finite moment reduces to O(1) (§5). The three localizations are the same
  one: distinguishing "m ≤ C" from "m = C+1" is an individual measure-zero event for
  every accessible statistic — the master quantifier (P43, Principle 3.1) also governs
  finiteness, not just vanishing.

**The phrase that summarizes the measurement:** *"m finite" is not the same statement as
"m = 0", but it is behind the same wall, because the wall was never about the value of
m: it is about the ability of any average to see ONE unit of m.*

---

## 7. VERDICT

**VERDICT: TARGET UNREACHABLE** — with current technique and with every form of argument
cataloged by the program (propagation, amplification, recurrence, positivity, sieve,
repulsion, power sums, moments/concentration), for the following reason:

> Every route to "m ≤ C" is a budget/cost certificate (Def. 6.1), and the dichotomy of
> Prop. 6.2 is exhaustive over the inventory: bounded functionals have a vanishing cost
> per quadruple (T_λ: 2δ²K_λ(γ₀) → 0) and uniform-cost ones (κ_W/n_W) have an
> RH-equivalent bound or the same uniform-over-windows second-order precision
> (Doc 108). There is no repulsion between quadruples (§3: anti-Siegel, additive and
> sub-error-bar interaction), the upper bound Turán needs does not exist (§4: Landau–Ingham
> circularity), and all unconditional averages — including Selberg's CLT,
> directly blind to the abscissa — tolerate m = ∞ of zero density (§5). Finiteness is
> behind the master quantifier, at the same point as vanishing.

**Nuances the verdict does NOT include (the document's positive results):**

1. L8 **does not collapse to RH**: "m ≥ 1 ⟹ m = ∞" neither exists nor is in sight
   (§2.5), and any future proof will need the Euler product essentially
   (Prop. 2.2/Cor. 2.3 — proved). The target remains recorded as a genuinely
   intermediate open statement.
2. Finiteness in compact boxes m(δ₀,Γ) ≤ N(½+δ₀,Γ) < ∞ is a trivial theorem (§4.3); the
   entire content of L8 is uniformity in Γ.
3. The exact form of the mechanism that would reach L8 is stated (Def. 6.1 + Obs. 6.3):
   a global O(1) budget with uniform minimum cost per quadruple — what the pole gives
   near s = 1 (Siegel) and dim H¹ gives in function fields (Weil). If the
   Connes–Consani program (or any other) produces a finite-dimensional invariant over
   Spec ℤ, its FIRST verifiable dividend would be L8, before RH. Final physical
   reading: **target L8 is the cheapest possible detector of genuine cohomology — and
   that is exactly why it is unreachable by pure analysis.**

---

## References

**Internal (backward-only):** Doc 108 (Prop. 2.3, 2.5; Theorems 3.3, 3.4, 4.3; §5; §8.1,
Obs. 8.1; Prop. 7.3); Doc 107 (Theorem 5.5, Prop. 6.1); Doc 106 (Prop. 3.6); Doc 100
(semilocal positivity; MW-7); Doc 99 (discriminator I2a); Doc 98 (Hypothesis T1, Cor. 2.4,
Prop. 6.1); Doc 96 (Theorem 8.1); Doc 95 (Lemma 2.2); Doc 89 (eight equivalences); Doc 86
(§6, K_λ); P43 (Principle 3.1, ledger L1–L8, §6); P42 (§6); P41 (interior/boundary no-go);
P35 (κ = 2m).

**Literature (verifiable):**
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. London
  Math. Soc. **53** (2021), 792–797. [verified: height 3 000 175 332 800]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. D. R.
  Heath-Brown), Oxford, 1986. [T86] (Ch. IX: density; §10.25: Davenport–Heilbronn;
  Ch. III: free region and Landau's reciprocal theorem; ζ with no zeros on (0,1).)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004. [IK04]
  (Thm. 5.8, 5.12; Cor. 8.30; Ch. 9–10: large values and density; Ch. 18: log-free and
  Deuring–Heilbronn.)
- H. Bohr, E. Landau (1914): N(σ,T) = O(T) for σ > ½. F. Carlson (1920); A. E. Ingham,
  *On the estimation of N(σ,T)*, Quart. J. Math. **11** (1940) [In40]; M. N. Huxley,
  Invent. Math. **15** (1972): density exponents cited.
- G. Halász, P. Turán, J. Number Theory **1** (1969); P. Turán, *On a New Method of
  Analysis and its Applications*, Wiley, 1984 (second main theorem; exact constants
  not load-bearing).
- Yu. V. Linnik (1944), log-free density and repulsion (exposition [IK04] Ch. 18);
  E. Landau (1918); A. Page (1935); C. L. Siegel (1935); M. Deuring (1933);
  H. Heilbronn (1934): exceptional-zero theory, standard statements.
- A. Selberg, Arch. Math. Naturvid. **48** (1946): unconditional moments of S(t);
  N. Levinson (1974) ≥ 1/3; J. B. Conrey, J. reine angew. Math. **399** (1989) ≥ 2/5.
  Improvement beyond 5/12: [NOT VERIFIED; not load-bearing].
- A. Speiser, Math. Ann. **110** (1934); N. Levinson, H. L. Montgomery, Acta Math.
  **133** (1974): zeros of ζ′ and the critical line.
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2)
  **8** (1974). [MV74]
- X.-J. Li, J. Number Theory **65** (1997); E. Bombieri, J. C. Lagarias, J. Number
  Theory **77** (1999). (Verified numerical range of λ_n ≥ 0: [NOT VERIFIED].)
- H. Davenport, H. Heilbronn, J. London Math. Soc. **11** (1936).
- A. Connes, C. Consani, semilocal Weil positivity (2021–22), cited via Doc 100
  [bibliographic details NOT VERIFIED here].

*End of Doc 111.*
