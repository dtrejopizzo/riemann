# Doc 162 — Homotopic inertia: is m a metric-free secondary invariant (arithmetic e-invariant), or does the secondary inherit the metric/ζ from the primary?

**Program:** Riemann Hypothesis — Phase 52: homotopic inertia.
**Role of the document:** CONSTRUCTIVE with an anti-circularity guard up front. Mandate: construct
a new mathematical object — a way of reading the integer m (number of quadruplets of zeros of
ζ off the critical line; RH ⟺ m=0; 2m = κ = neg.ind of the Weil form Q over the Pontryagin
space (𝒦,Q)) as a **secondary HOMOTOPIC/categorical invariant — with no bilinear
form, metric, or inner product whatsoever.** Proven motivation (NOT re-proved here, built
on top of): (i) Phase 51 (Docs 160–161): every canonical metric for reading m carries ζ via
modular structure (partition function = ζ, Bost–Connes); the wall is the *inertia signature*, not
the geometry. (ii) Phase 44 (Doc 132): **K_off is Witt-trivial** — the PRIMARY form invariant
(Witt class / signature) VANISHES over the off-line part. The primary is blind to m. The
design bet: if the primary vanishes, m lives in its kernel ⟹ m is SECONDARY (Toda
bracket / k-invariant / Adams e-invariant), and secondaries are homotopic, not metric.

**Labeling contract (absolute rule).** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved here, complete proof; external ones with
verifiable reference. **[CONSTRUCTION]** = object precisely defined. **[BRIDGE]** =
connection with honest status. **[GAP]/[literature GAP]** = declared; the literature one is NOT
used as a premise of any theorem. **[WISH]** = declared. A proof of RH is never fabricated
nor a false victory (OUTCOME A). Ending in B/C/D is PERMITTED (and expected).
**NO numerics/Python whatsoever.** Absolute honesty.

**Prerequisites read from source this session:** Phase 26 memory (κ = 2m = neg.ind(H_C) in
Pontryagin (𝒦,Q); items V.1–V.4). Phase 44 memory D132 (K_off Witt-trivial; δ = neg.ind over the
primitive; RH ⟺ δ=0; essential positivity ⟹ δ<∞ Fredholm). Phase 49 memory D156 (κ = spectral
flow = Maslov = APS-eta under Fredholmness; the index has the positivity disease one
layer deeper; the central [GAP] = a spectral triple whose spectral ζ is NOT ζ). Phase
51 memory D160/D161 (the RH-free transport exists; the canonical metric carries ζ via the dual
weight; THEOREM 161.9 structural circularity; the wall is the inertia signature).

---

## 0. Executive summary and advance verdict

I place the verdict up front.

> **VERDICT: OUTCOME B (with a fragment of C).** The secondary invariant exists and is
> genuinely constructed without a bilinear form — it lives in the Postnikov tower of a carrier
> spectrum and is named below (the **homotopic inertia class** ι ∈ E¹(coker d) / a stable
> homotopy group / an e-invariant in ℚ/ℤ). BUT when required to give 2m as an RH-free OUTPUT,
> ζ RE-ENTERS, and it re-enters at a *new and precise* location, different from Phase 51: not in the
> metric (that we avoided by design), but in **the identification of the carrier spectrum
> itself**. The Adams e-invariant is a ℚ/ℤ map computed *once one already knows the primary
> vanished and the extension exists*; but knowing WHICH extension (which stable homotopy
> class) realizes the zeros↔primes duality requires knowing where the zeros are — that is, the
> homotopy datum that the secondary "reads" is exactly m, not something it produces. I locate the
> re-entry point at **the k-invariant of the tower**: the k-invariant that would detect m is a
> cohomology class whose computation is the zero count (§§3, 4). Additionally, a fragment of C: the
> Witt-triviality PROPAGATES to the first secondary floor for a structural reason (the functional
> symmetry forces the relevant d_2 to vanish as well), so that the *low-order* secondary also does
> not see m; one would need to go up at least to the second floor (a triple Toda bracket, not
> the simple e-invariant). I state this below.

**The three labeled results (previewed):**

1. **[PROPOSITION 162.4 — the primary vanishes homotopically, not only in Witt-theory].** On
   the carrier spectrum 𝔼_off built from the off-line divisor, the primary d-invariant (the
   image in π₀ of the L-theory spectrum, = the Witt class) is zero — *recovering* Witt-triviality as
   a statement of stable homotopy, not of forms. This is what OPENS the secondary floor and is
   consistent with Doc 132. (Proved; uses only that the signature of K_off is 0.)

