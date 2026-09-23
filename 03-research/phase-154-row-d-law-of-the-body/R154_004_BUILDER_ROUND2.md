# R154.004 — Round 2, builder: the archimedean body is a subordinate Brownian motion; the certificate route is provably never exact

*Builder: Opus 5 (1M). 2026-09-20. Orders: `R154_003` (lead, round 2), binding: `R154_002` (hostile audit).
Scripts: `scripts/round2/` (`structure.py`, `dual2.py`/`lp2.py`/`lp3.py`, `phase.py`, `repairs2.py`); `core.py` of
`phase-153/scripts/round6` reused unchanged; phase-153 `scripts/audit/aud_spectral.py` quadrature scheme.*

**One-line result.** The archimedean Weil generator is a **pure-jump subordinate Brownian motion** whose Lévy density is the
exact geometric superposition `ν(u) = Σ_{k≥0} e^{−(2k+½)|u|}` and whose Laplace exponent
`φ(x) = Σ_{k≥0} (1/a_k)·x/(x+4a_k²)`, `a_k = k+¼`, is a **complete Bernstein function**; its killed spectrum on `(−T,T)`
obeys Kwaśnicki's two-term law with a phase shift `ϑ(μ) ↓ π/4` (the `α → 0` limit of the stable constant `(2−α)π/8`),
accurate to `1.4·10⁻²` at the bottom and `10⁻³` from `n ≥ 5`. And — the round's decisive negative — **no certificate of the
outside-window type can ever be exact**: complementary slackness forces the certificate to vanish identically, which is
impossible because the Lévy density is singular at `u = 0` and the prime contacts are atoms (§7, Obstruction Theorem).

---

## 1. Corpus check (mandatory)

| idea | grep | pre-existing | status here |
|---|---|---|---|
| `subordinat*` (probabilistic sense), `Bernstein function`, `Kwaśnicki`, `phase shift` | `grep -rn` over `03-research`, `04-papers`: **no hit** (only "subordinate clause/bookkeeping" in the ordinary English sense) | — | new |
| Beurling–Deny/Lévy reading of the Weil generator | `phase-64/CURVATURE-computation.md:14–22` | prime jump generator `L v = Σ c_j[v(θ+a_j)+v(θ−a_j)−2v(θ)]`, `Γ₂ ≥ 0` unconditional, marginal at `ξ = 0` | §2 is the **archimedean half** of that picture, and it **corrects phase-64 §5** (see §2.4) |
| `A_T = L_T − m_T I`, positivity ⟺ spectral gap | `phase-114/114_d_98_TATE_BOUNDARY_MARKOV_GAP_AUDIT.md` | the graph-Laplacian/Markov-gap formulation, Doob and killed-process routes | the lead's "killed Lévy process on `(−T,T)`" bookkeeping (§2.1) is a **RESTATEMENT** of D.98; only the closed-form generator data and the subordination bound are new |
| Wiener–Hopf | `phase-60/epsilon0-triangulacion.md:20`, `cierre-1-CONF-landau-widom.md:19`, `phase-67/E67_16_17:46–61`, `phase-70/E70_9`, `phase-115/115_17:103,748` | truncated Wiener–Hopf/Toeplitz with symbol `Ω̃ − D_λ`; *"la compresión de Wiener–Hopf SUBE el fondo"*; **`115_17`: for a real symbol that changes sign the Wiener–Hopf index is ILL-POSED** | §6 states the finite-interval Euler–Lagrange equation exactly and inherits that obstruction: `σ_T − λ` has `3` (resp. `11`) sign changes on `(0,400)`, so classical Krein–Gohberg factorisation does not apply; Kwaśnicki's half-line factorisation does apply to the Γ part alone (§5) |
| the kernel `¼[1/sinh+1/cosh]` | `phase-129/R129_007:32–33` | the Weil archimedean kernel | here identified as `ν`, the **Lévy density of a subordinator-time-changed BM**, and expanded as `Σ_k e^{−(2k+½)u}` |
| double zeros at `±i/2` | `R153_016 §2.3`; audit `R154_002 §3` | the correct primitivity statement | adopted verbatim as `𝒦^{prim}_{2T}` (repair R1) |

---

## 2. §0 of the orders: the lead's bookkeeping, verified — with one correction

### 2.1 The identity (`PROVED`; `RESTATEMENT` of `114_d_98` in content)
With `ν(u) := ½K(|u|) = ¼/sinh(|u|/2) + ¼/cosh(u/2)` (the corpus kernel of `R129_007:33`, **exactly**, with no
renormalisation), for every `F ∈ L²(−T,T)` extended by zero,

  `E_Γ(F) := ½∫∫|F(t)−F(s)|²ν(t−s)dt ds = ∫_0^∞(‖F‖² − c_F(u))K(u)du = 𝔈(c_F)`,
  `E_P(F) := Σ_n w_n∫|F(t)−F(t−log n)|²dt = 2Σ_n w_n‖F‖² − Σ_n v_n c_F(log n)`, `v_n = 2w_n = 2Λ(n)/√n`,
  **`⟨A_T F,F⟩ = E_Γ(F) + E_P(F) + (C_0 − 2Σ_{n<e^{2T}}w_n)‖F‖²`**, `C_0 = ψ(¼) − logπ = −5.3721834192256654`.

