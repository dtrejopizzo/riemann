# E2.kernel — all the pure mathematics possible Attack on the single remaining RH-hard knot, via the approximation-style
reframing (-style): not attacking `R_λ` nor `δV` (proved RH-equivalent, `(λ²)^{Θ−½}`),
but the difference with the **canonical Fourier truncation** of Ξ. Markers: **[P]** proved (pure mathematics) · **[GAP]** modulo a standard classical
result · **[!]** finding/frontier. --- ## 0. Object and goal `ξ̂_{λ,N}` = band-limited entire function of type `T = L/2 = log λ` (PW_{T}) whose
real zeros are the `ρ̂_n`, **real-rooted by Link 1** (Perron–Frobenius, Λ(n)≥0,
**proved**). `Ξ(z)` = Riemann xi function (entire, order 1, even, real on ℝ),
real-rooted `⟺` RH. Via Hurwitz, RH follows if `ξ̂_{λ,N} → Ξ` **uniformly on a complex strip of
fixed width** containing the zeros. All zeros of Ξ live in `|Im z| ≤ ½`
(because `ρ = ½+it` with `Re ρ ∈ (0,1)` ⟹ `Im z = ½−Re ρ ∈ (−½,½)`). Goal: convergence
uniform in `|Im z| ≤ ½`. --- ## 1. Canonical Fourier truncation `Ξ_T` — Step 1 [P] ### 1.1 Riemann's representation Classical (Riemann 1859 / Pólya):
``` Ξ(z) = ∫_{-∞}^{∞} Φ(u) e^{izu} du, Φ(u) = Σ_{n≥1} (2π²n⁴ e^{9u/2} − 3πn² e^{5u/2}) · exp(−πn² e^{2u}).
```
`Φ` is **even** (`Φ(−u)=Φ(u)`, content of the functional equation), smooth, and
``` Φ(u) ≤ C · e^{9u/2} · exp(−π e^{2u}) (u ≥ 0) (★)
```
with `C` absolute. (For `u≥0`, `Σ_n n⁴ e^{−πn²e^{2u}} ≤ e^{−πe^{2u}} Σ_n n⁴ e^{−π(n²−1)e^{2u}} ≤ C e^{−πe^{2u}}`.)
**DOUBLE-exponential decay.** That is all that is used. ### 1.2 Definition and type ``` Ξ_T(z):= ∫_{-T}^{T} Φ(u) e^{izu} du.
```
`Ξ_T` is entire of **exponential type `T`** (Paley–Wiener: support of the transform
in `[−T,T]`), with `|Ξ_T(x+iy)| ≤ (∫Φ) e^{T|y|}`. **[P]** ### 1.3 Theorem 1 (strip-uniform convergence, unconditional) > For all `δ ≥ 0` and `T = log λ`:
> ```
> sup_{|Im z| ≤ δ} |Ξ(z) − Ξ_T(z)| ≤ C_δ · λ^{5/2+δ} · e^{−π λ²}.
> ``` **Proof [P].** By evenness,
``` |Ξ(z) − Ξ_T(z)| = |∫_{|u|>T} Φ(u) e^{izu} du| ≤ 2∫_T^∞ Φ(u) e^{δu} du.
```
By (★),
``` 2∫_T^∞ Φ(u) e^{δu} du ≤ 2C ∫_T^∞ e^{(9/2+δ)u} e^{−π e^{2u}} du.
```
Substituting `v = e^{2u}` (`du = dv/2v`):
``` = C ∫_{e^{2T}}^∞ v^{5/4+δ/2} e^{−πv} dv = C · Γ(7/4+δ/2, π e^{2T}).
```
For the incomplete Gamma with large argument `X=e^{2T}`:
`∫_X^∞ v^a e^{−πv} dv ≤ 2 X^a e^{−πX}/π` (`X` large). With `a=5/4+δ/2`, `X=e^{2T}=λ²`:
``` ≤ C' · (λ²)^{5/4+δ/2} · e^{−πλ²} = C' · λ^{5/2+δ} · e^{−πλ²}. ∎
``` **[!] Strong corollary.** The prefactor `λ^{5/2+δ}` is **polynomial**; it is crushed
by `e^{−πλ²}`. The bound tends to 0 even if `δ = δ(λ) → ∞`, as long as
`(5/2+δ)log λ < π λ²`, i.e. **`δ(λ) = o(λ²/log λ)`**. The Fourier truncation
converges to Ξ uniformly on strips whose width **grows** up to `~ λ²/log λ`.
In particular, trivially, on `|Im z| ≤ ½`. ### 1.4 What Step 1 establishes (and what it does NOT) **Establishes [P]:** there exists a band-limited approximant of type `log λ`, canonical and
explicit, that converges to Ξ **uniformly on the strip containing ALL the zeros**, at
super-exponential rate `e^{−πλ²}`, **unconditionally and without mentioning the position of any
zero** (only the double-exponential `Φ`). **Refutes** my previous objection (eslabon2-soft-theorem §3): "type `log λ` ⟹ strip
`~1/log λ → 0`". **False for the Fourier truncation.** The Paley–Wiener-L² strip
does narrow, but the difference `Ξ−Ξ_T` is controlled by the **tail of `Φ`**, which is
double-exponential and wins over any fixed strip. **The Fourier truncation of Ξ is
not the obstacle.** (Phrasing adjusted per referee: we do not say "band-limiting is not the
obstacle" — that still depends on Step 2.) **Does NOT establish:** that `Ξ_T` is real-rooted (it is not, it is just any truncation).
Hence `Ξ_T` alone does not give RH. Real-rootedness is contributed by the CCM object `ξ̂`. → Step 2. --- ## 2. Decomposition and localization — Step 2 ### 2.1 The clean decomposition ``` ξ̂_{λ,N} − Ξ = (ξ̂_{λ,N} − Ξ_T) + (Ξ_T − Ξ). └──── δ̂ ────┘ └─ Theorem 1: ≤ λ³ e^{−πλ²} on |Im z|≤½ ─┘
```
The second term is **fully controlled** (Theorem 1, `δ=½`). **All the
remaining RH content lies in `δ̂:= ξ̂_{λ,N} − Ξ_T`**, which is entire of type `≤ T = log λ`
(difference of two functions of type `T`). **[P]** ### 2.2 Off-axis continuation lemma (PL + harmonic measure) [P] > **Lemma 2.** Let `F` be entire of exponential type `τ`, with `|F(x)| ≤ Γ` for all `x∈ℝ`
> and `|F(x)| ≤ ε` for `|x| ≤ R`. Then for `|x₀| ≤ R/2`, `0 < y₀ ≤ δ`:
> ```
> |F(x₀+iy₀)| ≤ e^{τ y₀} · ε^{ω} · Γ^{1−ω}, ω = ω_{[−R,R]}(x₀+iy₀),
> ```
> with `ω` the harmonic measure of the segment `[−R,R]` seen from `x₀+iy₀` in the upper
> half-plane. For `y₀ ≪ R`: `1−ω ≤ (2/π)(y₀/R)`. **Proof [P].** In `H={Im z>0}` set `w(z)=log|F(z)| − τ·Im z`. `log|F|` is
subharmonic, `τ Im z` harmonic ⟹ `w` is subharmonic in `H`. On the boundary `ℝ`:
`w(x)=log|F(x)| ≤ log Γ`, and `≤ log ε` on `[−R,R]`. `F` of type `τ` and bounded on `ℝ`
satisfies `|F(z)| ≤ Γ e^{τ|Im z|}` (Boas, *Entire Functions*, Thm 6.2.4), so `w` is
bounded above on `H` and Phragmén–Lindelöf applies: `w` lies below its
harmonic majorant of the boundary data,
``` w(z) ≤ ω_{[−R,R]}(z)·log ε + (1−ω_{[−R,R]}(z))·log Γ.
```
Exponentiating and restoring `τ y₀`: `|F(z)| ≤ e^{τ y₀} ε^{ω} Γ^{1−ω}`. The bound for the
harmonic measure of the segment from `iy₀`: `ω_{[−R,R]}(iy₀) = (2/π)arctan(R/y₀) ≥ 1−(2/π)(y₀/R)`. ∎ ### 2.3 Application to `δ̂` `δ̂` is of type `τ = log λ`. Let
``` ε_loc(λ):= sup_{|t| ≤ T*} |ξ̂_{λ,N}(t) − Ξ(t)|, T* = 2π λ² (horizon, Lemma 2/CCM),
```
the approximation rate **on the real axis, over the horizon segment**. On the
segment, `|δ̂| ≤ ε_loc + |Ξ_T−Ξ| ≤ ε_loc + λ^{5/2}e^{−πλ²} ≈ ε_loc`. Globally on ℝ,
`Γ:= sup_ℝ|δ̂| = poly(λ)` (both band-limited bounded; `Ξ` decays exponentially on ℝ via
the Euler Γ factor). Apply Lemma 2 with `R=T*~λ²`, `δ=½`, `τ=log λ`, on `|x₀|≤T*/2`:
``` |δ̂(x₀+iy₀)| ≤ e^{(log λ)·½} · ε_loc^{ω} · Γ^{1−ω} ≤ λ^{1/2} · ε_loc · poly(λ)^{(2/π)(1/2)/(2πλ²)} ≈ λ^{1/2} · ε_loc. (∗)
```
**[!] The harmonic-measure correction `Γ^{1−ω}` is negligible** because the horizon
`R=T*~λ²` is enormous: `1−ω ~ 1/λ²`, so `Γ^{1−ω}=poly(λ)^{1/λ²}→1`. **The giant
horizon kills the far tail.** Only the type-`λ^{1/2}` amplification survives (from
`δ=½`, the depth of the zeros). ### 2.4 Theorem 2 (final reduction, unconditional) > ```
> sup_{|Im z| ≤ ½} |ξ̂_{λ,N}(z) − Ξ(z)| ≤ C · λ^{1/2} · ε_loc(λ) + C λ³ e^{−πλ²}.
> ```
> **Corollary (criterion for RH):** if
> ```
> ε_loc(λ) = sup_{|t|≤2πλ²} |ξ̂_{λ,N}(t) − Ξ(t)| = o(λ^{−1/2}) (λ→∞),
> ```
> then `ξ̂_{λ,N} → Ξ` uniformly on `|Im z| ≤ ½`, and by **Hurwitz** Ξ inherits the
> real-rootedness of `ξ̂_{λ,N}` (Link 1) ⟹ **RH**. **Proof [P].** Sum of §2.1 (Theorem 1, `δ=½`: `λ³e^{−πλ²}`) and (∗)
(`λ^{1/2}ε_loc`). If `ε_loc=o(λ^{−1/2})`, the sup over the strip `→0`; the zeros of `ξ̂`
(real, Link 1) converge to those of Ξ and, by Hurwitz on the open strip `|Im z|<½`,
no zero of Ξ can lie off the axis. ∎ --- ## 3. Where the wall ended up — exact frontier [!] All of RH (in this program) is now in **a single measurable real number**:
``` ε_loc(λ) = sup-norm of (ξ̂_{λ,N} − Ξ) over the real segment [−2πλ², 2πλ²]. Is it o(λ^{−1/2})?
``` This is **much finer** than `(λ²)^{Θ−½}`. Honest analysis of whether it is RH-equivalent or
weaker: - **In favor of it closing (non-circular):** `ε_loc` is a **band-limited interpolation residue at critical density** (Beurling–Selberg/Plancherel–Pólya). The counting matches: Ξ has `~N(T*)~(T*/2π)log T* ~ λ²·2log λ` zeros below the horizon; `ξ̂` of type `log λ` has `~(log λ/π)·2T* ~ (2/π)λ²log λ` real degrees of freedom — **comparable** (this IS the horizon lemma). There are just barely enough DOF to interpolate. The pointwise measured rate was `e^{−cλ²}` (c≈11) — **if that rate holds in sup-norm over the WHOLE segment**, then `ε_loc ~ e^{−cλ²} ≪ λ^{−1/2}` and **RH follows**. The off-axis amplification factor `λ^{1/2}` is ridiculously small against `e^{−cλ²}`. - **The real risk (where the zeros re-enter):** `ε_loc` is a **sup over an interval that GROWS** like `λ²`. The band-limited approximation **degrades near the edge of the horizon** `|t|~T*`, where the interpolation residue depends on the actual spacing of the nodes `= the γ_n`. The worst case over the segment could be `O(1)`, not `e^{−cλ²}`. **There, and only there, can the information about the zeros re-enter.** But note: what matters near the edge is the **regularity of the spacing** of the γ_n (Riemann–von Mangoldt, density — unconditional), not their **real part** (position). Plausibly **weaker than full RH**. That is the bet, now sharpened. ### The precise mathematical target (replaces the diffuse wall)
``` ¿ sup_{|t|≤2πλ²} |ξ̂_{λ,N}(t) − Ξ(t)| = o(λ^{−1/2}) ?
```
An object of **pure approximation theory** (interpolation residue at critical
density near the edge of the horizon), numerically measurable, without naming Weil or
positivity. It is the program's cleanest localization: from `(λ²)^{Θ−½}` (manifestly
RH-equivalent) to "sup-norm of the residue over the horizon vs `λ^{−1/2}`". --- ## 4. Status | Piece | Status |
|---|---|
| **Theorem 1** — `Ξ_T→Ξ` strip-uniform `λ^{5/2+δ}e^{−πλ²}` | **[P] proved, unconditional, no zeros** |
| **Lemma 2** — off-axis continuation PL + harmonic measure | **[P] (modulo Boas Thm 6.2.4, classical)** |
| **Theorem 2** — reduction: RH ⟸ `ε_loc=o(λ^{−1/2})` | **[P] proved** |
| The horizon `λ²` kills the far tail (`Γ^{1−ω}→1`) | **[P]** |
| `ξ̂` real-rooted (Link 1) | **[P] (prior)** |
| **`ε_loc(λ) = o(λ^{−1/2})`** — the target | **[GAP] — sole knot; measurable** | **Conclusion.** All the pure mathematics possible was done without touching the knot: Step 1 is
a **clean, unconditional theorem**, and the continuation machinery reduces RH to a
**single sup-norm bound over the horizon**, `ε_loc = o(λ^{−1/2})`. It does not prove RH —
but it transforms the diffuse wall `(λ²)^{Θ−½}` into a precise and measurable
approximation target. Natural next step (numerical): measure `ε_loc(λ)` as the sup over `[−T*,T*]`
(not at loose points/zeros) and see its law in `λ`, in particular near the edge `|t|~T*`.
