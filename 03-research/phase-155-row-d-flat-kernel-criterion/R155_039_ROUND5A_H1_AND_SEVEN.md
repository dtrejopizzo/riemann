# R155.039 — round 5a: (H1) by a Birman–Schwinger count, and the nodal law of the 76 %

*[amended per R155_042]: E1 (2π/τ₀ = 0.9989426, T₂ ≤ not <), E2 (tr M₋ = 4.495774·T), E3
(scope, mixed spaces), E4 (missing ceiling), E5 (P_T bound vacuous at both windows), E6 (Theorem J′
demoted to unlabelled remark), E7 (6.65 %), E8 (3 digits), E9 (≈ 6.7 min); "both sides proved" now
cites R155_023 Prop 3(ii) (min–max upper bound), not Prop NC's 68.51·T; tr(M₊⁻¹M₋) noted as
plausibly +∞ (Galerkin values are lower bounds growing with N).*

*Phase 155, round 5a. Executes the round-5 orders (i) and (ii) of `R155_038 §3`.
Inherits `R155_033` (Prop NC and its overcount mechanism), `R155_032` (Thm 4a.1, Prop 4a.4, the
`π_ij` table), `R155_023` (`τ₀ = 6.28983599`, `m(τ) = C₀ + ∫₀^∞(1−cos τu)K(u)du`), Paper 47 §2
(`lem:K`, `thm:S`, `lem:mbounds`) and §8 (`prop:arch`, `prop:schur`). Paper 47, `R155_033`
and `R155_034` are **not** touched. Scripts: `scripts/r5a/` (`r5a_01`…`r5a_04`, ≈ 6.7 min total).*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`
(Paper 47 Thm C). No value of `inf W` at `log 2` is asserted (the `R155_038` withdrawal stands).**

---

## §0 Verdict in six lines

1. **(i) is a NEGATIVE, and quantitatively so.** The Birman–Schwinger route degenerates because
 `M₊` (symbol `m₊`, which vanishes identically on `|τ| < τ₀`) has **no spectral gap** on the
 window: Galerkin `λ_min(M₊) = 2.9·10⁻³` at `½log3` and `5·10⁻⁴` at `log 2` (and falling with `N`),
 so `tr(M₊^{−1}M₋) = 584` and `3548` (Galerkin lower bounds, growing with `N`; since `M₊`'s
 spectrum accumulates at `0`, the true `tr(M₊^{−1}M₋)` is plausibly `+∞`) — an order of magnitude
 **worse** than Prop NC's `37`/`47`.
 Every `ε`-shifted variant fails for a sign reason given in §2.2. **`(H1)` stays `HYPOTHESIS`;
 no `T₂` is produced. Prop NC's `68.5135·T` remains the best proved upper bound.**
2. **But the round produces the missing half: a PROVED LOWER bound, vacuous at the two windows of
 record.** Theorem J below gives `n₋(Γ_T on L²(−T,T)) ≥ #{k ≥ 1 : kπ/2T < τ₀} = ⌈2Tτ₀/π⌉ − 1`,
 hence `n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3`; at `½log3` and `log 2` this `P_T` bound evaluates to `0`
 (vacuous) — see §2.4. This upgrades the `HEURISTIC` half of `R155_023` Prop 3(ii) to `PROVED`:
 `n₋(T) = (2τ₀/π)T + O(log T)` is now proved on both sides — the upper half by `R155_023` Prop
 3(ii) (min–max, `PROVED`), not by Prop NC's `68.51·T`, which is a different, non-matching, explicit
 bound — with `2τ₀/π = 4.00405`.
3. **A hard explicit constant for (H1) falls out:** `n₋(A_∞|P_T) ≥ 2` once `2Tτ₀/π > 4`, i.e.
 **any `T₂` in (H1) satisfies `T₂ ≤ 0.9989426`** (`PROVED`). `(H1)` is therefore a statement about a
 bounded window, and `log 2 = 0.6931` sits comfortably inside it.
4. **Why every moment/Dirichlet route can only give upper bounds (REMARK, the concavity no-go —
 not a theorem; see E6/§2.4).**
 `m(τ) − C₀ = φ(τ²)` with `φ` complete Bernstein (`thm:S`), hence **concave**; Jensen therefore
 always runs `A_∞(F) ≤ C₀ + φ(‖F′‖²)`. The ceiling direction is free; a matching floor needs the
 *spread* of `|F̂|²`, i.e. exactly a prolate concentration estimate. This is the structural reason
 the two-level bound of Prop NC, the Chebyshev tail of `R155_001` and the BS count all fail alike.
