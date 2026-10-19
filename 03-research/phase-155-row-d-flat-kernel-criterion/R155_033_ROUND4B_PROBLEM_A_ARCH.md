# R155.033 — round 4b: Problem A on the archimedean form alone, and (H1)

*Phase 155, round 4b. Executes the the round-4 orders (c) and (b) of `R155_029 §3`.
Inherits Paper 47 §2 (`lem:K`, `thm:S`, `thm:A`, `lem:mbounds`), §3 (`thm:D1`, `thm:O`, `rem:OvsB`,
`thm:W`), §4 (`lem:F1`), §8 (`prob:A`, `prop:TK`, `lem:R1`, `thm:R`, `cor:R3`, `prop:arch`), and
`R155_001` (L1 negatives, Prop. L1.1, §2.3 endpoint profile), `R155_004 §6` (Lemma R1),
`R155_010 §5`, `R155_023` (amended: `τ₀ = 6.28983599`, `λ^{∞,P}_min`, `n₋`), `R155_029 §3`.
Paper 47 and `scripts/r4a` are **not** touched. Scripts: `scripts/r4b/`.*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged:
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 47 Thm C). Every number below is `DIAGNOSTIC`
(double precision, no interval arithmetic).**

---

## §0 Verdict

1. **(c) is a STRUCTURAL NEGATIVE, and it is now quantitative.** Removing the primes does *not* make
 Problem A easier. Two independent facts say so. (α) Paper 47 `thm:O` is stated "for every finite
 weight family, **including `v = 0`**", and its proof locates the obstruction in `K(u) ~ 1/u` as
 `u → 0⁺` — *inside the window, at its edge* — not in the prime atoms (`rem:OvsB` already says this
 in words). So the archimedean dual is never attained either, and the rate question survives intact.
 (β) [amended per R155_049: this clause holds for `(D_∞)` only; in the full programme of
 Paper 47 the sampling cost is `Θ(1/M)`, charged to the polar block's edge jump] **Theorem AL** below proves that for a *fixed smooth* flat-top weight the lattice
 restriction costs only `O_r(M^{−r})`, arbitrarily fast — so [amended per R155_037] **at
 fixed smoothness the lattice is free at rate `M^{−r}`; the deficit is the trade-off between the
 edge approximation and `V_r M^{−r}`** (in the joint optimisation `V_r(w)M^{−r}` *is* the lattice
 cost, §2.3). The wall is the window edge (Theorem O / V′ mechanism), exactly as the order
 anticipated.
2. **(c)(i) The archimedean TK ceilings converge, cleanly and from below, at a measured rate
 `≈ 0.28·M^{−1.17}`** (`DIAGNOSTIC`, `r4b_01`), and — the sharpest reading — **the gap
 `λ^{∞,P}_min − Ceil_∞(M,T)` is essentially independent of `T`**: at `M ≥ 24` the two windows
 `½log3` and `log2` agree to `<1 %` (`7.09e−3` vs `7.13e−3`, `2.027e−3` vs `2.045e−3`), although
 `λ^{∞,P}_min` itself differs by `0.24` and has opposite signs. The class deficit is a function of
 the resolution `M` alone. This is a **lower** bound on any admissible `D_∞`: `D_∞(M,T) ≳ 0.27 M^{−1.17}`.
3. **(c)(ii) No proved lower bound better than the general case.** What is proved is Theorem AL
 (explicit, `O(M^{−r})`, conditional on nothing) plus Theorem R with the comb removed (a sharper
 *upper* bound, `A_T = 0`); the continuous half remains `OPEN` with the same two options as in
 `R155_001`: `o(1)` with no rate unconditionally (`thm:D1`/`thm:R`), or `O((log M)^{−1})`-type
 statements `CONDITIONAL` on the logarithmic endpoint profile of `R155_001 §2.3`, itself
 `CONDITIONAL` on a maximum principle of the same family as the conclusion. **Nothing is upgraded.**
4. **(b) (H1) is not proved and the natural route cannot prove it.** `PROVED` and explicit:
 for every `τ₁ > τ₀`, `n₋(A_∞|P_T) ≤ #{n : λ_n(S_{T,τ₁}) > θ(τ₁)}`, `θ(τ₁) = m(τ₁)/(m(τ₁)−C₀)`,
 `S` the Slepian operator of parameter `c = Tτ₁`; with the trace/Markov input this is the fully
 explicit `n₋ ≤ ⌊2Tτ₁/(πθ(τ₁))⌋`. Evaluated: [amended per R155_037] the explicit bound
 gives `37, 47, 54` at `½log3, log2, 0.80`; with numerically computed prolate eigenvalues it gives
 `4, 5, 5` against the computed `n₋ = 0, 1, 1`. The overcount is **structural** (§3.3): `m` grows
 only logarithmically,
 so the min–max criterion constrains the bandwidth of a negative direction only logarithmically.
 `(H1)` stays `HYPOTHESIS`. No `T₂` is produced.
5. Nothing in this round touches row D's label or the endpoint of record.

---

## §1 Corpus check (grep-verified, `03-research` + `04-papers` + `05-meta-and-planning`)

| query | hits | what is already there | what is new here |
|---|---|---|---|
| `Problem A` | 98 files | `prob:A` (Paper 47 §8.4); `R155_010 §5` ("Problem A proper: a class-dependent **lower** bound. Everything in rounds 1–2 and the reverse track is upper-bound-side"); `R155_029 §2.4` (same); `R155_000 §2` levers L1–L4. Older hits (`phase-124`, `phase-16-surf-witness-variety`, `phase-136`) are a different "Problem A" | the archimedean specialisation `(D_∞)`, and the first **lower**-bound theorem of the phase (Theorem AL) |
| `one-sided approximation` | 10 files | `R154_018 §`/`R154_019` (the reformulation, and "its rate is a zero-counting wall"); `R154_019:28` records the corpus was empty before that round; `R154_020` audit | nothing new on the gapped one-sided side; §2.4 records **why** the Jackson route does not start |
| `Jackson` | 4 files | `R154_018:28` (the order), `R154_019:118` ("for the band-limited (classical) side, rates are sharp and classical"), `E67_1c` (unrelated) | §2.4: the Jackson rate is available for the *approximation*, useless because the **constraint is a spectral gap, not a degree bound**, and the cost reappears as `V_r ↑ ∞` |
| `prolate` | 389 files | Connes–Consani prolate compression (Paper 47 `subsec:arch` remark); `phase-7-weil-carleson-sine-kernel/connes/prolate_bridge.py`; `phase-93`, `phase-137` | the prolate operator used as a **negative-index counter** for `A_∞|P_T` (§3), via `θ(τ₁)` |
| `Slepian` | 57 files | Landau–Widom quoted in `R155_023 §4` (Prop. 3(ii), lower half `HEURISTIC`) | §3.2 replaces the `HEURISTIC` splitting by a `PROVED` min–max count, and then **measures how lossy it is** |
| `Bonami` | 1 file | `phase-61-open-problems/respuestas3.md` only — the Bonami–Karoui explicit prolate bounds are **not** in `00-references` | not used; §3.4 records that importing them would move `47 → ≈8`, still not `1` |
| `Poisson summation` | 66 files | `R154_025:284` and Paper 47 `lem:F1`: the **dual** direction (a lattice `ν` makes `ν̂` periodic); `R155_004 §6`/`lem:R1`: the **primal** direction (periodising `μ` gives a test kernel) | the **third** direction — *sampling a smooth continuous dual density onto the lattice*, with the aliasing error controlled by smoothness (Theorem AL). Grep for `Euler--Maclaurin`/`sampling the certificate` in phases 153–155 and Paper 47: no hits |
| `aliasing` | 15 files | `phase-106`, `phase-114` (unrelated Green/Legendre contexts) | new in this line of work |

Nothing below duplicates a corpus statement; Theorem AL and Proposition NC are new, Theorem R∞ is a
specialisation of `thm:R`.

---

## §2 (c) Problem A for the archimedean form

### 2.1 The programme `(D_∞)`

With the comb deleted the symbol is `σ_∞ = m`, `A_T = 0`, and Paper 47 §3 reads verbatim:

> **(P_∞)** `λ^{∞,P}(T) = inf{ ∫ m dμ : μ` even probability on `ℝ`, `μ̌(u) = 0` for `|u| ≥ 2T }`.
> **(D_∞)** `sup{ c : m + ν̂ + β·ĝ ≥ c` on `ℝ`, `ν` finite even signed, `supp ν ⊆ {|u| ≥ 2T} }`.
> Lattice class `L_∞(T,d,U)`: `ν` atomic on `{±jd : j ≥ M}`, `d = 2T/M`, within range `U`.

`thm:D1` (strong duality), `thm:O` (non-attainment), `lem:R1`, `thm:R`, `prop:TK` all hold with
`v = 0` — each proof either never mentions the comb or uses only `A_T ≥ 0`. In particular:

> **Theorem R∞ (`PROVED`; `thm:R` at `𝒩 = ∅`).** For every `μ` feasible for `(P_∞)`,
> `Ceil_∞(M,T;β) ≤ ∫ m dμ + Δ_∞(M,β)·μ({|τ| > πM/2T})`, with
> `Δ_∞(M,β) = [m(πM/2T) − C₀] + 2|β₀|ĝ₀(0) + 2|β₁|ĝ₁(0)`.
> Hence `limsup_M Ceil_∞(M,T;β) ≤ λ^{∞,P}(T)`, uniformly on bounded `β`-boxes.

*Proof.* Read the proof of `thm:R` with `A_T = 0`: the term `2A_T` in `Δ` is exactly the comb's
contribution to `sup_W S_β − inf_ℝ S_β`. ∎

This is strictly sharper than the general `Δ`: at `½log3`, `A_T = 0.9803`, so `Δ_∞ = Δ − 1.96`.
It is still an **upper** bound on the ceiling, i.e. upper-bound-side.

### 2.2 The certificate-as-weight dictionary, with no primes

`m(τ) = C₀ + ∫₀^∞ (1 − cos τu)K(u)du` (Paper 47 `thm:S`). For `w : [0,∞) → ℝ` with `w ≡ 1` on
`[0,2T]`, put `G(u) := (1 − w(u))K(u)·1_{u ≥ 2T}`, extended evenly, and `ν_w := G(|u|)du`. Then
`supp ν_w ⊆ {|u| ≥ 2T}` and

 **`m(τ) + ν̂_w(τ) = C₀ + ∫₀^∞ (1 − w(u)cos τu)K(u)du =: f_w(τ)`**, `β = 0`. (2.1)

This is Paper 47 `thm:Z` with the prime atoms deleted; `β = 0` because on `P_T` the two polar
functionals are free. So `(D_∞)` **is** the problem: choose a weight `w`, flat-top `≡ 1` on the
window, maximising `inf_τ f_w(τ)`; and `(P_∞)` is: choose an autocorrelation `c_F` supported in the
window with `c_F(0) = 1`, minimising `C₀ + Lev(c_F)`. Two elementary but sharp remarks:

* **The `τ = 0` cap.** `f_w(0) = C₀ + ∫_{2T}^∞ (1 − w)K du`, so any certificate of value
 `c ≥ λ^{∞,P}` needs `∫_{2T}^∞ (1−w)K du ≥ Lev(c_{F⋆}) = λ^{∞,P} − C₀`. At `½log3` this is
 `5.4547` against `∫_{2T}^∞K = 2.3642`, at `log2` `5.2179` against `2.0259`: **`w` must go
 substantially negative outside the window** (it cannot be a `[0,1]`-valued flat top), by a factor
 `≥ 2.3` and `≥ 2.5` respectively [amended per R155_037: the printed `≥ 2.6` rounded a
 lower bound up; the exact factors are `2.307`, `2.576`]. `PROVED` given the `DIAGNOSTIC` values of
 `λ^{∞,P}`.
* **`ν = 0, β = 0` is feasible with value `C₀`** (`m ≥ m(0) = C₀`, `lem:mbounds`(i)). So the trivial
 archimedean certificate has deficit exactly `Lev(c_{F⋆})`, i.e. `5.45` / `5.22` — the whole problem.
 `PROVED`.

### 2.3 Theorem AL: the lattice costs `O(M^{−r})`, the edge costs everything

> **[amended per TEX_R2 finding 1 / R155_049]** Theorem AL and Corollary AL′ below are
> **correct as stated, for the archimedean programme `(D_∞)` of §2.1 only**, where `G = (1−w)K`
> vanishes at `u = 2T⁺` (`w(2T) = 1`) so that `G_e ∈ C^{r−1}`. They were transplanted into Paper 47
> (`thm:AL`, `cor:ALdef`) for the **full** programme, and there they are **FALSE**: by `eq:nuw` the
> a.c. density of `ν_w` is `½(1−w)K + 2w cosh(u/2)`, which at `u = 2T⁺` equals `2cosh T ≠ 0` — a jump,
> so no `O(M^{−r})` Poisson bound holds. `R155_049` proves the correct replacement: the sampling of a
> flat-top certificate costs **`Θ(1/M)`**, exactly `(4/π)cosh T·d + O(d²)` for the endpoint-corrected
> sampling, the loss being the alias of the polar block's edge jump. Consequently the reading below
> ("the lattice contributes nothing", "Problem A is *entirely* the continuous problem") is
> **WITHDRAWN for the full programme**; it survives only for `(D_∞)`. The `M^{−1}` rate agrees with
> the measured `Ceil_∞` deficit of §2.5.

> **Theorem AL (archimedean lattice certificate from a smooth weight). `PROVED`.**
> [amended per R155_037] Let `T > 0`, `M ∈ ℕ`, `d = 2T/M`, `P = 2π/d = πM/T`. Let `w` be a
> weight as in §2.2, `w ≡ 1` on `[0,2T]` and on `[U,∞)`, with `C^{r−1}` contact with the constant `1`
> at both `u = 2T⁺` and `u = U⁻` (i.e. `w` has no jump at either end of the window), such that the
> even extension `G_e` of `G = (1−w)K·1_{[2T,U]}` lies in `C^{r−1}(ℝ)` with `G_e^{(r)} ∈ L¹`, `r ≥ 2`.
> (Feasibility of `(D_∞)` needs only `supp ν ⊆ {|u| ≥ 2T}`, `main.tex:425–433`; there are no moment
> equalities on `ν`, so the boundary atom at `u = ±2T` is harmless, `main.tex:449`.)
> Put `V₀ = ‖G_e‖_{L¹}`, `V_r = ‖G_e^{(r)}‖_{L¹}`, `c_w = inf_ℝ f_w`. Define the **lattice sampling**
> `ν_lat := Σ_{|j| ≥ M} d·G_e(jd)·δ_{jd}` — a finite atomic measure on `{±jd : j ≥ M}` (the atoms
> beyond `U` vanish), i.e. a member of the lattice class `L_∞(T, 2T/M, U)`. Then `(ν_lat, β = 0)` is
> dual feasible for `(D_∞)` with value
> ```
> c_lat(M) ≥ min{ c_w, m(πM/2T) − V₀ } − ε_r(M),
> ε_r(M) := 2(1 − 2^{−r}) ζ(r) V_r (πM/2T)^{−r}.
> ```
> Since `m(πM/2T) → ∞`, for `M ≥ M₀(w) := (2T/π)·m^{−1}(c_w + V₀)` the first term is the minimum and
> ```
> λ^{∞,P}(T) − c_lat(M) ≤ [λ^{∞,P}(T) − c_w] + ε_r(M), ε_r(M) = O_r(V_r M^{−r}).
> ```

*Proof.* `G_e` vanishes on `(−2T, 2T)`, so the sum defining `ν_lat` may be extended to all `j ∈ ℤ`.
Poisson summation for `G_e ∈ C^{r−1}`, `G_e^{(r)} ∈ L¹` (so `Ĝ_e(ξ) = O(|ξ|^{−r})` and both sides
converge absolutely) gives, with `ν̂_w = Ĝ_e`,
`ν̂_lat(τ) = d Σ_{j∈ℤ} G_e(jd) cos(jdτ) = Σ_{k∈ℤ} ν̂_w(τ + kP)`.
Hence `ν̂_lat` is `P`-periodic and, for `|τ| ≤ P/2`,
`|ν̂_lat(τ) − ν̂_w(τ)| ≤ Σ_{k≠0} |ν̂_w(τ+kP)| ≤ V_r Σ_{k≠0}|τ+kP|^{−r} ≤ 2V_r Σ_{k≥1}((k−½)P)^{−r}
 = 2V_r(P/2)^{−r}Σ_{k≥1}(2k−1)^{−r} = 2V_r(P/2)^{−r}(1−2^{−r})ζ(r) = ε_r(M)`,
using `|ν̂_w(ξ)| = |Ĝ_e(ξ)| ≤ V_r|ξ|^{−r}` (integrate by parts `r` times). Now bound
`f_lat := m + ν̂_lat` on the two ranges. For `|τ| ≤ P/2`: `f_lat ≥ f_w − ε_r ≥ c_w − ε_r`. For
`|τ| > P/2`: write `τ = τ' + kP` with `|τ'| ≤ P/2`; then `ν̂_lat(τ) = ν̂_lat(τ') ≥ ν̂_w(τ') − ε_r ≥
−V₀ − ε_r` (`|Ĝ_e| ≤ ‖G_e‖_{L¹}`), while `m(τ) ≥ m(P/2)` by `lem:mbounds`(i). Combine. The last
display is (2.1) plus the definition of the deficit. ∎

**Reading (this is the structural negative).** For a *fixed* weight `w` of fixed smoothness the
lattice is free at any polynomial rate: `ε_r(M) = O(M^{−r})`, and `r` may be taken as large as `w`
allows. Therefore

> **Corollary AL′ (`PROVED`).** `D_∞(T, 2T/M, U) ≤ inf_w { [λ^{∞,P}(T) − c_w] + ε_r(M) }`, the
> infimum over admissible `C^{r−1}`-smooth weights supported in `[2T,U]`. **Problem A for the
> archimedean form is *entirely* the continuous problem `sup_w c_w` — the lattice contributes nothing
> once `w` is smooth.**

And the continuous problem is closed by `thm:O` with `v = 0`: `sup_w c_w = λ^{∞,P}` is never attained,
and the proof says why — the required density is `−2·(the restriction of m̌ to 0<|u|<2T) = K(|u|)/…`,
unbounded as `u → 0`, so a maximising sequence must push mass towards the edge `u = 2T` and
`V_r ↑ ∞`. The rate in Corollary AL′ is therefore a **trade-off between the edge-approximation error
and `V_r M^{−r}`**, and nothing in the archimedean case bounds that trade-off that does not also
bound it with the primes present. `OPEN`, and **the primes are irrelevant to it**.

*Consistency check with §2.5.* [amended per R155_037] Corollary AL′ and the measured
`Ceil_∞` gap are not in conflict: `prop:TK` says `c_lat(M) ≤ Ceil_∞(M,T)`, so AL′ forces
`c_w ≤ Ceil_∞(M,T) + ε_r(M)` for **every** `M` and every fixed smooth `w`. Letting `M → ∞` recovers
only `c_w ≤ λ^{∞,P}`. What the pair does say quantitatively is: any `w` with `c_w ≥ λ^{∞,P} − δ` must
have `V_r ≥ (πM/2T)^r (Def(M) − δ)/(2(1−2^{−r})ζ(r))` for every `M` with `Def(M) > δ`, where
`Def(M) ≈ 0.28·M^{−1.17}` is the measured ceiling deficit — the bracket is `Def − δ`, not `δ − Def`,
and the prefactor is `(π/2T)^r M^r`, not `(2T/π)^r M^r`. Optimising at the largest `M` with
`Def(M) > δ` gives `V_r ≳ (π/2T)^r δ^{−r/1.17}·const → ∞` as `δ ↓ 0`: this "`V_r ↑ ∞`" reading is
**`DIAGNOSTIC`-conditional**, not a consequence of `thm:O` alone (which forbids attainment only) —
it depends on the numerical `Ceil_∞` ceilings of §2.5.

### 2.4 Why the Jackson route does not start

The classical one-sided (Jackson/Bernstein) rate `O(‖m''‖_∞ M^{−2})` is for approximation by trig
polynomials of **degree ≤ M**; our constraint is the complementary one, modes `|j| ≥ M` (equivalently:
a spectral gap `(−2T,2T)` in `u`). `R154_019` recorded that the gapped side is `OPEN` in the
literature. §2.3 makes the reason concrete and quantitative: the gap constraint is *not* a smoothness
constraint on `ν̂` at all — `ν̂_lat` is as smooth as one likes — it is [amended per
R155_037] a **low-mode vanishing, a spectral-gap constraint, not a smoothness constraint**:
`prop:TK` uses orthogonality to every mode `|j| < M` (every `|q|²`, `deg ≤ M−1`, Fejér–Riesz,
`main.tex:1793–1800`), not merely zero mean over a period (mode `0` alone). The smoothness of `m`
(`|m^{(j)}| ≤ 2^{−j}j!ζ(j+1,¼)`, `lem:mbounds`) is therefore *not the relevant resource*: the target
`−m + λ` is entire and perfectly smooth, and the obstruction is that the certificate must be
`P`-periodic with all low modes vanishing while the target is not periodic and grows. This is a clean
explanation of why every smoothness-based attack in rounds 1–4 has failed. `prop:TK` proves a ceiling,
not the non-existence of a route: label downgraded `PROVED → READING`/`OBSERVED`.

### 2.5 `(c)(i)` — the archimedean ceilings, computed (`DIAGNOSTIC`)

`Ceil_∞(M,T) = sup_{β∈ℝ²} inf_{τ₀} λ_min(C_M(τ₀,β))` with `S_β = m + β₀ĝ₀ + β₁ĝ₁` (`prop:TK` with the
comb removed); `r4b_01_ceil_inf.py`, Simpson on one period with `n = 2¹⁵`, `τ₀`-grid of 33 points on
`[−P,0]`, grid + Nelder–Mead on the concave `β`-objective. Reference values `λ^{∞,P}_min` from the
`R155_023` Galerkin table (`N = 18`, absolute accuracy `≈ 2.5·10⁻⁵`, themselves **upper** bounds).

| `M` | `Ceil_∞(M,½log3)` | deficit | local slope | `Ceil_∞(M,log2)` | deficit | local slope |
|---|---|---|---|---|---|---|
| 8 | `+5.98977e−02` | `2.2652e−02` | — | `−1.77911e−01` | `2.3631e−02` | — |
| 12 | `+6.75914e−02` | `1.4959e−02` | `−1.023` | `−1.70233e−01` | `1.5953e−02` | `−0.969` |
| 16 | `+7.14957e−02` | `1.1054e−02` | `−1.051` | `−1.66310e−01` | `1.2030e−02` | `−0.981` |
| 24 | `+7.54585e−02` | `7.0915e−03` | `−1.095` | `−1.61410e−01` | `7.1297e−03` | `−1.290` |
| 32 | `+7.76563e−02` | `4.8937e−03` | `−1.289` | `−1.59205e−01` | `4.9248e−03` | `−1.286` |
| 48 | `+7.96218e−02` | `2.9282e−03` | `−1.267` | `−1.57217e−01` | `2.9368e−03` | `−1.275` |
| 64 | `+8.05230e−02` | `2.0270e−03` | `−1.279` | `−1.56325e−01` | `2.0453e−03` | `−1.257` |

Global fits: `0.271·M^{−1.166}` at `½log3`, `0.308·M^{−1.197}` at `log2`.

Four readings, all `DIAGNOSTIC`.
1. **The ceilings converge from below**, monotonically in `M`, to the Galerkin `λ^{∞,P}_min`
 (`+0.08255`, `−0.15428`) — the first direct numerical confirmation of `thm:R`/`cor:R3` in the
 archimedean case, and it also cross-validates two entirely independent computations (a Legendre
 Galerkin of the *primal* form and a Toeplitz *dual* ceiling) to `2.5 %` at `M = 64`.
2. **The deficit is `T`-independent at `M ≥ 24`**, to `<1 %`, although `λ^{∞,P}_min` differs by `0.24`
 and changes sign between the two windows. So `D_∞(M,T) ≈ D_∞(M)`: the class deficit depends on the
 **resolution `M` (steps per window), not on the window**. Note `P = πM/T` differs by a factor
 `1.26` between the two rows, so the deficit is not a function of `P` either.
3. **A lower bound on any admissible `D_∞`:** since `c ≤ Ceil_∞(M,T)` for every certificate in the
 class (`prop:TK`, `PROVED`), `D_∞(M,T) ≥ λ^{∞,P} − Ceil_∞(M,T) ≈ 0.28·M^{−1.17}`. [amended
 per R155_037] This is **not earned as a refutation**: `λ^{∞,P}` is a Galerkin (`N=18`)
 *upper* bound and `Ceil_∞` a numerical `sup_β` (grid + Nelder–Mead), and both error directions
 inflate the measured deficit; at `½log3`, `M = 8/12/16` the optimiser leaves the seed box
 (`β = (7.92,−8.00), (8.10,−7.51), (9.16,−7.90)` against the stable `(2.29,−6.29)` for `M ≥ 24`);
 and the local slope still drifts (`−1.02 → −1.29`) over `M ≤ 64`. **`D = O(M^{−2})` "REFUTED" is
 downgraded to `DIAGNOSTIC`**: no numerical support for an `M^{−2}` law; the measured rate over
 `8 ≤ M ≤ 64` is `≈ 0.28 M^{−1.17}`, essentially `T`-independent for `M ≥ 24` (`<1 %`), which is the
 strongest datum of the round; `D ≍ M^{−1}` remains the honest target but excluding `M^{−2}` is an
 extrapolation, not a refutation. The runtime of `r4b_01_ceil_inf.py` is `≈ 4` min wall, not the
 `≈ 60` s of `scripts/r4b/README.md`.
4. The optimal `β` stabilises at `≈ (2.29, −6.29)` at `½log3` and `≈ (1.86, −3.28)` at `log2`. The
 first component sits near the polar multiplier `β₀ = 2` of `prop:P` at both windows (as in
 Theorem C), the second does not: with the comb deleted `β₁` is large and negative. `OBSERVED`.

### 2.6 `(c)(ii)` — what is proved about a lower bound, exactly

| statement | status |
|---|---|
| `D_∞(M) ≤ [λ^{∞,P} − c_w] + 2(1−2^{−r})ζ(r)V_r(πM/2T)^{−r}` for every admissible smooth `w` (Theorem AL, Cor. AL′) | **`PROVED`**, explicit, unconditional |
| `D_∞(M) → 0` with **no rate** | [amended per R155_037] **`PROVED` only on windows with `λ^{∞,P} > 0`** (`thm:D1` + `thm:R∞` + `cor:R3` at `v = 0`; `cor:R3` needs `λ^P > 0`, and `λ^{∞,P}(log 2) = −0.15428 < 0`, so the row fails at `log 2`) |
| an explicit `D_∞(M) = O((log M)^{−1})` | **`CONDITIONAL`** on the endpoint profile `μ⋆(|τ|>R) ≍ R^{−1}(log R)^{−1}` of `R155_001 §2.3`, itself `CONDITIONAL` on a maximum principle of the same family as the conclusion (`R155_001 §2.3(iv)`) — **not usable in a closing argument**. Nothing in the archimedean case removes that conditionality: `R155_001 §2.3`'s obstruction (a zero-order logarithmic symbol on a finite interval) is the *archimedean* operator, the comb playing no role in it |
| `D_∞(M) = O(M^{−2})` or better | [amended per R155_037] **`DIAGNOSTIC`** (downgraded from `REFUTED`): §2.5 reading 3's error directions both inflate the deficit and `β` is unconverged at `M ≤ 16` |
| "the primes are what makes Problem A hard" | [amended per R155_037] restated: **the primes are not necessary for the obstruction** — non-attainment and the edge singularity survive at `v = 0` (`PROVED`; `thm:O` at `v = 0`, Cor. AL′ shows the lattice is free, the residue is the edge `K(u) ~ 1/u`); `thm:O` is about attainment, not about the rate `D`, so "hard/REFUTED" overstates it |

The order's proposed route (periodise `μ⋆` by `lem:R1` and bound the loss by Lemma 4.1 and the decay
of `|F̂⋆|²`) is exactly the proof of `thm:R`, and it produces an **upper** bound on `Ceil`, not a lower
bound on `c` — it was already executed in `R155_004 §6`. The lower-bound content had to come from the
opposite direction (sampling, not periodising), which is Theorem AL.

