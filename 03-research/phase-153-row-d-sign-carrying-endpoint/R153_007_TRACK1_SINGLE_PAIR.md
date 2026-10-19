# R153.007 — Round 3, Track 1 (P153.5): the single off-line pair for `ζ` itself

*Construction of record: . Orders: `R153_006_ROUND3_BLUEPRINT.md` §Track 1, questions (1)–(5).
Conventions and prior results of record: `R153_003_ROUND2.md`, `R153_004_CONFIRMATION.md`,
`R153_005_CLOSING_DECISION.md`. Scripts: `scripts/round3/{track1.py, run_tstar2.py, fatal_check.py}`,
reusing the mesh-free spectral assembly of `scripts/audit/aud_spectral.py`.
Labels: `PROVED` / `RESTATEMENT` / `DIAGNOSTIC-NUMERIC` / `OPEN` / `WITHDRAWN`.*

**Headline.** The rank-two (in fact rank-four) law exists, is exact, and is *not* a law about the critical line:
its leverage in `a` over a window of length `2T` is exactly `cosh(2aT)`, which at `T = log 2` and `a = 0.45`
is `1.2010`. Numerically `T*(a,γ_0)` is `a`-independent to four decimals; the whole content is the
`γ_0`-dependence. At `T = log 2` the conditional criterion refutes configurations only for
`γ_0 ≲ 201`; for `γ_0 ≥ 300` the rank-four correction is already invisible against `λ_min(A_{log2}) ≈ 1.0·10⁻⁷`.
**The FATAL rule is satisfied with an enormous margin: nothing is excluded above `γ_0 ≈ 201`, versus
Platt–Trudgian's verified `3·10¹²`.** One blueprint formula is repaired (factor 2 → 4).

---

## 0. Corpus check (before building)

`grep -rIn "rank-two\|rank two"` → phases 119–124, 138: all about the *two polar coordinates* or the
ruling plane, none about a rank-two perturbation of `A_T` by a zero pair.
`grep -rIl "single off-line"` → phase 64 (`FACE-C-spectral-shift-monotonicity`, spectral-shift heuristics, no
explicit-formula divisor model), phase 105 (`105_02_OFF_LINE_ZERO_EXPONENTIAL_THEOREM`: Li-coefficient
quartet law `|w_ρ|=1 ⟺ β=½`, a *Cayley/Li* growth statement, not a windowed Weil statement — different object).
`grep -rIn "cosh(2aT)\|cosh(a r)\|Turán concentration"` → no hit. `grep -rIn "gamma_0\^max\|detection law"` →
only `R153_005` (`T*(a)` for the `Ξ_a` family). Conclusion: the single-pair divisor model, the identity
(T1.4) and the threshold `γ_0^max(T)` are new; the explicit formula used is Paper 42's, cited not reproved.

---

## 1. (1) The model, stated exactly

**Normalisation of record.** Paper 42 `main.tex`, `\subsec:primitiveendpoints`: for `F` supported in `I_T=(−T,T)`,
```
    F̂(s) = ∫_{−T}^{T} F(t) e^{(s−1/2)t} dt ,     M_∓F = F̂(0), F̂(1),     P_T = ker M_− ∩ ker M_+ .
```
`A_T = G_{Γ,T} − m_0 I − Σ_{2≤n<e^{2T}} Λ(n)n^{−1/2}(S_{log n}+S_{−log n})`, `m_0 = log π + γ + π/2 + 3log2
= log π − ψ(¼) = 10.74049…` (`main.tex` eq. `localizedprimitiveoperator`), `G_{Γ,T}` the zero-extension
compression of the multiplier `g_Γ(τ) = Re ψ(¼+iτ/2) − ψ(¼)`. The Weil pairing in evaluation coordinates is
`main.tex:1965` (eq. `evalcoords`):
`I_∂(D_f,D_g) = f̂(0)ĝ(1)‾ + f̂(1)ĝ(0)‾ − Σ_ρ m_ρ f̂(ρ) ĝ(ρ′)‾`, `ρ′ = 1−ρ̄`.