5. **(ii) is a structural YES.** The sign of each prime atom of `π₁₃` is a **nodal** statement, and
 an exact one: `⟨Re(R_Tτ_aR_T)F*, e⟩ = ∫_{a−T}^{T} F*(z−a)\,e(z)\,dz` (Lemma N, `PROVED`, two
 lines). At `log 2` the overlap `I(a)` has zeros at `a = 0.2128, 0.6087, 1.0225`, and
 **`log 2 = 0.6931` and `log 3 = 1.0986` straddle the third zero `a_c = 1.0225`** — that, and
 nothing numerical, is the `76 %` cancellation. The same straddle holds at `0.62` and `0.65`.
6. `T ↦ a_c(T)` is what the criterion of Prop G below asks about; the geometric criterion for the
 `2`-plane is **"the contact set must straddle a zero of `I(·)`"**, and the outermost zero tracks
 the node `z_F` of `F*` (`a_c ≈ T + z_F`, residual `≤ 0.015` at three windows: `DIAGNOSTIC`).

---

## §1 Corpus check (grep, whole repo, `*.md` + `*.tex`)

| term | files | what is there | what is new here |
|---|---|---|---|
| `Birman` / `Schwinger` | **44** | phases 106/114/116 use Birman–Schwinger as a *gate* on the Connes/Tate side (`114_d_50`, `114_d_52`, `114_d_134/135`, `106_59`, `106_132`); all are about the modular/screw operators, none about `A_∞` on a window | the count with the *variable symbol* `m` on `L²(−T,T)`; and its **refutation** by the no-gap mechanism |
| `Cwikel` | **2** (`R155_033` itself; `phase-60/attack-gap-i-improved-hardy.tex`) | mentioned, never carried out | §2.2 shows a CLR-type bound is unavailable: the free part has no gap and `M₋` is not `L^{p}`-controlled on a 1-D window |
| `Lieb` (Lieb–Thirring) | **8**, all Connes/Jacobi-side | — | §2.2: the LT inequality gives `Σ|λ_j^-|^{γ}`, and at `γ → 0` (the counting case) it is exactly the unavailable CLR bound in `d = 1` |
| `nodal` | **102** | mostly Hermite/prolate nodal talk in phases 60/78/114; **nothing on the nodal position of the prime shift** | Lemma N + Prop G are new: the atom sign as a nodal-crossing statement |
| `oscillation` | **162** | generic | — |
| `Bonami` (–Karoui) | **2** (`R155_033`, `phase-61/respuestas3.md`) | still not in `00-references` | unchanged: the `CONDITIONAL` upgrade of §2.4 still needs the citation |
| `prolate` | **381** | the standard equipment | Theorem J needs **no** prolate input — it uses Dirichlet modes and concavity only |

---

## §2 Task (i): the Birman–Schwinger count

### 2.1 Setting and the exact split

On `P_T` the pole term vanishes and `A_∞(F) = (1/2π)∫ m|F̂|²` (`prop:arch`). With
`m₊ = max(m,0)`, `m₋ = max(−m,0)`: `m₋` is supported in `|τ| < τ₀ = 6.28983599`, `0 ≤ m₋ ≤ −C₀ =
5.3721834`, and `A_∞ = M₊ − M₋` with `M_± = Q_T m_±(D) Q_T ≥ 0` on `L²(−T,T)`.
`M₋` is trace class with the **closed form**

> `tr M₋ = (2T/π)·∫₀^{τ₀}(−m(τ))dτ = (2T/π)·7.061946 = 4.495774·T`
> (`= 2.4696` at `½log3`, `3.1162` at `log 2`) — `PROVED` (the trace of `Q_T f(D) Q_T` is
> `(2T/2π)∫f`), the number `7.061946` `DIAGNOSTIC`.

`M₊ > 0` strictly (if `⟨M₊F,F⟩ = 0` then `F̂` vanishes off `|τ| < τ₀`, and `F̂` is entire of
exponential type `T`, so `F = 0`) — `PROVED`, as the order anticipated. Birman–Schwinger then says
`n₋(M₊ − M₋) = #{ λ(M₊^{−1/2}M₋M₊^{−1/2}) > 1 } ≤ tr(M₊^{−1}M₋)`.