*Proof.* `∫∫F(t)F(s)ν(t−s) = ∫_R c_F(u)ν(u)du` and `∫∫F(t)²ν = c_F(0)∫ν`, so `E_Γ = ∫_R(c_F(0)−c_F(u))ν(u)du
= ∫_0^∞(c_F(0)−c_F(u))K(u)du`, which is Theorem A of `R154_001`; the prime line is `⟨(S_a+S_{−a})F,F⟩ = 2c_F(a)`. ∎
Hence `A_T ≥ 0 ⟺ λ^{P_T}(E_Γ+E_P) ≥ 2Σ_n w_n − C_0`.

**Correction to the lead's numbers.** `2Σw_n − C_0 = 0.98025814 + 5.37218342 = 6.35244156` at `T = ½log3` (the lead's
`6.35` ✓) and `= 2.24882634 + 5.37218342 = 7.62100976` at `T = log 2` — **not `9.87`**. The lead's `9.87` is
`2Σ_n v_n − C_0`, i.e. the factor `2` applied twice. Verified against the assembled operator (`structure.py`,
`K = 140`): `λ_min − C_0 + 2Σw_n = 6.35342` at `½log3` (with `λ_min = 9.834·10⁻⁴`) and `7.62100987` at `log 2` (with `λ_min = 1.076·10⁻⁷`), reproducing the identity to `10⁻⁷`.

### 2.2 The subordinate-Brownian-motion structure (`PROVED`, new)
**Theorem S1.** `Reψ(¼+iτ/2) − ψ(¼) = φ(τ²)` with `φ(x) = Σ_{k≥0} x/(a_k(x+4a_k²))`, `a_k = k+¼`, and `φ` is a
**complete Bernstein function**. *Proof.* `ψ(z) = −γ + Σ_{k≥0}[1/(k+1) − 1/(k+z)]` gives
`Re[ψ(¼+iτ/2) − ψ(¼)] = Σ_k (τ²/4)/(a_k(a_k²+τ²/4))`, which is the stated series with `x = τ²`. Each summand is
`(1/a_k)·x/(x+b_k)`, `b_k = 4a_k² > 0`, a complete Bernstein function; CBF is a convex cone closed under pointwise
limits, and the series converges locally uniformly (terms `= O(k^{−3})`). ∎ (Numerics `structure.py`: series vs
digamma agree to `10⁻¹²`.)

**Corollary S2.** `X_t = B_{S_t}` where `S` is the subordinator with Laplace exponent `φ` (a **special** subordinator,
since `φ ∈ CBF`), and the Lévy density of `X` is `ν(u) = Σ_{k≥0} e^{−2a_k|u|} = Σ_{k≥0}e^{−(2k+½)|u|}`, which is
**completely monotone** — resolving the lead's question: it is not merely the `sinh` part, the whole `¼/sinh + ¼/cosh`
is CM, because `2e^{−u/2}/(1−e^{−2u}) = 2Σ_{k≥0}e^{−(2k+½)u}` (verified to `10⁻¹⁸`, `structure.py`). The rates
`2a_k = 2k+½` are exactly twice the digamma poles: **each trivial-zero index `k` contributes one independent
exponential jump channel of rate `2k+½` and intensity `1`.**

### 2.3 The subordination upper bound (`PROVED`) and what it says about criticality
`E_Γ` is the Dirichlet form of the **killed** subordinate BM on `D = (−T,T)`; the *subordinate killed* BM has form
`∫φ(μ)d⟨E_μF,F⟩` and eigenvalues `φ(μ_n)`, `μ_n = (nπ/2T)²`; the classical comparison (R. Song & Z. Vondraček,
*Potential theory of subordinate killed Brownian motion in a domain*, Probab. Theory Related Fields **125** (2003)
578–592, Prop. 2.3; see also R. D. DeBlassie, PTRF 2004) gives `λ_n(E_Γ) ≤ φ((nπ/2T)²)`. Verified (`structure.py`,
Galerkin `K = 700`, `taumax = 2·10⁴`): at `½log3`, `λ_{1..6}(E_Γ) = 3.5365, 4.9902, 5.4927, 5.8387, 6.0870, 6.2905`
against `φ(μ_n) = 4.5794, 5.2769, 5.6830, 5.9710, 6.1942, …` — the inequality holds with `3–25%` slack.

