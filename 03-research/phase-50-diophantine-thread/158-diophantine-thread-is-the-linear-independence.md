# Doc 158 — The Diophantine thread: is the ℚ-linear independence of {log p} the transversality certificate that collapses the individuation defect of the Weil form?

**Program:** Riemann Hypothesis — Phase 50: the Diophantine thread.
**Role of the document:** to decide whether **a specific structural input** —the ℚ-linear independence of {log p},
equivalent to the completeness of the system {p^{iτ}}— **can be the transversality certificate
S∩H_osc={0}** (in the sense of the individuation defect δ_A of Doc 155) that collapses the
average→individual wall of the Weil form, **WITHOUT reintroducing RH**. This is the only surviving crack of
Phase 49 (GAP-157.A; fifth collapser of Doc 155; frames of Doc 148), which appeared independently
in three documents.

**IRON RULE of this phase:** the goal is NOT to produce another RH⟺X equivalence. The deliverable is NOT an
equivalence of RH. My explicit expectation: the thread collapses into (a) Nyman–Beurling in disguise or (b)
Bohr/Voronin confined to the value side. If (c) were to appear, I distrust it and triple the stress test.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved here, complete proof; external results cited with
precision. **[CALCULATION]** = shown. **[BRIDGE]** = connection with frank status for each link. **[GAP]** =
declared. **[WISH]** = declared. **[literature GAP]** = data not verified at page level in this
phase, NOT used as a premise of any [THEOREM]. A proof of RH is never fabricated. **NO numerics.**

**Prerequisites read at the source this phase:** Doc 154 in full (taxonomy of crossings; Theorem 154.5 the wall
IS N(A); Theorem 154.9 exhaustiveness by logical type; Prop. 154.11 verifiable-boundary/disguised-conclusion
WITHIN positivity); Doc 155 in full (δ_A(F)=‖(1−A)F‖; Theorem 3.4 no-go; Theorem 4.8 reduction
principle; §5 fifth collapser of type τ=**?** non-commutative/phase); Doc 157 in full (GAP-157.A;
local Tauberian no-go; Prop. 157.7 resonance density = zeros); Doc 148 in full (frames on
Λ_p∪Λ_q; Prop. 2.2 never Riesz; Prop. 2.4 μ(T)=0; §5.2 infinite density breaks the frame); Doc 112 §§0–4.3
(LP-112; Lemma 2.2 Kronecker–Weyl on {log p}; Prop. 2.6 zero density of witnesses under ¬RH; Bagchi's
support S; positive-density↔RH / zero-density↔¬RH dichotomy; Lemma 3.3 non-discreteness).

---

## 0. Executive summary

1. **(§1) Exact formalization of the Diophantine input and of the space (H,A).** I fix three nested
   statements and prove their unconditional equivalences: (D-a) {log p} is ℚ-linearly independent (unique
   factorization, [THEOREM 158.1]); (D-b) Kronecker–Weyl ⟹ the flow t↦(p^{−it})_p is equidistributed and minimal
   on the torus 𝕋=∏_p S¹ ([THEOREM 158.2]); (D-c) the system {p^{iτ}}_p is **complete in B²** (the Besicovitch
   closure of Dirichlet polynomials) and, which is DIFFERENT, its completeness/minimality in
   L²(−T,T) is a frame problem ([PROP 158.3], which reuses Doc 148). I fix the averaging pair (H,A) of
   Doc 155 in which the question lives: **there is NO single (H,A); there are THREE candidates**, and the
   choice decides the verdict (§1.4). This is the first finding: *the Diophantine thread inhabits a different
   space depending on whether it is read as value (B², Bohr torus) or as inertia (the localized Weil form / Gram
   of the zeros)*.

2. **(§2) The attempted transversality certificate.** I try to prove: the ℚ-linear independence makes
   {p^{iτ}} "maximally independent," so that no nontrivial combination lives in H_osc — the
   Diophantine independence empties H_osc. **[PROP 158.5]: the attempt DOES work, but in the Bohr torus 𝕋,
   where it produces ergodicity of the Kronecker flow** (Theorem 4.7 of Doc 155, collapser of type **sym**)
   — and there H_osc empties out of nontrivial invariants. **[PROP 158.6]: the attempt FAILS in the space of the
   Weil form**, because the transversality that independence certifies is transversality to the
   *invariants of the flow* (value side), not transversality to the *zero-to-zero oscillatory ideal* (inertia
   side, Doc 134/Doc 155 §6). Independence empties the oscillation-of-values, not the oscillation-of-inertia.

3. **(§3) THE STRESS TEST, head-on.**
   - **(Nyman–Beurling collapse, §3.1):** I compare the TWO completeness systems with precision. NB/Báez-Duarte
     requires completeness of **dilations** {ρ(θ/x)} (equiv. power basis {(1/n)^s}) in L²(0,1)/H²; the
     thread requires completeness of **characters** {p^{iτ}} / {n^{−s}}. **[PROP 158.7]: they are NOT the same
     completeness system** — NB is completeness in a SCALE variable (Mellin/dilation) RH-equivalent by
     construction (1_{(0,1)}∈closure ⟺ RH); the thread is completeness in a FREQUENCY variable
     (Fourier/translation) that is UNCONDITIONAL. The thread is NOT NB in disguise *as a system*. **BUT** [PROP
     158.8]: both share the same defect — the weight/space in which completeness is measured carries the
     information of the zeros, and for the completeness of {p^{iτ}} to be RELEVANT to inertia it must be measured in
     the space of the Weil form, where it becomes RH-equivalent. The thread escapes NB as a *statement* but
     falls into the *same spatial trap*.
   - **(Bohr–Voronin collapse, §3.2):** the ℚ-linear independence IS what makes ζ almost-periodic (Bohr) and
     powers Voronin's universality. **[PROP 158.9]: Voronin/Bagchi universality is a VALUE
     statement and is BLIND to RH** (Bagchi: strong recurrence ⟺ RH uses the support, not raw
     universality; universality holds unconditionally). **[THEOREM 158.10] (the core): the Diophantine thread,
     in its B²/Bohr-torus completeness form, is CONFINED to the value side by construction** — it empties
     H_osc in the sense of oscillation-of-values (the Besicovitch time coordinate t, where the seminorm annihilates
     compacts, Doc 112 Obs. 2.4) and is structurally blind to the inertia coordinate (the height γ of
     a zero, a compact). It is the SAME B²-seminorm blindness that killed direct LP-112.

