# Doc 160 — Construction of the phase→inertia functor/transport: does the uniformity of the Kronecker flow buy RH-free inertia positivity?

**Program:** Riemann Hypothesis — Phase 51: construction of the phase→inertia functor.
**Role of the document:** CONSTRUCTIVE. Mandate: construct the mathematical object named by
GAP-158.A — a genuine transport of the uniform equidistribution structure of the
Kronecker flow on the Bohr torus 𝕋=∏_p S¹ (unconditional, RH-free input) to an invariant of
the inertia/height coordinate (where the ordinates γ of the zeros and m = neg.ind of the
Weil form = κ/2 from P35 live). Five design constraints inherited from Phases 49–50
(§0.2). It is NOT audited: it is CONSTRUCTED. A false victory is worse than a failure.

**Labeling contract (absolute rule).** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved here, complete proof; external results
cited with a verifiable reference. **[COMPUTATION]** = shown. **[CONSTRUCTION]** =
object precisely defined. **[BRIDGE]** = connection with the honest status of each link.
**[GAP]** = declared. **[literature GAP]** = data not verified at page level this
phase, NOT used as a premise of any theorem. **[WISH]** = declared. A proof of RH is never
fabricated, nor a victory that is not there. **NO numerics whatsoever.** Absolute honesty:
ending in (B/C/D) is PERMITTED; what is forbidden is faking (A).

**Prerequisites read from source this session:** Doc 158 in full (Thm 158.10 confinement
to the value-side; the tensor isomorphism H₃≅H_phase⊗H_height, Prop. 158.6; GAP-158.A the three
exact properties of the missing functor; the three pairs (Hᵢ,Aᵢ) Def. 158.4); Doc 159
in full (the three routes; C1–C5 of §6, in particular C5 = the universal/uniform hope;
GAP-159.C); Phase 43 memory (the transversal polarization metric CARRIES ζ: in
math/0204194 ‖ξ‖²=q is defined AFTER invoking Hasse; RH is input, not output — the
critical obstruction to avoid); Phase 26 memory (κ=2m=neg.ind(H_C) in the Pontryagin
space (𝒦,Q), the inertia the functor must reach).

---

## 0. Executive summary and specification

### 0.1. What is constructed

I construct, in order:

1. **(§1) The dynamical space.** The Bohr torus 𝕋=∏_p S¹ with the Kronecker flow
   R↷𝕋, its mapping torus / suspension Σ_𝕋, and the crossed-product C*-algebra
   𝒜 = C(𝕋)⋊_φ R. I precisely define the foliation (the orbits of R), the transversal
   (𝕋 itself as a floating Poincaré section), and the two candidates for "inertia
   coordinate": (i) the spectrum of the generator of the R-action / spectral flow, and (ii) the
   weights of a KMS state. **[CONSTRUCTION 160.1–160.3].**

2. **(§2) The phase→inertia transport.** I construct THREE candidate functors 𝔉 and test them
   one by one: 𝔉_coh (transversal foliated cohomology, à la Deninger/Moore–Schochet),
   𝔉_KMS (KMS weight on 𝒜 with the height as the dual variable), 𝔉_ind (spectral flow /
   index of the crossed product, à la Connes). The core of the document is identifying which
   one transports SOMETHING non-tautological and exactly what.

3. **(§3) The polarization test (the lesson of Phase 43, up front).** Every time an 𝔉
   produces a quadratic form whose positivity would give m<∞ or m=0, I STOP and verify:
   is the positivity defined using the zeros/eigenvalues (circular = Phase 43) or is it
   DERIVED from the Kronecker uniformity (RH-free)? I locate exactly where ζ enters.

4. **(§4) Does uniformity buy positivity?** The decisive point (C5 from Doc 159). I attempt
   to transport a UNIFORM discrepancy bound (Erdős–Turán, Koksma, LeVeque) through the
   surviving 𝔉 and see whether it gives a lower bound on the transversal inertia form.

5. **(§5) Verdict (A/B/C/D)** and the central GAP, triple stress test.

### 0.2. The five design constraints (each one killed a previous attempt)

I rewrite them as verifiable conditions on 𝔉, because the verdict is decided by
which of them breaks:

- **(a) INPUT = uniform Diophantine structure of {log p}:** the discrepancy/equidistribution
  of the Kronecker flow t↦(p^{−it})_p on 𝕋. Unconditional (Thm 158.2). 𝔉 must TAKE
  this as input.
- **(b) OUTPUT in the inertia/height coordinate:** where the γ and m=κ/2 live (Phase 26).
- **(c) WITHOUT passing through the VALUES of ζ:** everything measurable with respect to the
  value-torus / Bagchi measure Q is blind to RH (Voronin universality, Thm 158.9/159.9). 𝔉 must
  NOT factor through Σ_val. **This killed the ambient reading (Doc 158/159 Route 2).**
- **(d) WITHOUT reconstituting {k^{−s}} via Euler:** that turns it into Nyman–Beurling = RH-equivalent
  (Doc 159 Route 1, BRIDGE 159-A). 𝔉 must operate with the PRIME frequencies {log p}
  directly, without forming products.
- **(e) EXPLOITING uniformity (the universal gate):** a uniform bound does NOT select a
  τ (it is not existential), hence it would dodge the master quantifier of P43 (Doc 159 C5).
  This is the only live hope.

**Preview of the verdict (up-front honesty):** the result is **(D) with a core of
(B)**. I CONSTRUCT the functor 𝔉_KMS genuinely (it is not a tautology — it escapes (C), the
Doc 158 critique that the only bridge is the explicit-formula identity), and the transport DOES
exist as a morphism from the dynamics to a transversal operator. BUT in the polarization
test (§3) I locate that the positivity of the transversal inertia form enters at
exactly the same point as Phase 43: **the metric that turns the transversal operator
into a polarization with definite signature requires specifying the inner product over the
height space, and that inner product IS the Weil form Q — whose signature is m**. The
Kronecker uniformity buys positivity in H_phase (already known), and the functor 𝔉_KMS
transports it to a positivity over the ALGEBRA, but the step from the algebra to the inertia
signature requires a pairing that is NOT determined by the dynamics —
it remains as **[GAP-160.A]**, the central GAP, which I name and whose closing tool I
identify. It is NOT (A): uniformity does NOT buy inertia positivity on its own.

