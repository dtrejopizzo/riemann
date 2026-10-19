# Goal B — attempt to prove the lower bound of ε₀ (transparent, with [GAP]) **Goal:** bound from below ε₀(λ) = min_{g∈PW_{L/2}, ‖g‖=1} Σ_j |g(γ_j)|² (frame operator of the
zeros γ_j in PW_{L/2}; L=2logλ). Conjectured scale ε₀ ~ C e^{−S L}, S≈1 (not a firm target). Markers: [OK] rigorous step · [GAP] inferential step that I do NOT have justified. --- ## Step 1 [OK] — reduction to the residual over the horizon
g∈PW_{L/2} is entire of type L/2. By Jensen, its zero density ≤ L/2π. The γ_j have
local density (1/2π)log(T/2π), which equals L/2π at T*=2πλ² (Lemma 2). ⟹ g can vanish at
the γ_j with T≤T* (interpolation possible) but NOT at all those with T>T* (over-density). Then ε₀ = min_{g∈PW_{L/2},‖g‖=1, g(γ_j)=0 ∀γ_j≤T*} Σ_{γ_j>T*} |g(γ_j)|² + (corrections).
The minimizer vanishes below T* and leaves a residual above. ## Step 2 [OK] — the minimizer is the truncated canonical product
The optimal g that vanishes at {γ_j ≤ T*} and is of type L/2 is (up to normalization) the
canonical product P_{T*}(z) = ∏_{γ_j≤T*}(1 − z/γ_j)·e^{z/γ_j}, which has exponential type ~ (density)·π
= (n(T*)/T*)·π → L/2 (it exactly uses the band; Lemma 2). P_{T*} is the truncation to type L/2 of
ξ. ⟹ ε₀ ≍ ‖P_{T*}‖^{−2} · Σ_{γ_j>T*} |P_{T*}(γ_j)|². ## Step 3 [OK] — the residual is the tail of the product beyond the cutoff
For γ_k > T* (first zero above the horizon), P_{T*}(γ_k) = ∏_{γ_j≤T*}(1−γ_k/γ_j)e^{γ_k/γ_j}
≠ 0. The magnitude |P_{T*}(γ_k)| / ‖P_{T*}‖ is the residual. Rewriting the log: log|P_{T*}(γ_k)| = Σ_{γ_j≤T*} [log|1−γ_k/γ_j| + γ_k/γ_j].
With γ_k ≈ T* and γ_j ranging over {≤T*}: it is a sum over ~n(T*)=λ²L/(2π)·(…) terms. ## Step 4 [GAP] — the asymptotics of the tail = de Branges extremal theorem
Missing: the asymptotics of R(λ):= ‖P_{T*}‖^{−2} Σ_{γ_j>T*} |P_{T*}(γ_j)|²
as λ→∞. That is, how much the residual of the canonical product truncated to type L/2 is worth,
evaluated just above the horizon, normalized. **[GAP]** I do not have the argument that gives R(λ) ~ C e^{−SL}. What is needed: (a) controlling log‖P_{T*}‖ (norm of the truncated product) — via Jensen's formula/zero counting, connected to the explicit formula; (b) controlling log|P_{T*}(γ_k)| at the first zero above T* — the "tail" of the product; (c) the difference (b)−(a) gives log R; showing that = −SL + O(1). This is the asymptotics of canonical products in the critical-density regime = de Branges / Beurling–Selberg theory. It is the only missing step. ## What the [GAP] would need as input (for whoever closes it)
- The regularity of the zero distribution near T* (spacing ~2π/L, fluctuations). Under RH this is controlled; WITHOUT RH, only via density (PNT) — and that is where the non-circularity question lies: is DENSITY (PNT) enough for (a)-(c), or is the fine position needed (≈ RH)? If density suffices ⟹ B is non-circular. If fine position is needed ⟹ B is RH-dependent.
- A Beurling–Selberg-type estimate for the interpolation residual at critical density. ## Step 4A [COMPUTED] — CORRECTION of the scaling (Jensen, pure density) Jensen integral log|P_{T*}(x)| ≈ ∫_0^{T*}log|1−x²/t²|·(1/2π)log(t/2π)dt (density only).
Computed: J(T*)−min_x J grows like **c·λ²·logλ = c·n(T*)** (number of zeros below the horizon):
λ=3.7→19.9, 5→51.6, 7→137, 10→364, 15→1043, 25→3708. (J(T*)−minJ)/L GROWS (not constant). **[RETRACTED] The "correction" −log ε₀ ~ c·λ²logλ was FALSE.** The discriminant experiment
(ε₀ converged at λ=5, even sector, N=75≈T*) refuted it: it predicted −log ε₀~103 at λ=5, the actual value
is 46.7. The Jensen integral describes the growth of the BARE canonical product, NOT ε₀ —
due to the ‖·‖ normalization and its being a frame eigenvalue (caution 4A′ of, correct). **Actual status (two converged points):** (λ=3.7,L=2.62)→−log ε₀=46.03; (λ=5,L=3.22)→46.66 ⟹
slope≈1.05 ⟹ **ε₀ ≈ C₀·e^{−SL}, S≈1, C₀≈e^{−43.3}** (working hypothesis restored; the
original e^{−L} was correct in the exponent). The new phenomenon to explain is the large C₀
(−log C₀≈43): it dominates the absolute value but not the slope in L. ## Rigorous bounds that DO frame the [GAP]
- [OK] ε₀ > 0 (completeness, Step 1 + Jensen).
- [OK] ε₀ ≤ C/L² (sinc test).
⟹ the [GAP] lives in the interval (0, C/L²], and what is missing is the precise asymptotics of R(λ). ## Frank non-circularity diagnosis (the most valuable part of the attempt)
The [GAP] reduces to (a)-(c), which are sums Σ_{γ_j≤T*} f(γ_j) over zeros. By the explicit
formula, Σ_{γ_j} f(γ_j) = (archimedean) − Σ_p (primes). ⟹ sums (a)-(c) **are expressed
via primes (PNT)** if f is smooth. BUT log|1−γ_k/γ_j| has a SINGULARITY as γ_j→γ_k (near
the horizon): the terms with γ_j close to T* dominate and are NOT smooth. ⟹ controlling those
nearby terms requires the fine POSITION of the zeros near T*, not just the density. **Hint (not a proof):** B could be RH-dependent via the singular terms near the horizon. That is the exact point to decide — and is where de Branges/ should look.