---

## §3 (b) The negative index of `A_∞|P_T`

### 3.1 Setting

On `P_T` the pole term vanishes and `A_∞(F) = (1/2π)∫ m|F̂|²` (`prop:arch`). `m` is even, increasing on
`[0,∞)`, `m(0) = C₀ = −5.3721834`, and `m < 0` exactly on `|τ| < τ₀ = 6.28983599` (`R155_023`,
`lem:mbounds`(i)). Write `Q_T` for multiplication by `1_{(−T,T)}`, `B_s` for the band projection onto
`|τ| < s`, and `S_{T,s} = Q_T B_s Q_T` for the Slepian time–band-limiting operator on `L²(−T,T)`,
whose eigenvalues `λ_0(c) > λ_1(c) > …` in `(0,1)` depend only on `c = Ts`.

### 3.2 The count

> **Proposition NC (`PROVED`).** For every `τ₁ > τ₀` put `θ(τ₁) := m(τ₁)/(m(τ₁) − C₀) ∈ (0,1)`. Then
> ```
> n₋(A_∞|P_T) ≤ n₋(A_∞ on L²(−T,T) with the pole deleted) ≤ #{ n : λ_n(Tτ₁) > θ(τ₁) },
> ```
> and consequently, by `Σ_n λ_n(Tτ₁) = tr S_{T,τ₁} = 2Tτ₁/π` and Markov's inequality,
> ```
> n₋(A_∞|P_T) ≤ inf_{τ₁ > τ₀} ⌊ 2Tτ₁ / (π θ(τ₁)) ⌋,
> ```
> an explicit bound in `T` alone.