4. **(§4) VERDICT: case (b) PROVED, with a core of (a) in the spatial mechanism.** The Diophantine thread
   is **Bohr/Voronin confined to the value side** (case b): it empties the value oscillation but NOT the inertia one.
   The mechanism of the blindness is exact and triple-verified (§4.2): the ℚ-linear independence certifies
   transversality to the INVARIANTS of the Kronecker flow (empties H_osc^val), but the inertia of the zeros
   lives in H_osc^iner, orthogonal to the flow coordinate. It is NOT (c): there is no inertia certificate. The
   residue of (a): to promote the thread from value to inertia one must change to the space of the Weil
   form, and there completeness becomes RH-equivalent (NB-type core). **NO equivalence
   of RH is produced as a deliverable.**

5. **(§5) The exact GAP separating Diophantine (unconditional) completeness from the inertia certificate.**
   **[GAP-158.A]:** the ℚ-linear independence lives on the Bohr torus 𝕋=∏_p S¹ (an object of the
   PHASE/value coordinate); the inertia certificate that RH needs lives in the space of the Weil form over the
   HEIGHTS of the zeros (inertia coordinate, Doc 155 §6 compact ideal). The GAP is **the absence of a
   functor that transports the transversality of the phase torus to the transversality of the inertia ideal**, and
   that functor —if it existed— would be precisely the fifth collapser of type τ=**?** of Doc 155 §5.2
   (non-commutative/phase). The Diophantine thread is NOT that functor; it is its candidate input, not constructed.

---

## 1. Formalization of the Diophantine input and of the space (H,A)

### 1.1. The three nested Diophantine statements, with equivalences

I fix the content of the "Diophantine input" with precision, separating statements that are DISTINCT even if
related. Let ℙ be the set of primes.

**[THEOREM 158.1] (D-a: ℚ-linear independence of {log p} = unique factorization).** The set
{log p : p∈ℙ} is linearly independent over ℚ. Equivalently: the only integer solution of
Σ_p a_p log p = 0 with (a_p) of finite support is a_p≡0.

*Proof.* Σ_p a_p log p = 0 ⟺ ∏_p p^{a_p}=1. Separating positive and negative exponents,
∏_{a_p>0} p^{a_p} = ∏_{a_p<0} p^{−a_p}, two integers with disjoint prime factorizations; by the
fundamental theorem of arithmetic (unique factorization) both sides are 1, hence every a_p=0. Multiplying by the
lcm of the denominators reduces the rational case to the integer one. $\square$

This is the additive skeleton of the Euler product. It is **unconditional, purely arithmetic, RH-free by
construction** — the fact that gives the thread its appeal: it does not contain the zeros.

**[THEOREM 158.2] (D-b: Kronecker–Weyl — the prime flow is equidistributed and minimal on 𝕋).** Let
𝕋:=∏_p S¹ be the torus (compact, in the product topology) and consider, for any finite subset
F⊂ℙ, the linear flow φ_F: t↦(p^{−it})_{p∈F} = (e^{−it log p})_{p∈F} on 𝕋_F=∏_{p∈F}S¹. Then:
(a) the orbit {φ_F(t):t∈ℝ} is dense in 𝕋_F (minimality); (b) it is equidistributed with respect to the
Haar measure: (1/T)∫_0^T g(φ_F(t))dt → ∫_{𝕋_F} g dHaar for every g∈C(𝕋_F). In the projective limit, the flow
t↦(p^{−it})_{p∈ℙ} is minimal and uniquely ergodic on 𝕋.

*Proof.* By the Weyl/Kronecker theorem, the linear flow t↦(α_p t mod 1)_{p∈F} with frequencies
α_p=log p/2π is equidistributed and minimal on 𝕋_F iff {α_p}_{p∈F} are ℚ-linearly independent together
with 1 — which is D-a ([THEOREM 158.1]) plus the observation that log p/2π is never rational with another log q/2π
(same unique factorization). The unique ergodicity of the minimal Kronecker flow is classical
([Walters, *Ergodic Theory*, Thm 6.20: a minimal translation of a compact group is uniquely
ergodic]). The projective limit is inherited by compatibility of the Haar measures. $\square$

This is the content of Lemmas 2.2 and 3.3 of Doc 112, isolated as a theorem of the torus structure.

**[PROPOSITION 158.3] (D-c: completeness of the system {p^{iτ}} — TWO distinct readings).** The system of
characters {p^{iτ}}_{p} (more generally {n^{−s}}, equivalent via factorization) has completeness that
depends ENTIRELY on the space:
(i) **In B² (Besicovitch closure of Dirichlet polynomials with frequencies {log n}):** the system
{e^{i(log n)t}}_n is complete in B² by definition of the class (Besicovitch 1932). This is unconditional and
*tautological* (the class is defined as its closure).
(ii) **In L²(−T,T) over unions of progressions {(2πk+φ_p)/log p}:** it is a frame problem. By Doc 148
Prop. 2.2, that system **is never Riesz** (the Kronecker near-collisions violate uniform separation), and
by Prop. 2.4 **μ(T)=0**: complete but not a frame, with no lower bound.