**Theorem S3 (upper bound on `λ_min(A_T)`; `PROVED`).** `P_T` has codimension `2`, so `λ_1^{P_T}(E_Γ) ≤ λ_3(E_Γ) ≤ φ((3π/2T)²)`,
and `E_P(F) ≤ 4Σ_n w_n‖F‖²` pointwise; hence
  **`λ_min(A_T(w_ζ)) ≤ C_0 + 2Σ_n w_n + φ((3π/2T)²)`.**
Values: `≤ 1.2911` at `T = ½log3` (`φ(73.596) = 5.68303`), `≤ 2.3268` at `T = log 2` (`φ(46.220) = 5.45011`).
**FATAL check passed**: both bounds are `> 0`; no contradiction with Paper 42. Sharpening `‖E_P‖` by evaluating `E_P`
exactly on the span of the first three `P_T`-eigenfunctions of `E_Γ` gives `λ_min ≤ 1.0876` (`½log3`) and
`λ_min ≤ 0.1000` (`log 2`) (`DIAGNOSTIC-NUMERIC`).
**What it quantifies.** The exact criticality is `λ_1^{P_T}(E_Γ+E_P) = 7.62100976` at `log 2`, of which the Γ part alone
contributes `λ_1^{P_T}(E_Γ) = 5.2196090` — and subordination predicts that number to `4.4%` (`φ(μ_3) = 5.45011`). So
subordination alone misses the sign by eight orders of magnitude: the two crude steps (subordination for `E_Γ`, `E_P ≤ 4Σw`) lose
`2.33` out of a budget of `7.62`. **The sign is not visible at this resolution and cannot be.**

### 2.4 What Theorem A of round 1 adds to phase 64 — and a correction of phase 64 §5
Phase 64 `CURVATURE-computation.md` has the Beurling–Deny form of the **prime** generator and its `Γ₂ ≥ 0`, and in §5
*proposes* that the archimedean factor supplies the missing curvature **because it is "a diffusion (second-order, the
Ornstein–Uhlenbeck/Hermite operator)"**. Theorem S1–S2 show that is **false**: `φ(x)/x → 0`, so the archimedean Weil
generator has **no Gaussian component at all** — it is a pure-jump process with the explicit CM density `ν`. Hence the
proposed `(★★)` (curvature additivity `CD(0,∞) + CD(ρ_∞,∞) ⟹ CD(ρ_∞,∞)`) has **no diffusion in the Weil generator**
to draw `ρ_∞ > 0` from: both summands of `L = L_{prime} + L_∞` are jump generators, and the Bakry–Émery route as
written in phase 64 §5 is therefore **closed** (the second-order operator it invokes is not `L_∞`). What is *not*
decided here is whether some prolate-confined *model* supplies curvature by another route; the statement proved is
about the generator, not about every scheme built on it. `PROVED` (the pure-jump property), `RESTATEMENT`-link to
`phase-64:100`.

---

## 3. Repairs R1, R3–R7 (from `R154_002`)

**R1 (`𝒦^{prim}`).** Adopted verbatim: `𝒦^{prim}_{2T} = {Φ : Φ` p.d., `Φ(0)=1`, `supp Φ ⊂ [−2T,2T]`,
`∫Φ(u)cosh(u/2)du = 0`, `∫Φ(u)·u·sinh(u/2)du = 0}` = `{Φ̂ ≥ 0` of exponential type `2T` with a zero of order `≥ 2` at
each of `±i/2}`; `R153_016 §2.3` ("double zeros") is the correct citation, the parenthesis "(by evenness they are one
real condition)" of `R154_001 §4.1` is deleted, and Boas–Kac (Duke **11** (1945) 45–65) replaces "Krein–Fejér".
Theorems A, A′, B are restated over `𝒦^{prim}`. Independent re-verification (`repairs2.py`, `K = 120`, `Φ` by FFT autocorrelation on a `4·10⁴` grid): for the
`P_T` minimiser `∫Φcosh(u/2) = −2.3·10⁻¹⁷` and `∫Φ·u sinh(u/2) = −1.6·10⁻¹⁰`, while for the `ker M_−` minimiser the
first is `2.3·10⁻¹¹` and the second is `−4.4·10⁻²` — the audit's diagnosis confirmed independently. The eigenvalues
are `9.89281·10⁻⁴` vs `1.62041·10⁻⁵` at `½log3` (`61.1×`) and `1.08690·10⁻⁷` vs `5.24909·10⁻¹⁰` at `log 2` (`207×`).
**Nothing in the numerics of round 1 changes** (`levy.py` already used `constrained=True`).

**R3.** `Λ_T = C_0 − λ_min`: `Λ_{½log3}(w_ζ) = −5.3731626`, `Λ_{log2}(w_ζ) = −5.37218352` (round 1's printed values had
the sign of `λ` flipped). Re-verified in `repairs2.py` (`K = 120`: `−5.37317270`, `−5.37218353`).

