# R184.007 — The needle in `b` at `T = log 2`: what it is and the theorem behind it

* Scope: (P153.4) of R153_005 and its replacement (P153.4′) from R153_008/010.
Minimal numerics in the session scratchpad (`n184.py`, `n2.py`), reusing unchanged the spectral assembly of
`phase-153.../scripts/audit/aud_spectral.py` and `scripts/round3/track2_needle.py`. RH is not claimed, nor the closure of D.*

## State

| # | Statement | Label |
|---|---|---|
| 0 | **Corpus check:** the question of the task was already answered in round 3 of phase 153 (R153_008, audited in R153_009, decided in R153_010). The "needle of width `10⁻⁷`" of R153_005 is **withdrawn ex officio**; this document independently reconfirms it and adds the weight-convexity theorem (§3). | `CITED` (R153_008–010) |
| 1 | Normalization: `Q_{log 3} = A_{log 2}` from Paper 42 `eq:localizedprimitiveoperator`; the `n = 4` term (shift `2T`) vanishes identically in `L²(−T,T)` at `T = log 2` | `PROVED` |
| 2 | `b ↦ λ_min(b)` is the lower envelope of analytic functions; `λ_min = min(λ_even, λ_odd)` (symmetry `t ↦ −t`); Hellmann–Feynman `dλ/db = −2w_3 c'_{F_b}(b)` | `PROVED` (R153_008 §2.1, restated) |
| 3 | The "needle" is an **exact even/odd crossing** with `O(1)` slopes (`+0.26`, `−0.58`), not a high-frequency minimizer; the positivity set in `b` is `N(log 2) ≈ (log 3 − 3.9·10⁻⁷, log 3 + 2.03·10⁻⁵)`, of length `≈ 2.1·10⁻⁵`; negative outside, converged for `K = 40…240` | `NUMERICAL` |
| 4 | `b = log 3` is **not** the only `b` with `Q_b ≥ 0`; it is not the argmax (`b* ≈ log 3 + 1.3·10⁻⁵`); (P153.4) has a **negative** answer | `NUMERICAL` (reconfirms R153_008; R153_010 closed it `CLOSED (negative)`) |
| 5 | **Theorem W (weight convexity).** For each `b`, `𝒲_b = {(w_2,w_3) : Q_{b;w_2,w_3} ≥ 0 on 𝒫_{log 2}}` is convex compact; `(w_2,w_3) ↦ λ_min` is concave; for each `(b,w_2)` the fiber in `w_3` is a compact interval | `PROVED` |
| 6 | At `b = log 3`, the weights of ζ lie in the **interior** of `𝒲_{log 3}`, at relative distance `≈ 7·10⁻⁶` (in `w_3`) and `≈ 1.4·10⁻⁶` (in `w_2`) from the **upper** boundary, and at `1.9·10⁻⁴` / `9.3·10⁻⁴` from the lower boundary | `NUMERICAL` |
| 7 | The intersection of the region `{(b,w_3)}` with `w_3 = Λ(3)/√3` is the interval `N(log 2)` of #3, not `{log 3}` | `NUMERICAL` (form) + `PROVED` (interval structure in `w_3`) |
| 8 | Does it move D? **No.** It refines "critical positivity at `log 2`" (phenomenon W2/Theorem M); it is transferable to neighboring weights (nonempty interior), hence blind to W4/W11 | `NO-GO` (as a lever for D) |

## 1. Definition and normalization

`T = log 2`, `I = (−T,T)`, `𝒫 = 𝒫_{log 2} = {F ∈ L²(I) : ∫F e^{±t/2} = 0}` (Paper 42 `main.tex` `subsec:primitiveendpoints`).
`S_b F(t) = F(t − b)` (extension by zero, restriction to `I`), `S_{±b} := S_b + S_{−b}`, `c_F(b) = ∫F(t)F(t+b)dt`, so that
`⟨S_{±b}F,F⟩ = 2c_F(b)` for `F` real. For `b ∈ (log 2, 2T]` and weights `w_2, w_3 ∈ ℝ`:

  `Q_{b;w_2,w_3} := G_{Γ,T} − m_0 − w_2 S_{±log 2} − w_3 S_{±b}`,  `w_p^ζ := Λ(p)/√p`.