### 2.2 Why it fails (the no-gap mechanism). `PROVED` (structure) / `DIAGNOSTIC` (numbers)

`M₊ > 0` **without a spectral gap**: `inf spec M₊` is not bounded below by anything useful, because
the near-band-limited prolate quasi-modes make `⟨M₊F,F⟩` tiny while `m₊` only grows like `log τ`
(`lem:mbounds`). Galerkin (`r5a_01`, `N = 18`, Legendre/Bessel symbol quadrature, cross-checked
against the kernel matrix of `arch_core.gamma_matrix` to `1.1·10⁻²` relative):

| `T` | `λ_min(M₊)` (Galerkin, upper bd) | `tr M₋` | `tr(M₊^{−1}M₋)` | `tr M₋ / λ_min(M₊)` | Prop NC `68.51T` | computed `n₋(P_T)` |
|---|---|---|---|---|---|---|
| `½log3` | `2.9·10⁻³` | `2.4696` | **`584`** | `865` | `37.6` | `0` |
| `log 2` | `5.0·10⁻⁴` | `3.1162` | **`3548`** | `5948` | `47.5` | `1` |

So the BS bound is **two orders of magnitude worse** than the crude min–max bound it was meant to
replace. The `ε`-regularisations of the order do not repair it, for a sign reason:
`A_∞ = M₊ − M₋ ≤ (M₊+ε) − M₋`, so `n₋(A_∞) ≥ n₋((M₊+ε) − M₋)` — the shift moves the count the
**wrong way**; the only correct shift is `A_∞ ≥ (M₊+ε) − (M₋+ε)`, whose BS operator carries `εI`
and is not trace class. A CLR/Cwikel bound is likewise unavailable: in `d = 1` CLR fails, and the
"free" operator here is `M₊`, gapless and non-elliptic (its symbol vanishes on a whole band).
**Conclusion: the Birman–Schwinger route for (H1) is closed. `(H1)` remains `HYPOTHESIS`; the best
proved upper bound is Prop NC's `n₋ ≤ 68.5135·T` (`47` at `log 2`).**

### 2.3 Theorem J (the proved lower bound, and the hard limit on `T₂`). `PROVED`

Let `Γ_T` be the archimedean form without the pole term, `Γ_T(F) = C₀‖F‖² + Lev(c_F)`, on
`L²(−T,T)`.

> **Theorem J.** `n₋(Γ_T) ≥ #{ k ≥ 1 : kπ/(2T) < τ₀ } = ⌈2Tτ₀/π⌉ − 1`, and consequently
> `n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3`.

*Proof.* Let `D_k ⊂ H¹₀(−T,T)` be the span of the first `k` Dirichlet modes `sin(jπ(t+T)/2T)`,
`j ≤ k`. For `F ∈ D_k` (extended by `0`), Plancherel gives `(1/2π)∫τ²|F̂|² = ‖F′‖² ≤ (kπ/2T)²‖F‖²`.
By `thm:S`, `m(τ) − C₀ = φ(τ²)` with `φ` complete Bernstein, hence concave on `(0,∞)`; applying
Jensen to the probability measure `dμ = |F̂|²dτ/(2π‖F‖²)` in the variable `τ²`,
`Γ_T(F)/‖F‖² = C₀ + ∫φ(τ²)dμ ≤ C₀ + φ(∫τ²dμ) = C₀ + φ(‖F′‖²/‖F‖²) ≤ C₀ + φ((kπ/2T)²)`.
Now `φ(τ₀²) = −C₀` **exactly** (definition of `τ₀`: `m(τ₀) = 0`; verified to `1.2·10⁻¹⁰`, `r5a_04`),
and `φ` is strictly increasing, so `kπ/2T < τ₀` forces `Γ_T < 0` on `D_k∖{0}`, i.e. `n₋(Γ_T) ≥ k`.
The last clause is `codim(P_T) = 2`. ∎

**Consequences.** (a) With `R155_023` Prop 3(ii)'s upper bound `n₋ ≤ 2Tτ₀/π + O(log T) + 2` (min–max,
`PROVED`), the asymptotic `n₋(T) = (2τ₀/π)T + O(log T) = 4.00405·T + O(log T)` is now **`PROVED` on
both sides** (previously `PROVED` above / `HEURISTIC` below), citing `R155_023` Prop 3(ii) for the
upper half — **not** Prop NC's `68.51·T`, which is a different, explicit-in-`T`, non-matching bound.
(b) `⌈2Tτ₀/π⌉ − 3 ≥ 2` as soon as `2Tτ₀/π > 4`:

> **`(H1)` cannot hold beyond `T = 2π/τ₀`, explicitly `T₂ ≤ 0.9989426`** (`PROVED`).

Checks (`r5a_04` against the Galerkin counts of `r5a_01`): `T = ½log3`, bound `2`, computed
`n₋(Γ_T) = 2` — **sharp**; `T = log 2`, bound `2`, computed `3`.

**The `P_T` bound is vacuous at both windows of record.** `n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3` evaluates to
`≥ 0` at `T = ½log3` and at `T = log 2` — no non-vacuous `P_T` count is obtained there; the
non-vacuous content of Theorem J at these two windows is the `Γ_T` (i.e. `L²`) count and the
asymptotic corollary. The bound first becomes non-vacuous (`≥ 1`) for `T > 3π/(2τ₀) ≈ 0.74922`, and
`≥ 2` for `T > 2π/τ₀ = 0.9989426` (the `T₂` consequence above).

### 2.4 What is missing for `n₋ ≤ 1`

REMARK (the concavity no-go — not a theorem; only the ceiling inequality is proved): because `φ` is
concave, every Jensen/moment/Dirichlet argument produces a **ceiling** `A_∞(F) ≤ C₀ + φ(‖F′‖²)`
(`PROVED`) and never a floor; a floor requires a lower bound on `∫min(τ²,X)dμ`, i.e. control of the
*spread* of `|F̂|²`, i.e. a quantitative statement that a function supported in `(−T,T)` cannot
concentrate its spectrum in `|τ| < s`. That is precisely an explicit non-asymptotic prolate estimate.
This "no-go" is a reading, not a formalised claim: it quantifies over an unformalised class ("every
Jensen/moment/Dirichlet argument") and the "⟺ prolate spread bound" is informal. Hence, unchanged
from `R155_033 §3.4`: importing **Bonami–Karoui** (still not in `00-references`; `CONDITIONAL` on the
citation) would give `n₋ ≤ 5` at `log 2` — not `1`. Nothing in this round shortens that gap. The
honest state is

`0 ≤ n₋(A_∞|P_{log2}) ≤ 47` (`PROVED`, on `P_T` — not mixed with the `L²` bound `2 ≤ n₋(Γ_{log2}) ≤ 49`),
`n₋(A_∞|P_{log2}) = 1` (`DIAGNOSTIC`), `T₂ ≤ 0.9989426` (`PROVED`).

---

## §3 Task (ii): the analytic structure of the even Schur complement at `log 2`

`S_even = A_∞ + Π_T − (Π_TF*)(Π_TF*)^*/w₁₁` on `V_even`, with `Π_T = −v₂Re(R_Tτ_{log2}R_T) −
v₃Re(R_Tτ_{log3}R_T)` at `log 2` (Prop 4a.4; `log 4 = 2T` excluded), `v₂ = 0.98026`, `v₃ = 1.26864`.

### 3.1 Lemma N (the atom is a one-sided overlap). `PROVED`

> For `a ∈ (0,2T)` and `F, e ∈ L²(−T,T)` **even**, with `~` denoting extension by zero,
> `⟨Re(R_Tτ_aR_T)F, e⟩ = ½∫F(y)(ẽ(y+a)+ẽ(y−a))dy = ∫_{a−T}^{T} F(z−a)\,e(z)\,dz =: I_{F,e}(a)`,
> and the atom of `n` in `π_ij` is `−v_n·I_{e_i,e_j}(log n)`.

*Proof.* Unfold the truncated shift and use evenness of `F` and `e` to identify the two half-terms. ∎

Verified to `3` digits (quadrature level) against `r4a_01`'s matrix (`r5a_02`): at `T = log 2`,
`−v₂I(log2) = +0.1867`, `−v₃I(log3) = −0.1410`, reproducing the `π₁₃ = +0.0457`, `76 %` line of
`R155_032 §2`.

### 3.2 The geometry, and where the two signs come from. `DIAGNOSTIC` (numbers) / `PROVED` (Prop G)

At `T = log 2` the even eigenfunctions have nodes (`r5a_02`, `N = 18`):
`e₃`: `±0.1505, ±0.4786`; `F* = e₁`: `±0.3152` (so `F*` is **not** of one sign on `P_T` — the two
Tate constraints force one sign change; `∫F* = 0.0181`, negative mass `−0.5244`). The order's
guess "`F*` a positive bump" is therefore **false**, and the clean `F* ≥ 0` lemma it proposed is
not available; what survives is the window statement of Lemma N.

Because `a = log 2 = T` exactly at this window, the log-2 atom integrates over `z ∈ (0,T)` (half the
window) and the log-3 atom over `z ∈ (0.4055, 0.6931)` — a short interval **centred on the outer
node `z_e = 0.4786` of `e₃`**. The sign split in the integrand:

| `a` | window `(a−T,T)` | sign of `e₃` on it | sign of `F*(·−a)` | `I(a)` | atom `−v_nI` |
|---|---|---|---|---|---|
| `log 2` | `(0, 0.6931)` | `+ − +` (nodes `0.1505, 0.4786`) | `− −` then `+` (node at `0.378`) | `−0.1904` | `+0.1867` |
| `log 3` | `(0.4055, 0.6931)` | `− +` (node `0.4786`) | `−` throughout | `+0.1111` | `−0.1410` |

> **Proposition G (sign-forcing, `PROVED`).** If `a − T > z_e` (the window lies inside the last lobe
> of `e`, where `e > 0`) and `a > T + z_F` (the pulled-back window lies inside the last lobe of `F`,
> where `F < 0`), then `I_{F,e}(a) < 0` and the atom `−v_nI` is `> 0`. Hence the sign is *forced*
> for all `a > a^* := T + max(z_e, z_F)`.

At `log 2`: `a^* = T + z_e = 1.1717`, and `log 3 = 1.0986` **misses it by `0.073` (6.65 %)**. That is
the sharp statement of "the log-3 atom is where the sign is still free": one contact more (or a
window `≈ 7 %` wider) and both atoms would be forced positive and there would be no cancellation.

### 3.3 The criterion: the contact set must straddle a zero of `I`. `DIAGNOSTIC`

Scanning `a ↦ I_{F*,e₃}(a)` on `(0,2T)` (`r5a_03`, 220 points):

| `T` | nodes `z_e / z_F` | zeros of `I(a)` | `I(log2)` | `I(log3)` | straddle? |
|---|---|---|---|---|---|
| `log 2 = 0.69315` | `0.4786 / 0.3152` | `0.2128, 0.6087, **1.0225**` | `−0.1904` | `+0.1111` | **yes** |
| `0.65` | `0.4486 / 0.2952` | `0.1992, 0.5704, **0.9584**` | `−0.2682` | `+0.1429` | **yes** |
| `0.62` | `0.4278 / 0.2813` | `0.1898, 0.5438, **0.9139**` | `−0.3041` | `+0.1182` | **yes** |

Two of the three zeros are identified geometrically (`DIAGNOSTIC`, residuals in brackets):
the first at `a = T − z_e` (`0.2145` vs `0.2128` [`0.0017`]; `0.2014` vs `0.1992`; `0.1922` vs
`0.1898`) — the window's left edge crosses the outer node of `e₃`; the third at `a = T + z_F`
(`1.0083` vs `1.0225` [`0.014`]; `0.9452` vs `0.9584`; `0.9013` vs `0.9139`) — the pulled-back
edge crosses the node of `F*`. The middle zero is not matched by either rule.

> **Geometric criterion (`DIAGNOSTIC` as a criterion, `PROVED` as an equivalence).** By Thm 4a.1 the
> `2`-plane determinant is `w₁₁(λ₃+π₃₃) − (Σ_n v_nI(log n))²`, so the `2`-plane at `log 2` is
> positive **iff** the atoms cancel, i.e. iff the contact set `{log 2, log 3}` straddles a zero of
> `I`. At all three windows with contact set `{2,3}` it does, and the relevant zero is the one
> tracking the node of `F*`. The cancellation is therefore **not a coincidence of the primes `2` and
> `3`**: it is the statement that the third zero of `I` — an archimedean object, determined by the
> node of the ground state — falls in the gap `(log 2, log 3)`, a gap of width `0.405` while the
> zero sits `0.33`–`0.34` above `T` in all three windows.

The `log 3` atom is *not* inert on `e₃` here (contrast `π₃₃`, where `R155_032` records the log-3
atom as inert, `−0.0022`): the inertness there is the same phenomenon at a different pair.

---

## §4 Labels of record

| statement | label |
|---|---|
| `tr M₋ = (2T/π)∫₀^{τ₀}(−m) = 4.495774·T`; `M₊ > 0` on `L²(−T,T)` (Paley–Wiener) | **`PROVED`** (constant `DIAGNOSTIC`) |
| BS bound `tr(M₊^{−1}M₋) = 584 / 3548` at `½log3 / log2`; `λ_min(M₊) ≈ 2.9·10⁻³ / 5·10⁻⁴` | **`DIAGNOSTIC`** (Galerkin, `N = 18`, lower bounds growing with `N`; true `tr(M₊^{−1}M₋)` plausibly `+∞`) |
| the Birman–Schwinger / Cwikel / Lieb–Thirring route to `(H1)` | **CLOSED NEGATIVE**: `M₊` gapless, `ε`-shift has the wrong sign, CLR unavailable in `d=1` |
| **Theorem J**: `n₋(Γ_T) ≥ ⌈2Tτ₀/π⌉ − 1`; `n₋(A_∞\|P_T) ≥ ⌈2Tτ₀/π⌉ − 3` | **`PROVED`** (Dirichlet modes + concavity of `φ`; uses `φ(τ₀²) = −C₀`); vacuous (`≥ 0`) at `½log3` and `log 2`, first non-vacuous for `T > 3π/(2τ₀) ≈ 0.74922` |
| `n₋(T) = (2τ₀/π)T + O(log T)`, `2τ₀/π = 4.00405` | **`PROVED`** both sides (upper: `R155_023` Prop 3(ii), min–max, `PROVED` — not Prop NC's `68.51·T`; lower: Theorem J; upgrades `R155_023` Prop 3(ii), previously `HEURISTIC` below) |
| **any `T₂` in `(H1)` obeys `T₂ ≤ 0.9989426`** | **`PROVED`** |
| the concavity no-go (Jensen on `φ` gives ceilings only; a floor ⟺ a prolate spread bound) | **REMARK** (not a theorem — quantifies over an unformalised class; only the ceiling `A_∞(F) ≤ C₀+φ(‖F′‖²)` is `PROVED`) |
| `(H1)`: `n₋(A_∞\|P_T) = 1` on `(T*_{∞,P}, T₂]` | **`HYPOTHESIS`** — unchanged; no `T₂` produced; `n₋ ≤ 5` at `log 2` remains `CONDITIONAL` on Bonami–Karoui |
| **Lemma N**: `⟨Re(R_Tτ_aR_T)F,e⟩ = ∫_{a−T}^{T}F(z−a)e(z)dz` for even `F,e` | **`PROVED`** |
| **Prop G**: sign forced for `a > T + max(z_e,z_F)`; at `log 2`, `a^* = 1.1717` and `log 3` misses by `6.65 %` | **`PROVED`** (the node values `DIAGNOSTIC`) |
| zeros of `I(a)` at `log 2`: `0.2128, 0.6087, 1.0225`; `{log2, log3}` straddle the third; same at `0.62, 0.65`; zeros `≈ T−z_e` and `≈ T+z_F` | **`DIAGNOSTIC`** |
| `F* ≥ 0` (the order's hypothesis) | **`REFUTED`**: `F*` has nodes at `±0.3152` at `log 2` (the two Tate constraints force one sign change) |
| the `76 %` cancellation is structural (a straddled zero of an archimedean overlap function), not numerical | **`DIAGNOSTIC`**, with the `PROVED` equivalence of §3.3 |

---

## §5 Proposal for Paper 47 (to accept or refuse; Paper 47 untouched here)

1. **`subsec:arch` gains Theorem J** (four lines of proof) and the corollary `n₋(T) = (2τ₀/π)T +
 O(log T)` proved on both sides. This is the cheapest new theorem of the round and it removes a
 `HEURISTIC` from the record.
2. **A remark recording `T₂ ≤ 0.9989426`**, so that `(H1)` is stated as a bounded-window hypothesis.
3. **The concavity no-go as an unlabelled remark** after `cor:mono` (not a theorem): the concavity of `φ` is why `cor:mono` is an
 upper bound and why no companion lower bound exists by the same route — it names the missing
 ingredient (an explicit prolate concentration estimate) once and for all.
4. **Lemma N in `subsec:schur`**, with the `π₁₃` table as an example: it makes Prop 4a.4 computable
 and turns the `76 %` into a nodal statement. Prop G as a remark.
5. **Not proposed**: any Birman–Schwinger material; it is a closed negative and belongs here only.