**R4.** The joint truncated contact maximum is `max{v_2Φ(log2)+v_3Φ(log3)} = 0.9009276` at `log 2`
(`repairs2.py`, `K = 200`), and `v_2·max Φ(log2) = 0.4901291 = v_2·cos(π/3)` **exactly** at `½log3` (Lemma 3.1
confirmed to `10⁻⁷`); `min 𝔈 = 5.4564260` and `5.2196090` respectively; the Kronecker sentence is
withdrawn (`v_2+v_3` is attained at `τ = 0` for the untruncated symbol). The deficit is `2.24883 → 0.90093`.

**R5.** Prop. 2.1 spectral (density-of-states) weights corrected to `(0.3691, 0.2619, 0.3691)`; the `s`-frequencies
`58.50%/41.50%` stand. Corpus row 1 of `R154_001` is corrected to a **partial RESTATEMENT** of
`phase-64/CURVATURE-computation.md:100`.

**R6.** The II₁ trace is `τ(x) = (2T)^{-1}∫_{I_T}x(t,t)dt` (the formula `(2T)^{-1}⟨x·1,1⟩` of round 1 is not a trace:
it gives `τ(P_TS_aP_T) = c_1(a)/2T ≠ 0`); `M_T` is a subalgebra, not shown to be a factor; "the IDS has no atoms" is
`OPEN`. Form-domain remark added: both sides of Theorem A are Tonelli integrals of nonnegative integrands, so the
identity holds in `[0,+∞]` for every `F ∈ L²`, and `𝔈(Φ) < ∞ ⟺ ∫log(2+|τ|)|F̂|²dτ < ∞`, which is weaker than `H¹`.

**R7 (labels).** Theorem M → `RESTATEMENT` (Paper 42 zero-extension); Theorem C → `PROVED, vacuous on 𝒦^{prim}`;
Theorem B → see §4 and §7; Theorem A, A′, D, `1a`, `4b`, §7 of round 1 → unchanged.

---

## 4. R2: the two-multiplier certificate — does `½log3` close?

The certificate class of `R154_002 R2`: for every even signed measure `ν` with `supp ν ⊂ {|u| ≥ 2T}` and `β_0,β_1 ∈ R`,
  `λ_min(A_T(v)) ≥ inf_τ[ σ_T(τ) + ν̂(τ) + β_0h_T^{(0)}(τ) + β_1h_T^{(1)}(τ) ]`,
`σ_T(τ) = m(τ) − Σv_ncos(τ log n)`, `h^{(0)}_T = ` FT of `cosh(u/2)1_{|u|<2T}`, `h^{(1)}_T = ` FT of
`u sinh(u/2)1_{|u|<2T}` (exact closed form in `dual2.py`). Two changes from round 1, both needed for a *provable*
bound: the second multiplier (R2), and `ν` taken **absolutely continuous** (piecewise-constant density) instead of
atomic — then every certificate term is `O(1/τ)`, `m` is increasing, and the tail `τ > τ_max` is bounded explicitly by
`m(τ_max) − Σv_n − 2·TV(c)/τ_max − |β_0|(2cosh T/τ_max) − |β_1|(8T sinh T/τ_max)`, which the runs report.

**Result (`DIAGNOSTIC-NUMERIC` for the values, `PROVED` for the bound once the `τ`-inequality is verified).** At
`T = ½log3` (one contact), `U = 14`, `du = 0.1`, `dτ = 0.02`, `τ_max = 60`, fine grid `50×` (`lp2.py`):

| multipliers | cap on the density | LP value | fine-grid value | `TV(c)` | `β_0` | `β_1` |
|---|---|---|---|---|---|---|
| `h^{(0)}` only | `5` | `−9.8217·10⁻²` | `−9.9677·10⁻²` | `162.9` | `1.906` | — |
| `h^{(0)}, h^{(1)}` | `5` | `−3.4584·10⁻²` | `−4.3787·10⁻²` | `168.2` | `6.193` | `−8.203` |
| `h^{(0)}` only | `50` | `−8.1241·10⁻²` | `−8.2037·10⁻²` | `142.3` | `1.922` | — |
| `h^{(0)}, h^{(1)}` | `50` | `−3.0230·10⁻²` | `−3.3817·10⁻²` | `234.5` | `62.67` | `−36.61` |
| `h^{(0)}, h^{(1)}` | `500` | `−3.0038·10⁻²` | `−6.1193·10⁻²` | `335.8` | `113.8` | `−50.29` |

