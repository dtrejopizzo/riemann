# R155.005 — Reverse-engineering the closing weight `w_T` from the known zeros

* REVERSE-ENGINEERING track of phase 155. the idea: "we know the zeros up
to height 3·10¹² are on the line; use that known truth as training data: reverse-engineer what the
closing object `D` must look like for the first windows and find the pattern."*
*Inherits Paper 47 §7 (Theorem Z, Cor. 7.4 flat-kernel criterion), §5 (the 437-atom certificate at
`½log3`), §8.2 (the three scales), and `R155_003` (Theorem TK).*
*Scripts and data: `scripts/reverse/` (README with exact commands and runtimes).*
**Every number in this file is `DIAGNOSTIC`. Nothing here is a statement about RH, and nothing here
claims a sign for any `T > log 2`.**

## §0 Verdict (five lines)

1. The experiment runs and Theorem Z is confirmed numerically: for a C¹ flat-top `w` [amended
 per R155_010: the `t_sanity` weight is C¹, not C² — R155_006 §1], the zero side
 `Σ_γ ŵ(τ−γ)` and the prime/Γ side of `(7.2)` agree to `1.4·10⁻⁸` — the first numerical
 verification of Theorem Z in the corpus.
2. **The reverse-engineered `w_T` has no arithmetic structure.** At a bounded mass budget the optimal
 weight is a single smooth monotone shoulder decaying from `1` at `2T` to `0` over `≈ 4` units of `u`;
 no `log p` spacing, no comb, nothing that the primes could be read off from.
3. **It is not stable, and the one positive value it produces is fictitious — but the diagnosis is
 corrected. [amended per R155_010, R155_006 §3]** Pushing the LP value up to the class
 optimum destroys the shape: `‖w‖_∞` grows from `1` to `2.6·10²` while the value moves by `1.7·10⁻⁴`.
 The `+1.4·10⁻⁶` value is **not** refuted by the prime-side evaluation as originally diagnosed: the
 quoted `min f^{prime} = −8.7·10⁻⁵` gap is an artefact of Gauss–Legendre quadrature order, not a
 genuine sign disagreement (R155_006 §3 traces `max|f_zero−f_prime|` to GL order directly). The value
 dies instead **on the grid itself**: a fine-grid scan finds `f(16.745) = −1.72`, far below the
 coarse grid point `f(16.74) = +1.39·10⁻⁶` that the LP reports as active — the "positive value" is a
 grid artefact of the same kind Paper 47 §5/§6 already warn about, not a prime-side refutation. Even
 the tame weight's grid value `−1.68·10⁻⁴` is worth `−9.79·10⁻³` on the fine grid (factor `58`). This
 is Theorem O (non-attainment) made visible in the *weight*, not just in the measure. Note also that
 `L` (the mass budget) is **basis-dependent**, not an intrinsic scale of `w`, and the archived negative
 control uses the `s ≥ 1.5` weight class, not the class of Theorem E.
4. **"There is no law in `T`" is WITHDRAWN as stated. [amended per R155_010, R155_006 §6]**
 `c(T)` (LP value on the `τ`-grid over `[0,τ_env]`, mass budget `L=100`; an over-estimate by §3) is
 `−5.4·10⁻⁷, −2.35·10⁻², −2.64·10⁻², −2.62·10⁻², −3.17·10⁻², −4.29·10⁻², −8.57·10⁻²` at
 `T = ½log3, 0.58, 0.62, 0.65, log2, 0.75, 0.80`: a **step** at the entry of the prime `3`
 (`τ_env` jumps `16.7 → 59.5`), a plateau while `N_T = {2,3}`, and a second drop after `4` enters.
 The original extrapolation test straddled a prime entry, which is what made it fail; a fair
 **in-regime** test (train on `{0.58,0.62,0.65}`, all `N_T={2,3}`, test at `log2`, same regime) *does*
 fit: profile residual `1.3·10⁻²`, predicted-profile error `4 %` at the next window. **A law does
 exist within a prime regime.** What fails is the transfer of the *value* — a `4 %` profile error
 costs a factor `7` in `inf f`, a conditioning statement about the value functional, not a
 non-existence-of-law statement. Across a prime entry even the profile law breaks (residual `0.57`),
 because the training set there straddles the step.