*Proof.* Let `V ⊆ P_T` with `dim V = n` and `A_∞ < 0` on `V∖{0}`. For a unit `F ∈ V` put
`b := ‖B_{τ₁}F‖² ∈ [0,1]` (Plancherel, `‖F‖ = 1`). Since `m ≥ C₀` everywhere and `m ≥ m(τ₁) > 0` on
`|τ| ≥ τ₁` (`lem:mbounds`(i)),
`0 > A_∞(F) ≥ C₀·b + m(τ₁)·(1−b) = m(τ₁) − (m(τ₁) − C₀)b`, i.e. `b > θ(τ₁)`.
So `⟨S_{T,τ₁}F, F⟩ = ‖B_{τ₁}Q_TF‖² > θ(τ₁)‖F‖²` for every `F ∈ V` (`Q_TF = F`), and by the min–max
principle `λ_{n−1}(S_{T,τ₁}) > θ(τ₁)`, i.e. `S` has at least `n` eigenvalues above `θ(τ₁)`. The first
inequality is `P_T ⊂ L²(I_T)` with the pole term vanishing on `P_T`. The trace of `S_{T,τ₁}` is
`∫_{−T}^{T} (τ₁/π) dt = 2Tτ₁/π`; all eigenvalues are in `[0,1]`, so `#{λ_n > θ} < tr S/θ`. ∎

