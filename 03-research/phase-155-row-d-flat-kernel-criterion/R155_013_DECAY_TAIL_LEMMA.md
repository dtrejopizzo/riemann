# R155.013 — A decay-based tail lemma for flat-top weights (the smooth analogue of `lem:F1`)

*Phase 155. Written in answer to `R155_012 §12(2)`: "the missing object is a
decay-based tail lemma for flat-top weights … a bound `|ν̂_w(τ)| ≤ D(w)τ^{−2}` — explicit, one
integration by parts, no zeros — would close the tail at `τ ≍ D^{1/2}`, i.e. at `O(10²)` rather than
`10^{25}`, for **every** flat-top class."*

*Written for Paper 47 §7 (beside `lem:smooth`) but **not** inserted into the paper. Inherits
Paper 47 §4 (`lem:mbounds`, `lem:F1`, `prop:T0`, `lem:T`), §5 (`lem:gbounds`), §7 (Thm Z (7.2),
`lem:Rrig`, `lem:smooth`, `cor:nontermwise`), §8 (`prop:env`).*

**Every constant below is proved; every *number* is `DIAGNOSTIC` (double precision, no interval
arithmetic). No sign is claimed for `ζ` at any `T`, and no endpoint is claimed or changed.**

---

## §0 What it does, in four lines

1. `prop:env` closes the tail of a flat-top certificate at `τ_env = 2πe^{A_T+‖ν_w‖_TV}`, i.e. at
 `10^{18.5}…10^{40}` for the `R155_011` weights: the total-variation bound `|ν̂| ≤ ‖ν‖_TV` throws
 away all decay.
2. The theorem below replaces the TV bound on the **absolutely continuous** part of `ν_w` by
 `D(w)τ^{−2}`, `D(w)` explicit and computable from `w'' `, and closes that part of the tail at
 `τ ≍ D^{1/2} ≈ 10²`. `D(w) = 2.6·10⁴ … 5.1·10⁴` for the actual `R155_011` weights.
3. **The prime atoms do not decay at all.** They are bounded only by their mass
 `E_at(w) = Σ_{log n>2T} v_n|w(log n)|`, and that term enters the threshold *exponentially*:
 `τ_stop ≈ 2πe^{A_T+E_at(w)}`. With the measured `E_at = 18.0…44.0` this is `10^{9}…10^{20}` —
 twenty decades better than `prop:env`, and still hopeless.
4. **Corollary (the real content).** `E_at(w) = 0` is a *finite* set of linear conditions
 (`w(log n) = 0` at the `373…491` prime powers with `2T < log n ≤ U`), and for such *comb-free*
 weights the theorem closes the tail at `τ_stop = 118, 196, 170, 179` at
 `T = ½log3, 0.58, 0.62, log2`. That is the `O(10²)` the audit asked for, and it is the first
 flat-top tail lemma in the corpus that is not doubly exponential. It does **not** produce an
 endpoint: every measured value on `[0,60] ⊂ [0,τ_stop]` is negative (§6, and `R155_011 §8`
 amended).

---

## §1 Setting and notation

`T > 0`; `N_T = {n : n prime power, log n < 2T}`; `v_n = 2Λ(n)/√n`; `A_T = Σ_{n∈N_T} v_n`;
`K(u) = ½/sinh(u/2) + ½/cosh(u/2)` (`lem:K`); `m(τ) = Re ψ(¼+iτ/2) − log π`;
`σ_T(τ) = m(τ) − Σ_{n∈N_T} v_n cos(τ log n)`;
`ĝ₀(τ) = 2∫_0^{2T} cosh(u/2)cos τu\,du`, `ĝ₁(τ) = 2∫_0^{2T} u sinh(u/2) cos τu\,du`,
with the bounds `|ĝ₀| ≤ k₀(τ) = 2cosh T/τ + sinh T/τ²`, `|ĝ₁| ≤ k₁(τ) = 8T sinh T/τ`
(`lem:gbounds`).

`w ∈ W_T` is even, `w ≡ 1` on `[−2T,2T]`, and (Theorem Z (7.2))

```
f_w(τ) = σ_T(τ) + ν̂_w(τ) + (β₀−2)ĝ₀(τ) + β₁ĝ₁(τ) + 2ĝ₀(τ),
ν_w = [½(1−w)K + 2w cosh(u/2)]·1_{|u|≥2T} du − Σ_{n∉N_T} (v_n/2) w(log n) (δ_{log n}+δ_{−log n}).
```