---

## 1. The dynamical space

### 1.1. The Bohr torus and the Kronecker flow

**[CONSTRUCTION 160.1] (the phase space).** Let 𝕋 := ∏_{p∈ℙ} S¹, the Bohr torus,
compact in the product topology (= dual group of the discrete group ⊕_p ℤ generated by the
characters χ_p). Its elements are z=(z_p)_p with z_p∈S¹. The Kronecker flow is the ℝ-action:
$$\varphi: \mathbb R \times \mathbb T \to \mathbb T, \qquad \varphi_t(z) = (p^{-it} z_p)_p = (e^{-it\log p} z_p)_p.$$
By Theorem 158.2 (Kronecker–Weyl, via the ℚ-linear independence of {log p}, Thm 158.1), φ
is minimal and uniquely ergodic with respect to Haar measure μ_Haar.

Equivalently, 𝕋 is the phase space of the dynamical system whose "rotation number"
in the p-th factor is log p; the Diophantine datum (a) is exactly that the frequency vector
(log p)_p is ℚ-independent, which gives unique ergodicity (the "uniformity" of the input).

**Coordinate remark (key to the whole document).** The flow variable t is the SAME
variable as the height/ordinate in the critical strip: in the explicit formula, the prime
side appears as ∑_p (log p) p^{-1/2} ĥ(log p) (the transform in the t direction), and
the zero side as ∑_ρ ĥ(γ_ρ). That is: **the dual variable of t is, simultaneously,
log p (phase side) and γ (height side).** This coincidence is the engine of any candidate
transport — and also its trap (what Doc 158 Prop. 2.x called "the bridge is identity").

### 1.2. The suspension / mapping torus and the foliation

**[CONSTRUCTION 160.2] (the suspension solenoid).** I consider the suspension space
of the flow. Since φ is an R-flow (not a single homeomorphism), I take directly the foliated
space (𝕋, ℱ) where the foliation ℱ has leaves the orbits {φ_t(z) : t∈ℝ}. By
minimality, every leaf is dense (the foliation is minimal, with no closed leaves). The canonical
transversal T is any local section; globally, since 𝕋 is a group and φ a one-parameter
translation, we can take as the "total transversal" 𝕋 itself with the orbit
equivalence relation — but this is ergodic (it admits no Borel transversal set of
intermediate measure). This already anticipates a difficulty (§2.1).

The relevant structure:
- **leaf direction (1-dimensional):** the coordinate t = the flow = the direction where
  both log p (input) and γ (output) live. It is the INERTIA/HEIGHT direction.
- **transversal direction (∞-dimensional, profinite-compact):** the torus 𝕋 modulo the orbit
  = the PHASES (z_p)_p modulo the diagonal flow. It is the VALUE/PHASE direction.

