# R155_053 — round 8B: P6, the arithmetic content of row D as an equivalence chain

**Scope.** Item P6 of `PATH-TO-D.md` (lines 305–320). One 60-second script
(`scratchpad/band.py`, not committed) was used only for the sign structure of the symbol and for
proof-grade witnesses; every number below is labelled. No statement about the zeros of ζ is asserted as a
fact; no sign for ζ is claimed beyond `T ≤ log 2`.

**Notation** (Paper 46 §1, `main.tex:114–137`). `I_T = (−T,T)`, `F̂(τ) = ∫F e^{iτt}`, `c_F` the autocorrelation,
`m(τ) = Re ψ(¼+iτ/2) − log π = C₀ + ∫₀^∞(1−cos τu)K(u)du` (`eq:m`, line 330), `C₀ = −5.3721834`,
`v_n = 2Λ(n)/√n`, `N_T = {n ≥ 2 : log n < 2T}`, `A_T = Σ_{N_T} v_n`, `σ_T = m − Σ_{N_T} v_n cos(τ log n)`,
`𝔞_T(F) = (2π)^{−1}∫σ_T|F̂|²`, `P_T = {A(F)=B(F)=0}`, `W_T = 𝔞_T + 2Re(A B̄)`. Values:
`λ^A_T` = bottom of `𝔞_T` on the unit sphere of `P_T` (row D at `T` is `D_T :⟺ λ^A_T ≥ 0`); `λ^P_T` the relaxed
primitive value of `def:PD` (`main.tex:450`); `λ^W_T` the bottom of `W_T` on `L²(I_T)`. Record:
`λ^W_T ≤ λ^P_T ≤ λ^A_T` (`prop:weak`, line 462; intro line 137). For a general nonnegative arithmetic
function `a` we write `D_T(a)`, `σ_T^{(a)}`, `𝔞_T^{(a)}` for the same objects with `v_n = 2a(n)/√n`
("any nonnegative weights may be used", `main.tex:447`).

**Naming.** The alignment inequality is written `𝖠_T(w)` throughout (renamed from `X_T` per R155_058, because Paper 47
uses `X_T` for the Tate collar, `46/main.md:673–677, 790–796`).

**Corpus check (task item 5).** `grep -rn "alignment\|Kronecker\|X_T\|uniformity" 03-research/phase-15-arithmetic-hodge-index* 04-papers/47* 04-papers/46*`:
the alignment band is described (`DIAGNOSTIC`) in `47/main.tex:2739–2745` (§9.2) and `PATH-TO-D:305–320`;
Kronecker density of the comb's supremum is `lem:mbounds`(iii), `47/main.tex:671–676`, quoted in
`R155_013:150`, corrected in `R154_002:35,102`; "uniformity in `T` is what is missing" is `47/main.tex:298, 2719, 3020`
and `46/main.md:3575, 5511, 5890`; the field-uniformity constraint T1 is `46/main.md:4785–4820`. The
Diophantine location of the alignment intervals (Prop. 2.2), the finite-modification theorem (Thm 4.2)
and the finitely-supported-comb theorem (Prop. 4.3) have **no corpus hit** (`grep "finite modification\|finitely many terms\|amplif\|convergent\|12/19"`
returns nothing relevant). The trace-class split of the negative part has a precedent for the
archimedean part alone, `R155_039:70–82` (`M₋`, `tr M₋ = 4.4958·T`); Prop. 2.3 extends it to the full symbol.

---

## 1. Theorem 1 (finite dependence): row D at a fixed window is a condition on finitely many numbers

**Proposition 1.1 (finite dependence; `PROVED`).** Fix `T > 0`. For a nonnegative arithmetic function `a`
put `v_T(a) := (2a(n)/√n)_{n∈N_T} ∈ ℝ^{N_T}`, `|N_T| = ⌈e^{2T}⌉ − 2`. Then
(i) `D_T(a)` depends on `a` only through `v_T(a)`;
(ii) `𝒟_T := {v ∈ ℝ^{N_T} : 𝔞_T^{(v)} ≥ 0 on P_T}` is a closed convex set, namely
```
𝒟_T = ⋂_{F ∈ P_T real, ‖F‖=1, F in the form domain} { v : Σ_{n∈N_T} v_n c_F(log n) ≤ C₀ + Lev(c_F) },
Lev(Φ) = ∫₀^∞ (Φ(0) − Φ(u)) K(u) du ;
```
(iii) `0 ∉ 𝒟_T` for `T ≥ T₀(0) = 0.74921`, and more generally, on the cone `v ≥ 0` (which contains every `v_T(a)`),
`𝒟_T ∩ {v ≥ 0 : Σ v_n < −C₀ − φ((3π/2T)²)} = ∅` (for signed `v` the same proof gives the statement with `Σ|v_n|`);
(iv) for `a = Λ` the numbers entering are exactly `{Λ(n) : 2 ≤ n < e^{2T}}`, i.e. the primes and prime
powers below `e^{2T}`, together with the one explicit function `m` (equivalently `C₀` and `K`), and nothing else.

*Proof.* (i) is the definition of `σ_T^{(a)}`. (ii) Real tests suffice: for `F = F₁ + iF₂` with `F_j` real,
`|F̂|² = |F̂₁|² + |F̂₂|² + 2 Im(F̂₁\overline{F̂₂})`, and `F̂₁\overline{F̂₂}` is Hermitian-symmetric (`F̂_j(−τ) = \overline{F̂_j(τ)}`), so its imaginary part is odd and
integrates to `0` against the even `σ_T`; hence `𝔞_T(F) = 𝔞_T(F₁) + 𝔞_T(F₂)`, and `A(F) = A(F₁) + iA(F₂)`
with `A(F_j)` real, so `F ∈ P_T ⟺ F₁, F₂ ∈ P_T`. For real `F` the identity `𝔞_T(F) = C₀‖F‖² + Lev(c_F) − Σ v_n c_F(log n)`
is `thm:A` (`eq:Aform`, line 384). Each `F` gives a closed half-space (or the whole space when `Lev = ∞`, in
which case `𝔞_T(F) = +∞` and the inequality is void); an intersection of closed half-spaces is closed and
convex. (iii) `thm:SC` (`main.tex:2003`, stated for nonnegative weights) with `𝒩 = N_T`, `A = Σ v_n`: the bottom on `P_T` is `≤ C₀ + A + φ((3π/2T)²)`,
negative when `A < −C₀ − φ`; the case `A = 0` is `prop:arch`(ii) (`main.tex:2290`). (iv) restates (i). ∎

**Corollary 1.2 (regimes; `PROVED`).** Let `n₁ < n₂ < …` enumerate `supp Λ ∩ [2,∞)`. On each regime
`T ∈ (½ log n_k, ½ log n_{k+1}]` the vector `v_T`, the mass `A_T` and the symbol `σ_T` are constant; `D_T`
varies inside a regime only through `I_T`, and `λ^A_T` is nonincreasing inside a regime (extend `F ∈ P_T` by
zero: it lies in `P_{T'}`, `T' > T`, with the same `𝔞`). At a regime boundary one atom `v_{n_{k+1}}` enters, and
the sign of the change of `λ^A` is not determined by anything in this memo (`c_F(log n)` takes both signs
on `P_T`, Lemma 4.2b below). ∎