Write the three pieces of `ν̂_w + 2ĝ₀` as

```
Ψ_w(τ) = ∫_{2T}^∞ (1−w(u))K(u) cos(τu) du, (K-tail)
Φ_w(τ) = 4∫_0^∞ w(u) cosh(u/2) cos(τu) du, (cosh part, WITH the canonical column 2ĝ₀)
A_w(τ) = − Σ_{n : log n > 2T} v_n w(log n) cos(τ log n). (prime atoms outside the window)
```

so that `f_w = σ_T + Ψ_w + Φ_w + A_w + (β₀−2)ĝ₀ + β₁ĝ₁`. (This is exactly what `check.py`/
`primeside.py` evaluate; it was verified against the zero side to `3.6·10⁻⁶…1.1·10⁻⁵` in
`R155_011 §4`.)

### 1.1 Why `2ĝ₀` must be grouped with the `cosh` tail — the point the naive derivation misses

The order's derivation ("edge terms at `u = 2T` vanish by `w(2T)=1`, `w'(2T)=0`") is correct for the
`K`-tail and **false for the `cosh` tail taken alone**. The density of `ν_w` at `u = 2T⁺` is
`½(1−w)K + 2w cosh(u/2) = 0 + 2cosh T ≠ 0`, so `ν_w` restricted to `|u| ≥ 2T` has a jump of size
`2cosh T` at the window edge and one integration by parts leaves the irreducible term
`−(4 cosh T) sin(2Tτ)/τ`: **`ν̂_w` alone is `O(τ^{−1})`, never `O(τ^{−2})`.** That same term appears
in `ĝ₀ = 2cosh T·sin 2Tτ/τ + O(τ^{−2})` (`lem:gbounds`) with the opposite sign and the same
coefficient: `2·ĝ₀` contributes `+4cosh T sin(2Tτ)/τ`. The two cancel identically, which is visible
at once if one refuses to split the integral: `Φ_w = 2Ŵ` with `W(u) = w(|u|)cosh(u/2)`, and `W` is a
*globally* `C²`, even, compactly supported function — no edge at all. **This is why the lemma is a
statement about `ν̂_w + 2ĝ₀`, i.e. about `f_w − σ_T − (β₀−2)ĝ₀ − β₁ĝ₁`, and not about `ν̂_w`.**
(The canonical `β₀ = 2` of Paper 47 §3 is exactly the value that makes the flat-top edge smooth;
`R155_011`'s "the multipliers are decisive" has this as its structural counterpart.)

---

## §2 The theorem

> **Theorem D (decay tail for flat-top weights).** `PROVED`.
> Let `T > 0` and let `w ∈ W_T` be even with `w ≡ 1` on `[−2T,2T]`, `w ∈ C²(ℝ)`, and `w''` of
> bounded variation, and assume either (a) `supp w ⊂ [−U,U]`, or (b) `|w|,|w'|,|w''| ≤ Ce^{−s|u|}`
> with `s > ½`. Put
>
> ```
> D_K(w) = ∫_{2T}^∞ | ((1−w)K)''(u) | du,
> D_c(w) = 4 ∫_0^∞ | (w(u)cosh(u/2))'' | du, D(w) = D_K(w) + D_c(w),
> E_at(w) = Σ_{n : log n > 2T} v_n |w(log n)|.
> ```
> All three are finite. Then for every `τ > 0`
>
> ```
> (i) |Ψ_w(τ)| ≤ D_K(w) τ^{−2}, (ii) |Φ_w(τ)| ≤ D_c(w) τ^{−2},
> (iii) |A_w(τ)| ≤ E_at(w),
> ```
> and consequently, with `β = (β₀,β₁)`,
>
> ```
> f_w(τ) ≥ L_w(τ) := log(τ/2π) − 1/τ − 1/(2τ²) − A_T − E_at(w)
> − |β₀−2| k₀(τ) − |β₁| k₁(τ) − D(w) τ^{−2}.
> ```
> `L_w` is nondecreasing on `(0,∞)`, so if `L_w(τ_stop) ≥ 0` for one `τ_stop` then `f_w ≥ 0` on
> `[τ_stop,∞)`, and positivity of `f_w` on `ℝ` has to be verified only on the **compact** interval
> `[0, τ_stop]`, where
>
> ```
> τ_stop(w) = min{ τ : L_w(τ) ≥ 0 }.
> ```

