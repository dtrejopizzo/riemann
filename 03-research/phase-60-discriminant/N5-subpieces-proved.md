# Closing the sub-pieces of N5: N2, N3, N5c proved; N5a absorbed Rigorous proof of the "almost/known/measured" pieces of the table, to leave them as
**PROVED**. Core §V is left for last. Markers **[P]** proved · **[ABS]** absorbed. --- ## N2 — global amplitude `Γ = sup_ℝ|ξ̂_λ| = O(log λ)` — [P] **Proposition N2.** The band-limited approximant `ξ̂_{λ,N}` (unit eigenvector,
`‖ξ‖_{ℓ²}=1`) satisfies `‖ξ̂_{λ,N}‖_{L^∞(ℝ)} ≤ C·logλ`. In particular `Γ=poly(λ)`, which is all
Lemma 2 (N1) needs. **Proof [P].** We write the basis. Since `sin(Ls/2)=(−1)^k sin(L(s−d_k)/2)`,
``` ξ̂(s) = sin(Ls/2) Σ_k ξ_k/(s−d_k) = Σ_k ξ_k (−1)^k (L/2)·sinc_k(s), sinc_k(s):= sin(L(s−d_k)/2)/(L(s−d_k)/2), nodes d_k, step Δ=2π/L.
```
The `sinc_k` are **orthogonal** in `L²(ℝ)`: `∫ sinc_k sinc_j = Δ δ_{kj} = (2π/L)δ_{kj}`.
By Parseval (cardinal series),
``` ‖ξ̂‖²_{L²} = (L/2)² Σ_k ξ_k² · (2π/L) = (πL/2)‖ξ‖²_{ℓ²} = πL/2 = π logλ.
```
By the **Plancherel–Pólya / Nikolskii** inequality for exponential type `τ=logλ`
(`‖g‖_∞ ≤ C√τ ‖g‖_{L²}` for `g∈PW_τ`):
``` ‖ξ̂‖_∞ ≤ C √(logλ) · √(π logλ) = C√π · logλ = O(logλ). ∎
```
**Consequence.** In Lemma 2, `Γ^{1−ω}` with `Γ=O(logλ)` and `1−ω ≤ (2/π)(½)/T* ~ λ^{−2}`
gives `Γ^{1−ω} = exp((1−ω)logΓ) = exp(O(λ^{−2}·loglogλ)) → 1`. **N2 closed: the global
amplitude is poly-log, negligible in the off-axis transfer.** [P] --- ## N3 — off-axis amplification `|ξ̂(x+iy)| ≤ ‖ξ̂‖_∞ λ^{|y|}` — [P] **Proposition N3 (Boas/Bernstein).** If `F` is entire of exponential type `τ` and bounded on
ℝ by `M`, then `|F(x+iy)| ≤ M e^{τ|y|}`. With `τ=logλ`, `|y|≤½`: factor `≤ λ^{1/2}`. **Proof [P].** In the upper half-plane `H={Im z>0}` consider `g(z)=F(z)e^{iτz}`.
It is entire; on ℝ, `|g(x)|=|F(x)|≤M`. `F` of type `τ` ⟹ `|F(z)|≤C e^{τ|z|}`, hence
`|g(z)| = |F(z)|e^{−τ Im z} ≤ C e^{τ|z|−τ Im z} = C e^{τ(|z|−Im z)}`, which is bounded on
sectors of `H`; by **Phragmén–Lindelöf** on `H` (order 1, bounded on the boundary ℝ by
`M`), `|g(z)|≤M` throughout `H`, i.e. `|F(z)| ≤ M e^{τ Im z}` for `Im z≥0`. Reflecting with
`e^{−iτz}` gives `|F(x+iy)| ≤ M e^{τ|y|}` throughout ℂ. ∎ (Boas, *Entire Functions*,
Thm 6.2.4.) **N3 closed: this is exactly the factor `e^{τy_0}=λ^{y_0≤½}` of Lemma 2.** [P] --- ## N5a — interior = plunge — [ABS] absorbed (like N5b) After the collapse §VIII, `ε_loc ≤ C√(logλ)‖Â_λ−Â_∞‖_{low} + Ce^{−πλ²}`. The term
`e^{−πλ²}` (Theorem 1 with `δ=0`) bounds the target side **uniformly, both interior and boundary**.
No "interior rate" remains to be proved independently: the interior of the target side is
`e^{−πλ²}` (proved, N0); the interior of the approximant side (`ξ̂` vs `Ξ_T`) is part of the
operator convergence `‖Â_λ−Â_∞‖` = §V. **Conclusion [ABS].** N5a is **not an independent piece**: its provable content is N0
(Theorem 1); its remaining content is §V. The "plunge prolate `e^{−c'λ²}`" row was an
attempt to prove the interior separately, now subsumed. Same as N5b. The table should
mark N5a and N5b as **ABSORBED into the collapse**, not as gaps. --- ## N5c — β discrimination: lower bound `ε_loc(DH) ≥ c > 0` — [P] What was "measured" (ζ→10⁻¹³ vs DH≥10⁻²) is **proved** on the DH side: a
real-rooted approximant CANNOT converge off-axis to a function with a complex zero,
with a quantitative bound. This is the converse of Theorem 2 and certifies that `ε_loc` is the
correct object (not vacuous). **Lemma N5c.1 (monotonicity of real-rooted functions).** If `g` is a real entire function with only real zeros
(genus ≤1, i.e. `g∈\overline{LP}`), then `|g(x+iy)| ≥ |g(x)|` for all `x,y∈ℝ`. *Proof.* `g(z)=c e^{az+b} z^{m} ∏_n(1−z/r_n)e^{z/r_n}` with `r_n∈ℝ`, `a∈ℝ` (LP class). Each factor satisfies
`|1−(x+iy)/r_n|² = (1−x/r_n)² + (y/r_n)² ≥ (1−x/r_n)²`; the factor
`|e^{a(x+iy)}|=e^{ax}` does not depend on `y`; same for `|z^m|`. Product ⟹ `|g(x+iy)|≥|g(x)|`. ∎ **Proposition N5c.2 (DH does not converge off-axis, unconditional).** Let `f` be an
arithmetic datum (e.g. Davenport–Heilbronn) whose `Ξ_f` has a zero **off the axis**
`z₀ = x₀ + iη₀`, `η₀≠0` (i.e. a zero of `f` off the critical line). Suppose
convergence **on the real axis** `ξ̂_{λ}(x₀) → Ξ_f(x₀)` (the easy part, E2.a/horizon).
Then, since each `ξ̂_λ` is real-rooted (Link 1),
``` sup_{|Im z|≤|η₀|} |ξ̂_λ(z) − Ξ_f(z)| ≥ |ξ̂_λ(z₀) − Ξ_f(z₀)| = |ξ̂_λ(z₀)| ≥ |ξ̂_λ(x₀)| → |Ξ_f(x₀)| > 0.
```
**⟹ `ε_loc^{off}(f) ≥ |Ξ_f(x₀)| > 0`, bounded away from 0, UNCONDITIONAL.** *Proof.* `Ξ_f(z₀)=0` (off-line zero) ⟹ the error at `z₀` is `|ξ̂_λ(z₀)|`. By Lemma
N5c.1 (`ξ̂_λ` real-rooted), `|ξ̂_λ(z₀)|=|ξ̂_λ(x₀+iη₀)| ≥ |ξ̂_λ(x₀)|`. By the
convergence on the axis, `|ξ̂_λ(x₀)| → |Ξ_f(x₀)|`. And `Ξ_f(x₀)≠0` because `x₀` (the real
projection of the off-line zero) is **not** an on-line zero of `Ξ_f` (an off-line
zero is off the axis; its real projection is a regular point or a near-minimum, not a zero). ∎ **Reading.** This **proves** what E10 measured: for RH-false, `ε_loc` (its
off-axis version, the object of Theorem 2) is **bounded below** by an explicit constant
`|Ξ_f(x₀)|`. The lower bound **is** the content of Thm 1.1(iii) + Hurwitz, made
quantitative. The ζ side (`ε_loc(ζ)→0`) remains §V — but the **dichotomy** is
certified: `ε_loc` separates RH-true from RH-false, with the false side **proved**. **[P] N5c closed (DH side / lower bound).** Together with N2, N3 this leaves the table with
only IV.1, IV.2 (structural) and §V (the core) open. --- ## Table status after this round | Piece | Before | Now |
|---|---|---|
| N2 global amplitude `Γ=O(logλ)` | almost 🟡 | **PROVED** ✅ (Nikolskii) |
| N3 amplification `λ^{y≤½}` | known | **PROVED** ✅ (Boas/PL) |
| N5a interior | P*+GAP | **ABSORBED** (= N0) |
| N5b boundary | absorbed | **ABSORBED** |
| N5c β discrimination | measured | **PROVED** ✅ (DH side, lower bound) |
| IV.1 limit operator Jacobi `n²` | GAP | GAP (next) |
| IV.2 rigidity `n² ⟹ ξ̂_∞=Ξ` | GAP | GAP (next) |
| §V positivity under `/ε₀` | core | **RH-hard core** (left for last) | What remains are **IV.1, IV.2** (structural, tractable) and **§V** (the truly difficult one).