### 3.3 Evaluation, and why it fails (`r4b_02_negcount.py`)

| `T` | explicit trace bound `inf_{τ₁}⌊2Tτ₁/(πθ)⌋` (at `τ₁`) | prolate count `#{λ_n > θ(τ₁)}` (`DIAGNOSTIC`, at `τ₁`) | computed `n₋` (`R155_023`) |
|---|---|---|---|
| `½log3` | `37` at `τ₁ = 14.887`, `θ = 0.1383` | **`4`** at `τ₁ = 6.682`, `θ = 0.0111` | `0` |
| `log2` | `47` at `τ₁ = 14.887`, `θ = 0.1383` | **`5`** at `τ₁ = 6.682`, `θ = 0.0111` | `1` |
| `0.80` | `54` at `τ₁ = 14.887`, `θ = 0.1383` | **`5`** at `τ₁ = 6.682`, `θ = 0.0111` | `1` |

(Top prolate eigenvalues at `T = log2`, `τ₁ = 6.682`, `c = 4.632`: `0.9987, 0.9645, 0.7114, 0.2415,
0.0303, 0.0019` — the Landau–Widom plateau `2c/π = 2.95` plus a plunge of width `≈ 2`.)

**Why the route cannot give `1`.** The optimal `τ₁` is pushed down to `τ₀`, where `θ(τ₁) ↓ 0` and the
criterion degenerates to `‖B_{τ₀}F‖² > 0` — vacuous; the count then measures only the numerical rank
of `S_{T,τ₀}`, i.e. `2Tτ₀/π + (plunge)`. Pushing `τ₁` up to buy a larger `θ` costs more bandwidth than
it buys, **because `m` grows only logarithmically**: `θ(τ₁) ≍ log τ₁/(log τ₁ + |C₀|)` while the count
grows like `Tτ₁`. This is the same logarithmic-growth wall as Prop. L1.1 of `R155_001` (whose
Chebyshev tail is `(λ+B)/(m(R)−C₀)`, useless for the same reason). [amended per R155_037]
No choice of `τ₁` in Proposition NC escapes it: the trace bound is minimised at a finite `τ₁`, and the
exact minimum is `(2T/π)·inf_{τ₁>τ₀}(m(τ₁)−C₀)/m(τ₁) = 68.5135·T` at `τ₁ = 14.8815` — `PROVED` as
`(2T/π)·inf_{τ₁>τ₀}(m−C₀)/m`, the constant `DIAGNOSTIC`. (The earlier display carrying the bound
variable `τ₁` into a `τ₁`-free infimum, and the `O(·)`-with-`≥` non-statement, are withdrawn; `≳30T`
was wrong.)

