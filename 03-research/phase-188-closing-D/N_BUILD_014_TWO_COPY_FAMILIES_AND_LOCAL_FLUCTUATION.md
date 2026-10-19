# N_BUILD_014 — Non-concentrating families: two copies of a fixed profile at distance d. A prime-side local fluctuation Ξ, a proved implication "Ξ unbounded ⇒ t_∞ = 0", and the reduction of multi-copy families to packets

Pen and paper. Notation of N_BUILD_011–013. Premise respected: the summability statement of N_BUILD_013 §2 is recorded only as a
statement about packet limits and is NOT used below as a criterion for any route.

## Corpus check
Paper 47 lem:wit-freeze, thm:wit-Tc(i),(v) (extension by zero; dichotomy λ_A ≥ 0 ∀T or ≤ −c eventually), prop:wit-cheb; L2_BUILD_008
(clamped modes); R160_D4 Thm 5.1 (translations are window shifts); R186_046 Theorem X (new primes cancel σ on U at resolution π/T).
grep "two copies|translate|disjoint supports|cross term at lag d|local fluctuation|Ξ(d)": Theorem X uses averaged packets; no memo
computes the window form of two disjoint copies of a fixed primitive profile and its cross term. New: §1–§4.

## 1. Two-copy identity (PROVED)
Fix T₀ and F₀ ∈ P_{T₀} ∩ D_{T₀} real, ‖F₀‖ = 1, c₀ := c_{F₀}. For d > 2T₀ and T ≥ T₀ + d/2 put F := F₀ + τ_dF₀ (placed inside I_T; the
supports are disjoint). Then F ∈ P_T (A(τ_dF₀) = e^{d/2}A(F₀) = 0, likewise B), ‖F‖² = 2, c_F = 2c₀ + c₀(·−d) + c₀(·+d), and
 𝔞_T(F) = 2𝔞_{T₀}(F₀) − X(d),  X(d) := Ξ(d) + ∫c₀(v)K(v+d)dv,
 Ξ(d) := Σ_n v_n c₀(log n − d)   (the comb seen through c₀ shifted to scale x = e^d).
*Proof.* eq:Aform: C₀‖F‖² + 𝔈(c_F) − Σ v_n c_F(log n). 𝔈(c_F) = ∫₀^∞(c_F(0) − c_F(u))K(u)du = 2𝔈(c₀) − ∫₀^∞[c₀(u−d) + c₀(u+d)]K(u)du,
and c₀(u+d) = 0 for u > 0 (d > 2T₀); the comb splits likewise (c₀(log n + d) = 0). ∎
**Main term vanishes exactly (PROVED).** The PNT density 2e^{u/2} paired with c₀(·−d) gives 2e^{d/2}∫c₀(v)e^{v/2}dv = 2e^{d/2}Re(A B̄)(F₀)
= 0. So Ξ(d) = Σ_n v_n c₀(log n − d) − 2∫c₀(v)e^{(v+d)/2}dv: it is a pure Chebyshev fluctuation at scale x = e^d, smoothed by the
fixed Tate-annihilated profile c₀ (Mellin transform of c₀ vanishes doubly at ±i/2). The archimedean cross term is O(e^{−d/2})
(K(v+d) ≤ 2e^{−(v+d)/2}(1+O(e^{−d}))).
Similarly G_κ(F) = 2G_κ(F₀) + O(e^{−d/2}) (the kernels of m and of κ/(¼+τ²) at lag ≥ d − 2T₀ are O(e^{−d/2})).

## 2. Theorem A (PROVED): unbounded local fluctuation ⇒ t_∞ = 0
If for some F₀ as above limsup_{d→∞} Ξ_{F₀}(d) = +∞, then t_∞ = 0 (N_BUILD_012).
*Proof.* For the two-copy F at window T = T₀ + d/2 + 1, 𝔞_t(F) = (1−t)G_κ(F) + t𝔞_T(F) = (1−t)(2G_κ(F₀) + o(1)) + t(2𝔞(F₀) − Ξ(d) + o(1)),
negative as soon as t > (2G_κ(F₀) + o(1))/(2G_κ(F₀) − 2𝔞(F₀) + Ξ(d) + o(1)) → 0 along d with Ξ(d) → ∞. So t*(T) → 0 along these
windows, and t* is nonincreasing (012 §1(a)). ∎
**Corollary A′ (necessary condition, PROVED).** t_∞ > 0 implies, for every T₀ and every unit F₀ ∈ P_{T₀},
 limsup_{d→∞} Ξ_{F₀}(d) ≤ 2(1/t_∞ − 1)G_κ(F₀) + 2𝔞_{T₀}(F₀),