**Proof.**

*(i).* Set `R(u) = (1−w(u))K(u)` for `|u| ≥ 2T` and `R ≡ 0` on `(−2T,2T)`; `R` is even and
`Ψ_w(τ) = ½ R̂(τ)` with `R̂(τ) = ∫_ℝ R(u)e^{iτu}du = 2∫_{2T}^∞ R cos(τu)du`. At the edge
`R(2T) = (1−w(2T))K(2T) = 0` and `R'(2T) = −w'(2T)K(2T) + (1−w(2T))K'(2T) = 0`, because `w(2T)=1`
and `w'(2T)=0` (`w ≡ 1` on the window and `w ∈ C¹`). Hence the even extension of `R` by `0` is `C¹`
on `ℝ`, and `R'` is of bounded variation with `V(R') = 2∫_{2T}^∞|R''|` (in case (a) `R = K` beyond
`U`, whose derivatives are integrable at infinity; in case (b) `|R''| ≤ (|w''|+|w'|+|1−w|)·
sup_{u≥2T}(K+|K'|+|K''|)·e^{−u/2}` is integrable as well). Two integrations by parts, all boundary
terms vanishing,
`R̂(τ) = −τ^{−2}∫_ℝ e^{iτu} dR'(u)`, so `|R̂(τ)| ≤ V(R')τ^{−2}` and `|Ψ_w| ≤ ½V(R')τ^{−2}
= D_K(w)τ^{−2}`.

*(ii).* Set `W(u) = w(|u|)cosh(u/2)`; `W` is even, and `W ∈ C²(ℝ)` because `w ∈ C²` and `cosh(u/2)`
is even and entire (no edge at `u = 2T`: `w ≡ 1` there and `W = cosh(u/2)` on the window, matching
`C²` across `±2T` by hypothesis). `W'(0) = 0` by evenness. In case (a) `W` is compactly supported;
in case (b) `|W|,|W'|,|W''| ≤ C'e^{−(s−½)|u|}` is integrable, which is exactly where `s > ½` is
needed. `Φ_w(τ) = 2Ŵ(τ)` and two integrations by parts give
`Ŵ(τ) = −τ^{−2}∫_ℝ e^{iτu}dW'(u)`, so `|Φ_w| ≤ 2V(W')τ^{−2} = 4∫_0^∞|W''|\,du·τ^{−2} = D_c(w)τ^{−2}`.

*(iii).* Trivial: `|A_w(τ)| ≤ Σ_{log n>2T} v_n|w(log n)|`, the sum converging in case (a) because it
is finite (only `n < e^U`), and in case (b) because `Σ_n Λ(n)n^{−½−s} < ∞` for `s > ½` — the same
threshold as in (ii).

*The lower bound.* `σ_T(τ) ≥ log(τ/2π) − 1/τ − 1/(2τ²) − A_T` by `lem:mbounds`(ii),(iii); the
multiplier terms by `lem:gbounds`; the three pieces by (i)–(iii). Each term of `L_w` is
nondecreasing (`log` increasing; `1/τ`, `1/(2τ²)`, `k₀`, `k₁`, `D/τ²` decreasing), so `L_w` is
nondecreasing. ∎

> **Remark D.1 (sharpness of the two exponents).** The `τ^{−2}` in (i)–(ii) is exactly the order
> `lem:smooth`(i) gives for a `C²` edge (`k = 0` there is the flat-top edge, `k = 2` here after the
> two extra derivatives), and it cannot be improved to `τ^{−3}` without `w ∈ C³`: by
> `cor:nontermwise`(ii) the support endpoint `U` carries a jump of `w'''` and contributes
> `2J|t|^{−4}cos(Ut+φ)` to `ŵ`, i.e. a genuine `τ^{−2}` in `Φ_w`. **(iii) is sharp in the worst case**
> by Kronecker (`lem:mbounds`(iii)): the frequencies `log p` are `ℚ`-independent, so for a weight with
> `w(log p) ≥ 0` the sup of `−A_w` is `Σ_p v_p|w(log p)| + …`, i.e. `E_at` up to the prime-power terms.