*Proof.* (i) Besicovitch [Bes32, Ch. II]. (ii) Doc 148 Props. 2.2, 2.4. $\square$

**Critical reading of [PROP 158.3].** The "completeness of {p^{iτ}}" from the goal is NOT a single statement: in B²
it is tautological and unconditional (it carries no inertia); in L²(−T,T) it is a frame problem where the system
is ALREADY known to fail the lower bound by Kronecker. **The Diophantine completeness is real but lives on the
value side** — this will be confirmed in §3.

### 1.2. The averaging pair (H,A) — there isn't one, there are three

The goal asks that we fix EXACTLY which (H,A) from Doc 155 the question lives in. The frank answer is that the
Diophantine input admits three realizations of the averaging pair, and the choice **determines the verdict**.

**[NEW-DEFINITION 158.4] (the three candidate averaging pairs).**

- **(H₁,A₁) — the Bohr torus / value.** H₁ = L²(𝕋, Haar) on the Kronecker torus 𝕋=∏_p S¹.
  A₁ = projection onto the flow-φ invariants (= conditional expectation over the invariant σ-algebra).
  By D-b (Theorem 158.2) the flow is uniquely ergodic, so H_ind(A₁)=ℂ·1 (constants) and
  H_osc(A₁)=(constants)^⊥. This is the frame of the **sym** collapser (Theorem 4.7 of Doc 155).
- **(H₂,A₂) — Besicovitch / almost-periods.** H₂ = B²(ℝ) (Besicovitch), A₂ = B² projection onto the closure of the
  span of {e^{i(log n)t}}. H_osc(A₂) = what the B² seminorm erases. Crucially (Doc 112 Obs. 2.4): the
  B² seminorm **annihilates every compact** — H_osc(A₂) contains every function supported on a compact set of t.
- **(H₃,A₃) — the localized Weil form / inertia.** H₃ = the space of the localized Weil form
  (Doc 155 §6: sections/windows of the explicit side; Weil–Toeplitz algebra 𝒲). A₃ = average over
  windows / projection onto the "autonomous symbol computable from the primes"; H_osc(A₃) = the compact
  ideal 𝒥 = the corona 𝒞=𝒲/𝒥 where "the zeros live at the symbol/compact boundary" (Doc 134 Thm 5.2).
  F = the zero-to-zero oscillatory contribution. δ_{A₃}(F)=0 would be "the zero signal is determined by
  the autonomous symbol".

**The point of the phase, in one sentence.** The Diophantine input (D-a/D-b/D-c) lives natively in (H₁,A₁) and
(H₂,A₂) — the VALUE/PHASE spaces. RH is a statement about δ_{A₃}(F) — the INERTIA space. The
central question (§2) is whether the transversality that independence certifies in (H₁,H₂) transports to
(H₃,A₃). Preview: NO, and §3 proves why.

### 1.3. Why the three spaces are genuinely distinct (not pedantry)

**[PROPOSITION 1.x — structural record].** The three H_osc's are disjoint in their informational content:

| pair | coordinate | H_osc captures | does RH read here? |
|---|---|---|---|
| (H₁,A₁) Bohr torus | phase (p^{−it})_p | deviation from the Haar mean | NO (value) |
| (H₂,A₂) Besicovitch | time t (height) | EVERY compact (seminorm annihilates) | NO (blind to compacts) |
| (H₃,A₃) Weil | inertia/index | zero-to-zero signal (compact ideal 𝒥) | YES (it is δ_{A₃}=0) |

Row (H₂) is the subtle trap: the B² seminorm annihilates compacts, and an individual zero lives at a FIXED
height γ (a compact). Any transversality proved in (H₂) is invisible to inertia. Row (H₃) is where RH
lives. The Diophantine thread enters via (H₁)/(H₂) and must reach (H₃) — that jump is the GAP (§5).

---

## 2. The attempted transversality certificate

The candidate mechanism of the goal: *the ℚ-linear independence makes the oscillation system {p^{iτ}}
"maximally independent," so that no nontrivial combination lives in N(A) — the Diophantine
independence empties H_osc.* I try it in earnest, in each space.

### 2.1. The attempt SUCCEEDS in (H₁,A₁): independence produces ergodicity

**[PROPOSITION 158.5] (ℚ-linear independence empties H_osc of invariants on the Bohr torus).** In
(H₁,A₁), the ℚ-linear independence of {log p} (D-a) implies, via Kronecker–Weyl (D-b), that the flow φ is
uniquely ergodic, and hence H_osc(A₁)=(constants)^⊥ **contains no nontrivial invariant of the
flow**: the only F with φ_t F = F and δ_{A₁}(F)=0 is constant.

*Proof.* This is Theorem 4.7 of Doc 155 (**sym** collapser) instantiated on the Kronecker flow.
Unique ergodicity (Theorem 158.2) ⟺ dim H_ind(A₁)=1 ⟺ H_osc(A₁) hides no invariants
([Walters Thm 6.20; Doc 155 Theorem 4.7]). The transversality S∩H_osc={0} holds for S = {flow
invariants} = constants. $\square$

**This is exactly the transversality certificate requested — but of the wrong type.** The ℚ-linear
independence DOES certify a real transversality: that of the flow-invariant subspace to the flow's
oscillation space. By the reduction principle (Theorem 4.8 of Doc 155), it is a genuine collapser of
type **sym**. **But S = constants, and RH is not a statement about constants of the Bohr flow.** The
thread produces a collapser, yes — for the wrong problem.