and the target implies limsup_d Ξ_{F₀}(d) ≤ 2𝔞_{T₀}(F₀) (take t = 1). This is a **scale-local, one-sided, exponent-½ bound for a fixed
smoothing of the primes** — (N) localized to one profile and one scale at a time, with the PNT main term removed by the Tate
conditions, not by subtraction. Call it (Ξ).

## 3. Multi-copy families reduce to packets (PROVED + ARGUED)
For k copies at positions a_1 < … < a_k (gaps > 2T₀) with coefficients x_j: 𝔞_T(Σx_jτ_{a_j}F₀) = ‖x‖²𝔞(F₀) − Σ_{i≠j}x_ix̄_j X(a_i − a_j)
(same proof). Boundedness of the ratio over all k, positions and coefficients requires the kernel (i,j) ↦ X(a_i − a_j) to be bounded above
by C‖x‖² as a quadratic form for all configurations. On lattices a_j = jL with x_j = e^{iγjL}, k → ∞, the copies build a packet at
frequency γ with profile F̂₀ (ARGUED: the lattice sum is a Fejér-type concentration), and the condition becomes the packet condition
of N_BUILD_013 (critical limit). So: **every family built from one profile by translations and modulations falls under either the
two-copy test (Theorem A, k = 2) or the packet test (013), up to the intermediate k.** Families not of this form (genuinely
multiscale profiles, minimizer-like families) are not covered.

## 4. Is (Ξ) weaker than (N)? (honest status)
- (Ξ) has slack built in: the target gives Ξ ≤ 2𝔞(F₀), while (Ξ) with t_∞ > 0 allows the extra 2(1/t_∞ − 1)G_κ(F₀) ≥ 2(1/t_∞−1)η_κ > 0.
- Theorem A shows the dichotomy direction "local fluctuation unbounded above ⇒ t_∞ = 0" with prime-side data only.
- Whether "(Ξ) for all F₀ ⇒ t_∞ > 0" holds is OPEN: the multi-copy forms of §3 and non-translation families intervene.
- Hence the structural picture: t_∞ = 1 ⟺ target; t_∞ = 0 ⇐ (Ξ) fails for some profile; t_∞ ∈ (0,1) would require (Ξ) for every
profile together with a witness — not excluded by anything proved here. **No full {0,1}-dichotomy is proved.**
- (Ξ) at a fixed profile is a statement about the single function d ↦ Ξ_{F₀}(d) on [2T₀, ∞), built from Λ with a fixed compactly
supported weight: it is the most local form of (N) found so far. By cor:void it cannot follow from class membership (finite
modifications change Ξ only for d < max log n of the modification, so they do NOT kill (Ξ) as d → ∞ — (Ξ) is a tail statement;
W-tail-type deletions do change it, consistent).

## Self-review
1. §1: F ∈ P_T — A(τ_dF₀) = ∫F₀(t−d)e^{t/2}dt = e^{d/2}A(F₀): correct. Placement inside I_T needs T ≥ T₀ + d/2 (taking F₀ centred at
−d/2): correct. Disjointness gives ‖F‖² = 2.
2. Main-term vanishing uses ∫_ℝ c₀(v)e^{v/2}dv = Φ(1)Φ(0) = A·B = 0 (real F₀): correct; the window truncation is irrelevant since
c₀(· − d) is supported in [d − 2T₀, d + 2T₀] ⊂ (0, 2T).
3. Theorem A: the threshold computation is exact up to O(e^{−d/2}); correct. It uses no zero information.
4. §3 lattice-to-packet is ARGUED (not written in full).
5. Note the coordinator's premise: nothing in this memo uses the summability statement; Theorem A is prime-side.
No sign contact; no negative value certified.