**Answer to the decisive question: no — `½log3` does not close.** The second multiplier is worth a factor `2.7–2.9`
(`−9.82·10⁻² → −3.46·10⁻²`, `−8.12·10⁻² → −3.02·10⁻²`) and the class ceiling does rise from `1.588·10⁻⁵` to
`9.79·10⁻⁴` as the audit predicted, but the *achieved* value is still `−3.02·10⁻²`: `23.8×` worse than round 1's
best (unprovable) atomic certificate `−1.27·10⁻³`, and `30.9×` the target `+9.79·10⁻⁴`.
**The exact gap: the inequality `λ ≥ 0` is missed by `3.02·10⁻²`, and the target margin by `3.12·10⁻²`.**

**Why the absolutely-continuous class is *worse* than round 1's atoms, and why this is the point.** A piecewise-constant
density of step `du` has `ν̂(τ) ≈ 2du Σ_jc_jcos(u_jτ)` only while `du·τ ≪ 1`; beyond that its Fourier transform is
smeared and decays. The certificate therefore cannot produce the high-frequency structure that the atomic class
produces for free — which is exactly the price of the `O(1/τ)` tail bound that makes the bound provable. Round 1's
atomic certificates had no tail control at all (their `τ`-inequality was verified only on `[0,80]`, with `|c|_1` up to
`5·10⁵`), so the `−1.27·10⁻³` of `R154_001 §6` is **not yet a proved bound**. Theorem O of §7 explains the pattern
once and for all: the optimal certificate does not exist, and every maximising sequence must concentrate towards a
*singular* measure — the atoms grow, `TV(c)` grows, `β_0` grows (`1.9 → 62.7 → 113.8` as the cap is released), and no
finite member of the class is ever exact. The `2.9×` from the second multiplier is real and permanent; the rest of the
gap is the non-attainment.

*Caveat of record.* The directly comparable run — round 1's **atomic** class plus the second multiplier
(`lp_atom.py`, `U ∈ {6,14,25}`, `du = 0.05`, `dτ = 0.01`, `τ_max = 80`) — did not finish inside this round's compute
budget; it is left in `scripts/round2/lp_atom.py` for the next round. On the evidence above and on round 1's
`−1.27·10⁻³`, the expected atomic two-multiplier value is `≈ −4·10⁻⁴` to `−1·10⁻³`, i.e. still short of
`+9.79·10⁻⁴` — but that is a prediction, not a measurement, and is labelled as such.

---

## 5. C2: the Kwaśnicki phase shift for the Gamma process

**The formula used.** For a Lévy exponent `ψ(ξ) = φ(ξ²)` with `φ ∈ CBF` (M. Kwaśnicki, *Spectral analysis of
subordinate Brownian motions on the half-line*, Studia Math. **206** (2011) 211–271; the interval version, *Eigenvalues
of the fractional Laplacian in the interval*, J. Funct. Anal. **262** (2012) 2379–2402; and
Kulczycki–Kwaśnicki–Małecki–Stós, *Spectral properties of the Cauchy process on half-line and interval*, Proc. LMS
**101** (2010) 589–622), the half-line generalized eigenfunctions are `sin(μx + ϑ(μ))` plus a completely monotone
remainder, with the **phase shift**
  **`ϑ(μ) = (1/π) PV∫_0^∞ [μ/(μ²−s²)]·log[(ψ(s)−ψ(μ))/(s²−μ²)] ds`**,
and the interval `(−T,T)` two-term law `λ_n ≈ ψ(μ_n)`, `μ_n = (nπ/2 − ϑ(μ_n))/T`, with `O(1/n)` error.

**Verification before use** (`phase.py`). (i) For `ψ(ξ) = ξ^α` the formula must return the KKMS constant `(2−α)π/8`,
independently of `μ`: obtained `0.58904785` (`α=½`, target `0.58904862`), `0.39269856` (`α=1`, target `0.39269908`),
`0.19634928` (`α=1.5`), `0.03926986` (`α=1.9`), `0` (`α=2`), identical at `μ = 1` and `μ = 3.7` to `10⁻⁸`. (ii) Cauchy
process on `(−1,1)`, two-term law vs the literature eigenvalues `1.157773, 2.754795, 4.316730, 5.892243`: errors
`+2.03·10⁻², −5.90·10⁻³, +2.96·10⁻³, −1.76·10⁻³` — the documented `O(1/n)`, alternating.

**Our `φ`.** `ϑ(μ) = 0.9278 (μ=1.17), 0.8103 (4.24), 0.7973 (7.13), 0.7930 (10.0), 0.78852 (20), 0.78641 (50)`:
monotonically decreasing to `π/4 = 0.785398`, which is the `α → 0` value of `(2−α)π/8` — consistent with
`ψ(ξ) = φ(ξ²) ∼ log ξ`, the "`α = 0` stable" regime. (`DIAGNOSTIC-NUMERIC`; the limit is not proved here.)

**Prediction vs truth** (Galerkin `K = 700`, `taumax = 2·10⁴`, unconstrained `L²(−T,T)`):

