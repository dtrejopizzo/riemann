# Doc 108 — The sieve→index bridge: formulation, unconditional inventory, and measuring the distance

**Phase 36 — Forms A/B/C ·**
**Prerequisites:** P42 (§6: Missing Lemma 6.1 "sieve-to-index bridge", steps (1)–(3) and their falsifiers); Doc 107 (W₂, thickened class, nine blocks, Theorems 3.4, 4.2, 4.4, 5.5, Prop. 6.1, Missing Lemma 7.2); Doc 106 (§3 Prop. 3.4/3.5, sterility lemma Prop. 3.6, Missing Lemmas 5.2/5.3); Doc 99 (transmutation pattern, discriminator I2a); Doc 96 (Theorem 8.1); Doc 94 (condition C5); P41 (one-dimensional no-go: controlled interior / boundary = RH).
**Absolute rule:** no proof is fabricated. Every step is either a complete proof, a closed computation, or a declared GAP. No numerics, no simulations.

---

## 0. Executive summary

This document executes **step (1)** of Missing Lemma 6.1 of P42 (the sieve→index bridge)
and measures the distance between the available sieve bound and the bound the bridge needs.
Result in one line: **the distance is not a constant or a logarithm: it is the step from
"on average over windows" to "uniform over windows", and that step is RH re-encoded. BRIDGE
DEAD**, with the exact location of the wall in §7 and the transmutation documented in §8.

Main findings, in order:

1. **(§2) The variational problem is well posed but the "relative" invariant is not
   functional-accessible.** κ(Q₂^rel) = 8m² (the off×off block) is a spectral compression.
   What the test class sees are **indices by windows** of the full form Q₂, and
   under ¬RH these indices grow: in the height-T window of the sum variable,
   κ_W(Q₂) ≈ 2m·n_W with n_W ≍ |W|·(log T)/π (Proposition 2.6: off×on contamination,
   the mechanism of Prop. 6.1 of Doc 107 localized by windows). Under RH, κ_W = 0
   for every window. **The test-accessible index is binary: 0 for every window (RH) or
   unbounded over windows (¬RH).** Any unconditional theorem
   "sup_W κ_W ≤ f(2) < ∞" is therefore equivalent to RH already at k = 2: the boundary of
   the P41 no-go reappears inside the double form.

2. **(§3) Answer to the step (1) falsifier: neither "the arithmetic side controls" nor
   "the archimedean side dominates" — the archimedean side dominates exactly in the regime where
   the index is invisible.** In the signed ledger
   Q₂ = [DD+AA+PP+PA+AP] − [DP+PD+DA+AD], the almost-prime block enters with **positive
   sign** (unlike the one-variable Weil functional, where the prime side is
   subtracted). With fixed supports and window height T → ∞, all prime and polar
   blocks are O_sop(log T) while AA ~ c·(log T)² > 0: the form is positive definite
   on those tests (Theorem 3.3, "sub-resolution blindness"). The index only becomes
   visible when the support grows with T (a ≍ c log T, primes up to T^{O(1)}), and there the
   prime blocks reach by identity the same order (log T)² as the archimedean one: the
   negativity is a **second-order cancellation** phenomenon, not the domination of one
   block.

3. **(§3.4) The literal heuristic of P42 step (1) — "bound κ by the sign changes
   of the arithmetic kernel K(N)" — is refuted:** for φ ≥ 0 the kernel
   K(N) = Σ_{d|N}Λ(d)Λ(N/d)φ(d²/N) is **non-negative, with no sign change at all**, and
   yet the index is positive under ¬RH. The oscillation that carries the index lives in the
   test functions, not in the kernel; the correct object is the **deficit kernel**
   ΔK := K − (polar/archimedean prediction), whose fluctuations are exactly those of
   pair correlation.

4. **(§4–§5) The necessary bound is ASYMPTOTIC and second-order; the unconditional
   inventory gives something else.** The main term of S(g,φ) is ½ĝ(1)φ̂(0), **with no
   singular series** (multiplicative correlation, not additive: Theorem 4.2 — PNT² gives it
   unconditionally with Vinogradov–Korobov savings at fixed frequency; sieving is not even
   needed for the static asymptotic). What the bridge needs is that asymptotic **uniform in
   the oscillation frequency T** (up to scales X = T^C) with **relative error o(1/log T)** — one
   logarithmic order below the main term of pair correlation, in the scale of
   lower-order terms (Bogomolny–Keating / Montgomery–Soundararajan). Selberg's sieve
   gives a factor of 8 over the main term in the analogous additive problem (relative
   precision O(1)); Vaughan/Heath-Brown and the large sieve give cancellation **on average
   over T** (mean values of Dirichlet polynomials); no technique gives uniformity in T, and the
   exceptional window that the average does not control is exactly where the signal lives.

5. **(§6–§7) Measurement: outcome (C), aggravated.** It is not just that the necessary bound
   is of asymptotic type (the pair-correlation wall anticipated by P42 §6.2): it is its
   **uniform-in-windows and second-order** form, which (Theorem 6.2) implies RH directly —
   it fails the "RH in disguise" test of item (vi). The averaged version is a theorem
   (Montgomery–Vaughan) and is structurally insufficient. Even the consolation prize
   (κ_W ≤ C·n_W ⇒ m ≤ C/2, a density bound on quadruples) requires the
   same second-order precision: it is also behind the wall. Amplification in k does not
   move the mean/uniform boundary (Proposition 7.3).

**VERDICT: BRIDGE DEAD** (§9), with the location: the wall is not in the strength of
the sieve (the sieve here even gives asymptotics), it is in the quantifier over windows
— the same interior/boundary structure as the P41 no-go, reappearing in sieve clothing.

---

## 1. Notation and what is inherited

We inherit from Doc 107 without re-proving:

- The thickened test class: h_{g,φ}(x₁,x₂) = g(x₁x₂)φ(x₁/x₂), g, φ ∈
  C_c^∞(ℝ₊*); double Mellin ĥ(s₁,s₂) = ½ ĝ(σ) φ̂(τ), with σ := (s₁+s₂)/2,
  τ := (s₁−s₂)/2 (Doc 107, Theorem 3.4).
- The quadratic form Q₂(h,h') := W₂(h ⋆ h̃') (Doc 107, Def. 5.1), with the thickened
  class closed under ⋆ and involution: h_{g₁,φ₁} ⋆ h_{g₂,φ₂} = ½ h_{g₁⋆g₂, φ₁⋆φ₂},
  h̃_{g,φ} = h_{g̃, φ^∨} (Doc 107, Lemma 5.2(a)).
- The spectral side:
  Q₂(h,h) = Σ_{ρ₁,ρ₂} ĥ(ρ₁,ρ₂) · conj( ĥ(1−ρ̄₁, 1−ρ̄₂) ), absolutely convergent
  (Doc 107, Lemma 5.2(b)).
- The nine arithmetic blocks of W₂ = (D−P−A)⊗(D−P−A) (Doc 107, §2.3, Theorem 2.4),
  all computable with no positions of zeros.
- The almost-prime block: P⊗P(h_{g,φ}) = Σ_I + Σ_II + Σ_III + Σ_IV with
  Σ_I = Σ_N g(N) (Λ⋆_φΛ)(N), (Λ⋆_φΛ)(N) := Σ_{d|N} Λ(d)Λ(N/d) φ(d²/N)
  (Doc 107, Theorem 4.2).