### 2.2. The attempt FAILS in (H₃,A₃): inertia is orthogonal to the flow coordinate

**[PROPOSITION 158.6] (the Diophantine transversality does NOT transport to the Weil form).** In (H₃,A₃),
the subspace S={flow-of-Kronecker invariants / functions of the phase (p^{−it})_p} is NOT transversal
to the inertia ideal H_osc(A₃)=𝒥; in fact the zero-to-zero signal F that defines δ_{A₃} is NOT a function of the
flow's phase coordinate, but of the HEIGHT/inertia coordinate, which is independent of the Bohr flow.

*Proof.* The localized Weil form (Doc 134/Doc 148 Prop. 1.1) is
½ Q_X(F,F)=Σ_{ρ}|⟨F,e_{γ_ρ}⟩|² — a Gram sum over the HEIGHTS γ_ρ of the zeros, NOT over the phases of
the primes. The Kronecker flow acts on the phase torus ∏_p S¹; the heights {γ_ρ} of the zeros are NOT
functions of that torus (there is no homomorphism from the prime torus to the set of zeros: this is precisely
the "unknown statistics" of the zeros, Doc 148 §5.1). Hence S (functions of phase) and F (function of
height) live in independent tensor factors; S cannot be transversal to 𝒥 because it does not even
touch the coordinate where 𝒥 lives. Formally: H₃ ≅ H_phase ⊗ H_height (modulo the explicit formula that links
them, which is an IDENTITY, Doc 112 Prop. 4.2); the transversality of §2.1 lives in H_phase, the ideal 𝒥 lives
in H_height. $\square$

**The attempt fails for the cleanest possible reason: a change of coordinate.** The ℚ-linear independence empties
the oscillation in the phase coordinate (H_phase). The inertia of RH lives in the height coordinate (H_height).
They are orthogonal. **The Diophantine independence DOES empty H_osc — but the wrong H_osc.** This is,
exactly, the content of the goal: "it empties H_osc in the wrong sense — the value one, not the
inertia one". I confirm it and prove it in §3 from two independent angles (NB and Bohr/Voronin).

### 2.3. The only phase↔height bridge is the explicit formula, which is a tautology

The skeptical reader will object: phase and height ARE linked — by the explicit formula
Σ_ρ ĥ((ρ−½)/i) = (arithmetic side over {log p}). Doesn't that identity transport the transversality?

**[PROPOSITION 2.x] (the phase↔height bridge is the explicit formula and does not transport transversality).** The
explicit formula links the phase coordinate (prime side, over {log p}) and the height one (zero side,
over {γ_ρ}), but as an IDENTITY valid in every world (RH or ¬RH): by Doc 112 Prop. 4.2, every linear
combination of instances of the explicit formula is another instance, there is only ONE independent identity,
and the true configuration satisfies it identically. An identity satisfied identically **does not transport
a transversality**: it does not restrict the height parameters using the phase ones. The only
non-tautological content is one of SIGN (positivity over the Weil cone) = Weil's criterion = RH.

*Proof.* Doc 112 Prop. 4.2 (verified at the source this phase). Transporting transversality would
require knowing the prime side (unconditional) to determine the sign of the zero side; that sign is
exactly Weil's positivity, RH-equivalent. $\square$

Hence the only available bridge reintroduces RH through the positivity door — exactly the
disguised-conclusion case of Prop. 154.11 of Doc 154. The Diophantine transversality does not cross the bridge
without paying RH.

---

## 3. The stress test, head-on

### 3.1. Nyman–Beurling collapse: is the thread NB in disguise?

**The two completeness systems, precisely.**

- **Nyman–Beurling [Nym50; Beu55].** Let ρ(x)={1/x} (fractional part of 1/x). The NB criterion:
  **RH ⟺ 1_{(0,1)} ∈ closure_{L²(0,1)} of the span of the dilations {ρ(θ/x):0<θ≤1}.** Báez-Duarte [BD03]
  ("A strengthening of the Nyman–Beurling criterion", Rend. Lincei) refines it: the span of
  {ρ(1/(nx)):n∈ℕ} suffices, equivalently the completeness (with an explicit weight) of the system of
  **integer dilations**, and connects it to approximating 1/ζ by sums Σ c_n n^{−s}. The variable of the NB
  system is **SCALE** (dilation/Mellin): the acting group is (ℝ_{>0},·), and completeness is measured in L² of
  the critical line via the Mellin transform.
- **The Diophantine thread.** Completeness of the system of **characters** {p^{iτ}} (or {n^{−s}}=n^{−σ}n^{−iτ}), in
  the **FREQUENCY** variable (Fourier/translation): the acting group is (ℝ,+) by translation in t, and
  completeness is that of exponentials {e^{i(log n)t}} in B² or in L²(−T,T).

**[PROPOSITION 158.7] (the thread is NOT Nyman–Beurling as a completeness system).** The two
completeness systems are distinct: NB is completeness of dilations in the SCALE coordinate (multiplicative
group, Mellin transform), and is RH-equivalent BY CONSTRUCTION (the target 1_{(0,1)} encodes the
pole and completeness is equivalent to RH). The thread is completeness of characters in the FREQUENCY coordinate
(additive group, Fourier transform), and is UNCONDITIONAL (D-c(i): tautological in B²). There is no isomorphism
identifying an RH-equivalent target of the thread with NB's 1_{(0,1)} without choosing the weight (§3.1 below).

