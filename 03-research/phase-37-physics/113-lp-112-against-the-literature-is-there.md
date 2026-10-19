# Doc 113 — LP-112 against the literature: is there a precedent for sequential self-approximation without strong recurrence?

**Program:** Riemann Hypothesis — Phase 37, "physical mode"
**Prerequisites:** Doc 112 (LP-112; Theorem 2.3: LP-112 ⟹ m∈{0,∞}; Prop. 2.6: under ¬RH the good τ have upper density zero; Obs. 2.4: the B² seminorm annihilates compacts; Lemmas 2.1–2.2: unconditional B²-almost-periodicity and positive density of almost-periods); Doc 102 (Bagchi audit: strong recurrence ⟺ RH; the Euler observable discontinuous at ω₀; family SR_d); Doc 104 (effective SR_d: linear degeneration of the scale, anchored window, binary Hurwitz wall); Doc 109 (identity RH = (m<∞) ∧ D-109); P43 (Principle 3.1, master quantifier).
**Nature of the document:** literature mapping and fine comparison. Source verification is central: every external statement was checked against the accessible source (full text, abstract, or verified survey); what is unverified is marked [UNVERIFIED]. No numerics, no simulations. No proof is fabricated; GAPs are declared with exact location.

---

## 0. Executive summary

**The question.** LP-112 (Doc 112, §2.2): *there exists a sequence τ_k → ∞ such that
ζ(s+iτ_k) → ζ(s) uniformly on every compact disk of the open critical strip* —
**sequential** pointwise self-approximation, with no density requirement on the set of
τ, only non-emptiness. We know: RH ⟹ LP-112 (via Bagchi); LP-112 ⟹ m∈{0,∞} (D112,
Thm. 2.3); LP-112 is strictly weaker than strong recurrence; under ¬RH its witnesses
form an upper-density-zero set (D112, Prop. 2.6) whose emptiness is unknown. Is there
in the literature ANY precedent — for ζ, for L-functions, for some natural class of
functions — of sequential self-approximation proved WITHOUT going through strong
recurrence / without an RH equivalent? And is there any technique (Montel+B²,
Stepanov, Birkhoff) with a real chance of proving LP-112 unconditionally?

**Findings, in order:**

1. **(§2.1) The precedent for the equivalence is 60 years older than Bagchi: Bohr
   1922.** For χ a non-principal character, RH(L(·,χ)) ⟺ L(·,χ) is almost-periodic in
   σ > 1/2 in Bohr's local-compact sense (almost-periods **relatively dense**). The
   relative density is load-bearing in the converse direction (amplifier against
   Bohr–Landau); the sequential version of Bohr's statement is exactly LP-112 and is
   left open by his theorem for the same reason it is left open by Bagchi's.

2. **(§2.5–2.6) The inventory of what is proved about ζ's self-approximation is
   exhaustive and contains no unconditional sequential statement in any band σ₀ < 1.**
   Everything unconditional is of positive density and lives in d ≠ 0 (Nakamura,
   Pańkowski, Garunkštis; Baker and the six exponentials theorem); everything touching
   d = 0 is RH-equivalent (Bagchi 1987; short intervals 2025; Laurinčikas's 2025
   equivalents). The unconditional abscissa of pointwise almost-periodicity of ζ is
   exactly σ₀ = 1: below it, the relatively dense version in σ > σ₀ is **equivalent**
   to "ζ has no zeros in σ > σ₀" (circular), and the sequential version is open for
   EVERY σ₀ < 1 — the whole strip is terra incognita, even right against σ = 1.

3. **(§3) Precedents in other classes exist and all use the same technique: genericity
   of the point (full support).** The Hurwitz zeta ζ(s,α) with α transcendental (or
   rational ≠ 1/2, 1) is unconditionally strongly recurrent — a function WITH zeros in
   the strip that self-approximates with positive density — because its Bagchi measure
   has full support: the point is generic for its own statistics. There is no case in
   the literature of certified self-approximation for a point outside the support of
   its own shift statistics — which is exactly what LP-112 asks for under ¬RH.

