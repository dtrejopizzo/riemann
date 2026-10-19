# Link 2 (convergence ξ̂_{λ,N} → Ξ): structure, attack and status **Focus:** this is THE gap in the map to RH. Everything else (Links 1,3,4) is proved or
classical. Closing Link 2 ⟹ RH. --- ## 0. Why we pivoted from numerical to theoretical (candid) E6 tried to measure the "horizon" H(λ) = height up to which zeros are resolved, as an
empirical measure of 2b. **Numerically blocked:** cond(QW_λ^N) ≈ 10¹⁶–10¹⁷ (direct
diagnosis). The first zero survives (1e-14 at N=70) but the higher zeros — which depend on
the small components of the eigenvector of the smallest eigenvalue — drown in float64 noise. The
H(λ) measurement came out non-monotone in λ (λ=3.0→H≈56 but λ=3.7→H≈30): noise, not signal.
Resolving it requires mpmath at N~50-80 (expensive). **The 2b crux does not yield to brute numerical force here.** What the numerics DID leave solid: 2a converges fast (E4hp, geometric), and the engine is
validated on ζ (a=1/4) and L(χ_-4) (a=3/4). --- ## 1. 2a (N→∞ at fixed λ): REDUCED to simplicity. Almost closed. **Claim:** ξ̂_{λ,N} → ξ̂_{λ,∞} locally uniform, MODULO the smallest eigenvalue of A_λ
being simple (= hypothesis H1 of Thm 1.1). **Argument (solid):** 1. **A_λ has compact resolvent ⟹ discrete spectrum.** The scaling operator D_log = −i d/d(log u) on the COMPACT interval [λ⁻¹,λ] with periodic conditions has discrete spectrum {2πk/L}. The form QW_λ (3.19) = archimedean (θ-weight, defines the form domain) − prime part. The prime part is Σ_{n≤λ²} Λ(n) T(n), a **FINITE sum of bounded operators** (T(n) bounded: convolution on L² over a compact group is continuous, bounded evaluation). Bounded, semi-bounded-below perturbation (Prop 3.3). The form domain embeds **compactly** into L²([λ⁻¹,λ]) by **Rellich–Kondrachov** (bounded interval). ⟹ A_λ has compact resolvent ⟹ **discrete** spectrum, every eigenvalue isolated, including the infimum ε_∞. 2. **Galerkin/finite sections converge to the isolated ground level.** E_N = span{V_k: |k|≤N} ⊂ E_{N+1}, and E = ∪E_N is a **core** of the form (Prop 3.4). By min-max, ε_N ↓ ε_∞ monotonically. Since ε_∞ is an **isolated** eigenvalue (step 1), the spectral projector of the section converges in norm and the eigenvector ξ_N → ξ_∞ in form norm (standard Galerkin approximation theory for semi-bounded forms with an isolated ground level). 3. **Continuous transform ⟹ ξ̂_N → ξ̂_∞ locally uniform.** The transform ξ ↦ ξ̂ (3.5) is continuous in the relevant norm; convergence of ξ_N ⟹ local-uniform convergence of ξ̂_N to ξ̂_∞ (entire functions, compacta). **Residual gap of 2a:** simplicity of the ground level ε_∞ (H1). Reducible to the **even
sector** (H2, ξ even by invariance ι: u↦u⁻¹) + a nodal/Perron–Frobenius argument in the
even sector. It is a bounded, classical problem, NOT the wall. > **Status of 2a: essentially closed, modulo H1 (simplicity).** This is new and
> concrete mathematics for the program — the first piece of the convergence gap with a real proof. --- ## 2. 2b (λ→∞): the crux. Mechanism identified, proof open. **Key phenomenon to explain (from the data):** the 1st zero comes out at ~1e-18 with primes ≤13
(E4hp; paper: 1e-55). This is **far faster than truncation of the explicit formula**
(ψ(X)−X ~ O(1) at X=13). ⟹ **2b is NOT prime truncation.** The rigidity of
Carathéodory–Fejér extracts the zero with precision that truncation does not explain. **The real structure of 2b = growth of the HORIZON.** At fixed λ, ξ̂_λ is essentially
band-limited (band ∝ L=2logλ); it resolves zeros up to a height H(λ) and not above that.
2b ⟺ **H(λ) → ∞**. **Conjectured mechanism (zero-independent, the promising direction):**
the number of zeros up to height T is N(T) ~ (T/2π)log(T/2π); the number of primes ≤λ² is
π(λ²) ~ λ²/(2logλ). The operator "fixes" zeros as long as it has enough prime constraints.
Equating N(H(λ)) ~ π(λ²) gives the horizon. If this is correct, **H(λ)→∞ is governed by the
prime COUNT (PNT) — a prime-side datum, independent of the location of zeros.** > **If H(λ)→∞ is proved from π(λ²)→∞ (PNT), then 2b → RH is NON-circular.** That is the
> bet. The risk: that "fixing" each zero requires fine control of the rest of the
> spectrum that secretly amounts to zero-free regions (RH). Deciding this is the
> central pure-proof question of the program. **Next step for 2b (once mpmath at large N is available):** measure H(λ) cleanly (high precision) and
contrast its rate against π(λ²) (PNT prediction) vs N(T) — if H(λ) ~ (the height such that
N(H)=π(λ²)), the counting mechanism is confirmed and the theoretical target is fixed. --- ## 3. Gap status (summary) | Sub-link | Status | What's missing |
|---|---|---|
| 2a (N→∞) | **essentially closed** (compact resolvent + Galerkin) | simplicity H1 (even sector + nodal) |
| 2b (λ→∞) | mechanism identified (horizon ~ prime count, PNT) | proof of zero-indep H(λ)→∞; mpmath measurement of the rate | Closing 2a (via H1) is reachable and publishable. 2b is the real crux, now with a
concrete target (H(λ)→∞ by PNT) instead of abstract "convergence".