### 3.4 What would and would not help

* Importing the **Bonami–Karoui** explicit non-asymptotic prolate eigenvalue bounds (not in
 `00-references`; one corpus hit, `phase-61/respuestas3.md`) would turn the `DIAGNOSTIC` counts
 `4/5/5` into `PROVED` ones of roughly the same size — i.e. `n₋ ≤ 5` at `log2`, not `n₋ = 1`.
 That is a real but modest gain and is the **only** upgrade this round identifies.
* The two primitivity constraints subtract at most `2`, giving `n₋(A_∞|P_T) ≥ n₋(A_∞) − 2`; they do
 not help the upper bound (the bound already ignores them).
* A bound reaching `1` must use the *shape* of `m` inside the band, not the two-level majorisation
 `m ≥ C₀ / m ≥ m(τ₁)`: `m(τ) − C₀` rises steeply (`m(1) − C₀ = 0.61`, `m(τ₀) − C₀ = 5.37`), so almost
 all of the available negativity sits in `|τ| ≲ 2`, a time–bandwidth product `2Tτ/π ≈ 0.9` at `log2`
 — which is why the true `n₋` is `1`. Formalising this needs a Birman–Schwinger / Cwikel-type count
 for the *variable* symbol `m` on a finite interval, not a two-level split. Recorded as the
 round 5's treatment of `(H1)`; **no `T₂` is produced here**.