> **Proposition T1.1 (`RESTATEMENT`; Paper 42 eq. `evalcoords` + Guinand–Weil).** For real `F ∈ P_T`,
> ```
>       ⟨A_T F, F⟩  =  Σ_ρ m_ρ · F̂(ρ) · F̂(1−ρ)  =  Σ_ρ m_ρ · F̂(ρ) · conj F̂(ρ′) ,
> ```
> the sum over all non-trivial zeros of `ζ` with multiplicity; the two polar terms drop because `F ∈ P_T`.

*Proof.* `F` real gives `conj F̂(s) = F̂(s̄)`, hence `conj F̂(ρ′) = F̂(1−ρ)`. In Fourier variables, with
`\tilde F(τ) = F̂(½+iτ)` and `c(r) = ∫F(t)F(t+r)dt` (`‖\tilde F‖² ↔ c`), the Guinand–Weil formula with test
function `\tilde c(τ)=|\tilde F(τ)|²` reads
`Σ_ρ = [poles] + (1/2π)∫|\tilde F(τ)|²(Re ψ(¼+iτ/2) − log π)dτ − 2Σ_n Λ(n)n^{−1/2}c(log n)`;
the bracket is exactly the symbol of `A_T` since `m_0 = log π − ψ(¼)`, and `(1/2π)∫|\tilde F|²cos(τ log n)dτ = c(log n)`. ∎

**Verification (`DIAGNOSTIC-NUMERIC`, FATAL-rule normalisation check).** At `T=log 2`, `K=160` sine modes,
for the `A_T`-minimiser and two random `F ∈ P_T`, comparing `⟨A_TF,F⟩` with `2Σ_{k≤600}|F̂(½+iγ_k)|²`
(`mpmath.zetazero`): ratios `0.998299`, `0.999934`, `0.999978`; at the `Q`-minimisers of §3 the agreement is
`1 − 10⁻⁶`. The residual is the tail `γ > 600`: extending the sum to `k ≤ 4000` (`γ ≤ 4506`) gives
`343.06973528` vs `343.06949782`, ratio `1 − 6.9·10⁻⁷`, and agreement to all 8 printed digits on the
`A_T`-minimiser. This fixes the normalisation of `F̂`, the factor `2` from `±γ`
and the absence of any missing on-line term.

> **Lemma T1.2 (`PROVED`, elementary; contains a repair of `R153_006`).** Let `γ_0 > 0`, `a ∈ [0,½)`,
> `X := F̂(½+a+iγ_0) · conj F̂(½−a+iγ_0)` for real `F`. Then in `Σ_ρ F̂(ρ)F̂(1−ρ)`:
> (i) the on-line pair `½±iγ_0` (simple) contributes `2|F̂(½+iγ_0)|²`;
> (ii) the off-line quadruple `½±a±iγ_0` (all simple) contributes **`4 Re X`**.

*Proof.* (i) `1−ρ = ρ̄` so each of the two zeros gives `|F̂|²`, equal by reality. (ii) The four zeros pair as
`(½+a+iγ_0, ½−a−iγ_0)` and `(½−a+iγ_0, ½+a−iγ_0)` under `ρ ↦ 1−ρ`. The first pair contributes
`2·F̂(½+a+iγ_0)F̂(½−a−iγ_0) = 2X`; the second `2X̄`. Total `2X+2X̄ = 4 Re X`. ∎

**Repair.** `R153_006` Track 1 writes the correction as `−2|F̂(½+iγ_0)|² + 2 Re[…]`. The cross coefficient
is `4`, not `2` (the `±γ_0` symmetrisation doubles both terms equally, so the *ratio* is `2:4`, not `2:2`).
At `a = 0` Lemma T1.2 (ii) must reduce to *twice* (i), the quadruple degenerating to a **double** on-line pair:
`4Re X|_{a=0} = 4|F̂(½+iγ_0)|² = 2 × 2|F̂|²` ✓. With the blueprint's `2` this consistency fails. `WITHDRAWN`:
the coefficient `2` in `R153_006`.