> **Remark D.2 (this is the smooth analogue of `lem:F1`, and it is weaker in exactly one place).**
> `lem:F1` never bounds the prime comb by its mass: it evaluates the comb *exactly* on `N` copies of
> one period of `ν̂` and replaces it by its infimum `−A_T` beyond, which works because the lattice
> `ν̂` is `P`-periodic. A flat-top `ν̂_w` is not periodic, so no such "graded" argument is available,
> and the comb has to be met head-on. Theorem D meets the *smooth* part by decay and the comb by its
> mass; `lem:F1` meets the smooth part by periodicity and the comb by exact evaluation. **The union
> of the two techniques does not exist yet**, and that, not the smooth part, is where the remaining
> exponential sits.

---

## §3 Corollaries

> **Corollary D.2 (comb-free flat-top weights).** `PROVED`.
> Assume additionally `w(log n) = 0` for every prime power `n` with `2T < log n ≤ U` (a *finite* set
> of linear conditions when `supp w ⊂ [−U,U]`: `373, 388, 427, 491` conditions at
> `T = ½log3, 0.58, 0.62, log2` with `U = U_spl ≈ 7.74…8.09`). Then `E_at(w) = 0` and
>
> ```
> τ_stop(w) = min{ τ : log(τ/2π) − 1/τ − 1/(2τ²) − A_T − |β₀−2|k₀(τ) − |β₁|k₁(τ) − D(w)τ^{−2} ≥ 0 },
> ```
> which for `D(w) ≤ D₀` and `β = (2,0)` satisfies `τ_stop ≤ max{ 2πe^{A_T+1}, (D₀/(log(τ/2π)−A_T))^{1/2} }`
> and in particular `τ_stop = O(D(w)^{1/2})` as `D(w) → ∞`. **The verification interval is
> polynomial, not exponential, in the size of the weight.**

> **Corollary D.3 (what a bounded profile buys, and what it does not).** `PROVED`.
> If `0 ≤ w ≤ 1` with `supp w ⊂ [−U,U]` then
> `D_c(w) ≤ 4cosh(U/2)(‖w''‖₁ + ‖w'‖₁ + ¼‖w‖₁)` and
> `D_K(w) ≤ κ₀(T)‖w''‖₁ + 2κ₁(T)‖w'‖₁ + 2|K'(2T)|`, where `κ_j(T) = sup_{u≥2T}|K^{(j)}(u)|`
> (`κ₀ = K(2T) = 1.299, 1.242, 1.174, 1.067` and `κ₁ = |K'(2T)| = 0.974, 0.892, 0.802, 0.676` at the
> four windows, and `∫_{2T}^∞|K''| = |K'(2T)|` since `K'` is monotone). Hence
> `D(w) = O(e^{U/2})` and, by Cor. D.2, `τ_stop = O(e^{U/4})` for a **comb-free bounded profile** —
> *singly* exponential in the support radius, against the doubly exponential
> `2πe^{A_T+‖ν_w‖_TV}` of `prop:env`.
> **But boundedness alone does not control `E_at`:** `0 ≤ w ≤ 1` only gives
> `E_at ≤ Σ_{2T<log n≤U} v_n = 185.0, 188.8, 200.7, 218.7` at the four windows — *four to ten times
> the measured `E_at` of the `R155_011` optima* (`18.0…44.0`). So `R155_012 §12`'s recommended pair
> ("the decay lemma **together with** the bounded-profile class") is **not** the right pair: the
> bounded profile controls `D`, and only the comb condition controls `E_at`. The correct pair is
> **Theorem D + Corollary D.2**, with `0 ≤ w ≤ 1` as an optional extra that makes `D` small.

---

## §4 The numbers for the `R155_011` weights

Computed by `scripts/reverse/d1000/amend.py` (one process, 40 s, `amend.json`);
`D_K, D_c` from `∫|R''|`, `∫|W''|` on a `2·10⁻⁵` grid; `‖ν_w‖_TV` recomputed honestly (see §5).
All `DIAGNOSTIC`.