5. [amended per R155_010: the quasi-positive reading here ("the zeros alone bring `c` to
 within `10⁻⁶` of zero") is DELETED — R155_006 §9 flags it as a near-certificate misreading that
 §3–§4 void; see §3.1 for the correct diagnosis of that value.] What this teaches is where the
 difficulty sits: at `½log3` the whole verification interval `[0, 2πe^{A_T}] = [0,16.75]` lies
 **below** the resolution scale `2πe^{2T} = 18.85`; from `T = 0.58` on, `τ_env = 59.5 > 2πe^{2T} ≈ 20`
 and the class must control the *density* regime, where every class we could afford fails by two
 orders of magnitude. That crossing, not the size of `T`, is the wall.

## §1 Corpus check and the zeros

### 1.1 Corpus check (`grep -rin` over `03-research`, `04-papers`, `scripts`)

| term | hits | reading |
|---|---|---|
| `Odlyzko` | `phase-25-lower-bounds-bj-audit/01-audit-classical.md:192`, `phase-29-zeta-spectral-triples/37-doc-37-connection-with-random-matrix-theory.md:37`, `phase-28-four-fronts/04-front-D.md:32`, `phase-33-dbn/74:205`, `phase-37-physics/109:130`, `04-papers/12-.../main.tex:37` (`\nocite{bgOdlyzko}`), and **`phase-114/114_e_00_counterfactual_harness.py:86`** ("primeras alturas de ceros de zeta (Odlyzko); suficientes para un modelo finito") | all are *citations of GUE/pair-correlation evidence* or a finite counterfactual model. **No prior use of a zero table as training data for a dual certificate.** |
| `zetazero` | `phase-118/scripts/W5_cache_zeros.py`, `W0_weil_identity.py:102`, `phase-7-weil-carleson-sine-kernel/experiments/second_order_*.py` | `mpmath.zetazero` caching; `phase-118 W5` is the **closest precedent**: "verify `⟨A_T F,F⟩ = Σ_ρ h(γ_ρ)` numerically to 8+ digits against real zeta zeros". That is an identity check of the *primal* form; it is not an optimisation over `w`. |
| `Platt` | `phase-118/PROOF_ARCHITECTURE.md:155`, `scripts/W5_partB_bound.py` (`H_VERIFIED = 3.0000175e12`), `phase-104/104_00`, `104_03:214`, `104_66:69` | the verified-RH height is already in the corpus, and `104_03:214` already records the correct caveat ("Platt–Trudgian permite afirmar que los ceros hasta `H` yacen sobre la recta; no hace …"). |
| `known zeros` / `ceros conocidos` | `phase-71/E71_4:71`, `E71_5:9–13`, `phase-4/00-PROOF-LOG.md:168` (Theorem C NO-GO: "Zero-side `K` presupposes the unknown zeros (circular as tool)"), `phase-136/MAP_1:141` (ES-2) | **the corpus already contains the no-go this track must respect**: a zero-side object used as a *tool* is circular. Our LP is therefore explicitly labelled a *diagnostic training experiment*, never a proof step. |
| `smoothed counting` | none | — |
| `flat-top` | only phase 154/155 and Paper 47 | this track is new. |

Conclusion of the corpus check: the *idea* (use the verified zeros) appears twice as a caveat and once
as an identity check; the *experiment* (optimise a flat-top weight against a zero table and read the
shape) is not in the corpus. The circularity no-go (`phase-4`, `ES-2`) is respected by labelling.

### 1.2 The zeros

Odlyzko's table of the first `100 000` zeros,
<https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1>, downloaded,
`md5 b7b8be60df6d46e78cd60874f9fd76c0`, 1 800 000 bytes, archived as `scripts/reverse/zeros1.txt`.
Ordinates `γ_n` to 9 decimals: `γ_1 = 14.134725142`, `γ_100000 = 74920.827498994`.
Precision `≈ 10⁻⁹` per entry; no other precision is claimed. `mpmath.zetazero` was **not** needed.

## §2 The LP over `w` and its results

### 2.1 What is optimised, and what it never sees

`w ∈ W_T` is parametrised as `w ≡ 1` on `[−2T,2T]` and, for `u > 2T` (even extension),

```
w(u) = Σ_{i=1..4} y_i ψ_{s_i}(u−2T) + Σ_{j} x_j β((u − u_j)/h),
ψ_s(v) = (1 + s v + ½ s² v²) e^{−s v}, s ∈ {2.5, 4, 8, 16},
β = cardinal cubic B-spline (C², support 4h, ∫ = h), u_j = 2T + j h, h = 2T/M, j ≥ 2.
```

`ψ_s(0)=1`, `ψ_s'(0)=ψ_s''(0)=0`, so the single linear constraint `Σ_i y_i = 1` makes `w` **C² across
the window edge**; the B-splines are supported strictly outside `[−2T,2T]` and are C² everywhere.
`s > ½` holds with room, so `ν_w` is finite (Def. 7.1). All transforms are closed-form:

```
ŵ_box(t) = 2 sin(2Tt)/t,
ŵ_ψ(t) = 2 Re[ e^{2iTt} (1/(s−it) + s/(s−it)² + s²/(s−it)³) ],
ŵ_β(t) = 2h cos(u_j t) · sinc⁴(th/2), sinc(x)=sin x/x,
```

and, for the prime/Γ side, with `K(u) = 2 Σ_{i≥0} e^{−(2i+½)u}` (an exact expansion of
`½/sinh(u/2)+½/cosh(u/2)`, used throughout),

```
∫_{2T}^∞ ψ_s(u−2T) K(u) cos(τu) du = 2 Σ_i e^{−(2i+½)2T} Re[ e^{2iTτ} Φ_s(s+2i+½−iτ) ],
2∫_{|u|≥2T} ψ_s cosh(u/2) cos(τu) du = 2 Re[ e^{2iTτ} (e^{T} Φ_s(s−½−iτ) + e^{−T} Φ_s(s+½−iτ)) ],
Φ_s(z) = 1/z + s/z² + s²/z³,
```

the B-spline versions by 200-node Gauss–Legendre on each compact support.

**Why C² matters, and it is not cosmetic.** For a `w` with a jump at `2T`, `ŵ(t) = O(t⁻¹)` and
`Σ_γ ŵ(τ−γ)` converges only conditionally; with a kink, `O(t⁻²)` and the residual of the zeros beyond
`Γ` is `≍ Γ⁻¹ log Γ ≈ 10⁻³` even with all `10⁵` zeros — larger than any `c` we could hope for. With the
C² matching above, `ŵ(t) = O(t⁻⁴)` and the measured residual between `Γ = 6000` and
`Γ = 74920.8` is `1.4·10⁻⁷` (§3). **The class of weights for which the experiment is even
arithmetically possible is therefore the C¹-or-smoother flat-tops**; this is a constraint on
Problem B that Paper 47 §7 does not state.

The LP is: maximise `c` subject to `f^known_w(τ_i) = Σ_{|γ|≤6000} ŵ(τ_i−γ) ≥ c` on
`τ_i ∈ [0, τ_max]` with step `0.02`, `τ_max = min(2πe^{A_T}, 200)`, plus `Σ_i y_i = 1` and the mass
budget `Σ_i|y_i| + Σ_j|x_j| ≤ L`. Sizes: `≤ 2(4+140)+1 = 289` variables, `≤ 5956` rows, HiGHS,
seconds. **The primes appear nowhere in it.**

### 2.2 A negative control first: exponential columns fail

With the exponential-column class of Paper 47 Thm. E (`w = Σ x_k e^{−s_k(|u|−2T)}`, `s_k` log-spaced,
`K = 48…80`), which is the class the *exhaustion* theorem uses, the LP saturates below zero at every
window: at `½log3`, `c = −1.16·10⁻², −4.9·10⁻³, −1.10·10⁻³, −7.8·10⁻⁴, −1.6·10⁻⁴` for
`Σ|x| ≤ 20, 100, 400, 2000, 20000` (`s_min = 0.55`), and `Σ|x| = L` is always binding. The reason is
structural, not numerical: every exponential column carries the same edge phase `e^{2iTt}`, so the
class can only reshape the *envelope* of `ŵ`, never its oscillation; and the columns are monotone,
so they cannot place mass at a chosen `u`. Recorded in `scripts/reverse/run_lp.py`,
`lp_results.json`. (This is a class statement, not a statement about `λ^W`.)

### 2.3 Results table (C² spline class, `M = 8`, range cap `U ≈ 14`)

`A_T = Σ_{n<e^{2T}} v_n`, `τ_env = 2πe^{A_T}`; `c(T,L)` = LP value; `mass = ∫_{2T}^∞ w`;
`‖·‖` = `∫_{2T}^∞|w|`; `v_last` = largest `u_j − 2T` with `|x_j| > 10⁻³`.

| `T` | `N_T` | `A_T` | `τ_env` | `L=5` | `L=20` | `L=100` | `L=2000` | `mass(L=20)` | `v_last` |
|---|---|---|---|---|---|---|---|---|---|
| `½log3 = 0.5493` | `{2}` | `0.9803` | `16.75` | `−7.37e−3` | `−1.68e−4` | `−5.37e−7` | `+1.39e−6` | `2.005` | `12.5` |
| `0.58` | `{2,3}` | `2.2488` | `59.54` | `−1.153e−1` | `−3.308e−2` | `−2.351e−2` | `−2.340e−2` | `3.900` | `12.6` |
| `0.58` (`M=16`) | `{2,3}` | `2.2488` | `59.54` | `−1.046e−1` | `−2.639e−2` | `−5.47e−3` | `−5.32e−3` | `2.297` | `10.2` |
| `0.62` | `{2,3}` | `2.2488` | `59.54` | `−1.153e−1` | `−3.470e−2` | `−2.639e−2` | `−2.639e−2` | `4.151` | `12.6` |
| `0.65` | `{2,3}` | `2.2488` | `59.54` | `−1.189e−1` | `−3.400e−2` | `−2.624e−2` | `−2.624e−2` | `4.285` | `12.5` |
| `log2 = 0.6931` | `{2,3}` | `2.2488` | `59.54` | `−1.319e−1` | `−3.608e−2` | `−3.166e−2` | `−3.166e−2` | `4.468` | `12.3` |
| `0.75` | `{2,3,4}` | `2.9420` | `119.09` | `−2.039e−1` | `−4.737e−2` | `−4.287e−2` | `−4.287e−2` | `4.607` | `12.2` |
| `0.80` | `{2,3,4}` | `2.9420` | `119.09` | `−2.931e−1` | `−8.822e−2` | `−8.569e−2` | `−8.531e−2` | `4.959` | `12.2` |

Full table with every diagnostic in `scripts/reverse/TABLE.txt` and `win_*.json`.

### 2.4 The shape of the optimal `w_T`

At `½log3`, the profile `w(2T+v)` sampled at `v = 0, 0.5, 1, …` :

| `L` | `‖w‖_∞` | `w(2T+v)`, `v = 0,0.5,1,1.5,2,2.5,3,3.5,4` | reading |
|---|---|---|---|
| `5` | `1.00` | `1.000 0.642 0.605 0.343 0.253 0.203 0.077 0.108 0.012` | **one smooth monotone shoulder**, essentially `e^{−1.2 v}`; `y = (0.935, 0, 0.065, 0)`, i.e. `ψ_{2.5}` |
| `20` | `1.26` | `1.000 0.470 1.261 1.012 0.498 0.252 0.477 0.440 0.185` | shoulder + one bump at `v ≈ 1.2`, tail to `v ≈ 6` |
| `100` | `6.3` | `1.000 1.615 3.014 −0.258 −6.326 0.109 2.140 0.356 1.860` | oscillation sets in |
| `2000` | `262` | `1.000 −3.858 −41.05 −94.65 −261.9 −20.86 −1.823 −4.213 17.50` | shape destroyed |

Sign pattern of `x`: `8` sign changes among `~30` significant nodes at `L = 5`, `27` at `L = 2000`
(Paper 47 §5 reports alternation at `70 %` of consecutive lattice sites at its own optimum — the same
phenomenon at the same place on the mass axis). No node spacing related to `log 2` or `log 3` is visible at any `L` (inspection of `x` in
`win_*.json`; no quantitative test of arithmetic structure was run, so this is an observation, not a
measurement). **`mass = ∫_{2T}^∞ w` is `+2.0` at
`½log3` and settles at `+4.8…5.2` for every `T ≥ 0.58`** — a striking constancy, discussed in §4.

`v_last ≈ 12.2…12.6` in every single run: the range cap `U ≈ 14` is **binding at every window**. The
optimiser always wants a longer tail than it is given; the reverse-engineered `w_T` is not compactly
supported in any effective sense, which is the weight-side face of Theorem O.

## §3 Theorem-Z cross-check: the test set is the primes

The LP was trained on the zeros only. The independent evaluation is the prime/Γ side of `(7.2)`,
`f_w(τ) = m(τ) + ∫_{2T}^∞(1−w)K cos τu du − Σ_n v_n w(log n) cos(τ log n) + 2∫ w cosh(u/2) cos τu du`,
with `m(τ) = Re ψ(¼+iτ/2) − log π` from `scipy.special.digamma`, the `K`-integrals in closed form,
the Γ-integrals in closed form for `ψ_s` and by 200-node Gauss–Legendre for the B-splines, and the
prime sum over all `93 973` prime powers `n ≤ e^{14.007} = 1 211 433` (the B-splines are compactly
supported, so this sum is **exact**, not truncated, up to the last spline).

### 3.0 First: the identity itself

On a hand-made C¹ weight [amended per R155_010: not C² — R155_006 §1]
(`w = 2e^{−2v} − e^{−4v}` outside the window, `T = ½log3`, `τ ∈ [0,20]`),
zero side and prime side agree to `max|Δ| = 2.4·10⁻⁸` with `10⁵` zeros and to `1.4·10⁻⁸` with the
`5 598` zeros below `6000` (`scripts/reverse/t_sanity.py`). **Theorem Z is now verified numerically in
the corpus.** (The closest prior check, `phase-118/W5`, verifies the primal identity
`⟨A_TF,F⟩ = Σ_ρ h(γ_ρ)`, not `(7.2)`.)

### 3.1 The two optimal weights at `½log3`

| `L` | `‖w‖_∞` | `c` (LP, grid `0.02`) | far-zero residual `Γ: 6000 → 74920.8` | `max|f^known − f^{prime}|` | `min f^{prime}` (grid `0.05`) |
|---|---|---|---|---|---|
| `20` | `1.26` | `−1.676e−4` | `3.70e−9` | `3.13e−7` | `−3.317e−4` at `τ = 13.25` |
| `2000` | `262` | `+1.392e−6` | `1.38e−7` | `9.54e−5` | `−8.689e−5` at `τ = 3.30` |

Three things are visible and all three are negative results, honestly reported.

1. **The far-zero residual is under control, and only because `w` is C².** `3.7·10⁻⁹` for the tame
 weight. With a kink at the edge the same quantity would be `≈10⁻³`.
2. **The `L=2000` "positive certificate" is fictitious.** Its LP value `+1.39·10⁻⁶` is below the
 `9.5·10⁻⁵` disagreement between its own two evaluations — the weight is so large
 (`‖w‖_∞ = 262`, `‖ν_w‖ ≈ 2·10³`) that double precision no longer resolves `f_w`, and the prime
 side, which is the exact one here, gives `min f^{prime} = −8.7·10⁻⁵ < 0`. So the answer to the
 task's question "is `max|difference| < c(T)`?" is **no**, at every window we computed.
3. **The `τ`-grid is itself a lie at this accuracy.** The `L=20` weight has LP value `−1.676·10⁻⁴` on
 the grid of step `0.02` and true minimum `−3.317·10⁻⁴` — a factor `2.0` — attained at
 `τ = 13.25`, which is not a grid point. This reproduces exactly the warning of Paper 47 §5
 ("a coarse-grid value `+1.7·10⁻⁴` was worth `−2.1·10⁻²` in truth") and means every `c(T)` in §2.3
 is an **upper** bound on the honest value of its own weight, by a factor of order `2` for tame
 weights and unboundedly for wild ones.

### 3.2 Why the far-zero residual cannot be bounded a priori without RH, and how big `Γ` must be

`f^known_w(τ) = Σ_{|γ|≤Γ} ŵ(τ−γ)` differs from `f_w(τ) = Σ_ρ ŵ(τ−γ_ρ)` by `Σ_{|γ|>Γ} ŵ(τ−γ_ρ)`, the
sum over the zeros we have *not* verified. Two separate things are missing there. First, for the
zeros above `Γ` we do not know that `γ_ρ` is real: Theorem Z sums `ŵ` at the complex arguments
`τ − γ_ρ` with `|Im γ_ρ| ≤ ½`, and `ŵ` is entire of exponential type `U`, so an off-line zero at
height `H` contributes up to `e^{U/2}` times what an on-line zero at the same height would — a factor
`e^{7}` for `U = 14`. No bound on that residual that does not first exclude off-line zeros above `Γ`
is available; the verified height (`Platt–Trudgian, H = 3.0000175·10¹²`) excludes them only up to `H`,
and *that* exclusion is exactly the input a proof may not use (`phase-4/00-PROOF-LOG:168`, `ES-2`).
Second, even granting RH above `Γ`, what remains is a statement about the *density*: with
`|ŵ(t)| ≤ C_w |t|^{−4}` (C² edge) and `dN(t) ≈ (2π)^{−1}log(t/2π)dt`, the residual is
`≲ (C_w/2π)·(log(Γ/2π)+⅓)/(3Γ³)`, and `C_w ≈ 4‖x‖_1/h³` for the spline class. Numerically at
`½log3` with `h = 0.137`: `Γ = 1200 → 8·10⁻⁶·‖x‖₁`, `Γ = 6000 → 6·10⁻⁸·‖x‖₁`,
`Γ = 74920 → 3·10⁻¹¹·‖x‖₁`, which matches the measured `3.7·10⁻⁹` at `‖x‖₁ = 16.2`. For a C¹ (kinked)
weight the exponent drops to `Γ⁻²log Γ` and for a discontinuous one to `Γ⁻¹log Γ`, i.e. `10⁻³` with
all `10⁵` zeros: **the smoothness of the edge, not the length of the zero table, is what makes the
experiment possible.** Required `Γ` for a residual below `10⁻⁶` at `‖x‖₁ ≈ 10²`: about `3·10³`
(C²), `10⁸` (C¹), `10¹¹` (jump) — the last two are beyond any table and the last is beyond the
verified height.

## §4 The pattern

### 4.1 `c(T)` is a step function of the prime set, not a function of `T`

| `T` | `N_T` | `A_T` | `τ_env` | `2πe^{2T}` | `c(T)` at `L=100` | `N(T*)` (Zhu) |
|---|---|---|---|---|---|---|
| `0.5493` | `{2}` | `0.9803` | `16.75` | `18.85` | `−5.4e−7` | `0.30` |
| `0.58` | `{2,3}` | `2.2488` | `59.54` | `20.04` | `−2.35e−2` | `0.51` |
| `0.62` | `{2,3}` | `2.2488` | `59.54` | `21.71` | `−2.64e−2` | `0.83` |
| `0.65` | `{2,3}` | `2.2488` | `59.54` | `23.05` | `−2.62e−2` | `1.10` |
| `log2` | `{2,3}` | `2.2488` | `59.54` | `25.13` | `−3.17e−2` | `1.55` |
| `0.75` | `{2,3,4}` | `2.9420` | `119.09` | `28.16` | `−4.29e−2` | `2.24` |
| `0.80` | `{2,3,4}` | `2.9420` | `119.09` | `31.12` | `−8.57e−2` | `2.97` |

The variation *within* a prime set is a factor `1.3` (`0.58 → log2`); the jump *across* the entry of
`3` (`½log3 → 0.58`) is at least four orders of magnitude, and the jump across the entry of `4`
(`log2 → 0.75`) is a factor `1.4` plus a doubling of `τ_env`. The last row, `T = 0.80`, is `0.005`
below `½log5 = 0.8047`, where `5` enters, and it is already `2×` worse than `0.75`. **`w_T` changes
qualitatively when a new prime enters the window; within one regime, between entries, an affine law
in `T` does hold** [amended per R155_010: corrects "there is no law worth fitting" —
R155_006 §6 shows an in-regime fit (`{0.58,0.62,0.65}` → `log2`) succeeds to `1.3·10⁻²` profile
residual and `4 %` predicted-profile error; what fails is only the *value*, by conditioning, not
the profile law].

### 4.2 The three scales of Paper 47 §8.2, tested

*Resolution `2πe^{2T}`.* At `½log3`, `τ_env = 16.75 < 2πe^{2T} = 18.85`: the whole verification
interval lies **below** the resolution scale, so `f_w ≥ c` there is a statement about the first two
zeros only (`γ_1 = 14.13`, `γ_2 = 21.02`), and the zeros alone suffice to push `c` to `0`. From
`T = 0.58` on, `τ_env/2πe^{2T} = 2.97, 2.74, 2.58, 2.37, 4.23, 3.83`: the class must control the
density regime over a range two-to-four times the resolution, and every class we could afford fails
there by two orders of magnitude. **This ratio, not `T`, orders the difficulty**, and it is the
sharpest statement this experiment produces.

*Envelope `2πe^{A_T}`.* Binding as a definition of the work interval; `v_last ≈ 12.2` in every run
says the weight's *support* wants to be long, while §3 says its *transform* must be smooth — the two
pull against each other, which is what makes the class small.

*Zhu's Landau–Widom law* `−log λ ≈ 2π²N(T*)/log N(T*)`, `T* = 2πe^{2T}`: at our windows
`N(T*) ∈ [0.30, 2.97]`, so `log N(T*) ≤ 1.09` and the formula is far outside its asymptotic regime
(it returns `λ ≈ 10⁻⁹⁹` at `T = 0.65` and `10⁻³¹` at `log 2`, against the known
`λ^A(½log3) ≤ 9.9·10⁻⁴` and the recorded three-order fall between `0.58` and `log 2`). **No test of
Zhu's law is possible at these windows**; recorded as such, not as evidence either way.

### 4.3 The mass

`‖ν_{w_T}‖` is not directly comparable to Paper 47 §5's `‖ν‖_TV = 90.75` (that is an atomic measure
on a lattice; ours is absolutely continuous plus the prime atoms of `(7.1)`), but the LP's own budget
`L = Σ|y| + Σ|x|` is the analogue, and the analogy is close: the `½log3` weight needs `L ≈ 10²` to
reach `c ≈ 0` and `L ≈ 2·10³` to (spuriously) cross it, against `90.75` for the certified 437-atom
certificate at the same window. What is *new* is the shape of the mass: `∫_{2T}^∞ w_T` equals
`+2.0` at `½log3` and `+3.9, +4.2, +4.3, +4.5, +4.6, +5.0` at the six larger windows — and at
`L ≥ 100` it locks at `+5.0…+5.2` at every one of them, with `∫|w| = ∫w` (the tail stays
non-negative). A constant of the problem, not a function of `T`, and we have no explanation for it.

