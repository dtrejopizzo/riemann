# IV.1 — Identification of the limit operator `Â_∞` (spectrum `n²`) > **NOTICE (candid closure): the "Dirichlet Laplacian" identification below
> is REFUTED by the eigenvectors.** Test E12 (mpmath, λ=7, dim 29) gives: raw
> eigenvectors with 15–18 sign changes, de-modulated envelope `v_k·(−1)^j` with **10–13 nodes**
> (not 0,1,2,…), and overlap with the Dirichlet modes `sin((k+1)π·)` of **only 0.04–0.35**.
> Conclusion: **`Â_∞` shares the spectrum `{n²}` of `−d²/dx²` but is NOT that operator**
> (same spectrum, different eigenvectors). The IV.1a–c analysis below (symbol `W_λ`,
> KMS/Parter/Widom) **also fails to close** because the Weil symbol `W_λ` is INDEFINITE (it
> takes very negative values: `2θ'(0)≈−5.4`, arithmetic part `−2ΣΛ(n)/√n` large negative),
> while `QW` is PSD with `ε_0>0` — so `QW` **is not** the finite section of
> multiplication by `W_λ`. Both pictures (symbol and Dirichlet) were wrong.
> **IV.1 remains OPEN.** See "Candid status" at the end. --- ## (Refuted attempt, kept for record) The limit operator as the Dirichlet Laplacian Identification of the renormalized limit operator from the structure of the Weil form.
Result: the spectrum `n²` (measured in E11) **is not a mystery** — it is the small-eigenvalue
spectrum of a finite-section (Toeplitz) operator near a non-degenerate minimum
of its symbol, via the classical Kac–Murdock–Szegő / Parter–Widom theory. Markers: **[P]** proved · **[P\*]** modulo standard classical result · **[GAP]** core. --- ## IV.1a — `A_λ` is a finite section with Weil symbol `W_λ` — [P] By the Weil explicit formula, the quadratic form on band-limited functions
`g=ξ̂∈PW_Ω`, `Ω=logλ`, is
``` A_λ(g,g) = ⟨ξ, QW ξ⟩ = (1/2π) ∫_{-Ω}^{Ω} |ĝ(t)|² W_λ(t) dt, W_λ(t) = 2θ'(t) − 2 Re Σ_{n≤λ²} Λ(n) n^{-1/2-it},
```
where `θ'(t)=½ Re ψ(¼+it/2) − ½logπ` is the archimedean density. In the sampling basis
`{sinc_k}` (nodes `d_k`, transform `ê_k(t)=e^{-id_k t}1_{[-Ω,Ω]}`),
``` QW[m,n] = (1/2π)∫_{-Ω}^{Ω} e^{-i(d_m-d_n)t} W_λ(t) dt + (window corrections),
```
i.e. `QW` is the **finite-section matrix** (Toeplitz, modulo the Fejér window
`(1−y/L)` and the interval `[0,L]` which make it asymptotically Toeplitz-Loewner as
`L→∞`) of the **Weil symbol `W_λ`**. **[P]** (it is the explicit formula; the
Loewner→Toeplitz correction vanishes at rate `1/L=1/(2logλ)`). --- ## IV.1b — `W_λ` has a non-degenerate minimum, value `≈ ε_0 ≈ 0`, curvature `c_λ>0` — [P] `W_λ` is even and smooth on `(-Ω,Ω)`. The archimedean part `2θ'(t)`:
``` 2θ'(t) = Re ψ(¼ + it/2) − logπ,
```
is **even, with minimum at `t=0`** (`ψ(¼+it/2)` grows with `|t|`; `θ'(0)=½ Re ψ(¼)−½logπ` is
the background value) and **curvature**-controlled by `θ''’`: `(2θ')''(0) = −¼ψ''(¼) > 0`
(`ψ''(¼)<0`), non-degenerate. The arithmetic part `−2Re Σ Λ(n)n^{-½-it}` is a
bounded oscillating perturbation; near the bottom of the archimedean well it smooths it
but does not erase the non-degenerate minimum (this is the content of the *frame/Landau–Beurling
deficit*: `W_λ(t_0) = ε_0 = O(C_0/λ²) ≈ 0`, the positivity deficit). Thus
``` W_λ(t) = ε_0 + c_λ (t−t_0)² + O((t−t_0)³), c_λ = ½(2θ')''(t_0) + (arith) > 0.
```
**[P]** existence of a non-degenerate minimum (convex archimedean part + bounded
perturbation); **[minor GAP]** that the arithmetic perturbation does not create a lower
minimum at `t_0≠0` — equivalent to local Weil positivity near the bottom, expected but to be
verified. --- ## IV.1c — small eigenvalues of the finite section `∝ n²` (Dirichlet) — [P\*] **Theorem (Kac–Murdock–Szegő / Parter 1961 / Widom).** Let `T_N` be the `N×N` finite-section
matrix of a Hermitian symbol `W` attaining a **non-degenerate minimum**
`W_min` at an interior point, `W(t)=W_min + c(t−t_0)² + o(·)`. Then the small
eigenvalues of `T_N` above `W_min` satisfy, for fixed `j=1,2,3,…` and `N→∞`,
``` λ_j(T_N) − W_min ~ c · (π j / (N+1))² · κ,
```
with `κ` a scale constant. **They are the eigenvalues of the discrete Dirichlet Laplacian.** *Structural reason.* The symbol of the discrete Laplacian `2−2cosθ = θ²+O(θ⁴)` is the
prototype of a quadratic minimum; its Toeplitz matrix **is** exactly the Dirichlet
Laplacian with eigenvalues `2−2cos(πj/(N+1)) ~ (πj/(N+1))²`. Every symbol with a
non-degenerate quadratic minimum has the same low-eigenvalue asymptotics (universality of
the minimum). **[P\*]** (Böttcher–Grudsky–Spitkovsky, *Spectral properties of banded Toeplitz
matrices*, SIAM 2005; KMS 1953; Parter 1961). **Application.** With `W_min = ε_0 ≈ 0` (IV.1b), `ε_j ~ ε_0 + c_λ κ (π j/(N+1))²`. In the
renormalized regime, since `ε_0 ≈ 0` sits below the first box mode, the
eigenvalues are ordered as `ε_n ∝ n²` (`n=1,2,3,…`, no zero mode — **Dirichlet
condition** at the band edge `t=±Ω` / at the finite size `N`). Hence
``` ε_k / ε_0 → (k+1)² = n² (k=0,1,2,…↔ n=1,2,3,…).
``` --- ## IV.1 — Conclusion > **`Â_∞`** (limit of the renormalized Weil operator) **is the Dirichlet Laplacian**
> `−d²/dt²` on the effective interval `[−Ω,Ω]`, with spectrum `{n²}_{n≥1}`. **[P\*]** This **turns Conjecture IV (Conj 4.12 of the paper) into a theorem** modulo two
classical/minor inputs:
1. **[P\*]** the Toeplitz minimum asymptotic (KMS/Parter/Widom) — classical.
2. **[minor GAP IV.1b]** that the minimum of `W_λ` is interior, non-degenerate, and not shifted by the arithmetic perturbation — local Weil positivity, numerically verified (E11: `n²` improves with `λ`), to be closed analytically with the convexity of `θ'` + a bound on the arithmetic oscillation `‖Σ Λ(n)n^{-½-it}‖_{C²}` in a neighborhood of the background. **Minimal core of IV.1:** the only non-classical point is IV.1b (the minimum is not
shifted), and it is **the same Weil positivity localized at the bottom of the well** — an
echo of §V, but *local* (a single point `t_0`), much weaker than global §V. The `n²`
structure itself is robust and classical (2nd order + finite section = Dirichlet). ### Sub-division for the future (extreme core)
| IV.1 sub-piece | Status |
|---|---|
| IV.1a symbol `W_λ` (explicit formula) | **[P]** |
| IV.1b non-degenerate, non-shifted minimum | **[P]** existence · **[minor GAP]** non-shift |
| IV.1c low spectrum `∝ n²` (KMS/Parter/Widom) | **[P\*]** classical |
| **IV.1 ⟹ `Â_∞`=Dirichlet, spectrum `n²`** | **[P\*]** (modulo IV.1b) | Remaining: IV.2 (rigidity `n² ⟹ ξ̂_∞=Ξ`) and §V (global positivity under `/ε_0`). --- ## Candid status of IV.1 (after the refutation) **Refuted (two false identifications):**
1. `Â_∞ = −d²/dx²` Dirichlet — NO (eigenvectors do not match, overlap <0.35, nodes 10–13).
2. `QW =` finite section of multiplication by symbol `W_λ` — NO (`W_λ` indefinite, `QW` PSD). **Solid (not refuted):**
- `ε_k/ε_0 → (k+1)² = n²`, **robustly measured and improving with λ** (E11). It is the most stable datum in the whole program.
- Simple ground level (H1, Perron–Frobenius). *Caveat:* the "positive" eigenvector of H1 lives in a transformed representation; the raw `v_0` has sign changes (carrier). The relationship between the two representations (which similarity takes `QW` to its Perron–Frobenius form) **is not identified** — and is part of the same mystery of the operator. **What the chain NEEDS from IV.1 (minimal):** only the **relative gap `γ>0`**
(`ε_1/ε_0 → 1+γ`), the hypothesis of Theorem III (relative stability). If `n²` is accepted,
then `γ=3` follows automatically. But `n²` is **measured, not proved**. **Minimal open core of IV.1 (sub-divided to the extreme):**
> **IV.1★ — Prove `ε_1(λ)/ε_0(λ) ≥ 1+γ > 1` uniformly in λ** (relative gap bounded
> away from 1). Strong equivalent: identify the operator `Â_∞` (whose spectrum `n²` would give
> `γ=3`). Simplicity (H1) gives `ε_1>ε_0` but **not** the uniform bound on the ratio. **Verdict:** IV.1 **is not closed** by operator identification (both refuted). Its
content reduces to IV.1★ (uniform relative gap), which **remains open** — empirically
solid (`ε_1/ε_0→4`, stable, improving with λ) but not proved. Theorem III remains
**conditional on IV.1★**. **Lesson (anti-self-deception):** we record the refutation instead of hiding it. The `n²` is
real but its operator is not the naive one; forcing "Dirichlet" would have been a gap that
returns. Better a named, candid gap (IV.1★) than a false proposition.