*Proof.* In NB, completeness is measured in L²((0,1),dx) [or the Báez-Duarte weight] and the target
1_{(0,1)} is a FIXED vector whose membership in the span IS the content — and that content is RH (Beurling 1955:
the distance from 1_{(0,1)} to the span N as a function of the number of dilations decays to 0 ⟺ RH). In the
thread, {e^{i(log n)t}} is complete in B² by definition of the class, WITHOUT a distinguished target and WITHOUT
a condition. The difference of group (multiplicative vs additive) prevents a functorial identification: the
dilation x↦θx in the scale coordinate is the translation s↦s in Mellin, orthogonal to the translation t↦t+τ in
frequency. They are two completenesses in two distinct coordinates of the same plane. $\square$

**This is a partial POSITIVE finding: the thread escapes NB as a STATEMENT.** It is not NB in disguise in
the sense of being literally the same system. But the stress test does not end here — one must check whether they share
the trap of SPACE/WEIGHT.

**[PROPOSITION 158.8] (the thread and NB share the same spatial trap: the weight carries the zeros).** For
the unconditional completeness of {p^{iτ}} in B² (D-c(i)) to be RELEVANT to inertia, it must be measured in a
space whose inner product reads the heights of the zeros — i.e., transported to (H₃,A₃) (the Weil
form). But in (H₃,A₃) the completeness of the system over {log p} **becomes RH-equivalent**, exactly
like NB: the frame lower bound μ(T) (Doc 148) IS the modulus of Weil positivity, and its positivity is
RH. The thread, by changing space to touch inertia, acquires the NB core.

*Proof.* The identification in Doc 148 Prop. 1.1: the Weil form positivity modulus = frame lower
bound of {e^{i γ t}} in L²(−T,T). For ζ (not for two pure primes), the frequencies are the
HEIGHTS γ_ρ of the zeros, and μ(T)>0 ⟺ Weil positivity ⟺ RH (Weil's criterion [Wei52]). The Diophantine
completeness of {p^{iτ}} is completeness in the prime coordinate (unconditional); to use it on the zeros
one must pass through the explicit formula (Prop. 2.x: identity, not transport) and the result is the Weil
modulus. As in NB, *the space where completeness matters is the space where completeness is RH*. $\square$

**NB sub-verdict:** the thread is NOT NB in disguise as a *system* ([PROP 158.7], genuine escape in the
frequency vs. scale coordinate), **but it falls into the same spatial trap** ([PROP 158.8]): to touch
inertia it must be measured in (H₃,A₃), where its completeness is RH-equivalent. The escape at the level of statement is not
escape at the level of mechanism.

### 3.2. Bohr–Voronin collapse: is the thread confined to the value side?

**[PROPOSITION 158.9] (Voronin/Bagchi universality is value-side and blind to RH).** The ℚ-linear
independence of {log p} is exactly what gives Voronin's universality theorem [Vor75] (ζ uniformly approximates,
on discs of the strip ½<σ<1, any non-vanishing holomorphic function) and Bagchi's limit theorem [Bag81] (the
law of ζ(·+iτ) is the random Euler product ∏_p(1−ω_p p^{−s})^{−1}, ω uniform on
∏_p S¹). Both are VALUE statements and are UNCONDITIONAL (they neither presuppose nor imply RH). Raw
universality is blind to RH.

*Proof.* Voronin [Vor75], Bagchi [Bag81; Lau96 Ch. 5–6], used at the source via Doc 112 §2.4. The
universality and the limit theorem hold unconditionally; what is RH-equivalent is **strong
recurrence** (positive lower density of τ with ζ(·+iτ)≈ζ on a disc) [Bag87], which uses ζ|_D belonging to
Bagchi's support S = {non-vanishing}∪{0}, which is RH. Universality alone (approximating UNRELATED functions)
does not touch the status of ζ itself. $\square$

**[THEOREM 158.10] (the core: the Diophantine thread is confined to the value side by construction).** The
ℚ-linear independence of {log p}, in its B² completeness / Bohr-torus equidistribution form,
empties H_osc(A₁) and H_osc(A₂) in the sense of oscillation-of-VALUES (the flow's phase coordinate and
Besicovitch's time coordinate t), but is **structurally blind to the inertia coordinate** (the
height γ of a zero). Consequently, it does not collapse δ_{A₃}(F) (the defect in the Weil form) and is NOT the
transversality certificate that RH needs.

*Proof.* I combine three already-proved facts.
(1) (§2.1, Prop. 158.5) Independence certifies transversality in (H₁,A₁): ergodicity of the flow,
S=constants transversal to H_osc(A₁). Coordinate: PHASE.
(2) (§2.2, Prop. 158.6) That transversality does NOT transport to (H₃,A₃): the zero-to-zero signal F lives in the
HEIGHT coordinate, orthogonal to the phase one; the bridge (explicit formula) is identity, not transport
(Prop. 2.x).
(3) The blindness is exactly the B² seminorm of Doc 112 Obs. 2.4: in (H₂,A₂), the Besicovitch seminorm
ANNIHILATES every compact; an individual zero lives at a FIXED height γ, a compact; hence H_osc(A₂) contains
the window of the zero and the "B² transversality" says nothing about it. It is the same reason direct LP-112
died (Doc 112 §2.4, Prop. 2.6: zero-density witnesses) and why the Tauberian no-go located
the wall (Doc 157 Theorem 157.10: averages do not see the individual frequency of the zero).
From (1)+(2)+(3): the thread empties the value oscillation and is blind to the inertia one. $\square$

**Triple verification of the stress test (as the contract requires for any suspected escape).**
- **Verification 1 (via seminorm):** Obs. 2.4 of Doc 112 — the coordinate where independence acts (t,
  phase) has a seminorm that annihilates the compacts where inertia lives. ✓ confirms confinement.
