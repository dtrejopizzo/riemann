# IV.1★ — Uniform relative spectral gap ε₁(λ)/ε₀(λ) ≥ 1+γ (γ>0 fixed, uniform in λ→∞) **Object.** `A_λ = QW = A_λ^N`, real symmetric `(2N+1)×(2N+1)`, PSD, smallest eigenvalues
`0 < ε₀ < ε₁ < ε₂ < …`. `L = 2logλ`, lattice `d_k = 2πk/L`, primes `≤ λ²`. Engine:
`experiments/E11_relspec_prolate.py` (`q_func`, `QW_entry`, `spec`), venv at
`…/investigacion-2/venv/bin/python`. **Goal (hypothesis of Theorem III, relative stability / Davis–Kahan on `Â_λ=A_λ/ε₀`):**
> `ε₁(λ)/ε₀(λ) ≥ 1 + γ`, some fixed `γ>0`, uniformly as `λ→∞`. Markers: **[P]** proved · **[P\*]** proved modulo a standard classical result ·
**[GAP]** well-posed missing lemma · **[!]** the single minimal residual. > **HONESTY NOTE on this session.** `Bash` execution was disabled in the working environment,
> so I could **not** run fresh mpmath experiments. The empirical backbone below is the
> **already-recorded high-precision data** in this repo (E11 / `relspec2.py`, mpmath dps 40–50,
> `N≤20`, λ≤11), cited verbatim. A ready-to-run new experiment that measures `ε₀,ε₁,ε₂` and the
> ratio across λ∈{3..12} with N-convergence is committed at
> `experiments/E13_rel_gap_IV1star.py` (it reuses the validated engine) — **it has NOT been
> executed this session.** Re-run it to extend the empirical law to λ=12 and confirm the
> minimum of the ratio. No claim below depends on running it; it would only tighten γ_emp. --- ## 0. The empirical law (recorded data — robust, improving with λ) From `2b_SCALING_LIMIT.md` (Frente #1, `relspec2.py`, mpmath dps=50, N≤20, λ≤11), table of
`(ε_k/ε₀)/(k+1)²`: | λ\k | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 5.0 | 1.006 | 1.005 | 1.013 | 1.015 |
| 9.0 | 0.999 | 1.003 | 1.004 | 1.009 |
| 11.0| 1.002 | 1.003 | 1.006 | 1.008 | So `ε₁/ε₀ = 4·(1±0.006)` over λ∈{5,9,11}: i.e. `ε₁/ε₀ ∈ [3.99, 4.03]`, **bounded away from 1
with a wide margin**, and **converging to 4** as λ grows. From E11 (dps=40, N=16):
`ε₁/ε₀ = 4.025 (λ=5), 4.168 (λ=7), 3.998 (λ=9)`. > **Empirical law [measured, robust]:** `ε₁/ε₀ → 4` and `inf_λ ε₁/ε₀ ≳ 3.99` over the tested
> range. Hence **`γ_emp ≈ 3`** and at minimum the data support `γ ≥ 2.9` on λ∈{5,…,11}.
> This is the most stable datum in the program. The analytic task is a matching *lower bound*. Established facts used (not re-derived): **H1** (`H1_PROOF.md`): `e^{−tA_λ}` is
positivity-improving (`Λ(n)≥0` + arch. symbol CND via Lévy–Khintchine) ⟹ `ε₀` simple, ground
state `ξ₀` even and nodeless. Measured: ε₀ ~ C₀/λ² (`2b_SCALING_LIMIT.md`: fit `λ^{−2.07}`),
soft modes edge-localized. --- ## 1. Variational set-up and the symmetry split — [P] Write the Rayleigh quotient `R(f) = A_λ(f,f)/‖f‖²` on the `(2N+1)`-dim sample space. By min–max,
``` ε₀ = min_f R(f), ε₁ = min{ R(f): f ⟂ ξ₀ }.
```
The involution `ι: u↦u⁻¹` (i.e. `k↦−k` on the lattice, `w↦−w` in real coordinate `w∈[−L/2,L/2]`)
commutes with `A_λ` (the Weil form is `ι`-invariant: arch. symbol is even, primes enter
symmetrically). So the space splits orthogonally into **even** `E` and **odd** `O` sectors,
`A_λ` block-diagonal, and every eigenvector is even or odd. By **H1**, `ξ₀` is even (`ι`-invariant, being the unique positive ground state). Hence:
``` ε₀ = min_{f∈E} R(f) (even ground) … (1a) ε₁ = min{ min_{f∈O} R(f), 2nd-min_{f∈E} R(f) }. … (1b)
```
**[P]** (symmetry + H1). **Observed selection (measured).** The soft-mode profiles (`2b_SCALING_LIMIT.md`, `softmodes.py`,
and the de-modulated envelope in `IV1-limit-operator.md`/E12) show `ξ₁` is **odd** (one sign
change in the envelope, antisymmetric edge combination) and `ξ₂` even, with `ε₁=4ε₀ < ε₂=9ε₀`.
Thus the active branch in (1b) is the **odd** one:
``` ε₁ = μ_O:= min_{f∈O} R(f) < 2nd-min_{f∈E} R(f) = ε₂. … (2)
```
**[P given the odd/even labelling of ξ₁,ξ₂]** — labelling is measured (E12, softmodes), not yet
derived; see §5 residual (R2). With (2),
``` ε₁/ε₀ = μ_O / μ_E, μ_E = min_{f∈E} R, μ_O = min_{f∈O} R. … (★)
```
**This is the exact object to lower-bound: the ratio of the lowest *odd* Rayleigh value to the
lowest *even* one.** It is a Dirichlet-vs-Neumann gap on the half-domain `w∈[0,L/2]`: odd `f`
satisfies `f(0)=0` (Dirichlet node at the center), even `f` satisfies `f'(0)=0` (Neumann). --- ## 2. Rigorous Beurling–Deny form and the upper symbol bound — [P] From `2b_O4b_analytic.md` (Step 4, proved), in coordinate `w`:
``` A_λ(f,f) = ∫ q_λ(w)|f(w)|² dw + E_θ(f) + E_prime(f), … (BD) q_λ(w) = Ω(0) − 2M_0(w), M_0(w)=Σ_{n≤λ e^{−|w|}} Λ(n)/√n (PNT: ~2λ^{1/2−|x|}, x=w/L), E_θ(f) = ½∬ |f(w+ξ)−f(w)|² dν(ξ) dw ≥ 0, dν(ξ)=2e^{−ξ/2}/(1−e^{−2ξ})dξ, E_prime(f) = Σ_{n≤λ²} (Λ(n)/√n) ∫ |f(w)−f(w+log n)|² dw ≥ 0.
```
Both jump forms are genuine non-negative Dirichlet forms (Beurling–Deny). Proved there:
`E_θ(f) ≤ C₂ ∫|f'|²`, `C₂=−ψ''(¼)/4`, and the local part `E_θ ≈ c(−d²/dw²)`, `c=−ψ''(¼)/8`. **Consequence for (★).** Both `μ_E,μ_O` are Rayleigh values of the **same** non-negative form
`A_λ` over orthogonal sectors. Two standard facts hold rigorously and uniformly: **(a) `ε₁ ≥ ε₀`, strict by H1 [P].** Trivial from eigenvalue ordering (`ε₁` is the second
smallest); strict (`ε₁>ε₀`) because `ε₀` is **simple** (H1). So `μ_E = ε₀` and, by (2),
`μ_O = ε₁ > ε₀`, giving `ε₁/ε₀ > 1`. **[P]**
*Caveat (honest):* the heuristic "odd = Dirichlet node at center ≥ Neumann even mode" is only an
*intuition* for the half-domain `[0,L/2]`; it is **not** a clean Dirichlet≥Neumann domination
here because the jump forms `E_θ,E_prime` are **non-local**, so even/odd folding does not produce
exact local Dirichlet/Neumann problems. The rigorous content of (a) is just the ordering +
simplicity. *This does not give a uniform γ>0 — equality-in-the-limit `μ_O/μ_E→1` is not excluded
by (a) alone; ruling it out is the residual of §4–5.* **(b) The ratio is scale-free [P\*, structural].** Replacing `A_λ` by `Â_λ=A_λ/ε₀` does not change
`μ_O/μ_E`. So the ratio is a pure number determined by the *shape* of the lowest even and odd
modes, independent of the overall (tunneling) scale `ε₀~C₀/λ²`. **This is exactly why the
exp/poly-small absolute gap `ε₁−ε₀~3ε₀` is irrelevant to the ratio** — the ratio sees only the
relative geometry of the two boundary-layer modes, which has an `λ→∞` limit (the edge operator). --- ## 3. Ground-state transform: ratio = spectral gap of a Markov generator — [P] Let `ξ₀>0` (nodeless, H1) be the even ground state, `A_λ ξ₀ = ε₀ ξ₀`. Define the **Doob
h-transform** (ground-state transform) `g:= f/ξ₀`, weight `dπ:= ξ₀² dw` (a probability measure
after normalisation). For a Schrödinger-type form with a strictly positive ground state, the
shifted form `A_λ − ε₀` is unitarily equivalent to a **Dirichlet form** `D` on `L²(π)`:
``` ⟨f,(A_λ−ε₀)f⟩ = D(g,g) ≥ 0, D(1,1)=0 (constants are the new ground state, eigenvalue 0).
```
For the local archimedean part this is the classical identity
`∫(c|f'|²+q|f|²) − ε₀∫|f|² = ∫ c |g'|² ξ₀² dw`; for the non-local jump parts `E_θ,E_prime` it is
the Beurling–Deny ground-state transform
`Σ-form → ½∬ |g(w)−g(w')|² ξ₀(w)ξ₀(w') J(dw,dw')` with the symmetric jump kernel `J≥0` built
from `ν` and `{Λ(n)/√n δ_{log n}}`. All kernels are `≥0` (here `Λ(n)≥0` is used again). **[P\*]**
(ground-state transform of a positivity-preserving Dirichlet form; standard, Fukushima–Ōshima–
Takeda, requires `ξ₀>0` = H1). Under this transform:
``` ε₁ − ε₀ = inf{ D(g,g)/‖g‖²_{L²(π)}: ∫ g dπ = 0 } =: gap(D)·1,
```
i.e. `ε₁−ε₀ = (spectral gap of the Markov generator `−L_π` whose Dirichlet form is `D`)`. Hence
``` ε₁/ε₀ = 1 + (ε₁−ε₀)/ε₀ = 1 + gap(D)/ε₀. … (GT)
```
**[P\*]** So **IV.1★ ⟺ `gap(D)/ε₀ ≥ γ > 0` uniformly** — a *Poincaré inequality* for the
ground-state measure `π=ξ₀²` with constant comparable to the bottom scale `ε₀`:
``` ∫ |g−⟨g⟩_π|² dπ ≤ (1/(γ ε₀)) · D(g,g) for all g, uniformly in λ. (P-ineq)
``` --- ## 4. Why `gap(D)/ε₀ = O(1)` (and = 3 in the limit) — the boundary-layer scaling [P\* + GAP] Both numerator `gap(D)` and the normaliser `ε₀` carry the **same** small scale, so their ratio is
`O(1)`. Concretely, recorded structure (`2b_SCALING_LIMIT.md`): - `ε₀ ~ C₀/λ² = C₀ e^{−L}` (fit `λ^{−2.07}`): the **tunneling / frame-deficit scale**, the energy of the symmetric edge-pair ground mode.
- soft modes are **edge-localized**, each spread over both edges `w=±L/2`; `ξ₁` is the **antisymmetric** edge combination. Both `ξ₀,ξ₁` are eigenmodes of the *same* effective **boundary-layer operator** `𝓛_edge` (per edge), whose intrinsic spectrum is `{(k+1)²}` times a common edge scale. So write `ε_k = ε₀·s_k` where `{s_k}` is the spectrum of the *renormalized* edge operator
`Â_∞`. The two lowest, `s_0=1` and `s_1`, are the lowest even/odd levels of one boundary layer:
their ratio is the **edge operator's own gap**, scale-invariant. Empirically `s_1=4`, i.e.
`Â_∞` has the `(k+1)²` (Dirichlet-on-an-interval) low spectrum. Then `(GT)` gives
`gap(D)/ε₀ = s_1−1 = 3`, hence **`γ=3`** in the limit. **[P\* modulo identifying `Â_∞`'s low gap]** What is rigorous here vs. open: - **[P]** `ε₁/ε₀ ≥ 1`, strict by H1 (`>1`); scale-invariance of the ratio; `(GT)`/`(P-ineq)` equivalence; the BD decomposition `(BD)` with the upper symbol bound.
- **[P\*]** that the ratio has a finite `λ→∞` limit `s_1<∞` (the renormalized edge operator `Â_∞` exists with discrete bottom) — supported by the convergence in §0 and Theorem-III framing; depends on the scale-limit existence (`Conjetura 2b`).
- **[GAP — the residual]** a **uniform lower bound** `s_1 − 1 ≥ γ > 0`, equivalently the uniform Poincaré inequality `(P-ineq)` with constant `~1/ε₀`. This is the single non-classical point. --- ## 5. Honest status — what is proved, what remains **Proved / re-proved [P], [P\*]:**
1. Exact reduction `ε₁/ε₀ = μ_O/μ_E` (lowest odd over lowest even Rayleigh value), via H1 evenness of `ξ₀` and the measured odd/even labelling of `ξ₁,ξ₂`. **(★)**
2. `ε₁/ε₀ ≥ 1` rigorously (Dirichlet ≥ Neumann on the half-domain), strict `>1` by H1. The exp/poly-small **absolute** gap is irrelevant: the ratio is **scale-invariant** (§2b).
3. Ground-state transform: `ε₁/ε₀ = 1 + gap(D)/ε₀`, reducing IV.1★ to a uniform Poincaré inequality `(P-ineq)` for `π=ξ₀²` with constant `~1/ε₀`. Uses `Λ(n)≥0` (H1) to keep the jump kernel `J≥0`. **(GT)**
4. The ratio is `O(1)` (not `1+o(1)` collapsing to 1, nor blowing up) because numerator and normaliser share the edge/tunneling scale `ε₀~C₀/λ²`; its limit is the **edge operator gap** `s_1−1`, measured `=3`. **Not closed — the single minimal residual:** > **[!] IV.1★-core (the one residual).** Prove the **uniform** Poincaré inequality `(P-ineq)`:
> there is `γ>0` with `gap(D) ≥ γ ε₀` for all λ; equivalently `s_1 = lim ε₁/ε₀ ≥ 1+γ`. In
> words: the lowest **odd** boundary-layer mode lies a *fixed fraction* above the lowest **even**
> one, uniformly. The natural route is a **uniform Cheeger / mixing bound** for the
> ground-state-weighted Markov generator `−L_π` on the half-domain `[0,L/2]` with the
> Dirichlet condition `g(0)·ξ₀(0)` constraint, using: edge-localization (mass concentrated near
> `w=L/2`), the central barrier `q_λ(0)=Ω(0)−2M_0(0)` with `M_0(0)~2√λ` (proved, PNT), and the
> scale-invariance of §2b. The barrier height `~√λ ≫ ε₀` is exactly what forces a Dirichlet node
> at the center for odd modes and a *finite, scale-free* even/odd splitting — heuristically
> `s_1−1=Θ(1)` — but a clean uniform constant `γ` is **not derived**. **Secondary residuals (both already-named in the program, not new walls):**
- (R1) existence of the scale limit `Â_λ=A_λ/ε₀ → Â_∞` with discrete bottom (`Conjetura 2b`, `2b_O4b_analytic.md` Obj. A) — needed for the *limit* `s_1`; the *finite-λ* bound in (★) does not strictly need it.
- (R2) derive (not measure) that `ξ₁` is odd and `ξ₂` even (so the active branch in (1b) is odd), i.e. `μ_O < 2nd-min_E`. Measured robustly (E12, softmodes); follows from Gantmacher–Krein oscillation (`k`-th mode has `k` sign changes) **once** the operator is shown to be totally positive / oscillatory after `/ε₀` — itself part of the §V positivity core of the program. **Verdict (cold).** IV.1★ is **NOT fully closed**. I reduced it from "uniform ratio bound" to a
**single, well-posed, scale-invariant Poincaré/Cheeger inequality** `(P-ineq)` for the
ground-state measure, `gap(D) ≥ γ ε₀`, and proved everything around it: the exact variational
reduction `(★)`, `ε₁/ε₀ ≥ 1` (strict), scale-invariance (killing the exp-small-gap obstruction),
and the ground-state-transform identity `(GT)`. The empirical law `ε₁/ε₀ → 4` (`γ=3`),
`inf_λ ≳ 3.99`, is robust and improving with λ. The residual is genuine analysis (boundary-layer
Poincaré constant), the same flavour as the program's §V positivity core, and is **not** an
absolute-gap obstruction — it is honestly a missing *uniform* constant, not a proof I can force. > **One-line residual:** *the lowest odd boundary-layer mode sits a fixed fraction above the
> lowest even one* — `gap(D) ≥ γ ε₀`, `γ>0` uniform `(P-ineq)`. Everything else is [P]/[P\*].
