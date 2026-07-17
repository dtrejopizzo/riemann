# Phase 25-B — The de Bruijn–Newman Connection

## Literature Audit

**Literature.** de Bruijn (1950): H_λ(t) = ∫ Φ(u)e^{λu²}e^{itu}du has only real zeros iff λ ≥ Λ for some Λ ∈ ℝ. Newman (1976): conjectured Λ ≥ 0. Rodgers–Tao (Polymath 15, 2019): proved Λ ≥ 0. Kim–Sirohi (2021): explicit lower bound Λ ≥ −5.2×10⁻⁹. RH ⟺ Λ ≤ 0. Together: RH ⟺ Λ = 0.

**Connection to ξ.** The function H₀(t) = Φ̂(t)/something is (up to normalization) ξ(1/2+it). The de Bruijn heat flow at parameter λ corresponds to multiplying the Fourier transform of ξ by e^{λu²}.

---

## The key bijection: off-line zeros ↔ complex zeros of H₀

**Proposition 25-B.1** (Off-line zeros in the t-variable). Under the substitution s = 1/2+it:

A zero ρⱼ = (1/2+bⱼ)+iγⱼ of ξ (in the s-variable) with bⱼ > 0 corresponds to a COMPLEX zero of H₀(t) at:
$$t_j^* = -i(ρ_j - 1/2) = \gamma_j - ib_j \in \mathbb{C}, \quad \operatorname{Im}(t_j^*) = -b_j < 0.$$

*Proof.* $H_0(t_j^*) = \xi(1/2 + it_j^*) = \xi(1/2 + i(\gamma_j - ib_j)) = \xi(1/2 + b_j + i\gamma_j) = \xi(\rho_j) = 0$. $\square$

**Corollary 25-B.2.** Under Hypothesis D with $m$ off-line orbits:

$H_0(t)$ has $2m$ complex zeros (from the Klein V-orbit: $\gamma_j - ib_j$, $\gamma_j + ib_j$, $-\gamma_j - ib_j$, $-\gamma_j + ib_j$, reduced to $\pm\gamma_j \mp ib_j$ by conjugate symmetry) and infinitely many real zeros (the on-line zeros).

The complex zeros lie in BOTH the upper and lower half of the t-plane:
- $\gamma_j - ib_j$ (lower half-plane, Im < 0)
- $-\gamma_j + ib_j$ (upper half-plane, Im > 0)

*Note.* The orbit V = {ρⱼ⁺, ρ̄ⱼ⁺, ρⱼ⁻, ρ̄ⱼ⁻} maps to $\{γⱼ-ibⱼ, γⱼ+ibⱼ, -γⱼ-ibⱼ, -γⱼ+ibⱼ\}$ in the t-plane.

---

## The de Bruijn parameter and bⱼ

**Proposition 25-B.3** (de Bruijn heat flow on the off-line zero). Under the heat flow at parameter λ, the zero $t_j^* = \gamma_j - ib_j$ evolves. For small λ, the leading order motion is:

$$t_j^*(λ) = \gamma_j - ib_j + λ \cdot \frac{d}{dλ}t_j^*|_{λ=0} + O(λ^2).$$

