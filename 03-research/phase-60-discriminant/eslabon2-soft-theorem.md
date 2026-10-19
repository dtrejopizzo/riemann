# Soft link 2 as an approximation theorem + the exact boundary with the hard part Reframing World A (positivity) / World B (convergence). This document formalizes
the object of World B that does NOT arise from RH/Weil/de Branges: the
band + Euler-floor decomposition. And it isolates, in approximation language, the only upgrade that is hard. **[P]** proved · **[N]** numerical · **[O]** open · **[GAP]** step to prove. --- ## 0. The two worlds (agreed map) | | World A — Positivity | World B — Convergence |
|---|---|---|
| objects | A_λ, ε₀, 𝓛, (k+1)² | ξ̂_{λ,N}, Ξ, Euler truncation, T* |
| question | A_∞ ⪰ 0 ? | ξ̂_{λ,N} → Ξ ? |
| tradition | Weil / de Branges / Hilbert–Pólya | approximation theory |
| nature of the error | minimum eigenvalue | band e^{−cλ²} + Euler floor | **Thesis:** World B has its own dynamics (band + Euler), which do NOT go through 𝓛.
Previous phases attacked B with objects from A. Here we treat B in its own variables. --- ## 1. Target theorem (soft-E2): LOCAL convergence on the real axis **Statement (target).** Fix n, let ρ̂_n(λ,N) be the n-th real zero of ξ̂_{λ,N} and
γ_n the n-th zero of Ξ. There exists λ_n such that for λ ≥ λ_n (with N → ∞ taken),
``` | ρ̂_n(λ) − γ_n | ≤ C_band · e^{−c (T*(λ) − γ_n)} + C_Euler · 𝓔_λ(γ_n),
```
with:
- **T*(λ) ~ 2πλ²** the Nyquist horizon (Lemma 2, zero density = sampling density at T*);
- **𝓔_λ(γ_n)** the Euler truncation tail at primes ≤ λ², controlled by PNT. Both terms are **unconditional** and **do not mention the position of the off-line zeros**.
It is *local* convergence (each γ_n fixed, within the moving horizon). ### Status of the two terms **Band term [N→GAP]:** measured e^{−cλ²} (c≈11, λ=2.0–2.3, fixed primes {2,3}).
It is the band-limited approximation error: ξ̂_{λ,N} ∈ PW_{L/2} (type L/2=logλ), and approximating
γ_n (interior to the horizon) has an error exponential in the "room" T*−γ_n.
- **[GAP] Proof:** Beurling–Selberg / Plancherel–Pólya inequality for the interpolation residue at critical density. Classical tool; the constant c and uniformity are missing. Does not use off-line zeros (only density). **Euler term [N→GAP]:** measured < 1e-19 already with primes ≤13 (ultrafast). It is the
remainder of the truncated explicit formula, R_λ(½+iγ_n) (cf. weil-remainder-attack).
- **[!] Frank subtlety:** R_λ ~ Σ_ρ (λ²)^{ρ−s} IS sensitive to Re ρ. BUT for FIXED γ_n and within the horizon, the tail that matters is that of primes > λ², and its effect on the already-resolved zero is of PNT order (classical zero-free regions), not the position of the global γ's. RH sensitivity appears only in the UNIFORM regime (see §3), not in the local convergence of a fixed zero. **Reading:** soft-E2 = local convergence of each zero, governed by Nyquist (band)
+ PNT (Euler). Unconditional. It is the "quick win" that also **writes the boundary**. --- ## 2. Why soft-E2 does NOT give RH (and that's fine) Local convergence ρ̂_n(λ) → γ_n is on the **real axis**: it says that the n-th
real eigenvalue of the finite model converges to the n-th γ_n. **It does not establish that ρ_n is on
the line**, because γ_n is the height (imaginary part), which exists whether ρ_n is on or off the line. For RH, the convergence needs to **see the real part** β_n of ρ_n, which requires
convergence in a **COMPLEX neighborhood** of the axis (Hurwitz), not just on the real axis. --- ## 3. The exact boundary: LOCAL (soft) → UNIFORM-IN-STRIP (hard) Here is the heart of it, in approximation language (not positivity language): - ξ̂_{λ,N} is entire of **exponential type L/2 = log λ** (band-limited).
- By Paley–Wiener, an approximant of type log λ matches Ξ in a complex strip of width **~ 1/log λ → 0**. The strip **narrows** with λ.
- An off-line zero ρ₀ = ½+β₀+iγ₀ is at **fixed** depth δ₀ = β₀ from the real axis (in variable t). For ξ̂_{λ,N} to "capture" it (and for Hurwitz to force β₀=0), the strip of width 1/logλ would have to reach depth δ₀ — which is fixed. **It doesn't.** ### The computation that ALMOST closes it (and why it fails) Error on the real axis ~ e^{−cλ²} (band, super-fast). Continuation to depth δ
amplifies by the type: factor ~ e^{δ·logλ} = λ^δ. Product:
``` error at depth δ ~ λ^δ · e^{−cλ²} → 0 (∀ fixed δ, λ→∞).
```
**If this were the real sup-norm, it would give uniform convergence in a fixed strip ⟹ RH.** **Why it fails [!]:** e^{−cλ²} is the error of the ZEROS (local), not the **sup-norm**
|ξ̂_{λ,N} − Ξ| on a real interval. ξ̂_{λ,N} is band-limited and Ξ is not; their difference in
sup-norm is NOT e^{−cλ²} uniformly — only each zero converges this way, locally. Without
a uniform sup-norm bound there is nothing to amplify off-axis. ### ⟹ The hard question, in approximation variables ``` Can the LOCAL convergence of the zeros (e^{−cλ²}, unconditional) be UPGRADED to UNIFORM convergence in sup-norm on a real interval, with enough type control for a strip of FIXED width?
``` - **If yes ⟹ RH** (Hurwitz + off-axis amplification).
- **It is a de Branges / Paley–Wiener / Beurling question**, NOT a Weil-positivity question.
- **We do not know whether it is RH-by-necessity or RH-by-formulation.** This is the precise boundary your collaborator asked to have written. --- ## 4. What this changes (frankly) **We have not escaped RH-hardness yet.** But we **relocate the wall** from
"positivity / zero position" to a **clean approximation-theory question**: > upgrade from local convergence (unconditional) to uniform-in-fixed-strip, with type log λ. This is a **new object from World B**, distinct from A_∞⪰0. The candidate tools
are approximation tools (Beurling–Selberg, Plancherel–Pólya, model spaces, de Branges
without positivity), not positivity tools. **For the first time, the hard link 2 is written
without naming Weil or the zeros**: it is "type uniformity in band-limited". ## 5. Plan 1. **[GAP] Prove soft-E2** (Theorem §1): local band+Euler bound, unconditional. Formalizes the boundary. Tools: Beurling–Selberg (band), PNT (Euler).
2. **[O] Attack the upgrade §3** as an approximation problem: does the real sup-norm converge?, with what effective type? This is where necessity vs. formulation is decided. **What's new:** we stop asking "A_∞⪰0?" and start asking "type uniformity in
band-limited convergence?". Perhaps the same wall — but **a different face, different
tools**, and the first one that did not arise from RH/Weil/de Branges-positivity.
