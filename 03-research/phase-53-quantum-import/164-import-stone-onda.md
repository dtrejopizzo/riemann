# Doc 164 — Importing Stone's theorem: a structural unitary evolution whose generator has spectrum {γ}, with RH-free unitarity? Or is unitarity the Weil metric in disguise?

**Program:** Riemann Hypothesis — Phase 53: quantum import.
**Role of the document:** CONSTRUCTIVE with the UNITARITY GUARD at the front. Mandate: import the
machinery of mathematical quantum mechanics (Stone's theorem, essential self-adjointness, position-
momentum Fourier duality) to CONSTRUCT the object X of which primes and zeros are two
representations —by analogy with how ψ resolved wave-particle duality— or to PRECISELY LOCATE the
obstruction. The central tool to import is **Stone's theorem**: in QM the reality of the spectrum
(real eigenvalues) does NOT come from a chosen metric but from the evolution being UNITARY
(a conservation law), {U(t)=e^{itH}} group ⟺ H self-adjoint ⟺ spec(H)⊂ℝ. The bet: if {γ} were the
spectrum of the generator of a unitary evolution whose unitarity comes from a structural SYMMETRY
(the functional equation s↔1−s), not from a metric, then RH = "real spectrum" = automatic by Stone,
and the metric through which ζ re-enters would be replaced by a structural conservation law.

**Labeling contract (absolute rule).** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = genuinely proved here, complete proof; external ones with a
verifiable reference. **[CONSTRUCTION]** = precisely defined object. **[BRIDGE]** = connection with
an honest status. **[GAP]/[literature GAP]** = declared; a literature gap is NEVER used as a premise
of any theorem. **[WISH]** = declared. A proof of RH or a false victory is never fabricated
(OUTCOME A). PERMITTED (and expected) to end in B/C/D. **NO numerics/Python.**
**Spanish [translated to English].** Absolute candor. A false victory is worse than a failure.

**Prerequisites read from source this session:** Doc 162 (Phase 52: RH-free arithmetic e-invariant,
but ζ re-enters in the *fundamental class of the carrier* [C_Φ]=Σ_ρ δ_{γ_ρ}; trifurcation of
D156: (i) Fredholmness, (ii) orientation, (iii) escape; Phase 51 touched (ii), Phase 52 touched (i)).
Doc 163 (destructor: a secondary = an integral of a filling of the primary; "what is the filling and
what is it integrated with?"). B3.1 (universal template of Kreĭn ‖K‖≤1; Connes–Consani: ABSORPTION
spectrum over the Sonin space, semilocal formula). Phase 26 memory (κ=2m=neg.ind(H_C) in Pontryagin
(𝒦,Q); RH ⟺ H_C self-adjoint). Phase 33 memory (DBN: Λ=inf{t:T_λ(t)=0}; heat flow). Phase 38/45
memory (P_n = Meixner–Pollaczek, measure dm_∞=|Γ(1/4+is/2)|²ds; moment criterion). Phase 49–51
memory (the canonical metric carries ζ via the Bost–Connes partition; the wall is the inertia
signature, RH-free is the pure homotopy but not the arrow).

---

## 0. Executive summary and verdict stated in advance

> **VERDICT: OUTCOME B with a new fragment of D.** The Stone import does NOT give (A): there is no
> structural unitary evolution whose generator has spectrum {γ} and whose unitarity is RH-free. The
> reason is precise and constitutes the contribution of the document: **unitarity IS the Weil metric
> in disguise, but via a mechanism the program had not yet named with this clarity — the "inverted
> Stone theorem".** In QM one has the Hilbert space (the metric) *given a priori* by physics
> (probability = ‖ψ‖²), and from unitarity one deduces a real spectrum. In RH the direction is
> INVERTED: there is no metric given a priori; what is given is the dynamics (the scaling flow / the
> functional equation) and the spectral datum {γ}. For Stone to apply one must EXHIBIT the Hilbert
> space with respect to which U(t) is unitary — and exhibiting it *is* constructing the inner product
> that makes the γ real, which is exactly the Weil form Q (the metric that carries ζ, Phase 51).
> **The functional symmetry s↔1−s does give an RH-free unitary involution (Prop. 164.6) — but it is a
> unitarity in the WRONG parameter: it conjugates the spectrum (γ↦−γ̄ on the off-line divisor), it
> does not make it real. The available structural unitarity (the functional one) is not the one Stone
> needs (that of the scaling flow), and the one Stone needs is not structural.** That is the node, and
> it is *distinct* from Phase 52's: Phase 52 located ζ in the fundamental class of the carrier; this
> document locates it in **the choice of inner product that realizes the unitarity of the scaling
> flow**, and proves that the only RH-free symmetry at hand (the functional one) acts in the direction
> of conjugation (γ↦γ̄), not in that of evolution (γ real). The new fragment of D: the **discrepancy
> between the two one-parameter groups** —dilation (scale, Connes) versus translation
> (Fourier/wave)— is itself a nameable obstruction and is not Phase 52's duality.

**The three labeled results (previewed):**

1. **[PROPOSITION 164.4 — the inverted Stone theorem].** In QM the metric (‖ψ‖²) is physical input
   and Stone deduces spectrum⊂ℝ. In the arithmetic problem the metric is NOT input; the datum is the
   scaling dynamics θ_λ and the candidate spectrum {γ}. Exhibiting the Hilbert space that makes U(t)
   unitary is logically equivalent to exhibiting the inner product that makes {γ} real — and that
   inner product, over the adele class space, is the Weil form Q, which carries ζ. RH-free unitarity
   of the scaling flow would imply RH directly with no new content: it is the metric in disguise.
   (Proved as a logical implication; uses the κ=neg.ind(Q) dictionary of Phase 26.)