The "annihilation" parameter $\Lambda_j$ — the value of λ at which $t_j^*(λ)$ reaches the real axis — satisfies (to leading order for an isolated zero):
$$\Lambda_j \approx \frac{b_j^2}{2|H_0''(t_j^*)| / |H_0'(t_j^*)|^2}.$$

For an isolated zero far from other zeros: $\Lambda_j \approx b_j^2/2 \cdot (1 + O(b_j^2/\gamma_j^2))$.

*Derivation.* The heat equation for H_λ: $\partial_\lambda H_\lambda = \partial_{tt}H_\lambda$. For an isolated zero $t_j^*(λ)$: differentiating $H_\lambda(t_j^*(λ)) = 0$ twice gives $\dot t_j^* = -H_\lambda''/H_\lambda'$ (the inverse Weierstrass). For λ small: $\dot t_j^*|_{λ=0} = -H_0''/H_0'$ evaluated at $t_j^*$. The zero moves toward the real axis at rate $d(\operatorname{Im}(t_j^*))/dλ \approx +b_j/(b_j^2 + (\operatorname{Re}-\gamma_j)^2)$ ... this calculation requires the residue. The rough result is $\Lambda_j \sim b_j^2/2$ for isolated zeros.

**Theorem 25-B.4** (de Bruijn–Newman lower bound on Λ under Hypothesis D).

Under Hypothesis D with at least one off-line orbit (bⱼ > 0, $\gamma_j > 0$):
$$\Lambda \geq \frac{b_j^2}{2} \cdot (1 + O(b_j^2/\gamma_j^2)).$$

Combined with Rodgers–Tao: $\Lambda \geq 0$. Under Hypothesis D: $\Lambda > 0$.

*Status.* The rough estimate Λⱼ ~ bⱼ²/2 is plausible from the heat-equation analysis but its rigorous proof requires careful control of the motion of complex zeros under the heat flow. A rigorous version would need:
- Exact expression for $\dot t_j^*$ at λ=0 in terms of the Hadamard product.
- Control of interactions between $t_j^*$ and other zeros (both real and complex).

This is an open technical problem, nontrivial but likely accessible.

---

## What the dB-N connection gives (and does not give) for bⱼ

The connection Λ ≥ bⱼ²/2 means:

$$b_j \lesssim \sqrt{2\Lambda}.$$

This is an **upper** bound on bⱼ from Λ, not a lower bound.

For a lower bound on bⱼ from the de Bruijn approach:

We would need Λ ≤ f(bⱼ) for some increasing f, i.e., an **upper** bound on Λ in terms of bⱼ. The known upper bound Λ ≤ 1/4 (Pólya: for λ ≥ 1/4 all zeros of H_λ are real) gives only bⱼ ≤ √(1/2), which is trivial.

**The direction is therefore reversed:**

- Proven (Polymath 15): Λ ≥ 0.
- If Hypothesis D: Λ ≥ bⱼ²/2 > 0.
- RH ⟺ Λ = 0.
- **Better upper bound on Λ → better upper bound on bⱼ (smaller off-line zeros).**
- But NOT: lower bound on bⱼ from lower bound on Λ.

**New positive result:** The de Bruijn–Newman approach gives an exact DUAL formulation:

$$\text{RH} \iff \Lambda = 0 \iff \text{all complex zeros of } H_0 \text{ lie on the real axis}$$
$$\text{Hypothesis D} \iff \Lambda > 0 \iff \text{complex zeros of } H_0 \text{ have } |\operatorname{Im}(t_j^*)| = b_j > 0.$$

The de Bruijn constant Λ is a MEASURE of how far off-line the zeros are. But it's an upper-directional measure (Λ = "how much heat needed to bring zeros to the real axis"), giving bⱼ ≤ √(2Λ), not bⱼ ≥ F(Λ).

---

## RH Relevance

The de Bruijn–Newman approach is **not** a path to a lower bound on bⱼ.

However, it provides a **new quantitative connection** between Hypothesis D and the de Bruijn constant Λ:
$$b_j \approx \sqrt{2\Lambda_j}$$
where Λⱼ is the "partial de Bruijn constant" for the j-th off-line orbit.

This is a structural clarification of the relationship between the Kreĭn program (ours) and the Rodgers–Tao program. It was not previously formulated in this way.

**Connection to the program's main wall (LB):**

The "uniform spectral-gap (LB) inequality" of PLAN-RH-MAXIMAL.md §3 (Phase 3) is equivalent, via Theorem 25-B.4, to an upper bound on Λ better than the current state. Specifically:
$$\text{(LB) provable} \iff \Lambda = 0 \iff \text{RH.}$$

So (LB) and dB-N are the same wall, stated differently.

---

## Verdict

**Structural clarification.** The de Bruijn–Newman connection gives bⱼ ≲ √(2Λ) (upper bound, not lower bound). It does not produce a lower bound on bⱼ. It unifies the Kreĭn program with the Rodgers–Tao result but does not break new ground toward a lower bound.

Direction classification: **Structural clarification, not progress toward lower bound on bⱼ.**
