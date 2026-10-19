# Doc 112 — The dichotomy: rigorous attack on m < ∞ ⟹ m = 0

**Program:** Riemann Hypothesis — Phase 37, "physical mode"
**Prerequisites:** Doc 109 (dichotomy D-109; identity RH = (m<∞) ∧ (m∈{0,∞}); mean-square→pointwise gap, §4.4; Bagchi precedent, §4.3); Doc 110 (Prop. 4.5: a priori finite rank ⟹ autonomous inertia via Newton/Jacobi–Frobenius; axiom L6; infinite-rank/a-priori-finite-rank boundary); Doc 111 (Prop. 2.2: cosh-examples with finite m without Euler; Cor. 2.3: every proof of the dichotomy needs arithmetic input; §6: dichotomy budget/cost); Doc 104 (self-blocking amplifier, via P42 §2 and P43 Thm. C); Doc 102 (Bagchi: strong recurrence ⟺ RH; ω₀ and the Euler observable); Doc 98 (Cor. 2.4: cost 2δ²K_λ(γ₀) per quadruple); Doc 72 (T_λ via Weil's formula; structure verified at source for this document); Doc 105 (divergence of the prime series of B_λ); P43 (Principle 3.1, master quantifier; §4 value/inertia).
**Absolute rule:** no proof is fabricated. Every step is either a complete proof, a literature statement with a verifiable reference, or a declared GAP with exact location. No numerics, no simulations. Backward-only citations; what is unverified is marked [UNVERIFIED].

---

## 0. Executive summary

**The goal.** Hypothesis H(m): ζ has exactly m off-critical quadruples of zeros
{½ ± δ_j ± iγ_j : j = 1,…,m}, with 0 < m < ∞. Derive a contradiction. By the
architectural identity of Doc 109 (§4.5), this is exactly the D-109 half of RH:
RH = (m<∞) ∧ (m∈{0,∞}); the present document attacks the implication m<∞ ⟹ m=0 with
finiteness as the working hypothesis — the first time in the program that finiteness is
on the side of the inputs and not of the goals.

**Findings, in order:**

1. **(§2) The Bohr–Rouché argument, frozen by H(m), reduces to A SINGLE pointwise lemma
   (LP-112), and everything else is theorem.** The B² almost-periodicity of ζ on each
   line σ ∈ (½,1) is unconditional (Lemma 2.1), its almost-periods are relatively dense
   (Lemma 2.2), and H(m) freezes every constant of the Rouché step: if there exists ONE
   unbounded sequence τ_k with ζ(s+iτ_k) → ζ(s) uniformly on a fixed disk around an
   off-critical zero, then m = ∞ (Theorem 2.3, complete proof). The hypothesis m < ∞
   does two real things: it eliminates any need for uniformity in (δ, γ₀) — the
   constants are fixed positive numbers — and it turns ONE replica into a contradiction.

2. **(§2.4) The B²→pointwise step is not merely a gap: the distributional direction is
   proved AGAINST it.** Proposition 2.6 (new in this form, assembled from Bagchi +
   Hurwitz): under H(m), the set of τ that are good for Rouché in the disk of the
   off-critical zero has **upper density ZERO**. The B² almost-periods have positive
   density, but their goodness is an average in t that assigns zero weight to the fixed
   window of the zero (the Besicovitch seminorm annihilates compacts, Obs. 2.4); the
   pointwise goodness in the fixed disk is a density-zero event. The hope of "drawing a
   τ from a set of positive measure" is structurally false: the relevant set is of
   density zero, and exhibiting one of its elements is the master quantifier of P43 in
   almost-period coordinates.

3. **(§2.5) D104's blockage does NOT apply.** D104's amplifier self-blocked because it
   needed positive density of replicas and the ceiling N(σ,T) = O(T^κ) capped it with
   the same exponent. The sequential version needs ZERO density of replicas
   (#{k: τ_k ≤ T} arbitrarily rare), which no density theorem obstructs (Prop. 2.7). The
   route is not self-contradictory: it is simply unfed. This is a genuine difference and
   the reason LP-112 remains alive as a non-RH-equivalent target.

4. **(§3) The Euler product enters at three exact places, and D111's cosh-examples are
   excluded at the first.** (i) The Dirichlet series gives the B² almost-periodicity —
   the cosh-examples are not even B² on vertical lines (Lemma 3.1) and admit no
   self-approximating sequence (Lemma 3.2: |F(s+iτ)| → ∞ in the disk). (ii) The
   ℚ-linear independence of {log p} — unique factorization, pure and unconditional
   arithmetic — makes the almost-periods relatively dense and non-discrete (Lemma 3.3):
   the replicas fall at NEW heights, while a discrete group of exact periods maps the
   zero set onto itself and does not multiply m. (iii) The random Euler product
   determines the support of Bagchi's limit theorem — the input of Prop. 2.6 and of the
   direction RH ⟹ strong recurrence. Doc 111's requirement (Cor. 2.3) is satisfied by
   the ROUTE: its input is exactly what class ℰ lacks.

5. **(§4) The Newton moments/traces line collapses at two independent places, neither
   where it was feared.** Verified against Doc 72 at the source: B_λ(log p) =
   ∫W_λ(s)cos(s log p) dm_∞(s) is the Fourier transform of the test — autonomous, it does
   NOT depend on the zeros; the fear that "B_λ depends on all the zeros" is unfounded.
   The real walls: (i) the prime series Σ_p (log p/√p)B_λ(log p) **diverges** (Doc 105:
   ≍ (5√2/8)log X) — D72's arithmetic formula is strictly formal and there is no
   autonomous value feeding the moment system; (ii) even conceding a regularization,
   the explicit formula is ONE identity that the true configuration satisfies
   identically — it does not overdetermine the 4m parameters (Prop. 4.2); the only
   extractable non-tautological content is of sign (positivity over a cone of tests),
   which is Weil's criterion, i.e. RH, i.e. the inertia of P43. Moreover (Obs. 4.3) the
   required precision is not fixed: the infimum over configurations of the spectral gap
   ε₀ ≍ δ_min² e^{−πγ_min/2} is 0 — uniformity over the hypothesis space restores the
   wall that H(m) seemed to have removed. Doc 110's Prop. 4.5 does not apply: H(m)
   gives finite rank, not finite rank **a priori** (the dimension 4m is the unknown,
   Obs. 6.3 of D111).

6. **(§5) The best provable theorem today is the exact reduction** (Theorem 5.1):
   **LP-112 ⟹ D-109**; combined with target L8: (m<∞) ∧ LP-112 ⟹ RH. LP-112 is
   strictly weaker than Bagchi's strong recurrence (unbounded sequence vs. positive
   lower density); it is implied by RH; and it does not imply RH through any known
   dictionary — its conclusion under ¬RH is m = ∞, consistent. The case m = 1 avoids
   nothing (§5.3); parameter-region versions add nothing to the classical free regions
   (§5.2).

**VERDICT (§7): PARTIAL IMPLICATION** — proved conditionally on a single open lemma
(LP-112), with a complete proof of the conditional, with the proof that the set of
witnesses of LP-112 has density zero under ¬RH (the wall located with sign: the
average→individual inversion in its exceptional-set form), and with the extension of
the no-go: the hypothesis m < ∞ freezes the constants but does not feed the construction
of the exceptional τ; the direct-B² and moments lines remain BLOCKED with exact
location.

---

## 1. Framework: the hypothesis H(m) and exactly what finiteness buys

### 1.1. Hypothesis and goal

**Hypothesis H(m).** ζ has exactly m off-critical quadruples, 0 < m < ∞:
$$Z_{\mathrm{off}} = \{\tfrac12 \pm \delta_j \pm i\gamma_j : j = 1,\dots,m\},
\qquad \delta_j \in (0,\tfrac12),\ \gamma_j > 0,$$
counted with multiplicity (Doc 111, Def. 1.1; the quadruple structure is a theorem:
functional equation + Schwarz reflection + absence of real zeros in (0,1)).

**Goal.** Derive a contradiction from H(m). That would prove m∈{0,∞} (D-109) and, with
the identity of Doc 109 §4.5, would reduce RH to target L8 (m<∞).

### 1.2. Inventory of what H(m) puts on the table

H(m) is an unusually rich hypothesis; it is worth listing precisely what it gives,
because each line of attack will use different pieces:

- **(F1) Frozen parameters.** δ_min := min_j δ_j > 0, γ_max := max_j γ_j < ∞,
  γ_min := min_j γ_j ≥ 3·10¹² (Platt–Trudgian, via D111 §2.4(c)). These are **constants
  of the hypothetical world**: no argument under H(m) needs uniformity in (δ, γ₀); the
  bounds may depend on the entire configuration.
- **(F2) RH-pure tail.** Every zero with |γ| > γ_max lies on the critical line. There is
  a "last" off-critical zero.
- **(F3) Finite rank.** The off-critical subspace 𝒦_off has dimension exactly 4m and
  κ(Q) = 2m (P35); the off mass of the discrepancy is concentrated at the m spectral
  points {γ_j} with weights controlled by δ_j (Doc 98).
- **(F4) Minimal contradiction threshold.** To refute H(m) it suffices to produce ONE
  additional off-critical zero (a new quadruple): m+1 > m. No positive density is
  needed, not even direct infiniteness — a single replica above γ_max, at distance > 0
  from the line, closes the argument.

(F4) is the qualitative change with respect to everything previous in the program: the
earlier targets (density anchored in D104, uniform index bound in D108, semilocal
positivity in D99/100) demanded uniform or extensive statements. Here the goal is a
single event. The document's question is whether any unconditional machinery produces
that event. We state the answer in advance to frame the reading: **no — and the reason
is that the event, although unique, lives in a density-zero set whose non-emptiness is
exactly the type of statement the master quantifier blocks; but the way it fails leaves
a new residue (the reduction to LP-112 and the inapplicability of D104's self-blocking).**

---

## 2. Line (1): almost-periodicity + finiteness

### 2.1. Unconditional exact inventory of the almost-periodicity of ζ

**(a) Half-plane σ > 1: uniform Bohr almost-periodicity.** In every half-plane
σ ≥ 1+ε the Dirichlet series converges absolutely; ζ is a uniform limit of the
trigonometric polynomials Σ_{n≤N} n^{−σ}e^{−it log n} and is therefore **uniformly
almost-periodic in Bohr's sense** [Boh: H. Bohr, *Zur Theorie der allgemeinen
Dirichletschen Reihen*, Math. Ann. 79 (1918); exposition in Besicovitch, *Almost
Periodic Functions*, Cambridge 1932]. There the replica argument is vacuous: ζ has no
zeros in σ > 1 (Euler product). Note the structural irony: where almost-periodicity is
uniform, Euler has already killed the zeros; where there could be zeros, the available
almost-periodicity degrades to mean square.

**(b) Strip ½ < σ < 1: there is NO uniform almost-periodicity, for a trivial reason.** A
uniformly almost-periodic function on a vertical line is bounded on it (Bohr). But
lim sup_{t→∞} |ζ(σ+it)| = ∞ for every σ ≤ 1 (classical Ω-theorems; [Tit86, Ch. VIII]).
Hence ζ is **not** Bohr-almost-periodic on any line in the strip, unconditionally. The
uniform route is closed from the start — not by the wall, but by growth.

**(c) Strip ½ < σ < 1: Besicovitch B² almost-periodicity — unconditional THEOREM.**
This is the exact available statement:

**Lemma 2.1 (ζ is B²-almost-periodic on each line of the strip).** Let σ ∈ (½, 1) be
fixed and $P_X(t) := \sum_{n\le X} n^{-\sigma - it}$. Then
$$\limsup_{T\to\infty} \frac1T \int_0^T \bigl|\zeta(\sigma+it) - P_X(t)\bigr|^2\,dt
\;\le\; C_\sigma \sum_{n > X} n^{-2\sigma} \;\xrightarrow[X\to\infty]{}\; 0.$$
In particular ζ(σ+i·) belongs to Besicovitch's class B² and is B²-almost-periodic
(B² limit of trigonometric polynomials with frequencies {log n}).

*Proof.* By the approximate formula ζ(s) = Σ_{n≤t} n^{−s} + O(t^{−σ}) for
σ ≥ σ₀ > 0, t ≥ 1 ([Tit86, Thm. 4.11] with x = t), the difference ζ(σ+it) − P_X(t) is,
for t > X, the Dirichlet polynomial Σ_{X<n≤t} n^{−σ−it} plus O(t^{−σ}). The
Montgomery–Vaughan mean value theorem ([MV74]; or the classical computation of
[Tit86, §7.2]) gives
$$\frac1T\int_X^T \Bigl|\sum_{X<n\le t} n^{-\sigma-it}\Bigr|^2 dt
\;\ll\; \sum_{X<n\le T} n^{-2\sigma}\Bigl(1 + \frac nT\Bigr)
\;\ll\; \sum_{n>X} n^{-2\sigma} + \frac{T^{1-2\sigma}\cdot T}{T},$$
and since σ > ½ the second term is T^{1−2σ} = o(1). The term O(t^{−σ}) contributes
o(1) to the average. This is the content of the classical mean-square theorem
∫₀^T|ζ(σ+it)|²dt ∼ ζ(2σ)T ([Tit86, Thm. 7.2]), refined to the mean approximation via
partial sums — all unconditional. Membership in B² and B²-almost-periodicity follow
from the definition of the Besicovitch class as the B²-closure of trigonometric
polynomials [Besicovitch 1932, Ch. II]. ∎

**Lemma 2.2 (the B² almost-periods are relatively dense, with positive lower density).**
For every ε > 0, the set
$$E_\varepsilon := \Bigl\{\tau \in \mathbb{R} :
\limsup_{T\to\infty}\frac1T\int_0^T |\zeta(\sigma+it+i\tau) - \zeta(\sigma+it)|^2\,dt
< \varepsilon^2\Bigr\}$$
is relatively dense in ℝ and has positive lower density.

*Proof.* Choose X = X(ε) with C_σ Σ_{n>X} n^{−2σ} < ε²/9 (Lemma 2.1). The set
$$K_\eta := \{\tau : \|\tau \log p / 2\pi\| < \eta \ \ \forall p \le X\}$$
(‖·‖ = distance to the nearest integer) satisfies, for η = η(ε, X) sufficiently small:
|n^{-i\tau} − 1| < ε/(3‖P_X‖_{B^2} + 3) for every n ≤ X — because
log n = Σ_p a_p log p with Σ a_p ≤ log₂ X for n ≤ X, so that
‖τ log n/2π‖ ≤ (log₂X)·η. For τ ∈ K_η, ‖P_X(·+τ) − P_X‖_∞ < ε/3, and by the triangle
inequality in the B² seminorm (which is invariant under fixed translations, since the
limit of the average over [0,T] does not change when the window is shifted by a fixed
amount): ‖ζ(·+iτ) − ζ‖_{B²} ≤ ε/3 + ε/3 + ε/3. It remains to see that K_η is relatively
dense with positive density: the numbers {log p : p ≤ X} are linearly independent over
ℚ (unique factorization: a relation Σ a_p log p = 0 with a_p ∈ ℤ gives Π p^{a_p} = 1,
impossible unless a_p ≡ 0). By the Kronecker–Weyl theorem, the linear flow
τ ↦ (τ log p/2π)_{p≤X} mod 1 is equidistributed and minimal on the torus T^{π(X)} (it is
a group translation with dense orbit); by minimality, every orbit segment of length
≥ L₀(η) visits the basic neighborhood, and by equidistribution the density of K_η is
(2η)^{π(X)} > 0. ∎

Up to here everything is theorem. The arithmetic input of Lemma 2.2 is the linear
independence of {log p}: **unique factorization — the additive skeleton of the Euler
product — already enters at the B² level, unconditionally** (noted for §3).

### 2.2. The Bohr–Rouché argument frozen by H(m): the conditional is theorem

We first isolate the pointwise lemma that the whole line needs; then we prove that,
given it, H(m) falls.

**Lemma LP-112 (sequential pointwise almost-periodicity; OPEN).** *For every closed
disk D ⊂ {½ < σ < 1} there exists a sequence τ_k → ∞ such that*
$$\sup_{s \in D} |\zeta(s + i\tau_k) - \zeta(s)| \;\longrightarrow\; 0.$$

(Weak version sufficient, LP-112⁻: for every D and every ε > 0 there exists ONE
τ > height(D) with sup_D |ζ(s+iτ) − ζ(s)| < ε.)

**Theorem 2.3 (the conditional implication, with complete proof).** If LP-112⁻ holds
(in particular if LP-112 holds), then ζ cannot have a finite nonzero number of
off-critical quadruples: H(m) is contradictory for every 0 < m < ∞. Equivalently,
LP-112 ⟹ D-109 (m ∈ {0, ∞}), and therefore LP-112 ∧ (m<∞) ⟹ RH.

*Proof.* Assume H(m). Let ρ₀ = β + iγ₀ be an off-critical zero, β = ½ + δ with
δ := δ_{j_0} > 0, γ₀ ≤ γ_max. The zeros of ζ are isolated; choose
$$r := \tfrac12\min\bigl(\delta,\ 1-\beta,\ \mathrm{dist}(\rho_0,\, Z(\zeta)\setminus\{\rho_0\})\bigr) > 0,$$
so that the closed disk D := D̄(ρ₀, r) is contained in the open strip
{½ + δ/2 < σ < 1} and ζ does not vanish on D ∖ {ρ₀}; in particular
$$\eta := \min_{|s-\rho_0| = r} |\zeta(s)| > 0.$$
**All these are fixed constants of the H(m) world** — this is the use of (F1): without
H(m), δ and η would be parameters requiring uniformity; with H(m) they are numbers.

Apply LP-112⁻ to the disk D with ε := η/2 and with τ > γ_max + γ₀ + r + 1: there exists
τ with
$$\sup_{s \in D} |\zeta(s+i\tau) - \zeta(s)| < \eta/2 < \eta = \min_{\partial D}|\zeta|.$$
By Rouché's theorem applied on the contour ∂D to the pair (ζ(s), ζ(s+iτ) − ζ(s)):
ζ(·+iτ) has inside D the same number of zeros as ζ, i.e. at least one (the multiplicity
of ρ₀). Hence ζ has a zero ρ′ with |ρ′ − (ρ₀ + iτ)| < r. Then:
- Re ρ′ ∈ (β − r, β + r) ⊆ (½ + δ/2, 1): the zero ρ′ is **off-critical** (here we use
  r < δ/2 ≤ δ_min/2 in the worst case — the quantification required by the goal: the
  Rouché radius must be less than the distance of the zero to the line, and under H(m)
  that is a fixed admissible choice, not a degenerating limit);
- Im ρ′ > γ₀ + τ − r > γ_max: the zero ρ′ **is not any of the 4m zeros on the list**
  (F2): it is a new off-critical zero.
Its quadruple {ρ′, ρ̄′, 1−ρ′, 1−ρ̄′} is an (m+1)-th quadruple: contradicting
H(m). With the full LP-112, the sequence τ_k → ∞ produces (taking τ_k with separations
> 2r) infinitely many distinct off-critical zeros, i.e. m = ∞ directly: this gives
D-109 in the form m ≥ 1 ⟹ m = ∞. The last statement is the identity of Doc 109
§4.5. ∎

**Observation (what Theorem 2.3 actually proved).** The target implication
m<∞ ⟹ m=0 is, as the goal anticipated, **exactly** the statement that the
Bohr–Rouché argument proves once one has the local pointwise almost-periodicity.
Moreover: H(m) makes the conditional **clean** — no uniformities, no exploding
constants, no need for density. The entire weight of the problem has been compressed
into LP-112. The following two subsections measure that lemma with all the tools
requested, and the result is negative in an informative form.

### 2.3. The B² → pointwise step: three attempts, three exact failures

**(a) The Besicovitch seminorm annihilates compacts.**

**Observation 2.4.** For every fixed compact window K = [γ₀ − A, γ₀ + A] and every
locally L² function f,
$$\|f \cdot \mathbf{1}_K\|_{B^2}^2 = \limsup_{T\to\infty}\frac1T\int_0^T |f|^2\mathbf{1}_K\,dt
= \limsup_{T\to\infty}\frac1T\int_K |f|^2\,dt = 0.$$
Hence the condition τ ∈ E_ε (Lemma 2.2) **carries no information** about
∫_K |ζ(σ+it+iτ) − ζ(σ+it)|²dt: a function may have arbitrarily small B² seminorm and
be arbitrarily large on K. The off-critical zero lives at the fixed height
γ₀ ≤ γ_max — a compact. **B² almost-periodicity is blind, by the very definition of the
seminorm, exactly where the signal is.** This is the most stripped-down form of the gap
in Doc 109 §4.4: it is not that the B² control is "too weak" quantitatively in the
window — it is identically zero on it.

**(b) Subharmonicity: the localizer works, the feeder does not exist.**

The tool suggested in the goal is correct only halfway, and it is worth saying
precisely which half. For holomorphic g, |g|² is subharmonic, and for every z ∈ D(ρ₀, r):
$$|g(z)|^2 \;\le\; \frac{1}{\pi r^2}\iint_{D(z,r)} |g|^2\,dA
\;\le\; \frac{1}{\pi r^2}\iint_{D(\rho_0, 2r)} |g|^2\,dA,$$
so that
$$\sup_{D(\rho_0,r)} |\zeta(\cdot+i\tau)-\zeta|^2 \;\le\; \frac{1}{\pi r^2}
\iint_{D(\rho_0,2r)} |\zeta(s+i\tau)-\zeta(s)|^2\,dA(s). \tag{2.1}$$
The mean-local-L² → sup step is, therefore, FREE: **if** some τ makes the area integral
over the fixed disk D(ρ₀, 2r) small, Rouché activates. The problem is feeding (2.1).
The two available sources fail as follows:

**Lemma 2.5 (the full average in τ is not small: closed-form computation).** For
s₀ = σ+it₀ fixed with ½ < σ < 1,
$$\lim_{T\to\infty} \frac1T \int_0^T |\zeta(s_0 + i\tau) - \zeta(s_0)|^2\,d\tau
\;=\; \zeta(2\sigma) - 1 + |\zeta(s_0) - 1|^2 \;\ge\; \zeta(2\sigma) - 1 \;>\; 0.$$

*Proof.* Expanding the square, two classical and unconditional mean values suffice.
(i) (1/T)∫₀^T |ζ(s₀+iτ)|²dτ → ζ(2σ) ([Tit86, Thm. 7.2]; the fixed shift t₀ does not
alter the limit). (ii) (1/T)∫₀^T ζ(s₀+iτ)dτ → 1: by Cauchy–Schwarz and Lemma 2.1,
|mean(ζ − P_X)| ≤ ‖ζ−P_X‖_{B²} → 0 as X → ∞, while the mean of P_X(s₀+iτ) in τ is
1 + Σ_{2≤n≤X} n^{−σ−it₀}·mean(n^{−iτ}) → 1 (each n^{−iτ}, n ≥ 2, has mean 0). Then the
limit of the average is
ζ(2σ) − 2Re(\overline{ζ(s₀)}·1) + |ζ(s₀)|² = ζ(2σ) − 1 + |ζ(s₀)−1|². ∎

Integrating Lemma 2.5 in s₀ over D(ρ₀, 2r) (dominated convergence over the compact,
with standard polynomial bounds of ζ in the strip), the average in τ of the right-hand
side of (2.1) tends to a limit that is **strictly positive and bounded below**.
Conclusion: the full average in τ produces no good sequence — and neither does it
forbid one (an average bounded below is compatible with a positive-density set of τ
where the integrand is tiny). Subharmonicity reduces LP-112 to "making a local area
integral small for some τ", but neither the total average (Lemma 2.5: it is not small)
nor the average restricted to E_ε (Obs. 2.4: it cannot see the window) controls it.
The localizer exists; the feeder does not.

**(c) Normality/Montel: compactness without selection.** The family {ζ(·+iτ)}_τ
restricted to a bounded neighborhood of D is locally bounded in mean (Lemma 2.5 + (2.1)
give local-uniform bounds along subsequences of τ with bounded area integral — which
exist by Lemma 2.5 itself and Chebyshev) and hence normal along subsequences: there are
τ_k → ∞ and holomorphic g with ζ(·+iτ_k) → g uniformly on D. Montel **guarantees
limits, not which ones**: the set of possible limits is (by Bagchi's limit theorem,
§2.4) the support of the Bagchi measure, and the question of whether ζ|_D is among them
is exactly LP-112. Normality restates the problem; it does not solve it.

### 2.4. The zero-density proposition: the distributional direction, proved against it

The above shows that the averaging tools do not feed Rouché. The following shows
something stronger and more interesting: under the hypothesis H(m) we want to refute,
**the set of τ that would feed Rouché has density zero** — the distributional machinery
is not neutral: it certifies that the witnesses of LP-112 are exceptional.

**Proposition 2.6 (zero upper density of the good τ).** Assume H(m) with m ≥ 1 and let
ρ₀, r, η be as in the proof of Theorem 2.3. For every ε < η, the set
$$A_\varepsilon := \Bigl\{\tau > 0 : \sup_{|s-\rho_0|\le r} |\zeta(s+i\tau) - \zeta(s)| \le \varepsilon\Bigr\}$$
has upper density zero:
$\limsup_{T\to\infty} T^{-1}\,\mathrm{meas}(A_\varepsilon \cap [0,T]) = 0$.

*Proof.* Let D′ be an open disk with D̄(ρ₀,r) ⊂ D′ ⊂ D̄′ ⊂ {½<σ<1}. Bagchi's
unconditional functional limit theorem ([Bag81], full exposition in [Lau96,
Ch. 5]): the measures Q_T(·) := T^{-1}\,\mathrm{meas}\{τ ∈ [0,T] : ζ(·+iτ)|_{D′} ∈ ·\}
converge weakly, in the space H(D′) of holomorphic functions with the compact-open
topology, to the law Q of the random element ζ(s,ω) = Π_p (1 − ω_p p^{−s})^{−1}
(random Euler product, ω = (ω_p) uniform on the torus Π_p S¹; the product converges in
H(D′) almost surely). The support of Q is
$$S \;=\; \{f \in H(D') : f(s) \ne 0 \ \forall s \in D'\} \cup \{0\}$$
([Bag81]; [Lau96, Ch. 6]; this is the standard ingredient of universality theorems:
limits of nonzero Euler products are either nonzero or identically zero, Hurwitz).

Consider the set C_ε := {f ∈ H(D′) : sup_{D̄(ρ₀,r)} |f − ζ| ≤ ε}, closed in H(D′). We
claim C_ε ∩ S = ∅ for ε < η. Indeed, if f ∈ C_ε: on the circle |s−ρ₀| = r we have
|f − ζ| ≤ ε < η = min |ζ|, and Rouché gives f a zero in D(ρ₀, r), so f ∉ S unless
f ≡ 0; but f ≡ 0 would give sup_{D̄}|ζ| ≤ ε < η ≤ sup_{∂D}|ζ|, absurd. Then
Q(C_ε) = 0 (a closed set disjoint from the support has null measure) and, by the
Portmanteau theorem for closed sets,
$$\limsup_T \frac{\mathrm{meas}(A_\varepsilon\cap[0,T])}{T} \;\le\; \limsup_T Q_T(C_\varepsilon) \;\le\; Q(C_\varepsilon) \;=\; 0. \qquad\blacksquare$$

**Reading.** Proposition 2.6 is the easy half of Bagchi (an off-critical zero destroys
strong recurrence; Doc 102, Doc 109 §4.3) sharpened to its quantitative form: not just
"the density is not positive" — it is zero. Its consequences for this document:

1. **The hope of positive measure was false.** The goal asked: "if good almost-periods
   exist (positive measure) and each produces a replica, done — where exactly can this
   fail?" It fails here: the B² almost-periods have positive density (Lemma 2.2), but
   the τ useful for Rouché in the specific disk have density zero (Prop. 2.6). There is
   no contradiction between the two statements because B² goodness is an average in t
   that weighs 0 on the window of the zero (Obs. 2.4). **The positivity of measure lives
   in the wrong coordinate.**
2. **The wall has sign.** It is not merely that we do not know how to prove LP-112: we
   know that its witnesses, if they exist, form a set that the entire distributional
   machinery (Bagchi equidistribution, moments, B²) classifies as exceptional.
   Producing an element of a density-zero set defined by an individual condition is
   P43's Principle 3.1 — "the object lives in the exceptional set of its own generic
   behavior" — in almost-period coordinates.
3. **Revealing symmetry.** Under RH, the analogous set A_ε has POSITIVE lower density
   for every disk (strong recurrence, the hard half of Bagchi [Bag87], which uses that
   ζ|_D is nonzero and lies in the support S of the limit law). The density of A_ε is,
   therefore, a perfect detector of the two worlds: positive under RH, zero under ¬RH.
   As a detector it is useless (evaluating the density requires what we want to prove),
   but it explains why strong recurrence is RH-equivalent and the sequential version is
   not: the boundary between "positive density" and "density zero but non-empty" is
   exactly the boundary between RH and D-109.

### 2.5. Does D104's self-blocking apply? No — and the difference is structural

**Proposition 2.7 (the sequential version does not self-block).** The conclusion of
Theorem 2.3 under LP-112 (a family of off-critical zeros at heights γ₀ + τ_k,
k ∈ ℕ) is consistent with all known zero-density theorems, for any sequence τ_k → ∞,
even one with arbitrarily slow counting.

*Proof.* The zeros produced up to height T are at most
#{k : τ_k ≤ T} + 4m = o(T^θ) for any θ > 0 if τ_k grows fast enough, and in any case
O(#{k: τ_k ≤ T}), which is not bounded below by any increasing function: the
conclusion imposes no density. The density theorems
(N(σ,T) ≪ T^{κ(σ)}, D111 §2.3) bound from above; a countable sparse family satisfies
them trivially. ∎

Exact contrast with D104 (via P43, Thm. C): the Form C amplifier needed to convert a
zero into a family of **anchored positive density**, and that density was capped by the
unconditional ceiling N(σ,T) = O(T^{κ(σ)}) **with the same exponent**: the improvement
feeding the amplifier also fed the ceiling — self-blocking. The decisive question of
the goal ("does D104's blockage apply when only ONE replica is needed?") has a clean
answer: **it does not apply**. The requirement dropped from positive density to zero
density, and against zero density there is no ceiling. The price: there is also no
production machinery — the methods that manufacture τ's (equidistribution, averages)
manufacture generic ones, and the generic one is bad (Prop. 2.6). The blockage changed
nature: from *internal self-contradiction* (D104) to *absence of a feeder* (here). That
difference is what keeps LP-112 alive as a target (§5.4).

### 2.6. Final quantification of the Rouché step under H(m)

Explicit record of the quantification requested, because it shows exactly what
finiteness bought. Without H(m) (i.e. attacking m = 0 directly via recurrence), the
radius r and the margin η degenerate as δ → 0 and γ₀ → ∞, and any control must be
uniform in the configuration — Bagchi's situation, RH-equivalent. Under H(m):

- r < δ/2 guarantees an off-critical replica; r is a fixed constant (F1). **There is no
  blowup of constants:** the pair (ε, r) = (η/2, r(ρ₀)) is a fixed datum of the
  hypothetical world.
- The height threshold τ > γ_max + γ₀ + r + 1 guarantees novelty of the replica (F2).
- A SINGLE replica suffices (F4); infinitely many give m = ∞ directly.

The remaining gap is exactly one: **the existence of a single τ in the set A_ε of
Prop. 2.6.** Nothing else is missing. OPEN GAP (= LP-112⁻ for the disk D(ρ₀,r)).

---

## 3. Line (2): the role of the Euler product — the separation of the counterexamples

Doc 111's Prop. 2.2 forces: the cosh-examples F = P₁⋯P_m·cosh(a(s−½)) have m
quadruples, a functional equation, order 1 — and finite m is REALIZED in that class.
Any proof (even conditional) of m<∞ ⟹ m=0 must use something they lack. We verify that
line (1) does so, locating the input with lemma-level precision.

### 3.1. The cosh-examples already fall outside at the B² level

**Lemma 3.1 (the cosh-examples are not B² on vertical lines).** Let
F = P·F₀ with P = P₁⋯P_m (polynomial of degree 4m, m ≥ 1) and F₀(s) = cosh(a(s−½)).
For every fixed σ ∈ (0,1),
$$\frac1{2T}\int_{-T}^{T} |F(\sigma+it)|^2\,dt \;\asymp\; T^{8m} \;\longrightarrow\; \infty.$$
In particular F(σ+i·) ∉ B² and F is not B²-almost-periodic on any vertical line.

*Proof.* |P(σ+it)| ≍ |t|^{4m} as |t| → ∞ (dominant term of the polynomial), and
|F₀(σ+it)|² = sinh²(a(σ−½)) + cos²(at) ∈ [sinh²(a(σ−½)), cosh²(a(σ−½))], bounded
between positive constants for σ ≠ ½ (and between 0 and 1 for σ = ½, with mean ½ of
the cos²). Then the integrand is ≍ t^{8m} and the average ≍ T^{8m}/(8m+1). ∎

**Lemma 3.2 (the cosh-examples admit no sequential self-approximation).** With F as
above and D = D̄(ρ₀, r) a disk around an off-critical zero ρ₀ of F with
D ∩ {σ = ½} = ∅: there is no sequence τ_k → ∞ with
sup_D |F(s+iτ_k) − F(s)| → 0. That is, the analogue of LP-112 for F is **false**.

*Proof.* For s ∈ D: |F(s+iτ)| ≥ |P(s+iτ)|·sinh(a·min_D|σ−½|) ≥ c_D·τ^{4m} → ∞
(P has degree 4m ≥ 4 and |s + iτ| ≥ τ − |ρ₀| − r), while sup_D |F| < ∞. The
difference cannot tend to 0. ∎

This dissolves the circularity risk flagged by D111: the route of Theorem 2.3 is not a
"physical" argument (symmetry + growth) — its input, self-approximation, is false in
class ℰ with m ≥ 1. Perfect consistency: Theorem 2.3 says
"self-approximation ⟹ m ∈ {0,∞}", the cosh-examples have finite nonzero m, and
indeed do not self-approximate.

### 3.2. Single frequency vs. the Kronecker torus: non-discreteness as a lemma

The structure of the cosh-examples without the polynomial factor illuminates the
mechanism. F₀ is **exactly periodic** in t with period 2π/a: its period group is
discrete, and translation by one period maps the zero set onto itself — the
"replica" of the zero lands on a zero that was already there. A discrete-group
almost-periodicity multiplies nothing. The question posed by the goal: what exact
property of the set of almost-periods separates ζ, and is it unconditional?

**Lemma 3.3 (arithmetic non-discreteness of ζ's almost-periods).** (a) ζ is not
periodic in t on any sub-band of σ > ½: if ζ(s+iτ₀) = ζ(s) on an open set,
then (analytic continuation to the half-plane σ > 1 and uniqueness of Dirichlet-series
coefficients) n^{−iτ₀} = 1 for every n ≥ 2, i.e. τ₀ log n ∈ 2πℤ for every n;
with n = 2, 3 this forces log 2/log 3 ∈ ℚ, i.e. 2^q = 3^p with p, q ∈ ℤ not both
zero — impossible by unique factorization. Hence τ₀ = 0.
(b) For every ε > 0, the set E_ε of B² almost-periods (Lemma 2.2) is relatively
dense and **is not contained in any discrete subgroup of ℝ**: it contains the
Kronecker set K_η, and K_η ⊂ cℤ is impossible because K_η has density
(2η)^{π(X)} which, by equidistribution, is realized in intervals of every position,
while the density of any subset of cℤ is supported on an arithmetic progression —
it suffices to take η with (2η)^{π(X)} greater than 0 and observe that K_η is open
(a union of intervals of positive length: if τ ∈ K_η, a neighborhood of τ lies in
K_{η'} for η' close by), and a nonempty open set does not fit in a discrete set.

*Proof.* Contained in the statement; the only nontrivial input is the
irrationality of log 2/log 3 (unique factorization) and Weyl equidistribution already
used in Lemma 2.2. ∎

**Synthesis of the separation (exact answer to question (2) of the goal).** The
property that separates ζ from the counterexamples, at each level:

| level | ζ | cosh-examples (m ≥ 1) | ζ's input |
|---|---|---|---|
| B²-almost-periodicity in the strip | **theorem** (Lemma 2.1) | false (Lemma 3.1) | Dirichlet series with Σ\|a_n\|²n^{−2σ} < ∞ |
| relatively dense, non-discrete almost-periods | **theorem** (Lemmas 2.2, 3.3) | discrete period group (F₀ only); none (F) | ℚ-linear independence of {log p} = unique factorization — unconditional, pure arithmetic |
| replicas at NEW heights | automatic under H(m) (heights γ₀+τ_k → ∞, finite off-list) | the periodic translation fixes the zero set | — |
| support of the limit theorem (Bagchi) | random Euler product: S = {nonzero} ∪ {0} | no analogue | **full Euler product**, with independent coordinates ω_p |
| pointwise transfer (LP-112) | **OPEN GAP** | false (Lemma 3.2) | — |

The Euler product enters, then, at three places of increasing strength: as a
Dirichlet series (B² level), as independence of {log p} (Kronecker level: relative
density and non-discreteness of the almost-periods — the goal's infinite-dimensional
torus), and as a random product of independent coordinates (Bagchi level: the structure
of the support, used both in Prop. 2.6 and in the direction RH ⟹ strong recurrence).
The first two are unconditional and already serve the argument; the third governs the
boundary between positive and zero density.

### 3.3. Calibration with Davenport–Heilbronn: what Euler decides and what it does not

Sanity check. The Davenport–Heilbronn function (Dirichlet series, Riemann-type
functional equation, WITHOUT an Euler product; D111 Obs. 2.4) is B²-almost-periodic in
the strip by the same Lemma 2.1 (it only uses the series and the mean square value,
valid for linear combinations of L-functions), and has **infinitely many** off-critical
zeros [DH36]. That is: in the class "Dirichlet series + functional equation", the
pattern m ∈ {0,∞} is consistent to this day — the Euler-free exemplar realized the
alternative m = ∞, not finite m. This suggests (does not prove) that the D-109
dichotomy might hold on the full intermediate class, with the series almost-periodicity
as the sole engine; the full Euler product would then be responsible not for the
dichotomy but for the **alternative** m = 0 (Weil positivity / Bagchi's support).
Declared GAP (D111 Obs. 2.4): no exemplar of the intermediate class with finite nonzero
m is known, nor a proof of its impossibility. For this document the calibration
suffices: the route of Theorem 2.3 uses inputs that class ℰ lacks (Lemmas 3.1–3.2),
fulfilling D111's Cor. 2.3 requirement.

---

## 4. Line (3): Newton traces and the finite moment system

### 4.1. Finite rank is not a priori finite rank

Doc 110's Prop. 4.5: at **a priori known** finite rank n, the n traces
t_j = tr(Q^j) determine the inertia (Newton + Jacobi–Frobenius, [Gan59, Vol. 2,
Ch. X]). Under H(m), the form Q restricted to 𝒦_off has rank 4m — finite. But Doc
110's axiom L6 requires the dimension to be bounded **by arithmetic data, not by
zeros**: here the dimension is 4m with m the problem's unknown. The distinction is not
pedantry: the Newton–Frobenius procedure needs to know how many traces to compute and
against which Hankel to test; with n unknown, the accessible datum is an infinite
sequence of purported traces whose stabilization at rank ≤ 4m is indistinguishable,
at any finite stage, from a larger rank with small eigenvalues. This is Doc 111's
Obs. 6.3 (the receptacle measures, it does not bound) in moment form. Nonetheless,
there is a nuance in our favor that the goal rightly flags: to REFUTE H(m) we do not
need to read m — we need only derive an inconsistency. Let us see if the system
allows it.

### 4.2. The moment system under H(m): the spectral side is transparent

Spectral side (of zeros): under H(m), the cost of each quadruple in the CCM trace is
2δ_j²K_λ(γ_j)(1+o(1)) (Doc 98, Cor. 2.4, cited and used in D111 §6.2(a)), with
K_λ(γ) > 0 explicit and decaying as the density dm_∞ ≍ |γ|^{−1/2}e^{−π|γ|/2}
(Doc 95, Lemma 2.2, via D111). Hence
$$T_\lambda \;=\; \sum_{j=1}^{m} 2\delta_j^2\,K_\lambda(\gamma_j)\,(1+o(1))
\;>\; 0 \qquad \text{for every } \lambda \text{ in the effective range},\tag{4.1}$$
a **finite sum** of explicit functions of the 4m parameters — exactly the
"moments of a finite atomic measure" structure the goal asked for.

**Lemma 4.1 (finite determination; classical algebra).** A positive atomic measure
μ = Σ_{j≤k} c_j δ_{x_j} (c_j > 0, x_j distinct, k known) is determined by its
2k power moments s_i = Σ c_j x_j^i, i = 0,…,2k−1: the rank of the Hankel matrix
(s_{i+i'}) detects k, the nodal polynomial is recovered by the Prony/Newton
system, and the weights by Vandermonde. [Gan59, Vol. 2, Ch. X]; classical theory of
finite Hamburger moments [Akh65]. The finite moment problem is **determined**:
there is no Hamburger-type indeterminacy at finite rank. ∎

So, on the idealized plane: if an oracle delivered the exact values of a suitable
family {T_{λ_i}} (or of T_λ and its derivatives in λ — the family of kernels K_λ
playing the role of powers; the effective separation of parameters by the family
{K_λ(·)} is plausible but we do NOT assert it: it is not load-bearing, because the
route dies before that), the parameters {(δ_j, γ_j)} would be determined, and "empty
list" would be detectable: T_λ ≡ 0. This is fine and is the correct translation of
Doc 110's Prop. 4.5 into the problem. Everything then rests on: is there any autonomous
value to feed the system?

### 4.3. D72's structure, verified at source, and the two real walls

Direct verification against Doc 72 (done for this document):

- **Thm. 4.1 (D72):** T_λ = A_λ^{off} − Σ_p (log p/√p)·B_λ(log p) + O(p^{−1}-tails),
  where A_λ^{off} is the off-critical zero contribution (zero under RH) and
  $$B_\lambda(\log p) \;=\; \int W_\lambda(s)\cos(s\log p)\,dm_\infty(s).$$
- **Verification finding (the goal's fear was unfounded):** B_λ(log p) is the Fourier
  transform of the test W_λ·w at the frequency log p — a **fully autonomous**
  object (it depends on the CCM kernel and on dm_∞, not on the zeros). Doc 72
  constructs it as Σ_{n≤N(λ)} n∫|P_n|²cos(s log p)dm_∞ — CCM Jacobi polynomials,
  operator data, without zero positions. The suspicion "B_λ depends on ALL the
  zeros via the explicit formula" is false: what depends on the zeros is the OTHER
  side of the identity.
- **The first real wall (Doc 105, via Doc 109 §6.1):** the prime series
  Σ_p (log p/√p)B_λ(log p) **diverges**, as (5√2/8)·log X over primes p ≤ X: the
  CCM test W_λ·w sits at the boundary of the Weil class and D72's formula is
  strictly formal. **There exists today no "arithmetic value of T_λ" that the
  moment system needs as feed** — not even regularized without passing through
  the zeros. The system of §4.2 is well-posed and without data.

- **The second wall, independent of the first (structural):**

**Proposition 4.2 (the explicit formula does not overdetermine: identity tautology).**
Assume H(m) and grant, against Doc 105, a convergent regularization of D72's formula
(or use any test h from the legitimate Weil class, where the explicit formula is a
theorem). Then the system of equations obtainable by evaluating the explicit formula
over any family {h_i} of tests is **consistent by construction** with the true
configuration of parameters, and cannot derive a contradiction from H(m) without a
sign input. Precisely: for each test h, Weil's identity says
$$\underbrace{\widehat h(\tfrac i2) + \widehat h(-\tfrac i2)
- \sum_{n} \frac{\Lambda(n)}{\sqrt n}\,(h(\log n) + h(-\log n)) + \mathcal{A}_\infty(h)}_{\text{autonomous}}
\;=\; \sum_{\rho} \widehat h\Bigl(\frac{\rho - 1/2}{i}\Bigr)
= F_{\mathrm{on}}(h) + F_{\mathrm{off}}(h;\,\{\delta_j,\gamma_j\}),$$
and the only way to eliminate the non-autonomous term F_on (the on-line zeros, which
H(m) does not fix) is to subtract the identity from itself — any linear combination of
instances of the explicit formula is another instance: there is **a single**
independent arithmetic identity, and the true configuration satisfies it identically.
A system of identically satisfied identities does not constrain the parameters; it
constrains only if sign information is added (h in a cone with Σ_ρ ĥ ≥ 0 forced or
obstructed), and "the arithmetic side is ≥ 0 for every h in the Weil cone" is Weil's
criterion — equivalent to RH (and its verification is the inertia problem: P43 §4,
Doc 108).

*Proof (structural, with its declared status).* (i) The explicit formula for ζ is an
identity between linear functionals of the test, valid in every world (RH or ¬RH):
evaluating both sides produces no conditions on the world but on the test. (ii) The
attempt "global minus on-line prediction": define ξ_on := ξ/P_m with
P_m(s) = Π_j((s−½)² − (δ_j+iγ_j)²)((s−½)² − (δ_j−iγ_j)²) (the polynomial of D111
Prop. 2.2); ξ_on is entire of order 1 with all its zeros on-line, and
Σ_{ρ on} ĥ = Σ_{ρ} ĥ − F_off(h; params). Substituting this into any equation
involving "the on-line prediction", it is expressed as (autonomous Weil side) minus
F_off: forming "global value − on-line prediction" the autonomous side appears in
both terms with the same coefficient and cancels, leaving F_off = F_off — the
tautology announced. ξ_on has NO Dirichlet series or Euler product of its own
(dividing by a polynomial in s destroys the multiplicative structure), so there is no
second independent explicit formula to break the circularity.
(iii) That the remaining non-tautological content is exactly that of sign: this is the
content of Weil's criterion [Wei52] and of the chain Doc 108 → P43 §4 (detecting
F_off ≠ 0 via inequalities is reading the inertia, not the value). As in D111
Prop. 6.2(c), this is asserted with proof over the catalogued manipulations (linear
combinations of instances of the explicit formula and algebraic eliminations of
F_on), not as a classification of "every conceivable manipulation": declared GAP at
that generality. ∎

**Observation 4.3 (the required precision, and where the quantifier hides).** Even
ignoring Prop. 4.2 — suppose a regularization R of the prime side were computable and
that "R = 0 vs R = T_λ > 0" were the test. Under H(m) the gap is
ε₀ = Σ_j 2δ_j²K_λ(γ_j) > 0 — **a fixed positive constant of the hypothetical world**,
not a vanishing precision: this seems to dodge the second-order wall o(1/log T) of
Doc 108. But the contradiction must be derived for EVERY admissible finite
configuration (H(m) existentially quantifies over configurations), and
$$\inf_{\substack{m \ge 1,\ \delta_j > 0,\ \gamma_j > 3\cdot10^{12}}} \;\sum_j 2\delta_j^2 K_\lambda(\gamma_j) \;=\; 0$$
(δ → 0, or γ → ∞ with K_λ(γ) ≍ γ^{−1/2}e^{−πγ/2}: the vanishing cost of D111
Prop. 6.2(a)). The moment argument would then need to evaluate R with error smaller
than an infimum equal to zero — i.e. exactly: uniformity over the hypothesis space
restores the quantifier that finiteness seemed to have frozen. The contrast with
line (1) is instructive: there H(m) freezes the constants BECAUSE the mechanism
(Rouché) is local to the hypothetical world and the contradiction is internal (m+1 > m);
here the mechanism (arithmetic evaluation) must work uniformly over worlds, because the
arithmetic value is a single one and the candidate configurations are all of them.
**Finiteness protects arguments internal to the world; it does not protect external
evaluators.**

### 4.4. Verdict on line (3)

**BLOCKED, at two independent and named places:** (i) the feed for the moment system
does not exist — D72's prime series diverges (Doc 105) and there is no autonomous value
of T_λ, not even formally regularized, without passing through the zeros; (ii) even with
feed, the available identities are tautological in the parameters (Prop. 4.2) and the
non-tautological content is the sign — P43's inertia; moreover (iii) the required
precision unfreezes upon quantifying over configurations (Obs. 4.3). The line's positive
finding: the finite-moment structure is correct (Lemma 4.1: determination, without
Hamburger pathology) and B_λ is autonomous — the problem is NOT the accessibility of
the test but that of the spectral value. Line (3) is Doc 110's Prop. 4.5 colliding with
the exact boundary Doc 110 itself drew: finite rank yes, a priori no.

---

## 5. Line (4): the best provable theorem today

### 5.1. Candidate (A): the full implication — NOT provable today; actively searching for the error

By discipline of the goal, we actively search for the error in the path that came
closest to closing: the whole of §2. The exact point where a naive proof self-fabricates
is the step from Lemma 2.2 to Theorem 2.3: "the almost-periods have positive density, so
some one of them serves the disk". Proposition 2.6 shows that this step is **false as a
measure-theoretic inference**: B²-goodness (positive density) and goodness-in-the-disk
(density zero) are nearly disjoint events, and the intersection is not guaranteed
nonempty by any measure argument — on the contrary, goodness-in-the-disk is exceptional.
The D104 precedent ("something fails in the B²→pointwise step") is confirmed and
sharpened: what fails is not an improvable estimate but the direction of the
distributional machinery. There is no proof of (A) today. Nor is there a refutation of
the implication: no counterexample is possible within the constructible classes (a
counterexample would be a world with ζ having finite nonzero m — that is constructive
¬RH).

### 5.2. Candidate (B): parameter-region versions — empty

Does there exist f such that H(m) ∧ (δ_min > f(γ_max)) is contradictory? Inventory: the
only region (δ, γ₀) excluded unconditionally is the classical
{γ₀ ≤ 3·10¹²} ∪ {δ > ½ − c(log γ₀)^{−2/3}(log log γ₀)^{−1/3}} (D111 §2.4), which
neither uses nor needs H(m). Does H(m) add regional leverage? The catalogued levers:
Siegel-repulsion (does not exist for quadruples: D111 §3, anti-Siegel), Turán
(circular: D111 §4), partial positivities (regimes disjoint from the visibility one:
D111 §2.4(a)). None improve with finite m — all fail for reasons independent of the
cardinal (growing budget, circularity of the upper bound, sub-resolution). §2 also gives
no region: Prop. 2.6 holds for every non-excluded (δ, γ₀). **Nothing to declare:
(B) coincides with the classical.**

### 5.3. Candidate (C): m = 1 — the minimal case avoids nothing

With m = 1 the constants of Theorem 2.3 are maximally concrete (a single quadruple,
r = δ/2 ∧ …) and the contradiction threshold is minimal (one replica). But Prop. 2.6
applies verbatim: its proof uses ONE off-critical zero in the disk — m = 1 is exactly
its case. The set A_ε remains density zero; the feeder still does not exist.
Uniformity was never the problem under H(m) (it was already frozen for every finite m,
§2.6); the problem is the existence of the exceptional τ, and that difficulty is
independent of m. **m = 1 is no easier than general finite m.** (Symmetric record:
it is not harder either — D111 §3's anti-repulsion says the quadruples do not
interact.)

### 5.4. Candidate (D): the clean reduction — THEOREM, and the non-equivalence analysis

**Theorem 5.1 (exact reduction of the dichotomy).** Unconditionally:
$$\text{LP-112} \;\Longrightarrow\; \bigl(m \in \{0, \infty\}\bigr) = \text{D-109},
\qquad\text{and therefore}\qquad
\bigl(m < \infty\bigr) \wedge \text{LP-112} \;\Longrightarrow\; \mathrm{RH}.$$
With the identity of Doc 109 §4.5: RH ⟺ (m<∞) ∧ D-109 ⟸ (target L8) ∧ LP-112.

*Proof.* Theorem 2.3. ∎

**Hierarchy of almost-periodicity and the exact position of LP-112.**

| statement | status | consequence for m |
|---|---|---|
| ζ uniformly Bohr-a.p. on a sub-band of the strip | **FALSE** (Ω-theorems, §2.1(b)) | (vacuous) |
| Bagchi's strong recurrence (positive lower density of good τ, every disk) | ⟺ RH [Bag87] | m = 0 |
| **LP-112** (unbounded sequence of good τ, every disk) | **OPEN** | m ∈ {0,∞} (Thm. 5.1) |
| B² almost-periodicity (positive density of almost-periods in mean) | **THEOREM** (Lemmas 2.1–2.2) | none (Obs. 2.4) |

LP-112 is the minimal sufficient rung: strictly weaker than strong recurrence (it
asks for a sequence where the latter asks for positive lower density) and strictly
stronger than B² (it asks for pointwise control over a compact, which B² does not
give).

**Non-equivalence analysis with RH (requested triple check):**

1. **RH ⟹ LP-112.** Under RH, ζ is strongly recurrent (hard half of Bagchi
   [Bag87]: ζ|_D does not vanish, it lies in the support S of the limit measure, and
   the lower density of A_ε is positive for every ε): positive density ⟹ unbounded
   set ⟹ LP-112. Hence LP-112 is no stronger than RH.
2. **LP-112 ⇏ RH by any known dictionary.** The consequence of LP-112 under ¬RH is
   m = ∞ (Thm. 5.1) — a world consistent with everything known (Bohr–Landau allows
   m = ∞ of density zero). The mechanism that makes strong recurrence RH-equivalent is
   exactly what LP-112 evades: positive density of replicas would contradict the
   density theorems N(σ,T) = O(T^θ) (cloning ≫ T vs. ceiling o(T): Doc 109 §4.3,
   item 3), so strong recurrence forces m = 0; a density-zero sequence contradicts
   nothing (Prop. 2.7) and only forces m ∉ (0,∞). Candid statement: this shows that
   LP-112 does not imply RH *via the density route*; an implication via an unknown
   route cannot be excluded — but the structural asymmetry (LP-112 is invariant under
   removing any positive-density subset from the good set; strong recurrence is not)
   makes the collapse implausible. Minor GAP declared.
3. **LP-112 vs. the sequential version of D109 §4.4.** They are the same statement;
   this document names it, fixes its exact form (with the weak version LP-112⁻ that
   suffices to refute each H(m) individually) and proves the reduction with all the
   constants. The difference with Bagchi is now measured precisely: Bagchi needs
   self-approximation with positive density (and hence its negation is detectable by
   averages and the equivalence with RH closes); LP-112 needs ONE good pointwise
   representative per height bound — a Σ-existential statement over a set that
   Prop. 2.6 declares density zero under ¬RH.

**The document's best theorem is, therefore, the pair (Theorem 5.1, Proposition 2.6):**
the complete reduction of half of RH's dichotomy to a non-RH-equivalent pointwise
sequential almost-periodicity lemma, together with the proof that the witnesses of that
lemma are exceptional in the exact sense of the master quantifier. Neither more (we do
not prove LP-112) nor less (none of the above had been written with these constants and
this perimeter).

---

## 6. Line (5): analysis of the blockage against P43

### 6.1. Is it the same inversion? Yes — and the asymmetry of the goal, resolved

The fine question of the goal: the B² average is over τ ∈ ℝ with positive density of
candidates; extracting ONE good τ from a positive-measure set is not a null-measure
event — is this route different from the wall? Answer, with the dissection done:

- **The premise of the asymmetry is false.** The positive-measure set (B² almost-periods,
  Lemma 2.2) is not the set from which one must extract. The relevant set — τ good for
  Rouché in the fixed disk D(ρ₀, r) — has upper density ZERO under H(m)
  (Prop. 2.6). The chain "positive density of candidates → one works" breaks because
  B² candidacy does not imply (nor positively correlate with, in the measure-theoretic
  sense) goodness in the fixed window: the B² seminorm assigns weight 0 to the window
  (Obs. 2.4). Of the two scenarios the goal asked to settle — "the good ones have
  positive measure" vs. "the useful set has null measure even though the B²
  almost-periods have positive density" — the second holds, and not as a suspicion but
  as a theorem.
- **Therefore: the same inversion.** Certifying A_ε ≠ ∅ with dens(A_ε) = 0 is
  certifying an individual event within the exceptional set of the statistic that
  governs it — P43's Principle 3.1, literally. The coordinate is new (almost-periods
  in τ, not zeros in γ nor windows in T), the wall is the same.
- **But a strictly weaker instance, and without D104's short-circuit.** Two
  differences proved relative to the earlier instances: (i) the statement to certify
  (LP-112) is NOT RH-equivalent (§5.4) — unlike strong recurrence; (ii) the route does
  not self-block (Prop. 2.7) — unlike D104's amplifier, whose target collided with its
  own ceiling. The comparative state:

| replica route | requires | under ¬RH that set is | blockage |
|---|---|---|---|
| strong recurrence (Bagchi) | positive lower density of good τ | density 0 (Prop. 2.6) | the target IS RH (equivalence) |
| D104 amplifier (Form C) | anchored positive density of replicas | capped by N(σ,T) = O(T^κ), same exponent | self-blocking |
| **LP-112 (sequential, this doc)** | ONE τ per height bound (density 0 suffices) | density 0, emptiness UNKNOWN | no self-blocking; no feeder — P43 wall in exceptional-set form |

The form of the wall here is the barest in the program: no estimate is missing
(the relevant estimates are present: Lemmas 2.1, 2.2, 2.5), there is no internal
collision (Prop. 2.7) — what is missing is a mechanism of **non-generic selection**:
something that produces a point of a density-zero set defined by an individual
condition. No method on P43's list (propagation, amplification, recurrence,
positivity, sieve, moments) produces exceptional points; all produce generic ones.

### 6.2. The classical coordinate of the same wall: Jessen–Tornehave

A scholarly note confirming the diagnosis from classical zero theory of
almost-periodic functions. The canonical machinery for "zeros of almost-periodic
holomorphic functions in bands" is the Jessen–Tornehave theory of mean motions and
Jensen functions [JT45], extended to ζ in the strip by Borchsenius–Jessen [BJ48]: the
Jensen function φ(σ) = M_t(log|f(σ+it)|) is convex and its side derivatives measure
the **relative mean density** of zeros at each abscissa. For ζ with σ > ½, that mean
density is 0 (Bohr–Landau). That is: the classical theory of zeros of a.p. functions
is, by construction, a theory of averages — and a configuration with finite m (zero
mean density) is **invisible to the Jensen function**, indistinguishable from m = 0.
The entire classical apparatus lives on the averaged side of the quantifier; the D-109
dichotomy asks about the individual side. [Exact scope of BJ48 for ½<σ<1: NOT VERIFIED
in detail; its use here is illustrative only, not load-bearing.]

### 6.3. Balance of the blockage analysis

The remaining gap in the implication m<∞ ⟹ m=0 contains the average→individual
inversion — the same one from P43 — in the precise instance "non-emptiness of a
density-zero set of pointwise almost-periods". It is a strictly weaker instance than
those previously blocked (non-RH-equivalent, without self-blocking), which extends
P43's no-go with a new precision: **the wall does not distinguish between asking for
positive density and asking for a single point; it distinguishes between generic and
exceptional.** The number of witnesses required is irrelevant; their exceptionality is
what blocks. (This refines the phrase from Doc 111 §6.4: the wall was never about the
value of m — nor about the number of witnesses — but about seeing ONE individual unit
of anything.)

---

## 7. VERDICT

**VERDICT: PARTIAL IMPLICATION.**

The implication m < ∞ ⟹ m = 0 is neither proved nor refuted. It is **reduced, with
complete proof, to a single open lemma**, and all other routes are blocked with exact
location:

**What is proved (unconditional):**

1. **Theorem 2.3 / 5.1 (the reduction):** LP-112 (sequential pointwise almost-periodicity
   of ζ on compact disks of the strip) ⟹ m ∈ {0,∞}; in particular
   (m<∞) ∧ LP-112 ⟹ RH, and with the identity of Doc 109: RH ⟸ (target L8) ∧ LP-112.
   Under H(m) all the constants of the Rouché step are frozen (radius r < δ_min/2,
   margin η > 0, height threshold γ_max): there is no uniformity degeneration; exactly
   ONE τ is missing.
2. **Proposition 2.6 (the wall with sign):** under H(m), the set of τ good for
   Rouché in the disk of the zero has upper density ZERO (Bagchi + Hurwitz +
   Portmanteau). The hope "the good ones have positive measure" is false: the positive
   measure (B² almost-periods, Lemma 2.2) lives in the mean-in-t coordinate, which
   assigns zero weight to the window of the zero (Obs. 2.4). The B²→pointwise gap is
   not a missing estimate: it is the certification of non-emptiness of an exceptional
   set — P43's master quantifier, sequential instance.
3. **Proposition 2.7 (no self-blocking):** unlike D104, the sequential version does
   not collide with the density theorems — it needs zero density of replicas, which
   nothing obstructs. The route is unfed, not self-contradicted. LP-112 remains alive,
   non-RH-equivalent (RH ⟹ LP-112 via Bagchi; LP-112 only gives the dichotomy, not
   m = 0).
4. **Lemmas 3.1–3.3 (the Euler requirement, satisfied):** D111's cosh-examples are
   excluded at the first rung (not B² on lines; admit no self-approximation:
   |F(s+iτ)| → ∞); the separation of ζ is arithmetic and unconditional — Dirichlet
   series (B² level), ℚ-linear independence of {log p} = unique factorization
   (relative density and non-discreteness of the almost-periods: replicas at new
   heights), and random Euler product (Bagchi's support). Davenport–Heilbronn
   calibrates: without full Euler, the alternative realized is m = ∞ — the pattern
   m ∈ {0,∞} has no known counterexample in any class with a Dirichlet series.
5. **Moments line (§4), BLOCKED at two independent places:** (i) the feed does not
   exist — verified against D72 at the source: B_λ(log p) = ∫W_λ cos(s log p)dm_∞ is
   autonomous (transform of the test, no zeros — the goal's fear was unfounded), but
   the prime series diverges (Doc 105) and there is no arithmetic value of T_λ;
   (ii) the explicit-formula identities are tautological in the 4m parameters
   (Prop. 4.2: a single independent identity, satisfied identically; ξ_on = ξ/P_m
   has no explicit formula of its own); the non-tautological content is the sign =
   Weil's criterion = RH = inertia (P43 §4). Moreover (Obs. 4.3) the spectral gap
   ε₀ = Σ 2δ_j²K_λ(γ_j) is positive but its infimum over configurations is 0: finiteness
   protects arguments internal to the world (Rouché), not external evaluators
   (traces). Doc 110's Prop. 4.5 does not apply: finite rank ≠ a priori finite
   rank — Doc 110's boundary, confirmed from the other side.

**The exact remaining gap (unique):** LP-112⁻ — for the fixed disk D(ρ₀, r) around a
hypothetical off-critical zero and ε = η/2, exhibit ONE τ > γ_max + γ₀ + r + 1 with
sup_D |ζ(s+iτ) − ζ(s)| < ε. Status: open; non-RH-equivalent by known dictionaries;
its witnesses form a density-zero set under the hypothesis being refuted
(Prop. 2.6), so any proof will have to be a non-generic selection mechanism — outside
P43's list of argument forms.

**Answer to the decisive question of the goal** (does D104's blockage apply when only
ONE replica is needed?): **it does not apply** (Prop. 2.7) — but its place is taken by
a cleaner and deeper blockage: the single replica is a density-zero event, and the
master quantifier blocks certification of exceptional events totally independently of
how many are needed. The quantity dropped from "positive density" to "one"; the
difficulty did not drop at all. That invariance — the wall is insensitive to the
cardinality of what is asked, sensitive only to its exceptionality — is the
document's structural finding, and extends P43's no-go to the class of sequential
replica statements.

**For the phase:** the front is better than before in a precise sense: the analytic
half of the architecture (D-109) now has ONE lemma with a name, exact form, frozen
constants, complete conditional proof, a certificate of non-equivalence with RH, and
a certificate of non-self-blocking. It is the sharpest intermediate target the
program has produced on the rigidity side. What it asks for — selecting an exceptional
point of the Kronecker flow where the Euler observable meets itself — is exactly the
sequential version of the individual-orbit problem ω₀ of Doc 102. The two faces of the
program (torus recurrence, defect dichotomy) have converged on the same point: it is
not a coincidence; it is the wall, seen from its thinnest edge.

---

## References

**Internal (backward-only):** Doc 109 (§4.3–4.6: D-109, architectural identity, mean→
pointwise gap, Bagchi precedent; §6.1: recap of D70–72 and D105); Doc 110
(Prop. 4.5, axiom L6, §4.3–4.4); Doc 111 (Prop. 2.2, Cor. 2.3, Obs. 2.4, §2.3–2.5,
§3 anti-Siegel, Prop. 6.2, Obs. 6.3); Doc 108 (Theorems 3.3, 3.4; Prop. 2.5; §7.4);
Doc 105 (divergence (5√2/8)log X of the prime series; corrections to D70–72);
Doc 104 (self-blocking amplifier; via P42 §2 and P43 Thm. C); Doc 102 (Bagchi in the
program; ω₀ and the Euler observable); Doc 100 (semilocal positivity); Doc 99
(CCM-ZST); Doc 98 (Hypothesis T1; Cor. 2.4: cost 2δ²K_λ(γ₀)); Doc 95 (Lemma 2.2:
decay of dm_∞); Doc 72 (Thm. 4.1: T_λ = A_λ^{off} − Σ_p(log p/√p)B_λ(log p);
§3–5: B_λ as the Fourier transform of the test — **verified at source for this
document**); P43 (Principle 3.1; §4 value/inertia; Thm. C); P42; P41; P35 (κ = 2m).

**Literature (verifiable unless marked):**

- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge Univ. Press, 1932. (Classes
  B^p; Besicovitch almost-periodicity; B² closure of trigonometric polynomials.)
- H. Bohr, *Zur Theorie der allgemeinen Dirichletschen Reihen*, Math. Ann. 79 (1918),
  136–156; and the series *Zur Theorie der fast periodischen Funktionen* I–III, Acta Math.
  45–47 (1924–26). (Uniform almost-periodicity of Dirichlet series in half-planes of
  absolute convergence; general theory.)
- H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die
  ζ-Funktion und die L-Funktionen*, Rend. Circ. Mat. Palermo 37 (1914), 269–272.
  (Zero density off-critical.)
- B. Bagchi, *The statistical behaviour and universality properties of the Riemann
  zeta-function and other allied Dirichlet series*, Thesis, Indian Statistical Institute,
  Calcutta, 1981. [Bag81] (Functional limit theorem in H(D), unconditional; support of the
  measure.)
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta
  Math. Hungar. 50 (1987), 227–240. [Bag87] (Strong recurrence ⟺ RH.)
- A. Laurinčikas, *Limit Theorems for the Riemann Zeta-Function*, Kluwer, Dordrecht,
  1996. [Lau96] (Chs. 5–6: limit theorem in H(D) and
  support S = {f without zeros} ∪ {0}; standard exposition of Bagchi's apparatus.)
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed. (rev.
  D. R. Heath-Brown), Oxford Univ. Press, 1986. [Tit86] (Thm. 4.11: approximate
  formula; Thm. 7.2 and §7.2: unconditional mean square value in σ > ½; Ch. VIII:
  Ω-theorems, unboundedness of ζ on lines in the strip.)
- H. L. Montgomery, R. C. Vaughan, *Hilbert's inequality*, J. London Math. Soc. (2) 8
  (1974), 73–82. [MV74] (Mean value of Dirichlet polynomials.)
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London
  Math. Soc. 11 (1936), 181–185 and 307–312. [DH36]
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. [Wei52] (Explicit formula; positivity
  criterion ⟺ RH.)
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959, Vol. 2, Ch. X. [Gan59]
  (Newton's identities; Hankel forms; Jacobi–Frobenius.)
- N. I. Akhiezer, *The Classical Moment Problem*, Oliver & Boyd, 1965. [Akh65]
  (Hamburger moment problem; the finite-atomic case is determined.)
- B. Jessen, H. Tornehave, *Mean motions and zeros of almost periodic functions*, Acta
  Math. 77 (1945), 137–279. [JT45] (Jensen function; mean densities of zeros of
  holomorphic a.p. functions.)
- V. Borchsenius, B. Jessen, *Mean motions and values of the Riemann zeta function*,
  Acta Math. 80 (1948), 97–166. [BJ48] [Exact scope for ½<σ<1: NOT VERIFIED in
  detail; illustrative use only in §6.2.]
- D. Platt, T. Trudgian, *The Riemann hypothesis is true up to 3·10¹²*, Bull. London
  Math. Soc. 53 (2021), 792–797. (Via D111 §2.4(c).)
- H. Weyl, *Über die Gleichverteilung von Zahlen mod. Eins*, Math. Ann. 77 (1916),
  313–352. (Equidistribution; Kronecker–Weyl on the torus.)

*End of Document 112.*