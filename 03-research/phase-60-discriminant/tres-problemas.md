# Three problems about a family of quadratic forms ## Common framework (valid for all three) For `λ>1` let `L=2logλ`, `Ω=logλ`. On the space `E_λ` of entire functions of
exponential type `Ω` with spectral support in `[−L/2,L/2]`, we define the real symmetric
quadratic form
$$A_\lambda(f,f)=\int a(t)\,|\hat f(t)|^2\,dt,\qquad a(t)=\tilde\Omega(t)-D_\lambda(t),$$
with archimedean symbol `Ω̃(t)=−logπ+Re ψ_Γ(1/4+it/2)` (`ψ_Γ` digamma) and "coupling"
symbol `D_λ(t)=Σ_{n≤λ²}Λ(n)n^{−1/2}cos(t log n)` (`Λ` von Mangoldt). Equivalently
`A_λ` is the compression to `[0,L]` of convolution by `D_ζ(|x−y|)`. Established facts (at finite `λ`): `A_λ` is real symmetric, lower-bounded, with discrete
spectrum `ε_0(λ)≤ε_1(λ)≤⋯`; the ground state `ε_0` is **simple, isolated and even** (Perron–Frobenius via
the positivity of the archimedean semigroup and `Λ(n)≥0`). Notation: `γ(λ):=(ε_1(λ)−ε_0(λ))/|ε_0(λ)|` (relative gap); `Â_λ:=A_λ/|ε_0(λ)|` (family
renormalized by the absolute value of the ground state). --- ## PROBLEM III — Relative stability and uniform gap **Statement.**
- **(III-a)** Prove that `Â_λ` converges, in the sense of strong resolvent convergence, to a limit operator `𝓛_∞` as `λ→∞`.
- **(III-b)** Prove `liminf_{λ→∞} γ(λ) > 0` (the relative gap does not collapse). **What must be resolved to open it.** A **uniform tightness bound** on the family
`{Â_λ}`: that the spectral mass of the ground state escapes neither to `0` nor to `∞` under renormalization. In
terms of forms, a uniform equivalence `c_1 𝓔_D ≤ Â_λ ≤ c_2 𝓔_D` with the Dirichlet
form `𝓔_D(f)=∫|f'|²` and `0<c_1≤c_2<∞` independent of `λ`. The upper bound is direct
(the archimedean symbol dominates the derivative); the crux is the **uniform lower bound**. **What it opens.** III is the **gateway to IV.1**: without existence and stability of the limit
(III-a) and without a uniform gap (III-b), the identification in IV.1 is meaningless. Once the
tightness estimate is resolved, IV.1 becomes posable. **Nature.** Standard operator analysis (Prokhorov + strong resolvent convergence,
Reed–Simon VIII.21/24, once tightness is established). The sign of `ε_0` does not come into play. --- ## PROBLEM IV.1 — Identification of the limit operator **Statement.** Prove that the limit operator `𝓛_∞` from (III-a) is
$$\mathcal L_\infty=-c\,\frac{d^2}{dx^2}\quad\text{on a finite interval with Dirichlet
conditions},\qquad c=-\tfrac18\,\psi_\Gamma''(1/4),$$
with eigenvalues proportional to `(k+1)²` (`k=0,1,2,…`) and eigenfunctions of alternating parity. **What must be resolved to open it.** The **quantitative edge asymptotics** (Landau–Widom)
of the truncated compression: showing that the low spectrum of `Â_λ` converges to that of the
Dirichlet box `(k+1)²`. Ingredients already available: (a) the kinetic coefficient
`c=−ψ_Γ''(1/4)/8`, derived from the low-order expansion of the archimedean symbol (Lévy);
(b) the Dirichlet mechanism from the decay of the coupling terms (length `∼2logλ`,
greater than the edge-layer width `∼1/logλ`), which act as a hard wall; (c) numerical
verification `ε_k/ε_0→(k+1)²` with no offset, alternating parity. What remains is to convert (a)–(c) into the
uniform convergence bound. **What it opens.** IV.1 **implies III**: if the limit is `𝓛_∞`, then (III-a) exists and its relative
gap is `(2²−1²)/1²=3>0`, so `γ(λ)→3` and `liminf γ>0` (III-b). That is, **a single
tightness estimate resolves III and IV.1 at once**, with IV.1 being the finer version. **Dependency.** Requires III (the existence that IV.1 refines). It neither requires nor contributes anything about
the sign of `ε_0`. --- ## PROBLEM (P) — Positivity **Statement.** Prove that `ε_0(λ) ≥ 0` for all `λ>1`. **What must be resolved to open it.** A **lower bound on the minimum of the form**
`A_λ(f,f)` that controls its **sign**: equivalently, that the coupling part `D_λ` does not
dominate the archimedean part `Ω̃` over the band. The precise obstruction is given by the
**marginality theorem**: the negative well of `a(t)` has half-width
`δ_λ=(2|a(0)|/a''(0))^{1/2}=1/(√2 logλ)` and the resolution band is `r_λ=π/logλ`, with ratio
`2δ_λ/r_λ=√2/π≈0.45`; both depend **only on the magnitudes** `{|Λ(n)|}`. Therefore no
functional of those magnitudes decides the sign (there exist systems of equal magnitude with `ε_0<0`).
The sign resides in the **phase** of the coupling terms. Resolving (P) requires a
**phase-sensitive** estimate, not a magnitude one. **What it opens.** It is the terminal problem of the chain; nothing else depends on it within this
structure. **Dependency.** **Independent of III and IV.1.** These concern `Â_λ=A_λ/|ε_0|`, which is
blind to the sign of `ε_0` by construction. Resolving III and IV.1 **does not advance** (P), and (P)
needs neither of the two. The only way IV.1 would touch (P) would be by giving the asymptotics
of `ε_0` **with sign** (not `|ε_0|`), but that strengthening is already (P). --- ## Summary of the structure ``` ┌─ tightness bound / Landau–Widom ─┐ │ │ ▼ ▼ PROBLEM III ───────────────────────▶ PROBLEM IV.1 (existence + uniform gap) (identification of 𝓛_∞) gateway refinement; IV.1 ⟹ III PROBLEM (P) ── independent closure ── (sign of ε_0) is not opened by III nor IV.1; requires a phase estimate
``` - **III and IV.1:** coupled. A single estimate (tightness/Landau–Widom) opens both; IV.1 ⟹ III. Nature: standard technical analysis.
- **(P):** isolated. It is the deep, independent problem; no progress on III/IV.1 brings it closer. Requires control of **phase**, not magnitude (marginality theorem).
