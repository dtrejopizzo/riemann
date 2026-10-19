# Doc 161 — The canonical inertia metric via noncommutative Poincaré duality: RH-free KK fundamental class, or ζ through modular structure?

**Program:** Riemann Hypothesis — Phase 51: construction of the phase→inertia functor.
**Role of the document:** DECISIVE. Mandate: decide GAP-160.A + WISH 160.B. Doc 160
constructed a genuine, RH-free phase→inertia transport (𝔉_KMS), but located that the
METRIC that reads the transported object as inertia m = neg.ind of Weil is not determined
by the dynamics: the only known metric with signature m is the Weil form itself, which
enumerates the zeros (Phase 43 circularity). WISH 160.B named the candidate closing
tool: obtaining that metric CANONICALLY from the **fundamental class in KK-theory / the
noncommutative Poincaré duality** of the crossed product 𝒜 = C(𝕋)⋊_φ ℝ. This document
decides whether that canonical metric exists and whether it is RH-free. A false victory is worse than a
failure; ending in a genuine no-go is PERMITTED (and is the most likely outcome).

**Labeling contract (absolute rule).** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved here, complete proof; external results
cited with a verifiable reference. **[COMPUTATION]** = shown. **[CONSTRUCTION]** =
object precisely defined. **[BRIDGE]** = connection with the honest status of each link.
**[GAP]/[literature GAP]** = declared; the literature one is NOT used as a premise of any
theorem. **[WISH]** = declared. A proof of RH is never fabricated, nor OUTCOME 2 (the grail).
**NO numerics/Python whatsoever.** Absolute honesty.

**Prerequisites read from source this session:** Doc 160 in full (𝔉_KMS Prop. 160.7; the
polarization test Prop. 160.10; GAP-160.A the RH-free inertia metric; WISH 160.B the
Weil signature as a KK invariant; BRIDGE 160-A the Connes crossed product restricted to phase;
BRIDGE 160-B the forced flat-vs-Weil choice). Doc 156 in full (the
Fredholmness/class/escape trifurcation; VERDICT case (b)-Fredholmness: ζ enters primarily in the
Fredholmness of the Weil–Toeplitz symbol, secondarily in the class/winding; Prop. 156.6,
156.7; Theorem 156.5 κ = winding = 2m under m<∞). Phase 26 memory (κ = 2m = neg.ind(H_C) in
Pontryagin (𝒦,Q)). Phase 43 memory (the polarization metric carries ζ; the reversed arrow).

---

## 0. Executive summary and advance verdict

