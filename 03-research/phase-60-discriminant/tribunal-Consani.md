# Tribunal — Severe audit (lens) of the attempted RH proof via CCM **Referee:** C. (assumed role) · **Object:** `RH-PROOF-FULL.md` + supports
(`E2-nucleo-proof.md`, `N5-analytic-loewner.md`, `N5-subpieces-proved.md`,
`AUDIT-repairs-E1-III.md`, `AUDIT-repairs-norm-N5c-IV2.md`).
**Overall entry verdict:** RH is NOT proved. The document already admits it. My job is to
verify that the candor of the self-audit is *sufficient* —and where it still overstates—,
and to close what can be closed. Spoiler: the self-audit is mostly correct and notably
candid, but there are **two residual overstatements** in the variational core (§2.6) that
must be flagged, and the "horizon lemma" has a **wrong density factor** that
invalidates the count `#{γ_ρ≤T*}=dim` as written. I fix it below (Task 3). Cold candor first: the core is RH-equivalent, so **no amount of analysis
closes the chain**. What CAN be closed rigorously is the scaffolding and —partially—
the frame deficit lemma, with an explicit residual that is RH again. I do it. --- ## TASK 1 — Piece-by-piece verdict Convention: **SOLID** = withstands audit as mathematics (possibly modulo a classic
result cited candidly); **GAP** = proof missing, or the written proof is false, or the claim
is a disguised RH-equivalent. ### E0 — CCM construction, identity `QW=`Weil form — **SOLID (with one caveat)**
The definition (Def 0.1, divided-difference sine kernels, diagonal with Fejér
window) is correct and the Loewner reading (II.1–II.2 of `N5-analytic-loewner.md`) is clean and
correct: `QW` is a superposition of Loewner matrices of `sin` against the Weil measure
`μ_W = w_arch dy − Σ_{n'≤λ²}(Λ(n')/√n')δ_{log n'} + 𝒫`. **The caveat:** the
identity `⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` is claimed "exact", and the text adds
`A_λ = A_∞|_{E_λ}` "exact (primes >λ² do not contribute by support)". The **support
argument is correct in structure but is miscounted in the master document** — see Task 2,
where I show that the claim "primes >λ² contribute zero" is true *for the arithmetic
part* but the equality with `Σ_ρ` additionally requires the pole term `𝒫` and the
archimedean term, which are NOT truncated and which the document hides in "+𝒫". The identity as
*form* is correct (it is Weil's explicit formula restricted to `PW_Ω`); as a *sum over
zeros with those exact constants* there is a detail (factor and the `conj γ_ρ`) that I audit
below. Verdict: SOLID as a definition and as a Weil form; the phrase "=Σ_ρ... exact"
needs the qualification from Task 2. ### E1 / H1 / H1′ — finite real-rootedness — **GAP (correctly self-flagged)**
The self-audit is **correct and candid**, and here I sign off without reservations: the recorded
proof (interlacing with `ξ_k>0`) **is false**, and the counterexample `ξ=(−1,2,−1)`,
`d=(−1,0,1)` → `f(s)=−2/(s³−s)` (zero real roots) refutes it terminally. The
fundamental eigenvector is NOT of definite sign (edge carrier `ω*≈0.966π`), so
Perron–Frobenius does **not** deliver the property. The distinction H1 (PF ⟹ structure/nodelessness of
the *envelope*) vs H1′ (`QW` PSD ⟺ Weil-positivity ⟺ RH-up-to-T*) is **exactly the
correct fix**, and is the most important observation in the whole self-audit: *PF ≠
PSD*. If H1 "proved QW PSD" it would have proved RH; that is impossible, and the document now
acknowledges it. Real-rootedness is empirically true and can be cited as CCM Thm 1.1(iii)
black box; its own proof (Hermite–Biehler from the self-adjoint realization) is **open**.
HIGH severity but candidly stated. **GAP.** ### N0 — `Ξ_T→Ξ` strip-uniform — **SOLID**
The computation is correct and I sign it line by line. `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` (double-exp,
even) is classical (Riemann/Pólya). The change `v=e^{2u}` gives `Γ(7/4+δ/2, πλ²)` and the incomplete
Gamma bound `∫_X^∞ v^a e^{−πv}dv ≤ C X^a e^{−πX}` for large `X` is standard. Result
`C_δ λ^{5/2+δ}e^{−πλ²}` correct. The corollary (the strip can grow up to `o(λ²/logλ)`)
is correct and notable. Genuinely proved piece, unconditional, with no mention of zeros.
**SOLID.** ### N1 — axis→off-axis transfer (harmonic measure) — **SOLID*** (modulo Boas, classical)
Lemma 2 correct. `w=log|F|−τ Im z` subharmonic, bounded above on `H` by Boas Thm
6.2.4 (exponential type + bounded on ℝ ⟹ `|F(z)|≤Γe^{τ|Im z|}`), two-constants + harmonic
measure of the segment `ω_{[−R,R]}(iy₀)=(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)`. All correct. The
only nuance: it requires `F=δ̂` to be *bounded on all of ℝ* by `Γ`, not only on `[−R,R]`; that
is supplied by N2. It fits. **SOLID* (classical result cited candidly).** ### N2 — global amplitude — **SOLID**
Two versions coexist: `Γ=O(logλ)` (Nikolskii/Plancherel–Pólya, `‖ξ̂‖²_{L²}=πlogλ`) and
`Γ=O(1)` with normalization `ξ̂(0)=Ξ(0)`. Both correct; the first is the robust one and is the
one needed by N1 (`Γ^{1−ω}=exp(O(λ^{−2}loglogλ))→1`). The orthogonality of the `sinc_k` and
Parseval are fine. **SOLID.** (I note that the improvement to `O(1)` *assumes* `ξ̂_λ≈Ξ`, which is what
one wants to prove; that is why the load-bearing version is `O(logλ)`, which is unconditional.
Good that the document uses that one in the Reduction.) ### N3 — amplification `λ^{y≤½}` — **SOLID*** (Boas/Phragmén–Lindelöf)
Standard Bernstein/Boas: type `τ`, bounded by `M` on ℝ ⟹ `|F(x+iy)|≤Me^{τ|y|}`. Gives the
factor `λ^{1/2}` for `|y|≤½`. Correct. **SOLID*.** ### Reduction (Theorem 2) — **SOLID, modulo E1**
`ξ̂_λ−Ξ=(ξ̂_λ−Ξ_T)+(Ξ_T−Ξ)`; second term `O(λ³e^{−πλ²})` (N0, δ=½); first via N1 with
`R=T*~λ²` gives `≲λ^{1/2}ε_loc`. The conditional conclusion "`ε_loc=o(λ^{−½}) ⟹ ξ̂_λ→Ξ` on
`|Im z|≤½` ⟹ (E1+Hurwitz) RH" is **logically correct**. This is the jewel of the program: a
clean reduction of RH to *a single measurable real number*. It is candid because it does NOT claim to prove
`ε_loc=o(λ^{−½})`. **SOLID** as an implication (modulo E1 for the Hurwitz step). The real value
of the program lives here. ### III — relative stability — **GAP (conditional; correctly downgraded)**
The absolute form of Davis–Kahan is useless (`ε_1−ε_0≈3ε_0≈10^{−20}`); the renormalization
`Â=A/ε_0` fixes it *under (H-gap), (H-lim) and (H-pos)*. The self-audit already downgraded it to a
conditional theorem, **and also detected the crucial point**: `(H-pos) ε_0>0 = Weil-positivity-
up-to-T* ≈ RH-up-to-T*`. That is, the renormalization *bakes in RH*. This is correct
and severe: III is neither unconditional nor "almost". The three hypotheses are numerical or RH. **conditional
GAP.** Well stated. ### N5b — absorbed boundary — **SOLID (as a reduction)**
Argument VIII (`N5-analytic-loewner.md`) is correct: the target `Ξ_T` is uniform in `t`
including the boundary (`L¹` bound on the tail of `Φ`, `|e^{itu}|=1`), and `|Ξ(t)|~e^{−πt/4}` suppresses
the boundary in *absolute* sup-norm; the "boundary layer" seen numerically was a *root* error
(relative), not a sup-norm one. The root-vs-sup distinction is correct and I sign it. **BUT** —
caveat — "the boundary dissolves" reduces N5b to `sup|ξ̂−Ξ_T|`, which is **§V = the core**.
It is not that the boundary disappears as a problem; it *merges* with the core. The document
says so ("absorbed into §V"). SOLID as a reduction, not as a closure. ### N5c — β discrimination (RH-false does not converge) — **SOLID*** (modulo real-rootedness + axis-convergence)
The real-rooted monotonicity lemma `|g(x+iy)|≥|g(x)|` for `g∈\overline{LP}`: the proof via
Hadamard factorization (each factor `|1−(x+iy)/r_n|²≥(1−x/r_n)²`, `r_n∈ℝ`) is **correct**.
Prop N5c.2 (DH with off-line zero `z₀`: `ε_loc^{off}≥|ξ̂_λ(z₀)|≥|ξ̂_λ(x₀)|→|Ξ_f(x₀)|>0`) is
correct *modulo* (i) real-rootedness of `ξ̂_{f,λ}` (self-adjoint CCM, holds for DH with Λ≥0)
and (ii) axis convergence. **A severity objection:** the argument assumes `Ξ_f(x₀)≠0`
"because the real projection of an off-line zero is not an on-line zero". This is generically
true but is NOT a theorem: if `Ξ_f` happened to have a real zero *by chance* at `x₀`, the bound
would vanish. For Davenport–Heilbronn this is verified case by case (the known off-line zeros do not
project onto real zeros), so the bound is non-vacuous *in the exhibited cases*, but the general
statement needs that verification. Minor. **SOLID*** with that note. ### IV.1 — limit operator `Â_∞` — **GAP (open analysis)**
The measured relative spectrum `ε_k/ε_0→(k+1)²=n²` with alternating parity `(−1)^k` is a *datum*,
not a theorem. All the constant-coefficient identifications (Dirichlet, Hermite,
prolate, free box, totally non-negative) are **refuted** according to the document itself.
The reading "2nd-order Sturm–Liouville with variable coefficients in the boundary layer after `/ε_0`"
is phenomenological. Candidly flagged as analysis (Landau–Widom / de Branges), not RH-hard.
I agree: it is closable *in principle* but it is open. **GAP.** Note: `γ=3` (=2²/1²) is
only measured; (H-gap) of III depends on this. ### IV.2 ≡ §V — the core — **GAP RH-EQUIVALENT (correct, but with two residual overstatements)**
This is the piece I audit in depth in Task 2. Verdict: **RH-equivalent, correctly
identified as the core.** It is not conflation (`QW` IS the Weil form — I verify
and confirm this). But the chain `min Σ|g(γ_ρ)|² ⟹ g vanishes on {γ_ρ≤T*} ⟹ (horizon:
#=dim) g₀=Ξ_T+O(deficit) ⟹ g₀→Ξ_T` contains **two overstated steps** that I detail in
Task 2 and (partially) repair in Task 3. **RH-hard GAP.** ### E3 — Hurwitz — **SOLID, modulo E1**
Classical: a uniform limit on compacta of LP functions is LP (the zeros cannot migrate off
the axis without a real zero chasing them). Correct, modulo each `ξ̂_λ∈LP` (=E1). **SOLID.** ### E4 — `Ξ∈LP ⟺ RH` — **SOLID (classical)**
Definition of RH via the Laguerre–Pólya class; de Branges/classical. **SOLID.** --- ## TASK 2 — Scrutiny of the variational core (§2.6) ### 2.A Is `A_λ(g,g)=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` exactly correct? **Verdict: correct as a Weil FORM, but the master document over-simplifies the
non-arithmetic terms, and the "exact" deserves three bookkeeping corrections.** Weil's explicit formula states, for a suitable even test `g` with transform `ĝ`:
``` Σ_ρ ĝ(γ_ρ) = ĝ(i/2)+ĝ(−i/2) [pole] − Σ_{n} (Λ(n)/√n)(g(log n)+g(−log n)) [primes] + (1/2π)∫ ĝ(r)[archimedean ψ-term] dr [archimedean].
```
Rearranging, the "zero form" `Σ_ρ ĝ(γ_ρ)` EQUALS (archimedean + pole) − (arithmetic).
The document writes `QW[m,n]=∫q w_arch − Σ_{n'≤λ²}(Λ/√n')q + 𝒫`. This is **the right-
hand side** (archimedean − arithmetic + pole). Hence: 1. **The "+𝒫" (pole of ζ) is NOT a decorative detail.** It is `ĝ(i/2)+ĝ(−i/2)`, and it is precisely the term that breaks naive positivity: the Weil form is PSD *on the subspace where the pole term is controlled* (test functions with `ĝ(±i/2)` absorbed). The document folds it into "+𝒫" without exhibiting that its quadratic contribution is what makes "QW PSD ⟺ RH" rather than a trivial PSD. The identity `=Σ_ρ` is correct **only if** the pole and the archimedean term sit on the zero-side; the text asserts it but does not spell it out. It is not an error; it is an over-compression that hides where the difficulty lives. 2. **The `conj(g(conj γ_ρ))` and the constants.** Under RH `γ_ρ∈ℝ` and `conj γ_ρ=γ_ρ`, so the term is `Σ_ρ|g(γ_ρ)|²` — correct, a sum of squares, PSD. **Without RH**, `γ_ρ` is complex and `conj(g(conj γ_ρ))` is the factor that makes the form *indefinite Hermitian* (the pairs of zeros `ρ, 1−ρ̄` contribute cross terms of indefinite sign). This is **correct** and is the key observation: the structure `g(γ_ρ)conj(g(conj γ_ρ))` is exactly Weil's quadratic form whose positivity ⟺ RH (Weil 1952, Bombieri). **The document gets this right.** The only constant-level caveat: it is missing the multiplicity/measure factor (each zero enters with weight 1 only if simple; the correct form carries the density `d N(t)`), irrelevant under RH-simple but worth recording. 3. **The restriction `A_λ=A_∞|_{E_λ}` exact because "primes >λ² do not contribute".** This is **correct for the arithmetic part and ONLY for it**: `g=ξ̂` has transform support in `[−Ω,Ω]=[−logλ,logλ]`, and `g(log n')` is evaluated at `log n'`; for `n'>λ²`, `log n'>2logλ=L`... but watch out! the support of `g` is `Ω=logλ`, not `L=2logλ`. The prime-truncation argument at `n'≤λ²` uses `log n'≤logλ²=2logλ`, which is `L`, **not** `Ω`. There is a **factor-of-2 inconsistency** between the support `Ω=logλ` of `ξ̂` and the prime cutoff `n'≤λ²` (which corresponds to length `2logλ`). Checking: the `q_{mn}(y)` are integrated on `[0,L]` with `L=2logλ`, and the arithmetic term subtracts over `log n'∈[0,L]`, i.e. `n'≤e^L=λ²`. Consistent with `n'≤λ²`. But then the *effective support of the form* is `L=2logλ`, while `ξ̂` has type `Ω=logλ=L/2`. The self-convolution `g⋆g̃` (which is what the Weil form evaluates at `log n'`) has support `2Ω=L`. **Resolved: there is no error**, because the Weil form evaluates the *autocorrelation* `g⋆ḡ` of support `2Ω=L=2logλ`, and hence the natural cutoff is `e^L=λ²`. Fine. But the document should say "primes `>λ²` do not contribute because the autocorrelation of `ξ̂` has support `2Ω=L`", not just "by support". With that reading, **the support argument is SOLID.** **Conclusion 2.A:** the identity `A_λ(g,g)=Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))` is **correct as
Weil's quadratic form restricted to `PW_Ω`**, with the constants/weight fine if the zeros
are simple and with the pole+archimedean term counted on the zero-side. The phrase "QW IS the
Weil form" **holds** (there is no conflation). I confirm it as referee. ### 2.B Is "ground state = Ξ_T ⟺ RH" rigorous? Where is RH used? **Verdict: the EQUIVALENCE with RH is correct and rigorous in one direction and a half; the step
"the minimizer is exactly Ξ_T" is NOT rigorous as it stands, and that —not the
equivalence— is where the handwaving is.** Breaking down the document's chain: - **"Under RH the form is `Σ_ρ|g(γ_ρ)|²≥0`."** Correct and trivial (2.A.2). RH is used here: `γ_ρ∈ℝ`. - **"Its band-limited minimizer vanishes on `{γ_ρ≤T*}`."** Here lies the **first overstatement**. The minimizer of a PSD form `Σ_ρ|g(γ_ρ)|²` on `PW_Ω` with `‖g‖=1` is the **eigenvector of the smallest eigenvalue** of the frame operator `S=Σ_{γ_ρ≤T*}K_{γ_ρ}⊗K_{γ_ρ}`, which in general **is NOT zero** (the form is strictly positive if the `{K_{γ_ρ}}` span `PW_Ω`). "Vanishes on `{γ_ρ≤T*}`" is only possible if `dim PW_Ω > #{γ_ρ≤T*}`, i.e. if there are *more degrees of freedom than nodes*. The document invokes the "horizon lemma: #=dim" precisely for this — but then the null space has dimension `dim−#=0` (if #=dim exactly!), and `g₀=Ξ_T` is NOT forced: with `#=dim` the frame is a *basis* (exact critical density) and the only `g` vanishing at all the nodes is `g≡0`, not `Ξ_T`. **The count `#=dim` is precisely the limiting case where the argument breaks down**, not where it works. I discuss this in Task 3. - **"(Horizon lemma: #=dim) g₀=Ξ_T+O(deficit)."** The `+O(deficit)` acknowledges that it is NOT exact at finite `λ` (`AUDIT-repairs-norm-N5c-IV2.md` §3 already downgraded it from "exact" to "limit"). Fine. But the mechanism by which the deficit `ε_0~C₀/λ²` and by which the minimizer *converges to `Ξ_T` specifically* (rather than to any other near-null function) **is not proved**. It is the frame-deficit lemma claim, which I attack in Task 3. - **"Without RH the form is indefinite, the minimizer concentrates on off-line zeros, ≠Ξ_T."** Correct in spirit (N5c formalizes it from the *non-convergence* side, with lower bound `|Ξ_f(x₀)|>0`). This direction **is indeed proved** (modulo real-rootedness + axis-convergence), and it is the best part of the core: the RH-false side is unconditional. **Where exactly is RH used?** In TWO places, and they are the same: 1. So that `Σ_ρ g(γ_ρ)conj(g(conj γ_ρ))=Σ|g(γ_ρ)|²≥0` (positivity of the form) — this is `ε_0≥0`, **= Weil-positivity-up-to-T* = RH-up-to-T*** (not full RH, but truncated to height `T*~2πλ²`). 2. So that the limit `ξ̂_∞=Ξ` at rate `o(λ^{−½})` — the "bridge" of the Reduction. And here lies the **second residual overstatement** I must flag: the document says
"ground state of Weil = Ξ_T ⟺ all the γ_ρ real ⟺ RH". The equivalence
`ε_0≥0 ⟺ RH-up-to-T*` is correct (it is Weil's). But "ground state = Ξ_T" as a
*stronger* claim (not just `ε_0≥0` but the eigenvector IS `Ξ_T`) **is not equivalent to RH-
up-to-T***: it is equivalent to RH-up-to-T* **plus** a uniqueness/rigidity theorem for the
minimizer, which is the content of Landau–Beurling at critical density (Task 3). The chain
mixes "the form is PSD" (=local RH, correct) with "the minimizer is the truncated Riemann
function" (=local RH + frame rigidity, stronger than stated). The document **says it candidly
in one line** ("modulo rigor of the frame deficit, Landau–Beurling") but the
boxed statement `ground state=Ξ_T ⟺ RH` is therefore **slightly overstated**: the correct statement is
`ε_0≥0 ⟺ RH-up-to-T*`, and `ground state=Ξ_T ⟸ RH-up-to-T* + frame rigidity`. **Conclusion 2.B:** the piece is genuinely RH-equivalent (there is no trick, no
hidden circularity beyond what is confessed). The handwaving is NOT in the equivalence
`ε_0≥0⟺local-RH` (that is Weil's, solid) but in the jump to "the minimizer is exactly
`Ξ_T`", which requires the frame-deficit lemma. That is the only thing attackable without touching RH, and it is
Task 3. --- ## TASK 3 — The frame-deficit lemma + repair of the horizon lemma Here I do mathematics, not auditing. Goal: to prove rigorously, with
Landau–Beurling/interpolation theory, what exactly the minimizer `g₀` satisfies, and to exhibit the
**exact residual** that is RH again. I also repair the horizon count, which is
**wrong by a critical factor** in the document. ### 3.1 Repair of the horizon lemma (the count is wrong) The document (E2-nucleo §3, "Horizon lemma") states:
> "Ξ has `~N(T*)~(T*/2π)log T* ~ λ²·2logλ` zeros under the horizon; `ξ̂` of type `logλ`
> has `~(logλ/π)·2T* ~ (2/π)λ²logλ` real degrees of freedom — **comparable**." **This is not correct as the equality `#=dim`.** Let us compute both quantities carefully. **(a) Zero count (Riemann–von Mangoldt).** Up to height `T`,
``` N(T) = (T/2π)log(T/2π) − T/2π + O(log T).
```
With `T*=2πλ²`:
``` N(T*) = (2πλ²/2π)log(2πλ²/2π) − λ² + O(logλ) = λ²·log(λ²) − λ² + O(logλ) = 2λ²logλ − λ² + O(logλ) ≈ 2λ² logλ.
```
That is, **`#{γ_ρ: 0<γ_ρ≤T*} ≈ 2λ²logλ`** (and double that, `~4λ²logλ`, counting `±`). Good:
the document's `2λ²logλ` is correct for the one-sided count. **(b) Dimension / sampling density of `PW_Ω`.** `ξ̂∈PW_Ω` with `Ω=logλ` (exponential type
`logλ`). By Nyquist/Landau, the number of degrees of freedom of a `PW_Ω` function
*observed on an interval of length `2T*`* (from `−T*` to `T*`) is the **Nyquist
density × length**:
``` Nyquist density of PW_Ω = Ω/π = logλ/π (samples per unit length), effective DOF on [−T*,T*] = (Ω/π)·(2T*) = (logλ/π)·(4πλ²) = 4λ² logλ.
```
(The document writes `(logλ/π)·2T* = (2/π)λ²logλ`, losing a factor `2π` by using `2T*`
instead of the correct length `2T*=4πλ²`, and carrying the `1/π`. Clean recomputation:
length `=2T*=4πλ²`, density `=logλ/π`, product `=4λ²logλ`.) **(c) Correct comparison.** Both sides:
``` #{γ_ρ: |γ_ρ|≤T*} = 2·N(T*) ≈ 4λ²logλ − 2λ², DOF(PW_Ω on [−T*,T*]) ≈ 4λ²logλ.
```
**They agree at the leading order `4λ²logλ`**, with **deficit** `DOF − # ≈ +2λ² + O(logλ) > 0`. **Horizon lemma (corrected version).**
> The number of degrees of freedom of `PW_Ω` on `[−T*,T*]` **exceeds** the number of zeros
> `#{|γ_ρ|≤T*}` by exactly `≈ 2λ²` (the `−T/2π` term of Riemann–von Mangoldt),
> at an order subdominant to the common leading term `4λ²logλ`. **Consequence (critical for the frame deficit):** the density of the nodes `{γ_ρ}` relative
to the Nyquist density of `PW_Ω` is
``` ρ(nodes)/ρ(Nyquist) = [4λ²logλ − 2λ²] / [4λ²logλ] = 1 − 1/(2logλ) < 1.
```
That is, **the Riemann zeros sample `PW_Ω` STRICTLY BELOW the
Beurling critical density**, with relative deficit `1/(2logλ)→0`. This is the opposite of "#=dim
exactly": there is an *underspanning* that tends to critical from below. This is the correct version,
and —important— **it is what makes the frame-deficit argument work** (see 3.3): if
it were exactly critical (#=dim) the frame would be a tight Riesz basis and the only vector
vanishing at the nodes would be `0`; with deficit `>0` there is an "almost-null" space of dimension
`≈2λ²` where the minimizer lives. ### 3.2 Precise framework for the minimizer Let `Ω=logλ`, `H=PW_Ω` (Paley–Wiener, type `Ω`, `L²(ℝ)`), with reproducing kernel
`K_γ(s)=sin(Ω(s−γ))/(π(s−γ))`, `⟨g,K_γ⟩=g(γ)`. Define the **finite frame operator**
``` S_λ:= Σ_{|γ_ρ|≤T*} K_{γ_ρ} ⊗ K_{γ_ρ}: H → H, ⟨g,S_λ g⟩ = Σ_{|γ_ρ|≤T*} |g(γ_ρ)|².
```
Under RH-up-to-T* (the `γ_ρ` real up to `T*`), `S_λ⪰0` and the band-limited ground state is
``` g₀:= argmin_{‖g‖=1, g∈H} ⟨g, S_λ g⟩, ε_0:= λ_min(S_λ).
```
The program's claim is: `g₀ → Ξ_T` and `ε_0→0` (deficit). Let us test it with the explicit residual. ### 3.3 Frame-deficit theorem (candid partial progress) **Theorem (frame deficit, version).** Let `Ω=logλ`, `T*=2πλ²`, and suppose
**RH-up-to-T*** (i.e. `{γ_ρ}_{|γ_ρ|≤T*}⊂ℝ`). Let `m:=DOF−# ≈ 2λ²` be the deficit from Lemma 3.1.
Then: **(i) Upper bound on the smallest eigenvalue.** The space
``` V_λ:= { g∈PW_Ω: g(γ_ρ)=0 ∀ |γ_ρ|≤T* }
```
has `dim V_λ ≥ m ≈ 2λ² > 0` (because imposing `#≈4λ²logλ−2λ²` linear conditions on a
space of dimension `≈4λ²logλ` leaves a kernel of dimension `≥m`). For every nonzero `g∈V_λ`,
`⟨g,S_λ g⟩=0`, so
``` ε_0 = λ_min(S_λ) = 0 on V_λ (the minimum is exactly 0 on the null subspace!).
```
*Severe comment:* this says that the minimizer `g₀∈V_λ` vanishes at ALL the `γ_ρ≤T*`
**exactly**, NOT "with `O(deficit)`". The document's `O(deficit)` is misleading: with
strict underspanning the minimum of the *finite* form is exactly 0, not small. The "deficit
`ε_0~C₀/λ²`" of the document is NOT `λ_min(S_λ)` (which is 0) but `λ_min` of the **full
Weil form `QW`** (which includes archimedean+pole, not just `S_λ`). These are distinct objects. **This
is a third imprecision in the document:** it conflates `λ_min(S_λ)` (=0, the pure zero frame)
with `ε_0=λ_min(QW)` (the full Weil form, whose sign IS RH). The zero frame alone is
trivially PSD-degenerate; what has nontrivial sign is `QW`. **(ii) Why `Ξ_T` and not some other element of `V_λ`?** Here is the core. `Ξ_T∈V_λ`
**approximately**: `Ξ` vanishes exactly at the real `γ_ρ` (under RH), and `Ξ_T=Ξ+O(e^{−πλ²})`
uniformly (N0), so `Ξ_T(γ_ρ)=O(e^{−πλ²})` for `|γ_ρ|≤T*`. Hence
``` ⟨Ξ_T, S_λ Ξ_T⟩ = Σ_{|γ_ρ|≤T*} |Ξ_T(γ_ρ)|² = #·O(e^{−2πλ²}) = O(λ²logλ · e^{−2πλ²}) = O(e^{−πλ²}).
```
Thus `Ξ_T` is a quasi-element of the kernel of `S_λ`. **BUT `V_λ` has dimension `≈2λ²≫1`**:
there is a huge space of band-limited functions vanishing at the Riemann zeros. `Ξ_T`
is ONE of them; nothing in `S_λ` alone singles it out. **The distinction must come from the full
`QW` (archimedean+pole), not from `S_λ`.** That is: the minimizer of `QW` (not of `S_λ`) is what the
program wants, and `QW=S_λ−(arch+pole)` rearranged; the positivity of `QW` (=RH) is what
selects it. **There is no way to prove `g₀=Ξ_T` using only the zero frame + critical
density.** The residual is exactly the positivity of the full Weil form. **Exact residual (what does NOT close):**
``` g₀ = Ξ_T ⟺ Ξ_T minimizes QW (not S_λ) on PW_Ω ⟺ QW ⪰ 0 with ground state Ξ_T ⟺ Weil-positivity-up-to-T* with minimizer rigidity = RH-up-to-T* (+ uniqueness).
``` **Conclusion of Task 3 (candid).** The "frame-deficit lemma" **is NOT closable by
Landau–Beurling/interpolation alone**, contrary to what the document's appendix suggests
("Landau–Beurling would close g₀→Ξ_T"). Structural reason: the zero frame `S_λ` has a
*kernel of dimension `≈2λ²`* (underspanning, corrected Lemma 3.1), and `Ξ_T` is only one of
`≈2λ²` near-null candidates. Selecting `Ξ_T` requires the *full* Weil form
(archimedean + pole), whose positivity is RH-up-to-T*. **What I DID close rigorously:** 1. **The corrected horizon lemma** (3.1): zero density / Nyquist density `= 1 − 1/(2logλ) < 1`, strict underspanning tending to critical from below; dimensional defect `m≈2λ²`. (The document had the length factor wrong and claimed `#=dim`, which is false; the correct regime is sub-critical, not critical.) 2. **The identification of the exact residual**: `g₀=Ξ_T` is RH-up-to-T* plus uniqueness of the `QW` minimizer, NOT a consequence of sampling theory. This *refutes* the hope of Appendix-2 ("frame deficit ⟹ Landau–Beurling closes g₀→Ξ_T") and reclassifies it as **RH-hard**, not as closable analysis. 3. **The distinction of objects** `λ_min(S_λ)=0` (zero frame, trivial) vs `ε_0=λ_min(QW)` (Weil form, sign = RH). The document conflates them into "deficit `ε_0~C₀/λ²`". **Positive partial progress that IS real mathematics:** under RH-up-to-T*, `Ξ_T` *is* a
quasi-element of the kernel of `S_λ` with residue `O(e^{−πλ²})` (3.3.ii), and `dim V_λ≈2λ²`. This
means that **if** one additionally proves that `QW⪰0` (local RH) **and** that its ground state is unique
on `V_λ`, then `g₀=Ξ_T+O(e^{−πλ²})` with the super-exponential rate that the program measured.
The rate `o(λ^{−½})` required by the Reduction would follow comfortably — *conditional on local-
RH*. It is not a closure; it is the clean localization of the residual. --- ## TASK 4 — Closable vs RH-hard **Genuinely closable (analysis, not RH):**
- **N0, N1, N2, N3, Reduction (Thm 2), E3, E4**: already solid (some modulo classical results candidly cited). Require no work.
- **Horizon lemma**: I closed it here, corrected (3.1). Closed.
- **N5c (RH-false side)**: solid modulo real-rootedness + axis-convergence; the lower bound `|Ξ_f(x₀)|>0` is correct (verify `Ξ_f(x₀)≠0` case by case for DH).
- **IV.1 (identification of the limit operator)**: hard analysis (Landau–Widom/de Branges), open but not RH-hard. Closable in principle.
- **E1 proper (Hermite–Biehler from the self-adjoint realization)**: closable in principle (it is de Branges/HB theory), but NOT trivial — the recorded proof is false and the correct one is open. Medium risk. **RH-hard (not closable without proving RH):**
- **H1′ (`QW` PSD = `ε_0≥0`)**: = Weil-positivity-up-to-T* = local RH. RH-hard.
- **III (via `/ε_0` with (H-pos))**: the renormalization assumes `ε_0>0` = local RH. RH-hard (the conditional implication is correct; the hypotheses are not).
- **IV.2 ≡ §V (`ξ̂_∞=Ξ`, rate `o(λ^{−½})`)**: RH-equivalent. The core.
- **The "frame deficit" `g₀=Ξ_T`**: contrary to what the document suggested, **I reclassify it from closable to RH-hard** (Task 3): selecting `Ξ_T` is local RH + uniqueness, not sampling. This is my most substantive correction to the program's status. --- ## FINAL VERDICT () The document does NOT prove RH and does not claim to — I respect that. The self-audit is, for the
most part, candid and technically correct; the downgrades of E1, III and H1′ are the
correct ones, and the `PF≠PSD` observation is excellent. The approximation scaffolding (N0–N3,
Reduction) is solid, reusable mathematics; the reduction of RH to "a single real number
`ε_loc=o(λ^{−½})`" is clean and valuable. **My three referee corrections to the stated status:**
1. **The horizon lemma was miscounted** ("#=dim"); the correct statement is sub-critical underspanning, `zero density/Nyquist = 1−1/(2logλ)`, deficit `≈2λ²`. I repaired it.
2. **The "frame deficit" is NOT closable by Landau–Beurling** (as the Appendix hoped): `S_λ` (zero frame) has a kernel of dimension `≈2λ²` and `Ξ_T` is one of `≈2λ²` candidates; the selection requires the full Weil form = local RH. Reclassified as RH-hard.
3. **The document conflates `λ_min(S_λ)=0` with `ε_0=λ_min(QW)`** (the one whose sign=RH). The "deficit `ε_0~C₀/λ²`" belongs to the full `QW`, not to the zero frame. RH-hardness is **distributed** (H1′, `/ε_0`, IV.2, and now also the frame deficit),
more than the original picture admitted, but less catastrophically than a strict audit
would fear: there is no hidden circularity nor conflation `QW≠Weil` (I verified that `QW` IS the
Weil form). The program is a **candid and precise localization of RH in a
Weil-positivity variational core**, not a proof. Cold candor: the "core" does not move a
millimeter with analysis; it is RH.