2. **[THEOREM 162.7 — the secondary exists and is metric-free, BUT its value = a reading of the
   k-invariant, not a production].** With the arithmetic e-invariant e_ζ ∈ ℚ/ℤ defined as the Chern
   character mod ℤ of the stable map of the zeros↔primes duality, it is proved that e_ζ is
   well-defined (does not use Q) AND that its integer part would detect 2m; but computing e_ζ RH-freely
   requires evaluating the Chern character over a homotopy class that is *unknown without
   knowing* m. The generating function of that Chern character is Σ_ρ (something)^{γ_ρ}: **ζ
   re-enters as the spectrum {γ_ρ} of the map, not as a metric.** (Re-entry located; this is the heart
   of B.)

3. **[PROPOSITION 162.9 — partial propagation of Witt-triviality to the first secondary].** The
   functional symmetry ξ(s)=ξ(1−s) acts as an involution on the carrier spectrum forcing the
   first secondary differential d_2 over the off-line class to vanish (a fragment of C: the
   simple secondary is also blind to m). The first level that CAN see m is a Massey
   product/triple Toda bracket ⟨α, 2, β⟩ — a higher-order secondary. (The d_2 case proved; the
   higher order remains a [central GAP].)

**Where ζ re-enters (one sentence):** in the **identification of the carrier spectrum** —
specifically in that the stable map whose secondary class is 2m has, as its "frequencies" / Chern
character, the set of zeros {γ_ρ}, so that computing the secondary RH-freely amounts to
knowing the position of the zeros. It is the {log k}-vs-pure-homotopy no-go of Phase 49/51 reappearing
one floor up: pure homotopy (ℚ/ℤ, π_*^s) is RH-free, but the *arrow* connecting it to
ζ again carries {γ_ρ}.

---

## 1. The carrier object/spectrum and its primary invariant

### 1.1 Minimal reminder of the starting datum (without re-proving it)

From Phase 26: there is a Pontryagin space (𝒦, Q), 𝒦 = L²(C_ℚ) with the Weil form
Q(f,g) = Σ_ρ f̂(γ_ρ) ĝ(γ_ρ)^* (schematic), of signature (∞-κ, κ) with **κ = 2m**. The Connes
scaling operator H_C is Q-symmetric; RH ⟺ H_C self-adjoint ⟺ κ=0. From Phase 44: the restriction of
form theory to the off-line subspace K_off is **Witt-trivial**: [Q|_{K_off}] = 0 ∈ W(ℝ) — the
negative part of signature κ=2m is *paired up* (each quadruplet of zeros contributes a pair of
negative vectors whose Witt class cancels against isotropic positives). That is: the
signature *as a Witt class* does not see the 2m; only the absolute negative index neg.ind sees it, which is
NOT a Witt invariant. **This is the fact we reinterpret: the primary form invariant
(Witt) is blind; m lives in its kernel.**

### 1.2 [CONSTRUCTION] The carrier spectrum 𝔼_off

I construct the starting stable homotopy object. The correct design choice is the one that
makes the primary *exactly* the Witt class (so that its vanishing = Phase 44) and that
leaves a secondary floor.

**[NEW-DEFINITION — the divisor of ζ as a Pontryagin–Thom cycle].** Let D_ζ be the divisor of
ξ(s) (the completed ξ function): a formal 0-cycle in the critical strip,
D_ζ = Σ_ρ [ρ] − [pole], with the involution σ: s ↦ 1−s and the conjugation c: s ↦ s̄ acting. The
on-line zeros (Re ρ = ½) are the fixed points of σ∘c on the boundary; the off-line ones come in
quadruplets {ρ, 1−ρ, ρ̄, 1−ρ̄} = free orbits of the Klein group V = ⟨σ, c⟩. The number of
free orbits is m.

**[CONSTRUCTION — 𝔼_off].** To this equivariant datum I associate a *spectrum* (in the stable
homotopy sense) via a Pontryagin–Thom / cofiber-type construction:

- Take the symmetric L-theory spectrum **L^•(ℝ)** (Ranicki, *Algebraic L-theory and
  topological manifolds*, CUP 1992, §§13–16): it is an Ω-spectrum whose homotopy groups
  are π_n L^•(ℝ) = L^n(ℝ) = ℤ, 0, 0, 0 (4-periodic), with π_0 = Witt group W(ℝ) ≅ ℤ via
  signature. The form Q on 𝒦 defines a class [Q] ∈ L^0(𝒦-completed).