In Fourier: `⟨QF,F⟩ = (1/2π)∫[Re ψ(¼+iτ/2) − log π − 2w_2cos(τ log 2) − 2w_3cos(τ b)]|F̂(τ)|²dτ`. (The `2Λ(p)/√p · cos`
convention of the task is the same: the factor 2 is the symmetrization.) With `w = w^ζ` and `b = log 3`, `Q` is the `A_T`
of Paper 42 at `T = log 2` (`thm:certifiedendpoints`, certified `≥ 0`; R153_005: `λ_min ∈ (0, 1.05·10⁻⁷]` in `L²`).

**Lemma 1.1 (the `n = 4` boundary).** At `T = log 2`, `log 4 = 2T` and `⟨S_{±2T}F,F⟩ = 0` for every `F ∈ L²(I)`. *Proof.* `S_{2T}F`
has support in `[T,3T]`, which meets `Ī` only at the point `{T}`, of measure zero. ∎ (`PROVED`.) Thus the convention `log n < 2T`
of Paper 42 and `log n ≤ 2T` give the same operator; the assembly does not include `n = 4` and is correct at the boundary.

## 2. Structure in `b`

**Prop. 2.1** (`PROVED`). (i) `λ_min(b) = inf_{‖F‖=1,F∈𝒫} [q_0(F) − 2w_3 c_F(b)]`, with `q_0` independent of `b`: lower
envelope of a family of functions of `b`, each `C^∞` in `b` when `F ∈ H¹`. (ii) `R F(t) = F(−t)` leaves `𝒫` invariant
(it swaps the two moments) and commutes with `Q`; hence `λ_min = min(λ_even, λ_odd)`. (iii) If the bottom of a block is simple
with eigenvector `F_b ∈ H¹`, `dλ/db = −2w_3 c'_{F_b}(b)`.

**On the requested Lipschitz bound.** In `L²` there is no uniform bound (`c'_F` requires `F'`). But this is not needed: the
hypothesis "needle ⟹ high-frequency minimizers" is **false** here. The slopes measured on both sides (`+0.26` even block,
`−0.58` odd block; R153_008 §2.1, verified there via Hellmann–Feynman to 3 digits) are `O(1)`. The narrowness is of
**level set**: a peak with `O(1)` slopes and height `≈ 3.5·10⁻⁶` above zero has a positive set of width
`≈ 2·10⁻⁵`; the value at `log 3` (`10⁻⁷`) is at `4·10⁻⁷` from the left boundary.

**Table 2.2** (`NUMERICAL`; Rayleigh–Ritz, sine basis, exact moments; the values are upper bounds on `λ_min`,
decreasing in `K`; quadrature noise `≈ 10⁻¹¹`, R153_008 §1). `λ_min(log 3 + d)`:

| `d` | K = 40 | K = 80 | K = 160 | K = 240 |
|---|---|---|---|---|
| `−10⁻³` | `−6.32e−4` | `−6.43e−4` | `−6.51e−4` | `−6.54e−4` |
| `−10⁻⁴` | `−3.34e−5` | `−3.39e−5` | `−3.43e−5` | `−3.45e−5` |
| `−10⁻⁵` | `−2.64e−6` | `−2.66e−6` | `−2.68e−6` | `−2.68e−6` |
| `−10⁻⁶` | `−1.53e−7` | `−1.59e−7` | `−1.64e−7` | `−1.67e−7` |
| `0` | `+1.165e−7` | `+1.114e−7` | `+1.068e−7` | `+1.044e−7` |
| `+10⁻⁶` | `+3.84e−7` | `+3.80e−7` | `+3.76e−7` | `+3.74e−7` |
| `+10⁻⁵` | `+2.73e−6` | `+2.73e−6` | `+2.73e−6` | `+2.73e−6` |
| `+3·10⁻⁵` | `−4.09e−6` | `−4.67e−6` | `−5.36e−6` | `−5.67e−6` |
| `+10⁻⁴` | `−4.55e−5` | `−4.59e−5` | `−4.64e−5` | `−4.66e−5` |
| `+10⁻³` | `−8.87e−4` | `−9.68e−4` | `−1.03e−3` | `−1.05e−3` |

