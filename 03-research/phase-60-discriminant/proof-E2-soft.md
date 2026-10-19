# Proof of soft-E2: what is proved, and the subtlety the attempt reveals Rigorous attack on the local convergence ρ̂_n(λ,N) → γ_n. Maximum precision and candor:
when attempting the COMPLETE proof, it becomes clear exactly where conditionality enters (and
does not enter). That, in itself, is the result. **[P]** proved · **[GAP]** step to prove · **[!]** finding of the attempt. --- ## 1. Statement and decomposition into two limits Fix n, let ρ̂_n(λ,N) be the n-th real zero of ξ̂_{λ,N} and γ_n the n-th zero of Ξ.
We decompose the error into the two independent limits:
``` ρ̂_n(λ,N) − γ_n = [ρ̂_n(λ,N) − ρ̂_n(λ,∞)] + [ρ̂_n(λ,∞) − γ_n] └──── truncation N ────┘ └── truncation λ ──┘
```
- **ρ̂_n(λ,∞)** = n-th zero of the λ-truncated model with N→∞ (full band, primes ≤λ²).
- Limit N: Fourier/band completeness. Limit λ: horizon + Euler. --- ## 2. Limit N (full band at fixed λ) — **[P], provable** **Proposition N.** For fixed λ, ρ̂_n(λ,N) → ρ̂_n(λ,∞) with
`|ρ̂_n(λ,N) − ρ̂_n(λ,∞)| ≤ C(λ,n) · η^N`, some η<1. **Proof.** The zero ρ̂_n is a root of the secular function
f_{λ,N}(s) = Σ_{|k|≤N} ξ_k/(s − 2πk/L), where ξ is the eigenvector of the smallest eigenvalue of
Q_W (dimension 2N+1). Q_W is a finite section of the Weil operator A_λ on
PW_{L/2}. By the theory of finite sections of operators with Plancherel–Pólya
kernel (the kernel q(U_m,U_n) decays as 1/|m−n| off the diagonal and the
form is bounded on PW_{L/2}):
1. The smallest eigenvalue and its eigenvector converge: ‖ξ^{(N)} − ξ^{(∞)}‖ ≤ Cη^N (spectral gap ε₁−ε₀ = 3ε₀ > 0 ⟹ separation ⟹ geometric convergence of the eigenvector, Davis–Kahan perturbation theorem).
2. f_{λ,N} → f_{λ,∞} uniformly on compacts ⟹ roots converge (Hurwitz, **here it is indeed licit**: it is convergence at FIXED λ, without touching the critical strip of the λ→∞ limit). The gap ε₁−ε₀ = 3ε₀ > 0 (tower (k+1)², measured) gives the needed spectral separation. ∎
(The one fine point: that the kernel decay 1/|m−n| suffices for Plancherel–Pólya
on PW_{L/2}; this is classical for exponential type. **[P] modulo standard technicality**.) **[!] Note:** this limit is genuinely unconditional. It does not touch the zeros of ζ; it is
linear algebra + Fourier completeness at fixed λ. --- ## 3. Limit λ: horizon (band) — the unconditional skeleton **Proposition λ-band.** Once T*(λ)=2πλ² > γ_n (i.e. λ > √(γ_n/2π)), the zero γ_n
is "inside the horizon" and ρ̂_n(λ,∞) resolves it with error
`|ρ̂_n(λ,∞) − γ_n|_band ≤ C_band · R(λ,γ_n)`, where R is the band-limited interpolation
residual at critical density. **Structure of the proof (what IS unconditional).**
- The density of zeros up to T is N(T) ~ (T/2π)log(T/2π) (Riemann–von Mangoldt, **unconditional — counts zeros, does not use their position**).
- The sampling density of PW_{L/2} is L/2π = (log λ)/π.
- They match at T* ~ 2πλ² (Lemma 2). The band-limited model interpolates exactly up to T*.
- The zero γ_n (γ_n < T*) falls in the oversampling zone ⟹ it is resolved. The rate is given by the "room" T* − γ_n. **[GAP] the extremal de Branges residual.** The precise value of
R(λ,γ_n) = ‖residual band-limited projection‖ is the asymptotics of the canonical product
truncated to type L/2 evaluated at γ_n. Numerically R ~ e^{−c(T*−γ_n)} ~ e^{−cλ²}
(c≈11, measured). The precise proof = de Branges extremal theory / Beurling–Selberg at
critical density. **This is the candid [GAP] of the dominant term.** It is classical in
flavor, not elementary. **[!] Crucial:** this skeleton uses ONLY the density (zero count) and the sampling, NOT
the position (real part β) of the zeros. **The band term is unconditional.** --- ## 4. Limit λ: Euler correction — **[!] where the attempt REVEALS conditionality** The model uses primes ≤ λ². The tail is missing. The effect on the zero ρ̂_n:
``` |ρ̂_n(λ,∞) − γ_n|_Euler ≈ |R_λ(½+iγ_n)| / |Ξ'(γ_n)|, R_λ(s) = −ζ'/ζ(s) − Σ_{n≤λ²} Λ(n) n^{−s}.
```
**[!] And here the proof runs into the unexpected.** By the explicit formula
(weil-remainder-attack §2):
``` R_λ(½+iγ_n) ~ Σ_ρ (λ²)^{ρ−½−iγ_n}/(ρ−s) = Σ_ρ (λ²)^{β−½} · (phase), β=Re ρ.
```
**The Euler correction at a fixed zero γ_n is governed by ALL the zeros ρ, via
(λ²)^{β−½}.** If all β=½ (RH), it is O(1) and the correction is small (consistent with the
measured floor <1e-19). BUT an off-line zero ρ₀ with β₀>½ contributes (λ²)^{β₀−½}, which GROWS. **⟹ The Euler term is NOT unconditional: it inherits the RH sensitivity of R_λ.** **Regime where it IS unconditional:** for Re s ≥ 1+ε the Euler series converges
absolutely, R_λ → 0 geometrically, **unconditionally**. But there are no zeros there. The tail on
the critical line (where the γ_n live) is conditional. --- ## 5. Candid verdict of the attempt at a complete proof When attempting to prove soft-E2 with maximum precision, the structure splits as follows: | Piece | Status | Conditional? |
|---|---|---|
| Limit N (full band, fixed λ) | **[P]** (Davis–Kahan + Plancherel–Pólya) | **No** |
| Band/horizon (dominant term ~e^{−cλ²}) | **[GAP]** de Branges extremal | **No** (only density/count) |
| Euler correction at γ_n | explicit | **[!] Yes** (R_λ ~ Σ_ρ (λ²)^{β−½}) |
| Euler at Re s ≥ 1+ε | **[P]** | No (but no zeros there) | **[!] Finding of the attempt:** the split "soft = unconditional / hard = RH" was
**almost** correct, but not entirely. To be precise:
- The **dominant skeleton** (limit N + band/horizon) **is unconditional** — it uses zero count (density), not position. Rate ~ e^{−cλ²}.
- The **Euler correction** on each zero **is RH-sensitive** (sub-dominant when RH holds, which is why the measured floor is <1e-19, but not unconditionally bounded). **What this means.** Soft-E2 is proved UNCONDITIONALLY **to dominant order**
(band/horizon, modulo the de Branges extremal), but convergence to the EXACT zero
includes an Euler correction that inherits the conditionality of R_λ. The boundary
soft/hard is finer than we thought: ``` SKELETON (density/Nyquist): unconditional ← genuine soft-E2 CORRECTION (Euler at γ_n): RH-sensitive ← where the hard part sneaks in
``` This **confirms and refines** your collaborator's reframing: World B (convergence)
has a pure-approximation skeleton (density/Nyquist) that does NOT touch zero position
— that is real and unconditional. But the *last correction* (Euler at the zero) reintroduces
the zeros. **The good news:** the unconditional skeleton exists and is robust; **the
candid part:** it is not convergence to the exact zero, it is convergence to "the zero modulo the
Euler tail". --- ## 6. What remains, precisely 1. **[GAP] closable (classical):** the de Branges extremal residual for the band term. Would close the unconditional skeleton ~e^{−cλ²} with constant.
2. **[!] RH-sensitive:** the Euler correction R_λ(½+iγ_n). Bounding it unconditionally with the necessary strength = controlling (λ²)^{β−½} = zero-free regions → RH-optimal.
3. **Clean question remaining (for the hard upgrade, §3 of eslabon2-soft-theorem):** does the unconditional skeleton (band, density) suffice to force strip-uniform convergence, leaving the Euler correction as a controllable perturbation? If the band dominates the Euler correction ((λ²)^{β−½}) strongly enough (e^{−cλ²}), there might be an argument where the unconditional skeleton "wins" before the correction matters. **That is the next calculation: compare e^{−cλ²} (band) vs (λ²)^{Θ−½} (Euler/position) and see if the band dominates for all Θ<1.**
