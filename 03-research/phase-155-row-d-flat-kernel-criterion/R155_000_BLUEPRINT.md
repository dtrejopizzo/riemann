# R155.000 — Blueprint, phase 155: class-dependent value bounds, and the flat-kernel criterion

*Opens a pure-math phase on class-dependent value bounds, the only thing Lemma V′ leaves open. Rules: pure mathematics; no LP, no
B&B, no sweep on the local machine (compute, if any, is the off-machine package
`phase-154/scripts/offmachine/`); every idea corpus-checked independently before it is built;
one report plus one independent audit per round; FATAL rule (no sign for ζ beyond `T ≤ log 2`, no statement about
zeros) in force.*

## 0. What this phase inherits (Paper 46, `04-papers/46-row-d-dual-certificates/main.tex`)

Standing theorems (labels of record R154_012/021/023/030, all `PROVED` unless stated):
Theorem A (form = Lévy energy − prime evaluations; `λ^prim_T = C₀ − Λ_T`); Structure (complete
Bernstein in `τ²`, `K = ½/sinh + ½/cosh` completely monotone, pure jump); D1 (strong duality, atomic
sequences); O (dual never attained); W (Wiener–Hopf E–L); P (`β₀ = 2` restores the polar term = the
complete Weil form `W_T`); E (exponential columns exhaust); tail lemmas F1, T, Hybrid; F3 (second-order
cover); Identity M; Lemma W (moment interior); Lemma V′ (`Θ(log R)` exchange — no rate uniform in `R`);
Prop. env (verification threshold `2πe^{A_T}` cannot be lowered by pointwise envelopes; `A_T ~ 4e^T`);
Theorem C(½log3) `PROVED (machine-verified)` at `8.8577·10⁻⁵`.

**New in Paper 46 §7 (corpus-checked independently: not in the 154 phases; the
adjacent object is our own D1/C):**

> **Theorem Z.** For even `w ≡ 1` on `[−2T,2T]` with `|w| ≤ Ce^{−(½+δ)|u|}` outside, the finite measure
> `dν_w = [½(1−w)K + 2w cosh(u/2)]1_{|u|≥2T}du − Σ_{n∉N_T}(v_n/2)w(log n)(δ_{±log n})` is dual-feasible
> with `β = (2,0)`, and
> `σ_T + ν̂_w + 2ĝ₀ = f_w(τ) = C₀ + ∫₀^∞(1 − w(u)cos τu)K du − Σ_n v_n w(log n)cos(τ log n) + 2∫ w cosh(u/2)cos τu du`
> `= Σ_ρ ŵ(τ − γ_ρ)` (for smooth compactly supported `w`): **the certificate is the Weil explicit
> formula on the modulated test functions `w(u)cos(τu)`, and its value at `τ` is the flat-top smoothing
> of the zero measure.** `sup_w inf f_w = λ^W_T` (exhaustion, `T ≥ ½log2`); the primitive dual is the same
> plus `(β₀−2)ĝ₀ + β₁ĝ₁`.
> **Corollary.** RH ⟺ for every `T` there is a flat-top `w_T` with `Σ_ρ ŵ_T(τ−γ_ρ) ≥ 0` on `R`.
> **Corollary.** Any certificate proved from primes and Gamma alone is an unconditional inequality
> on the zeros. The "certificate at infinity" (`w → 1`) is the primes outside the window; its transform
> is the zero measure.

Paper 46 §8 states the two programmes: **Problem A** (class-dependent value bound — this phase) and
**Problem B** (arithmetic certificate — RH-hard by Theorem Z; recorded, not attacked).

## 1. The problem of this phase

> **Problem A (class-dependent value bound).** For the lattice class `L(T,d,U)` = atoms on
> `u_j = jd ∈ [2T, 2T+U]`, `d = 2T/M`, with the tail rows of Lemma F1 (`τ₁`, `N`), let `c(T,d,U)` be the
> best certificate value. Find an explicit `D(T,d,U) → 0` (as `d → 0`, `U → ∞`) with
> **`c(T,d,U) ≥ λ^prim_T − D(T,d,U)`.**

Equivalent form (Paper 46 §8.4, from `λ^prim − c = ∫(f − c)dμ⋆`, `μ⋆ = |F̂⋆|²dτ/2π` the primal
minimiser): a quantitative one-sided approximation theorem — approximate `−σ_T − β·ĝ + λ^prim` from
below on `[0, τ_env]` by `P`-periodic trigonometric polynomials with vanishing low modes `|j| < M`
(mean zero included), in the norm `L¹(μ⋆)`. Only where `|F̂⋆|²` lives does the slack cost.

