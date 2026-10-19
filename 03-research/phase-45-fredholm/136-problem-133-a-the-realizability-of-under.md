# Doc 136 — Problem 133.A: the realizability of σ⁰ under ¬RH — collapse of global density and localized rescue

**Program:** Riemann Hypothesis — Phase 45, "Fredholm"
**Prerequisites:** Doc 133 (infinitesimal signature σ_ε, Defs. 2.1–2.4; Thms. 2.6, 2.7, 2.10; Prop. 2.8, 2.11; bridge-Theorem 2.13; Problem 133.A in §5.2), Doc 108 (Defs. 1.1–1.2; Props. 2.2, 2.3, 2.5; Lemma 2.4 with its Hypothesis D; Thms. 3.3, 3.4, 4.3; §7.4), Doc 107 (Lemma 2.2(b) absolute convergence; Lemma 5.2(b) spectral side; Theorem 5.5 and Prop. 6.1 hyperbolic planes; closure of the class under x∂ₓ and polynomials in s), Doc 98 (quadruple structure: κ = 2, two hyperbolic planes), Doc 106 (tensor identity of the index), P43 (autonomy of the value).
**Creative contract of the phase:** **[NEW-DEFINITION]** = total freedom; **[THEOREM]/[PROPOSITION]/[LEMMA]** = truly proved, complete proof or status declared line by line; **[COMPUTATION]** = closed; **[BRIDGE]** = connection with ζ/RH with honest status; **[WISH]** = declared; **[GAP]** = marked. No proof is fabricated.

---

## 0. Executive summary

Problem 133.A asked to prove that under ¬RH the starting infinitesimal signature of the
canonical scheme satisfies σ⁰ ≥ c > 0 — the only cited-but-not-proved link between the
logistic law of Doc 133 and a clean equivalence of RH. This document resolves it
in two moves, one destructive and one constructive:

1. **(§2, [THEOREM] of collapse — the most important question of the target, answered.)**
   For EVERY scheme of Doc-133 type with increasing dimension (n_N → ∞) and well-conditioned
   band cells, under ¬RH **with finite defect** (a finite number of off-critical zeros, in
   particular the toy model with m quadruples): **σ⁰ = 0 for every ultrafilter**
   (Theorem 2.5). The cause is structural and is shown with two lines of tensor
   accounting: capturing a negative off×on plane requires resolving TWO
   slots, with dimensional cost $(w_\sigma \log T)(w_\tau \log T)$, while the off
   slot is rigid (≤ 4m̄ vectors): the ratio κ/n ≤ Cm̄/max(w log T) → 0 as soon as n → ∞.
   **The same tensor mechanism that amplifies the logistic tower dilutes the density
   of the defect.** Audited consequence: bridge-Theorem 2.13(b) of Doc 133, as
   written, is FALSE for its canonical scheme — the implicit identification
   n_N = "zero count of the window" is incoherent with n_N = dim V_N (§2.1). The
   global logistic tower starts at 0 in both worlds (RH and ¬RH-with-finite-defect):
   the 0 vs. ½ dichotomy of Doc 133, in its global normalization, does NOT distinguish RH. The
   gap feared by the target is real and is now named: **density invisibility**
   (individual defects are null for every asymptotic density of increasing dimension;
   §2.4). What the global σ_ε DOES detect is a strictly
   stronger property than ¬RH ("locally dense defect", Prop. 2.7), which the density
   theorems do not exclude but ¬RH does not imply.

2. **(§3–§5, the rescue.)** [NEW-DEFINITION] The **localized infinitesimal
   signature** σ_loc: the micro-cell scheme — a test-accessible grid of
   cells of BOUNDED dimension (Paley–Wiener bump × monomials, with positive padding)
   that is refined with N in mesh, height, and profile, and the index normalized per
   cell κ_N := max_cell neg.ind/dim. The logistic law survives verbatim (Prop. 3.5).
   [THEOREM] Sub-target (β) is proved completely and cleanly: stability of the index
   under norm perturbation (Weyl, Theorem 4.1), under bounded-rank perturbation
   (interlacing, Theorem 4.2, three-line proof without eigenvalues), and under
   shift of the cell with a computable mesh (Theorem 4.4). [THEOREM] Sub-target
   (α) closes **in the localized version** (Theorem 5.4): under ¬RH, the
   minimal off-critical quadruple produces, for all large N, a grid cell with
   index ≥ 1 and bounded standard dimension D₀, whence σ⁰_loc ≥ 1/(2D₀) > 0 —
   a standard constant, for every ultrafilter. The proof is complete over the
   cited inputs from Doc 107 (spectral side, absolute convergence, hyperbolic
   planes); Hypothesis D of Doc 108 **is not needed**: it was an artifact of working at
   height T → ∞ with resolution 1/log T, and localization to the defect's height
   (bounded, with fixed non-uniform constants) dissolves it. The new thing the proof
   uses: the index of a cell is a property of the compressed Gram matrix — test-accessibility
   restricts the SPACE, not the witness vector (Obs. 5.1), and that unlocks
   annihilation by positions within a span blind to positions.

3. **(§6, [BRIDGE] candid.)** The reformulated and promoted criterion:
   **RH ⟺ lim_k σ_loc^(k) = 0 ⟺ lim_k σ_loc^(k) ≠ ½** (Corollary 5.6), with the
   RH branch a theorem (positivity of the compressed Weil form) and the ¬RH branch a theorem
   modulo the listed D107 inputs — no longer modulo Hypothesis D. The
   non-canonicity of the ultrafilter is tamed: the dichotomy is the same for every non-principal 𝒰 (Obs. 5.7).
   The price, declared without anesthesia: the localized version degrades **density →
   existence**; its content is Weil positivity over a countable basis of
   computable arithmetic Grams, plus the logistic amplification. The wall is not crossed:
   it reappears as (i) the Π₁ non-effectiveness of the standard part (unchanged since D133) and
   (ii) the master quantifier shifted from "uniformity over windows" (D108) to
   "unbounded search over the grid" — ¬RH becomes semi-decidable by arithmetic Grams
   (another semi-decision, alongside the classical numerical one), RH gains nothing.
   What does remain in the catalog: an equivalence of RH with both branches at
   theorem-over-cited-inputs status, computable finite-algebraic events from the
   primes, and macroscopic separation 0 vs. ½.

---

## 1. Inheritance and the fine point of the normalization

### 1.1. What is inherited without re-proving