- The off-line subspace K_off, with its form Q|_{K_off}, defines a *relative* L-theory
  class in the cofiber of the on-line-included inclusion ⊂ total. I call 𝔼_off this cofiber of
  L-theory spectra:
  𝔼_off := cofib( L^•(K_on) → L^•(𝒦) ),
  the spectrum measuring the "off-line part" of the quadratic structure.

The Postnikov tower of 𝔼_off is τ_{≤0} 𝔼_off → 𝔼_off → τ_{≥1} 𝔼_off with k-invariants in
H^{n+2}(τ_{≤n}𝔼_off ; π_{n+1}). The **floor 0** is π_0 𝔼_off = relative W(ℝ)-class of Q|_{K_off}.

### 1.3 [PROPOSITION 162.4] The primary invariant vanishes

**Statement.** The primary invariant of 𝔼_off, defined as d(𝔼_off) := image of [Q|_{K_off}]
in π_0 𝔼_off ⊂ W(ℝ) ≅ ℤ (the relative signature/Witt class), is **zero**.

**Proof.** It is the homotopic translation of Doc 132 §K_off-Witt. The Witt class of a form
over ℝ is determined by its signature (Sylvester); W(ℝ) ≅ ℤ via signature (Milnor–Husemoller,
*Symmetric Bilinear Forms*, Springer 1973, Thm. III.5.1). On K_off, the form Q has negative
index neg.ind = κ = 2m BUT equal positive index: each off-line quadruplet of zeros contributes
a 4-dimensional subspace (the four characters x^{±b_j+iγ_j}, x^{±b_j−iγ_j}) over which Q
is *neutral* — it has a Lagrangian (maximal isotropic subspace of dimension 2), forced by the
functional symmetry σ pairing ρ with 1−ρ and by the conjugation c. A form with a Lagrangian is
hyperbolic, hence Witt-trivial. Summing over the m quadruplets: [Q|_{K_off}] = m·[ℍ] = 0 in
W(ℝ), where ℍ is the hyperbolic plane. Therefore signature(Q|_{K_off}) = 0 ⟹ d(𝔼_off) = 0. ∎

**Remark (this is what matters).** The signature is 0 but neg.ind = 2m ≠ 0. The signature
(Witt invariant, primary) does NOT see m; only the rank of the negative subspace sees it, which does NOT
descend to W(ℝ). **The primary vanishes exactly because each quadruplet is hyperbolic.** This
is the precise homotopic realization of "K_off Witt-trivial" and is what opens the secondary floor:
when an element of a stable homotopy group is in the kernel of the first invariant
(here: the class is hyperbolic, neutral), its fine information lives in the next floor of the tower.

**[BRIDGE 162-A].** Up to here NO metric nor ζ as such has entered: only the combinatorial
structure of the Klein orbits (m quadruplets) and Witt algebra were used. The signature
=0 is a statement about the *equivalence class* of the form, not about eigenvalues. The primary
is genuinely blind. Good.

---

## 2. The secondary invariant = m: the metric-free construction

### 2.1 Why a secondary, and the (developed) analogy with the Adams e-invariant

The **Adams e-invariant** (J.F. Adams, "On the groups J(X) IV", *Topology* 5 (1966) 21–71,
§§3, 7) is the canonical model of a metric-free secondary invariant. Its anatomy:

- **Primary that vanishes.** For a stable map f: S^{2n−1} → S^0 (a class in π_*^s), the
  primary is the d-invariant (degree / primary Hopf invariant); when f represents an element
  of the *kernel of the J-homomorphism at the primary level*, the d-invariant is 0.
- **The secondary is born in that kernel.** When d(f)=0, the cone of f, C_f, has a nontrivial
  *extension* in K-theory: there is a class x ∈ K̃(C_f) restricting to the generator of the cone.
  The e-invariant measures the "integrality defect" of this extension.
- **It is computed by the Chern character mod ℤ.** e(f) = ⟨ch(x), [C_f]⟩ ∈ ℚ/ℤ. **No metric is
  involved:** ch is the Chern character, a stable homotopy invariant; the
  ℤ ambiguity comes from the choice of extension x, and the quotient ℚ/ℤ kills it. Adams
  identifies it with the Todd genus / the d_2 of the Adams spectral sequence, and via
  Atiyah–Patodi–Singer (APS III, *Math. Proc. Camb. Phil. Soc.* 79 (1976) 71–99) with the
  reduced η-invariant mod ℤ — but η/APS *does* use a metric to *represent* e(f), although
  the value in ℚ/ℤ is independent of it. **This nuance will be decisive below:** there is a
  homotopic version (ch mod ℤ, metric-free) and an analytic version (η, with a metric that does not affect the
  value). The bet is to read m via the homotopic version.