**The model form.** `⟨B_T F,F⟩ := ⟨A_TF,F⟩ − 2|F̂(½+iγ_0)|² + 4Re X` is, by T1.1 + T1.2, exactly the Weil
form of the divisor "zeros of `ζ` with the pair `½±iγ_0` replaced by `½±a±iγ_0`" — `PROVED`, and trivial.
**But `B_T ≥ 0` has no justification**: `A_T` is built from the *primes and Gamma factor of `ζ`*, whose explicit
formula equals the sum over `ζ`'s *actual* zeros; moving zeros while keeping the primes produces a divisor
that is the divisor of no zeta function, so Weil positivity says nothing about `B_T`. Using `B_T ≥ 0` as the
test would subtract a non-negative quantity `2|F̂(½+iγ_0)|²` and manufacture spurious exclusions. §4 uses the
valid form instead.

---

## 2. (2) A-priori bounds, the autocorrelation identity, and the growth dichotomy

> **Lemma T1.3 (`PROVED`).** For `F ∈ L¹(I_T)` and `a,γ ∈ ℝ`: `|F̂(½±a+iγ)| ≤ e^{|a|T}‖F‖_1`.

*Proof.* `|∫F(t)e^{(±a+iγ)t}dt| ≤ ∫|F(t)|e^{|a||t|}dt ≤ e^{|a|T}‖F‖_1`. ∎

> **Lemma T1.4 (`PROVED`, new — the exact form of the correction).** With `c = c_F` the autocorrelation
> (`R153_003` Lemma C2), even and supported in `|r| ≤ 2T`,
> ```
>       X = ∫_{−2T}^{2T} c(r) e^{(a+iγ_0)r} dr ,        4 Re X = 4∫_{−2T}^{2T} c(r) cosh(a r) cos(γ_0 r) dr ,
>       2|F̂(½+iγ_0)|² = 2∫_{−2T}^{2T} c(r) cos(γ_0 r) dr .
> ```

*Proof.* `X = ∫∫F(t)F(s)e^{(a+iγ_0)t}e^{(−a−iγ_0)s}dt\,ds = ∫∫F(t)F(s)e^{(a+iγ_0)(t−s)}`; substitute `r=t−s`.
Taking real parts and using that `c` is even kills `sinh(ar)sin(γ_0r)`'s partner and leaves `cosh(ar)cos(γ_0r)`. ∎

> **Corollary T1.5 (two-sided growth dichotomy, `PROVED`; the upper half is classical in spirit —
> Weil/Bombieri, but no corpus or textbook statement in this windowed form was found, so it is proved here).**
> For real `F` supported in `I_T`:
> ```
>   (upper)   |4 Re X| ≤ 4 cosh(2aT) ‖c‖_1 ≤ 4 cosh(2aT) ‖F‖_1² ≤ 8T cosh(2aT) ‖F‖_2² ,
>   (sharp)   the constant is attained up to a factor 2: for the two-bump family
>             F_ε = ε^{−1}(1_{[−T,−T+ε]} + 1_{[T−ε,T]}) one has c_{F_ε} → 2δ_0 + δ_{2T} + δ_{−2T} weakly,
>             hence 4Re X/‖F‖_1² → 2 + 2cosh(2aT)cos(2γ_0T), which equals 2 + 2cosh(2aT) whenever
>             2γ_0T ∈ 2πℤ; compare the upper bound 4cosh(2aT).
> ```
> Hence a single off-line pair at distance `a` from the line can bend the Weil form on a window of length `2T`
> by at most `4cosh(2aT)‖F‖_1²`, and by that much for some `F`. Consequently: *if for every `T` and every
> `F ∈ P_T` the Weil form of the divisor exceeds `−C·cosh(2a'T)‖F‖_1²`, no single mirror pair lies at distance
> `> a'` from the line with constant `C ≥ 4`; conversely a pair at distance `a` cannot be detected by any
> window on which the positive part of the form exceeds `4cosh(2aT)‖F‖_1²`.*

