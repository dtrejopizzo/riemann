# The Riemann Hypothesis via zeta spectral triples (CCM)
## Full chain Link 0 → Link 4 — audited status **Program:** `riemann-program/phase-60-discriminant` > **TRIBUNAL AUDIT (··), see `tribunal-VEREDICTO.md`.**
> Corrections applied: (C.1) the **frame deficit `g₀=Ξ_T` is RH-hard**, NOT closable by
> Landau–Beurling — `S_λ` has a kernel of dim `≈2λ²`, `Ξ_T` is one of `≈2λ²` candidates; the
> selection requires the full Weil form to be PSD = local-RH. (C.2) Distinguish
> `λ_min(S_λ)=0` (zero frame, trivial) from `ε_0=λ_min(QW)` (Weil form, sign=RH).
> (C.3) **E1 is a mandatory citation, CCM Thm 1.1(iii)**, NOT a "closable repair" (, severe);
> the sub-case `ξ_k>0` IS elementary (Lemma M1, Herglotz). (C.4) **`γ=3` is NOT derived**
> (numerical; compactness obstructs deriving `n²`). Expository: **withdraw `Γ=O(1)`** (only
> `O(logλ)` is proved, and it suffices); horizon lemma corrected to **subcritical**
> (`zero/Nyquist density = 1−1/(2logλ) < 1`, deficit `≈2λ²`); free normalization **modulo
> a non-degenerate limit**. Master document: assembles the deductive chain of the –– program
(arXiv:2511.22755) from the construction of the finite Weil operator to RH, **with the
frank status of each piece after mathematical audit**. No proof of RH is claimed: the
core is RH-equivalent. The value is the **localization** of the problem and a genuinely proved
approximation scaffolding around a single core. Notation: `ξ(s)=½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`, `Ξ(t)=ξ(½+it)` (entire, order 1, even, real on
ℝ). `RH ⟺ Ξ∈LP` (Laguerre–Pólya class, real-rooted). `λ>1`, `L=2logλ`, `d_k=2πk/L`,
`Ω=logλ`, `T*=2πλ²` (Nyquist horizon). --- ## 0. STATUS BOARD (post-audit) Legend: **✅ proved** · **✅\*** proved modulo a standard classical result ·
**⟂ conditional** (correct implication, unproved hypotheses) · **🔧 pending repair**
(true but without its own proof) · **🟥 RH-hard core** · **⬚ open (analysis)**. | # | Piece | Status | Audit note |
|---|---|---|---|
| **E0** | CCM construction (Weil form `QW`, `ξ̂_{λ,N}`) | **✅** | definition; validated engine reproduces zeros |
| **E1** | Real-rootedness of `ξ̂_{λ,N}` | **🔧** | registered proof (interlacing) **REFUTED** by counterexample; true via CCM Thm 1.1(iii)/Hermite–Biehler; own proof open |
| └ H1 | simple ground state + positive eigenvector (envelope) | **✅** (structure) | does **NOT** give PSD — correction: PF ⟹ structure, not `ε_0≥0` |
| └ H1′ | `QW` is PSD (`ε_0≥0`) | **= RH** | `QW=`Weil form ⟹ PSD ⟺ Weil-positivity ⟺ RH-up-to-T* (NOT unconditional) |
| **E2** | Convergence `ξ̂_{λ,N} → Ξ` | scaffolding + core | ↓ |
| └ E2.a/c/horizon | limit N / Re s≥1+ε / `T*~2πλ²` | **✅** | |
| └ N0 | `Ξ_T→Ξ` strip-uniform (Fourier, double-exp Φ) | **✅** | robust proof |
| └ N1 | axis→off-axis transfer (harmonic measure) | **✅\*** | modulo Boas (classical) |
| └ N2 | global amplitude `Γ=O(1)` | **✅** | with normalization `ξ̂(0)=Ξ(0)` |
| └ N3 | amplification `λ^{y≤½}` | **✅\*** | Boas/Phragmén–Lindelöf |
| └ N5 reduction | `RH ⟸ ε_loc=o(λ^{−½})` | **✅** | modulo E1 (Hurwitz) |
| └ III | relative stability `ε_loc ≤ C√(logλ)‖Â_λ−Â_∞‖` | **⟂** | hypotheses (H-gap)+(H-lim)+(`ε_0>0`), numerical only |
| └ N5b | boundary absorbed | **✅** | valid reduction |
| └ N5c | discrimination β (RH-false does not converge) | **✅\*** | modulo real-rootedness + axis-convergence |
| └ **IV.1** | identify the limit operator `Â_∞` | **⬚** | phenomenological 2nd-order SL; constant-coefficient identifications refuted |
| └ **IV.2 ≡ §V** | `ξ̂_∞=Ξ` and rate `o(λ^{−½})` | **🟥** | **RH-equivalent** (variational) |
| **E3** | Hurwitz | **✅** | classical, modulo E1 |
| **E4** | `Ξ∈LP ⟺ RH` | **✅** | classical | **One-line summary:** approximation scaffolding (N0,N1,N2,N3) **proved**; E1 with its own
proof **broken** (true via CCM); III **conditional**; the **IV.2≡§V core is RH-equivalent**;
IV.1 is **open** analysis. Weil positivity (=RH) appears, after audit, in H1′
and in `/ε_0`. --- ## 1. Link 0 — the finite Weil operator **Def 0.1 (CCM Weil form).** For `|m|,|n|≤N`, divided-difference sine kernel
``` q_{mn}(y) = (sin(2πmy/L)−sin(2πny/L))/(π(n−m)) (m≠n), q_{nn}(y) = 2(1−y/L)cos(2πny/L).
```
`QW = A_λ^N = (𝒲_{mn})`, real symmetric `(2N+1)²`:
``` 𝒲_{mn} = ∫_0^L q_{mn}(y) w_arch(y) dy − Σ_{n'≤λ²} (Λ(n')/√n') q_{mn}(log n') + 𝒫_{mn},
```
`w_arch` regularized archimedean weight, `Λ` von Mangoldt, `𝒫` the pole term of ζ. **Def 0.2 (band-limited spectral function).** `ξ` eigenvector of the smallest eigenvalue
`ε_0=ε_0(λ,N)` of `QW`. **Canonical normalization** (see §2.0): `ξ` is rescaled so that
`ξ̂(0)=Ξ(0)`. Let
``` ξ̂_{λ,N}(s):= sin(Ls/2) · Σ_{|k|≤N} ξ_k/(s − d_k).
``` **Prop 0.3 [✅].** `ξ̂_{λ,N}` is entire of exponential type `Ω=logλ`, real on ℝ; its real
zeros are the roots of the secular equation `f(s)=Σ_k ξ_k/(s−d_k)` (the `ρ̂_n`). *Proof:*
`sin(Ls/2)` vanishes at `d_k=2πk/L` (`sin(πk)=0`), cancelling the poles; Paley–Wiener gives
type `L/2`. ∎ **Key identity [✅, explicit formula].** For `g∈PW_Ω`,
``` ⟨ξ, QW ξ⟩ = A_λ(g,g) = Σ_ρ g(γ_ρ) conj(g(conj γ_ρ)), g=ξ̂,
```
and `A_λ = A_∞|_{E_λ}` exactly (primes `>λ²` do not contribute, by support). **`QW` IS the
Weil form on the zero side** — this will be central in §4 (the core) and in the audit of H1. --- ## 2. Link 1 — finite real-rootedness 🔧 **Statement.** For all `λ,N`, all roots of `ξ̂_{λ,N}` are real (`ξ̂_{λ,N}∈LP`). **Status after audit: true, but the registered proof is FALSE.** **🔴 Counterexample refuting the old proof.** The registered proof used "with `ξ_k>0`,
the secular function runs `+∞→−∞` between poles ⟹ one root per gap." But the fundamental
eigenvector is **not** of definite sign (it has a boundary carrier `ω*≈0.966π`, ~`N` sign
changes). And without `ξ_k>0` the argument fails: take `ξ=(−1,2,−1)`, `d=(−1,0,1)`:
``` f(s) = −1/(s+1)+2/s−1/(s−1) = −2/(s³−s) → constant numerator, ZERO real roots.
``` **Correct mechanism (Hermite–Biehler / self-adjoint, NOT Perron–Frobenius).**
Real-rootedness also holds for `L_DH` (RH-false, `b(n)` with signs, where PF fails) —
empirically the DH roots are real. ⟹ **it does not depend on the sign of the coefficients**,
so **it is not Perron–Frobenius**; it is CCM's **self-adjoint** spectral realization (secular
roots as a real spectrum) / the **Hermite–Biehler** property of `ξ̂`. - **H1 [✅, corrected]:** PF (`Λ(n)≥0`, via Lévy–Khintchine + Schoenberg + Trotter) gives a **simple** ground state with **positive-envelope eigenvector** (in the de-modulated base). This is **ground-state structure**, and is what the program proved.
- **H1′ [= RH, NOT unconditional]:** that `QW` be **PSD** (`ε_0≥0`) does NOT follow from PF. Since `QW=`Weil form, `QW` PSD ⟺ Weil-positivity ⟺ RH-up-to-T*. (The memo stating "H1 proves QW PSD unconditionally" **overclaims**: PF≠PSD.) **Lemma M1 [✅, sub-case, settled by the tribunal].** If all residues `ξ_k>0`, then
`f(s)=Σξ_k/(s−d_k)` is Herglotz (`Im f<0` in the upper half-plane) ⟹ **only real zeros**,
with strict interlacing. Elementary, self-contained, without citing CCM. *Limitation:* it does
NOT cover the real ground state (boundary carrier `ω*≈0.966π`: neither `ξ_k>0` nor
`(−1)^kξ_k>0`, phase mismatch). **Obstruction theorem [✅, tribunal — see `E1-VEREDICTO-tribunal.md`].** **There is no
universal construction** realizing the roots of `f(s)=Σξ_k/(s−d_k)` as a self-adjoint
spectrum from the isolated data `(ξ_k,d_k)`. *Proof:* the counterexample
`ξ=(−1,2,−1)` **is the ground state of the Dirichlet Laplacian** `tridiag(−1,2,−1)` (a
legitimate real eigenvector) and its secular function `−2/(s³−s)` has no real roots; the
arrow matrix `[[D,ξ],[e^T,0]]` (spectrum = roots of `f`) is non-symmetric with non-real
spectrum. ∎ ⟹ real-rootedness must use SPECIFIC information about the Weil ground state that
`(−1,2,−1)` does not have (it is not the sign of `ξ` — DH holds —, nor total positivity —
refuted —, nor PF alone). The quadratic rescue `Σξ_k²/(s−d_k)` (Herglotz) is **a different
object** (its zeros ≠ those of `ξ̂`; squaring breaks the Weil identity).
The de Branges route exists but verifying HB `|E(s̄)|<|E(s)|` **is logically equivalent to E1**
(the carrier `ω*≈0.966π≠π` prevents translating the PF positivity of the envelope into the
residues). **Verdict on E1 [🔧 = mandatory citation, PROVED].** Real-rootedness **true** = **CCM Thm
1.1(iii)** (self-adjoint Nevanlinna m-function / de Branges `H(E)`), given H1+H2. The
tribunal **proved** that the citation is **necessary**, not laziness: an own proof at the
Herglotz/HB level is **impossible** (obstruction theorem). The `ξ_k>0` sub-case is closed
(Lemma M1). E3 and N5c inherit "modulo E1." **RH-neutral** (holds for DH) ⟹ using E1 is
**not circular**. --- ## 3. Link 2 — convergence (proved scaffolding + RH core) ### 2.0 Normalization [✅, loose end resolved]
The final conclusion is **Hurwitz**, invariant under a nonzero constant: if `c_λ ξ̂_λ→Ξ`
uniformly with `c_λ≠0` and `ξ̂_λ` real-rooted, then `Ξ` is real-rooted. ⟹ the normalization is
**free**; it is fixed by `ξ̂_λ(0)=Ξ(0)`. With it `Γ=sup|ξ̂_λ|=O(1)`, and `ε_loc=sup|ξ̂_λ−Ξ|`
is well defined. Loose end closed for N2, III, reduction. ### 2.1 The object and the reduction
``` ε_loc(λ):= sup_{|t|≤T*} |ξ̂_λ(t) − Ξ(t)|, ξ̂_λ = lim_N ξ̂_{λ,N}.
``` **Theorem N0 [✅] (strip-uniform Fourier truncation).** `Ξ(z)=∫Φ(u)e^{izu}du`,
`Ξ_T(z)=∫_{−T}^{T}Φ e^{izu}du`, `T=logλ`. For every `δ≥0`:
``` sup_{|Im z|≤δ} |Ξ−Ξ_T| ≤ C_δ λ^{5/2+δ} e^{−πλ²}.
```
*Proof:* `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` (double-exp), even; `|Ξ−Ξ_T|≤2∫_T^∞Φ(u)e^{δu}du
≤ C∫_{e^{2T}}^∞ v^{5/4+δ/2}e^{−πv}dv ≤ C'λ^{5/2+δ}e^{−πλ²}`. ∎ **Lemma N1 [✅\*] (off-axis transfer).** `F` entire of type `τ`, `|F|≤Γ` on ℝ, `|F|≤ε` on
`[−R,R]`. Then for `|x₀|≤R/2`, `0<y₀≤δ`:
``` |F(x₀+iy₀)| ≤ e^{τy₀} ε^{ω} Γ^{1−ω}, ω=ω_{[−R,R]}(x₀+iy₀) ≥ 1−(2/π)(y₀/R).
```
*Proof:* `log|F|−τ Im z` subharmonic in `H`, bounded (Boas); two-constants theorem
+ harmonic measure of the segment. ∎ **Lemma N2 [✅] (amplitude).** `Γ=sup_ℝ|ξ̂_λ|=O(logλ)` by Plancherel–Pólya (`‖ξ̂‖_{L²}²=πlogλ`)
+ Nikolskii. **[Tribunal: the previously claimed `Γ=O(1)` is NOT proved; withdrawn. The
`O(logλ)` is what is proved, and it suffices.]** In N1, `Γ^{1−ω}=exp(O(λ^{−2}loglogλ))→1` since `1−ω~λ^{−2}`. **Theorem N3 [✅\*] (amplification, Boas).** `F` of type `τ`, `|F|≤M` on ℝ ⟹ `|F(x+iy)|≤Me^{τ|y|}`.
*Proof:* `g=Fe^{iτz}` bounded on ℝ by `M`, Phragmén–Lindelöf in `H`. ∎ (Gives the factor
`λ^{y≤½}`.) **Theorem (Reduction) [✅, modulo E1].** The zeros of `Ξ` lie in `|Im z|≤½`, and
``` sup_{|Im z|≤½} |ξ̂_λ − Ξ| ≤ C λ^{1/2} ε_loc(λ) + C λ³ e^{−πλ²}.
```
Hence, **if `ε_loc(λ)=o(λ^{−½})`**, then `ξ̂_λ→Ξ` uniformly on `|Im z|≤½`, and by
E1 (real-rooted) + Hurwitz (E3), `Ξ∈LP`, i.e. **RH**. *Proof:* `ξ̂_λ−Ξ=(ξ̂_λ−Ξ_T)+(Ξ_T−Ξ)`;
2nd term `O(λ³e^{−πλ²})` (N0, `δ=½`); 1st, entire of type `logλ`, apply N1 with `R=T*~λ²`,
weight `1−ω~λ^{−2}` negligible (N2) ⟹ `≲ λ^{1/2}ε_loc`. ∎ ### 2.2 III — relative stability [⟂ conditional] The absolute gap `ε_1−ε_0≈3ε_0≈10^{−20}` makes naive Davis–Kahan useless. The renormalization
`Â_λ=A_λ/ε_0` fixes it **under hypotheses**: **Conditional Theorem III.** If **(H-gap)** `inf_λ ε_1/ε_0=1+γ>0`, **(H-lim)** the renormalized
`ξ̂_λ` are Cauchy in `L²`, and **(H-pos)** `ε_0>0`, then `ξ̂_∞` exists and
``` ε_loc(λ) ≤ (C/γ)√(logλ)·η(λ) + Cλ³e^{−πλ²}, η(λ)=‖Â_λ−Â_∞‖_{low}→0,
```
and, **if moreover `ξ̂_∞=Ξ`** (IV.2), `ε_loc→0`. *Proof:* Davis–Kahan on `Â` (bottom isolated,
gap `γ`) + Nikolskii + N0. ∎ **Audit of III:** (H-gap)=IV.1★ (numerical only, `→4`); (H-lim)=Conj 2b (numerical only);
**(H-pos) `ε_0>0` = Weil-positivity-up-to-T* ≈ RH-up-to-T*** (the renormalization bakes RH
right in!). III is a **correct implication with unproved hypotheses** — it is not an
unconditional theorem. ### 2.3 N5b — the boundary dissolves [✅]
`Ξ(t)~e^{−πt/4}` decays; at `T*~λ²`, `|Ξ(T*)|~e^{−π²λ²/2}`. The absolute error near a
root `~|Ξ'|·|ρ̂−γ|` is super-small at the boundary. The "boundary layer" seen numerically was
the **root** error (relative), not the absolute sup-norm (Thm 2). The boundary is benign; the
nontrivial part is absorbed into III/the core. ### 2.4 N5c — converse discriminant [✅\*, modulo named inputs]
**Prop N5c.** If `f` has an off-line zero `z₀=x₀+iη₀` (`η₀≠0`), and on-axis convergence holds
`ξ̂_{f,λ}(x₀)→Ξ_f(x₀)`, then (by real-rootedness of `ξ̂_{f,λ}`)
``` sup_{|Im z|≤|η₀|}|ξ̂_{f,λ}−Ξ_f| ≥ |ξ̂_{f,λ}(z₀)| ≥ |ξ̂_{f,λ}(x₀)| → |Ξ_f(x₀)| > 0.
```
*Proof:* `Ξ_f(z₀)=0`; real-rooted monotonicity `|g(x+iy)|≥|g(x)|`; `Ξ_f(x₀)≠0`. ∎
**Inputs:** real-rootedness (CCM, self-adjoint — holds for DH without `Λ≥0`) + on-axis
convergence (scaffolding E2.a/horizon). RH-false **does NOT converge** off-axis, unconditional
modulo those inputs. ### 2.5 IV.1 — the limit operator [⬚ open, analysis]
`Â_∞` (the limit of `A_λ/ε_0`) has **relative spectrum `ε_k/ε_0→(k+1)²=n²`** (robustly
measured) and **alternating parity `(−1)^k`** (2nd-order signature). **Refuted** are all
constant-coefficient identifications: Dirichlet, Hermite, prolate, free box, totally
non-negative matrix (Gantmacher–Krein). Coherent reading: **2nd-order Sturm–Liouville with
variable coefficients** (boundary operator of the critical frame). The FULL operator is a
**compact** Loewner kernel (not differential); the 2nd order lives in the limit layer after
`/ε_0`. **IV.1 residual:** pin down the coefficients via the limit (Landau–Widom / de
Branges) — **analysis, not RH-hard**. `γ=3` (=`2²/1²`) holds phenomenologically at 2nd order. ### 2.6 IV.2 ≡ §V — the RH-equivalent core [🟥] **Variational characterization [the heart].** By the identity in §1, `A_λ(g,g)=Σ_ρ
g(γ_ρ)conj(g(conj γ_ρ))`. **Under RH** (`γ_ρ` real) it is a sum of squares `Σ_ρ|g(γ_ρ)|²≥0`,
and its band-limited minimizer:
``` minimizes Σ_ρ |g(γ_ρ)|² ⟹ g nearly vanishes on {γ_ρ ≤ T*}.
```
**[Tribunal C.1+C.2 — substantive correction of the next step].** The "horizon lemma:
#=dim" in the document was **miscounted**; the correct count is **subcritical**:
`zero/Nyquist density = 1−1/(2logλ) < 1`, with **dimensional deficit `m≈2λ²`**. Hence the
zero frame `S_λ=Σ_{|γ_ρ|≤T*}K_{γ_ρ}⊗K_{γ_ρ}` has **kernel of dim `≈2λ²`** and
`λ_min(S_λ)=0` (trivial). `Ξ_T` is ONE near-kernel element (`Ξ_T(γ_ρ)=O(e^{−πλ²})`)
among `≈2λ²` candidates: **`S_λ` alone does NOT select `Ξ_T`**. The selection of `Ξ_T` is
made by the **full** Weil form `QW` (archimedean+pole) being PSD = local-RH; and
`ε_0=λ_min(QW)` (sign=RH), **not** `λ_min(S_λ)=0`. ⟹ "`g₀=Ξ_T`" is **RH-hard**, not closable
by Landau–Beurling.
That is, **the Weil ground state is `Ξ_T` ⟺ local-RH + uniqueness of the minimizer**. And
**without RH** (`γ_ρ` complex) the form is **indefinite**, the minimizer concentrates on the
off-line zeros, **`≠Ξ_T`**. By contraposition:
``` ┌──────────────────────────────────────────────────────────────┐ │ Weil ground state = Ξ_T ⟺ all γ_ρ real ⟺ RH │ └──────────────────────────────────────────────────────────────┘
```
**⟹ IV.2 (`ξ̂_∞=Ξ`) is RH-EQUIVALENT.** It is not conflation (`QW` IS the Weil form, the
same object — audited), it is not a soft piece: **it is the RH core**. What is proved of it:
under RH the minimizer **is** `Ξ_T` (variational, modulo rigor of the frame deficit,
Landau–Beurling); and N5c gives the RH-false side (does not converge) unconditionally. What
is missing is the bridge — `ξ̂_λ→Ξ` at rate `o(λ^{−½})` — which **is** RH. --- ## 4. Links 3 and 4 — classical results **E3 (Hurwitz) [✅, modulo E1].** If `ξ̂_λ→Ξ` uniformly on compacts of `|Im z|≤½` and each
`ξ̂_λ∈LP` (E1), then `Ξ` has no zeros with `0<|Im z|≤½` ⟹ `Ξ∈LP`. *Proof:* a complex
zero of `Ξ` would be the limit of real zeros of `ξ̂_λ` — contradiction (Hurwitz). ∎ **E4 [✅, classical].** `Ξ∈LP ⟺ RH` (de Branges). ∎ --- ## 5. Assembly (conditional) **Theorem (conditional proof of RH).** Assume: E1 (real-rootedness, true modulo its own
proof), III with (H-gap)+(H-lim)+(H-pos), and IV.2 (`ξ̂_∞=Ξ`). Then `ε_loc=o(λ^{−½})`
(III), `ξ̂_λ→Ξ` (Reduction), `Ξ∈LP` (E1+E3), **RH** (E4). ∎ But IV.2 is **RH-equivalent** (§2.6) and (H-pos) **is** Weil-positivity. So the assembly
**reduces RH to an RH core** — it does not prove it. The value is the clean reduction + the
proved scaffolding. --- ## 6. Frank evaluation (the audit) **Genuinely proved (survives audit):**
- E0 (def. + identity `QW=`Weil); E4 (classical); E3 (classical, modulo E1).
- **Approximation scaffolding N0, N1, N2, N3** — solid and reusable mathematics.
- N5b (valid reduction); N5c (modulo named inputs, correct monotonicity).
- Normalization (loose end closed, Hurwitz-invariant). **Conditional / with pending proof:**
- **E1 🔧:** real-rootedness true but the **registered proof refuted by counterexample**; its own proof (Hermite–Biehler from self-adjointness) **open**. Black box: CCM Thm 1.1(iii).
- **III ⟂:** conditional on (H-gap)+(H-lim)+(H-pos), all numerical; (H-pos)=Weil-positivity.
- **H1′:** "QW is PSD" is **NOT unconditional** (= RH); PF gives structure, not positivity. **Core and open analysis:**
- **IV.2≡§V 🟥:** RH-equivalent (variational). The only RH-hard core.
- **IV.1 ⬚:** identification of the boundary operator (phenomenological 2nd-order SL) — analysis, not RH-hard. **Conclusion.** The CCM chain, audited, is an **elegant reduction of RH to a single
RH-equivalent core** (`ξ̂_λ→Ξ`, equivalent to "the Weil ground state is `Ξ_T`"), surrounded by
a **genuinely proved approximation scaffolding** (N0–N3) and with three frank repairs still
pending (own proof of E1; rigor of the frame deficit `g₀→Ξ_T`; correction of H1′). Weil
positivity (=RH) appears, after audit, **distributed** across H1′, `/ε_0` (III), and
the IV.2 core. **RH is not proved; it is localized with precision, without self-deception.** --- ### Appendix — pending repairs (real mathematics, not RH-hard except the core)
1. **Own E1:** Hermite–Biehler for `ξ̂` from the self-adjoint realization (with boundary carrier). Would close real-rootedness without citing CCM.
2. **Frame deficit:** rigorize `g₀=Ξ_T+O(ε_0)`, `g₀→Ξ_T` (Landau–Beurling at critical density). Would close the "exactly `Ξ_T`" part of the core (RH side).
3. **IV.1:** 2nd-order boundary operator + spectrum `n²` (Landau–Widom). Would close `γ>0` and the identification.
4. **Core IV.2≡§V (RH):** the rate `o(λ^{−½})` protected by positivity — **RH**.