### 4.4 Where `f_{w_T}` touches zero

At `½log3` (`L = 20`, `36` contacts) the contact set is a **near-uniform comb across the whole
interval**: `0.24, 0.68, 1.12, 1.58, 2.00, 2.48, 2.94, 3.52, 4.06, …, 16.6`, mean spacing `0.44`,
against `2π/U = 2π/14.01 = 0.449`. It is the Nyquist comb of the weight's *support*, i.e. the finest
oscillation the class can produce — a statement about the class, not about ζ. It is not related to
the zeros (the first is at `14.13`, far to the right of most contacts) and not to the prime comb:
`Σ_{n∈N_T} v_n cos(τ log n) − m(τ)` takes the values `5.58, 3.58, 2.56, 1.87, 1.34, 0.79, 0.32,
−0.17, −0.49, …` at the successive contacts, i.e. it sweeps through its whole range and the contacts
sit at no distinguished value of it. **The contacts are at neither local sparsity of the zeros nor
prime near-alignment; they are at the class's own resolution limit.**

At `T ≥ 0.62` the comb breaks into clusters of `3–8` contacts separated by gaps
(`0.62`: `2.5, 2.8 | 5.3, 5.7 | 11.0–12.2 | 15.9–19.2 | 22.3–24.0 | 27.2–28.5 | …`), with intra-cluster
spacing `0.35–0.45` and no recognisable period between clusters (gaps `6.4, 4.9, 7.9, 9.3`). Paper 47
§5's contact comb is "a band inside `[0,13]` plus one phase per tail row"; ours is the same band
structure, seen in a different class and without the tail rows.