- The toy model (Hypothesis D, m = 1): quadruple {½±δ±iγ₀}, parameters
  z = ρ − ½; off×off block of signature (8,8), 8 hyperbolic planes, with half the
  index carried by φ̂ at Re τ = ±δ (Doc 107, Theorem 5.5, Corollary 5.6).
- κ(Q₂) global = ∞ under ¬RH, from the off×on planes (Doc 107, Prop. 6.1); the invariant
  of Form B is the **relative block** off×off, κ(Q₂^rel) = (4m)²/2 = 8m².

Window notation. For T ≥ 2 and Δ ∈ (0,1] fixed, the **window of the sum variable**
is
$$W_{T,Δ} := \{ σ ∈ ℂ : |\mathrm{Im}\,σ - T| ≤ Δ,\ |\mathrm{Re}\,σ - \tfrac12| ≤ \tfrac14 \}.$$
(The strip Re σ ∈ [¼, ¾] contains all possible σ = (ρ₁+ρ₂)/2, since
Re ρ_i ∈ (0,1).) The window is stable under the involution σ ↦ 1−σ̄ (which fixes Im σ and
reflects Re σ about ½). We write
$$n_W := \#\{γ : ζ(\tfrac12+iγ)=0 \text{ on-line},\ |γ - 2T| ≤ 2Δ\} \;\asymp\; \frac{2Δ}{\pi}\log T$$
(von Mangoldt density; [IK04, Thm. 5.8]).

**Definition 1.1 (index by window, spectral version).** Let B be the spectral Gram
form of Q₂ on the set of ordered pairs of zeros (that of Lemma 5.2(b) of
Doc 107, with the involution (ρ₁,ρ₂) ↦ (1−ρ̄₁,1−ρ̄₂)). We define
$$κ_W(Q₂) := \mathrm{neg.ind}\bigl( B|_{\{(ρ₁,ρ₂):\, (ρ₁+ρ₂)/2 \,\in\, W\}} \bigr),$$
the compression of B to the pairs whose mean falls in the window W. Since W is stable under
the involution, the compression is hermitian and the index is well defined.

**Definition 1.2 (test-accessible index).** For a subspace V' ⊆ span{h_{g,φ}},
κ(Q₂; V') := sup{dim U : U ⊆ V', Q₂|_U < 0}. It is the only index that an arithmetic
certificate (a theorem about the blocks of §2.3 of Doc 107) can bound, because the
blocks are functionals of (g,φ), not of the zeros.

---

## 2. (i) The variational problem for κ(Q₂^rel)

### 2.1. The form on the thickened class: bi-quadratic, with coupling

On a pure kernel h = h_{g,φ}, the spectral side is, by Theorem 3.4 and
Lemma 5.2(b) of Doc 107:

$$Q₂(h_{g,φ}, h_{g,φ}) \;=\; \frac14 \sum_{ρ₁,ρ₂}
\hat g(σ_{12})\,\overline{\hat g(1-\bar σ_{12})}\;
\hat φ(τ_{12})\,\overline{\hat φ(-\bar τ_{12})},
\qquad σ_{12}=\tfrac{ρ₁+ρ₂}{2},\ τ_{12}=\tfrac{ρ₁-ρ₂}{2}. \tag{2.1}$$

