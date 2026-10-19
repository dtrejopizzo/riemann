# Propagation of the scale correction −log ε₀ ~ c·n(T*) through Link 2 **Correction:** −log ε₀(λ) ~ c·n(T*) ~ c·λ²logλ (super-exp in L), NOT ~ L. (From 4A Jensen +
minimizer = canonical product via Thm 1.1.iii + Hadamard.) It must be propagated to see what
survives and what falls. ## SURVIVES (everything that is a RATIO or eigenvector — scale-independent)
- (i) exact restriction A_λ=A_∞|_{E_λ}.
- Lemma 2: horizon T*~2πλ² (independent of the scale of ε₀).
- **Relative spectrum {ε_k/ε₀}=(k+1)²** — these are RATIOS, they do not depend on the absolute scale. ✔
- Alternating parity, collapse of profiles φ_k(x) — these are eigenvectors, scale-independent. ✔
- Existence of 𝓛 (from the convergence of the relative spectrum + eigenvectors). ✔
- Argument #3 (rescaling by ε₀ → isolated bottom → Galerkin): the ARGUMENT survives; only ε₀ is much smaller. ✔
- Beurling–Deny: A_λ=∫q|f|²+𝓔_θ+𝓔_prime; c=−ψ''(¼)/8; M_0,M_2~λ^{1/2−|x|}. ✔ (Consistency: the B–D terms are O(λ^{1/2}) and cancel to ε₀~e^{−cλ²logλ} — super-precise cancellation = the minimizer annihilates ALL zeros = near-saturated Weil positivity. OK.) ## FALLS (every interpretation of the ABSOLUTE SCALE of ε₀)
- **"Action S≈1":** −log ε₀/L = cλ²logλ/(2logλ) = cλ²/2 → ∞, NOT 1. **DEAD.** It was an artifact.
- **"ℏ=1/L semiclassical" for the scale:** the scale is NOT e^{−S/ℏ}=e^{−SL}; it is e^{−cλ²logλ}. The WKB interpretation of the SCALE falls. (The O(1/L) correction of the RELATIVE spectrum survives, it is a ratio.)
- **"e^{−L} tunneling":** dead (N-limited artifact).
- **"ε₀ converges in N":** PREVIOUS CLAIM FALSE. ε₀ does NOT converge — it keeps decreasing with N (the effective horizon ~N·2π/L grows toward T*). What I saw (N=8→24, ratios→1.1) was slow approximation, NOT convergence. [Test: eps0_highN.py — should keep decreasing.] ## EXPLAINS the previous data (consistency)
The operator at N=24 for λ=3.7 and 5 gave −log ε₀~46 nearly constant. NOT because it is the real
scale, but because both were **N-limited to the same effective horizon (~50)**: ε₀~e^{−c·n(effective
horizon)}, and the effective horizon ~50 in both ⟹ similar ε₀. The real scale (N→∞, horizon T*)
is e^{−c·n(T*)}~e^{−cλ²logλ}, never reached by the N-limited operator. ## Consistency verdict [CORRECTED by the eps0_highN test]
TEST (λ=3.7, N=16..36): ε₀ CONVERGES (−log ε₀ plateau ~46.0, Δ→0.01) and at N=36 the horizon
reaches the full T*=86. ⟹ **my prediction "ε₀ does not converge in N" was FALSE — RETRACTED.**
ε₀ DOES converge (the original claim was correct). **UPDATED with converged λ=5 (discriminant experiment):**
- **ε₀ converges in N** (verified λ=3.7 N=36=T*, λ=5 N=75≈T*). I retract "ε₀ does not converge".
- **Two converged points:** (λ=3.7,L=2.62)→−log ε₀=46.03; (λ=5,L=3.22)→46.66. Slope≈1.05.
- **λ²logλ (Jensen of the bare product) REFUTED:** it predicted −log~103 at λ=5; actual 46.7.
- **e^{−L} RESTORED as working hypothesis:** ε₀≈C₀e^{−SL}, S≈1.05≈1, C₀≈e^{−43.3}. (What confused things before: the constant C₀~e^{−43} dominates the absolute value ~46, but the SLOPE in L is ~1 = e^{−L}.) The NEW phenomenon to explain is the large C₀ (−log C₀≈43). SURVIVES: the relative facts (𝓛, (k+1)², #3, Beurling–Deny, c, M₀/M₂) + ε₀~C₀e^{−SL} with S≈1.
FALLS/REFUTED: λ²logλ (bare Jensen); "ε₀ does not converge". Jensen remains relevant (structure of
the product) but does NOT control ε₀ (normalization + frame extremal; caution 4A′ of correct). ## Implication for Goal B
B is no longer "prove e^{−L}". It is **"prove −log ε₀ ~ c·n(T*)"**, with:
- minimizer identified (= canonical product, Thm 1.1.iii + Hadamard);
- leading order derived from DENSITY (PNT) = non-circular;
- missing: rigorous normalization + lower bound (de Branges) + the constant c (4B, possible dependence on fine position near the horizon).