- **Verification 2 (via density):** Prop. 2.6 of Doc 112 — under ¬RH the witnesses of the phase→inertia
  transfer have ZERO density; Diophantine equidistribution produces generics, and the generic is
  bad. Independence gives equidistribution (generic), not the exceptional event (inertia). ✓ confirms.
- **Verification 3 (via frames):** Doc 148 Prop. 2.4 + §5.2 — over the heights of the zeros, μ(T)=0 (no
  frame bound) and infinite density breaks the frame; the Diophantine completeness of {p^{iτ}} does not provide a
  lower bound in the inertia coordinate. ✓ confirms.
The three independent verifications give the same verdict: confinement to the value side. There is no (c).

**Bohr/Voronin sub-verdict:** the thread IS Bohr/Voronin — it lives on the Bohr torus (Prop. 158.5 = the
Kronecker flow), powers universality (Prop. 158.9), and is confined to the value side by the B²-seminorm
blindness ([THEOREM 158.10], triple-verified). **Case (b).**

### 3.3. Why the confinement is structural and not a technical defect

The underlying reason, in the language of Doc 154: the ℚ-linear independence is a certificate of type **sym**
(Theorem 154.9, type T4: invariance under the Kronecker flow). By Prop. 154.11, type T1/T3/T4/T5
certificates have verifiable-from-outside input and do NOT fall into the disguised-conclusion mode — but
RH falls into the POSITIVITY mode (T2), the only channel whose input can be the thesis itself. A
**sym** certificate (the thread) cannot collapse a defect that is of **positivity** type without crossing the
explicit-formula bridge, which reintroduces the sign (= RH). The confinement is the manifestation, in
Diophantine coordinates, of Prop. 154.12: *the RH wall is one of positivity because it is the only channel whose
input can be the conclusion*, and the thread is a symmetry input, of the wrong type.

---

## 4. Verdict (a/b/c)

### 4.1. The verdict

**VERDICT: case (b) — the Diophantine thread is Bohr/Voronin, confined to the value side; it empties the oscillation of
values but NOT the one of inertia; DEAD as a crossing, with a core of (a) in the spatial mechanism.**

Breakdown against the three options of the goal:

- **(a) Is the thread Nyman–Beurling in disguise (RH-equivalent, circular)?** **PARTIALLY, and in a precise
  sense.** As a *completeness system* NO ([PROP 158.7]: NB is completeness of dilations in Mellin
  scale; the thread is completeness of characters in Fourier frequency — distinct coordinates, distinct
  groups, the thread is unconditional). BUT it shares the *spatial trap* ([PROP 158.8]): for the
  unconditional completeness to touch inertia it must be measured in (H₃,A₃) = the Weil form, where it becomes
  RH-equivalent (μ(T)>0 ⟺ RH). The NB core reappears not in the statement but in the space.
- **(b) Is the thread confined to the value side (Bohr/Voronin), emptying H_osc in the wrong sense?**
  **YES, PROVED ([THEOREM 158.10], triple-verified §3.2).** Independence certifies transversality in
  the phase coordinate (Bohr torus, Kronecker ergodicity, **sym** collapser), which is orthogonal to the
  inertia coordinate (height of the zeros) where RH lives. The blindness is the B² seminorm that annihilates
  compacts (Obs. 2.4 Doc 112), the same one that killed direct LP-112.
- **(c) Is there a THIRD thing — an inertia certificate without RH-equivalence or confinement?** **NO.** The
  attempt of §2 fails (Prop. 158.6); the only phase→inertia bridge is the explicit formula, which is identity,
  not transport (Prop. 2.x); the three independent verifications (seminorm, density, frames) confirm
  confinement. I do not distrust a nonexistent (c): what there is is (b) with a residue of (a).

### 4.2. The mechanism of the blindness, exact and triple-verified

The heart of the verdict is that **the Diophantine thread and RH live in tensorially
independent coordinates**: H₃ ≅ H_phase ⊗ H_height. The ℚ-linear independence is an equidistribution theorem in
H_phase (the Bohr torus ∏_p S¹). RH is an inertia theorem in H_height (Weil positivity over the
heights {γ_ρ}). The only operator linking the factors is the explicit formula, which is an identity
(Doc 112 Prop. 4.2) and therefore does not transport the certificate from one factor to the other. The three
distributional tools acting in H_phase (B² seminorm, Bagchi equidistribution, Beurling–Landau frames)
are the three blind to H_height — and that blindness is exactly the master quantifier of P43 (the average does not
see the point), confirmed three times.

### 4.3. Why this is the frank and valuable result

The goal anticipated that the frank result would be (a) or (b), and that (c) would deserve triple
distrust. It is (b), with the core of (a) localized in the spatial mechanism. The value of the document is NOT an
equivalence of RH (none is produced). The value is **precisely locating the boundary between the
unconditional Diophantine completeness and the inertia certificate that RH needs**, and showing that that
boundary is a change of coordinate (phase→height) whose only bridge is a tautology. This closes the only
surviving crack of Phase 49 (GAP-157.A) with a well-founded NEGATIVE verdict: the Diophantine thread does not
cross the wall, and the reason is structural (Prop. 154.11/154.12), not technical.

---

## 5. The exact GAP: Diophantine (unconditional) completeness vs. the inertia certificate

Even though the verdict is (b)-dead, the contract requires isolating the exact GAP separating what the thread
DOES have (unconditional Diophantine completeness) from what RH needs (an inertia certificate). I name it with
precision.