## §5 Extrapolation test ("train on 1000, test on the next")

The only candidate law §4 offers is in the *profile*: at a fixed mass budget the optimal tail
`w_T(2T+v)` is a smooth shoulder whose shape moves slowly with `T` while `N_T` is fixed. The test
was run as requested: fit `w(v;T) = a(v) + b(v)·T` by least squares on the four training
windows `T ∈ {½log3, 0.58, 0.62, 0.65}` (all `≤ 0.68`) at `L = 20`, evaluate the fitted profile at
`T = log 2` and `T = 0.80`, project it onto that window's own basis (renormalising the edge
coefficients so that `Σ y_i = 1`, i.e. keeping `w` C² and admissible), and compute
`min_τ f^known` of the *predicted* weight — never re-optimising at the test window.
Script `scripts/reverse/extrapolate.py`, output `extrap_20.0.json`.

**Outcome — the prediction fails, and it fails already on the training set.**

| | `½log3` | `0.58` | `0.62` | `0.65` |
|---|---|---|---|---|
| in-sample residual `sup_v \|w_T(v) − (a(v)+b(v)T)\|` | `0.424` | `0.569` | `0.104` | `0.242` |

An affine-in-`T` law cannot even interpolate the four training profiles to better than `0.57` in a
function whose own sup norm is `1.26`. Out of sample:

| test window | `min_τ f^known` of the **predicted** `w` | `c` of the re-optimised `w` (LP) | ratio |
|---|---|---|---|
| `T = log 2` | `−2.201` | `−3.608·10⁻²` | `61×` worse |
| `T = 0.80` | `−20.61` | `−8.822·10⁻²` | `234×` worse |

(Projection of the predicted profile onto the test window's basis is not the culprit: the projection
errors are `0.34` and `3.4` in sup norm, an order of magnitude smaller than the damage.)

The reading is the one §4.1 predicts and is worth stating plainly: **the training set straddles a
prime entry** (`3` enters between `½log3` and `0.58`), so the four profiles are not four samples of
one curve but one sample of one regime and three of another; and even within the second regime the
profiles move too fast for an affine law. The "train on 1000, test on the next" works when
the next item is of the same kind as the previous thousand. Here the next window is of a different
kind whenever a new prime crosses `e^{2T}`, and the crossings are dense enough
(`½log p` for every prime power `p`) that a training set that straddles a crossing fails — but a
training set drawn from inside one regime does not. **"There is no law for `w_T` in `T` in this
class" is WITHDRAWN** [amended per R155_010, R155_006 §6]: in-regime, the affine law in
`T` fits and predicts (profile residual `1.3·10⁻²`, next-window error `4 %`); it is the *value*
functional's conditioning, not the absence of a profile law, that defeats extrapolation.