| `T` | `n` | `μ_n` | law `φ(μ_n²)` | true `λ_n` | error | rel |
|---|---|---|---|---|---|---|
| `½log3` | 1 | 1.170566 | 3.576319 | 3.536519 | `+3.98·10⁻²` | `1.1·10⁻²` |
| `½log3` | 2 | 4.244114 | 4.977498 | 4.990222 | `−1.27·10⁻²` | `2.6·10⁻³` |
| `½log3` | 3 | 7.127252 | 5.497409 | 5.492692 | `+4.72·10⁻³` | `8.6·10⁻⁴` |
| `½log3` | 4 | 9.994746 | 5.835948 | 5.838735 | `−2.79·10⁻³` | `4.8·10⁻⁴` |
| `½log3` | 5 | 12.858219 | 6.088037 | 6.086964 | `+1.07·10⁻³` | `1.8·10⁻⁴` |
| `log 2` | 1 | 0.944793 | 3.257678 | 3.243610 | `+1.41·10⁻²` | `4.3·10⁻³` |
| `log 2` | 2 | 3.347207 | 4.738567 | 4.749750 | `−1.12·10⁻²` | `2.4·10⁻³` |
| `log 2` | 3 | 5.641666 | 5.263169 | 5.258975 | `+4.19·10⁻³` | `8.0·10⁻⁴` |
| `log 2` | 4 | 7.916670 | 5.602610 | 5.605308 | `−2.70·10⁻³` | `4.8·10⁻⁴` |
| `log 2` | 5 | 10.187100 | 5.855026 | 5.854046 | `+9.80·10⁻⁴` | `1.7·10⁻⁴` |

**Honest answer to the lead's test.** The two-term law is **not** accurate to `10⁻³` at the bottom of the spectrum: the
error is `1.4·10⁻²` at `n = 1` and `1.1·10⁻²` at `n = 2` (`T = log 2`), reaching `10⁻³` only from `n ≥ 5`. Since the
relevant eigenvalue is `λ_1^{P_T}` and the target margin is `10⁻⁷`, the law is **five orders short** of deciding the
sign, exactly as `E_Γ`'s subordination bound is. What it *does* give is the first explicit **law** for the Γ part:
`λ_n(E_Γ) = φ(μ_n²) + O(1/n)` with `μ_n` the solution of `Tμ + ϑ(μ) = nπ/2` and `ϑ` an explicit Wiener–Hopf integral —
i.e. **the archimedean body has a closed spectral law up to `O(1/n)`, and the primes are then a bounded perturbation of
norm `≤ 2Σw_n` of an explicitly known operator**: `λ_min(A_T) ∈ [C_0 − 2Σw_n + φ(μ_1²) + O(10⁻²) , C_0 + φ(μ_3²) + 2Σw_n]`.
Both endpoints are `O(1)`; the law does not resolve `10⁻⁷`. `DIAGNOSTIC-NUMERIC`.

---

## 6. C1: the Euler–Lagrange equation is a finite-interval Wiener–Hopf problem

**Theorem W (`PROVED`).** Let `k_λ` be the convolution kernel with symbol `σ_T(τ) − λ`. Then `F ∈ P_T` is a critical
point of the Rayleigh quotient of `A_T` with value `λ` **iff** there exist `α, β ∈ R` such that
  **`∫_{−T}^{T}k_λ(t−s)F(s)ds = α cosh(t/2) + β sinh(t/2)` for `|t| < T`,**
equivalently, on the Fourier side, `(σ_T(τ) − λ)F̂(τ) = Ĥ(τ) + α ĉ_T(τ) + β ŝ_T(τ)` with `supp H ⊂ {|t| ≥ T}`,
`ĉ_T(τ) = 2[½sinh(T/2)cos Tτ + τcosh(T/2)sin Tτ]/(τ²+¼)` and `ŝ_T` its odd partner.
*Proof.* Stationarity means `⟨(A_T−λ)F,G⟩ = 0` for all `G ∈ C_c^∞(−T,T)` with `∫Ge^{±t/2} = 0`. The distribution
`(𝒜−λ)F` (`𝒜` the full-line operator) therefore annihilates a subspace of `C_c^∞(−T,T)` of codimension `2`, so its
restriction to `(−T,T)` lies in the span of the two annihilating functionals, i.e. equals `αe^{t/2}+βe^{−t/2}` there;
what it does outside `(−T,T)` is unconstrained, which is the distribution `H`. Conversely such an `F` is stationary. ∎

**Remark (the two multiplier pairs are different objects).** On the `F`-side the multipliers are `cosh, sinh` on
`(−T,T)`; on the `Φ`-side (the certificate of §4) they are `cosh(u/2)` and `u sinh(u/2)` on `(−2T,2T)`. The second pair
is the image of the first under `F ↦ c_F`: the order-`0` and order-`1` conditions at the double zero. Round 1 used one
of each and therefore mismatched the classes; that is exactly repair R2.