Why it is the right problem: (i) Lemma V′ excludes rates in a radius alone but not rates in the class
data; (ii) D1 guarantees `D → 0` but gives no rate; (iii) a rate would make Theorem C a construction
and predict the `M` needed at `0.58` (the value problem of R154_030 §2) without running the LP;
(iv) it is the finite-`T` half of the closing programme; the uniform half (Problem B) is RH itself.

## 2. Levers (each to be corpus-checked before use; this blueprint's assessment in brackets)

L1. **The slack identity + the structure of `μ⋆`.** `μ⋆` is the transform of the Wiener–Hopf
solution (Theorem W). Its decay in `τ` is governed by the boundary behaviour of `F⋆` at `±T`
(Bombieri 2000 Lemma 2: Hölder-½; expected `|F̂⋆|² ≍ τ^{−3}` or `τ^{−2−2α}`). A rate needs
`∫_{τ>R}(f−c)dμ⋆ ≲ (log R)·μ⋆(τ>R)` — small once `|F̂⋆|²` decays; so **the deficit is decided on a
bounded set**, and the approximation problem is compact. [Solid; first thing to prove: an explicit
decay bound for `|F̂⋆|²` from Theorem W.]

L2. **One-sided approximation with a spectral gap.** The class of `ν̂` is `{P`-periodic even trig
polynomials with modes `j ≥ M}` = `{g ∈ C(R/PZ) even : ĝ(j) = 0 for |j| < M}`. One-sided
approximation (from below) of a smooth target by such polynomials: the classical theory
(Beurling–Selberg, Vaaler 1985, Carneiro–Littmann for the *band-limited* side) is for the
complementary constraint (modes ≤ M). The gapped side is `OPEN` in the literature per R154_021.
Candidate route: write `ν̂ = target − (low-mode projection) − slack`; the low-mode projection of the
target on one period is what cannot be matched; its size is the **$M$-dependent floor**
`D ≥ ‖Π_{<M}(target)‖`-type quantity — this gives a *lower* bound on the deficit and hence a
prediction of the needed `M`. [This is the new mathematics to attempt: a two-sided estimate
`D(T,d,U) ≍ ‖Π_{<M}(−σ_T − β·ĝ)‖_{L¹(μ⋆)}`-ish, corrected by the one-sidedness constant (Fejér-type
kernels with gap).]

L3. **Theorem Z as a guide for the ansatz.** The near-optimal certificate is `f_w` for a flat-top
`w`; on the lattice class this suggests `a_j ≈ ½·d·[½(1−w)K + 2w cosh](u_j)` sampled — a
*closed-form profile* candidate (Paper 46 open item (4)). Test on paper against the archived 437 atoms
(sign alternation at 70% says the sampled smooth profile is *not* what the LP found; the LP exploits
aliasing of the lattice). [Diagnostic only unless a theorem comes out.]

L4. **The lower bound side (suggested in R154_029 §5).** A dual certificate *of negativity*
for a class: exhibit `μ` feasible for the relaxation with the lattice constraints only
(`μ̌(u_j) = 0`, moments zero) and `∫σ_T dμ < 0`; that bounds `c(class)` from above (below zero) and
would prove the class saturates. Lemma W supplies feasible `μ` with prescribed moments. [Gives upper
bounds on `c(class)`, not the wanted lower bound; useful to *prove* the negative outcome of the
off-machine sweep if it fails.]

## 3. Round plan (pure mathematics)

Round 1 (memo + audit): L1 — decay of `|F̂⋆|²` from Theorem W (Bombieri's Hölder-½ ⇒
`|F̂⋆(τ)| ≪ τ^{−3/2}`?), and the bounded-set reduction `λ^prim − c ≤ ∫_{[0,R]}(f−c)dμ⋆ + ε(R)` with an
explicit `ε(R)`. Corpus check: Bombieri Lemma 2 / phase 138 minimiser regularity / "Hölder" in phases
136–154.
Round 2: L2 — the gapped one-sided approximation problem on one period; first a *lower* bound on the
deficit in terms of the low-mode content of the target (a theorem-shaped negative that predicts `M`).
Corpus check: "spectral gap majorant", "Beurling–Selberg", R154_019 §1 (the round-7 reformulation).
Round 3: the one-contact case `T = ½log3` in full: is `D(½log3, log3/24, 20) ≈ λ^prim − 8.86e-5 ≈
9.0e-4` reproduced by the theorem? (The one number we have.)
Round 4 (only if rounds 1–3 close): two contacts, and the prediction for `M` at `0.58`, to be compared
with the off-machine sweep E1.

## 4. FATAL rule and labels
No sign for ζ beyond `T ≤ log 2`; no statements about zeros; Theorem Z's corollaries are equivalences.
Labels as in Paper 46 (`PROVED` / `PROVED (machine-verified)` / `DIAGNOSTIC`); every numeric is
DIAGNOSTIC.