* **`(H1)` label unchanged: `HYPOTHESIS` (computed, not proved).**

---

## §4 Labels of record

| statement | label |
|---|---|
| Theorem R∞ (`thm:R` at `𝒩 = ∅`; `Δ_∞ = Δ − 2A_T`) | `PROVED` (specialisation, proof re-read) |
| Dictionary (2.1): `(D_∞)` = flat-top weights, `m + ν̂_w = f_w`, `β = 0` | [amended per R155_037] `PROVED` as algebra, but **not** `thm:Z`: (2.1) drops the primes **and** the polar term `2ĝ₀`, whereas Paper 47's flat-top dual point is `(ν_w, β=(2,0))`; carries **no** explicit-formula/zero-sum reading via `thm:Z` |
| `τ = 0` cap: a certificate of value `≥ λ^{∞,P}` needs `∫_{2T}^∞(1−w)K ≥ λ^{∞,P} − C₀`, i.e. `w` must go negative outside (factor `≥ 2.3`, `≥ 2.5`) | `PROVED`; the two factors `DIAGNOSTIC` [amended per R155_037: `≥2.6` corrected to `≥2.5`, exact factors `2.307`, `2.576`] |
| `ν = 0, β = 0` feasible with value `C₀` | `PROVED` |
| **Theorem AL** (lattice sampling of a smooth weight; `ε_r(M) = 2(1−2^{−r})ζ(r)V_r(πM/2T)^{−r}`) | **`PROVED`** (Poisson summation + `lem:mbounds`(i)); **new**; [amended per R155_037] hypothesis unpacked: `w ≡ 1` on `[0,2T]` and on `[U,∞)` with `C^{r−1}` contact at both ends |
| **Corollary AL′** (Problem A for `A_∞` is entirely the continuous problem; the lattice is free) | **`PROVED`** as an inequality; [amended per R155_037] "the deficit is entirely continuous" holds only **at fixed `w`** — restated §2.3 |
| `V_r` blow-up bound for `δ`-optimal weights (§2.3 consistency check) | [amended per R155_037] `PROVED` with bracket `Def(M) − δ` and prefactor `(π/2T)^r M^r` (corrected sign/prefactor); "`V_r ↑ ∞`" is `DIAGNOSTIC`-conditional, not a consequence of `thm:O` alone |
| §2.4 (the Jackson route does not start; the constraint is low-mode vanishing on `|j|<M`, not smoothness) | [amended per R155_037] downgraded `PROVED → READING`/`OBSERVED` (`prop:TK` proves a ceiling, not non-existence of a route) |
| `Ceil_∞(M,T)` table, fits `0.271M^{−1.166}` / `0.308M^{−1.197}`, `T`-independence of the deficit | `DIAGNOSTIC` |
| `D_∞(M,T) ≥ λ^{∞,P} − Ceil_∞(M,T) ≈ 0.28M^{−1.17}`; `D = O(M^{−2})` | inequality `PROVED` given `prop:TK`, values `DIAGNOSTIC`; [amended per R155_037] "`D=O(M^{−2})` REFUTED" downgraded to **`DIAGNOSTIC`** (Galerkin upper bound + numerical `sup_β` both inflate the deficit; `β` escaped the seed box at `M=8/12/16`; slope drifting) |
| an explicit `D_∞ = O((log M)^{−1})` | `CONDITIONAL` (on `R155_001 §2.3`, itself conditional on a positivity hypothesis) — **not usable** |
| **"Problem A is hard because of the primes"** | [amended per R155_037] restated: **the primes are not necessary for the obstruction** — non-attainment and the edge singularity survive at `v = 0` — `PROVED` (`thm:O` at `v = 0`; Cor. AL′); `REFUTED` dropped (it conflated attainment with rate) |
| **Proposition NC** (`n₋ ≤ #{λ_n(Tτ₁) > θ(τ₁)}`; `n₋ ≤ ⌊inf_{τ₁}2Tτ₁/(πθ(τ₁))⌋`) | **`PROVED`**, explicit; replaces the `HEURISTIC` upper-bound sketch of `R155_023` Prop. 3(ii)'s upper half only (not its lower/asymptotic `HEURISTIC` half); merit is explicitness in `T` |
| explicit values `37/47/54`; prolate counts `4/5/5` | [amended per R155_037: corrects `38/48/55` and `4/5/6`] `PROVED` (trace bound) / `DIAGNOSTIC` (prolate); trace-bound infimum `68.5135·T` at `τ₁=14.8815` (corrects `≳30T`) |
| §3.3 obstruction (logarithmic growth of `m` caps `θ`) | `PROVED` |
| **(H1) `n₋(A_∞\|P_T) = 1` on `(T*_{∞,P}, T₂)`** | **`HYPOTHESIS`** — unchanged; no `T₂` produced |
| row-D label; endpoint of record | unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`); no sign for `ζ` beyond `log2` |

---

## §5 Proposal for Paper 47 (not applied here)

1. **`§8.4` (`prob:A`) gains a reduction and a floor.** Add Theorem AL and Corollary AL′ as a
 subsection of `§8`: they say that for the archimedean form the lattice class is not the obstruction
 — the deficit is the continuous one-sided problem — and they make the trade-off explicit
 (`edge error` vs `V_r M^{−r}`). Add the sentence: *by `thm:O` at `v = 0` the same non-attainment,
 with the same `K(u)~1/u` cause, holds with no primes at all, so Problem A's difficulty is the
 window edge and not the arithmetic.* This is the cleanest statement of the wall the paper has.
2. **`subsec:R` gains its first numbers.** `cor:R3` says the ceilings converge and leaves the rate
 open; §2.5 measures it in the archimedean case (`≈ 0.28 M^{−1.17}`, `T`-independent at `M ≥ 24`)
 and, via `prop:TK`, converts it into a `DIAGNOSTIC` **lower** bound on any `D` that answers
 `prob:A` — in particular `M^{−2}` is out. Worth a short `DIAGNOSTIC` paragraph with the table.
3. **`subsec:arch` gains Proposition NC.** It replaces the `HEURISTIC` half of the Landau–Widom
 remark by a proved, explicit negative-index bound, and records honestly that it overcounts by a
 factor `4`–`5` because `m` grows logarithmically. The remark on Connes–Consani's prolate
 compression is the natural place for it.