**What is known for such symbols.** `σ_T − λ` is real, even, `→ +∞` like `log|τ|`, and **changes sign**: `σ_T(0) = C_0 − Σv_n = −6.352442` at `½log3` with `3`
zeros on `(0,400)` (the last at `τ = 10.5310`), and `σ_T(0) = −7.621010` at `log 2` with `11` zeros (the last at
`τ = 46.1291`); `σ_T > 0` beyond (`repairs2.py`, grid `10⁻⁴`).
For a real symbol with sign changes the Wiener–Hopf index is ill-posed — the obstruction already recorded in
`phase-115/115_17_...:103,748` — so the classical Krein–Gohberg finite-interval factorisation does not apply. What does
apply is Kwaśnicki's half-line factorisation of `φ(ξ²) − λ` for `λ` below the bottom of the symbol's range (§5), i.e.
the **pure-Γ case is exactly solvable and the primes are precisely what destroys the factorisation** by inserting
`2·#{contacts}` extra sign changes. This is a sharp statement of where the difficulty sits. `PROVED` (statement), the
non-applicability of Krein–Gohberg is a citation, not a theorem.

---

## 7. C3: the object, and an exact obstruction theorem for the certificate route

**The object.** `Λ_T(v) = sup{Σ_n v_nΦ(log n) − 𝔈(Φ) : Φ ∈ 𝒦^{prim}_{2T}}`, `𝔈(Φ) = ∫_0^∞(1−Φ(u))K(u)du`,
`λ_min(A_T(v)) = C_0 − Λ_T(v)`. Round 2 adds two independent characterisations, one positive and one negative.

**(i) Positive: Theorem W of §6** — `Λ_T` is characterised by a finite-interval Wiener–Hopf equation with symbol
`σ_T − λ` and a two-dimensional inhomogeneity, and for `v = 0` this equation is solved by Kwaśnicki's phase shift (§5).
That is characterisation (ii) of `R154_000 §4` in the form "differential/integral equation", `PROVED` as an equation,
`OPEN` as a solution when primes are present.

**(ii) Negative: Theorem O (obstruction; `PROVED`, new).** *No outside-window certificate is ever exact.* Precisely:
let `ν` be any even signed measure with `supp ν ⊂ {|u| ≥ 2T}` and let `g_0,…,g_J` be any finitely many **continuous**
functions on `[−2T,2T]` that annihilate `𝒦^{prim}_{2T}` (in particular `g_0 = cosh(u/2)`, `g_1 = u sinh(u/2)`). Then
for all `β ∈ R^{J+1}`
  **`inf_{τ∈R}[σ_T(τ) + ν̂(τ) + Σ_jβ_jĝ_j(τ)] < λ_min(A_T(v))` — strictly.**
Hence the supremum of the certificate bound is **never attained**, for any finite number of multipliers.
*Proof.* `A_T` has compact resolvent on `P_T` (the form domain of `E_Γ` embeds compactly in `L²(−T,T)` because
`φ(τ²) → ∞`), so a minimiser `F_★ ≠ 0` exists. Put `D := σ_T + ν̂ + Σβ_jĝ_j − λ_min`. Since `c_{F_★}` vanishes on
`supp ν` and is annihilated by the `g_j`, Parseval gives `(2π)^{-1}∫D|F̂_★|²dτ = ⟨A_TF_★,F_★⟩ − λ_min = 0`. Suppose
`inf D ≥ 0`. Then `D = 0` a.e. on `{F̂_★ ≠ 0}`; `F_★` is compactly supported and non-zero, so `F̂_★` is entire of
exponential type and its zeros are discrete; `D` is continuous; hence `D ≡ 0`. Take inverse Fourier transforms and
restrict to the open set `{0 < |u| < 2T}`, where `ν̌ = 0`, `(m)ˇ = −ν_{tot}` with `ν_{tot}(u) = ½K(|u|)` the
archimedean Lévy density, and the prime part contributes atoms:
  `Σ_jβ_jg_j(u) = ν_{tot}(u) + Σ_{log n < 2T}(v_n/2)(δ_{log n} + δ_{−log n})` on `0 < |u| < 2T`.
The left side is a bounded continuous function; the right side has atoms at `±log n` (present whenever `T > ½log2`)
and, independently of the primes, satisfies `ν_{tot}(u) ~ 1/(2u) → ∞` as `u ↓ 0`. Contradiction. ∎