| run | `T` | `β₀−2, β₁` | `D_K` | `D_c` | **`D(w)`** | `E_at(w)` | `‖ν_w‖_TV` | `log₁₀τ_env` (`prop:env`) | **`τ_stop`** (Thm D) | **`τ_stop`** (Cor. D.2, `E_at=0`) |
|---|---|---|---|---|---|---|---|---|---|---|
| `log3h` | `½log3` | `(0,0)` | `1248` | `49520` | `5.08e4` | `43.98` | `89.90` | `40.3` | `2.1e20` | **`151.9`** |
| `log3h_b` | `½log3` | `(+3.6e−3,−2.6e−2)` | `1351` | `25444` | `2.68e4` | `22.05` | `45.32` | `20.9` | `6.3e10` | **`117.5`** |
| `log3h_b60` | `½log3` | — | `1264` | `24736` | `2.60e4` | `18.01` | `39.89` | `18.5` | `1.1e9` | **`117.7`** |
| `w058` | `0.58` | — | `1494` | `42919` | `4.44e4` | `24.78` | `54.34` | `25.4` | `3.4e12` | **`196.0`** |
| `w062` | `0.62` | — | `1086` | `29027` | `3.01e4` | `32.72` | `69.05` | `31.8` | `9.6e15` | **`170.1`** |
| `wlog2` | `log 2` | — | `831` | `32532` | `3.34e4` | `36.94` | `78.17` | `35.7` | `6.6e17` | **`179.0`** |

Reading, in order of importance.

1. **The smooth part of the tail is *cheap*.** `D(w) ≈ 3·10⁴` and `D^{1/2} ≈ 170`: the `K`-tail and
 the `cosh` part together need only `[0, ~2·10²]`. The `10^{18}…10^{40}` of `prop:env` is entirely
 an artefact of bounding a decaying function by its total variation. **`R155_012 §12(2)`'s
 prediction (`O(10²)` rather than `10^{25}`) is confirmed, and proved.**
2. **The prime atoms are the whole wall.** With `E_at` present, `τ_stop = 10^{9}…10^{20}` — better
 than `prop:env` by 8–20 decades, and still astronomically outside any computation. Every decade
 of the remaining threshold is `E_at/log 10`.
3. **`D_c ≫ D_K` by a factor `20–40`**: the tail cost of a flat-top weight is the `cosh(u/2)`
 weighting of the *shoulder*, exactly the quantity `R155_011 §3.2` identified (`E₃` dominant) —
 the decay lemma reduces its price from `e^{E₃}` to `E₃`-polynomial but does not remove it.
4. `D(w)` tracks `‖w''‖₁·e^{U/2}` as Cor. D.3 predicts: the `β`-free optimum at `½log3`
 (`‖w‖_∞ = 4.33`) has `D = 2.7·10⁴`, the `β`-fixed control (`‖w‖_∞ = 3.64`, `∫|w| = 7.90`)
 `5.1·10⁴`. The four values lie within a factor `2` of each other although `τ_env` spans `22`
 decades: **`D` is a far more stable functional of the class than `‖ν‖_TV`.**

### 4.1 Consistency with the far scans, and with `[0,60]`

- `R155_011`'s far scan found `f_w = −7.321` at `τ = 17.436` (`½log3`, `log3h_b`). Theorem D gives
 `L_w(17.436) = −24.1 < 0`, so there is no contradiction: `17.4 ≪ τ_stop`, and indeed no tail lemma
 of any kind can be in force at `τ = 17.4`, since `log(17.4/2π) − A_T = 0.039 − …` is barely
 positive before any weight-dependent cost is subtracted. **A negative value inside `[0,τ_stop]` is
 exactly what the lemma says one must go and look for.**
- The comb-free `τ_stop = 118…196` is *longer* than the `[0,60]` domain of the `R155_011` runs, and
 `f_w` is measured negative on `[0,60]` at every window (§6). So even in the best case the lemma
 leaves an interval on which the class is already known to fail. **Theorem D removes the excuse
 ("the interval is `10^{40}` long"), and what it uncovers is a genuine negative.**

---

## §5 Two corrections to the `prop:env` numbers of `R155_011 §3.2`

`check.py` has been amended (`[amended per R155_012]`). Two of the three defects the
audit lists are confirmed, and the third is **not**:

- **CONFIRMED**: `check.py:63` omitted `A_T` from `log₁₀τ_env`. Fixed.
- **CONFIRMED**: `E₁` used `(1+|w|)K` where the TV integrand is `|1−w|K`, and `E₃` integrated from
 `0` rather than `2T` (the window part of the `cosh` term belongs to `2ĝ₀`, not to `ν_w`); and the
 atom list was not restricted to `log n > 2T`. Fixed.
