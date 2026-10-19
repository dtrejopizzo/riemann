# Doc 121 — Gap analysis: the CC machinery measured against the forced axioms

**Program:** Riemann Hypothesis — Phase 39, G1↔G2 interface
**Prerequisites:** Doc 119 (axioms R-SIG, R-FIN, R-LEF-{POLE,PRIMES,REG,FLOW}, R-WEIGHT(a)(b), R-NC, R-TRZ-1/2; order R-SIG ≺ R-FIN ≺ R-LEF ≺ Newton; tensions T1–T4); Doc 120 (in-source inventory of the CC/CCM corpus,; roadmap-rh (nodes G1–G4, routes A/B, specification S1–S3, Thm. rank-sensitivity); Doc 110 (Thm. 4.3 impossibility in ℱ; Prop. 4.5); Doc 108 (per-window binarity); Doc 105 (Thm. 5.5, Mertens divergence); Doc 100 (archimedean positivity; Obstruction O_SL); P35 (κ(Q)=2m); P43/P44 (master quantifier; dichotomy).

**Labeling discipline (absolute rule of this phase):** every statement carries ONE label:
**[REQUISITE]** = derived in Doc 119. **[DATA]** = verified: from the CC corpus via Doc 120
(with its citation), or a theorem of the program (with internal citation). **[GAP]** = what is missing, with
precision (which property, in which space, with which quantifier). **[CONJECTURE-INTERFACE]**
= bridge proposal, ALWAYS as a conjecture, with its falsifier. **[NOT VERIFIED]** = from
memory or not found in source. NEVER "proved" for anything new. A false victory is
worse than a failure.

**Gap rating scale:**
- **COSMETIC** — notation/translation; closable by rewriting.
- **TECHNICAL** — hard work but of a known type (there is a method with precedent).
- **CONCEPTUAL** — new mathematics; no method with direct precedent.
- **POSSIBLY-EQUIVALENT-TO-RH** — closing the gap looks like RH-in-disguise (fails the test
  R-NC of Doc 119 at some link, or the link is on the NO-GO-LIST).

---

## 0. Executive summary

Axiom-by-axiom measurement (§1) and the four crossings (§2) produce this miniature map:

| axiom (Doc 119) | closest CC piece (Doc 120) | gap rating |
|---|---|---|
| R-SIG | Serre/Pontryagin duality with tolerance (2205.01391, Thm 1.2) | **CONCEPTUAL** (with finite sub-experiment: crossing A) |
| R-FIN | integer dimensions dim_𝕊 in dim 1 (2306.00456) | **CONCEPTUAL** (blocked upstream by R-SIG; the Newton mechanism is TECHNICAL once there is N₀) |
| R-LEF-POLE | archimedean positivity/realization (2006.13771; Doc 100 §4) | **TECHNICAL** (partial fire test already passed) |
| R-LEF-PRIMES | C_p orbits of the scaling site + Connes 1999 trace | **TECHNICAL conditional on G1** (the identity exists; the cohomological carrier is missing) |
| R-LEF-REG | Weil principal value; divergent term 2h(1)log λ pending (2602.15941 §9.3) | **TECHNICAL**, with declared risk T2 |
| R-LEF-FLOW | Frobenius flow 𝔽r_λ; correspondences Ψ(λ) | dynamical half: **TECHNICAL**; grading half: **CONCEPTUAL** |
| R-WEIGHT(a) | (nothing; only the integers of the site: slopes, degrees) | **CONCEPTUAL** — the heart of the wall |
| R-WEIGHT(b) | CC 2021 archimedean positivity as "germ of the Hodge index" (quote §4.4 Doc 120) | **CONCEPTUAL** in geometric form; **POSSIBLY-EQUIVALENT-TO-RH** in full analytic uniformization (MW-6/O_SL) |
| R-NC | (it is a test, not a gap) | transversal; applied in §2 |
| R-TRZ-1 | C_c^∞ tests with compact support of the semilocal frame | **TECHNICAL**, with the generating-richness step threatened by O_SL |
| R-TRZ-2 | (ordering discipline) | **COSMETIC** as a statement; blocked upstream |

Verdict of the crossings: **(A)** duality→signature: the self-dual divisor EXISTS and is
explicit (D₀ = −{2}, exactly K−D₀ = D₀, with χ(D₀) = 0: the analogue of a
theta characteristic); the crossing produces a decisive finite experiment (is the induced
pairing symmetric or alternating?) — but even in the best case it lives in dimension 1,
where there are no zeros: it is the PROTOTYPE of the mechanism, not the mechanism. **(B)**
tolerance→square: the best-rated gap in the document (TECHNICAL, high value, zero
RH risk); concrete test case: C_p × C_p. **(C)** Pick/Loewner→inertia: the truncated
Weil matrix is exactly a Loewner/Nevanlinna-type kernel and classical theory
(Krein–Langer, classes N_κ) is inertia theory — but the rigorous analysis (§2.3.4)
shows that **it falls within class ℱ of Doc 110 Thm 4.3**: it does not evade the impossibility
theorem; its real value is as Route B infrastructure *after* R-FIN.
**(D)** Jacobian→spectral flow: speculative, CONCEPTUAL, to be shelved.

**Minimal decisive experiment of the phase (§3.3):** compute the symmetry character of
the pairing induced by Serre duality with tolerance at the self-dual point
D₀ = −{2}. Finite, within the CC category, two clean outcomes.

**Synthesis (§4):** G1 is "they almost have it and haven't crossed it" (years); G2 is
"nobody has a signature anywhere in the corpus" (no frank upper time bound); and the
master quantifier reappears, in geometric language, in exactly
two identified places: semilocal→global uniformization and class membership
in Krein–Langer.

---

## 1. THE CENTRAL TABLE: axiom by axiom

Format of each section: (a) closest CC piece [DATA]; (b) what exactly it gives today;
(c) the precise GAP; (d) the shortest bridge [CONJECTURE-INTERFACE], if any, with
falsifier; (e) rating.

### 1.1. R-SIG — weight grading with integer signature

**[REQUISITE]** (Doc 119 §2.3). W-graded decomposition of H, stable under the flow,
additive weights under ⊗, duality w ↔ 2d−w, and an internal criterion (form, polarization or
absolute value) that decides membership without external input; the grading as a
primitive datum, NOT the spectrum of the generator.

**(a) Closest piece.** **[DATA]** (Doc 120 §3.2, arXiv:2205.01391 Thm 1.2): Serre
duality with tolerance for Spec ℤ̄ over 𝕊[±1]:
H⁰(K−D) ≅ Hom_{ΓT∗}(H¹(D), U(1)_{1/4}), with canonical divisor K = −2{2}
(deg K = −2 log 2) and dualizing module U(1)_{1/4} = H¹(K). It is the corpus's only
genuine duality pairing. Secondary: **[DATA]** (Doc 120 §7.2) the coexistence of Dim_ℝ
(type II, 1603.03191) and dim_𝕊 (integer, 2306.00456): CC have already crossed "averages → integers"
in dimension 1 *for dimensions*.

**(b) What it gives today.** A **perfect** duality pairing **between two
different spaces** (H¹ of the divisor against H⁰ of the dual divisor), with values in U(1) and with a
tolerance relation (not a strict equality) as a constitutive part. Integer dimensions of
both sides. Duality symmetry D ↔ K−D — the formal analogue of w ↔ 2d−w in
degrees: deg D + deg(K−D) = deg K, constant. Nothing else: **[DATA]** (Doc 120 §7.7,
negative search) the word "signature/inertia index" does not appear as an invariant
in any text read in the corpus; the only sign structure is
positivity/lower-boundedness.

**(c) [GAP]** With quantifiers: a bilinear (or quadratic, or hermitian)
form B: V × V → ℝ (or to an ordered set where "signature" makes sense) is missing, over ONE space V
associated functorially to the site (ultimately: to the square), such that (i) B is
symmetric — not alternating —, (ii) its inertia (p, q) is defined and stable, (iii)
a grading W exists with V_impure = support of the indefinite part. Today: B does not exist,
V does not exist, W does not exist, in any dimension, over any base. What exists is the
ingredient from which B is classically FABRICATED: a perfect duality plus a candidate
involution (D ↦ K−D).

**(d) [CONJECTURE-INTERFACE]** That of crossing A (§2.1): the explicit fixed point D₀ = −{2}
of the Serre involution turns the duality into a single-divisor pairing, and
the sum H⁰(D₀) ⊕ H¹(D₀) carries an induced form whose symmetry is decidable by finite
computation. Falsifiers in §2.1.5. Even if the bridge is built, it remains in dimension 1: the
space carrying the zeros is elsewhere (see (e)).

**(e) Rating: CONCEPTUAL.** The duality→form translation is classical (COSMETIC in
ordinary geometry), but here there are three non-classical obstructions: tolerance (does it break
bilinearity?), the dualizing module U(1) (can it be linearized to ℝ with signs?), and — the
decisive one — that everything happens in dimension 1, where H¹(D) ≅ U(1)_λ is tiny and **sees no
zeros**. The true R-SIG must live on the square (G1), which does not exist. The gap is
new mathematics with a finite experiment inside.

### 1.2. R-FIN — finiteness of the impure part of H¹, a priori, bounding κ(Q)

**[REQUISITE]** (Doc 119 §2.4): dim(⊕_{w≠1} gr^W_w H¹) < ∞, bounded a priori by site
data, with an accompanying theorem "every negative direction of Q comes from there"
whose proof does not mention zeros. Not statable without R-SIG.

**(a) Closest piece.** **[DATA]** (Doc 120 §3.3, arXiv:2306.00456): integer
dimensions dim_𝕊 H⁰(D), dim_𝕊 H¹(D) in dimension 1, with exact RR formula
χ(D) = ⌈deg₂ D⌉′ + 1 ("perfect analogy with genus 0", CC's own wording), and H¹(D) ≅
(U(1), d)_λ explicit with dim = m if 2^{−m−1} ≤ λ < 2^{−m}. Secondary: **[DATA]**
(Doc 120 §7.4, 2511.22755 Prop. 3.3): QW_λ is bounded below — CCM work de facto
in the κ < ∞ regime without ever naming the negative index as an invariant.

**(b) What it gives today.** Computed integers from the site (from the absolute base), with no zero
input: exactly the "Euler characteristic" half of the fire test of Doc 119
§2.5. The other half — the accompanying theorem — does not exist and cannot yet exist:
**[DATA]** (Doc 120 §8, row S1) all of CC's RR produces Euler characteristics,
never signatures; **[DATA]** (Doc 119 §2.2, Doc 110 §5.2 L6) an Euler characteristic
does not determine inertia at infinite rank.

**(c) [GAP]** Double, and ordered: (i) statability gap — without W (R-SIG) there is no
"impure part" to measure; the missing quantifier is "∃ V ⊂ H¹ functorial, dim V ≤ N₀
computable from the site, ∀ negative direction of Q: comes from V"; (ii) carrier gap —
CC's integers are those of Spec ℤ̄ in dimension 1; the impure part, if it exists, lives in
H¹ of the square (the classes associated with off-critical quadruples are objects of the analogue
of NS(C×C), not of Pic(C)).

**(d) [CONJECTURE-INTERFACE]** The shortest one available is derived, not direct: if
crossing B (§2.2) delivers an H¹ of the square with integer-type dimensions, and crossing
A delivers the duality→form mechanism, then N₀ = dim_𝕊 (impure graded piece of the square's H¹)
would be the candidate. Immediate falsifier inherited from Doc 119 §2.4: if the H¹ of the
square turns out finite-dimensional IN TOTAL, the proposal dies by T1 (a finite H
cannot carry the trace with singular support at {k log p}); the finiteness must be of a
graded piece, and that again presupposes R-SIG.

**(e) Rating: CONCEPTUAL** — but precisely: the component "reading inertia from N₀
traces" is TECHNICAL and already proved (**[DATA]** Doc 110 Prop. 4.5; roadmap Thm.
rank-sensitivity); the component "obtaining N₀ from the site via the accompanying
theorem" is CONCEPTUAL and is, together with R-WEIGHT, the wall itself. Flagged risk: if
someone proposes obtaining N₀ as a limit of per-window bounds, that is on the
NO-GO-LIST (**[DATA]** Doc 108 Prop. 2.5 via Doc 110 Thm 4.3(b): a uniform per-window
index bound is RH-tollway) — that variant would be POSSIBLY-EQUIVALENT-TO-RH and must
be rejected at the door.

### 1.3. R-LEF-POLE — rank-one H⁰/H² producing ĥ(±i/2)

**(a) Closest piece.** **[DATA]** (Doc 100 §4 via Doc 119 §3.2; CC Selecta 27
(2021)): the archimedean + polar term of the Weil explicit formula has a positive
operator realization on support (1/2, 2) — the only partial fire test already passed by
the CC candidate. Also **[DATA]** (Doc 120 §3.4, 2602.15941 §9): the action of C_ℚ on
the framed Picard group produces a Lefschetz-type trace formula with localization at
periodic orbits.

**(b) What it gives today.** The correct VALUES of the polar block in a window, from an
operator construction. It does not give: the carriers H⁰, H² as cohomological objects of
rank 1 and weights 0 and 2 with the flow acting via the trivial characters.

**(c) [GAP]** It remains to exhibit, in the theory of the square (once it exists), two rank-one
objects whose flow trace is exactly ĥ(−i/2) + ĥ(i/2), ∀ h in class 𝒯. In
absolute dimension 1 there is an unexplored natural candidate: H⁰(0) and H¹(K) = U(1)_{1/4}
(the dualizing module itself) as analogues of H⁰ and H² of the curve. **[NOT VERIFIED]** that CC
make that identification anywhere.

**(d) [CONJECTURE-INTERFACE]** The pair (H⁰(0), H¹(K)) of the absolute RR is the pair
(H⁰, H²) of the curve-object, and the trace of the scaling flow on them reproduces the
polar block. Falsifier: finite computation — the action of ℝ₊^× on U(1)_{1/4} is
determined in its category; if the resulting character is not the modulus (the scaling
character), the identification is false. It is a verification of a known type.

**(e) Rating: TECHNICAL.** The only axiom where the candidate has already passed half the test.

### 1.4. R-LEF-PRIMES — local traces = distributions W_p

**(a) Closest piece.** **[DATA]** (Doc 120 §2.2): the periodic orbits
C_p = ℝ₊^*/p^ℤ of the scaling site, one per prime, of length log p — the local structure
requested exists as GEOMETRY. And **[DATA]** (Doc 119 §3.4; Connes, Selecta 5
(1999)): the distributional trace of the flow over the adele class space
reproduces the arithmetic side term by term — the identity is a theorem, in the
adele realization.

**(b) What it gives today.** The two halves separately: the local geometry (C_p, with its
tropical RR, Jacobian ℤ/(p−1)) and the analytic identity (Connes trace). It does not give: the
local trace computed FROM the cohomology of an H of the square, because that H does not exist.

**(c) [GAP]** With quantifier: ∀ p, the local trace of the flow on the piece of H
corresponding to C_p (or on the fiber of the correspondence at p) must = W_p, computed
from H with both sides independent (R-LEF-FLOW fire test of Doc 119: if it is
a definition, G3 is vacuous). The gap is not the identity — it is the carrier.

**(d) [CONJECTURE-INTERFACE]** If crossing B produces H¹ with tolerance over C_p × C_p,
the trace of the Frobenius correspondence restricted to that piece should give W_p; the
test case of §2.2 includes this verification as its step 4. Falsifier: the trace
computed gives W_p only after a p-dependent normalization not explainable by Guillemin's
transverse determinant.

**(e) Rating: TECHNICAL conditional on G1.** Without G1 there is nowhere to compute; with G1,
the pattern (Guillemin + Connes 1999) is of a known type.

### 1.5. R-LEF-REG — archimedean regularization as counterweight

**(a) Closest piece.** **[DATA]** (Doc 100 §5 via Doc 119): the per-place additivity
of the geometric side of Weil is unconditional, and the archimedean place has its
realization (CC 2021). **[DATA]** (Doc 120 §3.4): in 2602.15941 §9.3 there remains a
divergent term 2h(1) log λ in the semilocal formula "whose rigorous treatment is
pending" — CC are touching exactly this wall right now.

**(b) What it gives today.** The Weil principal value works in the classical analytic
explicit formula; in the new geometric realization (Picard/Jacobian 2026) the
divergence reappears untreated.

**(c) [GAP]** Missing: a local archimedean contribution of the SAME FORMAL TYPE as the
p-adic ones (orbit/point of the site) such that the trace identity holds for the
regularized total sum, in a test class with margin ε. And — tension T2 (Doc 119
§6.3) — declared compatibility with R-SIG: the signature must be defined before the
regularizing limit, not read off it. **[DATA]** (Doc 105 Thm. 5.5): at the boundary of the
Weil class the sum of primes diverges Mertens-style; any theory inheriting that
boundary inherits the illegitimacy of term-by-term reading.

**(d) [CONJECTURE-INTERFACE]** The point {2} already plays, in the absolute RR, the role of "point
at infinity" (reading registered in Doc 120 §3.3); conjecture: the archimedean
place of the site admits a presentation as a degenerate orbit (infinitesimal length)
whose regularized transverse determinant IS the Weil principal value.
Falsifier: if the term 2h(1) log λ of 2602.15941 §9.3 is not cancelable by ANY
local contribution from the boundary of the Picard monoid (the boundary phenomena that CC
declare constitutive), the presentation does not exist in their framework.

**(e) Rating: TECHNICAL** — with the caveat that it is the requisite with no analogue
in char p (Doc 119 §3.3): "of a known type" here means "of the type of Weil 1952 and
Connes 1999", not "off-the-shelf".

### 1.6. R-LEF-FLOW — Guillemin trace + grading independent of the spectrum

**(a) Closest piece.** **[DATA]** (Doc 120 §1.3, 1502.05580 Thm 1.1): the scaling flow
IS Frobenius (the action of 𝔽r_λ on points = idele class group); and Thm 1.2: the
semigroup of correspondences Ψ(λ) over the square, with exact composition
for λλ′ ∉ ℚ. **[DATA]** (Doc 106 Prop. 3.10 via Doc 120 §7.6): on (𝒦, Q) the
Frobenius correspondences act by isometries — they measure, not generate, the defect.

**(b) What it gives today.** The entire dynamical half: flow, correspondences,
distributional trace (in adeles), correct orbits. The structural half — the grading W
as primitive datum within which the flow acts — zero.

**(c) [GAP]** Two: (i) the rational discontinuity of the composition Ψ(λ)∘Ψ(λ′) ≠
Ψ(λλ′) for λλ′ ∈ ℚ — the analogue of "exact Frobenius composition" fails exactly at
arithmetic values; quantifier: ∀ λ, λ′ (without exception) or else a structural
explanation of the exception (is it the boundary phenomenon of the monoid?); (ii) the grading
on which the flow acts: does not exist (it is R-SIG again).

**(d) [CONJECTURE-INTERFACE]** The rational discontinuity of Ψ and the "boundary/singular
phenomena" of the group→monoid step (2602.15941) are the same phenomenon seen in two
places; the correct square must be built over the monoid (not the group) so that
the composition is exact. Falsifier: reformulate Ψ(λ) in the language of the Picard
monoid and verify the composition in a concrete rational case; if the anomaly persists, the
conjecture is false. **[NOT VERIFIED]** — nobody has written Ψ(λ) in that language.

**(e) Rating:** dynamical half **TECHNICAL**; grading half **CONCEPTUAL**
(it is R-SIG). The fire test of Doc 119 ("both sides computed separately")
is not evaluable until there is a carrier.

### 1.7. R-WEIGHT(a) — the invariant w computable from H, not from ρ

**(a) Closest piece.** Strictly: none. The only functorial integers of the
site are **[DATA]** (Doc 120 §2.2, §3): integer slopes of the structure sheaf,
degrees (real, not integer) of tropical divisors, the torsional characteristic
χ ∈ ℤ/(p−1) of C_p, and the dim_𝕊 of the absolute RR.

**(b) What it gives today.** Raw material of integers, with no class-of-zero →
integer assignment at all. **[DATA]** (Doc 120 §8, reading 1): CC have duality but "no
bilinear form on a single space with an inertia index"; the interface question
("what condition makes the diagonal's duality refine into a form with
signature?") is not posed in their corpus.

**(c) [GAP]** The central one of the program: ∀ class c_ρ ∈ H¹ (once H¹ exists), a
w(c_ρ) ∈ ℤ computable by membership in a graded piece / sign under a form or algebraic class that
cuts it — without mentioning ρ. **[DATA]** (Doc 110 Thm 4.3(b); Doc 108 §7.4): within the
class ℱ this is impossible; the gap is building the category WHERE it is possible.

**(d) [CONJECTURE-INTERFACE]** None short and frank. The closest is the composition
of crossings A and B: form at the self-dual point (mechanism) + H¹ of the square with
tolerance (carrier) + sign under the form as the definition of w. Three links, two of
them conjectures themselves. The chain is stated, not shortened.

**(e) Rating: CONCEPTUAL.** It is the wall. With no sub-experiment of its own: its
sub-experiments are those of crossings A and B.

### 1.8. R-WEIGHT(b) — purity as a theorem from geometric positivity

**(a) Closest piece.** **[DATA]** (Doc 120 §4.2, 2006.13771 Thm 1 and Thm 6.11): the
archimedean positivity W_∞(g∗g^*) ≥ Tr(ϑ(g)𝐒ϑ(g)^*) ≥ 0 on support (1/2,2), with
quantified defect 13 < c < 17 in a single direction ĝ(0). **[DATA]** (Doc 120 §4.4,
key quote): CC themselves present it as part of "a novel geometric landscape still in
development for an intersection theory of divisors (on the square of the Scaling
Site)" — for them it IS the analytic germ of the Hodge index of the square.

**(b) What it gives today.** A real unconditional positivity (the only one in the
corpus), with partial overgeneration (holds ∀ test of support in (1/2,2) — partially
passes NC2, **[DATA]** Doc 119 §4.3), in one place.

**(c) [GAP]** With quantifiers, the gap has two forms and ONLY one is legitimate:
- Analytic form: ∀ finite set S of places, semilocal positivity, and uniformization
  S → all places. **[DATA]** (Doc 100, Obstruction O_SL; Doc 119 §4.3, "state of
  the candidate"): uniformization in λ is MW-6 — **this path is on the NO-GO-LIST**.
- Geometric form: a Castelnuovo-type inequality on the square, ∀ divisor
  (not only the graph of the flow), proved by a uniform surface method, from which
  the weight bound follows by Weil's argument. Neither the square with divisors exists.

**(d) [CONJECTURE-INTERFACE]** CC's own, made explicit: their archimedean positivity is the
restriction to the near-diagonal graph of an intersection inequality on the
square not yet formulated. Structural falsifier (NC2 test): once the intersection
theory exists, the inequality must be provable for divisors that do NOT encode ζ
(e.g. divisors supported on a single orbit C_p × C_q); if it can only be verified
for the object that encodes ζ, it was MW-1 in disguise.

**(e) Rating: bifurcated, and it must be said bluntly.** The geometric form:
**CONCEPTUAL** (the Castelnuovo/Mattuck–Tate precedent shows it CAN be
non-circular: a surface theorem that does not know which curve it is). Any variant going
through semilocal→global uniformization in the analytic category:
**POSSIBLY-EQUIVALENT-TO-RH** — it is MW-6, cataloged, and is the threat of §4.3.

### 1.9. R-NC — the non-circularity test

It is not a CC gap but the measuring instrument. Application status: **[DATA]**
(Doc 119 §4.3) CC 2021 positivity passes NC1, partially NC2, and FAILS today NC3 at
the global step (MW-6). In this document, R-NC is applied to each crossing in §2 (results:
crossing A passes NC1–NC2 in its construction, §2.1.6; crossing B passes trivially, §2.2.4;
crossing C fails NC4 — it falls into ℱ, §2.3.4). Rating: **transversal, not ratable**.

### 1.10. R-TRZ-1 — test class with margin and generating richness

**(a) Closest piece.** **[DATA]** (Doc 120 §4.2): the test class of CC's semilocal
framework: g ∈ C_c^∞ with multiplicative compact support (window (1/2,2);
condition Supp(f) ⊂ (p^{−1}, p) growing with S, **[DATA]** Doc 100 §5).

**(b) What it gives today.** The margin ε, solved with room to spare: for multiplicative
compact support, the prime side is a FINITE SUM (only finitely many p^k fall in the
support) — better than the strict requested margin; the Mertens divergence of Doc 105 does not
touch this class. Countability: trivial (separable density of C_c^∞).

**(c) [GAP]** Generating richness (clause (b) of R-TRZ-1) clashes with the geometry of
the window: a test with support in (p^{−1}, p) only "sees" primes < p; for the
family {h_n} to generate (triangularity over even polynomials, Doc 118 Lemma 5.2) the
supports must grow without bound — and uniform behavior under that growth is
exactly Obstruction O_SL. Gap quantifier: ∃ {h_n} ⊂ 𝒯 generating SUCH THAT
the trace identities used by Route B only require each h_n separately
(never uniformity in n).

**(d) [CONJECTURE-INTERFACE]** With R-FIN in hand (N₀ known), N₀ FIXED-support
tests suffice (the first N₀ of the triangular family): uniformity in n
disappears from the circuit because the universal quantifier is truncated. Falsifier: if
compression to the impure block (R-TRZ-2) requires growing-support tests to
separate it, the truncation does not happen and O_SL re-enters.

**(e) Rating: TECHNICAL**, conditional on the order: after R-FIN it is routine; before
R-FIN, any attempt to use this class to read inertia reopens O_SL
(POSSIBLY-EQUIVALENT-TO-RH through that door).

### 1.11. R-TRZ-2 — the order R-SIG ≺ R-FIN ≺ R-LEF/R-TRZ-1 ≺ Newton

**(a)–(b)** Does not correspond to a CC piece: it is program discipline. The relevant
measurement: **[DATA]** (Doc 120 §5.5, registered reading): the CCM "zeta spectral
triples" line de facto violates this order — it evaluates truncated traces and postpones ALL
of the structure to a convergence statement, which is the O_SL pattern.

**(c) [GAP]** None of its own; inherits those upstream.

**(e) Rating: COSMETIC** as a statement (it is a protocol), with detector
value: any interface proposal that evaluates traces before exhibiting N₀ is
rejected by this axiom without examining the rest.

---

## 2. THE PROMISING CROSSINGS

### 2.1. Crossing A — DUALITY→SIGNATURE: the self-dual divisor of the absolute RR

#### 2.1.1. The starting datum

**[DATA]** (Doc 120 §3.2; arXiv:2205.01391, Thm 1.2 and Prop. 5.2): Serre duality with
tolerance H⁰(K−D) ≅ Hom_{ΓT∗}(H¹(D), U(1)_{1/4}), derived from Pontryagin duality
for 𝕊[±1]-modules with tolerance; K = −2{2}, deg K = −2 log 2; integer dimensions of
both sides. The underlying pairing: P: H¹(D) × H⁰(K−D) → U(1), perfect.

**[REQUISITE]** (R-SIG, Doc 119 §2.3, realization (i)): a form on ONE space with
involution, whose signature is the invariant.

The interface question, in its classical form: a duality pairing
P: A × B → U(1) becomes a form on A when there is an isomorphism B ≅ A — that
is, when the divisor is in self-dual position with respect to the Serre involution
σ: D ↦ K−D.

#### 2.1.2. The self-dual divisor exists and is explicit

The fixed-point condition is D ~ K − D, i.e. 2D ~ K = −2{2}. There is a solution **exact
at the level of divisors, not only of classes**:

$$D_0 := -\{2\}, \qquad K - D_0 = -2\{2\} + \{2\} = -\{2\} = D_0.$$

**[DATA]** (immediate arithmetic from the statements verified in Doc 120 §3.2–3.3; requires
nothing new from the source): D₀ = −{2} is an EXACT fixed point (not only up to
linear equivalence) of the Serre involution, with deg D₀ = −log 2, deg₂ D₀ = −1.

Three consequences computable with CC's verified formulas:

1. **χ(D₀) = 0.** By RR over 𝕊 (2306.00456, Thm 1.1): χ(D₀) = ⌈deg₂ D₀⌉′ + 1 =
   ⌈−1⌉′ + 1 = 0. **[DATA]** (direct arithmetic consequence of the verified formula).
2. **The classical analogue is exact:** on a curve of genus g, χ(D) = 0 ⟺ deg D = g−1,
   and the points with 2D ~ K are the **theta characteristics**; D₀ is the theta
   characteristic of Spec ℤ̄. In the model declared by CC ("genus 0"): deg K_{ℙ¹} = −2,
   theta characteristic O(−1), χ = 0, h⁰ = h¹ = 0 generically. The consistency is
   perfect. **[CONJECTURE-INTERFACE]** the reading "D₀ = arithmetic theta characteristic";
   **[DATA]** each numerical equality separately.
3. **D₀ sits at the dimension jump boundary:** with λ = e^{deg D₀} = 1/2, Prop. 4.2
   of 2306.00456 (dim_𝕊 U(1)_λ = m if 2^{−m−1} ≤ λ < 2^{−m}) evaluates λ = 1/2
   exactly at the edge of the interval (m = 0, with λ = 2^{−m−1} at the
   lower boundary). The self-dual point falls at the jump locus of h⁰/h¹ — the analogue of the
   theta divisor {h⁰ > 0} ⊂ Pic^{g−1}. **[DATA]** the evaluation; **[INTERPRETATION]**
   labeled as such: that the jump is significant and not an artifact of
   normalization. Connection with crossing D: the dimension jumps are the "boundary
   phenomena" that CC declare constitutive of the group→monoid step.

#### 2.1.3. The central conjecture, step by step

**[CONJECTURE-INTERFACE] (121.A — duality→form at the self-dual point).** There exists a
form on a single space, constructed as follows:

- **Step 1 (identification).** At D₀, duality gives H⁰(D₀) ≅ Hom(H¹(D₀), U(1)_{1/4}):
  a perfect pairing P: H¹(D₀) × H⁰(D₀) → U(1).
- **Step 2 (the single space).** Define V := H⁰(D₀) ⊕ H¹(D₀) (the analogue of
  total De Rham H¹: on a classical curve, H¹(C) = H⁰(K_θ) ⊕ H¹(O_θ) for the
  polarization at the theta characteristic). The Serre involution acts on V
  interchanging the summands.
- **Step 3 (the two candidate forms).** On V, P induces
  B_±((a,b),(a′,b′)) := P(b, a′) ± P(b′, a), with values in U(1). B₊ is symmetric,
  B₋ is alternating; which of the two is the CANONICAL one (compatible with the ΓT∗
  structure and with the involution) is a fact of its category, not a choice of ours:
  it is decided by the symmetry character of the duality isomorphism
  (whether the square of the duality H¹ → (H¹)^∨∨ is +1 or −1 — the exact analogue
  of the symmetric/symplectic duality dichotomy of Weil theories, where H^i with odd i
  carries an ALTERNATING form via cup product).
- **Step 4 (linearization).** To speak of signature, B must be lifted from U(1) to ℝ:
  a quadratic refinement q: V → ℝ with B(x,y) = q(x+y) − q(x) − q(y) compatible with
  the 1/4 tolerance.
- **Step 5 (the candidate signature).** sig(V, B₊ linearized) is the candidate
  R-SIG invariant in dimension 1 — the PROTOTYPE of the mechanism the square should
  repeat at large scale.

#### 2.1.4. The falsifiers, in order of lethality

- **F-A1 (symmetry — the decisive one).** If the character of the duality is antisymmetric
  (B₋ canonical, B₊ not definable), the form is symplectic: THERE IS NO signature, only
  mod-2 invariants (Arf). The classical precedent is unfavorable and must be stated: in
  EVERY Weil cohomology, the cup product on H¹ (odd degree) is alternating, and the
  classical theory of theta characteristics produces exactly one mod-2 quadratic form
  on 2-torsion (Mumford; Atiyah) whose invariant is the PARITY of h⁰(θ) —
  a bit, not an integer. If Spec ℤ̄ follows that pattern, crossing A delivers ℤ/2 where R-SIG
  requires ℤ: insufficient for κ(Q) = 2m (which is already even: parity is blind to m). The
  classical escape route also exists and must be named: the integer signature does NOT
  come from the cup product alone but from the POLARIZATION (Hodge–Riemann: i^{p−q} and
  primitivity turn the alternating form into a piecewise-definite hermitian one).
  Translation: even in the best outcome, crossing A needs the analogue of the
  Lefschetz operator/Hodge star, which does not exist in the CC corpus. Falsifier F-A1 decides
  whether the path is cut at step 3 or continues to step 4.
- **F-A2 (tolerance vs bilinearity).** The duality is "with tolerance": the ΓT∗
  morphisms respect relations R_k, not equalities. If the tolerance makes P
  well-defined only up to a non-transitive relation, B is not a form but a
  "form up to tolerance", and inertia may not be defined (eigenvalues near 0 fall
  within the tolerance band — exactly tension T2 of
  Doc 119: signatures do not survive gapless limits). Verification: does the tolerance 1/4
  of U(1)_{1/4} induce in B an additive ambiguity (harmless for signs of
  large eigenvalues) or a multiplicative one (lethal)? It is computable in their category.
- **F-A3 (linearization).** U(1) is not ordered; the lift q: V → ℝ may not
  exist (Bockstein-type obstruction of the sequence ℝ → U(1)). If it does not exist, there is a
  "linking form" (as in 3-manifolds: torsion with values in
  ℚ/ℤ) — finite invariants, not signature. Again: torsion data where integers
  with sign are being requested.
- **F-A4 (triviality).** If dim H⁰(D₀) = dim H¹(D₀) = 0 (generic reading of the boundary
  point, §2.1.2.3), the form is empty and the content of the crossing lies entirely in the
  JUMP (the behavior under perturbing D₀) — that is, in a degeneration theory
  connecting with crossing D, not in a pointwise computation.

#### 2.1.5. The R-NC test applied to crossing A

- **NC1 (externality):** PASSES. The construction uses Arakelov divisors on
  Spec ℤ̄, Γ-rings, the Serre involution: ζ does not appear, nor its zeros, nor operators
  whose spectrum encodes them. The substitution discriminator is satisfied: the
  construction does not know which L-function it "is" — in fact that is its defect (see below).
- **NC2 (overgeneration):** PASSES at its level: the involution σ is defined ∀ D, the
  construction of B at any fixed point of σ modulo equivalence (∀ D with 2D ~ K),
  and falsifiers F-A1–F-A3 are questions about the WHOLE ΓT∗ category, not about an
  object that encodes ζ.
- **NC3/NC4:** NOT EVALUABLE yet — and this is the frank rating: crossing A's
  form, if it exists, is a theorem of ITS geometry (dimension 1), and precisely for
  that reason **it does not individuate zeros**: H¹(D₀) does not carry classes c_ρ. The
  positivity/signature of B would be CC mathematics, not RH-in-disguise — because it is
  too far from ζ to disguise anything. The circularity risk is carried over entirely to the
  (future) moment of repeating the mechanism on the square, where NC3/NC4 will have to
  be applied again.

**Rating of crossing A: CONCEPTUAL with a finite experimental core.** Real value:
it is the only place in the world corpus where "absolute arithmetic duality" and "form with
possible signature" are ONE explicit isomorphism apart, and the outcome
(symmetric/alternating; linearizable/not) is decidable by computation in a category that
already exists. Bounded value: everything happens in dimension 1 — it is the test bench
for the mechanism, not the mechanism.

### 2.2. Crossing B — TOLERANCE→SQUARE: the null elements of Čech

#### 2.2.1. The two data points and the chronology that matters

**[DATA]** (Doc 120 §6.3; arXiv:1805.10501, textual): CC's self-declared blockage
for RR on the square of the scaling site is "an appropriate definition of the sheaf
cohomology (as idempotent monoid) H¹... when applied to Čech covers, the presence of
the null elements creates unwanted contributions to the cohomology which so far we are
unable to handle".

**[DATA]** (Doc 120 §3.2, §6.4): the TOLERANCE technique (𝕊-modules with relation R_k,
Dold–Kan over Γ-rings) that produces the program's first H¹ is from 2022–23 —
LATER than the blockage declaration (2018) — and works in dimension 1 for
Spec ℤ̄. **[DATA]** (Doc 120 §6.4): CC do not explicitly state the connection
"tolerance resolves the null elements"; it is a reading of the program, registered as
plausible and NOT VERIFIED as a claim of theirs.

The structural diagnosis of why the conjecture is natural: the problem with the null
elements is that in an idempotent semiring 0 is absorbing and "equality to zero" in
Čech cocycles is not a linear condition — it produces parasitic classes. The
tolerance relation replaces "x = y" with "x − y ∈ image(ψ) with norm control": it is
exactly a mechanism for declaring near-zero elements negligible without
quotienting by them (a quotient that in the idempotent world does not exist well). That the
mechanism designed for the coker of ψ in dim 1 is the right one for the cocycles of the
square is the conjecture — not a fact.

#### 2.2.2. The conjecture and the ordered verification program

**[CONJECTURE-INTERFACE] (121.B — tolerance on the square).** The Čech complex
of the square of the scaling site, reformulated in the category of 𝕊-modules (or
𝕊[±1]-modules) with tolerance via the change of base from idempotent semirings to
Γ-rings, has a well-defined H¹: the null elements of 1805.10501 end up in trivial
tolerance classes.

Verification program, in order of increasing cost:

1. **Base change in local dim 2.** Express the sheaf of the square
   (ℤ_min ⊗_𝔹 ℤ_min; Newton polygons, **[DATA]** Doc 120 §6.1) as a Γ-𝕊-module,
   verifying that the convex-hull operation survives the base change.
   Risk: the tensor product over 𝔹 and the product over 𝕊 may not commute with
   tropicalization.
2. **The Čech complex with tolerance.** Define, for a finite cover of the
   square, the complex with relations R_k at each degree, and Dold–Kan as in
   2205.01391 §5.
3. **The null-element test.** Identify in a minimal example the exact
   "unwanted contributions" of 1805.10501 (cocycles supported on absorbing elements)
   and compute their tolerance class.
4. **THE TEST CASE: C_p × C_p.** The square of ONE periodic orbit: compact,
   with tropical RR known in each factor (**[DATA]** Doc 120 §3.1), finite Jacobians
   ℤ/(p−1). There: (i) is H¹ with tolerance 𝕊-integer-dimension computable?
   (ii) does a Künneth with the H⁰/H¹ of the factor hold? (iii) does the trace of
   the restricted Frobenius correspondence reproduce block W_p (connection with
   R-LEF-PRIMES, §1.4)? — three verifiable outcomes.
5. **Functoriality under Ψ(λ)** and behavior in the rational anomaly (§1.6).

**Falsifier of the crossing:** step 3/4 — if in C_p × C_p the null cocycles
persist as NON-trivial tolerance classes (or if H¹ turns out to be of 𝕊-infinite
dimension with no taming grading), the dim-1 technique does not extend and the 2018
blockage remains in its original formulation.

#### 2.2.3. What it delivers and does NOT deliver if it closes

If conjecture 121.B is verified: **G1 moves** — there would be, for the first time, an H¹ over
(a piece of) the square with integer-type dimensions. What it does NOT deliver, said
plainly (**[DATA]** Doc 120 §8, reading 2): G2 would remain intact — not even in dimension 1,
where the technique ALREADY works, is there signature; tolerance produces
Euler characteristic, and S1 requires signature. Crossing B unblocks the carrier; the
sign mechanism is crossing A.

#### 2.2.4. R-NC and rating

NC1–NC2: trivially passes (construction of topos + categorical algebra, without ζ; uniform
method for all covers). NC3/NC4: do not apply (no purity is intended to be derived from
this). RH-equivalence risk: **nil** — it is the cleanest gap in the whole
document on that axis.

**Rating: TECHNICAL.** Hard work of a known type: the type is exactly what
CC executed in 2022–23 one floor below. It is also the only gap in the whole
table whose closure depends SOLELY on mathematics the CC team already masters — the
operative definition of "they almost have it and haven't crossed it".

### 2.3. Crossing C — PICK/LOEWNER→INERTIA: does it evade the impossibility theorem?

#### 2.3.1. The datum

**[DATA]** (Doc 120 §5.2, §7.3; arXiv:2511.22755): the truncated Weil form of the
zeta spectral triples has, in the basis {V_n}, the structure τ_ii = a_i,
τ_ij = (b_i − b_j)/(i − j) for i ≠ j, with parities a_{−j} = a_j, b_{−j} = −b_j; CCM
use it exclusively for self-adjointness of the rank-one perturbation (via the
Carathéodory–Fejér extension for Toeplitz matrices).

The target's correct observation: τ_ij = (b_i − b_j)/(i − j) is **exactly a
Loewner matrix**: L_Φ = [(Φ(x_i) − Φ(x_j))/(x_i − x_j)] with nodes x_i = i and values
b_i = Φ(i). And the classical theory of Loewner/Pick matrices IS inertia theory:

**[DATA]** (classical literature): (i) Loewner 1934: Φ is operator-monotone ⟺ every
Loewner matrix of Φ is positive semidefinite; (ii) Krein–Langer (classes N_κ of
generalized Nevanlinna functions): Φ ∈ N_κ ⟺ the Nevanlinna kernel
K_Φ(z, w) = (Φ(z) − Φ(w̄)^*)/(z − w̄) has at most κ negative squares,
and exactly κ for sufficiently large collections of points — that is, **the
negative inertia of truncated Pick/Loewner matrices STABILIZES at a finite value κ characteristic
of the generating function's class** [Krein–Langer, *Über
einige Fortsetzungsprobleme...*, Math. Nachr. 77 (1977), and the series on spaces Π_κ]
**[NOT VERIFIED the exact editorial datum in this session; the mathematical content is
classical and stable]**; (iii) the inertia theory of Hankel/Loewner matrices
(Iohvidov; Fiedler) computes (p, q) via minors and jump rules.

The rhyme with the program is exact and must be recorded: the spaces where N_κ theory
lives are Pontryagin spaces Π_κ — the SAME category where P35 proved
κ(Q) = 2m. **[DATA]** (P35) + **[DATA]** (Krein–Langer) share even the letter κ.

#### 2.3.2. The conjecture

**[CONJECTURE-INTERFACE] (121.C — Loewner as an inertia reader).** There exists a
generating function Φ (built from the arithmetic data b_i of the explicit formula) such that
(i) the Loewner part of QW_λ^N is the Pick matrix of Φ at the integer nodes; (ii)
Φ ∈ N_κ with κ = 2m (the negative squares of the kernel = the index of the Weil
form); (iii) the Krein–Langer stabilization of the truncated inertia as N → ∞ is the
Loewner version of R-FIN.

#### 2.3.3. The decisive question: does the special structure evade Thm 4.3 of Doc 110?

This is the technical question of the crossing and it is answered rigorously and negatively.

**[DATA]** (Doc 110, Thm 4.3): in class ℱ of arithmetic quadratic functionals with
test-accessible compressions, (L2 autonomy) + (L3 inertia detection) + (L4
stability without RH toll) are inconsistent; **[DATA]** (Doc 108 via Doc 110): per-
window indices are binary (0 or ≍ m log T) and inertia is not test-accessible at
infinite rank.

Membership-in-ℱ analysis, in three steps:

1. **The Loewner matrix data are test-accessible.** The entries a_i, b_i of
   QW_λ^N are values of the explicit-formula functionals against concrete tests
   (**[DATA]** Doc 120 §5.2: "the construction only involves the Euler products over
   the primes p ≤ λ²"). Therefore EVERY function of the truncated matrix — including its
   inertia — is an arithmetic quadratic functional with test-accessible compressions:
   **the truncated Loewner matrix lies, entry by entry, WITHIN class ℱ.**
   The "special structure" adds no information: it is a syntactic property of how
   the same accessible values are organized.
2. **Where the extra information would be: in the CLASS of Φ, not in its values.** What
   Krein–Langer makes finite (the stabilization at κ) is a GLOBAL attribute of
   the generating function: membership in N_κ, i.e. meromorphic continuation with κ "negative"
   poles in the half-plane. For the relevant arithmetic function that is not neutral:
   **[DATA]** (program catalog; classical): "the logarithmic derivative of ξ
   (normalized) is Herglotz/Pick in the half-plane Re s > 1/2" is an EXACT
   reformulation of RH (every off-critical zero introduces a pole on the forbidden side =
   a negative square). Therefore statement (ii) of conjecture 121.C —
   "Φ ∈ N_κ with κ = 2m" — is not a bridge: it is the DEFINITION of m in another language.
   It belongs to the MW family (Weil positivity rewritten as membership in N_0);
   NC3 detects it: the link "Φ ∈ N_0" IS MW-1 in function-theory disguise.
3. **The stabilization threshold is not a priori.** Krein–Langer guarantees that the
   truncated inertia reaches κ for "sufficiently many points" — but HOW MANY depends on where
   Φ's singularities are (the generalized poles: the positions of the
   off-critical zeros). Without knowing them, the stabilization N is not computable: for
   every finite N, truncated inertia 0 is compatible both with κ = 0 and with κ = 2m of
   very high zeros. It is EXACTLY the binarity of Doc 108 rewritten: test NC4
   fails (to know whether the property fails in the ¬RH world one must know where the
   quadruple is). **Conclusion: the Pick/Loewner structure falls within class ℱ; it does not
   evade the impossibility theorem.** The deep reason: Loewner/Krein–Langer is
   inertia-READING machinery given a finite κ of the class; it is not
   finiteness-PRODUCING machinery for κ. The finiteness of the class is the input — and the
   input is R-FIN, which has to come from elsewhere (from geometry).

#### 2.3.4. What crossing C IS worth

Downgraded from "wall crossing" to its real value, which is not small:

- **Route B infrastructure.** **[DATA]** (Doc 110 Prop. 4.5): with N₀ known,
  Newton reads inertia from N₀ traces. The Loewner form improves that mechanism: Loewner/Hankel
  inertia theory (Iohvidov rules, minor algorithms) computes
  (p, q) directly from the entries — without going through matrix powers — and the
  identification with N_κ would give structural stability (the read-off inertia is the κ of
  a class, not an accident of truncation). If R-FIN ever arrives by a geometric
  route, the Loewner dialect is probably the format in which Route B is
  executed.
- **The correct dictionary of categories.** The coincidence Π_κ (P35) = Π_κ
  (Krein–Langer) suggests stating the G4→P35 bridge in the language of N_κ functions:
  "RH ⟺ Φ ∈ N_0" is the function-theory version of the program's criterion, with
  mature technical literature (de Branges models, Π_κ spaces). Useful as a lingua
  franca; not as a shortcut.

**Rating of crossing C: POSSIBLY-EQUIVALENT-TO-RH as a closure of R-FIN**
(the link "membership in N_κ with κ a priori" is MW-disguised and NC4 fails);
**TECHNICAL and valuable as post-R-FIN infrastructure for Route B**. The question
is answered: it does not evade Thm 4.3 — it falls within its class.

### 2.4. Crossing D — JACOBIAN→SPECTRAL FLOW (brief)

**[DATA]** (Doc 120 §3.4, arXiv:2602.15941): the Picard group of Spec ℤ̄ is a MONOID
(semi-norms with degeneration allowed), and CC literally state that the step
group→monoid is "a necessary step for incorporating boundary and singular phenomena…
precisely the features required for the spectral realization". **[DATA]** (Doc 110,
Thm 3.2): RH ⟺ sf = 0 for the Euler filtration, with a crossing at finite λ₀ under ¬RH.

**[CONJECTURE-INTERFACE] (121.D).** The spectral flow of the Euler filtration is
realized as a trajectory in the Picard monoid, and the eigenvalue crossings through zero
correspond to touches of the trajectory with the boundary stratum (degenerate
semi-norms): sf = intersection number with the boundary divisor. Internal coherence
in favor: in crossing A, the self-dual point D₀ fell exactly at the dimension-jump
boundary (§2.1.2.3) — the two crossings point to the same stratum.

Falsifiers: (F-D1) the monoid boundary is too small — the degeneration of a
rank-1 semi-norm is a one-parameter phenomenon and might not distinguish
multiplicities of the spectral crossing; (F-D2) the trajectory of the Euler
filtration might never touch the boundary in the RH world and the identification would be vacuous on
one side (fails NC4 through the opposite door); (F-D3) the divergent term 2h(1) log λ
(§9.3 of 2602.15941, pending for them) is exactly where the trajectory would be
defined — without its regularization the crossing cannot even be formulated.

**Rating: CONCEPTUAL, speculative.** Archival value: it is the only language in the
corpus CC where "degeneration/boundary" — the natural habitat of inertia indices in
families — is declared structure and not an accident. To be shelved until (a) CC treat
their divergent term or (b) crossing A confirms the relevance of the boundary stratum.

---

## 3. THE PRIORITY MAP

### 3.1. Ranking by (value if it closes) × (probability of closing without solving RH)

| # | gap/crossing | value if it closes | prob. of closing without RH | product (qualitative) |
|---|---|---|---|---|
| 1 | **Crossing B** (tolerance→square; C_p × C_p case) | high: unblocks G1, gives R-LEF-PRIMES a carrier | high: existing method, active team, nil RH risk | **maximum** |
| 2 | **Crossing A** (form at self-dual point D₀) | medium-high: decides whether the ONLY available duality mechanism can produce signatures (R-SIG prototype) | high for the experiment (finite computation); medium for the full bridge | **high** |
| 3 | R-LEF-POLE (identification H⁰(0), H¹(K) ↔ polar block) | medium: closes the cheapest axiom, validates the dictionary | high (computation in an existing category) | medium-high |
| 4 | R-LEF-REG (term 2h(1) log λ; archimedean as boundary orbit) | medium | medium (CC are already working on it; T2 lurking) | medium |
| 5 | **Crossing C** reformatted (N_κ/Loewner dialect for Route B) | medium conditional (only pays off after R-FIN) | high as translation; nil as closure | medium-low |
| 6 | R-WEIGHT(a)/(b) direct | maximum (it is the wall) | low: no method; the analytic variant is MW | low today — rises if 1 and 2 close |
| 7 | **Crossing D** (spectral flow in the monoid) | high in the limit | low (speculative, blocked by CC's §9.3) | low |

The strategic reading of the product: **the phase should spend on 1 and 2**, which are
mutually independent, complementary (carrier + mechanism), and neither touches
the NO-GO-LIST. The wall (6) is not attacked head-on: one attacks it by building the terrain (1) and
the weapon (2) and only then measuring whether the attack is statable.

### 3.2. What CC can do vs what we can do (specification mode)

- **CC (they have the machinery):** the entire crossing B; the divergent term of their
  §9.3; the question of the symmetry character of their own duality (crossing A, steps 1–3) is an
  internal statement about 2205.01391 that an expert in their formalism probably decides
  in weeks.
- **We (specification mode, without generating mathematics in their category):** write
  up the three experiments as self-contained problems with a falsifier (this document is
  the basis); apply R-NC to each output; keep the NO-GO catalog updated so that
  no partial closure is oversold. And our own task: the N_κ dictionary of crossing
  C (it is classical operator theory, the program's turf, not CC's).

### 3.3. The MINIMAL DECISIVE EXPERIMENT of the phase

Analogue of Problem 5.4 of earlier phases: finite, two clean outcomes, decides the
direction of everything else.

> **Problem 121.E (the symmetry character of the arithmetic duality).** In the
> category ΓT∗ of 2205.01391, let D₀ = −{2} be the exact fixed point of the Serre
> involution σ: D ↦ K−D. Determine the symmetry character of the pairing
> P: H¹(D₀) × H⁰(D₀) → U(1) under σ — equivalently, the sign ε ∈ {+1, −1} with which
> the bidualizing isomorphism acts (is the Pontryagin duality with tolerance of
> Prop. 5.2, composed with itself via σ, symmetric or antisymmetric?).
>
> **Outcome (+1):** a SYMMETRIC form is induced on V = H⁰(D₀) ⊕ H¹(D₀); the
> duality→signature path stays open and the next obstacles are F-A2 (tolerance) and
> F-A3 (linearization) — the phase continues through crossing A.
> **Outcome (−1):** the form is alternating; CC's duality mechanism produces at
> most mod-2 invariants (Arf/parity of the theta characteristic), blind to m; R-SIG
> needs a POLARIZATION in addition to the duality (the analogue of Lefschetz/Hodge ★), and
> the phase must redirect to specifying that ingredient — which has no candidate anywhere
> in the CC corpus.
>
> It is finite: H⁰(D₀) and H¹(D₀) are explicitly computed in their papers (small
> spaces: λ = 1/2, boundary case of Prop. 4.2 of 2306.00456); the pairing is
> explicit; the sign is ONE bit. It uses neither ζ nor zeros: it passes NC1 by construction. Neither
> of the two outcomes proves or disproves anything about RH — it decides where to dig.

Why this one and not the test case C_p × C_p of crossing B: crossing B is the best
value×probability product but it is not ONE experiment with a binary outcome — it is a
5-step program. 121.E is strictly binary, cheaper by an order of
magnitude, and its result conditions the interpretation of EVERYTHING else (if the duality
is alternating, even a successful crossing B delivers a carrier with no sign
mechanism, and specifying the polarization becomes problem number one of the program).

---

## 4. FRANK SYNTHESIS

### 4.1. Years or decades?

Separating by node, without averaging the incommensurable:

- **G1 (carrier): years.** It is "they almost have it and haven't crossed it" in the
  strict sense: the obstacle named in 2018 (null elements in idempotent Čech) is
  earlier than their own 2022–23 tool (tolerance over 𝕊), which solves it one
  floor below; nobody — not even them — has written the combination. TECHNICAL rating;
  with the CC team active (2025 and 2026 papers in the corpus), the reasonable order is
  years, not decades. Same category: R-LEF-POLE, R-LEF-REG, the dynamical half of
  R-LEF-FLOW.
- **G2 (mechanism): no frank upper bound.** There is not ONE signature in the whole
  CC corpus (verified negative search, Doc 120 §7.7); there is no form on a single
  space; there is no polarization; and the classical precedent warns that the
  duality alone (probably alternating in degree 1) is not enough — the analogue of the
  Hodge theory of polarization is needed, for which there is no candidate. This is "nobody
  has any idea" — WITH one measurable exception: experiment 121.E can turn "nobody
  has any idea" into "it is known exactly which ingredient is missing", which is a
  strictly better epistemic state. Saying "decades" here would be faking an estimate we do not have;
  the frank statement is: G2 is not bounded by work of a known type.

The total G1→G2 distance is, therefore, the sum of a short measurable stretch and an
unmeasurable one. Whoever asks "how much is left?" should receive this two-part
answer, not an average.

### 4.2. The "they almost have it" / "nobody has any idea" partition

**They almost have it (and haven't crossed it):** H¹ of the square via tolerance (crossing
B); the identification of the polar block (§1.3); the symmetry character of their own
duality (121.E — it is a statement ABOUT their definitions that nobody has evaluated);
the exact composition of Ψ(λ) in the language of the monoid (§1.6). Common pattern:
each piece is one combination of TWO of their already-published results away.

**Nobody has any idea:** the internal weight criterion (R-WEIGHT(a)); the
polarization (the ingredient 121.E will probably reveal as missing); the
Castelnuovo inequality of the square (R-WEIGHT(b) geometric); the accompanying theorem
of R-FIN ("every negative direction comes from V" without mentioning zeros). Common
pattern: all are the SAME unknown seen from four sides — the structure that produces
integer signs from geometry. The wall is one.

### 4.3. The gap that threatens to swallow the interface

Yes it exists, and must be named without euphemism. It is **R-WEIGHT(b) in its analytic
form**, and it has the poisonous property of OFFERING itself as a shortcut in every crossing: the
master quantifier (P43) reappears in geometric language every time a finite
construction (window, truncation, set S of places, N×N matrix) needs a uniform
statement to globalize. The three occurrences detected in this document:

1. **O_SL** (semilocal→global uniformization of positivities): MW-6, cataloged.
2. **Krein–Langer** (crossing C): the stabilization of the truncated inertia requires the
   class N_κ a priori — which is Weil positivity in function-theory disguise.
   Detected and neutralized in §2.3.3.
3. **The convergence of the spectral triples** (Doc 120 §5.4–5.5): CCM literally state
   that proving its convergence "would amount to a proof of RH" — the
   O_SL pattern in its purest form, declared by the authors themselves.

The interface's defense against the monster is structural and already installed: the
order R-SIG ≺ R-FIN ≺ R-TRZ (Doc 119) forbids using uniform-in-truncation statements
as a substitute for a priori finiteness, and NC3/NC4 detect them syntactically. The
phase's operative rule, derived from this analysis: **every bridge proposal
containing the phrase "and in the limit N→∞ / S→all places / λ→∞, uniformly" is
audited against MW BEFORE investing work in it.** Crossings A and B pass this
audit (they contain no uniform limits in their statement); crossing C failed it and was
reformatted; crossing D is not auditable yet.

### 4.4. Closing

No new geometric statement has been proved in this document. What has been measured:
six axioms against fourteen papers, with the result that the CC corpus contains the
carrier at TECHNICAL distance (crossing B), the prototype of the mechanism one bit
away (experiment 121.E), a reading tool for later (crossing C,
reformatted), a speculative receptacle (crossing D) — and no signature
anywhere. The phase now has its Problem 5.4: the symmetry character of the
arithmetic duality at the self-dual point D₀ = −{2}. A false victory is worse than a failure:
if 121.E comes out (−1), that too is a success of the phase — we would know, for the first time with
precision, that what is missing is not duality but polarization, and the search would change
its object.

---

## References

**Internal (backward-only):** Doc 119 (axioms R-*, dependency order, tensions
T1–T4, R-NC test); Doc 120 (CC inventory verified in source — all
arXiv citations in this document go through its verification); roadmap-rh (G1–G4, S1–S3,
Thm. rank-sensitivity, Routes A/B); Doc 110 (Thm 4.3, Prop. 4.5, Prop. 3.4, §5.2);
Doc 108 (per-window binarity, §7.4, Prop. 2.5); Doc 105 (Thm 5.5, Obs. 5.6);
Doc 100 (archimedean positivity, Obstruction O_SL, Conjecture 100.A); Doc 99 (QW_λ,
Lemma 5.1 — via Docs 100/105); Doc 106 (Prop. 3.10 — via Doc 120 §7.6); Doc 118
(Lemma 5.2, Thm 5.3, Thm 5.6, gap G-118.1); P35 (κ(Q)=2m in Pontryagin); P43
(master quantifier); P44 (dichotomy; anti-Siegel); NO-GO-LIST (MW-1…MW-7).

**CC/CCM corpus (via Doc 120, with source verification declared therein):**
arXiv:1405.4527, 1502.05580 (arithmetic site; Ψ(λ); square with Newton polygons);
1507.05818, 1603.03191 (scaling site; C_p; tropical RR Thm 5.17); 1509.05576
(*Essay*; the three strategies; "yet unclear if this is the right set-up");
1805.10501 (*RR strategy*; the null-elements obstacle, textual); 2205.01391
(RR for Spec ℤ̄; Thm 1.1; Thm 1.2 Serre duality with tolerance; K = −2{2};
U(1)_{1/4}); 2306.00456 (RR over 𝕊; χ = ⌈deg₂ D⌉′ + 1; Prop. 4.2: H¹(D) ≅ U(1)_λ);
2602.15941 (Jacobian of Spec ℤ̄; Picard monoid; §9.3 divergent term
2h(1) log λ; "boundary and singular phenomena"); 2006.13771 (archimedean positivity;
Thm 6.11, defect 13 < c < 17; "intersection theory of divisors (on the square of the
Scaling Site)"); 2310.18423 (semilocal prolates); 2511.22755 (*Zeta Spectral
Triples*; τ_ij = (b_i − b_j)/(i − j); Prop. 3.3 lower-boundedness); 2602.04022
(Connes's letter).

**Classical literature (verifiable):**
- K. Löwner, *Über monotone Matrixfunktionen*, Math. Z. 38 (1934), 177–216.
- M. G. Krein, H. Langer, series on classes N_κ and spaces Π_κ (Math. Nachr. 77
  (1977) and related) [NOT VERIFIED the exact editorial datum in this session].
- I. S. Iohvidov, *Hankel and Toeplitz Matrices and Forms*, Birkhäuser, 1982 (inertia
  theory of Hankel forms) [NOT VERIFIED the exact editorial datum].
- D. Mumford, *Theta characteristics of an algebraic curve*, Ann. Sci. ÉNS 4 (1971),
  181–192; M. F. Atiyah, *Riemann surfaces and spin structures*, Ann. Sci. ÉNS 4
  (1971), 47–62 (parity of theta characteristics; mod-2 quadratic forms / Arf).
- A. Mattuck, J. Tate (1958); A. Grothendieck (1958); A. Weil (1948): via Doc 119.
- V. Guillemin, Duke Math. J. 44 (1977); A. Connes, Selecta Math. 5 (1999): via
  Doc 119.

*End of Doc 121.*