*Proof.* Upper: `|cosh(ar)| ≤ cosh(2aT)` on `|r| ≤ 2T` and `‖c‖_1 ≤ ‖F‖_1²` (Young), `‖F‖_1 ≤ √(2T)‖F‖_2`.
Sharp: the two-bump `F` has `c` with unit masses at `r = 0` (weight 2) and `r = ±2T` (weight 1), so
`4Re X → 4[2 + cosh(2aT)cos(2γ_0T)]` while `‖F‖_1² = 4`. ∎

**This is the whole `a`-dependence.** The *leverage* of off-lineness over a window of length `2T` is
`cosh(2aT)`, not `e^{2aT}` (the blueprint's `e^{aT}`-based dichotomy overstates it by using one-sided
`ℓ¹` bounds twice). At `T = log 2`: `cosh(2aT) = 1.0226` (`a=0.15`), `1.0904` (`a=0.30`), `1.2010` (`a=0.45`).
So at the certified endpoint the criterion is at most a `20 %` perturbation of its `a=0` value.

---

## 3. (3) `T*(a,γ_0)`: computation and the two factors

**Criterion implemented.** `Q_T(a,γ_0) := A_T − C(a,γ_0)`, `⟨C F,F⟩ = 4 Re X(F)`, a real symmetric rank-4
operator assembled from the *exact* moment vectors `u_k = ∫φ_k e^{(a+iγ_0)t}dt`, `v = conj(∫φ_k e^{(−a+iγ_0)t}dt)`,
`C = 2(u_Rv_R^⊤+v_Ru_R^⊤−u_Iv_I^⊤−v_Iu_I^⊤)`. `A_T` by the audit's mesh-free spectral assembly (sine basis on
`(−T,T)`, graded Gauss–Legendre panels in `τ`, symbol `Reψ(¼+iτ/2) − log π − 2ΣΛ(n)n^{−1/2}cos(τ log n)`),
primitivity by the exact null space of `[∫φ_k e^{∓t/2}]`. Reproduces `λ_min(A_{log2}|P_T) = 1.068·10⁻⁷`
(`K=160`), `1.044·10⁻⁷` (`K=240`) — the round-2 value of record. Basis size is driven by a frequency cutoff
`Ω = max(4γ_0,120)`, `K = ⌊2TΩ/π⌋+40`, `τ_max = 8Ω`; refinement check by `Ω`-multiplier `3,4,6`
(identical to 5 decimals) and by `K`. `T*(a,γ_0) := inf{T : λ_min(Q_T|P_T) < 0}`, bisected; monotonicity in `T`
is `RESTATEMENT` (Q3(i) of `R153_005`: zero extension preserves primitivity, and both the extra primes and the
correction act through `c`, which vanishes past `2T`, so both forms are *unchanged* under extension).

**Table 1 — `γ_0 = γ_1 = 14.134725…`, varying `a`** (`DIAGNOSTIC-NUMERIC`; bisection tolerance `5·10⁻⁴`):

| `a` | 0.00 | 0.05 | 0.10 | 0.20 | 0.30 | 0.45 | 0.49 |
|---|---|---|---|---|---|---|---|
| `T*(a,γ_1)` | 0.23419 | 0.23419 | 0.23419 | 0.23383 | 0.23383 | 0.23383 | 0.23383 |

Identical at `Ω`-multipliers 4 and 6. **The variation over the whole range of `a` is `3.6·10⁻⁴`, i.e. the
bisection tolerance.** Predicted by T1.5: at `T ≈ 0.234` the leverage is `cosh(2aT) ≤ cosh(0.229) = 1.026`.

**Table 2 — `a = 0.30` (and `a = 0`), varying `γ_0` over true ordinates** (`DIAGNOSTIC-NUMERIC`):