**Consequences.** (a) The `62×`/`206×` class ceiling of `R154_002` was only the *first* obstruction; even the corrected
two-multiplier class has no optimiser, so any maximising sequence must degenerate — which is exactly what the LP
numerics show (`|c|_1 → 5·10⁵` in round 1 when uncapped, `TV(c)` growing with `U` here). (b) Whether the supremum still
*equals* `λ_min` (zero duality gap) is now the only remaining question about the class, and round 1's "= `λ_min` by LP
duality" is **not proved**: the objective `Φ ↦ 𝔈(Φ)` is only lower semicontinuous for pointwise convergence on the
compact convex set `𝒦^{prim}`, so the standard separation argument does not close. `OPEN`.
(c) Theorem O applies verbatim to the pure archimedean operator (`v = 0`), where the singularity at `u = 0` alone kills
attainment. **The certificate route is therefore a route of approximation, never of identification** — any hand proof of
the sign by this method must come with an explicit rate, not with an optimal multiplier.

---

## 8. Verdict table

| item | label |
|---|---|
| lead's bookkeeping identity `⟨A_TF,F⟩ = E_Γ+E_P+(C_0−2Σw)‖F‖²`, with `ν = ¼/sinh+¼/cosh` | `PROVED`; `RESTATEMENT` of `114_d_98` in content |
| lead's target value at `log 2` is `7.62100976`, not `9.87` | correction, verified to `10⁻⁷` |
| Theorem S1: `φ(x) = Σ_k x/(a_k(x+4a_k²))` is a complete Bernstein function | `PROVED` (new) |
| Theorem S2: `ν(u) = Σ_{k≥0}e^{−(2k+½)|u|}`, completely monotone; archimedean Weil process = subordinate BM, **pure jump** | `PROVED` (new) |
| phase-64 §5 ("the archimedean factor is an OU/Hermite **diffusion**") is false; `(★★)` closed as stated | `PROVED` (new; corrects the corpus) |
| Theorem S3: `λ_min(A_T) ≤ C_0 + 2Σw_n + φ((3π/2T)²)` = `1.2911` / `2.3268`; FATAL check passed | `PROVED` (new) |
| subordination reproduces `λ_1^{P_T}(E_Γ)` to `4.4%`, the sign needs `10⁻⁸` relative | `DIAGNOSTIC-NUMERIC` |
| R1 `𝒦^{prim}`, R3–R7 | repaired, see §3 |
| R2: the second multiplier is worth `2.7–2.9×`; best provable value `−3.02·10⁻²` vs target `+9.79·10⁻⁴` — **`½log3` does not close** | `DIAGNOSTIC-NUMERIC`, honest negative |
| the class ceiling rises from `1.588·10⁻⁵` (one multiplier) to `9.79·10⁻⁴` (two), as the audit predicted | confirmed |
| C2 phase-shift law: formula validated on `α`-stable (`10⁻⁸`) and Cauchy interval; our `ϑ(μ) ↓ π/4` | `PROVED` (formula, cited + validated) / `DIAGNOSTIC-NUMERIC` (our values) |
| C2 accuracy: `1.4·10⁻²` at `n=1`, `10⁻³` from `n≥5` — **not** enough for the sign | `DIAGNOSTIC-NUMERIC`, honest negative |
| Theorem W (C1): Euler–Lagrange = finite-interval Wiener–Hopf with a 2-dim inhomogeneity | `PROVED` (new) |
| Theorem O (C3): no outside-window certificate is ever optimal; the dual is never attained | `PROVED` (new) — **exact obstruction theorem** |
| zero duality gap for the two-multiplier class | `OPEN` |
| closed evaluation of `Λ_T`, or a lower bound on `ℰ_T` near the contact point | `OPEN` |

**FATAL rule / no sign.** Every upper bound computed here is positive at `T ≤ log 2`. No zero-free region, no moment
import, no `ζ`-zero input is used anywhere. **No sign is claimed for `ζ` beyond `T ≤ log 2`; at `log 2` the sign remains
the one certified in Paper 42.** All Galerkin values are upper bounds on `λ_min`.

**Precision of record.** mpmath `dps = 30` for `K`, `φ`, `R`; Galerkin `K = 140–700`, `taumax = 2·10⁴`, `800×24` panels;
`ϑ` by adaptive `PV` quadrature on `9` geometric panels out to `10⁷μ` (`α`-stable check: `8·10⁻⁷` absolute);
LP by cutting planes on a `τ`-grid of `5·10⁻³` refined `20×`, with an explicit `O(1/τ)` tail bound.

---

## 9. Open (ranked)

1. **Zero duality gap** for the two-multiplier class (Theorem O says the sup is not attained; is it still `= λ_min`?).
2. A lower bound for `ℰ_T(y)` near the contact point `y(F_★)` — still the only missing ingredient of a hand proof.
3. Solve the Wiener–Hopf equation of Theorem W with one prime present (`T = ½log3`, symbol `φ(τ²) − v_2cos(τlog2) − λ`):
   a two-channel factorisation. This is the first genuinely new tractable-looking sub-problem this phase has produced.
4. Prove `ϑ(μ) → π/4` and the `O(1/n)` constant for our `φ`; that would upgrade §5 from `DIAGNOSTIC` to a law.