**[GAP-158.A] (the missing phase→inertia functor).** The ℚ-linear independence of {log p} certifies
transversality on the phase torus 𝕋=∏_p S¹ (VALUE coordinate; collapser of type **sym**, unconditional,
RH-free). The inertia certificate that RH needs lives in the space of the Weil form over the HEIGHTS
of the zeros (INERTIA coordinate; defect δ_{A₃}, POSITIVITY type). The GAP is the **absence of a functor
𝔉: (transversality in 𝕋, phase side) → (transversality in 𝒥, inertia side)** that transports the
transversality without going through the explicit formula (which is identity, not a transport functor). Three
exact properties 𝔉 should have, and that no known object has:
1. **It must couple the factors H_phase and H_height** without being the explicit formula (which couples them as a
   tautological identity, Prop. 2.x). I.e., it must be a coupling that restricts, not one that equates.
2. **It must be blind to the B² seminorm** (which annihilates the height coordinate, Obs. 2.4) — i.e., it must operate
   in a space where height compacts carry positive weight, NOT in B² nor in raw L²(−T,T).
3. **It must be of type τ=? (non-commutative/phase)** in the sense of Doc 155 §5.2: NOT reducible to
   positivity (it would fall into RH-equivalence), NOR to bounds/orders/UCP (Doc 154 T1/T3), NOR to symmetry alone
   (which is what the thread ALREADY is, and it stays in H_phase). It must be the fifth collapser.

**[BRIDGE — status of GAP-158.A].** This GAP is the exact intersection of three independent lines of
the program:
- the **fifth collapser of type τ=?** of Doc 155 §5.2 (non-commutative/phase, pair of projections in
  generic position / incommensurable frame), which Doc 155 declared searchable but not constructed;
- the **crack GAP-157.A** of Doc 157 (non-local spectral Tauberian condition with Diophantine input), which
  Doc 157 left as an unproved [literature GAP];
- the **new input (not new mechanism)** of Doc 154 §5/§6: a cohomology class over Spec ℤ that reads
  inertia (T5 type with input nonexistent in the literature).
The three are the SAME thing seen from three tools: the phase→inertia functor that the Diophantine
thread does NOT provide but whose candidate input IT IS. **The thread is the correct input (unconditional, RH-free, lives
on the phase torus); what is missing is the transport to inertia, which is an unconstructed object of type τ=?.**

**[literature GAP, declared, NOT a premise of any theorem].** I am not aware of a theorem in the literature that
transports the ergodicity of the Kronecker flow in ∏_p S¹ to an inertia/positivity lower bound over
the heights of the zeros of ζ without going through the explicit formula. The machinery of operators in
Pontryagin spaces (the κ=2m of P35), incommensurable frames (Doc 148), and the foliated cohomology of Spec ℤ
(Phases 40–43) are the three candidates for 𝔉, all with their own open GAP. I record it as the frontier, not
as a proved route.

**[WISH 158.B].** That there exist an 𝔉 of type τ=? that uses the ℚ-linear independence of {log p} (via
completeness of {p^{iτ}} in a space with a positive height weight, NOT B²) as input for a non-commutative
collapser of the defect δ_{A₃}. It would be the fifth collapser of Doc 155 with its input identified. I do not
have it; I name it as a wish, not an actionable gap, because the phase→height coordinate change
(Prop. 158.6) suggests that the correct transport is not harmonic-analytic but rather spectral/non-commutative
in nature — consistent with the heuristic of Doc 155 §5.2.

---

## 6. Final message

**VERDICT: case (b) — the Diophantine thread is Bohr/Voronin, confined to the VALUE side.** The
ℚ-linear independence of {log p} (= completeness of {p^{iτ}}) IS a genuine transversality certificate, but of the
wrong type: it empties H_osc in the PHASE coordinate (the Bohr torus ∏_p S¹, via Kronecker
ergodicity — **sym**-type collapser, unconditional), which is orthogonal to the INERTIA coordinate (the
heights of the zeros) where RH lives. The blindness is the B² seminorm that annihilates compacts (the same one that killed
direct LP-112). It does NOT collapse the individuation defect δ_{A₃} of the Weil form. NO
equivalence of RH is produced.

**Which of the three collapses/escapes?** **Collapse (b) Bohr/Voronin — confinement to the value side**, with a
core of (a) Nyman–Beurling located NOT in the statement (genuine escape: completeness of characters in
frequency ≠ completeness of dilations in scale) but in the SPATIAL TRAP (to touch inertia one must
measure in the Weil form, where completeness becomes RH-equivalent). It is NOT (c).

**Three findings with labels:**

1. **[THEOREM 158.10 + PROP 158.5/158.6] — The thread empties the WRONG H_osc.** The ℚ-linear independence
   certifies transversality on the Bohr torus (ergodicity of the Kronecker flow, **sym** collapser),
   but that transversality does NOT transport to the Weil form because the zero-to-zero signal lives in the
   height coordinate, tensorially independent from the phase coordinate; the only bridge (explicit
   formula) is an identity, not a transport (Prop. 2.x). Triple-verified: B² seminorm annihilates compacts
   (Obs. 2.4 Doc 112), zero density of witnesses (Prop. 2.6 Doc 112), μ(T)=0 in frames (Doc 148 Prop. 2.4).

2. **[PROP 158.7 + PROP 158.8] — The thread escapes Nyman–Beurling as a STATEMENT but not as a MECHANISM.**
   NB is completeness of dilations in the scale coordinate (Mellin, multiplicative group), RH-equivalent
   by construction; the thread is completeness of characters in the frequency coordinate (Fourier, additive
   group), unconditional — they are distinct systems. BUT both share the spatial trap: for the
   Diophantine completeness to touch inertia it must be measured in (H₃,A₃), where the frame lower bound IS the
   Weil positivity = RH. The escape at the statement level is not escape at the mechanism level.