| `γ_0` | `γ_1 = 14.135` | `γ_2 = 21.022` | `γ_5 = 32.935` | `γ_10 = 49.774` | `γ_25 = 88.809` | `γ_50 = 143.112` | `γ_100 = 236.524` |
|---|---|---|---|---|---|---|---|
| `T*(0.30,γ_0)` | 0.23394 | 0.31093 | 0.41007 | 0.59347 | 0.61925 | 0.65847 | **0.78086** |
| `T*(0,γ_0)` | 0.23394 | 0.31129 | 0.41152 | 0.59783 | 0.62543 | 0.66683 | **0.79284** |
| `½ log(γ_0/2π)` | 0.4054 | 0.6038 | 0.8283 | 1.0348 | 1.3243 | 1.5629 | 1.8141 |

`γ_100` is the first tabulated ordinate with `T* > log 2 = 0.69315`, consistent with `γ_0^max(log 2) ≈ 201` of §4.

**Separation.** Yes, the law separates, but not as anticipated:
`T*(a,γ_0) = Θ(γ_0) − δ(a,T)` with `δ ≤ 10⁻² ` for all `a < ½` — the `a`-part is `cosh(2aT)`, a *multiplicative
correction of at most 20 % to the form*, contributing essentially nothing to the threshold; the `γ_0`-part is
the resolution/density part and carries everything. No fit is offered: over `log γ_0 ∈ [2.65, 4.96]` the data
are not log-linear (slope `0.194` on `[γ_1,γ_2]`, `0.061` on `[γ_10,γ_50]`); the growth is monotone and slower
than `¼log(γ_0/2π)` at small `γ_0` and appears to approach a slope near `0.06–0.25` per unit `log γ_0`.
`DIAGNOSTIC` only; the extremal problem behind it is stated as (P153.6) below.

**Mechanism (`PROVED` at `a=0`, `DIAGNOSTIC` in general).** At `a=0` the criterion `4|F̂(½+iγ_0)|² > ⟨A_TF,F⟩`
is, by T1.1, exactly `|F̂(½+iγ_0)|² > ½ Σ_ρ |F̂(½+iγ)|²`: *can more than half of the Weil mass be placed on a
single ordinate?* Measured fraction at the minimiser, `γ_0 = γ_1`: `0.8568` (`T = 0.30`), `0.9440` (`T = 0.40`),
`0.9524` (`T = log 2`). This is a Turán-type concentration problem for functions of exponential type `T`
against the weight `g(τ)`; the competitor count near `γ_0` is the zero density `log(γ_0/2π)/2π`, which is why
the threshold grows with `log γ_0`.

---

## 4. (4) The conditional theorem and the FATAL check

> **Theorem T1.6 (conditional exclusion, `PROVED`).** Let `a ∈ (0,½)`, `γ_0 > 0`. Suppose the non-trivial zeros
> of `ζ` consist of the four simple zeros `½±a±iγ_0` together with zeros lying on the critical line only.
> Then for **every** `T > 0` and every real `F ∈ P_T`,
> ```
>            4 ∫_{−2T}^{2T} c_F(r) cosh(a r) cos(γ_0 r) dr   ≤   ⟨A_T F, F⟩ .
> ```
> Equivalently `Q_T(a,γ_0) ≥ 0` on `P_T`. Hence every `(a,γ_0)` with `T*(a,γ_0) < T` is refuted under that hypothesis.

*Proof.* By T1.1, `⟨A_TF,F⟩ = Σ_ρ F̂(ρ)F̂(1−ρ)`, unconditional. Split the sum: the quadruple contributes `4 Re X`
(T1.2(ii), rewritten by T1.4), each remaining zero `½+iγ` contributes `|F̂(½+iγ)|² ≥ 0`. Drop the non-negative part. ∎