At `d = 0` the bottom is even (`1.04·10⁻⁷`); the odd one is at `1.18·10⁻⁵` (K = 240). Roots (brentq): `N(log 2) =
(log 3 − 3.95·10⁻⁷, log 3 + 2.08·10⁻⁵)` (K = 160), `(log 3 − 3.85·10⁻⁷, log 3 + 2.03·10⁻⁵)` (K = 240). Since `λ_K ≥ λ_min`,
these intervals are **outer envelopes** of the true set (modulo quadrature). True shape: an asymmetric roof
with vertex at the even/odd crossing `b* ≈ log 3 + 1.3·10⁻⁵`, not a needle.

**Answer to 2(b).** `Q_b ≥ 0` on an interval (numerical) around `log 3`, but highly asymmetric: `log 3` sits in the
leftmost 2%. Neither "robust positivity in `b`" nor "exact arithmetic coincidence": `b = log 3` does not solve any
distinguished equation (the vertex `b*(T)` shifts with `T` and crosses `log 3` at `T_c ≈ 0.703 ± 0.001`, R153_009 #23).
The task's conjecture "`⟨S_{±b}v₁,v₁⟩` extremal at `log 3`" is refuted in R153_008 §2.3 (`c_{v₁}` is strictly
decreasing at `log 3`, `c' ≈ −0.26`).

## 3. Theorem W and the geometry of the cone in weights

**Theorem W** (`PROVED`). Fixing `T = log 2` and `b ∈ (log 2, 2T)`:
(a) `Λ(w_2,w_3) := λ_min(Q_{b;w_2,w_3}|𝒫)` is concave and 1-Lipschitz with respect to the norm `|w_2|‖S_{±log2}‖+|w_3|‖S_{±b}‖`;
(b) `𝒲_b := {Λ ≥ 0}` is convex and closed;
(c) `𝒲_b` is bounded, hence compact; in particular each fiber `{w_3 : (w_2,w_3) ∈ 𝒲_b}` is a compact interval.

*Proof.* (a) `Λ` is the infimum over `‖F‖ = 1` of `q_0(F) − 2w_2c_F(log 2) − 2w_3c_F(b)`, functions affine in `w`; the
infimum of affine functions is concave; `|c_F(b)| ≤ 1` gives Lipschitz. (b) upper level set of an upper semicontinuous
concave function. (c) It suffices to exhibit, for each direction `θ = (θ_2,θ_3) ≠ 0`, an `F ∈ 𝒫` with `θ_2c_F(log 2) + θ_3c_F(b) > 0`: then
`⟨QF,F⟩ → −∞` along `sθ`, `s → ∞`. Let `g ∈ C_c^∞` have support in an
interval of length `< (2T − b)/4` (and `< (b − log 2)/4`), and for a shift `h ∈ {log 2, b}` and sign `ε = ±1` let
`F_{h,ε} = g + εg(· − h)`, placed inside `I` (possible since `h < 2T`), corrected to `𝒫` by subtracting a combination of two
fixed `C_c^∞` functions `ρ_±` with far-away support (with autocorrelation at `log 2` and `b`
of size `O(δ)` if `ρ_±` is chosen with `δ`-small support and the correction has bounded amplitude). Then
`c_{F}(h) = ε‖g‖² + O(δ)` and `c_F(h') = O(δ)` for the other shift `h' ≠ h` (small supports, `|h − h'| >` diameters).
Choosing `h` and `ε` according to the sign of the larger component of `θ`, `θ·(c_F(log 2), c_F(b)) > 0`. ∎
(The construction requires `b ≠ log 2` and `b < 2T`; at `b = 2T` the `w_3` term disappears by Lemma 1.1 and `𝒲_b` ceases
to be bounded in `w_3`.)

**Corollary W′** (`PROVED`). The region `ℛ = {(b,w_3) : Q_{b;w_2^ζ,w_3} ≥ 0}` is closed and **convex in `w_3`** for each `b`;
it is not (nor is it claimed to be) convex in `b`.

**Data at `b = log 3`** (`NUMERICAL`, K = 160 / 240; in relative units `s_p = w_p/w_p^ζ`):

| fiber | positivity interval | position of ζ (`s = 1`) |
|---|---|---|
| `s_3` (with `s_2 = 1`) | `[0.999815, 1.0000070]` | at `7.0·10⁻⁶` from the upper boundary |
| `s_2` (with `s_3 = 1`) | `[0.999070, 1.0000014]` | at `1.4·10⁻⁶` from the upper boundary |
| `b` (with `s = (1,1)`) | `[log3 − 3.9·10⁻⁷, log3 + 2.03·10⁻⁵]` | at `3.9·10⁻⁷` from the left boundary |