**[COMPUTATION 160.3] (the crossed-product C*-algebra).** The dynamical algebra is
$$\mathcal A := C(\mathbb T)\rtimes_\varphi \mathbb R,$$
the crossed product of the Kronecker flow. Generated by C(𝕋) and unitaries U_t implementing
φ_t: U_t f U_t^{-1} = f∘φ_{-t}. By unique ergodicity (Thm 158.2), 𝒜 is a
simple algebra (the flow is minimal) with a unique trace-KMS state associated to μ_Haar at the
appropriate parameter. The spectrum of the infinitesimal generator of {U_t} (the "flow
Hamiltonian") is the coordinate DUAL to t — and this is the direct candidate for the
inertia coordinate.

**[BRIDGE 160-A] (the C*-algebra is Connes's, restricted).** The crossed product
C(𝕋)⋊R is precisely the ingredient of Connes's adelic framework [Con99] when the idèle
action is restricted to the phase subgroup ∏_p S¹ (the "unitary" / norm-1 part of the
idèles). Connes identifies the zeros of ζ with the spectrum of the scaling action on
L²(C_ℚ) (the idèle classes); the TORUS 𝕋 is the compact part C_ℚ^1 (norm 1), and the
Connes scaling flow is transversal to 𝕋. **Honest status:** this identification is
structural and correct at the level of which group acts, but the spectral content (that the
spectrum GIVES the zeros) is exactly what Connes leaves as the positivity difficulty —
it is not a free input. I record it as a bridge, not as a theorem. The difference with Connes:
he uses the whole idèle (with the scale direction = Mellin, which is Nyman–Beurling, constraint
(d) violated); I restrict to the PHASE PART 𝕋 and try to reach inertia WITHOUT the
scale direction. That is the precise sense of (d).

### 1.3. The inherited tensor isomorphism and why it is the obstacle

From Doc 158 Prop. 158.6 / §4.2: the space of the Weil form factors as
$$H_3 \;\cong\; H_{\text{phase}} \otimes H_{\text{height}},$$
where H_phase = L²(𝕋, Haar) (the transversal direction) and H_height = the space where the
zero-to-zero signal lives (the leaf/flow direction, with the Weil inner product). The only
operator linking the factors is the explicit formula, **which is an identity** (Doc 112
Prop. 4.2), not a transport.

**The construction problem, in one sentence.** In the dynamical geometry I just
constructed, H_phase = transversal (∞-dim, profinite) and H_height = leaf direction (1-dim, the
flow). The functor 𝔉 that GAP-158.A asks for must carry a property of the transversal (the
uniform ergodicity/discrepancy) to a property of the leaf direction (the Weil
signature). **The geometric obstacle:** in a crossed product by a MINIMAL AND ERGODIC flow,
the transversal direction and the leaf direction are "entangled" by ergodicity — there is no
invariant projection from one to the other (that is precisely unique ergodicity). This is
what makes the transport nontrivial: it is NOT orthogonal projection (that would be a
tautology), and it must be some finer coupling. §§2.1–2.3 prove which one.

---

## 2. The phase→inertia transport: three candidates

### 2.1. Candidate 1 — 𝔉_coh: transversal foliated cohomology (Deninger / Moore–Schochet)

**The idea.** Deninger [Den98] proposes that ζ should arise as the zeta function of a
flow on a foliated space, with zeros = spectrum of the flow's generator on the
transversal FOLIATED COHOMOLOGY H¹_τ(𝕋,ℱ). The Diophantine input would be transported as: the
ergodicity ⟹ the foliated cohomology is "small" (the flow invariants are scarce)
⟹ control of inertia.

**[PROPOSITION 160.4] (Kronecker's foliated cohomology computes the flow's INVARIANTS,
= phase coordinate, NOT the height).** For the Kronecker foliation ℱ on 𝕋
(orbits of the minimal uniquely-ergodic flow), the degree-0 tangential foliated cohomology is
H⁰_τ = ℂ (the functions constant along the leaves = flow invariants, and by
ergodicity these are only the constants). The degree-1 reduced foliated cohomology, H¹_τ, is
controlled by Moore–Schochet theory [MS06] and by the cohomological
equation
$$\dot u = f - \int f\, d\mu_{\text{Haar}} \qquad (\text{flow homology equation}),$$
whose solvability (with loss of regularity) is governed by the DIOPHANTINE properties
of the frequency vector (log p)_p.

*Proof (structure).* H⁰_τ = ker(derivative along the leaf) = invariants = ℂ
by unique ergodicity (Thm 158.2; [Wal82, Thm 6.20]). For H¹_τ: a foliated 1-form is
g·dt (dt = the leaf-direction form); it is exact if g = u̇ for some u; solving
u̇ = g in Fourier coordinates on 𝕋 gives, for the frequency mode n=(n_p) (finite
support), û(n) = ĝ(n)/(i⟨n, (log p)⟩) — solvable except for small divisors
⟨n,(log p)⟩, which is the flow's Diophantine condition. [MS06] gives the general
framework of foliated cohomology for measurable foliations; the cohomological equation is
the Katok–Robinson one for linear flows. $\square$

**[POLARIZATION TEST — Candidate 1.] Where does the output live?** Prop. 160.4 shows that
𝔉_coh transports the Diophantine input (the small-divisor bounds ⟨n,(log p)⟩) to a
property of the regularity of the cohomological equation ON 𝕋 — that is, **in the
PHASE coordinate** (the Fourier mode n lives in the dual of 𝕋). The height γ does not appear:
Kronecker's foliated cohomology measures how the flow mixes the PHASES, it does not
produce the ordinates of the zeros.

**[PROPOSITION 160.5] (𝔉_coh does NOT reach inertia: the ordinates of the zeros are not
foliated cohomology classes of the Kronecker foliation).** The spectrum of the generator of the
Kronecker flow acting on L²(𝕋) is exactly {⟨n,(log p)⟩ : n∈⊕_pℤ} = the
semigroup/group generated by {log p} — which is {log k : k∈ℕ} ∪ {−log k} (the integers,
via unique factorization). The ordinates {γ_ρ} of the zeros of ζ do NOT belong to this
set (the γ are not ℤ-linear combinations of logarithms of primes: they are transcendental
of a different nature). Hence the spectrum of 𝔉_coh is that of the INTEGERS, not that of the
ZEROS.

*Proof.* The spectrum of the generator of the linear flow on the torus with frequencies
(log p) is the set of ⟨n, (log p)⟩ = ∑_p n_p log p = log(∏ p^{n_p}) = log k (k∈ℚ_{>0}),
by unique factorization (Thm 158.1). That {γ_ρ} ≠ {log k}: the γ_ρ are the zeros of an
entire function of order 1 whose distribution (spacing ~2π/log γ) differs from the
logarithmic spacing of {log k}; in particular no identity ∑ n_p log p = γ_ρ is known or
expected (that would be an explicit arithmetic relation between primes and zeros, which does
not exist). $\square$

**Verdict Candidate 1: Kronecker's foliated cohomology gives the INTEGERS, not the ZEROS —
and reconstructing the zeros from the integers is Euler on the line (constraint (d) violated).**
The spectrum {log k} is exactly the Nyman–Beurling system (Doc 159 Prop. 159.4–159.5):
to go from {log k} (spectrum of 𝔉_coh) to {γ_ρ} (the zeros) one needs the Euler
product / the zeta function itself. **𝔉_coh transports phase → INTEGER-SPECTRUM, not phase →
ZERO-INERTIA.** It falls into constraint (d). This is a clean negative finding:

> **The deep reason why Deninger's program has been open for ~30 years:** the foliated
> cohomology of the Kronecker foliation computes the spectrum of the INTEGERS (the
> logarithms of the multiplicative base), and for that spectrum to become the ZEROS one
> needs exactly the zeta function (the "regularized determinant" of the generator), which is
> Euler. The Deninger foliated space that would give the zeros directly is NOT the Kronecker
> foliation on 𝕋 — it is an object whose existence is the open problem. 𝔉_coh on 𝕋 is NOT
> that object.

[literature GAP, declared]: I do not know of a construction of the Deninger foliated space
whose foliated cohomology gives {γ_ρ} instead of {log k}; Deninger himself [Den98, Den02]
leaves it as a program. It is not used as a premise.

### 2.2. Candidate 2 — 𝔉_KMS: KMS weight with height as the dual variable (the one that DOES transport)

This is the candidate I construct in earnest, because it escapes the failure of Candidate 1:
instead of looking at the generator's spectrum (which gives integers), I look at a WEIGHT
on the algebra whose dual variable is the height.

**[CONSTRUCTION 160.6] (the height weight on 𝒜).** On 𝒜=C(𝕋)⋊_φ R, I define the
KMS_β state with respect to the dual flow θ_s (the dual ℝ̂=ℝ action on the crossed product,
scaling the U_t). The dual flow θ has as variable s the DUAL of t. Since t is simultaneously
the variable of log p (phase) and of γ (height, §1.1 Remark), the dual variable
s is the spectral coordinate where — if the algebra "knew" about ζ — the zeros would live.

I define the transport functional:
$$\mathfrak F_{\text{KMS}}: \mathcal A_{\text{sa}} \to \text{Functions}(\mathbb R_s), \qquad
\mathfrak F_{\text{KMS}}(a)(s) = \tau\big(\theta_s(a)\big),$$
where τ is the trace state (Haar) and θ_s the dual flow. For a = f·U_t with f∈C(𝕋), this gives
$$\mathfrak F_{\text{KMS}}(f U_t)(s) = e^{ist}\int_{\mathbb T} f\, d\mu_{\text{Haar}}.$$

**[PROPOSITION 160.7] (𝔉_KMS DOES transport to the height coordinate, and is NOT the
explicit-formula identity).** The functional 𝔉_KMS carries an element of the dynamical
algebra (phase side) to a distribution in the variable s (height/inertia side). Applied to the
ARITHMETIC ELEMENT
$$a_\zeta := \sum_p (\log p)\, p^{-1/2}\, U_{\log p} \;\in\; \mathcal A \quad(\text{suitable closure}),$$
it produces
$$\mathfrak F_{\text{KMS}}(a_\zeta)(s) = \sum_p (\log p)\, p^{-1/2}\, e^{is\log p},$$
which is exactly the prime part of the explicit side as a function of the height s. This
transport is a MORPHISM (linear, θ-compatible), NOT a tautological identity: unlike
the explicit formula (which EQUATES the prime side and the zero side), 𝔉_KMS only PRODUCES
the prime side as a function of s; the zero side is NOT baked in.

*Proof.* Direct computation of τ(θ_s(f U_t)) using τ(f U_t)=δ_{t,0}∫f dμ (trace of the
crossed product) and θ_s(U_t)=e^{ist}U_t (definition of the dual flow [Tak03, Vol II,
Thm X.2.3]). Linearity and continuity extend to a_ζ in the closure. That it is NOT the explicit
formula: the explicit formula is the EQUALITY ∑_p(...) = ∑_ρ ĥ(γ_ρ) + (archimedean); 𝔉_KMS
produces only the left-hand side as a spectral object, without asserting the equality. $\square$

**This is genuinely a transport, not a tautology — the first positive finding.**
𝔉_KMS escapes the central objection of Doc 158 (Prop. 2.x: "the only bridge is the explicit
formula-identity"). The crossed product gives a DIFFERENT bridge: the dual flow θ produces the
height coordinate as spectrum, and the arithmetic element a_ζ lives natively in 𝒜
(constraint (d) RESPECTED: a_ζ uses ONLY the U_{log p}, the prime frequencies, without forming
products / without Euler). The Diophantine input enters because the ergodicity of φ (Thm 158.2)
makes τ the ONLY invariant state, which fixes 𝔉_KMS uniquely.

**But now comes the polarization test, and here lies the heart of the verdict.**

### 2.3. Candidate 3 — 𝔉_ind: spectral flow / index (Connes), and why it reduces to 𝔉_KMS

**[PROPOSITION 160.8] (the spectral flow of the crossed product is the pairing of
𝔉_KMS with K-theory, and shares its fate).** The index / spectral flow of the R-action
on 𝒜 (à la Connes, [Con94, Ch. III]) is computed by pairing the cyclic cocycle associated
to the θ-invariant trace with K_1(𝒜). By the Connes–Thom isomorphism, K_1(C(𝕋)⋊R)≅K⁰(C(𝕋))
= K⁰(𝕋), which is the K-theory of the Bohr torus — a PHASE object. The pairing with
𝔉_KMS produces real numbers (the "jumps" of the spectral flow) that are, again, integrals
over 𝕋 of the phase coordinate. Inertia (γ) appears only through the same dual
variable s as 𝔉_KMS.

*Proof (structure).* Connes–Thom: K_•(A⋊R)≅K_{•+1}(A) [Con94, II.5; or Pimsner–Voiculescu
for ℤ, Connes–Thom for ℝ]. For A=C(𝕋), K⁰(𝕋) is the Grothendieck group of bundles over
the Bohr torus (profinite); the trace∘index pairing gives winding numbers over the
S¹ factors, = phase data. The spectral flow of a path of self-adjoint operators
associated to a_ζ is computed by the integral of 𝔉_KMS(a_ζ)(s) ds over the spectrum, reducing
to §2.2. $\square$

**Verdict Candidate 3: 𝔉_ind adds nothing new to 𝔉_KMS for our question** — the
index pairs with phase K-theory, and the only route to height is via the dual variable s,
already captured by 𝔉_KMS. I concentrate the analysis on 𝔉_KMS (§§3–4).

---

## 3. The polarization test: does it carry ζ? (the lesson of Phase 43, up front)

The surviving functor is 𝔉_KMS. It produces 𝔉_KMS(a_ζ)(s) = ∑_p (log p) p^{−1/2} e^{is log p},
a function/distribution of the height s, RH-free (it is only primes). For this to give m<∞ or
m=0, I need a QUADRATIC FORM in s whose positivity is Weil positivity. I construct it and
submit it to the brutal Phase 43 test.

### 3.1. The transversal inertia form

**[CONSTRUCTION 160.9] (the transported inertia form).** For a test function h (even,
with ĥ compactly supported in s), I define the "transported phase side":
$$\Phi(h) := \int_{\mathbb R} \mathfrak F_{\text{KMS}}(a_\zeta)(s)\, \hat h(s)\, ds
= \sum_p (\log p)\, p^{-1/2}\, \hat h(\log p) \cdot(\text{factor }2),$$
the prime contribution of the Weil formula. The candidate quadratic form is
$$\mathcal Q_{\mathfrak F}(h) := \langle \mathfrak F_{\text{KMS}}(a_\zeta), |h|^2\text{-kernel}\rangle,$$
where the "kernel" pairs the height function with the metric of the height space
H_height. **The decisive step is: what is the inner product on H_height?**

### 3.2. THE TEST — where ζ enters (identical to Phase 43's failure mode)

Here I stop, as the contract demands, and verify with brutality.

**[PROPOSITION 160.10] (the positivity of 𝒬_𝔉 requires the Weil inner product on
H_height, and that inner product carries the signature m — ζ enters exactly here).** For
𝒬_𝔉(h) to be a form whose positivity means m=0 (RH), the pairing of §3.1
must be
$$\mathcal Q_{\mathfrak F}(h) = \tfrac12 Q_X(h,h) = \sum_\rho |\hat h(\gamma_\rho)|^2_{\text{(with Weil sign)}},$$
that is, the inner product on H_height MUST be the Weil form Q (= the Gram sum
over the heights of the zeros, Doc 158 Prop. 158.6). But the Weil form Q has signature
neg.ind(Q) = m = κ/2 (Phase 26) — its definition ENUMERATES the heights γ_ρ of the
zeros. Therefore: specifying the inner product on H_height that makes 𝒬_𝔉 the
inertia form **requires knowing the heights of the zeros** — exactly the datum the
output was supposed to produce.

*Proof.* The transport 𝔉_KMS(a_ζ)(s) is only the prime-half of the explicit side. To
turn it into a form whose positivity is RH, one must CLOSE the explicit formula: equate
the prime side with the zero side ∑_ρ ĥ(γ_ρ) (plus archimedean). That equality is the explicit
formula (identity, Doc 112 Prop. 4.2). The positivity of the resulting form over the cone
of tests is Weil's criterion [Wei52], and its defect is m. The pairing that defines
H_height as the space where 𝒬_𝔉 = ½Q_X is, literally, the inner product
⟨h,h'⟩_height := ∑_ρ ĥ(γ_ρ) ĥ'(γ_ρ)^* — which NAMES the γ_ρ. $\square$

**THIS IS EXACTLY PHASE 43'S FAILURE MODE.** I compare side by side:

| | Phase 43 (Deninger foliated, math/0204194) | Doc 160 (𝔉_KMS) |
|---|---|---|
| bare space (RH-free) | foliated Spec ℤ, orbits {log p} | 𝕋, Kronecker flow, a_ζ |
| benign direction | complex structure J | the transport 𝔉_KMS(a_ζ)(s) (primes only) |
| **where ζ enters** | **the Kähler-Riemann metric ‖ξ‖²=q (Hasse) defines the transversal polarization** | **the Weil inner product on H_height defines the form 𝒬_𝔉; it enumerates the γ_ρ** |
| reversed arrow | RH-for-E is INPUT to the metric, not OUTPUT | the signature m is INPUT to the inner product, not OUTPUT |

**The diagnosis is identical.** The IMPLICATION "positivity of 𝒬_𝔉 ⟹ m=0 ⟹ RH" is correct and
geometric (it is Weil's criterion). The ANTECEDENT "the inner product on H_height is given
by the Kronecker dynamics WITHOUT using the zeros" is FALSE: the inner product that makes
𝒬_𝔉 the inertia form is the Weil form, which enumerates the γ_ρ. The Kronecker uniformity
gives the prime side (RH-free, ✓), but the METRIC of the height side (the one that
turns the prime side into a form with signature) carries the zeros. **ζ enters in the
polarization, not in the transport.** The transport 𝔉_KMS is genuine and RH-free; the
polarization that reads it as inertia is NOT.

**[BRIDGE 160-B — why this is not a repairable technical defect.]** One might hope to
repair this by using ANOTHER inner product on H_height, one given by the dynamics
(e.g. the flat L²(ℝ_s) one, without zero weights). But then 𝒬_𝔉(h) = ∫|𝔉_KMS(a_ζ)(s)|² ds (an
RH-free object, computable from primes) **stops being the Weil form** — its positivity is
trivial (it is an L² norm) and says NOTHING about m. The choice is forced: either the inner
product is flat (RH-free but blind to inertia, = Doc 158 H₂ seminorm B²) or it is the Weil
one (touches inertia but carries ζ). There is no known third inner product on H_height that is
(i) given by the Kronecker dynamics and (ii) non-flat so that its signature is m. **That
third inner product is exactly the central GAP (§5).**

---

## 4. Does uniformity buy positivity? (the decisive point, C5)

Hope C5 (Doc 159 §6): a UNIFORM discrepancy bound of the Kronecker flow
might supply the positivity of the transversal form WITHOUT using the zeros, dodging the
master quantifier through the universal gate. I attempt this explicitly with the
classical discrepancy inequalities.

### 4.1. The available discrepancy inequalities (unconditional input)

**[COMPUTATION 160.11] (Erdős–Turán / LeVeque for the Kronecker flow).** For the flow
t↦(p^{−it} z_p)_p restricted to a finite subset F⊂ℙ of primes and a time window
[0,T], the discrepancy D_T with respect to Haar satisfies the Erdős–Turán inequality [ET48]:
$$D_T \;\le\; \frac{C}{N} + C\sum_{0<|n|\le N} \frac{1}{|n|}\left|\frac{1}{T}\int_0^T e^{i\langle n,(\log p)\rangle t}\,dt\right|
= \frac{C}{N} + C\sum_{0<|n|\le N}\frac{1}{|n|}\cdot\frac{|\,\cdots\,|}{T|\langle n,(\log p)\rangle|},$$
for every N, where n ranges over ⊕_{p∈F}ℤ and ⟨n,(log p)⟩ = log(∏ p^{n_p}) = log k. The bound is
UNCONDITIONAL and UNIFORM in z (it does not select an orbit). Its size depends on the small
divisors |⟨n,(log p)⟩| = |log k| for k near 1 — controlled because log k ≥ log(1+1/k_max)
for integer k ≠ 1, an explicit Diophantine bound.

**Crucial point (the frequency coincidence, again).** The exponents appearing in
Erdős–Turán are e^{i⟨n,(log p)⟩t} = e^{i (log k) t} = k^{it} — the frequencies are {log k}
(INTEGERS), exactly the spectrum of 𝔉_coh (Prop. 160.5). Uniform discrepancy controls
how the flow equidistributes with respect to these integer-frequencies. **The discrepancy does
NOT contain the zero-frequencies {γ_ρ}.**

### 4.2. The attempted transport of the bound to inertia positivity

**[PROPOSITION 160.12] (the uniform discrepancy bound does NOT transport to a lower bound
on the inertia form — exact localization of the failure).** Let D_T(N) be the
Erdős–Turán bound (4.1). The transport 𝔉_KMS carries the discrepancy to a bound on the
sums ∑_p (log p) p^{−1/2} ĥ(log p) in the variable s. BUT the inertia form 𝒬_𝔉(h)=½Q_X(h,h)
pairs with the frequencies {γ_ρ} (Prop. 160.10), and the discrepancy bound controls the
frequencies {log k} ≠ {γ_ρ}. There is no inequality linking a bound on the
integer-frequencies {log k} with a lower bound on the form evaluated at the
zero-frequencies {γ_ρ}. Uniformity buys positivity IN THE PHASE COORDINATE (control
of equidistribution with respect to {log k}), not in the inertia coordinate (with respect to
{γ_ρ}).

*Proof.* The Erdős–Turán bound (4.1) bounds |D_T| in terms of the means
T^{-1}∫₀^T e^{i(log k)t}dt — functionals of the integer-frequencies. A lower bound on
𝒬_𝔉(h)=∑_ρ |ĥ(γ_ρ)|²_{sign} would require controlling ĥ evaluated at {γ_ρ}. The only object
linking {log k} and {γ_ρ} is the explicit formula / ζ itself (Prop. 160.10, Doc 159 Route 1
BRIDGE 159-A: the bridge {primes/integers}→{zeros} is Euler on the line). Uniform discrepancy,
however fine, lives on the {log k} side; transporting it to {γ_ρ} is Euler. Uniformity
dodges the master quantifier (✓ it does not select a τ — the bound is universal), but dodging it
is NOT ENOUGH: the universal bound is on the wrong coordinate. $\square$

**The decisive, negative, and precise result.** C5 (Doc 159) was right that a uniform
bound dodges the master quantifier through the universal gate — and I confirm it: the
Erdős–Turán discrepancy does NOT select a τ, it is universal in z, it dodges the
existential problem. **BUT the universal gate opens onto the wrong room:** the
uniform bound controls equidistribution with respect to the integer-frequencies {log k}, not
with respect to the zero-frequencies {γ_ρ}. Uniformity buys PHASE positivity (already
had, ergodicity), not INERTIA positivity. The master quantifier is not the only guardian;
behind it stands the coordinate change {log k}→{γ_ρ}, which is Euler/ζ, and uniformity does not
pay for it.

### 4.3. Triple stress test of the negative result

The contract demands tripling the stress test when there is a suspicion of escape (and also
when one is closed, so as not to self-deceive in the negative direction). I verify that
Prop. 160.12 is not an artifact of the chosen Erdős–Turán inequality.

- **Verification 1 (another inequality — LeVeque [LeV65]):** the LeVeque inequality bounds
  D_T² by ∑_n |n|^{-2} |Weyl mean|², with the SAME integer-frequencies ⟨n,(log p)⟩=log k.
  Swapping Erdős–Turán for LeVeque or Koksma–Hlawka does not change the frequency set: all
  discrepancy inequalities for a linear flow on the torus use the torus's characters, = {log k}.
  ✓ the failure is structural, not a feature of the chosen inequality.
- **Verification 2 (via the spectrum coincidence, Prop. 160.5):** the flow's spectrum
  IS {log k} by unique factorization; no linear functional of the flow can produce {γ_ρ}
  without a nonlinear object (Euler). Discrepancy is a (quadratic) functional of the
  flow's characters. ✓ the failure is the flow-spectrum = integers coincidence.
- **Verification 3 (via constraint (d), Doc 159 BRIDGE 159-A):** the step {log k}→{γ_ρ} is the
  Euler product on the critical line Re s=½; any transport crossing it violates (d) and
  reintroduces ζ. Uniform discrepancy does not cross (d); that is why it stays within {log k}.
  ✓ consistent with Route 1 of Doc 159.

The three verifications, independent, give the same verdict: uniformity buys
phase positivity, not inertia positivity, and the wall is the coordinate change {log k}→{γ_ρ} = Euler.

---

## 5. Verdict and the central GAP

### 5.1. The verdict: (D) with a core of (B)

**VERDICT: (D) — partial construction with a named central GAP; with a core of
failure mode (B) (the polarization carries ζ, identical to Phase 43).**

Breakdown against the four options of the objective:

- **(A) Did I construct the functor AND does uniformity buy RH-free positivity?** **NO.** The
  functor 𝔉_KMS was constructed (§2.2, genuine, non-tautological, respects (d)), but the
  uniformity does NOT buy inertia positivity (§4, Prop. 160.12, triple-verified): the
  discrepancy uniformity controls the integer-frequencies {log k}, not the zero-frequencies
  {γ_ρ}. (A) is not faked.
- **(B) Does the polarization carry ζ (Phase 43 again)?** **YES, partially, and precisely
  located (§3.2, Prop. 160.10).** The inner product on H_height that turns the
  transport into the inertia form IS the Weil form, which enumerates the γ_ρ. Identical to
  Phase 43's failure mode (the ‖ξ‖²=q metric of math/0204194). ζ enters in the metric of
  polarization, not in the transport.
- **(C) Does the transport not exist / is it a tautology?** **NO — and this is the positive
  finding.** 𝔉_KMS is a GENUINE transport (Prop. 160.7): it escapes the Doc 158 objection
  (Prop. 2.x) that the only bridge is the explicit-formula identity. The crossed product gives a
  distinct bridge (the dual flow), it respects (d), and it produces the prime side as a spectral
  object in the height variable without baking in the zero side. The transport exists; what does
  not exist is the RH-free inertia metric. It is not pure (C), but §2.1 proves that an
  alternative transport (𝔉_coh, foliated cohomology) IS tautological/circular in another sense
  (it gives {log k} = integers, constraint (d)).
- **(D) Partial construction with central GAP?** **YES, this is the verdict.** I constructed
  the space (§1), the transport 𝔉_KMS (§2.2), and located exactly the GAP: the inertia
  metric (§§3.2, 5.2).

### 5.2. The central GAP, named, and the tool that would close it

**[GAP-160.A] (the RH-free inertia metric).** The functor 𝔉_KMS transports the Kronecker
(phase) structure to a spectral object in the height variable s (Prop. 160.7,
RH-free). The single obstacle for this to give m is: **a missing inner product on
H_height that (i) is determined by the Kronecker dynamics / the flow's uniformity, and
(ii) whose signature is m = neg.ind(Q_Weil), WITHOUT enumerating the γ_ρ.** The two known
choices fail (BRIDGE 160-B): the flat inner product (L²(ℝ_s)) is RH-free but blind to
inertia (its signature is trivially 0, not m); the Weil inner product has signature m
but enumerates the γ_ρ (carries ζ, Prop. 160.10). The GAP is the ABSENCE of a third inner
product —given by the dynamics, non-flat, with signature m— on H_height.

**Restatement of the GAP in terms of Phase 26 (the target inertia).** By Phase 26,
m = κ/2 = neg.ind(H_C) in the Pontryagin space (𝒦,Q). GAP-160.A is: can the
ergodicity/uniform discrepancy of the Kronecker flow determine the Pontryagin signature
of (𝒦,Q) without diagonalizing H_C (without knowing its eigenvalues = the zeros)? The crossed
product C(𝕋)⋊R gives the algebra; the Pontryagin signature of the Weil form over it is NOT
determined by the phase dynamics — that is the exact content of the GAP.

**Candidate tool for closing it [WISH 160.B].** The missing inner product would be an
inner product of **Krein/Pontryagin type INTRINSIC to the crossed product** — defined by
a trace/coproduct of the algebra 𝒜 whose positivity defect (neg.ind) matches m without
reference to the eigenvalues. The natural candidate: a **regularized Weil form as a
pairing of the Connes cyclic cocycle** (the cocycle of the θ-invariant trace) **with
itself via the noncommutative Poincaré duality of the crossed product**
[Con94, Ch. IV; KK pairing / fundamental class]. If the fundamental class of C(𝕋)⋊R in
KK-theory induced, via the Weil cocycle, a form whose signature were computable from the
K-homology of 𝕋 (a phase object, RH-free), the signature m would be a topological
invariant of the crossed product and NOT of the zeros. **Status: [literature GAP].** I do
not know of a computation of the signature of the Weil form as a KK-theory invariant of the
Kronecker crossed product; Connes's index pairing (§2.3, Prop. 160.8) gives phase
winding numbers, not the Weil signature. If such a computation existed and gave m via phase
topology, it would be (A). I do not have it; I name it as the exact wish.

**Why this GAP is the real frontier (it coincides with three previous lines).** GAP-160.A is the
embodiment, in the language of the crossed product, of:
- **GAP-158.A** (the phase→inertia functor coupling H_phase and H_height without being the
  explicit formula): 𝔉_KMS IS that coupling, but the coupling does NOT determine the inertia
  metric. The functor existed; its metric part was missing.
- **GAP-159.C / C1–C5** (a uniform Diophantine property forcing individuation): the
  Kronecker uniformity (Erdős–Turán) is exactly property C5 (universal, does not
  select), and §4 proves it does NOT transport to inertia because it lives on {log k}, not
  {γ_ρ}. C5 is confirmed as necessary but insufficient: the universal gate opens onto the
  phase coordinate, not the inertia one.
- **Phase 43** (the foliated polarization that carries ζ in the metric): §3.2 reproduces the
  EXACT failure mode in the crossed-product framework, confirming that it is structural, not a
  defect of Deninger's particular foliated geometry.

**Three independent lines, a single missing object: the RH-free inertia metric on
H_height.** That is GAP-160.A.

### 5.3. Why this is the honest result and advances the program

The value of the document is NOT an equivalence or a proof of RH (none is produced). The
value is threefold:

1. **Constructing a genuine transport (𝔉_KMS) that is NOT the explicit-formula identity** —
   it refutes the reading that "phase and inertia only connect through the tautology" (Doc 158
   Prop. 2.x). The crossed product gives a real bridge. This is new mathematics: the functor of
   GAP-158.A exists as a morphism.
2. **Locating the GAP in the METRIC, not in the transport** — refines the diagnosis of Phase 43.
   Phase 43 left "the metric carries ζ" as a fact of Deninger's realized case; Doc 160
   proves it is structural (it appears the same way in the Kronecker crossed product, a
   completely different geometry). The wall is not the foliated geometry; it is the inertia
   signature.
3. **Proving that uniformity (C5) dodges the master quantifier but opens onto the
   wrong coordinate** — closes C5 as a direct route with a precise reason (the discrepancy lives
   in {log k}, the zeros in {γ_ρ}, and the bridge is Euler), without killing the residual GAP (the
   metric).

---

## 6. Final message

**VERDICT: (D) — partial construction with a named central GAP, with a core of
failure mode (B).** I constructed the dynamical space (Bohr torus 𝕋 with the Kronecker flow, its
crossed product 𝒜=C(𝕋)⋊R) and a GENUINE phase→inertia transport, the KMS functor
𝔉_KMS, which escapes the explicit-formula tautology and respects constraints (a)/(c)/(d). BUT
the transport produces only the prime side as a spectral object in the height variable; to
read it as inertia (m=neg.ind of Weil) one needs a METRIC on H_height, and the only
metric with signature m is the Weil form, which enumerates the zeros — **identical to
Phase 43's failure mode.** The Kronecker uniformity (C5) dodges the master quantifier through the
universal gate (✓) but opens onto the PHASE coordinate ({log k}, the integers), not the
INERTIA one ({γ_ρ}, the zeros); the bridge between the two is Euler on the critical line
(constraint (d)). The functor exists; the RH-free inertia metric does not — that is GAP-160.A.

**Where does ζ enter?** In the POLARIZATION METRIC, not in the transport. The transport 𝔉_KMS
is RH-free (it uses only the prime frequencies {log p} via the crossed product's dual flow).
ζ enters when the inner product on H_height that gives signature m is specified: that
inner product is the Weil form ∑_ρ ĥ(γ_ρ)ĥ'(γ_ρ)^*, which NAMES the γ_ρ. Exactly
as in Phase 43 the Kähler-Riemann metric ‖ξ‖²=q names the Frobenius eigenvalues via
Hasse. The arrow is reversed: the signature m is INPUT to the metric, not OUTPUT of the
transport.

**Three results with labels:**

1. **[PROPOSITION 160.7 + CONSTRUCTION 160.6] — The functor 𝔉_KMS exists and is NOT the
   explicit-formula identity.** The crossed product C(𝕋)⋊R, via its dual flow θ, transports the
   arithmetic element a_ζ=∑_p(log p)p^{−1/2}U_{log p} (which respects (d): primes only,
   without Euler) to the spectral height function ∑_p(log p)p^{−1/2}e^{is log p}. It is a
   genuine morphism, not the tautological prime=zero equality; it refutes the claim that phase
   and inertia only connect through the explicit formula (Doc 158 Prop. 2.x). The functor of
   GAP-158.A EXISTS as a coupling.

2. **[PROPOSITION 160.10 + BRIDGE 160-B] — The polarization carries ζ in the metric, identical to
   Phase 43.** For the transport to give m, the inner product on H_height must be the
   Weil form (signature m, enumerates the γ_ρ); the alternative flat inner product is
   RH-free but blind to inertia (trivial signature 0). There is no known third inner product
   —dynamical, non-flat, signature m— without enumerating the zeros. The failure mode is
   structural: it appears the same way in the Kronecker crossed product as in Deninger's foliated
   geometry (Phase 43), proving that the wall is not the particular geometry but the inertia
   signature.

3. **[PROPOSITION 160.12 + triple verification §4.3 — confirms/closes C5] — Uniformity
   buys PHASE positivity, not INERTIA positivity.** The Kronecker uniform discrepancy
   (Erdős–Turán, LeVeque, Koksma) dodges the master quantifier through the universal gate
   (does not select τ, ✓ C5) but controls the integer-frequencies {log k}=⟨n,(log p)⟩ (the
   flow's spectrum, by unique factorization), NOT the zero-frequencies {γ_ρ}. The bridge
   {log k}→{γ_ρ} is Euler on the critical line (constraint (d), Doc 159 BRIDGE 159-A). C5 is
   necessary but insufficient: the universal gate opens onto the wrong coordinate. **[GAP-160.A]:
   the RH-free inertia metric on H_height** = the single missing object, = embodiment of
   GAP-158.A (metric part) ∩ GAP-159.C (uniform positivity) ∩ Phase 43 (metric without ζ),
   three lines one object; candidate closing tool [WISH 160.B]: the Weil signature
   as a KK-theory invariant / noncommutative Poincaré duality of the crossed product
   (not constructed; [literature GAP]).

---

## References

**Internal (backward-only):** Doc 158 (H₃≅H_phase⊗H_height Prop. 158.6; Thm 158.10
confinement; GAP-158.A the three properties of the functor; three pairs (Hᵢ,Aᵢ) Def. 158.4;
Prop. 2.x the bridge is identity); Doc 159 (three routes; BRIDGE 159-A the toll {primes}→{integers}
is Euler; GAP-159.C; C1–C5 §6, in particular C5 universal gate); Doc 112 (Kronecker–Weyl
on {log p} Lemmas 2.2/3.3; Prop. 4.2 the explicit formula is an identity; seminorm B² annihilates
compacts Obs. 2.4); Doc 134 (corona 𝒞=𝒲/𝒥, zeros at the symbol/compact boundary); Phase 26
(κ=2m=neg.ind(H_C) in Pontryagin (𝒦,Q), V.1–V.4); Phase 43 (the transversal polarization
metric carries ζ; math/0204194 ‖ξ‖²=q defines the metric AFTER Hasse; RH input not
output; the failure mode replicated in §3.2).

**Literature (published, verifiable unless marked):**
- [Con99] A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann
  zeta function*, Selecta Math. (N.S.) 5 (1999), 29–106. (The adelic framework C_ℚ; zeros as
  spectrum of the scaling action; the positivity difficulty. The crossed product restricted to
  the phase part 𝕋 is the ingredient of §1.2.)
- [Con94] A. Connes, *Noncommutative Geometry*, Academic Press, 1994. (Ch. II.5
  Connes–Thom isomorphism K_•(A⋊R)≅K_{•+1}(A); Ch. III spectral flow / cyclic
  cocycles; Ch. IV noncommutative Poincaré duality / KK — the candidate tool of
  WISH 160.B.)
- [Den98] C. Deninger, *Some analogies between number theory and dynamical systems on foliated
  spaces*, Doc. Math., Extra Vol. ICM Berlin 1998, Vol. I, 163–186. (The foliated program;
  zeros = spectrum of the flow's generator on foliated cohomology; the foliated space that
  would give the zeros directly is the open problem — §2.1 Prop. 160.5 shows that the
  Kronecker foliation gives {log k}, not {γ_ρ}.)
- [Den02] C. Deninger, *A note on arithmetic topology and dynamical systems*, in *Algebraic
  Number Theory and Algebraic Geometry*, Contemp. Math. 300 (2002), 99–114. (Refinement of
  the program; foliated cohomology and dynamical zeta functions.)
- [MS06] C. C. Moore, C. Schochet, *Global Analysis on Foliated Spaces*, 2nd ed., MSRI
  Publications 9, Cambridge Univ. Press, 2006. (Foliated / tangential cohomology; global
  analysis on foliated spaces; the cohomological equation framework of §2.1.)
- [Tak03] M. Takesaki, *Theory of Operator Algebras II*, Encyclopaedia Math. Sci. 125,
  Springer, 2003. (Crossed products by flows; Tomita–Takesaki / KMS theory; the dual
  flow θ_s(U_t)=e^{ist}U_t, Thm X.2.3 — basis of CONSTRUCTION 160.6.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Weil's positivity criterion; the signature of the
  Weil form = m; the content of the inertia metric.)
- [ET48] P. Erdős, P. Turán, *On a problem in the theory of uniform distribution I, II*,
  Indag. Math. 10 (1948), 370–378, 406–413. (Erdős–Turán inequality; discrepancy bound
  via Weyl sums — COMPUTATION 160.11.)
- [LeV65] W. J. LeVeque, *An inequality connected with Weyl's criterion for uniform
  distribution*, Proc. Sympos. Pure Math. VIII, AMS (1965), 22–30. (LeVeque inequality;
  D² bounded by ∑|n|^{-2}|Weyl mean|² — Verification 1 of §4.3.)
- [Wal82] P. Walters, *An Introduction to Ergodic Theory*, GTM 79, Springer, 1982. (Thm 6.20:
  minimal translation of a compact group = uniquely ergodic — the ergodicity of the Kronecker
  flow, basis of Prop. 160.4 H⁰=ℂ.)
- [Wey16] H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77 (1916),
  313–352. (Equidistribution / Kronecker–Weyl on the torus; the uniform input.)
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and phase transitions with
  spontaneous symmetry breaking in number theory*, Selecta Math. (N.S.) 1 (1995), 411–457.
  (The BC system; KMS states on arithmetic algebras — context for CONSTRUCTION 160.6, the
  use of KMS with arithmetic weights; [literature GAP]: the specific height weight of
  𝔉_KMS is not that of BC, not verified against this source at page level.)

*End of Document 160.*