**Note (important, and contrary to the blueprint's framing).** Theorem T1.6 does **not** use Paper 42's
certificate `A_T ≥ 0` and is **not** restricted to `T ≤ log 2`. The `log 2` window is not the source of the
exclusion; it is only the window we choose to read the table at. Nothing in Track 1 depends on
`thm:certifiedendpoints`, and the `B_T ≥ 0` route of `R153_006` (which does) is invalid (§1).

**FATAL check.** Reading Theorem T1.6 at `T = log 2` (`DIAGNOSTIC-NUMERIC`, `fatal_check.py`,
`a = 0.45`, the maximal leverage):

| `γ_0` | 100 | 200 | 300 | 500 | 1000 |
|---|---|---|---|---|---|
| `λ_min(Q_{log2})`, `Ω`-mult 2 | `−3.5109·10⁻¹` | `−1.5427·10⁻¹` | `+1.0315·10⁻⁷` | `+1.0161·10⁻⁷` | `+1.0008·10⁻⁷` |
| `Ω`-mult 3 | `−3.5113·10⁻¹` | `−1.5439·10⁻¹` | `+1.0181·10⁻⁷` | `+1.0063·10⁻⁷` | `+9.9502·10⁻⁸` |

(`γ_0 = 2000`: `+9.891·10⁻⁸` at `Ω`-mult 2, `K = 1805`; at `Ω`-mult 3, `K = 2687`, the value collapses to
`−1.3·10⁻¹⁴`, i.e. to zero within the conditioning of a `2687`-mode generalised eigenproblem whose true value
is `10⁻⁷`. Recorded as a **conditioning artefact, not negativity**; the usable range of the present assembly
is `K ≲ 2·10³`, and `γ_0 ≥ 300` is already decided.)

Bisection in `γ_0` gives the cut-off `γ_0^max(log 2) = 200.8 ± 1`, **identical for `a = 0` and `a = 0.45`**.
Above it `λ_min(Q_{log2})` equals `λ_min(A_{log2}) = 1.0·10⁻⁷` to three digits: the rank-four correction is
invisible, the minimiser being the unperturbed near-null direction of `A_{log2}`, whose Fourier mass at `γ_0`
has already decayed.

**Outcome: the FATAL rule is satisfied, with margin `10¹⁰`.** The set excluded by the `log 2` window is
`{(a,γ_0) : 0 ≤ a < ½, γ_0 ≤ 201}`, contained with vast room inside the Platt–Trudgian verified range
`|γ| ≤ 3·10¹²`. No presumption of error arises; the four candidate error sources named in the orders were
checked explicitly and all are clean: the normalisation of `F̂` (§1, verified to `1−10⁻⁶` against 600 true
ordinates), the factor `2` from `±γ_0` (Lemma T1.2, one repair made to the blueprint's cross coefficient),
a missing on-line term (the verification would have detected it; the `B_T` variant that *does* drop an on-line
term is rejected in §1), and the growth of `|F̂|` at height `γ_0` (Corollary T1.5: the true growth is
`cosh(2aT) ≤ 1.21`, not `e^{2aT}`).

---

## 5. (5) What this does and does not say about `ζ`

**Says.** (i) The explicit formula, read as a sum over the divisor, gives an exact finite-rank law for a single
off-line quadruple, with the correction in closed form `4∫c_F(r)cosh(ar)cos(γ_0r)dr` — one integral against the
same autocorrelation polynomial that carries the round-2 certificate (`R153_003` (★)), hence in principle
interval-certifiable. (ii) Under "RH except one quadruple at height `γ_0`", a window of length `2T*(a,γ_0)`
suffices to refute; `T*` is computed above. (iii) The off-lineness parameter `a` contributes only the factor
`cosh(2aT)`: **a short window cannot see that a zero is off the line, only that Weil mass is concentrated at
one ordinate.** At `a = 0` the same criterion refutes a *double* on-line zero at `γ_0 ≤ 201` under RH-otherwise;
the criterion is therefore a multiplicity/concentration detector, not a critical-line detector. This is the
sharp, negative answer to (P153.5): Theorem A's mechanism (the cross term `−⟨A_T w,w⟩`, `w = sinh(at)F`) has
an analogue for a single pair, but the analogue is quantitatively empty because a single pair's `sinh` weight
is `O(aT)` while `Ξ_a`'s is a full vertical line of zeros.

**Does not say.** Nothing unconditional about `ζ`: every statement carries the hypothesis "all other zeros on
the line", which is strictly stronger than RH minus one quadruple only in the trivial sense and is unproven.
Nothing new: everything refuted lies below `γ_0 = 201`. No certified numbers: `T*` and `γ_0^max` are
floating-point Galerkin quantities with refinement checks only. Nothing about several off-line quadruples,
about zeros of unbounded multiplicity, or about the Epstein/Beurling falsifiers.

---

## 6. Verdict table

| id | statement | label |
|---|---|---|
| T1.1 | `⟨A_TF,F⟩ = Σ_ρ m_ρ F̂(ρ)F̂(1−ρ)` on `P_T`, `F̂(s)=∫Fe^{(s−½)t}` | `RESTATEMENT` (Paper 42 `main.tex:1965`, `subsec:primitiveendpoints`; Guinand–Weil) |
| verification | ratio `⟨A_TF,F⟩ : 2Σ_{k≤600}|F̂(½+iγ_k)|²` = `0.9983 … 0.999978`; `1−10⁻⁶` at minimisers | `DIAGNOSTIC-NUMERIC` |
| T1.2 | on-line pair `→ 2|F̂|²`; off-line quadruple `→ 4 Re X` | `PROVED` |
| `R153_006` cross coefficient `2` | must be `4` | `WITHDRAWN` (repaired) |
| `B_T = A_T + R_T ≥ 0` as a test | invalid: counterfactual divisor, not the divisor of a zeta; subtracts a non-negative on-line term | `WITHDRAWN` |
| T1.3 | `|F̂(½±a+iγ)| ≤ e^{|a|T}‖F‖_1` | `PROVED` (trivial) |
| T1.4 | `4Re X = 4∫c_F(r)cosh(ar)cos(γ_0r)dr` | `PROVED` (new) |
| T1.5 | growth dichotomy with the sharp constant `cosh(2aT)` (not `e^{2aT}`), attained | `PROVED` |
| T1.6 | conditional exclusion; holds for all `T`, independent of Paper 42's certificate | `PROVED` |
| `T*(a,γ_1)` | `0.2342 → 0.2338` over `a ∈ [0,0.49]`: `a`-independent to bisection tolerance | `DIAGNOSTIC-NUMERIC` |
| `T*(0.30,γ_0)` | `0.234, 0.311, 0.410, 0.593, 0.619, 0.658` for `γ_{1,2,5,10,25,50}` | `DIAGNOSTIC-NUMERIC` |
| separation | `a`-part = `cosh(2aT) ≤ 1.2010` at `T=log2`; `γ_0`-part = concentration/density, carries all growth; no fit offered | `DIAGNOSTIC-NUMERIC` |
| `γ_0^max(log 2)` | `200.8 ± 1`, same for `a = 0` and `a = 0.45`; above it `λ_min(Q) = λ_min(A) = 1.0·10⁻⁷` | `DIAGNOSTIC-NUMERIC` |
| FATAL rule | satisfied: excluded set `γ_0 ≤ 201 ≪ 3·10¹²` (Platt–Trudgian 2021) | passed, no error presumed |
| (P153.5) | answered: the analogue exists and is exact, but detects concentration, not off-lineness | `CLOSED` (negative) |

## 7. Open list

| id | statement | label |
|---|---|---|
| (P153.6) | the extremal problem behind `T*`: `Φ(T,γ_0) := sup{|F̂(½+iγ_0)|² / ⟨A_TF,F⟩ : F ∈ P_T}`; prove `4Φ(T,γ_0) < 1` for `log(γ_0/2π) > κT` with explicit `κ` (data suggest `κ ≈ 4–16`). A Turán/Beurling–Selberg concentration problem with the weight `g(τ)` | `OPEN` |
| (P153.7) | interval-certify one row of Table 2 (all ingredients are polynomial functionals of `c_F`, as in `R153_003` (★); the only new object is `∫c(r)cosh(ar)cos(γ_0r)dr`, an exact polynomial integral) | `OPEN` |
| (P153.8) | the multi-quadruple version: `n` off-line pairs, and the version with the on-line hypothesis relaxed to a zero-density bound — the first would be the only route to an unconditional statement | `OPEN` |
| (P153.9) | is `γ_0^max(T)` really `a`-independent, or does the coincidence at `a=0, 0.45` break at larger `T`? | `OPEN` |