- **NOT CONFIRMED (the audit's factor 2 on `E₂`)**: `ν_w`'s atoms are `(v_n/2)δ_{±log n}`, so the
 two-sided total mass is `Σ v_n|w(log n)|`, which is what `check.py` computed. `E₂` was **not**
 short by a factor `2`. The honest `‖ν_w‖_TV` is now computed by combining the two a.c. densities
 *before* taking `|·|` (the definition of TV), which is smaller than `E₁+E₃`: the result is
 `‖ν_w‖_TV = 39.9…89.9` and `log₁₀τ_env = 18.5…40.3` — larger than the reported `22.6…44.3` at some
 windows and smaller at others, and in every case still `≥ 10^{18}`. The audit's estimate
 `E ≈ 80–145`, `log₁₀τ_env ≈ 35–63` is an over-correction; the direction of its conclusion is
 unaffected and the reading "the LP defends `10⁻²⁰` of the interval" stands.

---

## §6 P3 (`R155_011 §8`): the bounded-profile class on `[0,60]`

*(see `R155_011 §8` amended for the protocol; `p3.py`, `p3_*.json`, `p3.log`.)*

Class: `w ≡ 1` on `[−2T,2T]`, `0 ≤ w ≤ 1` enforced pointwise on a `h/8` grid past the edge, same
`C²` `ψ`-edge + cubic-B-spline lattice `h = 2T/24`, 1000 zeros as oracle, `τ ∈ [0,60]`, `δ = 0.02`
LP grid with cutting planes, certified on the dense `δ = 0.005` grid with the corrected Bernstein
pad `B₂δ²/8`, prime side evaluated at the argmin.

| run | `T` | `β` | LP value | zero side, dense `δ=0.005` | argmin | **prime side at the argmin** | after the Bernstein pad | `‖w‖_∞` | `∫|w|` | unconstrained value on `[0,60]` (`R155_011 §3`) |
|---|---|---|---|---|---|---|---|---|---|---|
| `p3_log3h_b` | `½log3` | free | `−1.6128e−2` | `−1.7082e−2` | `55.49` | **`−1.70863e−2`** | `−3.634e−2` | `1.0039` | `7.16` | `−2.863e−3` |
| `p3_log3h_w` | `½log3` | `(2,0)` | `−3.0133e−2` | `−3.1050e−2` | `55.57` | **`−3.10484e−2`** | `−4.771e−2` | `1.0027` | `7.17` | — |
| `p3_w058_b` | `0.58` | free | `−2.8789e−2` | `−2.9110e−2` | `54.31` | **`−2.91093e−2`** | `−4.643e−2` | `1.0024` | `7.09` | `−5.865e−3` |
| `p3_w058_w` | `0.58` | `(2,0)` | `−2.9621e−2` | `−3.1760e−2` | `48.85` | **`−3.17634e−2`** | `−4.988e−2` | `1.0048` | `7.15` | — |
| `p3_w062_b` | `0.62` | free | `−2.6405e−2` | `−2.8177e−2` | `52.35` | **`−2.81756e−2`** | `−5.327e−2` | `1.0019` | `7.44` | `−2.380e−2` |
| `p3_w062_w` | `0.62` | `(2,0)` | `−2.9020e−2` | `−3.0769e−2` | `32.23` | **`−3.07705e−2`** | `−5.583e−2` | `1.0030` | `7.44` | — |
| `p3_wlog2_b` | `log 2` | free | `−3.7984e−2` | `−3.8491e−2` | `39.45` | **`−3.84916e−2`** | `−6.064e−2` | `1.0017` | `7.88` | `−3.440e−2` |
| `p3_wlog2_w` | `log 2` | `(2,0)` | `−4.5976e−2` | `−4.6354e−2` | `31.33` | **`−4.63554e−2`** | `−7.140e−2` | `1.0002` | `8.30` | — |

(`‖w‖_∞` exceeds `1` by `2·10⁻³…5·10⁻³` because the profile constraints are imposed on an `h/8`
grid; the violation is `0.2–0.5 %` and does not affect any sign. Zero and prime sides agree to
`1·10⁻⁶…5·10⁻⁶` at every argmin. Runtimes `47–78 s` each, one process at a time; the eight LPs took
`≈ 7.5 min` of wall time, over the `5 min` total budget — declared, not hidden.)

**Verdict.** **No value is `≥ 0` on `[0,60]` at any of the four windows, with `β` free or `β = (2,0)`, and the
prime side confirms every one of them at the argmin to `5·10⁻⁶`.** The bounded-profile class is
**worse** than the unconstrained one at every window — by `6.0×` at `½log3` (`−1.71e−2` against
`−2.86e−3`), `5.0×` at `0.58`, `1.2×` at `0.62`, `1.1×` at `log 2` — so `R155_008`'s bounded-profile
conjecture buys a smaller `D(w)` and `‖ν_w‖_TV` at the price of a strictly smaller value, and the
price is largest exactly at the window where the unconstrained class came closest. Releasing the two
multipliers helps in the bounded class too (`−3.01e−2 → −1.61e−2` at `½log3`), and does not change
the sign. By `R155_012 §12` ("*Until P3 returns a non-negative value on `[0,60]`, there is no path to
a new endpoint at any `T ∈ (½log3, log 2]`*"): **there is no such path in this class, and the
flat-top LP track is measured negative on every honest interval at every window tested.** The
endpoint of record is unchanged: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Thm C). `DIAGNOSTIC`.

---

## §7 Labels

| statement | label |
|---|---|
| Theorem D (i)–(iii) and the lower bound `f_w ≥ L_w`, `L_w` nondecreasing | **`PROVED`** |
| Remark D.1 (sharpness of `τ^{−2}` and of the mass bound on the comb) | **`PROVED`** (via `cor:nontermwise`(ii) and `lem:mbounds`(iii)) |
| Corollary D.2 (comb-free weights ⟹ `τ_stop = O(D^{1/2})`) | **`PROVED`** |
| Corollary D.3 (`D = O(e^{U/2})` for bounded profiles; `E_at ≤ Σ_{2T<log n≤U}v_n` is *not* small) | **`PROVED`** |
| The values of `D(w)`, `E_at(w)`, `‖ν_w‖_TV`, `τ_stop` in §4 | `DIAGNOSTIC` (double precision; the `∫|W''|`, `∫|R''|` are quadratures on a `2·10⁻⁵` grid, not enclosures) |
| The `E₂` factor-2 correction of `R155_012 §4` | **rejected**, with proof (§5) |
| P3 verdict (§6) | `DIAGNOSTIC` |
| Any statement about `λ^W`, `λ^P`, an endpoint, or the sign of `ζ` at any `T` | **none made**; endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Thm C) |