**Proposition 1.3 (the arithmetic content is uniformity; `PROVED`).**
```
RH ⟺ ∀T: D_T ⟺ ∀T: v_T(Λ) ∈ 𝒟_T,
```
(Paper 45 Thm 10.4 with Weil's criterion, as cited at `47/main.tex:137–142`), where each `𝒟_T` is a closed
convex subset of a finite-dimensional space defined by `Γ`-data only. Hence: (a) for fixed `T`, `D_T` is a
statement about a finite, exactly known list of numbers; (b) no finite amount of information about `Λ`
decides `∀T D_T` (Prop. 4.3: every finitely supported comb fails `D_T` for all large `T`, and Thm 4.2: every
finite initial segment of `Λ` is shared by combs failing `D_T` at explicit `T`); (c) the arithmetic content
of row D is therefore the single assertion that the *sequence* `(Λ(n))_{n≥2}` meets every `𝒟_T`, and
nothing per window. ∎ (The proof of (b) is deferred to §4; it uses nothing from §§2–3.)

**Remark 1.4 (`PROVED`, scope).** `prop:decide` (`main.tex:2694`) decides the sign of `λ^P_T` when `λ^P_T ≠ 0`,
not of `λ^A_T`; per window `D_T` is a closed condition on a known vector, semi-decidable from the negative
side by exhibiting `F`. Nothing more is claimed.

---

## 2. The band

Throughout §2 fix a regime and write `σ = σ_T` (constant on the regime), `A = A_T`, `v = v_T`.

**Proposition 2.1 (finite structure and the last sign change; `PROVED`).** Let `τ₁ = τ₁(A)` be the unique
positive root of `log(τ/2π) − 1/τ − 1/(2τ²) = A` (the left side increases from `−∞` to `+∞`, `lem:mbounds`(ii)).
Then (i) `σ > 0` on `(τ₁, ∞)`; (ii) `σ(0) = C₀ − A < 0`; (iii) `σ` is real-analytic and nonconstant on `ℝ`, so
`{τ ≥ 0 : σ(τ) = 0}` is finite; (iv) `{σ < 0}` is a finite union of bounded open intervals, the first one
containing `0`, and the last sign change `τ_* := sup{τ : σ(τ) < 0}` satisfies `τ_* ≤ τ₁`; (v)
`τ₁ = 2π e^{A} · e^{1/τ₁ + 1/(2τ₁²)} > 2π e^{A}`.
*Proof.* (i) `m(τ) ≥ log(τ/2π) − 1/τ − 1/(2τ²) > A ≥ Σ v_n cos(τ log n)` for `τ > τ₁` (`lem:mbounds`(ii),(iii)).
(ii) `m(0) = C₀`. (iii) `ψ` is analytic on `Re z > 0`, and `Re ψ(¼+iτ/2) = ½[ψ(¼+iτ/2) + ψ(¼−iτ/2)]` is a real-analytic
function of `τ ∈ ℝ`; the comb is a trigonometric polynomial; `σ → +∞`. A nonconstant real-analytic function
has finitely many zeros on a compact interval. (iv) from (i)–(iii). (v) rearrange the defining equation. ∎

*Values (elementary numerics, double precision):* `τ₁ = 60.5432` for `N_T = {2,3}` (`A = 2.248826`),
`τ₁ = 120.0865` for `N_T = {2,3,4}` (`A = 2.941974`, `v₄ = log 2`). Note `2πe^{A} = 59.543` and `119.087`
(`prop:env`(iii) quotes these as "the multiplier-free threshold"; the exact zero of the lower envelope is
`τ₁`, larger by the factor `e^{1/τ₁+…}`; the paper's `o(1)` covers it, but see item 6 below).

**Proposition 2.2 (the alignment structure; `PROVED`).** *Regime `N_T = {2,3}`,* `T ∈ (½ log 3, log 2]`. Put
`m_lo(τ) := log(τ/2π) − 1/τ − 1/(2τ²)` and let `τ_a`, `τ_b` be the roots of `m_lo = v₃ = 1.268568` and
`m_lo = v₂ = 0.980258` (`τ_a = 23.3409`, `τ_b = 17.7446`, elementary numerics). Then
```
{σ < 0} = { τ : v₂ cos(τ log 2) + v₃ cos(τ log 3) > m(τ) },
```
and on `(τ_a, ∞)` every `τ` with `σ(τ) < 0` satisfies
```
cos(τ log 2) > (m_lo(τ) − v₃)/v₂ > 0, cos(τ log 3) > (m_lo(τ) − v₂)/v₃ > 0,
```
so there are unique integers `k, l ≥ 1` with `|τ log 2 − 2πk| < δ₂(τ) := arccos((m_lo(τ)−v₃)/v₂) < π/2` and
`|τ log 3 − 2πl| < δ₃(τ) := arccos((m_lo(τ)−v₂)/v₃) < π/2`, both `δ_j` decreasing in `τ`, and consequently
```
|k log 3 − l log 2| < (δ₂ log 3 + δ₃ log 2)/(2π) < (log 6)/4 = 0.4479, i.e. 0.639 < 2^l/3^k < 1.565.
```
Every component of `{σ<0} ∩ (τ_a, τ₁]` is contained in one arc `{|τ log 2 − 2πk| < δ₂}` of length `< π/log 2 = 4.53`,
and the number of such arcs meeting `(τ_a, τ₁]` is at most `⌊(τ₁ − τ_a) log 2/(2π)⌋ + 2 = 6`.
*Proof.* If `σ(τ) < 0` then `v₂ cos(τ log 2) > m(τ) − v₃ cos(τ log 3) ≥ m_lo(τ) − v₃`, positive for `τ > τ_a`;
symmetrically for `3` (`τ_b < τ_a`). The arcs of `cos x > c > 0` are `|x − 2πk| < arccos c < π/2`. Subtracting the
two arc conditions after dividing by `log 2`, `log 3` gives `2π|k/log 2 − l/log 3| < δ₂/log 2 + δ₃/log 3`; multiply
by `log 2 · log 3/(2π)`. The arc count: consecutive arcs are `2π/log 2` apart. ∎

*Regime `N_T = {2,3,4}`,* `T ∈ (log 2, ½ log 5]`: comb `= g(τ log 2) + v₃ cos(τ log 3)`, `g(x) = v₂ cos x + v₄ cos 2x`,
`g = 2v₄y² + v₂y − v₄` in `y = cos x`, increasing on `y > −v₂/(4v₄) = −0.354`, with `g > 0 ⟺ y > y₀ = 0.43702`
(the negative root is `< −1`). Hence for `τ > τ_a` (same `τ_a`, since `m_lo > v₃` is the condition) every negative
`τ` has `|τ log 2 − 2πk| < arccos y₀ = 1.1185`, and for `τ > τ_b' = 34.4909` (root of `m_lo = v₂ + v₄ = 1.673405`)
also `|τ log 3 − 2πl| < arccos((m_lo − v₂ − v₄)/v₃) < π/2`; the Diophantine conclusion is the same with
`(1.1185·log 3 + (π/2) log 2)/(2π) = 0.369` in place of `0.4479` on `(τ_b', τ₁]`, and the arc count on `(τ_a, τ₁]` is
`≤ 12`. `PROVED`.

**Table 2.2a (the negative set; `DIAGNOSTIC` interval endpoints from bisection on a `4·10⁵`-point grid,
witnesses `PROVED`).**

| regime | components of `{σ<0}`, `τ ≥ 0` | last sign change `τ_*` | `(k,l)`, `2^l/3^k` of alignment components |
|---|---|---|---|
| `{2,3}` | `(0, 2.278) (4.816, 7.272) (9.666, 11.966) (16.251, 18.494) (27.558, 28.938) (45.149, 46.129)` | `46.129` (paper: `46.13`, `main.tex:1042`) | `(3,5): 1.185`; `(5,8): 1.053` |
| `{2,3,4}` | the same six to within `0.6`, then `(62.616, 63.777) (108.495, 108.950)` | `108.950` | `(3,5)`, `(5,8)`, `(7,11): 0.936`, `(12,19): 0.9865` |

*Proof-grade witnesses (`PROVED` modulo double-precision evaluation, using the upper bound `m ≤ m_up := log(τ/2π) + 1/τ + ½log(1+1/4τ²)` of
`lem:mbounds`(ii) and double-precision `cos`, `log`):* at `τ = 45.64206`, comb `= 2.21553 > m_up = 2.00492`
(margin `0.2106`), so `σ(τ) < 0`; at `τ = 108.72265` in the second regime, comb `= 2.93679 > m_up = 2.86013`
(margin `0.0767`). Hence `τ_* ∈ [45.642, 60.544]` for `{2,3}` and `τ_* ∈ [108.723, 120.087]` for `{2,3,4}`: the last sign
change is *located with a proof* inside these intervals; the digits `46.129`, `108.950` are the grid values.
The pairs `(k,l) = (5,8), (12,19)` carrying the last components are consecutive convergents of `log 2/log 3`;
`(3,5)` and `(7,11)` are intermediate fractions. (`DIAGNOSTIC` observation; the theorem is only the bound
`|k log 3 − l log 2| < 0.448`.)

**Proposition 2.3 (what the band decides, and what it does not; `PROVED`).** Write `σ = σ₊ − σ₋`, `σ₋ ≥ 0`
supported in `[−τ_*, τ_*]`, `Q_T` the projection onto `L²(I_T)`, `Pos_T := Q_T σ₊(D) Q_T ≥ 0` (unbounded form),
`Neg_T := Q_T σ₋(D) Q_T ≥ 0`. Then
(i) `Neg_T` is trace class, with `tr Neg_T = (2T/2π) ∫_ℝ σ₋(τ) dτ`;
(ii) `𝔞_T(F) ≥ −(2π)^{−1}∫_{|τ|≤τ_*} σ₋|F̂|²` for every `F`: all negativity of the form is produced on the band;
(iii) `λ^A_T ≥ inf_{L²} 𝔞_T ≥ −‖Neg_T‖ ≥ −tr Neg_T`;
(iv) `D_T ⟺ ⟨Neg_T F, F⟩ ≤ ⟨Pos_T F, F⟩ for all F ∈ P_T`: a compact operator dominated by a positive one on a
codimension-two subspace;
(v) the sign of `λ^A_T` is **not** a function of `σ|_{[−τ_*,τ_*]}` alone: with `λ₀ = λ₀(Tτ_*) < 1` the top prolate
eigenvalue, replacing `σ` by `σ − c·1_{|τ|>τ_*}` with `c > sup σ₊/(1−λ₀)` gives a form negative on all of `L²(I_T)`, and
replacing it by `σ + c·1_{|τ|>τ_*}` with `c > ‖Neg_T‖/(1−λ₀)` gives a form positive on all of `L²(I_T)`, while `σ|_{band}` is
unchanged in both cases.
*Proof.* (i) The kernel of `Neg_T` is `k(t−s)1_{I_T}(t)1_{I_T}(s)` with `k = (2π)^{−1}∫σ₋ e^{iτ·}`, continuous, `σ₋`
bounded and compactly supported; `Neg_T = (Q_T σ₋^{1/2}(D))(σ₋^{1/2}(D) Q_T)` is a product of two Hilbert–Schmidt
operators (each has kernel in `L²(I_T × ℝ)`), hence trace class, and the trace of an integral operator with
continuous kernel on `I_T` is `∫_{I_T} k(0) dt = 2T·k(0)`. This is the argument of `R155_039:78–80` for `m₋`.
(ii)–(iv) are the split `𝔞_T = Pos_T − Neg_T`. (v) On `L²(I_T)` the operator `Q_T 1_{[−τ_*,τ_*]}(D) Q_T` is the
time-band limiting (prolate) operator, with largest eigenvalue `λ₀(Tτ_*) < 1` (Slepian–Pollak; corpus:
`00-references/PROLATE-REFERENCES.md`, Theorem P of `R155_047`), so `⟨Q_T 1_{|τ|>τ_*}(D) Q_T F, F⟩ ≥ (1−λ₀)‖F‖²`.
Negative replacement: `σ ↦ σ − c·1_{|τ|>τ_*}` gives a form `≤ (sup σ₊)‖F‖² − c(1−λ₀)‖F‖² < 0` for `c > sup σ₊/(1−λ₀)`.
Positive replacement: `σ ↦ σ + c·1_{|τ|>τ_*}` gives a form `≥ −‖Neg_T‖‖F‖² + c(1−λ₀)‖F‖² > 0` for `c > ‖Neg_T‖/(1−λ₀)`.
Both are bounded even symbols agreeing with `σ` on `[−τ_*, τ_*]`, and the signs hold on all of `L²(I_T)`, hence on `P_T`.
(The proposition is about symbols, not about ζ.) ∎

*Value (`DIAGNOSTIC`, grid):* at `T = log 2`, `tr Neg_T = 5.233`, `sup σ₋ = 7.621` (`= B_*`, `main.tex:1057`), so
`λ^A_{log 2} ≥ −5.233` (`PROVED` inequality, `DIAGNOSTIC` number; useless for the sign, printed to show the scale).
At `T = ½ log 5`: `tr Neg_T = 7.039`. Compare `tr M₋ = 3.116` at `log 2` for the archimedean part alone (`R155_039`).
`HEURISTIC`: the effective number of negative modes of `Neg_T` is of order `2T·2τ_*/(2π) ≈ 20` at `log 2`, consistent
with the recorded arena `≥ 12` even modes (`R155_044`, memory).

**Reading of §2.** The band `[0, τ₁]` carries all negativity of `𝔞_T` (Prop. 2.3(ii)), is finite and of explicit
length (Prop. 2.1), and its negative part beyond `τ_a ≈ 23.3` sits at Diophantine near-solutions of `2^l ≈ 3^k`
(Prop. 2.2). In the sense of `prop:env` the band is where a *certificate* is checked (`f_w ≥ 0` is automatic
beyond `τ_env(w)`, Lemma 3.0); in the sense of Prop. 2.3(v) the band does *not* decide the primal sign by
itself: positivity is a global balance of `Pos_T` against `Neg_T`. Both halves are `PROVED`.

---

## 3. The conditional reduction: the alignment inequality `𝖠_T(w)`

For `w ∈ 𝒲_T` (`def:W`, `main.tex:1081`) define the three even functions
```
S_w(τ) := −2 Re Σ_{n≥2} Λ(n) n^{−½−iτ} w(log n) = −Σ_{n≥2} v_n w(log n) cos(τ log n) (smoothed prime sum),
M_w(τ) := C₀ + ∫₀^∞ (1 − w(u) cos τu) K(u) du (smoothed archimedean term),
Π_w(τ) := 2 ∫_ℝ w(u) cosh(u/2) cos(τu) du (polar term),
```
all absolutely convergent by the decay `|w| ≤ Ce^{−(½+δ)|u|}`. By `thm:Z`(i) (`eq:fw`, line 1098),
`f_w = M_w + S_w + Π_w`. Define
```
𝖠_T(w): S_w(τ) ≥ −M_w(τ) − Π_w(τ) for all τ ∈ ℝ ;
𝖠_T^{band}(w): the same inequality for |τ| ≤ τ_env(w), where τ_env(w) := the unique positive root of
 m_lo(τ) − A_T − ‖ν_w‖_TV − 2k₀(τ) = 0, m_lo(τ) = log(τ/2π) − 1/τ − 1/(2τ²), k₀(τ) = 2cosh T/τ + sinh T/τ².
```
**Lemma 3.0 (`PROVED`).** `τ_env(w)` is well defined (`m_lo` increasing, `k₀` decreasing, `lem:mbounds`(ii), `lem:gbounds`), and
`𝖠_T^{band}(w) ⟺ 𝖠_T(w)`. *Proof.* `prop:env`(i) (`main.tex:1033`) for the feasible triple `(ν_w, 2, 0)`:
`f_w ≥ m_lo(τ) − A_T − ‖ν_w‖_{TV} − 2k₀(τ) ≥ 0` for `τ ≥ τ_env(w)`. ∎ (So `𝖠_T` is genuinely a statement on the band; note
`τ_env(w) ≥ τ₁(A_T + ‖ν_w‖_TV) − o(1)` only, the `k₀` term and the `o(1)` of `prop:env` going in opposite directions; in the
two computed regimes the band `[0, τ_env(w)]` contains `[0, τ_*]` for every `w`, since `τ_env(w) ≥ τ_env(w)|_{‖ν‖=0,k₀=0}·e^{−2k₀} ≈ τ₁ > τ_*` — the
last inequality is DIAGNOSTIC in the `k₀` correction and is not used anywhere.)

**Lemma 3.1b (non-attainment for the complete form; `PROVED`, same proof as `thm:O`).** Let `T ≥ ½ log 2` and `w ∈ 𝒲_T`.
Then `inf_ℝ f_w < λ^W_T`. *Proof.* Weak duality gives `f_w ≥ c := inf f_w ⟹ W_T ≥ c` on `L²(I_T)`, so `c ≤ λ^W_T`. Suppose
`c = λ^W_T`. The bottom of `W_T` on the unit sphere of `L²(I_T)` is attained at some `F_⋆` (Bombieri Thm 3, or the compactness
argument in the proof of `thm:O`, `main.tex:572–577`, which uses only the form's structure). Then `ϱ := σ_T + ν̂_w + 2ĝ₀ − λ^W_T ≥ 0`
and `(2π)^{−1}∫ϱ|F̂_⋆|² = W_T(F_⋆) − λ^W_T‖F_⋆‖² = 0` (`prop:P` for the polar term; `∫ν̂_w|F̂_⋆|² = 0` since `c_{F_⋆}` vanishes
off `(−2T,2T)`). Since `ϱ ≥ 0` is continuous and `F̂_⋆` is entire with isolated zeros, `ϱ ≡ 0` on `ℝ`. Taking inverse Fourier
transforms on `0 < |u| < 2T`: the transform of `σ_T` is `−½K(|u|)du` plus the atoms `−½v_n δ_{±log n}` (`eq:m`), that of `ν̂_w`
is `ν_w`, supported in `|u| ≥ 2T`, that of `2ĝ₀` is `2g₀ = 2cosh(u/2)·1_{|u|<2T}`, and that of the constant `λ^W_T` is an atom at `0`;
so `2cosh(u/2) = ½K(u) + atoms` on `0 < u < 2T`, impossible because `K(u) ~ 1/u` as `u ↓ 0` while `cosh` is bounded. ∎

**Theorem 3.1 (the reduction chain; `PROVED` by citation, with the per-window gap made explicit).** Throughout, `T ≥ ½ log 2`
(the range on which `thm:Zexh`, `cor:RH` and Lemma 3.1b are stated; for `T < ½ log 2` the comb is empty and `D_T` is `prop:arch`(iii)).
(a) If `𝖠_T(w)` holds for some `w ∈ 𝒲_T` (regular or not), then `W_T ≥ 0` on `L²(I_T)`, hence `D_T`.
(b) *Exact per-window statement.* `[∃ w ∈ 𝒲_T : 𝖠_T(w)] ⟺ λ^W_T > 0`. (⟸: `thm:Zexh`(i) gives `w ∈ 𝒲_T^{reg}` with `inf f_w > 0`.
⟹: weak duality gives `λ^W_T ≥ inf f_w ≥ 0`, and Lemma 3.1b gives `λ^W_T > inf f_w ≥ 0`.) In particular if `λ^W_T = 0` then **no**
`w ∈ 𝒲_T` satisfies `𝖠_T(w)`. Likewise, if `λ^P_T > 0` there are `w ∈ 𝒲_T^{reg}` and `β ∈ ℝ²` with `inf[f_w + (β₀−2)ĝ₀ + β₁ĝ₁] > 0`
(`thm:Zexh`(ii)).
**Per window, `D_T` (i.e. `λ^A_T ≥ 0`) is not on record to imply `λ^W_T ≥ 0` or `λ^P_T ≥ 0`; the converse of (a)
at a single `T` is `OPEN` in this sense** (the inequalities `λ^W ≤ λ^P ≤ λ^A` are the only ones proved).
(c) `[∀T ≥ ½ log 2 ∃w ∈ 𝒲_T^{reg}: 𝖠_T(w)] ⟺ RH ⟺ [∀T: D_T]`, and RH `⟹ ∀T ≥ ½ log 2: λ^W_T > 0`; so the sharpest chain is
```
∀T D_T ⟹ RH ⟹ ∀T ≥ ½log2: λ^W_T > 0 ⟹ ∀T ≥ ½log2 ∃w: 𝖠_T(w) ⟹ ∀T D_T.
```
*Proof.* (a) The paragraph after `def:W` (`main.tex:1091–1095`): `(ν_w, 2, 0)` is dual feasible, `f_w ≥ 0` gives
`W_T ≥ 0` on `L²(I_T)` (`prop:P`, line 624, plus weak duality `prop:weak`), and `W_T = 𝔞_T` on `P_T`. (b) `thm:Zexh`(i),(ii)
(`main.tex:1140–1147`) and Lemma 3.1b. (c) `cor:RH` (line 1167, stated for `T ≥ ½ log 2`) for the first equivalence and for
RH `⟹ λ^W_T > 0` (Jensen/exponential-type step in its proof); Paper 45 Thm 10.4 for the second. ∎

**Remark 3.1a (why this is the sharpest true statement of its form; `PROVED` where labelled).** (i) `𝖠_T(w)` *is*
`f_w ≥ 0`; any prime-side inequality on the band that certifies `D_T` through the flat-top class is of this form
(`thm:Zexh`: every certificate of `W_T` is a flat-top explicit-formula certificate up to `ε`). (ii) The trivial
envelope `S_w ≥ −Σ_n v_n|w(log n)| =: −A_T(w)` certifies `𝖠_T(w)` exactly on `{τ : M_w + Π_w ≥ A_T(w)}`, and by
`prop:env`(ii) the envelope constant `A_T` for the inner comb cannot be lowered (Kronecker, `lem:mbounds`(iii)); on
the complement the actual values of the prime phases `τ log p mod 2π` must be used — by Prop. 2.2 that is the
set of near-solutions of `2^l ≈ 3^k` in the two computed regimes, and in general the Kronecker-dense set where
`Σ v_n cos(τ log n) > m(τ)`. (iii) For `w ∈ 𝒲_T^{reg}`, by `thm:Z`(ii) the inequality `𝖠_T(w)` at such `τ` is the statement
`Σ_ρ ŵ(τ − γ_ρ) ≥ 0`, i.e. `S_w ≥ −M_w − Π_w` says the primes are not *over-aligned* relative to the zero
density the explicit formula assigns to them there (`main.tex:2739–2745`, and §9.3 item 5, `main.tex:2789–2794`).

**Theorem 3.2 (the expected negative, stated as what is provable).** Let `θ ∈ (½,1)` and
`H_θ :⟺ ψ(x) − x ≪_ε x^{θ+ε}` for all `ε > 0`.
(i) `PROVED` (Paper 47 Thm 27.10, `46/main.md:11476–11499`, `CLASSICAL`): `H_θ ⟺ β_max ≤ θ`, where `β_max = sup Re ρ`;
in particular `H_{½} ⟺ RH`.
(ii) `PROVED` (Thm 3.1(c) + (i)): `[∀T ∃w 𝖠_T(w)] ⟺ RH ⟺ H_{½}`.
(iii) `PROVED` (translation): the implication `H_θ ⟹ ∀T ∃w 𝖠_T(w)` is **equivalent** to the zero-repulsion statement
`β_max ≤ θ ⟹ β_max = ½`. This is not a theorem of record for any `θ < 1`, and by Paper 47 §27.2 it is a statement
of the polar class: a partial-sum bound for `Λ` is exactly as strong as the corresponding zero bound, never
stronger (Cor. 27.10a, `46/main.md:11501–11508`).
(iv) **Logical form of the negative.** "`H_θ` does not imply `∀T 𝖠_T`" cannot be a theorem *about ζ*: if RH is true,
every true statement implies it. What is provable is the class statement of Theorem 4.2 below: within the class
of nonnegative combs with the *same* `H_θ` (same exponent, same zeros of the associated Dirichlet series, same
pole), `D_T` fails at explicit `T`; hence no derivation of `D_T` from `H_θ` alone (nor from any zero-free region,
zero-density estimate or partial-sum bound) is sound — in the sense of Paper 47 Thm 18.1 / Rem. 18.1a
(`46/main.md:4785–4820`), a derivation from a class-property is a derivation for every member of the class.
(v) `PROVED` (the converse direction; which theorem does what). Suppose ζ has a zero `ρ₀` with `β₀ = Re ρ₀ > ½`. Then:
 * `ψ(x) − x ≠ O(x^θ)` for every `θ < β₀` — Thm 27.10, direction (⇒), contrapositive (the stronger `Ω_±(x^{β₀−ε})`
 is classical (Landau/Phragmén) but not in the corpus record; not used);
 * there is `T` with `𝔞_T < 0` on `P_T` — Weil's criterion via Paper 45 Thm 10.4 (direction "primitive positivity
 for all `T` ⟹ RH", contrapositive);
 * at that `T`, no `w ∈ 𝒲_T` satisfies `𝖠_T(w)` — Thm 3.1(a), contrapositive; equivalently, by `thm:Z`, every
 flat-top `f_w` takes a negative value: at some `τ` the smoothed prime sum satisfies
 `S_w(τ) < −M_w(τ) − Π_w(τ)` — a genuine over-alignment of the primes relative to the archimedean density.
 * `OPEN`/not on record: an *effective* `T = T(β₀, γ₀)` from these citations (the recorded form of the converse
 is non-effective; Bombieri's test functions built from the zero would give one, but no window size is
 recorded in the corpus).

---

## 4. What is new: the one quantity per window, and the void of per-window arithmetic

**Proposition 4.1 (the per-window quantity; `PROVED`).** For `T ≥ ½ log 2` define the *alignment excess*
```
𝔈_T := inf_{w ∈ 𝒲_T^{reg}} sup_{τ∈ℝ} [ −S_w(τ) − M_w(τ) − Π_w(τ) ] (= − sup_w inf_τ f_w).
```
Then, for `T ≥ ½ log 2`: `𝔈_T = −λ^W_T` (`thm:Zexh`(i)); `𝖠_T` is solvable `⟺ 𝔈_T < 0` (Thm 3.1(b)); `λ^W_T ≥ 0 ⟺ 𝔈_T ≤ 0`; `T ↦ 𝔈_T` is
nondecreasing (`λ^W` nonincreasing, proof of `cor:KEP08`, `main.tex:1611–1613`); and
```
RH ⟺ sup_{T ≥ ½log2} 𝔈_T ≤ 0 ⟺ lim_{T→∞} λ^W_T ≥ 0.
```
The "maximal alignment of the primes against the zero-density-equivalent" asked for in P6 is exactly `𝔈_T`; it
is a real number determined by `v_T(Λ)` and `Γ` (Prop. 1.1), so *per window it carries no arithmetic beyond the
finite vector*; all arithmetic is in the one inequality `sup_T 𝔈_T ≤ 0`. ∎ `HEURISTIC` (Zhu's law, `main.tex:2735`):
`λ^W_T ↓ 0` with `−log λ^W_T ≍ e^{2T}`, so under RH the limit is `0`, approached from above.

**Theorem 4.2 (finite modifications; `PROVED`).** Let `a ≥ 0` be an arithmetic function on `n ≥ 2`.
(i) *Deletion.* Let `N ≥ 5` and `a := Λ·1_{n ≥ N}`. Then `D_T(a)` holds for `T < ½ log 2` (`prop:arch`(iii)) and **fails for every**
`T ∈ [T₀(0), ½ log N] = [0.74921, ½ log N]`; on `[½ log 2, 0.74921)` its sign is that of `λ^P_∞(T)`, not decided here
(`DIAGNOSTIC`: negative for `T > 0.5958`, `R155_023:23–24`, `R155_029:11`). No positivity is claimed on `[½ log 2, log 2]`.
(ii) *Amplification.* Let `n₀ ≥ 2`, `c > 0`, `a := Λ + c·1_{n=n₀}`. For every `T` with `2T > log n₀` there is `c_*(T,n₀) < ∞`
such that `D_T(a)` **fails for all** `c > c_*`. In particular (`n₀ = 2`) for every `T > ½ log 2`, including the
range `(½ log 2, log 2]` where `D_T(Λ)` is `PROVED` (Paper 42).
(iii) Both modifications preserve: `a ≥ 0`; `ψ_a(x) := Σ_{n≤x} a(n) = ψ(x) + const` for `x ≥ N` (resp. `≥ n₀`), hence
every partial-sum statement `H_θ`, the prime number theorem with any error term, and any zero-density or
zero-free-region statement read through `ψ_a`; and the meromorphic function
`ζ_a(s) := exp(Σ_n a(n) n^{−s}/log n) = ζ(s)·E(s)`, `E(s) = exp(−Σ_{n<N} Λ(n)n^{−s}/log n)` (resp. `exp(c n₀^{−s}/log n₀)`),
with `E` entire and zero-free: `ζ_a` has **exactly the zeros and the pole of ζ**. Deletion also preserves every
pointwise upper bound (`a ≤ Λ ≤ log n`, Brun–Titchmarsh-type and large-sieve-type upper bounds).
They do **not** preserve the functional equation (`E(s) ≠ E(1−s)`), i.e. the pairing of the comb with `m`.

*Proof.* (i) For `T ≤ ½ log N` the comb of `a` is empty, so `𝔞_T^{(a)} = A_∞|_{P_T}`; positivity for `T < ½ log 2` is
`prop:arch`(iii) (`main.tex:2296`, which covers exactly the empty-contact range `2T < log 2`), and `λ^{P}_{∞}(T) ≤ C₀ + φ((3π/2T)²) < 0` for `T ≥ T₀(0) = 0.74921` is `prop:arch`(ii)
(`thm:SC` with `𝒩 = ∅`); `N ≥ 5` makes `½ log N ≥ 0.8047 > 0.74921`, so the failure interval is nonempty.
(ii) *Lemma 4.2b.* Let `0 < u₀ < 2T`. Then there is a real `F ∈ P_T`, smooth and compactly supported in `I_T`, with
`c_F(u₀) > 0`. Proof: choose `ℓ` with `0 < ℓ < min(u₀, 2T − u₀)`, `J := (−T, −T+ℓ)`; then `J`, `J+u₀`, `J+2u₀` are
pairwise disjoint and `J ∪ (J+u₀) ⊂ I_T`. For `φ ∈ C_c^∞(J)` put `F_φ := φ + φ(·−u₀)`. Then
`c_{F_φ}(u₀) = ⟨F_φ, F_φ(·−u₀)⟩ = ⟨φ + φ_{u₀}, φ_{u₀} + φ_{2u₀}⟩ = ‖φ‖²` (the three cross terms vanish by disjointness).
`V := {F_φ}` is an infinite-dimensional subspace of `L²(I_T)`; `P_T ∩ V` has codimension `≤ 2` in `V`, hence
contains `F_φ` with `φ ≠ 0`, and `c_{F_φ}(u₀) = ‖φ‖² > 0`. ∎ Now with `u₀ = log n₀` and this `F`,
`𝔞_T^{(a)}(F) = 𝔞_T^{Λ}(F) − (2c/√n₀)·c_F(log n₀)`, finite since `F` is smooth, and negative for
`c > c_* := √n₀·max(𝔞_T^{Λ}(F), 0)/(2c_F(log n₀))`. (iii) direct. ∎

**Proposition 4.3 (finitely supported combs; `PROVED`).** Let `a ≥ 0` have finite support `S` and comb mass
`A_S = Σ_S v_n(a)`. Then `limsup_{T→∞} λ^A_T(a) ≤ C₀ − A_S < 0`; in particular `D_T(a)` fails for all large `T`.
This holds for every truncation `Λ·1_{n<N}` and for the empty comb (where it recovers `λ ↓ C₀`, `prop:arch`(ii)).
*Proof.* For `g ∈ C_c^∞(−1,1)`, `g ≠ 0`, put `G_T(t) := g(t/T)` and `F_T := (−∂_t² + ¼)G_T ∈ C_c^∞(I_T)`. Two integrations
by parts give `A(F_T) = ∫G_T(−∂² + ¼)e^{t/2}dt = 0` and likewise `B(F_T) = 0`, so `F_T ∈ P_T`; and
`F̂_T(τ) = (τ² + ¼)Ĝ_T(τ) = (τ²+¼)·T ĝ(Tτ)`. With `σ := m − Σ_S v_n cos(τ log n)` (independent of `T` once `2T > max_S log n`),
```
𝔞_T(F_T)/‖F_T‖² = ∫ σ(s/T)(s²/T² + ¼)²|ĝ(s)|² ds / ∫ (s²/T² + ¼)²|ĝ(s)|² ds → σ(0) = C₀ − A_S (T → ∞)
```
by dominated convergence: `|σ(s/T)| ≤ C(1 + log(2+|s|))` (`lem:mbounds`(ii) and `|comb| ≤ A_S`), `ĝ` Schwartz, `σ`
continuous at `0`. ∎
`HEURISTIC` reading: the low-frequency primitive test `F_T` is the one every *fixed* comb loses to; for ζ the comb
grows with `T` (`A_T ~ 4e^T`) and `σ_T(s/T) ↛ σ_T(0)` because `cos((s/T) log n)` with `log n` up to `2T` does not tend to
`1` — the new atoms are what can defeat this test. This is `thm:SC`'s "positivity is collective" seen from the
primal side.

**Corollary 4.4 (classical prime-side results are void per window; `PROVED`).** Let `𝒞` be a class of nonnegative
arithmetic functions containing `Λ`. If `𝒞` is closed under deletion of finitely many terms, then for every
`T ≥ 0.74921` some `a ∈ 𝒞` fails `D_T(a)`; if `𝒞` is closed under amplification of one term, then for every
`T > ½ log 2` some `a ∈ 𝒞` fails `D_T(a)`. The classes
 `C_PNT(θ) = {a ≥ 0 : ψ_a(x) = x + O(x^θ)}` (any fixed `θ`, and any weaker error term such as the de la Vallée Poussin
 or Korobov–Vinogradov one), `C_zeros(Z) = {a ≥ 0 : ζ_a = ζ·E, E entire zero-free}` (zeros and pole of ζ, hence every
 zero-free region and zero-density statement), are closed under both operations;
 `C_BT = {a : 0 ≤ a ≤ Λ}` (every upper-bound sieve statement: Brun–Titchmarsh, large sieve, `a(n) ≤ log n`) is closed
 under deletion.
Consequently, in the form of Paper 47 Thm 18.1(ii): a derivation of `D_T` whose only prime input is `𝒞`-membership is a
derivation of `D_T(a)` for every `a ∈ 𝒞`, hence proves a false statement for the member of Thm 4.2 — **so no such derivation
exists, at any window `T ≥ 0.74921` (and, for `C_PNT`, `C_zeros`, at any `T > ½ log 2`)** — a fortiori none yields `D_T`
for some `T` beyond `log 2`. The dichotomy asked for in the task is: either `𝒞 ⊆ 𝒞_D := {a : ∀T D_T(a)}` (then
"`𝒞` forces `∀T D_T`" is the definition of `𝒞`, and `Λ ∈ 𝒞` *is* RH by Prop. 1.3), or `𝒞` has a member failing some `D_T`;
every class defined by an asymptotic, a zero statement or an upper-bound sieve statement is of the second kind.
*Proof.* Thm 4.2 and Prop. 1.3. ∎

**Remark 4.5 (the complementary class; cited, not redone).** Paper 47 T2 (§18.2, `46/main.md:4822–4916`; X21 at
`3975`) exhibits `Ξ_Q` (Epstein, `h(−D) > 1`): entire of order `1`, real, `Ξ_Q(s) = Ξ_Q(1−s)`, polar set `{0,1}`, coefficients
`r_Q(n) ≥ 0`, and zeros in `Re s > 1` (Davenport–Heilbronn), so its Weil form is negative on some window. Together with
T1 (Thm 18.1: functional equation and pole are shared by every `ξ_K`), this is the FE-side half of the void:
hypotheses on the archimedean/functional-equation side alone do not give `D`; Thm 4.2 is the comb-side half:
hypotheses on the prime sequence alone (asymptotics, zeros, sieve bounds) do not give `D`. `PROVED` (both halves).

**Proposition 4.6 (synthesis: the coupling is irreducible; `PROVED` as a method constraint).** Any sound
derivation of `D_T` for ζ must use at a load-bearing step a hypothesis that (a) is *not* preserved by finite
modification of the comb (Cor. 4.4) — hence pins the actual values `Λ(n)`, `n ∈ N_T`, and not only their
asymptotics — and (b) is *not* shared by every `ξ_K` and not implied by FE + pole + reality + `r ≥ 0` (T1, T2). [`HEURISTIC`, interpretive, no minimality proved: the
minimal hypothesis with both properties is the joint statement "these values of `Λ(n)`, paired with `m` on `P_T`",
which is `D_T` itself.] Per window, the only derivations of record are computations with the actual vector
(Paper 42 at `T ≤ log 2`; Zhu at support `1.6`, `cor:KEP08`; `thm:C` at `½ log 3` in Paper 46). ∎
`HEURISTIC` corollary: a proof of `∀T D_T` cannot proceed by "prime input + archimedean input" separately; it must be
a statement about the sequence `(Λ(n))` *as paired with `Γ`* that is uniform in `T` — which is what §28.2 of Paper 47
states qualitatively and what this memo makes exact.

---

## 5. Labels of record (one line each)

| statement | label |
|---|---|
| Prop 1.1 (`D_T` = membership of the finite vector `v_T` in the closed convex `𝒟_T`; `0 ∉ 𝒟_T` for `T ≥ 0.74921`) | PROVED |
| Cor 1.2 (regime constancy of `σ_T`; `λ^A` nonincreasing inside a regime) | PROVED |
| Prop 1.3 (arithmetic content = uniformity) | PROVED |
| Prop 2.1 (`{σ<0}` finite union of intervals; `τ_* ≤ τ₁(A)`, `τ₁ = 60.5432 / 120.0865`) | PROVED (roots: elementary numerics) |
| Prop 2.2 (alignment structure; components beyond `τ_a = 23.34` at `\|k log 3 − l log 2\| < 0.448`; `≤ 6 / 12` arcs) | PROVED |
| Table 2.2a interval endpoints, `τ_* = 46.129 / 108.950` | DIAGNOSTIC |
| `τ_* ∈ [45.642, 60.544]` and `∈ [108.723, 120.087]` | PROVED modulo double-precision evaluation (margins `0.21` / `0.077` ≫ rounding) |
| convergent structure `(5,8), (12,19)` of the last components | DIAGNOSTIC (observation) |
| Prop 2.3 (`Neg_T` trace class, `tr = (2T/2π)∫σ₋`; band carries all negativity; band alone does not decide the sign, via `σ ∓ c·1_{off band}` and `λ₀ < 1`) | PROVED; values DIAGNOSTIC |
| Lemma 3.0 (with `τ_env(w)` defined as a root), Lemma 3.1b (complete-form non-attainment), Thm 3.1(a),(c) | PROVED |
| Thm 3.1(b): `[∃w ∈ 𝒲_T: 𝖠_T(w)] ⟺ λ^W_T > 0` (`T ≥ ½ log 2`) | PROVED |
| per-window converse `λ^A ≥ 0 ⟹ λ^W ≥ 0` | OPEN (not on record) |
| Thm 3.2(i)–(iii),(v) | PROVED (citations); (iv) logical remark; effective `T(β₀)` OPEN |
| Prop 4.1 (`𝔈_T = −λ^W_T`; RH `⟺ lim λ^W_T ≥ 0`) | PROVED; `λ^W ↓ 0` HEURISTIC |
| Thm 4.2 (deletion: positive for `T < ½log2`, fails on `[0.74921, ½log N]`; amplification; Lemma 4.2b) | PROVED; sign on `[½log2, 0.74921)` not decided |
| Prop 4.3 (finitely supported combs fail for large `T`; `limsup λ^A ≤ C₀ − A_S`) | PROVED |
| Cor 4.4 (classical prime-side results void per window) | PROVED (method-constraint form, as Paper 47 Thm 18.1) |
| Prop 4.6 (irreducibility of the coupling) | (a),(b) PROVED as method constraint; "minimal hypothesis" sentence and last sentence HEURISTIC |

No sign for ζ beyond `log 2`. No value of `inf W` at `log 2`. Row-D label unchanged.

## 6. Least certain points

1. **Prop 4.3, dominated convergence.** Check the bound `|σ(s/T)| ≤ C(1+log(2+|s|))` uniformly in `T ≥ 1` (it uses
 `m(τ) ≤ log(τ/2π) + 1/τ + …` for `τ ≥ 1` and boundedness of `m` on `[0,1]`), and that `F_T ∈ P_T` (two integrations
 by parts, boundary terms vanish by compact support). The conclusion `limsup ≤ C₀ − A_S` must be consistent with
 `prop:arch`(ii) (`λ ↓ C₀` for the empty comb): it is.
2. **Lemma 4.2b.** The disjointness needs `ℓ < u₀` (three supports) and `ℓ < 2T − u₀` (inside `I_T`); the
 codimension argument needs `V` infinite-dimensional (it is: `φ ↦ F_φ` is injective). For `n₀ = 2`, `u₀ = log 2`,
 any `T > ½ log 2` works.
3. **Prop 2.3(i) trace formula.** `tr(Q_T f(D) Q_T) = (2T/2π)∫f` for bounded compactly supported `f ≥ 0`: standard;
 the corpus precedent is `R155_039:78–80`. Step (v) uses `λ₀(Tτ_*) < 1` for the prolate operator (strict, classical);
 both replacements now use it (per R155_058); check `I − Q_T 1_{band}(D) Q_T ≥ (1−λ₀)` on `L²(I_T)` (`Q_T` is the identity there).
4. **Numerics.** `τ₁`, `τ_a`, `τ_b`, `τ_b'`, `y₀` are roots of explicit monotone equations (double precision); the two
 witnesses use `m ≤ m_up` (`lem:mbounds`(ii), PROVED) and double-precision `cos`/`log` with margins `0.21` and
 `0.077` — twelve orders of magnitude above rounding, but an interval-arithmetic check would make them
 certificate-grade. Interval endpoints in Table 2.2a are bisection values, DIAGNOSTIC.
5. **Per-window converse.** I state that `λ^A_T ≥ 0 ⟹ λ^W_T ≥ 0` (or `⟹ λ^P_T ≥ 0`) is not on record. Please confirm
 by grep that no corpus theorem gives it; if one exists, Thm 3.1(b) sharpens to a per-window equivalence.
6. **`prop:env`(iii) wording.** The paper calls `2πe^{A_T}` "the threshold" (`59.5`, `main.tex:1041`); the exact
 zero of the multiplier-free lower envelope is `τ₁ = 60.54` (Prop 2.1(v)). Nothing false (`τ_* = 46.13 < 59.5 < 60.54`),
 but the editor may want "`2πe^{A_T}(1+o(1))`" or the exact `τ₁`.
7. **Arc count vs component count.** Prop 2.2 bounds the number of *arcs* `|τ log 2 − 2πk| < δ₂` that can contain
 negative components, not the number of components (two components could share an arc). Observed: `2` and `4`
 components against bounds `6` and `12`.
8. **Thm 3.2(iv).** The "negative" is a statement about derivations/classes, not about ζ. I have tried to say so
 exactly; the audit should check that no sentence in §3–4 slides into "PNT does not imply RH" as a fact.
9. **Cor 4.4 for the zero-free-region class.** The class `C_zeros(Z)` is defined through `ζ_a = ζ·E` with `E` entire
 zero-free; a skeptical reader may prefer a class defined intrinsically by a zero-free region of `ζ_a` in a
 half-plane. Both readings are closed under (i),(ii) since `E` never vanishes; the memo uses the former.

## 7. Plain-language verdict: is P6 closed?

**P6 is closed, as an equivalence — the outcome PATH-TO-D predicted as "likely and expected".** The sharpest
prime-side inequality that gives row D at a window is `𝖠_T(w)`: the smoothed prime sum
`−2Re Σ Λ(n)n^{−½−iτ}w(log n)` must not fall below `−(M_w + Π_w)` on the band `[0, τ_env]`; that inequality is
literally `f_w ≥ 0`, it implies `D_T`, it is implied by `λ^W_T > 0`, and its solvability for every `T` is RH
(Thm 3.1). There is no isolated arithmetic statement `X` strictly weaker than `D_T` from which `D_T` follows: at a
fixed window the whole statement concerns the finitely many numbers `Λ(n)`, `n < e^{2T}`, paired with the
Γ-function (Prop 1.1), so no asymptotic, zero-theoretic or sieve-theoretic property of the primes can be
load-bearing there — such properties are shared by combs for which `D_T` fails (Thm 4.2, Cor 4.4) — and the
functional-equation side alone cannot be load-bearing either (Paper 47 T1/T2). What P6 has produced is
positive knowledge of a different kind: the exact per-window quantity is `𝔈_T = −λ^W_T`, RH is
`lim_{T→∞} λ^W_T ≥ 0` (Prop 4.1); the negative set of the symbol is a finite union of intervals located, beyond
`τ ≈ 23`, at Diophantine near-coincidences `2^l ≈ 3^k` (`(5,8)` and `(12,19)` carry the last sign changes in
the two computed regimes) with proved bounds on their number and position (Props 2.1–2.2); all negativity of
the form lives on that band through a trace-class operator with explicit trace, while positivity is a global
balance the band alone cannot decide (Prop 2.3). The arithmetic content of row D is therefore exactly one
statement — uniformity in `T` of `v_T(Λ) ∈ 𝒟_T` — and it cannot be split into a prime-side part and an
archimedean part. Nothing here moves the row-D label; no sign for ζ beyond `log 2` is claimed.

---

## 8. Amended per R155_058 (audit, round 8B)

Every change made in place; no new claims.
1. **Thm 4.2(i)** (mandatory): positive clause replaced by "`D_T(a)` holds for `T < ½ log 2` (`prop:arch`(iii))"; the earlier
 "holds for `T ≤ log 2`" was unsupported (`prop:arch`(iii) covers only the empty-contact range) and contradicted the
 DIAGNOSTIC record `T*_{∞,P} ≤ 0.5958`; the sign on `[½ log 2, 0.74921)` is now stated as not decided, with the DIAGNOSTIC
 note. The failure clause `[0.74921, ½ log N]` is unchanged; nothing downstream used the positive clause. Proof and §5 table adjusted.
2. **Prop 2.3(v)** (mandatory): the invalid negative replacement `σ₊ ↦ 0 off the band` (σ₊ is not supported off the band)
 replaced by `σ ↦ σ − c·1_{|τ|>τ_*}` with `c > sup σ₊/(1−λ₀(Tτ_*))`; both replacements now rest on the prolate bound
 `λ₀ < 1`; statement, proof and §5 table rewritten. §2 "Reading" sentence adjusted.
3. **Prop 1.1(iii)** (mandatory): hypothesis `v ≥ 0` added (thm:SC is stated for nonnegative weights); the signed version
 with `Σ|v_n|` noted.
4. **Lemma 3.1b** (new, one paragraph): non-attainment for the complete form, same proof as `thm:O`; **Thm 3.1(b)** now records
 the exact per-window statement `[∃w ∈ 𝒲_T: 𝖠_T(w)] ⟺ λ^W_T > 0`, `T ≥ ½ log 2`, and the bare citation of `thm:O` (stated
 for `λ^P`) is removed. Prop 4.1 upgraded accordingly ("solvable", not "strictly solvable").
5. **Thm 3.1(c), Prop 4.1**: quantifiers restricted to `T ≥ ½ log 2` where `cor:RH`/`thm:Zexh` are stated; the `T < ½ log 2`
 range noted as `prop:arch`(iii).
6. **Lemma 3.0**: `τ_env(w)` defined as the unique root of `m_lo − A_T − ‖ν_w‖_TV − 2k₀ = 0`; the inequality
 `τ_env(w) ≥ 2πe^{A_T}` dropped (replaced by the `− o(1)` form; the comparison with `τ_*` marked DIAGNOSTIC and unused).
7. **Rem 3.1a(iii)**: "for `w ∈ 𝒲_T^{reg}`" added (`thm:Z`(ii) is stated for regular `w`).
8. **Witness labels**: "PROVED modulo double-precision evaluation" in Table 2.2a paragraph and §5 table.
9. **Prop 4.6**: the "minimal hypothesis is `D_T` itself" sentence labelled HEURISTIC (no minimality is proved).
10. **Rename**: `X_T` → `𝖠_T(w)` throughout (Paper 47 uses `X_T` for the Tate collar); header paragraph rewritten; the
 corpus-grep line keeps the literal string `X_T` because that is what was grepped.
11. Editorial (from the audit): Cor 4.4 rephrased in the Paper 47 Thm 18.1(ii) form ("proves a false statement for the member
 of Thm 4.2 — so no such derivation exists") instead of "is not sound".
Unchanged: all numerics (reproduced by the audit to the printed digits), Props 1.3, 2.1, 2.2, 4.3, Thm 3.2, Rem 4.5. Row-D
label unchanged; no sign for ζ beyond `log 2`; no value of `inf W` at `log 2`.

---
**[Erratum, found by the Paper 46 integrating editor after audit `R155_058`]** Prop 2.3(v), negative
replacement: the audited symbol `σ − c·1_{off band}` with `c > sup σ₊/(1−λ₀)` is void, because `σ ≍ log τ` makes
`sup σ₊ = ∞`; the claim that both replaced symbols are bounded is false. Repaired (as in Paper 46 §10.5) by the
audit's alternative symbol `σ·1_band − c·1_off`, `c > max_band σ₊/(1−λ₀)`, with `λ₀(S_{T,τ_last}) < 1` proved in
place (entire-function argument). Conclusion of Prop 2.3(v) unchanged. Also: statements "for `T ≥ T₀(0) = 0.74921`"
hold for `T > T₀(0)` (at `T₀(0)` the `thm:SC` bound is `0`); the same endpoint slip is in Paper 46 `thm:SC`,
`prop:arch`(ii) — referred to review R4.