**Remark 2.1 (it does not factorize; answer to the statement's question).** (2.1) is
quadratic in g and quadratic in φ separately (bi-quadratic in the pair), but it does
**not** factorize as (form in ĝ)·(form in φ̂): each pair of zeros couples the value of ĝ at the
sum with the value of φ̂ at the difference, and the sum over pairs does not separate. Q₂ is a
genuine hermitian form on the linear span of the thickened kernels (not only on the
cone of pure tensors g⊗φ); the pure tensors form a non-linear cone within the
span, and the negative index is computed over the span (Doc 107, Lemma 5.4: the
evaluation map is surjective from the span).

**Proposition 2.2 (positivity under RH).** If every zero satisfies ρ = 1−ρ̄, then for
every h in the span of the thickened class, Q₂(h,h) = Σ_{ρ₁,ρ₂} |ĥ(ρ₁,ρ₂)|² ≥ 0.

*Proof.* Doc 107, Rem. 5.3: under RH the pairing of Lemma 5.2(b) is diagonal.
∎

**The variational problem, stated.** Under ¬RH (toy), for which (g,φ) — more
precisely, for which h in the span — is Q₂(h,h) < 0? By (2.1) and the orbit
structure: decomposing the spectral sum into on×on, off×on, and off×off blocks,

- **on×on**: pairs with ρ₁, ρ₂ both on-line are fixed points of the involution and
  contribute |ĥ(ρ₁,ρ₂)|² ≥ 0 — a positive "sea";
- **off×off**: 16m² pairs, 8m² hyperbolic planes (Doc 107, Theorem 5.5);
- **off×on**: for each on-line zero ½+iγ and each pair {z, z* = −z̄} of off
  parameters, a hyperbolic plane {(z, iγ), (z*, iγ)} (Doc 107, Prop. 6.1): 2m planes per each γ,
  plus the symmetric ones in the other slot.

Q₂(h,h) < 0 requires that the mass of ĥ on the hyperbolic planes (aligned with their
negative vectors) exceed the mass of |ĥ|² on the on×on sea. That is the exact
variational formulation; the negative directions live where ĥ is aligned with pairs that
contain at least one off zero, and suppressed on the on×on pairs.

### 2.2. Where the negative directions live: a reading in (σ,τ)

From Corollary 5.6 of Doc 107, in the toy model the 8 negatives of the relative block are
distributed: 2 in full off sums (σ = ±δ±iγ₀), 2 in real sums (σ = ±δ, τ = ±iγ₀),
2 in imaginary sums (σ = ±iγ₀, τ = ±δ), 2 in null sums (σ = 0, τ ∈ {±z₁,±z̄₁}).
Two operational consequences for the variational problem:

(a) **The whole relative block lives in bounded-height windows**: |Im σ| ≤ γ₀. High
windows (T ≫ γ₀) contain no off×off pairs.

(b) **Realizing any of the 8 negatives requires oscillation at the frequency of the
zero in one of the two variables**: either ĝ oscillates at frequency ~γ₀ (imaginary
sums), or φ̂ must be evaluated at heights Im τ = ±γ₀ (real sums: φ oscillates at
frequency γ₀ in the quotient variable x₁/x₂), or both. Since γ₀ is unknown, **any
certificate must be uniform in the alignment frequency** — the first appearance of the
quantifier that will kill the bridge.

### 2.3. The index by windows under ¬RH: off×on contamination grows

**Proposition 2.3 (spectral count by window).** In the toy model (m ≥ 1 quadruples,
all of bounded height ≤ γ₀ fixed), for T ≥ 2γ₀ + 2 and Δ ∈ (0,1]:
$$κ_{W_{T,Δ}}(Q₂) \;=\; 2m \cdot n_{W}^{(1)} + 2m \cdot n_{W}^{(2)}
\;=\; \frac{8mΔ}{\pi}\,\log T\,(1+o(1)) \qquad (T \to \infty),$$
where n_W^{(1)}, n_W^{(2)} count the on-line zeros γ with (z_off + iγ)/2 ∈ W according to the
slot. Under RH, κ_W(Q₂) = 0 for every window W.

*Proof.* The pairs in the high window are classified: (i) on×on: fixed points of
the involution, planes of signature (1,0): contribute no negatives. (ii) off×off: absent
(σ has |Im σ| ≤ γ₀ < T − 1). (iii) off×on: the pair (ρ_off, ½+iγ) with
σ = ½ + (z+iγ)/2 ∈ W requires |γ + γ_off − 2T| ≤ 2Δ (with z = ±δ + iγ_off,
γ_off ∈ {±γ₀}); the involution sends (z, iγ) ↦ (z*, iγ) with z* = −z̄ ≠ z (since
Re z = ±δ ≠ 0): free orbit, hyperbolic plane, signature (1,1), exactly the
mechanism of Prop. 6.1 of Doc 107. For each admissible γ there are 4m off vectors in the
first slot = 2m planes; likewise for the second slot. The count of admissible γ is
n_W ≍ (2Δ/π)·... by the von Mangoldt formula N(T+h)−N(T) = (h/2π)log T (1+o(1))
for fixed h. The claim under RH is Proposition 2.2 compressed. ∎

**Lemma 2.4 (realizability on the test class).** For every J ≤ κ_{W}(Q₂)
(count of Prop. 2.3) and every ε > 0, there exists a subspace U ⊂ span{h_{g,φ}} of
dimension J with Q₂|_U < 0.

*Proof.* It is the window extension of the argument of Prop. 6.1 of Doc 107,
with the same apparatus. We choose J target hyperbolic planes, with spectral points
(σ_j, τ_j) and (σ_j', τ_j') = (1−σ̄_j, −τ̄_j), all distinct (linear bijection
(z_i,z_j) ↦ (σ,τ), Doc 107 §5.2, extended to off×on pairs: the points remain
distinct because the γ's are distinct and Re τ = ±δ/... distinguishes the slots). For each
plane j, take h_j = h_{g_j,φ_j} with: ĝ_j concentrated at σ_j with superpolynomial
decay outside a neighborhood of radius η in Im σ (Paley–Wiener, Doc 107 Lemma 1.2),
multiplied by the polynomial in σ that vanishes at the finitely many points σ of the other
target planes and at the 9 values σ of the off×off block (multiplying by
polynomials in s preserves the class: it corresponds to applying x∂_x to g); φ̂_j concentrated
at τ_j in the same way. The evaluation of h_j on its plane is normalized to the negative
vector (a, ā') with B = anti-diagonal: Q₂-contribution of the plane = −2|a|². The
remaining contributions: (1) the other target planes: cancelled by the polynomial
factors; (2) the on×on tail and the non-target pairs: positive or bounded by
Σ_{(ρ₁,ρ₂) \text{ not target}} |ĥ_j| |ĥ_j∘inv| ≤ ε_j by the rapid decay and
absolute convergence (Doc 107, Lemma 2.2(b)), choosing η and the decay order; the
positive tails sum to ≥ 0 but the diagonal term of the Gram matrix of
U = span{h_j} is ≤ −2|a|² + ε_j and the cross terms are O(ε): for small ε the
Gram matrix is negative definite. ∎

**Declared caveat.** Lemma 2.4 inherits the status of Prop. 6.1 of Doc 107 (same
technique, same toy-model assumptions with Hypothesis D); fine tracking of the
constants ε(η, J) is not load-bearing: all that is used afterward is
κ(Q₂; test class, window W) ≥ (1−o(1))·κ_W(Q₂) in the sense of Prop. 2.3.

### 2.4. First structural conclusion: the relative invariant is not what arithmetic
can see

**Proposition 2.5 (binarity of the test-accessible index).** (a) Under RH,
κ_W(Q₂) = 0 for every window. (b) Under ¬RH with m ≥ 1, sup_W κ_W(Q₂) = ∞
(Proposition 2.3: grows like log T). Consequently, **any unconditional statement
of the form "there exists f(2) < ∞ with κ_W(Q₂) ≤ f(2) for every window W" is
logically equivalent to RH**.

*Proof.* (a) = Prop. 2.2. (b) = Prop. 2.3 + Lemma 2.4. The equivalence: if RH,
the bound holds with f(2) = 0; if ¬RH, it fails for every finite f(2). ∎

This reconfigures step (1) of P42. Lemma 7.2 of Doc 107 asked for exactly the
uniform bound by windows; Proposition 2.5 shows that **that formulation already is RH** —
not an intermediate amplifiable lemma but the complete statement. The relative block
κ(Q₂^rel) = 8m² (finite, amplifiable) is a compression to the off×off pairs, which is
defined by the positions of the zeros: to isolate it within a window one would have to
separate the off×off planes from the off×on planes that coexist in the same low
windows (|Im σ| ≤ γ₀: there the off×on terms with γ ≈ −γ_off also fall, in number
O(m·Δ·log γ₀) — finite but present). No functional of (g,φ) is known, computable
from the arithmetic side, whose index is that of the off×off block and not that of
the whole window; and §3–§6 will show that any substitute reduces to evaluating
the almost-prime deficit to second order. Declared structural GAP: **the notion "κ(Q₂^rel)"
of Missing Lemma 6.1 of P42 does not today have a test-accessible definition.**

---

## 3. (ii) The arithmetic ledger: who can turn negative and why

### 3.1. The signed decomposition

By Theorem 2.4 of Doc 107 applied to H := h ⋆ h̃ (which remains in the thickened class,
with G := ½ g⋆g̃, Ψ := φ⋆φ^∨):

$$Q₂(h,h) \;=\; \underbrace{DD(H) + AA(H)}_{\text{polar/archimedean}}
\;+\; \underbrace{PP(H)}_{\text{almost-prime}}
\;+\; \underbrace{PA(H)+AP(H)}_{\text{prime×arch.}}
\;-\; \underbrace{[DP+PD](H)}_{\text{pole×prime}}
\;-\; \underbrace{[DA+AD](H)}_{\text{pole×arch.}} \tag{3.1}$$

**Remark 3.1 (the sign of the almost-prime block is reversed relative to one
variable).** In one variable, Q(f,f) = D(F) − P(F) − A(F): the prime side is
**subtracted**, and the statement's guiding analogy ("the arithmetic side can in principle
outweigh the pole") is the classical mechanics of Weil positivity. In (3.1), by the
parity of the signs of the product (D−P−A)⊗(D−P−A), the almost-prime block PP enters with
**positive sign**, and the candidates for "winning in the negative" are the mixed
pole×prime and pole×archimedean blocks. The one-variable analogy carries over, but with
the roles permuted: the detector of ¬RH is not "primes > pole" but a cancellation between PP and
AA at the order of their fluctuations (§3.3).

Reality check: every block of (3.1) is real on H = h⋆h̃ (the involution makes H an
autocorrelation; the computation is the one-variable one, Doc 107 §1, in each
slot).

### 3.2. Size hierarchy I: fixed-support regime (sub-resolution)

We fix the supports: supp g, supp φ ⊆ [e^{−a}, e^{a}] with a fixed, and let the
window height grow: tests with ĝ concentrated at Im σ ≈ T → ∞ (g oscillates at
frequency T), φ̂ at heights O(T) depending on the target. We normalize ‖g‖₂ = ‖φ‖₂ = 1 (L²
norm in Haar measure d*x).

**Lemma 3.2 (sizes with fixed support).** With fixed supports and T → ∞:

(i) AA(H) = (1/4π²)∬ Ω(t₁)Ω(t₂) |ĥ(½+it₁, ½+it₂)|² dt₁dt₂, and since
Ω(t) = −log|t| + O(1), on tests concentrated at heights t₁+t₂ ≈ 2T with t₁−t₂ = O(1):
AA(H) = (log T)²·c(h)·(1+o(1)) with c(h) ≍ ‖ĥ‖²_{L²(lines)} > 0. **Positive and of order
(log T)².**

(ii) |PP(H)| ≤ Σ_{N} |G(N)|·(Λ⋆_{|Ψ|}Λ)(N) + (finite II–IV terms)
≤ C(a)·‖g‖₂²‖φ‖₂² = O_a(1): the sum runs over the O(e^{2a}) integers of the fixed
support, **with no growth in T**.

(iii) |[DP+PD](H)| ≤ C(a) and |DD(H)| ≤ C(a) e^{a/2}: finite sums and Mellin
evaluations off the line, bounded by Paley–Wiener with constant e^{O(a)},
**O_a(1) in T**.

(iv) |[PA+AP](H)| ≤ C(a)·log T and |[DA+AD](H)| ≤ C(a)·log T: a single
archimedean factor contributes a log.

*Proof.* (i): block (6) of Doc 107 §2.3 evaluated at H, with
Ĥ = |ĥ|² on the critical lines (Lemma 5.2(b) of Doc 107) and Ω(t) = −log|t| + O(1)
(Def. 1.3 of Doc 107, Stirling). (ii): Theorem 4.2 of Doc 107; the support of G bounds
N ≤ e^{2a}; (Λ⋆_{|Ψ|}Λ)(N) ≤ ‖Ψ‖_∞ (log N)·d(N)-trivial over a finite set.
(iii)–(iv): blocks (1)–(3),(5) of Doc 107 §2.3: the sums over n are confined to the
compact support; each factor A contributes ∫Ω·(rapid decay) ≪ log T on tests at
height T. ∎

**Theorem 3.3 (sub-resolution blindness: the archimedean side dominates where there is
nothing to see).** With fixed supports a and window tests at height T, there exists T₀(a)
such that for T ≥ T₀(a): Q₂(h,h) = AA(H)(1 + O_a(1/log T)) > 0. In particular,
**on tests of fixed support the index by high windows is 0 — unconditionally** — and the
first half of the step (1) falsifier of P42 ("if the archimedean block dominates, the
arithmetic side is irrelevant") holds **exactly in the regime where the index is
invisible**: archimedean domination and blindness are the same phenomenon.

*Proof.* Lemma 3.2: AA ~ c(h)(log T)² with c(h) > 0 bounded away from 0 on the
normalized concentrated class, and all other blocks are O_a(log T). ∎

Spectral consistency: with fixed support, ĥ has bandwidth ≥ 1/a fixed, does not
resolve individual zeros, and the hyperbolic planes of the window (Prop. 2.3) are not
alignable: the on×on sea (which is what AA measures at leading order) dominates. There is
no contradiction between Theorem 3.3 and Prop. 2.3: Lemma 2.4 uses tests whose
localization η and whose polynomial factors require **support growing with T**.

### 3.3. Size hierarchy II: resolution regime (a ≍ c·log T) and the two-worlds
argument

To align a test with a hyperbolic plane of the window W_{T,Δ} one must separate
spectral points at distance ≍ 1/log T (zero spacing) or distinguish
Re σ = ½ ± δ/2 from ½: by Paley–Wiener, bandwidth 1/log T requires a ≳ log T. In that
regime the prime sums run up to e^{O(a)} = T^{O(1)} and the bounds (ii)–(iii) of
Lemma 3.2 are no longer O(1): all blocks can reach order (log T)². Who then
controls the index? The answer needs no new estimates: it is given by the identity
itself.

**Theorem 3.4 (the two-worlds argument: necessity of second-order precision).** Let
E(g,φ) := DD + AA − DA − AD (the prime-free blocks: explicit functionals of
(ĝ, φ̂, Ω), identical in either world) and Π(g,φ) := PP + PA + AP − DP
− PD (the blocks with primes), so that Q₂(h,h) = E + Π. Suppose an
**unconditional arithmetic certificate** — a theorem about Π valid with no hypothesis —
implies κ(Q₂; window tests W_{T,Δ}) ≤ f(W) with f(W) = o(n_W) for every window.
Then that certificate distinguishes the value of Π, on the realizing tests of
Lemma 2.4, with precision
$$|Π_{\neg RH} - Π_{RH}| \;\gtrsim\; m\,n_W \cdot \|h\|_W^2
\qquad \text{against } E ≍ n_W^2\,\|h\|_W^2,$$
i.e., **relative precision o(1/log T) uniform in T**; and in fact the certificate
implies RH.

*Proof.* E depends only on (g,φ) and on archimedean data: it takes the same value
in the RH world and in the ¬RH world. The entire difference between worlds lives in Π (which
equals, by the identity, Σ_{ρ₁,ρ₂} − E). In the ¬RH world, the J = (1−o(1))·8mΔπ^{-1}
log T tests of Lemma 2.4 satisfy Q₂ < 0, i.e. Π < −E in each one; in the RH world
the same (g,φ) give Q₂ ≥ 0, i.e. Π ≥ −E. The separation between the two values of Π is
at least the negative mass of the planes, which is ≍ m n_W per normalized test-family,
while E ≍ n_W² (Theorem 3.3 persists at leading order: the on×on sea). A
certificate that forces κ ≤ o(n_W) must exclude the ¬RH value of Π in at least
(1−o(1))J of those directions: it must localize Π with relative error o(m n_W / n_W²) =
o(1/log T). And since under ¬RH the true value of Π is the ¬RH-world one, an
unconditional theorem with that precision is false under ¬RH unless ¬RH is false: the
certificate implies RH. ∎

**Answer to the step (1) falsifier of P42 (exact formulation).** The archimedean
block dominates and renders the index invisible at sub-resolution (Theorem 3.3); at
resolution, the index **is** controlled by the arithmetic side — but at **second
order**: by the deficit of Π relative to its archimedean prediction, with signal
m·n_W against mass n_W². Neither branch of the falsifier as originally
written: the arithmetic side is not irrelevant, but the control it requires is not of
bound type (size) but of evaluation type (second order). This triggers exactly the risk
P42 §6.2 flagged.

### 3.4. Refutation of the sign-change heuristic, and the correct kernel

**Remark 3.5 (K(N) has no sign changes).** Step (1) of P42 proposes
"bound the index by the number of sign changes of the arithmetic kernel
K(N) = Σ_{d|N}Λ(d)Λ(N/d)φ(d²/N)". But for φ ≥ 0 (and the reference thickenings
are), K(N) ≥ 0 for every N: **zero sign changes**, while κ > 0 under ¬RH. The
literal heuristic is false: Q₂ is not a form of Hankel/Toeplitz type whose index counts
oscillations of the symbol; the oscillation that carries the index is in the test
functions (frequencies T, γ₀), not in the kernel.

**Definition 3.6 (deficit kernel).** The object whose signs do govern the index is
$$ΔK_φ(N) \;:=\; (Λ⋆_φΛ)(N) \;-\; \mathbb{E}_∞[(Λ⋆_φΛ)](N),$$
where 𝔼_∞ is the polar/archimedean prediction (the continuous integrand that produces
the blocks DD−DA−AD+AA when inserted in the same sum: explicit, with no zeros). By the
identity of §3.1, the weighted sums of ΔK against oscillating tests are exactly the
fluctuations of pairs of zeros: ΔK is the almost-prime embodiment of pair
correlation. The correct question of step (1) — "what condition on K(N) would give
κ(Q₂^rel) ≤ f(2)?" — is answered: **a second-order asymptotic of ΔK, uniform in
the test frequency** (§4), not any size or sign property of K.

---

## 4. (iii) The necessary bound, stated exactly

### 4.1. The order-k functional

For k ≥ 2, with g ∈ C_c^∞(ℝ₊*) and Φ ∈ C_c^∞((ℝ₊*)^{k−1}) (transverse weight in the
coordinates v_i = x_i/x_{i+1}), the k-prime block of the main quadrant is
$$S_k(g,Φ) \;:=\; \sum_{n_1,\dots,n_k \ge 2} Λ(n_1)\cdots Λ(n_k)\;
g(n_1\cdots n_k)\,Φ\!\Bigl(\tfrac{n_1}{n_2},\dots,\tfrac{n_{k-1}}{n_k}\Bigr)
\;=\; \sum_{N} g(N)\,(Λ^{\star_Φ k})(N),$$
with (Λ^{⋆_Φ k})(N) := Σ_{N = n₁⋯n_k} Λ(n₁)⋯Λ(n_k) Φ(n₁/n₂, …, n_{k−1}/n_k), supported
on the semigroup of k-almost-primes with balanced factorization (each n_i ≍ N^{1/k} on
the compact support of Φ). It is the functional of Doc 107 §6.5; for k = 2,
S₂(g,φ) = S(g,φ) = Σ_N g(N)(Λ⋆_φΛ)(N).

### 4.2. The main term: PNT slot by slot, with no singular series

**Theorem 4.1 (static asymptotic, unconditional).** For fixed g, Φ (with no imposed
oscillation) with supports in [e^{−a}, e^{a}]^{...}, X := e^{a}:
$$S_k(g,Φ) \;=\; \hat g(1)\,\widehat Φ(0,\dots,0)\;+\;
O_k\!\left( \|g\|_{\infty}\,\|Φ\|_{C^1}\; X \,e^{-c (\log X)^{3/5-\varepsilon}} \right),$$
where ĝ(1) = ∫g(x)dx and Φ̂(0) = ∫Φ(v) d*v (transforms at the polar points). For
k = 2 this is S(g,φ) = ĝ(1)·φ̂(0)·(1 + error) in the Lebesgue×Haar normalization of
the change (u, v) (the ½ of the Jacobian is absorbed following the convention of Doc 107,
Lemma 3.3; in the block presentation, the main term of PP coincides
exactly with the ĝ(1)φ̂(0)-type summand of DD — the classical pole/prime
cancellation, doubled).

*Proof.* Induction over the slots: Σ_{n_k} Λ(n_k) G_{n_1..n_{k-1}}(n_k) with
G smooth of compact support is evaluated by PNT with Vinogradov–Korobov error
(ψ(x) = x + O(x e^{−c(log x)^{3/5−ε}}); [IK04, Cor. 8.30]) and partial summation; the main
term replaces Λ by 1·dx in each slot; the change of variables of Lemma 3.3 of
Doc 107 (and its k-version, §6.5) separates the integrals. ∎

**Remark 4.2 (no singular series: the correlation is multiplicative).** The analogue
of Goldston–Yıldırım for **additive** correlations Σ Λ(n)Λ(n+h) carries the
singular series 𝔖(h) (congruence interaction between n and n+h) and is **conjectural**
[GY03 for the approximants; the full asymptotic is Hardy–Littlewood]. Here the
correlation is **multiplicative** — (n₁, …, n_k) ↦ n₁⋯n_k — and imposes no
cross-congruence condition: the arithmetic constant is 1 and the static asymptotic
is an **unconditional theorem** (Theorem 4.1). The diagonal regime d ≈ √N that the
weight φ(d²/N) imposes is not a difficulty for the asymptotic: it restricts it to balanced
semiprimes, which are counted by PNT² (density ~ 2 log(b/a)·X/log²X for ratio in
[a,b], weighted to c·X with log·log weights). **Sieving is not even necessary for this.**
All the difficulty of the bridge lies, by Theorem 3.4, elsewhere: in uniformity
in frequency.

### 4.3. The conjecture step (2) needs

By Theorem 3.4, the certificate must evaluate the deficit on oscillating tests. The
exact formulation (form k = 2; the general k is identical with S_k and the
vector transverse weight):

**Conjecture 108-N (necessary bound; exact statement).** *There exists δ(T) → 0 such that for
every T ≥ 2, every fixed A ≥ 1, and all g, φ ∈ C_c^∞ with supports in
[e^{−A log T}, e^{A log T}] and normalization ‖g‖_{H} := ‖ĝ(½+it)‖_{L²(dt)} +
‖t·∂_t ĝ‖_{L²} ≤ 1 (likewise φ):*
$$\Bigl|\, S(g,φ) \;-\; \hat g(1)\hat φ(0) \;-\; \mathcal{A}_∞(g,φ) \,\Bigr|
\;\le\; δ(T)\,\log T, \tag{4.1}$$
*where 𝒜_∞(g,φ) is the explicit archimedean prediction (the combination
−AA−PA−AP+DA+AD+DP+PD of the continuous blocks evaluated per (3.1), computable with no
zeros). Required uniformity: in T (the oscillation frequency of g and φ is free up to
T), in A (polynomial scale X = T^A), and over the whole ball of the ‖·‖_H norm — not only
over a cone.*

Three clarifications requested by the goal's statement:

(a) **Operator norm or cone?** It must be over the whole ball (operator norm). The
realizing cone — the (g,φ) aligned with the hyperbolic planes — is parametrized
by the positions (δ, γ₀, and the neighboring on-line γ's), which are **unknown**: a
certificate restricted to a cone known in advance cannot cover the realizing
cone without uniformity over the alignment parameter, which amounts to the whole
ball (at most with polynomial losses in the Sobolev norm, irrelevant against the
log hierarchy).

(b) **Uniformity in k?** Yes: the P42 bridge needs f(k) subexponential with the
same source; the k-version of (4.1) has signal m·k·n_W^{k−1} against mass n_W^k:
relative precision o(k/log T) — apparently weaker for large k, but see
Proposition 7.3: the gain is illusory because the transverse budget grows in
step.

(c) **Size of the main term and of the signal.** Main term of S at frequency 0: ĝ(1)φ̂(0)
(Theorem 4.1). In the oscillating regime of (4.1), ĝ(1) and φ̂(0) are negligible
(rapid decay away from the window): S is **pure fluctuation**, its predictable
part is 𝒜_∞ ≍ (log T)² (the sea of pairs), and the signal to resolve is
≍ m log T — relative o(1/log T), as in Theorem 3.4.

### 4.4. The conjecture is RH in disguise (test of item (vi), anticipated)

**Theorem 4.3.** Conjecture 108-N implies RH.

*Proof.* Suppose ¬RH (toy with m ≥ 1; the general case with Hypothesis D is
identical window by window). Take the realizing tests of Lemma 2.4 in the
window W_{T,Δ} with T → ∞: they satisfy Q₂(h,h) ≤ −c·m·‖h‖²_W with archimedean
mass E ≍ n_W². By identity (3.1), S(g,φ) (plus the remaining prime blocks, which
are bounded likewise or incorporated into 𝒜_∞ by the same pattern) differs from its
prediction ĝ(1)φ̂(0) + 𝒜_∞ by at least the negative mass of the planes: ≫ m·log T. This
contradicts (4.1) with δ(T) → 0 for large T. Hence ¬RH is impossible. ∎

By the program's test (Doc 99, discriminator I2a; list of program equivalences): a
"Lemma 108" whose statement directly implies κ_W ≡ 0 — which is the spectral
equivalent of RH (P35/Doc 96) — **is not a lemma: it is the conclusion**. Outcome
(B) of the goal is thereby ruled out: any candidate with the uniformity
of (4.1) is disqualified as an "expectable theorem"; see §6 for the fine measurement and §8
for what remains.

---

## 5. (iv) Unconditional inventory: what sieves, identities, and the large sieve give today

### 5.1. Selberg's sieve / Λ₂

**(a1) The analogous additive problem.** The classical Selberg bound (1947; [HR74, Ch. 3];
modern expositions: Tao, 254A Notes 4) gives
$$\sum_{n \le X} Λ(n)\,Λ(n+h) \;\le\; (8 + o(1))\,\mathfrak{S}(h)\,X,$$
**factor 8** over the Hardy–Littlewood prediction 𝔖(h)X. Verified: the 8 is the
value of the pure Selberg method (π₂(x)/Π_{HL}(x) ≲ 8); the version via Montgomery–
Vaughan's analytic large sieve removes error terms and later refinements lower the
constant (≈ 7 and improvements; exact values of the improvements
[NOT VERIFIED in detail; not load-bearing]). The "factor 4" that circulates corresponds to
another normalization (Brun–Titchmarsh/Bombieri–Davenport-type bounds compared with
X/log²X without the twin constant) [exact origin NOT VERIFIED; not load-bearing]. What is
load-bearing is: **the sieve gives relative precision O(1) — an absolute constant > 1 —
over the main term, and only for non-negative weights.**

**(a2) Transport to S(g,φ).** For g, φ ≥ 0 the bound transports trivially — but
there is no need: Theorem 4.1 gives the **asymptotic** (constant 1) because the correlation
is multiplicative. The diagonal regime d ≈ √N is not that of the sieve but that of PNT²:
the divisors of N in [c₁√N, c₂√N] with both cofactors prime. Ford's theory of
H(x,y,z) [For08] — #{n ≤ x : ∃ d|n, d ∈ (y, 2y]} ≍ x/(log y)^{δ}(log log y)^{3/2} with
δ = 1 − (1+log log 2)/log 2 ≈ 0.086 — bounds the **support** of the sieve relaxation
without weights for Λ (the integers with some balanced divisor): it is relevant if one
replaces Λ⋆Λ by a sieve majorant Λ_R⋆Λ_R, whose support thickens exactly to that
Ford-thin set; it records that the majorization loses structure (the majorant lives on a
(log)^δ-denser support than the semiprimes) — another sign that the
"majorize" direction is not the one the bridge needs.

**(a3) What the sieve cannot give, by construction.** Sieve bounds are
**non-negative-weight** inequalities: majorizing Σ a_N K(N) by Σ a_N (majorant) requires
a_N ≥ 0. The index tests have oscillating g (frequency T): the sieve bounds
Σ |g(N)| K(N) — the L¹ mass, of size X·‖·‖ — when what is needed is the cancellation of
Σ g(N) ΔK(N) down to o(log T). Distance: **it is not the constant 8 vs. 1; it is that the sieve
bounds the wrong norm.** The parity problem, as P42 §6.2 anticipated, is
effectively irrelevant here (it does not even block the static asymptotic, Rem. 4.2);
the operative barrier is something else.

### 5.2. Vaughan / Heath-Brown

S(g,φ) = Σ_{m,n} Λ(m)Λ(n) g(mn)φ(m/n) with m ≍ n ≍ √X **already is** a type-II
bilinear sum in the optimal balanced regime — there is nothing left to decompose (the
Vaughan [Vau77] and Heath-Brown [HB82] identities serve to bring sums of Λ into this
regime; here we are born in it). The question is whether type-II machinery gives
cancellation against the specific kernel: g oscillating at frequency T in mn, φ (perhaps)
at frequency γ in m/n. Two exact structures:

(i) If φ̂ concentrates at τ = iγ (real sums of Corollary 5.6 of Doc 107), the
kernel separates: φ(m/n) ≈ (m/n)^{iγ}φ₀(m/n), and
S ≈ Σ_m Λ(m) m^{iγ} w₁(m) · conj(Σ_n Λ(n) n^{iγ} w₂(n))-type plus coupling via
g(mn): Dirichlet polynomials of Λ at unknown frequency γ, scale √X.

(ii) If ĝ oscillates at frequency T (high windows), S is Σ_N (Λ⋆_φΛ)(N) N^{−iT}-type:
the truncated polynomial of (ζ'/ζ)².

What the technique gives unconditionally: **mean values**. The Montgomery–Vaughan
mean value theorem [MV74],
∫_0^{T_0} |Σ_{n≤X} a_n n^{it}|² dt = (T_0 + O(X)) Σ|a_n|², gives square-root
cancellation **on average over t** for X ≤ T_0^{1−ε}: the asymptotic (4.1) holds for
**almost every** window (outside an exceptional set of measure o(T₀)). What the
technique does not give: the individual window. The step from "almost every" to "every" is
large-values / zero-density theory — and under ¬RH the polynomial (i)/(ii) **is**
large exactly at the frequencies of the off zeros: the exceptional window is not a
defect of the method, **it is the signal itself**. A theorem "with no exceptional windows" at
precision (4.1) implies RH (Theorem 4.3).

### 5.3. Large sieve / Montgomery's inequality; F(α,T)

The large sieve provides exactly the input of §5.2 (it is the source of the MV74
mean value). On the restricted form Q₂ there is no direct spectral bound: the large
sieve bounds averaged second moments of linear evaluations, i.e.,
**traces of compressions averaged over windows** — again the average, not the supremum.
The dictionary with pair correlation (Doc 107, Rem. 3.8): the two-test-function
version of Montgomery's F(α,T) [Mon73]. The honest status of F(α,T):
the asymptotic F(α,T) = (1+o(1))T^{−2α}log T + α + o(1) for 0 ≤ α ≤ 1 is proved
**under RH**; unconditionally only partial/averaged versions exist. The errors
of the RH version are o(1) **relative** (first order); the lower-order terms
of pair correlation (the arithmetic ones, beyond GUE) are of relative order
1/log T and remain **conjectural** even under RH [BK96; MS04]. (4.1) requires
precision o(1/log T): **one order below what pair-correlation theory even states
conditionally as a theorem.**

---

## 6. (v) Measuring the distance

### 6.1. Available vs. necessary table

| input | type | relative precision | uniformity in frequency | weights |
|---|---|---|---|---|
| Selberg/Λ₂ (§5.1) | upper bound | O(1) (factor 8) | n/a (no oscillation) | ≥ 0 |
| PNT² (Thm. 4.1) | asymptotic | e^{−c(log X)^{3/5}} | **fixed frequency only** | free |
| Vaughan/HB + MV74 (§5.2) | asymptotic on average | square root on average | **almost every window** | free |
| F(α,T) under RH (§5.3) | asymptotic | o(1) relative | averaged over [0,T] | fixed class |
| **necessary: (4.1)** | **asymptotic** | **o(1/log T)** | **every window, every T** | **whole ball** |

### 6.2. Which outcome occurs

**(A) — ruled out with proof.** The available sieve bound does not imply control of the
index: it bounds the wrong norm (§5.1(a3)) and its relative precision is O(1) when
o(1/log T) is needed (Theorem 3.4). Moreover the mechanical heuristic of step (1) (sign
changes of K) is false (Rem. 3.5).

**(B) — ruled out.** It is not "same form, different constants": the available form is
*upper bound of mass with positive weights / asymptotic on average*, the necessary one is
*uniform second-order evaluation with oscillating weights*. There is no "Lemma 108" with
the same form and a better constant: closing the constant gap (8 → 1+o(1)) gets us
nowhere (the static asymptotic is already there, Theorem 4.1, and is not enough); closing the
uniformity gap is Theorem 4.3: RH. The only identifiable intermediate statement — the
constant version of (4.1), which would give κ_W ≤ C·n_W and from there the density
bound m ≤ C/2 — requires the **same** second-order precision with a constant instead of
o(1): the signal m·n_W must likewise be distinguished from the mass n_W²; it is behind the
same wall (see §8.2).

**(C) — is what occurs, aggravated.** The necessary bound is of asymptotic type (exact
main term to second order), uniform over windows. The nominal wall anticipated by
P42 §6.2 was "pair correlation (Montgomery–Goldston): an evaluation barrier, not a
sign barrier." This document's precise measurement aggravates it by two degrees:

1. **Degree of uniformity**: what is needed is not the pair-correlation asymptotic
   in its standard form (averaged in T, which is how it is stated and how it would be
   proved), but its form uniform-in-each-window; that form implies RH
   (Theorem 4.3). The wall is not a neighbor of RH: it is RH.
2. **Degree of precision**: the signal lives at relative order 1/log T — the scale of
   the arithmetic lower-order terms of pair correlation, conjectural
   even under RH [BK96; MS04]. The sufficient asymptotic could be **false or
   inaccessible even in the RH world** with current technique: no known conditional
   statement covers it.

---

## 7. The transmutation, documented (Doc 99 pattern)

### 7.1. The chain

$$\text{sieve bound on } S(g,φ)
\;\xrightarrow{\ \S3.4\ }\; \text{evaluation of the deficit } ΔK
\;\xrightarrow{\ \text{Thm. 3.4}\ }\; \text{2nd-order asymptotic, uniform over windows}
\;\xrightarrow{\ \text{Thm. 4.3}\ }\; \text{RH}.$$

In the program's taxonomy: Missing Lemma 6.1 of P42 (step (1)+(2)) **transmutes**
— not to CAP (there is no RH-equivalent positivity involved; consistent with what was
anticipated in Doc 107 §6.4(γ)) but to the wall of **mean/uniform-in-the-window-
parameter uniformity**, which is exactly the interior/boundary structure of the P41
no-go: the interior (almost every window) is an unconditional theorem (MV74/large
sieve); the boundary (every window, including those aligned with the unknown zeros) is RH. The
novelty relative to the previous map: the pair-correlation wall, once measured, did not
turn out to be a wall distinct from the P41 boundary — **it is the same boundary with
sieve coordinates.**

### 7.2. Exact parallel with Form C

P42, Theorem 2.1 (Form C): the anchored density that would force RH and the zero-density
ceiling N(σ,T) = O(T^{κ(σ)}) that bounds it carry the same exponent: self-blocking.
Here: zero-density theorems are precisely the **averaged-over-windows** half of the
statement κ_W ≤ C (they say almost every window is free of off zeros); the uniform
half is RH. The Form B amplifier self-blocks with the same geometry: what can be
proved improves both sides of the inequality at once.

### 7.3. Why amplification in k does not help

**Proposition 7.3 (the boundary is k-invariant).** For every fixed k ≥ 2, the index by
windows of Q_k under ¬RH grows unboundedly over the windows (the (k−1)-tuples on-line
with one off factor populate every window, with multiplicity ≍ k·m·n_W^{k−2}·(transverse
budget); the mechanism is that of Lemma 2.4 slot by slot), and under RH it is 0. Hence
the statement "κ_W(Q_k) ≤ f(k) uniformly in W" is RH-equivalent **for each
k separately**, and the P42 chain — 2mk ≤ κ ≤ f(k) with f(k)/k → 0 — never gets to
use the amplification: its premise (b) is already the conclusion at k = 2. This is the
quantitative form, on the realized object, of the sterility lemma (Doc 106, Prop. 3.6):
the analytic realization did not provide the second source; it provided another
presentation of the same source.

*Proof (sketch, same status as Lemma 2.4).* The order-k signal in the window
W: tuples with exactly one off slot and k−1 aligned on-line; the involution acts
freely in the off slot: hyperbolic planes; count ∝ m·(local density)^{k−2}
limited by the transverse bandwidth of Φ̂ — a geometric budget that grows
with the support of Φ. The signal/mass ratio is k·m/n_W for fixed transverse
budget: the ratio improves linearly in k, but widening the transverse budget to
exploit large k re-inflates the on^k mass in the same proportion (each new
transverse direction multiplies mass and signal by the same density factor): the
signal/mass ratio in the realizing regime is ≍ m/n_W **independent of k** after optimizing.
The exact optimization is not claimed as a theorem; what is load-bearing is the easy half:
for each k, under ¬RH the index by windows is unbounded (one family suffices, the
one with a single off slot and minimal transverse budget), which already gives the
RH-equivalence of the bound uniform in fixed k. ∎

### 7.4. Where MW-7 reappears

Doc 107 proved that MW-7 (the Hadamard barrier: needing the positions of the
zeros) does not reappear **in the functional** W₂. This document locates where it does
reappear: **in the block structure of the quadratic form**. The relative off×off block —
the only finite and amplifiable invariant — is a spectral compression; separating it from
the off×on contamination within the same window requires knowing which pairs of the
window are off×off, i.e., the positions. The arithmetic side computes the **total**
of the window (that is autonomy, and remains true); it does not compute the **partition**
into blocks (that is MW-7, and it is what the relative index needs). The program's
formula: *autonomy of the value ≠ autonomy of the inertia.*

---

## 8. (vi) Does any "Lemma 108" survive? What remains

### 8.1. The formal candidate (B), and its dismissal

For the record, the statement that would have been Lemma 108 had the outcome been (B):

> **(Lemma 108, not viable.)** There exists an absolute C < ∞ such that for every T, Δ and every
> orthonormal family {h_j} of window tests W_{T,Δ}: the number of j with
> Q₂(h_j,h_j) < 0 is ≤ C·n_W, with C independent of T and of the configuration of zeros.

Plausibility against the literature: by Theorem 3.4 (with f(W) = C·n_W instead of
o(n_W), the same proof mutatis mutandis), proving it requires evaluating Π with
relative precision O(C/log T) — the same second-order scale; and its consequence
(§8.2) would already be a zero-density theorem of new strength. Applying the
program's test: it is not an expectable theorem with current technique (it is at the
scale of the arithmetic lower-order terms of pair correlation, conjectural under RH), and it
is not exactly RH in disguise (with C ≥ 2 it does not imply m = 0) — it is a
respectable **open problem of quantitative-pair-correlation type**, but not a bridge:
even if proved, it kills only m > C/2, and uniformity in k (Prop. 7.3) does not amplify it.

### 8.2. The genuine byproduct: a density bound on quadruples per window

**Remark 8.1.** The chain κ_W ≤ C·n_W ⇒ 2m·n_W(1+o(1)) ≤ C·n_W ⇒ **m ≤ C/2** is
correct (Prop. 2.3). That is: a linear-in-density bound on the index by windows would
imply an absolute bound on the number of off-critical quadruples — a statement stronger
than any known density theorem in that region (the N(σ,T) give o(T) off zeros up to
height T, not an absolute bound). This confirms, by methodological reductio, that
κ_W ≤ C·n_W cannot be cheap. It is recorded as a long-term target, outside the
scope of Form B.

### 8.3. What remains alive in the apparatus

(1) **The functional W_k as an identity machine**: the block-arithmetic = pairs-of-
zeros identity with two test functions (Doc 107) generalizes the
Montgomery/Goldston–Montgomery dictionary and is correct and unconditional; it has
independent interest apart from the bridge (e.g. for reformulating lower-order terms of
pair correlation as almost-prime deficits ΔK, Def. 3.6 — a reformulation, not
progress, but a clean one). (2) **Theorem 3.3 (sub-resolution blindness)**: unconditional
positivity of Q₂ on fixed-support tests in high windows — a genuine fragment
of doubled Weil positivity, new though modest. (3) **Remark
4.2** (the multiplicative correlation has no singular series and its static asymptotic
is a theorem): precisely delimits that the hard arithmetic content of the double object
lies entirely in frequency uniformity, not in the arithmetic of the
almost-primes.

---

## 9. VERDICT

**VERDICT: BRIDGE DEAD.**

**Exact location of the wall.** Missing Lemma 6.1 of P42 dies at its step (1), and
the mode of death is the one foreseen as a risk in P42 §6.2, aggravated:

1. The invariant κ(Q₂^rel) (off×off block, finite, amplifiable) **is not
   test-accessible**: what the test class and the arithmetic side can see are the
   indices by windows of the full form, which are binary — 0 in every window under
   RH, ≍ m·log T (unbounded) under ¬RH (Prop. 2.3, Lemma 2.4, Prop. 2.5). Any
   finite uniform bound is RH, already at k = 2: there is nothing left to amplify (Prop. 7.3:
   the sterility of Doc 106 reappears on the realized object).

2. The literal mechanism of step (1) (index ≤ sign changes of K(N)) is **false**:
   K ≥ 0 with no sign changes, index > 0 under ¬RH (Rem. 3.5). The corrected
   mechanism (deficit ΔK) requires evaluation, not majorization.

3. The necessary sieve bound is of type **second-order asymptotic, uniform over
   windows** (Conjecture 108-N, eq. (4.1)): relative error o(1/log T), uniform in the
   frequency T and over the whole ball of tests. It implies RH (Theorem 4.3): it fails the
   "RH in disguise" test. And its precision is at the scale of the lower-order
   terms of pair correlation, conjectural even under RH: the outcome is the
   (C) of the goal, with the aggravation that the nominal wall (Montgomery–Goldston) is,
   once measured, the same mean/uniform boundary of the P41 no-go — not a new wall.

4. The measured distance to the unconditional inventory: Selberg gives relative precision
   O(1) (factor 8) in the wrong norm (mass with positive weights); PNT² gives the
   exact asymptotic but only at fixed frequency (Theorem 4.1 — the sieve is not even
   needed there); Vaughan/Heath-Brown + Montgomery–Vaughan's mean value give the
   asymptotic **on average over windows** (almost every window); the exceptional window
   that the average does not control is exactly where the signal lives. The gap is not a
   constant or a logarithm: it is the quantifier.

**What is gained.** The map: Form B is closed off by the same type of boundary that
closed Forms A and C — with the additional precision that its candidate "second
source" (almost-prime sieve bounds) turned out to be the averaged presentation of the same
spectral source, not an independent source; the analogue of Deligne's rationality
did not appear. Surviving as byproducts: Theorem 3.3 (unconditional sub-resolution
positivity of Q₂), the ΔK ↔ pair-correlation identity with two test
functions, and the long-term target κ_W ≤ C·n_W ⇒ m ≤ C/2 (§8.2), recorded outside
Form B.

**Next step (outside this bridge).** None within Form B via this route. If
the program continues, the only direction not ruled out by this document is the
one flagged in §8.2/§5.3: the study of pair-correlation lower-order
terms as almost-prime deficits — territory for honest partial theorems, with no
claim toward RH.

---

## References

**Internal (backward-only):** P42 (§6: Missing Lemma 6.1, steps (1)–(3) and falsifiers;
§2 Theorem 2.1 Form C); Doc 107 (Theorems 2.4, 3.4, 4.2, 4.4, 5.5; Lemmas 2.2, 3.3,
5.2, 5.4; Cor. 3.6, 5.6; Rem. 3.8, 4.5, 5.3; Prop. 6.1; §6.4–6.5; Missing Lemma 7.2);
Doc 106 (Prop. 3.4, 3.5, 3.6; Rem. 3.9; Missing Lemmas 5.2/5.3; Problem 5.4); Doc 99
(transmutation pattern; discriminator I2a); Doc 96 (Theorem 8.1); Doc 94 (condition
C5); Doc 98 (toy model); P41 (interior/boundary no-go); P35 (Weil form, κ = 2m).

**Literature (verifiable):**
- A. Selberg, upper-bound sieve and π₂(x) ≲ 8·Π_{HL}(x) (1947); exposition in
  H. Halberstam, H.-E. Richert, *Sieve Methods*, Academic Press, 1974, Ch. 3. The
  factor 8 confirmed in modern expositions (T. Tao, 254A Notes 4: Some sieve
  theory; G. Oh, Applications of the Selberg sieve, Princeton notes). Refinements
  below 8: [exact constants NOT VERIFIED; not load-bearing].
- H. L. Montgomery, R. C. Vaughan, *The large sieve*, Mathematika **20** (1973),
  119–134; and the mean value theorem for Dirichlet polynomials
  (Montgomery–Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) **8** (1974),
  73–82). [MV74]
- R. C. Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci.
  Paris Sér. A **285** (1977), 981–983. [Vau77]
- D. R. Heath-Brown, *Prime numbers in short intervals and a generalized Vaughan
  identity*, Canad. J. Math. **34** (1982), 1365–1377. [HB82]
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos.
  Pure Math. **24**, AMS (1973), 181–193. [Mon73] (F(α,T): asymptotic for 0 ≤ α ≤ 1
  **under RH**.)
- D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short
  intervals*, Progr. Math. **70**, Birkhäuser (1987), 183–203. [GM87]
- D. A. Goldston, C. Y. Yıldırım, *Higher correlations of divisor sums related to
  primes I*, Proc. London Math. Soc. (3) **87** (2003) [reference for the main-term
  technology with singular series for additive correlations; bibliographic
  details of the volume NOT VERIFIED here; not load-bearing]. [GY03]
- K. Ford, *The distribution of integers with a divisor in a given interval*, Ann. of
  Math. (2) **168** (2008), 367–433; H(x,y,2y) ≍ x (log y)^{−δ}(log log y)^{−3/2},
  δ = 1 − (1+log log 2)/log 2 ≈ 0.086. [For08]
- E. B. Bogomolny, J. P. Keating, lower-order terms of pair correlation
  beyond GUE (1995–96, *Gutzwiller's trace formula and spectral statistics* /
  Nonlinearity) [exact article identification NOT VERIFIED; what is cited — that the
  arithmetic lower-order terms are conjectural and of relative order 1/log —
  is standard]. [BK96]
- H. L. Montgomery, K. Soundararajan, *Primes in short intervals*, Comm. Math. Phys.
  **252** (2004), 589–617 (lower-order terms of prime variances /
  correlations). [MS04]
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004
  (Thm. 5.8: N(T); Thm. 5.12: explicit formula; Cor. 8.30: PNT with
  Vinogradov–Korobov error). [IK04]
- J. Friedlander, H. Iwaniec, *Opera de Cribro*, AMS Colloq. Publ. 57, 2010 (parity:
  blocks signed asymptotics, not upper bounds; here it turned out not to be the
  operative wall).

*End of Doc 108.*