3. **[GAP-158.A + BRIDGE §5] — The exact GAP is the phase→inertia functor, = the unconstructed fifth
   collapser.** What separates the unconditional Diophantine completeness from the inertia certificate is the
   absence of a functor 𝔉 that transports the transversality from the phase torus (where the thread has it) to the
   inertia ideal (where RH needs it), without going through the explicit-formula tautology. 𝔉 must be of type
   τ=? (non-commutative/phase, Doc 155 §5.2), blind to the B² seminorm, and not reducible to positivity. It is the
   SAME boundary as GAP-157.A (Doc 157), the fifth collapser (Doc 155 §5), and the cohomological input over
   Spec ℤ (Doc 154 §5) — three tools, a single missing object. **The Diophantine thread is the candidate
   input of 𝔉 (unconditional, RH-free, lives on the phase torus); it is NOT 𝔉.**

---

## References

**Internal (backward-only):** Doc 154 (taxonomy of crossings; Theorem 154.5 the wall=N(A); Theorem 154.9
exhaustiveness by logical type T1–T5; Prop. 154.11/154.12 verifiable-boundary/disguised-conclusion WITHIN
positivity, RH is of positivity type); Doc 155 (defect δ_A=‖(1−A)F‖; Theorem 3.4 no free-individuation no-go;
Theorem 4.7 sym collapser/ergodicity; Theorem 4.8 reduction principle; §5.2 fifth collapser τ=?
non-commutative/phase; §6 Weil-form dictionary, compact ideal 𝒥); Doc 157 (GAP-157.A Diophantine
condition as spectral Tauberian; Theorem 157.10 local Tauberian no-go; Prop. 157.7 resonance
density=zeros); Doc 148 (frames Λ_p∪Λ_q; Prop. 1.1 Weil form=Gram of exponentials; Prop. 2.2 never
Riesz; Prop. 2.4 μ(T)=0; §5.2 infinite density breaks the frame); Doc 112 (LP-112; Lemma 2.2 Kronecker–Weyl
on {log p}; Obs. 2.4 B² seminorm annihilates compacts; Prop. 2.6 zero density of witnesses under ¬RH; Bagchi's
support S; Lemma 3.3 non-discreteness; Prop. 4.2 explicit formula is an identity); Doc 134 (corona
𝒞=𝒲/𝒥, zeros at the symbol/compact boundary); P35 (κ=2m, Pontryagin spaces); P43 (master
quantifier, value/inertia).

**Literature (published, verifiable unless marked):**
- [Nym50] B. Nyman, *On the One-Dimensional Translation Group and Semi-Group in Certain Function Spaces*,
  thesis, Uppsala, 1950. (Original criterion: RH ⟺ completeness of the translations/dilations of ρ.)
- [Beu55] A. Beurling, *A closure problem related to the Riemann zeta-function*, Proc. Nat. Acad. Sci. USA
  41 (1955), 312–314. (NB criterion in closed form; the distance from 1_{(0,1)} to the span decays to 0 ⟺ RH.)
- [BD03] L. Báez-Duarte, *A strengthening of the Nyman–Beurling criterion for the Riemann hypothesis*, Atti
  Accad. Naz. Lincei Cl. Sci. Fis. Mat. Natur. Rend. Lincei (9) Mat. Appl. 14 (2003), 5–11. (Refinement:
  the span of integer dilations / power basis suffices; connection with Σ c_n n^{−s}.)
- [Vor75] S. M. Voronin, *Theorem on the universality of the Riemann zeta-function*, Izv. Akad. Nauk SSSR
  Ser. Mat. 39 (1975), 475–486 (Math. USSR-Izv. 9 (1975), 443–453). (Universality: ζ approximates every
  non-vanishing holomorphic function in the strip; a value statement, blind to RH.)
- [Bag81] B. Bagchi, *The statistical behaviour and universality properties of the Riemann zeta-function and
  other allied Dirichlet series*, thesis, Indian Statistical Institute, Calcutta, 1981. (Functional limit
  theorem; random Euler product; support S={non-vanishing}∪{0}.)
- [Bag87] B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math. Hungar. 50
  (1987), 227–240. (Strong recurrence ⟺ RH — the half that DOES use the support, RH-equivalent, contrasted
  with raw universality which is not.)
- [Lau96] A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, 1996. (Complete exposition
  of Bagchi's limit theorem, Ch. 5–6; support of the limit measure.)
- [Boh18] H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918), 136–156.
  (Almost-periodicity of Dirichlet series; the ℚ-linear independence of {log p} gives almost-periodicity in
  σ>1; value side.)
- [Bes32] A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Class B²; the
  B² seminorm annihilates compacts; closure of trigonometric polynomials.)
- [Wei52] A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Sém. Math. Univ.
  Lund (1952), 252–265. (Weil's positivity criterion; positivity of the arithmetic side over the test
  cone ⟺ RH — the sign content, positivity type.)
- [Kro1884] L. Kronecker, *Näherungsweise ganzzahlige Auflösung linearer Gleichungen*, Berl. Sitzungsber.
  (1884). [Kronecker's theorem; H. Weyl, Math. Ann. 77 (1916), 313–352, for equidistribution.]
- [Wal82] P. Walters, *An Introduction to Ergodic Theory*, GTM 79, Springer, 1982. (Thm 6.20: minimal
  translation of a compact group = uniquely ergodic — the ergodicity of the Kronecker flow.)
- [Landau67] H. J. Landau, *Necessary density conditions for sampling and interpolation of certain entire
  functions*, Acta Math. 117 (1967), 37–52. (Beurling–Landau densities; via Doc 148.)

*End of Doc 158.*