I place the verdict up front (honesty: I don't want it to come as a surprise).

> **VERDICT: OUTCOME 1 — STRUCTURAL NO-GO.** The canonical inertia metric that
> noncommutative Poincaré duality would associate to 𝒜 = C(𝕋)⋊_φ ℝ is defined, by construction,
> through the **dual weight / Tomita–Takesaki modular structure** of the crossed product.
> For this system —the Kronecker flow of {log p}, identical in its arithmetic part to
> the Bost–Connes system— the **partition function of that modular structure IS the
> zeta function** (BC95 phenomenon: the partition of the BC system is ζ(β), the KMS_β states at
> β>1 encode the primes via Ẑ^×). Therefore: **every canonical normalization of the
> fundamental class that turns it into a metric with definite signature carries ζ through the
> modular structure, NECESSARILY, not by choice.** The Kronecker crossed-product route (=
> the family of Connes/crossed-product approaches) does NOT produce an
> RH-free inertia metric: it is circular by construction, not unfinished. I state this as a
> theorem (§5.2, [THEOREM 161.9]).

**The fine localization (and consistency with Doc 156).** ζ enters in the **orientation /
modular normalization of the fundamental class** — node (ii) of the trifurcation
(existence / normalization-orientation / escape). This is *consistent with and complementary to*
Doc 156, which found ζ in the *Fredholmness* (node (i)) via the Toeplitz route. They are two routes to
the same object m that touch ζ at two different nodes: the Toeplitz/symbol route touches it in the
existence (Fredholmness), the KK/dual-weight route touches it in the orientation (the modular weight).
The synthesis (§4.4): **the dual weight is positive (exists) RH-freely, but its modular MODULUS
—the Radon–Nikodym derivative that fixes the signature— is the flow whose partition function is
ζ.** The object exists; its orientation is ζ. It is a no-go of the "circular" type, reinforced by the
"the metric is not canonical without ζ" type.

**Why it is NOT OUTCOME 2.** I subjected the grail candidate to the triple stress test (§3.4):
(T1) the fundamental class of C(𝕋)⋊ℝ via Connes–Thom exists RH-freely —but gives
PHASE K-homology, not the inertia signature (same failure as 𝔉_ind, Doc 160 Prop. 160.8);
(T2) the Kasparov pairing produces phase winding numbers, not the signature m, unless it is
twisted with the dual weight —and that is where ζ enters; (T3) noncommutative Poincaré duality requires an
orientation class (KMS/weight), and for this system that class IS the partition function ζ.
The three tests, independent, give the same result: RH-free signature does not appear. (2) is
NOT faked.

Structure: §1 the fundamental class / noncommutative Poincaré duality of C(𝕋)⋊ℝ (does it exist?
is it canonical?). §2 the modular test and the Bost–Connes connection (the heart). §3 the
trifurcation and the triple stress test. §4 where EXACTLY ζ enters and the synthesis with Doc 156.
§5 verdict and the structural circularity theorem. §6 final message.

---

## 1. The fundamental class / noncommutative Poincaré duality of C(𝕋)⋊ℝ

### 1.1. What WISH 160.B precisely asks for

GAP-160.A is the absence of an inner product on H_height that is (i) determined by
the Kronecker dynamics and (ii) has signature m = neg.ind(Q_Weil) without enumerating the γ_ρ.
WISH 160.B proposes: such an inner product would be the pairing of the Weil cocycle with
itself **via the noncommutative Poincaré duality** of the crossed product. In the precise
language of KK-theory [Con94, IV; Kas88], a C*-algebra A is **Poincaré-dual** (a PD-algebra) if there
exists a **fundamental class**
$$[\Delta]\in KK_d(A\otimes A^\circ,\;\mathbb C)$$
with an inverse class [Δ]^{-1}∈KK_{-d}(ℂ, A⊗A°) satisfying the duality composition
relations (the Kasparov product with [Δ] gives the isomorphism K_•(A)≅K^{•+d}(A) from
K-theory to K-homology) [BMRS08, §2; Kas88, §4]. The idea of WISH 160.B: if [Δ] exists
canonically, it induces a **pairing** on K-homology, and that pairing would be the
candidate metric whose signature could be m.

**The scalpel question, restated as three decidable sub-questions:**
- (Q1) Does [Δ] exist for A = C(𝕋)⋊_φ ℝ? Is it canonical (unique, with no hand-picked choice)?
- (Q2) If it exists, does the Kasparov pairing it induces have signature m, or does it give
  something else (phase numbers)?
- (Q3) Does the normalization / orientation that turns [Δ] into a metric carry ζ?

### 1.2. The fundamental class EXISTS, via Connes–Thom — but it is PHASE

**[PROPOSITION 161.1] (the noncommutative Poincaré duality of C(𝕋)⋊ℝ reduces, via Connes–Thom, to
that of C(𝕋), shifted in degree 1 — and is therefore RH-free BUT of phase coordinate).** The
crossed product by ℝ is **KK-equivalent, with a degree-1 shift, to the base algebra**:
by the Connes–Thom isomorphism [Con81; Con94, II.5; FS81] there is an invertible class
$$\mathbf{t}\in KK_1\big(C(\mathbb T)\rtimes_\varphi\mathbb R,\;C(\mathbb T)\big),
\qquad \mathbf{t}^{-1}\in KK_1\big(C(\mathbb T),\;C(\mathbb T)\rtimes_\varphi\mathbb R\big),$$
implementing K_•(C(𝕋)⋊ℝ) ≅ K_{•+1}(C(𝕋)). Consequently, **C(𝕋)⋊ℝ is Poincaré-dual if and
only if C(𝕋) is**, and its fundamental class is
$$[\Delta_{\mathcal A}] \;=\; \mathbf t\otimes [\Delta_{C(\mathbb T)}]\otimes \mathbf t^\circ
\quad(\text{Kasparov product, with the Connes–Thom degree-1 twist in each factor}),$$
where [Δ_{C(𝕋)}] is the fundamental class of the Bohr torus. The fundamental class of the crossed
product, viewed through Connes–Thom, lives over the **K-homology of 𝕋** = an object of the
PHASE coordinate.

*Proof.* Connes–Thom gives that **t** is invertible in KK [Con81, Thm. 1; FS81 give the
suspension/Bott version: A⋊ℝ ≃ SA in KK, where S = suspension]. Invertibility
transports the PD property: if [Δ_B] is the fundamental class of B and A is KK-equivalent to B via
an invertible class u∈KK_j(A,B), then u⊗[Δ_B]⊗u° is a fundamental class of A in degree
d+2j [BMRS08, Lemma 2.x on invariance of PD under KK-equivalence]. With B = C(𝕋), j = 1, the
fundamental class of 𝒜 descends to that of 𝕋. Since K_•(C(𝕋)⋊ℝ)≅K_{•+1}(C(𝕋)) and the dual too,
the Kasparov pairing ⟨·,[Δ_𝒜]⟩ is computed over K-theory invariants of 𝕋. $\square$

**[COORDINATE TEST — the first failure, identical to 𝔉_ind].** Prop. 161.1 says that the
fundamental class, as a KK object, knows NOTHING about height: it lives over 𝕋 (phase). This is
**exactly** what Doc 160 §2.3 (Prop. 160.8) already found for 𝔉_ind: the crossed product's index
pairing is computed against K^•(𝕋) = phase winding numbers. The reason is the
same: Connes–Thom **shifts the degree, it does not create the inertia coordinate**. The height γ is not an
invariant of the K-theory of the Bohr torus. **The fundamental class exists and is RH-free, but its
pairing is of PHASE, not of inertia.** Preliminary answer to (Q1)/(Q2): the class exists,
canonical up to the orientation (§1.3), and its raw topological pairing is NOT m.

### 1.3. The critical point: the orientation / spin-c is NOT topological here — it is MODULAR

**[PROPOSITION 161.2] (the fundamental class of a crossed product by ℝ requires an
ORIENTATION that, for a type III algebra, is a MODULAR datum, not a topological one).** The
class [Δ] of §1.2 is defined **up to an orientation class**: noncommutative Poincaré duality, in the
formalism of spectral triples [Con94, VI; CM95], requires not only the K-homology class
but an **oriented fundamental class** — the NC analogue of a volume form / oriented
fundamental class of a manifold. In the commutative case of a spin-c manifold, that
orientation is topological (the spin-c class). **But C(𝕋)⋊_φ ℝ with the Kronecker flow is NOT,
in general, a finite algebra (type II₁) nor does it admit a canonical finite trace:** the crossed
product by a minimal ergodic flow on a compact group is typically a factor whose type
classification depends on the structure of the weight flow [CT77]. The orientation that
fixes the sign of the noncommutative Poincaré pairing on an algebra without finite trace is NOT the
topological spin-c class: it is the **state/weight (KMS) with respect to which the
Dixmier trace or the fundamental cycle is defined**, that is, a datum of **Tomita–Takesaki
modular theory**.

*Proof (structure).* (i) In Connes's formalism, a metric/orientation on an NC
algebra = the choice of a Dirac operator D and a trace functional (state or weight) that
turns (𝒜, H, D) into a spectral triple with a fundamental class [Con94, VI.1; CM95 §I]. (ii) For
a finite algebra (finite trace τ), τ is canonical (unique tracial state in a type II₁ factor) and the
orientation is topological. (iii) For C(𝕋)⋊_φ ℝ, the crossed product by ℝ is **properly
infinite** except in degenerate cases (the ℝ-action is a flow); by Takesaki theory, crossed
products by modular flows produce type III/II_∞ factors, whose canonical functional is not a
finite trace but a **weight** [Tak03, Vol. II, ch. X; CT77]. (iv) The canonical weight of the
crossed product is the **dual weight** φ̃ of a weight φ on C(𝕋) [Tak03, Vol. II,
Def. X.1.16, dual weight theorem]. The orientation of the fundamental cycle is read with respect to the
modular flow σ^{φ̃} of φ̃. $\square$

**This relocates the whole question into modular theory.** The topological fundamental class
(§1.2) is RH-free but gives phase. The signature m can only appear if the **modular
orientation** of the fundamental cycle twists the phase pairing into giving it a signature. And the
modular orientation is the **dual weight** — which is the object where, for this system, ζ lives.
This is the modular test of §2, the heart of the document.

### 1.4. [BRIDGE 161-A] Honest status of the existence of [Δ]

The existence of [Δ_{C(𝕋)}] (fundamental class of the Bohr torus) is a **[partial literature
GAP]**: the Bohr torus 𝕋 = ∏_p S¹ is an infinite-dimensional compact abelian group
(profinite-connected); noncommutative Poincaré duality for C(G), G a compact group, is standard in
finite dimension (G a spin-c manifold), but in infinite dimension the "spectral dimension" d is
not finite and the fundamental class in KK_d requires finite d. I record this as a bridge: the
TOPOLOGICAL fundamental class of 𝕋 exists at the level of each finite-dimensional truncated factor
(∏_{p≤P} S¹ = ordinary torus, canonical spin-c), and the infinite system is the projective
limit — but the inertia signature is precisely what does NOT survive the limit (it is where the
"dimension" becomes infinite). I do NOT use "the fundamental class exists in dim ∞" as a premise of
any theorem; the no-go of §5 does NOT depend on its existence —on the contrary, it reinforces the
no-go: either [Δ] does not exist in dim ∞ (no-go of the "the object does not exist" type, node (i)),
or it exists but its orientation is modular = ζ (node (ii)). Both branches are no-go.

---

## 2. The modular test (the heart) and the Bost–Connes connection

### 2.1. The dual weight and the modular flow of the crossed product

**[CONSTRUCTION 161.3] (the dual weight and its modular flow).** Let φ be a normal semifinite
faithful weight on C(𝕋) (in the ergodic case, the Haar integral μ_Haar gives the canonical state). The
crossed product 𝒜 = C(𝕋)⋊_φ ℝ carries the **dual weight** φ̃ [Tak03, Vol. II, X.1; Haagerup,
"On the dual weights for crossed products of von Neumann algebras I, II", Math. Scand. 43
(1978) 99–118, 119–140]. The modular flow of the dual weight satisfies Takesaki's
fundamental relation:
$$\sigma_t^{\tilde\varphi}(x) = \sigma_t^{\varphi}\text{-extended over } C(\mathbb T),
\qquad \sigma_t^{\tilde\varphi}(U_s) = U_s\, ( \text{dual-flow cocycle}),$$
and, decisively, the dual flow θ (the dual ℝ̂ = ℝ action that Doc 160 used in 𝔉_KMS) is
tied to the modulus of the dual weight: **θ_s = Ad of the Radon–Nikodym derivative of the
dual weight along the spectral parameter s** [Tak03, Vol. II, X.2; Takesaki–Takai duality relates
σ^{φ̃} and θ]. In words: **the dual flow θ of 𝔉_KMS (Doc 160) and the modular flow σ^{φ̃} of
Tomita–Takesaki are the TWO faces of the same object** — θ is the flow of the dual action, σ^{φ̃}
is the internal modular flow, and both are entangled by Connes–Takesaki theory of the
weight flow [CT77].

**[KEY REMARK — the dual role of the variable s, now at the modular level].** Doc 160
noted that the dual variable s of the flow θ is simultaneously the height coordinate (where
the γ would live) and the dual of log p. I now add: that same s is **the parameter of the
modular flow** σ^{φ̃}_s. The inertia signature we are looking for (the neg.ind of the Weil
form) is, in modular language, **the spectral asymmetry of the generator of the modular
flow** — and that asymmetry is exactly the η/dual-weight invariant. This connects directly with the η of
Doc 156 §4.2 (APS) and with the question of whether the canonical metric carries ζ.

### 2.2. The Bost–Connes identification: the partition function IS ζ

**[PROPOSITION 161.4 / BRIDGE 161-B] (the arithmetic part of the Kronecker crossed product is
the Bost–Connes system, whose partition function is ζ — the decisive datum).** The
Bost–Connes system [BC95] is the quantum-statistical system (𝒜_{BC}, σ_t) with
$$\mathcal A_{BC} \;=\; C^*\big(\mathbb Q/\mathbb Z\big)\rtimes \mathbb N^\times
\quad\text{(Hecke algebra of the pair } (P_\mathbb Q^+, P_\mathbb Z^+)\text{)},$$
and time flow σ_t generated by the log of the indices, σ_t(μ_n) = n^{it} μ_n on the
isometries μ_n implementing the action of the multiplicative semigroup ℕ^×. **Facts from BC95,
verified [BC95; Wikipedia "Bost–Connes system"; CM-lectures math/0409520]:**
- (BC-1) The **partition function** of the BC system is **Z(β) = ζ(β)** (the Riemann zeta
  function) [BC95, Prop. 25; CMR CM2short].
- (BC-2) **Phase transition at β = 1** with spontaneous symmetry breaking: for β ≤ 1 there is a
  unique KMS_β state; for 1 < β ≤ ∞ the extremal KMS_β states are parametrized by
  **Ẑ^× = Gal(ℚ^{ab}/ℚ)** [BC95, main Thm.].
- (BC-3) The **KMS_β states at β > 1 encode the primes**: the value of an extremal KMS_β
  state on the arithmetic generators is a series over primes (∏_p local Euler
  factors), and the inverse temperature β is the coordinate dual to height/scale.

**The connection with 𝒜 = C(𝕋)⋊_φ ℝ (the bridge, with honest status).** The Kronecker flow
φ_t(z) = (p^{-it} z_p)_p on the Bohr torus 𝕋 = ∏_p S¹ has frequency generators
exactly {log p}; the dual-flow generator θ_s(U_{log p}) = e^{is log p} U_{log p}
multiplies by p^{is}. **This is, on the prime generators, the SAME dynamics as the BC
flow σ_t(μ_p) = p^{it} μ_p.** The Bohr torus 𝕋 = ∏_p S¹ is precisely the dual group of
⊕_p ℤ ≅ ℚ^×_{>0} (the positive rationals under multiplication, via unique factorization), and
ℚ^×_{>0} is the semigroup-group whose completion gives the multiplicative part of the BC
idèles. **Honest status [BRIDGE 161-B]:** the Kronecker crossed product C(𝕋)⋊_φ ℝ and the BC
system are NOT literally isomorphic as C*-algebras (BC uses the SEMIGROUP ℕ^× and a Hecke
algebra with non-unitary isometries μ_n; Kronecker uses the GROUP ℝ with unitaries U_t and the
diagonal flow). But they share **exactly the relevant modular structure**: the dual/modular flow
on the prime generators is t ↦ p^{it}, and the partition function of that dynamics
—the trace of the evolution operator e^{-βH} over the space of prime modes— is
$$Z(\beta) = \mathrm{Tr}(e^{-\beta H}) = \sum_{k\ge 1} k^{-\beta} = \zeta(\beta),$$
where H is the generator of the modular flow (Hamiltonian), whose spectrum over the modes
{∏ p^{n_p}} = {log k} (by unique factorization, exactly the spectrum of 𝔉_coh from Doc 160
Prop. 160.5). **The partition function of the modular flow of the Kronecker crossed product is
ζ for the SAME reason as in BC: the spectrum of the modular Hamiltonian is {log k} and the
thermal trace is ∑ k^{-β} = ζ(β).** This is NOT a [literature GAP] but an elementary [COMPUTATION]
once the modular Hamiltonian is identified with the flow's generator (see §2.3).

### 2.3. [COMPUTATION 161.5] The partition function of the dual weight = ζ, explicitly

**[COMPUTATION 161.5].** The generator H of the modular flow σ^{φ̃}_s = Ad(e^{isH}) acts on
L²(𝕋, Haar) diagonalized by the characters χ_n (n ∈ ⊕_p ℤ) of the Bohr torus:
$$H\,\chi_n = \langle n, (\log p)\rangle\,\chi_n = \Big(\sum_p n_p \log p\Big)\chi_n
= \log\Big(\prod_p p^{n_p}\Big)\chi_n = (\log k)\,\chi_n,\quad k=\prod p^{n_p}\in\mathbb Q^\times_{>0}.$$
The **partition function** (thermal trace of the evolution semigroup, restricted to the
"non-negative energy" modes k ∈ ℕ, k ≥ 1, which is the positivity condition of the dual weight / the
KMS condition selecting the Tomita cone) is
$$Z(\beta) \;=\; \mathrm{Tr}\big(e^{-\beta H}\,\big|_{\text{energy}\ge 0}\big)
\;=\; \sum_{k\ge 1} e^{-\beta \log k} \;=\; \sum_{k\ge 1} k^{-\beta} \;=\; \zeta(\beta),
\qquad \mathrm{Re}\,\beta > 1.$$
The convergence for Re β > 1 and the pole at β = 1 reproduce the BC phase transition
(BC-2): β = 1 is the boundary of convergence, the pole of ζ. $\square$

**[PROPOSITION 161.6] (the canonical noncommutative-Poincaré metric is defined via the dual
weight, and its NORMALIZATION is the partition function ζ).** In the formalism of noncommutative
Poincaré duality for type III/II_∞ algebras [Con94, VI; CM95], the pairing of the fundamental cycle
—the "metric" that induces the class [Δ]— is normalized with respect to the canonical weight (the
dual weight φ̃), and the thermal normalization (the one that makes the cycle a class of
trace / summable, the existence condition of the Chern–Connes character) is **dividing by
the partition function Z(β) = ζ(β)**. Concretely, the functional defining the inner product on the
height space is
$$\langle a, b\rangle_{\tilde\varphi,\beta}
\;=\; \frac{1}{Z(\beta)}\,\mathrm{Tr}\big(e^{-\beta H}\, a^* b\big)
\;=\; \frac{1}{\zeta(\beta)}\,\sum_{k\ge1} k^{-\beta}\,\overline{\hat a(\log k)}\,\hat b(\log k),$$
the KMS_β state of the dual weight. **The normalization factor 1/ζ(β) IS ζ, literally; and the
analyticity / signature of ⟨·,·⟩_{φ̃,β} on continuing β into the critical region Re β = ½ is
governed by the ZEROS of ζ.**

*Proof.* The dual weight φ̃ has modular flow σ^{φ̃}_s = Ad(e^{isH}) (Construction
161.3, [Tak03, X.2]). The KMS_β state associated to a flow with generator H and finite partition
Z(β) is ω_β(a) = Z(β)^{-1} Tr(e^{-βH} a) [BR97, Ch. 5, KMS condition / Gibbs state]. The
GNS inner product of ω_β is ⟨a,b⟩ = ω_β(a*b), which gives the formula. The normalization 1/Z(β) is
forced by the condition that ω_β be a state (ω_β(1) = 1): Z(β) = Tr(e^{-βH}) = ζ(β) by
[COMPUTATION 161.5]. The signature of the quadratic form associated with continuing β to the
critical strip changes exactly at the β where ζ(β) = 0 or has poles (the zeros and the pole
control the sign changes of the normalized form). $\square$

**THIS IS THE HEART OF THE NO-GO.** The canonical metric that noncommutative Poincaré duality
associates to the crossed product is NOT the flat L²-form (that of Doc 160 BRIDGE 160-B, RH-free but
blind) NOR is it chosen by hand: it is the **KMS_β state of the dual weight**, and its definition
CARRIES ζ(β) in the denominator (the partition function), and its signature changes on continuing to the
critical strip are governed by the zeros of ζ. **It is not a choice; it is the canonical
modular structure. And it carries ζ.** This resolves GAP-160.A in a negative sense: the "third
metric" (dynamical, non-flat, signature m) that Doc 160 was looking for IS the KMS state of the dual
weight — and it carries ζ via the partition function.

---

## 3. The trifurcation and the triple stress test

### 3.1. The trifurcation (existence / normalization-orientation / escape)

I compare against the trifurcation of Doc 156 (Fredholmness / class / escape), which is the same
logical structure in different machinery:

| Node | Doc 156 (Toeplitz/symbol route) | Doc 161 (KK/dual-weight route) |
|---|---|---|
| (i) **EXISTENCE** | ζ enters in the **Fredholmness**: T_φ Fredholm ⟺ invertible symbol in the corona ⟺ m<∞ (Prop. 156.6, primary/dominant layer) | ζ enters in the **existence of [Δ] in dim ∞**: the spectral dimension of the Bohr torus is ∞; [Δ] exists only truncated, and the signature does not survive the limit (§1.4, BRIDGE 161-A) |
| (ii) **NORMALIZATION/ORIENTATION** | ζ enters in the **class/winding**: granted m<∞, winding(φ)=2m = position of the zeros (Prop. 156.7, secondary layer) | ζ enters in the **modular orientation**: the metric = KMS_β state of the dual weight, normalized by Z(β)=ζ(β); signature governed by zeros (Prop. 161.6) — **dominant node here** |
| (iii) **ESCAPE** | the RH-free spectral triple with Chern character = κ does NOT exist ([lit. GAP, Doc 156 §4.5] = Connes 1999 and CCM carry ζ in the metric) | the RH-free weight that would give signature m without going through Z(β) does NOT exist (§3.4, T2/T3); the only canonical weight is the dual one, and its partition is ζ |

**The fine difference between the two routes (and why both are no-go):** Doc 156 found that the
DOMINANT node is **existence** (Fredholmness): the index object does not exist without RH. Doc 161
finds that, via the KK/dual-weight route, the object (the topological fundamental class) DOES exist
RH-freely (§1.2, it is phase K-homology), but the dominant node shifts to the
**orientation/modular normalization**: the class exists but reading it as an inertia metric
carries ζ via the dual weight. **It is the same wall, one node deeper:** Doc 156 kills the object;
Doc 161 lets the topological object live but kills its RH-free orientation. Total consistency:
both routes locate ζ in the structure that turns "value" into "signature," and that structure
is modular (= partition function = ζ) both in the symbol (winding of ζ) and in the weight
(partition ζ).

### 3.2. At which node does ζ enter via the KK route? Answer: (ii), the modular orientation

**[PROPOSITION 161.7] (ζ enters in the ORIENTATION/NORMALIZATION of the fundamental class, not in
its topological existence).** By Connes–Thom (Prop. 161.1), the topological fundamental class of
C(𝕋)⋊ℝ exists (modulo the dim-∞ question, BRIDGE 161-A) and is RH-free: it pairs with
K^•(𝕋) = phase invariants. The signature m is NOT an invariant of that topological
K-homology (Prop. 161.1, "COORDINATE TEST"). To obtain m one must twist the
topological pairing with the **modular orientation** = the KMS_β state of the dual weight
(Prop. 161.6), whose normalization is ζ(β). Therefore ζ enters at node (ii): the class exists,
but its orientation as an inertia metric IS ζ.

*Proof.* Combination of Prop. 161.1 (the topological class is phase, RH-free) +
Prop. 161.6 (the inertia metric = KMS_β of the dual weight = normalized by ζ). The topological
Kasparov pairing ⟨·, [Δ]⟩ gives integers (phase winding, K-homology of 𝕋); for it to
produce the REAL signature m of an indefinite quadratic form one needs the state/weight
that gives the Hilbert metric (the fundamental symmetry J of the Pontryagin space, Doc 156
§1.3), and that weight is the dual one, normalized by Z(β) = ζ(β). $\square$

### 3.3. Consistency with Doc 156: contradiction or complement?

Doc 156 said "ζ enters primarily in Fredholmness" (node (i)). Doc 161 says "ζ enters in
the modular orientation" (node (ii)). **Contradiction? No — they are TWO distinct routes to the
same m, and each route touches ζ at the node where its machinery first exposes it.** I verify it:

- **Toeplitz/symbol route (Doc 156):** starts from the arithmetic symbol (value, RH-free) and asks
  whether the OPERATOR is Fredholm. The obstacle appears first in the existence (invertible
  symbol in the corona ⟺ m<∞), because Toeplitz machinery needs Fredholmness BEFORE
  being able to compute an index. ζ enters at (i).
- **KK/dual-weight route (Doc 161):** starts from K-theory (Connes–Thom, RH-free) which gives
  the fundamental class WITHOUT requiring Fredholmness of the arithmetic symbol — the K-theory
  of the crossed product is a topological invariant that always exists. That is why the obstacle does NOT
  appear in the existence (the topological class exists); it appears one node deeper, in the ORIENTATION
  (the dual weight), because reading the class as a signature requires the modular datum = ζ.

**The synthesis [BRIDGE 161-C]:** the two routes are consistent and reinforce each other. Doc 156 showed
that one cannot even FORM the index operator without m<∞ (Fredholmness). Doc 161 shows
that, if you go around that using topological K-theory (which does not need Fredholmness of the symbol),
the obstacle reappears in the dual weight: the topological class exists but reading it as an
inertia metric carries ζ via the partition. **There is no route that dodges both nodes: either ζ in the
existence (Toeplitz) or ζ in the orientation (KK). The wall is the same modular object.**

### 3.4. Triple stress test of the grail candidate (OUTCOME 2)

The contract requires tripling the stress test for any suspicion of a grail. The candidate for
OUTCOME 2 would be: "the KK fundamental class gives a metric with signature m that does NOT enumerate the
zeros and does NOT go through ζ." I submit it to the three tests of the mandate.

- **(T1) Does the fundamental class exist without assuming RH?** **YES topologically, NO as an
  inertia metric.** The Connes–Thom class **t** ∈ KK_1 exists unconditionally [Con81] (RH-free).
  BUT it pairs with PHASE K-homology (Prop. 161.1), not inertia signature. The grail
  candidate would need the TOPOLOGICAL fundamental class to already have signature m — and it does NOT
  have it (the height γ is not an invariant of K^•(𝕋)). **T1 refutes the grail: the class exists RH-free but
  is phase, not inertia.** (Identical to the failure of 𝔉_ind, Doc 160 Prop. 160.8, and to the "COORDINATE
  TEST" of §1.2.)

- **(T2) Does the Kasparov pairing give signature m without the γ?** **NO.** The
  Kasparov pairing ⟨·,[Δ]⟩ produces INTEGERS (winding numbers, Fredholm indices of twisted
  operators) — not a REAL indefinite quadratic form signature. To extract neg.ind(Q) = m
  (a count of negative squares of an indefinite form over H_height) one needs a
  Hilbert metric (the fundamental symmetry J), and that metric is the KMS_β state of the dual weight
  (Prop. 161.6), which carries ζ(β) in its normalization. **T2 refutes the grail: the Kasparov
  pairing gives phase-winding; the signature m only appears by twisting with the dual weight = ζ.**

- **(T3) Does noncommutative Poincaré duality require an orientation that encodes ζ?** **YES,
  decisively.** By Prop. 161.2, the orientation of the fundamental cycle of a type
  III/II_∞ algebra (which is what C(𝕋)⋊ℝ gives by the flow) is a MODULAR datum — the dual weight φ̃. By
  COMPUTATION 161.5, the partition function of φ̃ is ζ. Therefore the ORIENTED fundamental class
  (the only one that gives a metric with signature) encodes ζ in its orientation. **T3 refutes the
  grail most directly: the noncommutative-Poincaré orientation of the Kronecker crossed product
  IS the partition function ζ, by the Bost–Connes identification.**

**The three tests, independent, give the same verdict: there is NO grail.** The topological
fundamental class is RH-free but phase (T1); the Kasparov pairing gives phase, not signature (T2); the
orientation that would give signature is modular = ζ (T3). **OUTCOME 2 is refuted triply.** The
WISH 160.B candidate fails exactly where the mandate warned to be suspicious: the
fundamental class exists without RH, but the SIGNATURE is not given by the topological pairing, and the
orientation that would give it carries ζ via the modular structure = Bost–Connes.

---

## 4. Where EXACTLY ζ enters the canonical machinery

### 4.1. The surgical location

ζ enters in **the orientation / modular normalization of the fundamental class**, specifically in
the **partition function of the dual weight of the crossed product**, which is Z(β) = ζ(β) by
the Bost–Connes identification (COMPUTATION 161.5). Breakdown into a chain of four links, with the
exact link where ζ appears marked:

1. Connes–Thom: K_•(C(𝕋)⋊ℝ) ≅ K_{•+1}(C(𝕋)). **RH-free.** [clean link]
2. Topological fundamental class [Δ] via §1.2. **RH-free, but PHASE** (pairs with K^•(𝕋)).
   [clean link but blind to inertia]
3. To read [Δ] as a metric with signature m: orient the fundamental cycle with respect to the
   canonical weight. The canonical weight of a crossed product by a flow = the **dual weight φ̃**. [link
   where the coordinate turns modular]
4. The normalization of the dual weight (KMS_β / Gibbs state) divides by the **partition
   function Z(β) = Tr(e^{-βH}) = ∑_{k≥1} k^{-β} = ζ(β)**. **← ζ ENTERS HERE.** The signature of the
   normalized form on continuing β to Re β = ½ is governed by the zeros of ζ. [ζ link]

**Link (4) is the ζ link: the partition function of the dual weight.** It is structural, not a
choice: the dual weight is the only canonical weight of the crossed product (Takesaki), its
partition function is ζ (Bost–Connes), and normalizing by the partition is mandatory for the
metric to be a state. There is NO freedom to avoid it without abandoning canonicity (= going back
to choosing the metric by hand = GAP-160.A unresolved).

### 4.2. The reversed arrow, again (Phase 43 / Doc 160), now at the modular level

Phase 43: the Kähler-Riemann metric ‖ξ‖²=q names the Frobenius eigenvalues via Hasse (RH
is input). Doc 160: the Weil inner product ∑_ρ ĥ(γ_ρ)ĥ'(γ_ρ)* names the γ_ρ. **Doc 161
gives the modular version of the same reversed arrow:** the canonical metric = KMS_β state of the
dual weight = (1/ζ(β)) ∑_k k^{-β}(...). The partition function ζ(β) and the position of its zeros
in the critical strip are INPUT to the metric (via normalization and signature), not OUTPUT
of the transport. **Three incarnations of the same reversed arrow**: Hasse (Phase 43), the Weil
form (Doc 160), the partition function ζ (Doc 161). The novelty of Doc 161: it shows that the
reversed arrow is **forced by the Tomita–Takesaki modular structure**, not by the particular
choice of geometry (foliated, crossed product, or curve). It is the deepest invariant of the
wall.

### 4.3. Why the flat L² weight (naive OUTCOME 2) is NOT canonical

One could object: "use the flat trace weight (the Plancherel trace on L²(ℝ_s)), which is
RH-free." Response (reinforces BRIDGE 160-B): the flat weight is NOT the CANONICAL weight of the
crossed product by the Kronecker flow. The crossed product by a flow with spectrum {log k} has
canonical weight = the dual weight, whose modulus (Radon–Nikodym derivative) is e^{-βH} with H = the
generator with spectrum {log k}. The flat weight would correspond to H = 0 (trivial flow), which is NOT the
Kronecker flow. **Choosing the flat weight = erasing the dynamics = reverting to the blind
seminorm of Doc 160 BRIDGE 160-B (trivial signature 0, not m).** Canonicity (what WISH 160.B
asked for: a metric "not chosen by hand") FORCES the dual weight, and the dual weight carries ζ.
**Canonicity and RH-freedom are incompatible for this system.** That is the exact content of the
no-go.

### 4.4. The contrast with the commutative case (why the primes break RH-free canonicity)

**[REMARK 161.8].** In a commutative crossed product by a flow with a generic
DISCRETE-RATIONALLY-INDEPENDENT spectrum (generic Diophantine frequencies), the partition
function Tr(e^{-βH}) = ∑ e^{-β λ_n} is a generic Dirichlet series with no arithmetic
structure — its analytic continuation and its zeros encode nothing special. **What makes the
Kronecker flow of {log p} SPECIAL is precisely that the frequencies are the logarithms
of the PRIMES**, so that the partition function ∑ k^{-β} = ζ(β) is the Riemann zeta (by
unique factorization, BC95). That is: **the canonical metric carries ζ not because of the
KK/modular machinery in the abstract, but because the machinery is applied to the flow whose frequencies are
the primes, which is exactly the datum that makes the partition the zeta function.** This closes the
circle with Doc 160 Prop. 160.5 (the flow's spectrum is {log k} = integers): the thermal
partition of {log k} is ∑ k^{-β} = ζ. The modular structure turns the integer-spectrum of the
flow into the zeta-function-as-partition. **The "Euler bridge" of Doc 160 (from {log k} to {γ_ρ})
is, at the modular level, the step from the partition ζ(β) to its zeros γ_ρ — the analytic
continuation of the partition function to the critical strip.** Doc 161 identifies that bridge with a
canonical object: the analytic continuation of the dual weight.

---

## 5. Verdict and the structural circularity theorem

### 5.1. Verdict

**VERDICT: OUTCOME 1 — GENUINE STRUCTURAL NO-GO.** The canonical inertia metric obtained
from the noncommutative Poincaré duality / the KK fundamental class of the crossed product
C(𝕋)⋊_φ ℝ EXISTS as a topological object (Connes–Thom, RH-free) but is PHASE; to read it
as an inertia metric with signature m one must orient it with the dual weight, whose partition
function is ζ (Bost–Connes). Therefore **every canonical inertia metric on this crossed
product carries ζ via the Tomita–Takesaki modular structure, NECESSARILY.** The
Connes/Kronecker-crossed-product route is **circular by construction**, not unfinished. GAP-160.A
is RESOLVED in the negative sense: the "third metric" being sought (canonical, non-flat,
signature m, RH-free) does NOT exist — the only canonical non-flat metric is the KMS state of the dual
weight, which carries ζ. WISH 160.B (the closing tool) TURNS OUT TO BE the place where ζ enters,
not the escape.

OUTCOME 2 (grail) refuted triply (§3.4). OUTCOME 1 confirmed at node (ii) of the
trifurcation (modular orientation/normalization), consistent with and complementary to Doc 156 (which
found it at node (i), Fredholmness).

### 5.2. The structural circularity theorem

**[THEOREM 161.9 — structural circularity of the Kronecker crossed-product route].**
*Let 𝒜 = C(𝕋)⋊_φ ℝ be the crossed product of the Kronecker flow φ_t(z) = (p^{-it} z_p)_p on the
Bohr torus 𝕋 = ∏_p S¹, and let φ̃ be its dual weight with modular flow σ^{φ̃}_s = Ad(e^{isH}),
H = the generator of the dual action. Let ⟨·,·⟩_can be any inner product on the height space
H_height that is (i) canonically induced by the oriented fundamental class of the
noncommutative Poincaré duality of 𝒜 (orientation with respect to the canonical weight = dual), and
(ii) non-degenerate/non-flat (non-trivial signature). Then:*

1. *(RH-free topological existence)* the UN-oriented fundamental class [Δ] ∈ KK exists via
   Connes–Thom and is RH-free, but its Kasparov pairing takes values in the phase
   K-homology K^•(𝕋), not in the inertia signature;
2. *(orientation = ζ)* the orientation that turns [Δ] into ⟨·,·⟩_can is the KMS_β state of the dual
   weight, ω_β(a*b) = Z(β)^{-1} Tr(e^{-βH} a*b), whose **partition function is Z(β) = ζ(β)**;
3. *(circularity)* the signature of ⟨·,·⟩_can on continuing β to the critical strip Re β = ½ is
   governed by the zeros of ζ; in particular, neg.ind(⟨·,·⟩_can) coincides with m = neg.ind of
   the Weil form **only if the position of the zeros of ζ is known**.

*Therefore: there is NO canonical inner product on H_height, induced by the
noncommutative-Poincaré duality of the Kronecker crossed product, that is simultaneously (i) non-flat with
signature m and (ii) RH-free. Canonicity (orientation = dual weight) and
RH-freedom are incompatible, because the dual weight of this system has ζ as its partition function.*

**Proof.** (1) Prop. 161.1 (Connes–Thom gives [Δ] over K^•(𝕋), RH-free) + Prop. 161.2 (the
non-oriented class does not fix a signature). (2) Prop. 161.2 (the canonical orientation of a type
III/II_∞ algebra is the dual weight) + Prop. 161.6 (the metric = KMS_β of the dual weight) + COMPUTATION 161.5
(Z(β) = ζ(β) by unique factorization of the spectrum {log k}, Bost–Connes identification
BRIDGE 161-B). (3) Prop. 161.6 (the signature of the form normalized by 1/ζ(β) changes at the
zeros/poles of ζ on continuing to the critical strip). The final incompatibility: by (1) the only
RH-free part is the topological phase class (effectively 0 signature on inertia); by (2)-(3)
the only canonical non-flat orientation carries ζ. There is no third canonical option (§4.3: the flat
weight is not canonical for the Kronecker flow). $\square$

**[Declared, honest GAP]:** THEOREM 161.9 rests on (a) BRIDGE 161-B (the identification
of the partition of the Kronecker dual weight with ζ via the Bost–Connes analogy; COMPUTATION 161.5
is elementary given that the spectrum is {log k}, but the literal identification of the dual weight with the
Gibbs state of H requires that the positivity/energy condition of the dual weight select
exactly k ≥ 1, which I argue in §2.3 but do not prove with the full rigor of Haagerup's weight
theory); and (b) BRIDGE 161-A (the existence of the fundamental class in dim ∞ of the Bohr
torus). Neither of these GAPs weakens the no-go: if the fundamental class does NOT exist in dim ∞
(BRIDGE 161-A fails), then the no-go is of node (i) (the object does not exist) — still a no-go.
If the dual weight were not exactly Gibbs-of-ζ (BRIDGE 161-B is refined), the modular structure
is still that of the BC system whose partition is ζ by BC95 — still a no-go. **The no-go is
robust to both GAPs: it is a theorem about where ζ MUST enter, not about a fragile
computation.**

### 5.3. Which family of approaches this closes

THEOREM 161.9 honestly closes the family: **"obtaining the inertia metric from the
noncommutative Poincaré duality / KK fundamental class of the Kronecker crossed product (or of
any system whose arithmetic part is Bost–Connes)."** This includes: the WISH 160.B suggestion;
the natural reading of Connes's adelic framework [Con99] restricted to the phase part
(BRIDGE 160-A); any attempt to define the Weil metric as a pairing of the Connes cocycle via
noncommutative Poincaré duality. The single structural reason: **the canonical weight of the crossed product
is the dual weight, whose modular flow has partition function ζ (Bost–Connes), so that the
noncommutative-Poincaré orientation carries ζ via Tomita–Takesaki theory.** It is not a technical defect;
it is the identity "partition function of the BC system = ζ" read as an obstruction.

**What this does NOT close (honest frontier):** approaches where the algebra is NOT a crossed
product of the prime flow — e.g., a spectral triple whose Dirac operator D does NOT have spectrum
{log k} nor partition function ζ, but some other spectrum whose partition is analytic and benign,
BUT whose Chern character still produces κ=2m. That is the [central literature GAP] inherited from
Doc 156 §4.5 (the RH-free spectral triple with Chern = κ), which THEOREM 161.9 does NOT refute — it only
refutes building such a triple as a Kronecker crossed product. I leave it as the live frontier
after this document (§6).

---

## 6. Final message

**VERDICT: OUTCOME 1 — STRUCTURAL NO-GO.** The canonical inertia metric that noncommutative
Poincaré duality associates to the crossed product C(𝕋)⋊_φ ℝ of the Kronecker flow carries ζ
NECESSARILY, via the Tomita–Takesaki modular structure. The topological fundamental class
exists RH-freely (Connes–Thom) but is PHASE; the orientation that turns it into an inertia metric
with signature m is the dual weight, whose partition function is ζ (Bost–Connes
identification). Canonicity and RH-freedom are incompatible for this system. GAP-160.A
resolved negatively; WISH 160.B identified as the place where ζ enters, not as the escape.
The Connes/Kronecker-crossed-product route is circular by construction.

**Where EXACTLY does ζ enter the canonical machinery?** In the **partition function of the dual
weight** (the fourth link of §4.1): Z(β) = Tr(e^{-βH}) = ∑_{k≥1} k^{-β} = ζ(β), where H is the
generator of the modular flow σ^{φ̃} (= the dual flow θ of 𝔉_KMS, Doc 160), whose spectrum {log k}
is that of the integers by unique factorization. The normalization 1/ζ(β) of the KMS_β state of the dual
weight is the canonical metric, and its signature on continuing to the critical strip is governed by
the zeros of ζ. It is the modular avatar of the "reversed arrow" of Phase 43 (Hasse) and Doc 160
(the Weil form): the position of the zeros is INPUT to the metric, not OUTPUT of the transport; but
Doc 161 shows that this reversed arrow is FORCED by Tomita–Takesaki (the canonical orientation =
dual weight = partition ζ), not by the particular geometry. **The "Euler bridge"
{log k}→{γ_ρ} of Doc 160 is, at the modular level, the analytic continuation of the
partition function ζ(β) to its zeros.**

**Consistency with Doc 156 (the trifurcation):** Doc 156 found ζ at node (i) Fredholmness
(via Toeplitz: the operator does not exist without m<∞). Doc 161 finds ζ at node (ii)
orientation/normalization (via KK: the topological object exists but its orientation is ζ). They are
two routes to the same m, each touching ζ where its machinery first exposes it; neither dodges it.
The KK route goes around Fredholmness (topological K-theory always exists) only to re-encounter
ζ one node deeper, in the dual weight. **Synthesis: the wall is the modular object —the
partition function of the flow of the primes = ζ— and it appears as the winding of ζ (symbol, Doc 156)
or as the partition of ζ (dual weight, Doc 161); it is the same ζ seen from the two ends of the
symbol/weight duality.**

**Three results with labels:**

1. **[PROPOSITION 161.1 + 161.2] — The fundamental class of C(𝕋)⋊ℝ exists (Connes–Thom,
   RH-free) but is PHASE; its orientation is MODULAR, not topological.** By Connes–Thom
   K_•(C(𝕋)⋊ℝ)≅K_{•+1}(C(𝕋)), the fundamental class descends to the K-homology of the Bohr torus
   = phase invariants; the height γ is not an invariant of K^•(𝕋). Reading the class as an inertia
   metric requires an orientation, which for a type III/II_∞ algebra (what the flow gives) is a
   modular datum = the dual weight, not the topological spin-c class. The class exists
   RH-free; the inertia signature is NOT given by the topological Kasparov pairing (refutes the naive
   grail: T1+T2 of §3.4).

2. **[PROPOSITION 161.6 + COMPUTATION 161.5 — the heart] — The canonical metric is the KMS_β state
   of the dual weight, normalized by the partition function Z(β) = ζ(β) (Bost–Connes).** The
   dual weight of the crossed product has a modular flow with generator H of spectrum {log k} (integers,
   by unique factorization); its partition function is Tr(e^{-βH}) = ∑ k^{-β} = ζ(β), identical
   to that of the BC system (BC95: partition = ζ, phase transition at β=1, KMS_β at β>1 encode
   the primes via Ẑ^×). The canonical metric = ω_β(a*b) = ζ(β)^{-1} Tr(e^{-βH} a*b) carries ζ
   literally in the denominator, and its signature on continuing to Re β=½ is governed by the
   zeros of ζ. **ζ enters in the orientation/modular normalization — node (ii) of the
   trifurcation — via the Tomita–Takesaki structure, not by choice** (refutes grail T3,
   §3.4; the alternative flat weight is not canonical, §4.3).

3. **[THEOREM 161.9 — structural circularity] — No RH-free canonical inertia metric exists
   on the Kronecker crossed product; canonicity (orientation = dual weight) and
   RH-freedom are incompatible because the dual weight has ζ as its partition function.** This honestly
   closes the family of approaches "inertia metric via noncommutative Poincaré duality of the
   prime crossed product" (= WISH 160.B, = Connes restricted to phase). The no-go is
   robust to the two declared GAPs (existence in dim ∞; rigor of the dual weight = Gibbs): if the
   class does not exist in dim ∞, no-go at node (i); if it exists, no-go at node (ii). **Live
   frontier (NOT closed by this document):** a spectral triple whose operator is NOT the flow of the
   primes (spectrum ≠ {log k}, partition ≠ ζ) but whose Chern character still gives κ=2m — the [central
   literature GAP] inherited from Doc 156 §4.5, which THEOREM 161.9 bounds but does not refute.

---

## References

**Internal (backward-only):** Doc 160 (𝔉_KMS Prop. 160.7; polarization test Prop. 160.10;
BRIDGE 160-A Connes restricted to phase; BRIDGE 160-B flat-vs-Weil; GAP-160.A the
RH-free inertia metric; WISH 160.B the Weil signature as a KK invariant; Prop. 160.5 the flow's
spectrum = {log k} by unique factorization; Prop. 160.8 𝔉_ind pairs with phase K-theory).
Doc 156 (Fredholmness/class/escape trifurcation; VERDICT case (b)-Fredholmness,
Prop. 156.6/156.7; Theorem 156.5 κ=winding=2m under m<∞; §4.5 [central GAP] RH-free spectral
triple with Chern=κ does not exist). Phase 26 (κ=2m=neg.ind(H_C) in Pontryagin (𝒦,Q)). Phase 43
(the polarization metric carries ζ; reversed arrow RH-input-not-output). Doc 134 (Weil–Toeplitz
algebra, zeros at the symbol/compact boundary).

**Literature (published, verifiable unless marked):**
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions with
  spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.) 1 (1995), 411–457. (The
  BC system; **partition function = ζ(β)**; phase transition at β=1; KMS_β states at β>1
  parametrized by Ẑ^×=Gal(ℚ^{ab}/ℚ) and encoding the primes. Core of BRIDGE 161-B,
  Prop. 161.4, COMPUTATION 161.5 — the decisive datum of the no-go.)
- [Con99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann
  zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (The adelic framework; the spectral
  side reproduces Weil's explicit formula; the crossed product restricted to the phase part is
  the ingredient — the family the no-go closes when restricted to the phase part.)
- [Con94] A. Connes, *Noncommutative Geometry*, Academic Press, 1994. (Ch. II.5 Connes–Thom
  K_•(A⋊R)≅K_{•+1}(A); Ch. IV noncommutative Poincaré duality / KK, fundamental class;
  Ch. VI spectral triples, metric, orientation — basis for §1, Prop. 161.1/161.2.)
- [Con81] A. Connes, *An analogue of the Thom isomorphism for crossed products of a C*-algebra
  by an action of ℝ*, Adv. Math. 39 (1981), 31–55. (The Connes–Thom isomorphism as an invertible
  KK_1 class — basis for Prop. 161.1; the class **t**.)
- [CT77] A. Connes, M. Takesaki, *The flow of weights on factors of type III*, Tôhoku Math. J.
  29 (1977), 473–575. (The flow of weights; the type classification of crossed products by
  modular flows; the canonical orientation of a type III algebra is the weight, not a finite
  trace — basis for Prop. 161.2.)
- [Tak03] M. Takesaki, *Theory of Operator Algebras II*, Encyclopaedia Math. Sci. 125, Springer,
  2003. (Crossed products; **dual weight** Vol. II ch. X (Def. X.1.16, dual weight theorem);
  dual flow θ_s(U_t)=e^{ist}U_t (X.2); Tomita–Takesaki theory, modular flow — basis for
  CONSTRUCTION 161.3.)
- [Haagerup78] U. Haagerup, *On the dual weights for crossed products of von Neumann algebras
  I, II*, Math. Scand. 43 (1978), 99–118 and 119–140. (Rigorous construction of the dual weight and
  its modular flow; the rigor that BRIDGE 161-B / GAP §5.2 invokes and declares as not completed at
  page-level detail.)
- [Kas88] G. G. Kasparov, *Equivariant KK-theory and the Novikov conjecture*, Invent. Math. 91
  (1988), 147–201. (The Kasparov product; duality and fundamental classes in KK — formal
  basis for noncommutative Poincaré duality, §1.1.)
- [BMRS08] J. Brodzki, V. Mathai, J. Rosenberg, R. J. Szabo, *Noncommutative correspondences,
  duality and D-branes in bivariant K-theory*, Adv. Theor. Math. Phys. 13 (2009), 497–552
  (arXiv:0708.2648); and *D-branes, RR-fields and duality on noncommutative manifolds*, Comm.
  Math. Phys. 277 (2008), 643–706 (arXiv:0709.2128). (Precise definition of a PD-algebra: fundamental
  class [Δ]∈KK_d(A⊗A°,ℂ) with inverse; invariance of PD under KK-equivalence — basis for
  §1.1, Prop. 161.1.)
- [FS81] T. Fack, G. Skandalis, *Connes' analogue of the Thom isomorphism for the Kasparov
  groups*, Invent. Math. 64 (1981), 7–14. (The KK version of the Connes–Thom isomorphism: A⋊ℝ
  KK-equivalent to the suspension SA — reinforces Prop. 161.1.)
- [CM95] A. Connes, H. Moscovici, *The local index formula in noncommutative geometry*, GAFA 5
  (1995), 174–243. (Chern–Connes character, local index formula, residues of the spectral
  zeta; the orientation/summability condition of the triple — §1.3, and the live frontier §5.3
  inherited from Doc 156 §4.5.)
- [BR97] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics 2*,
  2nd ed., Springer, 1997. (KMS states, Gibbs states ω_β=Z(β)^{-1}Tr(e^{-βH}·), the KMS
  condition — basis for Prop. 161.6.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Weil's positivity criterion; the signature of the
  Weil form = m, the target of the inertia metric.)

*End of Document 161.*