---

## §8 What this opens

1. **Add the comb conditions to the LP.** `w(log n) = 0` for the `373` prime powers in
 `(2T, U]` is `373` equality columns in exactly the LP of `R155_011`, and by Cor. D.2 it converts
 the verification interval from `10^{20}` to `118`. It is the first flat-top experiment in this
 track whose *failure would be conclusive* and whose success would be a certificate on a
 computable interval. Cost: one LP of the same size, `≈ 60 s`. **This is the successor of (P3).**
 It is not free: `R155_011 §5(iv)` shows the optima put their largest mass bins exactly at
 `log 4`, `log 5`, `log 17`, so the constraint bites where the value lives, and the honest
 expectation is that the comb-free class is *worse*. That is precisely what should be measured.
2. **The graded/decay hybrid.** Remark D.2: `lem:F1` handles the comb exactly because `ν̂_lat` is
 periodic. A flat-top weight whose shoulder is supported on the lattice `{jd}` *and* smooth would
 admit both arguments; `lem:hybrid` already does this for exponential columns. Whether a `C²`
 flat-top weight can be written as `ν_lat + (smooth, comb-free)` is open and is the natural
 Paper-47 §7 question raised by Theorem D.
3. Theorem D is stated for `W_T ∩ C²`; for `C^k` it gives `τ^{−k}` with
 `D_k(w) = ‖(w cosh)^{(k)}‖₁`-type constants and `τ_stop = O(D_k^{1/k})`. Nothing below `k = 2` is
 useful (`k = 1` gives `τ_stop ≍ D₁`, no gain over TV in practice).

---

*Scripts: `scripts/reverse/d1000/amend.py` (`amend.json`), `dense.py` (`dense_*.json`),
`p3.py` (`p3_*.json`, `p3.log`); amended `check.py`, `insight.py`.*