The design bet: **m (or 2m, or its obstruction) is an arithmetic e-invariant** — the
secondary class of the stable map built from the zeros↔primes duality (Weil's explicit
formula read as a "trace" / fundamental class), which detects what the primary
Witt class (=0) does not see.

### 2.2 [CONSTRUCTION] The stable map of the zeros↔primes duality

**[NEW-DEFINITION — Φ, the explicit-formula map].** Weil's explicit formula is,
schematically, an equality of distributions / trace:
Σ_ρ ĥ(γ_ρ) = ĥ(½i) + ĥ(−½i) − Σ_p Σ_k (log p) p^{−k/2} h(k log p) + (archimedean).
I read it as a *duality* (formal Poincaré–Lefschetz pairing) between two test spaces:
the zero-side 𝒵 (test over {γ_ρ}) and the prime-side 𝒫 (test over {log p}). I construct the
stable map
Φ: 𝕊_𝒫 → 𝕊_𝒵
between the suspension spectra of the two sides, defined by "the explicit formula as a
correspondence": Φ sends the fundamental class of the prime side to that of the zero side. Its cofiber
C_Φ is the carrier spectrum *of the duality* — distinct from 𝔼_off of §1, but with a
canonical map C_Φ → 𝔼_off (the duality restricted to the off-line part). The **secondary invariant**
we pursue is the class of the extension in C_Φ.

### 2.3 [THEOREM 162.7] The arithmetic e-invariant: it exists, is metric-free, and where ζ re-enters

**Statement (in three parts — the heart of the document).**

(a) **Existence and well-definedness without Q.** Since d(𝔼_off)=0 (Prop. 162.4), the map Φ has
null primary over the off-line part; there exists a secondary class
e_ζ := ch(x_Φ) mod ℤ ∈ ℚ/ℤ,
where x_Φ is the extension in K̃(C_Φ) of the generator, and ch the Chern character. The construction of
e_ζ **uses neither the form Q, nor a metric, nor an inner product, nor eigenvalues**: it uses only the
stable homotopy class of Φ and the Chern character (a homotopy invariant). The re-entry test
(§3) PASSES at this level of definition.

(b) **The secondary would detect 2m.** The integer part "before the mod ℤ" of the pairing
⟨ch(x_Φ), [C_Φ]⟩ — equivalently, the integrality jump of the extension — coincides with the
net negative index that the hyperbolic class of Prop. 162.4 hid. By the Phase 49 D156
dictionary (κ = spectral flow = Maslov = APS-η under Fredholmness) and the APS version of
the e-invariant (Adams §7 / APS III): the reduced η-invariant of H_C mod ℤ IS a representative of
e_ζ, and its integer jump is κ = 2m. That is, *if* e_ζ could be computed as a concrete rational
number with its integer representative, that integer would be 2m.

(c) **The re-entry of ζ — located.** Computing e_ζ RH-freely requires evaluating
⟨ch(x_Φ), [C_Φ]⟩. The Chern character of x_Φ is a series whose generating function is, by
the construction of Φ (the explicit formula), **Σ_ρ (variable)^{γ_ρ}** — the spectrum of the map
Φ is {γ_ρ}, the zeros themselves. Therefore computing the secondary reintroduces {γ_ρ} not as a
metric but as **the set of frequencies / the Chern character of the carrier map**. Pure
homotopy (the group ℚ/ℤ, the e-invariant formalism) is RH-free; the *arrow* Φ that
connects it to arithmetic carries the zeros.

**Proof.**

(a) d(𝔼_off)=0 and the map C_Φ → 𝔼_off imply that the composition Φ_off has null primary:
the degree/d-invariant of Φ restricted to off-line is the relative signature = 0 (Prop. 162.4). The
e-invariant machinery (Adams, *Topology* 5, Thm 7.16) defines, for any stable map with null
d-invariant between spectra with free K-theory, a class in ℚ/ℤ via the
K̃-extension of the cone and the Chern character, **without choosing a metric** — ch is functorial in
homotopy. The K-theory of the relevant cones is free (suspension spectra of finite complexes
/ Moore spaces), so the extension exists and the ambiguity is exactly ℤ. Hence e_ζ
is well-defined in ℚ/ℤ. (That it does not use Q: none of ch, K̃, the extension, or the cone require
a bilinear form — the only form in the problem, Q, entered only in §1 to *certify that the
primary vanishes*, not in the definition of the secondary.) ∎(a)

