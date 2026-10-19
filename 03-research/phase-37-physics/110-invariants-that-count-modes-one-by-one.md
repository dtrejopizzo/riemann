# Doc 110 — Invariants that count modes one by one: the argument principle, spectral flow, and the specification of the inertia reader

**Program:** Riemann Hypothesis — Phase 37, "physics mode"
**Prerequisites:** P43 (§4 value vs inertia, §6 boundary principle); Doc 108 (autonomy of the value ≠ autonomy of the inertia; binarity of per-window indices; Theorems 3.3, 3.4, Prop. 2.3, 2.5); Doc 107 (W₂, nine blocks, Prop. 6.1); Doc 106 (tensor identity, amplification); Doc 100 (semilocal Maslov index, exhaustion lemma, Conjecture 100.A); Doc 99 (CCM-ZST, CF rigidity, route E5: κ_λ(N)); Doc 96 (Theorem 8.1); P35 (κ(Q) = 2m); P41 (interior/boundary no-go); NO-GO-LIST (MW-1…MW-7).
**Absolute rule:** no proof is fabricated. Every step is a complete proof, a literature statement with a verifiable reference, or a declared GAP. No numerics, no simulations. Backward-only citations; what is unverified is marked [NOT VERIFIED].

---

## 0. Executive summary

P43 closed the program with the master quantifier: every method fails because it
certifies the averaged side of a statement whose individual refinement is RH. But
mathematics has objects that count **without averaging**: winding numbers, spectral
flows, Fredholm indices, K-theory classes. An integer is not averaged: it is read.
This document examines why none of these integers resolves RH, locates the failure
point of each one, and produces the central contribution: the **axiomatic
specification of the inertia reader** (axioms L1–L6) and an **impossibility theorem**
in the class of arithmetic quadratic functionals. Findings, in order:

1. **(§2) The argument principle, taken seriously: the integer is individual and
   decidable box by box (Turing's method), but its UNIFORM evaluation requires
   either pointwise bounds in the strip (RH-strength) or averaging (Littlewood's
   lemma → zero density: individuality is lost).** Lemma 2.4 ("non-evaluation
   lemma"): the numerical gap is exactly that of Doc 108 — the per-box winding
   number is known with error O(log T) and distinguishing 0 from ≥1 requires error
   < 2π: relative precision o(1/log T), the scale of Conjecture 108-N. The
   winding-number wall IS the sieve wall in contour coordinates.

2. **(§2.6) The parity obstruction is vacuous.** The quadruple symmetry forces
   N_off ≡ 0 (mod 2) on boxes symmetric in t — unconditionally, in both worlds: an
   identically-zero invariant detects nothing (Prop. 2.6). Mod 4 is equivalent to
   the parity of the upper half-box, which no known symmetry determines (GAP). And
   the parity reading via sign changes of the Hardy Z function breaks down exactly
   at the on/off **partition** — the non-autonomy of inertia from Doc 108 in parity
   coordinates (Obs. 2.7).

3. **(§3) The spectral flow of the Euler filtration reformulates RH exactly
   (Theorem 3.2, unconditional): RH ⟺ sf{A_λ} = 0, with A_λ the semilocal CCM-ZST
   operator and the primes entering one by one at λ = √p by automatic support
   locality.** Under ¬RH the crossing occurs at a **finite** λ₀: the event is
   individual. The wall: λ₀ depends on the height of the unknown zero, the flow per
   CF-approximant step is 0 unconditionally (Carathéodory–Fejér rigidity: zeros of
   the H_x real at every finite step), and the limit pass of the flow requires the
   uniform gap — MW-6 literally (Prop. 3.4).

4. **(§4) Specification of the inertia reader: axioms L1–L6.** The key refinement
   is the **finiteness** axiom (L6): I must factor through an object of finite
   dimension bounded **a priori** (without zero positions) with arithmetic traces.
   Theorem 4.3 (impossibility, class ℱ): for I = neg.ind(Q|_V′) with Q of explicit-
   formula type and V′ test-accessible, (L2)+(L3)+(L4) are **inconsistent** —
   forced by the sub-resolution/resolution dichotomy of Doc 108. Prop. 4.5 (abstract
   counterexample): in **a priori finite range** the inertia IS autonomous — Newton's
   identities convert finitely many traces (values) into the signature (inertia).
   Corollary 4.6: the specification is consistent if and only if it includes a
   finiteness theorem; the inertia reader, if it exists, is cohomological in the
   precise sense of L6.

5. **(§5) Connes–Consani, measured against the specification: what is missing is
   exactly L6 with Lefschetz traces and the positivity of L3 — the "standard
   conjectures on Spec ℤ" form.** Their tropical Riemann–Roch produces Euler
   characteristics (values); not a signature with positivity. Obs. 5.3: the tensor
   amplification of Form B (Docs 106–108) is Deligne's trick **minus finiteness** —
   and it died precisely for that reason.

6. **(§6–§7) Passed entirely through the master quantifier: every candidate falls
   into the same inversion, but the passage leaves a new residue — RH is a
   countable conjunction of individually decidable integer events (Π₁ manifest in
   two coordinates: boxes and prime steps), and the wall is the absence of a LOCAL
   reason (curvature, per-step positivity) forcing each integer to 0.** In
   function fields that reason exists (Castelnuovo). VERDICT: **PARTIAL** (§7).

---

## 1. Framework: the physics question

P43 §6 (boundary principle): the missing mechanism must **read inertia, not
value** — individuate a signature where only one trace is available
unconditionally; the historical clue is ℓ-adic cohomology, which in function fields
gives an integer signature directly. Doc 108 §7.4 gave the formula: *autonomy of the
value ≠ autonomy of the inertia* — the arithmetic side computes the window total,
not the partition into blocks.

The question of this document: mathematics has invariants that count modes
**one by one, without averaging** — the winding number (argument principle: counts
zeros exactly), the spectral flow of a family of self-adjoint operators (counts
eigenvalue crossings through 0; [APS76], [Phi96], [RS95]), the Fredholm index and
its localizations (Atiyah–Singer [AS63]: analytic index = topological index, sum of
local contributions), K-theory classes and topological charges in physics
(quantized, stable under deformation). Why does none of these read the inertia of
ζ? The answer is not "because they average anyway" (the master quantifier as
mantra); it is a dissection of **where**, in each case, reading the integer turns
into an averaging problem, and which exact axiom fails. The positive residue is the
specification in §4.

---

## 2. (i) The argument principle, taken seriously

### 2.1. The integer

For σ₀ ∈ (1/2, 1) and 0 < T₁ < T₂, let R = [σ₀, 2] × [T₁, T₂] (no zeros on the
boundary — ensurable by moving T₁, T₂ by o(1)). The argument principle gives

$$N_{\mathrm{off}}(R) \;=\; \frac{1}{2\pi i}\oint_{\partial R}\frac{\zeta'}{\zeta}(s)\,ds
\;=\; \frac{1}{2\pi}\,\Delta_{\partial R}\arg\zeta \;\in\; \mathbb{Z}_{\geq 0},$$

the exact number of zeros of ζ in R, counted with multiplicity. It is a winding
number: the degree of the curve ζ(∂R) around 0. Individual, integer, not
averaged, stable under contour perturbations that do not cross zeros. And

$$\mathrm{RH} \iff N_{\mathrm{off}}(R) = 0 \ \text{ for every rectangle } R
\text{ to the right of the critical line}.$$

RH is the vanishing of a countable family of winding numbers (σ₀, T_i ∈ ℚ
suffice). Nothing could be more individual: each off-critical zero, if it exists,
contributes its integer unit to some R. Why can we not evaluate the integer?

### 2.2. Inventory of control over the four sides

We write Δ_L arg ζ for the variation of the argument along side L, so that
2π N_off(R) = Δ_right + Δ_top + Δ_left + Δ_bottom.

**(a) Right side, Re s = 2 (from 2+iT₁ to 2+iT₂): O(1) control, unconditional and
uniform.** On Re s = 2 the Euler product converges absolutely and
|log ζ(2+it)| ≤ Σ_p Σ_k p^{-2k}/k = log ζ(2) < ∞, whence
|Δ_right| ≤ 2 log ζ(2) — an absolute constant, independent of T. This side is
"bought" by the region of absolute convergence: it is the only portion of the
contour that a single prime controls (cf. MW-2).

**(b) Horizontal sides, t = T_j (from 2+iT_j to σ₀+iT_j): O(log T) control,
unconditional.** Classical Backlund/von Mangoldt argument ([Tit86, §9.4]): the
variation of arg ζ over the segment is bounded by π(1 + number of zeros of
Re ζ(σ+iT_j) in σ ∈ [σ₀,2]), and that number is bounded via Jensen applied to
½(ζ(s+iT_j) + ζ(s̄+iT_j)) on a disk centered at 2: |Δ_top|, |Δ_bottom| = O(log T_j),
valid if the segment does not pass through a zero. "Typically" this is not
improvable: the variation reaches ≍ log T when the segment passes near ≍ log T
zeros (von Mangoldt density N(T+1) − N(T) ≍ (1/2π) log T).

**(c) Left side, Re s = σ₀ (from σ₀+iT₂ to σ₀+iT₁): the whole problem lives here.**
The variation is π[S(σ₀,T₂) − S(σ₀,T₁)] with S(σ,T) := (1/π) arg ζ(σ+iT)
(continuous branch from 2+iT). What is known:

- **Unconditional, pointwise:** S(σ,T) = O(log T), uniform in σ ≥ 1/2 (Backlund
  shifted to abscissa σ; [Tit86, Thm. 9.4] and the standard uniformity remark).
  Nothing pointwise-better is known for fixed σ₀ ∈ (1/2, 1) without a hypothesis.
  Under RH: S(T) = O(log T / log log T) (Littlewood; [Tit86, Thm. 14.13]).
- **Unconditional, on average:** S₁(T) := ∫₀^T S(t)dt = O(log T) ([Tit86, Thm. 9.9]):
  the average of S over [0,T] is o(1). Selberg [Sel46]: ∫₀^T |S(t)|^{2k} dt ∼
  c_k T (log log T)^k — S is on average of size √(log log T). **The average of S is
  tiny; its pointwise value is known only to be O(log T).** All the individual
  information (the zero positions) lives in the difference between value and
  average — exactly the value/inertia structure.

### 2.3. The precise point where the integer turns into an average

The argument integral over the left side is **a sum of individual jumps**: by the
Hadamard identity ζ'/ζ(s) = Σ_ρ [1/(s−ρ) + 1/ρ] + O(log|s|), the contribution of
each zero to the variation over the left side is the angle subtended by the segment
as seen from ρ — close to 2π·(fraction of the winding) if ρ is to the right and
near the side, close to 0 if it is far. **To bound the sum of angles one needs to
know where the zeros are: the individual integer is evaluated only by knowing the
individuals.** The only two known routes for extracting something from the left
side:

**(α) Pointwise bounds in the strip.** If one knew ζ(s) ≠ 0 for Re s > σ₀ with a
controlled lower bound |ζ(σ₀+it)| > exp(−φ(t)), arg ζ would follow by integrating
ζ'/ζ over a zero-free region. But "ζ does not vanish for Re s > σ₀" **is**
quasi-RH at level σ₀: the needed input is (a version of) the conclusion.

**(β) Averaging in σ: Littlewood's lemma.** The standard unconditional tool
([Tit86, §9.9]; [IK04, Thm. 5.12 and Ch. 10]) is

$$2\pi \int_{\sigma_0}^{2} N_{\mathrm{off}}(\sigma, T)\, d\sigma
\;=\; \int_{0}^{T}\log|\zeta(\sigma_0+it)|\,dt \;+\; O(\log T).$$

The right side is an **average value** of log|ζ| over the left side, accessible via
moments of ζ: this is how ALL zero-density theorems are proved,
N(σ,T) ≪ T^{κ(σ)}(log T)^{O(1)} ([Ing40], [IK04, Ch. 10]). Note what happened:
the individual integer N_off(σ₀,T) was replaced by its **average in σ** — an
average of winding numbers over nested rectangles. The average is evaluable; the
individual is not: a single zero at β = σ₀ + ε contributes a mass ε to the
integral that drowns in the O(log T) error.

### 2.4. The non-evaluation lemma

**Lemma 2.4 (non-evaluation of the winding number).** Let R_T = [σ₀,2] × [T, T+1]
be the unit-height box. Then:

(a) *The unconditional contour budget is O(log T):* the bounds of §2.2 give
|2π N_off(R_T)| ≤ |Δ_right| + |Δ_top| + |Δ_bottom| + |Δ_left| = O(log T), and this
order is achieved (left side and horizontal sides really fluctuate at scale log T).

(b) *Detection requires absolute precision < 2π:* distinguishing N_off(R_T) = 0
from N_off(R_T) ≥ 1 demands evaluating Δ_left with absolute error < 2π, i.e.,
**relative error o(1/log T) over the side's budget** — the same second-order
precision scale as Conjecture 108-N (Doc 108, eq. (4.1)).

(c) *Evaluation dichotomy:* every known route for evaluating Δ_left is of one of
two types. (α) pointwise: requires a zero-free region to the right of σ₀ with a
lower bound on |ζ| — a quasi-RH-strength statement at level σ₀ (the conclusion as
input); or (β) averaged: integrates in σ (Littlewood) or in t (moments of S,
Selberg) and produces density theorems — valid for **almost every** box, with no
information about the individual box aligned with the hypothetical zero. The
exceptional box that the average does not control is exactly where the signal
lives.

*Proof.* (a) is §2.2. (b): N_off is an integer ≥ 0; 0 vs ≥1 is an absolute gap
of 2π in 2πN_off; the other three sides are evaluated with O(1) error (right
side: Euler product; horizontals: the standard reduction — shift σ₀ by o(1) to
dodge zeros of Re ζ — leaves the weight of detection in Δ_left). For (c) we do
not claim to classify "all possible routes" (not provable); we claim, with proof,
that the two routes from the literature have these profiles: (α) integrating ζ'/ζ
needs a zero-free domain for ζ plus a lower bound to fix the branch — and "no
zeros to the right of σ₀" is N_off = 0, what was to be evaluated; (β) Littlewood's
lemma has as its evaluable side an average in σ, and Selberg's moments are
averages in t; neither separates the individual box (Doc 108 §5.2: the step from
"almost every" to "every" is large-values theory, and under ¬RH the large value
is exactly at the frequency of the off-critical zero). ∎

**Observation 2.5 (the integer is decidable box by box; the wall is the
quantifier, not the decision).** Required frankness: for each FIXED box R_T, the
integer N_off(R_T) **is indeed computable** — that is what Turing's method [Tur53]
does, with which RH has been verified up to height 3·10¹² [PT21]: a finite
computation per box. What does not exist is a **uniform evaluation**: an argument
giving N_off(R_T) = 0 for ALL T at once. RH is thus a countable conjunction of
individually decidable integer events — a manifest Π₁ statement — and Lemma 2.4
says that the step from "each one, by computation" to "all, by a reason" is the
inversion of the master quantifier. The winding number does not dodge the wall: it
presents it in logical coordinates. It does contribute the **individuality of
falsification**: a single computation can refute RH; none can prove it.

### 2.6. The parity obstruction: analysis and closure

Can the winding number be evaluated MODULO something? The hope: a symmetry that
determines N_off mod 2 (or mod 4) without evaluating the integral.

**Proposition 2.6 (the forced parity is vacuous).** Let R^sym = [σ₀,2] × [−T,T] be
the box symmetric about the real axis (no zeros on the boundary). Then
N_off(R^sym) ≡ 0 (mod 2), unconditionally. The same conclusion holds for any box
symmetric in t. By contrast, for upper boxes R = [σ₀,2] × [T₁,T₂] with T₁ > 0, no
symmetry of ζ relates N_off(R) to N_off of the same box: the available symmetries,
s ↦ s̄ (reality: ζ(s̄) = conj ζ(s)) and s ↦ 1−s (functional equation), send R to its
reflection across the real axis (disjoint from R) and to its reflection to the
left of the critical line (disjoint from R), respectively. In particular: (a) the
mod 2 of the symmetric box is 0 in both worlds (RH and ¬RH) — an identically null
invariant detects nothing; (b) N_off(R^sym) mod 4 = 2·N_off(R^up) mod 4 is
equivalent to the parity of the upper half-box's count, which (by the second part)
no known symmetry determines. OPEN GAP (no candidate): no exploitable parity
obstruction is known.

*Proof.* The reality of ζ gives: ρ zero ⟺ ρ̄ zero, with equal multiplicity. The
symmetric box is stable under conjugation and has no real zeros (ζ(σ) ≠ 0 on
(0,1), [Tit86, §2.12]): the zeros come in free-orbit pairs {ρ, ρ̄}, an even count.
For (b): the involution ρ ↦ 1−ρ̄ swaps the half-planes and does not act within
R^up. That "no known symmetry" determines the upper parity is an inventory
statement, not a theorem: the exact symmetries of ζ are those generated by
s ↦ s̄ and s ↦ 1−s. ∎

**Observation 2.7 (where the parity reading breaks down: the partition, again).**
There is a parity that CAN be read individually: that of the total N(T). The
Riemann–Siegel function Z(t) is real, |Z(t)| = |ζ(½+it)|, its sign is computable
pointwise, and N(T) = (1/π)θ(T) + 1 + S(T) with explicit θ — Turing's method
exploits this. But the parity we need is that of N_off = N − N₀ (N₀ = zeros on
the line), and sign changes of Z give only a **lower bound** on N₀ (a zero of even
multiplicity or a symmetric off-critical pair do not change the sign). Reading the
parity of N_off requires separating the total count into on/off blocks — **the
same partition that Doc 108 §7.4 identified as non-autonomous for the inertia of
Q₂**. Parity is not a side door: it is the inertia mod 2, and it inherits its
non-autonomy. The symmetry kills the odd part (Prop. 2.6(a)) and the even part is
invisible to any parity argument — structurally identical to Selberg's parity
principle on Arc A (P43 §3.2): symmetry determines parity, and the parity so
determined does not distinguish the worlds.

### 2.8. Partial verdict (i)

The argument principle is neither trivial nor a way out: it is the master
quantifier in its cleanest form. The integer exists, is individual, is decidable
box by box; its uniform evaluation requires either (α) the conclusion as input or
(β) averaging and losing the individual; its mod 2 is vacuous by symmetry; its
mod 4 is equivalent to a non-autonomous partition. Net contribution: the
quantitative identification with Doc 108 (relative precision o(1/log T) in both)
and the explicit Π₁ form of RH as a family of decidable integers (Obs. 2.5), which
§3 will re-encounter.

---

## 3. (ii) Spectral flow of the Euler filtration

### 3.1. The arithmetic family is the analytic family: automatic locality

Verified input (Doc 99, §2, against arXiv:2511.22755): CCM-ZST construct, for each
λ > 1, the semilocal Weil form QW_λ = restriction of the full Weil form to
L²([λ^{-1}, λ], d*u), with **automatic locality**: if supp f ⊆ [λ^{-1},λ], then
W_p(f^* * f) = 0 for every p^m > λ². The "Euler product truncated at p ≤ λ²" is not
a mutilation: it is a support theorem. QW_λ defines a self-adjoint operator A_λ
with discrete spectrum bounded below, with μ_λ := inf spec(A_λ) **decreasing in λ**
(CCM-ZST eq. (3.27), via Doc 99), and

$$\lim_{\lambda\to\infty}\mu_\lambda \geq 0 \iff \mathrm{RH}$$

(⟸: restricted Weil criterion; ⟹: CCM-ZST Cor. 3.8; see Doc 99 §2.2).

Structural consequence: **the arithmetic family ζ_S → ζ_{S∪{p}} and the analytic
family λ → λ′ are the same family.** The prime p enters exactly when λ crosses
√p: the Euler filtration is realized as a continuous path of quadratic forms — the
canonical setting of spectral flow [Phi96], [RS95].

### 3.2. RH as vanishing spectral flow: exact theorem

Definition (standard, [Phi96]): for a path {B_t} of self-adjoint operators with
discrete semibounded spectrum, the spectral flow sf{B_t} through 0 is the net
number of eigenvalues crossing 0 downward minus upward, counted with
multiplicity. For our path the "entry count" version is convenient: since μ_λ is
monotonically decreasing, eigenvalues can only cross 0 downward.

**Theorem 3.2 (RH = zero spectral flow of the Euler filtration;
unconditional).** Let {A_λ}_{λ>1} be the CCM-ZST family. Then:

(a) Under RH, μ_λ ≥ 0 for all λ; no eigenvalue crosses 0;
sf{A_λ : λ ∈ (1,Λ]} = 0 for every Λ.

(b) Under ¬RH, there exists a **finite** λ₀ < ∞ such that μ_λ < 0 for all λ > λ₀:
the first crossing occurs at a finite parameter, and sf ≠ 0 already on the segment
(1, λ₀ + ε].

(c) Hence: RH ⟺ sf{A_λ} = 0 over every finite segment ⟺ the total spectral flow of
the Euler filtration is 0.

*Proof.* (a) RH ⟹ Weil positivity on C_c^∞(ℝ₊*) (Weil 1952; in the CC
normalization: Doc 100, Lemma 2.0) ⟹ QW_λ ≥ 0 for all λ (restriction of a
positive form) ⟹ μ_λ ≥ 0. (b) ¬RH ⟹ there exists f ∈ C_c^∞(ℝ₊*) with
QW(f,f) < 0 (Weil criterion, contrapositive); supp f ⊆ [λ₀^{-1}, λ₀] for some
finite λ₀; then μ_{λ₀} ≤ QW(f,f)/‖f‖² < 0, and by monotonicity μ_λ < 0 for λ ≥ λ₀.
Since μ_λ ≥ 0 for λ < √2 (BEFORE the first prime there are only polar/archimedean
terms: the archimedean positivity of CC 2021 covers support in (1/2,2) — Doc 100
§2), the path starts with μ ≥ 0 and ends with μ < 0: there is a crossing, sf ≠ 0.
(c) is (a)+(b). ∎

Three exact comments:

1. **The event is individual and finite.** Under ¬RH, the crossing occurs at
   finite λ₀, at the step where the window [λ₀^{-1}, λ₀] becomes able to resolve
   the off-critical zero: a countable event, of integer multiplicity, detectable
   by a computation (again: falsifiable, not certifiable).

2. **The per-prime-step flow is well defined.** sf_p := sf{A_λ : λ ∈ [√p, √p′]}
   (p′ = next prime) is an integer per step; RH ⟺ sf_p = 0 for every p AND no
   crossing at the limit. It is the "Euler filtration" version of the semilocal
   Maslov index of Doc 100 (§3, with its exhaustion lemma κ(Q) = lim_n
   κ(Q|_{𝒟_n}) proved there) and of object E5 of Doc 99 (κ_λ(N)).

3. **The base case is proved.** sf = 0 on the prime-free stretch (λ < √2) is the
   unconditional archimedean theorem (Yoshida 1992; Connes–Consani, Selecta 2021;
   Doc 100 §§2, 4: μ_∞ = 0 with operatorial mechanism). The first arithmetic step,
   sf₂ = 0 (a single prime), is exactly Conjecture 100.A — open, falsifiable,
   with infrastructure built in the literature (CCM 2024).

### 3.3. CF approximants have zero flow at every step — and why that does not sum up

Doc 99 (§§2–4, verified against CCM-ZST and CvS): the truncations QW_λ^N have
Loewner structure τ_ij = (b_i − b_j)/(i−j); generalized Carathéodory–Fejér rigidity
(Connes–van Suijlekom) applied to the shifted QW_λ^N − ε_N ≥ 0 produces
self-adjoint operators H_x whose regularized determinant has **all zeros real,
unconditionally, at every finite step**. *The spectrum of the approximants never
betrays the crossing*: negativity, if it exists, lives in μ_λ < 0 (the shift ε_N
absorbs it), not in non-real zeros of the approximant. The question — "do the CF
approximants have ZERO flow at every step, and is RH 'total flow of the filtration
= 0,' with the problem at the limit?" — is answered: **yes, and the problem at the
limit is MW-6 in literal form.**

**Proposition 3.4 (the telescoping sum does not converge without the uniform
gap).** Let sf_p be the per-prime-step flow (§3.2) and let sf^∞ be the flow of the
full path (equivalently, by the exhaustion lemma of Doc 100 §3, κ(Q) = 2m). Then:

(a) The telescoping identity sf^∞ = Σ_p sf_p holds **if** crossings occur at
finite parameters — and under ¬RH that is exactly what happens (Theorem 3.2(b)):
the series detects the crossing at the finite step p ≈ λ₀². There is no loss at
the limit here: ¬RH is visible in finite time.

(b) What is NOT computable is the value of each summand: certifying sf_p = 0
requires a lower bound μ_λ ≥ 0 on the stretch [√p, √p′], i.e., semilocal Weil
positivity with p primes — whose case p = 2 is already the open Conjecture 100.A,
and whose uniform version in p is lim μ_λ ≥ 0 = RH (semilocal MW-1 = MW-6; Doc 99
§2.2). The per-step flow is an individual integer whose per-step evaluation is a
per-step positivity problem, and the chain of per-step positivities, without a
uniform structural reason, is the Π₁ conjunction of Obs. 2.5 with another
coordinate.

(c) Approximation by finite truncations N adds the inner limit: the flow of
QW_λ^N converges to that of QW_λ if there is a uniform spectral gap in N around 0
(spectral flow is not continuous under strong resolvent convergence without a gap;
[Phi96] gives continuity IN the presence of a gap). The uniform bound of the
negative package κ_λ(N) is exactly object E5 of Doc 99, not initiated, with the
caveat recorded there: an unconditional increasing lower bound of κ_λ(N) surviving
N → ∞ would refute RH; an upper bound → 0 would prove it. OPEN GAP in both
directions.

*Proof.* (a): Theorem 3.2(b) + additivity of flow under path concatenation
[Phi96]. (b): sf_p = 0 ⟺ μ_{√p′} ≥ 0 (monotonicity) = positivity of QW with
primes ≤ p′; the identification with 100.A and MW-6 is Doc 100 §6 and Doc 99
§2.2. (c): standard counterexamples to discontinuity of the flow without a gap;
the sufficient gap condition is [Phi96]. ∎

### 3.5. What, then, does the spectral flow of the Euler filtration mean

Synthesis of front (ii): spectral flow IS the right invariant in a precise sense —
it reformulates RH **exactly** (Theorem 3.2, unconditional, new in this form even
though assembled from known pieces), turns ¬RH into an individual event with a
finite parameter, and decomposes RH into per-prime-step integers. Where it dies:
each per-step integer is a semilocal positivity with no local reason forcing it.
In function fields, what makes each step positive is not a step-by-step
computation but ONE local-geometric reason valid at all steps simultaneously —
the Castelnuovo inequality (Hodge index on C×C), from which Weil deduced RH for
curves [Wei48]. The spectral flow of the Euler filtration identifies the hole:
**what is missing is the analogue of "curvature is positive in every chart" — a
local theorem that annihilates every sf_p for the same reason.** It is not
averaging that is missing (the flow does not average); it is the local reason.
This feeds axiom L5 of §4.

---

## 4. (iii) The specification of the inertia reader

### 4.1. The axioms

**Definition 4.1 (inertia reader).** An *inertia reader* for ζ is an invariant I
with:

- **(L1) Quantization.** I takes values in ℤ (or a discrete group): it is not
  averageable; every continuous deformation of the data leaves it fixed or changes
  it by a detectable integer jump.
- **(L2) Autonomy of the value.** I is computable from unconditional arithmetic
  data — primes, pole, gamma factor — WITHOUT zero positions (as a functional of
  the arithmetic blocks of an explicit formula, or of an object built functorially
  from Spec ℤ).
- **(L3) Detection of inertia.** I = 0 ⟺ m = 0; better still, I = 2m = κ(Q) (P35).
  I reads the signature, not the trace.
- **(L4) Stability under computation.** I is stable under the deformations that
  computation involves — prime truncation (Euler filtration), rank truncation (N
  finite), window limits — WITHOUT an RH-equivalent uniformity (without MW-6 as a
  toll).
- **(L5) Localization.** I satisfies an index theorem: I = Σ computable local
  contributions, of Atiyah–Singer type (analytic index = topological) or of
  Castelnuovo type (local positivity ⟹ global vanishing for the same reason at
  every place). This is the axiom §3.5 showed to be missing in the Euler flow.
- **(L6) A priori finiteness.** I factors through an object of finite dimension,
  bounded by arithmetic data (NOT by zero positions), with arithmetically
  computable traces on that object.

L1–L5 are the refined version of the objective's list (L2 fixes "computable"; L4
names the forbidden toll; L5 admits the Castelnuovo variant in addition to AS). L6
is this document's addition, and §§4.2–4.4 show it is the decisive axiom: without
it, L2+L3+L4 are inconsistent in the class where the program has worked; with it,
consistent by an elementary mechanism.

### 4.2. The tension (L2)+(L3): formulation of the impossibility theorem

Doc 108 proved, for Q₂: autonomous value, non-autonomous inertia (the off×off /
off×on partition requires positions; P43 §4). Accident of Q₂, or impossibility
theorem? Let us fix the class frankly.

**Definition 4.2 (class ℱ of arithmetic quadratic functionals).** ℱ consists of
invariants of the form I = neg.ind(Q|_{V′}), where:

(i) Q is a Hermitian form on a space of test functions 𝒱 with an explicit-formula-
type identity: spectral side = sum over (tuples of) zeros of evaluations of the
Mellin transform of the tests, arithmetic side = finite sum of blocks computable
from primes/pole/gamma (the program's realizations: the one-variable Weil form
[Doc 91], W₂ and Q₂ [Doc 107], the W_k [Doc 107 §6.5], the semilocal forms QW_λ
[Doc 99]);

(ii) V′ ⊆ 𝒱 is **test-accessible**: specified without zero positions (by
supports, frequency windows, norms — Doc 108, Def. 1.2).

**Theorem 4.3 (impossibility in ℱ).** No I ∈ ℱ satisfies (L2), (L3), and (L4)
simultaneously. More precisely, the resolution dichotomy holds:

(a) *Sub-resolution regime.* If V′ has bounded resolution (fixed-support tests a,
height windows T → ∞), then I(V′) = 0 **unconditionally** for T ≥ T₀(a) — in both
worlds (Doc 108, Theorem 3.3: AA ∼ c(log T)² dominates all blocks, the form is
positive definite on those tests). A sub-resolution I violates (L3): it does not
detect m.

(b) *Resolution regime.* If V′ resolves individual zeros (bandwidth ≲ 1/log T,
i.e., support a ≳ log T), then I is **binary**: 0 in every window under RH, and
≍ m·n_W ≍ m·log T with no bound over windows under ¬RH, due to off×on
contamination (Doc 108, Prop. 2.3 + Lemma 2.4 + Prop. 2.5; in one variable: Doc
107 Prop. 6.1 and Doc 96 Theorem 8.1 — the global index is ∞ under ¬RH and only
the relative block is finite). Then: either I is defined as a per-window index —
and any finite uniform bound on I is logically equivalent to RH (Prop. 2.5 Doc
108), violating (L4) (the required uniform stability IS RH) — or I is defined as
the off×off relative block (finite, = 8m² for Q₂) — and then the compression that
defines it uses zero positions, violating (L2): the relative block is not
test-accessible (Doc 108 §2.4, structural GAP declared there).

(c) *There is no third regime:* evaluating any I ∈ ℱ with (L3) in regime (b)
requires localizing the arithmetic deficit Π with relative precision o(1/log T)
uniform over windows, which implies RH (two-worlds argument: Doc 108, Theorem 3.4
and Theorem 4.3).

**Status of the proof — stated exactly.** (a) and (c) are theorems of Doc 108
(3.3, 3.4, 4.3) for the program's forms cited in 4.2(i); the extension to the W_k
is mechanical (Doc 108, Prop. 7.3), but is NOT written for an arbitrary axiomatic
class: in the literal generality of 4.2 the statement is a **theorem for the
program's realizations + a scheme for the class** (the ingredients — positive
on×on sea, off×on contamination by free orbits, hierarchy AA ≫ rest in
sub-resolution — depend only on the structure "explicit formula + involution
ρ ↦ 1−ρ̄," but we do not fabricate the general theorem). (b) inherits the caveat
from Doc 108: realizability over the test class (Lemma 2.4 there) is proved in the
toy case under Hypothesis D. GAP declared: general axiomatic class and general m
without Hypothesis D.

**Corollary 4.4 (reading).** In the category where the program has spent three
phases (quadratic forms with an arithmetic side and test-accessible compressions)
the wall is total: the inertia of ANY arithmetic quadratic functional is either
non-autonomous, non-detecting, or RH-tolled. The inertia reader, if it exists, is
of another category. The formula of Doc 108 §7.4 is promoted to a class
principle, with the status stated above.

### 4.3. The abstract counterexample: finite rank

Does the specification refute anything? Yes — and the counterexample is
elementary, which is exactly the clue.

**Proposition 4.5 (in finite rank, the inertia IS autonomous from the value).**
Let Q be a Hermitian form on a space of finite dimension n, with n known a
priori. Then the inertia (p, q) of Q is determined by the n values
t_j = tr(Q^j), j = 1, …, n. In particular: if the traces of powers are
computable from arithmetic data, the signature — the individual datum, the
inertia — is computable from arithmetic data, by an integer, stable, and local
procedure in the t_j.

*Proof.* Newton's identities recover the coefficients of the characteristic
polynomial of Q from t_1, …, t_n; the eigenvalues are real (Q Hermitian); the
number of negative roots of a real polynomial with all real roots is read off from
the signs of the coefficients (Descartes' rule of signs, exact when all roots are
real) or, equivalently, the signature is read off from the Hankel form of the
power sums (Jacobi–Frobenius theorem; [Gan59, Vol. 2, Ch. X]). All steps are
algebraic in the t_j. ∎

Proposition 4.5 does not contradict Theorem 4.3: the forms in ℱ have infinite
rank (or relative finite rank defined by zero positions — precisely the
non-autonomous part). The isolated contrast:

> **Computing a trace is averaging; computing finitely many traces of an object of
> known finite rank is individuating.** The value/inertia boundary is not the
> trace/signature boundary: it is the infinite-rank/a-priori-finite-rank boundary.
> In finite dimension the average determines the individual because there are
> finitely many individuals and finitely many independent averages.

**Corollary 4.6 (conditioned consistency of the specification).** (L1)–(L5) plus
(L6) are consistent: the abstract model of Prop. 4.5 satisfies all of them (with
L5 trivialized by finite dimension). (L1)–(L5) without (L6), within ℱ, are
inconsistent (Theorem 4.3). Hence the entire content of the search for the
inertia reader reduces to:

> **(L6) as the missing theorem: a FINITENESS.** There exists an object of finite
> dimension bounded a priori by arithmetic data (not by zeros), whose traces are
> arithmetically computable (a Lefschetz formula), and whose signature/inertia is
> equivalent to 2m.

This is exactly what ℓ-adic cohomology provides in function fields: dim H¹ = 2g —
computable from the geometric datum WITHOUT knowing the zeros — and
tr(Frob^n | H¹) = point count (Lefschetz; [Wei48], [Del74]): finitely many
arithmetic traces of an a priori finite-rank object. Prop. 4.5 is the algebraic
reason why, with that in hand, the individual zeros (Frobenius eigenvalues) are
determined by averages (point counts): **in function fields the master quantifier
is crossed by finiteness, not by a better estimate.** The remaining step
(|α_i| = q^{1/2}) additionally required a positivity (Castelnuovo for Weil, Rankin
for Deligne) — L3+L5 on our list. Without finiteness, the question is not even
posed.

### 4.4. Final refinement of the tension (2)+(3)

Answer to the central question: (L1)–(L5) is NOT internally consistent in the
class where the program can instantiate it today (Theorem 4.3), and IS consistent
in the abstract — the counterexample is finite rank (Prop. 4.5). The
impossibility theorem does not say "there is no inertia reader"; it says: **the
inertia reader is not a compressed quadratic form — it is a finiteness theorem
with a trace formula.** The right category is not (forms, compressions, negative
indices) but (coherent object of finite rank, Frobenius, Lefschetz, Hodge
positivity). The wall, seen from here, has a classical name: the absence of a
Weil cohomology for Spec ℤ.

---

## 5. (iv) K-theory and the site: frank inventory against the specification

Without re-deriving MW-5 (NO-GO-LIST; Phase 27): the local-global factorization of
the zero side requires (1) a cohomology H¹(Spec ℤ, F), (2) a Frobenius per place,
(3) a positive intersection form. Here we only measure the Connes–Consani program
against L1–L6.

**5.1. What they have** (items with an asterisk were verified against source in
Docs 99/100; the rest are cited from their published data):

- The **arithmetic site** (C.R.A.S. 352, 2014; Adv. Math. 291, 2016): the space of
  points over ℝ₊^max recovers ℚ^×\𝔸_ℚ/ẑ^× with its scaling flow — the
  "Frobenius" is a one-real-parameter flow, not a discrete endomorphism.
- The **scaling site** and its tropical Riemann–Roch (C.R.A.S. 354, 2016; Selecta
  23, 2017): divisors, degree and RR over the tropical curves C_p = ℝ₊^*/p^ℤ; the
  declared strategy is to replicate the Weil/Mattuck–Tate–Grothendieck proof over
  the square of the site (*The Riemann–Roch strategy*, Springer 2019) [editorial
  data NOT VERIFIED in detail].
- (*) **Archimedean and semilocal positivity**: Selecta 27 (2021,
  arXiv:2006.13771); J. Number Theory 2021 (arXiv:2008.10974); CCM, Ann. Funct.
  Anal. 2024 (arXiv:2310.18423) — verified in Doc 100.
- (*) The **zeta spectral triples** (CCM-ZST, arXiv:2511.22755) and CF rigidity
  (Connes–van Suijlekom, CMP 406:312, 2025) — verified in Doc 99.

**5.2. The measurement against L1–L6.**

| axiom | status in the CC program | comment |
|---|---|---|
| L1 (integer) | ✓ in the tropical RR (degrees, dimensions) | the site invariants are integer/quantized |
| L2 (autonomous value) | ✓ | the whole construction is functorial from the arithmetic data; no input of zero positions |
| L3 (detects inertia) | ✗ | no site invariant has been connected to m or to κ(Q); the proved positivity (2021–2024) is per semilocal window, not a global signature |
| L4 (stable without RH toll) | ✗ (it is MW-6) | the semilocal → global step is lim μ_λ ≥ 0 = RH; Doc 100 measured it as Obstacle O_SL |
| L5 (localization) | partial | the geometric side of the explicit formula IS additive over places (unconditional — Doc 100 §5); the local reason for per-place positivity is missing |
| **L6 (finiteness + traces)** | **✗ — the exact hole** | there is no finite-dimensional H¹ with a Lefschetz formula: tropical RR produces an Euler characteristic (a VALUE: difference of dimensions, K-theory), not a signature over a finite space with Frobenius; the "Frobenius" is a continuous flow, with no integer weight structure |

Row L6 is the answer to the objective's question ("what exactly is missing for
their H¹ to count zeros individually?"): **what is missing is the finiteness
theorem with a trace formula — the analogue of Grothendieck's pair (finiteness of
cohomology, Lefschetz) — and, on top of it, positivity (L3/L5) — the analogue of
the Hodge index.** In char p, that second floor is the still-open part of the
standard conjectures [Gro69], [Ser60]; Deligne dodged it with the Rankin argument
(squaring to gain half a weight per iteration, [Del74]) — which works because the
dimensions are finite and the weights multiply in the tensors.

**Observation 5.3 (Form B was Deligne's trick without finiteness).** The
program's tensor amplification — κ(ψ^{⊗k}) = ½(4m)^k (Doc 106; ledger L3 of
P43) — is structurally Rankin–Deligne squaring: tensoring to amplify the defect
until it becomes visible against the main term. It died (Doc 108, Prop. 7.3)
because the comparison mass (the on×on sea, n_W^k) grows at the same rate as the
signal: in infinite rank, amplifying the numerator amplifies the denominator. In
Deligne, the denominator is PINNED by finiteness (dim H^i fixed, independent of
the twist): the amplification wins because it iterates against a fixed bound.
Diagnosis: **Form B = Deligne's method − L6** — the identification of the single
ingredient whose absence flipped the result. The inertia reader CC are looking
for and the one Form B needed are the same object, and the axiom neither
satisfies is the same (L6).

---

## 6. (v) Everything through the master quantifier

We apply the Master Principle (P43, Principle 3.1) to each candidate. Columns:
object controlled unconditionally / RH-equivalent refinement / where the
inversion sits.

| candidate | controlled (average/generic/interior) | RH-equivalent (individual/uniform/boundary) | the inversion |
|---|---|---|---|
| winding number N_off(R) | ∫_σ N_off(σ,T)dσ (Littlewood → density); moments of S (Selberg); each FIXED box by computation (Turing) | N_off(R) = 0 for EVERY box | average in σ/t → individual box; Π₁ conjunction with no uniform reason (Lemma 2.4, Obs. 2.5) |
| parity / mod k | parity of symmetric boxes (≡ 0, both worlds); parity of N(T) (sign of Z) | parity of N_off = inertia mod 2: on/off partition | the parity forced by symmetry is constant = no information; the informative one requires the partition (Obs. 2.7) |
| spectral flow of Euler | sf of every CF approximant = 0 (rigidity, every finite step); μ_λ per step, in principle computable | sf_p = 0 for EVERY p + limit (uniform gap) | per-step positivity with no local reason; MW-6 at the inner limit (Prop. 3.4) |
| index of quadratic forms (ℱ) | the VALUE of Q (autonomous); sub-resolution indices (= 0 unconditionally) | the per-window INERTIA (binary: 0 vs ≍ m log T) | Theorem 4.3: (L2)+(L3)+(L4) inconsistent in ℱ |
| K-theory / CC site | tropical Euler characteristic, semilocal per-window positivity | global signature of a finite H¹ with Lefschetz | L6 absent: without finiteness, the available integer is a value, not an inertia (§5.2) |

Verdict: **no candidate escapes the quantifier, and the way it falls is
informative.** The topological candidates do not fall by averaging — they do not
average — but by EVALUATION: the integer exists and is decidable event by event,
but the only unconditional evaluation machinery is averaged, and the alternative
is the infinite conjunction with no local reason. This refines P43: for quantized
invariants the wall is not "they average"; it is **"there is no localization
(L5) nor finiteness (L6) that evaluates the integer once and for all
instances."** The quantifier inversion reappears as the step from "each integer,
by computation" to "all of them, by a reason" — the Π₁ form of the wall. In the
one historical instance that was won, the reason was cohomological: finiteness +
Lefschetz + local positivity.

---

## 7. (vi) VERDICT

### 7.1. Final specification of the inertia reader

An invariant I that crosses the wall must satisfy **L1–L6** (§4.1), with the
logical structure proved in this document:

- (L1–L4) without L6 is **inconsistent** in class ℱ (Theorem 4.3; status: theorem
  for the program's realizations, scheme for the axiomatic class, toy-case
  caveats declared).
- (L1–L6) is **consistent** (Prop. 4.5: in a priori finite rank, finitely many
  traces determine the inertia — Newton / Jacobi–Frobenius).
- The operative specification thus compresses into **L6 + Lefschetz + local
  positivity (L3/L5)** — a Weil cohomology for Spec ℤ: an a priori arithmetically
  bounded finite-rank object, an arithmetic trace formula, local positivity
  annihilating the per-step flow. The other axioms come for free (Prop. 4.5
  gives L1, L2, L4 from L6 + traces).

### 7.2. Status of the impossibility theorem

**Proved within its class, with an exact boundary.** The inertia of any
arithmetic quadratic functional of the program's type is non-autonomous
(Theorem 4.3, via the sub-resolution/resolution dichotomy of Doc 108); the
abstract refutation of the general impossibility is elementary (finite rank,
Prop. 4.5); the combination localizes the wall in finiteness, not in
quadraticity nor in positivity. The clue from the counterexample: the reader is
not sought by improving estimates in infinite rank — it is sought by proving
that the problem LIVES in finite rank (a Grothendieck-style coherence/finiteness
over the right site). OPEN GAP (the usual one, in new coordinates): that
finiteness theorem does not exist; it is MW-5, item (1), promoted from
"ingredient" to "the only ingredient."

### 7.3. Most promising falsifiable statement

Two levels, from the closest to the most structural:

1. **(Falsifiable already, published infrastructure.) Effective Conjecture
   100.A, read as spectral flow:** sf{A_λ : λ ∈ (1, √3]} = 0, i.e., μ_λ ≥ 0 up to
   and including the prime 2 — in quantitative form, with explicit gap
   μ_λ ≥ c₂ > 0. It is the first nontrivial integer of the Euler filtration
   (Theorem 3.2 + Doc 100 §6); its falsification would refute semilocal Weil
   positivity at its first step; its proof would be the first per-step
   positivity theorem — the seed of the local reason L5 calls for. Each
   additional step (sf_p = 0 with subexponential gap c_p) is a frank partial
   theorem; uniformity in p is MW-6, declared as a wall.

2. **(Structural target, D108 §8.2, reformulated as a winding number.) Linear
   bound on the per-window winding number:** κ_W ≤ C·n_W with absolute C, which
   would imply m ≤ C/2 — an ABSOLUTE bound on the number of off-critical
   quadruples, weaker than RH and stronger than any known density result. It sits
   behind the same second-order wall (D108 §8.1), but it is the only identified
   intermediate statement that a partial inertia reader (without complete L6)
   could reach.

### 7.4. Verdict

**VERDICT: PARTIAL.**

- **NO CANDIDATE built:** none of the invariants that count one by one (winding
  number, parity, spectral flow, form indices, K-theory of the site) today reads
  the inertia of ζ; the document locates the failure point of each one
  (Lemma 2.4, Prop. 2.6/Obs. 2.7, Prop. 3.4, Theorem 4.3, §5.2).
- **WITH a closed and non-empty specification:** L1–L6, consistent (Prop. 4.5),
  inconsistent without L6 in the program's class (Theorem 4.3), equivalent in
  practice to a Weil cohomology for Spec ℤ; with two new identifications: Form B
  was Deligne's method minus finiteness (Obs. 5.3), and the spectral flow of the
  Euler filtration reformulates RH exactly (Theorem 3.2) — the ¬RH event is
  individual and has a finite parameter; what is missing is not individuality
  but a local reason valid at every step.
- The conceptual residue for Phase 37: **an integer is not averaged: it is
  read — but reading it uniformly requires finiteness (L6) or localization
  (L5). Physics calls that "protected topological charge": the protection, not
  the charge, is what ζ does not yet have.**

---

## References

**Internal (backward-only):** P43 (§3 Master Principle, §4 value/inertia, §6
boundary); P42 (§6 Missing Lemma 6.1); P41 (interior/boundary no-go); P35
(κ(Q) = 2m); Doc 108 (Theorems 3.3, 3.4, 4.3; Prop. 2.3, 2.5; Lemma 2.4; §§7.4,
8.1–8.2); Doc 107 (W₂, Theorem 2.4, Prop. 6.1, §6.5); Doc 106 (tensor identity,
Prop. 3.6); Doc 100 (Lemma 2.0, exhaustion lemma §3, μ_∞ = 0 §4, Obstacle O_SL
§5, Conjecture 100.A §6); Doc 99 (CCM-ZST §2, CF rigidity §§3–4, E5 κ_λ(N)); Doc
96 (Theorem 8.1); Doc 91 (Weil form, Prop. 4.5); NO-GO-LIST (MW-1…MW-7).

**Literature (verifiable):**
- [APS76] M. F. Atiyah, V. K. Patodi, I. M. Singer, *Spectral asymmetry and
  Riemannian geometry III*, Math. Proc. Cambridge Philos. Soc. 79 (1976), 71–99
  (spectral flow).
- [AS63] M. F. Atiyah, I. M. Singer, *The index of elliptic operators on compact
  manifolds*, Bull. Amer. Math. Soc. 69 (1963), 422–433.
- [Del74] P. Deligne, *La conjecture de Weil. I*, Publ. Math. IHÉS 43 (1974),
  273–307 (Rankin/squaring argument).
- [Gan59] F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Ch. X
  (signature via Hankel forms of Newton sums; Jacobi–Frobenius).
- [Gro69] A. Grothendieck, *Standard conjectures on algebraic cycles*, in Algebraic
  Geometry (Bombay Colloquium 1968), Oxford Univ. Press, 1969, 193–199.
- [IK04] H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53,
  2004 (Thm. 5.8: N(T); Thm. 5.12 and Ch. 10: Littlewood's lemma and density).
- [Ing40] A. E. Ingham, *On the estimation of N(σ,T)*, Quart. J. Math. Oxford 11
  (1940), 291–292. (Littlewood 1924, S(T) under RH, cited via [Tit86, Thm.
  14.13].)
- [Phi96] J. Phillips, *Self-adjoint Fredholm operators and spectral flow*,
  Canad. Math. Bull. 39 (1996), 460–467.
- [PT21] D. J. Platt, T. S. Trudgian, *The Riemann hypothesis is true up to
  3·10¹²*, Bull. London Math. Soc. 53 (2021), 792–797.
- [RS95] J. Robbin, D. Salamon, *The spectral flow and the Maslov index*, Bull.
  London Math. Soc. 27 (1995), 1–33.
- [Sel46] A. Selberg, *Contributions to the theory of the Riemann zeta-function*,
  Arch. Math. Naturvid. 48 (1946), 89–155 (moments of S(T)).
- [Ser60] J.-P. Serre, *Analogues kählériens de certaines conjectures de Weil*,
  Ann. of Math. 71 (1960), 392–394.
- [Tit86] E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed.
  (rev. D. R. Heath-Brown), Oxford Univ. Press, 1986 (§2.12; Thm. 9.4: S(T) =
  O(log T); §9.9: Littlewood's lemma and S₁(T); Thm. 14.13).
- [Tur53] A. M. Turing, *Some calculations of the Riemann zeta-function*, Proc.
  London Math. Soc. (3) 3 (1953), 99–117.
- [Wei48] A. Weil, *Sur les courbes algébriques et les variétés qui s'en
  déduisent*, Hermann, Paris, 1948 (RH for curves via Castelnuovo/Hodge index).
- Connes–Consani: *The Arithmetic Site*, C. R. Acad. Sci. Paris 352 (2014),
  971–975; *Geometry of the Arithmetic Site*, Adv. Math. 291 (2016), 274–329;
  *The Scaling Site*, C. R. Acad. Sci. Paris 354 (2016), 1–6; *Geometry of the
  Scaling Site*, Selecta Math. (N.S.) 23 (2017), 1803–1850; *The Riemann–Roch
  Strategy: Complex Lift of the Scaling Site*, in Advances in Noncommutative
  Geometry, Springer, 2019 [editorial data NOT VERIFIED in detail];
  *Weil positivity and trace formula: the archimedean place*, Selecta Math. 27
  (2021) (arXiv:2006.13771, verified in Doc 100); arXiv:2008.10974 (J. Number
  Theory 2021, verified in Doc 100).
- Connes–Consani–Moscovici: Ann. Funct. Anal. 2024 (arXiv:2310.18423, verified in
  Doc 100); *Zeta Spectral Triples* (arXiv:2511.22755, verified in Doc 99).
- A. Connes, W. D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the
  Spectral Action*, Commun. Math. Phys. 406:312 (2025) (arXiv:2511.23257,
  verified in Doc 99).
- H. Yoshida, archimedean positivity of the Weil form (1992), cited via
  Doc 100 §4 [exact bibliographic identification in Doc 100].

*End of Doc 110.*