4. **(§4 — the heart of the document) The Montel+B² chain dies, and it dies exactly at
   the point of D112 Prop. 2.6/Obs. 2.4.** The compactness links survive intact:
   unconditional moments + Chebyshev give density ≥ 1−δ of τ with local bound, the
   intersection with the B² almost-periods (positive density) has positive density,
   and Montel extracts a sequence τ_k → ∞ with ζ(·+iτ_k) → g. The link that dies is
   the **identification g = ζ**: the B² information is a global average in t that
   assigns zero weight to the window of the disk, and the compact-open information
   lives only in that window — the supports of the two pieces of information are
   disjoint. Under H(m) the death is a theorem: the generic limit is nonzero in D
   (Bagchi's support + Hurwitz) while ζ|_D vanishes. The attempt to re-anchor by
   composing almost-periods reproduces the anchored-window collapse of D104 §5.4.
   What is missing remains isolated as **LP-113 (anchoring lemma)**: localizing the
   mean goodness of ONE B² almost-period in the fixed compact window. LP-113 is not
   RH-equivalent by known dictionaries, but its witnesses have density zero under
   ¬RH: it is the same non-generic-selection wall, in window coordinates.

5. **(§5) Stepanov: the structural exit exists and is closed by growth,
   unconditionally.** The S² seminorm (fixed-size windows, sup over position) does
   NOT annihilate compacts — if ζ were S²-almost-periodic in a band, Prop. 2.6's
   argument would not apply and subharmonicity would give Rouché pointwise control.
   But we prove (Theorem 5.2, unconditional): ζ is NOT S^p-almost-periodic on any
   sub-band of the strip, for any p ≥ 1 — S-almost-periodicity implies S-boundedness,
   subharmonicity turns the large values of ζ (unconditional Ω-theorems; Montgomery
   1977, Aistleitner 2016) into windows of diverging norm. And the Weyl seminorm again
   annihilates compacts. The resulting dichotomy is exact and is the document's
   structural finding: **every almost-periodicity seminorm that sees compacts is
   destroyed by ζ's growth in the strip; every seminorm that survives the growth is
   blind to compacts.** P43's wall, in seminorm coordinates.

6. **(§6) Birkhoff does not apply:** the orbit {ζ(·+iτ)} is not relatively compact in
   H(strip) (Ω-theorems), Poincaré recurrence over the Bagchi measure produces
   almost-everywhere — generic — recurrence, and the available compactness lives above,
   on the Kronecker torus, where the obstruction is the discontinuity of the Euler
   observable at ω₀ (D102 §7.3): nothing new relative to D102, verified.

**VERDICT (§8): NO PRECEDENT.** No statement in the literature proves sequential
self-approximation without simultaneously proving recurrence with density (positive
or relative) via genericity of the point. LP-112 requires a new technique: a
mechanism of **non-generic selection** (anchoring of almost-periods to a fixed compact
window — the lemma LP-113), of which there is no instance in function theory,
topological dynamics, or analytic number theory.

---

## 1. The object and the comparison criterion

### 1.1. LP-112, exact statement (D112 §2.2)

**Lemma LP-112 (OPEN).** *For every closed disk D ⊂ {½ < σ < 1} there exists a
sequence τ_k → ∞ such that*
$$\sup_{s \in D} |\zeta(s + i\tau_k) - \zeta(s)| \;\longrightarrow\; 0.$$
(Weak version LP-112⁻, sufficient to refute each H(m): for every D and ε > 0 there
exists ONE τ > height(D) with sup_D |ζ(s+iτ) − ζ(s)| < ε.)

What is known (all in D112): RH ⟹ LP-112 (Bagchi's strong recurrence ⟹ positive
density ⟹ sequence); LP-112 ⟹ m ∈ {0,∞} (Thm. 2.3, Rouché with constants frozen by
H(m)); under H(m), the set A_ε of good τ has upper density zero (Prop. 2.6) but its
emptiness is unknown; LP-112 does not imply RH by any known dictionary (D112 §5.4).

### 1.2. What counts as a precedent

A precedent for LP-112 would be a theorem of the form: *in some natural class of
functions, f(s+iτ_k) → f(s) on compacts for some sequence τ_k → ∞, proved in a regime
where it is NOT known (or it is false) that the set of good τ has positive density* —
that is, certified self-approximation for a point that is possibly **non-generic** for
its own shift statistics. A theorem that proves positive density (or relative density)
and deduces the sequence as a corollary is NOT a precedent: it is exactly the
machinery that Prop. 2.6 of D112 closes off for ζ under ¬RH. This distinction
organizes the whole document.

---

## 2. Exact map of what is proved for ζ and L-functions in self-approximation

### 2.1. The precedent for the equivalence: Bohr 1922, sixty years before Bagchi

**Theorem (Bohr, 1922).** *Let χ be a non-principal Dirichlet character. Then RH for
L(s,χ) is equivalent to the almost-periodicity of L(s,χ) in the half-plane σ > 1/2,
where "almost-periodic on a region E" means: for every ε > 0 and every compact
K ⊂ E there exists a **relatively dense** set {τ_m} ⊂ ℝ with
sup_{s∈K} |f(s+iτ_m) − f(s)| < ε for every m.*

*Verification.* Statement verified via secondary sources (Herichi–Lapidus,
arXiv:1305.3933, §2, which states it with the cited local-compact definition; also
recorded in Steuding's standard exposition). The original: H. Bohr, *Über eine
quasi-periodische Eigenschaft Dirichletscher Reihen mit Anwendung auf die
Dirichletschen L-Funktionen*, Math. Ann. 85 (1922) [exact bibliographic data via
secondary sources; original text NOT VERIFIED in this session]. The recorded
historical motivation: Bohr introduced almost-periodicity as a tool for RH; the
approach "failed for ζ" (the pole at s = 1 and the structure of the problem) and the
reformulation for L(s,χ) with χ non-principal remained.

Three fine comparison observations, which are the useful content:

**(a) Bohr's notion is local-compact, not uniform-on-the-line.** It does not require
boundedness of L in the strip (which is false, Ω-theorems): it asks for almost-periods
per compact. It is exactly the topology of LP-112 — with one difference: **relative
density** of the set of almost-periods, where LP-112 only asks for a sequence.

**(b) Relative density is load-bearing in the direction "almost-periodicity ⟹ RH",
and it is so via the same amplifier as in Bagchi.** If L has a zero ρ₀ with
Re ρ₀ > 1/2, Rouché transports the zero to every almost-period: a relatively dense
set of τ_m gives ≫ T zeros up to height T in σ ≥ Re ρ₀ − ε, contradicting
N(σ,T) = o(T) (Bohr–Landau 1914 — available to Bohr in 1922). With a mere
SEQUENCE one obtains infinitely many zeros, i.e. m = ∞ — no contradiction: the
sequential version of Bohr's theorem is not equivalent to RH(χ), it is exactly the
analogue of LP-112 for L(s,χ), and it is equally open. **The boundary
relative-density/sequence was already drawn in 1922; no one crossed it.**

**(c) The direction "RH ⟹ almost-periodicity" is the same mechanism as D102
Prop. 7.2:** RH(χ) ⟹ Σ_p χ(p)p^{−s} converges in σ > 1/2 ⟹ log L inherits the
almost-periodicity of the convergent series (Bohr's machinery) ⟹ L = exp(log L) is
almost-periodic on compacts. The adaptation to ζ (with the pole excluded from the
compacts, or working with (s−1)ζ(s)) gives the folklore: **ζ is locally almost-periodic
(with relatively dense almost-periods) in σ > σ₀ ⟺ ζ has no zeros in σ > σ₀** — both
directions by the above. This is used in §2.6. [Assembled here from standard pieces:
we did not find this equivalence for ζ with this notion stated literally in the
consulted literature; the two directions are Bohr's proofs and the amplifier, and the
core (b)⟺(a) is D102's Prop. 7.2.]

### 2.2. Bagchi 1981/1987: strong recurrence ⟺ RH (verified)

**Theorem (Bagchi).** *RH ⟺ for every compact K ⊂ D(1/2,1) with connected complement
and every ε > 0:*
$$\liminf_{T\to\infty}\ \frac{1}{T}\,\mathrm{meas}\Big\{\tau\in[0,T] :
\sup_{s\in K}|\zeta(s+i\tau)-\zeta(s)|<\varepsilon\Big\}\;>\;0. \tag{SR}$$

*Verification.* Verified in D102 §2.3 against Matsumoto's survey
(arXiv:1407.4216, Thm. 20), which exposes Bagchi's thesis (Indian Statistical
Institute, 1981) and the paper B. Bagchi, *Recurrence in topological dynamics and the
Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240. Bagchi's improvement over
Bohr 1922: (i) it covers ζ; (ii) it replaces relative density with positive measure
density; (iii) the proof of RH ⟹ SR goes through the functional limit theorem and the
support S = {f ≠ 0 in D} ∪ {0} — the point ζ is generic under RH because it belongs
to the support. The structure is identical to Bohr's: genericity in one direction,
amplifier against density o(T) in the other. **In both theorems, the amount of
witnesses required (relative or measure density) is exactly what activates the
amplifier; LP-112 is calibrated to deactivate it (D112 Prop. 2.7), and that is why
neither theorem reaches it.**

### 2.3. The family SR_d, d ≠ 0: the complete unconditional state (verified)

For d ∈ ℝ, (SR_d) is statement (SR) with ζ(s+idτ) in place of ζ(s); (SR_0) = (SR)
= RH. Verified state at the source (D102 §6.3, D104 §1.2, and re-verified in this
session against accessible abstracts/texts):

- **d irrational algebraic:** (SR_d) unconditional — T. Nakamura, *The generalized
  strong recurrence for non-zero rational parameters*, Arch. Math. 95 (2010), 549–555
  (the algebraic part), via joint universality + **Baker's theorem** (linear forms in
  logarithms).
- **d transcendental:** (SR_d) unconditional — Ł. Pańkowski, via the **six
  exponentials theorem** (in *Self-approximation of Dirichlet L-functions*,
  arXiv:1006.1507, and exposed in Matsumoto §9).
- **d rational, d ≠ 0, ±1:** unconditional — Nakamura–Pańkowski, Arch. Math. 99
  (2012), 43–47 (corrigendum, verified via arXiv:1203.1393: ζ for |a−b| ≠ 1, log ζ
  for every d ≠ 0) and Ł. Pańkowski, *Joint universality and generalized strong
  recurrence with rational parameter*, arXiv:1503.06931 (verified: every rational
  d ≠ 0, ±1).
- **d = 1:** trivial (the two copies coincide). **d = −1:** compare ζ(s+iτ) with
  ζ(s−iτ); excluded from the above theorems; status: open according to the sources
  consulted [UNVERIFIED whether later work covers it].
- **Mapping note (candor about the fragility of the boundary):** the preprint
  T. Nakamura, *A simple proof of the generalized strong recurrence for any non-zero
  parameter*, arXiv:1006.3184, which claimed all d ≠ 0 at once, was **withdrawn by
  the author** ("the proof has a gap" — verified on arXiv). The d ≠ 0 boundary closed
  by accumulation of distinct Diophantine techniques per class of d, not by a
  unifying mechanism. The point d = 0 is not the end of a ramp: it is another
  category.
- **Also:** Nakamura–Pańkowski, *Self-approximation for the Riemann zeta function*,
  Bull. Aust. Math. Soc. (2012/13; verified via Cambridge Core at abstract level
  [volume and pages NOT VERIFIED]): self-approximation in σ > 1 and in the right
  half of the critical strip, with joint approximation results for
  ζ(s+λ+idτ) and ζ(s+iτ) — again, all statements of positive density with d ≠ 0
  or a fixed nonzero shift λ.

**Comparative reading (D104, confirmed by the literature):** all the (SR_d) with
d ≠ 0 exploit **relative equidistribution** — the phases p^{−i(1−d)τ} equidistribute
and Baker/six-exponentials certify the independence of the joint system. At d = 0 the
relative equidistribution is identically null and the problem collapses to the
absolute position of the arithmetic point: the Diophantine input runs out exactly at
the boundary (D102 §6.3). D104 quantified the collapse: the density does not
degenerate, the scale degenerates linearly (T₀ ≍ 1/|d|), and the quantity Rouché needs
(density in the anchored window J_d, of measure ≍ 1/|d|) is demonstrably exactly 0 —
a binary Hurwitz wall, not a quantitative one.

### 2.4. d = 0 in short intervals and the 2025 equivalents: still all density

Verified at abstract/secondary-source level: recent work on self-approximation of ζ
in short intervals (Andersson, Garunkštis, Kačinskaitė et al., Symmetry 17 (2025),
art. 2075 [author list partially verified via search engine; full text NOT VERIFIED —
the server denied access]) proves that RH is equivalent to the positivity of the lower
density (and, with precision caveats, of the density) of the set of approximating
shifts **in short intervals**; along the same line, A. Laurinčikas, *On equivalents of
the Riemann hypothesis connected to the approximation properties of the
zeta-function*, Axioms 14 (2025), 169 [verified at abstract level]. That is: active
research at d = 0 produces **more equivalences with RH**, all in terms of density —
no sequential version, nothing unconditional. The direction of the field confirms
D112's diagnosis: the boundary between "positive density" (RH-equivalent) and
"sequence" (LP-112) has not been explored because there is no tool on the sequential
side.

### 2.5. Is there ANY unconditional sequential result for ζ in the strip? Negative inventory

We searched systematically (search sessions on "self-approximation", "strong
recurrence", Nakamura/Pańkowski post-2011, Andersson, Garunkštis; Matsumoto's survey
§9 as a master map). Inventory result:

1. **τ_k from special sequences — Bohr almost-periods of the tail:** none exist.
   The only mechanism that produces explicit almost-periods (Kronecker–Weyl on
   {τ log p/2π}_{p≤X}, D112 Lemma 2.2) produces **B²** almost-periods, whose
   goodness is an average in t and zero weight on compacts (D112 Obs. 2.4). There is
   no theorem in the literature that promotes an almost-period of a truncated
   Dirichlet polynomial to a pointwise almost-period of ζ in the strip; the obstacle
   is the tail ζ − P_X, which is only controlled in mean (mean square value) — the
   same point where D112 §2.3 located the three failures.
2. **τ_k from ergodic return times:** the unconditional, relatively dense return
   times of the Kronecker flow on the torus (D102 E3) do not transfer to ζ because
   the Euler observable is not continuous at ω₀ (D102 Prop. 7.2/§7.3): the
   transference IS RH. No work in the literature avoids this; Bagchi 1987 stated it
   (it is the content of its title) and that is where it rested.
3. **Discrete universality (Reich):** shifts τ = nh, n ∈ ℕ — the statement is again
   of positive density (in n) and the target must be nonzero: A. Reich,
   *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980) [via Matsumoto §8;
   original NOT VERIFIED]. No new sequential content.
4. **Hybrid Euler-product approximations (Gonek; Gonek–Hughes–Keating):**
   ζ ≈ truncated product × zero factor, valid "for almost all t" or outside
   exceptional sets — again a.e./density-1 statements, never in the fixed window.
   [Cited as context; details NOT VERIFIED in this session, not load-bearing.]

**Conclusion of the inventory: there is no unconditional sequential self-approximation
result for ζ in any sub-region of the critical strip.** Everything published is:
(i) positive density with d ≠ 0; (ii) RH-equivalent with d = 0; (iii) trivial in
σ > 1.

### 2.6. The abscissa of pointwise almost-periodicity: σ₀ = 1 is the exact edge

**(a) σ > 1: trivially yes.** Absolute convergence ⟹ ζ is uniformly Bohr
almost-periodic on every σ ≥ 1+ε (Bohr 1918; D112 §2.1(a)) ⟹ the almost-periods
(relatively dense) give sequential self-approximation on compacts of σ > 1.
LP-112 restricted to σ > 1 is a classical theorem — and vacuous for zeros (Euler).

**(b) How far down to some σ₀ < 1 does it extend unconditionally? Answer: nowhere.**
The situation, precisely:

- **Uniform version (Bohr on the line):** FALSE for every σ ≤ 1 — ζ is unbounded on
  every line σ ≤ 1 (Ω-theorems, unconditional; [Tit86, Ch. VIII]; at σ = 1,
  ζ(1+it) = Ω(log log t)). The edge of uniform almost-periodicity is exactly the
  abscissa of boundedness, σ = 1.
- **Relatively dense local-compact version (Bohr's 1922 notion):** by §2.1(c), its
  validity in σ > σ₀ is **equivalent** to "ζ has no zeros in σ>σ₀" (quasi-RH of
  abscissa σ₀). Since no zero-free region of the form σ > σ₀ with σ₀ < 1 is proved
  (the Vinogradov–Korobov region degenerates with height and gives no fixed band),
  **any unconditional extension to some σ₀ < 1 is circular**: it would prove
  quasi-RH. The supremum θ of the real parts of the zeros is exactly the critical
  abscissa of this notion, and "extending below 1" = "lowering θ" — the problem
  itself.
- **Sequential version (LP-112 by bands):** for σ > σ₀ with σ₀ < 1 this implies only
  "the number of zeros in σ > σ₀ is 0 or ∞" (Theorem 2.3's argument of D112,
  verbatim by bands). This is NOT quasi-RH — there is no circularity — and yet
  **it is open for every σ₀ < 1**, even σ₀ = 1 − δ with δ minuscule, where the
  zero-density theorems are very strong (N(σ₀,T) ≪ T^{κ} with κ small). It is not
  even known whether the number of zeros of ζ in σ > 0.99 is 0 or infinite.
- **Moment/Carlson routes for some σ < 1?** The moments (Carlson, mean square value,
  [Tit86, Thm. 7.2]) are exactly the input of D112's Lemma 2.1: they give B², i.e.
  almost-periodicity **in mean** throughout the whole strip σ > 1/2 — lower and
  weaker than what the question asks. They do not promote to pointwise in any band:
  the promotion is the problem (D112 §2.3). There is no intermediate result "pointwise
  in σ > σ₀ for some σ₀ ∈ (1/2,1) unconditional" — the leap from mean to pointwise
  has not been taken at any abscissa below 1.

**Synthesis of (i):** σ₀ = 1 is the proved edge of pointwise almost-periodicity
(sequential or relatively dense) of ζ; the whole strip is terra incognita for the
sequential version, and RH-circular territory for the relatively dense version. The
map has exactly the shape P43's wall predicts: the pointwise is proved where there are
no zeros to find, the mean is proved everywhere, and the mean→pointwise promotion is
proved nowhere that it matters.

---

## 3. Precedents in other classes of functions

### 3.1. The real positive precedent: Hurwitz and full support

**Fact (unconditional, verified literature).** The Hurwitz zeta
ζ(s,α) = Σ_{n≥0}(n+α)^{−s} with α transcendental (Bagchi 1981; also Gonek for α
rational ≠ 1/2, 1 — via Matsumoto §7, verified in the survey) is **strongly
universal** on D(1/2,1): it approximates with positive density of shifts any
f ∈ H^c(K) — **without any non-vanishing restriction**, because without an Euler
product the functional limit theorem has full support (all of H(D)). Immediate
corollary (taking f = ζ(·,α)|_K): **ζ(s,α) is strongly recurrent — it self-approximates
with positive density — unconditionally, despite having infinitely many zeros in the
strip.** The specific self-approximation line: R. Garunkštis, E. Karikovas,
*Self-approximation of Hurwitz zeta-functions*, Funct. Approx. Comment. Math. 51
(2014), 181–188 (verified; they treat the family with parameter d, with α
transcendental), and Karikovas–Pańkowski for α rational [via secondary sources].

**Reading — why this is NOT a precedent for LP-112 but its perfect contrast.** Hurwitz
self-approximation is proved by making the point **generic**: ζ(·,α) belongs to the
support of its own limit measure because the support is everything. The miracle is not
in a selection technique but in the geometry of the support. For ζ under ¬RH the
opposite happens: the Euler product compresses the support to
{f ≠ 0} ∪ {0} and an off-critical zero expels ζ from it (D112 Prop. 2.6). The
comparison produces the program's structural irony in its sharpest form: **the
arithmetic property that makes RH plausible (Euler ⟹ support without zeros) is
exactly the one that makes self-approximation by genericity unprovable.** Functions
without Euler self-approximate trivially (full support) AND have off-critical zeros in
abundance (m = ∞: Hurwitz, Davenport–Heilbronn) — they realize the m = ∞ branch of
the dichotomy with self-approximation included, in perfect consistency with D112's
Thm. 2.3.

### 3.2. Davenport–Heilbronn and the intermediate class

The Davenport–Heilbronn function (Dirichlet series with functional equation, without
Euler) has infinitely many off-critical zeros ([DH36], verified in D111/D112). Its
strong recurrence would be the same full-support phenomenon as Hurwitz (it is a
combination of L-functions / Hurwitz zetas with rational α) [strong universality of
the class: plausible and cited in the mixed-universality literature; exact status for
DH NOT VERIFIED in this session — not load-bearing]. The confirmed pattern: in the
whole class "Dirichlet series + functional equation without Euler" where
self-approximation is proved, it is proved by genericity and coexists with m = ∞.

### 3.3. Random Euler products: a.e. recurrence

For the random element ζ(s,ω) (random Euler product, ω on the infinite torus), the
Bagchi measure is invariant under the vertical flow and for a.e. ω the point is
generic: the strong recurrence of ζ(·,ω) holds for almost every ω (limit theorem +
support; [Bag81], [Lau96]). The arithmetic point ω₀ is ONE point of the space; under
¬RH it is exactly a point of the exceptional null set (D102 Cor. 7.3). **Precedent for
"a.e. point of the space self-approximates": yes, standard. Precedent for "THIS point
self-approximates" when the point may be exceptional: none.**

### 3.4. The Selberg class and general B²-almost-periodic functions

- **Selberg class:** strong recurrence at d = 0 for elements of the Selberg class is
  GRH-equivalent by the same Bagchi mechanism (extensions: Bagchi himself to
  L(s,χ); Steuding to wider classes — via D102 §2.3 and Matsumoto). Nothing
  sequential.
- **B²-almost-periodic functions with ℚ-linearly independent frequencies (abstract
  class):** here the sequential question is FALSE in general without additional
  hypotheses: D111's cosh-examples are not even B² (D112 Lemma 3.1), but within B²
  the classical theory (Besicovitch 1932; Jessen–Tornehave [JT45] for the mean zero
  structure) is entirely a theory of averages — the Jensen function sees mean zero
  densities, not individual zeros (D112 §6.2). There is no theorem in the classical
  theory of almost-periodic holomorphic functions of the form "f ∈ B²(band) ⟹
  f(·+iτ_k) → f pointwise on compacts for some sequence": the B² class identifies
  functions that differ on compacts (the seminorm annihilates compacts), so the
  pointwise statement **is not even a property of the B² equivalence class** — it
  is a property of the representative. No theorem about the class can prove it. This
  trivial but exact observation explains why the search for precedents in abstract
  almost-periodicity theory is structurally empty: LP-112 is invisible in the
  category where ζ has its unconditional theorems.

---

## 4. The Montel + B² chain: examined with maximum rigor and maximum suspicion

This is the line flagged as most promising in the goal, and the heart of the
document. We lay it out link by link, prove what survives, and locate exactly where
it dies.

### 4.1. The five links

Fix a closed disk D = D̄(s₀, r) ⊂ {½ < σ < 1} and a compact rectangle R with
D ⊂ interior(R) ⊂ R ⊂ {½ < σ < 1}; let W = projection onto t of R (the "window").

- **(E1) Moments ⟹ local boundedness for almost all τ.** By the unconditional mean
  square value ([Tit86, Thm. 7.2], integrated in σ over R with dominated convergence
  — the computation of D112's Lemma 2.5), (1/T)∫₀^T (∬_R |ζ(s+iτ)|²dA(s)) dτ → c_R < ∞.
  By Chebyshev, G_M := {τ : ∬_R |ζ(s+iτ)|² dA ≤ M} has lower density
  ≥ 1 − c_R/M − o(1).
- **(E2) Subharmonicity ⟹ normality over G_M.** For τ ∈ G_M, subharmonicity of
  |ζ(·+iτ)|² gives sup_{D'} |ζ(·+iτ)|² ≤ M/(π d₀²) with D' ⊃ D intermediate and d₀ =
  dist(D', ∂R): the family {ζ(·+iτ) : τ ∈ G_M} is uniformly bounded on D', hence
  **normal** (Montel).
- **(E3) B² almost-periods.** E_ε (D112 Lemma 2.2) has positive lower density
  d(ε) > 0, unconditionally (Kronecker–Weyl + unique factorization).
- **(E4) Intersection and extraction.** For M ≥ M(ε) := 2c_R/d(ε), the set
  E_ε ∩ G_M has lower density ≥ d(ε)/2 > 0; in particular it is unbounded. Montel
  over it: there exist τ_k → ∞, τ_k ∈ E_ε ∩ G_M, and g_ε ∈ H(D') holomorphic with
  ζ(·+iτ_k) → g_ε uniformly on D.
- **(E5) Identification.** Is g_ε = ζ|_D (or at least ‖g_ε − ζ‖_{∞,D} ≤ φ(ε) → 0)?
  If so, diagonalizing over ε → 0 produces LP-112's sequence. **This is the link in
  question.**

**What remains proved (candid record): E1–E4 are theorems**, assembled from
unconditional pieces (moments, subharmonicity, Montel, Kronecker–Weyl). The delicate
point flagged in the goal — compatibility between the normality set (density 1−δ) and
the B² almost-period set (positive density) — resolves CLEANLY in our favor: the
intersection has positive density, no fine argument is needed. The chain delivers, for
every ε > 0, sequences τ_k → ∞ within the B² almost-periods along which
ζ(·+iτ_k) converges uniformly on D to a holomorphic limit g_ε.

### 4.2. Link E5 dies: the supports of the two pieces of information are disjoint

What we know about the limit g_ε, exactly:

**(α) From uniform convergence on D:** information about ζ(s+iτ_k) for
s ∈ D — i.e. about the values of ζ on the translates D + iτ_k. Heights:
t ∈ W + τ_k.

**(β) From τ_k ∈ E_ε:** $\limsup_T \frac1T\int_0^T |\zeta(\sigma+it+i\tau_k) -
\zeta(\sigma+it)|^2 dt < \varepsilon^2$ — an average over ALL t ∈ [0,T], T → ∞.

The identification question is: does (β) force g_ε ≈ ζ in D? The answer is no, and
the reason is D112's Obs. 2.4 in sharpened form:

**Proposition 4.1 (B² goodness carries not even one bit of information about the
window).** Let τ ∈ E_ε. The condition τ ∈ E_ε is invariant under modifying
ζ(σ+i·) — or its translate — on any compact set of heights t: the B² seminorm
assigns upper weight zero to every compact (D112, Obs. 2.4). In particular, for the
functional that LP-112 needs —
sup_{s∈D}|ζ(s+iτ)−ζ(s)|, supported on heights t ∈ W, a fixed compact — membership
τ ∈ E_ε imposes no bound, not even on average over τ ∈ E_ε. ∎

That is: **information (β) lives in the global average over t and weighs zero on W;
the required identification lives entirely in W.** The supports in the t coordinate of
what we know and of what we need are disjoint (modulo null weight). It is not that the
estimate is insufficient: it is that the certificate τ_k ∈ E_ε ∩ G_M is logically
compatible both with g_ε = ζ|_D and with g_ε arbitrarily far from ζ|_D.

**And under H(m) the direction is proved AGAINST it (the same theorem of D112):**
D112's Prop. 2.6 applies verbatim to the disk D anchored at the off-critical zero: the
set A_ε' = {τ : sup_D |ζ(s+iτ)−ζ(s)| ≤ ε'} has upper density zero for
ε' < η. Since E_ε ∩ G_M has positive lower density, **almost every τ of the chain is
bad**: the proportion of τ ∈ E_ε ∩ G_M ∩ [0,T] whose translates approach
ζ|_D tends to 0. The limits g the chain "sees" generically are those of Bagchi's
support — nonzero on D (Hurwitz) — while ζ|_D vanishes at ρ₀. The Montel+B² chain
dies, then, **at exactly the same point as D112 Prop. 2.6/Obs. 2.4**: not in
compactness (E1–E4 survive), but in the fact that the only information available for
selecting τ is blind — by definition of the seminorm — to the place where the signal
is. The combination with normality does not save it: normality adds compactness
(limits exist), not selection (which limit). D112 §2.3(c) already said it in one line
("Montel guarantees limits, not which ones"); the fine analysis confirms there is no
loophole: the B² input contributes exactly zero to link E5.

### 4.3. Second point of death, independent: the blowup M(ε) → ∞

Even if E5 had a partial mechanism ("g_ε is at distance φ(ε) from ζ in some weak
norm"), the diagonal ε → 0 faces a quantitative non-uniformity: the normality bound
is M(ε) = 2c_R/d(ε), and d(ε) — the density of the B² almost-periods — is of order
(2η)^{π(X(ε))} with X(ε) ≍ ε^{−2/(2σ−1)} (D112, Lemma 2.2): super-exponentially
small in 1/ε. The family {g_ε} has no uniform bound as ε → 0; the set of accessible
limits grows without control exactly when the requested precision increases. This is
not the main wall (E5 dies first), but it also closes off the variant "approximate
identification + diagonal". Quantitative GAP declared: we do not prove that no
diagonal works — we prove that this chain does not feed it.

### 4.4. The re-anchoring-by-composition attempt — and its collapse to D104 §5.4

One genuine idea remains to audit: the B² goodness of τ, although it weighs zero on the
fixed window W, guarantees pointwise goodness on MANY windows (positive density of
heights t where |ζ(σ+it+iτ) − ζ(σ+it)| is small — by Chebyshev on the integral in
(β)). Can two almost-periods be composed to drag the goodness toward W? Scheme: if τ
and τ' are good on the same moving window W₁ (it exists by positive density of both
height sets), then τ − τ' is a "local almost-period in W₁ + τ'". This
produces, unconditionally, pairs (τ̃, window) with local self-approximation —
**at an uncontrolled window position**. LP-112 needs the FIXED window W (the zero's).
The composition mechanism translates the event, never anchors it: the position of W₁
is chosen by density (generic), not by the argument. This is exactly the collapse of
the **anchored window** of D104 §5.4: self-approximation "somewhere" is cheap (indeed
it is essentially the content of Bagchi's limit theorem); self-approximation "here"
has provably exactly zero density. The re-anchoring reproduces the wall, it does not
avoid it. Verified against D104: same structure, another coordinate (pairs of
almost-periods instead of the slow copy ζ(s+idτ)).

### 4.5. The exact missing lemma: LP-113

The above dissection leaves a single missing statement, worth naming and isolating:

**Lemma LP-113 (almost-period anchoring; OPEN).** *Let W ⊂ ℝ be a fixed compact
window and B ⊂ (½,1) a compact interval of abscissas. There exists a sequence
ε_k → 0 and almost-periods τ_k ∈ E_{ε_k}, τ_k → ∞, whose goodness localizes in W:*
$$\int_W \sup_{\sigma \in B} |\zeta(\sigma+it+i\tau_k) - \zeta(\sigma+it)|^2\,dt
\;\longrightarrow\; 0$$
*(or the area version ∬_{B×W}, which suffices: subharmonicity promotes it to sup on
interior disks, and Rouché does the rest — D112 §2.3(b), "the localizer exists").*

Relations (all with immediate proof given D112's pieces): LP-113 ⟹ LP-112
(for disks D ⊂ interior(B×W); subharmonicity + extraction); RH ⟹ LP-113 (strong
recurrence gives positive density of τ with sup goodness on B×W, which contains the
integrated version; and A_ε ∩ E_ε ≠ ∅ under RH by densities); under H(m) the
witnesses of LP-113 for the zero's window form an upper-density-zero set (LP-113's
condition implies that of A_ε via subharmonicity, and D112's Prop. 2.6
applies). LP-113 does not imply RH by known dictionaries (same analysis as
D112 §5.4: its conclusion under ¬RH is m = ∞, consistent). **LP-113 is the distilled
form of the missing non-generic-selection mechanism: converting global mean goodness
(theorem, positive density) into goodness localized on ONE prescribed window
(density zero under the hypothesis being refuted).** It is not RH-equivalent; it is
exactly the edge of P43's master quantifier that LP-112 already exposed, now in
window coordinates instead of disk coordinates.

### 4.6. Verdict on the chain

**The Montel+B² chain does NOT close LP-112 and does NOT die at a new point: it dies
at D112 Prop. 2.6/Obs. 2.4** (link E5, identification), with a second independent
blockage in the diagonal (§4.3) and with the re-anchoring collapsing to D104 §5.4
(§4.4). It survives as a program only in the form of lemma LP-113 — which is a more
localized reformulation of the same gap, not a path toward it. The value of the
analysis: (i) E1–E4 are theorems and are recorded (compactness was never the
problem); (ii) the gap is reduced to its minimal form — one link, one window, one
bit of localization; (iii) it is proved that **no improvement of the E1–E4 estimates
can close E5**, because E5 is not an estimate: it is a selection within a set that
all of E1–E4's machinery classifies as exceptional.

---

## 5. Stepanov and Weyl: the structural exit and its closure by growth

### 5.1. The intermediate classes and the decisive property

Between Bohr (uniform) and Besicovitch (B², global mean) lie the Stepanov and Weyl
classes (Besicovitch 1932, Ch. II; Levitan–Zhikov, *Almost Periodic Functions and
Differential Equations*, standard reference):
$$\|f\|_{S^p}^p = \sup_{x\in\mathbb{R}} \int_x^{x+1} |f(t)|^p\,dt, \qquad
\|f\|_{W^p}^p = \lim_{L\to\infty}\ \sup_{x\in\mathbb{R}} \frac1L\int_x^{x+L} |f(t)|^p\,dt,$$
with f being S^p- (resp. W^p-) almost-periodic if it is a limit in that norm of
trigonometric polynomials (equivalently, relatively dense almost-periods in that
norm).

**The decisive property, and why the goal points to this line:** the S² seminorm
**does not annihilate compacts** — the sup over the position x of the window
includes the zero's window W. If ζ were S²-almost-periodic (band version, see
below) in a sub-band of the strip, then for S² almost-periods the local integral
∫_W |ζ(σ+it+iτ)−ζ(σ+it)|²dt would be controlled IN THE ZERO'S WINDOW, subharmonicity
would promote it to sup on disks (D112 §2.3(b): "the localizer works") and Rouché
would close: **S²-a.p. in a band ⟹ LP-112 (in fact, with relatively dense
almost-periods — more than LP-112).** D112's Prop. 2.6 argument would not obstruct
proving the premise, because Prop. 2.6 obstructs global-mean-type certificates, and
S² is local-mean. The whole question then reduces to: is ζ S²-almost-periodic on
bands of the strip?

### 5.2. Answer: no — unconditional theorem, by growth

First the correct form of the statement Rouché needs. Subharmonicity promotes
**area integrals**, so the useful version is the band one: for a closed band
B = [σ₁,σ₂] ⊂ (½,1), consider ζ as a function
t ↦ ζ(·+it) ∈ L²(B) and the vector Stepanov norm
$$\|\zeta\|_{S^2(B)}^2 := \sup_{x} \int_x^{x+1}\!\!\int_{\sigma_1}^{\sigma_2}
|\zeta(\sigma+it)|^2\,d\sigma\,dt.$$

**Lemma 5.1 (almost-periodicity ⟹ boundedness; standard).** If f is S^p-almost-periodic
(scalar or vector-valued), then ‖f‖_{S^p} < ∞: f is at distance < ε from a
trigonometric polynomial P in S^p norm, and ‖f‖ ≤ ε + ‖P‖ with ‖P‖_{S^p} < ∞.
[Besicovitch 1932, Ch. II; immediate from the definition of closure.] ∎

**Theorem 5.2 (ζ is not S^p-almost-periodic on any sub-band of the strip; p ≥ 1,
unconditional).** For every band B = [σ₁,σ₂] ⊂ (½,1) with σ₁ < σ₂,
‖ζ‖_{S^p(B)} = ∞; in particular ζ is not S^p(B)-almost-periodic.

*Proof.* Let σ ∈ (σ₁,σ₂) and r := min(σ−σ₁, σ₂−σ, ¼)/2 > 0. Unconditionally
(Ω-theorems: [Tit86, Ch. VIII]; quantitative with the resonance method:
H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
Helv. 52 (1977) [via Aistleitner, verified as a prior reference];
C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
vertical lines*, Math. Ann. 365 (2016), arXiv:1409.6035, verified: for
α ∈ (½,1) fixed, max_{t≤T}|ζ(α+it)| ≥ exp(c_α (log T)^{1−α}/(log log T)^α)) there
exists a sequence t_n → ∞ with V_n := |ζ(σ+it_n)| → ∞. By subharmonicity of |ζ|^p
(p ≥ 1; |g|^p is subharmonic for holomorphic g):
$$V_n^p \;\le\; \frac{1}{\pi r^2} \iint_{D(\sigma+it_n,\,r)} |\zeta|^p\,dA
\;\le\; \frac{1}{\pi r^2} \int_{t_n-r}^{t_n+r}\!\!\int_{\sigma_1}^{\sigma_2}
|\zeta(\sigma'+it)|^p\,d\sigma'\,dt,$$
and since r < ½, the time domain fits in a window [x_n, x_n+1] with x_n = t_n − r:
$$\|\zeta\|_{S^p(B)}^p \;\ge\; \pi r^2\, V_n^p \;\longrightarrow\; \infty. \qquad\blacksquare$$

**Corollary 5.3.** The implication of §5.1 (S²-band-a.p. ⟹ LP-112) is correct and
vacuous: its premise is false. The Stepanov route is closed unconditionally — and
note the mode: not by the quantifier wall (density zero, selection), but by
**growth**, just as in uniform Bohr (D112 §2.1(b)). The large values of ζ — which
exist unconditionally on every line of the strip — are incompatible with any
almost-periodicity seminorm that sees fixed-size windows.

**On the single-line version (not band):** if ζ(σ+i·) is S²-bounded on ONE fixed
line, this does not follow from Theorem 5.2 (subharmonicity spreads the mass over a
two-dimensional neighborhood, not over the line itself), and we found no work in the
literature on S²-almost-periodicity of ζ on lines in the strip (searches:
"Stepanov almost periodic zeta function" and variants — no relevant results; the
Bohr/zeta connection appears only via the local-compact notion of §2.1).
Declared status: minor GAP, open — **and irrelevant for LP-112**: Rouché needs area
control (band), and the band version is false.

### 5.3. Weyl annihilates compacts again

For W^p the sup over x is taken BEFORE the limit L → ∞, but the limit wins: for
every compact K, sup_x (1/L)∫_{[x,x+L]} |f·1_K|^p ≤ ‖f·1_K‖^p_{L^p}/L → 0. The
Weyl seminorm annihilates compacts exactly like Besicovitch's; a W²-almost-periodicity
theorem for ζ would have the same defect as D112's Lemma 2.1 for feeding Rouché.
(In case it does hold: the Montgomery–Vaughan computation that gives B² does NOT give
W² — the error term (x+L)^{2−2σ}/L of the approximate formula is not uniform in x
for L fixed; status of W² for ζ: open, not pursued here — of no value for LP-112
because of its blindness to compacts.) Minor GAP declared.

### 5.4. The seminorm dichotomy: the wall in another coordinate

Structural summary of §5, which is a finding of the document:

| seminorm | sees compacts? | is ζ a.p. in the strip? | what kills it |
|---|---|---|---|
| Bohr (global sup) | yes | NO (theorem) | growth (Ω) |
| Stepanov S^p, band | yes | **NO (Theorem 5.2, new here)** | growth (Ω + subharmonicity) |
| Weyl W^p | **no** (annihilates compacts) | open | (useless for Rouché even if true) |
| Besicovitch B² | **no** (annihilates compacts) | YES (theorem, D112 Lemma 2.1) | — (but blind where the signal is) |

**Every seminorm that sees compacts is destroyed by ζ's growth; every seminorm under
which ζ is almost-periodic is blind to compacts.** The boundary between the two
families is exactly the size of the averaging window: fixed window ⟹ dies by
growth; window → ∞ ⟹ survives and goes blind. This is not an accident: ζ's large
values in the strip (unconditional) and the hypothetical off-critical zeros live at
the same localization scale — a fixed window — and any control that saw the zero
would also see the large value and blow up. The growth/localization trade-off is
P43's wall expressed in classical almost-periodicity theory, and it explains with a
single criterion why ALL classical notions fail for LP-112: those that would localize
the zero do not admit ζ; those that admit ζ localize nothing.

---

## 6. Topological dynamics: Birkhoff and the recurrence of individual points

**(a) Direct Birkhoff on ζ's orbit: does not apply because of non-compactness.** The
Birkhoff recurrence theorem (every flow on a nonempty compact has uniformly
recurrent points; every point of a compact minimal system is uniformly recurrent)
requires compactness. The orbit {ζ(·+iτ) : τ ≥ 0} ⊂
H(D(½,1)) with the compact-open topology is NOT relatively compact: relative
compactness in H is equivalent (Montel) to local uniform boundedness, and
sup_τ sup_K |ζ(s+iτ)| = ∞ for every compact K of the strip with nonempty interior
(Ω-theorems again). The closure of the orbit is not compact; Birkhoff produces
nothing about it without more.

**(b) Birkhoff/Poincaré on compactified surrogates: produces GENERIC recurrence, not
ζ's.** Two standard substitutes: (i) the Bagchi measure Q is invariant under the
vertical flow and Poincaré recurrence gives: Q-a.e. point f of
supp Q is recurrent — a.e., generic; ζ under ¬RH is outside supp Q (D112
Prop. 2.6) and a.e. recurrence does not touch it. (ii) On the Kronecker torus Ω
(compact, minimal, uniquely ergodic — D102 §7.1, E1–E3) EVERY point is
uniformly recurrent, including ω₀ — unconditionally. Transferring ω₀'s recurrence
to ζ's requires continuity of the Euler observable Φ at ω₀, and that is exactly
MW-2/RH (D102, Prop. 7.2 and the verdict of §7.3). Verified against D102: the
obstruction of the individual orbit is the same, with no new residue.

**(c) The state of the art of dynamics on "recurrence of a distinguished point":**
the existence theorems for recurrent points (Birkhoff via Zorn/minimality;
Poincaré via measure) are intrinsically non-constructive AND generic: they produce
recurrence "at some point of the minimal set" or "at a.e. point", never at a point
prescribed in advance in a non-compact system. The question "is ζ a recurrent point
of its own translation flow?" IS LP-112 (with the observation that Bagchi
1987 titled his paper exactly in these terms), and topological dynamics does not
have a single theorem certifying recurrence of a non-generic individual point
without compactness of its orbit. No precedent in this category — and with D102's
diagnosis intact: the category is not where the problem is won; it is where it is
best seen why it is lost.

---

## 7. Comparative synthesis: the exact position of LP-112

Table of statements ordered by strength (strongest to weakest), with status and
technique or wall. "⟸ RH" = implied by RH; entries 1–2 are equivalent to
(quasi-)RH.

| # | statement | status | technique that proves it / wall that blocks it |
|---|---|---|---|
| 1 | Strong recurrence SR_0 (positive lower density, every K) | ⟺ RH (Bagchi 1987; precedent: Bohr 1922 for L(χ), relative density) | ⟸: full support under RH (genericity). ⟹: Rouché amplifier × density against N(σ,T)=o(T) |
| 2 | Relatively dense local a.p. of ζ in σ>σ₀ (σ₀<1) | ⟺ "ζ without zeros in σ>σ₀" (§2.1(c), §2.6) | circular: proving it for some σ₀<1 is quasi-RH |
| 3 | **LP-112** (sequence τ_k → ∞, every D; d = 0) | **OPEN**; ⟸ RH; ⟹ m∈{0,∞} (D112 Thm. 2.3); does not ⟹ RH by known dictionaries | wall: density-zero witnesses under ¬RH (D112 Prop. 2.6); non-generic selection (P43); **no precedent** (§§2–6) |
| 4 | S²(band)-a.p. of ζ in the strip [would imply LP-112 and more] | **FALSE** (Theorem 5.2, unconditional) | killed by growth (Ω + subharmonicity) |
| 5 | SR_d, d ≠ 0, ±1 (positive density, two speeds) | unconditional THEOREM (Nakamura 2010; Pańkowski; N–P 2012; P. 2015) | relative equidistribution + Baker / six exponentials; d→0 degeneration mapped in D104 (linear scale, window anchored at 0) |
| 6 | d=0 self-approximation of ζ(s,α) (Hurwitz, α transc. or rational ≠ ½,1) | unconditional THEOREM (strong universality; G–K 2014) | full support = genericity of the point; **not transferable to ζ: Euler compresses the support** |
| 7 | B²-a.p. of ζ on lines of the strip (positive-density almost-periods) | unconditional THEOREM (D112 Lemmas 2.1–2.2) | moments + Kronecker–Weyl; blind to compacts (Obs. 2.4) |
| 8 | Uniform Bohr-a.p. of ζ on some line σ ≤ 1 | FALSE (Ω-theorems) | growth |

**Answer to question (iii):** LP-112 does NOT sit between two proved statements.
It sits **strictly above everything proved for ζ at d = 0** (theorem 7, and
theorems 5–6 which live at d ≠ 0 or in another class) and **strictly below the
RH-equivalents** (1–2). In the intermediate band it inhabits — sequential pointwise
statements for the diagonal point d = 0 — the literature has neither a theorem, nor
a counterexample, nor a living candidate technique: the four entries that would
surround it (3, 4, and the sequential versions of 1–2) are, respectively,
open, refuted, and open with no published work. The asymmetry with the d ≠ 0
boundary is total: there the real Diophantine input (Baker, six exponentials)
reaches exactly to the edge; here no input reaches any part of the interior.

---

## 8. VERDICT on LP-112

**VERDICT: NO PRECEDENT.**

1. **There is no theorem in the literature of sequential self-approximation without
   strong recurrence.** The inventory (§2, exhaustive over the accessible sources:
   Matsumoto's survey, the complete Nakamura–Pańkowski–Garunkštis chain with its
   corrigendum and its withdrawn preprint, the 2025 equivalents) shows that every
   known positive self-approximation result is one of density (of measure or
   relative) and is proved by **genericity of the point** — membership in the
   support of the shift statistics —, whether because the support is full
   (Hurwitz, Euler-free classes: §3.1), whether because there is relative
   equidistribution to exploit (d ≠ 0: §2.3), whether under RH (d = 0: Bohr 1922,
   Bagchi 1987). The pure sequential statement — certifying non-emptiness where
   the density can be zero — has not a single proved instance in any class of
   functions, and in the B² category where ζ has its unconditional theorems the
   statement is not even a property of the equivalence class (§3.4).

2. **The technique LP-112 requires is specified negatively:** a mechanism of
   **non-generic selection with anchoring** — producing an almost-period whose
   global mean goodness localizes in a prescribed compact window (lemma
   LP-113, §4.5). The three audited candidates die at exact and distinct points:
   **Montel+B²** dies at the identification of the limit (link E5,
   §4.2) — the same point as D112 Prop. 2.6/Obs. 2.4, with the B² information
   and the compact-open information having disjoint supports in t, and with the
   composition re-anchoring collapsing to the anchored window of D104 §5.4;
   **Stepanov** — the only classical seminorm that would see the window —
   dies by growth, unconditionally (Theorem 5.2, new here; the seminorm
   dichotomy of §5.4: what would localize the zero does not admit ζ, what admits
   ζ localizes nothing); **Birkhoff/Poincaré** dies by non-compactness of the
   orbit and genericity of its conclusions, with the obstruction reduced —
   without residue — to the discontinuity of the Euler observable at ω₀ (D102).

3. **A real chance of unconditional proof with what was examined? Not with these
   chains.** The Montel+B² chain does not close and cannot close by improving
   estimates: E1–E4 are theorems and E5 is not an estimate but a selection in an
   exceptional set. It survives as a program only in the form of the lemma
   **LP-113** (almost-period anchoring), which is strictly more localized than
   LP-112, is implied by RH, is not RH-equivalent by known dictionaries (its
   conclusion under ¬RH is m = ∞, consistent — same analysis as D112 §5.4) —
   and whose witnesses, under the hypothesis being refuted, form exactly the
   same density-zero set. LP-113 is not a step toward LP-112: it is its minimal
   form. The wall between both and the literature is P43's master quantifier,
   and this document adds its seminorm coordinate (§5.4) and its certificate of
   non-precedence (§§2–3) to the record.

4. **For the phase:** LP-112 is confirmed as a genuinely new target — there is
   no theorem to adapt, no technique to import, no bridging class in which to
   test it (the only class with proved d = 0 self-approximation gets it by full
   support, which ζ loses by having an Euler product — the structural irony of
   §3.1). If the program decides to attack it, the front is LP-113 and the
   underlying physical question is one of anchoring: what arithmetic property of
   ζ — finer than the independence of {log p}, which is already fully spent in
   D112's Lemma 2.2 — could correlate the phase of the Kronecker flow with a
   prescribed window of the vertical axis. Today there is no candidate.

---

## References

**Internal (backward-only):** Doc 112 (LP-112, Thm. 2.3, Prop. 2.6, Obs. 2.4, Lemmas
2.1–2.2, §2.3, §5.4); Doc 111 (cosh-examples; Obs. 2.4); Doc 109 (architectural
identity); Doc 104 (effective SR_d; anchored window §5.4; linear degeneration);
Doc 102 (Bagchi audit; Prop. 7.2; §6.3 family d; §7 Euler observable);
P43 (Principle 3.1); P41 (Problem 8.1).

**Literature (verification status indicated):**

- H. Bohr, *Über eine quasi-periodische Eigenschaft Dirichletscher Reihen mit
  Anwendung auf die Dirichletschen L-Funktionen*, Math. Ann. 85 (1922). [Statement
  verified via Herichi–Lapidus and standard expositions; original NOT VERIFIED.]
- H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918).
  (Uniform a.p. in half-planes of absolute convergence; via D112.)
- H. Bohr, E. Landau, Rend. Circ. Mat. Palermo 37 (1914). (Off-critical density
  o(T); via D112.)
- B. Bagchi, thesis, Indian Statistical Institute, 1981; and *Recurrence in topological
  dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50 (1987), 227–240.
  [Verified via Matsumoto/D102.]
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014). [Full text consulted in previous sessions (D102); master
  source of §2.]
- S. M. Voronin, Izv. Akad. Nauk SSSR Ser. Mat. 39 (1975), 475–486. [Via
  Matsumoto/D102.]
- T. Nakamura, *The generalized strong recurrence for non-zero rational parameters*,
  Arch. Math. 95 (2010), 549–555. [Verified (Springer).]
- T. Nakamura, Ł. Pańkowski, corrigendum, Arch. Math. 99 (2012), 43–47;
  arXiv:1203.1393. [Verified.]
- T. Nakamura, *A simple proof of the generalized strong recurrence for any non-zero
  parameter*, arXiv:1006.3184. [**Withdrawn by the author** — verified on arXiv;
  cited as mapping data, not as a result.]
- Ł. Pańkowski, *Self-approximation of Dirichlet L-functions*, arXiv:1006.1507.
  [Title and content verified at abstract level.]
- Ł. Pańkowski, *Joint universality and generalized strong recurrence with rational
  parameter*, arXiv:1503.06931. [Verified: every rational d ≠ 0, ±1.]
- T. Nakamura, Ł. Pańkowski, *Self-approximation for the Riemann zeta function*,
  Bull. Aust. Math. Soc. (2012/13). [Abstract verified via Cambridge Core; volume
  and pages NOT VERIFIED.]
- R. Garunkštis, E. Karikovas, *Self-approximation of Hurwitz zeta-functions*,
  Funct. Approx. Comment. Math. 51 (2014), 181–188. [Verified (Project Euclid).]
- J. Andersson, R. Garunkštis, R. Kačinskaitė et al., *On self-approximation of the
  Riemann zeta function in short intervals*, Symmetry 17 (2025), art. 2075. [Existence
  and main thesis verified via search engine; full text NOT VERIFIED (403);
  author list partially verified.]
- A. Laurinčikas, *On equivalents of the Riemann hypothesis connected to the
  approximation properties of the zeta-function*, Axioms 14 (2025), 169. [Verified
  at abstract level.]
- A. Reich, *Werteverteilung von Zetafunktionen*, Arch. Math. 34 (1980). [Via
  Matsumoto; original NOT VERIFIED.]
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996.
  (Bagchi's apparatus; via D112.)
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
  (Thm. 7.2; Ch. VIII: Ω-theorems.)
- H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
  Helv. 52 (1977). [Cited as a precedent of Aistleitner's result, per
  Aistleitner himself; original NOT VERIFIED.]
- C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
  vertical lines*, Math. Ann. 365 (2016); arXiv:1409.6035. [Verified: abstract and
  main statement.]
- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge, 1932. (Classes S^p, W^p,
  B^p, Ch. II; a.p. ⟹ boundedness in the respective norm.)
- B. M. Levitan, V. V. Zhikov, *Almost Periodic Functions and Differential
  Equations*, Cambridge, 1982. [Standard reference for the Stepanov/Weyl classes;
  not load-bearing.]
- H. Herichi, M. L. Lapidus, *Truncated infinitesimal shifts, spectral operators and
  quantized universality of the Riemann zeta function*, arXiv:1305.3933. [Verified
  secondary source of Bohr's 1922 statement.]
- B. Jessen, H. Tornehave, Acta Math. 77 (1945). (Theory of mean zero densities of
  a.p. functions; via D112 §6.2.)
- H. Davenport, H. Heilbronn, J. London Math. Soc. 11 (1936). (Via D112.)
- H. Montgomery, R. Vaughan, J. London Math. Soc. (2) 8 (1974). (Via D112.)

*End of Document 113.*