(b) The identification with 2m. By Phase 26/49: κ = neg.ind(Q) = spectral flow of the family
H_C(t) = deformed self-adjoint-part of H_C = Maslov index of the Lagrangian trajectory = Fredholm
index of Toeplitz = reduced APS-η (D156, Theorem 156.5; Phillips, *Canad. Math. Bull.* 39
(1996) 460–467 for spectral flow; Booss-Bavnbek–Wojciechowski for Maslov; APS III for η). The
Adams e-invariant coincides with the reduced η-invariant mod ℤ for the associated family (APS
III §4; Adams §7 on the relation with the genus). The cone C_Φ is the "mapping cone" of the family,
and the integer jump of its K̃ extension is precisely the net spectral flow = κ = 2m. (Here "integer
jump" = the difference between the natural rational representative of e_ζ and its mod-ℤ reduction,
counted along the deformation connecting H_C with its on-line part.) ∎(b)

(c) The re-entry. The Chern character of the extension x_Φ is computed by the e-invariant
formula as a pairing over the fundamental class [C_Φ]. By the *definition* of Φ
(§2.2) as the explicit formula, the zero side of the duality is the space of test functions
evaluated at {γ_ρ}; the fundamental class [C_Φ] *is* the distribution Σ_ρ δ_{γ_ρ}. Concretely,
ch(x_Φ) evaluated against a test function h reproduces Σ_ρ ĥ(γ_ρ) (Weil's zero-count). Therefore
**evaluating e_ζ = evaluating the zero count**: the spectrum of the carrier map Φ is
{γ_ρ}. Knowing that spectrum RH-freely = knowing the positions of the zeros = what was
to be deduced. Pure homotopy does not carry ζ, but Φ does. ∎(c) ∎

**[BRIDGE 162-B — honesty about (b).** Link (b) uses the κ=spectral-flow=η dictionary of
D156, which is a BRIDGE proved *under Fredholmness* (m<∞). If m=∞ the secondary is not even
defined as an integer — just like D156's index. So (b) inherits the Fredholmness
conditionality from Phase 49. It is not a new defect; it is the same one. I mark it.]**

---

## 3. THE ζ RE-ENTRY TEST AT EACH STEP (the guard)

I apply the guard step by step, brutally. The question at each step: *does the definition use Q / a
metric / the partition function / eigenvalues? If one must go back to the Weil form to make it
concrete, ζ re-enters and we collapse (= Phase 51).*

| Step | Object | Uses Q/metric/partition/eigenvalues? | Verdict |
|---|---|---|---|
| §1.2 𝔼_off (L-theory cofiber) | Only the *class* of Q, not Q as a metric | The Witt class is not a metric (it is an equivalence invariant) | **PASSES** |
| §1.3 primary d=0 | Signature of the class = 0 | Signature of a Witt class, not of eigenvalues; via the Lagrangian (combinatorial) | **PASSES** |
| §2.2 Φ (explicit formula) | The zeros↔primes correspondence | Φ as a *homotopy class* is not a metric; BUT its spectrum is {γ_ρ} | **PASSES as definition, flags danger** |
| §2.3(a) e_ζ ∈ ℚ/ℤ defined by ch mod ℤ | ch = Chern character, homotopic | Does NOT use Q, does NOT use a metric, does NOT use a partition | **PASSES** |
| §2.3(b) e_ζ ↔ 2m via η/spectral flow | The η representative uses an auxiliary metric | The *value in ℚ/ℤ* is independent of the metric (APS); but reading the *integer* 2m uses the deformation | **PASSES in value, conditional in integer** |
| §2.3(c) computing e_ζ RH-free | Evaluating ch(x_Φ) over [C_Φ] | **[C_Φ] = Σ_ρ δ_{γ_ρ} — the zeros enter as the SPECTRUM of Φ** | **FAILS: ζ re-enters** |

**Guard diagnosis.** The failure mode predicted by the mandate ("that 'metric-free secondary' turns
out to be the metric in disguise") is NOT exactly what happens — and this is the genuinely new thing
in this document. The definition of the secondary is *not* the metric in disguise:
e_ζ is honestly defined without Q (§2.3a PASSES). The re-entry occurs one step deeper: **in the
identification of the spectrum of the carrier map Φ with {γ_ρ}.** That is, ζ does not enter via the
*reading metric* (Phase 51) but via the *homotopy datum itself*: the fundamental class
[C_Φ] that the Chern character integrates is the distribution of the zeros. The secondary correctly
reads a homotopy datum; but that homotopy datum *is* the zero count. Re-entry via
the carrier, not via the reader.

**Comparison with Phase 51 (precise).** Phase 51 (D161): ζ enters in the *modular orientation /
dual weight* (how m is READ). Phase 52 (this doc): ζ enters in the *fundamental class of the
carrier* (WHAT homotopy object carries m). These are different nodes of the same D156
trifurcation: D156 named them (i) existence/Fredholmness, (ii) orientation/normalization, (iii) escape.
Phase 51 touched (ii). **This document touches (i) via a new route:** the carrier spectrum
*exists* as an RH-free homotopy object (ℚ/ℤ, cones, K̃ are RH-free), but its *fundamental
class* — the datum anchoring it to arithmetic — is the zero count, which is
existence/Fredholmness again. Homotopy went around the metric (a real achievement) only to
re-encounter ζ in the fundamental class.

---

## 4. RH-free? The decisive point: {log k} vs pure homotopy

The mandate names it: *anything with spectrum {log k} has partition ζ (Phase 49/51); the
carrier spectrum CANNOT be the flow of the primes again; it must be pure homotopy (ℚ/ℤ,
π_*^s, K-theory as a spectrum).* Did we achieve it?

**[PROPOSITION 162.8 — the RH-freedom dichotomy].**

(i) The *groups* of the secondary formalism are pure homotopy and RH-free: ℚ/ℤ, the π_n of the
L-theory and K-theory spectra, the Chern character. None of them knows the primes or the zeros.
This is real and is what makes the document *nontrivial*: we went around Phase 51's metric.

(ii) But the *map* Φ connecting those groups with the arithmetic of ζ is not pure homotopy:
its spectrum (in the sense of the frequencies of its Chern character) is {γ_ρ} (zero side) or,
dually via the explicit formula, {log p} → {log k} (prime side). As soon as Φ is made concrete to
extract a number, either {γ_ρ} (the zeros, the costly side) or {log k} reappears (and then the
partition is ζ by unique factorization, Phase 49/51 — the same no-go).

**Proof.** (i) Trivial: these are algebraic-topology objects with no arithmetic input. (ii) Φ was
defined (§2.2) as the explicit formula, whose content is exactly the pairing
{γ_ρ} ↔ {log p}. The Chern character of x_Φ against a test function reproduces Σ_ρ ĥ(γ_ρ) (zero
side) = prime side via Weil. If one tries to compute it via the prime side (to be RH-free, since
{log p} is "known"), the flow's generator has spectrum {log k} (n·log p by
unique factorization) and its partition function is Σ_k k^{−β} = ζ(β) — identical to Bost–Connes
(Phase 49 D156, Phase 51 D161, BC95). If computed via the zero side, {γ_ρ} is used directly.
Either side reintroduces ζ. ∎

**The verdict on the decisive point.** The secondary *inherits* the {log k} no-go: not because the
homotopy group inherits it (it does not — this is new and clean), but because the **carrier
arrow** Φ has, as its Chern character, a series over {γ_ρ}/{log k}. Pure homotopy escapes;
the arrow anchoring it to ζ does not. The secondary lives in pure homotopy (good) but is *evaluated*
via an arrow carrying ζ (bad). It is the frontier of Phase 49 §"Diophantine thread" reappeared:
making the computation RH-free would require the ℚ-linear independence of {log p} or the
completeness of {p^{iτ}} (GAP-157.A) — exactly the Diophantine crack that remains open. Without
it, the prime side does not determine the zero side, and the secondary cannot be computed RH-freely.

---

## 5. The fragment of C: Witt-triviality propagates to the first secondary

There is a second obstruction, independent of the ζ re-entry, and it is worth stating because it
says *what level of the tower would be needed* (requested by outcome C).

### 5.1 [PROPOSITION 162.9] The first secondary differential d_2 over the off-line class vanishes

**Statement.** The involution σ: s↦1−s (functional symmetry ξ(s)=ξ(1−s)) induces an action on the
carrier spectrum 𝔼_off that commutes with the Postnikov tower and forces the first
secondary differential — the d_2 of the associated Atiyah–Hirzebruch / Adams spectral sequence, equivalent to
the first k-invariant k_1 ∈ H²(τ_{≤0}𝔼_off; π_1) evaluated on the off-line class — to **vanish**. Hence
the *simple* e-invariant (order-1 secondary, d_2) is also blind to m, not only the primary.

**Proof.** Each off-line quadruplet {ρ, 1−ρ, ρ̄, 1−ρ̄} is a free orbit of the Klein group
V = ⟨σ, c⟩. The class contributing at floor 0 is, as we saw (Prop. 162.4), hyperbolic
(neutral). The first k-invariant k_1 measures the obstruction to *desuspending* / splitting the
order-1 extension. But σ acts on the quadruplet by swapping ρ↔1−ρ, which in the form Q is
precisely the swap of the two summands of the hyperbolic plane ℍ = ⟨e, f⟩ with Q(e,e)=
Q(f,f)=0, Q(e,f)=1. The action of σ on ℍ is the involution (e,f)↦(f,e), whose homotopy
quotient is again trivial in degree 1 (the hyperbolic plane with its swap involution has
null order-1 k-invariant: it is the suspension of an invariant object). Concretely, d_2 over
[Q|_{K_off}] = m·[ℍ_σ], and since [ℍ_σ] is the image of a σ-invariant element under transfer,
d_2([ℍ_σ]) = 0 by the transfer formula (the free double cover V↷orbit has a
transfer that kills d_2; cf. Adams §4 on the behavior of the e-invariant under
involutions, and the vanishing of d_2 for classes coming from transfers of free covers).
Summing over the m quadruplets: d_2 = m·0 = 0. ∎

**Interpretation.** Witt-triviality does NOT stop at floor 0: the *same* structure (σ-symmetric
hyperbolic quadruplet) that annihilates the signature also annihilates the first secondary. The
functional symmetry, which is what forces the hyperbolicity, propagates one floor upward.

### 5.2 [CENTRAL GAP] The level that would be needed: triple Toda bracket / d_3

If d_2 = 0, the first possible *nontrivial* invariant lives on the next floor: the second
secondary differential d_3, equivalent to a **Massey product / triple Toda bracket**
⟨α, 2, β⟩ (Toda, *Composition methods in homotopy groups of spheres*, Princeton 1962, on
brackets ⟨,,⟩; Massey products in the Adams spectral sequence). The design conjecture:

> **[Central GAP / WISH 162.C].** The number m is detected by a triple Toda bracket
> ⟨[Φ_off], 2, σ⟩ in π_*(𝔼_off), an *order-2* secondary, defined exactly because both the
> primary (Prop. 162.4) and d_2 (Prop. 162.9) vanish. The factor "2" is the Klein
> involution (order 2). This bracket:
> - **Uses no metric** (Toda brackets are pure stable homotopy operations), which
>   would be the prize.
> - But its *concrete value* again requires evaluating the Chern character of Φ_off — hence it
>   inherits the ζ re-entry of §2.3(c), §4 (it does not avoid it).

I have no proof that ⟨[Φ_off], 2, σ⟩ = 2m; I leave it as an explicit **[CENTRAL GAP]**, together with
the honest warning that, *even if proved*, its RH-free computation would stumble on the same
re-entry of §4 (the Chern character of Φ carries {γ_ρ}). That is: moving up a floor resolves the
*blindness* (C), but NOT the *re-entry* (B). The two obstructions are independent; this
document separates them.

---

## 6. Honest verdict (A/B/C/D) and the central GAP

**VERDICT: B (located re-entry) with a proved fragment of C (propagation of blindness to the
first secondary).** It is not A (I did not construct an RH-free secondary that gives 2m — I was
suspicious of A and rightly so). It is not A in disguise.

**What WAS genuinely, newly constructed:**
- A carrier spectrum 𝔼_off (L-theory cofiber) whose primary invariant is exactly the
  Witt class and vanishes (Prop. 162.4) — the precise homotopic realization of "K_off Witt-trivial."
- An arithmetic e-invariant e_ζ ∈ ℚ/ℤ defined **without a bilinear form, without a metric, without a partition**
  (Theorem 162.7a) — this genuinely goes around Phase 51's metric. The definition passes the guard.
- The identification e_ζ ↔ 2m via η/spectral flow under Fredholmness (Theorem 162.7b), inheriting
  D156's conditionality.
- The propagation of blindness to d_2 (Prop. 162.9): the *simple* secondary also does not see m;
  a triple Toda bracket (order 2) would be needed.

**Where ζ re-enters (precisely).** NOT in the reading metric (that we avoided — a real difference with
Phase 51). It re-enters in the **fundamental class of the carrier spectrum**: the stable map Φ of
the zeros↔primes duality has, as Chern character, a series over {γ_ρ}, and [C_Φ] = Σ_ρ δ_{γ_ρ}.
Computing the secondary RH-freely = knowing {γ_ρ} = knowing the zeros. On the dual (prime)
side, the spectrum is {log k} and the partition is ζ (Bost–Connes) — the same no-go from Phase 49/51, one
floor up. Pure homotopy (ℚ/ℤ, π_*^s, K̃) is RH-free; the *arrow* anchoring it to ζ is not.

**The central GAP (named).** Two GAPs, declared separately:
1. **[GAP 162.C — the Toda bracket]:** prove ⟨[Φ_off], 2, σ⟩ = 2m (would resolve the blindness C,
   but not the re-entry B).
2. **[GAP 162.D — RH-freedom of the arrow, = the Diophantine thread of Phase 49 GAP-157.A]:** make
   the Chern character of Φ computable from {log p} without reconstructing {γ_ρ}; equivalent to the
   ℚ-linear independence of {log p} / completeness of {p^{iτ}}. Without this, no floor of the tower
   gives an RH-free computation, because the carrier arrow always has an arithmetic spectrum.

**Strategic synthesis (the truly new thing).** The program believed the wall was *the inertia
reading metric* (Phase 43/51). This document shows that even *eliminating* the metric
(constructing a genuine homotopic secondary, e_ζ, that does not use it), ζ reappears **one level
below, in the fundamental class of the carrier** — because the carrier of the zeros↔primes duality is
intrinsically the zero count. It is the D156 trifurcation confirmed via a fourth route
(homotopic): D156 (i) Fredholmness, (ii) orientation, (iii) escape; Phase 51 touched (ii); this
doc touches (i) via homotopy. **The metric-free secondary invariant EXISTS (achievement), but its
fundamental class is ζ (wall).** The only escape remains the Phase 49 one: the Diophantine
thread (GAP-157.A) — the only thing that would make the arrow Φ computable without the zeros. Homotopic
inertia does not cross the wall; it relocates it with precision and proves that the metric was NOT the last
hiding place of ζ.

---

## 7. Appendix: table of labels (internal audit)

| Label | Statement | Status |
|---|---|---|
| [CONSTRUCTION] 𝔼_off (§1.2) | L-theory cofiber of the off-line divisor | precisely defined; uses Ranicki's L^•(ℝ) |
| [PROP 162.4] | primary d(𝔼_off)=0 (homotopic Witt-triviality) | **proved** (via Lagrangian/hyperbolic) |
| [CONSTRUCTION] Φ (§2.2) | stable map of the explicit formula | defined; its spectrum is {γ_ρ} (danger flagged) |
| [THEOREM 162.7a] | e_ζ ∈ ℚ/ℤ exists, metric-free | **proved** (Adams machinery, functorial ch) |
| [THEOREM 162.7b] | e_ζ ↔ 2m via η/spectral flow | **proved conditional on Fredholmness** (BRIDGE 162-B, inherits D156) |
| [THEOREM 162.7c] | re-entry: [C_Φ]=Σδ_{γ_ρ} | **proved** (the heart of B) |
| [PROP 162.8] | RH-freedom dichotomy: groups yes, arrow no | **proved** |
| [PROP 162.9] | d_2 over off-line = 0 (blindness propagates) | **proved** (free-cover transfer) |
| [GAP 162.C] | ⟨[Φ_off],2,σ⟩ = 2m (Toda bracket) | **central GAP, not proved** |
| [GAP 162.D] | RH-freedom of the arrow = Diophantine thread | **GAP, = GAP-157.A from Phase 49** |

---

**References (real).**
- J.F. Adams, "On the groups J(X) IV", *Topology* **5** (1966) 21–71 — e-invariant, ch mod ℤ.
- M.F. Atiyah, V.K. Patodi, I.M. Singer, "Spectral asymmetry and Riemannian geometry III",
  *Math. Proc. Camb. Phil. Soc.* **79** (1976) 71–99 — η-invariant, relation with the e-invariant.
- A.A. Ranicki, *Algebraic L-theory and topological manifolds*, Cambridge Tracts 102, CUP 1992 —
  L-theory spectrum L^•, Postnikov tower.
- J. Milnor, D. Husemoller, *Symmetric Bilinear Forms*, Springer 1973 — W(ℝ)≅ℤ via signature.
- C.T.C. Wall, "Quadratic forms on finite groups, and related topics" / *Surgery on compact
  manifolds* — forms and L-theory.
- H. Toda, *Composition methods in homotopy groups of spheres*, Ann. Math. Studies 49, Princeton
  1962 — Toda brackets / compositions.
- J. Phillips, "Self-adjoint Fredholm operators and spectral flow", *Canad. Math. Bull.* **39**
  (1996) 460–467 — spectral flow, π_1(Fred^sa)=ℤ.
- J.-B. Bost, A. Connes, "Hecke algebras, type III factors and phase transitions with spontaneous
  symmetry breaking in number theory", *Selecta Math.* **1** (1995) 411–457 — partition = ζ.
- [literature GAP]: no e-invariant built from the divisor of ζ, nor an
  e-invariant ↔ Weil neg.ind identification, exists in the literature; the references anchor the tools, not
  the arithmetic bridge, which is new and remains in [GAP 162.C/D].