**ζ's position.** ζ lies **inside** the convex set `𝒲_{log 3}`, pinned against its **upper** boundary: increasing any
prime weight by one part in `10⁶` destroys positivity; decreasing it by up to `10⁻⁴`–`10⁻³` relative preserves it. That
`𝒲` has nonempty interior around `(1,1)` means that **neighboring non-arithmetic weights are also positive**: positivity
at `log 2` does not separate ζ from its weight deformations.

**Relation to the Type I curve `s₂^c = 0.9997678`** (R162_2001/2190). It is **a different object**: a Type I contact
(`μ₂ = λ = ⟨u₂,φ̂⟩ = 0`) of the even block at `T_c ≈ 0.593 < log 2` on the two-atom comb, not the boundary of `𝒲` at
`T = log 2`. What is common is the phenomenon: ζ's weights sit at distance `10⁻⁴`–`10⁻⁶` from a degeneracy manifold of the
truncated positivity problem. `s₂^c < 1` there says nothing about ζ's position here; here the position is given by the
table (ζ interior, upper boundary at `1.4·10⁻⁶`). It is not claimed that both manifolds are the same.

## 4. Does it move D?

No. (i) Everything `PROVED` (Lemma 1.1, Prop. 2.1, Theorem W) is elementary convex/spectral structure, valid for any
comb of weights: it is blind to the arithmetic of `Λ` (W4) and does not couple primes and the archimedean part at every
`T` (W11). (ii) What is specific to ζ (that `(1,1)` lies inside `𝒲_{log 3}`) is exactly Paper 42 `thm:certifiedendpoints`;
what is new is only the **numerical quantification of criticality** (`10⁻⁶` in weights, `4·10⁻⁷` in position), which
refines W2/Theorem M ("positivity at `log 2` is critical") without giving a mechanism for `T > log 2`. (iii) The
reading "the positivity of two primes is an exact arithmetic coincidence at `b = log 3`" is now definitively ruled out.

**Correction to R153_005** (already ex officio by R153_010 §2; reiterated here): the "`b`-scan" row must read: *"`λ_min(b)`
is positive exactly on an interval `≈ (log 3 − 4·10⁻⁷, log 3 + 2.0·10⁻⁵)`, an asymmetric roof with vertex at the even/odd
crossing `b* ≈ log 3 + 1.3·10⁻⁵` and `O(1)` slopes; the 'width `10⁻⁷`' was the zero level of a near-critical peak; the
critical point is not the arithmetic contact."* `NUMERICAL`. R153_005 is not edited in this document.

## For the audit

1. **Duplication.** §2 reproduces R153_008; verify that it is not presented as new. What is new is §1 Lemma 1.1, §3 Theorem W and
   the weight table.
2. **Theorem W (c).** The correction to `𝒫` (two moments) in the proof is sketched: check that `ρ_±` with
   `δ`-small support and bounded amplitude exist (the functionals `e^{±t/2}` are linearly independent on any interval,
   so two bumps of support `δ` suffice with coefficients `O(1/δ)`·`O(‖g‖_{L¹})` — watch that their autocorrelation at `log 2`
   and `b` stays `O(δ)`: this requires placing the two bumps at a distance different from `log 2, b` from each other and from
   `supp g`). If it fails, (c) drops to `CONDITIONAL`; (a),(b) do not depend on it.
3. **Direction of the bounds.** The numerical positivity intervals are **outer** envelopes (Rayleigh–Ritz gives
   upper bounds on `λ_min`); it is not claimed that `log 3 ∈ N` numerically: that is Paper 42.
4. **Normalization.** No comparison is made with the Feshbach capacity margin `8.63·10⁻⁸` (forbidden by R153_004 #23).
5. **`s₂^c`.** Check that the Type I curve of R162 has not been identified with `∂𝒲_{log 3}`.
6. **FATAL.** No zero-free region, no moment bounds, no RH. Row D label unchanged.

## Note (R184_092)

* Numerics not converged (λ(log 3) decreases between K=160 and 240); margins are upper bounds. Interiority of ζ's weights is PROVED via Lipschitz (minimum margin ≈8e-8, consistent with λ_min≈1.05e-7). Theorem W(c) correct (cross terms exactly 0).