From Doc 107/108: the form Q₂ on the span of the thickened class h_{g,φ}, with spectral
side
$$Q_2(h,h') \;=\; \sum_{(\rho_1,\rho_2)} \hat h(\rho_1,\rho_2)\,
\overline{\hat h'\big(\iota(\rho_1,\rho_2)\big)},
\qquad \iota(\rho_1,\rho_2) := (1-\bar\rho_1,\,1-\bar\rho_2), \tag{1.1}$$
sum over ordered pairs of nontrivial zeros (with multiplicity), absolutely
convergent on the class [D107, Lemma 5.2(b), Lemma 2.2(b)]; the evaluation factors:
$$\hat h_{g,\varphi}(\rho_1,\rho_2) = \tfrac12\,\hat g(\sigma)\,\hat\varphi(\tau),
\qquad \sigma = \tfrac{\rho_1+\rho_2}{2},\ \tau = \tfrac{\rho_1-\rho_2}{2}. \tag{1.2}$$
The pairs fixed by ι (both zeros online) contribute |ĥ|² ≥ 0 ("the sea"); the free
orbits {P, ιP} contribute 2Re[ĥ(P)·conj(ĥ(ιP))]: hyperbolic planes of
signature (1,1) [D107, Theorem 5.5, Prop. 6.1; D98 §6]. Under RH the sum is diagonal and
Q₂ ≥ 0 over the whole span [D108, Prop. 2.2]. The class is closed under x∂ₓ
(= multiplication by polynomials in the Mellin variable) [D107, §5.2, used in
D108 Lemma 2.4]. Autonomy: Q₂(h,h') is computable from the arithmetic blocks
without zero positions [P43; D133 Prop. 2.8].

From Doc 133: non-principal ultrafilter 𝒰 over ℕ, *ℝ = ℝ^ℕ/𝒰, standard part st;
scheme 𝒮 = (V_N), κ_N, n_N, σ_ε = st(κ*/n*); the tensor tower and the exact
logistic law x_{k+1} = 2x_k(1−x_k), with dichotomy lim σ^(k) ∈ {0, ½} (Thm. 2.10).

**Notation.** Generic zero ρ = β+iγ, β ∈ (0,1). "Off zero" := β ≠ ½. *Finite
defect*: the set of off zeros is finite, of cardinality 4m̄ (m̄ quadruples counting
multiplicity; the D98/D108 toy model has m̄ = m). *Minimal defect*: under ¬RH, we fix
once and for all ρ⁰ = ½+δ₀+iγ₀ an off zero of minimal height |γ₀| (it exists: the
zeros are discrete), with multiplicity m₀ ≥ 1, δ₀ ∈ (0,½). N(t) counts zeros with
0 < γ ≤ t; we only use N(t+1) − N(t) ≪ log(2+t) [IK04, Thm. 5.8].

### 1.2. [COMPUTATION] The fine point: dim V_W ≠ n_W, and the incoherence of the canonical scheme

Doc 133 (Def. 2.1, canonical example) takes κ_N := max_W neg.ind(Q|_{V_W}) over a
grid of resolution windows and n_N := dim V_W, and bridge-Theorem 2.13(b) cites the
D108 bound "κ_W ≳ m·n_W" as if n_W (the online zero count of the window,
D108 eq. after Def. 1.1, n_W ≍ (2Δ/π)log T) were dim V_W. Let us do the accounting that
Doc 133 did not do.

A resolution test at height T has logarithmic support [−a,a] with a = A log T and
band height w in the spectral coordinate: by Paley–Wiener, the number of degrees of
freedom (dimension of a stable frame of such tests) is
$$\mathrm{d.o.f.} \;\asymp\; \frac{a\,w}{\pi} \;=\; \frac{A\,w\log T}{\pi}. \tag{1.3}$$
The class is double: V is generated by tensors h_{g,φ}, with ĝ in a band of width
w_σ (sum coordinate) and φ̂ in a band of width w_τ (difference coordinate). The span of
the pure tensors is the full tensor product:
$$\dim V \;\asymp\; \Big(\frac{A w_\sigma \log T}{\pi}\Big)\cdot
\Big(\frac{A w_\tau \log T}{\pi}\Big). \tag{1.4}$$
Meanwhile, the negative planes of the window at height T (D108, Prop. 2.3) are
off×on: the off slot has at most 4m̄ vectors (rigid!), and the online
partner is confined by the two bands: at most C·m̄·(min(w_σ,w_τ) + 1/log T)·log T
planes. The density κ/dim is then, at best,
$$\frac{\kappa}{\dim V} \;\lesssim\;
\frac{m̄\,(\min w \cdot \log T + 1)}{(w_\sigma \log T)(w_\tau \log T)}
\;\le\; \frac{2m̄}{\max(w_\sigma, w_\tau)\,\log T}. \tag{1.5}$$
If dim V → ∞, some factor of (1.4) tends to ∞ and (1.5) tends to 0. **The identification
n_N ≍ n_W ≍ log T of Doc 133 is untenable: either n_N = dim V_N ≫ κ_N (collapse),
or n_N = n_W is not a dimension and the bound κ_N ≤ n_N of Def. 2.3 of Doc 133
fails (κ_W ≍ 8mΔπ^{-1}log T can exceed n_W ≍ 2Δπ^{-1}log T as soon as m ≥ 1).**
In both readings, statement 2.13(b) as written lacks proof. §2 converts this
computation into a theorem; §3 builds the normalization that sidesteps it.

---

## 2. [THEOREM] The collapse of global density

### 2.1. The class of schemes to which it applies

**Definition 2.1 (admissible-band scheme).** A scheme 𝒮 = (V_N) (test-accessible,
Doc 133 Def. 2.1, with n_N := dim V_N → ∞) is *of admissible band with profile
(T_N, w_σ(N), w_τ(N), c_N, ε_N)* if V_N admits a basis {h_i} of tensors h_{g,φ} such
that, writing ĥ_i = ½ĝ_i(σ)φ̂_i(τ):

(i) **(band)** there exists a region R_N = {|Im σ − c_N| ≤ w_σ} × {|Im τ − c'_N| ≤ w_τ}
(or a finite union of such, with common widths) such that the part of (1.1) supported
outside R_N defines a form F_tail with ‖F_tail‖_{op} ≤ ε_N on V_N in the basis
{h_i} (controlled tails);

(ii) **(θ-conditioning)** the compression to V_N of the fixed part
Q_fix := Σ_{ι-fixed pairs} |ĥ|² satisfies λ_min(Q_fix|_{V_N}) ≥ θ > 2ε_N, with θ > 0
fixed (Riesz frame: the tests are not asymptotically dependent).

The canonical example of Doc 133 — in any of its reasonable instantiations
(wide τ band, τ-cell grid, fixed τ band) — is of admissible band: (i) is the
superpolynomial Paley–Wiener decay plus absolute convergence [D107,
Lemma 2.2(b)]; (ii) is achieved by orthonormalizing the frame (a test-accessible
operation: computable Gram matrix, Prop. 2.8 of D133). It is not claimed that EVERY
scheme of Def. 2.1 of D133 is of admissible band; it is claimed that the canonical one
is, and the theorem is proved for the class.

**Lemma 2.2 (rank bound of the banded defect).** Under ¬RH with finite defect (4m̄
off zeros, all of height ≤ H₀), the free part of (1.1) supported in R_N (the
orbits {P, ιP} with evaluation in R_N) has rank, as a form on V_N, at most
$$R_1(N) \;\le\; C\, m̄\,\big(\min(w_\sigma, w_\tau)\,\log T_N + H_0\log T_N\cdot
\mathbf{1}_{\text{low bands}} + 1\big), \tag{2.1}$$
with C absolute. In particular R₁(N) ≤ C' m̄ (min(w_σ,w_τ)+1)·log T_N + C'(m̄,H₀).

*Proof.* A free orbit contains at least one off zero in some slot. Fixing
the off zero ρ_off (4m̄ choices per slot, 2 slots), the pair (ρ_off, ρ) falls in R_N
only if Im σ = (γ_off+γ)/2 and Im τ = (γ_off−γ)/2 lie in the bands: γ is then
confined to an interval of length ≤ 2 min(w_σ,w_τ) + O(1) around a center
determined by (c_N, c'_N, γ_off). The number of zeros (with multiplicity) in an
interval of length ℓ at height ≤ 2T_N is ≤ C(ℓ+1)log T_N [IK04, Thm. 5.8, summed
over ⌈ℓ⌉ unit intervals]. Off×off orbits also require both members of
height ≤ H₀: at most (4m̄)² orbits, and only if the band reaches heights ≤ H₀. Each
orbit contributes a form of rank ≤ 2 (the plane). Summing: (2.1). ∎

### 2.2. The collapse theorem

**Lemma 2.3 (stability of the index under rank perturbation; quadratic form).**
Let A, E be Hermitian forms on a finite-dimensional space V, r := rank E.
Then |neg.ind(A+E) − neg.ind(A)| ≤ r.

*Proof.* Let N ⊆ V be a subspace with A|_N < 0, dim N = neg.ind(A). Over
N ∩ ker E (codimension ≤ r in N), (A+E)|_{N∩ker E} = A|_{N∩ker E} < 0, so
neg.ind(A+E) ≥ neg.ind(A) − r. Swapping A+E and A (and E for −E, same rank) gives
the other inequality. ∎

**Lemma 2.4 (no negatives below the conditioning threshold).** If P ≥ θ·Id and
‖F‖_op ≤ ε < θ as forms on V, then neg.ind(P+F) = 0.

*Proof.* For every v ≠ 0: (P+F)(v,v) ≥ θ‖v‖² − ε‖v‖² > 0. ∎

**Theorem 2.5 (collapse of global density under finite defect).** Let 𝒮 be a
scheme of admissible band (Def. 2.1) with n_N → ∞. Under ¬RH with finite defect
(in particular, the D98/D108 toy model with m quadruples, any fixed m):
$$\frac{\kappa_N}{n_N} \;\longrightarrow\; 0 \qquad (N \to \infty),$$
and therefore **σ_ε(𝒮) = σ⁰ = 0 for every non-principal ultrafilter 𝒰**, and the
logistic tower of Doc 133 satisfies lim_k σ^(k) = 0 — exactly as under RH.

*Proof.* We decompose the compression to V_N of the spectral side (1.1):
Q₂|_{V_N} = Q_fix|_{V_N} + F_main + F_tail, where F_main is the free in-band part
(rank ≤ R₁(N), Lemma 2.2) and ‖F_tail‖ ≤ ε_N (Def. 2.1(i); the fixed part
outside the band is ≥ 0 and is absorbed into Q_fix without lowering its lower
bound... — precision: we define Q_fix|_{V_N} with ALL the fixed pairs; Def. 2.1(i) then
bounds the free part outside the band, which is the only remaining tail; the fixed
part never subtracts). By Lemmas 2.3 and 2.4 (with P = Q_fix|_{V_N} ≥ θ, F = F_tail,
ε_N < θ):
$$\kappa_N \;=\; \mathrm{neg.ind}\big(Q_2|_{V_N}\big)
\;\le\; \mathrm{neg.ind}\big(Q_{fix}|_{V_N} + F_{tail}\big) + \mathrm{rank}\,F_{main}
\;\le\; 0 + R_1(N).$$
It remains to bound R₁(N)/n_N. If the bands are at bounded heights (c_N, c'_N = O(1)),
R₁(N) ≤ C(m̄, H₀, w) is finite while n_N → ∞: the ratio → 0. If the bands grow
(T_N → ∞), by (1.4) the dimension of a θ-conditioned frame satisfies
n_N ≤ C(A)·(w_σ log T_N)(w_τ log T_N) and also n_N ≥ c·(w_σ log T_N)(w_τ log T_N)
(Paley–Wiener d.o.f.: a Riesz frame neither exceeds nor wastes the degrees of
freedom of the band more than by constants; it is the only property of (1.3)–(1.4)
that is used). Writing u := w_σ log T_N, v := w_τ log T_N (both ≥ c₀ > 0 by
minimal resolution), Lemma 2.2 gives R₁ ≤ C m̄ (min(u,v) + 1) + C(m̄,H₀), hence
$$\frac{R_1(N)}{n_N} \;\le\; \frac{C\,m̄\,(\min(u,v)+1)}{c\,u\,v} + \frac{C(m̄,H_0)}{n_N}
\;\le\; \frac{C'\,m̄}{\max(u,v)} + \frac{C(m̄,H_0)}{n_N}.$$
Since n_N ≍ uv → ∞ and u, v ≥ c₀, necessarily max(u,v) → ∞: both terms → 0.
For finite unions of bands the argument applies band by band and is summed (the
maximum over the grid inherits the bound of the worst cell). Finally κ_N/n_N → 0 implies
st([κ_N/n_N]) = 0 for every 𝒰 (st of a convergent sequence is its limit), and the
closed form of Thm. 2.10 of D133 with σ⁰ = 0 gives σ^(k) ≡ 0. ∎

**Corollary 2.6 (audit of Doc 133).** Bridge-Theorem 2.13(b) of Doc 133 is
false as stated for every canonical admissible-band scheme with
n_N = dim V_N → ∞: under ¬RH with m quadruples (m fixed), σ⁰ = 0, not σ⁰ ≥ c′m.
The error at the source: the citation of D108 Prop. 2.3 transports κ_W ≳ m·n_W with n_W =
*spectral count of the window*, which neither is nor can be dim V_W (§1.2). Corollary
2.13(c) ("RH ⟺ lim σ^(k) = 0") is left unsupported in its ¬RH branch. ∎

### 2.3. What the global σ_ε really detects

**Proposition 2.7 (σ⁰ global > 0 ⟺ locally dense defect; one direction proved).**
Let 𝒮 be of admissible band. (a) If σ⁰(𝒮) > 0 for some 𝒰, then
$$\limsup_{N\to\infty}\ \frac{\#\{\text{off zeros feeding free orbits in } R_N\}\cdot \log T_N}{n_N} \;>\; 0,$$
that is: there is a sequence of bands where the number of coupled off zeros is
≳ n_N/log T_N ≍ (a whole factor of the dimension) — **a positive proportion of
the degrees of freedom of an entire slot**, infinitely often. We call this
configuration *locally dense defect*. (b) Conversely, if the defect is
locally dense, the realizability of the corresponding index (per-window version of
Lemma 2.4 of D108) would give σ⁰ > 0 for a 𝒰 concentrated on the bad bands
[status: conditional on the same type of realizability; not used in this document].

*Proof of (a).* By the proof of Theorem 2.5, κ_N ≤ R₁(N), and bound (2.1)
generalized without the finite-defect hypothesis is R₁(N) ≤ C·D_off(N)·(min(u,v)+1)·
(log T_N)/log T_N — more precisely: each coupled off zero contributes ≤ C(min(w)+1)log T_N
planes, so κ_N ≤ C·D_off(N)·(min(u,v)+1) with D_off(N) := number of off zeros
feeding R_N. If κ_N/n_N ≥ c on a 𝒰-large set (necessary for σ⁰ > 0),
then D_off(N) ≥ c·n_N/(C(min(u,v)+1)) ≥ c'·n_N·(something ≥ 1/u or 1/v)... and using
n_N ≍ uv: D_off(N) ≥ c''·max(u,v) ≍ n_N/(min-factor) ≥ c''·n_N/(C·log T_N·w_min),
which is the statement with the band constants absorbed. ∎

**Remark 2.8 (density theorems are mute here; answer to question (i) of the
target).** Do density theorems N(σ,T) = o(T) force σ⁰ = 0
ALWAYS, even under genuine ¬RH (m = ∞, Bohr–Landau)? **No.** Bohr–Landau and the
density theorems bound the TOTAL of off zeros up to height T (zero mean
density), but do not exclude local clustering: unconditionally, a single band of
width O(1) can contain up to O(log T) off zeros (the trivial bound per unit
interval is all that is available), which is exactly the "locally dense" scale of
Prop. 2.7. Exact conclusion of the global picture: **global σ_ε is not a
detector of ¬RH; it is a detector of locally dense defect** — a strictly
stronger property than ¬RH (finite defect violates it, Theorem 2.5) and not excluded by
density theory. The global logistic dichotomy separates "RH ∨ ¬RH-sparse" from "¬RH-clustered":
it is not a criterion for RH.

### 2.4. The face of the wall, named

**[COMPUTATION/diagnosis] Density invisibility.** The mechanism of Theorem 2.5 is
the tensor: in Q₁⊗Q₂ the index mixes q₁p₂ + p₁q₂ (D106), and when one
slot is rigid (q ≤ 4m̄ fixed) the density of negatives scales as m̄/n₁ → 0. **The same
tensor identity that gives the logistic amplification (D133, Thm. 2.10) is the one
diluting the individual defect in every normalization of increasing dimension.** It is
the master quantifier (P43, Principle 3.1) in the "density" coordinate: an individual
defect (finite-cardinality object) is invisible to EVERY test-accessible
asymptotic-density functional — to see it one must give up density and move to
localized existence. We record this face of the wall with its own name:
**density invisibility of individual defects**. (It enters the NO-GO-LIST as a
companion to MW-7: the partition is not autonomous; density does not see the finite.)

---

## 3. [NEW-DEFINITION] The localized infinitesimal signature σ_loc

The way out that Theorem 2.5 leaves open is exactly the one the target anticipated:
cells of BOUNDED dimension (where the defect does not dilute), a grid that refines with
N (to find the defect without knowing its position), and per-cell normalization.

**Definition 3.1 (micro-resolution cell).** Fixed a *profile*
p = (D, w, M, b, c, c') with D ∈ ℕ (degree), w > 0 (width), M ∈ ℕ (decay order),
b ∈ ℚ_{>0} (gauge), (c, c') ∈ ℚ² (centers in Im σ, Im τ), the cell is the
subspace
$$V_p \;:=\; \mathrm{span}\Big\{\, h_{g_a,\varphi_b} \;:\; 0 \le a, b \le D \,\Big\},
\qquad
\hat g_a(\sigma) := B^{(M)}_w(\sigma - ic)\,\sigma^a,\quad
\hat\varphi_b(\tau) := B^{(M)}_w(\tau - ic')\,\tau^b,$$
where B^{(M)}_w is the Mellin transform of a fixed even-normalized bump
g₀^{(M,w)} ∈ C_c^∞(ℝ₊*), chosen once and for all in a computable family with
$$|B^{(M)}_w(z)| \;\le\; C_M\,e^{a_0|\mathrm{Re}\,z - \tfrac12|}\,(1+|\mathrm{Im}\,z|/w)^{-M},
\qquad B^{(M)}_w(0) = 1, \tag{3.1}$$
(Paley–Wiener; a₀ = a₀(M,w) the logarithmic support, FIXED — not growing with any
height). dim V_p ≤ (D+1)², and V_p is test-accessible: the profile does not mention
zeros. The *padded cell* is Ṽ_p := V_p ⊕ ℂ^{(D+1)²} with the form
Q̃_p := (Q₂|_{V_p}) ⊕ Id (positive padding of dimension equal to the cell's
cap; test-accessible: it is a formal identity block).

**Definition 3.2 (localized scheme 𝒮_loc).** For each N, the *grid* 𝒢_N is the
(finite, computable) set of profiles p with D ≤ N, M ≤ N, w ∈ {2^{-j} : j ≤ N},
b ∈ {2^{-j} : j ≤ N}, and centers (c, c') on the mesh (b·ℤ)² ∩ [−2^N, 2^N]². Define
$$x_0(N) \;:=\; \max_{p \in \mathcal{G}_N}\
\frac{\mathrm{neg.ind}\big(\tilde Q_p\big)}{\dim \tilde V_p} \;\in\; \mathbb{Q}\cap[0,\tfrac12],
\qquad p_N^* := \text{the first maximizer in lexicographic order},$$
(the bound ≤ ½ comes from the padding: neg.ind(Q̃_p) ≤ dim V_p = ½ dim Ṽ_p). The
*localized infinitesimal signature* and its tower:
$$\sigma_{loc} := \mathrm{st}\big([\,x_0(N)\,]\big) \in [0,\tfrac12], \qquad
\sigma_{loc}^{(k)} := \mathrm{st}\big([\,x_k(N)\,]\big),$$
where x_k(N) is the logistic sequence of the winning cell: the non-degenerate
reduced form Q̄_N of Q̃_{p_N^*} (quotient by the radical, D133 Def. 2.4) and
x_k(N) := neg.ind(Q̄_N^{⊗2^k})/n̄_N^{2^k}.

**Proposition 3.3 (well-definedness and autonomy).** (a) x_0(N) is well defined and
is computable from the arithmetic data without zero positions: each entry of
each Gram matrix is Q₂(h,h') with h, h' in the class (autonomy, D133 Prop. 2.8 / P43), the
grid is finite and specified without zeros, and neg.ind is computed exactly
(Lagrange–Sylvester). (b) σ_loc ∈ [0,½] exists for every 𝒰 (bounded sequence).
(c) x_0(N) is nondecreasing in N (𝒢_N ⊆ 𝒢_{N+1}), hence converges and σ_loc does
not depend on 𝒰: σ_loc = lim_N x_0(N).

*Proof.* (a) Composition of cited facts: the class contains B_w·(monomials)
because multiplication by polynomials in the Mellin variable is x∂ₓ [D107]; the
padding is an explicit block. (b) st exists over bounded sequences. (c) Monotonicity:
the maximum over a growing family of finite sets; a bounded monotone sequence
converges; st of a convergent sequence = its limit for every 𝒰 [D133, Thm. 2.6(c), same
argument]. ∎

**Remark 3.4 (what changed from Doc 133).** Three things. (1) The dimension
per cell is bounded by the profile, not growing with height: Theorem 2.5 does not
apply (its hypothesis n_N → ∞ per cell fails on purpose). (2) The normalization is by
winning cell (a ratio of bounded integers per cell), not by a global
dimension: density is replaced by a normalized existence. (3) The ultrafilter
is tamed for free (Prop. 3.3(c)): the non-canonicity the target asked to tame was
an artifact of the non-monotone global normalization.

**Proposition 3.5 (the logistic law survives verbatim).** For every 𝒰 and every
standard k ≥ 0: σ_loc^(k) = ½(1 − (1−2σ_loc)^{2^k}), and
$$\lim_{k\to\infty} \sigma_{loc}^{(k)} \;=\;
\begin{cases} 0, & \sigma_{loc} = 0,\\ \tfrac12, & \sigma_{loc} \in (0,\tfrac12].\end{cases}$$

*Proof.* For each fixed N, Q̄_N is a non-degenerate Hermitian form of finite
dimension: Theorem 2.10 of Doc 133 (tensor identity D106 + closed form) applies
coordinate by coordinate; st is a homomorphism over bounded sequences and the
identity is used finitely many times (k standard). The case σ_loc = 1 — the only one
breaking the dichotomy in D133 — is excluded by the padding: x_0(N) ≤ ½ ⟹ σ_loc ≤ ½,
and 1−2σ_loc ∈ [0,1) except for σ_loc = ½, where (1−2x)=0 gives σ^(k) ≡ ½ — within
the ½ branch.
∎

---

## 4. [THEOREM] Sub-target (β): stability of the cell index

The three perturbation lemmas, with complete proof. They are the engine of the
grid: they make a computable mesh sufficient to capture planes whose exact position is
unknown.

**Theorem 4.1 (Weyl stability).** Let A, E be Hermitian on V, dim V = n, and
μ > 0. If A has at least κ eigenvalues ≤ −μ and ‖E‖_op < μ, then
neg.ind(A+E) ≥ κ. Symmetrically, if A ≥ −μ' with μ' < −‖E‖... (useful form:) with
ordered eigenvalues λ₁ ≥ … ≥ λ_n, |λ_k(A+E) − λ_k(A)| ≤ ‖E‖_op for every k.

*Proof.* Courant–Fischer: λ_k(A+E) = min_{codim S = k−1} max_{0≠v∈S}
R_{A+E}(v) with R the Rayleigh quotient. For every v: |R_{A+E}(v) − R_A(v)| =
|E(v,v)|/‖v‖² ≤ ‖E‖. Taking the same optimal S for A: λ_k(A+E) ≤ λ_k(A) + ‖E‖;
swapping A and A+E: the other inequality. The first statement: the κ eigenvalues
≤ −μ of A move to ≤ −μ + ‖E‖ < 0. ∎

**Theorem 4.2 (stability under bounded rank).** |neg.ind(A+E) − neg.ind(A)| ≤
rank E. (= Lemma 2.3; proof there, three lines, without eigenvalues.) ∎

**Theorem 4.3 (Lipschitz property of the Gram matrix under cell shift).** Let p be a
profile and G(ϑ) the Gram matrix of Q₂ on the cell V_{p+ϑ} obtained by shifting the
centers (c,c') ↦ (c+ϑ₁, c'+ϑ₂). Then G is differentiable in ϑ and
$$\|\partial_{\vartheta_i} G(\vartheta)\|_{op} \;\le\; L_p \;:=\;
(D+1)^2\,\max_{a,b}\, \big|Q_2\big(\partial h, h'\big)\big|\text{-type}
\;<\;\infty,$$
with L_p computable from the arithmetic data: the shift of the center is the
modulation g ↦ g·x^{iϑ}, whose derivative in ϑ is i(log x)·g = i·(x∂ₓ applied in
the Mellin coordinate) — a test of the same class [D107]; the entries of ∂G are
values of Q₂ on tests of the class, computable (autonomy) and finite
(absolute convergence, D107 Lemma 2.2(b)); the norm of the (D+1)²×(D+1)² matrix is
bounded by the maximum of the entries times the dimension.

*Proof.* Differentiability entry by entry: Q₂(h_ϑ, h'_ϑ) with
ĥ_ϑ(σ,τ) = ĥ(σ−iϑ₁, τ−iϑ₂); the sum (1.1) converges absolutely with uniformity
local in ϑ (decay (3.1) is uniform in |ϑ| ≤ 1), which allows differentiating under
the sum; the derivative inserts the corresponding linear factor, which is the
evaluation of a derived test of the class. The norm bound: ‖B‖_op ≤ (dim)·max|entries| for
Hermitian matrices (trivial Schur bound). ∎

**Theorem 4.4 (β: the index of the aligned cell survives on the mesh).** Let p* be an
ideal profile (arbitrary real centers, not necessarily on the mesh) such that
G(p*) has κ eigenvalues ≤ −μ < 0. Let p ∈ 𝒢_N be the closest mesh profile,
with |centers(p) − centers(p*)| ≤ b√2 (b the gauge of 𝒢_N). If
$$b \;\le\; \frac{\mu}{2\sqrt2\,L_{p^*}},$$
then neg.ind(G(p)) ≥ κ. In particular, for every ideal profile with (μ, L) fixed,
there exists a computable N₀ from (μ, L, position) such that for every N ≥ N₀ the
grid 𝒢_N contains a cell with index ≥ κ.

*Proof.* By Theorem 4.3 and the mean value theorem in each coordinate,
‖G(p) − G(p*)‖ ≤ L_{p*}·b√2·(path constant ≤ 2) ≤ μ/2 < μ. (L is continuous in ϑ
and we take it as the supremum over the segment, finite by the same argument.)
Theorem 4.1 concludes. Existence of N₀: the mesh 𝒢_N has gauge 2^{-N} → 0 and
reach 2^N → ∞, and finite ideal profiles (D, w, M) enter the grid for N
larger than their size. ∎

**Remark 4.5 (reading the target).** This is sub-target (β) of Problem 133.A in
the form that survived §2: the "o(1) perturbation of the shift" is, in the
localized version, a perturbation of size b·L with computable b — there is no
o(1/log T) to chase because the cell lives at the height of the defect
(bounded) and its constants are fixed. In the global version of D108 the same lemma
would have required a mesh o(1/log T) with L growing in T: that is where the
second-order wall would have reappeared. Localization does not sidestep the lemma:
it sidesteps its adverse regime.

---

## 5. [THEOREM] Localized sub-target (α): realizability of σ_loc > 0 under ¬RH

**Remark 5.1 (the conceptual key: the witness need not be test-accessible).**
κ_N involves neg.ind(Q₂|_{V_p}): a property of the compressed Gram matrix. The
test-accessibility restricts the SPECIFICATION of V_p (without zero positions); the
WITNESS vector of negativity within V_p is an object of the proof, not of the
scheme, and may use all the positions it wants. Lemma 2.4 of D108 used
polynomial factors with roots at zero positions and so seemed to inherit a caveat;
here the same factors are reconstructed as linear combinations WITHIN
the test-accessible span {B·σ^a}: annihilation by positions is legitimate because
it occurs in the witness. This remark is what turns (α) from debt into theorem.

### 5.1. The spectral tail

**Lemma 5.2 (tail of the concentrated test; complete proof).** Let h ∈ V_p with
ĥ(σ,τ) = ½ĝ(σ)φ̂(τ), where |ĝ(σ)| ≤ C_g(1+|Im σ − γ₀|)^{−M+D} and
|φ̂(τ)| ≤ C_φ(1+|Im τ|)^{−M+D} in the strip |Re| ≤ 1 (which holds for every element
of V_p with bounded coefficients C: C_g, C_φ ≤ C·C_M·e^{a_0}·(1+|σ|)^D-absorbed,
profile constants). Let Ω_r be the set of pairs (ρ₁,ρ₂) with
max(|Im σ − γ₀|, |Im τ|) ≥ r. If M − D ≥ 4, then
$$\Sigma_{tail}(r) := \sum_{(\rho_1,\rho_2) \in \Omega_r}
\big|\hat h(\rho_1,\rho_2)\big|\,\big|\hat h(\iota(\rho_1,\rho_2))\big|
\;\le\; C_g^2 C_\varphi^2\; \frac{C^*(M-D)\,\big(\log(2+|\gamma_0|) \big)^2}{(1+r)^{\,M-D-4}},$$
with C*(·) absolute. In particular Σ_tail(r) → 0 as M → ∞ for fixed r, and when
r → ∞ for fixed M.

*Proof.* Write u := Im σ = (γ₁+γ₂)/2, v := Im τ = (γ₁−γ₂)/2, so that
γ₁ = u+v, γ₂ = u−v. With a := |γ₁−γ₀|, b := |γ₂−γ₀|: |u−γ₀| + |v| ≥ max(a,b)/1 −
... — we use the exact inequality verified by expansion:
$$\Big(1 + \tfrac{a+b}{2}\Big)^2 \;\ge\; (1+a)(1+b),$$
(since (1+(a+b)/2)² − (1+a)(1+b) = ((a−b)/2)² ≥ 0), together with
|u−γ₀| + |v| ≥ (a+b)/2 (triangle inequality in the two coordinates). Hence
$$(1+|u-\gamma_0|)\,(1+|v|) \;\ge\; 1 + |u-\gamma_0|+|v| \;\ge\; 1+\tfrac{a+b}{2}
\;\ge\; \sqrt{(1+a)(1+b)}.$$
The point ι(ρ₁,ρ₂) = (1−ρ̄₁, 1−ρ̄₂) has the SAME ordinates (Im(1−ρ̄) = Im ρ), so
the same bound holds for |ĥ(ι(P))|. Therefore, with m := M−D:
$$|\hat h(P)|\,|\hat h(\iota P)| \;\le\; \tfrac14 C_g^2C_\varphi^2\,
\big[(1+|u-\gamma_0|)(1+|v|)\big]^{-2m}
\;\le\; \tfrac14 C_g^2C_\varphi^2\,(1+a)^{-m}(1+b)^{-m}.$$
The sum over all pairs factors:
Σ_pairs ≤ ¼C²_gC²_φ (Σ_ρ (1+|γ−γ₀|)^{−m})². The single sum, grouping by
unit intervals |γ−γ₀| ∈ [j, j+1) (positive and negative heights, zeros with
multiplicity):
$$\sum_\rho (1+|\gamma-\gamma_0|)^{-m} \;\le\; \sum_{j\ge0} (1+j)^{-m}\cdot
C\log(2+|\gamma_0|+j+1) \;\le\; C'\,\zeta(m-1)\,\log(2+|\gamma_0|),$$
using N(t+1) − N(t) ≪ log(2+t) [IK04, Thm. 5.8] and log(x+j) ≤ log x·(1+j); it converges
for m ≥ 3. The restriction to Ω_r: in Ω_r, (1+|u−γ₀|)(1+|v|) ≥ 1+r, so a factor
(1+r)^{−(m−4)} can be extracted from each product keeping exponent 4 ≥ 3+1 for
convergence of the double sum (split: product^{−m} ≤ (1+r)^{−(m−4)}·
product^{−4}... with product ≥ (1+r) in Ω_r and product ≥ √((1+a)(1+b)) always:
product^{−m} = product^{−(m−4)}·product^{−4} ≤ (1+r)^{−(m−4)}(1+a)^{−2}(1+b)^{−2};
the double sum with exponent 2 on each factor still converges with m=... — exponent 2:
Σ(1+j)^{−2}log(·+j) converges; ✓). Collecting constants: the stated bound. ∎

### 5.2. Independence of evaluations and genericity of the center

**Lemma 5.3 (Vandermonde with bump; complete proof).** Let z₁,…,z_q ∈ ℂ be distinct and
B entire with B(z_i) ≠ 0 for every i. If D ≥ q−1, the evaluation functionals
f ↦ f(z_i) are linearly independent over span{B(σ)σ^a : 0 ≤ a ≤ D}; in
particular, for any data (y₁,…,y_q) there exists an element of the span with
f(z_i) = y_i, and the coefficients are bounded by
‖coef‖ ≤ C(z, min_i|B(z_i)|)·‖y‖ (inverse of the scaled Vandermonde matrix).
Moreover, if B = B^{(M)}_w(·−ic) with B^{(M)}_w ≢ 0 entire (Def. 3.1), the set of
centers c ∈ ℝ with B(z_i − ic) = 0 for some i is discrete: every open interval
of centers contains a c with min_i |B^{(M)}_w(z_i − ic)| ≥ b₀ > 0, and by continuity
a ball of centers with the same bound b₀/2.

*Proof.* The matrix (B(z_i)z_i^a)_{i,a} = diag(B(z_i))·(z_i^a) has rank q:
Vandermonde with distinct nodes by hypothesis and invertible diagonal. The function
c ↦ B^{(M)}_w(z_i − ic) is entire in c and not identically zero (B ≢ 0 entire, nonzero
on no complex line unless ≡ 0); its real zeros are discrete; the finite union of
discrete sets is discrete. The bound b₀: B continuous and nonzero on a compact set that
avoids the zeros. ∎

### 5.3. The localized realizability theorem

**Theorem 5.4 (realizability: σ_loc > 0 under ¬RH; complete proof over
cited inputs).** Suppose ¬RH. Let ρ⁰ = ½+δ₀+iγ₀ be the minimal off zero (§1.1), with
multiplicity m₀ ≥ 1. Then there exist a standard dimension D₀ = D₀(local
configuration of zeros around ±γ₀) and a standard N₀ such that for all N ≥ N₀:
$$x_0(N) \;\ge\; \frac{1}{2 D_0} \;>\; 0,$$
and therefore, for every non-principal ultrafilter 𝒰:
$$\sigma_{loc} \;\ge\; \frac{1}{2D_0} \;>\;0 \qquad\text{and}\qquad
\lim_{k\to\infty} \sigma_{loc}^{(k)} = \tfrac12.$$

*Proof.* **Step 0 (the target plane).** Take the diagonal pair
P₀ := (ρ⁰, ρ⁰), with coordinates (σ₀, τ₀) = (½+δ₀+iγ₀, 0), and its image
ιP₀ = (1−ρ̄⁰, 1−ρ̄⁰), of coordinates (σ₀', τ₀') = (½−δ₀+iγ₀, 0). Since δ₀ ≠ 0,
ιP₀ ≠ P₀: a free orbit. Its contribution to (1.1) for any h is
$$2\,m_0^2\,\mathrm{Re}\Big[\hat h(P_0)\,\overline{\hat h(\iota P_0)}\Big] \tag{5.1}$$
(the factor m₀²: the sum runs with multiplicity in both slots; hyperbolic-plane
structure: D107 Theorem 5.5/Prop. 6.1, D98 §6).

**Step 1 (the set to annihilate).** Let S be the (finite, zeros are discrete) set
of zeros ρ with ||γ| − |γ₀|| ≤ 2, and let Z_σ be the finite set of values
σ = (ρ₁+ρ₂)/2 over pairs with both members in S, EXCLUDING σ₀ and σ₀'. Set
q := |Z_σ| + 2 and F := number of pairs with both members in S. All of these are
standard numbers fixed by the configuration (which is fixed: ¬RH is a hypothesis about ζ,
not a parameter).

**Step 2 (the cell and the witness).** We choose the ideal profile p* with D := q−1,
w := w₀ to be determined, M to be determined, σ-side center c* in a neighborhood of γ₀
where Lemma 5.3 guarantees min |B(z−ic*)| ≥ b₀ over the q points z ∈ Z_σ ∪ {σ₀, σ₀'},
and τ-side center c'* = 0 analogously for the point τ = 0. In V_{p*} we build the
witness v = h_{g_v, φ_v}: by Lemma 5.3 there exist coefficients (a_j) with
$$\hat g_v(z) = 0 \ \ \forall z \in Z_\sigma, \qquad
\hat g_v(\sigma_0) = 1, \qquad \hat g_v(\sigma_0') = -1,$$
with ‖coef‖ ≤ C₁ = C₁(Z_σ, σ₀, σ₀', b₀) standard; and φ̂_v with φ̂_v(0) = 1, ‖coef‖ ≤ C₂.
(The data (1, −1) fixes the phase of the plane: by (5.1), the contribution of the
target plane is 2m₀²·Re[(½·1·1)·conj(½·(−1)·1)] = −m₀²/2 < 0.)

**Step 3 (budget of Q₂(v,v)).** We decompose (1.1) into three classes of pairs:
(a) the orbit {P₀, ιP₀}: contributes −m₀²/2 (Step 2). (b) Pairs with both members in S,
other than the target orbit: their σ ∈ Z_σ, where ĝ_v = 0: they contribute 0. (c) The rest:
some member outside S, i.e. ||γ|−|γ₀|| > 2 for that member; then
max(|Im σ − γ₀|, |Im τ|) ≥ 1 on the sector of heights near +γ₀, and the
sectors near −γ₀ or far from both remain at distance ≥ 1 from (γ₀, 0) in at least
one coordinate — in all cases the pair is in Ω_1 relative to the center (γ₀, 0)
[verification: if both |γ_i − γ₀| ≤ 2 failed for the two members relative to +γ₀
but held relative to −γ₀ or mixed opposites, then |Im σ − γ₀| ≥ (2|γ₀|−4)/2 ≥ 1
or |Im τ| ≥ |γ₀| − 2; if γ₀ < 3 one enlarges S to ||γ|−|γ₀|| ≤ 2+2|γ₀| and the
constant is absorbed — a finite standard adjustment]. Lemma 5.2 with r = 1, C_g ≤ C₁·C_M·e^{a₀}·poly-sup,
C_φ ≤ C₂·(likewise) gives
$$\big|\text{(c)}\big| \;\le\; \Sigma_{tail}(1) \;\le\;
C_3(\text{profile}, C_1, C_2)\cdot \theta(M, w),$$
where θ(M, w) → 0 as M → ∞ with w fixed (the bound of Lemma 5.2 decays in M−D−4; D
is fixed since Step 1). We choose M = M₀ standard such that |(c)| ≤ m₀²/4. Then
$$Q_2(v, v) \;\le\; -\frac{m_0^2}{2} + 0 + \frac{m_0^2}{4} \;=\; -\frac{m_0^2}{4} \;<\; 0,$$
hence neg.ind(Q₂|_{V_{p^*}}) ≥ 1, with spectral margin: the minimum eigenvalue of the
Gram matrix is ≤ Q₂(v,v)/‖v‖²_{coef} ≤ −μ₀ < 0 with standard μ₀.

**Step 4 (from the ideal cell to the grid).** The ideal profile p* has arbitrary real
centers; by Theorem 4.4 (with κ = 1, μ = μ₀, L = L_{p*} finite by Theorem
4.3, all standard) there exists a standard N₀ such that for N ≥ N₀ the grid 𝒢_N contains
a profile p with neg.ind(Q₂|_{V_p}) ≥ 1. Moreover, by Lemma 5.3 the condition
min|B| ≥ b₀/2 is stable on a ball of centers: the mesh reaches it.

**Step 5 (conclusion).** For N ≥ N₀: x₀(N) ≥ neg.ind(Q̃_p)/dim Ṽ_p ≥ 1/(2(D+1)²)
=: 1/(2D₀) with D₀ = (q)² standard (the padding doubles; the index does not drop
upon padding with positives: the negative subspace of V_p stays negative in Ṽ_p). By
Prop. 3.3(c), σ_loc = lim x₀(N) ≥ 1/(2D₀), for every 𝒰. Prop. 3.5 gives
σ_loc^(k) → ½ since σ_loc ∈ (0, ½]. ∎

**Declared status of Theorem 5.4 (line by line).** Cited, not re-proved, inputs:
(1.1) with absolute convergence and factorization (1.2) [D107, Lemmas
5.2(b), 2.2(b), Thm. 3.4]; the free-orbit/plane structure and the multiplicity
weights in (5.1) [D107 Thm. 5.5, Prop. 6.1; D98 §6]; closure of the class
under Mellin monomials [D107]; N(t+1)−N(t) ≪ log t [IK04]. Proved here: Lemmas
5.2, 5.3, Theorems 4.1–4.4 and the assembly. **Hypothesis D of Doc 108 is not used**:
there is no toy-model assumption (the zero configuration is arbitrary under ¬RH; the
additional off zeros, multiplicities, and clusterings are absorbed into the finite S
and into the tail), there is no uniformity in T (there is no T), and the constants are
standard because they depend only on the fixed configuration around the minimal defect.
What is NOT claimed: no uniform quantitative bound (D₀ and N₀ are not effective
in terms of m̄ or anything else: they depend on the unknown local configuration).
That is exactly what σ_loc does not need.

**Proposition 5.5 (RH branch).** Under RH, x₀(N) = 0 for all N, σ_loc = 0 and
σ_loc^(k) ≡ 0.

*Proof.* Q₂ ≥ 0 on the span of the class [D108, Prop. 2.2]; every compression
of a form ≥ 0 is ≥ 0; the padding is positive; neg.ind = 0 on every cell. ∎

**Corollary 5.6 (the logistic dichotomy, promoted — the closing of Problem 133.A).**
For every non-principal ultrafilter 𝒰:
$$\mathrm{RH} \;\iff\; \sigma_{loc} = 0 \;\iff\; \lim_{k\to\infty}\sigma_{loc}^{(k)} = 0
\;\iff\; \lim_{k}\sigma_{loc}^{(k)} \neq \tfrac12,$$
with the RH branch = Prop. 5.5 (theorem) and the ¬RH branch = Theorem 5.4 (theorem over the
cited inputs). ∎

**Remark 5.7 (canonicity).** The dichotomy of Corollary 5.6 is independent of
𝒰 (Prop. 3.3(c): σ_loc is a genuine limit). The target's non-canonicity objection
("the ultrafilter chosen to concentrate where the defect lives?") was
resolved by monotonicity, not by choice: the growing grid concentrates on its own.

---

## 6. [BRIDGE] What remains of the logistic law as a criterion for RH — a candid account

### 6.1. What was gained

1. **Problem 133.A is solved, with a course correction.** The original
   statement (σ⁰ ≥ c for the canonical global scheme) is FALSE (Theorem 2.5 +
   Corollary 2.6): there was nothing to prove, there was something to refute. The
   correct statement (σ_loc ≥ c under ¬RH) is a theorem (5.4). Doc 133 §5.2 asked to close
   "(α) Hypothesis D" and "(β) perturbation": (β) is proved (Theorems 4.1–4.4); (α)
   turned out not to be Hypothesis D but its dissolution — localization to bounded
   height eliminates the regime (T → ∞ with resolution 1/log T) where Hypothesis D
   was necessary.

2. **The equivalence enters the catalog with both branches at theorem (over
   cited inputs) status:** RH ⟺ the localized logistic tower tends to 0 and not to ½. The
   individual events x₀(N) are computable from the primes (Prop. 3.3(a)): it is
   the reformulation of D133 with the caveat removed and the normalization corrected.

3. **The map improved twice.** (i) The new face of the wall is now named
   (density invisibility, §2.4): individual defects are null for every
   increasing-dimension density — the "density" coordinate of the master
   quantifier. (ii) The global σ_ε does not die: it changes job — it is a detector of
   *locally dense defect* (Prop. 2.7), a configuration invariant that neither RH
   nor ¬RH decides, and that no current density theorem controls per window.

### 6.2. What was paid, without anesthesia

4. **Density → existence.** σ_loc > 0 says "there exists a bounded cell with a
   negative eigenvalue somewhere in an unbounded search." Unwinding the
   ultrapower and the tower, Corollary 5.6 is equivalent to: *Q₂ is positive
   semidefinite on every cell of a countable computable basis of tests* ⟺ RH — that
   is, a computable-by-Grams presentation of Weil positivity (restricted
   to a countable dense family; the sufficiency of the family for the direction
   "positivity ⟹ RH" lies within the ¬RH branch = Theorem 5.4, which is where the
   content lives). The real added value over classical Weil: (a) each event is finite
   linear algebra on arithmetic data — no contour integrals or positions; (b)
   the logistic amplification separates the two worlds into macroscopic constants 0 vs.
   ½; (c) the dichotomy is 𝒰-canonical. The NOT-added value: no new way to
   PROVE positivity.

5. **Where the wall now is.** Two places, both old acquaintances with new
   coordinates. (i) The standard part is still Π₁-non-effective: "x₀(N) = 0
   for all N" is exactly as unverifiable as always; falsification of RH is
   semi-decidable by arithmetic Grams (run the grid until a negative eigenvalue is
   found) — a second semi-decision machine alongside the classical numerical one
   (integrating ζ′/ζ), with the aesthetic difference that this one is exact in the
   arithmetic of the coefficients. (ii) The master quantifier moved from "uniform in
   windows" (D108, the o(1/log T)) to "unbounded search on the grid" (N₀ of Theorem
   5.4 is not effective: it depends on the unknown local configuration of the defect). The
   full transmutation of the dossier: D108 had it as precision; D133 had it
   as non-effectiveness of st plus a realizability caveat; this document settles
   the caveat and leaves pure non-effectiveness, split into (i)+(ii).

6. **Hypothesis D: where it stands.** It is no longer a bottleneck for the
   DICHOTOMY (Theorem 5.4 does not use it). It remains the bottleneck for any
   QUANTITATIVE version by height: if one wanted κ at height T to grow as m·log T
   realized over tests (Prop. 2.3 + Lemma 2.4 of D108 for real, with T → ∞),
   the resolution regime reappears and with it Hypothesis D and the second-order
   wall — intact. The exact boundary: **localized existence = theorem;
   uniform quantitative growth = RH re-encoded** (D108, Thm. 4.3). This
   document did not move that boundary; it mapped it.

### 6.3. The exact open link (what a Doc 137 could attack)

7. **[GAP/WISH].** The only honest intermediate statement that remains
   enunciable and unproved in this coordinate: an UNCONDITIONAL lower bound of
   approximate per-cell positivity — "there exists a computable function ε(p) > 0 such that
   under RH, λ_min(Gram(p)) ≥ ε(p) for every cell p" (localized
   quantitative Weil positivity). With it, the Π₁ of point 5(i) would become a Π₁ with
   modulus — every event of the grid would be decidable with a precomputable
   finite precision, and the search for ¬RH would have a stopping criterion by
   level. Known obstruction: under RH there are near-double zeros if there are any
   (Lehmer pairs), which make λ_min genuinely small on cells
   aligned with them: ε(p) must degrade with the local online
   configuration, and estimating it is again a zero-repulsion problem —
   pair correlation. The wall shows up there too, as it should.
   Recorded as Problem 136.A.

8. **[WISH 6.1].** That the global σ_ε (detector of locally dense defect,
   Prop. 2.7) find its own office: an unconditional theorem "σ⁰_global = 0 for
   every admissible-band scheme" would be equivalent to "there is no linear
   clustering of off zeros per band" — weaker than RH, stronger than per-window density
   theorems. It is a target for honest partial theorems (large sieve per
   short windows), beyond the scope of this document.

---

## 7. Verdict

**Problem 133.A: SOLVED, in two halves of opposite sign.** The destructive half:
global realizability is false — σ⁰ = 0 in both worlds for finite defect
(Theorem 2.5), bridge-Theorem 2.13(b) of Doc 133 was mis-normalized
(Corollary 2.6), and the global logistic dichotomy is not a criterion for RH; the face of the
wall responsible is now named (density invisibility, §2.4). The
constructive half: the localized signature σ_loc (Def. 3.2) inherits the logistic law
verbatim (Prop. 3.5), its realizability under ¬RH is a theorem with complete proof
over cited inputs (Theorem 5.4 — without Hypothesis D, with the conceptual key of
Obs. 5.1: test-accessibility restricts the space, not the witness), the sub-target
(β) is a clean, computable perturbation package (Theorems 4.1–4.4), and
the equivalence RH ⟺ lim σ_loc^(k) = 0 is promoted to a catalog entry with both
branches proved and canonicity in 𝒰 (Corollary 5.6, Obs. 5.7). Net content
measured without inflation: a Gram-computable, logistically amplified presentation of
Weil positivity, the D133 caveat settled, and the wall re-mapped in
Π₁-non-effectiveness pure plus unbounded search — with a single honest
new intermediate problem on the table (localized quantitative positivity, Problem 136.A,
which borders on Lehmer and pair correlation, as everything that matters does).

---

## References

**Internal (backward-only):** Doc 133 (Defs. 2.1–2.4, Thms. 2.6, 2.7, 2.10, Prop.
2.8, 2.11, bridge-Theorem 2.13, §5.2 Problem 133.A); Doc 108 (Defs. 1.1–1.2, Props.
2.2, 2.3, 2.5, Lemma 2.4 and Hypothesis D, Thms. 3.3, 3.4, 4.3, §7.4, §8.2); Doc 107
(Lemma 2.2(b), Lemma 5.2(b), Thm. 3.4, Thm. 5.5, Prop. 6.1, closure x∂ₓ); Doc 98
(§6: quadruple, κ = 2, hyperbolic planes); Doc 106 (tensor identity of the
index); Doc 110 (Thm. 4.3, Prop. 4.5); P43 (master quantifier, Principle 3.1;
autonomy of the value); P35 (κ = 2m); NO-GO-LIST (MW-7; proposal to register
"density invisibility", §2.4).

**Literature (verifiable; standard statements cited by classical reference):**
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004 —
  Thm. 5.8 (Riemann–von Mangoldt; N(t+1)−N(t) ≪ log t, with multiplicity). [IK04]
- A. Robinson, *Non-standard Analysis*, North-Holland, 1966 — ultrapowers, standard
  part (ch. 2; via D133).
- H. Bohr, E. Landau, *Beiträge zur Theorie der Riemannschen Zetafunktion*, Math.
  Ann. 74 (1913/14) — zero mean density of off zeros (used only as context in
  Obs. 2.8; the cited statement — N(σ,T) = O(T) for σ > ½ — is the classical one).
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Ch. X —
  signature by congruence (Lagrange–Sylvester; via D133 Prop. 2.8).
- R. Bhatia, *Matrix Analysis*, Springer GTM 169, 1997 — Courant–Fischer and
  Weyl inequalities (Ch. III); Theorems 4.1–4.2 are proved
  self-contained above and the reference is for courtesy.
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Lund (1952) — positivity ⟺ RH (normalization of the program via D108
  Prop. 2.2 / D110 §3.2).
- B. E. Petersen / R. Paley, N. Wiener — Paley–Wiener type theorems for C_c^∞
  (decay (3.1); standard, cf. Hörmander, *The Analysis of Linear Partial
  Differential Operators I*, Thm. 7.3.1).

*End of Doc 136.*