2. **[PROPOSITION 164.6 — the functional involution is RH-free unitary, but conjugates rather than
   evolves].** The functional equation ξ(s)=ξ(1−s) induces an involution J (s↦1−s) which is unitary
   with respect to the *ζ-free natural* inner product (that of L² of the critical line) and RH-free.
   BUT J is a charge conjugation (γ↦γ̄ on the off-line divisor, swaps ρ↔1−ρ̄), not the generator of the
   evolution that would make the γ real. Stone needs a group U(t)=e^{itH} with H the *scale
   generator*; the symmetry we have for free is the *reflection*, which lives in the wrong group
   (ℤ/2 ⊄ ℝ-flow). The available structural unitarity is not the one Stone consumes. (Proved: J²=1,
   J unitary without the ζ-metric; the proof that it is not e^{itH} for the scale H is by spectral
   incompatibility, §3.)

3. **[PROPOSITION 164.8 — form self-adjointness fails because the "potential" is the zero count].**
   For the natural candidate for a form-self-adjoint operator with spectrum {γ} (a regularized
   Berry–Keating-type −d²/dx² + V, or Connes's H_C), the condition "real V / manifestly symmetric
   form" is not satisfied *by the form*: the boundary conditions / the term that fixes exact {γ}
   encode ζ (essential self-adjointness of xp fails — Berry–Keating; the von Neumann deficiency index
   (n₊,n₋) that must be equalized is the datum that enumerates the zeros). There is no manifestly
   RH-free self-adjoint form. It reproduces and *localizes* the Berry–Keating wall: the stopping point
   is the equality of the deficiency indices, and that is ζ. (The xp / essential self-adjointness case
   is proved; the H_C case reduces to Phase 26.)

**Where ζ re-enters (one sentence):** in **the choice of Hilbert space that makes the scale flow
unitary** —which is the Weil form Q (Phase 51, a metric carrying a ζ-partition)— because the only
available RH-free unitary symmetry (the functional equation) acts as conjugation γ↦γ̄, not as the
evolution γ∈ℝ that Stone needs. **Inverted Stone theorem:** in QM the metric is given and the real
spectrum is deduced; here the real spectrum IS the metric yet to be deduced.

---

## 1. The precise QM↔RH dictionary

I fix the dictionary with the rigor the mandate demands, marking in each row whether the right-hand
object is RH-free or carries ζ. This is what the guard will audit afterward.

| QM (known, simple) | RH (the object X sought) | Status |
|---|---|---|
| Hilbert space ℋ, ‖ψ‖² = probability | 𝒦 = L²(C_ℚ) (adele classes, Connes) or L²(ℝ,dm_∞), dm_∞=\|Γ(1/4+is/2)\|²ds (CCM)? | **the inner product is the node** |
| Position x | Prime side: distribution over {log p} (logarithmic scale) | "known" datum |
| Momentum p | Zero side: distribution over {γ_ρ} | datum to be determined |
| Fourier transform ⟨x\|p⟩=e^{ixp} | **Weil's explicit formula** Σ_ρ ĥ(γ_ρ) = ĥ(±½i) − Σ_p Σ_k (log p)p^{−k/2}h(k log p)+arch. | the "change of basis" |
| Wave function ψ (object prior to the two bases) | **The object X** = a vector/state in 𝒦 whose two Fourier representations are primes and zeros | the sought Grail |
| Hamiltonian H, generator of e^{itH} | Generator of dilation/scale (Connes's H_C; Berry–Keating's xp) | self-adjoint ⟺ RH |
| Unitary evolution U(t)=e^{itH} | Scale flow θ_λ: ξ(v)↦ξ(λ^{−1}v), λ=e^t | **unitarity = the test** |
| "Energy" conserved by U(t) | the quantity whose conservation gives unitarity: here, the *Weil norm* | **= ζ (Phase 51)** |
| Spectrum(H) ⊂ ℝ (Stone) | {γ_ρ} ⊂ ℝ, i.e. Re ρ = ½ | **= RH** |
| Reality of the spectrum = unitarity (not metric) | RH = structural unitarity (the mandate's bet) | **to be decided here** |

**Comment on "ψ = object X".** The guiding analogy is correct and deep: wave-particle duality was
not resolved by choosing a side, but by exhibiting ψ with its two Fourier representations
(position/momentum) as bases of the same space. The arithmetic analogue exists and the program has
it partially: **Connes's scale flow on L²(C_ℚ)** is exactly a Fourier (Mellin) duality between scale
(∼ primes, via the adelic action) and frequency (∼ zeros, via the spectrum of the scale generator).
The explicit formula IS the Fourier–Mellin change of basis. Up to this point the analogy is
*literal*, not metaphorical. The problem —which I isolate in §2–§3— is not the absence of object X
(it exists: it is the adele class space with its scale flow), but **what is the conserved "energy"
that gives unitarity**, because that is where the dictionary breaks down.

**[BRIDGE 164-A].** The dictionary is honest and almost entirely RH-free EXCEPT for two cells, both
the same one: "conserved energy" and "inner product of ℋ". In QM those two cells come free from
physics (probability). In RH they are exactly what is missing, and the guard (§2) shows they are ζ.

---

## 2. Importing Stone and the candidate unitary evolution

### 2.1 Stone's theorem, exactly (Stone 1932; Reed–Simon I, Thm VIII.7–VIII.8)

**[Reminder — Stone's theorem].** Let ℋ be a Hilbert space. There is a bijection between:
(a) strongly continuous one-parameter groups of unitary operators {U(t)}_{t∈ℝ}, U(t+s)=U(t)U(s),
U(0)=1; and (b) self-adjoint operators H (generally unbounded, densely defined), via
U(t)=e^{itH}, where H = −i d/dt U(t)|_{t=0} on its natural domain. Immediate corollary:
**H self-adjoint ⟹ spec(H) ⊂ ℝ.** Ref.: M.H. Stone, "On one-parameter unitary groups in Hilbert
space", *Ann. of Math.* 33 (1932) 643–648; M. Reed, B. Simon, *Methods of Modern Mathematical
Physics I: Functional Analysis*, Academic Press 1980, Thm VIII.7 (Stone) and VIII.8.

**The physical point the mandate wants to import (correct).** In QM the reality of the spectrum is
NOT verified by choosing a metric: it follows from U(t) preserving ‖ψ‖² (conservation of probability
= unitarity), and ‖ψ‖² is physical input. The reality of the spectrum is a consequence of a
**conservation law**, not of an inner product imposed a posteriori. Beautiful. The question is
whether this can be transplanted.

### 2.2 [CONSTRUCTION] The candidate one-parameter group: the scale flow

There is ONE natural choice, not several, and it is best to commit to it so the guard has something
concrete to bite into.

**[CONSTRUCTION — U(t) = scale flow].** On ℋ = L²(ℝ₊*, d*λ) (the archimedean, even,
Connes–Consani version; B3.1 §2) or on L²(C_ℚ) (adele classes), define
U(t) ξ(v) = ξ(e^{−t} v), t ∈ ℝ.
It is a one-parameter group (composition of dilations). Its formal generator is
H = −i (v d/dv + ½) = −i d/d(log v) − i/2,
i.e., in the logarithmic coordinate u = log v, H = −i d/du − i/2 (a shifted translation/momentum
operator). In the Mellin representation (the Fourier transform of this flow), the spectrum of H is
the frequency line; the arithmetic spectral datum {γ_ρ} appears as the frequencies where
ζ(½+iγ)=0, via the explicit formula read as a trace formula of the flow (the "Connes distribution").
This is exactly the Connes 1999 and Berry–Keating setup (H ∼ xp in suitable coordinates: u d/du is
xp after x=u).

**The conserved "energy".** For U(t) to be unitary on ℋ with its d*λ, I need d*λ to be invariant
under dilation — and it is: d*λ = dλ/λ is the Haar measure of ℝ₊*. Then U(t) is unitary and H
self-adjoint on L²(ℝ₊*,d*λ) **trivially**, and its spectrum is the whole real line (it is the
momentum operator in u=log λ). **But its spectrum is the WHOLE line, not {γ_ρ}.** Here is the first
problem, which anticipates everything: the easy unitarity (Haar measure) gives the wrong operator
(continuous spectrum = ℝ, not the zeros). To get {γ_ρ} as spectrum one must *trim* the space
(boundary conditions, Sonin projection, absorption spectrum) — and that is where the easy unitarity
dies.

### 2.3 [BRIDGE 164-B] Three incarnations of the same flow, and where each one places {γ}

The program already has three versions of this flow; I align them so as not to reinvent:

1. **Berry–Keating's xp** (Berry–Keating, "H=xp and the Riemann zeros", in *Supersymmetry and Trace
   Formulae*, ed. Lerner et al., Kluwer 1999, pp. 355–367; and Berry–Keating, "The Riemann zeros and
   eigenvalue asymptotics", *SIAM Review* 41 (1999) 236–266). H=xp = ½(xp+px) is symmetric but **not
   essentially self-adjoint** on ℝ₊; it gives the AVERAGE density of zeros (the Riemann–von Mangoldt
   count N(T)∼(T/2π)log(T/2πe)) via the semiclassical Weyl rule, but NOT the exact spectrum. The
   boundary conditions / regularization (Sierra, Connes) that would fix the exact {γ_ρ} encode ζ.

2. **Connes 1999** (A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann
   zeta function", *Selecta Math. (N.S.)* 5 (1999) 29–106). The scale flow on L²(C_ℚ)/(idele class
   group). The zeros appear as **ABSORPTION** spectrum (gaps in the continuous spectrum of the flow,
   not emission eigenvalues). The trace formula is semilocal and the **positivity of the Weil
   trace ⟺ RH** is what remains open.

3. **CCM of the program** (Phase 29–45). Measure dm_∞=|Γ(1/4+is/2)|²ds; Meixner–Pollaczek polynomials
   P_n^(λ)(s;φ) as eigenfunctions of a QM-type operator (a Jacobi / creation-annihilation operator in
   that measure). Here the scale flow is concretely represented and the question of self-adjointness
   becomes a moment problem (Phase 38: RH ⟺ Δ_n constant).

**All three are the SAME scale flow in different realizations.** And all three place {γ} not as the
emission spectrum of a manifestly self-adjoint operator, but via a trim (boundary / absorption /
measure) which is where ζ enters. This is NOT a coincidence; §3 proves it.

---

## 3. THE UNITARITY TEST (the guard, UP FRONT)

I apply the guard mercilessly, as the mandate requires. **Unitary = preserves an inner product.**
Decisive question: *is the unitarity of U(t) established WITHOUT choosing the inner product that
carries ζ?*

### 3.1 [PROPOSITION 164.4 — the inverted Stone theorem]

**Statement.** Consider the scale flow U(t) (§2.2) as a candidate to have a generator H with
spectrum {γ_ρ}. Then:

(i) Under the Haar measure d*λ, U(t) is unitary *for free and RH-free*, but spec(H)=ℝ (continuous) —
the wrong operator: it does not see the zeros.

(ii) For spec(H)={γ_ρ} (the zeros as real eigenvalues/emission spectrum), ℋ must be restricted to a
subspace ℋ_{γ} (boundary conditions / projection). U(t) is unitary on ℋ_{γ} ⟺ ℋ_{γ} is U(t)-invariant
with the restricted inner product. **Exhibiting that ℋ_{γ} and certifying unitarity on it is
logically equivalent to exhibiting the inner product with respect to which the {γ_ρ} are real, which
is the Weil form Q (Phase 26: RH ⟺ Q≥0 ⟺ H_C self-adjoint), the metric that carries ζ (Phase 51).**

(iii) Therefore: an RH-free proof that U(t) is unitary on ℋ_{γ} would be an RH-free proof of RH with
no new content. **Unitarity in the correct space IS the Weil metric in disguise.**

**Proof.**
(i) U(t)ξ(v)=ξ(e^{−t}v); ∫|ξ(e^{−t}v)|² dλ/λ = ∫|ξ(w)|² dw/w (change w=e^{−t}v, dw/w=dλ/λ Haar
invariant) = ‖ξ‖². Hence U(t) is unitary, without using ζ. H=−i d/du−i/2 (u=log v) is the shifted
momentum, self-adjoint on L²(ℝ,du) by standard Fourier theory (Reed–Simon I, VIII); its spectrum is
ℝ. There are no zeros anywhere: this H "sees" only the group structure of ℝ₊*, which is RH-free and
for that reason *blind to ζ* — exactly the dynamical no-go N5 of Phase 8 (the flow is only
arithmetic-blind). ∎(i)

(ii) The spectrum of a self-adjoint operator is automatically real; conversely, given the set
{γ_ρ}⊂ℂ we want as spectrum, "the γ_ρ are real" is NOT a theorem about H but RH itself. The only way
for Stone to *force* γ_ρ∈ℝ is for H to be self-adjoint on some ℋ_{γ}. But H self-adjoint presupposes
an inner product ⟨·,·⟩_{ℋ_γ} with respect to which H=H*. Constructing that inner product on the space
of test functions of the scale flow, such that H_C (the Connes generator) is symmetric and the
eigenvectors associated with {γ_ρ} are orthonormal with positive norm, is *exactly* constructing the
Weil form Q with Q≥0. This is the content of Phase 26 (κ=2m=neg.ind(Q); RH ⟺ Q≥0 on the Pontryagin
space (𝒦,Q) ⟺ H_C self-adjoint, not merely Q-symmetric). And by Phase 51 (D161) every canonical
metric on the adele class space has a ζ partition function (Bost–Connes): the inner product that
makes Q positive *is* ζ-carrying. ∎(ii)

(iii) Immediate from (ii): "U(t) unitary on ℋ_γ" = "Q≥0" = "H_C self-adjoint" = "spec(H_C)⊂ℝ" = RH.
No extra content. ∎

**Interpretation (the conceptual contribution).** In QM the logical order is:
**[physical metric given] ⟹ [unitarity] ⟹ [real spectrum (Stone)].**
The metric (‖ψ‖²) is an AXIOM of the theory (Born's rule), not a theorem. Stone converts unitarity
into spectral reality *for free* because the metric was already in place. In RH the order is
**INVERTED**: there is no axiomatic metric; the given datum is the flow (RH-free, but blind to ζ by
(i)) and the set {γ_ρ}. What in QM is a datum (the metric) is here exactly the unknown, and "real
spectrum" is not Stone's conclusion but the disguised starting hypothesis. **Stone does not help
because it imports the conclusion, not the hypothesis: we would need to import Born's rule, and the
arithmetic Born rule is Weil positivity = ζ.** I call this the *inverted Stone theorem*. It is a new
mode of failure relative to Phase 52 (which located ζ in the fundamental class of the carrier): here
ζ is in *the metric axiom that QM gets for free and arithmetic must prove*.

### 3.2 What if unitarity came from a SYMMETRY instead of a metric? — the functional equation

This is exactly the move the mandate asks for (points 2–3): that U(t) be unitary via an **RH-free
structural symmetry** (the functional equation s↔1−s) instead of a chosen metric. I examine it and
carefully kill it, because it is the best hope for (A).

### 3.3 [PROPOSITION 164.6 — the functional involution is unitary and RH-free, but is in the wrong group]

**Statement.** The functional equation ξ(s)=ξ(1−s) (ξ = the completed, entire xi function, an exact
symmetry with no hypothesis) induces an involution J: s↦1−s on the s-plane, equivalently a
reflection on the critical axis. Then:

(a) J is **unitary with respect to the natural ζ-free inner product** (that of L² of the s-axis with
Lebesgue measure, or that of the de Branges realization where the functional equation is the
symmetry rule), and J²=1. It is RH-free: the functional equation is an unconditional theorem
(Riemann 1859; via the theta representation / the symmetry of θ's Mellin integral). **IT PASSES the
guard: unitarity without the ζ-metric.**

(b) BUT J is a **conjugation/reflection** (an order-2 element, J∈ℤ/2), NOT the generator of an ℝ
flow. On the off-line divisor, J swaps ρ↔1−ρ; composed with complex conjugation c (ρ↦ρ̄), it
generates the Klein group V=⟨J,c⟩ whose free orbits are the quadruples {ρ,1−ρ,ρ̄,1−ρ̄} (exactly the m
of Phase 52). J's action on the candidate spectrum {γ} of the scale generator is **γ↦−γ**
(reflection of the imaginary axis), not "γ real". J commutes with H_C but is NOT e^{itH_C} for any t
(it is an involution, not a flow; its spectrum is {±1}, that of H_C is {γ}).

(c) Conclusion: the RH-free unitary symmetry we have (J, the functional equation) lives in the
REFLECTION group ℤ/2, not the EVOLUTION group ℝ that Stone consumes. Stone needs unitarity of
{e^{itH_C}}_{t∈ℝ} (scale flow); the functional equation gives unitarity of {1,J} (reflection). **The
available structural unitarity is not the one Stone needs.** And the reality of {γ} (RH) is NOT
J-invariance (which is unconditional: J acts on off-line and on-line alike, it does not distinguish
m); it is the self-adjointness of H_C, which J does not give.

**Proof.**
(a) The functional equation is ξ(s)=ξ(1−s), ξ entire, proved unconditionally (the classical proof via
the modular transformation θ(1/t)=√t θ(t) and the Mellin integral; Titchmarsh, *The Theory of the
Riemann Zeta-Function*, 2nd ed. Oxford 1986, §2.6). On the critical line s=½+iτ, J: τ↦−τ is the
reflection, manifestly unitary in L²(ℝ,dτ) (it is f(τ)↦f(−τ), an isometry) and J²=1. No ζ, no special
metric: IT PASSES. ∎(a)

(b) J swaps the half-plane Re s>½ with Re s<½; on an off-line zero ρ=β+iγ with β≠½, Jρ=1−ρ is the
functional-conjugate zero; together with c: ρ↦ρ̄ one obtains the Klein orbit. The spectrum of J as an
operator is {+1,−1} (involution): even/odd eigenspaces under the reflection. The spectrum of H_C
(scale generator) is {γ_ρ} (continuous + absorption, Connes). An operator with spectrum {±1} cannot
be e^{itH} with spec(H)={γ_ρ} except in trivial cases (it would require e^{itγ_ρ}∈{±1} ∀ρ, impossible
for a dense {γ_ρ}). Hence J≠e^{itH_C}. And J commutes with H_C (both respect the functional equation)
but this only says that H_C is J-equivariant, not self-adjoint. ∎(b)

(c) Stone is a bijection {unitary ℝ-flows}↔{self-adjoint operators}. J is not an ℝ-flow (it is ℤ/2),
so Stone does not consume it: it does not produce "spec(H_C)⊂ℝ" from J. The reality of {γ_ρ} (RH) is
a property of H_C (self-adjointness), and J —unconditional, blind to m by the even/odd symmetry— does
not imply it: J is satisfied whether the zeros are on the line or in off-line quadruples (the
quadruples are J,c-symmetric by construction). **J does not see m.** (This recovers Phase 52 Prop.
162.9: the functional equation forces hyperbolicity/blindness; here: the functional equation is
unitary but blind to m.) ∎

**Interpretation (the heart of verdict B).** There are TWO one-parameter groups/symmetries in play
and they do NOT coincide:
- The **scale flow** (dilation, e^{itH_C}, group ℝ): its unitarity would give RH by Stone, but its
  unitarity in the correct space = Weil form = ζ (Prop. 164.4). Structural but ζ-carrying.
- The **functional reflection** (J, group ℤ/2): RH-free unitary, structural, but in the wrong group
  and blind to m (Prop. 164.6). RH-free but powerless.

The hope for (A) was that the second would give the unitarity of the first. It does NOT: it acts in
the direction of conjugation (γ↦−γ, axis reflection), not in the direction of evolution (γ∈ℝ). **The
unitarity escapes the metric only in the useless parameter.**

---

## 4. Where Berry–Keating and Connes stop, and whether Stone touches a new point

### 4.1 Berry–Keating: it stops at essential self-adjointness / boundary conditions

**What they achieve** (Berry–Keating 1999, *SIAM Rev.* 41): H=xp with the semiclassical
regularization reproduces the average density of zeros N(T)∼(T/2π)log(T/2πe)−T/2π+… via Weyl's
formula (phase-space area under the hyperbolas xp=E with cutoffs ℓ_x,ℓ_p). The number of levels up to
E comes out of the area (2π)^{−1}∮ = correct to first order.

**Where they stop (precisely).** xp = ½(xp+px) on L²(ℝ₊) is symmetric but has **deficiency indices
(1,1)** (it is not essentially self-adjoint): the equation x f' + ½f = ±i f has an L² solution for
each sign, f_±(x)=x^{−1/2±i}, both in L²(0,1] but the behavior at 0/∞ leaves a defect. There is
therefore a U(1) family of self-adjoint extensions (parametrized by a boundary phase θ∈[0,2π)).
**Each extension gives a distinct discrete spectrum; NONE gives {γ_ρ} except for a choice of boundary
condition that encodes ζ.** The "boundary potential" that would select the correct extension is the
phase of ζ on the critical line (arg ζ(½+it)) — exactly the datum that enumerates the zeros. Sierra
and collaborators (G. Sierra, "The Riemann zeros as spectrum and the Riemann hypothesis", *Symmetry*
11 (2019) 494; Sierra–Townsend; Berry–Keating "A compact hamiltonian with the same asymptotic mean
spectral density as the Riemann zeros", *J. Phys. A* 44 (2011) 285203) have built modified
xp-Hamiltonians (xp in one region, with reflection) that give the *exact* average density even with
corrections, but the fluctuations (the exact γ) require a semiclassical term = Σ_p (the sum over
primes) — i.e., the ζ datum enters as the "periodic orbits" of the system. **The Berry–Keating wall =
the choice of self-adjoint extension / the periodic orbits = ζ.**

### 4.2 Connes: it stops at the absorption spectrum and the positivity of the trace

**What they achieve** (Connes 1999, *Selecta* 5). Over the adele class space C_ℚ with the scale flow,
the zeros appear as **absorption** spectrum (gaps in the continuous spectrum), not as emission. The
trace formula is semilocal (a sum over places), and the Weil identity holds. **The wall: the
positivity of the Weil distribution (Weil trace ≥0) ⟺ RH** — Connes reduces RH to that positivity,
which remains open. Connes–Consani (B3.1; 2006, *2006.13771*) refine this: they realize the
archimedean part as a trace over the Sonin space (manifest square TT*≥0) plus a residual ε(ρ), and
RH ⟺ the residual keeps its sign. The Sonin space is **zero-independent** (defined by the phase
cutoff, prolate functions), but the residual ε is *not*.

**Where they stop (precisely).** The absorption spectrum is NOT the spectrum of a self-adjoint
emission operator: it is the absence of something in a continuum. Stone applies to the flow's
generator (self-adjoint, continuous spectrum ℝ), not to the absorption structure. The positivity of
the Weil trace = the Weil metric ≥0 = form Q≥0 (Phase 26). **The Connes wall = positivity of the
trace = Weil form Q≥0 = exactly Prop. 164.4(ii).**

### 4.3 Does Stone touch a NEW point, or does it reproduce its wall?

**Answer: it reproduces the Connes wall (positivity = metric = Q), but it NAMES it with a new
structure (inverted Stone) and cleanly discards the functional-symmetry route.** Detail:

- Stone does *not* touch a point that Berry–Keating/Connes did not touch. The positivity of the Weil
  trace (Connes) IS "U(t) unitary on the correct space" (Prop. 164.4(iii)). The deficiency-index
  defect (Berry–Keating) IS "which self-adjoint extension = which inner product" (Prop. 164.4(ii)).
  They are the same thing. Stone unifies them: both are "the missing metric".
- What is NEW in this document (not from Stone, but from its honest import):
  1. **The inverted-Stone diagnosis** (Prop. 164.4): it makes explicit WHY Stone does not transfer
     —in QM the metric is an axiom (Born), in RH it is a theorem (Weil positivity). This reorders the
     Connes wall as "the arithmetic Born axiom is missing", which is more precise than "positivity is
     missing".
  2. **The discarding of the functional symmetry** (Prop. 164.6): the best candidate for "RH-free
     structural unitarity" (the functional equation) is proved to be in the wrong group (ℤ/2
     reflection, not ℝ flow) and blind to m. This closes a route the mandate posed as open, without
     leaving it in [GAP].
- Stone does **NOT** reproduce the Phase 52 wall (the fundamental class of the carrier): it is a
  distinct node. Phase 52: ζ in the homotopy datum [C_Φ]=Σδ_{γ_ρ}. Phase 53: ζ in the inner product
  that makes the flow unitary. Both are facets of the D156 trifurcation (i)/(ii), but the
  inverted-Stone formulation is genuinely another lens.

---

## 5. Form self-adjointness? The decisive point

The mandate asks the right question: in QM −Δ+V is self-adjoint *by its form* (V real, −Δ semi-
bounded; Reed–Simon II, Thm X.28, Kato–Rellich), and the real spectrum follows automatically without
checking anything. Is there an arithmetic form-self-adjoint operator with spectrum {γ}?

### 5.1 [PROPOSITION 164.8 — there is no manifestly RH-free self-adjoint form; the "potential" is ζ]

**Statement.** For the natural candidates for "an operator with spectrum {γ_ρ} self-adjoint by its
form":

(a) **Berry–Keating's regularized −d²/dx²+V or xp:** it is not self-adjoint by its form. xp has
deficiency indices (1,1) (§4.1); the operator is not semi-bounded (its classical spectrum is the
whole line, the hyperbolas xp=E cover E∈ℝ), so the Kato–Rellich/closed-semi-bounded-form machinery
**does not apply**. The "potential" that would produce exact {γ_ρ} is the boundary condition/periodic
orbits = ζ.

(b) **Connes's H_C (scale generator):** it is self-adjoint on L²(Haar) but with spectrum ℝ (blind to
ζ, Prop. 164.4(i)); restricted to the space that gives {γ_ρ} (Pontryagin (𝒦,Q)), it is Q-symmetric
but self-adjoint ⟺ Q≥0 ⟺ RH (Phase 26). The "real potential" here is the positivity of Q = ζ.

(c) **CCM / Meixner–Pollaczek:** the Jacobi operator whose eigenfunctions are the P_n^(λ) IS
self-adjoint on L²(dm_∞), dm_∞=|Γ(1/4+is/2)|²ds, *by its form* (Jacobi operator with real
coefficients, essentially self-adjoint if the moment problem is determined; Phase 38: RH ⟺ Δ_n
constant). But its spectrum is that of the P_n (the Meixner–Pollaczek measure = spectrum of an
oscillator-type creation-annihilation operator), **NOT {γ_ρ}** — the γ_ρ enter only when *coupling*
this basis to ζ via the Δ_n-constant condition, which is ζ. The form is RH-free self-adjoint, but its
spectrum is not that of the zeros; turning it into that of the zeros requires ζ.

**Conjunction.** In all three cases: either the form is RH-free self-adjoint but its spectrum is NOT
{γ} (b: H_C on Haar; c: Meixner–Pollaczek), or the spectrum would be {γ} but the form is not
self-adjoint by construction and the term that would close it is ζ (a: Berry–Keating; b: H_C on 𝒦).
**The desired combination (manifestly RH-free self-adjoint form WITH spectrum {γ}) does not exist.**
The "potential V" that produces {γ} is real ⟺ RH: ζ is in the potential. It is the same wall.

**Proof.**
(a) Deficiency indices (1,1) of xp: §4.1, the deficiency equation (x∂_x+½∓i)f=0 gives
f=x^{−1/2±i}∈L²(0,1] but symmetry requires equating two extensions; the operator is not semi-bounded
(classical spectrum ℝ), so the semi-bounded-form criteria (Reed–Simon II X.23, KLMN) do not apply:
there is no closed, lower-semi-bounded form whose associated operator is xp. Self-adjointness, if
achieved, is by choice of extension, not by the form. ∎(a)

(b) H_C on L²(Haar): self-adjoint, spectrum ℝ (Prop. 164.4(i)). On (𝒦,Q): Phase 26, H_C is
Q-symmetric; self-adjoint in the Pontryagin sense ⟺ neg.ind(Q)=0 ⟺ κ=0 ⟺ m=0 ⟺ RH. "Reality of the
potential" = positivity of Q. ∎(b)

(c) The Jacobi operator J_MP with real coefficients a_n,b_n (those of the Meixner–Pollaczek
recurrence relation) is essentially self-adjoint on the polynomials dense in L²(dm_∞) iff the moment
problem of dm_∞ is determined (Akhiezer, *The Classical Moment Problem*, Oliver & Boyd 1965, chap.
1–2; dm_∞ is determined, exponential |Γ|² decay). Its spectrum = support of dm_∞ = ℝ (the P_n are
orthogonal over the whole line). That is NOT {γ_ρ}: it is the spectrum of the Meixner–Pollaczek
oscillator (continuous absolutely continuous spectrum), not the discrete zeros. The connection with ζ
is the moment formula / the condition Δ_n=const (Phase 38), which is where ζ enters. The
self-adjoint form is RH-free but "its V" is not that of the zeros. ∎(c) ∎

**Interpretation.** This is the mandate's decisive test and its result is clean: **form
self-adjointness DOES exist (Meixner–Pollaczek, H_C on Haar) but with the wrong spectrum; the
spectrum {γ} CAN be requested but then the form is not self-adjoint by itself.** The two desired
properties are mutually exclusive without ζ. The real potential ⟺ RH. There is no Grail.

---

## 6. Honest verdict (A/B/C/D) and the central GAP

**VERDICT: B (unitarity/self-adjointness is the Weil metric in disguise, localized node) with a new
fragment of D (the discrepancy between the two one-parameter groups).** It is NOT A: I did not
construct a structural unitary evolution with spectrum {γ} and RH-free unitarity, and I was rightly
suspicious of A. It is NOT disguised A.

**What WAS genuinely established:**
- The precise QM↔RH dictionary (§1), with the only two non-RH-free cells isolated: "conserved
  energy" and "inner product", which are the same thing and are ζ.
- **The inverted Stone theorem** (Prop. 164.4): in QM the metric is an axiom (Born) and Stone gives
  the real spectrum for free; in RH the metric is a theorem (Weil positivity), Stone imports the
  conclusion not the hypothesis, and "U(t) unitary in the correct space" = Q≥0 = RH. A new failure
  mode relative to Phase 52.
- **The discarding of the functional symmetry** (Prop. 164.6): the best candidate for RH-free
  structural unitarity (the functional equation J) IS unitary and RH-free, BUT it lives in the
  reflection group ℤ/2, not the ℝ flow that Stone consumes, and it is blind to m (γ↦−γ, conjugation,
  not γ∈ℝ, evolution). Route closed, not left as a GAP.
- **No RH-free form self-adjointness with spectrum {γ}** (Prop. 164.8): there exists a self-adjoint
  form (Meixner–Pollaczek, H_C/Haar) with the wrong spectrum, or spectrum {γ} with a form that is not
  self-adjoint by itself (Berry–Keating, H_C/𝒦); the two do not coexist without ζ. The real potential
  ⟺ RH.

**Where ζ re-enters (precise, and why it is NEW).** NOT in the fundamental class of the carrier
(Phase 52), NOT in the modular orientation (Phase 51). It re-enters in **the inner product that makes
the scale flow unitary** = the Weil form Q = the "arithmetic Born rule". The new mechanism: Stone's
logical direction is INVERTED relative to QM. In QM the metric is the starting axiom; in RH it is the
arrival unknown. The only available RH-free unitary symmetry (the functional equation) is in the
wrong group.

**The central GAP / fragment of D (named and new).**

> **[GAP/WISH 164.D — the discrepancy between the two one-parameter groups].** The program has two
> unitary symmetries: **dilation** (scale flow, group ℝ, e^{itH_C}, generator with spectrum {γ} but
> unitarity=ζ) and the **functional reflection** (J, group ℤ/2, RH-free unitary but blind to m). The
> obstruction to (A) is that these two groups do NOT combine into a single one-parameter group whose
> unitarity is simultaneously structural (from J) and evolutionary (from H_C). In QM this does happen:
> parity reflection and time evolution are both unitary with respect to the SAME Born metric, and they
> commute, giving a larger group (ℝ⋊ℤ/2). The [GAP] is: **does there exist an RH-free metric with
> respect to which BOTH J AND the scale flow are unitary, so that J-invariance (RH-free) propagates
> to the reality of H_C's spectrum (RH)?** In QM the propagation is trivial (a single metric). Here, J
> is unitary with respect to the Lebesgue/de Branges metric (RH-free) and H_C is unitary with respect
> to the Weil metric Q (ζ); their being the SAME metric is exactly RH (Phase 26: Q≥0 = reality of
> {γ}). This GAP is distinct from the "Diophantine thread" (GAP-157.A) and from "duality" (Phase 52):
> it is the **incompatibility of the two natural metrics (reflection vs. evolution)**, and it is, I
> believe, a new formulation of the wall: *RH ⟺ the metric of the functional reflection = the metric
> of the scale evolution.* I have no proof that this reformulation is more tractable; I leave it as a
> [central GAP], honestly, because it could be circular (the equality of metrics IS Q≥0). But the
> *form* —"unifying two one-parameter groups in a common metric"— is a standard problem in
> mathematical physics (representations of the Galilei/Poincaré group: one metric, several
> generators) and it names the wall in representation-theory language, which the program had not used.

**Strategic synthesis (what is genuinely new).** The program believed it had isolated the wall in the
*inertia-reading metric* (Phase 51) and then in the *fundamental class of the carrier* (Phase 52).
This document shows that importing Stone —the QM tool that gives spectral reality for free— **does
not transfer, because it transfers the conclusion and not the hypothesis**: QM has the metric for
free (Born) and RH must prove it (Weil positivity). The functional symmetry, which seemed to be the
way out (unitarity by symmetry, not by metric), is unitary and RH-free but in the wrong group
(ℤ/2 reflection, not ℝ evolution) and blind to m. The wall is relocated with precision: **RH ⟺ the
metric that makes the functional reflection unitary coincides with the one that makes the scale
evolution unitary** (GAP 164.D). It is not A; it is B with a D-type GAP formulated in representation
theory, distinct from the program's previous GAPs. Unitarity does NOT escape the metric: in the
useful parameter (the scale flow) unitarity IS the Weil metric; in the RH-free parameter (the
functional equation) unitarity exists but does not touch m.

---

## 7. Appendix: label table (internal audit) and step-by-step unitarity test

### 7.1 Labels

| Label | Statement | Status |
|---|---|---|
| §1 QM↔RH dictionary | precise map, two non-RH-free cells | **established** (BRIDGE 164-A) |
| [CONSTRUCTION] U(t) scale flow (§2.2) | dilation group, generator H_C | defined; Haar spectrum = ℝ (blind), spectrum {γ} requires trimming |
| [PROP 164.4] inverted Stone | unitarity in the correct space = Q≥0 = RH | **proved** (logical implication via Phase 26/51) |
| [PROP 164.6] functional-equation unitary RH-free but wrong group | J∈ℤ/2 reflection, blind to m, ≠e^{itH_C} | **proved** (J²=1, incompatible spectra, blindness to m) |
| §4 Berry–Keating/Connes | stop at deficiency (1,1)/boundary and at trace positivity=Q | **localized** (with refs) |
| [PROP 164.8] no RH-free self-adjoint form with spectrum {γ} | form OK ⟹ spectrum≠{γ}; spectrum={γ} ⟹ form not self-adjoint without ζ | **proved** (xp deficiency; H_C; Meixner–Pollaczek moments) |
| [GAP/WISH 164.D] two one-parameter groups | RH ⟺ metric(reflection)=metric(evolution) | **central GAP, new, unproved; possible circularity declared** |

### 7.2 The unitarity test, step by step (the guard)

| Step | Does unitarity use the ζ-metric? | Verdict |
|---|---|---|
| U(t) on L²(Haar) (§2.2) | No (Haar is RH-free) | **PASSES but spectrum=ℝ, blind to ζ** |
| U(t) on ℋ_γ (spectrum={γ}) | Yes: the inner product = Weil form Q | **FAILS: ζ re-enters (Prop. 164.4)** |
| J = functional reflection (§3.3) | No (Lebesgue/de Branges, RH-free) | **PASSES but group ℤ/2, blind to m (Prop. 164.6)** |
| Meixner–Pollaczek Jacobi form (§5) | No (real coefficients, determined moments) | **PASSES but spectrum≠{γ} (Prop. 164.8c)** |
| xp / Berry–Keating with boundary giving {γ} | Yes: the boundary phase = arg ζ / orbits = primes | **FAILS: ζ at the boundary (§4.1, Prop. 164.8a)** |
| H_C on Pontryagin (𝒦,Q) | Yes: self-adjointness = Q≥0 = RH | **FAILS: ζ = positivity (Prop. 164.4b, Phase 26)** |

**Reading the table.** Everything that is RH-free unitary/self-adjoint has the wrong spectrum (ℝ or
that of the oscillator, not {γ}); everything that has spectrum {γ} needs the Weil metric = ζ for its
unitarity. The boundary is exact and without gaps: **there is not a single row that is simultaneously
RH-free AND of spectrum {γ} AND unitary.** That IS outcome B.

---

**References (real).**
- M.H. Stone, "On one-parameter unitary groups in Hilbert space", *Ann. of Math.* **33** (1932) 643–648.
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics I: Functional Analysis*, Academic Press
  1980 — Stone Thm VIII.7–VIII.8; *Vol. II: Fourier Analysis, Self-Adjointness*, 1975 — Thm X.1 (von
  Neumann, deficiency indices), X.23/KLMN (forms), X.28 (Kato–Rellich).
- M.V. Berry, J.P. Keating, "H=xp and the Riemann zeros", in *Supersymmetry and Trace Formulae: Chaos
  and Disorder*, ed. I.V. Lerner et al., Kluwer/Plenum 1999, pp. 355–367.
- M.V. Berry, J.P. Keating, "The Riemann zeros and eigenvalue asymptotics", *SIAM Review* **41** (1999)
  236–266.
- M.V. Berry, J.P. Keating, "A compact hamiltonian with the same asymptotic mean spectral density as
  the Riemann zeros", *J. Phys. A: Math. Theor.* **44** (2011) 285203.
- G. Sierra, "The Riemann zeros as spectrum and the Riemann hypothesis", *Symmetry* **11** (2019) 494.
- A. Connes, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function",
  *Selecta Math. (N.S.)* **5** (1999) 29–106.
- A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place", arXiv:2006.13771
  (2020) — Sonin space, manifest square, residual.
- J.-B. Bost, A. Connes, "Hecke algebras, type III factors and phase transitions with spontaneous
  symmetry breaking in number theory", *Selecta Math.* **1** (1995) 411–457 — partition = ζ.
- E.C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev. Heath-Brown), Oxford 1986 —
  functional equation §2.6.
- N.I. Akhiezer, *The Classical Moment Problem*, Oliver & Boyd 1965 — Jacobi operator, determinacy.
- [literature GAP]: there is no identification in the literature of "unitarity of the scale flow =
  Weil form" formulated as an inverted Stone theorem, nor the reformulation of RH as the equality of
  the reflection and evolution metrics (GAP 164.D). The references anchor the tools (Stone, von
  Neumann, Berry–Keating, Connes); the inverted-Stone bridge and GAP 164.D are new.