## §6 What this proves, and what it teaches

### 6.1 What it proves about RH: nothing

Every statement in §§2–5 is `DIAGNOSTIC`. Three independent reasons, each sufficient:

1. **Circularity.** The LP is trained on a table of zeros. A certificate obtained that way cannot
 enter a proof: the corpus already records this as a no-go (`phase-4/00-PROOF-LOG:168`, "zero-side
 `K` presupposes the unknown zeros (circular as tool)"; `phase-136/MAP_1:141`, ES-2). The experiment
 is a *reading* of what the closing object looks like, not a step towards it.
2. **Truncation.** `f^known` omits the zeros above `Γ = 74920.8`, and §3.2 shows that bounding that
 remainder requires knowing those zeros are on the line — which is the conclusion, not a hypothesis.
3. **Precision.** Double precision, a `τ`-grid of step `0.02` whose values are inflated by a factor
 `2` (§3.1(3)), and a restriction of the verification to `[0, τ_env]` with no tail lemma. Nothing
 here is interval-certified.

No statement about a sign for any `T > log 2` is made. The endpoint of record is unchanged:
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 47 Thm. C).

### 6.2 What it teaches

| finding | label | where it bites |
|---|---|---|
| **Theorem Z verified numerically** (`2.4·10⁻⁸` on a hand-made C¹ weight [amended per R155_010: not C² — R155_006 §1]; `3.1·10⁻⁷` on an optimised one) | `DIAGNOSTIC` (verification of a `PROVED` statement) | Paper 47 §7 had no numerical check; it now has one, and `scripts/reverse/t_sanity.py` is a five-second regression test for every future change to the conventions. |
| **The edge must be smooth for the criterion to be usable with a finite zero table**: `ŵ = O(t⁻¹)` (jump), `O(t⁻²)` (kink), `O(t⁻⁴)` (C²); far-zero residual `≍ Γ⁻¹logΓ`, `Γ⁻²logΓ`, `Γ⁻³logΓ` | `DIAGNOSTIC` bound, elementary to make `PROVED` | a refinement of Cor. 7.4: the `w_T` whose existence is RH may be sought in `W_T ∩ C^2`, and the search *must* be, if the zeros are to be consulted at all. |
| **Problem B's weight has no arithmetic structure at bounded mass** — a monotone shoulder `≈ e^{−1.2v}`, no `log p` spacing | `DIAGNOSTIC` | Paper 47 Rem. 7.6 guesses "the canonical scale `s = ½`" or "weights adapted to the primes outside the window"; at `L ≤ 20` the optimiser picks `ψ_{2.5}`, i.e. a scale `2.5`, not `½`, and ignores the primes. Neither guess is supported. |
| **The shape degenerates as the value approaches the class optimum** (`‖w‖_∞: 1 → 262` while `c` moves by `1.7·10⁻⁴`) | `DIAGNOSTIC` | Theorem O (non-attainment) now has a visible form in the *weight*, not only in the measure. Any ansatz for `w_T` with `‖w‖_∞` bounded is therefore bounded away from `λ^W`, which is a testable prediction for Problem A. |
| **`c(T)` is a step function of `N_T`** (four orders across the entry of `3`; factor `1.3` inside `N_T = {2,3}`); the **profile** (not the value) obeys an affine-in-`T` law inside one regime [amended per R155_010: added per R155_006 §6 — in-regime fits do work] | `DIAGNOSTIC` | confirms Paper 47 §8.3(4) ("not an induction upward in `T`") from the dual side: the value cannot be extrapolated across a prime entry, and even in-regime the value's conditioning defeats extrapolation despite the profile law holding. |
| **`τ_env/2πe^{2T}` is the difficulty index**: `0.89` at `½log3`, `2.4–4.2` afterwards [amended per R155_010: the quasi-positive reading "(the only window that works)" is DELETED — R155_006 §9] | `DIAGNOSTIC` | sharpens §8.2: the window is easy exactly while the whole verification interval lies below the resolution scale, i.e. while the certificate is a statement about finitely many *individual* zeros. `½log3` is the last such window; `0.58` is the first that is not. This is a cleaner statement of the wall than "two primes in the window". |
| **The contacts are at `2π/U`, the class's Nyquist comb**, not at zero gaps or prime alignments | `DIAGNOSTIC` | tempers Paper 47 §8.2's alignment reading: at the values of `c` we can reach, complementary slackness is dominated by the class's resolution, and the arithmetic structure the paper predicts would only become visible much closer to `λ^W`. |
| **`∫_{2T}^∞ w_T` locks at `+5.0…+5.2` for every `T ≥ 0.58`** | `DIAGNOSTIC`, unexplained | a candidate invariant; worth one pure-math look (it is `ν̂_w(0)`-adjacent, and Paper 47 §5 records `ν̂(0) = 1.7337` for the certified certificate). |
| exponential columns (Thm. E's exhausting class) fail at every `L` and every window | `DIAGNOSTIC`, class statement | exhaustion is not constructive: the class that exhausts in the limit is the worst class to search in. Practical guidance for any future `w`-side computation. |

### 6.3 What should be done next with this, if anything

Two cheap pure-math items fall out and neither needs the zeros:
(i) **make the smoothness/decay statement a lemma**: `w ∈ W_T ∩ C^k` across the edge ⟹
`ŵ(t) = O(|t|^{−k−2})` ⟹ `Σ_{|γ|>Γ}|ŵ(τ−γ)| = O(Γ^{−k−1}log Γ)` under RH below `Γ`, and add to
Cor. 7.4 that the `w_T` may be taken in `C^∞_c` (it already is, by Thm. 7.3) with an explicit modulus;
(ii) **the bounded-`‖w‖_∞` prediction**: if `sup{inf f_w : ‖w‖_∞ ≤ A}` is bounded away from `λ^W` for
every `A`, that is a second, weight-side form of Theorem O and a genuine class-dependent value bound
in the sense of Problem A. §2.4 is evidence for it; the proof, if there is one, is a compactness
argument in `W_T ∩ {‖w‖_∞ ≤ A}` against Theorem O, and it would be the first *lower* bound this
phase has produced.
The reverse-engineering track itself has delivered what it can: the answer to "what must `D` look
like" is "like nothing in particular, and it stops looking like anything at all exactly where the
value starts to matter".
